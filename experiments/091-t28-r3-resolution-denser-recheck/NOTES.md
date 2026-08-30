# exp-091 — T28 R3 Resolution & Denser Recheck

*Panel Iteration 68. Lead seat: MATERIALS & METAMATERIALS. Runner:
photonlab-shift (cloud panel routine).*

## Hypothesis

The T28 caution-zone/floor-gate machinery (exp-087–090) rests entirely on
one never-varied grid resolution (`cpl=20`, 600nm) for the C40/G40
`PAIR_PAD` ambient channel (`delta_scene`, `frac_contrast`, `ratio_k`).
This is a direct, program-standing R3 violation left undischarged for
three cycles (MATERIALS flagged it at exp-088, exp-089, exp-090's own
Phase-2/5 reviews) and specifically load-bearing at 40.2°/41.4° — the two
angles that set the caution zone's own lower edge, each sitting a fraction
of a degree from a real `delta_scene` zero-crossing. **Hypothesis: the
`cpl=20` values reported for `delta_scene`/`frac_contrast`/`ratio_k` at
these three census angles are resolution-stable within this program's own
established survival tolerance — but this is a genuinely two-sided
question at 40.2°/41.4°, not a formality**, since both angles sit closer
(relative to their own signal size) to a zero-crossing than anything this
program's R3 machinery has ever certified before.

This cycle makes **no phenomenon-mechanism claim** — T1 escape route N/A,
Checkpoint criterion 2 N/A, matching every T28 desk/instrument cycle since
exp-069. It is pure instrument recalibration: does the measurement survive
a finer grid, and does the `R3_STEPS=4200` settling convention (adopted by
scaling argument since exp-069, never independently verified) actually
hold at the two hardest points in this cycle's own sample?

## Setup

