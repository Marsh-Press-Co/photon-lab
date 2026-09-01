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
calls.** θ=**39.854853°** (a hand-computed offset intended to match one Rank
2b interior angle, per exp-095's own precedent `RANK2A_ANGLE ∈
RANK2B_ANGLES` — **correction, Phase-5 Red Team audit mandatory fix #3**:
this is NOT literally identical to Step 3's own interior point, computed by
`run.py` as `θc40−0.067` in floating-point arithmetic — see the corrected
row below and §Result). `dg.R5_STEPS`
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
| 39.854853° → actual computed value **39.854519316666234°** | −0.067° (**correction, Phase-5 Red Team audit mandatory fix #3**: near, not equal to, Step 2's own 39.854853°; gap 3.3368×10⁻⁴°, since Step 2's angle is a hand-computed offset and Step 3's is `θc40−0.067` computed in floating point — see §Result) |
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
mechanism to map. **Correction, Phase-5 Red Team audit mandatory fix #4
(MATERIALS + QUANTUM OPTICS, independently) — two previously-conflated
claims, separated:**

1. **The `cpl`-resolution-knob-is-inert finding (newly verified THIS
   cycle)**: `cpl` is confirmed purely a grid-density/numerical-resolution
   parameter (`CPL={R3:30,R4:40,R5:50}`), with physical geometry
   (`L_GEOMETRIC_M`) `assert`-enforced invariant to 1e-12 across R3/R4/R5,
   extended to R5 for the first time this cycle. This specific fact is
   genuinely re-verified, not merely inherited.
2. **The tracked `delta_scene` feature's own realizability status (an
   inherited, still-genuinely-open ambiguity, NOT re-tested or reaffirmed
   this cycle or any cycle since Iteration 60)**: Iteration 59 adopted a
   "zero realizability content" framing rule for this PAD-toggled signal
   (`PAD` independently proven lossless vacuum, exp-076); Iteration 60's
   own Phase-5 text explicitly declined to reinstate it ("genuine
   ambiguity remains between two opposite-realizability readings"). That
   ambiguity has stood unresolved for 16 cycles (60→76) — it is NOT
   settled by fact 1 above, which concerns the resolution knob, not the
   feature. The realizability bound MATERIALS' charter owns remains
   entirely un-addressed by any cpl-indexed work in this seven-cycle run.
   **Per Red Team's Phase-5 audit, this ambiguity is why QUANTUM's
   PAD-vs-article partition (Iteration 77's §Next Tier 1) is a mandatory
   structural precondition, not an optional wording fix, before
   `delta_scene(θ)` is fed to any constraint-1/2/3/4 scoring pass.**

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

## Result

**Carried idealizations banner: this section is governed by Idealizations
1/7/17/38/39/42/46/49/53–61 (§Idealizations above) — restated here per
this program's own house discipline (VISION SCIENCE's originating fix,
exp-098).**

**Process note, disclosed (R4 discipline applied to this program's own
execution, not just its physics claims).** `run.py`'s first execution
this shift crashed at item 1's own interval-slope-decay computation
(`combined_delta_c[THETA0_C + 0.500]`, a `KeyError`) after item 1's 12
real FDTD calls had already completed and printed correctly — a freshly
computed float (`THETA0_C + 0.500`) does not bit-match the 6-decimal-
rounded key parsed from `experiments/098-.../results.json`'s own filed
string, so a direct-arithmetic dict lookup fails where the actual filed
key (`NULL_C_FILED_KEYS[3]`) succeeds. Fixed (pull the stored key,
matching this same document's own Fix 4 discipline: "never hand-type/
recompute") and the full script re-executed from scratch, per this
program's own exp-098 precedent for a mid-run defect caught before
`results.json` existed. **No data was lost or altered**: the two
executions' item 1 console output is bit-identical at all 7 combined
`delta_scene` values — **correction, Phase-5 Red Team audit mandatory fix
#5 (VISION SCIENCE)**: this comparison was performed in-session, by eye,
against the crashed run's own console capture visible in that turn's tool
output; it is **not independently re-auditable from the committed git
record** (checkpoint commit `d9f1006` stops at the launch banner, before
any of the crashed run's own item-1 per-theta lines were ever committed).
"Directly diffed" overstated the claim's own evidentiary status — the
values genuinely match, but a future reader cannot re-verify this from
`git log` alone, only from this document's own assertion. The defect was
confined to a downstream derived-statistic lookup, never the FDTD
measurements themselves. Logged
for Phase 5's attention (§Learned below): this is a different failure
shape than exp-098's own call-count arithmetic miss (Learned #1 there),
but the same underlying lesson — filed data must be read back by its
actual stored key/precision, never reconstructed by fresh arithmetic —
generalized to a second, distinct code location this cycle.

**40 real FDTD calls (the full PASS-path budget, exactly as the
self-checked table above priced it), 8899.4s (148.32 min) wall time**
(materially longer than the ≈84-minute scaled estimate — a container/
hardware timing difference, consistent with exp-098's own disclosed gap
in the same direction, not a physics finding). Trust suite reconfirmed
green (41/41, `--only 12346789`) both before this run and after this
cycle's full close; zero `lab/` diff throughout.

**Item 1 — Null C wider bracket: INCONCLUSIVE-AT-THIS-WIDTH**, the
predicted-reachable outcome this cycle's own Fix 5 correctly excluded
VANISHING-AMPLITUDE from. All 3 new points floor-clear
(`all_new_floor_pass=True`); no sign change anywhere across the combined
7-point span (4 filed + 3 new):

| θ | `delta_scene` |
|---|---|
| 40.960901° (θ₀−0.500°, filed) | +2.471869×10⁻³ |
| 41.294201° (θ₀−0.1667°, filed) | +1.512684×10⁻³ |
| 41.627601° (θ₀+0.1667°, filed) | +5.854146×10⁻⁴ |
| **41.960901° (θ₀+0.500°, filed) — the minimum** | **+4.704114×10⁻⁴** |
| 42.294201° (θ₀+0.8333°, new) | +1.322251×10⁻³ |
| 42.627601° (θ₀+1.1667°, new) | +2.456623×10⁻³ |
| 42.960901° (θ₀+1.500°, new) | +2.778079×10⁻³ |

The genuinely new finding: `delta_scene` does **not** continue
decelerating toward zero past θ₀+0.500° — it **reverses** and climbs
back up. **Correction, Phase-5 Red Team audit mandatory fix #2
(THERMODYNAMICS' own self-review)**: the ratio here is the code's own
`r_ratios[0]=|Δ₅|/|Δ₄|=1.332` (θ₀+0.833°→+1.167° step vs. θ₀+0.500°→+0.833°
step) — NOT `|Δ₄|/|Δ₃|` as originally labeled (that boundary-spanning
ratio, θ₀+0.500°→+0.833° vs. the last FILED interval θ₀+0.1667°→+0.500°,
is never computed by `run.py` at all; hand-computed for context here, it
is ≈7.41). `r_ratios[0]=1.332` (>1, growing, not the <0.5 decay Fix 5's
amplitude criterion needs) before decaying again on the next interval
(`r_ratios[1]=0.283`). `amplitude_criteria_met=False` on `r_ratios[0]` alone, so neither
clean pattern (crossing, or clean decay-to-plateau) holds — the data
describe a **smooth local minimum (trough) near θ₀+0.5°–0.83° with no
zero-crossing across this ±1.5° span**, not the "further deceleration"
or "reversal-without-crossing" the pre-registered
INCONCLUSIVE-AT-THIS-WIDTH bucket anticipated in the abstract, but a
concrete instance of it: this is a genuine bounce, not a stall. Whether
a true crossing sits beyond θ₀+1.5° (upward) remains untested
(Idealization 46).

**Item 2 — cpl=50 (R5) first real spend: every gate cleared, PASS-path
in full, 28/28 calls.**

- **Step 0** (fault-injection re-scoring, `family="R5"`, 0
  `sim.run()` calls): `all_as_predicted=True` — positive control clean,
  every corrupted scenario (FI-A/B/C/D via the exp-097 1234/7 idiom;
  FI-E/F/H via Check 6) caught (`caught_by_new=True` at all six),
  exactly matching every prior family's own idiom, zero exception.
- **Step 1** (ground-truth sign, θ=36.0°, R5, 4 calls):
  `delta_scene=−1.064305×10⁻³`, sign **negative**, matching the
  established R4-family reference at the same angle
  (`−8.776529×10⁻⁴`, `experiments/094-.../results.json`) —
  `sign_match=True`. R5's first-ever real measurement at any angle
  reproduces the correct sign at this one point (Idealization 59: this
  certifies nothing beyond that one point).
- **Step 2** (settling, θ=39.854853°, 8 calls): `delta_scene(R5_STEPS)
  =+5.253136×10⁻⁴`, `delta_scene(R5_STEPS_STRESS)=+5.243753×10⁻⁴`,
  `rel_dev=0.1786%` — well inside the ≤1% PASS band.
- **Step 3 gate**: both Step 1 (GT sign match) and Step 2 (not HALT)
  clear → **OPEN**, ran unconditionally-priced 16 calls.
- **Step 3** (interior sweep, 4 angles around θc40=39.921519°, 16
  calls): **SIGN-CHANGE-FOUND**, crossing at **θc50≈39.776870°**,
  bracket [39.688519°, 39.854519°]. **Correction, Phase-5 Red Team audit
  mandatory fix #3 (ELECTROMAGNETISM)**: Step 2's settling angle
  (39.854853°, a hand-computed offset) is NOT literally identical to
  Step 3's own nearest interior point (39.854519316666234°, computed as
  `θc40−0.067` in floating point) — the two differ by 3.3368×10⁻⁴°.
  Step 2's PASS is informative for the Step-3 bracket via smoothness (the
  two nearby points' `delta_scene` differ by only ~0.4%, `+5.230823×10⁻⁴`
  at 39.854519° vs. `+5.253136×10⁻⁴` at 39.854853°), not literal
  coincidence.

| θ (cpl=50) | `delta_scene` |
|---|---|
| 39.521519° | −1.667781×10⁻³ |
| 39.688519° | −5.951707×10⁻⁴ |
| 39.854519° | +5.230823×10⁻⁴ |
| 40.021519° | +1.597453×10⁻³ |

`shift_40_50 = θc50 − θc40 = −0.144649°` — **same (negative) sign** as
both established shifts (`shift_20_30=−0.150319°`,
`shift_30_40=−0.144649°`, note: exp-098's own filed 30→40 shift is
numerically coincidentally close to this cycle's fresh 40→50 shift,
confirmed distinct quantities read from distinct sources, not a
duplication bug — cross-checked against `results.json`'s own
`step3.theta_c40`/`crossing_cpl50` fields directly), confirming
Idealization 55's lean. **Richardson (30/40/50, corrected
marginal-to-marginal, descriptive only — Idealization 49):
observed_ratio=0.9623 vs. naive 2nd-order 0.64.** **Correction, Phase-5
Red Team audit mandatory fix #1 (PHOTONICS)**: this document's first
draft mis-cited exp-098's own Null-B Richardson figure (20/30/40) as
"observed 1.777 vs. naive 0.5625" and framed both together as a
"super-linear-growth pattern." `1.777` is exp-098's own retracted,
pre-correction number — exp-098's own currently-filed `results.json`
stores `observed_ratio=0.7765163757372424`, and exp-098's own NOTES.md
states explicitly that the corrected figure is `0.777` (**shrinking**,
same sign), not the originally-reported `1.777` (growing). The correct
comparison is **0.9623 (this cycle, 30/40/50) vs. 0.7765 (exp-098,
20/30/40) — both <1, both shrinking, not growing** — a materially more
reassuring reading than "super-linear growth": a shrinking
marginal-to-marginal pattern reproduced a second time, at a different
point-pair on the same feature (Null B), not a growing one. The
genuinely open question this correction surfaces (per QUANTUM OPTICS'
own Phase-5 review) is that the ratio is **climbing toward 1** across
the two data points (0.7765→0.9623), which could indicate either
genuine-but-slow convergence or a non-convergent recipe artifact
(Idealization 49) — this is the actual open question, not "growing
faster than 2nd order," and is queued as Iteration-77 Tier 1 item 3
(§Next).

**Item 3 — GP2′/`ptp` tail reconciliation, θc∈{79°,81°,83°,85°,87°}:
result does not cleanly support either falsification branch.**

| θc | `ptp` | ratio to θc=5° ref |
|---|---|---|
| 77° (filed) | 1.589445×10⁻¹ | 621.4× |
| 79° | 2.173539×10⁻¹ | 849.8× |
| 81° | 2.183528×10⁻¹ | 853.7× |
| 83° | 1.815694×10⁻¹ | 709.9× |
| 85° | 1.286959×10⁻¹ | 503.2× |
| 87° | 7.461436×10⁻² | 291.7× |

**Disclosed directly, not glossed over**: the predicted "weak lean
toward continued decline from θc=77°" **missed at the very next point**
— 77°→79° is an **increase** (621×→850×, +37%), well beyond the small
~0.3% 74°/74.5° uptick already on file and flagged as a caveat. From
79°→87° the trend **does** decline (850×→292×, a real ~66% drop), but
never approaches "low order" (θc=5°-reference-comparable, i.e. ~1×) —
it plateaus roughly an order of magnitude above the reference band
throughout, well short of recovery. Over the same θ≥74° range, GP2′'s
own (unchanged, re-read not recomputed) tail stays elevated
(12.2×–78.5×, `gp2_tail_any_valid=False`, zero VALID points). Both
curves show real decline in this range, in relative terms, but neither
reaches its own "recovered" regime by the tested edge — the
pre-registered falsification criterion does not resolve cleanly toward
either "one curve fully explains the gap" or "persistent, unexplained
shape divergence"; it is genuinely mixed, an honest non-resolution, not
a coin-flip default.

## Phase 5 corrections (same-shift, Red Team final audit — flagged per
R4/T10, not silently rewritten into the Result prose without a visible
trail)

All six blind Phase-5 reviews returned CONCUR-WITH-GAP(S); Red Team's
final audit independently re-verified every finding from source (not
taken on any reviewer's word) and ADOPTED all six in full, plus a
cross-review synthesis finding of its own (§2 below). None changes a
PASS/FAIL classification, a crossing value, or a scored verdict already
on file — all six are zero-FDTD, documentation-only prose/label
corrections, applied inline above (§T1 disposition, §Result, §Learned,
§Next) with explicit "**Correction, Phase-5 Red Team audit mandatory fix
#N**" markers at each site, never silently rewritten. Full detail:
`phase5_redteam_audit.md`.

1. **Richardson mis-citation (PHOTONICS, adopted)** — exp-098's own
   retracted `1.777` figure was cited instead of the corrected, currently
   filed `0.7765163757372424`; the qualitative story inverts from
   "super-linear growth" to "shrinking, twice." §Result, §Learned #4.
2. **r-index mislabel (THERMODYNAMICS' own self-review, adopted)** —
   `r₄=|Δ₄|/|Δ₃|=1.332` mislabeled a ratio the code never computes; the
   value is actually `r_ratios[0]=|Δ₅|/|Δ₄|`. §Result.
3. **False settling-angle "coincidence" (ELECTROMAGNETISM, adopted)** —
   Step 2's hand-computed 39.854853° is not literally identical to Step
   3's own floating-point-computed interior point (39.854519316666234°,
   a 3.3368×10⁻⁴° gap); Step 2's PASS informs Step 3 via smoothness, not
   exact coincidence. §Setup, §Result.
4. **T1-disposition conflation (MATERIALS + QUANTUM OPTICS, independently
   convergent, adopted)** — the newly-verified "`cpl` knob is inert"
   fact and the inherited, still-unresolved "tracked feature has zero
   realizability content" claim (Iteration 59, not reaffirmed at
   Iteration 60) were stated as one settled finding; separated. Elevates
   QUANTUM's PAD-vs-article partition from recommendation to mandatory
   Iteration-77 precondition. §T1 disposition.
5. **Unauditable "directly diffed" claim (VISION SCIENCE, adopted)** —
   the KeyError bugfix's crashed-vs-rerun comparison was performed
   in-session, by eye, and is not reconstructible from the committed git
   record (`d9f1006` stops before any item-1 output); scoped accurately.
   §Result.
6. **Word-count cap (VISION SCIENCE, adopted, process-only)** — 3 of 5
   Phase-2 critiques exceeded PANEL.md's 150-word cap, uncaught by Red
   Team's own Phase-2 audit; no text change to this document, flagged for
   Phase-2 discipline going forward.

**New synthesis (Red Team's own §2, cross-review)**: this single document
carries FIVE separate instances of the identical "claimed-exact
figure/citation/label that does not reproduce from source" defect shape
across its lifecycle — two caught pre-freeze at Phase 2 (θ₀'s digit
insertion; the interior-angle label mismatch), three more (#1–#3 above)
surviving into the frozen Result/Learned sections, uncaught until Phase
5. **New standing rule, ADOPTED NOW (R20)**: three or more independent
R4-class defects surviving a document's own Phase-3 freeze into its
Result/Learned sections, each caught only at Phase 5, constitutes a
Checkpoint-4-grade recurrence pattern on its own — a future cycle
exhibiting this density fires Checkpoint criterion 4 automatically. Does
not fire on its own founding instance (this cycle), matching every prior
R-rule's precedent. R20 also folds in Learned #1's own KeyError pattern
(a citation failure inside code, not prose — same root cause, one rule).
Logged to `LOGBOOK.md` this shift.

**Checkpoint criterion 4 ruled the closest call this program's R4
lineage has had, but does NOT fire**: every defect above was caught
blind, within this same cycle's own six-seat-plus-Red-Team review
process, before this LOGBOOK entry — matching the R16/R17/R18/R19
non-firing precedent. R19 itself (call-count vs. row-count) was
independently confirmed correctly honored this cycle (40 calls map to a
fully cross-checked job list, zero conflation). **All five checkpoint
criteria: do not fire** (1/2 N/A — no new T1 mechanism proposed; 3 N/A —
zero engine physics beyond the validated bench classes; 5 N/A — genuine
logbook-advancing content this cycle).

**Combined Verdict: PROMISING** (Red Team's final ruling). Item 2 — R5's
first-ever real FDTD spend in this program's 76-iteration history — is a
genuine methodological milestone: the first resolution family in this
sub-thread's entire history to clear a far-from-null ground-truth sign
check AND a full fault-injection re-scoring BEFORE its first
interior-near-null reading was trusted, rather than earning that
discipline only retroactively (R3 and R4 both did). All three gates
cleared cleanly; Step 3 delivered a genuine, cleanly-bracketed sign
change plus a second independent (and, corrected, reassuring) Richardson
data point at Null B. Item 1's "bounce" and item 3's honest non-
resolution are both disclosed as such, not smoothed into false
confidence — PHOTONICS' own Attack-5-derived period gate (Fix 5) is
empirically vindicated by the result it correctly barred. Weighed against
this: the five-instance R4-class defect density (why R20 exists), a
second-consecutive-cycle instance of the "filed data reconstructed, not
read back" root cause in a new code location, and one unauditable
verification claim — none individually load-bearing to any scored
verdict, but a real, non-blocking drag on this cycle's own record-keeping
quality. **All three item-level outcomes stand as computed and are not
disputed by anything in this audit.**

## Learned

1. **A second, distinct instance of "filed data reconstructed by fresh
   arithmetic instead of read back by its stored key/precision" broke a
   run this cycle** (the `KeyError`, above) — a different failure shape
   than exp-098's own call-count arithmetic miss (that Learned #1), but
   the same root lesson, now demonstrated twice in two consecutive
   cycles across two different code patterns. Neither instance survived
   past `run.py`'s own execution (both were caught before
   `results.json` existed), but neither was caught by the panel's
   review layers either — this cycle's bug lives entirely inside code
   that did not exist yet at Phase 2. Candidate governance question for
   Phase 5/Red Team: whether a lightweight, code-level convention (e.g.
   "any filed value pulled into a new computation must be looked up by
   its stored dict key or re-parsed string, never reconstructed by
   arithmetic on a cited float") is worth a named standing rule, given
   two independent occurrences.
2. **Null C's own wider-bracket behavior is a genuine bounce, not a
   stall or a crossing** — `delta_scene` reverses direction at
   θ₀+0.5°→+0.83° without approaching zero, the concrete shape behind
   the abstract INCONCLUSIVE-AT-THIS-WIDTH label. This is new
   information (not available from the ±0.5° bracket alone) even though
   it does not resolve Null C's own SIGN-CHANGE question.
3. **R5's first-ever real FDTD spend passed every gate it was asked to
   clear**: zero fault-injection surprises, GT sign match, settling
   well inside tolerance, and a genuine, cleanly-bracketed sign change
   at Step 3. This sub-thread's three-cycle-old "R5 built, never spent"
   status (exp-095) is now closed with a substantive, gated result, not
   merely an unblocked capability.
4. **Correction, Phase-5 Red Team audit mandatory fix #1 (PHOTONICS):**
   this item originally read "Richardson-style super-linear-growth
   pattern... reproduced," citing exp-098's own retracted `1.777` figure
   — see §Result's own corrected discussion. The corrected finding: **a
   shrinking marginal-to-marginal Richardson ratio (both `<1`) reproduced
   at a second, independent point-pair on Null B** (0.7765 at 20/30/40,
   exp-098; 0.9623 at 30/40/50, this cycle) — still descriptive only
   (Idealization 49), but two same-direction (shrinking) data points is a
   materially different, and more reassuring, evidentiary state than one.
   The ratio's own climb toward 1 across the two points (not "growing
   past 2nd order") is the genuinely open question, queued for Iteration
   77 (§Next).
5. **Item 3's falsification criterion, honestly applied, does not
   resolve** — the tail shows real decline without real recovery on
   both curves, plus an unpredicted early reversal (77°→79°). Disclosing
   a clean non-resolution is itself the informative outcome this item
   was built to produce either way (§Setup item 3), not a defect in the
   test.

## Next (Reconciled Iteration-77 queue — FINAL, per Red Team's Phase-5
audit, superseding the Director's own draft above; origins cited per
`phase5_redteam_audit.md` §5)

Five of six seats (MATERIALS, ELECTROMAGNETISM, THERMODYNAMICS, VISION,
and QUANTUM as an explicit gating precondition) converge on running the
constraint-1/2/3/4 scoring pass next cycle; PHOTONICS alone ranked it
third. Red Team's ruling, adopted: QUANTUM's dissent is a Red-Team-
charter-native expressibility concern and gates the trigger structurally;
PHOTONICS' dissent is a data-quality caution and is folded in as a
parallel precondition in the same tier, not grounds to demote the trigger
a full tier — seven consecutive T1:N/A cycles is exactly the drift
PANEL.md's own Checkpoint criterion 4 names.

**Tier 0 — mandatory documentation fixes**: applied same-shift, this
document, per `phase5_redteam_audit.md` §6 — the Richardson mis-citation,
the r-index mislabel, the settling-angle false-coincidence, the
T1-disposition conflation, the unauditable-verification-claim scoping,
and logging R20 into LOGBOOK.md.

**Tier 1 — preconditions that MUST run before any constraint-1/2/3/4
scoring pass touches `delta_scene(θ)`, bundled, zero-or-low marginal FDTD
cost:**

1. **QUANTUM's PAD-vs-article partition (mandatory, elevated from
   recommendation)**: decompose `delta_scene(θ)` into a PAD-toggled/
   article-held-fixed leg and an article-toggled/PAD-held-fixed leg, at
   the same angles, reusing `ratio_abs_ext`/`p_abs_w` — already computed
   at every point this sub-thread has run, including this cycle's 17 new
   cells. Zero new FDTD beyond what Iteration 77 spends anyway.
2. **MATERIALS' disposition memo**, bundled with #1: a short, zero-FDTD,
   citable finding formally separating "the `cpl` resolution knob is
   physically inert (newly confirmed, R3/R4/R5)" from "the tracked
   feature itself carries zero realizability content (an inherited,
   still-genuinely-ambiguous framing question, per Iteration 59→60 — NOT
   reaffirmed since)."
3. **A formal 4-point (cpl=20/30/40/50) convergence characterization at
   Null B**: is the Richardson ratio (0.7765→0.9623, climbing toward 1,
   not shrinking away from the naive figure) evidence of genuine-but-slow
   convergence or a non-convergent recipe artifact (Idealization 49/R15's
   own standing concern)? Zero new FDTD; all four points are already on
   file. Directly informs whether `delta_scene(θ)` is trustworthy enough
   to feed a scoring pass at all.

**Tier 2 — the scoring pass itself, gated on Tier 1's outputs, not
deferred a further cycle**: run `delta_scene(θ)`'s (or, if Tier 1's
partition finds the signal majority-PAD, its residual article-coupled
component's) sign structure through `emit.observer_record`,
`lab/ambient.py`, and the beam-behind box, per PANEL.md's own Metrics
table. If Tier 1 finds negligible article coupling, that converts Tier 2
into a disciplined negative finding (this diffraction feature has no
constraint-relevant material analog) — the honest, overdue answer to
seven cycles of deferred T1 status, not grounds to defer an eighth time.
Rotation lead: QUANTUM OPTICS. Must inherit VISION's own already-pinned
`C_thr(L)`/floor-gate machinery (T2/T16/T21/T24/T27) rather than
re-derive it.

**Tier 3 — parallel/lower-priority, cheap, fold in opportunistically:**

- Null C's own trough, widened to the full ≥2.9474° established period —
  but first spot-check the trough's own cross-resolution stability (1–2
  points at cpl=30 or cpl=50) before centering a wider search on it,
  matching R15's own discipline (QUANTUM's own finding, adopted).
- VISION's own pre-flight perceptual-caveat note (which `C_thr(L)`
  parameterization, which uncertainty budgets, Tier-W vs. Tier-A) —
  cheap, zero-FDTD, should exist before Iteration 77's own proposal is
  drafted, not folded in after.
- EM's own persistence gap (`xi_ext`/`sigma_abs_nonneg` margins never
  written to `results.json`) and THERMODYNAMICS' own persistence gap
  (`p_abs_w`/`dt_ss_full_K`/`netd_classification` computed-then-dropped
  at Step 1/Step 2) — both cheap, zero-new-FDTD backfills, bundle
  together.
- The Richardson pattern's lateral generalization to Null A — legitimate,
  lower priority than the vertical convergence question (Tier 1 item 3
  above).
- Item 3's direct GP2′-style recompute via exp-086's own narrow-window
  method over this cycle's same θc∈{79°...87°} range.
- Standing, now 5–8-cycle-deferred items, unchanged by this cycle: the
  full-width non-aliased second-wavelength `G40` leg and the real
  750/450nm wavelength-generality leg (six cycles deferred); the x-wall
  realizable-admittance refit (four cycles deferred); whether
  `PAD`-sensitivity survives with a real absorbing article loaded (five
  cycles deferred, still the single most overdue item on the T28 board)
  — if Iteration 77 defers these again, that must be a stated decision,
  not silence.
