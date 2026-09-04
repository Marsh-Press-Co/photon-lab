# Phase 5 Review — MATERIALS & METAMATERIALS

**Panel Iteration 88, exp-111.** Charter: sub-wavelength structure; what
could physically realize the proposed optical behavior; owns the
realizability bound (published/plausible/unobtainium-with-parameters).
As at Phase 2, this bound is N/A directly (governance/instrumentation
cycle, T1 correctly N/A throughout, independently reconfirmed below).
Applying this seat's standing secondary duty instead — the one this exact
LOGBOOK registry (R4, R4 Third Addendum) has repeatedly shown this seat
discharges well: independently re-deriving every checkable numeric claim
from primitives, and independently re-reading primary source for every
claim about what code does, rather than trusting any prior layer's own
report of it (blind to this cycle's own Phase-5 siblings, per protocol).

I did not read any `phase5_review_*.md` or `phase5_redteam_audit.md` file
this cycle. Everything below was independently re-derived or re-read from
`phase1_proposal.md`, the five Phase-2 critiques, `phase2_redteam_audit.md`,
`NOTES.md`, `results.json`, and the actual committed source
(`experiments/110-.../run.py`, `chunk_runner.py`, `analyze.py`,
`experiments/111-.../*.py`), plus `experiments/110-.../finalize.py` (read
for comparison, since NOTES.md's own Setup section cites this exact file
as this sub-thread's established precedent).

## 1. The assigned re-verification: the cpl-table arithmetic slip

**Independently re-derived, from primitives, twice: once by hand
arithmetic against `results.json`'s own `t156`/`t312` figures, and once by
actually re-executing `cpl_cost_table.py` fresh in this session** (not
merely reading its committed output):

```
t156 = 752.2232966423035s, t312 = 6938.207038640976s  (exp-110's own committed results.json)
cpl=25 (ratio 1.25x): r156=1469.19s (0.4081h), r312=13551.19s (3.7642h), both=15020.37s = 4.1723h
cpl=30 (ratio 1.50x): r156=2538.75s (0.7052h), r312=23416.45s (6.5046h), both=25955.20s = 7.2098h
```

This reproduces `results.json["cpl_cost_table"]` exactly (`both_h=
7.209778439328074` at cpl=30) and confirms, independently, that
`cpl_cost_table.py`'s own actual output genuinely corrects my own seat's
Phase-2 finding: the cpl=30 "Both r" figure is **7.21h**, not the
proposal's original hand-typed "~6.5h" (which was the r=312-*alone*
column's own conversion, `23416.45/3600=6.5046`, misplaced into the wrong
cell). NOTES.md's Result section states this correctly ("cpl=25: 4.17h,
cpl=30: 7.21h ... corrected here per mandatory fix 4") and the correction
is genuinely code-generated, not re-hand-typed — I ran the script myself
and it reproduces this figure without modification. **Confirmed: my own
cycle's Phase-2 finding is genuinely, correctly discharged in the record.**

## 2. Independent re-derivation of every other headline claim

I re-ran or independently re-derived every script in the exp-111 directory
myself this session (not read-only inspection of committed JSON):

- `python3 cost_gate_formula_control.py` — reproduces all three cases
  exactly: positive `10.145960350566288`; non-regression
  `7632.027742505074s` (`<10800s`, PASS — an *over*estimate of the real
  `6938.207038640976s`, vs. the old formula's `6017.786373138428s`
  *under*estimate); discriminating case old=`10799.0s` (PASS) / new=
  `13695.778228220666s` (FAIL). Exact match to `results.json`.
- `python3 gate_reposition_control.py` — reproduces 5/5 PASS exactly:
  favorable reaches `build_sim` (calls=1, gate written first,
  `proceed_to_r312=True`); both unfavorable cases refuse before
  `build_sim` (calls=0); r=156 unconditional case reaches `build_sim`
  (calls=1); the already-done/stale-156 case (mandatory fix 2) returns
  `True` with zero gate evaluation, zero `build_sim` calls. Exact match.
- `python3 floor_fault_injection_control.py` — FI-A `5.0e-4` exact; FI-B
  `0.0` exact; FI-C `floor_degenerate=True`, all `resolved=False`, no
  `inf` in `local_snr`; FI-D floor range `0.0`–`3.534e-4` (70.7% of
  amplitude), **falsified on its own "never exactly zero" conjunct at
  phases 0°/180°** — I independently verified the stated mechanism by
  direct computation: `cos(2π·BIN_CENTERS_DEG/P* + phase)` is bit-exact
  even under `i↔47-i` at phase=0° (max asymmetry `0.0`) and to float noise
  at 180° (`2.1e-14`), and genuinely *not* even at 90° (asymmetry `≈2.0`,
  near its max possible value) — the Interpretation section's mechanism
  claim is correct, independently confirmed, not merely plausible-sounding
  prose. Non-regression: all 12 real cells match. Exact match to
  `results.json` in every numeric field.
- Independently recomputed `KAPPA_COST_EXPONENT` from
  `experiments/110-.../results.json` (`ln(9.223600318696624)/ln(2) =
  3.2053299988171697`) and the floor range/`n_resolved` sums — exact
  match to §2.0's frozen table.
- Read `chunk_runner.py`'s committed `step_once()` directly: confirmed the
  gate call sits **after** the existing `if os.path.exists(done_path):
  return True` early-return, exactly as mandatory fix 2 required (the
  proposal's own original diff had it *before*; the committed code is the
  corrected ordering). Read `analyze.py` directly: its `cost_gate_check()`
  comment now reads "downstream reporting copy" as claimed.

Every one of these figures is genuine, independently reproduced by
re-execution, not by trusting `results.json`. **Nothing wrong found in any
of this — this is a materially clean batch.**

## 3. A previously-uncaught gap: mandatory fix 5 (R23) is only half-implemented

NOTES.md's own Phase-3 disposition table (row 5) states mandatory fix 5
was implemented as: *"`predictions_result_88.py` — new `DISCLAIMER_88`...
`build_predictions_text_88()`/`build_result_text_88()`, **both** assert
`DISCLAIMER_88 in ...`"* — matching VISION's own Phase-2 flip condition
verbatim ("both `assert DISCLAIMER in ...` calls re-fired").

**I read `predictions_result_88.py` directly. This claim is false.** The
file contains exactly one `assert DISCLAIMER_88 in ...` statement, gated
behind `if "--predictions-only" in sys.argv:` in the `__main__` block, and
it checks only `predictions_text`. `build_result_text_88()` (lines
120–174) contains **zero** assert statements anywhere in its body, and no
call site for it exists anywhere — I grepped the entire repository for
`build_result_text_88` and `predictions_result_88`; the only hits are the
function's own definition and NOTES.md's prose. There is no committed,
re-invocable script that calls `build_result_text_88()` with real
arguments and asserts `DISCLAIMER_88` is present in its output.

This matters because this exact sub-thread already has the correct
pattern one cycle prior, cited by NOTES.md's own Setup section as
precedent: `experiments/110-.../finalize.py` calls **both**
`R.build_predictions_text()` and `R.build_result_text(...)`, then runs
**both** `assert R.DISCLAIMER in predictions_text` and `assert R.DISCLAIMER
in result_text` before persisting into `results.json` — a genuine,
committed, re-runnable enforcement of R23 for both halves. exp-111 did not
reproduce this pattern (no `finalize_111.py` or equivalent exists). The
`result_text` value actually present in `results.json`/`result_text_88.txt`
*does* contain `DISCLAIMER_88` verbatim (I checked by direct string
containment: `DISCLAIMER_88 in results.json["result_text"]` → `True`) — so
today's data is not wrong — but it was necessarily produced by an
un-committed, non-reproducible invocation, since no committed code path
produces it. A future edit that silently truncates or drops
`DISCLAIMER_88` from `build_result_text_88()`'s f-string would ship with
**zero code-level check**, exactly the "manual prose-carrying-forward"
failure shape R23 exists to forbid, and the same "necessary but not
sufficient" shape this exact sub-thread ratified as **R28** one cycle ago
(a gate that exists and is correct in one place is not the same as a gate
that is *traced end-to-end* everywhere it is claimed to be). This cycle's
own steel-man language — Red Team's Phase-2 audit called this proposal
"the cleanest T28 governance cycle I can independently verify in this
sub-thread's own record" — is not undermined in its numeric substance, but
this specific completeness claim, made in the same frozen document that
makes that boast, does not survive independent primary-source reading.

**Severity**: non-outcome-reversing (today's `result_text` content is
correct; T1 is still N/A; no constraint verdict moves). Real and
independently verified, not a matter of interpretation. Fits this
program's own established "necessary but not sufficient" pattern (R27/R28)
one layer further down the same cycle's own remediation of an R23 gap.

## 4. Two smaller, related gaps, also independently found

**(a) The control script's own top-level gate conflates informational and
mandatory-gating cases.** `floor_fault_injection_control.py`'s own
`__main__` block computes `all_pass = fi_a["pass_"] and fi_b["pass_"] and
fi_c["pass_"] and fi_d["pass_"] and non_regression["all_match"]` and then
`assert all_pass`. I ran this script directly this session:
`python3 floor_fault_injection_control.py` **raises an uncaught
`AssertionError` and exits non-zero**, because FI-D is (correctly,
per NOTES.md's own Interpretation section) predicted to fail and does
fail — but the code's own final gate does not distinguish FI-D's
disclosed-informational status from the four mandatory-fix-gating cases
(FI-A/B/C, non-regression). NOTES.md's own Combined Verdict calls this
"non-blocking," but the control script that is supposed to be this
finding's canonical, re-runnable evidence crashes when literally invoked
as intended — the "non-blocking" framing exists only in the surrounding
prose, not in the code's own pass/fail contract. (The JSON output is still
written correctly before the crash, which is presumably how
`results.json` ended up populated with the correct FI-D=`FAIL`
disclosure — but a bare re-run of this file, the R4-mandated verification
action, fails loudly for a reason the record does not warn a reader to
expect.)

**(b) One of five `gate_reposition_control.py` cases skips the
mandatory-fix-1 identity checks.** Mandatory fix 1 (EM, adopted in full)
required binding the control to the real, imported `chunk_runner` module,
verified by explicit identity assertions
(`chunk_runner.build_sim is stub`, `chunk_runner.step_once is
ORIGINAL_STEP_ONCE`) "before Phase 4 trusts this control's result." Four
of the five cases go through the shared `run_case()` helper, which
contains both assertions. `case_scope_precision_r156()` — the case
proving the new guard does *not* fire on r=156 — is implemented as its
own separate code block that patches `chunk_runner.build_sim` directly and
calls `chunk_runner.step_once(156, "empty")`, but never runs either
identity assertion. In substance it is still bound to the real module (it
uses the same imported `chunk_runner` object, never a local
reimplementation), so I do not believe this reverses any outcome — but the
mandatory fix's own explicit safety-check requirement was applied to 4 of
5 cases, not uniformly to all 5, an incomplete discharge of the same shape
R28 was built to catch (a check present in one place is not proof it is
present everywhere it is claimed).

## 5. Everything else I checked against NOTES.md's own text

- **T1 escape route N/A**: confirmed structurally correct for all three
  executed items (a boolean guard + status field; orchestration ordering;
  a wall-clock formula constant) — none touches σ(I)/σ(x,t)/angular-
  selectivity/sub-threshold content. Correctly, honestly stated.
- **Idealizations "Does NOT establish" bullets**: the
  single-geometry/`kappa_ratio=2.0` non-generalization caveat for
  `KAPPA_COST_EXPONENT`/`COST_GATE_SAFETY_MARGIN`, and the "does not
  resolve the two PHOTONICS-named bins" caveat, both check out against
  what items 1/2/4 actually touch — no overclaim found here.
- **Item-3 deferral (R25 discipline)**: genuinely a second explicit
  deferral, not a hidden third; carried forward as its own numbered
  Reconciled-Iteration-89 Tier-1 line (mandatory fix 7), not folded into a
  subordinate clause — confirmed directly in NOTES.md's own queue section.
- **"Zero `lab/` diff" / trust-suite-unaffected claim**: confirmed via
  `git log`/`git diff --stat` — no commit under `lab/` since Iteration 87
  (exp-110); the claim is a logically necessary consequence of an
  unmodified `lab/` tree, not a fabricated recomputation.
- **House discipline (predictions before code execution)**: confirmed via
  `git log` — Phase 3 commit (`9cee2bf`, includes `predictions_result_88.py`
  complete) precedes the Phase 4 commit (`f095726`, output JSONs/text
  files only) with no code changes in between.

## Verdict

**CONFIRM-WITH-GAPS.**

Every headline number in this cycle's own record — the corrected cpl-table
figure (this seat's own Phase-2 finding, genuinely and correctly
discharged), the recalibrated cost-gate exponent/formula's three control
cases, the fault-injection triad-plus-FI-D, the gate-reposition control's
five cases, the guard-ordering fix, the FI-D failure mechanism itself — is
independently reproduced here by direct re-execution or from-primitives
recomputation, not by trusting any committed artifact's own report of
itself. T1/constraint-3 are correctly, verifiably N/A throughout; nothing
about the physical mechanism is claimed or overclaimed. But NOTES.md's own
Phase-3 disposition table makes one concrete, checkable claim about its
own code — that mandatory fix 5 gives both `build_predictions_text_88()`
and `build_result_text_88()` a code-level `assert DISCLAIMER_88 in ...` —
that a direct read of the committed source shows is false for half of the
pair, with no committed script anywhere invoking the unenforced half. Two
smaller code/narrative-consistency gaps (§4) compound the same general
shape: a control's own written pass/fail contract not fully matching the
disclosed-non-blocking status of one sub-case, and one of five identity
checks not applied uniformly. None of this reverses any claimed outcome,
moves any constraint verdict, or implicates T1 — but it is real,
independently verified, and unflagged by any Phase-2 critique or the
Phase-2 Red Team audit (whose own steel-man specifically praised this
cycle's R23 completeness). This is not a large defect, but it is the kind
of "necessary but not sufficient" completeness gap this exact registry
(R27→R28) already teaches should not be waved through a second time under
a self-congratulatory framing.

## Top-3 candidate directions for Iteration 89 (own ranking)

1. **Close the mandatory-fix-5 gap found here before anything else,
   zero new FDTD.** Write a small `finalize_111.py` (mirroring exp-110's
   own precedent, `finalize.py`) that calls both
   `build_predictions_text_88()` and `build_result_text_88()` with real
   data and runs `assert DISCLAIMER_88 in ...` on both, replacing whatever
   ad hoc invocation actually produced today's `result_text`. Cheap,
   directly closes a gap this seat independently found and no one else
   caught, and prevents this exact "half-enforced R23" shape from
   recurring a fourth time on this channel.
2. **Execute item 3 as queued** (Reconciled-Iteration-89 Tier-1 item 1):
   PHOTONICS' own cpl-refinement floor spot-check at the two named bins,
   `cpl=25`/r=156-alone-first per this cycle's own regenerated (and, per
   §1 above, independently reproduced) cost table — now protected by a
   genuinely upstream, correctly-ordered, real-module-verified cost gate.
   This is the only item in the current queue with any actual physical
   content; everything else on the board this cycle and last has been
   governance.
3. **Tighten the two smaller gaps found in §4** alongside item 1 above:
   separate `floor_fault_injection_control.py`'s informational FI-D from
   its mandatory-gating `assert` (e.g., a `mandatory_pass`/`informational`
   split so a bare re-run doesn't crash on a disclosed, expected
   informational failure), and add the missing identity assertions to
   `case_scope_precision_r156()` for uniformity with the other four cases.
   Low cost, closes the loop on this review's own findings the same way
   this program has closed prior seats' Phase-5 findings same-shift.
