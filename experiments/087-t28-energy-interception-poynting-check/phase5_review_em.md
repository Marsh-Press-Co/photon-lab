# PHASE 5 — REVIEW (ELECTROMAGNETISM) · Panel Iteration 64 · exp-087

## 0. Scope of this review

Independent re-derivation from first principles of `widths_direction_
corrected()`'s fix, per this cycle's charge — not a re-reading of `run.py`'s
own comment. All numbers below are recomputed directly from `results.json`
and from source (`lab/sections.py`, `lab/fdtd2d.py`, and the cited historical
`run.py`/`design_geometry.py` files), not restated from `NOTES.md`.

## 1. Is `sign(i_inc)` the physically correct fix? Yes — re-derived, not assumed

`_face_flux(ez, hx, hy, box)` sums `sx(x1)-sx(x0)+sy(y1)-sy(y0)` where
`sx`/`sy` are the module's own stated TMz Poynting components (`<Sx> =
-1/2 Re{Ez conj(Hy)}`, `<Sy> = +1/2 Re{Ez conj(Hx)}`). These are physical
field relations valid for *any* field configuration, forward- or
backward-propagating — nothing in their derivation from Maxwell's curl
equations assumes a propagation direction. By the divergence theorem, the
signed sum over the four faces is therefore a **coordinate-invariant** net
outward power flux through the box, regardless of which way the incident
wave travels. Consequently:

- `p_scat = _face_flux(scattered fields)` — genuinely non-negative for a
  passive scatterer (real emitted power), any propagation direction.
- `p_abs = -_face_flux(total fields)` — genuinely non-negative for a
  passive (σ_e≥0) absorber, any propagation direction.
- `p_ext_cross = -_cross_flux(pi, ps, box)` — same construction, same
  invariance argument; the optical theorem's own shadow-formation statement
  doesn't care which way the beam points either.

`i_inc`, by contrast, is *not* built this way: it is `sx()`'s formula
evaluated at a single fixed plane and used as a plain scalar divisor. For a
`+x`-propagating source this is positive by luck of geometry, not by
construction; for `PAIR_PAD`'s `-x`-propagating scene it is negative,
correctly reporting a genuinely negative x-flux at that plane. **The bug is
purely that a signed flux was used where an intensity magnitude was
required — nothing in `_face_flux`/`_cross_flux` themselves needed fixing,
confirmed by re-derivation, not merely by reading the comment that made this
claim.**

Algebraically, `sigma_raw = P/i_inc_raw`. The physically correct quantity is
`sigma_correct = P/|i_inc_raw| = sigma_raw · sign(i_inc_raw)`. So
`widths_direction_corrected()`'s two stated operations — "recover each raw
power and re-divide by `abs(i_inc)`" and "equivalent to multiplying every
sigma_* field by `sign(i_inc)`" — are **the same single operation described
two ways**, not two independent claims that happen to agree; there is no
double-correction risk. Confirmed directly: every cell in `results.json`
carries `direction_correction_sign_applied: -1.0`, consistent with a
uniformly `-x`-propagating scene.

**`xi_ext`/`box_dev` invariance, re-derived, not just cited:** both are
ratios of quantities that share the identical `i_inc` (same `ref_for(cfg)`
regardless of box), so the same `s=sign(i_inc)` multiplies numerator and
denominator identically in both `xi_ext = |sigma_ext_cross-sigma_ext|/
|sigma_ext|` and `box_dev = |sigma_ext(BOX_A)-sigma_ext(BOX_B)|/
|sigma_ext(BOX_A)|` — both provably unaffected. Confirmed by recomputing
`xi_ext` directly from `results.json::widths`' raw `sigma_ext`/
`sigma_ext_cross` fields at all 12 `(cfg,θ,box)` cells: max observed
`4.195×10⁻⁴` (`G40, θ=41.8°, BOX_A`), consistent with the reported
`≤0.00048`; e.g. `C40, θ=36.0°, BOX_A`: `|300.8243530749198 −
300.77047991578854| / 300.77047991578854 = 1.791×10⁻⁴`.

## 2. Passivity sanity check: `sigma_abs/sigma_ext`, recomputed at every cell

Recomputed directly from `results.json::widths`, all 12 `(cfg,θ,box)`
cells: `sigma_abs/sigma_ext` ranges **0.51277–0.51381** — inside `[0,1]`
everywhere (required by passivity: `sigma_scat,sigma_abs≥0` for a lossy
passive object ⇒ `0≤sigma_abs/sigma_ext≤1`), and remarkably close to T9's
own long-established `graded_black_shell` broadside anchor (`σ_abs/σ_ext=
0.51`, exp-002/ESTABLISHED) even though this is oblique incidence (36–42°)
on a PAD-shifted box, both never previously combined. This is strong,
independent corroboration that `p_abs`/`p_scat` individually carry the
correct sign and relative magnitude — this ratio is *exactly* invariant to
any `i_inc`-sign defect (both operands share the same `i_inc`, which
cancels), so its consistency with T9 confirms `_face_flux` itself was never
broken; only the external normalizer was.

## 3. `ENERGY-DOMINANT` at θ=38.6° does not violate T1/passivity

`ratio_k = frac_p_abs/frac_contrast` compares two dimensionally-different
observables under linear, passive bookkeeping: a bulk box-perimeter
absorbed-power fractional change and a local, background-subtracted
Weber-contrast fractional change. Nothing in reciprocity/passivity/energy
conservation constrains their ratio to any particular range — a linear
passive medium is free to produce a large bulk-power change alongside a
small local-contrast change, or vice versa; they are different projections
of the same field, not two measurements of one conserved quantity. **This
is a surprising result relative to this sub-thread's ten-plus-cycle prior
(phase/interference-dominant, energy-decoupled), not a physically forbidden
one** — worth stating explicitly since PANEL.md gives this seat exactly
this bookkeeping duty, and it is not stated anywhere in `NOTES.md`/
`phase3_synthesis.md`.

Independently re-derived the θ=38.6° outlier from `results.json`
(`ratio_k`: 36.0°→2.6423677612294223, 38.6°→53.988397675546146,
41.8°→5.710203290428644) and confirm `NOTES.md`'s own node-artifact
account: `frac_contrast(θ)=|delta_scene(θ)|/|C40_C(θ)|` has a numerator
that is *structurally* a ratio blowing up near a zero-crossing of
`delta_scene(θ)` — the same "ratio ill-conditioned near a node" instability
class this program has independently hit before (the R5/R9 lineage, applied
there to a search space and a unit mismatch respectively, here to a
denominator crossing zero). Even fully discounting θ=38.6° as a node
artifact, the surviving two angles read `ratio_k∈{2.64,5.71}` — squarely
**CONSISTENT** (0.1–10), not the predicted **ENERGY-DECOUPLED**. I concur
with `NOTES.md`: P7 is genuinely FALSIFIED, not merely a fragile single-cell
artifact.

## 4. A materially incorrect historical claim in `run.py`, independently caught

`run.py`'s `widths_direction_corrected()` docstring and `NOTES.md`'s Result
section both assert: *"every PRIOR caller of `widths()` (exp-002/024's own
absorber bench) had `src_x<obj_x`, propagating in +x... T28's `PAIR_PAD`
geometry is the FIRST `widths()` application with `src_x>obj_x>plane_x`."*
Per this cycle's own charge to verify this as a claim, not accept it as
fact: **this is false for exp-024, one of the two experiments the sentence
names as precedent.**

- `experiments/024-ambient-margin-adjudication/design_geometry.py`:
  `SRC_X=300`, `OBJ_X=170`, `PLANE_X = OBJ_X - R_OUT - PLANE_DX = 77` —
  i.e. `src_x(300) > obj_x(170) > plane_x(77)`, the **identical** directional
  relationship as T28's `PAIR_PAD`.
- `lab/fdtd2d.py::Sim.add_line_source`'s own docstring is explicit: *"The
  −x-going wave then travels along (−cosθ, +sinθ)"* — confirming exp-024's
  source, launched from `SRC_X=300` at oblique `angle_deg=theta`, is
  genuinely `-x`-propagating toward the object at `OBJ_X=170`, exactly like
  `PAIR_PAD`.
- exp-024's own `run.py` (line 101) calls `sc.widths(cap, cap_e, dg.BOX,
  REF)` directly on this `-x`-propagating scene — and its own P6 gates
  (lines 195–199) already wrap `sigma_abs*i_inc` and `net_box_flux` in
  `abs()` before comparing them, and `sigma_ext_cross-sigma_ext` in
  `abs(...)/abs(sigma_ext)` — a defensive pattern consistent with the same
  negative-`i_inc` phenomenon having been present and silently absorbed at
  **Panel Iteration 2**, many cycles before T28 existed, never diagnosed or
  named as a sign-convention issue. (exp-024's raw per-cell `sigma_abs` is
  not persisted to `results.json`, only gate ratios that already use
  `abs()`, so this cannot be confirmed to the same bit-exact standard as
  this cycle's own finding — but the geometry and the defensive-`abs()`
  code pattern together make "the same defect, present and silently
  worked around three years and 62 iterations earlier" the better-supported
  reading than "genuinely novel this cycle.")
- By contrast, `experiments/002-cross-sections/run.py` (`SRC_X=64`,
  `CX=252` ⇒ `src_x<obj_x`, genuinely `+x`-propagating) is the one member
  of the cited pair that actually fits the claimed history — confirmed
  directly from its own `results.json`: raw `sigma_abs` values are
  positive for both lossy articles (absorber: 122.8–124.3; the lossless
  `reflector`/PEC case reads small negative values, `-0.37`/`-0.60`,
  consistent with the established "lossless object's absorption channel
  reads ~zero" identity, not a direction defect).

**This does not weaken the fix — it strengthens it**: the diagnosis
generalizes to a real, recurring pattern in this codebase (any `widths()`
caller with the source on the far side of the object from the observation
plane), not a one-off. But the specific "first-ever" framing is an
overclaim that should be corrected in `NOTES.md`/LOGBOOK before it
propagates as settled fact the way several other precisely-this-shaped
claims have in this sub-thread's own history (the R4 lineage exists for
exactly this reason — an unverified "first"/"precisely recomputed" claim
recurring un-caught).

## 5. A second, non-blocking sign/label defect found underneath, as charged

`sections.widths()`'s `back_frac`/`fwd_frac` (`p_back` at the box's `x0`
face, `p_fwd` at `x1`) are computed under an unstated assumption baked into
the box-face convention: `x0` (upstream in a `+x`-propagating scene) =
"backward, toward the source." For T28's `PAIR_PAD` (`src_x>obj_x`), the
source sits on the `x1` side, not `x0` — **the labels are inverted for this
geometry.** Recomputed from `results.json::widths` (raw, unaffected by the
`i_inc` fix — `back_frac`/`fwd_frac` never pass through
`widths_direction_corrected()`'s sign multiply): e.g. `C40, θ=36.0°,
BOX_A`: `back_frac=0.6756`, `fwd_frac=8.5×10⁻⁵`. Correctly read for this
scene's real geometry, this means **~68% of scattered power continues
downstream (away from the source, toward the observation plane) and only
~0.0085% returns toward the source** — the code's own field names report
the opposite assignment.

This is **not outcome-determining for this cycle**: P7's classification
uses only `sigma_abs`/`sigma_ext` via `thermo_sidecar`, never
`back_frac`/`fwd_frac`. But these fields ARE persisted, verbatim, in this
cycle's own `results.json`, and any future consumer reading them at face
value — especially anything touching constraint 2 ("no specular return to
the observer") on a `-x`-propagating T28 scene — would get the physically
backward answer. Flagged here per this seat's charter duty to check
whether "`_face_flux`'s own outward-positive convention... already
correctly handles any propagation direction on its own" extends to every
field `widths()` returns: it does for `sigma_scat`/`sigma_abs`/
`sigma_ext`/`sigma_ext_cross` (Section 1), but **not** for `back_frac`/
`fwd_frac`, which carry their own, separate, uncorrected directional
assumption.

## Verdict on this cycle's Combined Verdict contribution

**Concur: P7 is genuinely FALSIFIED (ENERGY-DOMINANT), not an instrument
artifact.** The direction-correction fix is re-derived here from first
principles (Section 1), independently confirmed on raw fields (Sections
1–2), and the primary result survives even discounting the one node-driven
outlier angle (Section 3). This is a materially new finding, correctly
scoped (does not test constraints 1/2/4, does not re-open
`REALIZABILITY_MEMO.md`), that should stand.

Two corrections are needed before this cycle's record is treated as
closed, neither reversing the verdict:

1. **Correct the "first-ever `src_x>obj_x` application" claim** in
   `NOTES.md`/`phase3_synthesis.md`'s citation trail (Section 4) — it is
   independently falsified by exp-024's own geometry and its own
   already-defensive `abs()` code, which this cycle's authors did not
   check before asserting the negative.
2. **Disclose the `back_frac`/`fwd_frac` direction-label defect** (Section
   5) inline wherever this cycle's `widths` data is next cited, so no
   future cycle reads `results.json::widths::*::back_frac` at face value
   for a `-x`-propagating T28 scene.

Neither correction is a Checkpoint-4-shaped defect (no false claim reached
a scored verdict; both are citation/completeness gaps in supporting prose,
caught here, same-shift-correctable) — but both should be recorded, per
this program's own standing discipline that a Phase-5 reviewer must
independently re-derive, not restate, load-bearing claims (R4 lineage).

## Ranked candidate directions for Iteration 65

1. **(Tier 0, zero FDTD, cheap)** Fix or wrap `back_frac`/`fwd_frac`
   analogously to `widths_direction_corrected()` (or add a documented,
   gated `lab/` change) before these fields are ever consumed for a
   constraint-2-adjacent question on a `-x`-propagating scene — closes the
   Section 5 gap at essentially zero cost, using data already in hand.
2. **(Tier 0, zero FDTD, cheap)** Correct the historical record: log that
   exp-024 (Iteration 2) most likely carried the same negative-`i_inc`
   phenomenon, silently absorbed by ad hoc `abs()` wrapping, never
   diagnosed — the "first observed here, fixed here" framing should read
   "first *diagnosed* here; likely present and silently worked around
   since Iteration 2." Improves institutional memory quality at zero
   marginal cost.
3. **(Tier 1, cheap FDTD)** Densify sampling around θ=38.6° (a handful of
   angles either side) to determine whether `ENERGY-DOMINANT` is a real,
   narrow, node-adjacent feature or an artifact of a single unlucky grid
   point coinciding with `delta_scene`'s own zero-crossing — needed before
   this cycle's most striking single number is treated as a robust
   physical finding rather than a single-angle read.
4. **(Tier 1, cheap FDTD)** Now that the direction-corrected Poynting-box
   channel is validated (`xi_ext` clean, non-negativity clean,
   T9-anchor-consistent even obliquely), extend the same energy-
   interception measurement to `PAIR_ABSORB40`/`C80−C40` and to
   450/750nm — the CONSISTENT/ENERGY-DOMINANT bulk-vs-local coupling this
   cycle found is a new claim that needs a second config/wavelength before
   it generalizes past this one geometry.
5. **(Tier 2, governance)** Consider hardening `lab/sections.py::widths()`
   itself to normalize by `abs(i_inc)` internally (one-line change, a new
   stage-8 gate on a synthetic `-x`-propagating scene), rather than
   leaving this a caller-side responsibility — we now have two
   independent instances (exp-024, exp-087) of this exact geometry
   tripping the same latent issue; a third future caller should not have
   to rediscover it.
