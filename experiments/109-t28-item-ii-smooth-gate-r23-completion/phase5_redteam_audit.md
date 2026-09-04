# PHASE 5 — RED TEAM FINAL AUDIT · Panel Iteration 86 (exp-109)
## "The R24 Second-Instance Fix Genuinely Lands; a Broken Internal Cross-Reference, an Unevidenced Trust-Suite Citation, and the House Discipline on Commit Ordering — Resolved From Git, Not From Restatement"

Red Team seat, fresh context, going last. Received: PANEL.md, LOGBOOK.md in
full (RULED OUT registry R1–R25 read in full; R4/R16/R18/R19/R21/R23/R24/R25
lineage read at full text, not summary), PLAN.md lines 25–260, the complete
exp-109 record in order (`phase1_proposal.md`, all five
`phase2_critique_*.md`, `phase2_redteam_audit.md`, `NOTES.md` end to end,
`results.json`, `run_output.txt`), all six blind Phase-5 reviews
(`phase5_review_{photonics,materials,em,thermodynamics,quantum,vision}.md`),
the actual code (`experiments/108-.../run.py`, `.../analyze.py`,
`experiments/109-.../reclassify_108.py`), and `git log`/`git show`/`git
blame` on the exp-109 directory plus the two patched exp-108 files. Every
load-bearing claim below was independently re-derived from primitives —
none accepted from any seat's restatement, including this document's own
quotations, and including the six Phase-5 reviews' own restatements of each
other's absent work (each was blind to the other five).

---

## 0. Independent re-verification from primitives

**0.1 The core numeric chain — re-derived directly from
`experiments/108-.../results.json`'s own committed `tier1.r{r}.item_ii`
block, not from any document's table.**

| r | `delta_values` source | `raw_std` (`np.std`, ddof=0) | `residual_std` (fit) | `r_squared` | `smooth` | `raw_over_residual_ratio` | CONFIRM bar (`0.5·boxA`) | verdict |
|---|---|---|---|---|---|---|---|---|
| 156 | `results.json` | **5.008327900579266e-06** | 2.89716280726349e-06 | 0.6653735294260243 | `False` | 1.72870088212608 | 1.4845e-05 | CONFIRM (2.964× inside) |
| 312 | `results.json` | **2.1240857290489e-06** | 2.102199273342035e-06 | 0.020501712361515212 | `False` | 1.010411218377062 | 1.234e-05 | CONFIRM (5.809× inside) |

Reproduces `phase1_proposal.md`'s §4 table, all five Phase-2 critiques'
figures, `phase2_redteam_audit.md`'s §0.1 table, `NOTES.md`'s frozen
Predictions and Result tables, `experiments/109-.../results.json`'s own
`item_ii_reclassified` block, and all six Phase-5 reviews' own independent
re-derivations — six-of-six plus this audit, seven independent
computations, one number at each of two points. `classify_item_i()`'s
CONFIRM branch (`experiments/108-.../run.py:234–289`) re-traced directly:
`linear_fit_1_over_margin` is called exactly once, inside `for (i0,j0) in
runs:` (line 276), unreached when `runs` is empty; `verdict="CONFIRM"`
requires `confirm_all_margins and not runs` — CONFIRM is reachable only in
the one case where the fit/smoothness code path is never entered. This is
now the **eighth** independent re-trace of this exact control-flow fact
across this cycle's Phase 1 critique (PHOTONICS), Phase 2 (Red Team, §0.2),
and all six Phase-5 reviews bar VISION's (which confirmed it only via §1d's
supporting-checks list) — unanimous, zero dissent.

**0.2 The OLS-with-intercept inequality** (`residual_std ≤ raw_std` always,
for `A_mat=[1,1/margin]`): re-derived independently by normal equations —
the constant model `ŷ=mean(y)` (`B=0`) is a feasible point in the same
least-squares search space, forcing `RSS_fit ≤ RSS_constant`, hence (same
divisor `n`, `ddof=0` both sides) `residual_std ≤ raw_std` unconditionally.
Airtight; not merely true on these two points. Both r independently
reconfirmed: 2.897e-6 ≤ 5.008e-6 (r=156, ratio 1.729×), 2.102e-6 ≤ 2.124e-6
(r=312, ratio 1.010×, the near-degenerate case — appropriately the one
NOTES.md's own Tier 2 flags for the queued r=624 point to check against
both bars, not assume safe).

