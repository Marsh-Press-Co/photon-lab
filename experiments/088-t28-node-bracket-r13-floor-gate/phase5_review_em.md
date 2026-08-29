# PHASE 5 — REVIEW · ELECTROMAGNETISM (blind) · exp-088 · Panel Iteration 65

*Fresh context. Read in full: LOGBOOK.md's RULED OUT (R1–R13) and T28's
complete LIVE THREADS history through Iteration 64/exp-087; PANEL.md;
`phase1_proposal.md`, all five Phase-2 critiques, `phase2_redteam_audit.md`,
`phase3_synthesis.md`, `NOTES.md` (frozen spec + Result), `run.py`,
`results.json` — this cycle's complete record — plus my own
`phase2_critique_em.md` and exp-087's `run.py`/`results.json` for the
raw `i_inc`/`sigma_abs`/`sigma_ext`/`p_abs_w` primitives. All numbers below
independently recomputed from the committed JSON, not restated from
NOTES.md's own prose (R4/R9 discipline).*

## Verdict

**CONCUR with PARTIAL / PROCEED as filed, with one substantive addition
to the record.** No sign-convention, registration, or passivity-bookkeeping
defect is present anywhere in this cycle's own eight cells — a third
instance of the exp-024/exp-087 `i_inc`-sign hazard does **not** recur.
R13's floor gate and the retroactive reclassification (Q1/Q5) are
arithmetically and logically sound, independently reproduced bit-exact.
But the cycle's own headline surprise — `frac_p_abs(θ)`'s non-monotonic
dip at 38.4° — is, on inspection, evidence that plausibly falls *inside*
the exact blind spot this cycle's own EM-authored bracket-width bound
(§4/Idealization, "rules out only a feature ≳0.4° wide") disclosed it
could not rule out, and NOTES.md's Result section never connects the two.
This is not a defect that need block the cycle (the numeric miss is
honestly disclosed, the qualitative CONSISTENT/"C" labels are correctly
computed under the stated gates), but it is a load-bearing gap in how the
cycle characterizes its own most interesting number, and belongs in the
Iteration-66 queue as a named, prioritized item, not folded silently into
"a genuine, disclosed surprise... not adopted as evidence of any
particular mechanism."

## 1. Is the non-monotonic dip physically permitted? Any sign/registration
smell at 38.4° specifically?

**No bookkeeping violation anywhere. No third sign-bug instance.**

Tracing `sigma_abs`/`sigma_ext`/`i_inc` through `widths_direction_corrected()`
at 38.4° directly from `results.json`:

| Cell | `i_inc` | sign applied | `sigma_abs` | `sigma_ext` | `ratio_abs_ext` |
|---|---|---|---|---|---|
| C40 38.4 BOX_A | 0.3269064 | −1.0 | 159.1514 | 310.1750 | 0.51310 |
| C40 38.8 BOX_A | 0.3288500 | −1.0 | 160.0732 | 311.5988 | 0.51372 |
| G40 38.4 BOX_A | 0.3281218 | −1.0 | 159.3170 | 310.2567 | 0.51350 |
| G40 38.8 BOX_A | 0.3293555 | −1.0 | 160.5698 | 312.4852 | 0.51385 |

`i_inc` is smooth and consistently `-x`-signed across all 8 new cells
(0.3269→0.3294, monotonic with θ, no near-zero crossing, no sign flip) —
exactly the behavior EM's own Phase-2 steel-man predicted from
`design_geometry.py`'s fixed `src_x>obj_x>plane_x` geometry. There is no
mechanism by which 38.4° specifically could trigger a different
direction-correction branch than its neighbors, and none did.
`ratio_abs_ext` sits at 0.5131–0.5139 throughout, inside `[0,1]`
(passivity: `0≤σ_abs≤σ_ext`), matching T9's 0.51 broadside anchor to
<0.8%, and `σ_scat+σ_abs=σ_ext` holds to machine precision at every cell
(e.g. C40 38.4 BOX_A: 151.02366+159.15138=310.17504, matching `σ_ext`
exactly) — the extinction identity is intact, not merely gated by
`xi_ext` but directly verifiable. **No sign, registration, or
energy-conservation anomaly exists at 38.4° that would explain the dip as
an artifact; the reading is a genuine measurement.**

