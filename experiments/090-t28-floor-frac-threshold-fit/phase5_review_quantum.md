# PHASE 5 — REVIEW · QUANTUM OPTICS · Panel Iteration 67 · exp-090

Fresh-context review. I have no memory of critiquing this cycle at Phase 2
(a different fresh agent wrote `phase2_critique_quantum.md`) — this is a
blind, independent re-read of the finished record, including that
document, with no access to any other seat's own Phase-5 review this
cycle.

## 0. Independent verification performed

Before writing anything below, I re-derived every load-bearing number in
`NOTES.md`'s Result section from source, using implementations distinct
from the ones already in the record where possible:

- **Table 1 / RMS / FLOOR**: recomputed `frac_contrast(θ)` for all 7
  angles plus the excluded 38.6° directly from
  `experiments/083-.../results.json::per_theta`, and `RMS[frac_contrast]`
  over the full 31-point window. Bit-exact: `RMS=0.0019174375118374476`,
  `FLOOR=1.91744×10⁻⁴`, sorted margins `1.3095(X), 1.4764(X), 2.1709(C),
  3.8793(C), 6.5889(C), 7.4946(C), 8.0187(C)` — matches `results.json`
  digit-for-digit.
- **Q4, Firth's fit — reproduced by a THIRD, structurally different
  method** (the proposal used modified-score Newton–Raphson; two Phase-2
  seats re-ran the identical algorithm independently). I instead directly
  maximized Firth's own penalized log-likelihood objective,
  `ℓ*(β) = ℓ(β) + ½·log|I(β)|`, via a derivative-free Nelder–Mead
  optimizer with no score equation, no hat matrix, no Newton step of any
  kind: **`β=(1.78058957, −5.63151968)`, `m₅₀=2.0710128064`** — agrees
  with the committed Newton–Raphson result (`m₅₀=2.071012796646712`) to
  7 significant figures. This is a materially independent confirmation:
  two different optimization philosophies (score-equation root-finding vs.
  direct penalized-likelihood maximization) landing on the same optimum to
  7 s.f. rules out a shared implementation bug as the source of agreement.
  I also wrote my own from-scratch Newton–Raphson Firth implementation
  (24 iterations, `m₅₀=2.0710127967`) as a second cross-check — three
  independent code paths, one answer.
- **Q1**: my own from-scratch `AUC`/naive-MLE check confirms `AUC=1.0`
  (no ties) and naive-MLE divergence under an independent NR loop.
- **Q2 (permutation test)**: my own exhaustive `C(7,2)=21` enumeration:
  `p=1/21=0.047619047619047616`, bit-exact.
- **Q5 (LOO jackknife)**: recomputed all 7 leave-one-out zones
  independently — bit-exact match to `results.json::q5_diagnostic_only`.
