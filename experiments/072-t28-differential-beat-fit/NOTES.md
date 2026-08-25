# exp-072 — T28's differential/beat fit of `delta_AB(θ)` between adjacent `ABSORB` configs

**Panel Iteration 49.** Lead: PHOTONICS (by rotation). Director synthesis
post Phase 2 (five blind critiques + Red Team's Phase-2 audit, verdict
PROCEED-WITH-MANDATORY-FIXES, 15-item docket, **3 items' specific remedies
overridden and replaced with Red-Team-derived corrections, all other
requests accepted in full** — full record in `phase1_proposal.md`,
`phase2_critique_{photonics wrote it so no self-critique;
materials,em,thermodynamics,quantum,vision}.md`, `phase2_redteam_audit.md`,
`phase3_synthesis.md`).

## Mandate

PLAN.md's Iteration-49 queue, item 1: merge ELECTROMAGNETISM's and QUANTUM
OPTICS' Phase-5 differential/beat-fit proposals from exp-071 into one
zero-FDTD-cost item on live thread **T28** — the real, unexplained ~2.84°
periodicity in a congruent 4-config `ABSORB`-depth series (C40/C60/C70/C80,
600nm, θ∈[36°,42°]) whose per-config free periods rise smoothly with
`ABSORB` depth (Iteration 48, exp-071) but whose Combined Verdict came back
NEITHER — `spread_40_80` missed the 30% CONFIRM floor and `R²=0.8664` missed
the `≤0.30` REFUTE ceiling, both independently, before QUANTUM's own
established finding that the window is fundamentally Rayleigh-underpowered
to resolve C60 vs C70's absolute periods (0.59% apart, window supplies
<10% of needed resolution).

## Setup

Reads ONLY already-committed data — **zero new FDTD calls, zero `lab/`
diff**:

- `experiments/069-.../results.json` → `block_dense.rows` (C40, C80, 31
  points, θ=36–42°).
- `experiments/071-.../results.json` → `dense_causal.rows.C60/.C70` (same
  θ grid), `trend.linear_fit.slope` (the committed `m₀`, loaded
  programmatically — never hand-typed, per MATERIALS' Attack-5 finding that
  the Phase-1 proposal's own cited `m₀` was a mis-provenanced two-point
  chord slope, not the committed least-squares fit).
- `experiments/069-.../run.py` → `_fixed_period_fit`, reused verbatim.

The instrument: fit `delta_AB(θ) = C_B(θ) − C_A(θ)` for the three adjacent
`ABSORB` pairs (C40–C60, C60–C70, C70–C80) plus the already-analyzed
C40–C80, as a **ramp in quadrature with a common-mode carrier**
(`Cbar = (C_A+C_B)/2`, free-period-fit at `n_grid=3000`) rather than
independently fitting each config's absolute period and subtracting — this
converts an unresolvable absolute-frequency Rayleigh problem into a
coefficient-detection problem at the (well-resolved) common-mode carrier.
Full derivation: `phase1_proposal.md` §1–2.

## The fixed design (Red Team's 15-item docket, `phase2_redteam_audit.md` Sec 6)

Implemented verbatim in `run.py`; summary of what changed from the raw
Phase-1 proposal (full detail in `phase3_synthesis.md`):

- **Two nulls, both reported, the stricter one gates.** The unrestricted
  Fourier-phase null (proposal as written) and QUANTUM's H₀-restricted null
  (phase-randomize only the null-model residual) are both run; `RESOLVED`
  gates on the restricted null's Holm-adjusted p ≤ 0.01, but REFUTE requires
  BOTH nulls to show zero significant pairs AND a pre-registered
  injection-recovery power test to pass — closing the "REFUTE fires on pure
  power failure" defect (Red Team Attack 2).
- **`A_q` relabeled** `2a·sinχ` ("half the phase difference at window
  centre"), never converted to the extrapolated `Δψ` (Red Team Attack 3
  independently demonstrated EM's original proposed fix manufactures a
  175°-class artifact).
- **Carrier-consistency gate recalibrated** from a per-pair surrogate
  percentile (`q95`) instead of the imported, wrongly-scaled `0.414`
  Rayleigh figure (Red Team Attack 4).
- **`m₀` loaded from committed JSON at runtime**; P-072-4's rate-window is
  demoted to disclosed-only (a graded absorber's boundary return is a-priori
  expected to saturate, not stay linear, in `ABSORB` depth — MATERIALS'
  and THERMODYNAMICS' independently-converging finding, Red Team Attacks
  5–6); only the sign-reversal clause gates.
- **P-072-3 (closure) demoted** from a `CONFIRMED` conjunct to a disclosed
  basis-stability check (`ρ_c ≤ 0.05`) — three seats (EM, QUANTUM, VISION)
  independently showed the original framing was close to an arithmetic
  tautology (Red Team Attack 7).
- **Wrong-carrier control promoted to a gate**, at a carrier displaced ≥1.5
  Rayleigh widths from the true one (3.60°) rather than T21's 1.9608° (only
  0.65 Rayleigh widths away, provably non-diagnostic — Red Team Attack 9);
  the 1.9608° run stays as disclosure only, explicitly labeled a resolution
  identity, not a control.
