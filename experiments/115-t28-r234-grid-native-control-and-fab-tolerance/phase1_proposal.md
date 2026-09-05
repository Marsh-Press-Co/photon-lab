# exp-115 — Panel Iteration 92 (candidate)

**Lead seat: MATERIALS & METAMATERIALS** (rotation, PANEL.md: VISION
SCIENCE(90) → PHOTONICS(91) → **MATERIALS(92)** → ELECTROMAGNETISM →
THERMODYNAMICS → QUANTUM OPTICS → repeat). Governance/instrumentation
cycle continuing the T28 sub-thread (opened Iteration 46, exp-069; T1
route N/A throughout its own 46-iteration history to date).

**Queue items executed** (Reconciled Iteration-92 queue, PLAN.md lines
87–96 / `experiments/114-.../phase5_redteam_audit.md` §7):

- **Tier-1 item 1 — the falsifiable heart.** A genuine same-session
  control-timing burst measured **directly on the r=234 grid**
  (`N=2100`), matched-protocol against the r=156 grid (`N=1400`) in the
  same session, with EM's bundled immediate repeat. Independently ranked
  #1 by EM and PHOTONICS and #2 by QUANTUM at Iteration 91; the one check
  that resolves Red Team's own v2 **straddle** finding with real data
  instead of two competing unverified assumptions. Executed **first and
  in its queue order**, exactly as ranked.
- **Tier-1 item 2 — folded in, zero marginal cost.** Persist and disclose
  the short-reading alternative scoring and the v2 straddle as stated
  `..._DO_NOT_SCORE` sensitivities, with an explicit justification for
  the "sustained" choice. This cycle re-scores the same statistic, so
  carrying its sensitivities forward is bookkeeping this cycle owes
  anyway, not a second question.
- **Tier-1 item 5 — this seat's own charter debt, folded in as a clearly
  labelled analytic sidecar.** MATERIALS' fabrication-tolerance
  quantitative bound: **write the actual number, with sources, and its
  published / plausible / unobtainium-with-parameters tier.** Now SEVEN
  consecutive cycles named-but-undone (exp-111 → exp-114). §3 states why
  folding it in does not compromise item 1.

**A note on this seat's own charter fit, stated up front.** Item 1 is
wall-clock instrument calibration, not sub-wavelength structure — my
charter ("what could physically realize the proposed optical behavior;
owns the realizability bound") does **not** bind on a cost exponent, and
I do not dress it as if it did. What my charter *does* bind on, and what
I discharge here: (a) verifying that `geom_fixedabs_cpl` still builds the
same physical article at both grids being timed, so the two rates are
rates for the *same material law* and not two different objects (§2.0);
(b) item 5, which is squarely and *only* this seat's duty — no other
charter in PANEL.md can discharge "translate a repeated core/backing
insensitivity finding into a fabrication-tolerance bound with a
realizability tier."

---

## 1. Mechanism/execution narrative (≤300 words)

Before proposing anything I checked (R4/R9) whether the configuration
had ever been run, and found something stronger than a null: **no control
burst has ever been timed on the r=234 grid, or on any grid but r=156, in
this program's history** — `_time_control_blend` hardcodes
`geom_fixedabs_cpl(156, 25)` in both `chunk_runner113.py` and
`chunk_runner114.py`. "cross-grid" exists only as prose in exp-114's own
Phase-5 documents, never as executed code.

Then I re-derived exp-114's own scored statistic from its committed
primitives and found an identity nobody in that cycle stated. Because
`STEPS` scales linearly with `kappa` by construction and both legs run
three scenes, exp-114's `measured_ratio` reduces **exactly** to

    measured_ratio = kappa_ratio × G,    G ≡ per-step(r=234) / per-step(r=156)

with every cross-session term cancelling identically. Verified bit-exact:
1.5 × 2.74550565394726 = 4.11825848092089, the filed value to all 15
digits. So exp-114 did not measure a cross-session cost ratio at all — it
measured **G**, the same-session per-step cost ratio between two grids,
and its residual confound is not cross-session normalization but the
**protocol mismatch** between its r=156 denominator (3334 steps/scene,
cold, one call) and its r=234 numerator (12000 steps/scene,
checkpoint-chunked).

This cycle therefore measures `G` directly, on both grids, in one
session, at matched step counts and matched scene mix — a replication of
exp-114's scored statistic that is **R33-immune by construction** (no
operand mixes sessions) and free of that protocol mismatch. It can
confirm or refute a filed CONFIRM. The sidecar (item 5) rides along at
zero FDTD cost, from data already committed.

*(249 words.)*

---

## 2. Parameter table

### 2.0 Grounding-fact verification — run this session, before proposing (R4/R9 discipline)

Every figure below was produced by invoking committed code or reading
committed JSON, never hand-typed. Commands are reproducible from the
repository root.