**Is a non-monotonic dip in `frac_p_abs(θ)` itself physically permitted?**
Yes, and it is arguably the *expected* shape under this sub-thread's own
established mechanism. `frac_p_abs=|p_abs(G40)-p_abs(C40)|/p_abs(C40)` is
not a single passive quantity constrained by any monotonicity law — it is
the fractional size of a coherent PAD-driven interference delta riding on
a smoothly-rising baseline (both `p_abs(C40)` and `p_abs(G40)` individually
rise smoothly and monotonically with θ across all 5 points; I verified
this directly). Iteration 53's own proof that "`PAD` is provably lossless
vacuum... it cannot, by this proof, be a change in absorbed power" was
scoped to the **boundary's own intrinsic loss** (the damping-mask array,
a pure function of `absorb` alone) — it says nothing about whether a
PAD-shifted round-trip/interference pattern can modulate the *incident
field intensity at the object*, and hence the object's own measured
`σ_abs`. A field-intensity modulation at the object from a PAD-timed
echo is exactly the T1-permitted mechanism exp-087's own PRIMARY
falsification (ENERGY-DOMINANT, not DECOUPLED) already established this
cycle inherits — so a delta that oscillates with θ, including a local
minimum somewhere in a ~5.8° (≈2×`P*≈2.9474°`) span, is consistent with,
not in tension with, that finding. **I checked the sign of every
(`p_abs(G40)-p_abs(C40)`) delta across all 5 points explicitly (this
matters: `frac_p_abs`'s `abs()` construction could mask a sign crossing as
a spurious cusp) — the sign is uniformly positive (G40>C40) at 36.0°,
38.4°, 38.6°, 38.8°, and 41.8° with no flip anywhere.** The dip is a
genuine reduction in the *magnitude* of a same-signed delta, not an
artifact of the absolute-value construction crossing zero.

## 2. Does this cycle's own data violate the bracket-width bound it adopted?

