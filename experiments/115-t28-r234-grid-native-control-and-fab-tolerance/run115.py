"""exp-115 -- Panel Iteration 92, MATERIALS & METAMATERIALS' rotation-lead
cycle. Executes the Reconciled Iteration-92 queue's Tier-1 item 1 (a
genuine same-session control-timing burst measured DIRECTLY on the r=234
grid, matched-protocol against r=156 in the same session, with EM's
bundled immediate repeat), Tier-1 item 2 (the NOT-scored sensitivities),
and Tier-1 item 5 (MATERIALS' own fabrication-tolerance bound, an
ANALYTIC SIDECAR -- desk arithmetic over already-committed JSON, zero
FDTD).

This module holds ONLY shared constants and pure functions -- no
Sim.run() call anywhere in this file (Phase-1/Phase-3 discipline,
matching run112.py/run113.py/run114.py).

Runner: bench panel shift (T5820) -- Director Clyde, live session.

THE LOAD-BEARING IDENTITY (phase1_proposal.md Sec 1, independently
re-derived and confirmed bit-exact by Red Team's Phase-2 audit Sec 0):

    measured_ratio == kappa_ratio * G,   G == per_step(r=234)/per_step(r=156)

so exp-114 did not measure a cross-session cost ratio at all -- it
measured G, and its residual confound is the PROTOCOL MISMATCH between a
12000-steps/scene chunked numerator and a 3334-steps/scene cold-call
denominator. This cycle measures G directly, on both grids, in one
session, at matched step counts and matched scene mix.

PHASE-3 SYNTHESIS. All fifteen mandatory fixes of
`phase2_redteam_audit.md` Sec 3 (MF-1..MF-15) are ACCEPTED and applied
here; six disclosed overrides (OV-1..OV-6) are declined per Red Team's
own recommendation; Red Team's recommended-not-mandatory
SUSTAINED_CONTROL_STEPS step-down branch is ADOPTED. See NOTES.md
Phase 3 for the enumerated list. The code-visible fixes in THIS file:

  MF-1  M9(c) uses the coherent cross-term form -- scale exp(-tau_true)
        and upper bound 2*exp(-tau_true) -- NOT exp(-2*tau_true).
        tau_true is recomputed from lab/materials._graded_black at BOTH
        family members (bit-identical by construction), with a HALT.
  MF-2  M9(b)'s |sigma_ext - sigma_ext_cross| "floor" is WITHDRAWN as a
        differential floor (it is scene-independent, hence exactly
        common-mode between the two scenes being differenced); exp-108's
        six-margin item_ii family is substituted as the only differential
        floor on file; no differential floor exists at r=234.
  MF-3  M9(d) reports exp-110's floor-gated LOCAL normalization
        alongside the peak-normalized figure; the per-bin half of the
        "better than 1.6e-04" claim is withdrawn.
  MF-4  M9(d) restated at the resolution its evidence certifies
        (certified at margin=32 only; channel and resolution are fully
        confounded; near-to-mid-field box ledger, not far-field).
  MF-5  M5 goes through exponent_B = ln(1.5*G)/ln(1.5) before calling
        R114.classify_kappa_exponent_check(), with a code-assert.
  MF-7  M5 gets a coded protocol-mismatch INTERVAL (two-point bound) and
        a stated power limit (pure N^2 scaling lands INSIDE CONFIRM).
  MF-8  "resolves the straddle" withdrawn; the v2-with-measured-G
        sensitivity persisted, explicitly NOT scored.
  MF-9  Every composition rule reduced to one persisted boolean;
        mechanism-neutral M3 labels; two-sided M7 labels; M4's MARGINAL
        split at 0.03 and R_DEG/2 so the label carries its consequence.
  MF-10 DISCLAIMER_115's text lives here, with BOTH the predictions-side
        and the result-side assert in committed, re-invocable call sites
        (R23 First Addendum) -- `--predictions-only` and `--selftest`.
  MF-11 The three non-reproducing citations corrected; normalization
        conventions disclosed.
  MF-13 The perturbation disclosed for what it is (12 cells at exactly
        rr == R_CORE), with the bound that closes the alternative.
  MF-15 exp-061's MP-5 thermal counterweight carried into M9(e).

R29 (LOGBOOK.md RULED OUT registry, Iteration 89): this file is named
run115.py specifically so a downstream file binding `run as R110`,
`run112 as R112`, `run113 as R113`, `run114 as R114` and `run115 as R`
gets five genuinely distinct sys.modules entries. Executed identity
assertions below, before this module's own code trusts the distinction.

R30/R32: N/A, stated -- this cycle produces no discriminating statistic
of that class. Every scored quantity is a ratio of directly-measured
wall times against a pre-registered arithmetic reference.
"""
import json
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
EXP108_DIR = os.path.join(ROOT, "experiments", "108-t28-reclassification-angular-pattern-batch")
EXP110_DIR = os.path.join(ROOT, "experiments", "110-t28-item-i-local-norm-and-controls")
EXP112_DIR = os.path.join(ROOT, "experiments", "112-t28-cpl25-floor-spot-check")
EXP113_DIR = os.path.join(ROOT, "experiments", "113-t28-r312-cpl25-plus168-bin")
EXP114_DIR = os.path.join(ROOT, "experiments", "114-t28-kappa-exponent-r234-calibration")
DATA_DIR = os.path.join(HERE, "data")   # lab/ARTIFACTS.md: artifacts/ is RESERVED for
                                        # scene bundles; this cycle's data lives here.
sys.path.insert(0, ROOT)
sys.path.insert(0, EXP110_DIR)
sys.path.insert(0, EXP112_DIR)
sys.path.insert(0, EXP113_DIR)
sys.path.insert(0, EXP114_DIR)

from lab import materials as mat   # noqa: E402
import run as R110                 # noqa: E402  (experiments/110-.../run.py)
import run112 as R112              # noqa: E402
import run113 as R113              # noqa: E402
import run114 as R114              # noqa: E402

# R29: executed identity assertions -- five genuinely distinct module objects.
assert len({id(R110), id(R112), id(R113), id(R114)}) == 4, (
    "R29: run110/run112/run113/run114 must be four distinct module objects")
assert hasattr(R112, "geom_fixedabs_cpl") and hasattr(R112, "CPL_RATIO"), (
    "R29: R112 must be exp-112's own run112.py")
assert hasattr(R113, "r31_control_ratio") and hasattr(R113, "combine_control_readings"), (
    "R29: R113 must be exp-113's own run113.py")
assert hasattr(R114, "classify_kappa_exponent_check") and hasattr(R114, "refit_kappa_exponent"), (
    "R29: R114 must be exp-114's own run114.py")
assert os.path.basename(os.path.dirname(os.path.abspath(R114.__file__))) == os.path.basename(EXP114_DIR)


def _load(path):
    with open(path) as f:
        return json.load(f)


EXP108_RESULTS = _load(os.path.join(EXP108_DIR, "results.json"))
EXP110_RESULTS = _load(os.path.join(EXP110_DIR, "results.json"))
EXP112_RESULTS = _load(os.path.join(EXP112_DIR, "results.json"))
EXP114_RESULTS = _load(os.path.join(EXP114_DIR, "results.json"))

# ================================================================ scope / geometry (re-exported, never re-specified)
R_BASE = 156                     # kappa_of(156) = 2.0
R_NEW = 234                      # kappa_of(234) = 3.0
CPL_TARGET = R114.CPL_TARGET     # 25
assert CPL_TARGET == 25

kappa_of = R114.kappa_of
geom_fixedabs_cpl = R114.geom_fixedabs_cpl
verify_geometry_identity = R114.verify_geometry_identity

KAPPA_RATIO = kappa_of(R_NEW) / kappa_of(R_BASE)
assert KAPPA_RATIO == 1.5

# ================================================================ the reference the whole cycle is scored against (all INVOKED, never typed)
KAPPA_COST_EXPONENT = R110.KAPPA_COST_EXPONENT              # 3.2053299988171697 (R28)
REFERENCE_RATIO = KAPPA_RATIO ** KAPPA_COST_EXPONENT        # 3.6680107109370383
G_REF = REFERENCE_RATIO / KAPPA_RATIO                       # 2.4453404739580256 == 1.5**(k-1)
assert abs(G_REF - KAPPA_RATIO ** (KAPPA_COST_EXPONENT - 1.0)) < 1e-15

# exp-114's own session's figures -- every one derived from that cycle's
# committed results.json, never hand-typed (R4).
HIST_R234_PER_STEP_S = EXP114_RESULTS["t234_cpl25"] / 36000.0            # 0.19550806899203194
HIST_R156_SHORT_PER_STEP_S = EXP114_RESULTS["r31_control"]["short"]["this_session_per_step_s"]
HIST_R156_SUSTAINED_PER_STEP_S = EXP114_RESULTS["r31_control"]["sustained"]["this_session_per_step_s"]
HIST_R156_SHORT_SPEED_RATIO = EXP114_RESULTS["r31_control"]["short"]["speed_ratio"]
HIST_R156_SUSTAINED_SPEED_RATIO = EXP114_RESULTS["r31_control"]["sustained"]["speed_ratio"]
HIST_R234_EMPTY_PER_STEP_S = EXP114_RESULTS["total_wall_s_by_scene"]["empty"] / 12000.0

G_E = HIST_R234_PER_STEP_S / HIST_R156_SUSTAINED_PER_STEP_S              # 2.74550565394726
R_DEG = HIST_R156_SUSTAINED_PER_STEP_S / HIST_R156_SHORT_PER_STEP_S - 1.0  # 0.07596424755863729

# The R31 machinery, reused UNMODIFIED for the r=156 readings only (R9:
# HISTORICAL_PER_STEP_S is an r=156/cpl=25 3-scene blend; dividing an
# r=234-grid rate by it would be a textbook incommensurability).
r31_control_ratio = R114.r31_control_ratio
combine_control_readings = R114.combine_control_readings
HISTORICAL_R156_CPL25_TOTAL_S = R114.HISTORICAL_R156_CPL25_TOTAL_S
HISTORICAL_PER_STEP_S = R114.HISTORICAL_PER_STEP_S

# Cost-gate constants, reused unmodified from R110 (R27/R28).
COST_GATE_TOTAL_S = R110.COST_GATE_TOTAL_S                  # 10800
COST_GATE_SAFETY_MARGIN = R110.COST_GATE_SAFETY_MARGIN      # 1.10

# ================================================================ Block CG -- the six readings
SHORT_CONTROL_STEPS = 1000       # matches exp-113/114's own SHORT_CONTROL_STEPS
SUSTAINED_CONTROL_STEPS = 3334   # matches exp-113/114's own SUSTAINED_CONTROL_STEPS
CONTROL_SCENES = ("empty", "hollow", "peccored")   # Fix 3b (exp-113): the 3-scene mix is
                                                    # mandatory for blend-vs-blend commensurability
