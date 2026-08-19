"""exp-046 -- Panel Iteration 23: the aperture-consistent single-coherent-mode
beam (Block A, live thread T21), T23's mixed length-scale regime (Block B), and
the dose-accumulation extension to the full exp-038 grid (Block C).
Lead seat: THERMODYNAMICS (rotation). Director: this shift.

PHASE 4 IMPLEMENTATION NOTE. This file implements the configuration adopted in
`phase3_synthesis.md`, which adopted ALL 24 items of Red Team's mandatory-fix
docket (`phase2_redteam_audit.md`) with none overridden. Item 24 is a standing
program-integrity rule (LOGBOOK propagation at Phase 5), not code; the 23
substantive items are load-bearing here and are marked [docket N] at the point
of application. The Phase-1 proposal's own text survives unedited in
`phase1_proposal.md` as the historical record of what was proposed and
critiqued -- per this program's "flag, don't rewrite" convention.

Docket items, and where each lands:

  1  width = w0/cos(theta0) at EVERY oblique call (analytic AND FDTD).
  2  observation-plane w_y formula kept; the 199.33 slip corrected to 210.54.
  3  section-2.1 table re-issued: w_line, theta0-dependent z_R,line,
     N_F = 0.40-67.5, aperture ratio 2.15x-35.8x at theta0=40deg.
  4  BAND-SETTER REPLACED: the closed-form envelope no longer sets any band.
     Every A-band is set by a desk propagation of the ACTUAL complex aperture
     exp(-(Y/w_line)^2)*exp(i k sin(theta0) Y) through exp-042's own committed
     Huygens-Fresnel propagator (`_G0_for` + the corrected E/H reduction),
     reduced through `lab.ambient.window_means`/`weber`. The closed form is
     RETAINED only as a disclosed accuracy anchor, with its measured accuracy
     printed.
  5  A1 re-scoped to a POINTING/ESTIMATOR reading (explicitly not a coherence
     adjudication); A3 re-scoped to a desk-verifiable identity check with a
     numeric tolerance; `C_THR`'s own disclaiming comment carried verbatim.
  6  denominators fixed: FWHM<=10deg is 27 cells, FWHM=20deg is 9 cells.
  7  P-TH23-A4 DROPPED entirely (its premise -- a large FWHM=20 divergence --
     is false under the fix).
  8  P-TH23-A2 re-banded from the numerical propagation.
  9  P-TH23-A7 DROPPED entirely (conditioning factor 77-300x). The two
     object-present FDTD legs it motivated are still run, and reported as
     EXPLORATORY-NON-SCORING context, so the committed 9-call budget is
     unchanged and the data exists for a future, better-conditioned estimator.
  10 A3's target-convention mismatch disclosed, AND a corrected-convention
     coherent column generated here so the comparison can be made at matched
     convention (exp-042's committed `C_coherent` exists only under the
     superseded obliquity-on-E recipe; `block_beam_corrected` has no coherent
     column at all -- verified).
  11 idealization 4 restated with the corrected truncation numbers; the aimed
     leg is kept but per-cell truncation-validity flagged (cells whose rim
     amplitude exceeds 1e-2 are excluded from every aimed-leg summary).
  12 idealization 2 restated: the waist is 1.0737*lambda at ALL THREE
     wavelengths, one value -- so Block A's 3-lambda sweep carries no material
     wavelength dependence beyond fixed cell geometry.
  13 stage-16 oblique-width gate (600nm/theta0=40deg/width=56.063 ->
     1/e^2 half-width 79.47 cells, <=5%) added to `lab/validation/run_all.py`
     AND recomputed here as this run's own self-check.
  14 S16-c's tolerance restated as RELATIVE, with this shift's execution
     platform named.
  15 SIGN-CONVENTION GUARD: exp-042's analytic `B(y)` is globally negative
     (`Sx = -Re(E conj(H))`), the FDTD `observer_profile` is positive. `weber`
     is invariant under a global sign flip, so only `weber`-reduced SCALARS
     are ever compared across code paths here -- never `B(y)` profiles
     cell-by-cell, never a ratio of two `B`s, never analytic `B` mixed into
     `incoherent_sum` with an FDTD `B`. Enforced by `_weber_of` being the only
     route from any profile to any compared number.
  16 Block C extended to the FULL 5-host x 5-ratio exp-038 grid (Host E and
     the r=1.0 column added), minus Host D's 4 already-committed exp-045
     points. The new-point count is COMPUTED here and printed, not asserted.
  17 C3's scanned parameter is `dt_sweep` (the ON dwell D), NOT `T_pulse`
     (which is the OFF gap under exp-045's own disclosed role inversion).
     C3/C6 relabelled VERIFICATION of C2's closed form, not a test of it.
  18 silicon identity labelled `ASSUMED -- provenance terminates unsourced
     (T18)`, not "sourced".
  19 fill-factor idealization disclosed + rho*C_P sensitivity row; the
     "decided by the conduction length alone" claim corrected to the full
     rho C_P L^2/(4 eps sigma T^3 L + k_air) dependence.
  20 "eye-invisible" STRUCK everywhere; replaced by the disclaimed
     NETD/detectability framing `lab/thermo_sidecar.py` already provides.
  21 the NETD disclaimer inlined at the point of claim (console prints and
     every prediction record), not storage-only.
  22 REALIZABILITY_MEMO.md Amendment 5 (separate file, appended at Phase 4).
  23 small slips fixed: C = 0.374781250, ln(21 e^-0.5) = 2.5445224, C5's
     agreement floor ~2e-15, C6's r=1e-1 supremum 1.010711 / threshold 2.590.

Run:
  python3 run.py --predict-only   -> prints every P-TH23-* band, ZERO FDTD calls
  python3 run.py                  -> the same desk work + Block A's 9 FDTD
                                     legs, writes results.json

The `--predict-only` path never imports `lab.fdtd2d` (the import lives inside
`fdtd_leg`), so "predictions computed before any FDTD call" is a structural
property of this file, not a promise.
"""
import argparse
import json
import math
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
EXP042 = os.path.join(ROOT, "experiments", "042-t21-magnitude-bridge")
EXP041 = os.path.join(ROOT, "experiments", "041-t20-angle-audit")
EXP038 = os.path.join(ROOT, "experiments", "038-t17-rate-equation-kernel")
EXP045 = os.path.join(ROOT, "experiments", "045-intermediate-dwell-stress-hconv-rederivation")
sys.path.insert(0, ROOT)
sys.path.insert(0, EXP042)

import design_geometry as dg            # exp-042's own committed geometry+propagator
from lab import ambient as amb
from lab import kinetics as kin
from lab import thermo_sidecar as ts

# exp-038's own realizability tier function, imported rather than re-copied
# (Phase-1 section 6: "Block C imports exp-038's copy rather than making a third").
_prev_path = list(sys.path)
sys.path.insert(0, EXP038)
import importlib.util as _ilu
_spec = _ilu.spec_from_file_location("exp038_run", os.path.join(EXP038, "run.py"))
_exp038 = _ilu.module_from_spec(_spec)
_spec.loader.exec_module(_exp038)
sys.path = _prev_path
realizability_tier = _exp038.realizability_tier

# ============================================================== shared strings
NETD_DISCLAIMER = (
    "NETD is an instrument/detector threshold, not a human perceptual one "
    "(VISION SCIENCE's standing mandatory fix; exp-043 Red Team attack 7, "
    "exp-044 fix 6, exp-045 fix 6, exp-046 docket item 20/21). This "
    "classification does NOT bear on constraint-3/4's human-eye verdict, and "
    "no 'eye-invisible' claim is made in any committed result of this cycle "
    "[docket 20; wording corrected at Phase 5, p5 docket item 3 -- see "
    "phase5_erratum.phase1_proposal_superseded_banner].")
C_THR_COMMENT = ("VISION's T2 photopic C_thr -- context only, this leg scores "
                 "no perceptual pass/fail")   # verbatim from 042/run.py:41 [docket 5]
SILICON_PROVENANCE = "ASSUMED -- provenance terminates unsourced (T18)"  # [docket 18]

# ---------------------------------------------------------------------------
# PHASE-5 MANDATORY-FIX DOCKET (phase5_redteam_audit.md section 8), applied in
# the same shift as the audit that raised it. Tier-0 items 1-5 are
# checkpoint-criterion-4-conditional; Tier-1 items 6-20 are mandatory same
# shift by this program's established convention. Every [p5 docket N] marker
# below is one of them.
# ---------------------------------------------------------------------------

# [p5 docket 4] The item-24 hardened rule, in ONE rendering. This string is the
# single source of truth: it is written to results.json, propagated verbatim to
# NOTES.md, and is the text to carry to LOGBOOK's Iteration-23 close.
ITEM_24_HARDENED_RULE = (
    "If Iteration 24 closes without VISION SCIENCE's glare/adaptation Tier-W "
    "sidecar having been run (by any lead seat, sourced via "
    "WebSearch-snippet-tier per the standing T18 adaptation), Checkpoint "
    "criterion 4 fires automatically and immediately -- no further debate, no "
    "seat vote, no Director discretion, and no further one-cycle extensions "
    "via prose. A Phase-2 Red Team audit blessing a renewed deferral does NOT "
    "satisfy this rule: Iteration 23's own deferral was Red-Team-blessed, and "
    "that is what tripped it.")
ITEM_24_RULE_CORRECTION_NOTE = (
    "[p5 docket 4] REPAIRED at Phase 5. As written at phase3_synthesis.md:47-53 "
    "this rule (a) carried a carve-out -- 'or with an explicit renewed-deferral "
    "reason that itself survives a Phase-2 Red Team audit' -- that re-admits "
    "precisely the device its sibling (the Iteration-22 aperture-check rule) "
    "forecloses, and which Iteration 23's own deferral already satisfies, so a "
    "tripwire its own triggering event clears; (b) dropped the sibling rule's "
    "'and no further one-cycle extensions via prose' clause; and (c) claimed to "
    "be 'mirroring the aperture-check rule's own wording exactly', which was "
    "false. The carve-out is STRUCK, the dropped clause RESTORED, the false "
    "mirroring claim STRUCK, and VISION's disambiguating sentence added "
    "verbatim. It also existed in three inconsistent renderings "
    "(phase3_synthesis.md full text, a harder one-line form in NOTES.md, and a "
    "contentless pointer in results.json); this key is now the ONE rendering, "
    "and NOTES.md carries it verbatim.")

# [p5 docket 20] Standing rule adopted from ELECTROMAGNETISM, hardened by Red
# Team. Recorded here because the change item 1 makes to stage 16 is exactly
# the class of change it governs -- and the acceptance gate 16b2 added this
# shift IS the independent second derivation it demands.
POST_FREEZE_GATE_TARGET_RULE = (
    "STANDING RULE (Iteration 23 Phase-5 close, docket item 20): a post-freeze "
    "change to a trust-suite gate's TARGET -- as opposed to its bar or its "
    "reporting -- is a physics change and requires an INDEPENDENT SECOND "
    "DERIVATION, from a different route, before it is committed. Shipping one "
    "without that derivation fires Checkpoint criterion 4 automatically at the "
    "next Phase 5 that finds it. Recorded alongside Iteration 19's own warning "
    "that same-shift correction 'should not be read as establishing same-shift "
    "correction is generally safe from criterion 4'. Iteration 23 shipped one "
    "such change (stage-16 gate b's first-light amendment) WITHOUT a second "
    "derivation, and it was wrong; the Phase-5 repoint carries one, wired into "
    "the suite as gate 16b2 so it cannot silently rot.")

# [p5 docket 19] New live thread, for LOGBOOK propagation at close.
ABSORB_SYSTEMATIC_NOTE = (
    "NEW LIVE THREAD (Iteration 23 Phase-5 close, docket item 19): the C_empty "
    "channel carries an uncharacterized absorbing-boundary systematic. Red "
    "Team's own four new FDTD runs move ABSORB 40->60 at two legs: A-v4 "
    "(750nm/38deg/FWHM2) moves by +0.0070 in C -- 1.39x VISION's own C_thr = "
    "0.005 -- closing the gap to the desk propagator from 5.68% to 1.43%; A-v1 "
    "(600nm/40deg/FWHM2) moves by -0.0022, widening the gap from 1.91% to "
    "3.69%, i.e. AWAY from the desk value. Real at both legs, NOT a monotone "
    "convergence. ELECTROMAGNETISM's headline ('the residual is mostly a "
    "boundary artefact, and the desk propagator is better than credited') is "
    "therefore CONFIRMED AT ONE LEG and NOT established as a general "
    "explanation -- recorded as narrowed, not as 'the residual is explained'. "
    "What IS established is a 0.002-0.007 ABSOLUTE systematic (0.4-1.4x the "
    "perceptual threshold the whole T21 contamination question is scored "
    "against) on ABSORB = 40 with SRC_X = 300 and PLANE_X = 77 -- inherited "
    "unexamined by every T21/T16 reading since exp-041, including all 30 Block "
    "MAIN rows T21's fringe mechanism was fitted to and every N9/N17 delta T16 "
    "scores. Structurally the same debt T11 tracks for the box-ledger channel. "
    "Iteration 24 design (Tier-2 item 4): sweep ABSORB with SRC_X moved clear "
    "of the x-damping band so EM's ABSORB=80 confound does not recur, source "
    "span held fixed, all 3 lambda, ~6-9 FDTD runs. NOT re-measured this "
    "shift: the numbers above are Red Team's, cited as its measurement, "
    "because this close is a fix-application shift with no new FDTD budget.")

# ================================================================ Block A desk
C_COEF = 2.0 * math.sqrt(2.0 * math.log(2.0)) / (2.0 * math.pi)   # 0.374781250... [docket 23]
C_THR = 0.005
THETAS = (36, 38, 40)
FWHMS = (2, 5, 10, 20)
LAMS = (450, 600, 750)
FULL_APERTURE = dg.Y_HI - dg.Y_LO                 # 1504 cells
SIGMA_SPONGE = 0.10 / (2 * dg.R_OUT)              # exp-041 design_geometry.py:140-141
OBJ_XY = (dg.OBJ_X, dg.OBJ_Y)                     # sponge-disk centre, exp-041's own OBJ
Y_REL = dg.Y_SRC - dg.OBJ_Y                       # source-cell offsets from the aperture centre
PLATFORM = (f"python {sys.version.split()[0]} / numpy {np.__version__} / "
            f"{sys.platform}")                    # [docket 14] named reference platform


def _wrap(text, width=74):
    """Console wrapping for the long disposition strings [p5 docket 5]."""
    import textwrap
    return textwrap.wrap(text, width)


def _weber_of(profile):
    """The ONLY route from any B(y) profile to any compared number [docket 15].
    `weber` is invariant under a global sign flip of the profile, which is what
    makes analytic (globally negative) and FDTD (positive) readings comparable
    AS SCALARS -- and is exactly why profiles themselves are never compared."""
    bo, bf = amb.window_means(np.asarray(profile), dg.Y_LO, dg.OBJ_Y,
                              dg.R_OUT, dg.GUARD_OUT, dg.W_FLANK)
    return amb.weber(bo, bf)


def w0_cells(lam_cells, fwhm_deg):
    """Diffraction-limited Gaussian waist for a full-angle intensity FWHM."""
    return C_COEF * lam_cells / math.radians(fwhm_deg)


def w_line_cells(lam_cells, fwhm_deg, theta0_deg):
    """The SOURCE `width` argument [docket 1]: to emit divergence Delta-theta
    from a phase-ramped straight aperture you must pass w0/cos(theta0)."""
    return w0_cells(lam_cells, fwhm_deg) / math.cos(math.radians(theta0_deg))


def w_y_cells(lam_cells, fwhm_deg, theta0_deg):
    """Observation-plane 1/e half-width [docket 2] -- unchanged from the
    proposal's own section 2.1, which is exactly EM's, PHOTONICS' and Red
    Team's form once docket item 1 is applied (Attack 1c)."""
    w0 = w0_cells(lam_cells, fwhm_deg)
    c = math.cos(math.radians(theta0_deg))
    z_r = math.pi * w0 ** 2 / lam_cells
    z_eff = dg.D_SP / c
    return w0 * math.sqrt(1.0 + (z_eff / z_r) ** 2) / c


def prop_c_empty(width, theta0_deg, lam_cells, y_center=None):
    """[docket 4] The band-setter: the ACTUAL complex Gaussian aperture pushed
    through exp-042's own committed Huygens-Fresnel propagator in the CORRECTED
    E/H convention (`_G0_for` for E, obliquity-weighted `_G0_for` for H,
    Sx = -Re(E conj(H))), reduced through `lab.ambient`. One line different
    from `dg.field_and_h`: the taper P is replaced by the Gaussian."""
    k = 2.0 * np.pi / lam_cells
    yc = dg.OBJ_Y if y_center is None else y_center
    yy = dg.Y_SRC - yc
    src = np.exp(-((yy / width) ** 2)) * np.exp(1j * k * np.sin(np.radians(theta0_deg)) * yy)
    _, g0 = dg._G0_for(lam_cells)
    e = g0 @ src
    h = (g0 * dg._OBLIQUITY) @ src
    return _weber_of(-np.real(e * np.conj(h)))


def envelope_c_empty(w_y, theta0_deg, y_center=None):
    """The RETAINED closed-form anchor [docket 4] -- reported with its measured
    accuracy, never used to set a band."""
    yc = dg.OBJ_Y if y_center is None else y_center
    y_peak = yc + dg.D_SP * math.tan(math.radians(theta0_deg))
    return _weber_of(np.exp(-2.0 * (dg.Y_OBS - y_peak) ** 2 / w_y ** 2))


def coherent_effective_halfwidth(theta0_deg, fwhm_deg, lam_cells, n=41):
    """[docket 5 / Attack 2] The effective aperture `beam_divergence_coherent`
    actually synthesises: |sum_i sqrt(w_i) exp(i k sin(theta_i) Y)|. Red Team's
    analytic result, re-measured here: its 1/e half-width is w0/cos(theta0).

    Returns (interpolated, grid-quantized) half-widths. The grid-quantized
    number reproduces Red Team's own `block_a_check.py` measurement cell for
    cell; the INTERPOLATED number is what the identity band is set on, because
    the raw integer-grid crossing carries a +/-0.5-cell quantization that is
    2.4% of the width at the narrowest (FWHM=20deg / 450nm) cell -- i.e. the
    quantization, not the identity, dominates Red Team's own quoted spread
    there."""
    k = 2.0 * np.pi / lam_cells
    thetas, w = dg.gaussian_angle_weights(theta0_deg, fwhm_deg, n)
    a = np.zeros(Y_REL.size, dtype=complex)
    for th, wt in zip(thetas, w):
        a = a + np.sqrt(wt) * np.exp(1j * k * np.sin(np.radians(th)) * Y_REL)
    a = np.abs(a)
    a = a / a.max()
    ip = int(np.argmax(a))
    r = ip + int(np.argmax(a[ip:] < 1.0 / math.e))
    y0, y1 = float(Y_REL[r - 1]), float(Y_REL[r])
    a0, a1 = float(a[r - 1]), float(a[r])
    y_int = y0 + (1.0 / math.e - a0) * (y1 - y0) / (a1 - a0)
    return abs(y_int), abs(float(Y_REL[r]))


def beam_divergence_coherent_corrected(theta0_deg, fwhm_deg, lam_cells, n=41):
    """[docket 10] exp-042's `beam_divergence_coherent` re-expressed in the
    CORRECTED E/H convention -- the coherent column that `block_beam_corrected`
    never generated, so A3's comparison can be made at matched convention.
    Structure copied from `dg.beam_divergence_coherent`; only the reduction
    changes (Sx = -Re(E conj(H)) instead of |E|^2)."""
    thetas, w = dg.gaussian_angle_weights(theta0_deg, fwhm_deg, n)
    k, g0 = dg._G0_for(lam_cells)
    e_tot = np.zeros(dg.Y_OBS.size, dtype=complex)
    h_tot = np.zeros(dg.Y_OBS.size, dtype=complex)
    g_h = g0 * dg._OBLIQUITY
    for th, wt in zip(thetas, w):
        amp = np.sqrt(wt) * dg._src_amp(th, k)
        e_tot = e_tot + (g0 @ amp)
        h_tot = h_tot + (g_h @ amp)
    return _weber_of(-np.real(e_tot * np.conj(h_tot)))


