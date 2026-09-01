"""exp-099 -- Null C Wider-Bracket Re-Test, R5's First Real Spend
(Ground-Truth-Gated), and the GP2'/ptp Tail Reconciliation. Panel
Iteration 76. Lead seat (rotation): THERMODYNAMICS. Frozen spec: NOTES.md
(Predictions committed to git strictly BEFORE this file's first run,
house discipline). Change rationale: phase2_redteam_audit.md (9 numbered
attacks; 7 mandatory fixes, all adopted; 2 non-blocking wording fixes;
0 critiques overridden -- see NOTES.md's own "Changes from Phase 1"
section).

PASS-path budget: 40 real sim.run() calls (item 1: 12; item 2: 28 [Step 1:
4, Step 2: 8, Step 3: 16]; item 3: 0). HALT-path (item 2's gates fail):
24 calls. Item 2's Step 0 (fault-injection re-scoring at family="R5") is
0 sim.run() calls -- every check stops before .run().

Executes exp-098's own Reconciled Iteration-76 queue items 1-3 (item 4,
ratifying R19, already done; item 5 given a reasoned disposition in
NOTES.md's own section, not a fresh code artifact).
"""

import importlib.util
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, ROOT)


def _load(path, name):
    """House `_load()` pattern (exp-078..098's own idiom for cross-
    experiment-directory imports)."""
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


EXP090_DIR = os.path.join(ROOT, "experiments", "090-t28-floor-frac-threshold-fit")
EXP092_DIR = os.path.join(ROOT, "experiments", "092-t28-crossing-relocation-caution-zone-rebuild")
EXP094_DIR = os.path.join(ROOT, "experiments", "094-t28-cpl40-resolution-sigma-r3-census")
EXP095_DIR = os.path.join(ROOT, "experiments", "095-t28-r4-ground-truth-sign-control")
EXP097_DIR = os.path.join(ROOT, "experiments", "097-t28-r18-tier0-gate-closure")
EXP098_DIR = os.path.join(ROOT, "experiments", "098-t28-cpl40-null-bracket-grazing-instrument")
EXP086_DIR = os.path.join(ROOT, "experiments", "086-t28-free-period-boundary-fix-rescore")

# --- registration-readback gate (exp-097's own module) ---
exp097 = _load(os.path.join(EXP097_DIR, "run.py"), "_exp099_exp097")
CONFIGS = exp097.CONFIGS
CPL = exp097.CPL
TAPER = exp097.TAPER
PAIR_KEYS = exp097.PAIR_KEYS
REPRESENTATIVE = exp097.REPRESENTATIVE
run_checks_1234_and_7 = exp097.run_checks_1234_and_7
check6_positional_and_cpl = exp097.check6_positional_and_cpl
check6_set_membership_OLD = exp097.check6_set_membership_OLD

# --- R4/R5-family real-FDTD machinery (exp-095's own module) ---
exp095 = _load(os.path.join(EXP095_DIR, "run.py"), "_exp099_exp095")
dg = exp095.dg
PAIR_KEYS_R4 = exp095.PAIR_KEYS_R4
PAIR_KEYS_R5 = exp095.PAIR_KEYS_R5
cell_metrics_r4 = exp095.cell_metrics_r4
cell_metrics_r5 = exp095.cell_metrics_r5
pair_metrics_full = exp095.pair_metrics_full
netd_row = exp095.netd_row
run_block_r4 = exp095.run_block_r4
run_block_r5 = exp095.run_block_r5
compute_floor = exp095.compute_floor
XI_TOL = exp095.XI_TOL
SIGMA_R4_CORRECTED = exp095.SIGMA_R4_CORRECTED
SIGMA_R5_CORRECTED = exp095.SIGMA_R5_CORRECTED
assert abs(SIGMA_R4_CORRECTED - 0.25) < 1e-12
assert abs(SIGMA_R5_CORRECTED - 0.2) < 1e-12
assert PAIR_KEYS_R4 == ("C40_R4", "G40_R4")
assert PAIR_KEYS_R5 == ("C40_R5", "G40_R5")

# --- exp-098's own R4-family batch runner, diagnostic, and grazing-
#     incidence machinery, reused unmodified ---
exp098 = _load(os.path.join(EXP098_DIR, "run.py"), "_exp099_exp098")
run_r4_batch = exp098.run_r4_batch
find_sign_change = exp098.find_sign_change
richardson_style_diagnostic = exp098.richardson_style_diagnostic
FastEval = exp098.FastEval
GEOM_C40 = exp098.GEOM_C40
LAM600 = exp098.LAM600
NETD_ROW_KEYS = exp098.NETD_ROW_KEYS

