# THERMODYNAMICS — Phase 5 Review · Panel Iteration 49 · exp-072 (T28 differential/beat fit)

*Fresh sub-agent, THERMODYNAMICS charter (PANEL.md: where absorbed energy goes; owns the per-proposal energy sidecar, analytic and labeled as such). Blind to all other Phase-5 reviews this cycle. Every number below was re-executed against `run.py` and `results.json` in an independent scratch implementation; nothing is taken from prose. Where I contradict `phase4_results.md` I give the reproduction.*

---

## 0. Method

I re-ran: the Holm arithmetic; the four gates' clause-by-clause decomposition; the injection-recovery construction; the saturating-vs-linear fit at seven decay constants; the bootstrap at both `n_grid=400` and `n_grid=3000`; a carrier-phase sensitivity derivative; a 20,000-surrogate test of the phase-invariant ramp modulus; and a five-seed stability sweep on the power test. Total desk cost ~4 min. No `lab/` file, no repo file, and no committed artifact was modified.

**Verdict on the cycle: PARTIAL.** The design is the best-audited instrument this program has built, the Combined Verdict `NEITHER` is correct as pre-registered and I do not ask that it move, and the two findings I raised in Phase 2 were adopted honestly. But `phase4_results.md` contains two arithmetic errors, one misattributed gate failure repeated at two pairs, one power statement that is an artifact of its own construction, three mandated quantities that were never computed, four mandated disclosure sentences that were never written, and one cross-reference to a caveat that does not exist at the cited location. None of these moves the Combined Verdict. Two of them move the *reason* for it, which this cycle declared to be its substantive finding.

---

## 1. My two Phase-2 findings — implementation status

