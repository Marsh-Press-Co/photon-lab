# PHASE 5 — RED TEAM FINAL AUDIT · Panel Iteration 55 · exp-078
## Adjudicating all six blind Phase-5 reviews of the y-wall echo pre-screen, independently confirming and QUANTIFYING a second, deeper angle-convention defect inside the cycle's own "correction," and reconciling six Iteration-56 candidate rankings into one

**Seat: RED TEAM.** Read `PANEL.md` and `AGENTS.md` in full; `LOGBOOK.md` in
full (16,804 lines — RULED OUT R1–R9; the ESTABLISHED/LIVE-THREADS sections;
T28's complete Iteration 46–54 history, entries below line 1970). Read the
complete exp-078 record in order: `phase1_proposal.md` (as corrected in
place), `y_wall_prescreen.py`, `y_wall_prescreen_results.json`, all five
Phase-2 critiques, `phase2_redteam_audit.md`, `phase2_quantum_null_check.py`/
`_results.json`, `phase2_redteam_angle_correction_check.py`/`_results.json`,
`phase3_synthesis.md`, `phase4_results.md`,
`phase4_null_calibration_corrected.py`/`_results.json`, and all six blind
`phase5_review_{photonics,materials,em,thermodynamics,quantum,vision}.md`.
Also read `experiments/075-.../boundary_reflectance.py`,
`experiments/065-.../design_geometry.py`, and
`experiments/077-.../phase5_redteam_audit.md` for this document's own format
target. This is Phase 5's final audit: I alone see everything — the official
record and all six blind reviews — and speak last.

Own owned verification script, this audit:
`phase5_redteam_stationary_phase_check.py` /
`phase5_redteam_stationary_phase_check_results.json` (§2c below).

---

## 0. What I independently verified this cycle, from primitives, before ruling on anything

1. **Re-ran `y_wall_prescreen.py` end to end.** Bit-identical to the
   committed JSON and to every number in `phase4_results.md`'s table
   (`C80−C40` `rel_dev=0.4074` at the search boundary at every widened
   stage; `PAIR_ABSORB40` `rel_dev=0.3284`; `PAIR_PAD` `rel_dev=0.3021`;
   gates at 48°–54° clean, `G-LOSSLESS` `3.331e-16`, `G-N1` `2.701e-15`,
   `G-PASSIVITY` worst `|r|=0.038583`). No diff written to disk on re-run.
2. **VISION's stale-`§5.2`-table finding — CONFIRMED bit-exact from the raw
   JSON, not from either party's prose.** `y_wall_prescreen_results.json::
   primary_model_period_search.chosen` shows `at_boundary: False` for all
   five configs (`C40`…`G40`), and every `P*`/`R²` there disagrees with
   `phase1_proposal.md` §5.2's still-printed table (confirmed by direct
   read of both, above). `::as_filed_incorrect_audit_trail` contains only
   `note`/`scores`/`pair_deltas` — **no per-config data at all** —
   independently confirming THERMODYNAMICS' sharper finding that §5.2's
   five rows are not reproducible, correct or as-filed, from anything
   currently committed. Both seats' claims stand, verified from the JSON
   itself, not from either write-up.
3. **MATERIALS' realizable-admittance Pearson-r claim — CONFIRMED, after
   catching and correcting my own first-pass measurement error.** I
   rebuilt the `μ_r=1` TE admittance independently and computed
   `corrcoef(arg(r_matched), arg(r_real))` at the corrected 48°–54°
   envelope for `ABSORB∈{40,60,70,80}`. My first attempt (bare
   `np.angle`, no unwrap) gave `0.999982/0.999890/0.902044/0.749969` —
   disagreeing sharply with MATERIALS' cited `0.999982/0.999890/0.999865/
   0.999754` at `ABSORB=70/80`. Traced the discrepancy myself (R4's own
   discipline applied to my own check, matching exp-077's Red Team
   precedent, §0.5 there): `arg(r)` wraps through `±180°` once inside the
   `48°–54°` window at these depths (visible directly: `ABSORB=80`,
   `θ=53°→54°`, `arg_matched` jumps `+169.3°→−169.1°`), and a bare Pearson
   correlation on wrapped angles is corrupted by that single discontinuity
   given only 31 points. Re-computed with `np.unwrap()` applied to both
   curves before correlating: `0.999982/0.999890/0.999865/0.999754` —
   **matches MATERIALS' table exactly.** MATERIALS' finding is correct;
   my own naive first check would have wrongly disputed it had I not
   traced the discrepancy to its root.
4. **EM's rigorous stationary-phase bounce-angle finding — CONFIRMED
   bit-exact, then extended substantially beyond what EM's own review
   computed.** See §2 below — this is the task's own highest-priority
   item and gets its own section with a dedicated, owned script.
5. **QUANTUM's Fisher-combination and PHOTONICS'/QUANTUM's shared
   spot-checks of the null-calibration JSON** — reproduced directly from
   `phase4_null_calibration_corrected_results.json` (`P(null
   rel_dev≤observed)=0.39595/0.1258/0.17435`; joint `P(≤0 SUPPORT)=
   0.54265`) — matches both reviews' cited numbers exactly. No discrepancy.

No critique across the six reviews overreaches; every load-bearing numeric
claim independently reproduces once corrected for my own tooling error in
item 3. All six seats converged on **PARTIAL**; I concur, with one
substantive addition (§2, §5).

---

## 1. Adjudication of the six Phase-5 reviews

| # | Seat | Finding | Verified? | Load-bearing? | Disposition |
|---|---|---|---|---|---|
| F1 | PHOTONICS | Angular coherence now genuinely established (angle fix independently re-derivable); wavelength coherence still untested for the primary model (600nm-only); `|r|` spans ~20×–190× across configs and comparisons, unweighted, overstating weak configs' evidentiary weight; `PAIR_PAD` is the one comparison immune to the weighting gap and is also T28's own actual target, and it fails on its own terms regardless. | **CONFIRMED** — `|r|` ranges and the 20×–78× ratio independently reproducible from `primary_model_edge_curves`. | Yes — real, disclosed scope gaps (§6.2/§6.7 of the proposal), not new defects. | **ADOPT.** Folded into ranking §7. |
| F2 | MATERIALS | The angle fix and the admittance formula are orthogonal variables; the realizability bound is unchanged either way; a fresh, cycle-specific computation shows the realizable-admittance swap is **period-invariant** for the y-wall (Pearson r>0.9997 on `arg(r(θ))`'s shape), unlike the x-wall, where it may matter — re-ranks the standing realizable-admittance refit toward the x-wall. | **CONFIRMED**, after fixing my own phase-unwrap bug (§0.3). | Yes — a genuine, quantified re-prioritization. | **ADOPT.** Folded into ranking §7 (Tier 0). |
| F3 | ELECTROMAGNETISM | The "corrected" `90−θ_beam` angle is itself not the physically rigorous incidence angle for `edge_image_phase_difference`'s own point-source/Euclidean-distance construction — the rigorous, per-config-constant, stationary-phase bounce angle (13.7°–15.0° from the y-normal) is independent of `θ_beam`, and plugging it in collapses `Δφ_self(θ)` to a flat curve — no oscillatory signal at all. | **CONFIRMED, then extended**: I independently re-derived the angle from the same image-source geometry (bit-exact to EM's table, max `|dev|=2.6e-4°`), gate-checked the never-before-sampled 13.7°–15.1° envelope (clean), and — going beyond EM's own review — built the full doubly-corrected `Δφ_self(θ)` curve for all five configs and every `PAIR_*`/`C80−C40` delta, and diagnosed exactly why a naive re-application of the period-search machinery to this flat curve reports spuriously high R² (§2 below). | **Yes — the single most consequential finding of Phase 5.** | **ADOPT IN FULL, and go further.** See §2, §5, §6. |
| F4 | THERMODYNAMICS | The corrected primary-model reproduces exactly; `PAIR_PAD`'s near-invariance is structurally explained (shared `ABSORB=40`); the near-total-absorption caution touches no scored `PAIR_PAD` comparison; a genuine NEW finding — the mandatory-fix docket's own item 5 was only partially executed: §5.2's per-config table was never regenerated, and the specific `≥99.9999%` digit the corrected write-up now cites does not survive independent recomputation (`≥99.9996%` is correct). | **CONFIRMED bit-exact** (§0.2). | Yes — a real, disclosed, non-load-bearing R4-family gap. | **ADOPT IN FULL.** See §3 (R4), §6. |
| F5 | QUANTUM OPTICS | The fresh 20,000-trial null-calibration control is sound and reproduces exactly; its own joint SUPPORT-count statistic degenerates (near-vacuous) for a 0-of-3 observed outcome; a Fisher-combined omnibus p-value on the already-computed per-target p-values is materially more informative (`p≈0.15` period, `p≈0.63` R²) and should be wired into the committed record. | **CONFIRMED**, recomputed the Fisher combination myself from the three cited p-values (`X²=9.49`, `df=6`, `p=0.148`), matches exactly. | Yes — a real, disclosed, non-load-bearing completeness gap. | **ADOPT.** Folded into docket (§6) and ranking (§7). |
| F6 | VISION SCIENCE | No R9-shaped commensurability defect anywhere in this cycle's own scoring (checked independently, clean). Two findings: (a) `phase1_proposal.md` §5.2's own per-config table was never regenerated at the corrected angle, sitting directly under prose marked "CORRECTED" — non-load-bearing but a genuine, previously-uncaught risk; (b) `PAIR_PAD`'s Test-A period is provably, algebraically forced to equal `C40`'s own individual period (`cos(x+c)−cos(x)` identity, `C40`/`G40` sharing `arg(r(θ;40))` bit-identically) — not independent evidence about the `PAD` axis. | **CONFIRMED, both parts, independently.** (a) reproduced from the raw JSON (§0.2, matches THERMODYNAMICS'). (b) I independently re-derived the trig identity and confirmed `primary_model_pair_deltas.pair_pad.p_star_deg` is bit-identical to 15 significant digits to `C40`'s own individual `p_star_deg` in the committed JSON — exact. | Yes, both. | **ADOPT IN FULL.** See §3 (R4), §6, §7. |

Nothing across the six reviews is overridden. Every load-bearing claim
independently reproduces, once I corrected my own tooling error on F2
(§0.3) — a check I subject myself to precisely because R4/R8 apply to this
audit's own claims as much as to anyone else's.

---

## 2. EM's finding, independently confirmed and quantified: the "corrected" angle is itself wrong, and the model's honest prediction is a flat curve, not a wrong period

### 2a. Independent re-derivation of the rigorous bounce angle

`edge_image_phase_difference` already computes a propagation-phase term
from two Euclidean distances: `dist_real = hypot(D_SP, A)` (real edge to
observer) and `dist_image = hypot(D_SP, OBJ_Y+y_lo)` (the edge's own image,
mirrored through the near y-wall at `y=0`, to the observer) — a
point-source (isotropic 2D radiator), not a plane-wave, propagation
picture (§3.2 of the proposal itself states this explicitly, as the reason
a bare x↔y coordinate swap of the x-wall formula is not licensed). For a
point-source image construction in a homogeneous (vacuum) region, the
physically rigorous local angle of incidence on the wall — the one that
belongs inside a WKB/transfer-matrix reflectance evaluated "from the
interface's own normal" — is the Fermat/stationary-phase angle: the angle
the straight line from the image source `(SRC_X, −y_lo)` to the observer
`(PLANE_X, OBJ_Y)` makes with the wall's normal (`ŷ`). That line has
`Δx = D_SP` and `Δy = OBJ_Y+y_lo` — **the same two quantities already
inside `dist_image`** — so:

```
theta_local = atan(D_SP / (OBJ_Y + y_lo))
```

a **pure function of static per-config geometry**, with zero `θ_beam`
dependence anywhere in its own definition (confirmed by direct source
read: neither `D_SP`, `OBJ_Y`, nor `y_lo` is a function of `θ_beam`
anywhere in `design_geometry.py` or `y_wall_prescreen.py`). I computed this
independently (`phase5_redteam_stationary_phase_check.py` §[1]) and
reproduce EM's own cited table to four decimal places:

| cfg | `d_sp` | `OBJ_Y+y_lo` | `theta_local` (this audit) | EM's review | `\|dev\|` |
|---|---|---|---|---|---|
| C40 | 223 | 832 | 15.0043° | 15.004° | 3e-4° |
| C60 | 223 | 872 | 14.3450° | 14.345° | 0° |
| C70 | 223 | 892 | 14.0362° | 14.036° | 2e-4° |
| C80 | 223 | 912 | 13.7402° | 13.740° | 2e-4° |
| G40 | 223 | 912 | 13.7402° | 13.740° | 2e-4° |

**This is decisively different from `90−θ_beam` (48°–54°), and unlike
`90−θ_beam`, it never sweeps with the swept beam angle at all.** The
`90−θ_beam` convention is the correct incidence angle for a *plane wave*
traveling in the aperture's globally-steered direction — exactly the
picture that licenses the x-wall's own validated two-plane-wave reduction
(§3.1 of the proposal, reproduced bit-exact) — but `edge_image_phase_
difference` has already abandoned that picture (§3.2's own argument) in
favor of a single isotropic point source. A point source has no "steered"
radiation direction of its own; only the coherent sum over the whole
aperture produces one. Feeding a whole-aperture steering angle into a
single point's own reflection geometry is an internally inconsistent
mixture of two representations — exactly EM's own diagnosis, confirmed
here by an independent re-derivation from the primitives, not accepted on
EM's word.

### 2b. Gate check at the never-before-sampled 13.7°–15.1° envelope

Before trusting any `r(θ_local)` number, I re-ran the three sanity/
passivity gates at this envelope (never sampled by the as-filed `±44°`
range, nor by this cycle's own `48°–54°` corrected range):
`G-LOSSLESS` worst `||r|−1|=3.331e-16` PASS; `G-N1` worst
`|r_loop−r_direct|=3.972e-15` PASS; `G-PASSIVITY` worst `|r|=0.000107`
PASS. `reflection_coefficient` is trustworthy here too — this is not a
numerical-artifact regime.

### 2c. The doubly-corrected model, actually computed: flat to float precision, and *why* a naive re-application of Test-A's own machinery reports a spuriously high R² anyway

I built a third version of the phase-difference formula — identical to the
committed one in every line except the angle fed into
`reflection_coefficient` — and evaluated it across the real 31-point,
36°–42° grid for all five configs
(`phase5_redteam_stationary_phase_check.py` §[3]/§[4]):

```
C40: ptp(Delta_phi_self) = 0.000e+00 deg   |r|=1.061114e-04 (constant across all 31 theta_beam)
C60: ptp(Delta_phi_self) = 0.000e+00 deg   |r|=3.996755e-06 (constant)
C70: ptp(Delta_phi_self) = 0.000e+00 deg   |r|=3.733339e-06 (constant)
C80: ptp(Delta_phi_self) = 0.000e+00 deg   |r|=2.018022e-06 (constant)
G40: ptp(Delta_phi_self) = 0.000e+00 deg   |r|=9.271860e-05 (constant)
```

Every `PAIR_*`/`C80−C40` delta is a difference of two constants — also
exactly constant (`ptp=0.000e+00` for all three). **EM's prediction is
confirmed exactly: the model, evaluated at its own internally-consistent
angle, predicts literally no oscillation over the swept beam angle at
all.**

Naively feeding these flat arrays through the identical imported
`_free_period_search`/staged-widening machinery every T28 cycle since
Iteration 46 has used produces a trap I diagnosed and quantified (not
present in EM's own review, new to this audit, §[4b]/[4c] of my script):
the search reports `R²=1.0000` for `PAIR_PAD`/`PAIR_ABSORB40` at the
narrowest stage — apparently a *perfect* fit. This is **not** a real
period. `_fixed_period_fit`'s own `ss_tot>0 else 0.0` guard is meant to
catch an exactly-flat array and return `R²=0.0`, but `ss_tot` for a
numerically-flat array is not *exactly* `0.0` in floating point — `np.
mean()` of `n` bit-identical floats does not, in general, round-trip back
to that exact value, leaving residuals at the `~1e-16` *absolute* scale,
squared to `ss_tot~1e-31`. I verified this directly:

```
PAIR_PAD model curve: all 31 values bit-identical (ptp=0.000e+00),
  yet ss_tot = sum((y-mean(y))^2) = 3.821e-31   (NOT exactly 0.0)
Real PAIR_PAD data's own ss_tot (same statistic): 6.439e-05
Ratio (model/real): 5.934e-27
```

**The doubly-corrected model's entire "variance" available for any period
fit to explain is `5.9×10⁻²⁷`× the real data's own scale — 26 orders of
magnitude below it.** Any `R²` computed against this `ss_tot`, however
close to 1.0 it looks, is fitting floating-point rounding noise, not
physics. This is a *sharper* demonstration that no real period exists than
a clean `R²=0.0` would have been: it shows that a careless re-application
of the existing machinery, without checking the absolute scale, would
*misreport* a "perfect fit" for a model that in fact predicts zero
amplitude — a trap worth naming explicitly so no future cycle falls into
it (a candidate addition to this program's `model_period_runs_to_boundary`
diagnostic family: "check `ss_tot`'s absolute scale before trusting a
high-R² period fit," §6 item 7).

### 2d. Does this generalize beyond the single-edge reduction? Not yet tested — the correct next question, not a foregone conclusion

EM's own §4 point 2 (independently correct, not re-litigated here): this
finding is about the edge-dominance *reduction* specifically (one edge
point, its own image). `phase1_proposal.md` §3.2's own stationary-phase
argument (`dPhi/dy_s` never vanishes over `36°–42°` for the mirrored
aperture sum) already claims the full sum is edge-dominated throughout
this window, on the same footing as the real (non-mirrored) sum T21
established — which, if true, means every point in the full aperture sum
would have its *own* per-point rigorous bounce angle (not a shared
constant, since different aperture points sit at different `y`), and the
sum could in principle still acquire real `θ_beam`-dependence through
which points dominate shifting with `θ_beam` — the same mechanism that
makes the x-wall's whole-aperture picture work. This is a **prediction**,
not yet a result — I did not build the full aperture sum (out of scope for
a zero-new-machinery final audit; it is exactly the "full y-mirrored
propagator" every pre-screen since this queue item was named has been
scoped to avoid building without cause) — and it is now the single most
information-dense next question on this board (§7, Tier 0 #1).

---

## 3. R1–R9 registry, checked against this cycle

- **R1–R3, R6, R7**: N/A, as Red Team's own Phase-2 audit already ruled and
  I independently re-confirm — no constraint-1 claim, no shell-thickness
  claim, no resolution-convergence question (zero-FDTD desk model), no
  fitted carrier/phase coefficient, no un-fit conditioning-only closure
  claim anywhere in this cycle.
- **R4** (hand-typed / not-independently-reproduced figures): **a live,
  confirmed, non-load-bearing finding this cycle — the task's own item (b),
  confirmed independently at §0.2.** `phase1_proposal.md` §5.2's five-row
  per-config table is (i) stale (reproduces the as-filed, wrong-angle
  numbers exactly, digit for digit, verified by my own re-run) sitting
  under prose explicitly marked "CORRECTED," and (ii) not even
  reconstructible from the committed record as either the as-filed or the
  corrected version, since `as_filed_incorrect_audit_trail` was only ever
  populated with the three `PAIR_*`/`C80−C40` pair-delta rows, never the
  five individual per-config rows the docket item needed to preserve.
  **Non-load-bearing** (verified independently, not merely accepted from
  either VISION's or THERMODYNAMICS' review): `C60`/`C70` enter no scored
  `PAIR_*` comparison either way, confirmed by reading `y_wall_
  prescreen.py`'s own scoring calls (§5.3 uses only `C40`/`G40`/`C80`), and
  the Combined Verdict does not cite §5.2's table anywhere. This is the
  correct shape to compare against this program's own R4 precedent
  (exp-048's original trigger, and Iteration 53/exp-076's own "three small
  gaps caught same-cycle, read as the review layer working" ruling) — see
  §4 for why this does not, on its own, fire Checkpoint criterion 4.
- **R5** (null-permutation control mandatory for a dense search): engaged
  correctly — QUANTUM's Phase-2 2,000-trial control and Phase-4's fresh
  20,000-trial control both ran against the model actually being scored at
  each stage; the secondary naive coordinate-swap candidates (§5.4) are
  correctly R5-flagged throughout and never treated as evidence. Clean.
- **R8** (unverified robustness/independence argument filed non-blocking
  when an affordable named check exists): **the task's own item 2 —
  reasoned through explicitly below. Does NOT fire, but for a reason
  distinct from Phase 2's own R8 ruling on Attack 1.** Phase 2's own audit
  correctly ruled R8 does not apply to the *as-filed* angle bug (Attack 1),
  because that bug was caught and a full corrected re-score was actually
  run — the affordable check *was* run — before Phase 3 froze anything.
  EM's Phase-5 finding is a **different** gap: it was never named by any
  Phase-1/2/3/4 party at all — not flagged and dismissed with an unverified
  argument (which is what R8's text specifically targets), but genuinely
  first discovered at Phase 5, the same shape as PHOTONICS'/EM's own
  discovery of the y-wall candidate itself at exp-076/077's Phase 5 (an
  established non-firing pattern: "genuinely new information... not a
  defended wrong claim"). **This audit's own obligation under R8's
  discipline was to not leave EM's finding as an unverified argument once
  raised — I met it**: §2 above is an actual, from-scratch computation
  (bounce angle re-derived, gates re-run at the new envelope, the flat
  curve built and quantified, the `R²` artifact diagnosed), not a
  re-reasoning about EM's own claim. R8 does not fire on this cycle; had I
  instead written "EM's argument is plausible, informational only," while
  declining to run the check myself, *that* would have been exactly the
  shape R8 exists to catch, with this audit being the one chance to catch
  it before it propagates — which is precisely why I ran it.
- **R9** (operand commensurability): checked independently by VISION at
  Phase 2 and Phase 5, both clean, and I re-derived the `rel_dev`/R²
  commensurability argument myself (same units throughout,
  `_free_period_search` applied identically to real and model curves) —
  no R9-shaped defect anywhere in this cycle's scoring.

---

## 4. Checkpoint ruling — does the multi-layered correction history fire criterion 4?

The task's own item 4 asks me to reason through this explicitly: **as-filed
bug (raw `θ_beam`) → Phase-2/3/4 fix (`90−θ_beam`) → a Phase-5-discovered
SECOND, deeper defect in that very fix (§2, this audit)** — layered on top
of two further, independent Phase-5 findings (VISION's stale table, F6a;
THERMODYNAMICS' partially-executed docket item, F4). Is this a
Checkpoint-4-adjacent signal?

**My ruling: NO — this does not fire, and the reasoning below is what
distinguishes it from this program's own firing precedents, not a
coincidence of severity.**

**Matching the non-firing pattern, explicitly:**

1. **Iteration 53 (exp-076)** — three small, independently-caught Phase-5
   process gaps in one cycle, immediately following R8's adoption, ruled
   "evidence the Phase-5 review layer is working at high sensitivity, not
   drift... all three caught by the design, none survived into a defended
   headline claim." This cycle matches that shape closely: THREE distinct
   Phase-5 findings (EM's angle-within-angle defect, VISION's stale table,
   THERMODYNAMICS' partial-docket-execution) were all caught **within this
   same cycle's own Phase-5 layer**, before any of them reached LOGBOOK or
   survived as a defended claim across a cycle boundary.
2. **Iteration 51 (exp-074)** — a genuinely new Phase-5 finding (residual
   autocorrelation) ruled non-firing explicitly because it was "genuinely
   new information... shown non-load-bearing by three independent tests,
   not a defended wrong claim." EM's finding here matches this shape
   precisely: nobody at Phase 1–4 asserted, in their own voice, that
   `90−θ_beam` was rigorously the *correct* physical angle for the
   point-source construction and then had that assertion refuted — Phase
   2's three critics and Red Team's own Phase-2 audit only ever asked
   "which of `θ_beam` or `90−θ_beam` is right," within a framing the
   proposal itself offered as the two live candidates (EM's own §2c,
   independently confirmed correct at §2a above: neither convention was
   examined against the model's own representational switch from a
   plane-wave to a point-source picture). There was no false claim to
   defend — the deeper question was simply never posed until Phase 5.

**Distinguishing from this program's own firing precedents, explicitly:**

- **Unlike Iteration 52 (exp-075)**, where an *unverified* robustness
  argument ("Test A's REFUTE is robust to [the phase-convention issue]")
  was *adopted without independently computing the alternate case* and
  then stated as an uncaveated headline surviving Phase 3/4 — here, no
  argument about EM's specific finding was ever adopted at all before
  Phase 5 raised it, and once raised, this audit computed the alternate
  case immediately (§2), rather than reasoning about it and moving on.
- **Unlike Iterations 49/50 (exp-072/073)**, where a *verifiably false*
  claim ("ZERO items un-adopted," an inverted sign identity) was actively
  defended past multiple phases — nothing false is defended here. The
  official Phase-4 Combined Verdict (INCONCLUSIVE, 0/3 SUPPORT/REFUTE
  under the `90−θ_beam` convention) is **not false** — it is a correct,
  verified computation of what that specific, disclosed convention
  produces (re-confirmed bit-exact at §0.1). What Phase 5 adds is a
  *deeper* characterization, not a *correction* of a wrong number.
- **Unlike Iteration 54 (exp-077)**, where a claim was *actively
  re-verified incompletely* by a prior Red Team audit and then *written
  into LOGBOOK's permanent record* before a second Phase-5 seat caught the
  gap a full cycle later — nothing from this cycle has yet reached
  LOGBOOK. This audit is the first and only opportunity for any of these
  three findings to harden into the permanent record, and none of them do
  so unexamined (§6 closes all three same-shift).

**Net ruling: Checkpoint criterion 4 does not fire.** The multi-layered
correction history reads, correctly, as the panel's own layered-review
design working exactly as intended — three genuinely independent Phase-5
seats (EM, VISION, THERMODYNAMICS) each caught a distinct, real gap the
earlier phases had no occasion to find, none of which survived unexamined
to this document. This is a **close call worth stating plainly, not a
clean one** (unlike Phase 2's own audit, which called its own non-firing
"a clean non-firing call, not a contingent one" — I do not extend that
characterization to Phase 5): had this audit declined to independently
verify EM's finding, or filed it as "plausible but out of scope," the
ruling above would very likely flip via the exact R8 mechanism named in
§3. The reason it doesn't fire is that §2 exists.

---

## 5. Does EM's finding change exp-078's own Combined Verdict? What did this cycle actually establish?

**The frozen Phase-4 numbers stand, unedited, and should not be
retroactively rewritten.** `y_wall_prescreen.py`'s own official Test-A
result — INCONCLUSIVE, 0/3 SUPPORT, 0/3 REFUTE, under the `90−θ_beam`
convention Phase 2/3/4 adopted and pre-registered — is a correct,
independently-reproduced (§0.1) computation of exactly what that
convention predicts. Nothing about §2 makes that number wrong; it makes it
**incomplete as a characterization of what this pre-screen's own edge-image
construction, honestly derived, actually says.**

**Net of everything found through Phase 5, what exp-078 actually
established is stronger and more negative than "INCONCLUSIVE" for the
specific reduction it built — but does not close the y-wall mechanism
class.** Stated precisely:

- The `90−θ_beam`-evaluated model is a **real, disclosed, but internally
  inconsistent hybrid** (a whole-aperture steering angle plugged into a
  single point's own reflection geometry) — its own INCONCLUSIVE result
  should be read as a property of that hybrid, not of the underlying
  physical question.
- The **same edge-image, single-near-wall reduction, evaluated at the
  angle its own point-source construction actually requires**, predicts
  **exactly zero period-band amplitude** for every one of the three scored
  comparisons (§2c) — not a wrong period, the absence of one, to a
  precision (`ss_tot` ratio `5.9×10⁻²⁷`) that rules out this being a
  subtle near-null a finer search might resolve. This is a **decisively
  stronger negative result** for this specific reduction than the official
  INCONCLUSIVE — closer in spirit to a REFUTE (a proof, not a data-driven
  band comparison, that this exact construction cannot produce T28's
  periodicity), though I do not force it into the pre-registered
  `rel_dev`/`R²` band, because that band presupposes two comparably-
  determined nonzero periods, a precondition this result does not meet
  (matching the sub-thread's own established treatment of `C80−C40`'s
  "runs to search boundary, no resolvable period" as its own distinct
  outcome, not a forced REFUTE/SUPPORT).
- **This does NOT refute the y-wall echo mechanism class.** Exactly as
  MATERIALS' and EM's own reviews independently note, and as §2d states
  explicitly: the full (non-edge-reduced) aperture sum, and the far-edge/
  far-wall pair, remain untested, and `phase1_proposal.md`'s own §3.2
  argument leaves open whether the flat result generalizes to them. A
  proof that one specific, disclosed idealization (edge-dominance +
  single-near-wall) predicts zero signal is not a proof about the
  mechanism class as a whole — matching this program's own established
  distinction (exp-077's own Red Team audit, §2a: "what has actually been
  shown REFUTEd... is narrower than [the write-up's] 'Next' section
  states").

**Recommended record language (same-shift addendum, not a rewrite of
frozen numbers, §6 item 1)**: `phase4_results.md`/`NOTES.md` should state,
alongside the official Test-A result, that a further, internally-consistent
correction (this audit) shows the edge-image/single-near-wall reduction
predicts no oscillatory signal at all under its own rigorously-derived
incidence angle — narrowing, not reversing, the official INCONCLUSIVE, and
sharpening the case against building the full propagator on the *current*
edge-dominance idealization specifically, pending §2d's own open
generalization question.

---

## 6. Mandatory-fix docket (same-shift, zero new FDTD)

1. **[§5, this audit]** Add an addendum paragraph to `phase4_results.md`/
   `NOTES.md`'s "Combined result" section stating this audit's own
   doubly-corrected finding (§2, §5) — do not edit the frozen Test-A
   numbers themselves.
2. **[F6a/F4, VISION/THERMODYNAMICS]** Replace `phase1_proposal.md` §5.2's
   stale per-config table with the corrected values (already in
   `primary_model_period_search.chosen`, quoted in full at §0.2/§2 of
   VISION's own review) — a same-shift copy-in, zero new computation.
   Either backfill `as_filed_incorrect_audit_trail` with true per-config
   as-filed data for a genuine audit trail, or delete the stale table
   entirely (THERMODYNAMICS' own stated preference; either resolves the
   R4 gap).
3. **[F4, THERMODYNAMICS]** Correct the "`≥99.9999%`" digit wherever it
   appears in the corrected write-up to `≥99.9996%` (the true worst-case
   value at `C80`'s own `|r|max=0.0018892`, verified independently at
   §0.2/§3 of THERMODYNAMICS' own review; I did not independently re-derive
   the 247.9× ratio but the underlying `|r|` bounds are confirmed real
   numbers straight from the committed JSON).
4. **[F5, QUANTUM]** Wire the Fisher-combined omnibus p-value (`p≈0.148`
   period, `p≈0.632` R², independently reproduced at §0.5) into
   `phase4_null_calibration_corrected_results.json` as two new fields,
   computed from the three per-target p-values already in hand — zero new
   Monte Carlo trials.
5. **[§2c, this audit — new]** Add a `ss_tot`-scale sanity check to
   `free_period_with_widening`'s own diagnostic output (or a documented
   caveat at its call sites): before trusting a high-`R²` period fit,
   compare the array's own `ss_tot` to a reference scale (e.g. the real
   data's own `ss_tot` on the identical statistic) and flag when it sits
   many orders of magnitude below — the exact trap this audit's own §2c
   fell into on a first pass before diagnosing it, and a generically
   reusable hardening for this sub-thread's entire period-search
   machinery, not specific to this cycle's own doubly-corrected model.
6. **[F1, PHOTONICS]** No fix owed — disclosed idealizations (§6.2/§6.7),
   correctly scoped as open questions, not defects.
7. **[F2, MATERIALS]** No fix owed to this cycle's own record — MATERIALS'
   own re-ranking (retarget the realizable-admittance refit to the x-wall)
   is a ranking decision, folded into §7, not a correction to anything
   filed.

None of these seven items touch `y_wall_prescreen.py`'s own frozen Test-A
numbers, `lab/`, or the official Combined Verdict — all are record-
completeness fixes, matching this program's own established "catch and
close same-shift" pattern.

---

## 7. Reconciled Iteration-56 ranking (all six seats + this audit)

Six seats' own top-3 lists converge more than they diverge once EM's
finding (§2) is folded in as the gating question for anything built on the
`90−θ_beam` convention specifically. Reconciled by information density per
unit cost, zero-FDTD desk items first (this program's own established
Tier-0 practice):

### Tier 0 — zero FDTD, desk-only, run as one batch

1. **Does the flat/zero-amplitude result (§2) generalize from the
   single-edge reduction to the FULL (non-edge-reduced) y-mirrored
   aperture sum?** (Merges EM #2 and QUANTUM #3, sharpened into a
   concrete, answerable question by this audit's own §2c/§2d.) Each
   aperture point has its own per-point rigorous bounce angle (unlike the
   single-edge case's shared constant); `phase1_proposal.md`'s own §3.2
   stationary-phase argument (no interior stationary point over
   `36°–42°`) already predicts edge-domination should hold for the full
   sum too, but this is a prediction, not yet computed. This is now the
   single most information-dense item on the board: if it confirms
   edge-domination generalizes and the flat result survives, the y-wall
   *self-echo-off-the-near-wall* coherent-echo sub-class (not merely this
   pre-screen's own reduction) is close to formally exhausted at the desk
   level, without ever writing the full propagator; if it does NOT
   generalize (a real possibility, per EM's own honest framing), that is
   itself the discovery of genuine θ-dependence this six-cycle sub-thread
   has never found evidence for, and would justify the full build for the
   first time.
2. **Refresh `phase1_proposal.md` §5.2's stale table and resolve the
   `as_filed_incorrect_audit_trail` gap** (docket items 2–3, §6). Trivial,
   zero cost, run alongside item 1 regardless of its outcome.
3. **Retarget the still-unexecuted realizable-admittance (`μ_r=1`) refit
   at the X-WALL's own two-wall model**, not the y-wall (MATERIALS' own
   re-ranking, §0.3-confirmed: the y-wall's period is admittance-choice-
   invariant, Pearson r>0.9997; the x-wall's marginal Test-B numbers
   (`r²=0.0001–0.0418`, exp-077) remain the only place this substitution
   could plausibly move a verdict). Carried from exp-077's own Iteration-55
   ranking, still unexecuted two cycles later.
4. **Wire the Fisher-combined omnibus statistic into the committed
   null-calibration record** (QUANTUM #1, docket item 4, §6) — prevents a
   future reader from citing the degenerate joint SUPPORT-count as "nothing
   here is even mildly close to a signal" when the honest omnibus number is
   a materially more precise, still-non-significant, characterization.
5. **Gate the already-collected 750nm two-wall X-WALL spot-check with a
   properly-sized null and decide** (carried unexecuted from exp-077's own
   ranking through exp-078 unchanged — PHOTONICS/EM, the single oldest
   deferred item on the whole T28 board). Contingent on nothing above;
   costs nothing to finally clear.
6. **Add the `ss_tot`-scale sanity guard to the shared period-search
   diagnostic** (docket item 5, §6, this audit's own new finding) —
   prevents a future cycle from being misled by a spuriously high R² on a
   near-flat array the way this audit's own first pass at §2c was.
7. **Pre-register the amplitude/normalization convention for any future
   Test-B build, BEFORE it is built** (VISION #2 — a forward R9 guard,
   this seat's own standing charter duty). Cheap, documentation-only, and
   directly forecloses a fourth instance of R9's own failure shape in this
   exact sub-thread.
8. Contingent on item 1's outcome only if it shows real generalized
   θ-dependence: **`|r(θ)|`-weight the self-echo proxy curve and re-score**
   (PHOTONICS #1/THERMODYNAMICS #1) and **add the far edge/far-wall image
   pair** (PHOTONICS #3) — both explicitly deferred behind item 1 here,
   since both are refinements of the `90−θ_beam`-convention model that
   item 1 may render moot; not deleted from the board, re-sequenced.

### Tier 1 — cheap FDTD, next

9. **The full-width, non-aliased second-wavelength (`G40`) leg** (QUANTUM
   #2 — the standing precondition, now deferred across THREE consecutive
   cycles: exp-076, exp-077, exp-078). The cheapest remaining FDTD test of
   whether T28's periodicity is a real, wavelength-scaling-consistent
   physical effect at all, independent of which mechanism is being chased.
10. **Broadband pulsed reflectance spectroscopy of the `ABSORB` boundary**
    (THERMODYNAMICS #3, carried from Iteration 53). A genuinely orthogonal
    instrument class, still unexecuted.

### Tier 2 — the standing charter-relevant test

11. **Test whether the `PAD`-sensitivity survives with a real absorbing
    article loaded** (VISION #1/THERMODYNAMICS #2 — now deferred across
    THREE consecutive cycles: exp-076, exp-077, exp-078, each one's own
    ranking naming it explicitly and each one declining to run it). Per
    the Iteration-54 ranking's own standing instruction ("should not be
    deferred a third time without an explicit reason"), this cycle gave no
    such reason — it is now the single most overdue item on the whole T28
    board and should not be deferred a fourth time without one stated
    explicitly in Iteration 56's own synthesis.

### Tier 3 — governance

12. **Explicit ruling on whether the coherent-echo mechanism-class board
    is exhausted** (QUANTUM #3). **Ruled here: NOT YET RIPE — Checkpoint
    criterion 2 does not fire.** Per §5 above: one specific reduction
    (x-normal, unrealizable admittance, exp-075/077) is REFUTEd; a second
    specific reduction (y-normal, single-near-wall, edge-dominance) now
    predicts zero signal under its own rigorous angle, which is a stronger
    result than an ordinary REFUTE but is, structurally, still one
    reduction's own result, not the class's. At least four concrete,
    unpriced items remain open (item 1's own generalization question, the
    far-wall/far-edge pair, the x-wall's realizable-admittance refit, and
    the wavelength-generality leg, item 9) — matching this program's own
    non-firing precedent for this exact criterion (exp-077's own Red Team
    audit, §5 criterion 2, "not yet ripe").

### Tier 4 — record hygiene (bundle, zero cost, run alongside any of the above)

13. This audit's own mandatory-fix docket (§6, items 1–7 in full).

None of the above re-opens or re-proposes any RULED-OUT item (R1–R9); item
1's own full-aperture-sum question and the x-wall realizable-admittance
refit are new instances of the already-permitted coherent-echo mechanism
class applied to configurations no prior cycle has tested, not
resurrections of anything closed.

---

## 8. Bottom line

**Verdict: PARTIAL** — unanimous across all six blind Phase-5 reviews and
this final audit. The y-direction wall-echo pre-screen's own official
Test-A result (INCONCLUSIVE, 0/3 SUPPORT, 0/3 REFUTE, under the `90−θ_beam`
convention Phase 2/3/4 correctly adopted for the specific bug three
critics caught) stands, verified bit-exact. **This audit's own independent
confirmation and quantification of ELECTROMAGNETISM's Phase-5 finding is
the cycle's most consequential result, net of everything**: even that
"corrected" angle is not the physically rigorous one for this reduction's
own point-source construction, and the rigorously-derived angle (a
per-config constant, 13.7°–15.0° from the y-wall's own normal, independent
of the swept beam angle) collapses the model's predicted signal to exactly
zero — not a wrong period, the absence of one, to a precision 26 orders of
magnitude below the real data's own scale (§2c). This **sharpens** the
official INCONCLUSIVE into a decisive negative for the specific
edge-image/single-near-wall reduction, without reversing it into a formal
REFUTE (the pre-registered band does not fit a zero-amplitude prediction)
and without closing the y-wall mechanism class as a whole (the full
aperture sum and far-wall pair remain untested, §2d, §5). **Checkpoint
criterion 4 does not fire** — three genuinely independent Phase-5 findings
(EM's angle-within-angle defect, VISION's stale table, THERMODYNAMICS'
partially-executed docket item) were all caught within this same cycle's
own review layer, none surviving unexamined to this document, matching
this program's own established non-firing pattern (Iterations 51, 53) and
distinguished explicitly from its firing precedents (Iterations 49, 50, 52,
54) at §4. T28's own substantive mechanism question — the ~2.84°-family
periodicity's ultimate origin — remains open, narrowed this cycle toward
"not an x-normal, unrealizable-admittance echo, and not a y-normal
single-near-wall edge-image echo evaluated at its own correct angle
either," with the single highest-value next move (§7 Tier 0 #1) being
whether that same zero-signal result generalizes to the full, non-reduced
aperture sum — the one question that could, cheaply, close an entire
mechanism sub-class at the desk level for the first time in this
seven-cycle-deep sub-thread's history.
