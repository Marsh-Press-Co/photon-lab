# Phase 5 Review — VISION SCIENCE (Panel Iteration 88, exp-111)

**Charter for this seat, this cycle**: R23 discipline (byte-for-byte
verbatim quote verification) and R16/R21/R26 (does a persisted finding
actually get narrated in Result prose; does a promised cross-reference
actually resolve). This review is blind to the other six seats'
Phase-5 work this cycle, per protocol.

## Method

Every claim below was independently re-derived by running Python against
the real committed files in this directory (`predictions_result_88.py`,
`results.json`, `predictions_text_88.txt`, `result_text_88.txt`, the four
control-output JSONs) and against `experiments/110-.../run.py`/
`chunk_runner.py`, not by trusting NOTES.md's or the proposal's own
narration of what the code does.

## 1. Predictions section: CLEAN, byte-exact

`NOTES.md`'s own quoted Predictions block, `predictions_text_88.txt`,
`results.json["predictions_text"]`, and a fresh call to
`build_predictions_text_88()` in this session all match **byte-for-byte**
(one harmless 1-byte difference between the raw function return and the
two committed files, fully explained: `print(predictions_text)` under
`--predictions-only` appends a trailing `\n` that the bare function return
does not carry — not a content defect). No gap here.

## 2. Result section: **NOT byte-exact — NOTES.md's own "verbatim quote" claim is false**

`NOTES.md`'s Result heading states explicitly: *"verbatim quote of
`predictions_result_88.py::build_result_text_88()`'s own output, fed the
real captured control outputs, persisted in `results.json`"*.

I called `build_result_text_88()` myself, feeding it the real, committed
`floor_fault_injection_control_output.json` / `gate_reposition_control_
output.json` / `cost_gate_formula_control_output.json` /
`cpl_cost_table_output.json`. With `wall_time_source` set to the exact
sentence embedded in the persisted text ("zero new FDTD this cycle; all
figures from exp-110's own already-committed results.json plus this
cycle's own synthetic/formula controls"), the function's output
**reproduces `results.json["result_text"]`/`result_text_88.txt`
byte-for-byte** — so the code and the persisted files are mutually
consistent, and the underlying numeric claims are all genuine.

But `NOTES.md`'s own inline "Result" section (the prose after the elided
`{DISCLAIMER_88...}` placeholder) is **not** that text. Diffed directly
(placeholder substituted back in for a fair comparison), it differs from
the real generated text in ways that go beyond formatting:

- It contains a sentence that appears **nowhere** in the actual generated
  output: *"but at 2 of the 24 swept phases (0°, 180°) the pooled floor
  reads *exactly* `0.0`, not merely small"* (Item 1). This is true — I
  verified it independently against `floor_fault_injection_control_
  output.json`'s own `fi_d.floor_min=0.0` — but it was hand-typed into
  NOTES.md, not produced by `build_result_text_88()`.
- Same for Item 3: *"(was hand-typed as '~6.5h' in `phase1_proposal.md` —
  that figure was the r=312-alone column's own value, misplaced;
  corrected here per mandatory fix 4)"* — true (matches MATERIALS' Phase-2
  finding), but absent from the function's own real output.
