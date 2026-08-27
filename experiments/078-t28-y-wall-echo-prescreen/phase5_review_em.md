# PHASE 5 — REVIEW (ELECTROMAGNETISM, blind) · Panel Iteration 55 · exp-078

*Fresh sub-agent, ELECTROMAGNETISM charter: field/wave behavior, impedance
matching, energy coupling; owns reciprocity/passivity/causality bookkeeping —
formalizes what T1 permits and forbids. Blind to all other seats' Phase-5
reviews, including my own Phase-2 critique of this same cycle (re-derived
independently here, not carried forward by assumption). Grounded on
PANEL.md, AGENTS.md, LOGBOOK.md in full (RULED OUT R1–R9, T28's complete
Iteration 46–54 history), and the complete exp-078 record
(`phase1_proposal.md` as corrected in place, `y_wall_prescreen.py` — read in
full, not skimmed — `y_wall_prescreen_results.json`, all five Phase-2
critiques, `phase2_redteam_audit.md`, `phase2_redteam_angle_correction_
check.py`, `phase3_synthesis.md`, `phase4_results.md`,
`phase4_null_calibration_corrected.py`/`_results.json`), plus
`experiments/075-.../boundary_reflectance.py` and
`experiments/065-.../design_geometry.py` for background. Independent
computation this review: a standalone script re-deriving the geometric
(image-to-observer) incidence angle for the y-wall reflection directly from
`dg065.CONFIGS`, evaluating `br.reflection_coefficient` at it, and comparing
against both angle conventions already on the record — new to this cycle,
not present in any Phase-2 critique or the Red Team audit.*

---

## 1. Verdict: **PARTIAL** — the corrected pre-screen is honest and its
INCONCLUSIVE reading is defensible, but a fresh EM finding this review
contributes narrows the sub-thread further than the committed record shows

The angle-convention correction (Phase 2 → Red Team → Phase 3 → Phase 4) is
real, load-bearing, and correctly executed: I independently re-ran
`y_wall_prescreen.py` end to end and reproduce every number in
`phase4_results.md` exactly (`C80−C40` `rel_dev=0.4074` at the search
boundary; `PAIR_ABSORB40` `rel_dev=0.3284`; `PAIR_PAD` `rel_dev=0.3021`; all
three gates at 48°–54° clean, worst `|r|=0.038583`). Nothing about that
correction is in question. **But this review finds a second, deeper, and
independently new defect in the same reused primitive** (§2 below): the
"corrected" angle (`90−θ_beam`, 48°–54°) is itself not the physically
appropriate incidence angle for the specific point-source/image reduction
`edge_image_phase_difference` implements. A rigorous, internally-consistent
derivation — using the model's own Euclidean image/direct distances, which
already encode the actual reflection geometry — gives a **fixed, per-config
angle of 13.7°–15.0° from the y-wall's normal that does not depend on the
swept `θ_beam` at all.** Plugging that angle into the identical, already-
gated `reflection_coefficient` produces a **constant** `r` per config across
the entire 36°–42° window, which collapses `Delta_phi_self(θ)`'s only
θ-dependent term to zero. Under this reading, the primary model predicts
**no oscillatory signal whatsoever** — not a wrong-period match, an
identically flat curve. This does not change the document's own self-scored
bottom line (INCONCLUSIVE, no comparison reaches SUPPORT or REFUTE) because
the pre-screen was never entitled to a stronger verdict from a period-only
instrument in the first place — but it means the honest floor under this
sub-thread is lower than "0/3 SUPPORT, statistically indistinguishable from
noise" suggests: the specific reduction this file builds, done at the angle
its own physics actually calls for, has **no mechanism left to produce any
period at all**, principled or coincidental.

---

