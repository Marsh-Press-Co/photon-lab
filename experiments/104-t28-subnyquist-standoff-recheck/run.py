"""exp-104 -- The Sub-Nyquist Standoff Recheck (Reconciled Iteration-81 queue,
Tier 1). Panel Iteration 81. Lead seat (rotation): ELECTROMAGNETISM. Frozen
spec: NOTES.md (Predictions committed to git strictly BEFORE this file's
first real run, house discipline).

PANEL RECORD (compressed -- full record in NOTES.md "Panel record" section):
exp-103's own <=10-cell (window-spanning) standoff pitch was Phase-5-flagged
(PHOTONICS + QUANTUM, independently, two different routes) as degenerate
aliasing against the lambda/2=10-cell coherent-intensity fringe period it
was meant to guard against -- samples land at exactly one full period, not
a resolved one; true Nyquist needs <5-cell spacing. Five blind Phase-2
critiques (PHOTONICS, MATERIALS, THERMODYNAMICS, QUANTUM OPTICS, VISION
SCIENCE) all returned support-with-changes with distinct concrete flip
conditions; Red Team's audit independently re-verified every sharpest claim
from primitives and ADOPTED ALL FIVE flip conditions (none overridden),
raised 2 additional attacks of its own (a P3 grid-quantization artifact --
Attack 1, raw reversal-position differencing is mathematically confined to
EVEN multiples of the fixed 2-cell pitch and can never surface an odd true
period, fixed here by per-quintile FFT + parabolic sub-bin interpolation
instead; and P6 lacking a numeric threshold -- Attack 2, fixed here by the
explicit ripple_fraction_i <=0.20 / >0.50 narrows/overturns bands), and
ruled Checkpoint criterion 4 does NOT fire this cycle (the disclaimer-
erosion issue was caught blind, before freeze -- the discharge-test
precedent holds) while ratifying standing rule R23 (a disclaimer required
in multiple document sections must be enforced by a code-level assert on a
single source-of-truth string, not manual prose-carrying-forward -- this
pattern has recurred 8 times; see the DISCLAIMER/PREDICTIONS_TEXT/
RESULT_TEXT machinery and the two `assert DISCLAIMER in ...` calls below,
which is R23 actually IMPLEMENTED this cycle, not merely described).

Instrument-repair/recheck cycle, diagnostic only -- T1: N/A, zero `lab/`
diff, no mechanism proposed or varied. Geometry/`_run()`/`block_mean_
intensity`/`kappa_region_at`/`window_stats` machinery reused verbatim from
`experiments/103-.../run.py` wherever unchanged (byte-identical primary-pair
parameters: N=560, ABSORB=40, COURANT_FRAC=0.32, STEPS=3200, SRC_X=64,
CX=252, CY=280, R_CORE=30, R_COAT=78, R_CLK=90, CPL_600=20, EDGE=TAPER=40 --
verified directly against that file's own committed constant, NOT the
R4_TAPER=80 the Phase-1 proposal of THAT cycle originally (and incorrectly)
specified). `point_intensity`/the `delta_phi=angle(mean_a/mean_e)` formula
are ported from `experiments/102-.../run.py:406-407` (`point_intensity`)
and `:417` (the `delta_phi` line inside `kappa_at`), verified directly by
reading that file (see NOTES.md Setup for the exact citation).

MATERIALS' mandatory Idealizations fix (verbatim substance, this cycle's
own P2 ripple, adopted per its Phase-2 flip condition):
""" + __import__("textwrap").dedent("""\
    Any P2 ripple found in residual_point(x) is necessarily numerical/
    aliasing in origin -- a consequence of grid-sampling this idealized,
    continuously-graded article, which has no discrete layer structure --
    and is NOT evidence bearing on the layer-tied ripple signature a
    realizable, discretely-graded coating would add per exp-103's own
    restored Realizability Bound. graded_black_shell remains UNOBTAINIUM-
    WITH-PARAMETERS, unchanged.
""") + """
THERMODYNAMICS' mandatory Idealizations fix (verbatim substance, adopted
per its Phase-2 flip condition):
""" + __import__("textwrap").dedent("""\
    Thermal sidecar: N/A this cycle -- no thermo_sidecar.py call, no new
    sigma_ext/ratio_abs_ext measured. H_REGION_POINT=0 point samples are
    peak local downstream |Ez|^2 in a coherent-superposition zone, NOT an
    incident-intensity-on-object quantity, and are not thermally
    interpretable without a separate aperture-integration step not
    attempted here.
""") + """
Settling-leg scope (Red Team Attack 4, mandatory fix): this cycle runs NO
fresh STEPS_2X leg. "Settling already established clean" rests on exp-103's
own check at x in [352,356] only (a 4-cell span, 5 points) -- NOT
independently verified across the full 104-cell dense span out to x=456.
Skipping a fresh settling leg this cycle relies on the general physical
argument (settling error decreases monotonically with standoff, EM's own
prior finding, exp-103 Prediction 4) rather than direct measurement at the
farther points. This is stated as an explicit idealization, not an implied
full-span verification.

QUANTUM's citation-overreach correction (Red Team Attack 5, mandatory
fix): the H_REGION_WIDE=5 (11-cell) box-width sinc-null hazard used in the
P4 suppression-ratio prediction below is NOT "structurally identical" to
exp-103's own original pitch-aliasing defect -- it is analogous in EFFECT
(both mask ripple amplitude) but mechanistically DISTINCT (a low-pass
filter null vs. a sampling-rate failure). Stated that way throughout.

Checkpoint-4 ruling: does NOT fire this cycle -- both live sub-issues
(disclaimer-erosion recurrence pattern; the Nyquist-overclaim prose that
motivated this whole cycle) were caught BLIND, before freeze, per this
program's own unbroken discharge-test precedent. R23 is ratified and
IMPLEMENTED (not merely described) below.
"""

