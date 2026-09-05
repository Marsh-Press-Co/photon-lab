# Phase 2 critique — THERMODYNAMICS (blind)

Fresh sub-agent, this seat only, Panel Iteration 92 (candidate exp-115).
Read `PANEL.md` in full; `LOGBOOK.md`'s RULED OUT registry R1–R34 line by
line, ESTABLISHED, and the LIVE THREADS bearing on this seat (T5, T22,
T23, T27, T28); `PLAN.md` lines 1–110;
`experiments/115-.../phase1_proposal.md` in full; the exp-114 record
(`phase1_proposal.md`, `run114.py`, `chunk_runner114.py`, `analyze114.py`,
`results.json`, `NOTES.md`, `phase5_redteam_audit.md` §2/§7,
`phase5_review_thermodynamics.md`, `phase5_review_materials.md`);
`experiments/113-.../chunk_runner113.py`;
`experiments/112-.../results.json`; `experiments/108-.../run.py` +
`results.json`; `experiments/110-.../run.py` +
`phase5_review_thermodynamics.md`;
`experiments/109-.../phase5_review_thermodynamics.md`;
`experiments/061-.../NOTES.md`; `lab/materials.py`; `lab/fdtd2d.py`;
`lab/caveat_lint_config.json`; `lab/validation/VALIDATION.md`;
`lab/ARTIFACTS.md`. I have seen no other seat's Phase-2 output this cycle.

Every figure below was recomputed this session from committed JSON or
committed code — never copied from any document's prose, including this
proposal's own (R4). Zero FDTD calls were made; nothing in this critique
required one.

---

## 1. Steel-man (≤150 words)