- **`ΔP` reported at all four carriers** (`T_mean`, `T_delta`, 3.60°,
  1.9608°) for every pair, unconditionally — VISION's finding (sign is not
  invariant across carriers admitted by the original gate) is disclosed in
  full rather than gated on as originally proposed (Red Team Attack 10).
- **`R_i` model-strain flag**, a disclosed 6th curvature column, and
  bootstrap-propagated `SE(R_q)` all added (Red Team Attacks 8, items 7/11/15).
- **Holm–Bonferroni over the 3 algebraically-free adjacent pairs**, C40–C80
  reported unadjusted and explicitly labeled *derived* (Red Team Attack 12,
  `G0-b` proves it is the exact sum of the other three).

## Idealizations (unchanged from the Phase-1 proposal, `phase1_proposal.md` §6, still binding)

1. **600nm only** — no wavelength-general claim licensed.
2. **The `ABSORB`/`PAD` compound-axis confound is NOT relieved.** Any
   CONFIRM-shaped language from this cycle must read `ABSORB`-or-`PAD`-tied,
   never cleanly `ABSORB`-tied — and per Red Team's docket item 13, must
   additionally read "-or-frequency-or-fringe-weight-change", since `R_q` is
   shown non-identifiable against T21's own unresolved fringe contributor
   (QUANTUM's Attack 5a finding). This binds every deliverable — P-072-1 and
   the disclosed P-072-6 channels included — under EVERY verdict, not only
   CONFIRM (THERMODYNAMICS' finding, closing a gap in the original text).
3. **`ABSORB` is not a material.** A numerical boundary-condition
   parameter; no realizability claim is licensed by any result here.
4. **Window provenance, disclosed, not previously stated**: the 31-point
   36.0°–42.0° grid is inherited from Block MINI (exp-069); T28 was
   discovered inside it. All p-values in this cycle are conditional on this
   window and are not corrected for the roughly dozen statistics already
   computed on these same 31 points across exp-069/071/072 (VISION's
   finding).
5. `C_empty` is a dimensionless field ratio, not a Michelson/Weber
   perceptual contrast; `ptp/mean`-style figures are fit-conditioning
   statistics, never photometric ones (VISION's finding).
6. No new FDTD, no new identity gate against the engine — trust is
   inherited from exp-069's/exp-071's own already-passed gates; this cycle
   adds only arithmetic-integrity gates (G0-a/b/c/d).
7. 2D TMz, positive-θ branch only, bench scale (`R_OUT=78` cells), no
   witness-scale claim.
8. The energy sidecar is explicitly N/A this cycle — no absorbed-power
   number is produced anywhere in the design (THERMODYNAMICS' scoping,
   confirmed clean).

## Pre-registration contamination (binding, see `phase3_synthesis.md` for the full ruling)

Two Phase-2 seats computed real numbers from the committed data while
critiquing; Red Team independently verified which of two candidate null
constructions is outcome-determining (REFUTED vs. NEITHER) before Phase 3.
Per Red Team's ruling, **any CONFIRM-shaped result this cycle emits as
`CONFIRM_UNCERTIFIED`, never `CONFIRMED`** — a standing, cycle-scoped rule,
implemented as an unconditional override in `run.py`'s Combined-Verdict
logic. Full disclosure paragraph: `phase3_synthesis.md`.

## FROZEN PREDICTIONS (committed here, before this commit's official run of `run.py`)

Full gate/threshold specification: `phase2_redteam_audit.md` Sec 6 (15
items) — the single source of truth, to avoid a second transcription
surface. Combined Verdict is a fixed boolean function of: G0 gates (HALT on
failure) → P-072-2 (per-pair `RESOLVED`, CONFIRM/REFUTE/NEITHER/
UNDERPOWERED_NOT_EVALUABLE) → P-072-4 (sign-reversal REFUTE only, gating) →
CONFIRM requires BOTH P-072-2 and P-072-4 CONFIRM, downgraded unconditionally
to `CONFIRM_UNCERTIFIED` per the contamination ruling above.

**Red Team's own advance forecast (`phase2_redteam_audit.md` Sec 7),
inherited here unchanged**: no pair reaches `RESOLVED`; Combined Verdict
`NEITHER`; the substantive finding is that `R_q` is bounded not by the
noise floor originally anticipated but by non-identifiability against the
window's own unresolved second contributor and against its own carrier — a
limit the absolute-period route (exp-071) never got close enough to
encounter. This is recorded as a forecast the Combined-Verdict code does
not reference, not a target.

## Idealizations affecting this NOTES.md itself

This file was written by the Director with full knowledge of the numbers
Red Team's audit already disclosed (Sec 0's verification ledger, Sec 1's
attacks) — a further layer of the same contamination the disclosure above
already covers. No threshold here differs from `phase2_redteam_audit.md`
Sec 6 in any respect; this file restates, it does not decide.

## Result

See `phase4_results.md` for the official run's numbers and
`phase5_redteam_audit.md`/`phase5_review_*.md` for Phase 5.

## Learned

See `phase4_results.md` Bottom Line and this experiment's contribution to
LOGBOOK.md Iteration 49.

## Next

See PLAN.md's Iteration-50 queue (Director's update, post Phase 5).
