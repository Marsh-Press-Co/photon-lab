"""exp-052 design constants -- The Fixed-Absolute-Thickness `graded_black_shell`
Variant's Own Ambient-Contrast C (T13/T14 test).
=======================================================================
Panel Iteration 29 (lead: THERMODYNAMICS, rotation) -- executes PLAN.md's
LOCKED, UNCONDITIONAL Iteration-29 trigger (MATERIALS' own idea, first
queued Iteration 7; re-ranked without being reached at Iterations 25-28,
a 21-iteration deferral; granted unconditional status by Red Team at
Iteration 28 Phase 2, re-verified intact at Phase 5).

Domain-construction geometry (`geometry()`, below) is reused VERBATIM from
`experiments/030-scale-bridge/design_geometry.py` -- same PLANE_DX, ABSORB,
TAPER, MARGIN_MULT, N9 fallback angle set, NX/NY/OBJ/PLANE_X/D_SP/STEPS
formulas. Only the object's material law inside the object window differs,
by design -- this isolates the geometric-law question (self-similar
r_in vs. fixed-absolute r_in) from any domain-construction confound.

Phase-2/Red-Team mandatory-fix docket (LOGBOOK.md Iteration 29, full
transcript in this dir's phase*.md files) accepted in full at Phase 3:

  1. [ELECTROMAGNETISM #1, Red Team-verified LOAD-BEARING] Both the new
     fixed-absolute object AND the self-similar comparator are built
     PEC-CORED (`materials.pec_disk(r_in)` then `materials.graded_black_shell`)
     -- exp-030's own `run.py::build_ambient` silently built the "absorber"
     article HOLLOW (no interior fill at all), a defect `experiments/
     031-ripple-core-reconciliation` diagnosed and fixed for its own
     theta=0 diagnostic but never propagated back into exp-030's own
     committed results.json -- exactly the file exp-052's Phase-1 proposal
     drew its self-similar comparator numbers from.
  2. [Red Team, new finding at Phase 2] The self-similar comparator at
     r=156 (and r=312 if run) is therefore RE-MEASURED here, PEC-cored, at
     the full N9-ambient instrument -- not merely inherited from exp-030's
     own hollow-core results.json. This closes the "uncorrected comparator"
     gap on BOTH sides of every P-1/P-2 delta, not just the new object's
     side.
  3. [Red Team, new finding, moderate cost] A radial absorbed-power ledger
     check (`sections.radial_absorbed_power`, exp-028's own validated
     instrument) runs on the fixed-absolute PEC-cored object at every r in
     scope, confirming (or refuting) whether T9's established "core is
     energetically incidental" null (Delta sigma_abs/sigma_ext=1.56e-6,
     measured ONLY at r_in/r_out=0.385) survives at the much larger ratios
     this construction reaches (0.692 at r=156, 0.846 at r=312) -- no prior
     experiment in this program has built an object above ratio 0.385.
  4. [Red Team #6b, cosmetic-but-must-fix, R4 house rule] The Phase-1
     proposal's own C78 citation (-0.7211) does not match the actual
     `experiments/030-scale-bridge/design_geometry.py::C78_ESTABLISHED`
     value (-0.7208684660449545, rounds to -0.7209) -- corrected here,
     re-derived from the SAME module rather than hand-copied a second time.
  5. [PHOTONICS #1, scope fix] P-3's T14 verdict is explicitly scoped to
     600nm ONLY -- the mechanism argument (thickness-in-wavelengths) is
     itself wavelength-dependent (1.92lambda-3.2lambda across this
     program's 3lambda sweep at fixed 1.44um), so a single-lambda result
     cannot license a program-general claim. No new-lambda run added this
     cycle (cost discipline); the scope restriction is stated explicitly
     in NOTES.md instead, per Red Team's own offered alternative.
  6. [MATERIALS #1, desk-only] Sec. 9's realizability note is extended with
     the implied absorption e-folding length (tau_shell/thickness =
     24/1440nm = 1/60nm) -- computed here, not asserted -- so the
     PLAUSIBLE-not-PUBLISHED claim is stated honestly as thickness-only,
     absorptivity unchecked (no primary CNT-forest absorption-coefficient
     citation exists in this program yet; T18's WebFetch block is the
     reason, unaddressed this cycle).
  7. [QUANTUM #1, Director scope call -- NOT re-measured this cycle] The
     coherent-vs-incoherent ambient-sum bridge gate (exp-029's stage-11
     idiom) was only ever empirically validated at shell-fraction 61.5%
     (r=78-native, where fixed-absolute and self-similar coincide). This
     cycle's own r=156 result sits at shell-fraction 30.8%, untested.
     Director's call: re-implementing exp-029's bespoke beam-scene cross-
     term measurement for a NEW ambient-scene object is a nontrivial,
     error-prone undertaking under this shift's own time budget -- deferred
     explicitly, disclosed as an open assumption (not silently assumed
     clean), with the physical argument for low risk stated in NOTES.md
     (the measured cross-term's smallness is a property of the N9 angular
     averaging / source geometry, which this cycle does not touch -- not
     obviously a function of the object's own shell thickness) and queued
     as a named Iteration-30+ follow-up.
  8. [VISION #1, band widened not re-measured] P-2's r=312 falsifiable
     band is widened to +/-0.0016 (>=2x T16's own measured r=156 angular-
     quadrature+domain-construction uncertainty budget, 7.80e-4) rather
     than running a new per-angle floor spot-check at r=312 -- Red Team's
     own offered cheaper alternative.
  9. [Red Team #7, disclosure-only] A clean R-gate pass bears on flat-wall
     normal-incidence reflectance ONLY -- stated explicitly in NOTES.md,
     does not license any inference about the core-fill/comparator
     questions above.

See NOTES.md for the full Phase 1/2/3 accepted record and LOGBOOK.md
Iteration 29 for the verbatim panel transcript.
"""