The cycle identifies, by re-derivation rather than assertion, that
exp-114's scored statistic collapses to `measured_ratio = kappa_ratio ×
G` with every cross-session term cancelling identically. I reproduce it
bit-exact: `1.5 × 2.74550565394726 = 4.11825848092089`, the filed value
to all 15 digits. That reframing is new, and it is the right one — it
converts a contested cross-session normalization dispute into a single
same-session, same-machine per-step ratio that six cheap readings can
measure directly, making M5 R33-immune *by construction* instead of by
argument. The mandatory 3-scene mix, the grid-interleaved ordering, the
upstream re-projecting budget gate, and the graceful repeat-skip
degradation are all real design work, not decoration. Item 5 genuinely
costs zero FDTD calls and zero grid-steps. And §8 flags the one
uncertainty I was sent to examine rather than papering over it — an
honest invitation, which I take up below.

*(139 words.)*

---

## 2. Sharpest attack (≤150 words)

**M9(c) uses the wrong power of the optical depth.** `τ_true` is an
*intensity* depth (`experiments/061-.../NOTES.md:36–49`: `τ = 2·(2π/cpl)
·thickness·I_graded`), so `exp(−2τ_true) = 6.71×10⁻⁸` is the returned
**power**. But every quantity M9(a) compares it against is first-order in
the returned **amplitude**: `σ_ext` is linear in `f(0)` by the optical
theorem, and `Δσ_scat` is dominated by the interference cross-term
`2·Re(f*δf)`, not `|δf|²`. The correct scale is `exp(−τ_true) =
2.59×10⁻⁴` — larger by **3861×**. All eight measured deltas then sit at
**0.02–0.59** of it, i.e. plausibly a *resolved* effect. That contradicts
(b)'s own "upper bound set by the instrument's own floor" reading rather
than being "fully consistent" with it, and (d)'s "the physical value is
predicted at `O(10⁻⁷)`" is wrong by three decades — in the sentence R21
sends into LOGBOOK as a seven-cycle debt's discharge.

*(141 words.)*

---

## 3. Verdict

**support-with-changes.**

The falsifiable heart (item 1) is worth running and the reframing is a
real contribution. Four changes are required before Phase 3; none costs
an FDTD call.

- **C1 (mandatory arithmetic, not a parameter choice).** Replace M9(c)'s
  `exp(−2τ_true)` with the first-order amplitude estimate
  `exp(−τ_true) = 2.5896×10⁻⁴`; strike "predicted at `O(10⁻⁷)`" from
  M9(d); re-gate M9(b) on a *differential* floor, since the one it uses
  is provably common-mode (Appendix §1–§3).
- **C2.** Restate M9(d)'s per-bin claim in the units it is measured in —
  `rel32` is normalized by the **peak** bin, not per-bin (Appendix §4).
- **C3.** Carry exp-061's own thermal counterweight into M9(e)'s forward
  conditional (Appendix §5).
- **C4.** Re-anchor M3/M4 and disclose the duration-attribution
  sensitivity (Appendix §6–§9).

**The single protocol change that would flip me to unqualified support:**
stop consuming the repeat pass as a ratio. The six scheduled readings
already contain, at **zero additional cost**, two same-grid/same-duration
drift readings (`d_156 = U156b/U156 − 1`, `d_234 = U234b/U234 − 1`) and
two per-grid duration points (`S`,`U`). Persist and report both
decompositions, re-anchor M3/M4's bands on the **bench's own** `d_g`
instead of on the cloud-measured `R_DEG`, and reorder the sustained pass
**ABBA** (`U156, U234, U234b, U156b`). That converts the thermal-soak
question from an unbounded idealization into a measured quantity, using
data the cycle is already paying for.

---

## 4. Appendix — derivations, re-derived figures, rule findings

### A. Figures I re-derived and CONFIRM (proposal is clean here)

All from committed sources, recomputed this session:

| Proposal claim | file:line | My recomputation | Status |
|---|---|---|---|
| `1.5 × 2.74550565394726 = 4.11825848092089` = filed `measured_ratio` | `phase1_proposal.md:97` | identical to 15 digits from `experiments/114-.../results.json` `t234_cpl25/36000 ÷ r31_control.sustained.this_session_per_step_s` | ✅ |
| `t156_session_adjusted = 3×8000×0.07121022268191168 = 1709.0453…` | `:97` | `1709.0453443658805` = filed | ✅ |
| `k = 3.2053299988171697`, `G_ref = 1.5**(k−1) = 2.4453404739580256` = `reference_ratio/1.5` | `:99` | identical both ways | ✅ |
| `G_N² = 2.25` exactly, `1 + ln(2.25)/ln(1.5) = 3.0` exactly | `:100` | `(2100/1400)² = 2.25`; `k = 3.0000000000000004` → 3.0 | ✅ |
| `R_DEG = 0.07596424755863729` | `:101` | `0.07121022268191168/0.06618270341555277 − 1` = identical | ✅ |
| `ε(2.0) = 2**(k−3) = 1.1529500…` ≡ R28's founding miss `2**k/8 − 1 = 0.152950039837078` | `:698` | identical | ✅ |
| CONFIRM window `G ∈ [2.0785394, 2.8121415]`; REFUTE `≤1.7117383` or `≥3.1789426` | `:339–340` | `G_ref×{0.85,1.15,0.70,1.30}` = identical | ✅ |
| const-ε model `G = 2.25×ε(2.0) = 2.5941376`, 6.085% from const-k | `:398`, `:402` | `2.5941375896334256`; `/2.4453404739580256 − 1 = 0.0608492` | ✅ |
| `ε_E(1.5) = 1.2202247`, 5.835% / 12.275% from the two models | `:406–408` | `2.74550565394726/2.25 = 1.2202247350876712`; deviations identical | ✅ |
| all six energy-ledger deltas, M9(a) | `:458–461` | reproduce **exactly** — but only under a **mean-of-the-two-scenes** denominator (Appendix §B1) | ✅ with caveat |
| `\|σ_ext−σ_ext_cross\|/σ_ext` = `6.6495e−06` / `2.7794e−05` | `:461` | `6.649462e−06` (r156, peccored) / `2.779367e−05` (r234) | ✅ |
| per-bin max `1.4760284822434646e−04` / `1.5265673604659632e−04` | `:457` | `max(|rel32|)` from `experiments/108-.../results.json` — identical to 17 digits | ✅ |
| deltas at `0.2×–12.6×` the floor; `σ_abs` at r=234 below it | `:465–467` | `12.572 / 6.142 / 3.229` (r156), `3.912 / 0.204 / 1.873` (r234) | ✅ |
| `τ_true = 8.258819829686677`, `α = 5.7353×10⁴ cm⁻¹`, e-fold 174.36 nm, OD 3.587 | `:107` | `1/5.7353e4 = 174.359 nm`; `8.2588/ln10 = 3.5868`; `5.7353e4 × 1.44e−4 cm = 8.2588` | ✅ |
| 1.440 µm ≡ 2.40 λ, invariant: 48×30 nm = 60×24 nm | `:108` | `R_COAT−R_CORE = 195−135 = 292−232 = 60` cells at cpl=25; `1.44/0.6 = 2.4` | ✅ |
| thickness gap 70–350×, tier UNOBTANIUM-WITH-PARAMETERS | `:107`, `:516` | `experiments/061-.../NOTES.md` MP-2 CONFIRMED, "100–500 µm … 70–350×" verbatim | ✅ |
| budget projections 2407 s / 6136 s, margins 77.7% / 43.2% | `:566–567` | `23004×(1+2.7455057)×{0.0279366, 0.0712102}` = `2407.2 / 6135.8`; margins identical | ✅ |
| caveat registry clean on the proposal as written | — | `python lab/caveat_lint.py` → **15 caveats checked, 0 required-site failures** (the proposal appears only as a T28 WARN, like every sibling document) | ✅ |

**No R4-class hand-typed figure found in the proposal's own load-bearing
chain.** §2.0's grounding discipline is real and it held under audit.
Three figures nevertheless do **not** survive contact with their sources
— §B1, §7 and §8, below — and one physics estimate is wrong (§1).

---

### 1. The `exp(−2τ_true)` estimate is the wrong-order quantity (3861×)

`experiments/061-.../NOTES.md:36–49` defines

```
tau_true = 2 * (2*pi/cpl) * thickness_cells * I_graded
```

The leading factor 2 is the standard Beer–Lambert **intensity**
convention (`I = I₀·exp(−2k₀∫Im(n)dl)`); this is confirmed by the same
block's own derived quantities, which I re-derived: `α = τ/1440 nm =
5.7353×10⁴ cm⁻¹` (an intensity absorption coefficient), e-fold 174.36 nm,
and `OD = τ/ln10 = 3.587`. So:

| quantity | value |
|---|---|
| one-pass **intensity** transmission `exp(−τ)` | `2.589644×10⁻⁴` |
| one-pass **amplitude** transmission `exp(−τ/2)` | `1.609237×10⁻²` |
| **round-trip amplitude** `exp(−τ)` | `2.589644×10⁻⁴` |
| **round-trip intensity** `exp(−2τ)` | `6.706258×10⁻⁸` ← proposal:474 |

`6.71×10⁻⁸` is arithmetically correct *as the returned power*. It is the
wrong estimator for what M9(a) measures. `σ_ext` is **linear** in the
forward scattering amplitude by the optical theorem
(`σ_ext ∝ Im f(0)`), so a core-dependent addition `δf` of relative size
`exp(−τ_true)` produces `Δσ_ext/σ_ext ~ 2.6×10⁻⁴`, not `|δf/f|²`.
`σ_scat ∝ ∫|f|²` is dominated by the cross term `2·Re(f*δf)`, again
first-order. The `|δf|²` term the proposal quotes is subdominant by
exactly `exp(τ_true) = 3861.5×`.

**Corroboration from this program's own record, not from theory alone.**
exp-028 (Iteration 5) measured that the hollow core absorbs `0.0062%` =
`6.2×10⁻⁵` of total incident power — an *independent, measured*
core-illumination fraction of order `10⁻⁴`, four times below the
centre-line `exp(−τ_true) = 2.6×10⁻⁴` exactly as chord-averaging over a
disk predicts (near-tangent chords are longer). Nothing in the record
supports a `10⁻⁷`-scale core coupling.

**Where the eight measured deltas actually sit** (recomputed, §A):

| channel | value | `/exp(−τ)` | `/exp(−2τ)` |
|---|---|---|---|
| r156 σ_scat | 8.3594e−05 | 0.323 | **1247×** |
| r156 σ_abs | 4.0843e−05 | 0.158 | **609×** |
| r156 σ_ext | 2.1469e−05 | 0.083 | **320×** |
| r234 σ_scat | 1.0874e−04 | 0.420 | **1621×** |
| r234 σ_abs | 5.6662e−06 | 0.022 | **85×** |
| r234 σ_ext | 5.2044e−05 | 0.201 | **776×** |
| r156 per-bin max | 1.4760e−04 | 0.570 | **2201×** |
| r312 per-bin max | 1.5266e−04 | 0.590 | **2276×** |

Every one lands between 2% and 59% of the first-order estimate — the
signature of a *real* effect with an `O(0.1–1)` coupling factor. Under
the proposal's own `6.71×10⁻⁸`, all eight would have to be 85–2276×
above the physics, i.e. pure instrument floor.

### 2. …which makes (b) and (c) mutually contradictory, not "fully consistent"

`phase1_proposal.md:476` asserts (c) is "fully consistent with (b)'s
reading that the measurement is floor-limited." It is the opposite. (b)
reports the deltas at `0.2×–12.6×` the channel floor — i.e. **five of six
are ABOVE the floor** — while (c) says the physics is 320–2276× *below*
the deltas. Those two statements cannot both be right: either the deltas
are floor, in which case (b)'s own margins are meaningless, or they are
partly signal, in which case (c) understates the physics. Under the
corrected `exp(−τ_true)` the two sections become genuinely consistent for
the first time. This is an **R9** finding in its purest founding form: an
arithmetic that reproduces (it does — I checked) compared against an
operand in incommensurable units (energy vs. amplitude).

### 3. The floor M9(b) gates on is *exactly* common-mode and cancels in the difference

R13 requires a floor gate before a small ratio is cited. The proposal
applies one — but the floor it chooses,
`|σ_ext − σ_ext_cross|/σ_ext`, is a property of a **single scene**, and
the quantity being gated is a **difference between two scenes**. I
computed the optical-theorem residual per scene:

```
r=156:  peccored  σ_ext−σ_ext_cross = −4.65534379e−03
        hollow    σ_ext−σ_ext_cross = −4.65534379e−03
        difference between scenes   = −2.27e−13   (3.2e−16 of σ_ext)
