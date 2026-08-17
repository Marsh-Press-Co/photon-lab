"""exp-041 design constants -- Auditing the +-40deg Angle Pair as the N17
Correction Standard (live thread T20).
=============================================================================
Panel Iteration 18 (lead: QUANTUM OPTICS, rotation). Phase-3 synthesis
incorporates Red Team's PROCEED-WITH-MANDATORY-FIXES verdict on the Phase-1
proposal -- see NOTES.md for the full accepted/overridden record and
LOGBOOK.md Iteration 18 for the verbatim Phase 1/2/3 transcript.

Executes Iteration 2's (exp-024) own never-run follow-up: a fine 36->40deg
angle sweep, 1deg steps, at EXP-024'S EXACT GEOMETRY (MARGIN_MULT=3.5,
NY=1584 -- every constant below is copied verbatim from
experiments/024-ambient-margin-adjudication/design_geometry.py, not
recomputed or rescaled), to find where in that window the per-angle
empty-scene decision floor crosses the REAL hard gate.

MANDATORY FIX (Red Team, Phase 2, load-bearing -- VISION's catch,
independently reconfirmed against code): exp-024's own committed hard gate
is DELTA_C_GATE = 0.001 at every lambda (`experiments/024.../run.py:40-44`,
`NOTES.md:26-31`), not 0.005. 0.005 is VISION's OWN T2 perceptual C_thr
bar (photopic), not an instrument-floor gate -- scoring this leg's raw
diffraction/edge-leakage floor against it would conflate an instrument
characterization with a perceptual verdict. GATE_HARD below is the ONLY
number that scores PASS/FAIL in this experiment's Results section; every
other threshold (GATE_PERCEPTUAL_CONTEXT, ADVISORY_BOUND_040,
STAGE9_EMPTY_GATE) is reported as labeled context only, never as "the gate".

Three blocks (Red Team's own block-local-scope discipline, inherited from
exp-034/035 -- no shared cross-block harness):

  Block MAIN       -- the core audit. theta in {36,37,38,39,40}deg, BOTH
                      signs (PHOTONICS' Phase-1 recommendation, adopted:
                      exp-035's own per-angle +-40deg checks found a real,
                      unexplained sign asymmetry -- 3.4% at one geometry,
                      34% at another -- neither at exp-024's own geometry,
                      so auditing both signs here is the only way to close
                      that gap at the geometry that matters), all 3
                      wavelengths, empty-scene-only. 30 new FDTD calls.

  Block OBJPRESENT -- PHOTONICS' mandatory-fix-list addition (Red Team:
                      correctable, recommended). theta = +-40deg, 600nm
                      ONLY, dilute-sponge article (SIGMA_SPONGE, exp-024's
                      own primary N9 article, unchanged) -- tests whether
                      T15's established, resolution-growing (1.0%/2.7%/
                      3.1%) diffractive-leakage discrepancy (which only
                      manifests with an object present) couples with the
                      +-40deg geometry specifically, a channel Block MAIN's
                      empty-scene design cannot see by construction.
                      Reuses Block MAIN's own empty(+-40,600nm) profiles
                      for the contrast pairing -- 2 new FDTD calls, not 4.

  Block EXTEND     -- EM's mandatory-fix-list addition (Red Team:
                      correctable, recommended). theta in {41,42,43}deg,
                      both signs, 600nm only, empty-scene-only. Tests
                      whether the floor keeps rising smoothly past 40deg
                      (refuting any claim that 40deg is itself a special/
                      resonant point) or turns over. 6 new FDTD calls.

  TOTAL: 38 new FDTD calls.

MANDATORY FIXES applied here (Red Team, Panel Iteration 18 Phase 2 --
verdict PROCEED-WITH-MANDATORY-FIXES; full numbered attack list in
LOGBOOK.md Iteration 18 / NOTES.md Phase 3):
  1. [Red Team attack 1, VISION's catch, LOAD-BEARING] Gate corrected to
     GATE_HARD=0.001 (exp-024's own committed hard gate), not the Phase-1
     draft's 0.005. GATE_PERCEPTUAL_CONTEXT=0.005 kept, relabeled as
     VISION's own T2 photopic C_thr bar -- context only, never "the gate".
  2. [Red Team attack 2/2b, LOAD-BEARING] The Phase-1 draft's Idealization
     3 falsely claimed theta=40deg was already in the trust-suite's stage-9
     gate list. Verified against `lab/validation/run_all.py`: stage 9's
     angle set is (0, +-15) plus a separate 30deg wavelength check --
     theta=40 has NEVER been exercised by a trust-suite gate. Corrected
     below and in NOTES.md Idealizations. Also corrected: stage 9's current
     aggregate empty-identity gate is 0.005 (STAGE9_EMPTY_GATE), not the
     Phase-1 draft's stale 0.01 citation (Iteration-1's original P-V1
     number, tightened since by Red Team's own Iteration-1 attack).
  3. [PHOTONICS, correctable] Block OBJPRESENT added (see above).
  4. [ELECTROMAGNETISM, correctable] Block EXTEND added (see above); the
     Phase-1 draft's "sharp threshold, not smooth ramp" shape language is
     softened in NOTES.md Predictions to an explicit three-way falsifiable
     partition, since its original justification (EM's own "twentyfold
     cancellation collapse") was independently re-confirmed by Red Team to
     have already been REFUTED as an explanation for this exact floor by
     exp-024's own MARGIN_MULT widening (P-M1: REFUTED).
  5. [THERMODYNAMICS, correctable] Disposition of PLAN.md's two queued
     cheap THERMO add-ons (thermo_sidecar rescoping, docket #7's witness
     table) stated explicitly in NOTES.md Phase 3 -- DEFERRED, with reason
     (this cycle's own budget goes to closing the two load-bearing gate/
     idealization fixes and the two correctable block additions; folding
     in unrelated THERMO literature/coding work would blur this leg's own
     tightly-scoped, zero-mechanism charter).
  6. [MATERIALS, correctable] A realizability-relevance cap sentence added
     to NOTES.md Results discussion: this leg's outcome, in either
     direction, cannot move either UNOBTANIUM-WITH-PARAMETERS verdict in
     REALIZABILITY_MEMO.md (both gaps are 1-12 orders of magnitude,
     unrelated to this leg's bookkeeping-only scope).
  7. [Red Team attack 4] Phase-1 draft's Sec.4a self-contradiction removed:
     the central-magnitude estimates below are stated as informed
     extrapolation from geometrically-adjacent (not self-identical)
     evidence only -- no appeal to the MARGIN_MULT/fringe-ratio mechanism,
     which exp-024's own P-M1 result already refutes as this floor's cause.
  8. [Red Team attack 5] Citation correction: `block_cpl40()` (exp-034) is
     the function that discards signed C_empty and never persists per-angle
     arrays -- NOT `block_n17()` (exp-035), which retains signed data (as
     used by Block OBJPRESENT/EXTEND's own precedent below).
  9. [Red Team attack 3] VISION's own supporting statistic corrected: the
     mandatory-scope-tag/gate-ambiguity non-propagation pattern has
     recurred across Iterations 13, 14, 15, and 17 (each requiring a
     Phase-5 catch); ONE of those (17) escalated to Checkpoint criterion 4
     firing -- the program's first, not "4 of 5 firings" as originally
     miscited.

Pure geometry -- no FDTD, no measurement. Run it; the numbers it prints
cross-check the constants NOTES.md commits to.
"""

