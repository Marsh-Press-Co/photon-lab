# exp-073 — MATERIALS' corrected re-issue of exp-072's differential/beat fit of `delta_AB(θ)`

**Panel Iteration 50.** Lead: MATERIALS (by rotation). Director synthesis
post Phase 2 (five blind critiques + Red Team's Phase-2 audit, verdict
PROCEED-WITH-MANDATORY-FIXES, 12-item docket, **zero items overridden** —
full record in `phase1_proposal.md`, `phase2_critique_{photonics,em,
thermodynamics,quantum,vision}.md`, `phase2_redteam_audit.md`,
`phase3_synthesis.md`).

## Mandate

PLAN.md's Iteration-50 queue, item 1 (unanimous across all six of exp-072's
Phase-5 seats, `experiments/072-t28-differential-beat-fit/
phase5_redteam_audit.md` §7.2): a corrected, zero-FDTD re-issue of exp-072's
own differential/beat-fit instrument, behind the new `G0-e` ground-truth
recovery gate (LOGBOOK R6) — nothing downstream of exp-072's own step 2 is
fully clean until this lands as a freshly pre-registered cycle. Folds in
three items exp-072's own same-shift docket deferred as new-gate additions
(not same-shift-safe): EM's `A_q = 2a_cbar·tan χ` table correction,
QUANTUM's sign-flip/residual-permutation null (replacing the
phase-randomized H₀-residual one), and VISION's reinstated sign-invariance
admissibility condition over the gate-admitted carrier set.

## Setup

Reads ONLY already-committed data — **zero new FDTD calls, zero `lab/`
diff**:

- `experiments/069-.../results.json` → `block_dense.rows` (C40, C80, 31
  points, θ=36–42°).
