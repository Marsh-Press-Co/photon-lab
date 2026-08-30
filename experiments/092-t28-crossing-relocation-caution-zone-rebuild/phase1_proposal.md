# PHASE 1 — PROPOSAL · Panel Iteration 69 · exp-092 · Lead seat: ELECTROMAGNETISM

## "Crossing Relocation & Caution-Zone Rebuild" — a wider-net cpl=30 crossing search, two zero-FDTD caution-zone counterfactuals, and the sigma_max R3-rescale check extended to the PRIMARY channel, combined into one build (Reconciled Iteration-69 Ranks 1–3)

### 1. Design narrative — EM's own reasoning (≤300 words)

`delta_scene(θ) = C(G40,θ) − C(C40,θ)` is a Weber-contrast **difference**
between two independently passive, reciprocal, causal FDTD articles —
`PAD` is proven lossless vacuum (exp-076: the damping mask is a pure
function of `absorb`, never `nx`/`ny`/`pad`), so this channel is, by
construction, a coherent phase/timing signal, not an absorbed-power one.
That framing bounds what exp-091's own sign flip at 40.2° can and cannot
mean. Passivity forbids amplification (this bench's own P1/xi_ext/
non-negativity gates, re-verified clean at every cpl this program has
run, police exactly that) and reciprocity/causality are properties of the
continuous Maxwell system that the explicit leapfrog Yee update preserves
at *any* stable Courant fraction — none of that machinery cares what `cpl`
is. What resolution refinement *can* move, with zero passivity
implication, is the **accumulated propagation phase** across the
source-to-wall-to-observer path: numerical (Yee-grid) dispersion is an
`O((Δx/λ)²)` phase-velocity error, strictly a wave-propagation detail, not
a conservation law. A coherent interference null's *location* is exactly
the kind of quantity phase error moves; a null's mere *existence* is not
protected by anything passivity/reciprocity require. So a sign flip under
`cpl` 20→30 is fully consistent with — not evidence against — this
channel's own established bookkeeping, and is the expected signature of
genuine near-field structure (T10's own precedent: finer grids reveal
more of a feature coarser staircasing partially smooths), not a defect.

This cycle takes up exp-091's own Iteration-69 Tier-1 items 1–3
verbatim, run together as one build (Red Team's own exp-091 audit
recommendation): (1) locate the real `cpl=30` crossings with a net wide
enough to be justified by the cycle's own data, not a blind doubling;
(2) rebuild exp-090's caution zone under two counterfactual treatments,
zero FDTD; (3) test whether `graded_black_shell`'s unscaled `sigma_max`
contaminates the PRIMARY channel, not only `p_abs_w`.

### 2. Rank 1 — the wider-net crossing search

**2a. Physical argument for the net, not a blind ±0.4°/±0.6° doubling.**
Two independent, disclosed (non-conclusive) naive linear extrapolations
from exp-091's own already-collected `cpl=30` bracket pairs — reproduced
here from `results.json::a2.per_pair` before use, not re-derived by
hand — place the two crossings at:

