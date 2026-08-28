# PHASE 5 — REVIEW · ELECTROMAGNETISM · Panel Iteration 60 · exp-083

**Seat: ELECTROMAGNETISM.** Fresh sub-agent, zero memory of any prior
session. Charter: field/wave behavior, impedance matching, energy coupling —
owns the reciprocity/passivity/causality bookkeeping, formalizing what T1
permits and forbids for each proposal. Read `PANEL.md`, `AGENTS.md`,
`LOGBOOK.md` (RULED OUT R1–R9, ESTABLISHED, LIVE THREADS in full — T28's
complete Iteration 46–59 history), `PLAN.md`'s Iteration-60 queue, and the
complete `experiments/083-.../` record in the specified order
(`phase1_proposal.md`, `NOTES.md`, `run.py`, `results.json` spot-checked,
`run_output.txt`, `null_permutation_control.json`, all five Phase-2
critiques, `phase2_redteam_audit.md`, `phase3_synthesis.md`). Blind to any
other seat's Phase-5 review this cycle, per PANEL.md.

**No RULED-OUT item (R1–R9) is re-proposed here.**

---

## 0. What I independently verified, from primitives, not taken on faith

The task brief singled out one finding for genuine independent re-check —
Red Team's own reversal of the two-tone "resolved admixture" claim (lag-1
autocorrelation, circular-shift null p=0.581/0.097). I did not re-read that
finding and agree with it; I rebuilt it myself, a fourth independent
implementation after the committed run, QUANTUM's critique, EM's own
Phase-2 critique this cycle, and Red Team's audit — different code, closed-
form `np.linalg.lstsq` OLS over the fixed `[P_edge_A, P_continuity]` design,
pulling only the raw `delta_scene`/`em_field_difference_decomposition`
arrays from the committed `results.json`.

| Claim | Reported (Red Team §0) | My independent recomputation | Match |
|---|---|---|---|
| Single-tone `R²` (`P_edge_A` fixed), `delta_scene` | 0.843096 | 0.8430958569830258 | exact |
| Two-tone `R²`, `delta_scene` | 0.956032 | 0.9560323462892159 | exact |
| `F(2,26)`, `delta_scene` | 33.392 | 33.39214711428563 | exact |
| Lag-1 autocorrelation of single-tone residuals, `delta_scene` | `r≈0.9508` | `r=0.9508355827712793` (Pearson, `resid[:-1]` vs `resid[1:]`) | **exact** — I first computed the variance-ratio form of lag-1 autocorrelation (`0.927`) and got a mismatch; switching to the Pearson-correlation-of-shifted-subsamples form (the statistically standard sample-ACF estimator) reproduced Red Team's figure to 10 significant digits. Worth naming explicitly: two textbook-legitimate lag-1 estimators exist and disagree by ~2.5 points here (0.927 vs 0.951) — Red Team's own write-up doesn't state which it used; a future cycle citing "lag-1≈0.95" should cite the estimator, not just the number. |
| Lag-1 autocorrelation, EM's field-difference pair (`P_edge_A`-fixed baseline) | `r≈0.9355` | `r=0.9354599437752598` | exact (same estimator note applies) |
| Full-permutation Freedman–Lane `p`, `delta_scene` | `<5×10⁻⁶` (0/200,000, EM's own Phase-2 figure) | `p=0.000035` (200,000 trials, independent seed) — consistent, no dissent | matches (MC tolerance) |
| **Circular-shift null, `delta_scene`: `F_obs=33.39` vs its own 31 rotations, `p=0.581`** | `p=0.5806` | `p=0.5806` (18/31, strict `F_shift > F_obs`) — **exact**, including the discrete count | **exact** |
| Circular-shift null, EM field-difference pair: `p=0.097` | `p=0.0968` (implied 3/31) | `p=0.0645` (**2/31**, strict `>`) — using inclusive `≥` (self counts as a tie) instead gives `3/31=0.0968`, matching Red Team's figure exactly | **small, disclosed, non-substantive discrepancy** — see §1 |

**Everything load-bearing reproduces, most of it to the literal integer
count.** One genuine, minor gap: my strict-inequality convention gives
2/31 for the EM-companion circular-shift test where Red Team's own number
implies 3/31 (a tie-handling convention difference, not a computational
error — I found a clean gap in the sorted null distribution around
`F_obs=47.556`, no near-boundary float sensitivity, so this is not
floating-point noise). Both conventions land in the same qualitative place
(`p≈0.06–0.10`, nowhere near conventional significance either way, not
outcome-determining for anything gated this cycle since the EM companion's
two-tone reading was never gating to begin with). Flagged for the record
per this program's own R4 discipline (a cited figure should be exactly,
not approximately, reproducible) — not a Checkpoint-worthy gap given zero
outcome dependence, but worth a one-line convention note in whatever
document next cites it.

