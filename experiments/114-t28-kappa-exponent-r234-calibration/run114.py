"""exp-114 -- Panel Iteration 91, PHOTONICS' rotation-lead cycle: executes
the Reconciled Iteration-91 queue's Tier-1 item 3 -- a cheaper
intermediate-r calibration point (r=234, kappa=3.0, kappa_ratio=1.5
relative to the r=156/cpl=25 pilot) for the `fixedabs` family, at
cpl=25, chosen specifically because it does NOT depend on the r=312
leg's own repeated cost-gate deferrals (exp-111: sequencing; exp-112:
cost/density choice; exp-113: a real, R31-scaled refusal) and can
proceed in parallel with that still-blocked thread.

This is a PURE instrument-calibration leg, not a named-bin classification
cycle: T1 route N/A, matching exp-105/106/108/110/111/112/113's own
identical framing. It does NOT propose, vary, or score any
sigma(I)/sigma(x,t)/angular-selectivity/sub-threshold content, and it does
NOT re-engage the SEPARATE, already-abandoned `shape_ratio_fixedabs`
physics question (kappa_window's own forced shape_ratio===2^n scaling
law, exp-105/106 -- a DIFFERENT exponent from the one this document
concerns, see DISCLAIMER and Idealization 4, below, for the
disambiguation this cycle's own verification found necessary).

What this cycle actually measures, for the first time: a genuine, real
FDTD wall-time pair at kappa_ratio=1.5 (r=156->234), letting
KAPPA_COST_EXPONENT -- currently fit from exactly ONE (t156,t312) pair at
kappa_ratio=2.0 (exp-110, LOGBOOK.md R28) -- be independently checked at a
DIFFERENT kappa_ratio for the first time since its founding. Also
re-verifies exp-113's own Fix 1 (box_a clearance in wavelengths) and Fix 2
(sponge-margin figures) at a third geometry, at zero additional marginal
FDTD cost (the same 3 captures this leg needs anyway).

This module holds ONLY shared geometry/classification/cost-gate code --
no Sim.run() call anywhere in this file (Phase-1 discipline, matching
run112.py/run113.py). Reuses, by direct import, NEVER copy-paste:
experiments/110-.../run.py (R110 -- kappa_of, KAPPA_COST_EXPONENT,
COST_GATE_PILOT_S/TOTAL_S, COST_GATE_SAFETY_MARGIN, geom_fixedabs),
experiments/112-.../run112.py (R112 -- geom_fixedabs_cpl, already verified
byte-exact to R110.geom_fixedabs at cpl==20 for r=156/312, extended here
to r=234 for the first time), and experiments/113-.../run113.py (R113 --
HISTORICAL_R156_CPL25_TOTAL_S/STEPS/PER_STEP_S, r31_control_ratio,
combine_control_readings -- all genuinely r-independent, reused verbatim,
unmodified).

R29 (LOGBOOK.md RULED OUT registry, Iteration 89): this file is named
run114.py specifically so a downstream file doing `import run as R110`,
`import run112 as R112`, `import run113 as R113`, and `import run114 as R`
binds four genuinely distinct sys.modules entries. Executed identity
assertions below, before this module's own code trusts the distinction.

Deviation from "reuse the gate function unmodified" (R27/R28 discipline,
stated explicitly, per this cycle's own briefing): R110.cost_gate_check()
hardcodes `kappa_ratio = kappa_of(312) / kappa_of(156)` INSIDE its own
body -- it is not parameterized by a target r, so calling it unmodified
for an r=234 target would silently apply the WRONG kappa_ratio (2.0
instead of the correct 1.5), a genuine defect if reused blindly rather
than a mere style choice. `cost_gate_check_r234()`, below, is the minimal
adaptation: it reuses R110's own KAPPA_COST_EXPONENT/
COST_GATE_SAFETY_MARGIN/COST_GATE_PILOT_S/COST_GATE_TOTAL_S constants and
R110.kappa_of() unchanged, and duplicates only the one line that must
differ (the kappa_ratio computation itself, now parameterized by r).
"""
import json
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
EXP110_DIR = os.path.join(ROOT, "experiments", "110-t28-item-i-local-norm-and-controls")
EXP112_DIR = os.path.join(ROOT, "experiments", "112-t28-cpl25-floor-spot-check")
EXP113_DIR = os.path.join(ROOT, "experiments", "113-t28-r312-cpl25-plus168-bin")
sys.path.insert(0, ROOT)
sys.path.insert(0, EXP110_DIR)
sys.path.insert(0, EXP112_DIR)
sys.path.insert(0, EXP113_DIR)