**Finding 1 (P-072-4's smuggled linearity; Red Team Attacks 5–6, docket item 9): IMPLEMENTED CORRECTLY.** `run.py` lines 532–544 contain no rate-window clause at all — the `[m₀/10, 10m₀]` band is absent from the code, and `sign_reversal` is the only gating rate clause, exactly as the docket specified. `m₀` is read at runtime (line 113) from `d071["trend"]["linear_fit"]["slope"]`; no slope constant is typed anywhere in the file. I reproduce `m0_committed = 0.0025563909774436134`, matching the committed exp-071 JSON.

The saturating-vs-linear re-run at this cycle's own `n_grid=3000` reproduces exactly: linear R² = 0.8328, saturating (L=0.075 fixed) R² = 0.9901, on periods 2.437479 / 2.520507 / 2.535512 / 2.530510. Per-cell rates at that resolution are **+0.004151 / +0.001501 / −0.000500 °/cell**, confirming Red Team's Attack-6 correction (the C70→C80 rate is negative, not zero) against my own Phase-2 figures, which were taken from the `n_grid=400` data.

*Strengthening my own finding, and then walking part of it back:* I refit the saturating family at L ∈ {0.02, 0.04, 0.05, 0.06, 0.075, 0.09, 0.10, 0.15, 0.20, 0.30}. R² is **0.909–0.994 across the entire range** versus linear's 0.833. So the ranking does not depend on the engine-derived L=0.075 — a robustness check Phase 4 did not run, and a genuine strengthening. But the honest counterweight is larger: this is two 2-parameter models on four points (2 residual df), the saturating fit's largest residual (−0.0060° at C80) is **larger than the entire measured C70→C80 step (−0.0050°)**, and both models are monotone while the data are not. Red Team granted my finding on the *narrow* ground that `m₀` is an untrustworthy anchor, explicitly "not because saturation is established." `phase4_results.md` line 166 upgrades that to "MATERIALS' and THERMODYNAMICS' finding survives the tie-break." **That is a half-step of epistemic inflation on my own contribution and I flag it against my own interest** (defect D6 below).

**Finding 2 (the caveat rule bound only CONFIRM; docket item 13, bullet 1): IMPLEMENTED IN SUBSTANCE, HALF THE MANDATED SENTENCE DROPPED.** `NOTES.md` Idealization 2 carries the extension verbatim and attributes it correctly ("This binds every deliverable — P-072-1 and the disclosed P-072-6 channels included — under EVERY verdict, not only CONFIRM"). `phase4_results.md`'s caveat opens weaker ("Any *future* CONFIRM-shaped language…") but the following sentence repairs it ("This binds every table above, under every verdict, not only a hypothetical CONFIRM"). Accepted.

**But the second half of that same docket bullet — "state that P-072-6 supplies the confounded arm of Iteration-49 queue item 2 and does not substitute for it" — appears in no deliverable.** Grep across `NOTES.md`, `phase3_synthesis.md`, `phase4_results.md`, and `run.py` returns zero hits for "queue item 2." This is precisely the deferral-by-omission failure mode my Phase-2 §3 invoked (house precedent Iteration 5, exp-027), reproduced inside the fix that was adopted to close it. Defect D7.

---

## 2. Energy sidecar — N/A re-confirmed, by argument

**Clean.** A full-text grep of `NOTES.md`, `phase4_results.md`, and `run.py` for `absorbed power`, `temperature`, `thermal`, `emissiv`, `re-radiat`, `sidecar`, `watt`, `kelvin`, `joule` returns exactly two hits, and both are the N/A declarations themselves (`NOTES.md` Idealization 8; `phase4_results.md` caveats, line 219). No absorbed-power number, no ΔT, no emission band, no detectability statement is produced or implied anywhere in the cycle. The house-precedent requirement (deferral by argument, not by omission) is satisfied at both locations.

The argument, restated so it is on the record and not merely asserted: `C_empty` is an **empty-scene** field ratio — there is no article in the domain, so there is no dissipative volume over which to integrate a Poynting divergence, and therefore no absorbed power exists to convert into a temperature rise, an emission band, or a detectability figure. `ABSORB` is a numerical boundary-condition parameter (Idealization 3), not a lossy medium with a defined loss tangent. The chain absorbed power → ΔT → emission band → detectability has no first link this cycle. The sidecar is N/A by construction, not by scheduling.

**One wording risk I am raising against my own Phase-2 framing.** `phase4_results.md` describes the saturating comparator as "an engine-derived saturating model (decay fixed at `_damping`'s own 0.075/cell)," and my own Phase-2 attack framed the underlying physics as "boundary power-return." A reader can take "engine-derived … 0.075/cell" as a measured absorbed-power fraction. It is not: it is the damping profile's own numerical per-cell attenuation constant, chosen rather than fitted. A future cycle carrying this model forward should add the half-sentence. This is the only place in the cycle where anything thermal-shaped is within one reading of the text, and it is my own contribution that put it there.

---

## 3. Defects

### D1 — SUBSTANTIVE. The wrong-carrier gate failure is misattributed at two of three failing pairs, and the true failure mode is far more damaging than the one reported.

The gate is `(|R_q(3.60°)| ≤ ½|R_q(T_mean)|) AND (p(3.60°) > 0.01)`. Decomposed from `results.json`:

| Pair | \|R_q(3.60°)\| | ½·\|R_q(T_mean)\| | amplitude clause | p(3.60°) | p clause | phase4 says |
|---|---|---|---|---|---|---|
| C40–C60 | 0.02036 | 0.01139 | **FAIL** | 0.0195 | **pass** | "`p=0.0195` — fails" |
| C60–C70 | 0.00907 | 0.00042 | **FAIL** | 0.0071 | FAIL | "`p=0.0071` — fails" |
| C70–C80 | 0.00010 | 0.00296 | pass | 0.7647 | pass | ✓ (only pair to pass) |
| C40–C80 | 0.03029 | 0.00744 | **FAIL** | 0.0125 | **pass** | "`p=0.0125` — fails" |

At C40–C60 and C40–C80 the p-clause **passes** (0.0195 and 0.0125 are both > 0.01). The gate fails on amplitude, and `phase4_results.md` names the p-value as the cause at both.

The substantive point is what the amplitude clause actually found: **at a carrier displaced ≥1.5 Rayleigh widths from the true one, the estimator returns a ramp coefficient that is 0.89×, 10.7×, and 2.04× the coefficient at the true carrier.** The design's own pre-registered control — chosen specifically because 1.9608° was too close to be diagnostic — shows `R_q` is not carrier-specific at all at three of four pairs. That is a *stronger* statement than the Bottom Line's diagnosis (non-identifiability against a fringe sitting 0.65 Rayleigh widths away), and it is the one the data supports. The write-up has the number in a table and never says it.

### D2 — SUBSTANTIVE. The injection-recovery "power test" is not a power test; `power_demonstrated = False` is an artifact, and the failing pair inverts once it is corrected.

`run.py` line 413: `synthetic = yhat0 + resid0 + Rq_pred * X5[:,4]`. But `yhat0 + resid0 ≡ delta_ab` identically. So the test injects the predicted ramp **on top of the observed one**, and measures the detectability of `R_q^obs + R_q^pred`, not of `R_q^pred`. Verified to full precision at all three pairs:

| Pair | `R_q` obs | `R_q` pred | sum | `Rq_recovered` in results.json |
|---|---|---|---|---|
| C40–C60 | −0.022778 | −0.020211 | −0.042989 | −0.042989 |
| C60–C70 | +0.000850 | −0.010603 | −0.009754 | −0.009754 |
| C70–C80 | +0.005929 | −0.010530 | −0.004601 | −0.004601 |

`R_q^pred` is negative at every pair by construction (a positive predicted ΔP maps to a negative `R_q`). C70–C80's observed `R_q` is positive. Its "power failure" is **destructive interference**, not low power.

Correcting the injection to remove the observed ramp before installing the predicted one (`delta_ab − R_q·X5[:,4] + R_q^pred·X5[:,4]`), five seeds each:

| Pair | as coded, p range | corrected, p range |
|---|---|---|
| C40–C60 | 0.0030–0.0035 (pass) | **0.0155–0.0182 (FAIL)** |
| C60–C70 | 0.0077–0.0099 (pass) | 0.0064–0.0076 (pass) |
| C70–C80 | **0.0135–0.0158 (FAIL)** | 0.0030–0.0036 (pass) |

`power_demonstrated = False` survives the correction — so the Combined Verdict is untouched, and I do not ask for it to move. But every per-pair power statement in `phase4_results.md` is inverted. Specifically, the Bottom Line's rhetorical closure — "the one pair whose displaced-carrier control passes (C70–C80) is exactly the pair whose significance and injection-recovery power both fail" — is built on the artifact. Under a correct injection C70–C80 is the **best-powered** pair of the three. That sentence should be struck, not repaired.

This is a defect in Red Team's docket item 4 as written ("inject … into the H₀-fitted series plus the observed residual"), faithfully implemented. It is exactly the class of thing Phase 5 exists to catch, and Phase 2–4 could not have, because the specification and the implementation agree.

### D3 — SUBSTANTIVE. Docket item 7 is roughly half implemented, and `phase3_synthesis.md` claims all 15 items are implemented "verbatim to the audit's specification."

Item 7 mandates four things. `run.py` delivers one.

| Mandated | Delivered |
|---|---|
| Bootstrap step 1 into `SE(R_q)` | ✓ `SE_Rq_bootstrap` |
| …and into `SE(ΔP)` | ✗ **absent from `run.py` and `results.json`** |
| Report `dR_q/dψ̄` per pair | ✗ **never computed** |
| Report `R_i/R_q` per pair | ✗ (only the `\|R_i\|σ_u/a` strain proxy) |
| "All P-072-1 significance statements use the propagated SE" | ✗ **no gate uses `SE_Rq_bootstrap`; `RESOLVED` gates on the fixed-ψ surrogate p** |

Docket item 12 separately mandates "ΔP **and its propagated SE** at all four carriers." The item-12 table in `phase4_results.md` has no SE column, because the quantity was never computed.

I computed the three missing quantities. `SE(ΔP)_bootstrap = |ΔP/R_q|·SE(R_q)_boot` gives **0.0544° / 0.0192° / 0.0116° / 0.0691°**. Against a total measured C40→C80 period span of 0.093°, the instrument's 1σ on a single pair is **13% to 74% of the entire effect it is chasing**. With that column present, the sign-flipping ΔP table needs no interpretation at all: every entry is within ~1σ of zero at three of four pairs. Its absence is why the write-up has to reach for a narrative the numbers supply directly.

`phase3_synthesis.md` lines 10–11 assert "**All 15 docket items are implemented in `run.py`, verbatim to the audit's specification**." That claim does not hold for item 7 and does not hold for item 13 (D7 below).

### D4 — MODERATE. Two arithmetic errors in `phase4_results.md`'s P-072-1 section.

- "**Bootstrap SE is 3.7–4.8× the naive OLS SE at every pair.**" Actual ratios: **3.83 / 6.86 / 5.75 / 4.81** — the range is 3.8–6.9×. The quoted range brackets exactly the first and last pairs, which suggests the two interior pairs were never computed. The Bottom Line repeats it as "4–5× … at every pair."
- "**No pair's `|R_q|/SE_bootstrap` clears 2 (0.94 / 0.09 / 0.99 / 0.42).**" Actual: **1.06 / 0.11 / 1.24 / 0.55**. The conclusion survives, but the printed figures put all four pairs below 1 when two exceed it.

Both are R4-class (a figure presented as computed that does not reproduce from the committed function). Neither moves a verdict.

### D5 — MODERATE. The 1.9608° disclosure is incomplete, and the omitted half is the most consequential number in the run.

Docket item 10 retains the fringe carrier as "mandatory disclosure explicitly labelled a resolution identity." `phase4_results.md` discloses ΔP at 1.9608° in the item-12 table and nothing else. `results.json` also holds `R_q` and the restricted-null p at that carrier:

| Pair | `p` restricted at `T_mean` | `p` restricted at 1.9608° |
|---|---|---|
| C40–C60 | 0.0122 | **0.0017** |
| C60–C70 | 0.4634 | 0.0415 |
| C70–C80 | 0.0066 | 0.5548 |
| C40–C80 | 0.0501 | **0.00015** |

**The design's own significance test is 7× to 334× more significant at a carrier the design declares wrong** than at the carrier it gates on, at both of the two widest pairs. Any reader deciding how much weight to put on the restricted-null p-values needs this table and does not have it.

### D6 — MODERATE. Epistemic inflation on the saturating-vs-linear result (my own finding), and a dropped caveat.

Red Team's Attack 6 adopted MATERIALS' and my P-072-4 changes "on that narrower ground" — robustness of `m₀` as an anchor — and stated the caveat neither seat had: "all four numbers are 4 points against 2 parameters either way." `phase4_results.md` reports the R² comparison, correctly labels it disclosed and non-gating, correctly notes the ABSORB/PAD confound — and drops the 4-points/2-parameters caveat entirely while upgrading the conclusion to "MATERIALS' and THERMODYNAMICS' finding survives the tie-break VISION's critique forced." Restore the caveat; downgrade "survives" to "the ranking is robust to the tie-break and to the choice of L, on four points against two parameters."

### D7 — MODERATE. Four of docket item 13's disclosure bullets were never written, and one cross-reference points at a caveat that does not exist.

| Item 13 bullet | Status |
|---|---|
| ABSORB-or-PAD rule extended to P-072-1/P-072-6 | ✓ |
| …"P-072-6 supplies the confounded arm of queue item 2, does not substitute for it" | ✗ **absent everywhere** (THERMO §3) |
| "-or-frequency-or-fringe-weight," non-identifiability conceded | ✓ (`NOTES.md` Idealization 2) |
| C70/C80 reversal — "one sentence in §2c, one in **Idealization 6**" | ✗ **`NOTES.md` Idealization 6 is "No new FDTD…" and contains no such sentence** |
| MATERIALS 4: "genuine saturation is an equally live reading of the same node collision" | ✗ half (the PAD-curvature half is present; the equally-live-reading half is not) |
| Window provenance | ✓ |
| `C_empty` is not a contrast | ✓ |
| §7 energy sidecar N/A | ✓ |
| Name queue item 4, re-defer with a stated reason | ✗ **absent everywhere** (THERMO §4) |
| §4 contamination paragraph + `CONFIRM_UNCERTIFIED` rule | ✓ |

`phase4_results.md` line 157 states the order reversal is what "**Idealization 6 discloses**," and `run.py` line 227 repeats the attribution. The substance *is* disclosed — in `phase4_results.md` itself — but the mandated location is empty and both cross-references are false. Two of the three outright-missing bullets are mine.

### D8 — MINOR, but live for successors. The derived pair gates on an unadjusted p, and counts as an independent unit in two places.

`run.py` line 473 sets `per_pair["C40-C80"]["p_restricted_holm"] = p_restricted` (unadjusted), and line 479's `resolved` test then applies the same `≤ 0.01` bar to it. So the **derived** pair faces a strictly easier bar than the three free pairs it is the arithmetic sum of — and `phase4_results.md` records that CONFIRM "requires C40–C80 and C40–C60 `RESOLVED`," i.e. the CONFIRM path runs *through* the derived pair. Separately, `resolved_pairs` at line 534 includes C40–C80, so the derived pair can trigger P-072-4's `sign_reversal` REFUTE on its own and counts toward the `len(resolved_pairs) >= 2` CONFIRM precondition; and `n_resolved_holm10_*` (lines 497–502) adds it to the REFUTE-blocking count. Docket item 14 struck the *phrase* "independently-measured endpoint pair" from the prose but left the derived pair operating as a fourth independent unit in four places in the code. Outcome-inert this cycle (nothing resolved); it should not survive into the next pre-registration.

### D9 — MINOR. Two unsupported comparatives in the Bottom Line.

"The carrier itself resolves cleanly, R²≈0.43–0.45, at every pair, matching Iteration 48's own per-config fits." The numerical match is exact — exp-071's per-config free-period R² are 0.4327 / 0.4483 / 0.4422 / 0.4337. But R²≈0.44 is not "resolves cleanly," and the sentence's own evidence shows the differential route achieves **identically** what the absolute route achieved on the only comparable quantity. That undercuts the adjacent claim that the instrument is "better-conditioned than the absolute-period route it replaces," for which no comparative figure is offered (`cond5≈60` has no counterpart in the absolute route).

### Two checks that came back clean, recorded so nobody re-runs them

- **Bootstrap grid coarseness is immaterial.** `run.py` bootstraps step 1 at `n_grid=400` while the point estimate uses 3000. I re-ran 200 bootstrap replicates at both resolutions: C70–C80 SE = 0.004521 (400) vs 0.004519 (3000); C40–C60 SE = 0.023338 vs 0.023340. Identical to four significant figures. Not a defect.
- **Holm arithmetic is exact** at both nulls, over 3, with the correct step-down running maximum; every adjusted value in `results.json` reproduces by hand.
- **G0-a/b/c reproduce exactly** (`0.0` residuals), and the q95 surrogate free-period search uses the same [1.0°, 4.0°] range as `_free_period_search`. One asymmetry worth a footnote next time: the surrogate search runs at `n_grid=300` while the observed statistic runs at 3000; the in-code note defends *pair* symmetry, which is not the asymmetry that exists. Immaterial at these magnitudes.

---

## 4. What this cycle's own data says that the write-up does not

This is the part I would most like the panel to look at, because it is derivable in four lines from numbers already in `results.json` and it makes the Bottom Line's central claim both simpler and stronger.

**The 5-column design's column space is invariant under the step-1 carrier phase `ψ`.** Rotating `ψ → ψ + δ` rotates the pairs `(A_i, A_q)` and `(R_i, R_q)` within an unchanged span, so the fitted values do not move and the coefficients rotate exactly:

> `R_q(ψ+δ) = R_q·cos δ + R_i·sin δ`,  hence  **`dR_q/dψ̄ ≡ R_i`** — exactly, not to first order.

I verified this numerically: central differences give +0.02032 / +0.01049 / +0.00363 / +0.03594, against `R_i` = +0.020318 / +0.010489 / +0.003634 / +0.035944.

This collapses three of the docket's separate concerns into one object:

1. **Item 7's missing `dR_q/dψ̄` is item 11's model-strain flag.** `R_i` was never a nuisance; it is the sensitivity of the headline coefficient to a nuisance parameter. The design flagged it as "strain" and gave it no consequence, which is why the connection was never made.

2. **The step-1 carrier is not identified in this window.** Bootstrapping step 1 (400 replicates/pair) gives a circular SD on `ψ̄` of **1.035 / 1.053 / 1.102 / 1.071 rad** (59–63°), and a 5th–95th percentile band on the carrier *period* of [1.84°, 4.00°] / [1.79°, 2.77°] / [1.77°, 2.81°] / [1.77°, 2.73°]. The 1.9608° fringe sits **inside the carrier's own 90% bootstrap band at all four pairs**; the 3.60° "displaced control" sits inside it at C40–C60 (95th percentile 4.00°, the search's upper bound). Red Team established 0.6452 Rayleigh widths from a point estimate; the bootstrap says the point estimate does not exclude either comparator.

