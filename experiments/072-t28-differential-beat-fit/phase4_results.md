# PHASE 4 — TEST · Panel Iteration 49 · exp-072
## Official run: `python3 run.py`, seed 20490072, zero new FDTD calls

**This document REPLACES the original phase4_results.md in full** (Red
Team's Phase-5 final audit RT-5: "wholly superseded, not partially, and
must be republished rather than annotated" — nearly every number in the
original changed). The Combined Verdict is unchanged: `NEITHER`, verified
independently by the Director's own patch, by three of six Phase-5 blind
seats, and by Red Team's final audit, robust to the entire same-shift
correction set (§7 below), not only to the sign fix that triggered it.

## What happened between the original run and this one — read first

The first official run of this cycle (git history: commit `3059bfb`) was
executed on a **mis-rotated estimator basis**: a carrier-phase sign error
in the step-1→step-2 handoff (`_amp_phase_at`) made every published
coefficient a rotation of the intended one by `2ψ̄` (the common-mode carrier
phase — a nuisance parameter). Three of six Phase-5 blind seats (PHOTONICS,
MATERIALS, ELECTROMAGNETISM), using three different methods, independently
found this; the Director independently re-derived it from scratch and
applied a fix; Red Team's Phase-5 final audit independently re-verified the
fix against a synthetic ground-truth sweep (recovered/true ΔP = **1.0000 ±
0.0007** over 16 phases × 7 effect sizes) and against five Phase-2 ledger
quantities that reproduce post-fix and did not pre-fix. The audit then
found the fix was incomplete (the executed basis still deviated from the
frozen `-sin` convention) and issued a 10-item same-shift docket, all
implemented in this re-run. **CHECKPOINT criterion 4 fires** on this
cycle — see LOGBOOK.md Iteration 49 for the full ruling (a notification,
not a pause; Combined Verdict unaffected).

A new standing house tripwire, `G0-e` (a synthetic ground-truth recovery
gate), is now mandatory machinery for any cycle fitting a carrier- or
phase-conditioned coefficient — see §1.

## Pre-registration contamination disclosure (binding, unchanged from the original)

