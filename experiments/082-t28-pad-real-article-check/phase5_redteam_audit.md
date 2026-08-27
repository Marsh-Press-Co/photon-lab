# PHASE 5 — RED TEAM FINAL AUDIT · Panel Iteration 59 · exp-082
## Adjudicating all six blind Phase-5 reviews of the PAD-loaded real-article check — independently reproducing and extending QUANTUM's outlier phase-shift finding to test whether it is specific evidence or a generic n=7 artifact; ruling on EM's field-difference decomposition, PHOTONICS' article-edge-diffraction hypothesis, and MATERIALS'/THERMODYNAMICS' charter points; Checkpoint criteria 1–5; reconciling Iteration 60's queue

**Seat: RED TEAM.** Fresh sub-agent, zero memory of any prior session. Read,
in order: `PANEL.md` in full, `AGENTS.md` in full, `LOGBOOK.md` (RULED OUT
R1–R9 in full, ESTABLISHED, LIVE THREADS in full — T28's complete Iteration
46–58 history, standing house rules R4/R6/R8/R9 in particular), `PLAN.md`'s
Iteration-59 queue, `experiments/081-.../phase5_redteam_audit.md` (the direct
ancestor's Phase-5 final audit, format model, not copied), then the complete
`experiments/082-t28-pad-real-article-check/` directory in the order
specified (`phase1_proposal.md`, `NOTES.md`, `run.py`, `results.json`,
`run_output.txt`, `x_wall_realizable_refit.py`/`_results.md`/`_results.json`/
`x_wall_output.txt`, `phase_convention_extension.py`/`_results.md`/
`_results.json`/`_output.txt`, all five `phase2_critique_*.md`,
`phase2_redteam_audit.md`, `phase3_synthesis.md`), then all six Phase-5
reviews (`phase5_review_{photonics,materials,em,thermodynamics,vision,
quantum}.md`). I alone see the complete record and all six blind Phase-5
reviews, and speak last.

**No RULED-OUT item (R1–R9) is re-proposed or re-litigated by this document
or by anything it adjudicates.** Independently re-confirmed by my own fresh
grep of the complete `experiments/082-.../` directory for constraint-3/
witness/T1 language — every instance reads "N/A," matching all five blind
Phase-2 critics, Red Team's own Phase-2 audit, and all six Phase-5 seats.

---

## 0. What I independently verified

The task directs me to focus verification on what is NEW or DISPUTED this
cycle — the record already contains at least four independent from-scratch
reproductions of Red Team's own Phase-2 statistics (§0d–0k of
`phase2_redteam_audit.md`): PHOTONICS' Phase-5 review, EM's Phase-5 review,
QUANTUM's Phase-5 review, and VISION's own independent rebuild of the
secondary-metric comparators. I re-ran the deterministic core of that table
myself (session-local scratch, `redteam_verify_082.py`, importing only
`experiments/077-.../pad_round_trip_model.py::free_period_with_widening` via
the house `_load()` idiom, plus raw arrays copied verbatim from
`results.json`/`experiments/076-.../results.json`, never hand-typed) as a
sanity floor, then spent the bulk of my own effort on the genuinely new,
disputed question the task assigns me: **independently verifying and
extending QUANTUM's own phase-shift demonstration** — this is now the
**fifth** independent computation of the deterministic core (Red Team's own
Phase-2 audit; PHOTONICS, EM, QUANTUM's own Phase-5 reviews; mine) and the
**second** independent computation of QUANTUM's own phase-shift result
specifically.

### 0.1 Deterministic core — reconfirmed, bit-exact

| Claim | Committed figure | My independent recomputation | Match |
|---|---|---|---|
| `A_scene`, `A_empty`, `ratio` | 3.4076×10⁻³, 5.1846×10⁻³, 0.6573 | `ptp()` on the raw `results.json` arrays: bit-identical | exact |
| Pearson `r(delta_scene,delta_empty)` | 0.0306 | `0.03057312042619495` | exact |
| Exact 7!-permutation `p` | 0.953 | Full 5040-permutation enumeration: `0.952976...` | exact |
| Exact critical `\|r\|` at α=0.05, n=7 | 0.746 | `0.746117` (same enumeration, sorted) | exact |
| `delta_scene` free period/R² | P\*=2.940°, R²=0.858 | `2.9398496°`, `0.8582518` (real `free_period_with_widening`, re-run) | exact |
| `delta_empty` (7pt) free period/R² | P\*=1.015°, R²=0.864 | `1.0150376°`, `0.8637150` | exact |
| True 31-point `PAIR_PAD` period (ground truth) | `4.611289746337977°` | Re-ran `free_period_with_widening` on `experiments/076-.../results.json::headline`'s own C40/G40 arrays: `4.611289746337977°` | exact |
| `delta_empty`'s 7 points bit-identical to the 31-point ground truth at those angles | claimed | Confirmed indirectly and directly: the ground-truth free-fit on the reconstructed 31-point series reproduces the cited period to every digit | exact |

All eight numbers reproduce exactly. This is now independently confirmed a
fifth time across this cycle's own record. I found no discrepancy and spent
no further effort re-deriving what six prior computations already agree on
— per the task's own instruction, effort below is concentrated on what is
new.

### 0.2 QUANTUM's phase-shift demonstration — VERIFIED, reproduces closely, with two material refinements neither QUANTUM nor any other seat ran

QUANTUM's own finding (`phase5_review_quantum.md` §3b): a pure single-tone
sinusoid at `PAIR_PAD`'s own true period (`P=4.611289746337977°`), sampled at
exactly this cycle's 7 θ-points, correlated against a copy of itself shifted
by `φ`, produces `r=0.031` at `φ≈90.3°` — matching the observed
`r(delta_scene,delta_empty)=0.0306` closely.

**I independently rebuilt this from scratch** (not from QUANTUM's own code,
which does not exist as a committed artifact — QUANTUM's review states the
table but not a script). My own 0.1°-resolution grid search over
`φ∈[0°,360°)` finds the best match at **`φ=85.9°`, giving `r=0.0310`**
against the target `r_obs=0.0306` — matching QUANTUM's own `φ≈90.3°`/`r=0.031`
closely (the ~4° discrepancy is consistent with QUANTUM's own table being
read off a coarse 15°-step grid rather than genuinely optimized; my own
0.1°-resolution search is the more precise figure, and both agree on the
substance: a phase shift near a quarter-period reproduces the observed `r`
almost exactly). **QUANTUM's core empirical claim is confirmed, independently,
a second time.**

**Refinement 1 — QUANTUM's table reports only one of two solutions.** My own
grid search finds `r(φ)` crosses the target value `r_obs=0.0306` at **two**
points in `[0°,360°)`: `φ=85.9°` and `φ=269.6°`. QUANTUM's own review reports
only the near-90° branch; the near-270° branch (a phase shift in the
*opposite* direction) matches equally well and is, a priori, equally
physically plausible — nothing in QUANTUM's own linearity argument (§3a of
its review) picks a preferred sign for the article-induced path-length
shift. This does not weaken QUANTUM's finding (the near-90°-magnitude
observation stands either way — `|φ|≈86°`–`90°` is a quarter-period
regardless of sign), but the record should state there are two, not one,
degenerate solutions at this power, a genuinely new but minor precision.