3. **A carrier-phase rotation of ≤1σ_ψ annihilates `R_q` at every pair.** Solving `tan δ₀ = −R_q/R_i`: δ₀ = **+0.842 rad (48.3°) / −0.081 (−4.6°) / −1.021 (−58.5°) / +0.392 (22.5°)**, i.e. **0.08σ_ψ to 0.95σ_ψ**. Re-fitting at `ψ+δ₀` returns `R_q` = ~1e−17 at all four pairs. That is the entire resolution failure in one line, and it needs no appeal to a second contributor.

**The phase-invariant version of the test is null everywhere.** The rotation-invariant ramp magnitude ‖R‖ = √(R_i²+R_q²) = 0.030523 / 0.010523 / 0.006954 / 0.038900. Tested against a 20,000-surrogate restricted null that randomises *both* ramp columns (H₀: R_i = R_q = 0, a 3-column basis), raw p = **0.0361 / 0.0675 / 0.1060 / 0.0641**; Holm over the three free pairs = **0.108 / 0.135 / 0.135**. Not one pair reaches even the relaxed 0.10 bar.

The consequence deserves stating plainly and then bounding carefully. The pre-registered count `n_resolved_holm10_restricted = 3` — the count that blocked the REFUTE branch and produced `NEITHER` rather than `UNDERPOWERED_NOT_EVALUABLE` — is a count of significant *projections onto an axis fixed by a nuisance parameter with a 60° uncertainty*. On the invariant, that count is zero.

