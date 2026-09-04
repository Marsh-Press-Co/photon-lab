# PHASE 5 — SELF-REVIEW · MATERIALS & METAMATERIALS · Panel Iteration 86 (exp-109)

Fresh sub-agent, no memory of authoring the Phase-1 proposal. Blind to
every other seat's Phase-5 review this cycle. Read PANEL.md, LOGBOOK.md in
full (RULED OUT registry R1–R25, R23/R24/R25 read at full length),
PLAN.md's Current-state (lines 25–260), the full exp-109 record in order
(`phase1_proposal.md`, all five `phase2_critique_*.md`,
`phase2_redteam_audit.md`, `NOTES.md`, `results.json`, `run_output.txt`),
and the actual patched code (`experiments/108-.../run.py`'s new
`classify_item_ii`/patched `build_result_text`/restored assert,
`experiments/108-.../analyze.py`'s patched call site,
`experiments/109-.../reclassify_108.py`). Every load-bearing number below
was independently recomputed from `results.json` primitives with a
throwaway Python session, not trusted from any document's restatement,
including my own Phase-1 proposal's.

---

## 0. Independent re-derivation of the headline numbers

From `experiments/108-.../results.json`'s own committed `tier1.r{r}.
item_ii.delta_values` and `.fit`, recomputed with `numpy.std(..., ddof=0)`:

| r | `raw_std` (=`stat_used`, non-smooth branch) | `residual_std` | `r_squared` | `smooth` | `raw_over_residual_ratio` |
|---|---|---|---|---|---|
| 156 | **5.008327900579266e-06** | 2.89716280726349e-06 | 0.66537... | `False` | **1.72870088...** |
| 312 | **2.1240857290489e-06** | 2.102199273342035e-06 | 0.02050... | `False` | **1.01041122...** |

Both match `phase1_proposal.md` §4's table, all five Phase-2 critiques'
figures, `phase2_redteam_audit.md` §0.1's table, `NOTES.md`'s frozen
Predictions/Result tables, and `experiments/109-.../results.json`'s own
`item_ii_reclassified.r{156,312}` block to full float precision — not
merely to the documents' own claimed `<1e-9`/`<1e-3` tolerances. CONFIRM
bars (`0.5·|Δ_boxA|` = 1.4845e-5 / 1.234e-5) and REFUTE bars clear exactly
as claimed; `new_verdict="CONFIRM"` at both r reproduces exactly.
`stat_source` contains `"raw/undetrended"` (not `"detrended"`) at both r,
confirmed by direct read of `results.json`. **No arithmetic discrepancy
found anywhere in this cycle's numeric chain.**

Also independently re-traced `classify_item_i()` (`experiments/108-.../
run.py:234–286`, unmodified this cycle): `linear_fit_1_over_margin` is
called exactly once, inside `for (i0,j0) in runs:`, and CONFIRM requires
`confirm_all_margins and not runs` — i.e. CONFIRM is reachable only when
that loop body never executes. This independently confirms PHOTONICS'
Phase-2 finding and Red Team's §0.2 re-trace: `classify_item_i()`'s
CONFIRM branch is *structurally incapable* of facing a smoothness
judgment, not "deliberately unconditional" on one — my own Phase-1
proposal's §4 rejection of alternative (b) misdescribed this code.

Also confirmed: `grep -c "assert"` → `run.py`=1, `reclassify_108.py`=3
(NOTES.md's claimed "≥1"/"≥2" predicted, "1"/"3" reported — both match
live); `n_fdtd_calls=6`/`total_wall_s=7712.0` are genuine top-level keys
in exp-108's own `results.json`; `gate_p0.pass_`/`reproduction_
precondition.pass_` are `True` at both r; `"no Weber-contrast" in
predictions_text`/`result_text` both `True`; `predictions_text`/
`result_text` as quoted verbatim in `NOTES.md`'s Result section match
`results.json`'s own strings character-for-character (checked by direct
string comparison, not eyeball). Item i/iii/iv/closure figures reproduced
in `result_text` all match exp-108's own committed `results.json` exactly
(`0.18275`/`0.2525`, `closure_hollow.r156.closure=0.000196...`, etc.).

**Verdict on the substantive fix itself: sound.** The OLS-with-intercept
inequality is textbook-correct for `A_mat=[1,1/margin]`; the CONFIRM/
CONFIRM outcome is genuine, not an artifact of a miscomputed threshold or
a mis-cited figure.

---

## 1. Auditing my own Phase-1 proposal's six flagged defects — did the fixes actually land?

### 1a. Item-i sibling-code misdescription (fix 1, PHOTONICS + Red Team)

**PARTIALLY LANDED — a real, newly-discovered gap.** My own Phase-1 §4
claimed `classify_item_i()`'s CONFIRM branch is "unconditional on
smoothness... exactly because a null finding needs no trend-removal story
to be believed" — a considered-design-choice framing that both PHOTONICS
and Red Team (independently, from source) showed is false: the branch
never reaches the smoothness test at all. `NOTES.md`'s own "how each fix
is incorporated" list (item 1) promises this is *"Corrected below (§ 'Why
raw std, not forced AMBIGUOUS')"*. **I grepped the entire frozen
`NOTES.md` for that exact section header and for `"forced AMBIGUOUS"`/
`"alternative (b)"`/`"alternative (a)"` — the only hit is the sentence
making the promise itself (line 62). The named section does not exist
anywhere in the committed document.**

What actually happened: the flawed analogy was *silently dropped* from
`classify_item_ii()`'s new docstring (which cites only the OLS inequality
and the original Iteration-85 fix's own text as grounds — accurate, and
not repeating the error) rather than *corrected and displayed* as
`NOTES.md`'s own fix-1 disposition promises. The net effect is
non-outcome-reversing (the misdescription no longer misleads a reader,
since it isn't repeated anywhere) but the frozen record never actually
walks through *why* alternative (b) — forced AMBIGUOUS — is rejected in
its own right; that discursive argument (present in `phase1_proposal.md`
as three lettered bullets, including the rejection of alternative (c))
is nowhere reproduced or superseded in `NOTES.md`. A reader who trusts
`NOTES.md`'s own "Combined Verdict — All six Red Team mandatory fixes
were incorporated before this run (not after)" claim has no way to find
where fix 1 actually landed.

This is worth naming precisely because of what this cycle exists to
close: R24 is "a Phase-2 mandatory fix's own specified consequence...
once a Phase-3 synthesis states it was 'adopted in full,' must be
implemented... not merely computed and left as an unscored, disclosed
observation." My fix 1 is not a classification-string consequence (so it
does not literally re-trigger R24's own classification-verdict shape),
but it is the *same failure geometry one level down in the document*: a
mandatory fix's own Phase-3 disposition cites a specific, named location
for its correction, and that location is empty. I flag this as a **new,
distinct documentation-completeness defect** — not a re-filing of R24
itself (a Director/Red-Team call, not mine), but structurally adjacent to
it and worth the Director's attention before this document is cited
again.

### 1b. "Conservative in every case" overclaim (fix 2, ELECTROMAGNETISM)

**LANDED, verified in both places it needed to land.** The corrected
two-sided statement (conservative against false-CONFIRM, liberal against
false-REFUTE) appears both in `classify_item_ii()`'s own docstring/
`stat_source` string (read directly from `run.py:187–222`, and confirmed
present verbatim in the live-executed `stat_source` in
`results.json['item_ii_reclassified']`) and in `NOTES.md`'s own fix-2
prose. This is the one fix whose "must live in the generated string, not
just human prose" bar (explicitly demanded by EM's own flip condition) I
independently confirmed met by reading the actual f-string in source, not
by trusting `NOTES.md`'s claim that it was done.

### 1c. Undisclosed raw/residual ratio (fix 3, QUANTUM OPTICS)

**LANDED.** `raw_over_residual_ratio` is a real, persisted key in
`classify_item_ii()`'s return dict (`run.py:229–231`), threaded into
`stat_source`'s own f-string, and present in both `analyze.py`'s patched
call site and `experiments/109-.../results.json`'s
`item_ii_reclassified` block — 1.7287/1.0104, matching my own
independent re-derivation to full precision.

### 1d. Undisclosed AND-reduction (fix 4, THERMODYNAMICS)

**LANDED in code; not landed in docstring, as literally promised.**
`reclassify_108.py:84–87` computes `gate_p0_pass`/`repro_pass` as an
explicit `and` of both r's `pass_` fields — genuinely explicit, not
inferred. But fix 4's own text asked for this "in `reclassify_108.py`'s
own code **and docstring**" — the module docstring (top of the file)
describes the script's general purpose only; there is no comment at
lines 83–87 stating the reduction rule in words. Low severity (the `and`
keyword is self-evidently unambiguous to any reader of the code itself,
unlike fix 1's case where the promised prose is the *only* place the
corrected reasoning was ever going to appear) — noted for completeness,
not elevated.

### 1e. Wall-time attribution gap (fix 5, THERMODYNAMICS)

**LANDED and verified live-fired.** `build_result_text()` gained the
optional `wall_time_source` parameter (confirmed in `run.py:350–370`);
`reclassify_108.py`'s own call passes the attribution string; the
executed `result_text` in both `run_output.txt` and `results.json`
contains the line `"(exp-108's own historical spend, reused verbatim --
exp-109 makes zero new Sim.run() calls)"` immediately after the
"7712.0s... total wall time" line — checked by direct string search, not
trusted from NOTES.md's restatement.

