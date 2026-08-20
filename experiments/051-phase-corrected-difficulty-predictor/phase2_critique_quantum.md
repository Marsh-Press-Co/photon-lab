# PHASE 2 — CRITIQUE · Panel Iteration 28 · Seat: QUANTUM OPTICS

*Blind critique. No other seat's current-cycle output was read (no
`phase2_critique_*.md` / `phase2_redteam_*.md` opened; the directory
contained only `phase1_proposal.md` at read time). Charter: non-classical
absorption, state-dependent or coherent interactions — engaged here on its
coherence/interference-bookkeeping axis, since this cycle proposes no
mechanism. Every number below was produced by executing code against the
already-committed modules, not by argument (exp-050 Phase-5 standard).
Nothing under `lab/`, exp-049 or exp-050 was modified; scratch code lives
outside the repo.*

---

## Steel-man (≤150 words)

exp-050's integrated observable is not merely *related* to the T21 fringe —
it **is** a quadrature of it, and this proposal is the first in the program
to say so. I verified the identity by execution:
`beam_divergence_*(θ₀,20°,λ,g,n)` equals `Σᵢwᵢ·c(θᵢ)/Σᵢwᵢ` over the
single-angle Weber contrast, to **5.2×10⁻¹⁴ relative** (600 nm/38°, both
conventions) — `incoherent_sum`'s per-component flank normalization makes
the flank mean exactly 1, so the Weber contrast passes through the sum
linearly. That makes a sampling/phase framing exactly the right physics.
And the regime is severe: node spacing at n=41 is h = 5·FWHM/(n−1) = 2.5°
against P = 1.47–2.58°, i.e. **0.59–1.03 samples per fringe period, 1.9–3.4×
below Nyquist at all 18 combinations**. Tier instability here genuinely is
an aliasing phenomenon, genuinely phase-governed, genuinely desk-computable.
P-PCDP-0's bit-exact anchor, the pre-registered fallback and the explicit
`NOT_FOUND` diagnostic are the right discipline.

## Sharpest attack (≤150 words)

**The crux measures the wrong phase, and the proposal's own hard
falsification fires.** I built §2.2(a–e) and ran it. The n=41 error is
*exactly* the Poisson alias term
`E(41) = 2Re ∫W(u)c(θ₀+u)e^{−2πimu/h}du / ∫W du` (m=1,2), which reproduces
measured `C(41)−C(161)` at **all 18 combinations to ≤1.4%, Pearson
r = 1.00000**. Its phase reference is the **node lattice h**, not the
fringe. Discriminating test — hold the physics fixed, vary n: the residual's
period in θ₀ tracks h (measured 0.4115 / 0.5865 / 0.6658 cycles/deg at
n = 41/61/71 vs 1/h = 0.400/0.600/0.700), never the fringe's fixed
0.4979 cycles/deg. Consequently `|offset|` AUC = **0.649**, `x2` AUC =
**0.520**, and **P-PCDP-2's hard-falsification clause fires**: no threshold
in [0.05,0.40] reaches sens ≥5/7 *and* spec ≥7/11. Structurally it cannot —
mean |Δoffset| between conventions is **0.041** while **5/9** cells carry
split labels.

## Verdict

**SUPPORT-WITH-CHANGES.**

The cycle is correctly aimed, correctly scoped and correctly cheap, and its
underlying premise (tier instability = phase-dependent aliasing of the T21
fringe) is *true* — I confirmed it to five significant figures. But the one
new quantity it defines, §2.2(c)'s `phase_offset` against the nearest
zero-crossing at θ₀, is refuted at the desk before Phase 4 begins, and
§2.2(e)'s local slope is anti-correlated with the very asymmetry P-PCDP-4
claims it explains (Spearman ρ = **−0.300**, p = 0.43; Pearson −0.354).
Run as written, this cycle spends its budget to score two REFUTED
predictions and leaves exp-050's two open questions exactly where they were.
Run with the one change below, it *closes both of them* — I have already
executed the closing computation, so this is a verified request, not a
speculative one.

## The single change that would flip my verdict to SUPPORT