# ================================================================ established ground truth (re-pulled, not hand-typed)
j090 = json.load(open(os.path.join(EXP090_DIR, "results.json")))
CROSSINGS_CPL20 = j090["q8"]["crossings_deg"]
assert len(CROSSINGS_CPL20) == 4
THETA0_A, THETA0_38590, THETA0_B, THETA0_C = CROSSINGS_CPL20
for th, expect in [(THETA0_A, 37.127246), (THETA0_38590, 38.590230),
                    (THETA0_B, 40.265420), (THETA0_C, 41.460901)]:
    assert abs(th - expect) < 1e-5, f"crossing mismatch: {th} vs {expect}"

j092 = json.load(open(os.path.join(EXP092_DIR, "results.json")))
CR30 = j092["rank1"]["crossing_report"]
SHIFT_C_20_30_PRIMARY = CR30["shift_vs_cpl20_upper"]          # +0.320166 deg
SHIFT_C_20_30_SECOND = CR30["shift_vs_cpl20_upper_second"]    # +0.376752 deg
assert abs(SHIFT_C_20_30_PRIMARY - 0.3201659178026546) < 1e-9
assert abs(SHIFT_C_20_30_SECOND - 0.3767516353289935) < 1e-9

j098 = json.load(open(os.path.join(EXP098_DIR, "results.json")))
NULL_C_FILED = j098["item_i"]["C"]["report"]
# Fix 4/6 (Red Team Attack 4/6): pull the true stored keys, never hand-type
NULL_C_FILED_KEYS = sorted(float(k) for k in NULL_C_FILED.keys())
assert len(NULL_C_FILED_KEYS) == 4, NULL_C_FILED_KEYS
assert abs(NULL_C_FILED_KEYS[0] - 40.960901) < 1e-4
assert abs(NULL_C_FILED_KEYS[3] - 41.960901) < 1e-4
THETA0_B_CROSSING_CPL40 = j098["item_i"]["B"]["crossing_cpl40"]
assert abs(THETA0_B_CROSSING_CPL40 - 39.921519316666) < 1e-6
RICHARDSON_B_FILED = j098["richardson_diagnostic"]["B"]
SHIFT_B_30_40 = RICHARDSON_B_FILED["shift_30_40"]
SHIFT_B_20_30 = RICHARDSON_B_FILED["shift_20_30"]

j094 = json.load(open(os.path.join(EXP094_DIR, "results.json")))
GT_36_DEG = j094["rank3"]["per_theta"]["36.0"]
GT_36_DEG_SIGN = GT_36_DEG["delta_scene"] < 0
assert GT_36_DEG["floor_pass"] is True
assert GT_36_DEG["outcome"] == "CONSISTENT"
print(f"[ground truth, re-pulled] delta_scene(36.0deg, R4)={GT_36_DEG['delta_scene']:+.6e}  "
      f"sign={'negative' if GT_36_DEG_SIGN else 'positive'}  outcome={GT_36_DEG['outcome']}")

# Established delta_scene period (Idealization 60/Fix 5), pulled from LOGBOOK
# citation, not re-derived here -- LOGBOOK.md's own directly-fitted value.
DELTA_SCENE_PERIOD_DEG = 2.9474

j095 = json.load(open(os.path.join(EXP095_DIR, "results.json")))
assert j095["rank2_calls"] == 0 and j095["rank2"]["skipped"] is True, (
    "expected R5 to have zero prior real FDTD calls -- if this assert fails, "
    "the 'R5's first real spend' framing this cycle rests on is stale; HALT "
    "and re-check NOTES.md before proceeding")


