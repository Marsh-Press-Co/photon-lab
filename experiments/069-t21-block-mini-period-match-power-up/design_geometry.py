"""exp-069 design constants -- Block MINI's period-match test (P-VIS42-10),
powered up to the mandate PLAN.md's Iteration-46 queue LOCKED, unconditional:
"Either build the properly-powered FDTD version (>=2-3 T21 periods at ~0.2deg
spacing, settled STEPS>=2800, desk-first...) or formally retire the test with
a stated reason -- no further relabeling, no further citation-tripwire-only
treatment."

Panel Iteration 46 (lead: THERMODYNAMICS, by rotation). Phase 1 proposal
(fresh sub-agent) + five blind Phase-2 critiques + Red Team's Phase-2 audit
(PROCEED-WITH-MANDATORY-FIXES, 10 items) -- full record in phase1_proposal.md,
phase2_critique_{photonics,materials,em,quantum,vision}.md,
phase2_redteam_audit.md. This file implements the Phase-3 SYNTHESIS (Director)
applying all 10 mandatory fixes -- every number quoted in NOTES.md is produced
by running `python3 design_geometry.py`, never hand-typed (house rule R4).

WHAT THIS FIXES (P-VIS42-10, exp-065, three defects):
  1. Sparse sampling: 5 points/0.5deg step over ~1.0 T21 period ->
     31 points/0.2deg step over ~3.0 T21 periods (Block DENSE).
  2. Unsettled STEPS: 1400 -> settled 2800 (Block DENSE), plus a new
     STEPS=4200 stress cell closing the one remaining gap in T27's own
     C80 settling evidence (Block SETTLE-C80).
  3. Never-coded period-match clause: Sec-4's fixed-period (T=cpl/A, zero
     free period parameters) sinusoid fit in sin(theta), scored by R^2
     against a flat null (P-069-2), PLUS a free-period cross-check
     (P-069-3) -- promoted from diagnostic-only to CO-GATING per Red
     Team's Phase-2 audit (mandatory fix 3).

MANDATORY FIXES APPLIED HERE / in NOTES.md (phase2_redteam_audit.md's 10-item
docket, all ADOPTED, zero overridden -- see phase3_synthesis.md):
  1. P-069-4 wired as a BINDING precondition on the Combined Verdict, not an
     independent side-row.
  2. Sec-4's epistemic framing corrected: Delta(sin theta)=cpl/A tests
     CONSISTENCY with T21's established stationary-phase-limit model
     (R^2=0.7852->0.8271 at its own best fit, never 1.0), not an
     independently-verified exact period.
  3. Combined Verdict restructured into ONE fully-corroborated gate: ALL of
     P-069-1 REFUTE, P-069-2 REFUTE, P-069-3 within tolerance, P-069-4
     CONFIRM, AND the new R3 legs (fix 5) survive resolution refinement.
  4. A pre-committed non-decisive-outcome rule: anything short of full
     corroboration on the combined gate is NOT reported as PARTIAL-and-
     deferred -- it is immediate formal retirement of the period-match
     test, stated reason recorded verbatim in NOTES.md/phase4_results.md.
  5. A minimal R3 (resolution) check: Block R3, the two Block SETTLE-C80
     cells (39.0, 40.0 deg, 600nm) rerun at cpl=30, BOTH configs (C40 and
     C80 -- Red Team's "if budget allows" upgraded to done, not minimum).
  6. Idealization #2 corrected: all three established lambda sample BELOW
     Nyquist for their own fringe period at 1deg step
     (samples_per_period = 0.50/0.67/0.40 at 600/450/750nm); 600nm's
     flip_fraction=1.0 in the desk check is the SIGNATURE of near-Nyquist
     aliasing, not evidence of clean resolution -- the justification for
     600nm-primary scope is now "matches P-VIS42-10's own original scope",
     not "least aliased".
  7. A bounded 750nm confirmatory sub-sweep added: Block LEG750, theta in
     [38.0, 41.0]deg at 0.2deg step (16 points), both configs, STEPS=2800 --
     closes the one-wavelength generalization gap (750nm carries T21's own
     largest established fringe amplitude, c*=3.23 vs 600nm's 2.74,
     exp-042).
  8. Sec-1 misattribution corrected: the 59.8%/74.4% settling figures both
     belong to exp-065 (its own P-VIS42-11 C80 point / C40 four-point
     convergence trend), NOT exp-066 (which tested ONLY C40, never C80 --
     `experiments/066-.../NOTES.md` Setup: "exp-041/exp-065's C40 config,
     unchanged").
  9. R_contact disclosure: PLAN.md's Iteration-46 queue item #2 remains
     untouched this cycle -- still blocked on WebSearch/WebFetch tooling,
     not picked up in parallel despite PLAN.md's explicit invitation to do
     so if capacity allows. Stated once, here and in NOTES.md, not silently
     dropped.
  10. P-069-1 reports raw ptp and mean alongside the ratio (closes an
      interpretability gap on the cycle's own headline statistic).

Pure geometry + desk arithmetic -- NO FDTD in this file.
"""

