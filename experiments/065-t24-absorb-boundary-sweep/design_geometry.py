"""exp-065 design constants -- the dedicated T24 `ABSORB` boundary sweep on
the ambient-contrast (`C_empty`) channel.
=============================================================================
Panel Iteration 42, PHASE 1 (lead: VISION SCIENCE, by rotation). This file is
the PROPOSAL's arithmetic: every number quoted in `phase1_proposal.md` is
produced by running `python3 design_geometry.py`, never hand-typed (house rule
R4/R5, LOGBOOK.md RULED OUT).

Executes live thread T24's own never-run design (opened Iteration 23, exp-046
Phase-5 docket item 19; designed at Iteration 24 Tier-2 #4; re-ranked at
Iterations 25 (#3), 26 (#2), 28) -- "sweep ABSORB with SRC_X moved clear of the
x-damping band so EM's ABSORB=80 confound does not recur, source span held
fixed, all 3 lambda".

THE ONE CHANGE: `absorb` (the graded-loss band thickness, `lab/fdtd2d.py::
Sim._damping`) becomes a controlled variable instead of an inherited constant.

THE CONSTRUCTION (this cycle's own contribution to the T24 design): rather than
move `SRC_X` alone -- which changes `D_SP` and therefore the whole T21 fringe
geometry -- PAD the domain by exactly `ABSORB - 40` on every side and shift
every scene coordinate by the same amount. Under `PAD = ABSORB - 40`:

  * A  = OBJ_Y - y_lo               = 752  cells, for every ABSORB
  * plane-to-(-x)-band clearance    = 37   cells, for every ABSORB
  * source-to-(+x)-band clearance   = 20   cells, for every ABSORB
  * source-span-end-to-y-band       = 0    cells, for every ABSORB
  * D_SP, LEVER, window geometry    unchanged, for every ABSORB

so the ONLY thing that varies across the CONGRUENT series is the band's own
thickness and graded-loss profile. This is verified below, in code, and it is
verified a second way by the desk propagator: exp-048's committed
`edge_diffraction_c_empty_corrected` (a boundary-FREE Huygens-Fresnel sum)
returns BIT-IDENTICAL C_empty for C40/C60/C80, so any difference the FDTD
returns between them is boundary physics by construction, not geometry.

Configurations:
  C40  ABSORB=40 PAD= 0  -- exp-041's geometry VERBATIM (identity anchor)
  C60  ABSORB=60 PAD=20  -- congruent
  C70  ABSORB=70 PAD=30  -- congruent, PHASE-3 MANDATORY FIX 1 (Red Team
                            attack 1): ABSORB in {40,60,80} at cpl=20/600nm are
                            EXACT integer multiples of lambda (2/3/4 lambda) --
                            the one wavelength Block ARTICLE scores -- with no
                            non-aliased point to rule out a periodic boundary-
                            reflectivity artifact. ABSORB=70 checked against
                            all three cpl: 70/15=4.667, 70/20=3.5, 70/25=2.8 --
                            none an integer (ABSORB=50 was checked and
                            REJECTED: 50/25=2.0 exactly, still aliased at
                            750nm).
  C80  ABSORB=80 PAD=40  -- congruent
  G40  ABSORB=40 PAD=40  -- pad-only control (isolates the padding itself)
  N60  ABSORB=60 PAD= 0  -- the NAIVE protocol: what a same-domain ABSORB
                            bump does. `add_line_source`'s default span is
                            [absorb, ny-absorb], so A drops 752 -> 732 and the
                            plane clearance drops 37 -> 17. Run deliberately,
                            labeled, as the diagnostic that quantifies what the
                            naive sweep adds on top of the boundary change.

PHASE-3 MANDATORY FIXES applied here (Red Team, Panel Iteration 42 Phase 2 --
verdict PROCEED-WITH-MANDATORY-FIXES; full numbered attack list in
`phase2_redteam_audit.md`, disposition table in `phase3_synthesis.md`):
  1. C70 added (above) -- closes the integer-lambda aliasing risk on
     P-VIS42-2's headline.
  2. `causal_identity_step` recomputed at the stencil's TRUE numerical domain
     of dependence (1 cell/step), not the wave's Courant phase speed S --
     EM's catch: S bounds where the physical wavefront sits, not where a
     discrete 5-point-stencil recursion's exact-zero boundary sits. n=247,
     not 359 (a 45% overstatement the old derivation carried).
  3. `MINI_SWEEP_ANGLES` added below -- a dense (0.5 deg step) angular scan
     over one T21 fringe period at 600nm, falsifying the "matched-angle
     differencing cancels the quadrature phase error to first order"
     premise (QUANTUM's catch) directly, rather than assuming it.
  5. `G_TRANSFER` and `ARTICLE_CENTRAL_ESTIMATE` computed here in code (were
     hand-typed as 0.69 / 0.00449 in phase1_proposal.md, an R4 violation --
     Red Team attack 4), carrying T15's non-portability caveat inline.
  7. `STEPS_SETTLE` added -- the largest padded domain (ABSORB=80) gets one
     STEPS=2800 leg to close the settling-time/domain-size confound (Red
     Team attack 7, this program's own T10 precedent).
Fixes 4, 6, 8-11 are documentation-only (REALIZABILITY_MEMO.md / T5
citations, the CNT R_contact trade-off sentence, wording softening) and land
in NOTES.md / phase3_synthesis.md, not here.

Pure geometry + desk arithmetic -- NO FDTD in this file.
"""

