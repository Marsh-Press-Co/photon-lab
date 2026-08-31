# exp-095 — R4 Ground-Truth Sign Control, cpl=50 (R5) Third Resolution Point, sigma/38.4° Comparability Closes

*Panel Iteration 72. Lead seat (rotation): VISION SCIENCE. Full phase
record: `phase1_proposal.md` (VISION SCIENCE) → five blind Phase-2
critiques (PHOTONICS, MATERIALS, ELECTROMAGNETISM, THERMODYNAMICS, QUANTUM
OPTICS, unanimous support-with-changes) → `phase2_redteam_audit.md`
(PROCEED-WITH-MANDATORY-FIXES, 9 items, zero overridden) →
this document (Phase 3 SYNTHESIS, Director), all 9 fixes adopted.*

## Hypothesis

exp-094 (Iteration 71) found that its new `cpl=40` (`R4`) congruent-geometry
family reverses, in both sign and classification, exp-093's `cpl=30`
SINGLE-NULL reading at *all six* interior near-null points
(41.750°–41.900°) — R15's own founding concern, realized on R15's own
founding sub-thread one cycle after the verdict it exists to stress-test.
Red Team's Phase-5 final audit (exp-094) named the minimum discharge: a
ground-truth sign-recovery control on `R4` at points where the answer is
already known, before trusting any further `R4`-family spend (Rank 1);
only then a third, differently-ratioed resolution point (`cpl=50`, Rank 2,
gated on Rank 1). This cycle's own Phase 2 (five blind critiques + Red
Team) then found the Phase-1 draft's control points and Rank-2 evidentiary
framing themselves needed correction — see "Changes from Phase 1" below.

This cycle closes: (1) the ground-truth sign+node-bracketing gate on `R4`
(Rank 1, unconditional, runs first); (2) a third, differently-ratioed
resolution point at `cpl=50` (Rank 2, gated on Rank 1, now carrying an
explicit necessary-but-insufficient framing and a native-sigma comparator
leg); (3) the sigma-comparability chain at both edges of the
41.6°–42.0° window for the `R4` family (Rank 3, gated on Rank 1, unchanged
from Phase 1); (4) 38.4° re-measured at corrected sigma (Rank 4, the `R3`
family, unconditional). **Pure instrument recalibration — no
phenomenon-mechanism claim.** T1 route N/A, Checkpoint criterion 2 N/A,
matching every T28 desk/instrument cycle since exp-069.

## Changes from Phase 1, per Red Team's 9-item mandatory-fix docket

All nine items ADOPTED, zero overridden (`phase2_redteam_audit.md` §5):

1. **Control-angle replacement.** Dropped 39.8° (0.272° from a known null)
   and 39.0° (0.410°, comparably compromised, PHOTONICS' own proposed
   alternative rejected by Red Team's own independent check). Rank 1a now
   uses **39.2° and 39.4°** — distances to the nearest of the full known
   crossing set (four `cpl=20` crossings 37.127°/38.590°/40.265°/41.461°
   plus the `cpl=30` crossings 40.0718°/41.7811°/41.8377°, independently
   re-derived this session, §"Parameter table" below) are **0.610°** and
   **0.672°** respectively — both comfortably outside the ~0.27°–0.41°
   danger band that disqualified 39.8°/39.0°.
2. **Node-bracketing recovery check (Rank 1c), new, 8 calls.** QUANTUM's
   own finding: an off-node sign check has near-zero statistical power
   against the specific registration/phase-defect class R15's addendum
   exists to catch (near a node, sign is phase-controlled; far from a
   node, amplitude-controlled and phase-insensitive). Added as a THIRD,
   additive Rank-1 test at 38.49°/38.69° (±0.1° around the established
   `cpl=20` null θ₀≈38.590°), powered against exactly the defect class the
   sign check cannot see. Complementary to, not a replacement for, item 1.
3. **Native-sigma R5 comparator leg (Rank 2b-native), new, 4 calls.** EM's
   own finding, independently corroborated against exp-093's own Item 3
   (native→corrected sigma sign-flipped `delta_scene` at 42.0°, one angle
   over from this window): Rank 2b as drafted had no native-sigma `R5`
   leg anywhere, unlike Rank 3 (which has exactly this check for `R4`).
   Added at 41.825°/41.850° (nearest the already-demonstrated
   41.8°/42.0° sigma-sensitivity), article-only, reusing Rank 2b's own
   in-memory empty-scene captures at the identical angles/steps (sigma
   has no effect on the empty leg — the same reuse idiom exp-093's own
   Item 3 established for the `R4` family, applied here to `R5`).
4. **Rank 2b framing corrected.** MATERIALS' proof (independently
   re-verified, Red Team §1): `R_OUT=78` is even, so Gate-3 bit-exactness
   under this recipe requires `cpl` a multiple of 10 — `cpl=50` is the
   *nearest remaining* Gate-3-exact point, continuing the identical
   `1.5→2.0→2.5` arithmetic progression `R3`/`R4` already are, not an
   independent discretization. **No Rank-2b outcome (TWO-NODE
   CONFIRMED / SINGLE-NULL / STILL AMBIGUOUS) discharges R15's addendum on
   its own** — a recipe-level systematic reproduces at every ratio drawn
   from the identical `r{n}_config()` formula by construction. Stated
   explicitly wherever Rank 2b's outcome is reported (both print and
   `results.json`), per Idealization 17 and the mandatory disclosure
   sentence quoted verbatim in the Parameter table below.
