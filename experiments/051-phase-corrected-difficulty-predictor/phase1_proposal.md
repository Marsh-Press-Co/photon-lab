# PHASE 1 — PROPOSAL · Panel Iteration 28 · Lead seat: ELECTROMAGNETISM

## "The Phase-Corrected Difficulty Predictor" (candidate exp-051)

*Runner: cloud panel shift · rotation: VISION→PHOTONICS→MATERIALS→
**ELECTROMAGNETISM**→THERMODYNAMICS→QUANTUM OPTICS→repeat. Protocol:
PANEL.md. Memory: LOGBOOK.md (RULED OUT R1–R4 checked — nothing here
resurrects a ruled-out idea; this cycle proposes no mechanism at all).*

**Executing a queued item, not a fresh ELECTROMAGNETISM mechanism
proposal**, per PANEL.md's own Iteration-20/22/23/26/27 precedent for
instrument/model-fidelity cycles and Red Team's Iteration-27 Phase-5
synthesis, ranked #1, near-unanimous across five reviewing seats
(`experiments/050-n-convergence-a724-geometry/phase5_redteam_audit.md`;
PLAN.md panel-Iteration-28 queue entry (1)): *"a phase-corrected
difficulty-predictor test across the full FWHM=20° grid, including
`|C(n=81)|/ABS_TOL` as a regressor, to derive the unexplained ~1.9–2.3×
convention asymmetry."* This is also, verbatim, the open question exp-050's
own Reading section left unresolved: *"which convention's n=41→81 step
happens to cross the fixed `ABS_TOL=5×10⁻⁴` line is a reproducible
~1.9–2.3× magnitude coincidence ... itself new, real, and unexplained."*
Instrument/model-fidelity cycle, Iteration-20/22/23/26/27 class. **T1
escape route: NONE.**

---

## 1. Mechanism / test narrative (≤300 words)

**This is NOT a T1 mechanism proposal.** No material law, no σ(I)/σ(x,t),
no angular-selectivity claim, no constraint-3/4 verdict.

exp-050 found that `beam_divergence_incoherent` and
`beam_divergence_incoherent_corrected` both execute a genuine,
fast-settling destructive-interference null of the same FWHM=20° angular
integral at several GEOM78 (θ₀,λ) coordinates — but which convention's
n=41→81 quadrature-refinement step crosses the fixed `ABS_TOL=5×10⁻⁴` gate
is a reproducible ~1.9–2.3× magnitude coincidence between the two
conventions, unexplained by Red Team's own Phase-5 audit.

This proposal tests one specific, computable hypothesis: both conventions'
raw single-angle analytic `C_empty(θ,λ)` fringes (obliquity-on-E for
`incoherent`, single-obliquity-via-H for `incoherent_corrected` —
already-committed, magnitude-validated T21 machinery, exp-042 Block
MAGNITUDE) zero-cross at nearly, but not exactly, the same θ, because the
two conventions differ in how obliquity enters the coherent sum. Near a
shared zero-crossing, a cell's tier stability under n-doubling should
depend on (i) how close the Gaussian-weighted quadrature's own center θ₀
sits to that null — its **phase offset within the local T21 fringe period**
`P(θ)=λ/(A·cosθ)` — and (ii) how large the quadrature residual already is
relative to `ABS_TOL` one doubling in, `|C(n=81)|/ABS_TOL`. If both
regressors jointly discriminate exp-050's own 7 tier-unstable from 11
tier-stable GEOM78 (cell,function) combinations, that closes exp-050's own
first open question — a predictive handle on instability, not a residual.
If, additionally, the two conventions' *local fringe slopes* near the
shared near-zero cells bracket the observed ~1.9–2.3× step asymmetry, that
closes exp-050's second open question directly — one geometric fact
(differing curvature near a shared null), not two unexplained residuals.
Desk-only, pure numpy, zero new FDTD calls.

*(253 words)*

---

## 2. Parameter tables

### 2.0 Reused verbatim from exp-049/050 — no changes (flagged loudly if any were needed; none are)

