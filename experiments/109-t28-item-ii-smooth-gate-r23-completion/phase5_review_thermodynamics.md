# PHASE 5 — REVIEW · THERMODYNAMICS · Panel Iteration 86 (exp-109)

Fresh sub-agent, blind to every other seat's Phase-5 review this cycle. Not
directly engaged this cycle (no thermal sidecar work) — this review audits
provenance/traceability of every cited number and the R4/R19/R21 lineage,
per this seat's program-honed role, and independently re-verifies my own
prior-cycle (Phase-2) mandatory fixes actually landed in executed code, not
merely in NOTES.md's restatement of them.

## 0. Scope of independent re-derivation

Read in full: `PANEL.md`, `LOGBOOK.md` (RULED OUT registry R1–R25, with R4,
R16, R19, R21, R25 read at full text, not summary), `PLAN.md`'s Current
state, `phase1_proposal.md`, all five `phase2_critique_*.md` (including my
own `phase2_critique_thermodynamics.md`), `phase2_redteam_audit.md`,
`NOTES.md` in full, `results.json`, `run_output.txt`, plus the actual
patched source: `experiments/108-.../run.py`, `experiments/108-.../analyze.py`,
`experiments/109-.../reclassify_108.py`, and `experiments/108-.../results.json`
(re-opened independently, not trusted from any restatement).

Every check below was run against the literal file, by me, this review —
not accepted from NOTES.md's or the audit's own quotation of itself.

## 1. My own prior-cycle mandatory fixes — verified in executed code, not narration

**Fix 4 (AND-reduction rule for `gate_p0_pass`/`repro_pass`).** Read
`reclassify_108.py` lines 84–87 directly:

```python
gate_p0_pass = bool(committed["tier1"]["r156"]["gate_p0"]["pass_"]
                     and committed["tier1"]["r312"]["gate_p0"]["pass_"])
repro_pass = bool(committed["tier1"]["r156"]["reproduction_precondition"]["pass_"]
                   and committed["tier1"]["r312"]["reproduction_precondition"]["pass_"])
```

An explicit, literal `and` of the two per-r booleans, in the code itself —
not left to a reader's inference, not merely stated in a docstring.
**CONFIRMED discharged, in the source, independent of NOTES.md's own
restatement of it.**

