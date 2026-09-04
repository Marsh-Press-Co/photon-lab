"""exp-111 -- Panel Iteration 88: R23 single-source-of-truth predictions/
result text. Mandatory fix 5 of phase2_redteam_audit.md Sec 5 (VISION's own
Phase-2 finding, adopted in full): this cycle introduces three genuinely
new claims (floor_degenerate's new non-RESOLVED status semantics; the
recalibrated cost-gate formula's own single-geometry/single-kappa_ratio
scope limit; the gate's causal reposition) that were disclosed only in
free Idealizations prose in phase1_proposal.md Sec 6 -- exactly the
"manual prose-carrying-forward" shape R23 exists to forbid. Red Team's own
mandatory-fix text explicitly permits "DISCLAIMER (or its Iteration-88
successor string)" -- this file defines that successor, DISCLAIMER_88,
rather than mutating exp-110's own frozen DISCLAIMER (which is already
verbatim-quoted as exp-110's own historical Predictions/Result text in
that cycle's own NOTES.md; mutating it in place would silently break that
prior cycle's own reproducibility, an R4-shaped regression this file
avoids by construction).
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "experiments", "110-t28-item-i-local-norm-and-controls"))

import run as R  # noqa: E402  -- exp-110's own DISCLAIMER (unmodified this cycle), patched classifiers

NEW_CAVEATS_88 = (
    " Panel Iteration 88 (exp-111) adds three new caveats to the above, "
    "carried forward as part of this same single-source-of-truth string "
    "(R23): (1) `floor_degenerate` is a new status field, distinct from "
    "`resolved`/RESOLVED -- it marks the genuinely degenerate case where "
    "the pooled floor itself collapses to exactly 0.0 (both parent "
    "patterns exactly mirror-symmetric); a bin with `floor_degenerate=True` "
    "is UNRESOLVED-BY-CONSTRUCTION, not silently RESOLVED, and its "
    "`local_snr_peccored`/`local_snr_hollow` fields are `nan`, not `inf`. "
    "(2) `KAPPA_COST_EXPONENT=3.2053299988171697` and "
    "`COST_GATE_SAFETY_MARGIN=1.10` are an empirical re-derivation from a "
    "SINGLE geometry/kappa_ratio=2.0 data point (exp-110's own r=156/r=312 "
    "combined wall times) -- this does NOT establish that either constant "
    "generalizes to a different kappa_ratio (e.g. a future r=624 point); a "
    "future cycle introducing one must re-derive or re-validate this "
    "formula, not assume it transfers. (3) The R27/R28 cost gate's own "
    "enforcement point is repositioned this cycle from `analyze.py` "
    "(downstream, reporting-only as of this cycle) to `chunk_runner.py` "
    "(genuinely upstream of every real r=312 `Sim.run()` call) -- verified "
    "by a control bound to the real, imported `chunk_runner` module, never "
    "a hand-copied reimplementation."
)

DISCLAIMER_88 = R.DISCLAIMER + NEW_CAVEATS_88


def build_predictions_text_88():
    return f"""PREDICTIONS (pre-registered, exp-111, Panel Iteration 88)

{DISCLAIMER_88}

