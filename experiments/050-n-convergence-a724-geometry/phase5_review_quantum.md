# PHASE 5 — REVIEW (QUANTUM OPTICS) · Panel Iteration 27 · exp-050

## Charter framing

No T1 mechanism is at stake here (this cycle proposes none), so nothing
below touches a σ(I)/σ(x,t)/ε(ω)/gain parameter. My charter's other duty —
non-classical / coherent-vs-incoherent interaction bookkeeping — is exactly
what P-NCONV27-2's REFUTED result is about: three of this bench's own
coherent-sum conventions (`incoherent`, `incoherent_corrected`, `coherent`),
one of which (`beam_divergence_coherent`) is my own mandatory cross-check
function from T21 (Iteration 19), the others its incoherent-limit
comparators. Scrutinizing which of the three is doing something genuinely
different, versus sharing the same underlying physics, is squarely my lane.

## What I verified, and how

Per this program's own R4 rule, nothing below is hand-typed arithmetic.
I re-imported `experiments/050-.../design_geometry.py` directly (the actual
committed module, unmodified) and re-ran `beam_divergence_incoherent`,
`beam_divergence_incoherent_corrected`, and `beam_divergence_coherent` at
`g=GEOM78` for `n∈{41,81,161,321}` at all three violating coordinates —
(600nm,36°), (600nm,40°), (750nm,40°), all FWHM=20° — reproducing
`results.json`'s own `per_cell_summary_geom78` entries and extending them
with the two intermediate `n` values (161, 321) that `results.json` itself
does not store (only `c41`, `c401`, `converged_value`, `nstar`).

**Cross-check against `results.json` (all three functions, all three
coordinates):**

| θ₀ | λ | func | nstar | c41 (sign) | converged_value (sign) | sign flip? |
|---|---|---|---|---|---|---|
| 36° | 600nm | `incoherent` | 41 | +1.182e-4 | **−2.321e-4** | **yes** |
| 36° | 600nm | `incoherent_corrected` | 81 | +3.173e-4 | **−3.722e-4** | **yes** |
| 36° | 600nm | `coherent` | 81 | −0.9146 | −0.9159 | no |
| 40° | 600nm | `incoherent` | 41 | +5.663e-4 | +8.723e-4 | no |
| 40° | 600nm | `incoherent_corrected` | 81 | +1.777e-4 | +7.660e-4 | no |
| 40° | 600nm | `coherent` | 41 | −0.9797 | −0.9797 | no |
| 40° | 750nm | `incoherent` | 41 | +1.115e-3 | +7.216e-4 | no |
| 40° | 750nm | `incoherent_corrected` | 81 | +1.590e-3 | +7.010e-4 | no |
| 40° | 750nm | `coherent` | 41 | −0.9766 | −0.9766 | no |

All figures match `results.json`'s committed rows exactly.

## Finding 1 — the proposed mechanism (H-vs-E convention creates a
physically distinct sign-crossing unique to `incoherent_corrected`) is
**RULED OUT**, directly, not by inference

`incoherent` — the obliquity-on-E convention, structurally unrelated to
Faraday's law/H-field bookkeeping — shows the **identical sign flip** at
(36°,600nm): +1.182e-4 → −2.321e-4, the exact same n=41→81 transition step,
the same direction, comparable relative magnitude. At (40°,600nm) and
(40°,750nm), neither convention flips sign at all; both instead show a
large **same-sign** relative jump (54–125%) settling toward a smaller-
magnitude asymptote between n=41 and n=81. **Only one of the three
"violating" cells (36°,600nm) is actually a sign crossing** — NOTES.md's
Reading section describes all three under one "sign flip... near a sign
crossing" characterization, which over-generalizes; the other two are
same-sign magnitude collapses, a related but distinct near-zero
symptom. Worth a same-shift wording correction, non-load-bearing.