| Claim | How checked | Result |
|---|---|---|
| No control burst has ever been timed on any grid but r=156 | `grep -rn "geom_fixedabs_cpl(234\|_time_control_blend" experiments/*/chunk_runner*.py` | Only `chunk_runner113.py:177` and `chunk_runner114.py:174`, **both** hardcoding `geom_fixedabs_cpl(156, 25)` (line numbers re-verified by direct grep this session). Zero prior r=234-grid (or r=312-grid) control readings exist. |
| "cross-grid" has never been an executed or scored quantity | `grep -rln "cross_grid\|cross-grid" experiments/ lab/ *.md` | Four prose hits only — exp-114's `NOTES.md`, `phase5_redteam_audit.md`, `phase5_review_photonics.md`, plus `LOGBOOK.md`/`PLAN.md`. No code, no persisted field. |
| `measured_ratio ≡ kappa_ratio × G` (the identity §1 rests on) | Recomputed from `experiments/114-.../results.json` primitives: `(t234_cpl25/36000) / r31_control.sustained.this_session_per_step_s` × 1.5 | `1.5 × 2.74550565394726 = 4.11825848092089` vs. filed `kappa_exponent_result.measured_ratio = 4.11825848092089` — **bit-exact, all 15 digits.** Also verified `t156_session_adjusted = 3×8000×0.07121022268191168 = 1709.0453…` = filed, and `t234 = 3×12000×0.19550806899203194 = 7038.2904…` = filed. |
| `G_E`, exp-114's own session's cross-grid ratio | as above | `2.74550565394726` (r=234 production blend / r=156 sustained control blend). |
| `G_ref`, the value `KAPPA_COST_EXPONENT` predicts at `kappa_ratio=1.5` | `R110.KAPPA_COST_EXPONENT`; `1.5**(k-1)`; cross-checked as `reference_ratio/1.5` | `k = 3.2053299988171697`; `G_ref = 2.4453404739580256`; `3.6680107109370383/1.5 = 2.4453404739580256` — identical. |
| Pure cell-count (`N²`) scaling — the v2 method's own core assumption — implies which exponent? | `(2100/1400)**2 = 2.25`; `k = 1 + ln(2.25)/ln(1.5)` | `G_N² = 2.25` exactly, `k = 3.0` **exactly** — i.e. v2's assumption is algebraically identical to the ORIGINAL hardcoded exponent `3.0` that `KAPPA_COST_EXPONENT` replaced (R28). Not previously stated anywhere in the record. |
| `R_DEG`, exp-114's own measured single-grid sustained-load degradation (the anchor for this cycle's tolerance bands — R17) | `sustained.this_session_per_step_s / short.this_session_per_step_s − 1` from `experiments/114-.../results.json` | `0.07596424755863729` (7.596%, r=156 grid, 1000 → 3334 steps/scene). |
| Geometry identity at both grids to be timed | `python run114.py --verify-geometry` idiom, re-run | `{"pass_": true, "mismatches": []}` at r = 156, 234, 312. Both grids this cycle times build the **same material law**: `tau_shell = 24.0` and `absorb = edge = 50` identical at r=156/234/312, `cpl=25`; only `N`, `CX/CY`, `SRC_X`, `STEPS`, `R_CORE`, `R_COAT` scale with `kappa`. |
| exp-108's per-bin core-fill figures (sidecar input) | `experiments/108-.../results.json` → `tier1.r{156,312}.item_i.rel32` (48 entries each) | max = `1.4760284822434646e-04` (r=156), `1.5265673604659632e-04` (r=312); `confirm_all_margins = True` at both. |
| **R4 correction to my own seat's exp-114 Phase-5 review** | direct read of `experiments/108-.../run.py::classify_item_i` | `ITEM_I_CONFIRM_REL = 0.05` is the **decision bar**, not a measurement. My own exp-114 review (§3) cited "≤5% at 48 angular bins × 6 box radii" as though 5% were the measured figure; the measured figure at margin=32 is `1.5×10⁻⁴`, ~330× tighter. Only the margin-32 array is persisted; the other five margins are certified only by the boolean `confirm_all_margins`. Disclosed forward, not retro-edited. |
| exp-112/exp-114 aggregate core-fill deltas (sidecar input) | recomputed from each cycle's own `results.json.energy_ledger` | r=156: σ_scat `8.359387e-05`, σ_abs `4.084328e-05`, σ_ext `2.146913e-05`. r=234: σ_scat `1.087354e-04`, σ_abs `5.666218e-06`, σ_ext `5.204381e-05`. Bit-exact to my own exp-114 Phase-5 table. |
| The channel's own self-consistency floor (sidecar floor-gate, R13) | `|σ_ext − σ_ext_cross|/σ_ext` from the same ledgers | r=156: `6.6495e-06`; r=234: `2.7794e-05`. |
| `τ_true`, the shell's Im(n)-weighted one-way optical depth, and its already-filed realizability tier | `experiments/061-.../NOTES.md` lines 42–49, 344–347, 379–391 | `τ_true = 8.258819829686677`, `α_true = 5.7353×10⁴ cm⁻¹`, e-fold 174.36 nm, OD 3.587, at 1.44 µm physical thickness. **Tier already filed: UNOBTANIUM-WITH-PARAMETERS, driven by thickness** (record-blackness CNT forests run 100–500 µm, 70–350× this construction's 1.44 µm; MP-2/MP-4 CONFIRMED). |
| Shell physical thickness, invariance across the family | `R_COAT − R_CORE` evaluated at r = 156/234/312 and cpl = 20/25 | 48 cells at cpl=20 (dx = 30 nm) and 60 cells at cpl=25 (dx = 24 nm) → **1.440 µm ≡ 2.40 λ at 600 nm, identical at all three radii and both resolutions.** |

### 2.1 The two grids being timed (unchanged construction, both already validated)

| Quantity | r=156, cpl=25 | r=234, cpl=25 |
|---|---|---|
| Domain `N` (cells, square) | 1400 | 2100 |
| `CX`, `CY` | 630, 700 | 945, 1050 |
| `SRC_X` | 160 | 240 |
| `R_CORE` / `R_COAT` | 135 / 195 | 232 / 292 |
| `sigma_max` | 0.4 | 0.4 |
| `tau_shell` (invariant, asserted in code) | 24.0 | 24.0 |
| `absorb` / `edge` | 50 / 50 | 50 / 50 |
| `kappa_of(r)` | 2.0 | 3.0 |
| cell-count ratio to r=156 | 1.00 | 2.25 |
| production `STEPS`/scene (**not run this cycle**) | 8000 | 12000 |

