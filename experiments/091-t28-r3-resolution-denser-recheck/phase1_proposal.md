# PHASE 1 — PROPOSAL · Panel Iteration 68 · exp-091 · Lead seat: MATERIALS & METAMATERIALS

## "R3 Resolution & Denser Recheck" — the still-overdue cpl 20→30 resolution check on the C40/G40 `PAIR_PAD` ambient channel, run jointly with a tighter-settling native-cpl repeat, at θ=37.2°/40.2°/41.4°

### 1. Mechanism/method narrative (≤300 words)

Every headline number the T28 caution zone (exp-090) and the combined
angle census (exp-089) rest on — `delta_scene(θ)`, `frac_contrast(θ)`,
and the `ratio_k(θ)` classifications built from them — has been measured
on the AMBIENT instrument (`lab/ambient.py::contrast_from_runs`) at one,
never-varied grid resolution: `cpl=20`, 600nm. I (MATERIALS) flagged this
gap at exp-088, exp-089, and exp-090's own Phase-2/5 reviews as
undischarged and specifically load-bearing at 40.2°/41.4° — the two
angles setting the caution zone's own *lower* edge, each sitting only
0.065°/0.061° from its nearest `delta_scene` zero-crossing (R13's own
hazard class), where a resolution-driven shift in the crossing's own
location could move `frac_contrast` by a large fraction of its own
value. R3 — this program's own meta-rule that any surprising or
load-bearing feature gets a resolution check before a mechanism debate
proceeds — has never been applied to this specific channel. A partial
scaffold exists (`experiments/069-.../design_geometry.py`, `R3_CONFIGS`)
but builds only `C40_R3`/`C80_R3` — there is no `G40_R3`, so the C40/G40
`PAIR_PAD` this entire sub-thread depends on has never been
resolution-checked at all.

This cycle discharges that gap directly: add the missing `G40_R3`
config (an architecturally trivial extension — its cell footprint and
measured cost basis already equal `C80_R3`'s, exactly, by the same
pad-driven construction that makes native `G40` equal native `C80`'s
cost today), re-run the AMBIENT instrument at `cpl=30` for both configs
at the three T28 census angles, and compare against the already-
committed `cpl=20` values. Jointly, it runs a tighter-settling
(`STEPS=4200`, not 2800) native-`cpl` repeat at the same three angles —
testing reproducibility and directly relieving 37.2°'s own separately-
flagged "felt-lucky" noise-floor margin — plus a dedicated settling
spot-check at `R3_STEPS=4200` itself, never independently verified
since exp-069 adopted it by convention. This is pure instrument
recalibration: no new mechanism claim, `REALIZABILITY_MEMO.md`
untouched.

### 2. Parameter table

**2a. The missing `G40_R3` config — the one new geometry object this
cycle adds to `experiments/069-.../design_geometry.py`'s `R3_CONFIGS`.**
`R3_RATIO=1.5` (unchanged, exp-069's own established rescale, applied
here for the first time to the `G40` pad-only-control branch of the
pair):

