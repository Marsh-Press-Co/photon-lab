# Phase 5 Review — QUANTUM OPTICS seat, Panel Iteration 79 (exp-102)

Fresh sub-agent, blind and parallel to the other five Phase-5 seats. I am the
seat that found (a) the `I0_corrected` averaging-order bug at this cycle's
own Phase 2, and (b) the original `i_inc`/cosθ artifact at exp-101's Phase 5
that this whole instrument exists to route around — both re-checked below
from `run.py`'s actual code and `results.json`'s actual numbers, not from
NOTES.md's own restatement of either.

## 1. My own averaging-order fix — genuinely present in the final `run.py`

**Yes, confirmed present, correctly implemented, code-quoted directly**
(`run.py` lines 446-457):

```python
def i0_corrected_and_iinc(cap_empty, cfg):
    cx, cy, hh = ref_for_r4(cfg)
    pi = sc.phasors(cap_empty)
    sxp = sx_profile(pi["ez"], pi["hy"], cx, cy - hh, cy + hh)
    syp = sy_profile_vertical(pi["ez"], pi["hx"], cx, cy - hh, cy + hh)
    mean_sx = float(np.mean(sxp))
    mean_sy = float(np.mean(syp))
    i0_corrected = math.sqrt(mean_sx ** 2 + mean_sy ** 2)
    ...
```

This is `sqrt((mean_y Sx)^2 + (mean_y Sy)^2)` — components averaged first
(`np.mean(sxp)`, `np.mean(syp)`), THEN combined into the norm — exactly my
own Phase-2 proposed fix, and exactly what NOTES.md's Setup section claims
("mean first, then the norm — NOT norm-then-mean"). It is NOT the Phase-1
draft's `mean_y sqrt(Sx²+Sy²)` (norm-then-mean, the Jensen's-inequality-
biased form I flagged). The later, independently-found sign-correction pass
(Gate C's `u_x(θ)=-cosθ` vs. bare `cosθ`) touches only the comparison step
against `i_inc` (line ~641-643, `dev = abs(r["i0_corrected"] * u[0] -
r["i_inc"]) / r["i0_corrected"]`) — it does not re-touch `i0_corrected`'s own
internal averaging order. I traced both fixes end-to-end and confirm they
compose correctly: `i0_corrected` is computed once (mean-then-norm, my fix),
then used twice downstream — once signed correctly via `u_x(θ)` (Gate C,
the later fix) and once, appropriately, left unsigned in `I_abs(θ)`'s own
denominator (a magnitude reference, correctly not touched by the sign fix at
all). **Both bugs are fixed and coexist correctly in the committed code.**

## 2. Independent re-derivation of Gate C's sign, `u_x(θ)=-cos θ`

I re-derived this from source, not from NOTES.md's own account.

**Step 1 — propagation direction, from `lab/fdtd2d.py`'s own docstring**
(`add_line_source`, lines 138-140, read directly): "The −x-going wave then
travels along (−cosθ, +sinθ)." Every `R4_CONFIGS` entry has `src_x > obj_x`
(confirmed: `run.py`'s own `downstream_sign()` assert, lines ~369-372, which
would raise `AssertionError` at import time if false — and it did not, since
`results.json` exists) — the wave launched at the source and reaching the
object travels toward −x, so this is the applicable convention:
`u(θ)=(−cosθ, sinθ)`, hence `u_x(θ)=−cosθ`.

**Step 2 — the Poynting-vector sign convention, re-derived from Maxwell's
equations myself, not merely trusted from `sections.py`.** For 2D TE fields
(`Ez, Hx, Hy`), `S = E×H = Ez ẑ × (Hx x̂ + Hy ŷ) = -Ez Hy x̂ + Ez Hx ŷ`
(using `ẑ×x̂=ŷ`, `ẑ×ŷ=-x̂`). Time-averaged, phasor form:
`Sx = -0.5 Re{Ez conj(Hy)}`, `Sy = +0.5 Re{Ez conj(Hx)}` — this is EXACTLY
`sx_profile`/`sy_profile_vertical`'s own formulas (`run.py` lines 429-443,
lifted verbatim from `_face_flux`). Independently re-derived from first
principles, not merely re-read from source: the sign convention is correct.

