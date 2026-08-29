"""exp-088 -- T28 Node Bracket + R13 Floor Gate: the decisive theta=38.4/
38.8deg bracketing follow-up around exp-087's theta=38.6deg
ENERGY-DOMINANT spike, plus R13's new denominator floor gate applied both
forward (new points) and retroactively (exp-087's own three points).
=============================================================================
Panel Iteration 65 (lead: QUANTUM OPTICS, by rotation). Frozen spec:
phase3_synthesis.md (all 10 Phase-2 Red Team mandatory-fix-docket items
adopted, zero overridden). Predictions (NOTES.md Q1-Q7 + the non-negativity
gate) committed to git strictly BEFORE this file's first run (house
discipline, non-negotiable).

Reuses exp-087's own `_load()` idiom (itself chaining through exp-083's
`run.py` for `dg`/`build_article`/`_run_sim`), `box_for`/`ref_for`,
`widths_direction_corrected()`, `_label`/`classify_resolved()` VERBATIM,
UNMODIFIED -- zero geometry retyped, zero `lab/` diff. New code: two new
angles (38.4/38.8deg), the R13 floor gate (FLOOR = FLOOR_FRAC x
RMS[frac_contrast] over exp-083's own 31-point window, computed entirely
from already-committed JSON), its retroactive application to exp-087's own
three points, and (Phase-2 fix items 7-8) the NETD/T9-anchor extension to
the two new angles, reusing the thermo chain already required for the
PRIMARY metric.
"""

import importlib.util
import json
import math
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, ROOT)


def _load(path, name):
    """House `_load()` pattern (exp-078..087's own idiom for cross-
    experiment-directory imports)."""
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


EXP083_DIR = os.path.join(ROOT, "experiments", "083-t28-pad-article-full-power-retest")
EXP083_RESULTS = os.path.join(EXP083_DIR, "results.json")
EXP087_DIR = os.path.join(ROOT, "experiments", "087-t28-energy-interception-poynting-check")
EXP087_RESULTS = os.path.join(EXP087_DIR, "results.json")

# exp-087's own run.py: reuses exp-083's `_load()` idiom for dg/build_article/
# _run_sim, and defines box_for/ref_for/widths_direction_corrected/_label/
# classify_resolved. Loaded here, reused verbatim (not retyped).
exp087 = _load(os.path.join(EXP087_DIR, "run.py"), "_exp088_exp087")
dg = exp087.dg
build_article = exp087.build_article
_run_sim = exp087._run_sim
box_for = exp087.box_for
ref_for = exp087.ref_for
widths_direction_corrected = exp087.widths_direction_corrected
_label = exp087._label
classify_resolved = exp087.classify_resolved

from lab import Sim, sections as sc, ambient as amb, thermo_sidecar as ts  # noqa: E402

PAIR_KEYS = ("C40", "G40")
ANGLES = [dg.DENSE_ANGLES[12], dg.DENSE_ANGLES[14]]  # 38.4, 38.8
assert ANGLES == [38.4, 38.8], f"angle grid drifted: {ANGLES}"
STEPS_MAIN = dg.STEPS_SETTLED  # 2800, unchanged from exp-087 (Idealization 7: no new settling check)

BOX_CLEARANCE_A = exp087.BOX_CLEARANCE_A   # R_OUT+12
BOX_CLEARANCE_B = exp087.BOX_CLEARANCE_B   # R_OUT+24
R_OUT_CELLS = dg.R_OUT

DX_M = exp087.DX_M
L_GEOMETRIC_M = exp087.L_GEOMETRIC_M
IRR_CENTRAL_W_CM2 = exp087.IRR_CENTRAL_W_CM2
K_AIR = exp087.K_AIR
DENSITY_SI_KG_M3, C_P_SI_J_KGK = exp087.DENSITY_SI_KG_M3, exp087.C_P_SI_J_KGK
EMISSIVITY = exp087.EMISSIVITY
T_AMBIENT_K = exp087.T_AMBIENT_K
NETD_BAND_K = exp087.NETD_BAND_K
BIOT_SWING_X, H_CONV_SWING_X = exp087.BIOT_SWING_X, exp087.H_CONV_SWING_X

