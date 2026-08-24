"""exp-066 design constants -- Settling Re-Verification of exp-041's Block
MAIN (closing live thread T27, Iteration-43 ranked-#1 queue item).
=============================================================================
Panel Iteration 43 (lead: PHOTONICS, rotation). Executes the Iteration-42
Red-Team-ranked #1 priority (LOGBOOK.md T27 entry / PLAN.md queue, verbatim):
"Re-verify experiments/041-t20-angle-audit's own MAIN-block +-35/+-38/+-40deg
rows at STEPS>=2800, and scope exactly how many downstream citations are
affected."

THE ONE CHANGE: nothing physical changes -- this cycle re-runs exp-041's own
Block MAIN geometry (exp-065's `CONFIGS["C40"]`, itself exp-041 verbatim) at
a higher STEPS count, using exp-065's own already-validated harness. No new
`lab/` engine code. T1 escape route: NONE (instrument/model-fidelity
re-verification class, exp-041/exp-064 precedent).

PHASE-3 MANDATORY-FIX DOCKET applied here (Red Team, Panel Iteration 43
Phase 2 -- verdict PROCEED-WITH-MANDATORY-FIXES; full numbered attack list
in phase2_redteam_audit.md, disposition table in phase3_synthesis.md):

  A. Scope widened to cover the mandate's own literal text ("+-35/+-38/+-40")
     rather than exp-041's internal "Block MAIN" naming alone (Red Team
     attack 1, VISION's Phase-2 catch) -- at ZERO new FDTD cost, since
     exp-065's own C40 config already has +-35deg x 3lambda committed at
     BOTH STEPS=1400 (results.json Block SWEEP) and STEPS=2800
     (settled_sweep_steps2800_diagnostic.json). Cited directly here, not
     re-run (Red Team attack 2: VISION's own "+6 calls" costing was wrong).
  B. The lambda-coherence stress test is AUGMENTED, not swapped, with a
     genuine second (theta, lambda) point testing the settling-generalization
     claim along the THETA axis, not just lambda (Red Team attack 3 /
     ELECTROMAGNETISM's catch: zero of the 18 new interior-angle cells had
     any independent convergence check of their own). New cell: 37deg/600nm
     @ STEPS=4200, using MAIN-2800's own STEPS=2800 value and G-1-prime's own
     STEPS=1400 value as the other two points of the same 3-point trend.
  C. P-066-4's interpretation is relabeled STRICTLY STATISTICAL, per Red
     Team attack 4 / QUANTUM's own Phase-2 self-catch: an R^2 recovery after
     settling correction does NOT, by itself, distinguish "the T21
     edge-diffraction mechanism is real" from "the settling artifact's own
     (theta, lambda)-dependence happens to correlate with the fringe model's
     own geometric clock A*cos(theta)" -- both are governed by related
     geometric quantities. No causal language is used anywhere below.
  D. `lab/caveat_lint_config.json`'s `exp065-steps1400-unsettled-plane-
     channel` entry is widened (applied as a SEPARATE, disclosed step, not
     gated by this file's own `assert_lab_clean`-style check) to make
     REALIZABILITY_MEMO.md reachable -- Red Team attack 5 / MATERIALS'
     catch: the memo's own D_req~537-600x figure is calibrated from the
     N17 quadrature (which includes +-35deg, already shown to sign-flip
     under settling correction) and was structurally invisible to the
     existing entry's candidate_globs/trigger_terms.
  E. R_contact disposition, stated once here and in NOTES.md (Red Team
     attack 6 / THERMODYNAMICS' catch): PLAN.md's `R_contact` item (CNT-
     forest root-to-substrate thermal contact resistance) is DEFERRED a
     THIRD consecutive cycle (Iteration 41 -> 42 -> 43). This is disclosed,
     not silent: R_contact is desk/literature-sourcing work on
     `lab/thermo_sidecar.py`'s analytic Biot-number formula, orthogonal to
     this cycle's FDTD budget -- the two items never competed for the same
     resource, so this is a scope-discipline choice, not a resource
     trade-off, and is named explicitly per this program's own T27/exp-041
     precedent (an omitted-but-owed disposition, not silence).

Pure geometry + desk arithmetic -- NO FDTD in this file.
"""

import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..")))


def _load(name, relpath):
    """exp-065's and exp-042's own modules are BOTH called `design_geometry`,
    so a plain `import design_geometry` would collide with this file (and,
    when this file is imported as a module rather than run as __main__,
    could resolve to a partially-initialized self) -- same pattern exp-065
    itself used to load exp-048's module. Load each explicitly under a
    distinct name."""
    path = os.path.abspath(os.path.join(HERE, "..", relpath))
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


dg065 = _load("_exp065_design_geometry",
              "065-t24-absorb-boundary-sweep/design_geometry.py")
dg042 = _load("_exp042_design_geometry",
              "042-t21-magnitude-bridge/design_geometry.py")

# --------------------------------------------------------------- reused geometry
# exp-065's own C40 config = exp-041's geometry VERBATIM (identity anchor,
# G-1-gated bit-exact against exp-041's committed results.json at 12/30
# Block MAIN cells already). We reuse it unmodified -- no new config built.
CFG = dg065.CONFIGS["C40"]
CPL = dg065.CPL                          # {450: 15, 600: 20, 750: 25}
COURANT_FRAC = dg065.COURANT_FRAC
STEPS_BASE = dg065.STEPS                 # 1400 -- exp-041's own original STEPS
GATE_HARD = dg065.GATE_HARD              # 0.001, exp-024/041's own instrument floor
C_THR_LAB = dg065.C_THR_LAB
C_THR_FIELD = dg065.C_THR_FIELD
MARGINAL_LO, MARGINAL_HI = dg065.MARGINAL_LO, dg065.MARGINAL_HI

