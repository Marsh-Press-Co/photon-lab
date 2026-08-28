# PHASE 5 — REVIEW · VISION SCIENCE · Panel Iteration 62 · exp-085

*Fresh context, blind to any other seat's current-cycle Phase-5 review. Read
in full: PANEL.md, LOGBOOK.md in full (RULED OUT R1–R10, T28 Iterations
55–61 in full, both Checkpoint entries), and the complete exp-085 record in
order (`phase1_proposal.md`, all five Phase-2 critiques, the Phase-2 Red
Team audit, `phase3_synthesis.md`, `phase4_derivation.py`,
`derivation_results.json`, `NOTES.md`). Every number below is independently
recomputed from the primitives, not taken on the document's own word.*

## 1. Scope-framing check

Confirmed correct, as it has been every T28 desk cycle since exp-069.
Nothing in `phase1_proposal.md`, `phase3_synthesis.md`, `phase4_derivation.py`,
or `NOTES.md` compares any quantity to `C_thr`, photopic/scotopic ambient, or
any adaptation/detection quantity. The Phase-2 layer's own "unsourced
witness-scene claim" flag (VISION's own critique, Attack 10) was correctly
adopted by Phase 3 (Fix 10: the flashlight-beam clause dropped from
Idealization 4). One small completeness gap, non-blocking: `NOTES.md`'s own
Idealizations section says only "Identical to `phase1_proposal.md` §5...";
it does not explicitly restate that Attack 10's clause was dropped, so a
reader of `NOTES.md` alone (the record's own summary document) would not
know that fix landed without cross-referencing `phase3_synthesis.md`. Cheap
to fix, not load-bearing. T1/Checkpoint-2 N/A stands throughout; no
constraint-3 scene is touched anywhere in this cycle.

## 2. Tracing NOTES.md's own headline back to `derivation_results.json` — three independent findings

I did not accept `NOTES.md`'s own restatement of the run. I recomputed the
underlying numbers directly from `derivation_results.json` and re-derived
`phase4_derivation.py`'s own classification logic line-by-line.

**(i) The core bimodal-reliability claim is accurate.** `frac_recovered=1.0`,
`spread=9.2587`, `rho=0.8817` (`p=5.76×10⁻¹³`) — clears STRONG COHERENT
CHIRP's own formal band exactly (`frac≥0.80 AND spread>0.50 AND |ρ|≥0.5`).
`null_sample_pass_rate=0.4` (`4/10`) is exactly reproduced from the ten
sampled sub-windows' own `circular_shift_null.fraction_meet_or_exceed`
values: HIGH (≥0.40, "unreliable") at θc={5°:0.867, 21°:0.633, 37°:0.600,
45°:0.600}; LOW ("reliable") at θc={13°:0.067, 29°:0.033, 53°:0.0, 61°:0.167,
69°:0.0, 77°:0.0} — matching `NOTES.md`'s cited "0%, 0%, 0%, 3%, 7%, 17%"
exactly. **A structural pattern `NOTES.md` reports the raw numbers for but
never names**: every one of the four HIGH/unreliable sampled windows falls
in θc∈[5°,45°]; every one of the six LOW/reliable windows either sits at the
low end (13°, 29°) or spans the *entire* sampled tail (53°, 61°, 69°, 77°) —
exactly the region driving the "enormous" spread statistic (the corrected
periods run from ~1.2° near θc=5–13° to 34.96° at θc=77°). On the sampled
evidence, the chirp's most dramatic growth (the tail) is *better*, not
worse, attested than the low/mid-θc region — the opposite emphasis from
how a reader would naturally weight "4 unreliable out of 10, scattered."
This is not a correction to `NOTES.md`'s own numbers (they're right) but a
real synthesis gap: the one sentence that would let a Phase-5/Iteration-63
reader target *where* to extend the null first (all four HIGH windows
cluster at low/mid θc) is present in the data but never written.

