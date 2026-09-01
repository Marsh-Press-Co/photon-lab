"""exp-100 -- First Constraint-1/2/3 Scoring Pass on delta_scene(theta),
Gated on a PAD-vs-Article Partition. Panel Iteration 77. Lead seat
(rotation): QUANTUM OPTICS. Frozen spec: NOTES.md (Predictions committed
to git strictly BEFORE this file's first run, house discipline). Change
rationale: phase2_redteam_audit.md (9 numbered attacks, all adopted, 0
overridden -- see NOTES.md's own "Changes from Phase 1" section).

Tier 1 (0 FDTD): item 1 PAD-vs-article partition (pooled correlation,
75 rows across experiments/{091,092,093,094,095,098,099}); item 2
MATERIALS' disposition memo (per-outcome conditional); item 3 Richardson
4-point (cpl 20/30/40/50) convergence characterization at Null B.

Tier 2: Leg A (0 FDTD) -- C_thr(L) desk score of the pooled delta_scene
table, 36-43deg window. Leg B (24 sim.run() calls) -- beam_behind_t28 /
observer_record_t28, this bench's first-ever direct constraint-1/2
measurement, at 6 angles (4 established cpl=20 zero-crossings + 2
largest-filed-magnitude points, Red Team's RT-1 fix).

Run with --dry-run to execute Tier 1 + Leg A only (0 FDTD cost) and
validate before spending Leg B's real 24-call budget -- this program's
own house discipline after exp-099's mid-run KeyError.
"""

import importlib.util
import json
import math
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, ROOT)


def _load(path, name):
    """House `_load()` pattern (exp-078..099's own idiom for cross-
    experiment-directory imports)."""
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


EXP090_DIR = os.path.join(ROOT, "experiments", "090-t28-floor-frac-threshold-fit")
EXP095_DIR = os.path.join(ROOT, "experiments", "095-t28-r4-ground-truth-sign-control")
EXP097_DIR = os.path.join(ROOT, "experiments", "097-t28-r18-tier0-gate-closure")
EXP098_DIR = os.path.join(ROOT, "experiments", "098-t28-cpl40-null-bracket-grazing-instrument")
EXP099_DIR = os.path.join(ROOT, "experiments", "099-t28-null-c-r5-thirdpoint-gp2-reconciliation")

# --- exp-098's own registration-preflight extension + Richardson diagnostic,
#     AND (per a Phase-4 same-shift fix -- see run_output.txt's own first,
#     crashed execution) the R4-family real-FDTD machinery pulled through
#     exp098's OWN internal `exp095` chain, never a second, independent
#     `_load()` of exp-095/094. exp098's own module docstring already
#     names this exact hazard ("the actual FDTD calls below use ONLY
#     exp095's own objects, never mixed with [another chain's] own, to
#     stay internally consistent with each function's own closure") --
#     the first execution of this file violated it by ALSO calling
#     `_load(EXP095_DIR, ...)` directly, which registers `sys.modules
#     ["_exp095_exp094"]`; loading exp098 SECOND then re-executes exp095's
#     own file internally (a fresh `_load(EXP094_DIR, ..., "_exp095_
#     exp094")`, the SAME literal name, clobbering the registration this
#     file's own `run_block_r4` reference depended on for multiprocessing
#     pickling) -- `PicklingError: ... it's not the same object as
#     _exp095_exp094.one_call_r4`, thrown before any sim.run() call
#     executed (0 FDTD calls spent, confirmed from the crashed run's own
#     console capture). Fixed by taking every R4-family name from
#     `exp098.exp095` (exp098's own, single, internally-consistent
#     instance) instead of a second direct load. ---
exp097 = _load(os.path.join(EXP097_DIR, "run.py"), "_exp100_exp097")
run_checks_1234_and_7 = exp097.run_checks_1234_and_7

exp098 = _load(os.path.join(EXP098_DIR, "run.py"), "_exp100_exp098")
registration_preflight = exp098.registration_preflight
NETD_ROW_KEYS = exp098.NETD_ROW_KEYS

exp095 = exp098.exp095       # exp098's OWN internal instance -- not a fresh load
dg = exp095.dg
PAIR_KEYS_R4 = exp095.PAIR_KEYS_R4
cell_metrics_r4 = exp095.cell_metrics_r4
pair_metrics_full = exp095.pair_metrics_full
netd_row = exp095.netd_row
run_block_r4 = exp095.run_block_r4
compute_floor = exp095.compute_floor
XI_TOL = exp095.XI_TOL
SIGMA_R4_CORRECTED = exp095.SIGMA_R4_CORRECTED
assert abs(SIGMA_R4_CORRECTED - 0.25) < 1e-12
assert PAIR_KEYS_R4 == ("C40_R4", "G40_R4")