r=234:  peccored  = hollow = −3.03914978e−02
        difference between scenes   =  0.0        (exactly zero)
```

The residual is identical to machine precision (bit-identical at r=234).
It therefore contributes **exactly nothing** to the peccored−hollow
difference: as a floor for that difference it overstates by ~10⁵ at
r=156 and is undefined-by-zero at r=234. Gating a differential quantity
on a common-mode systematic satisfies R13's letter and inverts its
substance — and it biases in the direction that makes the sidecar's
headline look *safer* ("floor-limited, upper bound only") than the data
supports.

**The correct differential floor is `box_dev` on this channel** — which
this cycle does not compute at r=234, and which my own exp-114 Phase-5
review (`phase5_review_thermodynamics.md` §3) already named as the one
honest gap in exactly this reading, estimating the r=234 margin between
9× and 24× from the established `1221× → 23.8× (r=156) → 9.0× (r=312)`
trend. That gap was non-load-bearing at exp-114. **M9(d) makes it
load-bearing**, and the proposal does not carry it forward. Minimum
discharge: either compute `box_dev` at r=234, or state M9(b)'s floor
explicitly as "single-scene optical-theorem self-consistency, which
cancels in the differential and is therefore not a differential floor —
no differential floor exists at r=234."

### 4. M9(d)'s "per-bin … at better than 1.6×10⁻⁴ relative" is peak-normalized

`experiments/108-.../run.py:234–242`:

```python
max_peccored32 = float(np.max(np.abs(peccored32))) ...
rel32 = np.abs(delta32) / max_peccored32
```

The denominator is the **maximum over the 48 bins**, not the bin's own
value. For a forward-peaked 2D pattern that is much larger than a typical
bin: I recomputed `median(rel32) = 8.456×10⁻⁷` at r=156 against
`max = 1.476×10⁻⁴` — a 175× spread, i.e. the array is dominated by a few
bins and its normalization is a single global scalar.

M9(d) then writes "per-bin angular pattern … insensitive to the
core/backing material at **better than 1.6×10⁻⁴ relative**." A
fabrication reader takes "relative" to mean relative to that bin. It
means relative to the pattern's peak. The per-bin-relative sensitivity at
a non-peak bin is not bounded by this figure at all — and cannot be
recovered from the record, because `experiments/108-.../results.json`
persists `rel32` but **not** `peccored32` (verified: the only 48-element
arrays under `item_i` are `rel32` and `bin_centers_deg`). This is a
second R9 operand-commensurability defect in the same claim, and an
R16-adjacent one: the denominator needed to make the claim checkable was
never persisted.

The proposal's §2.0:104 already issues one R4 self-correction on this
exact array (`ITEM_I_CONFIRM_REL = 0.05` is a decision bar, not a
measurement). Good catch — but it stops one level short of the
normalization.

### 5. M9(e)'s forward conditional drops this seat's own already-filed counterweight

`phase1_proposal.md:524–529` recommends, conditionally, re-speccing the
article at exp-061's MP-5-plausible thickness (230–730× of 1.44 µm) and
states only the optical consequence: core/backing freedom "survives and
strengthens."

`experiments/061-.../NOTES.md:235–248` — this program's own THERMO
disposition, at **exactly that multiple**:

| MP-5 multiple | `l_geometric_m` | `ΔT_ss` (K) | margin vs NETD-lo (0.020 K) |
|---|---|---|---|
| 230× | 331.2 µm | 5.277×10⁻³ | **3.79×** |
| 730× | 1051.2 µm | 1.4774×10⁻² | **1.35×** |

Still UNDETECTABLE at every point — but the record's own words are "far
more fragile than the superseded 150 µm/8.1× figure suggested," and a
"~35% adjustment to any one free assumption … would move this cell into
MARGINAL."

The mechanism is not incidental to the recommendation, it *is* the
recommendation: `ΔT_ss = I·ratio/(4εσT³ + h)` with `h_eff = k_air/L`
(T22/T23), so growing `L` by the same 230–730× drives `h_eff` down by
that factor and pushes `ΔT_ss` toward the radiation-only ceiling. I
verified the scaling in the filed table itself: a 3.17× length increase
(331→1051 µm) raises `ΔT_ss` 2.80×, the near-linear behaviour an
`h`-dominated regime predicts. **The optical benefit M9(e) advertises and
the thermal cost it omits are the same physical change.** Naming only
the benefit, in the paragraph R21 sends to LOGBOOK, is the omission this
seat exists to prevent.

`lab/caveat_lint_config.json:121–144`
(`exp061-thermo-length-scale-staleness`) exists precisely to attach that
counterweight to citations of this disposition. It does **not** fire on
the proposal's wording (verified live: 0 required-site failures) —
its `trigger_terms` are `l_geometric_m` / `THERMO disposition` /
`150.{0,3}(u|µ)m`, none present, and the `230.{0,5}730.{0,10}multiple`
phrase pattern does not match "230–730× of 1.44 µm". So this is a
registry **coverage** observation, not a live lint defect — the same
shape the entry's own description records being widened once already at
Iteration 39. The honest remedy is to add the caveat voluntarily in
Phase 3, not to widen the registry mid-cycle to force it.

### 6. The assigned question — answered from data, not asserted: the soak has the WRONG SIGN in the only within-run measurement on file

§8:736–744 asks whether "a multi-hour thermal soak makes a minutes-long
burst structurally unable to represent" a production run. The record
already contains the discriminating measurement, and nobody has read it.

From `experiments/114-.../results.json` and
`phase5_redteam_audit.md:246–250` (both committed), for the **same**
r=234 empty scene, **same** 12000-step run:

```
first 3000 steps  (204.2541 + 196.8292 + 214.2101) / 3000 = 0.2050978 s/step
full 12000 steps  2355.936572790146 / 12000             = 0.1963280 s/step
last 9000 steps   (2355.9366 − 615.2934) / 9000         = 0.1934048 s/step

