# PHASE 2 — CRITIQUE · MATERIALS & METAMATERIALS seat · Panel Iteration 52 (exp-075)

*Fresh sub-agent, blind to the other five seats' critiques this cycle. Charter
(PANEL.md, verbatim): "sub-wavelength structure; what could physically realize
the proposed optical behavior. Owns the realizability bound (published /
plausible / unobtainium-with-parameters)."*

---

## Steel-man (<=150 words)

The friction-PDE bridge is not an arbitrary choice among several — it is
**forced** by what `lab/fdtd2d.py::Sim.run` actually does: `self.Ez *=
damp_e`, `self.Hx *= damp_hx`, `self.Hy *= damp_hy` all draw on the identical
`_damping` ramp for the same `x`. Any local (eps(x),mu(x)) medium reproducing
E and H decaying at the same rate at the same point must have matched
intrinsic impedance, and the derivation gets there by an unambiguous
requirement (passivity, `|r|<=1`), not a fit to the target data — the wrong
branch is shown failing by orders of magnitude, not merely disfavored. The
"exact, not small-loss" claim for `n=1-i*nu/omega` is a genuine, checked
algebraic identity, not an overclaim. Three assert-gated sanity checks (worst
deviations `2e-16`/`1e-15`) precede any trusted number, and I reproduced
every cited figure (`P_model=15.0000°`, `r^2=0.2586`, REFUTE) by re-running
`boundary_reflectance.py` myself — none is hand-typed.

## Sharpest attack (<=150 words)

The derived `Z(x,theta)=n(x)/sqrt(n(x)^2-sin^2(theta))` is not a neutral
"effective index" — it is the admittance of a **matched eps=mu medium**
(mu(x)=n(x) exactly), forced by the code's symmetric E/H decay. That is a
genuine physical class, but not this bench's own `graded_black_shell`'s
class, and not any realizable *optical*-frequency material's class: matched
magnetodielectric grading (broadband mu tracking a complex, lossy eps over a
mere 2-4lambda span) is microwave-RAM technology (ferrite/graphite-loaded
tiles), UNOBTANIUM-WITH-PARAMETERS at 450-750nm — no metamaterial platform
gives mu(x) any appreciable value there, let alone one tracking eps(x)
exactly. An ordinary realizable absorber (mu=1, sigma_e-graded, like this
bench's OWN physical absorber) has `Z(x)=1/sqrt(n(x)^2-s^2)` instead —
admittance-mismatched at every interior grading step, not just the wall —
producing a richer interior-reflection structure this single-echo model
cannot see. Nothing in the idealizations list (1-9) names this: the REFUTE is
earned for the numerical artifact studied, but does not license the further,
unstated inference that boundary-reflectance-type mechanisms are closed off
for any physically realizable equivalent-loss coating — only for this one,
matched-medium, single-echo instance of the idea.

## Verdict: **support-with-changes**

The R4 reproduction is clean, the passivity-adjudicated sign resolution is
the correct physics move, and the REFUTE conclusion for the specific
mechanism tested (single coherent echo off the `-x` wall through THIS
numerical band's own matched-medium admittance) is properly earned by its
own pre-registered bands — not overclaimed as written. My objection is a
missing idealization, not a computational or logical defect: the write-up
should add, explicitly, that the derived `n(x)/Z(x)` corresponds to a
matched-eps=mu medium class that is itself UNOBTANIUM-WITH-PARAMETERS at
these wavelengths, and should scope the REFUTE to "this matched-medium,
single-echo construct," not to boundary-reflectance-from-any-realizable-
absorber as a class — so a future LOGBOOK citation of this REFUTE cannot be
read more broadly than the physics actually supports.

**On idealizations 5/6, from a structure/realizability standpoint:**
Idealization 6 (single echo, no cavity) is the well-justified one —
`|r|<=0.0064` throughout §2d means a second bounce is suppressed by another
factor of `|r|`, ~4e-5 second-order, genuinely negligible; treating the
band+wall as a single coherent reflector is quantitatively, not just
qualitatively, defensible. Idealization 5 (skipping the `+x` band behind the
source) is the weaker cut: that band is driven by the identical
`self.absorb`-parameterized ramp (same matched-medium admittance class, same
machinery already built here) at a different, also-fixed standoff
(`clear_src=20`), so computing its echo would have been essentially free
with the code already written — an avoidable simplification, not a deep one,
even though correctly disclosed as future work rather than hidden.

## Parameter/derivation change that would flip verdict to support

Add one explicit idealization stating the matched-eps=mu realizability
status of the derived `Z(x)` (PUBLISHED/PLAUSIBLE only as microwave RAM,
UNOBTANIUM-WITH-PARAMETERS at optical lambda) and narrow the REFUTE's stated
scope accordingly in §5's "Reading" paragraph — no recomputation needed, the
numbers and verdict do not change.
