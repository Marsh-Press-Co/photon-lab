"""exp-029 design constants -- The Coherent-Superposition Bridge Gate.
=======================================================================
Panel Iteration 6 (lead: QUANTUM OPTICS, rotation). Phase-3 synthesis
incorporates Red Team's mandatory-fix docket (LOGBOOK.md Iteration 6,
Phase 2) in full:

  1. [MATERIALS/Red Team #1, LOAD-BEARING] The bench object is exp-028's
     Cell B construction EXACTLY -- graded_black_shell(30,78,sigma_max=0.5,
     eps_max=1.0) PLUS the core-fill line sigma_e[rr<r_in]+=sigma_max --
     not the shell alone, which leaves r<30 an unfilled vacuum hole (an
     untested hollow-shell article, not T9's validated one). A printed
     non-vacuum assertion enforces this in run.py before any run is
     trusted.
  2. [EM/THERMODYNAMICS/Red Team #2] The coherent-interference informational
     metric (P-QUANTUM-7/8, Phase-1 proposal) is renormalized to
     |delta_P_int| / P_abs(object+beam), NOT P_abs(object+off_axis) -- the
     proposal's original denominator gave a band ([0%,30%]) that both EM
     and THERMODYNAMICS independently re-derived (Cauchy-Schwarz on the
     sigma_e-weighted inner product) is impossible: the true ceiling
     against that denominator is 2/sqrt(AMP_REL) = 141.4x = 14,142%.
     Renormalized against P_abs(beam), the ceiling is 2*sqrt(AMP_REL) =
     2.83% -- a physically bounded, interpretable band.
  3. [PHOTONICS/Red Team #3, inexpressible] `add_line_source()` has no
     `intensity_role`/`amp_rel` kwargs (checked against its actual
     signature, lab/fdtd2d.py) -- these are results.json MANIFEST fields
     (exp-028's own precedent), never passed into the source call itself.
  4. [Red Team #4, NEW catch -- none of the five blind critiques caught
     this] The off-axis source amplitude is DERIVED in code as
     sqrt(AMP_REL) at full float64 precision, not a hand-copied 6-decimal
     literal -- the Phase-1 proposal's own literal (0.014142) fails its
     OWN stated 1e-9 assert tolerance by 3.8x (the identical "derived
     value checked against a pre-rounded display number" bug class as
     Iteration 5's SIGMA_ON drift and the 55.47 peak-bin rounding).
  5. [VISION/Red Team #5] The second source's role label is "off_axis",
     NOT "ambient" -- this build does not touch lab/ambient.py, computes
     no Weber contrast, and does not reproduce C (constraint 3's metric).
     It explicitly DEFERS the beam+ambient-C-reproduction half of
     Iteration 1's own committed bridge-gate design (LOGBOOK.md docket
     #4/(b): "one joint beam+ambient run on the linear sponge reproducing
     beam-behind and C simultaneously") -- named as a deferred commitment,
     not described as merely "orthogonal" (Red Team's sharpening of
     VISION's own catch).
  6. [Red Team #6, recommended, folded in] A bin-wise radial-ledger
     superposition check (joint scene's bins vs beam-only-bins +
     off_axis-only-bins) is added as an informational P-QUANTUM-9,
     closing the spatial-redistribution gap Gate Q3 alone doesn't test --
     Ez-level equality (Gate Q2) does not imply p_J=0.5*sigma_e*|Ez|^2 is
     bin-wise additive, since p_J is QUADRATIC in Ez.

See NOTES.md for the full Phase-1/2/3 accepted-overridden record and
LOGBOOK.md Iteration 6 for the verbatim panel transcript.
"""

import numpy as np

# ------------------------------------------------- shared beam-scene bench (exp-001/026/027/028, verbatim)
BEAM_N = 560
BEAM_ABSORB = 40
BEAM_FRAC = 0.32
BEAM_CX, BEAM_CY = 252, 280
BEAM_SRC_X = 64
R_IN, R_OUT = 30, 78
SIGMA_MAX = 0.5
BEAM_STEPS_NATIVE = 3200

BEAM_BOX_A = (142, 362, 170, 390)   # exp-002/026/027/028's box, unchanged
BEAM_BOX_B = (117, 387, 145, 415)
BEAM_REF = (BEAM_CX, BEAM_CY, 60)
RADIAL_N_BINS = 26

# fix 4: derived at full float64 precision, not a hand-copied literal
AMP_REL = 2e-4          # Iteration 1's own committed scenario default (LOGBOOK.md docket #4)
AMP_BEAM = 1.0
AMP_OFFAXIS = AMP_BEAM * np.sqrt(AMP_REL)
assert abs((AMP_OFFAXIS / AMP_BEAM) ** 2 - AMP_REL) < 1e-9, "amp_rel derivation failed"
OFFAXIS_ANGLE_DEG = 30.0

# Cauchy-Schwarz ceiling on the coherent interference cross-term, renormalized
# against P_abs(beam) (fix 2): |P_int| <= 2*sqrt(P_abs(beam)*P_abs(off_axis))
#   ~= 2*sqrt(AMP_REL)*P_abs(beam)  (since P_abs(off_axis) ~= AMP_REL*P_abs(beam)
#   for a linear, spatially-uniform-response object)
P_INT_CEILING_FRAC_OF_BEAM = 2.0 * np.sqrt(AMP_REL)   # 0.028284... = 2.83%

# established anchors this experiment cross-checks against
ESTABLISHED_ABS_EXT = {"graded_black_shell_600nm_cell_B": (0.5115, 0.5121)}  # exp-002/027/028, PEC-free
    # twin of this article; exp-028 measured 0.5118 exactly at this construction


if __name__ == "__main__":
    print("exp-029 geometry -- Panel Iteration 6 (Coherent-Superposition Bridge Gate)")
    print(f"AMP_REL={AMP_REL}  AMP_BEAM={AMP_BEAM}  AMP_OFFAXIS={AMP_OFFAXIS!r}")
    print(f"check: (AMP_OFFAXIS/AMP_BEAM)**2 = {(AMP_OFFAXIS/AMP_BEAM)**2:.12f} (target {AMP_REL})")
    print(f"Cauchy-Schwarz ceiling, |P_int|/P_abs(beam) <= {P_INT_CEILING_FRAC_OF_BEAM*100:.4f}%")
    print(f"bench: N={BEAM_N} (CX,CY)=({BEAM_CX},{BEAM_CY}) R_IN={R_IN} R_OUT={R_OUT} "
          f"SIGMA_MAX={SIGMA_MAX} SRC_X={BEAM_SRC_X} steps={BEAM_STEPS_NATIVE}")