**Conclusion of this section: Red Team's reversal is genuine, not an
artifact of a single implementation's choices.** The Freedman–Lane/
circular-shift disagreement — highly significant under one null,
unremarkable under the other, on the identical data and identical test
statistic — reproduces independently, down to the literal permutation
count for the primary (load-bearing) series.

---

## 1. The assigned physics question: is a circular-shift null the right one here, on EM grounds?

This is squarely my charter's own question — field behavior over a swept
angle, and what structure of the physical system licenses treating that
sweep as if it had periodic boundary conditions. **Short answer: circular-
shift is a legitimate, order-preserving improvement over full permutation
(it was the right call relative to Freedman–Lane), but it is not the
best-suited null for this specific angular sweep, and the physical reason
is concrete, not a vague caution.**

### 1a. There is no periodic boundary condition in θ here

A circular-shift null is exactly right when the sampled domain genuinely
wraps — a full 360° azimuthal scan around a scatterer, or a spatially
periodic lattice, where θ=42° being "adjacent" to θ=36° reflects a real
symmetry of the physical system. **That is not this geometry.** The swept
beam angle θ∈[36°,42°] is an open, one-way parameter sweep of the *source
direction* into a domain with ordinary (non-periodic) PEC/graded-loss
boundaries; nothing in `dg065.CONFIGS`/`run.py`'s own construction ties
θ=42.0° back to θ=36.0°. The wrap-around the circular-shift null imposes
is a pure resampling convenience borrowed from stationary time-series
statistics, not a symmetry of the field pattern being measured.

That alone doesn't disqualify it — resampling techniques routinely use
constructions with no literal physical counterpart (full permutation
itself has none either). The question is whether the wrap-around
*introduces an artifact this bench's own physics makes likely to matter*.

### 1b. The window is not an integer number of periods of either tested tone — the wrap manufactures a discontinuity the real data doesn't have

`P_edge_A=2.8421°` fits `6°/2.8421°=2.111` periods across `[36°,42°]`;
`P_continuity=4.611°` fits `6°/4.611°=1.301` periods. **Neither divides the
window evenly.** Every non-identity circular shift therefore splices the
residual sequence's own end back onto its own start at a point where the
underlying (non-periodic) signal has no reason to be continuous — a
synthetic discontinuity absent from the real, non-wrapping data. A single
jump discontinuity has broadband spectral content, and a low-order
sinusoid whose period is comparable to the window width (as
`P_continuity`'s 1.3-period fit is) can partially absorb a jump located
anywhere in the window — meaning the wrap artifact can inflate a rotated
surrogate's own two-tone `R²` for reasons that have nothing to do with
whether a genuine second physical component is present.

**This is not a hypothetical — it is visible in the null distribution
itself.** For `delta_scene`, the real (`k=0`) `F_obs=33.39` sits *below the
median* of its own 31 rotations (`38.53`); 18 of the other 30 rotations
exceed it, several by a wide margin (the null's own max is `228.3`, nearly
7× `F_obs`). A null distribution whose typical member out-scores the real
data on a nested-model comparison is exactly the signature a
wrap-discontinuity-inflated null would produce — the shift construction is
not merely "conservative," it may be actively manufacturing spurious
two-tone-favoring structure at some rotations, which happens to make the
real result look unremarkable by comparison. That is the right qualitative
direction for THIS cycle's own headline (it reinforces, not undermines,
"not significant" — see §1c), but it means the *p*-value's own numeric
value (`0.581`) should not be read as calibrated evidence of how
non-significant the result is, only as a directionally trustworthy but
mechanically noisy verdict.

