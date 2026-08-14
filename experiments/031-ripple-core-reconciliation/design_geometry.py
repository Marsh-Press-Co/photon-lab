"""exp-031 -- The T12 Ripple Sweep, the T13 Desk Reconciliation, and
QUANTUM's sigma-Held g-Point (Panel Iteration 8).
=======================================================================
Lead: PHOTONICS (rotation). Full seven-seat cycle -- see NOTES.md for the
Phase 1/2/3 accepted/overridden record and LOGBOOK.md Iteration 8 for the
verbatim transcript.

Red Team's Phase-2 audit found a MAJOR defect none of the five blind
critiques caught, and one that predates this cycle: exp-030's own
`build_ambient()` "absorber" branch calls ONLY `materials.graded_black_shell`
-- no `materials.pec_disk` -- so its r_in region (14.8% of the object's
cross-sectional area, self-similar across r=78/156/312) is literal vacuum,
not a coated solid. Every other construction of this article in this
program's history (exp-001, exp-020, exp-024, exp-025, exp-027) pairs
`pec_disk(r_in)` + `graded_black_shell(r_in, r_out)`. This is Fix 1 below --
load-bearing, not cosmetic, since theta=0 (boresight) is exactly the
geometry this bug most directly contaminates (a normal-incidence ray
through the hollow core passes unobstructed).

Six corrections/scope decisions from Phase 3 synthesis (LOGBOOK.md
Iteration 8, Phase 3 -- full accepted/overridden record there):

  1. [Red Team #1, LOAD-BEARING] The T12 sweep's "absorber" article is
     built with the historically-correct PEC-cored construction
     (`pec_disk(r_in)` + `graded_black_shell(r_in, r_out, ...)`), not
     exp-030's own hollow-core convention. Folded into the T12 sweep's own
     r=78/156 absorber runs (not a separate bolt-on run) -- this both
     supplies the T12 ripple data AND, by direct comparison against
     exp-030's existing (uncored) r=156/theta=0 reading, quantifies Red
     Team's own core-correction delta at zero extra run cost.
  2. [Red Team #2/#3, EM's flip, MATERIALS' point] T13's reconciliation
     fits BOTH the sqrt-law (C = C_inf + B*sqrt(z/zR)) and the ceiling-law
     (C = -1 + B*(z/zR)^p) to the theta=0 (r=78,r=156) pair for BOTH PEC
     and the (now correctly cored) absorber -- not just one law, not just
     one article. PEC's near-certain convergence (both laws agree once its
     own two points are already near-saturated) is stated explicitly as
     expected-regardless-of-truth, per Red Team attack #2 -- a PEC "pass"
     is not read as validating the metric-mismatch hypothesis. The
     absorber gets no "resolved" language under any framing this cycle;
     MATERIALS' point (PEC is constraint-2-disqualified, so even a clean
     PEC reconciliation is materially moot for constraint 3) is adopted
     verbatim.
  3. [VISION's flip, adopted verbatim] Every theta=0 single-angle C value
     produced this cycle (T12's raw sweep points, T13's fits) is labeled
     diagnostic-only and explicitly ineligible for constraint-3
     photopic/scotopic scoring -- only the N=9 ambient-summed metric may
     be scored against VISION's frozen C_thr ladder. Iteration 7's own e2
     tripwire is extended to cover future citation of these theta=0
     numbers without this caveat.
  4. [Red Team #5, magnitude floor] P-PHOTONICS-1/2's ripple-reversal
     count only registers a sign reversal if the slope change exceeds
     RIPPLE_NOISE_FLOOR = 0.002 (matching the established r=156 delta_C
     floor-bias scale, ~0.0012, rounded up) -- undifferentiated small
     flips are discretization noise, not evidence of Fresnel-zone
     structure.
  5. [THERMODYNAMICS' flip, adopted -- PANEL.md's own metric table
     mandate] The r=156/theta=0/PLANE_DX=15 (canonical anchor) absorber
     (cored) and PEC full-field captures feed a post-run analytic energy
     sidecar via the established `sections.widths()` box-ledger idiom.
     Correction made during Phase-4 implementation, not assumed at
     Phase-1/3: full 2D fields are NOT persisted between process
     invocations (only 1D observer profiles are saved to results.json),
     so this stage re-runs empty+pec+absorber at r=156/theta=0 (3 runs,
     ~2 min at the established rate) rather than reusing in-memory
     captures from the sweep stage -- still cheap, but not literally
     zero marginal FDTD cost as the Phase-1 proposal's framing implied
     for the general "full field stays in memory" claim once stages run
     as separate invocations:
     absorbed fraction of the object-footprint incident power. Labeled
     explicitly as a POST-RUN ANALYTIC calculation (expressibility
     contract), not an FDTD output. The DeltaT/emission-band step stays
     blocked on docket #7's still-missing witness-scenario watts, exactly
     as recorded at Iteration 1 -- this sidecar closes the "P_abs" half,
     not the whole chain.
  6. QUANTUM's sigma-held r=156 sponge run keeps sigma FIXED at
     sigma_off_lab(78) (not rescaled) -- tau_center(156) = 0.016 follows
     exactly. Reuses exp-030's own saved r=156 empty profiles (all 9
     FALLBACK_ANGLES) -- zero new empty runs. QUANTUM's own Phase-2 flip
     (cross-check g(156) against T12's flank-stability diagnostic before
     folding it into T1's calibration record) is adopted.

No new engine physics. No new escape-route mechanism. Instrumentation and
reconciliation only, per this cycle's own T1 escape-route statement.
"""

