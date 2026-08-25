# PHASE 2 — CRITIQUE · QUANTUM OPTICS · Panel Iteration 48 · exp-071

*Seat charter: non-classical absorption, state-dependent or coherent
interactions. Expressibility contract: mechanisms enter the bench only as
effective classical parameters — σ(I), σ(x,t), dispersive ε(ω), gain — or
Red Team strikes them. Fresh context, blind to the other six Phase-2
critiques this cycle.*

## 0. Verification performed

`python3 design_geometry.py` re-run fresh: output reproduces every cited
figure verbatim (`A=752` fixed across all four configs; peak-angle
fractions 0.949/0.984 of window ptp at θ=37.2°/41.4° vs. 0.000·ptp-scale
values at the old 39.0°/40.0° zero-crossing cells; budget 74 calls /
5882.3 CPU-s / 28.76 min wall / 86.28 min envelope; de-scope floor 70
calls / 24.53 min). Independently confirmed `_free_period_search`'s exact
signature in `experiments/069-.../run.py` (`center_deg=39.0, lo_deg=1.0,
hi_deg=4.0, n_grid=400`) and traced its reuse chain: exp-070's
`design_geometry.py` imports the function object directly
(`_free_period_search = run069._free_period_search`, no reimplementation).
No defect in the numbers as reported.

## 1. Steel-man (≤150 words)

This is the correct-shaped experiment for a QUANTUM-charter question. T28
is fundamentally a coherent-superposition puzzle — does a graded-loss
absorption profile σ(x) of a given depth imprint its own length scale on
an interference pattern, or is the pattern set entirely by the fixed
aperture/taper geometry the profile sits inside? `ABSORB` depth is exactly
an effective classical parameter (an absorption-profile length, expressible
per my own charter's contract) rather than a named FDTD bookkeeping
constant, so manipulating it directly — holding `A=752` bit-identical by
assertion — is a genuine, interpretable causal lever the desk-check batch
never had. Reusing `_free_period_search` and `P(θ)` verbatim, zero new
`lab/` diff, and gating everything on a bit-exact G1 identity check before
trusting the reused exp-069 data are all sound, house-consistent
discipline.

## 2. Sharpest attack (≤150 words)

**The R5-addendum argument is narrowly correct but misses the live risk in
its own instrument.** The addendum targets a *combinatorial named-constant*
search; a 4-point `ABSORB` manipulation isn't that, so the proposal is
right that it doesn't literally trigger. But `_free_period_search` is
itself a 400-point grid search for a best-fit period, applied
*independently* four times, over a window (36°–42°, `Δ(sinθ)=0.0813`) that
I computed to be at or below the Fourier/Rayleigh resolution needed to
separate the candidates in play: resolving T21's known 1.9608° fringe from
`P*_delta=2.8421°` requires `Δ(sinθ)≥0.0858` (window supplies 0.948× that);
from `C40`'s own 2.4361° free-fit, 0.597×; and — critically — resolving
`C40`'s 2.4361° from `C80`'s 2.5338° (the 3.93% figure EM leaned on to
disfavor `ABSORB`-tying) needs `Δ(sinθ)≥0.857`, **10.5× more window than
exists**. The window cannot resolve periods that close. So P-071-2's
REFUTE band (≤15% pairwise spread) can fire on resolution-floor
indistinguishability alone, indistinguishable from a genuine null — the
same "search finds *something* regardless of ground truth" shape R5/its
addendum names, just via under-resolution instead of combinatorics.
Idealization 5 calls the 4-point fit's 2 residual d.o.f. a "power" issue
only; it is also a look-elsewhere-adjacent resolution issue the proposal
never computes.

## 3. Elaboration — is the alternative even well-posed, and is the method inherited correctly?

**Well-posedness.** The "shared-geometry origin" alternative (interference
between wavelets diffracted at the fixed aperture edge and/or the `TAPER`
boundary, common to all four configs) is a legitimate classical coherent-
superposition mechanism and satisfies my seat's expressibility contract —
no objection there. My objection is narrower and sharper: the test's power
to *discriminate* that alternative from an `ABSORB`-tied one is bounded by
a computable spectral-resolution floor the proposal never states, and that
floor sits uncomfortably close to both pre-committed decision bands (REFUTE
at 15% pairwise spread; the floor for adjacent real periods in this family
is itself ~10–15% of a period in `Δ(sinθ)` terms at this window size).

**Inheritance check.** `_free_period_search` is confirmed unchanged in
*prose* and in exp-070's own import chain, but exp-071's own
`design_geometry.py` (the only committed code this cycle) never imports or
references it at all — it lives only in exp-069's `run.py`, to be wired up
whichever way the not-yet-written exp-071 `run.py` chooses at Phase 4.
Nothing is broken today, but "identical methodology" is currently a prose
promise, not a code-enforced one; the G1 identity gate checks the reused
*data*, not that the *analysis function object* is the same one imported
by reference (as exp-070 did) rather than re-derived with e.g. a different
`n_grid` or `lo/hi_deg`.

## Verdict

**Support-with-changes.**

## Parameter change that would flip to full support

Before P-071-2/P-071-3 are scored, compute and disclose — in code, not
prose — the Rayleigh/Fourier resolution floor `Δ(sinθ)_window /
|1/T(P1)−1/T(P2)|` for every one of the 6 pairwise comparisons in P-071-3,
and treat any pair whose observed `|P*(Ca)−P*(Cb)|/mean` falls below that
pair's own resolution floor as **unresolved**, not as REFUTE-supporting
evidence — this alone would have reclassified EM's own 3.93% `C40`-vs-`C80`
figure from "disfavors ABSORB-tying" to "not resolvable either way" last
cycle. Secondarily (cheap, same-shift): have exp-071's `run.py`, when
written, import `_free_period_search` by reference from exp-069's `run.py`
exactly as exp-070 did, and assert the imported function's `(lo_deg,
hi_deg, n_grid)` defaults match `(1.0, 4.0, 400)` in code before use, so
"identical methodology" is enforced, not merely claimed.
