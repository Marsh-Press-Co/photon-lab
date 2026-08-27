"""
experiments/080-t28-y-wall-planewave-validity-precheck/validity_precheck.py
=============================================================================
Panel Iteration 57 (exp-080). Lead: ELECTROMAGNETISM, by rotation. Executes
EM's own PRE-REGISTERED (phase1_proposal.md, frozen before this file was
written) validity pre-check of the plane-wave/global-steering y-wall
construction Red Team's exp-079 Phase-5 final audit (Sec 3, Sec 7 Tier-0
item 1) recommends building next, and PHOTONICS' own Phase-5 review (Sec 4)
sketched a concrete build for.

ZERO new FDTD calls. Imports, never reimplements:
  - experiments/065-.../design_geometry.py (dg065): CONFIGS -- raw geometry
    (aperture_cells, d_sp, obj_y, y_lo/y_hi, absorb) per congruent config.
  - experiments/075-.../boundary_reflectance.py (br): CPL (lambda=CPL[600]),
    damp_e_profile/nu_profile/n_profile_exact (the already-gated per-ABSORB
    complex index profile).
  - experiments/079-.../y_wall_aperture_sum.py (ywas): theta_local_deg,
    dist_image_cells, aperture_amplitude, source_driven_phase,
    reflection_coefficient_vec, build_aperture_grid, echo_field_curve,
    _trapz, K600, CONGRUENT_KEYS -- all already gated in that file's own
    main() (G-LOSSLESS/G-N1/G-PASSIVITY, a bit-exact vectorized-vs-scalar
    validation). Nothing here reimplements any of that physics.

Two parts, exactly as pre-registered in phase1_proposal.md Sec 4 (thresholds
and predictions frozen and pushed BEFORE this file existed):

  (a) FRAUNHOFER/FAR-FIELD MARGIN + theta_local SPREAD. W, lambda, Fraunhofer
      distance d_F=W^2/lambda; actual dist_image(y_s) at the aperture edges
      (y_lo,y_hi) per congruent config; the ratio dist_image/d_F; and the
      theta_local(y_s) envelope spread. Scored against the pre-registered
      FORECLOSE / MARGINAL / DOES-NOT-FORECLOSE thresholds.

  (b) SINGLE-ANGLE REPRODUCTION TEST. A single-angle variant of
      echo_field_curve: r(theta_eff;ABSORB) applied as ONE constant complex
      scalar (not the per-point r(theta_local(y_s)) the true model uses),
      for two theta_eff definitions (PRIMARY: amplitude-weighted mean over
      the native aperture grid; SECONDARY/robustness: aperture-midpoint
      value theta_local(OBJ_Y)). Compared against the TRUE per-point curve
      already committed in
      experiments/079-.../y_wall_aperture_sum_results.json's
      `primary_model_curves` key, via R^2, per config, both proxies (Re
      PRIMARY / |.| SECONDARY, this sub-thread's own house convention). A
      version-drift guard recomputes the true per-point curve fresh from
      ywas.echo_field_curve and asserts it matches the committed JSON to
      float precision before any R^2 is trusted.

Run: `python3 validity_precheck.py` from this directory (or anywhere --
paths resolve from __file__). Writes `validity_precheck_results.json` and
prints every table below; every number appended to phase1_proposal.md's
"PHASE 1 RESULTS (post-freeze)" section is copied from that JSON/stdout,
never hand-typed (R4).
"""

import importlib.util
import json
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, ROOT)


def _load(path, name):
    """House `_load()` pattern (boundary_reflectance.py / y_wall_prescreen.py
    / y_wall_aperture_sum.py's own convention) for filename collisions
    across experiment directories."""
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


EXP065_DIR = os.path.join(ROOT, "experiments", "065-t24-absorb-boundary-sweep")
EXP075_DIR = os.path.join(ROOT, "experiments", "075-t28-absorb-boundary-wkb-reflectance")
EXP076_RESULTS = os.path.join(ROOT, "experiments", "076-t28-g40-pad-decorrelation", "results.json")
EXP079_DIR = os.path.join(ROOT, "experiments", "079-t28-y-wall-full-aperture-sum")

dg065 = _load(os.path.join(EXP065_DIR, "design_geometry.py"), "_exp080_dg065")
br = _load(os.path.join(EXP075_DIR, "boundary_reflectance.py"), "_exp080_br")
ywas = _load(os.path.join(EXP079_DIR, "y_wall_aperture_sum.py"), "_exp080_ywas")

