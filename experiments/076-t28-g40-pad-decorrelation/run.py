"""exp-076 -- T28 G40/PAD Decorrelation: measurement harness.
=============================================================================
Panel Iteration 53 (lead: QUANTUM OPTICS, by rotation). Phase-3 SYNTHESIS
(Director) applying Red Team's Phase-2 mandatory-fix docket IN FULL (8/8
items ADOPTED, zero overridden -- see `phase3_synthesis.md` for the full
disposition table). This file implements the FIXED design, not the Phase-1
proposal's original (a)/(b)/(c1)/(c2) outcome scheme.

Three blocks, run in this exact order (docket item 4's HALT-if-fails
settling precondition MUST clear before the dense sweep is trusted):

  Block SETTLE_PRECONDITION: G40 @ {39,40}deg x 600nm x STEPS={2800,4200}
                              (the 2800 pair ARE Block DENSE's own theta=39/
                              40 points -- run once here, reused, not re-run)
                              + G40 @ 39deg x 600nm x STEPS=1400
                              = 5 calls run (3 of them new: 2x4200 + 1x1400)
  Block DENSE:                G40 @ 31 angles (36-42deg, 0.2deg step) x
                              600nm x STEPS=2800   (29 NEW + 2 reused above)
  Block LEG750:                G40 @ 16 angles (38-41deg, 0.2deg step) x
                              750nm x STEPS=2800  (advisory/narrow-window)

  TOTAL NEW FDTD CALLS: 2 (settle fwd) + 1 (settle back) + 31 (dense,
  including the 2 settle-reused points) + 16 (leg750) = 50.

House discipline (PANEL.md, non-negotiable): this file is committed and
`NOTES.md`'s FROZEN PREDICTIONS section is committed to git BEFORE this
script's first execution. Zero `lab/` diff. Reuses committed machinery
programmatically wherever possible (R4 discipline):
  - `experiments/065-.../design_geometry.py`'s CONFIGS/config() for G40's
    geometry -- reached here via `exp069_run.dg` (exp-069's own design_
    geometry.py sets `CONFIGS = dg065.CONFIGS` verbatim; loading it directly
    would risk a `sys.modules["design_geometry"]` name collision against
    exp-069's own `import design_geometry as dg` -- see `_load_module()`
    below).
  - `experiments/069-.../run.py`'s `_one_run`/`_profile`/`_c_empty` FDTD-call
    idiom (same `profile="plane"`, `edge=TAPER=40`, STEPS convention),
    reused VERBATIM via `exp069_run`, not re-implemented.
  - `experiments/076-.../g0e_amplitude_channel_check.py`'s own
    `_amp_ratio_recover` (which itself reuses exp-072's `carrier_fit`/
    `design_matrix`/`_amp_phase_at` VERBATIM) for every `amp_ratio` figure
    in this file -- this cycle's own already-verified G0-e machinery, not
    re-derived.
  - `experiments/072-.../run.py`'s `analyze_pair` VERBATIM for the two new
    pairs' `delta_P_obs` (needed for the disclosed-only `rho_pad_absorb`
    diagnostic, docket items 2/3).

MANDATORY-FIX DOCKET (phase2_redteam_audit.md, all 8 items, ADOPTED IN
FULL by the Director, zero overridden -- see phase3_synthesis.md):
  1/2. Rewritten, exhaustive & mutually-exclusive 9-cell/5-outcome §4 scheme
       (replaces the old (a)/(b)/(c1)/(c2) scheme) -- `classify_outcome()`.
  2.   `rho_pad_absorb` downgraded to a disclosed, non-gating, explicitly
       uncalibrated diagnostic -- `rho_pad_absorb()`, never compared against
       an "interaction exists" verdict anywhere in this file.
  3.   `R_q`'s role scoped precisely: NOT used in the gating `amp_ratio`
       statistic; used, via `delta_P_obs`, in the disclosed-only
       `rho_pad_absorb` diagnostic (no null-calibration attached to it here).
  4.   3-call settling precondition (`block_settle_precondition()` +
       `settling_gate_check()`), HALT-if-fails, run and checked FIRST.
  5.   16-call G40-at-750nm advisory leg (`block_leg750()` /
       `score_leg750()`), reusing `block_leg750`'s exact committed window.
  6.   0.050 threshold prose corrected (see NOTES.md/phase3_synthesis.md;
       this file computes the bins, never mis-glosses them).
  7.   MATERIALS' ABSORB/PAD-same-representational-class caveat -- textual,
       carried in NOTES.md/phase3_synthesis.md, attached to every outcome
       that uses ABSORB-tied/PAD-tied language.
  8.   THERMODYNAMICS' energy-sidecar N/A disposition -- textual, carried in
       NOTES.md's idealizations.
"""

import importlib.util
import json
import math
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)

EXP069 = os.path.join(ROOT, "experiments", "069-t21-block-mini-period-match-power-up")
EXP072 = os.path.join(ROOT, "experiments", "072-t28-differential-beat-fit")


def _load_module(name, path):
    """Load a file as a module under a DISTINCT sys.modules name -- the
    established idiom in this codebase (dg065._load_exp048,
    dg069._load_exp065, exp072's own g0e_amplitude_channel_check._load_
    exp072) for avoiding a plain-name collision when two experiments each
    have their own file of the same basename (every experiment in this
    program has a `run.py` and/or `design_geometry.py`)."""
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