**0.3 The double-braced quotation slip — independently confirmed.**
`experiments/108-.../run.py:361–367` (the actual committed, executed
source):

```python
**Gate P0: {'PASS' if gate_p0_pass else 'FAIL'}.**
**Reproduction precondition: {'PASS' if repro_pass else 'FAIL'}.**
```

Single-braced — correct f-string interpolation, confirmed by the executed
`result_text` rendering `**Gate P0: PASS.**` literally, in both
`run_output.txt` and `results.json`. `NOTES.md`'s own Setup section (lines
223–224), presenting this as "the exact new body," shows **double**-braced
`{{'PASS' if gate_p0_pass else 'FAIL'}}` — a documentation-quoting slip,
independently confirmed exactly as EM found. Cosmetic: no double-brace text
reaches the executed pipeline anywhere.

**0.4 The trust-suite citation gap — independently confirmed by direct
read of the actual committed artifact.** `NOTES.md`'s Result section
(line 388–390): *"trust suite green before and after (41/41, `--only
12346789`, 100s/102s). Full console record: `run_output.txt`."* The
complete, committed `run_output.txt` (81 lines, verified via `git show
7783f95 --stat` as the genuine Phase-4 console capture) contains only
`reclassify_108.py`'s own stdout — the two per-r reclassification blocks,
`predictions_text`, `result_text`, and the final `Written: .../results.json`
line. Grepped directly for `41/41`, `--only`, `stage`, `checks passed`,
`trust suite`: **zero matches, all five patterns.** `results.json` (both
exp-108's and exp-109's own) contains no suite-run record either. This is
the **fourth** independent confirmation of this exact gap this cycle
(MATERIALS, EM, THERMODYNAMICS, and now this audit) — the most heavily
convergent finding among the six Phase-5 reviews. `git diff --stat -- lab/`
across the full exp-109 commit range: empty, confirmed — the "zero `lab/`
diff" half of the same sentence is fully evidenced; only the specific
"41/41, 100s/102s" figure is not.

**0.5 `n_fdtd_calls`/`total_wall_s`/`source_results_json_sha` provenance —
independently recomputed, not merely re-read.** Opened
`experiments/108-.../results.json`'s own `wall_times_s` dict directly and
summed all six `{r156,r312}×{empty,hollow,peccored}` entries by script:
**7712.0 exact, six entries counted** — matches `n_fdtd_calls=6` and
`total_wall_s=7712.0` as top-level keys, not merely restated from either.
`git hash-object experiments/108-.../results.json` on the currently
committed file: `9bcdbdf7ca3066035363b61d272e921e133fb755` — matches
`experiments/109-.../results.json`'s own `source_results_json_sha` exactly,
a genuine, re-derivable provenance pointer, not hand-typed.

**0.6 Constraint/T1 structural check.** Every function this cycle touches
or adds (`classify_item_ii()`'s new body, the `--predictions-only` block,
`analyze.py`'s companion edit, `reclassify_108.py`) is a
classification-statistic gate or a text/persistence pipeline over
already-committed scalars — independently confirmed via
`grep -rn "C_thr\|Weber\|ambient\|sigma\|epsilon"` across all three touched
files: zero perceptual- or absorption-parameter code paths. T1 = N/A is
correct, structurally, not merely asserted.

---

## 1. Disposition of the six blind Phase-5 reviews

**PHOTONICS (CONFIRM-WITH-GAPS) — ADOPT the headline finding in full;
OVERRIDE the secondary git-history claim as factually incorrect (§2,
below).** The missing "§ Why raw std, not forced AMBIGUOUS" section is
real, independently reconfirmed (§1 below). PHOTONICS' own re-trace of
`classify_item_i()`'s CONFIRM branch (§0 of its review) is independently
reconfirmed exact (§0.1, above) — this is the strongest-verified single
fact in this cycle's record, checked eight separate times by eight
independent parties and never once contradicted. **Override**: PHOTONICS'
claim that "`NOTES.md` was committed for the first and only time in commit
`7783f95` — the same commit as `results.json`/`run_output.txt`... not in an
earlier, separate commit establishing the Predictions section before the
run" does not survive `git blame`/`git log` re-verification — see §2. This
is the one load-bearing factual error found anywhere in this cycle's seven
layers of review (six Phase-5 seats plus this audit), and it happens to sit
inside the one document whose entire second finding is about verifying
things from primitives rather than restatement — noted plainly, not to
diminish PHOTONICS' otherwise-exemplary review (its §0's from-scratch
re-derivations are the most thorough of the six), but because an incorrect
"the house discipline was violated" claim, left uncorrected, would be a
worse legacy defect than the one it describes.

**MATERIALS (self-review, CONFIRM-WITH-GAPS) — ADOPT both findings in
full.** The missing-section defect, found independently (not by reading
PHOTONICS — MATERIALS' own review states it audited its own Phase-1
proposal's six flagged defects one by one, landing on the identical gap by
a different route: auditing its own promise rather than grepping headings
first). The `run_output.txt` trust-suite-evidence gap, confirmed
independently at §0.4. No override.

**ELECTROMAGNETISM (CONFIRM-WITH-GAPS) — ADOPT in full.** Fix 2 verified
wired end-to-end into the machine-generated `stat_source` string in
committed `results.json`, not just NOTES.md prose — independently
reconfirmed by direct read of `experiments/108-.../run.py:212–222` and the
literal committed JSON string (§0.1). The double-braced documentation slip
(§0.3) and the trust-suite citation gap (§0.4, EM's own fresh re-run: 41/41
in 106s, corroborating the underlying claim as true without making the
*citation* evidenced) both independently reconfirmed exact. No override.

**THERMODYNAMICS (CONFIRM-WITH-GAPS) — ADOPT in full.** Fixes 4/5 verified
wired into executed code (`reclassify_108.py`'s literal `and`, confirmed at
lines 84–87) and persisted `result_text` (the wall-time attribution
sentence, confirmed present verbatim). `n_fdtd_calls`/`total_wall_s`/
`source_results_json_sha` all independently re-verified exact at §0.5 —
the strongest provenance check of the six, since it recomputed
`total_wall_s` from the underlying six-entry `wall_times_s` dict rather
than trusting the top-level key. Third independent confirmation of the
trust-suite-citation gap. No override.

**QUANTUM OPTICS (CONFIRM-WITH-GAPS) — ADOPT in full, including the
R25-spirit concern.** The ratio verified exact, three independent methods
(live re-execution, from-scratch re-implementation, direct source read) —
the most thoroughly cross-checked single figure in this cycle's record.
Independently re-read `NOTES.md`'s own Tier 2 text (lines 547–557,
directly, not via QUANTUM's quotation of it): confirmed exactly as
QUANTUM states — three semicolon-delimited items exist (the r=624 point,
the fabrication-tolerance framing, "formalize the absolute-floor six-margin
family from a resolution/aliasing bound"), and the `R2_SMOOTH_THRESHOLD`
re-derivation is grafted onto the third via a comma ("now including..."),
never given its own slot. QUANTUM's own ruling — this is R25-*shaped* but
not a literal R25 firing (R25's own text is scoped to "a code-level fix,"
this is a calibration/statistics task; and this is the founding instance of
this specific concern, not a second silent drop of an already-once-dropped
item) — is independently re-derived and correct on both counts (§3, below).
No override.

**VISION SCIENCE (clean CONFIRM) — ADOPT in full.** Byte-for-byte diff of
`results.json`'s two text fields against NOTES.md's own quoted blocks —
independently spot-checked at §0.4/§0.6 above via direct substring/length
comparison, matches VISION's own claimed lengths (2387/2386,
1916/1915 chars, one trailing newline each) exactly. DISCLAIMER text
confirmed present verbatim, twice, in the Result section — genuinely closes
VISION's own three-cycle-old finding for the first time, independently
reconfirmed. The process-hygiene note on Combined-Verdict vocabulary is
addressed directly at §4, below. No override on the substantive finding.

---

## 2. The commit-ordering question, resolved definitively from git history

**Ruling: house discipline was honored. PANEL.md's "predictions committed
to git BEFORE the run" was NOT violated. PHOTONICS' claim to the contrary
is incorrect and is overridden.**

`git log --oneline -- experiments/109-t28-item-ii-smooth-gate-r23-completion/`
shows 13 commits. `git log --oneline -- .../NOTES.md` (the file, not the
directory) shows exactly **two**:

```
1e20af5  2026-09-04 09:23:50 +0000  Panel Iteration 86 Phase 2: ELECTROMAGNETISM blind critique landing
7783f95  2026-09-04 09:28:23 +0000  Panel Iteration 86 Phase 4: results
```

`git show 1e20af5 --stat -- .../NOTES.md`: **390 insertions, new file** —
this commit is where `NOTES.md` first enters git, bundled (by the shift's
own commit-batching choice, not sequentially per the label) alongside
`phase2_critique_em.md` and `phase2_redteam_audit.md`. `git blame -L
1,120` and `-L 385,420` on the current file both attribute the Hypothesis/
Setup/Predictions/Idealizations/T1 content, and the placeholder
`## Result` line, to commit `1e20af5` — i.e. **everything through the
frozen Predictions section, including the exact `classify_item_ii()` code
body and the item-4 CONFIRM/CONFIRM prediction table, was committed at
09:23:50.** `git show 7783f95 --stat`: `NOTES.md | 182 ++++...-` (178
insertions, 4 deletions) — `git diff 1e20af5 7783f95 -- .../NOTES.md`
shows the **entire** diff is the four-line `## Result` placeholder
(*"Phase 4 not yet run..."*) replaced by the 178-line executed Result
section; nothing before that placeholder changed by one byte between the
two commits. Phase 4's own commit (`7783f95`, 09:28:23, five minutes
later) is where `run.py`/`analyze.py` were actually patched, the run was
actually executed, and `results.json`/`run_output.txt` were written.