CONGRUENT_KEYS = ywas.CONGRUENT_KEYS  # ("C40","C60","C70","C80","G40")
LAM600 = br.CPL[600]

with open(os.path.join(EXP079_DIR, "y_wall_aperture_sum_results.json")) as f:
    EXP079_RESULTS = json.load(f)

# ------------------------------------------------- pre-registered thresholds
# phase1_proposal.md Sec 4a (part a) -- frozen and pushed before this file
# existed (commit 6fb6b99).
FORECLOSE_RATIO = 0.10
DOESNOT_RATIO = 1.0
FORECLOSE_SPREAD = 1.5
DOESNOT_SPREAD = 1.2

# phase1_proposal.md Sec 4b (part b) -- same freeze.
SUPPORT_R2 = 0.90
SUPPORT_FLOOR_R2 = 0.75
REFUTE_R2 = 0.50

DRIFT_GUARD_TOL = 1e-6


def r_squared(true, model):
    true = np.asarray(true, dtype=float)
    model = np.asarray(model, dtype=float)
    ss_res = float(np.sum((true - model) ** 2))
    ss_tot = float(np.sum((true - np.mean(true)) ** 2))
    return float(1.0 - ss_res / ss_tot) if ss_tot > 0 else float("nan")


# ============================================================== part (a)
def part_a():
    rows = {}
    W_seen = set()
    for key in CONGRUENT_KEYS:
        c = dg065.CONFIGS[key]
        W_cfg = c["aperture_cells"]
        W_seen.add(int(W_cfg))
        d_f = (W_cfg ** 2) / LAM600
        y_lo, y_hi = c["y_lo"], c["y_hi"]
        d_lo = float(ywas.dist_image_cells(y_lo, c))
        d_hi = float(ywas.dist_image_cells(y_hi, c))
        d_min, d_max = min(d_lo, d_hi), max(d_lo, d_hi)
        th_lo = float(ywas.theta_local_deg(y_lo, c))
        th_hi = float(ywas.theta_local_deg(y_hi, c))
        env_lo, env_hi = min(th_lo, th_hi), max(th_lo, th_hi)
        spread = env_hi / env_lo
        rows[key] = dict(
            W=int(W_cfg), lam_cells=int(LAM600), fraunhofer_dist_cells=float(d_f),
            dist_image_at_y_lo=d_lo, dist_image_at_y_hi=d_hi,
            dist_ratio_min=d_min / d_f, dist_ratio_max=d_max / d_f,
            theta_local_at_y_lo_deg=th_lo, theta_local_at_y_hi_deg=th_hi,
            theta_local_env_lo_deg=env_lo, theta_local_env_hi_deg=env_hi,
            theta_local_spread_ratio=spread,
        )
    worst_ratio = max(r["dist_ratio_max"] for r in rows.values())
    best_ratio_all_above = min(r["dist_ratio_min"] for r in rows.values())
    worst_spread = max(r["theta_local_spread_ratio"] for r in rows.values())
    if worst_ratio < FORECLOSE_RATIO or worst_spread > FORECLOSE_SPREAD:
        verdict = "FORECLOSE"
    elif best_ratio_all_above > DOESNOT_RATIO and worst_spread < DOESNOT_SPREAD:
        verdict = "DOES-NOT-FORECLOSE"
    else:
        verdict = "MARGINAL"
    return dict(
        rows=rows, W_values_seen=sorted(W_seen), lam_cells=int(LAM600),
        worst_dist_ratio=worst_ratio, best_dist_ratio_all_configs_min=best_ratio_all_above,
        worst_theta_local_spread_ratio=worst_spread,
        thresholds=dict(foreclose_ratio=FORECLOSE_RATIO, doesnot_ratio=DOESNOT_RATIO,
                         foreclose_spread=FORECLOSE_SPREAD, doesnot_spread=DOESNOT_SPREAD),
        verdict=verdict,
    )


# ============================================================== part (b)
def theta_eff_primary(cfg):
    """Amplitude-weighted mean of theta_local(y_s) over the native (dy=1
    cell) aperture grid -- phase1_proposal.md Sec 2's PRIMARY definition."""
    y_grid = ywas.build_aperture_grid(cfg, 1)
    amp = ywas.aperture_amplitude(y_grid, cfg)
    th_loc = ywas.theta_local_deg(y_grid, cfg)
    num = ywas._trapz(amp * th_loc, y_grid)
    den = ywas._trapz(amp, y_grid)
    return float(num / den)