**Replace §2.2(c)'s `phase_offset(θ₀,…)` with the alias coefficient at the
quadrature node spacing** `h = 2·half_width_factor·FWHM/(n−1)` (= 2.5° at
n=41, FWHM=20°, the committed `gaussian_angle_weights` window):

```python
def alias_coeff(theta0, fwhm, lam_cells, g, convention, m=1, h=None, step=0.01):
    sig = fwhm / 2.3548
    h   = h or (5.0 * fwhm / 40.0)              # n=41 node spacing
    u   = np.arange(-2.5 * fwhm, 2.5 * fwhm + step, step)
    W   = np.exp(-0.5 * (u / sig) ** 2)
    c   = np.array([edge_diffraction_c_empty_g(theta0 + t, lam_cells, g, convention)
                    for t in u])
    return np.trapezoid(W * c * np.exp(-2j*np.pi*m*u/h), u) / np.trapezoid(W, u)
```

Then `E_pred(41) = 2·Re[alias_coeff(m=1)] + 2·Re[alias_coeff(m=2)]`, and the
regressor for P-PCDP-1/2 becomes `|E_pred|/ABS_TOL` (a *predicted* Δabs, not
a proxy). Measured against exp-050's own committed table this predicts
`C(41)−C(161)` at 18/18 combinations to ≤1.4% and separates the 7
tier-unstable from the 11 tier-stable combinations **perfectly (AUC = 1.000)
at the natural threshold `|E_pred| = ABS_TOL` itself**: all 7 unstable
combinations read ≥5.26×10⁻⁴, all 11 stable ones ≤4.25×10⁻⁴, with no fitted
parameter anywhere. Same dense
single-angle scan §2.2(c) already budgets; **no new FDTD, no new tuning
parameter, no new geometry** — it is the same integrand, transformed at the
alias frequency instead of searched for a zero-crossing.

The same object also settles P-PCDP-4/5 without the slope machinery: the
unexplained **~1.9–2.3× convention asymmetry is the ratio of the two
conventions' angular spectral amplitude of the single-angle fringe at the
one alias frequency 1/h = 0.4 cycles/deg** — measured
`|ĝ_corr|/|ĝ_inc|` = 1.664–2.232, median **1.950**, tightly grouped within
each λ (1.66–1.68 / 1.95–1.96 / 1.87–2.23 at 450/600/750 nm). That is one
geometric fact, exactly the deliverable §1 promises — but it is a
one-frequency spectral ratio, not "differing curvature near a shared null."

---

## Supporting evidence (all executed; reproduction recipe below)

### E1 — the exact identity that makes the steel-man's framing right

`lab/ambient.incoherent_sum` divides each per-angle profile by its own flank
mean, so the summed profile's flank mean is identically 1 and
`weber(·)` returns `Σwᵢcᵢ/Σwᵢ`. Verified numerically against the committed
`experiments/050-.../design_geometry.py` at (600 nm, θ₀=38°, FWHM=20°,
GEOM78, n=41):

| convention | committed function | `Σwᵢcᵢ/Σwᵢ` | rel. diff |
|---|---|---|---|
| `incoherent` | 3.318457747751857×10⁻⁴ | 3.318457747751684×10⁻⁴ | 5.2×10⁻¹⁴ |
| `incoherent_corrected` | 4.4686642318647607×10⁻⁴ | 4.468664231862714×10⁻⁴ | 4.6×10⁻¹³ |

### E2 — the 18-combination table reproduces §2.1 exactly (7 unstable / 11 stable)

Independently recomputed (not copied from `results.json`), `N_SERIES`,
`ABS_TOL=5×10⁻⁴`, `C_THR=0.005`, `REL_TOL=1%` and the exemption criterion
unchanged. Every `n*` matches §2.1's table, including 450/38 in both
functions. `Δabs(81→161)` is ≤1.2×10⁻⁴ everywhere and ≤3.5×10⁻⁶ at 600/750
nm, so `C(161)` is a safe stand-in for `C(∞)`.

### E3 — the crux predictor, scored on its own pre-registered bands

`phase_offset` implemented per §2.2(c) (4001-point grid, ±0.6·P widened once
to ±1.5·P, nearest crossing, wrapped to (−0.5,0.5]); no `NOT_FOUND` at any
of the 18.