**Refinement 2 — decisive: is this match SPECIFIC to the TRUE PAD period, or
is it a generic property of near-Nyquist 7-point correlation that essentially
ANY candidate period would also produce?** This is the load-bearing question
neither QUANTUM nor any other Phase-5 seat asked, and it is exactly the
question the task directs me to adjudicate. I ran the identical
phase-matching search over a dense grid of **281 candidate periods spanning
`[1°,15°]`** (0.05° step) — not merely the true period plus two named
comparison periods, but a systematic sweep — and for each period, searched
for ANY `φ∈[0°,360°)` reproducing `r_obs=0.0306` within `±0.01`:

```
Periods admitting a phase match within tolerance: 279 / 281 = 99.3%
  P=4.6113  (TRUE PAIR_PAD)        best phi= 85.9deg  r=0.0310  |dev|=0.0004
  P=2.8421  (T28 original C80-C40) best phi= 87.9deg  r=0.0305  |dev|=0.00003
  P=1.9608  (T21 established fringe) best phi=309.1deg  r=0.0289  |dev|=0.0017
  P=3.0000  (arbitrary)             best phi=271.5deg  r=0.0297  |dev|=0.0009
  P=7.5000  (arbitrary)             best phi= 91.0deg  r=0.0308  |dev|=0.0002
  P=12.000  (arbitrary, no established basis anywhere in this program) best phi= 89.1deg  r=0.0312  |dev|=0.0007
```

**This is decisive, and it materially reframes what QUANTUM's own finding
shows.** A phase-matched reproduction of `r_obs≈0.031` is achievable, to
comparable precision, at **99.3% of arbitrary candidate periods** across a
15°-wide window — including `12.0°`, a period with no established basis
anywhere in this program's nine-cycle T28 history. This is the expected,
essentially tautological consequence of `r(φ)` being a continuous function
of one free parameter that sweeps through nearly the full `[-1,+1]` range
as `φ` varies over `360°`: by the intermediate value theorem, a value near
zero is reached for almost any period, almost always, at n=7. **QUANTUM's
own phase-shift result, while numerically correct and independently
reproduced, is NOT specific evidence for the TRUE `4.611°` PAD period over
any other period** — it is a generic property of this instrument's own
near-Nyquist sampling at this window width, not a finding that discriminates
"same mechanism, phase-shifted" from any alternative hypothesis at all. This
is the same underlying shape R5's own family of house rules exists to catch
(an unconstrained free-parameter match to a target statistic is not evidence
without a control establishing how easily chance produces the same match) —
here applied for the first time to a phase-match rather than a combinatorial
search or a period-fit, a genuinely new instrument-caution finding in its
own right, alongside Red Team's own Phase-2 §0h–k findings about this same
instrument's other failure modes at n=7.

**A second, independent, weakly-disconfirming data point, also new.** I
additionally checked whether a *free-amplitude* (not merely a
correlation-matching) fit of a shifted sinusoid at each candidate period
actually reproduces `delta_scene`'s own real values well:

```
  P=4.6113 (TRUE PAIR_PAD) phi=85.9deg  best-fit R^2(fit to delta_scene) = 0.0628
  P=2.8421 (T28 2.84 family) phi=87.9deg  best-fit R^2(fit to delta_scene) = 0.5736
  P=1.9608 (T21 fringe)     phi=309.1deg best-fit R^2(fit to delta_scene) = 0.1819
```

A least-squares-scaled, phase-matched sinusoid at the TRUE PAD period
explains only **6%** of `delta_scene`'s own variance; the same construction
at PHOTONICS' own named `2.8421°` alternative explains **57%** — a
substantially better fit, for the SAME number of free parameters (phase, one
degree of freedom; amplitude/offset, two more, identical across all three
rows). **This is a real, disclosed, but explicitly NOT dispositive data
point that, if anything, mildly cuts the OPPOSITE direction from QUANTUM's
own "leading hypothesis" framing** — I flag it under the identical caution
Red Team's own Phase-2 audit already established generally for this
instrument (Attack 1, §0j: the free-period machinery is PROVEN to recover
the wrong answer for ground-truth data at this exact n=7 power), so neither
this finding nor QUANTUM's own should be read as resolving anything. Both
are symmetric illustrations of what a 7-point window can and cannot
distinguish — not a tie-breaker in either direction.

---

## 1. Adjudication of the six Phase-5 reviews