XI_TOL = exp087.XI_TOL
NOISE_MULT = exp087.NOISE_MULT
RATIO_LOW, RATIO_HIGH = exp087.RATIO_LOW, exp087.RATIO_HIGH

# --------------------------------------------------------------- R13 floor gate
FLOOR_FRAC = 0.10   # house-style, disclosed (NOTES.md Idealization 8 / R13 section)


def frac_contrast_of(per_theta, key_th):
    row = per_theta[key_th]
    return abs(row["delta_scene"]) / abs(row["C40_C"])


def compute_floor():
    """FLOOR = FLOOR_FRAC x RMS[frac_contrast(theta)] over exp-083's own
    committed 31-point window. Zero new FDTD -- entirely desk-computable
    from already-committed JSON (NOTES.md's own R13-floor-gate section)."""
    with open(EXP083_RESULTS) as f:
        res83 = json.load(f)
    per_theta_83 = res83["per_theta"]
    vals = [frac_contrast_of(per_theta_83, k) for k in per_theta_83]
    rms = math.sqrt(sum(v * v for v in vals) / len(vals))
    floor = FLOOR_FRAC * rms
    return floor, rms, len(vals), per_theta_83


def one_call(args):
    """Module-level (picklable) worker: (cfg_key, theta, with_article, steps)
    -> full_capture dict. Matches exp-087's own `one_call` idiom exactly."""
    key, th, art, steps = args
    cfg = dg.CONFIGS[key]
    cap = _run_sim(cfg, th, steps, art)
    return (key, th, art, steps, cap)


