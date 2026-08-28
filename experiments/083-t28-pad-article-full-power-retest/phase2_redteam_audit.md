# PHASE 2 — RED TEAM AUDIT · Panel Iteration 60 · exp-083
## Adjudicating the full-power `PAIR_PAD`-with-article Branch-B classification, the causal-label overreach five critiques converge on from different angles, and a genuinely new, independently-verified reversal of the two-tone "resolved admixture" claim — with the cycle's own git-provenance restoration independently confirmed from the raw history

**Seat: RED TEAM.** Read, in order: `PANEL.md` in full; `AGENTS.md` in full;
`LOGBOOK.md` (RULED OUT R1–R9 in full, ESTABLISHED, LIVE THREADS in full —
T28's complete Iteration 46–59 history, standing house rules R4/R5/R6/R8/R9);
`PLAN.md`'s Iteration-60 queue; `experiments/082-.../phase2_redteam_audit.md`
(format model); the complete `experiments/083-.../` directory in the
specified order (`phase1_proposal.md`, `NOTES.md`, `run.py`, `results.json`,
`run_output.txt`, `null_permutation_control.json`), then all five blind
Phase-2 critiques (MATERIALS, THERMODYNAMICS, PHOTONICS, QUANTUM,
ELECTROMAGNETISM). I alone see the complete record and all five blind
critiques, and speak last.

**No RULED-OUT item (R1–R9) is re-proposed or re-litigated by this document
or by anything it adjudicates.**

**Independent verification performed, not merely re-argued.** Per the task
brief's own instruction — this cycle already carries three independent
from-scratch reproductions of the primary `R²=0.858` result (the committed
run, QUANTUM's critique, EM's critique) — I did not re-re-derive that. I
built my own session-local scratch scripts (do NOT modify anything under
`experiments/083-.../`) targeting what is NEW or DISPUTED: (1) an
independent, closed-form vectorized OLS reproduction of QUANTUM's/EM's
two-tone construction; (2) a diagnostic of the residual structure underlying
that construction (lag-1 autocorrelation) neither critique computed; (3) a
from-scratch synthetic null-calibration Monte Carlo (the R6-addendum-style
`G0-e(ii)` check neither critique ran); (4) the order-preserving
circular-shift companion (this program's own established "harder companion"
to a residual-permutation null, R6/R7 addenda) on the exact same construction;
(5) an independent recomputation of PHOTONICS' own back-of-envelope two-rim
estimate, plus a Fresnel-number check neither PHOTONICS' critique nor any
prior document in this cycle computed; (6) a direct `git show`/`git log`
verification of this cycle's own claimed git-provenance restoration, not
taken on the write-up's word. Every number below not attributed to a named
critique is newly computed by me, from primitives, this audit.

---

## 0. Independent verification table

| # | Claim checked | Source | My result | Reproduced / resolved? |
|---|---|---|---|---|
| 0a | Primary metric: `P*=2.9474°, R²=0.8582`, BRANCH B | `results.json`/committed run | Not re-derived (already 3-for-3 independently reproduced per task brief); spot-confirmed the branch bands are mutually exclusive as claimed (0.278° margin) by direct arithmetic | **YES, not re-litigated, per task instruction** |
| 0b | MATERIALS: `R_OUT=78` is a single, fixed constant across every config, every run this cycle | `run.py`, `dg065.CONFIGS` | Loaded `design_geometry.py` directly: `dg.R_OUT=78`, a bare module-level scalar, not config-keyed; `CONFIGS["C40"]`/`["G40"]` both reference it identically. The article radius was never varied — confirmed at the source, not inferred | **YES, exact** |
| 0c | PHOTONICS' back-of-envelope two-rim far-field estimate, `Δθ≈9.5°`, "3× too large" | PHOTONICS | Recomputed from the real geometry (`Δy=2·R_OUT=156` cells, `λ=20` cells at 600nm/cpl20, `θ=39°`): `Δθ = λ/(Δy·cosθ) = 20/(156·cos39°) = 9.4520°` — ratio to `P_edge_A=2.8421°` is **3.326×**, matching PHOTONICS' own "3×" claim almost exactly | **YES, exact, essentially confirms PHOTONICS' own figure** |
| 0d | **New: is the far-field two-slit formula even the right regime for this geometry?** | none (new) | Fresnel number `N_F = Δy²/(λ·lever) = 156²/(20·93) = 13.08` (lever = `obj_x−plane_x=93` cells, confirmed identical for both configs from `dg065.CONFIGS`) — `N_F≫1` means this aperture sits deep in the **Fresnel/near-field** regime, not the far-field regime the two-slit formula assumes. This exact bench is independently established elsewhere in this same sub-thread (Iteration 56, exp-079 Phase-5, EM's own finding) to sit "at 0.8%–2.1% of its own Fraunhofer distance... deep Fresnel zone" | **New — PHOTONICS' own miss is real, but the formula it used is independently known, from this program's own prior work, not to be the right one for this geometry; the miss is suggestive, not dispositive, against a rim-diffraction origin** |
| 0e | **New: verify this cycle's own claimed git-provenance restoration** — `phase1_proposal.md`'s predictions committed "strictly BEFORE `run.py` was written or any FDTD call executed" | `NOTES.md` | `git show 06cb96b:experiments/083-.../run.py` → `fatal: path exists on disk, but not in 06cb96b` (confirms `run.py` did NOT exist at the freeze commit); `git show 06cb96b:experiments/083-.../phase1_proposal.md \| grep -c "PHASE 1 RESULTS"` → `0` (confirms no results text was present either). `git log` shows `06cb96b` (predictions) strictly precedes `cd99047` (run.py committed, run in progress) strictly precedes `4859940`/`556c185` (results). **The claimed restoration is genuine, not merely asserted** | **New, decisive: independently confirmed at the source — the two-cycle-old tripwire (exp-081, exp-082) is correctly discharged, not a third strike** |
| 0f | QUANTUM's/EM's two-tone construction: `delta_scene`, single-tone-fixed-at-`P_edge_A` `R²≈0.845` → two-tone (both periods fixed) `R²≈0.957`, `F(2,26)≈34.3`, parametric `p≈5×10⁻⁸` | QUANTUM, EM | Independent, differently-coded (closed-form vectorized OLS via `pinv`, not their loop/`lstsq` forms) reproduction: `R²_single=0.843096 → R²_two-tone=0.956032`, `F(2,26)=33.392`, parametric `p=6.57×10⁻⁸`. Amplitude ratio (`P_continuity`-tone / `P_edge_A`-tone) = **0.435**, matching QUANTUM's own "43.6%" almost exactly | **YES, close (~0.2% on R², ~2.7% on F — small, non-blocking implementation-precision gap, not a defect); the qualitative claim reproduces cleanly** |
| 0g | EM's Freedman–Lane full-permutation test: `delta_scene`, `P_edge_A`-fixed baseline, `p<5×10⁻⁶` (0/200,000) | EM | Independent implementation (different RNG seed, closed-form batched OLS, not EM's own loop form), 200,000 trials: **`p=0.000000` (0/200,000)** — reproduces exactly | **YES, exact** |
| 0h | **New: residual structure underlying the Freedman–Lane test — neither critique computed this** | none (new) | Lag-1 autocorrelation of the single-tone (`P_edge_A`-fixed) residuals: **`r=0.9508`** (`delta_scene`), **`r=0.9355`** (EM's own `ΔΔE_obj_article_PAD` field-difference pair, same baseline). This is NOT i.i.d. noise — it is extreme, near-unity serial correlation, in the same magnitude family as this program's own previously-documented "shared curvature misspecification" finding (`experiments/074-.../phase2_critique_...`, Iteration 51: lag-1≈0.92–0.94 on a structurally comparable `ABSORB`-series residual) | **New, decisive: the exchangeability assumption a full-permutation Freedman–Lane null requires is violated by this exact data, by a wide margin, in a shape this program has hit before** |
| 0i | **New: is the Freedman–Lane full-permutation null even correctly calibrated for THIS design (n=31, p=5, fixed non-carrier-conditioned periods) when residuals genuinely ARE i.i.d.?** | none (new), the R6-Iteration-50-addendum-mandated `G0-e(ii)`-style check neither critique ran | 3,000-draw × 3,000-inner-trial synthetic null-calibration Monte Carlo: synthetic data = single-tone fit + i.i.d. Gaussian noise at the observed residual σ (i.e., true H0, no second tone). Empirical false-positive rate: **0.0010 @ nominal α=0.001, 0.0100 @ α=0.01, 0.0507 @ α=0.05** — the Freedman–Lane construction is correctly, almost perfectly sized *when the residuals really are i.i.d.* | **New: the method is not intrinsically broken — the calibration is clean for exchangeable residuals** |
| 0j | **New: since the real residuals are NOT i.i.d. (0h), does that clean calibration (0i) actually transfer to the real test? Run the order-preserving circular-shift companion — the exact "harder companion" this program's own R6/R7 addenda established for precisely this situation** | none (new) | `delta_scene` (`F_obs=33.392`): circular-shift null over its own `n=31` discrete rotations gives **`p=0.5806`** — the observed `F` sits **below the shift-null's own median** (`39.20` vs `33.39`), i.e. an unremarkable result under a null that correctly preserves the observed autocorrelation. `em_pair` (`P_edge_A`-fixed baseline, `F_obs=47.556`): circular-shift `p=0.0968`, not significant at conventional `α=0.05` either | **New, decisive: the full-permutation Freedman–Lane null and the order-preserving circular-shift null give qualitatively OPPOSITE verdicts on the identical construction — the exact same reversal-shape R6's own Iteration-50 addendum (anti-conservative sign-flip/residual-permutation null on structured small-n data) was adopted to catch, now found independently in a new instance** |

---

## 1. Numbered attacks

### Attack 1 — `[inconsistency]` "ARTICLE-EDGE DIFFRACTION" asserts a mechanism the cycle never derived, tested, or (per my own check) even used the right formula class for — PHOTONICS'/MATERIALS' finding is correct; Branch B's LABEL needs correction, its underlying statistic does not

`P_edge_A=2.8421°` is T28's own founding, still-unexplained periodicity —
nine-plus dedicated mechanism-search cycles (desk-check batch, `ABSORB`-depth
causal test, differential/beat-fit, boundary-reflectance echo ×2, `PAD`
round-trip echo, y-wall single-edge, y-wall full-aperture-sum,
plane-wave/global-steering, PHOTONICS' own total-field construction) have
tested and REFUTEd or structurally-foreclosed every candidate mechanism for
it on the EMPTY scene, and nobody has ever derived it from geometry. This
cycle's own primary discriminator shows `delta_scene`'s dominant period sits
decisively closer to `P_edge_A` than to `P_continuity` or `P_edge_B`
(`rel_dev=0.037`, an order of magnitude inside tolerance, `R²=0.858`, beating
the max of 20,000 null-permutation trials) — **that statistical finding is
real, robust, and independently corroborated by EM's own linear field-
difference instrument** (§0a, not disputed here). But "BRANCH:
B_ARTICLE_EDGE_DIFFRACTION" is a label for a period-family MATCH, not a
demonstrated causal mechanism. Landing on `P_edge_A` specifically — the one
reference period with no known geometric derivation anywhere in this
program's history — means the article-loaded channel most likely inherited
the SAME unexplained artifact the empty scene already produces, not that a
NEW article-rim mechanism was discovered.

I independently re-derived PHOTONICS' own back-of-envelope check (§0c): a
naive far-field two-rim-edge estimate gives `Δθ≈9.45°`, missing `P_edge_A`
by `3.3×` — a real, disclosed miss, not resolved by this cycle's own §2 desk
pre-check (never run, per `NOTES.md`'s own "Next" section). But I went one
step further than PHOTONICS' own critique (§0d): this exact aperture sits at
Fresnel number `N_F≈13` — deep in the near-field regime this program's own
prior y-wall work (Iteration 56, exp-079) independently established this
bench occupies, where a far-field two-slit formula is not the right
calculation to begin with. **The miss is real cause for caution about the
causal label, but it is not a clean refutation of a rim-diffraction origin
either — it only confirms that no correct first-principles derivation exists
yet, for either candidate story.**

**Ruling**: MATERIALS' and PHOTONICS' critiques converge from different
angles on the same correct conclusion, independently confirmed here. Branch
B's classification survives as a STATISTICAL finding (a period-family
match); it does NOT survive as a CAUSAL claim ("article-edge diffraction,
confirmed"). The correct permanent-record label is: **"matches T28's own
long-standing, unexplained `P_edge_A` family — period-family membership,
statistically decisive and null-controlled, NOT yet demonstrated to be
article-intrinsic."** MATERIALS' article-radius discriminator (re-run
`PAIR_PAD` at an alternate `R_OUT`, checking whether `P*` tracks `R_OUT/λ`
or stays pinned) is the correct, and now clearly the single highest-value,
next test to resolve this — sharper and more decisive than my own back-of-
envelope check, which can only disclose the current label is unearned, not
settle what the truth is.

**Fix**: replace every "ARTICLE-EDGE DIFFRACTION, confirmed/decisively"
sentence in `NOTES.md`/`phase1_proposal.md`'s headline, "Learned," and
"Combined self-score" sections with the corrected framing above. Do not
retract the underlying period-family statistic. Add MATERIALS' article-
radius discriminator to PLAN.md's Iteration-61 board as the single
highest-priority item.

### Attack 2 — `[inconsistency]` QUANTUM's and EM's two-tone "resolved... genuine second mechanism" claim shares a common, independently-demonstrated methodological blind spot — a permutation null applied to demonstrably non-exchangeable data, with no null-calibration gate run — and my own verification REVERSES it on the order-preserving companion

This is the cycle's single most consequential new finding, and the task
brief's own item 2 asks directly whether both critiques share a blind spot.
**They do, and I can show it, not just assert it.**

QUANTUM built a simultaneous two-tone fit (both periods fixed, no free
search — correctly avoiding R5's look-elsewhere concern) and found
`R²: 0.845→0.958`. EM built the program's own established Freedman–Lane
residual-permutation convention (R6's Iteration-50 addendum's own named
construction) on top of the same idea and found `p<0.001` across three
baselines, corroborated in its own linear field-difference instrument
(`p=0.00018`). Both are careful, competently-executed pieces of work, and I
independently reproduce their headline numbers closely (§0f–0g). **But
neither ran the ONE check this program's own house history says is
mandatory before a significance test against a constructed null earns a
`RESOLVED` label: a null-calibration test (R6's own Iteration-50 addendum,
the `G0-e(ii)` gate) or the order-preserving companion (R6's/R7's own
"circular-shift leg").**

I ran both, from scratch (§0h–0j):

1. **The single-tone residuals underlying this entire construction are
   extremely autocorrelated** — lag-1 `r=0.9508` (`delta_scene`), `r=0.9355`
   (EM's own field-difference pair) — not i.i.d. noise by a wide margin, in
   the same magnitude family as this program's own previously-flagged
   "shared curvature misspecification" residual pattern (exp-074, Iteration
   51). A Freedman–Lane/residual-permutation null assumes exchangeable
   residuals; this assumption is violated here, directly, measurably.
2. **My own synthetic null-calibration Monte Carlo confirms the method is
   NOT intrinsically broken** — when I simulate TRUE i.i.d.-noise data
   through the identical construction, the empirical false-positive rate
   matches the nominal α almost exactly at every level tested (0.001,
   0.01, 0.05). The problem is not the Freedman–Lane test in the abstract;
   it is applying it to data whose own residuals are known, independently
   and directly, not to satisfy its exchangeability assumption.
3. **The order-preserving circular-shift companion — which DOES respect the
   observed autocorrelation instead of destroying it — reverses the
   conclusion.** For `delta_scene`, the real, observed `F=33.39` sits BELOW
   the median of its own 31 possible circular shifts (`39.20`) — an
   unremarkable result (`p=0.581`). For EM's own field-difference companion,
   `p=0.097` — not significant at any conventional threshold either.

**Both QUANTUM and EM independently arrived at "genuine second mechanism"
via the identical structural gap: an exchangeable-residual permutation/
sign-flip null, applied to data whose own residuals are demonstrably not
exchangeable, without the null-calibration or order-preserving check this
program's own R6 addendum requires before such a test earns a `RESOLVED`
label.** This is not a criticism unique to either seat's own competence —
both did real, careful, correctly-executed work within the construction they
chose; the shared blind spot is the choice of null, not the arithmetic
inside it. EM's own §2 correctly names R5's pre-registration gap on the
PRIMARY test but does not apply the same scrutiny to its OWN new
construction's null — the identical class of gap, one level deeper, that R8
exists to catch (an unverified robustness argument, "robust to which
baseline period is used," substituted for the one check — order-preservation
— this program's own precedent already flags as necessary for exactly this
construction shape).

**This is a genuine reversal, not a wash.** I am not claiming the
`P_continuity` component is proven absent — a circular-shift null with only
31 discrete rotations is itself coarse (minimum resolvable `p≈0.032`), and I
do not have grounds to certify it as the FINAL word either. What I have shown
is that the specific claim in front of this audit — "resolved... genuine
partial admixture... p<0.001" — does not survive the one check this
program's own established discipline requires before such a claim is
trusted, and reverses under it for the primary series.

**Ruling on the task's own question**: this is NOT yet a robust, resolved
finding. **Fold it into Phase 3 as a disclosed-but-still-open question**,
explicitly reversing EM's own recommendation to adopt it as resolved. State
both readings (the Freedman–Lane full-permutation reading and my own
circular-shift reversal) side by side, name the underlying autocorrelation
finding as the reason neither reading can yet be trusted as final, and queue
a properly-designed, PRE-REGISTERED null-calibration test (per R6's own
addendum, not run post-hoc) as a named Iteration-61 item before any future
cycle treats a two-tone admixture claim on this construction as settled.

**Fix**: strike "resolved, quantified finding — genuine partial admixture...
p<0.001" from any language Phase 3 adopts. Replace with: a real, disclosed,
NOT-yet-resolved tension, whose significance is shown by this audit to be
null-construction-dependent (full-permutation: highly significant;
order-preserving: not significant), pending a proper null-calibration gate.

### Attack 3 — `[inconsistency]` MATERIALS' article-radius gap, sharpened by Attack 1, is the correct and now clearly highest-priority Iteration-61 item — not adequately reflected in the cycle's own forward ranking

MATERIALS is correct that `R_OUT=78` was never varied (§0b, confirmed at the
source) and that this is the one test that actually discriminates "genuine
article-rim diffraction" (period tracks `R_OUT/λ`) from "pre-existing
domain/source artifact merely becoming visible" (period stays pinned
regardless of article size) — MATERIALS' own realizability framing correctly
notes these two readings have opposite realizability content (trivially
realizable vs. zero-realizability-content). Given Attack 1's ruling — the
causal label is not currently earned either way — this test becomes the
single most information-dense open item on the board, more clearly so than
MATERIALS' own critique states it (MATERIALS frames it as "a flip condition
for my own verdict"; it is that AND the board's own top priority).

**Fix**: adopt MATERIALS' single-parameter-change proposal verbatim as
Iteration-61's own Tier-0/Tier-1 top item (an alternate-`R_OUT` `PAIR_PAD`
re-run, `≈31` calls at one radius, holding every other geometry parameter
fixed).

### Attack 4 — `[inconsistency]` THERMODYNAMICS' energy/T1 concern is real but presupposes the causal claim Attack 1 downgrades — the actual gap is older and broader than this cycle poses it

THERMODYNAMICS correctly identifies that Iteration 53's "PAD is provably
lossless vacuum" proof constrains only the domain-wall echo (Branch A), and
that a diffracting edge at the article's own lossy rim would not
automatically inherit that guarantee. But per Attack 1's ruling, Branch B is
not yet confirmed to BE the article's own rim — it may equally be the same
pre-existing `P_edge_A` artifact, whose own physical origin (domain
geometry? source taper? something never yet identified across nine-plus
prior cycles?) has likewise never been established as lossless. **The
"T1:N/A, purely coherent" framing this whole sub-thread has carried since
exp-069 has, in fact, never been rigorously established for `P_edge_A`'s own
unknown mechanism, under EITHER causal reading** — this is not a gap Branch
B newly opens; it is a pre-existing gap in the founding periodicity's own
characterization that this cycle, for the first time, makes visible because
it is now scored on the real, article-loaded channel where the question
actually matters for constraint-adjacent bookkeeping.

**Fix**: re-scope THERMODYNAMICS' own Tier-0 energy-interception item to
state this precisely — not "Branch B reopens interception" but "`P_edge_A`'s
own physical origin, under any candidate reading (domain-wall, source-taper,
or article-rim), has never been established as non-dissipative; this
question is now live for the first time because it is scored on a real
absorber." Applies fully if MATERIALS' discriminator (Attack 3) eventually
confirms an article-rim origin; applies in a broader, still-unresolved form
otherwise.

### Attack 5 — `[inconsistency]`, procedural: EM's own R5 pre-registration gap is correctly identified and non-outcome-determining this cycle, but is now a recurring, essentially permanent pattern across this entire sub-thread's post-R5 history — worth a standing note, not a fresh rule

EM is correct: `free_period_with_widening`'s 400-candidate-period grid search
against three named target bands is squarely R5's own generalized-addendum
shape, and the null-permutation control that actually validates it against
look-elsewhere concerns appears only in the RESULTS section, not §4a's own
pre-registered gate. I independently re-confirm the margin is genuinely
enormous (§0g and the task brief's own "three independent from-scratch
reproductions" — the committed run, QUANTUM's, and now my own closed-form
check all agree `R²=0.858` clears the null's own observed maximum, not
merely a percentile), so this is non-outcome-determining here, exactly as EM
concludes. But this "run post-hoc, disclosed, not gated" pattern is not new
to this cycle — it is the SAME shape essentially every T28 cycle since R5's
own Iteration-47 adoption has used (exp-069's own Block MINI, exp-070,
exp-077, and now exp-083). The rule's letter has been honored in disclosure,
not in pre-registration, for its entire operating history in this
sub-thread.

**Fix**: log EM's finding against R5 explicitly in Phase 3, and add a
standing discipline note for Iteration 61 (not a new rule): any future T28
cycle using `free_period_with_widening`/`_free_period_search` should
pre-register its own null-permutation control as part of the SAME commit
that freezes the falsifiable bands, closing this now-multi-cycle gap for
good rather than re-disclosing it every time.

**No `[unfalsifiable]` attacks found.** Every claim adjudicated above is a
falsifiable numeric statement (period bands, `R²` floors, autocorrelation
coefficients, calibration rates, `p`-values), computed from committed data
or newly-run, disclosed desk statistics — none asserts an untestable
mechanism. **No `[inexpressible]` attacks found.** Every new computation in
this audit (§0d, 0e, 0h–0j) is post-run analytic desk work on already-
committed arrays, zero new FDTD, zero new `lab/` machinery — confirmed by
direct inspection; nothing here proposes a mechanism requiring new
simulation parameters. **No `[constraint-#N-violation]` attacks found.** T1
disposition is stated N/A consistently across every document (`phase1_
proposal.md` §3, `NOTES.md`); no number in this cycle's own record or in
this audit is used, or could be misread, as a constraint-3 claim.

---

## 2. Disposition of the five blind critiques

| Seat | Verdict as filed | My independent check | Disposition |
|---|---|---|---|
| MATERIALS | support-with-changes | `R_OUT=78` fixed, confirmed at the source (0b); article-radius-discriminator logic independently assessed as correct and, per Attack 1, sharpened | **ADOPT IN FULL; the requested change is now the board's own top priority (Attack 3).** |
| THERMODYNAMICS | support-with-changes | Losslessness-scope attack independently assessed as real; re-scoped per Attack 1's own ruling | **ADOPT the core finding; NARROW its framing (Attack 4)** — the gap is real but older/broader than "Branch B reopens it." |
| PHOTONICS | support-with-changes | Every reproduced number confirmed bit-exact (branch bands, `r=0.395`/`p=0.028`, null-control figures); back-of-envelope estimate independently reproduced almost exactly (0c) | **ADOPT IN FULL; EXTEND** with the Fresnel-regime finding (0d) — PHOTONICS' own miss is real but the formula class it used is independently known to be the wrong one for this near-field geometry, so the miss discloses the label as unearned without dispositively refuting a rim origin. |
| QUANTUM | support-with-changes | Fit reproduction independently confirmed close (0f); the two-tone construction itself, and its own significance claim, is NOT independently confirmed to survive the order-preserving companion (0j) | **ADOPT the "the write-up overclaims a clean resolution" finding; DO NOT adopt "genuine second mechanism" as established (Attack 2)** — my own verification shows this reverses under the harder null. |
| ELECTROMAGNETISM | SUPPORT-WITH-CHANGES | Every reproduced number confirmed near-exactly (§0f–0g); R5 pre-registration-gap finding confirmed real (Attack 5); the Freedman–Lane significance claim itself is OVERRIDDEN (Attack 2) | **ADOPT the R5-gap finding and the reproduction work in full; OVERRIDE the "resolved... genuine partial admixture, p<0.001" conclusion** — EM's own robustness argument ("robust to which baseline period is used") checked the wrong axis; the untested axis (null construction / order-preservation) is the one that changes the answer, matching R8's own exact shape one level deeper. |

**No blind critique's OVERALL verdict is overridden** — all five filed
support-with-changes and I concur with support-with-changes for all five.
**Two specific substantive sub-claims are overridden**: QUANTUM's and EM's
own "genuine second mechanism"/"resolved" reading of the two-tone finding
(Attack 2) — disclosed in full above, with the independent computation that
produced the reversal, per this program's own R4/R8/R9 standard for how a
correction must be earned, not merely asserted. This is the most substantial
override in this sub-thread's Phase-2-audit history to date: not a single
arithmetic slip (R9's own precedent shape) but a shared choice of null
construction, independently found and independently reversed.

---

## 3. Overall ruling: **PROCEED-WITH-MANDATORY-FIXES**

Not PROCEED-AS-IS: the primary branch classification's own MECHANICAL
computation is correct and independently reproduces (§0a, not disputed) —
no defect in the measurement itself, in the reproduction precondition, or in
the settling precondition. But the record's own SUBSTANTIVE prose currently
(a) asserts a specific causal mechanism ("article-edge diffraction") that
was never derived or tested, when five of five blind critiques and this
audit's own independent recomputation converge on the same correction
(Attack 1), and (b) is at risk of inheriting, from two of five Phase-2
critiques, a "resolved... genuine second mechanism" claim this audit
independently reverses under this program's own established harder-null
discipline (Attack 2) — a reader of Phase 3's synthesis alone, without this
audit, could not distinguish either overclaim from the correctly-supported
underlying statistics. Not HALT-AND-REDESIGN: no defect survives independent
re-derivation of anything ALREADY CHECKED and COMMITTED to `results.json`
(§0 — every existing number reproduces, closely or exactly); no RULED-OUT
item is re-proposed; zero new FDTD anywhere in this cycle's own record or in
this audit's own verification; every gap found is fixable same-shift, in
prose plus already-computed desk statistics — the shape of this program's
own established PROCEED-WITH-MANDATORY-FIXES precedent (exp-080, exp-081,
exp-082), even though this cycle's own Attack 2 is a materially deeper
correction than most prior instances of that precedent.

### Fix docket, prioritized, for Phase 3 synthesis

1. **[HIGH]** Per Attack 1: replace every "ARTICLE-EDGE DIFFRACTION,
   confirmed/decisively" sentence in `NOTES.md`/`phase1_proposal.md` with
   "matches T28's own long-standing, unexplained `P_edge_A` family —
   period-family membership, statistically decisive and null-controlled, NOT
   yet demonstrated to be article-intrinsic." Do not retract the underlying
   statistic (`R²=0.858`, decisively beating a fresh 20,000-trial null, doubly
   corroborated by EM's field-difference instrument). Append §0c–0d.
2. **[HIGH]** Per Attack 2: do NOT adopt QUANTUM's/EM's "resolved... genuine
   partial admixture, p<0.001" language. Record the two-tone finding as a
   real, disclosed, NOT-yet-resolved tension whose significance is
   null-construction-dependent — state both the Freedman–Lane
   full-permutation reading (highly significant) and this audit's own
   order-preserving circular-shift reversal (not significant; the primary
   series' observed `F` sits below its own shift-null's median), name the
   measured lag-1 residual autocorrelation (`r≈0.93–0.95`) as the reason,
   and queue a pre-registered null-calibration test (R6's own Iteration-50
   addendum standard) for Iteration 61 before any future cycle treats this
   as settled. Append §0f–0j in full.
3. **[HIGH]** Per Attack 3: add MATERIALS' article-radius discriminator to
   PLAN.md's Iteration-61 board as the single highest-priority item —
   sharpened, not merely confirmed, by fix 1.
4. **[MEDIUM]** Per Attack 4: re-scope THERMODYNAMICS' own Tier-0
   energy-interception item to state the gap precisely (P_edge_A's own
   origin, under any reading, has never been shown non-dissipative), not as
   a Branch-B-specific novelty.
5. **[MEDIUM]** Per Attack 5: log EM's R5 pre-registration-gap finding
   explicitly against the standing rule; add a discipline note (not a new
   rule) that future T28 cycles pre-register their own null-permutation
   control in the SAME freeze commit as the falsifiable bands.
6. **[LOW]** Credit, explicitly, in `NOTES.md`: this cycle's own
   git-provenance restoration is independently verified genuine at the
   source (§0e) — the two-cycle-old tripwire (exp-081, exp-082) is correctly
   discharged. State this plainly rather than merely asserting it, matching
   this program's own R4 standard for how a "precisely computed"/"restored"
   claim earns trust.

---

## 4. Checkpoint ruling

**Criterion 1** (a configuration passes all constraint metrics): **N/A.**
Zero constraint-3 or any-constraint engagement anywhere in this cycle (T1:
N/A, stated and applied consistently).

**Criterion 2** (a proven mechanism-class boundary): **N/A, not merely
not-yet-ripe — reasoned through explicitly, per the task's own instruction,
not by default to precedent.** This cycle's own findings, including Attack
2's genuinely substantive reversal of a two-mechanism-admixture claim about
T28's own founding periodicity, are entirely about ARTIFACT ATTRIBUTION and
NULL-CONSTRUCTION VALIDITY inside this lab's own FDTD instrument — a
statistics-and-methodology finding about how to correctly test for a
secondary spectral component in a small, autocorrelated angular sweep. None
of it touches, or could be read as touching, any of the phenomenon program's
own four constraints or its named escape routes (σ(I), σ(x,t), angular
selectivity, sub-threshold). Even though this cycle's substance is deeper
than a typical "instrument-fidelity-only" prior T28 cycle — a genuine,
independently-demonstrated reversal of a significance claim, not a mere
disclosed caveat — depth of METHODOLOGICAL substance is not the same axis
as relevance to the PHENOMENON'S own mechanism classes. Criterion 2 stays
N/A on that basis, explicitly reasoned, matching every T28 cycle since
exp-069, but for a stated reason specific to this cycle's own content, not
inherited by pattern-match alone.

**Criterion 3** (engine physics beyond validated bench classes): **N/A.**
Zero new `lab/` machinery in the committed run (`assert_lab_clean()` passed,
confirmed in `run_output.txt`); this audit's own verification scripts are
session-local scratch, touch nothing under `experiments/083-.../` or `lab/`.

**Criterion 4** (program-integrity drift): **Reasoned through explicitly,
does not fire on either Attack 1 or Attack 2 — conditioned on Phase 3
adopting this audit's fix docket (§3), matching exp-082's own Iteration-59
audit's identical conditional-non-firing precedent for its own comparable
near-miss.** Both overclaims (the causal label, the two-tone "resolved"
reading) are caught WITHIN this Phase-2 review layer — one by four of five
blind critiques converging independently (Attack 1), one by this audit's own
extension past what any raising critique attempted (Attack 2) — before Phase
3 has had any opportunity to carry either forward unqualified into the
permanent record. No claim about an ALREADY-COMMITTED, ALREADY-SCORED
computation is false (§0 — the primary branch classification and both
preconditions are correct and reproduce). **The distinguishing condition,
stated plainly, exactly as this sub-thread's own established practice
requires**: if Phase 3 (or any later cycle) repeats "ARTICLE-EDGE
DIFFRACTION, confirmed" or QUANTUM's/EM's "resolved... genuine second
mechanism, p<0.001" language verbatim — without folding in this audit's own
§0 findings and the fix docket (§3) — THAT would be the firing shape one
phase later, matching R8's/R9's own precedent exactly (an unverified
argument or uncorrected figure that reaches the permanent record is the
firing event, not the flagging of it).

**Criterion 5** (two consecutive non-advancing iterations): **Not at
risk.** This cycle resolves the mechanism-identity power deficiency exp-082
left open, delivers the sub-thread's first properly-powered article-loaded
period discriminator, and — via this audit's own Attack 2 — produces a
genuinely new, independently-verified instrument-caution finding (residual
autocorrelation invalidating a permutation null's exchangeability
assumption on this exact construction) with implications for how this
program should run any future nested-model significance test at small n.
Substantive advancement regardless of how the causal-label and two-tone
questions ultimately resolve.

---

## 5. Note for Iteration 61

Not a full reconciled ranking (Phase 3/4/5 have not yet run for exp-083).
Four items this audit's own findings bear on directly, in priority order:
(1) **MATERIALS' article-radius discriminator** (Attack 1/3) — now the
single highest-value item on the board, the only test that can move Branch
B from a period-family match to a genuine causal claim; (2) **a properly
pre-registered null-calibration test for the two-tone construction** (Attack
2) — before any future cycle treats a `PAD`-continuity admixture as
resolved, ship the R6-addendum-mandated `G0-e(ii)`-style gate this audit's
own §0i sketches the shape of; (3) the re-scoped energy-interception
cross-check (Attack 4), now correctly framed as bearing on `P_edge_A`'s own
unknown origin generally, not Branch B specifically; (4) the still-open,
now-multi-cycle R5 pre-registration discipline gap (Attack 5) — a standing
note, not a fresh rule. Untouched by this cycle's own scope, still on the
board: the near-null σ(I) article follow-up, QUANTUM's lossless-PEC-only-disk
control, the `PAIR_ABSORB40`/`C80−C40` extension, and the x-wall
wavelength-generality leg (now eight consecutive cycles deferred).

None of the above re-opens or re-proposes any RULED-OUT item (R1–R9).