import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..")))
BRIDGE_DIR = os.path.abspath(os.path.join(HERE, "..", "030-scale-bridge"))
sys.path.insert(0, BRIDGE_DIR)
import design_geometry as dg30   # noqa: E402  -- exp-030's own module, reused verbatim for geometry()

# --------------------------------------------------------- the r-family
R_FAMILY = (78, 156, 312)
R_BASE = 78

# domain-construction constants: IDENTICAL to exp-030, imported not copied,
# so no transcription can drift them
PLANE_DX = dg30.PLANE_DX
ABSORB = dg30.ABSORB
TAPER = dg30.TAPER
MARGIN_MULT = dg30.MARGIN_MULT
COURANT_FRAC = dg30.COURANT_FRAC
FALLBACK_ANGLES = dg30.FALLBACK_ANGLES     # N9, +-35deg fallback -- this program's standard
LAM_NM, CPL = 600, 20                       # single-lambda scope (idealization, scoped explicitly)

GEOM = dg30.GEOM                            # geometry() is domain-only -- reused verbatim, unchanged


def kappa(r):
    return r / R_BASE


# ---------------------------------------------- fixed-absolute-thickness family
ABS_THICKNESS = 48                          # r=78-native thickness, HELD CONSTANT
SIGMA_MAX_FIXED = 0.5                       # r=78-gated value, HELD CONSTANT (not rescaled)
EPS_MAX = 1.0


def r_in_fixedabs(r):
    return r - ABS_THICKNESS


def sigma_max_fixedabs(r):
    return SIGMA_MAX_FIXED


# ---------------------------------------------------- self-similar family
# (exp-030's own formulas, imported not re-derived -- the comparator this
# cycle re-measures PEC-cored, not a new geometric law)
def r_in_selfsim(r):
    return dg30.r_in_shell(r)


def sigma_max_selfsim(r):
    return dg30.sigma_max_shell(r)


# printed assertions (house discipline)
for _r in R_FAMILY:
    _t_fixed = _r - r_in_fixedabs(_r)
    _tau_fixed = sigma_max_fixedabs(_r) * _t_fixed
    assert _t_fixed == ABS_THICKNESS, f"fixed-absolute thickness drifted at r={_r}"
    assert abs(_tau_fixed - 24.0) < 1e-9, f"fixed-absolute tau_shell drifted at r={_r}: {_tau_fixed}"
    _t_self = _r - r_in_selfsim(_r)
    _tau_self = sigma_max_selfsim(_r) * _t_self
    assert abs(_tau_self - 24.0) < 1e-9, f"self-similar tau_shell drifted at r={_r}: {_tau_self}"