| Crossing | `cpl=20` (exp-083, 31-pt census) | naive `cpl=30` linear extrapolation (from exp-091's own two-point brackets) | direction |
|---|---|---|---|
| lower | 40.2654° | ≈ **40.04°** | moved to **smaller** θ |
| upper | 41.4609° | ≈ **41.69°** | moved to **larger** θ |

Re-derived here directly from the two flanking `cpl=30` values each
bracket actually measured (`results.json::a2.per_pair` and
`raw.r3_leg2_cpl30_steps4200`/`raw.r3_leg4_cpl30_steps4200_bracket`):
slope over `[40.2°,40.4°]` = `(9.856×10⁻⁴ − 4.370×10⁻⁴)/0.2° =
2.743×10⁻³/°`; zero-crossing at `40.2° − 4.370×10⁻⁴/2.743×10⁻³ ≈ 40.04°`.
Slope over `[41.4°,41.6°]` = `(1.784×10⁻⁴ − 5.626×10⁻⁴)/0.2° =
−1.921×10⁻³/°`; zero-crossing at `41.4° + 5.626×10⁻⁴/1.921×10⁻³ ≈
41.69°`. **These move in *opposite* directions** — inconsistent with a
single rigid phase shift (which would translate both crossings the same
way) and consistent instead with the positive lobe between them
*widening*: span grows from `41.4609−40.2654=1.196°` (cpl=20) toward
roughly `41.69−40.04≈1.65°` (naive cpl=30 estimate), a ~38% widening —
the same direction as EM's own independently-reconfirmed finding
(`phase5_redteam_audit.md` §1.3) that `frac_contrast` inflates
**2.8×–5.2× at all three census angles**, not only the two
crossing-adjacent ones: an amplitude-side effect (a taller, wider lobe),
not a pure phase translation. This is the concrete, data-derived reason
the net below is **asymmetric and outward-biased**, not a symmetric
±0.4° pad.

**2b. The angle set — five new points, all on the existing `DENSE_ANGLES`
grid (house convention: grid-aligned angles give a free, exact `cpl=20`
comparator at every new point, already present in exp-083's committed
31-point census).**

| New angle | `DENSE_ANGLES` index | Purpose | Margin beyond naive estimate | `cpl=20` `delta_scene` (exp-083, sign) |
|---|---|---|---|---|
| 39.6° | `[18]` | lower net, far end | 0.44° below ≈40.04° | −1.636×10⁻³ (−) |
| 39.8° | `[19]` | lower net | 0.24° below | −1.213×10⁻³ (−) |
| 40.0° | `[20]` | lower net, near end | 0.04° below | −6.899×10⁻⁴ (−) |
| 41.8° | `[29]` | upper net, near end | 0.11° above ≈41.69° | −6.612×10⁻⁴ (−) |
| 42.0° | `[30]`, window edge | upper net, far end | 0.31° above | −8.030×10⁻⁴ (−) |

Combined with the four already-committed `cpl=30` points (40.2°, 40.4°,
41.4°, 41.6°, from exp-091's own Leg 2 + Leg 4), this gives two
continuous, 0.2°-step `cpl=30` windows: **{39.6°,39.8°,40.0°,40.2°,40.4°}**
(0.8° span) around the lower crossing and **{41.4°,41.6°,41.8°,42.0°}**
(0.6° span) around the upper crossing — both comfortably straddling the
naive-extrapolated locations with margin, using only points this
program's own dense census already treats as load-bearing.

**Disclosed limitation, not silently assumed away**: 42.0° is the literal
edge of `DENSE_ANGLES` (the window this whole T28-census sub-thread has
used since exp-069). If the upper crossing has moved past 42.0° — the
±5.2× amplitude inflation observed elsewhere makes this a live, if
lower-probability, possibility — this design cannot locate it, and would
require an off-grid extension explicitly out of scope this cycle (§7).
At `cpl=20`, `delta_scene(42.0°)=−8.03×10⁻⁴`, comfortably past the local
minimum near 39.4–39.6°'s own trend reversing toward zero again at the
window's far edge — i.e. 42.0° sits well inside the *next* negative
excursion, not near a second, unrelated crossing, which is some
reassurance the window edge is not itself ambiguous.

**2c. `sigma_max` for this leg: `0.5` (unscaled), matching exp-091's own
already-filed R3-leg convention exactly — deliberately NOT the corrected
value.** Reasoning: mixing sigma_max conventions *within* one
crossing-location curve would make the five new points and the four
already-committed points measure two different physical articles,
contaminating exactly the comparison this leg needs (a single
internally-consistent `cpl=30` curve to locate the crossing on). Rank 3
(§4) tests the sigma_max question as an independent, separately-reported
validity check on the *same* already-collected points, not folded into
the crossing search itself. If Rank 3 finds the confound material, that
finding applies retroactively to this leg's own points too, disclosed
explicitly forward (§7) as a second-order open question, not resolved
this cycle.

### 3. Rank 2 — the zero-FDTD caution-zone rebuild

**Treatment definitions, exact, reusing exp-090's own `Table 1` (n=7,
θ/margin/`ratio_k`/`Y`) and its own committed `find_zero_crossings`/
`firth_logistic`/`naive_mle_diverges`/`auc` implementations verbatim, no
new statistical machinery:**

- **(i) DROP** — remove the θ=41.4° row entirely; recompute on the
  remaining `n=6` rows: `zone_lo=max(margin|Y=1)`,
  `zone_hi=min(margin|Y=0)`, `AUC(margin)`, and Firth's fit
  (`X=[1,log10(margin)]`, `Y` as reduced) exactly as exp-090's own script
  computes them.
- **(ii) RELABEL** — keep all `n=7` rows; flip θ=41.4°'s own `Y` from 1
  to 0 (its own `cpl=30` reading, exp-091, reclassifies CONSISTENT); leave
  every other row, including its `margin`, untouched; recompute the same
  four quantities on the full `n=7` set with the one flipped label.

**Both are compared side by side against the original, unmodified `n=7`
zone `[1.4764,2.1709]`/Firth `m₅₀=2.071013`.** No new data, no new
threshold, no change to `FLOOR`/`FLOOR_FRAC`/`RATIO_HIGH` — a pure
counterfactual recomputation on already-committed numbers.

**I (EM) independently ran this exact recipe against the real house
functions, imported unmodified from `experiments/090-.../run.py`, before
proposing it — matching this program's own R4/R8 discipline (verify
before claim; an argued outcome is not a substitute for a computed one).
The numbers below are disclosed as my own pre-verification, to be
independently reproduced bit-exact by a committed Phase-4 script, not
copied from this document as a substitute for that reproduction:**

