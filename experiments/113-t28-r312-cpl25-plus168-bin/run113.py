"""exp-113 -- Panel Iteration 90, VISION SCIENCE's rotation-lead cycle:
executes the Reconciled Iteration-90 queue's Tier-1 items 1+2 (the
`+168.75deg` bin -- r=312/cpl=25, the companion of exp-112's own
`-146.25deg`/r=156 leg, both originally flagged by PHOTONICS' Iteration-85
self-review at ~10% local deviation), 3 (R30 null-calibrated Check C), and
4 (the CPL_RATIO raw-magnitude confound, diagnosed by PHOTONICS' own
Iteration-89 Phase-5 review -- see phase5_review_photonics.md F2/F3,
LOGBOOK.md R30).

This module holds ONLY shared geometry/classification code -- no
Sim.run() call anywhere in this file (Phase-1 discipline). Reuses, by
direct import, NEVER copy-paste: experiments/110-.../run.py (R110 --
classify_item_i_local, kappa_of, cost_gate_check, COST_GATE_PILOT_S/
TOTAL_S) and experiments/112-.../run112.py (R112 -- geom_fixedabs_cpl,
already verified byte-exact to R110.geom_fixedabs at cpl==20 for BOTH
r=156 and r=312; CPL_RATIO; neighbor_correlation_check's own pattern,
generalized here) and lab/sections.py (unmodified).

R29 (LOGBOOK.md RULED OUT registry, Iteration 89): this file is named
run113.py specifically so a downstream file doing `import run as R110`
immediately followed by `import run112 as R112` and `import run113 as R`
binds three genuinely distinct sys.modules entries. Executed identity
assertions live in chunk_runner113.py and analyze113.py, before either
trusts the distinction.
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
EXP110_DIR = os.path.join(ROOT, "experiments", "110-t28-item-i-local-norm-and-controls")
EXP112_DIR = os.path.join(ROOT, "experiments", "112-t28-cpl25-floor-spot-check")
sys.path.insert(0, ROOT)
sys.path.insert(0, EXP110_DIR)
sys.path.insert(0, EXP112_DIR)

from lab import sections as sc  # noqa: E402
import run as R110               # noqa: E402  (experiments/110-.../run.py)
import run112 as R112            # noqa: E402  (experiments/112-.../run112.py)

assert R110 is not R112, "R29: run110 and run112 must be distinct module objects"
assert hasattr(R112, "geom_fixedabs_cpl") and hasattr(R112, "CPL_RATIO"), (
    "R29: R112 must be exp-112's own run112.py")

with open(os.path.join(EXP110_DIR, "results.json")) as f:
    EXP110_RESULTS = json.load(f)
with open(os.path.join(EXP112_DIR, "results.json")) as f:
    EXP112_RESULTS = json.load(f)

# ================================================================ this cycle's own scope
R_THIS_CYCLE = 312                 # the companion bin's own r (exp-112 tested r=156 alone)
CPL_BASELINE = R110.CPL_600         # 20
CPL_TARGET = 25
CPL_RATIO = CPL_TARGET / CPL_BASELINE          # 1.25, bit-identical to R112.CPL_RATIO
assert CPL_RATIO == R112.CPL_RATIO
NAMED_BIN_DEG = 168.75              # the r=312 companion of exp-112's -146.25deg (exp-108/110
                                     # committed named bin; PHOTONICS' Iteration-85 self-review)
MARGIN = 32                         # same margin exp-112 tested at r=156, for direct symmetry

_BASELINE_R312 = EXP110_RESULTS["r312"]
BASELINE_BIN_CENTERS_DEG = _BASELINE_R312["bin_centers_deg"]
assert len(BASELINE_BIN_CENTERS_DEG) == 48, "expected 48 angular bins"
NAMED_BIN_IDX = int(np.argmin(np.abs(np.array(BASELINE_BIN_CENTERS_DEG) - NAMED_BIN_DEG)))
assert abs(BASELINE_BIN_CENTERS_DEG[NAMED_BIN_IDX] - NAMED_BIN_DEG) < 1e-9, (
    "named bin must sit exactly on a bin center at cpl=20 (it does: 168.75 == "
    "BIN_CENTERS_DEG[46], confirmed against exp-110's own committed results.json)")

_BASELINE_MARGIN32 = _BASELINE_R312["raw_patterns"][str(MARGIN)]
BASELINE_PECCORED = _BASELINE_MARGIN32["peccored"][NAMED_BIN_IDX]
BASELINE_HOLLOW = _BASELINE_MARGIN32["hollow"][NAMED_BIN_IDX]
BASELINE_DELTA = _BASELINE_MARGIN32["delta"][NAMED_BIN_IDX]
_BASELINE_LOCAL = _BASELINE_R312["local_diag"][str(MARGIN)]
BASELINE_FLOOR = _BASELINE_LOCAL["floor"]
BASELINE_SNR_PECCORED = _BASELINE_LOCAL["local_snr_peccored"][NAMED_BIN_IDX]
BASELINE_SNR_HOLLOW = _BASELINE_LOCAL["local_snr_hollow"][NAMED_BIN_IDX]
BASELINE_RESOLVED = _BASELINE_LOCAL["resolved"][NAMED_BIN_IDX]
BASELINE_LOCAL_REL = abs(BASELINE_DELTA) / abs(BASELINE_PECCORED)   # ~9.8-10%, matches the
                                                                     # Iteration-85 self-review's
                                                                     # own "~10%" figure, re-derived


def kappa_of(r):
    return R110.kappa_of(r)


def geom_fixedabs_cpl(r, cpl):
    """Reused, unmodified, from R112 -- already verified byte-exact to
    R110.geom_fixedabs(r) at cpl==20 for BOTH r=156 and r=312
    (R112.verify_geometry_identity(), re-run and asserted below)."""
    return R112.geom_fixedabs_cpl(r, cpl)


def verify_geometry_identity():
    """Re-exposes R112's own check (already covers r=312) so this cycle's
    own Phase-1/Phase-4 halts locally if it ever drifts, without
    duplicating the mismatch-scan logic."""
    return R112.verify_geometry_identity()


# ================================================================ cost gate (R27/R28, reused verbatim) + R31 same-session control
# R31 (LOGBOOK.md RULED OUT registry, founding instance exp-112, Iteration
# 89): a cross-session wall-time projection must include a same-session
# control point before it gates a scope-limiting decision. This cycle's
# own r=156/cpl=25 pilot (empty+hollow+peccored, 670.4778s total) was
# measured in a DIFFERENT session (Iteration 89) than this one -- the
# per-scene breakdown was not separately recoverable from exp-112's own
# committed results.json (its own top-level `total_wall_s` key was
# overwritten by analyze.py's own `dict(row, total_wall_s=...)` merge,
# clobbering row's per-scene dict -- a genuine, disclosed completeness
# gap, flagged for this cycle's own NOTES.md, not fixed retroactively in
# exp-112's frozen files). The per-STEP average IS recoverable exactly
# (all three r=156/cpl=25 scenes share identical STEPS=8000 and identical
# grid N=1400x1400): historical_per_step_s = 670.4778 / (3 * 8000) -- a
# 3-SCENE BLEND, not a per-scene rate.
# Fix 3a (Red Team's Phase-2 audit, ELECTROMAGNETISM's own finding,
# CORRECTING an earlier draft's false claim): per-step FDTD cost is NOT
# materials-invariant -- lab/fdtd2d.py::Sim.run() executes an extra
# per-step masked write (`if self.pec.any(): self.Ez[self.pec] = 0.0`)
# that ONLY the 'peccored' scene pays (empty/hollow have self.pec all-
# False, so `.any()` short-circuits False and the masked assignment never
# executes for them) -- an independently op-counted ~14% extra cost on
# peccored specifically (1 extra op / 7 baseline full-grid touches),
# EM's own estimate, explicitly NOT a profiled measurement (none can
# exist before Phase 4). HISTORICAL_PER_STEP_S is still a valid, honestly
# labeled 3-SCENE BLEND (2 cheap scenes + 1 ~14%-costlier scene,
# averaged) -- what was false was calling it scene-invariant. Fix 3b
# (below, r31_control_ratio/combine_control_readings) makes the
# same-session CONTROL re-time the identical 3-scene blend, so both sides
# of the R31 ratio are commensurable (blend-vs-blend), removing the
# anti-conservative asymmetry an empty-only control introduced.
HISTORICAL_R156_CPL25_TOTAL_S = EXP112_RESULTS["total_wall_s"]  # 670.4778 (all 3 scenes)
HISTORICAL_R156_CPL25_STEPS = R112.geom_fixedabs_cpl(156, 25)["STEPS"]  # 8000
HISTORICAL_PER_STEP_S = HISTORICAL_R156_CPL25_TOTAL_S / (3 * HISTORICAL_R156_CPL25_STEPS)

COST_GATE_PILOT_S = R110.COST_GATE_PILOT_S
COST_GATE_TOTAL_S = R110.COST_GATE_TOTAL_S


def r31_control_ratio(control_steps_per_scene, total_control_wall_s, n_scenes=3):
    """R31's own same-session control, as repaired by Fix 3b/Fix 4 (Red
    Team's Phase-2 audit, EM's/THERMODYNAMICS' own findings):
    `control_steps_per_scene` steps of EACH of the r=156/cpl=25
    empty+hollow+peccored scenes (already-completed historical combo,
    re-timed FRESH at the start of THIS session, cold builds, no
    checkpoint reuse), summed, so the control is a 3-scene BLEND
    commensurable with HISTORICAL_PER_STEP_S's own 3-scene blend (Fix 3b
    -- re-timing 'empty' alone against a historical figure that blends in
    peccored's own ~14%-costlier PEC-zeroing step was a real, signed,
    anti-conservative mismatch EM's own critique found). speed_ratio > 1
    means THIS session is FASTER than the historical (Iteration 89)
    session per step (matches that cycle's own ~2.19x cross-session
    finding, not assumed to transfer unchanged -- re-measured here)."""
    total_steps = control_steps_per_scene * n_scenes
    this_session_per_step_s = total_control_wall_s / total_steps
    speed_ratio = HISTORICAL_PER_STEP_S / this_session_per_step_s
    return dict(control_steps=control_steps_per_scene, n_scenes=n_scenes,
                control_wall_s=total_control_wall_s,
                historical_per_step_s=HISTORICAL_PER_STEP_S,
                this_session_per_step_s=this_session_per_step_s,
                speed_ratio=speed_ratio)


def combine_control_readings(short, sustained):
    """Fix 4 (Red Team's Phase-2 audit, THERMODYNAMICS' own finding): a
    single short (1000-step/scene) burst on r=156's small grid cannot see
    sustained-load effects (turbo-boost clock decay, cache/memory-
    bandwidth saturation) a multi-hour, 4x-larger r=312 production job
    would experience -- both biasing speed_ratio anti-conservatively (a
    short/light-load control reads faster than sustained large-grid
    reality). Takes a second, sustained-duration reading and gates on
    the LOWER of the two speed_ratio values (lower speed_ratio = this
    session reads/is assumed SLOWER relative to history = a LARGER,
    more conservative scaled projection)."""
    used = short if short["speed_ratio"] <= sustained["speed_ratio"] else sustained
    return dict(short=short, sustained=sustained, used_speed_ratio=used["speed_ratio"],
                used_label=("short" if used is short else "sustained"),
                historical_per_step_s=HISTORICAL_PER_STEP_S)


def cost_gate_check_r31(pilot_empty_wall_s, pilot_total_wall_s, control):
    """R31-compliant wrapper around R110.cost_gate_check(): reports BOTH
    the raw (uncontrolled, cross-session-as-if-same-speed) gate reading
    AND a same-session-scaled reading that divides the cross-session
    pilot times by the combined control's own `used_speed_ratio` (Fix 4 --
    the LOWER, more conservative of the short/sustained pair) before
    projecting -- the conservative-if-this-session-is-slower, honest-
    either-way version R31 exists to require. proceed_to_r312 (the actual
    gate) uses the scaled reading; the raw reading is reported alongside
    for disclosure, never used to gate. `control` is a
    combine_control_readings() dict."""
    raw = R110.cost_gate_check(pilot_empty_wall_s, pilot_total_wall_s)
    speed_ratio = control["used_speed_ratio"]
    scaled_empty = pilot_empty_wall_s / speed_ratio
    scaled_total = pilot_total_wall_s / speed_ratio
    scaled = R110.cost_gate_check(scaled_empty, scaled_total)
    return dict(raw=raw, scaled=scaled, control=control,
                proceed_to_r312=scaled["proceed_to_r312"])


# ================================================================ this cycle's own classification
SNR_K1 = 1.0
COLLAPSE_REL = 0.10
SURVIVE_REL_LO = 0.10
SURVIVE_REL_HI = 10.0

# ================================================================ Check C (R30 -- null-calibrated, not a bare fixed bar)
NEIGHBOR_HALF_WINDOW = 2
CORR_BAR_LEGACY = 0.5   # exp-112's own bar, kept for continuity/disclosure -- R30 forbids citing
                        # a bare pass/fail against it with evidentiary language; superseded below
                        # by the percentile-against-null reading, which this cycle actually scores on.


def _window_indices(idx, half=NEIGHBOR_HALF_WINDOW, n=48):
    return [(idx + k) % n for k in range(-half, half + 1)]


_BASELINE_WINDOW_IDX = _window_indices(NAMED_BIN_IDX)
BASELINE_WINDOW_DELTA = np.array(
    [_BASELINE_MARGIN32["delta"][i] for i in _BASELINE_WINDOW_IDX])


def windowed_corr(delta_a_48, delta_b_48, idx, half=NEIGHBOR_HALF_WINDOW):
    """Pearson correlation of the +/-half-bin window around idx, between
    two same-length 48-bin delta arrays. None if either window is
    constant (zero-variance, undefined correlation)."""
    wi = _window_indices(idx, half, n=len(delta_a_48))
    a = np.array([delta_a_48[i] for i in wi])
    b = np.array([delta_b_48[i] for i in wi])
    if np.std(a) == 0 or np.std(b) == 0:
        return None
    return float(np.corrcoef(a, b)[0, 1])


def neighbor_correlation_null_scan(delta_a_48, delta_b_48, half=NEIGHBOR_HALF_WINDOW):
    """R30 (LOGBOOK.md RULED OUT registry, founding instance exp-112,
    Iteration 89): a freshly-adopted discriminating statistic must be
    checked against its OWN computable null population before an
    evidentiary reading is trusted. Generalizes PHOTONICS'/QUANTUM's own
    Iteration-89 Phase-5 method (an exhaustive scan of all 48 window
    centers) to ANY two same-length delta arrays, so THIS cycle computes
    its own r=312-specific null population (exp-112's Phase-5 scan was
    r=156-specific; R30's own text says 'its own', not a borrowed
    calibration) once both cpl=20 (already committed) and cpl=25
    (this cycle's own Phase-4 output) r=312 patterns exist. Zero
    marginal FDTD cost."""
    n = len(delta_a_48)
    corrs = [windowed_corr(delta_a_48, delta_b_48, i, half) for i in range(n)]
    valid = [c for c in corrs if c is not None]
    return dict(all_window_corrs=corrs, n_valid=len(valid),
                median=float(np.median(valid)) if valid else None,
                min=float(np.min(valid)) if valid else None,
                max=float(np.max(valid)) if valid else None)


def resolved_unresolved_crosstab(resolved_mask_48, all_window_corrs_48):
    """Fix 5b (Red Team's Phase-2 audit, QUANTUM OPTICS' own finding,
    ratifying R32): splits the 48-bin windowed-correlation null-scan array
    by `classify_item_i_local`'s own `resolved` mask (both length-48,
    same bin ordering) and reports which direction, if either, this
    GEOMETRY's own real data actually supports -- genuinely validating
    (or invalidating) the low-percentile-outlier premise
    `classify_resolution_check` currently codes as the candidate reading,
    rather than assuming exp-112's own r=156 finding (resolved mean
    0.9793 < unresolved mean 0.9921, a thin, non-monotonic-with-SNR gap)
    transfers unchanged to r=312. Zero marginal FDTD cost -- both arrays
    are already computed by the time this is called."""
    resolved_corrs = [c for c, r in zip(all_window_corrs_48, resolved_mask_48) if r and c is not None]
    unresolved_corrs = [c for c, r in zip(all_window_corrs_48, resolved_mask_48) if (not r) and c is not None]
    if not resolved_corrs or not unresolved_corrs:
        return dict(n_resolved=len(resolved_corrs), n_unresolved=len(unresolved_corrs),
                    resolved_mean=None, unresolved_mean=None, direction_supported=None,
                    note="degenerate split at this geometry -- one population empty, "
                         "cannot compare (this cycle's own r=312/cpl=20 resolved mask "
                         "may differ in shape from exp-112's own r=156 one)")
    resolved_mean = float(np.mean(resolved_corrs))
    unresolved_mean = float(np.mean(unresolved_corrs))
    if resolved_mean < unresolved_mean:
        direction_supported = "low"    # resolved bins show LOWER corr -> low-percentile-outlier
    elif resolved_mean > unresolved_mean:
        direction_supported = "high"   # resolved bins show HIGHER corr -> matches the ORIGINAL
                                        # neighbor_correlation_check premise
    else:
        direction_supported = None
    return dict(n_resolved=len(resolved_corrs), n_unresolved=len(unresolved_corrs),
                resolved_mean=resolved_mean, unresolved_mean=unresolved_mean,
                resolved_range=[float(np.min(resolved_corrs)), float(np.max(resolved_corrs))],
                unresolved_range=[float(np.min(unresolved_corrs)), float(np.max(unresolved_corrs))],
                direction_supported=direction_supported)


def percentile_of(value, population):
    """Fraction of `population` <= value (0-100 scale) -- the R30
    null-calibrated reading Check C actually scores on, replacing a bare
    fixed-bar pass/fail."""
    population = np.asarray([p for p in population if p is not None], dtype=float)
    if value is None or len(population) == 0:
        return None
    return float(100.0 * np.mean(population <= value))


# ================================================================ Check B (normalized -- Item 4, the CPL_RATIO confound)
# PHOTONICS' own Iteration-89 Phase-5 finding (F3, independently confirmed
# by Red Team's final audit, LOGBOOK.md R30's own record and the
# Reconciled Iteration-90 queue item 4): lab/sections.py::_face_flux()
# sums Re(E x H*) over Yee-index CELLS with no physical
# cell-width (dx) normalization -- "cells" is a resolution-dependent unit,
# so a fixed PHYSICAL cross-section's raw flux-derived reading (peccored,
# hollow, delta, sigma_scat/abs/ext) is EXPECTED to scale by very nearly
# CPL_RATIO when cpl is refined under this program's own congruent-
# resolution recipe (confirmed to <0.03% on three independent quantities,
# both r=156's arrays). This is NOT a defect in run112.py/run113.py's own
# geometry code (tau_shell/sigma_max ARE correctly held cpl-invariant);
# it is a units artifact in a SHARED, validated, trust-suite-gated
# library function this cycle does NOT modify (the safer of R30-adjacent
# item 4's own two disclosed options: normalize at the point of use,
# never touch lab/sections.py's own trust-gated behavior for every other
# caller that compares WITHIN one cpl, where this factor cancels and was
# never visible). Consequence, undisclosed until this cycle: exp-112's
# own Check B, AS CONSTRUCTED, compared raw delta[idx] cpl=20 vs cpl=25
# WITHOUT dividing out this ~1.25x systematic -- meaning Check B would
# trivially read 'SURVIVES' (same sign, within 1 order of magnitude) at
# ANY bin whatsoever purely from the units artifact, independent of real
# structure -- the same zero-discriminating-power failure mode R30 named
# for Check C, same root cause, previously unrecognized for Check B
# specifically. This cycle normalizes Check B by dividing delta_cpl25 by
# CPL_RATIO before the magnitude comparison, and reports BOTH the raw
# (legacy, exp-112-comparable) and normalized readings.
def classify_resolution_check(delta_pattern_cpl25, peccored_cpl25, hollow_cpl25,
                               local_diag_cpl25_at_idx, baseline_delta_48_cpl20):
    delta_cpl25 = float(delta_pattern_cpl25[NAMED_BIN_IDX])
    delta_cpl25_normalized = delta_cpl25 / CPL_RATIO

    # Fix 5 (Red Team's Phase-2 audit, exp-113, ratifying R32): the ORIGINAL
    # `neighbor_correlation_check` docstring (run112.py) states the mechanistic
    # premise as HIGH correlation across cpl = real structure ("a genuine
    # deterministic sub-wavelength field feature should imprint spatially
    # CORRELATED structure ... unlike uncorrelated Yee-grid discretization
    # noise"). An earlier draft of THIS cycle's own code silently inverted
    # that premise (LOW percentile = real), justified only by a post-hoc
    # reading of the SAME r=156 dataset whose own miscalibration motivated
    # R30 -- QUANTUM's own Phase-2 critique caught this, Red Team's own audit
    # confirmed it independently and ruled it a genuine, unvalidated direction
    # flip (R32: a recalibrated statistic's DIRECTION, not just its threshold,
    # needs independent validation at the geometry under test before an
    # evidentiary reading in EITHER direction). Per R32/Fix 5: this cycle
    # reports BOTH tails, undirected, and asserts neither as "supports real
    # structure" until analyze113.py's own resolved-vs-unresolved
    # cross-tabulation (Fix 5b, computed post-Phase-4 on r=312's own real
    # data) shows which direction, if either, is locally supported.
    check_c_null = neighbor_correlation_null_scan(baseline_delta_48_cpl20, delta_pattern_cpl25)
    corr_named = windowed_corr(baseline_delta_48_cpl20, delta_pattern_cpl25, NAMED_BIN_IDX)
    percentile_named = percentile_of(corr_named, check_c_null["all_window_corrs"])
    check_c = dict(corr=corr_named, bar_legacy=CORR_BAR_LEGACY,
                    clears_legacy_bar=(corr_named is not None and corr_named >= CORR_BAR_LEGACY),
                    null_scan=check_c_null,
                    percentile_in_null=percentile_named,
                    low_percentile_outlier=(percentile_named is not None and percentile_named <= 10.0),
                    high_percentile_outlier=(percentile_named is not None and percentile_named >= 90.0),
                    direction_validated=False)  # R32: true only once Fix 5b's cross-tab runs

    snr_p_new = local_diag_cpl25_at_idx["local_snr_peccored"]
    snr_h_new = local_diag_cpl25_at_idx["local_snr_hollow"]
    resolved_new = local_diag_cpl25_at_idx["resolved"]
    snr_p_improved = (snr_p_new is not None) and (snr_p_new > BASELINE_SNR_PECCORED)
    snr_h_improved = (snr_h_new is not None) and (snr_h_new > BASELINE_SNR_HOLLOW)
    clears_k1_new = (snr_p_new is not None and snr_h_new is not None
                      and snr_p_new >= SNR_K1 and snr_h_new >= SNR_K1)
    if clears_k1_new:
        check_a = ("SURVIVES (newly clears K=1 floor -- Check C reported undirected per R32/Fix 5, "
                    "NOT yet upgraded to 'candidate real structure' in either tail pending the "
                    "resolved-vs-unresolved cross-tabulation)")
    elif not (snr_p_improved or snr_h_improved):
        check_a = "COLLAPSES (no improvement in local_snr under refinement -- noise-consistent)"
    else:
        check_a = "AMBIGUOUS (some local_snr improvement, still below K=1)"

    def _check_b(delta_val, baseline_val, label):
        same_sign = (np.sign(delta_val) == np.sign(baseline_val)) if baseline_val != 0 else None
        rel = abs(delta_val) / abs(baseline_val) if baseline_val != 0 else float("inf")
        if (not same_sign) or rel < COLLAPSE_REL:
            verdict = f"COLLAPSES ({label})"
        elif SURVIVE_REL_LO <= rel <= SURVIVE_REL_HI and same_sign:
            verdict = f"SURVIVES ({label})"
        else:
            verdict = f"AMBIGUOUS ({label})"
        return dict(verdict=verdict, same_sign=bool(same_sign) if same_sign is not None else None,
                    rel_to_baseline=rel)

    check_b_raw = _check_b(delta_cpl25, BASELINE_DELTA, "raw, uncorrected for CPL_RATIO -- "
                            "legacy exp-112 construction, NOT this cycle's own scored reading")
    check_b_normalized = _check_b(delta_cpl25_normalized, BASELINE_DELTA,
                                   "normalized by CPL_RATIO -- this cycle's own scored reading")

    return dict(check_a=check_a, check_b_raw=check_b_raw, check_b_normalized=check_b_normalized,
                check_c=check_c, snr_p_new=snr_p_new, snr_h_new=snr_h_new,
                resolved_new=resolved_new, delta_cpl25=delta_cpl25,
                delta_cpl25_normalized=delta_cpl25_normalized)


# ================================================================ predictions/result text (R23 -- single source of truth)
# VISION SCIENCE's own Iteration-90 disclosure-completeness check (two additions,
# both computed here, not hand-typed -- R4 discipline):
#
# (a) exp-112's own corrected ABSORB/EDGE sponge disclosure (Phase-2 MATERIALS/EM,
#     Phase-5-corrected by MATERIALS from "6-8 orders" to "~1.8-4.5 orders",
#     LOGBOOK.md R30's own record) is REUSED, not re-derived: the sponge's one-way
#     accumulated log-attenuation at cpl=25/ABSORB=50 (17.242357, exp(-17.242357)=
#     3.249e-8) depends only on cpl, not r -- it is the IDENTICAL cpl=25 config this
#     cycle also uses (geom_fixedabs_cpl(312,25)["absorb"]==50==
#     geom_fixedabs_cpl(156,25)["absorb"]). What is genuinely NEW this cycle is the
#     comparison point: r=312's own floor scale differs from r=156's, so the
#     orders-of-magnitude margin is freshly (not blindly) computed against THIS
#     cycle's own r=312/cpl=20 floor (BASELINE_FLOOR, already loaded above).
_SPONGE_LOG_ATTEN_CPL25 = 17.242357   # exp-112 Phase-2/Phase-5-corrected figure, cpl=25-specific
_SPONGE_ABS_VAL = float(np.exp(-_SPONGE_LOG_ATTEN_CPL25))

# Fix 2 (Red Team's Phase-2 audit, MATERIALS' own finding): a single sponge-
# margin figure computed against BASELINE_FLOOR (the K=1 instrument-floor
# SCALE) silently answers a different question than "is the sponge below the
# signal/the quantity actually scored" -- three figures, each explicitly
# labeled against the operand it actually uses, replace the single ~4.02
# number VISION's own first draft shipped:
_SPONGE_MARGIN_ORDERS_FLOOR = float(np.log10(BASELINE_FLOOR / _SPONGE_ABS_VAL))
_SPONGE_MARGIN_ORDERS_SIGNAL = float(np.log10(min(abs(BASELINE_PECCORED), abs(BASELINE_HOLLOW))
                                               / _SPONGE_ABS_VAL))
_SPONGE_MARGIN_ORDERS_DELTA = float(np.log10(abs(BASELINE_DELTA) / _SPONGE_ABS_VAL))

# Fix 1 (Red Team's Phase-2 audit, PHOTONICS' own finding): box_a's clearance
# past the coat surface, in cells, is a FIXED PROPORTION of R_COAT by
# construction (BOX_A_MARGIN0 scaled the same way every other length is) --
# but in WAVELENGTHS (clearance_cells / cpl) it is NOT held constant across
# r, because kappa_of(r) itself grows with r. This is independent of the
# cpl=20->25 refinement (present already at cpl=20) and was undisclosed in
# VISION's own first draft.
_g156_25 = geom_fixedabs_cpl(156, 25)
_g312_25 = geom_fixedabs_cpl(312, 25)
_BOX_A_CLEARANCE_LAMBDA_R156 = (_g156_25["box_a"][1] - _g156_25["CX"] - _g156_25["R_COAT"]) / _g156_25["cpl"]
_BOX_A_CLEARANCE_LAMBDA_R312 = (_g312_25["box_a"][1] - _g312_25["CX"] - _g312_25["R_COAT"]) / _g312_25["cpl"]

DISCLAIMER = ("This is an instrument-fidelity/resolution-convergence check on "
              "an angular-scattering-pattern noise floor, not a phenomenon-"
              "mechanism proposal -- no sigma(I)/sigma(x,t)/angular-selectivity/"
              "sub-threshold content, no Weber-contrast or C_thr(L) perceptual "
              "scoring, is performed anywhere in this document. 'Coherent "
              "sub-wavelength structure', as used here, means spatially "
              "deterministic classical field structure, not quantum "
              "coherence. 'Detection floor' means the K=3/K=1 mirror-pooled-"
              "floor instrument's own grid-discretization SNR threshold -- NOT "
              "a human perceptual or observer-detection threshold; no "
              "constraint-2/3 claim is made or implied. Check C is scored as "
              "a PERCENTILE within its own null population of all 48 window "
              "correlations (R30), NOT a bare corr>=0.5 pass/fail -- exp-112's "
              "own Iteration-89 finding is that essentially every bin in this "
              "pattern clears a bare 0.5 bar (48/48), so clearing it alone "
              "carries no discriminating power. Fix 5/R32 (Red Team's Phase-2 "
              "audit, QUANTUM OPTICS' own finding): an EARLIER draft of this "
              "cycle's own code asserted that a LOW-percentile outlier is the "
              "only diagnostic Check-C reading -- this directly contradicted "
              "the ORIGINAL neighbor_correlation_check docstring's own "
              "premise (run112.py: HIGH correlation across cpl = real "
              "structure), was argued post-hoc from the same r=156 dataset "
              "whose own miscalibration motivated R30, and was never "
              "validated at r=312, the geometry this cycle actually tests. "
              "This document now reports BOTH tails, UNDIRECTED "
              "(low_percentile_outlier, high_percentile_outlier) and asserts "
              "'candidate real structure' in NEITHER direction -- "
              "direction_validated stays False until analyze113.py's own "
              "resolved-vs-unresolved windowed-correlation cross-tabulation "
              "(computed post-Phase-4, zero marginal FDTD cost, on r=312's "
              "own real data) shows which tail, if either, this geometry "
              "actually supports (R32: a recalibrated statistic's direction "
              "needs independent validation at the geometry under test, not "
              "just its threshold). Check C's own 'percentile'/'null population'/"
              "'outlier' vocabulary, immediately above, is a spatial-"
              "correlation-vs-grid-refinement statistic -- NOT a "
              "psychophysical signal-detection-theory statistic (a "
              "percentile of a fitted psychometric function, d-prime, "
              "hit/false-alarm rate); no perceptual-detectability claim is "
              "made or implied by this vocabulary anywhere in this document "
              "(VISION SCIENCE's own Iteration-90 addition, closing a "
              "term-scoping gap this seat's own charter exists to catch, "
              "in the R9/R30 'incommensurable-until-checked' lineage -- "
              "the vocabulary was never actually conflated with a "
              "perceptual claim in this document's own code or predictions/"
              "result text, so no verdict-arithmetic is affected; this is a "
              "prophylactic disambiguation of a term-reuse risk, not a "
              "correction of a discovered error). Check B is reported BOTH raw (exp-112's own "
              "uncorrected construction) and normalized by CPL_RATIO=1.25 -- "
              "PHOTONICS' own Iteration-89 Phase-5 finding (LOGBOOK.md R30's "
              "record) traced an unexplained ~1.25x multiplicative "
              "discrepancy between raw cpl=20/cpl=25 flux-derived quantities "
              "to lab/sections.py::_face_flux()'s own missing physical "
              "cell-width (dx) normalization -- 'cells' is a "
              "resolution-dependent unit, so this program's own congruent-"
              "cpl-refinement recipe (which holds PHYSICAL extents fixed "
              "while cpl grows) mechanically inflates every raw grid-unit "
              "flux reading by very nearly CPL_RATIO, independent of any "
              "real near-field structure. Un-normalized, Check B would read "
              "'SURVIVES' at essentially any bin from this artifact alone; "
              "this cycle's own scored Check-B reading is the "
              "CPL_RATIO-normalized one. lab/sections.py itself is NOT "
              "modified (a shared, trust-suite-gated library function every "
              "other caller in this program compares WITHIN one cpl, where "
              "this factor cancels and was never visible) -- the fix is "
              "applied at the point of cross-cpl comparison only, this "
              "cycle's own code. "
              f"The domain-edge sponge (ABSORB/EDGE=50 cells, cpl=25) carries "
              f"the SAME one-way accumulated log-attenuation exp-112's own "
              f"Phase-2/Phase-5-corrected figure established "
              f"({_SPONGE_LOG_ATTEN_CPL25}, exp(-{_SPONGE_LOG_ATTEN_CPL25})="
              f"{_SPONGE_ABS_VAL:.3e}) -- REUSED, not re-derived, since "
              f"ABSORB/EDGE depends only on cpl, not on r=156 vs r=312. "
              f"Fix 2 (Red Team's Phase-2 audit, MATERIALS' own finding): a "
              f"single margin figure computed against BASELINE_FLOOR (the "
              f"K=1 instrument-floor SCALE) answers a different question "
              f"than 'is the sponge below the signal/what Check B actually "
              f"scores' -- THREE figures, each against the operand it "
              f"actually uses: relative to the instrument's own K=1 "
              f"noise-floor scale ({BASELINE_FLOOR:.3e}), "
              f"~{_SPONGE_MARGIN_ORDERS_FLOOR:.2f} orders of magnitude; "
              f"relative to the named bin's own signal magnitude "
              f"(min(|peccored|,|hollow|)={min(abs(BASELINE_PECCORED), abs(BASELINE_HOLLOW)):.3e}), "
              f"~{_SPONGE_MARGIN_ORDERS_SIGNAL:.2f} orders; relative to "
              f"|delta|={abs(BASELINE_DELTA):.3e} (the quantity Check B "
              f"actually scores), ~{_SPONGE_MARGIN_ORDERS_DELTA:.2f} orders "
              f"-- all three non-fatal (consistent with, not a "
              f"re-introduction of, MATERIALS' own Iteration-89 correction, "
              f"'~1.8-4.5 orders, not 6-8'), but genuinely different "
              f"numbers, not interchangeable. "
              f"Fix 1 (Red Team's Phase-2 audit, PHOTONICS' own finding): "
              f"box_a's clearance past the coat surface, in wavelengths, is "
              f"{_BOX_A_CLEARANCE_LAMBDA_R156:.1f}lambda at r=156 (exp-112) "
              f"but {_BOX_A_CLEARANCE_LAMBDA_R312:.1f}lambda at r=312 (this "
              f"cycle) -- exactly kappa_ratio=2.0, independent of the "
              f"cpl=20->25 refinement (present already at cpl=20). "
              f"margin=32 preserves the PROPORTIONAL margin/R_COAT ratio "
              f"(a genuinely self-similar family) but NOT the near-field "
              f"depth in wavelengths -- Phase 5 must not read this leg's "
              f"outcome and exp-112's own -146.25deg/r=156 outcome as "
              f"probing the same physical near-field depth 'companion' "
              f"question; only the same proportional-margin construction "
              f"at two different physical depths. Non-blocking for this "
              f"leg's own self-referential falsification (each check scores "
              f"against its own r's own cpl=20 baseline). "
              "This leg tests r=312 alone, at cpl=25, "
              "gated by R31's own same-session control (re-timed this "
              "session, not assumed to transfer exp-112's own cross-session "
              "figure unchanged) before any r=312 Sim.run() is attempted.")


def build_predictions_text(control=None, gate=None):
    control_line = ""
    if control is not None and gate is not None:
        control_line = (f"\n\n**R31 same-session control (Fix 3b/Fix 4, measured "
                         f"pre-Phase-4-gate-decision, this session)**: two commensurable "
                         f"3-scene-blend re-timings (empty+hollow+peccored, matching "
                         f"HISTORICAL_PER_STEP_S's own 3-scene blend -- Fix 3b) of the "
                         f"already-completed r=156/cpl=25 scenes, fresh cold builds -- "
                         f"a short burst ({control['short']['control_steps']} steps/scene, "
                         f"{control['short']['this_session_per_step_s']:.5f}s/step) and a "
                         f"sustained reading ({control['sustained']['control_steps']} "
                         f"steps/scene, {control['sustained']['this_session_per_step_s']:.5f}"
                         f"s/step, Fix 4) -- gated on the LOWER (more conservative) of the "
                         f"two speed_ratio values ({control['short']['speed_ratio']:.3f} "
                         f"short vs. {control['sustained']['speed_ratio']:.3f} sustained; "
                         f"used={control['used_speed_ratio']:.3f}) vs. the historical "
                         f"(Iteration 89 session) average {control['historical_per_step_s']:.5f}"
                         f"s/step. Scaled cost-gate projection: "
                         f"{gate['scaled']['projected_312_total_s']:.1f}s vs. the "
                         f"{COST_GATE_TOTAL_S}s bound -- proceed_to_r312="
                         f"{gate['proceed_to_r312']}.")
    return f"""PREDICTIONS (pre-registered, exp-113, Panel Iteration 90)