def theta_eff_secondary(cfg):
    """Aperture-midpoint value -- phase1_proposal.md Sec 2's SECONDARY
    (robustness cross-check) definition."""
    return float(ywas.theta_local_deg(cfg["obj_y"], cfg))


def single_angle_curve(cfg, absorb_for_r, thetas_beam_deg, theta_eff_deg):
    """echo_field_curve's own machinery, with r(theta_local(y_s)) replaced
    by ONE constant r(theta_eff;ABSORB) -- everything else (taper, driven-
    phase ramp, dist_image) exactly as in the true per-point model."""
    y_grid = ywas.build_aperture_grid(cfg, 1)
    amp = ywas.aperture_amplitude(y_grid, cfg)
    dist_img = ywas.dist_image_cells(y_grid, cfg)
    n_prof = br.n_profile_exact(br.nu_profile(br.damp_e_profile(absorb_for_r)),
                                 2.0 * math.pi / LAM600)
    r_const = ywas.reflection_coefficient_vec(n_prof, np.array([theta_eff_deg]), LAM600)[0]
    curve = []
    for th_beam in thetas_beam_deg:
        phase_drive = ywas.source_driven_phase(y_grid, float(th_beam), cfg)
        integrand = amp * r_const * np.exp(1j * (phase_drive + ywas.K600 * dist_img))
        re = float(ywas._trapz(integrand.real, y_grid))
        im = float(ywas._trapz(integrand.imag, y_grid))
        curve.append(complex(re, im))
    return np.array(curve, dtype=complex), complex(r_const)


def part_b():
    with open(EXP076_RESULTS) as f:
        res76 = json.load(f)
    thetas = np.array(res76["headline"]["theta"])

    per_config = {}
    max_drift = 0.0
    for key in CONGRUENT_KEYS:
        c = dg065.CONFIGS[key]

        # version-drift guard: recompute the TRUE per-point curve fresh from
        # the live, already-gated function and check it against the
        # committed JSON before trusting any comparison built on it.
        true_curve, _ = ywas.echo_field_curve(c, c["absorb"], thetas, 1)
        stored = EXP079_RESULTS["primary_model_curves"][key]
        drift_re = float(np.max(np.abs(true_curve.real - np.array(stored["re_e_echo"]))))
        drift_abs = float(np.max(np.abs(np.abs(true_curve) - np.array(stored["abs_e_echo"]))))
        max_drift = max(max_drift, drift_re, drift_abs)

        eff_primary = theta_eff_primary(c)
        eff_secondary = theta_eff_secondary(c)

        curve_primary, r_primary = single_angle_curve(c, c["absorb"], thetas, eff_primary)
        curve_secondary, r_secondary = single_angle_curve(c, c["absorb"], thetas, eff_secondary)

        per_config[key] = dict(
            theta_eff_primary_deg=eff_primary,
            theta_eff_secondary_deg=eff_secondary,
            r_theta_eff_primary=dict(re=r_primary.real, im=r_primary.imag, abs=abs(r_primary)),
            r_theta_eff_secondary=dict(re=r_secondary.real, im=r_secondary.imag, abs=abs(r_secondary)),
            drift_guard_max_abs_diff_re=drift_re,
            drift_guard_max_abs_diff_abs=drift_abs,
            r2_re_theta_eff_primary=r_squared(true_curve.real, curve_primary.real),
            r2_abs_theta_eff_primary=r_squared(np.abs(true_curve), np.abs(curve_primary)),
            r2_re_theta_eff_secondary=r_squared(true_curve.real, curve_secondary.real),
            r2_abs_theta_eff_secondary=r_squared(np.abs(true_curve), np.abs(curve_secondary)),
        )

    assert max_drift < DRIFT_GUARD_TOL, (
        f"version-drift guard FAILED: recomputed per-point curve does not "
        f"match the committed y_wall_aperture_sum_results.json "
        f"(max_drift={max_drift:.3e} >= {DRIFT_GUARD_TOL:.0e}) -- do not "
        f"trust any R^2 number below until this is resolved")

    r2_primary_vals = [v["r2_re_theta_eff_primary"] for v in per_config.values()]
    mean_r2 = float(np.mean(r2_primary_vals))
    min_r2 = float(min(r2_primary_vals))
    if mean_r2 >= SUPPORT_R2 and min_r2 >= SUPPORT_FLOOR_R2:
        verdict = "SUPPORT"
    elif mean_r2 < REFUTE_R2:
        verdict = "REFUTE"
    else:
        verdict = "INCONCLUSIVE"

    return dict(
        per_config=per_config,
        mean_r2_re_theta_eff_primary=mean_r2,
        min_r2_re_theta_eff_primary=min_r2,
        max_drift_guard_abs_diff=max_drift,
        thresholds=dict(support_r2=SUPPORT_R2, support_floor_r2=SUPPORT_FLOOR_R2,
                         refute_r2=REFUTE_R2),
        verdict=verdict,
    )