### 1f. Unbound human-readable-citation half (fix 6, VISION SCIENCE)

**LANDED, and independently verified byte-for-byte.** I extracted the two
code-fenced blocks under `NOTES.md`'s own "`predictions_text`" and
"`result_text`" headings and diffed them programmatically against
`results.json['predictions_text']`/`['result_text']` — identical modulo
one trailing newline from markdown-fence extraction (immaterial). This is
a genuine verbatim quotation, not a paraphrase — the strongest of the six
fixes in terms of actual, checked execution.

**Net on the six flagged Phase-1 defects: 4 of 6 (fixes 2/3/5/6) landed
cleanly and were independently re-verified from source, not merely
trusted; fix 4 landed in substance (the code is unambiguous) but not in
the literal "and docstring" form promised; fix 1 is the one real gap —
the correction is not wrong, it is simply absent from the location
`NOTES.md` itself says to look.**

---

## 2. A newly discovered defect neither Phase 1, Phase 2, nor Red Team could have caught (post-freeze, execution-only)

**`NOTES.md`'s Result section states:** *"trust suite green before and
after (41/41, `--only 12346789`, 100s/102s). Full console record:
`run_output.txt`."*

I read `run_output.txt` (81 lines, git-tracked, `git show 7783f95 --stat`
confirms it is the actual committed console capture for this cycle's
Phase-4 run) in full and grepped it for `"trust suite"`, `"41/41"`,
`"--only 12346789"`, `"checks passed"`, and `"stage "` — **zero matches.**
The file contains only `reclassify_108.py`'s own stdout: the two
per-r reclassification blocks, `predictions_text`, `result_text`, and the
final "Written: .../results.json" line. There is no trust-suite
invocation, no per-stage listing, and no timing evidence anywhere in the
document `NOTES.md` itself cites as the "Full console record" backing
that exact claim.

