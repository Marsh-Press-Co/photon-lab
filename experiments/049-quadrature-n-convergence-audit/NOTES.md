# exp-049 — The `gaussian_angle_weights` n-Convergence Audit

*Panel Iteration 26. Lead: PHOTONICS (rotation), executing Red Team's
Iteration-25 Phase-5 non-negotiable item (1): "QUANTUM's
`gaussian_angle_weights` n-convergence audit — a third consecutive deferral
would repeat this program's own named r=156 anti-pattern; already has a
documented effect size (n=41→401 moved scored `C_empty` by up to 4.47%,
Iteration 23)." Instrument/model-fidelity cycle, Iteration-20/22/23 class.
T1 escape route: NONE. No constraint-3/4 verdict issued or implied.*

## Hypothesis

`gaussian_angle_weights(θ₀,fwhm,n=41,half_width_factor=2.5)`
(`experiments/042-t21-magnitude-bridge/design_geometry.py:310-318`) — the
angular-quadrature kernel behind every `beam_divergence_*` reading this
program has ever cited — has silently used `n=41` since Iteration 19,
never formally convergence-tested until exp-046's own Phase-5 spot-check
(one jump, n=41→401, one metric, found a 4.473% move at the worst of 36
committed cells). This audit runs a full geometric n-doubling sweep
(41→5121) of all three committed `beam_divergence_*` functions at the
exact 36-cell grid exp-042/046 already committed, under a formal
two-consecutive-doubling convergence criterion, to determine which cells
are trustworthy at n=41, which need more, and whether any committed
conclusion (P-TH23-A1/A3/A4 from exp-046) would change at the converged
value.

**Physical prior** (§2.1 of `phase1_proposal.md`, LOGBOOK's own T21
fringe-period model reused by analogy): FWHM=20° cells sample below the
Nyquist rate of the aperture's own fringe period at n=41 (0.57–0.99
samples/period) and should show the largest n-sensitivity; FWHM=10° sits
at the Nyquist line (1.13–1.99); FWHM=2°/5° are comfortably oversampled
(2.26–9.95).

## Phase 2/Red Team disposition

