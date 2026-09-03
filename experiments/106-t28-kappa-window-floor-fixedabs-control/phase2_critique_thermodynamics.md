# PHASE 2 — CRITIQUE · THERMODYNAMICS · Panel Iteration 83

*Reviewing candidate exp-106, "Floor-Gating, Settling, Risk-Propagation,
and the Fixed-Absolute-Thickness Control for `kappa_window`" (Lead:
QUANTUM OPTICS). Blind to all other seats' current-cycle critiques.*

## Steel-man (≤150 words)

§5's narrow claim is literally correct under this program's own thermal-
sidecar convention: `mixed_length_scale_regime`'s `l_geometric_m` derives
from `sigma_ext` under the standing Q_ext=1 placeholder
(`width_m = sigma_ext_cells * dx_m`, T9's convention, `lab/
thermo_sidecar.py`), which is a function of `r_out` alone — and `r_out`
is held bit-identical between families at every r in this proposal (§2b:
"Domain construction... is identical to §2a at the same r — only the
object's material law differs"). Since `R_CORE`/`sigma_max` never enter
`l_geometric_m`'s own formula, the sidecar's existing machinery genuinely
has nothing new to compute this cycle without a fresh `sigma_ext`
measurement neither family requests. Correctly scoped: this is an
instrumentation cycle, not a re-invocation of P5, and no falsifiable
thermal claim is silently smuggled in via the fixed-abs control.

## Sharpest attack (≤150 words)

§5's claim is too broad for what it's asked to carry. `l_geometric_m`
unchanged is true; "nothing about the thermal chain changes" is not the
same statement, and the gap matters here specifically. Both families hold
`tau_shell = sigma_max*thickness = 24.0` exactly (design_geometry.py's own
printed assertions), so normal-incidence transmittance is identical
(~e⁻²⁴) in both — but `kappa_window`'s entire measured signal, by
construction, is NOT that dead channel; it's edge/near-field diffraction
around the shell, governed by the *gradient steepness* fixed tau_shell
discards: fixed-abs holds sigma_max=0.5 (steep, abrupt) at every r while
self-similar falls to 0.25/0.125 (gradual, longer path) at r=156/312 —
exactly the confound item 4 is designed to probe. A steeper-gradient shell
Fresnel-mismatches more at its boundary; a gradual one absorbs more
adiabatically. That means `p_abs` (and its complement, diffracted-into-
window power) can genuinely differ between families at fixed r_out — the
very quantity the Q_ext=1/`sigma_ext∝r_out` placeholder assumes is
gradient-independent. §5 asserts this assumption's one output
(`l_geometric_m`) is safe without checking the assumption itself is safe
for *this* comparison, where the gradient is the whole point.

## Verdict

**Support-with-changes.**

Item 4's own falsifiable bands (§4, `shape_ratio_fixedabs ≤8.0` vs
`≥14.8`) are framed as discriminating "growing electrical thickness" from
"pure geometric z/z_R diffraction." But a third possibility sits between
those two and is currently unchecked: differential `p_abs` between the two
absorption-gradient profiles at identical `r_out`, which would move
`kappa_window` for reasons that are neither pure z/z_R geometry nor
merely "thickness in wavelengths" but the coating's *edge steepness*
specifically. `sections.radial_absorbed_power` (exp-028, already the named
instrument in exp-052's own Accepted Fix 3, "core-fill check using the SAME
validated instrument" precedent) can bin Joule dissipation `0.5*sigma_e*
|Ez|^2` from the article-scene fields already being captured for
`kappa_window` at r=156/312 in both families — this is a desk-cheap,
zero-new-`Sim.run()`-call addition (same captures, an extra reduction
pass), not a re-invocation of the thermal sidecar's ΔT/NETD chain. Without
it, a `shape_ratio_fixedabs` landing inside either pre-registered band
gets attributed entirely to the wrong one of two live mechanisms if the
gradient-steepness effect on `p_abs` is non-negligible. This does not
require re-architecting the cycle or adding FDTD calls — it is a checked
sanity pass on data already scheduled to exist, not a new sidecar
invocation, so it does not contradict §5's own "P5 not re-invoked" scope
statement; it closes a gap in a *different* claim (§5's generalization,
not P5 itself).

## Single parameter change that would flip this verdict

Add one line to §2c/§2e: for each of the four new (r, family) captures at
r=156/312, run `sections.radial_absorbed_power(cap_article, sigma_e, cx,
cy, r_max=R_COAT)` on the fields already captured for the window
floor-gate, and report the four `p_abs`/`i_inc` ratios alongside
`shape_ratio_fixedabs`. If fixed-abs and self-similar's `p_abs` fractions
land within, say, 10% of each other at matched r, the gradient-steepness
confound is empirically closed and I would move to **support**; if they
diverge materially, item 4's interpretation needs the three-way framing
this critique asks for, not the two-way one currently written.
