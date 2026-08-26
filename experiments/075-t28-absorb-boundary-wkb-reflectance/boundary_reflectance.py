"""
experiments/075-t28-absorb-boundary-wkb-reflectance/boundary_reflectance.py
============================================================================
Panel Iteration 52 (exp-075). Lead: THERMODYNAMICS, by rotation. Executes
PLAN.md's Iteration-52 queue item 1 (PHOTONICS' originally-named WKB/
adiabatic boundary-reflectance model for the graded-loss `ABSORB` band;
queued twice, dropped without execution both times, Iterations 46/47; the
first candidate in this six-cycle T28 sub-thread to engage a seat's own
charter physics -- absorbed/reflected energy bookkeeping -- directly
rather than re-verify statistics on an existing fit).

ZERO new FDTD calls. `lab.fdtd2d.Sim` is imported ONLY to read `_damping`'s
own arrays programmatically (its `__init__` builds them with no `.run()`
steps -- no time-stepping happens anywhere in this file), per the context
packet's own recommendation and house rule R4 (no hand-typed numbers).

WHAT THIS FILE DOES, in four stages (see NOTES.md / phase1_proposal.md for
the physics narrative and idealizations):

  [1] Extract the -x edge `ABSORB` band's per-cell Ez damping multiplier
      straight from `Sim`, for ABSORB in {40,60,70,80}, and convert it to
      an effective per-cell complex refractive index n(x) -- STATING the
      idealizations that conversion rests on.
  [2] Compute the reflection coefficient r(theta; ABSORB) -- magnitude and
      phase -- of a wave normally incident from the domain interior on this
      graded lossy layer, backed by the PEC-like hard wall at x=0, via an
      EXACT (given [1]'s idealizations) recursive transmission-line
      impedance transform over the `ABSORB` discrete grid cells -- not a
      truncated single-pass WKB/Born integral, because the band is only
      ~2-5 wavelengths thick (checked explicitly, [2b]) and a first-order
      adiabatic approximation is not automatically trustworthy at that
      thickness. The leading-order WKB adiabaticity parameter is computed
      alongside as a diagnostic, not as the reflectance calculation itself.
  [3] Three zero-data sanity/passivity gates on the transfer-matrix code
      itself (lossless unimodularity, N=1 closed-form identity, passivity
      |r|<=1 for every physically-lossy case computed) -- must ALL pass
      before any r(theta;ABSORB) number is trusted.
  [4] Turn r(theta;ABSORB) into a predicted angle-dependent interference
      signature at the observation plane, via an image-source extension of
      exp-048's own already-committed, already-vetted Huygens-Fresnel
      desk propagator (`edge_diffraction_c_empty_corrected` /
      `field_and_h`) -- the real source's field, PLUS a second coherent
      contribution from the mirror image of the source through the x=0
      wall, weighted by r(theta;ABSORB). Compared against
      experiments/069's own already-collected `block_dense.rows` (31
      points, theta in [36,42] deg, 0.2deg step, 600nm) -- the real T28
      differential dataset -- via (a) a period fit using the SAME
      fixed-then-free sinusoid methodology exp-069's own `run.py` used to
      recover P*=2.8421 deg (imported, not reimplemented), and (b) a
      Pearson r^2 shape-match between the model's own predicted delta(theta)
      curve and the real one -- the stronger test PANEL.md's own mandate
      names as preferable to a bare period match.

Run: `python3 boundary_reflectance.py` from this directory (or anywhere --
paths are resolved from `__file__`). Writes `boundary_reflectance_results.
json` and prints the tables below to stdout; every number in
`phase1_proposal.md` is copied from that JSON/stdout, never hand-typed.
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

from lab.fdtd2d import Sim  # noqa: E402


def _load(path, name):
    """Load a module from an explicit path under a unique name -- the
    house pattern for `design_geometry.py`/`run.py` filename collisions
    across experiment directories (see experiments/065's own
    `_load_exp048`)."""
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


dg065 = _load(
    os.path.join(ROOT, "experiments", "065-t24-absorb-boundary-sweep", "design_geometry.py"),
    "_exp065_design_geometry",
)
dg048 = _load(
    os.path.join(ROOT, "experiments", "048-evidentiary-chord-closure", "design_geometry.py"),
    "_exp048_design_geometry",
)

CPL = {450: 15, 600: 20, 750: 25}
ABSORB_LIST = (40, 60, 70, 80)
COURANT_FRAC = dg065.COURANT_FRAC
S_COURANT = COURANT_FRAC / np.sqrt(2.0)          # cells/step, Sim.S
DT = S_COURANT                                    # time/step, c=1, dx=1 units

RESULTS_69_PATH = os.path.join(
    ROOT, "experiments", "069-t21-block-mini-period-match-power-up", "results.json")
RUN69_PATH = os.path.join(
    ROOT, "experiments", "069-t21-block-mini-period-match-power-up", "run.py")


# ============================================================ [1] n(x)
def damp_e_profile(absorb, buffer=200):
    """The pure -x-edge Ez damping multiplier, cell by cell, straight from
    `Sim.__init__` (zero `.run()` steps). Sampled at the y-center of a
    domain wide/tall enough that neither the +x edge nor the y edges
    contribute at any x we read (checked by assertion, not assumed) --
    isolates the -x edge's own cubic ramp exactly as `Sim._damping`
    builds it, with no hand-retyped formula.

    Returns an array of length `absorb`; index 0 = the cell touching the
    x=0 wall (heaviest damping), index absorb-1 = the cell bordering the
    undamped interior (lightest damping)."""
    nx = 2 * absorb + buffer
    ny = 4 * absorb + buffer
    sim = Sim(nx, ny, cells_per_lambda=20, courant_frac=COURANT_FRAC, absorb=absorb)
    yc = ny // 2
    assert sim.damp_e[absorb, yc] == 1.0, "interior contaminated by another edge"
    assert sim.damp_e[absorb - 1, yc] < 1.0, "band itself reads undamped -- bug"
    assert sim.damp_e[nx - absorb - 1, yc] == 1.0, "+x edge leaking into sample column"
    return sim.damp_e[:absorb, yc].copy()


def nu_profile(damp_col):
    """nu(x), 1/time (c=1 units), s.t. exp(-nu*DT) == damp_col exactly --
    the rate that reproduces the discrete per-step multiplicative kick as
    continuous exponential decay sampled once per timestep (Idealization
    1, phase1_proposal.md)."""
    return -np.log(damp_col) / DT


def n_profile_exact(nu, omega):
    """Effective complex index at NORMAL incidence, exact (not linearized
    in nu/omega) local dispersion of a matched (E- and H-friction equal)
    lossy medium: k(x)^2 = (omega^2 - nu(x)^2 - 2*i*omega*nu(x)) / c^2,
    c=1 here. n(x) = k(x)/k0.

    SIGN NOTE (Idealization 3, phase1_proposal.md Sec 2): the friction-PDE
    derivation dE/dt=c dH/dx-nu E, dH/dt=c dE/dx-nu H, solved for a single
    traveling wave E,H ~ exp(i(kx-omega t)), gives k^2 with a +2i*omega*nu
    cross term under one natural (but, it turns out, wrong-for-this-
    formula) convention pairing. That pairing is ADJUDICATED, not assumed,
    against an unambiguous physical requirement: a source-free, PEC-backed,
    lossy (nu>=0 everywhere) stack must have |r(theta)|<=1 for every angle
    and every thickness (energy conservation -- reflected power cannot
    exceed incident power with no gain anywhere). The -2i*omega*nu sign
    used here is the one that satisfies this for every (absorb, theta)
    pair tested (verified by `gate_passivity`, which HALTS the whole run
    via `assert` if it is ever violated); the +2i*omega*nu sign fails
    passivity by orders of magnitude even at tiny loss (see NOTES.md /
    phase1_proposal.md Sec 2 for the worked comparison) -- a time-
    convention mismatch (e^{-i*omega*t} vs the transfer-matrix algebra's
    implicit convention) manifests as exactly this kind of sign flip
    (complex conjugation of n(x)), and passivity is the physical
    tie-breaker used to resolve it, not an assumption."""
    val = (omega ** 2 - nu ** 2 - 2j * omega * nu)
    return np.sqrt(val.astype(complex)) / omega


def n_profile_linear(nu, omega):
    """The naive weak-loss linearization n(x) = 1 - i*nu(x)/omega, kept as
    an independent cross-check against `n_profile_exact` above. NOTE (a
    finding of this file, not an assumption): (1-i*x)^2 = 1-x^2-2ix
    IDENTICALLY for any x -- so this "linearization" is in fact the EXACT
    solution of `n_profile_exact`'s own quadratic for every nu/omega, not
    merely a small-nu/omega approximation. Sec [1b]'s zero deviation is
    this algebraic identity showing up numerically, not a coincidence of
    this bench's specific nu/omega range -- reported as Idealization 2 in
    phase1_proposal.md, corrected from an original small-loss framing."""
    return 1.0 - 1j * nu / omega


# ================================================== [2] transfer matrix
def reflection_coefficient(n_prof, theta_deg, lam_cells):
    """Complex reflection coefficient at the OUTER (interior-facing) face
    of the graded stack, wave incident from vacuum (n=1) at angle
    theta_deg from the x-normal, stack backed by a PEC short circuit
    (Ez=0, exact per `Sim.run`'s own E-update never touching index 0/-1)
    at its innermost layer. Exact recursive transmission-line impedance
    transform over the discrete per-cell profile -- one homogeneous
    layer per grid cell, thickness = 1 cell = dx, TE (s-pol, matches this
    bench's scalar Ez field) admittance formula for a matched (eps=mu)
    medium: Z(x) = n(x) / sqrt(n(x)^2 - sin^2(theta)), free-space Z=1
    normalization (eta0=1)."""
    theta = math.radians(theta_deg)
    s2 = math.sin(theta) ** 2
    k0 = 2.0 * math.pi / lam_cells
    kx = k0 * np.sqrt(n_prof.astype(complex) ** 2 - s2)
    Z = n_prof / np.sqrt(n_prof.astype(complex) ** 2 - s2)
    Zin = 0.0 + 0.0j  # PEC short circuit, innermost boundary condition
    for i in range(n_prof.size):
        Zi = Z[i]
        t = np.tan(kx[i] * 1.0)  # thickness 1 cell
        Zin = Zi * (Zin + 1j * Zi * t) / (Zi + 1j * Zin * t)
    Zvac = 1.0 / math.cos(theta)
    return (Zin - Zvac) / (Zin + Zvac)


def wkb_adiabaticity(n_prof, theta_deg, lam_cells):
    """Standard WKB validity parameter Q(x) = |d(1/kx)/dx|, cell-to-cell
    finite difference on the SAME kx(x) this file's own transfer matrix
    uses -- Q << 1 is required for a leading-order (single-pass Born)
    WKB reflection integral to be trustworthy. Returns (Q array, max Q)."""
    theta = math.radians(theta_deg)
    s2 = math.sin(theta) ** 2
    k0 = 2.0 * math.pi / lam_cells
    kx = k0 * np.sqrt(n_prof.astype(complex) ** 2 - s2)
    inv_kx = 1.0 / kx
    dQ = np.abs(np.diff(inv_kx))  # per-cell step, dx=1
    return dQ, float(np.max(np.abs(dQ))) if dQ.size else 0.0


# ============================================================ [3] gates
def gate_lossless_unimodular(n_trials=6, seed=0):
    """A lossless (real n(x), arbitrary profile) stack backed by a PEC
    short circuit must reflect with |r|=1 EXACTLY, for any real theta --
    a hand-independent algebraic identity of the transfer-matrix formula
    (|i*x-1| == |i*x+1| for real x), not something the physics of loss
    can be blamed for if it fails. Random real profiles + random angles."""
    rng = np.random.default_rng(seed)
    worst = 0.0
    checks = []
    for _ in range(n_trials):
        length = int(rng.integers(5, 60))
        n_prof = 1.0 + 0.6 * rng.random(length)  # random real index profile
        theta_deg = float(rng.uniform(-44.0, 44.0))
        r = reflection_coefficient(n_prof.astype(complex), theta_deg, 20.0)
        dev = abs(abs(r) - 1.0)
        worst = max(worst, dev)
        checks.append(dict(length=length, theta_deg=theta_deg, abs_r=abs(r), dev=dev))
    return dict(worst_dev=worst, pass_=worst < 1e-9, checks=checks)


def gate_single_layer_identity(n_trials=8, seed=1):
    """N=1 layer: the general recursive loop's FIRST iteration must equal
    the textbook short-circuited single-layer formula
    Zin = i*Z1*tan(kx1*t) computed directly, outside the loop -- catches
    an indexing/initialization bug independent of the loop itself."""
    rng = np.random.default_rng(seed)
    worst = 0.0
    for _ in range(n_trials):
        n1 = complex(rng.uniform(0.5, 2.0), rng.uniform(0.0, 1.5))
        theta_deg = float(rng.uniform(-44.0, 44.0))
        lam = float(rng.uniform(10.0, 30.0))
        theta = math.radians(theta_deg)
        s2 = math.sin(theta) ** 2
        k0 = 2.0 * math.pi / lam
        kx1 = k0 * np.sqrt(n1 ** 2 - s2)
        Z1 = n1 / np.sqrt(n1 ** 2 - s2)
        Zin_direct = 1j * Z1 * np.tan(kx1 * 1.0)
        Zvac = 1.0 / math.cos(theta)
        r_direct = (Zin_direct - Zvac) / (Zin_direct + Zvac)
        r_loop = reflection_coefficient(np.array([n1]), theta_deg, lam)
        worst = max(worst, abs(r_direct - r_loop))
    return dict(worst_dev=worst, pass_=worst < 1e-12)


def gate_passivity(all_r):
    """Every physically-lossy (nu>0 somewhere) computed r(theta;ABSORB)
    must satisfy |r|<=1 -- a passive, PEC-backed lossy stack cannot
    amplify. `all_r` is the flat dict {(absorb,theta): complex r}."""
    worst = max(abs(v) for v in all_r.values())
    return dict(worst_abs_r=worst, pass_=worst <= 1.0 + 1e-9)


# ================================================ [4] interference model
def image_geometry(g):
    """Mirror-image source through the x=0 wall: same y-positions, same
    taper, D_SP replaced by the physical image-to-plane distance
    PLANE_X + SRC_X (the source's mirror sits at x = -SRC_X; distance
    from there to the plane at x=PLANE_X is PLANE_X - (-SRC_X))."""
    gi = dict(g)
    gi["D_SP"] = g["PLANE_X"] + g["SRC_X"]
    return gi


def c_empty_boundary_free(theta_deg, lam_cells, g):
    return dg048.edge_diffraction_c_empty_corrected(theta_deg, lam_cells, g)


def c_empty_with_wall(theta_deg, lam_cells, g, r_coeff):
    """Direct source field PLUS the image source's field, coherently
    summed, weighted by the complex reflection coefficient -- both terms
    computed by exp-048's own already-committed Huygens-Fresnel
    propagator, not reimplemented."""
    from lab import ambient as amb

    E_d, H_d, gd = dg048.field_and_h(theta_deg, lam_cells, g)
    gi = image_geometry(g)
    E_i, H_i, gdi = dg048.field_and_h(theta_deg, lam_cells, gi)
    assert np.array_equal(gd["y_obs"], gdi["y_obs"]), "image/direct y-grids disagree"
    E = E_d + r_coeff * E_i
    H = H_d + r_coeff * H_i
    Sx = -np.real(E * np.conj(H))
    bo, bf = amb.window_means(Sx, gd["y_lo"], gd["obj_y"], g["R_OUT"], g["GUARD_OUT"], g["W_FLANK"])
    return amb.weber(bo, bf)


# =============================================================== driver
def main():
    out = {}

    print("=" * 78)
    print("exp-075 -- WKB/adiabatic boundary-reflectance model, ABSORB band")
    print("=" * 78)

    # ---- [1]/[2]/[3] reflectance ----
    print("\n[1] n(x) PROFILES + BAND THICKNESS IN WAVELENGTHS (600nm, cpl=20)")
    thickness_lambda = {}
    max_nu_over_omega = {}
    n_profiles_exact = {}
    n_profiles_linear = {}
    omega600 = 2.0 * math.pi / CPL[600]
    for absorb in ABSORB_LIST:
        damp = damp_e_profile(absorb)
        nu = nu_profile(damp)
        n_exact = n_profile_exact(nu, omega600)
        n_lin = n_profile_linear(nu, omega600)
        n_profiles_exact[absorb] = n_exact
        n_profiles_linear[absorb] = n_lin
        thickness_lambda[absorb] = absorb / CPL[600]
        max_nu_over_omega[absorb] = float(np.max(nu / omega600))
        print(f"    ABSORB={absorb:3d}  thickness={thickness_lambda[absorb]:.2f} lambda  "
              f"max(nu/omega)={max_nu_over_omega[absorb]:.4f}  "
              f"n(x=0)={n_exact[0]:.4f}  n(x=absorb-1)={n_exact[-1]:.6f}")
    out["thickness_lambda_600nm"] = thickness_lambda
    out["max_nu_over_omega_600nm"] = max_nu_over_omega

    print("\n[1b] EXACT vs LINEARIZED n(x): max relative |n_exact-n_lin| per config")
    lin_vs_exact = {}
    for absorb in ABSORB_LIST:
        rel = np.abs(n_profiles_exact[absorb] - n_profiles_linear[absorb]) / np.abs(n_profiles_exact[absorb])
        lin_vs_exact[absorb] = float(np.max(rel))
        print(f"    ABSORB={absorb:3d}  max relative deviation = {lin_vs_exact[absorb]:.4f}")
    out["linear_vs_exact_n_max_rel_dev"] = lin_vs_exact

    print("\n[2] SANITY / PASSIVITY GATES (must ALL pass before any r(theta) is trusted)")
    g_lossless = gate_lossless_unimodular()
    g_single = gate_single_layer_identity()
    print(f"    G-LOSSLESS  worst ||r|-1| over {len(g_lossless['checks'])} random real "
          f"profiles/angles = {g_lossless['worst_dev']:.3e}  PASS={g_lossless['pass_']}")
    print(f"    G-N1        worst |r_loop - r_direct| over 8 random single layers "
          f"= {g_single['worst_dev']:.3e}  PASS={g_single['pass_']}")
    assert g_lossless["pass_"], "G-LOSSLESS FAILED -- transfer matrix code has a bug"
    assert g_single["pass_"], "G-N1 FAILED -- transfer matrix code has a bug"
    out["gate_lossless_unimodular"] = g_lossless
    out["gate_single_layer_identity"] = g_single

    print("\n[3] WKB ADIABATICITY DIAGNOSTIC (theta=39deg, 600nm) -- NOT the")
    print("    reflectance calculation itself (that is the exact transfer matrix");
    print("    above); this quantifies how badly a single-pass WKB/Born integral")
    print("    would have been stressed had it been used instead.")
    wkb_diag = {}
    for absorb in ABSORB_LIST:
        _, qmax = wkb_adiabaticity(n_profiles_exact[absorb], 39.0, CPL[600])
        wkb_diag[absorb] = qmax
        flag = "SLOWLY VARYING" if qmax < 0.1 else ("MARGINAL" if qmax < 1.0 else "NOT SLOWLY VARYING")
        print(f"    ABSORB={absorb:3d}  max|d(1/kx)/dx| = {qmax:.4f}   [{flag}]")
    out["wkb_adiabaticity_qmax_theta39_600nm"] = wkb_diag

    # ---- reflectance sweep over the real dense-sweep angle grid ----
    with open(RESULTS_69_PATH) as f:
        res69 = json.load(f)
    dense_rows = res69["block_dense"]["rows"]
    thetas = np.array([r["theta"] for r in dense_rows])
    real_delta = np.array([r["delta"] for r in dense_rows])
    real_c40 = np.array([r["C_empty_C40"] for r in dense_rows])
    real_c80 = np.array([r["C_empty_C80"] for r in dense_rows])

    print(f"\n[4] r(theta;ABSORB) SWEEP over the real dense grid "
          f"({len(thetas)} angles, {thetas.min()}-{thetas.max()}deg, 600nm)")
    r_table = {}
    all_r_flat = {}
    for absorb in ABSORB_LIST:
        n_exact = n_profiles_exact[absorb]
        rs = np.array([reflection_coefficient(n_exact, float(t), CPL[600]) for t in thetas])
        r_table[absorb] = rs
        for t, rv in zip(thetas, rs):
            all_r_flat[(absorb, float(t))] = rv
    g_pass = gate_passivity(all_r_flat)
    print(f"    G-PASSIVITY worst |r| over {len(all_r_flat)} (ABSORB,theta) pairs "
          f"= {g_pass['worst_abs_r']:.6f}  PASS={g_pass['pass_']}")
    assert g_pass["pass_"], "G-PASSIVITY FAILED -- |r|>1 somewhere, a bug or a branch error"
    out["gate_passivity"] = g_pass

    for absorb in (40, 80):
        rs = r_table[absorb]
        i0, imid, i1 = 0, len(thetas) // 2, len(thetas) - 1
        print(f"    ABSORB={absorb:3d}  theta={thetas[i0]:.1f}: |r|={abs(rs[i0]):.4f} "
              f"arg={math.degrees(np.angle(rs[i0])):+7.2f}deg   "
              f"theta={thetas[imid]:.1f}: |r|={abs(rs[imid]):.4f} "
              f"arg={math.degrees(np.angle(rs[imid])):+7.2f}deg   "
              f"theta={thetas[i1]:.1f}: |r|={abs(rs[i1]):.4f} "
              f"arg={math.degrees(np.angle(rs[i1])):+7.2f}deg")

    # ---- [4] predicted interference signature ----
    print("\n[5] PREDICTED DELTA(theta) = C_with_wall(ABSORB=80) - C_with_wall(ABSORB=40)")
    print("    via exp-048's Huygens-Fresnel propagator + a mirror-image source")
    print("    weighted by r(theta;ABSORB), 600nm, on the real dense grid.")
    c_wall = {absorb: [] for absorb in ABSORB_LIST}
    c_bfree = {absorb: [] for absorb in ABSORB_LIST}
    for absorb in ABSORB_LIST:
        cfg_key = f"C{absorb}"
        g = dg065.propagator_geom(dg065.CONFIGS[cfg_key])
        n_exact = n_profiles_exact[absorb]
        for t in thetas:
            r = reflection_coefficient(n_exact, float(t), CPL[600])
            c_wall[absorb].append(c_empty_with_wall(float(t), CPL[600], g, r))
            c_bfree[absorb].append(c_empty_boundary_free(float(t), CPL[600], g))
        c_wall[absorb] = np.array(c_wall[absorb])
        c_bfree[absorb] = np.array(c_bfree[absorb])

    # internal consistency: boundary-free term must be config-independent
    # (already established, exp-065 Sec [2]) -- re-verify in THIS run.
    bfree_spread = max(
        float(np.max(np.abs(c_bfree[a] - c_bfree[40]))) for a in ABSORB_LIST[1:]
    )
    print(f"    internal check: max|C_boundary_free(ABSORB)-C_boundary_free(40)| "
          f"over all configs/angles = {bfree_spread:.3e}  (expect ~0, exp-065 Sec 2)")
    out["boundary_free_spread_internal_check"] = bfree_spread

    pred_delta_wall = c_wall[80] - c_wall[40]
    pred_delta_direct = (c_wall[80] - c_bfree[80]) - (c_wall[40] - c_bfree[40])
    cross_check = float(np.max(np.abs(pred_delta_wall - pred_delta_direct)))
    print(f"    internal check: two equivalent ways of computing predicted delta "
          f"agree to {cross_check:.3e}")
    out["predicted_delta_equivalence_check"] = cross_check

    print(f"    predicted delta(theta): min={pred_delta_wall.min():.6e}  "
          f"max={pred_delta_wall.max():.6e}  "
          f"ptp={np.ptp(pred_delta_wall):.6e}")
    print(f"    REAL delta(theta) (exp-069 block_dense):    min={real_delta.min():.6e}  "
          f"max={real_delta.max():.6e}  ptp={np.ptp(real_delta):.6e}")
    out["predicted_delta"] = pred_delta_wall.tolist()
    out["real_delta"] = real_delta.tolist()
    out["thetas"] = thetas.tolist()

    # ---- period fits, reusing exp-069's own established methodology ----
    run69 = _load(RUN69_PATH, "_exp069_run")
    fixed_fit = run69._fixed_period_fit
    free_search = run69._free_period_search

    x_sin = np.sin(np.radians(thetas))
    # exp-069's OWN default arguments (lo_deg=1, hi_deg=4, n_grid=400) --
    # reused verbatim so this reproduces the established P*=2.8421deg
    # citation exactly, not an independently-gridded near-miss.
    real_free = free_search(thetas, real_delta, center_deg=39.0)
    pred_free = free_search(thetas, pred_delta_wall, center_deg=39.0, lo_deg=1.0, hi_deg=15.0, n_grid=2800)
    print(f"\n[6] FREE-PERIOD FIT (exp-069's own methodology, imported not reimplemented)")
    print(f"    REAL data      P*={real_free['p_star_deg']:.4f}deg  R^2={real_free['r_squared']:.4f} "
          f"(established citation: P*=2.8421deg, R^2=0.6272)")
    print(f"    MODEL predicted P*={pred_free['p_star_deg']:.4f}deg  R^2={pred_free['r_squared']:.4f}")
    out["real_free_period_fit"] = real_free
    out["model_free_period_fit"] = pred_free

    # Widened-range search: does the model's own free period actually
    # converge to an interior optimum anywhere near the closed-form Sec[8]
    # estimate, or does it run to the search boundary (meaning the model's
    # curve does not complete even one oscillation across the 6deg window,
    # so no well-constrained period exists here at all)?
    pred_free_wide = free_search(thetas, pred_delta_wall, center_deg=39.0,
                                  lo_deg=1.0, hi_deg=60.0, n_grid=6000)
    at_boundary = pred_free_wide["p_star_deg"] >= 59.9
    print(f"    MODEL predicted, WIDENED search (1-60deg): "
          f"P*={pred_free_wide['p_star_deg']:.4f}deg  R^2={pred_free_wide['r_squared']:.4f}"
          f"{'  [RUNS TO SEARCH BOUNDARY -- not a well-constrained period within this window]' if at_boundary else ''}")
    out["model_free_period_fit_widened"] = pred_free_wide
    out["model_period_runs_to_boundary"] = bool(at_boundary)

    rel_period_dev = abs(pred_free["p_star_deg"] - real_free["p_star_deg"]) / real_free["p_star_deg"]
    print(f"    relative period deviation |P_model - P*_real| / P*_real = {rel_period_dev:.4f}")
    out["relative_period_deviation"] = rel_period_dev

    # ---- shape match (Pearson r^2), the stronger test PANEL.md invites ----
    corr = np.corrcoef(pred_delta_wall, real_delta)[0, 1]
    shape_r2 = float(corr ** 2)
    print(f"\n[7] SHAPE MATCH: Pearson r^2(model predicted delta, real delta) = {shape_r2:.4f} "
          f"(sign of correlation = {'+' if corr > 0 else '-'})")
    out["shape_pearson_r"] = float(corr)
    out["shape_r_squared"] = shape_r2

    # ---- closed-form analytic period, cross-check on the numeric fit ----
    print("\n[8] CLOSED-FORM ROUND-TRIP PERIOD (cross-check on the numeric fit, Sec 2")
    print("    of phase1_proposal.md): P_wall(theta;ABSORB) = (180/pi)*lambda /")
    print("    (2*PLANE_X(ABSORB)*sin(theta)), zero-order in r(theta)'s own phase.")
    p_wall_closed = {}
    for absorb in ABSORB_LIST:
        plane_x = dg065.CONFIGS[f"C{absorb}"]["plane_x"]
        p = math.degrees(CPL[600] / (2.0 * plane_x * math.sin(math.radians(39.0))))
        p_wall_closed[absorb] = dict(plane_x=plane_x, period_deg=p)
        print(f"    ABSORB={absorb:3d}  plane_x={plane_x:4d}  P_wall(39deg)={p:.3f}deg")
    out["closed_form_period_at_39deg"] = p_wall_closed

    # ---- pre-registered bands, scored here in code (not by eye) ----
    print("\n[9] PRE-REGISTERED FALSIFIABLE BANDS -- scored")
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

    out_path = os.path.join(HERE, "boundary_reflectance_results.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2, default=_json_default)
    print(f"\nwrote {out_path}")
    return out


if __name__ == "__main__":
    main()
