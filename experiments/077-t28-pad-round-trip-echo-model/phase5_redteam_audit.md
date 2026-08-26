# PHASE 5 — RED TEAM FINAL AUDIT · Panel Iteration 54 · exp-077
## Adjudicating all six blind Phase-5 reviews of the `PAD` round-trip echo refit, ruling on a two-cycle-old dimensional error now embedded in LOGBOOK's permanent record, and reconciling six Iteration-55 candidate rankings into one

**Seat: RED TEAM.** Read `PANEL.md` in full; `LOGBOOK.md` lines 1–270
(RULED OUT R1–R8), lines 820–935 (T16 in full), lines 1892–2461 (T28's
complete Iteration 46–53 history), and the Checkpoint criteria. Read the
complete exp-077 record in order: `phase1_proposal.md`,
`phase2_critique_{photonics,materials,em,thermodynamics,quantum}.md`,
`phase2_redteam_audit.md`, `phase3_synthesis.md`, `phase4_results.md`,
`NOTES.md`, `pad_round_trip_model.py`, `pad_round_trip_results.json`, and
all six blind `phase5_review_*.md`. This is Phase 5's final audit: I alone
see everything — the official record and all six blind reviews — and speak
last.

---

## 0. What I independently verified this cycle (zero new FDTD, per scope)

I did not rule on any load-bearing claim above without checking it myself.

1. **Re-ran `pad_round_trip_model.py` end-to-end.** Bit-identical to the
   committed JSON and to `phase4_results.md`'s tables throughout
   (single-wall `rel_dev`=1.8798/0.9642, `r²`=0.0444/0.1997; two-wall
   `rel_dev`=0.8797/0.6851, `r²`=0.0001/0.0418; gates G-LOSSLESS
   `2.220e-16`, G-N1 `1.404e-15`, G-PASSIVITY worst `|r|=0.006423`; null
   calibration `P(R²≥0.70)=0.0/20000`, bootstrap `100.0%` within 20%).
2. **VISION's dimensional-error claim (the highest-priority item) —
   CONFIRMED, bit-exact, from raw primitives, not from either party's
   prose.** Traced `amp_ratio`'s definition to source: `experiments/072-.../
   run.py:172` (`amp = math.hypot(fit["a"], fit["b"])`, the fitted
   common-mode-carrier amplitude, itself in `C_empty` units) and `:301-303`
   (channel ratios normalized by that same `amp`); confirmed
   `experiments/076-.../run.py:526-527` computes `amp_ratio = hypot(A_i,
   A_q) / amplitude` — a ratio of two same-unit (`C_empty`-scale)
   quantities, hence itself **dimensionless**. Recomputed independently
   from `experiments/076-.../results.json::headline`:
   ```
   pair_pad:      A_i=6.0811e-4  A_q=-9.3774e-5  amplitude=5.15476e-3
                  raw = hypot(A_i,A_q) = 6.1530e-4   amp_ratio = 0.119366  (exact)
   pair_absorb40: A_i=1.5144e-4  A_q=-3.6468e-4  amplitude=5.51382e-3
                  raw = hypot(A_i,A_q) = 3.9488e-4   amp_ratio = 0.071616  (exact)
   ```
   Confirmed `C_thr=0.005` is used elsewhere in this program as a threshold
   on **raw** `C_empty`/Weber-contrast magnitude, not on any pre-normalized
   ratio (LOGBOOK.md line 1363: `"|C_empty|=0.004855, just under VISION's
   own C_thr=0.005"` — a raw magnitude compared directly). The
   dimensionally-consistent comparison is therefore `raw/C_thr`, not
   `amp_ratio/C_thr`:
   ```
   raw_pad / C_thr      = 6.1530e-4 / 0.005 = 0.12306   (≈8x BELOW C_thr)
   raw_absorb40 / C_thr  = 3.9488e-4 / 0.005 = 0.07898   (≈13x BELOW C_thr)
   ```
   These match VISION's own cited `0.123×`/`0.079×` exactly. **VISION's
   finding is correct: `amp_ratio(PAIR_PAD)=0.119` is a fitted-carrier-
   normalized fraction, not a `C_empty`-scale magnitude, and it is not "24×
   `C_thr`" — the raw signal is roughly 8× *below* `C_thr`, not 24× above
   it.** See §2 for why this is more than a documentation nit.
3. **MATERIALS' realizable-admittance sensitivity — CONFIRMED bit-exact.**
   Re-derived `boundary_reflectance.py::reflection_coefficient`'s matched
   admittance (`Z = n(x)/√(n(x)²−sin²θ)`) and built the alternate,
   realizable (`mu_r=1`) TE admittance (`Z' = 1/√(n(x)²−sin²θ)`) myself,
   ran both through the identical recursive transfer-matrix recursion at
   `ABSORB=40`:
   ```
   θ=36°: matched |r|=0.0029 arg=-78.12°   real |r|=0.0041 arg=-102.78°   ratio=1.402
   θ=39°: matched |r|=0.0043 arg=-40.91°   real |r|=0.0053 arg=-63.38°    ratio=1.251
   θ=42°: matched |r|=0.0064 arg=-1.23°    real |r|=0.0074 arg=-19.48°    ratio=1.151
   ```
   Matches MATERIALS' cited table exactly (my matched column reproduces
   §2e's committed table first, confirming methodology, before trusting
   the comparison column). MATERIALS' claim stands: swapping only the
   realizability-blocking assumption moves `|r|` by 15–40% and `arg(r)` by
   15–24° — a real, quantified, unpriced sensitivity.