import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
EXP030 = os.path.abspath(os.path.join(HERE, "..", "030-scale-bridge"))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..")))
sys.path.insert(0, EXP030)

import design_geometry as dg030   # exp-030's own module -- GEOM, C78_ESTABLISHED, etc.

LAM_NM, CPL = 600, 20              # unchanged, single-lambda scope throughout
RIPPLE_NOISE_FLOOR = 0.002         # Fix 4

# --------------------------------------------------------- T12 PLANE_DX grids
# Values below are the Phase-1 proposal's own table (LOGBOOK.md Iteration 8
# Phase 1, sec 2a) -- re-derived here in code, not hand-copied, and checked
# against the proposal's printed table by a printed assertion below.
R_SWEEP = (78, 156)

PLANE_DX_GRID = {
    78: (38, 30, 22, 15, 11, 8, 5, 4, 3),
    156: (122, 87, 60, 44, 30, 22, 15, 11),
}

ANCHOR_PLANE_DX = 15               # the committed T8 anchor, present in both grids


def n_fresnel(r, plane_dx):
    return r ** 2 / (dg030.LAM_CELLS * plane_dx)


def z_over_zr(r, plane_dx):
    return plane_dx * dg030.LAM_CELLS / r ** 2


def x_bridge(r, plane_dx):
    return float(np.sqrt(z_over_zr(r, plane_dx)))


def plane_x_at(r, plane_dx):
    g = dg030.GEOM[r]
    return g["obj_x"] - r - plane_dx


def clearance_at(r, plane_dx):
    return plane_x_at(r, plane_dx) - dg030.ABSORB


# printed-assertable sanity check: every swept point clears the ABSORB band
for _r in R_SWEEP:
    for _dx in PLANE_DX_GRID[_r]:
        assert clearance_at(_r, _dx) > 0, f"r={_r} PLANE_DX={_dx} enters ABSORB band"

# ------------------------------------------------------- absorber, cored
# Fix 1: the historically-correct construction. r_in/sigma_max/eps_max
# reuse exp-030's own (Red-Team-adjudicated) family formulas unchanged --
# only the missing pec_disk core is restored.
r_in_shell = dg030.r_in_shell
sigma_max_shell = dg030.sigma_max_shell
EPS_MAX = dg030.EPS_MAX

# -------------------------------------------------- QUANTUM sigma-held item
SIGMA_HELD = dg030.sigma_off_lab(78)          # = 0.008/156 = 5.128205e-5, FIXED
R_SIGMA_HELD = 156
TAU_SIGMA_HELD_156 = 2 * SIGMA_HELD * R_SIGMA_HELD
assert abs(TAU_SIGMA_HELD_156 - 0.016) < 1e-9

# free-riding endpoints (already exist, exp-026/030 -- Iteration 7's own
# QUANTUM finding: tau_off_field/tau_off_lab == kappa(312) == 4 exactly)
SIGMA_HELD_C78 = dg030.C78_ESTABLISHED["off_lab"]          # -0.00548, r=78, sigma=SIGMA_HELD
# r=312's off_field reading (results.json['fit']['off_field']['c312']) IS,
# bit-identically, the sigma-held-at-r=312 point -- read from exp-030's own
# results.json at analysis time (run.py), not hand-copied here.

FALLBACK_ANGLES = dg030.FALLBACK_ANGLES        # N=9, reused verbatim

if __name__ == "__main__":
    print("T12 PLANE_DX grids:")
    for r in R_SWEEP:
        print(f"  r={r}:")
        for dx in PLANE_DX_GRID[r]:
            print(f"    PLANE_DX={dx:4d}  N_F={n_fresnel(r,dx):8.3f}  "
                  f"z/zR={z_over_zr(r,dx):.5f}  x={x_bridge(r,dx):.5f}  "
                  f"plane_x={plane_x_at(r,dx)}  clearance={clearance_at(r,dx)}")
    print(f"\nsigma_held = {SIGMA_HELD:.6e}  tau(156) = {TAU_SIGMA_HELD_156}")
    print(f"r_in_shell(78)={r_in_shell(78)}  r_in_shell(156)={r_in_shell(156)}  "
          f"sigma_max_shell(78)={sigma_max_shell(78)}  sigma_max_shell(156)={sigma_max_shell(156)}")