| Quantity | Native `G40` (`dg065.CONFIGS["G40"]` = `config(40, 40)`) | `G40_R3` (this cycle, `r3_config(60, 60)`) | Derivation |
|---|---|---|---|
| `absorb` | 40 | **60** | `round(40 × 1.5)` — identical scaling `C40→C40_R3` (40→60) already applies |
| `pad` | 40 | **60** | `round(40 × 1.5)` — identical scaling `C80→C80_R3` (40→60) already applies |
| `nx` | 440 | **660** | `R3_BASE_NX(540) + 2×60` |
| `ny` | 1664 | **2496** | `R3_BASE_NY(2376) + 2×60` |
| `A` (half-aperture, cells) | 752 | **1128** | `R3_BASE_OBJ_Y − R3_BASE_ABSORB = 1188−60`; **pad-independent by construction** (`r3_config`'s `A = obj_y − y_lo`, and both `obj_y` and `y_lo` carry the identical `+pad` shift) — so `G40_R3["A"] == C40_R3["A"] == C80_R3["A"] == round(752×1.5)=1128` holds automatically, extending `dg069`'s existing three-way congruence assertion to all three R3 configs with zero new arithmetic risk |
| cells (`nx×ny`) | 732,160 | **1,647,360** | — |
| **Cell footprint vs. `C80_R3`** | (native `G40`≡native `C80`: both `pad=40`) | **identical to `C80_R3`** (`nx=660, ny=2496`, both `pad=60`) | same construction identity that already holds at native resolution |
| Cost basis | `dg065.CPU_S_PER_CALL["G40"]=34.8s` (measured, **equal to** `["C80"]=34.8s` — identical cell footprint) | inherits `C80`'s native basis via `dg069._cost("C80", steps, cell_ratio)` | `dg069`'s existing `_cost()` formula needs **no new measurement** — `G40_R3`'s cost is `C80_R3`'s cost, by the same identical-footprint fact that already holds natively |
| `DX_M` (physical cell pitch, 600nm) | 30.0×10⁻⁹ m (`cpl=20`) | **20.0×10⁻⁹ m** (`cpl=30`) | `600nm / cpl` |
| `L_GEOMETRIC_M` (`R_OUT×DX_M`) | `78×30nm = 2.34×10⁻⁶ m` | `117×20nm = 2.34×10⁻⁶ m` | **identical physical size**, cross-check that the R3 rescale genuinely holds the object fixed in physical units |

**2b. Angles, pair, steps — the census/repeat/R3 matrix.**

| Quantity | Value | Source |
|---|---|---|
| `PAIR_KEYS` | `("C40", "G40")` | exp-087/088/089/090, unchanged |
| `PAIR_KEYS_R3` | `("C40_R3", "G40_R3")` | `C40_R3` exists (`dg069`); `G40_R3` added this cycle (§2a) |
| λ | 600 nm | unchanged, matches every T28 cycle to date |
| `ANGLES` | `{37.2°, 40.2°, 41.4°}` = `dg069.DENSE_ANGLES[6],[21],[27]` | identical to exp-089's own set, re-measured, not re-selected |
| **Leg 1 — native-`cpl` repeat** | `cpl=20`, `STEPS=4200` (vs. exp-089's filed `STEPS=2800`) | tighter-settling repeat, mirrors `STEPS_STRESS=4200` at native `cpl`, `dg069` |
| **Leg 2 — R3 leg** | `cpl=30`, `STEPS=R3_STEPS=4200` | `dg069.R3_STEPS = round(2800×1.5)`, unchanged constant, first use with `G40_R3` |
| **Leg 3 — R3 settling spot-check** | `cpl=30`, `STEPS=6300 (=4200×1.5)`, θ=40.2° only, both configs | new this cycle — the R3_STEPS=4200 convention has never itself been settling-verified (§4c) |
| `BOX_CLEARANCE_A` (native) / `_R3` | 12 / **18** | `round(12×1.5)`, same scaling principle as every other R3 constant |
| `BOX_CLEARANCE_B` (native) / `_R3` | 24 / **36** | `round(24×1.5)` |
| `REF_HALF_H` (native) / `_R3` | 80 / **120** | `round(80×1.5)` |
| `XI_TOL`, `NOISE_MULT`, `RATIO_LOW/HIGH` | 0.12, 3.0, 0.1/10.0 | unchanged house constants, exp-087–090 |
| `FLOOR` (applied, not recomputed) | `1.91744×10⁻⁴` | exp-088's `FLOOR_FRAC(0.10)×RMS[frac_contrast]` over exp-083's native-`cpl` 31-point window — reused as-is against the new `cpl=30` numbers (Idealization 6: this is a disclosed mixed-resolution comparison, not a claim that `FLOOR` itself is R3-verified) |
| `frac_contrast(θ)`, `cpl=20`, cited | 37.2°: `4.162655×10⁻⁴`; 40.2°: `2.830881×10⁻⁴`; 41.4°: `2.510967×10⁻⁴` | exp-083/089 `results.json`, bit-exact citations |
| `delta_scene(θ)` sign, `cpl=20`, cited | 37.2°: **+** (`2.348254×10⁻⁴`); 40.2°: **−** (`−1.540815×10⁻⁴`); 41.4°: **+** (`1.337362×10⁻⁴`) | exp-083 `results.json::per_theta` |
| `ratio_k(θ)`, `cpl=20`, filed classification | 37.2°: `3.4433` → **CONSISTENT**; 40.2°: `25.0820` → **ENERGY-DOMINANT**; 41.4°: `28.8072` → **ENERGY-DOMINANT** | exp-089/090 |

**2c. Exact new FDTD call count — 28 calls total.**

| # | Config | θ | Leg | `cpl` | STEPS |
|---|---|---|---|---|---|
| 1–4 | C40 | 37.2° | empty, article | 20 | 4200 |
| 5–8 | G40 | 37.2° | empty, article | 20 | 4200 |
| — | *(repeat block continues identically for 40.2°, 41.4°)* | | | | |
| 9–12 | C40 | 40.2°/41.4° | empty, article ×2 angles | 20 | 4200 |
| 13–16 | G40 | 40.2°/41.4° | empty, article ×2 angles | 20 | 4200 |
| 17–20 | C40_R3 | 37.2°/40.2°/41.4° | empty, article | 30 | 4200 |
| 21–24 | G40_R3 | 37.2°/40.2°/41.4° | empty, article | 30 | 4200 |
| 25–26 | C40_R3 | 40.2° | empty, article | 30 | 6300 |
| 27–28 | G40_R3 | 40.2° | empty, article | 30 | 6300 |

= 12 (native repeat) + 12 (R3 leg) + 4 (R3 settling spot-check) = **28**.
(Rows 1–16 above are written compactly; the literal grid is 2 configs ×
3 angles × 2 legs = 12 calls for the native repeat, 2 configs × 3
angles × 2 legs = 12 for the R3 leg, 2 configs × 1 angle × 2 legs = 4
for the spot-check.)

**2d. Cost estimate (hand-computed via `dg069`'s own `_cost()` formula,
disclosed as an estimate, not a measurement — matching `dg065`'s own
convention for an unmeasured config, e.g. its `C70` interpolation):**

`_cost(key, steps, cell_ratio) = CPU_S_PER_CALL_1400[key] × (steps/1400) × cell_ratio`

| Block | `cell_ratio` | CPU-s | 
|---|---|---|
| Native repeat (`STEPS=4200`, `cell_ratio=1`) | 1 | `3×2×(75.0+104.4)=1076.4` |
| R3 leg (`STEPS=4200`, `cell_ratio=2.25`) | `1.5²` | `3×2×(168.75+234.9)=2421.9` |
| R3 settling spot-check (`STEPS=6300`, `cell_ratio=2.25`) | `1.5²` | `2×(253.125+352.35)=1211.0` |
| **Total** | | **4709.3 CPU-s ≈ 78.5 CPU-min** |

Wall time at `N_WORKERS=4`, `PARALLEL_EFFICIENCY=0.98`,
`OVERHEAD_FACTOR=1.15` (unchanged house constants): `wall_s = 1.15 ×
4709.3 / (4×0.98) ≈ 1382s ≈ 23.0 min`; 3× safety envelope ≈ 69 min —
inside every established T28 per-cycle FDTD budget, and consistent with
the Director's brief's own independent ~15–20 min hand-estimate (this
estimate runs slightly higher because it prices the settling spot-check
explicitly, at `STEPS=6300`, which the brief's estimate did not itemize).

### 3. T1 escape route

**N/A (T28 desk/instrument-calibration work), stated plainly — this
cycle does not itself advance a T1-escape-route mechanism claim.** Like
every T28 cycle since exp-069, this makes no phenomenon-mechanism
proposal and takes no position on σ(I) / σ(x,t) / angular selectivity /
sub-threshold operation. It **calibrates the measurement instrument**
(the AMBIENT/box-ledger pipeline and its R13/R14 floor-and-numerator
disciplines) that any future T1-mechanism claim on this channel would
be scored against — it does not itself move any constraint-1–4 needle,
and Checkpoint criterion 2 is N/A, matching every T28 desk/instrument
cycle on record.

### 4. Falsifiable predicted outcomes (committed before any code exists)

**Carried idealizations banner (mandatory at both this section and the
future Result section, per the Iteration-65 CHECKPOINT's own escalated,
non-discretionary rule — restated here, not stated once and dropped):**
every finding below is governed by Idealizations 3/7/8 (§5): NETD is
not a human-eye threshold; this cycle does not test constraint 1/2/3/4
or re-open `REALIZABILITY_MEMO.md`; `FLOOR`/`RMS[frac_contrast]` remain
`graded_black_shell`/600nm-specific and are applied here, unrecomputed,
against newly `cpl=30`-measured numbers (a disclosed mixed-resolution
comparison).

**(a) PRIMARY — does `frac_contrast`/`delta_scene` survive `cpl` 20→30
at all three angles?** Tolerance: **ratio `frac_contrast_R3(θ) /
frac_contrast_cpl20(θ) ∈ [0.3, 3.0]` AND same sign of `delta_scene(θ)`
at all three angles is CONFIRM.** This exact band is not invented for
this cycle — it is exp-069's own pre-registered P-069-5 CONFIRM band,
applied to the sibling `delta(θ)=C(config)−C(C40)` construction on the
identical resolution-rescale idiom (there, `C80−C40`; here, `G40−C40`),
reused rather than re-derived because both are the same physical
quantity class (a small ambient-contrast difference between two
congruent boundary/padding constructions) measured by the identical
instrument under the identical rescale. **REFUTE:** a sign flip in
`delta_scene` at any of the three angles, or a ratio outside `[0.1,
10]` at any angle. **Anything else (ratio inside `[0.1,0.3)` or
`(3.0,10]`, sign held) is reported as its own NEITHER outcome,
disclosed, not smoothed into either bucket** — matching exp-069's own
three-outcome convention. This is a genuinely two-sided test: 40.2°
and 41.4° sit only 0.065°/0.061° from a `delta_scene` zero-crossing —
closer, relative to their own `frac_contrast` value, than any point
this program has ever sent through this specific resolution check — so
a REFUTE at either is a live, disclosed possibility, not a formality.

**(b) PRIMARY — does the `ratio_k` classification (CONSISTENT /
ENERGY-DOMINANT) match between `cpl=20` and `cpl=30`, applying the
*existing*, unrecomputed `FLOOR`/`RATIO_HIGH=10` thresholds to the new
`cpl=30` numbers?** **37.2° — predicted PRESERVED (CONSISTENT),
moderate-high confidence:** its `cpl=20` `ratio_k=3.44` sits comfortably
mid-band (3.4× shy of `RATIO_HIGH`), and it is the most crossing-distant
of the three (0.073°). **40.2°/41.4° — no confident lean, stated
plainly, not hedged into a default:** both read `cpl=20` ENERGY-DOMINANT
at `ratio_k≈25–29`, but this is not a wide margin against `RATIO_HIGH`
in resolution-robustness terms — even a full pass of (a)'s own CONFIRM
band (a 3× *downward* shift in `frac_contrast_R3` is inside `[0.3,
3.0]`) is, by itself, enough arithmetic room to pull `ratio_k` from
~25–29 down through `RATIO_HIGH=10` at either angle, since `ratio_k`
scales inversely with `frac_contrast` at fixed `frac_p_abs`. **A
CONFIRM on (a) therefore does NOT imply a hold on (b) — the two are
pre-registered as logically separable outcomes, and either combination
(hold/hold, hold/flip, flip/flip) is treated as an equally informative,
scientifically load-bearing result**, exactly as exp-089 pre-registered
the identical honest non-lean at these same two angles for the analogous
question one cycle ago.

**(c) Settling-adequacy, two parts:**
- **(c1) Native-`cpl` reproducibility.** `C_empty(C40/G40, θ, STEPS=4200,
  cpl=20)` predicted to reproduce exp-083's own committed `STEPS=2800`
  `C_empty` at the same 3 angles within **≤1% relative** (CONFIRM,
  reusing P-069-4's own exact band) at all 6 cells (3 angles × 2
  configs). **REFUTE:** ≥5% relative at any cell — would mean
  `STEPS=2800` was NOT in fact settled at these specific angles, an
  independently important finding for every prior T28 citation built on
  it (exp-083/087/088/089/090 all used `STEPS=2800` as "settled").
- **(c2) R3-resolution settling spot-check (new instrument, first-ever
  use).** `R3_STEPS=4200` has been the R3-rescale's own settled-floor
  convention since exp-069, but was never independently settling-tested
  *at* `cpl=30` — only at native `cpl` (Block SETTLE-C80, P-069-4) and
  only implicitly assumed adequate by the `×1.5` scaling argument at R3
  itself (P-069-5's own leg reused `R3_STEPS=4200` without a dedicated
  check). At θ=40.2° (this cycle's thinnest-margin, most
  crossing-proximate angle), `C40_R3`/`G40_R3` at `STEPS=6300` predicted
  to reproduce their own `STEPS=4200` values within **≤1% relative**
  (CONFIRM) / **≥5%** (REFUTE), both legs. A REFUTE here would be a
  materially important, program-wide finding: it would mean `R3_STEPS=
  4200` has been silently under-settled at `cpl=30` in every cycle that
  has used it (T10's own standing caution — finer `cpl` can shrink
  settling margin at a step count that was not independently rescaled
  for it — realized concretely, for the first time, on this exact
  channel).

**(d) Falls out of this design, reported but not gating:**
- **R14(a)-style parent-quantity check, necessarily weaker than
  exp-089's own 8-point version.** `p_abs_w(C40_R3,θ)` and
  `p_abs_w(G40_R3,θ)` are predicted to vary smoothly (no sign of a
  spurious dip) across the three sparse R3 points, consistent in
  direction with the native-`cpl` trend across the same three angles —
  disclosed explicitly as a 3-point check, far weaker than the 8-point
  native-`cpl` series R14(a) was built against, not a substitute for it.
- **Ordering check.** The rank order `frac_contrast(37.2°) >
  frac_contrast(40.2°) > frac_contrast(41.4°)`, true at `cpl=20`,
  predicted preserved at `cpl=30` — a soft, descriptive corroboration of
  (a), not a separately gating prediction.
- **Disclosure gate (not falsifiable): `FLOOR` itself remains
  unverified at `cpl=30`.** This cycle applies the existing, native-`cpl`
  `FLOOR=1.91744×10⁻⁴` against newly `cpl=30`-measured numbers for (b)'s
  classification comparison — it does **not** attempt to rebuild
  `FLOOR`/`RMS[frac_contrast]` over an R3-rescaled version of exp-083's
  full 31-point window (that would cost on the order of 124 further R3
  calls, already named and explicitly declined as out-of-scope in
  exp-089's own Idealization 12). A future cycle that needs an R3-native
  `FLOOR` must build it separately; this cycle's (b) prediction is
  scoped accordingly.

### 5. Idealizations

1. **2D TMz, single polarization, single λ=600nm** — no chromatic sweep;
   the x-wall wavelength-generality leg remains separately queued
   (fifteen-plus consecutive cycles deferred, unchanged by this cycle).
2. **Single article pair, `C40`/`G40`** — the padding-boundary-control
   construction this whole T28 sub-thread is built on; no claim about
   any other config pair (`C60`, `C70`, `C80` proper, etc.).
3. **NETD (instrument/detector threshold) is not a human-eye
   threshold.** Nothing in this cycle bears on constraint-3/4's
   human-eye verdict, and this cycle does not re-open or re-score
   `REALIZABILITY_MEMO.md`.
4. **Bench scale only** (`r_out=78` cells native / `117` cells at R3,
   same ≈2.34µm physical radius) — no witness-scale claim.
5. **`NOISE_MULT=3.0`, `FLOOR_FRAC=0.10`'s current value, `RATIO_LOW/
   HIGH=0.1/10.0`** are all inherited house-style constants, unchanged
   and unre-derived here.
6. **`FLOOR`/`RMS[frac_contrast]` are applied, not recomputed, against
   the new `cpl=30` numbers** — a disclosed mixed-resolution comparison
   (§4d's disclosure gate). This cycle discharges the resolution
   question for `frac_contrast`/`delta_scene`/`ratio_k`'s own *reported
   values*; it does not discharge whether `FLOOR` itself, as a
   threshold, is resolution-invariant.
7. **This cycle does not test constraints 1/2/3/4 and takes no T1
   escape-route position** (§3).
8. **This cycle does not attempt a full R3-rescaled rebuild of exp-083's
   31-point window**, nor does it re-run or extend R14(b)'s still-queued
   formal null-controlled period fit against the raw signed
   `p_abs(G40,θ)−p_abs(C40,θ)` difference — both remain open, separate,
   standing T28 items, untouched by this design.
9. **The three target angles were chosen for their T28-census relevance
   (crossing-proximity, caution-zone-edge-setting), not as a random or
   representative sample** of the 31-point window — inherited directly
   from exp-089's own selection rule (Idealization 11, exp-090); any
   future citation extending this cycle's resolution finding to an
   arbitrary, non-crossing-adjacent angle would be extrapolating past
   this cycle's own support, exactly as already disclosed for the
   underlying n=7 sample.
10. **The settling spot-check (§4c2) is run at one angle (40.2°) only,
    not all three** — chosen as the thinnest-margin, most
    crossing-proximate point, on the reasoning that if `R3_STEPS=4200`
    is adequate at the hardest case it is unlikely to be the binding
    constraint elsewhere in this cycle's own 3-angle set; this is a
    scope choice, not a claim that 37.2°/41.4° are separately verified
    at `STEPS=6300`.

### 6. Confirming this design does not re-open ruled-out ground

**No ruled-out idea (R1–R3) is re-proposed, and no already-superseded
framing is revived.** This cycle makes no refractive/transformation-
optics claim (R1: not engaged — no mechanism claim of any kind, §3), no
"shell = integer×λ" standing-wave claim (R2: not engaged — this channel
has never been about shell thickness), and it is a direct, literal
**execution** of R3's own meta-rule ("any surprising feature gets a
resolution check before a mechanism debate — and 'artifact' claims need
the check too"), not a violation of it: `delta_scene`'s own ~2.84–2.95°
period is already independently null-controlled as real (exp-083,
p=0.0) and is not being re-litigated here; this cycle only asks whether
its *measured value* at three specific, load-bearing angles is
resolution-stable, which R3 requires before those values keep being
cited at face value.

**This design does not violate R13's or R14's own disciplines — if
anything, it discharges the exact debt those rules' own text names.**
R13's floor gate and R14's numerator-distrust rule both presuppose that
the underlying `frac_contrast`/`frac_p_abs` readings they threshold are
themselves trustworthy measurements; neither rule's text asserts
resolution-invariance, and both R13's founding record (exp-087) and
R14's (exp-088) explicitly flagged the missing R3 check as an open gap,
not a settled one. This cycle applies the *existing* `FLOOR`/
`RATIO_HIGH`/`RATIO_LOW` thresholds unchanged (§4d's disclosure gate
states plainly that it does not attempt to re-derive them) — it adds a
resolution-robustness measurement upstream of those thresholds, exactly
the missing input R13/R14's own text already calls for, not a
relaxation, override, or re-litigation of either rule.

### 7. Explicitly out of scope, named forward (not silently dropped)

The zero-cost unbiased margin-vs-distance rebuild on the full 31-point
window (Reconciled Iteration-68 queue, Rank 2) is not folded into this
cycle — it needs no FDTD and is independent of this design's own
findings either way; it remains a candidate to run alongside or after
this cycle at the Director's discretion, not a precondition for it.
PHOTONICS' own grazing-incidence validity check (Rank 3, the single
most-repeated item on the whole T28 board) and the x-wall
wavelength-generality leg (fifteen-plus cycles deferred) are untouched.
The still-queued R14(b) formal null-controlled period fit and a
retargeted bracket at 40.2°/41.4°'s own far-side "second-ring"
neighbors (exp-089's own Next item) remain open, real, and out of this
cycle's scope.
