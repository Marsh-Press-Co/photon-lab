# PHASE 2 — CRITIQUE · VISION SCIENCE · Panel Iteration 49 · exp-072

*Fresh sub-agent, VISION SCIENCE charter (PANEL.md seat 6): human perceptual limits — contrast thresholds, luminance edge detection, spectral sensitivity, adaptation, temporal sensitivity, saccadic/attentional blindness. Blind to the other seats' Phase-2 critiques this cycle. T1 N/A; constraint 3 not engaged; no perceptual threshold is scored here, so my charter duty this cycle is (a) confirm no perceptual claim is smuggled in, and (b) discharge my documented house role on window discipline and measurement reuse, which PLAN.md's Iteration-49 queue item 5 made a binding constraint on this cycle. Every number below was recomputed by me from the committed JSON, not taken from any document's prose.*

---

## 0. Verification performed

Loaded `experiments/069-.../results.json` → `block_dense.rows` and `experiments/071-.../results.json` → `dense_causal.rows.C60/.C70` directly and re-ran the proposal's own estimator as specified in §2b.

- **θ grid identity (G0-a) holds.** All three sources: 36.0°–42.0°, 0.2° step, 31 points, bit-identical. G0-b/G0-c will pass. The proposal's data plumbing is sound.
- **`ptp/|mean| = 16.200` for `C80−C40` reproduces exactly.** Also computed for the new pairs: 44.910 (C40–C60), 9.922 (C60–C70), 9.305 (C70–C80).
- **Per-config free periods at `n_grid=3000`** (the proposal's own refinement): C40 **2.43748**, C60 **2.52051**, C70 **2.53551**, C80 **2.53051**.
- **Design-matrix condition number ≈ 60** for every pair — G0-d (`cond ≤ 100`) passes and will not catch anything below.

Two findings fall directly out of this and are load-bearing for §3 and §6.

### 0a. The `n_grid=3000` refinement breaks Iteration 48's monotonicity, and the proposal does not say so

§1 correctly identifies that exp-069's `n_grid=400` put C70 and C80 on the **identical** grid node (both 2.5338°), and correctly calls that a quantization artifact. But it then asserts the finer grid "**adds no resolving power**, and the Rayleigh limit of §2c is untouched by it" (idealization 6) — and carries Iteration 48's `m₀ = 0.00244361 °/cell` forward as P-072-4's reference slope. At `n_grid=3000` the tie resolves as **C70 (2.53551) > C80 (2.53051)**: the order **reverses**. Iteration 48's headline "periods rise smoothly with `ABSORB` depth" is, at the grid resolution this proposal itself adopts, **not monotone**. The reversal is 0.2% — far inside Rayleigh, i.e. noise — which is exactly the point: the monotonicity was never established, and `m₀` (and therefore P-072-4's entire `[m₀/3, 3m₀]` band) is derived from four numbers one of which was a tie the proposal has now broken in the opposite direction. This is one sentence of disclosure, not a redesign, but it must be in the write-up.

### 0b. Recovered ΔP is not stable against the carrier choice

I ran §2b steps 1–4 verbatim at three carriers, **all of which pass the proposal's own §2c/P-072-2 carrier-consistency gate** (`|T_delta − T_mean|/T_mean ≤ 0.414`):

| Carrier | ΔP(40→60) | ΔP(60→70) | ΔP(70→80) | ΔP(40→80) | P-072-3 `ρ_c` |
|---|---|---|---|---|---|
| `T_mean` (proposal's choice) | **+0.0697°** (z=4.90) | +0.0085° (z=3.04) | **−0.0086°** (z=4.25) | +0.0668° (z=4.66) | 0.042 → **CONFIRM** |
| each pair's own `T_delta` | **−0.0001°** (z=0.00) | +0.0127° (z=1.89) | +0.0153° (z=1.80) | −0.0054° (z=0.19) | 6.17 → **REFUTE** |
| T21's 1.9608° (declared *wrong*) | +0.0092° (z=0.63) | **−0.0177°** (z=4.87) | −0.0080° (z=3.15) | −0.0175° (z=1.28) | 0.059 → **CONFIRM** |

Gate distances, for the record: `|T_delta − T_mean|/T_mean` = 0.124 / 0.162 / 0.254 / 0.141; `|1.9608 − T_mean|/T_mean` = 0.211 / 0.225 / 0.226 / 0.213. **All eight are inside 0.414.** The gate admits every carrier in the table.

---

## 1. Perceptual-claim scan — **clean**

I grepped the full proposal for `visib|percept|eye|see|seen|contrast|detect|legib|observ|naked|human|threshold|Weber|Michelson|glance|apparent`. Five hits, all benign:

- "beat-**detect**ion", "coefficient-**detect**ion" — signal-processing usage, correct.
- "**threshold**" (×2, §5) — pre-registered numeric gates, correct usage.
- "made `C80−C40` **legible** at `ptp/mean=16.2`" (§1) — a metaphor for statistical conspicuity, not a visibility claim. Acceptable, but see below.
- "checked programmatically, **not by eye**" (§2a) — this is *good* discipline and the opposite of a smuggled claim.

**No perceptual claim is made or scored anywhere in this proposal.** Nothing says or implies "this would/wouldn't be visible." My charter's central question is not engaged, and I confirm it stays that way.

**One forward-looking guard, non-blocking.** `C_empty` is named in T28's own thread text an "ambient-**contrast** metric." That word carries perceptual freight it does not earn here — `C_empty` is a dimensionless field ratio, not a Michelson or Weber contrast, and `ptp/|mean| = 16.2` is emphatically **not** a contrast ratio of 1620%. exp-069's own Phase-5 record already shows `mean = −0.000249`, i.e. the denominator is a near-zero-crossing quantity, so the ratio is large for reasons that have nothing to do with signal strength. If any pair's ΔP is ever quoted alongside a `ptp/mean` figure, one clause must state that this is a fit-conditioning statistic and not a perceptual or photometric contrast. Cheapest possible fix; prevents exactly the downstream miscitation my seat flagged in exp-071 Finding A.

---

## 2. Steel-man (≤150 words)

Three things here are better than "reuse the window again." (1) §2c does the arithmetic in the open: it computes the Rayleigh limit (41.4% minimum fractional separation), concedes the absolute-period route is dead at any achievable window, then **pre-registers** per-pair power — 15.0%/7.2%/7.2%/29.7% of carrier amplitude — with a fallback that *prohibits* quoting ΔP for underpowered pairs. That is precisely my seat's own discipline — pin the number before scoring against it — applied unprompted to instrument resolving power. (2) It names the most likely outcome in advance (two pairs resolve, two do not) and refuses to launder it as PARTIAL. (3) Idealization 2 forbids a sharper estimator lending false specificity to the confounded `ABSORB`/`PAD` axis. (4) A surrogate null is adopted where R5 does not require it. Zero FDTD: the reuse costs arithmetic, not spend.

*(135 words)*

---

## 3. Sharpest attack (≤150 words)

§2c re-justifies the window for the **conditioning of Δf**. It never re-justifies it for the **carrier the new estimator conditions on**. Step 2 holds `θ_c` fixed at `T_mean` — a period this window cannot pin to better than 41.4%. I ran the proposed estimator on the actual 124 points at three carriers, *all* of which pass the proposal's own carrier-consistency gate: `T_mean`, each pair's own `T_delta`, and T21's deliberately-wrong 1.9608°. ΔP(40→60) is **+0.0697° at z=4.90** under `T_mean` and **−0.0001° at z=0.00** under `T_delta`. ΔP(60→70) is +0.0085° under `T_mean` and **−0.0177° at z=4.87** under the wrong carrier. Sign, magnitude, and significance of the headline discriminator are set by a nuisance choice the window cannot adjudicate, not by the data. The Rayleigh problem was not defeated — it was **relocated** from the scored parameter into a fixed, unreported one.

*(147 words)*

---

## 4. Window-discipline ruling (my house role, per PLAN.md Iteration-49 item 5)

My exp-071 Phase-5 guidance was: *"Do not re-run the identical 36°–42° window a third time"* — scoped to "before any new FDTD dense-sweep repeats this test," and narrowed by Red Team's queue reconciliation to "for an **absolute-period** discriminator."

**Letter of the constraint: satisfied.** This is zero-FDTD, spends no calls, and the discriminator is differential, not absolute. Queue item 5 explicitly anticipated that item 1 "already substantially satisfie[s]" the guidance. I do not object on that basis, and I say so plainly so no later reader mistakes my verdict for a jurisdictional one.

**Spirit of the constraint: two-thirds satisfied.** The reuse argument in §2c is honest and specific where it engages, which is more than "we reused it because it's there." Two gaps remain:

### 4a. The re-justification covers the target parameter but not the nuisance parameter

This is §3, stated as a discipline finding rather than a numeric one. My original guidance's core was: *the window's resolving power must be pinned in code before it is scored against.* §2c pins it for `Δf` and concludes correctly that `Δf` is not subject to the Rayleigh criterion. It does not pin it for `T_mean` — which **is** subject to that criterion, is held **fixed** through step 2, and which §0b shows determines the answer. A window justified for one estimand is not thereby justified for a different one that the same estimator quietly depends on. The proposal's instinct is right; its audit perimeter is one parameter too small.

### 4b. Accumulated looks are not priced, and the surrogate null structurally cannot price them

The 31 θ-values at 36.0°–42.0°/0.2° were inherited from Block MINI (exp-069 `phase1_proposal.md` §3 idealization 3: *"matching Block MINI's own original"*), and **T28 was discovered inside them**. This proposal never states that provenance, and it should, in one sentence.

Statistics computed on this identical 31-point grid now number: exp-069's `ptp/mean`, its fixed-period fit, and its free-period search; exp-071's four per-config free-period fits; and now exp-072's four carrier searches plus four ramp fits. Holm–Bonferroni (§3) corrects across **4 pairs within this cycle**. Nothing corrects across the cycles. The `p ≤ 0.01` bar in P-072-2 is calibrated as though this were a first look at these points; it is roughly the twelfth.

The surrogate null cannot help here, and it is worth being precise about why: Fourier-phase randomization **preserves the amplitude spectrum of `delta_AB` over this exact window**. It therefore conditions on the window and asks only "given these 31 points, is the ramped-quadrature phase structure special?" That is the right question for residual correlation — and I endorse adopting it where R5 does not compel it — but it is *definitionally blind* to whether these 31 points were the ones where the effect looked strongest. A control that holds the window fixed cannot audit the window.

**Neither gap requires new FDTD, and neither is fatal.** Both are disclosure-and-gating changes.

### 4c. What the reuse does *not* do wrong

For completeness, since my seat's guidance is the one being tested: the proposal does **not** re-tune the window, the center (`center_deg=39.0`), the step, or the `[1°,4°]` search span to suit the new estimator. Everything except `n_grid` is inherited unchanged and stated. The one change (`n_grid` 400→3000) is disclosed with a correct rationale. That is the honest form of reuse, and it is why my verdict is not "oppose."

---

## 5. Secondary: P-072-3 is advertised as the strongest internal falsifier and is close to an arithmetic tautology

§5 asserts: *"the raw series telescope by arithmetic (G0-b), but the recovered `ΔP` estimates do **not** — each pair is fit at its own `T_mean`, `a`, `ψ̄`, so closure is a genuine, non-trivial test."*

The `T_mean` values are 2.4865 / 2.5285 / 2.5325 / 2.4905 — they span 1.9%. At carriers that similar, the step-2 basis is nearly identical across pairs, and OLS is linear in `y`, so `R_q` nearly telescopes for the same reason the raw series exactly does. Measured: at the identical-carrier limit (all four pairs at 1.9608°) the `R_q` telescoping residual is **3.8%** of `R_q(40→80)`, non-zero only because `ψ̄` differs slightly per pair.

The consequence is visible in §0b's last column. `ρ_c = 0.042` at `T_mean` and `ρ_c = 0.059` at the **deliberately wrong** T21 carrier — both far inside CONFIRM's `≤ 0.25`. P-072-3 **CONFIRMs on a carrier the proposal itself calls wrong.** It only fires REFUTE (`ρ_c = 6.17`) under `T_delta`, where the per-pair carriers genuinely diverge (2.79/2.94/3.18°). So P-072-3 does not test model linearity or common-mode cancellation; it tests **whether the four `T_mean` values came out similar**, which they were always going to. Calling it "the design's strongest internal falsifier" overstates its power by a wide margin. Demote the language, or re-derive a closure statistic that is not near-linear in the same data.

Related, and worth one line in the write-up: my `T_mean` run gives ΔP(70→80) = **−0.0086°**, a sign reversal sitting just under P-072-4's REFUTE threshold of `|ΔP| ≥ 0.010°`. Combined with §0a's `n_grid=3000` order reversal at exactly that pair, the threshold has landed within 15% of the actual value. That is not a defect — the threshold is pre-registered and must not move — but the report must state that P-072-4's NEITHER was a near miss on a specific pair, not a comfortable one.

---

## 6. Verdict: **SUPPORT-WITH-CHANGES**

The physics reasoning in §1 is sound, the honesty in §2c is exemplary and is the standard I want other cycles held to, the perceptual-claim perimeter is clean (§1), and the zero-cost reuse is legitimate under my own seat's guidance as Red Team narrowed it (§4). I am not opposing a well-argued desk-only re-analysis over a fixable identification gap.

But as written, the proposal can report `RESOLVED` with `p ≤ 0.01` and CONFIRM P-072-3 on a quantity whose sign is set by an unresolvable nuisance choice — and its own designated contamination control (P-072-5) is **explicitly non-gating**, so the design would detect this and score around it. Requested changes, in priority order:

1. **Promote P-072-5 from "disclosed, non-gating" to a hard gate**, and add each pair's own `T_delta` to its carrier set alongside T21's 1.9608°. (The flip condition — see §7.)
2. **Report `SE(ΔP)` and `ΔP` at all three carriers in P-072-1's table**, not only at `T_mean`. Zero extra cost; three more `lstsq` calls per pair.
3. **Disclose §0a**: at the `n_grid=3000` the proposal itself adopts, the C70/C80 order reverses, so Iteration 48's monotonicity — and `m₀`, P-072-4's reference — rest on a broken tie. One sentence in §2c and one in idealization 6.
4. **Demote P-072-3's "strongest internal falsifier" language** (§5) and state its measured near-tautology, or replace the statistic.
5. **State the window's provenance** in one sentence — inherited from Block MINI, T28 discovered inside it — and add one sentence to P-072-1 stating that all p-values are **conditional on this window** and are not corrected for the ~12 statistics now computed on these same 31 points across exp-069/071/072. Not a numeric correction; a citation guard, in the shape of exp-070's `caveat_lint_config.json` precedent.
6. **The `C_empty`-is-not-a-perceptual-contrast clause** (§1), wherever `ptp/mean` appears next to a ΔP.

None of these requires an FDTD call, a `lab/` diff, or a `VALIDATION.md` re-run. Items 3–6 are prose. Item 1–2 are under a minute of added compute inside a budget of "< 60 s."

---

## 7. The single parameter change that would flip my verdict to **SUPPORT**

Add one conjunct to P-072-2's `RESOLVED` definition, pre-registered before any computation:

> **`RESOLVED` additionally requires `sign(ΔP)` to be invariant across the carrier set `{T_mean, T_delta, 1.9608°}`**, all three of which lie inside the existing `≤ 0.414` carrier-consistency band, with all three ΔP values and their `SE`s published in P-072-1 regardless of outcome.

This is one added condition on an existing gate, using carriers the proposal already computes (`T_delta` in step 5, 1.9608° in P-072-5). It costs nothing and it converts the design's blind spot into a measurement.

I should be explicit about what it would do on the real data, since I have run it: **on my numbers, no pair survives it.** ΔP(40→60) is +0.0697 / −0.0001 / +0.0092; ΔP(60→70) is +0.0085 / +0.0127 / −0.0177; ΔP(70→80) is −0.0086 / +0.0153 / −0.0080; ΔP(40→80) is +0.0668 / −0.0054 / −0.0175. Every pair changes sign somewhere in the band. Under the §2c fallback that would force P-072-3 to `NOT_EVALUABLE`, P-072-4 to NEITHER, and the Combined Verdict to NEITHER — with the reported finding being *"the differential estimator's reach in this window is limited not by the noise floor §2c anticipated but by carrier identification, which this window cannot supply at any pair separation."*

That is a **sharper, more useful, and more honest** result than the one the current design would produce, and it is a genuine advance on Iteration 48 rather than a repeat of it. It also discharges the substance of my window-discipline guidance properly: it makes the window's actual limitation the finding, instead of letting a reused window silently pick the sign of the answer.
