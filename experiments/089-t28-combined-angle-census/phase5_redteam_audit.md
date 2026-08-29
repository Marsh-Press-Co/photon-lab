# PHASE 5 — RED TEAM FINAL AUDIT · exp-089 · Panel Iteration 66

*Fresh context. Read in full: `PANEL.md`; `LOGBOOK.md`'s RULED OUT (R1–R14,
R13/R14 in full) and ESTABLISHED sections; T28 live-thread history through
Iteration 65/exp-088 close, both CHECKPOINT entries (Iteration 61 and
Iteration 65), with particular attention to the Iteration-65 CHECKPOINT's own
language for a fourth disclaimer-erosion instance and exp-088's own Phase-5
Red Team audit's ruling on when a caught-blind gap does vs. doesn't fire
criterion 4; the complete exp-089 record (`phase1_proposal.md`, all five
Phase-2 critiques, `phase2_redteam_audit.md`, `phase3_synthesis.md`,
`NOTES.md`, `results.json`, `run.py`, `run_output.txt`); all six Phase-5
blind reviews; `experiments/088-.../phase5_redteam_audit.md` for house-style
calibration. Every load-bearing number below was independently recomputed
from `results.json`/`experiments/083-.../results.json`/`experiments/087-
.../results.json`/`experiments/088-.../results.json` raw primitives by a
standalone script — not trusted from any seat's own prose (R4/R9
discipline). No FDTD run. No file other than this one modified.*

## 0. Independent verification performed before adjudicating anything

- **All primitives reproduce bit-exact.** `frac_p_abs`, `frac_contrast`,
  `ratio_k` at 37.2°/40.2°/41.4° all reproduce exactly from raw `thermo::
  p_abs_w` and `experiments/083-.../results.json::per_theta` fields,
  matching every cited figure across the proposal, all five Phase-2
  critiques, the Phase-2 Red Team audit, `NOTES.md`, and all six Phase-5
  reviews: `ratio_k` = 3.4432952384206352 / 25.082014394860607 /
  28.80719359552826.
- **R13 floor margins** reproduce exactly: 2.1709× / 1.4764× / 1.3095×.
  `FLOOR=1.91744×10⁻⁴`, re-derived fresh (via `compute_floor()` re-
  invocation against unchanged `exp-083` data, per MATERIALS' §1 — not a
  hand-copied literal) and confirmed bit-identical to exp-088's own filed
  value.