# --------------------------------------------------------------- angle/steps sets
# exp-041's own Block MAIN angle set (10 angles, both signs of 5).
MAIN_ANGLES = (36.0, 37.0, 38.0, 39.0, 40.0)
# The 18-cell gap: no committed data anywhere in this program covers these
# angles at any STEPS beyond 1400 (36/37/39, both signs -- 38/40 were
# already settled by exp-065's own settled_sweep_steps2800_diagnostic.json).
NEW_ANGLES = (36.0, 37.0, 39.0)
ALREADY_SETTLED_ANGLES = (38.0, 40.0)          # exp-065's own settled_sweep coverage
FALLBACK_ONLY_ANGLE = 35.0                     # mandatory fix A -- cited, not re-run

STEPS_LONG = 2800              # the settled floor (4-point trend goes flat here)
STEPS_STRESS = (4200, 5600)    # P-066-3a's own second/third points (750nm leg)
STEPS_STRESS_THETA = (4200,)   # P-066-3b's own new point (37deg/600nm leg, fix B)
STRESS_CELL_LAMBDA = (40.0, 750)   # original lambda-coherence stress cell
STRESS_CELL_THETA = (37.0, 600)    # NEW theta-coherence stress cell (fix B)

# --------------------------------------------------------------- committed-data paths
EXP041_RESULTS = os.path.join(HERE, "..", "041-t20-angle-audit", "results.json")
EXP065_RESULTS = os.path.join(HERE, "..", "065-t24-absorb-boundary-sweep",
                               "results.json")
EXP065_SETTLED_JSON = os.path.join(
    HERE, "..", "065-t24-absorb-boundary-sweep",
    "settled_sweep_steps2800_diagnostic.json")

# --------------------------------------------------------------- R_contact disposition
R_CONTACT_DISPOSITION = (
    "PLAN.md's R_contact item (CNT-forest root-to-substrate thermal contact "
    "resistance, TD-5's own thinnest safety factor of any kind, 7.8x over "
    "kappa_critical) is DEFERRED A THIRD CONSECUTIVE CYCLE at this Iteration "
    "(41 -> 42 -> 43), disclosed per THERMODYNAMICS' Phase-2 mandatory fix "
    "(Red Team attack 6). R_contact is desk/literature-sourcing work on "
    "lab/thermo_sidecar.py's analytic Biot-number formula -- it never "
    "competed with this cycle's FDTD budget, so this is a scope-discipline "
    "choice (T27's own 19-iteration citation exposure vs. one margin "
    "number), not a resource trade-off. A fourth consecutive deferral would "
    "itself be worth flagging at Iteration 44 (T27's own closing note).")

# --------------------------------------------------------------- P-066-4 refit note
FRINGE_FIT_STATISTICAL_ONLY_NOTE = (
    "This refit reports ONLY whether the T21 edge-diffraction propagator's "
    "fit quality (R^2, sign agreement, best-fit scale c*) is recovered, "
    "degraded, or improved once the STEPS=1400 Block MAIN dataset is "
    "replaced by this cycle's settled STEPS>=2800 dataset. It makes NO "
    "claim about which physical mechanism, if any, the fit quality "
    "establishes -- a recovered R^2 does not, by itself, distinguish a "
    "genuine coherent edge-diffraction fringe from the settling artifact's "
    "own (theta,lambda)-dependence correlating with the fringe model's own "
    "geometric clock A*cos(theta) (Red Team attack 4 / QUANTUM's own "
    "Phase-2 self-catch, mandatory fix C). FORWARD TRIPWIRE, adopted "
    "verbatim from exp-065's own QUANTUM-proposed, Red-Team-ratified "
    "precedent, extended: no future citation of this refit's R^2 may be "
    "read as 'confirmed edge-diffraction/coherent-fringe mechanism' while "
    "Block MINI's period-match test (P-VIS42-10, exp-065) remains "
    "UNDECIDED.")

# --------------------------------------------------------------- settling mechanism note
SETTLING_MECHANISM_NOTE = (
    "Two candidate mechanisms for the 750nm residual are on the record; "
    "this cycle's P-066-3a does not adjudicate between them, only tests "
    "whether STEPS=2800 has converged regardless of which is correct. "
    "(1) The turn-on RAMP length (`ramp_periods*lam/S`) is ~107 steps at "
    "750nm/cpl=25 -- roughly one order of magnitude (~10.5x, corrected "
    "from the Phase-1 draft's 'two orders of magnitude') short of the "
    "~1121-step first-arrival TRANSIT time across the aperture "
    "(r_edge=784.4 cells / S=0.700, exp-042's own established figure) -- "
    "so the ramp alone cannot be the dominant driver of a multi-thousand- "
    "step settling defect. (2) exp-042's own established PERIODS-OF-"
    "SETTLING-MARGIN figure (MARGIN_PERIODS = (STEPS-TRANSIT_STEPS)*S/cpl) "
    "is thinnest at 750nm (7.8 periods vs 13.0/9.8 at 450/600nm) and "
    "tracks the T21 fit residual's own lambda-dependence -- a stronger, "
    "already-committed candidate this program has not yet connected to "
    "the settling-defect question directly (Red Team attack 3). Neither "
    "is tested as a causal claim here -- P-066-3a/3b are pure convergence "
    "checks, not mechanism tests.")