| Treatment | n | pos | AUC(margin) | zone `[lo,hi]` | inverted? | Firth converged | β | m₅₀ | m₅₀ inside zone? | naive MLE diverges? |
|---|---|---|---|---|---|---|---|---|---|---|
| ORIGINAL | 7 | 2 | 1.0000 | [1.4764, 2.1709] | No | Yes (20 it.) | [1.7806, −5.6315] | 2.071013 | Yes | Yes |
| (i) DROP 41.4° | 6 | 1 | 1.0000 | **[1.4764, 2.1709]** (unchanged) | No | Yes (29 it.) | [1.1798, −4.5447] | 1.818061 | Yes | Yes |
| (ii) RELABEL 41.4°→0 | 7 | 1 | **0.8333** | **[1.4764, 1.3095]** | **Yes** | Yes (24 it.) | [0.0385, −2.8425] | 1.031717 | No | **No** (converges) |

**Why the two treatments diverge so sharply — the mechanism, not just the
arithmetic.** Dropping 41.4° removes the *smaller*-margin of the two
`Y=1` points; since 40.2° (margin 1.4764) was already the tighter
(larger) of the two `Y=1` margins, the zone's own `zone_lo` is unchanged
by its removal — the zone is identical to three decimal places, only
Firth's `m₅₀` shifts (fewer data points, same qualitative fit). Relabeling
is a fundamentally different operation: 41.4°'s margin (1.3095) does not
disappear, it moves into the `Y=0` pool at a value *smaller* than 40.2°'s
own `Y=1` margin (1.4764) — the exact condition exp-090's own
pre-registered Q3 falsification clause names ("falsified if the computed
zone is... inverted"). A useful secondary fact this recomputation
surfaces: relabeling also breaks perfect rank separation outright
(AUC drops from 1.000 to 0.833) — the *naive*, unpenalized MLE, which
diverges under perfect separation in every other row of this table,
**converges** under relabeling, because 41.4° is now a genuine
counter-example to a monotone-in-margin decision rule, not merely a
smaller sample of the same separated pattern.

**Falsifiable check on this Rank (matching R4's committed-recomputation
discipline, not a physics hypothesis):** **CONFIRM** = Phase 4's
committed script reproduces every cell of the table above to at least
4 significant figures. **REFUTE** = any disagreement beyond that
tolerance — itself a genuinely important finding (either an
implementation subtlety this proposal missed, or an error in my own
pre-verification), to be investigated, not silently reconciled.

### 4. Rank 3 — the sigma_max R3-rescale check, extended to the PRIMARY channel

**Exact value: `sigma_max = 0.5 / R3_RATIO = 0.5 / 1.5 = 1/3 ≈
0.333333`.** Derivation: `graded_black_shell`'s native default
(`sigma_max=0.5`, unchanged since exp-024, used unscaled by every native
`build_article` call this program has ever run) combines with this
program's own `τ_center = 2·σ·r_out(cells)` optical-depth convention
(the T10/`SIGMA_ON` erratum mechanism, LIVE THREADS T10) to give
`τ_center(native) = 2×0.5×78 = 78` cells. `build_article_r3` (exp-091,
first-ever R3-resolution article-loaded FDTD call on this channel) left
`sigma_max` at its unscaled `0.5` default while `r_out` grew to `117`
cells (`R3_RATIO=1.5`), giving `τ_center(R3, as-filed) = 2×0.5×117 =
117` — a genuine **1.5× inflation** relative to the native reference,
not a resolution-equivalent replica. Holding `τ_center` fixed at the
native value of `78` at R3 resolution requires
`sigma_max_R3 = 78/(2×117) = 1/3`.

**Which configs/angles/legs it applies to — precisely, per Idealization
4's own "same physical article" requirement:**

- **Configs**: `C40_R3` and `G40_R3` (the same pair, no new geometry).
- **Angles**: all three census angles, **37.2°, 40.2°, 41.4°** — not
  merely the 2–4-call subset a narrower read of the Iteration-69 queue
  item might suggest. Including 37.2° (the CONSISTENT, non-crossing-
  adjacent control point) is deliberate: it is the one point in this
  cycle's own set where the sigma confound, if it moves `delta_scene`
  meaningfully, should show up as an ordinary, non-crossing-driven shift
  — a negative control that separates "sigma_max moves this channel
  generically" from "sigma_max only matters near a node," at a marginal
  cost of 2 extra calls over the cheapest possible 2-angle design (§4c
  below prices both).
- **Leg: ARTICLE ONLY (`with_article=True`).** The empty leg is **not**
  re-run.

**4a. Why empty-leg reuse is valid — verified from `lab/ambient.py` and
`run.py::_run_sim_r3`, not assumed.** `_run_sim_r3`'s own structure
(`if with_article: build_article_r3(...)`) means the empty-leg capture at
fixed `(cfg, θ, steps, cpl)` never calls `build_article_r3` at all — no
`materials.pec_disk`/`graded_black_shell` call of any kind touches that
`Sim` object. The empty-leg FDTD field is therefore bit-independent of
`sigma_max` by construction, not merely by argument: re-running it at a
different `sigma_max` would reproduce the identical field bit-for-bit
(same source, same domain, same `absorb`, same vacuum interior). Checked
against `lab/ambient.py::contrast_from_runs` next: for a fixed `(key,θ,
steps)` cell, `contrast_pair()` calls `amb.contrast_from_runs([scene_p],
[empty_p], ...)` with `scene_p` from the article-leg capture and
`empty_p` from the empty-leg capture of the *same* run — it does not
reach across configs or re-use another cell's empty capture, so there is
no cross-config coupling concern. Since `empty_p` for `(C40_R3,θ,4200)`/
`(G40_R3,θ,4200)` is unaffected by `sigma_max`, exp-091's own
already-committed empty-leg captures at these exact three angles
(`raw.r3_leg2_cpl30_steps4200`) may be reused directly, verbatim, with
zero new FDTD calls for that leg. **This is the correct application of
`contrast_from_runs`'s own convention, not an approximation of it.**

**4b. What gets recomputed with the new article-leg captures**: the
FULL result set this cycle's own headline rests on — `delta_scene(θ)`,
`frac_contrast(θ)`, `ratio_k(θ)` — using the *reused* empty-leg
`C_empty`/flank data paired with the *freshly captured*,
sigma-corrected article-leg `C`/scene data, at all three angles, both
configs. `p_abs_w`/`frac_p_abs` are also recomputed as a byproduct (same
pipeline), extending MATERIALS' own Phase-5 self-review (which checked
only this pair) to the channel it did not check.

