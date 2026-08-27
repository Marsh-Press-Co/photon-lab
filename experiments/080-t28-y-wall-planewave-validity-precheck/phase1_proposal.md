# PHASE 1 — PROPOSAL · ELECTROMAGNETISM · Panel Iteration 57 · exp-080
## EM's own named validity pre-check of the plane-wave/global-steering y-wall
## construction, run BEFORE anyone builds it

**Seat: ELECTROMAGNETISM** (field/wave behavior, impedance matching, energy
coupling; owns the reciprocity/passivity/causality bookkeeping). Lead this
cycle, by rotation. Read, in order: `PANEL.md` in full (this seat's own
charter, the target phenomenon + four constraints, the five-phase loop, the
Checkpoints section); `AGENTS.md` in full; the Director's condensed LOGBOOK.md
extract (RULED OUT R1–R9 in full; the T28 live-thread history, Iterations
46–56); `experiments/079-t28-y-wall-full-aperture-sum/phase5_redteam_audit.md`
§3 and §7 in full; `experiments/079-.../phase5_review_photonics.md` §4 in
full; `experiments/065-.../design_geometry.py`, `experiments/075-.../
boundary_reflectance.py`, and `experiments/079-.../y_wall_aperture_sum.py` in
full (the machinery this pre-check imports and reuses, never reimplements).

**No RULED-OUT item (R1–R9) is re-proposed.** This is a validity
pre-condition check on a not-yet-built instrument, not a mechanism claim of
its own — nothing here asserts a real y-wall echo, a shell-thickness rule, or
any dominantly-real Δε mechanism.

---

## 1. Mechanism narrative (≤300 words)

Red Team's exp-079 final audit (§3) and PHOTONICS' own Phase-5 review (§4)
both recommend, as the next T28 y-wall instrument, a **plane-wave/
global-steering** construction: apply ONE scalar `r(90°−θ_beam;ABSORB)` to
the *entire* mirrored aperture sum, mirroring how the x-wall's own exact
two-plane-wave reduction (`boundary_reflectance.py::c_empty_with_wall`)
applies a single `r_coeff` globally. The x-wall trick works because
mirroring *in x* leaves the aperture's own y-dependent driven phase and taper
untouched — the whole aperture presents one incidence angle to an x-normal
wall. Mirroring *in y* has no such symmetry: it flips the very coordinate the
taper and driven phase depend on, so a global-angle y-wall model is a
**genuinely new physical approximation**, not an analogous exact reduction.

EM's own charter obligation here is not to build that instrument but to
formalize, before anyone spends the build effort, whether replacing the
already-tested per-point bounce angle `theta_local(y_s)` with one global
angle is even a defensible approximation of the real multi-point
aperture-wall interaction — i.e. whether the aperture sits close enough to
its Fraunhofer distance from the wall, and whether `theta_local(y_s)`'s own
spread across the aperture is small enough, that a single incidence angle
could stand in for the true per-point geometry. This matters because a third
consecutive T28 y-wall cycle discovering, only after a build, that its
headline instrument could never have answered the question it was built for
(after the as-filed `theta_beam` bug and the corrected `90−theta_beam` bug)
would be exactly the failure shape this program's own R4 discipline exists
to catch early. If this pre-check forecloses the approximation, the Tier-0
build should not proceed as literally sketched; if it does not, PHOTONICS'
own build (§4 of its review) proceeds immediately, using this cycle's own
`theta_eff` machinery as a documented fallback characterization even where
the eventual construction uses `θ_beam` itself, not a static `theta_eff`.

---

## 2. Parameter table

All geometry constants below are direct lookups from already-committed code
(`dg065.CONFIGS`, `br.CPL`), not new computations — they are re-confirmed by
direct import in `validity_precheck.py`, never hand-typed (R4), but they are
not "the run": the run is the Fraunhofer-margin/spread ARITHMETIC on top of
these constants (part (a)) and the single-angle reconstruction test (part
(b)), both deferred to post-freeze per this program's house discipline.

