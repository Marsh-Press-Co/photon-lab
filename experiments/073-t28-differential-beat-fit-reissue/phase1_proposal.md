# PHASE 1 — PROPOSE · Panel Iteration 50 · exp-073
## MATERIALS' corrected re-issue of exp-072's differential/beat fit of `delta_AB(θ)` (T28), behind `G0-e`

*Fresh sub-agent, MATERIALS & METAMATERIALS charter (PANEL.md seat:
sub-wavelength structure; what could physically realize the proposed
optical behavior; owns the realizability bound), lead by rotation. Executes
PLAN.md's Iteration-50 queue item 1, unanimous across all six of exp-072's
Phase-5 seats (`experiments/072-t28-differential-beat-fit/
phase5_redteam_audit.md` §7.2: PHOT #1, MAT D1, EM #1, THERMO #2, QUANTUM
#1, VISION #2 — full convergence, no dissent).*

## Mandate (Iteration-50 queue, item 1, verbatim)

> A corrected zero-FDTD re-issue of exp-072's own differential/beat-fit
> instrument, behind the new `G0-e` ground-truth recovery gate — nothing
> downstream of exp-072's own step 2 is fully clean until this lands as a
> freshly pre-registered cycle (the contamination ruling's own condition 3
> explicitly contemplates this); folds in EM's `A_q = 2a_cbar·tan χ` table
> correction, QUANTUM's sign-flip/residual-permutation null replacing the
> phase-randomised H₀-residual one, and VISION's reinstated sign-invariance
> admissibility condition over the gate-admitted carrier set (all deferred
> from exp-072's own same-shift docket as new-gate additions, not
> same-shift-safe).

`phase5_redteam_audit.md` §7.2 names this cycle `exp-073` explicitly: *"1.
`exp-073` — the corrected re-issue, behind `G0-e`. Zero FDTD. Unanimous.
This is the Tier-1 docket executed as a **clean, uncontaminated
pre-registration**, which the contamination ruling's own condition 3
explicitly contemplates. Every fix in it is justified by a data-free
argument, so it retires the contamination question rather than re-opening
it."*

---

## 0. What this document is, and is not

This is not a new mechanism proposal. It is a fresh pre-registration of an
already-sound estimator whose prior instance (exp-072) was found, at its
own Phase 5, to have shipped a carrier-phase sign bug that rotated every
published coefficient by a nuisance parameter — caught by three independent
seats using three different methods, fixed, and verified — and to have been
observed mid-critique by two seats before its own Phase-3 commit, which
Red Team's own contamination ruling (exp-072 `phase2_redteam_audit.md` §4,
condition 3) states can only be retired by a fresh cycle, not by further
correction of the same one.

**Every design choice below is justified by an argument that does not
reference exp-072's own observed `p`-values, `ΔP` signs, `R_q` magnitudes,
or which pairs came out significant.** Where a number from exp-072 appears
below, it is either (a) a data-free structural/geometric fact (window
width, Rayleigh limit, a leakage-minimization derivation, an algebraic
identity), (b) a previously-closed, non-contaminated finding from an
**earlier** cycle (exp-071's own published `ABSORB`-depth causal-test
slope, Iteration 48 — closed before exp-072 existed), or (c) explicitly
flagged as inherited **machinery** (a formula, a basis, a threshold
derivation) rather than an inherited **result**. §3 below states, item by
item, which of these three classes each design choice belongs to.

The substrate is unchanged: the 124 already-collected `C40`/`C60`/`C70`/
`C80` points at `θ ∈ [36°,42°]`, 0.2° step, 600nm, from `experiments/069-.../
results.json` and `experiments/071-.../results.json`. Zero new FDTD calls.

---

## 1. Design narrative (≤300 words)

T28's `C80−C40` periodicity is real, resolution-robust, settled, and lives
in each config individually (Iterations 46–47); it climbs with `ABSORB`
depth at Iteration 48's original grid resolution, but that framing does not
survive a finer free-period grid (the `n_grid=400→3000` refinement reverses
the `C70`/`C80` order — a resolution artifact of the search, not the
physics, disclosed and inherited unchanged below). QUANTUM OPTICS
established (exp-071 Phase 5) that the 6°/31-point window supplies under
10% of the Rayleigh resolution needed to separate `C60`'s and `C70`'s
absolute periods. exp-072 built the correct answer to that problem —
differencing adjacent configs converts an unresolvable absolute-frequency
question into a well-conditioned coefficient-detection problem at the
window's own well-resolved common-mode carrier — and that instrument's
derivation was independently re-verified line by line at exp-072 Phase 2
and Phase 5 and found sound. What failed was not the idea; it was one sign
convention in one function, present for one cycle, caught one phase later
than it should have been.

exp-073 re-runs the same idea with three concrete changes: (i) the null the
`RESOLVED` gate is scored against is rebuilt so that, unlike exp-072's own
phase-randomized H₀-residual null, it cannot leave the tested signal inside
its own reference distribution; (ii) a `RESOLVED` finding must hold its
sign across every carrier the data admit as consistent, not just the one
the estimator happens to condition on; (iii) the one coefficient-table
entry exp-072 shipped with a wrong small-angle approximation is corrected
to its exact form. All three are provable from formulas alone. A fourth
change is process, not physics: a synthetic-ground-truth recovery gate
(`G0-e`, LOGBOOK R6) must pass, and now also calibrate its own new null,
before a single real point is scored. *(≈290 words)*

---

## 2. Parameter table

### 2a. Data sources (unchanged from exp-072; zero new FDTD)