# MF-6(a): the sustained pass is ABBA, not ABAB. Under ABAB both sustained
# pairs inherit the SAME-SIGNED (a+b)/2 lag and d_rep reads ~0 -- an alarm
# structurally incapable of producing the reading that means "bad"
# (lab/ARTIFACTS.md's own named invariant). Under ABBA the mean of the two
# pairwise G values is unbiased to first order in a linear drift.
READING_ORDER = ("S156", "S234", "U156", "U234", "U234b", "U156b")
READING_SPEC = {
    "S156":  dict(r=156, steps=SHORT_CONTROL_STEPS),
    "S234":  dict(r=234, steps=SHORT_CONTROL_STEPS),
    "U156":  dict(r=156, steps=SUSTAINED_CONTROL_STEPS),
    "U234":  dict(r=234, steps=SUSTAINED_CONTROL_STEPS),
    "U234b": dict(r=234, steps=SUSTAINED_CONTROL_STEPS),
    "U156b": dict(r=156, steps=SUSTAINED_CONTROL_STEPS),
}
PRIMARY_READINGS = ("S156", "S234", "U156", "U234")
REPEAT_READINGS = ("U234b", "U156b")
N_SCENES = len(CONTROL_SCENES)
GRID_STEPS_PER_GRID = N_SCENES * (SHORT_CONTROL_STEPS + 2 * SUSTAINED_CONTROL_STEPS)  # 23004
# R19: call-count invariant, asserted in code and CONDITIONAL on the
# graceful-degradation branch (MF-9 / RT-12: an invariant that fires
# spuriously on the designed-safe path is worse than none).
N_SIM_RUN_CALLS_FULL = len(READING_ORDER) * N_SCENES        # 18
N_SIM_RUN_CALLS_REPEAT_SKIPPED = len(PRIMARY_READINGS) * N_SCENES   # 12

# ================================================================ M3 -- duration-invariance of G (MF-9: MECHANISM-NEUTRAL labels)
# The mechanism ("sustained-load degradation") is unvalidated and is
# contradicted in SIGN on file: R_DEG = +7.596% (longer = slower) against
# exp-114's own intra-r=234 first-3000-vs-full reading of -4.467%
# (longer = faster). The labels therefore say only what is measured.
M3_INVARIANT_BAR = R_DEG / 2.0        # 0.03798212377931864
M3_NOT_INVARIANT_BAR = R_DEG          # 0.07596424755863729
M3_LABEL_INVARIANT = "G-DURATION-INVARIANT"
M3_LABEL_PARTIAL = "PARTIAL"
M3_LABEL_NOT_INVARIANT = "G-NOT-DURATION-INVARIANT"

# ================================================================ M4 -- MF-6(d): under ABBA this is a DRIFT+NOISE statistic, not a
# repeatability statistic. MF-9: MARGINAL is split at 0.03 and R_DEG/2 so
# the label itself carries the consequence a reader needs.
M4_REPEATABLE_BAR = 0.02
M7_POWER_BAR = 0.03                   # above this, M7's model comparison is UNDERPOWERED
M4_NOISY_BAR = R_DEG

# ================================================================ M5 -- bands reused UNMODIFIED from R114 (same classifier, same space)
KAPPA_EXPONENT_CONFIRM_REL = R114.KAPPA_EXPONENT_CONFIRM_REL   # 0.15
KAPPA_EXPONENT_REFUTE_REL = R114.KAPPA_EXPONENT_REFUTE_REL     # 0.30
G_CONFIRM_LO = REFERENCE_RATIO * (1.0 - KAPPA_EXPONENT_CONFIRM_REL) / KAPPA_RATIO
G_CONFIRM_HI = REFERENCE_RATIO * (1.0 + KAPPA_EXPONENT_CONFIRM_REL) / KAPPA_RATIO
G_REFUTE_LO = REFERENCE_RATIO * (1.0 - KAPPA_EXPONENT_REFUTE_REL) / KAPPA_RATIO
G_REFUTE_HI = REFERENCE_RATIO * (1.0 + KAPPA_EXPONENT_REFUTE_REL) / KAPPA_RATIO
M5_BOUNDED_REPLICATION = "BOUNDED-REPLICATION (protocol-mismatch interval spans a band edge)"

# MF-7(b): pure cell-count (N^2) scaling -- the v2 method's own core
# assumption -- is algebraically identical to the PRE-R28 hardcoded
# exponent 3.0, and it lands INSIDE the CONFIRM band. A CONFIRM therefore
# cannot distinguish k = 3.2053 from k = 3.0.
G_N2 = (2100.0 / 1400.0) ** 2                     # 2.25 exactly
K_N2 = 1.0 + math.log(G_N2) / math.log(KAPPA_RATIO)
assert abs(K_N2 - 3.0) < 1e-12, "N^2 scaling must be exactly the pre-R28 exponent 3.0"

# MF-7(c): the two protocol models, PRE-REGISTERED before any bench data
# exists, on OPPOSITE sides of the CONFIRM ceiling.
#
# CITED-NOT-RE-DERIVABLE (disclosed, Idealization 4): exp-114's three
# r=234 chunk wall times survive only as quotations inside
# experiments/114-.../phase5_redteam_audit.md Sec 2; that session's
# scratch wall-time log did not survive. Everything computed from them
# inherits that status and is labelled directional.
EXP114_R234_FIRST_CHUNKS_S = (204.2541, 196.8292, 214.2101)   # CITED, not re-derivable
EXP114_R234_FIRST3000_PER_STEP_S = sum(EXP114_R234_FIRST_CHUNKS_S) / 3000.0
# Drift/degradation model (QUANTUM B2): extrapolate R_DEG log-linearly
# from 1000->3334 to 3334->12000; a 3334-step burst is then FASTER per
# step than production, so G comes in BELOW G_E.
PROTOCOL_MODEL_DRIFT_FACTOR = R_DEG * math.log(12000.0 / 3334.0) / math.log(3334.0 / 1000.0)
PROTOCOL_MODEL_DRIFT_G = G_E / (1.0 + PROTOCOL_MODEL_DRIFT_FACTOR)          # ~2.5403
# Warm-up-amortization model (THERMO Sec 7 / PHOTONICS Sec 4.8 / EM A11(ii)):
# inside exp-114's own r=234 production scene the first 3000 steps ran
# SLOWER per step than the 12000-step average, so a burst is slower than
# production and G comes in ABOVE G_E. Two admissible denominators:
# scene-matched (empty-to-empty) and blend (the denominator G_E actually
# uses). Both reported; the range is the pre-registered prediction.
PROTOCOL_MODEL_WARMUP_G_SCENE_MATCHED = G_E * (EXP114_R234_FIRST3000_PER_STEP_S
                                               / HIST_R234_EMPTY_PER_STEP_S)   # ~2.8681
PROTOCOL_MODEL_WARMUP_G_BLEND = G_E * (EXP114_R234_FIRST3000_PER_STEP_S
                                       / HIST_R234_PER_STEP_S)                 # ~2.8802

# MF-8: the v2 straddle's own intra-r=234 factor, DERIVED (not typed) as
# blend-average / first-3000-burst, and asserted against exp-114's own
# filed value. It reproduces to ~2e-8 relative, not to 1e-9, because the
# three chunk times above are quoted to 4 decimal places -- disclosed.
V2_P_PROD_OVER_P_BURST_FILED = 0.9532431491914767
V2_P_PROD_OVER_P_BURST = HIST_R234_PER_STEP_S / EXP114_R234_FIRST3000_PER_STEP_S
assert abs(V2_P_PROD_OVER_P_BURST - V2_P_PROD_OVER_P_BURST_FILED) / V2_P_PROD_OVER_P_BURST_FILED < 1e-6
V2_STRADDLE_BOUNDARY_G = REFERENCE_RATIO / (KAPPA_RATIO * V2_P_PROD_OVER_P_BURST_FILED)  # 2.5652851...

# ================================================================ M7 -- two-sided labels (MF-9 / RT-14)
M7_HOLDS_BAR = 0.05
EPS_2 = 2.0 ** (KAPPA_COST_EXPONENT - 3.0)        # 1.152950039837078 == R28's own founding miss + 1
M7_FAILS_BAR = EPS_2 - 1.0                        # 0.152950039837078
M7_CONST_EPS_G = G_N2 * EPS_2                     # 2.5941375896334256, the constant-eps model
M7_CONST_K_G = G_REF                              # 2.4453404739580256, the model in force

# ================================================================ M6 -- cross-machine transfer of G
M6_TRANSFERS_BAR = M7_FAILS_BAR                   # 0.152950039837078 -- R28's own founding-miss
M6_NO_TRANSFER_BAR = 2.0 * M7_FAILS_BAR           # doubled, matching exp-114's own band structure


# ================================================================================
# CLASSIFIERS -- every composition rule is CODE, not prose (R24/MF-9)
# ================================================================================

def classify_m3(g_short, g_sustained):
    """M3 -- is G duration-invariant? MECHANISM-NEUTRAL labels (MF-9):
    the statistic says whether G moved between a 1000-step and a
    3334-step protocol, not why."""
    d_dur = abs(g_sustained - g_short) / abs(g_short)
    if d_dur <= M3_INVARIANT_BAR:
        verdict = M3_LABEL_INVARIANT
    elif d_dur >= M3_NOT_INVARIANT_BAR:
        verdict = M3_LABEL_NOT_INVARIANT
    else:
        verdict = M3_LABEL_PARTIAL
    return dict(d_dur=d_dur, invariant_bar=M3_INVARIANT_BAR,
                not_invariant_bar=M3_NOT_INVARIANT_BAR, verdict=verdict)


def classify_m4(g_pair1, g_pair2, repeat_skipped=False):
    """M4 -- MF-6(d): under ABBA this is a DRIFT+NOISE statistic, not a
    repeatability statistic; every composition rule that consumes it is
    re-justified on that reading in NOTES.md. MF-9: MARGINAL is split at
    M7_POWER_BAR (0.03) and M3_INVARIANT_BAR (R_DEG/2) so the label
    carries its own consequence."""
    if repeat_skipped:
        return dict(d_rep=None, verdict="UNMEASURED (repeat pass skipped by the budget gate)",
                    repeatable_bar=M4_REPEATABLE_BAR, m7_power_bar=M7_POWER_BAR,
                    m3_scored_bar=M3_INVARIANT_BAR, noisy_bar=M4_NOISY_BAR)
    d_rep = abs(g_pair2 - g_pair1) / abs(g_pair1)
    if d_rep <= M4_REPEATABLE_BAR:
        verdict = "REPEATABLE (M3 scored, M7 powered)"
    elif d_rep <= M7_POWER_BAR:
        verdict = "MARGINAL-M3-SCORED-M7-POWERED"
    elif d_rep <= M3_INVARIANT_BAR:
        verdict = "MARGINAL-M3-SCORED-M7-UNDERPOWERED"
    elif d_rep < M4_NOISY_BAR:
        verdict = "MARGINAL-M3-UNSCORED-M7-UNDERPOWERED"
    else:
        verdict = "NOISY-M3-UNSCORED-M7-UNDERPOWERED"
    return dict(d_rep=d_rep, verdict=verdict, repeatable_bar=M4_REPEATABLE_BAR,
                m7_power_bar=M7_POWER_BAR, m3_scored_bar=M3_INVARIANT_BAR,
                noisy_bar=M4_NOISY_BAR)


def exponent_from_g(g):
    """MF-5, the one line whose absence would have returned a false
    REFUTE on this cycle's declared PRIMARY metric. R114's classifier
    takes an EXPONENT and forms `kappa_ratio ** exponent` internally;
    handing it `measured_ratio = 1.5*G` directly evaluates 1.5**(1.5*G)
    and scores rel_dev = 0.4480 -> REFUTE on exp-114's own filed value."""
    return math.log(KAPPA_RATIO * g) / math.log(KAPPA_RATIO)