**I am not asking that this cycle's verdict change.** `NEITHER` is what the pre-registered boolean function returns on the pre-registered statistic, Red Team's contamination ruling makes post-hoc estimator substitution exactly the hazard it was written to prevent, and the invariant test is a different hypothesis (H₀: R_i = R_q = 0), not a strictly better version of the same one. What I am saying is that the cycle's declared substantive finding — *why* nothing resolved — is available in a sharper, carrier-free form than the one published, and that the correct pre-registration for the successor is a `ψ`-marginalized statistic.

---

## 5. Ranked top-3 candidate directions

### 1. Run Iteration-49 queue item 2 now (matched-`PAD` amplitude probe + `PAD` decorrelation, ~62–93 calls), with its primary metric re-scoped to phase-invariant channels.

This cycle is the argument for it. Every deliverable exp-072 produced is scope-limited by a sentence that has to read `ABSORB`-or-`PAD`-or-frequency-or-fringe-weight-tied — the confound is now the binding limit on the *disclosure* channels, not just on a hypothetical CONFIRM, which is the finding I brought in Phase 2 and which this cycle's zero-CONFIRM outcome makes load-bearing rather than hypothetical. Three consecutive cycles (47/48/49) have now closed without touching it.

More specifically, §4 says the period/phase route is exhausted in this window: a ≤1σ_ψ carrier rotation zeroes the headline coefficient at every pair, and the invariant version of the test is null everywhere. The amplitude discriminator I proposed for item 2 is the only channel on the table that never conditions on a fitted carrier phase — that is now a measured property of this window, not a design preference.

