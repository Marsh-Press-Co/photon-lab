"""exp-051 design geometry -- the alias-lattice difficulty predictor.
=============================================================================
Panel Iteration 28 (lead: ELECTROMAGNETISM, rotation). Phase-4 implementation
of the design frozen in `NOTES.md` (Phase-3-corrected: the crux quantity is
QUANTUM OPTICS' alias-lattice term, NOT the Phase-1 `phase_offset`).

PROVENANCE / INDEPENDENCE (NOTES.md idealization 10). Every line below was
written from the frozen `NOTES.md` spec. No Phase-2 seat's scratch code was
opened, read or copied -- agreement with QUANTUM's and Red Team's independent
pre-checks on the calibration 18 is the cross-validation this cycle is
testing for, and copying would have destroyed it.

WHAT IS REUSED, NOT REIMPLEMENTED (house rule R4 -- every quantity below is
the actual committed function, invoked):

  from `experiments/050-.../design_geometry.py`
      `_geom_derived`, `_src_amp`, `_G_for_g`, `GEOM78`, `GEOM_EXP042_OLD`,
      `gaussian_angle_weights`, `aperture_profile`, `CPL`,
      `beam_divergence_{incoherent,incoherent_corrected,coherent}`
  from `experiments/042-.../design_geometry.py` (via exp-050's own handle)
      module-global `edge_diffraction_c_empty` / `_corrected`
      -- the P-ALIAS-0a regression anchor
  from `experiments/048-.../design_geometry.py` (via exp-050's own handle)
      `ripple_period_deg` -- the descriptive local-period diagnostic
  from `lab/ambient.py`
      `window_means`, `weber`

exp-050's module is loaded via `importlib.util` under a PRIVATE module name,
per its own docstring's basename-collision warning: exp-042's, exp-048's and
exp-050's modules all share the basename `design_geometry`, and so does this
one -- importing any two under the default name would silently alias one to
the other. exp-050's module already loads exp-042's and exp-048's under its
own private names and exposes them as `.dg042` / `.dg048`; those handles are
reused here rather than re-executing either source module a second time.

NOTHING under `lab/` or in experiments 042/048/049/050 is modified.

WHAT IS NEW HERE (the two additions the frozen spec asks for):

  1. `edge_diffraction_c_empty_g(theta, lam, g, convention)` -- the
     geometry-parameterized single-angle Weber contrast, for BOTH committed
     conventions. exp-048's module has the `corrected` half already
     (`edge_diffraction_c_empty_corrected(theta,lam,g)`); the
     obliquity-on-E half (exp-042's `edge_diffraction_c_empty`, generalized)
     did not exist at any geometry but A=752, exactly as exp-050 found for
     `beam_divergence_incoherent`. Both halves here are algebraically the
     committed formula with `_geom_derived`'s `r`/`obliquity` substituted for
     exp-042's module-globals -- P-ALIAS-0a scores that claim to 1e-9.
  2. `alias_coeff` / `E_pred` -- QUANTUM's alias-lattice term, exactly as
     frozen in NOTES.md Setup, plus the descriptive samples-per-period
     diagnostic (NOTES.md idealization 5: `P` is DESCRIPTIVE ONLY, it is
     never the crux quantity -- that was the Phase-1 design's error).

MANDATORY MEMOIZATION (Red Team docket item 2, NOTES.md Setup -- "not
optional"). `_geom_derived(g)` and the two propagator matrices are built once
per `(geometry, lambda)` and cached; the dense alias scan is evaluated as a
BLAS matmul over a chunk of angles at a time rather than one matvec per
angle, and the whole 216-combination sweep shares one master scan per
`(geometry, lambda)` because every in-scope angle window lands on the same
0.01-degree integer lattice. Unmemoized this sweep costs hours.

`A = g["OBJ_Y"] - g["ABSORB"]` -- there is NO `g["A"]` key in either geometry
dict (Red Team docket item 5).
"""

import importlib.util
import inspect
import sys
from pathlib import Path

import numpy as np

_REPO_ROOT = Path(__file__).resolve().parents[2]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from lab import ambient as amb  # noqa: E402


def _load(name, relpath):
    spec = importlib.util.spec_from_file_location(name, _REPO_ROOT / relpath)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# Private module name -- see docstring (four files share this basename).