import json
import math
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, ROOT)

from lab import Sim, materials                      # noqa: E402
from lab import sections as sc                       # noqa: E402


# ================================================================ geometry
# Byte-identical to exp-103's primary pair (experiments/103-.../run.py),
# verified directly against that file -- NOT R4_TAPER=80.
N = 560
ABSORB = 40
COURANT_FRAC = 0.32
STEPS = 3200
SRC_X = 64
CX, CY = 252, 280
R_CORE, R_COAT, R_CLK = 30, 78, 90
CPL_600 = 20
EDGE = TAPER = 40  # exp-103's own corrected value (TAPER=40, cpl=20-
                    # calibrated), NOT R4_TAPER=80 -- verified against
                    # experiments/103-t28-gateb-footprint-aperture-match/run.py:102

# Established BEHIND window, byte-for-byte (exp-103/exp-001):
BEHIND_X_LO = CX + R_CLK + 15   # 357
BEHIND_X_HI = CX + R_CLK + 115  # 457
BEHIND_Y_LO = CY - 20           # 260
BEHIND_Y_HI = CY + 20           # 300
assert (BEHIND_X_LO, BEHIND_X_HI, BEHIND_Y_LO, BEHIND_Y_HI) == (357, 457, 260, 300)

# exp-103's own 16-point ALL_X (NEAR_FIELD_X + WINDOW_SPAN_X), reproduced
# verbatim -- needed for Gate P1 (the reproducibility identity check).
NEAR_FIELD_X = [352, 353, 354, 355, 356]
WINDOW_SPAN_X = [357, 367, 377, 387, 397, 407, 417, 427, 437, 447, 456]
ALL_X = NEAR_FIELD_X + WINDOW_SPAN_X
assert len(ALL_X) == len(set(ALL_X)) == 16

# New this cycle: dense 2-cell-pitch standoff sampling (Tier 1 fix).
DENSE_X = list(range(352, 457, 2))
assert len(DENSE_X) == 53
DENSE_PITCH = 2.0  # cells

NEED_X = sorted(set(ALL_X) | set(DENSE_X))  # union: everything the FDTD
                                             # post-processing pass reads

H_REGION_WIDE = 5   # unchanged 11x11 box (exp-103's own H_REGION) -- the
                     # "filtered" channel, reused for continuity.
H_REGION_POINT = 0  # literal single Ez cell, zero averaging -- ported
                     # from exp-102's point_intensity (run.py:406-407).
FLOOR_FRAC = 0.10

DISCLAIMER = ("Raw physical intensity/phase ratios only -- no Weber-contrast or "
              "C_thr(L) perceptual scoring is performed this cycle; not a claim "
              "about human visibility.")


def _run(with_article, steps):
    """Verbatim exp-103 `_run()`."""
    sim = Sim(N, N, cells_per_lambda=CPL_600, courant_frac=COURANT_FRAC, absorb=ABSORB)
    if with_article:
        materials.pec_disk(sim, CX, CY, R_CORE)
        materials.graded_black_shell(sim, CX, CY, R_CORE, R_COAT)
    sim.add_line_source(SRC_X, angle_deg=0.0, profile="plane", edge=EDGE)
    sim.run(steps)
    return sc.full_capture(sim)


# ================================================================ point/region readout primitives
def block_mean_intensity(ez, x, y, h):
    """Verbatim exp-103 `block_mean_intensity`."""
    xs = slice(x - h, x + h + 1)
    ys = slice(y - h, y + h + 1)
    block = np.abs(ez[xs, ys]) ** 2
    return float(np.mean(block))


def block_mean_complex(ez, x, y, h):
    """Complex-mean-before-magnitude, the same box exp-102's `kappa_at`
    uses for `delta_phi` (`mean_a`/`mean_e` in that file's `block_mean_
    intensity`, run.py:399-403)."""
    xs = slice(x - h, x + h + 1)
    ys = slice(y - h, y + h + 1)
    return complex(np.mean(ez[xs, ys]))


def point_intensity(ez, x, y):
    """Verbatim exp-102 `point_intensity` (run.py:406-407)."""
    return float(np.abs(ez[x, y]) ** 2)


def kappa_region_wide(ez_empty, ez_article, x, y=CY, h=H_REGION_WIDE):
    i_e = block_mean_intensity(ez_empty, x, y, h)
    i_a = block_mean_intensity(ez_article, x, y, h)
    k = i_a / i_e if i_e != 0 else float("inf")
    return k, i_e, i_a


def kappa_region_point(ez_empty, ez_article, x, y=CY):
    """H_REGION_POINT=0 -- literal single Ez cell (exp-102's `point_
    intensity`), zero averaging."""
    i_e = point_intensity(ez_empty, x, y)
    i_a = point_intensity(ez_article, x, y)
    k = i_a / i_e if i_e != 0 else float("inf")
    return k, i_e, i_a


def wrap_phase(phi):
    """Wrap to (-pi, pi]."""
    wrapped = (phi + math.pi) % (2 * math.pi) - math.pi
    if wrapped <= -math.pi:
        wrapped += 2 * math.pi
    return wrapped


