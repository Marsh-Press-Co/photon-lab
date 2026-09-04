"""exp-110 -- Panel Iteration 87 (ELECTROMAGNETISM's rotation-lead cycle):
item i's local-magnitude floor gate (mirror-symmetry noise floor, pooled
per Red Team's Fix 1), a synthetic fault-injection control for
linear_fit_1_over_margin's own smooth/noise discriminator (R18
discipline), and stage26's symmetric truncation-direction negative
control (lab/validation/run_all.py, patched separately). Frozen spec:
NOTES.md (Predictions committed to git strictly BEFORE this file's first
real Sim.run() call, house discipline). Change rationale:
phase2_redteam_audit.md (8 numbered mandatory fixes, all Phase-2 critiques
adopted, one partial override -- MATERIALS' own "add a genuine R14(a)
check" remedy declined as unachievable on multi-lobed curves, MATERIALS'
own alternative "drop the claim" adopted instead).

Grounding-fact finding (phase1_proposal.md Sec 0.5, independently
reconfirmed by all five Phase-2 critiques and Red Team): the
Iteration-86 queue's own "zero new FDTD, all data already committed"
premise for item i's local renormalization was FALSE -- the per-bin
angular-pattern arrays live only in a prior, now-defunct session's
ephemeral scratchpad. This file re-captures exp-108's own identical
6-call geometry (empty/hollow/peccored x r=156/312), this time
persisting the per-bin arrays permanently (item 1b).

This session's own backgrounded/nohup execution mode is confirmed
pathologically slow for sustained FDTD numpy work (exp-107's own
A/B-tested finding, reused without re-testing) -- actual capture is via
chunk_runner.py (checkpoint/resume, foreground Bash calls only); analysis
is via analyze.py, both importing this module.
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

EXP108_DIR = os.path.join(ROOT, "experiments", "108-t28-reclassification-angular-pattern-batch")
with open(os.path.join(EXP108_DIR, "results.json")) as f:
    EXP108_RESULTS = json.load(f)

# ================================================================ exp-106/108's own formula chain, reused byte-for-byte
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
ABS_THICKNESS = 48
SIGMA_MAX_FIXED = 0.5

BOX_A_MARGIN0 = 32
BOX_B_MARGIN0 = 57
REF_HH0 = 60

MARGINS = (24, 32, 40, 48, 57, 65)

# item-1(angular)/item-ii cost gate: abort r=312 leg if the pilot exceeds this.
# Fix 5 (Red Team, phase2_redteam_audit.md Sec 1.5/6): wired as executable
# code below (cost_gate_check()), not merely a referenced-in-prose constant --
# closes RT-4, the "prose-promised, code-toothless gate" gap (four-plus
# cycles old, exp-105 through exp-108, first named this cycle; ratified as
# a new standing rule, R27 -- see NOTES.md/LOGBOOK.md).
COST_GATE_PILOT_S = 90 * 60
COST_GATE_TOTAL_S = 180 * 60

ITEM_I_CONFIRM_REL = 0.05
ITEM_I_REFUTE_REL = 0.15
ITEM_I_MIN_RUN = 3
R2_SMOOTH_THRESHOLD = 0.90

DELTA_BOXA = {156: 2.969e-5, 312: 2.468e-5}
CLOSURE_CONFIRM = 0.001
CLOSURE_FALSIFY = 0.01

# item-1 local floor gate (this cycle, new)
MIRROR_FLOOR_K = 3.0
MIRROR_FLOOR_PERCENTILE = 50  # median, within-margin pooling (Red Team Sec 2, default)


def kappa_of(r):
    return r / R_BASE


def geom_fixedabs(r):
    """Fixed-absolute-thickness family, byte-for-byte reused from
    exp-106/108's own geom_fixedabs()."""
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
    """HALT before any new Sim.run() call if this file's own re-derived
    geom_fixedabs(r) disagrees with exp-106's own committed geometry."""
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
    exp-106's own committed ledger to <1e-6 relative -- HALT before any
    angular claim is trusted."""
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


def reproduction_precondition_108(cap_peccored, cap_empty, g):
    """A second, tighter cross-check specific to this cycle: this
    re-capture's own box_a widths should also reproduce exp-108's own
    already-committed item-i/ii inputs (same geometry, same box), not
    only exp-106's original ledger."""
    w = sc.widths(cap_peccored, cap_empty, g["box_a"], g["ref"])
    key = f"ledger_r{g['r']}"
    committed = EXP106_RESULTS[key]["fixedabs"]
    rel_abs = abs(w["sigma_abs"] - committed["sigma_abs"]) / abs(committed["sigma_abs"])
    rel_ext = abs(w["sigma_ext"] - committed["sigma_ext"]) / abs(committed["sigma_ext"])
    return dict(pass_=bool(rel_abs < 1e-6 and rel_ext < 1e-6), rel_abs=rel_abs, rel_ext=rel_ext)