# ======================================== PHASE 3 fix docket (Red Team's
# phase2_redteam_audit.md Sec 3, items 1-5, all ADOPTED IN FULL -- folds
# each blind Phase-2 critique's own independently-reproduced finding into
# committed, reusable code, exactly as this sub-thread's own house practice
# requires (y_wall_aperture_sum.py Sec [7]/[7b] precedent, exp-079
# Iteration 56). Every function below reproduces a number Red Team already
# independently re-derived from primitives and confirmed exact
# (phase2_redteam_audit.md Sec 0, items 4/5/6/8) -- no NEW previously-
# uncomputed claim is made here, so no fresh FROZEN-PREDICTIONS freeze cycle
# is needed (same reasoning exp-079 Iteration 56 Phase 3 gave for its own
# no-freeze-needed fix docket).


# ---- fix docket item 2 (MATERIALS): realizable (mu_r=1) admittance rerun
def reflection_coefficient_vec_realizable(n_prof, theta_deg_arr, lam_cells):
    """SAME recursive transfer-matrix algebra as reflection_coefficient_vec,
    with the per-layer admittance Zi=ni/sqrt(ni^2-sin^2(theta)) (implicitly
    mu_r=ni^2, the MATCHED/unobtainium family every other function in this
    file uses) replaced by Zi=1/sqrt(ni^2-sin^2(theta)) (mu_r=1, the
    REALIZABLE ordinary-dielectric family) -- the SAME substitution exp-079's
    own MATERIALS Phase-5 review made (phase5_review_materials.md Sec 2b),
    independently re-confirmed there by that cycle's own Red Team audit, and
    independently re-derived a second time by this cycle's own MATERIALS
    Phase-2 critique and Red Team's Phase-2 audit (Sec 0 item 4)."""
    theta = np.radians(np.asarray(theta_deg_arr, dtype=float))
    s2 = np.sin(theta) ** 2
    k0 = 2.0 * math.pi / lam_cells
    Zvac = 1.0 / np.cos(theta)
    Zin = np.zeros_like(theta, dtype=complex)
    n_prof = n_prof.astype(complex)
    for ni in n_prof:
        rad = (ni ** 2 - s2.astype(complex))
        kxi = k0 * np.sqrt(rad)
        Zi = 1.0 / np.sqrt(rad)  # <-- the one line that differs: mu_r=1
        t = np.tan(kxi * 1.0)
        Zin = Zi * (Zin + 1j * Zi * t) / (Zi + 1j * Zin * t)
    return (Zin - Zvac) / (Zin + Zvac)


def single_angle_curve_realizable(cfg, absorb_for_r, thetas_beam_deg, theta_eff_deg):
    """single_angle_curve, with reflection_coefficient_vec_realizable in
    place of reflection_coefficient_vec -- everything else (taper,
    driven-phase ramp, dist_image, theta_eff itself) unchanged."""
    y_grid = ywas_build_aperture_grid(cfg, 1)
    amp = ywas.aperture_amplitude(y_grid, cfg)
    dist_img = ywas.dist_image_cells(y_grid, cfg)
    n_prof = br.n_profile_exact(br.nu_profile(br.damp_e_profile(absorb_for_r)),
                                 2.0 * math.pi / LAM600)
    r_const = reflection_coefficient_vec_realizable(n_prof, np.array([theta_eff_deg]), LAM600)[0]
    curve = []
    for th_beam in thetas_beam_deg:
        phase_drive = ywas.source_driven_phase(y_grid, float(th_beam), cfg)
        integrand = amp * r_const * np.exp(1j * (phase_drive + ywas.K600 * dist_img))
        re = float(ywas._trapz(integrand.real, y_grid))
        im = float(ywas._trapz(integrand.imag, y_grid))
        curve.append(complex(re, im))
    return np.array(curve, dtype=complex), complex(r_const)


