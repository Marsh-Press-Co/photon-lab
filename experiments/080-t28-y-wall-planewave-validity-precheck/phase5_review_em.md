# PHASE 5 — REVIEW · ELECTROMAGNETISM · Panel Iteration 57 · exp-080
## Fresh-context review of the COMPLETE finished cycle (Phases 1–4), blind to
## the other six seats' Phase-5 reviews this cycle

**Seat: ELECTROMAGNETISM** (field/wave behavior, impedance matching, energy
coupling; owns reciprocity/passivity/causality bookkeeping). This sub-agent
has no memory of authoring Phase 1 — the record below is independently
re-derived from primitives, not recalled or trusted from the write-up's own
prose. Read, in full: `PANEL.md`, `AGENTS.md`, `phase1_proposal.md`
(including PHASE 1 RESULTS), `validity_precheck.py` as it now stands
(post-Phase-3 fold-in), `validity_precheck_results.json`, all five Phase-2
critiques, `phase2_redteam_audit.md`, `phase3_synthesis.md`,
`phase4_results.md`, `_output.txt`; background,
`experiments/079-.../phase5_redteam_audit.md` §3/§4c/§0. No RULED-OUT item
(R1–R9) is re-proposed or touched below.

---

## Verdict on the whole cycle: **PARTIAL — confirmed, with one refinement to how part (a) and part (d) are causally linked**

Independent re-derivation reproduces every load-bearing number in the
record exactly. No arithmetic defect, no passivity violation, and no
internal contradiction strong enough to change the Combined Verdict
(FORECLOSE / admittance-family-dependent INCONCLUSIVE-to-REFUTE / PHOTONICS'
image term already built-and-failing). One genuine new finding (§3 below)
sharpens, rather than overturns, the record's own causal story linking part
(a) to part (d) — it should be carried into Iteration 58's queue framing as
a disclosed refinement, not treated as a defect requiring rework.

---

## 1. Fourth independent re-derivation of the Fraunhofer-margin arithmetic

