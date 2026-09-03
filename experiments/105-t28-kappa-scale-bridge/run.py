"""exp-105 -- The T8 r=78/156/312 Bridge, Extended to the Coherent
Point/Region-Intensity Channel. Panel Iteration 82. Lead seat (rotation):
THERMODYNAMICS. Frozen spec: NOTES.md (Predictions committed to git
strictly BEFORE this file's first real run, house discipline). Change
rationale: phase2_redteam_audit.md (9 numbered attacks, all 5 blind
critiques' flip conditions ADOPTED in full -- zero overridden -- plus 3
new Red-Team-only findings, 8 mandatory fixes, verdict
PROCEED-WITH-MANDATORY-FIXES).

Instrument-extension cycle, diagnostic only -- T1: N/A, zero `lab/` diff,
no mechanism proposed or varied. Executes exp-104's own Reconciled
Iteration-82 queue, Tier 1 item 1 (Red Team's consensus top pick):
extends T8's r=78/156/312 near-field-to-witness-scale scale-bridge
methodology (exp-030, Iteration 7) to the coherent, phase-resolved
point/region-intensity channel built at exp-102/103/104
(kappa_window/kappa_region_wide/kappa_region_point/delta_phi), which has
never been scale-tested. r=78 REUSED (0 new FDTD calls) from exp-103's
own established kappa_window and exp-104's own committed results.json;
r=156 unconditionally committed; r=312 cost-gated behind a timing pilot
per T8's own Iteration-7 cost-blowup precedent (8x its own hand estimate).

Mandatory fixes applied (phase2_redteam_audit.md Sec.5, priority order,
all adopted, none overridden):

1/2. The Phase-1 proposal's own hand-typed z_over_zr sentence
   (0.0253/0.0063/0.0016, plus a THIRD, separately-wrong range bracket)
   is corrected here by never hand-typing it again -- `z_over_zr(r)` and
   `predicted_ripple_period(r)` are computed by the `geom()`/`fresnel_
   check()` functions below and printed, never typed in prose.
3. Mandatory fix 6 (EM): a doubled-STEPS settling-independence leg on
   kappa_region_point/delta_phi_point SPECIFICALLY (not just the wide
   channel exp-103's own settling leg covered) at r=156, gating P4's
   verdict there -- see SETTLING_POINT block below.
4. Mandatory fix 7 (QUANTUM): a Fresnel-number-forced predicted-ripple-
   period band at each committed r (`predicted_ripple_period(r) =
   LAMBDA_CELLS*D_EFF/r`, forced by the identical z/z_R~1/r^2 geometry
   QUANTUM's own attack derived), gating whether DENSE_PITCH=2 stays
   genuinely sub-Nyquist at that r before P4's verdict is trusted --
   see `nyquist_margin()` below.
5. Mandatory fix 9 (VISION): DISCLAIMER extended to name the NETD
   classification explicitly as an instrument/detector threshold, not a
   human-perceptual one -- asserted present in both PREDICTIONS_TEXT and
   RESULT_TEXT (R23 pattern), reusing thermo_sidecar's own netd_
   disposition()['disclaimer'] string verbatim as the load-bearing
   source, not a hand-typed paraphrase.
6. Mandatory fix 8 (MATERIALS): the sigma_ext(78)=240.0 Q_ext-invariance
   thermal anchor's own diffraction-inflation/UNOBTANIUM caveat is
   restated inline, immediately before the P5 thermal table, not left in
   a different section.
7. Mandatory fix 5 (PHOTONICS, folded): T8's own P-VISION-1b REFUTED-
   for-both-articles result (exp-030) is pre-registered as prior
   information in P3's own prediction text before any run.
8. Mandatory fix 3 (Red Team's own finding): Gate P1 for the REUSED r=78
   leg is explicitly rescoped and labeled a data-loading/transcription
   self-consistency check against exp-104's own already-computed
   numbers (0 new FDTD calls at r=78) -- NOT an independent cross-run
   physics-reproducibility test the way exp-104's own Gate P1 (built on
   a FRESH Sim.run() capture) was.
9. Recommended fix (Red Team attack 4): P5's illustrative numeric bands
   are demoted to descriptive context only -- the SCORED falsifiable
   claims are (a) classification stays UNDETECTABLE at every committed
   r, and (b) the margin trend is monotonically non-increasing with
   kappa -- both genuinely falsifiable, neither resting on the disputed
   Q_ext-invariance assumption for its qualitative content (Red Team
   Sec.1 attack 4's own point: the classification-flip condition is a
   near-structural certainty given gas-conduction dominance, so it is
   kept as context, not as the sole falsifiable claim).
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
from lab import thermo_sidecar as ts                 # noqa: E402

# ================================================================ T8's own formula chain (exp-030's beam_geometry(r), re-derived here)
DX_M = 30.0e-9
R_BASE = 78
N0, ABSORB, EDGE, TAPER = 560, 40, 40, 40
CX0, CY0, SRC_X0 = 252, 280, 64
R_CORE0 = 30
STEPS0 = 3200
SIGMA_MAX0 = 0.5
CPL_600 = 20
COURANT_FRAC = 0.32
LAMBDA_CELLS = 20.0
D_EFF = 77.0  # window offset midpoint from the object's own R_COAT surface
              # ((27+127)/2), fixed in cells across r -- T8's own PLANE_DX
              # convention (exp-030 design_geometry.py:111-143), applied here.

DENSE_PITCH = 2  # cells, fixed across r (exp-104's own established value)
H_REGION_WIDE = 5
H_REGION_POINT = 0
FLOOR_FRAC = 0.10
STABILITY_TOL = 0.20        # exp-103's own established settling tolerance
PHASE_STABILITY_TOL = 0.20  # rad, new this cycle (mandatory fix 3/EM)

NETD_BAND_K = (0.020, 0.050)
K_AIR = 0.026
DENSITY_SI, C_P_SI = 2330.0, 700.0
EMISSIVITY = 0.9
T_AMBIENT_K = 293.15


def kappa_of(r):
    return r / R_BASE


def geom(r):
    """T8's own formula chain, re-derived (Phase-1 proposal Sec.2a),
    generalized: EVERY number below is computed here, never hand-typed
    in prose elsewhere in this file (mandatory fixes 1/2)."""
    k = kappa_of(r)
    N = round(N0 * k)
    CX = round(CX0 * k)
    CY = round(CY0 * k)
    SRC_X = round(SRC_X0 * k)
    STEPS = round(STEPS0 * k)
    R_CORE = round(R_CORE0 * k)
    R_COAT = r
    sigma_max = SIGMA_MAX0 / k
    tau_shell = sigma_max * (R_COAT - R_CORE)
    behind_x_lo = CX + R_COAT + 27
    behind_x_hi = CX + R_COAT + 127
    behind_y_lo = CY - 20
    behind_y_hi = CY + 20
    dense_x = list(range(CX + R_COAT + 22, CX + R_COAT + 127, DENSE_PITCH))
    right_margin = N - ABSORB - behind_x_hi
    left_margin = SRC_X - ABSORB
    bottom_margin = behind_y_lo - ABSORB
    top_margin = N - ABSORB - behind_y_hi
    z_over_zr = D_EFF * LAMBDA_CELLS / (r ** 2)          # = 1/Fresnel_number
    predicted_period = LAMBDA_CELLS * D_EFF / r          # cells (mandatory fix 4/QUANTUM)
    nyq_margin = predicted_period / (2.0 * DENSE_PITCH)
    return dict(r=r, k=k, N=N, CX=CX, CY=CY, SRC_X=SRC_X, STEPS=STEPS,
                R_CORE=R_CORE, R_COAT=R_COAT, sigma_max=sigma_max,
                tau_shell=tau_shell,
                behind=(behind_x_lo, behind_x_hi, behind_y_lo, behind_y_hi),
                dense_x=dense_x, n_dense=len(dense_x),
                right_margin=right_margin, left_margin=left_margin,
                bottom_margin=bottom_margin, top_margin=top_margin,
                z_over_zr=z_over_zr, predicted_ripple_period=predicted_period,
                nyquist_margin=nyq_margin)


def nyquist_trust_tier(margin):
    if margin >= 2.0:
        return "TRUSTED"
    if margin >= 1.0:
        return "MARGINAL-REDUCED-CONFIDENCE"
    return "UNRESOLVED-BY-CONSTRUCTION"


DISCLAIMER = ("Raw physical intensity/phase ratios only -- no Weber-contrast or "
              "C_thr(L) perceptual scoring is performed this cycle; not a claim "
              "about human visibility. " +
              ts.netd_disposition(0.0, NETD_BAND_K)["disclaimer"] + ".")


def _run(with_article, steps, g):
    sim = Sim(g["N"], g["N"], cells_per_lambda=CPL_600, courant_frac=COURANT_FRAC, absorb=ABSORB)
    if with_article:
        materials.pec_disk(sim, g["CX"], g["CY"], g["R_CORE"])
        materials.graded_black_shell(sim, g["CX"], g["CY"], g["R_CORE"], g["R_COAT"],
                                      sigma_max=g["sigma_max"])
    sim.add_line_source(g["SRC_X"], angle_deg=0.0, profile="plane", edge=EDGE)
    sim.run(steps)
    return sc.full_capture(sim)


# ================================================================ point/region readout primitives (exp-102/103/104's own formulas, byte-for-byte)
def block_mean_intensity(ez, x, y, h):
    xs = slice(x - h, x + h + 1)
    ys = slice(y - h, y + h + 1)
    return float(np.mean(np.abs(ez[xs, ys]) ** 2))


def block_mean_complex(ez, x, y, h):
    xs = slice(x - h, x + h + 1)
    ys = slice(y - h, y + h + 1)
    return complex(np.mean(ez[xs, ys]))


def point_intensity(ez, x, y):
    return float(np.abs(ez[x, y]) ** 2)


def kappa_region_wide(ez_empty, ez_article, x, y, h=H_REGION_WIDE):
    i_e = block_mean_intensity(ez_empty, x, y, h)
    i_a = block_mean_intensity(ez_article, x, y, h)
    return (i_a / i_e if i_e != 0 else float("inf")), i_e, i_a


def kappa_region_point(ez_empty, ez_article, x, y):
    i_e = point_intensity(ez_empty, x, y)
    i_a = point_intensity(ez_article, x, y)
    return (i_a / i_e if i_e != 0 else float("inf")), i_e, i_a


def wrap_phase(phi):
    wrapped = (phi + math.pi) % (2 * math.pi) - math.pi
    if wrapped <= -math.pi:
        wrapped += 2 * math.pi
    return wrapped


def delta_phi_wide(ez_empty, ez_article, x, y, h=H_REGION_WIDE):
    mean_e = block_mean_complex(ez_empty, x, y, h)
    mean_a = block_mean_complex(ez_article, x, y, h)
    if mean_e == 0:
        return float("nan")
    return wrap_phase(float(np.angle(mean_a / mean_e)))


def delta_phi_point(ez_empty, ez_article, x, y):
    ez_e, ez_a = ez_empty[x, y], ez_article[x, y]
    if ez_e == 0:
        return float("nan")
    return wrap_phase(float(np.angle(ez_a / ez_e)))


def window_stats(ez, x_lo, x_hi, y_lo, y_hi):
    block = np.abs(ez[x_lo:x_hi, y_lo:y_hi]) ** 2
    return dict(mean=float(np.mean(block)), std=float(np.std(block)),
                min=float(np.min(block)), max=float(np.max(block)))


def floor_gate(pool_values, label, floor_frac=FLOOR_FRAC):
    arr = np.asarray(pool_values, dtype=float)
    rms = float(np.sqrt(np.mean(np.square(arr))))
    floor = floor_frac * rms
    passes = [bool(v >= floor) for v in arr]
    n_unresolved = sum(1 for p in passes if not p)
    print(f"  [floor gate: {label}] n={len(arr)} rms={rms:.6e} floor={floor:.6e} "
          f"n_unresolved={n_unresolved}")
    return dict(rms=rms, floor=floor, passes=passes, n_unresolved=n_unresolved)


# ================================================================ exp-104's own sub-Nyquist P3/P4 machinery, byte-for-byte reused
def estimate_period(y_vals, dx=DENSE_PITCH):
    n = len(y_vals)
    y = np.asarray(y_vals, dtype=float)
    if n < 4:
        return None, dict(reason="too few points", n=n)
    y = y - np.mean(y)
    nfft = 1
    while nfft < 4 * n:
        nfft *= 2
    yf = np.fft.rfft(y, n=nfft)
    power = np.abs(yf) ** 2
    if len(power) < 3:
        return None, dict(reason="fft too short", n=n, nfft=nfft)
    nonzero_power = power[1:]
    peak_rel_idx = int(np.argmax(nonzero_power))
    peak_idx = peak_rel_idx + 1
    peak_power = float(power[peak_idx])
    median_power = float(np.median(nonzero_power))
    diag = dict(n=n, nfft=nfft, peak_idx=peak_idx, peak_power=peak_power, median_power=median_power)
    if median_power <= 0 or peak_power <= 3.0 * median_power:
        diag["reason"] = "peak not > 3x median non-DC bin power (noise floor)"
        return None, diag
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
    diag["reason"] = "ok"
    return float(1.0 / freq_per_cell), diag


def near_null_exclusion(p_i, box_wide=11.0, tol=0.10):
    k = 1
    best = float("inf")
    while k * box_wide < p_i + box_wide * (tol + 1):
        best = min(best, abs(p_i - box_wide * k))
        k += 1
        if k > 50:
            break
    return (best / box_wide) < tol, best / box_wide


def predicted_ratio(p_i, box_wide=11.0, box_point=1.0):
    denom = np.sinc(box_point / p_i)
    if abs(denom) < 1e-12:
        return None
    return float(np.sinc(box_wide / p_i) / denom)


def run_p4_analysis(dense_x, residual_point, wide_seq_by_x):
    """exp-104's own quintile/FFT/sinc machinery, reused verbatim, applied
    to whatever (dense_x, residual_point, wide values) are handed in."""
    dense_sorted = sorted(dense_x)
    res_seq = [residual_point[x] for x in dense_sorted]
    wide_seq = [wide_seq_by_x[x] for x in dense_sorted]
    x_arr = np.array(dense_sorted, dtype=float)
    wide_arr = np.array(wide_seq, dtype=float)
    poly_coeffs = np.polyfit(x_arr, wide_arr, deg=3)
    wide_smooth_fit = np.polyval(poly_coeffs, x_arr)
    wide_smooth_residual = {x: float(wide_arr[i] - wide_smooth_fit[i]) for i, x in enumerate(dense_sorted)}

    quintiles = [list(map(int, q)) for q in np.array_split(np.array(dense_sorted), 5)]
    quintile_report = []
    for qi, q in enumerate(quintiles):
        q = sorted(q)
        res_q = np.array([residual_point[x] for x in q])
        wide_res_q = np.array([wide_smooth_residual[x] for x in q])
        period, period_diag = estimate_period(res_q)
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
        p4_scored = (period is not None and not near_null and pred_ratio is not None and meas_ratio is not None)
        p4_sign_match = p4_mag_ok = None
        if p4_scored:
            p4_sign_match = bool(np.sign(pred_ratio) == np.sign(meas_ratio))
            if pred_ratio != 0 and meas_ratio != 0:
                mag_ratio = max(abs(pred_ratio), abs(meas_ratio)) / min(abs(pred_ratio), abs(meas_ratio))
                p4_mag_ok = bool(mag_ratio <= 2.0)
            else:
                p4_mag_ok = False
        p4_cell_pass = bool(p4_scored and p4_sign_match and p4_mag_ok)
        ripple_fraction = float(ptp_res / abs(np.mean([wide_seq_by_x[x] for x in q]))) \
            if np.mean([wide_seq_by_x[x] for x in q]) != 0 else float("inf")
        quintile_report.append(dict(
            quintile=qi, x_lo=q[0], x_hi=q[-1], n=len(q),
            period_cells=period, period_diag=period_diag,
            near_null=bool(near_null), near_null_frac_of_11=near_null_frac,
            predicted_ratio=pred_ratio, measured_ratio=meas_ratio,
            p4_scored=p4_scored, p4_sign_match=p4_sign_match, p4_mag_ok=p4_mag_ok,
            p4_cell_pass=p4_cell_pass, ripple_fraction=ripple_fraction,
        ))
    # P2-analog: ripple existence (sign changes >5% relative amplitude)
    reversals = 0
    events = []
    for i in range(1, len(dense_sorted)):
        a, b = res_seq[i - 1], res_seq[i]
        if np.sign(a) != np.sign(b) and a != 0 and b != 0:
            local_scale = 0.5 * (abs(wide_seq[i]) + abs(wide_seq[i - 1]))
            amp = max(abs(a), abs(b))
            rel_amp = amp / local_scale if local_scale != 0 else float("inf")
            if rel_amp > 0.05:
                reversals += 1
                events.append(dict(x_lo=dense_sorted[i - 1], x_hi=dense_sorted[i], rel_amp=rel_amp))
    p2_verdict = "CONFIRMED" if reversals >= 2 else "FALSIFIED"

    p4_non_excluded = [r for r in quintile_report if r["p4_scored"]]
    p4_pass_count = sum(1 for r in p4_non_excluded if r["p4_cell_pass"])
    p4_verdict = ("CONFIRMED" if (len(p4_non_excluded) > 0 and p4_pass_count >= 2)
                  else ("AMBIGUOUS-NO-SCORABLE-QUINTILES" if len(p4_non_excluded) == 0 else "FALSIFIED"))
    return dict(quintiles=quintile_report, p2_reversals=reversals, p2_events=events,
                p2_verdict=p2_verdict, p4_verdict=p4_verdict,
                p4_n_scored=len(p4_non_excluded), p4_n_pass=p4_pass_count,
                wide_smooth_fit_poly_coeffs=list(poly_coeffs))


# ================================================================ predictions text (R23: single source of truth, generated BEFORE any FDTD call)
def build_predictions_text(g78, g156, g312):
    return f"""PREDICTIONS (pre-registered, exp-105, Panel Iteration 82)

