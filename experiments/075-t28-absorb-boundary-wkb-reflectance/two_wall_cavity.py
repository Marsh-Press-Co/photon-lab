"""
experiments/075-t28-absorb-boundary-wkb-reflectance/two_wall_cavity.py
============================================================================
Panel Iteration 52 (exp-075), PHASE 4 -- executes phase3_synthesis.md
Sec 3's mandatory fix 1: the actual two-wall-cavity interference model,
designed and pre-registered BEFORE this script touched the real
`block_dense.rows` data (predictions frozen in the prior commit).

ZERO new FDTD calls -- same discipline as `boundary_reflectance.py`, whose
already-vetted machinery (n(x), the transfer-matrix `reflection_coefficient`,
the three sanity/passivity gates, exp-048's Huygens-Fresnel propagator) is
IMPORTED here, not reimplemented.

WHAT THIS FILE ADDS, beyond boundary_reflectance.py's single (-x)-wall echo:

  [1] `image_geometry_right` -- the mirror image of the source through the
      OTHER PEC wall (x=nx-1, behind the source), by the SAME
      interferometer-arm argument boundary_reflectance.py already used for
      the near wall -- giving the physically-correct path difference
      2*(nx-1-SRC_X), not PHOTONICS' Phase-2 closed-form-only substitution
      of the raw domain width nx (phase3_synthesis.md Sec 3.2).
  [2] `c_empty_two_wall` -- THREE coherent terms (direct + left-image +
      right-image, same r(theta;ABSORB) for both walls -- justified in
      phase3_synthesis.md Sec 3.3), reduced through the SAME
      window_means/weber pipeline as the single-wall model.
  [3] The SAME Test A (period match) / Test B (shape match) scoring, on the
      SAME pre-registered bands as phase1_proposal.md Sec 5 -- reused, not
      re-tuned (phase3_synthesis.md Sec 3.5).
  [4] A NEW circular-shift (order-preserving, R6-style) null-calibration
      robustness check on Test B -- the look-elsewhere/robustness leg Red
      Team's Phase-2 audit made mandatory (phase2_redteam_audit.md Sec 9
      item 1; phase3_synthesis.md Sec 3.5).

Run: `python3 two_wall_cavity.py` from this directory (or anywhere -- paths
resolve from __file__). Writes `two_wall_cavity_results.json`; every number
in `phase4_results.md` is copied from that JSON/stdout, never hand-typed.
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
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


# boundary_reflectance.py's own already-vetted machinery -- imported, not
# reimplemented (n(x), reflection_coefficient, the three gates, CPL, etc.)
br = _load(os.path.join(HERE, "boundary_reflectance.py"), "_exp075_boundary_reflectance")
dg065 = br.dg065
dg048 = br.dg048
CPL = br.CPL
ABSORB_LIST = br.ABSORB_LIST

from lab import ambient as amb  # noqa: E402

RESULTS_69_PATH = br.RESULTS_69_PATH
RUN69_PATH = br.RUN69_PATH


# ===================================================== [1] the far wall
def image_geometry_right(g, nx):
    """Mirror image of the source through the x=nx-1 wall (behind the
    source, the OTHER PEC boundary -- lab/fdtd2d.py::Sim.run never updates
    Ez at index nx-1, confirmed directly against the code, same as index 0).
    By the identical interferometer-arm argument boundary_reflectance.py's
    own `image_geometry` (left wall) uses: image at x = 2*(nx-1) - SRC_X,
    so the image-to-plane distance is 2*(nx-1) - SRC_X - PLANE_X. The
    source-position dependence does NOT cancel out of this one the same
    tidy way it does for the near wall (that cancellation used PLANE_X <
    SRC_X specifically) -- this function returns the correct image
    geometry directly; phase3_synthesis.md Sec 3.2's closed-form table
    reports the resulting D_right = (nx-1) - SRC_X separately, as the
    genuinely simplifying quantity for THIS wall."""
    gi = dict(g)
    w = nx - 1
    x_img = 2 * w - g["SRC_X"]
    gi["D_SP"] = x_img - g["PLANE_X"]
    return gi


def closed_form_period(D, theta_deg, lam_cells):
    """Zero-order (ignoring r(theta)'s own phase) round-trip period, the
    same closed form as boundary_reflectance.py Sec [8], parameterized by
    the correct one-way wall distance D (=PLANE_X for the near wall,
    =(nx-1)-SRC_X for the far wall -- NOT the raw domain width)."""
    return math.degrees(lam_cells / (2.0 * D * math.sin(math.radians(theta_deg))))


# ============================================ [2] two-wall interference
def c_empty_two_wall(theta_deg, lam_cells, g, r_coeff, nx):
    """Direct field + LEFT image + RIGHT image, all three coherently
    summed before the window_means/weber reduction -- same r_coeff for
    both images (justified in phase3_synthesis.md Sec 3.3: identical
    ABSORB bands, mirror-symmetric launch angle magnitude at each wall,
    confirmed empty/object-free scene)."""
    E_d, H_d, gd = dg048.field_and_h(theta_deg, lam_cells, g)
    gi_l = br.image_geometry(g)
    E_l, H_l, gdl = dg048.field_and_h(theta_deg, lam_cells, gi_l)
    gi_r = image_geometry_right(g, nx)
    E_r, H_r, gdr = dg048.field_and_h(theta_deg, lam_cells, gi_r)
    assert np.array_equal(gd["y_obs"], gdl["y_obs"]) and np.array_equal(gd["y_obs"], gdr["y_obs"]), \
        "left/right/direct y-grids disagree"
    E = E_d + r_coeff * E_l + r_coeff * E_r
    H = H_d + r_coeff * H_l + r_coeff * H_r
    Sx = -np.real(E * np.conj(H))
    bo, bf = amb.window_means(Sx, gd["y_lo"], gd["obj_y"], g["R_OUT"], g["GUARD_OUT"], g["W_FLANK"])
    return amb.weber(bo, bf)


# ================================================= [4] circular-shift null
def circular_shift_null(pred_curve, real_curve, n_trials=20000, seed=42):
    """Order-preserving (R6-style) null-calibration test: how often does a
    CIRCULAR SHIFT of the real data's own delta(theta) array correlate with
    the model's FIXED predicted curve at least as strongly as the real,
    unshifted pairing? Preserves the real data's own autocorrelation
    structure (unlike an i.i.d. permutation), the harder companion test
    this program's own R6 standing rule requires (LOGBOOK.md, Iteration 50)
    for angularly-autocorrelated data (T28's real residuals are known
    lag-1~0.92-0.94 autocorrelated, exp-074 Iteration 51)."""
    rng = np.random.default_rng(seed)
    n = len(real_curve)
    observed_r = float(np.corrcoef(pred_curve, real_curve)[0, 1])
    observed_abs_r = abs(observed_r)
    null_abs_r = np.empty(n_trials)
    for i in range(n_trials):
        shift = int(rng.integers(1, n))  # never shift=0 (that's the real, unshifted pairing)
        shifted = np.roll(real_curve, shift)
        null_abs_r[i] = abs(float(np.corrcoef(pred_curve, shifted)[0, 1]))
    p_value = float(np.mean(null_abs_r >= observed_abs_r))
    return dict(observed_r=observed_r, observed_abs_r=observed_abs_r,
                n_trials=n_trials, p_value=p_value,
                null_mean_abs_r=float(np.mean(null_abs_r)),
                null_95pct_abs_r=float(np.percentile(null_abs_r, 95)))


# =============================================================== driver
def main():
    out = {}
    print("=" * 78)
    print("exp-075 Phase 4 -- the two-wall-cavity model (mandatory fix 1)")
    print("=" * 78)

    with open(RESULTS_69_PATH) as f:
        res69 = json.load(f)
    dense_rows = res69["block_dense"]["rows"]
    thetas = np.array([r["theta"] for r in dense_rows])
    real_delta = np.array([r["delta"] for r in dense_rows])

    print("\n[1] CLOSED-FORM PERIODS, BOTH WALLS, CORRECTLY DERIVED (zero data,")
    print("    reproduces phase3_synthesis.md Sec 3.2's table)")
    d_left = {}
    d_right = {}
    for absorb in ABSORB_LIST:
        cfg = dg065.CONFIGS[f"C{absorb}"]
        nx = cfg["nx"]
        d_left[absorb] = cfg["plane_x"]
        d_right[absorb] = (nx - 1) - cfg["src_x"]
        p_l = closed_form_period(d_left[absorb], 39.0, CPL[600])
        p_r = closed_form_period(d_right[absorb], 39.0, CPL[600])
        print(f"    ABSORB={absorb:3d}  D_left={d_left[absorb]:4d}  D_right={d_right[absorb]:4d}  "
              f"P_left(39deg)={p_l:.3f}deg  P_right(39deg)={p_r:.3f}deg")
    out["d_left"] = d_left
    out["d_right"] = d_right

    print("\n[2] TWO-WALL PREDICTED DELTA(theta) = C_two_wall(80) - C_two_wall(40)")
    c_two = {absorb: [] for absorb in ABSORB_LIST}
    for absorb in ABSORB_LIST:
        cfg_key = f"C{absorb}"
        cfg = dg065.CONFIGS[cfg_key]
        g = dg065.propagator_geom(cfg)
        nx = cfg["nx"]
        n_exact = br.n_profile_exact(br.nu_profile(br.damp_e_profile(absorb)), 2.0 * math.pi / CPL[600])
        for t in thetas:
            r = br.reflection_coefficient(n_exact, float(t), CPL[600])
            c_two[absorb].append(c_empty_two_wall(float(t), CPL[600], g, r, nx))
        c_two[absorb] = np.array(c_two[absorb])

    pred_delta_two = c_two[80] - c_two[40]
    print(f"    predicted delta(theta): min={pred_delta_two.min():.6e}  "
          f"max={pred_delta_two.max():.6e}  ptp={np.ptp(pred_delta_two):.6e}")
    print(f"    REAL delta(theta) (exp-069 block_dense):    min={real_delta.min():.6e}  "
          f"max={real_delta.max():.6e}  ptp={np.ptp(real_delta):.6e}")
    out["predicted_delta_two_wall"] = pred_delta_two.tolist()
    out["thetas"] = thetas.tolist()
    out["real_delta"] = real_delta.tolist()

    # ---- period fits, SAME methodology as boundary_reflectance.py ----
    run69 = _load(RUN69_PATH, "_exp069_run_twowall")
    free_search = run69._free_period_search
    real_free = free_search(thetas, real_delta, center_deg=39.0)
    pred_free = free_search(thetas, pred_delta_two, center_deg=39.0, lo_deg=1.0, hi_deg=15.0, n_grid=2800)
    pred_free_wide = free_search(thetas, pred_delta_two, center_deg=39.0, lo_deg=1.0, hi_deg=60.0, n_grid=6000)
    at_boundary = pred_free_wide["p_star_deg"] >= 59.9
    print(f"\n[3] FREE-PERIOD FIT (exp-069's own methodology, imported not reimplemented)")
    print(f"    REAL data      P*={real_free['p_star_deg']:.4f}deg  R^2={real_free['r_squared']:.4f} "
          f"(established citation: P*=2.8421deg, R^2=0.6272)")
    print(f"    MODEL predicted P*={pred_free['p_star_deg']:.4f}deg  R^2={pred_free['r_squared']:.4f}")
    print(f"    MODEL predicted, WIDENED search (1-60deg): "
          f"P*={pred_free_wide['p_star_deg']:.4f}deg  R^2={pred_free_wide['r_squared']:.4f}"
          f"{'  [RUNS TO SEARCH BOUNDARY]' if at_boundary else '  [interior optimum]'}")
    out["real_free_period_fit"] = real_free
    out["model_free_period_fit"] = pred_free
    out["model_free_period_fit_widened"] = pred_free_wide
    out["model_period_runs_to_boundary"] = bool(at_boundary)

    rel_period_dev = abs(pred_free["p_star_deg"] - real_free["p_star_deg"]) / real_free["p_star_deg"]
    print(f"    relative period deviation |P_model - P*_real| / P*_real = {rel_period_dev:.4f}")
    out["relative_period_deviation"] = rel_period_dev

    # ---- shape match ----
    corr = np.corrcoef(pred_delta_two, real_delta)[0, 1]
    shape_r2 = float(corr ** 2)
    print(f"\n[4] SHAPE MATCH: Pearson r^2(model predicted delta, real delta) = {shape_r2:.4f} "
          f"(sign of correlation = {'+' if corr > 0 else '-'})")
    out["shape_pearson_r"] = float(corr)
    out["shape_r_squared"] = shape_r2

    # ---- pre-registered bands, scored (SAME bands as phase1_proposal.md) ----
    print("\n[5] PRE-REGISTERED FALSIFIABLE BANDS -- scored (reused from phase1_proposal.md Sec 5)")
    period_support = rel_period_dev <= 0.30
    period_refute = rel_period_dev > 1.00
    shape_support = shape_r2 >= 0.30
    shape_refute = shape_r2 <= 0.05
    if period_support and shape_support:
        combined = "SUPPORT"
    elif period_refute or shape_refute:
        combined = "REFUTE"
    else:
        combined = "INCONCLUSIVE"
    print(f"    period band: SUPPORT<=0.30 REFUTE>1.00 rel_dev={rel_period_dev:.4f} "
          f"-> {'SUPPORT' if period_support else ('REFUTE' if period_refute else 'INCONCLUSIVE')}")
    print(f"    shape  band: SUPPORT>=0.30 REFUTE<=0.05 r^2={shape_r2:.4f} "
          f"-> {'SUPPORT' if shape_support else ('REFUTE' if shape_refute else 'INCONCLUSIVE')}")
    print(f"    COMBINED VERDICT: {combined}")
    out["combined_verdict"] = combined
    out["period_support"] = bool(period_support)
    out["period_refute"] = bool(period_refute)
    out["shape_support"] = bool(shape_support)
    out["shape_refute"] = bool(shape_refute)

    # ---- NEW: circular-shift null-calibration robustness check ----
    print("\n[6] CIRCULAR-SHIFT NULL-CALIBRATION ROBUSTNESS CHECK (mandatory, Red Team)")
    null_check = circular_shift_null(pred_delta_two, real_delta)
    print(f"    observed r = {null_check['observed_r']:+.4f}  |r| = {null_check['observed_abs_r']:.4f}")
    print(f"    null (circular-shift, N={null_check['n_trials']}): mean|r|={null_check['null_mean_abs_r']:.4f}  "
          f"95th pct |r|={null_check['null_95pct_abs_r']:.4f}")
    print(f"    p-value (P[null |r| >= observed |r|]) = {null_check['p_value']:.4f}")
    robust_significant = null_check["p_value"] <= 0.05
    print(f"    robustness verdict: {'SIGNIFICANT vs circular-shift null' if robust_significant else 'NOT significant vs circular-shift null'}")
    out["circular_shift_null_check"] = null_check
    out["robust_significant"] = bool(robust_significant)

    # ---- prediction check against phase3_synthesis.md Sec 3.6 ----
    print("\n[7] PRE-REGISTERED PREDICTION CHECK (phase3_synthesis.md Sec 3.6)")
    predicted_test_a_refute = True  # frozen prediction, committed before this run
    prediction_confirmed = predicted_test_a_refute and period_refute
    print(f"    Predicted (frozen, prior commit): Test A REFUTEs again.")
    print(f"    Observed: Test A {'REFUTE' if period_refute else ('SUPPORT' if period_support else 'INCONCLUSIVE')}")
    print(f"    Frozen prediction: {'CONFIRMED' if prediction_confirmed else 'NOT CONFIRMED -- see phase4_results.md for what this means'}")
    out["frozen_prediction_confirmed"] = bool(prediction_confirmed)

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

    out_path = os.path.join(HERE, "two_wall_cavity_results.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2, default=_json_default)
    print(f"\nwrote {out_path}")
    return out


if __name__ == "__main__":
    main()