**Channel:** `PAIR_KEYS=("C40","G40")` at native `cpl=20`; `PAIR_KEYS_R3=
("C40_R3","G40_R3")` at `cpl=30` (`R3_RATIO=1.5`, `experiments/069-t21-
block-mini-period-match-power-up/design_geometry.py`). λ=600nm throughout.
`C40_R3` already exists in `R3_CONFIGS` (`r3_config(60,0)`, the correct R3
scaling of native `C40=config(40,0)`). **`G40_R3 = r3_config(60,60)`** is
the one new config this cycle adds — the R3 scaling of native
`G40=config(40,40)` (`absorb` 40→60, `pad` 40→60, both `round(×1.5)`),
verified by both MATERIALS (phase1_proposal.md §2a) and Red Team
(phase2_redteam_audit.md §0) to produce a cell footprint (`nx=660,
ny=2496`) bit-identical to the already-existing `C80_R3`, and an aperture
`A` that automatically satisfies the file's existing three-way congruence
assertion (`A` is `pad`-independent by `r3_config()`'s own construction).

**Four measurement legs, 40 FDTD calls total** (all frozen before any
Phase-4 code exists — see Phase-3 synthesis §1 for the full ten-item
mandatory-fix disposition this design incorporates):

| Leg | Config(s) | Angles | `cpl` | `STEPS` | Calls |
|---|---|---|---|---|---|
| 1 — native-`cpl` repeat | C40, G40 | 37.2°, 40.2°, 41.4° | 20 | 4200 | 12 |
| 2 — R3 leg | C40_R3, G40_R3 | 37.2°, 40.2°, 41.4° | 30 | 4200 | 12 |
| 3 — R3 settling spot-check | C40_R3, G40_R3 | **40.2°, 41.4° (both)** | 30 | 6300 | 8 |
| 4 — bracket (new, EM's fix) | C40_R3, G40_R3 | **40.4°, 41.6° (new)** | 30 | 4200 | 8 |

Each cell above is 2 calls (empty + article legs). Leg 3 spot-checks
**both** 40.2° and 41.4° — not 40.2° alone as first proposed — because the
proposal's own §2b table shows **41.4° is actually the thinner-margin
(1.3095× vs. 1.4764×) and more crossing-proximate (0.061° vs. 0.065°)
angle**, the reverse of the first-drafted "40.2° is hardest" premise
(QUANTUM's Phase-2 attack, independently re-derived and upheld by Red
Team). Leg 4's two new angles, 40.4° and 41.6°, are exact, existing
`DENSE_ANGLES` grid members (`DENSE_ANGLES[i]=39.0+i×0.2`, `i=7` and
`i=13`) chosen specifically to **bracket** the known `cpl=20` zero-crossings
(40.265° and 41.461°) from the far side of each — 40.2°+40.4° straddle
40.265°; 41.4°+41.6° straddle 41.461° — enabling a direct linear
interpolation of the `cpl=30` crossing location, and giving a free exact
`cpl=20` comparator at 40.4°/41.6° too (both already exist in exp-083's
committed 31-point census).

**Cost** (hand-derived from `dg069._cost()`, disclosed as an estimate, not
a measurement): 7534.9 CPU-s ≈ 125.6 CPU-min; wall ≈ 36.9 min at 4 workers;
3× safety envelope ≈ 111 min.

**Applied unchanged:** `XI_TOL=0.12`, `NOISE_MULT=3.0`,
`RATIO_LOW/HIGH=0.1/10.0`, `FLOOR_FRAC=0.10`, `FLOOR=1.91744×10⁻⁴`
(this cycle applies the *existing*, native-`cpl` `FLOOR` against new
`cpl=30` numbers — a disclosed mixed-resolution comparison, Idealization
6), `BOX_CLEARANCE_A/B`, `REF_HALF_H` R3-scaled by the same `R3_RATIO`.

## Predictions (frozen, committed BEFORE any Phase-4 script runs)

**Carried idealizations banner (mandatory at both this section and the
future Result section, per the Iteration-65 CHECKPOINT's escalated,
non-discretionary rule):** every prediction below is governed by
**Idealizations 3/6/7** (§ below): NETD is not a human-eye threshold; this
cycle does not test constraint 1/2/3/4 or re-open `REALIZABILITY_MEMO.md`;
`FLOOR`/`RMS[frac_contrast]` remain applied, not recomputed, against newly
`cpl=30`-measured numbers (a disclosed mixed-resolution comparison).

**(a) PRIMARY — does `frac_contrast`/`delta_scene` survive `cpl` 20→30 at
all three census angles (37.2°/40.2°/41.4°)?** Reusing exp-069's own
pre-registered P-069-5 band: **CONFIRM** = ratio
`frac_contrast_R3(θ)/frac_contrast_cpl20(θ) ∈ [0.3,3.0]` AND same sign of
`delta_scene(θ)`, at all three angles. **REFUTE** = a sign flip at any
angle, or a ratio outside `[0.1,10]`. Ratio inside `[0.1,0.3)` or
`(3.0,10]` (sign held) reported as its own disclosed NEITHER outcome. A
genuinely two-sided test: 40.2°/41.4° sit closer to a crossing (relative to
their own signal) than any point this channel's R3 check has certified
before.

**(a2) PHOTONICS' location-sensitive companion test (zero marginal cost,
Phase-2 mandatory fix 3+4).** Using the bracket leg's own two point-pairs —
(40.2°,40.4°) and (41.4°,41.6°) at `cpl=30` — linearly interpolate each
pair's `delta_scene=0` crossing angle and compare against the known
`cpl=20` crossings (40.265°, 41.461°). **CONFIRM** (crossing stable) =
shift `≤0.1°` (half the 0.2° grid step) at both crossings. **REFUTE** =
shift `>0.1°` at either. This is the direct test of whether (a)'s magnitude
survival could mask a moved crossing, exactly the gap PHOTONICS' and EM's
Phase-2 attacks (both upheld) identified.

**(b) PRIMARY — does the `ratio_k` classification (CONSISTENT /
ENERGY-DOMINANT) match between `cpl=20` and `cpl=30`, applying the
existing, unrecomputed `FLOOR`/`RATIO_HIGH=10`?** **37.2° — predicted
PRESERVED (CONSISTENT), moderate-high confidence** (`ratio_k=3.44`,
comfortably mid-band, most crossing-distant of the three). **40.2°/41.4° —
no confident lean, stated plainly:** both read `cpl=20` ENERGY-DOMINANT at
`ratio_k≈25–29`; a full pass of (a)'s own CONFIRM band (a 3× downward
`frac_contrast` shift) is, by itself, arithmetically sufficient to pull
either `ratio_k` below `RATIO_HIGH=10`. **A CONFIRM on (a) does NOT imply a
hold on (b)** — pre-registered as logically separable, any of
hold/hold, hold/flip, flip/flip treated as equally informative. Per
QUANTUM's Phase-2 secondary observation (upheld, wording precisioned by
Red Team): the one available historical precedent for this exact
resolution-ratio (exp-069's own `[1.97×,2.50×]`) sits just *below* both
this cycle's own flip thresholds (`>2.508` at 40.2°, `>2.881` at 41.4°) —
**a close, live possibility this design's own two-sided framing already
anticipates, not the expected case.**

**(b2) PRIMARY — THERMODYNAMICS' co-equal numerator check (zero marginal
cost, Phase-2 mandatory fix 5).** Does `frac_p_abs(θ)` — `ratio_k`'s
numerator, and R14's own named hazard — separately survive `cpl` 20→30 at
all three census angles? Same bands as (a): **CONFIRM** = ratio
`frac_p_abs_R3(θ)/frac_p_abs_cpl20(θ) ∈ [0.3,3.0]`, same sign of
`p_abs_w(G40,θ)−p_abs_w(C40,θ)`. **REFUTE** = sign flip or ratio outside
`[0.1,10]`. (a) and (b2) are independent, both load-bearing to (b)'s
classification question — a CONFIRM on one does not license skipping the
other (THERMODYNAMICS' upheld attack: prior draft tested only the
denominator).

