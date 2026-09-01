# exp-099 — Null C Wider-Bracket Re-Test, R5's First Real Spend
(Ground-Truth-Gated), and the GP2′/`ptp` Tail Reconciliation

*Panel Iteration 76. Lead seat (rotation): THERMODYNAMICS. Director synthesis
of `phase1_proposal.md` (THERMODYNAMICS) after five blind Phase-2 critiques
(PHOTONICS, MATERIALS, ELECTROMAGNETISM, QUANTUM OPTICS, VISION SCIENCE —
unanimous support-with-changes) and Red Team's Phase-2 audit
(PROCEED-WITH-MANDATORY-FIXES, 9 numbered attacks, 0 critiques overridden,
1 new defect found independently by Red Team itself). Executes exp-098's
own Reconciled Iteration-76 queue items 1–3 (item 4, ratifying R19, already
done; item 5 given a reasoned disposition, not a silent seventh N/A).*

## Hypothesis

This is a T28 house-discipline/validation cycle, not a new T1 escape-route
proposal — continuing exp-096/097/098's own adaptation of the Phase-1/3
format. Three independent questions:

1. **Is Null C's current NO-SIGN-CHANGE verdict (exp-098, ±0.500° symmetric
   bracket) real, or an artifact of the same bracket-mis-sizing failure mode
   item (ii) already proved can hide a genuine crossing?** A wider,
   asymmetric, R17-compliant bracket, justified against Null C's own
   established cpl20→cpl30 shift, tests this — with a falsifiable
   VANISHING-AMPLITUDE outcome pre-registered as a live third possibility,
   not merely "try wider."
2. **Does the cpl=50 (R5) family — built four cycles ago (Iteration 72,
   exp-095) and never once spent — reproduce the known cpl20→cpl30→cpl40
   downward migration at Null B on a genuine third resolution point?** Red
   Team's Phase-2 audit found this is R5's first real FDTD spend in this
   program's history, and mandated it be gated by machinery this cycle
   actually validates at R5's own resolution first (a fault-injection
   re-scoring of the registration gate, plus a far-from-null ground-truth
   sign check) — not merely inherited, untested, from R3/R4.
3. **Does GP2′'s own non-recovering 74°–89.5° tail match or diverge from
   exp-086's independently-computed `ptp` sliding-window statistic over the
   same closed-form model**, extended for the first time past its own
   previous 77° edge?

Nothing below re-proposes any RULED-OUT idea (R1–R19 read in full, confirmed
independently by Red Team as well as five blind critiques).

## Changes from Phase 1, per Red Team's Phase-2 audit (9 attacks; 7
mandatory fixes ADOPTED in full; 2 non-blocking ADOPTs; 0 REJECT-level
defects; 0 critiques overridden)

Director's ruling: Red Team independently re-verified every load-bearing
claim in all five blind critiques against source before ruling (Null C's
filed `delta_scene` values and interval-slope ratios, Null B's Richardson
figures, R5's zero-call history, the registration gate's `family="R4"`
hardcoding, the `xi_ext`/`sigma_abs_nonneg` assert line numbers, the
established `delta_scene` period) — none of the seven fixes below rest on
the critiques' word alone, and Red Team additionally caught one load-bearing
defect (Attack 4) that all five blind seats missed.

