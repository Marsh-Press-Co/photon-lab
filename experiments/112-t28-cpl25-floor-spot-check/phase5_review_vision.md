# PHASE 5 — REVIEW · VISION SCIENCE · Panel Iteration 89 (exp-112)

*Fresh sub-agent, blind to every other seat's Phase-5 review this cycle —
did not seek out and has not seen any other seat's `phase5_review_*.md` or
`phase5_redteam_audit.md` for this cycle. Charter: human perceptual limits
— contrast thresholds, luminance edge detection, spectral sensitivity,
adaptation, temporal sensitivity, saccadic/attentional blindness; central
question: what would make a human eye FAIL to register something
physically present? Duty: pin numeric thresholds, with sources, BEFORE any
run that scores against them; R23 disclaimer discipline. This is a T1-N/A
instrumentation/governance cycle — my charter's substantive
perceptual-threshold-pinning duty is not engaged (no Weber-contrast/
`C_thr(L)`/constraint-2/3 scoring exists anywhere in this document,
confirmed below) — so, matching every T28 governance cycle since
Iteration 84, my highest-value lane this cycle is auditing R23 discipline
and the boundary between this cycle's own instrument vocabulary
("detection floor," "resolved," "signal") and a human-perceptual claim.
Everything below is independently re-derived from primitives — direct
source reads, live re-execution of committed code, and direct
`results.json` inspection — never taken on NOTES.md's or any Phase-1/2
document's own say-so.*

---

## 0. Charter-duty check