So: the falsifiable Predictions (item 4's CONFIRM/CONFIRM table to <1e-9
relative, the `raw_over_residual_ratio` figures to <1e-3 relative, the
`stat_source` substring conditions, all four mechanical checks) were
locked in git a full five minutes before the code that would be scored
against them was patched, run, or committed. **PHOTONICS' claim that
NOTES.md was committed "for the first and only time" in the same commit as
the results is a straightforward git-log error** — it appears to have
checked `git log` against the directory or against `results.json`/
`run_output.txt` specifically (both of which genuinely are `7783f95`-only,
correctly) and mis-attributed that same single-commit fact to `NOTES.md`
itself without separately verifying `NOTES.md`'s own file-scoped log. This
audit's own independent `git blame`, run fresh against the current
committed history rather than trusted from any seat's restatement (the
charter's own standing instruction), resolves the question the other way:
**two separate commits, predictions-then-results, in the correct order,
five minutes apart, with a byte-exact diff boundary at the `## Result`
header confirming nothing upstream of it was touched.**

One secondary, genuinely open observation (not house-discipline-violating,
but worth naming): the commit that froze `NOTES.md`'s Predictions section
is *labeled* "Phase 2: ELECTROMAGNETISM blind critique landing" even though
its own diff is Phase-3 synthesis content (all five Phase-2 critiques and
Red Team's own Phase-2 audit are attested by `NOTES.md`'s own "Phase 1 →
Phase 2 → Phase 3" narrative as complete inputs to that synthesis) — a
commit-message/content mismatch, not a sequencing defect (the other four
Phase-2 critique commits that follow it chronologically were plainly
already-written blind artifacts being landed in a batch-commit order that
does not mirror generation order). Purely a labeling inconsistency in the
git history's own narration of itself; does not affect any evidentiary
claim in this section.

---

## 3. R-rule ruling

**None of this cycle's gaps constitutes a firing of any existing R-rule.**
Checked individually against each candidate rule's own operative text:

**3.1 Fix 1's missing "§ Why raw std, not forced AMBIGUOUS" section — does
NOT fire R24.** R24's own text requires a Phase-2 mandatory fix's
"specified consequence" to be "implemented as a binding element of
whatever classification or verdict string it was written to gate."
Fix 1's actual consequence — ground the (b)-rejection on the OLS proof
plus the original mandatory fix's own text, not the flawed item-i analogy
— **is** correctly implemented in the one place that is load-bearing to a
classification string: `classify_item_ii()`'s own docstring (`run.py:
187–204`, independently confirmed at §0.1) states exactly this, correctly,
with no trace of the flawed analogy repeated anywhere in the executed
code. What is missing is a *second*, purely explanatory, prose section in
`NOTES.md` that `NOTES.md`'s own Phase-3 synthesis promised by name and
never wrote — a documentation self-reference that resolves to nothing, not
a classification consequence that was computed and left unscored. This is
a different failure geometry than R24's own, one level removed (three of
six Phase-5 seats — PHOTONICS, MATERIALS, QUANTUM — independently used
almost this exact phrase to describe it). **Does NOT fire R4** either: R4
concerns a hand-typed or restated *figure* that fails to reproduce
arithmetically from its own cited source; here no figure is wrong anywhere
— the gap is a dangling internal cross-reference (a promised heading that
was never written), not a miscomputed or mis-cited number.

**This is a genuinely new failure shape, independently and blindly
converged on by three of six Phase-5 seats (a stronger same-cycle
consensus than most of this registry's own founding instances) — Red Team
proposes a new standing rule.**

> **R26 (proposed, this audit) — a Phase-3 synthesis's own named forward
> cross-reference to a promised corrective section (e.g. "Corrected below,
> § 'X'") must resolve to real, substantive content at that location before
> the document is frozen; a promise that a fix's own reasoning "is
> corrected below" is not itself a discharge of the fix — the correction
> must actually appear there, checkable by heading-grep, not merely be
> true elsewhere in the document (a docstring, a different section) with
> the named pointer left dangling.** Distinguished from R4 (an external
> figure/citation that fails to reproduce) and from R18 (a check's
> documented scope vs. its actual code): this concerns a document's own
> internal self-reference to itself, a category no prior rule in this
> registry names, and one uniquely invisible to a reader who does not
> grep for the exact promised heading — unlike an external citation, which
> at least names a checkable target outside the document making the claim.
> **Does not fire on its own founding instance** (exp-109), matching every
> prior rule's own precedent — the underlying correction the missing
> section was meant to hold is, in this instance, genuinely present
> elsewhere (the `classify_item_ii()` docstring) and non-outcome-reversing
> (Red Team's own Phase-2 audit independently supplied a sufficient,
> stronger alternate ground for the same design choice before this gap
> could matter). **Rule, forward: a second instance of a named,
> unresolved forward cross-reference inside a frozen Phase-3/Phase-4
> document, on any channel, fires Checkpoint criterion 4 automatically** —
> a single-instance-ratified, forward-firing model, matching R16/R21/R22/
> R23/R24/R25's own precedent rather than R20's three-in-one-cycle density
> model, because this concerns one specific, cheaply-checkable defect
> shape (grep the promised heading), not a density measure across
> unrelated citations.

**3.2 The trust-suite citation gap — does NOT fire R4/R20, correctly
recognized by three of six Phase-5 seats as R4-lineage but not a fresh
firing.** This is squarely within R4's existing, already-generalized scope
("any falsifier or self-consistency figure cited... MUST be produced by
invoking the actual committed function... never hand-typed," already
extended once to "an aggregate flag... is not sufficient" and once to "a
Phase-5 reviewer's own re-checking") — a citation (`run_output.txt` as the
"Full console record") that does not, on inspection, contain the figure it
is cited to back. **R20's own three-or-more-in-one-document density
threshold does not clear**: checked strictly against R20's own trigger
("surviving... into its Result/Learned sections"), only two candidate
R4-class defects sit inside `NOTES.md`'s own Result/Combined-Verdict
prose — (a) the trust-suite citation itself, and (b) the Combined Verdict's
own "all six... mandatory fixes were incorporated before this run"
sentence, which is not quite true for fix 1 in the specific form promised
(§3.1). The double-braced quotation slip (§0.3) sits in the Setup section,
not Result/Learned, and so does not count toward this tally. **Tally: 2,
short of "three or more" — R20 does not fire**, an identical outcome to
exp-108's own R20 tally of 2 one cycle upstream (LOGBOOK.md Iteration 85
CHECKPOINT block) — not a coincidence worth over-reading, but worth naming:
this is the second consecutive governance cycle in this lineage to land
exactly one short of R20's own density bar.

**3.3 QUANTUM's R25-spirit concern (the `R2_SMOOTH_THRESHOLD` re-derivation
folded into a subordinate clause of a different Tier-2 item) — does NOT
fire R25, correctly ruled by QUANTUM and independently reconfirmed here.**
R25's own text is scoped explicitly to "a code-level fix an audit
determines is necessary" that an audit itself defers by a stated scope
limit. Here: (a) it is a calibration/statistics re-derivation, not a code
fix; (b) Red Team's own Phase-2 audit this cycle never determined it
"necessary" — it was explicitly, reasonedly declined as non-mandatory,
out-of-scope overreach (`phase2_redteam_audit.md` §2, QUANTUM disposition);
(c) this is the founding instance of this specific sub-concern (whether a
*named-but-declined* item's own forward-queue placement can itself violate
R25's line-item discipline), not a second silent drop of an
already-flagged, already-once-dropped item, which is what R25's own
two-strike model requires to escalate. All three grounds independently
verified at §1, above. Not a firing — but a real, disclosed process gap
worth a same-shift fix (§5).

**3.4 Fix 4's docstring shortfall (code has the `and`, but no inline
comment naming the reduction rule at that call site) — does not rise to
R-rule territory.** Two of six Phase-5 seats (MATERIALS, QUANTUM)
independently found this; both correctly rate it low-severity,
non-blocking, since the reduction rule itself is correct and
self-evident in the code (`and` is unambiguous). No further ruling needed.

**Net: zero R-rule firings this cycle, one existing-lineage gap correctly
recognized as non-firing by three-way blind convergence (§3.2), one
existing-lineage gap correctly recognized as non-firing by QUANTUM's own
careful textual reading (§3.3), and one genuinely new failure shape named
here as a proposed standing rule (R26, §3.1), founding instance, does not
fire.** This is, if anything, a cleaner governance outcome than either of
the two immediately preceding cycles in this lineage: exp-107 discharged
R25's founding instance while quietly incubating the failure that would
become exp-108's own R24-second-instance Checkpoint-4 firing; exp-108 fired
Checkpoint criterion 4 for real. exp-109 — the cycle built specifically to
close that firing's root cause — finds real, disclosed, non-outcome-
reversing gaps of its own (as every cycle in this lineage has), but none
of them meets any existing rule's firing bar, and the one genuinely novel
shape found is caught blind, same-cycle, before this document, exactly
this program's own unbroken discharge-test pattern.

---

## 4. Combined Verdict — vocabulary ruling, addressing VISION's hygiene note

**NOTES.md's own "Combined Verdict" line should read CONFIRM-WITH-GAPS,
not CONFIRM** — matching five of the six Phase-5 reviews' own verdicts on
this exact document, and correcting the one place NOTES.md's own prose
(the Combined Verdict's "all six... mandatory fixes were incorporated
before this run") is not quite accurate (§3.1/§3.2). This is a same-shift
annotation (§5, below), not a reopening: nothing about the underlying
CONFIRM/CONFIRM physical-reclassification result changes.

**On PANEL.md's own promising/partial/ruled-out vocabulary versus a
CONFIRM-shaped one — ruled explicitly, per the charter's own instruction to
address this directly.** PANEL.md's Phase 5 text is precise about *where*
that vocabulary is required: *"Director updates LOGBOOK.md (verdict:
promising / partial / ruled out...)"* — a requirement stated for the
LOGBOOK.md iteration entry specifically, not for a cycle's own internal
NOTES.md "Combined Verdict" line, which is a convention this document
family has followed by consistent practice, not by PANEL.md's own textual
mandate. exp-109 is a materially different kind of cycle from exp-107/108,
its own two immediate predecessors in this governance lineage: both of
those still executed real FDTD captures and scored physically-meaningful
CONFIRM/PASS verdicts against constraint-adjacent classifiers (item i/ii/
iii/iv), even while governance-labeled; exp-109 makes **zero** `Sim.run()`
calls and touches **zero** constraint-relevant code anywhere (§0.6) — its
entire subject matter is a deterministic reclassification of already-
committed scalars against pre-registered exact-match bands, i.e. CONFIRM/
AMBIGUOUS/REFUTE is not merely available vocabulary here, it is the
literal, correct name of the thing being checked, since that is the
vocabulary `classify_item_ii()` itself, this cycle's own subject, already
uses. **Ruling: a CONFIRM-shaped Combined Verdict at the NOTES.md level is
legitimate, and arguably the more precise self-description, for a cycle
whose entire content is a reproducibility gate rather than a step of
mechanism-search progress — but the LOGBOOK.md Iteration 86 entry itself
must still use PANEL.md's own promising/partial/ruled-out vocabulary**,
since that is what PANEL.md's text explicitly, unambiguously specifies for
that artifact, independent of what any individual NOTES.md chooses. Given
the disclosed gaps (§3, §5) are real, non-outcome-reversing, and caught
blind before this audit — matching this program's own established meaning
of the term across exp-107 and the corrected exp-108 — **the LOGBOOK.md
Iteration 86 entry should read PARTIAL**: not RULED OUT (nothing here was
refuted; T1 correctly N/A throughout), not PROMISING (real, disclosed
completeness gaps remain as of this audit, even though none is
outcome-reversing or R-rule-firing).

---

## 5. Same-shift annotations — apply directly to `NOTES.md` (blockquoted,
attributed, zero re-run, zero verdict-arithmetic change), matching this
program's own "annotated, not overwritten" discipline

1. **Write in the missing section.** Insert a real `### Why raw std, not
   forced AMBIGUOUS` section (or retarget the dangling pointer at line 62
   to point at it) containing the actual corrected reasoning — already
   fully worked out and independently reconfirmed seven times over in this
   cycle's own record: `classify_item_i()`'s CONFIRM branch is
   structurally incapable of reaching `linear_fit_1_over_margin`/the
   smoothness test (it is gated behind `not runs`, and the fit is called
   only inside the loop over `runs`), not a deliberate design choice to
   exempt null findings from a smoothness judgment; alternative (a) is
   chosen instead on (i) the OLS-with-intercept inequality (§0.2, airtight)
   and (ii) the original Iteration-85 mandatory fix's own text
   (`experiments/108-.../phase2_redteam_audit.md:340–347`), which already
   specifies raw `std` as the fix's own pre-registered non-smooth default.
   This is a pure transcription of already-verified content — zero new
   analysis, safe to insert same-shift.
2. **Correct the double-braced quotation** (NOTES.md lines 223–224) to
   match the actual single-braced, correctly-interpolating source at
   `experiments/108-.../run.py:361–367` (§0.3).
3. **Annotate the trust-suite citation.** After the Result section's
   "trust suite green before and after (41/41, `--only 12346789`,
   100s/102s)" sentence, add a blockquoted note: `run_output.txt`, the
   artifact this sentence cites as the "Full console record," contains no
   trust-suite invocation, stage listing, or timing evidence (§0.4) —
   independently corroborated as true by EM's own fresh re-run (41/41 in
   106s) but not evidenced by the cited record itself.
4. **Correct the Combined Verdict**: `CONFIRM` → `CONFIRM-WITH-GAPS`
   (§4); correct "All six Red Team mandatory fixes were incorporated
   before this run (not after)" to disclose that five of six landed in
   the specific, checkable form promised, and the sixth (fix 1) landed in
   substance (correctly, in `classify_item_ii()`'s own docstring) but not
   in the named location — corrected same-shift, per annotation 1.
5. **Optional, low-severity**: add a one-line comment at
   `reclassify_108.py:84–87` naming the AND-reduction explicitly (fix 4's
   own literal "code AND docstring" text, not fully met — §3.4).
6. **Recommended, not this cycle's own blocker**: the next cycle to touch
   Tier 2 should split "formalize the absolute-floor six-margin family
   from a resolution/aliasing bound" and "re-derive
   `R2_SMOOTH_THRESHOLD=0.90` for item ii's own question" into two
   separate, independently-checkable queue lines (§3.3, QUANTUM's own
   recommendation, adopted) — before either is worked, so neither can be
   silently satisfied by completing only the other.

None of the above touches `experiments/108-.../results.json`, `NOTES.md`,
or `phase5_redteam_audit.md` (exp-108's own historical record, correctly
left as-is per this cycle's own Idealizations) or reopens R25 or the R23
ratify-as-scoped ruling. **Zero re-run, zero verdict-arithmetic change**:
CONFIRM/CONFIRM at both r stands, exactly as predicted and as every one of
seven independent parties (six Phase-5 seats plus this audit) has now
confirmed from primitives.

---

## 6. Reconciled Iteration-87 queue (carries exp-108's own still-open Tier
1/2/3 forward unchanged, per NOTES.md's own accounting; amends Tier 2 per
§3.3/§5 item 6)

**Tier 0** — rule on the Iteration-85 Checkpoint-4 firing (still pending
Marsh; unchanged by this cycle, which fixed the code defect that CAUSED
the firing but does not itself rule on the firing's own governance
consequence, §3 of `phase2_redteam_audit.md`, independently reconfirmed
correct here).

**Tier 1** (from exp-108's own still-open queue, untouched this cycle) —
re-normalize (or floor-gate) item i's per-bin comparison against each
bin's own LOCAL magnitude, not the global peak (zero new FDTD, the single
highest-value item on this queue); a synthetic positive/negative control
for `linear_fit_1_over_margin`'s own smooth/noise discriminator — now
doubly motivated, discharging both `classify_item_ii()`'s new branch's own
disclosed R18 gap and `analyze.py`'s companion call site's identical gap
in one control; extend `stage26`'s negative control to the symmetric
truncation direction.

**Tier 2** — split into two independently-checkable lines, per §3.3/§5
item 6 (was one folded item this cycle): (a) formalize the absolute-floor
six-margin family from a resolution/aliasing bound; (b) re-derive
`R2_SMOOTH_THRESHOLD=0.90` for item ii's own question specifically
(QUANTUM's named-but-not-mandatory concern, now its own line, not a
subordinate clause of (a)). Plus, unchanged: a fourth r-point (r=624),
checked against BOTH the CONFIRM and REFUTE bars per this cycle's own
Attack 2/fix 2 finding (the raw-std fallback is liberal toward false
REFUTE, not merely conservative toward false CONFIRM); MATERIALS' own
fabrication-tolerance framing for item i's CONFIRM, with Red Team's own
observer-angle caveat folded in.

**Tier 3** — unchanged: the oblique-angle extension; the 750/450nm leg;
the `G40` full-width leg; the x-wall admittance refit; `PAD`-with-article
survival; `box_dev`'s own thinning margin (~9.0× at r=312, still
unresolved).

Full record: `experiments/109-t28-item-ii-smooth-gate-r23-completion/` —
Phase-1 proposal (MATERIALS), five Phase-2 blind critiques, Phase-2 Red
Team audit, Phase-3 synthesis (`NOTES.md`), Phase-4 results
(`results.json`, `run_output.txt`, the patched `experiments/108-.../
run.py`/`.../analyze.py`, the new `reclassify_108.py`), six Phase-5 blind
reviews, this Phase-5 Red Team final audit. LOGBOOK.md Iteration 86.

---

## Summary

**Overall verdict: PARTIAL** (LOGBOOK.md-level vocabulary, per §4's
ruling) — not RULED OUT (nothing refuted; T1 correctly N/A throughout,
independently reconfirmed at §0.6), not PROMISING (real, disclosed,
non-outcome-reversing completeness gaps remain as of this audit: the
missing "§ Why raw std" section, the unevidenced trust-suite citation, the
double-braced documentation slip, the R25-shaped Tier-2 folding). NOTES.md's
own internal Combined Verdict is separately corrected to CONFIRM-WITH-GAPS
(§4/§5), a legitimate, more precise vocabulary for this specific
reproducibility-gate cycle-type, distinct from the LOGBOOK-facing term.

**Zero R-rule firings.** One new standing rule proposed (R26 — a Phase-3
document's own named forward cross-reference to a promised corrective
section must resolve to real content there before freeze), founding
instance, does not fire. Two existing-lineage gaps (the trust-suite
citation, R4-class; QUANTUM's R25-shaped Tier-2 concern) independently
confirmed non-firing on their own governing texts.

**The substantive result stands, unreversed, seven-ways independently
verified**: `classify_item_ii()` is now genuinely gated on `fit["smooth"]`,
wired into the executed classification path (not merely re-narrated a
third time) — the R24 second instance is discharged for real. R23's
code/persistence half and its human-readable-citation half are both
genuinely closed, the latter for the first time in at least four cycles
of this specific document family's own history.

**Required same-shift annotations, one sentence**: write in the promised
"§ Why raw std, not forced AMBIGUOUS" section (currently a dangling
pointer), correct NOTES.md's double-braced code quotation and its
"all six fixes incorporated" overclaim, disclose that `run_output.txt`
does not evidence the cited trust-suite figures, and correct the Combined
Verdict line to CONFIRM-WITH-GAPS — all zero-re-run, zero-verdict-
arithmetic, blockquoted insertions into the existing frozen document.
