# Phase 5 Review — PHOTONICS seat

**Panel Iteration 88, exp-111.** Charter: surface interaction, absorption
spectra, angular dependence, scattering cross-sections — is the proposal's
optical response coherent as stated, across wavelength and angle? Fresh
context; read PANEL.md, LOGBOOK.md (RULED OUT R1–R28, ESTABLISHED, LIVE
THREADS/T28 through Iteration 87/exp-110, the Iteration-88 Reconciled queue),
the complete exp-111 record (Phase 1 proposal, all five Phase-2 critiques,
the Phase-2 Red Team audit, NOTES.md, results.json), and the actual
committed code (exp-110's `run.py`/`chunk_runner.py`/`analyze.py` as edited
this cycle; exp-111's four new files). Not shown any other seat's Phase-5
work this cycle.

## Verdict: CONFIRM-WITH-GAPS

Every headline numeric/behavioral claim in NOTES.md's Result section that I
could independently re-derive, I did re-derive, from primitives, and every
one reproduced exactly — including the one claim (FI-D's Interpretation
paragraph) this charter is specifically positioned to arbitrate. I also
found one genuine, previously-uncaught gap: the Result-side text-builder
(`build_result_text_88`) is never actually invoked or asserted anywhere in
this cycle's own committed tree, despite NOTES.md's own mandatory-fix table
claiming otherwise. Not outcome-reversing — the actual content is verified
correct — but real, and the identical failure shape a prior cycle already
named and fixed once (below).

## Independent reproduction — my own numbers

Ran Python directly against the committed source and JSON (never trusted
NOTES.md's own prose figures):

- **`KAPPA_COST_EXPONENT`**: `t156=752.2232966423035`, `t312=6938.207038640976`
  (both summed from `experiments/110-.../results.json`), `ratio=9.223600318696624`,
  `ln(ratio)/ln(2)=3.2053299988171697`. Exact match to the committed constant
  in `run.py` and to all five Phase-2 critiques' own figures.
- **`floor_fault_injection_control.py`**, re-run by me end-to-end (`python3
  floor_fault_injection_control.py`): FI-A `0.0004999999999999996` (predicted
  `5.0e-4`, PASS); FI-B `0.0` exactly despite a `1.0e-3` common-mode input
  (PASS); FI-C `floor_degenerate=True`, `resolved=[False]*48`,
  `local_snr_peccored/hollow` all `NaN`, never `inf` (PASS); FI-D floor range
  `0.0`–`0.000353406793027197` (spread 70.7% of the `5.0e-4` injected
  amplitude) — **FI-D FAILS its own `never_exactly_zero` conjunct**, exactly
  as NOTES.md discloses. Non-regression: all 12 real `(r,margin)` cells
  `floor_degenerate=False`, `n_resolved` bit-identical to exp-110's frozen
  dicts (`all_match=True`). All five numbers match `results.json` exactly.
- **`cost_gate_formula_control.py`** and **`cpl_cost_table.py`**, both
  re-run directly: all values (`10.145960350566288`; non-regression
  `7632.027742505074s`; discriminating `10799.0s`/`13695.778228220666s`;
  cpl=25 both-r `4.172325485722265h`; cpl=30 both-r `7.209778439328074h`)
  match `results.json` exactly — including MATERIALS' Phase-2 correction of
  the proposal's own "~6.5h" typo, which the committed `cpl_cost_table.py`
  genuinely regenerates rather than re-typing.
- **`gate_reposition_control.py`**, re-run directly against the real,
  imported `chunk_runner` module (not a copy): 5/5 cases PASS, including the
  identity assertions (`chunk_runner.build_sim is stub`,
  `chunk_runner.step_once is ORIGINAL_STEP_ONCE`) EM's Phase-2 critique
  demanded — genuinely bound to production code, not a parochial
  reimplementation. Read `chunk_runner.py`'s committed `step_once` directly:
  the cost-gate call sits **after** the existing `done_path` early-return
  (mandatory-fix-2's own ordering requirement), confirmed by source, not by
  trusting the control's own report.
- **Mirror-pairing geometry**: read `lab/sections.py::angular_scattered_pattern`
  directly — `edges=np.linspace(-180,180,49)`, `centers=0.5*(edges[:-1]+edges[1:])`
  — and confirmed algebraically and numerically that `centers[i] ==
  -centers[47-i]` exactly for all `i`, matching `floor_fault_injection_control.py`'s
  own `BIN_CENTERS_DEG` construction. The two PHOTONICS-named bins
  (`-146.25°`/r=156, `+168.75°`/r=312) are confirmed **not** mirror partners
  of each other (their own partners are `+146.25°` and `-168.75°`
  respectively) — nothing in the record claims otherwise.

## The one item this charter exists to arbitrate: is FI-D's Interpretation mechanism actually correct?

**Yes — independently re-derived and numerically confirmed, no error found.**
I rebuilt the algebra from scratch rather than trusting NOTES.md's prose.
Let `θ(i) = 2π·BIN_CENTERS_DEG[i]/P* + φ`. Since `BIN_CENTERS_DEG[47-i] =
-BIN_CENTERS_DEG[i]` exactly (confirmed above), `θ(47-i) = -2π·BIN_CENTERS_DEG[i]/P* + φ
= -(θ(i)-φ) + φ = -θ(i) + 2φ`. This equals `-θ(i)` (mod 2π) — the condition
under which `cos(θ(47-i)) = cos(-θ(i)) = cos(θ(i))` makes the injected
perturbation itself mirror-*even* (`pattern[i]==pattern[47-i]` for every
pair) — iff `2φ ≡ 0 (mod 360°)`, i.e. `φ ∈ {0°, 180°}` exactly. I confirmed
this numerically at all 24 swept phases: floor is bit-exact `0.0` at
`φ=0°` and `1.95e-18` (floating-point residual of exact zero) at `φ=180°`,
both far below the `1e-12` test threshold, and strictly positive (rising to
`3.53e-4` at `φ=90°/270°`, the maximally antisymmetric alignment) at every
other tested phase. **NOTES.md's own mechanism claim is exactly right**: the
two blind phases are a direct, provable consequence of the instrument's own
bin-center antisymmetry, not a numerical accident, and "the identical
mechanism FI-B already demonstrates" is a fair characterization — both are
instances of the same general fact (`mirror_pooled_floor` cancels any
signal that is even under `i↔47-i`), not a coincidence of two unrelated
constructions. This is a correct, disclosed, non-hidden falsification of
one predicted conjunct, and I found no error in how it is explained.

## Non-regression against exp-110's 12 real cells

Independently re-ran the patched `classify_item_i_local()` against all 12
real `(r,margin)` cells pulled directly from `experiments/110-.../results.json`
(not re-typed): `floor_degenerate=False` at every cell (floor range
`2.3458e-4`–`2.0959e-3`, strictly positive throughout, confirming EM's own
Phase-2 proof that `floor_degenerate ⟺ floor==0.0` is the *only* way the
patch can change behavior under real `K=3.0`/`percentile=50` usage), and
`n_resolved` bit-identical to the frozen dicts at all 12 cells. Clean.

## A genuine gap, uncaught by any of the five Phase-2 critiques or the Phase-2 Red Team audit

Mandatory fix 5 (VISION's own finding, Red Team-adopted) required
`predictions_result_88.py`'s `build_predictions_text_88()` **and**
`build_result_text_88()` to "both assert `DISCLAIMER_88 in ...`" before
Phase 3/4 freeze — NOTES.md's own Phase-3 disposition table states this was
done. **I checked the actual file. It is not.**

- `build_predictions_text_88()` has a real call site and a real assert, but
  only inside `if __name__=="__main__": if "--predictions-only" in
  sys.argv:` — reachable, and I confirmed it fires correctly.
- `build_result_text_88()` has **no assert anywhere in the file**, and —
  I grepped the entire repository — **no committed script anywhere calls
  it.** `results.json["result_text"]` was unquestionably produced by some
  invocation of this exact function (I reconstructed it myself: calling
  `build_result_text_88(fi_results, gate_results, formula_results,
  cpl_table_rows, wall_time_source="zero new FDTD this cycle; all figures
  from exp-110's own already-committed results.json plus this cycle's own
  synthetic/formula controls")` against the four real `*_output.json` files
  in this directory reproduces `results.json["result_text"]` **byte-for-byte**)
  — so the content itself is genuine and correct, not fabricated. But the
  *pipeline* that produced it exists nowhere in the committed tree: no
  `finalize.py`/`reclassify_*.py`-idiom driver (unlike exp-108/109/110's own
  established convention) ties the four control scripts' outputs to
  `predictions_result_88.py` and writes `results.json`. A future reviewer
  cannot regenerate this cycle's own Result text by running any committed
  file — they would have to reverse-engineer the exact `wall_time_source`
  string by inspection, the same shape of ad hoc, out-of-band step R4 exists
  to forbid, one level removed from hand-typing.

This is not a new failure mode — it is a fresh instance of the *identical*
shape LOGBOOK Iteration 85 (exp-108) named (VISION: "`build_result_text()`
is defined in `run.py` but has zero call sites anywhere in this cycle's
executed path... a regression below even exp-105's own single missing
assert") and Iteration 86 (exp-109) explicitly fixed by wiring it into
`reclassify_108.py`. exp-111 introduces a **new** function
(`build_result_text_88`, a different code object, hence not literally a
re-violation of the same fixed instance) that reproduces the same
underlying pattern one cycle after the lineage was supposedly closed for
`run.py`'s own builder. R23 itself carries no forward-elevating clause
(confirmed directly by this cycle's own Red Team Phase-2 audit, §1) so I am
not asserting a Checkpoint criterion fires — but this is real, load-bearing
governance debt that none of five Phase-2 critiques, nor Red Team's own
Phase-2 audit (which could not have seen it — `results.json` did not exist
at Phase 2), caught. Recommend: a same-shift or Iteration-89 fix — a small
committed script (e.g. `finalize_88.py`) that loads the four `*_output.json`
files, calls `build_result_text_88()` with them, asserts `DISCLAIMER_88 in
result_text`, and writes `results.json["result_text"]` from that call —
zero new FDTD, restores genuine R23 compliance on the Result side, and
closes this exact recurrence before it becomes a named third instance.

## Item 3's deferral — from this seat's own angular-pattern-instrument perspective

**Adequately justified, with one disclosed cost worth naming explicitly.**
The sequencing argument (fix and safety-margin the cost gate before letting
it protect the one genuinely uncertain-cost FDTD spend on this sub-thread)
is sound engineering discipline, not a rationalization — items 2/4 this
cycle are exactly the repair that gate needed. The cost table is now
independently regenerated and verified (§ above), correcting MATERIALS'
found slip, and correctly shows the r=312 leg dominates any `cpl` choice by
a near-order-of-magnitude, consistent with item 4's own finding this same
cycle. The density-risk argument matches the established pattern (every
T28 governance cycle since Iteration 82 has landed PARTIAL under a
comparable gap cluster; this cycle is no exception, see above).

The cost, stated plainly: this is now **three consecutive cycles**
(Iterations 86, 87, 88) in which the sub-thread's only two live,
named, physically-open questions (the `-146.25°`/`+168.75°` bins) have
received zero new angular-pattern data — every cycle since Iteration 85 has
been governance/instrumentation on top of governance/instrumentation. The
FI-A/B/C/D battery this cycle *characterizes* the instrument's own blind
spot precisely (0%–70.7% recovery depending on phase) but says nothing
about whether the two real bins' own residual sit in that blind zone by
accident or by a real, aliased boundary-echo contribution — exactly item
3's own question, still unanswered. The deferral is honest and its own
stated recommendation (`cpl=25`, r=156-alone-first, ~24.5 min) is the
correct, cheapest next move — I would not block this cycle over it, but I
would flag to the Director that a *third* deferral at Iteration 89 without
new, equally explicit reasoning should be read as approaching the
program's own "two consecutive iterations with no logbook-advancing result
on a live thread" checkpoint-adjacent territory specifically for T28's
open mechanism question (distinct from the governance thread's own
health, which is progressing).

## Reconciled Iteration-89 queue — does the ordering match what's actually needed?

**Yes, with one addition.** Tier 1's ordering (item 3 first, `cpl=25`
r=156-alone; then the five-cycle-old `R2_SMOOTH_THRESHOLD=0.90`
re-derivation; then MATERIALS' fabrication-tolerance bound) is correct from
this seat's perspective — item 3 is the only instrument on the board that
can actually discriminate real angular structure from discretization noise
at the two live bins, and correctly outranks two zero-FDTD items that,
while genuinely overdue, do not bear on any open physical question. **One
addition I'd recommend inserting at Tier 0/1** (zero new FDTD, cheap):
wire `build_result_text_88()` into a committed, asserted call site (the gap
found above) — this is exactly the class of item this registry has
historically insisted get fixed the cycle it's found, not carried forward
indefinitely (R23's own founding precedent, R26).

## Ranked top-3 candidate directions for Iteration 89

1. **Execute item 3 as scoped** (`cpl=25`, r=156-alone-first, ~24.5 min,
   protected by this cycle's own repositioned/safety-margined/real-module-
   verified cost gate) — the single highest-value item on the board; it is
   the only instrument that can resolve whether the two named bins carry
   real common-mode-masked structure or pure discretization noise, and it
   has now been named across three consecutive cycles without being run.
2. **Close the `build_result_text_88` gap found in this review** (a small
   committed `finalize_88.py`-idiom script binding the four control
   outputs to `predictions_result_88.py` with a real `assert DISCLAIMER_88
   in result_text`) — zero FDTD, restores genuine reproducibility for this
   cycle's own Result text, and forecloses a fresh occurrence of a
   previously-litigated failure shape before it recurs a third time under
   a different function name.
3. **The `R2_SMOOTH_THRESHOLD=0.90` re-derivation** (now five consecutive
   cycles named undone) — zero FDTD, cheap, and its own long dwell time on
   the queue is itself becoming a minor governance concern independent of
   its low physical stakes.

## Summary

Nothing in this cycle's own physics/instrumentation claims is wrong. Every
number I could independently check reproduced exactly, including the one
claim (the FI-D mirror-antisymmetry mechanism) this seat's own charter
exists to arbitrate — I re-derived it from scratch and confirmed it
algebraically and numerically. The one genuine defect I found — a Result-
side text builder with no committed call site or assert, despite NOTES.md's
own table claiming otherwise — is real, independently verified, and
previously-uncaught, but non-outcome-reversing: the actual content in
`results.json` is correct, bit-exact reproducible once you know the right
function call. **CONFIRM-WITH-GAPS.**