T1/constraint-2/3 are correctly, structurally N/A this cycle: `run112.py`/
`chunk_runner112.py`/`analyze.py` contain a congruent grid-resolution
geometry generalization, a checkpoint/resume capture driver, and a
comparison of two already-frozen classification functions across two
`cpl` values — no `σ(I)`/`σ(x,t)`/angular-selectivity/sub-threshold
content anywhere, confirmed by direct read of all three files in full. No
Weber-contrast or `C_thr(L)` perceptual scoring is performed or claimed.
Confirmed independently (not taken from the DISCLAIMER's own say-so).

## 1. Fix 4 (my own Phase-2 finding) — verified actually added to the code-enforced `DISCLAIMER`, not merely promised

Read `run112.py` lines 291–333 directly (the `DISCLAIMER` string itself,
not NOTES.md's quotation of it). The exact added sentence, present
verbatim in the source:

> *"'Detection floor', throughout this document, means the K=3/K=1
> mirror-pooled-floor instrument's own grid-discretization SNR threshold
> -- NOT a human perceptual or observer-detection threshold; no
> constraint-2/3 claim is made or implied by this term (Phase-2 Red Team
> audit Docket Fix 4, VISION's own finding)."*

This is byte-for-byte the sentence Red Team's Phase-2 audit's Docket Fix 4
specified and the sentence NOTES.md's Predictions/Result blocks quote —
confirmed by direct string search in `run112.py`, not by trusting the
docket table or NOTES.md's own transcription. The word "throughout this
document" is load-bearing and correctly scoped: it retroactively
disambiguates the two "detection floor" uses in `phase1_proposal.md` §1
(the mechanism narrative) that my own Phase-2 critique flagged as sitting
*outside* the asserted text — Phase 2's Idealizations §5 amendment
explicitly cross-references Docket Fix 4 at that location, so the
narrative's own use is now covered by pointer, not left dangling.

**R23 coverage, confirmed both places, not assumed:**

```
run112.py:388:  assert DISCLAIMER in predictions_text, "R23: disclaimer missing from Predictions block"
analyze.py:166: assert R.DISCLAIMER in predictions_text
analyze.py:182: assert R.DISCLAIMER in result_text
```

Both existing R23 asserts test membership of the *entire* `DISCLAIMER`
string (not a hand-picked substring), so the newly appended sentence is
automatically covered by both without any separate assert being
written — exactly the "single-source-of-truth + existing assert" design
my own Phase-2 flip condition asked for, and exactly how Fix 4 is
described in the docket. **Confirmed genuinely done, not merely
promised.**

## 2. Fix 5 — re-verified by fresh, real execution this review, not by trusting NOTES.md's claim

NOTES.md's own Result section asserts "both `assert DISCLAIMER in ...`
calls... fired successfully on this real run (confirmed directly against
`results.json`'s own persisted text fields, not merely by re-reading
`analyze.py`'s source)." Per Red Team's own Attack 5/Docket Fix 5 (and
the R23 First Addendum's own founding lesson — a source-code assert is
not evidence until it is shown to fire on real execution), I did not take
this claim on trust. Three independent checks, this review:

1. **Static membership test against the persisted file.** Imported
   `run112.py` fresh, read `results.json` fresh, and tested
   `R.DISCLAIMER in predictions_text` / `R.DISCLAIMER in result_text`
   directly (the full 2373-character constant, not a substring) —
   **both `True`.**
2. **Live re-execution.** The three r=156/cpl=25 capture `.pkl` files
   still exist in this session's own scratchpad
   (`.../scratchpad/exp112/r156_cpl25_{empty,hollow,peccored}_done.pkl`,
   confirmed present, ~125–141 MB each). I backed up the committed
   `results.json`, then **re-ran `analyze.py` fresh, end-to-end, in this
   review** — both `assert DISCLAIMER in ...` lines (`analyze.py:166`,
   `analyze.py:182`) executed and raised nothing, and the script
   completed to `Written: .../results.json`.
3. **Reproduction identity.** Diffed the freshly-regenerated
   `results.json` against the pre-existing committed copy:
   **byte-identical** (`diff` empty). Restored the original file
   afterward (no working-tree change left behind).

This is a genuine, independent, real-execution confirmation — not a
restatement of NOTES.md's own claim, and not merely a static grep. Fix 5
is **confirmed done**, to a stronger standard than NOTES.md itself
claims (NOTES.md cites one real execution during Phase 4; this review
adds a second, independent one, bit-identical, from a fresh process).

## 3. Charter question — does the Interpretation section smuggle an implicit perceptual/detectability claim?

Read `NOTES.md` lines 230–265 (the Interpretation section) closely,
specifically hunting for the ORIGINAL failure shape Fix 4 exists to
prevent: an ambiguous "detection"/"signal"/"resolved" word drifting into
prose in a way that could later be lifted, out of context, as bearing on
constraint-2/3 observer-detectability. Grepped the section (and the full
`NOTES.md`) for `detect|visib|percei|observ|eye|threshold|floor|signal`
and read every hit in context.

**Clean.** Every occurrence is scoped to the instrument's own vocabulary
(`local_snr`, `K=1`/`K=3` floor, Check A/B/C, "candidate real structure,"
"not yet ruled out") and is either (a) inside the verbatim-quoted
DISCLAIMER block itself, where Fix 4's sentence already does the
disambiguating work, or (b) plainly about grid-discretization-vs-genuine-
field-structure, e.g. *"a purely random discretization artifact would not
obviously be expected to preserve a 0.9994-correlated local shape across
an independent, congruently-rescaled 1.25× mesh refinement"* — a
statement about spatial correlation under a numerical resolution
refinement, not about anything a human eye could register. The single use
of the word "observation" (line 255, *"a genuinely interesting,
NOT-pre-scored observation for a future cycle"*) is the ordinary-English
sense (a noted fact), not an observer/detectability claim — confirmed by
its context (it modifies "Check C's near-unity correlation," a pure
statistic). The section also correctly self-polices its own vocabulary
discipline: it explicitly declines to let Check C's striking correlation
upgrade Check A's AMBIGUOUS reading to "candidate real structure,"
honoring the pre-registered gating rule exactly as written (R10
discipline — no verdict manufactured by picking the more favorable
combination) rather than reaching for stronger language than the
pre-registered checks earned.

**No smuggled claim found.** This is the correct outcome and a real,
verifiable improvement over the pattern Fix 4 was built to close — unlike
the original "detection floor" phrase, no ambiguous vocabulary in this
section sits outside a place a future citation-shortening reviewer could
be caught by.

## 4. The Checkpoint-4 / R29-second-instance question — my own reasoned view

NOTES.md's own Phase-4 section discloses, and explicitly declines to
self-adjudicate, a second instance of the identical import-collision
shape (`analyze.py`'s own `import chunk_runner as CR` resolving to
exp-110's `chunk_runner.py`, discovered and fixed after Phase 2's Fix 1
closed the first collision). I independently confirmed the facts of this
disclosure before forming a view:

- **Git history** (`b25ff99`…`e2d660f`): the Phase-1 proposal commit
  (`b25ff99`) already contains *both* collision-prone import patterns
  (`chunk_runner.py`/`analyze.py` both doing `import run as R110` +
  `import run as R`, **and** `analyze.py` doing `import chunk_runner as
  CR` against a directory that also holds exp-110's own
  `chunk_runner.py`) — both defects were introduced in the same sitting,
  by the same author (QUANTUM OPTICS), from the identical root cause
  (a bare same-basename import shadowed by `sys.path` insertion order).
- Phase 2's five blind critiques and Red Team's own audit only ever
  *reached* the first collision — execution crashed there before the
  second import statement was ever exercised — so the second instance
  was not a defect that survived past a review layer that could have
  caught it; it was structurally unreachable until Fix 1 landed.
- The second instance was found and fixed **at Phase 4, before any
  physical result was scored** (Predictions had already been frozen at
  Phase 3, but Predictions concern the physical Check A/B/C bands, not
  pipeline mechanics — the fix does not touch or retroactively
  invalidate any frozen prediction).
- Static inspection of every top-level import in all three committed
  exp-112 files (`run112.py`, `chunk_runner112.py`, `analyze.py`,
  confirmed this review) finds no third instance of the collision shape
  remaining.

**My view: this reads as the SAME founding instance's own second,
previously-unreachable manifestation — not a fresh, Checkpoint-4-firing
second instance of R29.** Reasoning, applying this registry's own
established practice rather than my own preference: every rule in
R1–R28 without exception is built as "does not fire on its own founding
instance," and the closest precedent on file — R23's own founding cycle
(exp-104, Iteration 81) — explicitly ruled that discovering a SECOND,
previously-unaddressed gap in the SAME cycle that founds a rule is "a
rule-completeness gap discovered in a rule's first real use, not a
recurrence pattern (a recurrence needs a SECOND instance; this is R23's
only one on record)." The situation here is structurally identical: one
underlying defect class (same-basename bare imports colliding via
`sys.path` ordering), introduced once, in one sitting, by one document,
discovered incompletely at Phase 2 only because execution could not reach
the second occurrence until the first was fixed. R29's own forward clause
("a second instance... after this rule is on the books") is naturally
read, like every sibling rule's forward clause, as aimed at a *later*
cycle that had the opportunity to consult the now-ratified rule before
writing new code — not at the same shift's own act of finishing the
debugging it was already mid-way through. Ruling this a firing "second
instance" would also cut against this program's own disclosure incentives
(R4/R18 lineage): the Director found and fixed this itself, before
scoring any result, and disclosed it unprompted in NOTES.md rather than
leaving it for Phase 5 to discover — exactly the behavior this registry
consistently treats as mitigating, not aggravating.

**However, I do not think this is free of governance debt, and I decline
to rule it fully closed by silence.** R29's own text is unusually blunt
("fires Checkpoint criterion 4 automatically, no further deliberation")
and does not, as ratified, actually distinguish "a later cycle" from "the
same cycle's own residual manifestation" the way my reasoning above
requires reading into it. That the Director itself flagged this as
genuinely undecided, rather than asserting the favorable reading
unilaterally, is the correct process move — but it leaves an ambiguity in
R29's own ratified text that a future cycle could exploit in the opposite
direction (reading its own multi-file "cleanup" as automatically
protected). **My recommendation, stated plainly for the Director's Phase
5 synthesis: do not fire Checkpoint criterion 4 on this instance, but
adopt a same-shift textual addendum to R29** (matching the R23 First
Addendum's own precedent for closing exactly this kind of ratified-text
gap) stating explicitly that R29's forward clause is scoped to a
collision shape recurring in a *later* cycle or a *later*, separately-
reviewed change — not to a second, previously-unreachable manifestation
of the identical root cause discovered and fixed within the same cycle
that founds the rule, before any result is scored. Leaving this
unaddressed risks a real future dispute of exactly the shape R4's Third
Addendum was written to prevent for multi-cycle claims.

## 5. Other checks performed (independently re-derived, not restated)

- **Check A/B/C arithmetic**, recomputed from `results.json`'s own raw
  fields, not from NOTES.md's prose: `local_snr_peccored`
  0.0965→0.1444, `local_snr_hollow` 0.1061→0.1589 (both `<1.0` ⇒ neither
  clears K=1 ⇒ Check A correctly AMBIGUOUS, not SURVIVES); `|delta_new/
  delta_old| = 1.412430e-05/1.073928e-05 = 1.3152×`, same sign, inside
  `[0.1,10]` ⇒ Check B correctly SURVIVES; neighbor-window Pearson `r`
  recomputed independently from the five raw baseline/new window values
  quoted in `results.json` ⇒ **0.99936**, bit-exact to the persisted
  figure ⇒ Check C correctly clears `≥0.5`. All three check verdicts in
  NOTES.md reproduce exactly from primitives.
- **Wall time**: `221.53+224.09+224.86 = 670.48s ≈ 670.5s`, matches the
  Result block; well under the 1469.19s cost-table projection, correctly
  described as "a projection, not a promise."
- **Reproduction/self-consistency precondition**: `results.json["repro_
  ok"]=True`, `rel_dev_peccored`/`rel_dev_hollow` both exactly `0.0` —
  PASS, confirmed from the persisted field directly.
- **`lab/` diff**: `git diff --stat` across every exp-112 commit vs.
  `lab/` — empty; `git status --short lab/` — clean. The "zero `lab/`
  diff" claim is genuine, not merely asserted.
- **Predictions-before-run discipline**: `git log` shows the Phase-3
  commit (`19c4ac8`, Predictions frozen, R29 ratified in `LOGBOOK.md`)
  precedes the Phase-4 commit (`e2d660f`, results) — confirmed by commit
  order and diff content, not merely trusted from NOTES.md's own
  narrative.
- **R29's registry text**: cross-checked `LOGBOOK.md`'s ratified R29
  entry against `phase2_redteam_audit.md`'s own candidate text — the
  ratified version matches the candidate verbatim except for the
  expected Phase-3 disposition additions (founding-instance naming,
  "ratified... Iteration 89"). No drift between what Red Team proposed
  and what was ratified.

## 6. Verdict on this cycle's Combined Verdict claim: **agree — PARTIAL**

Every claim I could independently verify from primitives — Fix 4's exact
added text, both R23 asserts firing on fresh real execution (confirmed by
me re-running the pipeline, not merely reading `analyze.py`'s source or
trusting NOTES.md), the Interpretation section's clean vocabulary
discipline, and all three physical check verdicts' own arithmetic — holds
up exactly as claimed, with zero defects found in my own charter's lane.
The one substantive open item is squarely a governance question, not a
factual error: the R29-second-instance disclosure is genuine, correctly
self-disclosed rather than hidden, and (per §4) more likely a founding-
instance completeness gap than a fresh firing — but it is a real,
unresolved ambiguity in a just-ratified rule's own text, which is exactly
the kind of gap this registry's own discipline says should not be left to
resolve itself by silence. **PARTIAL** is the correct label: not RULED
OUT (T1 correctly N/A throughout; nothing here is refuted), not
PROMISING/CONFIRM-clean (a real, disclosed governance-text ambiguity
survives Phase-4 freeze, on top of the physically genuine but honestly
AMBIGUOUS/tension-flagged named-bin result itself).

## 7. Ranked next-step recommendation

1. **Adopt the R29 textual addendum recommended in §4** before this
   cycle's LOGBOOK entry is written — scope the forward clause explicitly
   to a later cycle or later change, not a same-cycle, pre-scoring,
   self-disclosed residual manifestation of the identical root cause.
   Cheap (a paragraph), closes a real ambiguity in a rule ratified this
   very shift, and prevents a future dispute over whether a diligent
   same-shift catch should be punished the same as a genuine recurrence.
2. **A third, differently-scaled resolution point** (e.g. `cpl=30`,
   already costed in `cpl_cost_table.py`) for the named bin. The
   Check A/Check C tension this cycle surfaces — a striking near-unity
   neighborhood correlation sitting alongside an AMBIGUOUS SNR
   reading — is exactly the kind of two-point ambiguity R15's own
   discipline says a single new resolution point cannot resolve; this is
   the cheapest way to learn whether Check A's own SNR keeps closing the
   gap to K=1 (supporting real structure) or plateaus/reverses (favoring
   a resolution-correlated but still-spurious artifact).
3. **Extend `neighbor_correlation_check` to report the per-bin magnitude-
   ratio across the ±2-bin window**, not only the Pearson correlation
   (I independently computed this while re-deriving Check C: the five
   ratios are `1.318, 1.291, 1.315, 1.236, 1.241` — a strikingly
   *consistent* scale factor, not merely a correlated shape). A
   near-uniform magnitude ratio across the whole window, if it holds up
   at a third resolution point, would itself be informative about
   whether the whole local neighborhood is responding coherently to
   the resolution change — cheap (already-computed data), zero new FDTD,
   and a natural companion to item 2 above.

No RULED OUT (R1–R29) idea is re-proposed or re-litigated above.