| Symbol | Meaning | Source | Value (structural constant, re-confirmed not hand-typed) |
|---|---|---|---|
| `W` | aperture width (`aperture_cells`) | `dg065.CONFIGS[key]["aperture_cells"]` | asserted `1504` cells for every congruent-series config (`design_geometry.py`'s own congruence check) |
| `λ` | wavelength in cells at 600nm | `br.CPL[600]` | `20` cells |
| `D_SP` | source-to-plane x-distance | `dg065.CONFIGS[key]["d_sp"]` | `223` cells, congruent-series constant |
| `OBJ_Y` | aperture center y-coordinate | `dg065.CONFIGS[key]["obj_y"]` | varies by `PAD` (792/812/822/832/832 for C40/C60/C70/C80/G40) |
| `y_lo, y_hi` | aperture edge coordinates | `dg065.CONFIGS[key]` | per-config, congruent aperture width held at 1504 |
| `d_F` | Fraunhofer/far-field distance | derived: `d_F = W²/λ` | to be computed in `validity_precheck.py`, **not** copied from the exp-079 audit's own citation |
| `dist_image(y_s)` | image-to-observer propagation distance | `ywas.dist_image_cells(y_s, cfg) = hypot(D_SP, OBJ_Y+y_s)` | evaluated at `y_s∈{y_lo,y_hi}` per config |
| `theta_local(y_s)` | per-point rigorous bounce angle | `ywas.theta_local_deg(y_s, cfg) = atan(D_SP/(OBJ_Y+y_s))` | evaluated at `y_s∈{y_lo,y_hi}` per config (envelope) |
| `theta_eff` (PRIMARY) | one "effective" global angle per config | amplitude-weighted mean: `∫amp(y_s)·theta_local(y_s) dy_s / ∫amp(y_s) dy_s`, native (`oversample=1`) grid, `amp=ywas.aperture_amplitude` | computed in `validity_precheck.py` |
| `theta_eff` (SECONDARY, robustness) | aperture-midpoint angle | `theta_local(y_s=OBJ_Y)` | computed in `validity_precheck.py` |
| GoF metric | goodness of fit, single-angle vs true curve | `R² = 1 − SS_res/SS_tot`, `SS_res=Σ(true−model)²`, `SS_tot=Σ(true−mean(true))²` | per config, both proxies (`Re{E_echo}` primary, `|E_echo|` secondary) |

**Why the amplitude-weighted mean, not another `theta_eff` definition.**
`theta_local(y_s)` enters the true per-point integral weighted by
`amp(y_s)` (the raised-cosine taper) — the same weight that determines how
much each aperture point actually contributes to the coherent sum before
any reflectance or phase factor is applied. Weighting the mean by that same
`amp(y_s)` is the most direct one-number summary of "the angle the
amplitude-weighted aperture as a whole presents," and avoids circularity
(it does not use `r(theta_local(y_s))` itself to decide which points matter
most for defining the angle that then gets used to evaluate `r`). The
aperture-midpoint value is reported as a cheaper, more naive alternative —
useful precisely because it is likely to diverge somewhat from the
amplitude-weighted mean when the taper reshapes the effective aperture
center, giving a concrete robustness bound on how much the choice of
`theta_eff` definition alone can move the answer.

---

## 3. Idealizations

1. **`theta_eff`'s definition is a modeling choice, not a derivation.**
   Amplitude-weighting is the most defensible of several plausible choices
   (others: unweighted mean, energy (`amp²`) weighted mean, `r`-weighted
   mean) but is not uniquely forced by the physics. The midpoint
   cross-check bounds — but does not eliminate — this choice's own
   sensitivity.
2. **A high `R²` here does not itself validate PHOTONICS' own §4
   construction.** That construction evaluates `r` as a genuine function of
   `θ_beam` (`r(90°−θ_beam)`, applied globally, at the swept beam angle
   itself) — a structurally different object from this pre-check's
   `r(theta_eff)`, a single STATIC angle fixed by geometry alone, with zero
   `θ_beam` dependence, applied to the *already-built, already-foreclosed*
   per-point-image family. This test asks a narrower, necessary-but-not-
   sufficient question: does the per-point angle DISTRIBUTION this family
   already contains collapse well onto one number? It cannot, by
   construction, test whether making `r` itself `θ_beam`-dependent (the
   actual structural change Attack 1 says is missing) produces a valid
   approximation of the true multi-point interaction — only PHOTONICS'
   own build, if this pre-check does not foreclose proceeding, can test
   that.
3. **The Fraunhofer criterion's numerical prefactor is a classical
   heuristic, not a unique constant.** Conventions in the literature range
   from `d_F=W²/λ` to `d_F=8W²/λ. This proposal fixes `d_F=W²/λ` (no
   factor), matching the exp-079 audit's own citation, and states the
   FORECLOSE/DOES-NOT-FORECLOSE thresholds as ratios against *that*
   definition, disclosed explicitly rather than silently adopted.
4. **Zero new FDTD; every physics primitive is inherited, not
   re-verified here.** `theta_local_deg`, `aperture_amplitude`,
   `dist_image_cells`, `source_driven_phase`, `reflection_coefficient_vec`
   are imported unchanged from `y_wall_aperture_sum.py`, already gated
   there (G-LOSSLESS/G-N1/G-PASSIVITY, and a bit-exact vectorized-vs-scalar
   validation, §[2b]). A bug in those primitives is inherited unchanged, not
   independently re-verified by this cycle.
5. **Comparison is against the already-committed native-grid (`oversample=1`)
   primary curves**, `y_wall_aperture_sum_results.json::primary_model_curves`
   — the SAME discretization exp-079's own Combined Verdict is scored at.
   Coarser/finer discretization is not re-tested here (exp-079's own §[4]
   convergence check already established the answer is stable to
   oversampling at the level this cycle relies on).
6. **A version-drift guard, not a re-verification of exp-079's own
   result.** `validity_precheck.py` recomputes the true per-point curve
   fresh from `ywas.echo_field_curve` and checks it against the committed
   JSON before scoring `R²` — this catches an accidental mismatch between
   the frozen record and the live function it imports, not a re-audit of
   exp-079's own Combined Verdict.

---

## 4. PRE-REGISTERED, falsifiable predictions (before any code beyond this
## file is written or run)

### (a) Fraunhofer/far-field margin + `theta_local` spread

**Thresholds, stated before computing anything:**

- **FORECLOSE** if, for ANY of the 5 congruent configs, either
  `dist_image(y_s)/d_F < 0.10` at either aperture edge, **or** the
  `theta_local` spread ratio `theta_local(y_lo)/theta_local(y_hi) > 1.5`.
  Rationale: `0.10` is an order of magnitude below the bare (unmultiplied)
  Fraunhofer distance — comfortably inside the classical near/Fresnel
  regime by any convention's prefactor; a `>1.5×` spread means one aperture
  edge sees an incidence angle at least 50% larger than the other, which
  already strains "one global angle" as a description on its face.
- **DOES-NOT-FORECLOSE** if, for ALL 5 configs, `dist_image(y_s)/d_F > 1.0`
  at both edges **and** the spread ratio `< 1.2` for all 5.
- **MARGINAL** otherwise.

**My prediction (stated before running `validity_precheck.py`): FORECLOSE.**
The exp-079 audit's own Red Team independently re-derived (its §0.7, from
the same raw `dg065.CONFIGS` this proposal also points to, not copied
verbatim into any number below) a `~113,101`-cell Fraunhofer distance
against `861–2347`-cell actual propagation distances (a `0.76%–2.08%`
margin) and a `5.27°–15.00°` (`~2.8×`) `theta_local` spread for C40. I have
not re-run that arithmetic myself yet — `validity_precheck.py` will — but I
expect it to reproduce closely (the geometry has not changed since exp-079)
and to land deep inside the FORECLOSE band on both sub-metrics, for every
one of the 5 congruent configs, not merely C40. **If `validity_precheck.py`
instead finds MARGINAL or DOES-NOT-FORECLOSE for any config, that is itself
a finding requiring explanation before Phase 3 (a geometry change since
exp-079, or an arithmetic disagreement with the audit's own independently-
verified figure) — not something to wave through.**

### (b) Single-angle reproduction of the full per-point envelope

**Metric:** `R²` (see §2) per config, `Re{E_echo}` PRIMARY proxy at
`theta_eff` PRIMARY (amplitude-weighted mean); `|E_echo|` and the
`theta_eff` SECONDARY (midpoint) definition reported as robustness
cross-checks, not as the scored verdict.

**Bands, stated before computing anything:**

- **SUPPORT**: mean `R²` (`Re`, `theta_eff` primary) across the 5 congruent
  configs `≥ 0.90`, AND no single config below `0.75`.
- **REFUTE**: mean `R² < 0.50`.
- **INCONCLUSIVE**: anything between (including "mean ≥0.90 but one config
  below the 0.75 floor").

**My prediction: SUPPORT, stated with real uncertainty disclosed rather than
hedged into vagueness.** Reasoning FOR: exp-079's own reflectance-ablation
control already showed that replacing the ENTIRE per-point
`r(theta_local(y_s))` weighting with a bare constant `1.0` (a strictly
MORE drastic simplification than replacing it with a single non-unit
`r(theta_eff)`) left the `PAIR_PAD`/`C80−C40` recovered periods
statistically indistinguishable from the full per-point model
(`|ΔP*| ≤ 0.023°`) — i.e. per-point angular variation in `r()` was already
shown to barely move these curves' dominant shape. A single-`theta_eff`
model is a strictly gentler simplification than that ablation (it keeps a
non-trivial, config-dependent, ABSORB-dependent complex scalar, just not a
`y_s`-varying one), so if total ablation to `r≡1` barely moved two of the
three deltas, a single-angle `r(theta_eff)` should track the true curve at
least as well. Reasoning AGAINST, disclosed honestly: this is in real
tension with part (a)'s own predicted FORECLOSE finding — a `2.8×`
`theta_local` spread is direct evidence that per-point angular variation is
NOT small relative to the aperture, and `MATERIALS`' own exp-079 Phase-5
finding that a second, realizable admittance family's `arg(r)` correlates
with the matched family at only `Pearson r=0.74–0.88` (not near-unity)
across this exact envelope shows `r(θ)` is not perfectly smooth either. If
the run instead lands INCONCLUSIVE or REFUTE, the informative reading is
that per-point angular variation matters MORE to this construction's own
curve SHAPE (not just its previously-tested pair-delta PERIOD) than the
ablation control alone revealed — a genuinely new finding either way, not a
failure of this pre-check.

**Whichever way (a) and (b) land, they answer different questions and both
get reported, not resolved into a single combined verdict**: (a) is a
first-principles physical-validity question (is a global-angle description
even a sound approximation of this geometry at all); (b) is an empirical
question about THIS ALREADY-FORECLOSED per-point-image family's own
numerical sensitivity to angular summarization. A FORECLOSE-(a) +
SUPPORT-(b) outcome would mean: the formal far-field criterion fails, but
this specific family's own curve shape happens not to care — informative
about this family, silent about PHOTONICS' own not-yet-built construction
(Idealization 2). A FORECLOSE-(a) + REFUTE-(b) outcome would mean the two
findings reinforce each other, strengthening the case that a global-angle
approximation is not sound for ANY y-wall construction at this bench
geometry, PHOTONICS' included.

---

## 5. What happens next, contingent on the actual numbers

- **If (a) is FORECLOSE and (b) is SUPPORT or INCONCLUSIVE**: build
  PHOTONICS' own §4 construction anyway (Red Team's own §3 ruling already
  anticipated this — the construction is "worth building regardless,"
  sequenced so the near-field caution is IN the record before the build,
  not discovered after it), pre-registering PHOTONICS' own feasibility-probe
  prediction (dominant period still T21-proximate; the informative result
  is the ABSORB-dependent offset) explicitly conditioned on this cycle's own
  disclosed near-field caveat.
- **If (a) is FORECLOSE and (b) is REFUTE**: report both findings plainly
  to Checkpoint criterion 2 bookkeeping — this would be the first
  quantitative evidence that NO single-global-angle y-wall reduction (not
  just this one) is likely to be a sound approximation at this bench's own
  aperture-to-wall geometry, a genuine (if partial) narrowing of the
  mechanism-class board, though not by itself a proof for the specific,
  differently-structured PHOTONICS construction.
- **If (a) is DOES-NOT-FORECLOSE or MARGINAL** (not the number I expect,
  but falsifiable and therefore possible): report the disagreement with the
  exp-079 audit's own independently-verified figure explicitly before
  proceeding to (b) at all.

No FDTD is run at any stage of this cycle. No RULED-OUT item (R1–R9) is
re-proposed or re-litigated.

---

## Compliance note

This document makes no `lab/` changes and does not modify `LOGBOOK.md`/
`PLAN.md`/`SESSION_LOG.md`/`lab/ARTIFACTS.md`/`lab/artifacts.py`/`AGENTS.md`.
Per house discipline, this file is committed and pushed BEFORE
`validity_precheck.py` is written or run.
