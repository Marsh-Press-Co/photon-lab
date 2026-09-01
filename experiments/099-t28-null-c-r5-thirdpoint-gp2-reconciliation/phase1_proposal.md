# Panel Iteration 76 — Phase 1 Proposal (THERMODYNAMICS, rotation lead)

## 1. Mechanism/change narrative (≤300 words)

**This is a T28 house-discipline/validation cycle, not a new T1 escape-route
proposal** — the fourth in a row explicitly building on exp-096/097/098's
own adaptation of the Phase-1 format. It executes items 1, 2, 3 of exp-098's
own Reconciled Iteration-76 queue (item 4, ratifying R19, is already done —
R19 is in the RULED OUT registry; no action needed here) and gives item 5
(the six-consecutive-cycle T1-route-N/A flag) a reasoned disposition rather
than a silent seventh N/A.

**Item 1** re-tests Null C (θ₀=41.460901°) at cpl=40 with a wider,
R17-compliant, *asymmetric* bracket. exp-098's own item (ii) proved a
same-sized-but-mis-centered ±0.10° bracket can hide a real crossing at
38.590230°; Null C's current NO-SIGN-CHANGE verdict rests on the identical
untested failure mode — a symmetric ±0.500° bracket whose own 4 points show
a *decelerating*, still-positive `delta_scene` curve (THERMODYNAMICS reads
this as an open thermodynamic-limit question in its own right: a diffraction
amplitude asymptoting toward zero is not distinguishable, from 4 points
alone, from one about to cross). Width and direction are justified against
Null C's own established cpl20→cpl30 shift (exp-092), not borrowed by
analogy.