1. **Item 2 — fault-injection ground-truth on the registration gate itself
   (QUANTUM's fix, Attack 1, ADOPTED, ESCALATED to mandatory).** Confirmed
   at source: every fault-injection scenario in
   `experiments/097-.../run.py` (`pc`/`fia`/`fib`/`fic`/`fid`/`fi_e`/`fi_f`/
   `fi_h`) is hardcoded `family="R4"` (or, for `fi_h`, mislabels an R3
   point). Zero fault-injection coverage has ever existed at `family="R5"`.
   R5's own two `REPRESENTATIVE` points (41.825°/41.850°) are scored only in
   clean mode. **Fix**: re-run the positive-control + FI-A/B/C/D idiom (cpl
   swap, angle mislabel, sign flip, wrong taper edge) AND Check 6's FI-E/F/H
   idiom (index swap, cpl corruption, family mislabel), all at
   `family="R5"`, zero marginal FDTD cost (every check stops before
   `sim.run()`). Runs first, before any real R5 spend.
2. **Item 2 — one far-from-null R5 ground-truth sign check (MATERIALS' fix,
   Attack 2, ADOPTED, mandatory).** R15's addendum (Iteration 71, already on
   the books — NOT this cycle's founding instance) requires a new resolution
   family reproduce an already-known-correct sign at a robust, far-from-null
   angle before its interior-near-null readings are trusted. **Fix**: spend
   4 real R5 calls at **θ=36.0°** — confirmed ≥1° from all four established
   cpl=20 nulls (nearest: 37.127246°, distance 1.127°) — where
   `experiments/094-.../results.json::rank3.per_theta["36.0"]` already
   established a robust, floor-clear, CONSISTENT-across-cpl20/30/40
   **negative** `delta_scene` sign (pulled at runtime from that file, never
   hand-typed). Gates Rank 2b: if R5's sign at 36.0° does not match, Rank 2b
   is reported UNINTERPRETABLE-PENDING-R5-GROUND-TRUTH-CHECK, not run.
3. **Item 2 — price the Rank 2a/2b/GT HALT outcome (EM's fix, Attack 3,
   ADOPTED, mandatory).** Confirmed at source: `cell_metrics_r5`'s
   `xi_ext`/`sigma_abs_nonneg` asserts (mirrored from `cell_metrics_r4`) can
   HALT before any sign reading exists, and Phase 1's own Predictions table
   priced no such outcome — the exact failure shape exp-098 itself hit one
   cycle ago (an uncaught assert crashing mid-run). **Fix**: an explicit
   predicted row for this outcome, below (§Predictions).
4. **Item 1 — correct the Null C "filed, reused" table's angle labels (Red
   Team's own finding, Attack 4, ADOPTED, mandatory — missed by all five
   blind critiques).** The two interior filed angles are
   **41.294201°/41.627601°** (the source-exact stored keys in
   `experiments/098-.../results.json::item_i.C.report`), not
   `41.294235°/41.627568°` as Phase 1's table stated — traced to source: the
   proposal recomputed these as `θ₀±1/6` (exact fraction) instead of reading
   `experiments/098-.../run.py`'s own literal-decimal offset
   (`θ₀−0.1667`/`θ₀+0.1667`), a 3.33×10⁻⁵° labeling error (the underlying
   `delta_scene` VALUES were correct; only the LABELS were wrong). **Fix**:
   corrected throughout below; Phase 4 code pulls these four rows directly
   from `results.json` by their actual stored keys, asserting the expected
   keys are present before use — never by a hand-typed label.
5. **Item 1 — widen the VANISHING-AMPLITUDE discharge condition (PHOTONICS'
   fix, Attack 5, ADOPTED, mandatory, with Red Team's period-figure
   correction).** The bare `r_i<0.5`-at-3-points criterion cannot
   distinguish true decay-to-zero from ordinary curvature approaching a
   trough of `delta_scene`'s own independently-established
   **2.9474°** period (`LOGBOOK.md`, `R²=0.8582` fit — Red Team's correction
   from the proposal's cited `P_edge_A=2.8421°`, a related but distinct
   figure from a different config comparison). **Fix**: VANISHING-AMPLITUDE
   may be reported only if the tested half-width from θ₀ ALSO reaches
   ≥2.9474°. This cycle's own bracket (half-width 1.500°, ~51% of the
   period) does **not** reach this bar — disclosed explicitly below, not
   discovered as a surprise in Result: the achievable outcome set this cycle
   is SIGN-CHANGE-FOUND, INCONCLUSIVE-CONSISTENT-WITH-SAME-LOBE-OSCILLATION
   (amplitude criteria met, period criterion not), or
   INCONCLUSIVE-AT-THIS-WIDTH (neither clean pattern) — a clean
   VANISHING-AMPLITUDE verdict is not reachable at this width, full stop.