dg050 = _load("_exp051_exp050_design_geometry",
              "experiments/050-n-convergence-a724-geometry/design_geometry.py")
dg042 = dg050.dg042          # exp-050's own already-loaded handle, not a re-import
dg048 = dg050.dg048

# ------------------------------------------------------------- reused as-is
GEOM78 = dg050.GEOM78
GEOM_EXP042_OLD = dg050.GEOM_EXP042_OLD
CPL = dg050.CPL
gaussian_angle_weights = dg050.gaussian_angle_weights
aperture_profile = dg048.aperture_profile
_geom_derived = dg048._geom_derived
_src_amp = dg048._src_amp
_G_for_g = dg050._G_for_g
ripple_period_deg = dg048.ripple_period_deg

beam_divergence_incoherent = dg050.beam_divergence_incoherent
beam_divergence_incoherent_corrected = dg050.beam_divergence_incoherent_corrected
beam_divergence_coherent = dg050.beam_divergence_coherent

# exp-042's module-global single-angle functions -- the P-ALIAS-0a anchor
edge_diffraction_c_empty_042 = dg042.edge_diffraction_c_empty
edge_diffraction_c_empty_corrected_042 = dg042.edge_diffraction_c_empty_corrected

# `half_width_factor` is READ from the committed `gaussian_angle_weights`
# signature, not retyped -- NOTES.md Setup ("read from the committed
# gaussian_angle_weights"). Asserted so a future default change is caught.
HALF_WIDTH_FACTOR = float(
    inspect.signature(gaussian_angle_weights).parameters["half_width_factor"].default
)
assert HALF_WIDTH_FACTOR == 2.5, f"half_width_factor drift: {HALF_WIDTH_FACTOR}"

# The Gaussian kernel's own sigma convention, likewise read from the committed
# source rather than retyped (`sigma = fwhm_deg / 2.3548`).
FWHM_TO_SIGMA = 2.3548

STEP_DEG = 0.01          # NOTES.md idealization 7: fixed across all 216
STEP_DEG_FINE = 0.005    # NOTES.md idealization 7: the convergence spot-check

# Single-angle convention keys. NOTE the mapping from the three
# `beam_divergence_*` functions:
#   incoherent           -> "incoherent" (obliquity-on-E, |E|^2)
#   incoherent_corrected -> "corrected"  (obliquity-on-H, -Re(E conj(H)))
#   coherent             -> "incoherent"
# The last one is exact, not an approximation: at a SINGLE angle the coherent
# sum reduces to b = w*|G@amp|^2, and `amb.weber` is homogeneous of degree 0
# in a uniform rescale of the profile (exp-042 mandatory fix 2), so the
# coherent single-angle Weber contrast is bit-identical to `incoherent`'s.
# That is what makes the 9 `coherent` FWHM=20 rows a degenerate-x1 control
# (phase3_synthesis.md S3 item 3): identical E_pred, different committed
# labels.
CONVENTIONS = ("incoherent", "corrected")
FUNC_TO_CONVENTION = {
    "incoherent": "incoherent",
    "incoherent_corrected": "corrected",
    "coherent": "incoherent",
}


# =====================================================================
#  Mandatory memoization (Red Team docket 2)
# =====================================================================
def _gkey(g):
    return tuple(sorted(g.items()))


_GEOM_CACHE = {}
_PROP_CACHE = {}
_SCAN_CACHE = {}

MEMO_STATS = dict(geom_builds=0, prop_builds=0, scan_builds=0,
                  scan_points=0, scalar_evals=0)


def geom_derived_memo(g):
    """`_geom_derived(g)` -- the committed exp-048 function, invoked ONCE per
    geometry and cached (Red Team docket 2)."""
    key = _gkey(g)
    if key not in _GEOM_CACHE:
        MEMO_STATS["geom_builds"] += 1
        _GEOM_CACHE[key] = _geom_derived(g)
    return _GEOM_CACHE[key]


