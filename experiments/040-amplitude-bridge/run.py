"""exp-040 -- The Amplitude Bridge: measurement harness.
===========================================================
Panel Iteration 17 (lead THERMODYNAMICS; synthesis: Director, post Red
Team's proceed-with-mandatory-fixes -- the densest single-cycle Phase-2
catch-set this program has produced: 16 numbered Red Team attacks, 12
load-bearing fixes (L1-L12) adopted, 10 correctable-with-disclosure (C1-
C10) applied, 5 explicit overreach rejections (O1-O5) that would have
5x'd this cycle's scope). Full transcript: LOGBOOK.md Iteration 17.

Two FDTD blocks, both scoring `lab.amplitude_bridge.chord_contrast`
against measured data for the FIRST time anywhere in this program's
history at tau in the never-before-measured saturation shoulder
(tau in [0.3, 2]):

  Block V -- two new static, index-matched (eps_r=1) uniform sponge
    disks, v1 (tau=TAU_V1, sitting AT the Tier-W p=0.4 night-lab bar)
    and v2 (tau=TAU_V2, AT the Tier-W p=0.5 bar), on exp-026's own
    +-35deg N=9 fallback bench, at BOTH 600nm (the proposal's own
    primary) AND 450nm (Red Team's one approved run-adding fix, L12:
    Tier-W is a SCOTOPIC bar and V'(450)/V'(600)=13.8 -- inheriting
    600nm-only lambda-flatness into the shoulder was ruled unsupported).
    9 angles x (2 articles + empty) x 2 lambda = 54 runs.

  Block R -- the mandatory R3 resolution check (this program's own
    precedent, exp-005/010/015/023/033 et al.) on v2 alone, cpl 20->30,
    at exp-033's own committed x1.5-rescaled geometry (R_OUT=117).
    sigma is recomputed from THIS block's OWN r_out (Red Team attack #2,
    load-bearing -- copying Block V's sigma verbatim would silently
    drift tau by +50% and fire this very gate as a false artifact,
    exp-027's own published erratum class repeating). 9 angles x
    (1 article + empty) = 18 runs.

Total NEW FDTD runs: 54 + 18 = 72. Predictions committed in NOTES.md
BEFORE this file's first run (house discipline, non-negotiable).
"""

import json
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..")))
sys.path.insert(0, HERE)

import design_geometry as dg
from lab import Sim, ambient as amb, sections as sc
from lab import amplitude_bridge as ab


def build_disk(article, sim, obj, r_out, sigma):
    cx, cy = obj
    x = np.arange(sim.nx)[:, None]
    y = np.arange(sim.ny)[None, :]
    mask = (x - cx) ** 2 + (y - cy) ** 2 <= r_out ** 2
    sim.sigma_e[mask] += sigma
    sim.objects.append({"type": "uniform_sponge_disk",
                        "params": {"cx": cx, "cy": cy, "r": r_out, "sigma": sigma}})


# ------------------------------------------------------------- Block V (54 runs)

def one_v_run(article, theta, cpl):
    sim = Sim(dg.V_NX, dg.V_NY, cells_per_lambda=cpl, courant_frac=0.99,
              absorb=dg.V_ABSORB)
    if article != "empty":
        build_disk(article, sim, dg.V_OBJ, dg.V_R_OUT, dg.SIGMA_BY_ARTICLE_V[article])
    sim.add_line_source(dg.V_SRC_X, angle_deg=theta, edge=dg.V_TAPER, amplitude=1.0)
    sim.run(dg.V_STEPS_AMBIENT)
    return sc.full_capture(sim)


