# PHASE 2 — RED TEAM AUDIT · Panel Iteration 49 · exp-072 (T28 differential/beat fit)

*Fresh sub-agent, RED TEAM charter. Receives the Phase-1 proposal and all five blind Phase-2 critiques; speaks last. Desk-only instrument/methodology cycle on live thread T28 — T1 N/A, constraint 3 not engaged, so the constraint tags are N/A and every attack below is tagged `[inconsistency]` or `[unfalsifiable]`.*

---

## 0. Framing — what is actually at stake, and what this audit did

Two seats (QUANTUM OPTICS, VISION SCIENCE) executed the proposed estimator on the real 124 committed points during Phase 2. Their findings are not the same finding, they were derived blind to each other, and the parent's central question — same defect, different defects, or contradictory diagnoses? — is answered in §2.

Red Team's job here is not to average prose. **Every load-bearing numerical claim in all five critiques was re-executed from the committed JSON in an independent implementation**, including the two things neither sub-agent did: (a) running *both* proposed nulls to their observed p-values, and (b) forward-simulating the proposal's own noiseless model to calibrate its own gates. That work found three defects none of the five seats caught, and it found that one seat's prescribed remedy is worse than the disease it names.

It also means Red Team now holds outcome-determining numbers. That is ruled on explicitly in §4, and it constrains the docket in §6.

**Verification ledger (all reproduced independently from the committed JSON):**