def propagators_memo(g, lam_cells):
    """The two propagator matrices for one `(geometry, lambda)`, built ONCE
    and cached (Red Team docket 2):

        G0  = exp(i(k r - pi/4))/sqrt(r)              (bare, the E half)
        Gob = G0 * obliquity                          (obliquity-weighted)

    Both come from the committed `_G_for_g` (exp-050), which is exp-042's own
    `_G_for` generalized -- `obliquity=True` reproduces exp-042's `_G_for`,
    `obliquity=False` reproduces its `_G0_for`."""
    gd = geom_derived_memo(g)
    key = (_gkey(g), lam_cells)
    if key not in _PROP_CACHE:
        MEMO_STATS["prop_builds"] += 1
        k, G_ob = _G_for_g(lam_cells, gd, obliquity=True)
        _, G0 = _G_for_g(lam_cells, gd, obliquity=False)
        _PROP_CACHE[key] = (k, G0, G_ob)
    k, G0, G_ob = _PROP_CACHE[key]
    return gd, k, G0, G_ob


def _reduce(b, gd, g):
    """`amb.window_means` + `amb.weber`, invoked directly on the committed
    functions -- the same reduction every measured row in exp-041/042/049/050
    went through."""
    bo, bf = amb.window_means(b, gd["y_lo"], gd["obj_y"],
                              g["R_OUT"], g["GUARD_OUT"], g["W_FLANK"])
    return amb.weber(bo, bf)


# =====================================================================
#  New: the geometry-parameterized single-angle Weber contrast
# =====================================================================
def edge_diffraction_c_empty_g(theta_deg, lam_cells, g, convention="incoherent"):
    """Single-angle empty-scene Weber contrast c(theta) at geometry `g`.

    `convention="incoherent"`  -- exp-042's committed module-global
        `edge_diffraction_c_empty(theta, lam, obliquity=True)`, i.e. the
        ORIGINAL obliquity-on-E reduction b = |G_ob @ amp|^2. This is the
        single-angle fringe underlying BOTH `beam_divergence_incoherent` and
        `beam_divergence_coherent`.
    `convention="corrected"`   -- exp-042's committed module-global
        `edge_diffraction_c_empty_corrected(theta, lam)` (the Phase-5
        erratum convention), b = -Re(E conj(H)) with E bare and H
        obliquity-weighted. This is the fringe underlying
        `beam_divergence_incoherent_corrected`.

    Both are the committed formula evaluated on `_geom_derived`'s own
    `r`/`obliquity` instead of exp-042's module-globals -- P-ALIAS-0a scores
    that equivalence at g=GEOM_EXP042_OLD to 1e-9 on 18 spot points."""
    gd, k, G0, G_ob = propagators_memo(g, lam_cells)
    MEMO_STATS["scalar_evals"] += 1
    amp = _src_amp(theta_deg, k, gd)
    if convention == "incoherent":
        b = np.abs(G_ob @ amp) ** 2
    elif convention == "corrected":
        E = G0 @ amp
        H = G_ob @ amp
        b = -np.real(E * np.conj(H))
    else:
        raise ValueError(f"unknown convention {convention!r}")
    return _reduce(b, gd, g)


def _src_amp_batch(thetas_deg, k, gd):
    """Column-wise batch of `_src_amp` -- the SAME arithmetic, one BLAS-
    friendly array instead of a Python loop (Red Team docket 2). Column j is
    `_src_amp(thetas_deg[j], k, gd)`; run.py asserts that to 1e-9 before any
    science number is produced."""
    dy = gd["y_src"] - gd["obj_y"]
    ks = k * np.sin(np.radians(np.asarray(thetas_deg, dtype=float)))
    phase = ks[None, :] * dy[:, None]
    return gd["p"][:, None] * np.exp(1j * phase)


