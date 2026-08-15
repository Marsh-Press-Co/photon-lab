"""exp-033 -- The g600 Resolution Check (Block A only): measurement harness.
==============================================================================
Panel Iteration 10 (lead ELECTROMAGNETISM, rotation; synthesis: Director,
post Red Team's PROCEED-WITH-MANDATORY-FIXES verdict -- see design_geometry.py
module docstring and NOTES.md Phase 3 for the full accepted/overridden
record). Block B (radial_absorbed_power on beam-scene off_pass/off_bracket)
is CUT this cycle -- see design_geometry.py docstring.

Four sigma(I) OFF-state articles (off_bracket/off_pass/off_lab/off_field,
tau=0.003/0.0065/0.008/0.032) on exp-032's own +-35deg N=9 ambient bench,
RESCALED x1.5 (cpl 20->30, physical size held) -- this program's mandatory
R3 resolution check, at 600nm, the one wavelength never previously checked.

4 articles + empty = 5 scenes x 9 angles = 45 calls, + a 2-call settling
control (empty + off_pass @ theta=0, native STEPS=1400 vs this run's own
STEPS=2100) = 47 new FDTD calls total. No `lab/` change -- suite stays
46/46 fast-stage green (re-verified before results are read).

Predictions committed in NOTES.md BEFORE this file's first run (house
discipline, non-negotiable).
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


def build_ambient(article, sim):
    cx, cy = dg.OBJ
    x = np.arange(sim.nx)[:, None]
    y = np.arange(sim.ny)[None, :]
    mask = (x - cx) ** 2 + (y - cy) ** 2 <= dg.R_OUT ** 2
    sim.sigma_e[mask] += dg.SIGMA_BY_ARTICLE[article]
    sim.objects.append({"type": "uniform_sponge_disk",
                        "params": {"cx": cx, "cy": cy, "r": dg.R_OUT,
                                   "sigma": dg.SIGMA_BY_ARTICLE[article],
                                   "tau_center": dg.TAU_BY_ARTICLE[article]}})


def one_ambient_run(article, theta, steps):
    sim = Sim(dg.NX, dg.NY, cells_per_lambda=dg.CPL, courant_frac=0.99,
              absorb=dg.ABSORB)
    if article != "empty":
        build_ambient(article, sim)
    sim.add_line_source(dg.SRC_X, angle_deg=theta, edge=dg.TAPER, amplitude=1.0)
    sim.run(steps)
    return sc.full_capture(sim)


def run_ambient_group(args):
    lam_nm, theta, steps = args
    t0 = time.time()
    out = {}
    cap_e = one_ambient_run("empty", theta, steps)
    ph_e = sc.phasors(cap_e)
    prof_e = amb.observer_profile(ph_e, dg.PLANE_X, dg.ABSORB, dg.NY - dg.ABSORB)
    out["empty"] = {"profile": prof_e.tolist()}
    for art in dg.ARTICLES:
        cap = one_ambient_run(art, theta, steps)
        ph = sc.phasors(cap)
        prof = amb.observer_profile(ph, dg.PLANE_X, dg.ABSORB, dg.NY - dg.ABSORB)
        out[art] = {"profile": prof.tolist()}
    return (theta, steps, out, time.time() - t0)


def contrast(results, scenes_by_theta, article, angles, y_lo=dg.ABSORB):
    profs, e_profs = [], []
    for th in angles:
        grp = scenes_by_theta[th]
        profs.append(np.array(grp[article]["profile"]))
        e_profs.append(np.array(grp["empty"]["profile"]))
    weights = [1.0] * len(angles)
    return amb.contrast_from_runs(profs, e_profs, weights, y_lo,
                                  dg.OBJ[1], dg.W_OBJ, dg.GUARD_OUT, dg.W_FLANK)


def fit_free_line(taus, g_corrs):
    """Free two-parameter fit g_corr = A - B*tau (least squares). Returns
    (A, B, max_abs_residual). Mandatory fix per Red Team attack 16/4: NEVER
    impose the (4/3pi) chord coefficient -- it is refuted by the free fit on
    this bench's own native-cpl data (B/A=0.435 != 4/(3pi)=0.424, 2.5%,
    35x the fit's own residual scatter)."""
    taus = np.array(taus, dtype=float)
    g = np.array(g_corrs, dtype=float)
    # g = A - B*tau  <=>  g = A + (-B)*tau ; fit with polyfit degree 1
    coeffs = np.polyfit(taus, g, 1)   # [slope, intercept] = [-B, A]
    B, A = -coeffs[0], coeffs[1]
    fit_vals = A - B * taus
    max_resid = float(np.max(np.abs(g - fit_vals)))
    return float(A), float(B), max_resid


