# PHASE 2 — CRITIQUE · Panel Iteration 28 · Seat: PHOTONICS

*Blind. Written without sight of any other seat's current-cycle critique.
Every number below was produced by executing the proposal's own §2.2
machinery, rebuilt from its prose, against already-committed code — not
hand-computed (R4). Scratch code and raw output paths are listed at the
end.*

---

## Steel-man (≤150 words)

The predictor is anchored in machinery I could actually execute, not in
prose. I rebuilt §2.2(a) from the proposal's own pseudocode and it
reproduces exp-042's committed `edge_diffraction_c_empty` and
`edge_diffraction_c_empty_corrected` to **0.0 relative error** at all 9
(θ₀,λ) spot points, both conventions — P-PCDP-0 will pass, and every
downstream number inherits already-magnitude-validated optics (exp-042
Block MAGNITUDE). §2.1's tier table reproduces
`results.json::per_cell_summary_geom78` digit for digit (7 unstable / 11
stable, re-counted). The target is physically real: genuine
destructive-interference nulls of the FWHM=20° angular integral, with
|C| at the null 10⁻⁴–10⁻³ against a single-angle fringe whose full swing
across θ∈[34°,42°] I measure at 6.5×10⁻³–1.1×10⁻². Asking where θ₀ sits
inside that fringe is the right first question, it costs no FDTD, and a
REFUTED result still retires EM's Iteration-26 "missing phase term"
conjecture.

## Sharpest attack (≤150 words)

**Both regressors are convention-blind; the label is convention-determined.**
Running §2.2 at GEOM78 I get, at the *same* (θ₀,λ), |offset| differing
between the two conventions by only 0.0005–0.135 (mean 0.038) and
log₁₀(|C(81)|/ABS_TOL) by <0.30 — yet the tier label flips between
conventions at **4 of 9** (θ₀,λ) cells, and 6 of 7 positives are
`incoherent_corrected`. Optically that is expected: the conventions
differ in where cos ψ (0.65–1.0 across the scored windows, exp-042's own
self-check) multiplies the flux, not in the fringe's *angular phase*.
Computed consequence: |offset| alone gives AUC **0.649**; the 2-feature
fit **0.597** in-sample; and **no threshold in [0.05, 0.40] reaches
sensitivity ≥5/7 and specificity ≥7/11** — P-PCDP-2's own hard-falsification
clause, met before the run. Meanwhile "predict unstable iff convention ==
corrected", carrying zero phase information, scores sens **6/7**, spec
**8/11** — exactly P-PCDP-2's *success* bar.

## Verdict

**support-with-changes.** The cycle is cheap, honest, and R4-clean, and
its regression anchor is bit-exact. But as frozen it spends its budget on
two regressors that cannot, by their own optics, carry the convention
asymmetry the task was queued to explain — and its fallback prediction is
already hard-falsified at the desk.

## The single change that would flip me to support

Pre-register **convention identity as the null model P-PCDP-1/-2 must
beat** (it already scores sens 6/7, spec 8/11 / AUC 0.792), and score the
phase features on *incremental* discrimination over that null, per
convention, rather than on absolute AUC over the pooled 18. A predictor
that cannot beat "which convention is it" has not explained the 1.9–2.3×
asymmetry, whatever its pooled AUC says.

---

## Verified numbers and corrections for the Director (reference, not part of the attack)

**1. The phase offset is not a phase at this geometry.** §2.2(c) reads
`offset≈0 ⇒ node`, `offset≈±0.5 ⇒ antinode`, which requires the fringe's
zero crossings to recur at P/2. Measured, on the very function §2.2(a)
defines (GEOM78, θ∈[34°,42°], 0.02° step, both conventions), the
crossing-to-crossing gaps are:

| λ | gaps / P(38°) |
|---|---|
| 450 nm | 1.24, 1.28, 1.13 (inc) · 1.27, 1.24, 1.10 (corr) |
| 600 nm | 1.02, 0.63, 0.19, 1.00 (inc) · 1.07, 0.58, 0.35, 0.89 (corr) |
| 750 nm | 1.17, 0.47, 0.14 (inc) · 1.13, 0.43, 0.36 (corr) |