first 3000 is 6.046% SLOWER per step than the last 9000
             4.467% slower than the 12000-step mean
```

**Per-step cost fell as the run went on.** A thermal/turbo soak predicts
the opposite sign. Meanwhile the same session's controls
(`chunk_runner114.py:184–191`, short then sustained, back-to-back) give
`R_DEG = +7.596%` — the longer, later reading *slower*. The two on-file
duration signals from the same session have **opposite signs**, so they
cannot both be "sustained-load degradation," and neither is identified:
`run_control()` runs short-before-sustained with no counterbalance, so
`R_DEG` conflates duration with elapsed position by construction.

The one attribution consistent with both signs is the one Idealization 11
already names and then declines to act on: **multi-tenant contention on
that cloud sandbox**, varying over the session (exp-114's own Phase-2/5
records document 6–30 concurrent suite invocations at `/proc/loadavg`
25–30 on a 4-core box). Within-session excursions of ±6% are comparable
to `R_DEG` itself and larger than M7's entire `±5%` N2_HOLDS band.

**Consequences, all load-bearing:**

- **`R_DEG` is not a duration anchor.** M3's bands (`R_DEG/2`, `R_DEG`)
  and M4's NOISY bar are anchored on a cross-machine net figure whose
  dominant mechanism is a contention field that does not exist on a
  single-tenant bench. R17 requires an anchor drawn from "a comparable
  transition"; cross-machine, cross-mechanism is not comparable — and the
  cycle's own M6 exists to test whether cross-machine transfer holds.
  **M3/M4's bands assume the answer to the question M6 asks.**
- **M3's pre-registered labels assert an unvalidated direction.**
  CANCELS / PARTIAL / **DOES-NOT-CANCEL — "degradation is
  grid-dependent"** attaches a mechanism name to a statistic whose
  mechanism has the wrong sign in the only within-run data on file. §8's
  rules re-read (`:727`) declares R30/R32 "N/A … no asserted diagnostic
  tail." M3 asserts one. Not a fatal R32 firing — `d_dur` is an absolute
  deviation, not a tail — but the *interpretive label* is exactly what
  R32 governs, and it should read mechanism-neutrally ("`G` is / is not
  duration-invariant") unless the direction is validated on the bench.
- **The bench should show the opposite sign**, and I put that on record
  as this seat's falsifiable expectation, pre-run: on a single-tenant
  box, with the contention term removed, per-step rate should *fall*
  with reading duration, so the bench's `d_dur` analogue should come out
  **negative**, plausibly of order −4% to −6% by the r=234 within-run
  datum. If the bench reproduces `R_DEG > 0`, that is genuine evidence
  for a real thermal/turbo effect and this analysis is wrong. Either
  outcome is informative; neither is currently measurable as designed.

### 7. A third correction axis, wider than the v2 straddle, that this cycle can close for free

Model the measured per-step rate on grid `g` over `n` steps as
`p_g + C_g/n` (`C_g` = per-scene warm-up: first-touch page faults over a
112 MB / 251 MB working set, allocator warm-up, frequency ramp). Fitting
the r=234 empty scene's own two levels above gives
`C_234 = (0.2050978 − 0.1934048) × 3000 = 35.08 s/scene`.

Apply a **grid-independent** `C` of that magnitude to exp-114's 3334-step
r=156 control denominator only, and rescore with the unmodified
classifier bands:

| assumed `C` (s/scene) | corrected `p_156` | `G_E` | `measured_ratio` | `rel_dev` | verdict |
|---|---|---|---|---|---|
| 0 (as filed) | 0.0712102 | 2.7455 | 4.1183 | **0.1227** | CONFIRM |
| 17.54 | 0.0659486 | 2.9645 | 4.4468 | **0.2123** | AMBIGUOUS |
| 35.08 | 0.0606886 | 3.2215 | 4.8322 | **0.3174** | REFUTE |

Under the other extreme (`C ∝ memory footprint`, i.e. `C_156 = C_234/2.25`),
the correction cancels between numerator and denominator and `G_E` is
unchanged.

**So the duration/warm-up-attribution axis alone spans CONFIRM → REFUTE
on the already-filed verdict** — strictly wider than the v2 straddle Red
Team ruled "not a corroboration" (which spanned `+0.1227` to `−0.1229`,
both CONFIRM). This is a **third**, previously unnamed correction axis
sitting underneath EM's, QUANTUM's and PHOTONICS' three.

I state it as a **bounding sensitivity, not a correction** (R7/R10: an
unfitted two-parameter model may not license a verdict). Two honest
qualifiers: (i) the r=156 control's own two-point fit gives
`C_156 = −7.18 s` — negative, i.e. the contention term dominated the
warm-up term on that grid in that session, so neither extreme is the
truth; (ii) the three chunk times are non-monotone (204.25 / 196.83 /
214.21), so within the first 3000 steps there is no clean decay.

**And the cycle can measure `C_g` directly, for free.** `S` (1000 steps)
and `U` (3334 steps) on the same grid are two points on `p_g + C_g/n`:
two equations, two unknowns, per grid. Fit them, report the asymptotic
`G_∞ = p_234/p_156` alongside the raw `G`, and this axis closes with real
data instead of two competing assumptions — the same argument the
proposal itself makes for item 1, applied one level down. The alternative
(equally cheap) is to discard the first ~1000 steps from each timed
window: `sim.run(1000)` untimed, then `sim.run(2334)` timed, which
removes `C_g` from both grids by construction and makes the control
genuinely protocol-matched to a 12000-step production numerator.

### 8. The ordering is not counterbalanced — every r=234 reading follows its r=156 partner

`:159–164` claims the 1→2→3→4→5→6 interleave prevents the r=234 readings
sitting "later under more accumulated thermal/turbo load." It does not.
The order is `S156, S234, U156, U234, U156b, U234b`: **A always precedes
B in every pair.** Adjacency is achieved; counterbalancing is not. Under
any monotone drift `p_g(t) ≈ p_g0(1+δt)`, `G = p_234(t₂)/p_156(t₁)` is
biased by `(1 + δ·Δt)` with `Δt` = the full duration of the r=156 reading
— and `Δt` is large: at exp-114's anchor `U156` alone is
`10002 × 0.0712 = 712 s`, so the midpoint separation of the sustained
pair is `(712 + 1955)/2 = 1334 s`. It is also asymmetric by cost: the
r=234 readings consume ~73% of the session's wall time despite equal
grid-steps (23,004 each), so every r=234 reading sits systematically
deeper in whatever the session's drift field is.

The fix is free and standard: **ABBA** — `U156, U234, U234b, U156b` —
which cancels a linear drift to first order. The short pass can stay
`S156, S234` since it feeds only the budget gate.

Second, free, and higher-value: the repeat pass is currently consumed
**only** as `d_rep = |G_rep − G|/G` (`:305`), a ratio in which any
common-mode drift cancels — so M4 is structurally blind to exactly the
drift that biases M2. `U156b/U156` and `U234b/U234` are same-grid,
same-duration, later-in-session: the only clean measurement of session
drift this cycle can produce, and it is currently discarded. Persist
`d_156`, `d_234` and re-anchor M3/M4 on them.

### 9. Two inherited figures that do not survive their sources (R4)

**(a) "peccored steps are ~14% costlier" (`:148`).** This is offered as
the reason the 3-scene mix is "mandatory, not stylistic." exp-114's own
per-scene production wall times (`results.json.total_wall_s_by_scene`,
12000 steps each, r=234/cpl=25) are the only profiled per-scene
measurement in the record:

```
empty     2355.936573 s  → 0.1963280 s/step
hollow    2326.205099 s  → 0.1938504 s/step
peccored  2356.148812 s  → 0.1963457 s/step