def coherent_aperture_lobe_census(theta0_deg, fwhm_deg, lam_cells, n=41):
    """[p5 docket 6] SCOPE the 'permanent T21 fact' before it enters LOGBOOK.

    The identity `w_eff = w0/cos(theta0)` (P-TH23-A3) is a statement about the
    effective aperture's CENTRAL LOBE. Red Team's Attack 2 replaced the
    discrete sum `sum_i sqrt(w_i) exp(i k sin(theta_i) Y)` by an integral --
    a Poisson-summation step, legitimate ONLY when the comb's replicas fall
    outside the aperture. Attack 2 never checked whether they do; QUANTUM did,
    and is right. Measured here, from the same `gaussian_angle_weights` the
    production code uses:

      * angular sample spacing d(theta) = 0.125*FWHM (n=41, half_width 2.5
        FWHM), so replica spacing dY ~ lambda_cells/(cos(theta0)*d(theta_rad));
      * at FWHM=20deg that lands INSIDE the 752-cell aperture half-span, and
        the synthesised object is a three-lobe comb, not a single transverse
        mode.

    Returns per-cell: predicted and measured replica offset, replica
    amplitude, and the intensity fraction outside +-3*w_line with and without
    the real aperture taper P."""
    k = 2.0 * np.pi / lam_cells
    thetas, w = dg.gaussian_angle_weights(theta0_deg, fwhm_deg, n)
    a = np.zeros(Y_REL.size, dtype=complex)
    for th, wt in zip(thetas, w):
        a = a + np.sqrt(wt) * np.exp(1j * k * np.sin(np.radians(th)) * Y_REL)
    inten = np.abs(a) ** 2
    inten_tap = np.abs(a * dg.P) ** 2
    wl = w_line_cells(lam_cells, fwhm_deg, theta0_deg)
    core = np.abs(Y_REL) <= 3.0 * wl
    outside = np.where(~core)[0]
    if outside.size:
        j = int(outside[np.argmax(inten[outside])])
        replica_y, replica_amp = float(Y_REL[j]), float(math.sqrt(inten[j] / inten.max()))
    else:
        replica_y, replica_amp = float("nan"), 0.0
    d_theta_rad = math.radians(0.125 * fwhm_deg)
    return {
        "lambda_cells": lam_cells, "theta0_deg": theta0_deg, "fwhm_deg": fwhm_deg,
        "w_line_cells": wl,
        "angular_sample_spacing_deg": 0.125 * fwhm_deg,
        "replica_spacing_predicted_cells":
            lam_cells / (math.cos(math.radians(theta0_deg)) * d_theta_rad),
        "replica_offset_measured_cells": replica_y,
        "replica_amplitude": replica_amp,
        "intensity_fraction_outside_3w_line_untapered":
            float(inten[~core].sum() / inten.sum()),
        "intensity_fraction_outside_3w_line_tapered":
            float(inten_tap[~core].sum() / inten_tap.sum()),
        "single_transverse_mode": bool(inten[~core].sum() / inten.sum() < 0.01),
    }


def a3_residual_closed_form(theta0_deg, fwhm_deg):
    """[p5 docket 7] QUANTUM's ZERO-FREE-PARAMETER attribution for A3's
    residual, replacing Red Team's own '(taper truncation)' parenthetical
    (which Red Team retracts: at FWHM=20deg `w_line` is 21-35 cells inside a
    752-cell half-aperture, i.e. truncation at 21-36 waists, e^-441, and
    including the taper moves the lobe fraction only 67.1%->66.6%).

        w_meas / w_line = 1 / sqrt(1 - 4 sigma_theta^2 tan^2(theta0))

    It is the second-order term of the sin(theta) expansion about theta0:
    sin(theta0+d) ~ sin(theta0) + cos(theta0)d - sin(theta0)d^2/2, whose
    quadratic part broadens the synthesised Gaussian by exactly this factor.
    sigma_theta = FWHM/2.3548 in radians, matching `gaussian_angle_weights`."""
    sig = math.radians(fwhm_deg) / 2.3548
    u = 4.0 * sig ** 2 * math.tan(math.radians(theta0_deg)) ** 2
    return 100.0 * (1.0 / math.sqrt(1.0 - u) - 1.0)


def a3_residual_cubic_phase(theta0_deg, fwhm_deg, lam_cells, n=41):
    """[p5 docket 7] QUANTUM's accompanying finding: the synthesised mode is
    slightly ABERRATED even in its core. Residual phase over |Y| <= w_line
    after removing the best-fit linear ramp (the pointing term)."""
    k = 2.0 * np.pi / lam_cells
    thetas, w = dg.gaussian_angle_weights(theta0_deg, fwhm_deg, n)
    a = np.zeros(Y_REL.size, dtype=complex)
    for th, wt in zip(thetas, w):
        a = a + np.sqrt(wt) * np.exp(1j * k * np.sin(np.radians(th)) * Y_REL)
    ph = np.unwrap(np.angle(a * np.exp(-1j * k * np.sin(np.radians(theta0_deg)) * Y_REL)))
    wl = w_line_cells(lam_cells, fwhm_deg, theta0_deg)
    sel = np.abs(Y_REL) <= wl
    coef = np.polyfit(Y_REL[sel], ph[sel], 1)
    return float(np.abs(ph[sel] - np.polyval(coef, Y_REL[sel])).max())


def angular_sampling_convergence(theta0_deg, fwhm_deg, lam_cells, n_lo=41, n_hi=401):
    """[p5 docket 8] RESTORE P-TH23-A4's MECHANISM. A4 was dropped at Phase 3
    on the premise 'there is no divergence to explain' -- its 5-20% magnitude
    band was indeed falsified, but the 41-point angular-sampling aliasing it
    named is REAL. `gaussian_angle_weights`'s n=41 has never had a convergence
    check in this program's history, and it is the kernel that produced both
    exp-042 columns Iterations 19-23 have argued over.

    Measured in BOTH conventions: exp-042's own committed one (obliquity on E,
    |E|^2 -- the one that actually produced the disputed columns, and the one
    Red Team's `rt_nconv.py` measured), and this cycle's corrected one."""
    def committed(n):
        k, g = dg._G_for(lam_cells, True)
        e = np.zeros(dg.Y_OBS.size, dtype=complex)
        thetas, w = dg.gaussian_angle_weights(theta0_deg, fwhm_deg, n)
        for th, wt in zip(thetas, w):
            e = e + np.sqrt(wt) * (g @ dg._src_amp(th, k))
        return _weber_of(np.abs(e) ** 2)

    c_lo, c_hi = committed(n_lo), committed(n_hi)
    k_lo = beam_divergence_coherent_corrected(theta0_deg, fwhm_deg, lam_cells, n=n_lo)
    k_hi = beam_divergence_coherent_corrected(theta0_deg, fwhm_deg, lam_cells, n=n_hi)
    return {
        "n_lo": n_lo, "n_hi": n_hi,
        "committed_convention_n_lo": c_lo, "committed_convention_n_hi": c_hi,
        "committed_convention_rel_move_pct": 100.0 * abs(c_lo - c_hi) / abs(c_hi),
        "corrected_convention_n_lo": k_lo, "corrected_convention_n_hi": k_hi,
        "corrected_convention_rel_move_pct": 100.0 * abs(k_lo - k_hi) / abs(k_hi),
    }