def delta_phi_wide(ez_empty, ez_article, x, y=CY, h=H_REGION_WIDE):
    """exp-102's exact formula (`angle(mean_a/mean_e)`), H_REGION_WIDE box."""
    mean_e = block_mean_complex(ez_empty, x, y, h)
    mean_a = block_mean_complex(ez_article, x, y, h)
    if mean_e == 0:
        return float("nan")
    return wrap_phase(float(np.angle(mean_a / mean_e)))


def delta_phi_point(ez_empty, ez_article, x, y=CY):
    """exp-102's exact formula, literal single-cell values."""
    ez_e = ez_empty[x, y]
    ez_a = ez_article[x, y]
    if ez_e == 0:
        return float("nan")
    return wrap_phase(float(np.angle(ez_a / ez_e)))


def wide_pointwise_spread(ez_empty, ez_article, x, y=CY, h=H_REGION_WIDE):
    """Mirrors `kappa_window`'s own pointwise-spread convention exactly
    (experiments/103-.../run.py:229-237: per-cell |ez_a|^2/|ez_e|^2 ratio,
    reported mean/std/min/max), applied to each of the 16 original
    `kappa_region` x-points' own H_REGION_WIDE box instead of the whole
    BEHIND window."""
    xs = slice(x - h, x + h + 1)
    ys = slice(y - h, y + h + 1)
    ratio = np.abs(ez_article[xs, ys]) ** 2 / np.abs(ez_empty[xs, ys]) ** 2
    return dict(mean=float(np.mean(ratio)), std=float(np.std(ratio)),
                min=float(np.min(ratio)), max=float(np.max(ratio)))


def floor_gate(pool_values, label, floor_frac=FLOOR_FRAC):
    """RMS-across-pool floor gate, exp-102/exp-103's own established
    convention exactly."""
    arr = np.asarray(pool_values, dtype=float)
    rms = float(np.sqrt(np.mean(np.square(arr))))
    floor = floor_frac * rms
    passes = [bool(v >= floor) for v in arr]
    n_unresolved = sum(1 for p in passes if not p)
    print(f"  [floor gate: {label}] n={len(arr)} rms={rms:.6e} floor={floor:.6e} "
          f"n_unresolved={n_unresolved}")
    return dict(rms=rms, floor=floor, passes=passes, n_unresolved=n_unresolved)


# ================================================================ per-quintile period estimation (Red Team Attack 1 fix)
def estimate_period(x_vals, y_vals, dx=DENSE_PITCH):
    """FFT of the quintile's residual_point values, zero-padded to >=4x the
    point count, dominant non-DC bin found, quadratic/parabolic
    interpolation across the 3 straddling bins for a sub-bin-accurate
    spatial frequency -> a continuous-valued period estimate in cells (NOT
    constrained to even integers -- the whole point of this fix, per Red
    Team's Attack 1: raw reversal-position differencing on this fixed
    2-cell-pitch grid is mathematically confined to even multiples of 2
    cells and can never surface an odd true period).

    Peak criterion: peak non-DC bin power > 3x the median of all non-DC bin
    powers; otherwise period is indeterminate (None).

    Returns (period_cells_or_None, diagnostics_dict).
    """
    n = len(y_vals)
    y = np.asarray(y_vals, dtype=float)
    if n < 4:
        return None, dict(reason="too few points for a meaningful FFT peak", n=n)
    y = y - np.mean(y)
    nfft = 1
    while nfft < 4 * n:
        nfft *= 2
    yf = np.fft.rfft(y, n=nfft)
    power = np.abs(yf) ** 2
    if len(power) < 3:
        return None, dict(reason="fft too short", n=n, nfft=nfft)
    nonzero_power = power[1:]  # exclude DC (index 0)
    peak_rel_idx = int(np.argmax(nonzero_power))
    peak_idx = peak_rel_idx + 1
    peak_power = float(power[peak_idx])
    median_power = float(np.median(nonzero_power))
    diag = dict(n=n, nfft=nfft, peak_idx=peak_idx, peak_power=peak_power,
                median_power=median_power)
    if median_power <= 0 or peak_power <= 3.0 * median_power:
        diag["reason"] = "peak not > 3x median non-DC bin power (noise floor)"
        return None, diag
    # parabolic (quadratic) interpolation across the 3 bins straddling the peak
    if 1 <= peak_idx <= len(power) - 2:
        a, b, c = power[peak_idx - 1], power[peak_idx], power[peak_idx + 1]
        denom = (a - 2 * b + c)
        delta = 0.5 * (a - c) / denom if denom != 0 else 0.0
        delta = max(-1.0, min(1.0, float(delta)))
    else:
        delta = 0.0
    interp_bin = peak_idx + delta
    freq_per_cell = interp_bin / (nfft * dx)
    diag["interp_bin"] = float(interp_bin)
    diag["freq_per_cell"] = float(freq_per_cell)
    if freq_per_cell <= 0:
        diag["reason"] = "nonpositive interpolated frequency"
        return None, diag
    period = 1.0 / freq_per_cell
    diag["reason"] = "ok"
    return float(period), diag


def near_null_exclusion(p_i, box_wide=11.0, tol=0.10):
    """Pre-registered exclusion: p_i within `tol` (10%) of any integer
    multiple of `box_wide` (11 cells, the H_REGION_WIDE box width)."""
    k = 1
    best = float("inf")
    while k * box_wide < p_i + box_wide * (tol + 1):  # a couple of multiples past p_i is enough
        best = min(best, abs(p_i - box_wide * k))
        k += 1
        if k > 50:
            break
    return (best / box_wide) < tol, best / box_wide


