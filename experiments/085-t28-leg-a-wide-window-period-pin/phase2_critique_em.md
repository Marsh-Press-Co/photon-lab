# PHASE 2 — CRITIQUE · ELECTROMAGNETISM · Panel Iteration 62 · exp-085

*Fresh context, blind to other seats' current-cycle critiques.*

## Steel-man (150 words)

Leg (a)'s Green's function is exact — `G0=exp(i(kr−π/4))/√r` with
`r=hypot(D_SP, y−y_p)`, never the Fresnel/Fraunhofer quadratic-phase
truncation — verified directly in `dg048.field_and_h`. Extending its
evaluation from the established 6° window to `[2°,80°]` therefore adds no
new physics, only more samples of an already-validated, already-gated
function (exp-042/046 pedigree). The three-way STABLE/DRIFTING/NOT-STABLY-
PERIODIC taxonomy is the epistemically correct move: it refuses to presume
stationarity, which the exact hypot phase does not guarantee — a
stationary-phase reading (the steering angle moves a stationary point on
the aperture whose local curvature, not a fixed grating spacing, sets the
local fringe spacing) correctly predicts a θ-dependent instantaneous
frequency, i.e. chirp — an accurate, verified attribution to EM's own
exp-084 Phase-5 finding (§2.2 there says exactly this). Method B's FFT is a
genuinely independent instrument (unbounded, multi-peak-capable), not a
restatement of Method A's bounded matched-filter search. R4 sourcing is
clean throughout; zero new FDTD, zero engine change.

## Sharpest attack (150 words)

Method C's chirp diagnostic is quantitatively broken by its own reused
machinery. `free_period_with_widening` hardcodes `center_deg=39.0` inside
its call to `_free_period_search` (confirmed directly in
`y_wall_prescreen.py`), so all 37 sub-windows (θc=5°…77°) convert their OWN
local sin(θ)-period `Tc(θc)` back into "`P_local(θc)` degrees" via a FIXED
`cos(39°)`, never `cos(θc)`. A genuinely θ-invariant local period `P0`
(correctly, locally referenced) reports under this code as
`P_local(θc)=P0·cos(θc)/cos(39°)` — `1.28·P0` at θc=5°, `0.29·P0` at
θc=77°: a strong, monotonic, purely-artifactual trend that mechanically
satisfies DRIFTING's own `|ρ|≥0.5`/`spread>0.15` bar regardless of whether
the underlying physics chirps at all. As specified, Method C cannot
distinguish real chirp from this labeling artifact — it needs
`center_deg=θc` per sub-window, or an explicit `d(sinθ)/dθ` Jacobian
correction applied to `P_local` before `spread`/`ρ` are computed, or its
STABLE/DRIFTING call is uninterpretable.

## Verdict: **support-with-changes**

Two more points, both explicitly asked of this seat:

**Sin(θ) as the Fourier-conjugate variable.** It is exact — not paraxial —
for the angular-spectrum decomposition of a field's transverse-position
dependence at a fixed plane (k_y=k·sinθ is exact at any range). But that is
not quite what Method B measures: θ here is the source aperture's own
*steering* angle (`_src_amp`'s linear phase ramp), swept while the
observation window stays fixed at one near-field plane. Steering angle and
observation angle are reciprocally interchangeable — and sin(θ) is
guaranteed the right conjugate for *both* — only in the far field; the
whole premise of this proposal is that D_SP sits at 0.2% of Fraunhofer
range. The proposal never derives that sin(θ)-periodicity survives this
near-field steering/observing distinction, only asserts it because the
established convention already uses it. Not fatal (θ-space is denser
non-uniformly and arguably no better a priori), but worth stating plainly
rather than assuming.

**R10's carve-out.** R10's deterministic-curve clause explains how to
*read* a circular-shift result on a zero-noise curve (a self-similarity
question, "how much does the curve's own smoothness alone explain a good
fit") — its own worked example is this exact curve family, exp-084's leg
(a), where that circular-shift test is precisely what forced the
SUPPORT→INCONCLUSIVE downgrade this program now treats as binding
precedent. Nothing in R10's text licenses *skipping* the test for a
deterministic curve; the clause is interpretive, not an exemption, and R10
was adopted the same cycle specifically because a specificity sweep alone
(which this proposal does run) was shown insufficient. Compounding this:
the proposal's own physical account — genuine near-field chirp — is
exactly the situation where a fixed-period R² is *most* likely to be a
smoothness artifact rather than real periodic structure, since a smoothly
chirping curve is not a stationary tone and a "best single period" is by
construction a lossy summary of it. Citing R10 to justify omitting the one
test purpose-built for this proposal's own claimed physics is
self-undermining, not supportive.

## Parameter change that would flip my verdict to support

(1) Re-reference Method C's local-period conversion to `center_deg=θc` per
sub-window (or apply the `cos(θc)/cos(39°)` correction before scoring
`spread`/`ρ`), and (2) add a mandatory order-preserving circular-shift null
on the wide/dense Method A curve — same staged-widening refit machinery,
shifted copies of the `[2°,80°]` curve — as a required co-gate before any
STABLE or period-match outcome is reported as evidence, exactly as R10's
own rule requires and as this cycle's central physical claim (chirp) makes
more, not less, necessary.