def block_a_desk():
    with open(os.path.join(EXP042, "results.json")) as f:
        r042 = json.load(f)
    committed_coherent = {(r["lambda_nm"], r["theta0"], r["fwhm_deg"]): r["C_coherent"]
                          for r in r042["block_beam"]["rows"]}
    corrected_incoherent = {(r["lambda_nm"], r["theta0"], r["fwhm_deg"]): r["C_incoherent"]
                            for r in r042["phase5_erratum"]["block_beam_corrected"]["rows"]}

    cells = []
    for lam_nm in LAMS:
        lam = dg.CPL[lam_nm]
        for th0 in THETAS:
            c = math.cos(math.radians(th0))
            walk = dg.D_SP * math.tan(math.radians(th0))
            for fw in FWHMS:
                w0 = w0_cells(lam, fw)
                wl = w0 / c
                wy = w_y_cells(lam, fw, th0)
                z_eff = dg.D_SP / c
                # aimed leg: aperture recentred so the beam axis lands on OBJ_Y
                y_c_aim = round(dg.OBJ_Y - walk)
                half_span_aim = min(y_c_aim - dg.Y_LO, dg.Y_HI - y_c_aim)
                rim_amp_aim = math.exp(-(half_span_aim / wl) ** 2)
                rim_amp_unaimed = math.exp(-((dg.OBJ_Y - dg.Y_LO) / wl) ** 2)
                c_prop = prop_c_empty(wl, th0, lam)
                c_prop_aim = prop_c_empty(wl, th0, lam, y_center=y_c_aim)
                c_env = envelope_c_empty(wy, th0)
                c_coh_corr = beam_divergence_coherent_corrected(th0, fw, lam)
                cc = committed_coherent[(lam_nm, th0, fw)]
                ci = corrected_incoherent[(lam_nm, th0, fw)]
                eff, eff_grid = coherent_effective_halfwidth(th0, fw, lam)
                lobes = coherent_aperture_lobe_census(th0, fw, lam)      # [p5 docket 6]
                nconv = angular_sampling_convergence(th0, fw, lam)       # [p5 docket 8]
                cells.append({
                    "lambda_nm": lam_nm, "lambda_cells": lam, "theta0_deg": th0,
                    "fwhm_deg": fw, "w0_cells": w0, "w_line_cells": wl,
                    "two_w_line_cells": 2.0 * wl,
                    "aperture_ratio_1504_over_2w_line": FULL_APERTURE / (2.0 * wl),
                    "z_R_line_cells": math.pi * wl ** 2 / lam,
                    "z_R_w0_cells": math.pi * w0 ** 2 / lam,
                    "z_eff_cells": z_eff, "w_y_cells": wy,
                    "N_F": (2.0 * wl) ** 2 / (lam * z_eff),
                    "N_F_superseded_w0_convention": (2.0 * w0) ** 2 / (lam * z_eff),
                    "walk_cells": walk, "w0_over_lambda": w0 / lam,
                    "C_empty_propagator_unaimed": c_prop,
                    "C_empty_propagator_aimed": c_prop_aim,
                    "C_empty_envelope_anchor": c_env,
                    "envelope_vs_propagator_rel_pct": 100.0 * abs(c_env - c_prop) / abs(c_prop),
                    "C_coherent_committed_042_superseded_convention": cc,
                    "C_coherent_corrected_convention_this_cycle": c_coh_corr,
                    "prop_vs_committed_coherent_rel_pct": 100.0 * abs(c_prop - cc) / abs(cc),
                    "prop_vs_corrected_coherent_rel_pct": 100.0 * abs(c_prop - c_coh_corr) / abs(c_coh_corr),
                    "C_incoherent_corrected_042": ci,
                    "prop_over_incoherent_factor": abs(c_prop) / abs(ci),
                    "coherent_sum_effective_halfwidth_cells": eff,
                    "coherent_sum_halfwidth_vs_w_line_rel_pct": 100.0 * (eff - wl) / wl,
                    "coherent_sum_effective_halfwidth_gridquantized_cells": eff_grid,
                    "coherent_sum_halfwidth_gridquantized_vs_w_line_rel_pct":
                        100.0 * (eff_grid - wl) / wl,
                    "aimed_y_center": y_c_aim,
                    "aimed_half_span_over_w_line": half_span_aim / wl,
                    "aimed_rim_amplitude": rim_amp_aim,
                    "aimed_truncation_valid": rim_amp_aim <= 1.0e-2,   # [docket 11]
                    "unaimed_rim_amplitude": rim_amp_unaimed,
                    "unaimed_rim_intensity": rim_amp_unaimed ** 2,
                    # [p5 docket 6] effective-aperture lobe census
                    "effective_aperture_lobe_census": lobes,
                    # [p5 docket 7] A3 residual, closed form and aberration
                    "a3_residual_closed_form_pct": a3_residual_closed_form(th0, fw),
                    "a3_residual_measured_pct": 100.0 * (eff - wl) / wl,
                    "a3_residual_cubic_phase_rad": a3_residual_cubic_phase(th0, fw, lam),
                    # [p5 docket 8] 41-point angular-sampling convergence
                    "angular_sampling_convergence_n41_vs_n401": nconv,
                })

    n_le10 = sum(1 for c in cells if c["fwhm_deg"] <= 10)      # 27 [docket 6]
    n_20 = sum(1 for c in cells if c["fwhm_deg"] == 20)        # 9  [docket 6]
    assert n_le10 == 27 and n_20 == 9, (n_le10, n_20)

    env_dev = [c["envelope_vs_propagator_rel_pct"] for c in cells]
    a1_above_thr = sum(1 for c in cells if abs(c["C_empty_propagator_unaimed"]) > C_THR)
    a1_above_20x = sum(1 for c in cells if c["prop_over_incoherent_factor"] >= 20.0)
    a1_min_abs = min(abs(c["C_empty_propagator_unaimed"]) for c in cells)
    a3_le10 = [abs(c["coherent_sum_halfwidth_vs_w_line_rel_pct"]) for c in cells if c["fwhm_deg"] <= 10]
    a3_20 = [abs(c["coherent_sum_halfwidth_vs_w_line_rel_pct"]) for c in cells if c["fwhm_deg"] == 20]
    a3_le10_grid = [abs(c["coherent_sum_halfwidth_gridquantized_vs_w_line_rel_pct"])
                    for c in cells if c["fwhm_deg"] <= 10]
    a3_20_grid = [abs(c["coherent_sum_halfwidth_gridquantized_vs_w_line_rel_pct"])
                  for c in cells if c["fwhm_deg"] == 20]
    a3_target_le10 = [c["prop_vs_committed_coherent_rel_pct"] for c in cells if c["fwhm_deg"] <= 10]
    a3_target_20 = [c["prop_vs_committed_coherent_rel_pct"] for c in cells if c["fwhm_deg"] == 20]
    a3_matched_le10 = [c["prop_vs_corrected_coherent_rel_pct"] for c in cells if c["fwhm_deg"] <= 10]
    a3_matched_20 = [c["prop_vs_corrected_coherent_rel_pct"] for c in cells if c["fwhm_deg"] == 20]

    # ---- [p5 docket 6] lobe-census aggregates: WHERE the single-mode reading holds
    lob20 = [c["effective_aperture_lobe_census"] for c in cells if c["fwhm_deg"] == 20]
    lob_le10 = [c["effective_aperture_lobe_census"] for c in cells if c["fwhm_deg"] <= 10]
    frac20 = [l["intensity_fraction_outside_3w_line_untapered"] for l in lob20]
    frac20_tap = [l["intensity_fraction_outside_3w_line_tapered"] for l in lob20]
    frac_le10 = [l["intensity_fraction_outside_3w_line_untapered"] for l in lob_le10]
    # ---- [p5 docket 7] closed-form vs measured A3 residual
    a3_cf_pairs = [(c["a3_residual_closed_form_pct"], abs(c["a3_residual_measured_pct"]))
                   for c in cells]
    a3_cf_err = [abs(p - m) for p, m in a3_cf_pairs]
    cubic = {str(fw): max(c["a3_residual_cubic_phase_rad"] for c in cells if c["fwhm_deg"] == fw)
             for fw in FWHMS}
    # ---- [p5 docket 8] angular-sampling convergence aggregates
    nconv_all = [c["angular_sampling_convergence_n41_vs_n401"] for c in cells]
    nconv_worst = max(n["committed_convention_rel_move_pct"] for n in nconv_all)
    nconv_worst_cell = max(cells, key=lambda c: c["angular_sampling_convergence_n41_vs_n401"]
                           ["committed_convention_rel_move_pct"])
    nconv_worst_corr = max(n["corrected_convention_rel_move_pct"] for n in nconv_all)
    # ---- [p5 docket 10] the reading IS strongly chromatic: count positive-C cells
    pos_c = [{"lambda_nm": c["lambda_nm"], "theta0_deg": c["theta0_deg"],
              "fwhm_deg": c["fwhm_deg"], "C": c["C_empty_propagator_unaimed"]}
             for c in cells if c["C_empty_propagator_unaimed"] > 0.0]
    sign_reversal_rows = []
    for th0 in THETAS:
        for fw in FWHMS:
            row = {c["lambda_nm"]: c["C_empty_propagator_unaimed"]
                   for c in cells if c["theta0_deg"] == th0 and c["fwhm_deg"] == fw}
            signs = {1 if v > 0 else -1 for v in row.values()}
            if len(signs) > 1:
                sign_reversal_rows.append({"theta0_deg": th0, "fwhm_deg": fw, "C_by_lambda_nm": row})

    th40 = [c for c in cells if c["theta0_deg"] == 40]
    ratios40 = [c["aperture_ratio_1504_over_2w_line"] for c in th40]
    nf40 = [c["N_F"] for c in th40]
    nf_all = [c["N_F"] for c in cells]

    # FDTD leg specification [docket 1: every oblique width is w0/cos(theta0)]
    legs = [
        {"id": "S16-a", "n": 1, "lambda_nm": 600, "theta0_deg": 0.0, "profile": "gauss",
         "width": 40.0, "purpose": "Gaussian free-space divergence identity: 1/e^2 "
         "half-width at 3 planes vs w0*sqrt(1+(z/z_R)^2), z_R = pi*40^2/20 = "
         f"{math.pi*40**2/20:.4f} cells; gate <=3%", "gate": "S16-a"},
        {"id": "S16-b", "n": 2, "lambda_nm": 600, "theta0_deg": 40.0, "profile": "gauss",
         "width": 40.0, "purpose": "pointing identity: beam centre at PLANE_X = y_c + "
         f"D_SP*tan40 = {dg.OBJ_Y + dg.D_SP*math.tan(math.radians(40)):.2f} +/- 2 cells",
         "gate": "S16-b"},
        {"id": "S16-c", "n": 3, "lambda_nm": 600, "theta0_deg": 40.0, "profile": "plane",
         "width": None, "purpose": "ABSOLUTE regression anchor: reproduce exp-041 Block "
         "MAIN's committed C_empty(+40deg,600nm) = -0.010964794540566314 "
         "[docket 14: relative tolerance, platform named]", "gate": "S16-c"},
        {"id": "A-v1", "n": 4, "lambda_nm": 600, "theta0_deg": 40.0, "profile": "gauss",
         "width": w_line_cells(20, 2, 40), "purpose": "propagator validation", "gate": None},
        {"id": "A-v2", "n": 5, "lambda_nm": 600, "theta0_deg": 40.0, "profile": "gauss",
         "width": w_line_cells(20, 10, 40), "purpose": "propagator validation; ALSO carries "
         "the new stage-16 oblique-width gate [docket 13]", "gate": "S16-d"},
        {"id": "A-v3", "n": 6, "lambda_nm": 600, "theta0_deg": 40.0, "profile": "gauss",
         "width": w_line_cells(20, 20, 40), "purpose": "propagator validation (far-field "
         "transition)", "gate": None},
        {"id": "A-v4", "n": 7, "lambda_nm": 750, "theta0_deg": 38.0, "profile": "gauss",
         "width": w_line_cells(25, 2, 38), "purpose": "exp-042's own worst corrected-"
         "convention incoherent cell (C = -0.004006)", "gate": None},
        {"id": "A-o1", "n": 8, "lambda_nm": 600, "theta0_deg": 40.0, "profile": "gauss",
         "width": w_line_cells(20, 10, 40), "sigma": SIGMA_SPONGE,
         "purpose": "object-present pair for leg 5 -- EXPLORATORY-NON-SCORING [docket 9]",
         "gate": None},
        {"id": "A-o2", "n": 9, "lambda_nm": 600, "theta0_deg": 40.0, "profile": "gauss",
         "width": w_line_cells(20, 20, 40), "sigma": SIGMA_SPONGE,
         "purpose": "object-present pair for leg 6 -- EXPLORATORY-NON-SCORING [docket 9]",
         "gate": None},
    ]
    for leg in legs:
        if leg["profile"] == "gauss" and leg["theta0_deg"]:
            lam = dg.CPL[leg["lambda_nm"]]
            c = math.cos(math.radians(leg["theta0_deg"]))
            z_eff = dg.D_SP / c
            leg["N_F"] = (2.0 * leg["width"]) ** 2 / (lam * z_eff)
            if leg["id"].startswith("A-v"):     # empty-scene propagator-validation legs only
                leg["predicted_C_empty_propagator"] = prop_c_empty(
                    leg["width"], leg["theta0_deg"], lam)
                leg["fdtd_vs_propagator_band_pct"] = 35.0 if leg["N_F"] < 1.0 else 15.0

    fwhm_from_width = {}
    for leg in legs:
        if leg["id"].startswith("A-v"):
            lam = dg.CPL[leg["lambda_nm"]]
            fwhm_from_width[leg["id"]] = math.degrees(
                C_COEF * lam / (leg["width"] * math.cos(math.radians(leg["theta0_deg"]))))

    s16d_target = w_y_cells(20, 10, 40)

    return {
        "convention_note": (
            "Every oblique source width is w0/cos(theta0) [docket 1]; the "
            "observation-plane width w_y = w0*sqrt(1+(z_eff/z_R)^2)/cos(theta0) is "
            "UNCHANGED [docket 2]. Every band below is set by the numerical desk "
            "propagation of the actual complex aperture through exp-042's own "
            "committed propagator [docket 4]; the closed-form envelope is an "
            "accuracy anchor only."),
        "sign_convention_guard": (
            "exp-042's analytic B(y) is globally negative (Sx = -Re(E conj(H)), "
            "042/design_geometry.py:274); lab.ambient.observer_profile is positive. "
            "weber() is invariant under a global sign flip of B, so only "
            "weber-reduced SCALARS are compared here -- never B(y) profiles, never "
            "a ratio of two Bs, never analytic B inside incoherent_sum beside an "
            "FDTD B [docket 15]."),
        "C_coefficient": C_COEF,
        "C_THR": C_THR, "C_THR_comment_verbatim": C_THR_COMMENT,
        "full_aperture_cells": FULL_APERTURE,
        "n_cells": len(cells), "n_fwhm_le_10": n_le10, "n_fwhm_eq_20": n_20,
        "cells": cells,
        "geometry_table_theta40": [
            {k: c[k] for k in ("lambda_nm", "fwhm_deg", "w0_cells", "w_line_cells",
                               "two_w_line_cells", "aperture_ratio_1504_over_2w_line",
                               "z_R_line_cells", "w_y_cells", "N_F",
                               "N_F_superseded_w0_convention")}
            for c in th40],
        "aperture_ratio_span_theta40": [min(ratios40), max(ratios40)],
        "N_F_span_theta40": [min(nf40), max(nf40)],
        "N_F_span_all_cells": [min(nf_all), max(nf_all)],
        "t21_3x_30x_citation_restated": (
            f"LOGBOOK.md:1045's T21 '3-30x smaller' citation is restated against the "
            f"corrected span: at theta0=40deg the aperture narrowing is "
            f"{min(ratios40):.2f}x-{max(ratios40):.2f}x, so 2.15x now sits FURTHER "
            f"outside 3x at the low end than the Phase-1 table's own 2.80x [docket 3]."),
        "w_y_slip_correction": {
            "cell": "450nm / FWHM 2deg / theta0=40deg",
            "phase1_printed": 199.33, "corrected": w_y_cells(15, 2, 40),
            "diagnosis": "199.33 is that formula's theta0=36deg value "
                         f"({w_y_cells(15, 2, 36):.2f}) in a theta0=40deg column [docket 2]."},
        "envelope_anchor_accuracy": {
            "envelope_vs_propagator_rel_pct_max": max(env_dev),
            "envelope_vs_propagator_rel_pct_median": float(np.median(env_dev)),
            "n_le_5pct": sum(1 for v in env_dev if v <= 5.0),
            "n_gt_10pct": sum(1 for v in env_dev if v > 10.0),
            "per_fwhm_worst": {str(fw): max(c["envelope_vs_propagator_rel_pct"]
                                            for c in cells if c["fwhm_deg"] == fw)
                               for fw in FWHMS},
            "note": ("Retained as a DISCLOSED anchor only [docket 4]. Red Team's "
                     "independently measured width accuracy: <=0.15% (FWHM<=5deg) / "
                     "<=3.1% (FWHM=20deg) vs exact angular spectrum, <=1.3% vs FDTD.")},
        # ================================================ [p5 docket 6]
        "t21_permanent_fact_scope": {
            "claim_as_scoped": (
                "The identity w_eff = w0/cos(theta0) is a statement about the effective "
                "aperture's CENTRAL LOBE, and holds without qualification at the 27 "
                "FWHM<=10deg cells. It must NOT enter LOGBOOK unqualified [p5 docket 6]."),
            "grating_lobe_finding": (
                "At all 9 FWHM=20deg cells `beam_divergence_coherent` synthesises a "
                "THREE-LOBE COMB, not a single transverse mode: the n=41 angular sampling "
                "(d(theta) = 0.125*FWHM) puts replicas INSIDE the 752-cell aperture "
                "half-span. Measured here; QUANTUM's numbers reproduced, and this corrects "
                "Red Team's own Attack 2, which replaced the discrete sum by an integral "
                "(a Poisson-summation step) without checking whether the replicas fall "
                "outside the aperture."),
            "fwhm20_replica_offset_cells": [min(l["replica_offset_measured_cells"] for l in lob20),
                                            max(l["replica_offset_measured_cells"] for l in lob20)],
            "fwhm20_replica_amplitude": [min(l["replica_amplitude"] for l in lob20),
                                         max(l["replica_amplitude"] for l in lob20)],
            "fwhm20_intensity_fraction_outside_3w_line_untapered_pct":
                [100.0 * min(frac20), 100.0 * max(frac20)],
            "fwhm20_intensity_fraction_outside_3w_line_tapered_pct":
                [100.0 * min(frac20_tap), 100.0 * max(frac20_tap)],
            "fwhm_le10_intensity_fraction_outside_3w_line_pct_max": 100.0 * max(frac_le10),
            "n_cells_single_transverse_mode": sum(
                1 for c in cells if c["effective_aperture_lobe_census"]["single_transverse_mode"]),
            "single_transverse_mode_criterion":
                "<1% of the effective aperture's intensity outside +-3*w_line",
            "refinement_of_red_teams_own_table": (
                "DISCLOSED, not smoothed: Red Team's section-2.1 table gives '<=0.06 "
                "replica amplitude / <=0.1% outside' for the whole FWHM<=10deg class. "
                "Measured here that holds at 24 of the 27 cells but NOT at the three "
                "450nm/FWHM=10deg cells, where the predicted replica spacing (850-898 "
                "cells) sits just OUTSIDE the 752-cell aperture half-span and the "
                "replica's rising SHOULDER reaches the rim: amplitude 0.059/0.107/0.177 "
                "and 0.14%/0.51%/1.59% of intensity outside +-3*w_line at theta0 = "
                "40/38/36deg. This sharpens the scoping rather than contradicting it -- "
                "the comb is fully inside the aperture only at FWHM=20deg -- and it is "
                "why the single-transverse-mode count below is 26/36, not 27/36."),
            "what_is_and_is_not_falsified": (
                "The A3 MEASUREMENT (a local 1/e half-width around the peak) is NOT "
                "falsified -- the central lobe really does have half-width w0/cos(theta0). "
                "What IS falsified is the INTERPRETATION that the coherent column already "
                "IS the diffraction-limited single transverse mode: it is not, at 9 of 36 "
                "cells, where the w0/cos(theta0) Gaussian carries only ~32-58% of the "
                "energy."),
        },
        # ================================================ [p5 docket 18]
        "quantum_iteration20_conjecture_disposition": {
            "supersedes": ("NOTES.md 'What Block A actually established' item 3 and "
                           "phase3_synthesis.md, which both record the conjecture as "
                           "'mis-posed, not refuted or confirmed'. Red Team's Phase-5 "
                           "ruling, three lines, adopted verbatim [p5 docket 18]. "
                           "'Mis-posed' is over-charitable AND over-broad; QUANTUM's own "
                           "request to record it simply REFUTED is harder on QUANTUM's "
                           "seat than the evidence supports."),
            "premise": ("exp-042's coherent column holds the full ~75-lambda aperture "
                        "fixed -- beamforming, not natural divergence: REFUTED at the 27 "
                        "FWHM<=10deg cells; PARTIALLY VINDICATED at the 9 FWHM=20deg "
                        "cells, where the measured replicas do substantially occupy the "
                        "aperture -- directionally what the original premise claimed."),
            "prediction": ("'lands much closer to the incoherent reading': REFUTED at all "
                           "36 cells, at the desk (36/36 above C_THR, 35/36 at >=20x "
                           "incoherent, min|C| = 0.03227)."),
            "mis_posed_belongs_to": ("P-TH23-A1 AS A SCORED METRIC (Attack 7's pointing "
                                     "tautology) and nowhere else."),
        },
        # ================================================ [p5 docket 8]
        "angular_sampling_convergence": {
            "statement": (
                "P-TH23-A4's MECHANISM is restored as real. A4 was dropped correctly on "
                "its 5-20% magnitude band and INCORRECTLY on its premise: 41-point angular "
                "sampling aliasing exists and moves the scored C_empty. "
                "`gaussian_angle_weights(n=41)` has NEVER had a convergence check in this "
                "program's history, and it is the kernel that produced both exp-042 columns "
                "Iterations 19-23 have argued over. NEW OPEN ITEM for Iteration 24 "
                "(Tier-2 priority 3: the convergence audit runs before the M^2/etendue "
                "bridge, because that family interpolates THROUGH the FWHM=20deg regime "
                "where the comb is worst)."),
            "worst_rel_move_committed_convention_pct": nconv_worst,
            "worst_cell_committed_convention": {
                k: nconv_worst_cell[k] for k in ("lambda_nm", "theta0_deg", "fwhm_deg")},
            "worst_rel_move_corrected_convention_pct": nconv_worst_corr,
            "n_cells_above_1pct_committed": sum(
                1 for n in nconv_all if n["committed_convention_rel_move_pct"] > 1.0),
            "n_cells_above_0p16pct_committed": sum(
                1 for n in nconv_all if n["committed_convention_rel_move_pct"] > 0.16),
        },
        "idealization_2_restated": {
            "w0_over_lambda_all_cells": sorted({round(c["w0_over_lambda"], 6) for c in cells}),
            "w0_over_lambda_at_fwhm20": w0_cells(20, 20) / 20.0,
            "statement": ("w0/lambda = C/Delta-theta is LAMBDA-INDEPENDENT: the FWHM=20deg "
                          "waist is 1.0737*lambda at all three wavelengths, one value, not "
                          "1.07-1.34 [docket 12]. CORRECTED AT PHASE 5 [p5 docket 10]: the "
                          "'consequently ... NO material wavelength dependence' clause was "
                          "WRONG and is struck. The medium is dispersionless and the emitter "
                          "lambda-scale-invariant -- that part is true -- but N_F is "
                          "proportional to lambda_cells and the READING is strongly "
                          "chromatic. See `chromatic_dependence_corrected`."),
            "chromatic_dependence_corrected": {
                "n_cells_positive_C": len(pos_c),
                "n_of": len(cells),
                "positive_C_cells": pos_c,
                "sign_reversal_rows_across_the_visible_band": sign_reversal_rows,
                "note": ("A positive C is a GLINT at the object window, the opposite sign "
                         "to the mechanism A1's own statement asserts. The |C| > C_THR band "
                         "is blind to it because it takes an absolute value. Given T7's "
                         "chromatic-silhouette finding and T21's worst cell having been "
                         "750nm since Iteration 19, this is not a cosmetic wording issue. "
                         "R3's own meta-rule applies: a resolution check on these cells is "
                         "queued for Iteration 24 BEFORE 'glint at 750nm' is allowed into "
                         "the record as physics."),
                "contradicts_A1_mechanism_sentence": (
                    "P-TH23-A1's committed mechanism sentence ('C -> -1 regardless of "
                    "coherence') is contradicted at exactly these cells. Flagged, not "
                    "rewritten (T10 convention) -- A1's own statement string is left as "
                    "committed and carries a `phase5_flag` pointing here."),
            }},
        "idealization_4_restated": {
            "unaimed_rim_amplitude_max": max(c["unaimed_rim_amplitude"] for c in cells),
            "unaimed_rim_intensity_max": max(c["unaimed_rim_intensity"] for c in cells),
            "aimed_half_span_over_w_line_min": min(c["aimed_half_span_over_w_line"] for c in cells),
            "aimed_half_span_over_w_line_range_fwhm2_cells": [
                min(c["aimed_half_span_over_w_line"] for c in cells if c["fwhm_deg"] == 2),
                max(c["aimed_half_span_over_w_line"] for c in cells if c["fwhm_deg"] == 2)],
            "aimed_rim_amplitude_max": max(c["aimed_rim_amplitude"] for c in cells),
            "n_aimed_cells_truncation_invalid": sum(1 for c in cells if not c["aimed_truncation_valid"]),
            "statement": ("Under the corrected width the unaimed rim residual is "
                          "~1e-2 in amplitude / ~1e-4 in intensity -- WITHOUT the "
                          "four-orders margin the Phase-1 idealization claimed. The aimed "
                          "leg truncates at 1.61-2.96 w_line with rim amplitude up to "
                          "7.4e-2; cells with rim amplitude > 1e-2 are flagged "
                          "truncation-INVALID and are excluded from every aimed-leg summary "
                          "rather than the whole aimed leg being dropped [docket 11]. "
                          "CORRECTED AT PHASE 5 [p5 docket 11]: the phrase 'still below "
                          "C_THR=0.005' was an amplitude-vs-intensity confusion AND a "
                          "category error. The unaimed rim AMPLITUDE (9.99e-3) is ABOVE "
                          "C_THR = 0.005, not below it; only the INTENSITY (9.98e-5) is "
                          "below. And comparing a source-plane FIELD RESIDUAL to a Weber "
                          "CONTRAST threshold is a category error in either direction -- "
                          "they are not the same kind of quantity, so neither comparison "
                          "licenses a conclusion. The truncation numbers stand; the "
                          "C_THR comparison is withdrawn."),
            "c_thr_comparison_withdrawn": {
                "unaimed_rim_amplitude_vs_C_THR": "ABOVE (9.99e-3 > 5e-3)",
                "unaimed_rim_intensity_vs_C_THR": "below (9.98e-5 < 5e-3)",
                "ruling": ("Neither comparison is meaningful: a source-plane field residual "
                           "is not a Weber contrast. VISION's V4 is upheld -- the Phase-2 "
                           "docket's own re-authored sentence recreated at idealization 4 "
                           "exactly the defect the same docket fixed at A1."),
                "C_THR_comment_verbatim": C_THR_COMMENT}},
        "predictions": {
            "P-TH23-A0": {
                "class": "DESK-IDENTITY",
                "statement": "w0 = 0.374781250*lambda_cells/Delta-theta_rad reproduces the "
                             "corrected table; aperture ratio at theta0=40deg in [2.14, 35.8] "
                             "(Red Team's audit rounds the low end to 2.15x; the computed "
                             "value is 2.1462x)",
                "band": [2.14, 35.8], "measured": [min(ratios40), max(ratios40)],
                "C_coefficient_9sf": round(C_COEF, 9)},
            "P-TH23-A1": {
                "class": "DESK-POINTING-READING (re-scoped, NOT a coherence adjudication) [docket 5]",
                "statement": ("The aperture-consistent single-mode reading is dominated by "
                              "WHERE THE BEAM POINTS: the object window sits in the beam's "
                              "exponential wing while the +flank window sits under the beam, "
                              "so C -> -1 regardless of coherence. Reported as a pointing/"
                              "estimator reading. C_THR is carried with its own source "
                              f"comment verbatim: '{C_THR_COMMENT}'."),
                "n_above_C_THR": a1_above_thr, "n_of": 36,
                "n_at_or_above_20x_incoherent": a1_above_20x,
                "min_abs_C": a1_min_abs,
                "band": "36/36 above C_THR; >=35/36 at or above 20x the corrected-convention "
                        "incoherent reading; min|C| >= 0.03",
                # ------------------------------------------- [p5 docket 5]
                # The Director's Phase-4 withholding judgment existed in ONE prose
                # paragraph (`block_a_fdtd.gate_disposition`) and nowhere in the
                # record a future cycle actually cites -- `withheld` appeared 0
                # times in the 3.21 MB results.json, and this dict read as an
                # unqualified, fully-compliance-audited pass. Propagated here.
                "gate_backing": (
                    "NOT GATE-BACKED AS PRE-REGISTERED -- S16-b (pointing) FAILED against "
                    "the committed ray-optics target; this is an estimator reading, not a "
                    "validated measurement; P-TH23-A6's withholding clause applied in "
                    "scope, see block_a_fdtd.gate_disposition. SUPERSEDED IN THE SAME "
                    "CLOSE by p5 docket items 1-2: the S16-b failure is now attributed "
                    "96.8% to the gate's own target and 3.2% to the engine, and the "
                    "repointed suite gate (lab/validation/run_all.py stage 16b, "
                    "line-current/flux comparator, bar <=1.5%) PASSES at 0.46% -- 0.418 "
                    "cells of pointing error on a 90.99-cell half-width, cross-validated "
                    "against an independent real-space Huygens derivation to 0.030 cells. "
                    "The pointing chain IS therefore validated at 600nm/40deg, and A1 is "
                    "restored as an explicitly-labelled DESK GEOMETRY READING that is now "
                    "gate-backed at that configuration. It remains NOT an experimental "
                    "adjudication of coherence, and it is NOT counted as a CONFIRMED "
                    "prediction: see `phase5_erratum.a1_disposition` for the final "
                    "scorecard placement."),
                "phase5_flag": (
                    "[p5 docket 10] The mechanism sentence above ('C -> -1 regardless of "
                    "coherence') is CONTRADICTED at the 4 of 36 cells that read POSITIVE "
                    "C (all FWHM=2deg, 600/750nm), a sign reversal across the visible "
                    "band. Flagged, not rewritten (T10). See "
                    "idealization_2_restated.chromatic_dependence_corrected.")},
            "P-TH23-A2": {
                "class": "DESK (re-banded from the numerical propagation) [docket 8]",
                "statement": "Closed-form envelope anchor vs the numerically propagated reading",
                "n_le_5pct": sum(1 for v in env_dev if v <= 5.0),
                "n_gt_10pct": sum(1 for v in env_dev if v > 10.0),
                "worst_pct": max(env_dev), "median_pct": float(np.median(env_dev)),
                "band": "<=5% at >=26/36 and <=15% at 36/36 (the Phase-1 >=30/36 clause is "
                        "retired: it fails at 26/36 under the corrected convention)"},
            "P-TH23-A3": {
                "class": "DESK-VERIFIABLE IDENTITY CHECK (re-scoped) [docket 5, 10]",
                "statement": ("exp-042's `beam_divergence_coherent` ALREADY synthesises a "
                              "Gaussian aperture of 1/e half-width w0/cos(theta0) -- so the "
                              "'aperture-consistent reading lands on the coherent column' is "
                              "an algebraic identity of that function, not an experimental "
                              "result. Measured here as an identity check with a numeric "
                              "tolerance."),
                "effective_halfwidth_vs_w_line_pct_fwhm_le10": [min(a3_le10), max(a3_le10)],
                "effective_halfwidth_vs_w_line_pct_fwhm_20": [min(a3_20), max(a3_20)],
                "gridquantized_vs_w_line_pct_fwhm_le10": [min(a3_le10_grid), max(a3_le10_grid)],
                "gridquantized_vs_w_line_pct_fwhm_20": [min(a3_20_grid), max(a3_20_grid)],
                "band": "interpolated crossing: <=1% at all 27 FWHM<=10deg cells and "
                        "<=4% at all 9 FWHM=20deg cells (residual explained by QUANTUM's "
                        "closed form w_meas/w_line = 1/sqrt(1 - 4 sigma_theta^2 "
                        "tan^2(theta0)), zero free parameters -- NOT taper truncation, "
                        "which is refuted [p5 docket 7]). Grid-quantized "
                        "crossing reported alongside because it reproduces Red Team's own "
                        "measurement cell-for-cell",
                # --------------------------------------------- [p5 docket 7]
                "residual_attribution": {
                    "closed_form": "w_meas/w_line = 1/sqrt(1 - 4*sigma_theta^2*tan^2(theta0))",
                    "origin": ("second-order term of the sin(theta) expansion about theta0; "
                               "sigma_theta = FWHM/2.3548 in radians, matching "
                               "`gaussian_angle_weights`. Zero free parameters, no fit."),
                    "predicted_vs_measured_pct_worst_abs_error": max(a3_cf_err),
                    "predicted_pct_at_fwhm10_theta40": a3_residual_closed_form(40, 10),
                    "predicted_pct_at_fwhm20_theta40": a3_residual_closed_form(40, 20),
                    "superseded_attribution": (
                        "'(taper truncation)' -- Red Team's own Phase-2 parenthetical, "
                        "committed twice, and RETRACTED by Red Team at Phase 5. It cannot "
                        "be right: at FWHM=20deg w_line is 21-35 cells inside a 752-cell "
                        "half-aperture, i.e. truncation at 21-36 waists (e^-441), and "
                        "including the real taper moves the effective-aperture lobe "
                        "fraction only 67.1% -> 66.6%."),
                    "residual_cubic_phase_rad_max_by_fwhm": cubic,
                    "aberration_note": ("QUANTUM's accompanying finding: the synthesised "
                                        "mode is slightly ABERRATED even in its core -- "
                                        "residual phase after removing the linear pointing "
                                        "ramp, over |Y| <= w_line."),
                },
                "quantization_note": (
                    "Red Team's audit prose quotes 0.07-1.3% (FWHM<=10) / 3.5-5.7% "
                    "(FWHM=20) for this identity. Re-running their own script here "
                    "reproduces 0.07-2.98% / 3.45-7.64% -- their prose understated the "
                    "upper end of the spread they measured. The excess is integer-grid "
                    "crossing quantization (+/-0.5 cell = 2.4% of the width at the "
                    "narrowest cell), not a failure of the identity: with the crossing "
                    "interpolated the FWHM<=10 spread collapses. Disclosed rather than "
                    "quietly re-quoting the audit's own range."),
                "target_convention_mismatch_disclosure": (
                    "exp-042's committed `C_coherent` exists ONLY under the superseded "
                    "obliquity-on-E recipe; `phase5_erratum.block_beam_corrected` carries no "
                    "coherent column at all (verified). A corrected-convention coherent column "
                    "is therefore GENERATED here so the comparison is made at matched "
                    "convention; both comparisons are reported [docket 10]."),
                "prop_vs_committed_coherent_n_gt_3pct_fwhm_le10": sum(1 for v in a3_target_le10 if v > 3.0),
                "prop_vs_committed_coherent_worst_fwhm_le10": max(a3_target_le10),
                "prop_vs_committed_coherent_fwhm20_range": [min(a3_target_20), max(a3_target_20)],
                "prop_vs_CORRECTED_coherent_n_gt_3pct_fwhm_le10": sum(1 for v in a3_matched_le10 if v > 3.0),
                "prop_vs_CORRECTED_coherent_worst": max(a3_matched_le10 + a3_matched_20),
                "phase1_fwhm20_clause_status": (
                    "DROPPED [docket 7]: the Phase-1 '5-20% divergence at FWHM=20' clause "
                    "hard-falsifies pre-run under the corrected width (measured 0.1-2.5%)."),
            },
            "P-TH23-A4": {
                "class": "DROPPED [docket 7] -- MECHANISM RESTORED AS REAL [p5 docket 8]",
                "statement": ("Premise false under the corrected width: there is no "
                              "large FWHM=20deg divergence to explain as 41-point "
                              "angular aliasing. CORRECTED AT PHASE 5 [p5 docket 8]: A4 "
                              "was dropped CORRECTLY on its 5-20% magnitude band and "
                              "INCORRECTLY on that premise. The 41-point angular-sampling "
                              "aliasing it named is real and measurable -- n=41 -> n=401 "
                              "moves the scored C_empty by up to the figure recorded in "
                              "`block_a_aperture_consistent_beam.angular_sampling_"
                              "convergence` (Red Team measured 4.473% at "
                              "450nm/36deg/FWHM=20deg; QUANTUM measured 3.18% under a "
                              "different reduction). The drop stands as a SCORING "
                              "decision; the mechanism is restored to the record and is a "
                              "new open item for Iteration 24."),
                "magnitude_band_status": "FALSIFIED (5-20% claimed; measured well below)",
                "mechanism_status": "REAL, magnitude-corrected",
                "never_convergence_checked": (
                    "`gaussian_angle_weights`'s n=41 has never had a convergence check in "
                    "this program's history until this shift.")},
            "P-TH23-A5": {
                "class": "FDTD-SCORED (the cycle's genuine falsifiable Block-A content)",
                "statement": "FDTD reproduces the desk propagator's C_empty at the new "
                             "Fresnel numbers",
                "band": "<=15% relative at legs A-v1/A-v2/A-v4 (N_F = "
                        + ", ".join(f"{leg['N_F']:.2f}" for leg in legs if leg["id"] in ("A-v1", "A-v2", "A-v4"))
                        + "), <=35% at A-v3 (N_F = "
                        + f"{[leg['N_F'] for leg in legs if leg['id'] == 'A-v3'][0]:.2f}"
                        + "); sign agreement 4/4",
                "predicted_C_empty": {leg["id"]: leg["predicted_C_empty_propagator"]
                                      for leg in legs if leg["id"].startswith("A-v")}},
            "P-TH23-A6": {
                "class": "FDTD-SCORED (trust-suite gates; if any fails, no Block-A number is "
                         "reported as trusted)",
                "band": {
                    "S16-a": "1/e^2 half-width vs w0*sqrt(1+(z/z_R)^2) at 3 planes, <=3%",
                    "S16-b": f"beam centre at PLANE_X within +/-2 cells of "
                             f"{dg.OBJ_Y + dg.D_SP*math.tan(math.radians(40)):.2f}",
                    "S16-c": ("reproduces -0.010964794540566314 to <=1e-12 RELATIVE on the "
                              f"named reference platform ({PLATFORM}) [docket 14]"),
                    "S16-d": (f"NEW oblique-width gate [docket 13]: 600nm/theta0=40deg/"
                              f"width=56.063 -> 1/e^2 half-width {s16d_target:.2f} cells, "
                              f"<=5% (Red Team's own FDTD run of this exact configuration "
                              f"measured 80.47, i.e. 1.3% high)")},
                "s16d_target_cells": s16d_target},
            "P-TH23-A7": {"class": "DROPPED [docket 9]",
                          "statement": "The ratio estimator C_corr = (1+C_scene)/(1+C_empty)-1 "
                                       "is ill-conditioned by 77-300x at these C_empty values "
                                       "(-0.997/-0.987), so it cannot carry a scored band. The "
                                       "two object-present legs are still run and reported as "
                                       "EXPLORATORY-NON-SCORING context."},
        },
        "fdtd_legs": legs,
        "fdtd_leg_effective_fwhm_deg": fwhm_from_width,
        "n_new_fdtd_calls_planned": len(legs),
        "platform": PLATFORM,
    }


