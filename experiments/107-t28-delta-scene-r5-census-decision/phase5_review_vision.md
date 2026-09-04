# PHASE 5 — SELF-REVIEW · VISION SCIENCE · Panel Iteration 84 (exp-107)

*Fresh context. This cycle's rotation lead. Charter: human perceptual
limits — contrast thresholds, luminance edge detection, spectral
sensitivity, adaptation, temporal sensitivity, saccadic/attentional
blindness. Central question: what would make a human eye FAIL to
register something physically present? Duty: pin numeric thresholds,
with sources, BEFORE any run that scores against them. This is a
self-review of my own Phase-1 proposal and how the cycle actually
turned out — honest, not defensive.*

---

## 1. Owning my Phase-1 proposal's defects

My `phase1_proposal.md` shipped two independently-caught defects, both
confirmed exact by Red Team's Phase-2 audit before any FDTD call ran.
I take them in turn, against my own charter's duty clause.

**1a. The `θ_anchor` selection rule was structurally unsatisfiable.**
QUANTUM found, and Red Team's audit independently re-derived digit-for-
digit (`phase2_redteam_audit.md` §0.1), that my own `≥1.4°`-from-every-
crossing buffer, applied to the four native-grid zero-crossings
(37.127°/38.590°/40.265°/41.461°), produces four exclusion intervals
that pairwise overlap and merge into one continuous forbidden band
`[35.727°, 42.861°]` — a band that fully swallows my own proposed
`[36.0°, 42.0°]` grid. Zero of 31 points could ever serve as the anchor.
Gate G0, the gate I built and called "MANDATORY... must PASS before ANY
correlation reading counts as evidence," had an empty domain before a
single `Sim.run()` call. Worse, Red Team generalized this (§0.2) into a
structural indictment of the rule itself, not a window-placement
accident: a buffer sized to *half a period*, applied to a lattice of
crossings recurring *at that period*, tiles the entire angular axis with
exclusion zones, leaving safe slivers (`0.04°–0.15°` wide) narrower than
my own grid's `0.2°` step — no re-centering or widening at this grid
density rescues it. **Should I have caught this myself?** Yes, without
qualification. My own §7 explicitly told Red Team to "check this against
the actual pooled data BEFORE freezing, not discover it at Phase 4" — I
named the exact test and then didn't run it on my own design before
publishing it. This is not a subtle numerical-analysis result; it is
four subtractions and a comparison against numbers I myself cited two
sections earlier in the same document. This is a plain execution
failure, not a hard-to-anticipate one.