def run_v_group(args):
    lam_nm, cpl, theta = args
    t0 = time.time()
    out = {}
    cap_e = one_v_run("empty", theta, cpl)
    ph_e = sc.phasors(cap_e)
    prof_e = amb.observer_profile(ph_e, dg.V_PLANE_X, dg.V_ABSORB, dg.V_NY - dg.V_ABSORB)
    out["empty"] = {"profile": prof_e.tolist()}
    for art in dg.ARTICLES_V:
        cap = one_v_run(art, theta, cpl)
        ph = sc.phasors(cap)
        prof = amb.observer_profile(ph, dg.V_PLANE_X, dg.V_ABSORB, dg.V_NY - dg.V_ABSORB)
        out[art] = {"profile": prof.tolist()}
    return (lam_nm, theta, out, time.time() - t0)


# ------------------------------------------------------------- Block R (18 runs)

def one_r_run(article, theta):
    sim = Sim(dg.R_NX, dg.R_NY, cells_per_lambda=dg.R_CPL, courant_frac=0.99,
              absorb=dg.R_ABSORB)
    if article != "empty":
        build_disk(article, sim, dg.R_OBJ, dg.R_R_OUT, dg.SIGMA_BY_ARTICLE_R[article])
    sim.add_line_source(dg.R_SRC_X, angle_deg=theta, edge=dg.R_TAPER, amplitude=1.0)
    sim.run(dg.R_STEPS_AMBIENT)
    return sc.full_capture(sim)


def run_r_group(theta):
    t0 = time.time()
    out = {}
    cap_e = one_r_run("empty", theta)
    ph_e = sc.phasors(cap_e)
    prof_e = amb.observer_profile(ph_e, dg.R_PLANE_X, dg.R_ABSORB, dg.R_NY - dg.R_ABSORB)
    out["empty"] = {"profile": prof_e.tolist()}
    for art in dg.ARTICLES_R:
        cap = one_r_run(art, theta)
        ph = sc.phasors(cap)
        prof = amb.observer_profile(ph, dg.R_PLANE_X, dg.R_ABSORB, dg.R_NY - dg.R_ABSORB)
        out[art] = {"profile": prof.tolist()}
    return (theta, out, time.time() - t0)


def contrast_v(results, article, lam_nm, cpl):
    profs, e_profs = [], []
    for th in dg.V_ANGLES:
        grp = results[(lam_nm, th)]
        profs.append(np.array(grp[article]["profile"]))
        e_profs.append(np.array(grp["empty"]["profile"]))
    weights = [1.0] * len(dg.V_ANGLES)
    return amb.contrast_from_runs(profs, e_profs, weights, dg.V_ABSORB,
                                  dg.V_OBJ[1], dg.V_W_OBJ, dg.V_GUARD_OUT, dg.V_W_FLANK)


def contrast_r(results, article):
    profs, e_profs = [], []
    for th in dg.R_ANGLES:
        grp = results[th]
        profs.append(np.array(grp[article]["profile"]))
        e_profs.append(np.array(grp["empty"]["profile"]))
    weights = [1.0] * len(dg.R_ANGLES)
    return amb.contrast_from_runs(profs, e_profs, weights, dg.R_ABSORB,
                                  dg.R_OBJ[1], dg.R_W_OBJ, dg.R_GUARD_OUT, dg.R_W_FLANK)