# ================================================================ Block B desk
DX_M = 30.0e-9
R_OUT_CELLS = 78
SIGMA_EXT_ON, RATIO_ON = 235.96673494878587, 0.6074830175566805
NETD_BAND_K = (0.020, 0.050)
EMISSIVITY, H_CONV_OLD, MASS_KG_OLD, C_P_OLD = 0.9, 5.0, 1.0e-15, 700.0
T_AMBIENT_K = 293.15
K_AIR_W_MK = 0.026
DENSITY_SI_KG_M3, C_P_SI, K_SI_W_MK = 2330.0, 700.0, 148.0
LAMBDA_AIR_M = 65.7e-9
DWELL_S = 10.0 / 150.0


def _irradiance_w_cm2(candela, efficacy_lm_w, distance_m):
    return (candela / distance_m ** 2) / efficacy_lm_w / 1.0e4


def block_b_desk():
    irr_central = _irradiance_w_cm2(40000.0, 300.0, 45.0)
    on_central = ts.absorbed_power_established_ratio(irr_central, SIGMA_EXT_ON, DX_M, RATIO_ON)
    dt_ss_full_old = ts.steady_state_delta_T(on_central["p_abs_w"], on_central["area_m2"],
                                             EMISSIVITY, H_CONV_OLD, T_AMBIENT_K)
    dp_dt_old = on_central["area_m2"] * (4.0 * EMISSIVITY * ts.SIGMA_SB * T_AMBIENT_K ** 3 + H_CONV_OLD)
    tau_thermal_s_old = MASS_KG_OLD * C_P_OLD / dp_dt_old

    r_out_m = R_OUT_CELLS * DX_M
    w_on_m = SIGMA_EXT_ON * DX_M

    def self_consistent_regime(length_power_m, length_cond_m, name):
        """exp-045's own `self_consistent_regime` idiom, extended to take
        SEPARATE power and conduction lengths (Phase-1 section 2.3's own spec).
        The two committed exp-045 regimes are recovered exactly by passing the
        same value twice. exp-045's fix-7 cross-consistency assertion is
        STRENGTHENED, not weakened: h_eff and mass/area must both come from
        length_cond, and p_abs from length_power alone."""
        h_eff = K_AIR_W_MK / length_cond_m
        area_m2 = length_cond_m ** 2
        mass_kg = DENSITY_SI_KG_M3 * length_cond_m ** 3
        dp_dt = area_m2 * (4.0 * EMISSIVITY * ts.SIGMA_SB * T_AMBIENT_K ** 3 + h_eff)
        p_abs = irr_central * (length_power_m ** 2) * 1.0e4 * RATIO_ON
        dt_ss_full = p_abs / dp_dt
        tau_thermal_s = mass_kg * C_P_SI / dp_dt
        kn = LAMBDA_AIR_M / length_cond_m
        h_slip = h_eff / (1.0 + 2.0 * kn)
        assert abs(h_eff * length_cond_m - K_AIR_W_MK) < 1e-15 * K_AIR_W_MK
        assert abs(mass_kg - DENSITY_SI_KG_M3 * length_cond_m ** 3) < 1e-30
        assert abs(p_abs - irr_central * (length_power_m ** 2) * 1.0e4 * RATIO_ON) < 1e-30
        return {
            "regime": name, "length_power_m": length_power_m, "length_cond_m": length_cond_m,
            "h_eff_w_m2k": h_eff, "area_m2": area_m2, "mass_kg": mass_kg,
            "dp_dt_w_k": dp_dt, "p_abs_w": p_abs, "dt_ss_full_K": dt_ss_full,
            "tau_thermal_s": tau_thermal_s,
            "dwell_over_tau_thermal": DWELL_S / tau_thermal_s,
            "biot_number": h_eff * length_cond_m / K_SI_W_MK,
            "knudsen_number": kn, "h_eff_slip_corrected_w_m2k": h_slip,
            "slip_correction_relative": (h_slip - h_eff) / h_eff,
            "saturation_fraction_at_dwell": 1.0 - math.exp(-DWELL_S / tau_thermal_s),
            "netd_lo_over_dt_ss_full": NETD_BAND_K[0] / dt_ss_full,
            "wien_peak_um": ts.wien_peak_wavelength_um(T_AMBIENT_K + dt_ss_full),
            "netd": ts.netd_disposition(dt_ss_full, NETD_BAND_K),
            "netd_disclaimer": NETD_DISCLAIMER,
            "material_identity": {
                "material": "silicon (doped Si/Ge FCA host, matching the Block-A grid)",
                "density_kg_m3": DENSITY_SI_KG_M3, "c_p_j_kgk": C_P_SI,
                "k_solid_w_mk": K_SI_W_MK,
                "provenance": SILICON_PROVENANCE,          # [docket 18]
                "provenance_trace": (
                    "exp-046 section 2.3 -> 'sourced: experiments/037-.../NOTES.md:828-829' "
                    "-> that line reads 'standard CITED thermal constants' -> grep over "
                    "experiments/037-* for DOI/Handbook/CRC/2330/148 returns only that same "
                    "sentence. The chain terminates unsourced. The values are correct for "
                    "bulk crystalline Si; this is a PROVENANCE downgrade, not a claim the "
                    "numbers are wrong [docket 18]."),
            },
        }

    regime_w = self_consistent_regime(w_on_m, w_on_m, "w_on_consistent")
    regime_r = self_consistent_regime(r_out_m, r_out_m, "r_out_consistent")
    regime_mixed = self_consistent_regime(w_on_m, r_out_m, "mixed_w_power_r_cond")

    # exp-045 reproduction self-check (the desk gate on the third column)
    exp045_committed = {"w_on": (1.0875240683859519e-05, 3.139185832536293e-03),
                        "r_out": (3.5982339737222747e-06, 3.4332969490950116e-04)}
    repro = {
        "w_on_dt_ss_rel": abs(regime_w["dt_ss_full_K"] - exp045_committed["w_on"][0]) / exp045_committed["w_on"][0],
        "w_on_tau_rel": abs(regime_w["tau_thermal_s"] - exp045_committed["w_on"][1]) / exp045_committed["w_on"][1],
        "r_out_dt_ss_rel": abs(regime_r["dt_ss_full_K"] - exp045_committed["r_out"][0]) / exp045_committed["r_out"][0],
        "r_out_tau_rel": abs(regime_r["tau_thermal_s"] - exp045_committed["r_out"][1]) / exp045_committed["r_out"][1],
    }
    assert max(repro.values()) < 1e-12, repro

    # [docket 19] rho*C_P (fill-factor) sensitivity: tau_th scales linearly in
    # rho*C_P, so the "below vs above 25" question is NOT decided by the
    # conduction length alone.
    #
    # [p5 docket 15] THERMODYNAMICS' Biot finding, adopted: a fill factor below
    # unity also LOWERS the effective conductivity of the host, raising
    # Bi = k_air/kappa_eff toward unity and invalidating the lumped single-tau
    # model whose numbers this very row reports. Mixing rule stated:
    # Maxwell-Garnett for a dilute-solid-in-air composite,
    # kappa_eff = k_air*(1 + 2*phi)/(1 - phi). Knudsen is reported per row on
    # the same conduction length (length-invariant here by construction, but
    # printed so the validity condition is visible where the number is read).
    rho_cp_sensitivity = []
    for phi in (1.0, 0.5, 0.1, 0.01):
        tau = regime_mixed["tau_thermal_s"] * phi
        kappa_eff = (K_SI_W_MK if phi >= 1.0
                     else K_AIR_W_MK * (1.0 + 2.0 * phi) / (1.0 - phi))
        bi_row = K_AIR_W_MK / kappa_eff
        rho_cp_sensitivity.append({
            "rho_cp_scale_or_fill_factor": phi,
            "tau_thermal_s": tau, "dwell_over_tau_thermal": DWELL_S / tau,
            "above_N_TRANSIENT_TAU_25": DWELL_S / tau >= kin.N_TRANSIENT_TAU,
            "dt_ss_full_K_unchanged": regime_mixed["dt_ss_full_K"],
            # ------------------------------------------- [p5 docket 15]
            "mixing_rule": "Maxwell-Garnett: kappa_eff = k_air*(1+2*phi)/(1-phi)",
            "kappa_eff_w_mk": kappa_eff,
            "biot_number": bi_row,
            "knudsen_number": LAMBDA_AIR_M / r_out_m,
            "lumped_single_tau_valid_Bi_lt_0p1": bi_row < 0.1})

    # [p5 docket 16] MATERIALS' emissivity sensitivity, with the COMPUTED
    # magnitude rather than its "~4x" estimate (wrong by ~4 orders, in the safe
    # direction). At the mixed regime the radiative channel is a ~0.05% share
    # of dP/dT, so even the absurd bound epsilon -> 0 barely moves dt_ss.
    h_eff_mixed = regime_mixed["h_eff_w_m2k"]
    rad_channel = 4.0 * EMISSIVITY * ts.SIGMA_SB * T_AMBIENT_K ** 3
    emissivity_sensitivity = []
    for eps in (EMISSIVITY, 0.09, 0.009, 0.0):
        dpdt_eps = regime_mixed["area_m2"] * (4.0 * eps * ts.SIGMA_SB * T_AMBIENT_K ** 3 + h_eff_mixed)
        dt_eps = regime_mixed["p_abs_w"] / dpdt_eps
        emissivity_sensitivity.append({
            "emissivity": eps,
            "radiative_channel_w_m2k": 4.0 * eps * ts.SIGMA_SB * T_AMBIENT_K ** 3,
            "dt_ss_full_K": dt_eps,
            "dt_ss_inflation_vs_committed": dt_eps / regime_mixed["dt_ss_full_K"],
            "netd_lo_over_dt_ss_full": NETD_BAND_K[0] / dt_eps})
    emissivity_disclosure = {
        "committed_emissivity": EMISSIVITY,
        "radiative_channel_w_m2k": rad_channel,
        "conduction_channel_h_eff_w_m2k": h_eff_mixed,
        "radiative_share_of_dP_dT_pct": 100.0 * rad_channel / (rad_channel + h_eff_mixed),
        "rows": emissivity_sensitivity,
        "statement": (
            "[p5 docket 16] MATERIALS' concern is REAL AS A DISCLOSURE GAP and wrong by "
            "~4 orders of magnitude as a number: its review states eps_corr = 0.1 'only "
            "inflates dt_ss_full by up to ~4x'; the computed figure is 1.0004x. Its "
            "CONCLUSION ('comfortably short of threatening 607x') holds a fortiori, and "
            "its actual finding stands -- idealization 7's 'dilution is uniformly "
            "conservative' framing omits a third, opposite-signed consequence already "
            "flagged in lab/thermo_sidecar.py:151-153 since exp-033. Recording the "
            "computed number, not the estimate. NOTE ALSO: `netd_disposition`'s own "
            "`emissivity_correction` is a multiplier ON delta-T "
            "(lab/thermo_sidecar.py:205), so on the DETECTOR side lower emissivity is "
            "strictly conservative -- the two sides push opposite ways and both are "
            "negligible here."),
    }

    # true-disk shape sensitivity (idealization 5, carried from Phase 1)
    h_disk = K_AIR_W_MK / r_out_m
    area_disk = math.pi * r_out_m ** 2
    mass_disk = DENSITY_SI_KG_M3 * math.pi * r_out_m ** 2 * (2.0 * r_out_m)
    dpdt_disk = area_disk * (4.0 * EMISSIVITY * ts.SIGMA_SB * T_AMBIENT_K ** 3 + h_disk)
    tau_disk = mass_disk * C_P_SI / dpdt_disk

    # ---- the 6-regime regrowth of exp-045's Block A sweep (P-TH23-B5)
    hosts = [("A", 1e9), ("B", 1e6), ("C", 1e3), ("D", 1e1)]
    ratios = [1e-9, 1e-5, 1e-3, 1e-1]
    n_r = 13
    r_grid = [10.0 ** (-1.0 + 2.0 * i / (n_r - 1)) for i in range(n_r)]
    regimes = {
        "uncorrected": (tau_thermal_s_old, dt_ss_full_old),
        "t22_area_only_x2.9": (tau_thermal_s_old * 2.9, dt_ss_full_old),
        "t22_area_only_x3.0": (tau_thermal_s_old * 3.0, dt_ss_full_old),
        "fully_corrected_si_w_consistent": (regime_w["tau_thermal_s"], regime_w["dt_ss_full_K"]),
        "fully_corrected_si_r_out_consistent": (regime_r["tau_thermal_s"], regime_r["dt_ss_full_K"]),
        "mixed_w_power_r_cond_T23": (regime_mixed["tau_thermal_s"], regime_mixed["dt_ss_full_K"]),
    }
    sweep_points = []
    for host, k_r in hosts:
        for r in ratios:
            k_f = r * k_r
            tau_k = 1.0 / (k_f + k_r)
            for reg_name, (tau_th, dt_ss) in regimes.items():
                for axis, anchor in (("K", tau_k), ("T", tau_th)):
                    for rv in r_grid:
                        dwell = rv * anchor
                        exact = coupled_kinetics_thermal_dT(k_f, k_r, dt_ss, tau_th, dwell)
                        sweep_points.append({
                            "host": host, "r": r, "regime": reg_name, "axis": axis,
                            "R": rv, "dwell_s": dwell, "exact_coupled_dT_K": exact,
                            "netd": ts.netd_disposition(exact, NETD_BAND_K),
                            "netd_disclaimer": NETD_DISCLAIMER})
    new_pts = [p for p in sweep_points if p["regime"] == "mixed_w_power_r_cond_T23"]
    max_new = max(p["exact_coupled_dT_K"] for p in new_pts)
    max_all = max(p["exact_coupled_dT_K"] for p in sweep_points)

    return {
        "irradiance_w_cm2": irr_central, "dwell_s": DWELL_S,
        "r_out_m": r_out_m, "w_on_m": w_on_m,
        "regimes": {"w_on_consistent": regime_w, "r_out_consistent": regime_r,
                    "mixed_w_power_r_cond": regime_mixed},
        "primary_regime": "mixed_w_power_r_cond",
        "exp045_reproduction_selfcheck_rel": repro,
        "tau_thermal_structure_note": (
            "tau_thermal = rho C_P L_cond^2 / (4 eps sigma T^3 L_cond + k_air) -- "
            "algebraically independent of the ABSORBED POWER, hence of L_power. But it "
            "is NOT 'decided by the conduction length alone' [docket 19]: the rho*C_P "
            "factor is the unsourced half of the chain (see the provenance downgrade "
            "and the rho*C_P sensitivity row), and `netd_disposition`'s own fill_factor "
            "multiplier is left at 1.0 here while mass = rho_Si*L^3 assigns 100%-fill "
            "crystalline silicon to what the same module elsewhere calls a dilute "
            "vapour/aerosol host. Disclosed, not silently carried."),
        "fill_factor_disclosure": {
            "netd_fill_factor_used": 1.0,
            "note": ("`lab.thermo_sidecar.netd_disposition` carries an explicit "
                     "fill_factor multiplier which this cycle leaves at 1.0, exactly as "
                     "exp-045 did. A dilute host would push the effective delta-T DOWN "
                     "(further below NETD), so the UNDETECTABLE classifications here are "
                     "conservative with respect to this idealization -- but the thermal "
                     "MASS uses 100%-fill silicon, which pushes tau_thermal UP; the two "
                     "are disclosed together because they are the same unsourced "
                     "assumption seen from two sides [docket 19]."),
            "validity_conditions": (
                "[p5 docket 15] A fill factor below unity ALSO lowers kappa_eff, raising "
                "Bi = k_air/kappa_eff toward unity (0.25 / 0.75 / 0.97 at phi = 0.5 / 0.1 "
                "/ 0.01 under Maxwell-Garnett, computed per row in `rho_cp_sensitivity`) "
                "and INVALIDATING the lumped single-tau model the sensitivity row's own "
                "numbers come from. THERMODYNAMICS' framing, adopted: the sensitivity "
                "table offered as reassurance is evaluated at fill fractions where the "
                "model that produced its numbers is no longer licensed, and the "
                "reassurance is largest precisely where the model is most invalid. The "
                "delta-T CLASSIFICATION is unaffected (internal gradients make the "
                "radiating surface cooler, not warmer, so detectability gets more "
                "conservative); the TAU_THERMAL numbers are the ones affected -- and "
                "T23's entire content is a tau_thermal question, which is why this is a "
                "T23 finding, not a delta-T finding.")},
        "emissivity_disclosure": emissivity_disclosure,           # [p5 docket 16]
        "rho_cp_sensitivity": rho_cp_sensitivity,
        "shape_sensitivity_true_disk": {
            "tau_thermal_s": tau_disk, "dwell_over_tau_thermal": DWELL_S / tau_disk,
            "dt_ss_full_K": regime_mixed["p_abs_w"] / dpdt_disk,
            "note": "cube idiom (area=L^2, volume=L^3) inherited unchanged from exp-045 so "
                    "the mixed regime differs in exactly one variable; the true-disk "
                    "alternative is a disclosed sensitivity, not the headline."},
        "block_a_regrowth": {
            "n_points": len(sweep_points), "n_new_points_mixed_regime": len(new_pts),
            "n_regimes": len(regimes),
            "max_dT_new_points_K": max_new,
            "netd_lo_margin_new_points": NETD_BAND_K[0] / max_new,
            "max_dT_all_points_K": max_all,
            "all_undetectable_or_better": all(
                p["netd"]["classification"] != "DETECTABLE" for p in sweep_points),
            "points": sweep_points},
        "predictions": {
            "P-TH23-B1": {"statement": "mixed dwell/tau_thermal equals the r_out-consistent "
                          "value identically (tau_thermal is independent of L_power)",
                          "band": "194.176815 +/- 1 in the 12th s.f.",
                          "measured": regime_mixed["dwell_over_tau_thermal"],
                          "identical_to_r_out": abs(regime_mixed["dwell_over_tau_thermal"]
                                                    - regime_r["dwell_over_tau_thermal"]),
                          # ----------------------------------- [p5 docket 17]
                          "class": "DESK-VERIFIABLE STRUCTURAL IDENTITY (not a measurement)",
                          "identity_tag": (
                              "[p5 docket 17] Tagged in the scorecard the same way A1/A3 "
                              "are: tau_thermal = rho C_P L_cond^2/(4 eps sigma T^3 L_cond "
                              "+ k_air) contains NO power term, and 'mixed' is DEFINED as "
                              "r_out-conduction, so bit-identity to the r_out regime cannot "
                              "fail. Same species as the identity Attack 2 struck one block "
                              "over. phase3_synthesis.md already said 'a reproduction, not "
                              "a fresh finding' -- one document upstream of the one that "
                              "gets cited; carried into results.json here.")},
            "P-TH23-B2": {"statement": "mixed dt_ss_full and its two ratios",
                          "band": "3.2930761e-5 K; ratio to r_out = (w_on/r_out)^2 = "
                                  "9.151923 exactly; ratio to w_on = 3.02805; +/-0.01%",
                          "dt_ss_full_K": regime_mixed["dt_ss_full_K"],
                          "ratio_to_r_out": regime_mixed["dt_ss_full_K"] / regime_r["dt_ss_full_K"],
                          "w_on_over_r_out_squared": (w_on_m / r_out_m) ** 2,
                          "ratio_to_w_on": regime_mixed["dt_ss_full_K"] / regime_w["dt_ss_full_K"]},
            "P-TH23-B3": {"statement": ("mixed regime remains UNDETECTABLE by the "
                                        "NETD/detectability instrument comparison. The "
                                        "Phase-1 'eye-invisible' claim is STRUCK [docket 20]: "
                                        "it had no perceptual falsifier and is "
                                        "constraint-3-shaped."),
                          "band": "NETD_lo/dt_ss_full in [600, 615]; Wien peak in [9.87, 9.90] um",
                          "netd_lo_over_dt_ss": regime_mixed["netd_lo_over_dt_ss_full"],
                          "wien_peak_um": regime_mixed["wien_peak_um"],
                          "classification": regime_mixed["netd"]["classification"],
                          "netd_disclaimer": NETD_DISCLAIMER},
            "P-TH23-B4": {"statement": "Biot/Knudsen at the mixed regime match the r_out regime",
                          "band": "Bi = 1.7567568e-4, Kn = 2.807692e-2, slip correction -5.3168%",
                          "biot": regime_mixed["biot_number"], "knudsen": regime_mixed["knudsen_number"],
                          "slip_correction_pct": 100.0 * regime_mixed["slip_correction_relative"]},
            "P-TH23-B5": {"statement": "Block A regrows to 6 regimes",
                          "band": "2496 points; max dT over the 416 new points in "
                                  "[2.95e-6, 3.05e-6] K; NETD_lo margin >= 6500x; all "
                                  "UNDETECTABLE-or-better",
                          "n_points": len(sweep_points), "n_new": len(new_pts),
                          "max_dT_new_K": max_new,
                          "netd_lo_margin": NETD_BAND_K[0] / max_new,
                          "netd_disclaimer": NETD_DISCLAIMER},
            "P-TH23-B6": {"statement": "the N_TRANSIENT_TAU=25 stake is void: thermal "
                                       "saturation at both endpoints",
                          "band": "1-exp(-dwell/tau_th) >= 1-1e-9 at both 21.24x and 194.18x",
                          "saturation_w_on": regime_w["saturation_fraction_at_dwell"],
                          "saturation_mixed": regime_mixed["saturation_fraction_at_dwell"],
                          "one_minus_saturation_w_on": math.exp(-DWELL_S / regime_w["tau_thermal_s"]),
                          "one_minus_saturation_mixed": math.exp(-DWELL_S / regime_mixed["tau_thermal_s"]),
                          "N_TRANSIENT_TAU": kin.N_TRANSIENT_TAU,
                          "stake_note": ("N_TRANSIENT_TAU is a NUMERICAL-INTEGRATION constant "
                                         "for lab.kinetics' RK4 branch (lab/kinetics.py:97); "
                                         "nothing in the thermal chain is numerically "
                                         "integrated at all -- every thermal quantity here is "
                                         "a closed form.")},
        },
        # ==================================================== [p5 docket 14]
        "t23_disposition": {
            "thread": "T23 -- which characteristic length governs the thermal sidecar",
            "ruling": ("MIXED is adopted as the primary convention: absorbed power on "
                       "`w_on`, conduction and thermal mass on `r_out`."),
            "argument_power_on_w_on": (
                "P_abs is set by the illuminated cross-section the established "
                "extinction ratio RATIO_ON was itself calibrated on, which is `w_on` "
                "(sigma_ext's own 1/e width). Using r_out there would double-count the "
                "beam geometry the ratio already contains."),
            "argument_conduction_and_mass_on_r_out": (
                "h_eff = k_air/L and mass = rho*L^3 must use the length over which heat "
                "actually leaves and is stored, which is the body's outer radius r_out. "
                "The Nusselt-2 derivation h_eff = k_air/L that this bench uses is derived "
                "for the BODY's own scale, not the illumination's."),
            "honest_split": (
                "The OPERATIVE question -- whether dwell/tau_thermal sits below or above "
                "N_TRANSIENT_TAU = 25 -- is decided ROBUSTLY: 97x-19418x across every "
                "disclosed shape and fill variation (true disk 97.09x, cube 194.18x, "
                "phi=0.5 388.35x, phi=0.1 1941.8x, phi=0.01 19418x), so no endpoint of "
                "the disclosed range crosses 25. The NOMINAL length question is decided "
                "by ARGUMENT, not by measurement -- this cycle produced no measurement "
                "that discriminates between the three conventions."),
            "validity_caveat": (
                "[p5 docket 15] The tau_thermal numbers above are lumped single-tau "
                "numbers, and Bi >= 0.25 at every sub-unity fill factor, where that model "
                "is not licensed. A tau_thermal that is not a well-defined single number "
                "is a worse problem for T23 than the length-scale ambiguity T23 was opened "
                "to settle. Recorded as the sharpest charter-relevant open item this "
                "cycle leaves."),
            "why_this_key_exists": (
                "The lead seat's own Tier-1 #2 deliverable produced no recorded lesson: "
                "before this fix, `T23` appeared in results.json only inside two regime "
                "LABELS, NOTES.md mentioned it only in the title and hypothesis, and the "
                "argument for the mixed convention lived ONLY in phase1_proposal.md "
                "section 2.3 -- a document with a dozen struck claims in it and, until "
                "this same close, no banner. EM's ruling upheld: three endpoints and no "
                "ruling is worse than two."),
        },
        "netd_disclaimer": NETD_DISCLAIMER,
    }


