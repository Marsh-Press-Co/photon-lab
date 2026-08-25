# PHASE 5 — RED TEAM FINAL AUDIT · Panel Iteration 49 · exp-072
## PHOTONICS' differential/beat fit of `delta_AB(θ)` for T28 — final ruling, same-shift docket, checkpoint determination

*Fresh sub-agent, RED TEAM charter (PANEL.md seat 7: attacks every proposal,
speaks last and hardest; kills internal inconsistency, unfalsifiable claims,
mechanisms inexpressible as simulation parameters, and quiet
constraint violations; never leads, has no proposal to protect). Input
packet: the full Phase 1–4 record, all six Phase-5 blind reviews, `run.py`
and `results.json` in their **post-fix** state, and the Director's applied
patch. Nothing below is adjudicated from prose alone: every load-bearing
claim in this document was re-executed in an independent scratch session
against the committed code and the committed JSON, and where I disagree
with a seat I give the reproduction.*

---

## 0. Independent re-verification performed

Fifteen computations, ~6 min desk cost, zero FDTD, zero `lab/` diff, zero
committed file modified during the audit.

| # | Check | Result |
|---|---|---|
| A | Phase convention re-derived from scratch: fit `A·cos(wu+φ)` at 5 values of φ | `atan2(b,a) = −φ` exactly; `psi = −atan2(b,a)` is required for `θ_c = wu+psi` to track the carrier |
| B | Synthetic ground truth, post-fix chain, ψ₀ swept over `[0,2π)` at ΔP=+0.05° | recovered/true = **1.0000**, range [0.9999, 1.0003] |
| C | Same, ΔP swept ±0.005 → ±0.08° at ψ₀=1.75 | ratio **1.0000–1.0008** |
| D | 2-D grid, 16 phases × 7 ΔP | **max \|ratio−1\| = 0.00069** |
| E | Pre-fix code emulated (psi=+atan2, leading minus restored) | ratio = **−cos(2ψ₀)** exactly, over the full [−1,+1] range |
| F | `R_q / (2πa·Δf)` in the committed `+sin` basis | **−1.0004** — opposite sign to docket item 5's frozen `R_q = +2πa·Δf` |
| G | Rayleigh widths, all four pairs, six candidate comparators | 3.60° = **0.702–0.746**, not ≥1.5; ≥1.5 requires **T ≤ 1.5331° or T ≥ 6.5765°** |
| H | Leakage function `L(T)` (data-free), 17 periods × 4 pairs, plus global max | 3.60° sits at **99.1–99.8% of the global maximum** (34.8–36.1/unit amp) |
| I | Injection identity on the **post-fix** JSON | `Rq_recovered − (Rq_obs + Rq_pred) = 0` to machine zero at all three pairs |
| I2 | H₀-clean injection rebuilt, 20 000 surrogates, + Holm | pass/fail set **inverts**; 0 of 3 pass under the docket's own frozen Holm rule |
| J | Case bootstrap ratios from JSON vs design-respecting residual bootstrap (300 draws, step 1 refit) | 2.27/4.87/2.89/2.96× vs **1.60/1.77/1.87/1.85×**; `\|R_q\|/SE` = **3.06/1.72/2.27/2.52** |
| K | `ρ_c`, `‖R‖`, `\|R_i/R_q\|`, `dR_q/dψ̄` | `ρ_c` = **0.0408**; `dR_q/dψ̄ ≡ R_i` to 5 decimals; `\|R_i/R_q\|` = **0.478/2.811/1.687/1.099** |
| M/N | Wrong-carrier gate clause decomposition; phase-invariant `‖R‖` test, 20 000 surrogates | magnitude clause fails **4 of 4**; `‖R‖` Holm = **0.104/0.143/0.143** |
| P/Q | `A_i` vs directly measured `a_B − a_A`; ΔP sign agreement vs `n_grid=3000` absolute differences | `A_i(C40–C60)` = **+8.2396e−4** (6.5% off measured); sign agreement **4/4** |
| R/T/U | Item-8 telescoping residual at a common carrier; gate re-run at `T_ctrl=1.259°`; item-6 gate admissible range | **0.0000% exactly**; 3 of 4 would pass; gate admits **46–78%** of the `[1,4]°` search range |

---

## 1. Ruling on the Director's applied fix

### 1.1 The sign fix is CORRECT. Re-derived from scratch, not accepted on the reviews' authority.

The claim under test is that `_fixed_period_fit` fits `y = c₀ + a·cos(wu) +
b·sin(wu)`, that this equals `c₀ + A·cos(wu + ψ)` with `ψ = −atan2(b,a)`,
and that `design_matrix`'s `θ_c = wu + psi` therefore requires
`psi = −atan2(b,a)`. I tested it directly rather than algebraically —
constructed carriers with a *known* `φ` written in `design_matrix`'s own
convention `A·cos(wu + φ)` and asked what `_fixed_period_fit` returns:

| φ (constructed) | `atan2(b,a)` | `−atan2(b,a)` |
|---|---|---|
| 0.0000 | +0.000000 | −0.000000 |
| +0.4000 | −0.400000 | **+0.400000** |
| +1.2000 | −1.200000 | **+1.200000** |
| −2.0000 | +2.000000 | **−2.000000** |
| +3.0000 | −3.000000 | **+3.000000** |

Exact at every value. The patch is right, and the Director's docstring
derivation (which writes the carrier as `A·cos(wu − φ)` with `φ = atan2(b,a)`)
is the same statement in the other sign convention. **Confirmed.**

### 1.2 The fix is COMPLETE on the ΔP axis — verified against ground truth, not against plausibility.

The failure mode that produced this bug was that every gate in the design
(`cond5`, R², residuals, fitted values) is invariant under the rotation the
bug induces, so "the numbers look reasonable" is not evidence. I therefore
tested the post-fix chain against a known input:

**Phase sweep, ΔP = +0.05° held fixed, ψ₀ over `[0, 2π)`** — recovered/true
= 0.9999, 0.9999, 1.0001, 1.0003, 1.0002, 1.0000, 0.9999, 0.9999, 1.0001,
1.0003, 1.0002, 1.0000. **Flat in the nuisance parameter, which is the whole
requirement.**