from lab import sections as sc  # noqa: E402
import run as R110               # noqa: E402  (experiments/110-.../run.py)
import run112 as R112            # noqa: E402  (experiments/112-.../run112.py)
import run113 as R113            # noqa: E402  (experiments/113-.../run113.py)

# R29: executed identity assertions -- four genuinely distinct sys.modules entries.
assert R110 is not R112 and R110 is not R113 and R112 is not R113, (
    "R29: run110/run112/run113 must be three distinct module objects")
assert hasattr(R112, "geom_fixedabs_cpl") and hasattr(R112, "CPL_RATIO"), (
    "R29: R112 must be exp-112's own run112.py")
assert hasattr(R113, "r31_control_ratio") and hasattr(R113, "combine_control_readings"), (
    "R29: R113 must be exp-113's own run113.py")

with open(os.path.join(EXP112_DIR, "results.json")) as f:
    EXP112_RESULTS = json.load(f)

# ================================================================ this cycle's own scope
R_BASE_PILOT = 156                 # the r=156/cpl=25 pilot every prior cycle in this family anchors to
R_NEW = 234                        # kappa_of(234)=3.0 -- the genuinely new geometry this cycle adds
R_EXISTING_FAR = 312               # the already-attempted (cost-gate-refused) leg, for comparison only
CPL_BASELINE = R110.CPL_600         # 20
CPL_TARGET = 25
CPL_RATIO = CPL_TARGET / CPL_BASELINE
assert CPL_RATIO == R112.CPL_RATIO == R113.CPL_RATIO


def kappa_of(r):
    return R110.kappa_of(r)


def geom_fixedabs_cpl(r, cpl):
    """Reused, unmodified, from R112 -- a generic function of (r, cpl),
    never previously evaluated at r=234. verify_geometry_identity(),
    below, is the first check this program has ever run confirming that
    genericity actually holds at this r, not merely assumed."""
    return R112.geom_fixedabs_cpl(r, cpl)


def verify_geometry_identity():
    """Extends R112's own check (r in {156, 312}) to r=234 for the first
    time (R6-style ground-truth-recovery discipline, applied to a
    genuinely new evaluation point of an already-verified-elsewhere
    formula, not a fitted estimator): geom_fixedabs_cpl(234, R110.CPL_600)
    must reproduce R110.geom_fixedabs(234) EXACTLY, field-for-field --
    R110.geom_fixedabs(r) is itself a generic function of r (parameterized
    only via kappa_of(r)), so this is a genuine, not vacuous, check: it
    was never evaluated at r=234 by any prior committed code or run in
    this program before this file existed."""
    shared = ("N", "CX", "CY", "SRC_X", "STEPS", "R_CORE", "R_COAT",
              "sigma_max", "tau_shell", "box_a", "ref")
    mismatches = []
    for r in (156, 234, 312):
        g_new = geom_fixedabs_cpl(r, R110.CPL_600)
        g_old = R110.geom_fixedabs(r)
        if g_new["absorb"] != R110.ABSORB:
            mismatches.append((r, "absorb", g_new["absorb"], R110.ABSORB))
        if g_new["edge"] != R110.EDGE:
            mismatches.append((r, "edge", g_new["edge"], R110.EDGE))
        for field in shared:
            if g_new[field] != g_old[field]:
                mismatches.append((r, field, g_new[field], g_old[field]))
    return dict(pass_=(len(mismatches) == 0), mismatches=mismatches)


