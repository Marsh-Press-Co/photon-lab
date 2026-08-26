# PHASE 5 — RED TEAM FINAL AUDIT · Panel Iteration 51 · exp-074
## Adjudicating all six blind Phase-5 reviews of the 9-column fit + null-calibration test

*Fresh sub-agent, RED TEAM charter (PANEL.md: attacks every proposal,
speaks last and hardest; standard is not textbook-physics compliance — it
kills internal inconsistency, unfalsifiable claims, mechanisms
inexpressible as simulation parameters, and quiet constraint-N
violations, especially #3). Receives everything this cycle produced:
`phase1_proposal.md`, `desk_check_pricing.py`+results, all five Phase-2
critiques, `phase2_redteam_audit.md`, `phase3_synthesis.md`, `NOTES.md`,
`fit_and_calibrate.py`+results, `phase4_results.md`, and all six Phase-5
reviews (`phase5_review_{photonics,materials,thermodynamics,quantum,
vision,em}.md`). Every load-bearing claim below — including claims made
**by** the six Phase-5 reviews — was independently re-derived by invoking
or extending the actual committed code, never taken on any seat's word
(LOGBOOK R4).*

---

## 0. What I ran

1. `python3 desk_check_pricing.py` and `python3 fit_and_calibrate.py`,
   both unmodified end-to-end — bit-exact reproduction of both committed
   `results.json` files, confirming `CHECK0 pass=True worst_rel_err=
   0.00e+00` and `Combined Verdict: HALT_NULL_MISCALIBRATED_9COL`.
2. A direct count of the `detail` dictionaries in the committed
   `fit_and_calibrate_results.json` — the cell-count arithmetic check.
3. A from-scratch recomputation of every circular-shift/i.i.d.
   rejection-rate ratio, under five comparison conventions (worst-, best-,
   mean-, and fixed-σ i.i.d. comparators, plus every individual cell) —
   the ratio-range arithmetic check.
4. Independent computation of the four configs' own per-config residual
   pools (`per_config_residuals`, unmodified), their pairwise Pearson
   correlations, and their lag-1 autocorrelations.
5. An independent Monte-Carlo re-run of the circular-shift leg under
   three constructions — the as-committed independent-shift, a
   coupled-shift (`sA=sB`) counterfactual, and a matched-scale white-noise
   control (both independent- and coupled-shift variants) — using the
   script's own `sign_flip_9col_surrogates`/`circular_shift` functions.
6. A direct numerical test of the sign-flip p-value's scale-invariance
   under a 3.7× rescaling of the null data.
7. A from-scratch reproduction of the naive-Gaussian-quantile inflation
   translation QUANTUM used to quantify the `lev9_Rq` magnitude gap.
8. `git show 3aaae38 --stat` / `git show af2f381 --stat` / `git diff
   3aaae38 af2f381 -- fit_and_calibrate.py` — independent verification of
   the pre-registration ordering claim.

Every one of these reproduces the corresponding Phase-5 review's own
figures to the precision each review itself reported, with one partial
exception (§1 below) that changes an interpretation, not a verdict.

---

## 1. The four-way cross-config-correlation finding (PHOTONICS/EM/THERMODYNAMICS/QUANTUM) — CONFIRMED as fact, PARTIALLY OVERRIDDEN as mechanism, does NOT change the Combined Verdict

### 1a. The facts, independently re-verified

```
Cross-config Pearson r (raw, unshifted):  C40–C60=0.9967  C60–C70=0.9991
                                            C70–C80=0.9995  C40–C80=0.9921
Per-config lag-1 autocorrelation:          C40=0.936  C60=0.933  C70=0.926  C80=0.922
Independent-shift null std vs real, correctly-aligned std:  6.1×/21.9×/38.3×
Coupled-shift (sA=sB) null std vs real, correctly-aligned std: 0.64×/0.75×/0.89×
```

All four numbers match PHOTONICS', EM's, THERMODYNAMICS', and QUANTUM's
own independently-computed tables to the reported precision. This is a
genuine, previously-undisclosed structural fact about the calibration
machinery's own inputs, confirmed a fifth time by this audit: the four
`ABSORB` configs' own per-config carrier-fit residuals are, to within
0.05–0.8%, the *same shared curve*, and that curve is strongly
autocorrelated in θ (lag-1 ≈ 0.92–0.94). **Not in dispute; all four
seats and this audit agree.**

### 1b. Where the four seats disagree, and how I resolve it

The four seats diverge on *why* this drives the circular-shift leg's
extra severity over the i.i.d. leg — and this is not a cosmetic
disagreement, because it determines what the record should say about
whether the leg's own 38.9×–46.1× failure means anything about
`delta_ab`'s real noise process:

- **PHOTONICS**: independent shifting destroys near-total common-mode
  cancellation, manufacturing a null 6×–38× larger than real,
  correctly-aligned noise — "not a draw from genuine θ-adjacent noise in
  `delta_ab`."
- **QUANTUM** (§3b): the *same* magnitude argument, stated as "the
  direct, quantified mechanism behind the leg's 38.9×–46.1× nominal
  rejection rate."
- **THERMODYNAMICS** (§2c): ran the actual coupled-shift counterfactual
  (`sA=sB`, which *does* respect the cross-config correlation) and found
  it fails **comparably or worse** (35.9×–52.3× vs. the official
  38.9×–46.1×) — ruling out the independent-vs-coupled shift-pairing
  choice as the driver, and isolating real lag-1 autocorrelation
  (confirmed against a matched-scale white-noise control) as the actual
  cause.
- **EM** (§4): independently ran the identical coupled-shift
  counterfactual (comparable figures: 36.1/35.9/52.3× mine vs. theirs)
  and additionally proved, algebraically and numerically, that the
  sign-flip test's p-value is **exactly invariant to uniform rescaling of
  `y0`** — which directly falsifies PHOTONICS'/QUANTUM's stated
  mechanism: a null draw being 6×–38× larger in *amplitude* cannot, by
  itself, explain an elevated *rejection rate*, because rejection rate
  depends only on `y0`'s shape relative to the design, never its scale.

**I independently re-ran both the missing pieces and both hold up:**

- Coupled-shift counterfactual, my own re-derivation (K=500,
  independent seed): C40–C60 34.0×, C60–C70 34.6×, C70–C80 49.4× nominal
  at α=0.01 — matching THERMODYNAMICS' 36.1/35.9/52.3× to within
  Monte-Carlo noise at this sample size. **Confirmed: coupled-shift does
  not rescue calibration.**
- Scale-invariance, my own direct test: `p(y0) = 0.4523` vs.
  `p(3.7·y0) = 0.4519` (5000 surrogates, matched RNG state) — exact to
  Monte-Carlo precision. **Confirmed: EM's algebraic proof is correct.**

**Adjudication: PHOTONICS' and QUANTUM's shared causal claim (the
amplitude mismatch from destroyed cross-config cancellation is "the
direct, quantified mechanism" behind the leg's severity) is OVERRIDDEN,
by EM's rigorous scale-invariance proof and THERMODYNAMICS' isolate-the-
variable coupled-shift experiment, both independently reproduced here.**
The correct mechanistic story is THERMODYNAMICS'/EM's: genuine lag-1
autocorrelation (0.92–0.94) in the real per-config residuals is what
makes a sign-flip/permutation null miscalibrated here — sign-flip tests
assume exchangeability under H₀, which strongly autocorrelated errors
violate, independent of how the two series being differenced are
recombined. The cross-config correlation (§1a) is real and should be
disclosed (PHOTONICS'/EM's shared recommendation, which I adopt — see
§6), but it is a *fact about these particular residuals*, not the
*reason* the calibration leg fails as badly as it does.

**This does not vindicate `phase4_results.md`'s original framing either.**
Its claim — "the real per-config residuals carry genuine, exploitable
θ-adjacent correlation structure that an i.i.d.-of-any-marginal-shape
null cannot represent" — turns out to be *right for a different reason
than any document had stated before this Phase 5*: it is right because
of autocorrelation *shape*, not because the leg exposes something
uniquely present in `delta_ab` itself at the magnitude the null draws
suggest. QUANTUM's own §3c point 1–2 (wrong signature: the shared
structure is common-mode, not `ABSORB`-differential; wrong scale: its
own ~6.3–6.7° characteristic length matches neither T21's 1.9608° fringe
nor the ~2.5° T28 family) stand entirely independent of the scale-
invariance correction and are **not** overridden — they are arguments
about physical relevance, not about the calibration mechanism, and my
own re-verification of the underlying facts (§1a) supports them.

### 1c. Does this change the Combined Verdict? **No — confirmed three independent ways, all reproduced here.**

1. **The i.i.d. leg alone already fails, decisively, with zero
   dependence on any circular-shift construction choice**: 8.7×–11.2×
   nominal at α=0.01 (my own end-to-end re-run reproduces this exactly).
   This is sufficient, on its own, for `HALT_NULL_MISCALIBRATED_9COL`.
2. **The coupled-shift counterfactual (which respects the cross-config
   correlation) still fails, comparably or worse** (my own re-derivation:
   34.0×/34.6×/49.4× vs. the official independent-shift leg's
   38.9×/46.1×/44.1×) — so even granting PHOTONICS'/QUANTUM's concern in
   full and "fixing" it, the circular-shift leg's own verdict does not
   flip to PASS.
3. **`E[R_q^surr]=0` holds exactly** (EM's algebraic proof, THERMODYNAMICS'
   exhaustive 961-combination enumeration, both independently checkable
   from the pseudoinverse identity `row9·X8=0` I re-verified directly) —
   there is no location bias hiding behind the magnitude story either.

**Resolution of the task's explicit question**: EM's and THERMODYNAMICS'
robustness testing (same-shift/coupled-shift reconstructions) **is
sufficient confirmation that `HALT_NULL_MISCALIBRATED_9COL` stands
regardless** of how the cross-config-correlation finding is read. The
finding changes what the record should say about *why* the
circular-shift leg fails so much worse than the i.i.d. leg (a shape/
autocorrelation story, not an amplitude/cancellation-destruction story),
and it flags a real disclosure gap in the reusable machinery (§6), but it
does not touch the Combined Verdict, which was already established by
the i.i.d. leg alone.

---

## 2. The two arithmetic corrections — CONFIRMED, both real, both non-load-bearing, both to be corrected in place per R4

### 2a. "72 cell combinations" → 36

Direct count of `fit_and_calibrate_results.json`'s own `calibration.<pair>.detail`
dictionaries: 12 cells per pair (9 i.i.d. + 3 circular-shift) × 3 free
pairs = **36**, not 72. Confirmed identically by THERMODYNAMICS and
VISION; independently re-confirmed here by direct enumeration. **All 36
cells fail** — the substantive claim ("every cell fails") is unaffected;
only the count is wrong, by exactly 2×.

### 2b. "3.5×–5.9× worse... at every α" → does not hold at α=0.10; true range ≈2.2×–6.7× depending on comparison method

Recomputed the circular-shift/i.i.d. ratio directly from the committed
JSON under five conventions (worst-, best-, mean-, and fixed-σ i.i.d.
comparators, and every individual (pair,α,σ) cell):

| Method | α=0.01 | α=0.05 | α=0.10 | Overall |
|---|---|---|---|---|
| worst i.i.d. (max over 3σ) | 3.47–5.07× | 2.74–3.30× | 2.24–2.66× | 2.24–5.07× |
| best i.i.d. (min over 3σ) | 4.48–5.65× | 3.22–4.02× | 2.63–2.95× | 2.63–5.65× |
| fixed σ=0.0005 | 3.47–6.68× | 2.74–3.65× | 2.24–2.95× | 2.24–6.68× |

Matches MATERIALS' and VISION's independently-computed tables exactly.
**At α=0.10 the ratio never reaches 3.5× under any convention (tops out
at 2.66×–3.00×), and at α=0.01 two conventions exceed 5.9× (up to 6.68×
at C60–C70/σ=0.0005).** The claim as written ("3.5×–5.9× at every α")
does not reproduce. **Non-outcome-determining** — the qualitative claim
(circular-shift leg fails far worse than i.i.d., at every pair and every
α individually) is correct and unaffected; only the specific numeric
range attached to "at every α" is wrong. **Correction (per MATERIALS'/
VISION's recommendation, adopted): replace with the honest full range
(2.2×–6.7× over all cells) or a per-α breakdown (α=0.01: 3.5×–5.7×;
α=0.05: 2.7×–4.0×; α=0.10: 2.2×–3.0×).**

Both corrections should be applied in place to `phase4_results.md` and
`NOTES.md` per R4/house convention — neither changes the Combined
Verdict, both are the same failure shape (an aggregate/derived figure
computed once and generalized without re-checking every case) this
program's R4 lineage exists to catch.

---

## 3. `lev9_Rq` "exactly as predicted" — CONFIRMED as a real, minor overclaim, in tension with the record's own more careful statement elsewhere

Independently reproduced QUANTUM's naive-Gaussian-quantile translation
(`ratio(α) = 2·(1−Φ(z_{α/2}·√lev))/α`):

```
lev≈0.795 (exp-073, 5-col): predicted ratio @α=0.01 ≈ 2.16   observed 5.4–5.7×
lev≈0.59  (exp-074, 9-col): predicted ratio @α=0.01 ≈ 4.79   observed 8.7–11.2×
```

Both cycles' observed inflation exceeds the naive translation by a
consistent factor (≈1.8×–2.6× on my own quick reproduction, matching
QUANTUM's stated "~1.6×–2.7×" band). **Confirmed: `lev9_Rq` correctly
predicts the *direction* (lower ratio ⇒ worse inflation) and the
*relative* worsening between cycles, but underpredicts the *absolute*
magnitude by a real, consistent factor.** `phase4_results.md`'s "exactly
as predicted from the lower `lev9_Rq`" phrasing overclaims precision;
`NOTES.md`'s own "Learned" section already states the more careful
version ("correctly predicted the DIRECTION... but could not have
predicted its MAGNITUDE") — the two documents are in tension with each
other on this exact point. **Minor, non-outcome-determining, correct in
place**: soften `phase4_results.md`'s phrasing to match `NOTES.md`'s
already-correct hedge.

---

## 4. QUANTUM's recommendation to kill the "circular-shift leg as evidence of a genuine second contributor" reading — ADOPTED, with one of its four supporting reasons revised

QUANTUM's four reasons (§3c): (1) wrong signature (common-mode, not
config-differential), (2) wrong scale (6.3–6.7° ≈ window span, matches
neither T21's fringe nor the T28 family), (3) manufactured-not-exposed
(the amplitude-mismatch mechanism), (4) textbook R5 look-elsewhere shape
(an enormous, unregistered `(sA,sB)` search space with no pre-registered
target).

**Adopted as record language, with reason 3 revised per §1b above**:
reasons 1, 2, and 4 stand independently of the scale-invariance
correction and are confirmed by this audit's own re-derivation of the
underlying facts. Reason 3 should be restated as: *"the leg's severity
is driven by genuine lag-1 autocorrelation in the per-config residuals
(confirmed by a coupled-shift counterfactual and a matched-scale
white-noise control, both robust to the independent-vs-coupled shift-
pairing choice — see THERMODYNAMICS'/EM's Phase-5 findings), not by an
amplitude artifact of independently decorrelating two near-identical
signals (EM's scale-invariance proof rules out the amplitude story as
the mechanism) — but this autocorrelated structure is itself the
window's own already-disclosed curvature misspecification
(Idealization 7), common-mode across all four `ABSORB` depths, not a
config-specific or T28-scale-relevant signal."* With that revision, the
four-reason kill recommendation is stronger, not weaker, than as
originally written (it is no longer resting on a mechanism EM's own
rigorous proof contradicts) and should be adopted verbatim in the
LOGBOOK entry.

---

## 5. Checkpoint check

### Criterion 4 (program-integrity drift) — does NOT fire. Explicit comparison against the exp-072/073 precedent, per the task's instruction.

**exp-072 (Iteration 49) fired**: a carrier-phase sign bug corrupted
every published coefficient, invisible to `cond5`, R², residuals, fitted
values, four phases of review, and an independent re-implementation —
caught only by forward-simulating known ground truth at Phase 5. The
defect was live in the *scored, load-bearing* numbers throughout Phases
1–4 and nobody caught it until Phase 5's ground-truth check.

**exp-073 (Iteration 50) fired**: a self-catch reached the *wrong*
conclusion (`dR_q/dψ̄≡+R_i` instead of `−R_i`) and that wrong conclusion
was *defended* — passed by a magnitude-only check that could not
distinguish the two signs — surviving Phase 3/4 and five of six Phase-5
seats before EM's Phase-5 review caught it. The firing shape, per
LOGBOOK's own language: "a claim defended rather than re-derived against
contradicting evidence already on the table."

**exp-074 does not match either shape:**

- The Phase-1 CLOSURE-CONFIRM overclaim was caught by **two of five
  blind Phase-2 critics, by two independent methods**, confirmed
  computationally by Red Team's own Phase-2 audit — all of this
  happened **before Phase 3 synthesis**, and Phase 3 accepted every one
  of Red Team's ten docket items with **zero** overrides. The flawed
  claim never reached an officially-scored result; it was withdrawn at
  the earliest possible gate, exactly the shape Red Team's own Phase-2
  audit (§8) already ruled non-firing, conditional on Phase 3 not
  re-adopting it — and Phase 3 did not.
- The Phase-5 cross-config-correlation finding is a **genuinely new
  finding, not a defended wrong claim**. `fit_and_calibrate.py` did not
  exist until Phase 3 (commit `3aaae38`) — after all five blind Phase-2
  critiques and Red Team's Phase-2 audit had already run (`b5006ad`,
  earlier). No seat had the opportunity to catch this before Phase 5;
  PHOTONICS' own review states this explicitly and correctly. Nobody
  defended a claim against contradicting evidence already on the table —
  the evidence did not exist yet.
- Independent of interpretation, **the Combined Verdict itself never
  moved** — three independent seats confirmed `HALT_NULL_MISCALIBRATED_
  9COL` stands regardless of how the circular-shift leg's causal story
  is read (§1c above). exp-072/073 both fired because a corrupted or
  wrongly-defended number was actively load-bearing in what the program
  believed; here, the number the program's verdict rests on (the i.i.d.
  leg's own decisive failure) was never in question.

**One recurring pattern worth flagging explicitly, though it does not
rise to firing Criterion 4 on its own**: two of six blind Phase-5 seats
(PHOTONICS §1, MATERIALS §0) reproduced the false "72 cell combinations"
figure verbatim in their own "what I ran" reproduction sections, without
independently re-deriving the count — the *identical* failure shape
LOGBOOK's own R4 addendum (Iteration 50) was written to police ("two of
six blind Phase-5 seats... independently re-ran the pipeline and still
repeated a false '144/144' claim"). This is now a **third** instance of
this exact pattern (exp-073's "144/144", now exp-074's "72 cells"),
despite the rule already being on the books. It is non-load-bearing here
(the other two of six seats, VISION and THERMODYNAMICS, did independently
catch it, and the correction reaches LOGBOOK regardless), but the
recurrence across a third cycle after the rule was written suggests the
existing R4 addendum language ("must be independently checked") is not
by itself sufficient to prevent a Phase-5 reviewer from restating an
aggregate figure while verifying something else. **Recommended addendum
to R4 (not a new rule number — one more instance, not yet the pattern
threshold for a fresh rule)**: a Phase-5 reviewer's own reproduction
section must recompute, not merely restate, any cell-count or
combinatorial total it cites from a prior document, the same standard
already applied to the substantive claim being reviewed.

### Criterion 5 (two consecutive non-advancing iterations) — does NOT fire.

This cycle delivers genuine, independently-verifiable narrowing, matching
the non-firing pattern already established for exp-070/072/073: R7
adopted and confirmed on its first application (direction correct,
magnitude gap now quantified); the i.i.d.-leg HALT is decisive and
robust; a real, new methodological finding (autocorrelation, not
amplitude, drives structure-preserving-null miscalibration, confirmed
against a proper control) generalizes beyond T28 to any future
correlated-residual calibration leg in this program; two small numeric
corrections identified and closed within the same cycle's own Phase 5
before reaching LOGBOOK. This is the sixth consecutive non-decisive
cycle on the exact differential/two-tone sub-thread (Iterations 46–51),
but — per the pre-committed seventh-cycle rule (`phase3_synthesis.md`
§6), which this audit finds correctly triggered — that is itself the
honest, decisive outcome this rule exists to produce, not a failure to
advance.

---

## 6. R7 — CONFIRMED standing, no drift, no amendment needed to its text; one disclosure addendum recommended for its *machinery*, not the rule itself

MATERIALS' side-by-side comparison of Red Team's Phase-2 candidate text
against `phase3_synthesis.md` §2 found no drift; I independently
re-checked the same two passages and concur — substance identical,
necessary-not-sufficient framing intact, no softening or scope-widening.
EM's from-scratch re-derivation of both closed-form properties R7's
first application depends on (`E[R_q^surr]=0` exactly; `lev9_Rq` is
exactly `E[Var(R_q^surr)]/Var(R_q_obs)` under H₀) checks out, independent
of any prior seat's authority, and I independently re-verified the
`row9·X8=0` identity and the scale-invariance property both proofs rely
on. **R7 stands as adopted, without modification.**

**Recommended, non-blocking, for the reusable machinery (not R7's own
text)**, per PHOTONICS'/EM's converging recommendation: before
`per_config_residuals`/`calibrate_null` is pointed at different data in
a future cycle, disclose the cross-config correlation table (§1a) in the
script's own output, and add a documented coupled-shift (or
jointly-resampled) alternative as a second, comparison leg — not because
it changes this cycle's verdict (it does not, confirmed §1c), but
because the next dataset's per-config residuals may not be as forgivingly
comparable-under-either-construction as this one happened to be.

---

## 7. My own recommendation for LOGBOOK.md's Iteration 51 entry

**Verdict: PARTIAL.** (Matches five of six Phase-5 seats — PHOTONICS,
MATERIALS, EM, QUANTUM score PARTIAL; THERMODYNAMICS and VISION score
PROMISING but scope it identically, as a methodological/instrument
result, not a T28 mechanism finding. I use PARTIAL because the mechanism
question — the program's actual object of interest — is exactly where
exp-072 left it, and "PROMISING" risks being misread as forward motion on
that question when the real forward motion is entirely instrument-level.)

**Suggested entry text:**

> **Iteration 51 (exp-074) — the actual 9-column fit + a genuinely
> order-preserving null-calibration test, Combined Verdict
> `HALT_NULL_MISCALIBRATED_9COL`, confirmed robust; a Phase-1 overclaim
> caught and withdrawn before it ever reached a scored result; a new,
> generalized standing rule (R7) confirmed on first application.**
> Phase 1 (EM) priced the 9-column two-tone design's conditioning
> without fitting it and claimed CLOSURE-CONFIRM; two of five blind
> Phase-2 critics (PHOTONICS, THERMODYNAMICS), by two independent
> methods, showed this claim does not survive (contaminant-period
> non-robustness; the real fit's significance exceeds the "optimistic"
> bound at 3 of 4 pairs, by up to 9.3×) — confirmed in full by Red Team's
> Phase-2 audit, which added a sixth finding of its own and proposed a
> new standing rule, **R7**: *a conditioning/VIF-based pricing of an
> un-fit multi-tone design is necessary, not sufficient, evidence for a
> closure or detection claim — the design must be fit to real data and
> null-calibrated before either verdict is drawn.* The Director adopted
> all ten of Red Team's docket items with zero overrides, withdrew §5/§6
> of the Phase-1 proposal, adopted R7, and designed `fit_and_calibrate.py`
> — the actual 9-column fit, gated behind a two-leg null-calibration test
> (i.i.d. Gaussian; a new, genuinely order-preserving circular-shift leg
> built from each config's own real residual). **Official result: both
> legs fail.** The i.i.d. leg fails 8.7×–11.2× nominal at α=0.01 (worse
> than exp-073's 5-column 5.4×, as predicted in direction, though not in
> absolute magnitude, by the lower `lev9_Rq≈0.59` computed before the
> run). The circular-shift leg fails far worse (38.9×–46.1× nominal at
> α=0.01, corrected count: 36 total calibration cells, not the "72"
> `phase4_results.md` states; all 36 fail). **z9=5.03 at C60–C70 remains
> genuinely unresolved** — no valid null yet exists to test it.
> **Six independently-blind Phase-5 reviews converged on a genuine
> methodological finding not available at Phase 2** (`fit_and_calibrate.py`
> did not exist until Phase 3): the four `ABSORB` configs' own per-config
> residuals are near-identical (r=0.992–1.000) and strongly autocorrelated
> in θ (lag-1≈0.92–0.94) — a shared, common-mode curvature-misspecification
> artifact (Idealization 7), not `ABSORB`-differential noise. **Three
> independent robustness tests (EM's scale-invariance proof, THERMODYNAMICS'
> coupled-shift counterfactual, QUANTUM's direct magnitude comparison — all
> independently reconfirmed by this audit) establish this does NOT change
> the Combined Verdict**: the i.i.d. leg alone already fails decisively
> and independently of the circular-shift construction; a coupled-shift
> counterfactual respecting the cross-config correlation still fails
> comparably-or-worse (35.9×–52.3×); the leg's severity is driven by
> genuine autocorrelation shape (confirmed against a matched-scale
> white-noise control), not by an amplitude artifact of the independent-
> vs-coupled shift-pairing choice (a mechanism EM's rigorous scale-
> invariance proof rules out). Per this audit's ruling, QUANTUM's
> recommendation to explicitly foreclose reading the circular-shift leg
> as "evidence of a genuine second [T28-relevant] contributor" is adopted
> as record language (wrong signature — common-mode, not config-tied;
> wrong scale — ~6.3–6.7° matches neither T21's fringe nor the T28 family;
> a textbook R5 look-elsewhere shape). **R7 stands as adopted, without
> modification, confirmed on its first application** (correctly predicts
> direction and relative worsening; underpredicts absolute inflation
> magnitude by a consistent ~1.6×–2.7×, a disclosed, non-fatal limitation).
> Two small arithmetic slips in `phase4_results.md`/`NOTES.md` — "72 cell
> combinations" (true: 36) and "3.5×–5.9× worse... at every α" (does not
> hold at α=0.10; true range ≈2.2×–6.7× depending on comparison method) —
> corrected in place per R4; both non-load-bearing. **This is the sixth
> consecutive non-decisive T28 differential/two-tone cycle (Iterations
> 46–51). Per the pre-committed seventh-cycle rule, no seventh cycle on
> the same instrument class (a sign-flip/permutation null on this
> ramped-quadrature OLS basis, at any window width, single- or multi-tone)
> is authorized without a qualitatively different calibration strategy —
> the underlying pricing/fitting machinery (`desk_check_pricing.py`,
> `fit_and_calibrate.py`, R6, R7) is NOT retired.** No Checkpoint
> criterion fires — this cycle's self-correction sequence (Phase-1
> overclaim caught pre-synthesis by two blind critics and confirmed by
> Red Team; a genuinely new Phase-5 finding correctly shown non-
> load-bearing by three independent robustness tests) is materially
> weaker-triggering than the exp-072/exp-073 Checkpoint-4 precedent (a
> corrupted or wrongly-defended number that was actively load-bearing in
> the program's belief, surviving to Phase 5 undetected or defended
> against contradicting evidence) — explicitly compared and distinguished
> in this cycle's own Phase-5 final audit. One recurring, non-firing
> pattern flagged for the record: two of six blind Phase-5 seats
> (PHOTONICS, MATERIALS) restated the false "72 cells" figure without
> independently recomputing it — the third instance of the exact shape
> R4's Iteration-50 addendum was written to police (after exp-073's
> "144/144"); the other two of six seats (VISION, THERMODYNAMICS) did
> catch it, so the correction reaches the record regardless, but the
> recurrence is worth naming. Verdict PARTIAL.