{DISCLAIMER}

**Gate P0 (ground-truth recovery, zero cost, mandatory precondition).**
geom(78) reproduces exp-103/104's own established constants EXACTLY
(N={g78['N']}, CX={g78['CX']}, CY={g78['CY']}, SRC_X={g78['SRC_X']},
STEPS={g78['STEPS']}, R_CORE={g78['R_CORE']}, sigma_max={g78['sigma_max']},
BEHIND window={g78['behind']}, dense_x span=[{g78['dense_x'][0]},{g78['dense_x'][-1]}]
n={g78['n_dense']}). Falsified by ANY mismatch -> halt, do not trust r=156/312.

**Gate P1 (r=78 leg, RESCOPED per Red Team mandatory fix 3 -- a
data-loading/transcription self-consistency check, NOT an independent
cross-run physics-reproducibility test).** 0 new FDTD calls at r=78:
kappa_region_wide(x), recomputed here from exp-104's own persisted
i_region_empty/i_region_article scalars, reproduces exp-104's own
persisted kappa_region_wide(x) to <1e-9 relative at all 16 of its ALL_X
points. This only verifies this file's own loading/division code is not
itself buggy -- it does NOT independently re-derive exp-104's own FDTD
physics (no fresh Sim.run() call backs it, unlike exp-104's own Gate P1,
which compared a FRESH capture against a stored reference).