# ================================================================ cost gate (R27/R28) -- adapted for a genuinely different kappa_ratio
# See module docstring for the disclosed reason R110.cost_gate_check() cannot
# be reused unmodified: it hardcodes kappa_ratio=kappa_of(312)/kappa_of(156).
KAPPA_COST_EXPONENT = R110.KAPPA_COST_EXPONENT          # 3.2053299988171697, UNCHANGED, reused
COST_GATE_SAFETY_MARGIN = R110.COST_GATE_SAFETY_MARGIN  # 1.10, UNCHANGED, reused
COST_GATE_PILOT_S = R110.COST_GATE_PILOT_S              # 5400s, UNCHANGED, reused
COST_GATE_TOTAL_S = R110.COST_GATE_TOTAL_S              # 10800s, UNCHANGED, reused

KAPPA_RATIO_234_156 = kappa_of(R_NEW) / kappa_of(R_BASE_PILOT)   # 1.5, the new ratio this cycle adds
KAPPA_RATIO_312_156 = kappa_of(R_EXISTING_FAR) / kappa_of(R_BASE_PILOT)  # 2.0, the founding/only ratio on file
assert KAPPA_RATIO_234_156 == 1.5 and KAPPA_RATIO_312_156 == 2.0

# R4 correction (this cycle's own verification, PHOTONICS): MATERIALS' own
# Iteration-90 Phase-5 review (experiments/113-.../phase5_review_materials.md,
# Finding 4) estimated "1.5**3.2 approx 2.98x" and "about 32% of this cycle's
# own projected/refused cost" for a future r=234 leg -- independently
# re-derived here by actually invoking the formula (never hand-typed): the
# true multiplier is 1.5**KAPPA_COST_EXPONENT (below), not 2.98, and the true
# ratio to the r=312 leg's own analogous uncontrolled projection is
# (1.5**k)/(2.0**k) -- approx 39.8%, not approx 32%. This does NOT change the
# qualitative conclusion (r=234 is still comfortably the cheaper option) but
# it is a real, disclosed R4-class citation discrepancy in an already-filed
# Phase-5 review, not silently propagated forward as "~32%" in this document.
KAPPA_RATIO_COST_MULTIPLIER_234 = KAPPA_RATIO_234_156 ** KAPPA_COST_EXPONENT
KAPPA_RATIO_COST_MULTIPLIER_312 = KAPPA_RATIO_312_156 ** KAPPA_COST_EXPONENT
KAPPA_RATIO_COST_MULTIPLIER_RATIO = KAPPA_RATIO_COST_MULTIPLIER_234 / KAPPA_RATIO_COST_MULTIPLIER_312



def cost_gate_check_r234(pilot_empty_wall_s, pilot_total_wall_s,
                          kappa_exponent=KAPPA_COST_EXPONENT,
                          safety_margin=COST_GATE_SAFETY_MARGIN):
    """R27/R28-compliant gate for the r=234 leg specifically -- see module
    docstring for why R110.cost_gate_check() cannot be called unmodified.
    Every other constant/behavior (pilot_pass bound, safety margin,
    proceed_ semantics) is identical to R110's own function; only the
    kappa_ratio computation is corrected to this cycle's own target r."""
    pilot_pass = pilot_empty_wall_s < COST_GATE_PILOT_S
    kappa_ratio = KAPPA_RATIO_234_156  # = 1.5, NOT R110's hardcoded 2.0
    projected_234_total_s = pilot_total_wall_s * (kappa_ratio ** kappa_exponent) * safety_margin
    total_pass = projected_234_total_s < COST_GATE_TOTAL_S
    proceed = bool(pilot_pass and total_pass)
    return dict(pilot_empty_wall_s=pilot_empty_wall_s, pilot_total_wall_s=pilot_total_wall_s,
                pilot_pass=pilot_pass, kappa_ratio=kappa_ratio,
                kappa_exponent=kappa_exponent, safety_margin=safety_margin,
                projected_234_total_s=projected_234_total_s, total_pass=total_pass,
                proceed_to_r234=proceed)


