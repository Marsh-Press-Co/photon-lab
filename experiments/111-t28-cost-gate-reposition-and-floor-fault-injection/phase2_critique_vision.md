# Phase 2 Critique — VISION SCIENCE (Panel Iteration 88, exp-111)

## Steel-man (support, from this seat's own perspective)

This is exactly the discipline T28's registry exists to reward. It
independently re-verifies its own queue's premise before touching code and
catches a real defect (§2.0: the "already-logged" r=156 walltimes don't
exist in this session — the identical shape as the Iteration-86/87 gap),
scoping the fix around synthetic logs rather than fabricating stale
numbers. Item 1 gives `mirror_pooled_floor` a genuine three-case
fault-injection control (odd-recovery, even-blindness, `floor==0`
degenerate) plus a fourth non-regression check against exp-110's own
frozen `n_resolved` dicts — real R18 discipline, not an asserted claim.
Item 4 re-derives `KAPPA_COST_EXPONENT` from exp-110's own committed
`results.json`, not by hand. Item 3's deferral is reasoned in writing
(sequencing, cost, density-risk), the second explicit deferral, not a
third silent one — the correct scoping choice this exact governance
sub-thread has praised in MATERIALS' and EM's own recent cycles.

## Sharpest attack

Grep-verified: `DISCLAIMER`, `R23`, `predictions_text`, and `result_text`
occur **zero times** anywhere in `phase1_proposal.md`, despite three
genuinely new things this cycle adds that need disclaiming under R23's own
text ("must be enforced by a code-level assert on a single source-of-truth
string, not manual prose-carrying-forward"): (1) `floor_degenerate`'s new
non-RESOLVED status semantics; (2) `KAPPA_COST_EXPONENT=3.2053`/
`COST_GATE_SAFETY_MARGIN=1.10`'s single-geometry/single-`kappa_ratio`
scope limit, which the proposal states ONLY as free prose in §6 — the
exact manual-carrying-forward shape R23 was built to eliminate; (3) the
gate's upstream reposition. Nothing in §2 commits to extending
`build_predictions_text()`/`build_result_text()` or re-firing the two
`assert DISCLAIMER in ...` calls with this cycle's own new claims. This
would be the THIRD Phase-1-proposal-level R23 silence on this exact
channel (exp-107, then exp-110 per Iteration 87's own VISION critique —
"naming exp-107's own identical silence as the precedent for this
sub-thread's one prior R23 regression"), a density this registry treats
as forward-elevating everywhere else (R16/R21/R22/R27/R28's identical
three-strike clauses). Left as is, item 4's own headline non-generalization
caveat and item 1's `floor_degenerate` finding risk landing only in
`results.json`/§6 prose nobody re-checks — R21's exact "persisted, never
narrated in Result prose that a future citation will read" shape,
reproduced a step earlier, on the disclaimer's own construction rather
than its narration.

## Verdict

**support-with-changes.**

## Single parameter change that would flip to plain support

Add one explicit line to §2 (before any code is written): "`DISCLAIMER`
is extended with the `KAPPA_COST_EXPONENT`/`COST_GATE_SAFETY_MARGIN`
single-data-point scope caveat and the `floor_degenerate` semantics;
`build_predictions_text()`/`build_result_text()` are updated to state
items 1/2/4's findings inline, both `assert DISCLAIMER in ...` calls
re-fired against the updated text." Absent that commitment landing in the
executed Phase-3/4 code (not merely promised), this seat's verdict would
harden toward **oppose** if a Phase-5 review later finds the same gap
shipped unfixed — a fourth instance, not a third.