---

## 8. My own final top-3 ranking for PLAN.md's Iteration-52 queue

Reconciling all six seats' rankings (PHOTONICS, MATERIALS, EM, QUANTUM
rank PHOTONICS' WKB/adiabatic model #1; THERMODYNAMICS ranks it #2;
VISION ranks it #2 behind a same-cycle housekeeping item):

1. **PHOTONICS' WKB/adiabatic boundary-reflectance analytic model for the
   graded-loss `ABSORB` band** (PLAN.md Iteration-51 queue item 4; queued
   and dropped without execution at Iterations 46 and 47; near-unanimous
   #1 this cycle, 4 of 6 seats). Zero FDTD, zero data, engages a seat's
   own charter physics directly rather than re-verifying statistics a
   sixth time, and is the explicit example this cycle's own seventh-cycle
   rule names as a "qualitatively different" approach that WOULD authorize
   a further attempt on the sub-thread. Independently strengthened by
   this cycle's own §1 finding: the leftover-after-best-single-sinusoid
   residual shape is depth-*independent* (essentially the same curve at
   all four `ABSORB` depths), which argues, for free, toward a
   shared-geometry/boundary-admittance origin rather than a graded-
   absorber-depth-tied one — a data point this analytic model can use
   directly.
2. **G40/`PAD` decorrelation** (~31 FDTD calls, per MATERIALS' verified
   geometry-reuse claim; picked in the top 3 by five of six seats).
   The only queued item that actually *relieves*, rather than discloses
   or prices, the `ABSORB`-or-`PAD` confound that has followed every
   causal claim on this thread since Iteration 48. Orthogonal to item 1
   and to this cycle's own null-calibration findings; cheapest remaining
   FDTD relief on the board. Readout on the phase-invariant amplitude
   channel (`√(A_i²+A_q²)/a`) inherits neither the Rayleigh-resolution
   problem nor any sign-flip calibration problem, and is explicitly NOT
   blocked by the seventh-cycle rule (a genuinely different instrument
   class, per VISION's own note — worth stating explicitly in the
   Iteration-52 entry so the rule is not misread as barring it).
3. **Bundle this cycle's own record-hygiene corrections with a disclosure
   patch to the reusable calibration machinery, before either of items
   1–2 starts** (near-zero cost, touched by all six seats in some form):
   (a) correct `phase4_results.md`/`NOTES.md`'s two arithmetic slips
   (§2, this audit) and the `lev9_Rq` "exactly as predicted" overclaim
   (§3); (b) add the cross-config correlation table and lag-1
   autocorrelation figures (§1) as committed, reproducible script output
   rather than prose assertions, and add a documented coupled-shift
   alternative to `calibrate_null` (§6) — before `fit_and_calibrate.py`'s
   own explicitly-kept-for-reuse machinery is pointed at a dataset where
   the two constructions might not agree as comfortably as they did here;
   (c) finally correct the three-document-old "house precedent, Iteration
   5, exp-027" mislabel (THERMODYNAMICS' Phase-2 finding this cycle,
   correctly ruled out-of-scope for exp-074 itself, still uncorrected).
   None of this relieves a physical confound or advances T28's mechanism
   question, but all three are on the sub-thread's own critical path for
   trustworthiness and get more expensive the longer they sit, per this
   program's own R4 history.

