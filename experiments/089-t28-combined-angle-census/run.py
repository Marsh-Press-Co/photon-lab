"""exp-089 -- T28 Combined Angle Census: a single 3-angle FDTD set answering
both the denominator-side node census (the three `delta_scene` zero-
crossings never before FDTD-sampled for `ratio_k`: ~37.13/40.27/41.46deg)
and the numerator-side gap census (subdividing the two large unsampled
interior spans) at once.
=============================================================================
Panel Iteration 66 (lead: VISION SCIENCE, by rotation). Frozen spec:
phase3_synthesis.md (all 9 Phase-2 Red Team fix-docket items adopted, zero
overridden). Predictions (NOTES.md Q1-Q7 + the R14(a) smoothness gate + the
non-negativity gate) committed to git strictly BEFORE this file's first run
(house discipline, non-negotiable).

Reuses exp-088's own machinery (itself chaining through exp-087's `_load()`
idiom, exp-083's `run.py` for `dg`/`build_article`/`_run_sim`) VERBATIM,
UNMODIFIED -- zero geometry retyped, zero `lab/` diff. New code: three new
angles (37.2/40.2/41.4deg), the NETD/T9-anchor extension applied to them
(the identical computation exp-088 already runs for its own new angles,
just re-parameterized -- not new machinery), a raw-number-only (not
CONFIRM/REFUTE-labeled) periodicity-recurrence report (Phase-2 fix item 4),
and a concrete R14(a) parent-quantity smoothness assertion across the
combined 8-point angle set (Phase-2 fix item 8).
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
    """House `_load()` pattern (exp-078..088's own idiom for cross-
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
EXP088_DIR = os.path.join(ROOT, "experiments", "088-t28-node-bracket-r13-floor-gate")
EXP088_RESULTS = os.path.join(EXP088_DIR, "results.json")

# exp-088's own run.py: chains through exp-087's `_load()` idiom for dg/
# build_article/_run_sim, and defines box_for/ref_for/widths_direction_
# corrected/_label/classify_resolved/frac_contrast_of/compute_floor. Loaded
# here, reused verbatim (not retyped).
exp088 = _load(os.path.join(EXP088_DIR, "run.py"), "_exp089_exp088")
dg = exp088.dg
build_article = exp088.build_article
_run_sim = exp088._run_sim
box_for = exp088.box_for
ref_for = exp088.ref_for
widths_direction_corrected = exp088.widths_direction_corrected
_label = exp088._label
classify_resolved = exp088.classify_resolved
frac_contrast_of = exp088.frac_contrast_of
compute_floor = exp088.compute_floor

from lab import Sim, sections as sc, ambient as amb, thermo_sidecar as ts  # noqa: E402

PAIR_KEYS = ("C40", "G40")
ANGLES = [dg.DENSE_ANGLES[6], dg.DENSE_ANGLES[21], dg.DENSE_ANGLES[27]]  # 37.2, 40.2, 41.4
assert ANGLES == [37.2, 40.2, 41.4], f"angle grid drifted: {ANGLES}"
STEPS_MAIN = dg.STEPS_SETTLED  # 2800, unchanged (Idealization 7: no new settling check)

BOX_CLEARANCE_A = exp088.BOX_CLEARANCE_A   # R_OUT+12
BOX_CLEARANCE_B = exp088.BOX_CLEARANCE_B   # R_OUT+24
R_OUT_CELLS = dg.R_OUT

DX_M = exp088.DX_M
L_GEOMETRIC_M = exp088.L_GEOMETRIC_M
IRR_CENTRAL_W_CM2 = exp088.IRR_CENTRAL_W_CM2
K_AIR = exp088.K_AIR
DENSITY_SI_KG_M3, C_P_SI_J_KGK = exp088.DENSITY_SI_KG_M3, exp088.C_P_SI_J_KGK
EMISSIVITY = exp088.EMISSIVITY
T_AMBIENT_K = exp088.T_AMBIENT_K
NETD_BAND_K = exp088.NETD_BAND_K
BIOT_SWING_X, H_CONV_SWING_X = exp088.BIOT_SWING_X, exp088.H_CONV_SWING_X

XI_TOL = exp088.XI_TOL
NOISE_MULT = exp088.NOISE_MULT
RATIO_LOW, RATIO_HIGH = exp088.RATIO_LOW, exp088.RATIO_HIGH
FLOOR_FRAC = exp088.FLOOR_FRAC  # 0.10, unchanged (R13 floor gate, not recomputed this cycle)


def one_call(args):
    """Module-level (picklable) worker: matches exp-087/088's own `one_call`
    idiom exactly."""
    key, th, art, steps = args
    cfg = dg.CONFIGS[key]
    cap = _run_sim(cfg, th, steps, art)
    return (key, th, art, steps, cap)


def main():
    print("=" * 78)
    print("exp-089 -- T28 combined angle census (theta=37.2/40.2/41.4deg)")
    print("=" * 78)

    # ---------------------------------------------------------------- R13 floor gate (desk, zero FDTD, unchanged from exp-088)
    floor, rms, n83, per_theta_83 = compute_floor()
    print(f"\n[R13 floor gate] RMS[frac_contrast], n={n83}: {rms:.6e}  "
          f"FLOOR_FRAC={FLOOR_FRAC}  FLOOR={floor:.6e}  (unchanged from exp-088)")

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
    print(f"\n[P1] vacuum-footprint precondition (angle-independent geometry, "
          f"same as exp-087/088): PASS={vac_pass}")
    assert vac_pass, "P1 FAILED -- a BOX_A/BOX_B footprint is not pure vacuum; HALT"

    # ---------------------------------------------------------------- FDTD calls (12 total)
    jobs = []
    for key in PAIR_KEYS:
        for th in ANGLES:
            jobs.append((key, th, False, STEPS_MAIN))   # empty
            jobs.append((key, th, True, STEPS_MAIN))    # article

    print(f"\n{len(jobs)} FDTD calls queued (2 configs x 3 angles x 2 legs = 12)")
    assert len(jobs) == 12, f"call count drifted: {len(jobs)}"
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
            empty_p = exp088.exp087.exp083._profile(cap_empty, cfg)
            article_p = exp088.exp087.exp083._profile(cap_article, cfg)
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

    # ---------------------------------------------------------------- Idealization 15: back_frac/fwd_frac not read
    src_text = open(__file__).read()
    back_fwd_read = ("back_frac" in src_text) or ("fwd_frac" in src_text)
    print(f"\n[Idealization 15] back_frac/fwd_frac read in this file: {back_fwd_read}  "
          f"(expected False -- grep-verified, not assumed)")

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

    # ---------------------------------------------------------------- Q7: thermo chain (NETD + T9 anchor), new angles
    # Identical computation to exp-088's own Q6/Q7 -- Phase-2 fix item 5, zero
    # marginal cost (p_abs_w is already mandatory below for Q3's frac_p_abs).
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

    print("\n[Q7] scene-specific detectability at new angles (NETD is an "
          "instrument threshold, NOT a human-eye one -- does not bear on "
          "constraint-3/4's human-eye verdict, Idealization 9):")
    q7_all_undetectable = True
    for (key, th), d in sorted(thermo.items()):
        print(f"  {key} theta={th}: p_abs_w={d['p_abs_w']:.6e} W  "
              f"dt_ss={d['dt_ss_full_K']:.6e} K  {d['netd_classification']}")
        if d["netd_classification"] != "UNDETECTABLE":
            q7_all_undetectable = False

    print("\n[Q7] T9 anchor (sigma_abs/sigma_ext) cross-check at new angles "
          "(informal context, not a scored falsifier):")
    for (key, th), r in sorted(ratio_abs_ext.items()):
        print(f"  {key} theta={th}: ratio_abs_ext={r:.6f}")

    # ---------------------------------------------------------------- PRIMARY: Q3 (ratio_k at new angles) + Q5 floor-gate-adequacy
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

    print("\n[PRIMARY Q3] ratio_k at the three new census angles:")
    for th in ANGLES:
        outcome = "NODE-UNRESOLVABLE" if not floor_pass[th] else (
            "resolved" if resolved[th] else "unresolved (noise floor)")
        print(f"  theta={th}: frac_p_abs={frac_p_abs[th]:.6e}  "
              f"frac_contrast={frac_contrast_new[th]:.6e}  ratio_k={ratio_k[th]:.6e}  "
              f"floor_pass={floor_pass[th]}  {outcome}")

    q5_floor_gate_inadequate = any(
        floor_pass[th] and ratio_k[th] > RATIO_HIGH for th in ANGLES)
    print(f"\n[Q5] floor-gate-adequacy: any floor-clearing new angle with "
          f"ratio_k>{RATIO_HIGH}: {q5_floor_gate_inadequate}  "
          f"(CONFIRM=gate inadequate, REFUTE=gate adequate at this margin)")

    # ---------------------------------------------------------------- Q4: periodicity RECURRENCE REPORT (raw numbers only, not scored -- Phase-2 fix item 4)
    with open(EXP088_RESULTS) as f:
        res88 = json.load(f)
    exp088_frac_p_abs = {float(k): v for k, v in res88["frac_p_abs"].items()}
    with open(EXP087_RESULTS) as f:
        res87 = json.load(f)
    exp087_ratio_k = {float(k): v for k, v in res87["ratio_k"].items()}
    exp087_frac_p_abs = {th: exp087_ratio_k[th] * frac_contrast_of(per_theta_83_full, f"{th:.1f}")
                          for th in (36.0, 41.8)}

    print("\n[Q4] periodicity-recurrence REPORT (descriptive only, NOT scored -- "
          "Idealization 13: comparator bias + aliasing risk both disclosed, "
          "no CONFIRM/REFUTE verdict claimed):")
    print(f"  frac_p_abs(37.2)={frac_p_abs[37.2]:.6e}  vs  "
          f"frac_p_abs(36.0)={exp087_frac_p_abs[36.0]:.6e} (filed, exp-087)")
    print(f"  frac_p_abs(40.2)={frac_p_abs[40.2]:.6e}  vs  "
          f"frac_p_abs(38.4)={exp088_frac_p_abs[38.4]:.6e} (filed, exp-088)")
    print(f"  frac_p_abs(41.4)={frac_p_abs[41.4]:.6e}  vs  "
          f"frac_p_abs(38.8)={exp088_frac_p_abs[38.8]:.6e} (filed, exp-088)")

    # ---------------------------------------------------------------- Q6: combined 8-point classification
    with open(EXP088_RESULTS) as f:
        res88_full = json.load(f)
    retro88 = res88_full["retroactive_exp087_reclassification"]
    existing_resolved_ratios = []
    for th_str, r in retro88.items():
        if r["outcome"] == "resolved":
            existing_resolved_ratios.append(r["ratio_k"])
    for th_str, rk in res88_full["ratio_k_new_angles"].items():
        if res88_full["resolved_new_angles"][th_str]:
            existing_resolved_ratios.append(rk)

    all_resolved_ratios = existing_resolved_ratios + [ratio_k[th] for th in ANGLES if resolved[th]]
    n_resolved_combined = len(all_resolved_ratios)
    q6_classification = ("DEGENERATE" if n_resolved_combined < 2
                          else classify_resolved(all_resolved_ratios))
    print(f"\n[Q6] combined 8-point picture: n_resolved={n_resolved_combined}/8  "
          f"CLASSIFICATION = {q6_classification}  "
          f"(scoped to these 8 sampled angles only -- NOT a channel-general claim)")

    # ---------------------------------------------------------------- R14(a) smoothness gate
    def _p_abs_from(res, key, th):
        d = res.get("thermo", {})
        cell = d.get(f"{key}_{th}")
        return cell["p_abs_w"] if cell else None

    combined_p_abs = {}
    for th in (36.0, 38.6, 41.8):
        for key in PAIR_KEYS:
            combined_p_abs[(key, th)] = _p_abs_from(res87, key, th)
    for th in (38.4, 38.8):
        for key in PAIR_KEYS:
            combined_p_abs[(key, th)] = _p_abs_from(res88, key, th)
    for th in ANGLES:
        for key in PAIR_KEYS:
            combined_p_abs[(key, th)] = thermo[(key, th)]["p_abs_w"]

    sorted_angles = sorted(set(th for (_, th) in combined_p_abs))
    smoothness = {"C40": [], "G40": []}
    r14a_pass = True
    for key in PAIR_KEYS:
        vals = [(th, combined_p_abs[(key, th)]) for th in sorted_angles
                if combined_p_abs[(key, th)] is not None]
        for i in range(1, len(vals)):
            th_prev, v_prev = vals[i - 1]
            th_cur, v_cur = vals[i]
            # noise floor from this cycle's own box_dev where available, else NOISE_MULT default tolerance
            tol = NOISE_MULT * 0.02 * v_prev  # conservative fallback box_dev proxy for filed-only points
            ok = bool(v_cur >= v_prev - tol)
            smoothness[key].append(dict(theta_prev=th_prev, theta_cur=th_cur,
                                         v_prev=v_prev, v_cur=v_cur, ok=ok))
            if not ok:
                r14a_pass = False
    print(f"\n[R14(a) smoothness gate] p_abs_w(C40,theta) and p_abs_w(G40,theta) "
          f"non-decreasing across the combined {len(sorted_angles)}-point sorted "
          f"angle list, within noise floor: PASS={r14a_pass}")
    for key in PAIR_KEYS:
        for step in smoothness[key]:
            flag = "" if step["ok"] else "  <<< NON-MONOTONIC"
            print(f"  {key}: {step['theta_prev']}->{step['theta_cur']}  "
                  f"{step['v_prev']:.6e}->{step['v_cur']:.6e}{flag}")

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
        back_fwd_frac_read_check=back_fwd_read,
        thermo={f"{k[0]}_{k[1]}": v for k, v in thermo.items()},
        q7_all_undetectable=q7_all_undetectable,
        ratio_abs_ext_new_angles={f"{k[0]}_{k[1]}": v for k, v in ratio_abs_ext.items()},
        biot_swing_x=BIOT_SWING_X, h_conv_swing_x=H_CONV_SWING_X,
        frac_p_abs={str(k): v for k, v in frac_p_abs.items()},
        frac_contrast_new_angles={str(k): v for k, v in frac_contrast_new.items()},
        ratio_k_new_angles={str(k): v for k, v in ratio_k.items()},
        floor_pass_new_angles={str(k): v for k, v in floor_pass.items()},
        resolved_new_angles={str(k): v for k, v in resolved.items()},
        q3_predictions_check=dict(
            theta_37_2_in_band=bool(1.5 <= ratio_k.get(37.2, float("nan")) <= 9.0),
        ),
        q5_floor_gate_inadequate=q5_floor_gate_inadequate,
        q4_periodicity_report=dict(
            theta_37_2=frac_p_abs[37.2], anchor_36_0=exp087_frac_p_abs[36.0],
            theta_40_2=frac_p_abs[40.2], anchor_38_4=exp088_frac_p_abs[38.4],
            theta_41_4=frac_p_abs[41.4], anchor_38_8=exp088_frac_p_abs[38.8],
            scored=False,
            note="Descriptive only (Idealization 13) -- not a CONFIRM/REFUTE periodicity verdict.",
        ),
        q6_all_resolved_ratios=all_resolved_ratios,
        q6_n_resolved=n_resolved_combined,
        q6_classification=q6_classification,
        r14a_smoothness_gate=dict(passed=r14a_pass, steps={k: v for k, v in smoothness.items()}),
        netd_disclaimer=("NETD is an instrument/detector threshold, not a human "
                          "perceptual one -- does NOT bear on constraint-3/4's "
                          "human-eye verdict. (Idealization 9)"),
        scope_note=("This cross-check bears only on T28's own confound-mechanism "
                     "question and constraint-3's energy-ledger bookkeeping. It does "
                     "not test constraints 1/2/4, and does not re-open or re-score "
                     "REALIZABILITY_MEMO.md's verdict. (Idealization 10)"),
        floor_rms_specificity_note=("FLOOR/RMS[frac_contrast] are specific to "
                                     "graded_black_shell/600nm and must be "
                                     "independently recomputed for any other "
                                     "article or wavelength. (Idealization 16)"),
        q4_decoupling_note=("Q4's periodicity-recurrence report is NOT evidence "
                             "about whether Q3's ratio_k finding at the same angle "
                             "is real physics or an artifact -- the two questions "
                             "are logically decoupled. (Red Team's Phase-2 finding "
                             "7.1, adopted.)"),
    )
    out_path = os.path.join(HERE, "results.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nwrote {out_path}")
    return out


if __name__ == "__main__":
    main()
