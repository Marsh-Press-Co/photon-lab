# PHASE 2 — CRITIQUE (PHOTONICS) · Panel Iteration 27 · exp-050

## Steel-man (≤150 words)

The proposal's central physics claim is exact algebra, not approximation:
because the T21 fringe period P(θ)=λ/(A·cosθ) depends on A only through a
single scalar, and the angular sampling step in `gaussian_angle_weights`
depends only on n and FWHM — never on A — the ratio of samples-per-period
between GEOM78 and GEOM_EXP042_OLD is a geometry-independent constant,
752/724=1.038674, verified identically at all nine (λ,θ) combinations in
§2.4, not merely asserted. The mandatory 108-row regression anchor (§2.3)
directly repairs last cycle's own Attack-7 defect (an unexecutable
regression gate). Every idealization — the twice-compounded analogy gap,
T24's ABSORB systematic being A=752-only, the propagator's own magnitude
validation being untested at A=724 — is disclosed inline, not smoothed
over. No mechanism, no T1 route, nothing here can move a
REALIZABILITY_MEMO tier: scoped exactly as an instrument-fidelity cycle
should be.

## Sharpest attack (≤150 words)

P-NCONV27-2's hard-falsification clause — "any combination moves to a
larger tier" refutes the period-growth argument outright — over-trusts a
model exp-049 itself only PARTIALLY validated as a difficulty predictor:
the identical T21-period/Nyquist analogy scored ρ=0.45–0.48 against
measured Δrel magnitude at A=752, below the 0.70 CONFIRM bar, and Red
Team's own Iteration-27 priority #3 names the missing ingredient as each
cell's PHASE offset within the fringe, not period alone. §2.4 is exact
about how the period's magnitude shifts but silent on phase, and phase —
not period — is what actually decides where a given (θ,FWHM,λ,n) sampling
grid lands within a cycle. A single cell whose phase offset moves
unfavorably under the 3.87% stretch (a real possibility the weak ρ leaves
open) would trip the hard-falsification clause and be misread as "the
period argument is wrong" when the honest diagnosis is "the period
argument was never phase-complete."

## Verdict

**Support-with-changes.**

The geometry arithmetic (§2.1), the fringe-period ratio (§2.4), the
samples-per-period figures, and the regression-anchor design (§2.3) all
check out independently against `experiments/042-.../design_geometry.py`,
`experiments/048-.../design_geometry.py`, and exp-049's own committed
`results.json` — no arithmetic or citation defect found. The physics is
coherent as *stated*; my objection is that one falsifiable prediction
(P-NCONV27-2) states its hard-falsification condition more confidently
than the cited evidence for its own governing model supports.

## Parameter change that would flip to full support

Add one sentence to P-NCONV27-2's hard-falsification clause: a single
FWHM=20°/coherent cell moving to a strictly larger N_SERIES tier does
**not**, by itself, falsify the period-growth argument if that cell's own
41→81 phase offset (relative to its local fringe period, at both
geometries) can be shown to have shifted unfavorably despite the period
growing — i.e., pre-register the phase-offset diagnostic (Iteration-27
priority #3) as the tie-breaker for exactly this failure mode, rather than
letting one phase-driven outlier be scored as refuting a period-only
argument it was never built to fully explain.