def main():
    print(f"exp-033 Block A: {len(dg.ARTICLES)} articles x {len(dg.FALLBACK_ANGLES)} angles "
          f"+ empty = {(len(dg.ARTICLES)+1)*len(dg.FALLBACK_ANGLES)} calls @ steps={dg.STEPS_AMBIENT}, "
          f"+ 2 settling-control calls @ steps={dg.STEPS_SETTLING_CONTROL}, "
          f"{os.cpu_count()} cpus", flush=True)
    t0 = time.time()

    # ---------------- main sweep, STEPS_AMBIENT (2100) ----------------
    main_args = [(600, float(th), dg.STEPS_AMBIENT) for th in dg.FALLBACK_ANGLES]
    scenes_by_theta = {}
    with ProcessPoolExecutor(max_workers=4) as ex:
        for theta, steps, out, dt in ex.map(run_ambient_group, main_args):
            scenes_by_theta[theta] = out
            print(f"  [main {len(scenes_by_theta):1d}/{len(main_args)}] theta={theta:+05.1f} "
                  f"({dt:5.1f} s)", flush=True)
    elapsed_main = time.time() - t0

    # ---------------- settling control, STEPS_SETTLING_CONTROL (1400), theta=0 only ----------------
    t1 = time.time()
    ctrl_theta, ctrl_steps, ctrl_out, ctrl_dt = run_ambient_group((600, 0.0, dg.STEPS_SETTLING_CONTROL))
    elapsed_settling = time.time() - t1
    print(f"  [settling-control] theta=0.0 steps={dg.STEPS_SETTLING_CONTROL} ({ctrl_dt:5.1f} s)", flush=True)

    elapsed = time.time() - t0
    print(f"exp-033 done in {elapsed:.0f} s ({elapsed_main:.0f}s main + {elapsed_settling:.0f}s settling)", flush=True)

    # ---------------- contrasts, N=9 (main sweep) ----------------
    table = {}
    r_empty = contrast(None, scenes_by_theta, "empty", dg.FALLBACK_ANGLES)
    fresh_floor_600 = abs(r_empty["C_empty"])
    for art in dg.ARTICLES:
        r = contrast(None, scenes_by_theta, art, dg.FALLBACK_ANGLES)
        table[art] = {"C": r["C"], "C_empty": r["C_empty"]}

    # ---------------- g_corr / g_raw, per article ----------------
    g_corr, g_raw = {}, {}
    for art in dg.ARTICLES:
        tau = dg.TAU_BY_ARTICLE[art]
        C, C_empty = table[art]["C"], table[art]["C_empty"]
        g_corr[art] = abs(C - C_empty) / tau
        g_raw[art] = abs(C) / tau

    # ---------------- free-curvature fit (mandatory: NOT the imposed 4/(3pi)) ----------------
    taus_sorted = [dg.TAU_BY_ARTICLE[a] for a in dg.ARTICLES]
    gcorr_sorted = [g_corr[a] for a in dg.ARTICLES]
    A_fit, B_fit, max_resid = fit_free_line(taus_sorted, gcorr_sorted)

    # ---------------- mandatory fixes 5/6: residual-gated R3 disposition ----------------
    residual_gate_pass = max_resid <= dg.RESIDUAL_GATE_4ARTICLE
    delta_A = abs(A_fit - dg.G0_ESTABLISHED_600_CPL20)
    if not residual_gate_pass:
        r3_disposition = "INCONCLUSIVE (residual gate failed -- data too noisy to trust A)"
    elif delta_A <= dg.A_CONFIRMED_BAND:
        r3_disposition = "CONFIRMED (resolution-invariant)"
    elif delta_A >= dg.A_ARTIFACT_BAND:
        r3_disposition = "ARTIFACT"
    else:
        r3_disposition = "INCONCLUSIVE (delta_A between confirmed and artifact bands)"

    # ---------------- mandatory fix 14: QUANTUM's Iteration-9 clause, retired + superseded ----------------
    quantum_clause_retired = {
        "original_iteration9_clause": "raw g600(off_pass) >= 0.69 flags anomaly-consistent",
        "retirement_reason": "dissolved by this cycle's own desk arithmetic before any run: "
                             "g_corr(600) for all 4 articles clusters at 0.686-0.689, BELOW "
                             "the 0.69 threshold -- the raw-g600 clause would never have fired "
                             "once the C_empty floor is subtracted; the apparent >=0.69 "
                             "'anomaly' was g0 showing through the lambda-dependence of the "
                             "empty-scene floor, not a physical effect.",
        "successor_clause_g_corr_currency": "the 600nm channel is anomaly-consistent iff "
                                            "EITHER the fit-residual gate fails OR "
                                            f"delta_A >= {dg.A_ARTIFACT_BAND} (the ARTIFACT band) "
                                            "-- i.e. iff this cycle's own R3 check flags artifact "
                                            "or data-quality failure. A CONFIRMED result licenses "
                                            "g0~0.6889 as resolution-stable at 600nm and formally "
                                            "closes the raw-g600 anomaly question.",
        "this_run_disposition": r3_disposition,
    }

    # ---------------- mandatory fix 13: scoring currency declared (VISION P-VIS-0(i)) ----------------
    def score(c):
        ac = abs(c)
        if ac < 0.005:
            return "PASS"
        elif ac < 0.02:
            return "MARGINAL"
        return "FAIL"

    ladder_raw_C = {art: score(table[art]["C"]) for art in dg.ARTICLES}
    ladder_g_corr_corrected_C_SENSITIVITY_ONLY = {
        art: score(-g_corr[art] * dg.TAU_BY_ARTICLE[art]) for art in dg.ARTICLES}

    # ---------------- settling control ----------------
    r_empty_ctrl = amb.contrast_from_runs(
        [np.array(ctrl_out["empty"]["profile"])], [np.array(ctrl_out["empty"]["profile"])],
        [1.0], dg.ABSORB, dg.OBJ[1], dg.W_OBJ, dg.GUARD_OUT, dg.W_FLANK)
    r_pass_ctrl = amb.contrast_from_runs(
        [np.array(ctrl_out["off_pass"]["profile"])], [np.array(ctrl_out["empty"]["profile"])],
        [1.0], dg.ABSORB, dg.OBJ[1], dg.W_OBJ, dg.GUARD_OUT, dg.W_FLANK)
    r_pass_main_theta0 = amb.contrast_from_runs(
        [np.array(scenes_by_theta[0.0]["off_pass"]["profile"])],
        [np.array(scenes_by_theta[0.0]["empty"]["profile"])],
        [1.0], dg.ABSORB, dg.OBJ[1], dg.W_OBJ, dg.GUARD_OUT, dg.W_FLANK)
    c_ctrl_1400 = r_pass_ctrl["C"]
    c_main_2100 = r_pass_main_theta0["C"]
    settling_rel_delta = abs(c_ctrl_1400 - c_main_2100) / abs(c_main_2100) if c_main_2100 else float("nan")

    # ---------------- mandatory fix 10: THERMO sidecar (post-run analytic, chord model) ----------------
    import math
    def chord_absorptance(tau):
        return (math.pi / 4.0) * tau * (1.0 - (4.0 / (3.0 * math.pi)) * tau)
    thermo_sidecar = {
        "label": "POST-RUN ANALYTIC, NOT AN FDTD OUTPUT (expressibility contract)",
        "absorbed_fraction_chord_model": {art: chord_absorptance(dg.TAU_BY_ARTICLE[art])
                                          for art in dg.ARTICLES},
        "off_pass_steady_state_dT_K": 8.17e-4,
        "off_pass_transient_dT_K_by_dwell_s": {"0.1": 6.9e-5, "0.5": 3.46e-4, "1.0": 6.92e-4},
        "microbolometer_NETD_K_band": [0.020, 0.050],
        "off_state_detectability": "UNDETECTABLE at every dwell tested -- 30-700x below NETD "
                                   "even at steady state, and the phenomenon is a SWEPT beam "
                                   "(constraint 4): transient dwell-limited DeltaT is the "
                                   "physically apt number, not steady-state.",
        "on_endpoint_lwir_claim": "HELD AT HYPOTHESIS-NOT-RESULT (Red Team attack 11): steady-"
                                  "state estimate ~0.15K (2-5x above NETD) INVERTS once "
                                  "swept-beam dwell is applied (same scaling as off_pass "
                                  "would put transient DeltaT far below steady-state); dwell "
                                  "time, parcel geometry, and host phase (MATERIALS restricts "
                                  "off_pass's realizable host to dilute vapour/aerosol, where "
                                  "graybody radiative-equilibrium is the wrong model) are all "
                                  "unpinned. Not scored. Docket #7 (sourced witness-scenario "
                                  "table) would resolve this; still deprioritized behind T13.",
    }

    out = {
        "meta": {
            "geometry": {k: getattr(dg, k) for k in
                        ("NX", "NY", "ABSORB", "SRC_X", "OBJ", "R_OUT", "PLANE_X",
                         "W_OBJ", "GUARD_OUT", "W_FLANK", "BOX", "CPL", "CPL_NATIVE")},
            "fallback_angles": list(dg.FALLBACK_ANGLES),
            "tau": dg.TAU_BY_ARTICLE, "sigma": dg.SIGMA_BY_ARTICLE,
            "decision_floor_corrected_equal_weighted": dg.DECISION_FLOOR_NATIVE_CPL20,
            "established_fit_600nm_cpl20": {"A_g0": dg.G0_ESTABLISHED_600_CPL20,
                                            "B": dg.B_ESTABLISHED_600_CPL20},
            "eps_r_idealization_note": dg.EPS_R_IDEALIZATION_NOTE,
            "block_b_status": "CUT THIS CYCLE -- see design_geometry.py docstring and NOTES.md "
                              "Phase 3 (Red Team's sanctioned fallback; PHOTONICS' "
                              "structurally-underpowered attack, independently confirmed).",
            "elapsed_s": elapsed, "elapsed_s_main": elapsed_main,
            "elapsed_s_settling": elapsed_settling, "n_new_runs": 45 + 2,
        },
        "ambient_contrasts": table,
        "fresh_empty_decision_floor_600_cpl30": fresh_floor_600,
        "g_corr": g_corr, "g_raw": g_raw,
        "free_curvature_fit": {"A_g0": A_fit, "B": B_fit, "max_residual": max_resid,
                               "residual_gate_threshold": dg.RESIDUAL_GATE_4ARTICLE,
                               "residual_gate_pass": residual_gate_pass,
                               "delta_A_vs_established": delta_A,
                               "confirmed_band": dg.A_CONFIRMED_BAND,
                               "artifact_band": dg.A_ARTIFACT_BAND,
                               "disposition": r3_disposition},
        "quantum_disposition_clause_retirement": quantum_clause_retired,
        "vision_ladder_raw_C_SCORED": ladder_raw_C,
        "vision_ladder_g_corr_corrected_C_SENSITIVITY_ONLY_not_scored": ladder_g_corr_corrected_C_SENSITIVITY_ONLY,
        "settling_control": {"C_1400steps": c_ctrl_1400, "C_2100steps_main_theta0": c_main_2100,
                             "relative_delta": settling_rel_delta, "band": 0.03},
        "thermo_sidecar_analytic": thermo_sidecar,
    }
    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(out, f, indent=1)

    print("\nambient Weber contrast C @600nm, cpl=30 (N=9 fallback):")
    for art in dg.ARTICLES:
        print(f"  {art:12s} tau={dg.TAU_BY_ARTICLE[art]:.4f}  C={table[art]['C']:+.5f}  "
              f"[raw-C ladder: {ladder_raw_C[art]}]  g_corr={g_corr[art]:.4f}  g_raw={g_raw[art]:.4f}")
    print(f"\nfresh empty decision floor @600nm/cpl30: {fresh_floor_600:.6e} "
          f"(established @cpl20, equal-wt: {dg.DECISION_FLOOR_NATIVE_CPL20[600]:.6e})")
    print(f"\nfree-curvature fit: A(g0)={A_fit:.6f} B={B_fit:.6f} max_residual={max_resid:.6e} "
          f"(gate <= {dg.RESIDUAL_GATE_4ARTICLE})")
    print(f"vs established A(g0)={dg.G0_ESTABLISHED_600_CPL20} (cpl=20): delta_A={delta_A:.6f}")
    print(f"R3 DISPOSITION: {r3_disposition}")
    print(f"\nQUANTUM clause: {quantum_clause_retired['successor_clause_g_corr_currency']}")
    print(f"  this run's disposition: {r3_disposition}")
    print(f"\nsettling control: C(1400 steps)={c_ctrl_1400:+.5f}  C(2100 steps, main theta=0)={c_main_2100:+.5f}  "
          f"relative_delta={settling_rel_delta:.4f} (band <=0.03)")
    print(f"\nTHERMO sidecar (analytic, not FDTD): off_pass steady dT={thermo_sidecar['off_pass_steady_state_dT_K']:.2e} K, "
          f"transient (1s dwell) dT={thermo_sidecar['off_pass_transient_dT_K_by_dwell_s']['1.0']:.2e} K "
          f"-- {thermo_sidecar['off_state_detectability']}")
    print("\nresults.json written")


if __name__ == "__main__":
    main()