# exp-069's run.py: gives us `_one_run`/`_profile`/`_c_empty` (the FDTD-call
# idiom) AND, via its own `dg` global, exp-065's CONFIGS/CPL/TAPER/
# COURANT_FRAC/DENSE_ANGLES/LEG750_ANGLES/STEPS_SETTLED/STEPS_STRESS
# verbatim -- loading it FIRST and reading everything off `exp069_run.dg`
# avoids ever separately `import design_geometry` under the plain name
# ourselves (which would race exp069_run's own `import design_geometry as
# dg` for the sys.modules cache slot and silently hand it the wrong file).
exp069_run = _load_module("_exp076_exp069_run", os.path.join(EXP069, "run.py"))
dg = exp069_run.dg   # = experiments/065-.../design_geometry.py's own module

# This cycle's own already-built, already-PASSing G0-e check (Phase 1) --
# reuse its `_amp_ratio_recover` (and, transitively, exp-072's `carrier_fit`/
# `design_matrix`/`_amp_phase_at`) rather than re-deriving any of it.
import g0e_amplitude_channel_check as g0e   # noqa: E402

exp072_run = g0e.exp072_run
_amp_ratio_recover = g0e._amp_ratio_recover

STEPS_SETTLED = dg.STEPS_SETTLED      # 2800 -- T27's established settled floor
STEPS_STRESS = dg.STEPS_STRESS        # 4200 -- forward-settling stress cell
STEPS_NATIVE = 1400                    # backward-settling differential (VISION)
DENSE_ANGLES = dg.DENSE_ANGLES         # 31 angles, 36.0-42.0deg, 0.2deg step
LEG750_ANGLES = dg.LEG750_ANGLES       # 16 angles, 38.0-41.0deg, 0.2deg step
SETTLE_THETAS = (39.0, 40.0)           # EM's forward-settling pair
SEED = 20530076                        # panel iteration 53, exp-076

# ============================================================= structural freeze
FROZEN_PREDICTIONS = """
exp-076 -- G40/PAD Decorrelation -- FROZEN before any FDTD call this cycle.

HEADLINE STATISTICS (identical formula to the confounded series, exp-072's
own `amp_ratio = sqrt(A_i^2+A_q^2)/amp`, reused verbatim via
`_amp_ratio_recover`):
  x = amp_ratio(PAIR_PAD)      = amp_ratio(C40, G40)   [pure PAD effect]
  y = amp_ratio(PAIR_ABSORB40) = amp_ratio(G40, C80)   [pure ABSORB effect]

BIN EDGES (re-derived at run time from the real committed baseline
amp_ratio(C40,C80), NEVER hand-typed -- R4; ~0.050/~0.116 at this program's
already-committed baseline, exact values printed and stored in results.json):
  THRESH_LOW  = 0.3 x amp_ratio(C40,C80)
  THRESH_HIGH = 0.7 x amp_ratio(C40,C80)
  LOW  = [0, THRESH_LOW)
  MED  = [THRESH_LOW, THRESH_HIGH)
  HIGH = [THRESH_HIGH, inf)

9-CELL -> 5-OUTCOME MAPPING (exhaustive, mutually exclusive by construction
-- a direct lookup table over the full x_bin x y_bin partition; see
`classify_outcome()`/`OUTCOME_TABLE` and phase3_synthesis.md's printed 3x3
table for the by-hand verification Red Team's Attack 1 asked for):
  (LOW,  LOW)  -> BOTH_LOW_NULL
  (LOW,  MED)  -> ABSORB_LEANING
  (LOW,  HIGH) -> ABSORB_TIED
  (MED,  LOW)  -> PAD_TIED
  (MED,  MED, x<y)  -> ABSORB_LEANING
  (MED,  MED, x>=y) -> PAD_TIED           [tie x==y: conservatively PAD_TIED]
  (MED,  HIGH) -> ABSORB_LEANING
  (HIGH, LOW)  -> PAD_TIED
  (HIGH, MED)  -> PAD_TIED
  (HIGH, HIGH) -> BOTH_HIGH_SUPER_ADDITIVE   [carved out of the (x=HIGH, any
                                               y) PAD_TIED catch-all as its
                                               own named cell -- see
                                               phase3_synthesis.md's docket-
                                               item-1/2 resolution note]

SETTLING PRECONDITION (docket item 4, MANDATORY, HALT-if-fails, checked
BEFORE Block DENSE's remaining 29 points run or any real amp_ratio is
scored -- see `settling_gate_check()`):
  forward (EM's fix):  |C_G40(4200,theta) - C_G40(2800,theta)| / amp_ref
                        < THRESH_LOW, at BOTH theta in {39,40}deg, where
                        amp_ref = the C40-C80 baseline's own fitted carrier
                        amplitude (the SAME denominator amp_ratio uses) --
                        i.e. the shift, expressed in the identical units
                        amp_ratio's numerator is measured in, must not by
                        itself be able to move an amp_ratio reading across
                        the smallest live band edge (THRESH_LOW). Bar cited
                        exactly: THRESH_LOW itself (not a separately-chosen
                        number), per the Director's own instruction to use
                        "the smallest live threshold, 0.050". If this fails:
                        HALT, write a partial results.json flagged for
                        Director review, do not run the remaining 45 calls.
  backward (VISION's fix, DISCLOSED, non-gating): |C_G40(2800,39) -
                        C_G40(1400,39)|, relative to C_G40(1400,39) --
                        bounds how wrong exp-065's own unsettled Block PAD
                        G40 reading was. Reported, never gates.

DIAGNOSTICS (disclosed-only, NEVER gating, docket items 2/3):
  rho_pad_absorb = |delta_P_obs(PAIR_PAD) + delta_P_obs(PAIR_ABSORB40) -
                    delta_P_obs(C40,C80)| / max(|delta_P_obs(C40,C80)|,
                    0.005), delta_P_obs(C40,C80) LOADED from exp-072's
                    committed results.json, not re-fit. This is an
                    uncalibrated magnitude signal indistinguishable, by this
                    design, from an artifact of each pair's independently-
                    fit carrier (exp-072's own run.py documents the
                    identical `rho_c` construction as NOT a basis-stability
                    or interaction test). NO interaction claim is drawn from
                    it anywhere in this file.

750nm LEG (docket item 5, advisory/narrow-window, NOT decisive): raw
  amp_ratio(PAIR_PAD)/amp_ratio(PAIR_ABSORB40) at the LEG750_ANGLES window,
  reported with a same-direction/opposite-direction qualitative comparison
  against the 600nm headline ordering (x<=y or x>y) ONLY -- the 9-cell band
  machinery is NOT applied at 750nm (the bins were calibrated for the 6deg
  600nm window; this window is 3deg).

None of this is a RESOLVED/CONFIRMED-class significance claim on R_q or any
carrier/phase-conditioned coefficient -- amp_ratio is null-free and R_q-free
(exp-076 phase1_proposal.md Sec7); rho_pad_absorb carries no null-calibration
and is explicitly non-gating.
"""