def scan_c_empty(g, lam_cells, i_lo, i_hi, step=STEP_DEG, chunk=512):
    """Dense single-angle scan of BOTH conventions over the integer lattice
    theta = i*step for i in [i_lo, i_hi], memoized per
    `(geometry, lambda, step)`.

    Angles are addressed by integer lattice index, never by float value: every
    in-scope window edge (theta0 +- 2.5*FWHM, theta0 in {36,38,40},
    FWHM in {2,5,10,20}) is an exact multiple of 0.5 deg and hence an exact
    multiple of `step`, so one master scan per (geometry, lambda) serves all
    36 cells with no interpolation and no float-comparison hazard.

    The two conventions share their matmuls: `G_ob @ AMP` is needed by both
    (as |.|^2 and as the H half), so one pass over the angle grid produces
    both fringes."""
    key = (_gkey(g), lam_cells, step)
    cached = _SCAN_CACHE.get(key)
    if cached is not None and cached["i_lo"] <= i_lo and cached["i_hi"] >= i_hi:
        return cached
    if cached is not None:                       # widen, keep one scan per key
        i_lo = min(i_lo, cached["i_lo"])
        i_hi = max(i_hi, cached["i_hi"])

    gd, k, G0, G_ob = propagators_memo(g, lam_cells)
    npts = i_hi - i_lo + 1
    idx = np.arange(i_lo, i_hi + 1)
    thetas = idx * step
    c_inc = np.empty(npts)
    c_cor = np.empty(npts)
    for a in range(0, npts, chunk):
        b_ = min(a + chunk, npts)
        AMP = _src_amp_batch(thetas[a:b_], k, gd)
        Hb = G_ob @ AMP
        Eb = G0 @ AMP
        prof_inc = np.abs(Hb) ** 2
        prof_cor = -np.real(Eb * np.conj(Hb))
        for j in range(b_ - a):
            c_inc[a + j] = _reduce(prof_inc[:, j], gd, g)
            c_cor[a + j] = _reduce(prof_cor[:, j], gd, g)
    MEMO_STATS["scan_builds"] += 1
    MEMO_STATS["scan_points"] += npts
    out = dict(i_lo=i_lo, i_hi=i_hi, step=step, thetas=thetas,
               incoherent=c_inc, corrected=c_cor)
    _SCAN_CACHE[key] = out
    return out


def c_window(theta0_deg, fwhm_deg, lam_cells, g, convention, step=STEP_DEG):
    """`c(theta0 + u)` on the dense u-grid, and the u-grid itself.

    The support is the SAME +-half_width_factor*FWHM window the committed
    quadrature spans (NOTES.md Setup), sampled at `step`."""
    hw = HALF_WIDTH_FACTOR * fwhm_deg
    i_lo = int(round((theta0_deg - hw) / step))
    i_hi = int(round((theta0_deg + hw) / step))
    assert abs(i_lo * step - (theta0_deg - hw)) < 1e-9, "u-grid off lattice"
    assert abs(i_hi * step - (theta0_deg + hw)) < 1e-9, "u-grid off lattice"
    sc = scan_c_empty(g, lam_cells, i_lo, i_hi, step=step)
    o = i_lo - sc["i_lo"]
    n = i_hi - i_lo + 1
    c = sc[convention][o:o + n]
    u = np.arange(n) * step - hw
    return u, c


# =====================================================================
#  The crux quantity (frozen, NOTES.md Setup)
# =====================================================================
def node_spacing_deg(fwhm_deg, n=41):
    """h = 2 * half_width_factor * FWHM / (n - 1) -- the quadrature NODE
    lattice spacing, read off the committed `gaussian_angle_weights` window.
    2.5 deg at n=41, FWHM=20."""
    return 2.0 * HALF_WIDTH_FACTOR * fwhm_deg / (n - 1)


def alias_coeff(theta0_deg, fwhm_deg, lam_cells, g, convention, m=1, n=41,
                step=STEP_DEG):
    """The alias coefficient, exactly as frozen:

        alias_coeff(m) = int w(theta) c(theta) exp(-2 pi i m theta / h) dtheta
                         / int w(theta) dtheta

    with `w` the committed Gaussian angular weight (sigma = FWHM/2.3548, the
    `gaussian_angle_weights` convention) and `c` the committed single-angle
    Weber contrast for that convention, both on the dense grid spanning the
    same +-half_width_factor*FWHM support the quadrature itself spans.

    `theta` in the exponent is the offset from theta0, i.e. the quadrature
    node lattice is anchored at theta0 -- which it is: `gaussian_angle_weights`
    returns `linspace(theta0 - hw, theta0 + hw, n)` with n odd, so theta0 is
    itself a node and every node sits at an integer multiple of h from it.
    That anchoring is what makes Re[] meaningful rather than an arbitrary
    phase.

    Returns the complex coefficient; `|alias_coeff(m=1)|` is the angular
    spectral amplitude `|g_hat(1/h)|` P-ALIAS-5 scores."""
    h = node_spacing_deg(fwhm_deg, n)
    sigma = fwhm_deg / FWHM_TO_SIGMA
    u, c = c_window(theta0_deg, fwhm_deg, lam_cells, g, convention, step=step)
    w = np.exp(-0.5 * (u / sigma) ** 2)
    num = np.trapezoid(w * c * np.exp(-2j * np.pi * m * u / h), dx=step)
    den = np.trapezoid(w, dx=step)
    return num / den


