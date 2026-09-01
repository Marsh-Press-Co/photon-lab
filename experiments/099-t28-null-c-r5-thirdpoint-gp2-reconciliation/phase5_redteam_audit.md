# Panel Iteration 76 (exp-099) — Phase 5 RED TEAM FINAL AUDIT

*Speaks last, sees everything: `phase1_proposal.md`, all five Phase-2
critiques, `phase2_redteam_audit.md`, `NOTES.md`, `run.py`, `results.json`,
`run_output.txt`, and all six blind Phase-5 reviews (PHOTONICS, MATERIALS,
ELECTROMAGNETISM, QUANTUM OPTICS, THERMODYNAMICS, VISION SCIENCE) —
PANEL.md, LOGBOOK.md (R1–R19 in full, T1–T28 live threads), PLAN.md's
current state, and exp-098's own `results.json`/`NOTES.md` read directly.
Standard: not textbook-physics compliance — speculation is permitted. Kills
internal inconsistency, unfalsifiable claims, mechanisms that cannot be
expressed as simulation parameters, and quiet constraint violations
(especially #3, N/A this cycle). This is T28 house-discipline work, not a
new mechanism proposal — constraint-tags apply only where genuinely
relevant, per the Director's brief. Every load-bearing number below was
independently recomputed this session, from `results.json`/`run.py`
primitives and from exp-098's own committed files — nothing taken on any
review's word.*

## 0. Independent source-of-truth confirmations (before ruling on anything)

All performed this session, by direct Python read of `results.json` and
`run.py`/exp-098's own files (not retyped by hand):

1. **exp-098's own `richardson_diagnostic.B`, read directly**:
   `observed_ratio = 0.7765163757372424`, `naive_order2_ratio = 0.5625`,
   `note: "...corrected, Phase-5 Red Team audit..."`. exp-098's own
   `NOTES.md` line 461 tabulates `1.777` as the row explicitly superseded by
   line 543/689's own text: *"the corrected marginal-to-marginal ratio is
   0.777 (shrinking, same sign), not the originally-reported 1.777."*
   `1.777` exists in exp-098's permanent record **only** as the named,
   retracted, pre-correction figure. **PHOTONICS' finding confirmed exactly,
   independently, from exp-098's own source — not merely from this cycle's
   citation of it.**
2. **exp-099's own `item_1.r_ratios`, read directly**: `[1.3316739748300177,
   0.28337723580831364]`. Tracing `run.py:339-365`: `deltas_seq` is built as
   `[value at NULL_C_FILED_KEYS[3] (θ₀+0.500°)] + [3 new points, sorted]` —
   4 points, 3 differences (`diffs[0..2]`), and `r_ratios = [|diffs[1]|/
   |diffs[0]|, |diffs[2]|/|diffs[1]|]`. Using the same Δ-numbering
   `NOTES.md`'s own Result section already establishes for the four filed
   points (Δ₁, Δ₂, Δ₃), the natural continuation is Δ₄ (θ₀+0.500°→+0.833°),
   Δ₅ (+0.833°→+1.167°), Δ₆ (+1.167°→+1.500°). `diffs[0]=Δ₄=8.518395×10⁻⁴`,
   `diffs[1]=Δ₅=1.134372×10⁻³`, `diffs[2]=Δ₆=3.214553×10⁻⁴`. So
   `r_ratios[0]=|Δ₅|/|Δ₄|=1.3317` and `r_ratios[1]=|Δ₆|/|Δ₅|=0.2834`. The
   quantity `NOTES.md`'s Result section labels **`r₄=|Δ₄|/|Δ₃|`** is neither
   of these — I computed it directly: `|Δ₄|/|Δ₃| = 8.518395×10⁻⁴ /
   1.150032×10⁻⁴ = 7.407`, and confirmed the code **never computes this
   ratio at all** — `diffs[]` starts at Δ₄, so no `|diffs[0]|/|Δ₃|`
   comparison exists anywhere in `run.py`. **THERMODYNAMICS' finding
   confirmed exactly, independently re-derived from `run.py`'s own control
   flow, not merely from the printed numbers.**
3. **exp-099's own `item_2.step2.angle` vs. `item_2.step3.angles[2]`, read
   directly**: `step2.angle = 39.854853` (a hardcoded literal, `run.py:421`);
   `step3.angles[2] = 39.854519316666234` (`= theta_c40 − 0.067`,
   `run.py:474`). `run.py`'s own adjacent assert (`abs((theta_c40−0.067) −
   settle_angle) < 5e-4`) uses a loose, non-bit-exact tolerance — the code
   itself does not claim literal equality. `NOTES.md`'s Setup table (line
   251, frozen before any run) and its Result-section discussion nonetheless
   state the stronger claim of the two points being the same location.
   Gap: `39.854853 − 39.854519316666234 = 3.3368×10⁻⁴°`. **EM's finding
   confirmed exactly, independently traced to the same two source lines.**
4. **VISION's Phase-2 word-count table, independently recomputed by direct
   section extraction and `wc`-equivalent counting**: PHOTONICS steel-man
   117 / attack **182** (+32, 21% over); MATERIALS steel-man 135 / attack
   **151** (+1); ELECTROMAGNETISM steel-man **152** (+2) / attack 127;
   QUANTUM OPTICS 96 / 149; VISION (own Phase-2 critique) 145 / 135. **Three
   of five critiques exceed the ≤150-word cap on at least one section,
   matching VISION's own Phase-5 table to the word.**
5. **VISION's git-provenance finding, independently re-checked**: commit
   `d9f1006` ("Committing the partial log now to satisfy the stop hook's
   untracked-file check") diffs in exactly 12 lines of `run_output.txt`,
   ending at `"new angles=[42.294201, 42.627601, 42.960901]"` — the launch
   banner, before any of the 12 per-theta lines the crashed run would have
   printed. **No committed artifact anywhere in this repository preserves
   the crashed run's own completed item-1 console output.** Confirmed
   exactly.
6. **MATERIALS' `L_GEOMETRIC_M` claim, independently re-checked against
   `design_geometry.py`**: `L_GEOMETRIC_M_R4 = R4_R_OUT(156)×DX_M_R4(1.5e-8)
   = 2.34×10⁻⁶`; `L_GEOMETRIC_M_R5 = R5_R_OUT(195)×DX_M_R5(1.2e-8) =
   2.34×10⁻⁶`, both module-`assert`ed to `<1e-12` against the native
   `R_OUT×30nm` anchor. Confirmed bit-identical, confirmed a real,
   `assert`-enforced invariant, not an assumption.
7. **A minor, non-load-bearing bookkeeping check**: top-level
   `wall_time_s=8899.44s` vs. the sum of item_1's `wall_s` + item_2's
   step1/step2/step3 `wall_s` = `8825.98s` — a `73.46s` gap. Traced this to
   Step 0's ~9 `Sim()` constructions (never `.run()`), the registration
   preflight checks, and item 3's 155 `FastEval` evaluations plus general
   JSON-loading overhead — all zero-`sim.run()` work, consistent with the
   gap's small size. **Not a defect**; no reviewer raised it, and it does
   not warrant a numbered attack.

All source-of-truth checks above corroborate every review's own
independent-verification claims — I found no case where a seat's cited
figure failed to reproduce from source.

## 1. Adopt / Adopt-with-correction / Reject — each of the six reviews' own
findings, independently re-verified (not taken on the reviewer's word)

| Seat | Finding | My independent verification | Ruling |
|---|---|---|---|
| **PHOTONICS** | `NOTES.md`'s Result/Learned #4 cites exp-098's Richardson ratio as `1.777 vs. 0.5625`; the correct, currently-filed figure is `0.7765163757372424`, and `1.777` is a retracted, pre-correction number. Citing it inverts the qualitative claim (growing→shrinking). | §0.1 above — read exp-098's `results.json` and `NOTES.md` directly, confirmed `1.777` appears ONLY as the named-and-superseded figure. | **ADOPT, in full.** [correctness / R4-class] |
| **THERMODYNAMICS** (self-review) | `NOTES.md`'s Result section labels a ratio `r₄=|Δ₄|/|Δ₃|=1.332`; that formula actually evaluates to ≈7.41, and `1.332` is really `|Δ₅|/|Δ₄|` — the code's own `r_ratios[0]`. | §0.2 above — traced `run.py:339-365`'s own `deltas_seq`/`diffs` construction line-by-line; confirmed `|Δ₄|/|Δ₃|` is never computed by the code at all. | **ADOPT, in full.** [correctness / R4-class] |
| **ELECTROMAGNETISM** | `NOTES.md` states Step 2's settling angle (39.854853°) "coincides" with a Step-3 interior point; the true Step-3 point is 39.854519316666235° — a 3.34×10⁻⁴° gap, over 10× Attack 4's own label-mismatch magnitude, one order below VISION's θ₀-digit magnitude. | §0.3 above — read `run.py:421`/`474` and `results.json::item_2.step2.angle`/`step3.angles[2]` directly; confirmed the code's own assert uses a loose (`5×10⁻⁴°`) tolerance, i.e. the code does not itself claim exactness — only `NOTES.md`'s prose does. | **ADOPT, in full.** [correctness / R4-class] |
| **QUANTUM OPTICS** | `delta_scene`'s realizability content was never actually resolved — Iteration 59's "zero realizability content" rule was explicitly *not* reinstated at Iteration 60 ("genuine ambiguity remains"); NOTES.md's own §T1 trigger risks scoring a PAD-domain artifact as a material mechanism next cycle if honored literally. | Independently read LOGBOOK.md Iterations 53/59/60 in full (§0 of my required reading): confirmed exp-076 proved `PAD` lossless vacuum; confirmed Iteration 59 adopted "zero realizability content" as a framing rule; confirmed Iteration 60's own Phase-5 text reads *"MATERIALS correctly declined to auto-reinstate its own Iteration-59 rule (genuine ambiguity remains between two opposite-realizability readings)"* — never resolved in either direction across the 19 subsequent cycles I traced. | **ADOPT, in full — elevated to a mandatory precondition, not a mere recommendation (§4 below).** [inexpressible-mechanism risk / Red-Team-charter-native] |
| **MATERIALS** | `NOTES.md`'s §T1 disposition conflates a newly-verified fact (cpl/`L_GEOMETRIC_M` invariance across R3/R4/R5) with an inherited, not-re-tested claim (the tracked *feature's* own realizability irrelevance, from Iteration 59, not reaffirmed at Iteration 60). | §0.6 above (the geometric-invariance half) plus the LOGBOOK trace above (the inherited-claim half, same evidence QUANTUM independently reached). Both halves of MATERIALS' distinction independently confirmed. | **ADOPT, in full.** [correctness / claim-compounding, R4/R9-adjacent] |
| **VISION SCIENCE** | (a) 3 of 5 Phase-2 critiques exceed PANEL.md's 150-word cap, uncaught by Red Team's own Phase-2 audit; (b) the KeyError bugfix's "directly diffed" claim is not reconstructible from the committed git record. | §0.4 (word counts, exact match) and §0.5 (git history, exact match) above. | **ADOPT both, in full.** [(a) process/format; (b) correctness — unauditable-verification-claim, R4/R9-adjacent] |

No review is rejected. Every one of the six is independently re-derivable
from primitives exactly as claimed — this is an unusually clean Phase-5
crop by this program's own historical standard (cf. exp-069's own
Iteration-46 false-positive rate, or Iteration 66's affirmative false
claim). PHOTONICS, THERMODYNAMICS, and EM each independently caught a
**distinct** instance of the identical failure shape (a claimed-exact
citation/label that does not survive contact with source) in three
different sections of the same document — none restates another; each
traces to a different pair of source lines.

## 2. What all six reviewers missed — findings none of them raised

I found no new *substantive* physics or process defect beyond what the six
reviews already surfaced (my own independent from-primitives recomputation
in §0 turned up nothing new). What none of the six explicitly did, however,
is the thing my seat exists to do: **name the aggregate pattern across all
six reviews as a single, program-level finding, and rule on its
consequence.**

**2a. [pattern, cross-review synthesis] This single document (`NOTES.md`,
post-Phase-3-freeze) now carries FIVE separate instances of the identical
R4-class defect shape across its full lifecycle — two caught pre-freeze by
Red Team's own Phase-2 audit (θ₀'s digit insertion; the interior-angle
label mismatch, my own Attack 4 last cycle), and THREE more, none caught
until Phase 5, surviving into the frozen Result/Learned sections
(PHOTONICS' Richardson citation; THERMODYNAMICS' own r-index mislabel;
EM's settling-angle false-coincidence claim).** No single review states
this five-instance count explicitly — each names its own instance (or, for
Red Team's own Phase-2 audit, two instances) in isolation. Taken together,
across TWO consecutive T28 cycles this specific document's own §1/§2 lean
explicitly on "not hand-typed," "re-read this session, not assumed"
language to earn arithmetic trust, and the underlying discipline visibly
holds at Phase 2 (two caught, fixed, before freeze) but visibly does NOT
yet extend past Phase 3 into the writing of Result/Learned prose itself
(three new instances, uncaught until Phase 5). This is the pattern I rule
on formally in §3.

**2b. [minor, non-blocking] QUANTUM's own §3 finding (the PAD-vs-article
partition precondition) and MATERIALS' own §3 finding (the T1-disposition
claim-compounding) are, on independent re-reading, the SAME underlying gap
approached from two charters, not two separate findings — QUANTUM names
the forward risk (a future scoring pass), MATERIALS names the present
prose defect (a current mischaracterization). Neither review cites the
other (blind by construction), so neither states this convergence; I state
it here because it strengthens, not merely adds to, the case for treating
QUANTUM's discharge recommendation as mandatory rather than advisory (§4).**

## 3. Ruling on Checkpoint criterion 4

**Does not fire this cycle.**

Every one of the newly-caught defects (§0.1–0.3, §0.5, §2a's three
Phase-5-only instances) was caught **blind, within this same cycle's own
review layers, before this LOGBOOK entry** — matching, exactly, the
non-firing precedent this program has now applied five consecutive times
(R16/exp-094, R17/exp-095, R18/exp-096, R19/exp-098, and by the same logic
here). None is a "known, named, ignored" recurrence in the strict sense
R6–R19's own automatic-fire language requires: no prior cycle named any of
these three specific defects for this cycle to reuse unfixed, and R19's own
rule (call-count vs. row-count conflation, the most recent, most similar
precedent) was independently confirmed **correctly honored** this cycle
(EM's own §1.6 check: 40 calls map to a fully cross-checked job list, zero
call/row conflation anywhere). The KeyError (Learned #1) is a genuinely new
code location — a `run.py`-internal derived-statistic lookup that Attack
4's own fix (which addressed the "filed, reused" TABLE's hand-typed labels
specifically) did not, and could not, have reached — matching R16's own
"the code path that dropped the data was new" non-firing rationale exactly.

**But this is the closest call in the R4 lineage specifically that this
program has had, and the existing R4 rule has a real gap my own reading
surfaced: unlike R6 through R19, R4 has never carried an explicit
forward-elevating/automatic-fire clause.** R4 states the underlying
discipline ("any falsifier or self-consistency figure cited as 'precisely
recomputed' MUST be produced by invoking the actual committed function...
never hand-typed") and two addenda extending its scope, but no clause
telling a future cycle when a *recurrence density* on its own should
escalate to Checkpoint 4 regardless of individual load-bearing status —
every other standing rule in this program's registry (R6 onward) has
exactly this clause; R4, the oldest and most-repeated rule in the book
(five-plus prior invocations: exp-048, exp-072/073's sign-correction
addendum, exp-074's cell-count addendum, and now this cycle's own two
pre-freeze catches plus three post-freeze catches), does not. That is a
real, nameable gap in the program's own governance, independent of whether
this specific cycle fires.

**New standing rule, proposed and adopted NOW (R20)**: *Three or more
independent instances of an R4-class defect (a claimed-exact figure,
citation, label, or coincidence that does not reproduce from its own cited
source) surviving a document's own Phase-3 prediction-freeze into its
Result/Learned sections, each caught only at Phase 5 — not earlier — in a
single document, constitutes a Checkpoint-4-grade recurrence pattern on its
own, independent of whether any individual instance is load-bearing to a
scored verdict. A future cycle whose Result/Learned sections exhibit this
density fires Checkpoint criterion 4 automatically, no further
deliberation, matching R6–R19's own "known, named, ignored" escalation
standard — except that here the "known" precondition is discharged by THIS
rule's own text, not by a prior cycle's specific named instance.* **Does
not fire on its own founding instance** (exp-099), matching every prior
R-rule's own precedent (R5/R6/R9/R10/R11/R12/R13/R14/R15/R16/R17/R18/R19).
Separately, folding in THERMODYNAMICS' own explicitly-deferred-to-Red-Team
governance question (Learned #1: whether a construction-time-lookup
discipline deserves a standing rule, given a second cross-cycle instance of
the "reconstructed, not read back" root cause): **R20 covers this too, by
the same root text** — "does not reproduce from its own cited source"
applies identically whether the citation lives in prose or in a dict
lookup inside `run.py`. One rule, not two, for one root lesson, exactly as
`NOTES.md`'s own Learned #1 already argues. Full record: this document,
§0/§2a/§3; `experiments/098-.../results.json::richardson_diagnostic.B`
(exp-098's own retracted-figure record); LOGBOOK.md Iteration 76 (to be
written from this entry).

## 4. Combined Verdict: **PROMISING**

This is instrument/house-discipline work, not a constraint-1/2/3/4 test —
using this program's own established vocabulary for such cycles
(PROMISING/PARTIAL/MIXED, per R6–R19's own precedent cycles and PLAN.md's
own Current-state entries).

**Why PROMISING, not merely PARTIAL.** Item 2 — R5's first-ever real FDTD
spend in this program's 76-iteration history — is a genuine methodological
milestone, independently praised by MATERIALS and ELECTROMAGNETISM on
different grounds: it is the **first resolution family in this sub-thread's
entire history to clear a far-from-null ground-truth sign check (R15's
addendum) AND a full fault-injection re-scoring (R18's own standard) BEFORE
its first interior-near-null reading was trusted**, rather than earning
that discipline only retroactively (R3 and R4 both did). All three gates
(Step 0 fault-injection, Step 1 ground-truth sign, Step 2 settling) cleared
cleanly, and Step 3 then delivered a genuine, cleanly-bracketed sign change
plus a second independent Richardson-ratio data point at Null B — real
scientific content, not an idle, merely-unblocked capability. Item 1's
"bounce" (a genuine local trough, not the anticipated crossing or clean
decay) and item 3's honest non-resolution are both disclosed as such,
neither smoothed into false confidence — the correct scientific posture,
and PHOTONICS' own Attack-5-derived period gate (Fix 5) is empirically
vindicated by the result it correctly barred (VANISHING-AMPLITUDE would
have mis-scored a real oscillatory trough as an asymptote).

**Why not a clean PROMISING, unqualified.** Weighed against that
substantive achievement: the same document accumulated FIVE R4-class
defects across its lifecycle (§2a), three of them undetected past Phase 3,
plus a second-consecutive-cycle instance of the "filed data reconstructed,
not read back" root cause (Learned #1) in an entirely new code location,
plus VISION's second-in-three-cycles catch of a Phase-2 word-cap
recurrence uncaught by Red Team's own Phase-2 audit, plus one
verification claim in the frozen Result section that cannot be
independently re-audited from the committed git record. None of these is
individually load-bearing to any scored verdict — I confirmed this
directly for every one, above — but the density is real, new (R20 exists
because of it), and should be named as a genuine, if non-blocking, drag on
this cycle's own record-keeping quality, not waved off because the
underlying FDTD science is sound.

**Verdict, stated precisely, per item**: Item 1 — INCONCLUSIVE-AT-THIS-WIDTH,
correctly reached, genuinely new information (a located trough) underneath
the label. Item 2 — SIGN-CHANGE-FOUND, θc50≈39.77687°, all gates cleared,
a real methodological first. Item 3 — genuine non-resolution, honestly
reported. **All three item-level outcomes stand as computed and are NOT
disputed by anything in this audit.**

## 5. Reconciled, ranked Iteration-77 queue

All six reviews' own top-3 lists, resolved — not concatenated. Five of six
seats (MATERIALS #1, ELECTROMAGNETISM #1, THERMODYNAMICS #1,
VISION #1, and QUANTUM's own #1 as an explicit gating precondition on the
same action) converge on running THERMODYNAMICS' own committed
constraint-1/2/3/4 scoring-pass trigger next cycle. PHOTONICS alone ranks
it third, arguing Null C's own unresolved SIGN status and the
resolution-convergence-rate question should settle first. **This is a real
disagreement, resolved here, not merely noted.**

**Ruling on the disagreement.** QUANTUM's dissent and PHOTONICS' dissent are
not the same kind of objection and get different treatment. QUANTUM's
finding (§1 above, ADOPTED as mandatory) is a Red-Team-charter-native
concern — an inexpressible-mechanism risk, not a scheduling preference — so
it gates the trigger structurally: the constraint-scoring pass may not run
on raw `delta_scene(θ)` until the PAD-vs-article partition (below) has run.
PHOTONICS' concern (Null C's SIGN status, the Richardson ratio's own
still-open convergence behavior) is a data-quality caution, not an
expressibility one, and is better addressed as a **parallel, cheap
precondition folded into the same gating tier**, not as a reason to
demote the constraint-scoring pass a full tier below Null-C-only
instrument work — seven consecutive T1:N/A cycles is exactly the drift
PANEL.md's own Checkpoint criterion 4 language names, and further
Null-C-only bracket work without ever running the trigger repeats the same
"characterize the artifact in ever finer detail while deferring the
constraint-relevance step" pattern MATERIALS' own review names explicitly.

**Tier 0 — mandatory documentation fixes** (§6 below; must close before
this cycle's own record is treated as final).

**Tier 1 — preconditions that MUST run before any constraint-1/2/3/4
scoring pass touches `delta_scene(θ)`, bundled, zero-or-low marginal FDTD
cost:**

1. **QUANTUM's PAD-vs-article partition** (mandatory, elevated from
   recommendation): decompose `delta_scene(θ)` into a PAD-toggled/
   article-held-fixed leg and an article-toggled/PAD-held-fixed leg, at the
   same angles, reusing `ratio_abs_ext`/`p_abs_w` — already computed at
   every point this sub-thread has run, including this cycle's 17 new
   cells. Zero new FDTD beyond what Iteration 77 spends anyway.
2. **MATERIALS' disposition memo**, bundled with #1: a short, zero-FDTD,
   citable finding formally separating "the `cpl` resolution knob is
   physically inert (newly confirmed, R3/R4/R5)" from "the tracked feature
   itself carries zero realizability content (an inherited, still-genuinely-
   ambiguous framing question, per Iteration 59→60 — NOT reaffirmed since)."
3. **THERMODYNAMICS' own #2 / QUANTUM's own #3, merged**: a formal
   4-point (cpl=20/30/40/50) convergence characterization at Null B — is
   the Richardson ratio (0.777→0.962, climbing toward 1, not shrinking)
   evidence of genuine-but-slow convergence or a non-convergent recipe
   artifact (R15's own standing concern)? Zero new FDTD; all four points
   are already on file. This directly informs whether `delta_scene(θ)` is
   trustworthy enough to feed a scoring pass at all (PHOTONICS' own
   concern, discharged here rather than by further bracket-widening).

**Tier 2 — the scoring pass itself, gated on Tier 1's outputs, not
deferred a further cycle:** THERMODYNAMICS' own committed trigger — run
`delta_scene(θ)`'s (or, if Tier 1's partition finds the signal is
majority-PAD, its residual article-coupled component's) sign structure
through `emit.observer_record`, `lab/ambient.py`, and the beam-behind box,
per PANEL.md's own Metrics table. **If Tier 1 finds negligible article
coupling, this is not a license to skip Tier 2 — it converts Tier 2 into a
disciplined negative finding (this diffraction feature has no
constraint-relevant material analog), which is itself the honest,
overdue answer to seven cycles of deferred T1 status, not a reason to
defer an eighth time.** Whichever seat leads (rotation: QUANTUM OPTICS)
must inherit VISION's own already-pinned `C_thr(L)`/floor-gate machinery
(T2/T16/T21/T24/T27) rather than re-derive it — VISION's own §5 finding,
adopted here.

**Tier 3 — parallel/lower-priority, cheap, fold in opportunistically:**

- Null C's own trough, widened to the full ≥2.9474° established period —
  but per QUANTUM's 4b (adopted), first spot-check the trough's own
  cross-resolution stability (1–2 points at cpl=30 or cpl=50) before
  centering a wider search on it, matching R15's own discipline.
- VISION's own pre-flight perceptual-caveat note (which `C_thr(L)`
  parameterization, which uncertainty budgets, Tier-W vs. Tier-A) — cheap,
  zero-FDTD, should exist before Iteration 77's own proposal is drafted,
  not folded in after.
- EM's own persistence gap (`xi_ext`/`sigma_abs_nonneg` margins never
  written to `results.json`) and THERMODYNAMICS' own persistence gap
  (`p_abs_w`/`dt_ss_full_K`/`netd_classification` computed-then-dropped at
  Step 1/Step 2) — both cheap, zero-new-FDTD backfills, bundle together.
- The Richardson-pattern's lateral generalization to Null A — legitimate,
  lower priority than the vertical convergence question (Tier 1 item 3
  above), per QUANTUM's own explicit ranking.
- Item 3's direct GP2′-style recompute via exp-086's own narrow-window
  method (NOTES.md's own Next §4).
- Standing, now 5–8-cycle-deferred items, unchanged by this cycle: the
  x-wall wavelength-generality leg, the real 750/450nm leg, the
  PAD-with-article survival check (the single most overdue item on the
  whole T28 board) — if Iteration 77 defers these again, that must be a
  stated decision, not silence, per this sub-thread's own standing
  convention.

## 6. Mandatory-fix docket — what must be corrected in `NOTES.md` before
this cycle closes (documentation-only, zero-FDTD, all independently
verified above)

1. **Fix the Richardson mis-citation (PHOTONICS, §0.1/§1).** In Result and
   Learned #4: replace "exp-098's own Null-B Richardson figure (20/30/40:
   observed 1.777 vs. naive 0.5625)" with the corrected, currently-filed
   figure: `observed_ratio=0.7765163757372424` vs. `naive_order2_ratio=
   0.5625`. Rewrite the "super-linear-growth pattern... reproduced" framing:
   both `0.7765` (20/30/40) and `0.9623` (30/40/50, this cycle) are `<1`
   (shrinking, not growing) — the qualitatively correct, more reassuring
   reading — while separately noting (per QUANTUM's own §4a, folded in)
   that the ratio is climbing TOWARD 1 across the two data points, which is
   the actually consequential open question, addressed by Tier-1 item 3
   above, not by the retracted "super-linear growth" framing.
2. **Fix the `r`-index mislabeling (THERMODYNAMICS, §0.2/§1).** Replace
   "r₄=|Δ₄|/|Δ₃|=1.332" with a correct label — either restate as
   `r_ratios[0]=|Δ₅|/|Δ₄|=1.332` (matching the code's own indexing) or
   explicitly note that the trough-spanning ratio `|Δ₄|/|Δ₃|≈7.41` was
   never computed by the code, and that `1.332` describes the FIRST of the
   two NEW-interval ratios, not the boundary-spanning one the "r₄" label
   implies.
3. **Fix the false settling-angle "coincidence" claim (EM, §0.3/§1).**
   Correct Setup's table row and the Result-section discussion: state the
   true Step-3 interior point is `39.854519316666235°` (`θc40−0.067°`),
   `3.3368×10⁻⁴°` from the hardcoded Step-2 settling angle
   (`39.854853°`), not identical to it. State the smoothness argument as
   the actual basis for treating Step 2's PASS as informative for the
   Step-3 bracket (`delta_scene` differs by only ~0.4% between the two
   nearby points), rather than claiming literal coincidence.
4. **Separate the two conflated T1-disposition claims (MATERIALS/QUANTUM,
   §0.6/§1).** Reword §T1: distinguish "the `cpl` resolution knob is
   physically inert (newly confirmed for R5 this cycle, `L_GEOMETRIC_M`
   invariant to 1e-12)" from "the tracked `delta_scene` feature's own
   realizability status (an inherited, still-genuinely-open ambiguity from
   Iteration 59→60, NOT re-tested or reaffirmed this cycle, or any cycle
   since)." State explicitly that Iteration 60 declined to reinstate
   Iteration 59's "zero realizability content" rule.
5. **Correct or scope the "directly diffed" verification claim (VISION,
   §0.5/§1).** Either state explicitly that the item-1 crashed-vs-rerun
   comparison was performed in-session and is not independently
   re-auditable from the committed git record (the checkpoint commit stops
   before any item-1 per-theta output), or strike "directly diffed" in
   favor of that more accurate description.
6. **Log R20** (§3 above) into LOGBOOK.md's RULED OUT / standing-rules
   registry, folding in THERMODYNAMICS' own Learned #1 governance question
   as discharged by the same rule text.

**Not mandatory, recommended for a future cheap same-shift or Iteration-77
opportunistic fix (zero-FDTD but a data/code change, not pure prose):**
backfill `netd_row()` into `item_2.step1`/`step2` (THERMODYNAMICS' §3);
persist `xi_ext`/`sigma_abs_nonneg` margins into every report row (EM's
§4.1); tighten the over-permissive `total_calls in (40,24,16,20,32)` assert
to `(40,24)` (QUANTUM's §4c, MATERIALS' §4.2); add an explicit `note` field
inside `results.json`'s own `richardson_30_40_50` object clarifying the
relabeled keys (MATERIALS' §4.1).
