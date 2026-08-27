"""
experiments/079-t28-y-wall-full-aperture-sum/y_wall_aperture_sum.py
============================================================================
Panel Iteration 56 (exp-079). Lead: MATERIALS & METAMATERIALS, by rotation.
Executes the reconciled Iteration-56 ranking's own Tier-0 item 1
(`experiments/078-.../phase5_redteam_audit.md` Sec 7, item 1) -- the single
highest-value item on the whole T28 board: does the flat/zero-amplitude
result exp-078's Phase-5 final audit found for the SINGLE-EDGE reduction
(`phase5_redteam_stationary_phase_check.py`) generalize to the FULL,
non-edge-reduced, y-mirrored SOURCE APERTURE SUM?

ZERO new FDTD calls. Imports, never reimplements:
  - `experiments/065-.../design_geometry.py` (`dg065`): `CONFIGS`
    (`C40`/`C60`/`C70`/`C80`/`G40`) -- `obj_y`, `y_lo`, `y_hi`, `A`, `d_sp`,
    `absorb`, `aperture_cells`.
  - `experiments/075-.../boundary_reflectance.py` (`br`): `damp_e_profile`,
    `nu_profile`, `n_profile_exact`, `reflection_coefficient`, `CPL`,
    `ABSORB_LIST` -- the already-gated (G-LOSSLESS/G-N1/G-PASSIVITY),
    Red-Team-adjudicated-on-convention (R8, Iteration 52) transfer-matrix
    reflectance. NOT reimplemented; a vectorized-over-theta variant is added
    below (Sec [2]) for performance, and VALIDATED bit-exact against the
    scalar, already-gated function before it is trusted at scale (Sec [2b]).
  - `experiments/078-.../y_wall_prescreen.py` (`ywp`): `CONGRUENT_KEYS`,
    `free_period_with_widening` (the SAME staged-widening idiom, including
    its own `SS_TOT_DEGENERATE` guard added at exp-078's own Phase-5
    mandatory-fix docket item 5), `_free_period_search`, `run69`.
  - `experiments/076-.../results.json::headline`: the REAL, already-
    collected `C40`/`G40`/`C80` dense 31-point/600nm/settled-STEPS=2800
    sweep, read (never hand-typed, R4) as the real reference data every
    period comparison below is scored against.

WHAT THIS FILE DOES -- see `phase1_proposal.md` for the full derivation
narrative; summary:

  [0] Geometry per config, and per-config theta_local(y_s) ENVELOPE across
      the real aperture (not just the single near edge exp-078 checked) --
      the natural per-point generalization of exp-078's own rigorous
      stationary-phase bounce-angle formula,
      theta_local(y_s) = atan(D_SP / (OBJ_Y + y_s)), re-derived from the
      SAME image-source geometry (image at (SRC_X,-y_s), observer at
      (PLANE_X,OBJ_Y)) for a GENERAL aperture point y_s, not merely y_lo.
  [1] Gate-check `reflection_coefficient` across the FULL observed
      theta_local envelope for all five configs (a wider range than ANY
      prior gate run in this program -- exp-078's own Phase-2 corrected
      envelope was 48-54deg; its Phase-5 rigorous-angle envelope was
      13.7-15.1deg, the single near edge ONLY; this file's full-aperture
      envelope reaches down to ~5deg at the far edge) -- before trusting
      any r(theta_local(y_s)) number anywhere in this file.
  [2] A vectorized-over-theta re-implementation of `br.reflection_
      coefficient`'s own recursive transfer-matrix loop (same algebra,
      arrayed over many theta_local(y_s) values at once instead of one
      scalar call per aperture point -- pure performance, not a new
      physics claim) -- VALIDATED bit-exact against the scalar,
      already-gated function at a battery of sample angles before use.
  [3] The full coherent aperture sum: for each config, each real aperture
      point y_s in [y_lo, y_hi] (the discretized source aperture, per
      `Sim.add_line_source`'s own raised-cosine edge-taper convention,
      re-derived from that function's own code -- NOT assumed), the
      per-point complex contribution to the REFLECTED (echo) field is
        amp(y_s) * r(theta_local(y_s); ABSORB) *
          exp(i*[phase(y_s;theta_beam) + k*dist_image(y_s)])
      where phase(y_s;theta_beam) = k*sin(theta_beam)*(y_s-OBJ_Y) is
      `add_line_source`'s own driven source phase (re-derived from that
      function's own code, Sec [3a]) and dist_image(y_s) =
      hypot(D_SP, OBJ_Y+y_s) is the image-source-to-observer propagation
      distance (the SAME quantity exp-078's own edge-image model already
      uses, generalized from y_lo to a general y_s). Evaluated as a
      trapezoidal-rule NUMERICAL INTEGRAL over y_s (not a bare discrete
      sum), at three discretizations (native grid dy=1 cell, and 2x/4x
      oversampled) as an explicit numerical-convergence check (Sec [4]) --
      does the integral's own value change if the number of aperture
      points is doubled/quadrupled?
  [4] Convergence check (does the answer change with more aperture points?).
  [5] The total reflected-field complex phasor E_echo(cfg,theta_beam), over
      the real 31-point 36-42deg/600nm grid, for all five configs. TWO
      scalar proxies reported symmetrically (not cherry-picked): PRIMARY
      Re{E_echo} (this bench's own house convention for a phasor's
      physical value, `lab/emit.py`'s `f(n)=Re{F e^{-i*omega*n}}` --
      Sec [5a] states this justification explicitly) and a robustness
      cross-check |E_echo|.
  [6] PAIR_PAD / PAIR_ABSORB40 / C80-C40 deltas of each proxy, scored
      against the SAME real, already-established reference periods via the
      SAME imported `_free_period_search`/staged-widening machinery this
      T28 sub-thread has used since Iteration 46, under the SAME
      pre-registered band (rel_dev<=0.30 SUPPORT / >1.00 REFUTE) exp-075/
      077/078 used throughout, with the SAME `SS_TOT_DEGENERATE` guard
      (exp-078's own Phase-5 hardening) active throughout.

Run: `python3 y_wall_aperture_sum.py` from this directory (or anywhere --
paths resolve from `__file__`). Writes `y_wall_aperture_sum_results.json`
and prints every table below; every number in `phase1_proposal.md` is
copied from that JSON/stdout, never hand-typed (R4).
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
    """House `_load()` pattern (boundary_reflectance.py / y_wall_prescreen.py
    / phase5_redteam_stationary_phase_check.py's own convention) for
    filename collisions across experiment directories."""
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


EXP065_DIR = os.path.join(ROOT, "experiments", "065-t24-absorb-boundary-sweep")
EXP075_DIR = os.path.join(ROOT, "experiments", "075-t28-absorb-boundary-wkb-reflectance")
EXP076_RESULTS = os.path.join(ROOT, "experiments", "076-t28-g40-pad-decorrelation", "results.json")
EXP078_DIR = os.path.join(ROOT, "experiments", "078-t28-y-wall-echo-prescreen")

dg065 = _load(os.path.join(EXP065_DIR, "design_geometry.py"), "_exp079_dg065")
br = _load(os.path.join(EXP075_DIR, "boundary_reflectance.py"), "_exp079_boundary_reflectance")
CPL = br.CPL

ywp = _load(os.path.join(EXP078_DIR, "y_wall_prescreen.py"), "_exp079_ywp")
run69 = ywp.run69
_free_period_search = ywp._free_period_search
free_period_with_widening = ywp.free_period_with_widening
CONGRUENT_KEYS = ywp.CONGRUENT_KEYS
SS_TOT_DEGENERATE_FLOOR = ywp.SS_TOT_DEGENERATE_FLOOR

def _trapz(y, x):
    """`numpy.trapz`/`numpy.trapezoid` compatibility shim -- numpy>=2.0
    renamed `trapz` to `trapezoid` and removed the old name; older numpy
    only has `trapz`. Tries both, never reimplements the rule itself."""
    fn = getattr(np, "trapezoid", None) or getattr(np, "trapz")
    return fn(y, x=x)


LAM600 = CPL[600]
K600 = 2.0 * math.pi / LAM600
TAPER_EDGE = dg065.TAPER  # 40 cells, add_line_source's own edge= argument


# ======================================================= [0] per-point angle
def theta_local_deg(y_s, cfg):
    """The rigorous, per-APERTURE-POINT stationary-phase bounce angle,
    measured from the y-wall's own normal -- the natural generalization of
    exp-078 Phase-5's single-near-edge formula (`phase5_redteam_audit.md`
    Sec 2a) from the one point y_lo to a GENERAL aperture point y_s.
    Re-derived, not copied: the image source sits at (SRC_X,-y_s) [mirror
    of the real point (SRC_X,y_s) through the y=0 wall -- the wall reflects
    y only, x=SRC_X is shared by EVERY point on the line source]; the
    observer sits at (PLANE_X,OBJ_Y). That line has Delta_x=D_SP (constant,
    independent of y_s, since every aperture point shares SRC_X) and
    Delta_y=OBJ_Y-(-y_s)=OBJ_Y+y_s -- so theta_local(y_s) =
    atan(D_SP/(OBJ_Y+y_s)), a PURE function of static per-config geometry
    and y_s, with ZERO theta_beam dependence anywhere (matching exp-078
    Phase-5's own finding at the single point y_s=y_lo, generalized here to
    every point)."""
    d_sp = cfg["d_sp"]
    denom = cfg["obj_y"] + np.asarray(y_s, dtype=float)
    return np.degrees(np.arctan(d_sp / denom))


def dist_image_cells(y_s, cfg):
    """Image-source-to-observer propagation distance, hypot(D_SP,OBJ_Y+y_s)
    -- the SAME quantity exp-078's own edge-image model already computes
    for y_s=y_lo (its `dist_image`), generalized to a general y_s."""
    d_sp = cfg["d_sp"]
    return np.hypot(d_sp, cfg["obj_y"] + np.asarray(y_s, dtype=float))


# ============================================== [3a] source amplitude taper
def aperture_amplitude(y_s, cfg):
    """Re-derived from `lab/fdtd2d.py::Sim.add_line_source`'s own code
    (verified against that function's source, not guessed): a unit-height
    top hat over the full aperture [y_lo,y_hi), with a raised-cosine
    (Hann-half) taper over the first/last `edge=TAPER` cells at each end --
    p[i] = 0.5*(1-cos(pi*i/edge)) for i<edge, p[i]=0.5*(1-cos(pi*(n-1-i)/
    edge)) for i>=n-edge, p[i]=1 elsewhere, where i=y_s-y_lo (integer index
    into the discrete source; here evaluated at CONTINUOUS i to support the
    numerical-integration convergence check, Sec [4] -- exactly reproduces
    the discrete formula at integer i, and is the natural continuous
    interpolant of it in between)."""
    y_lo = cfg["y_lo"]
    n = cfg["aperture_cells"]  # y_hi - y_lo, an INTEGER constant per config
    i = np.asarray(y_s, dtype=float) - y_lo
    edge = float(TAPER_EDGE)
    amp = np.ones_like(i)
    lo_mask = i < edge
    hi_mask = i > (n - 1 - edge)
    amp = np.where(lo_mask, 0.5 * (1.0 - np.cos(np.pi * np.clip(i, 0, None) / edge)), amp)
    amp = np.where(hi_mask, 0.5 * (1.0 - np.cos(np.pi * np.clip(n - 1 - i, 0, None) / edge)), amp)
    return amp


def source_driven_phase(y_s, theta_beam_deg, cfg):
    """Re-derived from `Sim.add_line_source`'s own code (verified, not
    assumed): `phase = k*sin(radians(angle_deg))*(yy - 0.5*(y_lo+y_hi))`.
    Since this bench's aperture is symmetric about OBJ_Y (0.5*(y_lo+y_hi)
    == obj_y EXACTLY for every congruent-series config -- checked in code,
    Sec [0] of main()), this is phase(y_s;theta_beam) =
    k*sin(theta_beam)*(y_s-OBJ_Y), matching `phase1_proposal.md`'s own
    stated convention and the task's own ingredient list."""
    theta = math.radians(theta_beam_deg)
    return K600 * math.sin(theta) * (np.asarray(y_s, dtype=float) - cfg["obj_y"])