- **Q7 (37.2°'s separate resolved-gate margin)**: recomputed from raw
  `experiments/089-.../results.json::thermo`/`box_dev` primitives
  (`p_abs_w(C40,37.2°)=2.8127043563514567×10⁻¹²`,
  `p_abs_w(G40,37.2°)=2.808672836407139×10⁻¹²`,
  `box_dev_max=4.5691305539087015×10⁻⁴`): **margin=1.0456585785601518**,
  bit-exact to `results.json::q7_disclosure::recomputed_resolved_margin`
  and consistent with exp-089's own filed "1.046×."
- **Q8 (zero-crossings)**: independently re-ran linear interpolation
  between adjacent sign changes of `delta_scene(θ)` over exp-083's own
  31-point grid: `37.1272°, 38.5902°, 40.2654°, 41.4609°` — bit-exact.
- **`run_output.txt` vs `results.json`**: line-by-line consistent; no
  printed number differs from its persisted counterpart anywhere I
  checked (Q1–Q8, all fields).

**Everything reported reproduces.** This is a cleanly verified cycle at
the level of arithmetic — every finding below is about what the correctly
computed numbers license, not an error in computing them.

## 1. Was my own (a different agent's) Phase-2 critique correctly discharged?

**Yes, cleanly, in both code and prose.** `phase2_critique_quantum.md`'s
sharpest attack was that P5's leave-one-out jackknife is a deductive
tautology given P1's perfect, tie-free separation — not a falsifiable
stress test — and that its own stated falsification condition can never
fire. I re-derive that order-statistics argument myself here, independent
of trusting the prior agent's proof: given `AUC=1.0` with no ties, (a) any
subsequence of a strict total order is still a strict total order, so "no
LOO subset loses separation" is guaranteed with probability 1 for all 7
refits; (b) a min/max order statistic is unchanged by dropping any point
other than the current argmin/argmax, so 5 of 7 refits are guaranteed a
priori to leave both zone edges bit-identical, and the other 2 are
guaranteed to move to the *next* order statistic. This holds regardless
of whether the margin–outcome relationship is real physics or pure
coincidence — it is a fact about ordered sets, not a measurement.

Checking the finished record against this:

- **Red Team's Phase-2 audit** (`phase2_redteam_audit.md` §1.4) upholds
  the attack, independently re-derives the same order-statistics argument,
  and goes further — compounding it with EM's independent finding that
  P2's permutation null is also not exchangeable with the generative
  mechanism (§2), recommending both P2 *and* P5 be reclassified from
  "falsifiable predictions" to "diagnostic sanity checks."
- **Phase 3** (`phase3_synthesis.md`, disposition item 6) adopts this in
  full: "P1, P3, and P4 remain this cycle's load-bearing, falsifiable
  deliverables; P2 ... and P5 ... are retained and still computed ...
  but are no longer scored as independent evidence."
- **`run.py`** prints `[Q5, DIAGNOSTIC SANITY CHECK ONLY -- not a live
  falsification test, see NOTES.md]` immediately before the LOO loop, and
  persists `q5_diagnostic_only` (not `q5`) as the JSON key, with an
  explicit `note` field repeating the same framing.
- **`NOTES.md`** states, in both the Predictions section (Q5: "This is a
  deterministic illustration of point-sensitivity, not a live stress
  test... every one of these outcomes is an order-statistics certainty,
  not new empirical information") and the Result section (Q5: "Confirms
  QUANTUM's order-statistics argument was exactly right — this table
  contains zero bits of information beyond Q1+Q3 themselves") and again in
  Learned #2 ("Both reproduced bit-exact, exactly as algebraically
  guaranteed... neither supplied information beyond what Q1/Q3 already
  state").

I checked every occurrence of "Q5"/"P5"/"falsif*" across
`phase1_proposal.md`, `phase3_synthesis.md`, `NOTES.md`, and `run.py`
(grep, not sampling) and found **no remaining place where Q5 is described
as a live or falsifiable test** — the correction propagated completely,
including into the code's own JSON key naming, not merely the prose. This
is a clean discharge, better than several prior T28 cycles' own
disclaimer-carry-forward record (R4/R9/the Iteration-65 disclaimer-erosion
lineage) managed on the first attempt.

## 2. A genuinely new finding: Q8's "margin is empirically more robust
   than distance" claim is confounded by its own sample's construction —
   not caught anywhere in Phase 2, the Red Team audit, or Phase 3

Red Team's RT-3 (upheld, adopted as Q8) correctly applied R8's discipline
— compute the distance-to-crossing comparator instead of merely arguing
`margin`'s superiority — and the computation itself reproduces exactly as
predicted (`AUC(distance)=1.0`, distance-zone `[0.0654°,0.0728°]`, gap
ratio `1.11` vs. margin's `1.47`). **But R8's fix (compute, don't argue)
is necessary and was correctly applied; it is not, on its own, sufficient
to license the conclusion drawn from the computation** — and that second
step was never checked by anyone this cycle.

The load-bearing fact, independently confirmed by me from the source
documents: of the 7 points in this fit, **three — 37.2°, 40.2°, and
41.4° — were not selected by proximity to a crossing in general; they
were each explicitly selected by exp-089's own stated rule as "the
**tightest-floor-margin** grid neighbor" of their respective crossing**
(`experiments/089-.../phase1_proposal.md` line 23-24, quoted verbatim;
restated in exp-090's own Idealization 11). That is: for each of the
three newly-identified crossings, exp-089 chose — from the candidate grid
neighbors — specifically the one with the **smallest `margin`**. The
other four points are not similarly margin-selected: 36.0°/41.8° are
exp-087's original, arbitrary 3-angle census (unselected for any
crossing-related property), and 38.4°/38.8° are a symmetric ±0.2°/±0.4°
grid bracket around 38.6° (a *distance*-based selection, not a margin
one — confirmed by reading `experiments/088-.../phase1_proposal.md`
lines 22-24, which specifies the bracket as "established-grid neighbors
flanking 38.6° on either side," with no margin criterion mentioned).

This matters specifically because **the three margin-selected points are
exactly the three points that set the caution zone's edges**: 41.4° and
40.2° are the two `Y=1` points defining the zone's lower edge, and 37.2°
is the `Y=0` point defining the zone's upper edge. Every point that
determines `[1.4764, 2.1709]` was chosen from a menu of grid candidates
by *minimizing margin itself* — while the corresponding `distance-to-
crossing` values for those same three points were never a selection
target; they are whatever fell out passively. A selection procedure that
explicitly minimizes one candidate regressor near a decision boundary,
then asks "which regressor has better boundary-region separation, the one
I selected for, or the one I didn't?" is structurally biased toward the
one it selected for, independent of which quantity is mechanistically
more informative. This is not a claim that margin's own advantage over
distance is entirely spurious — the mechanistic argument in
`phase1_proposal.md` §5 (margin *is* the gate's own native quantity;
distance requires an extra assumption of locally-uniform slope across
four physically-distinct crossings) is sound reasoning independent of the
sampling question. But Q8's own **quantitative** claim — "roughly a
third of margin's own gap ratio," reported as measured evidence rather
than argued belief — cannot be read as an unbiased comparison between the
two regressors, because the sample it is computed on was partly built by
optimizing one of the two candidates.

I checked whether anyone in the record connects this. Red Team's own
RT-2 (upheld, adopted as Idealization 11) independently found and
disclosed the *same underlying fact* — it quotes the identical
"tightest-floor-margin grid neighbor" language — but frames the risk
narrowly, as an *extrapolation* concern ("a future user applying
`[1.4764, 2.1709]` to an arbitrary, non-crossing-adjacent angle would be
extrapolating past this sample's actual support"). That framing is
correct as far as it goes, but it never connects back to Q8's own
specific, headline comparative claim, which is the one place in this
document where the margin-selection fact is actually load-bearing for an
evidentiary conclusion rather than a scope caveat. I grepped `NOTES.md`
for any cross-reference between Idealization 11 and Q8 (Predictions item
8, Result Q8, or Learned #3) and found none — the two live as
disconnected facts in the same document. `phase2_redteam_audit.md` itself
raises RT-2 and RT-3 (Q8's own origin) as two *separate* numbered
attacks and never notes that RT-2's finding directly undercuts RT-3's own
fix. This is a different, and in my view sharper, defect than either
individually: it is not that the population is "not representative of
arbitrary angles" (Idealization 11's framing) — it is that **the specific
comparison Q8 was built to settle is confounded by exactly the same fact
Idealization 11 discloses for a different purpose**.

**Consequence for the record.** This does not overturn Q8's own
computed numbers (which reproduce exactly, and the mechanistic argument
for margin's superiority in §5 stands on independent grounds). It means
Learned #3's own framing — "computing it (Q8) produced a materially
stronger and more precise claim than arguing it did... margin carries
roughly 3× the relative safety margin" — overstates what was actually
shown. The honest reading is: margin's own gap ratio is *at least
partly* an artifact of a sample that was built by selecting for small
margin; a genuinely unbiased test of "which regressor better separates
this classification, in general" would need to be run on a sample not
selected via either candidate regressor — for instance, scoring both
`margin` and `distance-to-crossing` against `Y` on a denser or
differently-constructed angle set from exp-083's already-committed
31-point window (using the *known*, already-computed `delta_scene`/
`C40_C` values to infer what `ratio_k`/`Y` would be, zero new FDTD, if
such an extension is judged worth building) rather than the existing
margin-curated n=7. Absent that, Q8's comparative conclusion should be
downgraded from "empirically confirmed, a real measured safety margin" to
"consistent with, but not independently isolated from, the sample's own
construction" — the same downgrade in kind (not merely degree) that this
cycle's own Phase 2 correctly applied to P2 and P5, now missed for a
structurally similar reason on P8/Q8.

This is, to be clear, a genuinely new observation relative to everything
in `phase1_proposal.md`, all five Phase-2 critiques, `phase2_redteam_
audit.md`, and `phase3_synthesis.md` — I checked each document
specifically for any statement connecting the margin-based selection
rule to Q8's own comparative claim and found none. It does not rise to a
Checkpoint-4-firing defect (nothing was falsely claimed as independently
verified when it wasn't — Q8's own arithmetic is exactly right, and the
gap is a scope/interpretation question of the kind R9's own
commensurability lineage exists to catch, caught here at Phase 5, before
any further cycle cites Q8 as closed evidence). It is a real, previously
undiscovered methodological gap in this cycle's own headline secondary
finding, from exactly the discipline (statistical/methodological rigor)
this seat has repeatedly been asked to scrutinize.

## 3. Other spot-checks (no new defects found)

- **MATERIALS' R3 resolution gap** (upheld by Red Team, adopted as
  Idealization 9): correctly disclosed, correctly scoped to the two
  points (40.2°/41.4°) that set the zone's lower edge. I confirm the
  underlying concern is real and undischarged as claimed — `grep`-checked
  that no `cpl`-resolution check exists anywhere in this cycle's own
  files, matching MATERIALS' own finding.
- **VISION's dual-section banner gap** (upheld, ruled non-firing at
  Phase 2 per Red Team's explicit shape test in §3 of its audit):
  correctly fixed — I independently checked `NOTES.md`'s Predictions
  section and confirm Idealizations 6/7/13 are now cited inline at
  multiple items (Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8), not merely once at the
  top. Red Team's own reasoning distinguishing this omission from
  exp-089's own "freshly-composed false claim" shape (which fired
  Checkpoint 4) versus this cycle's "existing-caveat-fails-to-propagate"
  shape (caught blind, pre-freeze, non-firing) is sound and I find no
  reason to overturn it independently.
- **EM's permutation-null exchangeability attack and THERMODYNAMICS'
  forward-sampling-bias caution**: both correctly adopted, both correctly
  reflected in the final `NOTES.md` language (Q2's Result entry, and
  Idealization 10 respectively). No residual gap found.
- **Q7's "1.046× vs 1.0455×" note**: correctly resolved as a rounding
  display artifact, not a discrepancy — I independently confirm
  `1.0456585785601518` rounds to `1.046` at the precision printed.

## Verdict: **CONCUR** (with one Tier-0 disclosure fix required before the
next citation of Q8)

The core deliverable — the non-parametric caution zone `[1.4764,
2.1709]` and Firth's corroborating fit (`m₅₀≈2.071`) — is sound,
correctly scoped, and independently over-verified (now by at least four
parties across Phase 2/3 plus this review, using at minimum three
distinct computational methods for the Firth fit alone). The
reclassification of P2/P5 from falsifiable predictions to diagnostic
sanity checks is a genuine, correctly-executed methodological correction,
completely and consistently carried through code, JSON, and prose — my
own Phase-2 concern from this cycle is fully discharged. This is, by this
program's own recent T28-desk-cycle standard, an unusually clean review
layer: nine Phase-2 fixes adopted in full, zero overridden, every one
independently checkable and checked.

Set against that: Q8, this cycle's own second primary falsifiable
deliverable and its most novel contribution beyond exp-089's own closed
questions, rests on a comparison I find to be confounded by the very
sample-selection procedure inherited from exp-089 — a gap that both Red
Team's own RT-2 and RT-3 came within one inferential step of catching
(each independently found half of the underlying fact) without ever
connecting the two halves. This does not overturn the zone or invalidate
`margin` as the correct regressor on mechanistic grounds (§5's argument
stands independent of Q8) — it means Q8's own *quantitative* "materially
stronger... 3× the relative safety margin" claim should be downgraded to
disclosed-but-unresolved, the same treatment this cycle correctly gave
P2 and P5, applied here to a place nobody looked. I am filing this as
CONCUR rather than PARTIAL because it does not touch the zone itself (the
cycle's true primary deliverable) and requires no new FDTD or run
correction — only a same-shift disclosure, exactly the kind of cheap fix
this cycle's own docket already applied nine times over.

**Recommended Tier-0 fix (zero-FDTD, same-shift, before next citation):**
add one sentence to Idealization 11 (or a new Idealization 12) stating
explicitly that three of the seven points — including both `Y=1` points
and the point setting the zone's upper edge — were selected by a
margin-based (not distance-based) criterion, so Q8's own comparative gap-
ratio finding should be read as consistent with, not independently
isolated from, that construction; downgrade Learned #3's "materially
stronger and more precise claim" language accordingly.

## Ranked top-3 candidate directions for Iteration 68

1. **Build an unbiased margin-vs-distance regressor comparison on
   exp-083's own already-committed 31-point window** (zero new FDTD): for
   every one of the 31 angles, `frac_contrast`/`margin` and
   `distance-to-nearest-crossing` are both already computable from data on
   record; if `ratio_k`/`frac_p_abs` were also computed at a denser subset
   of that window (or even approximated/flagged as unavailable at points
   never FDTD-measured), a genuinely unselected comparison of the two
   regressors' separating power would directly resolve §2's finding above
   — either confirming margin's advantage survives on a fair sample, or
   showing it does not. This is the most direct, cheapest fix to this
   cycle's own newly-identified gap, and reuses machinery already built
   this cycle (`find_zero_crossings`, the AUC/gap-ratio scoring) verbatim.
2. **The still-overdue R3 spatial (`cpl`) resolution check** on the
   `frac_p_abs`/`ratio_k`/`frac_contrast` channel — undischarged three
   T28 cycles running (exp-088, exp-089, exp-090), directly load-bearing
   for this cycle's own zone (40.2°/41.4° set the lower edge and have
   never been resolution-checked), and already the top-ranked substantive
   item in `NOTES.md`'s own Next section. I rank it second rather than
   first only because it requires new FDTD calls where item 1 does not.
3. **A repeat or denser FDTD measurement at or near 37.2°.** This cycle's
   own Q7 disclosure gate establishes that 37.2° is simultaneously (a) the
   single point setting the caution zone's upper edge and anchoring
   Firth's shallow end, (b) a point selected specifically for having a
   tight margin (§2, above — not an independent draw), and (c) already
   on record, from exp-089's own prior cycle, as "the thinnest
   `resolved`-gate margin this sub-thread has ever accepted... a
   felt-lucky pass." Three independently-motivated reasons now converge
   on the same single angle as this sub-thread's most under-verified,
   highest-leverage data point — a denser local sample here would
   simultaneously stress-test the zone's fragile upper edge and generate
   the first non-margin-selected data point near a genuine crossing,
   partially addressing item 1's concern as a side effect.