def classify_m5(g_sustained):
    """M5 -- PRIMARY. Bench replication of exp-114's own scored
    statistic, through R114's own committed classifier, UNMODIFIED, via
    the MF-5 log inversion, with the MF-5 code-assert."""
    exponent_b = exponent_from_g(g_sustained)
    result = R114.classify_kappa_exponent_check(exponent_b)
    assert abs(result["measured_ratio"] - KAPPA_RATIO * g_sustained) < 1e-12, (
        "MF-5: classify_kappa_exponent_check must be fed an EXPONENT, not a ratio")
    out = dict(result)
    out["g_sustained"] = g_sustained
    out["exponent_B"] = exponent_b
    return out


def protocol_mismatch_interval(p156_short, p156_sustained, p234_short, p234_sustained,
                               n_short=SHORT_CONTROL_STEPS, n_sustained=SUSTAINED_CONTROL_STEPS,
                               n_prod_156=8000, n_prod_234=12000):
    """MF-7(a). Two-point `p(n) = p_inf + C_g/n` on EACH grid. `S` and
    `U` are the two points, so the relation is EXACTLY DETERMINED -- it
    BOUNDS, it does not fit (R7: no conditioning/VIF pricing of an unfit
    multi-parameter model is implied or needed). The interval's endpoints
    are the three protocol points the readings can reach: the measured
    burst protocol (n = n_sustained), the production protocol
    (n = 8000/12000, the step counts exp-114's own numerator and
    denominator were taken at), and the amortized limit (n -> inf).

    This extracts the same information THERMODYNAMICS' declined
    discard-first-1000-steps protocol would have (disclosed override
    OV-3) from readings already scheduled, without changing the recipe
    away from chunk_runner114::_time_control_blend and thereby breaking
    matched-protocol comparability with every prior R31 reading."""
    def two_point(p_s, p_u):
        c = (p_s - p_u) / (1.0 / n_short - 1.0 / n_sustained)
        p_inf = p_s - c / n_short
        return p_inf, c

    p156_inf, c156 = two_point(p156_short, p156_sustained)
    p234_inf, c234 = two_point(p234_short, p234_sustained)

    def g_at(n156, n234):
        return (p234_inf + c234 / n234) / (p156_inf + c156 / n156)

    g_burst = g_at(n_sustained, n_sustained)
    g_prod = g_at(n_prod_156, n_prod_234)
    g_inf = p234_inf / p156_inf
    lo, hi = min(g_burst, g_prod, g_inf), max(g_burst, g_prod, g_inf)

    # Does the interval straddle a scoring boundary?
    edges = (G_CONFIRM_LO, G_CONFIRM_HI, G_REFUTE_LO, G_REFUTE_HI)
    spans_edge = any(lo < e < hi for e in edges)
    return dict(p156_inf=p156_inf, c156=c156, p234_inf=p234_inf, c234=c234,
                g_at_burst_protocol=g_burst, g_at_production_protocol=g_prod,
                g_at_amortized_limit=g_inf, interval_lo=lo, interval_hi=hi,
                interval_rel_width=(hi - lo) / lo if lo > 0 else None,
                band_edges=list(edges), m5_protocol_caveat=bool(spans_edge))


def classify_m6(g_sustained, m3_verdict):
    """M6 -- cross-machine transfer of G. MF-9 INVERTS the proposal's
    1-of-4-state rule: M6 is directional-only UNLESS M3 reads
    G-DURATION-INVARIANT, so PARTIAL / UNSCORED / repeat-skipped all
    inherit the caveat instead of escaping it (RT-13)."""
    t = g_sustained / G_E
    dev = abs(t - 1.0)
    if dev <= M6_TRANSFERS_BAR:
        verdict = "TRANSFERS"
    elif dev >= M6_NO_TRANSFER_BAR:
        verdict = "DOES-NOT-TRANSFER"
    else:
        verdict = "AMBIGUOUS"
    directional_only = (m3_verdict != M3_LABEL_INVARIANT)
    return dict(T=t, abs_dev=dev, transfers_bar=M6_TRANSFERS_BAR,
                no_transfer_bar=M6_NO_TRANSFER_BAR, verdict=verdict,
                m6_directional_only=bool(directional_only),
                g_e_protocol_caveat=bool(directional_only), g_e=G_E)


def classify_m7(g_sustained, m7_underpowered):
    """M7 -- the N^2/v2 assumption. MF-9/RT-14: the labels are TWO-SIDED.
    `|excess| >= bar` also fires at excess = -0.15295 (G = 1.9059), which
    is SUB-cell-count scaling, the opposite finding, and inherits a
    meaning true only on the positive branch."""
    excess = g_sustained / G_N2 - 1.0
    k_b = 3.0 + math.log(g_sustained / G_N2) / math.log(KAPPA_RATIO)
    if abs(excess) <= M7_HOLDS_BAR:
        verdict = "N2_HOLDS"
    elif excess >= M7_FAILS_BAR:
        verdict = "N2_FAILS-SUPERLINEAR"
    elif excess <= -M7_FAILS_BAR:
        verdict = "N2_FAILS-SUBLINEAR"
    else:
        verdict = "AMBIGUOUS"
    # The secondary, explicitly-labelled model comparison. Pre-registered
    # as likely-underpowered with its own power condition (M7_POWER_BAR).
    d_k = abs(g_sustained - M7_CONST_K_G) / M7_CONST_K_G
    d_eps = abs(g_sustained - M7_CONST_EPS_G) / M7_CONST_EPS_G
    model = dict(const_k_prediction=M7_CONST_K_G, const_eps_prediction=M7_CONST_EPS_G,
                 rel_to_const_k=d_k, rel_to_const_eps=d_eps,
                 separation=abs(M7_CONST_EPS_G - M7_CONST_K_G) / M7_CONST_K_G,
                 underpowered=bool(m7_underpowered))
    model["favoured"] = ("UNDERPOWERED -- no model declared favoured" if m7_underpowered
                         else ("constant-k" if d_k < d_eps else "constant-eps"))
    return dict(excess=excess, k_B=k_b, holds_bar=M7_HOLDS_BAR, fails_bar=M7_FAILS_BAR,
                verdict=verdict, model_comparison=model,
                note=("N2_HOLDS requires BOTH candidate cost models to be wrong: the in-force "
                      "constant-k model predicts excess=%.5f (AMBIGUOUS) and the constant-eps "
                      "model predicts excess=%.15f, bit-adjacent to the N2_FAILS bar."
                      % (M7_CONST_K_G / G_N2 - 1.0, M7_CONST_EPS_G / G_N2 - 1.0)))


def sensitivities_do_not_score(g_sustained=None):
    """M8 (Tier-1 item 2) + MF-8. Persisted as explicitly-suffixed
    `..._DO_NOT_SCORE` fields. NONE of these is scored, and none may move
    a LOGBOOK verdict.

    OV-1 (disclosed override, on Red Team's own recommendation): QUANTUM's
    M10 is adopted here as a NOT-scored sensitivity only. Its scored half
    -- a pre-registered STRADDLE-CLOSED/STRADDLE-OPEN verdict -- is
    DECLINED, because `1.5*G_bench*(p_prod/p_burst)` composes a
    bench-measured G with exp-114's own session's protocol ratio, which
    presumes exactly the machine-independence M6 exists to test."""
    out = {}

    # exp-114 rescored with its OWN short control reading.
    t156_short_adj = HISTORICAL_R156_CPL25_TOTAL_S / HIST_R156_SHORT_SPEED_RATIO
    e_short = R114.refit_kappa_exponent(t156_short_adj, EXP114_RESULTS["t234_cpl25"])
    r_short = R114.classify_kappa_exponent_check(e_short)
    out["sensitivity_short_reading_DO_NOT_SCORE"] = dict(
        t156_session_adjusted_short=t156_short_adj,
        speed_ratio_short=HIST_R156_SHORT_SPEED_RATIO,
        measured_ratio=r_short["measured_ratio"], rel_dev=r_short["rel_dev"],
        signed_dev=(r_short["measured_ratio"] - REFERENCE_RATIO) / REFERENCE_RATIO,
        verdict=r_short["verdict"])

    # The v2 (N^2-normalization) straddle, reconstructed from primitives.
    v2_ratio = KAPPA_RATIO * G_N2 * V2_P_PROD_OVER_P_BURST_FILED
    v2_signed = (v2_ratio - REFERENCE_RATIO) / REFERENCE_RATIO
    filed_signed = (EXP114_RESULTS["kappa_exponent_result"]["measured_ratio"]
                    - REFERENCE_RATIO) / REFERENCE_RATIO
    out["sensitivity_v2_straddle_DO_NOT_SCORE"] = dict(
        measured_ratio=v2_ratio, signed_dev=v2_signed, filed_signed_dev=filed_signed,
        opposite_sides=bool(v2_signed * filed_signed < 0),
        spread_between_central_estimates=(EXP114_RESULTS["kappa_exponent_result"]["measured_ratio"]
                                          - v2_ratio) / v2_ratio,
        note=("The two 'sensitivities' are the SAME question in different clothes: which "
              "same-session r=156 per-step rate is protocol-matched to the r=234 numerator."))

    # MF-8: the same construction with THIS cycle's own measured G. Not scored.
    if g_sustained is not None:
        v2m = KAPPA_RATIO * g_sustained * V2_P_PROD_OVER_P_BURST_FILED
        out["sensitivity_v2_with_measured_G_DO_NOT_SCORE"] = dict(
            measured_ratio=v2m, signed_dev=(v2m - REFERENCE_RATIO) / REFERENCE_RATIO,
            straddle_sign_boundary_G=V2_STRADDLE_BOUNDARY_G,
            straddle_still_open=bool(g_sustained < V2_STRADDLE_BOUNDARY_G),
            fraction_of_confirm_band_below_boundary=((V2_STRADDLE_BOUNDARY_G - G_CONFIRM_LO)
                                                     / (G_CONFIRM_HI - G_CONFIRM_LO)),
            NOT_SCORED=("Composes a bench-measured G with exp-114's own session's "
                        "p_prod/p_burst; scoring it would presume the machine-independence "
                        "M6 exists to test (OV-1)."))

    out["sustained_choice_justification"] = (
        "'Sustained' (3334 steps/scene) is the protocol-matched r=156 comparator for a "
        "12000-steps/scene production numerator because 3334 is the CLOSER DURATION MATCH "
        "than 1000 is, and R_DEG = %.6f shows duration measurably matters on this axis. "
        "That is a protocol-commensurability argument (R9), NOT the cost-gate conservatism "
        "argument Iteration 90 ratified -- a materially different justification, and M3 "
        "tests it directly rather than asserting it. Disclosed conflict, not papered over: "
        "R113.combine_control_readings() selects the LOWER speed_ratio, which happened to be "
        "the sustained reading in exp-114's session but is not the same rule."
        % R_DEG)
    return out