# ========================================= [2] vectorized-over-theta r(theta)
def reflection_coefficient_vec(n_prof, theta_deg_arr, lam_cells):
    """SAME recursive transfer-matrix algebra as `br.reflection_coefficient`
    (line for line), arrayed over MANY theta_deg values at once (one array
    op per LAYER, ~40-80 layers, instead of one Python call per aperture
    point -- pure performance, not a new physics claim). n_prof is the
    SAME per-ABSORB complex index profile `br.n_profile_exact` already
    builds and this whole T28 sub-thread already trusts; only the loop
    structure differs from the scalar function, which this file VALIDATES
    bit-exact against before using at scale (Sec [2b] of main())."""
    theta = np.radians(np.asarray(theta_deg_arr, dtype=float))
    s2 = np.sin(theta) ** 2
    k0 = 2.0 * math.pi / lam_cells
    Zvac = 1.0 / np.cos(theta)
    Zin = np.zeros_like(theta, dtype=complex)
    n_prof = n_prof.astype(complex)
    for ni in n_prof:
        rad = (ni ** 2 - s2.astype(complex))
        kxi = k0 * np.sqrt(rad)
        Zi = ni / np.sqrt(rad)
        t = np.tan(kxi * 1.0)
        Zin = Zi * (Zin + 1j * Zi * t) / (Zi + 1j * Zin * t)
    return (Zin - Zvac) / (Zin + Zvac)


