# exp-065 — Phase 2 Critique: ELECTROMAGNETISM (blind)

**Seat charter applied:** field/wave behavior, impedance matching, energy
coupling; reciprocity/passivity/causality bookkeeping; formalizing what T1
permits and forbids. This is an instrument/model-fidelity cycle (N/A on T1,
correctly stated) — the charter work here is auditing whether the
congruence argument (§2.2), the causal-identity gate (P-VIS42-1b/G-2), and
the "no new machinery" passivity standard (§8.2) actually hold up as
*formal* EM claims, not just as procedurally-satisfied checkboxes.

---

## Steel-man (≤150 words)

The congruent-series construction is genuinely sound single-variable
bookkeeping. By padding and shifting every scene coordinate together, the
proposal holds `A`, both clearances, `D_SP`, `LEVER`, and the aperture span
bit-for-bit constant across `ABSORB ∈ {40,60,80}` (verified independently
by re-running `design_geometry.py`: output matches the committed file
exactly) — so the *only* physical quantity varied across C40/C60/C80 is
the band's own thickness and damping profile, exactly the isolation T24
was designed for and the naive N60 protocol destroys. Exhibiting the desk
propagator's exact `0.000e+00` degeneracy on that congruent series is the
correct zero-cost way to prove, before any FDTD spend, that a nondegenerate
model which structurally cannot see domain boundaries at all still predicts
identical readings across the series — a real, useful independent
cross-check on the geometry table, not decoration.

## Sharpest attack (≤150 words)

P-VIS42-1b's causal-identity step, `n = 359`, is derived by dividing the
round-trip distance (263 cells, `2·clear_src + D_SP`) by the wave's
Courant-limited phase speed `S ≈ 0.700036` cells/step. But the actual
FDTD update (`Sim.run`, traced directly) is a 5-point cross stencil —
`Ez(new,i,j)` depends only on `Ez(old,i±1,j)`, `Ez(old,i,j±1)` — whose
**true numerical domain of dependence grows by exactly 1 cell/step**,
strictly faster than `S`. The rigorously "guaranteed by causality alone"
step is `263 − 16 = 247`, not 359 — a 112-step, 45% overstatement of the
safe window an *absolute* (`Δ=0.0` exact) gate is staked on. Whether the
gate still passes at 359 in practice depends on whether the true
numerical precursor beyond the group-velocity front has underflowed to
exact float64 zero by then — an empirical fact the proposal never checks,
because it never derives the stencil's own propagation speed. `S` bounds
the *physical* wavefront; it does not bound the *stencil's* light cone.

---

## Discussion (supporting the two items above, not a third headline)

**On the causality gap, precisely.** `_damping`'s exponential factor is
purely multiplicative (`Ez *= damp_e`) and never couples neighboring
cells, so it cannot itself widen the stencil's domain of dependence —
the 1-cell/step bound is exact for the full leapfrog H-then-E update,
independent of `absorb`. Using it instead of `S` in
`causal_identity_step` (same 16-step guard, same 263-cell path) gives
`n=247`. This is not a claim the gate *fails* at 359 — the true
numerical precursor for a smoothly-ramped source (`env(0)=0` exactly,
raised-cosine growth) decays extremely fast per cell beyond the
group-velocity front and very plausibly underflows before step 359. It
is a claim that the proposal's own stated justification — "guaranteed
IDENTICAL by causality alone" — is not the rigorous bound it is
presented as, for a gate the whole cycle is built to halt on if it fails.
A gate whose PASS is only explicable by float64 underflow rather than by
the argument advanced for it is not the "absolute standard" §8.2 claims
it is.

**On §8.2's "zero `lab/` diff ⇒ no new machinery" standard.** From a
strict passivity standpoint the position is actually defensible: `damp_e
= exp(−0.30·d)` with `d ≥ 0` is manifestly dissipative-only for *any*
`absorb`, so no new passivity risk is created by varying it — energy can
only leave the domain faster or slower, never be added. But passivity was
never the open question; **boundary FIDELITY** (reflection/absorption
accuracy as a function of `absorb`) is, and the proposal's own §8.2 text
concedes no suite stage has ever pinned `absorb` as a controlled
variable. G-1 and G-2 are real gates, but neither one — by design —
touches the region *after* the wave reaches the band: G-1 is a
pre-existing-value regression at `absorb=40` only, G-2 certifies only
the pre-boundary-interaction vacuum extension (and inherits the gap
above). Characterizing `ABSORB=60/80`'s own reflection behavior is
exactly what Block SWEEP is *for* — which is fine, but means §8.2's
"absolute-identity gates discharge the honest counter-argument" framing
overstates what G-1/G-2 can certify; they authorize running the
experiment, they do not pre-validate its answer.

**On the desk propagator's blind spot (§2.4).** `edge_diffraction_c_
empty_corrected` is a free-space Huygens–Fresnel sum over `_src_amp`
(taper × phase ramp) with no domain-edge term at all — it cannot see
reflection physics by construction, which is the intended property. But
it equally cannot see **near-field reactive loading of the source by a
nearby lossy band**: `clear_src = 20` cells (≈0.8–1.3λ at this bench's
CPL) is close enough that the graded band could plausibly perturb the
source's own effective near-field impedance before any far-field
propagation the model captures. This mechanism, if real, would NOT
appear as boundary physics in T24's sense but would still move
`C_empty`. Encouragingly, this is close to self-policed: `clear_src` is
held at 20 across the whole C40/C60/C80 congruent series (only G40
changes it, to 60), so P-VIS42-5's pad-only null is already the correct
targeted test for it — but a REFUTE there would be evidence for exactly
this mechanism, not merely "sensitivity to padding," and NOTES.md should
say so if it fires rather than leaving it as an unnamed "second
systematic."

---

## Verdict: **support-with-changes**

The single-variable congruence design is EM-sound and the right way to
isolate `absorb` from T21's fringe geometry. What should not survive
unchanged into Phase 3: the causal-identity gate's derivation, and the
§8.2 framing that G-1/G-2 fully discharge the "new configuration class"
concern rather than partially relocating it into Block SWEEP's own
results.

**Single parameter change that would flip this to unconditional
support:** re-derive `causal_identity_step` using the stencil's true
propagation speed (1 cell/step per axis, not `S`) rather than the wave's
Courant-limited phase speed — a one-line change, zero FDTD cost, giving
`n≈247` in place of 359 — and re-run G-2 at the corrected step. If it
still passes at `n=247` (a strictly harder bound to clear), the
padded-domain congruence claim is actually airtight rather than merely
consistent with underflow.
