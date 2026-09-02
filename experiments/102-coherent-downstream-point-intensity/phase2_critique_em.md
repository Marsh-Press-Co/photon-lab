# Phase 2 — Critique (ELECTROMAGNETISM, blind)

## Steel-man

κ(θ) is the physically correct successor to `sigma_scat_downstream`: it
reads the TOTAL-field complex phasor `Ez_article` at a point, so any
destructive interference between incident and scattered contributions is
already baked into `|Ez_article|²` — no explicit phase subtraction is
needed to get the coherent answer exp-101's Learned section called for.
The design also correctly separates what needs a shared time origin from
what doesn't: κ is a same-run-pair magnitude-squared ratio, invariant to
any absolute-phase/registration offset between the two legs, while
Δφ — which *would* need matched origins — is honestly left unscored. I
verified `I0_corrected` against `_face_flux`'s own `sx()`/`sy()` primitives
directly: it is the genuine direction-agnostic Poynting magnitude, not a
re-hash of `i_inc`, closing the R9 commensurability gap exp-101's QUANTUM
finding identified rather than merely asserting closure. T1 route N/A is
correct; no mechanism or passivity claim is at stake in an unmodified
article.

## Sharpest attack

`P_off(θ) = (P_x(θ), P_y(θ)+450)` is NOT a lateral offset from the beam —
it's a fixed lab-frame Δy added to an already beam-rotated point, and
decomposing it into the proposal's own `u(θ)`/`v(θ)` basis shows why that
matters: `Δy=450` splits into `a=450·sinθ` along-beam and `b=450·cosθ`
truly lateral. At the six committed angles, `a` ranges **271.6–306.7
cells**, not the ~0 a matched-distance lateral check requires — `P_off`
sits **471.6–506.7 cells** downstream of the object along the beam axis
(2.4–2.5× `D_STANDOFF`=200), a materially different point in the
diffraction pattern's near-field evolution, not the same z-slice sampled
off to the side. Prediction 3 (`κ_off≥0.90`) therefore risks passing or
failing on where THIS point sits in Fresnel ringing at a different
standoff, not on whether the primary shadow is spatially localized — the
localization check can be satisfied or violated for reasons unrelated to
what it's claimed to test. This is the same fixed-lab-frame failure
SHAPE T28 diagnosed twice already (`beam_behind_t28`, exp-100;
`back_frac`, exp-101) — for the SECONDARY point, inside the very cycle
built to retire that pattern for the primary one. Disclosed as an
"idealization," but the magnitude of the confound (a matched or exceeded
b) is undisclosed and load-bearing for Prediction 3's validity.

## Verdict

**Support-with-changes.**

## Parameter change that would flip to full support

Replace the off-axis offset with `P_off(θ) = P(θ) + Δ_lat·v(θ)` (offset
purely along the beam-perpendicular unit vector already defined in the
proposal, `v(θ)=(sinθ,cosθ)`), choosing `Δ_lat` to still clear the
~312-cell shadow diameter — this keeps `P_off` on the same beam-axis
z-slice as `P(θ)` (a=0 by construction) so Prediction 3 tests localization
at matched downstream distance, not a conflated distance-plus-offset
point.

## RULED OUT / closed Live Thread check

No item in R1–R21 is re-proposed, and T8/T9's disclaimers are restated,
not contested, matching the proposal's own accounting. The one thing
worth flagging explicitly: the off-axis point's construction reproduces
the *failure pattern* (not the letter) of two already-closed findings —
`beam_behind_t28`'s fixed lab-frame window (Iteration 77) and `back_frac`'s
fixed lab-frame box (Iteration 78, PHOTONICS' Phase-5 finding) — for a
secondary channel inside the cycle explicitly commissioned to retire that
pattern for the primary one. Not a re-tread of a settled claim, but the
same defect class recurring one level down, and worth naming as such
rather than letting "disclosed idealization" stand in for "checked to be
small."