**Item 2** spends exp-095's already-built, gate-verified, never-executed
cpl=50 (R5) family on Null B (θ₀=40.265420°), the one established null with
*two* same-direction marginal shifts already on file (20→30, 30→40) —
letting the corrected marginal-to-marginal Richardson diagnostic
(exp-098's `richardson_style_diagnostic()`) run on a genuine third point for
the first time, descriptively (Idealization 49), not as a convergence-order
proof.

**Item 3** reconciles GP2′ against exp-086's own sliding-window `ptp`
statistic through the untested 74°–89.5° tail, scoping whether the 235.4×
vs. 5,444×–6,631× severity gap is a statistic artifact or a real physical
divergence.

Nothing below re-proposes any RULED-OUT idea (R1–R19 read in full).

## 2. Parameter table

All FDTD calls below reuse, unmodified: `Sim`/`add_line_source`
(`lab/fdtd2d.py`), `r{4,5}_config()`/`R{4,5}_CONFIGS`
(`experiments/069-.../design_geometry.py`), `cell_metrics_r4`/`run_block_r4`
(`experiments/094-.../run.py`), `cell_metrics_r5`/`run_block_r5`/
`_run_sim_r5_sigma` (`experiments/095-.../run.py`), `pair_metrics_full`/
`netd_row()` (`experiments/093-.../run.py`), the registration-readback gate
`run_checks_1234_and_7`/`check5_recipe_spot_check_extended`/
`check6_positional_and_cpl` (`experiments/097-.../run.py`, CLEAN, imported
never edited), and `richardson_style_diagnostic()`/`FastEval`
(`experiments/098-.../run.py`, `experiments/085-.../phase4_derivation.py`).
λ=600nm (2D TMz) only, matching Idealization 1. No new machinery is built.

### (1) Null C re-test — wider, asymmetric, R17-compliant bracket — 12 new calls

θ₀=41.460901139413461° (`experiments/090-.../results.json::q8.crossings_deg[3]`,
re-pulled this session, byte-exact). exp-098's own item (i) already ran 4
quartile-spaced points at cpl=40, ±0.500° symmetric — filed, reused not
rebuilt:

| θ (cpl=40, filed) | `delta_scene` | Δ vs. previous |
|---|---|---|
| 40.960901° (θ₀−0.500°) | +2.4719×10⁻³ | — |
| 41.294235° (θ₀−0.1667°) | +1.5127×10⁻³ | −9.592×10⁻⁴ |
| 41.627568° (θ₀+0.1667°) | +5.854×10⁻⁴ | −9.273×10⁻⁴ |
| 41.960901° (θ₀+0.500°) | +4.704×10⁻⁴ | −1.150×10⁻⁴ |

All four floor-clear, same sign, NO-SIGN-CHANGE — but the last interval's
slope magnitude drops **~8.06×** relative to the prior interval
(9.273×10⁻⁴ → 1.150×10⁻⁴), the deceleration signature this proposal reads
as a live "vanishing amplitude" candidate, not only "bracket too narrow."

**Width/direction, justified per R17 against Null C's own established
cpl20→cpl30 shift** (`experiments/092-.../results.json::rank1.crossing_report`,
re-read this session, not hand-typed): `shift_vs_cpl20_upper=+0.3201659178°`
(primary crossing) and `shift_vs_cpl20_upper_second=+0.3767516353°` (the
second near-C crossing branch) — **both positive**, i.e. Null C's own
cross-resolution history at cpl30 moves the crossing *upward* in θ, the
opposite direction from the downward analogy item (ii) used for
38.590230°. This is Null C's *own* directly-measured shift, not an analogy
borrowed from a different feature — the strongest available R17 basis.

**New bracket: 3 new points continuing upward** at the same 0.3333° quartile
step exp-098's own item (i) used (θ₀+0.8333°, θ₀+1.1667°, θ₀+1.500°):
**42.294235°, 42.627568°, 42.960901°.** Upward half-width from θ₀ = **1.500°**,
a margin of **3.98×** over the larger established shift (0.3767516°) and
**4.69×** over the smaller (0.3201659°) — genuinely wider than exp-096's own
1.33×–2.58× margin, not a reused round number (avoiding a second R17
violation by undersizing). **No new downward points**: the existing 4
filed points show `delta_scene` magnitude *growing* monotonically as θ
decreases away from θ₀ with no deceleration on that side, and Null C's own
established shift direction (upward, both branches) gives no directional
reason to search below θ₀−0.500°; the filed θ₀−0.500° point stands as the
bracket's lower anchor, unchanged, zero new cost.

Family: `R4` only, both legs `C40_R4`/`G40_R4`, both conditions
(empty/article) per angle. **Self-checked arithmetic**: 3 new angles × 2
legs × 2 conditions = **12 `sim.run()` calls** (matches the
`run_r4_batch`/R19-era job-construction pattern exactly: 2 keys × 2
conditions = 4 jobs/angle, 3 angles × 4 = 12 — not 3×2=6, the exact
undercount class R19 exists to prevent).

**Pre-registered third outcome — vanishing amplitude (not "try wider
next").** Define the interval-slope-decay ratio `r_i = |Δᵢ|/|Δᵢ₋₁|`
between consecutive `delta_scene` differences. The existing filed data
already show `r₃=0.1240` (the ~8× drop above). If the 3 new intervals
continue this pattern — `delta_scene` stays strictly positive across all 3
new points, remains floor-clear, and each new `r_i < 0.5` (each successive
change less than half the prior, the textbook signature of a curve
asymptoting rather than approaching a crossing) — this proposal
pre-registers that combination as **VANISHING-AMPLITUDE, no crossing at
this or any comparably-sized width**, to be reported as such rather than
deferred to "try an even wider bracket." If `delta_scene` crosses zero
anywhere in the 3 new points: **SIGN-CHANGE-FOUND**, matching Nulls A/B. If
neither clean pattern holds (e.g. `delta_scene` decelerates further but
does not clearly plateau, or reverses direction without crossing zero):
report **INCONCLUSIVE-AT-THIS-WIDTH** explicitly, and disclose — in advance
— that a third widening attempt would require a firm asymptote/floor
check before being proposed, not an open-ended re-widening loop.

### (2) cpl=50 (R5) third resolution point at Null B — 24 new calls, gated

**No R5 data exists near Null B or 38.590230° on file** — confirmed this
session by reading `experiments/095-.../results.json`: `rank2_calls=0`,
`rank2={"skipped": true, "reason": "Rank 1 combined go/no-go gate did not
PROCEED"}`. The R5 family (`dg.R5_CONFIGS`, `PAIR_KEYS_R5=("C40_R5",
"G40_R5")`, `SIGMA_R5_CORRECTED=0.2`, `R5_STEPS=7000`,
`R5_STEPS_STRESS=10500`) is fully built and gate-verified (exp-095's own
static Gates 1–4/6) but has spent zero real FDTD calls anywhere. This
proposal spends it for the first time.

**Target: Null B (θ₀=40.265420°), not 38.590230°.** Null B is the *only*
established null with **two** same-direction marginal cpl-shifts already on
file for the identical feature: cpl20→cpl30 = **−0.1935812645°**
(`experiments/092-.../results.json::rank1.crossing_report.shift_vs_cpl20_lower`)
and cpl30→cpl40 = **−0.1503190219°** (`experiments/098-.../results.json::
richardson_diagnostic.B.shift_30_40`), both downward, ratio **0.7765**
(shrinking, same sign). θ₀≈38.590230° has only a cumulative cpl20→cpl40
shift (item ii, exp-098) with no cpl30 intermediate on file — no marginal
decomposition is possible there. Null B alone lets
`richardson_style_diagnostic()` be reused a second time, on a genuine third
point, for the first time in this program's history.

Established cpl40 crossing (reused, not re-derived):
θc40=**39.921519316666°** (`experiments/098-.../results.json::item_i.B.crossing_cpl40`).

**Rank 2a — settling precondition, 8 calls** (mirrors exp-095's own
unexecuted Rank 2a exactly: `R5_STEPS`/`R5_STEPS_STRESS` compared at one
representative angle, gating Rank 2b). Angle: **39.854853°** — chosen to
coincide with one of Rank 2b's own interior-sweep angles (below), matching
exp-095's own precedent that `RANK2A_ANGLE ∈ RANK2B_ANGLES`. 2 keys × 2
step counts × 2 conditions = **8 `sim.run()` calls**. Gate: `settle_band`
(exp-095's own function) on `rel_dev = |Δdelta_scene(10500,7000)|/
|delta_scene(7000)|` — PASS ≤1%, CAUTIONARY-PASS ≤10%, HALT >10%. Rank 2b
runs only if not HALT.

**Rank 2b — interior sweep, 4 angles, 16 calls, gated on Rank 2a.**
Asymmetric bracket around θc40, weighted toward lower θ (matching Null B's
own doubly-confirmed downward shift direction — both the 20→30 and 30→40
marginal shifts are negative): span **[θc40−0.400°, θc40+0.100°]**,
quartile-spaced at **0.1667°** steps (0.861× the largest established Null B
marginal shift, 0.1935813° — finer than the largest known shift, so a real
crossing cannot hide between two same-sign samples, matching item i/ii's
own design rule):

| θ (cpl=50, new) | Offset from θc40 |
|---|---|
| 39.521519° | −0.400° |
| 39.688186° | −0.233° |
| 39.854853° | −0.067° (= Rank 2a angle) |
| 40.021519° | +0.100° |

Family: `R5` only, both legs `C40_R5`/`G40_R5`, both conditions. 4 angles ×
2 legs × 2 conditions = **16 `sim.run()` calls.**

**Self-checked arithmetic, item 2**: Rank 2a 2×2×2=8; Rank 2b 4×2×2=16;
subtotal 8+16=**24**. Disclosed, not silently optimized: per exp-095's own
(unexecuted) design, Rank 2a's settling angle intentionally coincides with
one Rank 2b interior angle (39.854853°) — the resulting 4 overlapping
`(key, 39.854853°, condition, R5_STEPS)` jobs between Rank 2a and Rank 2b
are **not deduplicated**, a minor (4-call) redundancy accepted for
structural consistency with exp-095's own precedent rather than a new,
unvalidated optimization.

**New third-point diagnostic**: if Rank 2b finds a genuine cpl50 crossing
θc50 (sign change among the 4 interior points), compute `shift_40_50 =
θc50 − θc40` and call `richardson_style_diagnostic(shift_20_30=shift_30_40,
shift_30_40=shift_40_50, cpl20=30, cpl30=40, cpl40=50)` — the corrected,
Phase-5-verified marginal-to-marginal function, imported unmodified,
relabeled positionally for the 30/40/50 triple exactly as its own docstring
permits. `naive_order2_ratio=(40/50)²=0.64` in this relabeling (not the
20/30/40 triple's own 0.5625). If no crossing is found among the 4 interior
points, no Richardson figure is computed — reported as its own outcome, not
forced.

### (3) Reconcile GP2′ against exp-086's `ptp` method through 74°–89.5° — 0 new FDTD, 155 new zero-FDTD evaluations

**Actual current θc range, read from `experiments/086-.../
phase4_rescore_results.json::method_c_rescore.sub_results`, not assumed**:
`theta_centers = np.arange(5.0, 77.0+1e-9, 2.0)`, **37 windows**, θc ∈
[5.0°, 77.0°]. Each window is `sub_theta = np.arange(θc−3.0, θc+3.0+1e-9,
0.2)` (**31 points**, 6° wide), so the actual θ-coverage is [2.0°, 80.0°] —
it does **not** reach the GP2′ tail's own 89.5° upper bound; the last
window (θc=77°) covers only up to θ=80°. Peak `ptp`, already on file:
θc=69° → `ptp=1.695985`, a **6630.99×** ratio to the θc=5° reference
(`ptp=2.5577×10⁻⁴`) — matching the already-published 6,631× figure exactly.
Recovery is also already visible by θc=75° (`ptp=0.0796`, 311×) and
persists through θc=77° (`ptp=0.1589`, 621×) — but nothing beyond 77° is on
file.

**Extension, reusing the method verbatim** (same `FastEval`, same
`theta_centers`/`sub_theta` construction, same `ptp_sub = np.ptp(c_sub)`
formula — no new statistic): continue the identical 2° step, same odd-θc
parity, to **θc ∈ {79°, 81°, 83°, 85°, 87°}** — **5 new windows**, window
coverage now reaching θ=90° (θc=87° window spans [84°,90°]), comfortably
past GP2′'s own 89.5° edge. **5 windows × 31 points/window = 155 new
zero-FDTD `FastEval.one()` evaluations** — the `ptp` statistic alone
(`np.ptp` of the raw curve) requires no `free_period_with_widening` fit, no
circular-shift null, no Spearman stride test (those serve the periodicity
question exp-086 asked, not the amplitude-severity comparison this item
asks); this proposal computes only what the reconciliation needs.

**Scoping the severity gap.** GP2′'s worst ratio, already on file
(`experiments/098-.../results.json::item_v.gp2_curve`, re-read this
session): **235.396× at θ=66.0°** — vs. exp-086's own 6,630.99× at
θc=69°, a ~28× gap between the two instruments' own peak severities. Both
instruments read the *identical* underlying closed-form curve
(`edge_diffraction_c_empty_corrected`/`FastEval`), per exp-098's own
disclosure — the gap cannot be a different physical measurement, only a
different *statistic* on the same curve, or a different *reference*. GP2′'s
own already-filed 74°–89.5° tail (re-read this session, all 32 points at
0.5° step) shows **zero VALID points** (ratio never drops below ~12.2× at
θ=89.5°) — a monotonic-but-slow decline from 78.5× (θ=74°) to 12.2×
(θ=89.5°), never recovering to VALID (≤10×) anywhere in the tested tail.
This is qualitatively different from exp-086's own already-established
59°–73° shape (a sharp peak with genuine recovery to 311×–621× by
θc=75°–77°, itself only ~5–10% of the peak) — the two curves' *shapes*, not
just their magnitudes, look different over the one range where both are
now on file (74°–77°/80°).

**What would distinguish "statistic explains the gap" from "something else
contributes":** if the newly-computed θc=79°–87° `ptp` values continue
exp-086's own established recovery trend (settling to a low, comparable-to-
θc=5°-reference order, e.g. <1000× and trending down) over the SAME range
where GP2′ stays elevated and non-recovering (12×–78×, MARGINAL throughout,
never VALID) — that persistent divergence in *shape*, not merely
*magnitude*, would indicate something beyond the statistic choice: a
windowed peak-to-peak captures local curve *variation* within a 6°-wide
window, while GP2′'s single-point ratio captures curve *magnitude* at one
θ relative to a distant low-θ band — these are genuinely different
mathematical projections of the same curve, and a shape mismatch (not just
a scale mismatch) would mean the "differing statistic" framing is
necessary but not sufficient to explain the whole gap. Conversely, if the
extended `ptp` values ALSO stay persistently elevated through 87° (never
recovering to a low multiple of the θc=5° reference, mirroring GP2′'s own
non-recovery), that would support "the same underlying curve behavior,
viewed two ways, and the gap is fully accounted for by statistic + scale."
No confident lean stated — this is the open question item 3 exists to
answer, not to assume.

## 3. T1 escape-route mapping

**No new escape-route mechanism is proposed this cycle — Checkpoint
criterion 2 (T1 position) is N/A**, matching exp-094 through exp-098's own
precedent. This makes exp-099 the **seventh** consecutive cycle with
"T1 escape-route: N/A" if left unexamined, the exact recurrence MATERIALS'
governance flag (exp-098, queue item 5) exists to force a genuine
disposition on, not a silent restatement.

**Disposition (this seat's ruling, THERMODYNAMICS lead): option (b),
reasoned, not deferred.** Items 1–3 above are, without exception, house-
discipline/instrument-trust work on the *evidentiary basis* for an
*already-committed* escape route (angular selectivity) — none proposes a
new candidate mechanism, material parameter, or constraint-satisfaction
argument; there is no new σ(I)/σ(x,t)/angular-selectivity/sub-threshold
parameter set on the table to map against T1's central tension. A T1
escape-route field requires a candidate mechanism's own constraint stance;
none exists this cycle to state one for. Forcing a T1 entry here would be
exactly the "unfalsifiable claim manufactured to fill a field" failure mode
Red Team's charter exists to strike.

**But this is not indefinitely defensible, and a bound is stated now,
not left open-ended.** THERMODYNAMICS' own charter asks where absorbed
energy goes and whether it is detectable — and none of this seven-cycle
run (exp-094–099) has yet asked that question of the angular-selectivity
line's own `delta_scene(θ)` finding against PANEL.md's actual phenomenon
target (constraints 1–4). The `delta_scene` sign-structure result this
whole sub-thread validates is, at present, purely an instrument-trust
finding about a diffraction model's own internal consistency — it has
never been cashed out as an angular-dependent absorption/transmission mask
and scored against beam-termination, backscatter, or ambient-contrast
metrics (Metrics table, PANEL.md). **Explicit trigger for the next cycle**:
once items 1–3 above close (Iteration 76, or a short continuation), the
Iteration 77 queue should include, for the first time in this T28
sub-thread's recorded history, an actual constraint-1/2/3/4 scoring pass
that treats the now-well-characterized `delta_scene(θ)` sign structure as
an angular-selectivity parameter and runs it through the existing
constraint-metric instruments (`emit.observer_record`, `lab/ambient.py`,
the beam-behind box) — not another round of bracket/instrument validation
on the same underlying evidence. If Iteration 77 also files T1: N/A without
addressing this trigger, that is the point at which this seat's own
disposition should be read as overridden, not reaffirmed by default.

## 4. Per-metric predicted outcomes (falsifiable, frozen before any run)

| Item | Metric | Predicted band / criterion | Confident lean? |
|---|---|---|---|
| (1) | `delta_scene` sign, 3 new Null C points | **SIGN-CHANGE-FOUND** (crossing somewhere in 41.96°–42.96°); **VANISHING-AMPLITUDE** (stays positive, floor-clear, each new `r_i<0.5`); **INCONCLUSIVE-AT-THIS-WIDTH** (neither clean pattern). No confident lean — genuinely open, all three are live, pre-registered outcomes. |
| (1) | `floor_pass` | All 3 new angles clear `FLOOR_FRAC=0.10` (matching all 12 filed Null-A/B/C points and all 6 filed 38.09°–38.69° points to date, zero exception on file). Confident lean: **PASS**. |
| (2) Rank 2a | `settle_band(rel_dev)` at 39.854853° | Confident lean: **PASS** (≤1%) — every prior R4/R5-family settling-adjacent check on file (exp-086's own 10-seed multi-seed replication, R12) has shown negligible sensitivity to a stress-level step-count increase at this box geometry. Stated as a lean, not a certainty — this is the first REAL R5 settling check ever executed. |
| (2) Rank 2b | `delta_scene` sign, 4 interior cpl=50 points | Genuinely open — no confident lean. If a crossing is found, `shift_40_50` is expected (not certain) to carry the SAME sign as the two already-established Null B shifts (both negative) per the doubly-confirmed downward trend, but Idealization 49/MATERIALS' unconverged-discretization finding means this is a lean, not a prediction with a stated numeric band. |
| (2) | Richardson diagnostic (30/40/50 triple), IF a crossing is found | No confident lean on the observed ratio's value. `naive_order2_ratio=0.64` is the mechanical comparison target; whether `observed_ratio` sits near, above, or below it (as the 20/30/40 triple's own 0.777 vs. 0.5625 did) is the open question this item exists to answer. |
| (3) | Extended `ptp` values, θc∈{79°,81°,83°,85°,87°} | No confident lean on exact magnitude. Weak lean toward continued decline from the θc=77° value (0.1589, 621×) given the monotonic post-peak decay already visible from θc=69°→77°, but whether it drops toward a low multiple of the θc=5° reference (order 10¹–10²×, "genuine recovery") or plateaus at an elevated level (order 10²–10³×, "partial, GP2′-like non-recovery") is the open question. |
| (3) | Severity-gap attribution | No confident lean stated in advance — falsifiable per the criterion in §2 item (3) above (shape match/mismatch over the 74°–87° overlap range). |

## 5. Idealizations

**Carried forward** (exp-096/097/098, cited by number, unchanged): 1 (2D
TMz, 600nm only), 7 (no constraint-1/2/3/4 test executed THIS cycle — see
§3 above for the explicit disposition, not merely a restated N/A), 17
(R3/R4/R5 share one mechanical recipe — a family-wide defect is not
distinguishable from independent per-family bugs by any single item alone),
38/39/42 (Check 5 has never tested any `G40_*` padded config, any family),
46 (a 4-point quartile bracket localizes a sign change but does not certify
absence outside the tested span — extended here to the 7-point Null C
bracket and the 4-point Null B cpl50 sweep alike), 49 (any Richardson-style
figure is explicitly descriptive, no continuum reference value exists —
applies identically to the new 30/40/50 relabeling in item 2).

**New this cycle:**

53. Item (1)'s pre-registered VANISHING-AMPLITUDE reading is itself a
    finite-sample inference from 3 additional points (7 total) — it
    cannot distinguish a true asymptote from a crossing sitting just
    beyond 42.96° at comparably small amplitude. The `r_i<0.5` criterion
    is a disclosed, non-formal heuristic (a geometric-decay signature),
    not a proof of convergence to zero.
54. Item (2)'s choice of Null B over θ₀≈38.590230° is a resource
    allocation decision (Null B has both marginal shifts on file; the
    other does not), not a claim that 38.590230° is less physically
    interesting — it remains the natural next R5 target once its own
    cpl30 intermediate is established.
55. Item (2)'s asymmetric, lower-θ-weighted Rank 2b bracket assumes the
    downward marginal-shift trend (20→30, 30→40) continues into 40→50; if
    it does not, the true cpl50 crossing (if any) could sit outside the
    tested [θc40−0.400°, θc40+0.100°] span — matching Idealization 46's own
    caveat, restated for this specific asymmetric design.
56. Item (3)'s extension reuses exp-086's `ptp` statistic exactly, but
    `ptp` and GP2′'s `ratio_to_ref` are not interchangeable measures of the
    same underlying phenomenon (a windowed spread vs. a single-point
    magnitude) — a close numeric match between the two, if found, would be
    informative but not a proof they measure the identical thing; a
    mismatch is equally informative, per §2 item (3)'s own falsification
    criterion.
57. GP2′ and exp-086's `ptp` method both evaluate the same closed-form
    diffraction MODEL, not new FDTD measurements (exp-098's own
    Idealization 50/52) — item 3's reconciliation is a comparison between
    two post-processing statistics on one model, not two independent
    physical instruments; a "shape match" or "shape mismatch" finding
    describes the model's own internal structure, not a new physics
    result.

**Carried idealizations banner: every prediction in §4 is governed by
Idealizations 1/7/17/38/39/42/46/49 plus this cycle's own 53–57.**

## 6. Total estimated FDTD-call budget

- Item (1): 3 new angles × 2 legs (`C40_R4`/`G40_R4`) × 2 conditions
  (empty/article) = 3×2×2 = **12 `sim.run()` calls**.
- Item (2), Rank 2a: 2 legs (`C40_R5`/`G40_R5`) × 2 step counts
  (`R5_STEPS`/`R5_STEPS_STRESS`) × 2 conditions = 2×2×2 = **8 `sim.run()`
  calls**.
- Item (2), Rank 2b (gated on Rank 2a not HALTing): 4 new angles × 2 legs
  × 2 conditions = 4×2×2 = **16 `sim.run()` calls**.
- Item (3): **0 `sim.run()` calls** — 5 new windows × 31 points/window =
  5×31 = **155 zero-FDTD `FastEval.one()` evaluations**.

**PASS-path total (Rank 2a does not HALT): 12 + 8 + 16 + 0 = 36
`sim.run()` calls.**
**HALT-path total (Rank 2a HALTs, Rank 2b skipped per exp-095's own
pre-registered "a FAIL/HALT is a reported outcome, never spent past"
discipline): 12 + 8 + 0 + 0 = 20 `sim.run()` calls.**

Both totals additionally carry: item (1) — 6 zero-cost registration-
readback preflight checks (3 angles × 2 config keys, Checks 1–4+7); item
(2) — 2 preflight checks for Rank 2a (1 angle × 2 keys) plus, if run, 8 for
Rank 2b (4 angles × 2 keys), all zero marginal FDTD cost (the gate stops
before `sim.run()`); item (3) — 155 zero-FDTD closed-form evaluations, no
`Sim()` construction of any kind.

Wall-time estimate, scaling from exp-098's own 64-call/134.62-min pace
(≈2.10 min/call, the most recent same-family, same-hardware-class
comparator on file): **≈76 minutes** for the 36-call PASS-path total
(≈42 minutes for the 20-call HALT-path floor); item (3)'s 155 closed-form
`FastEval.one()` evaluations add well under 2 seconds — exp-086's own
filed `method_c_rescore.stage_elapsed_total_s=7.287s` covers 37×31=1147
points *including* a full `free_period_with_widening` fit per window, a
strictly more expensive computation than the bare `ptp`-only pass this
item needs for 155 points.