6. **Item 1 — correct θ₀'s citation (VISION's fix, Attack 6, ADOPTED,
   mandatory, folded into the same corrective pass as Fix 4).** Corrected to
   the source-exact **41.46090139413461°** (the proposal's own citation had
   an extra hand-inserted "1" digit, physically negligible at 2.5×10⁻⁷° but
   a literal R4-discipline violation). Re-verified by direct recomputation
   that the three new-bracket angles use the SAME literal-decimal-offset
   convention as `experiments/098-.../run.py` (not the exact-fraction
   convention that produced Attack 4's defect): θ₀+0.8333/+1.1667/+1.500 =
   **42.294201°/42.627601°/42.960901°** — internally consistent with the
   corrected filed-table labels (Fix 4), confirmed no second instance of the
   labeling-convention mismatch.
7. **§4 — duplicate the idealizations banner (VISION's fix, Attack 7,
   ADOPTED, mandatory).** Banner sentence now physically duplicated inside
   §Predictions' own body (below), not only in §Idealizations' closing
   paragraph — matching exp-098's own established fix (Iteration 75).

Non-blocking, adopted as wording only (Red Team's Attacks 8–9): item 5's
disposition (below) now states the cpl-orthogonal-to-realizability finding
using the words "realizability"/"orthogonal" explicitly (MATERIALS'
secondary note); item 3's Result-section framing will avoid "monotonic"
language for the 74°–77° tail given a small (~0.3%) non-monotonic uptick at
θ=74.5° vs. θ=74.0° already on file (Red Team's own §0 check) — noted here
for Phase 4/Result, not a Predictions-table change.

## Setup

All FDTD calls below reuse, unmodified: `Sim`/`add_line_source`
(`lab/fdtd2d.py`), `r{4,5}_config()`/`R{4,5}_CONFIGS`
(`experiments/069-.../design_geometry.py`), `cell_metrics_r4`/`run_block_r4`
(`experiments/094-.../run.py`), `cell_metrics_r5`/`run_block_r5`
(`experiments/095-.../run.py`), `pair_metrics_full`/`netd_row()`
(`experiments/093-.../run.py`), the registration-readback gate
`run_checks_1234_and_7`/`check6_positional_and_cpl`/`check6_set_membership_OLD`
(`experiments/097-.../run.py`, imported never edited), and
`richardson_style_diagnostic()`/`FastEval`/`find_sign_change`
(`experiments/098-.../run.py`, `experiments/085-.../phase4_derivation.py`).
λ=600nm (2D TMz) only, matching Idealization 1. No new machinery is built —
every fix above reuses existing functions with new arguments.

### Item 1 — Null C re-test: wider, asymmetric, R17-compliant bracket — 12 new calls

θ₀ = **41.46090139413461°** (`experiments/090-.../results.json::
q8.crossings_deg[3]`, corrected per Fix 6). Filed (reused, not rebuilt),
corrected labels per Fix 4:

| θ (cpl=40, filed) | `delta_scene` |
|---|---|
| 40.960901° (θ₀−0.500°) | +2.471869×10⁻³ |
| **41.294201°** (θ₀−0.1667°) | +1.512684×10⁻³ |
| **41.627601°** (θ₀+0.1667°) | +5.854146×10⁻⁴ |
| 41.960901° (θ₀+0.500°) | +4.704114×10⁻⁴ |

Interval-slope-decay ratio (Idealization 53's own criterion): `r₃ =
|Δ₃|/|Δ₂| = 0.1240` (an ~8.06× drop) — the deceleration signature motivating
this re-test.

**New bracket** (literal-decimal offsets, matching
`experiments/098-.../run.py`'s own convention exactly — Fix 6):
**42.294201° (θ₀+0.8333°), 42.627601° (θ₀+1.1667°), 42.960901°
(θ₀+1.500°)**. Upward half-width 1.500° — a margin of 3.98× over Null C's
own larger established cpl20→cpl30 shift (0.376752°) and 4.69× over the
smaller (0.320166°), both pulled from
`experiments/092-.../results.json::rank1.crossing_report`. No new downward
points (the filed data shows monotonically growing magnitude toward lower
θ, with no deceleration on that side; Null C's own established shift
direction is upward on both branches).

Family: `R4` only, both legs (`C40_R4`/`G40_R4`), both conditions
(empty/article). **3 angles × 2 legs × 2 conditions = 12 `sim.run()`
calls.** Plus 6 zero-cost registration-readback preflight checks (3 angles
× 2 config keys).

**Pre-registered outcome trichotomy, widened per Fix 5:**
- **SIGN-CHANGE-FOUND**: `delta_scene` crosses zero anywhere in the 3 new
  points.
- **VANISHING-AMPLITUDE**: reachable only if `delta_scene` stays strictly
  positive, floor-clear, every new `r_i<0.5`, **AND** the tested half-width
  (1.500°) reaches ≥2.9474° — it does not, so this outcome is **not
  reachable this cycle** (disclosed now, not discovered in Result).
- **INCONCLUSIVE-CONSISTENT-WITH-SAME-LOBE-OSCILLATION**: the amplitude
  criteria (positive, floor-clear, `r_i<0.5`) are met but the period
  criterion is not (i.e., the realistic best case this cycle can produce if
  the decelerating trend continues cleanly).
- **INCONCLUSIVE-AT-THIS-WIDTH**: neither clean pattern holds (e.g. further
  deceleration without a clean geometric-decay signature, or reversal
  without crossing zero).

### Item 2 — cpl=50 (R5) family: first real spend, ground-truth-gated — 28/12 calls (PASS/HALT-path)

**Confirmed zero R5 real-FDTD history**: `experiments/095-.../results.json`:
`rank2_calls=0`, `rank2.skipped=true` ("Rank 1 combined go/no-go gate did
not PROCEED"). R5 machinery (`dg.R5_CONFIGS`, `PAIR_KEYS_R5=("C40_R5",
"G40_R5")`, `SIGMA_R5_CORRECTED=0.2`, `dg.R5_STEPS`/`dg.R5_STEPS_STRESS`) is
fully built and statically gate-verified but has never spent a real call.

**Step 0 — fault-injection re-scoring at `family="R5"` (Fix 1, zero marginal
FDTD cost, runs first).** Positive control + FI-A(cpl swap)/FI-B(angle
mislabel)/FI-C(sign flip)/FI-D(wrong taper edge), all at θ=41.825°,
`config_key="C40_R5"`, `cpl_intended=50` — mirroring `experiments/097-.../
run.py`'s own R4 idiom exactly, substituting `family="R5"`. Plus Check 6's
FI-E(index swap)/FI-F(cpl corruption)/FI-H(family mislabel) idiom, reusing
the existing R5 `REPRESENTATIVE` point (`notes_line=476`,
θ∈{41.825°,41.850°}). **0 `sim.run()` calls** — every check stops before
`.run()` is invoked. HALTs item 2 entirely if any scenario reads the wrong
outcome (a real defect scored CLEAN, or a clean case scored DEFECT-FOUND).

**Step 1 — far-from-null ground-truth sign check (Fix 2), 4 calls.**
θ=**36.0°** (≥1° from every established cpl=20 null; nearest is 37.127246°,
distance 1.127°). Reference sign pulled at runtime from
`experiments/094-.../results.json::rank3.per_theta["36.0"].delta_scene`
(established negative, CONSISTENT across cpl=20/30/40) — never hand-typed.
Family `R5` only, both legs, both conditions: 2×2 = **4 `sim.run()`
calls**, plus 2 zero-cost registration preflight checks (1 angle × 2 keys).
Gates Step 3 (Rank 2b): if the R5 sign at 36.0° does not match, Rank 2b is
skipped and reported UNINTERPRETABLE-PENDING-R5-GROUND-TRUTH-CHECK.

**Step 2 — Rank 2a, settling precondition (unchanged from Phase 1), 8
calls.** θ=**39.854853°** (coincides with one Rank 2b interior angle, matching
exp-095's own precedent `RANK2A_ANGLE ∈ RANK2B_ANGLES`). `dg.R5_STEPS`
vs. `dg.R5_STEPS_STRESS`, both legs, both conditions: 2×2×2 = **8
`sim.run()` calls**, plus 2 zero-cost preflight checks. Gate: `settle_band`
on `rel_dev = |Δdelta_scene(R5_STEPS_STRESS, R5_STEPS)| /
|delta_scene(R5_STEPS)|` — PASS ≤1%, CAUTIONARY-PASS ≤10%, HALT >10%. Runs
unconditionally (not gated on Step 1), per Red Team's own budget
arithmetic (28/12 — see below).

**Step 3 — Rank 2b, interior sweep, 4 angles, 16 calls, gated on BOTH Step 1
(GT sign match) AND Step 2 (not HALT).** Asymmetric bracket around
θc40=**39.921519316666°** (`experiments/098-.../results.json::
item_i.B.crossing_cpl40`), weighted toward lower θ (Null B's own doubly-
confirmed downward marginal-shift direction, 20→30 AND 30→40 both negative):

| θ (cpl=50, new) | Offset from θc40 |
|---|---|
| 39.521519° | −0.400° |
| 39.688186° | −0.233° |
| 39.854853° | −0.067° (= Step 2's angle) |
| 40.021519° | +0.100° |

Family `R5` only, both legs, both conditions: 4×2×2 = **16 `sim.run()`
calls**, plus 8 zero-cost preflight checks.

**Item 2 budget, self-checked**: Step 1: 2×2=4. Step 2: 2×2×2=8. Step 3
(conditional): 4×2×2=16. **PASS-path (both gates clear): 4+8+16=28.
HALT-path (either gate fails, Step 3 skipped): 4+8=12.** Matches Red Team's
own stated 28/12 exactly.

If a genuine cpl=50 crossing θc50 is found in Step 3: `shift_40_50 = θc50 −
θc40`; `richardson_style_diagnostic(shift_20_30=shift_30_40,
shift_30_40=shift_40_50, cpl20=30, cpl30=40, cpl40=50)` (the corrected,
Phase-5-verified function, imported unmodified, relabeled positionally for
the 30/40/50 triple exactly as its own docstring permits;
`naive_order2_ratio=(40/50)²=0.64` in this relabeling). If no crossing is
found, no Richardson figure is computed.

### Item 3 — GP2′/`ptp` reconciliation through 74°–89.5° — 0 new FDTD, 155 new zero-FDTD evaluations

**Current `ptp` coverage, confirmed at source**:
`experiments/086-.../phase4_rescore_results.json::method_c_rescore.sub_results`
— `theta_centers = np.arange(5.0, 77.0+1e-9, 2.0)`, 37 windows, each
`sub_theta = np.round(np.arange(θc−3.0, θc+3.0+1e-9, 0.2), 6)` (31 points, 6°
wide) — θ-coverage reaches only [2.0°, 80.0°]. Peak `ptp=1.695985` at
θc=69° (6630.99× the θc=5° reference); recovers to 311.10×/621.44× by
θc=75°/77° (a small, non-monotonic ~0.3% uptick at θ=74.5° vs. 74.0°, not a
clean monotonic decline — Red Team's own correction, non-load-bearing).

**Extension, method reused verbatim** (same `FastEval`, same
`theta_centers`/`sub_theta` construction, same `ptp_sub = float(np.ptp(c_sub))`
— no new statistic): θc ∈ **{79°, 81°, 83°, 85°, 87°}**, 5 new windows,
window coverage reaching θ=90° (θc=87° spans [84°,90°]), past GP2′'s own
89.5° edge. **5×31 = 155 new zero-FDTD `FastEval.curve()` evaluations.**

**Scoping the severity gap** (unchanged from Phase 1): GP2′'s worst ratio,
235.396× at θ=66.0° (`experiments/098-.../results.json::item_v.gp2_curve`),
vs. exp-086's 6630.99× at θc=69° — both read the identical closed-form
curve, so the ~28× gap is a statistic/reference choice, not a different
physical measurement. GP2′'s own 74°–89.5° tail (32 points, 0.5° step) shows
zero VALID points, declining from 78.283×(θ=74.0°)/78.534×(θ=74.5°) to
12.222× (θ=89.5°), never recovering to VALID (≤10×). Falsification
criterion (Idealization 56): if the new θc=79°–87° `ptp` values continue
exp-086's own established recovery trend toward a low order (comparable to
the θc=5° reference) OVER THE SAME range where GP2′ stays elevated and
non-recovering — a persistent SHAPE divergence, not just a magnitude one —
that indicates the statistic choice alone does not fully explain the gap.
If the extended `ptp` values ALSO stay persistently elevated through 87°,
that supports "one underlying curve, viewed two ways, fully accounts for
the gap." No confident lean stated.

## Idealizations

**Carried forward** (exp-096/097/098, cited by number, unchanged): 1 (2D
TMz, 600nm only), 7 (no constraint-1/2/3/4 test executed this cycle — see
§T1 disposition below), 17 (R3/R4/R5 share one mechanical recipe), 38/39/42
(Check 5 has never tested any `G40_*` padded config), 46 (a 4-point/6-point
quartile bracket localizes a sign change, does not certify absence outside
the tested span), 49 (any Richardson-style figure is explicitly
descriptive, no continuum reference value exists).

**Carried from Phase 1, renumbered as this cycle's own (53–57, unchanged in
substance)**: 53 (VANISHING-AMPLITUDE is a finite-sample inference, cannot
distinguish a true asymptote from a crossing just beyond the tested span at
comparably small amplitude — now additionally bounded by Fix 5's period
requirement, which this cycle's own bracket does not reach); 54 (Null B over
θ₀≈38.590230° is a resource-allocation choice, not a physical-interest
claim); 55 (Rank 2b's asymmetric bracket assumes the downward marginal-shift
trend continues 40→50; if not, a true crossing could sit outside the tested
span); 56 (`ptp` and `ratio_to_ref` are not interchangeable measures — a
match or mismatch is informative either way, not a proof of identity); 57
(GP2′ and `ptp` both evaluate one closed-form model, not new FDTD
measurements — item 3 compares two statistics on one model, not two
physical instruments).

**New this cycle:**

58. Item 2's Step 0 fault-injection re-scoring validates the registration
    gate's construction-time wiring logic at R5's resolution; it does NOT
    itself validate that R5's physical FDTD output (grid dispersion,
    boundary placement, taper discretization) reproduces the correct
    continuum answer — that is Step 1's (the ground-truth sign check's) own,
    narrower, separate job, and neither substitutes for a full R3-style
    resolution-convergence sweep at R5 (still not run anywhere in this
    program's history).
59. Step 1's single far-from-null angle (36.0°) establishes sign-agreement
    at ONE point; it does not certify R5's construction is defect-free at
    every angle, only that the specific class of registration/construction
    defects R18's fault-injection idiom + this sign check target are absent
    at this one point.
60. Fix 5's period-based VANISHING-AMPLITUDE bar (≥2.9474°) means this
    cycle's own item 1 design, even if every amplitude criterion is met
    cleanly, can at best report INCONCLUSIVE-CONSISTENT-WITH-SAME-LOBE-
    OSCILLATION — a genuinely wider bracket (≥2.9474° half-width) is now a
    named, explicit candidate for a future cycle if this branch is hit, not
    an open-ended "try wider again."
61. Item 3's θc=87° window spans [84.0°,90.0°] — its own upper edge sits
    0.5° past GP2′'s own 89.5° edge, so point-coverage is not the gap; the
    scope note is that `ptp` at θc=87° characterizes VARIATION across that
    6°-wide window, not a value AT 89.5° specifically (GP2′'s own unit of
    comparison), so the two curves' comparison at the extreme tail is
    still a windowed-statistic-vs-point-value comparison, per Idealization
    57 — not a new gap, a restatement of that same scope note at the new
    edge.

**Carried idealizations banner: every prediction in this section
(§Predictions) is governed by Idealizations 1/7/17/38/39/42/46/49/53–61.**

## §T1 escape-route disposition (item 5, THERMODYNAMICS' own Phase-1
ruling, ratified by Red Team without attack — non-blocking Attack 8 only
asked for explicit wording, adopted)

**No new escape-route mechanism is proposed this cycle — Checkpoint
criterion 2 (T1 position) is N/A, the seventh consecutive cycle.** This
seat's own disposition (Phase 1, unattacked at Phase 2): items 1–3 are
house-discipline/instrument-trust work on the evidentiary basis for an
already-committed escape route (angular selectivity); none proposes a new
mechanism to map. **The cpl-is-orthogonal-to-realizability finding, stated
explicitly (MATERIALS' non-blocking wording fix)**: `cpl` is confirmed
purely a grid-density/numerical-resolution parameter (`CPL={R3:30,R4:40,
R5:50}`), with physical geometry (`L_GEOMETRIC_M`) held invariant to 1e-12
across R3/R4/R5 — it carries zero realizability content of its own; the
realizability bound MATERIALS' charter owns remains entirely un-addressed
by any cpl-indexed work in this seven-cycle run, and is orthogonal to it.
**Explicit trigger, restated**: once items 1–3 close, Iteration 77's queue
should include an actual constraint-1/2/3/4 scoring pass treating the
now-more-fully-characterized `delta_scene(θ)` sign structure as an
angular-selectivity parameter, scored against the existing constraint-metric
instruments — not another round of bracket/instrument validation on the
same underlying evidence. If Iteration 77 also files T1: N/A without
addressing this trigger, this seat's own disposition should be read as
overridden, not reaffirmed by default.

## Predictions (frozen before any Phase-4 code exists)

**Carried idealizations banner (duplicated here into the Predictions
section body itself, per Fix 7 — VISION SCIENCE's own finding): every
prediction below is governed by Idealizations 1/7/17/38/39/42/46/49/53–61
(§Idealizations above).**

| Item | Metric | Predicted band / criterion | Confident lean? |
|---|---|---|---|
| (1) | `delta_scene` sign, 3 new Null C points | Four-way outcome per the widened trichotomy above (§Setup item 1): SIGN-CHANGE-FOUND / INCONCLUSIVE-CONSISTENT-WITH-SAME-LOBE-OSCILLATION / INCONCLUSIVE-AT-THIS-WIDTH; VANISHING-AMPLITUDE is not reachable this cycle (Fix 5). No confident lean — genuinely open. |
| (1) | `floor_pass` | All 3 new angles clear `FLOOR_FRAC=0.10` (matching every filed R4-family point to date, zero exception on file). Confident lean: **PASS**. |
| (2) Step 0 | Fault-injection re-scoring at `family="R5"` | Confident lean: **all_as_predicted=True** — positive control CLEAN/CLEAN, FI-A/B/C/E/F/H each DEFECT-FOUND on the corrupted channel and CLEAN elsewhere, FI-D CLEAN(1234)/DEFECT-FOUND(7) — matching every prior family's own fault-injection idiom on file, zero exception to date. If ANY scenario reads unexpectedly, item 2 HALTS entirely (priced explicitly, Fix 3's own spirit extended to Step 0). |
| (2) Step 1 | R5 sign at θ=36.0° | Confident lean: **matches established negative sign** (R3/R4 both CONSISTENT here per exp-094) — but stated as a lean, not a certainty: this is R5's first-ever real measurement at any angle, and Idealization 59 disclaims certifying construction-defect-free beyond this one point. |
| (2) Step 1/2 | `xi_ext`/`sigma_abs_nonneg` asserts, both steps | No confident lean (Fix 3, EM's own priced outcome) — HALT is a live, disclosed possibility, not assumed away. If it fires, item 2 stops at 4 (Step-1-only) or 12 (Step-1+2) calls, reported as such. |
| (2) Step 2 | `settle_band(rel_dev)` at 39.854853° | Weak lean toward **PASS** (≤1%) given every prior R4-family settling-adjacent check's negligible sensitivity — but this is R5's own first real settling check ever, so stated as a lean only. |
| (2) Step 3 | `delta_scene` sign, 4 interior cpl=50 points (gated) | Genuinely open — no confident lean. If a crossing is found, `shift_40_50` is expected (not certain) to carry the same (negative) sign as Null B's two already-established shifts, per Idealization 55. |
| (2) | Richardson diagnostic (30/40/50 triple), IF a Step-3 crossing is found | No confident lean on the observed ratio's value — the open question this item exists to answer. |
| (3) | Extended `ptp`, θc∈{79°,81°,83°,85°,87°} | Weak lean toward continued decline from the θc=77° value (621.44×), given the post-peak decay visible from θc=69°→77° — but whether it reaches a low order (genuine recovery) or plateaus elevated (GP2′-like non-recovery) is the open question. No confident lean on which. |
| (3) | Severity-gap attribution (shape match/mismatch over 74°–87° overlap) | No confident lean stated in advance — falsifiable per the criterion in §Setup item 3. |

**Total FDTD-call budget, self-checked:**
- Item 1: 3 × 2 × 2 = **12 calls**.
- Item 2, Step 1: 2 × 2 = **4 calls**. Step 2: 2 × 2 × 2 = **8 calls**. Step
  3 (gated): 4 × 2 × 2 = **16 calls**.
- Item 2 total: **PASS-path 4+8+16=28; HALT-path 4+8=12.**
- Item 3: **0 calls** (155 zero-FDTD closed-form evaluations).

**Grand total: PASS-path 12+28+0=40 `sim.run()` calls; HALT-path (item 2
gates fail) 12+12+0=24 calls.** Plus 6(item 1)+2(item 2 Step 1)+2(Step
2)+8(Step 3, if run)=18 zero-cost registration preflight checks, and item
2's Step 0 fault-injection re-scoring (0 `sim.run()`, ~9 new `Sim()`
constructions that never call `.run()`).

Wall-time estimate, scaling from exp-098's own 64-call/134.62-min pace
(≈2.10 min/call): **≈84 minutes** for the 40-call PASS-path total (≈50
minutes for the 24-call HALT-path floor); item 3's 155 closed-form
evaluations add well under 1 second.