# ================================================================================
# MF-8, second half: the numbered decline the Iteration-92 queue's own
# Tier-1 item 1 needs and that phase1_proposal.md Sec 3 did not carry.
# ================================================================================
DECLINE_8 = (
    "8. Tier-1 item 1's OWN SECOND HALF -- 're-score kappa_exponent_result against the "
    "corrected denominator' -- is DECLINED as un-executable, not silently absorbed (R25). "
    "It has two halves and neither is available: (i) the cross-session half DISSOLVES under "
    "the Sec-1 identity (measured_ratio == kappa_ratio * G; every cross-session term cancels "
    "identically, so there is no cross-session denominator left to correct); (ii) the "
    "burst-vs-production half is not measurable without an r=234 PRODUCTION leg, which this "
    "cycle does not run and which would cost three 12000-step scenes. What this cycle CAN do "
    "for it -- MF-7(a)'s two-point protocol-mismatch interval -- it does.")


# ================================================================================
# M9 -- ANALYTIC SIDECAR (Tier-1 item 5). Desk arithmetic over committed
# JSON and committed source. ZERO FDTD calls, zero grid-steps, zero bench
# wall time on the timed path.
# ================================================================================
TAU_TRUE_FILED = 8.258819829686677          # exp-061's own committed figure
TAU_TRUE_REPRO_REL_BAR = 0.01               # the pre-registered HALT bar (<1%)
SHELL_THICKNESS_UM = 1.440
SHELL_THICKNESS_LAMBDA = 2.40


def _trapezoid(y, x):
    """Portable trapezoid rule. numpy 2.x removed `np.trapz` and numpy
    1.x has no `np.trapezoid`, so neither name is safe across the bench
    venv and this workstation -- this is two lines and is."""
    y = np.asarray(y, dtype=float)
    x = np.asarray(x, dtype=float)
    return float(np.sum((y[1:] + y[:-1]) * 0.5 * (x[1:] - x[:-1])))


def i_graded(sigma_max, cpl, npts=2000001):
    """`I_graded = integral_0^1 Im(n(sigma_graded(d))) dd`, recomputed
    from lab/materials._graded_black's OWN committed profile -- never
    re-typed from exp-061's prose. `sigma(d) = sigma_max * s(d)^2` (the
    committed `_graded_black` returns `(s, 0.5*s**2)` and
    `graded_black_shell` writes `sigma_max * sig / 0.5`), and
    `n = sqrt(1 + i*sigma*cpl/(2*pi))` at this bench's grid
    normalization. Closes exp-061's own hand-carried `I_graded = 0.273840`,
    which exists nowhere as committed code."""
    d = np.linspace(0.0, 1.0, npts)
    _s, sig = mat._graded_black(d)
    sigma = sigma_max * sig / 0.5
    n = np.sqrt(1.0 + 1j * sigma * cpl / (2.0 * math.pi))
    return _trapezoid(np.imag(n), d)


def tau_true(sigma_max, cpl, thickness_cells, npts=2000001):
    """`tau_true = 2 * (2*pi/cpl) * thickness_cells * I_graded` -- the
    leading 2 is the `alpha = 2*k0*Im(n)` INTENSITY convention, which is
    exactly why MF-1 matters: tau_true is a one-way INTENSITY optical
    depth, and the measured observable is a relative change in a
    cross-section, which is quadratic in the TOTAL field."""
    return 2.0 * (2.0 * math.pi / cpl) * thickness_cells * i_graded(sigma_max, cpl, npts)


def _shell_cell_counts(N, CX, CY, R_CORE, R_COAT):
    """MF-13. Counts, from the same radius convention lab/materials._grids
    uses at the Ez family, (i) the graded_black_shell cells and (ii) the
    cells where `pec_disk`'s `rr <= R_CORE` and `graded_black_shell`'s
    `rr >= R_CORE` OVERLAP -- i.e. cells at exactly rr == R_CORE, both
    PEC-zeroed and maximally lossy. Pure numpy on a radius grid; builds
    no Sim and runs nothing."""
    x = np.arange(N)[:, None] - CX
    y = np.arange(N)[None, :] - CY
    rr = np.hypot(x, y)
    shell = int(np.sum((rr >= R_CORE) & (rr <= R_COAT)))
    overlap = int(np.sum(rr == R_CORE))
    return shell, overlap


def _aggregate_deltas(ledger):
    """MF-11 normalization disclosure, stated as a formula rather than
    left for a reader to guess twice: the six M9(a) deltas are
    SYMMETRIC-MEAN normalized, `|h - p| / ((h + p)/2)`. (The withdrawn
    M9(b) 'floors' were `peccored`-normalized -- two different,
    undisclosed conventions inside one headline ratio, RT-9.)"""
    out = {}
    for ch in ("sigma_scat", "sigma_abs", "sigma_ext"):
        h = ledger["hollow"][ch]
        p = ledger["peccored"][ch]
        out[ch] = abs(h - p) / ((h + p) / 2.0)
    return out


def _std_sample(values):
    """Sample standard deviation (ddof=1) -- the convention Red Team's own
    4.46x / 11.70x figures were computed under."""
    v = np.asarray(values, dtype=float)
    n = len(v)
    return float(math.sqrt(float(np.sum((v - v.mean()) ** 2)) / (n - 1)))