**1b. The `C_thr_lab` citation was the wrong statistic — an R9-shaped
defect, on my own signature threshold, inside my own charter's central
risk-framing sentence.** My §1 stated `delta_scene`'s magnitude is
"≈0.08–0.12× C_thr=0.005" — PHOTONICS found, and Red Team independently
reproduced exactly (§0.4: `peak/C_thr_lab = 0.6299`, i.e. **63.0%** of
the bar, a `5.25×–7.87×` discrepancy from my own figure), that this cited
T16/R9's `amp_ratio`-normalized fitted-sinusoid figure for a *different*
measurement construction (`PAIR_PAD`/`PAIR_ABSORB40`, exp-076/077) — not
`delta_scene`'s own raw peak, whose directly on-point figure was already
sitting in my own cited source pool (exp-100's own Tier-2 Leg A). Two
answers to the task's direct question:

- **Was this specifically a failure of my own duty clause?** Yes,
  unambiguously. My duty is "pin numeric thresholds, with sources, BEFORE
  any run." I did cite a source (LOGBOOK T16) — but citing a source is
  not the same discipline as verifying the cited figure is
  *commensurable* with the quantity I placed next to it. R9 exists
  precisely because "reproducing the division is necessary, not
  sufficient" — I reproduced nobody's division wrong; I picked the wrong
  numerator's proxy entirely, then treated it as interchangeable with a
  differently-normalized quantity of nominally the same signal. That is
  R9's exact failure shape, applied to a perceptual-threshold comparison,
  which is squarely inside my charter, not adjacent to it.
- **The sharper, more uncomfortable fact**: R9 itself exists because of
  a chain my own seat is part of. LOGBOOK's own T16 entry records that
  VISION's Iteration-53 Phase-5 review (exp-076) *already* raised "a
  draft warning" about exactly this `amp_ratio`-vs-raw-magnitude
  conflation risk — a warning "immediately contradicted in the same
  document's own headline." I am not claiming that Iteration-53 review
  and this Phase-1 proposal are the same failure event, and I have not
  re-read that document's authorship to claim more identity between them
  than the record supports — but the pattern is damning regardless of
  which individual body wore this seat's hat each time: this exact
  conflation risk has now brushed against VISION's own charter at least
  three times (the exp-076 draft warning, R9's founding correction at
  exp-077, and now this proposal), and on the third occasion the seat
  whose entire job is pinning perceptual thresholds correctly produced a
  fresh instance of it rather than catching one.

## 2. R23 disclaimer discipline — a gap I found, not one that was flagged to me

I checked, per my task's instruction, whether the standing `DISCLAIMER`
text (the perceptual/expressibility disclaimer, R23 code-enforced since
exp-104) is still correctly present in this cycle's own module. **It is
not present at all, anywhere in code, this cycle.** I grepped
`run.py`, `chunk_runner.py`, and `finalize.py` for `DISCLAIMER` and
`disclaimer` (case-insensitive) — zero hits in all three files. There is
no `DISCLAIMER` string constant, no `build_predictions_text()`/
`build_result_text()` pair, and no `assert DISCLAIMER in ...` anywhere in
this cycle's executable record. The only place disclaimer-adjacent
language appears at all is `NOTES.md` line 307–308, in prose, in the
Idealizations section: *"`DISCLAIMER` text (exp-105/106's own standing
perceptual/expressibility disclaimer, R23 code-enforced) applies
unchanged."* That sentence is true of exp-105/106's own `run.py` — it is
not true of exp-107's. This cycle's `run.py` never generates a
Predictions/Result text via code at all (Tier-1's predictions and results
live as hand-written NOTES.md tables, and Tier 0 is explicitly "text-only,
zero code"), so the entire R23 machinery this program built specifically
to prevent "manual prose-carrying-forward" was simply not reused — the
disclaimer this cycle actually relies on (the NETD-is-not-a-human-
threshold sentence, and the "no Weber-contrast/C_thr(L) scoring performed"
sentence) is manual prose, unchecked by any assert, exactly the discipline
R23 exists to replace.

I want to be precise about the stakes, not overclaim them: this cycle's
own Red Team audit and my own reading agree constraint-3 is genuinely,
correctly N/A throughout (§1 of `phase2_redteam_audit.md`: "constraint-3
is not engaged by any branch of this cycle"), so nothing was scored
against an unstated or misapplied perceptual threshold — the disclaimer's
absence from code is not currently load-bearing. But it is a real,
previously-unflagged data point in the disclaimer-erosion lineage this
program has already named three times before (R16, R21, R23's own
founding and Iteration-82 partial-loss instances) — this is, structurally,
the SAME channel (a document whose Idealizations section makes a
perceptual/expressibility scope claim) losing its code-level backing
entirely, one cycle after exp-106's own Phase 5 called R23 "the cleanest
implementation in the three-cycle lineage." Whether this counts as a
formal recurrence on R23's own text is a governance call for Red
Team/the Director, not mine to rule on unilaterally — but I flag it
plainly, with sources, per my own duty clause, rather than let it pass
silently because "T1 was N/A anyway."

## 3. Item 4's finding: solver-numerics, not perceptual — stated plainly

Item 4 found the article-scene window numerator is contaminated by the
solver's own noise floor at both measured r (`frac_unresolved=0.18275`
at r=156, `0.2675` at r=312, both against a `≤0.10` clean band) —
independently confirmed bit-exact across `results.json`, `run_output.txt`,
and `finalize.py`'s own independent re-derivation from the checkpoint
pickles. **This has no perceptual-science-relevant interpretation, and I
say so plainly rather than manufacture one.** `frac_unresolved` measures
whether individual FDTD grid cells' `|Ez|²` intensity, inside a fixed
window box, sit above `floor_frac × rms` of that same box's own pool —
a statement about whether the solver's floating-point/discretization
noise floor swamps a physically real but small signal at that
resolution. It says nothing about luminance, contrast, adaptation state,
spectral sensitivity, or any quantity a human retina responds to; the
window in question is not being compared to any human detection
threshold this cycle (T1: N/A, constraint-3 correctly unscored). This is
squarely PHOTONICS'/ELECTROMAGNETISM's/Red Team's territory — whether
`kappa_window`'s own headline "accelerating collapse" (exp-102/105/106)
partly reflects this same numerator-side noise floor rather than
genuine physics is a real, important, and correctly-flagged open
question (NOTES.md's own Next item 1) — but it is a question about
instrument fidelity, not about what a human eye would fail to register.
My charter does not get to claim relevance here just because the word
"floor" appears in both this instrument and mine; the two floors
(solver noise vs. perceptual threshold) share nothing but the English
word. Manufacturing a perceptual reading of this number would itself be
the kind of unjustified cross-charter overreach PANEL.md's "speaks only
from its own discipline" rule exists to prevent.

## 4. Was "execute the census, name a process not a verdict" the right call?

Re-reading `disposition_memo.md` at the source (not from memory): its
own "ceiling" paragraph is unconditional — *"Under NO branch of this
memo's own per-outcome conditional does a genuine new realizability
question ever open."* I had already read and *quoted this exact
sentence in my own Phase-1 proposal* (§1: "MATERIALS' own disposition
memo (exp-100) proves a second, independent ceiling..."). I did not miss
this argument's existence or its content. What I did was treat it as a
consideration for Phase 2 to weigh against a competing procedural
concern (Red Team's own text foreclosing a silent eighth deferral),
rather than draw the conclusion myself that a *written, cited retirement*
— not only a data-bearing census — discharges that same deferral
obligation, matching Iteration-51's own on-file precedent (a standing
item closed by reasoned retirement, not only by one more data point).
That precedent was equally available to me at Phase 1; I did not cite it
or weigh it against my own "must execute, not merely scope" framing.

**Honest answer: I should have recognized the ceiling as dispositive on
my own, without needing Phase 2 to surface it — the information to do so
was not new at Phase 2, it was already in my own document.** The
disposition memo's own text was not ambiguous, and the Iteration-51
retirement-by-writing precedent was on file and directly analogous. My
own §1 came close — I *named* the ceiling — but then explicitly punted
the "is a bounded, gated spend still worth it" judgment to Phase 2
("that is their call to override... I name the process, not the
verdict") rather than applying my own charter's stated duty (pin
thresholds *before* any run, not merely disclose that someone else could
object to the run). Given I had already independently established
(correctly, and un-challenged) that `delta_scene` sits sub-threshold
under either resolution family's own reading, the marginal information
value of resolving *which* family is "more correct" was never going to
move any constraint-3 verdict I own — I had the two facts needed to
reach retirement myself and did not connect them.

**The steel-man, stated fairly.** The panel process is explicitly built
so that no single seat, including the lead, needs to get every call
right alone — Phase 2's entire function is adversarial surfacing of
exactly this class of error, and my own §7 pre-registered the specific
challenge ("if the ceiling makes even this bounded spend not worth it,
that is a valid override") that in fact fired. The outcome is the
system working as designed, not failing: zero FDTD budget was spent on
a doomed design, the retirement text is better-sourced and more
precisely scoped than my own Phase-1 framing would have produced
unchallenged (PHOTONICS' correction folded a properly-cited 63%-of-bar
figure into the permanent record instead of my mistaken 8–12% one), and
my own bundled, structurally-independent Tier-1 items — which had no
defects found against them — proceeded and delivered real, honestly
mixed results. A design that pre-registers its own falsification
conditions this explicitly, and is corrected by exactly the mechanism
built to correct it, before any irreversible cost, is not a design
failure in the sense that matters most to this program's own house
discipline (R5/R6/R7's entire lineage exists to keep costly, wrong
designs from reaching Phase 4 — this one didn't).

## 5. Verdict on this cycle's actual outcome: **CONFIRM-WITH-GAPS**

The filed outcome is sound. Tier 0's retirement is correctly scoped,
correctly cited, and does not overreach — it closes the resolution-
family-attribution question while explicitly leaving T28's larger
mechanism question and every other standing deferred item open, matching
this program's own Iteration-51 precedent in substance. Tier 1 is
genuine, disclosed, and honestly graded rather than smoothed toward a
clean story: Item 3 is a real methodological improvement (first
real-ledger-measured, non-placeholder P5 row on this channel) and
reproduces its own pre-registered table to floating-point precision;
Item 1 passes only the loose band, stated as an honest partial rather
than claimed as a tight reproduction of the T9 anchor; Item 4 falsified
its own r=156 prediction and surfaced a genuinely new, previously
unconsidered gap in `kappa_window`'s own trust chain. The disclosed
execution-methodology detour (`chunk_runner.py`/`finalize.py`, forced by
a background-execution slowdown this session diagnosed and disclosed,
not hidden) reproduces `run.py`'s own formulas bit-exact, independently
confirmed by my own read of `finalize.py` against `run.py`'s
`item1_and_4_one_r()`.

The gaps are real but non-load-bearing: my own Phase-1 proposal shipped
two independently-caught, pre-Phase-4 defects that I should have caught
applying my own charter's duty clause to my own text (§1–§2 above), and
I found a third, previously-unflagged gap this shift (§2, the R23
code-enforcement lapse) that nobody's mandate this cycle happened to
name. None of the three changed any scored number, any constraint
verdict, or the Combined Verdict PARTIAL already on file — but three
independently-findable gaps in one document's governing narrative,
however non-load-bearing individually, is exactly the density pattern
this program's own R20/R4 lineage was built to notice. I do not believe
it clears R20's own three-or-more bar in the sense that rule was written
(R20 requires defects surviving Phase-3 freeze into Result/Learned; my
two Phase-1 defects were caught and corrected before freeze, and the
R23 gap is a code-absence, not a citation/figure-reproduction mismatch)
— but I name the pattern for Red Team to rule on, not to pre-empt that
ruling myself.

## 6. The single most important thing for Iteration 85

**Run item 4's numerator noise-floor check on the actual PEC-cored
PRIMARY article** (self-similar and fixed-abs, r=156/312) — not the
hollow substitute this cycle used. This cycle's own Item 4 measured a
real, 18–27% noise-floor contamination on a *different* physical scene
than the one `kappa_window`'s own P2/P3 shape-fit was scored from
(disclosed explicitly, not smoothed over, in this cycle's own NOTES.md).
Until the genuine article is checked, exp-102/105/106's own headline
"accelerating collapse" carries an open, plausible, and now
quantitatively-motivated numerics confound that no prior cycle's
Phase-5 review flagged with a number this concrete. This is squarely a
solver-fidelity question (§3, above) — not my charter's question to
answer — but it is the one open item this cycle leaves that could
change how much trust a future constraint-adjacent citation of
`kappa_window`'s shape-fit should carry, and it is cheap (this cycle's
own Next item 1 already names it, low marginal cost if a captured-field
checkpoint is saved). Separately, and smaller: restore a code-level
`DISCLAIMER`/assert mechanism the next time this document family scores
anything perceptually-flavored, so the R23 lapse I found here does not
recur on a cycle where constraint-3 actually is in scope.