# ==================================================== [3] full aperture sum
def build_aperture_grid(cfg, oversample):
    """y_s grid over [y_lo,y_hi], `oversample`x the native per-cell (dy=1)
    resolution -- oversample=1 is the PRIMARY, physically-literal
    discretization (one point per real source grid cell, matching
    `Sim.add_line_source`'s own actual cell count exactly); oversample=2/4
    are numerical-integration convergence checks (Sec [4]), NOT claims
    about additional physical grid cells."""
    y_lo, y_hi = cfg["y_lo"], cfg["y_hi"]
    n = cfg["aperture_cells"]
    n_pts = oversample * n + 1
    return np.linspace(y_lo, y_hi, n_pts)


def echo_field_curve(cfg, absorb_for_r, thetas_beam_deg, oversample, r_vec_cache=None):
    """The total reflected-field complex phasor E_echo(theta_beam), one
    trapezoidal-rule numerical integral over y_s per theta_beam value.
    `r_vec_cache`, if given, is a precomputed (y_s_grid, r_of_ys) pair
    reused across calls at different theta_beam (r(theta_local(y_s)) does
    NOT depend on theta_beam -- computed ONCE per (config,oversample), per
    the task's own point: 'each aperture point has its own per-point
    rigorous bounce angle... independent of theta_beam')."""
    if r_vec_cache is not None:
        y_grid, r_of_ys, amp_of_ys, dist_img = r_vec_cache
    else:
        y_grid = build_aperture_grid(cfg, oversample)
        th_loc = theta_local_deg(y_grid, cfg)
        n_prof = br.n_profile_exact(br.nu_profile(br.damp_e_profile(absorb_for_r)),
                                     2.0 * math.pi / LAM600)
        r_of_ys = reflection_coefficient_vec(n_prof, th_loc, LAM600)
        amp_of_ys = aperture_amplitude(y_grid, cfg)
        dist_img = dist_image_cells(y_grid, cfg)

    curves = []
    for th_beam in thetas_beam_deg:
        phase_drive = source_driven_phase(y_grid, float(th_beam), cfg)
        integrand = amp_of_ys * r_of_ys * np.exp(1j * (phase_drive + K600 * dist_img))
        # complex trapezoidal-rule numerical integral over y_s (re/im parts
        # separately -- np.trapz on a complex array is not universally
        # supported across numpy versions, so this is done explicitly)
        re = float(_trapz(integrand.real, y_grid))
        im = float(_trapz(integrand.imag, y_grid))
        curves.append(complex(re, im))
    return np.array(curves, dtype=complex), (y_grid, r_of_ys, amp_of_ys, dist_img)