This is not merely "the number seems plausible" — I checked whether this
program has a weaker but still-real precedent of at least summarizing the
trust-suite run inline even without full raw output, and it does:
exp-107's own `run_output.txt` contains the one-line summary "Trust
suite: green (41/41) at this shift's start; zero `lab/` diff throughout,"
and exp-108's own `run_output.txt` contains a full `"=== Full trust suite
(--only 12346789) ===" / "41/41 checks passed in 83 s"` section. exp-109
has **neither** — not even a one-line summary — a genuine regression from
both immediate predecessors in this exact document family, on the exact
claim ("trust suite green... 100s/102s") that is most directly checkable
and least excusably left unevidenced.

I cannot determine from the committed record whether the trust suite was
actually run and its output simply never appended to `run_output.txt`
(a disclosure/capture gap), or whether the specific "100s/102s" figure
was carried over/estimated without a fresh invocation this cycle (a
verify-before-claim violation). Either way, as committed, **this specific
sentence in `NOTES.md`'s Result section is not backed by any artifact a
reader can independently check** — the exact shape the lab's own
verify-before-claim discipline (CLAUDE.md) and this program's R4/R19
lineage exist to catch, here on the trust-suite gate itself rather than a
physics figure.

I did not re-run the trust suite myself as part of this review (out of
scope for a Phase-5 desk review of the committed record, and would not
retroactively validate what happened during the original Phase-4 shift
regardless of its outcome now) — flagging this as a gap in the record,
not asserting the claim is false.