Since `incoherent` uses none of `incoherent_corrected`'s H-field/Faraday's-
law bookkeeping and still reproduces the same qualitative instability at
the same three coordinates, **the H-vs-E convention difference is not the
origin of this pathology.** Both conventions are evaluating the same
underlying coherent aperture sum (`_geom_derived`'s shared `G0`, `amp`,
`obliquity`) at (θ₀,FWHM,λ) cells where the *converged, physically real*
answer is a near-total cancellation across the FWHM=20° angular window —
consistent with, and explainable by, the already-established T21
edge-diffraction fringe (period ~1.9–2.6° at these λ,θ, LOGBOOK T21) being
under-resolved at n=41 within a ~20°-wide integration window. This is a new
INSTANCE of the near-|C|≈0 ill-conditioning class I flagged at Iteration 26
(`P-NCONV26-2`'s correlation metric) — same general regime, same general
cause (a genuinely small denominator/near-cancellation quantity meeting a
fixed absolute tolerance), but a structurally different metric
(`find_nstar`'s doubling-step criterion, not a Spearman ratio) and,
crucially, **not specific to one propagator convention** — it is a property
of where the *weighted angular integral* itself sits near zero, which both
`incoherent` and `incoherent_corrected` inherit from the same source
physics.

## Finding 2 — a real, unexplained, convention-dependent AMPLITUDE
asymmetry, not previously documented

Direct code trace (`design_geometry.py:67-79` vs `experiments/048-.../
design_geometry.py:207-219`, `field_and_h`) shows `incoherent`'s per-angle
profile is literally `|H|²` — the **same H array** `beam_divergence_
incoherent_corrected` builds (`G0 * gd["obliquity"]) @ amp`), just squared
against itself instead of cross-multiplied against the un-oblique `E`.
`incoherent_corrected`'s profile is `-Re(E·conj(H))`. The two conventions
are not independent computations; they are two different real-valued
functionals (self-product vs. cross-product) of the identical complex field
pair `(E,H)`.

Computing the n=41→81 step size `Δabs` at all three coordinates:

| θ₀,λ | Δabs, `incoherent` | Δabs, `incoherent_corrected` | ratio |
|---|---|---|---|
| 36°,600nm | 3.493e-4 (passes, 30% under ABS_TOL) | 6.864e-4 (fails, 37% over) | **1.97×** |
| 40°,600nm | 3.065e-4 (passes, 39% under) | 5.887e-4 (fails, 18% over) | **1.92×** |
| 40°,750nm | 3.925e-4 (passes, 22% under) | 8.862e-4 (fails, 77% over) | **2.26×** |

`incoherent_corrected`'s refinement jump is **consistently ~1.9–2.3× larger
in absolute magnitude than `incoherent`'s, at all three coordinates
independently** — not one lucky/unlucky draw against a fixed boundary but a
tight, reproducible ratio across two wavelengths and both flagged θ₀ values.
This is the genuinely deeper fact NOTES.md's own candidate explanation
(§Reading) does not surface: **why `incoherent_corrected` trips the
ABS_TOL=5×10⁻⁴ boundary at exactly these three cells while `incoherent`
does not is not coincidence-of-placement alone** — `incoherent_corrected`'s
n-refinement step is systematically larger here, for a reason not yet
derived (candidate: the cross-term `-Re(E·conj(H))` is more sensitive to
the *relative phase* between the E- and H-aperture sums than `|H|²` is to
`H`'s own phase alone, since a phase-sensitive cross-term can swing through
zero from *either* operand drifting, while a self-product only needs its
one operand to drift — untested this cycle, flagged for Iteration 28).

## Why `coherent` is uninformative here, not evidence of stability

`coherent` never approaches this regime at these three coordinates
(|C|≈0.91–0.98 throughout, changing by <0.2% under refinement) — but that
is because at FWHM=20° `coherent`'s own dominant physics is the
Iteration-23 beamformed/grating-lobe-replica construction (a near-total
synthetic-aperture shadow reading, T21 LOGBOOK entry), not because the
coherent-sum convention is inherently immune to near-zero cancellation.
`coherent`'s stability at these specific cells says nothing about the
mechanism question; it is simply evaluating a different regime of its own
integrand at FWHM=20°.

## Verdict

**RULED OUT** (the specific proposed mechanism): a genuine physical
sign-crossing unique to the single-obliquity-via-H convention, not shared
by the obliquity-on-E conventions — refuted directly, by running
`beam_divergence_incoherent` at the same three coordinates and finding the
identical sign flip (36°,600nm) and identical same-sign near-zero
instability (40°,600nm; 40°,750nm) it was hypothesized not to share.

**PROMISING** (the underlying open question, sharpened, not closed): the
near-|C|≈0 ill-conditioning itself is real and recurring — a shared
symptom of both incoherent conventions evaluating a genuinely
near-cancelling angular integral at n=41, consistent with T21's own
established under-sampled-fringe mechanism generalized from single-angle
sweeps to divergent-beam integrals for the first time. NOTES.md's own
candidate explanation (b) — "ABS_TOL comparable to the values themselves" —
is CONFIRMED as the proximate trigger (directly verified, not merely
plausible), but is now shown to sit on top of a **second, novel, tightly
reproducible finding this cycle's own Reading section missed**: a ~2×
convention-dependent amplitude asymmetry in the n=41→81 refinement step,
consistent across all three cells, that is the actual reason
`incoherent_corrected` — and only `incoherent_corrected` — crosses the
fixed boundary here while `incoherent` does not.

## Ranked candidates for Iteration 28

1. **[Top priority]** A dedicated near-zero-crossing/sign-flip
   investigation, scoped narrowly: derive (or numerically bound) why
   `-Re(E·conj(H))`'s n-refinement step is systematically ~2× `|H|²`'s at
   near-null cells — a concrete, falsifiable, zero-FDTD desk question
   (does the ratio hold at OTHER near-null cells not yet found, e.g. a
   deliberate search across the full 108-combination grid for every cell
   with `|converged_value| < 5·ABS_TOL`, not just these three found by
   coincidence this cycle).
2. **A structural fix to `find_nstar`'s own criterion**: flag any
   cell-function combination whose `converged_value` itself is smaller in
   magnitude than a fixed multiple of `ABS_TOL` (e.g. `|converged_value| <
   3·ABS_TOL`) as "tier index not meaningful — near-cancellation regime,"
   reported separately from genuine under-sampling failures. As currently
   built, `find_nstar`'s tier assignment in this regime measures which side
   of an arbitrary fixed boundary a numerically tiny near-cancellation
   lands on, not a meaningful convergence-difficulty ranking — the same
   metric-vs-physics conflation this seat's Iteration-26 catch addressed
   for the correlation metric, recurring here in the tier-convergence
   metric itself.
3. **Extend this cycle's own three-coordinate spot check to the full grid**:
   compute `Δabs` for both `incoherent` and `incoherent_corrected` at every
   FWHM=20° cell (not just the 3 that happened to trip the boundary) to
   check whether the ~2× ratio is a general property of the two
   conventions or specific to these near-null cells — settles whether
   candidate 1's mechanism is a general fact about the two functionals or
   an artifact of proximity to cancellation.
4. Lower priority: no FDTD validation exists for any of these three cells
   at GEOM78 (idealization 5, this cycle) — before any of this is cited
   near a real constraint-3 boundary, at least one of the three should be
   checked against a live FDTD run, not just the desk propagator.