**Material law, numbers (unchanged, reused not re-specified):**
`materials.graded_black_shell(sim, CX, CY, R_CORE, R_COAT,
sigma_max=0.4)` — a graded conductive sponge, `eps_r ≡ 1.0` throughout
(no index step, hence no interface to glint off), `σ(r)` ramping
adiabatically from 0 at `r_out` to `sigma_max` at `r_in` along the
committed `_graded_black` smoothstep profile, giving
`tau_shell = sigma_max × (R_COAT − R_CORE) = 24.0` at both radii. The
`peccored` scene adds `materials.pec_disk(sim, CX, CY, R_CORE)` inside
that shell; the `hollow` scene leaves the core vacuum. Source:
`add_line_source(SRC_X, angle_deg=0.0, profile="plane", edge=50)`.
Wavelength 600 nm, `cells_per_lambda = 25` (dx = 24 nm),
`courant_frac = R110.COURANT_FRAC`.

### 2.2 Block CG — the readings (six control bursts, all cold-build 3-scene blends)

Each reading re-times **all three** scenes (`empty`, `hollow`,
`peccored`), cold-built, in one `sim.run(steps)` call per scene, and
reports the blended per-step rate — the identical recipe as
`chunk_runner114.py::_time_control_blend`, reused with the **one minimal,
disclosed change**: `r` becomes a parameter instead of the hardcoded
`156`. The 3-scene mix is mandatory, not stylistic: exp-113's own Fix 3b
established that re-timing `empty` alone against a blended comparator is
a real, signed, anti-conservative commensurability defect (`peccored`
steps are ~14% costlier).

| # | Reading | grid | steps/scene | grid steps | purpose |
|---|---|---|---|---|---|
| 1 | `S156` | r=156, N=1400 | 1000 | 3000 | short baseline; matches exp-113/114 `SHORT_CONTROL_STEPS` |
| 2 | `S234` | r=234, N=2100 | 1000 | 3000 | **first r=234-grid control in program history** |
| 3 | `U156` | r=156 | 3334 | 10002 | sustained; matches exp-114 `SUSTAINED_CONTROL_STEPS` |
| 4 | `U234` | r=234 | 3334 | 10002 | sustained, matched to #3 |
| 5 | `U156b` | r=156 | 3334 | 10002 | EM's bundled immediate repeat |
| 6 | `U234b` | r=234 | 3334 | 10002 | EM's bundled immediate repeat |

**Execution order is 1 → 2 → 3 → 4 → 5 → 6, deliberately interleaving the
two grids within the sustained pass.** Running all r=156 readings before
all r=234 readings would place every r=234 reading later under more
accumulated thermal/turbo load, biasing `G` upward by exactly the effect
`R_DEG` measures. Alternating pairs each sustained reading with an
adjacent same-duration reading on the other grid.

**Nothing else runs.** No production leg, no `full_capture`, no
`window_stats`, no angular-pattern instrument, no named-bin
classification, no checkpoint/resume. Total: **18 `Sim.run()` calls**
(6 readings × 3 scenes), **46,008 grid-steps** (23,004 per grid).

### 2.3 Chunking / R31 machinery

`r31_control_ratio()` and `combine_control_readings()`
(`run113.py`, re-exported by `run114.py`) are reused **unmodified** for
the r=156 readings, so this cycle also produces a conventional
bench-native R31 control every future bench cycle can cite. They are
**not** applied to the r=234 readings: `r31_control_ratio` divides by
`HISTORICAL_PER_STEP_S`, an r=156/cpl=25 3-scene blend, and dividing an
r=234-grid rate by it would be a textbook R9 incommensurability. The
r=234 readings are compared only against this cycle's own r=156 readings
(same session, matched protocol) and, informationally, against exp-114's
own r=234 figure `HIST_R234_PER_STEP_S = 0.19550806899203194 s/step`
(derived in code as `results.json["t234_cpl25"]/36000`, invoked not
hand-typed).

---

## 3. Scope decision — what this cycle declines, and why folding item 5 in is safe

**Declined, each a real and undropped debt, named not silently dropped:**

1. **Tier-1 item 3, the `+168.75°`/r=312/cpl=25 leg.** Red Team's own
   Iteration-92 queue sequences it explicitly *after* item 1 lands, so it
   can reuse whatever cross-grid factor item 1 measures. Running it here
   would defeat that sequencing. Carried to Iteration 93.
2. **Tier-1 item 4, `resolved_unresolved_crosstab`/
   `apply_crosstab_to_check_c`.** Has no real r=312 data to run against
   (three consecutive gate refusals, exp-111/112/113). Blocked on item 3.
3. **Tier-2 item 6, the per-bin core/backing check at r=234.** I *cannot*
   ride it free on exp-114's captures as my own Phase-5 review assumed:
   those pickles lived in that session's `/tmp` scratch and were never
   committed, and `results.json` persists only the aggregate ledger. It
   would need three fresh full-production r=234 scenes (12000
   steps/scene), which would compete directly with item 1's own budget.
   Carried, with this reason stated for the first time.
4. **Tier-2 item 8, the third P5 thermal-margin point.** Gated on the
   `CPL_RATIO` commensurability gap (THERMODYNAMICS' own explicit
   caution), unresolved.
5. **Tier-2 item 9 / Tier-3, a fourth r-point (r≈624) and an r=312 leg on
   the far side of `kappa_ratio=2.0`.** Both would double or triple this
   cycle's grid cost; and my own Phase-5 request that one run serve both
   MATERIALS' `σ_ext`-superlinearity residual and THERMODYNAMICS' own
   `r^-1.16` projection still stands, unchanged, for a later cycle.
6. **Tier-3 item 10, VISION's re-score of the program's only-ever
   Tier-W/Tier-A constraint-3 citation.** The single highest-value
   NEW-territory move on the board and the one item that would re-engage
   the phenomenon itself rather than the instrument. Out of scope here
   only because this cycle executes the queue in its own Tier order;
   flagged again, deliberately, so it does not decay into furniture.
7. **Tier-3 items 11–13** (`PAD`-with-article survival; N33; the
   `R2_SMOOTH_THRESHOLD=0.90` re-derivation, seventh consecutive cycle).