5. **Companion desk bound, new, zero FDTD.** MATERIALS' own remedy (b):
   after Rank 2b's classification is known, if it *differs* from
   exp-094's own already-filed `cpl=40` classification at the corresponding
   angle, compute and report the ratio of the observed cross-resolution
   `delta_scene` shift to the `cpl=45`-scale radius-drift bound Red Team
   quantified (`|175.5−176|/176 ≈ 0.284%`) — an honest, disclosed
   order-of-magnitude sanity check (Idealization 29), not a rigorous
   alias-decomposition, arguing against (not proving against) a pure
   radius-rounding origin for any reversal seen.
6. **Rank 2b/Rank 3b cross-reference.** Attack #2 (Red Team): Rank 3b's
   native-vs-corrected `cpl=40` disentangling test and Rank 2b-native's
   own native-vs-corrected `cpl=50` reading (item 3 above) are the SAME
   open question (is the sigma correction itself, not resolution
   refinement, the dominant driver of this window's reversals?) asked at
   two resolutions — not two independently-scoped items. Both results are
   printed and persisted with an explicit AGREE/DISAGREE cross-reference
   sentence (§ Rank 2b-native below).
7. **`cell_metrics_r5` named and wired, same diff as everything else.**
   THERMODYNAMICS' own R16-risk catch, independently confirmed against
   this exact failure shape recurring in exp-094's own first draft: no
   `cell_metrics_r5` was named anywhere in the Phase-1 draft, despite Rank
   2 being fresh code in exactly the shape (`box_for_rN`/`ref_for_rN`/
   `_run_sim_rN_sigma`, hand-copied per family) that produced R16's
   founding gap. `cell_metrics_r5(key, th, steps, cap_empty, cap_article)`
   is written below as a line-for-line mirror of `cell_metrics_r4`, its
   `netd_row()` merge wired into every Rank-2/Rank-2a report dict in the
   SAME diff that adds the function.
8. **`p_abs_w` settling band for Rank 2a, new.** Rank 2a's own settling
   precondition previously named only a `delta_scene`-based band. Now ALSO
   computes the identical three-way PASS/CAUTIONARY-PASS/HALT band on
   `p_abs_w` at the same two `STEPS` values, reported alongside,
   informational, non-gating (matches this program's established
   treatment of `p_abs_w` throughout — never PRIMARY).
9. **Budget reconciliation, disclosed explicitly.** §"Estimated FDTD call
   count" below states the PASS-path total is well above this sub-thread's
   own established ~100–150 CPU-min per-cycle band, and reconciles this
   against items 4–6 above (Rank 2's rescoped, necessary-but-insufficient
   evidentiary weight) rather than silently inheriting "the largest cycle
   to date" without comment.

**Disclosed spec-resolution note (this Phase, not part of Red Team's
docket — an implementation-necessity gap found while writing `run.py`,
resolved the same way exp-094's own docstring disclosures (i)–(iii)
resolved comparable frozen-spec internal contradictions):** the Phase-1
draft's own call accounting for Rank 3b ("12 calls... empty legs already
filed in exp-094's own Rank-1b `results.json`... article-only") and Rank 4
("2 calls... empty and native-article legs already filed in exp-094's own
Rank-3 `results.json`... article-only") both describe CROSS-PROCESS reuse
(exp-094 is a separate, already-completed script execution) using language
that only correctly describes SAME-PROCESS reuse (exp-093's own Item 3,
which reuses an in-memory captures dict populated earlier in that same
script's own execution — confirmed by reading `experiments/093-.../run.py`
directly this session). This codebase's `results.json` convention never
persists raw field captures, only derived scalar metrics (confirmed by
reading `experiments/093/094-.../results.json` directly) — `delta_scene`
is, throughout this program, `C_g − C_c`, where each config's own `C`
requires BOTH its empty-scene AND article-scene captures
(`amb.contrast_from_runs`, confirmed by reading
`experiments/091-.../run.py::contrast_pair` directly). A genuinely NEW
sigma-branch reading (Rank 3b's native-sigma `cpl=40` leg; Rank 4's
corrected-sigma `cpl=30` leg) therefore structurally requires a FRESH
empty-scene capture alongside the fresh article capture — there is no
raw-capture object left over from exp-094's own, separate, already-closed
process to reuse. This is the identical cross-process pattern
exp-094's own Rank 2 already used correctly (a fresh corrected-sigma
reading spent BOTH legs, comparing only its final scalar against an
already-filed native comparator that cost zero new calls) — Rank 3b/Rank 4
are implemented identically: the "already filed" side is a pulled scalar
comparator (zero new calls), and the new side spends its full empty+article
pair. This raises Rank 3b from 12→**24** calls and Rank 4 from 2→**4**
calls (both configs × both legs), and the PASS-path grand total from the
Phase-1/Red-Team-stated 72 to **86** (FAIL-path 18→**20**). Nothing about
the angles, sigma choices, gating logic, outcome taxonomy, or idealizations
changes — only the mechanical FDTD-call bookkeeping for two items is
corrected to match what the design actually requires to execute. Flagged
here explicitly, not silently absorbed into the headline figures, per this
program's own recompute-don't-hand-type discipline.

## Setup

**Channel:** `PAIR_KEYS_R4=("C40_R4","G40_R4")` (Rank 1, Rank 3), reusing
exp-094's own committed `R4_CONFIGS`/`box_for_r4`/`ref_for_r4`/
`build_article_r4_sigma`/`_run_sim_r4_sigma`/`cell_metrics_r4`/
`run_block_r4` verbatim — zero diff to `experiments/094-.../run.py`.
`PAIR_KEYS_R5=("C40_R5","G40_R5")` (Rank 2), a genuinely new family already
appended to `experiments/069-.../design_geometry.py` by the Director prior
to this Phase (`R5_RATIO=2.5`, mechanically substituted for `R4_RATIO=2.0`
into the already-committed `r4_config()` recipe — verified present and
bit-exact by reading that file directly this session, not re-derived).
`PAIR_KEYS_R3=("C40_R3","G40_R3")` (Rank 4), reusing
`experiments/091–094`'s own committed `R3_CONFIGS`/`build_article_r3_sigma`
verbatim. λ=600nm throughout.

**R5 geometry constants** (already committed in `design_geometry.py`,
confirmed present, not re-derived here):

| Constant | Value |
|---|---|
| `R5_RATIO` | `2.5` |
| `R5_CPL` | `{600: 50}` |
| `R5_R_OUT`/`R5_W_OBJ`/`R5_W_FLANK` | `195` |
| `R5_GUARD_OUT` | `462` |
| `R5_STEPS` / `R5_STEPS_STRESS` | `7000` / `10500` |
| `PEC_R_R5` | `75` |
| `BOX_CLEARANCE_A_R5` / `B_R5` | `30` / `60` |
| `REF_HALF_H_R5` | `200` |
| `SIGMA_R5_CORRECTED` | `0.2` |
| `DX_M_R5` | `1.2×10⁻⁸` m |
| `L_GEOMETRIC_M_R5` | `2.34×10⁻⁶` m (bit-identical to native/`R3`/`R4`) |
| `R5_CONFIGS["C40_R5"/"G40_R5"]["A"]` | `1880 = round(752×2.5)` |

**Full known-crossing set** (re-derived this session, not hand-typed):
`cpl=20` (`experiments/090-.../results.json::q8.crossings_deg`):
37.127246°, 38.590230°, 40.265420°, 41.460901°. `cpl=30`
(`experiments/092-.../results.json::rank1.crossing_report`): lower
40.071838°, upper 41.781067°, upper (second) 41.837653°.

**Rank-1 control-angle distances** (mandatory fix #1, recomputed against
the FULL set above, not merely the nearest `cpl=30` crossing):

| θ | nearest known null | distance |
|---|---|---|
| 39.0° (rejected, PHOTONICS' own alternative) | 38.590° | 0.410° |
| 39.2° | 38.590° | **0.610°** |
| 39.4° | 40.0718° | **0.672°** |
| 39.8° (rejected, Phase-1 draft's original) | 40.0718° | 0.272° |

**Already-filed comparator values for the Rank-1a sign check** (re-pulled
this session, not hand-typed):

| θ | `delta_scene` @ `cpl=20` (exp-083 `results.json::thetas`/`delta_scene`) | `delta_scene` @ `cpl=30` (exp-092 `results.json::rank1.per_theta`) | `floor_pass`@30 |
|---|---|---|---|
| 39.2° | −1.8292×10⁻³ | −2.4921×10⁻³ | True |
| 39.4° | −1.8669×10⁻³ | −2.2113×10⁻³ | True |

Both angles: **negative** sign, consistent across both already-measured
resolutions, comfortably floor-clearing — the known-correct answer at
both control points.

**Full parameter table:**

| Item | Angles | Family | `cpl` | `sigma_max` | `STEPS` | Configs | Calls |
|---|---|---|---|---|---|---|---|
| Rank 1a (sign check, gate) | 39.2°, 39.4° | `R4` | 40 | 0.25 (corrected) | 5600 | `C40_R4`,`G40_R4` | 8 |
| Rank 1c (node bracket, gate) | 38.49°, 38.69° | `R4` | 40 | 0.25 (corrected) | 5600 | `C40_R4`,`G40_R4` | 8 |
| Rank 2a (settling, gated) | 41.825° | `R5` | 50 | 0.2 (corrected) | 7000 vs 10500 | `C40_R5`,`G40_R5` | 8 |
| Rank 2b (interior sweep, gated) | 41.750–41.900 (6 pts) | `R5` | 50 | 0.2 (corrected) | 7000 | `C40_R5`,`G40_R5` | 24 |
| Rank 2b-native (comparator, gated) | 41.825°, 41.850° | `R5` | 50 | 0.5 (native), article-only | 7000 | `C40_R5`,`G40_R5` | 4 |
| Rank 3a (gated) | 41.6° | `R4` | 40 | native 0.5 **and** corrected 0.25 | 5600 | `C40_R4`,`G40_R4` | 6 |
| Rank 3b (gated) | 41.750–41.900 (same 6) | `R4` | 40 | native 0.5 | 5600 | `C40_R4`,`G40_R4` | 24* |
| Rank 4 (unconditional) | 38.4° | `R3` | 30 | corrected 1/3 | 4200 | `C40_R3`,`G40_R3` | 4* |

`*` Rank 3b/Rank 4 counts corrected upward from the Phase-1 draft's stated
12/2 — see "Disclosed spec-resolution note" above.

**Rank 1 — combined go/no-go gate (16 calls, unconditional, runs FIRST).**
Rank 1a (sign check): PASS = `delta_scene(R4)` negative at BOTH 39.2° and
39.4°, `floor_pass=True` at both. Rank 1c (node-bracketing recovery,
NEW): PASS = `floor_pass=True` at BOTH 38.49°/38.69° AND their
`delta_scene` signs DIFFER (confirms the `R4` family reproduces the
established node's presence, not merely a far-field sign);
INCONCLUSIVE = `floor_pass=False` at either point; FAIL = both
floor-clear but SAME sign (the established node appears to have vanished
from this window in the `R4` family — a genuine integrity finding).
**Combined go/no-go:** PROCEED to Rank 2/3 only if Rank 1a is PASS AND
Rank 1c is PASS or INCONCLUSIVE (not FAIL). Otherwise HALT before Rank
2/3 — Rank 4 still runs (independent, unconditional), and a full
`results.json`/`NOTES.md` is written reporting everything measured,
flagged as a Checkpoint-4-relevant integrity finding per Phase-1's §2
language, per this program's own "a FAIL is a reported outcome, never a
crash" discipline.

**Rank 2 — `cpl=50` (`R5`) family, gated on Rank 1 PROCEED (36 calls).**
Rank 2a: three-way settling precondition (CONFIRM/CAUTIONARY-PASS/HALT,
identical bands to exp-094's own Rank 1a) on BOTH `delta_scene` (PRIMARY,
gating) and `p_abs_w` (informational, non-gating, mandatory fix #8), at
`STEPS`∈{7000,10500}. Rank 2b: six-angle interior sweep, corrected sigma,
gated on Rank 2a not HALTing — TWO-NODE CONFIRMED / SINGLE-NULL / STILL
AMBIGUOUS, identical categories to exp-094's own Rank 1b. **Mandatory
disclosure (mandatory fix #4), non-buried, printed and persisted wherever
this outcome is reported:** "This outcome alone does NOT discharge R15's
Iteration-71 addendum — R5 is drawn from the identical `r{n}_config()`
mechanical recipe as R3/R4 (only Gate-3-exact ratios, i.e. `cpl` a
multiple of 10, are reachable), so a recipe-level systematic would
reproduce identically at this ratio too. See Idealization 17/28/29." Rank
2b-native (mandatory fix #3): native-sigma article-only leg at
41.825°/41.850°, empty legs reused in-memory from Rank 2b itself (no
sigma dependency). Compared against Rank 2b's own corrected-sigma reading
at the same two angles: CONFIRM (sign/classification survives) or REFUTE
(reverts). **Mandatory fix #6, explicit cross-reference:** this
sub-result is compared, in the same print/persist block, against Rank
3b's own `cpl=40` disentangling result — stated as AGREE (both CONFIRM or
both REFUTE sigma-robustness) or DISAGREE, since they are the same open
question at two resolutions. **Mandatory fix #5, companion desk bound:**
computed only if Rank 2b's classification at any of the six angles
differs from exp-094's own filed `cpl=40` classification at the
corresponding angle; otherwise reported as "not triggered."

**Rank 3 — `cpl=40` (`R4`) sigma-comparability, gated on Rank 1 PROCEED
(30 calls, corrected count — see disclosure above; UNCHANGED design from
Phase 1).** Rank 3a: 41.6°, native+corrected sigma, `[0.3,3.0]` CONFIRM /
outside-`[0.1,10]` REFUTE bands (sign-matched), exactly as exp-094's own
Rank 2 scored the identical comparison at `cpl=30`. Rank 3b: the
confound-disentangling test — native-sigma `cpl=40` readings at the six
interior angles, compared against exp-094's own already-filed
corrected-sigma readings (all six CONSISTENT, `delta_scene>0`). CONFIRM =
native-sigma readings ALSO positive/CONSISTENT at all six (the reversal is
a genuine grid-refinement property). REFUTE = native-sigma reverts to
negative/ENERGY-DOMINANT at ≥4/6 (the sigma correction, not `cpl=40`
refinement, was the dominant driver). MIXED = neither majority.

**Rank 4 — 38.4° at corrected sigma, `R3`/`cpl=30` family (4 calls,
corrected count — see disclosure above; UNCONDITIONAL, runs regardless of
Rank 1's outcome).** Baseline (exp-094 Rank 3, native sigma, already
filed): `ratio_k=16.9967`, `floor_pass=True`, `Y=1` (FLIPPED from
`cpl=20`'s `Y=0`). CONFIRM = corrected-sigma reading also `Y=1`. REFUTE =
reverts to `Y=0` (matching `cpl=20` — the `cpl=30` flip was itself a
`sigma_max` contamination artifact). NEITHER = neither clears
`floor_pass` cleanly in one direction.

**`cell_metrics_r5`** (mandatory fix #7): explicit line-for-line mirror of
`cell_metrics_r4`, substituting every `R4`-scoped constant/function for
its `R5` equivalent (`box_for_r5`/`ref_for_r5`/`PEC_R_R5`/`BOX_CLEARANCE_
A_R5`/`B_R5`/`dg.R5_R_OUT`/`DX_M_R5`/`L_GEOMETRIC_M_R5`/`dg.R5_W_OBJ`/
`dg.R5_GUARD_OUT`/`dg.R5_W_FLANK`). Its `netd_row()` merge is wired into
every Rank-2/Rank-2a report dict in the SAME diff that adds the function.

**New functions this cycle** (thin, mechanical mirrors of the `R4` layer):
`box_for_r5`, `ref_for_r5`, `build_article_r5_sigma`, `_run_sim_r5_sigma`
(carrying the mandatory Gate 5 runtime `sigma_e`/`sigma_max` check from
its first commit, `shell_mask=(PEC_R_R5<=rr<=dg.R5_R_OUT)`), `one_call_r5`,
`run_block_r5`, `cell_metrics_r5`. `gate5_wiring_defect_
verification.py` extends exp-094's own fault-injection idiom to the new
`R5` call site — written this Phase, run (its own light logic only, no
FDTD) this Phase, and to be RE-RUN with a real FDTD positive control
during Phase 4 before any `R5`-family result is reported (per Red Team's
own confirmation this is correctly planned, phase2 critique EM/§1).

### Mandatory new-suite gates (`R5` family, PANEL.md's "new machinery ⇒ new
suite stage with ≥1 absolute identity gate")

1. Vacuum-footprint precondition, applied to `R5_CONFIGS`.
2. `assert R5_CONFIGS["C40_R5"]["A"] == R5_CONFIGS["G40_R5"]["A"] ==
   round(A_HALF_APERTURE×2.5) == 1880`.
3. `assert abs(L_GEOMETRIC_M_R5 - L_GEOMETRIC_M) < 1e-12` **and**
   `abs(L_GEOMETRIC_M_R5 - L_GEOMETRIC_M_R3) < 1e-12` **and**
   `abs(L_GEOMETRIC_M_R5 - L_GEOMETRIC_M_R4) < 1e-12` — bit-identical
   physical shell radius across all four resolution families now in use
   (native/`R3`/`R4`/`R5`).
4. `assert abs(SIGMA_R5_CORRECTED - 0.2) < 1e-12`.
5. **(Mandatory, from this family's first commit.)** The `sim.sigma_e
   [shell_mask].max()` runtime check, immediately after
   `build_article_r5_sigma`, before any FDTD step, mirrored line-for-line
   for `R5` — see `_run_sim_r5_sigma`. Fault-injection verification
   (`gate5_wiring_defect_verification.py`, extended to the `R5` call site)
   is written and its light logic run this Phase; the full FDTD-backed
   positive/negative control pair runs during Phase 4, before any
   `R5`-family result is reported — not deferred to a mid-Phase-5 fix as
   exp-094's own first draft mistakenly claimed had already happened.
6. (Documentation-only, non-discriminating, `R4`'s own precedent.)
   `abs(2×SIGMA_R5_CORRECTED×R5_R_OUT − 2×SIGMA_NATIVE×R_OUT) < 1e-9`.

**Results-file convention (R16 compliance):** the top-level
`netd_disclaimer` key travels unconditionally, identical wording to
exp-093/094. `netd_row()` (imported verbatim through the `_load()` chain)
is called and its output merged into every Rank's own report dict at
first draft.

## Idealizations

**Carried forward from exp-094's own list, cited by original number:** 1
(2D TMz, 600nm only), 3 (NETD ≠ human-eye threshold), 6 (`FLOOR` applied,
not recomputed, at every new point/resolution — now inherited unrecomputed
a fourth time, at `cpl=50`), 7 (no constraint-1/2/3/4 test, no T1
position), 8 (the unbiased margin-vs-distance rebuild on the full
31-point window remains open, untouched), 11 (a sigma-branch verdict at
one angle/resolution does not, by itself, revalidate comparability
elsewhere), 16 (angular-only or single-resolution results are not
automatically R15-grade), 17 (the `R3`/`R4`/`R5` families are a single
mechanical construction recipe applied at three ratios, not three
independent re-derivations of the discretization scheme — extended
explicitly to `R5`), 21 (Rank 4 assumes the sigma-sensitivity found at
41.8°/42.0°/38.4° may or may not be general — untested at 36.0°/38.8°),
23 (the energy-flatness finding is now `cpl`∈{20,30,40}-verified; this
cycle's own informational checks are its first test at `cpl=50`, not
assumed pre-answered).

**Carried forward from exp-095's own Phase-1 draft, renumbered/kept:**

24. Rank 1a's go/no-go criterion tests **sign only**, at exactly two
    angles. A PASS does not certify every `R4`-family reading in exp-094
    is artifact-free — a registration defect could in principle be
    angle-dependent in a way these two points do not expose. Rank 1c
    (new) partially, not fully, closes this gap (Idealization 28).
25. The `R5` (`cpl=50`) family, like `R4` before it, is validated at Gate
    5 only for the specific call sites this cycle exercises (Rank 2a/2b).
    Retrofitting an equivalent runtime check onto the `R3` family's own
    existing sigma-branch call sites (exp-091/092/093) remains open — Red
    Team's own queue item 6 from the Iteration-72 reconciled queue,
    explicitly out of this cycle's scope.
26. Rank 3b's confound-disentangling test (native-vs-corrected sigma at
    fixed `cpl=40`) isolates ONE candidate explanation (sigma choice) for
    exp-094's own reversal. A CONFIRM outcome does not rule out other
    candidate explanations (e.g. genuine curved-boundary staircasing at
    finer `cpl`) — it only rules sigma choice OUT as the sole driver, or
    IN as a contributing one.
27. This cycle gates Rank 3 on Rank 1 by extending Red Team's own literal
    text ("any further `R4`-family spend") — a judgment call, stated and
    justified in the Phase-1 draft's §2, not itself Red-Team-pre-registered
    language. Unaffected by this Phase's mandatory fixes.

**New this cycle (Phase 3, from the mandatory-fix docket):**

28. The node-bracketing check (Rank 1c) tests whether the `R4` family
    reproduces an existing null's PRESENCE near 38.590°, not its EXACT
    location to sub-0.01° precision — a coarser recovery test than a full
    free-period fit, chosen for cost per Red Team's own item 2 scoping.
29. The desk bound in Rank 2's mandatory fix #5 (radius-drift-scale
    comparison) is an order-of-magnitude sanity check, not a rigorous
    alias-decomposition — it cannot rule OUT a recipe-level artifact of a
    different character (e.g. one not well-modeled as a radius
    perturbation at all), only argue against the SPECIFIC
    radius-rounding-scale story.
30. **(New, this Phase's own disclosed spec-resolution note.)** Rank 3b's
    and Rank 4's "already filed... reused" empty-leg language, read
    literally, describes a cross-process raw-capture reuse this codebase
    cannot perform (captures are never persisted). Implemented instead as
    a fresh full-leg measurement compared against an already-filed scalar
    comparator (exp-094's own Rank 2 precedent) — raises these two items'
    own call counts (12→24, 2→4) without changing any angle, sigma
    choice, or outcome-classification logic. See "Disclosed
    spec-resolution note" above for the full reasoning.

**Carried idealizations banner (mandatory at both this section and
Predictions, per the Iteration-65 CHECKPOINT's non-discretionary rule):
every prediction below is governed by Idealizations
1/3/6/7/8/11/16/17/21/23 plus this cycle's own 24–30.**

## Predictions (frozen, committed BEFORE any Phase-4 script runs)

*Every prediction below is governed by Idealizations
1/3/6/7/8/11/16/17/21/23/24–30.*

**(Rank 1a, PRIMARY, gates Rank 2+3 jointly with Rank 1c.)** PASS =
`delta_scene(R4, 39.2°) < 0` AND `delta_scene(R4, 39.4°) < 0`, both
`floor_pass=True`. No confident lean on PASS-vs-FAIL itself (a control,
not a hypothesis test with a preferred outcome) — but if PASS, the
specific numeric values are predicted to land within an order of
magnitude of the already-filed `cpl=20`/`cpl=30` comparators
(informational band [0.2, 5]× ratio, non-gating).

**(Rank 1c, PRIMARY, gates Rank 2+3 jointly with Rank 1a.)** PASS =
`floor_pass=True` at both 38.49°/38.69° AND `delta_scene(R4)` signs
DIFFER across the pair. INCONCLUSIVE = `floor_pass=False` at either.
FAIL = both floor-clear, same sign. No confident lean stated — this is a
control powered against a specific defect class, not a hypothesis with a
preferred direction; a FAIL here is exactly as informative (a genuine,
disclosed integrity finding) as a PASS.

**(Rank 2a, PRIMARY, gates Rank 2b.)** Identical three-way bands to
exp-094's own Rank 1a, applied at `cpl=50` on `delta_scene`: PASS
`rel_dev≤1e-2`; CAUTIONARY-PASS `(1e-2,1e-1]`; HALT `>1e-1` (skips Rank
2b's 24 calls). **New (mandatory fix #8), informational, non-gating:**
the identical band computed on `p_abs_w` at the same two `STEPS` values,
reported alongside — no confident lean on whether it lands PASS or
CAUTIONARY-PASS, but per this program's own unbroken record the energy
channel is expected to settle at least as cleanly as `delta_scene`.

**(Rank 2b, PRIMARY.)** Three-way outcome, identical categories to
exp-094's own Rank 1b: TWO-NODE CONFIRMED / SINGLE-NULL / STILL AMBIGUOUS.
No confident lean stated: the two available data points
(`cpl=30`→SINGLE-NULL, `cpl=40`→TWO-NODE CONFIRMED) are a complete
reversal with no established trend to extrapolate — all three outcomes
are equally plausible, pre-registered. **Whatever the outcome, it is
reported with the mandatory non-buried disclosure sentence (mandatory fix
#4, quoted in Setup above) — this outcome alone does not discharge R15's
addendum.**

**(Rank 2b-native, PRIMARY, mandatory fix #3.)** CONFIRM = native-sigma
`cpl=50` readings at 41.825°/41.850° preserve Rank 2b's own
corrected-sigma sign/classification at those two angles. REFUTE =
reverts. No confident lean (mirrors Rank 3b's own no-lean framing — this
test exists precisely because the prior design left this question
unexamined). **Cross-referenced explicitly against Rank 3b's own
`cpl=40` verdict (mandatory fix #6)**: AGREE if both CONFIRM or both
REFUTE sigma-robustness; DISAGREE otherwise — printed and persisted as
its own field, not left for the reader to infer.

**(Rank 2's companion desk bound, mandatory fix #5.)** Triggered only if
Rank 2b's classification differs from exp-094's own filed `cpl=40`
classification at any of the six angles. If triggered: report the ratio
of the observed `delta_scene` magnitude shift to the 0.284%
`cpl=45`-scale radius-drift bound, stated explicitly as an
order-of-magnitude sanity check, not a formal test (Idealization 29). If
not triggered: reported as "not triggered — no angle differs from
exp-094's own cpl=40 classification."

**(Rank 3a, PRIMARY, informational lean only.)** `delta_scene`/
`frac_contrast` ratio (corrected/native) at 41.6°, `cpl=40`, scored with
the established `[0.3,3.0]` CONFIRM / outside-`[0.1,10]` REFUTE bands,
exactly as exp-094's own Rank 2 scored the identical comparison at
`cpl=30`. No confident directional lean (41.6°'s high `ratio_k` at
`cpl=30`-native sits in the same fragile, near-null-adjacent population as
this window's other sensitive points).

**(Rank 3b, PRIMARY, the sharpest falsifiable question this cycle asks at
`cpl=40`.)** CONFIRM = native-sigma `cpl=40` readings ALSO read
positive/CONSISTENT at all six angles (the reversal is a genuine
grid-refinement property, not a sigma-choice artifact of exp-094's own
corrected-sigma-only interior sweep). REFUTE = native-sigma reverts to
negative/ENERGY-DOMINANT at ≥4/6. MIXED = neither majority. No confident
lean stated — this test exists precisely because exp-094's own design
confounded these two variables and never separated them.

**(Rank 4, PRIMARY.)** 38.4° at corrected sigma (1/3), `cpl=30`.
Baseline (exp-094 Rank 3, native sigma): `ratio_k=16.9967`,
`floor_pass=True`, `Y=1` (FLIPPED from `cpl=20`'s `Y=0`). CONFIRM =
corrected-sigma reading also `Y=1`. REFUTE = reverts to `Y=0`. NEITHER =
neither clears `floor_pass` cleanly. No confident lean — the premise that
38.4° sits "far from any known or suspected null," which licensed
native-sigma-only measurement there, is exactly what exp-094's own
Idealization-21 finding self-falsified; native-sigma-only readings at
38.4° are therefore no longer safe to trust alone, which is this item's
entire reason for existing.

**Informational, non-gating, every Rank:** `p_abs_w` (G/C) ratio expected
within 1–5% of unity, `ratio_abs_ext_raw` within ~1% of the T9 0.51
anchor, matching this program's own unbroken three-resolution record
(`cpl`∈{20,30,40}) that the coherent `delta_scene`/`ratio_k` channel swings
by 10×–20× while the energy channel never has. A deviation outside this
band at `cpl=50` specifically would be a genuine, previously-unexamined
surprise (Idealization 23-lineage, extended one resolution further), not
smoothed over.

## Estimated FDTD call count and wall-time budget (mandatory fix #9)

**If Rank 1 gate PASSES** (both Rank 1a and Rank 1c clear): Rank 1 (16) +
Rank 2 (36: 8+24+4) + Rank 3 (30, corrected: 6+24 — see "Disclosed
spec-resolution note") + Rank 4 (4, corrected) = **86 calls total**
(Phase-1/Red-Team's own stated figure was 72; corrected here per the
call-accounting fix above, angles/sigma/gating unaffected).
**If Rank 1 gate FAILS:** Rank 1 (16) + Rank 4 (4) = **20 calls total**
(Ranks 2/3 skipped).

This is well above this sub-thread's own established ~100–150 CPU-min
per-cycle band (mandatory fix #9) — disclosed, not silently inherited.
**CPU-minute model**, scaling from exp-094's own filed per-call rates
(2D-grid cost scales roughly with `RATIO³` — cells ~`RATIO²`, `STEPS`
~`RATIO`):

- Rank 1 (16 calls, `cpl=40`, `STEPS`=5600): exp-094's own Rank 1b rate
  (191.4 CPU-min / 24 calls ≈7.975 CPU-min/call) → 16 × 7.975 ≈**127.6
  CPU-min** (Rank 1a's own 8 calls ≈63.8 CPU-min of this; Rank 1c's own
  new 8 calls add the other ≈63.8 CPU-min, per mandatory fix #9's own
  request to itemize the +12-call increment precisely: Rank 1c alone
  ≈8×7.975≈**63.8 CPU-min more** than the Phase-1 draft's 8-call Rank-1
  figure).
- Rank 2a+2b+2b-native (36 calls, `cpl=50`): exp-094's own `R4` Rank-1
  rate (271.1 CPU-min / 32 calls ≈8.47 CPU-min/call) scaled by
  `(2.5/2.0)³≈1.953` ≈16.54 CPU-min/call → 36 × 16.54 ≈**595.3 CPU-min**
  (the 4 new Rank-2b-native calls alone ≈4×16.54≈**66.2 CPU-min more**
  than the Phase-1 draft's 32-call Rank-2 figure — matching mandatory
  fix #9's own request for a precise, non-hand-waved figure).
- Rank 3 (30 calls, corrected count, `cpl=40`, `STEPS`=5600): ≈8.0
  CPU-min/call ≈**240 CPU-min** (18-call Phase-1 figure ≈144 CPU-min;
  the +12 calls from the disclosed spec-resolution fix add ≈96 CPU-min
  more).
- Rank 4 (4 calls, corrected count, `cpl=30`): exp-094's own Rank-2 rate
  (13.5 CPU-min / 4 calls ≈3.4 CPU-min/call) ≈**13.6 CPU-min**.

**Total ≈976.5 CPU-min (≈16.3 CPU-hours) if Rank 1 passes; ≈141.2 CPU-min
if it fails** (FAIL-path total = Rank 1's 127.6 + Rank 4's 13.6 ≈141.2
CPU-min — Ranks 2/3 skipped entirely). At 4
workers: wall ≈(1.15×976.5)/(4×0.98) ≈**286.3 min (≈4.8h)** on the PASS
path, ≈**41.4 min** on the FAIL path — both model estimates; this
program's own unbroken track record (every T28 cycle's actual wall time
has landed under its own model estimate) makes the PASS-path figure a
conservative upper bound, not an expected value. This is disclosed,
reconciled against mandatory fixes 4–6 (Rank 2's rescoped,
necessary-but-insufficient evidentiary weight) rather than presented as
an unqualified "largest cycle to date" without comment — matching
mandatory fix #9's own requirement.

## T1 escape route

**N/A** — independently re-verified against LOGBOOK.md's own record: every
T28 sub-thread entry from Iteration 46 through Iteration 71 states T1
route N/A / Checkpoint criterion 2 N/A. This cycle takes no position on
σ(I)/σ(x,t)/angular selectivity/sub-threshold operation, makes no
phenomenon-mechanism claim, and does not touch `REALIZABILITY_MEMO.md`.
Matching every T28 desk/instrument cycle since exp-069, this is
INSTRUMENT-VALIDATION work: a ground-truth control on a measurement
family, a resolution-convergence probe, and a confound-disentangling
check on an existing near-null window — not a claim about any material or
mechanism.

## Realizability bound

**N/A**, for the identical reason. `REALIZABILITY_MEMO.md` is not opened,
cited, or re-scored.