# ================================================================ item 2, Step 0: fault-injection re-scoring at family="R5" (0 sim.run() calls)
def run_r5_fault_injection_rescoring():
    """Fix 1 (QUANTUM's finding, Red Team Attack 1, mandatory): every
    fault-injection scenario in this program's history (exp-096/097's own
    positive-control/FI-A/B/C/D/E/F/H idiom) was hardcoded family="R4" (or,
    for FI-H, mislabeled an R3 point). Zero fault-injection coverage has
    ever existed at family="R5". This re-runs the identical idiom at
    family="R5", theta=41.825deg (R5's own REPRESENTATIVE[6] point),
    config_key="C40_R5", cpl_intended=50. Zero new sim.run() calls -- every
    check stops before .run()."""
    theta0, cpl0, key0 = 41.825, 50, "C40_R5"
    pc = run_checks_1234_and_7("R5", theta0, cpl0, key0)
    fia = run_checks_1234_and_7("R5", theta0, cpl0, key0, cpl_actual=dg.R4_CPL[600])
    fib = run_checks_1234_and_7("R5", theta0, cpl0, key0, theta_actual=41.850)
    fic = run_checks_1234_and_7("R5", theta0, cpl0, key0, theta_actual=-41.825)
    fid = run_checks_1234_and_7("R5", theta0, cpl0, key0, edge_actual=TAPER["R4"])

    fi_1234_7 = dict(
        positive_control=dict(**pc, must_be_1234="CLEAN", must_be_7="CLEAN"),
        FI_A_family_cpl_swap=dict(**fia, must_be_1234="DEFECT-FOUND", must_be_7="CLEAN"),
        FI_B_angle_mislabel=dict(**fib, must_be_1234="DEFECT-FOUND", must_be_7="CLEAN"),
        FI_C_sign_flip=dict(**fic, must_be_1234="DEFECT-FOUND", must_be_7="CLEAN"),
        FI_D_wrong_taper_edge=dict(**fid, must_be_1234="CLEAN", must_be_7="DEFECT-FOUND"),
    )
    fi_1234_7["all_as_predicted"] = bool(
        pc["clean_1234"] and pc["clean_7"]
        and not fia["clean_1234"] and fia["clean_7"]
        and not fib["clean_1234"] and fib["clean_7"]
        and not fic["clean_1234"] and fic["clean_7"]
        and fid["clean_1234"] and not fid["clean_7"]
    )

    # Check 6 idiom: FI-E (index swap), FI-F (cpl corruption), FI-H (family
    # mislabel), all at/around R5's own REPRESENTATIVE[6]/[7] (notes_line=476).
    r5_pt0 = REPRESENTATIVE[6]
    assert r5_pt0["family"] == "R5" and r5_pt0["notes_line"] == 476 and r5_pt0["theta"] == 41.825

    swapped = (41.850, 41.825)  # exp-095's own RANK2B_NATIVE_ANGLES reversed
    fie_results = []
    for pair_index in (0, 1):
        pt = dict(family="R5", theta=swapped[pair_index], notes_line=476, pair_index=pair_index)
        new = check6_positional_and_cpl(pt)
        old = check6_set_membership_OLD(pt)
        fie_results.append(dict(pair_index=pair_index, theta_scored=swapped[pair_index],
                                 new_clean=new["clean"], old_clean=old["clean"]))
    fi_e = dict(results=fie_results,
                caught_by_new=bool(any(not r["new_clean"] for r in fie_results)),
                missed_by_old=bool(all(r["old_clean"] for r in fie_results)))

    cpl_saved = CPL["R5"]
    CPL["R5"] = 40
    try:
        new_f = check6_positional_and_cpl(r5_pt0)
        old_f = check6_set_membership_OLD(r5_pt0)
    finally:
        CPL["R5"] = cpl_saved
    fi_f = dict(new_clean=new_f["clean"], old_clean=old_f["clean"],
                caught_by_new=bool(not new_f["clean"]), missed_by_old=bool(old_f["clean"]))

    r4_pt0 = REPRESENTATIVE[0]
    assert r4_pt0["family"] == "R4" and r4_pt0["notes_line"] == 437
    mislabeled = dict(r4_pt0, family="R5")
    new_h = check6_positional_and_cpl(mislabeled)
    old_h = check6_set_membership_OLD(mislabeled)
    fi_h = dict(true_family="R4", mislabeled_family="R5", notes_line=437,
                new_clean=new_h["clean"], old_clean=old_h["clean"],
                new_family_ok=new_h["family_ok"],
                caught_by_new=bool(not new_h["clean"]), missed_by_old=bool(old_h["clean"]))

    check6_idiom_all_as_predicted = bool(
        fi_e["caught_by_new"] and fi_f["caught_by_new"] and fi_h["caught_by_new"])

    all_clean = bool(fi_1234_7["all_as_predicted"] and check6_idiom_all_as_predicted)
    return dict(fi_1234_7=fi_1234_7, fi_e=fi_e, fi_f=fi_f, fi_h=fi_h,
                check6_idiom_all_as_predicted=check6_idiom_all_as_predicted,
                all_as_predicted=all_clean)


