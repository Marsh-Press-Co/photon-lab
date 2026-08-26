# PHASE 1 — PROPOSE · Panel Iteration 51 · exp-074
## ELECTROMAGNETISM's window pricing: Cramér–Rao/conditioning + `L(T)` leakage, code-committed (T28)

*Fresh sub-agent, ELECTROMAGNETISM charter (PANEL.md seat: field/wave
behavior, impedance matching, energy coupling; owns reciprocity/passivity/
causality bookkeeping), lead by rotation. Executes Iteration-51 queue item
1, near-unanimous #1 across all six of exp-073's Phase-5 seats
(`phase5_redteam_audit.md` §6.2), with queue item 5's decision-rule
requirement folded in as §6 below.*

---

## 0. What this is, and what it is not

This turns two **informal, hand-computed, uncommitted** Phase-5 numbers —
my own predecessor's `cond(X9)=529` / `36.6×` VIF (`exp-072/
phase5_review_em.md` §6.2) and QUANTUM's `L(T)` leakage table (`exp-072/
phase5_review_quantum.md` §3, one representative pair) — into real,
committed, reproducible code (`desk_check_pricing.py`, this directory),
run against the **real fitted carriers of all four `ABSORB` pairs**, not
one. It is a **desk-check pre-registration verification**, exp-069's own
`desk_check_settling_delta.py` precedent: the code is committed and its
output disclosed *before* this proposal's numbers are cited, exactly so no
figure below is hand-typed (LOGBOOK R4). `CHECK 0` in the script
independently re-derives every reused formula against exp-072's own
committed `results.json` (`T_mean_deg`, `T_x`, `amplitude`, `cond5`) and
passes at machine precision (`worst_rel_err=0.00e+00`) before anything
else runs — this pricing is anchored to the record's own established
basis, not a plausible-looking reconstruction.

**Disclosure, matching this program's own contamination-disclosure
convention (exp-072/073):** because this is a deterministic instrument-
pricing calculation on already-published data (no null-hypothesis
p-fishing, no threshold tuned after seeing an outcome), the "numbers seen
before pre-registration" concern that gated exp-072/073 does not apply the
same way — the whole point of this cycle is to compute `cond`/VIF/`L(T)`
on real data. The bands in §5 are stated as falsifiable thresholds a
future re-run of the identical, unmodified script must reproduce; they are
not tuned to make the observed numbers look a particular way — every
threshold below is argued from Iteration 49/50's own already-published
figures (the `2σ` detectability bar EM stated in exp-072 §6.2; the
`cond≤100`/`(n−p)/n` machinery already standing in `run.py`), not invented
for this cycle.

---

## 1. Narrative (≤300 words)

Five T28 cycles (Iterations 46–50) have repeatedly *asserted*
non-identifiability against T21's 1.9608° fringe without ever pricing it
as a design question independent of any one null construction. Two
informal Phase-5 numbers said the price was already known — a 9-column
two-tone design with `cond≈529` and `~6×` SE inflation on `R_q` — but
neither was committed to code, verified across all four pairs, or
connected to exp-073's own independently-established leverage mechanism
(`mean diag(M5)=(n−p)/n`, the exact driver of `G0-e(ii)`'s anti-
conservative sign-flip null). This proposal computes both, in one script,
on real data, and adds the piece neither predecessor had: how the same
quantities move at a **widened** window, so the panel can answer not
"is the current null miscalibrated" (exp-073 already answered that) but
"can *any* correctly-calibrated null ever work here, and if not here, at
what width would it."

The answer, computed below: at 36°–42° the two-tone design's information
content is decisively too poor — `cond9∈[478,529]`, `SE`-inflation
`5.6–6.1×`, optimistic joint-fit significance `z_joint≤0.81` at every
pair, well short of 2σ — independent of which null eventually gates it.
Widening to ~46° (1.05 Rayleigh widths) leaves the case genuinely
marginal. Widening to ~51° (1.5 Rayleigh widths) changes the arithmetic
qualitatively: `SE`-inflation drops to `~1.2×`, optimistic `z_joint`
clears 2σ at 3–4 of 4 pairs, and the leverage-weighted ratio driving
`G0-e(ii)`'s anti-conservatism improves from `0.80` to `0.91` — still not
exactly calibrated, but a different regime. This is a real, citable,
zero-cost boundary: the differential/two-tone route is closed *in this
window*, not closed *at any window*. *(≈290 words)*

---

## 2. Parameter table

### 2a. Data and reused machinery (zero new FDTD, zero `lab/` diff)

| Item | Source |
|---|---|
| `C40(θ)`, `C80(θ)` | `experiments/069-.../results.json` → `block_dense.rows`, 31 pts, 36.0–42.0°, 0.2° step |
| `C60(θ)`, `C70(θ)` | `experiments/071-.../results.json` → `dense_causal.rows.{C60,C70}`, identical grid (checked, `g0a_grid_identical`) |
| `_fixed_period_fit`/`_free_period_search` | `experiments/069-.../run.py`, imported verbatim |
| `_amp_phase_at`/`carrier_fit`/`design_matrix` | re-implemented byte-identically to exp-072/073's `run.py` (import collision on the module name `run` prevents a direct import — see script docstring); **CHECK 0 verifies exact agreement** against exp-072's committed `results.json` |
| `CENTER_DEG` | 39.0° (unchanged) |
| `N_GRID_CARRIER` | 3000 (unchanged, exp-072 Idealization 6) |

### 2b. Real fitted carriers, all four pairs (`desk_check_pricing.py` output, this run)

| Pair | `T_mean` (deg) | `cond(X5)` | `\|R_q\|/SE_ols` |
|---|---|---|---|
| C40–C60 | 2.4865 | 60.0 | 4.90 |
| C60–C70 | 2.5285 | 60.8 | 3.04 |
| C70–C80 | 2.5325 | 61.0 | 4.25 |
| C40–C80 | 2.4905 | 59.9 | 4.66 |

(`cond(X5)≈60` and the four `z_ols` values reproduce EM's exp-072 §6.2
figures exactly — `cond≈60`, `4.9/3.0/4.3/4.7` — confirming those informal
numbers, not merely repeating them.)

### 2c. Second tone (the contaminant) — item (a)

Second tone fixed at **`T=1.9608°`**, T21's own established `x=sinθ`
period (disclosure-only in exp-072/073, promoted here to a modelled
column) — its own phase `ψ̄₂` is **fit from the real common-mode `Cbar`**
at that period (`_amp_phase_at`, same idiom as `at_carrier()`'s fringe
leg), never hand-set. 9-column design `X9 = [1, cosθ_c1, −sinθ_c1,
u·cosθ_c1, −u·sinθ_c1, cosθ_c2, −sinθ_c2, u·cosθ_c2, −u·sinθ_c2]`. `R_q`
stays column index 4. `VIF_Rq = [(X9ᵀX9)⁻¹]₄₄ / [(X5ᵀX5)⁻¹]₄₄`.

| Pair | `cond(X9)` | `VIF_Rq` | `SE`-inflation | `z_joint` (optimistic*) |
|---|---|---|---|---|
| C40–C60 | 529.4 | 36.6 | 6.05 | 0.81 |
| C60–C70 | 482.4 | 31.6 | 5.63 | 0.54 |
| C70–C80 | 478.4 | 31.1 | 5.58 | 0.76 |
| C40–C80 | 524.5 | 36.1 | 6.01 | 0.78 |

*`z_joint = z_ols / SE-inflation`: an **optimistic upper bound** — it
assumes the joint fit's noise and true effect are exactly what the
single-carrier fit observed, which the two-tone fit cannot do better than
even in principle (idealization, §5).

**Reproduces EM's exp-072 §6.2 figures exactly** (`cond=529.4` at
C40–C60 vs the quoted `529`; `VIF=36.6` vs the quoted `36.6×`;
`SE`-inflation `6.05` vs the quoted `6.0×`) — the informal calculation was
right, at least at the one pair it checked. It was wrong only in scope:
three of four pairs were never priced, and the number was never connected
to `mean diag(M5)`.

### 2d. Leverage-concentration pattern — item (c)

House convention (exp-073): `M5 ≡ I − H5` (the sign-flip null's own
residual-maker), so `diag(M5) = 1−h_ii` and `mean(diag(M5))=(n−p)/n`
exactly (`trace(H5)=p`, an algebraic identity, independent of *where* the
θ points sit — confirmed at every window width below to the last digit).
What is **not** algebraic is where the ordinary hat-matrix leverage `h_ii`
concentrates, and the leverage-weighted ratio that drives `G0-e(ii)`'s own
`~0.79` anti-conservative figure:

`lev_ratio = Σᵢ row5ᵢ²·(1−h_ii) / Σᵢ row5ᵢ²`, `row5 = pinv(X5)[4,:]`

| Pair | `mean diag(M5)` | edge `h_ii` / center `h_ii` | `lev_ratio` |
|---|---|---|---|
| C40–C60 | 0.8387 | 0.2272 / 0.1384 | 0.8002 |
| C60–C70 | 0.8387 | 0.2277 / 0.1382 | 0.7992 |
| C70–C80 | 0.8387 | 0.2278 / 0.1382 | 0.7989 |
| C40–C80 | 0.8387 | 0.2272 / 0.1384 | 0.8000 |

`lev_ratio≈0.80` reproduces QUANTUM's/Red Team's/PHOTONICS'/EM's own
four-way-independently-verified `~0.79` figure at every pair, not one.

### 2e. Widened-window candidates (design-only; item c)

Purely geometric/statistical — no new FDTD data exists at these angles,
so `cond5`, the leverage pattern, `VIF`, and `L(T)` are computed holding
the **true carrier's own `T_x`** fixed (the physical `x=sinθ` periodicity
does not change with window choice) and **sweeping both nuisance phases**
(`ψ̄` of the carrier, `ψ̄₂` of the second tone) over 8×8=64 combinations
spanning `[0°,180°)` each — every reported quantity is a (min, median,
max) over that sweep, never a single cherry-picked phase (`cond5` is
exactly phase-invariant, verified in-script by assertion).

| Window | n | Rayleigh widths (carrier↔fringe) | `cond(X5)` | `mean diag(M5)` | `VIF_Rq` (min/med/max) | `lev_ratio` (min/med/max) |
|---|---|---|---|---|---|---|
| 36–42° (baseline) | 31 | 0.65 | 59.9 | 0.8387 | 35.9/36.9/38.0 | 0.791/0.796/0.800 |
| 36–45.5° | 49 | 1.01 | 40.2 | 0.8980 | 4.7/5.5/6.5 | 0.868/0.870/0.871 |
| 36–46.0° | 51 | 1.05 | 37.1 | 0.9020 | 4.0/4.9/5.8 | 0.873/0.875/0.877 |
| 36–51.0° | 76 | 1.51 | 26.7 | 0.9342 | 1.4/1.4/1.5 | 0.914/0.914/0.914 |

### 2f. `L(T)` leakage function — item (b)

`L(T)` = max-over-relative-phase projection of a unit-amplitude sinusoid
of period `T` into `R_q`, `=√(A²+B²)`, `A=row5·cos(w_T u)`,
`B=row5·sin(w_T u)` — design-time, no data.

| Pair | `L(1.9608°)` | `L`-peak | peak location |
|---|---|---|---|
| C40–C60 | 28.0 | 36.1 | 3.48° |
| C60–C70 | 27.7 | 35.1 | 3.54° |
| C70–C80 | 27.9 | 34.9 | 3.54° |
| C40–C80 | 28.1 | 35.9 | 3.49° |

Reproduces QUANTUM's exp-072 §3 table (`|L(1.9608°)|≈26.8`, peak
`35.7–36.7` at `3.49–3.55°`) at all four pairs, within the expected spread
from a slightly different (but equally real, data-fitted) second-tone
phase convention. `L(T)` at the widened 51° window (computed, not shown
in the table above) collapses by an order of magnitude at the fringe
itself (`~1.8`, from `~28`) but its *peak* location (`~2.8°`, `Lpeak≈14`)
is still comfortably inside the window's own Nyquist limit — a wider
window shrinks the leakage budget broadly, not just against the one named
fringe.

---

## 3. T1 escape-route statement — item (f)

**None — pure instrument/statistics characterization.** This cycle fits
no medium, proposes no absorber, and computes no field response; every
quantity above is a property of a fixed design matrix (`θ` grid, a fitted
carrier period/phase) and already-published dimensionless field-ratio
data. No passivity, reciprocity, or causality claim is made or implied —
checked explicitly, against my own charter's bookkeeping duty: `ABSORB`
is not touched as a material parameter anywhere in this script (it enters
only via which already-collected series is loaded), no S-parameter or
energy quantity is computed, and no claim compares to a passive bound.
**Checkpoint-criterion-2 candidacy: none** — no constraint subset of the
phenomenon (PANEL.md §"Constraints") is bounded by this cycle; T28 is a
diagnostic side-thread in the FDTD instrument, not a phenomenon-mechanism
claim (matches exp-070/072/073's own identical ruling).

---

## 4. Idealizations

1. **600nm only.** No wavelength-general claim; T21's own established
   fringe period is itself a 600nm quantity.
2. **`ABSORB` is not a material.** Nothing here licenses a realizability
   claim; the four series are boundary-condition sweeps, not media.
3. **Single-carrier-plus-ramp basis, fixed.** The 5-column basis this
   pricing evaluates is the one T28 has used for two cycles; QUANTUM's own
   exp-072 finding (§3, "the single-carrier-plus-ramp model is
   misspecified on this window") is not re-litigated here — this cycle
   prices *that specific model's* two-tone extension, not a
   from-scratch-optimal estimator.
4. **The named contaminant is T21's own fringe only.** `L(T)`'s own
   design-time table (§2f) shows leakage of comparable or greater size
   exists across ~1.8°–5° generally; pricing the two-tone fit against
   *one* named contaminant is the best case for that fit, not the worst.
5. **Widened-window figures are a physical extrapolation, not a
   measurement.** They assume the real, fitted `T_x` (the carrier's
   period in `x=sinθ`) is unchanged outside 36°–42° — a reasonable but
   untested assumption for any smooth, slowly-varying boundary effect.
6. **`z_joint(optimistic)` is an upper bound, not a prediction.** It
   assumes the joint two-tone fit's achievable noise level and true
   effect size are identical to what the single-carrier fit measured at
   36°–42° — real data at a wider window could easily show a *worse*
   effective SNR, not better, especially given the next point.
7. **Binding curvature caveat, inherited from EM's own exp-072 §6.2
   Direction 3, unresolved here.** `cos θ` varies 8.1% across 36°–42°,
   14.1% across 36°–46°, 22.2% across 36°–51° — the "sinusoid in `x`"
   model itself strains further at a widened window. This pricing does
   not include a curvature column; a real widened-window run must, or its
   own `R_q` will absorb model-strain the way the current window's
   already does (QUANTUM's exp-072 Finding, §2f above).
8. **`lev_ratio` is a necessary, not sufficient, indicator of null
   calibratability.** `lev_ratio→1` is required for the sign-flip null's
   *variance* to be correctly sized, but `G0-e(ii)`'s own finding was
   about a specific null construction — a genuinely new null must still
   pass its own fresh calibration test at any window (R6, generalized,
   LOGBOOK Iteration 50), regardless of how favorable this pricing looks.
9. **No energy sidecar; N/A by argument, not omission** (house
   precedent) — nothing here computes absorbed power.

---

## 5. Falsifiable predicted outcomes — pre-registered numeric bands

All bands below are already met by the desk-check run committed in this
directory (`desk_check_pricing_results.json`); any future re-run of the
identical, unmodified script on the identical committed source data must
reproduce them to the stated tolerance, or this proposal's own central
claim is wrong and must be corrected, not defended (R4).

### G0 — reproduction gate (must PASS before any band below is scored)

| Gate | Bar | On FAIL |
|---|---|---|
| CHECK0 (basis identity) | `worst_rel_err ≤ 1e-9` vs exp-072's committed `results.json` | `HALT_BASIS_MISMATCH` — this script does not implement the record's own basis |
| G0-a (grid identity) | θ arrays from all sources bit-identical | `HALT_GRID_MISMATCH` |

### CLOSURE-CONFIRM (baseline window, 36–42°) — "the differential/two-tone route is priced shut in this window, independent of null choice"

⟺ at **all four pairs**: `cond9 ≥ 300` **and** `VIF_Rq ≥ 15` (SE-inflation
`≥ 3.9×`) **and** `z_joint(optimistic) < 1.5`.

**Observed (this run): CONFIRM.** `cond9∈[478,529]`, `VIF_Rq∈[31,37]`,
`z_joint∈[0.54,0.81]` — every pair clears the CONFIRM bar with wide
margin (the tightest, `z_joint=0.81` at C40–C60, is still 46% below the
1.5 threshold and 60% below the 2σ detectability bar itself).

### WIDENED-WINDOW-LICENSES-FURTHER-SPEND (θ_max≈51°, ~1.5 Rayleigh widths)

⟺ `VIF_Rq` median `≤ 2.5` (SE-inflation `≤ 1.6×`) **and**
`z_joint(optimistic) ≥ 2.0` at **≥3 of 4** pairs **and** `lev_ratio ≥ 0.90`
at every pair (necessary-not-sufficient calibratability signal, idealization 8).

**Observed (this run): CONFIRM (licenses further spend at this width,
gated on a fresh FDTD run and its own `G0-e(ii)`-style calibration
test).** `VIF_Rq` median `1.4`, `z_joint∈[2.55,4.10]` at all four pairs
(4/4, exceeding the ≥3 bar), `lev_ratio=0.914` at every pair.

### INTERMEDIATE (θ_max≈46°) — pre-registered as the honest middle

⟺ neither of the two bands above is met at that width.

**Observed (this run): NEITHER.** `VIF_Rq` median `4.9` (between 2.5 and
15), `z_joint∈[1.4,2.2]` — genuinely straddles 2σ, not resolved by
pricing alone. This band exists precisely so a future cycle cannot quietly
report "46° is basically fine" or "46° is basically the same as 42°" —
neither is true; it must be measured, not priced.

### `L(T)`-leakage cross-check (non-gating, disclosure)

Predicted: `L(1.9608°) ∈ [25,30]` at every pair (baseline), `Lpeak ∈
[33,37]` at `T∈[3.4°,3.6°]`. **Observed: matches** (§2f). At `θ_max=51°`,
predicted `L(1.9608°) < 5` (an order-of-magnitude collapse). **Observed:
1.76** — confirmed.

---

## 6. Pre-committed decision rule (Iteration-51 queue item 5, binding)

**This pricing decisively closes the differential/two-tone route in the
current 36°–42° window** (§5, CLOSURE-CONFIRM, all four pairs, wide
margin). Per PANEL.md's own "mapped constraint boundary" alternative
product and matching the **Block-MINI precedent** (exp-069, Iteration 46:
a properly-powered, pre-registered test answering its own question
honestly, formally retired rather than deferred a further time):

> **T28's differential/two-tone-fit sub-thread, at θ∈[36°,42°], is
> formally retired as of this cycle's close — not deferred a sixth time.**
> No future cycle should re-fit `R_q` (single-carrier or two-tone) on this
> exact 124-point/31-angle substrate as a route to resolving the ~2.5°
> family's mechanism. The reason, stated here per this program's own
> non-relabeling discipline: statistical power was priced, in committed
> code, against the real fitted carriers of all four pairs and the
> design's own established leverage mechanism, and the answer is
> decisively negative *independent of which null eventually gates it* —
> continuing to fit this window cannot produce a `RESOLVED` pair no matter
> how the null is calibrated.

**This is NOT a formal retirement of T28 itself**, nor of the
differential-fit *method* at every window — §5's second band shows a
substantially wider window (~51°, ~1.5 Rayleigh widths, ≈45 new FDTD
calls for a two-config extension, cf. EM's exp-072 §6.2 costing) plausibly
changes the calculus, gated on its own fresh `G0-e(ii)`-style calibration
test and the curvature column promoted from disclosed to fitted
(Idealization 7). **Binding forward rule, matching queue item 5's own
requirement for what a further non-decisive outcome would mean:** if a
future cycle runs the widened window and its own properly-calibrated null
construction and *still* returns a non-decisive verdict (Combined Verdict
`NEITHER` or an equivalent `HALT`), that outcome — a **sixth-or-later**
non-advancing cycle on this exact sub-thread, this time at a window this
pricing calculation itself certified as favorable — must be scored
`FORMAL_RETIREMENT_NON_DECISIVE` for the differential/two-tone-fit
*method as a whole*, at any window, with no further deferral and no
further widening proposed as a next step. The method gets exactly one
more properly-priced attempt, at the width this cycle shows is worth
trying; it does not get an indefinitely receding goalpost.

---

## 7. Cost estimate

**Zero FDTD calls. Zero `lab/` diff.** `desk_check_pricing.py` reads three
already-committed `results.json` files and runs in **1.3s** (measured,
this run, single core) — pure `numpy` linear algebra (matrix inverses,
condition numbers, a 64-point phase sweep per window candidate, an
861-point `L(T)` grid per pair). If Phase 3/4 adopts this proposal
verbatim, the "run" is re-executing this same script; there is no
meaningful cost axis to trade off against — the entire point of this
cycle is that the answer was obtainable for free five cycles ago.

---

## Reproduction

`python3 experiments/074-t28-window-pricing-cramer-rao-bound/desk_check_pricing.py`
— writes `desk_check_pricing_results.json` in this directory and prints
the summary tables above. No seed, no Monte Carlo, no stochastic element
anywhere in this script (the phase "sweep" is a deterministic grid); two
independent invocations are byte-identical.