| Claim | Source | Status |
|---|---|---|
| θ grid bit-identical, 31 pts, 36.0–42.0° (G0-a) | QUANTUM, VISION | **VERIFIED** |
| G0-b telescoping residual | QUANTUM, VISION | **VERIFIED = 0.0 exactly** |
| G0-c: exp-069 `delta` ≡ `C80 − C40` | proposal | **VERIFIED = 0.0 exactly** |
| Design-matrix `cond ≈ 60` at every pair | QUANTUM, VISION | **VERIFIED (59.9–61.0)** |
| `X = 0.0813454`, `1/X = 12.2933`, 41.4% Rayleigh floor | proposal, QUANTUM | **VERIFIED** |
| 1.9608° carrier sits at 0.645 Rayleigh widths | EM (0.645), QUANTUM (0.646) | **VERIFIED = 0.6452** |
| `x̄/σ_u ≈ 27` | EM | **VERIFIED (25.9 pop. sd; 26.8 on EM's `X/2√3`)** |
| VISION's entire §0b three-carrier ΔP/z/ρ_c table | VISION | **VERIFIED, every digit** |
| `n_grid=3000` per-config periods 2.43748/2.52051/2.53551/2.53051 | VISION | **VERIFIED — C70/C80 order does reverse** |
| `R_q` telescoping residual 3.8% at a common carrier | VISION | **VERIFIED = 3.79%** |
| exp-071 per-pair rates 0.004135/0.001504/0.000000 °/cell | THERMODYNAMICS | **VERIFIED exactly** |
| Committed `trend.linear_fit.slope = 0.0025564` ≠ cited `0.00244361` | MATERIALS | **VERIFIED — and see Attack 5, it is worse than a typo** |
| Saturating ≫ linear on the four committed periods | MATERIALS, THERMO | **VERIFIED in substance (see Attack 6 for the caveat)** |
| `R_i` non-zero and comparable-to-larger than `R_q` at every pair | QUANTUM 5b | **VERIFIED: |R_i/R_q| = 0.48 / 2.81 / 1.69 / 1.10** |
| Sub-Rayleigh fringe leaks into `R_q` at tens per unit amplitude | QUANTUM 5a (34.8) | **VERIFIED = 28.0; substance stands** |
| Unrestricted-null SD ÷ OLS SE = 4.7–5.9× | QUANTUM §4 | **PARTIALLY — I get 3.6–6.0×** |
| Restricted-null SD ÷ OLS SE = 1.04–1.37× | QUANTUM §4 | **NOT REPRODUCED — I get 1.8–2.4×** |

The last two rows matter: QUANTUM's headline correction is right in direction and wrong in magnitude in my implementation. **No threshold in the docket may be set from QUANTUM's specific ratios.**

---

## 1. Numbered attacks

### 1. [inconsistency] The null the design gates on tests a hypothesis that is not H₀, and the choice between the two candidate nulls is outcome-determining between `REFUTED` and `NEITHER`. I have verified which way, at both.

QUANTUM's §4 argues on principle that phase-randomising raw `delta_AB` embodies "`delta_AB` is coloured noise with this spectrum," not H₀: `R_q = 0`. That is correct and it is standard surrogate-data practice (the surrogate ensemble must be generated *under the null being tested*). QUANTUM deliberately withheld the consequence. I computed it.

Running §3 exactly as pre-registered (N=20,000, seed `20490072`, statistic `|R_q|`, two-sided, Holm across 4), at the proposal's own `T_mean`/`ψ̄`:

| Pair | raw *p*, **unrestricted** (as written) | Holm-adj | raw *p*, **restricted** (QUANTUM's fix) | Holm-adj |
|---|---|---|---|---|
| C40–C60 | 0.1738 | 0.6954 | 0.0057 | 0.0172 |
| C60–C70 | 0.7495 | 1.0000 | 0.1034 | 0.1034 |
| C70–C80 | 0.4706 | 1.0000 | 0.0041 | 0.0164 |
| C40–C80 | 0.3746 | 1.0000 | 0.0158 | 0.0316 |

Robust across three seeds and against EM's detrend-before-randomise variant (§1.3 secondary); the largest seed-to-seed drift is 0.003.

**Consequence, pre-registered branches applied literally.** Under the null *as written*, **zero pairs reach even the relaxed Holm-adjusted `p ≤ 0.10`, including C40–C80 → P-072-2 fires REFUTE → Combined Verdict `REFUTED`**, whose pre-committed reading is "the differential/beat framing buys nothing over the absolute one in this window." Under the restricted null, C70–C80 clears 0.10, REFUTE cannot fire, no pair clears 0.01, and the Combined Verdict is `NEITHER`.

So the single most consequential sentence this cycle will publish is selected by a null-construction detail that the proposal spends four bullet points specifying and zero sentences justifying. QUANTUM called this exactly right — "a REFUTE that reads as a verdict on the beat framing when it is a verdict on the null's width" — and did so before computing the observed p. That the prediction was made blind is what makes the fix adoptable; see §4.

### 2. [unfalsifiable] P-072-2's REFUTE branch fires with high a-priori probability under *both* H₀ and H₁. It is an auto-firing branch wearing a falsifier's label, and Combined-Verdict rule 2 promotes it to the headline.

REFUTE ⟺ *nothing* is significant. QUANTUM's §2 already showed, using the proposal's own `m₀` and the proposal's own null, that the design's own predicted effect clears its own Holm gate at one pair out of four (ratios 0.53/0.80/1.31/0.82). A design whose a-priori power analysis says "we expect to detect nothing" and whose REFUTE branch fires on "we detected nothing" is not testing anything — the branch's firing carries no information about the instrument, only about the sample size. §2c's "honest statement, pre-registered" concedes the power shortfall in prose and then leaves a branch standing that converts that shortfall into a published negative result about the *framing*.

This is a defect independent of Attack 1 and independent of which null wins. It must be fixed by requiring a **demonstration of power** before REFUTE is reachable, not by moving a threshold. Docket item 3.

### 3. [inconsistency] EM's diagnosis of the `A_q` table row is correct. EM's prescribed remedy is wrong, and would inject a 26-σ extrapolation into a disclosed quantity. **I override it.**

EM is right that `A_q = −a·Δψ` is wrong and that `Δf` is not absent from `A_q`. The exact relation is `A_q = 2a·sin χ` with `χ = πΔf·x̄ + Δψ/2`; EM's `A_q = a·Δψ + R_q·x̄` is its small-χ linearisation.

EM then prescribes reporting the phase channel as `|A_q − R_q·x̄|/a`. That quantity is `|Δψ|` — the phase difference between the two configs **extrapolated back to `x = 0`, i.e. θ = 0°, roughly 26 σ_u outside a window spanning 36°–42°.** Two independent demonstrations that this is not a repair:

- **Forward simulation.** On noiseless synthetic data built from the proposal's own model at the C60–C70 predicted effect size (`ΔP = 0.0244°`) with **true `Δψ = 0`**, EM's estimator returns `+0.1407` rad of phase offset; at the C40–C60 size it returns `+2.216` rad. The exact-in-χ estimator `Δψ = 2·arctan(A_q/2a) − R_q·x̄/a` returns `−0.0002` and `−0.0057`. EM's formula manufactures precisely the spurious-phase-offset artifact EM's own attack says it prevents — it removes the leading term and leaves an O(χ³) residual that is large here because χ is order 0.6–1.2 rad, not small.
- **Real data.** EM's channel evaluates to `+3.244` rad (**185.9°**) at C40–C60 and `+3.053` rad (**174.9°**) at C40–C80. Fitting each config separately at the same pair carrier gives the directly measured within-window phase difference: `−0.0525` rad (**−3.0°**) and `−0.1074` rad (**−6.2°**). EM's fix would have P-072-6 announce that C40 and C80 are 175° out of phase — for two configs whose measured phase offset is 6°, and whose common-mode average retains 99.9% of the mean per-config amplitude (arithmetically impossible at 175°).

EM's supporting claim that P-072-6 "will report a constant phase offset with probability ≈ 1" is also false on the data: `|A_q|/a` vs `|R_q|·σ_u/a` is 0.039/0.127, 0.041/0.015, 0.012/0.015, 0.087/0.121 — `R_q` dominates at two of four pairs.

**Correct fix (docket item 5):** relabel the row `A_q = 2a·sin χ`, `χ = πΔf·x̄ + Δψ/2` — *half the phase difference at window centre*, which is what this window measures — keep `|A_q|/a` as P-072-6's phase channel, and **prohibit quoting `Δψ` anywhere**, since it is an extrapolation 26 σ outside the data. EM's `A_i = a_B − a_A` checks out (fitted `8.24e−4` vs directly measured `7.73e−4`, 6%); `R_q = 2πa·Δf` and `R_i ≈ 0` check out as first-order statements.

### 4. [inconsistency] The carrier-consistency gate (`≤ 0.414`) is calibrated against the wrong reference quantity by two orders of magnitude, and this — not the Rayleigh width — is why every carrier in VISION's table passes it.

`0.414` is the Rayleigh floor for *separating two absolute frequencies*. It is applied to a completely different statistic: the sampling deviation of `T_delta` from `T_mean`. Nothing connects them.

Forward-simulating the proposal's own noiseless model at each pair's predicted `ΔP`: `|T_delta − T_mean|/T_mean` = **0.000, 0.000, 0.001**. The model predicts near-perfect carrier agreement. With iid noise added at the observed per-config residual level, the reference distribution has median 0.05–0.11 and 95th percentile **0.18 (C40–C80) to 1.16 (C40–C60)** — pair-dependent by a factor of six. The observed values (0.124/0.162/0.254/0.141) are therefore *not* the smoking gun a naive reading would make them, and I decline to claim otherwise — but `0.414` is demonstrably neither model-derived nor pair-appropriate. It is a number imported from a different problem, and its two documented consequences are exactly the ones EM and VISION found: it admits T21's declared-wrong 1.9608° carrier at all four pairs (`0.211–0.226`), and it admits every carrier in VISION's sign-flipping table.

Fix: calibrate the gate per-pair from the same surrogate ensemble, at a pre-registered percentile. Docket item 6.

### 5. [inconsistency] `m₀` is not a mis-transcription. It is a *different estimator* carrying another estimator's goodness-of-fit — an R4 failure of a nastier class than MATERIALS diagnosed.

Verified against `experiments/071-t28-absorb-depth-causal-test/results.json`:

- `trend.linear_fit.slope` = **0.0025563909774436134** (MATERIALS is right).
- The proposal's `0.00244361` = `(2.533834586466165 − 2.43609022556391)/40` = **0.002443609022556381** exactly — the C40→C80 **endpoint chord slope**, present nowhere in the committed JSON as a named field.

The proposal labels it "Iteration 48's own linear slope, R²=0.8664", attaching the least-squares fit's R² to a two-point chord. Both §2c's entire power table and every P-072-4 band are multiples of it. MATERIALS' fix is adopted; MATERIALS' *diagnosis* is corrected — this is not a typing slip, it is a provenance conflation, and the docket must require the value be **read from the JSON at runtime**, not restated.

### 6. [inconsistency] MATERIALS and THERMODYNAMICS converge on saturating-vs-linear and both are right about the direction — but the evidence is thinner than either says, because the fourth data point is the tie VISION broke.

Verified: per-pair rates 0.0041353 / 0.0015038 / 0.0000000 °/cell exactly; linear R² = 0.866381 exactly; a two-parameter saturating fit with decay constant fixed at `_damping`'s own per-cell optical depth (0.30/4 = 0.075) gives **R² = 0.9974** (MATERIALS reports 0.9957 — same finding, minor derivation difference). THERMO's independent energy-side derivation reaches the same place.

The caveat neither seat states: **all four numbers are 4 points against 2 parameters either way, and the "0.0000 °/cell" datum driving the saturation is exp-069's `n_grid=400` node collision that VISION showed reverses at the `n_grid=3000` this very proposal adopts.** Recomputing both models on the `n_grid=3000` periods: linear R² falls to 0.8328, saturating (L=0.075) to 0.9901 — the ranking survives, but the C70→C80 rate becomes **−0.0005 °/cell**, not 0. So the physics argument is credible and the *conclusion* is right — `m₀` is not a trustworthy band anchor — but it is right for the robustness reason, not because saturation is established. Both seats' P-072-4 changes are adopted on that narrower ground.

### 7. [unfalsifiable] P-072-3 is a conjunct of `CONFIRMED` and is close to an arithmetic tautology. EM, QUANTUM and VISION converge from three directions; all three are correct.

EM: OLS is linear in `y`, G0-b makes the raw deltas telescope exactly, so `ρ_c` inherits only second-order basis deviations. QUANTUM 5c: G0-b *proves* C40–C80 is the arithmetic sum, so the Combined-Verdict text calling it "the **independently-measured** endpoint pair" is false by the proposal's own gate. VISION §5: measured — the `R_q` telescoping residual at a common carrier is **3.79%** (I verify exactly), `ρ_c = 0.041` at `T_mean` and `ρ_c = 0.059` at the **carrier the proposal itself declares wrong**, both far inside the `≤ 0.25` CONFIRM band.

A closure statistic that CONFIRMs at a deliberately wrong carrier is not testing common-mode cancellation. Docket items 8–9.

### 8. [inconsistency] `R_i ≈ 0` is a first-order prediction of the model and it fails at every pair, and the design attaches no consequence.

Verified `|R_i|/|R_q|` = 0.48 / 2.81 / 1.69 / 1.10. §2b's table calls `R_i` a "nuisance / model-strain indicator" and then gives it no threshold, no gate, and no place in P-072-6. The model that licenses the entire `R_q → Δf` readout predicts this coefficient is zero; it is larger than the target coefficient at three of four pairs. QUANTUM's 5b request is adopted and hardened.

### 9. [inconsistency] P-072-5 is a resolution identity, not a control — and EM's flip condition would gate the Combined Verdict on it. **I modify EM's flip.**

QUANTUM 5a and EM's flip agree on the arithmetic and disagree on what to do. Verified: `f₂ − f̄ = 7.9316` against `1/X = 12.2933` → **0.6452 Rayleigh widths**. A unit-amplitude 1.9608° component projects into `R_q` at **28.0 per unit amplitude**; a between-config fringe-amplitude difference of only **2.2%** of carrier amplitude reproduces the entire observed 10-cell-step `R_q` (18.6% for the wide pairs). So `R_q` is a mixture of "period difference" and "second-contributor weight difference" that this window cannot separate.

QUANTUM is right about what P-072-5 *is*; EM is right that it must gate something. But gating on a sub-Rayleigh comparator converts an under-resolution identity into a verdict — the comparator is guaranteed to be comparable, so EM's clause `|R_q(1.9608°)| ≤ ½|R_q(T_mean)|` would fail pairs for a reason unrelated to contamination. **Adopt EM's promotion-to-gate, at QUANTUM's displaced carrier (≥1.5 Rayleigh widths, i.e. ≳3.6° or ≲1.85°); keep the 1.9608° run as mandatory disclosure explicitly labelled a resolution identity.** Docket item 10.

### 10. [inconsistency] VISION's facts reproduce perfectly; VISION's inference over-reaches, and its gate as specified is rigged to fail. **I adopt the disclosure and override the gate.**

Every number in VISION's §0b reproduces to the digit. The finding is real: the sign of ΔP for every pair flips somewhere inside the admitted carrier band.

But the three carriers are not on equal footing, and VISION's flip condition requires sign-invariance across a set containing one carrier the proposal itself declares wrong and which QUANTUM (blind to VISION) proved cannot be diagnostic. Requiring invariance across a knowingly-wrong comparator is a gate no correct measurement could pass. Two further pieces of evidence Red Team computed that VISION did not:

- **The `T_mean` result is not an arbitrary member of the admitted set.** At `T_mean` the differential ΔP agrees **in sign at 4/4 pairs** with the independently-computed `n_grid=3000` absolute-period differences — `+0.0697/+0.0830`, `+0.0085/+0.0150`, `−0.0086/−0.0050`, `+0.0668/+0.0930` (ratios 0.84/0.57/1.72/0.72) — *including the C70/C80 reversal VISION themselves discovered*. Only ≈3 of those signs are algebraically free, so this is weak (p ≈ 1/8), and both routes share the same 31 points and the same carrier machinery. It is not proof. It is enough to refuse "the sign is set by a nuisance choice, therefore the answer is arbitrary."
- **The real defect is upstream of carrier choice: nuisance-parameter uncertainty is nowhere propagated.** This is EM's item 3, and it is the correct general form of VISION's finding.

So: VISION's three-carrier table becomes **mandatory disclosure in P-072-1** (item 12); the sign-invariance conjunct is **not** adopted as specified; the underlying identification problem is fixed by the tightened, surrogate-calibrated carrier gate (item 6) plus mandatory propagation of step-1 uncertainty into `SE(R_q)` (item 7).

### 11. [inconsistency] THERMODYNAMICS' caveat hole is real as a reading of the text. Adopted verbatim.

Idealization 2's binding sentence conditions on "**Any CONFIRM**"; P-072-6 is non-gating and publishes an amplitude discriminator on the confounded `ABSORB`/`PAD` axis under *any* verdict, including NEITHER. Extend the writing rule to P-072-1 and P-072-6. Item 13.

### 12. [inconsistency] Holm is mis-scoped, and — verified — fixing it is outcome-neutral this cycle.

QUANTUM 5c: G0-b proves three algebraically free series, not four. Holm over 3 gives adjusted p of 0.0123/0.1034/0.0123 (restricted) and 0.5215/0.9412/0.9412 (unrestricted) — **no branch changes under either null.** Adoptable with zero contamination exposure. Item 14.

### 13. R5 check — not re-triggered, and nothing in this docket re-triggers it.

The proposal's §3 reasoning is sound: one physically-motivated functional form, four pre-specified pairs, one 1-D continuum grid already ruled non-triggering by exp-069/071. The docket's expanded carrier set is four named carriers, all pre-specified here — not a search. No LOGBOOK R5 ruled-out item (`A_alt≈3·R_OUT`, the `A_eff≈519` cluster) appears anywhere. **Confirmed clean.** THERMO's §5 concurs.

---

## 2. The central adjudication: QUANTUM's restricted null vs VISION's carrier gate

**They are two different defects, both real, fully compatible, non-redundant, and they must be adopted together — with VISION's evaluated first.**

| | QUANTUM §4 | VISION §3/§0b |
|---|---|---|
| Object attacked | the **reference distribution** for `R_q` | the **point estimate** `R_q` itself |
| Nature | null misspecification (surrogate does not embody H₀) | non-identification (nuisance carrier fixed, uncertainty unpropagated) |
| Touches | *p*-value only | sign, magnitude, SE, and *every* downstream verdict |
| Direction on the verdict | **increases** significance | **removes** estimates from admissibility |
| Fix is | narrower null | admissibility condition + variance propagation |

They are orthogonal in what they act on and **opposite in direction**. That is the whole reason both are required:

**Adopting QUANTUM's fix without VISION's is the actively dangerous combination.** It delivers `p ≤ 0.01`-class significance on a quantity whose sign VISION has shown is set by a nuisance choice the window cannot adjudicate. Adopting VISION's without QUANTUM's is merely conservative. Neither moots the other; the two changes touch disjoint parts of the pipeline (step 3's surrogate construction vs step 1's carrier admissibility) and can be implemented in the same `run.py` without interaction.

**And the two seats do not actually disagree.** QUANTUM's §5a — `R_q` is a non-identifiable mixture of "period difference" and "second-contributor weight difference," measured at 2.2–18.6% of carrier amplitude — **is VISION's §3 finding, reached from the contaminant side instead of the carrier side.** QUANTUM found *both* defects and demoted the second to "non-gating, but I ask that it be recorded"; VISION found only the second and made it the flip condition. Adjudication: **QUANTUM is right about what the defect is (non-identifiability, not carrier arbitrariness); VISION is right that it must gate rather than be recorded.** EM's item 3 (propagate phase-reference error into `SE(R_q)`) is the bridge between them and is the correct general form of the fix. The docket implements all three as one coherent change.

---

## 3. Requested changes I am overriding, and why

| Seat | Requested | Ruling |
|---|---|---|
| **ELECTROMAGNETISM** | P-072-6 phase channel = `|A_q − R_q·x̄|/a` | **OVERRIDDEN.** Diagnosis accepted, remedy replaced — it reports a 26-σ extrapolation and manufactures the artifact it names (Attack 3, two independent demonstrations). Replaced by the centre-phase relabel. |
| **ELECTROMAGNETISM** | Flip: gate `RESOLVED` on `|R_q(1.9608°)| ≤ ½|R_q(T_mean)|` | **MODIFIED.** Promotion-to-gate accepted; comparator moved to QUANTUM's ≥1.5-Rayleigh-displaced carrier. Gating on a sub-Rayleigh comparator gates on an identity (Attack 9). |
| **VISION SCIENCE** | Flip: `RESOLVED` requires sign-invariance across `{T_mean, T_delta, 1.9608°}` | **OVERRIDDEN as a gate, ADOPTED IN FULL as disclosure.** The set contains a carrier the design declares wrong; no correct measurement could pass (Attack 10). Underlying defect fixed by items 6 + 7 instead. |
| **MATERIALS / THERMO** | Loosen or demote P-072-4's rate bands | **ADOPTED**, on robustness grounds (`m₀` is an unreliable anchor, Attacks 5–6), not "the physics is saturating." Verified outcome-inert this cycle: P-072-4 cannot reach its ≥2-`RESOLVED` precondition under either null. |
| **All other requests, all five seats** | — | **ACCEPTED IN FULL.** |

---

## 4. Ruling on pre-registration contamination

**The pre-registration of exp-072 is contaminated, and the cycle may no longer claim any Phase-4 result was scored blind.** State that plainly rather than manage it.

**The facts.** QUANTUM executed the estimator and both nulls and disclosed structure while withholding outcome numbers. VISION executed the estimator and **published outcome-determining numbers** — ΔP, z, and `ρ_c` at three carriers, which directly determine P-072-3's branch and P-072-4's sign clause. Red Team has now computed the observed surrogate p-values under both nulls and knows which P-072-2 branch each selects.

**The precedent.** exp-070's Phase-2 audit (LOGBOOK Iteration 47) ran the proposal's own null control in scratch, mandated it into the docket on the strength of that run, and — docket item 7 — required the write-up to **state whether thresholds were set before or after specific numbers were computed, so downstream readers judge independence for themselves.** The operative boundary in this program is the Phase-3 commit of `run.py` and thresholds to git; Phase-2 computation is a feature of the blind-critique design, not a violation of it.

**Why that precedent is not sufficient here.** In exp-070 the Phase-2 computation made the design *stricter* — the audit found the proposed control would likely fail and mandated it anyway. Here, two requested fixes (the restricted null; Holm over 3) make the design **looser**, and I have verified that the first of them flips the headline verdict from `REFUTED` to `NEITHER`. That is a live researcher-degree-of-freedom hazard, and "we followed exp-070" does not discharge it.

**Ruling — four binding conditions, and the docket is constructed to satisfy them.**

1. **Outcome-independence test.** Every docket item must be justified by an argument that does not reference an observed value. The restricted null passes: it was argued by QUANTUM on the textbook ground that a surrogate ensemble must be generated under the null being tested, *in a document written before any seat computed an observed p*. The REFUTE power gate passes: it follows from QUANTUM's §2 a-priori table, computed from the proposal's own `m₀`. The carrier-gate recalibration passes: derived from a **noiseless forward simulation of the proposal's own model**, touching no data. Items whose justification could not be separated from an observed number are not in the docket.
2. **Net strictness.** The docket must not be a net loosening. It is not: the restricted null is adopted **in the both-reported form, gating `RESOLVED`**, but the REFUTE branch is simultaneously placed behind a demonstrated-power requirement (item 3) and `RESOLVED` behind a tightened carrier gate (item 6) and a displaced wrong-carrier gate (item 10). Net effect on reachable verdicts: strictly stricter.
3. **CONFIRM is unavailable this cycle.** Three seats have seen the answer; a CONFIRM could not be certified as pre-registered by anyone. If the Phase-4 run satisfies CONFIRM's boolean conditions it must be emitted as `CONFIRM_UNCERTIFIED`, reported as such, and re-run as a fresh pre-registered cycle before entering LOGBOOK. This costs nothing — verified: no pair is `RESOLVED` under either null, so CONFIRM is unreachable on the actual data regardless — and it closes the loophole permanently.
4. **Full disclosure, named.** `phase4_results.md` and `NOTES.md` must carry a paragraph naming who computed what and when, citing this audit, and stating that the null construction was selected in Phase 2 with Red Team already knowing it selects between `REFUTED` and `NEITHER` and in which direction. A reader must be able to discount this cycle's *p*-values without reconstructing the history.

**Nothing in this ruling permits a threshold to move after Phase 3's git commit.** Everything below is fixed *now*, before `run.py` exists.

---

## 5. Verdict

# **PROCEED-WITH-MANDATORY-FIXES**

The instrument is the right move on T28 and all five seats say so. The derivation is correct where EM checked it; the estimand substitution genuinely executes QUANTUM's own exp-071 Rayleigh argument rather than evading it; the confound and not-a-material caveats are the best in the T28 series; VISION's window-discipline constraint is satisfied in letter and mostly in spirit; the cost is zero FDTD.

What is not yet safe to run is the pre-registration wrapped around it. Three of its scored branches are miscalibrated in ways that are *proven*, not argued — a null that tests the wrong hypothesis and selects the headline verdict; a REFUTE branch that fires on power failure; a carrier gate imported from a different problem; a coefficient table whose one interpreted entry is wrong and whose proposed repair is worse; and a closure test that CONFIRMs at a carrier the proposal itself calls wrong. Every one is fixable at the design stage at zero FDTD cost. This is exactly the shape PROCEED-WITH-MANDATORY-FIXES exists for. REJECT-REDESIGN would be wrong: the estimator is sound and the data are already collected.

---

## 6. Mandatory-fix docket — 15 items, to be applied at Phase 3 before `run.py` and thresholds are committed to git

**A. Null construction and significance (Attacks 1, 2, 12)**

1. **Adopt the H₀-restricted surrogate null, in addition to the original.** Per pair: fit the 4-column basis `[1, cos θ_c, −sin θ_c, u·cos θ_c]` (H₀: `R_q = 0`); phase-randomise that fit's residual; add it back to the fitted null series; refit the 5-column model; statistic `|R_q|`. N=20,000, seed `20490072`, two-sided, unchanged. **Report both p-values for every pair, always.** *(QUANTUM §4, accepted; magnitudes not adopted — see item 2.)*
2. **No threshold anywhere may be derived from QUANTUM's quoted null-SD ratios.** Red Team's independent implementation reproduces 3.6–6.0× (QUANTUM: 4.7–5.9×) unrestricted and 1.8–2.4× (QUANTUM: 1.04–1.37×) restricted. `run.py` computes its own; the pre-registered gates are on p-values, not on SD ratios. *(Red Team.)*
3. **`RESOLVED` gates on the restricted-null Holm-adjusted p (`≤ 0.01`). REFUTE is placed behind a demonstrated-power precondition.** P-072-2 REFUTE now requires all three: zero pairs at Holm-adjusted `p ≤ 0.10` under the **restricted** null; **and** zero pairs at `p ≤ 0.10` under the **unrestricted** null; **and** the injection-recovery test of item 4 passes. If the injection test fails, the branch emits `UNDERPOWERED_NOT_EVALUABLE`, never REFUTE. *(Attack 2; QUANTUM §2.)*
4. **Add a pre-registered injection-recovery power test.** Per pair: inject a synthetic ramp of amplitude `R_q^pred = 2πa·Δf(m₀_committed · ΔABSORB)` into the H₀-fitted series plus the observed residual; run the identical pipeline including the restricted surrogate null; require recovery at the same Holm-adjusted `p ≤ 0.01`. Deterministic, seed `20490072`, reported per pair in P-072-1. This is the design's power statement in code rather than in §2c's prose. *(Red Team.)*
14. **Apply Holm–Bonferroni over the three adjacent pairs only.** Report C40–C80's p unadjusted and explicitly labelled *derived*, and strike "independently-measured endpoint pair" from the Combined-Verdict text — G0-b proves it is the arithmetic sum. Verified outcome-neutral under both nulls. *(QUANTUM 5c.)*

**B. Estimator, coefficients, carrier (Attacks 3, 4, 8, 9, 10)**

5. **Correct the `A_q` row to `A_q = 2a·sin χ`, `χ = πΔf·x̄ + Δψ/2` — "half the phase difference at window centre."** P-072-6's phase channel stays `|A_q|/a`. **`Δψ` (the θ = 0° extrapolation) may not be quoted anywhere in any deliverable.** EM's `|A_q − R_q·x̄|/a` is not adopted. `A_i = a_B − a_A` and `R_q = 2πa·Δf` unchanged. *(EM item 1, diagnosis accepted / remedy overridden — Attack 3.)*
6. **Recalibrate the carrier-consistency gate from the surrogate ensemble, per pair.** Replace `|T_delta − T_mean|/T_mean ≤ 0.414` with `≤ q₉₅`, where `q₉₅` is the 95th percentile of that same statistic over the restricted-null surrogate ensemble for that pair, computed and reported in-run. The `0.414` figure is the Rayleigh floor for a different quantity; the proposal's own noiseless model predicts `≤ 0.001`. *(Attack 4; the correct fix for EM's and VISION's shared observation that the band admits 1.9608°.)*
7. **Propagate step-1 uncertainty into `SE(R_q)`.** Bootstrap step 1 (carrier period and `ψ̄`) and propagate into `SE(R_q)` and `SE(ΔP)`; additionally report `dR_q/dψ̄` and `R_i/R_q` per pair. All P-072-1 significance statements use the propagated SE. *(EM item 3 = VISION §3 = QUANTUM 5a, unified — see §2.)*
10. **Promote the wrong-carrier control to a gate, at a displaced carrier.** `RESOLVED` additionally requires `|R_q(T_wrong)| ≤ ½·|R_q(T_mean)|` **and** restricted-null Holm-adjusted `p(T_wrong) > 0.01`, with `T_wrong` fixed at **3.60°** (≥1.5 Rayleigh widths from the carrier), pre-registered here. The 1.9608° run is retained as **mandatory disclosure explicitly labelled a resolution identity, not a control** (0.6452 Rayleigh widths). *(EM's flip, modified per QUANTUM 5a — Attack 9.)*
11. **Add QUANTUM's model-strain flag.** Report `|R_i|·σ_u/a` in P-072-6 alongside the other three channels, with a disclosed non-gating strain flag when it exceeds `|R_q|·σ_u/a`. Verified to fire at three of four pairs. *(QUANTUM 5b — Attack 8.)*
12. **Report ΔP and its propagated SE at all four carriers — `T_mean`, each pair's `T_delta`, 1.9608°, and 3.60° — in P-072-1, for every pair, regardless of outcome**, with a sentence stating that sign is not invariant across the set and citing this as a measured limitation of the window. VISION's sign-invariance *conjunct* is not adopted; VISION's *table* is. *(VISION items 1–2, adjudicated — Attack 10.)*
15. **Add MATERIALS' curvature column** `u²·(−sin θ_c)` as a sixth, disclosed, non-gating column, reporting its coefficient and the 6-column condition number. A pure `Δf` predicts zero; an angle-dependent boundary-reflection phase does not. *(MATERIALS item 3.)*

**C. Constants, bands, closure (Attacks 5, 6, 7)**

8. **Strip P-072-3 from the `CONFIRMED` conjunction and relabel it a basis-stability check with `ρ_c ≤ 0.05`.** Strike "the design's strongest internal falsifier." Report the measured `R_q` telescoping residual at a common carrier (3.79%) as the calibration that justifies the band. *(EM item 2 + QUANTUM 5c + VISION §5 — Attack 7.)*
9. **Re-anchor `m₀` to the committed OLS slope, read from the JSON at runtime.** `run.py` loads `experiments/071-t28-absorb-depth-causal-test/results.json → trend.linear_fit.slope` (0.0025563909774436134); **no slope constant may be typed into any file.** Add a one-line note that the proposal's `0.00244361` was the C40→C80 endpoint chord, not the linear fit, and carried the linear fit's R². Recompute every §2c power figure from the loaded value. Then, per MATERIALS 2 and THERMO's flip: score resolved rates against **both** the linear `m₀` ramp and an engine-derived saturating model (decay constant fixed at `_damping`'s own 0.075/cell, not fitted); demote the `[m₀/10, 10m₀]` rate-window REFUTE clause to disclosed; retain the sign-reversal REFUTE clause (`ΔP < 0` with `|ΔP| ≥ 0.010°`) as the only gating rate clause. **Verified outcome-inert this cycle** — P-072-4 cannot reach its ≥2-`RESOLVED` precondition under either null. *(MATERIALS 1–2 + THERMO flip — Attacks 5–6.)*

**D. Disclosure and scope (Attacks 6, 11; THERMO §3–4; VISION §4)**

13. **Disclosure block, all of the following, one to two sentences each:**
 - Extend the "`ABSORB`-or-`PAD`-tied, never `ABSORB`-tied" writing rule **verbatim to P-072-1 and P-072-6**, binding under every verdict including NEITHER; state that P-072-6 supplies the confounded arm of Iteration-49 queue item 2 and does not substitute for it. *(THERMO §3.)*
 - Per QUANTUM 5a, any CONFIRM-shaped language must read "`ABSORB`-or-`PAD`-tied **frequency-or-fringe-weight** change," and Idealization 4 must concede the mixture is **non-identifiable** in this window, not merely present.
 - At `n_grid=3000` the C70/C80 order **reverses** (2.53551 vs 2.53051); Iteration 48's "smooth rise" and `m₀` rest on a broken tie. One sentence in §2c, one in Idealization 6. *(VISION 0a.)*
 - §1's C70≡C80 attribution must state that genuine saturation is an equally live reading of the same node collision, and that the `P(ABSORB)` curvature is zero-cost partial information on the standing PAD confound. *(MATERIALS 4.)*
 - Window provenance: the 31-point 36.0°–42.0° grid was inherited from Block MINI and **T28 was discovered inside it**; all p-values are conditional on this window and are not corrected across the ~12 statistics now computed on these same points across exp-069/071/072. *(VISION 4b/5.)*
 - `C_empty` is a dimensionless field ratio, not a Michelson/Weber contrast; `ptp/mean = 16.2` is a fit-conditioning statistic, not a perceptual or photometric contrast — wherever `ptp/mean` appears next to a ΔP. *(VISION §1.)*
 - §7 states explicitly that no absorbed-power number is produced and THERMODYNAMICS' energy sidecar is therefore N/A — deferral by argument, not by omission. *(THERMO §2, house precedent Iteration 5.)*
 - Name Iteration-49 queue item 4 (PHOTONICS' two-tone joint fit) and re-defer it with a stated reason; P-072-5 is a single-carrier contamination diagnostic, not a two-tone joint fit. *(THERMO §4.)*
 - The §4 pre-registration disclosure paragraph, verbatim per that ruling's condition 4, plus the `CONFIRM_UNCERTIFIED` rule per condition 3.

---

## 7. What this cycle should expect to publish

Under the fixed design, on the data as it stands, no pair is `RESOLVED`, P-072-3 is `NOT_EVALUABLE`, P-072-4 is `NEITHER`, and the Combined Verdict is `NEITHER` — reported, per house discipline, as a finding with its own sentence rather than a deferral. Red Team states that here, in advance, because §4's disclosure ruling requires it and because the finding is a real one: **the differential estimator's reach in this window is bounded not by the noise floor §2c anticipated, but by the identifiability of `R_q` against an unresolved second contributor and against its own carrier — a limit the absolute-period route never even got close enough to encounter.** VISION reached that sentence first and it is the right one. It is a genuine advance on Iteration 48, and it is worth more than the `REFUTED` the unfixed design would have printed.