peccored vs empty:  +0.0090%      peccored vs hollow: +1.287%
```

**~1.3%, not ~14%** — a 10× overstatement. Red Team's own exp-114 audit
(`phase5_redteam_audit.md:296–316`) already flagged the 14% figure as an
*estimate*, "explicitly not a profiled measurement"; the profiled
measurement now exists and contradicts it. The 3-scene requirement itself
is still right (commensurability, R9) and I do not ask for it to be
dropped — only that its cited magnitude be corrected to the measured one.
The scene-mix insensitivity is itself informative: it means per-step cost
in this engine is essentially content-independent at production scale
(a PEC-filled scene and an empty scene cost the same to 9×10⁻⁵), which
is what makes §7's warm-up/streaming account the leading one and rules
out a field-content (denormal) mechanism.

**(b) Idealization 4's "≲5%" bound (`:625–634`).** The bound is asserted
from three chunk times whose own `max/min = 214.2101/196.8292 = 1.0883`
— an **8.83%** spread, not ≲5%. More seriously, chunk-to-chunk scatter is
the wrong statistic for the mismatch it claims to bound: the real,
measured level shift within that same run is 5.70% between the first 3000
and last 9000 steps (§6), a quantity chunk scatter cannot see at all.
Idealization 4 does not bound the effect it is written to bound.

### 10. Does this proposal inherit my seat's two prior findings? Yes — both

**(i) Wall-time attribution** (my exp-110 Phase-5 §2 Fix-6 finding; my
exp-109 Phase-5 §4 "no committed artifact" finding). `:630–634` states
plainly that the three chunk times "survive only as quotations inside
`phase5_redteam_audit.md` §2; the scratch wall-time log … did not survive
that session … cited, not independently re-derivable." That is the same
defect one cycle downstream — and this cycle then builds Idealization 4's
load-bearing bound on those un-re-derivable numbers. The proposal's own
§6 bench figures ("41/41 in 87 s, cloak stage 124 s") likewise have no
committed artifact and no numpy version named, which
`lab/validation/VALIDATION.md`'s own docket-14 rule ("a 1400-step FDTD
bit-reproducibility claim that does not name its platform is not a gate")
already anticipates. **Prospective fix, cheap:** persist every reading's
**raw per-scene wall time** (not only the blended per-step rate) into
`results.json`, plus a machine-state block — `lscpu` L3, THP setting,
`OMP_NUM_THREADS`/BLAS thread count, `loadavg` before/after each reading,
and per-reading start/end timestamps. Idealization 3 declares `G` "a
machine property"; a machine property recorded without the machine's
state is not reproducible, and Iteration 93 will otherwise be quoting
this cycle the way this cycle quotes exp-114.

**(ii) The explicit AND-reduction** (my exp-109 Phase-5 §1 Fix-4
finding). The proposal correctly invokes R24 for its composition rules
(`:313–320`), but does not reduce them. Two gaps: (a) M4's MARGINAL band
is `0.02 < d_rep < 0.0759642` while M3's UNINTERPRETABLE trigger sits at
`0.0379821` — **inside** it, so `M4 = MARGINAL` is consistent with M3
being either scored or unscored, and no single field states which; (b)
the `repeat_skipped` branch says M3 is "reported with an explicit … caveat
rather than a clean verdict," which is not a classification. **Fix, in
the exp-109 idiom:** one literal boolean in code,
`m3_scored = (not repeat_skipped) and (d_rep <= R_DEG/2)`, persisted, with
`m3_verdict = "UNINTERPRETABLE"` whenever it is `False`, and an assert
that the two agree — not left to a reader's inference.

### 11. Charter items: the energy ledger, the metrics table, and DISCLAIMER_115

My exp-114 Phase-2 attack was that real absorbed-power data would be
computed in memory by `sc.widths()` and silently discarded. **I do not
repeat that ask here, and the reason is a physics reason, not a
concession.** `geom_fixedabs_cpl` sets `STEPS = round(STEPS0·κ·ratio)`
(`experiments/112-.../run112.py:114`) — 8000 at r=156, 12000 at r=234 —
sized so each grid gets ~2 domain crossings at `S = courant_frac/√2 =
0.32/√2 = 0.2263` cells/step (`lab/fdtd2d.py:78`;
`experiments/110-.../run.py:58`). The control bursts run **1000 and 3334
steps**, i.e. 8.3%–41.7% of production; the wavefront reaches only
`160 + 0.2263n` / `240 + 0.2263n` cells, so at 3334 steps the r=156 grid
is ~65% filled and the r=234 grid only ~47%. A `σ_abs`/`σ_ext` ledger
from fields that far from settled would be a **wrong number, not a free
byproduct** — T27 is this program's own paid-for lesson that a truncated
run is not a small perturbation of a settled one.

**But that reason appears nowhere in the proposal.** §7's eleven
idealizations contain no energy-ledger or thermal-sidecar line, and
PANEL.md's metrics table carries an "Absorbed energy budget + predicted
re-radiation | ledger | Joule accounting + THERMO sidecar" row that
exp-114 filled and exp-115 will not. Silently dropping a row the
immediately preceding cycle filled — via a ratified mandatory fix bearing
this seat's name — is the R16/R21 shape. **Requested fix, one sentence,
zero cost:** DISCLAIMER_115 carries an explicit energy-ledger/thermal-
sidecar N/A sentence with the settling reason above, with **both** the
predictions-side and result-side asserts in committed, re-invocable call
sites (R23 First Addendum, which the proposal correctly commits to at
`:719–721` for the string as a whole). That also closes, for the first
time, one of the three disclaimers R23's own founding cycle (exp-104)
named as uncovered — "the THERMODYNAMICS thermal-sidecar-N/A sentence"
(LOGBOOK.md:960–965) — a completeness gap open since Iteration 81.

A related instrument-thermodynamics correction to `:227`: the sidecar
"can be computed before, during, or after the bursts without perturbing a
single timing measurement" is **false for "during."** Both grids' working
sets (~112 MB and ~251 MB at 7 float64 planes + a bool over 1400²/2100²
cells, `lab/fdtd2d.py:85–98`) exceed the W-2145's 11 MB L3 by 10× and
23×, so this is a DRAM-bandwidth-bound streaming stencil; any concurrent
process competes for the resource that *is* the measurement. Zero FDTD
cost ≠ zero perturbation. The bursts need a stated exclusive-use
protocol — no concurrent trust-suite run, no other seat's SSH session, no
`analyze115.py` — which is enforceable on a team-owned bench even though
it was not on the cloud sandbox. Idealization 11 declares the bench
"multi-tenant to an unknown degree"; on this machine that is *knowable*
and *controllable*, and declaring it unknown is an unforced idealization
on the cycle's own primary axis.

**One pre-run expectation, from the same memory analysis, offered as a
hypothesis and not a claim** (M7 is the metric it bears on): with both
working sets far past L3 and transparent huge pages covering 251 MB in
~126 pages, there is no cache- or TLB-hierarchy mechanism that would
produce a per-step superlinearity between these two sizes — byte traffic
scales as `N²`, so `G ≈ 2.25` (N2_HOLDS) is the mechanistically expected
outcome, and exp-114's 22% excess is more plausibly protocol (§6–§7)
than machine. Checkable on the bench for free (`lscpu`,
`/sys/kernel/mm/transparent_hugepage/enabled`, thread count) and worth
recording alongside the readings whichever way M7 lands.

### 12. Rule-compliance findings, consolidated

| Rule | Finding |
|---|---|
| **R4** | Two inherited figures fail to reproduce from source: "~14% costlier peccored" (measured 1.3%, §9a) and Idealization 4's "≲5%" from a `max/min = 1.088` spread (§9b). Neither is currently verdict-bearing; both would enter frozen prose. Tally is 2 — below R20's three-in-one-document bar, but both are pre-freeze and correctable now. |
| **R9** | Three operand-commensurability defects, all in M9: energy vs. amplitude (§1); common-mode floor vs. differential quantity (§3); peak-normalized vs. per-bin (§4). |
| **R13** | M9(b) claims R13 compliance with a floor that is provably zero for the gated quantity (§3). Letter satisfied, substance inverted. R13 does not *fire* — its trigger is a zero-crossing-capable denominator — but its discipline is not met. |
| **R16 / R21** | The energy-ledger/metrics-table row is dropped without disclosure (§11); M9(e)'s counterweight is omitted from the prose R21 sends to LOGBOOK (§5). |
| **R17** | M3/M4's bands are anchored on `R_DEG`, a cross-machine figure whose dominant mechanism (cloud contention) is absent on the bench, and whose transferability is what M6 exists to test — circular (§6). |
| **R23 First Addendum** | Correctly committed to at `:719–721`. Recommend widening DISCLAIMER_115 to carry the thermal-sidecar-N/A sentence, closing exp-104's own named completeness gap (§11). |
| **R24** | The M3/M4/M6 composition rules are stated but not reduced to a single coded boolean; M4's MARGINAL band straddles M3's UNINTERPRETABLE trigger (§10ii). |
| **R25** | §3's declined items are properly numbered queue lines, not parentheticals. **Compliant.** |
| **R27 / R28** | §6's gate is executable and traced upstream of each `Sim.run()`. **Compliant.** One residual: the gate can only skip the *repeat*; if the bench proves ≳2× slower than exp-114's session the first re-projection raises after a single reading, with no reduced-scope fallback. A `SUSTAINED_CONTROL_STEPS` step-down branch would make the degradation graceful at both ends. |
| **R29** | `run115.py`/`chunk_runner115.py` with executed identity asserts — **compliant as specified**. |
| **R31 / R33** | M5 is genuinely R33-immune by construction (verified: no scored operand mixes sessions). M6 is disclosed as cross-machine, correctly. §7 opens a new axis *inside* R33's own founding instance that R33's text does not yet cover — duration/warm-up attribution within a single session. Not a rule violation; a candidate widening for Phase 5 to consider, not for this Phase-2 to ratify. |
| **R32** | Not fired. But M3's interpretive labels name a mechanism ("degradation is grid-dependent") whose direction is unvalidated and contradicted in sign by on-file data (§6); §8:727's "no asserted diagnostic tail" is true of the statistic and not of its labels. Recommend mechanism-neutral wording. |
| **R34 / checkpoints** | Nothing here fires criterion 4. No unfalsifiable claim; constraint 3 is not quietly dropped. |

### 13. Constraint-3 and metrics-table exposure

**T1 route NONE / N/A is correct and I independently confirm it** for
item 1: a per-step rate, a grid size and a cost bound cannot express
`σ(I)`, `σ(x,t)`, angular selectivity or sub-threshold operation, and no
constraint-1/2/3/4 metric is computed anywhere in the cycle.

Two exposures worth naming, neither a violation as written:

1. **M9(d) is a positively-framed claim about the flagship absorber**
   ("a real process … does not need to control the substrate or core
   material at all") that a future citation could read as progress. §4
   and M9(e)'s second bullet guard it explicitly and adequately. Keep
   both sentences in the Result prose verbatim, not only in the proposal.
2. **M9(e)'s first bullet points at a configuration that is worse on my
   own ledger.** Thickening 230–730× improves the optical
   backing-independence and simultaneously drives the IR detectability
   margin to 1.35×–3.79× (§5) while making the object a physically larger
   black silhouette — constraint 3's own failure mode, which the
   ESTABLISHED section already records this article failing by
   construction. Presenting it as a pure gain is the quiet drift risk
   here. C3 removes it.

**Metrics table:** six of seven rows are legitimately N/A by this cycle's
scope and precedent. The seventh — the ledger row — needs the explicit
N/A sentence of §11 rather than silence.

---

## Trust suite

Not re-run by me this session: this critique made **zero** FDTD calls and
touched no `lab/` code path whose correctness a suite run would bear on.
`git diff --stat -- lab/` is empty; every figure above came from
committed JSON, committed source, or pure arithmetic. I did execute one
committed `lab/` tool, `python lab/caveat_lint.py`, which reports **15
caveats checked, 0 required-site failures** with the candidate proposal
in the tree (§A). I note, without asserting it, that the proposal's own
bench figure ("41/41 in 87 s") has no committed artifact and names no
numpy version — see §10(i); the Director should confirm it independently
before Phase 3, per this program's own docket-14 platform rule.