## 2. Independent re-derivation: which angle does `edge_image_phase_
difference` actually owe `reflection_coefficient`, and is `90−θ_beam`
correct?

### 2a. The docstring's phase-preservation claim, checked directly

`edge_image_phase_difference`'s own comment states: "an image source
preserves the real source's own driven phase exactly, up to `r`'s own
complex factor... it does not re-derive a new 'steered' phase from its
mirrored position." Taken as a statement about *what an image-source
construction means* — reflected field at the observer = `r(θ_local) ×`
(the field the source's own image would produce at the observer, absent the
wall) — this is standard, correct linear-boundary image theory for **any**
passive, non-gyrotropic, PEC-backed reflector, lossy or lossless; nothing
about loss or the PEC backing changes it, and no separate reciprocity
argument is needed to state it (reciprocity would matter if the construction
swapped source and observer roles, which it does not). `phase2_critique_em.
md` (my own Phase-2 pass, re-derived here rather than merely re-cited)
already reached this same conclusion; I re-confirm it, unchanged. **The
defect is not in the preservation claim — it is in which angle `θ_local`
gets fed into `r`.**

### 2b. Is `θ_local = 90−θ_beam` (the Phase-2/Red-Team fix) the geometrically
correct choice? Independently re-derived: no — and the reason is visible in
the model's own committed numbers.

`Delta_phi_self` uses two Euclidean (`np.hypot`) distances — `dist_real =
hypot(D_SP, A)` and `dist_image = hypot(D_SP, OBJ_Y+y_lo)` — to build the
propagation-phase term `k·(dist_image−dist_real)`. This is the *same*
Green's-function convention `dg048.field_and_h` uses for the established,
already-gated x-wall/edge-diffraction propagator (`G0 = exp(i(k·r−π/4))/
√r`, `r = hypot(d_sp, Δy)` exactly — confirmed by reading
`experiments/048-.../design_geometry.py::_geom_derived`, line 189, the same
`r_edge = hypot(d_sp, a)` construction this file's `dist_real` reproduces).
That convention treats the edge as an **isotropic 2D point radiator**: a
scalar complex amplitude (taper × driven phase) sitting at one location,
propagating via a Green's function whose phase depends only on Euclidean
distance, with **no angular directivity of its own** — a point source has
no "steered" radiation direction; only an *aperture* (a coherent sum over
many such points) produces one. `add_line_source`'s own docstring confirms
this split explicitly: "`angle_deg`: launch angle from the x-axis (a phase
ramp `k·sinθ` along the line). The `−x`-going wave then travels along
`(−cosθ,+sinθ)`" — a statement about the **coherent sum's** emergent
wavefront direction, which is exactly why it licenses the x-wall's
whole-aperture plane-wave image argument (§3.1, validated bit-exact) but has
no logical claim on a **single, isolated** point's own reflection geometry
once the edge-dominance idealization has already discarded the rest of the
aperture.

For an isotropic point source reflecting off a planar admittance boundary,
the rigorous treatment is a Sommerfeld/Weyl angular-spectrum integral; its
leading (stationary-phase) term — valid here by a wide margin, `k·r ≈
(2π/20)·800 ≈ 251 ≫ 1` — reduces to exactly the geometric-optics/Fermat
result: **the local incidence angle is set by the straight line from the
image position to the observer**, i.e. by the very same `dist_image`
geometry already computed. I recomputed this angle directly from
`dg065.CONFIGS` for all five configs (script: this session's scratchpad,
reusing only `br.reflection_coefficient`/`dg065.CONFIGS`, no reimplementation
of either):

| cfg | `d_sp` | `OBJ_Y+y_lo` | geometric bounce angle (from ŷ) | `θ_beam` (as-filed) | `90−θ_beam` (corrected) |
|---|---|---|---|---|---|
| C40 | 223 | 832 | **15.004°** | 36–42° | 48–54° |
| C60 | 223 | 872 | **14.345°** | 36–42° | 48–54° |
| C70 | 223 | 892 | **14.036°** | 36–42° | 48–54° |
| C80 | 223 | 912 | **13.740°** | 36–42° | 48–54° |
| G40 | 223 | 912 | **13.740°** | 36–42° | 48–54° |

This angle is a **per-config constant** — it has zero dependence on `θ_beam`
by construction, since `dist_image`/`dist_real` never contain a `θ_beam`
term anywhere in the file (already established, §3.3 of the proposal, for
the unrelated purpose of showing `fixed_offset` contributes no oscillation —
the same fact independently forecloses `θ_local` from oscillating too, once
`θ_local` is derived from the same distances rather than borrowed from the
aperture's steering convention). Evaluating `r(θ_local;ABSORB)` at this
fixed angle (verified directly against the same, already-gated
`reflection_coefficient`):

| cfg | `\|r\|` at `θ_beam=39°` | `\|r\|` at `90−θ_beam=51°` | `\|r\|` at geometric `θ_local` | `arg(r)` at `θ_local` |
|---|---|---|---|---|
| C40 | 0.004269 | 0.024900 | 0.000106 | +150.07° |
| C60 | 0.000294 | 0.004173 | 0.000004 | −171.86° |
| C70 | 0.000114 | 0.002022 | 0.000004 | −159.79° |
| C80 | 0.000068 | 0.000777 | 0.000002 | −161.81° |
| G40 | 0.004269 | 0.024900 | 0.000093 | +157.96° |

Because `θ_local` does not sweep with `θ_beam` under this reading, `r(θ_local)`
— and therefore `arg(r)`, already established by Red Team's Attack 1 as
`Delta_phi_self`'s **sole** source of θ-dependence — is a **flat constant**
across the entire 36°–42° window for every config. `Delta_phi_self(θ)`
collapses to a config-dependent constant; `cos(Delta_phi_self(θ))` is a
constant curve; every `PAIR_*`/`C80−C40` difference of two constants is
identically zero. **The primary model, evaluated at the angle its own
Euclidean-distance construction actually implies, predicts no periodic
signal at all — a cleaner, more decisive null than "period doesn't match,"
though not a formal Test-A REFUTE in this sub-thread's own established sense
(a flat curve has no well-defined period to score against the `rel_dev`
band at all, the same structural situation `model_period_runs_to_boundary`
already flags for `C80−C40` under the corrected-but-swept angle).**

### 2c. Why this was not caught at Phase 2

All three critics who found the angle defect (EM, MATERIALS, THERMODYNAMICS)
— myself included, in my own Phase-2 pass — worked entirely within the
"which fixed convention, `θ_beam` or `90−θ_beam`" framing inherited from the
x-wall's validated plane-wave derivation, because that framing is what the
proposal itself offered as the two live candidates (§5b's own audit-trail
structure). None asked whether *either* convention is licensed once the
model has already switched from a whole-aperture plane-wave picture (§3.1,
where a swept steering angle is exactly right) to a single-point Green's-
function picture (§3.2's own edge-dominance reduction, where it is not).
This is a genuinely different defect class from Attack 1 — not a sign or
frame error within an otherwise-correct setup, but a leftover assumption
carried across a representational switch the document itself documents
(§3.2) without re-examining what that switch does to the reflection-angle
question specifically.

---

## 3. Passivity, reciprocity, and does the 48°–54° gate re-run close every
open EM question?

**Passivity: clean, confirmed independently, at every angle checked.**
`gate_passivity`'s algebraic structure (`|r|≤1` for any `nu≥0` PEC-backed
stack, any angle) is angle-agnostic by construction — it is a property of
the transfer-matrix recursion, not of which angle a caller happens to supply
— so re-running it at 48°–54° was the right check for the question Phase 2
actually raised (has this code path ever been exercised outside its
originally-tested `±44°` range), and it passes cleanly (worst `|r|=0.0386`,
consistent in magnitude with the `±44°` range). I additionally spot-checked
passivity at my own §2b angles (13.7°–15.0°, also never previously
gate-tested) directly from the table above: every `|r|` value is `≤10⁻³`,
comfortably inside the bound. **No passivity violation anywhere this cycle
touches.**

**Reciprocity: not at risk, and not the right frame for this specific gap.**
`reflection_coefficient` enters `θ_deg` only through `sin(θ)²`, even in
`θ` by construction — the function cannot distinguish `+θ` from `−θ`,
matching this program's own prior finding for the x-wall (exp-077 Phase-5
review, §2a, independently re-derived there and not re-litigated here). No
image/source-observer exchange is performed anywhere in this file that would
put reciprocity itself in question; the task brief's own framing ("does it
need a more careful reciprocity argument") is better read, after
independent derivation, as "does it need a more careful *stationary-phase/
geometric-optics* argument" — which is exactly §2's finding — reciprocity
proper is undisturbed.

**Does the 48°–54° gate re-run close every open EM question from Phase 2?
No — it closes the narrower question it was built to answer (is the
transfer-matrix code itself trustworthy outside its originally-sampled
range), and it does close that cleanly. It does not, and structurally
cannot, address whether 48°–54° is the *physically appropriate* range to
query in the first place — that is a question about the geometry feeding
the gate, not about the gate's own arithmetic, and §2 shows the answer is
no.** This is worth stating plainly because the gate re-run's clean PASS
could otherwise read as having fully closed the angle question this cycle
raised; it closes one layer of it and leaves a second, deeper layer (which
this review is the first to surface) untouched.

---

## 4. Has this narrows T28's board correctly, or does it license something
the record doesn't yet show?

`phase4_results.md`'s own honest framing — "this does not close the y-wall
echo mechanism class... but it substantially lowers the case for building
the full y-mirrored coherent propagator" — undersells, not oversells, what
this cycle plus this review together show. Two points, stated plainly for
Iteration 56:

1. **The specific reduction this file builds (edge-dominance + Euclidean-
   distance propagation + swept-angle reflectance) is not merely
   unsupported by data — it is internally inconsistent**, mixing a
   whole-aperture steering convention with a point-source propagation
   convention that, correctly applied, forbids the very θ-dependence the
   model was built to produce. This is stronger grounds for deprioritizing
   the full propagator build (phase1's own open question 5) than the
   as-computed 0/3-SUPPORT/null-calibration result alone: even if the
   period-band scoring had come back marginally encouraging under
   `90−θ_beam`, §2 shows that encouragement would itself have rested on
   the same uncorrected assumption.
2. **This does not touch the full (non-edge-reduced) y-mirrored aperture
   sum**, which is a genuinely different calculation (phase1's own open
   question 3) — a coherent sum over the *whole* mirrored aperture, each
   point with its own image-to-observer angle, could in principle recover
   real θ-dependence through which points dominate the sum shifting with
   `θ_beam`, the same mechanism that makes the x-wall's whole-aperture
   picture work. But phase1's own §3.2 argument (`dPhi/dy_s` never
   vanishes over `36°–42°` for the mirrored sum) already states this sum is
   edge-dominated throughout the swept window, on the *same* footing as the
   real (non-mirrored) sum T21 already established — meaning §2's finding
   plausibly generalizes to the full propagator too, not merely to this
   pre-screen's own reduction. That is a prediction, not yet a result; it
   is the correct next test, not a foregone conclusion, and I rank it
   below.

---

## 5. Ranked top-3 candidate directions for Iteration 56 (my own seat, EM)

1. **Run this review's §2 correction as a cheap, zero-FDTD, pre-registered
   follow-up before any full propagator is built**: re-score
   `y_wall_prescreen.py`'s primary model with `reflection_coefficient`
   evaluated at the per-config geometric bounce angle (`hypot`-derived,
   §2b's table, not `θ_beam` or `90−θ_beam`), confirm `Delta_phi_self(θ)`
   is flat to machine precision as predicted, and record this as a genuine,
   sharper narrowing of the edge-image reduction specifically — distinct
   from, and going beyond, this cycle's own angle-convention fix. This is
   the single cheapest, most information-dense item on the board: it either
   confirms §2's prediction (closing this specific reduction formally, a
   real narrowing) or refutes it (meaning §2's stationary-phase argument
   has an error worth finding, which would itself be informative).
2. **Before committing any FDTD budget to the full y-mirrored propagator
   (phase1 §8 open question 5), settle whether the edge-dominance
   idealization's own stationary-phase argument (no interior stationary
   point over `36°–42°`, for either the real or mirrored aperture sum)
   forecloses angle-swept reflectance for the *full* sum too, not just the
   single-edge reduction** — a short, desk-only stationary-phase check
   (does the full mirrored-sum's stationary point, if any exists, actually
   move with `θ_beam` within this window, or is it edge-pinned throughout
   as phase1's own §3.2 argument already suggests?) before spending the
   moderate (not trivial) build cost item 3 in exp-077's own Phase-5
   ranking named. If item 1 confirms the flat-curve prediction and this
   check confirms edge-pinning generalizes, the y-wall coherent-echo class
   (at least in its point/edge-source form) is close to formally exhausted
   without ever writing the full propagator.
3. **Score the already-built two-wall x-normal model against the already-
   collected 750nm leg** (`experiments/069-.../results.json::block_leg750`)
   — carried unexecuted since Iteration 53's own ranking (item 3), through
   Iterations 54 and 55 both, still zero new FDTD. This is orthogonal to
   items 1–2 (it closes out the x-wall sub-class's own last open thread
   rather than advancing the y-wall one) but remains the single oldest
   deferred item on T28's board and costs nothing to finally clear.

---

## Compliance note

No RULED-OUT item (R1–R9) is re-opened or re-proposed here. §2 is a new,
independently-computed finding not present in `phase1_proposal.md`, any of
the five Phase-2 critiques (including my own), or `phase2_redteam_audit.md`
— verified against the committed geometry (`dg065.CONFIGS`) and the
already-gated `reflection_coefficient`, not a re-statement of the
angle-convention fix already on the record. Consistent with R5's
look-elsewhere discipline: §5 item 1 is explicitly framed as a single,
pre-registrable check, not a new dense parameter search. Consistent with R8:
this review runs the check itself (§2b's table, computed, not argued) rather
than asserting an unverified robustness claim about the corrected model's
own angle.
