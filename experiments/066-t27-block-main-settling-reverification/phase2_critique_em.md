# ELECTROMAGNETISM — Phase 2 Critique · Panel Iteration 43 · exp-066 proposal

*Fresh sub-agent, blind to the other four seats' critiques this cycle. Preserved
verbatim as delivered.*

## 1. Steel-man (≤150 words)

Diagnostic 1 (inherited from exp-065) is the load-bearing EM fact this
proposal correctly builds on: the settling defect reproduces on the
**unpadded** C40 anchor geometry itself (74.4% shift), ruling out a
domain-construction artifact and confirming this is a genuine
transient-decay property of the plane/tapered-source channel — consistent
with this program's own Iteration-35 finding (`VALIDATION.md`) that a
near-lossless/undamped channel settles far more slowly than an
absorbing-object channel, since an empty-scene run has no interior σ_e
and depends entirely on the graded-loss bands at the domain edges to
damp its transient. The 4-point trend (1400→2800→4200→5600, flat to four
significant figures) is a real, monotone decay, not noise. Extending the
bit-exact identity gate (G-1′) to the 18 previously-unaudited MAIN cells
before trusting any new number is sound house discipline, and spending
the marginal budget at exactly the wavelength (750nm) where Diagnostic
3's residual already concentrated is the right place to look next.

## 2. Sharpest attack (≤150 words)

No transit-time or causal derivation anywhere in this proposal (or its
exp-065 predecessor) predicts 2800 steps from first principles — it is
read off **one** flattened curve at 40°/600nm/C40 and extrapolated
across five new angles, and (partially) three wavelengths. The
proposal's own candidate mechanism for the persisting 750nm residual
(`ramp_periods·lam/S`, ~75–125 steps even at cpl=25) is two orders of
magnitude too small to explain a multi-thousand-step settling defect;
the real driver is almost certainly light-transit/multipath-bounce time
across the ~750–1500-cell aperture against the imperfectly-absorbing
graded boundary (first-arrival alone is ~800–1100 steps at A=752,
D_SP=223), which this document never computes. Of the 38 new calls,
only 2 test convergence at a *second* (θ,λ) point — **zero** test
convergence at any of the 18 new interior angles (36°/37°/39°) actually
being certified "settled." G-1′ verifies harness reproducibility of the
(unsettled) 1400-step number, not settlement — it cannot stand in for
the missing angle-generalization check.

## 3. Verdict

**Support-with-changes.** The scope, gates, and cost discipline are
sound, and the λ-coherence stress test is a legitimate, well-targeted
use of two calls. But the causal justification for treating STEPS=2800
as licensed across five new angles is thin: it rests on extrapolation
along the wrong axis (λ, tested twice) while leaving the axis that
actually differentiates the 18 new cells (θ) completely unverified.
Given T21's own established ~1–2° fringe period at this geometry —
itself a function of aperture-edge path-length asymmetry, the same
geometric quantity that plausibly sets settling time — there is no
basis to assume 36°/37°/39° share 40°'s convergence behavior rather
than, say, needing more (or fewer) steps at their own phase points in
the oscillation.

## 4. Parameter change that would flip verdict to support

Reallocate 2 of the 38 calls: replace one leg of the 40°/750nm stress
test (keep at least one, e.g. STEPS=4200) with a 1400/2800 convergence
pair at a **new interior angle** (37°/600nm/C40 is the cheapest, since
600nm's period is nearest-Nyquist and best-characterized). That single
addition would make the settling floor's generalization claim rest on
verified evidence along both axes (λ and θ) it is being extrapolated
across, not λ alone.
