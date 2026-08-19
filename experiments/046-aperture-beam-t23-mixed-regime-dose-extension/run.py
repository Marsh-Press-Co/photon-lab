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
    "no 'eye-invisible' claim is made anywhere in this cycle [docket 20].")
C_THR_COMMENT = ("VISION's T2 photopic C_thr -- context only, this leg scores "
                 "no perceptual pass/fail")   # verbatim from 042/run.py:41 [docket 5]
SILICON_PROVENANCE = "ASSUMED -- provenance terminates unsourced (T18)"  # [docket 18]

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
        "idealization_2_restated": {
            "w0_over_lambda_all_cells": sorted({round(c["w0_over_lambda"], 6) for c in cells}),
            "w0_over_lambda_at_fwhm20": w0_cells(20, 20) / 20.0,
            "statement": ("w0/lambda = C/Delta-theta is LAMBDA-INDEPENDENT: the FWHM=20deg "
                          "waist is 1.0737*lambda at all three wavelengths, one value, not "
                          "1.07-1.34. Consequently Block A's 3-lambda sweep carries NO "
                          "material wavelength dependence beyond fixed cell geometry "
                          "[docket 12].")},
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
                          "~1e-2 in amplitude / ~1e-4 in intensity -- still below "
                          "C_THR=0.005 but WITHOUT the four-orders margin the Phase-1 "
                          "idealization claimed. The aimed leg truncates at 1.61-2.96 "
                          "w_line with rim amplitude up to 7.4e-2; cells with rim "
                          "amplitude > 1e-2 are flagged truncation-INVALID and are "
                          "excluded from every aimed-leg summary rather than the whole "
                          "aimed leg being dropped [docket 11].")},
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
                        "incoherent reading; min|C| >= 0.03"},
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
                        "<=4% at all 9 FWHM=20deg cells (taper truncation). Grid-quantized "
                        "crossing reported alongside because it reproduces Red Team's own "
                        "measurement cell-for-cell",
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
            "P-TH23-A4": {"class": "DROPPED [docket 7]",
                          "statement": "Premise false under the corrected width: there is no "
                                       "large FWHM=20deg divergence to explain as 41-point "
                                       "angular aliasing."},
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
    rho_cp_sensitivity = []
    for phi in (1.0, 0.5, 0.1, 0.01):
        tau = regime_mixed["tau_thermal_s"] * phi
        rho_cp_sensitivity.append({
            "rho_cp_scale_or_fill_factor": phi,
            "tau_thermal_s": tau, "dwell_over_tau_thermal": DWELL_S / tau,
            "above_N_TRANSIENT_TAU_25": DWELL_S / tau >= kin.N_TRANSIENT_TAU,
            "dt_ss_full_K_unchanged": regime_mixed["dt_ss_full_K"]})

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
                     "assumption seen from two sides [docket 19].")},
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
                                                    - regime_r["dwell_over_tau_thermal"])},
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
           "C_empty_fdtd": _weber_of(prof),           # [docket 15] scalars only
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
        print(f"  [{leg['n']}/{len(legs)}] {leg['id']:6s} "
              f"lam={leg['lambda_nm']} th={leg['theta0_deg']:+.0f} "
              f"{'width=%.3f' % leg['width'] if leg['width'] else 'plane'}"
              f"  C_empty={r['C_empty_fdtd']:+.6f}  ({r['elapsed_s']:.1f}s)", flush=True)

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
                      "pass": abs(ctr - target_center) <= 2.0, "band": "+/-2 cells"}
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
                    and ((pred < 0) == (got < 0))}
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
    for r in results.values():
        r["profile_plane_x"] = None      # keep results.json to a sane size
    return {"legs": results, "gates": gates, "P-TH23-A5": a5,
            "exploratory_object_present": explor,
            "all_gates_pass": all(g["pass"] for g in gates.values()),
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
    print("\n--- P-TH23-A5: FDTD vs the desk propagator ---")
    for lid, s in fd["P-TH23-A5"].items():
        print(f"  [{'PASS' if s['pass'] else 'FAIL'}] {lid}: N_F={s['N_F']:.2f} "
              f"pred={s['predicted_propagator']:+.6f} fdtd={s['measured_fdtd']:+.6f} "
              f"rel={s['rel_pct']:.2f}% (band {s['band_pct']:.0f}%) sign_ok={s['sign_agrees']}")
    print("\n--- object-present legs (EXPLORATORY-NON-SCORING [docket 9]) ---")
    for oid, s in fd["exploratory_object_present"].items():
        print(f"  {oid}: C_scene={s['C_scene_sponge']:+.6f} vs empty {s['C_empty']:+.6f} "
              f"-> C_corr={s['ratio_estimator_C_corr']:+.4f} "
              f"(amplification {s['conditioning_amplification']:.0f}x)")

    out = {
        "experiment": "exp-046",
        "panel_iteration": 23,
        "lead_seat": "THERMODYNAMICS",
        "phase": "4 (TEST)",
        "docket": ("all 23 substantive items of phase2_redteam_audit.md's mandatory-fix "
                   "docket applied; item 24 is a standing program-integrity rule"),
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
    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(out, f, indent=1, default=float)
    print(f"\nresults.json written ({time.time() - t0:.1f}s total, "
          f"{fd['n_new_fdtd_calls']} new FDTD calls)")


if __name__ == "__main__":
    main()