def ywas_build_aperture_grid(cfg, oversample):
    return ywas.build_aperture_grid(cfg, oversample)


def part_b_realizable():
    """Fix docket item 2: rerun part (b) end-to-end under the realizable
    admittance -- BOTH the true per-point curve and the single-angle model
    recomputed consistently under mu_r=1 (not a mismatched-family
    comparison), mirroring exp-079's own Sec 2b methodology."""
    with open(EXP076_RESULTS) as f:
        res76 = json.load(f)
    thetas = np.array(res76["headline"]["theta"])

    per_config = {}
    for key in CONGRUENT_KEYS:
        c = dg065.CONFIGS[key]
        y_grid = ywas.build_aperture_grid(c, 1)
        amp = ywas.aperture_amplitude(y_grid, c)
        dist_img = ywas.dist_image_cells(y_grid, c)
        th_loc = ywas.theta_local_deg(y_grid, c)
        n_prof = br.n_profile_exact(br.nu_profile(br.damp_e_profile(c["absorb"])),
                                     2.0 * math.pi / LAM600)
        r_of_ys_realizable = reflection_coefficient_vec_realizable(n_prof, th_loc, LAM600)

        eff_primary = theta_eff_primary(c)  # geometry-only, admittance-independent

        true_curve_realizable = []
        model_curve_realizable = []
        r_const = reflection_coefficient_vec_realizable(n_prof, np.array([eff_primary]), LAM600)[0]
        for th_beam in thetas:
            phase_drive = ywas.source_driven_phase(y_grid, float(th_beam), c)
            true_integrand = amp * r_of_ys_realizable * np.exp(1j * (phase_drive + ywas.K600 * dist_img))
            model_integrand = amp * r_const * np.exp(1j * (phase_drive + ywas.K600 * dist_img))
            true_curve_realizable.append(complex(
                float(ywas._trapz(true_integrand.real, y_grid)),
                float(ywas._trapz(true_integrand.imag, y_grid))))
            model_curve_realizable.append(complex(
                float(ywas._trapz(model_integrand.real, y_grid)),
                float(ywas._trapz(model_integrand.imag, y_grid))))
        true_curve_realizable = np.array(true_curve_realizable, dtype=complex)
        model_curve_realizable = np.array(model_curve_realizable, dtype=complex)

        per_config[key] = dict(
            theta_eff_primary_deg=eff_primary,
            r_theta_eff_realizable=dict(re=r_const.real, im=r_const.imag, abs=abs(r_const)),
            r2_re_realizable=r_squared(true_curve_realizable.real, model_curve_realizable.real),
        )

    r2_vals = [v["r2_re_realizable"] for v in per_config.values()]
    mean_r2 = float(np.mean(r2_vals))
    min_r2 = float(min(r2_vals))
    if mean_r2 >= SUPPORT_R2 and min_r2 >= SUPPORT_FLOOR_R2:
        verdict = "SUPPORT"
    elif mean_r2 < REFUTE_R2:
        verdict = "REFUTE"
    else:
        verdict = "INCONCLUSIVE"
    return dict(per_config=per_config, mean_r2_realizable=mean_r2, min_r2_realizable=min_r2,
                verdict=verdict,
                note="admittance-family-DEPENDENT vs part_b's matched-family mean=0.7345/"
                     "min=0.5214 -- both computed self-consistently (true curve AND model "
                     "curve under the SAME admittance family per config, not a mismatched "
                     "comparison), per Red Team phase2_redteam_audit.md Sec 0 item 4")


# ---- fix docket item 3 (THERMODYNAMICS): |r(90-theta_beam)|^2 power budget
def part_c_power_budget_at_true_angle():
    """The reflected-power fraction 1-|r(theta_beam)|^2 THERMODYNAMICS'
    standing suggestion (exp-079 Sec 7 Tier-0 item 1) asks for, evaluated at
    the angle PHOTONICS' own Sec 4 construction actually uses
    (90-theta_beam), NOT this cycle's own geometry-only theta_eff (whose
    |r|^2 answers a different, much smaller-magnitude question, Red Team
    phase2_redteam_audit.md Sec 1 Attack 2 / Sec 0 item 5)."""
    with open(EXP076_RESULTS) as f:
        res76 = json.load(f)
    thetas = np.array(res76["headline"]["theta"])
    out = {}
    for absorb in br.ABSORB_LIST:
        n_prof = br.n_profile_exact(br.nu_profile(br.damp_e_profile(absorb)),
                                     2.0 * math.pi / LAM600)
        r_vals = ywas.reflection_coefficient_vec(n_prof, 90.0 - thetas, LAM600)
        r2 = np.abs(r_vals) ** 2
        out[f"absorb_{absorb}"] = dict(
            r2_min=float(r2.min()), r2_max=float(r2.max()),
            reflected_power_fraction_min=float(r2.min()),
            reflected_power_fraction_max=float(r2.max()),
        )
    return out