def coupled_kinetics_thermal_dT(k_f, k_r, dt_ss_full, tau_thermal_s, dwell_s):
    """Reused VERBATIM from experiments/045-.../run.py:121-143 (itself reused
    verbatim from exp-044, where it was verified against scipy.integrate.odeint
    to <4e-4 relative at every grid point)."""
    tau_k = 1.0 / (k_f + k_r)
    n_ss = k_f / (k_f + k_r)
    if abs(tau_k - tau_thermal_s) < 1e-12 * max(tau_k, tau_thermal_s):
        raise ValueError("degenerate tau_k == tau_thermal_s, not expected on this grid")
    bracket = (1.0
               - (tau_k / (tau_k - tau_thermal_s)) * math.exp(-dwell_s / tau_k)
               + (tau_thermal_s / (tau_k - tau_thermal_s)) * math.exp(-dwell_s / tau_thermal_s))
    return dt_ss_full * n_ss * bracket


def coupled_segment_general(k_f, k_r, dt_ss_full, tau_thermal_s, dt, n0, dT0):
    """Reused VERBATIM from experiments/045-.../run.py:146-172."""
    n_eq = k_f / (k_f + k_r)
    tau_k = 1.0 / (k_f + k_r)
    n_final = n_eq + (n0 - n_eq) * math.exp(-dt / tau_k)
    if abs(tau_k - tau_thermal_s) < 1e-12 * max(tau_k, tau_thermal_s):
        raise ValueError("degenerate tau_k == tau_thermal_s, not expected on this grid")
    dT_final = (dT0 * math.exp(-dt / tau_thermal_s)
                + dt_ss_full * n_eq * (1.0 - math.exp(-dt / tau_thermal_s))
                + dt_ss_full * (n0 - n_eq) * (tau_k / (tau_k - tau_thermal_s))
                * (math.exp(-dt / tau_k) - math.exp(-dt / tau_thermal_s)))
    return n_final, dT_final


# ================================================================ Block C desk
HOSTS_FULL = [("A", 1e9), ("B", 1e6), ("C", 1e3), ("D", 1e1), ("E", 1e0)]   # exp-038's own
RATIOS_FULL = [1e-9, 1e-5, 1e-3, 1e-1, 1.0]                                  # exp-038's own
EXP045_DONE = {("D", r) for r in (1e-9, 1e-5, 1e-3, 1e-1)}                    # already committed
N_PULSES = 5
GAP_MULTS = (("5tau", 5.0), ("0.5tau", 0.5))


def memory_ratio_closed_form(dwell_s, k_f, k_r, gap_mult):
    """[C2] Fixed point of the end-of-ON affine map n_{k+1} = n_eq(1-a) + a f n_k:
        ratio_inf = 1/(1 - a f),  a = exp(-D/tau_k),  f = exp(-k_r G) = exp(-m/(1+r))
    for a gap G = m*tau_k. Memory onset (ratio_inf > 1.05) <=> D/tau_k < ln(21 f)."""
    tau_k = 1.0 / (k_f + k_r)
    r = k_f / k_r if k_r > 0 else float("inf")
    a = math.exp(-dwell_s / tau_k)
    f = math.exp(-gap_mult / (1.0 + r))
    thr = math.log(21.0 * f) if 21.0 * f > 0 else float("-inf")
    return {"tau_kinetics_s": tau_k, "a": a, "f": f,
            "ratio_infinity": 1.0 / (1.0 - a * f),
            "supremum_ratio_at_zero_dwell": 1.0 / (1.0 - f),
            "dwell_over_tau_k": dwell_s / tau_k,
            "onset_threshold_dwell_over_tau_k": thr,
            "memory_possible_at_any_dwell": 21.0 * f > 1.0,
            "predicted_memory": (21.0 * f > 1.0) and (dwell_s / tau_k < thr)}


def train_ratio(k_f, k_r, dwell_s, gap_s, dt_ss, tau_th, n_pulses=N_PULSES):
    """exp-045's Block-C convention VERBATIM, including its disclosed role
    inversion [docket 17]: `T_pulse` is the OFF GAP and `dt_sweep` is the ON
    DWELL D. The OFF gap uses a hard k_f=0 (A=0.0) -- exp-045's own disclosed
    idealization, unchanged so these points are comparable to its Host-D four."""
    segs = kin.pulse_train_segments(k_f_ambient=k_f, k_r=k_r, A=0.0,
                                    T_pulse=gap_s, dt_sweep=dwell_s, n_pulses=n_pulses)
    _, _, n_arr = kin.integrate_segments(segs, n0=0.0, method="exp", record=True)
    on_end_idx = [1 + 2 * i for i in range(n_pulses + 1)]
    n_on = [float(n_arr[i]) for i in on_end_idx]
    n_walk, dT_walk = 0.0, 0.0
    dT_seg = []
    for s_kf, s_kr, s_dt in segs:
        n_walk, dT_walk = coupled_segment_general(s_kf, s_kr, dt_ss, tau_th, s_dt, n_walk, dT_walk)
        dT_seg.append(dT_walk)
    dT_on = [dT_seg[2 * i] for i in range(n_pulses + 1)]
    return n_on, dT_on