import importlib.util
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..")))


def _load_exp048():
    """exp-048's propagator module is ALSO called `design_geometry`, so a
    plain `import design_geometry` collides with this file (and, when this
    file is imported as a module rather than run as __main__, resolves to a
    partially-initialized self). Load it explicitly under a distinct name."""
    path = os.path.abspath(os.path.join(
        HERE, "..", "048-evidentiary-chord-closure", "design_geometry.py"))
    spec = importlib.util.spec_from_file_location("_exp048_design_geometry", path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["_exp048_design_geometry"] = mod
    spec.loader.exec_module(mod)
    return mod


dg048 = _load_exp048()                    # exp-048's committed desk propagator
from lab import glare_sidecar as gs      # noqa: E402
from lab.fdtd2d import Sim as _Sim       # noqa: E402  (G-2 replacement, zero-step)

# --------------------------------------------------------------- base geometry
# Copied VERBATIM from experiments/041-t20-angle-audit/design_geometry.py
# (itself copied verbatim from exp-024). Nothing here is recomputed.
BASE_NX = 360
BASE_NY = 1584
BASE_ABSORB = 40
BASE_SRC_X = 300
BASE_PLANE_X = 77
BASE_OBJ_X = 170
BASE_OBJ_Y = BASE_NY // 2                     # 792
TAPER = 40
R_OUT = 78
W_OBJ = 78
GUARD_OUT = 185
W_FLANK = 78
CPL = {450: 15, 600: 20, 750: 25}
STEPS = 1400
COURANT_FRAC = 0.99
D_SP = BASE_SRC_X - BASE_PLANE_X              # 223
LEVER = BASE_OBJ_X - BASE_PLANE_X             # 93

FALLBACK_ANGLES = (-35, -25, -15, -5, 0, 5, 15, 25, 35)   # exp-024's own N=9
SWEEP_ANGLES = (-40.0, -38.0, -35.0, 35.0, 38.0, 40.0)    # this cycle's 6
ANCHOR_ANGLES = (-40.0, -38.0, 38.0, 40.0)   # the 4 present in exp-041 Block MAIN

# PHASE-3 FIX 3 (Red Team attack 5 / QUANTUM's catch): a dense angular mini-
# sweep spanning >=1 full T21 fringe period at 600nm, centered near the
# sweep's own theta=40 edge. P(40deg, A=752, 600nm) = 1.989 deg (design
# arithmetic below); span 2.0deg at 0.5deg steps = 5 angles, C40 and C80 only.
MINI_SWEEP_CENTER = 39.0
MINI_SWEEP_HALF_SPAN = 1.0
MINI_SWEEP_STEP = 0.5
MINI_SWEEP_ANGLES = tuple(
    MINI_SWEEP_CENTER + i * MINI_SWEEP_STEP
    for i in range(-int(MINI_SWEEP_HALF_SPAN / MINI_SWEEP_STEP),
                   int(MINI_SWEEP_HALF_SPAN / MINI_SWEEP_STEP) + 1)
)   # (38.0, 38.5, 39.0, 39.5, 40.0)

# PHASE-3 FIX 7 (Red Team attack 7 / T10 precedent): settling-time check at
# the largest padded domain, ABSORB=80, one representative cell.
STEPS_SETTLE = 2800
SETTLE_CELL = dict(absorb="C80", theta=40.0, lambda_nm=600)

# The `off_pass` sigma(I) OFF-state article (exp-032/033/034/056), expressed at
# this bench's own radius under this lab's optical-depth convention
# tau_center = 2*sigma*r_out.
TAU_OFF_PASS = 0.0065
SIGMA_OFF_PASS = TAU_OFF_PASS / (2 * R_OUT)

# REALIZABILITY_MEMO.md (T2/T9 lineage): this EXACT tau=0.0065 no longer
# clears the realizability bar at EITHER geometry it has been checked at
# (the memo's own Amendment, Iteration 12) -- D_req~540-600x there is a
# LOWER bound, not an achieved reference point. Cited here, not silently
# reused (Red Team attack 3 / MATERIALS' catch).
REALIZABILITY_MEMO_CAVEAT = (
    "REALIZABILITY_MEMO.md names tau_off=0.0065 (exp-032 off_pass) as the "
    "basis of its UNOBTANIUM-WITH-PARAMETERS verdict (D_req~540-600x); its "
    "own Amendment (Iteration 12) states this tau 'no longer clears the bar "
    "at EITHER geometry it has ever been checked at' and that D_req should "
    "be read as a LOWER bound, not an achieved PASS reference. Block "
    "ARTICLE reuses this tau as an instrument-uncertainty probe ONLY -- it "
    "is not a new realizability claim and does not re-open or re-score the "
    "memo's own verdict.")

# T5/Iteration-20 (exp-043, lab/thermo_sidecar.py): every OFF-state sigma(I)
# article at bench scale reads UNDETECTABLE, >100x below sourced
# microbolometer NETD. Block ARTICLE's disk shares tau and construction
# idiom with that exact class -- cited so the disposition is inherited
# explicitly, not silently (Red Team attack 6 / THERMODYNAMICS' catch).
T5_THERMAL_CAVEAT = (
    "Block ARTICLE's tau=0.0065 uniform disk shares tau and construction "
    "idiom with the OFF-state article class T5/Iteration-20 (exp-043) "
    "established as UNDETECTABLE, >100x below sourced microbolometer NETD. "
    "Only the far-boundary padding changes between C40 and C80 (same "
    "sigma, same r_out) -- that disposition is inherited unchanged here; "
    "no new thermal question is opened by this cycle.")

# g = |C|/tau_center transfer constant (T1, Iteration 8/exp-031), used ONLY
# for a DESCRIPTIVE, NOT SCORED, central estimate at P-VIS42-7 -- T15 (LIVE
# THREADS) established this constant is NOT portable across geometries; it
# is reported with that caveat inline, not as a prediction (Red Team attack
# 4 -- was hand-typed as 0.00449 in phase1_proposal.md; now code-produced).
G_TRANSFER = 0.69
G_TRANSFER_T15_CAVEAT = (
    "g=0.69 is T1's established OFF-state transfer constant (multiple "
    "confirmations at OTHER geometries), NOT re-derived at this cycle's "
    "own geometry. T15 (LIVE THREADS) found this constant is geometry-"
    "specific, not portable -- this estimate is descriptive context only, "
    "never scored as a prediction.")
ARTICLE_CENTRAL_ESTIMATE = G_TRANSFER * TAU_OFF_PASS   # descriptive only

# --------------------------------------------------------------- decision bars
GATE_HARD = 0.001              # exp-024/041's own committed instrument-floor
                                # gate -- THE bar that scores every empty-scene
                                # row in this experiment (exp-041 mandatory
                                # fix 1: an instrument floor is NOT scored
                                # against a perceptual threshold)
C_THR_LAB = gs.c_thr(3.0, 0.4, bar="lab")      # T2 frozen photopic lab bar
C_THR_FIELD = gs.c_thr(3.0, 0.4, bar="field")  # T2 frozen field bar (context)
MARGINAL_LO, MARGINAL_HI = dg048.MARGINAL_LO, dg048.MARGINAL_HI

# T24's own published beam-channel numbers (exp-046 phase5_redteam_audit.md
# section 7 table) -- the figures Block BEAM must reproduce from committed code.
T24_BEAM = {
    "A-v4": dict(lambda_nm=750, theta0_deg=38.0, fwhm_deg=2.0,
                 desk_C=+0.163673, fdtd_C_absorb40=+0.154376,
                 fdtd_C_absorb60=+0.161333, delta=+0.00696),
    "A-v1": dict(lambda_nm=600, theta0_deg=40.0, fwhm_deg=2.0,
                 desk_C=-0.123345, fdtd_C_absorb40=-0.125698,
                 fdtd_C_absorb60=-0.127896, delta=-0.00220),
}

# ---------------------------------------------------------- measured cost basis
# MEASURED on THIS container, 2026-08-24, pre-freeze, at cpl=20/STEPS=1400/
# full_capture, four calls per domain under ProcessPoolExecutor(max_workers=4)
# -- i.e. WITH the 4-way memory contention the real run will have, not a
# single-process figure extrapolated by cell count (cost scales worse than
# cell count on this box: C80/C40 = 1.39x for a 1.28x cell ratio).
#   360x1584 (C40, N60): 24.48 / 25.53 / 24.26 / 25.33 s  -> 25.0 s used
#   400x1624 (C60)     : 29.48 / 30.95 / 32.58 / 31.30 s  -> 31.1 s used
#   440x1664 (C80, G40): 34.55 / 34.08 / 35.49 / 35.17 s  -> 34.8 s used
# Wall for 4 concurrent calls at 440x1664 = 35.51 s -> parallel efficiency
# 0.981 (nproc = 4; capture footprint 35.1 MB/sim, 14 GB free).
# Cross-check on the smallest domain, single process: 20.651 s, and that call
# reproduced C_empty = -0.010964794540566314, BIT-IDENTICAL to exp-041
# results.json block_main (theta=+40, 600 nm).
CPU_S_PER_CALL = {"C40": 25.0, "N60": 25.0, "C60": 31.1, "C80": 34.8, "G40": 34.8,
                   # C70 (pad=30, nx=420,ny=1644): not separately measured;
                   # linearly interpolated between the measured C60(pad=20)/
                   # C80(pad=40) figures -- disclosed as an estimate, not a
                   # measurement, and used only for the wall-clock budget
                   # (never for a physics comparison).
                   "C70": 0.5 * (31.1 + 34.8)}
BASE_CELLS = BASE_NX * BASE_NY
N_WORKERS = 4
PARALLEL_EFFICIENCY = 0.98
OVERHEAD_FACTOR = 1.15          # phasors/window reduction/JSON, not measured


# --------------------------------------------------------------- constructions
def config(absorb, pad, naive=False):
    """One FDTD configuration. `pad` cells are added on EVERY side and every
    scene coordinate shifts by `pad`.

    `naive=False` (this cycle's construction): the source span is passed
    EXPLICITLY and shifts with the scene, y_lo = BASE_ABSORB + pad, so the
    half-aperture A = OBJ_Y - y_lo = 752 is held for every ABSORB.
    `naive=True`: the span is left to `add_line_source`'s own default,
    y_lo = absorb -- which is what a same-domain ABSORB bump silently does,
    and which drags A with it."""
    nx = BASE_NX + 2 * pad
    ny = BASE_NY + 2 * pad
    src_x = BASE_SRC_X + pad
    plane_x = BASE_PLANE_X + pad
    obj_x = BASE_OBJ_X + pad
    obj_y = BASE_OBJ_Y + pad
    y_lo = absorb if naive else (BASE_ABSORB + pad)
    y_hi = ny - y_lo
    return dict(
        naive=naive,
        absorb=absorb, pad=pad, nx=nx, ny=ny,
        src_x=src_x, plane_x=plane_x, obj_x=obj_x, obj_y=obj_y,
        y_lo=y_lo, y_hi=y_hi,
        A=obj_y - y_lo,
        aperture_cells=y_hi - y_lo,
        clear_plane=plane_x - absorb,
        clear_src=(nx - absorb) - src_x,
        clear_span_y=y_lo - absorb,
        d_sp=src_x - plane_x,
        lever=obj_x - plane_x,
        cells=nx * ny,
    )


CONFIGS = {
    "C40": config(40, 0),     # exp-041 verbatim -- identity anchor
    "C60": config(60, 20),    # congruent
    "C70": config(70, 30),    # congruent -- Phase-3 fix 1, non-aliased point
    "C80": config(80, 40),    # congruent
    "G40": config(40, 40),    # pad-only control (A held at 752, clearances +40)
    "N60": config(60, 0, naive=True),   # naive protocol (A drops to 732)
}
CONGRUENT_KEYS = ("C40", "C60", "C70", "C80")   # every ABSORB point in the series


def propagator_geom(cfg):
    """The geometry dict exp-048's committed desk propagator consumes.
    `_geom_derived` uses g["ABSORB"] ONLY to derive the aperture span
    [ABSORB, NY-ABSORB], so the span -- not the band thickness -- is what
    must be handed over (checked by the assert)."""
    assert cfg["y_hi"] == cfg["ny"] - cfg["y_lo"], "span not symmetric"
    return dict(NY=cfg["ny"], OBJ_Y=cfg["obj_y"], D_SP=cfg["d_sp"],
                GUARD_OUT=GUARD_OUT, R_OUT=R_OUT, W_FLANK=W_FLANK,
                PLANE_X=cfg["plane_x"], SRC_X=cfg["src_x"],
                ABSORB=cfg["y_lo"], TAPER=TAPER)


def causal_identity_step(cfg_a, cfg_b, _speed=1.0):
    """The largest step count at which the observer-plane row of two
    configurations is guaranteed IDENTICAL by causality alone -- i.e. before
    any signal that has touched a region where the two domains differ can have
    reached the plane.

    PHASE-3 FIX 2 (Red Team attack 2 / EM's catch, Panel Iteration 42): the
    bound uses the leapfrog stencil's TRUE numerical domain of dependence,
    which is EXACTLY 1 cell/step (traced directly from lab/fdtd2d.py::
    Sim.run: the H-update reads Ez at +-1 cell, the E-update reads the
    just-computed H at +-1 cell, so Ez(new,i,j) depends only on Ez(old,i,j)
    and its 4 nearest neighbors -- a 5-point cross, independent of
    courant_frac). The wave's own Courant phase speed S = courant/sqrt(2)
    cells/step bounds where the PHYSICAL wavefront sits; it is NOT a bound
    on where a discrete, finite-support recursion's exact-zero boundary
    sits, and conflating the two overstated the old n=359 bound by 45%
    (this program's own R2/T16/T21/R5 lesson: a modeled-physics bound is
    not a numerical one). Using 1 cell/step is the rigorous, strictly
    harder bound; a PASS at this bound is a proof, not merely evidence.

    The gate is read ONLY over the scored windows of the plane row
    (|y - OBJ_Y| <= W_OBJ, and GUARD_OUT..GUARD_OUT+W_FLANK both sides) --
    NOT the whole row, because the y-band difference region sits flush
    against the source-span end and reaches the row's outermost cells early.

    Three round trips must be excluded, per configuration, all measured from
    the source (the only place energy enters):
      (i)   source -> (+x) band inner edge -> back to the plane
              = 2*clear_src + (src_x - plane_x)
      (ii)  source -> plane -> (-x) band inner edge -> back to the plane
              = d_sp + 2*clear_plane
      (iii) source -> (y) band inner edge -> nearest scored window cell
              = max(clear_span_y, 1) + hypot(d_sp, GUARD_OUT - W_OBJ + ...)
            conservatively: 1 + hypot(d_sp, GUARD_OUT)
    The bound is the earliest of the six, minus a 16-step guard, divided by
    the stencil's 1 cell/step domain-of-dependence growth rate (not S).

    `_speed` is exposed only so `main()` can print the OLD, over-stated
    bound (at S) alongside the corrected one for the record -- every live
    call site in this experiment uses the default."""
    paths = []
    for c in (cfg_a, cfg_b):
        paths.append(2 * c["clear_src"] + (c["src_x"] - c["plane_x"]))
        paths.append(c["d_sp"] + 2 * c["clear_plane"])
        paths.append(max(c["clear_span_y"], 1)
                     + float(np.hypot(c["d_sp"], GUARD_OUT)))
    return int(np.floor(min(paths) / _speed)) - 16


def static_construction_identity(cfg_a, cfg_b, pad):
    """PHASE-3 G-2 REPLACEMENT (Director's remedy, discovered applying Red
    Team's own fix 2): the corrected `causal_identity_step` (1 cell/step)
    gives n=247 for (C40, G40) -- but the direct source->plane arrival time
    is D_SP/S = ceil(223/0.700036) = 319. 247 < 319: the dynamic causal-
    field snapshot gate has NO VALID WINDOW at this geometry -- by the time
    real signal reaches the plane, the topological (not physical) domain of
    dependence has already had time to connect the boundary-difference
    region to it. This is exactly the proposal's own stated halt condition
    ("if (c) fails, the cycle stops... diagnose before any other FDTD call
    reads a result") -- caught at the DESK stage, before any FDTD call, at
    zero cost. Diagnosis: the dynamic argument was the wrong tool. The
    construction claim it existed to verify -- "the padded region is a pure
    vacuum extension, and the shared footprint's SCORED WINDOW is
    unperturbed by the shift" -- is a STATIC fact about the damping arrays,
    not a transient one, and is strictly stronger to check directly: build
    both `Sim` objects (ZERO `.run()` steps -- `__init__` alone computes
    `damp_e`/`damp_hx`/`damp_hy`) and compare them bit-for-bit at the actual
    scored-window cells, offset by `pad`. True at EVERY time step (not
    merely before some causal horizon), and catches the exact class of bug
    (coordinate-shift error, off-by-one, asymmetric pad) the dynamic gate
    was built to catch -- more directly, since a construction bug lives in
    the STATIC arrays, not in wave propagation."""
    a = _Sim(cfg_a["nx"], cfg_a["ny"], cells_per_lambda=20,
              courant_frac=COURANT_FRAC, absorb=cfg_a["absorb"])
    b = _Sim(cfg_b["nx"], cfg_b["ny"], cells_per_lambda=20,
              courant_frac=COURANT_FRAC, absorb=cfg_b["absorb"])
    y_obj = slice(BASE_OBJ_Y - W_OBJ, BASE_OBJ_Y + W_OBJ + 1)
    y_fl_lo = slice(BASE_OBJ_Y - GUARD_OUT - W_FLANK, BASE_OBJ_Y - GUARD_OUT + 1)
    y_fl_hi = slice(BASE_OBJ_Y + GUARD_OUT, BASE_OBJ_Y + GUARD_OUT + W_FLANK + 1)
    x = BASE_PLANE_X
    diffs = {}
    for name, ysl in (("obj", y_obj), ("flank_lo", y_fl_lo), ("flank_hi", y_fl_hi)):
        for arr_name, arr_a, arr_b in (("damp_e", a.damp_e, b.damp_e),
                                        ("damp_hx", a.damp_hx, b.damp_hx)):
            va = arr_a[x, ysl]
            vb = arr_b[x + pad, slice(ysl.start + pad, ysl.stop + pad)]
            diffs[f"{name}/{arr_name}"] = float(np.max(np.abs(va - vb)))
    return dict(max_diff=max(diffs.values()), by_window=diffs,
                all_vacuum=bool(np.all(a.damp_e[x, y_obj] == 1.0)))


def fdtd_budget():
    """Call counts and wall-clock, block by block. Article/empty legs are
    counted explicitly; no leg is double-counted (FALLBACK angles shared with
    Block SWEEP at 600 nm are reused, not re-run). Includes Phase-3 fixes
    1 (C70), 3 (mini-sweep) and 7 (settling check)."""
    n_lam = len(CPL)
    n_sweep_ang = len(SWEEP_ANGLES)
    # Block SWEEP: 6 angles x 3 lambda, at C40/C60/C70/C80/N60 (fix 1: +C70)
    sweep = {k: n_sweep_ang * n_lam for k in ("C40", "C60", "C70", "C80", "N60")}
    # Block PAD: G40 at theta in {-35,35,40} x 3 lambda (pad-only control +
    # the causal-identity gate's own pair)
    pad = {"G40": 3 * n_lam}
    # Block ARTICLE: N9 FALLBACK at 600 nm, article + empty, at C40 and C80.
    # +-35 @600nm empty already exist in Block SWEEP -> 7 new empty angles.
    article = {"C40": len(FALLBACK_ANGLES) + 7, "C80": len(FALLBACK_ANGLES) + 7}
    # Block BEAM: 2 T24 cells at C40 / C60 / N60
    beam = {"C40": 2, "C60": 2, "N60": 2}
    # Block MINI (fix 3): MINI_SWEEP_ANGLES = (38,38.5,39,39.5,40) @ 600nm.
    # 38 and 40 already exist in Block SWEEP for C40/C80 (SWEEP_ANGLES
    # includes +-38/+-40) -- reused, not re-run. Only 38.5/39/39.5 are new.
    n_mini_new = sum(1 for a in MINI_SWEEP_ANGLES if a not in SWEEP_ANGLES)
    mini = {"C40": n_mini_new, "C80": n_mini_new}
    # Block SETTLE (fix 7): 1 extra STEPS=2800 call at C80/40deg/600nm,
    # counted at 2x the STEPS=1400 cost (linear in step count).
    settle = {"C80_settle": 2}
    per_cfg = {}
    for d in (sweep, pad, article, beam, mini):
        for k, v in d.items():
            per_cfg[k] = per_cfg.get(k, 0) + v
    cpu = sum(n * CPU_S_PER_CALL[k] for k, n in per_cfg.items())
    cpu += settle["C80_settle"] * CPU_S_PER_CALL["C80"]   # the 2x-STEPS call
    total_calls = sum(per_cfg.values()) + 1   # +1 physical FDTD call for settle
    wall = OVERHEAD_FACTOR * cpu / (N_WORKERS * PARALLEL_EFFICIENCY)
    return dict(sweep=sweep, pad=pad, article=article, beam=beam, mini=mini,
                settle=settle, per_config=per_cfg, total_calls=total_calls,
                cpu_s=cpu, wall_s=wall)


def main():
    print("=" * 78)
    print("exp-065 -- T24 ABSORB boundary sweep: geometry and desk arithmetic")
    print("=" * 78)

    print("\n[1] CONFIGURATIONS (congruence check)")
    hdr = ("cfg", "ABS", "PAD", "NX", "NY", "SRC_X", "PLANE_X", "OBJ_Y",
           "y_lo", "y_hi", "A", "aper", "clrPl", "clrSrc", "clrSpan", "D_SP")
    print("  " + " ".join(f"{h:>7}" for h in hdr))
    for k, c in CONFIGS.items():
        row = (k, c["absorb"], c["pad"], c["nx"], c["ny"], c["src_x"],
               c["plane_x"], c["obj_y"], c["y_lo"], c["y_hi"], c["A"],
               c["aperture_cells"], c["clear_plane"], c["clear_src"],
               c["clear_span_y"], c["d_sp"])
        print("  " + " ".join(f"{v:>7}" for v in row))
    cong = [CONFIGS[k] for k in CONGRUENT_KEYS]
    for field, want in (("A", 752), ("clear_plane", 37), ("clear_src", 20),
                        ("clear_span_y", 0), ("d_sp", 223), ("lever", 93),
                        ("aperture_cells", 1504)):
        vals = {c[field] for c in cong}
        assert vals == {want}, (field, vals, want)
        print(f"    congruent series holds {field:>15} = {want} across "
              f"ABSORB in (40, 60, 70, 80)  [OK]")
    print(f"    NAIVE N60 breaks it: A={CONFIGS['N60']['A']} "
          f"(-{752 - CONFIGS['N60']['A']} cells, "
          f"{100 * (752 - CONFIGS['N60']['A']) / 752:.2f}%), "
          f"clear_plane={CONFIGS['N60']['clear_plane']}, "
          f"aperture={CONFIGS['N60']['aperture_cells']}")

    print("\n[2] DESK PROPAGATOR (exp-048 `edge_diffraction_c_empty_corrected`,")
    print("    a boundary-FREE Huygens-Fresnel sum -- zero free parameters)")
    desk = {}
    for k in ("C40", "C60", "C70", "C80", "G40", "N60"):
        g = propagator_geom(CONFIGS[k])
        for lam, cpl in sorted(CPL.items()):
            for th in (35.0, 38.0, 40.0):
                desk[(k, lam, th)] = dg048.edge_diffraction_c_empty_corrected(
                    th, cpl, g)
    print("    lam  theta |        C40        C60        C70        C80"
          "        G40        N60 |  N60-C40")
    for lam in sorted(CPL):
        for th in (35.0, 38.0, 40.0):
            vals = [desk[(k, lam, th)]
                    for k in ("C40", "C60", "C70", "C80", "G40", "N60")]
            print(f"    {lam}  {th:4.0f}  | " +
                  " ".join(f"{v:+10.6f}" for v in vals) +
                  f" | {vals[5] - vals[0]:+9.6f}")
    dmax = max(abs(desk[(k, lam, th)] - desk[("C40", lam, th)])
               for k in ("C60", "C70", "C80") for lam in CPL for th in (35.0, 38.0, 40.0))
    print(f"\n    max |desk(C60/C70/C80) - desk(C40)| over all 12 cells = {dmax:.3e}")
    print("      -> the congruent series is EXACTLY degenerate in the")
    print("         boundary-free model: every FDTD difference C60/C80 vs C40")
    print("         is boundary physics by construction.")
    n60 = [abs(desk[("N60", lam, th)] - desk[("C40", lam, th)])
           for lam in CPL for th in (35.0, 38.0, 40.0)]
    print(f"    NAIVE artifact predicted by the SAME model, zero FDTD:")
    print(f"      |desk(N60) - desk(C40)|  min {min(n60):.3e}  "
          f"median {float(np.median(n60)):.3e}  max {max(n60):.3e}")
    print(f"      (compare T24's published beam-channel systematic "
          f"0.0022-0.0070 absolute)")
    print(f"    G40 (pad-only) vs C40 in the desk model: "
          f"{max(abs(desk[('G40', lam, th)] - desk[('C40', lam, th)]) for lam in CPL for th in (35.0, 38.0, 40.0)):.3e}")

    print("\n[3] T21 FRINGE PERIOD at each A (exp-048 `ripple_period_deg`)")
    for lam, cpl in sorted(CPL.items()):
        p752 = dg048.ripple_period_deg(752, cpl, 40.0)
        p732 = dg048.ripple_period_deg(732, cpl, 40.0)
        # fringe phase in cycles accumulated at theta=40 for each aperture
        cyc752 = 752 * np.sin(np.radians(40.0)) / cpl
        cyc732 = 732 * np.sin(np.radians(40.0)) / cpl
        print(f"    {lam}nm: P(A=752)={p752:.3f} deg  P(A=732)={p732:.3f} deg"
              f"   |delta phase| at theta=40 = {abs(cyc752 - cyc732):.3f} cycles")

    print("\n[1b] ALIASING CHECK (Phase-3 fix 1 / Red Team attack 1, "
          "PHOTONICS' catch)")
    print("    ABSORB / cpl at each (absorb, lambda) -- an exact integer "
          "means that leg")
    print("    sits on a resonant boundary-electrical-thickness point:")
    for absorb in (40, 60, 70, 80):
        row = " ".join(
            f"{lam}nm={absorb / cpl:6.3f}" for lam, cpl in sorted(CPL.items()))
        flags = [f"{lam}" for lam, cpl in sorted(CPL.items())
                 if float(absorb / cpl).is_integer()]
        print(f"    ABSORB={absorb:3d}:  {row}" +
              (f"   <-- INTEGER at {','.join(flags)}nm" if flags else ""))
    print("    -> C40/C60/C80 are ALL integer at 600nm (2/3/4 lambda) -- the")
    print("       one wavelength Block ARTICLE scores. C70 (added this Phase-3")
    print("       fix) is non-integer at all three: 70/15=4.667, 70/20=3.5, "
          "70/25=2.8.")
    integer_at_600 = [a for a in (40, 60, 70, 80) if float(a / CPL[600]).is_integer()]
    assert integer_at_600 == [40, 60, 80], (
        "sanity: exactly 40/60/80 (not 70) should be integer at 600nm",
        integer_at_600)

    print("\n[4] CAUSAL-IDENTITY GATE STEP (pad construction, C40 vs G40)")
    n_causal = causal_identity_step(CONFIGS["C40"], CONFIGS["G40"])
    s = COURANT_FRAC / np.sqrt(2.0)
    print(f"    Courant S = {s:.6f} cells/step (PHYSICAL wavefront speed only)")
    print(f"    first-arrival step at the plane (direct, D_SP={D_SP}) = "
          f"{int(np.ceil(D_SP / s))}")
    n_causal_old = causal_identity_step(CONFIGS["C40"], CONFIGS["G40"], _speed=s)
    n_arrival = int(np.ceil(D_SP / s))
    print(f"    guaranteed-identical up to step n = {n_causal}  "
          f"(Phase-3 fix 2: derived at 1 cell/step, the stencil's TRUE")
    print(f"    numerical domain of dependence -- NOT at S. Old, over-stated "
          f"bound (EM's catch) would have been n = {n_causal_old} "
          f"({100 * (n_causal_old - n_causal) / n_causal:.1f}% too generous).")
    print(f"\n    *** THE CORRECTED BOUND KILLS THE DYNAMIC GATE. ***")
    print(f"    Corrected causal bound n = {n_causal}; direct source->plane "
          f"arrival = {n_arrival}.")
    print(f"    {n_causal} < {n_arrival}: there is NO window in which real "
          f"signal has reached the")
    print(f"    plane AND the boundary-difference region provably cannot have. "
          f"The dynamic")
    print(f"    field-snapshot gate (P-VIS42-1b as originally written) is "
          f"VOID at this")
    print(f"    geometry -- and was only ever 'valid' under the overstated "
          f"n=359 bound.")
    print(f"    Caught at the DESK stage, zero FDTD cost, per the proposal's "
          f"own halt")
    print(f"    condition. G-2 is REPLACED by a strictly stronger static "
          f"check (below).")

    print("\n[4b] G-2 REPLACEMENT — STATIC CONSTRUCTION IDENTITY "
          "(zero FDTD steps)")
    sci = static_construction_identity(CONFIGS["C40"], CONFIGS["G40"], pad=40)
    print(f"    Sim.__init__ alone builds damp_e/damp_hx/damp_hy; compared "
          f"bit-for-bit at")
    print(f"    the SCORED window cells (obj, flank_lo, flank_hi) on the "
          f"observation plane,")
    print(f"    C40 vs G40 offset by pad=40:")
    for k, v in sorted(sci["by_window"].items()):
        print(f"      {k:<20} max|diff| = {v:.3e}")
    print(f"    max over all = {sci['max_diff']:.3e}  "
          f"(scored window is pure vacuum: {sci['all_vacuum']})")
    assert sci["max_diff"] == 0.0, "static construction identity FAILED"
    assert sci["all_vacuum"], "scored window is not vacuum"
    print(f"    -> holds at EVERY time step, not merely before a causal "
          f"horizon. Strictly")
    print(f"       stronger than the gate it replaces, and it actually has a "
          f"valid domain.")

    print("\n[5] FROZEN PERCEPTUAL BARS (invoked from lab/glare_sidecar.py)")
    print(f"    C_thr lab   (cued,   L=3 cd/m2, p=0.4) = {C_THR_LAB:.6f}")
    print(f"    C_thr field (uncued, L=3 cd/m2, p=0.4) = {C_THR_FIELD:.6f}")
    print(f"    MARGINAL band convention = [{MARGINAL_LO}, {MARGINAL_HI}] x bar")
    for L in (1e-1, 1e-2, 1e-3, 1e-4):
        lo = gs.c_thr(L, 0.4, bar="lab")
        hi = gs.c_thr(L, 0.5, bar="lab")
        print(f"    C_thr(L={L:g} cd/m2, lab) = {lo:.4f} (p=0.4) .. "
              f"{hi:.4f} (p=0.5)")
    print(f"    INSTRUMENT-FLOOR gate (scores every empty row): "
          f"GATE_HARD = {GATE_HARD}")

    print("\n[6] ARTICLE (Block ARTICLE)")
    print(f"    off_pass-equivalent uniform disk: tau_center = {TAU_OFF_PASS}, "
          f"r_out = {R_OUT} -> sigma_e = {SIGMA_OFF_PASS!r}")
    print(f"    descriptive-only central estimate (Phase-3 fix 5, code-"
          f"produced, NOT scored):")
    print(f"      g={G_TRANSFER} * tau={TAU_OFF_PASS} = "
          f"{ARTICLE_CENTRAL_ESTIMATE:.5f}")
    for line in (REALIZABILITY_MEMO_CAVEAT, G_TRANSFER_T15_CAVEAT,
                 T5_THERMAL_CAVEAT):
        print(f"      caveat: {line}")

    print("\n[7] FDTD BUDGET")
    b = fdtd_budget()
    for name in ("sweep", "pad", "article", "beam", "mini", "settle"):
        print(f"    Block {name.upper():<8} {b[name]}")
    print(f"    per-configuration totals: {b['per_config']}")
    print(f"    TOTAL FDTD calls = {b['total_calls']}")
    print(f"    measured cost basis (4-way parallel, this container): "
          f"{CPU_S_PER_CALL}")
    print(f"    projected CPU  = {b['cpu_s']:.0f} s = {b['cpu_s'] / 60:.1f} min")
    print(f"    projected WALL = {b['wall_s']:.0f} s = {b['wall_s'] / 60:.1f} min "
          f"({N_WORKERS} workers at {PARALLEL_EFFICIENCY:.0%} efficiency)")
    print(f"    3x safety envelope = {3 * b['wall_s'] / 60:.1f} min")

    print("\n[8] T24's PUBLISHED BEAM-CHANNEL NUMBERS (Block BEAM must reproduce)")
    for k, v in T24_BEAM.items():
        rel = abs(v["delta"]) / abs(v["fdtd_C_absorb40"])
        print(f"    {k}: {v['lambda_nm']}nm theta0={v['theta0_deg']} "
              f"FWHM={v['fwhm_deg']}  C(40)={v['fdtd_C_absorb40']:+.6f}  "
              f"C(60)={v['fdtd_C_absorb60']:+.6f}  dC={v['delta']:+.5f}  "
              f"|dC|/|C| = {rel:.4f}")
    print("    -> T24's systematic is 1.8-4.5% RELATIVE on the beam channel.")
    print("       Whether it transfers to the plane/ambient channel as an")
    print("       ABSOLUTE 0.002-0.007 or as a RELATIVE 2-5% is exactly what")
    print("       this cycle measures -- and the two hypotheses differ by")
    print("       ~30x on a |C_empty| ~ 0.01 row.")


if __name__ == "__main__":
    main()