| Constant / function | Value | Source |
|---|---|---|
| `N_SERIES` | (41, 81, 161, 321, 641, 1281, 2561, 5121) | `experiments/050-.../run.py:30` |
| `N_REGRESSION` | 401 | ibid. `:31` |
| `C_THR`, `ABS_TOL`, `REL_TOL` | 0.005, 5×10⁻⁴, 1.0% | ibid. `:26-28` |
| Convergence / exemption criterion | `Δabs(n)=\|C(2n)−C(n)\|`; if `\|C(2n)\|≥C_THR` also require `Δrel≤REL_TOL`; else exempted, judged on `Δabs≤ABS_TOL` alone | ibid. `delta_step`, `:56-67` |
| `nstar` / tier definitions, tier-unstable label (`nstar≠41`) | unchanged | ibid. `find_nstar`/`tier_index`, `:70-90` |
| `gaussian_angle_weights(θ₀,fwhm,n,half_width_factor=2.5)` | reused as-is | `experiments/042-.../design_geometry.py:310-318` |
| `GEOM78` (`A=724`), `GEOM_EXP042_OLD` (`A=752`) | verbatim | `experiments/048-.../design_geometry.py:145-158` |
| `beam_divergence_incoherent`, `beam_divergence_incoherent_corrected` (geometry-parameterized) | reused unmodified | `experiments/050-.../design_geometry.py:99-136` |
| `edge_diffraction_c_empty`, `edge_diffraction_c_empty_corrected` (module-global, single-angle) | source formulas reused, generalized (§2.2) | `experiments/042-.../design_geometry.py:298-309,268-277` |

**No tuning parameter is changed anywhere in this proposal.** The only new
work is (a) generalizing the two module-global single-angle fringe
functions to a geometry dict — a strict subset of exp-050's own already-
completed generalization work, since `beam_divergence_*` already builds the
identical per-angle field terms internally — and (b) the phase-offset /
slope machinery defined in §2.2, which is genuinely new.

### 2.1 Scope: exactly 18 cell-function combinations (task-specified, not a superset)

**9 cells** (θ₀,λ), FWHM=20° fixed, the FWHM=20° subset of exp-049/050's
own 36-cell grid — **× 2 functions** (`incoherent`, `incoherent_corrected`
only; `coherent` excluded, per the task's own scope and because `coherent`
is not part of the "incoherent-family" the 1.9–2.3× asymmetry was measured
between):

| λ (nm) | θ₀ | `P(θ₀)` at A=724 (deg, exp-050 §2.4, reused) | `incoherent` n\* (GEOM78) | `incoherent_corrected` n\* (GEOM78) |
|---|---|---|---|---|
| 450 | 36° | 1.4673 | 41 | 41 |
| 450 | 38° | 1.5064 | **81** | **81** |
| 450 | 40° | 1.5496 | 41 | **81** |
| 600 | 36° | 1.9564 | 41 | **81** |
| 600 | 38° | 2.0085 | 41 | **81** |
| 600 | 40° | 2.0661 | 41 | **81** |
| 750 | 36° | 2.4455 | 41 | 41 |
| 750 | 38° | 2.5107 | 41 | 41 |
| 750 | 40° | 2.5827 | 41 | **81** |

(`n*`/`P(θ₀)` values copied directly from `experiments/050-.../results.json`
`per_cell_summary_geom78` and `experiments/050-.../phase1_proposal.md` §2.4
— not recomputed by hand for this table; Phase 4 recomputes both
independently as part of the regression anchor, §2.3.) **7 of 18 bolded
combinations are tier-unstable (`n*=81`); 11 are tier-stable (`n*=41`).**
450nm/38° is the "masked" 4th cell Red Team's Phase-5 audit found unstable
in *both* functions (never registering as an A752→A724 "violation" because
its own `n*` was already 81 at A=752 too) — included here because this
proposal scores absolute tier-instability at GEOM78, not the A752→A724
delta exp-050 scored.

### 2.2 New machinery — the crux, defined precisely and computably