| Series | Source | Rows |
|---|---|---|
| `C40(θ)`, `C80(θ)`, `delta_C80−C40(θ)` | `experiments/069-t21-block-mini-period-match-power-up/results.json` → `block_dense.rows` | 31 |
| `C60(θ)` | `experiments/071-t28-absorb-depth-causal-test/results.json` → `dense_causal.rows.C60` | 31 |
| `C70(θ)` | same file → `dense_causal.rows.C70` | 31 |
| `m₀` (OLS slope, loaded at runtime, never typed) | same file → `trend.linear_fit.slope` | scalar |
| Per-config free periods (context only; class (b), closed Iteration 48) | same file → `per_config_free_periods` | 4 |

θ grid re-verified bit-identical across all three sources at Phase 3 before
any fit — inherited gate, see G0-a below. Total 124 points, unchanged.

### 2b. The estimator (inherited machinery — class (c), re-derived here, not re-observed)

Every item below was independently re-derived from first principles at
exp-072 Phase 2 or Phase 5, confirmed by at least two seats and Red Team's
own re-implementation, and holds regardless of what any pair's `R_q`
happens to measure. All fits in `x = sinθ`, centered `u = x−x̄`,
`center_deg = 39.0`.

1. **Common-mode carrier.** `Cbar(θ) = ½(C_A+C_B)`. Free-period grid search,
   `[1°,4°]`, `n_grid=3000` (fine enough to remove the 0.0075° node-collision
   quantization that reversed `C70`/`C80`'s order at `n_grid=400` — adds no
   resolving power, only removes a discretization artifact) → `T_mean`, and,
   fitting amplitude/phase **directly in `u`-space** (the Phase-3 self-catch
   from exp-072: no residual `w·x̄` shift may be introduced by fitting in raw
   `sinθ` and reusing the phase downstream), the common-mode amplitude
   `a_cbar` and phase `ψ̄`.
2. **Ramped differential fit.** With `θ_c = 2πu/T_mean + ψ̄` fixed from step
   1, OLS of `delta_AB(θ)` on the **frozen** 5-column basis
   `[1, cosθ_c, −sinθ_c, u·cosθ_c, −u·sinθ_c]` → `[c0, A_i, A_q, R_i, R_q]`.
   31 points, 5 parameters, 26 residual dof. This exact sign convention —
   not `[1,cosθ_c,sinθ_c,u·cosθ_c,u·sinθ_c]` — is the one exp-072's own
   Director-derived, Red-Team-verified fix confirmed recovers known
   synthetic `ΔP` at `+1.0000 ± 0.0007`; the un-negated version returns
   exactly `−cos(2ψ̄)` of the true value. **This basis is not re-derived by
   this cycle; it is inherited as a settled fact, class (c).**
3. **Exact physical readout** (Red Team's re-derivation, exp-072 Phase 5
   `phase5_review_em.md` §1a, algebraically exact, not a small-angle
   approximation):

   ```
   delta_AB = δa·cosΘ − 2·a_cbar·sin(χ₀ + πΔf·u)     [+ O(δa·χ) cross term]
   Θ = 2πf̄·u + ψ̄          χ₀ = πΔf·x̄ + Δψ/2
   ```

   | Coeff | Exact relation | Interpretation |
   |---|---|---|
   | `A_i` | `a_B − a_A` | amplitude difference between configs |
   | `A_q` | **`2·a_cbar·tan χ₀`** | half the phase difference at window centre (`χ₀ = arctan(A_q/2a_cbar)`) |
   | `R_q` | `2π·a_cbar·Δf` | the target — period/frequency difference |
   | `R_i` | first-order-zero; nonzero values are model-strain | nuisance / model-strain indicator |

   `Δψ` (the θ=0° extrapolation, ≈26 `σ_u` outside the window) **may not be
   quoted anywhere in any deliverable** — reported only as `|A_q|/a_cbar`,
   never inverted to a phase at window centre in absolute degrees.
4. **Period difference.** `Δf = R_q/(2π·a_cbar)`; `ΔP = −(Δf/f̄)·P_mean`.
   `SE(ΔP)` propagated from a **design-respecting** bootstrap: resample the
   5-column ramp-fit residual *and*, independently, the common-mode
   carrier-fit residual, refitting the free period and phase from step 1 on
   every draw (not a case-resampling bootstrap on the deterministic 31-point
   design grid — exp-072 Phase 5 confirmed by three independent seats that
   case resampling on a fixed design measures the resampling scheme, not the
   instrument). Also report `dR_q/dψ̄` — an **exact algebraic identity of
   the rotation, `≡ R_i`**, not a separate computation — and `|R_i/R_q|`.
5. **Cross-check (disclosed, non-gating).** Free-period grid search on
   `delta_AB` alone → `T_delta`.

### 2c. Does the window resolve *this* quantity? — a-priori power, corrected `m₀`

Window in `x`: `X = sin42° − sin36° = 0.0813454`; Rayleigh floor 41.4%
fractional frequency separation (class (a), pure geometry — unchanged from
exp-072). `m₀` is exp-071's own committed least-squares slope of the
`ABSORB`-depth trend, `0.0025563909774436134` — **not** exp-072's own
Phase-1 draft figure of `0.00244361`, which Red Team's audit found (exp-072
`phase2_redteam_audit.md` Attack 5) was actually the C40→C80 two-point
endpoint chord, mislabeled with the least-squares fit's own R². `m₀` is
class (b): closed at Iteration 48, before exp-072 existed, and **must be
loaded from the JSON at runtime — never typed into `run.py` or this
document as a constant** (the R4 lesson, twice-learned on this exact
number).

Using the corrected `m₀` against the Iteration-48-published per-config free
periods (class (b), also closed before exp-072):