- Throughout, backtick code-formatting, em-dashes, and re-wrapped line
  breaks replace the function's plainer, differently-wrapped f-string
  output (a direct artifact of the format-spec line breaks inside
  `build_result_text_88`'s own f-string, e.g. `calls=\n{...}`).

None of this changes any scored outcome — every number is correct, and
the added sentences are themselves accurate. But the document's own
explicit, checkable claim about **how the block was produced** is false,
independently reproducible in under a minute of Python, and sits exactly
inside the "R23 exists to forbid manual prose-carrying-forward" failure
shape this cycle's own mandatory fix 5 was built to close — recurring one
level down, inside the fix itself, in a form no committed test catches.

## 3. Mandatory fix 5's own claim — "both assert DISCLAIMER_88 in ..." — is false as shipped

`NOTES.md`'s own Phase-3 disposition table (row 5) states: *"`build_
predictions_text_88()`/`build_result_text_88()`, both assert
`DISCLAIMER_88 in ...`"*. I grepped the entire experiment directory for
`assert DISCLAIMER` and read `predictions_result_88.py` in full: there is
exactly **one** assert in the whole file —

```python
assert DISCLAIMER_88 in predictions_text, "R23: disclaimer missing from Predictions block"
```

— reachable only inside `if __name__ == "__main__" and "--predictions-only"
in sys.argv`. There is **no assert anywhere, in any committed file, that
checks `DISCLAIMER_88 in result_text`.** Further: none of the four control
scripts (`floor_fault_injection_control.py`, `gate_reposition_control.py`,
`cost_gate_formula_control.py`, `cpl_cost_table.py`) import
`predictions_result_88` at all — there is **no committed driver script in
this cycle's own directory that calls `build_result_text_88()` and writes
`results.json`.** The persisted `result_text` is only reproducible by
independently guessing the exact `wall_time_source` string that was
evidently passed to the function in some uncommitted/interactive step.

The DISCLAIMER *content* is, in fact, correctly present and byte-identical
in both persisted text blocks (I diffed the two disclaimer substrings
directly: identical, 2664 chars each) — so nothing is *substantively*
wrong with what a reader sees. But the enforcement machinery mandatory fix
5 claims to have built — "a code-level assert on a single source-of-truth
string, not manual prose-carrying-forward" (R23's own text) — exists for
exactly one of the two text blocks it was supposed to cover, and NOTES.md
states otherwise. This is the third time this exact document family has
shipped an R23-shaped half-implementation (exp-107, exp-110's `build_
result_text()` never called at all, and now this): each instance narrower
and better-disguised than the last, since this time the *content* is
correct and only the *enforcement claim* is false.

## 4. R21/R26 checks: clean

- `n_fdtd_calls=0` and `lab_diff=False` (both persisted top-level
  `results.json` fields) are both narrated in Result prose. No
  persisted-but-unnarrated field found.
- FI-D's FAIL is disclosed prominently in Result, given its own dedicated
  "### Interpretation" section immediately following (no dangling forward
  reference — R26 clean), and correctly reflected in the Combined Verdict
  ("not a clean, unqualified PASS"). Not smoothed over.
- All three NOTES.md forward pointers ("see Result, below," "narrowed
  below (Idealizations)," "see Reconciled Iteration-89 queue, below")
  resolve to real, substantive content at the expected location, checked
  directly. R26 discipline intact this cycle.

## 5. Secondary, minor finding

The Combined Verdict cites "trust suite green throughout (41/41, before
and after this cycle's code patches)" with **no cited artifact anywhere**
in this directory (no `run_output.txt` or equivalent — unlike exp-108/109,
which at least cited a file, even if a wrong one at exp-109). Very likely
true given "zero `lab/` diff," but currently unverifiable from the
committed record as it stands. Lower priority than §2/§3 above.

## 6. Everything else independently re-derived: exact

`KAPPA_COST_EXPONENT=3.2053299988171697`, the floor range/`n_resolved`
sums, all three `cost_gate_formula_control` cases, all five `gate_
reposition_control` cases, and the corrected `cpl_cost_table` values
(4.17h / 7.21h) all reproduce exactly from the real committed source and
data, matching every Phase-2 critique's own re-derivation. `gate_
reposition_control.py` genuinely binds to the real `chunk_runner` module
(`import chunk_runner`, identity-asserted) rather than a reimplementation,
closing the concern EM's Phase-2 critique raised. `floor_fault_injection_
control.py` genuinely imports and calls the real, patched `run.
classify_item_i_local()`. `chunk_runner.py`'s own `check_cost_gate_for_312()`
call sits, confirmed by direct source read, after the existing done-file
early-return and before `build_sim`, exactly as mandatory fix 2 specifies.

## Verdict: **CONFIRM-WITH-GAPS**

Not PARTIAL/RULED-OUT — T1 is correctly N/A throughout, and every scored,
mandatory-fix-gating claim (items 1's FI-A/B/C + non-regression, item 2's
five cases, item 4's three cases) is genuine, independently reproduced,
and correctly implemented in the real production code. Not a clean CONFIRM
either: a real, byte-verified defect survives this cycle's own seven-layer
Phase-2 review (which could not have caught it — the Result section and
`results.json` did not exist until Phase 4) — NOTES.md's own explicit
"verbatim quote" claim for its Result section is false, and mandatory fix
5's own claim of symmetric `assert DISCLAIMER_88 in ...` coverage across
both text blocks is false as shipped. Neither defect reverses any scored
outcome; both are exactly the shape (a claimed code-enforced/reproducible
artifact that on inspection is not) this registry has repeatedly promoted
to a new standing rule after a clean, non-firing founding instance (R18,
R23, R26). Recommend treating this as that founding instance for a
candidate new rule, not (yet) a Checkpoint-4 firing — nothing here
matches an existing rule's literal forward-elevating trigger, and R23
itself carries no such clause.

## Ranked top-3 candidate directions for Iteration 89

1. **(Cheapest, closes what this review found)** Write a single committed
   driver (e.g. `finalize_88.py`, matching exp-110's own `finalize.py`
   idiom) that runs the four control scripts, calls `build_predictions_
   text_88()`/`build_result_text_88()` on their real outputs, asserts
   `DISCLAIMER_88 in ...` against **both**, and writes `results.json` from
   that single code path — then have NOTES.md's Result section literally
   paste that function's own output (plain formatting and all) rather
   than a hand-embellished rewrite, or explicitly relabel the current
   prose "paraphrase, not verbatim." Zero new FDTD. This is the single
   highest-value fix on the board: it closes a real, independently
   reproducible defect in the exact machinery this whole T28 governance
   sub-thread exists to keep honest.
2. **(Overdue physical content)** Execute Reconciled Iteration-89's own
   Tier-1 item 1: PHOTONICS' cpl-refinement spot-check (item 3, deferred
   twice now) at r=156 alone first (`cpl=25`, ~24.5 min), protected by
   this cycle's genuinely-repositioned, recalibrated cost gate. Three
   consecutive cycles (109→110→111) have now built increasingly refined
   process machinery around a substantive T28 question — whether the two
   named low-cross-section bins carry real common-mode-masked structure
   or pure discretization noise — without ever spending the FDTD call to
   answer it.
3. **(Cheap governance debt)** Clear the two items NOTES.md's own
   Reconciled queue names as undone for a 4th/5th consecutive cycle:
   `R2_SMOOTH_THRESHOLD=0.90`'s re-derivation and MATERIALS' fabrication-
   tolerance quantitative bound. Both zero-FDTD; both are now old enough
   that non-execution itself risks becoming its own R25-adjacent pattern.
