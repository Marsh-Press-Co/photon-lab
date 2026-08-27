# PHASE 2 — CRITIQUE · QUANTUM OPTICS (blind) · Panel Iteration 57 · exp-080

*Fresh sub-agent, QUANTUM OPTICS charter (PANEL.md seat 5): non-classical
absorption, state-dependent or coherent interactions; expressibility
contract — mechanisms enter the bench only as effective classical
parameters or Red Team strikes them. I am blind to every other seat's
Phase-2 critique this cycle. My own prior seat's exp-079 Phase-5 review
(`phase5_review_quantum.md` §3) found the "structurally incapable at ANY
period" reading of exp-079's own headline is proven only for `r(θ)`
slowly-varying relative to the aperture window, via the reflectance-ablation
control (`y_wall_aperture_sum.py` §[7]/§[7b]). This cycle's charge: apply the
same ablation-style, from-primitives reasoning to EM's own claim that
PHOTONICS' not-yet-built plane-wave/global-steering construction is
"structurally different" and therefore untouched by this cycle's own part
(b) INCONCLUSIVE finding.*

**Nothing below re-proposes any RULED-OUT item (R1–R9).** Part (a)'s
FORECLOSE arithmetic and part (b)'s INCONCLUSIVE self-scoring are both
independently re-checked here (reproduced exactly, no discrepancy) — the
target of this critique is the proposal's own §5/Combined-reading
*recommendation*, not its arithmetic.

---

## 1. Steel-man (145 words)

EM's algebraic point holds: the scored object in part (b),
`E_approx(θ_beam) = r(theta_eff)·[per-point model]`, uses a scalar `r_const`
that is literally invariant across the ENTIRE θ_beam sweep — no R² number
this pre-check computed can mechanically exercise PHOTONICS'
`r(90°−θ_beam)`, which is a fresh complex number at every θ_beam, a genuine
new degree of freedom the static test cannot touch at all. Likewise, part
(a)'s FORECLOSE finding is specifically about `theta_local(y_s)`'s own
per-point spread across the aperture; PHOTONICS' construction never
evaluates `theta_local(y_s)` anywhere, so a stated violation of ITS OWN
validity criterion does not automatically transfer to a construction that
doesn't use that quantity. Treating (b) as a disclosed caveat rather than a
foreclosure, while proceeding to build — exactly Red Team's own §3/§7
sequencing for a FORECLOSE-leaning (a) result — is a defensible way to keep
the program moving without re-litigating anything already RULED OUT.

---

## 2. Sharpest attack (150 words)

PHOTONICS' `r(90°−θ_beam)` is, at every fixed θ_beam, still a single
y_s-independent scalar multiplying the same unweighted image sum `W(θ_beam)`
exp-079's own ablation already computed — pointwise-in-θ_beam, structurally
identical to exp-080's own "pull r out of the integral" operation, just
re-anchored at a θ_beam-varying angle. I computed
`E_photonics(θ_beam)=r(90°−θ_beam;ABSORB)·W(θ_beam)` directly (zero new
FDTD, gated primitives only) for all 5 configs against the same true
per-point curve. Raw R² is catastrophic (−8×10⁴ to −2×10⁷):
`|r(90°−θ_beam)|≈0.015–0.04` (48–54° from wall normal) is 100–400× larger
than `|r(theta_local(y_s))|≈1×10⁻⁴` (the true 5.3–15.0° range) — PHOTONICS'
angle samples a part of the wall's response the near-field geometry never
visits, the numeric consequence of part (a)'s FORECLOSE finding. Even after
a generous best-fit complex rescale isolating pure shape, mean R²(Re)=0.602,
min=0.085 (C70) — worse than this cycle's own 0.52 floor — and R²(abs) again
goes negative at the identical C70/C80 configs (−4.49, −7.71): the same
zero-crossing pathology recurs, unattenuated.

---

## 3. Derivation detail (supporting §2, zero new FDTD)