def predicted_ratio(p_i, box_wide=11.0, box_point=1.0):
    """predicted_ratio_i = sinc(box_wide/p_i) / sinc(box_point/p_i), SIGNED
    (no abs()), np.sinc's normalized convention (sin(pi x)/(pi x))."""
    denom = np.sinc(box_point / p_i)
    if abs(denom) < 1e-12:
        return None
    return float(np.sinc(box_wide / p_i) / denom)


# ================================================================ predictions text (R23: single source of truth, generated BEFORE any FDTD call)
def build_predictions_text():
    return f"""PREDICTIONS (pre-registered, exp-104, Panel Iteration 81)

{DISCLAIMER}

**P1 (reproducibility gate, absolute identity check).** kappa_region_wide(x)
at the 16 original x-points (ALL_X, reproduced verbatim from exp-103's own
NEAR_FIELD_X+WINDOW_SPAN_X) reproduces experiments/103-.../results.json's
kappa_region_trend to <1e-9 relative. This is the run's precondition -- if
it fails, halt and report the defect rather than proceeding to trust P2-P6.

**P2 (ripple existence).** residual_point(x) = kappa_region_point(x) -
kappa_region_wide(x), at each of the 53 DENSE_X points (2-cell pitch,
x=352..456), shows >=2 sign changes (local reversals) with amplitude >5%
relative to the local kappa_region_wide value, across the full 53-point
span. Predicted CONFIRMED, citing exp-103's own disclosed kappa_window
pointwise spread (std/mean=0.849, 97x min/max) as evidence of nearby
comparable-scale structure -- that ripple is not present in the wide-box
trend (VISION's Phase-2 wording fix: "not present in", not "NOT visible
in").

**P3 (per-quintile period match, PHOTONICS' chirp-tolerant fix).** The 53
DENSE_X points are split into 5 contiguous quintiles (numpy.array_split,
~10-11 points each). In each quintile where a period is determined (FFT of
that quintile's residual_point, zero-padded to >=4x its point count,
dominant non-DC bin + parabolic sub-bin interpolation; peak power >3x the
median non-DC bin power, else indeterminate/None), the estimated period
falls in [7,13] cells. Predicted: at least 3 of 5 quintiles determine a
period in this band -- chirp across quintiles is expected and does NOT
falsify this prediction; a per-quintile band match does.

**P4 (signed suppression-ratio cross-check, QUANTUM's refined fix).** For
each quintile with both a determined period AND not near-null-excluded
(pre-registered exclusion below), predicted_ratio_i =
sinc(11/p_i)/sinc(1/p_i) (numpy's normalized sinc, SIGNED, no abs()) is
compared against the measured ratio = signed peak-to-peak(kappa_region_
wide's own residual from a smooth global fit, within quintile i) /
peak-to-peak(residual_point, within quintile i) -- sign assigned via the
sign of the (demeaned) correlation between the two residual signals within
the quintile (a defensible simplified proxy for "same phase vs. inverted
phase", analogous to what a negative sinc lobe means physically: the
11-cell box average phase-inverts a period this short relative to a
1-cell point sample). Pre-registered exclusion: if p_i is within 10% of
any integer multiple of 11 (min(|p_i-11k|)/11 < 0.10 for integer k>=1),
that quintile's P4 comparison is flagged "near-null, not scored" rather
than forced into pass/fail. Predicted CONFIRMED for at least 2 of
however-many non-excluded quintiles exist: sign(predicted_ratio_i) matches
the measured ratio's sign, AND |predicted_ratio_i| is within a factor of
2x of |measured ratio_i| (loose magnitude tolerance, justified by
quintile-scale amplitude estimation being crude with ~10 points).

**P5 (delta_phi co-variation, QUANTUM's fix, simplified proxy).**
delta_phi_wide(x) (exp-102's angle(mean_a/mean_e) formula, H_REGION_WIDE
box) is computed only at the 16 sparse original x-points (item 4's own
scope); delta_phi_point(x) is computed at all 53 DENSE_X points. A rigorous
same-frequency-bin phase decomposition against a densely-sampled delta_phi_
wide is not available (delta_phi_wide is sparse by construction), so the
adopted simplified proxy is: linearly interpolate delta_phi_wide (unwrapped
across the 16 sparse points) onto the DENSE_X grid, form a phase-ripple
residual = delta_phi_point(x) - interpolated delta_phi_wide(x) within each
quintile, and take sign(correlation(residual_point, phase-ripple residual))
as the proxy sign, compared against sign(predicted_ratio_i). This
substitutes a correlation-sign covariation check for a rigorous per-
frequency-component phase comparison -- stated exactly as computed, not
fabricated to a false precision. Predicted: directionally consistent (same
sign) in a majority of quintiles where both P3 and P4 are determined.

**P6 (scope, Red Team's numeric threshold, Attack 2 fix).**
ripple_fraction_i = peak-to-peak(residual_point in quintile i) /
mean(kappa_region_wide in quintile i). "Narrows" exp-103's own framing:
ripple_fraction_i <= 0.20 in ALL 5 quintiles. "Overturns": ripple_fraction_i
> 0.50 in ANY quintile. Between 0.20 and 0.50 in one or more quintiles
(none exceeding 0.50): reported as "MIXED/PARTIAL narrowing," not forced
into either bucket. Predicted: NARROWS (all quintiles <=0.20) -- because
kappa_window/exp-103's own Prediction-3 span-consistency result are wide-
window averages insensitive to ripple phase and are predicted to reproduce
unchanged (via kappa_region_wide at the retained 16 points, to P1's <1e-9
tolerance).

Mandatory Idealizations fixes (MATERIALS, THERMODYNAMICS, settling-leg
scope, QUANTUM citation correction) are stated in full in this file's
module docstring and in NOTES.md's Idealizations section verbatim.
"""