def assert_lab_clean():
    import subprocess
    out = subprocess.run(["git", "diff", "--stat", "--", "lab/"], cwd=ROOT,
                          capture_output=True, text=True).stdout.strip()
    assert out == "", f"lab/ is dirty:\n{out}"
    return "clean"


# ===================================================== desk-only preconditions
def geometry_congruence_check():
    """Zero-FDTD desk check #1 (R4/G0-style): G40 shares C80's ENTIRE padded
    domain/clearances/aperture/D_SP, differing from C80 ONLY in `absorb`
    (and the clearances that are mechanically derived from it); and shares
    C40's `absorb` exactly. Reproduces phase1_proposal.md Sec2a's table
    directly from CONFIGS, not by re-typing it."""
    c40, c80, g40 = dg.CONFIGS["C40"], dg.CONFIGS["C80"], dg.CONFIGS["G40"]
    shared_with_c80 = ("nx", "ny", "src_x", "plane_x", "obj_y", "y_lo", "y_hi",
                        "A", "aperture_cells", "d_sp")
    matches_c80 = {f: (g40[f] == c80[f]) for f in shared_with_c80}
    absorb_matches_c40 = (g40["absorb"] == c40["absorb"])
    pad_matches_c80 = (g40["pad"] == c80["pad"])
    differs_from_c40 = {f: (g40[f] != c40[f])
                         for f in ("clear_plane", "clear_src", "clear_span_y",
                                   "nx", "ny", "aperture_cells")}
    all_pass = (all(matches_c80.values()) and absorb_matches_c40
                and pad_matches_c80)
    return dict(all_pass=bool(all_pass), matches_c80=matches_c80,
                absorb_matches_c40=bool(absorb_matches_c40),
                pad_matches_c80=bool(pad_matches_c80),
                differs_from_c40=differs_from_c40,
                c40=c40, c80=c80, g40=g40)


def baseline_reproduction_check():
    """Zero-FDTD desk check #2 (R4/G0-style, mirrors exp-072's own `g0_pass`
    precondition pattern): reproduce all four baseline amp_ratio figures
    (C40-C60/C60-C70/C70-C80/C40-C80) TWO independent ways from committed
    data -- (i) re-invoking the real pipeline (`_amp_ratio_recover`, i.e.
    `carrier_fit`->`design_matrix`->OLS) on the raw committed C40/C60/C70/
    C80 series, and (ii) reading exp-072's own committed, already-scored
    A_i/A_q/amplitude coefficients straight out of its results.json -- and
    asserting the two agree to near machine precision. No baseline number is
    hand-typed anywhere in this file; the bin edges (THRESH_LOW/THRESH_HIGH)
    are then derived from whichever of the two the check certifies (they are
    identical to float precision when this passes)."""
    data = exp072_run.load_data()
    with open(os.path.join(EXP072, "results.json")) as f:
        committed72 = json.load(f)
    pair_keys = [("C40", "C60"), ("C60", "C70"), ("C70", "C80"), ("C40", "C80")]
    checks = {}
    for a, b in pair_keys:
        key = f"{a}-{b}"
        recovered, diag = _amp_ratio_recover(data["theta"], data[a], data[b])
        stored = committed72["scored"]["per_pair"][key]
        stored_ratio = math.hypot(stored["A_i"], stored["A_q"]) / stored["amplitude"]
        rel_err = (abs(recovered / stored_ratio - 1.0) if stored_ratio != 0
                   else abs(recovered))
        checks[key] = dict(recovered_amp_ratio=recovered,
                            stored_amp_ratio=stored_ratio, rel_err=rel_err,
                            passed=bool(rel_err <= 1e-6))
    all_pass = all(c["passed"] for c in checks.values())
    return dict(all_pass=bool(all_pass), checks=checks,
                delta_P_obs_C40_C80=committed72["scored"]["per_pair"]["C40-C80"]["delta_P_obs"],
                data=data, committed72=committed72)