from lab import Sim, sections as sc, emit  # noqa: E402

# ================================================================ established ground truth (re-pulled, not hand-typed)
j090 = json.load(open(os.path.join(EXP090_DIR, "results.json")))
CROSSINGS_CPL20 = j090["q8"]["crossings_deg"]
assert len(CROSSINGS_CPL20) == 4
THETA0_A, THETA0_38590, THETA0_B, THETA0_C = CROSSINGS_CPL20
for th, expect in [(THETA0_A, 37.127246), (THETA0_38590, 38.590230),
                    (THETA0_B, 40.265420), (THETA0_C, 41.460901)]:
    assert abs(th - expect) < 1e-5, f"crossing mismatch: {th} vs {expect}"

j098 = json.load(open(os.path.join(EXP098_DIR, "results.json")))
RICH_B_20_30_40 = j098["richardson_diagnostic"]["B"]
assert RICH_B_20_30_40["available"]
SHIFT_20_30 = RICH_B_20_30_40["shift_20_30"]
SHIFT_30_40 = RICH_B_20_30_40["shift_30_40"]
OBSERVED_RATIO_20_30_40 = RICH_B_20_30_40["observed_ratio"]
assert abs(OBSERVED_RATIO_20_30_40 - 0.7765163757372424) < 1e-9
assert abs(SHIFT_20_30 - (-0.1935812644838535)) < 1e-9
assert abs(SHIFT_30_40 - (-0.15031902190763446)) < 1e-9

j099 = json.load(open(os.path.join(EXP099_DIR, "results.json")))
STEP3 = j099["item_2"]["step3"]
RICH_30_40_50 = STEP3["richardson_30_40_50"]
assert RICH_30_40_50["available"]
# Fix 4/relabeling note (exp-099's own text): richardson_style_diagnostic
# was called positionally for the 30/40/50 triple, so this dict's own
# "shift_20_30"/"shift_30_40" KEYS actually hold the TRUE shift_30_40 and
# shift_40_50 values respectively -- read by the corrected mapping below,
# never re-derived.
SHIFT_30_40_FROM_099 = RICH_30_40_50["shift_20_30"]
SHIFT_40_50 = RICH_30_40_50["shift_30_40"]
OBSERVED_RATIO_30_40_50 = RICH_30_40_50["observed_ratio"]
assert abs(OBSERVED_RATIO_30_40_50 - 0.962282667915931) < 1e-9
assert abs(SHIFT_30_40_FROM_099 - SHIFT_30_40) < 1e-9, (
    "SANITY: 098's own true shift_30_40 must match 099's relabeled "
    "'shift_20_30' field exactly -- same underlying quantity, two files")
assert abs(SHIFT_40_50 - (-0.14464938943979178)) < 1e-9
CROSSING_CPL50 = STEP3["crossing_cpl50"]

# The two largest-filed-magnitude delta_scene values in the 36-43deg
# window (Red Team RT-1's fix -- reused, not re-derived): exp-099's own
# item_1 combined_report, read by actual stored key.
NULL_C_COMBINED = j099["item_1"]["combined_report"]
EXTREMA_ANGLES = [40.960901, 42.960901]
for a in EXTREMA_ANGLES:
    key = f"{a:.6f}"
    assert key in NULL_C_COMBINED, f"expected filed key {key} missing from exp-099 item_1"

LEG_B_ANGLES = sorted([THETA0_A, THETA0_38590, THETA0_B, THETA0_C] + EXTREMA_ANGLES)
assert len(LEG_B_ANGLES) == 6, LEG_B_ANGLES

FLOOR, _FLOOR_RMS, _FLOOR_N, _ = compute_floor()