During Phase 2, QUANTUM OPTICS executed the proposed estimator and both
candidate nulls on the real committed data (withholding outcome numbers)
and VISION SCIENCE executed the estimator and published outcome-determining
numbers. Red Team then independently computed the observed surrogate
p-values under both nulls. Per Red Team's Phase-2 ruling, any CONFIRM-shaped
result this cycle is coded to emit as `CONFIRM_UNCERTIFIED`, never
`CONFIRMED` — verified inert on this data, before and after all
corrections (no pair reaches `RESOLVED` under any combination tested).
**Correction to the original disclosure text** (Red Team's Phase-5 final
audit, QUANTUM's finding): the null choice was outcome-determining between
`UNDERPOWERED_NOT_EVALUABLE` and `NEITHER`, not between `REFUTED` and
`NEITHER` as originally stated — the REFUTE branch was blocked independently
by the power-demonstration precondition (docket item 3) regardless of which
null was used, so `REFUTED` was never actually reachable on this data. The
four binding conditions of the original ruling are unchanged; only this
factual claim is corrected.

## Gates

| Gate | Result |
|---|---|
| G0-a (grid identity, 3-way) | **PASS** — bit-identical |
| G0-b (telescoping identity) | **PASS** — `max\|residual\| = 0.0` exactly |
| G0-c (column provenance) | **PASS** — `max\|Δ\| = 0.0` exactly |
| G0-d (conditioning, per pair) | **PASS**, all four: `cond5 ≈ 59.9–61.0` (≪100) |
| **G0-e (NEW, T1-2 — ground-truth recovery)** | **PASS** — recovered/true ΔP within **0.15%** of 1.0000 across 16 carrier phases × 10 effect sizes (worst cell 0.0015; HALT threshold 0.02) |

## P-072-1 — full per-pair table (published regardless of every other outcome)

| Pair | `T_mean` (°) | carrier R² | `R_q` | `A_i` (= `a_B−a_A`) | `SE(R_q)` OLS / residual-bootstrap | `p` unrestricted (Holm) | `p` restricted (Holm) | `cond5` |
|---|---|---|---|---|---|---|---|---|
| C40–C60 | 2.4865 | 0.4394 | −0.02754 | +8.240e−4 | 0.00562 / 0.01230 | 0.1737 (0.5212) | 0.0067 (**0.0135**) | 60.0 |
| C60–C70 | 2.5285 | 0.4451 | −0.00353 | +5.70e−6 | 0.00116 / 0.00514 | 0.7430 (0.9536) | 0.1042 (0.1042) | 60.8 |
| C70–C80 | 2.5325 | 0.4380 | +0.00355 | −8.78e−5 | 0.00083 / 0.00248 | 0.4768 (0.9536) | 0.0045 (**0.0135**) | 61.0 |
| C40–C80 | 2.4905 | 0.4308 | −0.02618 | +7.413e−4 | 0.00562 / 0.01651 | 0.3716 (unadj., *derived*) | 0.0171 (unadj., *derived*) | 59.9 |

*C40–C80's p-values are reported unadjusted and labeled derived — G0-b
proves it is the exact arithmetic sum of the other three (docket item 14);
it is not an independent fourth test, and (T1-9) is excluded from the
REFUTE-blocking count below for the same reason.*

`A_i` now reads true against its own pre-registered definition
(`A_i = a_B − a_A`, docket item 1's table): the C40–C60 figure (+8.240e−4)
matches the directly-measured per-config amplitude difference to 6.5% —
the deeper-`ABSORB` config's common-mode fringe amplitude is genuinely
**larger**, at three of four pairs, which is itself informative (§8): a
purely absorptive `ABSORB`/`PAD` axis could not increase the boundary
return monotonically.

**Residual bootstrap (T1-5): 2.2–4.4× the naive OLS SE**, not the
3.7–4.8× originally published — the original used case-resampling on a
*deterministic, uniformly-spaced 31-point design grid*, the wrong bootstrap
for a fixed design (it duplicates/drops θ nodes and destroys the free-period
search's own resolving power). This version holds the θ design fixed and
resamples residuals (both the common-mode carrier fit's and the ramp fit's),
refitting the free period and phase on every draw — genuinely propagating
step-1 `(T_mean, ψ̄)` uncertainty as docket item 7 specified.
**`|R_q|/SE_bootstrap` = 2.24 / 0.69 / 1.43 / 1.59** — three of four pairs
now clear 1σ and one (C40–C60) clears 2σ; the original "no pair clears 2"
claim does not hold under the corrected propagation. None of this gates
`RESOLVED`, which runs on the surrogate p, not on this ratio.

**Phase/frequency/strain decomposition (P-072-6), corrected:**

| Pair | phase channel `\|A_q\|/a` | freq channel `\|R_q\|σ_u/a` | strain channel `\|R_i\|σ_u/a` | `\|R_i/R_q\|` | `dR_q/dψ̄` (= `R_i` exactly) | strain flag |
|---|---|---|---|---|---|---|
| C40–C60 | 0.039 | 0.127 | 0.061 | 0.478 | −0.01316 | False |
| C60–C70 | 0.041 | 0.015 | 0.042 | 2.811 | −0.00991 | **True** |
| C70–C80 | 0.012 | 0.015 | 0.025 | 1.687 | −0.00598 | **True** |
| C40–C80 | 0.087 | 0.121 | 0.133 | 1.099 | −0.02877 | **True** |

`\|R_i/R_q\|` now matches docket item 11's own pre-registered expectation
(0.48 / 2.81 / 1.69 / 1.10) to the digit; the strain flag fires at **three**
of four pairs (C60–C70, C70–C80, C40–C80), not two as originally reported.
`dR_q/dψ̄` — one of docket item 7's mandated-but-never-computed
quantities — turns out to be **exactly `R_i`** (verified to 5 decimals,
an algebraic identity of the estimator's own rotation structure, not a new
computation): the coefficient the single-carrier model predicts is zero is
in fact the exact sensitivity of the target coefficient to the carrier
phase, and it dominates `R_q` at three of four pairs. `SE(ΔP)` at `T_mean`,
propagated from the residual bootstrap: **0.031° / 0.012° / 0.006° /
0.042°** — against a total measured C40→C80 period span of 0.093°, this is
1σ ranging 6–45% of the whole effect the estimator is chasing.

**ΔP at all four carriers (item 12, mandatory disclosure — VISION's
original finding, corrected normalization at the two wrong carriers, T1-7):**

| Pair | `T_mean` | `T_delta` (pair's own) | `T_wrong` = 1.2591° (displaced, corrected constant) | `T_wrong` = 1.9608° (T21 fringe, disclosure only) |
|---|---|---|---|---|
| C40–C60 | **+0.0697°** | −0.0001° | +0.0435° | +0.0092° |
| C60–C70 | +0.0085° | +0.0127° | +0.0122° | −0.0177° |
| C70–C80 | −0.0086° | +0.0153° | −0.0023° | −0.0080° |
| C40–C80 | **+0.0668°** | −0.0054° | +0.0553° | −0.0175° |

The original wrong-carrier column (`3.60°`) has been **struck and replaced**
— it was 0.70–0.75 Rayleigh widths from the carrier, not the ≥1.5 the
docket claimed, and sat within 2% of the *global maximum* of the leakage
function it was meant to be clean of (§4). `1.2591°` is the data-free
leakage-minimizing comparator (worst-pair leak 0.988 vs ~35.8 at 3.60°, a
36× reduction, at 2.36–2.40 Rayleigh widths) that Red Team's audit derived
and this run adopts.

Sign is still not invariant across the admitted carrier set — C60–C70 and
C40–C80's signs at `T_delta` disagree with `T_mean`'s — but the pattern is
milder than originally reported (which used a comparator sitting at the
leakage maximum and therefore maximally unstable by construction). The
`1.9608°` disclosure column (a resolution identity, never a control — see
§4) is retained unchanged in sign pattern.

**Curvature column (item 15, disclosed, non-gating), in the frozen `-sin`
basis:** coefficients −0.814 / −0.232 / −0.006 / −0.996 (sign and magnitude
both changed from the original, which was computed in the un-restored
basis) — non-negligible at three of four pairs, recorded without further
interpretation this cycle.

## P-072-2 — does the differential instrument resolve structure?

`RESOLVED` requires: `cond5 ≤ 100` **and** restricted-null Holm-adjusted
`p ≤ 0.01` **and** the linearization gate **and** the recalibrated
carrier-consistency gate **and** the displaced-wrong-carrier gate
(now **Holm-adjusted**, per docket item 10's own frozen rule — T1-4/RT-4;
the original tested raw p).

| Pair | cond OK | `p` restr. Holm ≤ 0.01 | linearization | carrier (obs vs. `q95`) | wrong-carrier: magnitude / p-Holm | **RESOLVED** |
|---|---|---|---|---|---|---|
| C40–C60 | ✓ | 0.0135 — fails | ✓ | 0.1235 ≤ 0.4715 ✓ | ✓ / 1.000 ✓ (**passes**) | **No** |
| C60–C70 | ✓ | 0.1042 — fails | ✓ | 0.1622 ≤ 0.2724 ✓ | ✗ / 1.000 (**fails on magnitude**) | **No** |
| C70–C80 | ✓ | 0.0135 — fails | ✓ | 0.2540 ≤ 0.3853 ✓ | ✓ / 1.000 ✓ (**passes**) | **No** |
| C40–C80 | ✓ | 0.0171 — fails | ✓ | 0.1410 ≤ 0.3767 ✓ | ✓ / 0.444 ✓ (**passes**) | **No** |

**Zero pairs `RESOLVED`** — unchanged from the original run, but for a
different reason at three of four pairs: the corrected wrong-carrier gate
now *passes* three of four pairs (vs. one of four originally), and every
pair is stopped purely by the significance clause, which never reaches
`p ≤ 0.01` anywhere (minimum 0.0135).

Not CONFIRM (requires C40–C80 and C40–C60 `RESOLVED` plus at least one of
{C60–C70, C70–C80} — none resolved). Not REFUTE either:
`n_resolved_holm10_restricted = 2` (T1-9: counted over the **three free
pairs only** — C40–C60 and C70–C80 clear the relaxed `p ≤ 0.10` bar; the
original count of 3 double-counted the derived C40–C80 pair). REFUTE
requires **zero** pairs at `p ≤ 0.10` under *both* nulls; two clear it under
the restricted null. **P-072-2 = `NEITHER`.**

## Injection-recovery power test (item 4) — reconstructed, T1-3

The original construction injected the predicted ramp **on top of the
observed data** rather than into a clean null base (`yhat0 + resid0 ≡
delta_ab` identically, so `Rq_recovered = Rq_observed + Rq_predicted`) and
scored against a raw p where the docket froze a **Holm-adjusted** `p ≤ 0.01`
rule. Both are corrected here: the pair's own fitted `R_q` is stripped
before injecting, so the injected amplitude is exactly `Rq_pred` by
construction, and the reported figure is Holm-adjusted over the three
pairs.

| Pair | `R_q` predicted (from committed `m₀`) | `R_q` observed (stripped before injection) | `R_q` recovered | raw `p` | **Holm-adjusted `p`** |
|---|---|---|---|---|---|
| C40–C60 | −0.02021 | −0.02754 | −0.02021 | 0.0110 | 0.0271 |
| C60–C70 | −0.01060 | −0.00353 | −0.01060 | 0.0146 | 0.0271 |
| C70–C80 | −0.01053 | +0.00355 | −0.01053 | 0.0090 | 0.0271 |

**`power_demonstrated = False`** — under the corrected construction and
the docket's own frozen Holm rule, **zero of three** pairs demonstrate
power (all Holm-adjusted p = 0.027, above 0.01), not two of three as
originally reported. The original per-pair story is **struck**: it
credited C40–C60 and C60–C70 with "passing" and blamed C70–C80 for a "small
margin" miss, driven entirely by the self-cancellation artifact (at
C70–C80 the observed and injected ramps were opposite in sign, so the old
test recovered only 44% of what it injected; C40–C60's old "pass" was
correspondingly amplified by constructive interference). Under the
corrected, H₀-clean construction, **C70–C80 has the strongest raw signal of
the three** (p=0.0090) — the reverse of the original attribution.

## P-072-3 — closure, corrected interpretation (T1-6/RT-1)

Requires all three adjacent pairs `RESOLVED`; none are. **`NOT_EVALUABLE`.**

**A genuine new finding this shift, not in the original docket**: item 8's
mandated calibration (a "3.79% telescoping residual at a common carrier")
is not merely unimplemented — it is **mathematically vacuous, always
exactly 0%**. G0-b proves the raw `delta_AB` series telescope bit-exactly
(`delta_40_80 ≡ delta_40_60 + delta_60_70 + delta_70_80`), and OLS on a
*fixed* design matrix is a linear functional of `y`; therefore `R_q`
telescopes identically at *any* shared carrier, always. Verified directly:
refitting all four pairs at C40–C80's own `(T_x, ψ̄)`, the telescoping
residual is **1.3×10⁻¹⁶ relative** — machine zero. `ρ_c` (the
per-pair-own-carrier version this cycle actually gates on) is therefore
**not a basis-stability statistic** — it measures nothing but each pair's
own carrier choice, and is this cycle's cleanest single measurement of
carrier sensitivity, not item 8's intended calibration target.

## P-072-4 — consistency with Iteration 48's `ABSORB`-depth trend, or new structure?

Evaluated over `RESOLVED` pairs only; none resolved. **`NEITHER`** (fewer
than 2 resolved pairs — the design's own pre-registered fallback for
insufficient data).

**Disclosed only (docket item 9, non-gating), for completeness — unchanged
by the sign-bug fix (this analysis never touches step 2):** the committed
linear `m₀ = 0.0025564°/cell` and an engine-motivated saturating model
(scale constant `_damping`'s depth-averaged per-step exponent, 0.075/cell,
**imported from an amplitude-attenuation context to a phase observable
with no stated causal relation** — softened language per T1-10i) were both
fit to the four per-config free periods at this cycle's own `n_grid=3000`
(2.43748° / 2.52051° / 2.53551° / 2.53051° for C40/C60/C70/C80):

| Model | Params | R² |
|---|---|---|
| Linear in `ABSORB` | 2 (intercept, slope) | 0.8328 |
| Saturating, `L=0.075/cell` fixed | 2 (`P_∞`, amplitude) | **0.9901** |

**Correction (VISION's D11 finding, confirmed): the published R² = 0.8328
belongs to a slope of 0.0024637 that this fit *re-derives*, not to the
committed `m₀ = 0.0025564`** — the exact figure-provenance defect (Attack
5) the docket was written to prevent, reproduced inside the disclosure
meant to prevent it. Both models remain disclosed, non-gating context; the
ranking (saturating over linear) is robust to the choice of decay constant
over 0.02–0.30/cell and to this tie-break, on four points against two
parameters — it discriminates curvature, not functional form or decay
constant, and the fitted saturating model's own extrapolation to
`P(ABSORB=0) = 0.46°` sits below the free-period search's own 1.0° floor
and is not physically meaningful.

## Combined Verdict — branch trace

1. G0 gates: **PASS** (all five, including the new G0-e).
2. P-072-2 = `NEITHER`, P-072-4 = `NEITHER` → neither REFUTE condition
   fires.
3. CONFIRM requires P-072-2 CONFIRM AND P-072-4 CONFIRM — neither holds.
4. → **`NEITHER`.**

The contamination-ruling override (`CONFIRM_UNCERTIFIED`) never engages —
verified inert under every combination of the fixes tested (see §7).

## Bottom line (rewritten, T1-10b)

The fixed, officially pre-registered design resolves **zero of four**
`ABSORB` pairs in this window. The reason, measured rather than argued:

**`R_q` is the projection of `delta_AB(θ)` onto an axis fixed by a nuisance
parameter — the common-mode carrier phase `ψ̄`.** The sensitivity is exact
and free: `dR_q/dψ̄ ≡ R_i`, with `|R_i| ≥ |R_q|` at three of four pairs. The
window (36°–42°, `X = ptp(sinθ) = 0.08135`, Rayleigh width `1/X = 12.29`,
**2.4 carrier cycles across 31 points**) does not make `R_q` non-identifiable
against *specifically* T21's 1.9608° fringe — it is non-identifiable against
essentially **any** periodic contributor from ~1.8° to ~5.0° (a data-free
leakage calculation, `|L(T)| = 15–36` per unit amplitude across that band,
peaking at 3.48–3.54°; the 1.9608° fringe, `|L|≈28`, is one named member of
that band and not its worst). The single-carrier-plus-ramp model is
misspecified on this window, the ramp column absorbs the misspecification,
and at 2.4 cycles absorbed misspecification is indistinguishable from a
genuine `Δf`. That is a stronger, more general and more falsifiable
statement than "T21's fringe contaminates it," and it is what the corrected
numbers support — not the noise floor the Phase-1 proposal's a-priori power
table anticipated.

The carrier itself is well-determined (R² ≈ 0.43–0.45 at every pair,
matching — not exceeding — Iteration 48's own per-config fits; the
common-mode construction bought no improvement in carrier determination,
which is the parameter whose uncertainty actually broke the estimator). The
genuine instrument-conditioning improvement is `cond5 ≈ 60` — well below
the `≤100` gate — not the carrier fit.

## Caveats (binding, per Idealizations above and Red Team's docket item 13)

- **600nm only** — no wavelength-general claim.
- **2D TMz, single polarization; positive-θ branch only (36°–42°), not a
  symmetry test; bench scale (`R_OUT=78` cells) — no witness-scale claim**
  (restored; dropped from the original caveat block).
- **`ABSORB`/`PAD` compound-axis confound not relieved, AND the mixture is
  non-identifiable against frequency-or-fringe-weight change.** Any future
  CONFIRM-shaped language on this series must read `ABSORB`-or-`PAD`-or-
  frequency-or-fringe-weight-tied, never cleanly `ABSORB`-tied. This binds
  every table above, under every verdict, not only a hypothetical CONFIRM.
  This channel (P-072-6's amplitude/phase readouts) supplies the confounded
  arm of Iteration-49 queue item 2 and does not substitute for the
  dedicated PAD-decorrelation build that item requires.
- **`ABSORB` is not a material** — a numerical boundary-condition parameter
  ("graded damping mask," not "graded absorber" — no permittivity,
  conductivity, dispersion, or impedance to match); no realizability claim
  licensed.
- **Window provenance**: the 31-point 36.0°–42.0° grid is inherited from
  Block MINI; T28 was discovered inside it; no cross-cycle multiplicity
  correction is applied across the ~12 statistics now computed on these
  same 31 points across exp-069/071/072.
- **`C_empty` is a dimensionless field ratio, not a Michelson/Weber
  perceptual contrast**; `ptp/mean=16.2`-style figures are fit-conditioning
  statistics, never photometric ones.
- Energy sidecar: N/A this cycle, no absorbed-power number produced
  anywhere in the design.
- **Queue item 4 (PHOTONICS' two-tone joint fit) is explicitly re-deferred**
  this shift: `P-072-5` is a single-carrier contamination diagnostic, not a
  two-tone joint fit, and a Cramér–Rao feasibility calculation (§4) is
  queued ahead of it for Iteration 50.
- **The measured second-tone period (1.824–1.837°, §4) is UNQUOTABLE
  without a null-permutation control** — it is a free-period search over
  the same continuum this program's own R5/Iteration-47 look-elsewhere
  discipline governs, and none has been run.
- Pre-registration contamination: see disclosure above — this cycle's
  p-values should be read as design-verification numbers computed under a
  fully-specified, Red-Team-audited design, not as a first, blind look.
- **The order reversal between C70/C80's free periods at `n_grid=3000` vs.
  `n_grid=400`** (2.53551° vs. 2.53051°, a 5-grid-step, 0.5%-of-Rayleigh-floor
  effect) underlies the saturating-model's own curvature and should not be
  read as more than a resolution-robust but very fine-grained measurement.

## §4 — the leakage function and the case for closing this window (disclosure, non-gating)

Red Team's Phase-5 final audit computed `L(T)`, the coefficient with which
a unit-amplitude sinusoid of period `T` projects into `R_q` through the
fixed 5-column basis, maximized over relative phase — a **data-free**
function of the design matrix and the θ grid alone. It peaks at
3.48°–3.54° (`|L|` = 34.9–36.1) and remains 15–36 per unit amplitude across
roughly 1.8°–5.0°. A second-contributor amplitude difference of only 3–6%
of carrier amplitude reproduces the entire observed `R_q` at almost any
period in that band. ELECTROMAGNETISM's independent Cramér–Rao-style
pricing of a two-tone joint fit (queue item 4) in this same window gives a
condition number of 529 (vs. this cycle's 60) and a 6× SE inflation on
`R_q` — against corrected `|R_q|/SE_OLS` ratios of 4.9/3.0/4.3/4.7,
suggesting the two-tone route cannot reach 2σ at this SNR in this window
either. Iteration 50's queue (LOGBOOK.md) ranks pricing this feasibility
question, and possibly widening the window past `θ_max ≈ 46°` (where the
carrier and T21's fringe first separate by a full Rayleigh width), ahead of
any further FDTD spend on this specific differential/beat instrument.