**Effect-size sweep at ψ₀ = 1.75 (the real data's regime)** — ratios 1.0000 /
0.9999 / 1.0000 / 1.0001 / 1.0002 / 1.0001 / 1.0008 for ΔP = +0.005 / +0.010 /
+0.020 / −0.010 / −0.040 / +0.040 / +0.080°.

**Full grid, 16 phases × 7 effect sizes: max |ratio − 1| = 0.00069.**

And the pre-fix code, emulated (`psi = +atan2`, leading minus restored),
returns **exactly `−cos(2ψ₀)`**: −0.9999, −0.4999, +0.5001, +1.0003, +0.5001,
−0.5000, −0.9999 at ψ₀ = 0 … π. The estimator's answer was a pure function
of a parameter carrying no information about ΔP. ELECTROMAGNETISM's
characterisation ("wandering over [−1,+1] tracking cos(2ψ̄)") is exact.

The fix also carries the correct sign convention: **ΔP is recovered as
`P_B − P_A`**, positive meaning the higher-`ABSORB` config has the longer
period. Verified in the ground-truth construction.

### 1.3 Four independent Phase-2 ledger quantities reproduce post-fix and did not pre-fix

This is the decisive evidence, because these are numbers computed by a
*different* implementation before `run.py` existed:

| Quantity | Phase-2 ledger | pre-fix run | **post-fix run (mine)** |
|---|---|---|---|
| Docket item 11's `\|R_i/R_q\|`, pre-registered | 0.48 / 2.81 / 1.69 / 1.10 | 0.892 / 12.342 / 0.613 / 2.417 | **0.478 / 2.811 / 1.687 / 1.099** |
| item 11's strain flag, "verified to fire at three of four pairs" | 3 of 4 | 2 of 4 | **3 of 4** (F/T/T/T) |
| Attack 3's `A_i` at C40–C60 ("fitted 8.24e−4 vs measured 7.73e−4, 6%") | +8.24e−4 | −7.33e−4 | **+8.2396e−4** vs measured **+7.7333e−4**, **6.5%** |
| Attack 7 / VISION's `ρ_c` closure | 0.041 | 0.0846 | **0.0408** |
| Attack 10's ΔP sign agreement with the `n_grid=3000` absolute differences | 4/4, ratios 0.84/0.57/1.72/0.72 | 3/4 | **4/4, ratios +0.84/+0.57/+1.72/+0.72** |

Five for five, to the quoted digits, on quantities nobody could have tuned.
**Red Team's Phase-2 implementation was correct; the committed `run.py` was
not it; the patched `run.py` is.**

### 1.4 One residual defect the fix leaves standing: the executed basis is not the frozen basis

`phase1_proposal.md:99` and docket items 1 and 15 freeze the basis as
`[1, cos θ_c, −sin θ_c, u·cos θ_c, −u·sin θ_c]` with curvature column
`u²·(−sin θ_c)`. `run.py::design_matrix` builds the `+sin` variants. The
column *span* is identical, so `cond5`, the residuals, the H₀ fit, the
surrogate construction and every `|·|` statistic are unaffected — but I
measured the consequence directly:

> `R_q / (2πa·Δf) = **−1.0004**` in the executed basis, against docket item
> 5's frozen `R_q = 2πa·Δf`.

So the published `A_q`, `R_q`, `R_i` and curvature columns carry **the
opposite sign to their own pre-registered definitions**. The Director's
patch compensated for this correctly by removing the leading minus from
`delta_P_obs` / `dP_from` / `df_pred`, which is why ΔP is now right — but
the compensation is undocumented and the coefficient table is now published
in a convention no document states. MATERIALS' §2e (docket-literal basis +
`atan2(-b,a)` + keep the leading minus) is the equivalent alternative and
restores the frozen algebra verbatim. **Tier-1 docket item 1 below adopts
it**, because the Director is re-running anyway, the change is four lines,
it is provably ΔP-neutral and p-value-neutral, and it removes a permanent
reading hazard from the record.

**Ruling: the fix is correct and complete for every gate, every p-value, the
Combined Verdict and ΔP. It is incomplete on coefficient-sign
pre-registration compliance, and it does not touch the other seven
substantive defects the reviews found.**

---

## 2. Adjudication of the six blind reviews

Twenty-nine distinct substantive findings across six seats. I re-executed
the load-bearing ones. Ruling per finding; overrules argued.

### 2.1 CONFIRMED — re-executed by me, and standing

| # | Finding | Seats | My reproduction |
|---|---|---|---|
| C1 | `_amp_phase_at` carrier-phase sign error; every coefficient a `2ψ̄` rotation | PHOT D1, MAT §2a, EM 2a | §1.1–1.2. Confirmed; **fixed** |
| C2 | Executed basis deviates from the frozen `−sin` basis in 3 columns | PHOT D2, EM 2b, MAT §4e | §1.4. Confirmed; **still live** |
| C3 | Injection test injects on top of the observed ramp: `Rq_rec ≡ Rq_obs + Rq_pred` | PHOT D4, EM D2, THERMO D2, QUANTUM D1, VISION D8 | Machine-zero identity on the **post-fix** JSON at all three pairs. Amplification 2.363× / 1.333× / **0.663×** |
| C4 | Pass/fail set inverts under an H₀-clean base | EM D2, THERMO D2, QUANTUM D1, VISION D8 | as-coded p = 0.0020/0.0071/**0.0170**; H₀-clean p = **0.0109/0.0149**/0.0075. C70–C80 is the **best**-powered pair |
| C5 | Item 4's frozen rule is Holm-adjusted `p ≤ 0.01`; `run.py` tests raw `p` | **QUANTUM D2, sole finder** | Confirmed against docket text. Holm: as-coded 0.0060/0.0142/0.0170; H₀-clean 0.0225/0.0225/0.0225. **Zero of three demonstrate power under the frozen rule, either way** |
| C6 | `T_WRONG = 3.60°` is 0.702–0.746 Rayleigh widths, not ≥1.5 | PHOT D3, EM 1b, QUANTUM D3 | Confirmed. ≥1.5 requires **T ≤ 1.5331° or ≥ 6.5765°**; search range `[1,4]°` admits only the lower branch |
| C7 | 3.60° sits at the **maximum of the leakage function** it was meant to be clean of | **QUANTUM D3, sole finder** | Confirmed and sharpened: global max of `\|L(T)\|` is 34.87–36.13 at T = 3.481–3.539°; `\|L(3.60°)\|` = 34.79–35.81 = **99.1–99.8% of max** |
| C8 | A genuinely diagnostic comparator exists at `T_ctrl ≈ 1.259°` | **QUANTUM, sole finder** | Confirmed: worst-pair leak **0.988** vs 35.8 at 3.60° (**36× reduction**), at **2.36–2.40 Rayleigh widths**, 4.8 carrier cycles, well above Nyquist |
| C9 | `SE(R_q)` is a case resample of a deterministic 31-point design grid | MAT 4b, EM D3, QUANTUM D4, VISION D2 | Confirmed. Design-respecting residual bootstrap with step-1 refit: **1.60/1.77/1.87/1.85×** OLS, vs case 2.27/4.87/2.89/2.96× |
| C10 | Docket items 7, 8, 12 and four of item 13's bullets are unimplemented behind a "**all 15 implemented verbatim**" claim | MAT 4c/4d, EM D4, THERMO D3/D7, QUANTUM, VISION D9 | Confirmed against the docket text: `SE(ΔP)`, `dR_q/dψ̄`, `R_i/R_q`, item 8's calibration, item 12's SE column, and four item-13 bullets are all absent |
| C11 | "Idealization 6 discloses" is a dangling citation at three sites | MAT 4d, THERMO D7, VISION D9 | Confirmed: `NOTES.md` Idealization 6 is the no-new-FDTD idealization |
| C12 | `NOTES.md`'s "Idealizations unchanged from the Phase-1 proposal … still binding" is false | **PHOT D6, sole finder** | Confirmed by count: proposal has **9**, `NOTES.md` has **8**, dropping proposal items 4 (single-carrier model), 5 (~2.4 periods), 6 (`n_grid` adds no resolving power), 9 (a-priori power) |
| C13 | `phase4_results.md`'s caveat block drops the angular/polarization/scale scope entirely | **PHOT D7, sole finder** | Confirmed: proposal + `NOTES.md` Idealization 7 (2D TMz, single polarization, positive-θ branch, bench scale) appears in no deliverable caveat |
| C14 | Wrong-carrier gate failures misattributed to the p-clause | PHOT D3b, EM D6, THERMO D1, VISION D5 | Confirmed and **worse post-fix**: the **magnitude** clause fails at **all four** pairs; the p-clause fails only at C60–C70 |
| C15 | ΔP at the two wrong carriers is mis-normalised by the `T_mean` amplitude | EM D5, QUANTUM D9, VISION D3 | Confirmed: amp(`T_mean`)/amp(3.60°) = **4.71 / 6.18 / 7.75 / 5.62**; /amp(1.9608°) = 1.27/1.35/1.31/1.23 |
| C16 | Item 6's recalibrated carrier gate is near-vacuous and its own justification is unfixed | PHOT D9, QUANTUM D11, VISION D10 | Confirmed: admits **46–78%** of the `[1,4]°` search range and admits 1.9608° **at all four pairs** — the exact defect it was written to close |
| C17 | `n_resolved_holm10_*` counts the derived pair | EM D8, THERMO D8, QUANTUM D12, VISION D12 | Confirmed. Free-pair-only count = 2 restricted / 0 unrestricted. Outcome-inert |
| C18 | The derived pair retains gating privileges in four places | **THERMO D8, sole finder** | Confirmed by code reading (`resolved` on an unadjusted p; `resolved_pairs`; the ≥2 CONFIRM precondition; CONFIRM's own conjunction) |
| C19 | `dR_q/dψ̄ ≡ R_i` **exactly**, not to first order | **THERMO §4, sole finder** | Confirmed numerically: ratio **1.00000** at all four pairs. Item 7's "never computed" quantity was already in `results.json` under another name |
| C20 | The phase-invariant test `‖R‖ = √(R_i²+R_q²)` is null at every pair | **THERMO §4, sole finder** | Confirmed post-fix: raw p **0.0348 / 0.0714 / 0.1085 / 0.0638**; Holm over the free pairs **0.104 / 0.143 / 0.143**. Not one pair reaches even the relaxed 0.10 bar |
| C21 | "T21's 1.9608° fringe" over-specifies the contaminant | **QUANTUM §3, sole finder** | Confirmed by my own `L(T)`: leakage is **15–36 per unit amplitude across ~1.8°–5.0°**, peaking at 3.48–3.54°. The fringe (\|L\|≈28) is a named member of that band and is not its worst |
| C22 | Hand-typed prose figures do not reproduce (R4 recurrence) | all six | Confirmed — and **moot**: `phase4_results.md` is now wholly pre-fix (§3, RT-5) |
| C23 | "Resolves cleanly R²≈0.43–0.45" / "better-conditioned" is parity offered as superiority | PHOT D5, MAT 4e, THERMO D9, QUANTUM D10, VISION D13 | Confirmed: exp-071's per-config R² 0.4327/0.4483/0.4422/0.4337 vs this cycle's 0.4308–0.4451. Identical |
| C24 | Saturating-vs-linear is over-specified; any concave 2-parameter form wins on 4 points | MAT 1b, THERMO D6, VISION D11, EM §4 | Confirmed in substance; and VISION's sharper point holds — the published R² = 0.8328 belongs to the **refitted** slope 0.0024637, not to the `m₀` = 0.0025564 the sentence names |
| C25 | The contamination paragraph's "outcome-determining between REFUTED and NEITHER" is overstated | **QUANTUM D7 (first half), sole finder** | Confirmed by code trace: the REFUTE branch is gated behind `power_demonstrated = False`, so it emits `UNDERPOWERED_NOT_EVALUABLE`. **`REFUTED` was unreachable** |

### 2.2 CONFIRMED-BUT-RETIRED — true of the buggy run, dissolved by the fix

**R-a. "Red Team's 4/4 sign-agreement counter-evidence to VISION does not
reproduce."** (MAT #4, EM 2e, QUANTUM D8, VISION D6 — four seats.) True of
the pre-fix run (3/4). **Post-fix I measure 4/4**, with ratios +0.84 / +0.57 /
+1.72 / +0.72 — digit-for-digit Attack 10's own figures. The override of
VISION's sign-invariance gate stands on evidence that does reproduce. Do not
carry this finding into LOGBOOK.

**R-b. "The design's own p is 7–334× more significant at a carrier it calls
wrong."** (QUANTUM D6, VISION §2(iii), THERMO D5, PHOT D10 — four seats,
strong convergence, and **it does not survive the fix in the form
published**.) Pre-fix `p_fringe` = 0.0017 / 0.0415 / 0.5548 / 0.00015.
Post-fix, from the committed JSON: **0.6660 / 0.00055 / 0.0543 / 0.4202**
against true-carrier `p_restricted` of 0.0067 / 0.1042 / 0.0045 / 0.0171.
The claim **inverts at C40–C60 and C40–C80** — the two pairs on which all
four seats built it — and survives at **exactly one pair, C60–C70**
(0.00055 vs 0.1042, ~190×). The same correction applies to the
displaced-carrier `|R_q|` ratio: `|R_q(3.60°)|/|R_q(T_mean)|` = **0.91 /
3.06 / 0.51 / 1.42**, so the wrong carrier absorbs more ramp at **two** of
four pairs, not three. The qualitative conclusion (the ramp column is not
carrier-specific) survives; **every number offered for it must be
restated.** This is the single most important thing this audit prevents from
entering the permanent record, because four independent seats converged on
it and convergence is not correctness when all four read the same corrupted
JSON.