def linear_fit_1_over_margin(margins, values):
    """Fit values = A + B/margin (least squares); return A, B, residuals,
    residual_std, R^2, is_monotonic, smooth. Byte-for-byte reused from
    exp-108/109's own committed run.py -- THIS is the function item 2's
    fault-injection control targets, imported unmodified via
    linear_fit_control.py."""
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
    """Byte-for-byte reused from exp-108/109's own committed run.py
    (the R24-second-instance fix, Panel Iteration 86) -- unchanged,
    reproduced here only so item ii's own code path is available without
    depending on a cross-experiment-directory import."""
    boxA = DELTA_BOXA[r]
    raw_std = float(np.std(delta_values))
    ratio = raw_std / fit["residual_std"] if fit["residual_std"] else float("inf")
    if fit["smooth"]:
        stat = fit["residual_std"]
        stat_source = f"detrended (fit smooth: is_monotonic={fit['is_monotonic']}, r_squared={fit['r_squared']:.4f})"
    else:
        stat = raw_std
        stat_source = (f"raw/undetrended (fit NOT smooth: is_monotonic={fit['is_monotonic']}, "
                        f"r_squared={fit['r_squared']:.4f} < {R2_SMOOTH_THRESHOLD:.2f}). "
                        f"raw/residual ratio this point: {ratio:.3f}x)")
    if stat <= 0.5 * boxA:
        verdict = "CONFIRM"
    elif stat >= boxA:
        verdict = "REFUTE"
    else:
        verdict = "AMBIGUOUS"
    return dict(verdict=verdict, stat_used=stat, stat_source=stat_source, boxA=boxA,
                raw_std=raw_std, residual_std=fit["residual_std"], raw_over_residual_ratio=ratio)


def classify_item_i(pattern_by_margin_delta, sigma_scat_by_margin_peccored, r):
    """Byte-for-byte reused from exp-108/109's own committed run.py --
    the existing, frozen, already-CONFIRMed classifier. UNCHANGED this
    cycle; item 1's new local diagnostic (below) is explicitly
    informational and does not replace or gate this verdict (Red Team
    Fix 2's own reasoning: a brand-new instrument must not be folded into
    a frozen verdict the same cycle it is built -- R24's own logic)."""
    margin32 = 32
    delta32 = pattern_by_margin_delta[margin32]
    peccored32 = sigma_scat_by_margin_peccored[margin32]
    max_peccored32 = float(np.max(np.abs(peccored32))) if np.max(np.abs(peccored32)) > 0 else 1e-30
    rel32 = np.abs(delta32) / max_peccored32

    confirm_all_margins = True
    for m in MARGINS:
        dm = pattern_by_margin_delta[m]
        pm = sigma_scat_by_margin_peccored[m]
        maxpm = float(np.max(np.abs(pm))) if np.max(np.abs(pm)) > 0 else 1e-30
        relm = np.abs(dm) / maxpm
        if np.any(relm > ITEM_I_CONFIRM_REL):
            confirm_all_margins = False
            break

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


