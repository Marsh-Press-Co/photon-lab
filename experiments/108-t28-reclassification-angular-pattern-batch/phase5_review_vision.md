# PHASE 5 — VISION SCIENCE REVIEW · Panel Iteration 85 (exp-108)

## Verdict: **CONFIRM-WITH-GAPS**

The specific, narrow live-fire check I bound at Phase 2 genuinely ran and
is accurately reported. But a wider check this review was specifically
tasked with — whether `build_result_text()` is actually exercised, and
whether the resulting "genuinely R23-compliant" claim is earned —
surfaces a real, previously-uncaught gap in the R23 pipeline this cycle
claims to have closed. Not RULED OUT, not a Checkpoint-4 case on its own
(reasons below), but the record's own confidence language overstates
what was actually verified, and I say so on the record rather than
retroactively endorsing it.

## 1. Independent re-verification of the bound live-fire check

I did not trust NOTES.md's own report. I re-ran the check myself, from
this cycle's own committed files, not from any summary.

**`python3 run.py --predictions-only`, executed independently**: runs
cleanly, prints the `DISCLAIMER` string embedded in the predictions
block, byte-identical to `run_output.txt`'s own transcript and to
NOTES.md's own quoted excerpt. Confirmed genuine, not merely described.

**`grep -in disclaimer` across all four executable files, run myself**:

| File | My count | NOTES.md's claim | Match |
|---|---|---|---|
| `run.py` | 4 | 4 | Yes |
| `chunk_runner.py` | 0 | 0 | Yes |
| `analyze.py` | 0 | 0 | Yes |
| `reclassify_106.py` | 0 | 0 | Yes |

NOTES.md's reported hit counts are **accurate**, digit-for-digit. The
`results.json['r23_live_fire']` field (`predictions_only_ran: true`,
matching `disclaimer_grep_hits`) is consistent with both the transcript
and my own re-run. I also independently re-ran `lab/validation/run_all.py
--only 26` (item iv, the new suite stage): both checks reproduce exactly
(`0.000e+00` positive control, `2.000` negative control) — this specific
piece of the record is solid.

**So: the mandatory bound condition I attached at Phase 2, read
literally, was genuinely discharged.** This is not the disclaimer-erosion
pattern in its familiar shape (a claimed check that never ran, or a
disclaimer silently dropped from the source). Something did run, and what
ran is honestly reported.

## 2. The check I was specifically asked to make that nobody else made

Two questions the task brief posed, that no seat in this cycle's own
Phase 1/2/Red Team/NOTES.md record asks: is the `DISCLAIMER` text itself
adequate, and does `build_result_text()` — the other half of R23's own
founding two-function contract — actually execute anywhere.

**2a. Disclaimer content: adequate.** The `DISCLAIMER` string (`run.py`
line 254) covers all three things this cycle's own idealizations require:
raw-physical-ratios-only / no perceptual scoring ("no Weber-contrast or
`C_thr(L)` perceptual scoring is performed this cycle; not a claim about
human visibility"), the `angular_scattered_pattern` square-path
idealization ("not a true circular far-field pattern"), and the new
six-margin family's own un-derived status ("not independently re-derived
from a resolution or aliasing bound"). This is genuinely well-crafted —
no content gap here, and better-scoped than several prior cycles'
disclaimers (which needed a second sentence bolted on after Phase 5
caught a gap).

**2b. `build_result_text()`: defined, never called — dead code.**

- `grep -rn "build_result_text"` across the whole directory finds exactly
  two things: the function's own definition (`run.py:312`) and three
  prose *mentions* of its name (`NOTES.md:122`, `NOTES.md:573`,
  `phase1_proposal.md:155`, `phase1_proposal.md:185`). **Zero call
  sites.** Compare to `build_predictions_text()`, which the same grep
  finds actually invoked at `run.py:333` (`print(build_predictions_text())`,
  inside the `--predictions-only` branch).
- `run.py`'s own `__main__` block (lines 331–336) has exactly two
  branches: `--predictions-only` (calls `build_predictions_text()`) and
  else (prints a placeholder pointing to `chunk_runner.py`/`analyze.py`).
  Neither branch calls `build_result_text()`.
- `analyze.py` — the script that actually computes and prints every
  scored number in this cycle's Result section (items i/ii/iii, closure,
  gate P0) — never imports, calls, or even mentions `build_result_text`,
  `RESULT`, or `result_text` anywhere (checked by direct grep and by
  reading the file in full). Its own `__main__` prints raw f-strings
  directly (lines 123–129), not through the R23 pipeline.
