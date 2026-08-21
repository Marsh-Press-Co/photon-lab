# exp-054 Phase 2 Critique — PHOTONICS (blind, independent)

## Steel-man

The core physical separation is optically sound. For size parameter
x=2π·r_out/λ, with r_out=2.34 μm across this program's own 450/600/750 nm
sweep, x≈19.6–32.7 — well into the regime where the extinction paradox is
expected: Q_ext asymptotes toward 2 as diffraction adds an edge
contribution on top of the geometric shadow. So w_on (σ_ext·dx) genuinely
exceeding r_out is not numerically suspicious; it is the textbook
signature of a real body extinguishing more light than its ray-optics
silhouette. T9's finding that ratio_abs_ext=0.6075 exceeds the chord
model's ≤0.5 ceiling correctly disqualifies the ray-chord absorptance
*formula* there, not the measurement. And the structural move — leaving
P_abs on the measured, diffraction-inclusive w_on while routing
h_eff/mass/area through r_out, the one length a solid's conduction/
heat-capacity physics can actually see — respects a real distinction:
extinction can exceed geometric shadow; a conducting surface cannot
exceed the solid's own boundary.

## Sharpest attack

w_on is not a clean measurement of "how far diffraction extends the
object's optical footprint" — it is sigma_ext_cells run through the
iso_xsec_sq convention, which already encodes an arbitrary shape choice
(the module's own docstring: the object is "treated as compact... a
finite-rod-length convention would scale P_abs linearly instead"). That
convention was adopted to fix an AREA for a watts computation, not to
characterize a diffraction-broadened linear extent. The proposal reuses
the same number in a second, physically distinct role — as evidence w_on
is "diffraction-inflated past the real object" and therefore excludable
from h_eff/mass — without separating how much of w_on/r_out's ~3.0×
excess is genuine extinction-paradox diffraction (Q_ext=σ_ext/2r_out≈1.51,
plausible but never checked against a Mie/cylinder closed form) versus an
artifact of the square-vs-rod convention itself. No bound is offered on
that split, so "w_on is optical, not geometric" is asserted, not
established to the precision the mixed-chain margins (607×, ~8,900×)
lean on.

## Verdict

**support-with-changes**

## Parameter change that would flip to support

A desk closed-form Q_ext(x) check for an infinite dielectric/absorbing
cylinder at r_out, λ=600 nm (or an existing bench-native alternative
geometry probe), bounding how much of w_on's ~3.0× excess over r_out is
attributable to genuine diffraction versus the iso_xsec_sq shape
convention — run before the mixed chain is promoted to the sidecar's
default, headline path.