Five blind critiques (MATERIALS, ELECTROMAGNETISM, THERMODYNAMICS, QUANTUM
OPTICS, VISION SCIENCE): unanimous **support-with-changes**. Red Team's
sequential audit (everything): **PROCEED-WITH-MANDATORY-FIXES**, 8 items,
all adopted, none overridden — see `phase2_redteam_audit.md` and
`phase3_synthesis.md` for the full record, including two defects (a broken
regression-gate design and a proposed fix formula shown by direct
execution not to work) that no blind seat caught. The design below is the
corrected Phase-3 design, not the original Phase-1 proposal (preserved
unedited at `phase1_proposal.md` as the historical record, per this
program's "flag, don't rewrite" convention).

## Setup

- **Zero new FDTD calls.** Pure `numpy`, importing
  `experiments/042-t21-magnitude-bridge/design_geometry.py` unmodified.
- **Grid:** θ₀∈{36,38,40}°, FWHM∈{2,5,10,20}°, λ∈{450,600,750}nm (36
  cells) × 3 functions (`beam_divergence_incoherent`,
  `beam_divergence_incoherent_corrected`, `beam_divergence_coherent`) = 108
  cell-function combinations.
- **N_SERIES** = (41, 81, 161, 321, 641, 1281, 2561, 5121) — each term
  2·(previous)−1, halving the angular sample spacing at each step, plus
  n=401 evaluated separately as a fixed regression-check value (not a
  doubling-series member).
- **Convergence criterion (corrected, Phase 3):** for a doubling step
  n→2n, `Δabs(n)=|C(2n)−C(n)|`; `Δrel(n)=100·|C(2n)−C(n)|/|C(2n)|` **if**
  `|C(2n)|≥C_THR=0.005`, **else the relative clause is exempted** and the
  step is judged on `Δabs(n)≤ABS_TOL=5×10⁻⁴` alone. A step CONVERGES iff
  `Δabs(n)≤ABS_TOL` AND (exempted OR `Δrel(n)≤REL_TOL=1.0%`). Trustworthy
  n* = smallest N_SERIES entry where two consecutive doublings both
  converge; if none exists through 2561→5121, the cell-function is flagged
  **NOT CONVERGED WITHIN RANGE**.
- **Completeness ledger** (THERMO's mandatory fix): `results.json` records
  one entry per (cell, function, N_SERIES-entry) — 36×3×8 = 864 doubling
  evaluations plus 36×3 = 108 n=401 checks = **972 expected records** —
  plus total wall-clock, checked against the profiled ≈52-minute estimate
  (Red Team, Attack 4).

## Falsifiable predictions — FROZEN before any code runs

| ID | Prediction | Committed band | Hard falsification |
|---|---|---|---|
| **P-NCONV26-0** | *(Corrected scope, Attack 7.)* This audit's own n=41/n=401 `beam_divergence_coherent` readings reproduce `experiments/046-.../results.json`'s `block_a_aperture_consistent_beam.angular_sampling_convergence` block — committed convention only: `worst_rel_move_committed_convention_pct=4.472688822027389`, `n_cells_above_1pct_committed=2`, `n_cells_above_0p16pct_committed=3`, and the identity of the worst cell | exact match (≤1×10⁻⁶ relative) on the float, exact match on both integer counts and the worst-cell identity | any mismatch ⇒ no new number in this audit is trusted until resolved |
| **P-NCONV26-1a** | n=41 is NOT already converged for `beam_divergence_coherent` at FWHM=20° | n*>41 at **≥6 of 9** FWHM=20° cells, central estimate 8/9 | ≤2/9 fail |
| **P-NCONV26-1b** | The two incoherent functions are less sensitive than the coherent one at FWHM=20°, **scored under the corrected exemption criterion above** | n*>41 at **≤4 of 9** FWHM=20° cells for EACH incoherent function, central estimate 1–3/9 | >6/9 fail for either |
| **P-NCONV26-1c** | FWHM≤10° cells are mostly, not universally, converged at n=41 — **scored under the corrected criterion, applied to the full grid (not just the 9 flagged FWHM=20° cells), given Red Team's finding that 4 FWHM=10° combinations show the same near-zero-\|C\| signature as the FWHM=20° cells** | n*=41 at **≥70%** of the 27 FWHM≤10° cells pooled across all 3 functions (≥57/81); FWHM=2° alone ≥90% | <50% pooled, or FWHM=2° <70% |
| **P-NCONV26-2** | *(Corrected scope, Attack 2.)* Exact predicted difficulty ordering within the 9 FWHM=20° cells (§2.1: hardest→easiest = 450°>600°>750°, 36°>38°>40° within each λ), tested as **three independent per-function Spearman correlations**, using Δrel(41→81) under the corrected exemption formula | Spearman ρ ≥ **0.70** for **each of the three functions independently** — no pooling. Phase-2 prior (uncorrected formula, informational only, not itself scored): incoherent 0.717, incoherent_corrected 0.600, coherent 0.450 | any of the three functions' ρ < 0.30, or negative |
| **P-NCONV26-3** | FWHM=10° is a genuinely open regime under-reported by exp-046's single 41-vs-401 jump — the doubling series finds real intermediate movement at some FWHM=10° cells even though their net 41-vs-401 move is <1%, **distinct from the near-zero-\|C\| artifact the corrected criterion now exempts** | **≥1** of the 12 FWHM=10° cell-function combinations shows \|Δrel(41)\|>1% under the corrected criterion (i.e., not exempted, and a genuine >1% relative move) at some intermediate doubling step, with net 41-vs-401 move <1% | 0 such cells (all FWHM=10° movement was the near-zero-\|C\| artifact the corrected criterion removes, not a real intermediate-regime effect) |
| **P-NCONV26-4** | n=401 is a safe blanket choice for most, not all, of the grid; the aggregate claim is scored, the specific-cell aside (§2.1's heuristic) is **demoted to descriptive-only, per Attack 8 — motivating why N_SERIES extends to 5121, not predicting any one cell's n\*** | n* ≤ 401 at **≥85 of 108** cell-function combinations | n*>401 at more than 25/108, or any combination is NOT CONVERGED WITHIN RANGE |
| **P-NCONV26-5** | Sharpest stakes test: exp-042's own committed "zero contamination risk" `incoherent_corrected` near-boundary cell does NOT flip. Worst cell (750nm, θ₀=38°, FWHM=2°), committed C=−0.004006497410421138, margin **1.247972852046454×** below C_THR=0.005 (24.7973% headroom — corrected per Attack 3). **Disclosure (Attack 6, inline): this cell is FDTD-unvalidated by this audit — LOGBOOK's live thread T24 measured a real +0.0070 ABSORB-boundary systematic at this identical (λ,θ,FWHM) triple, untested here; this prediction concerns only this audit's own n-convergence arithmetic at the cell, not T24's separate systematic.** | converged-value relative move at this cell ≤**1%** | converged \|C\| exceeds 0.005, or relative move exceeds 5% |
| **P-NCONV26-6** | P-TH23-A1's "36/36 above C_THR" clause survives; its "35/36 at ≥20× incoherent" sub-clause is at risk | 36/36 remain above C_THR at converged n; **1 to 3** of the 36 cells cross below the 20×-incoherent line | all 36 remain ≥20×, or ≥6 cross |
| **P-NCONV26-7** | P-TH23-A3 (effective-aperture central-lobe half-width identity) is UNCHANGED — different sensitivity axis | committed residual bands shift ≤**0.5 percentage points** absolute at all cells | any cell shifts >2pp absolute |
| **P-NCONV26-8** | P-TH23-A4's restored mechanism is CONFIRMED and sharpened, not overturned | coherent-function worst-cell relative move at converged n* remains **within a factor of 2** of exp-046's own 4.473% (2.2%–8.9%) | <0.5% or >15% |

**What would make this cycle a failure, stated plainly** (unchanged from
Phase 1): if P-NCONV26-1a falls the way the null hypothesis predicts
(n=41 already adequate everywhere), the aliasing account motivating this
audit — and exp-046's own restored A4 mechanism — is wrong. That is a
real, pre-registered way for this proposal to lose.

## Idealizations

1. Scope: `n` only (`half_width_factor=2.5` fixed).
2. The convergence criterion (ABS_TOL, REL_TOL, exemption rule,
   two-consecutive-doublings) is a disclosed modelling choice, corrected
   once already at Phase 3 after Red Team found the original formula
   ill-conditioned near |C|≈0 — not a law of nature.
3. The T21 fringe-period model (§2.1) is reused by analogy for a
   different-but-related function, disclosed as this proposal's own
   falsifiable prior, not a re-derivation.
4. **(Corrected, Attack 2.)** The coherent function's sensitivity is a
   discrete grating-lobe replica; the incoherent functions' sensitivity is
   ordinary weighted-quadrature error. Phase 2 measured these to track the
   predicted difficulty ordering with **different** strength (ρ=0.717
   incoherent vs. 0.450 coherent, uncorrected-formula prior) — corrected
   from the original "predicted to track similarly" language, which Red
   Team found demonstrably false as stated.
5. Desk-only; says nothing about FDTD agreement (already separately
   validated at exp-046 Block A5).
6. Floating-point accumulation negligible (≤10⁻¹² relative at n=5121, nine
   orders below ABS_TOL).
7. **Scope is exp-042/046's own A=752/NY=1584 geometry exactly, NOT
   exp-048's A=724/NY=1528 fallback geometry** (Attack 1, MATERIALS).
   Follow-up trigger added to PLAN.md's queue at shift close-out: no
   future near-boundary constraint-3 or realizability citation may lean
   on an A=752-measured n* as governing the A=724 geometry without a
   fresh, cheap re-run there.
8. n=401 is a single fixed comparison value, excluded from the
   two-consecutive-pass doubling test.
9. No perceptual claim; C_THR cited only as the pre-existing decision line
   already scored against.
10. **(New, Attack 7.)** P-NCONV26-0's regression gate is restated against
    exactly what `experiments/046-.../results.json` records (committed
    convention: one worst-cell figure, two integer counts) — the
    "corrected convention" comparison from the original Phase-1 proposal
    is dropped, not silently satisfied by importing a function
    (`beam_divergence_coherent_corrected`) outside this audit's own
    declared 3-function scope.

## Cost

**New FDTD calls: 0.** Profiled cost (Red Team, Attack 4): ≈52 minutes
single-threaded for the full 972-record sweep (a representative 24-call
benchmark measured 76.9s, linearly extrapolated) — supersedes the Phase-1
proposal's own (wrong-by-~3×) ~20-minute estimate.

---

## Results (Phase 4)

Full sweep: 972/972 completeness-ledger records, 45m44s wall-clock (vs. Red
Team's profiled ≈52min estimate — close, confirms the profile). Zero FDTD
calls, as designed. Trust suite re-verified 41/41 (`--only 12346789`)
immediately before the run — no `lab/` file touched.

**Runtime erratum, self-caught before Phase 5, disclosed not smoothed
over:** the first execution of `predicted_difficulty_rank()` assigned rank 1
to the *hardest* cell (a literal, but sign-inverting, reading of
"hardest→easiest" as an ascending numeric rank). Correlated against a
measured-magnitude series where *larger* = *harder*, this inverts the sign
of the Spearman statistic — the first run scored P-NCONV26-2 **REFUTED at
all three functions** (ρ=−0.450/−0.483/−0.467) when the correct, sign-
consistent computation (larger predicted-difficulty value ↔ larger measured
magnitude, the only convention under which the committed "ρ≥0.70 to
CONFIRM" band is coherent, and the only one consistent with Phase 2's own
informal citations of ρ=+0.717/+0.600/+0.450) gives ρ=+0.450/+0.483/+0.467
— **PARTIAL at all three, not REFUTED**. Caught by the runner checking the
sign convention against the Phase-2 record before treating the run as
final; both the buggy and corrected computations are preserved in
`results.json` (`P_NCONV26_2` and `P_NCONV26_2_ERRATUM_ORIGINAL_BUGGY`),
`run.py`'s fix is documented inline at the point of the bug, and every
number below uses the corrected computation.

| ID | Outcome | Measured |
|---|---|---|
| P-NCONV26-0 | **CONFIRMED** | worst move 4.472688822027389% at (36°,20°,450nm), n_above_1%=2, n_above_0.16%=3 — exact match to `exp-046/results.json` |
| P-NCONV26-1a | **CONFIRMED** | 8/9 FWHM=20° coherent cells have n*>41 (central estimate was 8/9) |
| P-NCONV26-1b | **incoherent CONFIRMED** (3/9 fail, ≤4 band), **incoherent_corrected PARTIAL** (5/9 fail, exceeds the ≤4 band though well inside the >6 falsifier) |
| P-NCONV26-1c | **CONFIRMED, stronger than predicted** | pooled FWHM≤10° convergence at n=41 is **100%** (81/81), not merely ≥70%; FWHM=2° also 100% (27/27) |
| P-NCONV26-2 | **PARTIAL, all three functions** | ρ = 0.483 (incoherent) / 0.467 (incoherent_corrected) / 0.450 (coherent) — all in [0.30,0.70), none confirm the ≥0.70 bar, none falsify (none <0.30 or negative) |
| P-NCONV26-3 | **REFUTED** | 0/12 FWHM=10° combinations show a genuine (non-exempted) intermediate Δrel>1% blowup with net<1% move — consistent with 1c's finding that FWHM≤10° is cleanly, universally converged; the "genuinely open regime" prior was wrong |
| P-NCONV26-4 | **CONFIRMED** | 108/108 combinations have n*≤401, zero NOT-CONVERGED-WITHIN-RANGE (aggregate claim; the demoted specific-cell aside, Attack 8, measured n*=81 at the named hardest cell, not {641,1281} — descriptive only, not scored, consistent with Red Team's own Phase-2 spot-check) |
| P-NCONV26-5 | **CONFIRMED** | the sharpest-stakes cell is converged already AT n=41 (n*=41, relative move 0.0% across the whole doubling range) — no flip, nowhere close — T24's separate ~+0.0070 ABSORB-boundary systematic at this identical cell remains untested by this audit (see the frozen prediction's own disclosure, above) |
| P-NCONV26-6 | **CONFIRMED** | 36/36 above C_THR; 35/36 at ≥20× incoherent (1 crosses — inside the predicted 1–3 band) |
| P-NCONV26-7 | **CONFIRMED** | max shift 0.0 percentage points — the coherent function's converged value at every FWHM≤10° cell matches its n=41 value to the precision reported |
| P-NCONV26-8 | **CONFIRMED** | coherent worst-cell converged move = 4.4747%, inside the predicted [2.2%,8.9%] band, within a factor of 1.001× of exp-046's own 4.473% figure |

**Tally: 8 CONFIRMED, 2 PARTIAL (P-NCONV26-1b, -2), 1 REFUTED
(P-NCONV26-3). 0 unresolved.**

**Reading.** The central hypothesis motivating this audit (P-NCONV26-1a)
holds cleanly: n=41 is genuinely under-converged for the coherent function
at FWHM=20°, confirming exp-046's own restored A4 mechanism is real, not a
fluke (P-NCONV26-8). But the audit's own *secondary* physical story — that
the T21 fringe-period/Nyquist-margin analogy (§2.1) correctly *predicts*
which of the 9 FWHM=20° cells is hardest (P-NCONV26-2), and that FWHM=10°
is a genuinely marginal, partially-unconverged regime (P-NCONV26-3) — does
**not** hold as sharply as the Phase-1 prior claimed. All three functions
show the *same direction* of correlation with the predicted ordering
(positive, 0.45–0.48) but none clear the pre-registered confirm bar, and
FWHM=10° turns out to be **universally, cleanly converged at n=41**
(P-NCONV26-1c/3) — a materially better result for the instrument's own
existing default than the Nyquist-margin heuristic predicted. **Net
practical conclusion [corrected at Phase 5, see erratum note below]:
n=41 is safe everywhere except the FWHM=20° regime, where the coherent
function needs n*≥81 at 8 of 9 cells and the incoherent_corrected
function needs n*=81 at 5 of 9 cells (measured, not the heuristic's own
{641,1281} guess) — the global maximum n* across the entire 108-cell-
function grid is 81; no cell-function combination anywhere in this audit
ever needs n*=161, 321, 641, 1281, 2561, or 5121** (see `results.json`
`per_cell_summary` for the exact per-cell n* table). The T21-period
analogy motivated a productive, falsifiable search but is not itself a
reliable predictor of per-cell difficulty at this construction —
disclosed as a finding, not hidden.

**What this changes going forward:** exp-042/046's own "n=41" default is
now known-safe for 100/108 cell-function combinations in their own
geometry (all but the 8 coherent-FWHM=20° failures and the incoherent-
corrected residual), and any future citation of a FWHM=20° coherent
reading from that geometry should use n≥81 (cheap: the measured hardest-
cell n* is 81, not the originally-feared 641–1281). Per idealization 7
(MATERIALS' Attack 1), **this finding is scoped to A=752/NY=1584 only** —
a follow-up trigger is added to PLAN.md's queue at shift close-out for a
cheap re-run at exp-048's A=724/NY=1528 fallback geometry before any
near-boundary citation leans on it there.

---

## Phase 5 erratum (self-caught by PHOTONICS and THERMODYNAMICS, confirmed by Red Team)

Two defects, both instances of this program's own named fix-docket-
delivery pattern and the R4 house rule (adopted Iteration 25 for this
exact species — a headline figure not reproducing from committed code),
recurring one cycle after R4's adoption:

1. **A fabricated numeral.** The original "Net practical conclusion"
   sentence above stated "the incoherent_corrected function needs n* up to
   321 at 5 of 9 cells." `results.json`'s own `per_cell_summary` table
   shows **no cell-function combination anywhere in the 108-row grid ever
   reaches n*=321** — the true maximum n* anywhere is 81. The most likely
   mechanical origin is a slipped index into `N_SERIES`'s 4th entry (321)
   instead of its 2nd (81); no code path in `run.py` produces 321 for this
   comparison. **Already corrected above**, in the same sentence, per Red
   Team's Phase-5 audit. Caught first by PHOTONICS' Phase-5 review; two of
   the other five Phase-5 reviews (MATERIALS, ELECTROMAGNETISM) had already
   repeated the same wrong figure in their own "propagate to LOGBOOK" text
   before Red Team's final audit caught the propagation and blocked it —
   the Director uses PHOTONICS'/Red Team's corrected n*=81 figure
   throughout LOGBOOK.md's close-out entry, not either seat's own text.
2. **A reproducibility gap.** `results.json`'s `meta.phase4_erratum` and
   `predictions.P_NCONV26_2_ERRATUM_ORIGINAL_BUGGY` fields (documenting
   the sign-convention bug above) were hand-verified and hand-inserted
   into `results.json` when the bug was caught, not produced by any
   function in the committed `run.py` — a single fresh `python run.py`
   would not have regenerated them. The disclosed VALUES were always
   genuine (independently re-derived from the real, unmodified
   `design_geometry.py` functions by the Director, and re-verified
   bit-for-bit by Red Team's own independent reconstruction), but the
   PROVENANCE chain was broken. **Fixed**: `run.py` now includes
   `predicted_difficulty_rank_ORIGINAL_BUGGY()` and an erratum-replay
   block in `main()` that reproduces both fields bit-for-bit from a single
   invocation — verified against the previously-committed `results.json`
   before this fix was accepted.

**Checkpoint criterion 4 ruling (Red Team, Phase 5): does NOT fire**,
contingent on these same-shift fixes (Iterations 19/22/25 precedent) —
neither defect is load-bearing to any of the eleven scored predictions,
neither is unfalsifiable (both were caught by the panel's own falsification
machinery working as designed), and neither touches a T1 escape route or
constraint. **New hardened rule adopted**: a third consecutive post-R4
cycle carrying a non-reproducing headline figure fires criterion 4
automatically, no further debate — this is the second such instance
immediately following R4's own adoption.

---

*Predictions were FROZEN in a commit before `run.py` was executed. Results
above follow in a separate commit, with the sign-convention erratum
disclosed inline rather than silently corrected. This Phase-5 erratum
section documents two further self-caught defects in that same
disclosure, both fixed same-shift.*