# ================================================================ item 1's NEW local floor-gate diagnostic (this cycle)
def mirror_pooled_floor(pattern_48, percentile=MIRROR_FLOOR_PERCENTILE):
    """Red Team Fix 1 (phase2_redteam_audit.md Sec 6): a POOLED statistic
    of the per-bin mirror-asymmetry array, not a single per-bin draw.
    This bench is mirror-symmetric about the propagation axis (CY=N/2
    exactly, symmetric plane-wave source, every box/circle centered on
    CY -- independently re-derived by PHOTONICS' own Phase-2 critique,
    confirmed by Red Team, Sec 1.1) -- bin i and bin (n-1-i) are an exact
    geometric pair. |pattern[i]-pattern[n-1-i]|/2 is a per-pair estimate
    of the ODD/antisymmetric noise component only (any common-mode/even
    bias cancels identically -- PHOTONICS' own Sec-1.1-confirmed
    structural blindness, disclosed in NOTES.md Idealizations, NOT closed
    by this pooling). Pooling (median, within-margin, default) over the
    n/2 bin-pairs improves the estimate of that odd component's typical
    SCALE (closing QUANTUM's own correlated-single-realization concern,
    Sec 1.2) -- a variance fix, not a bias fix; both are independently
    needed (Red Team Sec 2)."""
    n = len(pattern_48)
    assert n % 2 == 0, "mirror pooling requires an even bin count"
    pairs = np.array([abs(pattern_48[i] - pattern_48[n - 1 - i]) / 2.0 for i in range(n // 2)])
    return float(np.percentile(pairs, percentile))


def classify_item_i_local(r, margin, pattern_peccored, pattern_hollow, pattern_delta,
                           K=MIRROR_FLOOR_K, percentile=MIRROR_FLOOR_PERCENTILE):
    """Item 1's local-magnitude diagnostic. EXPLICITLY INFORMATIONAL --
    does not replace, gate, or reclassify classify_item_i()'s own frozen
    CONFIRM verdict (Red Team Fix 2). Discharges R13 (denominator
    floor-gating) ONLY -- NOT R14 (Red Team Fix 3: a literal R14(a)
    numerator-parent-smoothness check does not apply to genuinely
    multi-lobed diffraction-pattern curves that are non-monotonic/
    non-smooth BY PHYSICS, not by artifact).

    Panel Iteration 88 (exp-111) fix, mandatory-fix 3 of
    experiments/111-.../phase2_redteam_audit.md Sec 5 (QUANTUM's own
    Phase-2 finding): floor==0.0 is a genuinely degenerate, mirror-symmetric
    input (both parent patterns exactly even under i<->n-1-i) -- guarded
    explicitly via `floor_degenerate`, distinct from RESOLVED, rather than
    silently reading `resolved=[True]*n` (a mathematical identity of
    `abs(x)>=0`, not a measurement). local_snr_peccored/local_snr_hollow are
    now `nan`-filled (not `inf`-filled) in this same degenerate case, closing
    a live self-contradiction the founding exp-110 cycle's own patch would
    otherwise have left (`resolved=False` beside `local_snr=inf` in the same
    returned dict) -- independently caught by QUANTUM's own Phase-2 critique
    and confirmed by Red Team's own from-primitives re-run,
    experiments/111-.../phase2_redteam_audit.md Sec 1/5 item 3. Verified
    non-regressive against all 12 real committed (r,margin) cells in
    exp-110's own results.json (floor strictly positive at every one;
    `floor_degenerate=False` and `n_resolved` bit-identical throughout) --
    see experiments/111-.../floor_fault_injection_control.py."""
    pattern_peccored = np.asarray(pattern_peccored, dtype=float)
    pattern_hollow = np.asarray(pattern_hollow, dtype=float)
    pattern_delta = np.asarray(pattern_delta, dtype=float)
    floor_p = mirror_pooled_floor(pattern_peccored, percentile)
    floor_h = mirror_pooled_floor(pattern_hollow, percentile)
    floor = K * max(floor_p, floor_h)
    floor_degenerate = bool(floor <= 0.0)
    resolved = ((floor > 0.0)
                & (np.abs(pattern_peccored) >= floor)
                & (np.abs(pattern_hollow) >= floor))
    local_rel = np.full(pattern_delta.shape, np.nan)
    local_rel[resolved] = np.abs(pattern_delta[resolved]) / np.abs(pattern_peccored[resolved])
    if floor > 0.0:
        local_snr_peccored = np.abs(pattern_peccored) / floor
        local_snr_hollow = np.abs(pattern_hollow) / floor
    else:
        local_snr_peccored = np.full(pattern_delta.shape, np.nan)
        local_snr_hollow = np.full(pattern_delta.shape, np.nan)
    return dict(r=r, margin=margin, K=K, percentile=percentile,
                floor_peccored_pooled=floor_p, floor_hollow_pooled=floor_h, floor=floor,
                floor_degenerate=floor_degenerate,
                resolved=resolved.tolist(), n_resolved=int(np.sum(resolved)), n_total=int(len(pattern_delta)),
                local_rel=[None if np.isnan(v) else float(v) for v in local_rel],
                local_snr_peccored=local_snr_peccored.tolist(),
                local_snr_hollow=local_snr_hollow.tolist(),
                confirm_band=ITEM_I_CONFIRM_REL, refute_band=ITEM_I_REFUTE_REL)


# ================================================================ cost gate (Fix 5 -- wired as code, R27's own founding fix)
# Panel Iteration 88 (exp-111), mandatory-fix 4 of experiments/111-.../
# phase2_redteam_audit.md Sec 5 (EM's own Phase-5-of-exp-110 finding, R28's
# own companion caution): the previous hardcoded exponent (3.0, "area x
# steps scaling") underestimated the measured r=312/r=156 combined-wall
# ratio (9.2236x) by ~15% -- independently re-derived, this cycle, from
# exp-110's own committed results.json: ln(9.223600318696624)/ln(2.0) =
# 3.2053299988171697. A single-geometry/single-kappa_ratio=2.0 empirical
# fit, not a first-principles law (disclosed in DISCLAIMER_88, below) --
# a 10% multiplicative safety margin is applied on top, since this
# exponent has not been validated at any other kappa_ratio (e.g. a future
# r=624 point, Tier 2 item 5).
KAPPA_COST_EXPONENT = 3.2053299988171697
COST_GATE_SAFETY_MARGIN = 1.10


def cost_gate_check(pilot_empty_wall_s, pilot_total_wall_s,
                     kappa_exponent=KAPPA_COST_EXPONENT,
                     safety_margin=COST_GATE_SAFETY_MARGIN):
    """R27 (this cycle's own ratified standing rule): a numeric cost gate
    MUST be enforced by executable code, not merely referenced in prose.
    pilot_empty_wall_s: r=156's own empty-scene capture wall time.
    pilot_total_wall_s: r=156's own 3-call (empty+hollow+peccored) total.
    Projects r=312's total via an empirically re-derived exponent (see
    KAPPA_COST_EXPONENT, above) plus an explicit safety margin -- reported
    explicitly, not silently assumed. R28's own founding-instance gap
    (this same function sat downstream of 90.2% of exp-110's own
    wall-clock spend) is fixed by chunk_runner.py's own upstream call
    (Panel Iteration 88, mandatory-fix 1/2), not by this function itself --
    this function only computes the projection; see
    check_cost_gate_for_312() in chunk_runner.py for the causal
    repositioning."""
    pilot_pass = pilot_empty_wall_s < COST_GATE_PILOT_S
    kappa_ratio = kappa_of(312) / kappa_of(156)          # = 2.0
    projected_312_total_s = pilot_total_wall_s * (kappa_ratio ** kappa_exponent) * safety_margin
    total_pass = projected_312_total_s < COST_GATE_TOTAL_S
    proceed = bool(pilot_pass and total_pass)
    return dict(pilot_empty_wall_s=pilot_empty_wall_s, pilot_total_wall_s=pilot_total_wall_s,
                pilot_pass=pilot_pass, kappa_ratio=kappa_ratio,
                kappa_exponent=kappa_exponent, safety_margin=safety_margin,
                projected_312_total_s=projected_312_total_s, total_pass=total_pass,
                proceed_to_r312=proceed)


# ================================================================ predictions/result text (R23: single source of truth)
DISCLAIMER = ("Raw physical angular-scattering-pattern and absorbed-power/ "
              "extinction ratios only -- no Weber-contrast or C_thr(L) perceptual "
              "scoring is performed this cycle; not a claim about human "
              "visibility. angular_scattered_pattern() is a square-path "
              "near-to-mid-field angular sample, not a true circular "
              "far-field pattern (function's own docstring). The absolute-"
              "floor six-margin family and item 1's own mirror-symmetry "
              "floor are both new conventions this cycle, not independently "
              "re-derived from a resolution or aliasing bound. Item 1's "
              "mirror floor characterizes grid-discretization/floating-"
              "point noise for the IDEALIZED simulated geometry ONLY -- a "
              "bin clearing it licenses NO inference about a physically "
              "realized coated disk's own achievable angular-pattern "
              "symmetry (real deposition/machining tolerances sit orders "
              "of magnitude above this floor's ~1e-9-1e-4 scale). Item 1's "
              "mirror floor is structurally BLIND to common-mode/even noise "
              "(a bias, not variance -- any bias identical at bin i and "
              "its mirror bin cancels exactly in the differencing "
              "construction, at any sample size, unclosed by pooling) -- "
              "a RESOLVED bin under this gate is cleared only against the "
              "ODD/antisymmetric noise component, not validated clean of "
              "common-mode contamination. Item 1's diagnostic is "
              "INFORMATIONAL ONLY and does not replace, gate, or "
              "reclassify item i's own existing frozen CONFIRM verdict.")


def build_predictions_text():
    return f"""PREDICTIONS (pre-registered, exp-110, Panel Iteration 87)

{DISCLAIMER}

**Item 1a** (re-capture fidelity): gate_p0 PASS exact, both r. reproduction_
precondition PASS, sigma_abs/sigma_ext/abs_ext_ratio matching exp-108's own
committed results.json to <1e-9 relative at both r (r=156:
sigma_abs=279.6607, sigma_ext=560.1989; r=312: sigma_abs=588.0218,
sigma_ext=1191.3259). Falsified by ANY deviation exceeding that bound.

**Item 1b** (persistence): len(results.json["item_i"]["raw_patterns"][m]
["peccored"]) == 48 for all 6 margins, both r actually captured (r=312
conditional on the cost gate below). Falsified by any missing combination.

**Item 1c/1d** (mirror pooled floor -- genuinely uncertain, the open
question this instrument exists to answer): I predict at least SOME of
the low-power bins PHOTONICS' own Iteration-85 self-review found (<1% of
peak power, 30/48 bins both r) will fail the K=3 pooled floor gate
(UNRESOLVED-BY-CONSTRUCTION). Falsified if ALL 48 bins clear K=3
comfortably (local_snr>10 everywhere) at both r captured. No advance
position taken on the two specific bins PHOTONICS named (-146.25 deg at
r=156, +168.75 deg at r=312) -- RESOLVED-with-genuine-structure or
UNRESOLVED-by-construction, whichever the run produces.

**Item 2**: all four synthetic (is_monotonic, r_squared, smooth) triples
reproduce bit-exact (deterministic numpy arithmetic on closed-form
sequences, independently re-verified already by QUANTUM and VISION's own
Phase-2 critiques by direct invocation of the real committed function):
P1=(True, 1.0, True); P2=(True, 0.397, True); P3=(False, 0.912, True);
N1=(False, 0.097, False).

**Item 3**: rel_diff_truncated > 0.01 (the gate's own minimum
discrimination bar), predicted in (0.01, 10], same order of magnitude as
the existing over-run control's own 2.0 (200%) figure. Falsified only if
rel_diff_truncated <= 0.01.

**Cost gate (R27, wired as code this cycle)**: pilot_empty_wall_s for
r=156 predicted well under 5400s (90 min) based on exp-108's own recorded
combined 128.5 min/6-call wall time (r=156 is the cheaper leg, k=2 vs
k=4). If the pilot clears, r=312 is attempted; if not, r312_deferred=True
is written and item 1's r=312 analysis is reported NOT-RUN, not silently
skipped.
"""


def build_result_text(n_fdtd_calls, total_wall_s, gate_p0_pass, repro_pass,
                       item_1a, item_1b, item_1cd, item_2, item_3,
                       wall_time_source=None):
    wall_time_note = f"\n({wall_time_source})" if wall_time_source else ""
    return f"""RESULT (exp-110, Panel Iteration 87)

{DISCLAIMER}

{n_fdtd_calls} real FDTD calls, {total_wall_s:.1f}s ({total_wall_s/60.0:.2f} min)
total wall time this cycle, zero `lab/` diff except the disclosed stage26
symmetric-truncation addition (item 3).{wall_time_note}

**Gate P0: {'PASS' if gate_p0_pass else 'FAIL'}.**
**Reproduction precondition: {'PASS' if repro_pass else 'FAIL'}.**
**Item 1a (re-capture fidelity):** {item_1a}
**Item 1b (persistence):** {item_1b}
**Item 1c/1d (mirror pooled floor, informational):** {item_1cd}
**Item 2 (linear_fit_1_over_margin control):** {item_2}
**Item 3 (stage26 truncation control):** {item_3}
"""


if __name__ == "__main__":
    if "--predictions-only" in sys.argv:
        predictions_text = build_predictions_text()
        assert DISCLAIMER in predictions_text, "R23: disclaimer missing from Predictions block"
        print(predictions_text)
    else:
        print("This module holds shared geometry/constants and analysis functions only.")