def main():
    print("=" * 78)
    print("exp-088 -- T28 node bracket (theta=38.4/38.8deg) + R13 floor gate")
    print("=" * 78)

    # ---------------------------------------------------------------- R13 floor gate (desk, zero FDTD)
    floor, rms, n83, per_theta_83 = compute_floor()
    print(f"\n[R13 floor gate] RMS[frac_contrast], n={n83}: {rms:.6e}  "
          f"FLOOR_FRAC={FLOOR_FRAC}  FLOOR={floor:.6e}")

    # ------------------------------------------------------- P1: vacuum footprint (new angles)
    vac_report = {}
    vac_pass = True
    for key in PAIR_KEYS:
        cfg = dg.CONFIGS[key]
        sim = Sim(cfg["nx"], cfg["ny"], cells_per_lambda=dg.CPL[600],
                  courant_frac=dg.COURANT_FRAC, absorb=cfg["absorb"])
        cell = {}
        for box_name, clearance in (("BOX_A", BOX_CLEARANCE_A), ("BOX_B", BOX_CLEARANCE_B)):
            x0, x1, y0, y1 = box_for(cfg, clearance)
            footprint = sim.damp_e[x0:x1 + 1, y0:y1 + 1]
            ok = bool(np.all(footprint == 1.0))
            cell[box_name] = dict(box=[x0, x1, y0, y1], all_vacuum=ok)
            vac_pass = vac_pass and ok
        vac_report[key] = cell
    print(f"\n[P1] vacuum-footprint precondition (new angles' geometry is angle-"
          f"independent, same as exp-087): PASS={vac_pass}")
    assert vac_pass, "P1 FAILED -- a BOX_A/BOX_B footprint is not pure vacuum; HALT"

    # ---------------------------------------------------------------- FDTD calls (8 total)
    jobs = []
    for key in PAIR_KEYS:
        for th in ANGLES:
            jobs.append((key, th, False, STEPS_MAIN))   # empty
            jobs.append((key, th, True, STEPS_MAIN))    # article

    print(f"\n{len(jobs)} FDTD calls queued (2 configs x 2 angles x 2 legs = 8)")
    assert len(jobs) == 8, f"call count drifted: {len(jobs)}"
    t0 = time.time()
    captures = {}

    with ProcessPoolExecutor(max_workers=4) as ex:
        for n, (key, th, art, steps, cap) in enumerate(ex.map(one_call, jobs), 1):
            captures[(key, th, art, steps)] = cap
            print(f"  [{n:2d}/{len(jobs)}] {key} theta={th:+06.2f} "
                  f"article={art} steps={steps}", flush=True)
    total_wall = time.time() - t0
    print(f"\ntotal wall time: {total_wall:.1f}s")

    # ---------------------------------------------------------------- P2: reproduction precondition
    with open(EXP083_RESULTS) as f:
        res83_full = json.load(f)
    per_theta_83_full = res83_full["per_theta"]

    repro = {}
    max_dev = 0.0
    for key in PAIR_KEYS:
        cfg = dg.CONFIGS[key]
        for th in ANGLES:
            cap_empty = captures[(key, th, False, STEPS_MAIN)]
            cap_article = captures[(key, th, True, STEPS_MAIN)]
            empty_p = exp087.exp083._profile(cap_empty, cfg)
            article_p = exp087.exp083._profile(cap_article, cfg)
            r = amb.contrast_from_runs([article_p], [empty_p], [1.0],
                                        cfg["y_lo"], cfg["obj_y"], dg.W_OBJ,
                                        dg.GUARD_OUT, dg.W_FLANK)
            key_th = f"{th:.1f}"
            ref_c_empty = per_theta_83_full[key_th][f"{key}_Ce"]
            dev = abs(r["C_empty"] - ref_c_empty)
            repro.setdefault(key, {})[key_th] = dict(fresh=r["C_empty"], ref=ref_c_empty, dev=dev)
            max_dev = max(max_dev, dev)
    repro_pass = bool(max_dev < 1e-9)
    print(f"\n[P2] reproduction precondition: max_dev={max_dev:.3e} PASS(<1e-9)={repro_pass}")
    assert repro_pass, "P2 FAILED -- fresh empty leg does not reproduce exp-083; HALT"

    # ---------------------------------------------------------------- widths() + xi_ext (P3, P4)
    widths_by_cell = {}
    box_dev = {}
    xi_ext = {}
    xi_pass = True
    for key in PAIR_KEYS:
        cfg = dg.CONFIGS[key]
        ref = ref_for(cfg)
        for th in ANGLES:
            cap_empty = captures[(key, th, False, STEPS_MAIN)]
            cap_article = captures[(key, th, True, STEPS_MAIN)]
            for box_name, clearance in (("BOX_A", BOX_CLEARANCE_A), ("BOX_B", BOX_CLEARANCE_B)):
                box = box_for(cfg, clearance)
                w = widths_direction_corrected(cap_article, cap_empty, box, ref)
                widths_by_cell[(key, th, box_name)] = w
                xi = abs(w["sigma_ext_cross"] - w["sigma_ext"]) / abs(w["sigma_ext"])
                xi_ext[(key, th, box_name)] = xi
                if xi > XI_TOL:
                    xi_pass = False
            ba, bb = widths_by_cell[(key, th, "BOX_A")], widths_by_cell[(key, th, "BOX_B")]
            box_dev[(key, th)] = dict(
                ext=abs(ba["sigma_ext"] - bb["sigma_ext"]) / abs(ba["sigma_ext"]),
                abs=abs(ba["sigma_abs"] - bb["sigma_abs"]) / abs(ba["sigma_abs"]),
            )
    print(f"\n[P4] xi_ext (extinction-routes agreement) <= {XI_TOL} everywhere: PASS={xi_pass}")
    for (key, th, box_name), xi in sorted(xi_ext.items()):
        print(f"  {key} theta={th} {box_name}: xi_ext={xi:.6f}")
    assert xi_pass, "P4 FAILED -- extinction-routes disagreement exceeds tolerance; HALT"

    # ---------------------------------------------------------------- non-negativity gate
    nonneg_pass = True
    for (key, th, box_name), w in sorted(widths_by_cell.items()):
        flag = "" if w["sigma_abs"] >= 0 else "  <<< NEGATIVE"
        print(f"  [widths, direction-corrected] {key} theta={th} {box_name}: "
              f"sigma_abs={w['sigma_abs']:.6f} sigma_ext={w['sigma_ext']:.6f}{flag}")
        if w["sigma_abs"] < 0:
            nonneg_pass = False
    print(f"\n[non-negativity gate] sigma_abs>=0 everywhere: PASS={nonneg_pass}")
    assert nonneg_pass, "non-negativity gate FAILED; HALT"

    # ---------------------------------------------------------------- Q6/Q7: thermo chain + T9 anchor (new angles)
    thermo = {}
    ratio_abs_ext = {}
    for key in PAIR_KEYS:
        for th in ANGLES:
            w = widths_by_cell[(key, th, "BOX_A")]
            sigma_ext_cells = w["sigma_ext"]
            ratio_abs_ext_raw = w["sigma_abs"] / w["sigma_ext"] if w["sigma_ext"] != 0 else 0.0
            ratio_abs_ext[(key, th)] = ratio_abs_ext_raw
            ratio_abs_ext_clamped = min(max(ratio_abs_ext_raw, 0.0), 1.0)
            p = ts.absorbed_power_established_ratio(
                IRR_CENTRAL_W_CM2, sigma_ext_cells, DX_M, ratio_abs_ext_clamped)
            assert p["p_abs_w"] >= 0, "non-negativity gate FAILED on p_abs_w; HALT"
            regime = ts.mixed_length_scale_regime(
                p_abs_w=p["p_abs_w"], l_geometric_m=L_GEOMETRIC_M,
                k_air=K_AIR, density_kg_m3=DENSITY_SI_KG_M3, c_p_j_kgk=C_P_SI_J_KGK,
                emissivity=EMISSIVITY, t_ambient_k=T_AMBIENT_K,
                length_provenance="bench_construction")
            netd = ts.netd_disposition(regime["dt_ss_full_K"], NETD_BAND_K)
            thermo[(key, th)] = dict(
                sigma_ext_cells=sigma_ext_cells, ratio_abs_ext_raw=ratio_abs_ext_raw,
                p_abs_w=p["p_abs_w"], dt_ss_full_K=regime["dt_ss_full_K"],
                netd_classification=netd["classification"],
                netd_disclaimer=netd["disclaimer"],
            )

    print("\n[Q6] scene-specific detectability at new angles (NETD is an "
          "instrument threshold, NOT a human-eye one -- does not bear on "
          "constraint-3/4's human-eye verdict, Idealization 9):")
    q6_all_undetectable = True
    for (key, th), d in sorted(thermo.items()):
        print(f"  {key} theta={th}: p_abs_w={d['p_abs_w']:.6e} W  "
              f"dt_ss={d['dt_ss_full_K']:.6e} K  {d['netd_classification']}")
        if d["netd_classification"] != "UNDETECTABLE":
            q6_all_undetectable = False
    if not q6_all_undetectable:
        print(f"  *** Q6 departs from UNDETECTABLE -- triage rule applies: check "
              f"against material-identity swing magnitudes (~{BIOT_SWING_X:.0f}x "
              f"Biot, ~{H_CONV_SWING_X:.0f}x H_CONV) before reading as new physics. ***")

    print("\n[Q7] T9 anchor (sigma_abs/sigma_ext) cross-check at new angles "
          "(informal context, not a scored falsifier):")
    for (key, th), r in sorted(ratio_abs_ext.items()):
        print(f"  {key} theta={th}: ratio_abs_ext={r:.6f}")

    # ---------------------------------------------------------------- PRIMARY: Q4 (ratio_k at new angles)
    frac_p_abs = {}
    frac_contrast_new = {}
    ratio_k = {}
    resolved = {}
    floor_pass = {}
    for th in ANGLES:
        p_c40 = thermo[("C40", th)]["p_abs_w"]
        p_g40 = thermo[("G40", th)]["p_abs_w"]
        frac_p_abs[th] = abs(p_g40 - p_c40) / p_c40 if p_c40 != 0 else float("inf")

        key_th = f"{th:.1f}"
        fc = frac_contrast_of(per_theta_83_full, key_th)
        frac_contrast_new[th] = fc
        floor_pass[th] = bool(fc >= floor)

        ratio_k[th] = frac_p_abs[th] / fc if fc != 0 else float("inf")

        box_dev_max = max(box_dev[("C40", th)]["ext"], box_dev[("C40", th)]["abs"],
                           box_dev[("G40", th)]["ext"], box_dev[("G40", th)]["abs"])
        noise_floor = NOISE_MULT * box_dev_max * p_c40
        noise_resolved = bool(abs(p_g40 - p_c40) > noise_floor)
        resolved[th] = bool(noise_resolved and floor_pass[th])

    print("\n[PRIMARY Q4] ratio_k at the two new bracketing angles:")
    for th in ANGLES:
        outcome = "NODE-UNRESOLVABLE" if not floor_pass[th] else (
            "resolved" if resolved[th] else "unresolved (noise floor)")
        print(f"  theta={th}: frac_p_abs={frac_p_abs[th]:.6e}  "
              f"frac_contrast={frac_contrast_new[th]:.6e}  ratio_k={ratio_k[th]:.6e}  "
              f"floor_pass={floor_pass[th]}  {outcome}")

    # ---------------------------------------------------------------- Q1: retroactive R13 reclassification of exp-087
    with open(EXP087_RESULTS) as f:
        res87 = json.load(f)
    exp087_ratio_k = {float(k): v for k, v in res87["ratio_k"].items()}
    exp087_resolved_orig = {float(k): v for k, v in res87["resolved"].items()}

    retro = {}
    for th_str in ["36.0", "38.6", "41.8"]:
        th = float(th_str)
        fc = frac_contrast_of(per_theta_83_full, th_str)
        fp = bool(fc >= floor)
        retro[th] = dict(
            frac_contrast=fc, floor_pass=fp,
            ratio_k=exp087_ratio_k[th],
            resolved_orig=exp087_resolved_orig[th],
            resolved_under_r13=bool(exp087_resolved_orig[th] and fp),
            outcome="NODE-UNRESOLVABLE" if not fp else "resolved",
        )

    q1_resolved_ratios = [retro[th]["ratio_k"] for th in (36.0, 41.8)]  # 38.6 excluded by construction
    q1_classification = classify_resolved(q1_resolved_ratios)

    print("\n[Q1] retroactive R13 reclassification of exp-087's own 3-angle result:")
    for th_str in ["36.0", "38.6", "41.8"]:
        th = float(th_str)
        r = retro[th]
        print(f"  theta={th}: frac_contrast={r['frac_contrast']:.6e}  "
              f"floor_pass={r['floor_pass']}  ratio_k={r['ratio_k']:.6e}  {r['outcome']}")
    print(f"  Q1 corrected classification (5 sampled angles only, per "
          f"Idealizations 9-10/NOTES.md scoping): {q1_classification}")

    # ---------------------------------------------------------------- Q5: combined 5-angle picture
    all_resolved_ratios = q1_resolved_ratios + [ratio_k[th] for th in ANGLES if resolved[th]]
    n_resolved_combined = len(all_resolved_ratios)
    q5_classification = ("DEGENERATE" if n_resolved_combined < 2
                          else classify_resolved(all_resolved_ratios))
    print(f"\n[Q5] combined 5-angle picture: n_resolved={n_resolved_combined}/5  "
          f"CLASSIFICATION = {q5_classification}  "
          f"(scoped to these 5 sampled angles only -- NOT a channel-general claim, "
          f"see Next/forward-tripwire in NOTES.md)")

    # ---------------------------------------------------------------- persist
    out = dict(
        angles=ANGLES,
        pair_keys=PAIR_KEYS,
        steps_main=STEPS_MAIN,
        total_new_fdtd_calls=len(jobs),
        total_wall_time_s=total_wall,
        r13_floor_gate=dict(floor_frac=FLOOR_FRAC, rms_frac_contrast=rms,
                             n_window_points=n83, floor=floor),
        vacuum_footprint_check=vac_report,
        reproduction_precondition=dict(per_cell=repro, max_dev=max_dev, passed=repro_pass),
        widths={f"{k[0]}_{k[1]}_{k[2]}": v for k, v in widths_by_cell.items()},
        box_dev={f"{k[0]}_{k[1]}": v for k, v in box_dev.items()},
        xi_ext={f"{k[0]}_{k[1]}_{k[2]}": v for k, v in xi_ext.items()},
        xi_pass=xi_pass,
        nonneg_pass=nonneg_pass,
        thermo={f"{k[0]}_{k[1]}": v for k, v in thermo.items()},
        q6_all_undetectable=q6_all_undetectable,
        ratio_abs_ext_new_angles={f"{k[0]}_{k[1]}": v for k, v in ratio_abs_ext.items()},
        biot_swing_x=BIOT_SWING_X, h_conv_swing_x=H_CONV_SWING_X,
        frac_p_abs={str(k): v for k, v in frac_p_abs.items()},
        frac_contrast_new_angles={str(k): v for k, v in frac_contrast_new.items()},
        ratio_k_new_angles={str(k): v for k, v in ratio_k.items()},
        floor_pass_new_angles={str(k): v for k, v in floor_pass.items()},
        resolved_new_angles={str(k): v for k, v in resolved.items()},
        q4_predictions_check=dict(
            theta_38_4_in_band=bool(1.5 <= ratio_k.get(38.4, float("nan")) <= 5.0),
            theta_38_8_in_band=bool(1.5 <= ratio_k.get(38.8, float("nan")) <= 5.5),
        ),
        retroactive_exp087_reclassification={str(k): v for k, v in retro.items()},
        q1_classification=q1_classification,
        q5_all_resolved_ratios=all_resolved_ratios,
        q5_n_resolved=n_resolved_combined,
        q5_classification=q5_classification,
        netd_disclaimer=("NETD is an instrument/detector threshold, not a human "
                          "perceptual one -- does NOT bear on constraint-3/4's "
                          "human-eye verdict. (Idealization 9)"),
        scope_note=("This cross-check bears only on T28's own confound-mechanism "
                     "question and constraint-3's energy-ledger bookkeeping. It does "
                     "not test constraints 1/2/4, and does not re-open or re-score "
                     "REALIZABILITY_MEMO.md's verdict. (Idealization 10)"),
        historical_record_note=("experiments/087-.../results.json and NOTES.md remain "
                                 "the unedited historical record of the frozen "
                                 "Iteration-64 pipeline's output. Q1/Q5 above are a "
                                 "separate, R13-corrected reading supplied for forward "
                                 "citation only -- not a retroactive edit."),
        floor_gate_scope_note=("This cycle's own 5-point sample measures ratio_k near "
                                "only ONE of exp-083's four delta_scene zero-crossings "
                                "(37.127, 38.590, 40.265, 41.461 deg). The other three "
                                "have never been FDTD-sampled for ratio_k. Any "
                                "channel-general CONSISTENT claim requires closing that "
                                "gap first -- see NOTES.md Next."),
    )
    out_path = os.path.join(HERE, "results.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nwrote {out_path}")
    return out


if __name__ == "__main__":
    main()