# ================================================================ R31 same-session control -- REUSED, UNMODIFIED, from R113
# r31_control_ratio()/combine_control_readings() are genuinely r-independent:
# both concern only the SAME r=156/cpl=25 pilot's own re-timing this session,
# vs. HISTORICAL_PER_STEP_S (also r-independent -- a per-step average of the
# r=156/cpl=25 3-scene blend). Nothing about them needs adapting for a
# different target r -- only the FINAL gate wrapper (below) must change,
# because THAT is where the target-r-specific kappa_ratio enters.
r31_control_ratio = R113.r31_control_ratio
combine_control_readings = R113.combine_control_readings
HISTORICAL_R156_CPL25_TOTAL_S = R113.HISTORICAL_R156_CPL25_TOTAL_S   # 670.4777698516846, reused verbatim
HISTORICAL_R156_CPL25_STEPS = R113.HISTORICAL_R156_CPL25_STEPS       # 8000, reused verbatim
HISTORICAL_PER_STEP_S = R113.HISTORICAL_PER_STEP_S                   # reused verbatim
assert HISTORICAL_R156_CPL25_TOTAL_S == EXP112_RESULTS["total_wall_s"]


def cost_gate_check_r31_r234(pilot_empty_wall_s, pilot_total_wall_s, control):
    """R31-compliant wrapper, mirroring R113.cost_gate_check_r31() exactly
    in structure (raw + scaled, gated on the scaled reading only) but
    calling THIS module's own cost_gate_check_r234() instead of
    R110.cost_gate_check() -- the one substitution the module docstring's
    deviation note discloses. `control` is a combine_control_readings()
    dict (R113's own function, reused unmodified above)."""
    raw = cost_gate_check_r234(pilot_empty_wall_s, pilot_total_wall_s)
    speed_ratio = control["used_speed_ratio"]
    scaled_empty = pilot_empty_wall_s / speed_ratio
    scaled_total = pilot_total_wall_s / speed_ratio
    scaled = cost_gate_check_r234(scaled_empty, scaled_total)
    return dict(raw=raw, scaled=scaled, control=control,
                proceed_to_r234=scaled["proceed_to_r234"])


# ================================================================ pre-registered kappa_exponent generalization check (the falsifiable
# heart of this cycle -- see module docstring; NOT the fixedabs shape_ratio
# physics question, a different exponent entirely, see Idealization 4)
#
# Phase-3 correction (Red Team's Phase-2 audit, exp-114, Fix 1 -- route (a),
# independently converged on by EM/VISION/QUANTUM's own blind critiques):
# the ORIGINAL form of this check (through Phase 2) scored rel_dev in
# EXPONENT space (|exponent_234 - KAPPA_COST_EXPONENT|/KAPPA_COST_EXPONENT)
# but justified its 0.15/0.30 bands by citing R28's own founding miss, which
# is a RATIO-space quantity (the projected wall-time MULTIPLIER miss,
# (2.0**3.2053...-2.0**3.0)/2.0**3.0 = 0.1530, not an exponent-space one --
# the true exponent-space equivalent is only (3.2053-3.0)/3.0 = 0.0684).
# Independent of the citation error, an exponent-space band of fixed
# nominal size has a kappa_ratio-DEPENDENT real-world (ratio-space)
# stringency (0.15 exponent-space implies 21.5% ratio-space stringency at
# kappa_ratio=1.5 but 39.6% at kappa_ratio=2.0) -- undermining the very
# cross-ratio-portability question this check exists to answer. Scoring
# DIRECTLY in ratio-space (below) fixes both: the 0.15/0.30 bands now
# genuinely reuse R28's own founding figure in the SAME space it was
# measured in, and their real-world stringency is kappa_ratio-invariant by
# construction (a fixed relative gap between two ratio-space numbers, not
# an exponent-space gap whose ratio-space image depends on kappa_ratio).
KAPPA_EXPONENT_CONFIRM_REL = 0.15   # RATIO-space bound -- matches R28's own founding
                                     # miss (2.0**3.2053.../2.0**3.0 - 1 = 0.1530) in
                                     # the SAME space it was measured, at ANY kappa_ratio
KAPPA_EXPONENT_REFUTE_REL = 0.30    # double that -- a deviation this large is evidence
                                     # the exponent genuinely depends on kappa_ratio,
                                     # not a single portable constant