- `chunk_runner.py` and `reclassify_106.py`: same, zero references.
- `results.json` has no `predictions_text` or `result_text` field at all
  (checked directly) — unlike exp-104's own founding pattern, which
  persisted both (`predictions_text=PREDICTIONS_TEXT`,
  `result_text=result_text`, exp-104 `run.py` line 777–778) specifically
  so the asserted string and the string a future citation would quote are
  the same object, not two independently-maintained texts.

**This is the exact silent-drop shape my seat exists to catch, present
in code, not merely alleged.** The RESULT half of R23's own two-part
founding contract (`experiments/104-.../run.py` docstring: *"the two
`assert DISCLAIMER in ...` calls below"*) does not exist in this cycle's
executed path at all. It exists only as an unused function definition
that happens to satisfy a grep count.

**2c. Zero `assert` statements anywhere — a regression below exp-105's
own single missing assert, not a repeat of it.** `grep -n "assert"
run.py` returns nothing. R23's own founding text (LOGBOOK.md ~908–920)
specifically mandates "**enforced by a code-level assert** on a single
source-of-truth string, not manual prose-carrying-forward" and names the
founding implementation as "two hard asserts." This cycle has none — not
one, not two. The `DISCLAIMER` constant is embedded into
`build_predictions_text()`'s f-string, so the two are consistent *by
construction* wherever that function actually runs — but nothing in this
codebase checks that at runtime, and the one place a check would matter
most (whether the RESULT text a future cycle will cite actually carries
the disclaimer) is never even generated, let alone asserted.

**2d. The actual Result-section prose is hand-typed, not code-generated
— precisely what R23 exists to prevent.** NOTES.md's own Result section
(lines 453–610) states the Item i/ii/iii/iv/closure numbers as
hand-written prose and tables, sourced from `analyze.py`'s printed
numbers and `analyze_output.json`, not from any call to
`build_result_text()`. The `DISCLAIMER` text itself never appears
verbatim anywhere in the Result section prose — only a *description* of
having grepped for it (line 568–581). This continues, unbroken, the
gap VISION's own Phase-5 review named at exp-105/exp-106 ("the Result
section's own prose never quotes the disclaimer text verbatim") — now a
third-plus consecutive cycle, still non-R23-violating by this program's
own precedent (R23's text scopes to the code-generated pipeline, not
NOTES.md's own hand-written narrative), but it means the one place a
future citation is actually likely to read from carries the disclaimer
only by careful hand-consistency, exactly the failure mode R23 was
built to retire.

## 3. Where this leaves the R23 scope ruling and the "genuinely
R23-compliant" claim

NOTES.md's Idealizations section states, verbatim: *"`DISCLAIMER` text
… applies unchanged to this cycle's own `run.py` … **Live-fire-verified,
not merely asserted (§Result, Phase 4).**"* And the Result section
itself: *"this cycle's own Tier-1 batch newly invokes the code-generated
pipeline and is genuinely R23-compliant, live-fire-verified."*

Both statements are **true only for the predictions half of the
pipeline** and **false, or at minimum unverified and unverifiable, for
the result half** — because `build_result_text()` never runs, there was
nothing for the live-fire check to have caught even if it had looked (it
didn't: the bound condition I attached at Phase 2 only specified
`--predictions-only`, not a check that `build_result_text()` itself is
exercised — a gap in my own Phase-2 flip condition, not only in this
cycle's execution of it, and I own that here). The word "pipeline" (a
single noun) is doing work to paper over the fact that only one of its
two named halves is live.

One additional, minor citation slip in the same paragraph: the mandatory
bound condition's own text (NOTES.md line 118) names the file to grep as
`finalize.py` — that file does not exist in this cycle's directory (it
was exp-107's file; this cycle's equivalent is `analyze.py`). The actual
Phase-4 execution correctly grepped `analyze.py` instead (matching
`run_output.txt`), so the substance is unaffected — an R4/R9-class
citation-hygiene note, not a live defect, flagged for completeness.

## 4. Does this rise to Checkpoint criterion 4 / a DISPUTE?

**No — reasoned explicitly, matching this program's own "does not fire
on a founding instance" and "R23 does not carry a forward-elevating
clause" precedent, applied to a new sub-shape of the same standing gap:**

- This is not a repeat of any of R23's three prior named instances
  (exp-104's scope gap, exp-105's missing assert, exp-107's zero
  disclaimer code) in the same shape — it is a new failure mode (a
  claimed dual-pipeline compliance where only one half is ever
  exercised, caught by a check that did not test for it), first
  identified this cycle, by this review.
- The substantive science this cycle produced (items i–iv, the
  reclassification fix, the six-margin floor characterization) does not
  depend on `build_result_text()` in any way — that function's absence
  from the executed path affects only the R23 governance claim's own
  evidentiary strength, not any scored physics result. T1 is correctly
  N/A throughout (independently confirmed, §5).
- The DISCLAIMER's own content is genuinely adequate (§2a) — this is a
  code-enforcement/verification gap, not an under-disclaiming of any
  actual claim made this cycle.
- No witness-statement constraint is implicated.

This is real, and load-bearing to the R23 scope ruling's own **evidentiary
strength** — not to any physics finding. It should be named as a fourth
R23 data point on the record (a fifth if exp-107's zero-disclaimer-code
gap and this cycle's are counted as the third and fourth non-firing
instances respectively) and explicitly queued for Iteration 86, not
folded into "closed on the record."

## 5. Structural constraint-3 check (charter duty, independent of the
above)

