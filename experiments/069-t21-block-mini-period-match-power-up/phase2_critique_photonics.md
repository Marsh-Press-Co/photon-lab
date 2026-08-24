# PHASE 2 — CRITIQUE · PHOTONICS · exp-069 (Block MINI power-up)

## Steel-man (150 words)

The §4 reformulation is a genuine improvement, not cosmetic. Fitting against
`sinθ` with period `T = cpl/A` fixed rather than `θ` linearly correctly
absorbs the ~9% period drift across the 36°–42° window (`P(36°)=1.88°` vs
`P(42°)=2.05°`, both computable from the established `P(θ)=λ/(A·cosθ)`
formula) that a naive fixed-θ-period fit would blur. Going from 0.5°/1°
sampling to 0.2° gives ≈10 samples/period at 600 nm — solidly above Nyquist
for the first time on this channel, where every prior pass (Block MINI's
original 5 points, the STEPS-delta desk check at 1° step) sat at or below
it. The fixed-period 3-parameter linear fit is well-posed by construction,
sidestepping the nonlinear-fit-convergence risk a free-period fit would
carry into a REFUTE-band citation. Pairing this with the first-ever 3-point
C80 convergence trend (Block SETTLE-C80) finally controls the one variable
(settling) that made every prior version of this test structurally unable
to discriminate mechanism from artifact.

## Sharpest attack (149 words)

Idealization #2's justification for 600nm-only is backward. It cites the
desk check's flip-fraction (600nm=1.0 vs 450nm=0.6, 750nm=0.8) as evidence
600nm is "least aliasing-prone." But `samples_per_period_at_1deg_step` is
0.5027 at 600nm — almost exactly 2 samples/period, i.e. Nyquist-critical —
versus 0.67 (450nm) and 0.40 (750nm). A perfect 1-cell-period alternation
at that sampling rate is the textbook symptom of aliasing, not clean
signal: it cannot distinguish a true `P≈1.99°` fringe from an alias of a
different frequency. This is the program's own stated reading of this
exact effect (LOGBOOK T21, Iteration 19: 600nm's near-Nyquist period
"should show the cleanest sign-alternation... exactly what the data
shows" — offered there as an aliasing explanation, not a cleanliness
merit). So the wavelength picked for the one "decisive... for good" test
is the one whose pilot diagnostic is least interpretable, while 750nm —
which carries the largest established fringe amplitude, `c*=3.23` vs
600nm's 2.74 (exp-042) — is deferred entirely.

## Verdict

**Support-with-changes.**

## Parameter change that would flip to full support

Add a confirmatory sub-sweep at 750nm (θ∈[38°,41°], 0.2° step, ≈16 points,
2 configs) alongside the 600nm run. Cost is trivial against the proposal's
own budget (measured wall ≈19 min vs a 75 min hard stop) and closes the
one-wavelength generalization gap without touching the combined-verdict
machinery (§4's statistic is per-λ by construction). Absent that, the
combined verdict should be reported explicitly as 600nm-only, not as
closing T21/T24/T27's mechanism question for the channel generally.