# ---- fix docket item 4 (PHOTONICS): calibration-corrected R^2(abs) for part (b)
def _best_scale(true, model):
    """Least-squares-optimal real scalar alpha minimizing ||true-alpha*model||^2."""
    model = np.asarray(model, dtype=float)
    true = np.asarray(true, dtype=float)
    denom = float(np.sum(model ** 2))
    return float(np.sum(true * model) / denom) if denom > 0 else float("nan")


def part_b_abs_calibration_corrected():
    """PHOTONICS' finding (Red Team Sec 0 item 6): the raw theta_eff-based
    R^2(abs) at C70/C80 (-7.82/-8.45) is ~2x worse than the true shape-only
    floor because |r(theta_eff)| happens to undershoot the least-squares-
    optimal scale -- report both, per Red Team's Attack 4 fix."""
    with open(EXP076_RESULTS) as f:
        res76 = json.load(f)
    thetas = np.array(res76["headline"]["theta"])
    out = {}
    for key in CONGRUENT_KEYS:
        c = dg065.CONFIGS[key]
        true_curve, _ = ywas.echo_field_curve(c, c["absorb"], thetas, 1)
        eff_primary = theta_eff_primary(c)
        model_curve, _ = single_angle_curve(c, c["absorb"], thetas, eff_primary)
        alpha_star = _best_scale(np.abs(true_curve), np.abs(model_curve))
        r2_abs_calibrated = r_squared(np.abs(true_curve), alpha_star * np.abs(model_curve))
        out[key] = dict(alpha_star=alpha_star, r2_abs_calibration_corrected=r2_abs_calibrated)
    return out


# ---- fix docket item 1 (QUANTUM, adopted by Red Team as the canonical
# zero-FDTD implementation of PHOTONICS' Sec 4 image term -- NOT a future
# "build item", per phase2_redteam_audit.md Sec 2/Sec 6: this construction
# has already been independently derived twice (QUANTUM's blind critique,
# Red Team's from-scratch reproduction) and reproduces to 4 decimal places
# both times. Folded here into committed, reusable code so Iteration 58 can
# extend it (real free-period scoring) rather than re-derive it a third time.
def photonics_image_term_curve(cfg, absorb_for_r, thetas_beam_deg):
    """E_photonics(theta_beam) = r(90-theta_beam;ABSORB) * W(theta_beam),
    where W(theta_beam) is exp-079's own Sec [7] r_ablated=1 integral
    (re-derived here fresh from the same primitives, not copied) -- PHOTONICS'
    own Sec 4 review's sketched construction (apply ONE scalar r(90-theta_beam),
    evaluated at the SWEPT BEAM ANGLE itself, globally to the unweighted image
    sum), fix-docket Idealization 5: E_direct(theta_beam) is OMITTED here,
    an inherited-not-independently-verified assumption (valid only insofar as
    it cancels identically across congruent-config pair deltas -- flagged,
    not resolved, by this file)."""
    y_grid = ywas.build_aperture_grid(cfg, 1)
    amp = ywas.aperture_amplitude(y_grid, cfg)
    dist_img = ywas.dist_image_cells(y_grid, cfg)
    n_prof = br.n_profile_exact(br.nu_profile(br.damp_e_profile(absorb_for_r)),
                                 2.0 * math.pi / LAM600)
    thetas_beam_deg = np.asarray(thetas_beam_deg, dtype=float)
    r_at_beam = ywas.reflection_coefficient_vec(n_prof, 90.0 - thetas_beam_deg, LAM600)
    curve = []
    for i, th_beam in enumerate(thetas_beam_deg):
        phase_drive = ywas.source_driven_phase(y_grid, float(th_beam), cfg)
        integrand = amp * np.exp(1j * (phase_drive + ywas.K600 * dist_img))
        w_re = float(ywas._trapz(integrand.real, y_grid))
        w_im = float(ywas._trapz(integrand.imag, y_grid))
        w = complex(w_re, w_im)
        curve.append(r_at_beam[i] * w)
    return np.array(curve, dtype=complex)