def sidecar_m9():
    """The fabrication-tolerance bound, corrected per MF-1..MF-4 and
    MF-11/MF-13/MF-15. Carries a code-enforced arithmetic reproduction
    gate; ANY mismatch HALTs the sidecar, which is then reported
    NOT-REPRODUCED rather than published.

    RT-15 is accepted in full and is the reason MF-1..MF-4 are applied
    rather than the sidecar merely re-gated: a reproduction gate is
    structurally incapable of catching a FUNCTIONAL-FORM error. The
    corrected (c) is a genuine zero-free-parameter prediction that the
    measured deltas either do or do not sit within an order of, and
    MF-2's differential floor makes 'resolved vs floor-limited' an
    answerable question rather than an asserted one."""
    checks = []

    def gate(name, got, expected, rel_bar=1e-12):
        rel = abs(got - expected) / abs(expected) if expected else abs(got)
        ok = rel <= rel_bar
        checks.append(dict(name=name, got=got, expected=expected, rel=rel,
                           rel_bar=rel_bar, ok=bool(ok)))
        return ok

    # ---- (c) first: the HALT sub-check, at BOTH family members. -------------
    # MF-1 / OV-5: the two members are the SAME OPTICAL ARTICLE BY
    # CONSTRUCTION, not by coincidence -- sigma_max*cpl = 0.5*20 = 0.4*25 = 10
    # (identical loss tangent) and thickness/cpl = 48/20 = 60/25 = 2.40 lambda.
    # tau_true is therefore bit-identical at both, and QUANTUM's
    # (6.6071, 8.2588) concavity bound is DECLINED as refuted, not adopted.
    tau_cpl20 = tau_true(0.5, 20, 48)
    tau_cpl25 = tau_true(0.4, 25, 60)
    repro_cpl20 = gate("tau_true@cpl20(sigma_max=0.5,48 cells)", tau_cpl20,
                       TAU_TRUE_FILED, TAU_TRUE_REPRO_REL_BAR)
    repro_cpl25 = gate("tau_true@cpl25(sigma_max=0.4,60 cells)", tau_cpl25,
                       TAU_TRUE_FILED, TAU_TRUE_REPRO_REL_BAR)
    gate("tau_true bit-identity between family members", tau_cpl25, tau_cpl20, 1e-12)
    gate("loss tangent sigma_max*cpl identical", 0.4 * 25, 0.5 * 20, 1e-15)
    gate("thickness/cpl identical (lambda)", 60.0 / 25.0, 48.0 / 20.0, 1e-15)

    tau = tau_cpl25
    scale = math.exp(-tau)          # the correct characteristic SCALE
    bound = 2.0 * math.exp(-tau)    # the correct coherent-cross-term UPPER BOUND
    wrong_form = math.exp(-2.0 * tau)   # the proposal's figure: the |dA|^2 term only

    lam_rows = []
    for lam_nm, cpl in ((450.0, 18.75), (600.0, 25.0), (750.0, 31.25)):
        t = tau_true(0.4, cpl, 60)
        lam_rows.append(dict(lambda_nm=lam_nm, cpl=cpl, I_graded=i_graded(0.4, cpl),
                             tau_true=t, two_exp_minus_tau=2.0 * math.exp(-t)))

    # ---- (a) the measured deltas, recomputed from each cycle's own JSON. ----
    d156 = _aggregate_deltas(EXP112_RESULTS["energy_ledger"])
    d234 = _aggregate_deltas(EXP114_RESULTS["energy_ledger"])
    gate("exp-112 sigma_scat delta", d156["sigma_scat"], 8.359387007873527e-05, 1e-9)
    gate("exp-114 sigma_scat delta", d234["sigma_scat"], 1.0873544930288214e-04, 1e-9)

    # MF-11: two independent channels and their EXACT ALGEBRAIC SUM.
    # lab/sections.py:150 DEFINES sigma_ext == (p_scat + p_abs)/i_inc, so
    # d(sigma_ext) == d(sigma_scat) + d(sigma_abs) identically. NOT three
    # independent channels. OV-4: EM's A9 promotion of sigma_ext_cross to a
    # third channel is DECLINED, refuted by EM's own A7.
    def abs_delta(ledger, ch):
        return ledger["hollow"][ch] - ledger["peccored"][ch]
    sum_resid_156 = (abs_delta(EXP112_RESULTS["energy_ledger"], "sigma_scat")
                     + abs_delta(EXP112_RESULTS["energy_ledger"], "sigma_abs")
                     - abs_delta(EXP112_RESULTS["energy_ledger"], "sigma_ext"))
    sum_resid_234 = (abs_delta(EXP114_RESULTS["energy_ledger"], "sigma_scat")
                     + abs_delta(EXP114_RESULTS["energy_ledger"], "sigma_abs")
                     - abs_delta(EXP114_RESULTS["energy_ledger"], "sigma_ext"))

    # ---- (b) MF-2: the withdrawn floor, and the real differential floor. ---
    def cross_minus_ext(ledger, scene):
        return ledger[scene]["sigma_ext_cross"] - ledger[scene]["sigma_ext"]
    withdrawn = dict(
        r156_peccored=cross_minus_ext(EXP112_RESULTS["energy_ledger"], "peccored"),
        r156_hollow=cross_minus_ext(EXP112_RESULTS["energy_ledger"], "hollow"),
        r234_peccored=cross_minus_ext(EXP114_RESULTS["energy_ledger"], "peccored"),
        r234_hollow=cross_minus_ext(EXP114_RESULTS["energy_ledger"], "hollow"))
    withdrawn["r156_between_scene_difference"] = withdrawn["r156_peccored"] - withdrawn["r156_hollow"]
    withdrawn["r234_between_scene_difference"] = withdrawn["r234_peccored"] - withdrawn["r234_hollow"]
    withdrawn["status"] = (
        "WITHDRAWN as a differential floor (MF-2). p_ext_cross - p_ext = F(pi), a function of "
        "the EMPTY capture and the box alone, carrying no scene information -- so the quantity "
        "is bit-identical in the two configurations being differenced (0.0 EXACTLY at r=234, "
        "2.27e-13 roundoff at r=156) and cancels. It is a SOLVER SELF-CONSISTENCY statistic, "
        "never a differential floor; dividing a between-scene difference by a within-scene "
        "common-mode residual is a pure R9 incommensurability, and the proposal's '0.2x-12.6x "
        "the floor' reading and its 'upper bound, not a resolved effect' conclusion are both "
        "void. R30, not R13, was the live rule on that gate (sigma_ext ~ 1093 has no "
        "zero-crossing); this withdrawal discharges it.")

    diff_floor = {}
    for tag, key in (("r156", "r156"), ("r312", "r312")):
        dv = EXP108_RESULTS["tier1"][key]["item_ii"]["delta_values"]
        mean = float(np.mean(dv))
        sd = _std_sample(dv)
        diff_floor[tag] = dict(margins=EXP108_RESULTS["tier1"][key]["item_ii"]["margins"],
                               mean_delta=mean, std_delta=sd, mean_over_std=abs(mean) / sd,
                               n_margins=len(dv))
    gate("exp-108 item_ii r156 mean/std", diff_floor["r156"]["mean_over_std"], 4.4653, 1e-3)
    gate("exp-108 item_ii r312 mean/std", diff_floor["r312"]["mean_over_std"], 11.6959, 1e-3)
    diff_floor["r234"] = "NO DIFFERENTIAL FLOOR EXISTS AT r=234 (THERMODYNAMICS' box_dev gap)"
    diff_floor["reading"] = (
        "On the only differential floor this program has -- exp-108's item_ii family, the SAME "
        "peccored-minus-hollow differential measured at six independent box radii -- the "
        "core-swap effect is RESOLVED at 4.47x (r=156) and 11.70x (r=312), NOT floor-limited.")

    # ---- (a)/(d) MF-3: the per-bin channel, on BOTH normalizations. --------
    per_bin = {}
    for tag in ("r156", "r312"):
        ld = EXP110_RESULTS[tag]["local_diag"]["32"]
        bc = EXP110_RESULTS[tag]["bin_centers_deg"]
        pairs = [(v, bc[i]) for i, v in enumerate(ld["local_rel"]) if v is not None]
        pairs.sort(reverse=True)
        per_bin[tag] = dict(
            max_floor_gated_local_rel=pairs[0][0], at_bin_center_deg=pairs[0][1],
            second=dict(local_rel=pairs[1][0], at_bin_center_deg=pairs[1][1]),
            n_resolved=ld["n_resolved"], n_total=ld["n_total"],
            peak_normalized_rel32_max=max(abs(x) for x in
                                          EXP108_RESULTS["tier1"][tag]["item_i"]["rel32"]))
    gate("exp-110 r156 max floor-gated local_rel", per_bin["r156"]["max_floor_gated_local_rel"],
         0.014669070259562213, 1e-12)
    gate("exp-110 r312 max floor-gated local_rel", per_bin["r312"]["max_floor_gated_local_rel"],
         0.05290046381280309, 1e-12)
    per_bin["withdrawal"] = (
        "The PER-BIN half of any 'insensitive at better than 1.6e-04' claim is WITHDRAWN "
        "(MF-3). 1.5266e-04 is the PEAK-normalized figure (denominator = the global max over "
        "48 bins), which LOGBOOK Iteration 85 already records as structurally blind to real "
        "shape differences in low-cross-section side/back-scatter sectors, and which exp-110 "
        "was built at Iteration 87 to replace. On the floor-gated LOCAL normalization the "
        "figure is 99.4x larger at r=156 and 346.5x larger at r=312. The two largest resolved "
        "r=312 deviations sit at +/-138.75 deg, INSIDE the observer-return hemisphere PANEL.md "
        "scores constraint 2 on. exp-112's ungated backscatter bins are NOT cited: that "
        "cycle's own mirror-pooled floor gate marks 0 of 12 backscatter bins resolved.")

    # ---- MF-4: the scope clauses, restated at the resolution certified. ----
    scope = dict(
        margin_scope=("CERTIFIED AT MARGIN=32 ONLY for the tight per-bin figure. "
                      "experiments/108-.../run.py:244-254 sets confirm_all_margins as ONE "
                      "boolean over MARGINS=(24,32,40,48,57,65) against "
                      "ITEM_I_CONFIRM_REL = 0.05 -- a DECISION BAR, not a measurement, and "
                      "330x looser than the quoted figure; only the margin-32 array is "
                      "persisted. R4 second addendum: an aggregate flag is not sufficient to "
                      "certify an 'every single X' claim."),
        channel_resolution_confound=("CHANNEL AND RESOLUTION ARE FULLY CONFOUNDED: the "
                                     "per-bin channel exists only at cpl=20 (exp-108/110, "
                                     "r=156/312) and the aggregate channels only at cpl=25 "
                                     "(exp-112/114, r=156/234). 'Two grid resolutions' is "
                                     "therefore NOT a resolution check on any channel."),
        radius_scope="r=234 contributes AGGREGATE channels only (exp-114's captures were never persisted).",
        instrument_scope=("NEAR-TO-MID-FIELD BOX LEDGER at this bench's own measurement "
                          "geometry -- NOT a far-field pattern. lab/sections.py:212-215 says "
                          "so in its own docstring ('a square-path angular sample, not a true "
                          "circular far-field pattern'), and LOGBOOK's ESTABLISHED section "
                          "plus T9 record that this bench's box sits deep in the shadow's near "
                          "zone (sigma_abs/sigma_ext = 0.51 and 0.606-0.608 both EXCEED the "
                          "far-field Babinet ceiling of 0.5 for exactly that reason)."))

    # ---- MF-13: what the perturbation actually is. -------------------------
    g156 = geom_fixedabs_cpl(156, CPL_TARGET)
    g234 = geom_fixedabs_cpl(234, CPL_TARGET)
    shell156, overlap156 = _shell_cell_counts(g156["N"], g156["CX"], g156["CY"],
                                              g156["R_CORE"], g156["R_COAT"])
    shell234, overlap234 = _shell_cell_counts(g234["N"], g234["CX"], g234["CY"],
                                              g234["R_CORE"], g234["R_COAT"])
    smallest_delta = min(list(d156.values()) + list(d234.values()))
    largest_delta = max(list(d156.values()) + list(d234.values()))
    overlap_bound = (overlap234 / float(shell234)) * scale
    perturbation = dict(
        what_it_is=("vacuum -> PERFECT ELECTRIC CONDUCTOR over rr <= R_CORE. It is NOT a pure "
                    "core-material swap: materials.pec_disk sets sim.pec |= rr <= R_CORE while "
                    "graded_black_shell writes sigma for rr >= R_CORE, so the sets OVERLAP on "
                    "cells at exactly rr == R_CORE, which are both PEC-zeroed and maximally "
                    "lossy."),
        overlap_cells_r156=overlap156, shell_cells_r156=shell156,
        overlap_cells_r234=overlap234, shell_cells_r234=shell234,
        overlap_fraction_r156=overlap156 / float(shell156),
        overlap_fraction_r234=overlap234 / float(shell234),
        closure_bound=overlap_bound,
        closure_bound_with_4x_standing_wave=4.0 * overlap_bound,
        ratio_to_smallest_measured_delta=smallest_delta / overlap_bound,
        ratio_to_largest_measured_delta=largest_delta / overlap_bound,
        closure=("RULED OUT, not merely unaddressed. Those cells sit at the shell's inner face "
                 "where the intensity has already been attenuated by exp(-tau_true) = %.4e, so "
                 "their contribution to a relative delta is ~%.2e -- %.0fx below the SMALLEST "
                 "of the six measured aggregate deltas (%.3e) and %.0fx below the largest "
                 "(%.3e), even allowing a 4x standing-wave enhancement at the PEC face. "
                 "PHOTONICS' Sec 4.11 calls these 12 cells 'the innermost ring', which "
                 "overstates them by ~3 orders. DISCLOSED FORWARD CORRECTION (R4): MF-13's own "
                 "wording says this bound sits 'five orders below the smallest measured delta'; "
                 "recomputed here it is %.1f orders below the smallest and %.1f below the "
                 "largest. The ~1e-8 magnitude MF-13 states reproduces; its 'five orders' "
                 "comparison does not, and the qualitative conclusion (ruled out) is unchanged."
                 % (scale, overlap_bound, smallest_delta / overlap_bound, smallest_delta,
                    largest_delta / overlap_bound, largest_delta,
                    math.log10(smallest_delta / overlap_bound),
                    math.log10(largest_delta / overlap_bound))))

    # ---- MF-15: exp-061's own MP-5 thermal counterweight. -------------------
    thermal_counterweight = dict(
        source="experiments/061-absorptivity-mechanism-literature-check/NOTES.md, THERMO disposition table",
        rows=[dict(mp5_multiple=230, l_geometric_um=331.2, delta_T_ss_K=5.277e-3,
                   margin_vs_netd_lo=3.79, classification="UNDETECTABLE"),
              dict(mp5_multiple=730, l_geometric_um=1051.2, delta_T_ss_K=1.4774e-2,
                   margin_vs_netd_lo=1.35, classification="UNDETECTABLE")],
        netd_lo_K=0.020,
        reading=("The same thickening that makes the article MORE backing-independent (the "
                 "bound scales as exp(-tau_true) and tau_true grows with thickness) also "
                 "shrinks the thermal margin from 3.79x to 1.35x against NETD-lo, and makes "
                 "the article a physically LARGER BLACK SILHOUETTE -- constraint 3's own "
                 "failure mode. The forward conditional is not free."))

    all_ok = all(c["ok"] for c in checks)
    status = "REPRODUCED" if all_ok else "NOT-REPRODUCED"
    c_withheld = not (repro_cpl20 and repro_cpl25)

    return dict(
        status=status,
        reproduction_checks=checks,
        c_physics=dict(
            tau_true_recomputed_cpl20=tau_cpl20, tau_true_recomputed_cpl25=tau_cpl25,
            tau_true_filed=TAU_TRUE_FILED,
            characteristic_scale_exp_minus_tau=scale,
            coherent_cross_term_upper_bound_2exp_minus_tau=bound,
            proposal_figure_exp_minus_2tau_WITHDRAWN=wrong_form,
            wrong_by_factor=math.exp(tau),
            wavelength_rows=lam_rows,
            withheld=bool(c_withheld),
            note=("MF-1. tau_true is a ONE-WAY INTENSITY optical depth; the measured "
                  "observable is a relative change in a cross-section, and every "
                  "cross-section in lab/sections.py is a flux integral QUADRATIC IN THE TOTAL "
                  "FIELD. Writing A = A_shell + A_core, "
                  "dSigma/Sigma = [2 Re(A_shell* dA_core) + |dA_core|^2]/|A_shell|^2 -- the "
                  "leading term is the COHERENT CROSS TERM, first order in the returned "
                  "amplitude. exp(-2 tau_true) answers 'how much core-reflected POWER returns' "
                  "and is the wrong answer to 'how much does the CROSS-SECTION change'; this "
                  "is a deterministic single-frequency FDTD field and the cross term does not "
                  "average away. exp(-tau_true) is the characteristic SCALE, 2 exp(-tau_true) "
                  "the correct UPPER BOUND (|2 Re z| <= 2|z|). Backing freedom is weakest in "
                  "the red (2.05x worse at 750 nm than 450 nm) and has been MEASURED only at "
                  "600 nm.")),
        a_aggregate_deltas=dict(
            r156=d156, r234=d234,
            normalization="symmetric mean: |hollow - peccored| / ((hollow + peccored)/2)",
            channel_count_correction=("TWO independent channels and their EXACT ALGEBRAIC SUM "
                                      "(MF-11), not 'three independent energy-ledger channels': "
                                      "lab/sections.py:150 defines sigma_ext == "
                                      "(p_scat + p_abs)/i_inc. Residual d_scat + d_abs - d_ext "
                                      "= %.3e (r=156), %.3e (r=234). At r=156 the two genuine "
                                      "channels PARTIALLY CANCEL, so the derived sigma_ext "
                                      "delta is about half the largest real one -- the "
                                      "flattering direction."
                                      % (sum_resid_156, sum_resid_234)),
            largest=largest_delta, smallest=smallest_delta),
        b_floor=dict(withdrawn_common_mode_statistic=withdrawn, differential_floor=diff_floor),
        d_per_bin=per_bin,
        d_scope=scope,
        perturbation=perturbation,
        e_tier=dict(
            tier="UNOBTANIUM-WITH-PARAMETERS",
            inherited_from="exp-061 (Iteration 38), MP-2/MP-4 CONFIRMED",
            binding_axis=("thickness: alpha_true ~ 5.74e4 cm^-1 is not an implausible "
                          "absorption rate, but the coating is asked to deliver it in 1.44 um "
                          "where real record-blackness CNT-forest coatings run 100-500 um -- a "
                          "70-350x gap, the dominant anchor-invariant falsification axis."),
            moved_by_this_finding=False,
            evidentiary_tier=("T18: every literature figure behind this tier is "
                              "WebSearch-snippet synthesis, NOT primary-source-verified "
                              "(WebFetch blocked at 41+ consecutive attempts as of exp-061). "
                              "This cycle attempts no new literature search and makes no new "
                              "realizability claim from new sources; the tier is CITED, not "
                              "re-derived."),
            forward_conditional=("IF a future cycle re-specs this article at exp-061's own "
                                 "MP-5-plausible thickness (230-730x of 1.44 um), the "
                                 "core/backing freedom survives and strengthens -- the bound "
                                 "scales as exp(-tau_true) (MF-1: exp(-tau), not exp(-2 tau)) "
                                 "and tau_true grows with thickness. Stated as a physical "
                                 "argument, explicitly NOT re-measured here."),
            thermal_counterweight=thermal_counterweight,
            open_caveat=("exp052-alpha-60nm-absorptivity-open still bites on 'thickness as the "
                         "binding constraint': the 60 nm absorptivity question is open."),
            constraint_scope=("Says NOTHING about constraints 3 or 4, about any T1 escape "
                              "route, or about any sigma(I)/sigma(x,t) mechanism. The article "
                              "FAILS CONSTRAINT 3 BY CONSTRUCTION (a perfect absorber is a "
                              "black shape in daylight -- LOGBOOK ESTABLISHED).")),
        headline=build_m9_bound_text(
            largest_delta, per_bin, diff_floor, scale, bound, status))