**Item 1** (fault-injection control, `mirror_pooled_floor`/
`classify_item_i_local`): FI-A recovers `5.0e-4` exactly (`<1e-12` abs
diff). FI-B recovers `0.0` exactly (`<1e-12`) despite a 2x larger
common-mode input. FI-C (degenerate): `floor_peccored_pooled==
floor_hollow_pooled==0.0` exactly; post-fix, `floor_degenerate=True`,
`resolved==[False]*48`, and (closing QUANTUM's own Phase-2 finding)
neither `local_snr_peccored` nor `local_snr_hollow` is `inf` anywhere.
FI-D (PHOTONICS' own recommended addition, informational): the pooled
floor's recovered magnitude is NOT constant across a 24-point phase sweep
of a `P*=2.8421deg`-period synthetic perturbation (spread > 1% of the
injected amplitude), and no swept phase drives the floor to exactly 0.0
or exactly the full injected amplitude. Non-regression: the patched
function, re-run against all 12 real (r, margin) cells already committed
in exp-110's own `results.json`, reports `floor_degenerate=False`
everywhere and `n_resolved` bit-identical to the frozen dicts. Falsified
by any single deviation from the above.

**Item 2** (cost-gate reposition control, bound to the real `chunk_runner`
module): favorable case reaches `build_sim` (raises `StubReached`, call
counter `==1`), with `r312_costgate.json` written showing
`proceed_to_r312=True` BEFORE the stub is reached. Both unfavorable cases
(budget-exceeded; r=156 precondition incomplete) raise `RuntimeError`
before `build_sim` is ever called (counter `==0`), with the predicted
substring (`"REFUSED"` / `"not complete"`) present. The r=156 scope-
precision case reaches `build_sim` unconditionally (counter `==1`) --
the guard fires only for `r==312`. The fifth case (r=312 already DONE,
r=156 logs absent/stale) returns `True` immediately, WITHOUT evaluating
the cost gate at all (`r312_costgate.json` not written this call,
`build_sim` counter `==0`) -- the fixed guard ordering (done-check before
gate-check) never re-evaluates the gate on an idempotent status check.
Falsified by any call reaching `build_sim` in an unfavorable case, any
unfavorable case reaching it via `step_once(156, ...)` instead, or the
fifth case ever writing/evaluating the gate.

**Item 4** (cost-gate formula recalibration control): unit-arithmetic case
`==10.145960350566288` (`<1e-9`); non-regression case (exp-110's own real
r=156 pilot data) `==7632.027742505074s`, `<10800s` (PASS, an OVERestimate
of the real measured r=312 total `6938.207038640976s` -- the opposite
direction from the old formula's own `6017.786...s` UNDERestimate, the
fix's whole point); discriminating case: old formula (exponent 3.0, no
margin) `==10799.0s` (PASS), new formula `==13695.778220666s` (FAIL) --
the two formulas diverge in their pass/fail decision on this constructed
near-boundary input. Falsified if the non-regression case flips to FAIL,
or if the two formulas do not diverge on the discriminating case.

**Item 3**: no outcome predicted -- deferred, not run this cycle (see
NOTES.md Setup/Idealizations for the reasoned scoping decision and the
regenerated `cpl_cost_table.py` output, correcting Sec 3's own
hand-typed-table arithmetic slip MATERIALS' Phase-2 critique caught --
mandatory fix 4).

**T1**: N/A. Confirmed structurally: item 1 touches only a `floor>0.0`
boolean guard, a new status field, and a `nan`-vs-`inf` fill choice on an
already-informational angular-noise-floor diagnostic; item 2 touches only
checkpoint/resume orchestration (WHEN a chunk is permitted to run), not
what any chunk computes; item 4 touches only an exponent and a
multiplicative constant in a wall-clock projection formula. None of the
three scores or moves any constraint-1/2/3/4 verdict. Item 3, the one
item with any physical content, is untouched this cycle.
"""


def build_result_text_88(fi_results, gate_results, formula_results, cpl_table_rows,
                         wall_time_source=None):
    wall_time_note = f"\n({wall_time_source})" if wall_time_source else ""
    fi_a, fi_b, fi_c, fi_d, non_regr = (fi_results["fi_a"], fi_results["fi_b"],
                                        fi_results["fi_c"], fi_results["fi_d"],
                                        fi_results["non_regression"])
    both_pass_str = ", ".join(f"cpl={r['cpl']}: {r['both_h']:.2f}h" for r in cpl_table_rows)
    return f"""RESULT (exp-111, Panel Iteration 88)

{DISCLAIMER_88}

Zero new FDTD calls this cycle (items 1/2/4 are synthetic/orchestration/
formula-only, item 3 deferred), zero `lab/` diff.{wall_time_note}

**Item 1 (fault-injection control):** FI-A {'PASS' if fi_a['pass_'] else 'FAIL'}
(recovered {fi_a['floor']:.6e}, predicted {fi_a['predicted']:.6e}). FI-B
{'PASS' if fi_b['pass_'] else 'FAIL'} (recovered {fi_b['floor']:.6e} despite
{fi_b['injected_magnitude']:.1e} injected common-mode magnitude). FI-C
{'PASS' if fi_c['pass_'] else 'FAIL'} (`floor_degenerate`=
{fi_c['floor_degenerate']}, `resolved` all False={fi_c['resolved_all_false']},
no `inf` in `local_snr`={fi_c['no_inf_snr']}). FI-D (informational)
{'PASS' if fi_d['pass_'] else 'FAIL'} (floor range
{fi_d['floor_min']:.3e}-{fi_d['floor_max']:.3e}, spread
{fi_d['spread']:.3e} = {100*fi_d['spread']/fi_d['amplitude']:.1f}% of
injected amplitude -- phase-dependent, neither FI-A's full recovery nor
FI-B's exact blindness). Non-regression: all {non_regr['n_cells']} real
cells match={non_regr['all_match']}.

**Item 2 (gate reposition control, bound to the real `chunk_runner`
module):** {sum(1 for c in gate_results if c['pass_'])}/{len(gate_results)}
cases PASS. Favorable reaches `build_sim` (calls=
{gate_results[0]['build_sim_calls']}), gate written before the stub with
`proceed_to_r312`={gate_results[0].get('gate_proceed_to_r312')}. Both
budget/precondition-unfavorable cases refuse before `build_sim` (calls=0).
r=156 scope-precision case reaches `build_sim` unconditionally (calls=
{gate_results[3]['build_sim_calls']}). The already-done/stale-156 case
(mandatory-fix 2) returns True with zero gate evaluation and zero
`build_sim` calls, as predicted.

**Item 4 (cost-gate formula recalibration control):**
{sum(1 for v in formula_results.values() if v['pass_'])}/3 cases PASS.
Non-regression projects {formula_results['non_regression']['projected']:.3f}s
(overestimates the real measured r=312 total by
{formula_results['non_regression']['new_formula_overestimate_s']:.1f}s;
the OLD formula underestimated it by
{formula_results['non_regression']['old_formula_underestimate_s']:.1f}s).
Discriminating case: old formula {formula_results['discriminating']['old_formula_projection_s']:.1f}s
(PASS) vs new formula
{formula_results['discriminating']['new_formula_projection_s']:.1f}s (FAIL)
-- the two formulas diverge as predicted.

**Item 3 (deferred, not run):** regenerated cost table (`cpl_cost_table.py`,
correcting MATERIALS' own found arithmetic slip): {both_pass_str}.
Recommendation for Iteration 89 unchanged: `cpl=25`, r=156-alone-first.
"""


if __name__ == "__main__":
    if "--predictions-only" in sys.argv:
        predictions_text = build_predictions_text_88()
        assert DISCLAIMER_88 in predictions_text, "R23: disclaimer missing from Predictions block"
        print(predictions_text)
    else:
        print("This module holds Panel Iteration 88's own R23 predictions/result text only.")
