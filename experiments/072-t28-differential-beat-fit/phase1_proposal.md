# PHASE 1 — PROPOSE · Panel Iteration 49 · exp-072
## PHOTONICS' differential/beat fit of `delta_AB(θ)` between adjacent `ABSORB` configs (T28)

*Fresh sub-agent, PHOTONICS charter (PANEL.md seat: surface interaction,
absorption spectra, angular dependence, scattering cross-sections), lead by
rotation. Executes the Iteration-49 queue item 1 — Red Team's Phase-5
final-audit merge of ELECTROMAGNETISM's differential/beat-fit proposal and
QUANTUM OPTICS' matching Phase-5 proposal from exp-071 into a single
zero-FDTD-cost item.*

## Mandate (Iteration-49 queue, item 1, verbatim)

> Merge ELECTROMAGNETISM's differential/beat-fit and QUANTUM OPTICS'
> matching Phase-5 proposal into one item — zero new FDTD cost, fit
> `delta_AB(θ)=C_B(θ)−C_A(θ)` directly between ADJACENT `ABSORB` pairs
> (C40–C60, C60–C70, C70–C80, plus the already-analyzed C40–C80) on the 124
> already-collected data points, instead of independently fitting absolute
> periods per-config and then subtracting — converts an absolute-frequency
> Rayleigh-resolution problem (unsolvable at any achievable window for the
> C60–C70 pair specifically) into a phase-accumulation/beat-detection
> problem, reusing the exact methodology that discovered T28 in the first
> place (`C80−C40`, `ptp/mean=16.2`).

---

## 1. Mechanism narrative (why the differential is a sharper instrument)

T28's ~2.84° `C80−C40` periodicity is real and resolution-robust
(Iteration 46), lives in each config individually (Iteration 47), and
climbs smoothly with `ABSORB` depth (Iteration 48: 2.4361°/2.5188°/2.5338°/
2.5338°, linear R²=0.8664) — but Iteration 48 returned NEITHER, and
QUANTUM OPTICS then established why: the 6°/31-point window supplies
<10% of the Rayleigh resolution needed to separate C60's and C70's
absolute periods (0.59% apart). Fitting two absolute frequencies and
subtracting asks the window for a quantity it cannot deliver.

Differencing asks a different question. For two configs sharing every
construction constant but one, write
`C_A = a·cos(2πf_A x+ψ_A)`, `C_B = a·cos(2πf_B x+ψ_B)` in `x = sin θ`.
Then exactly

`delta_AB = −2a · sin(2πf̄x+ψ̄) · sin(πΔf·u + χ)`, `u = x−x̄`,

and because `|Δf|·X ≪ 1` over this window, the second factor linearizes:
`delta_AB ≈ −2a·sin(carrier)·[sin χ + πΔf·u·cos χ]`. The frequency
difference does **not** appear as a resolvable beat *frequency* inside a
6° window — the beat envelope is ~10× longer than the window. It appears
as a **linear amplitude ramp, in quadrature with the common-mode carrier**.
That coefficient is a continuous, well-conditioned regression parameter
estimated at the *common-mode* carrier frequency (which the window
resolves comfortably, ~2.4 periods), not a difference of two frequencies
neither of which the window resolves. Common-mode structure — T21's
fringe, the fixed `A=752` aperture response, discretization offsets —
cancels in the subtraction, exactly the logic that made `C80−C40` legible
at `ptp/mean=16.2` in the first place.

A concrete symptom of the old instrument's failure: exp-069's free-period
grid (`n_grid=400` over [1°,4°]) quantizes at 0.00752°, i.e. 0.30% of the
period. C60 and C70 land two grid nodes apart; **C70 and C80 land on the
identical node**, so their absolute-period difference is reported as
exactly 0.000000° — a quantization artifact, not a measurement. The
ramp coefficient is not quantized at all. *(≈292 words)*

---

## 2. Parameter table — pairs, quantity, and functional form

### 2a. Data sources (all already committed; zero new FDTD)