**Not ranked, but flagged as a strong secondary candidate for the
backlog**: THERMODYNAMICS' proposal to fit the near-universal common-mode
residual directly (not another pairwise difference) — a genuinely
different instrument (no differencing of two near-identical signals, no
sign-flip/permutation null on `X9`) that is not barred by the
seventh-cycle rule and is independently motivated by this cycle's own
§1 finding. It does not make my top 3 only because item 1 (WKB) answers
the same underlying question analytically, at zero cost and zero new
statistical-calibration risk, and should be tried first.

---

## 9. Bottom line

The instrument built this cycle (`desk_check_pricing.py`,
`fit_and_calibrate.py`, R7) is sound, correctly engineered, and earns its
place in the record regardless of T28's own fate — every load-bearing
computational claim in `phase4_results.md` reproduces exactly, and the
Combined Verdict `HALT_NULL_MISCALIBRATED_9COL` is robust to every
adversarial reconstruction this audit and all six Phase-5 reviews
attempted. This cycle's own arc — a Phase-1 overclaim caught by two blind
critics before Phase 3 ever adopted it, a properly-gated re-design that
then surfaced one more subtle, previously-uncheckable defect at Phase 5,
shown by three independent seats not to be load-bearing — is the
program's self-correction machinery working at every gate it has, one
level earlier each time (Phase 2 catches Phase 1; Phase 5 catches what
Phase 2 structurally could not have seen). Two small, non-load-bearing
citation/arithmetic slips remain to be corrected in place, and a third
recurrence of a previously-named failure pattern (aggregate figures
repeated blind by a subset of Phase-5 reviewers) is worth a tightened R4
addendum. No Checkpoint criterion fires. T28's differential/two-tone
sub-thread is retired on this instrument class, as pre-committed; the
program's real next move is PHOTONICS' queued analytic model, which no
further work on this statistical instrument can substitute for.