**(a) Geometry-parameterized single-angle fringe functions.** Trivial
extensions of exp-042's own module-global `edge_diffraction_c_empty`
(obliquity-on-E, `:298-309`) and `edge_diffraction_c_empty_corrected`
(single-obliquity-via-H, `:268-277`) to accept a geometry dict `g`, evaluated
on `_geom_derived(g)`'s own `r`/`obliquity` — the *same* substitution
exp-050's own `design_geometry.py` already performed for the *integrated*
`beam_divergence_*` functions, applied here to their un-integrated,
single-angle building blocks instead:

```
def edge_diffraction_c_empty_g(theta_deg, lam_cells, g, convention):
    gd = _geom_derived(g)                       # exp-048's own function, reused
    k = 2*pi / lam_cells
    if convention == "incoherent":               # obliquity-on-E
        k2, G = _G_for_g(lam_cells, gd, obliquity=True)   # exp-050's own function, reused
        b = abs(G @ _src_amp(theta_deg, k2, gd))**2
    else:  # "incoherent_corrected"               # single-obliquity-via-H
        G0 = exp(1j*(k*gd["r"] - pi/4)) / sqrt(gd["r"])
        amp = _src_amp(theta_deg, k, gd)
        E, H = G0 @ amp, (G0 * gd["obliquity"]) @ amp
        b = -real(E * conj(H))
    bo, bf = amb.window_means(b, gd["y_lo"], g["OBJ_Y"], g["R_OUT"], g["GUARD_OUT"], g["W_FLANK"])
    return amb.weber(bo, bf)
```

Every line reuses an already-committed function (`_geom_derived`,
`_G_for_g`, `_src_amp`, `amb.window_means`, `amb.weber`) — no new physics,
a bookkeeping generalization exactly like exp-050's own §2.2.

**(b) The local T21 fringe period — LOGBOOK's own formula, no rederivation:**

```
def local_period_deg(theta0_deg, lam_cells, A):
    return degrees(lam_cells / (A * cos(radians(theta0_deg))))
```

`A = g["OBJ_Y"] - g["ABSORB"]` (724 at GEOM78, 752 at GEOM_EXP042_OLD) —
`P(θ)=λ/(A·cosθ)`, LOGBOOK's T21 entry (Iteration 18), used exactly as
stated, reused by exp-049/050 by analogy already.

**(c) Phase offset — the crux, defined operationally against the ALREADY-
VALIDATED analytic fringe, not re-derived from a two-edge toy formula:**

```
def phase_offset(theta0_deg, fwhm_deg, lam_cells, g, convention, n_grid=4001):
    P = local_period_deg(theta0_deg, lam_cells, g["A"])
    window = 0.6 * P                      # >= 1 full period on each side
    thetas = linspace(theta0_deg - window, theta0_deg + window, n_grid)
    c = [edge_diffraction_c_empty_g(t, lam_cells, g, convention) for t in thetas]
    # scan outward from theta0 in both directions; take the FIRST sign
    # change found on each side; linearly interpolate to the zero; keep
    # whichever zero is angularly closer to theta0
    theta_zero = nearest_zero_crossing(thetas, c, theta0_deg)   # None if not found
    if theta_zero is None:
        return None, "NOT_FOUND_WIDEN_TO_1.5P"     # diagnostic, not silently dropped
    offset = (theta0_deg - theta_zero) / P
    return ((offset + 0.5) % 1.0) - 0.5, "OK"       # wrapped to (-0.5, 0.5]
```

`offset≈0`: θ₀ sits at a fringe **node** (the underlying single-angle
fringe crosses zero right where the Gaussian-weighted quadrature is
centered — the near-zero destructive-interference regime exp-050's own
Reading section named as the shared mechanism). `offset≈±0.5`: θ₀ sits at
an **antinode** (maximal local fringe magnitude, far from the pathology).
`n_grid=4001` over a ±0.6·P window is a Phase-3-tunable resolution choice,
not load-bearing physics — flagged for Phase 3 to set, cost-permitting
(§6).