**Why folding item 5 in does not compromise item 1** (argued, not
asserted): item 5 consumes **zero FDTD calls, zero grid-steps, and zero
bench wall time on the timed hardware path** — it is arithmetic over four
already-committed `results.json` files plus one desk integral, and it can
be computed before, during, or after the bursts without perturbing a
single timing measurement. It introduces no new discriminating statistic
of the kind R30/R32 govern and no new FDTD machinery of the kind R18
governs. Red Team has repeatedly flagged **density** in this sub-thread;
the density risk is additional *falsifiable FDTD questions*, of which
this cycle has exactly one. Item 5 is labelled throughout as an
**analytic sidecar** — a post-run desk calculation, not an FDTD output —
following THERMODYNAMICS' own expressibility contract in PANEL.md
verbatim. Against that near-zero cost sits an eighth consecutive silent
deferral of the one debt only this seat can pay, which Red Team's own
queue says should not happen without an explicit Director decision.

---

## 4. T1 escape route: N/A — stated explicitly, and reasoned structurally

**Item 1** changes only which grid a wall-clock stopwatch is started on.
No σ(I) / σ(x,t) / angular-selectivity / sub-threshold content is
expressible in a per-step rate, a grid size, or a cost bound. No
constraint-1/2/3/4 metric is computed or moved anywhere in it.

**Item 5** needs the reasoning spelled out rather than copied, because it
*is* a materials statement. The article it bounds — `graded_black_shell`,
`tau_shell=24`, `eps_r≡1` — is **passive, linear and time-invariant**.
LOGBOOK's own ESTABLISHED section already records that this article
satisfies constraints 1 and 2 broadband and **fails constraint 3 by
construction** (a perfect absorber is a black shape in daylight). The
sidecar quantifies how insensitive its optical signature is to the
*material behind the coating* — a fabrication degree of freedom. It takes
**no** T1 escape route, because it proposes no escape: it is a
realizability bound on the bench's workhorse article, not a candidate
solution to the phenomenon, and must not be read as constraint-3
progress. **T1 escape route: NONE / N/A**, matching every T28
desk/instrument cycle since Iteration 46 including exp-105 through
exp-114 by name.

---

## 5. Falsifiable predicted outcomes — per-metric bands

Every band is anchored on a figure already established in this program's
record (R17: a tolerance must be justified, before the run, against the
largest already-established comparable magnitude). **No advance position
is taken on which band any metric lands in.**

### M1 — `G_short` (descriptive + gate input)

`G_short = per_step(S234) / per_step(S156)`. No pass/fail band; reported,
and consumed by the §6 budget gate as the re-projection input before the
sustained pass.

### M2 — `G_sustained` (the cycle's central measurement)

`G_sustained = per_step(U234) / per_step(U156)`. No pass/fail band of its
own; it is the operand M5/M6/M7 score.

### M3 — duration-invariance of `G` (does load degradation cancel between grids?)

Statistic: `d_dur = |G_sustained − G_short| / G_short`.

| Outcome | Condition |
|---|---|
| **CANCELS** — sustained-load degradation is grid-independent and divides out of `G` | `d_dur ≤ R_DEG/2 = 0.0379821` |
| **PARTIAL** | between |
| **DOES-NOT-CANCEL** — degradation is grid-dependent | `d_dur ≥ R_DEG = 0.0759642` |

*Anchor (R17):* `R_DEG = 0.0759642` is exp-114's own measured single-grid
(r=156) short→sustained degradation. If that effect were purely
grid-independent it would cancel in `G` exactly; a `d_dur` reaching its
full single-grid magnitude means it does not cancel at all. Not a round
number, not borrowed from a critique's illustrative "e.g."

*Refuted by:* `d_dur ≥ 0.0759642` refutes the assumption — implicit in
R31/R33 as currently written, and never before tested — that a session's
throughput factor is grid-independent.

### M4 — repeatability, and the composition rule that guards M3

Statistic: `d_rep = |G_sustained_repeat − G_sustained| / G_sustained`.

| Outcome | Condition |
|---|---|
| **REPEATABLE** | `d_rep ≤ 0.02` |
| **MARGINAL** | `0.02 < d_rep < 0.0759642` |
| **NOISY** | `d_rep ≥ R_DEG = 0.0759642` |

**Pre-registered composition rule, to be wired into code, not left in
prose (R24 discipline):** if `d_rep > R_DEG/2 = 0.0379821` — i.e. the
single-sample scatter is as large as M3's own CANCELS bar — then **M3 is
reported `UNINTERPRETABLE` and no M3 verdict is scored.** A difference
cannot be attributed to duration when repeat scatter alone spans it.
Likewise, if the §6 budget gate skips the repeat pass, `repeat_skipped`
is persisted `True`, M4 reports `UNMEASURED`, and M3 is reported with an
explicit "no repeat available" caveat rather than a clean verdict.

### M5 — PRIMARY: bench replication of exp-114's own scored statistic

`measured_ratio_B = 1.5 × G_sustained`, scored by importing and invoking
`run114.classify_kappa_exponent_check()` **unmodified** — the same
committed classifier, the same ratio-space bands, the same
`reference_ratio = 3.6680107109370383`.

| Outcome | Condition | Meaning |
|---|---|---|
| **CONFIRM** | `rel_dev ≤ 0.15` | exp-114's CONFIRM replicates independently, on a second machine, with the cross-session normalization removed algebraically and the protocol mismatch removed by design |
| **AMBIGUOUS** | `0.15 < rel_dev < 0.30` | |
| **REFUTE** | `rel_dev ≥ 0.30` | `KAPPA_COST_EXPONENT` is not portable to `kappa_ratio = 1.5` |

**Exact boundaries in the measured quantity** (so the falsifier is
checkable without re-deriving anything): with
`G_ref = 2.4453404739580256`,

- CONFIRM iff `G_sustained ∈ [2.0785394, 2.8121415]`
- REFUTE iff `G_sustained ≤ 1.7117383` or `G_sustained ≥ 3.1789426`