def E_pred(theta0_deg, fwhm_deg, lam_cells, g, convention, n=41,
           step=STEP_DEG):
    """E_pred = 2 Re[alias_coeff(1)] + 2 Re[alias_coeff(2)]  (NOTES.md Setup).

    BOTH m=1 and m=2 are required -- m=1 alone is 6-16% off at 450nm
    (QUANTUM's E5, Red Team-confirmed). The predicted-unstable rule is the
    UNFITTED `|E_pred| >= ABS_TOL`; no fitted parameter appears anywhere in
    this function.

    Returns every piece the completeness ledger and P-ALIAS-5/6 need."""
    a1 = alias_coeff(theta0_deg, fwhm_deg, lam_cells, g, convention, m=1, n=n,
                     step=step)
    a2 = alias_coeff(theta0_deg, fwhm_deg, lam_cells, g, convention, m=2, n=n,
                     step=step)
    e1 = 2.0 * a1.real
    e2 = 2.0 * a2.real
    return dict(
        E_pred_m1=e1,                 # ledger quantity 1: the m=1 term alone
        E_pred_m2=e2,                 # ledger quantity 2: the m=2 term alone
        E_pred=e1 + e2,               # the crux quantity
        abs_ghat1=float(abs(a1)),     # |g_hat(1/h)| -- P-ALIAS-5
        abs_ghat2=float(abs(a2)),
        a1_real=float(a1.real), a1_imag=float(a1.imag),
        a2_real=float(a2.real), a2_imag=float(a2.imag),
        h_deg=node_spacing_deg(fwhm_deg, n),
    )


# =====================================================================
#  Descriptive diagnostic ONLY (NOTES.md idealization 5)
# =====================================================================
def geom_A(g):
    """A = OBJ_Y - ABSORB. There is no `g["A"]` key (Red Team docket 5)."""
    return g["OBJ_Y"] - g["ABSORB"]


def local_period_deg(theta_deg, lam_cells, g):
    """P(theta) = lambda / (A cos theta), in degrees -- via exp-048's own
    committed `ripple_period_deg`. USED ONLY DESCRIPTIVELY (NOTES.md
    idealization 5): normalizing by P was the Phase-1 design's error, and
    nothing in `alias_coeff`/`E_pred` above touches P."""
    return ripple_period_deg(geom_A(g), lam_cells, theta_deg)


def samples_per_period(theta0_deg, fwhm_deg, lam_cells, g, n=41):
    """P(theta0)/h -- the Nyquist diagnostic quoted in NOTES.md Hypothesis
    (0.59-1.03 samples/period at FWHM=20, i.e. 1.9-3.4x below Nyquist).
    Descriptive; never a crux quantity."""
    return local_period_deg(theta0_deg, lam_cells, g) / node_spacing_deg(fwhm_deg, n)


def main():
    print(f"exp-051 design geometry -- half_width_factor={HALF_WIDTH_FACTOR} "
          f"(read from committed gaussian_angle_weights)")
    for name, g in (("GEOM_EXP042_OLD", GEOM_EXP042_OLD), ("GEOM78", GEOM78)):
        print(f"  {name}: A = OBJ_Y-ABSORB = {geom_A(g)}")
    g = GEOM78
    print(f"  h(FWHM=20,n=41) = {node_spacing_deg(20, 41)} deg")
    for lam in (450, 600, 750):
        sp = samples_per_period(38, 20, CPL[lam], g, 41)
        print(f"  samples/period @38deg,FWHM=20,{lam}nm,GEOM78 = {sp:.3f} "
              f"(P={local_period_deg(38, CPL[lam], g):.4f} deg)")
    c = edge_diffraction_c_empty_g(38.0, CPL[600], GEOM_EXP042_OLD, "corrected")
    c042 = edge_diffraction_c_empty_corrected_042(38.0, CPL[600])
    print(f"  anchor spot: {c!r} vs committed exp-042 {c042!r} "
          f"(rel {abs(c - c042) / abs(c042):.3e})")


if __name__ == "__main__":
    main()