import numpy as np

# ----------------------------------------------------------- pinned geometry
# Every constant in this block is copied VERBATIM from
# experiments/024-ambient-margin-adjudication/design_geometry.py -- this leg
# audits THAT geometry specifically, so nothing here is rescaled or rebuilt.
MARGIN_MULT = 3.5
NX = 360
ABSORB = 40
CPL = {450: 15, 600: 20, 750: 25}
SRC_X = 300
TAPER = 40
R_OUT = 78
PLANE_DX = 15
OBJ_X = 170
PLANE_X = OBJ_X - R_OUT - PLANE_DX          # = 77

W_OBJ = 78
GUARD_OUT = 185
W_FLANK = 78
FLANK = (GUARD_OUT, GUARD_OUT + W_FLANK)     # (185, 263)

BOX_CLEARANCE = 12

SPONGE_TAU_CENTER = 0.10
SIGMA_SPONGE = SPONGE_TAU_CENTER / (2 * R_OUT)   # exp-024's own primary N9 article

LEVER = OBJ_X - PLANE_X       # 93
D_SP = SRC_X - PLANE_X        # 223

STEPS = 1400                  # exp-024's own settling steps, unchanged


def required_ny(margin_mult, lam_max_cpl=25):
    """Verbatim from exp-024/design_geometry.py -- reproduces NY=1584."""
    walk40 = D_SP * np.tan(np.radians(40.0))
    rule = margin_mult * np.sqrt(lam_max_cpl * D_SP)
    const = FLANK[1] + TAPER + ABSORB + walk40
    ny_min = 2 * (const + rule)
    return ny_min, rule, walk40