# ================================================================ Tier 1, item 1: PAD-vs-article partition
# Exact (file, json-path, family) table -- each family independently
# confirmed by reading that file's own run.py for which family-specific
# constant/function populated it (STEPS_R3/cell_metrics_full -> R3;
# dg.R4_STEPS/cell_metrics_r4 -> R4; PAIR_KEYS_R5/R5_CONFIGS -> R5),
# never guessed from the JSON alone. "cpl20-native" = the pre-R3 original
# congruent construction, a fourth resolution class outside the R3/R4/R5
# census proper.
POOL_TABLE = [
    ("091-t28-r3-resolution-denser-recheck", ["raw", "native_leg1_cpl20_steps4200"], "cpl20-native"),
    ("091-t28-r3-resolution-denser-recheck", ["raw", "r3_leg2_cpl30_steps4200"], "R3"),
    ("091-t28-r3-resolution-denser-recheck", ["raw", "r3_leg3_cpl30_steps6300"], "R3"),
    ("091-t28-r3-resolution-denser-recheck", ["raw", "r3_leg4_cpl30_steps4200_bracket"], "R3"),
    ("092-t28-crossing-relocation-caution-zone-rebuild", ["rank1", "per_theta"], "R3"),
    ("093-t28-upper-crossing-resolution-netd-thread", ["item1", "per_theta"], "R3"),
    ("093-t28-upper-crossing-resolution-netd-thread", ["item5", "per_theta"], "R3"),
    ("094-t28-cpl40-resolution-sigma-r3-census", ["rank1b", "per_theta"], "R4"),
    ("094-t28-cpl40-resolution-sigma-r3-census", ["rank3", "per_theta"], "R3"),
    ("095-t28-r4-ground-truth-sign-control", ["rank1", "rank1a", "per_theta"], "R4"),
    ("095-t28-r4-ground-truth-sign-control", ["rank1", "rank1c", "per_theta"], "R4"),
    ("098-t28-cpl40-null-bracket-grazing-instrument", ["item_i", "A", "report"], "R4"),
    ("098-t28-cpl40-null-bracket-grazing-instrument", ["item_i", "B", "report"], "R4"),
    ("098-t28-cpl40-null-bracket-grazing-instrument", ["item_i", "C", "report"], "R4"),
    ("098-t28-cpl40-null-bracket-grazing-instrument", ["item_ii", "combined_report"], "R4"),
    ("099-t28-null-c-r5-thirdpoint-gp2-reconciliation", ["item_1", "combined_report"], "R4"),
    ("099-t28-null-c-r5-thirdpoint-gp2-reconciliation", ["item_2", "step3", "report"], "R5"),
]
# Two single-fixed-angle rows (not angle-keyed dicts) with a known theta
# pulled from that cycle's own module constant, cited by source line:
SINGLE_ANGLE_ROWS = [
    ("094-t28-cpl40-resolution-sigma-r3-census", ["rank2", "corrected"], "R3", 41.6),      # RANK2_ANGLE, run.py:228
    ("094-t28-cpl40-resolution-sigma-r3-census", ["rank2", "native_comparator"], "R3", 41.6),
    ("095-t28-r4-ground-truth-sign-control", ["rank4", "corrected"], "R3", 38.4),           # RANK4_ANGLE, run.py:270
]


def _dig(d, path):
    for k in path:
        d = d[k]
    return d


def pool_rows():
    """Every filed (theta, family, delta_scene, frac_p_abs[, ratio_abs_ext
    deltas]) row this sub-thread has produced with the inputs item 1 needs
    -- read by actual stored key, never hand-typed. Two extraction shapes:
    angle-keyed dicts (POOL_TABLE) and single-fixed-angle dicts
    (SINGLE_ANGLE_ROWS)."""
    rows = []
    cache = {}
    for fname, path, family in POOL_TABLE:
        if fname not in cache:
            cache[fname] = json.load(open(os.path.join(ROOT, "experiments", fname, "results.json")))
        sub = _dig(cache[fname], path)
        for theta_key, row in sub.items():
            frac_p_abs = row.get("frac_p_abs")
            if frac_p_abs is None:
                frac_p_abs = abs(row["p_abs_w_g"] - row["p_abs_w_c"]) / row["p_abs_w_c"]
            rows.append(dict(
                source=fname, family=family, theta=float(theta_key),
                delta_scene=row["delta_scene"], frac_p_abs=frac_p_abs,
                ratio_abs_ext_raw_c=row.get("ratio_abs_ext_raw_c"),
                ratio_abs_ext_raw_g=row.get("ratio_abs_ext_raw_g"),
            ))
    for fname, path, family, theta in SINGLE_ANGLE_ROWS:
        if fname not in cache:
            cache[fname] = json.load(open(os.path.join(ROOT, "experiments", fname, "results.json")))
        row = _dig(cache[fname], path)
        frac_p_abs = row.get("frac_p_abs")
        if frac_p_abs is None:
            frac_p_abs = abs(row["p_abs_w_g"] - row["p_abs_w_c"]) / row["p_abs_w_c"]
        rows.append(dict(
            source=fname, family=family, theta=theta,
            delta_scene=row["delta_scene"], frac_p_abs=frac_p_abs,
            ratio_abs_ext_raw_c=row.get("ratio_abs_ext_raw_c"),
            ratio_abs_ext_raw_g=row.get("ratio_abs_ext_raw_g"),
        ))
    return rows