# ===================================================== FDTD call workers
def _g40_call(args):
    theta, cpl_nm, steps = args
    cfg = dg.CONFIGS["G40"]
    t0 = time.time()
    cap = exp069_run._one_run(cfg, dg.CPL[cpl_nm], theta, steps)
    prof = exp069_run._profile(cap, cfg)
    c = exp069_run._c_empty(prof, cfg)
    return (theta, cpl_nm, steps, c, time.time() - t0)


def _run_jobs(jobs, label):
    print(f"\n=== {label}: {len(jobs)} calls ===", flush=True)
    t0, n, out = time.time(), 0, {}
    with ProcessPoolExecutor(max_workers=4) as ex:
        for theta, cpl_nm, steps, c, dt in ex.map(_g40_call, jobs):
            out[(theta, cpl_nm, steps)] = c
            n += 1
            print(f"  [{label} {n:3d}/{len(jobs)}] theta={theta:+06.2f} "
                  f"{cpl_nm}nm STEPS={steps} C_empty={c:+.6f} ({dt:5.1f}s)",
                  flush=True)
    assert n == len(jobs), f"{label} run-count mismatch: {n} != {len(jobs)}"
    return dict(n_new_runs=n, elapsed_s=time.time() - t0, by_key=out)


# ===================================================== Block SETTLE_PRECONDITION
def block_settle_precondition():
    """docket item 4: 3 NEW FDTD calls + the 2 theta={39,40}@STEPS=2800
    points that ARE Block DENSE's own points (run here first, reused
    below, never re-run). Returns C_empty readings keyed by (theta, steps)."""
    jobs = [(39.0, 600, STEPS_SETTLED), (40.0, 600, STEPS_SETTLED),
            (39.0, 600, STEPS_STRESS), (40.0, 600, STEPS_STRESS),
            (39.0, 600, STEPS_NATIVE)]
    res = _run_jobs(jobs, "SETTLE_PRECONDITION")
    return res


def settling_gate_check(pre, amp_ref, thresh_low):
    """docket item 4a (EM's forward-settling fix, MANDATORY, HALT-if-fails)
    + item 4b (VISION's backward differential, DISCLOSED, non-gating).

    Bar cited exactly, per the Director's instruction: the forward shift
    |C(4200)-C(2800)|, expressed as a fraction of `amp_ref` (the C40-C80
    baseline's own fitted carrier amplitude -- the SAME normalization
    amp_ratio's numerator is divided by), must stay below `thresh_low`
    (THRESH_LOW, the smallest live §4 band edge) at BOTH theta=39/40deg.
    This is a direct translation of "the shift must not be able to move an
    amp_ratio reading across the smallest live threshold on its own" into
    absolute C_empty units via amp_ratio's own denominator -- matching this
    program's established settling-gate convention (exp-066/069's own
    Block STRESS / Block SETTLE: compare a STEPS-refinement shift against a
    fixed, previously-established bar) but re-targeted at THIS cycle's own
    decision-relevant scale rather than a generic 1%/5% relative-ratio bar,
    since exp-069's P-069-4 bar was never validated at G40's own untested
    (thin-boundary, large-domain) geometry (EM's own Phase-2 attack)."""
    c2800_39, c2800_40 = pre[(39.0, 600, STEPS_SETTLED)], pre[(40.0, 600, STEPS_SETTLED)]
    c4200_39, c4200_40 = pre[(39.0, 600, STEPS_STRESS)], pre[(40.0, 600, STEPS_STRESS)]
    c1400_39 = pre[(39.0, 600, STEPS_NATIVE)]

    shift_39 = abs(c4200_39 - c2800_39)
    shift_40 = abs(c4200_40 - c2800_40)
    frac_39 = shift_39 / amp_ref
    frac_40 = shift_40 / amp_ref
    forward_pass = bool(frac_39 < thresh_low and frac_40 < thresh_low)

    back_abs_39 = abs(c2800_39 - c1400_39)
    back_rel_39 = back_abs_39 / abs(c1400_39) if c1400_39 != 0 else float("nan")

    # bonus, zero extra cost: exp-065's own committed Block PAD already has
    # G40@theta=40/600nm/STEPS=1400 (-0.012657284695401505) -- reused, not
    # re-run, for the SAME backward-differential disclosure at the second
    # settling angle.
    with open(os.path.join(ROOT, "experiments", "065-t24-absorb-boundary-sweep",
                            "results.json")) as f:
        exp065_results = json.load(f)
    pad_1400 = {r["theta"]: r["C_empty"] for r in exp065_results["block_pad"]["rows"]
                if r["lambda_nm"] == 600}
    c1400_40 = pad_1400.get(40.0)
    back_abs_40 = abs(c2800_40 - c1400_40) if c1400_40 is not None else None
    back_rel_40 = (back_abs_40 / abs(c1400_40)
                   if c1400_40 not in (None, 0) else float("nan"))

    return dict(
        amp_ref=amp_ref, thresh_low=thresh_low,
        forward=dict(shift_39=shift_39, shift_40=shift_40,
                     frac_39=frac_39, frac_40=frac_40, passed=forward_pass,
                     bar_cited="THRESH_LOW (0.3 x baseline amp_ratio(C40,C80)"
                               " -- the smallest live band edge)"),
        backward_39=dict(c_1400=c1400_39, c_2800=c2800_39,
                          abs_shift=back_abs_39, rel_shift=back_rel_39,
                          disclosed_only=True, gates=False, new_call=True),
        backward_40_bonus=dict(c_1400=c1400_40, c_2800=c2800_40,
                                abs_shift=back_abs_40, rel_shift=back_rel_40,
                                disclosed_only=True, gates=False,
                                new_call=False,
                                source="experiments/065-.../results.json::block_pad"),
        c2800=dict(theta_39=c2800_39, theta_40=c2800_40),
        c4200=dict(theta_39=c4200_39, theta_40=c4200_40),
    )