**Fresnel/Nyquist pre-check (mandatory fix 4/QUANTUM, zero cost, computed
by geom(), not hand-typed).** predicted_ripple_period(r) =
LAMBDA_CELLS*D_EFF/r: r=78 -> {g78['predicted_ripple_period']:.3f} cells
(nyquist_margin={g78['nyquist_margin']:.3f}, {nyquist_trust_tier(g78['nyquist_margin'])});
r=156 -> {g156['predicted_ripple_period']:.3f} cells
(nyquist_margin={g156['nyquist_margin']:.3f}, {nyquist_trust_tier(g156['nyquist_margin'])});
r=312 -> {g312['predicted_ripple_period']:.3f} cells
(nyquist_margin={g312['nyquist_margin']:.3f}, {nyquist_trust_tier(g312['nyquist_margin'])}).
z_over_zr(r) = D_EFF*LAMBDA_CELLS/r^2: r=78 -> {g78['z_over_zr']:.6f}; r=156 ->
{g156['z_over_zr']:.6f}; r=312 -> {g312['z_over_zr']:.6f} (corrects the
Phase-1 proposal's own hand-typed, doubly-wrong figure -- Red Team attacks
1/2). P4's verdict at a given r is trusted in full only if that r's own
nyquist_margin>=2.0 (TRUSTED); 1.0<=margin<2.0 is reported with reduced
confidence (MARGINAL); margin<1.0 means P4 is NOT SCORED at that r
(UNRESOLVED-BY-CONSTRUCTION -- a FALSIFIED reading there could be a
second-generation aliasing null, not a genuine one).