def pearson_r(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    if x.size < 3 or np.std(x) == 0 or np.std(y) == 0:
        return 0.0
    return float(np.corrcoef(x, y)[0, 1])


def permutation_test(x, y, n_trials=20000, seed=20260901):
    """Fix 2 (Red Team RT-2): pre-registered joint decision rule --
    coupling detected requires BOTH p<0.05 (this test) AND |r|>=0.2
    (effect-size floor, applied by the caller). Unpaired shuffle of y
    against x (R10: the pooled set is an assembled census, not a swept
    curve -- no circular-shift operation applies)."""
    r_obs = pearson_r(x, y)
    rng = np.random.default_rng(seed)
    y = np.asarray(y, float).copy()
    count = 0
    for _ in range(n_trials):
        rng.shuffle(y)
        if abs(pearson_r(x, y)) >= abs(r_obs):
            count += 1
    p = count / n_trials
    return r_obs, p


def tier1_item1():
    rows = pool_rows()
    x = [r["frac_p_abs"] for r in rows]
    y = [r["delta_scene"] for r in rows]
    r_obs, p = permutation_test(x, y)
    coupling_detected = bool(p < 0.05 and abs(r_obs) >= 0.2)

    by_family = {}
    for fam in ("R3", "R4", "R5"):
        sub = [r for r in rows if r["family"] == fam]
        if len(sub) >= 3:
            rf, pf = permutation_test([s["frac_p_abs"] for s in sub], [s["delta_scene"] for s in sub])
            by_family[fam] = dict(n=len(sub), r=rf, p=pf,
                                   coupling_detected=bool(pf < 0.05 and abs(rf) >= 0.2))
        else:
            by_family[fam] = dict(n=len(sub), note="too few rows (<3)")

    # Idealization 70 (pre-registered in NOTES.md before this script ran):
    # a family-stratified split that CONTRADICTS the pooled joint-rule
    # result is folded into "ambiguous/underpowered," not left to post-hoc
    # judgment -- a real cross-term should recur across families (R15's
    # own addendum discipline); a pooled-only or single-family-only signal
    # falsifies "genuine, general coupling" even if some individual test
    # clears the joint rule.
    family_flags = {f: d["coupling_detected"] for f, d in by_family.items() if "coupling_detected" in d}
    contradiction = len(set(family_flags.values()) | {coupling_detected}) > 1
    if contradiction:
        outcome = "ambiguous"
    elif coupling_detected:
        outcome = "coupling_detected"
    else:
        outcome = "majority_pad"

    deltas = [abs(r["ratio_abs_ext_raw_g"] - r["ratio_abs_ext_raw_c"])
              for r in rows if r["ratio_abs_ext_raw_c"] is not None and r["ratio_abs_ext_raw_g"] is not None]
    return dict(
        n_rows=len(rows), n_by_family={f: len([r for r in rows if r["family"] == f])
                                        for f in ("cpl20-native", "R3", "R4", "R5")},
        r_pooled=r_obs, p_pooled=p, coupling_detected=coupling_detected,
        by_family=by_family, family_contradiction=bool(contradiction), outcome=outcome,
        delta_ratio_abs_ext_n=len(deltas),
        delta_ratio_abs_ext_max=(max(deltas) if deltas else None),
        delta_ratio_abs_ext_mean=(float(np.mean(deltas)) if deltas else None),
        rows_raw=rows,
    )


def tier1_item2(item1):
    """MATERIALS' fix (rescoped per-outcome conditional, NOTES.md fix 6)."""
    outcome = item1["outcome"]
    if outcome == "coupling_detected":
        branch = "coupling_detected"
        text = (
            "Branch (ii) -- coupling detected, consistently across the "
            "pooled test and every family stratum with enough rows to "
            "test. The coupled residual is read as a diffraction "
            "consequence of the already-published, already-realized "
            "graded_black_shell rim geometry: PUBLISHED, no new material "
            "or structure required. This does not certify the specific "
            "*magnitude* is material-relevant at every angle -- only that "
            "no new realizability question is raised by its existence."
        )
    elif outcome == "majority_pad":
        branch = "majority_pad"
        text = (
            "Branch (i) -- majority-PAD / no significant coupling, "
            "consistently across the pooled test and every family stratum "
            f"(pooled r={item1['r_pooled']:.4f}, permutation p={item1['p_pooled']:.4f}). "
            "delta_scene's dominant identity is a domain-geometry artifact; "
            "no realizability tier applies -- it is not a material property "
            "to bound. This rescopes item 2 away from the category error "
            "Phase 2's MATERIALS critique found in the original framing: "
            "neither of delta_scene's two candidate readings requires a "
            "published/plausible/unobtainium verdict for a *new* structure."
        )
    else:
        branch = "ambiguous"
        text = (
            "Branch (iii) -- ambiguous/underpowered (Idealization 70, "
            "pre-registered before this script ran). The pooled test "
            f"(r={item1['r_pooled']:.4f}, p={item1['p_pooled']:.4f}, "
            f"coupling_detected={item1['coupling_detected']}) is CONTRADICTED "
            f"by at least one family-stratified result: {item1['by_family']}. "
            "A real, general article-coupling effect should recur across "
            "families (R15's own addendum discipline); a family-specific-"
            "only signal is evidence for a family-specific recipe artifact, "
            "not genuine coupling. Disposition deferred -- no realizability "
            "claim made this cycle."
        )
    memo = f"""# exp-100 Tier 1 item 2 -- MATERIALS' disposition memo

Rescoped per-outcome conditional (Red Team Phase-2 mandatory fix 6,
NOTES.md). Decided by Tier 1 item 1's own pooled correlation result.

## Established, unchanged fact (cpl-is-inert)

`cpl` (the FDTD grid-density/numerical-resolution knob, `CPL={{R3:30,R4:40,
R5:50}}`) is confirmed purely numerical: `L_GEOMETRIC_M` is invariant to
1e-12 across R3/R4/R5 (Gate 3, every `R{{n}}` cycle since exp-094). This is
a resolution-knob fact, closed, and orthogonal to the question below.

## This cycle's own finding (delta_scene's realizability disposition)

Pooled dataset: {item1['n_rows']} rows across 7 experiment directories
({item1['n_by_family']}), r(delta_scene, frac_p_abs) = {item1['r_pooled']:.4f},
permutation p = {item1['p_pooled']:.4f} (20,000 trials), joint rule
(p<0.05 AND |r|>=0.2) on the pooled set: **{"MET" if item1['coupling_detected'] else "NOT MET"}**.
Family-stratified contradiction (Idealization 70): **{item1['family_contradiction']}**.
Overall outcome: **{outcome.upper()}**.

{text}

Per-family breakdown (a real cross-term should recur across families,
R15's own addendum discipline): {json.dumps(item1['by_family'], indent=2)}
"""
    with open(os.path.join(HERE, "disposition_memo.md"), "w") as f:
        f.write(memo)
    return dict(branch=branch)


def tier1_item3():
    """4-point Richardson characterization at Null B, full stored
    precision (not the 6-decimal display exp-099's own prose used)."""
    mags = [abs(SHIFT_20_30), abs(SHIFT_30_40), abs(SHIFT_40_50)]
    monotonic = mags[0] > mags[1] > mags[2]

    def implied_order(r, cpl_mid, cpl_fine):
        return math.log(abs(r)) / math.log(cpl_mid / cpl_fine)

    p1 = implied_order(OBSERVED_RATIO_20_30_40, 30, 40)
    p2 = implied_order(OBSERVED_RATIO_30_40_50, 40, 50)
    return dict(
        shift_20_30=SHIFT_20_30, shift_30_40=SHIFT_30_40, shift_40_50=SHIFT_40_50,
        magnitudes=mags, monotonic_decreasing=bool(monotonic),
        observed_ratio_20_30_40=OBSERVED_RATIO_20_30_40,
        observed_ratio_30_40_50=OBSERVED_RATIO_30_40_50,
        implied_order_p1=p1, implied_order_p2=p2,
        p_decreasing=bool(p2 < p1),
        interpretation=("ratio climbing toward 1 (0.7765->0.9623) with implied "
                        "local order dropping (p1->p2) is consistent with either "
                        "slow-but-genuine convergence or a non-convergent recipe "
                        "artifact -- n=2 ratios cannot distinguish these "
                        "(Idealization 49); descriptive only."),
    )


# ================================================================ Tier 2, Leg A
C_THR_LAB = 0.005
C_THR_FIELD = 0.02
# Fix 9 (VISION-b): corrected Phase-3 committed band, replacing the
# superseded Iteration-1 pre-correction draft numbers.
L_STAR_LAB_BAND = (5.3e-6, 7.5e-5)
L_STAR_FIELD_BAND = (1.7e-4, 1.2e-3)


def tier2_leg_a(item1_rows):
    window = [r for r in item1_rows if 36.0 <= r["theta"] <= 43.0]
    if not window:
        return dict(n_in_window=0)
    abs_vals = [(abs(r["delta_scene"]), r["theta"], r["source"]) for r in window]
    peak, peak_theta, peak_source = max(abs_vals, key=lambda t: t[0])
    return dict(
        n_in_window=len(window), peak_abs_delta_scene=peak,
        peak_theta=peak_theta, peak_source=peak_source,
        pass_lab=bool(peak < C_THR_LAB), pass_field=bool(peak < C_THR_FIELD),
        caveat=("Fix 8 (VISION-a): static-contrast bound only, provisional "
                "pending T3 (still this program's longest-standing unbuilt "
                "instrument) -- NOT a completed Tier-W/Tier-A verdict on a "
                "swept angular fringe. Fix/Idealization 64 (PHOTONICS): "
                "600nm-only; LOGBOOK's established T21 750nm/theta=40deg "
                "fringe (0.0237, 4.7x C_thr) in this identical window is an "
                "unaddressed same-window contamination-risk precedent, not "
                "tested this cycle."),
        l_star_lab_band=L_STAR_LAB_BAND, l_star_field_band=L_STAR_FIELD_BAND,
    )


# ================================================================ Tier 2, Leg B
PLANE_OBS_STANDOFF_CELLS = 10
BEAM_BEHIND_HALF_WIDTH = dg.REF_HALF_H_R4 if hasattr(dg, "REF_HALF_H_R4") else 160


def plane_x_obs(cfg):
    """New plane, source side (between src_x and obj_x), symmetric with
    plane_x_behind's own standoff -- not previously used anywhere on this
    bench (observer_record has never been computed on it before). This
    bench's src_x > obj_x > (existing, far-side) plane_x; the observer
    sits with the source at high-x."""
    return cfg["obj_x"] + dg.R4_R_OUT + PLANE_OBS_STANDOFF_CELLS


def plane_x_behind(cfg):
    """~10 cells past the object's outer radius, far (downstream, low-x)
    side -- matching exp-001's own beam-behind idiom, per NOTES.md Setup."""
    return cfg["obj_x"] - dg.R4_R_OUT - PLANE_OBS_STANDOFF_CELLS


def _fresh_sim_scaffold(cfg):
    """A throwaway, never-`.run()` Sim purely to recover the scalar grid
    attributes (omega/S/lam/absorb/ny) `emit.observer_record` needs --
    identical construction to `_run_sim_r4_sigma`'s own first line, minus
    the source/materials/run() calls. No field data is ever read from
    this object; it costs one array allocation, not a timestep."""
    return Sim(cfg["nx"], cfg["ny"], cells_per_lambda=dg.R4_CPL[600],
               courant_frac=dg.COURANT_FRAC, absorb=cfg["absorb"])


def beam_behind_t28(cap, cfg):
    ph = sc.phasors(cap)
    y0 = cfg["obj_y"]
    y_lo, y_hi = y0 - BEAM_BEHIND_HALF_WIDTH, y0 + BEAM_BEHIND_HALF_WIDTH
    # Sign-negated to match ambient.observer_profile's own established
    # -x-propagation convention (T28's src_x>obj_x>plane_x geometry) --
    # this extraction was already correct in the Phase-1 proposal,
    # confirmed by EM's Phase-2 critique.
    profile = -sc.flux_profile_x(ph, plane_x_behind(cfg), y_lo, y_hi)
    return float(np.sum(profile))


def observer_record_t28(sim_scaffold, cap, cfg):
    """Fix 4 (RT-4/EM, independently re-derived by Red Team): NO array
    mirror (a bare index-reversal of Hy without the required pseudovector
    sign flip exactly cancels the intended correction). Instead: an
    unmirrored `emit.observer_record` call, then swap which of its two
    already-correct scalar totals means "toward the observer" for this
    bench's geometry (src_x>obj_x>plane_x, opposite emit.py's own assumed
    low-x/+x-source convention -- the same mismatch
    `sections.widths_direction_corrected` already corrects for via a
    scalar relabeling, never an array mirror)."""
    capture_tuple = (cap["ez_a"], cap["hy_a"], cap["ez_b"], cap["hy_b"], cap["off"])
    _, _, aux = emit.observer_record(sim_scaffold, capture_tuple, plane_x_obs(cfg), reference=None)
    # emit.py's own convention: p_forward_total = sum p_fwd (a+, +x-
    # traveling); p_backward_total = sum p_bwd (a-, -x-traveling). This
    # bench's injected beam IS the -x-traveling wave (source at high-x),
    # so the quantity toward the TRUE observer (back the way the beam
    # came, i.e. +x, toward high-x) is p_forward_total, not
    # p_backward_total.
    return dict(p_observer_raw=aux["p_forward_total"], p_incident_raw=aux["p_backward_total"])


def run_leg_b():
    preflight = registration_preflight(LEG_B_ANGLES, config_keys=PAIR_KEYS_R4)
    assert preflight["all_clean"], f"REGISTRATION GATE FAILED for {LEG_B_ANGLES}: HALT"

    jobs = []
    for th in LEG_B_ANGLES:
        for key in PAIR_KEYS_R4:
            jobs.append((key, th, False, dg.R4_STEPS, None))
            jobs.append((key, th, True, dg.R4_STEPS, SIGMA_R4_CORRECTED))
    assert len(jobs) == 24, f"R19 call-count assert: expected 24 jobs, got {len(jobs)}"
    t0 = time.time()
    captures, wall = run_block_r4(jobs)
    assert len(captures) == 24, f"R19: expected 24 captures, got {len(captures)}"

    scaffolds = {key: _fresh_sim_scaffold(dg.R4_CONFIGS[key]) for key in PAIR_KEYS_R4}

    xi_pass, nonneg_pass = True, True
    cells = {}
    for th in LEG_B_ANGLES:
        for key in PAIR_KEYS_R4:
            cap_empty = captures[(key, th, False, dg.R4_STEPS)]
            cap_article = captures[(key, th, True, dg.R4_STEPS)]
            cell = cell_metrics_r4(key, th, dg.R4_STEPS, cap_empty, cap_article)
            cells[(key, th)] = cell
            for xi in cell["xi_ext"].values():
                if xi > XI_TOL:
                    xi_pass = False
            if not cell["sigma_abs_nonneg"]:
                nonneg_pass = False
    assert xi_pass, "xi_ext gate FAILED -- extinction-routes disagreement; HALT"
    assert nonneg_pass, "sigma_abs>=0 gate FAILED; HALT"

    report = {}
    empty_self_ratios = {}
    for th in LEG_B_ANGLES:
        c_cell = cells[("C40_R4", th)]
        g_cell = cells[("G40_R4", th)]
        pm = pair_metrics_full(c_cell, g_cell, floor=FLOOR)
        nrow = netd_row(pm)
        assert set(nrow.keys()) >= NETD_ROW_KEYS, (
            f"MANDATORY netd_row() COVERAGE ASSERT FAILED at theta={th} -- "
            f"missing keys; HALT before results.json (fix 7)")

        row = dict(delta_scene=pm["delta_scene"], frac_contrast=pm["frac_contrast"],
                   ratio_k=pm["ratio_k"], floor_pass=pm["floor_pass"], **nrow)

        # New instruments (this cycle's own first-ever spend on this bench).
        for key in PAIR_KEYS_R4:
            cfg = dg.R4_CONFIGS[key]
            cap_empty = captures[(key, th, False, dg.R4_STEPS)]
            cap_article = captures[(key, th, True, dg.R4_STEPS)]
            bb_empty = beam_behind_t28(cap_empty, cfg)
            bb_article = beam_behind_t28(cap_article, cfg)
            obs_empty = observer_record_t28(scaffolds[key], cap_empty, cfg)
            obs_article = observer_record_t28(scaffolds[key], cap_article, cfg)
            # R18 mandatory validation gate: empty-scene self-ratio must
            # read near the established camera-floor scale (stage-6's own
            # "empty room returns ~nothing" bar, <0.02) before any
            # article-loaded reading from this same spend is trusted.
            self_ratio = (obs_empty["p_observer_raw"] / obs_empty["p_incident_raw"]
                          if obs_empty["p_incident_raw"] != 0 else float("inf"))
            empty_self_ratios[(key, th)] = self_ratio
            row[f"beam_behind_ratio_{key}"] = (bb_article / bb_empty) if bb_empty != 0 else float("inf")
            row[f"beam_behind_empty_{key}"] = bb_empty
            row[f"beam_behind_article_{key}"] = bb_article
            row[f"observer_empty_self_ratio_{key}"] = self_ratio
            row[f"observer_article_raw_{key}"] = obs_article["p_observer_raw"]
            row[f"observer_article_norm_{key}"] = (
                obs_article["p_observer_raw"] / obs_empty["p_incident_raw"]
                if obs_empty["p_incident_raw"] != 0 else float("inf"))
        report[th] = row

    validation_gate_pass = all(v < 0.02 for v in empty_self_ratios.values())

    return dict(preflight=preflight, report=report, wall_s=wall, n_calls=len(jobs),
                xi_pass=xi_pass, nonneg_pass=nonneg_pass,
                empty_self_ratios={f"{k[0]}@{k[1]}": v for k, v in empty_self_ratios.items()},
                validation_gate_pass=bool(validation_gate_pass))


# ================================================================ main
def main(dry_run=False):
    print("=" * 78)
    print("exp-100 -- First constraint-1/2/3 scoring pass on delta_scene(theta)")
    print("=" * 78)
    t_start = time.time()

    print("\n-- Tier 1, item 1: PAD-vs-article partition --")
    item1 = tier1_item1()
    print(f"  n_rows={item1['n_rows']}  by_family={item1['n_by_family']}")
    print(f"  r_pooled={item1['r_pooled']:.4f}  p_pooled={item1['p_pooled']:.4f}  "
          f"coupling_detected={item1['coupling_detected']}")
    for fam, d in item1["by_family"].items():
        print(f"  [{fam}] {d}")
    print(f"  Delta ratio_abs_ext: n={item1['delta_ratio_abs_ext_n']} "
          f"max={item1['delta_ratio_abs_ext_max']} mean={item1['delta_ratio_abs_ext_mean']}")

    print("\n-- Tier 1, item 2: MATERIALS' disposition memo --")
    item2 = tier1_item2(item1)
    print(f"  branch={item2['branch']} (disposition_memo.md written)")

    print("\n-- Tier 1, item 3: Richardson 4-point characterization at Null B --")
    item3 = tier1_item3()
    print(f"  magnitudes(|20-30|,|30-40|,|40-50|)={item3['magnitudes']}  "
          f"monotonic_decreasing={item3['monotonic_decreasing']}")
    print(f"  observed_ratio: 20/30/40={item3['observed_ratio_20_30_40']:.4f}  "
          f"30/40/50={item3['observed_ratio_30_40_50']:.4f}")
    print(f"  implied order p1={item3['implied_order_p1']:.4f}  p2={item3['implied_order_p2']:.4f}  "
          f"p_decreasing={item3['p_decreasing']}")

    print("\n-- Tier 2, Leg A: C_thr(L) desk score --")
    leg_a = tier2_leg_a(item1["rows_raw"])
    print(f"  n_in_window={leg_a.get('n_in_window')}  "
          f"peak_abs_delta_scene={leg_a.get('peak_abs_delta_scene')} "
          f"at theta={leg_a.get('peak_theta')} ({leg_a.get('peak_source')})")
    print(f"  pass_lab(<{C_THR_LAB})={leg_a.get('pass_lab')}  pass_field(<{C_THR_FIELD})={leg_a.get('pass_field')}")

    # Fix 3 (RT-3): pre-registered T1 label, decided by item 1's own THREE-WAY
    # outcome (Idealization 70 folds a family-stratified contradiction into
    # the ambiguous branch, not left to post-hoc judgment).
    if item1["outcome"] == "coupling_detected":
        t1_label = "angular-selectivity, partial/gated evidence -- scoped to this bench/600nm/tested-window only"
    elif item1["outcome"] == "majority_pad":
        t1_label = "N/A -- delta_scene excluded from the angular-selectivity class for this specific signal"
    else:
        t1_label = ("N/A, unresolved -- Tier 1's pooled/family-stratified results contradict each other "
                     "(Idealization 70); Tier 2's own numbers below are filed as instrument-"
                     "characterization only and do not move T1 in either direction")
    print(f"\n-- Pre-registered T1 label (fix 3), decided by Tier 1 item 1's outcome "
          f"({item1['outcome']}): {t1_label}")

    result = dict(
        experiment="exp-100", panel_iteration=77,
        tier1_item1={k: v for k, v in item1.items() if k != "rows_raw"},
        tier1_item2=item2, tier1_item3=item3, tier2_leg_a=leg_a,
        t1_label=t1_label,
    )

    if dry_run:
        print("\n[DRY RUN] Skipping Tier 2 Leg B (24 sim.run() calls). "
              "Validate the above, then re-run without --dry-run.")
        result["leg_b_skipped_dry_run"] = True
        with open(os.path.join(HERE, "results.json"), "w") as f:
            json.dump(result, f, indent=2, default=str)
        return result

    print(f"\n-- Tier 2, Leg B: {len(LEG_B_ANGLES)} angles x 2 keys x 2 conditions = "
          f"{len(LEG_B_ANGLES) * 4} sim.run() calls --")
    leg_b = run_leg_b()
    print(f"  wall_s={leg_b['wall_s']:.1f}  n_calls={leg_b['n_calls']}  "
          f"xi_pass={leg_b['xi_pass']}  nonneg_pass={leg_b['nonneg_pass']}")
    print(f"  R18 validation gate (empty-scene observer self-ratio < 0.02): "
          f"{leg_b['validation_gate_pass']}")
    print(f"  empty_self_ratios={leg_b['empty_self_ratios']}")
    for th, row in sorted(leg_b["report"].items()):
        print(f"  theta={th:+.6f}  delta_scene={row['delta_scene']:+.6e}  "
              f"beam_behind[C40_R4]={row.get('beam_behind_ratio_C40_R4')}  "
              f"observer_article_norm[C40_R4]={row.get('observer_article_norm_C40_R4')}")

    result["tier2_leg_b"] = leg_b
    result["total_wall_s"] = time.time() - t_start

    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(result, f, indent=2, default=str)
    print(f"\nTotal wall time: {result['total_wall_s']:.1f}s. results.json written.")
    return result


if __name__ == "__main__":
    main(dry_run="--dry-run" in sys.argv)
