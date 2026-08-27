# PHASE 2 — CRITIQUE · MATERIALS & METAMATERIALS seat · Panel Iteration 55 (exp-078)

*Fresh sub-agent, blind to the other six seats' critiques this cycle. Charter
(PANEL.md, verbatim): "sub-wavelength structure; what could physically
realize the proposed optical behavior. Owns the realizability bound
(published / plausible / unobtainium-with-parameters)." Proposal under
review: `experiments/078-t28-y-wall-echo-prescreen/phase1_proposal.md`
(PHOTONICS, lead by rotation), a zero-FDTD closed-form period pre-screen of
a coherent echo off the domain's transverse (y-normal) wall.*

---

## Steel-man (≤150 words)

This pre-screen does real MATERIALS-adjacent diligence rather than gliding
past it. §3.4 doesn't just assert `r(theta;ABSORB)` transfers to the y-band —
it verifies `Sim._damping`'s ramp array in code (Sec[0]), comparing an actual
`Sim` instance's x-edge and y-edge `damp_e` columns and reporting worst
`|diff|=0.0` exactly; I reproduced this independently and it holds bit-for-
bit. Idealization 6 correctly re-states, unprompted, the exact unrealizable
matched-`eps=mu` admittance caveat this seat attached at exp-075/077 rather
than letting it quietly lapse just because the wall orientation changed — the
honest default is to assume a materials caveat resets at a new geometry, and
this document didn't take the shortcut of assuming inheritance for free. The
self-scored verdict (INCONCLUSIVE, not SUPPORT, on `R²=0.13–0.15` fits)
also resists overselling 2-of-3 period matches, unlike earlier T28 cycles
this program had to walk back after the fact.

## Sharpest attack (≤150 words)

§3.4's verified claim only shows the *depth profile* `n(x)` is orientation-
invariant — it never checks the angle argument fed into
`br.reflection_coefficient`, whose own docstring defines `theta_deg` as
measured **from the interface's own normal**. For the x-wall that equals the
sweep `theta`; for a y-wall it is `90−theta` (propagation direction
`(−cosθ,+sinθ)` makes `cos(angle-from-ŷ)=sinθ` exact). `edge_image_phase_
difference` passes the raw, unconverted sweep `theta` into that function at
every call. I recomputed both ways: at `θ=36°/39°/42°`, `|r|` swings by
`13.3×/5.8×/2.5×` and `arg(r)` shifts `130–230°` between the as-used and
angle-corrected evaluations — a different reflectance regime, not a small
idealization. Before MATERIALS can bound what structure realizes
`r(theta;ABSORB)` "for a y-oriented wall," the model must first compute that
quantity at the wall's *actual* angle of incidence. As shipped, every number
in §5.2/§5.3 — both nominal SUPPORT verdicts included — is the x-wall's
admittance evaluated at the wrong angle for a y-wall.

## Verdict: **support-with-changes**

Two separable materials-adjacent claims are bundled in Idealization 6 and
§3.4, and only one survives my check. (1) "The y-band's per-cell damping
profile is identical to the x-band's" — **confirmed**, independently
re-verified from `lab/fdtd2d.py::Sim.__init__` directly, not merely from the
document's own printed `worst_abs_diff=0.0`. (2) "Therefore `r(theta;ABSORB)`
applies unchanged" — **not established**, because reusing the function
requires reusing its angle convention too, and that convention is
wall-orientation-specific in a way this document never addresses. This isn't
a second-order idealization on top of an already-disclosed unrealizable
admittance (Idealization 6's own point); it is upstream of realizability
entirely — a MATERIALS bound only attaches to a correctly-computed target
transfer function, and I cannot yet certify that `r(theta;ABSORB)` as used
here is that function for a y-wall.

Separately, worth stating plainly since the proposal asks MATERIALS to weigh
in on realizability directly: even a *correctly angle-computed* `r(theta)`
here would describe the reflectance of the domain's own PEC-backed graded-
loss edge termination (`boundary_reflectance.py`'s own docstring: "backed by
the PEC-like hard wall," i.e., the FDTD engine's open-boundary substitute) —
not a coating anyone would place in the witness scene. If the mechanism
survives future Test-B scoring, the realizability question worth asking is
not "can a metamaterial realize this specific admittance" but "does this
mechanism even correspond to anything beyond an artifact of how this solver
truncates open space" — a T1-N/A, instrument-fidelity framing the proposal
already uses correctly for its own scope, but one this seat flags explicitly
so a future SUPPORT is never read as materials progress toward a buildable
device, the same over-read this seat guarded against at exp-077 §5.

## Parameter/scope change that would flip verdict to support

Re-run Sec [4]/[4c] of `y_wall_prescreen.py` calling
`br.reflection_coefficient(n_prof, 90.0 - theta_deg, lam_cells)` for the
y-band evaluation (equivalently: swap the `sin²θ`/`cos²θ` roles inside
`reflection_coefficient` when it is invoked for a y-normal interface), then
re-score §5.3's three comparisons against the corrected curve. If the
corrected `rel_dev`/R² values still clear the same bands this document
reports (or even if they don't — a clean REFUTE is equally usable), that
closes the one gap separating this from a fully soundly-derived pre-screen.
No new FDTD is required either way.