def block_c_desk(block_b):
    reg = block_b["regimes"]
    primary = reg["mixed_w_power_r_cond"]
    regime_thermal = {
        "mixed_w_power_r_cond_T23_PRIMARY": (primary["dt_ss_full_K"], primary["tau_thermal_s"]),
        "w_on_consistent": (reg["w_on_consistent"]["dt_ss_full_K"], reg["w_on_consistent"]["tau_thermal_s"]),
        "r_out_consistent": (reg["r_out_consistent"]["dt_ss_full_K"], reg["r_out_consistent"]["tau_thermal_s"]),
    }

    # ---- C1: the FULL 5x5 grid minus Host D's already-committed four [docket 16].
    # The count is COMPUTED, never asserted (Phase-3's own instruction).
    grid = [(h, k_r, r) for h, k_r in HOSTS_FULL for r in RATIOS_FULL]
    new_grid = [(h, k_r, r) for (h, k_r, r) in grid if (h, r) not in EXP045_DONE]
    n_new_points = len(new_grid)
    count_note = (f"full exp-038 grid = {len(grid)} points; Host D's exp-045-committed "
                  f"four removed; NEW points computed here = {n_new_points}. Phase 3's own "
                  f"hand-count was 21 -- "
                  + ("code and hand-count AGREE." if n_new_points == 21 else
                     f"DISAGREEMENT: the code's {n_new_points} is authoritative."))

    points = []
    for host, k_r, r in new_grid:
        k_f = r * k_r
        tau_k = 1.0 / (k_f + k_r)
        for gap_name, m in GAP_MULTS:
            gap = m * tau_k
            cf = memory_ratio_closed_form(DWELL_S, k_f, k_r, m)
            rec = {"host": host, "k_r": k_r, "r": r, "k_f_on": k_f,
                   "tau_kinetics_s": tau_k, "gap_name": gap_name, "gap_s": gap,
                   "dwell_s": DWELL_S, "n_pulses": N_PULSES,
                   "dwell_over_tau_kinetics": DWELL_S / tau_k,
                   "realizability_tier": realizability_tier(host, r),
                   "closed_form": cf, "netd_disclaimer": NETD_DISCLAIMER,
                   "by_regime": {}}
            for reg_name, (dt_ss, tau_th) in regime_thermal.items():
                n_on, dT_on = train_ratio(k_f, k_r, DWELL_S, gap, dt_ss, tau_th)
                ratio = n_on[-1] / n_on[0] if n_on[0] > 0 else float("inf")
                dec_first, dec_per = dt_ss * n_on[0], dt_ss * n_on[-1]
                rec["by_regime"][reg_name] = {
                    "n_at_on_end": n_on,
                    "periodic_over_first_ratio": ratio,
                    "dT_first_decoupled_K": dec_first,
                    "dT_periodic_decoupled_K": dec_per,
                    "dT_exact_first_K": dT_on[0], "dT_exact_periodic_K": dT_on[-1],
                    "exact_over_decoupled_first": dT_on[0] / dec_first if dec_first > 0 else float("nan"),
                    "exact_over_decoupled_periodic": dT_on[-1] / dec_per if dec_per > 0 else float("nan"),
                    "decoupled_is_conservative": (dT_on[0] <= dec_first) and (dT_on[-1] <= dec_per),
                    "netd_periodic": ts.netd_disposition(dec_per, NETD_BAND_K),
                    "netd_disclaimer": NETD_DISCLAIMER,
                }
            rec["closed_form_vs_measured_rel"] = abs(
                cf["ratio_infinity"] - rec["by_regime"]["mixed_w_power_r_cond_T23_PRIMARY"]["periodic_over_first_ratio"]
            ) / cf["ratio_infinity"]
            points.append(rec)

    def prim(p):
        return p["by_regime"]["mixed_w_power_r_cond_T23_PRIMARY"]

    neg_control = [p for p in points if p["dwell_over_tau_kinetics"] >= 66.0]
    memory_pts = [p for p in points if abs(prim(p)["periodic_over_first_ratio"] - 1.0) > 1e-6]
    max_dev_neg = max(abs(prim(p)["periodic_over_first_ratio"] - 1.0) for p in neg_control)
    max_dT = max(prim(p)["dT_periodic_decoupled_K"] for p in points)
    worst_cons = min(prim(p)["exact_over_decoupled_periodic"] for p in points)
    all_cons = all(v["decoupled_is_conservative"] for p in points for v in p["by_regime"].values())
    all_undet = all(v["netd_periodic"]["classification"] != "DETECTABLE"
                    for p in points for v in p["by_regime"].values())
    published = [p for p in points if p["realizability_tier"] == "PUBLISHED"]
    unobtanium = [p for p in points if p["realizability_tier"].startswith("UNOBTANIUM")]
    host_e = [p for p in points if p["host"] == "E"]
    host_e_05 = [p for p in host_e if p["gap_name"] == "0.5tau"]
    max_5tau = max(prim(p)["periodic_over_first_ratio"] for p in points if p["gap_name"] == "5tau")
    max_05tau = max(prim(p)["periodic_over_first_ratio"] for p in points if p["gap_name"] == "0.5tau")
    weak = [p for p in points if p not in memory_pts]
    cf_weak = max(p["closed_form_vs_measured_rel"] for p in weak)
    cf_strong = max([p["closed_form_vs_measured_rel"] for p in memory_pts] or [0.0])
    n_5tau_memory_c1 = sum(1 for p in points if p["gap_name"] == "5tau"
                           and prim(p)["periodic_over_first_ratio"] > 1.05)

    # ---- C5: closed form vs exp-045's own 8 committed Host-D points
    with open(os.path.join(EXP045, "results.json")) as f:
        r045 = json.load(f)
    c5_rows = []
    for key, v in r045["block_c_dose_accumulation_kinetics"]["points"].items():
        m = 5.0 if v["gap_name"] == "5tau" else 0.5
        cf = memory_ratio_closed_form(v["dwell_central_s"], v["k_f_on"], v["k_r"], m)
        c5_rows.append({"point": key, "committed_ratio": v["periodic_over_first_ratio"],
                        "closed_form_ratio": cf["ratio_infinity"],
                        "rel_diff": abs(cf["ratio_infinity"] - v["periodic_over_first_ratio"])
                        / v["periodic_over_first_ratio"]})
    c5_max = max(row["rel_diff"] for row in c5_rows)
    c5_min = min(row["rel_diff"] for row in c5_rows)

    # ---- C3/C6: the ON-dwell (dt_sweep) duration scan [docket 17] -- a
    # VERIFICATION of C2's closed form, not a test of it (MATERIALS M2).
    dwell_scan = [1.0e-3, 1.0e-2, 66.7e-3, 0.1, 1.0]
    scan = []
    for host, k_r in HOSTS_FULL:
        for r in RATIOS_FULL:
            k_f = r * k_r
            tau_k = 1.0 / (k_f + k_r)
            for d in dwell_scan:
                for gap_name, m in GAP_MULTS:
                    n_on, _ = train_ratio(k_f, k_r, d, m * tau_k, 1.0, 1.0e12)
                    ratio = n_on[-1] / n_on[0] if n_on[0] > 0 else float("inf")
                    cf = memory_ratio_closed_form(d, k_f, k_r, m)
                    scan.append({
                        "host": host, "r": r, "dt_sweep_dwell_s": d, "gap_name": gap_name,
                        "dwell_over_tau_kinetics": d / tau_k,
                        "measured_ratio": ratio, "closed_form_ratio": cf["ratio_infinity"],
                        "closed_form_predicts_memory": cf["predicted_memory"],
                        "measured_memory": ratio > 1.05,
                        "realizability_tier": realizability_tier(host, r)})
    scan_agree = sum(1 for s in scan if s["closed_form_predicts_memory"] == s["measured_memory"])
    scan_5tau_over = [s for s in scan if s["gap_name"] == "5tau" and s["measured_ratio"] > 1.05]
    sup_5tau_r_small = 1.0 / (1.0 - math.exp(-5.0))
    sup_5tau_r_1e1 = 1.0 / (1.0 - math.exp(-5.0 / 1.1))
    thr_r_small = math.log(21.0 * math.exp(-0.5))
    thr_r_1e1 = math.log(21.0 * math.exp(-0.5 / 1.1))

    def crossing(m, r):
        lo, hi = 1e-6, 60.0
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            k_r = 10.0
            k_f = r * k_r
            tau_k = 1.0 / (k_f + k_r)
            n_on, _ = train_ratio(k_f, k_r, mid * tau_k, m * tau_k, 1.0, 1.0e12)
            if n_on[-1] / n_on[0] > 1.05:
                lo = mid
            else:
                hi = mid
        return 0.5 * (lo + hi)

    c6 = {
        "measured_0.5tau_crossing_dwell_over_tau_k_r_1e-3": crossing(0.5, 1e-3),
        "measured_0.5tau_crossing_dwell_over_tau_k_r_1e-1": crossing(0.5, 1e-1),
        "closed_form_threshold_r_small": thr_r_small,           # ln(21 e^-0.5) [docket 23]
        "closed_form_threshold_r_1e-1": thr_r_1e1,              # 2.590 [docket 23]
        "supremum_5tau_r_small": sup_5tau_r_small,              # 1.006784
        "supremum_5tau_r_1e-1": sup_5tau_r_1e1,                 # 1.010711 [docket 23]
        "n_5tau_points_above_1.05": len(scan_5tau_over),
    }

    return {
        "convention_note": (
            "exp-045's Block-C convention held identical: n_pulses=5, gaps 5*tau_k and "
            "0.5*tau_k, hard k_f=0 in the OFF gap, and `pulse_train_segments`'s own "
            "disclosed role inversion (T_pulse = the OFF gap, dt_sweep = the ON dwell D). "
            "C3 therefore scans `dt_sweep` [docket 17]."),
        "grid_note": count_note,
        "n_full_grid": len(grid), "n_new_points": n_new_points,
        "n_point_runs": len(points),
        "points": points,
        "c3_duration_scan": {
            "scanned_parameter": "dt_sweep (the ON dwell D) [docket 17]",
            "relabelled": "VERIFICATION of C2's closed form, not a test of it (MATERIALS M2)",
            "dwell_values_s": dwell_scan, "n_points": len(scan),
            "closed_form_agreement": f"{scan_agree}/{len(scan)}",
            "points": scan},
        "c6": c6,
        "c5_closed_form_vs_exp045": {"rows": c5_rows, "max_rel": c5_max, "min_rel": c5_min},
        "predictions": {
            "P-TH23-C1": {
                "statement": ("RESTATED for the extended grid [docket 16]: the "
                              "D/tau_k >= 66.7 points are exact negative controls (every ON "
                              "segment re-equilibrates), while the newly-added Host E column "
                              "and Host D r=1.0 exercise the POSITIVE branch for the first "
                              "time -- the original 12-point Hosts-A/B/C scope contained no "
                              "cell in which memory could appear at all."),
                "band": "|ratio-1| <= 1e-12 at all 30 negative-control point-runs "
                        "(D/tau_k >= 66.7); 12 point-runs with nonzero memory and 7 above "
                        "1.05, ALL confined to Host D r=1.0 and Host E",
                "n_negative_controls": len(neg_control),
                "max_deviation_negative_controls": max_dev_neg,
                "n_points_with_memory": len(memory_pts),
                "memory_points": [f"{p['host']}/r={p['r']:.0e}/{p['gap_name']}="
                                  f"{prim(p)['periodic_over_first_ratio']:.6f}" for p in memory_pts],
                "max_ratio_5tau": max_5tau, "max_ratio_0.5tau": max_05tau},
            "P-TH23-C2": {
                "statement": "closed-form memory-onset criterion ratio_inf = 1/(1-a f), "
                             "memory iff D/tau_k < ln(21 f)",
                "band": ("closed form (the INFINITE-train fixed point) reproduces the "
                         "measured 5-pulse ratio to <=1e-3 relative at every no-memory / "
                         "weak-memory point; at the strong-memory points the 5-pulse train "
                         "UNDER-converges to the fixed point by up to ~10%, in the expected "
                         "direction -- disclosed, not a discrepancy"),
                "max_rel_no_or_weak_memory_points": cf_weak,
                "max_rel_memory_points": cf_strong,
                "max_closed_form_vs_measured_rel": max(p["closed_form_vs_measured_rel"] for p in points),
                "ln_21_exp_minus_0.5": thr_r_small},
            "P-TH23-C3": {
                "statement": ("delta-T on the extended grid (mixed regime primary). NOTE: "
                              "Phase 1's [2.9e-6, 3.1e-6] K band was written for the "
                              "pre-extension 12-point Hosts-A/B/C scope, whose largest n_eq "
                              "was 0.0909 (r=1e-1). Docket item 16 adds the r=1.0 column "
                              "(n_eq=0.5) and Host E, which raises the ceiling by ~5.5x by "
                              "construction. The Phase-1 band is SUPERSEDED here, before the "
                              "run, and the superseding is attributed."),
                "band": "max decoupled dT in [1.6e-5, 1.7e-5] K (extended grid); NETD_lo "
                        "margin >= 1200x; every point UNDETECTABLE-or-better",
                "phase1_band_superseded": "[2.9e-6, 3.1e-6] K -- valid only for the "
                                          "pre-docket-16 Hosts-A/B/C r<=1e-1 scope",
                "max_dT_periodic_decoupled_K": max_dT,
                "netd_lo_margin": NETD_BAND_K[0] / max_dT,
                "all_undetectable_or_better": all_undet,
                "netd_disclaimer": NETD_DISCLAIMER},
            "P-TH23-C4": {
                "statement": ("Tier scoring on the FULL grid. The Phase-1 'corroborating "
                              "Amendment 3' claim is STRUCK unless Host E is present -- it is "
                              "now present, so the check is real: Amendment 3's finding is "
                              "'memory only at Hosts D and E', and this grid can now see both "
                              "halves of it [docket 16]."),
                "band": "zero memory at every PUBLISHED-tier point; memory confined to "
                        "Host D r=1.0 and Host E (the PLAUSIBLE/UNOBTANIUM tiers)",
                "n_published_points": len(published),
                "n_published_with_memory": sum(1 for p in published
                                               if prim(p)["periodic_over_first_ratio"] > 1.05),
                "n_unobtanium_points": len(unobtanium),
                "n_unobtanium_with_memory": sum(1 for p in unobtanium
                                                if prim(p)["periodic_over_first_ratio"] > 1.05),
                "n_host_e_0.5tau_with_memory": sum(1 for p in host_e_05
                                                   if prim(p)["periodic_over_first_ratio"] > 1.05)},
            "P-TH23-C5": {
                "statement": "the closed form reproduces exp-045's own 8 committed Host-D points",
                "band": "<= 0.2% relative at 8/8; the 5tau points agree to ~2e-15 [docket 23]",
                "max_rel": c5_max, "min_rel": c5_min, "n_rows": len(c5_rows)},
            "P-TH23-C6": {
                "statement": ("Amendment 3's host-list finding is a DIMENSIONLESS-DWELL "
                              "finding: memory at the 0.5tau gap iff D/tau_k < ln(21 f). "
                              "VERIFICATION of C2's closed form, not an independent test "
                              "[docket 17]. CORRECTED PRE-RUN: Phase 1's second clause -- "
                              "'at the 5tau gap NO point anywhere exceeds 1.05' -- is FALSE "
                              "on the extended grid. It holds only for r <= 1e-1, where "
                              "21f = 21 e^(-5/(1+r)) < 1 and the supremum is 1.0107. At "
                              "r = 1.0, f = e^(-2.5) = 0.0821, 21f = 1.72 > 1, so the "
                              "supremum is 1.0894 and short dwells DO cross 1.05 at a 5tau "
                              "gap. The r=1.0 column only exists here because docket item 16 "
                              "added it -- the clause was untestable in the Phase-1 scope."),
                "band": "0.5tau crossing at 2.5445 (r<<1) and 2.590 (r=1e-1), both inside "
                        "[2.4, 2.7]; 5tau supremum 1.006784 (r<<1) / 1.010711 (r=1e-1) / "
                        "1.0894 (r=1.0); 5tau points above 1.05 occur ONLY in the r=1.0 "
                        "column",
                "detail": c6,
                "n_c1_5tau_points_above_1.05": n_5tau_memory_c1,
                "supremum_5tau_r_1p0": 1.0 / (1.0 - math.exp(-2.5)),
                "onset_threshold_5tau_r_1p0": math.log(21.0 * math.exp(-2.5)),
                "duration_scan_agreement": f"{scan_agree}/{len(scan)}"},
        },
        "netd_disclaimer": NETD_DISCLAIMER,
    }


# ============================================================= Block A -- FDTD
def _width_1e2(b, y_lo):
    """1/e^2 half-width and interpolated centre of a positive flux profile.
    Reused from Red Team's own verified `fdtd_geom.py` measurement."""
    b = np.asarray(b, dtype=float)
    y = np.arange(y_lo, y_lo + b.size, dtype=float)
    ip = int(np.argmax(b))
    thr = b[ip] / math.e ** 2
    r = ip + int(np.argmax(b[ip:] < thr))
    l = ip - int(np.argmax(b[:ip + 1][::-1] < thr))

    def itp(i0, i1):
        return y[i0] + (thr - b[i0]) * (y[i1] - y[i0]) / (b[i1] - b[i0])

    hi, lo = itp(r - 1, r), itp(l + 1, l)
    return 0.5 * (hi - lo), 0.5 * (hi + lo), float(y[ip])