**Step 3 — combine.** A locally-plane-wave field's time-averaged Poynting
vector points along its own propagation direction with magnitude `I0`:
`S ≈ I0·u(θ)`. So `Sx ≈ I0·u_x(θ) = -I0 cosθ`, meaning `i_inc = mean_y(Sx)`
should itself be **negative** and satisfy `i_inc ≈ I0_corrected·(-cosθ)`,
i.e. `u_x(θ)=-cosθ` is the correct sign for Gate C's comparison —
independently confirming NOTES.md's own derivation, arrived at from the
source docstring and Maxwell's equations directly, not from NOTES.md's
prose.

**Quantitative cross-check (my own, not in NOTES.md): the magnitude of the
"bug" predicts the magnitude of the artifact exactly.** If the bare-`cosθ`
(unsigned) formula is used against a true `i_inc≈-I0 cosθ`, the relative
deviation should be `|I0 cosθ - (-I0 cosθ)|/I0 = 2|cosθ|`. At the six R4
angles (37.13°–42.96°), `2cos θ` ranges `2×0.7318=1.464` to `2×0.7973=1.595`
— i.e. **146.4%–159.5%**. I recomputed the original-erroneous deviations
directly from `results.json`'s stored `i0_corrected`/`i_inc`/`u_x` fields
independent of any stored `dev_original_erroneous_cos_theta` field, and got
range **145.4%–159.8%**, max 159.78% — matching my closed-form `2cosθ`
prediction to within the expected plane-wave-approximation residual. This is
strong, independent confirmation that the ~150% "deviation" is a pure sign
artifact of exactly the predicted size, not a coincidence and not per-cell
noise (corroborating Learned item 3's own diagnostic claim). I also
independently recomputed the corrected-formula deviations from the raw
`i0_corrected`/`i_inc`/`u_x` fields: max **0.9198%** — matches the reported
`max_dev=0.009197942611745866` in `results.json` exactly.

## 3. Non-classical-absorption / coherent-interaction concern: none found

Confirmed genuinely true, per my seat's expressibility contract. I read
`run.py` in full: the article is the byte-identical R4-family
`pec_disk`+`graded_black_shell` (linear, passive, real-valued `σ`), used
unmodified from `experiments/069-.../design_geometry.py`'s constants. No
`σ(I)`, `σ(x,t)`, dispersive `ε(ω)`, or gain parameter appears anywhere.
Every new quantity this instrument computes (`κ(θ)`, `Δφ(θ)`,
`I0_corrected(θ)`, `I_abs(θ)`) is a classical linear-response field/Poynting
construction — a same-point complex-phasor ratio and a Poynting magnitude,
nothing quantum-coherence-specific (no entanglement, no photon-number
statistics, no state-dependent cross-section). This is exactly what a
diagnostic instrument on an already-locked classical article should be. No
seat-charter concern.

## 4. Independent numeric re-verification (recomputed, not restated)

I loaded `results.json` directly and recomputed, from the raw
`primary_rows`/`gates` dicts (not from NOTES.md's prose), the following —
all reproduce:

- Gate C: recomputed `|i0_corrected·u_x − i_inc|/i0_corrected` for all 12
  cells from raw fields → max **0.9198%**, min **0.0435%** — exact match to
  `results.json`'s own stored `max_dev` and to NOTES.md's stated "range
  0.04%–0.92%."
- Gate D: recomputed `rel_dev_region` from raw `kappa_region_correct`/
  `kappa_region_perturbed` → **48.95%** (C40_R4), **8.24%** (G40_R4) — exact
  match.
- Off-axis `κ_off(θ)`: recomputed min/max across all 12 cells →
  **1.0406–1.0766**, matching NOTES.md's "1.041–1.077."
- Point-vs-region ratio: recomputed `max(κ_point,κ_region)/min(...)` across
  all 12 cells → **1.230–1.559**, matching NOTES.md's "1.23–1.56×."
- `Δφ(θ)`: recomputed min/max → **0.2092–0.5871** rad, all positive,
  matching "+0.21–+0.59 rad."

## 5. Citation/restatement defect found (R4/R20 lineage) — flagging

**One genuine, previously-uncaught R4-class defect, independently found by
direct recomputation, non-load-bearing.** NOTES.md's Result section states:
"on-axis coherent intensity ratio `κ(θ)` (region-averaged) ranges
`3.68×10⁻³`–`7.29×10⁻³` across all 12 (angle,config) cells." I recomputed
`min`/`max` of `kappa_region` across all 12 `primary_rows` entries directly
from `results.json`: **min = 3.479968×10⁻³** (`C40_R4@41.460901`), **max =
7.289772×10⁻³** (`C40_R4@42.960901`). The maximum matches exactly. The
stated minimum, `3.68×10⁻³`, does NOT reproduce — the true minimum is
`3.48×10⁻³` (a different cell); `3.6815×10⁻³` (`C40_R4@38.59023`) is the
true THIRD-lowest value, not the minimum. This is the same shape of defect
as R4/R20's own registry (a claimed range/extremum figure that does not
reproduce from its own cited `results.json`), caught only at Phase 5.
**Non-load-bearing**: both the true and the stated minimum satisfy
Prediction 1's `κ(θ)∈[0,0.10]` band by a wide margin, so no verdict changes.
Recommend a same-shift, zero-FDTD prose correction (`3.68×10⁻³`→`3.48×10⁻³`)
before this figure is cited elsewhere. This is a single, isolated instance
on my own independent check — I do not have visibility into whether other
Phase-5 seats found additional R4-class defects this cycle; if any do, this
instance should be counted alongside theirs against R20's "three or more"
bar (not yet met on what I alone can see).

## 6. Verdict: **CONFIRM-WITH-GAPS**

The instrument's central contribution is genuine and correctly executed:
`κ(θ)` sidesteps the `i_inc`/cosθ artifact by construction (never calls
`sc.widths()`), the rotating-frame `P(θ)` construction is independently
validated by Gate D (a real positive control, not a self-comparison), and
both of the averaging-order and sign defects this instrument's own
development surfaced are now correctly and independently fixed, confirmed
above from source and from raw data respectively — not merely trusted from
NOTES.md's own account. The **gaps** are real and disclosed, not
manufactured for form's sake: (i) Gate B, the one gate meant to cross-check
this new instrument against the bench's own established `beam_behind`
figure, genuinely FAILS, and remains failed — this cycle's own primary-
channel numbers are validated only by Gates A and D (internal-consistency
and fault-injection), not by an independent cross-scale reproduction, a real
open limitation correctly named in Learned/Next rather than hidden; (ii) the
`κ_region` range citation defect in §5, new and independently found here.
Neither gap changes any of the five scored prediction verdicts. Recommend
CONFIRM-WITH-GAPS rather than plain CONFIRM specifically because Gate B's
unresolved failure means "this instrument is trustworthy" currently rests on
one fewer independent leg than the four-gate design intended — a genuine,
not cosmetic, shortfall for the next cycle to close.

## 7. Ranked top-3 candidate directions for Iteration 80

1. **A properly-scoped Gate B**, matched to the established `beam_behind`
   figure's own spatial footprint (the literal `BEHIND` window, or an
   R4-scale equivalent) rather than a rescaled point/region sample —
   closing this cycle's own most consequential open gap (§6) before this
   instrument's readings are cited as validated elsewhere. Highest priority:
   without it, every future `κ(θ)`/`I_abs(θ)` citation still rests on
   internal self-consistency alone, not cross-instrument agreement.
2. **The Tier-2 perceptual conversion** (constraint 1's own missing
   conversion from this cycle's raw `κ(θ)`/`I_abs(θ)` to a witness-perceived
   `C_thr(L)` judgment, VISION's charter) — now has a genuine, phase-
   resolved, artifact-free physical input to build on for the first time on
   this bench, the natural next step once (1) is either done or explicitly
   deferred.
3. **Formalize Learned item 4's candidate standing rule** (a vector-valued
   self-consistency identity's SIGN must be independently re-derived from
   the same convention already governing that vector elsewhere in the same
   document, not merely checked for magnitude) — this cycle is itself the
   second on-the-books instance of a sign slipping past multiple review
   layers that correctly caught magnitude/averaging-order issues (exp-073's
   R4 addendum was the first); worth Red Team's explicit ratify-or-decline
   ruling before a third instance forces the question reactively.