Two concrete additions from this cycle, both free:
- Report the **phase-invariant differential carrier amplitude** √(A_i²+A_q²)/a alongside the ptp discriminator. This cycle's confounded-arm values are **0.161 / 0.041 / 0.020 / 0.166** for C40–C60 / C60–C70 / C70–C80 / C40–C80 — a directly comparable baseline the matched-`PAD` arm can be scored against, at zero additional cost.
- Carry `SE(ΔP)` (0.012–0.069° per pair here) into the new cycle's power table. Any period-channel claim in item 2's window must clear that, and this cycle shows it will not.

### 2. A zero-FDTD clean re-pre-registration of the differential estimator, on a carrier-phase-marginalized statistic.

Cost: zero new calls, one desk cycle. Red Team's contamination ruling already means this cycle's p-values "should be read as design-verification numbers … not as a first, blind look"; condition 3 explicitly contemplates a fresh pre-registered cycle. Four deliverables, all specified by defects above rather than by outcomes:

- Pre-register a `ψ`-marginalized test of `R_q` (profile over the bootstrap `ψ` distribution) as the gating statistic, with the invariant ‖R‖ test reported alongside. The estimand is preserved; the nuisance is integrated rather than conditioned on.
- Fix the injection-recovery to remove the observed ramp before injecting (D2). The corrected per-pair power profile is the inverse of the published one.
- Compute and report the three quantities item 7/12 mandated and never produced: `SE(ΔP)`, `dR_q/dψ̄` (= `R_i`), `R_i/R_q`.
- Strip the derived pair's gating privileges (D8) and settle, on a clean pre-registration, whether this window's honest verdict is `NEITHER` or `UNDERPOWERED_NOT_EVALUABLE`.