**(c) Settling-adequacy, two independent legs, run at BOTH angles per the
corrected "which angle is hardest" premise (item 1/2 of the mandatory-fix
docket):**
- **(c1) Native-`cpl` reproducibility.** `C_empty(C40/G40, θ, STEPS=4200,
  cpl=20)` predicted to reproduce exp-083's own `STEPS=2800` value at all 3
  angles within **≤1% relative** (CONFIRM) / **≥5%** (REFUTE), all 6 cells.
- **(c2) R3-resolution settling, both angles.** `C40_R3`/`G40_R3` at
  `STEPS=6300` predicted to reproduce their own `STEPS=4200` values within
  **≤1% relative** (CONFIRM) / **≥5%** (REFUTE), at **both** 40.2° and
  41.4°, both legs. A REFUTE at either would mean `R3_STEPS=4200` has been
  silently under-settled at `cpl=30` in every cycle using it since exp-069
  — a program-wide finding, independent of which angle it appears at.
- **Cross-reference (mandatory fix 10):** the Result write-up must state
  whether (a2)'s bracket-derived crossing-shift finding is directionally
  consistent with which of the two spot-checked angles shows the larger
  settling residual — reported together, not as two independent findings.

**(d) Disclosed, non-gating:**
- **Operationalized "felt-lucky" relief claim (mandatory fix 8).** Compute
  the 37.2° `resolved`-gate noise-floor margin
  (`|Δp_abs|/(NOISE_MULT·box_dev_max·p_abs(C40))`) at `STEPS=4200` using
  Leg 1's own data, and report it directly against the cited `STEPS=2800`
  figure of `1.046×` — not merely asserted as "relieved."
