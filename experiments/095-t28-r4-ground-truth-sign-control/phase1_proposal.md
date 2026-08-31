# exp-095 — R4 Ground-Truth Sign Control, cpl=50 Third Resolution Point, sigma/38.4° Comparability Closes

*Panel Iteration 72. Lead seat (rotation): VISION SCIENCE. Phase 1 proposal
only — no `run.py`, no FDTD calls executed by this document. Executes Red
Team's own Reconciled Iteration-72 queue items 1–4 (`experiments/094-t28-
cpl40-resolution-sigma-r3-census/phase5_redteam_audit.md` §7, LOGBOOK.md
Iteration 71) as one combined, internally-gated build, matching this
sub-thread's own established pattern (exp-091/092/093/094 each combined a
reconciled queue into a single Phase-1 proposal).*

## Standing-rule compliance header (checked against R1–R16; Red Team will
## check this line by line)

- **R1–R2, R5, R7, R10** — not engaged: this cycle fits no carrier/phase
  parameter, searches no named-constant space, prices no un-fit design, and
  claims no mechanism (T1 route N/A throughout, see below).
- **R3** (resolution-check meta-rule) — this entire proposal exists to
  extend R3 checks to a fourth grid density; complied with directly.
- **R4/R9** (recompute-don't-hand-type; commensurability) — every existing
  figure cited below (the `cpl=20`/`cpl=30` `delta_scene` comparators at
  39.2°/39.8°, `SIGMA_R4_CORRECTED`, exp-094's own Rank-3 38.4° reading) was
  retrieved this session by directly reading the committed `results.json`
  files, not hand-typed from memory or a prior prose citation. Exact
  provenance is cited per figure in §4.
- **R6/R8** — not engaged directly, but this proposal's own central move
  (Rank 1) is the generalized-R6 discipline R15's own Iteration-71 addendum
  demands: a synthetic/ground-truth-style recovery check on the new `R4`
  family, at a point where the correct answer is already independently
  known, run BEFORE any further `R4`-family spend — not an unverified
  robustness argument standing in for a check.
- **R11/R12** — not engaged: no `free_period_with_widening` search; no
  seed-dependent statistic.
- **R13** (denominator floor gate) — applied unchanged: `floor_pass` is
  computed via the existing, unmodified `compute_floor()`/`FLOOR` at every
  new angle/resolution. A point failing it is reported `NODE-UNRESOLVABLE`,
  never silently scored, including inside the Rank-1 gate itself (see §4).
- **R14** (numerator subtractive-cancellation caution) — `frac_p_abs`/
  `p_abs_w` reported informationally only throughout, never PRIMARY,
  matching standing treatment since exp-088.
- **R15 / its Iteration-71 addendum** (the rule this cycle exists to
  advance) — this proposal is the addendum's own named minimum-discharge
  package: a far-from-null ground-truth control on the `R4` family (Rank 1)
  BEFORE a third, differently-ratioed resolution point (Rank 2) is trusted.
  Explicit: this cycle does not by itself close R15 on this channel — a
  `cpl=50` reading, even if internally consistent, remains one more sample
  of a shared construction recipe (Idealization 17, exp-094, carried
  forward unchanged below), not an independent re-derivation of the
  underlying discretization scheme.
- **R16** (NETD byproduct must be persisted, not merely disclaimed) —
  every Rank below that calls a `_full`-style metrics path retrofits
  `netd_row()` into its own report dict at Phase-4 write time, from the
  first draft — not added post-audit as exp-094's own cycle needed to.

## 1. Mechanism/instrument narrative (≤300 words)

Pure instrument recalibration — no phenomenon-mechanism claim, no new
material law, no position on T1's escape routes. exp-094 (Iteration 71)
found that its new `cpl=40` (`R4`) congruent-geometry family reverses, in
both sign and classification, exp-093's `cpl=30` SINGLE-NULL reading at
*all six* interior near-null points (41.750°–41.900°) — R15's own founding
concern, realized on R15's own founding sub-thread one cycle after the
verdict it exists to stress-test. Red Team's Phase-5 final audit named the
minimum discharge: a ground-truth sign-recovery control on `R4` at a
point where the answer is already known, before trusting any further
`R4`-family spend (Rank 1); only then a third, differently-ratioed
resolution point (`cpl=50`, Rank 2, gated on Rank 1). Two further gaps are
closed unconditionally: the sigma-comparability chain at both edges of the
41.6°–42.0° window (Rank 3 — itself `R4`-family spend, and therefore also
gated on Rank 1, a scope extension beyond Red Team's literal text,
justified in §2); and 38.4° re-measured at corrected sigma (Rank 4, the
`R3` family, already independently validated across four prior cycles, run
unconditionally).

Rank 1 is deliberately the cheapest, fastest item and runs first: it is a
pure precondition, not a scientific result in its own right, and its
entire purpose is to decide — before another CPU-hour is spent on `R4`- or
`R5`-family geometry — whether this cycle's own most expensive item
(Rank 2, a brand-new `cpl=50` family) is worth building at all. If Rank 1
fails, this cycle stops at 10 calls with an integrity finding, not 60.

## 2. Sequencing and the go/no-go gate (stated before any run)

**Order: Rank 1 → Rank 4 (independent, may run alongside/after) → Rank 2 +
Rank 3 (both gated on Rank 1's verdict).**

**Judgment call, stated and justified:** Red Team's own ranked item 1 says
the ground-truth control gates "any further `R4`-family spend this cycle,"
not merely the `cpl=50` item named next in its own list. Rank 3(a) (41.6°
at `cpl=40`) and Rank 3(b) (the interior six points at `cpl=40` *native*
sigma) are new `R4`-family FDTD calls in the most direct sense — same
family, same grid density, filling gaps in the same window Rank 1a/1b
already measured. It would be inconsistent to gate Rank 2 (a different,
`cpl=50` family) on Rank 1 while spending un-gated `R4`-family calls under
a different name. **Rank 3 is therefore gated on Rank 1 too.** Rank 4 uses
only the `R3` (`cpl=30`) family, independently ground-truth-validated
across exp-091/092/093/094's own four prior cycles — it carries none of
Rank 1's risk and runs unconditionally, the cheapest-and-independent-first
item.

**The exact go/no-go criterion (Rank 1), committed before any FDTD call:**

Two already-robust, far-from-null angles are tested: **39.2°** and
**39.8°**. Both were considered by Red Team (alongside 37.2°); 37.2° is
excluded here by name — it is this sub-thread's own repeatedly-flagged
"felt-lucky" thinnest-margin point (`ratio_k`=3.443/margin=2.17× at
`cpl=20`, degrading to a bare 1.046× floor-margin at `cpl=30`, exp-091) —
a poor choice for a control whose entire value depends on there being *no
ambiguity* about the correct answer. 39.2°/39.8° have no such history.

Already-filed comparator values (retrieved this session, not hand-typed):

| θ | `delta_scene` @ `cpl=20` (exp-083 `results.json`, `thetas`/`delta_scene` arrays) | `delta_scene` @ `cpl=30` (exp-092 `results.json::rank1.per_theta`) | `ratio_k`@30 | `floor_pass`@30 |
|---|---|---|---|---|
| 39.2° | −1.8292×10⁻³ | −2.4921×10⁻³ | 0.9197 | True |
| 39.8° | −1.2131×10⁻³ | −9.7931×10⁻⁴ | 3.8410 | True |

Both angles: **negative** sign, consistent across the two already-measured
resolutions, `ratio_k`<10 (CONSISTENT class), comfortably floor-clearing —
an unambiguous "known-correct answer" at both points.

- **PASS (go — Rank 2 and Rank 3 proceed):** `delta_scene` computed from
  the new `R4` (`cpl=40`) family reads **negative** at *both* 39.2° and
  39.8°, `floor_pass=True` at both.
- **FAIL (no-go — skip Rank 2's 32 calls and Rank 3's 18 calls; HALT
  before spending them):** `delta_scene(R4)` reads **positive** (wrong
  sign) at *either* angle, with `floor_pass=True` there (a floor-cleared
  wrong sign is unambiguous, not a measurement-noise artifact). On FAIL,
  this cycle still writes `results.json`/`NOTES.md` reporting Rank 1's own
  numbers and Rank 4's independent result, and names the finding an
  R4-family registration-defect candidate for Phase 2/5 to investigate —
  not silently absorbed, and explicitly flagged as Checkpoint-4-relevant
  if any of exp-094's own citations turn out to rest on it.
- **AMBIGUOUS (treated conservatively as a soft FAIL — HALT, but not
  scored a "wrong sign"):** `floor_pass=False` at either angle at `cpl=40`
  (i.e., a point independently known to sit far from any null at two
  coarser resolutions becomes NODE-UNRESOLVABLE at `cpl=40`). Given the
  ~10⁻³-scale comparators above sit roughly an order of magnitude above
  `FLOOR` (§4), this is not expected, but if it occurs it is itself a
  significant, disclosed surprise, not smoothed into a directional verdict
  either way.

Only the **sign** is gating, per Red Team's own stated criterion. A
magnitude comparison (`delta_scene(R4)/delta_scene(R3)` at each angle) is
reported **informationally only** — expected order-of-magnitude stable
(loosely, ratio inside [0.2, 5]) but not scored, to avoid re-importing the
R13/R14-style over-interpretation of a magnitude ratio this program's own
rules exist to guard against, applied here to a quantity that is (by
construction) far from any null.

## 3. Parameter table

**Wavelength:** 600 nm throughout (this sub-thread's standard since
exp-069). **Channel:** `PAIR_KEYS_R4=("C40_R4","G40_R4")` (Rank 1, Rank
3(b)'s native-sigma interior points, all reusing exp-094's own committed
`R4_CONFIGS`/`box_for_r4`/`ref_for_r4`/`build_article_r4_sigma`/
`_run_sim_r4_sigma`/`cell_metrics_r4`/`run_block_r4` verbatim — zero diff
to `experiments/094-.../run.py`); a genuinely new `PAIR_KEYS_R5=
("C40_R5","G40_R5")` family (Rank 2) additively appended to
`experiments/069-t21-block-mini-period-match-power-up/design_geometry.py`,
mechanically substituting `R5_RATIO=2.5` for `R4_RATIO=2.0` into the
already-committed `r4_config()` recipe (itself already a mechanical
substitution into `r3_config()`) — zero diff to any existing constant;
`PAIR_KEYS_R3=("C40_R3","G40_R3")` (Rank 3(a)'s corrected-sigma leg, Rank
4) reusing `experiments/091–094`'s own committed `R3_CONFIGS`/
`build_article_r3_sigma` verbatim.

**cpl=50 (`R5`) vs. cpl=45 — the choice, justified.** Red Team's own text
offered `cpl=50` or, "per MATERIALS' own non-clean-multiple suggestion,"
`cpl=45`. Computed both mechanically through the existing recipe before
choosing: at `R5_RATIO=2.25` (cpl=45), `R_OUT` rescales to
`round(78×2.25)=176`, but `78×2.25=175.5` exactly — a genuine half-cell
rounding on the one constant this program's own mandatory Gate 3
(bit-identical physical shell radius, `L_GEOMETRIC_M`, across every
resolution family) is built to police, producing
`L_GEOMETRIC_M≈2.3467×10⁻⁶` m vs. the native/`R3`/`R4` value of
`2.3400×10⁻⁶` m exactly — a ~0.28% radius drift that would **fail** Gate 3
as every prior cycle has stated it, for no compensating benefit: MATERIALS'
own underlying worry (that `R4_RATIO=2.0` was suspiciously exact — *zero*
rounding anywhere in its own constants table) is not actually fixed by
`cpl=45`, since both `cpl=45` and `cpl=50` use the *identical* mechanical
`r{n}_config()` recipe (Idealization 17's own disclosed limitation applies
equally to either choice). **`cpl=50` (`R5_RATIO=2.5`) is chosen**: `R_OUT`
scales exactly (`78×2.5=195`, integer, Gate 3 holds bit-exact), while two
of the twelve derived constants (`PLANE_X`: `77×2.5=192.5→192`;
`GUARD_OUT`: `185×2.5=462.5→462`) still pick up genuine half-cell rounding
— the *same* rounding profile `R3_RATIO=1.5` already has at exactly these
two constants (`PLANE_X` 77×1.5=115.5→116; `GUARD_OUT` 185×1.5=277.5→278)
— which already answers MATERIALS' concern (this is not another
zero-rounding `R4`-style family) without opening a new, avoidable Gate-3
failure.

**New geometry constants** (append to `design_geometry.py`, mirroring the
`R4` block's own inline-derivation-comment convention):

| Constant | Formula | Value |
|---|---|---|
| `R5_RATIO` | `50/20` | `2.5` |
| `R5_CPL` | `{600: 50}` | — |
| `R5_BASE_NX` | `round(360×2.5)` | `900` |
| `R5_BASE_NY` | `round(1584×2.5)` | `3960` |
| `R5_BASE_ABSORB` | `round(40×2.5)` | `100` |
| `R5_BASE_OBJ_Y` | `R5_BASE_NY // 2` (mirrors `R4_BASE_OBJ_Y`'s own corrected derivation, exp-094 Phase-4 disclosed-resolution note — absorb subtracted exactly once, later, via `y_lo` inside `r5_config()`) | `1980` |
| `R5_BASE_SRC_X` | `round(300×2.5)` | `750` |
| `R5_BASE_PLANE_X` | `round(77×2.5)` | `192` |
| `R5_BASE_OBJ_X` | `round(170×2.5)` | `425` |
| `R5_TAPER` | `round(40×2.5)` | `100` |
| `R5_R_OUT` | `round(78×2.5)` | `195` |
| `R5_W_OBJ` | `round(78×2.5)` | `195` |
| `R5_GUARD_OUT` | `round(185×2.5)` | `462` |
| `R5_W_FLANK` | `round(78×2.5)` | `195` |
| `R5_STEPS` | `round(2800×2.5)` | `7000` |
| `R5_STEPS_STRESS` | `round(R5_STEPS×1.5)` | `10500` |
| `PEC_R_R5` | `round(30×2.5)` | `75` |
| `BOX_CLEARANCE_A_R5` | `round(12×2.5)` | `30` |
| `BOX_CLEARANCE_B_R5` | `round(24×2.5)` | `60` |
| `REF_HALF_H_R5` | `round(80×2.5)` | `200` |
| `SIGMA_R5_CORRECTED` | `SIGMA_NATIVE/2.5` (EM's Iteration-71-established first-principles derivation, applied at a third ratio) | `0.2` |
| `DX_M_R5` | `600e-9/50` | `1.2×10⁻⁸` m |
| `L_GEOMETRIC_M_R5` | `R5_R_OUT×DX_M_R5` | `2.34×10⁻⁶` m (bit-identical to native/`R3`/`R4`) |

`r5_config(absorb, pad)` — line-for-line mirror of `r4_config()`, R5
constants substituted. `R5_CONFIGS = {"C40_R5": r5_config(100, 0),
"G40_R5": r5_config(100, 100)}`. Congruent-construction check: both give
`A = obj_y − y_lo = round(752×2.5) = 1880` (verified: `C40_R5`:
`1980−100=1880`; `G40_R5`: `2080−200=1880`).

**Angles:**

| Item | Angles | Family | `sigma_max` | `STEPS` |
|---|---|---|---|---|
| Rank 1 (gate) | 39.2°, 39.8° | `R4` (cpl=40) | 0.25 (corrected) | 5600 |
| Rank 2a (settling, gated) | 41.825° | `R5` (cpl=50) | 0.2 (corrected) | 7000 vs 10500 |
| Rank 2b (interior sweep, gated) | 41.750, 41.775, 41.825, 41.850, 41.875, 41.900° | `R5` (cpl=50) | 0.2 (corrected) | 7000 |
| Rank 3a (gated) | 41.6° | `R4` (cpl=40) | native 0.5 **and** corrected 0.25 | 5600 |
| Rank 3b (gated) | 41.750–41.900° (same six as exp-094 Rank 1b) | `R4` (cpl=40) | native 0.5 | 5600 |
| Rank 4 (unconditional) | 38.4° | `R3` (cpl=30) | corrected 1/3 | 4200 |

**FDTD call accounting** (matching this sub-thread's own established
per-angle costing: a genuinely new angle/resolution/sigma combination with
no already-filed comparator needs empty+article for both configs = 4
calls; a corrected-sigma-only addition where the empty and native-sigma
legs are already filed needs article-only calls, reusing prior data,
matching exp-093's own item-3 precedent exactly):

- **Rank 1:** 2 angles × 2 configs × (empty + article) = **8 calls**. (No
  prior `cpl=40` data exists at 39.2°/39.8° — a genuinely fresh pair of
  points, both legs needed, matching Rank 2's own 4-calls-per-angle
  precedent in exp-094, not the loosely-stated "2–4" in Red Team's own
  queue text — refined here to the precise, house-consistent count.)
- **Rank 2a:** 2 `STEPS` × 2 configs × (empty + article) = **8 calls**.
- **Rank 2b:** 6 angles × 2 configs × (empty + article) = **24 calls**.
- **Rank 3a:** 2 configs × (empty + native-article + corrected-article) =
  **6 calls** — a genuinely new angle/resolution pair, all three legs
  fresh.
- **Rank 3b:** 2 configs × 6 angles × (native-article only; empty legs
  already filed in exp-094's own Rank-1b `results.json`, corrected-article
  legs already filed too — only the native-sigma article call is new,
  mirroring exp-093's own item-3 reuse idiom exactly) = **12 calls**.
- **Rank 4:** 2 configs × (corrected-article only; empty and native-article
  legs already filed in exp-094's own Rank-3 `results.json`) = **2 calls**.

**Total: 60 calls if Rank 1 PASSES** (8 + 32 + 18 + 2); **10 calls if Rank
1 FAILS** (8 + 2, Ranks 2/3 skipped). Either way, `run.py` completes and
writes a full `results.json`/`NOTES.md` — a FAIL is a reported outcome,
never a crash.

**Mandatory new-suite gates (`R5` family; PANEL.md's "new machinery ⇒ new
suite stage with ≥1 absolute identity gate," applied fresh — not inherited
from `R4`):**

1. Vacuum-footprint precondition, applied to `R5_CONFIGS`.
2. `assert R5_CONFIGS["C40_R5"]["A"] == R5_CONFIGS["G40_R5"]["A"] ==
   round(A_HALF_APERTURE×2.5) == 1880`.
3. `assert abs(L_GEOMETRIC_M_R5 - L_GEOMETRIC_M) < 1e-12` **and**
   `abs(L_GEOMETRIC_M_R5 - L_GEOMETRIC_M_R3) < 1e-12` **and**
   `abs(L_GEOMETRIC_M_R5 - L_GEOMETRIC_M_R4) < 1e-12` — bit-identical
   physical shell radius across all four resolution families now in use.
4. `assert abs(SIGMA_R5_CORRECTED - 0.2) < 1e-12`.
5. **(Mandatory, from this family's first commit — not retrofitted after
   the fact.)** The `R4` family's own Gate 5 (`sim.sigma_e[shell_mask]
   .max()` runtime check, immediately after `build_article_r5_sigma`,
   before any FDTD step), mirrored line-for-line for `R5`. **Learned
   directly from exp-094's own Result-section correction**: the
   fault-injection verification of this gate (`gate5_wiring_defect_
   verification.py`'s own idiom, extended to the new `R5` call site) is
   written and RUN during Phase 4 itself, before any `R5`-family result is
   reported — not deferred to a mid-Phase-5 fix as exp-094's own first
   draft mistakenly claimed had already happened. This is the R4-house-rule
   application exp-094's own Learned #5 named (a verification claim is
   itself subject to recompute-don't-hand-type) applied prospectively,
   not just retrospectively.
6. (Documentation-only, non-discriminating, per `R4`'s own precedent — not
   a substitute for gate 5.) `abs(2×SIGMA_R5_CORRECTED×R5_R_OUT −
   2×SIGMA_NATIVE×R_OUT) < 1e-9`.

**Results-file convention (R16 compliance):** the top-level
`netd_disclaimer` key travels unconditionally, identical wording to
exp-093/094. `netd_row()` (exp-093's own committed extraction, imported
verbatim) is called and its output merged into every Rank's own report
dict at first draft — not added post-audit.

## 4. T1 escape route

**N/A** — independently re-verified against LOGBOOK.md's own record: every
T28 sub-thread entry from Iteration 46 through Iteration 71 states T1
route N/A / Checkpoint criterion 2 N/A. This cycle takes no position on
σ(I)/σ(x,t)/angular selectivity/sub-threshold operation, makes no
phenomenon-mechanism claim, and does not touch `REALIZABILITY_MEMO.md`.
Matching every T28 desk/instrument cycle since exp-069 (e.g. exp-069/070/
072/090/091/092/093/094), this is INSTRUMENT-VALIDATION work: a
ground-truth control on a measurement family, a resolution-convergence
probe, and a confound-disentangling check on an existing near-null window
— not a claim about any material or mechanism. **Realizability bound: N/A**
for the identical reason; `REALIZABILITY_MEMO.md` is not opened, cited, or
re-scored.

## 5. Predicted outcomes, per metric, falsifiable (frozen before any run)

**Rank 1 (PRIMARY, gates Rank 2 + Rank 3).** See §2 for the full go/no-go
criterion. Restated compactly: PASS = `delta_scene(R4, 39.2°) < 0` AND
`delta_scene(R4, 39.8°) < 0`, both `floor_pass=True`. No confident lean
stated on PASS-vs-FAIL itself (this is a control, not a hypothesis test
with a preferred outcome) — but if PASS, the *specific* numeric values are
predicted to land within an order of magnitude of the already-filed `R3`
comparators (informational band [0.2, 5]× ratio, non-gating, per §2).

**Rank 2a (settling precondition, PRIMARY, gates Rank 2b).** Identical
bands to exp-094's own Rank 1a, applied at the new `R5` resolution:
CONFIRM/PASS = `|delta_scene(STEPS=10500) − delta_scene(STEPS=7000)| /
|delta_scene(STEPS=7000)| ≤ 1×10⁻²`. CAUTIONARY-PASS (proceed, flag
settling-uncertain) = `(1×10⁻², 1×10⁻¹]`. HALT (skip Rank 2b's 24 calls) =
`> 1×10⁻¹`.

**Rank 2b (PRIMARY).** Three-way outcome, identical categories to
exp-093's item 1 / exp-094's Rank 1b: **TWO-NODE CONFIRMED** (≥1 point
`delta_scene>0` AND `floor_pass`, matching `cpl=40`'s own reading);
**SINGLE-NULL** (all six points `delta_scene≤0`, matching `cpl=30`'s own
reading — i.e. `cpl=50` reverts, suggesting oscillation with resolution,
not convergence); **STILL AMBIGUOUS** (no point clears the floor gate
either direction, or the six points split — neither prior reading
reproduced, suggesting genuine non-convergence at any resolution this
bench can affordably reach). **No confident lean stated**: the two
available data points (`cpl=30`→SINGLE-NULL, `cpl=40`→TWO-NODE CONFIRMED)
are a complete reversal with no established trend to extrapolate: SINGLE-
NULL, TWO-NODE CONFIRMED, and STILL AMBIGUOUS are treated as equally
plausible, pre-registered outcomes, per R15's own addendum text ("two such
points cannot, on their own, distinguish genuine continuum convergence
from a persistent recipe-level artifact or a genuinely non-convergent
oscillation").

**Rank 3a (PRIMARY, informational lean only).** `delta_scene`/
`frac_contrast` ratio (corrected/native) at 41.6°, `cpl=40`, scored with
the established `[0.3,3.0]` CONFIRM / outside-`[0.1,10]` REFUTE bands
(sign-matched), exactly as exp-094's own Rank 2 scored the identical
comparison at `cpl=30`. No confident directional lean (matching exp-094's
own Phase-3 RT-2 correction) — 41.6°'s `cpl=30`-native `ratio_k`=25.9467
sits in the same high-`ratio_k`, near-null-adjacent population as this
window's other fragile points.

**Rank 3b (PRIMARY, the confound-disentangling test — the sharpest
falsifiable question this cycle asks).** Compare native-sigma `cpl=40`
readings (this item, new) against the already-filed corrected-sigma
`cpl=40` readings (exp-094 Rank 1b, all six angles CONSISTENT,
`delta_scene>0`, `ratio_k` 3.67–7.13). **CONFIRM** = native-sigma `cpl=40`
readings ALSO read positive/CONSISTENT at all six angles (sign/
classification survives the sigma choice) — the `R4`-family reversal is a
genuine grid-refinement property, not an artifact of exp-094's own choice
to run the interior sweep only at corrected sigma. **REFUTE** = native-
sigma `cpl=40` reverts to negative/ENERGY-DOMINANT (matching `cpl=30`'s
own SINGLE-NULL reading) at a majority (≥4/6) of the six angles — meaning
the sigma correction itself, not `cpl=40` refinement, was the dominant
driver of exp-094's own headline reversal, a materially different and
more specific finding than exp-094's own record currently states. **MIXED**
= neither majority holds. No confident lean stated — this test exists
precisely because exp-094's own design confounded these two variables and
never separated them.

**Rank 4 (PRIMARY).** 38.4° at corrected sigma (1/3), `cpl=30`. Baseline
(exp-094 Rank 3, native sigma, already filed): `ratio_k`=16.9967,
`delta_scene`>0 (`Y=1`, FLIPPED from `cpl=20`'s `Y=0`). **CONFIRM** =
corrected-sigma reading also positive/`Y=1` (the `cpl=20→30` flip is a
genuine crossing migration, unaffected by the sigma correction).
**REFUTE** = corrected-sigma reverts to negative/`Y=0` (matching `cpl=20`
— the `cpl=30` flip was itself a `sigma_max` contamination artifact, not a
genuine crossing migration, the identical failure mode item 3 found at
42.0°, one angle over). **NEITHER** = neither clears `floor_pass` cleanly
in one direction. No confident lean (QUANTUM's own self-falsified
Idealization-21 finding, exp-094: the premise that 38.4° sits "far from
any known or suspected null" — which licensed native-sigma-only
measurement there in the first place — no longer holds; native-sigma-only
readings at 38.4° are therefore no longer safe to trust alone, which is
this item's entire reason for existing).

**Informational, non-gating, every Rank:** `p_abs_w` (G/C) ratio expected
within 1–5% of unity, `ratio_abs_ext_raw` within ~1% of the T9 0.51
anchor, matching this program's own unbroken three-resolution record
(`cpl`∈{20,30,40}) that the coherent `delta_scene`/`ratio_k` channel swings
by 10–20× while the energy channel never has. A deviation outside this
band at `cpl=50` specifically would be a genuine, previously-unexamined
surprise (Idealization 23-lineage, extended one resolution further), not
smoothed over.

## 6. Idealizations

**Carried forward from exp-094's own list, cited by original number:** 1
(2D TMz, 600 nm only), 3 (NETD ≠ human-eye threshold), 6 (`FLOOR` applied,
not recomputed, at every new point/resolution — now inherited unrecomputed
a fourth time, at `cpl=50`; Red Team's own queue item 8, a FLOOR
recalibration per family, is explicitly NOT in this cycle's scope), 7 (no
constraint-1/2/3/4 test, no T1 position), 8 (the unbiased margin-vs-
distance rebuild on the full 31-point window remains open, untouched), 11
(a sigma-branch verdict at one angle/resolution does not, by itself,
revalidate comparability elsewhere), 16 (angular-only or single-resolution
results are not automatically R15-grade), 17 (the `R3`/`R4`/`R5` families
are a single mechanical construction recipe applied at three ratios, not
three independent re-derivations of the discretization scheme — now
extended explicitly to `R5`), 21 (Rank 4 assumes the sigma-sensitivity
found at 41.8°/42.0°/38.4° may or may not be general; this cycle tests
38.4° but does not test whether 36.0°/38.8° — Rank 3's own CONSISTENT
census points — carry the same sensitivity), 23 (the energy-flatness
finding is now `cpl`∈{20,30,40}-verified; this cycle's own informational
checks are its first test at `cpl=50`, not assumed pre-answered).

**New this cycle:**

24. Rank 1's go/no-go criterion tests **sign only**, at exactly two angles.
    A PASS does not certify every `R4`-family reading in exp-094 is
    artifact-free — a registration defect could in principle be
    angle-dependent in a way these two points do not expose. It is the
    minimum discharge Red Team's own queue named, not an exhaustive
    `R4`-family audit.
25. The `R5` (`cpl=50`) family, like `R4` before it, is validated at Gate
    5 only for the specific call sites this cycle exercises (Rank 2a/2b).
    Retrofitting an equivalent runtime check onto the `R3` family's own
    existing sigma-branch call sites (exp-091/092/093) remains open — Red
    Team's own queue item 6, explicitly out of this cycle's scope (ranked
    below items 1–4).
26. Rank 3b's confound-disentangling test (native-vs-corrected sigma at
    fixed `cpl=40`) isolates ONE candidate explanation (sigma choice) for
    exp-094's own reversal. A CONFIRM outcome (reversal survives at native
    sigma too) does not rule out other candidate explanations (e.g. genuine
    curved-boundary staircasing at finer `cpl`, EM's own re-applied
    dispersion-integral account, exp-094 Learned #1) — it only rules sigma
    choice OUT as the sole driver, or IN as a contributing one.
27. This cycle gates Rank 3 on Rank 1 by extending Red Team's own literal
    text ("any further `R4`-family spend") — a judgment call, stated and
    justified in §2, not itself Red-Team-pre-registered language.

**Carried idealizations banner (mandatory at both this section and §5, per
the Iteration-65 CHECKPOINT's non-discretionary rule): every prediction in
§5 is governed by Idealizations 1/3/6/7/8/11/16/17/21/23 plus this cycle's
own 24–27.**

## 7. Estimated FDTD call count and wall-time budget

**60 calls total if Rank 1 PASSES (8 + 32 + 18 + 2); 10 calls if Rank 1
FAILS (8 + 2).** This would be the largest single T28 cycle to date on the
PASS path (exceeding exp-094's own 48-call record), driven almost entirely
by `R5`'s `cpl=50` cost — justified because it is the specific,
minimum-discharge test R15's own addendum names, not spend for its own
sake, and is itself pre-gated by the cheapest possible check (8 calls) to
avoid it being wasted on a compromised `R4` anchor.

**CPU-minute model** (scaling from exp-094's own filed per-call rates;
2D-grid cost scales roughly with `RATIO³` — cells ~`RATIO²`, `STEPS`
~`RATIO`):

- Rank 1 (8 calls, `cpl=40`, `STEPS`=5600 throughout): ≈64 CPU-min
  (exp-094 Rank 1b's own rate, 191.4 CPU-min / 24 calls ≈7.98 CPU-min/call).
- Rank 2a+2b (32 calls, `cpl=50`): exp-094's own `R4` Rank-1 rate (271.1
  CPU-min / 32 calls ≈8.47 CPU-min/call) scaled by `(2.5/2.0)³≈1.953` ≈
  16.5 CPU-min/call → ≈529 CPU-min.
- Rank 3 (18 calls, `cpl=40`, `STEPS`=5600): ≈8.0 CPU-min/call ≈144 CPU-min.
- Rank 4 (2 calls, `cpl=30`): exp-094's own Rank-2 rate (13.5 CPU-min / 4
  calls ≈3.4 CPU-min/call) ≈7 CPU-min.

**Total ≈744 CPU-min (≈12.4 CPU-hours) if Rank 1 passes; ≈71 CPU-min if it
fails.** At 4 workers: wall ≈186 min (≈3.1 h) on the PASS path, ≈18 min on
the FAIL path — both model estimates; this program's own unbroken
track record (every T28 cycle's actual wall time has landed under its own
model estimate, e.g. exp-093: 29.4 min actual vs. 55–166 min estimated;
exp-094: 50.6 min actual vs. 80–100 min estimated) makes the PASS-path
figure a conservative upper bound, not an expected value.