def exact_angular_spectrum_center(width, theta0_deg, lam_cells, z=None, n_fft=1 << 20, span=6.0e4):
    """POST-RUN DIAGNOSTIC, added after the predictions commit (disclosed in
    NOTES.md, not back-dated): exact NON-PARAXIAL angular-spectrum propagation
    of the same aperture (k_x = sqrt(k^2 - k_y^2), evanescent clipped) --
    Red Team's own `geom_check.py` method, reused. Zero FDTD cost.

    It exists because gate S16-b failed, and the question a failed gate must
    answer is WHICH of its two halves broke: the engine, or the target. The
    gate's target is ray optics (y_c + D_SP*tan(theta0)), which assumes the
    paraxial mapping k_y = k*theta; at S16-b's own width=40 the emitted
    divergence is 14deg FWHM, where k_y = k*sin(theta) is measurably nonlinear
    and the propagated profile is skewed toward +y. This function measures
    where the exact physics actually puts the beam, so the failure can be
    attributed instead of merely reported. It does NOT change the gate, its
    band, or its verdict.

    CORRECTED AT PHASE 5 [p5 docket 2], identically to the suite's own
    `stage16_oblique_gaussian_source::exact_center` [p5 docket 1]. As first
    written this function propagated the aperture as a prescribed FIELD and
    reduced it with |E|^2. Neither factor matches the bench:

      * `lab/fdtd2d.py:232-237` adds env*sin(wn - phase)*profile to Ez every
        step -- an impressed line CURRENT sheet J_z. The radiated angular
        spectrum therefore carries E~(k_y) ~ J~(k_y)/k_x.
      * `lab/ambient.py:36-39` -> `lab/sections.py:79-88`: observer_profile =
        -flux_profile_x = +0.5*Re(E_z conj(H_y)) -- a FLUX, carrying +k_x/k
        once via H, not squared via E.

    Two missing obliquities, opposite directions, no cancellation -- the same
    error species this program adjudicated at Iteration 19 (LOGBOOK T21). The
    corrected model divides by k_x and reduces with Sx = Re(E conj(H)),
    H = F^-1[(k_x/k) E~]. It reproduces exp-042's own committed
    `_G0_for` + `field_and_h` propagator to 0.030 cells in centre and 0.011
    cells in half-width; the SUPERSEDED field/|E|^2 reading is retained in the
    return value so the correction is auditable rather than silent."""
    k = 2.0 * np.pi / lam_cells
    z = float(dg.D_SP) if z is None else z
    y = (np.arange(n_fft) - n_fft // 2) * (span / n_fft)
    e0 = np.exp(-((y / width) ** 2)) * np.exp(1j * k * np.sin(np.radians(theta0_deg)) * y)
    ky = 2.0 * np.pi * np.fft.fftfreq(n_fft, d=span / n_fft)
    kx2 = k * k - ky * ky
    ok = kx2 > 0
    kx = np.sqrt(np.maximum(kx2, 0.0))
    spec = np.fft.fft(e0)
    phase = np.where(ok, np.exp(1j * kx * z), 0.0)

    def _read(inten):
        ip = int(np.argmax(inten))
        thr = inten[ip] / math.e ** 2
        r = ip + int(np.argmax(inten[ip:] < thr))
        l = ip - int(np.argmax(inten[:ip + 1][::-1] < thr))

        def itp(i0, i1):
            return y[i0] + (thr - inten[i0]) * (y[i1] - y[i0]) / (inten[i1] - inten[i0])

        hi, lo = itp(r - 1, r), itp(l + 1, l)
        return (0.5 * (hi - lo), 0.5 * (hi + lo) + dg.OBJ_Y, float(y[ip]) + dg.OBJ_Y)

    # CORRECTED: line-current source (spectrum / k_x), flux reduction
    a = np.where(ok, spec / np.where(ok, kx, 1.0), 0.0) * phase
    e = np.fft.ifft(a)
    h = np.fft.ifft(a * np.where(ok, kx / k, 0.0))
    hw_c, ctr_c, pk_c = _read(np.real(e * np.conj(h)))
    # SUPERSEDED: prescribed aperture field, |E|^2 -- kept for the erratum
    hw_s, ctr_s, pk_s = _read(np.abs(np.fft.ifft(spec * phase)) ** 2)
    return {"half_width_1e2": hw_c,
            "center_1e2_midpoint": ctr_c,
            "peak_cell": pk_c,
            "source_model": "impressed line current (spectrum/k_x), matching "
                            "lab/fdtd2d.py:232-237",
            "reduction": "flux Sx = Re(E conj(H)), H = F^-1[(k_x/k) E~], matching "
                         "lab/ambient.py observer_profile",
            "superseded_field_aperture_E2": {
                "half_width_1e2": hw_s, "center_1e2_midpoint": ctr_s, "peak_cell": pk_s,
                "note": "the shipped-at-Phase-4 comparator; physically wrong on BOTH "
                        "counts (prescribed field, |E|^2 reduction) [p5 docket 2]"},
            "emitted_fwhm_deg": math.degrees(
                C_COEF * lam_cells / (width * math.cos(math.radians(theta0_deg))))}


def fdtd_leg(leg):
    """One Block-A FDTD call on exp-042/041's committed geometry, VERBATIM."""
    from lab import Sim, ambient as _amb, sections as sc
    lam_cells = dg.CPL[leg["lambda_nm"]]
    t0 = time.time()
    sim = Sim(dg.NX, dg.NY, cells_per_lambda=lam_cells, courant_frac=dg.COURANT_FRAC,
              absorb=dg.ABSORB)
    if leg.get("sigma"):
        cx, cy = OBJ_XY
        x = np.arange(sim.nx)[:, None]
        y = np.arange(sim.ny)[None, :]
        sim.sigma_e[(x - cx) ** 2 + (y - cy) ** 2 <= dg.R_OUT ** 2] += leg["sigma"]
    if leg["profile"] == "gauss":
        sim.add_line_source(dg.SRC_X, profile="gauss", width=leg["width"],
                            angle_deg=leg["theta0_deg"], amplitude=1.0)
    else:
        sim.add_line_source(dg.SRC_X, angle_deg=leg["theta0_deg"], edge=dg.TAPER,
                            amplitude=1.0)
    sim.run(dg.STEPS)
    ph = sc.phasors(sc.full_capture(sim))
    prof = _amb.observer_profile(ph, dg.PLANE_X, dg.ABSORB, dg.NY - dg.ABSORB)
    out = {"id": leg["id"], "elapsed_s": time.time() - t0,
           # [docket 15] scalars only. At theta0 = 0 the beam sits ON the object
           # window and the flank windows sit in its far exponential wing, so the
           # Weber denominator underflows and C is meaningless (it is not a gate
           # for that leg either -- S16-a is gated on w(z)). Recorded as None
           # rather than as a 1e10 artefact.
           "C_empty_fdtd": _weber_of(prof) if leg["theta0_deg"] else None,
           "profile_plane_x": np.asarray(prof, dtype=float)}
    if leg["id"] == "S16-a":
        planes = {}
        for px, label in ((250, "z=50"), (150, "z=150"), (dg.PLANE_X, "z=223")):
            p = _amb.observer_profile(ph, px, dg.ABSORB, dg.NY - dg.ABSORB)
            hw, ctr, pk = _width_1e2(p, dg.ABSORB)
            z = dg.SRC_X - px
            z_r = math.pi * leg["width"] ** 2 / lam_cells
            target = leg["width"] * math.sqrt(1.0 + (z / z_r) ** 2)
            planes[label] = {"plane_x": px, "z_cells": z, "measured_half_width": hw,
                             "closed_form": target,
                             "rel_pct": 100.0 * abs(hw - target) / target,
                             "z_R_cells": z_r}
        out["s16a_planes"] = planes
    if leg["id"] in ("S16-b", "A-v2"):
        hw, ctr, pk = _width_1e2(prof, dg.ABSORB)
        out["half_width_1e2"] = hw
        out["beam_center_interpolated"] = ctr
        out["beam_peak_cell"] = pk
    return out


def run_block_a_fdtd(desk):
    legs = desk["fdtd_legs"]
    results = {}
    print(f"\n=== Block A FDTD: {len(legs)} new calls "
          f"(the ONLY FDTD in this cycle) ===", flush=True)
    for leg in legs:
        r = fdtd_leg(leg)
        results[leg["id"]] = r
        c = r["C_empty_fdtd"]
        print(f"  [{leg['n']}/{len(legs)}] {leg['id']:6s} "
              f"lam={leg['lambda_nm']} th={leg['theta0_deg']:+.0f} "
              f"{'width=%.3f' % leg['width'] if leg['width'] else 'plane'}"
              f"  C_empty=" + (f"{c:+.6f}" if c is not None else "n/a (theta0=0)")
              + f"  ({r['elapsed_s']:.1f}s)", flush=True)

    # ---- gates (this run's own self-check; the trust suite's stage 16 runs the
    # same gates independently, from its own FDTD calls) [docket 13]
    gates = {}
    a = results["S16-a"]["s16a_planes"]
    gates["S16-a"] = {"detail": a, "worst_rel_pct": max(v["rel_pct"] for v in a.values()),
                      "pass": max(v["rel_pct"] for v in a.values()) <= 3.0,
                      "band": "<=3%"}
    target_center = dg.OBJ_Y + dg.D_SP * math.tan(math.radians(40.0))
    ctr = results["S16-b"]["beam_center_interpolated"]
    gates["S16-b"] = {"target_center": target_center, "measured_center": ctr,
                      "measured_peak_cell": results["S16-b"]["beam_peak_cell"],
                      "delta_cells": abs(ctr - target_center),
                      "pass": abs(ctr - target_center) <= 2.0, "band": "+/-2 cells",
                      "estimator": "interpolated 1/e^2 crossing midpoint (as committed)"}
    # POST-RUN DIAGNOSTIC on the failed gate (added after the predictions
    # commit; disclosed in NOTES.md; changes no band and no verdict).
    diag = {}
    for lid, width in (("S16-b", 40.0), ("A-v2", w_line_cells(20, 10, 40))):
        ex = exact_angular_spectrum_center(width, 40.0, dg.CPL[600])
        diag[lid] = {
            "width": width, "exact_angular_spectrum": ex,
            "fdtd_center_1e2_midpoint": results[lid]["beam_center_interpolated"],
            "fdtd_peak_cell": results[lid]["beam_peak_cell"],
            "fdtd_half_width_1e2": results[lid]["half_width_1e2"],
            "ray_optics_center": target_center,
            "exact_minus_ray_optics_cells": ex["center_1e2_midpoint"] - target_center,
            "fdtd_minus_exact_cells": results[lid]["beam_center_interpolated"] - ex["center_1e2_midpoint"]}
    gates["S16-b"]["post_run_diagnostic_nonparaxial"] = diag
    gates["S16-b"]["diagnosis"] = (
        "The gate's TARGET is ray optics, which assumes the paraxial mapping "
        "k_y = k*theta. At width=40 the emitted divergence is 14.0deg FWHM, where "
        "k_y = k*sin(theta) is measurably nonlinear and the propagated profile is "
        "skewed toward +y. Exact non-paraxial angular-spectrum propagation of the "
        "same aperture puts the 1/e^2 midpoint at "
        f"{diag['S16-b']['exact_angular_spectrum']['center_1e2_midpoint']:.2f} -- "
        f"{diag['S16-b']['exact_minus_ray_optics_cells']:+.1f} cells from the "
        "ray-optics target the gate scores against, i.e. the pre-registered target "
        "is outside its own +/-2-cell band before any engine is involved. FDTD "
        f"reads {results['S16-b']['beam_center_interpolated']:.2f}, "
        f"{diag['S16-b']['fdtd_minus_exact_cells']:+.1f} cells from the exact "
        "value. Reported as a FAILED gate, not re-banded: the fix belongs to "
        "Phase 5, and the honest statement is that S16-b as specified tests a "
        "paraxial identity at a non-paraxial divergence.")
    ref = -0.010964794540566314
    got = results["S16-c"]["C_empty_fdtd"]
    rel = abs(got - ref) / abs(ref)
    gates["S16-c"] = {"reference": ref, "measured": got, "relative_difference": rel,
                      "pass": rel <= 1e-12, "band": "<=1e-12 RELATIVE",
                      "platform": PLATFORM,
                      "note": "restated as relative and platform-named [docket 14]"}
    s16d_target = w_y_cells(20, 10, 40)
    hw = results["A-v2"]["half_width_1e2"]
    gates["S16-d"] = {"target_cells": s16d_target, "measured_cells": hw,
                      "rel_pct": 100.0 * abs(hw - s16d_target) / s16d_target,
                      "pass": 100.0 * abs(hw - s16d_target) / s16d_target <= 5.0,
                      "band": "<=5%", "width_passed": results and legs[4]["width"],
                      "note": "the oblique-width gate [docket 13] -- the only stage-16 gate "
                              "that could have failed on this cycle's own actual defect"}

    # ---- P-TH23-A5 scoring
    a5 = {}
    for leg in legs:
        if not leg["id"].startswith("A-v"):
            continue
        pred = leg["predicted_C_empty_propagator"]
        got = results[leg["id"]]["C_empty_fdtd"]
        a5[leg["id"]] = {
            "N_F": leg["N_F"], "predicted_propagator": pred, "measured_fdtd": got,
            "rel_pct": 100.0 * abs(got - pred) / abs(pred),
            "band_pct": leg["fdtd_vs_propagator_band_pct"],
            "sign_agrees": (pred < 0) == (got < 0),
            "pass": (100.0 * abs(got - pred) / abs(pred) <= leg["fdtd_vs_propagator_band_pct"])
                    and ((pred < 0) == (got < 0)),
            # ------------------------------------------------- [p5 docket 9]
            # RE-ISSUE IN THE CONDITIONED CURRENCY. C is a Weber contrast, and
            # the propagator/FDTD comparison is really a comparison of the
            # UNDERLYING window ratio 1+C. Near C -> -1 the two currencies
            # diverge by the conditioning factor 1/|1+C| -- which is the SAME
            # factor `run.py` already uses to DROP P-TH23-A7 as unusable. The
            # cycle applied its own disqualifying criterion to one prediction
            # and not to the neighbouring one at identical C_empty values.
            "predicted_1_plus_C": 1.0 + pred,
            "measured_1_plus_C": 1.0 + got,
            "rel_pct_in_1_plus_C": 100.0 * abs(got - pred) / abs(1.0 + pred),
            "conditioning_amplification_C_to_1plusC": abs(pred) / abs(1.0 + pred),
            "informative": abs(1.0 + pred) > 0.1}
    # ---- object-present legs: EXPLORATORY-NON-SCORING [docket 9]
    explor = {}
    for oid, eid in (("A-o1", "A-v2"), ("A-o2", "A-v3")):
        c_scene = results[oid]["C_empty_fdtd"]
        c_empty = results[eid]["C_empty_fdtd"]
        explor[oid] = {
            "C_scene_sponge": c_scene, "paired_empty_leg": eid, "C_empty": c_empty,
            "ratio_estimator_C_corr": (1.0 + c_scene) / (1.0 + c_empty) - 1.0,
            "conditioning_amplification": 1.0 / abs(1.0 + c_empty),
            "status": "EXPLORATORY-NON-SCORING [docket 9]: P-TH23-A7 is dropped; this "
                      "estimator is amplified by the factor printed above, so it carries "
                      "no band and scores nothing."}
    # The suite's own stage-16 gate b was AMENDED on first light (see
    # lab/validation/run_all.py::stage16_oblique_gaussian_source). The amended
    # gate is recorded HERE ALONGSIDE the pre-registered one, never in place of
    # it: P-TH23-A6's S16-b clause is scored against what was committed.
    d = gates["S16-b"]["post_run_diagnostic_nonparaxial"]["S16-b"]
    off = abs(d["fdtd_minus_exact_cells"]) / d["fdtd_half_width_1e2"]
    gates["S16-b-amended"] = {
        "band": "<=1.5% of the beam half-width from the EXACT angular-spectrum centre "
                "(line-current/flux model) [re-barred at Phase 5, p5 docket 1]",
        "measured_fraction_of_half_width": off, "pass": off <= 0.015,
        "measured_delta_cells": abs(d["fdtd_minus_exact_cells"]),
        "status": ("FIRST-LIGHT AMENDMENT, following stages 6/7/8/10's own recorded "
                   "first-run amendment convention, REPOINTED AND RE-BARRED at Phase 5 "
                   "[p5 docket 1-2]: the first-light comparator was itself physically "
                   "wrong (prescribed aperture field reduced with |E|^2, where this "
                   "engine impresses a line current and observer_profile reads a flux), "
                   "understating the engine by ~12x and leaving the bar ~17x too loose. "
                   "It does NOT retro-fit P-TH23-A6: the pre-registered S16-b clause "
                   "above stands as FAILED."),
    }
    for r in results.values():
        r["profile_plane_x"] = None      # keep results.json to a sane size
    # [p5 docket 9] A5 re-issued in the conditioned currency, as a block.
    a5_conditioned = {
        "statement": (
            "PHOTONICS, ELECTROMAGNETISM, THERMODYNAMICS and QUANTUM all independently "
            "correct, and Red Team confirms the arithmetic: A5's 'CONFIRMED 4/4' is 2 "
            "INFORMATIVE legs and 2 SATURATED ones by this cycle's own disqualifying "
            "criterion. Nothing is refuted -- 8.4% passes a 15% band -- but the headline "
            "'the cycle's genuine falsifiable Block-A content' overstates what 4/4 buys."),
        "per_leg": {lid: {"N_F": s["N_F"],
                          "rel_pct_in_C": s["rel_pct"],
                          "rel_pct_in_1_plus_C": s["rel_pct_in_1_plus_C"],
                          "conditioning_amplification_C_to_1plusC":
                              s["conditioning_amplification_C_to_1plusC"],
                          "informative": s["informative"]}
                    for lid, s in a5.items()},
        "n_informative": sum(1 for s in a5.values() if s["informative"]),
        "n_saturated": sum(1 for s in a5.values() if not s["informative"]),
        "learned_1_restated": (
            "[p5 docket 9] The propagator reproduces FDTD to <=0.80% at N_F ~ 54-66 and "
            "to ~8.4% at N_F ~ 0.5-2.2, where the reduction is ill-conditioned by 74-299x "
            "and should NOT be quoted in C. NOTE ALSO [PHOTONICS, upheld]: `_G0_for`'s "
            "validity parameter is kr, NOT N_F -- the module asserts kr > 50, set by D_SP "
            "and the window span, not by aperture width. 'Validated three orders of "
            "Fresnel number outside where it was built' is the wrong statement of what "
            "was earned; what was earned is a validation across N_F at fixed, "
            "always-satisfied kr."),
    }
    pre_registered = {k: v for k, v in gates.items() if not k.endswith("-amended")}
    return {"legs": results, "gates": gates, "P-TH23-A5": a5,
            "P-TH23-A5_conditioned_currency": a5_conditioned,     # [p5 docket 9]
            "exploratory_object_present": explor,
            "all_gates_pass": all(g["pass"] for g in pre_registered.values()),
            "all_gates_pass_with_first_light_amendment": all(
                g["pass"] for k, g in gates.items() if k != "S16-b"),
            "gate_disposition": (
                "P-TH23-A6 committed 'any gate fails => no Block-A number is reported at "
                "all'. One gate failed: S16-b. Applying that clause in SCOPE rather than "
                "as a blanket, and disclosing the judgment: S16-b measures beam POINTING, "
                "and its failure is attributed (post-run diagnostic, above) to its own "
                "ray-optics target being non-paraxial-invalid at 14deg divergence, not to "
                "the engine. The three gates that certify the WIDTH/propagator chain -- "
                "S16-a (free-space divergence identity, 1.06%), S16-c (absolute regression "
                "anchor, 7.0e-15 relative) and S16-d (the oblique-width gate, 1.25%) -- all "
                "pass, so P-TH23-A0/A2/A3/A5 are reported as trusted. The one reading that "
                "depends on where the beam POINTS, P-TH23-A1, is reported WITH the "
                "withholding clause applied: it is not gate-backed at this divergence. "
                "[p5 docket 5] THIS PARAGRAPH IS NO LONGER THE ONLY PLACE THE WITHHOLDING "
                "LIVES: A1's own prediction dict now carries a `gate_backing` key, this "
                "paragraph is printed to the console immediately after the gate table, and "
                "the scorecard cell reads 'WITHHELD -- not gate-backed (S16-b FAILED)'. "
                "[p5 docket 1-2] AND the attribution is corrected: 96.8% of the 12.974-cell "
                "failure is the gate's own ray-optics TARGET and 3.2% is the engine, not "
                "62/38 as committed -- see phase5_erratum."),
            "absorbing_boundary_systematic": ABSORB_SYSTEMATIC_NOTE,   # [p5 docket 19]
            "n_new_fdtd_calls": len(legs)}


# ====================================================================== output
def print_predictions(a, b, c):
    print("=" * 78)
    print("exp-046 -- PANEL ITERATION 23, PHASE 4 -- FROZEN PREDICTIONS")
    print("(computed with ZERO FDTD calls; committed to git before any Block-A leg runs)")
    print("=" * 78)
    print(f"platform: {PLATFORM}")
    print(f"\nNOTE (inlined at the point of claim [docket 21]): {NETD_DISCLAIMER}")

    print("\n--- BLOCK A: corrected geometry table (theta0 = 40 deg) [docket 3] ---")
    print(f"C = {C_COEF:.9f}   width_line = w0/cos(theta0) [docket 1]")
    print(f"{'lam':>5}{'FWHM':>5}{'w0':>9}{'w_line':>9}{'2w_line':>9}{'1504/2wl':>10}"
          f"{'zR_line':>10}{'w_y':>9}{'N_F':>8}{'(was)':>9}")
    for row in a["geometry_table_theta40"]:
        print(f"{row['lambda_nm']:>5}{row['fwhm_deg']:>5}{row['w0_cells']:>9.2f}"
              f"{row['w_line_cells']:>9.2f}{row['two_w_line_cells']:>9.2f}"
              f"{row['aperture_ratio_1504_over_2w_line']:>9.2f}x{row['z_R_line_cells']:>10.1f}"
              f"{row['w_y_cells']:>9.2f}{row['N_F']:>8.2f}"
              f"{row['N_F_superseded_w0_convention']:>9.2f}")
    print(f"  N_F span at theta0=40: {a['N_F_span_theta40'][0]:.2f} - {a['N_F_span_theta40'][1]:.2f}"
          f"   (all 36 cells: {a['N_F_span_all_cells'][0]:.2f} - {a['N_F_span_all_cells'][1]:.2f})")
    print(f"  aperture ratio span: {a['aperture_ratio_span_theta40'][0]:.2f}x - "
          f"{a['aperture_ratio_span_theta40'][1]:.2f}x")
    print(f"  {a['t21_3x_30x_citation_restated']}")
    print(f"  w_y slip [docket 2]: 450nm/FWHM2/40deg = "
          f"{a['w_y_slip_correction']['corrected']:.2f} (Phase 1 printed 199.33; "
          f"{a['w_y_slip_correction']['diagnosis']})")
    print(f"  idealization 2 [docket 12]: w0/lambda = "
          f"{a['idealization_2_restated']['w0_over_lambda_at_fwhm20']:.4f} lambda at FWHM=20 "
          f"for ALL three wavelengths (one value, not 1.07-1.34)")
    i4 = a["idealization_4_restated"]
    print(f"  idealization 4 [docket 11]: unaimed rim amplitude "
          f"{i4['unaimed_rim_amplitude_max']:.3e} / intensity "
          f"{i4['unaimed_rim_intensity_max']:.3e}; aimed truncation (FWHM=2 cells) "
          f"{i4['aimed_half_span_over_w_line_range_fwhm2_cells'][0]:.2f}-"
          f"{i4['aimed_half_span_over_w_line_range_fwhm2_cells'][1]:.2f} w_line, rim amp "
          f"{i4['aimed_rim_amplitude_max']:.3e}, {i4['n_aimed_cells_truncation_invalid']}/36 "
          f"aimed cells flagged truncation-INVALID")
    anc = a["envelope_anchor_accuracy"]
    print(f"  closed-form anchor accuracy [docket 4]: worst {anc['envelope_vs_propagator_rel_pct_max']:.1f}%, "
          f"median {anc['envelope_vs_propagator_rel_pct_median']:.2f}%, "
          f"per-FWHM worst {[f'{k}deg:{v:.1f}%' for k, v in anc['per_fwhm_worst'].items()]}")

    print("\n--- BLOCK A: committed prediction bands ---")
    for pid, p in a["predictions"].items():
        print(f"  {pid} [{p['class']}]")
        if "statement" in p:
            print(f"     statement: {p['statement']}")
        if "band" in p:
            print(f"     band: {p['band']}")
        for k, v in p.items():
            if k in ("class", "band", "statement"):
                continue
            print(f"     {k}: {v}")
    # ---------------- Phase-5 mandatory-fix docket, Block-A half -------------
    print("\n--- PHASE-5 MANDATORY-FIX DOCKET (same shift): Block A ---")
    sc = a["t21_permanent_fact_scope"]
    print(f"  [p5 6] T21 'permanent fact' SCOPED to the central lobe. At the 9 FWHM=20deg "
          f"cells\n         the synthesised aperture is a THREE-LOBE COMB: replicas at "
          f"{sc['fwhm20_replica_offset_cells'][0]:.0f}..{sc['fwhm20_replica_offset_cells'][1]:.0f} cells, "
          f"amplitude {sc['fwhm20_replica_amplitude'][0]:.3f}-{sc['fwhm20_replica_amplitude'][1]:.3f},\n"
          f"         carrying {sc['fwhm20_intensity_fraction_outside_3w_line_untapered_pct'][0]:.1f}"
          f"-{sc['fwhm20_intensity_fraction_outside_3w_line_untapered_pct'][1]:.1f}% of the intensity "
          f"outside +/-3 w_line (tapered "
          f"{sc['fwhm20_intensity_fraction_outside_3w_line_tapered_pct'][0]:.1f}"
          f"-{sc['fwhm20_intensity_fraction_outside_3w_line_tapered_pct'][1]:.1f}%);\n"
          f"         FWHM<=10deg worst {sc['fwhm_le10_intensity_fraction_outside_3w_line_pct_max']:.3f}%. "
          f"Single-transverse-mode at {sc['n_cells_single_transverse_mode']}/36 cells\n"
          f"         (criterion: {sc['single_transverse_mode_criterion']}).")
    for line in _wrap(sc["refinement_of_red_teams_own_table"], 70):
        print(f"         {line}")
    ra = a["predictions"]["P-TH23-A3"]["residual_attribution"]
    print(f"  [p5 7] A3 residual is NOT taper truncation. QUANTUM's closed form "
          f"1/sqrt(1-4 sigma_th^2 tan^2 th0):\n"
          f"         FWHM=10/th0=40 predicted {ra['predicted_pct_at_fwhm10_theta40']:.3f}% · "
          f"FWHM=20/th0=40 predicted {ra['predicted_pct_at_fwhm20_theta40']:.3f}%; "
          f"worst |pred-meas| over 36 cells {ra['predicted_vs_measured_pct_worst_abs_error']:.3f} pp.\n"
          f"         Residual cubic phase (aberration) by FWHM: "
          + " · ".join(f"{k}deg {v:.3f} rad" for k, v in ra["residual_cubic_phase_rad_max_by_fwhm"].items()))
    nc = a["angular_sampling_convergence"]
    print(f"  [p5 8] A4's MECHANISM restored as real: n=41 -> n=401 moves the scored "
          f"C_empty by\n         {nc['worst_rel_move_committed_convention_pct']:.3f}% worst "
          f"(cell {nc['worst_cell_committed_convention']}), committed convention; "
          f"{nc['worst_rel_move_corrected_convention_pct']:.3f}% worst corrected.\n"
          f"         `gaussian_angle_weights(n=41)` had NEVER been convergence-checked. "
          f"New open item for Iteration 24.")
    ch = a["idealization_2_restated"]["chromatic_dependence_corrected"]
    print(f"  [p5 10] idealization 2's 'consequently no material wavelength dependence' is "
          f"STRUCK:\n          {ch['n_cells_positive_C']} of {ch['n_of']} cells read POSITIVE C "
          f"(a glint), a SIGN REVERSAL across the visible band at\n"
          f"          {len(ch['sign_reversal_rows_across_the_visible_band'])} of 12 "
          f"(theta0, FWHM) rows. A1's 'C -> -1 regardless of coherence' is contradicted there.")
    i4 = a["idealization_4_restated"]["c_thr_comparison_withdrawn"]
    print(f"  [p5 11] idealization 4's C_THR comparison WITHDRAWN: rim amplitude "
          f"{i4['unaimed_rim_amplitude_vs_C_THR']},\n          rim intensity "
          f"{i4['unaimed_rim_intensity_vs_C_THR']} -- and a source-plane field residual is "
          f"not a Weber contrast\n          in either direction (category error). "
          f"C_THR comment verbatim: '{C_THR_COMMENT}'")
    q = a["quantum_iteration20_conjecture_disposition"]
    print(f"  [p5 18] QUANTUM's Iteration-20 conjecture, recorded accurately:\n"
          f"          premise: {q['premise'][:150]}...\n"
          f"          prediction: {q['prediction'][:120]}...\n"
          f"          'mis-posed' belongs to: {q['mis_posed_belongs_to']}")

    print("\n  FDTD legs to be run (widths per [docket 1]):")
    for leg in a["fdtd_legs"]:
        print(f"    {leg['n']}. {leg['id']:6s} lam={leg['lambda_nm']} th0={leg['theta0_deg']:+.0f} "
              f"profile={leg['profile']:5s} width="
              + (f"{leg['width']:.3f}" if leg["width"] else "n/a")
              + (f"  N_F={leg['N_F']:.2f}" if "N_F" in leg else "")
              + (f"  C_pred={leg['predicted_C_empty_propagator']:+.6f}"
                 if "predicted_C_empty_propagator" in leg else "")
              + (f"  sigma={leg['sigma']:.6e}" if leg.get("sigma") else ""))

    print("\n--- BLOCK B: T23's mixed length-scale regime (desk) ---")
    print(f"{'quantity':>26}{'w_on-consistent':>20}{'r_out-consistent':>20}{'MIXED (T23)':>20}")
    keys = [("h_eff_w_m2k", "h_eff (W/m^2K)"), ("area_m2", "area (m^2)"),
            ("mass_kg", "mass (kg)"), ("dp_dt_w_k", "dP/dT (W/K)"),
            ("p_abs_w", "P_abs (W)"), ("dt_ss_full_K", "dt_ss_full (K)"),
            ("tau_thermal_s", "tau_thermal (s)"), ("dwell_over_tau_thermal", "dwell/tau_thermal"),
            ("biot_number", "Biot"), ("knudsen_number", "Knudsen"),
            ("h_eff_slip_corrected_w_m2k", "h_eff slip-corrected"),
            ("netd_lo_over_dt_ss_full", "NETD_lo/dt_ss_full")]
    for key, label in keys:
        print(f"{label:>26}{b['regimes']['w_on_consistent'][key]:>20.10g}"
              f"{b['regimes']['r_out_consistent'][key]:>20.10g}"
              f"{b['regimes']['mixed_w_power_r_cond'][key]:>20.10g}")
    print(f"  exp-045 reproduction self-check (max rel): "
          f"{max(b['exp045_reproduction_selfcheck_rel'].values()):.2e}")
    print(f"  silicon identity: {SILICON_PROVENANCE} [docket 18]")
    print(f"  {b['tau_thermal_structure_note']}")
    print("  rho*C_P / fill-factor sensitivity [docket 19]:")
    for row in b["rho_cp_sensitivity"]:
        print(f"    scale {row['rho_cp_scale_or_fill_factor']:>5}: tau_th="
              f"{row['tau_thermal_s']:.6e}s  dwell/tau_th={row['dwell_over_tau_thermal']:.3f}"
              f"  above N_TRANSIENT_TAU=25: {row['above_N_TRANSIENT_TAU_25']}")
    for pid, p in b["predictions"].items():
        print(f"  {pid}: {p['statement']}")
        print(f"     band: {p['band']}")
        for k, v in p.items():
            if k in ("statement", "band"):
                continue
            print(f"     {k}: {v}")

    # ---------------- Phase-5 mandatory-fix docket, Block-B half -------------
    print("\n--- PHASE-5 MANDATORY-FIX DOCKET (same shift): Block B ---")
    em = b["emissivity_disclosure"]
    print(f"  [p5 16] emissivity: the radiative channel is "
          f"{em['radiative_share_of_dP_dT_pct']:.4f}% of dP/dT "
          f"({em['radiative_channel_w_m2k']:.4f} vs {em['conduction_channel_h_eff_w_m2k']:.2f} "
          f"W/m^2K).")
    for row in em["rows"]:
        print(f"          eps={row['emissivity']:<6}: dt_ss={row['dt_ss_full_K']:.6e} K  "
              f"inflation {row['dt_ss_inflation_vs_committed']:.6f}x  "
              f"NETD_lo/dt_ss {row['netd_lo_over_dt_ss_full']:.2f}x")
    print("          MATERIALS' '~4x' estimate is wrong by ~4 orders, in the safe "
          "direction; conclusion holds a fortiori.")
    print("  [p5 15] fill-factor validity conditions (Maxwell-Garnett kappa_eff, "
          "Bi = k_air/kappa_eff):")
    for row in b["rho_cp_sensitivity"]:
        print(f"          phi={row['rho_cp_scale_or_fill_factor']:<5}: "
              f"kappa_eff={row['kappa_eff_w_mk']:.4g} W/mK  Bi={row['biot_number']:.4g}  "
              f"Kn={row['knudsen_number']:.4g}  lumped single-tau valid: "
              f"{row['lumped_single_tau_valid_Bi_lt_0p1']}")
    print("          The reassurance is largest precisely where the lumped model that "
          "produced it is most invalid.")
    t23 = b["t23_disposition"]
    print(f"  [p5 14] T23 DISPOSITION (was recorded nowhere durable): {t23['ruling']}")
    for line in _wrap(t23["honest_split"], 72):
        print(f"          {line}")
    print(f"  [p5 17] P-TH23-B1 tagged: {b['predictions']['P-TH23-B1']['class']}")

    print("\n--- BLOCK C: dose accumulation on the FULL exp-038 grid (desk) ---")
    print(f"  {c['grid_note']}")
    print(f"  point runs (new points x 2 gaps): {c['n_point_runs']}")
    print(f"  C3 duration scan [docket 17]: {c['c3_duration_scan']['n_points']} points, "
          f"closed-form agreement {c['c3_duration_scan']['closed_form_agreement']}")
    for pid, p in c["predictions"].items():
        print(f"  {pid}: {p['statement']}")
        print(f"     band: {p['band']}")
        for k, v in p.items():
            if k in ("statement", "band"):
                continue
            print(f"     {k}: {v}")
    # ---------------- Phase-5 mandatory-fix docket, program-integrity half ---
    print("\n--- PHASE-5 MANDATORY-FIX DOCKET (same shift): program integrity ---")
    print("  [p5 4] THE ITEM-24 HARDENED RULE, in ONE rendering (canonical string; "
          "propagated\n         verbatim to NOTES.md and to LOGBOOK's Iteration-23 close):")
    for line in _wrap(ITEM_24_HARDENED_RULE, 72):
        print(f"         {line}")
    print("  [p5 20] " + _wrap(POST_FREEZE_GATE_TARGET_RULE, 70)[0])
    for line in _wrap(POST_FREEZE_GATE_TARGET_RULE, 70)[1:]:
        print(f"          {line}")
    print("  [p5 19] NEW LIVE THREAD — the C_empty channel's ABSORB systematic:")
    for line in _wrap(ABSORB_SYSTEMATIC_NOTE, 70):
        print(f"          {line}")
    print(f"\nNOTE (repeated at the point of claim [docket 21]): {NETD_DISCLAIMER}")
    print("=" * 78)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--predict-only", action="store_true",
                    help="compute and print every P-TH23-* band with ZERO FDTD calls")
    args = ap.parse_args()

    t0 = time.time()
    a = block_a_desk()
    b = block_b_desk()
    c = block_c_desk(b)
    print_predictions(a, b, c)
    print(f"\ndesk work: {time.time() - t0:.2f}s, 0 FDTD calls")

    if args.predict_only:
        print("--predict-only: no FDTD leg executed, no results.json written.")
        return

    fd = run_block_a_fdtd(a)

    print("\n--- stage-16 gates (this run's own self-check) ---")
    for gid, g in fd["gates"].items():
        print(f"  [{'PASS' if g['pass'] else 'FAIL'}] {gid}: " +
              ", ".join(f"{k}={v}" for k, v in g.items()
                        if k in ("worst_rel_pct", "delta_cells", "relative_difference",
                                 "rel_pct", "measured_cells", "target_cells",
                                 "measured_center", "target_center", "measured", "band")))
    # [p5 docket 5] The Director-level withholding judgment is PRINTED here,
    # immediately after the gate table, not left to a key nobody reads.
    print("\n  GATE DISPOSITION (P-TH23-A6's withholding clause) [p5 docket 5]:")
    for line in _wrap(fd["gate_disposition"], 74):
        print(f"    {line}")
    print("\n--- P-TH23-A5: FDTD vs the desk propagator ---")
    for lid, s in fd["P-TH23-A5"].items():
        print(f"  [{'PASS' if s['pass'] else 'FAIL'}] {lid}: N_F={s['N_F']:.2f} "
              f"pred={s['predicted_propagator']:+.6f} fdtd={s['measured_fdtd']:+.6f} "
              f"rel={s['rel_pct']:.2f}% (band {s['band_pct']:.0f}%) sign_ok={s['sign_agrees']}")
    # [p5 docket 9] the same four legs in the conditioned currency
    print("  in the conditioned currency (1+C) [p5 docket 9]:")
    for lid, s in fd["P-TH23-A5_conditioned_currency"]["per_leg"].items():
        print(f"    {lid}: N_F={s['N_F']:6.2f}  rel in C {s['rel_pct_in_C']:6.3f}%  "
              f"rel in 1+C {s['rel_pct_in_1_plus_C']:6.3f}%  amplification "
              f"{s['conditioning_amplification_C_to_1plusC']:7.1f}x  "
              f"{'INFORMATIVE' if s['informative'] else 'SATURATED'}")
    print(f"    -> {fd['P-TH23-A5_conditioned_currency']['n_informative']} informative, "
          f"{fd['P-TH23-A5_conditioned_currency']['n_saturated']} saturated")
    print("\n--- object-present legs (EXPLORATORY-NON-SCORING [docket 9]) ---")
    for oid, s in fd["exploratory_object_present"].items():
        print(f"  {oid}: C_scene={s['C_scene_sponge']:+.6f} vs empty {s['C_empty']:+.6f} "
              f"-> C_corr={s['ratio_estimator_C_corr']:+.4f} "
              f"(amplification {s['conditioning_amplification']:.0f}x)")

    # ======================================================================
    # [p5 docket 2] FLAG, DON'T REWRITE (exp-042's own precedent): the Phase-4
    # record's S16-b attribution is left standing as committed, and this key
    # carries the correction. Numbers are recomputed here from the corrected
    # comparator, never hand-typed.
    d_s16b = fd["gates"]["S16-b"]["post_run_diagnostic_nonparaxial"]["S16-b"]
    ex_s16b = d_s16b["exact_angular_spectrum"]
    ray_ctr = fd["gates"]["S16-b"]["target_center"]
    fdtd_ctr = fd["gates"]["S16-b"]["measured_center"]
    fdtd_hw = d_s16b["fdtd_half_width_1e2"]
    target_err = abs(ex_s16b["center_1e2_midpoint"] - ray_ctr)
    engine_err = abs(fdtd_ctr - ex_s16b["center_1e2_midpoint"])
    total_err = abs(fdtd_ctr - ray_ctr)
    peak_err = abs(ex_s16b["peak_cell"] - ray_ctr)
    superseded = ex_s16b["superseded_field_aperture_E2"]
    phase5_erratum = {
        "convention": ("FLAG, DON'T REWRITE (T10; exp-042's own phase5_erratum "
                       "precedent). Nothing in the Phase-4 record above is edited; "
                       "this key states what is superseded and by what."),
        "s16b_attribution_corrected": {                       # [p5 docket 2]
            "committed_at_phase_4": {"target_error_cells": 8.03, "engine_error_cells": 4.95,
                                     "share": "62% target / 38% engine"},
            "corrected": {
                "target_error_cells": target_err,
                "engine_error_cells": engine_err,
                "total_cells": total_err,
                "target_share_pct": 100.0 * target_err / total_err,
                "engine_share_pct": 100.0 * engine_err / total_err,
                "engine_error_as_fraction_of_beam_half_width_pct":
                    100.0 * engine_err / fdtd_hw},
            "why": ("The Phase-4 diagnostic's comparator propagated the aperture as a "
                    "prescribed FIELD and reduced it with |E|^2. This bench impresses a "
                    "line CURRENT (lab/fdtd2d.py:232-237 -> spectrum carries 1/k_x) and "
                    "`ambient.observer_profile` reads a FLUX (lab/ambient.py:36-39 -> "
                    "obliquity k_x/k enters once, via H). Two missing obliquities in "
                    "opposite directions; they do not cancel. Fourth appearance of the "
                    "error species LOGBOOK T21 records from Iteration 19, and the first "
                    "inside lab/."),
            "superseded_comparator_reading": superseded,
            "estimator_skew_decomposition": {
                "note": ("Under a PEAK estimator -- which is what ray optics actually "
                         "predicts, a stationary-phase ray -- the exact/ray-optics gap is "
                         "only the figure below. So the 12.97 cells decompose as "
                         "~estimator/skew mismatch + ~genuine non-paraxial target error + "
                         "~engine, and NOTES.md Learned #2 and idealization 2 name the "
                         "right species while assigning it ~4x too much of the effect and "
                         "none to the estimator pairing that dominates."),
                "peak_estimator_exact_vs_ray_optics_cells": peak_err,
                "exact_peak": ex_s16b["peak_cell"],
                "fdtd_peak_cell": d_s16b["fdtd_peak_cell"],
                "ray_optics_center": ray_ctr,
                "estimator_skew_cells": total_err - peak_err - engine_err,
                "genuine_nonparaxial_target_error_cells": peak_err,
                "engine_cells": engine_err},
            "shipped_8pct_bar_would_have_failed": {
                "cell": "Block A's own extreme: FWHM=20deg, theta0=40deg, 600nm, "
                        "width = w0/cos(theta0) = 28.03",
                "fdtd_center_half_width": [1005.549, 120.776],
                "shipped_comparator_center": 994.223,
                "offset_vs_8pct_bar_pct": 9.38,
                "verdict": "FAIL -- and it would have blamed the engine",
                "correct_comparator_center": 1005.090,
                "true_engine_offset_pct": 0.38,
                "source": ("Red Team's own new FDTD run (`rt_extreme.py`), cited as its "
                           "measurement; not re-run this shift -- this close carries no "
                           "new FDTD budget. The corrected comparator's 1005.090 IS "
                           "reproduced here by `exact_angular_spectrum_center(28.03, 40, "
                           "20)`."),
                "correct_comparator_reproduced_here":
                    exact_angular_spectrum_center(
                        w_line_cells(20, 20, 40), 40.0, dg.CPL[600])["center_1e2_midpoint"]},
            "suite_gate_repointed": (
                "lab/validation/run_all.py stage 16 gate (b) is repointed to the "
                "line-current/flux comparator and re-barred at <=1.5% of the beam "
                "half-width (measured 0.46%), with a new desk-only acceptance gate (b2) "
                "requiring agreement with an INDEPENDENT real-space Huygens derivation "
                "(measured 0.030 cells in centre, 0.011 in half-width). Stage 16 is now "
                "5/5. [p5 docket 1]"),
        },
        "a1_disposition": {                                    # [p5 docket 5]
            "scorecard_cell": "WITHHELD -- not gate-backed (S16-b FAILED)",
            "scorecard_tally": "11 CONFIRMED / 2 PARTIAL / 1 WITHHELD / 1 REFUTED / "
                               "2 DROPPED",
            "note": ("A1 is dropped from the PARTIAL count: a reading the Director has "
                     "withheld must not be counted in the cycle's own success tally, and "
                     "the Phase-4 cell 'PARTIAL (computed in band; withheld as "
                     "gate-backed)' parses literally as the inverse of its intent -- "
                     "which matters because LOGBOOK entries are built by copying "
                     "scorecard rows."),
            "post_fix_status": ("Once p5 docket items 1-2 land -- and they land in this "
                                "same commit -- the repointed S16-b PASSES at 0.46% "
                                "(0.418 cells on a 90.99-cell half-width), so the "
                                "pointing chain IS validated at 600nm/40deg and A1 is "
                                "restored as an explicitly-labelled DESK GEOMETRY READING "
                                "that is gate-backed at that configuration. It stays out "
                                "of the CONFIRMED column: it was never an experimental "
                                "adjudication of coherence, and its own mechanism "
                                "sentence is contradicted at the 4 positive-C cells "
                                "[p5 docket 10]."),
        },
        "item_24_hardened_rule": ITEM_24_HARDENED_RULE,         # [p5 docket 4]
        "item_24_rule_correction_note": ITEM_24_RULE_CORRECTION_NOTE,
        "only_flag_erratum_corrected": (                        # [p5 docket 12]
            "[p5 docket 12] VALIDATION.md's and NOTES.md Learned #5's `--only` erratum "
            "over-claimed its own blast radius. The exact-match rule that caused the "
            "packed-token regression landed at commit 6082e02, 2026-08-17. Running the "
            "PRE-6082e02 `_stage_selected` against `--only 12346789,10,11` selects "
            "{1,2,3,4,6,7,8,9,10,11} -- the intended ten stages. All five SESSION_LOG "
            "citations of that invocation (lines 1026/1155/1253/1347/1455) sit under "
            "headers dated 2026-08-14/15 (Iterations 7-11, exp-030/031/032/033/034) and "
            "were correct under the code in force. The regression affects "
            "POST-2026-08-17 invocations only, NONE of which was ever cited: no "
            "published trust-suite citation in this program's history was damaged. The "
            "`--only 16 -> {1,6,16}` and `--only 12 -> {1,2,12}` halves are correct and "
            "the fix itself is right. Corrected in VALIDATION.md and NOTES.md before it "
            "reached LOGBOOK."),
        "docket_21_override_stated": (                          # [p5 docket 13]
            "[p5 docket 13] STATED AS AN OVERRIDE, per this program's own rule that an "
            "overridden docket item is stated as overridden rather than silently "
            "narrowed: Phase-2 docket item 21 asked for the NETD disclaimer at every "
            "point of claim. It is applied at every point of claim in C2 and C5 and at "
            "block scope for C1 and C4, because C1 and C4 issue NO detectability claim of "
            "their own -- they count memory point-runs and realizability tiers -- and a "
            "per-point disclaimer on a key that makes no detectability claim is noise, "
            "not disclosure. The block-scope key carries it. This was an override, not a "
            "delivery, and was not stated as one at Phase 4."),
        "netd_disclaimer_coverage_corrected": None,             # filled in below
        "absorbing_boundary_systematic": ABSORB_SYSTEMATIC_NOTE,      # [p5 docket 19]
        "post_freeze_gate_target_rule": POST_FREEZE_GATE_TARGET_RULE,  # [p5 docket 20]
        "phase1_proposal_superseded_banner": (                  # [p5 docket 3]
            "[p5 docket 3] `phase1_proposal.md` now carries a SUPERSEDED banner in "
            "exp-045's own form (commit f48de18), naming: 'eye-invisible' (section 1 and "
            "P-TH23-B3), section 2.1's geometry table, section 1's N_F range, "
            "idealizations 2 and 4, the 'sourced' silicon label, and predictions "
            "A3/A4/A7. NOTES.md's 'struck everywhere' is corrected to 'struck from every "
            "live artifact and every committed result; the Phase-1 draft is preserved "
            "unedited under a SUPERSEDED banner'. The NETD_DISCLAIMER constant now reads "
            "'in any committed result of this cycle', not 'anywhere in this cycle'. The "
            "SUBSTANTIVE half of Phase-2 docket 20 was already delivered -- no live "
            "artifact, no scored prediction, no committed result carries a perceptual "
            "claim -- what was false was the DELIVERY CLAIM, and the house remedy "
            "(invented one cycle earlier at exp-045, for this exact failure mode) had "
            "not been applied."),
        "tier0_items_landed": [1, 2, 3, 4, 5],
        "tier1_items_landed": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
        "disclosed_scope_calls": (
            "Two calls the Phase-5 docket does not fully resolve, disclosed rather than "
            "smoothed over (this program's convention). (1) Items 4, 19 and 20 each say "
            "'propagate to LOGBOOK's Iteration-23 close'; that close is not yet written, "
            "so the strings are made canonical HERE and in NOTES.md and are the text to "
            "carry at close -- no partial LOGBOOK entry is invented by this shift. "
            "(2) Item 1's mandatory acceptance test must reproduce exp-042's `_G0_for` + "
            "`field_and_h`, but VALIDATION's own rule is that the suite depends on no "
            "experiment directory; the propagator is therefore RE-DERIVED inside "
            "run_all.py from the geometry constants, which reproduces exp-042's numbers "
            "exactly AND doubles as the independent second derivation docket item 20 "
            "requires."),
    }

    out = {
        "experiment": "exp-046",
        "panel_iteration": 23,
        "lead_seat": "THERMODYNAMICS",
        "phase": "4 (TEST) + Phase-5 mandatory-fix close (same shift)",
        "phase5_erratum": phase5_erratum,
        "docket": ("all 23 substantive items of phase2_redteam_audit.md's mandatory-fix "
                   "docket applied; item 24 is a standing program-integrity rule (as "
                   "REPAIRED at Phase 5, p5 docket 4). PLUS all 20 items of "
                   "phase5_redteam_audit.md section 8's mandatory-fix docket, applied in "
                   "the same shift as the audit that raised them: Tier 0 (1-5, "
                   "checkpoint-criterion-4-conditional) and Tier 1 (6-20). Marked "
                   "[p5 docket N] at the point of application; see `phase5_erratum`."),
        "platform": PLATFORM,
        "meta": {"elapsed_s": time.time() - t0,
                 "n_new_fdtd_calls": fd["n_new_fdtd_calls"],
                 "trust_suite": "lab/validation/run_all.py stage 16 (new this cycle) plus the "
                                "full fast suite; stage 16's oblique-width gate is the "
                                "absolute-identity-adjacent gate PANEL.md's new-machinery "
                                "rule requires"},
        "block_a_aperture_consistent_beam": a,
        "block_a_fdtd": fd,
        "block_b_mixed_length_scale_regime": b,
        "block_c_dose_accumulation_full_grid": c,
        "netd_disclaimer_ALL_CLAIMS": NETD_DISCLAIMER,
    }
    # [p5 docket 13] Idealization 10's per-point claim, CORRECTED and COMPUTED.
    # The claim "stored per point at all 2496 + 42 + 250 points" is false: the
    # 250 duration-scan points carry no NETD classification and need none. The
    # true figure is the number of `netd_disclaimer` keys actually emitted,
    # counted here on the serialized document rather than asserted. Counting
    # BEFORE this key is inserted is exact: the key's value is an integer, so
    # inserting it adds no further instance of the disclaimer string.
    blob = json.dumps(out, indent=1, default=float)
    phase5_erratum["netd_disclaimer_coverage_corrected"] = {
        "n_netd_disclaimer_keys": blob.count('"netd_disclaimer"'),
        "n_disclaimer_string_instances": blob.count(NETD_DISCLAIMER[:60]),
        "block_b_regrowth_points_with_classification":
            len(b["block_a_regrowth"]["points"]),
        "block_c_point_runs_with_classification": c["n_point_runs"],
        "c3_duration_scan_points_without_classification":
            c["c3_duration_scan"]["n_points"],
        "statement": (
            "[p5 docket 13] NOTES.md idealization 10 claims the disclaimer is stored "
            "'per point at all 2496 + 42 + 250 points'. The 250 duration-scan points "
            "carry NO NETD classification -- they scan a memory ratio, not a "
            "temperature -- and need none. The count above is the number of "
            "`netd_disclaimer` keys the document actually carries, computed on the "
            "serialized document, not asserted."),
    }
    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(out, f, indent=1, default=float)
    print(f"\nresults.json written ({time.time() - t0:.1f}s total, "
          f"{fd['n_new_fdtd_calls']} new FDTD calls)")


if __name__ == "__main__":
    main()