def build_m9_bound_text(largest_delta, per_bin, diff_floor, scale, bound, status):
    """M9(d) -- the one stated claim seven cycles have named and none has
    written, corrected per MF-1..MF-4 and MF-11. R21: this is the string
    the Result section quotes; MF-4 puts the constraint-3 failure, the
    realizability tier and the T18 evidentiary tier INSIDE it."""
    if status != "REPRODUCED":
        return ("NOT-REPRODUCED -- the sidecar's arithmetic reproduction gate failed; the "
                "bound is WITHHELD rather than published (M9's own pre-registered HALT).")
    return (
        "FABRICATION-TOLERANCE BOUND (analytic sidecar -- desk arithmetic over committed data, "
        "NOT an FDTD output of this cycle). For the graded_black_shell recipe at "
        "tau_shell = 24, eps_r == 1, lambda = 600 nm, plane-wave normal incidence, 2D TM, "
        "measured on this bench's NEAR-TO-MID-FIELD BOX LEDGER at its own measurement geometry "
        "(NOT a far-field pattern): replacing the core/backing over the entire inner radius, "
        "vacuum -> perfect electric conductor, moves the AGGREGATE cross-section channels by at "
        "most %.4e relative (two independent channels, sigma_scat and sigma_abs, and their "
        "exact algebraic sum sigma_ext -- not three), and moves the PER-BIN angular pattern, on "
        "the program's own floor-gated local-normalization instrument, by up to %.4e at r=156 "
        "(%d/%d bins resolved) and %.4e at r=312 (%d/%d resolved), with the two largest "
        "resolved r=312 deviations at +/-138.75 deg, INSIDE the observer-return hemisphere "
        "PANEL.md scores constraint 2 on. The per-bin half of any 'better than 1.6e-04' reading "
        "is WITHDRAWN. On the only differential floor on file (exp-108's six-margin item_ii "
        "family) the aggregate effect is RESOLVED at %.2fx (r=156) and %.2fx (r=312), NOT "
        "floor-limited; no differential floor exists at r=234 at all. The coating's own "
        "committed optical depth predicts a core-dependent cross-section change at the "
        "coherent-cross-term scale exp(-tau_true) = %.4e, upper bound 2 exp(-tau_true) = %.4e -- "
        "the SAME ORDER as the measured aggregate deltas, not orders below them. SCOPE: "
        "CERTIFIED AT MARGIN=32 ONLY for the tight per-bin figure (the other five margins are "
        "certified only by one boolean against a 5e-02 decision bar, 330x looser); per-bin "
        "evidence at cpl=20 only and aggregate evidence at cpl=25 only, so CHANNEL AND "
        "RESOLUTION ARE FULLY CONFOUNDED; r=234 contributes aggregate channels only. "
        "FABRICATION CONSEQUENCE, at that scope: over the vacuum-to-PEC range tested at 600 nm, "
        "normal incidence, 2D TM, a process implementing this design does not need to control "
        "the core/backing material to better than the ~1e-04 aggregate level -- and it does NOT "
        "license varying the backing without re-measuring the per-bin angular channel in the "
        "observer-return hemisphere, which moves by ~5 percent there. The optical function is "
        "carried entirely by a %.3f um (%.2f lambda) graded-sigma coating whose physical "
        "thickness is INVARIANT across r = 156/234/312 and cpl = 20/25. THIS ARTICLE FAILS "
        "CONSTRAINT 3 BY CONSTRUCTION (a perfect absorber is a black shape in daylight); the "
        "bound is a fabrication statement about the bench's workhorse article and MUST NOT be "
        "read as constraint-3 progress. REALIZABILITY TIER: UNOBTANIUM-WITH-PARAMETERS, "
        "inherited unchanged from exp-061 and driven by the 70-350x thickness gap; EVERY "
        "literature figure behind that tier is WebSearch-snippet synthesis, NOT "
        "primary-source-verified (T18)."
        % (largest_delta,
           per_bin["r156"]["max_floor_gated_local_rel"], per_bin["r156"]["n_resolved"],
           per_bin["r156"]["n_total"],
           per_bin["r312"]["max_floor_gated_local_rel"], per_bin["r312"]["n_resolved"],
           per_bin["r312"]["n_total"],
           diff_floor["r156"]["mean_over_std"], diff_floor["r312"]["mean_over_std"],
           scale, bound, SHELL_THICKNESS_UM, SHELL_THICKNESS_LAMBDA))


# ================================================================================
# DISCLAIMER_115 (MF-10) -- single source of truth, asserted on BOTH sides
# in committed, re-invocable call sites (R23 First Addendum).
# ================================================================================
DISCLAIMER_115 = (
    "This is an instrument-fidelity / governance cycle on the T28 sub-thread -- not a "
    "phenomenon-mechanism proposal and not a named-bin resolution-convergence "
    "classification. T1 escape route: NONE / N/A. No sigma(I)/sigma(x,t)/"
    "angular-selectivity/sub-threshold content, no Weber-contrast or C_thr(L) perceptual "
    "scoring, is performed anywhere in this document; none of PANEL.md's seven metric rows "
    "is recorded (see PANEL.md's Iteration-92 scope amendment). "
    "ANALYTIC SIDECAR, NOT FDTD: M9's fabrication-tolerance bound is desk arithmetic over "
    "already-committed results.json files plus one desk integral over lab/materials."
    "_graded_black -- it consumes zero FDTD calls, zero grid-steps and zero bench wall time "
    "on the timed path, and it is NOT an output of this cycle's own six timing readings. It "
    "carries a code-enforced arithmetic reproduction gate; any mismatch HALTs it and it is "
    "reported NOT-REPRODUCED rather than published. "
    "UPPER BOUND VS RESOLVED: the sidecar's per-bin channel figures are floor-GATED and "
    "resolved on exp-110's own local-normalization instrument; the aggregate channels are "
    "resolved at 4.47x/11.70x on exp-108's six-margin differential family, which is the ONLY "
    "differential floor this program has -- no differential floor exists at r=234, and the "
    "|sigma_ext - sigma_ext_cross| quantity the Phase-1 proposal used as a floor is WITHDRAWN "
    "(it is scene-independent and cancels exactly between the two scenes being differenced). "
    "The bound is certified at margin=32 only, with channel and resolution fully confounded. "
    "CONSTRAINT 3: the graded_black_shell article this bound describes FAILS CONSTRAINT 3 BY "
    "CONSTRUCTION -- a perfect absorber is a black shape in daylight (LOGBOOK ESTABLISHED) -- "
    "and nothing in this cycle is constraint-3 progress or a T1 escape route. "
    "EVIDENTIARY TIER (T18): every literature figure behind the UNOBTANIUM-WITH-PARAMETERS "
    "realizability tier is inherited from exp-061's WebSearch-snippet synthesis, NOT "
    "primary-source-verified; this cycle attempts no new literature search. "
    "ENERGY-LEDGER / THERMAL-SIDECAR: N/A THIS CYCLE, and the reason is physical, not "
    "clerical. geom_fixedabs_cpl sizes STEPS so each grid gets ~2 domain crossings at "
    "S = courant_frac/sqrt(2) = 0.2263 cells/step; the control bursts run 1000 and 3334 steps, "
    "so the wavefront reaches only ~65 percent of the r=156 domain and ~47 percent of the "
    "r=234 domain. A sigma_abs/sigma_ext ledger from fields that far from settled would be a "
    "WRONG NUMBER, not a free byproduct (T27 is this program's own paid-for lesson that a "
    "truncated run is not a small perturbation of a settled one) -- so PANEL.md's "
    "'Absorbed energy budget + predicted re-radiation' row, which exp-114 filled, is declared "
    "N/A here rather than silently dropped. "
    "SCORING SCOPE: G is a MACHINE PROPERTY, not a physics constant. M5 replicates exp-114's "
    "own scored statistic and can move a filed verdict; M6 tests machine transfer with N = 2 "
    "machines; M7 is descriptive. Pure cell-count (N^2) scaling is algebraically identical to "
    "the pre-R28 hardcoded exponent 3.0 and lands INSIDE the CONFIRM band at rel_dev = 0.0799, "
    "so a CONFIRM does NOT distinguish k = 3.2053 from k = 3.0. Two defensible protocol models "
    "put G on OPPOSITE sides of the CONFIRM ceiling; whenever MF-7(a)'s protocol-mismatch "
    "interval spans a band edge, M5 is reported BOUNDED-REPLICATION and may not move exp-114's "
    "LOGBOOK entry. The claim that this cycle 'resolves the v2 straddle' is WITHDRAWN: v2's "
    "construction contains no r=156 quantity and its second operand, an intra-r=234 "
    "production-vs-burst factor, is not measured here. "
    "R30/R32: N/A -- this cycle produces no discriminating statistic of that class. R31/R33: "
    "M5 is R33-immune BY CONSTRUCTION (no scored operand mixes sessions); M6 is explicitly a "
    "cross-machine comparison and is labelled one.")