def refit_kappa_exponent(t156_cpl25, t234_cpl25, kappa_ratio=KAPPA_RATIO_234_156):
    """Fits a fresh exponent from the (t156, t234) pair alone -- the exact
    same log-ratio construction KAPPA_COST_EXPONENT itself was originally
    derived by (ln(t312/t156)/ln(2.0), exp-110/exp-111) applied to this
    cycle's own new pair. Zero marginal cost once both times exist."""
    return math.log(t234_cpl25 / t156_cpl25) / math.log(kappa_ratio)


def classify_kappa_exponent_check(exponent_234, kappa_ratio=KAPPA_RATIO_234_156):
    """Phase-3-corrected (Red Team's audit, Fix 1, route (a)): scores in
    RATIO space, not exponent space. `kappa_ratio ** exponent_234` is
    mathematically identical to the real measured ratio t234/t156
    (refit_kappa_exponent's own construction inverted) -- so this compares
    the real measured wall-time-scaling ratio directly against the ratio
    KAPPA_COST_EXPONENT itself would have predicted at this SAME
    kappa_ratio, exactly mirroring how R28's own founding ~15.3% figure was
    computed (old-guess-exponent's ratio vs. fitted-exponent's ratio, both
    at kappa_ratio=2.0)."""
    measured_ratio = kappa_ratio ** exponent_234
    reference_ratio = kappa_ratio ** KAPPA_COST_EXPONENT
    rel_dev = abs(measured_ratio - reference_ratio) / abs(reference_ratio)
    if rel_dev <= KAPPA_EXPONENT_CONFIRM_REL:
        verdict = "CONFIRM (kappa_exponent generalizes across kappa_ratio)"
    elif rel_dev >= KAPPA_EXPONENT_REFUTE_REL:
        verdict = "REFUTE (kappa_exponent is kappa_ratio-dependent, not a portable constant)"
    else:
        verdict = "AMBIGUOUS"
    return dict(exponent_234=exponent_234, exponent_reference=KAPPA_COST_EXPONENT,
                kappa_ratio=kappa_ratio, measured_ratio=measured_ratio,
                reference_ratio=reference_ratio, rel_dev=rel_dev,
                confirm_band=KAPPA_EXPONENT_CONFIRM_REL,
                refute_band=KAPPA_EXPONENT_REFUTE_REL, verdict=verdict)


# ================================================================ Fix 1/Fix 2 re-verification at a third geometry (zero-FDTD, geometry-only
# half computable now; the sponge-vs-signal half needs Phase-4 real data)
_g156_25 = geom_fixedabs_cpl(156, 25)
_g234_25 = geom_fixedabs_cpl(234, 25)
_g312_25 = geom_fixedabs_cpl(312, 25)
_BOX_A_CLEARANCE_LAMBDA_R156 = (_g156_25["box_a"][1] - _g156_25["CX"] - _g156_25["R_COAT"]) / _g156_25["cpl"]
_BOX_A_CLEARANCE_LAMBDA_R234 = (_g234_25["box_a"][1] - _g234_25["CX"] - _g234_25["R_COAT"]) / _g234_25["cpl"]
_BOX_A_CLEARANCE_LAMBDA_R312 = (_g312_25["box_a"][1] - _g312_25["CX"] - _g312_25["R_COAT"]) / _g312_25["cpl"]

_SPONGE_LOG_ATTEN_CPL25 = 17.242357   # exp-112 Phase-2/Phase-5-corrected figure, cpl=25-specific,
                                       # depends only on cpl (ABSORB/EDGE), not r -- REUSED, not
                                       # re-derived, since geom_fixedabs_cpl(*, 25)["absorb"] is
                                       # identical at r=156/234/312 (asserted below)
assert _g156_25["absorb"] == _g234_25["absorb"] == _g312_25["absorb"] == 50
_SPONGE_ABS_VAL = float(np.exp(-_SPONGE_LOG_ATTEN_CPL25))