**What would REFUTE this cycle's own leading expectation:** exp-114's own
`G_E = 2.7455057` sits inside the CONFIRM window at 82% of the way to its
upper edge. A bench `G_sustained` above `2.8121415` moves the filed
verdict to AMBIGUOUS; above `3.1789426` it becomes a REFUTE, and
exp-114's CONFIRM-WITH-NAMED-GAPS would have to be re-framed in LOGBOOK
by forward disclosure. That is a real, reachable, verdict-moving outcome
from a ~40–100 minute measurement.

### M6 — cross-machine transfer of `G` (the direct answer to the v2 straddle)

`T = G_sustained / G_E`, with `G_E = 2.74550565394726`.

| Outcome | Condition | Meaning |
|---|---|---|
| **TRANSFERS** | `\|T − 1\| ≤ 0.15` | `G` is a machine-independent property of the computation; session-speed factors cancel out of it; R31's r=156-only control is safe to use for r=234-grid quantities, and PHOTONICS' Iteration-91 cross-grid finding is bounded at ≤15% |
| **AMBIGUOUS** | between | |
| **DOES-NOT-TRANSFER** | `\|T − 1\| ≥ 0.30` | session slowdown is grid-dependent; **no** cost verdict normalized by an r=156-only control may be scored across grids without its own grid-native control |

*Anchor (R17):* `0.15` is R28's own founding-miss magnitude
(`2.0**k/2.0**3 − 1 = 0.1529500`) reused in the same ratio space it was
measured in — exactly the anchoring exp-114's own Phase-3 Fix 1
established for this family of bands; `0.30` is double it, matching
exp-114's own band structure.

**Composition rule (coded, not prose):** `G_E` is itself
protocol-mismatched (12000-steps/scene chunked numerator vs.
3334-steps/scene cold-call denominator). If M3 reads `DOES-NOT-CANCEL`,
M6 is persisted with `g_e_protocol_caveat = True` and reported as
**directional only**, not as a scored verdict — the mismatch would then
be known to be large enough to explain the difference by itself.

### M7 — the `N²` / v2 assumption, and a secondary alternative cost model

Statistic: `excess = G_sustained / 2.25 − 1` (equivalently the per-step
superlinearity `ε(1.5) = G_sustained/2.25`), with implied exponent
`k_B = 3 + ln(G_sustained/2.25)/ln(1.5)`.

