# exp-114 — Panel Iteration 91 (candidate)

**Lead seat: PHOTONICS** (rotation: VISION SCIENCE→PHOTONICS→MATERIALS→
ELECTROMAGNETISM→THERMODYNAMICS→QUANTUM OPTICS→repeat; Iteration 90 led
with VISION SCIENCE, so Iteration 91 leads here). Governance/
instrumentation cycle continuing the T28 sub-thread (opened Iteration 46,
exp-069; T1 route N/A throughout its own 45-iteration history to date).
Executes the Reconciled Iteration-91 queue's own Tier-1 item 3
(LOGBOOK.md Iteration 90 / `experiments/113-t28-r312-cpl25-plus168-bin/
phase5_redteam_audit.md` §7, `phase5_review_materials.md` Finding 4): a
cheaper intermediate-`r` calibration point (`r=234`) for the `fixedabs`
family, at `cpl=25`, chosen specifically because it does **not** depend
on the r=312 leg's own repeated cost-gate deferrals (exp-111: sequencing;
exp-112: cost/density choice; exp-113: a real, R31-scaled refusal) and
can proceed in parallel with that still-blocked thread.

**A note on this seat's own charter fit, stated up front**: this is
instrument-calibration/cost-gate work on this program's own measurement
machinery, not a phenomenon-mechanism proposal. My own charter question
("is the proposal's optical response coherent as stated, across
wavelength and angle?") does not bind on the calibration question itself
(a wall-time exponent and a cost-gate projection are not an optical
response) — but it **does** bind on verifying that `geom_fixedabs_cpl`
still constructs a physically sensible, self-consistent shell/coating
geometry at this new `r` (tau_shell held invariant, `R_CORE`/`R_COAT`
proportioned identically to the already-validated r=156/312 members of
the same family) before any FDTD spend is proposed on it — which §2,
below, verifies directly, not by assertion.

## 1. Mechanism/execution narrative (≤300 words)

Before committing to `r=234` as the Director's brief specifically
authorized me to reconsider, I checked two things this program's own
house discipline requires (R4/R9): (a) whether `r=234` is redundant with
an `r` this program has already measured for the `fixedabs` family — it
is not; a direct grep of every experiment directory for `r=234`/
`R_COAT=234`/`geom_fixedabs_cpl(234` found zero prior FDTD runs at this
`r` (only two informal Phase-5 *proposals* to use it, for two **different**
purposes — see Idealization 4); (b) whether its estimated cost, computed
from the actual committed cost-gate code (never hand-derived), is safely
inside `COST_GATE_TOTAL_S`. Both checks pass — see §2.0.

The leg itself: run the `fixedabs` family's three standard scenes (empty,
hollow-article, PEC-cored-article) at `r=234`, `cpl=25` — the same
congruent `cpl=20→25` refinement recipe (`geom_fixedabs_cpl`, reused
unmodified from `run112.py`) already validated at r=156/312. This gives,
for the first time, a real `(t156, t234)` wall-time pair at
`kappa_ratio=1.5` — a **genuinely different** ratio from the single
`kappa_ratio=2.0` pair (`r=156→312`, exp-110) `KAPPA_COST_EXPONENT`
(`≈3.2053`) has ever been fit from or tested against. This lets the
cost-scaling exponent be checked for kappa-ratio-invariance for the first
time since its founding (R28's own standing caveat: "this exponent has
not been validated at any other kappa_ratio"). At zero additional
marginal FDTD cost, the same three captures also let exp-113's own Fix 1
(`box_a` clearance in wavelengths) and Fix 2 (sponge-margin figures) be
re-verified at a third geometry.

This document does **not** propose, vary, or score any
σ(I)/σ(x,t)/angular-selectivity/sub-threshold content, and does **not**
re-engage the separate `shape_ratio_fixedabs≡2^n` physics question
(kappa_window's own near-field-collapse exponent, `n≈4.31`, exp-105/106
— a materially different quantity from this document's own cost exponent;
see Idealization 4 for why conflating the two would be an R9-class
error).

## 2. Parameter table

### 2.0 Grounding-fact verification (independently run this session, before proposing anything — R4 discipline)

| Claim | Checked | Result |
|---|---|---|
| `r=234` has never been used for the `fixedabs` family in this program | `grep -rn "r=234\|R_COAT.\{0,3\}234\|geom_fixedabs_cpl(234\|geom(234\|kappa_of(234" experiments/` | Zero prior FDTD runs at this `r`. Two prior *informal Phase-5 proposals* to use it (never executed): PHOTONICS' own Iteration-83 review (exp-106, `phase5_review_photonics.md:269`, for a **fourth point on the `shape_ratio_fixedabs≡2^n` physics fit**) and MATERIALS' own Iteration-90 review (exp-113, `phase5_review_materials.md:200-247`, for **this document's own cost exponent**) — two different quantities, disambiguated in Idealization 4. |
| `geom_fixedabs_cpl(234, cpl)` reduces exactly to `R110.geom_fixedabs(234)` at `cpl=20` (a genuinely new evaluation point of an already-committed, generic formula — never checked at this `r` before) | `python3 run114.py --verify-geometry` (re-run fresh this session) | `{"pass_": true, "mismatches": []}` at **all three** r=156, 234 (new), 312 — extends `run112.py`'s own check (previously r∈{156,312} only). |
| `KAPPA_COST_EXPONENT`'s own founding data (not hand-typed, reused verbatim) | `R110.KAPPA_COST_EXPONENT` | `3.2053299988171697` — fit from exactly ONE `(t156,t312)` pair at `cpl=20`, `kappa_ratio=kappa_of(312)/kappa_of(156)=2.0` (exp-110/exp-111, R28). |
| `kappa_of(234)` | `R110.kappa_of(234)` (`=r/78`, reused unmodified) | `3.0` exactly. |
| The new ratio this leg adds | `kappa_of(234)/kappa_of(156)` | `1.5` — a genuinely different ratio from the only one `KAPPA_COST_EXPONENT` has ever been measured at (`2.0`). |
| Projected cost multiplier at this new ratio | `1.5 ** KAPPA_COST_EXPONENT` (invoked, not hand-typed) | `3.6680107109370383`. |
| Projected cost multiplier at the already-attempted r=312 ratio, for comparison | `2.0 ** KAPPA_COST_EXPONENT` | `9.223600318696624` — matches exp-110/111/113's own committed figure bit-exact. |
| Ratio of the two multipliers (**this leg's own cost relative to the refused r=312 leg**) | `(1.5**k)/(2.0**k)` | `0.39767667550618246` (≈**39.8%**) — **an R4 correction to MATERIALS' own Iteration-90 Phase-5 review** (exp-113, Finding 4), which estimated `"1.5**3.2 ≈ 2.98×"` and "about 32%" without invoking the actual formula. Independently re-derived here by direct execution: the true multiplier is `3.668×`, not `2.98×`, and the true ratio is `≈39.8%`, not `≈32%`. Non-fatal to that review's own qualitative conclusion (r=234 remains comfortably the cheaper option) — but a real, disclosed citation discrepancy, not silently propagated forward. |
| Projected r=234 total wall time, UNCONTROLLED (as if this session matches the historical throughput exactly — **not** the gating figure, R31 applies) | `cost_gate_check_r234(670.4778/3.0, 670.4778)` (the real committed function, this document's own `run114.py`) | `{"projected_234_total_s": 2705.2516053872732, "pilot_pass": true, "total_pass": true, "proceed_to_r234": true}` — 75.0% margin under `COST_GATE_TOTAL_S=10800s` if this reading held. Compare: the already-attempted r=312 leg's own analogous uncontrolled reading was `6802.6s` (37% margin) — which **still failed** once R31-controlled for real (`16737.4s`, REFUSED, exp-113). This leg's own uncontrolled margin is nearly double r=312's own uncontrolled margin (75.0% vs. 37%), for a projection built from the identical formula and the identical historical pilot — consistent with, not a coincidence given, the lower `kappa_ratio`. |
| The historical `cpl=25`/r=156 pilot total (this leg's own R31 baseline, reused not re-derived) | `EXP112_RESULTS["total_wall_s"]` (`experiments/112-.../results.json`) | `670.4777698516846` — the same bare scalar exp-113 already found genuinely unrecoverable per-scene (Idealization 1, carried forward unchanged, not re-litigated here). |

### 2.1 Geometry — congruent `cpl=20→25` refinement, r=234, fixedabs family (unchanged construction, new `r`)

| Quantity | `cpl=20` (new this cycle) | `cpl=25` (this cycle's own real leg) |
|---|---|---|
| Domain `N` (cells, square) | 1680 | **2100** |
| `CX`, `CY` | 756, 840 | **945, 1050** |
| `SRC_X` | 192 | **240** |
| `STEPS` | 9600 | **12000** |
| `R_CORE` | 186 | **232** |
| `R_COAT` | 234 | **292** |
| `sigma_max` | 0.5 | **0.4** |
| `tau_shell` (invariant, by construction — verified `==24.0` at r=156/234/312 in `run114.py`'s own printed assertions) | 24.0 | 24.0 |
| `ABSORB`/`EDGE` (PML-taper/source-taper, cells) | 40 | **50** (identical to r=156/312 at cpl=25 — confirmed by assertion, `run114.py`) |
| `box_a` (margin=32) | — | **(533, 1357, 638, 1462)** |
| `ref` (incident-intensity strip) | — | **(945, 1050, 225)** |

**FDTD calls this leg: 3** (empty, hollow-article, PEC-cored-article,
`r=234` only, `cpl=25`). **STEPS per scene: 12000; total steps: 36000**
(vs. r=156's 24000 and r=312's 48000 at the same `cpl` — sits exactly
between them, as `kappa_of(234)=3.0` sits between `kappa_of(156)=2.0` and
`kappa_of(312)=4.0`). Grid cell-count ratio to r=156 at the same `cpl`:
`(2100/1680)²=2.25`.

### 2.2 The falsifiable question this leg answers

**Does `KAPPA_COST_EXPONENT≈3.2053` (fit from a single `kappa_ratio=2.0`
pair) generalize to `kappa_ratio=1.5`?** Full bands in §5. This is the
falsifiable heart of the cycle — everything else (Fix 1/Fix 2
re-verification) is a zero-marginal-cost bonus on the same captures, not
this leg's own primary question.

## 3. Scope decision: r=234 alone, R31-gated, no further bundling

**r=234-alone**, matching the queue's own item 3 exactly. I decline to
also attempt: the still-blocked r=312 leg itself (the queue's own item 1,
explicitly a **parallel**, not competing, thread — a different Director
session's own call, gated on a fresh R31 control this document does not
supply); the `resolved_unresolved_crosstab` item 2 (has no real r=312
data to run against yet); any named-bin Check A/B/C classification at
r=234 (this leg was never scoped by the Director's brief as a named-bin
question, and building the additional per-margin/per-bin capture and
classification machinery exp-108/110/112/113 use would repeat the
"density" pattern Red Team has flagged in multiple recent T28 cycles for
no falsifiable question this document actually asks); and the
`shape_ratio_fixedabs≡2^n` physics fourth-point question (MATERIALS' own
charter question, a different exponent, deliberately out of scope — see
Idealization 4). Each is a real, named, undropped debt, not silently
dropped.

## 4. T1 escape route: N/A

Confirmed structurally, independent of outcome: this document changes
only a geometry-scaling function's own evaluation point (`r=234`, already
generic in `r`, reused unmodified), a checkpoint/resume capture driver,
and a wall-time exponent's own generalization check. No
σ(I)/σ(x,t)/angular-selectivity/sub-threshold content is expressible in a
grid size, a wall-clock ratio, or a cost-gate bound. No constraint-1/2/3/4
verdict is scored or moved anywhere in this document — matching every T28
desk/instrument cycle since Iteration 46, including exp-105 through
exp-113 by name.

## 5. Falsifiable predicted outcomes — numeric bands

Verbatim from `run114.py::build_predictions_text()` (re-run this session,
§2.0), restated here per this document's own format requirement (the
predictions text itself remains the single source of truth — R23
discipline):

**Geometry identity** (zero-FDTD, pre-Phase-4): `verify_geometry_identity()`
returns `pass_=True` at r=156, 234 (new), AND 312. Falsified by any
mismatch — HALT before any `Sim.run()` call. **Already run, PASS** (§2.0).

**Cost gate**: UNCONTROLLED projected total = `2705.3s` vs. the `10800s`
bound (75.0% margin if this reading held) — **explicitly not the gating
figure**. R31 (LOGBOOK.md, founding instance exp-112, ratified Iteration
89) requires a fresh same-session control point (`chunk_runner114.py
--control`, reusing `run113.py`'s own `r31_control_ratio`/
`combine_control_readings` unmodified) before `proceed_to_r234` governs
any real spend — `chunk_runner114.py::check_cost_gate_for_r234` raises
rather than proceeds if no control point is on file, exactly as
`chunk_runner113.py` did for r=312. `proceed_to_r234` may read `False`
even though the uncontrolled projection looks comfortable — exp-113's own
r=312 leg is the standing cautionary instance (37% uncontrolled margin,
REFUSED once R31-controlled for real).

**`kappa_exponent` generalization check** (the falsifiable heart of this
cycle): once real `t156` (already on file, `670.4778s`) and a fresh real
`t234` both exist, `refit_kappa_exponent()` computes `exponent_234 =
ln(t234/t156)/ln(1.5)`, scored against `KAPPA_COST_EXPONENT=
3.2053299988`:

| Outcome | Condition |
|---|---|
| CONFIRM (generalizes across `kappa_ratio`) | relative deviation ≤ 0.15 |
| AMBIGUOUS | 0.15 < relative deviation < 0.30 |
| REFUTE (`kappa_exponent` is `kappa_ratio`-dependent, not a portable constant) | relative deviation ≥ 0.30 |

The `0.15` CONFIRM band is not an arbitrary round number: it matches
R28's own already-tolerated founding miss magnitude (the ORIGINAL
hardcoded exponent, `3.0`, missed the real measured r=312/r=156 ratio by
`≈15%` before `KAPPA_COST_EXPONENT` was fit at all) — a deviation at or
below that scale is "no surprise, matches this program's own already-
accepted single-point calibration uncertainty," not a new finding. The
`0.30` REFUTE band is double that — a deviation this large would be
positive, falsifiable evidence that the cost law genuinely depends on
`kappa_ratio` rather than being a single portable constant, a genuinely
new and useful finding either way. **No advance position is taken on
which band this leg's own real data will land in.**

**Fix 1** (`box_a` clearance in wavelengths, zero-FDTD, computable now):
`3.2λ` at r=156, `4.8λ` at r=234 (new — sits exactly at the linear
midpoint between 3.2 and 6.4, as expected since `box_a`'s own clearance
scales linearly with `kappa_of(r)` by construction), `6.4λ` at r=312 — a
geometry fact, not a pass/fail band, reported for continuity with
exp-113's own finding.

**Fix 2** (sponge-margin figures): the domain-edge sponge's own one-way
accumulated log-attenuation is IDENTICAL at r=234 to r=156/312
(`17.242357`, `exp(-17.242357)=3.249×10⁻⁸`, confirmed `absorb=50`
identical at all three r) — the margin-against-signal/floor split
(exp-113's own three-way figures) cannot be computed until Phase 4
produces a real r=234 measurement to compare against; not predicted here.

**R30/R32 applicability**: N/A, stated explicitly. This document produces
no discriminating statistic of the kind R30/R32 govern (a spatial-
correlation/threshold reading needing null-calibration, or a
recalibrated statistic's direction needing independent validation) — it
produces a wall-time calibration point and two geometry-derived
re-verifications. If a future cycle extends this leg to a named-bin
Check A/B/C classification at r=234 (declined here, §3), R30/R32 would
then apply to that extension, not retroactively to this document.

## 6. Idealizations — what this leg does and does not establish

- **Does establish**: a real, executed `(t156, t234)` wall-time pair at
  `kappa_ratio=1.5` — the first time `KAPPA_COST_EXPONENT` has ever been
  tested at a ratio other than the single `2.0` it was fit from; a
  re-verification of `geom_fixedabs_cpl`'s own genericity in `r` at a
  third, previously-unevaluated point; a re-verification of Fix 1/Fix 2's
  own geometry-derived figures at that third point.
- **Does NOT establish**: whether `KAPPA_COST_EXPONENT` holds at ratios
  larger than `2.0` (e.g. a hypothetical `r=624` point, named but never
  executed since exp-108/110) — this leg's own ratio (`1.5`) sits
  strictly *below*, not above, the only ratio on file; a REFUTE verdict
  here would be positive evidence of ratio-dependence generally, but a
  CONFIRM verdict here does not, by itself, license extrapolating
  `KAPPA_COST_EXPONENT` to ratios beyond `2.0`.
- **Does NOT establish** anything about the `shape_ratio_fixedabs≡2^n`
  physics question (kappa_window's own near-field-collapse exponent) —
  see Idealization 4.
- **Idealization 1 (carried forward, unchanged, from exp-113)**: the
  cross-session historical wall-time breakdown
  (`HISTORICAL_R156_CPL25_TOTAL_S`) is a bare 3-scene-blend scalar, not a
  per-scene measurement — `exp-112`'s own `analyze.py` merge clobbered the
  per-scene dict, as exp-113 already found and disclosed. This leg's own
  `pilot_empty_wall_s` estimate (`670.4778/3`) inherits that same averaged,
  not measured, per-scene split.
- **Idealization 2 (carried forward, unchanged, from exp-113)**: the
  projected cost above is explicitly provisional until Phase 4's own R31
  control runs — assumes this session's own compute throughput matches
  the historical (Iteration 89) session's exactly. `chunk_runner114.py`'s
  own `check_cost_gate_for_r234` raises, rather than silently proceeding,
  if `proceed_to_r234` reads `False` once the real control is measured.
- **Idealization 3 — no named-bin/angular-pattern instrument is invoked
  this leg** (§3): the "reproduction/self-consistency precondition" in
  §5's predictions text is conditional ("if the angular-pattern
  instrument is invoked at all this cycle") precisely because this
  document's own scope does not require it — `window_stats()`/wall-time
  capture alone answers this leg's own falsifiable question. If a future
  Phase-4 execution or a later cycle also computes
  `angular_scattered_pattern` at r=234 (free, since the same captures
  already exist), that reproduction check must still be run and reported
  before any such downstream figure is trusted.
- **Idealization 4 — `r=234` has been proposed twice before in this
  program's history, for two DIFFERENT, unrelated quantities; this
  document concerns only one of them.** PHOTONICS' own Iteration-83
  Phase-5 review (exp-106, `phase5_review_photonics.md:264-275`) named
  `r=234` as a candidate **fourth point to break the two-point degeneracy
  of `kappa_window`'s own forced `shape_ratio≡2^n` PHYSICS fit**
  (`n≈4.31`, a near-field-diffraction-collapse exponent) — never
  executed. MATERIALS' own Iteration-90 Phase-5 review (exp-113,
  `phase5_review_materials.md:198-218`) independently named `r=234` as a
  cheap **third calibration point for `KAPPA_COST_EXPONENT`** — the
  wall-time cost-scaling exponent this document actually concerns. These
  are materially different quantities (one governs a near-field optical
  intensity ratio's own scaling with `r`; the other governs FDTD wall-time
  cost's own scaling with `r`) that happen to share a candidate `r`-value
  by coincidence of both being "a point between 156 and 312." This
  document scopes itself to the cost exponent only (§3) — it does not
  compute, cite, or extend `shape_ratio_fixedabs` at r=234 anywhere.
  A future cycle that DOES want the physics fourth-point question could,
  in principle, reuse this leg's own three captures at zero additional
  marginal FDTD cost (the same `window_stats()` machinery `run106.py`
  used) — but would need to independently address the `CPL_RATIO`
  confound this program's own R30 finding (exp-113) established for
  flux-derived quantities under a `cpl=20→25` refinement, since the
  established `shape_ratio` fit is at `cpl=20` throughout and this leg
  runs at `cpl=25` — not addressed or assumed resolved here.
- **Idealization 5 — the numeral `234` also appears in this program's own
  RULED-OUT registry, for a THIRD, unrelated reason.** R5's own addendum
  (exp-070, Iteration 47) named `A_alt≈3·R_OUT=233/234` as a REJECTED
  named-constant match for T28's own `≈2.84°` periodicity mechanism — a
  dense-search coincidence independently shown statistically
  indistinguishable from chance (`null_p≈0.204–0.806` across the
  candidate matches checked, a 20,000-trial null-permutation control).
  That finding concerns a periodicity-**mechanism** candidate for a
  wholly different question (T28's own angular signal) and has nothing
  to do with `r=234` as a **geometry size** for this cost-calibration
  leg — stated explicitly so this proposal is not mistaken for a
  re-litigation of a ruled-out idea. It is not: R5's ruling concerns a
  small-integer bookkeeping-constant coincidence search; this document
  proposes running a real, physically-motivated intermediate geometry
  size for a stated, falsifiable, unrelated purpose.