def rel_dev(p_real, p_model):
    return abs(p_model - p_real) / p_real


def score_period(name, p_real, p_model, out_print=True):
    rd = rel_dev(p_real, p_model)
    if rd <= 0.30:
        v = "SUPPORT"
    elif rd > 1.00:
        v = "REFUTE"
    else:
        v = "INCONCLUSIVE"
    if out_print:
        print(f"    {name}: P*_real={p_real:.4f}deg  P*_model={p_model:.4f}deg  "
              f"rel_dev={rd:.4f} -> {v}")
    return dict(p_real_deg=p_real, p_model_deg=p_model, rel_dev=rd, verdict=v)


def main():
    out = {}
    t_start = time.time()
    print("=" * 78)
    print("exp-079 -- y-wall FULL, non-edge-reduced aperture sum (coherent")
    print("Huygens-Fresnel echo model), zero new FDTD")
    print("=" * 78)

    # ---- [0] geometry + symmetric-aperture premise check ----
    print("\n[0] GEOMETRY PER CONFIG + symmetric-aperture premise "
          "(0.5*(y_lo+y_hi) == obj_y, required for source_driven_phase's "
          "own simplification)")
    geom = {}
    for key in CONGRUENT_KEYS:
        c = dg065.CONFIGS[key]
        mid = 0.5 * (c["y_lo"] + c["y_hi"])
        assert mid == c["obj_y"], (key, mid, c["obj_y"])
        geom[key] = dict(absorb=c["absorb"], pad=c["pad"], obj_y=c["obj_y"],
                          y_lo=c["y_lo"], y_hi=c["y_hi"], A=c["A"], d_sp=c["d_sp"],
                          aperture_cells=c["aperture_cells"])
        print(f"    {key}: absorb={c['absorb']:3d} pad={c['pad']:3d} "
              f"obj_y={c['obj_y']:4d} y_lo={c['y_lo']:3d} y_hi={c['y_hi']:4d} "
              f"A={c['A']} d_sp={c['d_sp']} aperture_cells={c['aperture_cells']} "
              f"mid==obj_y: {mid == c['obj_y']}")
    out["geometry"] = geom

    # ---- theta_local envelope across the FULL aperture, per config ----
    print("\n[0b] theta_local(y_s) ENVELOPE across the full aperture "
          "(vs exp-078 Phase-5's single-point 13.7-15.0deg at y_lo only)")
    envelope = {}
    all_lo, all_hi = [], []
    for key in CONGRUENT_KEYS:
        c = dg065.CONFIGS[key]
        y_edges = np.array([c["y_lo"], c["y_hi"]])
        th_edges = theta_local_deg(y_edges, c)
        lo, hi = float(th_edges.min()), float(th_edges.max())
        envelope[key] = dict(theta_local_at_y_lo=float(th_edges[0]),
                              theta_local_at_y_hi=float(th_edges[1]),
                              env_lo=lo, env_hi=hi)
        all_lo.append(lo)
        all_hi.append(hi)
        print(f"    {key}: theta_local(y_lo)={th_edges[0]:.4f}deg  "
              f"theta_local(y_hi)={th_edges[1]:.4f}deg  range=[{lo:.4f},{hi:.4f}]")
    global_lo, global_hi = min(all_lo) - 0.5, max(all_hi) + 0.5
    print(f"    GLOBAL envelope across all 5 configs (with 0.5deg margin): "
          f"[{global_lo:.4f},{global_hi:.4f}]deg -- never sampled by ANY "
          f"prior gate in this program (as-filed +-44deg; exp-078 corrected "
          f"48-54deg; exp-078 Phase-5 rigorous single-edge 13.7-15.1deg)")
    out["theta_local_envelope"] = envelope
    out["global_gate_envelope_deg"] = [global_lo, global_hi]

    # ---- [1] gate check at the full observed envelope ----
    print("\n[1] GATE CHECK at the full aperture's theta_local envelope "
          "(scalar, already-gated br.reflection_coefficient)")

    def gate_lossless_unimodular_range(lo, hi, n_trials=2000, seed=41):
        rng = np.random.default_rng(seed)
        worst = 0.0
        for _ in range(n_trials):
            length = int(rng.integers(5, 60))
            n_prof = 1.0 + 0.6 * rng.random(length)
            theta_deg = float(rng.uniform(lo, hi))
            r = br.reflection_coefficient(n_prof.astype(complex), theta_deg, 20.0)
            worst = max(worst, abs(abs(r) - 1.0))
        return worst

    def gate_single_layer_identity_range(lo, hi, n_trials=2000, seed=43):
        rng = np.random.default_rng(seed)
        worst = 0.0
        for _ in range(n_trials):
            n1 = complex(rng.uniform(0.5, 2.0), rng.uniform(0.0, 1.5))
            theta_deg = float(rng.uniform(lo, hi))
            lam = float(rng.uniform(10.0, 30.0))
            theta = math.radians(theta_deg)
            s2 = math.sin(theta) ** 2
            k0 = 2.0 * math.pi / lam
            kx1 = k0 * np.sqrt(n1 ** 2 - s2)
            Z1 = n1 / np.sqrt(n1 ** 2 - s2)
            Zin_direct = 1j * Z1 * np.tan(kx1 * 1.0)
            Zvac = 1.0 / math.cos(theta)
            r_direct = (Zin_direct - Zvac) / (Zin_direct + Zvac)
            r_loop = br.reflection_coefficient(np.array([n1]), theta_deg, lam)
            worst = max(worst, abs(r_direct - r_loop))
        return worst

    def gate_passivity_range(lo, hi, n_trials=2000, seed=47):
        rng = np.random.default_rng(seed)
        worst = 0.0
        for absorb in br.ABSORB_LIST:
            damp = br.damp_e_profile(absorb)
            nu = br.nu_profile(damp)
            n_exact = br.n_profile_exact(nu, 2.0 * math.pi / LAM600)
            for _ in range(n_trials // len(br.ABSORB_LIST)):
                theta_deg = float(rng.uniform(lo, hi))
                r = br.reflection_coefficient(n_exact, theta_deg, LAM600)
                worst = max(worst, abs(r))
        return worst

    g_lossless = gate_lossless_unimodular_range(global_lo, global_hi)
    g_n1 = gate_single_layer_identity_range(global_lo, global_hi)
    g_pass = gate_passivity_range(global_lo, global_hi)
    print(f"    G-LOSSLESS ({global_lo:.2f}-{global_hi:.2f}deg, 2000 trials): "
          f"worst ||r|-1| = {g_lossless:.3e}  PASS={g_lossless < 1e-9}")
    print(f"    G-N1       ({global_lo:.2f}-{global_hi:.2f}deg, 2000 trials): "
          f"worst |r_loop-r_direct| = {g_n1:.3e}  PASS={g_n1 < 1e-12}")
    print(f"    G-PASSIVITY({global_lo:.2f}-{global_hi:.2f}deg, 2000 trials/depth): "
          f"worst |r| = {g_pass:.6f}  PASS={g_pass <= 1.0 + 1e-9}")
    gates = dict(g_lossless_worst_dev=g_lossless, g_lossless_pass=bool(g_lossless < 1e-9),
                 g_n1_worst_dev=g_n1, g_n1_pass=bool(g_n1 < 1e-12),
                 g_passivity_worst_abs_r=g_pass, g_passivity_pass=bool(g_pass <= 1.0 + 1e-9))
    assert gates["g_lossless_pass"] and gates["g_n1_pass"] and gates["g_passivity_pass"], \
        "full-aperture envelope gate FAILED -- do not trust r(theta_local(y_s))"
    out["gates_at_full_envelope"] = gates

    # ---- [2b] validate the vectorized r(theta) against the scalar, gated one ----
    print("\n[2b] VALIDATE reflection_coefficient_vec against the scalar, "
          "already-gated br.reflection_coefficient (bit-exact required "
          "before using the vectorized form at scale)")
    val_thetas = np.array([global_lo, 6.0, 9.0, 12.0, global_hi])
    max_val_dev = 0.0
    for absorb in br.ABSORB_LIST:
        n_prof = br.n_profile_exact(br.nu_profile(br.damp_e_profile(absorb)),
                                     2.0 * math.pi / LAM600)
        r_vec = reflection_coefficient_vec(n_prof, val_thetas, LAM600)
        for i, th in enumerate(val_thetas):
            r_scalar = br.reflection_coefficient(n_prof, float(th), LAM600)
            dev = abs(r_vec[i] - r_scalar)
            max_val_dev = max(max_val_dev, dev)
    print(f"    max |r_vec - r_scalar| over {len(br.ABSORB_LIST)} ABSORB depths x "
          f"{len(val_thetas)} sample angles = {max_val_dev:.3e}")
    assert max_val_dev < 1e-12, "vectorized reflection coefficient does NOT match the scalar, gated function"
    out["vectorized_r_validation_max_dev"] = max_val_dev
    print("    -> vectorized form reproduces the scalar, already-gated function to float precision.")

    # ---- real reference data + periods (recomputed, R4) ----
    with open(EXP076_RESULTS) as f:
        res76 = json.load(f)
    headline = res76["headline"]
    thetas = np.array(headline["theta"])
    real_c40 = np.array(headline["C40"])
    real_g40 = np.array(headline["G40"])
    real_c80 = np.array(headline["C80"])
    real_delta_pad = real_g40 - real_c40
    real_delta_absorb40 = real_c80 - real_g40
    real_delta_c80_c40 = real_c80 - real_c40

    print(f"\n[3] REAL reference periods (re-derived from committed data via "
          f"the SAME imported _free_period_search, {len(thetas)} angles, "
          f"{thetas.min()}-{thetas.max()}deg, 600nm)")
    real_stages = {"pair_pad": [], "pair_absorb40": [], "c80_c40": []}
    real_free_pad = free_period_with_widening(thetas, real_delta_pad, "real PAIR_PAD",
                                               real_stages["pair_pad"])
    real_free_absorb40 = free_period_with_widening(thetas, real_delta_absorb40,
                                                     "real PAIR_ABSORB40", real_stages["pair_absorb40"])
    real_free_c80c40 = free_period_with_widening(thetas, real_delta_c80_c40, "real C80-C40",
                                                   real_stages["c80_c40"])
    REFERENCE_PERIODS = dict(
        c80_c40_deg=real_free_c80c40["p_star_deg"],
        pair_pad_deg=real_free_pad["p_star_deg"],
        pair_absorb40_deg=real_free_absorb40["p_star_deg"])
    print(f"    REFERENCE_PERIODS used for scoring below: {REFERENCE_PERIODS} "
          f"(citations: 2.8421 / 4.6113 / 4.1761 deg)")
    out["real_periods"] = dict(pair_pad=real_free_pad, pair_absorb40=real_free_absorb40,
                                c80_c40=real_free_c80c40, stages=real_stages,
                                reference_periods_deg=REFERENCE_PERIODS)

    # ---- [4] convergence check: does the answer change with more points? ----
    print("\n[4] NUMERICAL-CONVERGENCE CHECK: 1x (native, dy=1 cell -- the "
          "REAL per-cell source resolution) vs 2x vs 4x oversampled "
          "trapezoidal-rule aperture integral")
    conv = {}
    for oversample in (1, 2, 4):
        curves_over = {}
        caches = {}
        for key in CONGRUENT_KEYS:
            c = dg065.CONFIGS[key]
            curve, cache = echo_field_curve(c, c["absorb"], thetas, oversample)
            curves_over[key] = curve
            caches[key] = cache
        model_delta_pad = (curves_over["G40"] - curves_over["C40"]).real
        model_delta_absorb40 = (curves_over["C80"] - curves_over["G40"]).real
        model_delta_c80c40 = (curves_over["C80"] - curves_over["C40"]).real
        stg = []
        fp_pad = free_period_with_widening(thetas, model_delta_pad,
                                            f"conv os={oversample} PAIR_PAD", stg)
        n_pts = caches["C40"][0].size
        conv[oversample] = dict(
            n_points_C40=int(n_pts),
            ptp_pair_pad=float(np.ptp(model_delta_pad)),
            ptp_pair_absorb40=float(np.ptp(model_delta_absorb40)),
            ptp_c80_c40=float(np.ptp(model_delta_c80c40)),
            pair_pad_p_star_deg=fp_pad["p_star_deg"],
            pair_pad_r_squared=fp_pad["r_squared"])
        print(f"    oversample={oversample}x  n_points(C40)={n_pts}  "
              f"ptp(PAIR_PAD)={conv[oversample]['ptp_pair_pad']:.6e}  "
              f"ptp(PAIR_ABSORB40)={conv[oversample]['ptp_pair_absorb40']:.6e}  "
              f"ptp(C80-C40)={conv[oversample]['ptp_c80_c40']:.6e}  "
              f"PAIR_PAD P*={fp_pad['p_star_deg']:.4f}deg R^2={fp_pad['r_squared']:.4f}")
    rel_1_2 = abs(conv[2]["ptp_pair_pad"] - conv[1]["ptp_pair_pad"]) / conv[1]["ptp_pair_pad"] \
        if conv[1]["ptp_pair_pad"] else float("nan")
    rel_2_4 = abs(conv[4]["ptp_pair_pad"] - conv[2]["ptp_pair_pad"]) / conv[2]["ptp_pair_pad"] \
        if conv[2]["ptp_pair_pad"] else float("nan")
    print(f"    relative change in ptp(PAIR_PAD), 1x->2x = {rel_1_2:.4e}, "
          f"2x->4x = {rel_2_4:.4e}  (small and shrinking = converged)")
    conv["relative_change_ptp_pair_pad_1x_to_2x"] = rel_1_2
    conv["relative_change_ptp_pair_pad_2x_to_4x"] = rel_2_4
    conv["converged"] = bool(rel_2_4 < 0.01)
    out["convergence_check"] = conv
    print(f"    CONVERGED (2x->4x relative change < 1%): {conv['converged']}")

    # ---- [5] PRIMARY: full curves at the native (1x, physically-literal) grid ----
    print("\n[5] PRIMARY MODEL -- full coherent aperture-sum echo field "
          "E_echo(cfg,theta_beam), native (1x, dy=1 cell) discretization")
    OVERSAMPLE_PRIMARY = 1
    curves = {}
    caches = {}
    for key in CONGRUENT_KEYS:
        c = dg065.CONFIGS[key]
        curve, cache = echo_field_curve(c, c["absorb"], thetas, OVERSAMPLE_PRIMARY)
        curves[key] = curve
        caches[key] = cache
        re = curve.real
        ab = np.abs(curve)
        print(f"    {key}: ptp(Re E_echo)={np.ptp(re):.6e}  mean(|E_echo|)={ab.mean():.6e}  "
              f"ptp(|E_echo|)={np.ptp(ab):.6e}  n_points={cache[0].size}")
    out["primary_model_curves"] = {
        k: dict(re_e_echo=curves[k].real.tolist(), abs_e_echo=np.abs(curves[k]).tolist(),
                ptp_re=float(np.ptp(curves[k].real)), ptp_abs=float(np.ptp(np.abs(curves[k]))))
        for k in CONGRUENT_KEYS
    }

    # ---- [5b] diagnostic: does a T21-like period already dominate EACH
    # config's OWN Re{E_echo} curve individually (not just the pair deltas)?
    # A=752 is bit-identical across the whole congruent series, and this
    # model's own driven-phase term k*sin(theta_beam)*(y_s-OBJ_Y) is the
    # SAME ramp that produces T21's own established fringe in the REAL
    # (non-reflected) aperture -- if that same ramp dominates the coherent
    # SUM here too (plausible: the reflectance/propagation-phase envelope
    # varies slowly across the aperture compared to the driven-phase ramp),
    # every config's own curve, and hence every pairwise delta, would show
    # a period near T21's 1.9608deg regardless of which two configs are
    # differenced -- exactly what would explain [6]'s three near-identical
    # model periods (1.99/2.02/2.03deg) mechanistically, not by coincidence.
    print("\n[5b] DIAGNOSTIC -- per-config free-period fit on Re{E_echo(cfg,theta)} "
          "ALONE (not a pair delta): does a T21-like (~1.96deg) period already "
          "dominate each config's own curve individually?")
    per_config_periods = {}
    per_config_stages = {}
    for key in CONGRUENT_KEYS:
        stg = []
        fp = free_period_with_widening(thetas, curves[key].real, f"solo {key}", stg)
        per_config_periods[key] = fp
        per_config_stages[key] = stg
    out["per_config_solo_free_period"] = dict(chosen=per_config_periods, stages=per_config_stages)
    t21_p39 = dg065.dg048.ripple_period_deg(752, LAM600, 39.0)
    print(f"    (T21's own established fringe period, A=752, 600nm, 39deg: "
          f"{t21_p39:.4f}deg -- re-derived here from the already-committed "
          f"dg048.ripple_period_deg, not hand-typed)")
    out["t21_fringe_period_A752_600nm_39deg"] = t21_p39

    # ---- [5a] proxy justification ----
    print("\n[5a] SCALAR PROXY CHOICE: PRIMARY = Re{E_echo} (this bench's own "
          "house phasor convention, lab/emit.py's f(n)=Re{F e^{-i*omega*n}} "
          "-- the physically-meaningful, sign-carrying field value a real "
          "time-domain monitor would record); SECONDARY robustness cross-"
          "check = |E_echo| (sign-blind magnitude). Both reported "
          "symmetrically -- neither is dropped or cherry-picked based on "
          "which fits better (R5 discipline: two proxy CHOICES on one "
          "already-derived model, not a search over candidate mechanisms).")

    # ---- [6] pair deltas, both proxies, scored ----
    print("\n[6] MODEL PAIR DELTAS (PAIR_PAD / PAIR_ABSORB40 / C80-C40), "
          "PRIMARY proxy Re{E_echo}, scored against real periods")
    model_delta_pad_re = (curves["G40"] - curves["C40"]).real
    model_delta_absorb40_re = (curves["C80"] - curves["G40"]).real
    model_delta_c80c40_re = (curves["C80"] - curves["C40"]).real

    primary_stages = {"pair_pad": [], "pair_absorb40": [], "c80_c40": []}
    primary_free_pad = free_period_with_widening(thetas, model_delta_pad_re,
                                                  "model(Re) PAIR_PAD", primary_stages["pair_pad"])
    primary_free_absorb40 = free_period_with_widening(thetas, model_delta_absorb40_re,
                                                        "model(Re) PAIR_ABSORB40",
                                                        primary_stages["pair_absorb40"])
    primary_free_c80c40 = free_period_with_widening(thetas, model_delta_c80c40_re,
                                                      "model(Re) C80-C40", primary_stages["c80_c40"])
    primary_scores = {}
    primary_scores["c80_c40_vs_2.8421"] = score_period(
        "Re-model C80-C40 vs real", REFERENCE_PERIODS["c80_c40_deg"], primary_free_c80c40["p_star_deg"])
    primary_scores["pair_pad_vs_4.6113"] = score_period(
        "Re-model PAIR_PAD vs real", REFERENCE_PERIODS["pair_pad_deg"], primary_free_pad["p_star_deg"])
    primary_scores["pair_absorb40_vs_4.1761"] = score_period(
        "Re-model PAIR_ABSORB40 vs real", REFERENCE_PERIODS["pair_absorb40_deg"], primary_free_absorb40["p_star_deg"])
    print("\n[6a] DIAGNOSTIC -- how close are the PRIMARY model's own three "
          "periods to T21's OWN established fringe (1.9608deg, A=752, "
          "39deg, 600nm) vs to T28's own real targets? (disclosed "
          "look-elsewhere comparison, R5 -- see phase1_proposal.md Sec 3.3/7)")
    t21_ref = dg065.dg048.ripple_period_deg(752, LAM600, 39.0)
    vs_t21 = {}
    for name, p_model in (("c80_c40", primary_free_c80c40["p_star_deg"]),
                           ("pair_pad", primary_free_pad["p_star_deg"]),
                           ("pair_absorb40", primary_free_absorb40["p_star_deg"])):
        rd_t21 = rel_dev(t21_ref, p_model)
        vs_t21[name] = rd_t21
        print(f"    {name}: P*_model={p_model:.4f}deg  vs T21 fringe "
              f"{t21_ref:.4f}deg -> rel_dev={rd_t21:.4f}")
    out["primary_model_periods_vs_t21_fringe_rel_dev"] = vs_t21

    out["primary_proxy_re"] = dict(
        pair_pad=primary_free_pad, pair_absorb40=primary_free_absorb40, c80_c40=primary_free_c80c40,
        stages=primary_stages, scores=primary_scores,
        ptp_delta_pad=float(np.ptp(model_delta_pad_re)),
        ptp_delta_absorb40=float(np.ptp(model_delta_absorb40_re)),
        ptp_delta_c80c40=float(np.ptp(model_delta_c80c40_re)))

    print("\n[6b] MODEL PAIR DELTAS, SECONDARY proxy |E_echo| (robustness cross-check)")
    model_delta_pad_abs = np.abs(curves["G40"]) - np.abs(curves["C40"])
    model_delta_absorb40_abs = np.abs(curves["C80"]) - np.abs(curves["G40"])
    model_delta_c80c40_abs = np.abs(curves["C80"]) - np.abs(curves["C40"])
    secondary_stages = {"pair_pad": [], "pair_absorb40": [], "c80_c40": []}
    secondary_free_pad = free_period_with_widening(thetas, model_delta_pad_abs,
                                                     "model(abs) PAIR_PAD", secondary_stages["pair_pad"])
    secondary_free_absorb40 = free_period_with_widening(thetas, model_delta_absorb40_abs,
                                                          "model(abs) PAIR_ABSORB40",
                                                          secondary_stages["pair_absorb40"])
    secondary_free_c80c40 = free_period_with_widening(thetas, model_delta_c80c40_abs,
                                                        "model(abs) C80-C40", secondary_stages["c80_c40"])
    secondary_scores = {}
    secondary_scores["c80_c40_vs_2.8421"] = score_period(
        "abs-model C80-C40 vs real", REFERENCE_PERIODS["c80_c40_deg"], secondary_free_c80c40["p_star_deg"])
    secondary_scores["pair_pad_vs_4.6113"] = score_period(
        "abs-model PAIR_PAD vs real", REFERENCE_PERIODS["pair_pad_deg"], secondary_free_pad["p_star_deg"])
    secondary_scores["pair_absorb40_vs_4.1761"] = score_period(
        "abs-model PAIR_ABSORB40 vs real", REFERENCE_PERIODS["pair_absorb40_deg"], secondary_free_absorb40["p_star_deg"])
    out["secondary_proxy_abs"] = dict(
        pair_pad=secondary_free_pad, pair_absorb40=secondary_free_absorb40, c80_c40=secondary_free_c80c40,
        stages=secondary_stages, scores=secondary_scores,
        ptp_delta_pad=float(np.ptp(model_delta_pad_abs)),
        ptp_delta_absorb40=float(np.ptp(model_delta_absorb40_abs)),
        ptp_delta_c80c40=float(np.ptp(model_delta_c80c40_abs)))

    # ---- ss_tot scale sanity guard (exp-078 Phase-5 hardening, applied here) ----
    print("\n[6c] SS_TOT-SCALE SANITY (exp-078 Phase-5's own SS_TOT_DEGENERATE "
          "hardening, applied explicitly here): model ss_tot vs real ss_tot, "
          "same statistic, PRIMARY proxy PAIR_PAD")
    ss_tot_model_pad = float(np.sum((model_delta_pad_re - np.mean(model_delta_pad_re)) ** 2))
    ss_tot_real_pad = float(np.sum((real_delta_pad - np.mean(real_delta_pad)) ** 2))
    ss_ratio = ss_tot_model_pad / ss_tot_real_pad
    print(f"    ss_tot(model, Re-proxy PAIR_PAD) = {ss_tot_model_pad:.6e}")
    print(f"    ss_tot(real PAIR_PAD)             = {ss_tot_real_pad:.6e}")
    print(f"    ratio (model/real) = {ss_ratio:.6e}  "
          f"(exp-078's own flat single-edge model measured 5.9e-27 here -- "
          f"a ratio many orders of magnitude below 1 would mean this file's "
          f"model is ALSO degenerate/flat, not a real oscillation)")
    ss_degenerate = ss_tot_model_pad < SS_TOT_DEGENERATE_FLOOR
    print(f"    ss_tot below the SS_TOT_DEGENERATE floor ({SS_TOT_DEGENERATE_FLOOR:.0e}): "
          f"{ss_degenerate}")
    out["ss_tot_sanity"] = dict(ss_tot_model_pad=ss_tot_model_pad, ss_tot_real_pad=ss_tot_real_pad,
                                 ratio_model_to_real=ss_ratio, ss_tot_degenerate=bool(ss_degenerate))

    # ---- [7] summary ----
    print("\n[7] SUMMARY")
    n_primary_support = sum(1 for v in primary_scores.values() if v["verdict"] == "SUPPORT")
    n_primary_refute = sum(1 for v in primary_scores.values() if v["verdict"] == "REFUTE")
    n_secondary_support = sum(1 for v in secondary_scores.values() if v["verdict"] == "SUPPORT")
    n_secondary_refute = sum(1 for v in secondary_scores.values() if v["verdict"] == "REFUTE")
    print(f"    PRIMARY (Re{{E_echo}}):   {n_primary_support}/3 SUPPORT, "
          f"{n_primary_refute}/3 REFUTE")
    print(f"    SECONDARY (|E_echo|):    {n_secondary_support}/3 SUPPORT, "
          f"{n_secondary_refute}/3 REFUTE")
    print(f"    ss_tot ratio (model PAIR_PAD / real PAIR_PAD, primary proxy): {ss_ratio:.3e}")
    print(f"    numerical convergence (2x->4x relative ptp change): {rel_2_4:.4e}, "
          f"converged={conv['converged']}")
    out["summary"] = dict(
        n_primary_support=n_primary_support, n_primary_refute=n_primary_refute,
        n_secondary_support=n_secondary_support, n_secondary_refute=n_secondary_refute,
        ss_tot_ratio_primary_pair_pad=ss_ratio, converged=conv["converged"])
    print(f"\n    elapsed: {time.time() - t_start:.1f}s")

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

    out_path = os.path.join(HERE, "y_wall_aperture_sum_results.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2, default=_json_default)
    print(f"\nwrote {out_path}")
    return out


if __name__ == "__main__":
    main()