| Outcome | Condition |
|---|---|
| **N2_HOLDS** (v2's core assumption validated) | `\|excess\| ≤ 0.05` |
| **AMBIGUOUS** | between |
| **N2_FAILS** | `\|excess\| ≥ 0.1529500` |

*Anchor:* the REFUTE bar is again R28's own founding miss — which, per
§2.0, **is** the per-step superlinearity at `kappa_ratio = 2.0`,
`ε(2.0) = 2**(k−3) = 1.1529500`. So this band asks a physically exact
question: is the r=234 grid's excess over pure cell-count scaling as
large as the r=312 grid's already-established one?

**Secondary, explicitly-labelled, likely-underpowered model comparison
(pre-registered as such, with its own power condition).** Two cost models
make different predictions for `G(1.5)`:

- **constant exponent `k`** (the model currently in force):
  `G = 1.5**(k−1) = 2.4453405`
- **constant per-step superlinearity `ε`** (a machine-property model,
  never before stated in this program): `G = 2.25 × ε(2.0) = 2.5941376`

They differ by only **6.085%**, so discriminating them needs `G` measured
to better than ~3%. **Pre-registered power condition:** if
`d_rep > 0.03`, this comparison is reported `UNDERPOWERED` and **not
scored** — no model is declared favoured. Stated in advance precisely so
a post-hoc "our data prefers model X" reading is not available. For the
record, and computed here before any bench data exists: exp-114's own
`ε_E(1.5) = 1.2202247` sits 5.835% from the constant-ε prediction and
12.275% from the constant-k prediction — suggestive that the constant-k
model may be the weaker of the two, on **one** protocol-mismatched
point, which is exactly why it is filed as a hypothesis and not a claim.

### M8 — item 2: the persisted, NOT-scored sensitivities (no band; disclosure)

Persisted as explicitly-suffixed `..._DO_NOT_SCORE` fields, mirroring the
established pattern:

- `sensitivity_short_reading_DO_NOT_SCORE` — exp-114 rescored with its
  own short control reading (`speed_ratio = 0.422112913224623`):
  `rel_dev = 0.20803870`, verdict AMBIGUOUS.
- `sensitivity_v2_straddle_DO_NOT_SCORE` — the `N²`-scaling
  normalization: `measured_ratio = 3.2171956`, **signed** deviation
  `−0.12290` against the original's `+0.12275`, a 28.0% spread between
  central estimates on **opposite sides** of `reference_ratio`.
- `sustained_choice_justification` — the explicit statement Red Team
  asked for, which the §1 identity now lets me make properly rather than
  by appeal to precedent: both "sensitivities" are the **same** question
  in different clothes — *which same-session r=156 per-step rate is
  protocol-matched to the r=234 numerator*. "Sustained" is the right
  choice for this purpose not because Iteration 90 ratified it for
  cost-gate conservatism (QUANTUM is correct that this was never
  re-argued for a scientific use) but because 3334 steps/scene is the
  **closer duration match** to a 12000-steps/scene production numerator
  than 1000 steps/scene is, and exp-114's own `R_DEG = 7.596%` shows
  duration measurably matters on this axis. That is a
  protocol-commensurability argument (R9), not a conservatism argument —
  a materially different and, I argue, correct justification. **M3 tests
  it directly**, so this cycle does not merely assert it.

### M9 — item 5: the fabrication-tolerance bound (ANALYTIC SIDECAR — desk calculation, not an FDTD output)

**Expressibility contract, stated up front, following PANEL.md's own
THERMODYNAMICS sidecar language:** every number below is a post-run
analytic calculation over already-committed data, labelled as such. This
sidecar carries **no blind prediction** — its inputs are all on file, so
what it carries instead is a **code-enforced arithmetic reproduction
gate**: each cited figure must be recomputed in `analyze115.py` from its
source `results.json` and asserted equal to the value quoted here, to
`<1e-12` relative; **any mismatch HALTs the sidecar** and it is reported
`NOT-REPRODUCED` rather than published. That is the falsifiable element
this metric can honestly offer, and it is stated as the whole of it.

**(a) The measured bound.** Replacing the article's core — the strongest
available perturbation, vacuum → perfect electric conductor over the
entire inner radius — moves the far-field optical signature by:

| Channel | r=156 | r=234 | r=312 |
|---|---|---|---|
| per-bin angular pattern, max over 48 bins, margin=32 (exp-108) | `1.4760e-04` | not measured (see §3 item 3) | `1.5266e-04` |
| aggregate σ_scat (exp-112 / exp-114) | `8.359e-05` | `1.0874e-04` | — |
| aggregate σ_abs | `4.084e-05` | `5.666e-06` | — |
| aggregate σ_ext | `2.147e-05` | `5.204e-05` | — |
| **channel self-consistency floor** `\|σ_ext−σ_ext_cross\|/σ_ext` | `6.649e-06` | `2.779e-05` | — |

**(b) Floor-gate (R13 discipline, applied to my own number before I cite
it).** Those deltas sit at **0.2×–12.6×** the channel's own
optical-theorem self-consistency floor; one of the six (σ_abs at r=234)
is *below* it. **The correct statement is therefore an upper bound, not a
resolved measurement of a nonzero effect** — and I state it that way,
which is a stricter reading than my own exp-114 Phase-5 review's
"insensitive to well under 1%."

**(c) Zero-free-parameter mechanistic check.** Light reaching the core
has traversed the coating once and must traverse it again to leave, so
the core-dependent contribution to the far field is
`O(exp(−2·τ_true)) = 6.71e-08` in intensity, using exp-061's own
committed `τ_true = 8.2588` — **three orders of magnitude below anything
this instrument can resolve**, fully consistent with (b)'s reading that
the measurement is floor-limited. Sub-check, pre-registered with a HALT:
`τ_true` is recomputed from `lab/materials._graded_black`'s own committed
profile at the exp-061 member (cpl=20, `sigma_max=0.5`, 48 cells) and
must reproduce `8.258819829686677` to `<1%`; if it does not, the
`exp(−2τ)` estimate is reported `NOT-REPRODUCED` and (c) is withheld,
leaving (a)+(b) standing alone. It is then evaluated at the cpl=25 /
`sigma_max=0.4` / 60-cell member the r=234 data actually came from —
never assumed transferable, since `Im(n)` is concave in σ. *(This also
closes exp-061's own hand-carried `I_graded = 0.273840`, which I verified
this session exists nowhere as committed code.)*

**(d) The bound, written as one stated claim — the thing seven cycles
have named and none has written:**

> For the `graded_black_shell` recipe at `tau_shell = 24`, `eps_r ≡ 1`,
> λ = 600 nm, plane-wave normal incidence, in 2D TM: the article's
> far-field optical signature — per-bin angular pattern and every
> aggregate cross-section alike — is insensitive to the **core/backing
> material** at **better than 1.6×10⁻⁴ relative**, measured across a
> 2× geometric size range (r = 156 → 312, `kappa` 2.0 → 4.0), two grid
> resolutions (cpl 20 and 25), 48 angular bins, six box radii, and three
> independent energy-ledger channels. That figure is an **upper bound set
> by the instrument's own floor**, not a resolved effect; the physical
> value is predicted at `O(10⁻⁷)` by the coating's own already-committed
> optical depth. The optical function is carried entirely by a **1.440 µm
> (2.40 λ) graded-σ coating whose physical thickness is invariant across
> the whole validated size range**; the material behind it is a free
> parameter over the entire span from vacuum to a perfect conductor.
> **Fabrication consequence: a real process implementing this design does
> not need to control the substrate or core material, its optical
> constants, or its interface at all.**

**(e) Realizability tier — published / plausible / unobtainium-with-parameters.**

**UNOBTANIUM-WITH-PARAMETERS — inherited unchanged, and this finding does
not move it.** The tier is already filed at exp-061 (Iteration 38,
MATERIALS' own unconditional-lock cycle): `α_true ≈ 5.74×10⁴ cm⁻¹` is
*not* an implausible absorption rate, but the coating is asked to deliver
it in **1.44 µm** where real record-blackness CNT-forest coatings run
**100–500 µm** — a **70–350×** thickness gap, MP-2/MP-4 CONFIRMED, and
the dominant anchor-invariant falsification axis. What the tolerance
bound does is narrower and worth stating precisely: it **removes
core/backing material control from the list of things such a process
would have to get right**, leaving thickness as the binding constraint it
already was. Two forward consequences, both stated as conditionals
because that is all the evidence supports:

- *If* a future cycle re-specs this article at exp-061's own
  MP-5-plausible thickness (230–730× of 1.44 µm), the core/backing
  freedom **survives and strengthens** — the bound scales as
  `exp(−2·τ_true)` and τ_true grows with thickness, so a realizable
  coating is exponentially *more* backing-independent, not less. Stated
  as a physical argument from (c), explicitly **not** re-measured here.
- The bound says nothing whatever about constraints 3 or 4, about any T1
  escape route, or about any σ(I)/σ(x,t) mechanism. It is a fabrication
  statement about a passive article this program has already recorded as
  failing constraint 3 by construction (§4).

**Evidentiary tier disclosure (T18):** every literature figure invoked in
(e) is inherited from exp-061's own Phase-4 record, which is
**WebSearch-snippet synthesis, not primary-source-verified** — T18's
WebFetch block was still in force at 41+ consecutive attempts as of that
cycle, and this cycle attempts no new literature search. No new
realizability claim is made from new sources; the tier is cited, not
re-derived.

---

## 6. Cost estimate — via the committed cost-gate machinery, with margin

**Runtime context (stated so the estimate is honest).** Phase 4 runs on
the team bench: Dell T5820, Xeon W-2145 (8c/16t), 128 GB, WSL2 Ubuntu
24.04, python 3.11 venv — **not** the GitHub CI runner and **not** the
cloud sandbox exp-114's timing data was taken on. Trust suite on this
bench measured today: **41/41 in 87 s**, cloak stage 124 s. **This bench
has no measured per-step FDTD rate for either grid** — which is precisely
why this cycle exists, and why the budget gate below re-projects from
measured readings rather than trusting any prior.

**Grid-step budget:** 46,008 grid-steps total (23,004 per grid, 18
`Sim.run()` calls). In r=156-equivalent cost units, using exp-114's own
`G_E = 2.7455057` as the disclosed prior:
`23,004 × (1 + 2.7455057) = 86,162` r=156-equivalent steps.

**Projected wall time, bracketed by the two real per-step anchors on
file** (no bench anchor exists to interpolate between them):

| Anchor | `per_step(r=156)` | Projected total | Margin vs. `COST_GATE_TOTAL_S = 10800 s` |
|---|---|---|---|
| exp-112's session (the faster of the two) | `0.0279366 s` | **2407 s** (40.1 min) | **77.7%** |
| exp-114's session, sustained (the slower) | `0.0712102 s` | **6136 s** (102.3 min) | **43.2%** |

**Worst-anchor margin: 43.2%.** The bench is plausibly faster than
either cloud session (both cloud figures were taken under heavy disclosed
sandbox contention), but that is an expectation, not a measurement, and
the gate below does not rely on it.

**The gate itself — R27/R28-compliant, executable, causally upstream of
each expensive stage.** `COST_GATE_TOTAL_S = 10800` and
`COST_GATE_SAFETY_MARGIN = 1.10` are reused from `R110` **unmodified**.
The one disclosed deviation, in the same idiom `run114.py` used to
disclose its own: `R110.cost_gate_check()` and
`run114.cost_gate_check_r234()` both project a *full production leg* from
a pilot, and this cycle runs no production leg — so
`chunk_runner115.py::control_budget_gate()` reuses those two constants
and the same `proceed`/raise semantics, but projects the *remaining
control readings* from the readings already measured:

```
after S156:  project = per_step_S156 × 23004 × (1 + G_prior) × 1.10        [G_prior = G_E = 2.7455057]
after S234:  re-project with the MEASURED G_short in place of G_prior
after U234:  project the repeat pass from measured elapsed; if it would
             breach the bound, SKIP readings 5-6, set repeat_skipped=True
             with the reason persisted, and let M4/M3's composition rule
             (§5) degrade the verdict honestly rather than silently
```

Each projection raises `RuntimeError` before the next `Sim.run()` call
rather than after it — traced from the actual resource-consuming call
site backward, per R28's own founding lesson. The graceful-degradation
branch is deliberate: a budget breach should cost this cycle its
*repeat*, not its primary measurement.

**Policy note:** Tier-0 item 0c (whether `COST_GATE_TOTAL_S` should bound
wall-clock or compute cost) is Marsh's own pending call and is out of my
scope; I apply the constant exactly as committed, i.e. as a wall-clock
bound, and take no position.

---

## 7. Idealizations — what this cycle does and does not establish

1. **Does establish (if it runs clean):** the first per-step cost
   measurement ever taken on any grid but r=156 in this program; a
   matched-protocol, same-session, single-machine measurement of `G` free
   of every cross-session normalization exp-114's verdict depended on; a
   second-machine replication (or refutation) of that verdict; a
   bench-native R31 control for every future bench cycle to cite; and one
   written fabrication-tolerance bound with a stated realizability tier.
2. **Does NOT establish** anything about `kappa_ratio` other than `1.5`.
   `k`'s portability to `kappa_ratio = 2.0` still rests on the single
   founding pair, and to ratios above `2.0` on nothing at all. A CONFIRM
   here does not license extrapolation past `2.0`.
3. **`G` is a machine property, not a physics constant.** Everything M2
   measures characterizes an FDTD implementation on a memory hierarchy.
   M6 is the only metric that tests portability across machines, and it
   does so with `N = 2` machines — the minimum that can detect a
   difference, not enough to characterize a distribution.
4. **`G_E`'s protocol mismatch is bounded, not eliminated.** exp-114's
   r=234 numerator was checkpoint-chunked at 1000 steps/scene; this
   cycle's readings are single-call. Chunk-boundary cache effects are
   bounded at ≲5% by exp-114's own first three chunk times (204.25,
   196.83, 214.21 s — max/min = 1.088, with the *second* chunk fastest,
   so no monotone cold-start penalty is visible). Those three figures
   survive only as quotations inside `experiments/114-.../
   phase5_redteam_audit.md` §2; the scratch wall-time log they came from
   did not survive that session, so they are **cited, not independently
   re-derivable** — disclosed as such.
5. **Pickle I/O is excluded from both sides by construction**, verified
   by direct read: `chunk_runner114.py::step_budgeted` records
   `dt = time.time() − t0` around `sim.run(chunk)` only, with the
   `pickle.dump` after it, and resume `pickle.load` before `t0`. This is
   the one protocol difference that could have been large and is not.
6. **The `HISTORICAL_R156_CPL25_TOTAL_S` per-scene split remains a bare
   3-scene-blend scalar** (exp-112's `analyze.py` merge clobbered the
   per-scene dict; carried unchanged since exp-113). This cycle's own
   readings are blends by design, so nothing here needs that split — but
   it is still not recoverable, and any future per-scene claim still
   cannot use it.
7. **The sidecar's per-bin evidence is r=156/312 only.** exp-114's r=234
   captures were never persisted (§3 item 3), so the r=234 contribution
   to the bound is aggregate-only. The bound is stated over the channels
   each radius actually supplies, never averaged across them as if all
   three radii carried all channels.
8. **The sidecar's `exp(−2τ_true)` estimate is a 1-D centre-line
   Beer–Lambert argument** on a graded annulus. It ignores diffraction
   into the geometric shadow, near-tangent chords (which are *longer*
   through the annulus, so the estimate is conservative in the safe
   direction), and the `eps_r ≡ 1` idealization. It is an
   order-of-magnitude argument offered as a consistency check on (b),
   never as a replacement for the measurement.
9. **`τ_true` is validated at one member of the family.** exp-061 derived
   it at cpl=20 / `sigma_max=0.5` / 48 cells; the r=234 data is cpl=25 /
   `sigma_max=0.4` / 60 cells. `Im(n)` is concave in σ, so the two are
   not assumed equal — §5 M9(c) recomputes it at the second member and
   HALTs if the first cannot be reproduced.
10. **T18 still binds.** No primary-source literature access is attempted
    or claimed; the realizability tier in M9(e) is inherited from
    exp-061's WebSearch-snippet-tier record, disclosed at that tier.
11. **Both the bench and the two cloud sessions are multi-tenant to an
    unknown degree.** Contention is the dominant known noise source on
    every wall-time figure in this program; M4 is the only instrument
    this cycle has for it, and it samples it exactly twice.

---

## 8. Verified before proposing (R4 / R9) — what I actually checked

Read in full this session: `PANEL.md`; `LOGBOOK.md`'s RULED OUT registry
R1–R33 line by line, ESTABLISHED, and LIVE THREADS T1–T28 (T28 at its
opening, Iteration 46, and its recent closes); Iterations 88–91 in full;
`PLAN.md` lines 1–110; the complete exp-114 record (`phase1_proposal.md`,
`run114.py`, `chunk_runner114.py`, `analyze114.py`, `results.json`,
`phase5_review_materials.md`, `phase5_redteam_audit.md`);
`lab/validation/VALIDATION.md` and `lab/ARTIFACTS.md`. Grounded against
`experiments/108-.../run.py` + `results.json`, `experiments/112-.../
results.json`, `experiments/113-.../chunk_runner113.py` + `run113.py`,
`experiments/060-.../run.py`, `experiments/061-.../NOTES.md`, and
`lab/materials.py`.

**Not-previously-run verification (R4/R9), executed not assumed:**

- **This configuration has never been run.** No control burst on any grid
  but r=156 exists anywhere in the repository (grep, §2.0). `G` has never
  been computed, scored, or persisted as a quantity.
- **The load-bearing identity was re-derived, not trusted.**
  `measured_ratio ≡ kappa_ratio × G` reproduces exp-114's filed
  `4.11825848092089` bit-exact from independent primitives.
- **Every band's anchor was invoked, never hand-typed:**
  `KAPPA_COST_EXPONENT` and `COST_GATE_*` from `R110`; `G_ref` from
  `1.5**(k−1)` cross-checked against `reference_ratio/1.5`; `R_DEG` from
  exp-114's own control JSON; `ε(2.0) = 2**(k−3) = 1.1529500` confirmed
  identical to R28's own founding-miss figure.
- **Ruled-out check.** Nothing here re-proposes a ruled-out idea. Nearest
  neighbours checked explicitly: **R5's addendum** rejects `≈233/234` as
  a named-*constant* periodicity match — unrelated to r=234 as a geometry
  size (exp-114 Idealization 5, re-confirmed); **R28's** own companion
  caution is that a gate's projection formula must be checked against
  real data as soon as such data exists — which is what this cycle does,
  not contradicts; **R31/R33** are extended by measurement here, not
  circumvented — M5 removes their applicability by construction rather
  than working around them, and M6 tests the assumption they both rest
  on.
- **Rules re-read against this specific proposal:** R4 (no hand-typed
  "recomputed" figures — every number above has a stated invocation),
  R9 (operand commensurability — §2.3 is written entirely for this),
  R13 (floor-gate before citing a small ratio — M9(b)), R17 (tolerance
  anchored on the largest established comparable magnitude — every band
  in §5), R18 (a check's claimed scope must match its code — the M3/M4/M6
  composition rules are specified as code, not prose), R19 (call counts
  code-asserted — 18 `Sim.run()` calls, to be asserted), R21 (a persisted
  sidecar's headline must appear in Result prose — M9(d) is written to be
  quoted there), R23 + First Addendum (a new `DISCLAIMER_115` string
  needs **both** predictions-side and result-side asserts, in committed,
  re-invocable call sites, in this same cycle), R24 (a stated consequence
  must be wired into the classification — hence the coded composition
  rules), R25 (declined items are numbered queue lines, §3, not
  parentheticals), R27/R28 (§6's gate is executable and upstream),
  R29 (this cycle's modules will be named `run115.py`/
  `chunk_runner115.py` with executed identity assertions against
  `R110`/`R112`/`R113`/`R114`), R30/R32 (**N/A**, stated: this cycle
  produces no discriminating statistic of that class — M3/M4/M6/M7 are
  ratios of directly-measured wall times against pre-registered
  arithmetic references, with no recalibrated threshold and no asserted
  diagnostic tail), R33 (**made inapplicable by construction** for M5 —
  no scored operand mixes sessions — and disclosed, not evaded, for M6,
  which is explicitly a cross-machine comparison and is labelled one).

**One point of genuine uncertainty I could not resolve from the record,
flagged for Phase 2 rather than papered over:** exp-114's `t234` is a
*production* figure (12000 steps/scene, chunked, over hours), while every
control this program has ever taken is a short cold burst. Idealization 4
bounds the chunking half of that difference at ≲5% from three quoted
chunk times, but those three numbers are the only surviving evidence and
they are not independently re-derivable. If a critic can construct a
tighter bound — or show that a multi-hour thermal soak makes a
minutes-long burst structurally unable to represent it — M6 may need to
be demoted to directional-only regardless of what M3 reads.
