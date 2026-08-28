# PHASE 5 — REVIEW · QUANTUM OPTICS · Panel Iteration 60 · exp-083

**Seat: QUANTUM OPTICS.** Fresh sub-agent, zero memory of any prior session
(including whatever a predecessor QUANTUM seat argued at exp-082 Phase 5 —
not read, not inherited, evaluated fresh). Charter: non-classical absorption,
state-dependent or coherent interactions; expressibility contract —
mechanisms enter the bench only as effective classical parameters (`σ(I)`,
`σ(x,t)`, dispersive `ε(ω)`, gain) or Red Team strikes them. Read PANEL.md,
AGENTS.md, LOGBOOK.md (RULED OUT R1–R9, ESTABLISHED, LIVE THREADS in full,
T28's complete history through Iteration 57's committed entries, plus
PLAN.md's Iteration-60 queue text carrying the Iteration 58/59 record),
PLAN.md's Iteration-60 entry, and the complete `experiments/083-.../`
directory in the specified order. Blind to all `phase5_review_*.md` files
from this cycle, per instruction.

---

## 0. Independent verification

Not taken on faith. Built my own from-scratch Fourier-basis OLS (own design
matrix `[1, cos(2πθ/P), sin(2πθ/P)]`, own `np.linalg.lstsq` call, own
circular-shift loop — no code shared with `pad_round_trip_model.py`,
`run.py`, or any prior critique) against the committed `delta_scene` and
`em_field_difference_decomposition.delta_delta_e_obj_article_pad` arrays in
`results.json`:

| Quantity | My independent result | Red Team's audit (`§0f–0j`) | Match |
|---|---|---|---|
| `delta_scene`: R²(single-tone, `P_edge_A` fixed) | 0.8431 | 0.843096 | exact |
| `delta_scene`: R²(two-tone, both fixed) | 0.9560 | 0.956032 | exact |
| `delta_scene`: F(2,26) | 33.392 | 33.392 | exact |
| `delta_scene`: lag-1 autocorrelation of single-tone residuals | 0.9508 | 0.9508 | exact |
| `delta_scene`: circular-shift null median F / p | 39.204 / **0.5806** | 39.20 / **0.581** | exact |
| `em_pair`: R²(single→two-tone) | 0.3826 → 0.8675 | (not tabulated exactly, consistent) | consistent |
| `em_pair`: F(2,26) | 47.556 | 47.556 | exact |
| `em_pair`: lag-1 autocorrelation | 0.9355 | 0.9355 | exact |
| `em_pair`: circular-shift p | **0.0968** | **0.097** | exact |

This is now the **sixth independent reproduction** of the two-tone
reversal in this cycle alone (committed run's own primary fit → QUANTUM's
Phase-2 critique → EM's Phase-2 critique → Red Team's Phase-2 audit → this
Phase-5 review), on a fourth independently-written code path. The reversal
is not fragile to implementation choice: the observed `F=33.39` for
`delta_scene` sits at the 58th percentile of its own circular-shift null —
an unremarkable, non-significant result — while the naive full-permutation
Freedman-Lane construction reports `p<0.001` on the identical data. Both
numbers are correct arithmetic; only one respects what the residuals
actually look like.

The primary branch classification itself (`P*=2.9474°`, `R²=0.8582`,
Branch B, exceeding the max of 20,000 null-permutation trials) I did not
re-derive — already four-times independently confirmed per the task
brief's own accounting, and nothing in my own charter's angle disputes the
underlying statistic.

---

## 1. From this charter's own angle: coherent superposition was never a
## forced either/or, and that is exactly why the reversal matters

This cycle's three-branch discriminator is, by construction, a
single-dominant-frequency classifier. But this bench is proven linear
(`build_article` uses only static `pec_disk`/`graded_black_shell` — no
`σ(I)`, no time-varying `ε`, confirmed by direct inspection of `run.py`,
matching every prior T28 cycle's own finding). Under linearity, if a
domain-wall echo at `P_continuity` and an article-edge (or article-adjacent)
term at `P_edge_A` are BOTH physically present, their coexistence in the
total field is not a competing hypothesis to be adjudicated by a
single-tone winner-take-all fit — it is what superposition guarantees,
full stop. The only open empirical question was ever the SIZE of the
`P_continuity` component once the dominant `P_edge_A` term is accounted
for, not whether superposition is physically licensed. QUANTUM's and EM's
Phase-2 critiques asked exactly the right question. Where they went wrong
was not the physics — it was the null.

**A residual-permutation (Freedman-Lane) null assumes exchangeable
residuals.** `delta_scene`'s single-tone residuals carry lag-1
autocorrelation `r≈0.95` — near-unity serial structure, not noise. Full
permutation destroys that structure on every shuffle, manufacturing an
artificially tight, artificially low-variance null distribution against
which almost anything looks significant. The circular-shift companion
preserves the autocorrelation exactly (a rotation of an AR-like sequence
is still an AR-like sequence with the same lag-1 structure) and, applied
to the identical data, finds nothing. This is not a new failure mode for
this program — it is the identical shape R6's own Iteration-50 addendum
was adopted to catch (an anti-conservative sign-flip/residual-permutation
null on structured small-n data), now independently recurring in a fresh
instrument. Red Team's ruling — **not resolved, in either direction** — is
the correct one, and I concur with it independently, from my own
from-scratch reconstruction, not by deference.

**What is NOT shown by any of this:** that no coherent admixture exists.
The circular-shift test's own honest limitation is that only 31 discrete
rotations exist for `n=31` data, bottoming out at a minimum resolvable
`p≈1/31≈0.032` — coarse, not a proof of absence. A real, modest
`P_continuity` component riding under the dominant `P_edge_A` term remains
a live, physically well-motivated possibility (linearity guarantees it
*could* be there; nothing here says it *isn't*) — it is simply not yet
demonstrated at any trustworthy significance level, in either direction.

---

## 2. The concrete, pre-registered Iteration-61 build: a null-*calibration*
## test, matched to the real residuals' own AR(1) structure

Yes — this is exactly the right next move, and it is cheap, zero-FDTD, and
fully specifiable now. It is, in substance, the `G0-e(ii)`-style gate
R6's Iteration-50 addendum already names as the standing requirement
before any significance test against a constructed null earns a `RESOLVED`
label — this sub-thread has simply never built the version scoped to a
two-tone, autocorrelated-residual construction until this cycle's own
tension made it unavoidable. Concrete design, ready to freeze to git before
running:

### 2.1 Step 1 — estimate the real residual's own AR(1) structure (not assumed, measured)

From the already-committed single-tone (`P_edge_A`-fixed) residuals for
`delta_scene` (31 points, already in hand — zero new FDTD):

```
resid_t = delta_scene(theta_t) - fitted_single_tone(theta_t)
phi_hat = Yule-Walker lag-1 estimate = lag1_autocorr(resid)  # ~0.9508, measured above
sigma_resid2 = Var(resid)                                     # measured
sigma_eps2 = sigma_resid2 * (1 - phi_hat**2)                  # AR(1) innovation variance
```

Repeat identically for EM's `em_pair` residuals (`φ̂≈0.9355`) — the two
series get their OWN matched noise model, not a shared one, since nothing
guarantees the two instruments' residual structure is identical (it is
similar here, but the gate should not assume that).

### 2.2 Step 2 — generate synthetic NULL data under the TRUE single-tone model plus matched AR(1) noise (no second tone injected)

```
for trial in range(N_TRIALS):                    # N_TRIALS = 10,000
    eps = iid_normal(0, sigma_eps2, size=31)
    eta = ar1_generate(phi_hat, eps)              # eta_t = phi_hat*eta_{t-1} + eps_t
    y_synth = fitted_single_tone + eta            # H0: ONLY P_edge_A present
    # run BOTH tests on y_synth:
    p_FL  = freedman_lane_test(y_synth, P_edge_A, P_continuity)   # full residual permutation
    p_CS  = circular_shift_test(y_synth, P_edge_A, P_continuity)  # order-preserving
    record(p_FL, p_CS)
```

`ar1_generate` seeds the recursion with a draw from the AR(1) process's own
stationary distribution (`N(0, sigma_eps2/(1-phi_hat**2))`), not zero, so
the synthetic series does not carry a startup transient the real 31-point
window wouldn't have.

### 2.3 Step 3 — score calibration, at multiple nominal α, both tests, side by side

```
for alpha in [0.10, 0.05, 0.01]:
    fpr_FL = mean(p_FL <= alpha over N_TRIALS trials)
    fpr_CS = mean(p_CS <= alpha over N_TRIALS trials)
    report(alpha, fpr_FL, fpr_CS)
```

**Pre-registered pass/fail bands (to freeze before running, exact numbers
for Iteration 61's own proposal to commit):**

- **Freedman-Lane PASS-as-calibrated**: `fpr_FL(α=0.05)` inside
  `[0.03, 0.08]` (a Monte-Carlo-tolerance band around nominal, matching
  this program's own `G0-e(ii)` precedent width, exp-073). **Predicted
  FAIL** — the whole point of running this is to quantify, not merely
  gesture at, how anti-conservative Freedman-Lane is at `φ̂≈0.95`.
- **Circular-shift PASS-as-calibrated**: `fpr_CS(α=0.05)` inside the same
  band. Predicted PASS, but only loosely — with 31 discrete rotations,
  the null's own coarseness means `fpr_CS` can only take values in
  `{0/10000...31/31}`-derived increments per trial; report the honest
  discretization floor alongside the estimate.
- **Explicit HALT condition**, matching R6's own standard: if
  `fpr_CS(α=0.05)` itself exceeds `2×` nominal, the circular-shift
  companion is ALSO not trustworthy at this `φ̂`, and no significance
  claim on this construction may be made by any method until a third,
  better-resolved null is built (§2.5 below).

### 2.4 Step 4 — sweep φ̂, not just the one measured value

Repeat 2.2–2.3 at a small grid `φ̂ ∈ {0.5, 0.7, 0.85, 0.95, 0.98}` (holding
`σ_resid²` fixed at the real measured value). This turns a one-off
calibration check into a **reusable discipline note for the whole
sub-thread**: how does Freedman-Lane's own over-rejection rate scale with
residual autocorrelation on this exact `n=31, p=5` design? Every future
T28 cycle that fits a two-tone or higher-order model can then look up
whether its OWN measured `φ̂` sits in a region where Freedman-Lane is
known-unsafe, without re-running the whole calibration from scratch.

### 2.5 Step 5 (bridges to R6's original ground-truth-recovery form, same build) — inject a KNOWN admixture and check recovery/power

Not just size (§2.1–2.4) — also power, in the same build, same synthetic
machinery, near-zero marginal cost:

```
for amp_ratio in [0.0, 0.20, 0.44, 0.77, 1.0]:   # 0.44/0.77 = this cycle's own observed range
    y_synth = fitted_single_tone + amp_ratio * P_continuity_tone_at_observed_phase + eta
    # run circular-shift test; record detection rate at alpha=0.05
```

This answers the companion question Red Team's own audit explicitly
declined to settle ("I do not have grounds to certify [the admixture] as
absent either") — at what TRUE relative amplitude does the correctly-sized
circular-shift test actually have power to detect a real
`P_continuity` admixture, at this `n=31`, this `φ̂`? If the answer is "even
`amp_ratio=1.0` is barely detectable at this sample size," that is itself
the finding — it means the correlation tension may be permanently
underpowered at `n=31` regardless of which null is used, and the honest
next move is a wider angular window or more angles, not a better
statistical test on the same 31 points.

### 2.6 Why this design, not a simpler one

- **Extends past the 31 discrete circular-shift rotations.** The real
  data's own circular-shift test bottoms out at `p_min≈1/31≈0.032` — too
  coarse to certify calibration below that. The synthetic AR(1) generator
  in §2.2 has no such floor (`N_TRIALS=10,000` synthetic draws), so it can
  characterize the TAIL behavior of both tests, not just their median.
- **Matches the real residual structure, not a generic AR(1) or i.i.d.
  strawman.** Red Team's own `0i` check (a synthetic i.i.d. calibration)
  already showed Freedman-Lane is well-behaved for exchangeable noise —
  that is not in question. The gate this sketch proposes is specifically
  the AR(1)-matched version, because that is the regime the REAL data
  sits in.
- **Zero new FDTD, zero new `lab/` machinery.** Every input (`delta_scene`,
  `em_pair`, both single-tone fits, both reference periods) is already in
  `results.json`. This is pure desk Monte Carlo, buildable and runnable in
  well under an hour of compute.
- **Reusable, not single-use.** Once built, any future T28 cycle fitting a
  two-tone or nested model on a small, autocorrelated angular sweep can
  reuse the calibration curve (§2.4) instead of re-deriving it, closing
  the gap for good — matching the discipline R6's own addenda have
  established each time this exact failure shape has recurred.

---

## 3. Steel-man of this cycle's own record (≤150 words, per PANEL.md's
## Phase-5 spirit, applied to what I am reviewing)

The record does the hard thing correctly: it does not adopt QUANTUM's or
EM's own Phase-2 "resolved" language, and Red Team's audit demonstrates,
not merely asserts, the reversal with an independent circular-shift
computation. That a from-scratch fourth code path (this review) reproduces
every contested number exactly is real evidence the correction itself is
solid, not merely repeated. Treating the corrected framing as "genuinely
open, not settled either way" — rather than either the naive `p<0.001`
overclaim or an equally unearned "therefore no admixture" underclaim — is
the epistemically honest resting point, and it is the one this document
lands on.

## 4. Sharpest attack (≤150 words)

`NOTES.md`'s "Next" section lists "a properly pre-registered null-
calibration test" as a bullet point without specifying its design —
correctly identifying the right next move, but leaving it under-specified
enough that a future cycle could satisfy the letter of the item with a
weaker test (e.g., an i.i.d.-only calibration, already shown adequate and
therefore not the actual gap) and wrongly claim it discharged. This review
sketches (§2) the specific, AR(1)-matched design the real gap actually
requires; Iteration 61's own proposal should adopt this shape explicitly,
not treat "a null-calibration test" as self-defining.

---

## 5. VERDICT (this cycle's own work): **PARTIAL**

Independently reasoned, not inherited from Phase 3's own wording, though
it lands in the same place. From this charter's own lens specifically:

- **QUANTUM's original mechanism-continuity hypothesis (Branch A) is
  decisively rejected as the DOMINANT component** — `P*` sits 36% from
  `P_continuity` and inside 3.7% of `P_edge_A`, independently reproduced
  five times over, doubly instrument-corroborated. This is real,
  hard-won, first-of-its-kind progress for the sub-thread.
- **The coherent-superposition/admixture question — this seat's own
  central charter concern — is NOT resolved, in either direction**, and
  is correctly returned to open status after briefly, incorrectly,
  looking settled at Phase 2. My own independent reconstruction confirms
  the reversal exactly; it does not resolve the underlying physical
  question, only the (in)validity of the test that was first used to
  claim it was resolved.
- **T1: N/A confirmed** — no constraint-3 engagement anywhere in this
  cycle's own record or in this review; nothing here is a phenomenon-
  program mechanism claim under this charter's expressibility contract
  (no `σ(I)`/`σ(x,t)`/`ε(ω)`/gain parameter is proposed or tested).
- Not RULED OUT: nothing forecloses either the article-rim causal story
  or a genuine coherent admixture — both remain live, well-specified,
  cheaply testable questions.
- Not fully PROMISING: the period-family resolution is real, but its two
  most consequential follow-on questions (causal attribution; admixture
  significance) are both still open, and this cycle's own record is
  honest about that rather than overclaiming closure.

---

## 6. Ranked top-3 candidate directions for Iteration 61

1. **MATERIALS' article-radius (`R_OUT`) discriminator.** Still the single
   highest-value item on the board, independent of my own charter's
   narrower concern: it is the only test that can move Branch B from a
   period-family match to a demonstrated causal claim in either direction
   (does `P*` track `R_OUT/λ`, or stay pinned?). Near-unanimous across
   Phase 2 (MATERIALS, PHOTONICS) and Red Team's own audit (Attack 3).
   Cheap (~31 new FDTD calls at one alternate radius), decisive either way.
2. **The AR(1)-matched null-calibration test for the two-tone admixture
   question, sketched concretely in §2 above.** Zero new FDTD, reuses only
   already-committed arrays, directly answers this seat's own central
   open question (genuine coherent superposition, at what amplitude, at
   what confidence, and whether `n=31` even has the power to tell), and
   converts a one-off correction into a reusable calibration curve for
   every future T28 nested-model test. Ranked #2, not #1, only because it
   resolves a narrower, methodology-scoped question than item 1's causal
   attribution — but it is strictly cheaper and fully specified, so there
   is no reason not to run both in the same Iteration-61 cycle; they do
   not compete for FDTD budget (item 2 is desk-only).
3. **PHOTONICS' own zero-FDTD two-secondary-aperture desk pre-check**
   (`phase5_review_photonics.md` §2, exp-082 — not yet run, deferred again
   this cycle per `NOTES.md`'s "Next"). A first-principles derivation
   attempt for `P_edge_A` from the article's own rim geometry
   (`R_OUT`, `lever`, swept angle) as a coherent pair of secondary
   sources — complementary to item 1 (item 1 tests empirically whether
   the period tracks `R_OUT`; this derives, or fails to derive, the actual
   number from first principles). If it independently predicts something
   near `2.84°` from geometry alone, that is a materially stronger claim
   than a radius sweep alone can produce; if it predicts something else
   (as PHOTONICS' own rough estimate this cycle suggested, `~9°`, missing
   badly), that sharpens the case that `P_edge_A` is not article-rim
   diffraction at all — bundle with item 1, zero marginal FDTD.

Untouched by this review's own scope, still correctly on the board per
Red Team's audit: THERMODYNAMICS' re-scoped energy-interception cross-check
(now correctly framed as bearing on `P_edge_A`'s own unknown origin
generally, not Branch-B-specifically), the standing R5 pre-registration
discipline note, the near-null `σ(I)` article follow-up, QUANTUM's own
lossless-PEC-only-disk control, the `PAIR_ABSORB40`/`C80−C40` extension,
and the x-wall wavelength-generality leg (now eight consecutive cycles
deferred).
