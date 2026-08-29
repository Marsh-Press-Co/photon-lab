# PHASE 5 — RED TEAM FINAL AUDIT · Panel Iteration 67 · exp-090

*Fresh context, zero memory of any prior cycle. Read in full: `PANEL.md`;
`LOGBOOK.md` start to end (~19,800 lines) — R1–R14 in the RULED OUT
registry, the ESTABLISHED section, and LIVE THREADS T1–T28, with T28's
complete history from its Iteration-46 opening through Iteration 66/
exp-089, both CHECKPOINT entries (Iteration 61/exp-084, Iteration 65/
exp-088) read in full; the complete exp-090 record (`phase1_proposal.md`,
all five Phase-2 critiques, `phase2_redteam_audit.md`, `phase3_synthesis.md`,
`NOTES.md`, `run.py`, `run_output.txt`, `results.json`); all six blind
Phase-5 reviews; and exp-087/088/089's `NOTES.md`/`results.json` for the
source data this cycle reuses. Every load-bearing number below was
independently re-derived by me from raw primitives or by executing the
committed code myself — not trusted from any seat's prior verification,
including this cycle's own Phase-2 Red Team audit.*

## 0. Independent re-verification performed (raw primitives, not trusted prose)

Before adjudicating anything, I recomputed, myself, from scratch:

- **All 7 `frac_contrast`/`margin`/`ratio_k` triples and `FLOOR`/`RMS`**,
  loading `experiments/083-.../results.json::per_theta` directly and
  applying `frac_contrast(θ)=|delta_scene(θ)|/|C40_C(θ)|` at all 31 grid
  points: `RMS=1.9174375118374476×10⁻³`, `FLOOR=1.91744×10⁻⁴`; margins
  `36.0°→3.87928, 37.2°→2.17095, 38.4°→7.49463, 38.8°→8.01866,
  40.2°→1.47639, 41.4°→1.30954, 41.8°→6.58890` — bit-exact to Table 1.
  Zone `[max{margin:Y=1}, min{margin:Y=0}] = [1.4764, 2.1709]` follows.
- **The four `delta_scene(θ)` zero-crossings**, by linear interpolation on
  the raw `thetas`/`delta_scene` arrays: `37.127246°, 38.590230°,
  40.265420°, 41.460901°` — bit-exact to Q8.
- **Q1's naive-MLE trace**, re-executing `run.py::naive_mle_diverges`
  verbatim: the blowup guard (`|β|>100`) fires and returns at loop index
  `it=10` — i.e. after **11** Newton–Raphson steps, `β=(26.11462482,
  −103.01357742)` — bit-exact to `results.json::q1`.
- **The Q6 out-of-sample score**: `margin(38.6°)=0.386457`,
  `P(Y=1)=0.983791` under the committed Firth `β` — bit-exact to Q6.
- **Both candidate Q8 ratio readings** (see §2, below):
  `gap_ratio_margin/gap_ratio_distance = 1.32222`; `(margin excess)/(distance
  excess) = 0.470445/0.112107 = 4.19638`.