- `experiments/071-.../results.json` → `dense_causal.rows.C60/.C70` (same
  θ grid), `trend.linear_fit.slope` (`m0_native`, exp-071's own
  n_grid=400 slope, historical anchor only), `per_config_free_periods`
  (used to build the residual pool for `G0-e(ii)`'s robustness leg).
- `experiments/072-.../results.json` → `saturating_vs_linear.linear.slope`
  (`m0_resolved`, the n_grid=3000-resolved slope — the **operative**
  reference for the power table and P-073-4's rate comparison, docket item
  6), plus (disclosure only, non-gating) the real, already-closed `A_q`/
  `amplitude` values for every pair, used to correct the `χ0` "binds hard"
  prose (docket item 5).
- `experiments/069-.../run.py` → `_fixed_period_fit`, reused verbatim.
- `experiments/072-.../run.py`, used as this file's own base (per the
  task's own scoping instruction): `_amp_phase_at`, `carrier_fit`,
  `design_matrix`, the design-respecting residual bootstrap, and
  `holm_adjust` are reused unmodified (class (c), independently re-derived
  from scratch this cycle by ELECTROMAGNETISM, `phase2_critique_em.md` §1).

The instrument, unchanged in kind from exp-072: fit `delta_AB(θ) =
C_B(θ) − C_A(θ)` for the three adjacent `ABSORB` pairs (C40–C60, C60–C70,
C70–C80) plus the already-analyzed C40–C80, as a ramp in quadrature with a
common-mode carrier (`Cbar = (C_A+C_B)/2`, free-period-fit at
`n_grid=3000`). Full derivation: `phase1_proposal.md` §1–2.

## What changed vs. exp-072 (Red Team's 12-item docket, `phase2_redteam_audit.md` §5)

Implemented verbatim in `run.py`; full mapping and four disclosed
implementation-level judgment calls in `phase3_synthesis.md` §2–3. Summary:

- **The gating null is replaced.** T2-3: a Freedman–Lane-style sign-flip
  null (sign-flip the FULL 5-column residual, add back the 4-column H₀-fit
  prediction, refit) replaces exp-072's phase-randomized H₀-residual null.
  `E[R_q^surr]=0` exactly (an algebraic identity, independently re-derived
  by EM this cycle) — but Red Team's own from-scratch Monte Carlo
  (independently reproduced again in this file's own dev run) shows the
  construction is **anti-conservative by 2–6× nominal**, a leverage effect.
  `G0-e(ii)` is therefore kept as a **binding, non-relaxable HALT**
  (docket item 3) rather than adopting either of two candidate patches —
  and it fires: this cycle's dev run HALTs at `G0-e(ii)` before any real
  pair is scored (see `phase3_synthesis.md` §4).
- **`G0-e` is sharpened on two axes**, both mandatory before any real data
  is touched: (i) widened synthetic recovery coverage, now with genuinely
  independent amplitude (`δa`) and phase (`Δψ`) axes so the `A_i` tripwire
  is live, not dead code (docket items 1–2); (ii) a brand-new null
  **calibration** check (`G0-e(ii)`) that tests whether T2-3's own null is
  correctly sized under pure H₀ noise, at every (σ, ψ, α) cell, plus a
  residual-structure robustness leg using real per-config residuals instead
  of i.i.d. Gaussian (docket items 3–4).
- **T2-1 (sign-invariance) is reinstated with a self-contained
  admissibility gate and a non-emptiness floor** (docket items 7–8): a
  carrier only counts toward the sign-invariance test if it independently
  clears its own admissibility check; if both non-`T_mean` candidates are
  excluded, the pair is explicitly `NOT_EVALUABLE` for this clause, never
  vacuously passed.
- **`A_q`'s exact identity (`= 2a_cbar·tan χ0`, not `sin`) requires no code
  change** — it is a re-labelling of the same OLS-fitted coefficient — but
  the "binds hard" a-priori claim is corrected to state, with exp-072's own
  real (class-b, non-gating) numbers, that the correction is expected to
  stay numerically inert on this substrate (docket item 5).
- **The power table and P-073-4's rate reference are re-anchored** to
  exp-072's own `n_grid=3000`-resolved slope, loaded at runtime, never
  hand-typed — the third recurrence of the same defect class now closed
  (docket item 6).
- **A structural contamination question, distinct from and broader than
  exp-072's own Phase-2 episode, is disclosed and forward-locked** (docket
  items 9–11): because this cycle's machinery is bit-identical to exp-072's
  own on unchanged data, every real point estimate this cycle produces was
  already computable from exp-072's own published `results.json` before
  Phase 1 was proposed. Ruled not outcome-determining (no threshold was set
  with reference to those numbers), but the disclosure and forward lock are
  binding, and a CONFIRM-shaped outcome must carry them into
  `phase4_results.md` — wired automatically into `results.json`'s own
  `contamination` block so this cannot be omitted later.

## Idealizations

1. **600nm only.** No wavelength-general claim licensed.
2. **The `ABSORB`/`PAD` compound-axis confound is NOT relieved.** `PAD =
   ABSORB − 40` holds exactly at all four configs (Iteration 48, closed).
   Any CONFIRM-shaped language must read "`ABSORB`-or-`PAD`-tied," never
   cleanly "`ABSORB`-tied" — binding under every verdict, not only CONFIRM.
3. **`ABSORB` is not a material.** A numerical boundary-condition parameter
   (a graded damping mask). No realizability claim is licensed by any
   result here — MATERIALS' own charter note, restated as the lead seat
   this cycle: a dependence on it is at least as likely to be a boundary
   artifact as a physical effect.
4. **Single-carrier-plus-ramp model, on a window shown to contain ≥2
   contributors.** T21's 1.9608° fringe coexists with the ~2.5° family; per-
   config/per-pair carrier fits reach only moderate R². `G0-e(ii)`'s own
   calibration validates the null construction's *size*, not the
   correctness of this functional-form assumption against a genuinely
   multi-component signal — a limitation shared with, and not closed
   relative to, exp-072.
5. **~2.4 carrier cycles in the window.** Not asymptotic; edge effects on
   the ramp coefficient are real — `dR_q/dψ̄ ≡ R_i` exactly (an algebraic
   identity, independently re-verified this cycle against exp-072's own
   real, published `(T_x, ψ, R_i)` values to 10 decimals — see
   `phase3_synthesis.md` §3, Ambiguity 4, for the sign-convention subtlety
   this required getting right), and `|R_i| ≥ |R_q|` at three of four pairs
   in exp-072's own already-closed record.
6. **`n_grid=3000` adds no resolving power** — it only removes the
   `n_grid=400` node-collision quantization that reversed C70/C80's free-
   period order. The linear-fit `m0_resolved` used as this cycle's
   operative rate reference (docket item 6) is the least-squares slope at
   this resolution, not the endpoint chord; the underlying node-collision
   fact is disclosed, not resolved by re-anchoring to it.
7. **2D TMz, single polarization, positive-θ branch only (36°–42°)** — not
   a symmetry test; single-angle `C_empty` readings, not an N9/N17
   aggregate (T25/T26 do not apply); bench scale only (`R_OUT=78` cells) —
   no witness-scale claim.
8. **No new FDTD, no new engine-physics identity gate.** Trust in the
   underlying numbers is inherited from exp-069's and exp-071's own
   already-passed G1 identity gates, settling checks, and peak-cell R3
   resolution checks. This cycle adds only arithmetic-integrity gates
   (G0-a/b/c) and the sharpened ground-truth/null-calibration gates
   (G0-d/e(i)/e(ii)); it inherits, does not re-establish, engine trust.
9. **Statistical power is estimated a-priori from a corrected `m0` read at
   runtime.** If the true effect differs from that estimate, the
   under/over-powered set may differ from the two pairs named in
   `phase1_proposal.md` §2c. The pre-registered fallback (report sign and
   `p`, quote no period for unresolved pairs) covers both directions.
10. **`G0-e`'s own synthetic sweeps use deliberately generic carrier
    periods, amplitudes, phase offsets, and noise levels — bracketing, not
    reproducing, the real fitted values** — so that passing `G0-e` is
    evidence about the pipeline alone, never about this cycle's own real
    data, exactly what R6 requires. (The one place a synthetic parameter
    was chosen relative to a real closed value — G0-e(i)'s `T_A` bracket
    around the published 2.4361°–2.5338° per-config range — deliberately
    avoids the four real values directly, per the proposal's own text.)
11. **`C_empty` is a dimensionless field ratio, not a Michelson/Weber
    contrast**; any `ptp/mean`-style statistic beside a `ΔP` is a
    fit-conditioning statistic, not a perceptual or photometric quantity.
12. **Window provenance and cross-cycle multiplicity.** The 31-point
    36.0°–42.0° grid is inherited from Block MINI (exp-069); statistics on
    these identical 124 points now span five cycles (exp-069/070/071/
    072/073). Holm corrects within this cycle's own three free pairs;
    nothing corrects across cycles. Disclosed, not fixed, by this design.
13. **No absorbed-power number is produced; THERMODYNAMICS' energy sidecar
    is N/A this cycle, by argument, not by omission** (house precedent,
    **Iteration 2** — corrected citation, docket item 12; THERMODYNAMICS'
    own Phase-2 critique independently traced the actual origin of this
    norm in LOGBOOK.md and found the prior "Iteration 5" citation was a
    provenance slip, not the norm's own source).

## Pre-registration contamination (binding; full ruling `phase2_redteam_audit.md` §3, restated `phase3_synthesis.md` §6)

This cycle's carrier-fit and ramped-OLS machinery is bit-identical to
exp-072's own already-published `run.py`, on the identical 124-point
substrate — meaning every real per-pair point estimate this cycle's Phase 4
produces was already computable, bit-exact, from exp-072's own
`results.json` before this cycle's Phase 1 was even proposed, and was in
fact independently computed for the `A_q`/`χ0` channel by this cycle's own
EM critique. Ruled **not outcome-determining** for the Combined Verdict as
specified: none of the three new-machinery items (T2-1, T2-3, T2-4) were
tuned in response to these numbers; every threshold traces to a data-free
argument. **Forward lock**: any gate/band/threshold change made from the
Phase-2 audit forward, for any reason traceable to exp-072's known real
numbers, must be treated as a fresh Phase-1/2 decision, never a same-cycle
Phase-3 correction — no such change was made anywhere in this file. **If
Phase 4 reaches a CONFIRM-shaped outcome on any pair**, this disclosure and
the forward-lock statement must travel into `phase4_results.md` — wired
automatically via `results.json`'s `scored.contamination` block
(`confirm_disclosure_required`/`confirm_disclosure_text`), computed from
the Combined Verdict so it cannot be omitted later.

## FROZEN PREDICTIONS (committed here, before Phase 4's official run of `run.py`)

Full gate/threshold specification: `phase2_redteam_audit.md` §5 (12 items)
plus `phase1_proposal.md` §7 (the full pre-registered structure, corrected
per the docket) — the single source of truth, to avoid a second
transcription surface (the R4 lesson, applied to this exact `m0` figure a
third time at docket item 6).

**Identity/integrity gates, evaluated first, in order — any HALT stops the
cycle, nothing is scored:**

| Gate | PASS bar | On FAIL |
|---|---|---|
| G0-a (grid identity) | θ arrays from all three source files bit-identical | `HALT_GRID_MISMATCH` |
| G0-b (telescoping identity) | `delta_40_60+delta_60_70+delta_70_80−delta_40_80=0`, max abs residual ≤1e-12 | `HALT_TELESCOPE_MISMATCH` |
| G0-c (column provenance) | exp-069's committed `delta` column ≡ `C_empty_C80−C_empty_C40`, max abs Δ ≤1e-12 | `HALT_PROVENANCE_MISMATCH` |
| G0-d (conditioning) | `cond(X5)≤100` per pair | that pair `ILL_CONDITIONED`, excluded downstream (per-pair, not global — see `phase3_synthesis.md` §5) |
| G0-e(i) (recovery accuracy) | worst-cell `\|ΔP_est/ΔP_true−1\|≤0.02` over the widened synthetic sweep (5,760 cells), plus both tripwires clean | `HALT_RECOVERY_FAILED` |
| G0-e(ii) (null calibration) | empirical rejection rate inside `α±3√(α(1−α)/K)` at every cell, **both legs** (i.i.d. and residual-structure) | `HALT_NULL_MISCALIBRATED` |

**Scored predictions (only reached if all gates PASS):**

- **P-073-1** — full descriptive per-pair table (`T_mean`, `a_cbar`, `ψ̄`,
  `A_i`, `A_q`, `R_i`, `R_q`, `SE(R_q)`, `‖R‖`, `Δf`, `ΔP`, `SE(ΔP)`,
  `dR_q/dψ̄`, `|R_i/R_q|`, sign-flip and disclosed permutation-null `p`,
  `ρ_c`, the full carrier-admissibility table) — published for all four
  pairs regardless of every other outcome.
- **P-073-2** — per-pair `RESOLVED` (6 conjunctive clauses: not
  ill-conditioned; sign-flip-null Holm-adjusted `p≤0.01`; linearization
  `|Δf|·X≤0.25`; carrier-consistency `≤q95`; wrong-carrier gate; T2-1
  sign-invariance with non-emptiness floor). **CONFIRM** ⟺ C40–C80 AND
  C40–C60 resolved AND at least one of {C60–C70, C70–C80} resolved.
  **REFUTE** ⟺ zero pairs reach relaxed `p≤0.10` AND injection-recovery
  demonstrates power at all three adjacent pairs (else
  `UNDERPOWERED_NOT_EVALUABLE`, never REFUTE). **NEITHER** ⟺ anything else.
- **P-073-3** — `ρ_c` carrier-sensitivity closure, computed at each pair's
  own independently-fit `T_mean` (the common-carrier `≡0` identity is a
  disclosed sanity check only, never scored). CONFIRM ⟺ `ρ_c≤0.05` and
  sign(S)=sign(D). REFUTE ⟺ `ρ_c≥1.00` or a genuine sign mismatch with
  both `|S|,|D|≥0.010°`. NOT_EVALUABLE ⟺ any of the three adjacent pairs
  unresolved.
- **P-073-4** — `ABSORB`-depth-trend consistency over resolved pairs only
  (≥2 required). REFUTE ⟺ any resolved pair has `ΔP<0` with `|ΔP|≥0.010°`
  — the only gating rate clause. CONFIRM requires, additionally
  (disclosed, non-gating band), every resolved pair's rate inside
  `[m0_resolved/3, 3·m0_resolved]`.
- **P-073-5/6** — carrier-admissibility and different-null disclosure;
  amplitude/phase/frequency decomposition. Both non-gating, mandatory
  alongside any CONFIRM.

**Combined Verdict**, computed in this order: HALT (named branch) →
REFUTED ⟺ P-073-2 REFUTE or P-073-3 REFUTE → CONFIRMED ⟺ P-073-2 CONFIRM
and P-073-3 CONFIRM and P-073-4 CONFIRM → NEITHER ⟺ everything else.

## Result

*(Placeholder — Phase 4's official run has not been executed as part of
this deliverable. Per the task's own scoping instruction, `results.json`
and `phase4_results.md` are Phase 4's job, to be produced in the next step,
run once, officially, after these predictions are frozen and committed. A
development-only run of `run.py` against the real data, with these exact,
unmodified thresholds, HALTed at `G0-e(ii)` as `HALT_NULL_MISCALIBRATED` —
see `phase3_synthesis.md` §4 for full disclosure of what was run and why
that output is not treated as this cycle's result.)*

## Learned

*(Placeholder — see `phase4_results.md` Bottom Line and this experiment's
contribution to LOGBOOK.md Iteration 50, once Phase 4/5 are run.)*

## Next

*(Placeholder — see PLAN.md's Iteration-51 queue, Director's update, post
Phase 5.)*