### 1c. A better-suited null exists, I built it, and it makes the reversal MORE robust, not less

The physically cleaner construction doesn't assume periodicity at all: fit
an AR(1) model directly to the single-tone residuals' own measured serial
structure (`φ=0.9508`, the same Pearson lag-1 figure both Red Team and I
independently recovered), generate synthetic AR(1) noise realizations of
length 31 at that φ (no wrap, no boundary artifact — a genuine
finite-window stochastic-process surrogate), add each to the reduced
model's fitted values, and refit. This is the natural EM/statistics-native
analog of Red Team's own §0i i.i.d.-Gaussian calibration check, extended to
the ACTUAL (autocorrelated, not i.i.d.) residual structure this data has —
closing the exact gap NOTES.md's own "Next" item 2 names but does not
fill.

**Result, 50,000 trials, independently computed this review:**

```
AR(1)-parametric surrogate null (phi=0.9508, matched to measured residual autocorrelation):
  F_obs = 33.392
  null median = 78.44   null p95 = 255.4   null p99 = 356.0   null max = 1275.0
  p = 0.7663
```

**This is a MORE decisive non-significant result than the circular-shift
null's own `p=0.581`, not a wash.** The mechanism is well-known in time-
series statistics (Granger–Newbold "spurious regression," 1974): a process
with φ this close to 1 (near-unit-root) generates large, smooth,
low-frequency-looking excursions over short windows purely from its own
serial correlation — exactly the kind of structure a second low-order
sinusoid (`P_continuity`, 1.3 periods across the window) will fit
suspiciously well *by chance*, far more often than either a full-
permutation null (which destroys the correlation entirely, hence anti-
conservative) or a discrete 31-point circular-shift (which preserves
correlation but adds a wrap artifact) would suggest on their own. Two
structurally different, non-wrap-around-dependent constructions — the
discrete circular shift and the continuous AR(1) parametric surrogate —
now independently agree: `delta_scene`'s own two-tone improvement is
unremarkable against its own residuals' real serial-correlation structure.

**Answer to the assigned question, stated plainly:** no, circular-shift is
not the best-suited null on physical grounds for this open angular sweep —
there is no genuine periodicity in θ to justify the wrap, and the
window/period mismatch (§1b) manufactures an artifact. But this is not a
reason to distrust Red Team's reversal — it is a reason to *not yet trust
its exact p-value as calibrated*, while trusting its qualitative direction
more, now that a second, wrap-free, physically better-motivated null
(AR(1) parametric, directly calibrated to the measured φ) independently
lands in the same place, more emphatically. **Recommend, concretely, for
whatever Iteration-61 pre-registered null-calibration test gets built: use
the AR(1)-parametric surrogate (or a moving-block/reflected-boundary
bootstrap that likewise avoids wrap-around) as the primary null, with the
circular-shift kept only as a secondary, cross-checking companion — not the
reverse of this cycle's own ordering.**

---

## 2. Charter bookkeeping: reciprocity / passivity / causality — clean, and correctly scoped as T1: N/A

Confirmed by direct inspection of `run.py::build_article`/`_run_sim`:
every material in this cycle's own construction (`materials.pec_disk`,
`materials.graded_black_shell`) is static, linear, and passive — no
`σ(I)`, no time-varying `ε`, no gain medium anywhere in this cycle's own
code path (matching both predecessor findings this cycle's Phase 2 cites).
Under that confirmed linearity, EM's own field-difference decomposition
(`E_total ≡ E_no-article + ΔE_article`, §4b of `phase1_proposal.md`) is not
an approximation or a modeling choice — it is an algebraic identity, and
this cycle's use of it (persisting both legs, computing the exact
difference, free-period-fitting the difference) is the correct and only
way to exploit that identity. I have no correction to it.

Nothing in this cycle's own record touches T1 (the phenomenon's
central-tension escape routes) or any of the four founding constraints —
correctly and consistently disposed "N/A" in every document I read
(`phase1_proposal.md` §3, `NOTES.md`, `phase3_synthesis.md` §6). The
Branch-B period-family match and the two-tone admixture question are both
entirely about artifact attribution inside the FDTD instrument, not about
absorption, switching, angular selectivity, or sub-threshold operation —
Red Team's own Checkpoint-2 ruling (N/A, reasoned through explicitly, not
by precedent) is correct, and I concur for the same reason stated
independently: nothing here is expressible as, or bears on, a constraint-3
mechanism claim.