Everything scored (Q1, Q3, Q4, Q6, Q8's raw numbers) reproduces exactly. No
arithmetic dispute exists anywhere in this cycle's own numbers. This
confirms the same floor five Phase-2 critiques, the Phase-2 Red Team audit,
the Director, and all six Phase-5 seats already found — I add an
independent confirmation rather than a correction on any scored quantity.

## 1. Adjudication of the four assigned findings

### 1.1 MATERIALS — the naive-MLE narrative and the `phase3_synthesis.md` beta discrepancy — **UPHOLD, and extended**

**Independently confirmed, from the code itself, not from any seat's
account of it.** I ran `naive_mle_diverges(X, Y)` exactly as committed:
it exits **inside the loop**, the first time `np.max(np.abs(beta)) >
blowup` (`blowup=100.0`) — at loop index 10 (0-based), i.e. after **11**
Newton–Raphson steps, producing `β=(26.11462482, −103.01357742)` bit-exact
to `results.json`. `NOTES.md`'s Result section states this happened
*"after 2000 Newton–Raphson steps, still climbing"* — this does not
describe the committed function's behavior in any sense: the function
never approaches 2000 iterations on this data, and "still climbing" (an
open-ended, ongoing process) misdescribes a hard, deterministic exit that
fires at step 11 of a possible 2000. MATERIALS' Phase-5 finding is
correct in every particular.

**On `phase3_synthesis.md`'s own cited `β≈(65.0,−256.8)`**: I confirm this
does **not** reproduce from the committed `naive_mle_diverges` function
under any blowup threshold I tested that would let the loop run past
step 11, and I went one step further than MATERIALS' review to
characterize *why*. Running the identical loop structure (gradient check,
then Newton step, then blowup check) with the blowup threshold raised to
1,000 or removed entirely, the loop does **not** run to iteration 2000 —
it exits via the **gradient-underflow branch** (`np.max(np.abs(grad)) <
1e-10`, which `naive_mle_diverges` labels **`diverged=False`**, i.e.
"converged") at iteration 24, landing at **exactly** `β=(65.02117314,
−256.81786153)` — matching `phase3_synthesis.md`'s cited figure to the
printed precision. Two things follow, neither previously stated in the
record: (a) a script sharing this exact structure with a looser or absent
blowup guard would have reported this data point as **converged**, not
diverging — the opposite of `phase3_synthesis.md`'s own framing ("diverges
as predicted... and climbing"); (b) a genuinely unconstrained Newton–Raphson
loop with *no* gradient-underflow exit at all (which is what "2000 steps,
still climbing" literally describes) lands at `β≈(92.9,−366.9)` after 2000
iterations, a **third**, different number again. None of the three
candidate mechanisms I tried reproduces both the cited number *and* the
cited narrative simultaneously. **Ruling: MATERIALS' finding is UPHELD
without qualification, and the discrepancy is real, load-bearing enough to
name precisely (not merely "a different divergence criterion"), though
non-blocking** — Q1 is explicitly a diagnostic, not a scored, falsifiable
prediction (`phase3_synthesis.md`'s own frozen spec, item 2), so nothing
in Q3/Q4/Q8 or the Combined Verdict depends on it. This is squarely the
R4 lineage's own shape (a descriptive claim about a computation's mechanics
that does not reproduce from the code sitting next to it), caught here for
the first time by a Phase-5 seat after passing eight prior verification
passes (proposal, five critiques, Red Team's Phase-2 audit, the Director's
own pre-freeze check) unexamined — worth naming as such in the fix, not
softened to a "rounding difference" the way Q7's own genuinely benign
1.0455/1.045659 discrepancy correctly was.

### 1.2 ELECTROMAGNETISM — the "roughly a third"/"roughly 3×" characterization of Q8's gap-ratio comparison — **UPHOLD**

Independently computed both candidate ratios from the committed numbers
(`gap_ratio_margin=1.4704450941323812`, `gap_ratio_distance=
1.1121073393138168`, `zone=[1.4763877483857824, 2.170947121651026]`,
`distance_zone=[0.06541960, 0.07275362]`):

- **Ratio of the two `gap_ratio` values** (the literal reading of "margin's
  own gap ratio" vs. "distance's own gap ratio"): `1.470445/1.112107 =
  1.32222` — margin's gap ratio is about **1.32×** distance's, not 3×, and
  distance is **75.6%** of margin's, not "roughly a third."
- **Ratio of each zone's own excess-over-1.0 (`(hi−lo)/lo`)** — the
  "relative safety margin" reading, and the one Q3's own `width/lo`
  convention (`47.0% of the lower edge`) already uses elsewhere in this
  same document: margin's excess is `47.04%`, distance's is `11.21%`,
  ratio **4.19638** — closer to "roughly 4×" than "roughly 3×," and still
  not the figure quoted.

**Neither natural reading supports "roughly a third"/"roughly 3×."**
Ruling: the document (`NOTES.md`, `phase1_proposal.md` §5 hindsight-note,
`phase3_synthesis.md`) should **drop the round-number multiplicative
claim entirely and cite the two raw numbers** (`1.11` vs. `1.47`,
optionally with `47.0%` vs. `11.2%` excess) — exactly what `run.py`'s own
printed output already does correctly, and exactly the fix EM's own
review recommends. I do not adopt "state the precise 1.32× or 4.20×
figure" as an equally-good alternative to dropping the approximation: this
program's own T16 "24×" saga (R9) is the standing lesson that a
single named multiplicative factor invites exactly the kind of restatement
risk that caused that error to propagate for a full cycle — the raw pair
of numbers is the more durable citation. This does not change any
classification (margin is more robust than distance under both precise
readings) and is non-blocking, but it is a real, avoidable imprecision in
a document held to R9's own standard everywhere else.

### 1.3 QUANTUM OPTICS — Q8's sample-selection confound — **UPHOLD**

Independently verified against exp-089's and exp-088's own committed
`phase1_proposal.md` text, not merely against QUANTUM's paraphrase:

- `experiments/089-.../phase1_proposal.md` lines 23–24, quoted exactly:
  *"This proposal picks θ = {37.2°, 40.2°, 41.4°} — **the tightest-floor-
  margin grid neighbor** of each remaining zero-crossing..."* — confirming
  these three angles were selected by minimizing `margin` among candidate
  grid points, not by any distance-only criterion.
- `experiments/088-.../phase1_proposal.md` lines 22–24 specify 38.4°/38.8°
  as *"the established-grid neighbors flanking 38.6° on either side"* — a
  symmetric ±0.2°/±0.4° distance bracket, with no margin criterion
  mentioned.
- 36.0°/41.8° are exp-087's original three-angle census, unselected for
  any crossing-related property.

So of the 7 points: **3 (37.2°, 40.2°, 41.4°) were explicitly selected by
minimizing `margin`** among grid candidates near each of the three newer
crossings; 2 (38.4°/38.8°) were selected by *distance* to the founding
node; 2 (36.0°/41.8°) were unselected. The three margin-selected points
are **exactly** the three points that set the caution zone's edges: both
`Y=1` points (40.2°, 41.4°, the zone's lower edge) and the `Y=0` point
(37.2°, the zone's upper edge). A procedure that explicitly minimizes one
candidate regressor near a decision boundary, then compares that
regressor's own boundary-region tightness against an un-optimized
alternative, is structurally biased toward the regressor it optimized for
— independent of which quantity is mechanistically more informative.
This is a different, and more specific, fact than Red Team's own Phase-2
RT-2 (which frames the same underlying selection rule as an
*extrapolation* risk for future arbitrary-angle citations) — I confirm
QUANTUM's own observation that RT-2 and RT-3 (Q8's own origin) are each
independently on the record, cited as two *separate* numbered attacks in
`phase2_redteam_audit.md`, and neither cross-references the other; the
connection between "the sample was margin-curated" and "therefore Q8's
own comparative claim about margin vs. distance is confounded" is
genuinely new at this cycle's Phase 5, not raised at Phase 1, any of the
five Phase-2 critiques, the Phase-2 Red Team audit, or Phase 3.

**Ruling: Q8's quantitative claim needs to be downgraded**, from
"empirically confirmed — margin is the measurably more robust regressor by
a real, measured safety margin" to **"consistent with, but not
independently isolated from, this sample's own margin-based construction"
— the qualitative, mechanistic argument in §5 (margin is the gate's own
native quantity; a simple zero's local slope is not uniform across the
four crossings, independently confirmed by both EM's and PHOTONICS' own
Phase-5 reviews, below) stands on its own, construction-independent
grounds and is unaffected; only the *quantitative* "measured 1.3–4×
safety margin" claim is confounded and should be so labeled.** This does
not reach Checkpoint-4 territory (nothing was falsely claimed as
independently verified when it was not — the arithmetic is exactly
right; this is a scope/interpretation gap of the R9/R8 commensurability-
and-independence family, caught here, before any further citation of Q8
as closed evidence).

### 1.4 VISION SCIENCE — the Result-section banner narrower than the Predictions-section per-item citations — **UPHOLD the fact; PARTIAL, not full, agreement on its severity**

Verified directly against the committed `NOTES.md` text (not against any
seat's restatement of it):

- Predictions section, per-item citations, verbatim: Q1/Q2/Q4/Q5/Q6/Q8
  each cite `"Idealizations 6/7/13"`; **Q3 additionally cites `"9-11"`**;
  **Q7 additionally cites `"9"`**.
- Result section's own banner (stated once, governing "every finding
  below"): `"Idealizations 6/7/13"` **only** — grepping the entire Result
  section for `"9"`, `"10"`, `"11"` as idealization citations returns
  nothing; Q3's and Q7's own Result bullets carry no per-item citation at
  all.

The fact is exactly as VISION states it. **On severity, I rule closer to
MATERIALS' own framing (§3 of its review) than to VISION's own**: the
Iteration-65 CHECKPOINT's escalated, non-discretionary requirement was
that the *carried-idealizations banner* — the mandatory NETD-is-not-a-
human-eye-threshold / constraint-1–4-not-tested / `FLOOR`/`RMS`-scope
disclaimer (Idealizations 6/7/13) — appear at **both** the Predictions
and Result sections of a T28 committed-predictions document, precisely
because a prior cycle's own version of that *specific* mandatory
disclaimer failed to propagate into one prose restatement. That specific,
mandatory disclaimer **is** present, correctly, in both sections here —
the letter of the escalated rule is satisfied. What is missing is a
narrower, second-order layer: this cycle's own *supplementary*,
self-invented per-item convention of also restating the cycle-specific
Idealizations (9, 10, 11) beside each Predictions-section item, which
this cycle chose to do in the Predictions section but did not carry
through to the Result section's own bullets. This is a real omission,
correctly caught, and it does sit inside the same general family of
"a caveat that exists correctly in one place fails to propagate to its
parallel restatement" — but it is not a failure of the *specific*
disclaimer the escalated rule exists to protect.

**Checkpoint-4 relevance, ruled explicitly, applying this program's own
shape-and-discharge test as prior audits have (§7 of this document
elaborates the general Checkpoint-4 ruling; this subsection states the
result for this specific finding):** I rule this is **a lesser,
same-shift fix, not a fresh (would-be sixth) instance of the specific
disclaimer-erosion lineage that fired Checkpoint 4 at Iteration 65** —
for two independent reasons, either of which is sufficient on its own:
(1) the mandatory disclaimer itself (6/7/13) did not fail to propagate;
only a supplementary, cycle-local convention around it did, a materially
narrower defect than Iterations 63/64/65's own core-disclaimer omissions;
and (2), even read as a further instance of the general lineage, it was
caught blind, by a Phase-5 seat, before any LOGBOOK entry for this cycle
exists — the ordinary discharge test this program has applied to every
first catch of every R-rule, and the one Iteration 66's own Red Team
confirmed does not carry an unconditional "fires automatically"
extension beyond the specific fourth instance it was written for. VISION
herself reaches the same non-firing conclusion (by the second route
alone); I additionally credit the first, milder-shape route, which
MATERIALS' own review named independently and which I find the more
precise characterization of what actually happened here.

## 2. Adjudication of the six Phase-5 reviews, item by item

### 2.1 MATERIALS (verdict: CONCUR-WITH-GAP)

- Naive-MLE narrative gap (§1, above): **UPHOLD**, extended (§1.1).
- §3, the R3 spatial-resolution disclosure's own carry-forward softness
  (Q3's Result bullet lacks the Idealization-9/10/11 per-item citation the
  Predictions section gives it): **UPHOLD** — this is the same fact
  VISION's own Phase-5 review independently found and elevated to its
  headline finding; MATERIALS found it first, in passing, and correctly
  declined to treat it as a fresh disclaimer-erosion instance. I concur
  with MATERIALS' own milder characterization over VISION's harsher one
  (§1.4, above).
- §4, the new connective finding (the caution zone's own *support* — the
  angles informing it — is drawn entirely from the neighborhood of a
  `PAD`-echo domain-geometry artifact, not a material-absorption feature,
  per this program's own established Iteration-59 "zero realizability
  content" rule): **UPHOLD**. I independently confirm all four Q8
  crossings sit on the `C40`/`G40` config pair exp-076 proved lossless-
  vacuum, and I find this genuinely sharpens Idealization 11 for any
  future `FLOOR_FRAC` recalibration, as MATERIALS claims.
- §5, the "SIXTEEN consecutive cycles" arithmetic drift (should be
  fifteen inclusive, `090−076+1=15`, tracing to a one-count jump that
  entered at Iteration 65/exp-088's own "FOURTEEN...076-088" — should have
  been "THIRTEEN"): **UPHOLD, independently reconfirmed.** I recomputed
  the inclusive count myself (`090-076+1=15`) and traced the jump to the
  same Iteration-65 citation MATERIALS names. Trivial, non-scoring, but a
  real, three-cycle-old instance of the "restated, not recomputed" pattern
  R4's addenda target.

### 2.2 ELECTROMAGNETISM (verdict: CONCUR)

- The exchangeability discharge check (§2 of its review, re-verifying
  that Phase 3 correctly demoted Q2/Q5 in code, JSON, and prose, not just
  argument): **UPHOLD**. I independently grepped `run.py`, `results.json`,
  and `NOTES.md` and confirm the same completeness EM reports — the
  demotion reaches every layer.
- §3(a), the physical-mechanism finding (the four crossings' own local
  slopes differ by ~1.83×, explaining *why* margin outperforms distance,
  not merely *that* it does): **UPHOLD**. I note this is independently,
  convergently reproduced by PHOTONICS' own self-review via a different
  computation (`margin/distance` at the nearest sampled angle to each
  crossing, ratio of steepest/shallowest ≈1.83×) — two seats, two methods,
  same physical finding. Worth stating together in any future citation, as
  both reviews separately suggest.
- §3(b), the ratio-language imprecision (Q8's "roughly a third"/"roughly
  3×"): **UPHOLD**, addressed fully at §1.2, above, with my own
  independent computation matching EM's exactly (1.32222 and 4.19638).
- §4, passivity/reciprocity bookkeeping: **UPHOLD** (correctly N/A, no new
  field physics this cycle; I find no smuggled sign or normalization
  defect either).

### 2.3 THERMODYNAMICS (verdict: CONCUR-with-PARTIAL)

- Five independent recomputations (Table 1/zone, Q7, Q8, Q4, and a full
  `run.py` re-execution showing zero `git diff`): **UPHOLD**, all
  independently reconfirmed by me from the same raw sources.
- The Idealization-10 adoption check (was THERMODYNAMICS' own Phase-2
  forward-sampling-bias caution adopted with adequate force?): **UPHOLD**
  — I independently confirm Idealization 10's wording is present, strong,
  and correctly attributes the mechanism to R14.
- The Q7 "1.0455 vs. 1.045659" mechanism refinement (traces to
  intermediate-value rounding in two independent by-hand checks, not
  final-answer round-half-up as `phase3_synthesis.md`'s own text states):
  **UPHOLD**. Genuinely minor, correctly labeled non-load-bearing by
  THERMODYNAMICS itself; I find no reason to elevate it further. Folded
  into the fix docket below as a small correction to
  `phase3_synthesis.md`'s own stated mechanism, not a new finding.

### 2.4 QUANTUM OPTICS (verdict: CONCUR, one Tier-0 fix required)

- The order-statistics re-derivation of its own prior-cycle Phase-2
  attack on Q5 (a min/max order statistic is invariant to dropping any
  point but the current argmin/argmax): **UPHOLD**, and I confirm the
  same deduction independently.
- The Q8 sample-selection confound (§2 of its review): **UPHOLD**, in
  full, at §1.3 above.
- Other spot-checks (R3 gap disclosure, VISION's banner-Phase-2 gap, EM's
  exchangeability attack, THERMODYNAMICS' sampling-bias caution, the Q7
  rounding note): **UPHOLD**, no residual gap found by me either.

### 2.5 VISION SCIENCE (verdict: PARTIAL)

- The docket-by-docket verification of all nine Red Team Phase-2
  mandatory-fix items landing in the committed record: **UPHOLD** — I
  independently spot-checked items 1, 6, 7, and 8 against the file and
  find no daylight between the docket and the delivered text, matching
  VISION's own table.
- The "1.046× thinnest-ever" superlative provenance trace (correctly
  attributed to exp-089, not invented or inflated by exp-090): **UPHOLD**.
- The Result-section banner-scope finding (§2 of its review): **UPHOLD
  the fact; PARTIAL agreement on severity/shape**, per §1.4, above — I
  side with MATERIALS' milder characterization on shape while agreeing
  with VISION's own non-firing conclusion on outcome.
- The governance observation (a third distinct catch of the banner-
  carry-forward mechanism inside two consecutive T28 cycles): **UPHOLD**
  — accurate, and I add my own independent count in §7, below.

### 2.6 PHOTONICS (self-review; verdict: CONCUR)

- §1, independent reproduction of `margin`, gap ratios, `m50`, and Q7:
  **UPHOLD**, all bit-exact to my own recomputation.
- §2, the nine-item docket-application table: **UPHOLD**, matches my own
  and VISION's independent checks.
- §3a, the crossing-slope-spread finding: **UPHOLD**, and cross-confirmed
  against EM's own independent finding, per §2.2, above — genuine
  convergent discovery, not a coincidence of restatement.
- §3b (far-from-crossing points behave as a bounded oscillation, not a
  runaway linear extrapolation, and §5's argument is correctly scoped to
  avoid over-claiming there) and §3c (two independent fragility signals
  co-locate at 37.2°, worth naming together): **UPHOLD**, both correct
  and non-blocking. I find PHOTONICS' own self-review — required by this
  program's convention when the Phase-1 lead reviews at Phase 5 — was
  conducted with the same rigor as every other seat's, including finding
  a genuinely new (if minor) result about its own proposal's underlying
  physics, not merely certifying its own prior work.

## 3. Independent Red Team attacks (not raised by any of the six Phase-5 seats)

**RT-1 [inconsistency]. `phase3_synthesis.md`'s own §"Q7's 1.046× vs
1.0455× note" text is itself imprecise about the true quantity —
labeled a non-issue by three parties (THERMODYNAMICS, and this cycle's
own Q7 disclosure), correctly, but the precision claim inside the
"non-discrepancy" explanation is not exactly right.** Already addressed
above (§2.3) as THERMODYNAMICS' own finding, upheld — recorded here only
to note I independently verified the refined mechanism (intermediate-
value rounding in the by-hand check) reproduces: manually rounding
`box_dev_max` to `4.569×10⁻⁴` and `p_abs_w(C40)` to `2.8127×10⁻¹²`
*before* multiplying and dividing reproduces a result in the `1.0455–
1.0456` range depending on exactly where the intermediate rounding lands
— consistent with THERMODYNAMICS' account, not with `phase3_synthesis.md`'s
own "round-half-up on the final answer" explanation. Fold into the fix
docket (item 7, below) rather than treating as a fresh finding, since
THERMODYNAMICS already surfaced the substance.

**RT-2 [inconsistency, methodological]. The reconciling explanation this
document should carry for the `β≈(65.0,−256.8)` figure is more precise
than "used a different, uncommitted divergence check" — it should name
that the figure is best explained by an early, mislabeled "converged"
exit, not a slow climb.** Detailed in full at §1.1. This is my own
addition beyond MATERIALS' own (correct, but less specific) finding, and
I fold the precise mechanism into the fix docket (item 2, below) so a
future reader does not need to re-derive it.

**RT-3 [informational, non-blocking]. A structural observation on Q4's
own reported iteration counts (20 in `run.py`/`NOTES.md`, 19 in two
Phase-2 critiques and `phase2_redteam_audit.md`).** I confirm this
1-iteration spread is exactly what `phase3_synthesis.md` already says it
is — implementation-detail noise in exactly where a `‖Δβ‖_∞<10⁻¹⁰`
tolerance check is evaluated relative to the step that satisfies it — by
re-running the committed `firth_logistic` function myself and separately
re-implementing a version that checks the tolerance one half-step earlier;
both land on `β` matching to 8 significant figures with only the reported
iteration count differing by one. No fix needed; noted only because the
assignment asks for independent re-verification of load-bearing numbers
and I want the record to show this specific harmless discrepancy was
checked, not merely asserted harmless.

**RT-4 [informational, non-blocking]. Q8's own "empirically more robust"
finding and QUANTUM's own confound (§1.3) point toward a specific,
already-available, zero-cost closing test that no seat's own ranked list
states as a *falsifiable pre-registration*, only as a general direction.**
QUANTUM's own #1 pick (build an unbiased margin-vs-distance comparison on
exp-083's full 31-point window) is the right instrument, but as currently
scoped by QUANTUM it does not have a `ratio_k`/`Y` label at most of the
31 points (only 7 are FDTD-measured) — so it can only compare `AUC`/zone
tightness on the 5 continuous-valued channels or hunt for an alternate
labeling proxy, not repeat this cycle's exact classification test at
larger n. This is not a defect in QUANTUM's own finding, which is correct
as a directional next step, but a scoping gap in how it would actually be
executed. I recommend, as the concrete next-step specification: (a) score
both `margin` and `distance-to-crossing` as continuous predictors of the
*already-computed, continuous* `delta_scene(θ)`-sign or `C40_C(θ)`-window
membership at all 31 points (a proxy label available with zero new FDTD),
as a bridge test, while (b) treating an actual FDTD-labeled 31-point
`ratio_k` build as the only test that can fully resolve the confound —
folded into the Iteration-68 ranking below.

## 4. Combined Verdict

**PARTIAL.**

The core deliverable — the non-parametric caution zone `[1.4764, 2.1709]`
and Firth's corroborating fit (`m₅₀≈2.071`) — is sound, correctly scoped,
methodologically careful (the demotion of P2/P5 from falsifiable evidence
to diagnostic sanity checks is a genuine, completely-executed
methodological correction reaching code, not just prose), and now
independently reproduced by at least nine parties across Phase 1, five
Phase-2 critiques, the Phase-2 Red Team audit, the Director, six Phase-5
seats, and this final audit — an unusually deep verification stack. This
is not RULED OUT (no mechanism-class claim anywhere; T1 route N/A,
matching every T28 desk cycle since exp-069) and not PROMISING (no
constraint-metric progress claimed, correctly, by this cycle's own scope).

Set against that: this cycle's own second falsifiable deliverable, Q8, is
shown at Phase 5 (by QUANTUM, independently confirmed by me at §1.3) to be
confounded by the very sample-selection rule inherited from exp-089 —
correct arithmetic, overstated evidentiary conclusion. A genuinely
uncaught R4-shape defect (the naive-MLE narrative and the unreconciled
`phase3_synthesis.md` beta figure) survived eight independent verification
passes before a ninth (MATERIALS' Phase-5 review) found it, and I found
its precise mechanism goes one step further than even that review states.
A real, if narrower-than-first-characterized, banner-carry-forward gap
recurred for a third time inside two cycles. None of these four findings
touches Q3 (the zone itself) or overturns anything scored — but four
independent, genuine, previously-uncaught gaps surfacing at Phase 5, on
top of the nine-item Phase-2 docket this cycle already needed, is real
information about the cycle's own record, not a clean pass. This matches
this sub-thread's own recent convention (e.g. exp-088, exp-089) of a
Combined Verdict of PARTIAL when a genuinely usable, logbook-advancing
deliverable ships alongside multiple same-shift-fixable but real defects,
none individually severe.

## 5. Tier-0 mandatory-fix docket (same-shift, before this cycle's LOGBOOK.md entry)

1. **[MATERIALS, §1.1]** Correct `NOTES.md`'s Q1 Result-section sentence.
   Replace *"after 2000 Newton–Raphson steps, still climbing"* with an
   accurate description, e.g.: *"diverges decisively: the blowup guard
   (`|β|>100`) fires after only 11 Newton–Raphson steps
   (β=(26.11,−103.01)), not a slow asymptotic climb."*

2. **[MATERIALS + RT-2, §1.1]** Add a reconciling footnote to
   `phase3_synthesis.md`'s "Director's own independent verification"
   section, stating precisely (not merely "a different divergence
   criterion"): the pre-freeze throwaway script's `β→(65.0,−256.8)` figure
   is independently confirmed reproducible from a variant of the committed
   `naive_mle_diverges` loop structure with its blowup threshold raised
   or removed — which causes the loop to exit via the **gradient-underflow
   ("converged") branch** at iteration 24, not by running to iteration
   2000 while still diverging. State explicitly that Q1 was never a
   frozen, bit-exact falsifiable prediction requiring Director/Phase-4
   agreement (unlike Q4 and Q8), so this number needed no reconciliation
   at freeze time — but the mismatch should not be left as a live,
   unexplained discrepancy in the permanent record now that it has been
   traced.

3. **[ELECTROMAGNETISM, §1.2]** Replace every occurrence of "roughly a
   third"/"roughly 3×" describing Q8's gap-ratio comparison (`NOTES.md`,
   `phase1_proposal.md` §5, `phase3_synthesis.md`, Learned #3) with the
   two raw numbers (`1.11` vs. `1.47`, i.e. `≈0.076` distance / `≈0.470`
   margin excess-over-lower-edge), reported without an approximate
   multiplicative headline factor — matching what `run.py`'s own printed
   output already does correctly and this program's own R9 precedent for
   avoiding a restated single ratio.

4. **[QUANTUM OPTICS, §1.3]** Add a new Idealization (12, or append to 11)
   stating explicitly: three of the seven points — both `Y=1` points
   (40.2°, 41.4°, the zone's lower edge) and the `Y=0` point setting the
   zone's upper edge (37.2°) — were selected by exp-089's own rule
   specifically as the tightest-floor-**margin** grid neighbor of each
   crossing, so Q8's own comparative "margin is empirically more robust"
   finding should be read as consistent with, but not independently
   isolated from, that construction. Downgrade Learned #3's "materially
   stronger and more precise claim... margin carries roughly 3× the
   relative safety margin" language to reflect this — the mechanistic
   argument in §5 (unaffected by the selection procedure) remains the
   primary basis for preferring `margin`; the *quantitative* safety-margin
   claim does not.

5. **[VISION SCIENCE, §1.4]** Widen the Result section's per-item
   citations for Q3 and Q7 to restate Idealizations 9-11 and 9
   respectively, mirroring the Predictions section's own citations —
   closing the scope gap without needing to treat this as a fresh
   disclaimer-erosion instance (see §1.4's ruling).

6. **[MATERIALS, §2.1]** Correct `NOTES.md`'s Next item 3: "SIXTEEN
   consecutive cycles deferred (076–090)" should read **FIFTEEN**
   (`090−076+1=15`); optionally note the one-count arithmetic jump that
   entered at Iteration 65/exp-088's own citation for future correction
   if that specific historical citation is ever revisited (not urgent —
   purely rhetorical, scores nothing).

7. **[THERMODYNAMICS + RT-1, §2.3]** Correct `phase3_synthesis.md`'s own
   stated mechanism for the "1.046× vs. 1.0455×" figure: the difference
   traces to rounding *intermediate* quantities before dividing (in two
   independent by-hand checks), not to a round-half-up convention applied
   to the final answer as currently stated. Non-substantive; note for
   completeness since a future citation should quote `run.py`'s own
   `1.045659×` (or exp-089's own `1.046×`), not either scratch figure.

None of the above requires new FDTD, changes any scored classification, or
touches Q3/Q4/the zone itself.

## 6. Checkpoint criterion 4 ruling

**Does NOT fire.** Applying this program's own shape-and-discharge test:

- The Phase-2-caught instance of the missing banner (VISION's Phase-2
  critique, §4 of `phase1_proposal.md` entirely lacking the mandatory
  banner) was correctly ruled non-firing by `phase2_redteam_audit.md` §3
  — caught blind, before Phase 3 froze anything, matching this program's
  standing discharge test. I find no basis to overturn that ruling.
- The Phase-5-caught instance of the narrower Result-section banner
  (VISION's Phase-5 review) does not fire, for two independent reasons
  (§1.4, above): it is a milder variant of the specific lineage that fired
  at Iteration 65 (the mandatory 6/7/13 disclaimer itself did not fail to
  propagate; only a supplementary, self-invented per-item convention did),
  and, independently, it was caught blind, before any LOGBOOK entry,
  matching the ordinary discharge test Iteration 66's own Red Team
  confirmed still governs any instance beyond the specific fourth one
  Iteration 64's text escalated.
- The naive-MLE/beta-figure discrepancy (§1.1) is a genuine, previously-
  uncaught R4-shape defect, but it is caught here, at Phase 5, before any
  LOGBOOK entry for this cycle exists, non-load-bearing (Q1 is explicitly
  diagnostic, not scored), and does not defend a false claim against a
  contradicting re-derivation the way R4's own firing precedents (e.g.
  Iteration 50) did — it is disclosed and corrected same-shift, matching
  this program's own non-firing shape.
- QUANTUM's Q8 sample-selection confound (§1.3) is a genuine gap in a
  scored, PRIMARY finding, but Q8's own arithmetic is exactly right — the
  gap is evidentiary interpretation, not a false verification claim — and
  it is caught blind, before LOGBOOK, same-shift-fixable. This is the R9/
  R8-family "caught before it became settled record" shape, not the
  "known, named, ignored" shape R6–R14 fire on.

No governance escalation is warranted beyond what Red Team's own Phase-2
audit already named: this is now a **third** distinct catch of the
banner-carry-forward mechanism inside two consecutive T28 cycles
(exp-089's own in-cycle self-catch; exp-090's own Phase-2 VISION catch;
now this Phase-5 catch) — I concur with the standing recommendation that a
mechanical lint-style safeguard (in the spirit of
`lab/caveat_lint_config.json`'s existing STEPS=1400 enforcement) be built
for Iteration 68's board rather than relying on a fourth bet on vigilance,
and I recommend it be scoped to check **per-item idealization citation
parity** between the Predictions and Result sections specifically (not
merely top-level banner presence), since that is the precise gap that
survived two rounds of otherwise-correct, good-faith application of the
existing rule.

Checkpoint criterion 2 (mechanism-class boundary): **N/A**, matching every
T28 desk/instrument cycle since exp-069 — no phenomenon-mechanism claim
anywhere in this cycle. Checkpoint criterion 5 (two consecutive
non-advancing cycles): does not apply — exp-089 was independently ruled
logbook-advancing, and this cycle supplies a real, usable calibration
result (the zone, the fragility disclosures, the corrected Q2/Q5
reclassification) in its own right.

## 7. Reconciled ranked list of top candidate directions for Iteration 68

Merging all six seats' own Phase-5 rankings (they need not agree) with my
own judgment as final arbiter:

| Rank (seat) | MATERIALS | EM | QUANTUM | VISION | PHOTONICS | THERMO |
|---|---|---|---|---|---|---|
| 1 | R3 resolution check | R3 resolution check | Unbiased margin-vs-distance rebuild | R3 resolution check | Grazing-incidence validity check | 37.2°/R3 joint remeasurement |
| 2 | Repeat/denser at 37.2° | Repeat/denser at 37.2° | R3 resolution check | Repeat/denser at 37.2° | R3 resolution check | Tier-1 σ_abs(θ) build |
| 3 | x-wall wavelength leg | R14(b) period fit | Repeat/denser at 37.2° | Grazing-incidence check | Denser sweep at all 4 crossings | Grazing-incidence check |

**Two items appear in every seat's own top three, in some form: the
still-overdue R3 spatial (`cpl` 20→30) resolution check on the
`frac_contrast`/`frac_p_abs`/`ratio_k` channel, and a repeat/denser FDTD
measurement at or near 37.2°.** Both are cheap, both are undischarged
three consecutive T28 cycles running (exp-088/089/090), and both bear
directly on the actual numerical inputs this cycle's own zone is built
from: 40.2°/41.4° (never resolution-checked, set the zone's lower edge —
also independently shown this cycle, by both EM and PHOTONICS via
different computations, to sit at the two *shallowest*-slope crossings,
meaning a fixed grid-quantization perturbation converts into the largest
relative `margin` shift there of anywhere this method touches) and 37.2°
(sets the zone's upper edge, anchors Firth's shallow end, and independently
carries this sub-thread's own thinnest-ever `resolved`-gate significance
margin — three fragility findings converging on one point, as PHOTONICS'
own §3c and VISION's own §4 both separately name).

**My own ranking, reconciling the above with §3's own new finding (RT-4):**

1. **A single, combined FDTD cycle: the R3 spatial (`cpl` 20→30)
   resolution check plus a repeat/denser, tighter-settling measurement,
   run jointly at 37.2°, 40.2°, and 41.4°** — the near-unanimous top pick
   across all six seats in one form or another (explicit #1 for
   MATERIALS/EM/VISION; explicit #2 for QUANTUM/PHOTONICS/THERMODYNAMICS,
   or folded into a combined #1 for THERMODYNAMICS). This is the single
   strongest next item: it closes the board's single oldest undischarged
   T28-desk-cycle debt (three consecutive cycles), it directly
   revalidates or revises the exact numerical inputs this cycle's own
   headline deliverable (the caution zone) rests on, and it simultaneously
   relieves 37.2°'s two independently-flagged, unrelated fragilities
   (PHOTONICS' §3c) at zero additional marginal cost beyond what was
   already queued.
2. **[Zero-cost, run first/alongside item 1]** QUANTUM's own margin-vs-
   distance rebuild, scoped per RT-4 above: score both regressors as
   continuous predictors against the already-available proxy labels
   (`delta_scene(θ)` sign, `C40_C(θ)` window membership) across the full
   31-point window before treating item 1's own new FDTD points as the
   only route to resolving Q8's confound — this is free, can run
   immediately, and would either strengthen or narrow the case for
   `margin` on an unselected sample for the first time.
3. **PHOTONICS' own grazing-incidence validity check** — still the
   single most-repeated, near-unanimous #1 item across the whole T28
   board's multi-iteration history (named explicitly #1 or #2 by three of
   six seats this cycle alone), and increasingly the actual bottleneck:
   every angle this cycle's n=7 table draws from sits in the aperture's
   own deep near-field/grazing-incidence regime, and this check would
   determine whether the entire R13/R14 floor-gate apparatus this cycle
   just refined is even being applied in a regime where its own
   underlying assumptions hold.

**Single strongest next item: item 1 above** — the combined R3
resolution + repeat measurement at 37.2°/40.2°/41.4°. It is the item
every seat converges on in some form, it is the cheapest genuine
uncertainty-reduction available for this cycle's own new deliverable, and
it is the board's single longest-standing undischarged debt now entering
its fourth consecutive cycle if deferred again.
