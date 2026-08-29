# PHASE 2 — RED TEAM FINAL AUDIT · Panel Iteration 67 · exp-090
## "Floor-Frac Threshold Fit"

Red Team reads everything: `phase1_proposal.md` plus all five blind
Phase-2 critiques (MATERIALS, ELECTROMAGNETISM, THERMODYNAMICS, QUANTUM
OPTICS, VISION SCIENCE). Scope note, stated up front per this cycle's own
precedent (exp-070, exp-085 leg-a, exp-089): this is a zero-FDTD T28
desk-statistics cycle, T1 route N/A, Checkpoint criterion 2 N/A. The
charter's four attack tags are adapted accordingly: `constraint-#N-
violation` is used here for a misstatement of a standing R-rule or the
LOGBOOK record (the closest analogue available in a mechanism-free
cycle); `unfalsifiable` is used in its literal sense — a stated
falsification condition that cannot fire, or a test whose "evidence"
value is already fixed by facts on the record; `inconsistency` covers
internal contradiction and failure to carry forward an already-disclosed,
load-bearing caveat; `inexpressible` does not apply anywhere in this
cycle (every method is concretely coded, deterministic desk arithmetic)
and is not used below.

## 0. Independent verification performed (before adjudicating anything)

I did not take any of the five critiques' "I independently reproduced
this" claims on faith either. From raw `results.json` primitives in
`experiments/087/088/089`, I recomputed, myself, from scratch:

- **All 7 `frac_contrast`/`margin`/`ratio_k` triples** (Table 1):
  bit-exact match, sorted margins `1.3095(X,41.4°), 1.4764(X,40.2°),
  2.1709(C,37.2°), 3.8793(C,36.0°), 6.5889(C,41.8°), 7.4946(C,38.4°),
  8.0187(C,38.8°)` — no ties, `AUC=1.0`.
- **P2, the exact permutation test**: wrote my own `C(7,2)=21`
  enumeration independent of every other seat's code. `p =
  1/21 = 0.047619047619047616`, bit-exact.
- **P4, Firth's fit**: implemented the modified-score Newton–Raphson
  update independently, from the formula alone. Converges in 19
  iterations to `β=(1.78058954, −5.63151961)`, `m₅₀=2.0710128` — matches
  the proposal's and two critiques' own figures to the digit.
- **EM's algebraic claim** (`Y=1 ⟺ margin < frac_p_abs/(10·FLOOR)`):
  recomputed the implied per-angle threshold at all 7 points myself —
  `0.6801 (38.4°) … 3.7724 (41.4°)`, bit-exact to EM's cited `0.680…
  3.772` range.
- **A load-bearing number none of the five critiques checked**: exp-089's
  own NOTES.md (Learned #4) states 37.2°'s *own* `resolved`-gate
  noise-floor margin — a different quantity from R13's `frac_contrast`
  floor margin, namely `|Δp_abs|/(NOISE_MULT·box_dev_max·p_C40)` — is
  "1.046×, the thinnest this sub-thread has ever accepted as
  `resolved=True`… a felt-lucky pass, not a robust one." I recomputed
  this myself from raw `box_dev`/`p_abs_w` primitives in
  `experiments/089/results.json` (`box_dev_max=4.569×10⁻⁴`,
  `p_C40=2.8127×10⁻¹²`, `Δp_abs=4.031×10⁻¹⁵`): **margin = 1.0455×** —
  confirms exp-089's own figure independently. See RT-1, below, for why
  this matters here.

Every load-bearing statistical number this proposal and all five
critiques cite reproduces. Nothing below is an arithmetic dispute.

## 1. Adjudication of the five blind critiques

### 1.1 MATERIALS — undisclosed R3 spatial-resolution gap on the load-bearing points — **UPHOLD**

Tag: `inconsistency`. MATERIALS is correct on every count I can check:
`grep` of `phase1_proposal.md` for "R3"/"resolution" returns nothing;
MATERIALS' own Phase-5 review of exp-088 and exp-089's own NOTES.md Next
section both already name this exact gap, twice, as "undischarged two
cycles running"; `VALIDATION.md` independently confirms the underlying
physical risk is real, not hypothetical, on this bench ("λ/20 resolution
staircases the tensor," line 319). The specific aim is sharp and correct:
the zone's *lower* edge is set by 40.2°/41.4°, the two points whose
`frac_contrast` sits closest to a real, established zero-crossing — the
exact regime where a small absolute (grid-quantization) perturbation
produces the largest relative shift in a near-zero denominator. This is
not a generic small-print gap; MATERIALS names precisely why it bites
where the method is most load-bearing. Fix is cheap and MATERIALS' own
proposed language is right-sized (disclosure only, not a new FDTD
gate) — adopted into the mandatory docket below (§4 item 2).

### 1.2 ELECTROMAGNETISM — the permutation test's null is not exchangeable with the generative mechanism — **UPHOLD**

Tag: `unfalsifiable`. I independently re-derived EM's algebraic identity
above and it holds exactly at all 7 points, with the implied threshold's
own range (`0.68–3.77`, a 5.55× spread) comparable to `margin`'s own
range (6.12×) — EM's point is not an edge case, it's structural. Given
exp-089's own five-way-converging decomposition already establishes the
40.2°/41.4° misclassification is ~90% denominator-driven (i.e., ~90%
attributable to `frac_contrast`, the very quantity `margin` *is*), a
label-permutation null that reshuffles `Y` across fixed margins is
testing how orderly R13's own algebra is, not whether nature's
floor-gate failure is surprising. This is the R10 lineage's own lesson
("regressor and label aren't exchangeable," there for a circular-shift
null; here for a label-permutation null) applied correctly to a new
instrument. EM's own proposed remedy (a measurement-uncertainty-derived
null, or else a purely descriptive reframing) is the right fix, and I
extend it: this attack and QUANTUM's (§1.4, below) compound — see §2 for
why both landing changes what "PROCEED" should look like for P2 and P5
specifically.

### 1.3 THERMODYNAMICS — the zone risks becoming a de facto sampling-deprioritization signal — **UPHOLD**

Tag: `inconsistency` (an undisclosed downstream-use risk in a proposal
that is itself, correctly, only about a trust label). THERMODYNAMICS'
logic is sound and independently checkable without new computation: by
construction, `margin` is small exactly where `delta_scene` is near a
zero, which THERMODYNAMICS' own established R14 finding (already on the
LOGBOOK record, not asserted fresh here) says is exactly where the
`σ_ext(θ)` config-differential term — the physical quantity the
already-ranked Tier-1/3 `σ_abs(θ)` build exists to resolve — is most
active. A future build that reads "CAUTION" as "avoid" rather than
"look harder here" would be a real, if not yet realized, misuse. The
requested one-sentence fix is proportionate and free. Adopted (§4 item
3).

### 1.4 QUANTUM OPTICS — P5's leave-one-out jackknife is a deductive tautology given P1, not an empirical stress test — **UPHOLD**

Tag: `unfalsifiable`. This is the sharpest of the five attacks and I
re-derive it independently, without running any LOO computation, as a
pure order-statistics fact: given `AUC=1.0` with **no ties** (P1, itself
verified above), (a) a subsequence of a strict, tie-free total order is
still a strict, tie-free total order — so "no LOO subset loses
separation" is guaranteed for all 7 refits with probability 1, not an
outcome that could have gone the other way; (b) a min/max order
statistic over a finite set is unchanged by removing any point other
than the current argmin/argmax — so 5 of the 7 "exhaustive" LOO refits
are, a priori, guaranteed to leave both zone edges bit-identical, and the
remaining 2 (drop the current argmin, drop the current argmax) are
guaranteed to move each edge to the *next* order statistic, which is
also a deduction, not a discovery. QUANTUM's own finding that the
proposal's stated falsifier ("Falsified if any LOO subset loses full
separation") can never actually fire, once P1 holds, is correct and I
find no way around it. This is not a defect in the *computation* — P5's
numbers, once run, will be exactly what QUANTUM (and I) predict from
algebra alone — it is a defect in the *evidentiary claim* attached to
running it. QUANTUM's own secondary observation (P2's "not a 7-point
coincidence" framing over-claims given the same margin/`frac_p_abs`
mechanistic relationship R13/exp-089 already established) independently
corroborates §1.2's finding above from a different angle — two seats
converging on the same underlying fact (margin and `Y` are not
exogenous) via different routes strengthens, not merely repeats, the
case for the joint fix in §2.

### 1.5 VISION SCIENCE — missing dual-section carried-idealizations banner in §4 — **UPHOLD**, with an explicit shape-ruling (see §3)

Tag: `inconsistency`. VISION is factually correct: `grep` of §4
(`phase1_proposal.md` lines 86–176) for "constraint-3," "NETD," or
"Idealization" returns nothing across P1–P6; the disclaimer appears only
once in §3 and once, at the very end, in §6 Idealization 7 — exactly the
asymmetric-carry shape the Iteration-65 CHECKPOINT's own mandatory
dual-section-banner rule exists to prevent, in exactly the document type
(a T28 committed-predictions document) that rule targets. I rule on the
harder question this raises — whether this is a fifth instance of the
lineage that fired Checkpoint 4 at Iteration 65 — in §3, separately,
since it deserves reasoning through explicitly rather than folded into
this line item.

## 2. Compounding finding: P2 and P5 should be demoted, not merely reworded

Both EM's and QUANTUM's attacks land, independently verified above, and
they compound rather than merely coexist. EM shows P2's null hypothesis
is not a credible alternate world given the mechanism; QUANTUM shows
P5's stated falsifier is mathematically unreachable given P1. Read
together: **neither P2 nor P5, as specified, is capable of returning a
result other than the one already guaranteed by facts already on this
program's record** (the margin–`frac_p_abs`/`ratio_k` mechanistic link
established by exp-089's own decomposition, and the tie-free total order
established by P1 itself). That is a stronger, joint conclusion than
either critique states alone: this is not "P2 is weaker evidence than
claimed" and, separately, "P5 is weaker evidence than claimed" — it is
that this proposal's own two "falsifiable predictions" beyond the core
zone (P3) and fit (P4) do not, as a matched pair, supply any information
a reader does not already have from P1 and R13/exp-089's own prior
record. Per the assignment's own instruction, I recommend explicitly:
**P2 and P5 should be reclassified in Phase 3 from "falsifiable
predictions" to "diagnostic sanity checks"** — a real methodological
correction to the proposal's own §4 scoring table, not a wording nit.
Concretely: P3 (the zone) and P4 (Firth's fit, genuinely contingent —
convergence and interval membership were not algebraically guaranteed in
advance) remain the load-bearing, falsifiable deliverables; P1 remains a
legitimate precondition check; P2 and P5 should each ship with a
one-line reclassification noting they confirm internal
consistency/arithmetic correctness of the pipeline, not new evidence
about whether the margin–outcome relationship is real. This does not
touch P3's own status as a correctly-computed order statistic — it needs
neither P2 nor P5's corroboration to stand, and continues not to need it
under this correction.

## 3. VISION's disclaimer-erosion finding: ruled explicitly, not by pattern-match

**Is this a genuine fifth instance of the lineage that fired Checkpoint 4
at Iteration 65, or a distinguishable defect the way Iteration 66's own
Red Team ruled for a similarly-shaped issue?**

First, the shape comparison. Iteration 65's firing (exp-088) was: a
caveat that already exists correctly elsewhere in the SAME document
(`results.json`, and the document's own adjacent Q1/Q5/Q6 Result
paragraphs) failed to propagate into one specific prose restatement (the
Q4 Result paragraph) — an *omission* of an existing correct caveat.
Iteration 66's own Red Team explicitly distinguished a DIFFERENT defect
in exp-089 (QUANTUM's/`NOTES.md`'s own freshly-composed, affirmatively
FALSE claim — "non-artifactual," "away from any… neighborhood" — text
that was never true anywhere in the record before) as mechanistically
different from the omission lineage, and ruled it does NOT count as a
fifth instance of that specific pattern.

exp-090's defect, as VISION correctly finds it, is an *omission*, not a
freshly-composed false claim: the disclaimer is present, correctly
worded, in §3 and §6, and simply fails to propagate into §4. **This
matches the omission shape exactly — the same shape as Iterations
53/63/64/65, not exp-089's own distinguishable false-claim shape.** So on
a pure shape test, this would be the fifth instance of the recurring
lineage.

But shape alone is not the whole test this program applies. The
Iteration-65 CHECKPOINT's own ruling turned on a second, independent
fact: the fourth instance (exp-088) survived undetected through Phase 5,
into a document already treated as a settled record, before being
caught — the "known, named, ignored" shape R6–R13 exist to fire on.
exp-090's instance was caught by VISION at **Phase 2**, before Phase 3
has frozen anything, matching the standing discharge test this program
has applied consistently across every prior R-rule ("caught blind, same
cycle, before [LOGBOOK/Phase 3 freeze]" — non-firing). Instances 1–3 of
this very lineage were each, individually, non-firing for exactly this
reason before their *recurrence itself* became the basis for firing a
fourth time. I find no text anywhere in LOGBOOK.md generalizing
Iteration 65's escalated language ("required at BOTH sections… any
future T28 committed-predictions document") into an unconditional
"any future omission fires automatically" — that generalization was
explicitly declined one cycle ago (Iteration 66, for a different reason,
but the declining-to-generalize move itself is on the record) — Iteration
66's own Red Team was careful to say it found no such text before
ruling.

**Ruling: this is the same recurring omission shape, not exp-089's own
distinguishable false-claim shape — but it does not fire Checkpoint 4
this cycle, because it was caught blind, by a Phase-2 critique, before
Phase 3 freezes anything, matching this program's own standing
discharge test for every prior instance of every R-rule at first catch.**
It becomes MANDATORY (not optional) that Phase 3 actually apply the fix
— per the Iteration-65 CHECKPOINT's own text, this specific omission is
not discretionary.

**A governance observation, stated plainly and not softened**: this is
now at least the *second* consecutive T28 cycle in which a Phase-1 LEAD
drafted a committed-predictions document without the mandatory banner,
one cycle after that exact banner was made a hard, escalated requirement
specifically because per-cycle vigilance had already failed to prevent
it three times running (exp-089's own Phase-2 VISION critique caught a
near-identical gap in its own cycle, non-firing for the identical
reason). Two clean catches in a row by the review layer is not evidence
the underlying discipline is self-sustaining at the drafting stage — it
is evidence the review layer is doing exactly the job it exists to do,
while the authoring stage keeps needing it to. I recommend the Director
consider a mechanical safeguard (in the spirit of the existing
`lab/caveat_lint_config.json` enforcement for the STEPS=1400 gap) rather
than relying on a third, fourth, or fifth consecutive Phase-2 catch —
named here as a standing item for Iteration 68's board, not adjudicated
further by this audit.

## 4. Red Team's own independent attacks (not raised by any of the five blind critiques)

**RT-1. The caution zone's upper edge rests entirely on a single point
(37.2°) that the SOURCE document itself already flagged as fragile —
undisclosed here.** [`inconsistency`]

exp-089's own NOTES.md (Learned #4) states, in its own permanent record:
37.2°'s `resolved`-gate noise-floor margin (a *different* quantity from
R13's `frac_contrast` floor margin — the ordinary `|Δp_abs|/
(NOISE_MULT·box_dev_max·p_C40)` significance gate every T28 angle must
clear before entering any classification at all) is "1.046×, the
thinnest this sub-thread has ever accepted as `resolved=True`… a
felt-lucky pass, not a robust one." I independently recomputed this from
raw `box_dev`/`p_abs_w` primitives above and confirm **1.0455×** —
bit-consistent with exp-089's own figure. exp-090's `phase1_proposal.md`
cites 37.2° in Table 1 as an ordinary "C" point with no cross-reference
to this pre-existing, already-published concern anywhere in the
document.

This matters specifically because 37.2° is not just one of seven generic
data points — it **sets the zone's own upper edge** (2.1709) and is the
single most load-bearing point in the C-class for both the
non-parametric zone and Firth's fit (its `log₁₀(margin)` value anchors
the shallow end of the fitted curve). The proposal's own P5 (LOO) table
already reports what happens if 37.2° is dropped — the upper edge moves
to 3.8793, a 79% widening — but frames this as one of seven
undifferentiated, purely hypothetical stress-test scenarios. It is not:
this is the ONE scenario the record already gave concrete, independent,
pre-existing reason to take seriously, and the proposal does not
connect the two facts anywhere. If 37.2°'s own reliability is genuinely
in question (a live, unresolved concern per its own source document, not
resolved by this proposal), the zone most likely reported to a future
citation (`[1.4764, 2.1709]`) may understate the true caution region by
close to double, and Firth's `m₅₀=2.071` — which the proposal's own P4
predicts lands "in the upper half" of the zone, i.e., close to its
fragile upper edge — is the reading most exposed to this specific,
already-documented risk.

**Fix (mandatory, cheap, zero-FDTD):** disclose 37.2°'s own resolved-margin
fragility explicitly next to the zone's upper edge and `m₅₀`, and
re-frame the "drop 37.2°" LOO scenario as the operationally primary
sensitivity reading, not an undifferentiated one-of-seven.

**RT-2. The n=7 population is a curated, crossing-proximity-enriched
sample, not a representative one — "clean separation" is closer to
confirming the sampling design than discovering new structure.**
[`inconsistency`]

Of the 7 angles, only 36.0° and 41.8° (exp-087's own original,
arbitrarily-chosen 3-angle census, minus the excluded node) were not
selected because of proximity to a `delta_scene` zero-crossing. 38.4°/
38.8° were chosen explicitly as a ±0.2°/±0.4° bracket around the 38.6°
node (exp-088's own stated purpose); 37.2°/40.2°/41.4° were chosen
explicitly as "the tightest-floor-margin grid neighbor" of the three
OTHER known crossings (exp-089's own stated selection rule, §1, cited
verbatim in its own record and independently re-confirmed as the actual
selection reason by two seats at Phase 5 of that cycle). Given R13's own
established mechanism (a denominator with real, known zero-crossings
drives near-crossing angles toward large `ratio_k`), a sample built by
deliberately targeting near-crossing angles finding that near-crossing
angles have low margin and misclassify is expected by construction, not
an independent empirical discovery about margin's general predictive
power across the swept window. This is a different point from MATERIALS'
resolution attack (about grid convergence) and from EM's/QUANTUM's
attacks (about mechanical dependence between margin and the label at the
*measured* points) — this is about whether the *population itself* is
representative of "angles a future citation might apply this zone to."
A future user applying `[1.4764, 2.1709]` to an arbitrary, non-crossing-
adjacent angle would be extrapolating a selection-biased convenience
sample past its actual support.

**Fix (mandatory, cheap):** state explicitly, alongside Idealization 3,
that the n=7 population is a targeted, crossing-proximity-enriched
sample by construction, not a random or representative draw over the
31-point window — any future citation applying the zone/`m₅₀` to a
typical or arbitrarily-chosen angle should carry this caveat alongside
the article/wavelength scope already disclosed.

**RT-3. §5's rejection of a distance-to-known-crossing regressor rests
on an argued, not computed, robustness claim — an R8-shape gap.**
[`inconsistency`, R8-adjacent]

§5 argues raw angular distance to the nearest known `delta_scene`
zero-crossing is "a strictly worse, indirect, more assumption-laden
regressor for the identical underlying quantity" and "near-collinear [to
`margin`] by the mechanism just stated" — and declines to include it on
that basis. This claim is never computed. R8 (LOGBOOK's own standing
rule, adopted specifically because an *argued* independence/robustness
claim was accepted in place of an actually-computed check one cycle
before it mattered) requires exactly this kind of claim to be
independently verified by computing the alternate case, not by
re-reasoning about it, before a flagged alternative is dismissed as
redundant. This is cheap here: exp-083's own already-committed 31-point
dense sweep gives all four crossing locations to high precision at zero
marginal FDTD cost, so a single-regressor sensitivity model (`Y` vs.
`log(distance-to-nearest-known-crossing)`, in place of, not alongside,
`margin` — avoiding the legitimate small-n multi-parameter concern §5
also raises) is a ~10-line, same-shift computation that would either
corroborate or falsify the "no information gain" claim directly.

**Fix (mandatory, cheap, zero-FDTD, same-shift):** run the single-
regressor distance-to-crossing model as a sensitivity comparison against
the margin-only model and report the result, whichever way it comes out,
rather than resting the rejection on an uncomputed collinearity
argument.

## 5. Checkpoint / standing-rule check

- **Constraint 1–4 / T1**: N/A, correctly and consistently disclosed
  throughout — no misstatement found.
- **R3**: undischarged, undisclosed here (MATERIALS, upheld) — fix is
  disclosure-only; does not require gating a new FDTD run before this
  desk cycle proceeds, since the underlying spatial-resolution check is
  already independently queued (exp-089's own Next, Tier-1 item 3).
- **R13/R14**: correctly applied, correctly NOT extended to a `D`-class
  or a `frac_p_abs`-conditioned model without new data — no violation.
- **R8**: the §5 regressor-rejection argument (RT-3) is an unverified-
  argument-in-place-of-a-computed-check gap of the exact shape R8 exists
  to prevent — not yet outcome-determining (nothing currently rests on
  it being wrong), so it does not itself fire Checkpoint 4, but it is a
  real gap this docket closes before Phase 3 freezes, matching R8's own
  "affordable and not run" standard for what should not survive to a
  synthesis unaddressed.
- **Disclaimer-erosion lineage (§3, above)**: same recurring shape,
  non-firing this cycle on the standard discharge test, MANDATORY fix,
  governance concern named forward.
- **Checkpoint criterion 5** (two consecutive non-advancing cycles): does
  not apply — exp-089 was a logbook-advancing PARTIAL (a mechanistic
  decomposition, a new rule, R14), and this cycle, once corrected per the
  docket below, supplies real, usable calibration evidence (the zone, the
  fragility disclosure, the confirmed permutation/LOO reclassification) —
  logbook-advancing in its own right.
- **No LOGBOOK misstatement found**: `FLOOR=1.91744×10⁻⁴` is correctly
  cited as unchanged since exp-088, computed over exp-083's own 31-point
  window — independently reconfirmed.

## 6. Overall verdict: **PROCEED-WITH-MANDATORY-FIXES**

The core deliverable (P3, the non-parametric caution zone; P1 and P4's
genuinely contingent convergence/interval-membership claim) is sound,
independently over-verified (by three of five critiques, and again by
this audit, bit-exact at every load-bearing number), and answers Red
Team's own exp-089 ask correctly in shape. Nothing found here overturns
the zone itself. But the docket below is not cosmetic: items 4–6 change
what P2 and P5 are allowed to be cited as (evidence vs. sanity check —
"a real methodological correction," per the assignment's own framing),
and item 7 identifies a concrete, previously-undisclosed fragility in
the exact data point that sets the zone's own upper bound. None of these
require new FDTD; all are same-shift, zero-cost fixes to prose,
scoring-table labels, and one cheap sensitivity computation.

### Mandatory-fix docket (apply before Phase 3 freezes; nine items)

1. Add the mandatory dual-section carried-idealizations banner to §4,
   citing Idealizations 9/10/16 inline at P3–P6 (VISION, upheld,
   non-firing — see §3 for the shape-ruling; this is not discretionary
   per the Iteration-65 CHECKPOINT's own text).
2. Add MATERIALS' R3 spatial-resolution disclosure: the n=7
   `frac_contrast` values (especially 40.2°/41.4°, which set the zone's
   *lower* edge) have not passed a `cpl` 20→30 spatial-resolution check
   on this channel; note the already-queued check (exp-089 Next, Tier-1
   item 3) will also discharge this gap for this fit's own inputs.
3. Add THERMODYNAMICS' forward-sampling-bias disclosure: the caution
   zone governs trust in `ratio_k`'s classification label only and must
   not be used to deprioritize or exclude CAUTION-zone/sub-zone angles
   from any future denser `σ_abs(θ)` sampling design — if anything, those
   angles should be oversampled, per R14's own established
   `σ_ext(θ)`-differential concentration there.
4. Reword P2 (EM, upheld): the exact permutation test does not certify
   the margin–outcome relationship "is not a 7-point coincidence" — it
   is not exchangeable with the actual generative mechanism, since
   `margin` mechanically drives ~90% of the classification per exp-089's
   own decomposition. Either supplement with a measurement-uncertainty
   (`box_dev`-propagated) null, or reword P2 as purely descriptive.
5. Reword P5 (QUANTUM, upheld): drop the "falsifiable stress test"
   framing. Given P1 (perfect, tie-free separation, independently
   re-derived by this audit as an order-theoretic certainty), P5's own
   stated falsification condition cannot fire — report the LOO
   enumeration, if kept, as a deterministic illustration of each zone
   edge's point-sensitivity, not a pre-registered prediction.
6. Per §2 above (a real methodological correction, not a wording nit,
   consistent with the assignment's own instruction): reclassify P2 and
   P5 in Phase 3's own scoring table from "falsifiable predictions" to
   "diagnostic sanity checks." P1, P3, and P4 remain the load-bearing,
   falsifiable deliverables.
7. Disclose 37.2°'s own `resolved`-gate fragility (1.046× noise-floor
   margin — independently reconfirmed by this audit at 1.0455×, "a
   felt-lucky pass" per exp-089's own record) directly next to the
   zone's upper edge and `m₅₀`; re-frame the "drop 37.2°" LOO scenario
   (edge → 3.8793) as the operationally primary sensitivity reading, not
   an undifferentiated one-of-seven generic case (RT-1).
8. Run the zero-FDTD, same-shift distance-to-nearest-known-crossing
   single-regressor sensitivity comparison against the margin-only
   model, to verify (not merely argue) the §5 near-collinearity claim
   before it is used to dismiss the alternative regressor — an R8-shape
   gap otherwise (RT-3).
9. State explicitly, alongside Idealization 3, that the n=7 population
   is a targeted, crossing-proximity-enriched sample by construction,
   not a representative draw over the 31-point window — any future
   citation applying the zone/`m₅₀` to an arbitrary or typical angle
   should carry this caveat (RT-2).

### Standing item for the board, not part of the docket (named, not adjudicated further)

A mechanical safeguard for the recurring dual-section-banner omission
(§3's governance observation) — two consecutive Phase-1 drafts missing a
mandatory requirement, both caught only by Phase-2 review, is worth a
lint-style check rather than a third bet on vigilance.