def _m5_line(m5, interval):
    if m5 is None:
        return "Not yet scored (no bench readings on file)."
    caveat = interval is not None and interval.get("m5_protocol_caveat")
    verdict = M5_BOUNDED_REPLICATION if caveat else m5["verdict"]
    return ("G_sustained=%.7f, exponent_B=%.7f, measured_ratio=%.7f, reference_ratio=%.7f, "
            "rel_dev(ratio-space)=%.5f, verdict=%s"
            % (m5["g_sustained"], m5["exponent_B"], m5["measured_ratio"],
               m5["reference_ratio"], m5["rel_dev"], verdict))


def build_predictions_text():
    """R23 First Addendum: the predictions-side assert lives INSIDE this
    function, and `python run115.py --predictions-only` is its committed,
    re-invocable call site."""
    sens = sensitivities_do_not_score()
    s_short = sens["sensitivity_short_reading_DO_NOT_SCORE"]
    s_v2 = sens["sensitivity_v2_straddle_DO_NOT_SCORE"]
    m8_line = (
        "sensitivity_short_reading_DO_NOT_SCORE: measured_ratio = %.7f, rel_dev = %.8f "
        "(AMBIGUOUS). sensitivity_v2_straddle_DO_NOT_SCORE: measured_ratio = %.7f, SIGNED "
        "deviation %+.5f against the filed %+.5f -- opposite sides of reference_ratio, a "
        "%.1f%% spread between central estimates."
        % (s_short["measured_ratio"], s_short["rel_dev"], s_v2["measured_ratio"],
           s_v2["signed_dev"], s_v2["filed_signed_dev"],
           100.0 * s_v2["spread_between_central_estimates"]))
    n2_rel_dev = abs(KAPPA_RATIO * G_N2 - REFERENCE_RATIO) / REFERENCE_RATIO
    straddle_frac = 100.0 * ((V2_STRADDLE_BOUNDARY_G - G_CONFIRM_LO)
                             / (G_CONFIRM_HI - G_CONFIRM_LO))
    model_sep = 100.0 * abs(M7_CONST_EPS_G - M7_CONST_K_G) / M7_CONST_K_G
    text = f"""PREDICTIONS (pre-registered, exp-115, Panel Iteration 92)
Runner: bench panel shift (T5820) -- Director Clyde, live session.

{DISCLAIMER_115}

**Geometry identity (zero-FDTD, pre-Phase-4)**: verify_geometry_identity()
returns pass_=True at r=156, r=234 AND r=312 -- geom_fixedabs_cpl(r, cpl=20)
must reduce to R110.geom_fixedabs(r) exactly at all three. Falsified by any
mismatch -- HALT before any Sim.run() call.

**MF-12 absolute identity gate on the new machinery (zero-FDTD, pre-reading)**:
chunk_runner115.py's parameterized _time_control_blend(r, ...) at r=156 must
construct a scene set IDENTICAL to chunk_runner114.py's own hardcoded
_time_control_blend() -- same geometry dict field-for-field, same three scenes
in the same order, same SHORT/SUSTAINED step constants, and a build_sim source
segment byte-identical to chunk_runner114.py's. Falsified by any difference --
HALT before any reading is trusted. The trust suite is re-run ON THE BENCH and
its console record committed (VALIDATION.md docket-14: a reproducibility claim
that does not name its platform is not a gate).

**Block CG -- six readings, {N_SIM_RUN_CALLS_FULL} Sim.run() calls, {2*GRID_STEPS_PER_GRID} grid-steps**
({GRID_STEPS_PER_GRID} per grid), in the order {', '.join(READING_ORDER)}. The
sustained pass is ABBA (MF-6a), not ABAB: under ABAB both sustained pairs
inherit the same-signed (a+b)/2 lag while d_rep reads ~0 -- an alarm
structurally incapable of producing the reading that means "bad".
G_sustained is the MEAN of the two pairwise G values, both persisted.
Same-grid drift is reported as a RATE PER UNIT ELAPSED TIME, because ABBA
makes the two same-grid lags unequal (a+2b vs b). Exclusive use of the bench
is enforced for the duration of the readings; a machine-state block is
persisted with each reading.

**M1 `G_short` / M2 `G_sustained`** -- descriptive; M2 is the operand M5/M6/M7
score. No advance position is taken on which band any metric lands in.

**M3 -- is `G` duration-invariant? (MECHANISM-NEUTRAL labels, MF-9)**
| Outcome | Condition |
|---|---|
| {M3_LABEL_INVARIANT} | d_dur <= R_DEG/2 = {M3_INVARIANT_BAR:.7f} |
| {M3_LABEL_PARTIAL} | between |
| {M3_LABEL_NOT_INVARIANT} | d_dur >= R_DEG = {M3_NOT_INVARIANT_BAR:.7f} |
Anchor (R17): R_DEG = {R_DEG:.7f} is exp-114's own measured single-grid
(r=156) 1000->3334 steps/scene shift, the largest comparable on file. The
labels name no mechanism because the mechanism is unvalidated AND
contradicted in sign on file: R_DEG is +7.596% (longer = slower) while
exp-114's own intra-r=234 first-3000-vs-full reading is -4.467% (longer =
faster), and run_control() runs short-then-sustained with no counterbalance,
so R_DEG conflates duration with elapsed session position by construction.

**M4 -- drift+noise (MF-6d: under ABBA this is NOT a repeatability statistic)**
| Outcome | Condition | Consequence carried in the label |
|---|---|---|
| REPEATABLE | d_rep <= {M4_REPEATABLE_BAR:.2f} | M3 scored, M7 powered |
| MARGINAL-M3-SCORED-M7-POWERED | <= {M7_POWER_BAR:.2f} | |
| MARGINAL-M3-SCORED-M7-UNDERPOWERED | <= {M3_INVARIANT_BAR:.7f} | |
| MARGINAL-M3-UNSCORED-M7-UNDERPOWERED | < {M4_NOISY_BAR:.7f} | |
| NOISY-M3-UNSCORED-M7-UNDERPOWERED | >= {M4_NOISY_BAR:.7f} | |
Coded booleans, all persisted (MF-9): m3_scored = (not repeat_skipped) and
(d_rep <= R_DEG/2); m5_protocol_caveat; m6_directional_only = (m3_verdict !=
"{M3_LABEL_INVARIANT}"); m7_underpowered. If the budget gate skips the repeat
pass, repeat_skipped=True is persisted with its reason, M4 reports UNMEASURED,
m3_scored is False, and the R19 call-count assert expects
{N_SIM_RUN_CALLS_REPEAT_SKIPPED} calls instead of {N_SIM_RUN_CALLS_FULL}.

**M5 -- PRIMARY: bench replication of exp-114's own scored statistic**
Scored by exponent_B = ln(1.5*G_sustained)/ln(1.5) fed to R114's own
committed classify_kappa_exponent_check(), UNMODIFIED, with a code-assert
that |measured_ratio - 1.5*G_sustained| < 1e-12 (MF-5 -- passing
measured_ratio directly, as the Phase-1 document's own text says, evaluates
1.5**(1.5*G) and returns rel_dev = 0.4480 -> a false REFUTE on exp-114's own
filed value).
| Outcome | Condition | Exact boundary in G |
|---|---|---|
| CONFIRM | rel_dev <= {KAPPA_EXPONENT_CONFIRM_REL:.2f} | G in [{G_CONFIRM_LO:.7f}, {G_CONFIRM_HI:.7f}] |
| AMBIGUOUS | between | |
| REFUTE | rel_dev >= {KAPPA_EXPONENT_REFUTE_REL:.2f} | G <= {G_REFUTE_LO:.7f} or G >= {G_REFUTE_HI:.7f} |

**M5's stated power limit, pre-registered (MF-7)**. (b) Pure N^2 (cell-count)
scaling gives G = {G_N2:.2f} exactly, i.e. k = {K_N2:.1f} EXACTLY -- the pre-R28
hardcoded exponent -- and rel_dev = {n2_rel_dev:.4f}, INSIDE the CONFIRM band. A
CONFIRM therefore does NOT distinguish k = {KAPPA_COST_EXPONENT:.4f} from k = 3.0;
the entire hypothesis space between the two competing exponents is ~8% wide and
the CONFIRM band is 15% wide. (c) Two defensible protocol models, both on file,
predict G on OPPOSITE sides of the CONFIRM ceiling ({G_CONFIRM_HI:.7f}):
  - drift/degradation model (R_DEG extrapolated log-linearly from 1000->3334 to
    3334->12000, factor {PROTOCOL_MODEL_DRIFT_FACTOR:.5f}): G ~ {PROTOCOL_MODEL_DRIFT_G:.4f} -- comfortable CONFIRM
  - warm-up-amortization model (exp-114's own r=234 first-3000-steps rate against
    its own 12000-step average): G ~ {PROTOCOL_MODEL_WARMUP_G_SCENE_MATCHED:.4f} (scene-matched) to {PROTOCOL_MODEL_WARMUP_G_BLEND:.4f}
    (blend-denominator) -- ABOVE the ceiling, i.e. AMBIGUOUS
  The span is ~13%, comparable to M5's entire CONFIRM half-width. These two
  models' inputs include exp-114's three r=234 chunk times, which survive only
  as quotations and are NOT independently re-derivable -- directional, cited.
(a) A protocol-mismatch INTERVAL is persisted from the two-point
p(n) = p_inf + C_g/n relation on each grid (S and U are the two points, so it
is exactly determined -- it BOUNDS, it does not fit, R7). If the interval
spans a band boundary, m5_protocol_caveat=True is persisted and M5 is reported
{M5_BOUNDED_REPLICATION} -- NOT a verdict that can move exp-114's LOGBOOK entry.

**M6 -- cross-machine transfer of G**: T = G_sustained/G_E, G_E = {G_E:.8f}.
TRANSFERS if |T-1| <= {M6_TRANSFERS_BAR:.7f} (R28's own founding-miss
magnitude, reused in the same ratio space); DOES-NOT-TRANSFER if
|T-1| >= {M6_NO_TRANSFER_BAR:.7f}. m6_directional_only is True unless M3 reads
{M3_LABEL_INVARIANT} -- MF-9 INVERTS the Phase-1 rule so PARTIAL, UNSCORED and
repeat-skipped all INHERIT the caveat instead of escaping it. This cycle does
NOT claim to resolve the v2 straddle (MF-8): v2's construction contains no
r=156 quantity, and over {straddle_frac:.1f}% of M5's own CONFIRM band the cycle
would return "CONFIRM, replicated" with the straddle still open (sign boundary
at G >= {V2_STRADDLE_BOUNDARY_G:.7f}).

**M7 -- the N^2 assumption, TWO-SIDED labels (MF-9/RT-14)**: excess =
G_sustained/{G_N2:.2f} - 1. N2_HOLDS if |excess| <= {M7_HOLDS_BAR:.2f};
N2_FAILS-SUPERLINEAR if excess >= {M7_FAILS_BAR:.9f}; N2_FAILS-SUBLINEAR if
excess <= -{M7_FAILS_BAR:.9f} (sub-cell-count scaling is the OPPOSITE finding
and must not inherit the positive branch's meaning). Note, computed before any
bench data: N2_HOLDS requires BOTH candidate cost models to be wrong -- the
in-force constant-k model predicts excess = {M7_CONST_K_G/G_N2 - 1.0:.5f} (AMBIGUOUS) and the
constant-eps model predicts excess = {M7_CONST_EPS_G/G_N2 - 1.0:.15f}, bit-adjacent to the
N2_FAILS bar. The two models differ by only {model_sep:.3f}%, so the comparison is
reported UNDERPOWERED and NOT scored whenever d_rep > {M7_POWER_BAR:.2f}. VISION's identity
is carried forward: eps_E/eps_k == G_E/G_ref == measured_ratio/reference_ratio,
so M5 and M7's secondary comparison are ONE datum wearing two hats.

**M8 -- persisted, NOT-scored sensitivities (Tier-1 item 2)**:
{m8_line} A third,
sensitivity_v2_with_measured_G_DO_NOT_SCORE, is added once G is measured
(OV-1: the SCORED half of QUANTUM's M10 is DECLINED -- scoring it would
presume the machine-independence M6 exists to test).

**M9 -- fabrication-tolerance bound (ANALYTIC SIDECAR, no blind prediction)**.
Its falsifiable element is a code-enforced arithmetic reproduction gate: every
cited figure is recomputed in analyze115.py from its source results.json and
asserted equal to <1e-12 relative, and tau_true is recomputed from
lab/materials._graded_black at BOTH family members and must reproduce
{TAU_TRUE_FILED} to <{100*TAU_TRUE_REPRO_REL_BAR:.0f}%. Any mismatch HALTs the
sidecar, which is then reported NOT-REPRODUCED rather than published. The
sidecar's PHYSICS is stated in its corrected functional form BEFORE the run
(MF-1): the core-dependent contribution to a cross-section is the COHERENT
CROSS TERM, scale exp(-tau_true), upper bound 2*exp(-tau_true) -- NOT
exp(-2*tau_true), which is the |dA|^2 term only and is wrong by exp(+tau_true)
~ 3.86e3.

**Budget gate (R27/R28, executable, upstream of every Sim.run)**: reuses
R110.COST_GATE_TOTAL_S = {COST_GATE_TOTAL_S} and COST_GATE_SAFETY_MARGIN =
{COST_GATE_SAFETY_MARGIN} unmodified, re-projecting after S156 (G_prior = G_E),
after S234 (measured G_short), and after U234 (the repeat pass). Graceful
degradation at BOTH ends (Red Team's recommended-not-mandatory branch,
ADOPTED and disclosed): a breach spends the REPEAT first (repeat_skipped=True
with its reason persisted); if even the primary sustained pass would breach,
SUSTAINED_CONTROL_STEPS steps DOWN to the largest value that fits and
sustained_steps_used is persisted with a flag. Only if no value at or above
{SHORT_CONTROL_STEPS} steps/scene fits does the gate raise.

**Declined this cycle, numbered (R25)**: phase1_proposal.md Sec 3 items 1-7,
plus --
{DECLINE_8}
"""
    assert DISCLAIMER_115 in text, "R23 First Addendum: predictions-side assert"
    return text