_ny_min, _rule750, _walk40 = required_ny(MARGIN_MULT)
NY = int(np.ceil(_ny_min / 8.0) * 8)          # = 1584, verified below
assert NY == 1584, f"geometry drift from exp-024: NY={NY}, expected 1584"

OBJ = (OBJ_X, NY // 2)
SRC_Y = (ABSORB, NY - ABSORB)

# ----------------------------------------------------------- this leg's angles
MAIN_ANGLES = tuple(sorted(
    [float(t) for t in range(36, 41)] + [-float(t) for t in range(36, 41)]
))                                            # (-40..-36, 36..40), N=10
OBJPRESENT_ANGLES = (-40.0, 40.0)             # 600nm only
EXTEND_ANGLES = tuple(sorted(
    [float(t) for t in range(41, 44)] + [-float(t) for t in range(41, 44)]
))                                            # (-43..-41, 41..43), N=6, 600nm only

# ----------------------------------------------------------- decision floors
GATE_HARD = 0.001                  # exp-024's own committed hard gate --
                                    # THE decision floor for this leg's
                                    # PASS/FAIL language (mandatory fix 1)
GATE_PERCEPTUAL_CONTEXT = 0.005    # VISION's own T2 photopic C_thr bar --
                                    # reported as context ONLY, never "the gate"
ADVISORY_BOUND_040 = 0.04          # exp-035's +-15deg-derived per-angle
                                    # advisory (PER_ANGLE_EMPTY_ADVISORY_BOUND)
                                    # -- the loose bound that let +-40deg slip
                                    # through undetected at N17 for 6+ iterations
STAGE9_EMPTY_GATE = 0.005          # lab/validation/run_all.py's CURRENT
                                    # aggregate empty-identity gate (corrected;
                                    # NOT 0.01 -- that was Iteration-1's
                                    # original, since-tightened P-V1 number)


def main():
    print(f"exp-041 geometry audit -- reusing exp-024 verbatim")
    print(f"NX={NX} NY={NY} ABSORB={ABSORB} SRC_X={SRC_X} OBJ={OBJ} "
          f"R_OUT={R_OUT} PLANE_X={PLANE_X} (lever {LEVER}) D_SP={D_SP}")
    print(f"MAIN_ANGLES ({len(MAIN_ANGLES)}): {MAIN_ANGLES}")
    print(f"OBJPRESENT_ANGLES ({len(OBJPRESENT_ANGLES)}, 600nm only): {OBJPRESENT_ANGLES}")
    print(f"EXTEND_ANGLES ({len(EXTEND_ANGLES)}, 600nm only): {EXTEND_ANGLES}")
    n_main = len(MAIN_ANGLES) * len(CPL)
    n_obj = len(OBJPRESENT_ANGLES)          # reuses MAIN's empty profiles
    n_ext = len(EXTEND_ANGLES)
    print(f"\nrun count: MAIN {n_main} + OBJPRESENT {n_obj} (reuses MAIN empty) "
          f"+ EXTEND {n_ext} = {n_main + n_obj + n_ext} new FDTD calls")
    print(f"\ndecision floors: GATE_HARD={GATE_HARD} (scores this leg) | "
          f"context only: GATE_PERCEPTUAL_CONTEXT={GATE_PERCEPTUAL_CONTEXT}, "
          f"ADVISORY_BOUND_040={ADVISORY_BOUND_040}, "
          f"STAGE9_EMPTY_GATE={STAGE9_EMPTY_GATE}")


if __name__ == "__main__":
    main()