| Series | Source | Rows |
|---|---|---|
| `C40(θ)`, `C80(θ)`, `delta_C80−C40(θ)` | `experiments/069-t21-block-mini-period-match-power-up/results.json` → `block_dense.rows` | 31 |
| `C60(θ)` | `experiments/071-t28-absorb-depth-causal-test/results.json` → `dense_causal.rows.C60` | 31 |
| `C70(θ)` | same file → `dense_causal.rows.C70` | 31 |
| absolute free periods (cross-reference only, **not** this cycle's discriminator) | same file → `per_config_free_periods` | 4 |

θ grid verified identical across all three sources: 36.0°–42.0°, 0.2° step,
31 points (checked programmatically, not by eye). Total 124 points.

### 2b. The estimator (fully specified, implementable)

Reuses `_fixed_period_fit` / `_free_period_search` from
`experiments/069-t21-block-mini-period-match-power-up/run.py`
**verbatim** (house convention: never re-derive existing machinery); the
ramped model is a 5-column extension of `_fixed_period_fit`'s own `lstsq`
idiom. All fits in `x = sin θ`, centered `u = x − x̄`, `center_deg=39.0`,
period reported in degrees via `T_x = radians(P°)·cos 39°`.

For each pair `(A,B)` with `B` the deeper `ABSORB`:

1. **Common-mode carrier.** `Cbar(θ) = ½(C_A+C_B)`. Free-period grid search
   (`_free_period_search` idiom, `[1°,4°]`, **`n_grid=3000`** — finer than
   exp-069's 400 solely to remove the 0.0075° quantization; a finer grid
   adds no resolution, only removes a discretization artifact) → `T_mean`,
   plus its in-phase/quadrature coefficients → carrier amplitude `a` and
   phase `ψ̄`.
2. **Ramped differential fit.** With `θ_c = 2πu/T_mean + ψ̄` held fixed from
   step 1, ordinary least squares of `delta_AB(θ)` on the 5-column basis
   `[1, cos θ_c, −sin θ_c, u·cos θ_c, −u·sin θ_c]`
   → coefficients `[c0, A_i, A_q, R_i, R_q]`. 31 points, 5 parameters,
   26 residual dof. Report the design matrix's condition number.
3. **Physical readout of each coefficient** (this decomposition is the
   proposal's actual instrument):

   | Coeff | Encodes | Interpretation |
   |---|---|---|
   | `A_i` (unramped, in phase) | `a_B − a_A` | oscillation **amplitude** differs with `ABSORB` |
   | `A_q` (unramped, quadrature) | `−a·Δψ` | constant **phase offset** between configs |
   | `R_q` (**ramped, quadrature**) | `2πa·Δf` | **frequency/period difference** — the target |
   | `R_i` (ramped, in phase) | amplitude drift across window | nuisance / model-strain indicator |

4. **Period difference.** `Δf = R_q/(2πa)`; `f̄ = 1/T_mean`;
   `ΔP_AB = −(Δf/f̄)·P_mean` in degrees, with `P_mean` the step-1 period.
   Standard error on `R_q` from the OLS covariance → propagated `SE(ΔP)`.
5. **Cross-check (disclosed, non-gating).** Free-period grid search on
   `delta_AB` alone → `T_delta`; model validity requires
   `|T_delta − T_mean|/T_mean ≤ 0.414` (one Rayleigh width, §2c).

### 2c. Does the 6°/31-point window resolve *this* quantity? — honest answer

Window in `x`: `X = sin42° − sin36° = 0.0813454`. Rayleigh frequency
resolution `Δf_min ≈ 1/X = 12.293`; at `P̄≈2.485°`, `f̄ = 29.67`, so the
**minimum resolvable fractional frequency separation is 41.4%**. C60 vs
C70 are 0.59% apart — 1.4% of Rayleigh. Confirms QUANTUM OPTICS: an
absolute-period discriminator is hopeless there, at any achievable window.

The differential quantity is *not* subject to that criterion — it is a
coefficient-detection problem, not a frequency-separation problem — but it
has its **own** power limit, which must be stated a-priori rather than
discovered post-hoc. Using Iteration 48's own linear slope
`m₀ = 0.00244361 °/cell` as the expected effect size, the predicted ramped
component as a fraction of common-mode amplitude is:

| Pair | Δ`ABSORB` | Δ`PAD` | Predicted `ΔP` | `ΔP/P̄` | `|Δf|·X` | **Predicted ramp / carrier amplitude** | A-priori expectation |
|---|---|---|---|---|---|---|---|
| C40–C60 | 20 | 20 | 0.0489° | 1.97% | 0.048 | **15.0%** | plausibly resolvable |
| C60–C70 | 10 | 10 | 0.0244° | 0.97% | 0.023 | **7.2%** | **likely underpowered** |
| C70–C80 | 10 | 10 | 0.0244° | 0.96% | 0.023 | **7.2%** | **likely underpowered** |
| C40–C80 | 40 | 40 | 0.0977° | 3.93% | 0.095 | **29.7%** | should resolve (T28's own founding pair) |

All four satisfy the linearization domain `|Δf|·X ≤ 0.25` by a wide margin,
so the small-angle expansion in §1 is valid throughout.

**Honest statement, pre-registered:** the differential estimator improves
conditioning by roughly an order of magnitude over the absolute-period
route, but for the two 10-cell steps the predicted signature is ~7% of
carrier amplitude, which against the residual scatter implied by the
per-config fits (`R²≈0.43–0.45`) is **not** confidently above the noise
floor. The most likely honest outcome of this cycle is that C40–C80 and
C40–C60 resolve and C60–C70 / C70–C80 do not. **Fallback rule, fixed in
advance:** for any pair failing the resolution gate (§5, P-072-2), the
report quotes the *sign* of `R_q`, its `SE`, and its surrogate p-value —
and **no fitted `ΔP`**. Unresolved pairs are excluded from P-072-4's rate
test and force P-072-3 to `NOT_EVALUABLE`. Quoting a period for an
unresolved pair is prohibited by this proposal.

---

## 3. Named-constant / parameter search — R5 applicability

**No named-constant or parameter search is involved.** There is no catalog
of candidate constants, no combinatorial space of `A_eff`-style
explanations, and no target value being matched. The procedure is a single
physically-motivated curve fit (a first-order expansion of the exact
difference of two sinusoids) applied to four pre-specified pairs; the only
continuum searched is the one-dimensional period grid `[1°,4°]`, which
prior cycles (exp-069, exp-071) already established does not trigger R5.
**LOGBOOK R5's ruled-out items are not re-proposed here**: `A_alt≈3·R_OUT`
and the `A_eff≈519` cluster appear nowhere in this design.

**However, a null control is adopted anyway**, because the "resolved"
claim rests on a coefficient significance test whose nominal `SE` assumes
independent residuals — false for structured FDTD residuals, and exactly
the failure mode that inflated exp-070's matches. Pre-registered, before
any computation:

- **Surrogates:** 20,000 Fourier-phase-randomized surrogates of
  `delta_AB(θ)` per pair (amplitude spectrum preserved exactly, phases
  drawn uniform with Hermitian symmetry enforced). This asks precisely the
  right question: is the *ramped-quadrature* structure special, or does
  same-spectrum noise produce it as readily?
- **Statistic:** `|R_q|`, recomputed on each surrogate through the identical
  step-2 fit at the identical `T_mean`, `ψ̄`.
- **p-value:** two-sided, `p = (1 + #{|R_q^surr| ≥ |R_q^obs|})/(N+1)`.
- **Seed:** `20490072`, fixed here, in this file, before any run.
- **Multiplicity:** Holm–Bonferroni across the 4 pairs. Adjusted p-values
  are what the §5 gates consume.

---

## 4. T1 escape route

**N/A — instrument/methodology work on live thread T28, not a T1 mechanism
proposal.** (Matches the prior desk-check-batch cycle, exp-070.) No
mechanism is offered as satisfying the phenomenon's four constraints;
constraint 3 is not engaged. **Checkpoint-criterion-2 candidacy: none** —
no mechanism class is bounded here, in either outcome.

---

## 5. Predictions — pre-registered, numeric, committed before any computation

### Gates

| ID | Gate | PASS | FAIL |
|---|---|---|---|
| **G0-a** (grid identity) | θ arrays from exp-069 `block_dense`, exp-071 `dense_causal.C60`, `.C70` are bit-identical, 31 points each | all three identical | any mismatch → **HALT** |
| **G0-b** (telescoping identity) | `delta_40_60 + delta_60_70 + delta_70_80 − delta_40_80 = 0` at every θ, as *raw series* (an arithmetic identity — this checks the loader, nothing physical) | `max|residual| ≤ 1e-12` | else **HALT** |
| **G0-c** (column provenance) | exp-069's committed `delta` column equals its own `C_empty_C80 − C_empty_C40` | `max|Δ| ≤ 1e-12` | else **HALT** |
| **G0-d** (conditioning) | condition number of the 5-column design matrix, each pair | `cond ≤ 100` | `cond > 100` → that pair reported `ILL_CONDITIONED`, excluded from all gates |

### Scored predictions

**P-072-1 — descriptive, disclosed, not gated.** Full per-pair table:
`T_mean`, `P_mean`, `a`, `ψ̄`, `T_delta`, `c0`, `A_i`, `A_q`, `R_i`, `R_q`,
`SE(R_q)`, `Δf`, `|Δf|·X`, `ΔP`, `SE(ΔP)`, raw and Holm-adjusted surrogate
p, plus the four-coefficient physical decomposition of §2b step 3.
Published **for all four pairs regardless of every other outcome.**

**P-072-2 — (a) does the differential instrument resolve structure, and
where?** Per-pair `RESOLVED` ⟺ all three of:
Holm-adjusted `p ≤ 0.01`; **and** linearization gate `|Δf|·X ≤ 0.25`;
**and** carrier-consistency `|T_delta − T_mean|/T_mean ≤ 0.414`.

- **CONFIRM** ⟺ C40–C80 `RESOLVED` **and** C40–C60 `RESOLVED` **and** at
  least one of {C60–C70, C70–C80} `RESOLVED` (i.e. ≥3 of 4, including at
  least one 10-cell step that the absolute-period method provably cannot
  resolve — the instrument beats its predecessor).
- **REFUTE** ⟺ **zero** pairs reach even the relaxed Holm-adjusted
  `p ≤ 0.10` — including C40–C80, the pair where T28 was originally found
  at `ptp/mean=16.2`. That would refute the differential/beat framing as an
  instrument in this window, not merely leave it undecided.
- **NEITHER** ⟺ anything else. **This includes the a-priori-most-likely
  outcome** (both wide pairs resolve, both 10-cell steps do not), and it is
  reported as a real, quantitative finding — "the differential estimator
  extends reach from 40 cells to 20 cells of `ABSORB` step but not to 10" —
  never as a silent PARTIAL escape hatch.

**P-072-3 — closure (the design's strongest internal falsifier).**
`S = ΔP(40→60) + ΔP(60→70) + ΔP(70→80)`; `D = ΔP(40→80)`.
`ρ_c = |S − D| / max(|D|, 0.005°)`.
*Note:* the raw series telescope by arithmetic (G0-b), but the recovered
`ΔP` estimates do **not** — each pair is fit at its own `T_mean`, `a`, `ψ̄`,
so closure is a genuine, non-trivial test of the model's linearity and of
the common-mode-cancellation assumption.

- **CONFIRM** ⟺ `ρ_c ≤ 0.25` **and** `sign(S) = sign(D)`.
- **REFUTE** ⟺ `ρ_c ≥ 1.00`, **or** `sign(S) ≠ sign(D)` with both
  `|S| ≥ 0.010°` and `|D| ≥ 0.010°`.
- **NOT_EVALUABLE** ⟺ any of the three adjacent pairs is not `RESOLVED`
  (per the §2c fallback rule — no `ΔP` exists to sum).
- **NEITHER** ⟺ `0.25 < ρ_c < 1.00` with all pairs resolved.

**P-072-4 — (b) is the recovered differential structure consistent with
Iteration 48's established `ABSORB`-depth trend, or new?** Over `RESOLVED`
pairs only (≥2 required); per-pair rate `r = ΔP/Δ ABSORB`; reference
`m₀ = 0.00244361 °/cell` (Iteration 48's own linear slope, R²=0.8664).

- **CONFIRM (consistent, corroborates Iteration 48)** ⟺ every resolved pair
  has `ΔP > 0` **and** every resolved pair's `r ∈ [m₀/3, 3m₀] =
  [0.000815, 0.007331] °/cell`.
- **REFUTE (new structure — trend is not a smooth monotone ramp)** ⟺ any
  resolved pair has `ΔP < 0` with `|ΔP| ≥ 0.010°` (a genuine sign
  reversal, i.e. non-monotonic `ABSORB` dependence, not a null wobble),
  **or** any resolved pair's `r` falls outside
  `[m₀/10, 10m₀] = [0.000244, 0.024436] °/cell`.
- **NEITHER** ⟺ anything else, **or** fewer than 2 pairs resolved.

**P-072-5 — wrong-carrier control (disclosed, non-gating).** The window
contains at least two oscillatory contributors (T21's established
`P(39°,600nm)=1.9608°` fringe and the ~2.5° family). Re-run steps 1–4 with
`T` **fixed** to T21's 1.9608° instead of the free `T_mean`. If `|R_q|`
and its surrogate p are comparable at the wrong carrier, the single-carrier
decomposition is contaminated and the P-072-1 readouts must be read as
model-strained. Reported in full; does not enter the Combined Verdict, but
is mandatory disclosure alongside any CONFIRM.

**P-072-6 — amplitude-vs-phase-vs-frequency disclosure (non-gating).**
Report `|A_i|/a`, `|A_q|/a`, `|R_q|·σ_u/a` per pair. If the `ABSORB` step's
dominant effect is an amplitude change (`A_i`) or a constant phase offset
(`A_q`) rather than a frequency change (`R_q`), that is itself a
substantive T28 finding and must be stated as such, not buried.

### Combined Verdict — pre-committed, computed in code, evaluated in this order

1. **HALT** ⟺ any of G0-a/b/c FAIL. Nothing else is scored; the reused data
   is not trusted this run.
2. **REFUTED** ⟺ gates PASS **and** (P-072-2 REFUTE **or** P-072-3 REFUTE).
   Reading: the differential/beat framing buys nothing over the absolute
   one in this window, or its own internal closure fails — the instrument,
   not T28, is what is refuted.
3. **CONFIRMED** ⟺ gates PASS **and** P-072-2 CONFIRM **and** P-072-3
   CONFIRM **and** P-072-4 CONFIRM. Reading: the differential estimator
   resolves a consistent, `ABSORB`-step-proportional period shift on the
   already-collected 124 points, including at a step the absolute-period
   method provably cannot resolve, and its three adjacent estimates close
   on the independently-measured endpoint pair.
4. **NEITHER** ⟺ everything else — explicitly enumerated in the results
   JSON with the branch that fired, published with the complete P-072-1
   per-pair table, the P-072-5 wrong-carrier control, and the P-072-6
   decomposition attached. Per house discipline (exp-069's VISION catch,
   exp-071's own NEITHER), this is a reported finding with its own
   sentence — "the differential instrument reaches X and not Y, and here is
   the measured noise floor that stops it" — not a deferral.

All bands above are raw and independent, exactly as exp-071's were: each is
evaluated on its own pre-registered threshold, and the Combined Verdict is
a fixed boolean function of those outcomes. No threshold may be revised
after any number is computed.

---

## 6. Idealizations

1. **600nm only.** T28's entire evidential base, and every datum reused
   here, is at 600nm. A CONFIRM at 600nm licenses **no** wavelength-general
   mechanism claim — a period difference that scales with `ABSORB` at one
   wavelength says nothing yet about its dispersion. Matching exp-071's own
   mandatory caveat, restated here without softening.
2. **The `ABSORB`/`PAD` compound-axis confound is NOT relieved by this
   analysis.** `PAD = ABSORB − 40` holds exactly at all four configs
   (Iteration 48's Red-Team-confirmed finding), so every pair analyzed here
   steps `ABSORB` and `PAD` together — 20/20, 10/10, 10/10, 40/40 cells.
   The differential framing changes the *estimator*, not the *design*: it
   cannot decorrelate what the congruent series never varied
   independently. **Any CONFIRM from this cycle must be written as
   "`ABSORB`-or-`PAD`-tied", never "`ABSORB`-tied."** A PAD-decorrelated
   config remains separately queued and is not this cycle's job. Stated
   plainly here so that the sharper instrument does not lend spurious
   specificity to a confounded axis.
3. **`ABSORB` is not a material.** It is a numerical
   boundary-condition parameter (graded-absorption depth in cells). No
   result from varying it licenses any realizability or physical-medium
   claim; it is an instrument parameter of the solver, and a dependence on
   it is at least as likely to be a boundary artifact as a physical effect.
4. **Single-carrier model.** The estimator assumes each config's response
   is one sinusoid plus noise, with the two configs sharing amplitude and
   phase up to the small differences being estimated. The window demonstrably
   contains ≥2 contributors (T21's 1.9608° fringe coexists with the ~2.5°
   family; per-config fits reach only `R²≈0.43–0.45`). P-072-5 measures the
   contamination but does not remove it.
5. **`~2.4 periods` of carrier in the window.** Not asymptotic; edge
   effects on the ramp coefficient are real and are exactly what the
   surrogate null is there to calibrate.
6. Free-period grid refined to `n_grid=3000` (from exp-069's 400) removes a
   0.0075° quantization artifact — it **adds no resolving power**, and the
   Rayleigh limit of §2c is untouched by it.
7. 2D TMz, single polarization; positive-θ branch only (36°–42°) — not a
   symmetry test; single-angle `C_empty` readings, not an N9/N17 aggregate
   (T25/T26 do not apply); bench scale only (`R_OUT=78` cells) — no
   witness-scale claim.
8. No new FDTD means no new identity gate against the engine; trust in the
   underlying numbers is inherited from exp-069's and exp-071's own
   already-passed G1 identity gates, settling checks, and peak-cell R3
   resolution checks. This cycle adds arithmetic-integrity gates (G0-a/b/c)
   only, and inherits — it does not re-establish — engine trust.
9. Statistical power is estimated a-priori in §2c from Iteration 48's own
   slope. If the true effect is smaller than that slope implies, the
   underpowered set is larger than the two pairs named. The pre-registered
   fallback (report sign and p, quote no period) covers that case.

---

## 7. Budget

**Zero new FDTD calls. Desk-only, pure arithmetic over already-committed
JSON.** No `lab/` diff; `lab/validation/VALIDATION.md` re-run not triggered
(no engine change). Inputs: 124 already-committed data points from two
existing `results.json` files.

Cost: 4 pairs × (1 grid search at `n_grid=3000` on 31 points + one 5-column
`lstsq`) + 4 × 20,000 surrogate refits (each a 31×5 `lstsq`, vectorizable
via a single precomputed pseudo-inverse since `T_mean`/`ψ̄` are held fixed
across surrogates) + the P-072-5 wrong-carrier repeat.

**Estimated wall-clock: < 60 s single-core**, dominated by the 80,000
surrogate fits; the fits themselves are seconds. Deliverables:
`run.py`, `results.json`, `phase4_results.md`, `NOTES.md` in
`experiments/072-t28-differential-beat-fit/`.