### 2.3 OVERRULED

**O-1. VISION D7 — OVERRULED, and it is the most instructive item in the
cycle.** VISION re-implemented steps 1–2 independently from the docket
specification, reproduced the *committed* numbers exactly, and concluded:
*"the officially committed numbers are the trustworthy ones and my Phase-2
table is the outlier."* It then retracted a correct finding. Its Phase-2
ΔP table (+0.0697 / +0.0085 / −0.0086 / +0.0668) is **exactly what the
corrected pipeline produces** (`results.json`: +0.06967 / +0.00850 /
−0.00861 / +0.06684). Its D7(c) claim that `ρ_c` is "now 0.0846, outside
the ≤0.05 band" likewise inverts: post-fix I compute **ρ_c = 0.0408**,
inside the band and matching its own Phase-2 value.

The general lesson VISION drew is correct — *"a ledger row saying VERIFIED
certifies that two implementations agreed, not that either matches the
committed code"* — but it applied it in the wrong direction. The sharper
form, which is this cycle's real methodological finding: **an independent
re-implementation that agrees with a buggy one is not a validation when both
are built from the same ambiguous specification.** The docket's phase
convention is that ambiguous surface; two implementers landed on the same
side of it. Only a **ground-truth recovery test** discriminates, and this is
the strongest argument in the entire record for making `G0-e` mandatory
machinery.

**O-2. QUANTUM D7 (second half) — OVERRULED on its inference.** QUANTUM
inferred from the Phase-2/Phase-4 discrepancy that *"Red Team's Phase-2
implementation almost certainly carried the same step-1→step-2 phase-handoff
bug"* and declared every ledger row downstream of that handoff — the
null-SD ratios, `|R_i/R_q|`, VISION's ΔP/z/ρ_c table, the 3.79% residual,
the 28.0 leak — untrustworthy. The opposite is the case, and §1.3 is the
proof: five Phase-2 ledger quantities reproduce post-fix to the quoted
digits and none reproduced pre-fix. **Every row QUANTUM condemned is
reinstated by the fix.** QUANTUM's factual observation — that the two
ledgers are irreconcilable and no deliverable says so — stands, and is the
process finding.

**O-3. MATERIALS §4b's residual-bootstrap *number* — OVERRULED; its
diagnosis upheld.** MATERIALS reports the design-respecting bootstrap
"collapses to at or below the OLS SE" (0.00471 / 0.00077). That construction
appears to omit the step-1 refit item 7 explicitly mandated. Perturbing both
the ramp residual **and** the common-mode carrier residual, and refitting the
free period and phase on every draw, I get **1.60 / 1.77 / 1.87 / 1.85×
OLS**, consistent with QUANTUM's 1.6–2.3× and VISION's 1.7–2.1×, and
inconsistent with EM's finding that holding the carrier fixed gives a
*larger* spread. Use 1.6–1.9×. The diagnosis — case resampling on a
deterministic design grid is the wrong bootstrap and the published inflation
measures the scheme, not the instrument — is confirmed by all four seats and
by me.

**O-4. PHOTONICS D5's measured second tone at 1.824–1.837° — NOT
OVERRULED, RULED UNQUOTABLE without a control.** It is a free-period search
over the same `[1,4]°` continuum, on a residual, on the same 31 points that
R5 and the Iteration-47 look-elsewhere addendum govern. Its physical reading
is plausible and my `L(T)` is consistent with it. But this program's own
precedent (exp-070's null-permutation result: a dense search finds a
plausible match regardless of ground truth) applies to it exactly. Run the
null-permutation control in the successor cycle before the number is quoted
anywhere. The same discipline does *not* bite MATERIALS'/THERMO's `L`-sweeps,
which are correctly stated as "any concave form wins," not as a measured
constant.

**O-5. MATERIALS D2's G40 cost revision (~31 calls vs PLAN's 62–93) —
ACCEPTED-CONDITIONAL, not adjudicated.** I did not verify the geometry
claim, and it is the single largest cost claim in the six reviews. The
Director must verify it against `experiments/065-.../design_geometry_output.txt`
before it re-ranks a queue. Its structural caveat — the 2×2 is **not
completable**, `config(80,0)` gives `clear_span_y = −40` — is a design fact
that must be pre-registered up front, not conceded at Phase 5.