| Pair | ΔABSORB | Predicted ΔP = m₀·ΔABSORB | ΔP/P̄ | Predicted ramp/carrier (`≈π·|Δf|·X`) | A-priori expectation |
|---|---|---|---|---|---|
| C40–C60 | 20 | 0.0511° | 2.06% | **≈16%** | plausibly resolvable |
| C60–C70 | 10 | 0.0256° | 1.01% | **≈7.5%** | likely underpowered |
| C70–C80 | 10 | 0.0256° | 1.01% | **≈7.5%** | likely underpowered |
| C40–C80 | 40 | 0.1023° | 4.11% | **≈31%** | should resolve (T28's founding pair) |

(Recomputed here for planning purposes only, from `m₀` and public window
geometry; `run.py` computes its own from the runtime-loaded value and does
not reuse these printed numbers.) The qualitative shape — two pairs
plausibly resolvable, two likely not — is unchanged from exp-072's own
a-priori read and is **not** an outcome-dependent claim: it follows from
`m₀` and `X` alone, both fixed before this pair of pairs was ever fit.
**Unchanged pre-registered fallback:** any pair failing the resolution gate
reports sign, `SE`, and surrogate `p` only — never a quoted `ΔP`.

---

## 3. What changed vs exp-072, and why each change is data-free-justified

Per item, tagged by evidentiary class: **(a)** pure structural/geometric
fact computable with zero data; **(b)** a previously-closed, non-
contaminated finding from a cycle that predates exp-072; **(c)** inherited
machinery (a formula or threshold derivation, re-verified from first
principles, not from an exp-072 observation).

### 3a. Inherited unchanged (class c — verified sound, not re-derived)

- The frozen 5-column basis and its sign convention (§2b.2).
- `R_q = 2π·a_cbar·Δf`, `A_q = 2·a_cbar·tan χ₀` (§2b.3) — the `tan`, not
  `sin`, form is EM's exact re-derivation (exp-072 `phase5_review_em.md`
  §1a), algebraically forced by the definition of `a_cbar` as the common
  mode of two detuned tones (`a_cbar = a_cfg·cosχ₀`); it is **not** an
  empirical correction, it is a trigonometric identity. Numerically
  outcome-inert in exp-072's own regime (`|A_q|/2a_cbar` small enough that
  `tan≈sin` to <0.5%, per Red Team's O-6 ruling) but binds hard exactly
  where this design's own predicted effect sizes (§2c: `χ₀` order 0.5–1.2
  rad at the two wide pairs) put it — a ~2.6× discrepancy factor at
  `χ₀≈1.2` rad, computed from the exact identity, not from any exp-072
  reading.
- The design-respecting bootstrap for `SE(ΔP)` (§2b.4), replacing a
  case-resampling scheme shown (three independent seats, exp-072 Phase 5)
  to measure the resampling procedure rather than the instrument on a
  deterministic design grid — a statistical-methodology argument, true for
  any data this exact 31-point grid could carry.
- `dR_q/dψ̄ ≡ R_i` — an algebraic identity of the OLS rotation, true for any
  data.
- The wrong-carrier comparator, `T_wrong = 1.2591°`, replacing exp-072's own
  first-draft `3.60°`. Both the value and its justification are class (a):
  `3.60°` sits at only 0.70–0.75 Rayleigh widths of displacement and within
  1–2% of the global maximum of the leakage function `|L(T)|` (a
  zero-free-parameter calculation of how strongly a unit-amplitude
  component at period `T` projects onto `R_q` through this exact 31-point
  design — computable with no data at all); `1.2591°` gives ≥2.36 Rayleigh
  widths of displacement and a leakage value 36× smaller, the
  leakage-minimizing choice inside the `[1°,4°]` search range. Neither
  number references any pair's observed `R_q`.
- The Holm–Bonferroni multiplicity structure: adjust across the three
  algebraically-free pairs (`C40–C60`, `C60–C70`, `C70–C80`); report
  `C40–C80`'s `p` unadjusted and explicitly labelled *derived* — because
  `delta_C40–C80 ≡ delta_C40–C60 + delta_C60–C70 + delta_C70–C80` at every
  θ, bit-exactly, an arithmetic identity of how the four series were
  constructed (verified as gate G0-b, below), true before any fit is run.
- REFUTE placed behind a demonstrated-power precondition (an
  injection-recovery test scored at Holm-adjusted `p≤0.01` on a **known**,
  H₀-clean-base injected effect) — a statistical-methodology argument
  (a null result cannot be trusted from an instrument that has not first
  been shown able to detect a known effect of the predicted size) that
  holds regardless of what this cycle's real data show.
- The dual linear/saturating scoring of `ABSORB`-depth-trend consistency,
  with the rate-window clause demoted to disclosed and only the
  sign-reversal clause (`ΔP<0` with `|ΔP|≥0.010°`) gating — justified
  because `m₀` is shown (class b, Iteration 48's own resolution-sensitive
  node collision) to be an unreliable band anchor at the precision this
  gate would otherwise demand, independent of what exp-073's own `ΔP`
  values are.
- The `ABSORB`-or-`PAD`-tied writing rule (§6, Idealization 2), the
  "`ABSORB` is not a material" caveat (§6, Idealization 3), and "graded
  damping mask" as the house term for the boundary parameter — all
  disclosure conventions, none conditioned on any observed value.
- `ρ_c`, the closure statistic, is **reframed** (not merely inherited) per
  Red Team's own constructive finding (exp-072 `phase5_redteam_audit.md`
  RT-1): at a literal **common** carrier, closure is an algebraic identity
  (`ρ_c ≡ 0` to machine precision, forced by G0-b plus OLS linearity on a
  fixed design) and therefore uninformative by construction — a fact
  provable with zero data. `ρ_c` is measured, as before, at each pair's own
  independently-fit `T_mean` — the only construction under which it
  measures anything (carrier-choice sensitivity, not "basis stability" —
  see §5, P-073-3). The common-carrier identity is retained only as a
  disclosed sanity check that must read `≡0`, never scored.

### 3b. New this cycle (the mandate's own three folded items, all class a/c)

