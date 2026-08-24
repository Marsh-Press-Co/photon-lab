"""exp-068 design constants -- Block ARTICLE Settled-STEPS Re-Verification
(closing live thread T27's own still-open half, Iteration-45 queue item 2).
=============================================================================
Panel Iteration 45 (lead: ELECTROMAGNETISM, rotation). Executes the
Iteration-44 Red-Team-ranked queue item 2 (PLAN.md/LOGBOOK.md, verbatim):
"VISION's Block-ARTICLE settled-STEPS FDTD leg (T27), now FOUR consecutive
cycles (Iterations 42->43->44) without being a cycle's primary FDTD work...
Pre-committed, capped scope per VISION's own Phase-5 flip condition:
article-present legs at minimum the +-35deg/600-750nm pair, STEPS>=2800,
ceiling ~30-45 FDTD calls."

THE ONE CHANGE: nothing physical changes -- this cycle re-scores exp-065's
own Block ARTICLE construction (tau_center=0.0065 off_pass-analog disk,
CONFIGS["C40"]/["C80"], both exp-065 verbatim) at STEPS>=2800 instead of
STEPS=1400, using exp-065's own already-validated harness. No new `lab/`
engine code. T1 escape route: N/A (instrument/model-fidelity
re-verification class, exp-041/exp-064/exp-066 precedent).

PHASE-3 MANDATORY-FIX DOCKET applied here (Red Team, Panel Iteration 45
Phase 2 -- verdict PROCEED-WITH-MANDATORY-FIXES; full numbered attack list
in phase2_redteam_audit.md, disposition table in phase3_synthesis.md):

  1. Deferral-count correction (VISION's catch): this is the FOURTH
     consecutive cycle (42->43->44->45) Block ARTICLE has not closed; a
     Tier-0 failure is a FIFTH consecutive miss, not a fourth.
  2. Tier0/Tier1 double-count fix (Red Team's own Attack 1): Tier1's
     article-present block is the 7 INTERIOR FALLBACK_ANGLES only
     (+-35 already covered by Tier0) -- 14 calls, not 18.
  3. Tier2 extended to both C40 and C80, both wavelengths (PHOTONICS' flip,
     Red Team Attack 4's resolution) -- 4 calls, folded into the mandatory
     floor alongside Tier0 (never de-scoped).
  4. T5_THERMAL_CAVEAT/REALIZABILITY_MEMO_CAVEAT/G_TRANSFER_T15_CAVEAT
     (THERMODYNAMICS' flip, elevated to mandatory by Red Team Attack 7)
     carried verbatim from exp-065's own design_geometry.py -- reused
     below, not redefined.
  5. exp-066's own M3 GATE_HARD-vs-C_THR_LAB scoping sentence (Red Team's
     own Attack 3, the hidden constraint-3 angle no seat surfaced) carried
     verbatim, printed at every GATE_HARD-tally reporting site.
  6. REALIZABILITY_MEMO.md contingency (MATERIALS' flip): a PASS flip on
     the article row triggers an explicit, loud flag (Amendment-needed),
     checked in run.py's scoring, not silently absorbed.
  7. caveat_lint registry widening (Red Team's own Attack 6): applied
     directly to lab/caveat_lint_config.json as a disclosed, separate step
     (same precedent as exp-066's own mandatory fix D) -- not gated by
     this file's own lab-diff check.
  8. (nice-to-have, applied) QUANTUM's Block-MINI citation tripwire: the
     14 new interior-angle empty-scene cells may not be cited on the T21
     mechanism-vs-artifact question until Block MINI's own dense scan runs.

Pure geometry + desk arithmetic -- NO FDTD in this file.
"""

import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..")))


def _load(name, relpath):
    """exp-065's design_geometry.py is loaded under a distinct module name to
    avoid colliding with this file's own name (same pattern exp-066 used to
    load exp-065's and exp-042's modules)."""
    path = os.path.abspath(os.path.join(HERE, "..", relpath))
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


dg065 = _load("_exp065_design_geometry",
              "065-t24-absorb-boundary-sweep/design_geometry.py")

# --------------------------------------------------------------- reused geometry
CONFIGS = {"C40": dg065.CONFIGS["C40"], "C80": dg065.CONFIGS["C80"]}
CPL = dg065.CPL                          # {450: 15, 600: 20, 750: 25}
COURANT_FRAC = dg065.COURANT_FRAC
R_OUT = dg065.R_OUT
STEPS_BASE = dg065.STEPS                 # 1400 -- exp-065's own Block ARTICLE STEPS
GATE_HARD = dg065.GATE_HARD              # 0.001, exp-024/041's own instrument floor
C_THR_LAB = dg065.C_THR_LAB
C_THR_FIELD = dg065.C_THR_FIELD
MARGINAL_LO, MARGINAL_HI = dg065.MARGINAL_LO, dg065.MARGINAL_HI
FALLBACK_ANGLES = dg065.FALLBACK_ANGLES  # (-35,-25,-15,-5,0,5,15,25,35)
TAU_OFF_PASS = dg065.TAU_OFF_PASS
SIGMA_OFF_PASS = dg065.SIGMA_OFF_PASS

# Mandatory fix 4 (THERMODYNAMICS/MATERIALS) -- carried verbatim, not redefined.
T5_THERMAL_CAVEAT = dg065.T5_THERMAL_CAVEAT
REALIZABILITY_MEMO_CAVEAT = dg065.REALIZABILITY_MEMO_CAVEAT
G_TRANSFER_T15_CAVEAT = dg065.G_TRANSFER_T15_CAVEAT