- **Zero-crossing distances, independently re-derived by linear
  interpolation of `delta_scene(θ)` on the real 31-point grid**
  (`experiments/083-.../results.json::per_theta`, confirmed directly, not
  taken from any cited number): crossing between 40.2° (`delta_scene=
  −1.541×10⁻⁴`) and 40.4° (`+3.170×10⁻⁴`) → **40.2654°**, distance from the
  sampled point **0.0654°**. Crossing between 41.4° (`+1.337×10⁻⁴`) and
  41.6° (`−3.055×10⁻⁴`) → **41.4609°**, distance **0.0609°**. On this
  program's own 0.2° grid, both sampled points (40.2°, 41.4°) are the
  *closer* of the two grid points flanking their respective crossings
  (the alternative neighbors, 40.4°/41.6°, sit 0.135°/0.139° away) —
  **the closest possible grid point to each crossing**, exactly as
  `phase1_proposal.md` §1 states its own selection rule was designed to
  produce ("the tightest-floor-margin grid neighbor of each remaining
  zero-crossing"). This is not a close call or a matter of interpretation.
- **The load-bearing numerator/denominator decomposition, independently
  re-derived by two methods, both matching THERMODYNAMICS' and QUANTUM's
  own independent figures exactly** (§1 below).
- **`NOTES.md`'s own dual-section banner**, checked by direct grep: present
  and correctly worded at the top of both the Predictions and Result
  sections, naming Idealizations 2/7/8/9-10/11/16. Per-item citation
  audit (mirroring VISION's own table) confirms Idealizations 9-10 are
  present at **both** Predictions and Result for every ratio_k/ENERGY-
  DOMINANT-bearing item (Q3, Q6, Q7) — the disclaimer-carrying machinery
  itself is intact and working as designed this cycle.
- **`run.py`'s R14(a) gate code, read directly** (lines 369–385): confirms
  EM's finding exactly — `tol = NOISE_MULT * 0.02 * v_prev` is applied
  unconditionally to every step, never branching to the real `box_dev`
  values already loaded in the same script. Non-blocking (§4).

No arithmetic, indexing, or citation defect was found anywhere in this
cycle's own record. Every substantive finding below is a mechanistic-
attribution, framing, or scoping matter — not a wrong number — matching
every Phase-2 and Phase-5 seat's own conclusion.

## 1. Independent re-derivation of the four-way convergent finding

Reproducing PHOTONICS', EM's, THERMODYNAMICS', and QUANTUM's own
decompositions from raw `results.json`/`experiments/083-.../results.json`
primitives, by an independent script, using two separate methods:

**Method A — counterfactual substitution.**

- Swap in a "typical," non-crossing-adjacent `frac_contrast` (mean of the
  two nearest already-established CONSISTENT points, 38.8°=1.5375×10⁻³ and
  41.8°=1.2634×10⁻³ → 1.4005×10⁻³), holding the actual measured numerator
  fixed: `ratio_k(40.2°)=7.100×10⁻³/1.4005×10⁻³=5.070`;
  `ratio_k(41.4°)=7.233×10⁻³/1.4005×10⁻³=5.165` — **both collapse to
  squarely CONSISTENT**, matching QUANTUM's own 5.07/5.17 exactly.
- Swap in the numerator's own pre-registered "smooth-trend" desk estimate
  (Q4's own comparator, `6.5427×10⁻³`/`7.0463×10⁻³`), holding the actual
  measured denominator fixed: `23.11` vs. actual `25.08` (**7.9%** off);
  `28.06` vs. actual `28.81` (**2.6%** off) — the classification **stays
  ENERGY-DOMINANT** either way, matching PHOTONICS'/EM's/the Phase-2
  audit's own ≈23.1/≈28.1 exactly.

**Method B — log-decomposition against the last previously-established
point (38.8°).**

| θ | `frac_p_abs` ratio vs 38.8° | `frac_contrast` ratio vs 38.8° | `ratio_k` ratio vs 38.8° | numerator's log-share | denominator's log-share |
|---|---|---|---|---|---|
| 40.2° | 1.1923× | 0.18412× (5.43× collapse) | 6.476× | **9.4%** | **90.6%** |
| 41.4° | 1.2146× | 0.16331× (6.12× collapse) | 7.437× | **9.7%** | **90.3%** |

(Checked exactly: `log₁₀(1.1923)+log₁₀(1/0.18412)=0.0764+0.7349=0.8113=
log₁₀(6.476)`, and likewise at 41.4°.)

**Both methods, independently re-derived from primitives here (a fifth
independent computation, after PHOTONICS/EM/THERMODYNAMICS/QUANTUM), confirm
the four-way convergent finding exactly and quantitatively: the `ratio_k`
swing at 40.2°/41.4° is ~90%/~10% attributable to the denominator
(`frac_contrast`, an R13-class zero-crossing-proximity effect) vs. the
numerator (`frac_p_abs`, ordinary smooth continuation within 2.6–8.5% of
its own pre-registered, explicitly-distrusted linear-trend estimate).**
This is not a marginal or contestable finding — four independent
decompositions (PHOTONICS' sigma/ratio-cross-section framing, EM's local-
trend-percentage framing, THERMODYNAMICS' Taylor/σ_ext framing, QUANTUM's
counterfactual-substitution framing) and this audit's own fifth, all
converge on the same conclusion via structurally different methods, with
numbers matching to 3+ significant figures.

## 2. Ruling A — QUANTUM's "factually false claim in NOTES.md's own Result text"

**CONFIRMED. The claim is false, independently verified from primitives
(§0). It is a materially incorrect statement in the frozen, Phase-4/Result-
stage record.**

`NOTES.md`'s Q6 Result paragraph (line ~331) states:

> "This is a SECOND and THIRD floor-clearing, **non-artifactual**
> ENERGY-DOMINANT angle — not one isolated node (38.6°, already excluded by
> R13) but two more, **both away from any previously-known zero-crossing's
> immediate neighborhood.**"

Both clauses are false as written, independently re-verified at §0/§1
above: 40.2° and 41.4° sit 0.065° and 0.061° from real, independently-
established `delta_scene` zero-crossings — the closest available grid
points to those crossings, chosen *for* that reason by this cycle's own
Phase-1 design (`phase1_proposal.md` §1's own "tightest-floor-margin grid
neighbor of each remaining zero-crossing"), and the swing itself is ~90%
mechanistically attributable to that exact proximity (§1). "Non-
artifactual" is at best a narrow, technically-defensible restatement of
"not excluded by R13's own binary `floor_pass` flag" — but as written, and
as it will be read and cited, it asserts the opposite of what §1's
decomposition shows: the finding *is* explained by zero-crossing proximity,
almost entirely.

This is not a subtle inference gap. It directly contradicts:

- **This same document's own §4/Idealization-16 framing**, one section
  earlier, which explicitly selects these two angles *because* they are
  the tightest-margin grid neighbors of the two remaining crossings.
- **Q5's own correct diagnosis, one paragraph before Q6 in the same
  document**: "`FLOOR_FRAC=0.10`... is not fully protective near a
  zero-crossing" — a sentence that is only true, and only makes sense,
  *because* these angles are near a zero-crossing. Q6 then asserts they
  are not.

## 3. Ruling B — does this fire Checkpoint criterion 4 as a fifth disclaimer-erosion instance?

**NO. This is a distinguishable defect, not a fifth instance of the R6–R14
disclaimer-erosion lineage. Checkpoint criterion 4 does NOT fire on this
finding.** I reasoned through this explicitly, against both possible
answers, before ruling.

### 3.1 What the disclaimer-erosion "shape" actually is, checked against all four cited instances

I re-read all four cited instances at their own LOGBOOK/CHECKPOINT text
(Iteration 53/T16, Iteration 63/exp-086, Iteration 64/exp-087, Iteration
65/exp-088) rather than pattern-matching from the label alone. In every
one, the defect is the same specific mechanism: **a scope-limiting
qualifier or caveat that already exists somewhere in the cycle's own
record — in `results.json`, in an adjacent prose section of the same
document, or as an explicitly flagged risk — fails to propagate into a
load-bearing prose restatement that needed it.** It is a completeness/
omission failure of an *existing, correct* qualifier. exp-088's own
instance is the cleanest example and the one this cycle's own machinery was
built to prevent: `results.json::netd_disclaimer` carried the correct text
throughout, and Q1/Q5/Q6 correctly restated it — only Q4 silently dropped
it.

exp-089's Q6 defect is mechanistically different. It is not an omission of
a caveat that exists elsewhere — it is an **affirmative, freshly-composed,
false empirical claim** ("away from any... neighborhood," "non-
artifactual") that was never true anywhere in the record and now
contradicts the very data (§4/Idealization 16, Q5) sitting immediately
around it. The dual-section banner and Idealizations 9-10 — the actual
machinery that failed four times before — are independently confirmed
intact and correctly present at Q6 in both sections (§0 above; VISION's own
per-item citation table, §3 of their review, confirms this directly). **The
disclaimer-carrying machinery worked. What failed is a separate, new
mechanistic claim that nobody had reason to write a disclaimer against,
because nothing like it existed in this record before.**

### 3.2 Was there a real fifth-instance risk this cycle, and was it discharged?

Yes — but it was a different defect, and it *was* discharged, before Phase
3. The Phase-2 Red Team audit (§6, §9-10) found `phase1_proposal.md`'s own
first draft *did* commit the actual disclaimer-erosion shape: Idealizations
8 and the FLOOR/RMS specificity caveat appeared once, in §5, with zero
inline occurrence in §6's own "committed... predictions." That audit
explicitly named this "at material, immediate, and elevated risk of firing
automatically as this sub-thread's FIFTH disclaimer-erosion instance,"
ruled the fix mandatory (not merely recommended), and Phase 3 adopted it in
full. Independently reconfirmed at §0 above and by every one of the six
Phase-5 reviews: the fix landed, and held through Phase 5. **The actual
near-miss for a fifth disclaimer-erosion instance this cycle already
happened, was caught blind at Phase 2 (an even earlier, more precautionary
catch than any of the first four instances, none of which were caught
before Phase 3 adoption), and was closed before Phase 3 froze anything.**
QUANTUM's finding is a separate defect in a separate section, discovered
after that fix had already landed successfully.

### 3.3 Is there textual support for an unconditional "fires automatically" rule reaching a fifth instance of *any* kind?

I checked directly rather than assuming. Iteration 64's close used
unconditional language for **a fourth instance specifically** ("a fourth
instance fires automatically... no further deliberation") — I find no text
anywhere in LOGBOOK.md's Iteration-65 CHECKPOINT entry, or in exp-088's own
`NOTES.md`/`phase5_redteam_audit.md`, generalizing that unconditional
language forward to a fifth, sixth, or later instance of the *identical*
shape, let alone to a different shape. What Iteration 65's own record
actually commits to is structural, not punitive-by-default: "the fix that
prevents a fifth instance" (exp-088's own audit, Tier-0 item 1) — the
mandatory dual-section banner is the mechanism meant to make a fifth
instance of *that specific shape* not occur, not a pre-written verdict for
if one does. Since §3.2 shows the actual banner-carry-forward machinery
held throughout exp-089's frozen record, there is no fifth instance of that
shape for any such rule to apply to, written or unwritten.

### 3.4 What Q6's defect actually is, and the closest precedent for it

This is squarely the R4/R9 "verify-before-claim" lineage: an unverified,
uncited absence/negation claim ("away from...") entering the permanent
Phase-4/Result-stage record. **The closest and most instructive precedent
is not any of the four disclaimer-erosion instances — it is QUANTUM's own
mistake one cycle earlier**, at exp-088's own Phase-5 Secondary Note
("No fourth disclaimer-erosion instance found in the filed record"),
independently proven false by that cycle's own Red Team audit. That audit
ruled explicitly: non-firing (inert, caught blind, same cycle, before
LOGBOOK), and logged it as "a should-not-recur data point for the R4/R9
registry" — a new discipline note, not a fifth numbered instance of R6–R13,
and not a Checkpoint-4 firing. The two cases are structurally close:
both are unverified negative/absence claims ("no fourth instance exists" /
"away from any... neighborhood") entering a document at the Result/review
stage, both independently caught false by direct primitive re-derivation,
both non-load-bearing to any underlying measurement. The one difference —
QUANTUM's own false claim last cycle sat in a Phase-5 review (a secondary,
blind-critique layer, corrected before it could reach LOGBOOK), while this
cycle's false claim sits in `NOTES.md` itself (the primary frozen record,
Phase-4/Result-stage) — is a real aggravating factor on placement, weighed
below, but does not itself convert a *different mechanism* (an affirmative
false claim) into an instance of a *specifically-defined* lineage
(disclaimer carry-forward omission) that it does not share the failure
shape of.

### 3.5 Weighing the placement aggravation against the discharge test

The task brief is right to flag that this is Phase-4/Result-stage, not a
Phase-1 draft caught blind before Phase 3 — this is exactly the stage every
prior disclaimer-erosion firing occurred at, and it deserves scrutiny on
that basis alone, not a reflexive pass. But this program's own established
discharge test for a Checkpoint-4-adjacent finding — applied identically to
R4's, R6's through R13's, and R14's own founding/discovery instances, and
most recently to QUANTUM's own false Secondary Note one cycle ago — is:
**was the defect caught blind, independently, within the same cycle, before
any LOGBOOK entry exists, and is it non-load-bearing to any underlying
measurement?** Here: yes to all three. QUANTUM's Phase-5 review caught it
independently (one of six blind seats, with no cross-talk); it is caught
inside this same cycle, before this document (which precedes any LOGBOOK
entry); and it corrupts no underlying `ratio_k`/`frac_p_abs` measurement —
only a one-sentence mechanistic characterization in Q6's prose, immediately
correctable, with zero downstream numeric consequence (§1's decomposition
stands regardless of how Q6's prose is worded). This is precisely the
pattern this program has never fired Checkpoint 4 on before, for any rule's
founding/discovery instance or for a same-shift-caught near-miss — and I
find no principled basis, once the mechanism is actually checked rather
than pattern-matched from the label, to treat this one differently.

### 3.6 Ruling, stated explicitly

**Checkpoint criterion 4 does NOT fire on QUANTUM's finding.** It is a
genuine, real, independently-confirmed defect in the frozen record — logged
as a new R4/R9 registry note (§7, Tier 0 item 4) and requiring a mandatory
same-shift correction to `NOTES.md`'s Q6 text (§6) before this cycle's
record is treated as closed — but it is not the disclaimer-erosion
lineage's fifth instance: the machinery that failed four times before is
independently confirmed intact this cycle, the mechanism of this specific
defect (an affirmative false claim, not an omitted existing caveat) does
not match that lineage's own defining shape, and no text anywhere in this
program's record commits an unconditional, no-discharge consequence to a
defect of this different kind. This is a **new**, first-instance finding
in its own right (an unverified absence-claim entering `NOTES.md` itself,
one step more serious in placement than QUANTUM's own prior Phase-5-review
instance of the identical shape) — treated, per this program's own
founding-instance precedent, as the discovery instance rather than a
retroactive violation.

## 4. Adjudication of every other Phase-5 finding

**PHOTONICS — SUSTAIN, genuinely convergent with QUANTUM's mechanistic
finding (not duplicative — reached via an independent decomposition, sigma/
cross-section framing rather than counterfactual substitution) and
genuinely convergent with VISION's Learned-item-1 finding (§ below, via a
still further independent route — margin/outcome correlation vs.
mechanistic decomposition).** Its "R13-class denominator-margin failure
riding an unremarkable numerator" characterization is independently
confirmed exactly by §1 above. Its recommendation (retarget densification
at `frac_contrast`'s own local curvature near the true crossings, not
`frac_p_abs`) is sound and adopted into the ranking below.

**MATERIALS — SUSTAIN, correctly self-scoped as "not yet a violation."**
Independently re-checked by full-text grep: `FLOOR_FRAC=0.10` is correctly
scoped to `graded_black_shell`/600nm everywhere inside exp-089's own text;
the risk is prospective — a bare module constant, carried forward by
direct-import reference rather than a recomputed value, could silently
become a future cycle's inherited default if a `FLOOR_FRAC` recalibration
is filed without restating its own material/wavelength scope. This is a
genuinely new finding (not a repeat of exp-088's own forward-risk note —
it identifies a *specific, still-open* document region, Learned/Next, that
sits outside the mandatory banner rule's literal text). Does not fire
anything; logged as a same-shift-fixable forward-risk item.

**ELECTROMAGNETISM — SUSTAIN, the `run.py`/Idealization-11 code-prose
mismatch is confirmed exactly at §0 by direct source read.** Non-blocking
this cycle (every step passes by 10×–30× margin under either tolerance).
A real, cheap fix, not a Checkpoint matter. EM's further finding — the raw
signed numerator flips sign four times across the 8-point set, at
coarse-timing loosely consistent with half of T28's established period —
is a genuinely new, disclosed-not-oversold observation; adopted into the
ranking as motivation for the still-queued R14(b) formal fit.

**THERMODYNAMICS — SUSTAIN.** The Q7-vs-Q3 decoupling gap is real and,
unlike Q6's defect (§3), *is* structurally close to the Idealization-13/
§7.1 discipline already established for Q4 — but it is a **newly
identified** requirement (Q7-vs-Q3 decoupling was never established
anywhere in the record before this seat named it this cycle), not an
established caveat that silently dropped out of one restatement. Treated,
correctly, as a first-instance finding, not a disclaimer-erosion recurrence
— matching how R13/R14 themselves were treated as founding instances when
first identified. THERMODYNAMICS' own independent decomposition (§1 above)
is the same finding as PHOTONICS'/EM's/QUANTUM's, reached via a fourth
distinct method (Taylor/σ_ext) — genuinely convergent, not restated.

**VISION — SUSTAIN, genuinely convergent with PHOTONICS (independent
route, §4 above).** Independently re-derived the margin/outcome table at
§0: every point with FLOOR margin ≥3.88× reads cleanly CONSISTENT; every
point at ≤2.17× either fails the gate (38.6°) or reads ENERGY-DOMINANT/
barely-resolved (37.2°, 40.2°, 41.4°). Learned item 1's "not confined to
one node's immediate neighborhood" is, read plainly, a stronger and more
general claim than the data supports — the more accurate reading, per §1's
own decomposition, is "confined to zero-crossing-adjacent nodes, now shown
at three locations instead of one, still fundamentally the same R13-class
floor-gate-calibration story." VISION's own ruling that this is *not* the
disclaimer-erosion shape ("not disclaimer dropping this time, but causal
over-generalization") is correct and consistent with my own §3 ruling on
Q6 — the same underlying document-wide pattern (confident language
outrunning what a specific data table supports) recurring in two different
paragraphs of the same NOTES.md, via two different mechanisms (Q6: false
factual claim; Learned §1: unsupported generalization), neither of them
the historically-fired disclaimer-omission shape.

**QUANTUM's own Ruling A finding — SUSTAIN as the cycle's single most
important correction (§2, §3 above).**

**Genuinely convergent pairs, not duplicative, across this cycle's Phase-5
record:** {PHOTONICS, EM, THERMODYNAMICS, QUANTUM, this audit} on the
numerator/denominator attribution (five independent methods, §1);
{PHOTONICS, VISION} on Learned item 1's overclaim (two independent methods,
§4); {MATERIALS, this audit's §3.2} on the disclaimer-machinery's own
forward-risk boundary (MATERIALS on `FLOOR_FRAC`'s scope, this audit on the
banner's own discharge). No two Phase-5 findings conflict.

## 5. Ruling on R13's `FLOOR_FRAC=0.10` — inadequate, but a new numbered rule is premature

**Demonstrated inadequate, with mechanism — not merely "maybe too loose."
A new binary-threshold numbered rule is premature at this cycle's own
sample size; a graduated/re-fit approach, deferred to a slightly larger
sample, is the right next step, not an immediate re-mint.**

Independently checked, sorting all 7 resolved points (excluding the
NODE-UNRESOLVABLE 38.6°) by FLOOR margin against outcome:

| margin | 1.31× | 1.48× | 2.17× | 3.88× | 6.59× | 7.49× | 8.02× |
|---|---|---|---|---|---|---|---|
| θ | 41.4° | 40.2° | 37.2° | 36.0° | 41.8° | 38.4° | 38.8° |
| outcome | ENERGY-DOM | ENERGY-DOM | CONSISTENT | CONSISTENT | CONSISTENT | CONSISTENT | CONSISTENT |

This is a **clean separation** on n=7: every misclassified point sits at
≤1.48×; every correctly-classified point sits at ≥2.17×. Any `FLOOR_FRAC`
value scaled so the pass threshold lands in the open interval (1.48×,
2.17×) — concretely, any `FLOOR_FRAC` value in **(0.148, 0.217)** —
perfectly separates this cycle's own 7 points. This is a real, quantified,
data-justified finding, not a vague "seems too loose" impression, and it is
now backed by *mechanism* (§1's >90% denominator attribution, replicated at
two of three known near-crossing angles: 38.6° at 0.39× and now 40.2°/
41.4° at 1.31–1.48×), not merely by outcome counts — the strongest kind of
evidence this instrument has produced for a calibration claim since R13's
own founding.

**But minting an exact new numbered threshold now is premature, for three
reasons, independently checked:**

1. **n=2 new near-boundary misses, both clustered at 1.31–1.48×** — there
   is no data anywhere in (1.48×, 2.17×) to know where inside that ~0.7×-
   wide gap the true separating boundary actually sits, or whether it is
   sharp at all rather than graded.
2. **NOTES.md's own "Next" section proposes 0.20–0.30× as a candidate
   range** — independently checked here: 0.20 sits inside the data-clean
   (0.148, 0.217) interval and would work on this sample, but **0.30 would
   NOT** — it would additionally exclude 37.2° (margin 2.171× under the
   current `FLOOR_FRAC=0.10`; under `FLOOR_FRAC=0.30` its margin becomes
   `2.171×(0.10/0.30)=0.724×`, below the pass line), a point this cycle's
   own data shows is genuinely, correctly CONSISTENT. The upper half of
   NOTES.md's own suggested range is not actually supported by its own
   data — a concrete, checkable correction for Iteration 67.
3. **This is still a binary-gate question being asked of what §1's own
   decomposition shows is fundamentally a continuous, mechanistically
   understood phenomenon** (`ratio_k` tracking `1/frac_contrast` smoothly
   as the denominator approaches its own zero). PHOTONICS' own proposal — a
   logistic/threshold fit against floor margin, using all 7 resolved points
   now on record — is the right zero-FDTD next step; it directly answers
   "is there a sharp separating value, and where" rather than picking one
   by inspection.

**Ruling: R13's `FLOOR_FRAC=0.10` is empirically demonstrated inadequate at
this material/wavelength, both by outcome (clean n=7 separation) and by
mechanism (the >90% denominator-attribution finding, independently
confirmed five ways). Do not adopt a new fixed numbered threshold this
cycle. Recommend: (a) PHOTONICS' own zero-FDTD logistic/threshold fit
against the now-7-point margin/outcome record as the immediate next step;
(b) explicitly correct NOTES.md's own "0.20–0.30" suggested range, since
0.30 is shown here to misclassify a genuinely CONSISTENT point on this
cycle's own data; (c) treat a graduated caution zone (already named as an
option in Q5) as more consistent with the now-established continuous
mechanism than a re-tuned binary cutoff.**

## 6. Mandatory fixes before this cycle's record is treated as closed

1. **[Mandatory, zero-FDTD] Correct `NOTES.md`'s Q6 sentence.** Replace
   "both away from any previously-known zero-crossing's immediate
   neighborhood" and "non-artifactual" with language stating the actual,
   verified facts: both angles sit 0.061°/0.065° from a real `delta_scene`
   zero-crossing — the closest available grid point, chosen for that
   reason by this cycle's own design — and the swing is ~90% attributable
   to that proximity (§1), not to any anomaly in the numerator. Corrected
   language (adapt freely): *"This is a SECOND and THIRD floor-clearing
   ENERGY-DOMINANT angle — not one isolated node (38.6°, already excluded
   by R13) but two more, both sitting within 0.061–0.065° of a real
   `delta_scene` zero-crossing (the closest available grid point to each,
   by this cycle's own design). The swing is, quantitatively, ~90%
   attributable to the denominator continuing to shrink toward that
   crossing and only ~10% to the numerator's own ordinary, on-trend growth
   (§ decomposition below) — mechanistically an R13-class floor-gate-
   calibration finding, not a new R14 numerator anomaly and not evidence of
   a phenomenon distributed independently of node proximity."*
2. **[Mandatory, zero-FDTD] Correct Learned item 1.** Replace "whatever
   T28's energy-interception channel is actually doing, it is not confined
   to one node's immediate neighborhood" with language that does not
   outrun the margin/outcome correlation (VISION §4, independently
   confirmed here §0): e.g., "not confined to the single node exp-088
   found, but the pattern (three of three near-crossing points measured to
   date misclassify or barely resolve, all comfortably-margined points
   classify cleanly) is fully consistent with a node-proximity/floor-gate-
   calibration story at three locations, not evidence of a phenomenon
   independent of zero-crossing proximity generally."
3. **[Mandatory, zero-FDTD] File the four/five-way convergent decomposition
   into the permanent record.** Currently exists only across four Phase-5
   reviews and this audit — add it to `NOTES.md` itself (a short paragraph
   or table under Q6, per fix item 1 above) so a future citation of exp-089
   does not have to reconstruct it from review documents.
4. **[Record hygiene]** Log QUANTUM's Q6 finding as a new R4/R9 registry
   note (§3.4 above): an unverified absence/negation claim ("away from...")
   entering a Phase-4/Result-stage document itself, one placement-step more
   serious than the Phase-5-review-stage precedent this same seat's own
   exp-088 self-review set one cycle earlier — both non-firing, both to be
   cited going forward as instances of the same registry item.
5. **[Recommended, zero-FDTD, before Iteration 67 files any `FLOOR_FRAC`
   recalibration]** Add MATERIALS' one-sentence scoping statement (§4
   above) alongside any new `FLOOR_FRAC` value.
6. **[Recommended, zero-FDTD]** Add THERMODYNAMICS' Q7-vs-Q3 decoupling
   sentence, mirroring Idealization 13's Q4-vs-Q3 treatment.
7. **[Recommended, cheap]** Fix `run.py`'s R14(a) gate to branch to real
   `box_dev`-derived tolerances where available (EM §5), matching what
   Idealization 11 already claims it does.

None of items 1–7 requires new FDTD or touches any underlying measurement;
all are same-shift, zero-marginal-cost corrections to prose/scoping. Item 1
is the single highest-priority fix — it is the corrected text a future
LOGBOOK/PLAN.md citation should quote instead of the current, false Q6
sentence.

## 7. Combined Verdict: PARTIAL

**Not RULED OUT** (no mechanism class foreclosed; T1 route N/A, matching
every T28 desk/instrument cycle since exp-069) **and not PROMISING** (no
constraint-metric progress claimed, correctly, by this cycle's own scope).
This cycle did real, logbook-advancing work: it ran the cheapest, most
decisive next test of R13's own floor gate at the thinnest margins this
sub-thread has ever sent to FDTD, got a genuine, honestly-disclosed,
"single most consequential possible outcome" surprise at both
lowest-confidence angles simultaneously, and — via four independently-
converging Phase-5 decompositions plus this audit's own fifth — the surprise
is now mechanistically *understood*, not merely observed: it is an R13
(denominator, zero-crossing-proximity) story, not a new R14 (numerator)
hazard, resolving the "vindicated or new mechanism" ambiguity the task
brief itself raised. That is a materially stronger scientific result than
exp-088 produced at the equivalent stage — a **corrected mechanistic
diagnosis**, not just a corrected classification.

Set against that: the record's own Q6 paragraph, as filed, states the
opposite of that diagnosis, in the same document, in a way that directly
contradicts its own Q5 paragraph one sentence away — an error a future
citer skimming only the bolded Result claims would carry forward
uncorrected. This is real and mandates a same-shift fix (§6) before the
cycle is closed, but — per §3's full reasoning — does **not** fire
Checkpoint criterion 4: it is a distinguishable, newly-identified,
same-cycle-caught, non-load-bearing defect, not a fifth instance of this
sub-thread's own specifically-defined disclaimer-erosion lineage. **No
CHECKPOINT entry is warranted for this finding.**

## 8. Reconciled Iteration-67 queue

Built by ranking, not concatenating, all six reviews' own top-3 lists —
weighing genuine convergence, load-bearing importance, and cost.

**Tier 0 — same-shift, zero cost, mandatory before this record is closed
(§6 above, items 1–7 in priority order as listed there).** Item 1 (correct
Q6) is the single most important item in this entire queue: it is free,
it is the exact sentence a future citation is likeliest to quote, and every
other finding in this cycle's own record already supports the correction.

**Tier 1 — cheap, zero-FDTD, immediate:**

1. **PHOTONICS' logistic/threshold fit of `FLOOR_FRAC` against all 7
   resolved points' own margin/outcome record** (§5 above) — the single
   highest-value next step precisely because it is free, uses data already
   in hand, and turns this cycle's own biggest open question (is 0.10
   really too loose, and by how much) into a defensible number rather than
   an inspection-by-eye range. Ranked above the FDTD-costing items below
   because it should inform how any densification bracket is designed.
2. **A targeted bracket at 40.2°/41.4°, retargeted per PHOTONICS'/EM's own
   correction**: not "isolated spike vs. broader elevated region" in
   `frac_p_abs` (already shown: no, the numerator is unremarkable there),
   but whether `ratio_k` tracks `1/frac_contrast` smoothly toward the true
   crossings (40.265°/41.461°) — sampling the "second-ring" ≈0.19–0.21°
   neighbors on the far side, mirroring 38.4°/38.8°'s own comfortable-
   margin relationship to 38.590° (VISION's own concrete design, §4 of
   their review). A 2–4 call bracket at each answers this directly and
   would supply the wider-margin data item 1's fit is currently missing.
3. **Both a temporal AND, for the first time on this channel, a spatial
   (`cpl`) resolution check at 38.4°** — R3's own standing meta-rule,
   named at Iteration 65's own CHECKPOINT, MATERIALS' own top exp-088
   ranking item, still undischarged two cycles running (MATERIALS' §3
   finding this cycle) — should not be deferred a third time without an
   explicit stated reason.

**Tier 2:**

- Run the still-queued R14(b) formal, null-controlled fit against the raw
  signed difference `p_abs(G40,θ)−p_abs(C40,θ)` (EM's own concretely
  strengthened case: 4-fold sign alternation, coarse-timing period-
  plausible but failing a naive single-tone amplitude check at 38.4°→38.8°
  — a real, structured, unexplained EM finding worth a proper fit).
- MATERIALS' `FLOOR_FRAC`-scoping sentence and THERMODYNAMICS' Q7-vs-Q3
  decoupling sentence, if not already folded into Tier 0.
- Fix `run.py`'s R14(a) proxy-tolerance mismatch (EM §5) before third reuse.

**Tier 3 — standing, unaffected by this cycle:**

- Execute Red Team's own Iteration-65 ranking item 2 (the ~124-call
  full/denser individual-`σ_abs(C40,θ)`/`σ_abs(G40,θ)` build) — now doubly
  motivated: it is the only instrument dense enough to properly fit both
  the `FLOOR_FRAC` recalibration (Tier 1 item 1) and the R14(b) period
  question (Tier 2) against real data rather than a 7–8-point sample.
- PHOTONICS' grazing-incidence validity check (still near-unanimous #1 on
  the whole T28 board).
- The x-wall wavelength-generality leg — now **FIFTEEN** consecutive
  cycles deferred (076–089), the single oldest item on the whole T28
  board.
- The still-queued full-scale null-calibration re-run; R12-into-standard-
  practice; leg-(b) work; QUANTUM's lossless-PEC-only-disk control;
  hardening `sections.py::widths()` to normalize by `abs(i_inc)`
  internally; the ritualization governance question (Iteration 61), still
  unresolved.

## 9. Files consulted

`PANEL.md`; `LOGBOOK.md` (RULED OUT R1–R14 in full, ESTABLISHED, T28 live-
thread history through Iteration 65/exp-088 in full, both CHECKPOINT
entries); `experiments/089-.../{phase1_proposal.md, phase2_critique_
{em,materials,photonics,thermodynamics,quantum}.md, phase2_redteam_audit.md,
phase3_synthesis.md, NOTES.md, run.py, run_output.txt, results.json,
phase5_review_{photonics,materials,em,thermodynamics,vision,quantum}.md}`;
`experiments/088-.../{results.json, NOTES.md, phase5_redteam_audit.md}`;
`experiments/087-.../results.json`; `experiments/083-.../results.json`. All
recomputation performed by independent Python scripts against raw JSON, not
by re-reading any seat's own tables.