# ===================================================== Block DENSE / LEG750
def block_dense_remaining(exclude_thetas):
    jobs = [(th, 600, STEPS_SETTLED) for th in DENSE_ANGLES
            if th not in exclude_thetas]
    return _run_jobs(jobs, "DENSE_REMAINING")


def block_leg750():
    jobs = [(th, 750, STEPS_SETTLED) for th in LEG750_ANGLES]
    return _run_jobs(jobs, "LEG750")


def assemble_dense_g40(pre, remaining):
    """Merge the 2 settle-precondition points (theta in {39,40} @ STEPS=2800)
    with the 29 remaining DENSE_ANGLES points into ONE 31-point G40 series,
    in DENSE_ANGLES order -- the 2 points are REUSED here, not re-run."""
    by_theta = dict(remaining["by_key"])
    for th in SETTLE_THETAS:
        by_theta[(th, 600, STEPS_SETTLED)] = pre["by_key"][(th, 600, STEPS_SETTLED)]
    assert len(by_theta) == len(DENSE_ANGLES), \
        f"assembled G40 dense series has {len(by_theta)} points, want {len(DENSE_ANGLES)}"
    return {th: by_theta[(th, 600, STEPS_SETTLED)] for th in DENSE_ANGLES}


def load_committed_c40_c80_dense():
    with open(os.path.join(EXP069, "results.json")) as f:
        d = json.load(f)
    rows = {r["theta"]: r for r in d["block_dense"]["rows"]}
    return rows


def load_committed_c40_c80_leg750():
    with open(os.path.join(EXP069, "results.json")) as f:
        d = json.load(f)
    rows = {r["theta"]: r for r in d["block_leg750"]["rows"]}
    return rows


# ===================================================== outcome classification
def classify_bin(v, thresh_low, thresh_high):
    if v < thresh_low:
        return "LOW"
    if v < thresh_high:
        return "MED"
    return "HIGH"


# Explicit 3x3 lookup table -- exhaustive and mutually exclusive BY
# CONSTRUCTION (a total function over a 9-cell partition). The (MED, MED)
# cell is resolved by the x<y / x>=y tie-break at classify_outcome() call
# time (its value here is a placeholder, never looked up directly).
#
# IMPLEMENTATION NOTE (resolves the only textual ambiguity in the docket's
# literal wording, disclosed here and in phase3_synthesis.md): the docket's
# prose defines PAD-TIED as "(x=HIGH, any y) OR ..." and separately carves
# out BOTH-HIGH as "(x=HIGH, y=HIGH)" as its own "new category" -- read
# literally, cell (HIGH,HIGH) would satisfy BOTH descriptions at once,
# exactly the non-mutual-exclusivity defect Red Team's Attack 1 exists to
# close. The only reading consistent with BOTH-HIGH being introduced as a
# distinctly-flagged NEW outcome (rather than dead text) is that it is
# carved OUT of PAD-TIED's otherwise-catch-all "(x=HIGH, any y)" disjunct.
# This table implements that resolution directly: cell (HIGH,HIGH) maps to
# BOTH_HIGH_SUPER_ADDITIVE only.
OUTCOME_TABLE = {
    ("LOW", "LOW"): "BOTH_LOW_NULL",
    ("LOW", "MED"): "ABSORB_LEANING",
    ("LOW", "HIGH"): "ABSORB_TIED",
    ("MED", "LOW"): "PAD_TIED",
    ("MED", "MED"): None,          # tie-break at call time (x<y / x>=y)
    ("MED", "HIGH"): "ABSORB_LEANING",
    ("HIGH", "LOW"): "PAD_TIED",
    ("HIGH", "MED"): "PAD_TIED",
    ("HIGH", "HIGH"): "BOTH_HIGH_SUPER_ADDITIVE",
}


def classify_outcome(x, y, thresh_low, thresh_high):
    """x = amp_ratio(PAIR_PAD), y = amp_ratio(PAIR_ABSORB40), both >= 0 by
    construction. Returns the bin labels and the single named outcome."""
    x_bin = classify_bin(x, thresh_low, thresh_high)
    y_bin = classify_bin(y, thresh_low, thresh_high)
    if x_bin == "MED" and y_bin == "MED":
        outcome = "ABSORB_LEANING" if x < y else "PAD_TIED"
    else:
        outcome = OUTCOME_TABLE[(x_bin, y_bin)]
    return dict(x=x, y=y, x_bin=x_bin, y_bin=y_bin, outcome=outcome)