def part_d_photonics_construction():
    """Score photonics_image_term_curve against the true per-point curve --
    raw, then scale-corrected (single best-fit real scalar per config,
    isolating pure shape from the raw amplitude-regime mismatch)."""
    with open(EXP076_RESULTS) as f:
        res76 = json.load(f)
    thetas = np.array(res76["headline"]["theta"])
    out = {}
    for key in CONGRUENT_KEYS:
        c = dg065.CONFIGS[key]
        true_curve, _ = ywas.echo_field_curve(c, c["absorb"], thetas, 1)
        model_curve = photonics_image_term_curve(c, c["absorb"], thetas)
        raw_r2_re = r_squared(true_curve.real, model_curve.real)
        raw_r2_abs = r_squared(np.abs(true_curve), np.abs(model_curve))
        alpha_re = _best_scale(true_curve.real, model_curve.real)
        alpha_abs = _best_scale(np.abs(true_curve), np.abs(model_curve))
        sc_r2_re = r_squared(true_curve.real, alpha_re * model_curve.real)
        sc_r2_abs = r_squared(np.abs(true_curve), alpha_abs * np.abs(model_curve))
        out[key] = dict(absorb=int(c["absorb"]), raw_r2_re=raw_r2_re, raw_r2_abs=raw_r2_abs,
                         scale_corrected_r2_re=sc_r2_re, scale_corrected_r2_abs=sc_r2_abs)
    sc_re_vals = [v["scale_corrected_r2_re"] for v in out.values()]
    return dict(per_config=out, mean_scale_corrected_r2_re=float(np.mean(sc_re_vals)),
                min_scale_corrected_r2_re=float(min(sc_re_vals)),
                note="canonical zero-FDTD implementation of PHOTONICS' Sec 4 image term "
                     "(QUANTUM's construction, Red-Team-adopted); worse floor than this "
                     "cycle's own part (b) static-theta_eff result -- see phase3_synthesis.md")


