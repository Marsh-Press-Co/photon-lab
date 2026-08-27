"""
experiments/078-t28-y-wall-echo-prescreen/y_wall_prescreen.py
============================================================================
Panel Iteration 55 (exp-078). Lead: PHOTONICS, by rotation. Executes
PLAN.md's Iteration-55 queue Tier 0 item 2 (PHOTONICS #1, EM #1,
independently convergent, Iteration 54's own Phase-5 final audit): a
CLOSED-FORM period PRE-SCREEN (ZERO new FDTD) of a coherent echo off a wall
whose NORMAL is TRANSVERSE (the +y/-y walls) to the beam's principal
(x) propagation axis -- the untested candidate PHOTONICS and
ELECTROMAGNETISM independently converged on at exp-077 Phase 5, after the
x-normal (-x/+x wall) echo class was REFUTEd twice over (single-wall,
exp-075; two-wall, exp-077) without ever checking the parameter (PAD's
`clear_span_y`: 0/40/0 across C40/G40/C80) that actually tracks T28's own
dominant PAIR_PAD signal.

ZERO new FDTD calls anywhere in this file. Every reusable piece of
machinery is IMPORTED from already-committed, already-vetted files, per
house rule R4 and this sub-thread's own established `_load()` convention
(boundary_reflectance.py / two_wall_cavity.py / pad_round_trip_model.py):

  - `experiments/065-.../design_geometry.py` (`dg065`): `CONFIGS`
    (`C40`/`C60`/`C70`/`C80`/`G40`), each config's own `obj_y`, `y_lo`,
    `A`, `d_sp`, `plane_x`, `absorb`, `clear_span_y`.
  - `experiments/075-.../boundary_reflectance.py` (`br`): `damp_e_profile`,
    `nu_profile`, `n_profile_exact`, `reflection_coefficient`, the three
    sanity/passivity gates, `CPL`. The y-direction `ABSORB` band is BUILT
    BY THE IDENTICAL FORMULA as the x-direction band (`Sim._damping`,
    `lab/fdtd2d.py:122-129` -- one shared cubic ramp applied to all four
    edges), verified in code below (Sec [0]) before it is reused -- so
    `r(theta;ABSORB)`, already built, gated (G-LOSSLESS/G-N1/G-PASSIVITY)
    and Red-Team-adjudicated on convention (R8, Iteration 52) for the
    x-wall, applies UNCHANGED to a y-wall of the same `ABSORB` depth. No
    new reflectance model is built or needed here.
  - `experiments/069-.../run.py` (`run69`): `_free_period_search`,
    `_fixed_period_fit` -- this entire T28 sub-thread's own period-fitting
    methodology since Iteration 46, imported verbatim, never reimplemented.
  - `experiments/076-.../results.json::headline`: the REAL, already-
    collected `C40`/`G40`/`C80` dense 31-point/600nm/settled-STEPS=2800
    sweep -- read, never hand-typed (R4). `experiments/077-.../
    pad_round_trip_results.json`: the already-established real free-period
    citations this pre-screen compares against (`P*=4.6113`/`4.1761`/
    `3.8271` deg), reproduced here by re-running the SAME imported
    `_free_period_search` on the SAME real data, not copied from prose.

WHAT THIS FILE DOES -- see `phase1_proposal.md` Sec 2-3 for the full
derivation narrative; summary:

  [0] Verify, in code, that the y-direction ABSORB band is built by the
      IDENTICAL formula as the x-direction band `boundary_reflectance.py`
      already models -- the load-bearing premise for reusing `r(theta)`
      unchanged.
  [1] PRIMARY derivation: an edge-image (self-echo) two-point model. T21's
      OWN established mechanism is edge diffraction from the source
      aperture's two taper edges (points, not the whole aperture) --
      offset +-A from OBJ_Y, at y_lo/y_hi. This file mirrors ONE such edge
      (the near-wall one, y_lo) through its own nearby y-wall, weighted by
      r(theta;ABSORB) (identical function, y-band), and derives the phase
      difference between the real edge and its own wall-image at the
      observation point -- a closed-form Euclidean two-point
      Huygens-Fresnel phase difference, NOT the T21-style plane-wave/ray
      reduction (shown analytically, Sec [1a], not to apply here: mirroring
      the driven phase RAMP in y, unlike mirroring the WHOLE APERTURE in x,
      does not preserve a well-defined "reflected ray", so the two-ray
      shortcut that reproduces T21's own formula (Sec [1a] validation) does
      NOT transfer to the y-wall case without justification -- justified
      instead via a stationary-phase argument that the full aperture image
      sum is edge-dominated, same idealization T21's own model already
      makes for the real (non-mirrored) sum).
  [1a] VALIDATION: re-derive the established x-wall closed form
      (`boundary_reflectance.py` Sec[8], `P=lambda/(2*PLANE_X*sin(theta))`)
      from the same two-plane-wave mirror-image argument, from scratch,
      and confirm it reproduces the committed formula bit-for-bit -- the
      check that the general method is sound BEFORE applying it somewhere
      new, and that a naive x<->y coordinate swap is NOT how the y case
      naturally comes out (documented in [1b]).
  [2] SECONDARY, explicitly NAIVE candidates: a bare coordinate-swap of the
      x-wall closed form (P_y(theta) = lambda/(2*Y_STANDOFF*cos(theta)) for
      two candidate Y_STANDOFF values (OBJ_Y; y_lo) -- reported ONLY as a
      look-elsewhere-flagged cross-check (R5's own standing rule: multiple
      candidate length scales tried against multiple targets is a search,
      not a derivation), never as the primary claim.
  [3] Evaluate [1]'s primary model's own period (does it even have one, via
      the SAME staged free-period-search widening idiom
      `pad_round_trip_model.py` uses) and [2]'s naive candidates, against
      the real, already-established T28 periods (2.8421 / 4.6113 / 4.1761
      / 3.8271 deg -- each re-derived here from committed data via the
      SAME imported function, not hand-typed).
  [4] Score against the SAME pre-registered period band exp-075/077 use
      (rel_dev <= 0.30 SUPPORT / > 1.00 REFUTE) -- period-only, since this
      pre-screen builds no full coherent field model and so has no Test-B
      shape curve to score (disclosed, not silently dropped).

Run: `python3 y_wall_prescreen.py` from this directory (or anywhere --
paths resolve from `__file__`). Writes `y_wall_prescreen_results.json` and
prints every table below; every number in `phase1_proposal.md` is copied
from that JSON/stdout, never hand-typed (R4).

PHASE-3 UPDATE (Panel Iteration 55, post Phase-2 Red Team mandatory-fix
docket, `phase2_redteam_audit.md`): the as-originally-filed Phase-1 version
of this file fed `reflection_coefficient` the raw sweep `theta_deg`
unconverted for the y-wall call -- WRONG, since that function's own angle
convention is "from the interface's own normal" and the y-wall's normal is
NOT the x-wall's. Three independent blind critics (MATERIALS, ELECTROMAGNETISM,
THERMODYNAMICS) and Red Team's own from-scratch re-derivation all
independently converged: the correct angle is `90-theta_deg`
(`y_wall_incidence_angle`, added below). This is now the file's PRIMARY,
pre-registered computation (`use_corrected_angle=True`, the default
everywhere); the as-originally-filed numbers are retained ONLY as an
explicitly labeled audit-trail comparison (Sec [5b]), never as this file's
own claim. Folding in this fix flips BOTH of the as-filed document's
nominal SUPPORT verdicts to INCONCLUSIVE (`C80-C40` additionally loses its
own resolvable interior-optimum period entirely) -- see `phase3_synthesis.md`
for the full accounting and `phase2_redteam_audit.md` for the audit that
caught it.
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
    """House `_load()` pattern (boundary_reflectance.py / two_wall_cavity.py
    / pad_round_trip_model.py's own convention) for filename collisions
    across experiment directories (`design_geometry.py`, `run.py` are
    reused names throughout this program)."""
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


EXP065_DIR = os.path.join(ROOT, "experiments", "065-t24-absorb-boundary-sweep")
EXP075_DIR = os.path.join(ROOT, "experiments", "075-t28-absorb-boundary-wkb-reflectance")
EXP076_RESULTS = os.path.join(ROOT, "experiments", "076-t28-g40-pad-decorrelation", "results.json")
EXP077_RESULTS = os.path.join(ROOT, "experiments", "077-t28-pad-round-trip-echo-model",
                               "pad_round_trip_results.json")

dg065 = _load(os.path.join(EXP065_DIR, "design_geometry.py"), "_exp078_dg065")
br = _load(os.path.join(EXP075_DIR, "boundary_reflectance.py"), "_exp078_boundary_reflectance")
CPL = br.CPL

run69 = _load(br.RUN69_PATH, "_exp078_run69")
_fixed_period_fit = run69._fixed_period_fit
_free_period_search = run69._free_period_search

CONGRUENT_KEYS = ("C40", "C60", "C70", "C80", "G40")


# ============================================================ [0] premise
def verify_shared_damping_formula(absorb=40, buffer=200):
    """The load-bearing premise for reusing `r(theta;ABSORB)` (built and
    gated for the -x edge in boundary_reflectance.py) UNCHANGED for a
    y-edge: `Sim._damping` (lab/fdtd2d.py:122-129) applies the SAME cubic
    ramp array to all four domain edges (x_lo, x_hi, y_lo, y_hi) via
    `np.maximum` on the SAME `ramp` -- verified here by direct comparison
    of a y-edge damp_e column against `boundary_reflectance.py`'s own
    x-edge column, same `absorb`, same `Sim` instance (not a separate
    claim -- one object, two edges read off it)."""
    from lab.fdtd2d import Sim as _Sim
    nx = 4 * absorb + buffer
    ny = 4 * absorb + buffer
    sim = _Sim(nx, ny, cells_per_lambda=20, courant_frac=br.COURANT_FRAC, absorb=absorb)
    x_edge_col = sim.damp_e[:absorb, ny // 2]
    y_edge_col = sim.damp_e[nx // 2, :absorb]
    worst = float(np.max(np.abs(x_edge_col - y_edge_col)))
    return dict(worst_abs_diff=worst, identical=worst == 0.0,
                x_edge_sample=x_edge_col[:5].tolist(), y_edge_sample=y_edge_col[:5].tolist())


# ================================================== [1a] x-wall validation
def x_wall_closed_form_rederivation(theta_deg, lam_cells, plane_x):
    """Re-derive `boundary_reflectance.py` Sec[8]'s own established x-wall
    closed form from scratch, via the two-plane-wave mirror-image argument
    (direct wave direction (-cos(theta),+sin(theta)) per
    `Sim.add_line_source`'s own docstring; the x=0-wall image flips k_x,
    preserves k_y -> direction (+cos(theta),+sin(theta))). Evaluated at the
    observation point (PLANE_X, OBJ_Y=yc): the SRC_X dependence cancels
    identically (image position (-SRC_X,yc) and direct position (SRC_X,yc)
    both project through the SAME arrival point), leaving
    Delta_phi(theta) = 2*k*PLANE_X*cos(theta) -- independent re-derivation,
    not copied. Returns the same period formula
    P(theta) = (180/pi)*lambda / (2*PLANE_X*sin(theta))."""
    k = 2.0 * math.pi / lam_cells
    theta = math.radians(theta_deg)
    # symbolic slope check: d(delta_phi)/d(theta) = -2*k*PLANE_X*sin(theta)
    dphi_dtheta = -2.0 * k * plane_x * math.sin(theta)
    period_rad = 2.0 * math.pi / abs(dphi_dtheta)
    period_deg = math.degrees(period_rad)
    return period_deg


# ====================================== [1b] why a naive x<->y swap fails
# Documented in code (not just prose): mirroring the driven phase ramp
# phase(y_s) = k*sin(theta)*(y_s - yc) THROUGH A WALL AT y=0 maps a source
# point at y_s (phase phase(y_s)) to an IMAGE point at y=-y_s -- but the
# image's OWN driven phase (a property of the physical current being
# reflected, unchanged by the mirror, up to r(theta)'s own phase) is STILL
# phase(y_s), NOT phase(-y_s) = -phase(y_s). This is the disanalogy with
# the x-wall: there, mirroring in x leaves phase(y_s) untouched (phase is a
# function of y only), so the whole aperture's image is coherently
# "steerable" exactly like the real one, and the two-ray/plane-wave
# reduction in [1a] applies cleanly. Mirroring in y touches the SAME
# coordinate the phase ramp depends on, breaking that reduction. See
# phase1_proposal.md Sec 3 for the full worked argument.


# ============================================ [1] primary: edge-image model
def y_wall_incidence_angle(theta_deg):
    """MANDATORY FIX (Phase 2 Red Team audit, phase2_redteam_audit.md
    Attack 1 -- independently converged on by MATERIALS, ELECTROMAGNETISM,
    THERMODYNAMICS, then re-derived a fourth way and confirmed by Red
    Team's own phase2_redteam_angle_correction_check.py). `boundary_
    reflectance.py::reflection_coefficient`'s own docstring states
    `theta_deg` is the angle measured FROM THE INTERFACE'S OWN NORMAL
    (it enters only as `sin(theta_deg)**2`, the standard oblique-incidence
    tangential-wavevector fraction). For the x-wall, whose normal is x-hat,
    the angle from that normal equals the sweep theta itself (direct-wave
    direction (-cos(theta),+sin(theta)) per `Sim.add_line_source`'s own
    docstring => cos(alpha_x)=cos(theta) => alpha_x=theta) -- so the x-wall
    model's original theta-in/theta-out usage was always correct. For the
    y-wall, whose normal is y-hat, the SAME direction vector gives
    cos(alpha_y)=sin(theta) => alpha_y=90-theta, NOT theta. This function
    performs that conversion; every call into `br.reflection_coefficient`
    in this file for the y-wall model MUST route through it."""
    return 90.0 - theta_deg


def edge_image_phase_difference(theta_deg, lam_cells, cfg, absorb_for_r, use_corrected_angle=True):
    """Delta_phi_self(theta; cfg) = arg(r(theta;absorb_for_r))
       + k*[hypot(D_SP, OBJ_Y+y_lo) - hypot(D_SP, A)]
    -- the near edge (y_lo) vs its OWN image through the near (y=0) y-wall,
    weighted by r(theta;ABSORB) (Sec[0]'s justified reuse). The driven
    phase term k*sin(theta)*A is IDENTICAL on the real edge and its own
    image (an image source preserves the reflected current's own temporal
    phase -- it does not re-derive a new "steered" phase from its mirrored
    position) and cancels exactly in the difference; only r(theta)'s own
    phase and a FIXED (theta-independent) propagation-distance offset
    survive. `use_corrected_angle` (default True, the PRIMARY/pre-registered
    computation per the Phase-2 Red Team mandatory-fix docket, item 1)
    routes `reflection_coefficient` through `y_wall_incidence_angle`
    (90-theta); `use_corrected_angle=False` reproduces the AS-ORIGINALLY-
    (INCORRECTLY)-FILED Phase-1 computation (raw, unconverted theta),
    retained ONLY as an explicitly labeled audit-trail comparison row per
    the docket's item 2 -- never as this file's own headline. Returns
    (delta_phi_rad, dist_real, dist_image, fixed_offset_cells)."""
    k = 2.0 * math.pi / lam_cells
    n_prof = br.n_profile_exact(br.nu_profile(br.damp_e_profile(absorb_for_r)),
                                 2.0 * math.pi / CPL[600])
    r_angle = y_wall_incidence_angle(theta_deg) if use_corrected_angle else theta_deg
    r = br.reflection_coefficient(n_prof, r_angle, lam_cells)
    d_sp = cfg["d_sp"]
    a = cfg["A"]
    y_lo = cfg["y_lo"]
    obj_y = cfg["obj_y"]
    dist_real = float(np.hypot(d_sp, a))
    dist_image = float(np.hypot(d_sp, obj_y + y_lo))
    fixed_offset = dist_image - dist_real
    delta_phi = float(np.angle(r)) + k * fixed_offset
    return dict(delta_phi_rad=delta_phi, arg_r_rad=float(np.angle(r)), abs_r=float(abs(r)),
                dist_real_cells=dist_real, dist_image_cells=dist_image,
                fixed_offset_cells=fixed_offset)


def edge_image_curve(thetas, lam_cells, cfg, absorb_for_r, use_corrected_angle=True):
    """Delta_phi_self(theta) over the real angle grid, plus a proxy
    oscillation curve cos(Delta_phi_self(theta)) (unweighted by |r| or
    aperture taper -- Idealization, phase1_proposal.md -- this pre-screen
    is a PERIOD check, not a full amplitude/shape model). See
    `edge_image_phase_difference` for `use_corrected_angle`."""
    dphis = []
    absr = []
    for t in thetas:
        d = edge_image_phase_difference(float(t), lam_cells, cfg, absorb_for_r,
                                         use_corrected_angle=use_corrected_angle)
        dphis.append(d["delta_phi_rad"])
        absr.append(d["abs_r"])
    dphis = np.array(dphis)
    return dict(delta_phi_rad=dphis, abs_r=np.array(absr),
                cos_delta_phi=np.cos(dphis),
                ptp_delta_phi_rad=float(np.ptp(dphis)),
                ptp_delta_phi_deg=float(np.degrees(np.ptp(dphis))))


# =================================== [2] secondary, explicitly naive swaps
def naive_y_wall_period(theta_deg, lam_cells, y_standoff):
    """SECONDARY, NAIVE candidate ONLY (R5-flagged, phase1_proposal.md):
    a bare x<->y coordinate swap of the established x-wall closed form,
    P_y(theta) = (180/pi)*lambda / (2*y_standoff*cos(theta)) -- the trig
    function swaps (sin -> cos) because the wall-normal direction cosine
    swaps (k_x/k=cos(theta) governs the x-wall's standoff term; k_y/k=
    sin(theta) governs a y-wall's, by the SAME derivation structure as
    [1a] -- but see [1b]: this whole closed-ray reduction is NOT justified
    for a y-wall in the first place, so this candidate is reported ONLY as
    a labeled look-elsewhere cross-check, never as this file's own
    primary derivation."""
    theta = math.radians(theta_deg)
    return math.degrees(lam_cells / (2.0 * y_standoff * math.cos(theta)))


# ===================================================== free-period helper
def free_period_with_widening(thetas, delta, label, out_list):
    """SAME staged-widening idiom as pad_round_trip_model.py's own
    `free_period_with_widening` (imported logic pattern, not the function
    itself, since that module is not import-safe standalone here without
    re-running its own main()-adjacent state -- the STAGES and the
    at-boundary rule are reproduced verbatim from that file)."""
    stages = [
        dict(name="narrow[1,4]", lo_deg=1.0, hi_deg=4.0, n_grid=400),
        dict(name="wide[1,15]", lo_deg=1.0, hi_deg=15.0, n_grid=2800),
        dict(name="widest[1,60]", lo_deg=1.0, hi_deg=60.0, n_grid=6000),
    ]
    chosen = None
    for st in stages:
        fit = _free_period_search(thetas, delta, center_deg=39.0,
                                   lo_deg=st["lo_deg"], hi_deg=st["hi_deg"], n_grid=st["n_grid"])
        p = fit["p_star_deg"]
        at_boundary = bool(p <= st["lo_deg"] * 1.005 or p >= st["hi_deg"] * 0.995)
        rec = dict(window=st["name"], p_star_deg=p, r_squared=fit["r_squared"],
                   at_boundary=at_boundary)
        out_list.append(rec)
        print(f"    [{label}] {st['name']:>12}: P*={p:9.4f}deg  R^2={fit['r_squared']:.4f}"
              f"{'  [AT BOUNDARY -- widening]' if at_boundary else '  [interior optimum]'}")
        if chosen is None or (chosen["at_boundary"] and not at_boundary):
            chosen = rec
        if not at_boundary:
            break
    return chosen


def main():
    out = {}
    print("=" * 78)
    print("exp-078 -- y-wall (transverse-normal) echo: closed-form period pre-screen")
    print("=" * 78)

    # ---- [0] premise check ----
    print("\n[0] SHARED-DAMPING-FORMULA PREMISE (y-edge vs x-edge, same Sim instance)")
    prem = verify_shared_damping_formula()
    print(f"    worst |x_edge_col - y_edge_col| = {prem['worst_abs_diff']:.3e}  "
          f"identical={prem['identical']}")
    print(f"    x_edge[:5]={['%.4f' % v for v in prem['x_edge_sample']]}")
    print(f"    y_edge[:5]={['%.4f' % v for v in prem['y_edge_sample']]}")
    assert prem["identical"], "y-edge damping differs from x-edge -- r(theta) reuse premise FALSE"
    out["shared_damping_formula_check"] = prem

    # ---- geometry table ----
    print("\n[1] GEOMETRY PER CONFIG (dg065.CONFIGS, congruent series + G40)")
    geom_table = {}
    hdr = ("cfg", "absorb", "pad", "obj_y", "y_lo", "A", "d_sp", "plane_x", "clear_span_y")
    print("    " + " ".join(f"{h:>10}" for h in hdr))
    for key in CONGRUENT_KEYS:
        c = dg065.CONFIGS[key]
        row = (key, c["absorb"], c["pad"], c["obj_y"], c["y_lo"], c["A"], c["d_sp"],
               c["plane_x"], c["clear_span_y"])
        print("    " + " ".join(f"{v:>10}" for v in row))
        geom_table[key] = dict(absorb=c["absorb"], pad=c["pad"], obj_y=c["obj_y"],
                                y_lo=c["y_lo"], A=c["A"], d_sp=c["d_sp"], plane_x=c["plane_x"],
                                clear_span_y=c["clear_span_y"])
    out["geometry"] = geom_table
    # confirm the queue's own cited clear_span_y pattern
    csy = {k: dg065.CONFIGS[k]["clear_span_y"] for k in ("C40", "G40", "C80")}
    print(f"    clear_span_y check (C40,G40,C80) = {csy} "
          f"(queue-cited pattern: 0/40/0)")
    assert csy == {"C40": 0, "G40": 40, "C80": 0}, csy
    out["clear_span_y_C40_G40_C80"] = csy

    # ---- [1a] x-wall re-derivation, validation ----
    print("\n[2] VALIDATION -- x-wall closed form, RE-DERIVED from scratch, "
          "vs the committed formula")
    validation = {}
    for key in ("C40", "C80"):
        c = dg065.CONFIGS[key]
        p_rederived = x_wall_closed_form_rederivation(39.0, CPL[600], c["plane_x"])
        p_committed = math.degrees(CPL[600] / (2.0 * c["plane_x"] * math.sin(math.radians(39.0))))
        dev = abs(p_rederived - p_committed)
        validation[key] = dict(plane_x=c["plane_x"], p_rederived_deg=p_rederived,
                                p_committed_deg=p_committed, abs_dev_deg=dev)
        print(f"    {key}: plane_x={c['plane_x']:4d}  rederived={p_rederived:.6f}deg  "
              f"committed(boundary_reflectance.py Sec[8])={p_committed:.6f}deg  "
              f"|dev|={dev:.3e}deg")
    assert all(v["abs_dev_deg"] < 1e-9 for v in validation.values()), \
        "x-wall re-derivation does not reproduce the committed formula -- method invalid"
    print("    -> method validated: independent from-scratch re-derivation reproduces "
          "the committed x-wall formula bit-for-bit. Proceeding to apply the SAME "
          "general (mirror-image, evaluated-at-observation-point) method to the y-wall.")
    out["x_wall_rederivation_validation"] = validation

    # ---- real data: PAIR_PAD / PAIR_ABSORB40 (exp-076), C80-C40 (exp-069) ----
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

    print(f"\n[3] REAL, ALREADY-ESTABLISHED PERIODS -- RE-DERIVED here from committed data "
          f"via the SAME imported `_free_period_search` (not hand-typed), "
          f"{len(thetas)} angles, {thetas.min()}-{thetas.max()}deg, 600nm, "
          f"settled STEPS=2800 (experiments/076/results.json::headline)")
    real_stages = {"pair_pad": [], "pair_absorb40": [], "c80_c40": []}
    real_free_pad = free_period_with_widening(thetas, real_delta_pad, "real PAIR_PAD",
                                               real_stages["pair_pad"])
    real_free_absorb40 = free_period_with_widening(thetas, real_delta_absorb40,
                                                     "real PAIR_ABSORB40", real_stages["pair_absorb40"])
    real_free_c80c40 = free_period_with_widening(thetas, real_delta_c80_c40, "real C80-C40",
                                                   real_stages["c80_c40"])
    out["real_periods"] = dict(
        pair_pad=real_free_pad, pair_absorb40=real_free_absorb40, c80_c40=real_free_c80c40,
        stages=real_stages)
    print(f"    established citations to compare against: PAIR_PAD (this run) = "
          f"{real_free_pad['p_star_deg']:.4f}deg (exp-077 cites 4.6113deg); "
          f"PAIR_ABSORB40 (this run) = {real_free_absorb40['p_star_deg']:.4f}deg "
          f"(exp-077 cites 4.1761deg); C80-C40 (this run) = "
          f"{real_free_c80c40['p_star_deg']:.4f}deg (exp-069 cites 2.8421deg)")
    with open(EXP077_RESULTS) as f:
        res77 = json.load(f)
    p750_real = res77.get("test_a_two_wall_pair_pad", {}) or {}
    print(f"    (750nm two-wall PAIR_PAD leg, exp-077 phase1_proposal.md Sec 5c: "
          f"P*_real=3.8271deg, R^2=0.9884 -- carried here as a fourth reference, "
          f"not re-derived, since exp-077's own committed JSON does not persist the "
          f"750nm leg fit under this key; disclosed, not silently dropped)")
    REFERENCE_PERIODS = dict(
        c80_c40_deg=real_free_c80c40["p_star_deg"],
        pair_pad_deg=real_free_pad["p_star_deg"],
        pair_absorb40_deg=real_free_absorb40["p_star_deg"],
        pair_pad_750nm_two_wall_deg=3.8271,
    )
    print(f"    REFERENCE_PERIODS used for scoring below: {REFERENCE_PERIODS}")
    out["reference_periods_deg"] = REFERENCE_PERIODS

    # ---- [1] primary model: edge-image (self-echo) curves per config ----
    print("\n[4] PRIMARY MODEL -- edge-image (self-echo) Delta_phi_self(theta) per config")
    edge_curves = {}
    for key in CONGRUENT_KEYS:
        c = dg065.CONFIGS[key]
        curve = edge_image_curve(thetas, CPL[600], c, c["absorb"])
        edge_curves[key] = curve
        print(f"    {key}: ptp(Delta_phi_self) = {curve['ptp_delta_phi_deg']:.6f}deg (as PHASE, "
              f"not angle-of-theta-sweep) over the window; |r| range "
              f"[{curve['abs_r'].min():.4f},{curve['abs_r'].max():.4f}]")
    out["primary_model_edge_curves"] = {
        k: dict(ptp_delta_phi_deg=v["ptp_delta_phi_deg"],
                abs_r_min=float(v["abs_r"].min()), abs_r_max=float(v["abs_r"].max()))
        for k, v in edge_curves.items()
    }

    print("\n[4b] PRIMARY MODEL -- does Delta_phi_self(theta) even have a resolvable "
          "period over 36-42deg? (free-period search on cos(Delta_phi_self), same "
          "staged-widening idiom as pad_round_trip_model.py; a fit that runs to the "
          "search boundary at every stage means NO well-constrained period exists "
          "in this window under this model -- boundary_reflectance.py's own "
          "'model_period_runs_to_boundary' diagnostic, reused)")
    primary_periods = {}
    primary_stages = {}
    for key in CONGRUENT_KEYS:
        stages_list = []
        chosen = free_period_with_widening(thetas, edge_curves[key]["cos_delta_phi"],
                                            f"model self-echo {key}", stages_list)
        primary_periods[key] = chosen
        primary_stages[key] = stages_list
    out["primary_model_period_search"] = dict(chosen=primary_periods, stages=primary_stages)

    print("\n[4c] PRIMARY MODEL -- PAIR_PAD / PAIR_ABSORB40 deltas of the self-echo proxy curve")
    model_delta_pad = edge_curves["G40"]["cos_delta_phi"] - edge_curves["C40"]["cos_delta_phi"]
    model_delta_absorb40 = edge_curves["C80"]["cos_delta_phi"] - edge_curves["G40"]["cos_delta_phi"]
    model_delta_c80c40 = edge_curves["C80"]["cos_delta_phi"] - edge_curves["C40"]["cos_delta_phi"]
    pair_stages = {"pair_pad": [], "pair_absorb40": [], "c80_c40": []}
    model_free_pad = free_period_with_widening(thetas, model_delta_pad, "model PAIR_PAD delta",
                                                pair_stages["pair_pad"])
    model_free_absorb40 = free_period_with_widening(thetas, model_delta_absorb40,
                                                      "model PAIR_ABSORB40 delta", pair_stages["pair_absorb40"])
    model_free_c80c40 = free_period_with_widening(thetas, model_delta_c80c40, "model C80-C40 delta",
                                                    pair_stages["c80_c40"])
    out["primary_model_pair_deltas"] = dict(
        pair_pad=model_free_pad, pair_absorb40=model_free_absorb40, c80_c40=model_free_c80c40,
        stages=pair_stages,
        ptp_model_delta_pad=float(np.ptp(model_delta_pad)),
        ptp_model_delta_absorb40=float(np.ptp(model_delta_absorb40)))

    def rel_dev(p_real, p_model):
        return abs(p_model - p_real) / p_real

    print("\n[5] PRIMARY MODEL -- period-band scoring (rel_dev<=0.30 SUPPORT / >1.00 REFUTE, "
          "the SAME band exp-075/077 pre-registered for this sub-thread's Test A)")

    def score_period(name, p_real, p_model):
        rd = rel_dev(p_real, p_model)
        if rd <= 0.30:
            v = "SUPPORT"
        elif rd > 1.00:
            v = "REFUTE"
        else:
            v = "INCONCLUSIVE"
        print(f"    {name}: P*_real={p_real:.4f}deg  P*_model={p_model:.4f}deg  "
              f"rel_dev={rd:.4f} -> {v}")
        return dict(p_real_deg=p_real, p_model_deg=p_model, rel_dev=rd, verdict=v)

    primary_scores = {}
    primary_scores["c80_c40_vs_2.8421"] = score_period(
        "self-echo C80-C40 vs C80-C40 real", REFERENCE_PERIODS["c80_c40_deg"],
        model_free_c80c40["p_star_deg"])
    primary_scores["pair_pad_vs_4.6113"] = score_period(
        "self-echo PAIR_PAD vs PAIR_PAD real", REFERENCE_PERIODS["pair_pad_deg"],
        model_free_pad["p_star_deg"])
    primary_scores["pair_absorb40_vs_4.1761"] = score_period(
        "self-echo PAIR_ABSORB40 vs PAIR_ABSORB40 real", REFERENCE_PERIODS["pair_absorb40_deg"],
        model_free_absorb40["p_star_deg"])
    out["primary_model_scores"] = primary_scores
    at_boundary_flags = {
        "c80_c40": model_free_c80c40["at_boundary"],
        "pair_pad": model_free_pad["at_boundary"],
        "pair_absorb40": model_free_absorb40["at_boundary"],
    }
    print(f"    at-search-boundary at EVERY widened stage (no interior optimum found "
          f"anywhere up to 60deg): {at_boundary_flags}")
    out["primary_model_at_boundary_every_stage"] = at_boundary_flags

    # ---- [5b] AS-ORIGINALLY-(INCORRECTLY)-FILED audit-trail comparison ----
    # Mandatory-fix docket item 2 (phase2_redteam_audit.md): the as-filed
    # Phase-1 numbers (raw, unconverted theta fed to reflection_coefficient)
    # are kept ONLY as an explicitly labeled comparison row, never as the
    # headline. Reuses the SAME edge_image_curve/free_period_with_widening/
    # score_period machinery, only the angle-convention flag differs.
    print("\n[5b] AS-ORIGINALLY-(INCORRECTLY)-FILED audit trail (raw theta, not "
          "90-theta -- kept ONLY for comparison, per phase2_redteam_audit.md's "
          "mandatory-fix docket item 2; NOT this file's own claim)")
    as_filed_curves = {key: edge_image_curve(thetas, CPL[600], dg065.CONFIGS[key],
                                              dg065.CONFIGS[key]["absorb"],
                                              use_corrected_angle=False)
                        for key in CONGRUENT_KEYS}
    as_filed_delta_pad = as_filed_curves["G40"]["cos_delta_phi"] - as_filed_curves["C40"]["cos_delta_phi"]
    as_filed_delta_absorb40 = as_filed_curves["C80"]["cos_delta_phi"] - as_filed_curves["G40"]["cos_delta_phi"]
    as_filed_delta_c80c40 = as_filed_curves["C80"]["cos_delta_phi"] - as_filed_curves["C40"]["cos_delta_phi"]
    as_filed_pair_stages = {"pair_pad": [], "pair_absorb40": [], "c80_c40": []}
    as_filed_free_pad = free_period_with_widening(thetas, as_filed_delta_pad,
                                                    "AS-FILED PAIR_PAD delta", as_filed_pair_stages["pair_pad"])
    as_filed_free_absorb40 = free_period_with_widening(thetas, as_filed_delta_absorb40,
                                                          "AS-FILED PAIR_ABSORB40 delta",
                                                          as_filed_pair_stages["pair_absorb40"])
    as_filed_free_c80c40 = free_period_with_widening(thetas, as_filed_delta_c80c40,
                                                        "AS-FILED C80-C40 delta", as_filed_pair_stages["c80_c40"])
    as_filed_scores = {}
    as_filed_scores["c80_c40_vs_2.8421"] = score_period(
        "AS-FILED self-echo C80-C40 vs C80-C40 real", REFERENCE_PERIODS["c80_c40_deg"],
        as_filed_free_c80c40["p_star_deg"])
    as_filed_scores["pair_pad_vs_4.6113"] = score_period(
        "AS-FILED self-echo PAIR_PAD vs PAIR_PAD real", REFERENCE_PERIODS["pair_pad_deg"],
        as_filed_free_pad["p_star_deg"])
    as_filed_scores["pair_absorb40_vs_4.1761"] = score_period(
        "AS-FILED self-echo PAIR_ABSORB40 vs PAIR_ABSORB40 real", REFERENCE_PERIODS["pair_absorb40_deg"],
        as_filed_free_absorb40["p_star_deg"])
    print("\n    AS-FILED (incorrect) vs CORRECTED (primary), side by side:")
    for k, real_p in (("c80_c40_vs_2.8421", None), ("pair_pad_vs_4.6113", None),
                       ("pair_absorb40_vs_4.1761", None)):
        af = as_filed_scores[k]
        co = primary_scores[k]
        print(f"      {k:24s} AS-FILED  rel_dev={af['rel_dev']:.4f} -> {af['verdict']:<12}  "
              f"CORRECTED  rel_dev={co['rel_dev']:.4f} -> {co['verdict']}")
    out["as_filed_incorrect_audit_trail"] = dict(
        note="Phase-1-as-originally-computed (raw theta, not 90-theta); kept ONLY as a "
             "labeled comparison row per phase2_redteam_audit.md's mandatory-fix docket "
             "item 2, NEVER as this file's primary claim (see [5]/[7] for the corrected "
             "primary result).",
        scores=as_filed_scores,
        pair_deltas=dict(pair_pad=as_filed_free_pad, pair_absorb40=as_filed_free_absorb40,
                          c80_c40=as_filed_free_c80c40, stages=as_filed_pair_stages))

    # ---- [2] secondary naive candidates ----
    print("\n[6] SECONDARY, EXPLICITLY NAIVE candidates (R5-flagged look-elsewhere risk -- "
          "reported for the queue item's own 'is it even in the right ballpark' question, "
          "NEVER as this file's own primary claim; see [1b] in the module docstring for why "
          "the underlying closed-ray reduction is not justified for a y-wall in the first place)")
    naive_candidates = {}
    for standoff_name, standoff_key in (("OBJ_Y", "obj_y"), ("y_lo", "y_lo")):
        naive_candidates[standoff_name] = {}
        print(f"  -- Y_STANDOFF = {standoff_name} --")
        for key in CONGRUENT_KEYS:
            c = dg065.CONFIGS[key]
            standoff = c[standoff_key]
            p600 = naive_y_wall_period(39.0, CPL[600], standoff)
            p750 = naive_y_wall_period(39.0, CPL[750], standoff)
            naive_candidates[standoff_name][key] = dict(
                standoff_cells=standoff, period_deg_600nm=p600, period_deg_750nm=p750)
            print(f"    {key}: {standoff_name}={standoff:4d}  P_y(600nm,39deg)={p600:.4f}deg  "
                  f"P_y(750nm,39deg)={p750:.4f}deg")
    out["naive_secondary_candidates"] = naive_candidates

    print("\n[6b] SECONDARY candidates vs all four reference periods (rel_dev, period-band only, "
          "R5-CAVEATED -- multiple candidates x multiple targets is a search, not evidence; "
          "no null-permutation control is run here, so NO match below is claimed as support)")
    naive_scores = {}
    for standoff_name in naive_candidates:
        naive_scores[standoff_name] = {}
        for key in ("C40", "C80", "G40"):
            p600 = naive_candidates[standoff_name][key]["period_deg_600nm"]
            row = {}
            for ref_name, ref_val in (("c80_c40", REFERENCE_PERIODS["c80_c40_deg"]),
                                       ("pair_pad", REFERENCE_PERIODS["pair_pad_deg"]),
                                       ("pair_absorb40", REFERENCE_PERIODS["pair_absorb40_deg"]),
                                       ("pair_pad_750nm", REFERENCE_PERIODS["pair_pad_750nm_two_wall_deg"])):
                row[ref_name] = rel_dev(ref_val, p600)
            naive_scores[standoff_name][key] = row
            print(f"    {standoff_name}/{key}: P_model={p600:8.4f}deg  rel_dev vs "
                  f"[c80c40,pad,absorb40,pad750]="
                  f"[{row['c80_c40']:.3f},{row['pair_pad']:.3f},"
                  f"{row['pair_absorb40']:.3f},{row['pair_pad_750nm']:.3f}]")
    out["naive_secondary_rel_dev"] = naive_scores

    # ---- [7] gate re-run at the CORRECTED y-wall angle envelope ----
    # Mandatory-fix docket item 3 (phase2_redteam_audit.md Attack 2): the
    # x-wall's own sanity/passivity gates (boundary_reflectance.py) were only
    # ever sampled at theta in [-44,44]deg; the CORRECTED y-wall call routes
    # reflection_coefficient through 48-54deg (90-theta for theta in
    # [36,42]deg), a range never previously gate-tested. Re-run here,
    # near-verbatim from phase2_redteam_angle_correction_check.py Sec [E]
    # (Red Team's own already-verified corrected pipeline, reused per the
    # docket rather than re-derived a fifth time).
    print("\n[7] GATE RE-RUN at the corrected y-wall envelope (48-54deg), never "
          "sampled by the originally committed +-44deg gates")

    def gate_lossless_unimodular_range(lo, hi, n_trials=2000, seed=11):
        rng = np.random.default_rng(seed)
        worst = 0.0
        for _ in range(n_trials):
            length = int(rng.integers(5, 60))
            n_prof = 1.0 + 0.6 * rng.random(length)
            theta_deg = float(rng.uniform(lo, hi))
            r = br.reflection_coefficient(n_prof.astype(complex), theta_deg, 20.0)
            worst = max(worst, abs(abs(r) - 1.0))
        return worst

    def gate_single_layer_identity_range(lo, hi, n_trials=2000, seed=13):
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

    def gate_passivity_range(lo, hi, n_trials=2000, seed=17):
        rng = np.random.default_rng(seed)
        worst = 0.0
        for absorb in br.ABSORB_LIST:
            damp = br.damp_e_profile(absorb)
            nu = br.nu_profile(damp)
            n_exact = br.n_profile_exact(nu, 2.0 * math.pi / CPL[600])
            for _ in range(n_trials // len(br.ABSORB_LIST)):
                theta_deg = float(rng.uniform(lo, hi))
                r = br.reflection_coefficient(n_exact, theta_deg, CPL[600])
                worst = max(worst, abs(r))
        return worst

    g_lossless_new = gate_lossless_unimodular_range(48.0, 54.0)
    g_n1_new = gate_single_layer_identity_range(48.0, 54.0)
    g_pass_new = gate_passivity_range(48.0, 54.0)
    print(f"    G-LOSSLESS (48-54deg, 2000 trials): worst ||r|-1| = {g_lossless_new:.3e}  "
          f"PASS={g_lossless_new < 1e-9}")
    print(f"    G-N1       (48-54deg, 2000 trials): worst |r_loop-r_direct| = {g_n1_new:.3e}  "
          f"PASS={g_n1_new < 1e-12}")
    print(f"    G-PASSIVITY(48-54deg, 2000 trials/depth): worst |r| = {g_pass_new:.6f}  "
          f"PASS={g_pass_new <= 1.0 + 1e-9}")
    gates_corrected = dict(
        g_lossless_worst_dev=g_lossless_new, g_lossless_pass=bool(g_lossless_new < 1e-9),
        g_n1_worst_dev=g_n1_new, g_n1_pass=bool(g_n1_new < 1e-12),
        g_passivity_worst_abs_r=g_pass_new, g_passivity_pass=bool(g_pass_new <= 1.0 + 1e-9))
    assert gates_corrected["g_lossless_pass"] and gates_corrected["g_n1_pass"] \
        and gates_corrected["g_passivity_pass"], \
        "corrected-envelope gate FAILED -- do not trust r(theta) at 48-54deg"
    out["gates_at_corrected_envelope_48_54deg"] = gates_corrected

    # ---- combined self-scored verdict inputs ----
    print("\n[8] SUMMARY FOR PHASE-1 SELF-SCORING (CORRECTED primary model, "
          "post Phase-2 Red Team mandatory-fix docket)")
    n_primary_refute = sum(1 for v in primary_scores.values() if v["verdict"] == "REFUTE")
    n_primary_support = sum(1 for v in primary_scores.values() if v["verdict"] == "SUPPORT")
    n_as_filed_support = sum(1 for v in as_filed_scores.values() if v["verdict"] == "SUPPORT")
    print(f"    CORRECTED primary model: {n_primary_refute}/3 comparisons REFUTE on the "
          f"period band; {n_primary_support}/3 SUPPORT; every pair-delta period search ran "
          f"to the search boundary at all three widened stages (no interior optimum found "
          f"up to 60deg) = {all(at_boundary_flags.values())}")
    print(f"    (AS-FILED, incorrect-angle audit trail: {n_as_filed_support}/3 SUPPORT -- "
          f"kept for comparison only, per phase2_redteam_audit.md item 2, NOT the headline)")
    out["summary"] = dict(
        n_primary_refute=n_primary_refute, n_primary_support=n_primary_support,
        all_primary_at_boundary=bool(all(at_boundary_flags.values())),
        n_as_filed_support_audit_trail_only=n_as_filed_support)

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

    out_path = os.path.join(HERE, "y_wall_prescreen_results.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2, default=_json_default)
    print(f"\nwrote {out_path}")
    return out


if __name__ == "__main__":
    main()