Spread **0.137 P – 1.279 P (9.3×)**, and at 450 nm the crossings are
~1.2 P apart, i.e. the fringe's full sign-oscillation period is ≈2.4×
the `P(θ)=λ/(A·cosθ)` the proposal normalizes by (idealization 4, "used
exactly as LOGBOOK states it"). Dividing (θ₀−θ_zero) by P and wrapping
into (−0.5, 0.5] therefore does not produce a phase, and the wrap can
alias a genuinely-far offset (0.61) back into 0.39.

**2. `NOT_FOUND` fires on 2 of the 7 positives, not as a rare diagnostic.**
At 450 nm/38° the ±0.6·P window contains **no** sign change in either
convention (crossings at 36.992°/38.919° and 37.063°/38.938°; the window
is 38±0.904°, missing them by 0.10° and 0.02°). That is the "masked 4th
cell" §2.1 deliberately added. Widened to 1.5·P the offsets land at 0.390
and 0.378 — the bin §2.2(c) calls "antinode … far from the pathology" —
for the one cell that is tier-unstable in *both* conventions. Idealization
5's completeness ledger is therefore load-bearing, not cosmetic, and the
0.6-vs-1.5·P window choice is not a free resolution knob.

**3. P-PCDP-1's estimator is unstable at N=18.** A converged 2-feature
logistic gives in-sample AUC 0.597 and LOOCV-AUC 0.000 — the classic
small-sample leave-one-out anti-correlation, not a physics result. The
0.85 / 0.65 bands are being applied to a statistic whose variance at
7-positive/11-negative is larger than the gap between them; idealization 6
concedes the sample is thin but the bands are still scored as if the
estimator were stable.

**4. Three small, checkable errors in §2.2.**
(a) `local_period_deg(...)` is called with `g["A"]`, but neither `GEOM78`
nor `GEOM_EXP042_OLD` (`experiments/048-.../design_geometry.py:145-158`)
contains an `A` key — `A` must be derived as `OBJ_Y − ABSORB`, as the
proposal's own prose says two lines later.
(b) §2.2(c)'s comment `window = 0.6 * P  # >= 1 full period on each side`
is arithmetically false — 0.6 P per side is 0.6 of a period, and finding
1 confirms it (see 2 above).
(c) §2.0/§2.2(a) present *both* single-angle functions as new
generalizations; the corrected one already exists, geometry-parameterized
and committed, as
`experiments/048-.../design_geometry.py::edge_diffraction_c_empty_corrected(theta,lam,g)`.
Only the obliquity-on-E variant is genuinely new. This does not change the
cost note materially but the provenance line should cite exp-048, not
exp-042, for the corrected half.

**5. Full offset / regressor table as I measure it** (GEOM78, FWHM=20°,
n_grid=601 over ±0.6·P, 1.5·P widening where noted; `y=1` = tier-unstable
per `results.json`):

| λ | θ₀ | conv | y | \|offset\| | \|C(81)\|/ABS_TOL |
|---|---|---|---|---|---|
| 450 | 36 | inc | 0 | 0.4049 | 0.118 |
| 450 | 36 | corr | 0 | 0.4193 | 0.361 |
| 450 | 38 | inc | 1 | 0.3899\* | 0.449 |
| 450 | 38 | corr | 1 | 0.3780\* | 0.097 |
| 450 | 40 | inc | 0 | 0.3968 | 2.176 |
| 450 | 40 | corr | 1 | 0.3830 | 2.053 |
| 600 | 36 | inc | 0 | 0.3372 | 0.462 |
| 600 | 36 | corr | 1 | 0.3198 | 0.738 |
| 600 | 38 | inc | 0 | 0.0405 | 0.122 |
| 600 | 38 | corr | 1 | 0.1084 | 0.163 |
| 600 | 40 | inc | 0 | 0.1552 | 1.746 |
| 600 | 40 | corr | 1 | 0.1294 | 1.533 |
| 750 | 36 | inc | 0 | 0.4773 | 0.776 |
| 750 | 36 | corr | 0 | 0.4768 | 1.006 |
| 750 | 38 | inc | 0 | 0.1782 | 0.226 |
| 750 | 38 | corr | 0 | 0.0979 | 0.419 |
| 750 | 40 | inc | 0 | 0.4680 | 1.445 |
| 750 | 40 | corr | 1 | 0.3334 | 1.408 |

\* = `NOT_FOUND` at ±0.6·P, widened to 1.5·P (finding 2).

**Method note / limits of my own numbers.** I used `n_grid=601` over
±0.6·P (the proposal's Phase-3-tunable 4001 would sharpen each crossing to
~10⁻⁴ P; my grid resolves them to ~2×10⁻³ P, far finer than any of the
effects above) and linear interpolation to the crossing, exactly as
§2.2(c) specifies. `|C(n=81)|` is a fresh call to exp-050's own committed
`beam_divergence_*` at GEOM78, per §2.2(d). My logistic is hand-rolled
(no sklearn in this environment), so treat 0.597/0.000 as
implementation-dependent; AUC 0.649, the threshold scan, and the
convention-baseline 6/7 & 8/11 are pure order statistics and are not.
Nothing under `lab/`, exp-049 or exp-050 was modified; scratch code lives
in `/tmp/claude-0/-home-user-photon-lab/3f566c8d-1309-5c26-a429-8ae6c0875c6b/`
(`scratchpad/probe.py`, `probe2.py`, `probe3.py`).