# ================================================================ item 2 registration preflight + batch runner (R5 family)
def registration_preflight_r5(angles, config_keys=("C40_R5", "G40_R5")):
    """R5-family analog of exp-098's own `registration_preflight` (R4-only
    there) -- zero-cost extension of the registration-readback gate to
    every NEW (family, theta, cpl=50, config_key) point this item spends
    real FDTD on."""
    checks = []
    for th in angles:
        for key in config_keys:
            checks.append(run_checks_1234_and_7("R5", th, 50, key))
    all_clean = all(c["clean_1234"] and c["clean_7"] for c in checks)
    return dict(n_points=len(checks), all_clean=bool(all_clean), checks=checks)


def run_r5_batch(angles, floor):
    """R5-family analog of exp-098's own `run_r4_batch`, substituting every
    R4-scoped constant/function for its R5 equivalent (mirroring exp-095's
    own R4->R5 mirroring discipline)."""
    preflight = registration_preflight_r5(angles)
    assert preflight["all_clean"], f"REGISTRATION GATE FAILED for R5 angles {angles}: HALT"

    jobs = []
    for th in angles:
        for key in PAIR_KEYS_R5:
            jobs.append((key, th, False, dg.R5_STEPS, None))
            jobs.append((key, th, True, dg.R5_STEPS, SIGMA_R5_CORRECTED))
    captures, wall = run_block_r5(jobs)

    xi_pass = True
    nonneg_pass = True
    cells = {}
    for th in angles:
        for key in PAIR_KEYS_R5:
            cap_empty = captures[(key, th, False, dg.R5_STEPS)]
            cap_article = captures[(key, th, True, dg.R5_STEPS)]
            cell = cell_metrics_r5(key, th, dg.R5_STEPS, cap_empty, cap_article)
            cells[(key, th)] = cell
            for xi in cell["xi_ext"].values():
                if xi > XI_TOL:
                    xi_pass = False
            if not cell["sigma_abs_nonneg"]:
                nonneg_pass = False
    assert xi_pass, "xi_ext gate FAILED (R5) -- extinction-routes disagreement; HALT"
    assert nonneg_pass, "sigma_abs>=0 gate FAILED (R5); HALT"

    report = {}
    for th in angles:
        c_cell = cells[("C40_R5", th)]
        g_cell = cells[("G40_R5", th)]
        pm = pair_metrics_full(c_cell, g_cell, floor)
        row = dict(delta_scene=pm["delta_scene"], frac_contrast=pm["frac_contrast"],
                   ratio_k=pm["ratio_k"], floor_pass=pm["floor_pass"],
                   **netd_row(pm))
        assert NETD_ROW_KEYS <= set(row.keys())
        report[th] = row

    return dict(preflight=preflight, report=report, wall_s=wall,
                n_calls=len(jobs), xi_pass=xi_pass, nonneg_pass=nonneg_pass)