def verify_outcome_table_exhaustive_and_exclusive(thresh_low, thresh_high):
    """Enumerate a representative point in EVERY one of the 9 cells and
    confirm each maps to exactly one of the 5 named outcomes -- the direct,
    by-hand-checkable verification Red Team's Attack 1 asked for. Returns
    the full 3x3 table for embedding in NOTES.md/phase3_synthesis.md."""
    lo_pt, med_pt, hi_pt = (thresh_low / 2.0, (thresh_low + thresh_high) / 2.0,
                             thresh_high * 1.5)
    bin_reps = {"LOW": lo_pt, "MED": med_pt, "HIGH": hi_pt}
    table = {}
    outcomes_seen = set()
    for xb, xv in bin_reps.items():
        for yb, yv in bin_reps.items():
            r = classify_outcome(xv, yv, thresh_low, thresh_high)
            table[(xb, yb)] = r["outcome"]
            outcomes_seen.add(r["outcome"])
    # (MED, MED) needs BOTH sub-cases checked explicitly (the tie-break):
    below_med = classify_outcome(med_pt, med_pt * 1.3, thresh_low, thresh_high)  # x<y
    above_med = classify_outcome(med_pt * 1.3, med_pt, thresh_low, thresh_high)  # x>=y
    equal_med = classify_outcome(med_pt, med_pt, thresh_low, thresh_high)        # x==y
    n_cells = len(table)
    n_named = len(outcomes_seen)
    exhaustive = n_cells == 9 and all(v is not None for v in table.values())
    return dict(
        exhaustive=bool(exhaustive), n_cells_covered=n_cells,
        n_distinct_outcomes=n_named, outcomes=sorted(outcomes_seen),
        table={f"{k[0]}/{k[1]}": v for k, v in table.items()},
        med_med_x_lt_y=below_med["outcome"], med_med_x_gte_y=above_med["outcome"],
        med_med_x_eq_y=equal_med["outcome"],
    )


# ===================================================== diagnostics (disclosed-only)
def rho_pad_absorb(dp_pad, dp_absorb40, dp_c40_c80):
    """docket items 2/3: disclosed, uncalibrated, non-gating. Mirrors
    exp-072's `rho_c` construction EXACTLY (same 0.005 floor) -- and
    inherits its documented disposition: NOT a basis-stability or
    interaction test, indistinguishable from a carrier-choice artifact of
    each pair's independently-fit carrier. No verdict is attached to any
    value of this quantity anywhere in this file."""
    S = dp_pad + dp_absorb40
    D = dp_c40_c80
    return abs(S - D) / max(abs(D), 0.005)


# ===================================================== headline scoring
def score_headline(dense_g40_by_theta, c40_c80_dense_rows, rng):
    theta = np.array(DENSE_ANGLES)
    c40 = np.array([c40_c80_dense_rows[t]["C_empty_C40"] for t in DENSE_ANGLES])
    c80 = np.array([c40_c80_dense_rows[t]["C_empty_C80"] for t in DENSE_ANGLES])
    g40 = np.array([dense_g40_by_theta[t] for t in DENSE_ANGLES])

    data_new = dict(theta=theta, C40=c40, G40=g40, C80=c80)
    # analyze_pair (exp-072, VERBATIM) gives us A_i/A_q/amplitude (->
    # amp_ratio) AND delta_P_obs from ONE call each -- no separate re-fit.
    pair_pad = exp072_run.analyze_pair(data_new, "C40", "G40", 0.0, rng)
    pair_absorb40 = exp072_run.analyze_pair(data_new, "G40", "C80", 40.0, rng)

    x = math.hypot(pair_pad["A_i"], pair_pad["A_q"]) / pair_pad["amplitude"]
    y = math.hypot(pair_absorb40["A_i"], pair_absorb40["A_q"]) / pair_absorb40["amplitude"]

    return dict(theta=theta.tolist(), C40=c40.tolist(), G40=g40.tolist(),
                C80=c80.tolist(), x_amp_ratio_PAIR_PAD=x,
                y_amp_ratio_PAIR_ABSORB40=y, pair_pad=pair_pad,
                pair_absorb40=pair_absorb40)


def score_leg750(g40_leg750_by_theta, c40_c80_leg750_rows, headline_x, headline_y):
    theta = np.array(LEG750_ANGLES)
    c40 = np.array([c40_c80_leg750_rows[t]["C_empty_C40"] for t in LEG750_ANGLES])
    c80 = np.array([c40_c80_leg750_rows[t]["C_empty_C80"] for t in LEG750_ANGLES])
    g40 = np.array([g40_leg750_by_theta[t] for t in LEG750_ANGLES])

    x750, diag_x = _amp_ratio_recover(theta, c40, g40)
    y750, diag_y = _amp_ratio_recover(theta, g40, c80)

    same_direction = bool((x750 <= y750) == (headline_x <= headline_y))
    return dict(theta=theta.tolist(), C40=c40.tolist(), G40=g40.tolist(),
                C80=c80.tolist(),
                x_amp_ratio_PAIR_PAD_750nm=x750,
                y_amp_ratio_PAIR_ABSORB40_750nm=y750,
                same_direction_as_600nm_headline=same_direction,
                advisory_only=True, decisive=False,
                window_deg=(LEG750_ANGLES[-1] - LEG750_ANGLES[0]),
                headline_window_deg=(DENSE_ANGLES[-1] - DENSE_ANGLES[0]),
                note=("advisory / narrow-window (3deg vs the 600nm window's "
                      "6deg) -- NOT decisive, and does not license any "
                      "wavelength-general citation of this cycle's headline "
                      "verdict (Red Team Attack 4 disposition, docket item 5)"))


