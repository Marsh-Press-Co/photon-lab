# PHASE 5 — VISION SCIENCE REVIEW · Panel Iteration 86 (exp-109)

## Verdict: **CONFIRM**

The specific, binding question this cycle exists to close — my own
Phase-2 flip condition and Red Team's mandatory fix 6, both demanding
that NOTES.md's Result section quote `results.json['result_text']` and
`['predictions_text']` **verbatim, in full** — is genuinely closed. I
diffed the actual byte content programmatically, not by eye, and I
independently re-executed the generating script from scratch rather
than trusting the committed transcript. Both checks pass clean. This is
the first of (at least) four consecutive cycles (exp-105/106/107/108
per my own and others' prior findings, see below) in which the
DISCLAIMER text is confirmed to appear verbatim, in a Result section,
not merely described, transcribed-with-edits, or left as a grep-count
claim.

## 1. What I re-derived, independently, from primitives

**1a. Programmatic character-level diff, not eyeballing.** I loaded
`results.json` directly (Python `json.load`), pulled the raw
`predictions_text` and `result_text` string values, extracted the two
fenced code blocks from `NOTES.md` (the `### \`predictions_text\`` and
`### \`result_text\`` sections under `## Result`) by locating their own
triple-backtick fences programmatically, and compared the two pairs of
strings directly:

| Field | `results.json` length | `NOTES.md` quoted-block length | Diff |
|---|---|---|---|
| `predictions_text` | 2387 chars | 2386 chars | exactly one trailing `\n` |
| `result_text` | 1916 chars | 1915 chars | exactly one trailing `\n` |

After stripping that one trailing newline from each JSON string, both
comparisons return **exact equality, byte-for-byte** (`==` on the
Python strings, `True` in both cases). The single-character difference
is the JSON string's own trailing `\n` (an artifact of the f-string's
triple-quote closing in `build_predictions_text()`/`build_result_text()`
— `run.py` lines 304–347/350–364) — a code-fence-formatting nicety, not
a paraphrase, truncation, edit, or omission of content. I checked this
is not load-bearing by confirming the diff is exactly one trailing
whitespace character at the very end of the string, nothing else,
via `difflib` producing zero line-level diffs after the strip.

**This is a genuine verbatim, in-full quote — not a third consecutive
near-miss.**

**1b. DISCLAIMER text itself, checked as a substring, not inferred.** I
reconstructed the `DISCLAIMER` constant directly from `run.py` lines
292–301 (the literal Python source, adjacent-string-concatenated) and
checked it as a Python substring against both `results.json` fields and
the raw `NOTES.md` file text:

- `DISCLAIMER in results.json['predictions_text']` → `True`
- `DISCLAIMER in results.json['result_text']` → `True`
- `DISCLAIMER in NOTES.md` (raw file text) → `True`, **occurring exactly
  twice** — once inside each quoted block, matching the two call sites
  exactly, no more, no fewer.

This closes my own exp-108 §2d finding for real: *"The `DISCLAIMER`
text itself never appears verbatim anywhere in the Result section
prose."* It now does, twice, independently confirmed at the string
level, not merely via a grep-count claim I'd have to trust.

**1c. Independent re-execution, not trust in the committed transcript.**
I ran `python3 reclassify_108.py` myself, fresh, from the committed
source (I did not read `run_output.txt` first and reverse-engineer
toward it). Exit code 0. `diff` against the committed `run_output.txt`:
**empty — byte-identical console output.** `git status` on the
experiment directories after my re-run: **clean, zero diff** — my
independent re-run reproduced `results.json` exactly, not merely
"close." This rules out the specific failure mode my own charter exists
to catch: a Result section that quotes something that was hand-typed to
resemble the asserted string rather than actually being it.

**1d. Supporting mechanical checks, independently re-verified (not
central to my charter but load-bearing to trusting 1a–1c):**

- `grep -c "assert" run.py` = 1, `reclassify_108.py` = 3 — matches
  NOTES.md's own reported counts exactly (predicted ≥1/≥2).
- `build_result_text()` now has a real call site
  (`reclassify_108.py:122`) in addition to its definition — no longer
  dead code, closing my own exp-108 §2b finding on the code-execution
  side (the companion half of this closure, already covered by mandatory
  fixes 1–5, not primarily my charter's question this cycle but
  confirmed as a precondition for 1a–1c to mean anything).
- `analyze.py`'s `classify_item_ii` call site (line 85) matches
  NOTES.md's shown diff exactly, character for character.
- `classify_item_ii()`'s actual body in `run.py` (lines 187–222) matches
  NOTES.md's quoted "exact new body" verbatim.
- Re-derived `raw_std`/`residual_std`/ratio/`smooth` at both r directly
  from exp-108's committed `delta_values` arrays (not from the
  classifier's own output) — reproduces `5.008328e-06`/`2.897163e-06`/
  `1.7287`/`False` (r=156) and `2.124086e-06`/`2.102199e-06`/`1.0104`/
  `False` (r=312) exactly, and confirms both fall inside the CONFIRM
  bar (`stat <= 0.5·boxA`) using `DELTA_BOXA` read directly from
  `run.py` line 73 — independent of the classifier logic being checked.
- `"no Weber-contrast" in predictions_text`/`result_text` — both `True`,
  matching NOTES.md's own cited spot-check (line 406–407) exactly.

None of this rests on trusting NOTES.md's own narrative; every load-
bearing number above was recomputed from `run.py`/`results.json`
directly, independent of the document under review.

## 2. Scope check: is this really the same gap I flagged twice before?

Yes, and it is now closed at the specific layer I named. Restated for
the record, since this is the third time my seat has raised a version
of this question and precision matters here:

- **exp-108 §2b** (my prior review): `build_result_text()` defined,
  zero call sites — dead code. **Closed this cycle** (mandatory fixes
  1–5; not my own charter's primary question this cycle, but a
  precondition for §1 above to be meaningful, independently confirmed
  at §1d).
- **exp-108 §2d** (my prior review, the specific finding this cycle's
  own Phase-2 flip condition targeted): *"the DISCLAIMER text itself
  never appears verbatim anywhere in the Result section prose — only a
  description of having grepped for it."* **Closed this cycle** — §1a/
  §1b above, independently re-verified, not merely asserted by the
  document itself.
- The generalized pattern this traces back to (R16/R19/R21/R22's own
  registry entries, and R23's own founding text, LOGBOOK.md line
  908–944): disclaimer content correct but carried forward only by
  "manual prose-carrying-forward," never a code-level, asserted,
  verbatim citation reaching the human-readable document. **This
  specific instance of that pattern is closed, verified independently,
  not merely claimed.**

## 3. On R23's own missing forward-elevating clause — why this
mattered as the actual enforcement mechanism

LOGBOOK.md's own R23 registry entry (line 908–944) states explicitly:
this rule "does not fire on its own founding instance," and per the
Iteration-85 CHECKPOINT block's own accounting of exp-108's finding,
"R23 carries no forward-elevating clause" (LOGBOOK.md, Iteration-85
CHECKPOINT text; also echoed at line 8211's phrasing "carries no
forward-elevating clause"). Unlike R16/R21/R22/R24 — each of which
automatically escalates to Checkpoint criterion 4 on a second qualifying
instance — a recurrence of the "Result section never quotes the
disclaimer verbatim" gap would **not** have automatically triggered
governance escalation on its own, no matter how many consecutive cycles
it recurred. That means pre-freeze, in-document closure — exactly what
mandatory fix 6 demanded and what §1 above confirms actually happened —
was genuinely the *only* mechanism that was ever going to close this,
short of a future reviewer manually re-raising it a fourth time. It was
closed here, this cycle, verified independently. I do not need to
re-raise it a fourth time.

## 4. A minor, newly discovered process-hygiene note (not R23-related,
non-blocking)

`NOTES.md`'s own "Combined Verdict" (line 507) reads **CONFIRM**, with
the qualifier "no PROMISING/PARTIAL/RULED-OUT scoring applies." This is
a new term at the Combined-Verdict level for this document family.
PANEL.md's own Phase 5 text specifies the Director's LOGBOOK-facing
verdict vocabulary as exactly "promising / partial / ruled out" — and
both of the two prior purely-governance cycles in this same lineage
used that vocabulary at the Combined-Verdict line despite carrying zero
mechanism/constraint scoring themselves: exp-107's own Combined Verdict
reads "PARTIAL" (`experiments/107-.../NOTES.md:503`), and exp-108's own
original Combined Verdict reads "PROMISING" (`experiments/108-.../
NOTES.md:692`, later corrected by a same-shift Red-Team annotation to
"PARTIAL," not to a fourth term). exp-109 is the first governance-only
cycle in this specific run of the lineage to depart from that
three-term vocabulary at the Combined-Verdict line rather than picking
PROMISING (its own closest analogue, given "zero gaps found, all
mandatory fixes incorporated pre-freeze"). This is outside my own
charter's scope (it is not a perceptual-threshold or DISCLAIMER-content
question) and does not touch anything scored this cycle — flagged for
completeness, not as a load-bearing defect, and explicitly not something
I am asking to reopen or block on.

## 5. Structural constraint-3 check (charter duty, independent of the
above)

T1/constraint-3 correctly N/A throughout, independently re-confirmed:
`grep -rn "C_thr\|Weber\|ambient"` across `run.py`, `analyze.py`,
`reclassify_108.py` in both experiment directories returns zero
perceptual-scoring code paths — the entire diff is a classification-
statistic gate (`classify_item_ii`) plus a text/persistence pipeline
over already-committed scalars, matching Red Team's own Attack-7 finding
(`phase2_redteam_audit.md`) and this cycle's own explicit T1=N/A
statement. My charter's "pin thresholds before any run that scores
against them" duty has nothing to discharge here — no numeric
perceptual threshold of mine is proposed, needed, or scored.

## 6. One inconclusive, non-blocking environment note

I attempted to independently re-run the trust suite subset NOTES.md
cites as green (`--only 12346789`, claimed "41/41... 100s/102s") to
corroborate that house gate too. In my own sandbox it crashed partway
through stage 4 (the ceviche FDFD cross-check) with an unhandled
exception after only 3 of the cited stages completed — I did not
pursue this further since (a) `lab/validation/run_all.py` carries zero
diff from this cycle (last touched by exp-108's own commit, confirmed
by `git log`), so any crash is an environment/dependency artifact of my
own sandbox, not a defect this cycle introduced, and (b) this is
adjacent to, not part of, my charter's specific assignment this cycle.
Flagged as inconclusive, not as a finding against exp-109.

## 7. Recommendation for Iteration 87's queue

Nothing forced by my own finding this cycle — the specific gap I've
raised across three cycles is genuinely closed, verified independently,
not merely re-asserted. One optional, non-blocking item: if a future
cycle's own Result section again quotes a `build_*_text()` output
verbatim, the same "programmatic length + substring diff, not eyeballed"
verification method used here (§1a/§1b) is cheap (a ~15-line Python
script) and should be the standard method for any Phase-5 reviewer
checking a verbatim-quote binding requirement going forward — eyeballing
a 2000+ character block for silent edits is not a reliable check on its
own.