| λ,θ₀ | \|off\|_inc | \|off\|_cor | Δ | labels (inc,cor) |
|---|---|---|---|---|
| 450/36 | 0.405 | 0.419 | 0.014 | (0,0) |
| 450/38 | 0.390 | 0.378 | 0.012 | (1,1) |
| 450/40 | 0.397 | 0.383 | 0.014 | **(0,1)** |
| 600/36 | 0.337 | 0.320 | 0.017 | **(0,1)** |
| 600/38 | 0.040 | 0.108 | 0.068 | **(0,1)** |
| 600/40 | 0.155 | 0.129 | 0.026 | **(0,1)** |
| 750/36 | 0.477 | 0.477 | 0.001 | (0,0) |
| 750/38 | 0.178 | 0.098 | 0.080 | (0,0) |
| 750/40 | 0.468 | 0.333 | 0.135 | **(0,1)** |

- in-sample AUC, score = −\|offset\| (near-node ⇒ unstable): **0.6494**
  (below P-PCDP-1's own 0.65 PARTIAL floor; LOOCV cannot exceed it
  materially at N=18).
- in-sample AUC, score = `x2 = log10(|C(81)|/ABS_TOL)`: **0.5195** — chance.
- P-PCDP-2: **no** threshold in [0.05,0.40] reaches sens ≥5/7 **and**
  spec ≥7/11 → the pre-registered **hard falsification fires**. Best
  achievable anywhere in that range: t=0.391 → 7/7 sensitivity but 6/11
  specificity, and t=0.391 is outside P-PCDP-2's own committed [0.10,0.30]
  band.