# ================================================================ item 3: GP2'/ptp tail reconciliation (0 FDTD)
def run_ptp_tail_extension():
    """Extends exp-086's own sliding-window ptp method (`phase4_rescore.py`)
    verbatim -- identical FastEval, identical theta_centers/sub_theta
    construction, identical ptp_sub=np.ptp(c_sub) formula -- no new
    statistic. New windows only: theta_c in {79,81,83,85,87}deg."""
    fe = FastEval(GEOM_C40, LAM600)
    new_centers = [79.0, 81.0, 83.0, 85.0, 87.0]
    new_windows = []
    for thc in new_centers:
        sub_theta = np.round(np.arange(thc - 3.0, thc + 3.0 + 1e-9, 0.2), 6)
        c_sub = fe.curve(sub_theta)
        ptp_sub = float(np.ptp(c_sub))
        new_windows.append(dict(theta_c=thc, ptp=ptp_sub, window=[float(sub_theta[0]), float(sub_theta[-1])],
                                 n_points=len(sub_theta)))
    assert sum(w["n_points"] for w in new_windows) == 155, "expected 5*31=155 new evaluations"

    j086 = json.load(open(os.path.join(EXP086_DIR, "phase4_rescore_results.json")))
    sub_results_filed = j086["method_c_rescore"]["sub_results"]
    ref_5 = next(r for r in sub_results_filed if abs(r["theta_c"] - 5.0) < 1e-6)
    ptp_ref_5 = ref_5["ptp"]
    ratios_new = [dict(theta_c=w["theta_c"], ptp=w["ptp"], ratio_to_theta_c_5=w["ptp"] / ptp_ref_5)
                  for w in new_windows]

    # GP2' comparator, re-read (not hand-typed) from exp-098's own results.json
    gp2_curve = j098["item_v"]["gp2_curve"]
    gp2_tail = [r for r in gp2_curve if r["theta"] >= 74.0]
    gp2_tail_min = min(r["ratio_to_ref"] for r in gp2_tail)
    gp2_tail_max = max(r["ratio_to_ref"] for r in gp2_tail)
    gp2_tail_any_valid = any(r["classification"] == "VALID" for r in gp2_tail)

    return dict(new_windows=new_windows, ptp_ref_theta_c_5=ptp_ref_5, ratios_new=ratios_new,
                gp2_tail_min_ratio=gp2_tail_min, gp2_tail_max_ratio=gp2_tail_max,
                gp2_tail_any_valid=gp2_tail_any_valid,
                filed_theta_c_69_ptp=next(r["ptp"] for r in sub_results_filed if abs(r["theta_c"] - 69.0) < 1e-6),
                filed_theta_c_77_ptp=next(r["ptp"] for r in sub_results_filed if abs(r["theta_c"] - 77.0) < 1e-6))