Re-confirmed directly, not accepted from Red Team's own scan: zero
occurrences of `C_thr`, `ambient`, `Weber`, or any perceptual-scoring
construction anywhere in `run.py`, `chunk_runner.py`, `analyze.py`,
`reclassify_106.py`, or the new `stage26_chunked_run_identity()` addition
to `lab/validation/run_all.py`. T1/constraint-3 is genuinely N/A
throughout this cycle — no numeric threshold of mine is needed before
this run, and none was scored against. My charter's "pin thresholds
before any run that scores against them" duty has nothing to discharge
here; the duty this cycle actually engages is the disclaimer-discipline
one, addressed above.

## 6. Recommendation for Iteration 86's queue

1. **Wire `build_result_text()` into `analyze.py`'s own `__main__`** (or
   an equivalent result-generation call site), with the two founding
   `assert DISCLAIMER in ...` statements restored — on both the
   predictions and result strings — matching exp-104's own founding
   two-assert pattern exactly, not a reduced version of it.
2. **Persist `predictions_text`/`result_text` (or their exp-108-scoped
   equivalents) into `results.json`**, closing the same gap R23's
   founding instance closed: the string a future citation quotes should
   be the same object a code-level assert checked, not a hand-typed
   paraphrase.
3. **Sharpen the R23 mandatory-live-fire-check convention itself**: a
   future cycle's Phase-2 flip condition binding a live-fire check should
   name explicitly "confirm every `build_*_text()` function this file
   defines has at least one call site," not only "run
   `--predictions-only` and grep." I own that this cycle's own binding
   condition (mine, from Phase 2) did not ask for that, and that gap is
   why this was caught only now, at Phase 5, rather than at Phase 4.
4. Correct the `finalize.py` → `analyze.py` citation slip in NOTES.md's
   own mandatory-condition paragraph (line 118) — non-blocking, R4/R9
   class only.
