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

*Predictions above are FROZEN at this commit, before `run.py` is executed.
Results follow in a separate commit.*