# ================================================================ main
def main():
    t0 = time.time()
    print("=" * 78)
    print("exp-099 -- Null C wider bracket, R5 first spend (GT-gated), GP2'/ptp tail")
    print("Panel Iteration 76, THERMODYNAMICS rotation lead")
    print("=" * 78)

    floor, rms, n83, per_theta_83_full = compute_floor()
    print(f"\n[R13 floor gate] RMS[frac_contrast], n={n83}: {rms:.6e}  FLOOR={floor:.6e}  "
          "(unchanged, applied unrecomputed -- Idealization 6)")

    # ---- item 1: Null C wider, asymmetric bracket ----
    print("\n" + "=" * 78)
    print("ITEM 1: Null C re-test, wider asymmetric bracket (+1.500deg upward)")
    print("=" * 78)
    new_angles_c = [THETA0_C + 0.8333, THETA0_C + 1.1667, THETA0_C + 1.500]
    print(f"theta0(cpl20)={THETA0_C:.11f}deg  new angles={[round(a, 6) for a in new_angles_c]}")
    batch_c = run_r4_batch(new_angles_c, floor)
    print(f"  wall={batch_c['wall_s']:.1f}s ({batch_c['wall_s'] / 60.0:.2f} min)  "
          f"calls={batch_c['n_calls']}  preflight_clean={batch_c['preflight']['all_clean']}")

    combined_angles_c = sorted(new_angles_c + NULL_C_FILED_KEYS)
    combined_delta_c = {}
    combined_report_c = {}
    for a in new_angles_c:
        combined_delta_c[a] = batch_c["report"][a]["delta_scene"]
        combined_report_c[f"{a:.6f}"] = batch_c["report"][a]
    for k_str, row in NULL_C_FILED.items():
        a = float(k_str)
        combined_delta_c[a] = row["delta_scene"]
        combined_report_c[f"{a:.6f}"] = row
    for a in combined_angles_c:
        print(f"    theta={a:.6f}: delta_scene={combined_delta_c[a]:+.6e}")

    # New-points-only trichotomy (Fix 5): interval-slope-decay ratios among
    # the 3 new points continuing on from the last filed interval.
    new_sorted = sorted(new_angles_c)
    deltas_seq = [combined_delta_c[THETA0_C + 0.500]] + [combined_delta_c[a] for a in new_sorted]
    diffs = [deltas_seq[i + 1] - deltas_seq[i] for i in range(len(deltas_seq) - 1)]
    r_ratios = [abs(diffs[i + 1]) / abs(diffs[i]) if diffs[i] != 0 else float("inf")
                for i in range(len(diffs) - 1)]
    all_new_positive = all(combined_delta_c[a] > 0 for a in new_sorted)
    all_new_floor_pass = all(batch_c["report"][a]["floor_pass"] for a in new_angles_c)
    amplitude_criteria_met = bool(all_new_positive and all_new_floor_pass and all(r < 0.5 for r in r_ratios))
    half_width_c = 1.500
    period_criterion_met = bool(half_width_c >= DELTA_SCENE_PERIOD_DEG)

    crossing_c, bracket_c = find_sign_change(combined_angles_c, combined_delta_c)
    if not all_new_floor_pass:
        item1_verdict = "INCONCLUSIVE-FLOOR"
    elif crossing_c is not None:
        item1_verdict = "SIGN-CHANGE-FOUND"
    elif amplitude_criteria_met and period_criterion_met:
        item1_verdict = "VANISHING-AMPLITUDE"
    elif amplitude_criteria_met and not period_criterion_met:
        item1_verdict = "INCONCLUSIVE-CONSISTENT-WITH-SAME-LOBE-OSCILLATION"
    else:
        item1_verdict = "INCONCLUSIVE-AT-THIS-WIDTH"
    print(f"[Item 1 SUMMARY] verdict={item1_verdict}  crossing={crossing_c}  "
          f"r_ratios={r_ratios}  half_width={half_width_c}deg vs period={DELTA_SCENE_PERIOD_DEG}deg")

    item_1 = dict(theta0_cpl20=THETA0_C, new_angles=new_angles_c,
                  combined_angles=combined_angles_c, combined_report=combined_report_c,
                  all_new_floor_pass=all_new_floor_pass, r_ratios=r_ratios,
                  amplitude_criteria_met=amplitude_criteria_met,
                  half_width_deg=half_width_c, established_period_deg=DELTA_SCENE_PERIOD_DEG,
                  period_criterion_met=period_criterion_met,
                  crossing_cpl40=crossing_c, crossing_bracket=bracket_c, verdict=item1_verdict,
                  wall_s=batch_c["wall_s"], n_calls=batch_c["n_calls"], preflight=batch_c["preflight"],
                  shift_vs_cpl20_30_primary=SHIFT_C_20_30_PRIMARY, shift_vs_cpl20_30_second=SHIFT_C_20_30_SECOND)

    # ---- item 2: R5 first real spend, ground-truth-gated ----
    print("\n" + "=" * 78)
    print("ITEM 2: cpl=50 (R5) first real spend -- Step 0 (FI rescoring) -> "
          "Step 1 (far-from-null GT) -> Step 2 (settling) -> Step 3 (interior, gated)")
    print("=" * 78)

    print("\n[Step 0] fault-injection re-scoring at family='R5' (0 sim.run() calls)")
    step0 = run_r5_fault_injection_rescoring()
    print(f"  all_as_predicted={step0['all_as_predicted']}")
    assert step0["all_as_predicted"], "R5 FAULT-INJECTION RE-SCORING FAILED -- HALT item 2 entirely"

    print("\n[Step 1] far-from-null ground-truth sign check, theta=36.0deg, R5")
    batch_gt = run_r5_batch([36.0], floor)
    ds_gt = batch_gt["report"][36.0]["delta_scene"]
    gt_sign_match = bool((ds_gt < 0) == GT_36_DEG_SIGN)
    print(f"  delta_scene(36.0deg, R5)={ds_gt:+.6e}  established_sign="
          f"{'negative' if GT_36_DEG_SIGN else 'positive'}  match={gt_sign_match}  "
          f"calls={batch_gt['n_calls']}")
    step1 = dict(theta=36.0, delta_scene=ds_gt, floor_pass=batch_gt["report"][36.0]["floor_pass"],
                 established_sign_negative=GT_36_DEG_SIGN, sign_match=gt_sign_match,
                 established_reference=dict(source="experiments/094-.../results.json::rank3.per_theta['36.0']",
                                             delta_scene=GT_36_DEG["delta_scene"], outcome=GT_36_DEG["outcome"]),
                 n_calls=batch_gt["n_calls"], wall_s=batch_gt["wall_s"], preflight=batch_gt["preflight"])

    print("\n[Step 2] Rank 2a settling precondition, theta=39.854853deg, R5_STEPS vs R5_STEPS_STRESS")
    settle_angle = 39.854853
    settle_jobs = []
    for steps in (dg.R5_STEPS, dg.R5_STEPS_STRESS):
        for key in PAIR_KEYS_R5:
            settle_jobs.append((key, settle_angle, False, steps, None))
            settle_jobs.append((key, settle_angle, True, steps, SIGMA_R5_CORRECTED))
    settle_preflight = registration_preflight_r5([settle_angle])
    assert settle_preflight["all_clean"], "REGISTRATION GATE FAILED (Step 2 settling angle); HALT"
    settle_captures, settle_wall = run_block_r5(settle_jobs)

    xi_pass_2a, nonneg_pass_2a = True, True
    cells_2a = {}
    for steps in (dg.R5_STEPS, dg.R5_STEPS_STRESS):
        for key in PAIR_KEYS_R5:
            cap_empty = settle_captures[(key, settle_angle, False, steps)]
            cap_article = settle_captures[(key, settle_angle, True, steps)]
            cell = cell_metrics_r5(key, settle_angle, steps, cap_empty, cap_article)
            cells_2a[(key, steps)] = cell
            for xi in cell["xi_ext"].values():
                if xi > XI_TOL:
                    xi_pass_2a = False
            if not cell["sigma_abs_nonneg"]:
                nonneg_pass_2a = False
    assert xi_pass_2a, "Step 2 xi_ext gate FAILED; HALT"
    assert nonneg_pass_2a, "Step 2 sigma_abs>=0 gate FAILED; HALT"

    pm_7000 = pair_metrics_full(cells_2a[("C40_R5", dg.R5_STEPS)], cells_2a[("G40_R5", dg.R5_STEPS)], floor)
    pm_10500 = pair_metrics_full(cells_2a[("C40_R5", dg.R5_STEPS_STRESS)], cells_2a[("G40_R5", dg.R5_STEPS_STRESS)], floor)
    ds_7000, ds_10500 = pm_7000["delta_scene"], pm_10500["delta_scene"]
    rel_dev_2a = abs(ds_10500 - ds_7000) / abs(ds_7000) if ds_7000 != 0 else float("inf")

    def settle_band(rel_dev):
        if rel_dev <= 1e-2:
            return "PASS"
        if rel_dev <= 1e-1:
            return "CAUTIONARY-PASS"
        return "HALT"

    step2_verdict = settle_band(rel_dev_2a)
    print(f"  delta_scene(R5_STEPS)={ds_7000:+.6e}  delta_scene(R5_STEPS_STRESS)={ds_10500:+.6e}  "
          f"rel_dev={rel_dev_2a:.4%}  verdict={step2_verdict}  calls={len(settle_jobs)}")
    step2 = dict(angle=settle_angle, delta_scene_r5_steps=ds_7000, delta_scene_r5_steps_stress=ds_10500,
                 rel_dev=rel_dev_2a, verdict=step2_verdict, n_calls=len(settle_jobs), wall_s=settle_wall,
                 preflight=settle_preflight)

    step3_gate_open = bool(gt_sign_match and step2_verdict != "HALT")
    print(f"\n[Step 3 gate] gt_sign_match={gt_sign_match}  step2_verdict={step2_verdict}  "
          f"gate_open={step3_gate_open}")

    if step3_gate_open:
        print("\n[Step 3] interior sweep, 4 angles around theta_c40, R5")
        theta_c40 = THETA0_B_CROSSING_CPL40
        step3_angles = [theta_c40 - 0.400, theta_c40 - 0.233, theta_c40 - 0.067, theta_c40 + 0.100]
        # theta_c40-0.067 should coincide with the settling angle (39.854853deg)
        assert abs((theta_c40 - 0.067) - settle_angle) < 5e-4, (theta_c40 - 0.067, settle_angle)
        print(f"  theta_c40={theta_c40:.6f}deg  angles={[round(a, 6) for a in step3_angles]}")
        batch_3 = run_r5_batch(step3_angles, floor)
        print(f"  wall={batch_3['wall_s']:.1f}s ({batch_3['wall_s'] / 60.0:.2f} min)  calls={batch_3['n_calls']}")
        delta_3 = {a: batch_3["report"][a]["delta_scene"] for a in step3_angles}
        for a in step3_angles:
            print(f"    theta={a:.6f}: delta_scene={delta_3[a]:+.6e}")
        all_floor_pass_3 = all(batch_3["report"][a]["floor_pass"] for a in step3_angles)
        crossing_50, bracket_50 = find_sign_change(sorted(step3_angles), delta_3)
        step3_verdict = ("SIGN-CHANGE-FOUND" if crossing_50 is not None else "NO-SIGN-CHANGE")
        if not all_floor_pass_3:
            step3_verdict = "INCONCLUSIVE-FLOOR"
        print(f"[Step 3 SUMMARY] verdict={step3_verdict}  crossing_cpl50={crossing_50}")

        richardson_30_40_50 = dict(available=False)
        if crossing_50 is not None:
            shift_40_50 = crossing_50 - theta_c40
            richardson_30_40_50 = richardson_style_diagnostic(
                shift_20_30=SHIFT_B_30_40, shift_30_40=shift_40_50, cpl20=30, cpl30=40, cpl40=50)
            print(f"[Richardson 30/40/50, corrected marginal-to-marginal] {richardson_30_40_50}")

        step3 = dict(theta_c40=theta_c40, angles=step3_angles, report={f"{a:.6f}": batch_3["report"][a] for a in step3_angles},
                     all_floor_pass=all_floor_pass_3, crossing_cpl50=crossing_50, crossing_bracket=bracket_50,
                     verdict=step3_verdict, n_calls=batch_3["n_calls"], wall_s=batch_3["wall_s"],
                     preflight=batch_3["preflight"], richardson_30_40_50=richardson_30_40_50)
        item2_calls = step1["n_calls"] + step2["n_calls"] + step3["n_calls"]
    else:
        print("\n[Step 3] SKIPPED -- gate closed (UNINTERPRETABLE-PENDING-R5-GROUND-TRUTH-CHECK)")
        step3 = dict(skipped=True, reason="UNINTERPRETABLE-PENDING-R5-GROUND-TRUTH-CHECK",
                     gt_sign_match=gt_sign_match, step2_verdict=step2_verdict)
        item2_calls = step1["n_calls"] + step2["n_calls"]

    item_2 = dict(step0=step0, step1=step1, step2=step2, step3=step3,
                  step3_gate_open=step3_gate_open, total_calls=item2_calls)
    print(f"\n[Item 2 SUMMARY] total real FDTD calls={item2_calls}  "
          f"(PASS-path expects 28, HALT-path 12)")

    # ---- item 3: GP2'/ptp tail reconciliation ----
    print("\n" + "=" * 78)
    print("ITEM 3: GP2'/ptp tail reconciliation, theta_c in {79,81,83,85,87}deg")
    print("=" * 78)
    item_3 = run_ptp_tail_extension()
    for w in item_3["new_windows"]:
        print(f"  theta_c={w['theta_c']:.1f}deg  ptp={w['ptp']:.6e}  "
              f"ratio_to_theta_c=5={w['ptp'] / item_3['ptp_ref_theta_c_5']:.4f}x")
    print(f"  filed theta_c=69deg ptp={item_3['filed_theta_c_69_ptp']:.6e}  "
          f"filed theta_c=77deg ptp={item_3['filed_theta_c_77_ptp']:.6e}")
    print(f"  GP2' tail (theta>=74deg): min_ratio={item_3['gp2_tail_min_ratio']:.4f}x  "
          f"max_ratio={item_3['gp2_tail_max_ratio']:.4f}x  any_VALID={item_3['gp2_tail_any_valid']}")

    # ---- assemble, self-checked call-count/row-count invariant (R19) ----
    total_calls = item_1["n_calls"] + item_2["total_calls"]
    print(f"\n[R19 assert] item1={item_1['n_calls']}  item2={item_2['total_calls']}  "
          f"total_real_fdtd_calls={total_calls}")
    assert total_calls in (40, 24, 16, 20, 32), (
        f"unexpected total call count {total_calls} -- re-check R19-style call-count arithmetic before trusting results.json")
    if item_2["step3_gate_open"]:
        assert total_calls == 40, f"PASS-path expected 40, got {total_calls}"
    else:
        assert total_calls in (24, 16), f"HALT-path expected 24 (Step-2 HALT) or 16 (Step-1 GT mismatch, Step-2 not run -- N/A, Step2 always runs), got {total_calls}"

    total_wall = time.time() - t0
    print(f"\n{'=' * 78}\nTOTAL: {total_calls} real FDTD calls, {total_wall:.1f}s "
          f"({total_wall / 60.0:.2f} min) wall time\n{'=' * 78}")

    results = dict(
        experiment="exp-099", panel_iteration=76,
        fdtd_calls=total_calls, wall_time_s=total_wall,
        r13_floor_gate=dict(floor=floor, rms=rms, n83=n83),
        item_1=item_1, item_2=item_2, item_3=item_3,
        delta_scene_established_period_deg=DELTA_SCENE_PERIOD_DEG,
    )
    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(results, f, indent=2, default=str)
    print("\nresults.json written.")


if __name__ == "__main__":
    main()