- **T2-3 — QUANTUM's sign-flip/residual-permutation null, replacing the
  phase-randomized H₀-residual null.** exp-072's own restricted null
  phase-randomized the **4-column H₀-fit residual** (`resid0 = delta_AB −
  yhat0`, `yhat0` from the ramp-free basis `[1,cosθ_c,−sinθ_c,u·cosθ_c]`).
  That residual still contains any true ramp signal
  `R_q·(u·(−sinθ_c))` — the H₀ fit, by construction, cannot remove a
  component it does not include — so phase-randomizing it scrambles real
  signal into the null's own variance: conservative at large effect sizes,
  not a clean test of `H₀: R_q=0`, a defect proven from the basis
  definitions alone (exp-072's own author, QUANTUM, raised this against its
  own Phase-2 proposal at Phase 5, argued from the algebra, not from any
  observed `p`). The fix (Freedman–Lane-style, standard nonparametric
  regression-permutation practice): compute the **5-column (full model)
  residual** `resid5 = delta_AB − ŷ5` — which, by construction, has the
  ramp component fit out regardless of its true size — sign-flip it
  (Rademacher ±1, i.i.d. per point) **or** permute its order, add the
  surrogate back to `yhat0` (the H₀-fit prediction), refit the 5-column
  model on the surrogate, and take `|R_q^surr|` as the statistic. This null
  is generated *under* `H₀: R_q=0` exactly (the surrogate's own `E[R_q]=0`
  by construction, since `yhat0 ∈ span(X4) ⊂ span(X5)` — verified in
  exp-072 Phase 2 for the phase-randomized case and true identically here),
  which the phase-randomized construction is not. **Primary gating null,
  N=20,000 draws (sign-flip), seed fixed below, before any pair is scored.
  Residual-permutation is run as a disclosed cross-check, not a second
  gate**, to avoid re-introducing exp-072's own "which of two nulls
  decides the verdict" ambiguity (Attack 1) — one null gates, one null is
  reported alongside it.
- **T2-1 — VISION's reinstated sign-invariance admissibility condition.**
  `RESOLVED` now additionally requires `sign(ΔP)` to agree across every
  member of the **gate-admitted carrier set**
  `{T_mean, T_delta, T_wrong=1.2591°}` that also independently passes that
  pair's own per-pair carrier-consistency gate (item below, §5 G-gate
  table) — i.e. a carrier only enters the admissibility test if the data
  themselves certify it consistent with the common-mode fit; a carrier the
  gate would reject is not counted against sign invariance, and its
  exclusion is disclosed. This is a strictly better-motivated set than
  exp-072's own first-draft `{T_mean, T_delta, 1.9608°}`: `1.9608°` (T21's
  fringe) sits at only 0.645 Rayleigh widths and is a **resolution
  identity**, not an independent carrier (exp-072 Phase 2 Attack 9,
  algebra-only) — a correct measurement is not obliged to agree with itself
  measured at a period the design cannot separate from its own; `1.2591°`
  is a genuinely displaced (≥2.36 Rayleigh widths), leakage-minimizing
  comparator, so requiring sign agreement with it is a real test, not a
  gate rigged to fail (Red Team's Attack 10 ruling on exactly this
  distinction). The set, its ordering, and the ≥1-Rayleigh-width admission
  rule are fixed here, before any pair is fit.
- **T2-4 — the `A_q = 2a_cbar·tan χ` correction.** Already folded into §2b.3
  and §3a above as inherited machinery — restated here because the mandate
  names it explicitly. It is fixed in the coefficient table *before* any
  successor (this cycle) quotes a phase channel, per Red Team's own O-6
  ruling (exp-072 `phase5_redteam_audit.md` §272).