| Seat | Verdict as filed | My independent check | Disposition |
|---|---|---|---|
| PHOTONICS | PARTIAL | Deterministic core reproduced bit-exact (§0.1); the `R_OUT/λ=78/20=3.9λ` figure independently confirmed against `dg065.R_OUT=78`, `CPL[600]=20`; the two-branch period prediction (4.611° vs. 2.84°/1.96° family) is genuinely falsifiable (§4, below) | **ADOPT IN FULL.** The article-edge-diffraction hypothesis is a real, distinct, well-posed alternative — see §4. |
| MATERIALS | PARTIAL | x-wall refit "2 of 4 flip, none to SUPPORT" reconfirmed directly from `x_wall_realizable_refit_results.json::verdict_flips` (this is now the third independent read of that exact field, after MATERIALS' own Phase-2 critique and Red Team's Phase-2 audit §0m); the "zero realizability content" charter argument independently assessed as sound (§5, below) | **ADOPT IN FULL**, including the new realizability-framing finding. |
| ELECTROMAGNETISM | PARTIAL | All eight of EM's own independently-reproduced Phase-2 statistics reconfirmed by my own §0.1 (matching the deterministic core's own fifth independent computation, §0 above); the field-difference decomposition independently assessed (§3, below) — sound but not fully self-sufficient as EM's own framing implies | **ADOPT IN FULL, with one scoping refinement** (§3) — does not change EM's own verdict or its own ranking (item 1, bundled with the full-window re-test). |
| THERMODYNAMICS | PARTIAL | The fix-docket item 4 merge independently re-traced through all three documents (`phase1_proposal.md`, `NOTES.md`, `phase3_synthesis.md`) — confirmed as genuine prose unification, not two footnotes under one heading; the sidecar-convention check (zero energy/power/joule/watt hits in this cycle's own new artifacts) independently re-grepped, confirmed | **ADOPT IN FULL.** |
| VISION | PARTIAL | Independently re-derived all three secondary-metric comparators from `analyze_pair`'s own raw `A_i`/`A_q` primitives — reproduces Red Team's own ≈2.77× exactly, confirms the original Phase-2 "≈4.2×" figure is unreconstructable from its own stated operands under any reading, matching Red Team's own Attack 5 finding independently | **ADOPT IN FULL.** This is now the fourth independent confirmation of the ≈2.77× correction (Red Team's audit, PHOTONICS' Phase-5 field-trace, VISION's own from-scratch rebuild, and implicitly EM's own numbers) — settled beyond reasonable dispute. |
| QUANTUM | **PROMISING** (outlier; explicitly scoped away from the mechanism-identity question itself) | Phase-shift demonstration independently reproduced (§0.2) — the core number is correct. Its own generalization to a "leading hypothesis" is NOT supported once tested for specificity (§0.2, Refinement 2, and §2, below) — genuinely new counter-evidence, not a re-argument | **ADOPT the phase-shift NUMBER in full; DO NOT adopt QUANTUM's own reading of what it shows, and rule the verdict LABEL should not carry to LOGBOOK as filed — see §2.** |

**No blind Phase-5 review's underlying arithmetic or from-primitives
reproduction is overridden — every load-bearing number across all six
reviews independently reproduces.** The one substantive adjudication this
audit performs is not a numeric correction (unlike exp-074's/exp-077's own
precedents) but a **specificity check** on a correctly-computed number whose
interpretive weight QUANTUM's own review overstated — a different failure
shape than any prior R4/R6/R7/R8/R9 instance, closer in kind to R5's own
original "a tight raw deviation alone is not sufficient... a
null-permutation/look-elsewhere control is required" discipline, applied
here for the first time to a single-phase match rather than a combinatorial
or period search.

---

## 2. Central adjudication: does QUANTUM's finding justify PROMISING, or does PARTIAL stand for this cycle's own work?

**Ruling: PARTIAL stands as the correct Combined Verdict for this cycle's
own work. QUANTUM's finding is real, independently reproduced twice now, and
correctly logged as a strong argument FOR running the full 31-point test
next — it is NOT evidence that this cycle's own result is "promising" in the
sense PANEL.md's own verdict vocabulary is built to convey, and my own
extension (§0.2) shows the finding does not even favor mechanism continuity
over any other candidate period once tested for specificity.**

Reasoned through explicitly, not by vote-counting the five-to-one split:

**(a) What QUANTUM's finding actually establishes, precisely.** A physically
ordinary, first-order-expected consequence of this bench's own linearity
(QUANTUM's §3a: Weber contrast is quadratic in field, so
`E_no-article+E_scattered` produces a genuine coherent cross-term) —
*combined with* a quarter-period phase shift at the TRUE PAD period — is
numerically consistent with the observed near-zero correlation. This is a
real, correctly-computed, twice-independently-reproduced fact. It shows
"same mechanism, phase-shifted" is **not ruled out** by the low correlation
— a genuinely useful correction to any reader who might have mistaken
`r=0.031` itself as evidence *against* continuity.

**(b) What it does NOT establish, per my own new §0.2 extension.** Whether
this specific numerical coincidence is *meaningful* evidence FOR continuity,
as opposed to an artifact of matching one free parameter (phase) to one
target statistic (`r`) at n=7, is exactly the question QUANTUM's own review
does not test and my own §0.2 Refinement 2 answers directly: **99.3% of
arbitrary candidate periods across a 15°-wide window admit an equally good
phase-matched reproduction of the observed `r`, including periods with no
established basis anywhere in this program.** This is not a close call — it
is the same order of magnitude as R5's own original "36,680 combinations
found a sub-0.1% match regardless of ground truth" finding, translated into
a continuous-parameter setting. A finding that would reproduce equally well
under a false premise is not evidence for the premise. QUANTUM's own review
explicitly and correctly declines to claim the phase-shift finding "resolves
which of the two readings is correct" (§3b, its own text: "this is new
evidence FOR the 'same mechanism, phase-shifted' reading being physically
live, not evidence that resolves which of the two readings is correct") —
my own extension goes one step further and shows it is not even evidence
that the reading is *more likely than any alternative*, which is what its
own §4 "leading hypothesis, not merely not-ruled-out" framing and its own
Iteration-60 ranking language ("a real discriminator... sharpened into a
specific, falsifiable coherent-optics prediction") lean on.

**(c) QUANTUM's own verdict text, read in full, is substantively describing
PARTIAL.** QUANTUM's own VERDICT line reads: "**PROMISING** (for the item-7
tripwire discharge and the instrument-limitation finding; the
mechanism-identity question itself remains genuinely open, not 'promising'
in isolation)." Read plainly, QUANTUM is not claiming the phenomenon-program
relevant question — mechanism identity — is promising; it explicitly says
the opposite. What QUANTUM calls "promising" is the cycle's own
*execution*: discharging the tripwire, and producing a genuinely reusable
instrument-caution finding. Every one of the other five seats says the
identical thing about the SAME two facts, in their own words, while filing
PARTIAL: "real advancement, not merely record-keeping" (VISION); "genuine,
substantive advancement" (Red Team's own Phase-2 audit, Criterion 5 ruling);
"the sub-thread's first-ever article-loaded FDTD measurement... genuine
advancement" (PHOTONICS, MATERIALS, THERMODYNAMICS, EM, in near-identical
language). **The substantive disagreement between QUANTUM and the other five
seats is thinner than the verdict labels suggest — it is largely a
vocabulary choice about what PANEL.md's promising/partial/ruled-out taxonomy
is FOR.**

