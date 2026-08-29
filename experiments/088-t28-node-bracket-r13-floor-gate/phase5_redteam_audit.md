# PHASE 5 — RED TEAM FINAL AUDIT · exp-088 · Panel Iteration 65→66

*Fresh context. Read in full: PANEL.md; LOGBOOK.md's RULED OUT (R1–R13) in
full and LIVE THREADS/T28 in full through Iteration 64/exp-087, with close
attention to R13's own text and Iteration 64's own disclaimer-erosion
tripwire language; the complete exp-088 record (`phase1_proposal.md`, all
five Phase-2 critiques, `phase2_redteam_audit.md`, `phase3_synthesis.md`,
`NOTES.md`, `run.py`, `results.json`); all six blind Phase-5 reviews
(`phase5_review_{photonics,materials,em,thermodynamics,vision,quantum}.md`);
exp-087's `results.json`/`NOTES.md`. No FDTD run. No file other than this
one modified. Every load-bearing number below was recomputed from
`results.json`/`per_theta` primitives by independent script, not trusted
from any seat's own prose (R4/R9 discipline) — see §0.*

## 0. Independent verification performed before adjudicating anything

- **R13 floor-gate arithmetic** (RMS, FLOOR, all 5+2 margins,
  `delta_scene`'s 4 zero-crossings in [36°,42°]): recomputed from
  `experiments/083-.../results.json::per_theta` by independent script.
  `RMS=1.9174375118374476×10⁻³`, `FLOOR=1.91744×10⁻⁴`; zero-crossings
  `37.127°, 38.590°, 40.265°, 41.461°`; margins at
  36.0/38.6/41.8/38.4/38.8/40.2/41.4° = `3.879×/0.386×(fails)/6.589×/
  7.495×/8.019×/1.476×/1.310×`. **All exact matches** to every cited
  figure across the proposal, all five Phase-2 critiques, the Phase-2
  Red Team audit, and all six Phase-5 reviews. No defect.
- **`p_abs_w(C40,θ)`/`p_abs_w(G40,θ)`, both configs, all 5 angles**
  (exp-087+exp-088 combined): pulled directly from both `results.json`
  files. Confirmed **both individual curves are smooth and strictly
  monotonically increasing** across 36.0°→41.8° with no anomaly; the raw
  difference `G40−C40` **falls** from `5.403×10⁻¹⁵` (36.0°) to
  `3.815×10⁻¹⁵` (38.4°) before rising to `1.177×10⁻¹⁴`/`1.760×10⁻¹⁴`/
  `2.334×10⁻¹⁴` at 38.6°/38.8°/41.8° — exact match to QUANTUM's cited
  table, independently reproduced by script, not by re-reading their prose.
- **`frac_p_abs`/`ratio_k` at 38.4°/38.8°**: `1.30414×10⁻³`/`5.95524×10⁻³`
  and `0.90751`/`3.87325` — exact matches, `q4_predictions_check` and
  `retroactive_exp087_reclassification` fields bit-exact against
  `results.json`.
- **Resolved-margin table** (`|Δp_abs|/(NOISE_MULT·box_dev_max·p_C40)`,
  the gate `resolved[θ]` actually checks): independently recomputed from
  raw `box_dev`/`thermo` fields at all 5 angles: `36.0°=3.196×,
  38.6°=4.487×, 41.8°=10.666×, 38.4°=2.696×, 38.8°=4.224×` — exact match
  to both EM's and THERMODYNAMICS' independently-cited figures.
- **NOTES.md's own Result section, direct keyword scan** (not a
  paraphrase): grepped `NOTES.md` for `NETD|human-eye|constraint-3|
  Idealization` with line numbers. Confirmed: **the Q1 Result paragraph
  (line 275: "Idealizations 9-10"), Q5 Result paragraph (line 325:
  "Idealizations 9-10"), and Q6 Result paragraph (lines 332-333: "NETD
  is an instrument/detector threshold... constraint-3/4's human-eye
  verdict") all carry the disclaimer inline. The Q4 Result paragraph
  (lines 282–319 — the PRIMARY-metric write-up, the cycle's only
  genuinely new/surprising finding) contains ZERO occurrences of any of
  these four strings**, anywhere in its ~500-word discussion of the
  38.4° dip. Q3 (277-280) and Q7 (336-339) also carry none — but neither
  restates CONSISTENT/ENERGY-DOMINANT classification language the way
  Q1/Q4/Q5/Q6 do, so their omission is not the same defect (see §3).
- **`results.json` itself** carries `netd_disclaimer` and `scope_note`
  top-level fields plus a per-cell `netd_disclaimer` string at all four
  thermo cells, stating Idealizations 9/10 verbatim — confirming the
  disclaimer language existed and was available to be carried into Q4's
  Result prose and was not.

No arithmetic, indexing, or citation defect was found anywhere in this
cycle's own record. Every substantive finding below is a scoping/
carry-forward/completeness matter, not a wrong number — matching every
Phase-2 and Phase-5 seat's own conclusion.

## 1. Adjudication of the six Phase-5 reviews

**PHOTONICS — CONFIRM.** The "same C40/G40 differencing pair as
`delta_scene`, therefore plausibly inheriting the same periodicity"
argument is sound and independently checkable: `experiments/083-.../
run.py` line 120 confirms `delta_scene` is built on the identical pair.
The claim that this is a *better-argued* reading than treating the dip as
an unexplained artifact is fair, and the R3-meta-rule gap it names (no
independent settling spot-check *at the surprising point itself*, only at
an adjacent angle) is real and unclosed.

**MATERIALS — CONFIRM.** Independently re-traced: `graded_black_shell`'s
existing `REALIZABILITY_MEMO.md` disposition (PLAUSIBLE-not-PUBLISHED,
Iteration 29) covers bulk shell thickness/e-folding length, not the
θ-dependent absorption *profile* now under scrutiny — a genuinely
unaddressed gap, correctly distinguished from the settled realizability
question. The companion finding — this channel has *never*, in either
cycle that has used it, received a spatial-resolution (`cpl`) convergence
check, only a temporal-settling one — is independently confirmed by
re-reading Idealization 7 in both exp-087's and exp-088's own text: both
disclose STEPS-only spot-checks, neither mentions `cpl`.

**ELECTROMAGNETISM — CONFIRM**, and this is the audit's own sharpest
independent corroboration (§0): the 38.4°→38.6° step (one 0.2° grid
increment, exactly half the ±0.4° bracket radius) carries a **3.07×**
jump in `frac_p_abs` — steeper by a factor of ~2 than any other adjacent-
point ratio in the five-point record — and this is data, not argument,
that the cycle's own EM-authored bracket-width bound ("rules out only a
feature ≳0.4° wide") was correctly hedged. The independently-reproduced
resolved-margin table (38.4°=2.70×, thinnest of the five) is exact and a
genuinely new number not stated anywhere in `NOTES.md` itself.

**THERMODYNAMICS — CONFIRM.** The `p_abs_w ∝ σ_ext²·ratio_abs_ext`
Taylor decomposition was independently re-run here from the same raw
`sigma_ext_cells`/`ratio_abs_ext_raw` fields: the two-term linear
decomposition (`2·Δσ_ext/σ_ext + Δratio/ratio`) reproduces the exact
`frac_p_abs` to <0.5% relative at all 5 points, and the `σ_ext`
differential term alone bottoms out at 38.4° (0.026%, below every other
sampled angle including 36.0°'s 0.070%) while `ratio_abs_ext`'s own
config-to-config spread stays small and roughly stable throughout — this
independently and mechanistically pins the dip to the `σ_ext(θ)`
differential specifically, not to a shift in the absorption/scattering
partition. Confirmed by re-deriving the same decomposition from primitives
independently, not by trusting the table.

**VISION — CONFIRM, with one qualification.** The core claim —
Idealizations 9/10 are present in `results.json` and correctly carried
inline in Q1/Q5/Q6's Result prose but **absent from Q4's Result
paragraph, the PRIMARY metric and the cycle's sole new finding** — is
independently and exactly reproduced (§0). This is the identical shape to
the three prior LOGBOOK-recorded instances (Iteration 53/T16, Iteration
63/exp-086, Iteration 64/exp-087), now recurring a fourth time, inside the
one document that had just finished demonstrating (in its own frozen
Predictions section) that it knew how to avoid it. **Qualification, not a
retraction**: VISION's own review states the frozen Predictions section
"correctly carries Idealizations 9/10 inline at every one of Q1/Q3/Q4/
Q5/Q6" — independently re-checked (§0), this is not quite accurate: Q3's
Predictions text cites only Idealization 13 (the FLOOR/RMS
material-specificity disclaimer), not 9/10. This is a minor, non-material
inaccuracy in VISION's own verification (Q3 does not restate
CONSISTENT/ENERGY-DOMINANT classification language the way Q1/Q4/Q5/Q6
do, so its omission is not the defect the tripwire targets), and does not
weaken VISION's central, correctly-verified finding about Q4's Result
section — but it is exactly the kind of unverified "every one of..." claim
this program's own R4 discipline exists to catch, so it is recorded here
rather than silently passed over.

**QUANTUM OPTICS — CONFIRM the primary finding (§2 below); REJECT the
Secondary Note.** The numerator-hazard decomposition (§1 of their review)
is independently reproduced exactly (§0 above) — a genuine, well-argued,
newly-identified structural point. **But QUANTUM's own "Secondary note"
states: "every Q1/Q4/Q5/Q6 restatement in the committed record carries
the NETD-not-human-eye and constraint-3-not-tested disclaimers inline...
No fourth disclaimer-erosion instance found in the filed record" — this
claim is FALSE, independently and directly disproven by §0's own
keyword scan of `NOTES.md`.** QUANTUM's own review states this was
"verified directly, not assumed" — it was not; had it been, the same
direct grep performed here (and by VISION) would have found the same
absence. This is itself a real instance of the exact failure this
program's R4/R9 lineage exists to prevent: an unverified "I checked, it's
fine" claim entering a permanent Phase-5 record. It is inert this cycle
(VISION's independent, correctly-verified finding reaches this audit
regardless, and this ruling corrects the record directly, in the same
document, before any LOGBOOK entry exists) — but it is logged here,
explicitly, as a should-not-recur data point for the R4/R9 registry:
**a Phase-5 reviewer's claim that a previously-recurring defect is
absent from a specific section must cite the specific text (grep output,
line numbers, or quoted absence) it checked — a general "verified
directly" assertion is not, on this program's own standard, sufficient
to certify a negative.**

## 2. Ruling A — VISION's disclaimer-erosion finding: does Checkpoint criterion 4 fire?

**YES. Checkpoint criterion 4 FIRES.**

**The fact, independently confirmed (§0, §1):** `NOTES.md`'s Q4 Result
paragraph — the PRIMARY metric, the cycle's sole unpredicted finding, and
the section a future LOGBOOK/PLAN.md citation is most likely to quote —
carries zero inline occurrence of Idealization 9 (NETD is not a
human-eye threshold) or Idealization 10 (does not test constraint 3),
even though `results.json` itself carries the disclaimer text and even
though this cycle's own frozen Predictions section, and this cycle's own
Q1/Q5/Q6 Result paragraphs sitting immediately adjacent to Q4 in the same
document, all correctly carry it. This is the identical failure shape
named at Iteration 53 (T16), Iteration 63 (exp-086), and Iteration 64
(exp-087) — a fourth instance of a shape this program has now caught,
individually, three times running.

**The exact language gap.** Insert, at the end of the Q4 Result
paragraph (after "...this cycle's own data cannot distinguish those
readings and does not attempt to."), one sentence mirroring Q6's own
already-correct wording: *"NETD is an instrument/detector threshold, not
a human-eye one, and this finding does not bear on constraint-3/4's
human-eye verdict (Idealizations 9-10)."* This single sentence — costing
nothing, requiring no new computation — is the entire fix.

**Why this is not a discretionary weighing call, and why the ordinary
"caught blind, same cycle, before LOGBOOK" discharge pattern that closed
instances 1–3 does not apply here.** Every one of R6 through R13's own
adoption texts closes with language of the shape "fires Checkpoint
criterion 4 automatically... [if/unless] caught blind, same cycle, before
[LOGBOOK/this entry]" — and Iteration 64's own close explicitly used that
exact discharge condition for the *third* disclaimer-erosion instance:
"the third disclaimer-erosion instance, closed same-shift with a new
forward tripwire — a fourth instance fires automatically... all caught
blind, same cycle, before this entry." Read carefully, that sentence
states the discharge condition for instance 3 (caught blind, same cycle)
and then states an *unconditional* consequence for instance 4 — "a fourth
instance fires automatically" — with no discharge clause attached to it.
This is a deliberate asymmetry, not an oversight: the entire reason
Iteration 64 escalated to unconditional language for the fourth instance,
rather than simply re-stating the ordinary R6–R13 "caught blind, same
cycle" pattern a fourth time, is that a defect that gets "fixed just in
time" three times running by that exact discharge mechanism is
demonstrated, by that very recurrence, not to be reliably preventable by
per-cycle vigilance alone — the tripwire exists specifically to stop
treating each catch as a fresh non-firing case. Ruling this instance
non-firing on "it was caught blind, same cycle, before LOGBOOK, same as
the third instance" would apply the discharge test Iteration 64's own
text explicitly withheld from the fourth occurrence, collapsing the
escalation the tripwire was built to enforce back into the ordinary
pattern it was written to break out of. **This audit rules formally:
Checkpoint criterion 4 fires — a CHECKPOINT entry in LOGBOOK.md and
SESSION_LOG.md, and Marsh notified, per PANEL.md's continuous-mode
protocol**, matching the format of every prior Checkpoint-4 firing this
program has recorded (Iterations 52, 54, 61).

**This firing is procedural/program-integrity, not scientific.** No
arithmetic in Q4 is wrong, no gate was bypassed, and the underlying
`ratio_k`/`frac_p_abs` measurements at 38.4°/38.8° are sound (§1,
independently re-verified by four of six Phase-5 seats from raw
primitives). The firing is about the record's own carry-forward
discipline for a scope-limiting disclaimer, not about the validity of
the science it discloses. The Combined Verdict below is therefore not
determined by this firing; it is a separate governance flag layered on
top of a scientifically sound cycle, exactly as R11's escalation (a
"known, named, ignored" governance rule) coexisted with sound underlying
FDTD in its own founding instance.

## 3. Ruling B — QUANTUM's numerator-hazard finding: genuine, generalizable, and does it warrant a new standing rule?

**Genuine and independently confirmed (§0). Generalizable in spirit, but
mechanistically distinct from R13's own criterion — recommend a new,
sibling standing rule, not a literal R13 addendum.**

**The fact.** `frac_p_abs(θ) = |p_abs_w(G40,θ) − p_abs_w(C40,θ)| /
p_abs_w(C40,θ)` is a small difference between two independently smooth,
strictly monotonically increasing curves, divided by one of them.
Independently re-derived from raw `thermo` primitives across both
`results.json` files (§0): both `p_abs_w(C40,θ)` and `p_abs_w(G40,θ)`
rise monotonically and smoothly across all five sampled angles with no
irregularity in either curve individually; the entire non-monotonic
"dip" lives in the *difference* between them, which is itself a much
smaller quantity (`~10⁻¹⁵` vs. `~10⁻¹²` for the parent curves) riding on
top of two much larger numbers.

**Is this "the same hazard class" R13 named?** Related in spirit, but not
identical in mechanism, and the distinction matters for how any new rule
should be worded. R13's hazard is a genuine mathematical singularity:
`frac_contrast`/`delta_scene` has demonstrated, real zero-crossings, so
`ratio_k` (which *divides by* `frac_contrast`) is architecturally capable
of blowing up without bound arbitrarily close to a crossing — that is
what actually happened at 38.6° (`ratio_k=53.99`). `frac_p_abs`, by
contrast, is not a denominator anywhere in this pipeline, and its own
internal denominator (`p_abs_w(C40,θ)`) is never close to zero anywhere
in the swept window (it stays within `2.7×10⁻¹²`–`3.3×10⁻¹²` W
throughout) — so `frac_p_abs` cannot blow up the way `ratio_k` did at
38.6°. What it *can* do — and did — is swing to a small, non-monotonic
value because its own numerator is a subtractive-cancellation quantity:
two close, comparable-magnitude, independently-varying numbers, whose
difference amplifies any small relative wiggle in either parent curve
(a classic catastrophic-cancellation sensitivity, not a pole). The
observed consequence at 38.4° was a spuriously *small* `ratio_k`
reading (well inside CONSISTENT, not a misclassification this cycle) —
but the same construction could, at an unsampled angle, just as easily
produce a spuriously large or erratic single-point reading in either
direction, and nothing in the current pipeline flags or floor-gates
against that possibility the way R13 now does for the denominator side.

**Weighing PHOTONICS' and THERMODYNAMICS' explanations — these three
findings are complementary, not competing, and adjudicating them
together strengthens all three rather than leaving a three-way
conflict.** They operate at different explanatory levels and answer
different questions about the identical fact pattern:
- **QUANTUM** names the *construction-level* hazard: any ratio built as
  `|A(θ)−B(θ)|/B(θ)` where A and B are close and independently varying is
  fragile by its own mathematical shape, regardless of the underlying
  physics — this is a general, physics-agnostic caution about the
  pipeline's own arithmetic.
- **PHOTONICS** supplies the *physical reason* such a difference could
  genuinely be non-monotonic here specifically: C40 and G40 are the
  identical config pair `delta_scene` is built from, and `delta_scene`
  is independently, twice-over, null-controlled to carry a genuine
  ~2.84–2.95° period — so a shared PAD-diffraction mechanism plausibly
  imprints comparable oscillatory structure on both channels built from
  the same pair.
- **THERMODYNAMICS** supplies the *mechanistic pathway*: because
  `ratio_abs_ext` (the absorption/scattering partition) is independently
  confirmed flat/config-invariant to <0.1% at every sampled point, the
  entire fractional swing in `frac_p_abs` is forced, by that flatness, to
  live in the `σ_ext(θ)` config-differential term specifically — not a
  free-floating unexplained residual, a specific, checkable term.
Read together: QUANTUM explains *why the construction is fragile in
general*; PHOTONICS explains *why a real, non-artifactual oscillation is
physically plausible here specifically*; THERMODYNAMICS explains *exactly
where in the bookkeeping that oscillation must live, given what is
already established flat*. None of the three numeric claims disagrees
with either of the others — independently re-verified here, all three
reproduce from the identical primitives (§0) and are mutually consistent
by construction (THERMODYNAMICS' decomposition is a refinement of the
same `G40−C40` difference QUANTUM isolates; PHOTONICS' periodicity
argument supplies a candidate origin for exactly the σ_ext-differential
term THERMODYNAMICS locates).

**Ruling: warrants a new standing rule.** The founding-instance discipline
this program has applied to every rule since R5 (does not fire
retroactively on the instance that discovered it) applies here too — this
does not retroactively touch exp-088's own filed Q4/Q5 CONSISTENT
verdict, which remains correctly computed and disclosed. But the
underlying construction hazard is real, distinct from R13's specific
zero-crossing criterion, and generalizable to any future ratio-classifier
numerator built the same way. **Recommended text for the Director to
adopt, as a new rule (not a literal R13 addendum, since the triggering
condition differs — R13 requires a demonstrated or knowable real
zero-crossing; this rule's trigger is the construction shape itself, with
no zero-crossing required or claimed):**

> *A ratio classifier's own numerator, when itself constructed as a small
> difference between two independently-measured, comparable-magnitude
> quantities divided by one of them (`|A(θ)−B(θ)|/B(θ)`, A and B each
> individually smooth), must be treated with the same single-point-
> distrust R13 applies to a zero-crossing-capable denominator — even
> absent any demonstrated zero-crossing on the numerator side — before a
> single sampled angle's reading is cited as representative. Minimum
> discharge: (a) verify, as done here, that the numerator's own parent
> quantities (A and B individually) are smooth/monotonic, ruling out a
> sign-bookkeeping or registration artifact; (b) where the pipeline that
> produced A and B shares its underlying config pair or geometry with an
> already-established oscillatory confound (as here, C40/G40 also
> underlying `delta_scene`), state that shared-pair risk explicitly and
> either fit or explicitly decline to fit the established period against
> the raw signed difference `A(θ)−B(θ)`; (c) do not extrapolate a
> numerator-side reading across a span exceeding roughly half of any
> established period on the same config pair without an interior
> check denser than one point.*

## 4. Ruling C — the un-sampled node census and the bracket-width caveat: retroactively weakened, and the tripwire's shape must broaden

**Yes, retroactively weakened — by data, not merely by a forward
disclaimer that turned out to be prudent — and yes, the forward tripwire's
shape needs to broaden, not merely keep its stated urgency.**

`NOTES.md`'s own "Bracket-width bound" section states the ±0.2°/±0.4°
test "rules out only a feature ≳0.4° wide." That was written as a
theoretical hedge before Phase 4 ran. Independently re-verified here
(§0, confirming EM's Phase-5 finding): the actual 5-point record shows a
**3.07× jump in `frac_p_abs` across the single 0.2° step from 38.4° to
38.6°** — the steepest normalized slope anywhere in the record, at a
length scale *at or below* the grid step itself, i.e. inside the exact
regime the bracket-width bound disclosed it could not see. This does not
prove a genuine sub-0.4° feature exists (a periodic-inheritance
explanation, §3, remains equally live and unadjudicated by this cycle's
own data) — but it demonstrates the caveat was not merely defensive
boilerplate: the channel's own behavior, where actually sampled at fine
grid resolution, shows curvature at the scale the caveat named as
untested. This is exactly PHOTONICS' own independent point (§1 of their
review) sharpened with a concrete number.

**Consequence for the already-named forward tripwire.** The tripwire as
currently written in `NOTES.md`'s Next section targets only the
*denominator*-side census: `ratio_k` at the three other `delta_scene`
zero-crossings (≈37.1°/37.2°, 40.2°, 41.4°). That remains real and
overdue — but this cycle's own data shows a second, independent
completeness gap on the *numerator* side that the denominator-only
tripwire does not close: the two large gaps this cycle's own 5-point set
still leaves unsampled (36.0°→38.4°, a 2.4° span, and 38.8°→41.8°, a 3.0°
span) are exactly where a `frac_p_abs`-side feature — whether periodic
inheritance or a genuine narrow anomaly — would also need to be
distinguished. Four of six Phase-5 seats (PHOTONICS, EM, THERMODYNAMICS,
QUANTUM) independently converged on the same concrete remedy from four
different angles: sample 1–2 additional established-grid points inside
those two gaps (candidates converge on ≈37.0°/37.2°/37.4° and
≈40.2°/41.4°, several of which are *also* the already-named
denominator-side tripwire angles). **The forward tripwire should be
restated, before any future cycle executes it, as a single combined
angle set answering both questions at once** — not two separate future
asks — since the candidate angles substantially overlap and a single
dispatch is strictly cheaper than two.

## 5. Checkpoint criteria — explicit ruling on all five

1. **N/A.** No constraint metric passed or approached; this is T28
   instrument work.
2. **N/A**, matching every T28 desk/instrument cycle since exp-069 (T1
   route N/A, restated correctly in this cycle's own §3).
3. **N/A.** No engine-physics build beyond the validated bench classes is
   needed.
4. **FIRES** — see Ruling A (§2) above. This is the single Checkpoint-
   relevant matter this audit found. No other matter in this cycle's
   record (the numerator-hazard finding, the bracket-width empirical
   weakening, the un-validated angular-absorption-profile gap, the
   `cpl`-resolution-check gap, QUANTUM's own false Secondary Note) rises
   to a Checkpoint-4 firing: each is a newly-surfaced, first-instance
   finding, caught blind at Phase 5, correctly disclosed or correctable
   same-shift, matching this program's own non-firing precedent for a
   rule's founding/discovery instance (R5/R6/R9/R10/R11/R12/R13).
5. **N/A.** This is not a non-advancing cycle: the R13 floor gate was
   correctly specified, applied, and independently reproduced by every
   reviewing seat; exp-087's own filed classification received a
   disclosed, forward-citable correction; a genuine, unpredicted,
   honestly-reported new finding (the 38.4° dip) opened two new,
   independently-confirmed methodological questions (§3, §4) that did
   not exist on the board before this cycle ran.

## 6. Combined Verdict: PARTIAL

This cycle did what it set out to do, cheaply and correctly: R13's floor
gate is specified, applied both forward and retroactively, and
independently reproduced bit-exact by all six Phase-5 seats and this
audit; exp-087's own filed ENERGY-DOMINANT classification receives a
disclosed, non-destructive, R13-corrected CONSISTENT reading at the 5
now-sampled angles, correctly scoped as not channel-general. That is real,
logbook-advancing progress on T28's own instrument-fidelity question —
not RULED OUT (no mechanism class is foreclosed; T1 route N/A, matching
every T28 instrument cycle) and not PROMISING (no constraint-metric
progress is claimed, correctly, by this cycle's own scope).

But the cycle's own genuinely new, unpredicted finding — the 38.4° dip —
opened, rather than closed, two independently-confirmed methodological
questions that were not on the board before this cycle ran (the
numerator-hazard construction risk, §3; the empirically-demonstrated
fragility of the bracket-width bound, §4), and the cycle's own record
carries a real, confirmed, fourth instance of a program-integrity defect
this sub-thread has now failed to prevent structurally three times
running (§2). **PARTIAL** — matching this sub-thread's own recurring
convention — correctly captures a cycle that is scientifically sound and
genuinely advances the board, carries a real governance finding requiring
Marsh's attention, and leaves more open, better-characterized questions
than it closes.

## 7. Reconciled Iteration-66 queue

**Tier 0 — same-shift, zero cost, before this cycle's record is treated
as closed:**

1. **[Checkpoint-4 discharge]** Add the one-sentence Idealization 9/10
   disclaimer to `NOTES.md`'s Q4 Result paragraph, mirroring Q6's own
   wording verbatim (§2's exact text). This does not undo the firing; it
   is the fix that prevents a fifth instance and closes the letter of the
   defect going forward.
2. **[Structural, escalated from Red Team's own Phase-2 §5 recommendation
   to warranted]** Make the "carried idealizations" banner convention
   mandatory — not merely recommended — at BOTH the Predictions section
   AND the Result section of any future T28 (and, given the recurrence
   count, arguably any panel) committed-predictions document. This
   cycle is direct, first-hand proof a banner scoped only to "every
   prediction below" does not propagate to a Result section written
   after Phase 4 — exactly where the fourth instance recurred.
3. **[New standing rule]** Adopt Ruling B's recommended text (§3) as a
   new standing rule, sibling to R13, in LOGBOOK's RULED OUT registry.
4. **[R4/R9 registry note]** Log QUANTUM's own false "no fourth instance
   found" Secondary Note claim (§1) as a should-not-recur data point:
   a Phase-5 reviewer's claim that a named recurring defect is *absent*
   from a specific section must cite the specific text it checked.
5. **[Record hygiene]** File the independently-reproduced resolved-margin
   table (36.0°=3.20×, 38.6°=4.49×, 41.8°=10.67×, 38.4°=2.70°,
   38.8°=4.22×, §0) into the permanent record — currently exists only
   across two Phase-5 reviews and this audit, never in `NOTES.md` or
   `results.json` itself.

**Tier 1 — cheap FDTD, near-unanimous across the six reviews (combine
into one dispatch, per §4):**

1. **A single combined angle set answering both the denominator-side
   node census and the numerator-side gap census at once** — candidates
   converge (PHOTONICS, EM, THERMODYNAMICS, QUANTUM) on
   ≈37.0°/37.1°/37.2°/37.4° (bridges the 36.0°→38.4° gap and the
   `delta_scene` 37.127° crossing simultaneously) and 40.2°/41.4°
   (already the two other node-adjacent points, and the far side of the
   38.8°→41.8° gap). Roughly 8–16 calls depending on final angle count,
   strictly cheaper than dispatching the numerator-side and
   denominator-side questions in two separate future cycles.
2. **A tight sub-grid bracket of the 38.4°→38.6° step itself**
   (EM's/QUANTUM's proposal: 38.45°/38.5°/38.55° or similar, 2–6 calls)
   — the single cheapest, most decisive test of whether the observed
   3.07×/0.2° slope reflects a genuine sub-0.4°-scale feature or ordinary
   curvature aliased by coarse sampling.
3. **Both a temporal (STEPS) and, for the first time on this channel, a
   spatial (`cpl`) resolution check at 38.4°** (MATERIALS' and
   THERMODYNAMICS' finding: this channel has never received a spatial
   convergence check in either cycle that has used it) — R3's own
   standing meta-rule is directly triggered by a surprising feature and
   has not yet been discharged for this channel.

**Tier 2:**

- Zero-FDTD desk check: fit T28's established `P*≈2.8421–2.9474°`
  period to the signed delta `p_abs(G40,θ)−p_abs(C40,θ)` across the 5
  already-collected points (EM's item 2) — immediate, sharpens §3's
  periodicity-inheritance hypothesis before any new FDTD is spent.
- Add a disclosure (new idealization or Result-section addendum) that
  `graded_black_shell`'s angular absorption *profile* has never been
  validated against any published/plausible real material's own
  oblique-incidence response — distinct from the settled bulk-thickness
  realizability disposition (MATERIALS, §1).
- Institutionalize the FLOOR/RMS material-and-wavelength specificity
  caveat (this cycle's Idealization 13) into house convention
  documentation, not only this cycle's local disclaimer — MATERIALS'
  own Phase-2 critique named a concrete future citation risk (exp-087's
  own queued "near-null σ(I) article" extension) this does not yet
  structurally prevent.

**Tier 3 — standing, unaffected by this cycle:**

- Execute Red Team's own Iteration-65 ranking item 2 (the ~124-call
  full/denser individual-`σ_abs(C40,θ)`/`σ_abs(G40,θ)` build across the
  full 31-point window) — now doubly motivated: it is simultaneously the
  only instrument dense enough to fit a real period against both the
  numerator-side and denominator-side census questions, rather than
  merely flag them.
- PHOTONICS' grazing-incidence validity check (still near-unanimous #1
  on the whole T28 board).
- The x-wall wavelength-generality leg — now **FOURTEEN** consecutive
  cycles deferred (076–088), the single oldest item on the whole T28
  board.
- The still-queued full-scale null-calibration re-run.
- R12-into-standard-practice.
- Leg-(b) work.
- QUANTUM's lossless-PEC-only-disk control.
- Hardening `sections.py::widths()` to normalize by `abs(i_inc)`
  internally (two independent instances on record, exp-024 and exp-087).
- The ritualization governance question (Iteration 61), still unresolved.

## 8. Files consulted

`PANEL.md`; `LOGBOOK.md` (RULED OUT R1–R13 in full; LIVE THREADS/T28 in
full through Iteration 64/exp-087); `experiments/088-.../
{phase1_proposal.md, phase2_critique_{em,materials,photonics,
thermodynamics,vision}.md, phase2_redteam_audit.md, phase3_synthesis.md,
NOTES.md, run.py, results.json, phase5_review_{photonics,materials,em,
thermodynamics,vision,quantum}.md}`; `experiments/087-.../
{results.json, NOTES.md}`; `experiments/083-.../results.json`. All
recomputation performed by independent Python script against raw JSON,
not by re-reading any seat's own tables.