**P2 (monotonicity, T8's own P-VISION-2 structure).** kappa_window(r)
decreases monotonically with r (78 > 156 > 312 if committed) -- predicted
CONFIRMED, matching T8's own graded_black_shell finding on the ambient
channel (exp-030). Falsified by a non-monotonic reversal at either step.

**P3 (functional-form + shape discriminator, T8's own P-VISION-1/1b
structure -- PRE-REGISTERED PRIOR, mandatory fix 5/PHOTONICS): T8's own
r=78/156/312 bridge (exp-030) already found this EXACT discriminator
REFUTED for graded_black_shell on the ambient Weber-contrast channel
(measured ratio 5.33, outside both the sqrt-law 2.00+/-0.3 and linear-law
4.00+/-0.5 bands -- a documented miss, not a fresh unknown). This cycle
asks whether the coherent-intensity channel replicates that miss or
behaves differently -- a miss here would replicate established program
history, not surprise. Full 2-point-fit-vs-held-out-r=78 test requires
r=312; if r=312 is cost-deferred (see Run budget), only the qualitative
single-step (r=78->156) trend direction is reported, explicitly NOT
scored CONFIRMED/REFUTED.**

**P4 (sub-Nyquist ripple generalization, exp-104's own P1-P6 machinery,
reused byte-for-byte, GATED by the Fresnel/Nyquist pre-check above and by
a NEW settling-independence leg on kappa_region_point/delta_phi_point
specifically -- mandatory fix 3/EM).** At r=156 (STEPS={g156['STEPS']},
doubled-STEPS settling leg at STEPS={2*g156['STEPS']}): predicted P2-analog
(ripple existence) FALSIFIED again (0 or 1 qualifying sign changes),
extending exp-104's own clean r=78 null -- IF and ONLY IF the settling
leg passes (STABILITY_TOL={STABILITY_TOL:.0%} on kappa_region_point,
{PHASE_STABILITY_TOL:.2f} rad on delta_phi_point) AND the Nyquist margin
at r=156 clears TRUSTED. If the settling leg fails, P4's r=156 verdict is
reported but flagged NOT-TRUSTED (settling artifact indistinguishable
from genuine ripple), not silently scored as if clean.

**P5 (THERMODYNAMICS' own charter prediction -- thermal sidecar, INVOKED
this cycle, mandatory fix 6/MATERIALS caveat restated immediately below,
mandatory fix 9/Red-Team-recommended reframing applied: illustrative
numeric bands are DESCRIPTIVE CONTEXT ONLY, not scored).**
DIFFRACTION-INFLATION / REALIZABILITY CAVEAT, restated inline per Red
Team attack 8 (not left in a separate section): `graded_black_shell`
remains UNOBTANIUM-WITH-PARAMETERS at every r in this family; the
sigma_ext(78)=240.0073740162445 anchor this table's `Q_ext`-invariance
placeholder depends on is, per exp-057's own results.json, "ASSERTED, NOT
INDEPENDENTLY BOUNDED" (a ~1.54x linear diffraction-inflated optical
width, not the object's true geometric diameter) -- the r=156/312 rows
below are illustrative extrapolations of that same unverified anchor, not
independent measurements. **Scored falsifiable claims (the only two,
per Red Team attack 4's own reframing):** (a) NETD classification stays
UNDETECTABLE at every committed r; (b) the margin (against
NETD_BAND_K[0]={NETD_BAND_K[0]}) trend is monotonically non-increasing
with kappa. Falsified only if either fails.

Mandatory Idealizations: 2D TMz, single lambda=600nm/cpl=20 scope,
theta=0 deg only (see NOTES.md for the full justification carried
forward from the Phase-1 proposal), graded_black_shell remains
UNOBTANIUM-WITH-PARAMETERS at every r, no witness-scale extrapolation
attempted or claimed this cycle.
"""


# ================================================================ main
def main():
    print("=" * 78)
    print("exp-105 -- T8 r=78/156/312 bridge, extended to the coherent")
    print("point/region-intensity channel")
    print("=" * 78)

    t_start = time.time()
    n_fdtd_calls = 0

    g78, g156, g312 = geom(78), geom(156), geom(312)

    # ---------------------------------------------------------- Gate P0
    exp104_dir = os.path.join(ROOT, "experiments", "104-t28-subnyquist-standoff-recheck")
    with open(os.path.join(exp104_dir, "results.json")) as f:
        exp104 = json.load(f)
    p0_pass = (g78["N"] == exp104["geometry"]["N"] and
               g78["CX"] == exp104["geometry"]["cx"] and
               g78["CY"] == exp104["geometry"]["cy"] and
               g78["SRC_X"] == exp104["geometry"]["src_x"] and
               g78["STEPS"] == exp104["geometry"]["steps"] and
               g78["R_CORE"] == exp104["geometry"]["r_core"] and
               abs(g78["sigma_max"] - 0.5) < 1e-12 and
               g78["behind"] == (exp104["behind_window"]["x_lo"], exp104["behind_window"]["x_hi"],
                                  exp104["behind_window"]["y_lo"], exp104["behind_window"]["y_hi"]) and
               g78["dense_x"] == exp104["dense_x"])
    print(f"\n[Gate P0] geom(78) reproduces exp-104's established constants: PASS={p0_pass}")
    if not p0_pass:
        raise SystemExit("GATE P0 FAILED -- formula chain mis-derived; halting before any FDTD call.")

    print(f"\n{build_predictions_text(g78, g156, g312)}")

    # margin gates for every committed geometry (156 unconditional; 312 checked before any call)
    for label, g in (("r=156", g156), ("r=312", g312)):
        for x in g["dense_x"]:
            lo_x, hi_x = x - H_REGION_WIDE, x + H_REGION_WIDE
            assert lo_x > ABSORB and hi_x < g["N"] - ABSORB, f"{label} x={x} block too close to boundary"
        lo_y, hi_y = g["CY"] - H_REGION_WIDE, g["CY"] + H_REGION_WIDE
        assert lo_y > ABSORB and hi_y < g["N"] - ABSORB
        print(f"[margin gate] {label}: {g['n_dense']} standoff points, all clear of absorb/boundary: PASS "
              f"(right={g['right_margin']}, left={g['left_margin']}, "
              f"bottom={g['bottom_margin']}, top={g['top_margin']})")

    # ============================================================ r=78 leg: 0 new FDTD calls, reused from exp-103/104
    exp103_path = os.path.join(ROOT, "experiments", "103-t28-gateb-footprint-aperture-match", "results.json")
    with open(exp103_path) as f:
        exp103 = json.load(f)
    kappa_window_78 = exp103["kappa_window"]["value"]

    wide78 = {int(x): v["kappa_region_wide"] for x, v in exp104["wide_channel"].items()}
    i_e_wide78 = {int(x): v["i_region_empty"] for x, v in exp104["wide_channel"].items()}
    i_a_wide78 = {int(x): v["i_region_article"] for x, v in exp104["wide_channel"].items()}
    all_x_78 = exp104["all_x"]

    # Gate P1 (rescoped, mandatory fix 3): recompute kappa_region_wide at
    # ALL_X from the SAME stored scalars, compare to the stored ratio.
    p1_max_rel = 0.0
    for x in all_x_78:
        recomputed = i_a_wide78[x] / i_e_wide78[x] if i_e_wide78[x] != 0 else float("inf")
        stored = wide78[x]
        rel = abs(recomputed - stored) / abs(stored) if stored != 0 else float("inf")
        p1_max_rel = max(p1_max_rel, rel)
    p1_pass = p1_max_rel < 1e-9
    print(f"\n[Gate P1, RESCOPED r=78 self-consistency check] max_rel={p1_max_rel:.3e} PASS={p1_pass}")
    if not p1_pass:
        raise SystemExit("GATE P1 (rescoped) FAILED -- halting, do not trust r=78 leg.")

    dense78 = {int(x): v for x, v in exp104["point_channel"].items()}
    residual_point_78 = {int(x): v["kappa_region_point"] - wide78[int(x)] for x, v in exp104["point_channel"].items()}
    p4_78 = run_p4_analysis(g78["dense_x"], residual_point_78,
                             {x: wide78[x] for x in g78["dense_x"]})
    nyq78 = nyquist_trust_tier(g78["nyquist_margin"])
    print(f"[r=78, REUSED] kappa_window={kappa_window_78:.6e}  "
          f"P2-analog={p4_78['p2_verdict']} (reversals={p4_78['p2_reversals']})  "
          f"P4={p4_78['p4_verdict']} nyquist_tier={nyq78}")

    # ============================================================ r=156 leg: 2 primary + 2 settling calls
    print("\n" + "=" * 78)
    print(f"r=156 PRIMARY PAIR -- empty + article, theta=0, STEPS={g156['STEPS']}")
    print("=" * 78)
    t0 = time.time()
    cap_e156 = _run(False, g156["STEPS"], g156)
    cap_a156 = _run(True, g156["STEPS"], g156)
    n_fdtd_calls += 2
    wall_156_primary = time.time() - t0
    print(f"r=156 primary pair wall time: {wall_156_primary:.1f}s")
    ez_e156 = sc.phasors(cap_e156)["ez"]
    ez_a156 = sc.phasors(cap_a156)["ez"]

    win_e156 = window_stats(ez_e156, *g156["behind"])
    win_a156 = window_stats(ez_a156, *g156["behind"])
    kappa_window_156 = win_a156["mean"] / win_e156["mean"]

    wide156, i_e_wide156, i_a_wide156 = {}, {}, {}
    point156, i_e_point156, i_a_point156 = {}, {}, {}
    dphi_w156, dphi_p156 = {}, {}
    for x in g156["dense_x"]:
        k_w, i_e_w, i_a_w = kappa_region_wide(ez_e156, ez_a156, x, g156["CY"])
        k_p, i_e_p, i_a_p = kappa_region_point(ez_e156, ez_a156, x, g156["CY"])
        wide156[x], i_e_wide156[x], i_a_wide156[x] = k_w, i_e_w, i_a_w
        point156[x], i_e_point156[x], i_a_point156[x] = k_p, i_e_p, i_a_p
        dphi_w156[x] = delta_phi_wide(ez_e156, ez_a156, x, g156["CY"])
        dphi_p156[x] = delta_phi_point(ez_e156, ez_a156, x, g156["CY"])

    fg_wide156 = floor_gate([i_e_wide156[x] for x in g156["dense_x"]], "r=156 wide channel")
    fg_point156 = floor_gate([i_e_point156[x] for x in g156["dense_x"]], "r=156 point channel")

    residual_point_156 = {x: point156[x] - wide156[x] for x in g156["dense_x"]}

    # ------------------------------------------------------ settling leg (mandatory fix 3/EM): point channel + delta_phi_point SPECIFICALLY
    print("\n" + "=" * 78)
    print(f"r=156 SETTLING-INDEPENDENCE LEG on kappa_region_point/delta_phi_point "
          f"-- STEPS={2*g156['STEPS']}")
    print("=" * 78)
    t0 = time.time()
    cap_e156_2x = _run(False, 2 * g156["STEPS"], g156)
    cap_a156_2x = _run(True, 2 * g156["STEPS"], g156)
    n_fdtd_calls += 2
    wall_156_settling = time.time() - t0
    print(f"r=156 settling pair wall time: {wall_156_settling:.1f}s")
    ez_e156_2x = sc.phasors(cap_e156_2x)["ez"]
    ez_a156_2x = sc.phasors(cap_a156_2x)["ez"]

    settling156 = {}
    settling_kappa_pass = True
    settling_phase_pass = True
    for x in g156["dense_x"]:
        k1 = point156[x]
        k2, _, _ = kappa_region_point(ez_e156_2x, ez_a156_2x, x, g156["CY"])
        rel_change = abs(k2 - k1) / abs(k1) if k1 != 0 else float("inf")
        kappa_pass = rel_change <= STABILITY_TOL
        p1_phase = dphi_p156[x]
        p2_phase = delta_phi_point(ez_e156_2x, ez_a156_2x, x, g156["CY"])
        phase_diff = abs(wrap_phase(p2_phase - p1_phase)) if not (math.isnan(p1_phase) or math.isnan(p2_phase)) else float("nan")
        phase_pass = (phase_diff <= PHASE_STABILITY_TOL) if not math.isnan(phase_diff) else False
        settling_kappa_pass = settling_kappa_pass and kappa_pass
        settling_phase_pass = settling_phase_pass and phase_pass
        settling156[x] = dict(kappa_point_1x=k1, kappa_point_2x=k2, rel_change=rel_change,
                               kappa_pass=bool(kappa_pass), dphi_point_1x=p1_phase,
                               dphi_point_2x=p2_phase, phase_diff=phase_diff, phase_pass=bool(phase_pass))
    n_kappa_fail = sum(1 for v in settling156.values() if not v["kappa_pass"])
    n_phase_fail = sum(1 for v in settling156.values() if not v["phase_pass"])
    settling_overall_pass = settling_kappa_pass and settling_phase_pass
    print(f"[settling gate, r=156, point channel] kappa PASS(all<= {STABILITY_TOL:.0%})={settling_kappa_pass} "
          f"({n_kappa_fail}/{len(g156['dense_x'])} failed); "
          f"phase PASS(all<={PHASE_STABILITY_TOL:.2f}rad)={settling_phase_pass} "
          f"({n_phase_fail}/{len(g156['dense_x'])} failed); OVERALL={settling_overall_pass}")

    p4_156 = run_p4_analysis(g156["dense_x"], residual_point_156, wide156)
    nyq156 = nyquist_trust_tier(g156["nyquist_margin"])
    p4_156_trusted = settling_overall_pass and (nyq156 == "TRUSTED")
    print(f"[r=156] kappa_window={kappa_window_156:.6e}  "
          f"P2-analog={p4_156['p2_verdict']} (reversals={p4_156['p2_reversals']})  "
          f"P4={p4_156['p4_verdict']}  nyquist_tier={nyq156}  "
          f"settling_pass={settling_overall_pass}  P4_TRUSTED={p4_156_trusted}")

    # ============================================================ r=312 leg: cost-gated pilot
    print("\n" + "=" * 78)
    print("r=312 COST-GATED PILOT -- empty scene alone")
    print("=" * 78)
    t0 = time.time()
    cap_e312 = _run(False, g312["STEPS"], g312)
    n_fdtd_calls += 1
    wall_312_pilot = time.time() - t0
    projected_2call_min = 2 * wall_312_pilot / 60.0
    print(f"r=312 pilot (empty scene) wall time: {wall_312_pilot:.1f}s "
          f"({wall_312_pilot/60.0:.2f} min). Projected 2-call total: {projected_2call_min:.2f} min.")

    r312_committed = projected_2call_min < 180.0 and (wall_312_pilot / 60.0) < 90.0
    print(f"[r=312 cost gate] committed={r312_committed} "
          f"(rule: pilot<90min AND projected-2call<180min)")

    kappa_window_312 = None
    p2_verdict_312 = p4_312 = None
    nyq312 = nyquist_trust_tier(g312["nyquist_margin"])
    wall_312_article = None
    if r312_committed:
        t0 = time.time()
        cap_a312 = _run(True, g312["STEPS"], g312)
        n_fdtd_calls += 1
        wall_312_article = time.time() - t0
        print(f"r=312 article-scene call wall time: {wall_312_article:.1f}s")
        ez_e312 = sc.phasors(cap_e312)["ez"]
        ez_a312 = sc.phasors(cap_a312)["ez"]
        win_e312 = window_stats(ez_e312, *g312["behind"])
        win_a312 = window_stats(ez_a312, *g312["behind"])
        kappa_window_312 = win_a312["mean"] / win_e312["mean"]

        wide312, i_e_wide312, point312 = {}, {}, {}
        for x in g312["dense_x"]:
            k_w, i_e_w, i_a_w = kappa_region_wide(ez_e312, ez_a312, x, g312["CY"])
            k_p, _, _ = kappa_region_point(ez_e312, ez_a312, x, g312["CY"])
            wide312[x], i_e_wide312[x], point312[x] = k_w, i_e_w, k_p
        fg_wide312 = floor_gate([i_e_wide312[x] for x in g312["dense_x"]], "r=312 wide channel")
        residual_point_312 = {x: point312[x] - wide312[x] for x in g312["dense_x"]}
        p4_312 = run_p4_analysis(g312["dense_x"], residual_point_312, wide312)
        print(f"[r=312] kappa_window={kappa_window_312:.6e}  "
              f"P2-analog={p4_312['p2_verdict']} (reversals={p4_312['p2_reversals']})  "
              f"P4={p4_312['p4_verdict']}  nyquist_tier={nyq312}")
    else:
        print("[r=312] COST-DEFERRED, not attempted beyond the empty-scene pilot -- "
              "queued for a future cycle per the pre-registered cost-gating rule.")

    total_wall = time.time() - t_start

    # ============================================================ P2/P3 verdicts
    kappa_windows = dict(r78=kappa_window_78, r156=kappa_window_156, r312=kappa_window_312)
    if kappa_window_312 is not None:
        p2_monotonic = kappa_window_78 > kappa_window_156 > kappa_window_312
        p2_verdict = "CONFIRMED" if p2_monotonic else "FALSIFIED"
    else:
        p2_monotonic = kappa_window_78 > kappa_window_156
        p2_verdict = "CONFIRMED-PARTIAL(78->156 only)" if p2_monotonic else "FALSIFIED-PARTIAL(78->156 only)"

    p3_full = kappa_window_312 is not None
    p3_result = {}
    if p3_full:
        x78 = math.sqrt(g78["z_over_zr"])
        x156 = math.sqrt(g156["z_over_zr"])
        x312 = math.sqrt(g312["z_over_zr"])
        # Model A (sqrt-law, linear in x): fit on (156,312), held out 78
        BA = (kappa_window_156 - kappa_window_312) / (x156 - x312)
        CA = kappa_window_156 - BA * x156
        pred78_A = CA + BA * x78
        missA = abs(pred78_A - kappa_window_78) / abs(kappa_window_78)
        # Model B (linear-law, linear in x^2): fit on (156,312), held out 78
        BB = (kappa_window_156 - kappa_window_312) / (x156 ** 2 - x312 ** 2)
        CB = kappa_window_156 - BB * x156 ** 2
        pred78_B = CB + BB * x78 ** 2
        missB = abs(pred78_B - kappa_window_78) / abs(kappa_window_78)
        shape_ratio = ((kappa_window_78 - kappa_window_156) / (kappa_window_156 - kappa_window_312)
                        if (kappa_window_156 - kappa_window_312) != 0 else float("inf"))
        p3_result = dict(x78=x78, x156=x156, x312=x312, model_A_B=BA, model_A_C=CA,
                          model_A_pred78=pred78_A, model_A_miss=missA,
                          model_B_B=BB, model_B_C=CB, model_B_pred78=pred78_B,
                          model_B_miss=missB, shape_ratio=shape_ratio,
                          verdict="SCORED")
        print(f"\n[P3] x(78:156:312)={x78:.4f}:{x156:.4f}:{x312:.4f}  "
              f"shape_ratio={shape_ratio:.4f}  "
              f"Model-A miss={missA:.4%}  Model-B miss={missB:.4%}")
    else:
        single_step_dir = "DEEPENS" if kappa_window_156 < kappa_window_78 else "SHALLOWS"
        p3_result = dict(verdict=f"PARTIAL-NOT-SCORED (r=312 not committed; single-step 78->156 {single_step_dir})")
        print(f"\n[P3] PARTIAL, not scored -- r=312 not committed this shift. "
              f"Single-step 78->156: {single_step_dir}.")

    # ============================================================ P5 -- thermal sidecar
    print("\n" + "=" * 78)
    print("P5 -- THERMAL SIDECAR (mixed_length_scale_regime, Q_ext-invariance placeholder)")
    print("=" * 78)
    SIGMA_EXT_78 = 240.0073740162445
    P_ABS_78 = 1.7409069740390205e-12
    RATIO_ABS_EXT = 0.51
    Q_EXT = SIGMA_EXT_78 / (2 * 78)
    width_m_78 = SIGMA_EXT_78 * DX_M
    i_incident = (P_ABS_78 / RATIO_ABS_EXT) / ((width_m_78 ** 2) * 1e4)

    thermal_rows = {}
    r_list = [78, 156] + ([312] if r312_committed else [])
    for r in r_list:
        r_out_m = r * DX_M
        sigma_ext_r = Q_EXT * 2 * r
        width_m = sigma_ext_r * DX_M
        p_abs = i_incident * (width_m ** 2) * 1e4 * RATIO_ABS_EXT
        regime = ts.mixed_length_scale_regime(
            p_abs_w=p_abs, l_geometric_m=r_out_m, k_air=K_AIR,
            density_kg_m3=DENSITY_SI, c_p_j_kgk=C_P_SI, emissivity=EMISSIVITY,
            t_ambient_k=T_AMBIENT_K, length_provenance="bench_construction")
        dt_ss = regime["dt_ss_full_K"]
        margin = NETD_BAND_K[0] / dt_ss
        disp = ts.netd_disposition(dt_ss, NETD_BAND_K)
        thermal_rows[r] = dict(sigma_ext=sigma_ext_r, p_abs_w=p_abs,
                                h_eff=regime["h_eff_w_m2k"], dt_ss_K=dt_ss,
                                margin=margin, classification=disp["classification"])
        print(f"  r={r}  sigma_ext={sigma_ext_r:.3f}  p_abs_w={p_abs:.6e}  "
              f"dt_ss_K={dt_ss:.6e}  margin={margin:.3f}x  class={disp['classification']}")

    r78_reproduces = abs(thermal_rows[78]["dt_ss_K"] - 2.8601275372385233e-05) < 1e-10
    print(f"  [ground-truth check] r=78 row reproduces exp-057's locked "
          f"699.27x citation: {r78_reproduces}")

    p5_all_undetectable = all(v["classification"] == "UNDETECTABLE" for v in thermal_rows.values())
    margins_in_order = [thermal_rows[r]["margin"] for r in r_list]
    p5_margin_monotonic = all(margins_in_order[i] >= margins_in_order[i + 1]
                               for i in range(len(margins_in_order) - 1))
    p5_verdict = "CONFIRMED" if (p5_all_undetectable and p5_margin_monotonic) else "FALSIFIED"
    print(f"[P5] all_undetectable={p5_all_undetectable}  "
          f"margin_monotonic_nonincreasing={p5_margin_monotonic}  VERDICT={p5_verdict}")

    print(f"\nTotal wall time: {total_wall:.1f}s ({total_wall/60.0:.2f} min)")
    print(f"Real FDTD calls: {n_fdtd_calls}")

    # ============================================================ RESULT_TEXT (R23 pattern)
    result_text = f"""RESULT (exp-105, Panel Iteration 82)

{DISCLAIMER}

{n_fdtd_calls} real FDTD calls, {total_wall:.1f}s ({total_wall/60.0:.2f} min)
total wall time, zero `lab/` diff throughout.

**Gate P0 (ground-truth recovery): {'PASS' if p0_pass else 'FAIL'}.**
**Gate P1 (r=78, RESCOPED self-consistency check): {'PASS' if p1_pass else 'FAIL'}**
(max_rel={p1_max_rel:.3e}) -- verifies this file's own loading/division
code only, NOT an independent cross-run physics reproduction (mandatory
fix 3).

**Fresnel/Nyquist pre-check:** r=78 nyquist_margin={g78['nyquist_margin']:.3f}
({nyq78}); r=156 nyquist_margin={g156['nyquist_margin']:.3f} ({nyq156});
r=312 nyquist_margin={g312['nyquist_margin']:.3f} ({nyq312}).
z_over_zr(r): r=78={g78['z_over_zr']:.6f}, r=156={g156['z_over_zr']:.6f},
r=312={g312['z_over_zr']:.6f} (computed here, corrects the Phase-1
proposal's own doubly-wrong hand-typed figure).

**kappa_window(r):** r=78 (REUSED)={kappa_window_78:.6e}; r=156 (NEW)=
{kappa_window_156:.6e}; r=312={'NOT COMMITTED (cost-gated)' if kappa_window_312 is None else f'{kappa_window_312:.6e}'}.

**P2 (monotonicity): {p2_verdict}.**

**P3 (functional-form + shape discriminator): {p3_result['verdict']}.**
{('Model-A (sqrt-law) miss=' + format(p3_result.get('model_A_miss', 0), '.4%') +
  ', Model-B (linear-law) miss=' + format(p3_result.get('model_B_miss', 0), '.4%') +
  ', shape_ratio=' + format(p3_result.get('shape_ratio', 0), '.4f')) if p3_full else
 'r=312 not committed this shift -- see run budget/cost gate above.'}
Pre-registered prior (mandatory fix 5): T8's own r=78/156/312 bridge
(exp-030) already found this discriminator REFUTED for graded_black_shell
on the ambient channel (ratio 5.33, outside both bands) -- a miss here
would replicate, not contradict, established program history.

**P4 (sub-Nyquist ripple generalization, GATED):** r=78 (reused)
P2-analog={p4_78['p2_verdict']}, P4={p4_78['p4_verdict']}, nyquist_tier={nyq78}.
r=156 (new) P2-analog={p4_156['p2_verdict']}, P4={p4_156['p4_verdict']},
nyquist_tier={nyq156}, settling_pass={settling_overall_pass},
**P4_TRUSTED={p4_156_trusted}** (settling AND Nyquist-margin gates both
required per mandatory fixes 3/4). {'r=312 P2-analog=' + p4_312['p2_verdict'] + ', P4=' + p4_312['p4_verdict'] + ', nyquist_tier=' + nyq312 + ' (no settling leg run at r=312 this cycle -- disclosed idealization, Next item).' if p4_312 is not None else 'r=312 not committed this shift.'}

**P5 (thermal sidecar): {p5_verdict}.** Realizability/diffraction-inflation
caveat (mandatory fix 6, restated inline): `graded_black_shell` is
UNOBTANIUM-WITH-PARAMETERS at every r; the sigma_ext(78)=240.007...
anchor is exp-057's own "ASSERTED, NOT INDEPENDENTLY BOUNDED" diffraction-
inflated optical width, not an independent measurement -- the r=156/312
rows are illustrative extrapolations of that same unverified anchor.
Scored claims only (mandatory fix 9): classification stays UNDETECTABLE
at every committed r ({p5_all_undetectable}); margin trend monotonically
non-increasing with kappa ({p5_margin_monotonic}). r=78 ground-truth
reproduction of the locked 699.27x citation: {r78_reproduces}.

**r=312 cost gate:** pilot wall time {wall_312_pilot:.1f}s
({wall_312_pilot/60.0:.2f} min); committed={r312_committed}.
"""
    assert DISCLAIMER in result_text, "R23: disclaimer missing from Result block"
    print("\n" + result_text)

    result = dict(
        experiment="exp-105", panel_iteration=82,
        n_fdtd_calls=n_fdtd_calls, total_wall_s=total_wall,
        wall_156_primary_s=wall_156_primary, wall_156_settling_s=wall_156_settling,
        wall_312_pilot_s=wall_312_pilot, wall_312_article_s=wall_312_article,
        geom_78=g78, geom_156=g156, geom_312=g312,
        gate_p0=dict(pass_=p0_pass),
        gate_p1_rescoped=dict(pass_=p1_pass, max_rel=p1_max_rel),
        kappa_windows=kappa_windows,
        r78=dict(p2=p4_78["p2_verdict"], p2_reversals=p4_78["p2_reversals"],
                  p4=p4_78["p4_verdict"], nyquist_tier=nyq78, quintiles=p4_78["quintiles"]),
        r156=dict(p2=p4_156["p2_verdict"], p2_reversals=p4_156["p2_reversals"],
                   p4=p4_156["p4_verdict"], nyquist_tier=nyq156, quintiles=p4_156["quintiles"],
                   settling=settling156, settling_kappa_pass=settling_kappa_pass,
                   settling_phase_pass=settling_phase_pass, settling_overall_pass=settling_overall_pass,
                   p4_trusted=p4_156_trusted,
                   wide_channel=wide156, point_channel=point156,
                   delta_phi_wide=dphi_w156, delta_phi_point=dphi_p156,
                   floor_gate_wide=fg_wide156, floor_gate_point=fg_point156),
        r312=(dict(p2=p4_312["p2_verdict"], p2_reversals=p4_312["p2_reversals"],
                    p4=p4_312["p4_verdict"], nyquist_tier=nyq312, quintiles=p4_312["quintiles"],
                    committed=True)
              if r312_committed else dict(committed=False, pilot_wall_s=wall_312_pilot)),
        p2_verdict=p2_verdict, p3=p3_result,
        thermal_rows=thermal_rows, p5_verdict=p5_verdict,
        p5_all_undetectable=p5_all_undetectable, p5_margin_monotonic=p5_margin_monotonic,
        r78_reproduces_locked_citation=r78_reproduces,
        predictions_text=build_predictions_text(g78, g156, g312),
        result_text=result_text,
    )
    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(result, f, indent=2, default=str)
    print("\nresults.json written.")
    return result


if __name__ == "__main__":
    if "--predictions-only" in sys.argv:
        g78, g156, g312 = geom(78), geom(156), geom(312)
        print(build_predictions_text(g78, g156, g312))
    else:
        main()