I rank this second only because it cannot relieve the confound. It is a prerequisite for any *period-channel* scoring inside direction 1 and should run as that cycle's desk-side companion, not after it.

### 3. Re-scope queue item 4: keep PHOTONICS' two-tone joint fit, defer or fold in the `ABSORB≈120` build (31 calls).

This is my seat's own physics and it argues against spending. On the engine-derived decay constant, the saturating model puts **P(∞) − P(80) = 0.0052°** (0.0100° at L=0.06; 0.0256° at L=0.04). The residual boundary return has essentially exhausted itself by C80 — there is almost nothing left on the `ABSORB` axis to measure.

That cuts both ways and I will state both. An 80→120 step is where the two models diverge *most*: linear predicts +0.102°, saturating +0.005°, a ~0.10° separation — the largest model-discriminating step available anywhere on this axis. But the separation must be read against this cycle's own propagated uncertainty at 40-cell pair separation, `SE(ΔP)` = 0.054–0.069°, giving a discrimination of **z ≈ 1.4–1.8**. That is not decisive, it costs 31 calls, and VISION's queue item 5 has already ruled the 36°–42° window off-limits for a third absolute-period discriminator — which is exactly what an `ABSORB=120` period comparison would be.

Recommendation: fold `ABSORB=120` into item 2's build so it shares the matched-`PAD`, resolution-floor-free amplitude readout, or defer it until a wider-θ window exists (a wider window shrinks the Rayleigh width, which is the only thing that would pull both the 1.9608° fringe and the 3.60° comparator out of the carrier's own bootstrap band — see §4). Run the two-tone joint fit regardless; it is desk-only, and §4's finding that the carrier is bimodally unstable under resampling is a direct motivation for it.