---

## 3. Realizability-adjacent framing: is item i's fabrication-tolerance angle correctly deferred?

**Yes, correctly deferred, not silently assumed.** `NOTES.md`'s own scope
statement ("this cycle does not re-score items i/iii/iv/closure") is
honored in the diff: independently confirmed `item_i.verdict` in the
executed `result_text` reproduces exp-108's own committed
`CONFIRM`/`CONFIRM` values unchanged (checked against
`experiments/108-.../results.json` directly, not `NOTES.md`'s
restatement), and the fabrication-tolerance framing for item i's CONFIRM
appears only in the "Next — candidate Iteration 87 directions" section's
Tier 2, named as future work ("MATERIALS' own recommended
fabrication-tolerance framing for item i's CONFIRM, with Red Team's own
observer-angle caveat folded in") — not executed, not scored, and not
conflated with this cycle's own item-ii-only substantive change anywhere
in the diff or the T1/constraint bookkeeping. My own seat's realizability
discipline is correctly named as future work, not smuggled into this
cycle's CONFIRM verdict.

---

## 4. Constraint/T1 scope check

Independently re-confirmed (as Red Team's Attack 7 already did): every
touched or added code path (`classify_item_ii()`'s new body,
`analyze.py`'s companion edit, the `--predictions-only` assert,
`reclassify_108.py`) is a classification-statistic gate or text/
persistence pipeline over already-committed scalars. None reads or writes
σ(I), σ(x,t), ε(ω), or a perceptual quantity. T1 = N/A is correct.

---

## 5. Verdict

**CONFIRM-WITH-GAPS.**

The core substantive result — `classify_item_ii()` gated on
`fit["smooth"]`, both r taking the raw-fallback branch, both landing
CONFIRM — is genuine and reproduces exactly from primitives; I found no
arithmetic, provenance, or logic error anywhere in that chain, and 4 of
the 6 mandatory fixes (2/3/5/6) are cleanly, verifiably executed exactly
as claimed, independently checked against source and against
`results.json` rather than trusted from `NOTES.md`'s own narration.

Two gaps, both newly found this review (neither appears in any Phase-2
critique or Red Team's own audit, since both are execution-stage,
post-Phase-2 defects a proposal-stage review structurally cannot see):

1. **Fix 1's promised corrected section ("§ 'Why raw std, not forced
   AMBIGUOUS'") does not exist anywhere in the frozen `NOTES.md`** — the
   flawed item-i analogy is silently dropped rather than corrected and
   displayed, so the document's own "all six fixes incorporated" claim is
   true only for 5 of 6 in the specific, checkable form each fix's own
   disposition promised. Non-outcome-reversing; a documentation
   completeness gap, structurally adjacent to (not a fresh instance of)
   R24.
2. **The Result section's specific trust-suite claim ("41/41... 100s/
   102s") is not backed by anything in `run_output.txt`, the file
   `NOTES.md` itself cites as the full console record** — a regression
   from both exp-107's and exp-108's own weaker-but-real precedent of at
   least summarizing that check inline. Cannot confirm or refute whether
   the suite was actually run this cycle from the committed evidence
   alone.

Neither gap reverses the CONFIRM/CONFIRM headline outcome or implicates
T1/constraint scoring. Both are the kind of small, checkable
completeness defect this program's own discipline treats as worth
recording precisely rather than rounding off — consistent with this
program's history of Phase-5 self-reviews (including PHOTONICS' own
exp-108 self-review) finding the deepest residual defects precisely
because a fresh read of the *executed* artifact catches what a Phase-2
read of the *proposed* text cannot.

**Single most important finding:** `NOTES.md`'s own fix-1 disposition
promises a named corrected section ("§ 'Why raw std, not forced
AMBIGUOUS'") that does not exist anywhere in the frozen document — the
misdescribed sibling-code analogy from my own Phase-1 proposal was
silently dropped rather than corrected and shown, so one of the six
mandatory fixes this cycle's own Combined Verdict claims was
"incorporated before this run" is not actually retrievable from the
committed record in the specific form promised.