**Yes — plausibly, and this is the cycle's most consequential omission.**
My own Phase-2 attack argued the ±0.2°/±0.4° bracket only rules out a
feature ≳0.4° wide on the absorbed-power channel specifically, and Phase
3 adopted the fix verbatim (NOTES.md's "Bracket-width bound" section).
The frozen text states this as a *forward* caveat about what the test
cannot see. It was never checked against what the test's own results
*actually showed*.

The five-point sequence (`results.json` combined with exp-087's), in
order:

| θ | `frac_p_abs` | Δθ from prior point | ratio to prior point |
|---|---|---|---|
| 36.0° | 1.9655×10⁻³ | — | — |
| 38.4° | **1.3041×10⁻³** | 2.4° | ×0.663 (dip, below 36.0°) |
| 38.6° | 4.0006×10⁻³ | **0.2°** | **×3.068** |
| 38.8° | 5.9552×10⁻³ | 0.2° | ×1.489 |
| 41.8° | 7.2142×10⁻³ | 3.0° | ×1.211 |

The step from 38.4°→38.6° — a single 0.2° grid increment, one-half the
narrowest bracket radius this cycle actually tested — carries a **3.07×**
jump in `frac_p_abs`, by far the steepest slope anywhere in the five-point
record (the next-steepest normalized rate, 38.6°→38.8°, is 1.49× over the
same 0.2°). Whatever produces this curvature has a length scale
comparable to or shorter than the 0.2° grid step itself, i.e. **at or
below the ≳0.4°-wide floor this cycle's own EM-adopted bound explicitly
disclaimed being able to rule out.** This does not prove a genuine
sub-grid resonance exists — a two-cycle-period coherent-interference beat
(T28's established `P*≈2.8421–2.9474°`) sampled at these five uneven
points, or the crude two-anchor linear-interpolation model's own
documented ~7.9% bias, remain live, unresolved alternative explanations,
and NOTES.md is correct not to adjudicate between them. **But the write-up
frames the finding only as "a genuine, disclosed surprise... not adopted
as evidence of any particular mechanism," never noting that its own shape
is a live candidate instance of the exact failure mode the cycle's own
Phase-2 fix predicted might exist and be missed.** That connection belongs
in the record, not left for a reader to reconstruct from two separate
sections.

## 3. `xi_ext`/box-independence at 38.4° vs 38.8°: anything suspicious?

**No gate violation, but a real, quantifiable, previously-unremarked
asymmetry: 38.4° carries this five-point set's thinnest noise-floor
margin.**

All `xi_ext` values at both angles sit comfortably inside `XI_TOL=0.12`
(range 5.3×10⁻⁶–3.9×10⁻⁴ across all 8 cells, no order-of-magnitude
anomaly at 38.4° relative to its neighbors). Box-independence
(`box_dev`) is likewise gate-clean but shows an interesting flip: at
38.4° `G40`'s box-dependence dominates (`abs`=1.61×10⁻⁴ vs `C40`'s
4.96×10⁻⁵, a ~3.2× gap); at 38.8° `C40`'s dominates instead (`abs`=4.70×10⁻⁴
vs `G40`'s 1.90×10⁻⁴, a ~2.5× gap) — the "worse-conditioned config" swaps
between the two angles. This is plausible ordinary Yee-grid/box-placement
noise (`C40`/`G40` sit at different absolute coordinates by construction,
so a fixed clearance samples different grid-relative offsets at each
angle) and is not, on its own, evidence of a defect.

Recomputing the actual resolved-margin (the ratio of the measured signal
`|p_abs(G40)-p_abs(C40)|` to `NOISE_MULT×box_dev_max×p_abs(C40)`, the
quantity `resolved[θ]` gates on) at all five points, independently, from
raw `results.json` fields:

| θ | margin over noise floor |
|---|---|
| 36.0° | 3.20× |
| **38.4°** | **2.70×** |
| 38.6° | 4.49× (excluded by R13, not by this gate) |
| 38.8° | 4.22× |
| 41.8° | 10.67× |

**38.4° — the point carrying the surprise dip — is also the thinnest
margin of the four points that actually enter Q5's CONSISTENT
classification**, notably thinner than its own 38.8° partner (2.70× vs
4.22×) and less than a third of 41.8°'s margin (10.67×). It formally
clears `resolved=True` and the R13 floor (`7.49×` FLOOR, a separate gate)
without ambiguity, so nothing here overturns the classification — but a
number this close to the program's own de facto historical band (compare
38.6°'s own 4.49× margin, independently confirmed in LOGBOOK Iteration 64)
is the least statistically robust of the five readings, and that should
temper how much weight the dip's *precise magnitude* is given, separate
from the qualitative "C" label, which is not in question.

## 4. Other findings from this seat's lens

- **The R13 floor-gate arithmetic is sound and independently re-verified**
  a sixth time (`RMS=1.91744×10⁻³`, `FLOOR=1.91744×10⁻⁴`, all margins
  reproduce to displayed precision from `experiments/083-.../results.json`)
  — no defect found on top of the five Phase-2 critiques' and Red Team's
  own audit's prior six independent reproductions.
- **Q7's T9-anchor extension is clean and reinforces the established
  `σ_abs/σ_ext≈0.51` broadside anchor at oblique incidence** a second time
  (now 8 cells total across exp-087+exp-088, all within 0.55–0.76% of
  0.51) — worth noting as a small, genuine, cumulative confirmation of
  T9's own established near-field-limited caveat (LOGBOOK's ESTABLISHED
  section): nothing here approaches the idealized `≤0.5` geometric-optics
  ceiling in a way that would newly re-open that caveat.
- **Idealization 7 (no settling re-check at 38.4°/38.8°) remains
  low-risk** — the observed dip is a factor-of-~4.6 shape effect (from
  1.30×10⁻³ to 5.96×10⁻³ within 0.4°), several orders of magnitude larger
  than the settling-adjacency evidence cited (`rel_dev(sigma_abs)=7.9×10⁻⁵`
  at the immediately adjacent G40/38.6° spot-check) — a genuine, resolved
  physical/interference reading, not a settling artifact, though this was
  already correctly argued by the proposal and not elevated by Red Team's
  Phase-2 audit; I re-confirm that judgment, not reverse it.
- **Historical-record discipline (fix item 9) is respected**: `results.json`
  and NOTES.md correctly frame Q1/Q5 as a forward-citable reading
  alongside, not a retroactive edit of, exp-087's own filed ENERGY-DOMINANT
  record.

## Sharpest finding

The cycle's own headline surprise — `frac_p_abs`'s dip at 38.4°, followed
by a 3.07× jump in a single 0.2° step to 38.6° — is data whose own shape
plausibly instantiates the exact "feature narrower than 0.4°" failure mode
my own Phase-2 critique raised and this cycle's own adopted bracket-width
bound explicitly disclosed it could not rule out, yet NOTES.md's Result
section never connects the two; separately, 38.4° — the point carrying
this surprise — also carries the thinnest resolved-noise-floor margin
(2.70×) of the five sampled angles, independently recomputed from raw
`results.json` fields and not stated anywhere in the filed record.

## Ranked top-3 for Iteration 66

1. **A tight, direct desk-first-then-cheap-FDTD follow-up bracketing the
   38.4°–38.6° gap itself** (e.g. 38.45°/38.5°/38.55°, 2–6 new calls) — the
   single cheapest, most decisive test of whether the observed 3.07×/0.2°
   slope reflects a genuine sub-0.4°-scale feature on the absorbed-power
   channel (my finding above) or a coarse-sampling/interpolation artifact.
   Same idiom this cycle itself used against exp-087's own node.
2. **A zero-FDTD desk check**: fit T28's own established coherent-PAD
   period (`P*≈2.8421°–2.9474°`) to the SIGNED delta
   `p_abs(G40,θ)-p_abs(C40,θ)` across all 5 now-collected points (this
   cycle's + exp-087's, already-committed JSON, no new FDTD) and ask
   whether a 2-cycle sinusoid over this 5.8° span predicts a trough near
   38.4°–38.5° — directly discriminating between "expected periodic
   confound structure" and "genuinely new narrow feature" for the dip
   this review's §2/§sharpest-finding flags, at zero marginal cost.
3. **Execute Red Team's own already-named, currently-queued Iteration-65
   item 2** (the ~124-call full/denser individual-`σ_abs(C40,θ)`/
   `σ_abs(G40,θ)` build across the full 31-point window) — explicitly
   scoped out of this cycle (Idealization 11) but now doubly motivated:
   it is simultaneously PHOTONICS' own "un-sampled node census" fix (the
   three other `delta_scene` zero-crossings never FDTD-sampled for
   `ratio_k`) and the only instrument dense enough to resolve, rather than
   merely flag, whether the 38.4° dip is representative of a real
   sub-degree structure on the energy channel generally.