- The structural reason, stated as a number: the two conventions' offsets
  agree to a mean of 0.041 (idealization 3's own premise — "both conventions
  zero-cross at nearly the same θ" — is *correct*), while the *label* is
  convention-determined at 5 of 9 cells. A convention-blind regressor cannot
  separate a convention-determined label. This is not a small-sample
  complaint; it is a structural one.

### E4 — where the phase actually lives (the discriminating experiment)

Quadrature error `E(n,θ₀) = C(n,θ₀) − C(321,θ₀)` measured on a
θ₀ ∈ [30°,46°] grid at 0.05° step, 600 nm, `incoherent_corrected`,
FWHM=20° held fixed (so P(θ₀) is unchanged by construction), dominant
frequency by least-squares over 20001 trial frequencies:

| n | node spacing h = 100°/(n−1) | predicted 1/h | **measured dominant f** | rms \|E\| |
|---|---|---|---|---|
| 41 | 2.5000° | 0.4000 | **0.4115** | 7.77×10⁻⁴ |
| 61 | 1.6667° | 0.6000 | **0.5865** | 3.02×10⁻⁴ |
| 71 | 1.4286° | 0.7000 | **0.6658** | 4.14×10⁻⁵ |
| 161 | 0.6250° | 1.6000 | (meaningless) | 2.79×10⁻⁹ |

The fringe frequency is fixed at 0.4979 cycles/deg (P=2.0085° at 600 nm/38°)
throughout. The residual's period in θ₀ moves with the *grid*, within ~5%,
and is never near the fringe's. Residual deviations from exact 1/h are
expected — the fringe is chirped (P = λ/(A·cosθ) varies across the ±50°
window) so the alias integral samples a band, not a line.

### E5 — the alias model, scored against the committed numbers

`E_pred = 2Re[ĝ(1/h)] + 2Re[ĝ(2/h)]`, `ĝ(f) = ∫W(u)c(θ₀+u)e^{−2πifu}du/∫W du`,
h = 2.5°, dense scan at 0.01°:

| λ | θ₀ | conv | `C(41)−C(161)` measured | `E_pred` | ratio |
|---|---|---|---|---|---|
| 450 | 36 | inc | −5.206×10⁻⁵ | −5.231×10⁻⁵ | 1.005 |
| 450 | 36 | cor | −7.606×10⁻⁵ | −7.716×10⁻⁵ | 1.014 |
| 450 | 38 | inc | 5.432×10⁻⁴ | 5.437×10⁻⁴ | 1.001 |
| 450 | 38 | cor | 8.879×10⁻⁴ | 8.899×10⁻⁴ | 1.002 |
| 450 | 40 | inc | 4.252×10⁻⁴ | 4.247×10⁻⁴ | 0.999 |
| 450 | 40 | cor | 7.398×10⁻⁴ | 7.377×10⁻⁴ | 0.997 |
| 600 | 36/38/40 | both | — | — | 1.000 (6/6) |
| 750 | 36/38/40 | both | — | — | 1.000 (6/6) |

Pearson r(measured, predicted) = **1.00000** across all 18; median ratio
1.0000. The m=1 term alone already carries 84–109%; m=2 closes the rest.
Note the 450 nm rows: m=1 alone is 6–16% off there and m=2 is *required* —
a detail a Phase-3 implementation must not drop.

### E6 — P-PCDP-4/5 as written

`slope(θ₀)` per §2.2(e), h_step = P/200:

| λ/θ₀ | \|slope_cor\|/\|slope_inc\| | Δabs_cor/Δabs_inc (the thing to explain) |
|---|---|---|
| 450/36 | 1.977 | 1.382 |
| 450/38 | 1.970 | 1.675 |
| 450/40 | 1.249 | 1.658 |
| 600/36 | **0.520** | 1.965 |
| 600/38 | 2.433 | 1.952 |
| 600/40 | 1.563 | 1.921 |
| 750/36 | 3.184 | 2.176 |
| 750/38 | **3.215** | **0.775** |
| 750/40 | 1.548 | 2.258 |

- P-PCDP-4 as scored: 3 of 4 named cells in [1.5,3.0] ✓, but the four-cell
  median is **1.556**, outside the committed [1.7,2.6] → the prediction
  splits, and does so for a reason that is not informative.
- The claim underneath it fails outright: slope ratio vs Δabs ratio,
  **Spearman ρ = −0.300 (p = 0.433)**, Pearson −0.354. The two extreme
  slope-ratio cells (600/36 at 0.520, 750/38 at 3.215) are the two cells
  whose Δabs ratios are *least* extreme / most anomalous respectively. A
  [1.5,3.0] band that a ρ=−0.30 quantity happens to land inside is a band
  wide enough to be hit by an unrelated number, not an explanation.
- The correct quantity (E-change section above) gives 1.664–2.232, median
  1.950, and is *tight within each λ* — which is what an explanation of a
  "reproducible ~1.9–2.3× coincidence" should look like.

### What I am *not* claiming

- Idealization 3 is not the defect. Its concession ("the integrated quantity
  has no simple periodic structure in θ₀") is true and honestly stated; the
  defect is that the *replacement* structure it implies — periodicity at
  P(θ₀) inherited through the sampling — is also absent, and the actual
  structure is periodicity at h.
- No `lab/`, exp-049 or exp-050 file was modified, no FDTD was run, no
  constraint-3/4 claim is made or implied, no `REALIZABILITY_MEMO.md` tier
  is touched, and nothing here endorses or resurrects any RULED-OUT item
  (R1–R4). T1 escape route: NONE, matching §3.
- My `phase_offset` and `slope` are my own faithful implementations of
  §2.2(c)/(e); a Phase-4 implementation may differ in the last digit. The
  *labels* and `Δabs` values are exact (E2 reproduces §2.1's `n*` column
  cell for cell), so E3's falsification of P-PCDP-2 does not depend on
  implementation detail — it depends on the offsets being convention-blind
  to 0.041, which is a property of the physics, not of my code.

### Reproduction

All results above come from four short scripts driving
`experiments/050-n-convergence-a724-geometry/design_geometry.py`'s own
committed functions plus a reduced-row evaluator (object-window + flank rows
only — dropping rows outside both windows cannot change either window mean;
validated to 5×10⁻¹⁴ against the committed function, E1). Total compute for
everything in this critique: **≈4 minutes single-threaded**, well inside the
proposal's own §6 budget — which is itself a point in the proposal's favour
and the reason a Phase-3 swap of the crux regressor costs nothing.