**4c. Call count and cost**: 3 angles × 2 configs × 1 leg = **6 calls**
(`cpl=30`, `STEPS=4200`, matching Leg 2's settled convention exactly —
no new settling check needed, citing exp-091's own `(c1)/(c2)` clean
result at this identical `STEPS`/`cpl` combination, Idealization 3
below).

### 5. Full parameter table — geometry, `STEPS`, `cpl`, configs, leg-by-leg cost

All geometry, `R3_RATIO=1.5`, `R3_CONFIGS`, `DENSE_ANGLES` conventions
are unchanged, cited forward from `experiments/069-.../design_geometry.py`
and `experiments/091-.../run.py` (§2a's `build_article_r3`/`box_for_r3`/
`ref_for_r3`/`_run_sim_r3`) — reused verbatim, zero new `lab/` diff, zero
new geometry formula. `λ=600nm` throughout, matching every T28 cycle.

| Leg | Configs | Angles | `cpl` | `STEPS` | `sigma_max` | Calls |
|---|---|---|---|---|---|---|
| Rank 1 — wider net | `C40_R3`, `G40_R3` | 39.6°, 39.8°, 40.0°, 41.8°, 42.0° (5 new) | 30 | 4200 | 0.5 (unscaled, matches Leg 2) | 5×2×2=**20** |
| Rank 2 — zone rebuild | — (desk only) | — | — | — | — | **0** |
| Rank 3 — sigma check | `C40_R3`, `G40_R3` | 37.2°, 40.2°, 41.4° (article leg only) | 30 | 4200 | **1/3** | 3×2×1=**6** |
| **Total new FDTD** | | | | | | **26** |

