"""exp-108 -- Tier-1 batch: `angular_scattered_pattern` on the
hollow-vs-PEC-cored fixed-absolute-thickness pair (r=156/312), an
absolute box-ledger noise floor (six-margin family, detrended per the
EM+QUANTUM unified fix), the numerator floor-gate check on the PEC-cored
PRIMARY article, and shared machinery for the chunked-vs-continuous
suite-stage identity gate (item iv). Panel Iteration 85. Frozen spec:
NOTES.md (Predictions committed to git strictly BEFORE this file's first
real `Sim.run()` call, house discipline). Change rationale:
phase2_redteam_audit.md (5 numbered attacks, all five blind critiques
ADOPTED in full; EM's and QUANTUM's remedies combined into one unified
multi-margin fix; verdict PROCEED-WITH-MANDATORY-FIXES).

This file holds shared geometry/constants (re-derived byte-for-byte from
exp-106's own formula chain, gated against exp-106's own committed
`geom_156_fixedabs`/`geom_312_fixedabs` before any new `Sim.run()`), the
R23 `DISCLAIMER`/predictions/result text pipeline, and all zero-FDTD
post-processing/classification functions. This session's own
backgrounded/nohup execution mode is confirmed pathologically slow for
sustained FDTD numpy work (exp-107's own A/B-tested finding, reused
without re-testing) -- actual capture is via `chunk_runner.py`
(checkpoint/resume, foreground Bash calls only); analysis is via
`analyze.py`, both importing this module.
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, ROOT)

from lab import sections as sc  # noqa: E402

EXP106_DIR = os.path.join(ROOT, "experiments", "106-t28-kappa-window-floor-fixedabs-control")
with open(os.path.join(EXP106_DIR, "results.json")) as f:
    EXP106_RESULTS = json.load(f)

# ================================================================ exp-106's own formula chain, reused byte-for-byte
DX_M = 30.0e-9
R_BASE = 78
N0, ABSORB, EDGE, TAPER = 560, 40, 40, 40
CX0, CY0, SRC_X0 = 252, 280, 64
R_CORE0 = 30
STEPS0 = 3200
SIGMA_MAX0 = 0.5
CPL_600 = 20
COURANT_FRAC = 0.32

FLOOR_FRAC = 0.10
ABS_THICKNESS = 48          # cells, HELD CONSTANT across r (exp-052's own established value)
SIGMA_MAX_FIXED = 0.5       # HELD CONSTANT across r

BOX_A_MARGIN0 = 32
BOX_B_MARGIN0 = 57
REF_HH0 = 60

# ---------------------------------------------- absolute-floor / angular-pattern box family (this cycle, new)
MARGINS = (24, 32, 40, 48, 57, 65)  # cells at r=78-equivalent scale; scaled by kappa below (32/57 = box_a/box_b)

# item-1(angular)/item-ii cost gate (NOTES.md, disclosed): abort r=312 leg if projected exceeds this
COST_GATE_PILOT_S = 90 * 60
COST_GATE_TOTAL_S = 180 * 60

# ---------------------------------------------- item i/ii classification bands (pre-registered, NOTES.md)
ITEM_I_CONFIRM_REL = 0.05
ITEM_I_REFUTE_REL = 0.15
ITEM_I_MIN_RUN = 3           # contiguous bins
R2_SMOOTH_THRESHOLD = 0.90

# |Delta_boxA| (margin=32), already measured exp-107, this identical hollow-vs-PEC-cored pair
DELTA_BOXA = {156: 2.969e-5, 312: 2.468e-5}

CLOSURE_CONFIRM = 0.001
CLOSURE_FALSIFY = 0.01


def kappa_of(r):
    return r / R_BASE


def geom_fixedabs(r):
    """Fixed-absolute-thickness family, byte-for-byte reused from
    exp-106's own `geom_fixedabs()` (which itself extends `geom()`).
    Reproduced independently here (not imported -- exp-106's own run.py
    executes real Sim.run() calls at module scope if run as __main__; this
    file re-derives the formula chain directly, matching exp-107's own
    established pattern of reproducing rather than importing exp-106)."""
    k = kappa_of(r)
    N = round(N0 * k)
    CX = round(CX0 * k)
    CY = round(CY0 * k)
    SRC_X = round(SRC_X0 * k)
    STEPS = round(STEPS0 * k)
    R_COAT = r
    R_CORE = r - ABS_THICKNESS
    sigma_max = SIGMA_MAX_FIXED
    tau_shell = sigma_max * (R_COAT - R_CORE)
    behind_x_lo = CX + R_COAT + 27
    behind_x_hi = CX + R_COAT + 127
    behind_y_lo = CY - 20
    behind_y_hi = CY + 20
    box_a_hw = R_COAT + round(BOX_A_MARGIN0 * k)
    box_b_hw = R_COAT + round(BOX_B_MARGIN0 * k)
    box_a = (CX - box_a_hw, CX + box_a_hw, CY - box_a_hw, CY + box_a_hw)
    box_b = (CX - box_b_hw, CX + box_b_hw, CY - box_b_hw, CY + box_b_hw)
    ref = (CX, CY, round(REF_HH0 * k))
    margin_boxes = {}
    for m in MARGINS:
        hw = R_COAT + round(m * k)
        margin_boxes[m] = (CX - hw, CX + hw, CY - hw, CY + hw)
    return dict(r=r, k=k, N=N, CX=CX, CY=CY, SRC_X=SRC_X, STEPS=STEPS,
                R_CORE=R_CORE, R_COAT=R_COAT, sigma_max=sigma_max, tau_shell=tau_shell,
                behind=(behind_x_lo, behind_x_hi, behind_y_lo, behind_y_hi),
                box_a=box_a, box_b=box_b, ref=ref, margin_boxes=margin_boxes,
                family="fixedabs")


def gate_p0(g):
    """Cross-check this file's own re-derived geom_fixedabs(r) against
    exp-106's own committed geom_{r}_fixedabs on every shared field --
    HALT before any new Sim.run() call if these disagree."""
    key = f"geom_{g['r']}_fixedabs"
    committed = EXP106_RESULTS[key]
    shared_fields = ("N", "CX", "CY", "SRC_X", "STEPS", "R_CORE", "R_COAT", "sigma_max", "tau_shell")
    mismatches = []
    for field in shared_fields:
        mine = g[field]
        theirs = committed[field]
        if isinstance(mine, float) or isinstance(theirs, float):
            ok = abs(float(mine) - float(theirs)) < 1e-9
        else:
            ok = mine == theirs
        if not ok:
            mismatches.append((field, mine, theirs))
    return dict(pass_=(len(mismatches) == 0), mismatches=mismatches)


def reproduction_precondition(cap_peccored, cap_empty, g):
    """Fresh PEC-cored capture's sections.widths() at box_a must reproduce
    exp-106's own committed ledger_r{r}['fixedabs'] to <1e-6 relative --
    HALT before any angular claim is trusted (NOTES.md, item i)."""
    w = sc.widths(cap_peccored, cap_empty, g["box_a"], g["ref"])
    w = dict(w)
    w["abs_ext_ratio"] = w["sigma_abs"] / w["sigma_ext"]
    key = f"ledger_r{g['r']}"
    committed = EXP106_RESULTS[key]["fixedabs"]
    checks = {}
    for field in ("sigma_abs", "sigma_ext", "abs_ext_ratio"):
        mine = w[field]
        theirs = committed[field]
        rel = abs(mine - theirs) / abs(theirs) if theirs else float("inf")
        checks[field] = dict(mine=mine, committed=theirs, rel_dev=rel, pass_=bool(rel < 1e-6))
    return dict(pass_=all(c["pass_"] for c in checks.values()), checks=checks, widths=w)


def abs_ext_ratio_at_margin(cap_article, cap_empty, g, margin, ref=None):
    box = g["margin_boxes"][margin]
    w = sc.widths(cap_article, cap_empty, box, ref if ref is not None else g["ref"])
    return w


def linear_fit_1_over_margin(margins, values):
    """Fit values = A + B/margin (least squares); return A, B, residuals,
    residual_std, R^2. Used to detrend the six-margin family (EM+QUANTUM
    unified fix, NOTES.md item ii): box radius is not an exchangeable
    nuisance parameter, so a smooth near-to-far-field convergence trend
    must be removed before what remains is treated as a noise floor."""
    x = np.array([1.0 / m for m in margins])
    y = np.array(values, dtype=float)
    A_mat = np.vstack([np.ones_like(x), x]).T
    coeffs, _, _, _ = np.linalg.lstsq(A_mat, y, rcond=None)
    A, B = coeffs
    fitted = A + B * x
    residuals = y - fitted
    residual_std = float(np.std(residuals))
    ss_res = float(np.sum(residuals ** 2))
    ss_tot = float(np.sum((y - np.mean(y)) ** 2))
    r_squared = 1.0 - ss_res / ss_tot if ss_tot != 0 else 1.0
    is_monotonic = bool(np.all(np.diff(y) > 0) or np.all(np.diff(y) < 0))
    return dict(A=float(A), B=float(B), residuals=residuals.tolist(),
                residual_std=residual_std, r_squared=float(r_squared),
                is_monotonic=is_monotonic, smooth=bool(is_monotonic or r_squared >= R2_SMOOTH_THRESHOLD))


def classify_item_ii(r, fit, delta_values):
    """R24 second-instance fix (Panel Iteration 86, exp-109): gate the
    reported floor statistic on fit["smooth"], mirroring classify_item_i's
    own smoothness-gated fit machinery. When the 6-margin sequence is
    smooth, use the detrended residual_std (exp-108's own original logic,
    unchanged). When it is not smooth, fall back to the raw, undetrended
    np.std(delta_values) -- the original Iteration-85 mandatory fix's own
    text already specifies this as the non-smooth default (a stronger
    ground than the OLS-inequality proof alone, itself independently
    airtight: for any OLS fit with an intercept, residual_std <= raw_std
    always, since the constant model is a feasible fit point -- 'residual
    std' can never exceed 'raw std'). NOTE this inequality is one-sided:
    the raw-std fallback is conservative against manufacturing a false
    CONFIRM (it cannot make the reported floor read smaller than the
    trusted detrended estimate) but simultaneously liberal/anti-
    conservative against a false REFUTE (inflating the statistic only
    ever makes stat>=boxA easier to satisfy) -- NOT 'more conservative in
    every case.'"""
    boxA = DELTA_BOXA[r]
    raw_std = float(np.std(delta_values))
    ratio = raw_std / fit["residual_std"] if fit["residual_std"] else float("inf")
    if fit["smooth"]:
        stat = fit["residual_std"]
        stat_source = (f"detrended (fit smooth: is_monotonic={fit['is_monotonic']}, "
                        f"r_squared={fit['r_squared']:.4f})")
    else:
        stat = raw_std
        stat_source = (f"raw/undetrended (fit NOT smooth: is_monotonic={fit['is_monotonic']}, "
                        f"r_squared={fit['r_squared']:.4f} < {R2_SMOOTH_THRESHOLD:.2f} -- "
                        f"residual_std is not trusted as 'the genuine floor'; falls back to "
                        f"raw std, which is provably >= residual_std for any OLS fit with an "
                        f"intercept term (conservative against a false CONFIRM; liberal/"
                        f"anti-conservative against a false REFUTE, since inflating the "
                        f"statistic only ever makes stat>=boxA easier to satisfy -- NOT "
                        f"'conservative in every case'). raw/residual ratio this point: "
                        f"{ratio:.3f}x)")
    if stat <= 0.5 * boxA:
        verdict = "CONFIRM"
    elif stat >= boxA:
        verdict = "REFUTE"
    else:
        verdict = "AMBIGUOUS"
    return dict(verdict=verdict, stat_used=stat, stat_source=stat_source, boxA=boxA,
                raw_std=raw_std, residual_std=fit["residual_std"],
                raw_over_residual_ratio=ratio)


def classify_item_i(pattern_by_margin_delta, sigma_scat_by_margin_peccored, r):
    """pattern_by_margin_delta: {margin: np.array([48]) of Delta_pattern}
    sigma_scat_by_margin_peccored: {margin: np.array([48]) of PEC-cored sigma_scat_per_bin, floor-cleared mask applied upstream}
    Implements the 3-way classification, NOTES.md item i."""
    margin32 = 32
    delta32 = pattern_by_margin_delta[margin32]
    peccored32 = sigma_scat_by_margin_peccored[margin32]
    max_peccored32 = float(np.max(np.abs(peccored32))) if np.max(np.abs(peccored32)) > 0 else 1e-30
    rel32 = np.abs(delta32) / max_peccored32

    # CONFIRM check: at margin=32, every floor-cleared bin <=5% rel, AND holds at all 6 margins
    confirm_all_margins = True
    for m in MARGINS:
        dm = pattern_by_margin_delta[m]
        pm = sigma_scat_by_margin_peccored[m]
        maxpm = float(np.max(np.abs(pm))) if np.max(np.abs(pm)) > 0 else 1e-30
        relm = np.abs(dm) / maxpm
        if np.any(relm > ITEM_I_CONFIRM_REL):
            confirm_all_margins = False
            break

    # candidate contiguous runs at margin=32 clearing REFUTE bar
    n_bins = len(rel32)
    clears = rel32 >= ITEM_I_REFUTE_REL
    runs = []
    i = 0
    while i < n_bins:
        if clears[i]:
            j = i
            while j < n_bins and clears[j]:
                j += 1
            if (j - i) >= ITEM_I_MIN_RUN:
                runs.append((i, j))
            i = j
        else:
            i += 1

    smooth_run_found = False
    run_details = []
    for (i0, j0) in runs:
        bin_idx = int(np.argmax(rel32[i0:j0])) + i0
        seq = [pattern_by_margin_delta[m][bin_idx] for m in MARGINS]
        fit = linear_fit_1_over_margin(MARGINS, seq)
        run_details.append(dict(bin_range=(i0, j0), anchor_bin=bin_idx, sequence=seq, fit=fit))
        if fit["smooth"]:
            smooth_run_found = True

    if confirm_all_margins and not runs:
        verdict = "CONFIRM"
    elif runs and smooth_run_found:
        verdict = "REFUTE"
    else:
        verdict = "AMBIGUOUS"
    return dict(verdict=verdict, rel32=rel32.tolist(), runs=runs, run_details=run_details,
                confirm_all_margins=confirm_all_margins)


# ================================================================ predictions/result text (R23: single source of truth)
DISCLAIMER = ("Raw physical angular-scattering-pattern and absorbed-power/ "
              "extinction ratios only -- no Weber-contrast or C_thr(L) perceptual "
              "scoring is performed this cycle; not a claim about human "
              "visibility. angular_scattered_pattern() is a square-path "
              "near-to-mid-field angular sample, not a true circular "
              "far-field pattern (function's own docstring). The absolute-"
              "floor six-margin family is a new convention this cycle, "
              "interpolating/extending the already-validated box_a/box_b "
              "pair, not independently re-derived from a resolution or "
              "aliasing bound.")


def build_predictions_text():
    return f"""PREDICTIONS (pre-registered, exp-108, Panel Iteration 85)

{DISCLAIMER}

**Tier 0, item 1** (deterministic): reclassify_106.py's reported string
contains "THREE-WAY-AMBIGUOUS"; all other fields bit-identical to
exp-106's own committed results.json.

**Gate P0** (ground-truth reproduction, zero cost): geom_fixedabs(156/312)
reproduces exp-106's own committed geom_156_fixedabs/geom_312_fixedabs
exactly. Falsified by ANY mismatch -> halt.

**Reproduction precondition** (item i, must PASS before any angular claim
is trusted): fresh PEC-cored capture's sections.widths() at box_a
reproduces exp-106's own committed ledger_r{{r}}['fixedabs'] to <1e-6
relative.

**Item i** (angular_scattered_pattern, unified multi-margin fix): CONFIRM
if every floor-cleared bin <=5% relative deviation at ALL 6 margins;
REFUTE if a >=3-bin contiguous run clears a 15% bar at margin=32 AND its
6-point across-margin sequence is smooth (monotonic or R^2>=0.90 fit to
A+B/margin); else AMBIGUOUS.

**Item ii** (absolute floor, six-margin, detrended): fit Delta(margin) =
A + B/margin; CONFIRM if residual_std <= 0.5*|Delta_boxA|; REFUTE if
residual_std >= |Delta_boxA|; else AMBIGUOUS. |Delta_boxA| = {DELTA_BOXA[156]:.3e}
(r=156) / {DELTA_BOXA[312]:.3e} (r=312), reused from exp-107.

**Item iii** (numerator floor-gate, PEC-cored PRIMARY article):
frac_unresolved within +/-0.05 of exp-107's own hollow-article reading
(0.18275 at r=156, 0.2675 at r=312).

**Item iv** (chunked-vs-continuous suite-stage identity): positive control
max|diff|=0.0; negative control (corrupted checkpoint) deviates >1%
relative.

**closure** (ledger sanity, both articles, both r): <=0.1%, falsified if
>1%.

Cost gate (reused verbatim, exp-106's own r312_primary_committed rule):
pilot r=156 (3 calls) first; commit r=312 (3 calls) only if pilot empty-
scene wall time <90 min AND projected 3-call r=312 total <180 min.
"""


def build_result_text(n_fdtd_calls, total_wall_s, gate_p0_pass, repro_pass,
                       item_i, item_ii, item_iii, item_iv, closure_rows,
                       wall_time_source=None):
    wall_time_note = f"\n({wall_time_source})" if wall_time_source else ""
    return f"""RESULT (exp-108, Panel Iteration 85)

{DISCLAIMER}

{n_fdtd_calls} real FDTD calls, {total_wall_s:.1f}s ({total_wall_s/60.0:.2f} min)
total wall time, zero `lab/` diff except the new stage26 addition.{wall_time_note}

**Gate P0: {'PASS' if gate_p0_pass else 'FAIL'}.**
**Reproduction precondition: {'PASS' if repro_pass else 'FAIL'}.**
**Item i:** {item_i}
**Item ii:** {item_ii}
**Item iii:** {item_iii}
**Item iv:** {item_iv}
**closure:** {closure_rows}
"""


if __name__ == "__main__":
    if "--predictions-only" in sys.argv:
        predictions_text = build_predictions_text()
        assert DISCLAIMER in predictions_text, "R23: disclaimer missing from Predictions block"
        print(predictions_text)
    else:
        print("This module holds shared geometry/constants and analysis functions only.")
        print("Capture via chunk_runner.py; analysis via analyze.py.")