4. **PHOTONICS' 750nm two-wall flip — CONFIRMED, independently
   re-implemented from scratch (own script, not PHOTONICS' or anyone
   else's).** Retargeted `two_wall_cavity.py::c_empty_two_wall` at
   `CPL[750]=25` against `experiments/076-.../results.json::leg750_scored`
   (`(C40,G40)`, 16 points, 38.0–41.0°):
   ```
   P*_real=3.8271° (R²=0.9884)   P*_model=4.1611° (R²=0.9788)
   rel_dev=0.08729 -> well inside SUPPORT (<=0.30)
   shape r=-0.5004, r²=0.2504 -> INCONCLUSIVE (sign flips vs 600nm's +0.0097)
   Combined: INCONCLUSIVE (600nm's two-wall Combined was REFUTE)
   ```
   Matches PHOTONICS' cited numbers to the digit. Confirmed real.
5. **QUANTUM's lag-1 autocorrelation (0.6307) — CONFIRMED, after
   discovering my own first attempt used the wrong estimator.** My first
   pass (a plain Pearson correlation between `resid[:-1]` and `resid[1:]`)
   gave 0.731, not 0.6307 — a discrepancy I did not let stand
   unresolved (R4's own discipline, applied to my own check, not just to
   others'). The correct, standard ACF estimator (`Σrᵢrᵢ₊₁ / Σrᵢ²`, full-`n`
   normalization, not a pairwise-only Pearson coefficient) reproduces
   QUANTUM's `0.630747...` to six decimal places exactly, using the
   identical residual array the committed bootstrap resamples from.
   QUANTUM's finding is correct; my own naive first check would have
   wrongly disputed it had I not traced the discrepancy to its root.
6. **QUANTUM's dead-code claim (`rel_dev_gt1`) — CONFIRMED by direct
   source read.** `pad_round_trip_model.py:280` declares
   `rel_dev_gt1 = 0`, never incremented, never included in `out_a`
   (line 289's dict). `pad_round_trip_results.json::null_calibration_
   appendix.pure_noise_null` contains no `p_rel_dev_gt1` key. Confirmed:
   the raw-threshold-crossing half of the null-calibration table
   (`P(rel_dev>1.00)`, `P(shape r²≤0.05)`) that Red Team's own Phase-2
   audit (Attack 5) explicitly mandated ("both checks") was silently
   narrowed to the R²-only half during implementation.
7. **PHOTONICS' `clear_span_y` y-wall asymmetry — CONFIRMED bit-exact.**
   Imported `experiments/065-.../design_geometry.py::CONFIGS` directly:
   `clear_span_y` = 0 (`C40`), **40** (`G40`), 0 (`C80`) — `G40` alone has a
   40-cell standoff from the y-absorbing band that neither `C40` nor `C80`
   has. `load_pair_geometries()`'s own 7-field congruence assertion
   (`nx,ny,src_x,plane_x,obj_x,obj_y,d_sp`) does not include
   `clear_span_y` — confirmed by reading the assertion list directly.
   `PAIR_ABSORB40 ≡ (G40,C80)`, treated throughout this six-cycle
   sub-thread as "geometry-fixed, ABSORB-only," is **not** y-direction
   congruent.
8. **EM's "even in theta" claim — CONFIRMED bit-exact.**
   `reflection_coefficient(n40, +39.0°, CPL[600])` and the same call at
   `-39.0°` return the identical complex value
   (`0.003226−0.002796j`, exactly). The premise underlying both the
   single- and two-wall models (same `r(theta;ABSORB)` weights every
   wall) is exact by construction of the formula, not an approximation
   that happens to hold for this cycle's specific geometries.
9. **EM's energy-balance decomposition (§2b of the EM review)** — spot-
   checked for internal consistency (triangle-inequality bound, left-only
   term matching the filed single-wall `ptp` exactly) but **not**
   independently re-derived cell-by-cell by me; no seat contradicts it and
   it is not load-bearing to any verdict. Flagged as plausible, not
   independently bit-verified, consistent with this program's own
   disclosure standard.

No discrepancy found between any of the six blind reviews' load-bearing
numeric claims and either the committed record or my own from-scratch
recomputation, once I corrected my own estimator mismatch on item 5. All
six seats converged on **PARTIAL**; I concur.

---

## 1. Adjudication of the six reviews

| # | Seat | Finding | Verified? | Load-bearing? | Disposition |
|---|---|---|---|---|---|
| F1 | PHOTONICS | Two-wall model's shape mismatch is visible cycle-by-cycle (3 real zero-crossings vs 2 model); the already-collected 750nm leg flips the two-wall model to INCONCLUSIVE (Test A well inside SUPPORT, Test B sign-flips) — a real, outcome-relevant finding the Idealization-11 "out of scope" call should not leave silently deferred a further cycle; a genuinely new y-wall candidate (`clear_span_y` tracks `PAD`, invisible to the congruence check). | **CONFIRMED**, all three parts, independently reproduced from scratch (§0.4, §0.7). | **Yes, all three.** The 750nm flip changes the wavelength-generality status of the two-wall REFUTE; the y-wall gap is a genuine unpriced candidate. | **ADOPT in full.** See §2, §5, §6. |
| F2 | MATERIALS | Idealization 10's REFUTE says nothing about a *realizable* admittance instantiation of the same mechanism — only the unrealizable matched-`eps=mu` construct has been tested, twice; swapping to a real, `mu_r=1` admittance is quantitatively non-trivial against this cycle's own near-boundary margins. `graded_black_shell` is a concrete, zero-FDTD candidate profile. | **CONFIRMED bit-exact** (§0.3). | **Yes.** This is a real scoping gap in `NOTES.md`'s "doubly excluded" language. | **ADOPT in full.** See §2. |
| F3 | ELECTROMAGNETISM | The "same `r(theta)` for both walls" premise is exact by construction (dispersion relation + even-in-theta formula), not an approximation; the two-wall model's amplitude growth is energy-bookkeeping-clean (triangle-inequality bound respected); the y-direction walls are a genuinely distinct, untested boundary configuration sharing T21's own already-refuted reference length (`A=752`) as a caution, not yet a proposal to build. | **CONFIRMED**, the first-principles derivation bit-exact (§0.8); the energy decomposition plausibility-checked, not independently re-derived cell-by-cell (§0.9). | **Yes**, on the premise and the y-wall caution; the energy decomposition is corroborating, not itself load-bearing. | **ADOPT.** Converges with PHOTONICS (F1) on the y-wall candidate — see §2. |
| F4 | THERMODYNAMICS | The mechanism REFUTE is thermodynamically clean, and the corrected §3 sidecar reasoning holds up on independent re-derivation (own Attack-4-flagged Phase-2 arithmetic slip re-confirmed as a genuine, non-load-bearing slip). New finding: the T5/exp-043 microbolometer-NETD comparison (Idealization 12) mixes a witness-pinned absolute-watts detectability floor with a dimensionless, no-witness-wattage fractional reflectance delta — not commensurable as stated. Offers the correct, commensurable comparison instead (`Δ(absorbed fraction)/real signal ptp` ≈ 1.4e-3–6.6e-3). | **CONFIRMED.** Spot-checked the commensurability argument against `thermo_sidecar_check`'s own outputs (`delta_absorbed_frac` and `real_delta_absorb40`'s `ptp` both present in the committed JSON) — the ratio recomputes as stated. | **Yes**, but explicitly non-load-bearing (THERMODYNAMICS' own disposition, and mine): Tests A/B already REFUTE independently of this paragraph. | **ADOPT**, as a same-shift text correction, not urgent. |
| F5 | QUANTUM OPTICS | The committed null-calibration appendix reproduces the R²-separation half of what Red Team's own Phase-2 audit mandated, but silently drops the raw-threshold-crossing half (`P(rel_dev>1.00)`, `P(shape r²≤0.05)`) — a dead variable (`rel_dev_gt1`) is direct in-source evidence. Reconstructed the missing statistics (`P(rel_dev>1.00)≈0.15`, `P(shape r²≤0.05)≈0.77` at reduced scale). Also: the bootstrap resamples residuals i.i.d. despite a real lag-1 autocorrelation of 0.63 in the actual residuals — likely anti-conservative on the "100% within 20%" figure, the same failure shape `G0-e(ii)` (R6 addendum) was built to catch, though not outcome-determining here. | **CONFIRMED**, both halves, independently (§0.5, §0.6 — including catching and resolving my own estimator error on the autocorrelation figure before accepting it). | **Yes.** A real fidelity gap between what was mandated and what was delivered; non-outcome-determining but should not stand a second time. | **ADOPT in full.** See §5. |
| F6 | VISION SCIENCE | `x=amp_ratio(PAIR_PAD)=0.119` is not "~24× `C_thr`" — `amp_ratio` is a dimensionless ratio normalized by a fitted local carrier, not a raw `C_empty`-scale magnitude comparable to `C_thr`. The dimensionally-consistent comparison (raw `hypot(A_i,A_q)` vs `C_thr`) gives ≈0.12×/0.08× — sub-threshold, not 14–24× over it. This exact risk was self-disclosed once before (exp-076's own Idealization 11 and a draft warning in that cycle's own Phase-5 VISION review) and used anyway in that same document's own headline; Red Team's Iteration-53 audit "confirmed" only the arithmetic (`0.119366/0.005=23.87`), not whether `amp_ratio` was the right numerator, before mandating the figure into LOGBOOK's permanent T16 entry. | **CONFIRMED bit-exact** (§0.2), the single most consequential finding this cycle. | **Yes — the most consequential finding of Phase 5.** Does not change `PAD_TIED`'s classification or this cycle's REFUTE (neither depends on a `C_thr` comparison), but corrupts a headline urgency figure now sitting in LOGBOOK's permanent memory. | **ADOPT in full, and elevate to a Checkpoint ruling.** See §2. |

Nothing across the six reviews is overridden. Every load-bearing claim
independently reproduces; no critic overreached.

---

## 2. The two findings that require correcting how this cycle's own record — and LOGBOOK's T16 entry — should be read

### 2a. Does "the coherent-echo mechanism class... doubly excluded" (NOTES.md's own current language) need correcting? **Yes.**

Combining PHOTONICS'/EM's convergent y-wall finding (F1/F3) with MATERIALS'
realizability-scope finding (F2), independently confirmed at §0.3/§0.7/§0.8
above: what has actually been shown REFUTEd, twice, is narrower than
`NOTES.md`'s "Next" section states. Precisely:

- **What IS doubly excluded**: the **x-normal** (near + far wall)
  coherent-echo mechanism, tested only against the **unrealizable**
  matched-`eps=mu` admittance construction, at 600nm, on the single-wall
  cut (period-driven REFUTE) and the two-wall cut (shape-driven REFUTE).
  This is real, hard-won, and correctly reported as such.
- **What is NOT yet excluded, and is not merely hypothetical**:
  1. The **y-direction (transverse) wall echo** — a structurally distinct
     boundary configuration (different incidence-angle convention,
     different image geometry), confirmed to exist in the same admittance
     class and confirmed to track `PAD` exactly (`clear_span_y`: 0/40/0),
     invisible to this cycle's own congruence assertion. Never modeled by
     exp-075 or exp-077.
  2. A **realizable** (`mu_r=1`) admittance instantiation of the *same*
     x-wall mechanism just tested — confirmed to move `|r|`/`arg(r)` by
     15–40%/15–24°, a materially different transfer function from the one
     actually REFUTEd, never fit against Test A/B.
  3. (New, from VISION's own review, §4b, not yet independently verified
     by me but a coherent, concrete, zero-FDTD candidate): a **Yee-grid
     numerical-dispersion-corrected** version of the same x-wall model —
     the committed model uses vacuum phase velocity `c` for the round-trip
     phase; the FDTD engine's own discretized phase velocity has never
     been substituted in.
  4. The two-wall's own 600nm REFUTE does not survive unchanged to 750nm
     (F1, §0.4) — the mechanism's wavelength-generality is itself an open
     question, not settled.

`NOTES.md`'s "Next" section states: *"the coherent-echo mechanism class
now doubly excluded... the program may be approaching the point where NO
known mechanism class remains untested."* Read narrowly ("two REFUTEs have
now occurred"), this is literally true. Read as written, in context, it
overstates what has been shown — four concrete, unpriced candidates remain
on the board, three of them zero-FDTD. **This must be corrected, same-shift
(mandatory-fix docket, §5).** I do **not** rule this an independent
Checkpoint-4 firing: the sentence is explicitly framed as a question for
"an explicit Red Team reckoning next cycle" (i.e., this audit), not
asserted as a settled fact and defended — the mechanism designed to catch
premature closure claims (this final audit) is doing exactly its job by
resolving the question now, before it hardens. This matches the program's
own non-firing pattern (an open question flagged and then actually
adjudicated, not a false claim defended past the point it should have been
caught).

### 2b. Does VISION's dimensional-error finding fire Checkpoint criterion 4? **Yes — this is the live firing item this cycle.**

The task asks me to apply this program's own precedent test explicitly:
*was the error caught before or after propagating into a defended headline
claim across multiple cycles?* Tracing the full chain, independently
verified at every link:

1. **Iteration 53 (exp-076), Phase 2**: VISION's own critique that cycle
   flagged, as a self-labeled *secondary* (not sharpest) finding, that the
   `amp` normalizer sits within 3–10% of `C_thr` — a "future conflation
   risk." Disclosed, then dropped (absent from both the Phase-2 audit's
   disposition table and Phase 3's acceptance table) — Red Team's own
   Iteration-53 audit ruled this **non-firing** at the time, reasoning
   that the committed prose was "clean" (no `C_thr`/perceptual language
   anywhere in `phase4_results.md`/`NOTES.md`/`run.py`) and the risk was
   "latent, not live."
2. **Iteration 53, Phase 5**: a *different* fresh VISION sub-agent's
   Phase-5 review, in the same cycle, independently (a) re-drafted this
   exact warning in its own §2 ("a reader could plausibly misread '0.119'
   as '24× the lab detection bar'... when it has no perceptual referent at
   all"), **and, self-contradictorily, in its own §4** used the flawed
   framing as fact: *"a domain-padding choice... can move this channel's
   own signal by an amount ~24× VISION's own lab bar."* Nobody caught this
   internal contradiction within one document.
3. **Iteration 53's Red Team final audit** (the document I am extending)
   took up VISION's Phase-5 finding, independently recomputed the `amp`
   normalizer's proximity to `C_thr` (3.1%/10.3% above), and — in the same
   breath — wrote: *"confirming the 'within ~10%' and '~24×'
   (`x/C_thr=23.87`) figures both VISION reviews cite."* This "confirmation"
   checked only that `0.119366/0.005=23.87` is correct **arithmetic** — it
   never independently asked whether `amp_ratio` (a fitted-carrier-
   normalized fraction) was the right numerator to divide by `C_thr` (an
   absolute `C_empty`-scale threshold) in the first place. That audit's
   own **mandatory-fix docket item 4** then instructed: *"Add the T16
   cross-reference: log `PAD_TIED`... with the `x=0.119/C_thr=0.005`
   (~24×) figures attached, in LOGBOOK.md's T16 entry."* **Red Team itself
   is the party that wrote the flawed comparison into LOGBOOK's permanent
   record**, as an active editorial action following an incomplete
   verification pass — not a passive oversight that slipped through.
4. **LOGBOOK.md's T16 entry (Iteration 53)** now states, as settled
   record: *"a domain-padding choice ALONE... can move this channel's
   signal by `x=amp_ratio(PAIR_PAD)=0.119`... ~24× VISION's own pinned lab
   detection bar (`C_thr=0.005`)."*
5. **Iteration 54 (exp-077), this cycle's own task brief**, quotes this
   LOGBOOK passage verbatim as established background fact, handed to a
   fresh, independent VISION seat with no memory of Iteration 53's process.
   That seat traced `amp_ratio` back to its own defining primitives and
   caught the unit mismatch Red Team's own prior audit had missed despite
   performing an explicit "verification" pass on exactly this figure.

This is the program's own established **firing** shape, not its
non-firing one: the error was *not* caught by a blind critic before Phase
3 froze anything (Iteration 53's own non-firing ruling on the Phase-2
finding was correct **for that finding**, which was about the normalizer's
proximity to `C_thr`, a different and genuinely latent risk). What fires
here is a **different, later** event in the same chain: a defended claim
— actively re-verified and then written into LOGBOOK's permanent record by
Red Team's own mandatory-fix docket — survived across a full cycle
boundary (53→54) as settled fact, and it took a **second, independent**
blind Phase-5 seat, one full cycle later, to catch what the first
verification pass checked incompletely. This matches Iteration 52's own
language for a firing instance almost exactly: *"took blind Phase-5 seats
plus the final audit to surface,"* not *"caught by blind critics before
Phase 3 adopted it."* The fact that the checking party each time was Red
Team itself (rather than a Phase-2 critique or a Phase-3 synthesis) does
not exempt it — R8 already established that this program's own audit
layer is not above the standard it applies to everyone else.

This is also a genuinely new **variant** of a previously-named failure
shape, not a repeat of R4 or R8 verbatim: R4 targets hand-typed figures
that were never invoked from the committed function; R8 targets an
*unverified* robustness argument adopted without computation. Here, a
computation **was** run, and it was **correct** — the division
`0.119366/0.005=23.87` is not in dispute. What was never checked is
whether the two operands of that division belong on either side of it at
all. **I am proposing this as a candidate addendum, for the Director's
adoption in the LOGBOOK entry** (not unilaterally imposing a new numbered
rule, matching QUANTUM's own restraint standard from this cycle's Attack
5): *verifying that a cited ratio/comparison reproduces arithmetically is
not sufficient to verify the comparison's own claim — the operands'
commensurability (same units/normalization) must be independently
confirmed before a "confirmed" comparison is trusted, distinct from
confirming the arithmetic between them.*

**Ruling: CHECKPOINT CRITERION 4 FIRES.** Consistent with this program's
unbroken precedent (12 for 12, now including this instance — Iterations
49, 50, 52 fired; Iteration 53 correctly did not, on a different,
genuinely-latent finding), **this is ruled a notification, not a pause**:
no `lab/` diff, no frozen prediction of *this* cycle is touched, `PAD_TIED`'s
own classification and this cycle's REFUTE verdict are both independently
unaffected (neither depends on a `C_thr` comparison), and the remedy (a
LOGBOOK correction) is actionable without halting any other thread.

---

## 3. Combined Verdict for exp-077: **PARTIAL**

The specific mechanism this cycle set out to test — a coherent echo off
the domain's two x-normal PEC walls, weighted by the graded-loss band's
`r(theta;ABSORB)`, instantiated with the unrealizable matched-`eps=mu`
admittance — is **REFUTEd, robustly, confirmed five independent ways now**
(PHOTONICS' and EM's Phase-2 from-scratch two-wall retargets, Red Team's
own Phase-2 audit re-derivation, the official Phase-4 re-run, and this
final audit's own re-run, §0.1) for `PAIR_PAD`, the task's own primary
target, and — once the two-wall term is correctly included — for
`PAIR_ABSORB40`, the secondary control, too. This is real, well-earned
negative evidence and should stand as reported.

It is **not** RULED OUT, and it is not the closing of a mechanism class:
§2a's four unpriced candidates (y-wall echo, realizable-admittance
instantiation, Yee-grid-dispersion correction, unresolved 750nm
generality) mean the honest reading is "one specific, narrowly-scoped
instantiation of the coherent-echo class is dead; the class itself is not."
It is not PROMISING: nothing here points toward a positive mechanism
identification. **PARTIAL**, matching every one of the six blind reviews
independently.

---

## 4. Mandatory-fix docket (same-shift, zero new FDTD)

1. **[§2a, PHOTONICS/EM/MATERIALS]** Correct `NOTES.md`'s "Next" section:
   replace "the coherent-echo mechanism class now doubly excluded... no
   known mechanism class remains untested" with an explicit, scoped
   statement — the x-normal, unrealizable-admittance instantiation is
   REFUTEd twice; the y-wall echo, the realizable-admittance instantiation,
   and a Yee-grid-dispersion-corrected version of the same x-wall model
   remain untested and unpriced; the 750nm generality of the two-wall
   REFUTE is itself unresolved (F1). State plainly that a Checkpoint-2
   "mechanism board exhausted" reading is **not yet ripe** (§6 below rules
   this explicitly, so it need not be re-litigated next cycle).
2. **[F2, MATERIALS]** Amend Idealization 10 (or add Idealization 13):
   state that this cycle's REFUTE is a statement about the zero-free-
   parameter, matched-`eps=mu` instantiation only; a realizable (`mu_r=1`)
   admittance changes `|r|` by 15–40%/`arg(r)` by 15–24° (cite §0.3's
   table) and has never been fit against Test A/B.
3. **[F1, PHOTONICS]** Officially fold the 750nm two-wall spot-check
   (§0.4's numbers) into the committed record with its own explicit
   caveat (narrow 16-point/3° window, no dedicated null-calibration,
   4-parameter free-sinusoid fits at suspiciously high `R²` on both
   curves) — advisory, not a counter-finding, matching exp-076's own
   precedent caveat on this exact dataset. Recommend Idealization 11's
   "out of scope" framing be replaced with an explicit forward pointer to
   Iteration 55's own item 3 (§6 below), since it is now shown
   outcome-relevant, not merely deferred.
4. **[F5, QUANTUM]** Wire up or delete the dead `rel_dev_gt1` variable and
   report the full three-quantity pure-noise table
   (`P(rel_dev>1.00)`, `P(R²≥0.70)`, `P(shape r²≤0.05)`), not the R²-only
   half; re-run the bootstrap ground-truth-recovery check with a
   circular-shift or block-resampling scheme alongside the existing i.i.d.
   version (matching the `G0-e(ii)` precedent, R6 addendum) and report
   both, so "100% within 20%" is not read as more precise than the
   underlying i.i.d. assumption currently supports.
5. **[F4, THERMODYNAMICS]** Replace or supplement the T5/exp-043 NETD
   sentence in §3/Idealization 12 with the commensurable, same-instrument
   ratio (`Δ(absorbed fraction)/real signal ptp ≈ 1.4e-3–6.6e-3`),
   correctly labeled as an energy-scale plausibility check, not a
   detectability claim in T5's sense.
6. **[F6, VISION — the Checkpoint-4 item]** Correct LOGBOOK.md's T16 entry
   (Iteration 53 text): replace the "`x=amp_ratio(PAIR_PAD)=0.119`... ~24×
   VISION's own pinned lab detection bar" framing with the
   dimensionally-consistent comparison (`raw=hypot(A_i,A_q)` vs `C_thr`:
   `≈0.12×`/`≈0.08×` for `PAIR_PAD`/`PAIR_ABSORB40`, i.e. sub-threshold by
   roughly an order of magnitude, not 14–24× over it), citing this
   cycle's independent bit-exact re-verification (§0.2). This re-ranks
   `PAD_TIED`'s urgency within T16's own ledger downward, not upward — see
   §6, item 1.
7. **[§2b, this audit]** Add the proposed R4-adjacent addendum text (§2b's
   closing paragraph) to LOGBOOK's RULED-OUT/house-discipline section, for
   the Director's adoption, on the same footing R8 was adopted at
   Iteration 52 (Red Team's own ruling, stated in the Checkpoint entry).

None of these seven items touch `pad_round_trip_model.py`'s own frozen
Test A/B numbers, `lab/`, or the Combined Verdict — all are record-
completeness and LOGBOOK-correctness fixes, matching this program's own
established "catch and close same-shift" pattern.

---

## 5. Checkpoint ruling — all five criteria, explicit

1. **A configuration passes all constraint metrics.** N/A. T1/constraint-3
   is correctly disengaged throughout (§4 of the proposal, re-confirmed:
   zero absorber, zero scene, zero perceptual-threshold language anywhere
   in the committed record). **Does not fire.**
2. **A proven boundary within a mechanism class, gates clean.** This is
   the criterion three seats (PHOTONICS, QUANTUM, and implicitly EM) asked
   me to rule on explicitly, given `NOTES.md`'s own "approaching the point
   where no known mechanism class remains untested" language. Per §2a
   above, that reading does **not** survive: at least four concrete,
   unpriced candidates remain (y-wall echo, realizable-admittance
   instantiation, Yee-grid-dispersion correction, unresolved 750nm
   generality), three of them zero-FDTD and cheap to run next cycle. **Does
   not fire — explicitly not yet ripe**, matching PHOTONICS' own §4 item 3
   recommendation. This closes the open question `NOTES.md` deferred to
   this audit; it should not be re-litigated at Iteration 55 without new
   information from items 1–3 of §6 below.
3. **Synthesis requires engine physics beyond the validated bench classes.**
   No engine change; zero new FDTD; `Sim`, `boundary_reflectance.py`,
   `two_wall_cavity.py`, `_free_period_search` are all reused unchanged.
   VISION's Yee-grid-dispersion candidate (§2a item 3) would use the
   engine's *own already-existing* dispersion relation as a closed-form
   correction to an existing model, not a new engine capability. **Does
   not fire.**
4. **Program-integrity drift.** Assessed in full at §2b above. **FIRES** —
   a claim Red Team's own prior audit actively verified (incompletely) and
   wrote into LOGBOOK's permanent record survived across a full cycle
   boundary as settled fact, and was caught only by an independent blind
   Phase-5 seat one cycle later — this program's own established firing
   shape. **Ruled a notification, not a pause** (12th consecutive instance
   of this program's unbroken "notification, not pause" precedent):
   nothing in this cycle's own `lab/` state, frozen predictions, or
   Combined Verdict is touched; the remedy (mandatory-fix docket item 6,
   a LOGBOOK text correction) is actionable without halting any other
   thread. A candidate rule addendum is proposed (§2b, docket item 7) for
   the Director's adoption, not unilaterally imposed.
5. **Two consecutive iterations with no logbook-advancing result.**
   Iteration 53 (exp-076, `PAD_TIED` plus the lossless-vacuum proof) and
   Iteration 54 (exp-077, two mechanism REFUTEs on the complete
   instrument, plus the y-wall/realizability/dimensional-error findings
   this audit adds) are both genuine, independently-verified advances.
   **Does not fire.**

**Net: Checkpoint criterion 4 fires, notification only; criteria 1, 2, 3,
5 do not fire.** This is the second consecutive T28 cycle in which
criterion 4 fires (Iteration 52 also fired, on a different failure shape —
an unverified robustness argument, R8's original trigger); Iteration 53
did not fire. The recurrence is on a *new* variant (§2b's proposed
addendum), not a repeat of R8's own exact shape, and should be read as
such rather than as evidence R8 failed to close the gap it was built for.

---

## 6. Reconciled Iteration-55 ranking (all six seats + this audit)

Six seats' top picks converge more than they diverge this cycle: PHOTONICS
and EM independently rank the y-wall pre-screen #1; MATERIALS ranks the
realizable-admittance refit #1; VISION ranks the T16 correction #1 (by
cost, trivially) and adds a genuinely new zero-FDTD candidate (Yee-grid
dispersion) at #2; QUANTUM ranks hardening the null-calibration appendix
#1. Reconciled by information-density per unit cost, zero-FDTD desk items
first (this program's own established Tier-0 practice):

### Tier 0 — zero FDTD, desk-only, run as one batch

1. **Correct the T16 "24×" framing (VISION, F6/§2b/§4 item 6).** Trivial,
   zero cost, two cycles overdue, and the one item on this list that is
   purely a correctness fix rather than a new test — run it first so no
   further cycle inherits the error as settled fact.
2. **A closed-form period pre-screen of the y-direction (transverse) wall
   echo, before building any new image-geometry code** (PHOTONICS #1, EM
   #1, independently convergent). Derive the correct grazing-incidence
   period formula for a wall whose normal is transverse to the beam's
   principal axis (not a copy of `closed_form_period`, which assumes an
   x-normal wall), evaluate at `A=752` and at each config's actual
   aperture-to-wall distance, and compare to T28's established
   `P*≈2.84°`/`4.2–4.6°` periods. EM's own caution, independently arrived
   at: `A=752` is the *same* reference length T21's own already-refuted
   edge-diffraction fringe model uses — if the y-wall period lands close
   to T21's `1.96°`, this sub-mechanism can likely be desk-closed in under
   an hour without ever building the full y-mirrored propagator.
3. **The realizable-admittance refit** (MATERIALS #1). Map
   `graded_black_shell`'s already-characterized `eps_r(x)`/`sigma_e(x)`
   profile onto a complex `n(x)`, swap in the standard (`mu_r=1`) TE
   admittance in place of the matched one, re-score Test A/B against the
   same already-collected `PAIR_PAD`/`PAIR_ABSORB40` data. Zero new FDTD;
   the only pending test that can move MATERIALS' realizability bound in
   either direction — the two-wall extension this cycle explicitly could
   not (Idealization 10).
4. **Gate the 750nm two-wall spot-check with a null sized for its own
   16-point/3° window, and decide** (PHOTONICS #2, EM #2). If the
   INCONCLUSIVE flip survives calibration, the 600nm-only REFUTE needs an
   explicit wavelength-generality caveat; if it doesn't survive, that
   itself is worth stating plainly rather than leaving Idealization 11
   deferred a further cycle.
5. **The Yee-grid-numerical-dispersion-corrected re-score** (VISION #2,
   new this cycle, not independently verified by me but concrete and
   cheap). Recompute `boundary_reflectance.py`'s round-trip phase using
   the engine's own closed-form 2D FDTD dispersion relation at
   `cells_per_lambda=20`, `courant_frac=0.99`, instead of vacuum `c`, and
   re-run Test A/B. Distinguishes "the physics is dead" from "the model's
   assumed phase velocity was wrong" — a distinction nothing so far has
   made.
6. **Harden the null-calibration appendix** (QUANTUM #1). Wire up or
   delete `rel_dev_gt1`; add a circular-shift/block-resampling bootstrap
   alongside the i.i.d. one. Already in the mandatory-fix docket (§4 item
   4); listed here too because it belongs in the same zero-FDTD batch.

### Tier 1 — cheap FDTD, next

7. **The full-width, non-aliased second-wavelength (`G40`) leg** (QUANTUM
   #2, near-unanimous standing precondition since Iteration 53, deferred
   twice: exp-076, exp-077). Now the cheapest remaining FDTD test of
   whether T28's periodicity is a real, wavelength-scaling-consistent
   physical effect at all — ranked below Tier 0 specifically because items
   2–5 above should decide which configuration/mechanism is worth the
   spend, not because it is less important.
8. **Broadband pulsed reflectance spectroscopy of the `ABSORB` boundary**
   (THERMODYNAMICS #2, carried from Iteration 53's own Tier 1). A genuinely
   orthogonal instrument class (measured, not transfer-matrix-proxy,
   absorbed power vs. frequency) — cheap, and closes THERMODYNAMICS' own
   "post-run analytic calculation only" gap for the first time in this
   sub-thread's history.

### Tier 2 — the standing charter-relevant test

9. **Test whether the `PAD`-sensitivity survives with a real absorbing
   article loaded** (THERMODYNAMICS #3, VISION #3, deferred twice:
   exp-076, exp-077). The only item that reconnects T28's now seven-cycle-
   deep instrument-diagnostic work to a real constraint-3 scene, and the
   precondition for THERMODYNAMICS' own sidecar to attach to a real,
   witness-relevant absorbed-power number for the first time. Ranked
   behind Tier 0/1 because its interpretation benefits from items 2–3/7
   already being in hand (a mechanism candidate and a wavelength-general
   reading both sharpen what "survives loading" would mean) — not because
   VISION's own charter question is unimportant; it is the most-deferred
   item on this board and should not be deferred a third time without an
   explicit reason next cycle.

### Tier 3 — record hygiene (bundle, zero cost, run alongside any of the above)

10. This audit's own mandatory-fix docket (§4, items 1–7 in full).

None of the above re-opens or re-proposes any RULED-OUT item (R1–R8); the
y-wall and realizable-admittance candidates are new instances of the
already-permitted coherent-echo mechanism class applied to configurations
neither exp-075 nor exp-077 tested, not resurrections of anything closed.

---

## 7. Bottom line

**Verdict: PARTIAL** — unanimous across all six blind Phase-5 reviews and
this final audit. The x-normal, unrealizable-admittance coherent-echo
mechanism is REFUTEd, robustly, five independent ways, for both
`PAIR_PAD` and `PAIR_ABSORB40`, on the complete two-wall instrument — a
real, well-earned negative result. It is **not** the closing of the
coherent-echo mechanism class as a whole: a y-wall echo, a realizable-
admittance instantiation of the same x-wall mechanism, and a Yee-grid-
dispersion correction all remain untested and are ranked for Iteration 55.
`NOTES.md`'s "doubly excluded... no known mechanism class remains
untested" language is corrected accordingly (§2a, §4 item 1).

**Checkpoint criterion 4 fires** — not on this cycle's own mechanism work,
which is sound throughout, but on a two-cycle-old dimensional error
(`amp_ratio` treated as if directly comparable to `C_thr`) that was
self-disclosed once, used anyway in the same document's own headline,
actively but incompletely re-verified by Red Team's own prior audit, and
written into LOGBOOK's permanent T16 entry as settled fact — caught only
by a second, independent blind Phase-5 seat one full cycle later. Ruled a
notification, not a pause, the 12th consecutive such ruling; a same-shift
LOGBOOK correction and a candidate rule addendum are proposed (§2b, §4
item 7). T28's own substantive mechanism question — the ~2.84° periodicity's
ultimate origin — remains open, narrowed this cycle toward "not an
x-normal, unrealizable-admittance echo" specifically, with the board's
next moves now ranked by cost and information density (§6) rather than
left as six seats' independent, unreconciled top-3 lists.