---

## 3. On Branch B's own causal label — I concur with the Phase 2/3 correction, with one addition

Five of five blind critiques and Red Team's own audit converged on
downgrading "ARTICLE-EDGE DIFFRACTION, confirmed" to "matches the
unexplained `P_edge_A` family, not yet shown article-intrinsic." I
independently reproduced the two numbers that drive this (§0c/0d of Red
Team's audit: `Δθ=9.452°`, a 3.326× miss; `N_F=13.08`, deep Fresnel/
near-field) exactly, above. I have nothing to add to the substance of that
correction — it is sound, and the record now states it correctly.

**One addition from my own charter's angle**, not raised elsewhere in this
cycle's record: whatever eventually explains `P_edge_A`, it must also
respect reciprocity. If MATERIALS' article-radius discriminator (Iteration
61's own top-ranked item) confirms an article-rim origin, the resulting
diffraction description should be checked for consistency with the
source–observer reciprocity this bench's own absorber-model work has
relied on since exp-002 — a genuine article-edge diffraction term is
reciprocal by construction (Babinet-type edge diffraction is a linear,
passive scattering process), so this is a low-risk, cheap confirmatory
check to fold into that same cycle rather than a new one, not a concern
that changes anything about this cycle's own verdict.

---

## VERDICT: **PARTIAL**

This cycle delivers a genuine, hard-won, first-of-its-kind result for this
nine-cycle-plus sub-thread — the article-loaded channel's dominant
periodicity is, for the first time, statistically pinned to a specific
established family, doubly instrument-corroborated (Weber-contrast and
EM's own linear field-difference pair, independently null-controlled). It
does not resolve, and does not claim to resolve (after the Phase 2/3
correction), what causes that periodicity, nor whether a second,
weaker `PAD`-continuity component genuinely coexists — the two-tone
question is now, if anything, MORE clearly unresolved than the record
states, per §1's own finding that even Red Team's own reversal likely
understates how unremarkable the two-tone improvement is. No constraint-3
ground is gained or lost; T1 stays N/A throughout, correctly. This is
real, board-advancing instrument work, not yet a mechanism finding.

## Ranked top-3 candidate directions for Iteration 61

1. **MATERIALS' article-radius discriminator** (re-run `PAIR_PAD` at an
   alternate `R_OUT`, checking whether `P*` tracks `R_OUT/λ` or stays
   pinned). I concur with the near-unanimous ranking — this is the only
   test that converts Branch B from a period-family match into an actual
   causal claim, and it is cheap (~31 calls, zero new machinery). Fold in
   my own §3 reciprocity spot-check as a zero-cost rider if it confirms
   article-rim origin.
2. **A pre-registered, wrap-free null-calibration test for the two-tone
   admixture question, replacing the circular-shift companion as primary**
   — build the AR(1)-parametric surrogate I ran above (§1c) as committed,
   reusable machinery (matching R6's Iteration-50-addendum standard: a
   synthetic calibration run BEFORE any real significance claim is
   trusted), calibrated to the actually-measured residual φ, with the
   discrete circular-shift retained only as a secondary cross-check. This
   is the single most concrete, actionable output of this review — it
   closes a gap this cycle's own record already flags as open but does not
   fill, and my own result above (§1c: `p=0.766`, more decisive than the
   circular-shift's own `p=0.581`) shows it is not merely a formality; it
   changes the confidence, not just the mechanics, of the conclusion.
3. **THERMODYNAMICS' re-scoped energy-interception item** — whatever
   ultimately explains `P_edge_A` (domain artifact or article rim) has
   never been shown non-dissipative under either reading; now that a real
   absorbing article sits in the same channel for the first time, this
   stops being a purely academic gap. Zero-FDTD, analytic, and its
   ingredients (`delta_scene`, both `ΔE_article` legs, the flagship's own
   established extinction figures) are all already sitting in this cycle's
   own committed `results.json` — the cheapest item on this list to
   execute.