**(ii) A genuine, undisclosed validity gap in the `p=5.76×10⁻¹³` figure
itself — not covered by Fix 2's own reliability check at all.** Method C's
37 sub-windows are `θc±3°` (6° wide) spaced 2° apart — consecutive windows
overlap by 4° out of 6°, a 67% overlap. `spearmanr` (and its p-value) treats
the 37 `(θc, P_local)` pairs as independent draws; they manifestly are not —
adjacent sub-window fits share the large majority of their own underlying
30-plus-point angular window. A smoothly-varying local-fit sequence
produced by *any* slowly-varying artifact (not just genuine chirp) would
also present as a strongly rank-correlated, "highly significant" trend
under this test, because the windows are not independent measurements of
different regions — they are 37 heavily-overlapping views of the same
continuous curve. Fix 2's circular-shift null (per sub-window) tests
whether *each individual* local fit survives reshuffling; it says nothing
about whether the *cross-window* correlation the `ρ` statistic reports is
inflated by this overlap. `NOTES.md`'s own prose — "a highly significant
monotonic trend of local period against `θc`" — leans on this p-value as
corroborating evidence for the chirp being "coherent," without disclosing
that the significance figure itself is not a valid test of that claim at
face value. This is a genuinely new gap, distinct from anything Phase 2 or
Red Team flagged (which concerned the `center_deg` reference-angle bug,
the outcome-band MECE gaps, and per-window self-similarity — never
cross-window independence).