# Mandatory fix 5 (Red Team Attack 3) -- exp-066's own M3 sentence, verbatim.
GATE_HARD_M3_NOTE = (
    "GATE_HARD is not VISION's own perceptual bar, and this result does "
    "not by itself move any constraint-3 verdict. GATE_HARD=0.001 (exp-024/"
    "041's per-angle instrument-floor decision rule) is five times "
    "stricter than C_THR_LAB=0.005, which is never the bar scored here. "
    "(exp-066 Phase-5 mandatory fix M3, Red Team's final audit / VISION "
    "SCIENCE's catch -- carried forward verbatim per this cycle's own "
    "mandatory fix 5.)")

# Nice-to-have fix 8 (QUANTUM) -- Block MINI citation tripwire.
BLOCK_MINI_TRIPWIRE_NOTE = (
    "The 14 new interior-angle (0,+-5,+-15,+-25 deg) empty-scene settling-"
    "delta cells produced by this cycle's Tier1b may NOT be cited as "
    "bearing on T21's mechanism-vs-artifact question (whether the "
    "edge-diffraction fringe is a genuine optical effect or a settling "
    "artifact) until Block MINI's own properly-powered dense angular scan "
    "(>=2-3 T21 periods at ~0.2deg spacing, settled STEPS) runs -- these "
    "14 cells are at 5deg spacing, the same statistical underpowering "
    "QUANTUM's own Phase-5 self-catch relabeled P-VIS42-10 UNDECIDED over. "
    "(QUANTUM OPTICS' Phase-2 flip, Iteration 45, applied as a forward "
    "tripwire per Red Team's docket.)")

# --------------------------------------------------------------- angle/steps sets
INTERIOR_ANGLES = tuple(a for a in FALLBACK_ANGLES if abs(a) != 35)  # 7 angles
TIER0_ANGLES = (-35.0, 35.0)
TIER0_LAMBDAS = (600, 750)
TIER1_LAMBDA = 600
STEPS_LONG = 2800              # the settled floor (exp-065/066's own established value)
STEPS_STRESS = 4200            # Tier2's own convergence-generalization point
TIER2_THETA = -35.0            # the highest-stakes cell (sign-flips at both lambda)

# --------------------------------------------------------------- committed-data paths
EXP065_RESULTS = os.path.join(HERE, "..", "065-t24-absorb-boundary-sweep",
                               "results.json")
EXP065_SETTLED_JSON = os.path.join(
    HERE, "..", "065-t24-absorb-boundary-sweep",
    "settled_sweep_steps2800_diagnostic.json")

# --------------------------------------------------------------- deferral disposition
DEFERRAL_DISCLOSURE = (
    "ERRATUM (Iteration 45 Phase-5 close, Red Team's final audit, Attack "
    "3): the text below as originally frozen at predict-commit time "
    "self-contradicted its own arithmetic (three misses enumerated, a "
    "hypothetical fourth-cycle failure labeled a 'FIFTH miss'). Left "
    "standing below for the historical record (this string was already "
    "baked into the committed results.json output before the error was "
    "found -- not silently rewritten); corrected count, enumerated: "
    "Block ARTICLE's article-present legs were NOT closed at settled "
    "STEPS for three consecutive cycles (Iterations 42, 43, 44 -- three "
    "misses). Iteration 45 (this cycle, exp-068) is the FOURTH cycle in "
    "the sequence (42,43,44,45) and the first to make it the cycle's own "
    "primary FDTD work; had it also failed to complete the mandatory "
    "floor, that would have been the FOURTH miss, not a fifth. ORIGINAL "
    "TEXT: "
    "This is the FOURTH consecutive cycle (Iterations 42->43->44->45) "
    "Block ARTICLE's article-present legs have not been closed at settled "
    "STEPS -- exp-065 (144 calls) and exp-066 (39 calls) each fully "
    "dedicated a cycle to the surrounding T27 thread without reaching it; "
    "exp-067 explicitly deferred it a third time. This cycle (exp-068) is "
    "the first of the four in which it is the cycle's own primary, "
    "dedicated FDTD work -- closing the deferral streak at three misses "
    "if it completes. A failure to complete the mandatory floor (Tier0+"
    "Tier2) must be disclosed as a FIFTH consecutive miss, per Red Team's "
    "Phase-2 adjudication against PLAN.md/LOGBOOK.md's own Iteration-44 "
    "close text (corrected from the Phase-1 proposal's own miscount of "
    "'3 cycles / 4th miss').")

# --------------------------------------------------------------- REALIZABILITY_MEMO contingency
REALIZABILITY_MEMO_PATH = os.path.join(
    HERE, "..", "034-floor-convergence-scale-bridge", "REALIZABILITY_MEMO.md")
REALIZABILITY_MEMO_PASS_FLIP_NOTE = (
    "MATERIALS' mandatory fix (Phase 2): if the article-row C (N9, 600nm) "
    "flips PAST MARGINAL_LO at either config (i.e. clears |C| < 0.0025, a "
    "live outcome per exp-065's own Phase-5 correction showing the exact "
    "-35deg cells feeding this aggregate sign-flip by 0.0055-0.0065 in the "
    "empty channel alone), REALIZABILITY_MEMO.md's own 'tau=0.0065 no "
    "longer clears the bar at EITHER geometry, D_req is a LOWER bound' "
    "language is directly contradicted, not merely probed, and this "
    "same-shift close must open a REALIZABILITY_MEMO.md Amendment 2.")