**(d) `|C(n=81)|/ABS_TOL`** — literally `abs(beam_divergence_<fn>(θ₀,20,λ,g,n=81)) / ABS_TOL`,
one fresh call per combination to exp-050's own already-committed
geometry-parameterized function (not stored in `results.json` for the 11
tier-stable combinations, where `converged_value` was recorded at `n*=41`
instead — cheap to recompute, §6).

**(e) Local fringe slope** (for the asymmetry-explanation prediction,
P-PCDP-4/5): central finite difference of `edge_diffraction_c_empty_g` at
θ₀, step `h = P(θ₀,λ)/200`:
`slope(θ₀,λ,g,convention) = (c(θ₀+h) − c(θ₀−h)) / (2h)`.

### 2.3 Regression anchor — checked first (P-PCDP-0)

`edge_diffraction_c_empty_g` at `g=GEOM_EXP042_OLD` must reproduce exp-042's
own committed module-global `edge_diffraction_c_empty`/
`edge_diffraction_c_empty_corrected` (`experiments/042-.../design_geometry.py`)
to ≤10⁻⁹ relative, at every one of the 9×3=27 (θ₀,λ) spot-check points this
proposal's own zero-crossing grids pass through at θ=θ₀ exactly. **Hard
failure ⇒ no phase-offset or slope number in this proposal is trusted until
resolved** — the same "checked first, gates everything else" role every
prior n-convergence cycle's own #0 prediction has held.

---

## 3. T1 escape-route statement

**NONE.** This cycle proposes no material law, no σ(I), no σ(x,t), no
angular selectivity, no sub-threshold operation, and no new mechanism
class. It builds a small, desk-only diagnostic on top of already-committed,
already-gated propagator code to explain a numerical-convergence residual.
No constraint-3/4 verdict is issued at either tier, and no result here can
move any `REALIZABILITY_MEMO.md` tier — same statement exp-050's own
NOTES.md made verbatim.

---

## 4. Falsifiable predicted outcomes — committed BEFORE any run