DISCLAIMER = ("This is an instrument-calibration/cost-gate cycle -- not a "
              "phenomenon-mechanism proposal and not a named-bin "
              "resolution-convergence classification (unlike exp-108/110/"
              "112/113). No sigma(I)/sigma(x,t)/angular-selectivity/"
              "sub-threshold content, no Weber-contrast or C_thr(L) "
              "perceptual scoring, is performed anywhere in this document. "
              "R30/R32 (a discriminating statistic's threshold/direction "
              "needing null-calibration/validation before an evidentiary "
              "reading) are N/A -- this cycle produces no discriminating "
              "statistic of that kind; it produces a wall-time calibration "
              "point and a re-verification of two already-established "
              "geometry-derived figures (Fix 1/Fix 2, exp-113) at a third "
              "r. R31 (same-session cost-projection control) DOES apply "
              "and gates the real Phase-4 spend, exactly as in exp-113 -- "
              "the projection reported in this document's own predictions "
              "text is the UNCONTROLLED reading (as if this session matches "
              f"the historical {HISTORICAL_R156_CPL25_TOTAL_S:.4f}s/3-scene "
              "session's own throughput exactly), explicitly provisional, "
              "never the gating figure -- chunk_runner114.py's own "
              "check_cost_gate_for_r234() raises rather than proceeds if no "
              "same-session control point is on file. This document's own "
              "`kappa_exponent` (KAPPA_COST_EXPONENT, a wall-time COST-"
              "scaling exponent, empirically fit from ONE (t156,t312) pair "
              "at kappa_ratio=2.0, exp-110/R28) is a DIFFERENT quantity "
              "from `shape_ratio_fixedabs`'s own forced shape_ratio===2^n "
              "PHYSICS exponent (kappa_window's own near-field-collapse "
              "scaling, n approx 4.31, exp-105/106) -- r=234 has been "
              "informally proposed twice in this program's history, once "
              "for EACH of these two unrelated exponents (PHOTONICS' own "
              "Iteration-83 Phase-5 review, exp-106, for the physics "
              "exponent; MATERIALS' own Iteration-90 Phase-5 review, "
              "exp-113, for THIS cost exponent) -- this document concerns "
              "only the cost exponent; it does not re-engage, score, or "
              "extend the physics shape_ratio question (see Idealization "
              "4). Separately: `234` also appears in this program's own "
              "RULED-OUT registry (R5 addendum, exp-070) as a REJECTED "
              "named-constant mechanism match (`A_alt approx 3*R_OUT = "
              "233/234`, a dense-search coincidence shown statistically "
              "indistinguishable from chance, `null_p=0.204-0.806`) -- that "
              "finding concerns a periodicity-MECHANISM candidate for T28's "
              "own 2.84-degree signal and has nothing to do with r=234 as "
              "a GEOMETRY SIZE for this cost-calibration leg; the two uses "
              "of the numeral are unrelated, stated here only so a future "
              "reader does not conflate a ruled-out mechanism search with "
              "this cycle's own, entirely different, proposal. "
              "R4 correction (this cycle's own re-derivation): MATERIALS' "
              "own Iteration-90 Phase-5 review (exp-113, Finding 4) "
              "estimated the r=234 leg's own cost multiplier as "
              "'1.5**3.2 approx 2.98x' ('about 32%' of the r=312 leg's own "
              "projected/refused cost) -- independently re-invoked here "
              f"from the actual committed formula: the true multiplier is "
              f"{KAPPA_RATIO_COST_MULTIPLIER_234:.6f}x (not 2.98x), and the "
              f"true ratio to the r=312 leg's own analogous uncontrolled "
              f"multiplier is {KAPPA_RATIO_COST_MULTIPLIER_RATIO:.4f} "
              f"(approx {100*KAPPA_RATIO_COST_MULTIPLIER_RATIO:.1f}%, not "
              f"approx 32%). Non-fatal to that review's own qualitative "
              f"conclusion (r=234 remains comfortably the cheaper option), "
              f"but a real, disclosed citation discrepancy, not silently "
              f"propagated forward as '~32%' in this document.")