import importlib.util
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, ROOT)


def _load_exp065():
    """exp-065's own design_geometry module -- reused VERBATIM (CONFIGS,
    CPL, GATE_HARD, the congruent-construction machinery). Loaded explicitly
    under a distinct name; a plain `import design_geometry` would collide
    with THIS file."""
    path = os.path.abspath(os.path.join(
        HERE, "..", "065-t24-absorb-boundary-sweep", "design_geometry.py"))
    spec = importlib.util.spec_from_file_location("_exp065_design_geometry", path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["_exp065_design_geometry"] = mod
    spec.loader.exec_module(mod)
    return mod


dg065 = _load_exp065()
from lab.fdtd2d import Sim as _Sim   # noqa: E402  (for the R3 config's static array, none needed here)

CONFIGS = dg065.CONFIGS          # C40, C60, C70, C80, G40, N60 -- reused verbatim
CPL = dg065.CPL                  # {450:15, 600:20, 750:25}
GATE_HARD = dg065.GATE_HARD
COURANT_FRAC = dg065.COURANT_FRAC
TAPER = dg065.TAPER
R_OUT = dg065.R_OUT
W_OBJ = dg065.W_OBJ
GUARD_OUT = dg065.GUARD_OUT
W_FLANK = dg065.W_FLANK
A_HALF_APERTURE = 752   # dg065.CONFIGS["C40"]["A"] -- verified equal below

assert CONFIGS["C40"]["A"] == A_HALF_APERTURE == CONFIGS["C80"]["A"], \
    "congruent construction: A must be held fixed across C40/C80"

STEPS_NATIVE = 1400
STEPS_SETTLED = 2800      # this cycle's OWN floor -- T27's own established
                           # settled point (exp-066), NOT 1400
STEPS_STRESS = 4200       # Block SETTLE-C80 -- closes T27's C80 gap

# --------------------------------------------- T21's own established period
def P_deg(theta_deg, lambda_nm, A=A_HALF_APERTURE):
    """T21's established fringe period (Iteration 18/19, exp-041/042):
    the full coherent Huygens-Fresnel aperture-integral model's own
    stationary-phase limit. Fit to real FDTD data at R^2=0.7852 (Iteration
    19) -> 0.8271 (Iteration 43's settled refit) -- NEVER 1.0. This is a
    MODEL under test, not ground truth (mandatory fix 2)."""
    cpl = CPL[lambda_nm]
    return math.degrees(cpl / (A * math.cos(math.radians(theta_deg))))


# T=cpl/A is the exact period of d(sin theta) that reduces to P(theta) as its
# own local (first-derivative) approximation -- a strictly more constrained
# form of the SAME model under test, not independent verification of it
# (mandatory fix 2's corrected framing).
T_SINTHETA_600 = CPL[600] / A_HALF_APERTURE   # 20/752 = 0.026595744...

# --------------------------------------------------------- Block DENSE (600nm)
DENSE_CENTER = 39.0
DENSE_HALF_SPAN = 3.0
DENSE_STEP = 0.2
DENSE_ANGLES = tuple(round(DENSE_CENTER + i * DENSE_STEP, 4)
                      for i in range(-int(round(DENSE_HALF_SPAN / DENSE_STEP)),
                                      int(round(DENSE_HALF_SPAN / DENSE_STEP)) + 1))
assert len(DENSE_ANGLES) == 31
assert DENSE_ANGLES[0] == 36.0 and DENSE_ANGLES[-1] == 42.0
DENSE_SPAN_DEG = DENSE_ANGLES[-1] - DENSE_ANGLES[0]
DENSE_N_PERIODS = DENSE_SPAN_DEG / P_deg(DENSE_CENTER, 600)

# ---------------------------------------------------- Block LEG750 (750nm)
LEG750_LO, LEG750_HI, LEG750_STEP = 38.0, 41.0, 0.2
LEG750_ANGLES = tuple(round(LEG750_LO + i * LEG750_STEP, 4)
                       for i in range(int(round((LEG750_HI - LEG750_LO) / LEG750_STEP)) + 1))
assert len(LEG750_ANGLES) == 16
assert LEG750_ANGLES[0] == 38.0 and LEG750_ANGLES[-1] == 41.0

# ---------------------------------------------- Block SETTLE-C80 (600nm)
SETTLE_ANGLES = (39.0, 40.0)   # already earmarked in exp-065's own block_mini
                                # (STEPS=1400) -- closes the gap at zero extra
                                # design cost

# --------------------------------------------------- Block R3 (resolution)
# Mandatory fix 5: mirrors exp-033's own established R3 rescale idiom
# (cpl 20 -> 30, every cell constant scaled x1.5, geometry held fixed in
# PHYSICAL units, STEPS scaled x1.5 to hold the same optical dwell). Ratio
# and rounding match exp-033's own precedent exactly (independently
# reproduced: PLANE_X 77*1.5=115.5 -> 116, GUARD_OUT 185*1.5=277.5 -> 278,
# both round-half-up, both bit-identical to exp-033's own committed
# constants).
R3_RATIO = 1.5
R3_CPL = {600: 30}
R3_BASE_NX = round(360 * R3_RATIO)          # 540
R3_BASE_NY = round(1584 * R3_RATIO)         # 2376
R3_BASE_ABSORB = round(40 * R3_RATIO)       # 60
R3_BASE_SRC_X = round(300 * R3_RATIO)       # 450
R3_BASE_PLANE_X = round(77 * R3_RATIO)      # 116 (77*1.5=115.5, round-half-up)
R3_BASE_OBJ_X = round(170 * R3_RATIO)       # 255
R3_BASE_OBJ_Y = R3_BASE_NY // 2             # 1188
R3_TAPER = round(TAPER * R3_RATIO)          # 60
R3_R_OUT = round(R_OUT * R3_RATIO)          # 117
R3_W_OBJ = round(W_OBJ * R3_RATIO)          # 117
R3_GUARD_OUT = round(GUARD_OUT * R3_RATIO)  # 278 (185*1.5=277.5, round-half-up)
R3_W_FLANK = round(W_FLANK * R3_RATIO)      # 117
R3_STEPS = round(STEPS_SETTLED * R3_RATIO)  # 4200 -- the settled-equivalent
                                             # floor at cpl=30 (coincides
                                             # numerically with STEPS_STRESS,
                                             # a different quantity at native
                                             # cpl -- disclosed, not conflated)


def r3_config(absorb, pad):
    """R3-rescaled congruent config, mirroring dg065.config()'s own
    construction exactly (source span passed explicitly, A held fixed in
    CELLS at the rescaled resolution -- i.e. A_r3 = 1.5 * A_native by
    construction, matching the physical aperture)."""
    nx = R3_BASE_NX + 2 * pad
    ny = R3_BASE_NY + 2 * pad
    src_x = R3_BASE_SRC_X + pad
    plane_x = R3_BASE_PLANE_X + pad
    obj_x = R3_BASE_OBJ_X + pad
    obj_y = R3_BASE_OBJ_Y + pad
    y_lo = R3_BASE_ABSORB + pad
    y_hi = ny - y_lo
    return dict(
        naive=False, absorb=absorb, pad=pad, nx=nx, ny=ny,
        src_x=src_x, plane_x=plane_x, obj_x=obj_x, obj_y=obj_y,
        y_lo=y_lo, y_hi=y_hi, A=obj_y - y_lo, aperture_cells=y_hi - y_lo,
        cells=nx * ny,
    )


R3_CONFIGS = {
    "C40_R3": r3_config(60, 0),      # ABSORB scales too: 40*1.5=60
    "C80_R3": r3_config(120, 60),    # 80*1.5=120, pad 40*1.5=60
    "G40_R3": r3_config(60, 60),     # R3 scaling of native G40=config(40,40): absorb 40->60, pad 40->60
}
assert R3_CONFIGS["C40_R3"]["A"] == R3_CONFIGS["C80_R3"]["A"] == R3_CONFIGS["G40_R3"]["A"] == \
    round(A_HALF_APERTURE * R3_RATIO), \
    f"R3 congruent construction: A must scale by exactly R3_RATIO ({A_HALF_APERTURE*R3_RATIO})"

# ------------------------------------------------------------- cost basis
# Reused verbatim from dg065.CPU_S_PER_CALL (measured on the SAME container,
# same shift -- 4-worker ProcessPoolExecutor contention included, linear-in-
# STEPS scaling, independently corroborated by exp-066's own block_g1ext
# (1400) vs block_main2800 (2800) wall-clock ratio, 2.02x vs assumed 2.00x).
CPU_S_PER_CALL_1400 = dg065.CPU_S_PER_CALL   # {"C40":25.0, "C80":34.8, ...}


def _cost(cfg_key, steps, cell_ratio=1.0):
    base = CPU_S_PER_CALL_1400[cfg_key]
    return base * (steps / STEPS_NATIVE) * cell_ratio


def fdtd_budget():
    """Call counts and wall-clock, block by block. No leg double-counted."""
    n_dense = len(DENSE_ANGLES)
    n_leg750 = len(LEG750_ANGLES)
    n_settle = len(SETTLE_ANGLES)

    # Block DENSE: 31 theta x {C40,C80} x 600nm x STEPS=2800
    dense_calls = n_dense * 2
    dense_cpu = n_dense * (_cost("C40", STEPS_SETTLED) + _cost("C80", STEPS_SETTLED))

    # Block SETTLE-C80: 2 theta x C80 x 600nm x STEPS=4200
    settle_calls = n_settle
    settle_cpu = n_settle * _cost("C80", STEPS_STRESS)

    # Block R3: 2 theta x {C40_R3,C80_R3} x 600nm x cpl=30 x STEPS=4200(r3)
    # cell_ratio = (1.5)^2 = 2.25 (both nx and ny scale by RATIO)
    r3_calls = n_settle * 2
    r3_cell_ratio = R3_RATIO ** 2
    r3_cpu = n_settle * (_cost("C40", R3_STEPS, r3_cell_ratio)
                          + _cost("C80", R3_STEPS, r3_cell_ratio))

    # Block LEG750: 16 theta x {C40,C80} x 750nm x STEPS=2800 (same cell
    # count as 600nm -- lambda does not change NX/NY, only cells_per_lambda)
    leg750_calls = n_leg750 * 2
    leg750_cpu = n_leg750 * (_cost("C40", STEPS_SETTLED) + _cost("C80", STEPS_SETTLED))

    total_calls = dense_calls + settle_calls + r3_calls + leg750_calls
    total_cpu = dense_cpu + settle_cpu + r3_cpu + leg750_cpu

    overhead_factor = 1.15
    n_workers = 4
    parallel_efficiency = 0.98
    wall_s = overhead_factor * total_cpu / (n_workers * parallel_efficiency)

    return dict(
        dense=dict(calls=dense_calls, cpu_s=dense_cpu),
        settle=dict(calls=settle_calls, cpu_s=settle_cpu),
        r3=dict(calls=r3_calls, cpu_s=r3_cpu),
        leg750=dict(calls=leg750_calls, cpu_s=leg750_cpu),
        total_calls=total_calls, total_cpu_s=total_cpu, wall_s=wall_s,
        wall_min=wall_s / 60.0, envelope3x_min=3 * wall_s / 60.0,
    )


if __name__ == "__main__":
    b = fdtd_budget()
    print(f"A_HALF_APERTURE = {A_HALF_APERTURE}")
    print(f"P(39deg, 600nm) = {P_deg(39.0, 600):.4f} deg")
    print(f"P(40deg, 600nm) = {P_deg(40.0, 600):.4f} deg  "
          f"(established anchor: 1.989)")
    print(f"P(39deg, 750nm) = {P_deg(39.0, 750):.4f} deg")
    print(f"T_SINTHETA_600 = {T_SINTHETA_600:.9f}")
    print(f"DENSE_ANGLES ({len(DENSE_ANGLES)} points): "
          f"{DENSE_ANGLES[0]}..{DENSE_ANGLES[-1]} step {DENSE_STEP}")
    print(f"DENSE_SPAN_DEG = {DENSE_SPAN_DEG:.2f}  "
          f"N_PERIODS(at center) = {DENSE_N_PERIODS:.3f}")
    print(f"LEG750_ANGLES ({len(LEG750_ANGLES)} points): "
          f"{LEG750_ANGLES[0]}..{LEG750_ANGLES[-1]} step {LEG750_STEP}")
    print(f"R3_CONFIGS: C40_R3 A={R3_CONFIGS['C40_R3']['A']} "
          f"nx={R3_CONFIGS['C40_R3']['nx']} ny={R3_CONFIGS['C40_R3']['ny']}")
    print(f"R3_CONFIGS: C80_R3 A={R3_CONFIGS['C80_R3']['A']} "
          f"nx={R3_CONFIGS['C80_R3']['nx']} ny={R3_CONFIGS['C80_R3']['ny']}")
    print()
    for k, v in b.items():
        if isinstance(v, dict):
            print(f"  {k}: calls={v['calls']}  cpu_s={v['cpu_s']:.1f}")
    print(f"  TOTAL calls = {b['total_calls']}")
    print(f"  TOTAL cpu_s = {b['total_cpu_s']:.1f}")
    print(f"  wall = {b['wall_min']:.2f} min")
    print(f"  3x envelope = {b['envelope3x_min']:.2f} min")