**O-6. EM §1a's `A_q = 2a_cbar·tan χ` correction to item 5 — ACCEPTED,
DEFERRED.** Not re-derived here. Outcome-inert this cycle by EM's own
figure (`|A_q|/2a_cbar ≤ 0.065`, so `tan ≈ sin` to <0.5%). It must be fixed
in the docket table before any successor quotes a phase channel, because
the docket's own regime of interest (`χ ≈ 1.2 rad`) is where it becomes a
factor of 2.6.

---

## 3. Red Team's own attacks — findings no seat made

**RT-1 [inconsistency] — Docket item 8's mandated calibration is not merely
unimplemented; it is *vacuous*, and no re-run will produce it.** All six
seats reported "item 8's 3.79% telescoping residual is absent." I computed
it. At a **common** carrier the `R_q` telescoping residual is:

> `Σ R_q(adjacent) = +0.026182` · `R_q(C40–C80) = +0.026182` · residual =
> **0.0000%**, at machine precision.

It must be. G0-b proves `delta_C40–C80` is the **bit-exact** sum of the
three adjacent deltas (`max|residual| = 0.0`), and OLS on a **fixed** design
matrix is a linear functional of `y`. Therefore `R_q` telescopes
identically, at any common carrier, always. The docket's "3.79%" is not that
quantity, and the `ρ_c ≤ 0.05` band is not merely uncalibrated in print —
it is **uncalibratable by the route the docket specified**.

The constructive half: this tells us exactly what `ρ_c` measures. Since
closure is exact at a common carrier, `ρ_c = 0.0408` is **entirely** an
artifact of each pair choosing its own `T_mean`. Read that way it stops
being a "basis-stability check" and becomes this cycle's cleanest single
measurement of carrier sensitivity — a 4.1% closure failure produced by
nothing but the carrier choice, on a quantity that is algebraically exact
otherwise. That is a better statistic than the one item 8 asked for.

**RT-2 [inconsistency] — The design certifies 3.60° as carrier-*consistent*
at C40–C60 while simultaneously calling it the *wrong* carrier there.**
Item 6's recalibrated gate admits any `T_delta` with
`|T − T_mean|/T_mean ≤ q95`. At C40–C60, `q95 = 0.4715` and
`|3.60 − 2.4865|/2.4865 = 0.4478 ≤ 0.4715`. The same run contains a pair at
which the same carrier passes the consistency gate and fails the
wrong-carrier gate. Neither the docket nor any of the six seats states this.

**RT-3 [inconsistency] — Item 6's replacement gate fails its own stated
justification, and at one pair is *looser* than what it replaced.** Item 6
struck the imported `0.414` band because it "admits T21's declared-wrong
1.9608° carrier at all four pairs." The replacement admits 1.9608° at **all
four pairs** (`|Δ|/T` = 0.211/0.225/0.226/0.213 vs `q95` =
0.472/0.272/0.385/0.377), and at C40–C60 `q95 = 0.4715 > 0.414`. VISION
found the second half; I confirm both and add the consequence: the
contamination ruling's condition-2 certification that "the net effect of the
docket is strictly stricter" **does not hold at C40–C60** on this gate. That
certification is in a frozen pre-registration document.

**RT-4 [inconsistency] — Item 10's wrong-carrier gate is also scored against
a raw p where the docket froze a Holm-adjusted one, and nobody found it.**
Item 10: *"restricted-null **Holm-adjusted** p(T_wrong) > 0.01."* `run.py`:
`p_wrong_disp > 0.01`, raw. Direction matters and cuts the other way from
QUANTUM's C5: Holm can only raise p, so for a `> 0.01` clause the raw
reading is **stricter**, and this deviation is conservative and
outcome-inert (the magnitude clause fails at all four pairs regardless). I
record it because **two of the docket's gates were scored against
undisclosed departures from their own frozen thresholds, in opposite
directions**, and neither departure appears in any deliverable. That is a
pattern, not two typos.

**RT-5 — `phase4_results.md` is *wholly* superseded, not partially, and must
be republished rather than annotated.** Six seats each recommended
correcting subsets of it. The correct ruling is stronger. Every number in
the committed file is a pre-fix number, and the changes are not confined to
the coefficient tables: `R_q` flips sign at 3 of 4 pairs; the strain-flag
set changes F/T/F/T → **F/T/T/T**; the displaced-carrier gate goes from
1-of-4 passing to **0-of-4**; which injection pair cancels is relabelled;
the curvature coefficients change sign *and* magnitude (−1.058/−0.177/+0.025/−1.231
→ **+0.814/+0.232/+0.006/+0.996**); `p_fringe` changes at every pair and
**inverts** the four-seat claim in §2.2 R-b; `|R_q|/SE_bootstrap` at C40–C60
goes 0.94 → **2.158**, so even the published qualitative claim "no pair
clears 2" is now false. A reader handed an annotated version cannot tell
which figures survived. EM reached this conclusion independently and it is
correct.

**RT-6 — The two gates added *specifically* to make this cycle's negative
result trustworthy are each defective in a way that inverts what they
report, and both defects were computable with zero data before the run.**
Item 4's defect is a two-line algebraic identity (`yhat0 + resid0 ≡
delta_ab`). Item 10's defect is one division (0.746, not 1.5). Neither
needed the data, a surrogate, or an FDTD call. Both survived a 15-item Red
Team audit that authored them, a Director's Phase-3 independent re-check of
three overrides, and a Phase-4 write-up. QUANTUM stated this; it is the
checkpoint-relevant fact and I adopt it verbatim as my own.

**RT-7 [unfalsifiable] — the item-6 gate as it stands cannot fail.** It
admits 46–78% of the entire `[1,4]°` free-period search range while the
design's own noiseless forward model (Attack 4) predicts the statistic at
`≤ 0.001` and the observed values are 0.12–0.25, i.e. 120–250× the model
prediction. A gate calibrated to H₀ rather than to the model can be violated
by two orders of magnitude and print "✓". It is not passing; it is blind.
This is a live instance of my charter's second kill criterion and it must
not be carried into a successor pre-registration in this form.

---

## 4. Verdict on the Combined Verdict

**`NEITHER` STANDS.** Verified from the post-fix `results.json` and by
re-derivation, not accepted from the six reviews' concurrence.

1. **CONFIRM is foreclosed independently of every disputed gate.** `RESOLVED`
   requires restricted-null Holm-adjusted `p ≤ 0.01`. The minimum over all
   four pairs is **0.0135**. No pair reaches the bar, so **zero pairs
   `RESOLVED`** before the wrong-carrier gate, the carrier gate or the
   linearisation gate is consulted at all. The `CONFIRM_UNCERTIFIED`
   override never engages — verified inert, as forecast.
2. **REFUTE is blocked twice over.** It requires zero pairs at `p ≤ 0.10`
   under *both* nulls **and** `power_demonstrated`. The restricted null puts
   3 pairs (2 of the 3 free pairs) at `≤ 0.10` → blocked. And
   `power_demonstrated = False` under the as-coded injection, under the
   H₀-clean injection, and under the docket's own frozen Holm rule (0 of 3
   in every combination) → blocked again.
3. **P-072-3 = `NOT_EVALUABLE`** (needs all three adjacent pairs
   `RESOLVED`), **P-072-4 = `NEITHER`** (needs ≥2). Both follow mechanically.
4. **G0-a/b/c/d pass exactly** — grid identity bit-identical, telescoping
   residual `0.0`, column provenance `0.0`, `cond5 = 59.9–61.0`.

**Robustness to the *entire* fix set, not just the sign fix** — this is the
part I did not take on faith:

- Re-running the wrong-carrier gate at the corrected comparator
  `T_ctrl = 1.259°`: 3 of 4 pairs would pass. `RESOLVED` is still zero,
  because the `p ≤ 0.01` clause binds first at every pair.
- The design-respecting bootstrap (`|R_q|/SE` = 3.06/1.72/2.27/2.52) does
  not gate anything; `RESOLVED` runs on the surrogate p.
- The H₀-clean injection leaves `power_demonstrated = False`.
- The phase-invariant `‖R‖` test — the version of the hypothesis that does
  not condition on the carrier at all — is **weaker still**: Holm
  0.104/0.143/0.143, not one pair at the relaxed 0.10 bar.

Every correction on this docket moves the evidence away from `RESOLVED` or
leaves it unmoved. **There is no combination of the accepted fixes under
which this cycle's verdict changes.** `NEITHER` is not surviving by luck.

---

## 5. Same-shift mandatory-fix docket

**Tier 1 — must land this shift, before the cycle closes.** All zero-FDTD,
zero `lab/` diff. Every item is justified by an argument that references no
observed value, satisfying the contamination ruling's own condition 1, so
none of this re-opens the pre-registration question.

**T1-1. Restore the frozen basis, atomically.**
```python
# design_matrix — phase1_proposal.md:99, docket items 1 and 15
cols = [np.ones_like(x), np.cos(theta_c), -np.sin(theta_c),
        u * np.cos(theta_c), -u * np.sin(theta_c)]