def build_predictions_text(control=None, gate=None):
    control_line = ""
    if control is not None and gate is not None:
        control_line = (f"\n\n**R31 same-session control (measured pre-Phase-4-gate-decision, "
                         f"this session, reusing R113.r31_control_ratio/combine_control_readings "
                         f"unmodified)**: a short ({control['short']['control_steps']} steps/scene) "
                         f"and a sustained ({control['sustained']['control_steps']} steps/scene) "
                         f"3-scene-blend re-timing of the already-completed r=156/cpl=25 scenes -- "
                         f"gated on the LOWER (more conservative) of the two speed_ratio values "
                         f"({control['short']['speed_ratio']:.3f} short vs. "
                         f"{control['sustained']['speed_ratio']:.3f} sustained; used="
                         f"{control['used_speed_ratio']:.3f}). Scaled cost-gate projection: "
                         f"{gate['scaled']['projected_234_total_s']:.1f}s vs. the "
                         f"{COST_GATE_TOTAL_S}s bound -- proceed_to_r234={gate['proceed_to_r234']}.")
    _uncontrolled = cost_gate_check_r234(HISTORICAL_R156_CPL25_TOTAL_S / 3.0,
                                          HISTORICAL_R156_CPL25_TOTAL_S)
    return f"""PREDICTIONS (pre-registered, exp-114, Panel Iteration 91)

{DISCLAIMER}{control_line}

**Geometry identity (zero-FDTD, pre-Phase-4)**: verify_geometry_identity()
returns pass_=True at r=156, r=234 (new), AND r=312 -- geom_fixedabs_cpl(r,
cpl=20) must reduce to R110.geom_fixedabs(r) exactly at all three, not just
the two this program has evaluated it at before. Falsified by any
mismatch -- HALT before any Sim.run() call.

**Reproduction/self-consistency precondition (r=234 only, this cycle's own
new capture)**: sum(sigma_scat_per_bin) == sigma_scat (angular_scattered_
pattern's own docstring identity, if the angular-pattern instrument is
invoked at all this cycle -- see Idealization 3) to <1e-9 relative.
Falsified by any larger deviation -- HALT before any downstream figure
from this capture is trusted.

**Cost gate (the genuinely uncertain question this leg exists to answer
cheaply)**: UNCONTROLLED reading (as if this session matches the
historical per-step throughput exactly, NOT the gating figure --
R31 requires a fresh same-session control first): projected r=234 total
= {_uncontrolled['projected_234_total_s']:.1f}s vs. the {COST_GATE_TOTAL_S}s
bound ({100.0*(1-_uncontrolled['projected_234_total_s']/COST_GATE_TOTAL_S):.1f}%
margin if this reading held) -- compare against the already-attempted
r=312 leg's own analogous uncontrolled reading of 6802.6s (37% margin,
exp-113 Sec 2.0), which STILL failed once R31-controlled for real
(16737.4s, REFUSED). This cycle's own real, same-session R31 control
(chunk_runner114.py --control) governs the actual Phase-4 decision;
proceed_to_r234 may read False even though the uncontrolled projection
above looks comfortable, exactly as it did for r=312 last cycle.

**kappa_exponent generalization check (pre-registered, falsifiable, the
falsifiable heart of this cycle -- NOT the shape_ratio_fixedabs physics
question, see DISCLAIMER)**: once real t156(cpl=25) (already on file,
{HISTORICAL_R156_CPL25_TOTAL_S:.4f}s) and a fresh real t234(cpl=25) both
exist, refit_kappa_exponent() computes exponent_234 =
ln(t234/t156)/ln(1.5). **Phase-3 correction (Red Team's audit, Fix 1 --
EM/VISION/QUANTUM's convergent Phase-2 finding)**: scored in RATIO space,
not exponent space -- measured_ratio = 1.5**exponent_234 (== t234/t156
exactly) vs. reference_ratio = 1.5**KAPPA_COST_EXPONENT=
{KAPPA_COST_EXPONENT:.10f} (the founding exponent's own prediction, fit
from the single existing r=156-to-r=312 pair at kappa_ratio=2.0,
exp-110/R28, evaluated at THIS leg's own kappa_ratio=1.5):
| Outcome | Condition |
|---|---|
| CONFIRM | relative deviation (ratio-space) <= {KAPPA_EXPONENT_CONFIRM_REL:.2f} |
| AMBIGUOUS | {KAPPA_EXPONENT_CONFIRM_REL:.2f} < relative deviation < {KAPPA_EXPONENT_REFUTE_REL:.2f} |
| REFUTE | relative deviation (ratio-space) >= {KAPPA_EXPONENT_REFUTE_REL:.2f} |
The 0.15/0.30 bands are RATIO-space bounds, matching R28's own founding
miss (2.0**3.2053.../2.0**3.0 - 1 = 0.1530) in the same space it was
measured, at ANY kappa_ratio -- not an exponent-space bound whose
real-world stringency would otherwise vary with kappa_ratio (see
classify_kappa_exponent_check's own docstring). No advance position is
taken on which band this cycle's own real data will land in.

**Fix 1 (box_a clearance in wavelengths, zero-FDTD, computable now)**:
{_BOX_A_CLEARANCE_LAMBDA_R156:.1f} lambda at r=156, {_BOX_A_CLEARANCE_LAMBDA_R234:.1f}
lambda at r=234 (new), {_BOX_A_CLEARANCE_LAMBDA_R312:.1f} lambda at r=312 --
a geometry fact reported for continuity with exp-113's own Fix 1 finding,
not a pass/fail band (margin=32 preserves the PROPORTIONAL margin/R_COAT
ratio, not the near-field depth in wavelengths, at every r).

**Fix 2 (sponge-margin figures)**: the domain-edge sponge's own one-way
accumulated log-attenuation is IDENTICAL at r=234 to r=156/312
({_SPONGE_LOG_ATTEN_CPL25}, exp(-{_SPONGE_LOG_ATTEN_CPL25})=
{_SPONGE_ABS_VAL:.3e}, cpl-dependent only, confirmed identical `absorb`
at all three r above) -- but the margin-against-signal/floor figures
(exp-113's own three-way split: floor/signal/delta) cannot be computed
until Phase 4 produces a real r=234 measurement to compare against; not
predicted here, reported in result_text only if this cycle's own scope
extends to computing it (see Idealization 3).
"""


