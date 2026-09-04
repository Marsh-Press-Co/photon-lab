# PHASE 2 — CRITIQUE · VISION SCIENCE · Panel Iteration 87 (candidate exp-110)

Fresh sub-agent, blind to every other seat's critique this cycle. Read
PANEL.md, LOGBOOK.md in full (RULED OUT R1–R26, Live Threads T1/T28
Iterations 83–86), the Phase 1 proposal, and exp-108's own `run.py`/
`NOTES.md` (the R23 `DISCLAIMER`/`PREDICTIONS_TEXT`/`RESULT_TEXT`
machinery) before critiquing. Independently re-derived, not taken on
faith: exp-108's committed `sigma_abs`/`sigma_ext` figures (match the
proposal's cited 279.6607/560.1989 and 588.0218/1191.3259 exactly); all
four Item-2 synthetic-sequence fits by direct invocation of the real
committed `linear_fit_1_over_margin` (all four `(is_monotonic,
r_squared, residual_std, smooth)` tuples reproduce bit-exact); `stage26`'s
existing negative control (re-ran it: `2.000` exactly, matching the
proposal's cited "2.0 (200%)"); the mirror-index algebra and the actual
committed `bin_centers_deg` array (exact `reverse == negate`, 48 bins, 24
pairs, confirmed by direct array check, not just the stated formula).

## 1. Steel-man (≤150 words)

The grounding-fact correction (§0.5) is real, independently verified work,
not a rhetorical setup: I confirmed `results.json`/`analyze_output.json`'s
`item_i` genuinely carries only the seven keys claimed (no per-margin
pattern arrays), so the Iteration-86 queue's "zero new FDTD" premise for
item 1 really was false, and re-scoping to a minimal bit-identical
re-capture is the honest fix, not scope creep. Item 2's synthetic table is
exemplary R4/R18 discipline — I independently reproduced all four cases
bit-exact by invoking the real function, not a hand-derived table dressed
up as verified. Item 1's mirror-symmetry floor gate is a principled,
same-units instrument (avoiding R13's cross-family unit mismatch) kept
explicitly informational, correctly citing R24's own logic for why a
brand-new instrument must not be folded into a frozen verdict the same
cycle it is built. T1 is genuinely N/A throughout, confirmed structurally,
not merely asserted.

## 2. Sharpest attack (≤150 words)

Zero occurrences anywhere in this document of `DISCLAIMER`, `R23`,
`predictions_text`, `result_text`, `build_predictions_text`, or
`build_result_text` (grepped directly). Yet items 1c/1d write NEW
functions (`mirror_floor`, `classify_item_i_local`) extending
`angular_scattered_pattern`'s own six-margin family — the *exact* subject
of the existing `DISCLAIMER` string ("no Weber-contrast or `C_thr(L)`
perceptual scoring... not a claim about human visibility... the
absolute-floor six-margin family is a new convention"). Item 1b forks a
new `analyze.py`; item 2 forks a new `linear_fit_control.py`. None of the
parameter table or predicted outcomes says how, or whether,
`experiments/110-...`'s own eventual `results.json`/`NOTES.md` will carry
the two asserts exp-109 just finished restoring after exp-107 shipped a
cycle with genuinely zero `DISCLAIMER` code — and exp-107's own Phase 1
is the one prior proposal in this family that *also* never mentioned R23.
Silence here is the precise precondition of that prior regression, one
cycle after full compliance was finally reached.

## 3. Verdict: **support-with-changes**

## 4. Flip condition

Add one binding execution-requirement clause: item 1's new `results.json`
must call the existing `build_predictions_text()`/`build_result_text()`
(imported from the patched `experiments/108-.../run.py`, matching
`reclassify_108.py`'s own idiom) for whatever new predictions/result text
this cycle produces, assert `DISCLAIMER in` both, persist both, and
NOTES.md must quote `result_text` verbatim (closing my own prior-cycle
exp-108 §2d gap, not just the code/JSON half exp-109 closed) — reported
pass/fail before the Combined Verdict is written. With that clause I flip
to support.

## 5. Additional charter-duty notes (not word-capped)

**(b) Perceptual-relevance/threshold check — clean.** I searched for any
implicit human-perceptual-relevance framing (words like "notice",
"visible", "reader/reviewer would…", "obvious") — none found beyond one
unrelated metaphorical use ("not yet visible from a colder session," §0.5,
about code-archaeology, not vision). "Informational diagnostic" (item 1)
describes a verdict-scoping choice (R24 discipline), not a perceptual
claim. This is a genuine T1-N/A governance cycle exactly like
exp-107/108/109 — my charter's duty clause is not engaged this cycle, and
saying so plainly is itself the correct discharge of it.

**(c) Predicted-outcomes audit — one minor, non-load-bearing citation
imprecision.** §0.5 point 2 names the in-memory-only variables `analyze.py`
allegedly discards as `pattern_by_margin_delta[m]`,
`sigma_scat_by_margin_peccored[m]`, `sigma_scat_by_margin_hollow[m]`. I
read `analyze_r()` (lines 50–68, the range cited, correctly) directly: the
actual names are `pattern_delta[m]`/`pattern_peccored[m]`/
`pattern_hollow[m]`, and there is no top-level `sigma_scat_by_margin_*`
structure at all — the per-margin `sigma_scat` values live nested inside
`sum_check[m]["peccored"/"hollow"]["sigma_scat"]`. The substance is
correct (the data is computed per margin and discarded, unpersisted) but
the specific identifiers cited as evidence do not exist verbatim in the
source — an R4/R9/R20-lineage-adjacent precision slip, low severity
(non-outcome-reversing, would surface immediately when item 1b's own
persistence code is actually written against real names), flagged for the
record rather than as grounds to change my verdict. Everything else I
checked in the predicted-outcomes section (item 1a's reproduction figures,
item 2's full synthetic table, item 3's "2.0" precedent figure, the
mirror-index algebra) reproduced exactly from primitives.
