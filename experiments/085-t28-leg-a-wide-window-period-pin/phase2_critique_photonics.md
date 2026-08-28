# PHASE 2 — CRITIQUE · PHOTONICS · Panel Iteration 62 · exp-085

## Steel-man (verdict-independent)

The core move is optically sound. This bench's source aperture sits at
0.197% of its own Fraunhofer distance (verified against source: `D_SP=223`
cells, `A_full²/λ=1504²/20=113,101` cells) — deep Fresnel regime, where a
fixed-period grating description (`P_edge_B=λ/(A·cosθ)`, already REFUTEd)
has no first-principles license. A finite, edge-tapered aperture genuinely
can present a non-stationary (chirped) angular fringe pattern in this
regime — exactly what EM's own exp-084 Phase-5 review flagged qualitatively
("genuine near-field diffraction is expected to be chirped") and this
cycle now proposes to actually test rather than re-assert. Re-evaluating
the already-validated `edge_diffraction_c_empty_corrected` over a wider,
denser, zero-cost domain is the right next move to distinguish "weak chirp,
one dominant tone still describes it" from "no single period exists" —
the two outcomes §1 itself states are both a priori plausible. Citations
check out against the actual committed code, and the R5 specificity
control is correctly re-applied to the wide fit.

## Sharpest attack

§1's own physics (deep-Fresnel, chirped fringe) predicts the model curve
has NO single stationary period over a wide window — yet both
confirmatory tools test exactly the hypothesis §1 argues is likely false.
Method A (`free_period_with_widening`) is a global least-squares fit to
ONE fixed period across the entire 78°-wide domain; Method B is an
un-windowed, hard-truncated FFT over the same domain — also a
global-stationarity read. A genuinely chirped signal will smear or
underperform on BOTH regardless of whether real near-field structure
exists, so a weak Method-A/B result cannot discriminate "no periodicity"
from "genuine near-field chirp too broadband for a single-tone test" —
only Method C (local sub-windows) actually probes that hypothesis, yet
the falsifiable bands in §4(a) require Method B's peak-sharpness to
*corroborate* Method C before DRIFTING/STABLE is called. Calling A and B
"genuinely independent" checks is optically misleading — they are two
implementations of one stationary-tone question. Separately: an unwindowed
FFT over a rectangular-truncated domain will itself generate sidelobe
leakage that can mimic the "smeared/broadened peak" signature Method B
reads as evidence of chirp — an ordinary diffraction-integral windowing
pitfall, undisclosed anywhere in the parameter table or idealizations.

## Verdict: support-with-changes

The near-field/chirp framing is coherent, falsifiable optics and a real
advance over re-litigating one null-limited window — worth running. But
as designed, a "NOT STABLY PERIODIC" or ambiguous Method-A/B reading would
be systematically over-read as ruling out the mechanism, when it may only
mean the wrong instrument was applied to a correctly-predicted chirped
signal; Section 4 should state up front that a poor global fit is
uninformative between those two readings, and Method C's local trend
(`ρ`, `spread`) should be treated as primary, not merely corroborating.
Add a Hann/Tukey taper before Method B's FFT. The `θ<2°`/`>80°` exclusion
is adequately justified at the grazing end (vector/polarization validity)
but under-argued at the near-normal end: θ near 0° is close to this
phased-taper source's own main-lobe pointing direction, a physically
different regime from the edge-diffraction sidelobe fringes the mechanism
is about — Method C's sub-windows there (θc=5°,7°,9°) may be measuring
main-lobe curvature, not edge fringes, and this is never addressed.

## Flip

Section 4 states "No circular-shift null is run on the wide curve — per
R10's own explicit carve-out: this curve is deterministic and zero-noise
by construction, so a null-under-noise question does not apply." This
misreads R10. R10's deterministic-curve clause (adopted specifically
because exp-084 ran a circular-shift on this SAME `leg_a_curve()` function)
says the test still runs and answers a *self-similarity/specificity*
question, not that it is skipped: "both are legitimate uses of the same
test... for a curve that has no noise in it at all." R10's own escalation
clause fires Checkpoint criterion 4 on a cycle that "omits the mandatory
circular-shift baseline entirely." Running a circular-shift on Method A's
wide/dense fit (correctly reinterpreted, per R10, as "how much does the
curve's own smoothness alone explain an apparently good global fit over a
huge, densely-sampled domain") before any STABLE/period-match verdict is
reported would flip my verdict to support outright.