- **T2-2 — THERMO's ψ-marginalized gating statistic, `‖R‖ =
  √(R_i²+R_q²)`, published as disclosure, not conflated with the primary
  gate.** `‖R‖` is rotation-invariant — the one analysis in exp-072's
  entire Phase-5 record the sign bug never touched — and tests a
  **different** null, `H₀: R_i=R_q=0`, not a corrected version of the
  pre-registered `H₀: R_q=0`. It is reported in P-073-1 and P-073-5 with
  its own sign-flip-null significance (computed by projecting the same
  N=20,000 sign-flip surrogates onto `√(R_i²+R_q²)`, at zero extra
  simulation cost), explicitly labelled *"a different hypothesis, not a
  substitute for or a relaxation of `RESOLVED`."*

### 3c. Explicitly out of scope, with reasons (not this cycle's job)

- **T2-5 — PHOTONICS' second-tone measurement (1.824–1.837°).** Ruled
  UNQUOTABLE without its own null-permutation control (R5 / Iteration-47
  look-elsewhere discipline: a free-period search on a residual, over the
  same governed `[1,4]°` continuum, on the same 31 points R5 already
  governs). Not attempted here; a future cycle's job.
- **T2-6 — MATERIALS' own G40/`PAD`-decorrelation cost revision** (~31
  calls if the geometry-reuse claim verifies against `experiments/065-.../
  design_geometry_output.txt`). This is PLAN's separate Iteration-50 queue
  item 3, a **new FDTD build**, not a re-analysis of already-collected
  points — orthogonal to this cycle by construction (zero-FDTD mandate) and
  explicitly not folded in per the Director's own scoping instruction. It
  remains the cheapest confound relief on the board and stays queued.
- **Window pricing (queue item 2) and window extension to `θ_max≈46°`
  (queue item 4).** Both are legitimate next moves — EM's Cramér–Rao
  pricing and QUANTUM's `L(T)` leakage budget can decide, at zero FDTD
  cost, whether 36°–42° can ever support a carrier-conditioned
  discriminator at all, and a widened window is the only change that
  attacks the resolution problem at its cause rather than its symptom —
  but they are ranked **after** this item in the Iteration-50 queue
  precisely because a clean re-issue must land first (nothing downstream of
  exp-072's own step 2 is readable until it does). Not this cycle's
  mandate.
- **Mask-functional-form ablation (queue item 3-subordinate).** Orthogonal,
  carries no `PAD` confound by construction, but per Red Team's own ruling
  belongs inside whichever window a future cycle settles on, not this one.

---

## 4. `G0-e` — the ground-truth recovery gate (R6, mandatory, sharpened)

LOGBOOK R6 (adopted Iteration 49, on the R4 model): *"any future estimator
that conditions on a fitted carrier or phase parameter must ship a
pre-registered synthetic ground-truth recovery test — inject a KNOWN effect
at a swept nuisance-parameter value, HALT unless recovered/true is within a
stated tolerance — before any real data is scored."* exp-072's own post-fix
`G0-e` is the template: synthetic congruent pairs on the real 31-point θ
grid, `A=a·cos(2πu/T_A+ψ₀)`, `B=a·cos(2πu/T_B+ψ₀)`, `T_A=2.49°`,
`ΔP∈{±0.005,±0.01,±0.02,±0.04,±0.08}`, `ψ₀` swept over 16 phases in
`[0,2π)`, pushed through the committed `carrier_fit → design_matrix →
delta_P_obs` chain; HALT unless `|ΔP_est/ΔP_true−1|≤0.02` at every cell.
Verified at exp-072: the corrected chain passes at worst-cell error
0.00069 (0.069%, comfortably inside the 2% bar); the pre-fix chain fails,
returning exactly `−cos(2ψ₀)`.

exp-073 reuses this test's tolerance unchanged (2% is an already-validated,
sufficiently strict bar — sharpening it further buys nothing) and sharpens
it on two axes that are each necessary given this cycle's own new
machinery, both fully specified here, before any real pair is fit:

### G0-e(i) — recovery accuracy, widened coverage

- **Synthetic ground truth:** congruent pairs `A=a·cos(2πu/T_A−ψ₀)`,
  `B=a·cos(2πu/T_B−ψ₀)` on the real 31-point θ grid (`u=sinθ−x̄`, matching
  the real data's own centering exactly).
- **Sweep:** `T_A ∈ {2.40°, 2.49°, 2.55°}` (three carrier periods bracketing
  the public, Iteration-48-published per-config period range 2.4361°–
  2.5338°, without using any of those four values directly — a deliberate
  design choice so `G0-e` is not silently tuned to the real fitted
  carriers); `a ∈ {0.002, 0.005, 0.01}` (three amplitudes spanning a
  plausible small-signal range for this field-ratio channel, chosen for
  coverage, not fit to any observed amplitude); `ΔP ∈
  {±0.005,±0.01,±0.02,±0.04,±0.08,±0.10}` (six magnitudes, widened from
  exp-072's five to bracket §2c's own predicted range, 0.026°–0.102°, on
  both sides); `ψ₀` over 32 phases in `[0,2π)` (doubled from 16, to halve
  the angular sampling step of the one nuisance parameter this entire
  correction cycle exists because of). Total: 3×3×6×32 = 1,728 cells,
  pushed through the corrected, frozen chain (§2b, §3a).
- **Tolerance, HALT rule:** unchanged, `|ΔP_est/ΔP_true−1| ≤ 0.02` at
  **every** cell; worst-cell error persisted to `results.json` as
  `g0e.worst_abs_ratio_error`. **HALT the entire cycle — no pair is scored —
  if any cell exceeds 2%.**
- **Two cheap assertion tripwires, carried forward from exp-072's own T1-2**
  (both class (c), formula-derived, not data-derived): `dR_q/dψ̄` must equal
  `R_i` to within 1e-6 at every synthetic cell (the algebraic identity of
  §3a); `A_i` must match the directly-constructed `a_B−a_A` to within 1% at
  every cell where `|a_B−a_A|≥1e-4`.

### G0-e(ii) — null calibration (new; the reason `G0-e` must be sharpened, not just re-run)

T2-3's entire justification is that the sign-flip null is *correctly
calibrated* under `H₀: R_q=0` where the phase-randomized one was not. That
claim is itself testable with zero real data, and R6's own text — *"before
any real data is scored"* — reads naturally as covering the null
construction, not only the point estimator. exp-073 adds that test as part
of `G0-e`, not as a separate gate, so that a single named HALT covers both
failure modes this design's own new machinery could have.

- **Synthetic null data:** pure noise on the real 31-point θ grid,
  `y = ε`, `ε ~ N(0, σ²)` i.i.d., **zero ramp signal** (`ΔP_true=0`
  identically) — the sign-flip null's own textbook target case.
- **Sweep:** `σ ∈ {0.0005, 0.002, 0.008}` (three noise levels bracketing a
  plausible small-signal residual range for this channel, chosen for
  coverage, not fit to any observed residual); carrier fixed at
  `T_A=2.49°`, `ψ₀` over 8 phases in `[0,2π)` — coarser than G0-e(i)'s
  sweep because this is a calibration check on the null construction, not
  the point estimator, and does not need the same angular resolution.
- **Procedure, per grid cell:** draw `K=500` independent synthetic null
  datasets; for each, run the full sign-flip null (`N=20,000` draws,
  identical construction to the real gating null) and record whether it
  rejects at each of `α ∈ {0.01, 0.05, 0.10}`; the cell's empirical
  rejection rate is `k/K` at each `α`.
- **Tolerance, HALT rule:** at each of the 3×8 = 24 grid cells and each of
  the 3 `α` levels, the empirical rejection rate must fall inside
  `α ± 3·√(α(1−α)/K)` — a standard three-sigma Monte-Carlo calibration
  band (`K=500`: ±1.34pp at α=0.01, ±2.93pp at α=0.05, ±4.02pp at α=0.10).
  **HALT the entire cycle if any cell at any α falls outside its band.**
  This directly tests T2-3's own claim (§3b) that `E[R_q^surr]=0` under the
  sign-flip construction translates into correctly-sized rejection rates in
  finite samples on this exact design — not merely true in expectation.
- **Seed:** fixed, distinct from the real-data null's seed (§5), so that no
  single draw could accidentally leak information between the calibration
  check and the real analysis.

Both G0-e sub-gates are computed once, first, before `carrier_fit` is
called on any real `delta_AB` series. If either fails, the cycle HALTs and
reports only the `G0-e` failure — no real pair is scored, per R6's own
text.

---

## 5. Named-constant / parameter search — R5 applicability

Unchanged from exp-072's own clean finding: **no named-constant or
parameter search is involved.** One physically-motivated curve fit (an
exact identity of the difference of two sinusoids, §2b.3), applied to four
pre-specified pairs; the only continuum searched is the 1-D period grid
`[1°,4°]`, already established (exp-069, exp-071, exp-072) not to trigger
R5. No LOGBOOK R5 ruled-out item (`A_alt≈3·R_OUT`, the `A_eff≈519` cluster)
appears anywhere in this design. A surrogate null is retained (now the
sign-flip construction, §3b) for the same reason exp-072 adopted one: the
nominal `SE` on a fitted coefficient assumes independent residuals, false
for structured FDTD residuals — this is a robustness discipline, not a
name-search, and R5 is not triggered by it.

---

## 6. T1 escape route

**N/A — instrument/methodology re-verification class, identical in kind to
exp-069, exp-070, exp-071 and exp-072 itself.** No mechanism is proposed;
no σ(I), σ(x,t), angular-selectivity, or sub-threshold claim is made,
touched, or advanced. Constraint 3 is not engaged. **Checkpoint-criterion-2
candidacy: none** — no mechanism class is bounded by this cycle in either
outcome; this is desk-analysis/instrument-integrity work on live thread
T28, matching the precedent set by Iterations 46–49 (exp-069/070/071/072).

---

## 7. Predictions — pre-registered, numeric, committed before any computation

### Identity / integrity gates (evaluated first, in order; any HALT stops the cycle)

| ID | Gate | PASS | FAIL |
|---|---|---|---|
| **G0-a** (grid identity) | θ arrays from all three source files bit-identical, 31 points each | identical | any mismatch → **HALT** |
| **G0-b** (telescoping identity) | `delta_40_60+delta_60_70+delta_70_80−delta_40_80=0` at every θ, as raw series | `max\|residual\|≤1e-12` | else **HALT** |
| **G0-c** (column provenance) | exp-069's committed `delta` column ≡ its own `C_empty_C80−C_empty_C40` | `max\|Δ\|≤1e-12` | else **HALT** |
| **G0-d** (conditioning) | condition number of the 5-column design matrix, each pair | `cond≤100` | `cond>100` → that pair `ILL_CONDITIONED`, excluded from every downstream gate |
| **G0-e(i)** (recovery accuracy) | worst-cell `\|ΔP_est/ΔP_true−1\|` over the 1,728-cell synthetic sweep (§4) | `≤0.02` | else **HALT — no pair scored** |
| **G0-e(ii)** (null calibration) | empirical rejection rate at every (σ,ψ₀,α) cell of the 24-cell synthetic-null sweep (§4) | inside `α±3√(α(1−α)/K)` | else **HALT — no pair scored** |

### Scored predictions

**P-073-1 — descriptive, disclosed, always.** Full per-pair table: `T_mean`,
`P_mean`, `a_cbar`, `ψ̄`, `T_delta`, `c0`, `A_i`, `A_q`, `R_i`, `R_q`,
`SE(R_q)` (design-respecting bootstrap), `‖R‖=√(R_i²+R_q²)` (T2-2), `Δf`,
`|Δf|·X`, `ΔP`, `SE(ΔP)`, `dR_q/dψ̄` (`≡R_i`), `|R_i/R_q|`, raw and
Holm-adjusted sign-flip-null `p`, disclosed residual-permutation-null `p`,
`ρ_c` at own `T_mean` and the `≡0` common-carrier sanity check, and the
full carrier-admissibility table (`ΔP`, `SE`, sign, at `T_mean`, `T_delta`,
`1.9608°` labelled *resolution identity, not a control*, and `1.2591°`
labelled *displaced comparator*), published for all four pairs regardless
of every other outcome.

**P-073-2 — does the differential instrument resolve structure, and where?**
Per-pair `RESOLVED` ⟺ **all** of:
(i) not `ILL_CONDITIONED`;
(ii) sign-flip-null Holm-adjusted `p ≤ 0.01`;
(iii) linearization gate `|Δf|·X ≤ 0.25`;
(iv) carrier-consistency: `|T_delta−T_mean|/T_mean ≤ q₉₅`, `q₉₅` the 95th
percentile of that same statistic computed **from the sign-flip surrogate
ensemble** for that pair (recalibrated in-run, per exp-072's own item 6,
now applied to the corrected null so both the significance test and the
consistency gate share one null construction — closing an inconsistency
exp-072's two-null design never had to face);
(v) wrong-carrier gate: `|R_q(1.2591°)| ≤ ½|R_q(T_mean)|` **and**
sign-flip-null Holm-adjusted `p(1.2591°) > 0.01` (both clauses scored on
Holm-adjusted p, consistently — exp-072's own RT-4 catch, that one clause
was frozen Holm-adjusted and coded raw, is designed out here by using one
convention throughout);
(vi) **T2-1: `sign(ΔP)` agrees at `T_mean` with every member of
`{T_delta, 1.2591°}` that itself independently passes clause (iv) at its
own carrier — a carrier failing (iv) is excluded from this test, with the
exclusion disclosed, not silently dropped.

- **CONFIRM** ⟺ `C40–C80` `RESOLVED` **and** `C40–C60` `RESOLVED` **and** at
  least one of `{C60–C70, C70–C80}` `RESOLVED` — unchanged structural
  requirement from exp-072 (the instrument must beat the absolute-period
  predecessor, which could resolve neither 10-cell step, at a step the
  absolute route provably cannot reach).
- **REFUTE** ⟺ zero pairs reach relaxed Holm-adjusted `p≤0.10` under the
  sign-flip null, **and** the injection-recovery power test (§2b.4-adjacent;
  H₀-clean base, `synthetic = delta_ab − R_q·col + R_q^pred·col`, scored at
  Holm-adjusted `p≤0.01` on the known injected effect) demonstrates power at
  all three adjacent pairs. If power is not demonstrated, the branch emits
  `UNDERPOWERED_NOT_EVALUABLE`, never REFUTE.
- **NEITHER** ⟺ anything else, including the a-priori-most-likely outcome
  (both wide pairs resolve, both 10-cell steps do not) — reported as a
  quantitative finding with its own sentence, never a silent PARTIAL escape
  hatch.

**P-073-3 — carrier-sensitivity closure (relabelled from exp-072's "internal
falsifier," per Red Team's own RT-1 finding).** `S=ΔP(40→60)+ΔP(60→70)+
ΔP(70→80)`; `D=ΔP(40→80)`; `ρ_c=|S−D|/max(|D|,0.005°)`, **computed at each
pair's own independently-fit `T_mean`** (deliberately not a shared carrier
— see below). *Pre-registered, provable now:* at a literal common carrier,
`ρ_c≡0` to machine precision (G0-b's exact telescoping of the raw series,
composed with OLS linearity on a fixed design matrix — an algebraic fact,
verified as a disclosed sanity check every run, never scored). The
per-pair-`T_mean` construction is therefore the *only* version of this
statistic that measures anything: it isolates exactly the contribution of
each pair choosing its own carrier, i.e. genuine carrier sensitivity, not
"basis stability."
- **CONFIRM** ⟺ `ρ_c≤0.05` **and** `sign(S)=sign(D)`.
- **REFUTE** ⟺ `ρ_c≥1.00`, **or** `sign(S)≠sign(D)` with both `|S|≥0.010°`
  and `|D|≥0.010°`.
- **NOT_EVALUABLE** ⟺ any of the three adjacent pairs is not `RESOLVED`.
- **NEITHER** ⟺ `0.05<ρ_c<1.00` with all pairs resolved.
- Combined-Verdict language may **not** call this "the design's strongest
  internal falsifier" (exp-072's own overclaim, per RT-1) — it is a
  carrier-sensitivity diagnostic, reported as such.

**P-073-4 — is the recovered structure consistent with Iteration 48's
`ABSORB`-depth trend, or new?** Over `RESOLVED` pairs only (≥2 required);
per-pair rate `r=ΔP/ΔABSORB`; reference `m₀` loaded at runtime (§2c).
- **CONFIRM** ⟺ every resolved pair has `ΔP>0` **and** `r` within a
  **disclosed, non-gating** `[m₀/3,3m₀]` band against **both** the linear
  `m₀` model and a saturating alternative (decay constant fixed at
  `_damping`'s own per-cell exponent, not fitted — engine-motivated, not
  engine-derived: the scale constant is imported from an amplitude-
  attenuation context to a phase observable with no established causal
  relation, and this caveat travels with any CONFIRM).
- **REFUTE** ⟺ any resolved pair has `ΔP<0` with `|ΔP|≥0.010°` (a genuine
  sign reversal) — **the only gating rate clause**, per exp-072's own
  Attacks 5–6 finding that `m₀`-anchored rate-window bands are not a
  trustworthy gate at this precision.
- **NEITHER** ⟺ anything else, or fewer than 2 pairs resolved.

**P-073-5 — carrier-admissibility and different-null disclosure (non-gating,
mandatory alongside any CONFIRM).** Full ΔP/SE/sign table at every carrier
in the admissible set plus `1.9608°`, explicitly labelled a sub-Rayleigh
(0.645-width) resolution identity, not a control. `‖R‖` (T2-2) and its own
sign-flip-null significance, explicitly labelled *tests `H₀:R_i=R_q=0`, a
different hypothesis — not a relaxation of P-073-2's gate*.

**P-073-6 — amplitude-vs-phase-vs-frequency decomposition (non-gating).**
Report `|A_i|/a_cbar`, `|A_q|/a_cbar` (`=2·tanχ₀`, exact per §2b.3),
`|R_q|·σ_u/a_cbar`, `|R_i|·σ_u/a_cbar`, with a disclosed model-strain flag
when the `R_i` channel exceeds the `R_q` channel. Curvature column
`u²·(−sinθ_c)` (6th, disclosed, non-gating; matches the frozen basis's own
sign convention) reported alongside, with its own coefficient and the
6-column condition number — a pure `Δf` predicts zero; an angle-dependent
boundary-reflection phase does not.

### Combined Verdict — pre-committed, computed in code, evaluated in this order

1. **HALT** ⟺ any of G0-a/b/c/e(i)/e(ii) FAIL, or any pair exceeds G0-d.
   Nothing is scored.
2. **REFUTED** ⟺ gates PASS **and** (P-073-2 REFUTE **or** P-073-3 REFUTE).
3. **CONFIRMED** ⟺ gates PASS **and** P-073-2 CONFIRM **and** P-073-3
   CONFIRM **and** P-073-4 CONFIRM.
4. **NEITHER** ⟺ everything else — enumerated in the results JSON with the
   branch that fired, published with the complete P-073-1 table, P-073-5
   disclosure, and P-073-6 decomposition attached, and reported as a
   finding with its own sentence, never a deferral.

**Pre-registration discipline, stated up front (per exp-072's own
contamination ruling, condition 3, which this cycle exists to satisfy):**
any Phase-2 seat that executes this estimator on the real 124 points may
disclose structure but any resulting request to loosen a threshold must be
justified by an argument that does not reference the observed value (the
same outcome-independence test exp-072's own Phase-2 Red Team audit
applied, §4 condition 1) — otherwise the finding is adopted as disclosure
only, not as a threshold change, and Phase 3's synthesis must state which
class each accepted change falls into. This keeps exp-073 itself clean
under the same standard it was built to satisfy on exp-072's behalf.

---

## 8. Idealizations

1. **600nm only.** T28's entire evidential base, and every datum reused
   here, is at 600nm. A CONFIRM licenses no wavelength-general mechanism
   claim.
2. **The `ABSORB`/`PAD` compound-axis confound is NOT relieved by this
   analysis.** `PAD=ABSORB−40` holds exactly at all four configs
   (Iteration 48, closed). Any CONFIRM-shaped language must read
   "`ABSORB`-or-`PAD`-tied," never "`ABSORB`-tied" — binding under every
   verdict including NEITHER, extended to every section of this document
   and its results per exp-072's own item-13 precedent.
3. **`ABSORB` is a graded damping mask, not a material.** A numerical
   boundary-condition parameter (graded-absorption depth in cells). No
   result from varying it licenses any realizability or physical-medium
   claim — MATERIALS' own charter note, restated as the lead seat this
   cycle: a dependence on it is at least as likely to be a boundary
   artifact as a physical effect, and this document proposes no
   realizability bound because none is at stake.
4. **Single-carrier-plus-ramp model, on a window shown to contain ≥2
   contributors.** T21's 1.9608° fringe coexists with the ~2.5° family;
   per-config fits reach only moderate R². The sign-flip null's own
   calibration (G0-e(ii)) validates the *null construction*, not the
   correctness of this functional-form assumption against a genuinely
   multi-component signal — a limitation this design shares with exp-072
   and does not close.
5. **~2.4 periods of carrier in the window.** Not asymptotic; edge effects
   on the ramp coefficient are real, part of what both G0-e sub-gates
   calibrate against.
6. **At `n_grid=3000` the `C70`/`C80` free-period order reverses relative to
   exp-071's own `n_grid=400` reading** — Iteration 48's "smooth rise" and
   the raw `m₀` chord rest on a tie broken only by finer search resolution;
   the linear-fit `m₀` used here is the least-squares slope, not the
   endpoint chord, and is comparatively more robust to this tie, but the
   underlying node-collision fact is disclosed, not resolved.
7. 2D TMz, single polarization; positive-θ branch only (36°–42°) — not a
   symmetry test; single-angle `C_empty` readings, not an N9/N17 aggregate
   (T25/T26 do not apply); bench scale only (`R_OUT=78` cells) — no witness-
   scale claim.
8. No new FDTD means no new engine-physics identity gate. Trust in the
   underlying numbers is inherited from exp-069's and exp-071's own
   already-passed G1 identity gates, settling checks, and peak-cell R3
   resolution checks. This cycle adds arithmetic-integrity gates (G0-a/b/c)
   and the ground-truth/null-calibration gates (G0-d/e) only, and inherits
   — does not re-establish — engine trust.
9. **Statistical power is estimated a-priori (§2c) from a corrected `m₀`
   read at runtime.** If the true effect differs from that estimate, the
   under/over-powered set may differ from the two pairs named. The
   pre-registered fallback (report sign and `p`, quote no period for
   unresolved pairs) covers both directions.
10. **G0-e's own synthetic sweeps (§4) use deliberately generic carrier
    periods, amplitudes and noise levels — bracketing, not reproducing, the
    real fitted values** — so that passing `G0-e` cannot be read as evidence
    about this cycle's own real data; it is evidence about the pipeline
    alone, which is exactly what R6 requires it to be.
11. **`C_empty` is a dimensionless field ratio, not a Michelson/Weber
    contrast**; any `ptp/mean`-style statistic appearing beside a `ΔP` is a
    fit-conditioning statistic, not a perceptual or photometric quantity —
    carried forward from exp-072's own item-13 disclosure.
12. **Window provenance and multiplicity across cycles.** The 31-point
    36.0°–42.0° grid was inherited from Block MINI (exp-069) and T28 was
    discovered inside it. Statistics now computed on these identical 124
    points span exp-069's `ptp/mean` and fixed/free-period fits, exp-071's
    four per-config free-period fits, exp-072's four carrier searches and
    ramp fits (pre- and post-fix), and now exp-073's own re-run. Holm
    corrects within this cycle's own three free pairs; nothing corrects
    across cycles. This is disclosed, not fixed, by this design.
13. No absorbed-power number is produced; THERMODYNAMICS' energy sidecar is
    N/A this cycle, by argument (house precedent, Iteration 5), not by
    omission.

---

## 9. Budget

**Zero new FDTD calls. Desk-only, pure arithmetic over already-committed
JSON plus synthetic data generated in-run.** No `lab/` diff;
`lab/validation/VALIDATION.md` re-run not triggered (no engine change).

Cost: 4 real pairs × (1 carrier fit + 1 five-column `lstsq` + `N=20,000`
sign-flip surrogate refits, vectorizable via one precomputed pseudo-inverse
since `T_mean`/`ψ̄` are held fixed across surrogates, plus a disclosed
`N=20,000` residual-permutation cross-check) + `G0-e(i)`'s 1,728-cell
synthetic-recovery sweep (one `lstsq` per cell) + `G0-e(ii)`'s 24-cell ×
`K=500` × `N=20,000` synthetic-null-calibration sweep (the dominant cost,
still a vectorized linear-algebra operation, no FDTD) + the wrong-carrier
and admissibility-set repeats at `1.2591°`/`T_delta` for every pair.

**Estimated wall-clock: a few minutes, single-core**, dominated by
`G0-e(ii)`'s calibration sweep; every operation is a fixed-design linear
projection against a precomputed pseudo-inverse, not an FDTD call.
Deliverables: `run.py`, `results.json`, `phase4_results.md`, `NOTES.md` in
`experiments/073-t28-differential-beat-fit-reissue/`.
