# Phase 2 Critique — VISION SCIENCE (blind)

## Steel-man (≤150 words)

Section 3's escape-route statement is stronger than most prior cycles':
it names the exact mechanism (`DISCLAIMER` sourced from
`thermo_sidecar.netd_disposition()`) and explicitly claims the string is
"asserted present in both `PREDICTIONS_TEXT` and `RESULT_TEXT`" — the
correct two-block pattern, matching exp-105's actual `run.py` lines 524
and 844 rather than the single-assert regression exp-105 itself shipped
with at Phase 1. It also correctly leans on PANEL.md's own binding spec
rather than re-deriving anything: `kappa_window` is *structurally*
distinguished from the ambient/Weber-contrast instrument, so no fresh
ΔC-style numeric proof is owed this cycle for a pure floor-gate/settling/
fixed-abs-control instrumentation change with zero mechanism variation.
Given T1:N/A and zero σ(I)/σ(x,t)/angular-selectivity content, deferring
to the already-settled structural argument rather than re-litigating it
is the right economy of effort.

## Sharpest attack (≤150 words)

§3's claim that the disclaimer is "asserted present in both
`PREDICTIONS_TEXT` and `RESULT_TEXT`" is *prose*, not a code
requirement — and identical prose is exactly what exp-105 shipped before
its own docstring's two-assert claim proved false in code (only
`result_text` was asserted; NOTES.md's own R23 finding). Worse this
cycle: §2c's new `window_floor_gate`/`frac_unresolved`/raw-array outputs
are described as additions to the **persisted record** (`results.json`),
and §4's `shape_ratio_fixedabs` CONFIRMS/REFUTES/AMBIGUOUS verdict and
§2d's `settling_pass_window` results are never explicitly said to be
concatenated *into* `predictions_text_`/`result_text` at all — they
could just as easily land in a separate printed table or bare JSON
field the two existing asserts never touch. That would be a **subtler**
third erosion instance than either prior one: the asserts would still
pass (DISCLAIMER's substring is still present via reused boilerplate)
while the cycle's actual new load-bearing numbers travel uncaptioned.
Nothing in §2/§3 pins which function assembles item-1/2/4's text.

## Verdict

**support-with-changes**

## Parameter change that would flip verdict

Add one concrete Phase-3 requirement to §3: the floor-gate (§2c),
settling (§2d), and fixed-abs `shape_ratio_fixedabs` verdict (§4) text
must be string-concatenated into the *same* `build_predictions_text()`/
`build_result_text()`-equivalent functions whose output the two
`assert DISCLAIMER in ...` lines already check — not printed or
persisted via a separate, unasserted path — with a pre-freeze grep
confirming exactly two (or more, if new blocks are added) assert sites
exist and both fire on the actual concatenated string, not on a
docstring's claim about it.