**Fix 5 (wall-time attribution note).** Read `results.json["result_text"]`
directly (not NOTES.md's quotation of it): the string contains, verbatim,
immediately after the wall-time line:
`"(exp-108's own historical spend, reused verbatim -- exp-109 makes zero new Sim.run() calls)"`.
Independently confirmed present via a substring check on the raw JSON
value, and traced to `build_result_text()`'s own new `wall_time_source`
parameter and `wall_time_note` f-string line in the patched
`experiments/108-.../run.py` (lines 352–353, 359). **CONFIRMED discharged
in the actual persisted artifact, not only in NOTES.md's prose.**

Both of my own Phase-2 mandatory fixes are genuinely wired into the
executed path — this document does not repeat the R24 failure shape
(a fix claimed "adopted in full" but never wired into the code it was
meant to gate) on either of my own two items.

## 2. Independent re-verification of exp-108's own committed `results.json` — the R4/R19/R21 standard

Opened `experiments/108-t28-reclassification-angular-pattern-batch/results.json`
directly, independent of exp-109's copy of these numbers:

- `n_fdtd_calls` = **6** (genuine top-level key, matches).
- `total_wall_s` = **7712.0** (genuine top-level key). Independently
  recomputed as `sum(v for r in wall_times_s.values() for v in r.values())`
  over the six `{r156,r312}×{empty,hollow,peccored}` entries →
  **7712.0 exact**, six entries counted (matches `n_fdtd_calls=6` — the R19
  call-count-vs-entry-count distinction holds up under an independent
  recount, not merely restated).
- `tier1.r156.gate_p0.pass_` = `True`, `tier1.r312.gate_p0.pass_` = `True`,
  `tier1.r156.reproduction_precondition.pass_` = `True`,
  `tier1.r312.reproduction_precondition.pass_` = `True` — all four source
  booleans independently re-read `True`, confirming the AND-reduction (§1)
  produces the correct headline PASS/PASS this cycle.
- `tier1.r{156,312}.item_ii.delta_values` → independently recomputed
  `np.std()`: **5.008327900579266e-06** (r=156) and **2.1240857290489e-06**
  (r=312) — bit-for-bit identical to `reclassify_108.py`'s own printed
  `raw_std` and to `results.json["item_ii_reclassified"]`'s `stat_used`.
- `fit["smooth"]` = `False` at both r (r²=0.6654/0.0205, both `< 0.90`),
  independently re-read — confirms both r take the raw-fallback branch as
  predicted.
- `tier1.r{156,312}.item_i/.item_iii/.closure_hollow/.closure_peccored` and
  top-level `item_iv` — all independently re-opened from exp-108's own
  `results.json` and diffed character-for-character against the strings
  embedded in exp-109's `result_text`: item_i verdicts (CONFIRM/CONFIRM),
  item_iii (`0.18275`→formatted `0.1827`, `0.2525`), closure figures
  (`0.000196`/`0.000563`/`0.000160`/`0.000581`), and the item_iv dict
  literal all reproduce exactly. **Nothing in the Result section's
  "unchanged this cycle" figures is hand-typed — every one traces to a
  real, re-openable key in exp-108's own committed file.**
- `source_results_json_sha` in exp-109's own `results.json`
  (`9bcdbdf7ca3066035363b61d272e921e133fb755`) — independently recomputed
  via `git hash-object experiments/108-.../results.json` on the currently
  committed file: **matches exactly**. This is a genuine, re-derivable
  provenance pointer, not a hand-typed hash.

## 3. Code-level re-verification (not NOTES.md's quotation of the code)

- `experiments/108-.../run.py:187–231` (`classify_item_ii`'s actual body,
  read directly): matches NOTES.md's "exact new body" block character for
  character, including the corrected two-sided conservative/liberal
  docstring language (ELECTROMAGNETISM's Phase-2 fix) and the
  `raw_over_residual_ratio` field.
- `experiments/108-.../run.py:304–369` (`build_predictions_text`,
  `build_result_text`, `DISCLAIMER`): matches verbatim; `wall_time_source`
  parameter and note line present exactly as claimed.
- `experiments/108-.../run.py:372–378` (`--predictions-only` block): the
  restored `assert DISCLAIMER in predictions_text` is present in the actual
  source, not only described.
- `experiments/108-.../analyze.py:85–92` (the line-85 companion edit,
  Attack 6/non-blocking): read directly — matches the "NEW" diff block in
  NOTES.md exactly, including all seven `item_ii_result[...]` keys threaded
  through. Genuinely applied, not merely narrated, though (as disclosed)
  not re-exercised against live data this cycle.
- `grep -c "assert"`: `run.py` = **1**, `reclassify_108.py` = **3** —
  independently recounted, matches NOTES.md's Result-section claim exactly
  (≥1/≥2 predicted, both cleared with margin).
- `DISCLAIMER` substring, `"CONFIRM"` count, both ratio strings
  (`1.729x`/`1.010x`), and the wall-time attribution sentence — all
  independently re-checked present in the raw `results.json["result_text"]`
  and `["predictions_text"]` string values via direct substring tests, not
  via NOTES.md's rendering of them.
- **Mandatory fix 6 (VISION, verbatim Result-section quotation)**:
  independently tested `results.json["predictions_text"].rstrip("\n") in NOTES.md`
  and the same for `result_text` — **both `True`**. NOTES.md's Result
  section genuinely quotes the persisted strings in full, not a paraphrase
  that merely looks similar.
- `git diff --stat lab/` — empty, both as a working-tree check and across
  the full commit range for this cycle. **Zero `lab/` diff confirmed
  independently**, corroborating the T1 N/A / zero-new-FDTD claim
  structurally, not just by assertion.

Every number and code claim above traces to a real, checkable source
exactly as this seat's charter requires — no R4-shaped hand-typed figure
found anywhere in the load-bearing chain (`classify_item_ii`'s outputs,
the DISCLAIMER pipeline, the AND-reduction, the wall-time note, the sha
provenance pointer).

## 4. One gap found: the trust-suite figure is not traceable to any committed artifact

NOTES.md's Result section states: *"trust suite green before and after
(41/41, `--only 12346789`, 100s/102s)"*. Unlike every other number checked
above, this figure has **no corresponding artifact anywhere in exp-109's
own committed record** — no log file, no captured stdout, nothing in
`run_output.txt` (which contains only `reclassify_108.py`'s own console
output, not a trust-suite invocation), and no reference to a suite-run
capture in `results.json`. I attempted to independently reproduce it this
review by re-running `lab/validation/run_all.py --only 12346789` myself;
stages 1–3 passed consistent with a healthy engine, but I did not complete
a clean from-scratch run to independently confirm the specific "41/41"
count or the "100s/102s" timing pair, so I can neither confirm nor refute
those exact figures from primitives.

This is structurally the R4 shape this seat exists to catch: *"any
falsifier or self-consistency figure cited... MUST be produced by invoking
the actual committed function... never hand-typed"* — generalized here from
a formula output to a suite run, but the same "was this actually invoked
and captured, or restated from memory/session scrollback" question. It is
**not load-bearing** to any scored verdict in this cycle: the cycle makes
zero new `Sim.run()` calls and zero `lab/` diff (independently confirmed,
§3), so nothing about the suite result determines whether item ii's
CONFIRM/CONFIRM holds. But it is the one number in this document's entire
Result section that does not trace to a committed, re-openable source the
way `n_fdtd_calls`, `total_wall_s`, both DISCLAIMER strings, the AND-gated
booleans, and the git-hash provenance pointer all independently do.
Flagged as a gap, not a defect requiring a re-run: a future cycle citing
this document's "41/41, 100s/102s" figure would be citing an unverifiable
number by the same standard this document itself applies rigorously to
everything else in its own chain.

## 5. Verdict: **CONFIRM-WITH-GAPS**

The substantive fix (item ii's `fit["smooth"]` gate, closing R24's second
instance) and both of my own prior-cycle mandatory fixes (the explicit
AND-reduction rule, the wall-time attribution note) are genuinely,
verifiably wired into the executed code and the persisted `results.json` —
independently re-derived from primitives in this review, not accepted from
any restatement, including NOTES.md's own. `n_fdtd_calls==6` and
`total_wall_s==7712.0` are confirmed as real source values from exp-108's
own committed `results.json`, independently recomputed from the underlying
`wall_times_s` entries (not merely read as a top-level key). VISION's
mandatory fix 6 (verbatim Result-section citation) is genuinely discharged,
confirmed by a programmatic substring test, not merely asserted. No
hand-typed figure was found anywhere in the load-bearing provenance chain
this review traced.

**The one gap**: NOTES.md's Result-section trust-suite figure ("41/41,
100s/102s") is the single cited number in this document with no
corresponding committed artifact — a non-load-bearing but real
traceability gap, in the same lineage as R4's standing rule, on a channel
(suite-run capture, not a formula output) this rule has not previously been
applied to explicitly. Does not rise to a Checkpoint-4-grade finding (one
instance, non-outcome-reversing, zero verdicts depend on it) — named here
so a future cycle does not cite it as independently verified when it is
not.

## Most important finding

Both of my own Phase-2 mandatory fixes (the AND-reduction rule and the
wall-time attribution note) are confirmed literally present in
`reclassify_108.py`'s source and in `results.json["result_text"]`'s actual
string value, independently re-derived rather than trusted from NOTES.md —
and every other number in the Result section traces to a real,
independently-recomputable source in exp-108's own committed
`results.json`, except the trust-suite "41/41, 100s/102s" figure, which
has no committed artifact anywhere in this cycle's record.