def build_result_text(readings_summary, n_sim_run_calls, total_wall_s, geom_ok,
                      identity_gate_ok, m1=None, m2=None, m3=None, m4=None, m5=None,
                      m6=None, m7=None, protocol_interval=None, drift=None,
                      sidecar=None, repeat_skipped=False, sustained_steps_used=None,
                      machine_state=None):
    """R23 First Addendum: the RESULT-side assert lives INSIDE this
    function, and it has TWO committed, re-invocable call sites in this
    same cycle -- `python run115.py --selftest` (synthetic operands, runs
    now, at Phase 3) and analyze115.py (real operands, at Phase 4). The
    founding defect this addendum was written for was precisely a
    result-side builder that no committed script ever invoked."""
    sidecar_line = ("Not computed." if sidecar is None
                    else "%s\n\n%s" % (sidecar["status"], sidecar["headline"]))
    lines = [
        "RESULT (exp-115, Panel Iteration 92)",
        "Runner: bench panel shift (T5820) -- Director Clyde, live session.",
        "",
        DISCLAIMER_115,
        "",
        ("%d real FDTD calls (Sim.run), %.1fs (%.2f min) total wall time this cycle, "
         "zero `lab/` diff." % (n_sim_run_calls, total_wall_s, total_wall_s / 60.0)),
        ("R19 call-count invariant: expected %d (repeat_skipped=%s), got %d."
         % (N_SIM_RUN_CALLS_REPEAT_SKIPPED if repeat_skipped else N_SIM_RUN_CALLS_FULL,
            repeat_skipped, n_sim_run_calls)),
        "**Geometry identity: %s.**" % ("PASS" if geom_ok else "FAIL"),
        "**MF-12 absolute identity gate on the new machinery: %s.**"
        % ("PASS" if identity_gate_ok else "FAIL"),
        "**SUSTAINED_CONTROL_STEPS used: %s** (nominal %d)."
        % (sustained_steps_used if sustained_steps_used else SUSTAINED_CONTROL_STEPS,
           SUSTAINED_CONTROL_STEPS),
        "",
        "**Readings (ABBA sustained pass, MF-6a):** %s" % json.dumps(readings_summary, default=str),
        "**M1 G_short:** %s" % ("n/a" if m1 is None else "%.7f" % m1),
        "**M2 G_sustained (mean of the two pairwise G, both persisted):** %s"
        % ("n/a" if m2 is None else "%.7f" % m2),
        "**M3 (mechanism-neutral):** %s" % ("n/a" if m3 is None
                                            else "d_dur=%.6f, %s" % (m3["d_dur"], m3["verdict"])),
        "**M4 (drift+noise under ABBA):** %s"
        % ("n/a" if m4 is None else "d_rep=%s, %s"
           % ("UNMEASURED" if m4["d_rep"] is None else "%.6f" % m4["d_rep"], m4["verdict"])),
        "**M5 PRIMARY:** %s" % _m5_line(m5, protocol_interval),
        "**M5 protocol-mismatch interval (MF-7a):** %s"
        % ("n/a" if protocol_interval is None
           else "G in [%.7f, %.7f], m5_protocol_caveat=%s"
                % (protocol_interval["interval_lo"], protocol_interval["interval_hi"],
                   protocol_interval["m5_protocol_caveat"])),
        "**M6:** %s" % ("n/a" if m6 is None else "T=%.6f, %s, directional_only=%s"
                        % (m6["T"], m6["verdict"], m6["m6_directional_only"])),
        "**M7:** %s" % ("n/a" if m7 is None else "excess=%+.6f, k_B=%.6f, %s (model comparison: %s)"
                        % (m7["excess"], m7["k_B"], m7["verdict"],
                           m7["model_comparison"]["favoured"])),
        "**Same-grid drift rate per unit elapsed time (MF-6c):** %s" % json.dumps(drift, default=str),
        "**Machine state (MF-6e):** %s" % json.dumps(machine_state, default=str),
        "",
        "**M9 -- fabrication-tolerance bound (ANALYTIC SIDECAR, R21: stated here, not merely "
        "persisted):** %s" % sidecar_line,
        "",
        "**What this cycle does NOT establish:** anything about kappa_ratio other than 1.5; "
        "k's portability to kappa_ratio = 2.0 still rests on the single founding pair, and to "
        "ratios above 2.0 on nothing at all. A CONFIRM here does not license extrapolation "
        "past 2.0, and does not distinguish k = 3.2053 from k = 3.0.",
    ]
    text = "\n".join(lines) + "\n"
    assert DISCLAIMER_115 in text, "R23 First Addendum: result-side assert"
    return text


# ================================================================================
def _selftest():
    """Committed, re-invocable Phase-3 verification. Exercises the
    MF-5 route against exp-114's own filed value, the result-side
    DISCLAIMER_115 assert, and the sidecar's own reproduction gate --
    all with zero FDTD."""
    ok = True
    m5 = classify_m5(G_E)
    print("MF-5 self-test: classify_m5(G_E=%.14f)" % G_E)
    print("  exponent_B      = %.15f  (exp-114 filed exponent_234 = %.15f)"
          % (m5["exponent_B"], EXP114_RESULTS["kappa_exponent_result"]["exponent_234"]))
    print("  measured_ratio  = %.14f  (filed %.14f)"
          % (m5["measured_ratio"], EXP114_RESULTS["kappa_exponent_result"]["measured_ratio"]))
    print("  rel_dev         = %.17f  (filed %.17f)"
          % (m5["rel_dev"], EXP114_RESULTS["kappa_exponent_result"]["rel_dev"]))
    filed = EXP114_RESULTS["kappa_exponent_result"]["rel_dev"]
    if abs(m5["rel_dev"] - filed) > 1e-9:
        print("  FAIL: does not reproduce exp-114's filed rel_dev to 1e-9")
        ok = False
    else:
        print("  PASS: reproduces exp-114's filed rel_dev=0.12275 to <1e-9 (delta %.3e)"
              % abs(m5["rel_dev"] - filed))
    # The failure mode MF-5 exists to prevent, demonstrated (not scored):
    wrong = R114.classify_kappa_exponent_check(KAPPA_RATIO * G_E)
    print("  MF-5 counterfactual (passing measured_ratio directly, as the Phase-1 text said): "
          "rel_dev=%.17f -> %s" % (wrong["rel_dev"], wrong["verdict"].split(" ")[0]))

    print("\nR23 First Addendum: result-side call site")
    txt = build_result_text(readings_summary={"selftest": True}, n_sim_run_calls=0,
                            total_wall_s=0.0, geom_ok=True, identity_gate_ok=True)
    print("  build_result_text() invoked; DISCLAIMER_115 present = %s" % (DISCLAIMER_115 in txt))
    ptxt = build_predictions_text()
    print("  build_predictions_text() invoked; DISCLAIMER_115 present = %s"
          % (DISCLAIMER_115 in ptxt))

    print("\nM9 sidecar reproduction gate")
    sc9 = sidecar_m9()
    for c in sc9["reproduction_checks"]:
        print("  %-52s %s (rel %.3e)" % (c["name"], "OK" if c["ok"] else "FAIL", c["rel"]))
    print("  sidecar status: %s" % sc9["status"])
    if sc9["status"] != "REPRODUCED":
        ok = False
    print("\nSELFTEST %s" % ("PASSED" if ok else "FAILED"))
    return 0 if ok else 1


if __name__ == "__main__":
    if "--predictions-only" in sys.argv:
        print(build_predictions_text())
    elif "--verify-geometry" in sys.argv:
        result = verify_geometry_identity()
        print(json.dumps(result, indent=2))
        assert result["pass_"], "geom_fixedabs_cpl does not reduce to R110.geom_fixedabs at cpl==20"
        print("verify_geometry_identity: PASS (r=156, 234, 312)")
    elif "--selftest" in sys.argv:
        raise SystemExit(_selftest())
    else:
        print("This module holds shared constants and pure classification/sidecar functions "
              "only -- no Sim.run() call anywhere in this file. "
              "Modes: --predictions-only | --verify-geometry | --selftest")