{DISCLAIMER}{control_line}

**Geometry identity (zero-FDTD, pre-Phase-4)**: verify_geometry_identity()
returns pass_=True at both r=156 and r=312 (already re-run above).
Falsified by any mismatch -- HALT before any Sim.run() call.

**Reproduction/self-consistency precondition**: sum(sigma_scat_per_bin) ==
sigma_scat (angular_scattered_pattern's own docstring identity) to <1e-9
relative, at margin=32, both peccored and hollow captures, r=312, cpl=25.
Falsified by any larger deviation -- HALT before the named-bin comparison
is trusted.

**Named bin ({NAMED_BIN_DEG}deg, r=312, margin=32, bin index {NAMED_BIN_IDX}) --
the genuinely uncertain question this leg exists to answer**:
Check A (mirror-pooled-floor instrument, reused unmodified, at cpl=25):
SURVIVES if local_snr_peccored AND local_snr_hollow both clear {SNR_K1}
(cpl=20 values: {BASELINE_SNR_PECCORED:.4f}/{BASELINE_SNR_HOLLOW:.4f});
COLLAPSES if neither local_snr improves over cpl=20; else AMBIGUOUS.
Check B-normalized (this cycle's own scored reading, CPL_RATIO-divided):
SURVIVES if delta[idx]/CPL_RATIO keeps the same sign as cpl=20
({BASELINE_DELTA:.6e}) and stays within one order of magnitude of it;
COLLAPSES on a sign flip or a >=10x drop; else AMBIGUOUS. Check B-raw
(uncorrected, exp-112-comparable, disclosed but NOT scored) reported
alongside. Check C (R30 null-calibrated, R32/Fix 5 UNDIRECTED): reports
whether the named bin's own +/-{NEIGHBOR_HALF_WINDOW}-bin correlation is a
low_percentile_outlier (<=10th percentile) and/or a high_percentile_outlier
(>=90th percentile) of this cycle's own 48-window null population -- NEITHER
tail is asserted as "candidate real structure" this cycle (direction_validated
stays False) regardless of Check A's own reading, pending the
resolved-vs-unresolved cross-tabulation (Fix 5b, computed post-Phase-4 on
r=312's own real data, zero marginal FDTD cost). No advance position taken
on which outcome any of the three checks, or either Check-C tail, will
report.
"""


def build_result_text(n_fdtd_calls, total_wall_s, geom_ok, repro_ok,
                       named_bin_result, wall_time_source=None):
    wall_time_note = f"\n({wall_time_source})" if wall_time_source else ""
    return f"""RESULT (exp-113, Panel Iteration 90)

{DISCLAIMER}

{n_fdtd_calls} real FDTD calls, {total_wall_s:.1f}s ({total_wall_s/60.0:.2f} min)
total wall time this cycle, zero `lab/` diff.{wall_time_note}

**Geometry identity: {'PASS' if geom_ok else 'FAIL'}.**
**Reproduction/self-consistency precondition: {'PASS' if repro_ok else 'FAIL'}.**
**Named bin ({NAMED_BIN_DEG}deg, r=312, margin=32):** {named_bin_result}
"""


if __name__ == "__main__":
    if "--predictions-only" in sys.argv:
        print(build_predictions_text())
    elif "--verify-geometry" in sys.argv:
        result = verify_geometry_identity()
        print(json.dumps(result, indent=2))
        assert result["pass_"], "geom_fixedabs_cpl does not reduce to R.geom_fixedabs at cpl==20"
        print("verify_geometry_identity: PASS")
    else:
        print("This module holds shared geometry/constants and analysis functions only.")