def main():
    t_start = time.time()

    # ---------------- Block V (54 runs) -------------------------------
    groups_v = [(lam_nm, cpl, float(th))
                for lam_nm, cpl in dg.V_CPL.items() for th in dg.V_ANGLES]
    print(f"exp-040 Block V: {len(groups_v)} groups ({len(groups_v) * 3} runs incl. empty), "
          f"{os.cpu_count()} cpus", flush=True)
    t0 = time.time()
    v_results = {}
    with ProcessPoolExecutor(max_workers=4) as ex:
        for lam_nm, theta, out, dt in ex.map(run_v_group, groups_v):
            v_results[(lam_nm, theta)] = out
            print(f"  V [{len(v_results):2d}/{len(groups_v)}] lambda={lam_nm} "
                  f"theta={theta:+05.1f} ({dt:5.1f} s)", flush=True)
    elapsed_v = time.time() - t0
    print(f"Block V done in {elapsed_v:.0f} s", flush=True)

    # ---------------- Block R (18 runs) -------------------------------
    print(f"exp-040 Block R: {len(dg.R_ANGLES)} groups ({len(dg.R_ANGLES) * 2} runs incl. empty)",
          flush=True)
    t0 = time.time()
    r_results = {}
    with ProcessPoolExecutor(max_workers=4) as ex:
        for theta, out, dt in ex.map(run_r_group, [float(t) for t in dg.R_ANGLES]):
            r_results[theta] = out
            print(f"  R [{len(r_results):2d}/{len(dg.R_ANGLES)}] theta={theta:+05.1f} "
                  f"({dt:5.1f} s)", flush=True)
    elapsed_r = time.time() - t0
    print(f"Block R done in {elapsed_r:.0f} s", flush=True)

    # ---------------- assemble + score ---------------------------------
    table = {}
    for lam_nm, cpl in dg.V_CPL.items():
        table[lam_nm] = {}
        for art in ("empty",) + dg.ARTICLES_V:
            r = contrast_v(v_results, art, lam_nm, cpl)
            table[lam_nm][art] = {"C": r["C"], "C_empty": r["C_empty"]}

    r_block = {}
    for art in ("empty",) + dg.ARTICLES_R:
        r = contrast_r(r_results, art)
        r_block[art] = {"C": r["C"], "C_empty": r["C_empty"]}

    # ---- predictions, committed BEFORE this run in NOTES.md -- scored here
    def pct(x):
        return f"{x:+.2%}"

    C_V1_model = ab.chord_contrast(dg.TAU_V1, dg.V_R_OUT, dg.V_PLANE_DX, dg.V_ANGLES,
                                   dg.V_GUARD_OUT, dg.V_W_FLANK)
    C_V2_model = ab.chord_contrast(dg.TAU_V2, dg.V_R_OUT, dg.V_PLANE_DX, dg.V_ANGLES,
                                   dg.V_GUARD_OUT, dg.V_W_FLANK)
    C_R_model = ab.chord_contrast(dg.TAU_V2, dg.R_R_OUT, dg.R_PLANE_DX, dg.R_ANGLES,
                                  dg.R_GUARD_OUT, dg.R_W_FLANK)

    v1_600 = abs(table[600]["v1"]["C"])
    v1_450 = abs(table[450]["v1"]["C"])
    v2_600 = abs(table[600]["v2"]["C"])
    v2_450 = abs(table[450]["v2"]["C"])
    r_v2 = abs(r_block["v2"]["C"])

    def rel_err(measured, model):
        return abs(measured - model) / abs(model)

    def within(rel, band):
        return rel <= band

    predictions = []

    predictions.append({
        "id": "P-EXP040-1a [amplitude-only -- not a Tier-W or Tier-A constraint-3 verdict; "
              "bench-scale, N9-quadrature-uncorrected (T16), 600nm]",
        "claim": "chord model reproduces measured |C(v1, 600nm)| in the never-before-measured "
                 "shoulder (tau=TAU_V1, the Tier-W p=0.4 bar)",
        "model": C_V1_model, "measured": v1_600, "rel_err": rel_err(v1_600, C_V1_model),
        "band": 0.10,
        "verdict": "CONFIRMED" if within(rel_err(v1_600, C_V1_model), 0.10) else
                   ("PARTIAL" if within(rel_err(v1_600, C_V1_model), 0.20) else "REFUTED"),
    })
    predictions.append({
        "id": "P-EXP040-1b [amplitude-only -- not a Tier-W or Tier-A constraint-3 verdict; "
              "bench-scale, N9-quadrature-uncorrected (T16), 600nm]",
        "claim": "chord model reproduces measured |C(v2, 600nm)| in the shoulder (tau=TAU_V2, "
                 "the Tier-W p=0.5 bar)",
        "model": C_V2_model, "measured": v2_600, "rel_err": rel_err(v2_600, C_V2_model),
        "band": 0.10,
        "verdict": "CONFIRMED" if within(rel_err(v2_600, C_V2_model), 0.10) else
                   ("PARTIAL" if within(rel_err(v2_600, C_V2_model), 0.20) else "REFUTED"),
    })

    chrom_v1 = abs(v1_600 - v1_450) / ((v1_600 + v1_450) / 2.0)
    chrom_v2 = abs(v2_600 - v2_450) / ((v2_600 + v2_450) / 2.0)
    predictions.append({
        "id": "P-EXP040-2a [amplitude-only -- not a Tier-W or Tier-A constraint-3 verdict; "
              "bench-scale, N9-quadrature-uncorrected (T16); PHOTONICS/VISION L12]",
        "claim": "chromatic spread at v1 (shoulder) is smaller than exp-026's own off_lab "
                 "endpoint spread (~16.8% relative) -- band <=8% relative, reflecting decay "
                 "toward the ON endpoint's small (~0.4%) spread as tau grows",
        "measured_600": v1_600, "measured_450": v1_450, "relative_spread": chrom_v1,
        "band": 0.08,
        "verdict": "CONFIRMED" if chrom_v1 <= 0.08 else
                   ("PARTIAL" if chrom_v1 <= 0.168 else "REFUTED"),
    })
    predictions.append({
        "id": "P-EXP040-2b [amplitude-only -- not a Tier-W or Tier-A constraint-3 verdict; "
              "bench-scale, N9-quadrature-uncorrected (T16); PHOTONICS/VISION L12]",
        "claim": "chromatic spread at v2 (deeper in the shoulder, closer to ON) is smaller "
                 "still -- band <=4% relative",
        "measured_600": v2_600, "measured_450": v2_450, "relative_spread": chrom_v2,
        "band": 0.04,
        "verdict": "CONFIRMED" if chrom_v2 <= 0.04 else
                   ("PARTIAL" if chrom_v2 <= 0.10 else "REFUTED"),
    })

    r3_rel = abs(r_v2 - v2_600) / abs(v2_600)
    predictions.append({
        "id": "P-EXP040-3 [R3 resolution check, mandatory -- Red Team attack #2 fix (L2) live-tested]",
        "claim": "cpl 20->30 R3 check on v2: |C(cpl30)-C(cpl20)|/|C| <=4% (Phase-1 proposal's "
                 "own gate, preserved) -- central estimate ~2%, informed by this bench's own "
                 "established g_raw cpl-sensitivity (off_pass: 0.6927->0.7056, ~1.9%)",
        "model_predicted_geometric_shift": abs(C_R_model - C_V2_model) / abs(C_V2_model),
        "measured_cpl20": v2_600, "measured_cpl30": r_v2, "rel_shift": r3_rel,
        "band": 0.04,
        "verdict": "CONFIRMED" if r3_rel <= 0.04 else "REFUTED (ARTIFACT-CANDIDATE, T15/T16-relevant)",
    })

    # ---- n_ss ceiling table (Red Team L5+L7+L6+L9 -- desk, zero-cost, computed here for
    # the record; not itself a "prediction" scored against a run, so not in `predictions`)
    def ceiling_row(c_thr_center, tau_on=3.9):
        c_lo, c_hi = c_thr_center / (10 ** 0.3), c_thr_center * (10 ** 0.3)
        row = {}
        for tag, c in (("lo", c_lo), ("center", c_thr_center), ("hi", c_hi)):
            t = ab.tau_thr_from_c_thr(c, dg.V_R_OUT, dg.V_PLANE_DX, dg.V_ANGLES,
                                      dg.V_GUARD_OUT, dg.V_W_FLANK)
            if t is None:
                row[tag] = {"C_thr": c, "tau_thr": None, "n_ss_Dinf": None,
                           "n_ss_finite_D_0p008": None, "note": "NO BAR (exceeds asymptote)"}
            else:
                row[tag] = {"C_thr": c, "tau_thr": t,
                           "n_ss_Dinf": ab.n_ss_ceiling(t, tau_on, 0.0),
                           "n_ss_finite_D_0p008": ab.n_ss_ceiling(t, tau_on, 0.008),
                           "n_ss_finite_D_0p0065": ab.n_ss_ceiling(t, tau_on, 0.0065)}
        return row

    ceiling_table = {
        "tier_A_lab": ceiling_row(0.005),
        "tier_A_field": ceiling_row(0.02),
        "tier_W_p04_night_lab_bystander": ceiling_row(dg.C_THR_P04),
        "tier_W_p05_night_lab_bystander": ceiling_row(dg.C_THR_P05),
        "note": ("Tier-W rows here are the DARK-ADAPTED-BYSTANDER bar, NOT true PANEL.md Tier "
                 "W (Red Team attack #5 / VISION L8) -- the flashlight holder's own Stiles-"
                 "Holladay self-glare (LOGBOOK Iteration-1 sidecar) elevates the actual Tier-W "
                 "bar 12-80x looser (no bar at all), so these rows are CONSERVATIVE, not the "
                 "reported scene's own regime. True Tier W stays unscored pending docket #7."),
    }

    dual_g_table = {
        "chord_model_g0": 0.6857163680484835,
        "measured_g_N9_r78native_cpl30": 0.705609358926726,
        "measured_g_N17_r78native_cpl30": 0.805945917,
        "note": ("Red Team attack #16 / L10: the bridge's OWN transfer function predicts a "
                 "-3.3% N9->N17 shift (angular-quadrature term is FRACTIONAL, confirmed across "
                 "a 317x tau span) but the one REAL N9->N17 measurement at this geometry shows "
                 "+14.2% -- opposite sign, 4.3x magnitude. At minimum 100% of the measured "
                 "shift is non-chord physics (T16's open near-field-fringe candidate and/or "
                 "the still-unexplained +-40deg-specific artifact). Neither the additive nor "
                 "the fractional extrapolation of this shift into the shoulder tau range is "
                 "licensed by evidence -- disclosed as open T16, not resolved this cycle."),
    }

    a_req_table = []
    for f_peak, tau_peak, behind in ((0.5, 1.95, 0.142), (0.9, 3.51, 0.030),
                                      (0.99, 3.861, 0.021)):
        n_ss = ceiling_table["tier_A_lab"]["center"]["n_ss_Dinf"]
        a_req_table.append({
            "f_peak": f_peak, "tau_peak": tau_peak, "beam_behind_at_peak": behind,
            "A_req_Dinf_tierA_lab": ab.a_req(f_peak, n_ss),
        })

    out = {
        "experiment": "exp-040-amplitude-bridge",
        "panel_iteration": 17,
        "lead": "THERMODYNAMICS",
        "block_v": table,
        "block_r": r_block,
        "predictions": predictions,
        "n_ss_ceiling_table": ceiling_table,
        "dual_g_table": dual_g_table,
        "a_req_table_note": ("A_req diverges as f_peak->1 (Red Team attack #1, load-bearing "
                             "L3) -- the witness's I_beam/I_ambient~5e3 is UNSOURCED "
                             "(idealization 11, docket #7) and is NOT reported here as a "
                             "cleared margin at any f_peak."),
        "a_req_table": a_req_table,
        "block_v_runs": len(groups_v) * 3, "block_r_runs": len(dg.R_ANGLES) * 2,
        "elapsed_v_s": elapsed_v, "elapsed_r_s": elapsed_r,
        "elapsed_total_s": time.time() - t_start,
    }

    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(out, f, indent=2, default=float)

    n_confirmed = sum(1 for v in predictions if v["verdict"] == "CONFIRMED")
    print(f"\nexp-040: {n_confirmed}/{len(predictions)} predictions CONFIRMED")
    for v in predictions:
        print(f"  [{v['verdict']}] {v['id'][:60]}...: {v['claim'][:90]}")
    print(f"elapsed: {out['elapsed_total_s']:.2f}s "
          f"(block V {elapsed_v:.1f}s, block R {elapsed_r:.1f}s)")


if __name__ == "__main__":
    main()