**Cost (via `dg069._cost(key,steps,cell_ratio)` at `steps=4200,
cell_ratio=R3_RATIO²=2.25`, the identical formula/basis exp-091 §2.4
used, disclosed as an estimate not a measurement):**

`cost(C40_R3,4200,2.25) = 168.75` CPU-s/call; `cost(G40_R3,4200,2.25) =
234.9` CPU-s/call (both bit-identical to exp-091's own cited per-call
figures, since `C40_R3`/`G40_R3` are unmodified this cycle).

| Block | Calls | CPU-s | Basis |
|---|---|---|---|
| Rank 1 (5 new angles, both legs) | 20 | `5×2×(168.75+234.9)=4036.5` | |
| Rank 3 (3 angles, article leg only) | 6 | `3×(168.75+234.9)=1210.95` | |
| **Total** | **26** | **5247.45 CPU-s ≈ 87.5 CPU-min** | |

Wall time at `N_WORKERS=4, PARALLEL_EFFICIENCY=0.98, OVERHEAD_FACTOR=1.15`
(unchanged house constants, exp-091's own formula):
`wall_s = 1.15×5247.45/(4×0.98) ≈ 1539s ≈ 25.6 min`; 3× safety envelope
≈ 77 min — below exp-091's own 125.6 CPU-min/36.9 min-wall precedent,
inside every established T28 per-cycle FDTD budget.

**Unchanged from exp-091, applied without modification**:
`BOX_CLEARANCE_A_R3=18`, `BOX_CLEARANCE_B_R3=36`, `REF_HALF_H_R3=120`,
`XI_TOL=0.12`, `NOISE_MULT=3.0`, `RATIO_LOW/HIGH=0.1/10.0`,
`FLOOR_FRAC=0.10`, `FLOOR=1.91744×10⁻⁴` (Rank 1 applies this existing,
native-derived floor unrecomputed against the new points — the same
disclosed mixed-resolution comparison exp-091 Idealization 6 already
names; Rank 3 does the same for its own new points).

### 6. Falsifiable predicted outcomes

**Carried idealizations banner (mandatory at this section AND any future
Result section, per the Iteration-65 CHECKPOINT's own escalated,
non-discretionary rule): every prediction below is governed by
Idealizations 3/6/7 (§8): NETD is not a human-eye threshold; this cycle
does not test constraint 1/2/3/4 or re-open `REALIZABILITY_MEMO.md`;
`FLOOR` is applied, not recomputed, against the new points.**

**(R1a) PRIMARY — does the wider net locate a genuine sign change in
either window?** **CONFIRM** = a sign change detected within the
5-point lower window (39.6°–40.4°) AND/OR the 4-point upper window
(41.4°–42.0°), with the flanking same-signed points confirming a single
monotonic crossing (not an interior oscillation). **REFUTE** = no sign
change anywhere in either extended window — a further-widened,
off-grid net would then be required, a live, disclosed possible outcome,
not a formality (§2b's own edge-of-window caveat already names the risk
at the upper crossing specifically). **NEITHER** = a sign change is
found but the local curve is non-monotonic within the window (more than
one apparent crossing), reported as its own outcome, not forced into
CONFIRM.

**(R1b) diagnostic, not gating** — report the interpolated crossing
location(s) where found, against both the naive extrapolation
(≈40.04°/≈41.69°) and the native `cpl=20` location (40.2654°/41.4609°),
stating signed shift magnitude at each. No pre-registered tolerance band
— this is a location report, not a pass/fail test.

**(R1c) diagnostic, not gating** — `ratio_k`/floor-gate classification
at all 5 new angles, using the existing unrecomputed `FLOOR`/
`RATIO_HIGH=10`, falls out of the same pipeline at zero marginal cost;
reported as context (does a new floor-clearing ENERGY-DOMINANT node
appear near either relocated crossing?), not scored against any
falsifiable band this cycle.

**(R2) PRIMARY — Rank 2's own recomputation reproduces §3's table.**
**CONFIRM** = every cell reproduces to ≥4 significant figures.
**REFUTE** = any disagreement — see §3's own closing paragraph.

**(R3) PRIMARY — does the sigma-corrected article leg move
`delta_scene`/`frac_contrast`/`ratio_k` materially at any of the three
census angles?** Reusing the *same* `[0.3,3.0]` CONFIRM /
`[0.1,10]` REFUTE ratio-and-sign bands exp-091 §4(a) established for the
identical resolution-rescale question, applied here to
`{sigma-corrected value} / {as-filed exp-091 value}` at each of
`delta_scene` (sign + ratio) and `frac_contrast` (ratio) independently:
**CONFIRM** (negligible/small effect, exp-091's headline stands
unmodified) = ratio inside `[0.3,3.0]` and sign held at all three
angles, for both quantities. **REFUTE** (material contamination,
exp-091's own PRIMARY headline must be re-read as partly or wholly a
sigma-confound artifact) = a sign flip in `delta_scene` at any angle, or
either ratio outside `[0.1,10]`. **NEITHER** = ratio inside `[0.1,0.3)`
or `(3.0,10]`, sign held — a disclosed, non-trivial-but-inconclusive
shift, reported plainly. **No confident directional lean stated in
advance** — MATERIALS' own Phase-5 finding that the *bulk* `p_abs_w`
effect is small (~3.5%, consistent with an already near-saturated
absorber, T9's `σ_abs/σ_ext≈0.51` anchor) is informative but explicitly
does **not** license a prior on the *residual-reflection-phase* channel
`delta_scene` is built from — this is a genuinely open, two-sided
question, stated as such.

### 7. Explicitly out of scope this cycle, named forward

This cycle's own ~87.5 CPU-min / 26-call budget, combined with exp-091's
already-spent 125.6 CPU-min the same sub-thread used one cycle earlier,
keeps two consecutive T28 cycles inside the ~100–150 CPU-min band this
program has established as its own per-cycle norm — a reason, not an
excuse, for declining the following, all real and all ranked below Rank
1–3 in exp-091's own reconciled queue:

- **Tier 2 — a third `cpl=40` resolution point** (to distinguish
  converging from still-drifting). Explicitly deferred: this cycle's own
  Rank 1 result is a precondition for knowing WHERE a `cpl=40` check
  should even be centered (the crossing location is not yet known at
  `cpl=30`, let alone what a third point should target) — running it now
  would be premature, not merely lower-priority.
- **Tier 3 — extending R3 to the remaining four of exp-090's seven
  caution-zone points** (36.0°, 38.4°, 38.8°, 41.8° — note 41.8° is
  partially addressed as a side effect of this cycle's own Rank 1 net,
  though not at the full R3 settling-spot-check standard exp-091 applied
  to 40.2°/41.4°). Deferred as a distinct, lower-ranked item; not folded
  in silently.
- **Tier 4 — structural/governance items**: persisting
  `sigma_ext_cells`/`ratio_abs_ext_raw` into `results.json` going
  forward, and the print-parity/Result-section-existence structural
  safeguard named at exp-091's own Phase-5 audit §2/§6. Neither is
  FDTD-load-bearing to this cycle's own predictions; both remain named,
  open board items for whichever future cycle builds Iteration-69+'s own
  tooling improvements.
- Also untouched, standing, unaffected by this cycle (carried forward
  unchanged): PHOTONICS' own grazing-incidence validity check (still the
  single most-repeated item on the whole T28 board); the x-wall
  wavelength-generality leg (now well past sixteen consecutive cycles
  deferred); the still-queued R14(b) formal null-controlled period fit;
  the Rank-2-in-exp-090's-own-queue unbiased margin-vs-distance rebuild
  on the full 31-point window; the ritualization governance question
  (Iteration 61), still unresolved.

### 8. Idealizations (cited forward from exp-090/exp-091, not re-derived)

1. **2D TMz, single λ=600nm** — no chromatic sweep; the x-wall
   wavelength-generality leg remains separately queued, unchanged by
   this cycle (exp-091 Idealization 1).
2. **Single article pair, `C40`/`G40`** (`PAIR_PAD`) — no claim about
   `C60`/`C70`/`C80` proper (exp-091 Idealization 2).
3. **NETD is not a human-eye threshold.** Nothing here bears on
   constraint-3/4's human-eye verdict; `REALIZABILITY_MEMO.md` is not
   re-opened or re-scored (exp-091 Idealization 3).
4. **Bench scale only** — same ≈2.34µm physical radius at both native
   and R3 resolution (exp-091 Idealization 4, R3-scaling rule).
5. **`NOISE_MULT=3.0`, `FLOOR_FRAC=0.10`, `RATIO_LOW/HIGH=0.1/10.0`** —
   inherited house constants, unre-derived (exp-091 Idealization 5).
6. **`FLOOR`/`RMS[frac_contrast]` applied, not recomputed,** against the
   new points in both Rank 1 and Rank 3 — a disclosed mixed-resolution
   comparison, exactly as exp-091 §4d already discloses for its own
   points (exp-091 Idealization 6).
7. **This cycle does not test constraints 1/2/3/4 and takes no T1
   escape-route position** (§9 below; exp-091 Idealization 7).
8. **No settling re-check at the new angles/legs** — `STEPS=4200` at
   `cpl=30` is cited as already clean from exp-091's own `(c1)/(c2)`
   result at this identical `STEPS`/`cpl` pair; not independently
   re-verified at these specific new angles, on the reasoning that
   settling is a temporal/domain property, not source-angle-dependent,
   in this bench's own established convention. New this cycle.
9. **Rank 1's own crossing search is run at `sigma_max=0.5` (unscaled),
   not the corrected `1/3`** — a deliberate scope decision (§2c), not an
   oversight: if Rank 3 finds the sigma confound material, Rank 1's own
   located crossing(s) would need re-interpretation under the corrected
   article, explicitly flagged forward, not resolved this cycle. New
   this cycle.
10. **The five new Rank-1 angles and three Rank-3 angles were chosen for
    T28-census/crossing-bracketing relevance, not as a random or
    representative sample** of the dense window (exp-091 Idealization 9,
    same convention).

### 9. T1 escape route

**N/A**, stated plainly, matching every T28 desk/instrument cycle since
exp-069 (independently confirmed from LOGBOOK.md's own record, not taken
on the Director's word: every entry from Iteration 46/exp-069 through
Iteration 68/exp-091 states "T1 route N/A"/"Checkpoint criterion 2: N/A"
for this sub-thread). This cycle makes no phenomenon-mechanism proposal
and takes no position on σ(I)/σ(x,t)/angular selectivity/sub-threshold
operation. It is pure instrument recalibration of the AMBIENT channel's
own R13/R15 caution-zone machinery; Checkpoint criterion 2 is N/A, not
merely not-yet-ripe.

### 10. Confirming this design does not re-open ruled-out ground

No R1–R15 rule is violated or re-litigated. This is a direct execution
of R3's own meta-rule (resolution check before a mechanism debate) and
of R15's own founding text (a calibration boundary built from points
whose classification depends on proximity to a resolution-sensitive node
must have that sensitivity independently R3-verified before being
trusted — exactly what Rank 1/Rank 3 together attempt to complete, and
what Rank 2 reports the consequence of, on the existing data, without
waiting on it). R13's floor gate and R14's numerator-distrust rule are
applied unchanged throughout (§5, §6). No new numbered rule is proposed.