def main():
    print("=" * 78)
    print("exp-080 -- EM validity pre-check for the plane-wave/global-steering")
    print("y-wall construction (Red Team exp-079 Sec 3/7 Tier-0 item 1)")
    print("=" * 78)

    print("\n[a] FRAUNHOFER/FAR-FIELD MARGIN + theta_local SPREAD "
          "(pre-registered thresholds: FORECLOSE if ratio<%.0f%% or spread>%.1fx; "
          "DOES-NOT-FORECLOSE if ratio>%.0f%% and spread<%.1fx)"
          % (FORECLOSE_RATIO * 100, FORECLOSE_SPREAD, DOESNOT_RATIO * 100, DOESNOT_SPREAD))
    a = part_a()
    print(f"    W={a['W_values_seen']} cells (all congruent configs)  "
          f"lambda={a['lam_cells']} cells  "
          f"d_F=W^2/lambda={a['rows'][CONGRUENT_KEYS[0]]['fraunhofer_dist_cells']:.1f} cells")
    for key, row in a["rows"].items():
        print(f"    {key}: dist_image=[{row['dist_image_at_y_lo']:.1f},"
              f"{row['dist_image_at_y_hi']:.1f}] cells  "
              f"ratio=[{row['dist_ratio_min'] * 100:.2f}%,{row['dist_ratio_max'] * 100:.2f}%]  "
              f"theta_local=[{row['theta_local_env_lo_deg']:.2f},"
              f"{row['theta_local_env_hi_deg']:.2f}]deg  "
              f"spread={row['theta_local_spread_ratio']:.3f}x")
    print(f"    worst dist_ratio (max over configs/edges) = {a['worst_dist_ratio'] * 100:.3f}%")
    print(f"    smallest dist_ratio floor (min over configs/edges) = "
          f"{a['best_dist_ratio_all_configs_min'] * 100:.3f}%")
    print(f"    worst theta_local spread ratio = {a['worst_theta_local_spread_ratio']:.3f}x")
    print(f"    VERDICT (a): {a['verdict']}")

    print("\n[b] SINGLE-ANGLE REPRODUCTION TEST "
          "(pre-registered thresholds: SUPPORT if mean R2>=%.2f and min>=%.2f; "
          "REFUTE if mean R2<%.2f)" % (SUPPORT_R2, SUPPORT_FLOOR_R2, REFUTE_R2))
    b = part_b()
    print(f"    version-drift guard: max|recomputed - committed| = "
          f"{b['max_drift_guard_abs_diff']:.3e} (PASS, tol={DRIFT_GUARD_TOL:.0e})")
    for key, row in b["per_config"].items():
        print(f"    {key}: theta_eff(primary)={row['theta_eff_primary_deg']:.4f}deg  "
              f"theta_eff(secondary)={row['theta_eff_secondary_deg']:.4f}deg  "
              f"R2(Re,primary)={row['r2_re_theta_eff_primary']:.4f}  "
              f"R2(abs,primary)={row['r2_abs_theta_eff_primary']:.4f}  "
              f"R2(Re,secondary)={row['r2_re_theta_eff_secondary']:.4f}  "
              f"R2(abs,secondary)={row['r2_abs_theta_eff_secondary']:.4f}")
    print(f"    mean R2(Re,primary) over {len(CONGRUENT_KEYS)} configs = "
          f"{b['mean_r2_re_theta_eff_primary']:.4f}")
    print(f"    min  R2(Re,primary) over {len(CONGRUENT_KEYS)} configs = "
          f"{b['min_r2_re_theta_eff_primary']:.4f}")
    print(f"    VERDICT (b): {b['verdict']}")

    print("\n[b-realizable] Fix docket item 2 (MATERIALS): part (b) rerun under "
          "the REALIZABLE (mu_r=1) admittance, self-consistently")
    b_realizable = part_b_realizable()
    for key, row in b_realizable["per_config"].items():
        print(f"    {key}: R2(Re,realizable)={row['r2_re_realizable']:.4f}")
    print(f"    mean R2(Re,realizable) = {b_realizable['mean_r2_realizable']:.4f}  "
          f"min = {b_realizable['min_r2_realizable']:.4f}  "
          f"VERDICT: {b_realizable['verdict']}")

    print("\n[c] Fix docket item 3 (THERMODYNAMICS): |r(90-theta_beam)|^2 "
          "reflected-power fraction at the REAL angle PHOTONICS' construction uses")
    c = part_c_power_budget_at_true_angle()
    for key, row in c.items():
        print(f"    {key}: reflected-power-fraction=[{row['r2_min']:.3e},{row['r2_max']:.3e}]")

    print("\n[b-abs-cal] Fix docket item 4 (PHOTONICS): calibration-corrected "
          "R2(abs) for part (b)'s static-theta_eff model")
    b_abs_cal = part_b_abs_calibration_corrected()
    for key, row in b_abs_cal.items():
        print(f"    {key}: alpha*={row['alpha_star']:.4e}  "
              f"R2(abs,calibrated)={row['r2_abs_calibration_corrected']:.4f}")

    print("\n[d] Fix docket item 1 (QUANTUM, Red-Team-adopted as canonical): "
          "PHOTONICS' Sec 4 image term E_photonics(theta_beam)=r(90-theta_beam)*W(theta_beam)")
    d = part_d_photonics_construction()
    for key, row in d["per_config"].items():
        print(f"    {key}: raw R2(Re)={row['raw_r2_re']:.3e}  raw R2(abs)={row['raw_r2_abs']:.3e}  "
              f"scale-corrected R2(Re)={row['scale_corrected_r2_re']:.4f}  "
              f"scale-corrected R2(abs)={row['scale_corrected_r2_abs']:.4f}")
    print(f"    mean scale-corrected R2(Re) = {d['mean_scale_corrected_r2_re']:.4f}  "
          f"min = {d['min_scale_corrected_r2_re']:.4f}")

    out = dict(part_a=a, part_b=b, part_b_realizable=b_realizable,
               part_c_power_budget=c, part_b_abs_calibration_corrected=b_abs_cal,
               part_d_photonics_construction=d)

    def _json_default(o):
        if isinstance(o, (np.bool_,)):
            return bool(o)
        if isinstance(o, (np.floating,)):
            return float(o)
        if isinstance(o, (np.integer,)):
            return int(o)
        if isinstance(o, np.ndarray):
            return o.tolist()
        if isinstance(o, complex):
            return dict(re=o.real, im=o.imag)
        raise TypeError(f"not JSON serializable: {type(o)}")

    out_path = os.path.join(HERE, "validity_precheck_results.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2, default=_json_default)
    print(f"\nwrote {out_path}")
    return out


if __name__ == "__main__":
    main()