**(d) Why the vocabulary question matters and how it should be resolved.**
PANEL.md's own verdict taxonomy ("Director updates LOGBOOK.md (verdict:
promising / partial / ruled out)") exists to characterize a *mechanism
candidate's* status against the phenomenon program's own constraints. This
cycle's own T1 disposition is N/A, stated and independently reconfirmed by
every phase and every seat: there is no live mechanism candidate here to be
promising or ruled out. "PARTIAL" — used by five of six seats and by both
Red Team audits this cycle (Phase 2's Criterion-5 ruling and this one) —
correctly captures "genuine, disciplined, independently-verified narrowing,
without resolving the central open question," the shape this whole
nine-cycle T28 sub-thread's own established convention already uses for
exactly this kind of cycle (Iterations 53, 55, 56, 58, per LOGBOOK's own
record). QUANTUM's own use of PROMISING, scoped explicitly to execution
quality rather than to a mechanism finding, is not wrong on its own terms,
but it applies the wrong word from this program's own controlled vocabulary
to describe it, and would read, unqualified, to a future LOGBOOK reader as
implying more than QUANTUM's own text intends. **Ruling: the Combined
Verdict for this cycle is PARTIAL, matching the majority and matching what
QUANTUM's own prose substantively describes; QUANTUM's own PROMISING label
is not adopted for the permanent record, and the reason is stated
explicitly here, not merely by outvoting it.** QUANTUM's own phase-shift
finding is fully retained and correctly credited (§0.2, above; the fix
docket, §6, below) — this is not an override of QUANTUM's arithmetic or its
good-faith reasoning, only of the verdict LABEL, on the specific,
independently-tested ground that its own justification for the label (a
"leading hypothesis" reading) does not survive a specificity check neither
QUANTUM nor any other seat ran.

**(e) The correct, affirmative use of QUANTUM's finding.** Exactly as the
task frames the alternative: QUANTUM's finding is correctly logged as a
**strong argument for running the full 31-point test next** — not because
it shows continuity is likely, but because it demonstrates, concretely, that
this cycle's own 7-point instrument cannot distinguish "same mechanism,
ordinarily phase-shifted" from "a coincidental match at any of dozens of
candidate periods," which is a sharper, more specific reason to prioritize
that test than "we need more statistical power" in the abstract. This
strengthens, rather than weakens, the near-unanimous ranking of the
full-window re-test as Iteration 60's own top item (§7, below) — every one
of the six seats independently converges on it regardless of how the
PARTIAL/PROMISING question is resolved.

---

## 3. Is EM's field-difference decomposition (`ΔE_article = E_with − E_without`) a sound, board-worthy new instrument, and does it structurally solve what it claims to?

**Sound and board-worthy: yes. Structurally solves the confound on its own:
no — it is a genuine, valuable, cheap complementary diagnostic, not a
replacement for the intensity-level test, and should be run alongside it,
exactly as EM itself in fact proposed (bundled with the full-window
re-test, not standalone).**

**What it gets right.** This bench is confirmed fully linear at 600nm (no
`σ(I)`, no time-varying `ε` anywhere in `build_article`/`Sim` — independently
re-confirmed by direct inspection of `run.py`'s own imports and construction
calls, matching EM's own and QUANTUM's own independent charter-angle
confirmations). Superposition therefore holds exactly at the FIELD level:
`E_total ≡ E_no-article + ΔE_article`. Computing `ΔE_article` directly and
free-period-fitting IT, rather than the reduced, nonlinear Weber-contrast
ratio `C=(B_obj−B_flank)/B_flank`, is a genuinely different instrument that
never passes through the ratio EM's own Phase-2 critique correctly named as
the likely reason `ptp` amplitude survives while point-wise shape
correlation collapses (a large, near-constant shadow term in the
denominator). This is real, novel to this cycle's record, cheap (the raw
`observer_profile` arrays already exist transiently inside `run.py`'s own
execution — persisting them costs one line, and EM's own proposal correctly
notes the marginal FDTD cost is zero if bundled with the already-necessary
full-window re-test), and uses only already-gated primitives
(`amb.observer_profile`, `pad_round_trip_model.free_period_with_widening`).
**This is a genuinely new, well-motivated EM-charter instrument idea, worth
Iteration 60's own board — I concur with EM's own ranking (item 1, bundled
with the full-window re-test).**