**Why this comparison is fair, not a category error.** `theta_local(y_s)`
is not a modeling choice — it is exact ray/image geometry
(`atan(D_SP/(OBJ_Y+y_s))`, measured from the y-wall's own normal, per
`y_wall_aperture_sum.py`'s own docstring). It is *the* incidence angle every
real aperture point's own image ray actually presents to this wall, at this
bench's actual dimensions. `90°−θ_beam` is the correct incidence angle (also
measured from the wall's own normal, by the x-wall's own established
convention EM's narrative borrows) **only if** the aperture radiates as a
single plane wave in the wall's far field. Part (a) already proved it does
not (`dist_image/d_F` = 0.76–2.15%, deep Fresnel zone). My derivation turns
that qualitative violation into a number: at THIS bench's geometry, the two
angle arguments (`theta_local(y_s)∈[5.3°,15.0°]` vs. `90°−θ_beam∈[48°,54°]`
for θ_beam∈[36°,42°]) are separated by ~35–40°, landing on completely
different parts of `boundary_reflectance.py`'s own admittance-profile
response — not a modest per-point-vs-global summarization gap, an
angle-regime mismatch.

**Method.** `W(θ_beam) = ∫ amp(y_s)·exp(i·[phase_drive(y_s,θ_beam) +
K600·dist_image(y_s)]) dy_s` is exactly exp-079's own §[7] `r_ablated≡1`
integral (re-derived here fresh, not copied). For each config I evaluated
`r(90°−θ_beam;ABSORB)` via `reflection_coefficient_vec` (unchanged) at every
one of the 31 real θ_beam grid points (36°–42°, from
`experiments/076-.../results.json::headline.theta`, the same grid
`validity_precheck.py` uses), multiplied pointwise onto `W(θ_beam)`, and
scored R² (both Re and `|·|` proxies, this sub-thread's own house
convention) against the SAME `y_wall_aperture_sum_results.json` true curve
`validity_precheck.py` already trusts (its own version-drift guard already
passed at 0.0 max diff). Every primitive
(`aperture_amplitude`/`dist_image_cells`/`source_driven_phase`/
`reflection_coefficient_vec`/`build_aperture_grid`/`K600`) is imported
unchanged from `y_wall_aperture_sum.py`, never reimplemented.

| cfg | ABSORB | raw R²(Re) | raw R²(abs) | scale-corrected R²(Re) | scale-corrected R²(abs) |
|---|---|---|---|---|---|
| C40 | 40 | −1.09×10⁵ | −3.54×10⁵ | 0.8836 | 0.4902 |
| C60 | 60 | −5.18×10⁶ | −2.35×10⁷ | 0.6985 | 0.2225 |
| C70 | 70 | −3.33×10⁵ | −2.36×10⁷ | 0.0852 | −4.4949 |
| C80 | 80 | −1.06×10⁶ | −1.90×10⁷ | 0.5072 | −7.7066 |
| G40 | 40 | −8.15×10⁴ | −3.91×10⁵ | 0.8356 | 0.6632 |

"Scale-corrected" fits one best-fit real scalar `α` (least squares) per
config onto `Re{curve}` (resp. `|curve|`) before scoring — the single most
generous correction available, isolating pure shape/zero-crossing agreement
from the raw amplitude-regime mismatch shown in the first two columns.
Scale-corrected mean R²(Re) = **0.602**, min = **0.085** (C70) — a *worse*
floor than exp-080's own static-`theta_eff` test (min 0.5214), and R²(abs)
repeats the exact sign flip to strongly negative at the exact same two
configs (C70, C80) exp-080's own test flagged, not a different pair.

**Two findings, not one, and they answer the two-part question directly:**

1. **The amplitude-regime mismatch is new, not previously stated anywhere
   in the record** (not in EM's proposal, not in PHOTONICS' own §4
   feasibility probe, which swept `arg(r(90−θ_beam))` for phase content but
   never checked `|r|` against the true `theta_local(y_s)` range at all).
   It may or may not matter to the eventual T28 metric — `score_period`
   fits a period, plausibly scale-invariant — but it does mean any
   downstream comparison of PHOTONICS' construction against this
   sub-thread's own per-point baseline must be shape-only, explicitly
   stated as such, never amplitude-based, a disclosure gap this critique
   closes for free.
2. **The shape-only (scale-corrected) result answers the charter question
   asked directly: yes, the same kind of pathology reappears, in a
   different guise.** Pulling a y_s-independent complex scalar out of the
   aperture integral — whether that scalar is fixed across θ_beam (exp-080's
   test) or re-evaluated fresh at each θ_beam (PHOTONICS' own construction)
   — distorts the resulting curve's zero-crossings/envelope enough to send
   the `|·|` proxy negative, and it does so at the SAME two configs
   (C70/C80) both times. That recurrence across two structurally different
   multiplier choices is evidence of something about THIS aperture's own
   phase/taper structure at ABSORB=70/80 specifically (not an artifact of
   which θ_eff or θ_beam-map was chosen) that any global-in-y_s treatment of
   `r(θ)` is liable to mishandle — a genuinely new, disclosed-nowhere risk
   flag for the PHOTONICS build, not a reason it cannot proceed.

---

## 4. Verdict: **support-with-changes**

The proposal's part (a)/(b) arithmetic is solid and correctly self-scored —
I find no defect there, and I do not oppose proceeding to PHOTONICS' own
build (Red Team's own §3/§7 sequencing already correctly treats a
FORECLOSE-leaning (a) result as "worth building regardless," and a REFUTE
outcome there would itself be a genuine, useful narrowing of the mechanism
board). What I oppose is the specific framing in the proposal's own
Combined-reading — "a structurally different object... this test cannot
rule it out" — being carried forward as an unquantified caveat rather than
a pre-registered, falsifiable check. §3 above shows that check is already
computable, for free, from already-gated code, and that it does not clear
even a generous bar.

**Required change:** before or immediately upon building PHOTONICS' own §4
construction, pre-register a SUPPORT/INCONCLUSIVE/REFUTE band — structured
exactly like this cycle's own part (b) — scored on the scale-corrected
R²(Re) of `r(90°−θ_beam;ABSORB)·W(θ_beam)` against this sub-thread's own
true per-point curve (mean ≥0.90 and min ≥0.75 for SUPPORT, mean <0.50 for
REFUTE, matching §4 of `phase1_proposal.md`'s own thresholds so the two
results are directly comparable). Report it alongside PHOTONICS' own
`arg(r)`-phase-swing feasibility probe, not instead of it. State explicitly,
before the build, whether the eventual scoring against T28's own period
family will use shape only (recommended, given §3's amplitude-regime
finding) or absolute amplitude.

## 5. Single parameter change that would flip this to plain "support"

If the scale-corrected R²(Re) numbers in §3's table had themselves cleared
mean ≥0.90 / min ≥0.75 — i.e., if PHOTONICS' own `r(90°−θ_beam)` construction
had, on this same zero-cost check, tracked the true per-point curve's shape
at least as well as this cycle's own static-`theta_eff` test claimed to
target — I would drop the "required change" above to a same-shift
disclosure sentence and support the recommendation as written. It did not
(0.602 mean, 0.085 floor, negative `|·|` R² recurring at C70/C80): the gap
between "untested" and "already tested, for free, and does not clear the
bar" is exactly what this critique closes.