assert r_in_fixedabs(78) == r_in_selfsim(78) == 30, "families must coincide at r=78"
assert sigma_max_fixedabs(78) == sigma_max_selfsim(78) == 0.5, "families must coincide at r=78"

# --------------------------------------------------- r=78 anchor (P-0 identity)
# Fix 4: re-derived from dg30's own module, not hand-copied a second time.
C78_ABSORBER_ESTABLISHED = dg30.C78_ESTABLISHED["absorber"]     # -0.7208684660449545

# ------------------------------------------------------- realizability (Sec 9/Fix 6)
DX_NM = 30.0                                # this bench's established dx @ 600nm/cpl20
THICKNESS_NM = ABS_THICKNESS * DX_NM        # 1440.0 nm = 1.44um
TAU_SHELL = 24.0
ALPHA_PER_NM = TAU_SHELL / THICKNESS_NM     # implied absorption e-folding rate
EFOLD_LENGTH_NM = 1.0 / ALPHA_PER_NM        # ~60nm

# ------------------------------------------------------- T16 band-widening (Fix 8)
T16_R156_BUDGET = 7.80e-4                   # LOGBOOK T16, Iteration 11/12
P2_R312_BAND = 2.0 * T16_R156_BUDGET        # 0.00156, widened per Red Team's offered alternative


def box_dev(sigma_ext_a, sigma_ext_b):
    """Established convention (T11), reused verbatim."""
    return abs(sigma_ext_a - sigma_ext_b) / abs(sigma_ext_a)


def main():
    print("exp-052 geometry (fixed-absolute-thickness graded_black_shell variant)\n")
    for r in R_FAMILY:
        g = GEOM[r]
        print(f"r_out={r:4d}  NX={g['nx']:5d} NY={g['ny']:5d}  OBJ={g['obj']}  "
              f"D_SP={g['d_sp']:5d}  STEPS={g['steps_ambient']:5d}")
    print("\nfixed-absolute family (r_in=r_out-48, sigma_max=0.5 fixed):")
    for r in R_FAMILY:
        t = r - r_in_fixedabs(r)
        print(f"  r={r:4d}  r_in={r_in_fixedabs(r):4d}  thickness={t:3d}  "
              f"frac_of_rout={t/r:.4f}  thickness_lambda={t/CPL:.3f}  "
              f"tau_shell={sigma_max_fixedabs(r)*t:.4f}")
    print("\nself-similar comparator family (r_in=round(30/78*r_out), sigma_max=0.5/kappa):")
    for r in R_FAMILY:
        t = r - r_in_selfsim(r)
        print(f"  r={r:4d}  r_in={r_in_selfsim(r):4d}  thickness={t:3d}  "
              f"frac_of_rout={t/r:.4f}  sigma_max={sigma_max_selfsim(r):.4f}  "
              f"tau_shell={sigma_max_selfsim(r)*t:.4f}")
    print(f"\nC78_ABSORBER_ESTABLISHED (re-derived from dg30, Fix 4): "
          f"{C78_ABSORBER_ESTABLISHED:.10f}  (rounds to {C78_ABSORBER_ESTABLISHED:+.4f})")
    print(f"\nrealizability (Fix 6): thickness={THICKNESS_NM:.1f}nm, "
          f"tau_shell={TAU_SHELL}, alpha={ALPHA_PER_NM:.6f}/nm, "
          f"e-fold length={EFOLD_LENGTH_NM:.2f}nm")
    print(f"\nP-2 r=312 band, widened (Fix 8): +/-{P2_R312_BAND:.5f}  "
          f"(2x T16's r=156 budget of {T16_R156_BUDGET:.2e})")
    print(f"\nratio r_in/r_out reached by fixed-absolute family (T9 generalization test):")
    for r in R_FAMILY:
        print(f"  r={r:4d}: {r_in_fixedabs(r)/r:.4f}  (T9's own established point: 0.3846)")


if __name__ == "__main__":
    main()