**Where the "structurally removes the confound" framing overstates what the
test alone would show.** EM's own §3 states the field-level decomposition
"removes, rather than out-powers, the shadow-term confound." This is true
for isolating `ΔE_article`'s **own** periodicity in isolation — a genuinely
clean question about what oscillatory structure the article's own scattered
field alone carries. But the quantity constraint-3 citations actually score
is the nonlinear Weber contrast `C`, not the raw field, and QUANTUM's own
§3(a) linearity argument (independently confirmed correct by me, §0.2's own
premise) supplies the precise reason this matters: the scored intensity is
`|E_no-article+E_scattered|² = |E_no-article|² + |E_scattered|² +
2·Re(E_no-article·E_scattered*)` — a **cross term** between the article's own
scattered field and the pre-existing (PAD-tied) boundary-echo field. Even if
`ΔE_article(θ)` alone shows NO period near `4.611°` (a clean, informative
negative result about the article's OWN echo terms), the cross term could
still reproduce PAD-tied structure at the intensity level, because it
depends on `E_no-article`'s own phase (which DOES carry the PAD ripple) as
well as `E_scattered`'s. Symmetrically, a genuinely PAD-periodic
`ΔE_article(θ)` would be strong, direct evidence FOR continuity — the test
is asymmetrically informative (a clean negative on `ΔE_article` does not
settle the intensity-level question; a clean positive would be much more
decisive). **Ruling: EM's proposal is adopted as a genuinely new, cheap,
board-worthy Tier-1 instrument for Iteration 60 (§7, below), correctly
bundled with, not substituted for, the intensity-level free-period fit on
`delta_scene`/`delta_empty` at full power — the record should state this
asymmetry explicitly when the test is run, so a clean `ΔE_article` negative
is not over-read as settling the mechanism-identity question the way a
positive result would.**

---

## 4. Is PHOTONICS' article-edge-diffraction hypothesis a genuinely distinct alternative to QUANTUM's phase-shift-of-same-mechanism hypothesis, or are they compatible?

**Genuinely distinct and mutually exclusive at the level that matters —
each predicts a DIFFERENT true period for `delta_scene(θ)` at full power —
while being operationally complementary: the SAME already-near-unanimous
next experiment (the full 31-point window) cleanly discriminates between
them.**

PHOTONICS' hypothesis (§2 of its review): the flagship article's own radius,
`R_OUT=78` cells at `cpl=20`, spans `78/20=3.9λ` at 600nm (independently
reconfirmed directly against `dg065.R_OUT`/`CPL[600]`, §1 table, above) — large
enough to present its own diffracting rim, a second, physically distinct
source of angle-dependent interference structure, independent of the
domain's PEC-wall echo. This predicts `delta_scene(θ)`'s TRUE period (at full
statistical power) should land near the `≈2.84°` (T28's own original
`C80−C40` empty-scene period) or `≈1.96°` (T21's own established
source-taper fringe) family — periods with an established, independent
diffractive origin elsewhere in this program, structurally unrelated to
`PAIR_PAD`'s own `4.611°` round-trip distance.

QUANTUM's hypothesis (§0.2, above): the SAME `4.611°`-period wall echo
persists, merely phase-shifted by the article's own added path length —
predicting the TRUE period should still land near `4.611°`.

These are not restatements of each other. They agree that the empty-scene
mechanism does not simply vanish (both predict a real, article-induced
oscillatory structure at comparable scale to what was measured), but they
make **opposite, falsifiable predictions about which established period
family the true, full-power fit should recover** — a clean, two-branch,
pre-registerable discriminator exactly as PHOTONICS' own review frames it.
**My own new §0.2 finding is directly relevant here and should be logged
alongside both hypotheses, not folded into either**: at this cycle's own
7-point power, a free-amplitude-and-phase fit weakly (and, per Red Team's
own established Attack-1 caution, non-dispositively) favors PHOTONICS' own
`2.8421°` family (`R²=0.57`) over QUANTUM's `4.611°` continuity reading
(`R²=0.06`) against the real `delta_scene` values — worth disclosing as a
mild, explicitly-non-dispositive tilt in the pre-registration for the full
31-point test, not as evidence for either hypothesis at this power.
**Ruling: both hypotheses are adopted as genuinely distinct, well-posed,
falsifiable candidates for Iteration 60's own pre-registered two- (or
three-, including a null "neither established family" outcome) branch
prediction on the full-window re-test — complementary in that one
experiment resolves both, not because they are the same claim.**

---

## 5. MATERIALS' and THERMODYNAMICS' charter-level points

