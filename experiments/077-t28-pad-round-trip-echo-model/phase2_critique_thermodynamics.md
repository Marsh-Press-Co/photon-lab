# THERMODYNAMICS — Phase 2 Critique · Panel Iteration 54 · exp-077 (T28 PAD round-trip echo refit)

*Fresh sub-agent, THERMODYNAMICS charter (PANEL.md, verbatim): "where absorbed
energy goes. Always asks what re-radiates and whether it would be detectable.
Owns the per-proposal energy sidecar: absorbed power -> temperature rise ->
emission band -> detectability. Expressibility contract: the sidecar is a
post-run analytic calculation, not an FDTD output, and is labeled as such."
Blind to all other Phase-2 critiques this cycle. Verified independently by
re-running `pad_round_trip_model.py` and re-deriving `r(theta;ABSORB)` from
`boundary_reflectance.py`'s own `reflection_coefficient`/`n_profile_exact` —
not merely trusting the proposal's printed table.*

---

## Steel-man (≤150 words)

The N/A conclusion for `PAIR_PAD` is defensible on a fact the proposal has
but doesn't cite: `pad_round_trip_model.py` line 176,
`r_for = {"C40": r40, "G40": r40, "C80": r80}`, reuses the exact same
`r(theta;ABSORB=40)` array object — bit-identical, not merely numerically
close — for both `C40`'s and `G40`'s predicted echo term. The absorbed-power
fraction at that boundary, `1-|r(θ;40)|²` (I compute 99.99788%–99.99959%
across 36°–42°), is therefore a shared multiplicative scale factor common to
*both* terms of the `PAIR_PAD` difference. A quantity that enters identically
on both sides of a subtraction cannot, by construction, drive the shape or
period of the *difference* Tests A/B score — only its overall amplitude,
consistent with the disclosed 2.4× amplitude under-prediction. So the REFUTE
verdict is untouched by anything absorbed power could do — a real, stronger
argument than the one actually given.

## Sharpest attack (≤150 words)

§3's stated reason — "PAD cells are proven lossless vacuum" — answers a
question nobody asked and doesn't cover the case it's applied to. Nothing
claims PAD absorbs; absorption happens at the ABSORB band, which is not
lossless: `1-|r(θ;40)|²`=99.9979%–99.9996% (36°–42°, matching §2e's
|r|=0.0029–0.0064 exactly); at ABSORB=80, 99.999997%–99.9999999%. Every
reflection event either config computes IS an absorbed-power effect — it's
common-mode for `PAIR_PAD` only because line 176 reuses the same `r40` array,
not because PAD is lossless. exp-075's own §3 already gave the correct
reasoning ("has nowhere to re-radiate into this measurement") and this cycle
drops it unacknowledged. Worse: `PAIR_ABSORB40`'s two terms use *different*
r (r40 vs r80) — a genuine, non-common-mode absorbed-power differential
(Δ=8.4e-6 to 4.1e-5 across the sweep, computed directly) that the blanket
N/A never names or bounds. It's almost certainly negligible, but "almost
certainly" from an un-run calculation is not this seat's standard.

## Verdict

**support-with-changes.**

Neither the Combined Verdict for `PAIR_PAD` (REFUTE) nor `PAIR_ABSORB40`
(INCONCLUSIVE) is affected — Tests A/B are computed from the model's complex
`c_empty_with_wall` output directly and do not route through my critique.
This is a sidecar-correctness finding, not a results finding, but it sits
squarely in this seat's charter and the charter's own expressibility contract
requires the sidecar to be an actual analytic calculation, not an asserted
disposition — which is what §3 currently is.

Mandatory fix before this cycle closes: replace §3's justification with (a)
the correct PAIR_PAD reasoning — the absorbed-power fraction is common-mode
because `r40` is the literal same array object in both terms, computed and
quantified (99.9979%–99.9996%), not because PAD is lossless; and (b) an
explicit, computed disposition for `PAIR_ABSORB40`, where ABSORB genuinely
differs between terms: state the Δabsorbed-fraction (8.4e-6–4.1e-5) and argue
its thermodynamic insignificance quantitatively (it perturbs a boundary
already absorbing ≥99.998% of incident power by at most ~4×10⁻⁵ in relative
terms — no plausible temperature-rise/emission-band chain reaches
detectability at that scale) rather than importing PAIR_PAD's PAD-lossless
argument by silent extension to a pair it doesn't apply to.

## Single change that would flip my verdict to support

None needed to flip to oppose — this is a documentation/reasoning-quality
gap in the required sidecar, not a defect in the computed numbers or bands.
It would flip to **support** outright if §3 were rewritten as above with the
two disposition arguments (common-mode-scale-factor for PAIR_PAD;
quantified-and-bounded-negligible differential for PAIR_ABSORB40) before
Phase 3 freeze — a same-shift text fix, zero new computation, zero `lab/`
diff, zero change to any frozen prediction or verdict.

---

## Independent verification notes (for the record)

- Re-ran `python3 experiments/077-t28-pad-round-trip-echo-model/pad_round_trip_model.py`
  from repo root: output is bit-for-bit consistent with the proposal's
  tables (Test A `rel_dev`=1.8798/0.9642, Test B `r²`=0.0444/0.1997,
  Combined REFUTE/INCONCLUSIVE).
- Re-derived `r(theta;40)` and `r(theta;80)` independently from
  `boundary_reflectance.py`'s primitives across the full 31-point grid (not
  just the three §2e sample angles) and computed `1-|r|²` at every point;
  values above are from that independent recomputation, not copied from the
  proposal.
- Confirmed `lab/fdtd2d.py::_damping` (lines 122-129): the damping ramp is
  `(np.arange(self.absorb,0,-1)/self.absorb)**3`, a pure function of
  `self.absorb` and array shape, with no `pad`/`nx`/`ny`-dependent term —
  `PAD` genuinely cannot appear in the damping construction, confirming the
  proposal's own §2b claim independently. This part of the proposal's
  reasoning is solid; my attack is confined to §3's use of it.
- Confirmed `pad_round_trip_model.py` line 176 (`r_for = {"C40": r40, "G40":
  r40, "C80": r80}`): `r40` is the same Python object passed for both `C40`
  and `G40`, not independently recomputed/re-fetched — the common-mode
  claim in my steel-man is a code-level identity, not an approximation.