**(iii) A real, independently-reproducible citation error, non-load-bearing
to the verdict.** `NOTES.md` states: `rel_dev(P_wide,P_fft)=62.8%... far
past the 10% disagreement bar`. The pre-registered convention
(`phase1_proposal.md` §4, restated in `phase3_synthesis.md` Fix 4) is
`rel_dev` relative to the pair's *mean*: `|P_wide−P_fft|/mean(P_wide,P_fft)`.
Recomputed directly from `derivation_results.json` (`P_wide=3.255639...°`,
`P_fft=8.754371...°`): `|diff|/mean = 5.4987/6.0050 = 0.9157` — **91.6%**, not
62.8%. Traced to source: `phase4_derivation.py` line 405 computes
`rd_wide_fft = rel_dev(P_wide, P_fft)` using the *general-purpose* `rel_dev`
helper (`|a−b|/b`, this sub-thread's own target-comparison convention,
denominator = `P_fft` alone — `5.4987/8.7544 = 0.6281`, exactly the printed
62.8%), then prints it at line 418–419 under the label
`"rel_dev(P_wide,P_fft vs mean)"` — a label that does not match what was
computed. The actual classification-gating boolean (`disagreement`, lines
406–407) correctly uses the mean-based formula and is unaffected — this
did **not** flip `classification_b`, which is correctly "METHOD
DISAGREEMENT" either way (both 62.8% and 91.6% clear the 10% bar). But
`NOTES.md` restated a mislabeled printout figure as a "recomputed" fact
without independently re-deriving it against the definition it cites — the
exact R4/R9 shape ("reproducing the arithmetic is not the same as
confirming it answers the stated question") applied here to a print-string
label rather than a unit mismatch. Cosmetic, but should not sit uncorrected
in a permanent record.

## 3. Is NOTES.md's headline honest about the strength of evidence?

**Yes, on balance — it does not lean hard in either direction, and where it
hedges, the hedge is earned.** It leads with the literal, spec-derived label
("STRONG COHERENT CHIRP") because that is what the frozen, pre-registered
decision table outputs on the real numbers — changing that after seeing the
result would itself violate this sub-thread's own R4/R9 anti-post-hoc-patch
norm. It immediately qualifies with "contested by its own reliability
check," gives the honest 4/10-vs-6/10 breakdown with real numbers rather
than a summary adjective, and states plainly that the cycle's own stated
goal ("pin the asymptotic period... with certainty") was not achieved. It
does not oversell "STRONG COHERENT CHIRP" as settled, and it does not
undersell it into "probably just noise" either — both readings remain open,
correctly. The two gaps I found above ((ii) the overlap/non-independence
issue on the p-value, and the un-synthesized θc-clustering pattern in (i))
make the finding *more* uncertain than `NOTES.md`'s own text discloses, not
less — so if there is a directional lean at all in what actually reached
the page, it is toward slightly overstating confidence in "coherent," via
the unexamined p-value — but this is a finding my seat is adding to the
record, not one `NOTES.md` itself should be faulted for omitting: no prior
phase (Phase 2, Red Team, or Phase 3's own synthesis) named the overlapping-
window independence assumption either, so it isn't a case of an
already-known gap being suppressed.

## 4. Is Learned item 2's self-disclosure of the Fix-2-coverage gap adequate?

**Yes — genuine, not evasive.** The gap (Fix 2's downgrade rule, written
before real data existed, covers only a nominal STABLE outcome, not the new
STRONG COHERENT CHIRP cell Fix 5 added in the same synthesis) is stated
plainly, the run's own contradictory printed line
(`UNRELIABLE per Fix 2 -- CLASSIFICATION (a) = STRONG COHERENT CHIRP`) is
quoted rather than smoothed into prose, and it is explicitly named "Phase
5's first job" under "Next," with the two live readings stated evenhandedly
("probably real, spatially uneven" vs. "Fix 2's own intent requires a full
downgrade regardless of which cell is hit"). Given this program's own
house discipline — predictions/decision rules frozen before the run, no
post-hoc rule-rewriting once real numbers exist (the exact discipline R4/R9
exist to enforce) — the Director *could not* have unilaterally resolved this
after the fact without itself committing the violation the rule exists to
prevent. Deferring it to this review, with the raw numbers and the
contradiction stated in full, is the correct move, not a quiet decision to
let it slide.

**My own adjudication, since it is asked of this review**: Fix 2 was a
unanimous five-seat mandatory fix, adopted specifically because the
identical circular-shift check, applied to this same curve family one cycle
earlier, reversed a nominal SUPPORT to INCONCLUSIVE. Its evident *intent*
(not just its literal STABLE-only text) is that a comparable-to-50%
self-similarity contamination rate should discount a periodicity claim
regardless of which named cell it nominally lands in. I read the intent as
requiring a downgrade here too: report classification (a) as **"STRONG
COHERENT CHIRP, UNRELIABLE per Fix 2's own intent — not certified"**, not
as an unqualified label with a contested footnote. This does not change the
Combined Verdict (still PARTIAL either way — the underlying uncertainty is
identical), but it changes how confidently this cycle's own headline number
should be cited by any future cycle.

## Steel-man

This is the T28 sub-thread's cleanest desk cycle to date on process
discipline. Phase 1 through Red Team produced five independently-convergent
blind critiques (all five, correctly re-tallied by Red Team's own audit,
not four) plus a Red Team audit that re-derived every claim from primitives
rather than trusting citations — and every one of the seven mandatory fixes
actually *landed and functioned* in the executed code: the `center_deg`
reference-angle bug is fixed (each of the 37 sub-windows uses its own
`θc`), the mandatory circular-shift null is genuinely run on the wide curve
(3,900 exhaustive shifts, not skipped this time — directly correcting the
exact failure mode that created R10 one cycle earlier), the Hann taper is
applied to Method B, and the 4-band MECE precedence rule resolves cleanly
with no residual overlap or gap. The result is a real, informative negative
finding, honestly reported: both global instruments (A, B) collapse to
noise-scale on the wide/dense domain (R²_wide=0.013, met/exceeded by 45.4%
of its own shifts; Method B's true dominant peak sits at 140° near-DC, not
in-range) — the cheapest possible instrument answered the cycle's own
question in the negative, which is worth knowing.

## Sharpest critique

Two gaps survive independent scrutiny that neither five blind critiques,
Red Team, nor Phase 3 caught, because they sit one layer past what any of
them checked: (1) the `ρ` p-value's significance claim is invalid on its
own terms — 37 sub-window fits sampled at 2° spacing from 6°-wide windows
overlap 67% pairwise, so `spearmanr`'s independence assumption is violated,
and `NOTES.md`'s "highly significant... trend" language leans on that
invalid figure as corroboration without flagging it; (2) `NOTES.md`'s own
"62.8%" citation for `rel_dev(P_wide,P_fft)`, described as "of their mean,"
does not reproduce under that description — the true mean-based figure is
91.6% — traced to a mislabeled print statement in `phase4_derivation.py`
(the classification-gating code itself is correct; only the printed/cited
number is mislabeled). Neither defect changes any Combined Verdict, but
both are exactly the "a cited figure must independently reproduce, and
independence assumptions must be checked, not merely computed" failure
shape this program's own R4/R9 lineage exists to catch — now found one
layer deeper than either rule's prior instances.

## Verdict: **PARTIAL**

Not RULED OUT — nothing here forecloses the near-field-diffraction
mechanism-class question, and Checkpoint criterion 2 is correctly N/A (no
phenomenon-constraint claim anywhere). Not fully PROMISING — the cycle's
own stated goal (pin `P_model_a`'s asymptote) was not achieved, the
positive finding (Method C's chirp) is honestly self-flagged as only
partially certified, and I found a genuine, previously-uncaught statistical
validity gap in the one figure (`p=5.76×10⁻¹³`) doing the most work to make
the chirp read as "coherent" rather than merely "large and unresolved."

## Ranked top-3 candidate next directions (Iteration 63)

1. **Resolve the reliability contradiction properly, closing both gaps
   found in this review.** Extend the circular-shift null to all 37 Method C
   sub-windows (`NOTES.md`'s own Next item 2 — already known cheap,
   ~1 additional minute), explicitly reporting the result by θc-region given
   this review's own finding that the 10 sampled unreliable windows cluster
   at θc∈[5°,45°] while the entire sampled tail (53°–77°) reads reliable —
   test whether that clustering holds at full resolution. Simultaneously,
   re-score `ρ`'s significance with the window overlap accounted for (a
   block/effective-N correction, or re-run `spearmanr` on a
   non-overlapping subset — e.g. every 3rd sub-window, ~6° stride matching
   the window width) before citing any p-value as evidence in a permanent
   record. This is the single highest-value item: it directly answers the
   Director's own self-disclosed Fix-2 gap and closes a validity hole no
   prior phase caught.
2. **Cheap hygiene**: fix `phase4_derivation.py`'s mislabeled `rd_wide_fft`
   print statement (line 418–419) and correct `NOTES.md`'s inherited 62.8%
   citation to the true mean-based 91.6% figure. Non-blocking, but should
   not stand uncorrected now that it's found — matches this program's own
   R4 discipline.
3. **Redirect zero-FDTD leg-(a) period-search effort elsewhere.** Both
   global instruments now read as noise-scale at the wide/dense window —
   the cheapest possible test of "does a single period exist here" has been
   run and answered negatively. Further global-fit period-pinning attempts
   on this same curve have a shrinking marginal return; the queue's own
   Tier-1 items 8–9 (PHOTONICS' domain-truncation test for Anchor 2, EM's
   matrix-valued RS/Kirchhoff kernel rebuild) are the more promising
   zero/low-FDTD next moves on this sub-thread. Separately, and with equal
   weight: the joint EM/THERMO energy-interception cross-check (Iteration
   61's own Tier-2 item 11, the standing Checkpoint-4-adjacent item, now
   untouched for a cycle that — unlike exp-084 — has no structural excuse,
   since exp-083's own article-loaded scene already exists) should not be
   deferred again without the explicit reason this program's own tripwire
   history requires.