**MATERIALS — `PAIR_PAD` carries zero realizability content: sound, adopted
as a standing framing rule.** Independently re-derived from primitives
(matching MATERIALS' own citation): `lab/fdtd2d.py`'s damping-mask
construction is a pure function of `absorb` alone, proven zero-dependent on
`pad`/`nx`/`ny` (Iteration 53, re-confirmed this cycle by THERMODYNAMICS'
own Phase-2 attack and Red Team's Attack 3). `PAIR_PAD` is therefore not a
question about what material property or admittance family could realize a
boundary's optical response — it is a question about the FDTD domain's own
vacuum-padding round-trip distance, a scene/instrument-geometry fact with no
"published / plausible / unobtainium-with-parameters" entry in MATERIALS'
own charter taxonomy at all. MATERIALS' own stated consequence — that even
in the counterfactual where mechanism continuity were shown to hold, that
would carry zero realizability content, and must be filed as a scene-geometry
disclosure alongside, never folded into, any future `REALIZABILITY_MEMO.md`
citation — is correct and adopted as a standing framing rule for this
sub-thread (§6, Tier 0, below).

**THERMODYNAMICS — a tighter, scene-specific energy-interception cross-check:
sound, adopted, and materially overlapping with EM's own §2 proposal — merge
into one joint Tier-0 item.** THERMODYNAMICS' own Phase-2 critique (§3,
disclosed as a lower-stakes note) and its own Phase-5 ranking item 3
independently arrive at essentially the same desk-only diagnostic EM's own
Phase-2 critique proposed in §4 of that document (a passivity/Poynting bound
using the article's own established extinction figures, now specific to
this cycle's own geometry rather than exp-081's own loosest-possible
`interception_factor_upper_bound=1.0` assumption). Both are zero-FDTD,
post-run analytic (correctly matching THERMODYNAMICS' own sidecar
convention, re-confirmed clean this cycle at §1/§2 of its own Phase-5
review — zero energy/power/joule/watt hits anywhere in this cycle's own new
artifacts). **Ruling: these are the SAME proposed item from two adjacent
charters, not two competing ones — merged into one joint Tier-0 board item,
co-owned by EM and THERMODYNAMICS** (§6, below), rather than carried forward
as a duplicate the way T28's own history has occasionally let happen (e.g.
the x-wall item's own near-miss at exp-080).

---

## 6. Should the near-null σ(I) article follow-up be added to PLAN.md's own queue explicitly this cycle?

**Yes — near-unanimous across all six Phase-5 seats (ranked #1 by MATERIALS
and VISION; #2 by PHOTONICS, THERMODYNAMICS, and QUANTUM; #3, sequenced not
deprioritized, by EM), and MATERIALS' own review explicitly names this as
the outstanding Phase-5 job Phase 3 deferred** ("`phase3_synthesis.md` §3
item 2 is explicit that this is recorded in `NOTES.md` only... that edit is
deferred to 'the Director's own Phase 5 job.' I confirm this disposition is
consistent... but flag directly: this Phase-5 pass is that job"). This audit
performs that job: the item is added to the reconciled Iteration-60 ranking
below (§7, Tier 1) with its full citation (`off_pass`, `τ_off≈0.0065`,
exp-032/exp-034) and its own stated purpose (MATERIALS' own flip
condition — extends this cycle's flagship-only scoping to the near-threshold
regime where the confound could plausibly be perceptually load-bearing,
per VISION's own charter framing). Whoever next updates `PLAN.md`'s own
active queue block (matching this program's own established convention,
e.g. `experiments/081-.../phase5_redteam_audit.md`'s own §6 becoming the
superseding block at `PLAN.md` line 3174) should carry this item forward
explicitly, not leave it standing only in `NOTES.md`'s own prose a second
cycle running.

---

## 7. Checkpoint ruling — all five criteria, reasoned through explicitly

**Criterion 1** (a configuration passes all constraint metrics): **N/A.**
Zero constraint-3 engagement anywhere in this cycle, independently
reconfirmed by my own fresh grep and matching all prior checks (five blind
Phase-2 critiques, Red Team's own Phase-2 audit, Phase 3, all six Phase-5
reviews).

**Criterion 2** (a proven mechanism-class boundary): **N/A, not merely
not-yet-ripe** — matching Red Team's own Phase-2 ruling and Phase 3's
re-reasoned confirmation. This cycle is explicitly instrument-fidelity/
generalization work; no mechanism-class claim is scored anywhere in the
record, so criterion 2's ripe/not-ripe framing does not apply. (This
cycle's own finding — and its own genuinely open mechanism-identity
question — will eventually bear on how much weight the WHOLE T28 y-wall/PAD
sub-thread's own REFUTE-leaning mechanism-class rulings should carry once a
real scene is involved; flagged for Iteration 60's own board, §7 below, not
a criterion-2 event itself.)

**Criterion 3** (engine physics beyond validated bench classes): **N/A.**
`git diff --stat -- lab/` independently re-run by me at HEAD: empty. Zero
new `lab/` machinery anywhere in this cycle's own record (`run.py`, both
riders) or in my own verification script (identical import discipline:
`pad_round_trip_model` and raw JSON only, no `fdtd2d`/`Sim`/`emit`).

**Criterion 4** (program-integrity drift): **Reasoned through explicitly for
two distinct matters — does not fire on either, one closed, one flagged
forward as a now-two-cycle-old pattern.**

*4a. The fix-docket adoption (Phase 2 → Phase 3).* Independently reconfirmed
by three separate Phase-5 seats (PHOTONICS §1, MATERIALS §1, THERMODYNAMICS
§1) and by my own direct reading of the corrected `phase1_proposal.md`/
`NOTES.md` text (§0.1's own reproduction depends on trusting this, and I read
both documents in full at task start, not merely on a reviewer's say-so):
all six fix-docket items landed correctly, including the one specific
numeric override (VISION's own uncorrected "≈4.2×" figure, replaced with the
independently-quadruple-confirmed "≈2.77×"). **Does not fire — condition
satisfied, matching the identical condition Red Team's own Phase-2 audit and
Phase 3 both attached to this cycle's own comparable near-miss.**

*4b. The git-provenance pattern (Attack 6, `phase2_redteam_audit.md`).*
Independently reconfirmed via `git show 5bb78df --stat` and `git log`
myself: the FDTD run was genuinely 27/29 calls complete at the moment
`phase1_proposal.md`'s own pre-registered §4 predictions text was committed
— confirmed exactly as Red Team's own Phase-2 audit found, and, per
PANEL.md's own literal text (the git-before-run mandate binds Phase 3's
FROZEN PREDICTIONS commit specifically, not Phase 1), **this remains not a
rules violation**, matching exp-081's own Iteration-58 precedent for the
identical shape. But this is now the **second consecutive T28 cycle**
(exp-081, exp-082) under **two different lead seats** (THERMODYNAMICS,
QUANTUM) that a blind Phase-2 critique has had to flag this exact pattern —
a lead-seat-independent habit, not a one-off, per Red Team's own Phase-2
audit's own explicit tripwire language ("a third recurrence should not be
read as a close call"). VISION's own Phase-5 review independently confirms
this disposition is correct and does not re-open it. **Ruling: does not
fire this cycle — an omission pattern, not a false claim, correctly
disclosed at every phase, and this exact instance does not touch any FROZEN
PREDICTIONS commit (none was needed this cycle, per Phase 3 §2). I record
this explicitly, matching this program's own established two-strike
convention: a THIRD consecutive T28 cycle repeating this exact
predictions-after-execution pattern, at either Phase 1 or Phase 3, would no
longer be a close call and I would expect it to fire criterion 4 outright.**

*4c. QUANTUM's PROMISING verdict (§2, above).* This is not a Checkpoint-4
matter. QUANTUM did not make a false claim, did not misrepresent a
computation, and disclosed its own reasoning in full, including the honest
caveat that the mechanism-identity question "remains genuinely open." The
disagreement this audit resolves (§2) is an interpretive one about verdict
vocabulary and about a specificity check nobody had yet run — exactly the
kind of finding this review layer exists to surface and reconcile, not a
drift pattern.

**Criterion 5** (two consecutive non-advancing iterations): **Not at risk.**
This cycle discharges PLAN.md's own twice-escalated six-cycle tripwire on
item 7, delivers the sub-thread's first-ever article-loaded FDTD measurement
in nine T28 cycles, produces a genuinely new, twice-independently-verified
instrument-limitation finding (Red Team's Phase-2 §0h–k) *and* a second,
newly-established one this audit adds (§0.2: phase-matching at n=7 is
non-specific across 99%+ of candidate periods) — real, substantive,
independently-verified advancement by every measure this program uses.

---

## 8. Same-shift mandatory-fix docket

1. **[Verdict label]** `NOTES.md`'s own eventual LOGBOOK-facing summary and
   any future citation of this cycle's own six Phase-5 verdicts should state
   the Combined Verdict as **PARTIAL** (5 of 6 seats, and this audit's own
   ruling, §2) — QUANTUM's own PROMISING label is not carried to the
   permanent record as filed, with the reason stated in full (§2) rather
   than by vote-count. QUANTUM's own phase-shift finding IS carried forward
   in full, credited by name (§0.2, §6).
2. **[QUANTUM's finding, refined]** Any future citation of QUANTUM's own
   phase-shift result should carry this audit's own two refinements: (a) two
   symmetric solutions exist (`φ≈86°` and `φ≈270°`), not one; (b) the match
   is NOT specific to the true `4.611°` period — 99.3% of candidate periods
   across `[1°,15°]` admit an equally good match — so it correctly argues FOR
   running the full 31-point test, not FOR mechanism continuity being the
   leading hypothesis at this power.
3. **[EM's proposal, scoped]** The field-difference decomposition
   (`ΔE_article`) is adopted as a genuinely new Tier-1 instrument, explicitly
   noted as asymmetrically informative (§3) — bundle with, do not substitute
   for, the intensity-level free-period fit.
4. **[MATERIALS'/THERMODYNAMICS' points, merged]** MATERIALS' "zero
   realizability content" framing rule and THERMODYNAMICS'/EM's own
   energy-interception cross-check are both adopted (§5); the latter two are
   merged into one joint Tier-0 board item, not carried as duplicates.
5. **[Near-null σ(I) article follow-up, queued]** Added explicitly to the
   reconciled Iteration-60 ranking (§7, below), discharging the outstanding
   Phase-5 job MATERIALS' own review names.
6. **[Governance]** The git-provenance pattern (§7, criterion 4b) is logged
   as a two-cycle-old pattern with an explicit forward tripwire, matching
   this program's own established convention.

None of the above touches `lab/`, any frozen prediction, or any RULED-OUT
item. No new FDTD is run by this audit.

---

## 9. Combined Verdict for the record: **PARTIAL**

For LOGBOOK.md's Iteration 59 entry, verbatim in substance:

This cycle discharged PLAN.md's own twice-escalated, six-cycle-deferred
tripwire (item 7) — the PAD-loaded real-article check — delivering the T28
y-wall/PAD sub-thread's first-ever article-loaded FDTD measurement in nine
cycles. **Primary metric: `ratio=A_scene/A_empty=0.6573`, VERDICT SURVIVES,
stands MECHANICALLY** — decisive, bit-exact, centrally inside the
pre-registered `[0.5,2.0]` band, scoped correctly to the flagship,
strongly-absorbing article class (`materials.graded_black_shell`+
`pec_disk`) after Phase 3 corrected an initial over-generalization
(MATERIALS' Attack 2). **The substantive mechanism-continuity question —
whether this is the SAME lossless phase effect Iteration 53 characterized
on the empty scene, merely observed through the article's own shadow term,
or a qualitatively different, article-mediated interaction — is
demonstrated, not merely left open, to be UNRESOLVABLE at this cycle's own
7-point statistical power**, on four independent lines of evidence (an
exact permutation test, `p=0.953`; the two series' free periods diverging
190%; a ground-truth check proving the same machinery recovers the WRONG
period, 78% off, for a signal of independently-known period; a
200,000-trial null-permutation control showing the achieved `R²≈0.86` is
common under pure noise at this n), independently reproduced from primitives
at minimum **five** times across this cycle's own record (Red Team's Phase-2
audit; PHOTONICS', EM's, and QUANTUM's own Phase-5 reviews; this audit) —
with VISION's own Phase-5 review independently reconfirming the closely
related secondary-metric comparator chain by a sixth, separate computation.
**A newly-run check (this audit, §0.2), extending QUANTUM's own outlier
finding, demonstrates the same underlying instrument limitation extends to
phase-matching specifically**: a physically-motivated phase-shift
demonstration (QUANTUM's own Phase-5 finding, independently reproduced and
extended here) that appears to support mechanism continuity is shown to be
non-specific — 99.3% of arbitrary candidate periods admit an equally good
match at this power — correctly read as a strong argument FOR running the
full 31-point window next, not as evidence favoring continuity over any
alternative. **Combined Verdict: PARTIAL** (five of six blind Phase-5 seats
and this audit; the sixth seat's own PROMISING label described the same
substantive facts as the majority but is not carried to the permanent
record — reasoned through explicitly above, not resolved by vote-count).
Two genuinely new, board-worthy instrument proposals emerged this cycle:
EM's field-difference decomposition (adopted, scoped as complementary, not
a standalone resolution) and QUANTUM's lossless-PEC-only-disk control
(adopted, tests whether persistence depends on absorption specifically).
PHOTONICS' article-edge-diffraction hypothesis and QUANTUM's phase-shift
hypothesis are ruled genuinely distinct, falsifiable, and mutually exclusive
at the level of true period, resolvable by the SAME already-near-unanimous
next test. MATERIALS' "zero realizability content" finding is adopted as a
standing framing rule for this sub-thread. The near-null σ(I) article
follow-up (MATERIALS' own flip condition) is added explicitly to the
Iteration-60 board, discharging the outstanding Phase-5 job Phase 3
deferred. **Checkpoint criteria 1/3 N/A, criterion 2 N/A (not merely
not-yet-ripe, matching Phase 3's own ruling), criterion 4 does not fire on
either matter adjudicated (the fix-docket adoption, confirmed landed; the
git-provenance pattern, now a two-cycle-old tripwire flagged forward — a
third recurrence would fire outright), criterion 5 not at risk.**

---

## 10. Reconciled ranking for Iteration 60's queue

### Tier 0 — zero FDTD, desk-only

1. **[MATERIALS' framing rule, §5]** Log, as a standing rule for this
   sub-thread: `PAIR_PAD`'s effect is a scene/instrument-geometry fact (FDTD
   domain vacuum-padding distance), not a materials-realizability question —
   any future `REALIZABILITY_MEMO.md` citation of this cycle's SURVIVES
   finding must file it as a scene-geometry disclosure, never folded into a
   materials realizability score.
2. **[EM's/THERMODYNAMICS' joint energy-interception cross-check, §5]** One
   merged post-run-analytic sidecar (co-owned by EM and THERMODYNAMICS,
   zero FDTD): a tighter Poynting/interception bound specific to this
   cycle's own article-loaded geometry (reusing the flagship's own
   established extinction figures), checking whether `delta_scene(θ)`'s own
   measured amplitude is even physically consistent with carrying an
   absorbed-power signature.
3. **[Governance]** Log this cycle's own git-provenance pattern (§7,
   criterion 4b) as a two-cycle-old (exp-081, exp-082), lead-seat-independent
   pattern — a third consecutive recurrence at Iteration 60 fires Checkpoint
   criterion 4 outright, not weighed as a close call again.
4. **[Record note]** State, wherever this cycle's own phase-shift finding is
   next cited, both refinements from §0.2/§8 item 2 (two symmetric
   solutions; non-specific across 99%+ of candidate periods) alongside the
   original number.

### Tier 1 — cheap FDTD, near-unanimous next, bundle together

5. **The full 31-point/0.2° `PAIR_PAD`-with-article re-test at 600nm** — the
   single highest-value item on the board (ranked #1 by PHOTONICS,
   THERMODYNAMICS, QUANTUM; a top-2 precondition by MATERIALS, VISION; paired
   by EM). Pre-register PHOTONICS' own two-branch (plus a "neither
   established family" null) period prediction (§4, above) BEFORE running.
   **Bundle in, at zero marginal FDTD cost, EM's own field-difference
   decomposition** (§3, above): persist the raw `observer_profile` arrays
   for both legs (one-line harness change) and independently fit
   `ΔE_article(θ)`'s own period, explicitly logged as complementary to, not
   a substitute for, the intensity-level fit.
6. **The near-null σ(I) article follow-up** (`off_pass`, `τ_off≈0.0065`,
   exp-032/exp-034) — MATERIALS' own flip condition, near-universal top-2
   pick across all six seats (§6, above). Explicitly added to this board
   this cycle, discharging the outstanding Phase-5 job.
7. **QUANTUM's own lossless-PEC-only-disk control** (`materials.pec_disk`
   alone, no `graded_black_shell`, at the identical location) — 14 new
   calls, tests whether the confound's persistence depends on the article's
   own absorption specifically or on its presence as any coherent scatterer.
   Genuinely new, cheap, complementary to items 5–6.
8. Extend the real-article check to `PAIR_ABSORB40`/`C80−C40` (PHOTONICS #3,
   VISION #3) — tests whether SURVIVES is specific to the `PAD` axis or
   general to any boundary-tied confound once a real absorber occupies the
   object window.

### Tier 2 — the board's standing, increasingly overdue items

9. **The x-wall wavelength-generality leg (750/450nm)** — now SEVEN
   consecutive cycles deferred (076–082), ranked #2 by MATERIALS this cycle.
   This item does not yet carry item-7's own explicit escalating tripwire
   language, but its own deferral streak now exceeds item 7's pre-tripwire
   streak (six cycles) — Iteration 60 should not defer it again without an
   explicitly stated reason, matching this sub-thread's own established
   discipline before a formal tripwire becomes necessary.
10. The 750nm x-wall two-wall spot-check — still the single oldest-
    unexecuted item on the whole T28 board, untouched again this cycle.
11. Broadband pulsed reflectance spectroscopy of the `ABSORB` boundary —
    still deferred, unrelated to this cycle's own scope.
12. A proper R3-grade settling convergence study with the article present —
    this cycle ran 2 of 14 config×angle cells (the committed check plus EM's
    own independent second spot-check); real, disclosed, lower urgency.

### Tier 3 — governance

13. Checkpoint criterion 2 ruled N/A this cycle (not merely not-yet-ripe) —
    instrument-fidelity work, no mechanism-class claim made anywhere.
14. Checkpoint criterion 4 ruled non-firing on both matters this audit
    adjudicated (the fix-docket adoption, confirmed landed; the
    git-provenance pattern, flagged forward as a two-cycle-old tripwire).
15. QUANTUM's PROMISING verdict is not carried to the permanent record as
    filed; the substantive finding behind it is fully retained and credited
    (§2, §8 item 1–2) — this is a vocabulary ruling, not an override of any
    computation.

---

## 11. Bottom line

**Combined Verdict: PARTIAL.** The primary metric (`ratio=0.6573`, SURVIVES)
stands mechanically, decisively, and correctly scoped. The mechanism-
continuity question is demonstrated — not merely left open — to be
unresolvable at this cycle's own 7-point power, on four independent lines
of evidence from Red Team's own Phase-2 audit, independently reconfirmed a
further four times across this cycle's own Phase-5 layer (PHOTONICS, EM,
QUANTUM, and this audit — five independent computations in total), including
this audit's own new extension of QUANTUM's phase-shift finding: real,
correctly computed, and correctly read as a strong argument for the full
31-point test next — not as evidence favoring mechanism continuity, which a
systematic specificity check (99.3% of arbitrary periods admit an equally
good match) shows it is not. QUANTUM's own PROMISING verdict is adjudicated
explicitly, not by vote-count: its substantive content matches the other
five seats' own PARTIAL; its label is not carried forward, with the reasons
stated in full. EM's field-difference decomposition and QUANTUM's
lossless-PEC-only-disk control are adopted as genuinely new, cheap,
board-worthy Tier-1 instruments for Iteration 60. PHOTONICS' article-edge-
diffraction hypothesis and QUANTUM's phase-shift hypothesis are ruled
genuinely distinct and falsifiable, resolvable by the same next test.
MATERIALS' and THERMODYNAMICS' charter-level points are both adopted, the
latter merged with EM's own overlapping proposal. The near-null σ(I) article
follow-up is added to the board explicitly this cycle. Checkpoint criteria
1/3 N/A, criterion 2 N/A, criterion 4 does not fire on either matter
adjudicated (one closed, one flagged forward as a two-cycle-old pattern),
criterion 5 not at risk.

No RULED-OUT item (R1–R9) is re-proposed or re-litigated by this document or
by anything it recommends.