*R5 check: none of the three re-proposes a ruled-out idea. None is a dense unconstrained parameter search; the `P`-normalized phase offset (R5 proper) and the `A_alt≈3·R_OUT` / `A_eff≈519` named-constant dead ends do not appear. Direction 2's `ψ`-marginalization is a nuisance-parameter treatment on a pre-specified single statistic, not a search, and does not trigger the Iteration-47 look-elsewhere addendum.*

---

## 6. Summary for the Director

- **My two Phase-2 findings**: finding 1 (rate-window demotion) implemented correctly in code and verified; finding 2 (caveat rule extended past CONFIRM) implemented in substance, with the mandated second half of the sentence dropped from every deliverable.
- **Energy sidecar**: genuinely N/A, disclosed by argument at two locations, no smuggled thermal or detectability claim anywhere. One wording risk noted, in a sentence my own Phase-2 contribution motivated.
- **Nine defects**, three substantive (D1 gate misattribution + the stronger finding it hides; D2 the injection test is not a power test; D3 item 7 half-implemented under a blanket "all 15 implemented" claim), none of which moves the Combined Verdict, two of which materially change the *reason* for it.
- **One structural result** the cycle's own data supports and the write-up does not state: `dR_q/dψ̄ ≡ R_i` exactly, σ_ψ ≈ 1.07 rad, and a ≤1σ_ψ carrier rotation annihilates `R_q` at all four pairs — with the phase-invariant version of the test null everywhere (Holm 0.108 / 0.135 / 0.135).
- **`NEITHER` stands.** It is the right verdict on the pre-registered statistic and I do not ask that it move.