PREDICTIONS_TEXT = build_predictions_text()
assert DISCLAIMER in PREDICTIONS_TEXT, "R23: disclaimer missing from Predictions block"


# ================================================================ main
def main():
    print("=" * 78)
    print("exp-104 -- Sub-Nyquist standoff recheck")
    print("=" * 78)
    print("\n" + PREDICTIONS_TEXT)

    t_start = time.time()
    n_fdtd_calls = 0

    # ---------------------------------------------------------- margin gate
    h_max = H_REGION_WIDE
    for x in NEED_X:
        lo_x, hi_x = x - h_max, x + h_max
        assert lo_x > ABSORB and hi_x < N - ABSORB, f"x={x} block too close to absorb/boundary"
    lo_y, hi_y = CY - h_max, CY + h_max
    assert lo_y > ABSORB and hi_y < N - ABSORB
    print(f"\n[margin gate] {len(NEED_X)} standoff points (union of 16-pt + 53-pt DENSE_X), "
          f"all clear of absorb/boundary: PASS")

    # ============================================================ exactly 2 FDTD calls
    print(f"\n-- Primary pair: empty + article, theta=0, STEPS={STEPS}, edge={EDGE} --")
    t0 = time.time()
    cap_empty = _run(with_article=False, steps=STEPS)
    cap_article = _run(with_article=True, steps=STEPS)
    n_fdtd_calls += 2
    wall_primary = time.time() - t0
    print(f"Primary pair wall time: {wall_primary:.1f}s")
    assert n_fdtd_calls == 2, f"expected exactly 2 real FDTD calls, got {n_fdtd_calls}"

    ez_empty = sc.phasors(cap_empty)["ez"]
    ez_article = sc.phasors(cap_article)["ez"]

    # ============================================================ per-x readings at NEED_X (union)
    wide = {}
    point = {}
    for x in NEED_X:
        k_w, i_e_w, i_a_w = kappa_region_wide(ez_empty, ez_article, x)
        k_p, i_e_p, i_a_p = kappa_region_point(ez_empty, ez_article, x)
        wide[x] = dict(kappa_region_wide=k_w, i_region_empty=i_e_w, i_region_article=i_a_w)
        point[x] = dict(kappa_region_point=k_p, i_point_empty=i_e_p, i_point_article=i_a_p)

    # delta_phi_wide only at the 16 original x-points (item 4's own scope)
    dphi_wide = {x: delta_phi_wide(ez_empty, ez_article, x) for x in ALL_X}
    # delta_phi_point at all 53 DENSE_X points
    dphi_point = {x: delta_phi_point(ez_empty, ez_article, x) for x in DENSE_X}

    # wide-box pointwise spread at the 16 original x-points
    spread16 = {x: wide_pointwise_spread(ez_empty, ez_article, x) for x in ALL_X}

    # ============================================================ Gate P1 -- reproducibility identity check
    print("\n" + "=" * 78)
    print("GATE P1 -- reproducibility identity check vs exp-103's own kappa_region_trend")
    print("=" * 78)
    exp103_path = os.path.join(ROOT, "experiments",
                                "103-t28-gateb-footprint-aperture-match", "results.json")
    with open(exp103_path) as f:
        exp103_results = json.load(f)
    exp103_trend = exp103_results["kappa_region_trend"]

    p1_max_rel = 0.0
    p1_rows = {}
    for x in ALL_X:
        got = wide[x]["kappa_region_wide"]
        ref = float(exp103_trend[str(x)]["kappa_region"])
        rel = abs(got - ref) / abs(ref) if ref != 0 else float("inf")
        p1_max_rel = max(p1_max_rel, rel)
        p1_rows[x] = dict(got=got, ref=ref, rel=rel)
        print(f"  x={x:4d}  got={got:.12e}  ref={ref:.12e}  rel={rel:.3e}")
    p1_pass = p1_max_rel < 1e-9
    print(f"[Gate P1] max relative deviation = {p1_max_rel:.3e}  PASS(<1e-9)={p1_pass}")

    if not p1_pass:
        print("\n" + "!" * 78)
        print("GATE P1 FAILED -- halting per NOTES.md/Director instruction. NOT proceeding "
              "to trust P2-P6. This is reported as a genuine defect, not forced through.")
        print("!" * 78)
        result_fail = dict(
            experiment="exp-104", panel_iteration=81,
            gate_p1=dict(pass_=False, max_rel=p1_max_rel, rows={str(x): v for x, v in p1_rows.items()}),
            status="HALTED_GATE_P1_FAILED",
        )
        with open(os.path.join(HERE, "results.json"), "w") as f:
            json.dump(result_fail, f, indent=2, default=str)
        raise SystemExit(
            f"GATE P1 FAILED: max relative deviation {p1_max_rel:.3e} >= 1e-9. "
            f"See results.json (status=HALTED_GATE_P1_FAILED). Not proceeding to P2-P6."
        )

    # ============================================================ floor gates
    print("\n" + "=" * 78)
    print("FLOOR GATES (FLOOR_FRAC=0.10)")
    print("=" * 78)
    fg_wide = floor_gate([wide[x]["i_region_empty"] for x in ALL_X], "wide channel (16-pt pool, exp-103 convention)")
    fg_point = floor_gate([point[x]["i_point_empty"] for x in DENSE_X], "point channel (53-pt DENSE_X pool)")
    for x in ALL_X:
        wide[x]["floor_pass"] = fg_wide["passes"][ALL_X.index(x)]
    for i, x in enumerate(DENSE_X):
        point[x]["floor_pass"] = fg_point["passes"][i]

    # ============================================================ residual_point at DENSE_X
    residual_point = {x: point[x]["kappa_region_point"] - wide[x]["kappa_region_wide"] for x in DENSE_X}

    # ============================================================ P2 -- ripple existence
    print("\n" + "=" * 78)
    print("P2 -- ripple existence (residual_point sign changes, DENSE_X span)")
    print("=" * 78)
    dense_sorted = sorted(DENSE_X)
    res_seq = [residual_point[x] for x in dense_sorted]
    wide_seq = [wide[x]["kappa_region_wide"] for x in dense_sorted]
    p2_reversals = 0
    p2_events = []
    for i in range(1, len(dense_sorted)):
        if np.sign(res_seq[i]) != np.sign(res_seq[i - 1]) and res_seq[i] != 0 and res_seq[i - 1] != 0:
            local_scale = 0.5 * (abs(wide_seq[i]) + abs(wide_seq[i - 1]))
            amp = max(abs(res_seq[i]), abs(res_seq[i - 1]))
            rel_amp = amp / local_scale if local_scale != 0 else float("inf")
            if rel_amp > 0.05:
                p2_reversals += 1
                p2_events.append(dict(x_lo=dense_sorted[i - 1], x_hi=dense_sorted[i], rel_amp=rel_amp))
    p2_verdict = "CONFIRMED" if p2_reversals >= 2 else "FALSIFIED"
    print(f"  qualifying sign changes (>5% relative amplitude): {p2_reversals}  VERDICT={p2_verdict}")
    for ev in p2_events:
        print(f"    x=[{ev['x_lo']},{ev['x_hi']}]  rel_amp={ev['rel_amp']:.4%}")

    # ============================================================ quintile split (item 8)
    quintiles = [list(map(int, q)) for q in np.array_split(np.array(dense_sorted), 5)]
    print(f"\nQuintiles: {[ (q[0], q[-1], len(q)) for q in quintiles ]}")

    # global smooth fit to kappa_region_wide over the full DENSE_X span
    # (cubic polynomial) -- the "smooth fit" P4's measured-ratio numerator
    # is a residual against.
    x_arr = np.array(dense_sorted, dtype=float)
    wide_arr = np.array(wide_seq, dtype=float)
    poly_coeffs = np.polyfit(x_arr, wide_arr, deg=3)
    wide_smooth_fit = np.polyval(poly_coeffs, x_arr)
    wide_smooth_residual = {x: float(wide_arr[i] - wide_smooth_fit[i]) for i, x in enumerate(dense_sorted)}

    # delta_phi_wide interpolated onto DENSE_X (unwrapped across the 16
    # sparse points first, per P5's simplified proxy -- see PREDICTIONS_TEXT)
    all_x_sorted = sorted(ALL_X)
    dphi_wide_sorted = np.unwrap([dphi_wide[x] for x in all_x_sorted])
    dphi_wide_interp = dict(zip(dense_sorted,
                                 np.interp(dense_sorted, all_x_sorted, dphi_wide_sorted)))
    phase_ripple_residual = {x: dphi_point[x] - dphi_wide_interp[x] for x in dense_sorted}

    print("\n" + "=" * 78)
    print("P3/P4/P5/P6 -- per-quintile analysis")
    print("=" * 78)
    quintile_report = []
    for qi, q in enumerate(quintiles):
        q = sorted(q)
        res_q = np.array([residual_point[x] for x in q])
        wide_q = np.array([wide[x]["kappa_region_wide"] for x in q])
        wide_res_q = np.array([wide_smooth_residual[x] for x in q])
        phase_res_q = np.array([phase_ripple_residual[x] for x in q])

        period, period_diag = estimate_period(q, res_q)
        p3_in_band = period is not None and 7.0 <= period <= 13.0

        near_null, near_null_frac = (near_null_exclusion(period) if period is not None
                                       else (False, None))

        pred_ratio = predicted_ratio(period) if (period is not None and not near_null) else None

        ptp_res = float(np.ptp(res_q))
        ptp_wide_res = float(np.ptp(wide_res_q))
        if ptp_res == 0 or period is None or near_null:
            meas_ratio = None
        else:
            res_dm = res_q - res_q.mean()
            wide_dm = wide_res_q - wide_res_q.mean()
            cov = float(np.sum(res_dm * wide_dm))
            sign_proxy = np.sign(cov) if cov != 0 else 1.0
            meas_ratio = float(sign_proxy * (ptp_wide_res / ptp_res))

        p4_scored = (period is not None and not near_null and pred_ratio is not None
                     and meas_ratio is not None)
        p4_sign_match = None
        p4_mag_ok = None
        if p4_scored:
            p4_sign_match = bool(np.sign(pred_ratio) == np.sign(meas_ratio))
            if pred_ratio != 0 and meas_ratio != 0:
                mag_ratio = max(abs(pred_ratio), abs(meas_ratio)) / min(abs(pred_ratio), abs(meas_ratio))
                p4_mag_ok = bool(mag_ratio <= 2.0)
            else:
                p4_mag_ok = False
        p4_cell_pass = bool(p4_scored and p4_sign_match and p4_mag_ok)

        # P5 proxy: sign(correlation(residual_point, phase_ripple_residual)) vs sign(pred_ratio)
        p5_scored = p4_scored  # "quintiles where both P3 and P4 are determined"
        p5_match = None
        if p5_scored:
            res_dm2 = res_q - res_q.mean()
            phase_dm = phase_res_q - phase_res_q.mean()
            cov2 = float(np.sum(res_dm2 * phase_dm))
            proxy_sign = np.sign(cov2) if cov2 != 0 else 1.0
            p5_match = bool(proxy_sign == np.sign(pred_ratio))

        ripple_fraction = float(ptp_res / abs(np.mean(wide_q))) if np.mean(wide_q) != 0 else float("inf")

        row = dict(
            quintile=qi, x_lo=q[0], x_hi=q[-1], n=len(q),
            period_cells=period, period_diag=period_diag,
            p3_in_band=p3_in_band,
            near_null=bool(near_null), near_null_frac_of_11=near_null_frac,
            predicted_ratio=pred_ratio, measured_ratio=meas_ratio,
            ptp_residual_point=ptp_res, ptp_wide_smooth_residual=ptp_wide_res,
            p4_scored=p4_scored, p4_sign_match=p4_sign_match, p4_mag_ok=p4_mag_ok,
            p4_cell_pass=p4_cell_pass,
            p5_scored=p5_scored, p5_match=p5_match,
            ripple_fraction=ripple_fraction,
        )
        quintile_report.append(row)
        print(f"  Q{qi} x=[{q[0]},{q[-1]}] n={len(q)}  period={period}  "
              f"in_band[7,13]={p3_in_band}  near_null={near_null}  "
              f"pred_ratio={pred_ratio}  meas_ratio={meas_ratio}  "
              f"P4_pass={p4_cell_pass}  P5_match={p5_match}  "
              f"ripple_fraction={ripple_fraction:.4f}")

    # ---- P3 verdict
    p3_determined = [r for r in quintile_report if r["period_cells"] is not None]
    p3_in_band_count = sum(1 for r in p3_determined if r["p3_in_band"])
    p3_verdict = "CONFIRMED" if p3_in_band_count >= 3 else "FALSIFIED"

    # ---- P4 verdict
    p4_non_excluded = [r for r in quintile_report if r["p4_scored"]]
    p4_pass_count = sum(1 for r in p4_non_excluded if r["p4_cell_pass"])
    p4_verdict = ("CONFIRMED" if (len(p4_non_excluded) > 0 and p4_pass_count >= 2)
                  else ("AMBIGUOUS-NO-SCORABLE-QUINTILES" if len(p4_non_excluded) == 0 else "FALSIFIED"))

    # ---- P5 verdict
    p5_scorable = [r for r in quintile_report if r["p5_scored"]]
    p5_match_count = sum(1 for r in p5_scorable if r["p5_match"])
    if len(p5_scorable) == 0:
        p5_verdict = "AMBIGUOUS-NO-SCORABLE-QUINTILES"
    else:
        p5_verdict = "CONFIRMED" if p5_match_count > len(p5_scorable) / 2.0 else "FALSIFIED"

    # ---- P6 verdict
    ripple_fracs = [r["ripple_fraction"] for r in quintile_report]
    p6_all_le_020 = all(rf <= 0.20 for rf in ripple_fracs)
    p6_any_gt_050 = any(rf > 0.50 for rf in ripple_fracs)
    if p6_all_le_020:
        p6_verdict = "NARROWS"
    elif p6_any_gt_050:
        p6_verdict = "OVERTURNS"
    else:
        p6_verdict = "MIXED/PARTIAL"

    print("\n" + "=" * 78)
    print("VERDICTS")
    print("=" * 78)
    print(f"P1: {'CONFIRMED' if p1_pass else 'FALSIFIED'}  (max_rel={p1_max_rel:.3e})")
    print(f"P2: {p2_verdict}  (qualifying reversals={p2_reversals})")
    print(f"P3: {p3_verdict}  ({p3_in_band_count}/{len(p3_determined)} determined quintiles in [7,13], "
          f"{len(p3_determined)}/5 quintiles determined a period)")
    print(f"P4: {p4_verdict}  ({p4_pass_count}/{len(p4_non_excluded)} non-excluded quintiles pass)")
    print(f"P5: {p5_verdict}  ({p5_match_count if len(p5_scorable) else 0}/{len(p5_scorable)} scorable quintiles match)")
    print(f"P6: {p6_verdict}  (ripple_fraction per quintile: {[f'{rf:.4f}' for rf in ripple_fracs]})")

    total_wall = time.time() - t_start
    print(f"\nTotal wall time: {total_wall:.1f}s ({total_wall/60.0:.2f} min)")
    print(f"Real FDTD calls: {n_fdtd_calls} (expected 2)")

    # ============================================================ RESULT_TEXT (R23: generated from code, not hand-typed)
    result_text = f"""RESULT (exp-104, Panel Iteration 81)

{DISCLAIMER}

All 2 real FDTD calls executed exactly as budgeted (theta=0, STEPS={STEPS}),
{total_wall:.1f}s ({total_wall/60.0:.2f} min) total wall time, zero `lab/`
diff throughout.

**Gate P1 (reproducibility identity check): {'PASS' if p1_pass else 'FAIL'}.**
max relative deviation = {p1_max_rel:.3e} across all 16 original x-points,
against experiments/103-.../results.json's own kappa_region_trend
(<1e-9 required). This is the run's precondition; P2-P6 below are only
trusted because Gate P1 passed.

**P1: {'CONFIRMED' if p1_pass else 'FALSIFIED'}.**

**P2 (ripple existence): {p2_verdict}.** {p2_reversals} qualifying sign
changes (>5% relative amplitude) found in residual_point(x) across the
full 53-point DENSE_X span (>=2 required).

**P3 (per-quintile period match): {p3_verdict}.** {len(p3_determined)}/5
quintiles determined a period; {p3_in_band_count} of those fall in [7,13]
cells (>=3 required). Per-quintile periods: {[ (r['quintile'], r['period_cells']) for r in quintile_report ]}.

**P4 (signed suppression-ratio cross-check): {p4_verdict}.**
{len(p4_non_excluded)} quintile(s) scorable (determined period, not
near-null-excluded); {p4_pass_count} pass (sign match + magnitude within
2x) (>=2 required, or AMBIGUOUS if zero are scorable). Near-null-excluded
quintiles (period within 10% of an integer multiple of 11 cells): {[r['quintile'] for r in quintile_report if r['near_null']]}.

**P5 (delta_phi co-variation, simplified proxy): {p5_verdict}.**
{p5_match_count if len(p5_scorable) else 0}/{len(p5_scorable)} scorable
quintiles (both P3 and P4 determined) show sign-consistent covariation
between residual_point and the delta_phi_point-vs-interpolated-delta_phi_
wide phase-ripple residual (majority required). Proxy computed exactly as
pre-registered in PREDICTIONS_TEXT -- no rigorous per-frequency-bin phase
decomposition was attempted (delta_phi_wide is sparse by construction,
only the 16 original x-points).

**P6 (scope, narrows/overturns/mixed): {p6_verdict}.** Per-quintile
ripple_fraction_i (peak-to-peak(residual_point)/mean(kappa_region_wide)):
{[f'{rf:.4f}' for rf in ripple_fracs]}. Narrows requires all <=0.20;
overturns requires any >0.50.

Mandatory Idealizations fixes (MATERIALS' aliasing-origin disclaimer on any
P2 ripple found here, THERMODYNAMICS' thermal-sidecar N/A disclosure, the
settling-leg scope correction, and QUANTUM's citation-overreach correction
distinguishing a low-pass filter null from a sampling-rate failure) are
carried unchanged from this file's own module docstring and NOTES.md's
Idealizations section -- restated in full there, not narrowed or dropped
here.
"""
    assert DISCLAIMER in result_text, "R23: disclaimer missing from Result block"

    print("\n" + result_text)

    result = dict(
        experiment="exp-104", panel_iteration=81,
        n_fdtd_calls=n_fdtd_calls, wall_primary_s=wall_primary, total_wall_s=total_wall,
        geometry=dict(N=N, absorb=ABSORB, courant_frac=COURANT_FRAC, steps=STEPS,
                      src_x=SRC_X, cx=CX, cy=CY, r_core=R_CORE, r_coat=R_COAT,
                      r_clk=R_CLK, cpl=CPL_600, edge=EDGE,
                      h_region_wide=H_REGION_WIDE, h_region_point=H_REGION_POINT,
                      floor_frac=FLOOR_FRAC),
        behind_window=dict(x_lo=BEHIND_X_LO, x_hi=BEHIND_X_HI, y_lo=BEHIND_Y_LO, y_hi=BEHIND_Y_HI),
        all_x=ALL_X, dense_x=DENSE_X,
        gate_p1=dict(pass_=p1_pass, max_rel=p1_max_rel, rows={str(x): v for x, v in p1_rows.items()}),
        floor_gate_wide=dict(rms=fg_wide["rms"], floor=fg_wide["floor"], n_unresolved=fg_wide["n_unresolved"]),
        floor_gate_point=dict(rms=fg_point["rms"], floor=fg_point["floor"], n_unresolved=fg_point["n_unresolved"]),
        wide_channel={str(x): wide[x] for x in NEED_X},
        point_channel={str(x): point[x] for x in DENSE_X},
        delta_phi_wide={str(x): dphi_wide[x] for x in ALL_X},
        delta_phi_point={str(x): dphi_point[x] for x in DENSE_X},
        wide_pointwise_spread={str(x): spread16[x] for x in ALL_X},
        residual_point={str(x): residual_point[x] for x in DENSE_X},
        phase_ripple_residual={str(x): phase_ripple_residual[x] for x in DENSE_X},
        wide_smooth_fit_poly_coeffs=list(poly_coeffs),
        quintiles=quintile_report,
        predictions=dict(
            p1=dict(verdict="CONFIRMED" if p1_pass else "FALSIFIED", max_rel=p1_max_rel),
            p2=dict(verdict=p2_verdict, reversals=p2_reversals, events=p2_events),
            p3=dict(verdict=p3_verdict, n_determined=len(p3_determined), n_in_band=p3_in_band_count),
            p4=dict(verdict=p4_verdict, n_scored=len(p4_non_excluded), n_pass=p4_pass_count),
            p5=dict(verdict=p5_verdict, n_scored=len(p5_scorable), n_match=p5_match_count if len(p5_scorable) else 0),
            p6=dict(verdict=p6_verdict, ripple_fractions=ripple_fracs),
        ),
        predictions_text=PREDICTIONS_TEXT,
        result_text=result_text,
    )
    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(result, f, indent=2, default=str)
    print("\nresults.json written.")
    return result


if __name__ == "__main__":
    if "--predictions-only" in sys.argv:
        print(PREDICTIONS_TEXT)
    else:
        main()