def build_result_text(n_fdtd_calls, total_wall_s, geom_ok, repro_ok, cost_gate_result,
                       kappa_exponent_result=None, wall_time_source=None):
    wall_time_note = f"\n({wall_time_source})" if wall_time_source else ""
    kx_line = ("Not yet scored (no real t234 on file)." if kappa_exponent_result is None
               else f"exponent_234={kappa_exponent_result['exponent_234']:.6f}, "
                    f"measured_ratio={kappa_exponent_result['measured_ratio']:.6f}, "
                    f"reference_ratio={kappa_exponent_result['reference_ratio']:.6f}, "
                    f"rel_dev(ratio-space)={kappa_exponent_result['rel_dev']:.4f}, "
                    f"verdict={kappa_exponent_result['verdict']}")
    return f"""RESULT (exp-114, Panel Iteration 91)

{DISCLAIMER}

{n_fdtd_calls} real FDTD calls, {total_wall_s:.1f}s ({total_wall_s/60.0:.2f} min)
total wall time this cycle, zero `lab/` diff.{wall_time_note}

**Geometry identity: {'PASS' if geom_ok else 'FAIL'}.**
**Reproduction/self-consistency precondition: {"N/A (not reached)" if repro_ok is None else ('PASS' if repro_ok else 'FAIL')}.**
**Cost gate:** {json.dumps(cost_gate_result, default=str) if cost_gate_result else 'NOT RUN'}
**kappa_exponent generalization check:** {kx_line}
"""


if __name__ == "__main__":
    if "--predictions-only" in sys.argv:
        print(build_predictions_text())
    elif "--verify-geometry" in sys.argv:
        result = verify_geometry_identity()
        print(json.dumps(result, indent=2))
        assert result["pass_"], "geom_fixedabs_cpl does not reduce to R110.geom_fixedabs at cpl==20"
        print("verify_geometry_identity: PASS (r=156, 234, 312)")
    else:
        print("This module holds shared geometry/constants and cost-gate/calibration "
              "functions only -- no Sim.run() call anywhere in this file.")