if curvature:
    cols.append(u * u * (-np.sin(theta_c)))
# delta_P_obs (analyze_pair)
delta_P_obs = -(delta_f_obs / f_bar) * carrier["T_mean_deg"]
# dP_from
return -(df / fb) * Tdeg_val
# injection_recovery
df_pred = -dT_x / (T_x ** 2)
```
Keep `psi = -math.atan2(fit["b"], fit["a"])` exactly as applied. This is
provably neutral: the H₀ span is unchanged so `yhat0`/`resid0` are
bit-identical; `pinv5` row 4 flips sign so the `|R_q|` statistic and every
p-value are unchanged; `Rq_pred · X5[:,4]` is a product of two flipped signs
and is unchanged. **Acceptance test: ΔP, every p, every gate and the
Combined Verdict must be bit-comparable to the current run; only the signs
of `A_q`, `R_q`, `R_i` and the curvature coefficient may move.** After this,
item 5's `R_q = 2πa·Δf` and `A_i = a_B − a_A` read true as written.

**T1-2. Add `G0-e`, the ground-truth recovery gate, and run it before any
pair is scored.** Construct congruent synthetic pairs on the committed
31-point θ grid, `A = a·cos(2πu/T_A + ψ₀)`, `B = a·cos(2πu/T_B + ψ₀)`,
`T_A = 2.49°`, `ΔP ∈ {±0.005, ±0.01, ±0.02, ±0.04, ±0.08}`,
`ψ₀ ∈ {0, π/8, …, 15π/8}`; push each through the committed
`carrier_fit → design_matrix → delta_P_obs` chain; **HALT unless
`|ΔP_est/ΔP_true − 1| ≤ 0.02` at every cell.** Persist the worst cell to
`results.json` as `g0e.worst_abs_ratio_error`. Verified the current chain
passes at **0.00069** and the pre-fix chain fails, returning exactly
`−cos(2ψ₀)`. Add two cheap assertion tripwires alongside it, both from the
docket's own pre-registered values: `|R_i/R_q|` must reproduce
**0.48 / 2.81 / 1.69 / 1.10** to ±0.02, and `A_i` must match the directly
measured `a_B − a_A` within 10% **at pairs where `|a_B − a_A| ≥ 1e−4`**
(C40–C60 and C40–C80: measured 6.5% and 2.8%; the two narrow pairs have
`A_i` near zero and the ratio is not a usable tripwire there).

**T1-3. Rebuild the injection-recovery test on an H₀-clean base and score it
against the *frozen* rule.** Replace
```python
synthetic = yhat0 + resid0 + Rq_pred * X5[:, 4]      # == delta_ab + Rq_pred*col
```
with
```python
synthetic = delta_ab - R_q * X5[:, 4] + Rq_pred * X5[:, 4]
```
(equivalently `yhat0 + resid5 + Rq_pred·X5[:,4]`, which recovers `Rq_pred`
exactly by construction), and change `power_demonstrated` to test the
**Holm-adjusted** injection p at `≤ 0.01`, as docket item 4 froze. Verified:
as-coded p 0.0020/0.0071/0.0170, H₀-clean p 0.0109/0.0149/0.0075, Holm on
the H₀-clean set 0.0225/0.0225/0.0225. `power_demonstrated = False` in every
combination, so the Combined Verdict is untouched — **but the per-pair story
inverts and C70–C80 is the best-powered pair of the three.** The paragraph
in `phase4_results.md` crediting the precondition with "doing its job of
preventing exactly the REFUTE-fires-on-pure-power-failure defect" must be
**struck, not repaired**: it reached the safe branch for a reason unrelated
to power.

**T1-4. Replace the wrong-carrier comparator and correct the docket's false
constant.** `T_WRONG_DISPLACED = 3.60` → **`1.2591`**. Justification,
entirely data-free and computable before any run: 3.60° sits at
**0.702–0.746** Rayleigh widths (the docket asserts ≥1.5) and at **99.1–99.8%
of the global maximum** of the leakage function `|L(T)|` = 34.8–36.1 per unit
amplitude; 1.2591° gives a worst-pair leak of **0.988** — a **36×**
reduction — at **2.36–2.40** Rayleigh widths, with 4.8 carrier cycles in the
window, comfortably above Nyquist. Prefer it over PHOTONICS'/EM's 1.50°
(leak 6.25–7.98, 1.59–1.63 widths), which clears the displacement criterion
but not the leakage one. Correct the docket text: **≥1.5 Rayleigh widths
from a 2.4865° carrier requires `T ≤ 1.5331°` or `T ≥ 6.5765°`**, and the
`[1,4]°` search range admits only the lower branch. Also apply item 10's
frozen **Holm-adjusted** p-clause (RT-4), and report **both** clauses per
pair. Disclose the outcome: at 1.2591° the gate would pass at 3 of 4 pairs
(magnitude-only failure at C60–C70, whose `|R_q|` is the smallest in the
set); zero pairs still reach `RESOLVED`.

**T1-5. Replace the case-resampling bootstrap; report both.** Hold the
31-point θ design fixed; resample the 5-column fit residual for the ramp fit
and, independently, the common-mode carrier-fit residual, refitting the free
period and phase on the perturbed common mode every draw — which is what
item 7 actually specified. Verified: **1.60 / 1.77 / 1.87 / 1.85× OLS**,
against the case bootstrap's 2.27/4.87/2.89/2.96×. `|R_q|/SE` =
**3.06 / 1.72 / 2.27 / 2.52** — three of four pairs clear 2. Every sentence
built on "the bootstrap-propagated uncertainty is 4–5× the naive OLS
estimate" and "no pair's `|R_q|/SE_bootstrap` clears 2" must be struck. The
corrected statement is sharper and more honest: *the design-respecting
propagation is 1.6–1.9× OLS, three pairs clear 2σ on `R_q`, and none clears
the pre-registered significance bar* — which locates the failure in the null
calibration rather than in the point estimates.

**T1-6. Compute and publish the four never-computed docket quantities, and
retire item 8's vacuous calibration.**
- `dR_q/dψ̄` **is exactly `R_i`** (verified to 5 decimals at all four pairs;
  it is an algebraic identity of the rotation). Report it as such. No new
  computation is required — item 7's single missing diagnostic has been in
  `results.json` all along under another name, which is why nobody noticed
  it was missing and why nobody used it to catch the sign bug.
- `R_i/R_q` as an explicit field: magnitudes **0.478 / 2.811 / 1.687 /
  1.099**, matching item 11's pre-registered values exactly.
- `SE(ΔP) = |ΔP/R_q|·SE(R_q)` at all four carriers. At `T_mean`, with the
  T1-5 bootstrap: **0.0228° / 0.0050° / 0.0038° / 0.0265°** (with the case
  bootstrap it would read 0.0323/0.0137/0.0059/0.0425). Against a total
  measured C40→C80 period span of 0.093°, this is the column that makes the
  ΔP table interpretable without narrative.
- **Item 8 must be retired, not implemented.** See RT-1: the residual it
  mandates is **0.0000% exactly, always**, by G0-b plus linearity of OLS on
  a fixed design. Replace item 8's sentence with: *"`ρ_c` is not a
  basis-stability statistic. At a common carrier the closure is exact by
  construction (verified 0.0000%); `ρ_c = 0.0408` measures only the per-pair
  carrier choice, and is therefore this cycle's cleanest single measurement
  of carrier sensitivity."*

**T1-7. Fix the ΔP-by-carrier normalisation.** `at_carrier()` must return
its own amplitude and `dP_wrong`/`dP_fringe` must use it, as `dP_Tdelta`
already correctly does. Measured factors: amp(`T_mean`)/amp(3.60°) =
**4.71 / 6.18 / 7.75 / 5.62**; /amp(1.9608°) = **1.27 / 1.35 / 1.31 / 1.23**.
Signs are unaffected; the two wrong-carrier columns are understated by those
factors.

**T1-8. Publish the withheld half of item 10's mandatory disclosure — in its
post-fix form only.** `R_q` and restricted-null p at 1.9608° and at the
comparator are in `results.json` and in no deliverable. **Post-fix**:
`p_fringe` = 0.6660 / 0.00055 / 0.0543 / 0.4202 against true-carrier
`p_restricted` 0.0067 / 0.1042 / 0.0045 / 0.0171; `|R_q(3.60°)|/|R_q(T_mean)|`
= 0.91 / 3.06 / 0.51 / 1.42. **The pre-fix version of this table — on which
four seats independently built a 7–334× claim — must not enter LOGBOOK.**
The surviving statement is: *at C60–C70 the design's own significance test is
~190× stronger at a carrier it declares wrong than at the carrier it gates
on, and the ramp coefficient at the wrong carrier exceeds the right one at
two of four pairs.*

**T1-9. Strip the derived pair from the REFUTE-blocking counter only.**
`n_resolved_holm10_*` must run over the three algebraically-free pairs, per
item 14's own logic. Verified outcome-inert: 2 restricted / 0 unrestricted,
branch unchanged. **Do not** touch the deeper items this shift (C40–C80
gating `RESOLVED` on an unadjusted p; entering `resolved_pairs` for
P-072-4's sign-reversal clause and the ≥2 CONFIRM precondition; standing in
CONFIRM's own conjunction). Those are frozen pre-registration; they go to
the successor's Phase 1 as a required design change.

**T1-10. Republish `phase4_results.md` and correct `NOTES.md`.** Not
annotate — republish (RT-5). Required prose changes:
- **a.** Strike the Bottom Line sentence *"the one pair whose
  displaced-carrier control passes (C70–C80) is exactly the pair whose
  significance and injection-recovery power both fail."* Post-fix, **zero**
  pairs pass that control and C70–C80 is the best-powered pair. It has no
  referent.
- **b.** Replace "T21's 1.9608° fringe" as *the* contaminant with the
  data-free general statement re-derived above: *`R_q` is non-identifiable
  against essentially any periodic contributor from ~1.8° to ~5.0°, at 15–36
  per unit amplitude, peaking at 3.48–3.54°; the 1.9608° fringe (|L| ≈ 28)
  is one named member of that band and is not its worst.* The honest
  sentence is QUANTUM's: **the single-carrier-plus-ramp model is misspecified
  on this window, the ramp column absorbs the misspecification, and with 2.4
  carrier cycles across 31 points there is no way to separate absorbed
  misspecification from a genuine `Δf`.**
- **c.** Restate the wrong-carrier gate failures **by clause**: the magnitude
  clause fails at all four pairs (0.02511 vs 0.01377; 0.01081 vs 0.00176;
  0.00182 vs 0.00177; 0.03716 vs 0.01309), the p-clause only at C60–C70.
- **d.** Correct the contamination paragraph in all four locations
  (`run.py` docstring, `phase3_synthesis.md`, `NOTES.md`,
  `phase4_results.md`): the null choice was outcome-determining between
  **`UNDERPOWERED_NOT_EVALUABLE` and `NEITHER`**, not between `REFUTED` and
  `NEITHER` — `REFUTED` was unreachable, because the REFUTE branch sits
  behind `power_demonstrated = False`. The four binding conditions were right
  ex ante and are not relaxed; only the factual claim is corrected.
- **e.** Restore proposal Idealizations **4** (single-carrier model), **5**
  (~2.4 periods; edge effects on the ramp coefficient are real), **6**
  (`n_grid=3000` adds no resolving power), **9** (a-priori power caveat) to
  `NOTES.md`, or stop claiming the list is "unchanged from the Phase-1
  proposal … still binding." Dropping item 4 is what allowed "the carrier
  itself resolves cleanly, R²≈0.43–0.45" into the Bottom Line against a
  frozen limitation citing the identical numbers.
- **f.** Repair the dangling *"Idealization 6 discloses"* citation at all
  three sites (`phase4_results.md`, `run.py:64`, `run.py:223`) and put the
  C70/C80 order-reversal sentence where item 13 mandated it.
- **g.** Write the four never-written item-13 bullets: P-072-6 supplies the
  confounded arm of Iteration-49 queue item 2 and does not substitute for it;
  name queue item 4 (two-tone joint fit) and re-defer it with a stated
  reason; "genuine saturation is an equally live reading of the same node
  collision"; and restore Idealization 7's scope (**2D TMz, single
  polarization, positive-θ branch 36°–42°, bench scale `R_OUT=78`**) to
  `phase4_results.md`'s caveat block, which currently says only "600nm only."
- **h.** Restore the `C_empty`-is-not-a-Michelson/Weber-contrast clause to
  `phase4_results.md`'s caveats and inline it at the Bottom Line's own
  `ptp/mean = 16.2` use site.
- **i.** Saturating-vs-linear: downgrade *"MATERIALS' and THERMODYNAMICS'
  finding survives the tie-break"* to **"the ranking is robust to the
  tie-break and to the choice of `L` over 0.02–0.30, on four points against
  two parameters; the comparison discriminates curvature, not functional form
  or decay constant."** Attach the unphysical extrapolation
  `P(ABSORB=0) = 0.46°` — below the free-period search's own 1.0° floor.
  Replace "engine-derived" with **"engine-motivated; the scale constant is
  `_damping`'s depth-averaged per-step exponent, imported from an
  amplitude-attenuation context to a phase observable with no stated causal
  relation"** (EM's and MATERIALS' wording, both correct). Correct VISION's
  D11: the published `R² = 0.8328` belongs to the **refitted** slope
  0.0024637, not to the `m₀ = 0.0025564` the sentence names — the exact
  Attack-5 defect, reproduced inside the disclosure written to prevent it.
  Use "graded damping mask," not "graded absorber," throughout.
- **j.** Correct "better-conditioned than the absolute-period route" to name
  the quantity that actually improved (`cond5 ≈ 60`) and strike "resolves
  cleanly" for R² ≈ 0.43–0.45.
- **k.** Add THERMO's phase-invariant result as disclosure (T2-2 below).
- **l.** State plainly, in the re-issue and in `phase3_synthesis.md`, that
  the "all 15 docket items implemented verbatim, ZERO items un-adopted"
  claim was **false as written** — items 1, 4, 7, 8, 10, 12, 13 and 15 each
  departed from the frozen specification — and that the Combined Verdict was
  **verified to survive** the correction. Saying so protects the finding;
  leaving it protects nothing.

**Tier 2 — deferred to Iteration 50, with reasons.**

- **T2-1. VISION's reinstated sign-invariance admissibility condition** over
  the gate-admitted set `{T_mean, T_delta, any ≥1-Rayleigh-displaced carrier
  inside q95}`. *Reason: it is a new gate. Adding a gate to a frozen
  pre-registration after the numbers are known is precisely what this
  cycle's own contamination ruling forbids.* It is a good proposal and it
  belongs in the successor's Phase 1.
- **T2-2. THERMO's ψ-marginalized gating statistic.** *Reason: `‖R‖` tests a
  different hypothesis (H₀: `R_i = R_q = 0`), not a corrected version of the
  pre-registered one.* **But publish the invariant now as disclosure** —
  verified post-fix (raw p 0.0348/0.0714/0.1085/0.0638; Holm over the free
  pairs 0.104/0.143/0.143) and, because `‖R‖` is rotation-invariant, it is
  the **one analysis in the entire Phase-5 set the sign bug never touched**.
  It is free, it required no re-run, and it sharpens the finding.
- **T2-3. QUANTUM's sign-flip / residual-permutation null** replacing the
  phase-randomised H₀-residual null (which leaves the signal in the null).
  *Reason: changes the gating null.*
- **T2-4. EM's `A_q = 2a_cbar·tan χ`** correction to item 5's table.
  *Reason: outcome-inert here; must be fixed before any successor quotes a
  phase channel.*
- **T2-5. PHOTONICS' second-tone measurement (1.824–1.837°).** *Reason: R5 /
  Iteration-47 look-elsewhere discipline — it needs a null-permutation
  control before it is quoted anywhere.*
- **T2-6. MATERIALS' G40 cost revision.** *Reason: Director must verify the
  geometry claim against exp-065's committed output before it re-ranks a
  queue.*
- **T2-7. Quote no curvature coefficient** until it is re-run in the
  restored basis. Its sign convention was opposite to item 15's **and** its
  values changed under the fix.

---

## 6. Checkpoint determination — all five criteria, explicit

**Criterion 1 (a configuration passes all constraint metrics): DOES NOT
FIRE.** No constraint metric was scored this cycle; T1 escape route is N/A
(`t1_escape_route: null`); desk-only re-analysis of `C_empty` field ratios.

**Criterion 2 (a proven boundary): DOES NOT FIRE.** Nothing here closes a
mechanism class. QUANTUM's `L(T)` and EM's Cramér–Rao pricing are candidate
bounds for a successor to establish, not a boundary proven this cycle.

**Criterion 3 (engine physics beyond validated bench classes): DOES NOT
FIRE.** Zero FDTD calls, zero `lab/` diff — verified.

**Criterion 5 (two consecutive non-advancing iterations): DOES NOT FIRE.**
Iteration 48 delivered a genuine result and Iteration 49 delivers two: the
measured reason for the resolution failure, and the estimator-integrity
finding itself.

### Criterion 4 (Red Team flags program-integrity drift): **FIRES.**

I considered ruling it non-firing on the ground that the mechanism worked —
the bug was found at Phase 5, by the phase designed to find it, before
anything false entered `LOGBOOK.md`. That is the strongest available
argument and it is not sufficient, for four reasons, weighed against this
program's own precedents.

**1. This is the firing shape, by the program's own stated test.** Iteration
45 drew the line explicitly: defects *"found-and-fixed by the cycle's own
process before close"* (Iterations 19/23/38/42/43) do **not** fire; defects
that *"took blind Phase-5 seats plus the final audit to surface"*
(Iterations 37/39/40/44/45) **do**. This is unambiguously the second shape.
Phases 1, 2, 3 and 4 all passed a defect that made every published
coefficient a rotation by a nuisance parameter; it took **three of six blind
seats, using three different methods**, plus a Director self-re-derivation,
plus this audit.

**2. A written verification claim in a frozen pre-registration document is
false.** `phase3_synthesis.md`: *"All 15 docket items are implemented in
`run.py`, verbatim to the audit's specification"* and *"ZERO items
un-adopted."* Verified false on **eight** counts — items 1 and 15 (basis
sign), 4 (raw p where Holm was frozen, in the loose direction), 7 (three of
four mandated quantities absent), 8 (a calibration that is mathematically
vacuous), 10 (a false Rayleigh constant, and raw p where Holm was frozen),
12 (no SE column), 13 (four bullets never written). PANEL.md's criterion 4
names *unfalsifiable claims* and *program-integrity drift*; a
verification claim that does not hold, inside the document that freezes the
design, is the centre of that class, not its edge.

**3. Aggravation, on this program's own Iteration-36 precedent.** The
**same function**, `_amp_phase_at`, carried a Director-caught, honestly
disclosed bug at Phase 3 — and the diagnostic that found it (comparing the
tool's outputs against independently computed Phase-2 values) was **retired
after the patch instead of being re-run as an acceptance test**. The second
half of the same defect then shipped, in the same function, in the same
cycle. Iteration 36's ruling applies verbatim: a recurrence inside the very
cycle whose fix was written to close it *"aggravates rather than
mitigates."* The generalisable lesson, which EM stated best and which is
adopted here as this cycle's contribution to house discipline: **a
cross-check that finds a bug must be re-run as an acceptance test after the
fix, not retired once it has served.** That is exactly what `G0-e`
institutionalises.

**4. Two independent supporting instances.** (a) R4 recurrence — three
hand-typed headline figures that do not reproduce from the committed
function, inside a cycle that adopted an R4-motivated `m₀` provenance fix;
the Iteration-26 hardened tripwire on this pattern is on the record. (b)
Docket item 10's "≥1.5 Rayleigh widths" — a **false constant** that entered
a frozen pre-registration, adopted verbatim from a seat by Red Team without
recomputation, and re-verified by the Director for the *other* number in the
same item while the wrong one went unchecked.

**Mitigating, and recorded in full because it is real.** The bug was found
at Phase 5 before anything false reached `LOGBOOK.md`. The Director
independently re-derived it from scratch rather than accepting three
converging reviews on faith — the correct response, and the reason this
audit could verify a fix rather than argue about one. The Combined Verdict
is unaffected and it is verified robust to the entire fix set. The
arithmetic-integrity gates the cycle *did* build (G0-a/b/c/d) all worked
exactly as designed. And the design Red Team produced at Phase 2 is
architecturally sound; the failure is in execution and in two of its own
authored gates, not in its structure.

**Ruled a notification, not a pause** — this program's unbroken precedent,
zero exceptions in this record. No engine physics is implicated, zero
`lab/` diff, no committed FDTD number is wrong, the verdict stands, and the
remedy (the Tier-1 docket plus `G0-e`) is actionable without halting any
thread. Marsh is notified via the LOGBOOK entry and `SESSION_LOG.md`.

**One new pre-committed tripwire, adopted here on the Iteration-26 and
Iteration-35 model.** `G0-e` — a synthetic ground-truth recovery gate — is
now **mandatory machinery for any cycle that fits a carrier-conditioned or
phase-conditioned coefficient**. A cycle that ships such an estimator
without one fires criterion 4 automatically, no further deliberation. The
justification is measured, not rhetorical: the defect this cycle shipped was
invisible to `cond5`, to R², to the residuals, to the fitted values, to four
phases of review, and to an independent re-implementation built from the
same specification (§2.3 O-1) — and it was detectable in **under one second**
by a test that asks the estimator to recover a number it was given.

---

## 7. For the Director's LOGBOOK entry

### 7.1 Final headline finding of exp-072

**Combined Verdict: `NEITHER`** — zero of four `ABSORB` pairs `RESOLVED`,
unchanged from the Phase-4 branch trace and now verified robust to the full
correction set rather than only to the sign fix.

**The substantive reason, post-all-fixes** — and it is sharper than the one
the cycle was about to publish:

> The differential/beat estimator's target coefficient `R_q` is the
> projection of `delta_AB(θ)` onto an axis fixed by a **nuisance
> parameter** — the common-mode carrier phase `ψ̄`. The sensitivity is exact
> and free: **`dR_q/dψ̄ ≡ R_i`**, with `|R_i| ≥ |R_q|` at three of four
> pairs, and the carrier rotation that annihilates `R_q` entirely —
> `δ₀ = arctan(−R_q/R_i)` = **1.125 / 0.342 / −0.535 / 0.738 rad**, i.e.
> **0.33σ_ψ to 1.02σ_ψ** against a bootstrap `σ_ψ ≈ 1.03–1.10 rad` — is
> inside the carrier's own uncertainty at every pair. The
> **phase-invariant** version of the same test,
> `‖R‖ = √(R_i² + R_q²)`, is null everywhere (Holm 0.104 / 0.143 / 0.143 over
> the three algebraically-free pairs). The cause is the window, not the
> noise floor: 36°–42° supplies `X = ptp(sin θ) = 0.08135`, a Rayleigh width
> of `1/X = 12.29`, and **2.4 carrier cycles across 31 points**, at which
> `R_q` is non-identifiable not specifically against T21's 1.9608° fringe
> but against **essentially any periodic contributor from ~1.8° to ~5.0°**
> (leakage 15–36 per unit amplitude, peaking at 3.48–3.54°). The
> single-carrier-plus-ramp model is misspecified on this window, the ramp
> column absorbs the misspecification, and at 2.4 cycles absorbed
> misspecification is indistinguishable from a genuine `Δf`. That is a
> stronger, more general and more falsifiable statement than "T21's fringe
> contaminates it," and it is what the numbers support.

**The estimator-integrity finding, which must be recorded in the same entry
and not softened:**

> The cycle's first official run was executed on a **mis-rotated basis**: a
> carrier-phase sign error in the step-1→step-2 handoff (`_amp_phase_at`)
> made every published coefficient a rotation of the intended one by `2ψ̄`,
> mixing `R_i` into `R_q` at first order. A second, partially compensating
> deviation from the frozen basis kept the published ΔP signs plausible at
> three of four pairs — an accident of where this window's carrier phase
> happens to sit. The defect was invisible to every gate in the design
> (`cond5`, R², residuals, fitted values are all rotation-invariant) and to
> an independent Phase-5 re-implementation built from the same
> specification. Found at Phase 5 by **three of six blind seats using three
> different methods**, independently re-derived and patched by the Director,
> and verified in this audit against a synthetic ground-truth sweep
> (recovered/true ΔP = **1.0000 ± 0.0007** over 16 carrier phases × 7 effect
> sizes; the pre-fix chain returns exactly `−cos(2ψ₀)`) and against **five
> Phase-2 ledger quantities that reproduce post-fix and did not pre-fix**.
> The Combined Verdict was unaffected. `phase4_results.md`'s number tables
> are **wholly superseded and republished**, not annotated. **CHECKPOINT
> criterion 4 fires** (notification, not a pause).

Two further sentences the entry should carry, because both are corrections
to claims that four or more seats converged on and that do **not** survive
the fix, and convergence is not correctness when every seat reads the same
corrupted JSON:

- Red Team's Attack-10 counter-evidence to VISION **does** reproduce
  post-fix: ΔP sign agreement with the `n_grid=3000` absolute-period
  differences is **4/4** (ratios +0.84/+0.57/+1.72/+0.72), not 3/4.
- The "the design's own p is 7–334× more significant at a carrier it calls
  wrong" claim **inverts at both wide pairs** post-fix and survives at
  **one** pair only (C60–C70, ~190×).

### 7.2 Ranked queue for Iteration 50 (synthesised, not vote-averaged)

All six seats rank a corrected zero-FDTD re-issue first (PHOT #1, MAT D1,
EM #1, THERMO #2, QUANTUM #1, VISION #2) — full convergence, no dissent.
They split three ways below that: widen the window (PHOT #3, EM #3, VISION
#1), decorrelate `PAD` (MAT D2, THERMO #1, VISION #3), or model the
contaminant (PHOT #2, QUANTUM #3) — with EM arguing the differential route
should be **closed** on a computed bound instead. Synthesis:

**1. `exp-073` — the corrected re-issue, behind `G0-e`. Zero FDTD.**
Unanimous. This is the Tier-1 docket executed as a **clean, uncontaminated
pre-registration**, which the contamination ruling's own condition 3
explicitly contemplates. Every fix in it is justified by a data-free
argument, so it retires the contamination question rather than re-opening
it. Nothing downstream of step 2 in this thread is readable until it lands.

**2. Price the window before spending in it — a data-free feasibility
calculation, then the window decision. Zero FDTD.** EM's conditioning /
Cramér–Rao pricing (the 9-column two-tone design gives `cond = 529` and a
**6.0× SE inflation** on `R_q`, against corrected `|R_q|/SE_OLS` of
4.9/3.0/4.3/4.7) and QUANTUM's `L(T)` leakage budget are both computable
with zero new data, and between them they decide whether 36°–42° can ever
support a carrier-conditioned discriminator. Rank this above both FDTD
builds because it is free and it determines which of them is worth 31–156
calls. Adopt QUANTUM's standing requirement: *any new FDTD spend must
report `max|L|` over the admitted carrier band for its proposed window and
pre-register a target.* If the calculation says this window cannot reach 2σ
on `R_q` at this SNR — as EM's number already suggests — **publish that as
the closing bound on the differential route in this window.** A computed
bound is a real result and is worth more than a fourth `NEITHER`.

**3. Then one FDTD build, chosen by what step 2 says is buyable.** If both
are, **run G40 first**:
- **G40 / `PAD` decorrelation (~31 calls if MATERIALS' geometry claim
  verifies; PLAN currently says 62–93).** Cheapest confound relief on the
  board, and it buys two clean contrasts (G40 vs C80 = pure `ABSORB` at
  fixed `PAD`; G40 vs C40 = pure `PAD` at fixed `ABSORB`). It relieves the
  caveat that binds **every** deliverable in this series under **every**
  verdict, and its readout can be the **phase-invariant amplitude channel**
  `√(A_i²+A_q²)/a` — this cycle's baseline **0.161 / 0.041 / 0.020 / 0.166**
  — which conditions on no carrier at all and is therefore not hostage to
  the resolution problem. Pre-register the structural limit up front: the
  2×2 is **not completable** (`config(80,0)` gives `clear_span_y = −40`), so
  the main effects are identifiable only under additivity and the
  interaction is not identifiable at all.
- **Window extension to `θ_max ≈ 46°`** (EM: 40 calls, C40/C80 two-config;
  VISION: 64 calls for 1.0 Rayleigh across four configs, 156 for 1.5). The
  only change that attacks the cause rather than a symptom. **VISION's
  window-discipline constraint now generalises: 36°–42° is retired for *any*
  carrier-conditioned T28 estimator, differential and two-tone included, not
  only absolute-period ones.** Binding precondition, adopted from EM and
  VISION jointly: the fit is a sinusoid in `x = sin θ` and `cos θ` varies
  8.1% across 36–42° and 14.1% across 36–46°, so the extension must promote
  the curvature column from disclosed to fitted, or pre-register an
  envelope-agreement check across sub-windows — otherwise it trades a
  resolution failure for a misspecification failure, and `R_i` is already
  the larger coefficient at three of four pairs.

**4. Explicitly subordinate.** Queue item 3 (mask-functional-form ablation)
is strong, orthogonal and carries **no `PAD` confound by construction** —
MATERIALS is right that it buys a new axis rather than a fifth point on an
under-determined curve — but run it **inside** the widened window once one
exists. Queue item 4's two-tone joint fit stays **deferred with a stated
reason, in writing this time**: EM has priced it (cannot reach 2σ at this
SNR) and VISION's R5 argument bites (a flexible model on under-resolved data
returns a confident, meaningless answer); it becomes evaluable only if step 2
says the window supports it. Queue item 4's `ABSORB ≈ 120` FDTD half is
separately weak — THERMO's own saturating model puts the discrimination at
`z ≈ 1.4–1.8`, and MATERIALS' covariate observation (`ABSORB/λ` is integer
at 40/60/80 and would be integer again at 120) means it **preserves** an
uncontrolled covariate rather than breaking it.

**Two standing rules adopted this cycle:** `G0-e` (§6, criterion-4 tripwire)
and QUANTUM's window-leakage budget (§7.2 item 2).

---

## 8. Closing assessment

The design Red Team wrote at Phase 2 was the best-audited instrument this
program has built, and two of the gates it added specifically to make a
negative result trustworthy were each defective in a way that **inverted
what they reported** — both computable with zero data, before the run. That
is the cycle in one sentence, and it is why the Phase-5 mechanism exists.

The verdict is right, the reason for it is now better than the one the cycle
was about to publish, and every number underneath it has to be republished.
`NEITHER` stands. Checkpoint criterion 4 fires. The docket is ten items and
it is all arithmetic.