Re-derived from raw geometry in a fresh scratch script, importing only
`dg065.CONFIGS` and `br.CPL` — **not** `y_wall_aperture_sum.py`'s own
`theta_local_deg`/`dist_image_cells` functions, to keep this a genuinely
independent fourth pass (after EM's own Phase-1 script, exp-079's audit
§0.7, and Red Team's Phase-2 from-scratch reproduction):

```
d_F = W²/λ = 1504²/20 = 113,100.8 cells   (identical, all 5 configs)
d_lo = hypot(D_SP, OBJ_Y+y_lo);  d_hi = hypot(D_SP, OBJ_Y+y_hi)
θ_lo = atan(D_SP/(OBJ_Y+y_lo));  θ_hi = atan(D_SP/(OBJ_Y+y_hi))
```

Result, bit-identical to the committed JSON for all 5 configs (spot-check,
C40): `d_lo=861.367`, `d_hi=2346.620`, ratio `0.762%/2.075%`,
`θ_lo=15.0043°`, `θ_hi=5.4531°`, spread `2.7515×`. Every config reproduces
to full float precision. **The FORECLOSE verdict holds on this fourth
independent pass — no discrepancy found.**

---

## 2. Reciprocity/passivity check of `photonics_image_term_curve()`'s `E_direct` omission

**No passivity violation is hidden by the omission**, but the check surfaced
an adjacent, previously-unstated gap in the record's own gating discipline
that is worth fixing forward.

**(a) Bound on the image term itself.** `E_photonics(θ_beam) =
r(90°−θ_beam;ABSORB)·W(θ_beam)`, where `W(θ_beam)` is the `r≡1` ablated
aperture integral (exp-079's own reference scale for "what this aperture
radiates with a perfectly-reflective wall"). Since `E_photonics` is a scalar
multiple of `W`, `|E_photonics|/|W| = |r(90°−θ_beam)|` identically. I swept
`|r(90°−θ_beam;ABSORB)|` at every ABSORB depth over `θ∈[36°,60°]` (covering
and extending past the sub-thread's own `36°–42°` grid) directly from
`br.n_profile_exact`/`ywas.reflection_coefficient_vec`: worst case
`|r|=0.0853` (ABSORB=40, θ=60°), every other depth smaller. So
`|E_photonics|` never exceeds ~8.5% of the aperture's own "perfectly
reflective" radiated scale, at any ABSORB depth or angle this construction
actually uses. A companion spot-check (C40, C70 at θ_beam=39°) confirms
`|E_photonics|/|W|` equals `|r|` exactly (`0.0249` and `0.0020`
respectively) — nowhere near unity, let alone exceeding it. **If `E_direct`
(itself expected to be of order `|W|` or smaller, since it is the same
aperture radiating without reflecting at all) were added back in, the total
could not be pushed into an unphysical (super-unit-reflectivity, gain-like)
regime by this term** — `E_photonics` is a small, `|r|<1`-bounded
perturbation on top of whatever `E_direct` contributes, not a term capable
of masking a passivity violation. The relevant conservation law here
(`|r|²≤1` at the wall, energy in ≥ energy out) is a per-interaction bound
that the omission of a non-wall-interacting term (`E_direct` never touches
the boundary) cannot hide a violation of — coherent superposition of
`E_direct+E_echo` can locally exceed either term alone (ordinary
interference), which is not a passivity violation; passivity constrains the
wall's own reflectivity, not the summed field's pointwise magnitude.

**(b) The adjacent gap, independently found.** `y_wall_aperture_sum.py`'s
own G-LOSSLESS/G-N1/G-PASSIVITY gates (its `main()`, `gate_passivity_range`
et al.) were validated **only** over `[global_lo,global_hi] =
[4.77°,15.50°]` — the `theta_local(y_s)` envelope across all 5 congruent
configs, confirmed by reading the gate-construction code directly
(`all_lo`/`all_hi` built from `theta_local_deg` at each config's `y_lo,y_hi`,
`global_lo,global_hi = min−0.5, max+0.5`). `photonics_image_term_curve()`
and `part_c_power_budget_at_true_angle()` both call the **same**
`reflection_coefficient_vec` at `90°−θ_beam ∈ [48°,54°]` — a range **never
covered by any of this sub-thread's own house gates**. This is not flagged
anywhere in `phase1_proposal.md`, `validity_precheck.py`'s own docstrings,
or either Red Team audit. I independently ran the equivalent of
G-PASSIVITY at this untested range myself (`|r(θ)|` for `θ∈[36°,60°]`, all
4 ABSORB depths, matched admittance family): **worst `|r|=0.0853`, well
under `1.0` — passivity holds**, so nothing is currently wrong. But the
formal gate machinery this program's own house discipline relies on
(`gate_lossless_unimodular_range`/`gate_single_layer_identity_range`/
`gate_passivity_range`) was never re-run at this angle range before
`validity_precheck.py` started evaluating `reflection_coefficient_vec`
there — an unstated extrapolation of already-gated machinery beyond its own
validated envelope, the same shape of gap Idealization 4 discloses in
general terms ("a bug in those primitives is inherited unchanged") but does
not name specifically for this angle range. **Recommendation for Iteration
58 (cheap, zero new FDTD): re-run `gate_lossless_unimodular_range`/
`gate_single_layer_identity_range`/`gate_passivity_range` over
`[47.5°,54.5°]` (the `90°−θ_beam` envelope, with the same 0.5° margin
convention) before `photonics_image_term_curve()` is treated as fully
gated, not merely "probably fine because I checked it once in a Phase-5
review."**

---

## 3. Does the Phase 1→4 chain hold together? A genuine subtlety in how part (a) is used to explain part (d)

The record (Red Team's Phase-2 audit Attack 1, adopted verbatim by Phase 3)
states the amplitude-regime mismatch in part (d) is **"a direct numerical
consequence of part (a)'s own FORECLOSE finding — the aperture never
actually presents `90°−θ_beam` to the wall."** This is directionally right
but **overstates the causal coupling** between the two findings once the
actual numbers are traced through a counterfactual. This is disclosed as a
refinement, not a reversal — it does not change any verdict in the record.

**The check.** `theta_local(y_s) = atan(D_SP/(OBJ_Y+y_s))` is, by the
function's own docstring and by direct inspection, **exactly
`θ_beam`-independent** — it is fixed once the static bench geometry
(`D_SP`, `OBJ_Y`, `y_s`) is fixed, for every `θ_beam` in any sweep.
`90°−θ_beam`, by construction, **varies** with `θ_beam` (48°→54° as
`θ_beam` sweeps 42°→36°). Two objects where one is parameter-independent
and the other is parameter-dependent can coincide at isolated points but
cannot track each other as a matched pair across a sweep — this is true
regardless of near-field or far-field regime, and I verified it
concretely rather than asserting it:

I re-derived `theta_local`'s own **far-field limit** by scaling `D_SP`
upward (holding `OBJ_Y`, `y_lo`, `y_hi`, `W`, `λ` fixed at C40's own
values) until part (a)'s own criterion flips from FORECLOSE to
DOES-NOT-FORECLOSE:

| `D_SP` scale | `theta_local` envelope | spread ratio | `dist_ratio` |
|---|---|---|---|
| 1× (actual bench) | `[5.45°,15.00°]` | `2.75×` | `0.76–2.07%` |
| 10× | `[43.67°,69.54°]` | `1.59×` | `2.10–2.86%` |
| 100× | `[84.02°,87.86°]` | `1.05×` | `19.7–19.8%` |
| 1000× | `[89.40°,89.79°]` | `1.004×` | `197%` (comfortably DOES-NOT-FORECLOSE) |

The spread ratio does converge toward `1×` as the far-field criterion is
satisfied — confirming a single global angle *does* become a good
description of the aperture in the true far field, exactly as part (a)'s
own spread criterion anticipates. **But the value it converges to is
`~90°` (grazing incidence on the wall) — not `48°–54°`, and not tracking
`θ_beam` at all.** This is the direct algebraic consequence of
`theta_local`'s own `θ_beam`-independence: sending `D_SP→∞` with `OBJ_Y`
fixed drives `D_SP/(OBJ_Y+y_s)→∞` for every `y_s`, hence
`theta_local(y_s)→90°` uniformly — a **fixed** value, never a
`θ_beam`-tracking one. A construction (`90°−θ_beam`) whose entire physical
content is "the direction the driven-phase array is steered" cannot
converge to a construction (`theta_local`) whose entire physical content is
"the geometric ray from an image point to a *fixed* observer location,"
because the latter was built, correctly, to have zero dependence on the
former (`y_wall_aperture_sum.py`'s own stated reasoning: each aperture
point radiates as a point source, so `θ_beam` sets each point's *phase*,
not the *geometric direction* its reflected ray takes to a fixed
observer). I also confirmed the same asymmetry the other way: `d_F=W²/λ`
depends only on `W,λ`, never on `D_SP` or `OBJ_Y`, so a hypothetical fix
that satisfied the Fraunhofer ratio by shrinking `W` or lengthening `λ`
instead of moving the wall would leave `theta_local`'s actual values
**exactly where they already are** (`[5.3°,15.0°]`, since `D_SP,OBJ_Y,y_s`
would be untouched) — a DOES-NOT-FORECLOSE part-(a) verdict reached that way
would still leave the `~40°` angle gap versus `90°−θ_beam` completely
unresolved.

**What this means, stated plainly.** Part (a)'s FORECLOSE finding correctly
identifies that a *single global angle* is not yet a valid description of
this aperture's own per-point geometry at the current bench distances — that
much is unqualified and confirmed a fourth time (§1). But it does **not**,
by itself, predict or explain **which** global angle a valid far-field
reduction would converge to, and the value it *would* converge to (`~90°`,
via the one physically meaningful knob — aperture-to-wall distance — that
actually moves `theta_local`) is itself far from `90°−θ_beam`'s swept range.
The two constructions being compared in part (d) differ in a way that is
independent of the near/far-field question: one is a fixed geometric
ray-angle (correct for a point-source array observed at a fixed location),
the other is a swept phase-steering angle (correct for treating the array as
a coherently-launched, θ_beam-directed plane wave) — a conflation the
proposal's own §1 narrative already named in different words ("mirroring in
y... is a genuinely new physical approximation, not an analogous exact
reduction") but which the Phase-2/Phase-3 causal shorthand ("a direct
numerical consequence of part (a)'s FORECLOSE") risks flattening into "just
get farther from the wall and this goes away." **It would not go away** —
resolving the near-field problem would fix the *spread* pathology (all
aperture points agreeing on one angle) without fixing the *choice* of which
angle-generating convention (`theta_local`-style vs `θ_beam`-style) is the
physically correct one to plug into `r()` for a swept-beam echo measured at
a fixed observer.

**This does not change any verdict.** It does not rescue PHOTONICS' `90°
−θ_beam` construction (if anything, it shows the failure mode is more
structural, and less a fixable side-effect of bench distance, than the
current record's phrasing suggests) and it does not touch part (a)'s own
FORECLOSE finding, part (b)'s admittance-family-dependent verdict, or the
Checkpoint-2 NOT-YET-RIPE ruling. It is offered as a sharper, independently
verified statement of *why* part (d)'s mismatch is as large as it is, for
whoever next tries to build a valid global-angle y-wall reduction (Iteration
58's own queue item 2, and any future attempt at this construction family):
the fix is not "move the wall farther away," it is "use an angle convention
whose defining physics actually matches a swept-beam-to-fixed-observer echo
measurement," which `theta_local(y_s)` already is and `90°−θ_beam` is not.

---

## 4. Everything else independently spot-checked, no defect found

- Version-drift guard: recomputed `ywas.echo_field_curve` fresh myself for
  C40/C70 at `θ_beam=39°`; matches the committed curves used throughout
  (consistent with the `0.0` max-diff already reported four times over in
  this record).
- Part (b)'s matched-vs-realizable admittance split, part (c)'s power
  budget at the true `90°−θ_beam` angle, and part (d)'s scale-corrected R²
  values: spot-checked several entries directly from `br`/`ywas` primitives
  (not copied from the JSON) — all match to the reported precision. I found
  nothing to add to Red Team's own eight-item, zero-discrepancy
  reproduction table.
- No RULED-OUT item (R1–R9) is touched, re-proposed, or re-litigated by
  this review or by anything it recommends.

---

## Summary for the Combined Verdict / Iteration 58 queue

**Confirm PARTIAL**, unchanged from `phase3_synthesis.md` §3. Two additions
to carry forward, neither blocking, neither reopening anything closed:

1. **[Cheap, pre-existing gap, not a new defect]** Re-run
   `gate_lossless_unimodular_range`/`gate_single_layer_identity_range`/
   `gate_passivity_range` over `[47.5°,54.5°]` before
   `photonics_image_term_curve()`/`part_c_power_budget_at_true_angle()` are
   treated as fully gated — currently relying on an angle range this
   sub-thread's own house gates never covered. I checked it by hand this
   review (`|r|≤0.0853`, passivity holds) but a hand-check in a Phase-5
   review is not a substitute for the committed gate.
2. **[Refinement, not a reversal]** State explicitly, alongside Attack 1's
   existing framing, that the part-(d) amplitude/angle mismatch is not
   solely a near-field artifact that a farther-away bench would resolve —
   `theta_local`'s own far-field limit is `~90°` (θ_beam-independent by
   construction), not `90°−θ_beam`'s swept `48°–54°` range. Any future
   attempt at a valid global-angle y-wall reduction needs an angle
   convention built from the same fixed-observer ray geometry
   `theta_local(y_s)` already uses, not a borrowed θ_beam-steering
   convention, regardless of how the Fraunhofer margin is eventually
   satisfied.

Full independent-verification detail and the `D_SP`-scaling table above are
reproducible from `dg065.CONFIGS`/`br.CPL`/`ywas.reflection_coefficient_vec`
alone; no new file was written to the repo by this review beyond this
document, per the zero-`lab/`-change, review-only scope of Phase 5.