# ===================================================== main
def main():
    t_start = time.time()
    print(FROZEN_PREDICTIONS, flush=True)
    print(f"lab/ clean: {assert_lab_clean()}", flush=True)

    print("\n[G0-desk-1] GEOMETRY CONGRUENCE CHECK (zero FDTD)", flush=True)
    geom = geometry_congruence_check()
    print(f"  G40 shares C80's full padded domain (nx/ny/src_x/plane_x/"
          f"obj_y/y_lo/y_hi/A/aperture/D_SP): {geom['matches_c80']}", flush=True)
    print(f"  G40.absorb == C40.absorb: {geom['absorb_matches_c40']}   "
          f"G40.pad == C80.pad: {geom['pad_matches_c80']}", flush=True)
    assert geom["all_pass"], f"GEOMETRY CONGRUENCE CHECK FAILED: {geom}"
    print("  [PASS]", flush=True)

    print("\n[G0-desk-2] BASELINE amp_ratio REPRODUCTION CHECK (zero FDTD)",
          flush=True)
    baseline = baseline_reproduction_check()
    for k, c in baseline["checks"].items():
        print(f"  {k}: recovered={c['recovered_amp_ratio']:.6f} "
              f"stored={c['stored_amp_ratio']:.6f} rel_err={c['rel_err']:.2e} "
              f"[{'PASS' if c['passed'] else 'FAIL'}]", flush=True)
    assert baseline["all_pass"], f"BASELINE REPRODUCTION CHECK FAILED: {baseline}"
    print("  [PASS]", flush=True)

    baseline_c40_c80_amp_ratio = baseline["checks"]["C40-C80"]["recovered_amp_ratio"]
    baseline_c40_c80_amplitude = baseline["committed72"]["scored"]["per_pair"]["C40-C80"]["amplitude"]
    delta_P_obs_C40_C80 = baseline["delta_P_obs_C40_C80"]
    THRESH_LOW = 0.3 * baseline_c40_c80_amp_ratio
    THRESH_HIGH = 0.7 * baseline_c40_c80_amp_ratio
    print(f"\n  THRESH_LOW  = 0.3 x {baseline_c40_c80_amp_ratio:.6f} = {THRESH_LOW:.6f}", flush=True)
    print(f"  THRESH_HIGH = 0.7 x {baseline_c40_c80_amp_ratio:.6f} = {THRESH_HIGH:.6f}", flush=True)
    print(f"  (docket item 6: THRESH_LOW is well ABOVE the smallest "
          f"established adjacent-pair reading C70-C80=0.020, not 'at or "
          f"below' it)", flush=True)

    verify = verify_outcome_table_exhaustive_and_exclusive(THRESH_LOW, THRESH_HIGH)
    print(f"\n[G0-desk-3] 9-CELL OUTCOME TABLE VERIFICATION (zero FDTD): "
          f"exhaustive={verify['exhaustive']}, "
          f"5 named outcomes={verify['outcomes']==sorted(['ABSORB_TIED','ABSORB_LEANING','PAD_TIED','BOTH_LOW_NULL','BOTH_HIGH_SUPER_ADDITIVE'])}",
          flush=True)
    for k, v in verify["table"].items():
        print(f"    {k}: {v}", flush=True)
    assert verify["exhaustive"], f"OUTCOME TABLE NOT EXHAUSTIVE: {verify}"
    assert set(verify["outcomes"]) == {"ABSORB_TIED", "ABSORB_LEANING",
                                        "PAD_TIED", "BOTH_LOW_NULL",
                                        "BOTH_HIGH_SUPER_ADDITIVE"}, verify
    print("  [PASS]", flush=True)

    # -------------------------------------------------- (a) settling precondition
    pre = block_settle_precondition()
    gate = settling_gate_check(pre["by_key"], amp_ref=baseline_c40_c80_amplitude,
                                thresh_low=THRESH_LOW)
    print(f"\n[SETTLING GATE] forward: shift_39={gate['forward']['shift_39']:.6e} "
          f"frac_39={gate['forward']['frac_39']:.4f}  "
          f"shift_40={gate['forward']['shift_40']:.6e} "
          f"frac_40={gate['forward']['frac_40']:.4f}  bar={THRESH_LOW:.4f}  "
          f"PASSED={gate['forward']['passed']}", flush=True)
    print(f"  backward (disclosed, non-gating): 39deg rel_shift="
          f"{gate['backward_39']['rel_shift']:.4f}  "
          f"40deg (bonus, reused) rel_shift="
          f"{gate['backward_40_bonus']['rel_shift']:.4f}", flush=True)

    if not gate["forward"]["passed"]:
        print("\n*** HALT: settling precondition FAILED -- flagged for "
              "Director review. Remaining 45 FDTD calls NOT run. ***", flush=True)
        out = dict(experiment="076-t28-g40-pad-decorrelation", panel_iteration=53,
                   lead_seat="QUANTUM OPTICS", halted=True,
                   halt_reason="settling precondition (docket item 4a) FAILED",
                   geometry_congruence={k: v for k, v in geom.items()
                                        if k not in ("c40", "c80", "g40")},
                   baseline_reproduction={k: v for k, v in baseline.items()
                                          if k not in ("data", "committed72")},
                   thresh_low=THRESH_LOW, thresh_high=THRESH_HIGH,
                   settle_precondition={
                       "n_new_runs": pre["n_new_runs"], "elapsed_s": pre["elapsed_s"],
                       "by_key": {f"{k[0]}_{k[1]}nm_STEPS{k[2]}": v
                                  for k, v in pre["by_key"].items()},
                   },
                   settling_gate=gate)
        with open(os.path.join(HERE, "results.json"), "w") as f:
            json.dump(out, f, indent=2, default=float)
        return out
    print("  [PASS] -- proceeding to Block DENSE / Block LEG750", flush=True)

    # -------------------------------------------------- (b) Block DENSE (remaining)
    remaining = block_dense_remaining(exclude_thetas=set(SETTLE_THETAS))
    dense_g40 = assemble_dense_g40(pre, remaining)
    c40_c80_dense_rows = load_committed_c40_c80_dense()

    # -------------------------------------------------- (c) Block LEG750
    leg750_res = block_leg750()
    g40_leg750_by_theta = leg750_res["by_key"]
    g40_leg750_by_theta = {th: g40_leg750_by_theta[(th, 750, STEPS_SETTLED)]
                            for th in LEG750_ANGLES}
    c40_c80_leg750_rows = load_committed_c40_c80_leg750()

    # -------------------------------------------------- (d) scoring
    rng = np.random.default_rng(SEED)
    headline = score_headline(dense_g40, c40_c80_dense_rows, rng)
    x, y = headline["x_amp_ratio_PAIR_PAD"], headline["y_amp_ratio_PAIR_ABSORB40"]
    classification = classify_outcome(x, y, THRESH_LOW, THRESH_HIGH)

    dp_pad = headline["pair_pad"]["delta_P_obs"]
    dp_absorb40 = headline["pair_absorb40"]["delta_P_obs"]
    rho = rho_pad_absorb(dp_pad, dp_absorb40, delta_P_obs_C40_C80)

    leg750_scored = score_leg750(g40_leg750_by_theta, c40_c80_leg750_rows, x, y)

    print(f"\n[HEADLINE] x=amp_ratio(PAIR_PAD)={x:.6f}  "
          f"y=amp_ratio(PAIR_ABSORB40)={y:.6f}", flush=True)
    print(f"  bins: x_bin={classification['x_bin']}  y_bin={classification['y_bin']}"
          f"  OUTCOME = {classification['outcome']}", flush=True)
    print(f"[DIAGNOSTIC, disclosed-only, non-gating] rho_pad_absorb={rho:.4f}  "
          f"(dp_pad={dp_pad:+.5f}deg dp_absorb40={dp_absorb40:+.5f}deg "
          f"dp_c40_c80={delta_P_obs_C40_C80:+.5f}deg, loaded not re-fit)",
          flush=True)
    print(f"[750nm LEG, advisory] x750={leg750_scored['x_amp_ratio_PAIR_PAD_750nm']:.6f}  "
          f"y750={leg750_scored['y_amp_ratio_PAIR_ABSORB40_750nm']:.6f}  "
          f"same_direction_as_600nm_headline="
          f"{leg750_scored['same_direction_as_600nm_headline']}", flush=True)

    total_new_runs = (pre["n_new_runs"] - 2  # the 2 reused-not-rerun 2800 pts
                       + remaining["n_new_runs"] + 2  # count them once, here
                       + leg750_res["n_new_runs"])
    total_elapsed = time.time() - t_start

    out = dict(
        experiment="076-t28-g40-pad-decorrelation", panel_iteration=53,
        lead_seat="QUANTUM OPTICS", halted=False,
        t1_escape_route="N/A (instrument/model-fidelity class, phase1_proposal.md Sec3)",
        geometry_congruence={k: v for k, v in geom.items() if k not in ("c40", "c80", "g40")},
        baseline_reproduction={k: v for k, v in baseline.items() if k not in ("data", "committed72")},
        thresh_low=THRESH_LOW, thresh_high=THRESH_HIGH,
        outcome_table_verification=verify,
        settle_precondition={
            "n_new_runs": pre["n_new_runs"], "elapsed_s": pre["elapsed_s"],
            "by_key": {f"{k[0]}_{k[1]}nm_STEPS{k[2]}": v
                       for k, v in pre["by_key"].items()},
        },
        settling_gate=gate,
        dense_angles=list(DENSE_ANGLES), leg750_angles=list(LEG750_ANGLES),
        block_dense_remaining={"n_new_runs": remaining["n_new_runs"],
                                "elapsed_s": remaining["elapsed_s"]},
        block_leg750={"n_new_runs": leg750_res["n_new_runs"],
                      "elapsed_s": leg750_res["elapsed_s"]},
        dense_g40_series=dense_g40,
        headline=headline, classification=classification,
        rho_pad_absorb=rho, delta_P_obs_PAIR_PAD=dp_pad,
        delta_P_obs_PAIR_ABSORB40=dp_absorb40,
        delta_P_obs_C40_C80=delta_P_obs_C40_C80,
        leg750_scored=leg750_scored,
        R_q_disclosure=("R_q is NOT used in the gating amp_ratio statistic "
                        "(A_i/A_q only); R_q IS used, via delta_P_obs, in the "
                        "disclosed-only, uncalibrated rho_pad_absorb "
                        "diagnostic, without null-calibration (docket item 3)."),
        total_new_runs=total_new_runs, total_elapsed_s=total_elapsed,
    )

    out_path = os.path.join(HERE, "results.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2, default=float)

    print(f"\n=== DONE: {total_new_runs} new FDTD calls, {total_elapsed:.1f}s "
          f"({total_elapsed/60:.2f} min) ===", flush=True)
    print(f"OUTCOME: {classification['outcome']}", flush=True)
    return out


if __name__ == "__main__":
    main()