- **R14(a)-style parent-quantity check, 3(+2 bracket)-point, necessarily
  weaker than exp-089's 8-point version.** `p_abs_w` predicted smooth
  across the R3-leg's angles, consistent in direction with the native
  trend.
- **Ordering check.** `frac_contrast(37.2°)>frac_contrast(40.2°)>
  frac_contrast(41.4°)`, true at `cpl=20`, predicted preserved at `cpl=30`.
- **Perceptual-threshold check (mandatory fix 7, pre-computed by Red Team,
  independently re-verified in Phase 3 synthesis §2.4):** the `[0.3,3.0]`/
  `[0.1,10]` band's edges, in absolute `delta_scene` units, sit **7.0–12.5×
  (CONFIRM edge) / 2.1–3.7× (REFUTE edge) below `C_THR_BASE=0.005`**
  (Blackwell 1946 / Rose 1948 / CIE 19/2 / Adrian 1989, `lab/
  glare_sidecar.py`) at all three census angles — the reused tolerance
  does not risk swallowing the one pinned perceptual threshold this
  instrument exists to police, though it comes closest (within ~2.1×) at
  37.2° under the REFUTE, not CONFIRM, outcome. Disclosure only — this
  cycle does not test constraint 3 (Idealization 3/7).
- **`FLOOR` itself remains unverified at `cpl=30`** (Idealization 6) — this
  cycle does not attempt the ~124-call full 31-point R3 rebuild that would
  discharge that separately, named forward, out of scope.

## Idealizations

1. **2D TMz, single λ=600nm** — no chromatic sweep; the x-wall
   wavelength-generality leg remains separately queued (now well past
   fifteen consecutive cycles deferred, unchanged by this cycle).
2. **Single article pair, `C40`/`G40`** — the `PAIR_PAD` construction this
   T28 sub-thread is built on; no claim about `C60`/`C70`/`C80` proper.
3. **NETD is not a human-eye threshold.** Nothing here bears on
   constraint-3/4's human-eye verdict; `REALIZABILITY_MEMO.md` is not
   re-opened or re-scored.
4. **Bench scale only** (`r_out=78` cells native / `117` cells at R3, same
   ≈2.34µm physical radius) — no witness-scale claim.
5. **`NOISE_MULT=3.0`, `FLOOR_FRAC=0.10`, `RATIO_LOW/HIGH=0.1/10.0`** are
   inherited house constants, unchanged and unre-derived here.
6. **`FLOOR`/`RMS[frac_contrast]` are applied, not recomputed,** against
   the new `cpl=30` numbers — a disclosed mixed-resolution comparison.
   This cycle discharges the resolution question for `frac_contrast`/
   `delta_scene`/`frac_p_abs`/`ratio_k`'s own *reported values*; it does
   not discharge whether `FLOOR` itself, as a threshold, is
   resolution-invariant.
7. **This cycle does not test constraints 1/2/3/4 and takes no T1
   escape-route position.**
8. **No full R3-rescaled rebuild of exp-083's 31-point window**, and no
   extension of R14(b)'s still-queued formal null-controlled period fit —
   both remain open, separate, standing T28 items.
9. **The five `cpl=30` angles (37.2°/40.2°/40.4°/41.4°/41.6°) were chosen
   for T28-census/crossing-bracketing relevance, not as a random or
   representative sample** of the 31-point window.
10. **The settling spot-check (c2) now runs at both 40.2° and 41.4°** — the
    original draft named 40.2° alone as "the hardest case," which the
    proposal's own margin/crossing-distance numbers contradict (41.4° is
    thinner-margin and more crossing-proximate on both metrics). Both
    angles are checked; no claim that either alone would have sufficed.

Corrects `phase1_proposal.md`'s own Idealization 10 and §4c2, whose stated
premise ("40.2° is the hardest case") is superseded here per the
mandatory-fix docket (Phase-3 synthesis §1, items 1–2) — the original
document is left as-filed, not retroactively edited, per house convention.