"Tier-unstable" = `n*≠41` (i.e. `n*=81`, the only tier value observed at
these 18 GEOM78 combinations, per §2.1's own already-committed table).

| ID | Prediction | Committed band | Hard falsification |
|---|---|---|---|
| **P-PCDP-0** | **Regression anchor, checked first** (§2.3) | ≤10⁻⁹ relative at all 27 spot-check points, both conventions | any mismatch beyond float noise ⇒ nothing else in this cycle is trusted until resolved |
| **P-PCDP-1** | **Primary discriminator.** A 2-feature classifier (`x1=\|offset\|`, `x2=log10(\|C(n=81)\|/ABS_TOL)`) scored by leave-one-out cross-validated AUC on all 18 GEOM78 combinations (7 positive / 11 negative, §2.1) | LOOCV-AUC ≥ **0.85** ⇒ CONFIRMED; 0.65–0.85 ⇒ PARTIAL; <0.65 ⇒ REFUTED | LOOCV-AUC < 0.55 (statistically indistinguishable from chance at N=18) on either the LOOCV or plain in-sample metric |
| **P-PCDP-2** | **Simpler rank-ordering fallback** (pre-registered given N=18 is thin for a 2-parameter fit): a single fixed threshold on `\|offset\|` alone, somewhere in [0.10,0.30], simultaneously reaches sensitivity ≥6/7 and specificity ≥8/11 | such a threshold exists | no threshold in [0.05,0.40] reaches sensitivity ≥5/7 **and** specificity ≥7/11 simultaneously |
| **P-PCDP-3** | **Generalization, not refit**: applying P-PCDP-2's own fixed threshold, unchanged, to the 18 GEOM_EXP042_OLD combinations (tier data already committed, `experiments/049-.../results.json`; offsets freshly computed at A=752) reproduces comparable discrimination | sensitivity and specificity both within 20 percentage points of the GEOM78 figures | either axis falls below 50% (worse than chance) at A=752 — the relationship would be GEOM78-specific, not general |
| **P-PCDP-4** | **The asymmetry explanation.** At the 4 cells where both conventions are tier-unstable or near-null (750/40, 600/36, 600/40, 450/38 — §2.1), the slope ratio `\|slope_corrected\|/\|slope_incoherent\|` (§2.2e) falls in **[1.5, 3.0]** (bracketing the measured ~1.9–2.3× `Δabs` step asymmetry) at ≥3 of 4 cells, median in [1.7, 2.6] | as stated | ≤1 of 4 cells in [1.5,3.0], or median outside [1.2,4.0] |
| **P-PCDP-5** | **Negative control** against a trivial-uniform-rescaling explanation: the 18 per-combination slope ratios are NOT one constant — IQR spans ≥1.5× (high/low), and antinode cells (`\|offset\|>0.35`) deviate from the near-node median by >30% | as stated | all 18 ratios cluster within ±10% of one value (would mean `incoherent_corrected` is just a uniformly rescaled `incoherent` — the near-zero-specific story would be wrong) |

**What would make this cycle a failure, stated plainly:** if P-PCDP-1 AND
P-PCDP-2 both land REFUTED, the phase-offset/`|C(n=81)|`/ABS_TOL predictor
Red Team's own Iteration-27 synthesis proposed does not actually
discriminate tier-stability at this program's own geometry — a real,
pre-registered way for this cycle to lose, matching exp-049/050's own
"what would make this cycle a failure" convention. P-PCDP-1/2's own outcome
does not gate P-PCDP-4/5 (a different, narrower claim about only the 4
near-null cells) — the two halves of Iteration 28's ranked #1 priority
(predictive handle vs. asymmetry explanation) are scored independently, per
the task's own framing.

---

## 5. Idealizations (lab convention — stated, not buried)

1. **Scope: exactly the 18 GEOM78 (cell,function) combinations named in
   §2.1**, plus the 18 GEOM_EXP042_OLD combinations for P-PCDP-3's
   generalization check only (not refit, not independently scored against
   its own new predictions) — `coherent` is out of scope throughout,
   matching the task's own "incoherent-family" framing.
2. **`N_SERIES`, `ABS_TOL`, `REL_TOL`, `C_THR`, the exemption criterion are
   unchanged from exp-049/050** — no re-tuning of the convergence machinery
   itself is in scope.
3. **Phase offset is defined against the raw single-angle analytic fringe
   (§2.2a), not the FWHM-integrated `beam_divergence_*` quantity itself.**
   This is a modelling choice: the claim is that θ₀'s position relative to
   the *underlying, un-integrated* fringe governs how well a finite-n
   Gaussian-weighted quadrature can resolve it — not a claim that the
   integrated quantity itself has a simple periodic structure in θ₀ (it
   does not, by construction, once FWHM≫P). Same "reused by analogy, not a
   fresh magnitude validation at this quantity" status exp-049/050's own
   idealization 3 already carried for the period formula itself — carried
   forward, not resolved, here.
4. **The period formula `P(θ)=λ/(A·cosθ)` is used exactly as LOGBOOK states
   it**, without re-deriving the underlying two-edge path-difference
   formula from first principles — a modelling choice, disclosed, per the
   task's own instruction to ground the crux quantity in that formula
   specifically.
5. **The zero-crossing search (§2.2c) assumes exactly one relevant sign
   change within a ±0.6·P window.** Not silently assumed to succeed:
   `phase_offset` returns an explicit `NOT_FOUND` diagnostic per
   combination if no crossing is found in that window (widened once to
   1.5·P before giving up); Phase 4 must report
   `n_not_found`/`n_widened` counts as a completeness check, the same
   discipline as this program's own completeness ledgers.
6. **AUC at N=18 (7 positive/11 negative) is a small-sample estimate.**
   The wide CONFIRMED/REFUTED gap (0.85 vs 0.65) and the pre-registered
   P-PCDP-2 fallback exist specifically because a tight band would not be
   honest at this sample size — disclosed here, not smoothed into the
   headline number.
7. **P-PCDP-3 is a generalization check, not an independent discovery
   cycle**: it reuses P-PCDP-2's own threshold unchanged; a REFUTED result
   there narrows how far the relationship travels, it does not retroactively
   invalidate P-PCDP-1/2 (scored at GEOM78 only).
8. **No new trust-suite gate.** This is analytic/desk work built entirely
   on already-committed, already-gated propagator code (matching
   exp-049/050's own "zero new FDTD calls" scope) — bench re-verified 41/41
   immediately before the run per house discipline, but no new `lab/`
   engine code is touched, so no new suite stage is warranted (Iteration-
   26/27 precedent).
9. **No perceptual claim.** `C_THR=0.005`/`ABS_TOL=5×10⁻⁴` are cited only
   as the pre-existing decision lines already governing `nstar`; this cycle
   issues no new perceptual verdict.
10. **T24's ABSORB-boundary systematic and any FDTD cross-check are out of
    scope**, identical status to exp-050's own idealizations 5/6 — this
    remains a purely desk, quadrature-fidelity question about already-
    committed analytic machinery, not a physics-validation-against-the-
    engine question.

---

## 6. Cost note

**New FDTD calls: 0.** Pure `numpy`, reusing exp-042/048/049/050's own
already-committed functions; the only new code is the thin single-angle
geometry-parameterized generalization (§2.2a, a strict subset of exp-050's
own already-completed generalization effort) plus the phase-offset/slope
diagnostics (§2.2b–e), all elementary closed-form or finite-difference
computations on top of it.

**Scale, estimated bottom-up (not a doubling guess):**

- Zero-crossing search (§2.2c): 36 combinations (18 GEOM78 + 18
  GEOM_EXP042_OLD for P-PCDP-3) × `n_grid=4001` single-angle evaluations ≈
  **144,036** evaluations.
- `|C(n=81)|/ABS_TOL` (§2.2d): 36 combinations × one `beam_divergence_*`
  call at `n=81` (81 single-angle evaluations internally) ≈ **2,916**
  evaluations.
- Local slope (§2.2e): 18 GEOM78 combinations × 2 finite-difference points
  ≈ **36** evaluations (negligible).
- P-PCDP-0 regression anchor: 27 spot points × 2 conventions ≈ **54**
  evaluations (negligible).
- **Total ≈ 147,042 single-angle evaluations** — roughly **13% of** exp-049's
  own measured 1,145,772-evaluation single-geometry sweep, and about **6%
  of** exp-050's own two-geometry 2,291,544-evaluation sweep, because this
  proposal never repeats the full `N_SERIES` doubling series out to n=5121
  — it only ever needs `n=81` (once, for §2.2d) plus a fixed, Phase-3-set
  grid resolution for the zero-crossing search, not a geometric doubling
  budget.

At exp-050's own disclosed true per-evaluation cost (≈12,490s / 2,291,544
evaluations ≈ 5.45ms/evaluation, the honest *total*-cost figure Red Team's
mandatory-fix 2 established, not the understated single-clean-run figure) —
**≈147,042 × 5.45ms ≈ 800s ≈ 13 minutes single-threaded**, plausibly less
if `n_grid` is trimmed at Phase 3 (a resolution choice, not load-bearing
physics, §2.2c) or the (uncached, per exp-050's own disclosed gap)
propagator matrix is memoized once per `(λ,g,convention)` — a cheap,
optional Phase-4 fix this proposal does not require. **Order of magnitude
below exp-049 (2743.2s) and exp-050 (6225.3s / true cost ≈12,490s)**, by
design: this cycle targets a narrow, fixed-resolution diagnostic, not
another full doubling-series sweep.

**Code footprint:** `experiments/051-.../design_geometry.py` (new, the
single-angle geometry-parameterized generalization plus phase-offset/slope
functions, per §2.2) and `experiments/051-.../run.py` (new, scores
P-PCDP-0 through -5 against the frozen bands above). No new trust-suite
stage (§5, idealization 8).
