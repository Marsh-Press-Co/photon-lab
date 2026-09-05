"""exp-112 -- Panel Iteration 89 (candidate), QUANTUM OPTICS' rotation-lead
cycle: PHOTONICS' own cpl-refinement floor spot-check (Reconciled
Iteration-89 queue, LOGBOOK.md Iteration 88 / experiments/111-.../
phase5_redteam_audit.md Sec 8), deferred twice (exp-110 Sec "Item 3
scoping decision", exp-111 phase1_proposal.md Sec 3), executed here for
the first time: does the -146.25deg bin (r=156, margin=32/box_a, bin
index 4 of 48 -- exp-108/110's own committed named bin) reflect genuine
sub-wavelength field structure or Yee-grid discretization noise?

This module holds ONLY shared geometry/classification code -- no
Sim.run() call anywhere in this file. Reuses experiments/110-.../run.py
(imported as R, unmodified -- classify_item_i_local, mirror_pooled_floor,
cost_gate_check, COST_GATE_PILOT_S/TOTAL_S, geom_fixedabs, CPL_600, and
every named geometry constant) and lab/sections.py (unmodified) by direct
import, per this cycle's own Phase-1 discipline: reuse existing modules
by import, never copy-paste.

Congruent cpl-resolution-refinement convention: this program's own
established idiom for a cpl refinement (experiments/069-t21-block-mini-
period-match-power-up/design_geometry.py's own R3_RATIO/R4_RATIO family,
R3/R11 discipline) scales EVERY cell-count geometry quantity by
ratio=cpl_new/cpl_old, and sigma_max by 1/ratio (holding the shell's
optical thickness tau_shell constant) -- NOT a "hold geometry-in-cells
fixed, change cpl alone" construction, which would silently change the
object's ELECTRICAL size rather than its GRID RESOLUTION. This is the
FIRST application of that convention to the fixedabs family
(experiments/106/108/110's own hollow-vs-PEC-cored geometry, distinct
from the T21/Block-MINI family that convention was built for) --
geom_fixedabs_cpl() below is the generalization, verified byte-exact to
R.geom_fixedabs() at cpl==R.CPL_600 by verify_geometry_identity() (a
zero-FDTD, R6-style ground-truth-recovery check, executed and reported in
this document's own phase1_proposal.md Sec 2.0, and re-runnable here).
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "experiments", "110-t28-item-i-local-norm-and-controls"))

from lab import sections as sc  # noqa: E402
import run as R  # noqa: E402  (experiments/110-.../run.py -- reused unmodified)

EXP110_DIR = os.path.join(ROOT, "experiments", "110-t28-item-i-local-norm-and-controls")
with open(os.path.join(EXP110_DIR, "results.json")) as f:
    EXP110_RESULTS = json.load(f)

# ================================================================ this cycle's own scope
R_THIS_CYCLE = 156                 # r=156-alone-first (exp-111's own recommendation)
CPL_BASELINE = R.CPL_600           # 20
CPL_TARGET = 25                    # this cycle's own resolution target
CPL_RATIO = CPL_TARGET / CPL_BASELINE   # 1.25
NAMED_BIN_DEG = -146.25            # the bin at r=156 PHOTONICS named (exp-108 Phase-5)
MARGIN = 32                        # box_a -- the margin the named bin was flagged at

# Baseline (cpl=20) reference figures, read back from exp-110's own committed
# results.json -- NOT hand-typed (R4 discipline).
_BASELINE_R156 = EXP110_RESULTS["r156"]
BASELINE_BIN_CENTERS_DEG = _BASELINE_R156["bin_centers_deg"]
assert len(BASELINE_BIN_CENTERS_DEG) == 48, "expected 48 angular bins"
NAMED_BIN_IDX = int(np.argmin(np.abs(np.array(BASELINE_BIN_CENTERS_DEG) - NAMED_BIN_DEG)))
assert abs(BASELINE_BIN_CENTERS_DEG[NAMED_BIN_IDX] - NAMED_BIN_DEG) < 1e-9, (
    "named bin must sit exactly on a bin center at cpl=20 (it does: -146.25 == "
    "BIN_CENTERS_DEG[4], confirmed against exp-110's own committed results.json)")

_BASELINE_MARGIN32 = _BASELINE_R156["raw_patterns"][str(MARGIN)]
BASELINE_PECCORED = _BASELINE_MARGIN32["peccored"][NAMED_BIN_IDX]
BASELINE_HOLLOW = _BASELINE_MARGIN32["hollow"][NAMED_BIN_IDX]
BASELINE_DELTA = _BASELINE_MARGIN32["delta"][NAMED_BIN_IDX]
_BASELINE_LOCAL = _BASELINE_R156["local_diag"][str(MARGIN)]
BASELINE_FLOOR = _BASELINE_LOCAL["floor"]
BASELINE_SNR_PECCORED = _BASELINE_LOCAL["local_snr_peccored"][NAMED_BIN_IDX]
BASELINE_SNR_HOLLOW = _BASELINE_LOCAL["local_snr_hollow"][NAMED_BIN_IDX]
BASELINE_RESOLVED = _BASELINE_LOCAL["resolved"][NAMED_BIN_IDX]
BASELINE_LOCAL_REL = abs(BASELINE_DELTA) / abs(BASELINE_PECCORED)   # ~9.88%, re-derived not hand-typed


def kappa_of(r):
    return R.kappa_of(r)


def geom_fixedabs_cpl(r, cpl):
    """Congruent cpl-resolution generalization of R.geom_fixedabs(r).
    Reduces to it EXACTLY when cpl == R.CPL_600 -- see
    verify_geometry_identity(), below. Every cell-count quantity scales by
    ratio = cpl / R.CPL_600; sigma_max scales by 1/ratio (tau_shell
    invariant). Returns a superset of R.geom_fixedabs()'s own fields, plus
    'absorb'/'edge'/'cpl'/'ratio' (needed by chunk_runner.py's build_sim,
    since R.ABSORB/R.EDGE are module constants in the cpl=20-only original,
    not part of its returned dict)."""
    ratio = cpl / R.CPL_600
    k = kappa_of(r)
    N = round(R.N0 * k * ratio)
    CX = round(R.CX0 * k * ratio)
    CY = round(R.CY0 * k * ratio)
    SRC_X = round(R.SRC_X0 * k * ratio)
    STEPS = round(R.STEPS0 * k * ratio)
    R_COAT = round(r * ratio)
    abs_thickness = round(R.ABS_THICKNESS * ratio)
    R_CORE = R_COAT - abs_thickness
    absorb = round(R.ABSORB * ratio)
    edge = round(R.EDGE * ratio)
    sigma_max = R.SIGMA_MAX_FIXED / ratio
    tau_shell = sigma_max * (R_COAT - R_CORE)
    box_a_hw = R_COAT + round(R.BOX_A_MARGIN0 * k * ratio)
    box_a = (CX - box_a_hw, CX + box_a_hw, CY - box_a_hw, CY + box_a_hw)
    ref = (CX, CY, round(R.REF_HH0 * k * ratio))
    return dict(r=r, cpl=cpl, ratio=ratio, k=k, N=N, CX=CX, CY=CY, SRC_X=SRC_X, STEPS=STEPS,
                R_CORE=R_CORE, R_COAT=R_COAT, sigma_max=sigma_max, tau_shell=tau_shell,
                absorb=absorb, edge=edge, box_a=box_a, ref=ref, family="fixedabs_cpl")


def verify_geometry_identity():
    """Zero-FDTD ground-truth-recovery check (R6 discipline, applied to a
    genuinely new instrument's own construction, not a fitted estimator --
    the closest available analogue here): geom_fixedabs_cpl(r, R.CPL_600)
    must reproduce R.geom_fixedabs(r) EXACTLY, field-for-field, at both
    r this program has ever used this family at. Run and reported in
    phase1_proposal.md Sec 2.0 (pre-Phase-4); re-run here as a hard
    assertion so Phase 4 halts before any Sim.run() call if this file's
    own generalization has drifted from the function it must reduce to."""
    shared = ("N", "CX", "CY", "SRC_X", "STEPS", "R_CORE", "R_COAT",
              "sigma_max", "tau_shell", "box_a", "ref")
    mismatches = []
    for r in (156, 312):
        g_new = geom_fixedabs_cpl(r, R.CPL_600)
        g_old = R.geom_fixedabs(r)
        if g_new["absorb"] != R.ABSORB:
            mismatches.append((r, "absorb", g_new["absorb"], R.ABSORB))
        if g_new["edge"] != R.EDGE:
            mismatches.append((r, "edge", g_new["edge"], R.EDGE))
        for field in shared:
            if g_new[field] != g_old[field]:
                mismatches.append((r, field, g_new[field], g_old[field]))
    return dict(pass_=(len(mismatches) == 0), mismatches=mismatches)


# ================================================================ cost gate (R27/R28, reused verbatim -- not redefined)
# This cycle's own r=156 leg is cheap (predicted ~1469s/24.5min total,
# see phase1_proposal.md Sec 2.0/cpl_cost_table.py) and needs no gate of
# its own to be affordable. R.cost_gate_check() is reused UNCHANGED for a
# different, forward-looking purpose: deciding whether a FUTURE cycle may
# expand this same cpl=25 leg to r=312, exactly the decision
# R.cost_gate_check() was built for (it is cpl-agnostic -- it only reads
# a kappa_ratio=r312/r156 and an empirically-fit wall-time exponent, both
# independent of which cpl the pilot itself was run at). This cycle does
# NOT call it for real (no r=312 Sim.run() is attempted here) -- reported
# in phase1_proposal.md Sec 2.0 as a PRE-REGISTERED projection using the
# cpl=25 pilot total from cpl_cost_table.py's own regenerated estimate,
# disclosed as a projection-of-a-projection until real r=156/cpl=25 data
# exists.
COST_GATE_PILOT_S = R.COST_GATE_PILOT_S
COST_GATE_TOTAL_S = R.COST_GATE_TOTAL_S


def cost_gate_check_for_r312_expansion(pilot_empty_wall_s, pilot_total_wall_s):
    """Thin, disclosed wrapper around R.cost_gate_check() (reused
    unmodified) -- the gate a FUTURE cycle must clear before spending on
    r=312 at cpl=25. Not invoked for real this cycle (chunk_runner.py's
    own guard raises before reaching this if r=156/cpl=25 is not yet
    complete)."""
    return R.cost_gate_check(pilot_empty_wall_s, pilot_total_wall_s)


# ================================================================ this cycle's own classification (the genuinely uncertain question)
SNR_K1 = 1.0           # "clears even the unmultiplied floor" bar, PHOTONICS' own
                       # exp-110 Phase-5 bimodal-gap finding (RESOLVED pop: snr>=1.32
                       # everywhere; UNRESOLVED pop: snr<=0.79 everywhere -- no bin
                       # anywhere near the K=3=MIRROR_FLOOR_K cutoff)
COLLAPSE_REL = 0.10   # order-of-magnitude-collapse bar, reused from this program's
                       # own founding T28 R3 standard (exp-069: "sign-flip/order-of-
                       # magnitude collapse", i.e. new/old < 0.1 or a sign flip)
SURVIVE_REL_LO = 0.10
SURVIVE_REL_HI = 10.0


def classify_resolution_check(delta_cpl25, peccored_cpl25, hollow_cpl25,
                               local_diag_cpl25_at_idx):
    """Applies this cycle's own pre-registered PASS/FAIL/INCONCLUSIVE bands
    (phase1_proposal.md Sec 2, falsification table) to a fresh cpl=25
    reading at the named bin. Two independent, complementary checks (per
    this proposal's own reasoning: neither alone is decisive):

    Check A (primary -- reuses classify_item_i_local's own K=3/median
    mirror-pooled-floor instrument, UNMODIFIED, at the new resolution):
    does the named bin's own local_snr improve enough to newly clear even
    the K=1 floor (SNR_K1), the bar PHOTONICS' own exp-110 Phase-5 review
    found cleanly separates the RESOLVED and UNRESOLVED populations at
    cpl=20?

    Check B (supplementary -- this program's own founding T28 R3 standard,
    exp-069): does delta[idx] keep the same sign and stay within one
    order of magnitude of its cpl=20 value?
    """
    snr_p_new = local_diag_cpl25_at_idx["local_snr_peccored"]
    snr_h_new = local_diag_cpl25_at_idx["local_snr_hollow"]
    resolved_new = local_diag_cpl25_at_idx["resolved"]

    snr_p_improved = (snr_p_new is not None) and (snr_p_new > BASELINE_SNR_PECCORED)
    snr_h_improved = (snr_h_new is not None) and (snr_h_new > BASELINE_SNR_HOLLOW)
    clears_k1_new = (snr_p_new is not None and snr_h_new is not None
                      and snr_p_new >= SNR_K1 and snr_h_new >= SNR_K1)

    if clears_k1_new:
        check_a = "SURVIVES (newly clears K=1 floor -- candidate real structure)"
    elif not (snr_p_improved or snr_h_improved):
        check_a = "COLLAPSES (no improvement in local_snr under refinement -- noise-consistent)"
    else:
        check_a = "AMBIGUOUS (some local_snr improvement, still below K=1)"

    same_sign = (np.sign(delta_cpl25) == np.sign(BASELINE_DELTA)) if BASELINE_DELTA != 0 else None
    rel_to_baseline = abs(delta_cpl25) / abs(BASELINE_DELTA) if BASELINE_DELTA != 0 else float("inf")
    if (not same_sign) or rel_to_baseline < COLLAPSE_REL:
        check_b = "COLLAPSES (sign flip or >=1 order-of-magnitude drop vs. cpl=20)"
    elif SURVIVE_REL_LO <= rel_to_baseline <= SURVIVE_REL_HI and same_sign:
        check_b = "SURVIVES (same sign, within 1 order of magnitude of cpl=20)"
    else:
        check_b = "AMBIGUOUS"

    return dict(check_a=check_a, check_b=check_b,
                snr_p_new=snr_p_new, snr_h_new=snr_h_new, resolved_new=resolved_new,
                same_sign=bool(same_sign) if same_sign is not None else None,
                rel_to_baseline=rel_to_baseline)


# ================================================================ predictions/result text (R23 -- single source of truth)
DISCLAIMER = ("This is an instrument-fidelity/resolution-convergence check on "
              "an angular-scattering-pattern noise floor, not a phenomenon-"
              "mechanism proposal -- no sigma(I)/sigma(x,t)/angular-selectivity/"
              "sub-threshold content, no Weber-contrast or C_thr(L) perceptual "
              "scoring, is performed anywhere in this document. 'Coherent "
              "sub-wavelength structure', as used here, means spatially "
              "deterministic classical field structure, not quantum "
              "coherence -- no non-classical or state-dependent mechanism is "
              "proposed, varied, or required. The congruent cpl-resolution-"
              "refinement construction (geom_fixedabs_cpl) is verified "
              "byte-exact to the cpl=20 baseline geometry at cpl==20 "
              "(verify_geometry_identity), but this is the FIRST application "
              "of that construction to the fixedabs family -- a single new "
              "resolution point (cpl=25) relative to the cpl=20 baseline can "
              "rule out a sign-flip/order-of-magnitude collapse but CANNOT "
              "establish full continuum convergence (R15's own two-point "
              "caution): a third, differently-scaled resolution point would "
              "be needed for that stronger claim, not proposed this cycle. "
              "This leg tests r=156 alone -- the +168.75deg bin at r=312 "
              "remains untested, deferred pending this cycle's own gate "
              "(Sec 2.0) and Phase-4 outcome.")


def build_predictions_text():
    return f"""PREDICTIONS (pre-registered, exp-112, Panel Iteration 89)

{DISCLAIMER}

**Geometry identity (zero-FDTD, pre-Phase-4)**: verify_geometry_identity()
returns pass_=True at both r=156 and r=312 (geom_fixedabs_cpl(r, cpl=20)
byte-exact to R.geom_fixedabs(r)). Falsified by any mismatch -- HALT
before any Sim.run() call.

**Reproduction/self-consistency precondition**: sum(sigma_scat_per_bin) ==
sigma_scat (from sections.widths(), same box -- angular_scattered_pattern's
own docstring identity) to <1e-9 relative, at margin=32, both peccored and
hollow captures, r=156, cpl=25. Falsified by any larger deviation -- HALT
before the named-bin comparison is trusted.

**Named bin (-146.25deg, r=156, margin=32, bin index {NAMED_BIN_IDX}) --
the genuinely uncertain question this leg exists to answer**:
Check A (mirror-pooled-floor instrument, reused unmodified, at cpl=25):
SURVIVES if local_snr_peccored AND local_snr_hollow both clear {SNR_K1}
(the K=1 bar cleanly separating exp-110's own RESOLVED/UNRESOLVED
populations); COLLAPSES if neither local_snr improves over its cpl=20
value ({BASELINE_SNR_PECCORED:.4f}/{BASELINE_SNR_HOLLOW:.4f}); else
AMBIGUOUS. Check B (this program's own founding T28 R3 standard):
SURVIVES if delta[idx] keeps the same sign as cpl=20
({BASELINE_DELTA:.6e}) and stays within one order of magnitude of it;
COLLAPSES on a sign flip or a >=10x drop; else AMBIGUOUS. No advance
position taken on which of the three outcomes either check will report.
"""


def build_result_text(n_fdtd_calls, total_wall_s, geom_ok, repro_ok,
                       named_bin_result, wall_time_source=None):
    wall_time_note = f"\n({wall_time_source})" if wall_time_source else ""
    return f"""RESULT (exp-112, Panel Iteration 89)

{DISCLAIMER}

{n_fdtd_calls} real FDTD calls, {total_wall_s:.1f}s ({total_wall_s/60.0:.2f} min)
total wall time this cycle, zero `lab/` diff.{wall_time_note}

**Geometry identity: {'PASS' if geom_ok else 'FAIL'}.**
**Reproduction/self-consistency precondition: {'PASS' if repro_ok else 'FAIL'}.**
**Named bin (-146.25deg, r=156, margin=32):** {named_bin_result}
"""


if __name__ == "__main__":
    if "--predictions-only" in sys.argv:
        predictions_text = build_predictions_text()
        assert DISCLAIMER in predictions_text, "R23: disclaimer missing from Predictions block"
        print(predictions_text)
    elif "--verify-geometry" in sys.argv:
        result = verify_geometry_identity()
        print(json.dumps(result, indent=2))
        assert result["pass_"], "geom_fixedabs_cpl does not reduce to R.geom_fixedabs at cpl==20"
        print("verify_geometry_identity: PASS")
    else:
        print("This module holds shared geometry/constants and analysis functions only.")
