# exp-054 — The `h_eff` Length-Scale Re-derivation

Panel Iteration 31 (LOCKED, UNCONDITIONAL — fifth-deferral trigger, named at
Iterations 25/26/27/28/29 closes without being reached). Lead:
**THERMODYNAMICS**. Runner: cloud panel shift, 2026-08-21. Full Phase 1/2
record: `phase1_proposal.md`, `phase2_critique_*.md`, `phase2_redteam_audit.md`,
`phase3_synthesis.md` — read those for the debate; this file states the
corrected, frozen hypothesis/setup/predictions Phase 4 actually runs.

## Hypothesis

`lab/thermo_sidecar.py`'s thermal-detectability chain has, since Iteration
22, carried an unresolved ambiguity: which characteristic length is
physically licensed for `h_eff = k_air/L` (quiescent gas-phase conduction)?
This cycle argues, formally and for the first time, that `h_eff`, thermal
mass, and radiating/convecting area must ALL derive from `r_out` (the
object's real geometric radius) — never from `w_on` (the ON-endpoint's
measured, diffraction-inflated extinction-cross-section width) — while
absorbed power `P_abs` stays on `w_on` (a separate, already-calibrated
optical measurement). The corrected chain is MIXED by design, not uniform.
Applied to exp-043's ON-endpoint (τ=3.9) and exp-045's dose-accumulation
article (Host D, kinetics-driven), replacing Iteration 25's informal,
never-run estimate with real, code-computed numbers.

## Setup

- **Zero new FDTD calls** — pure desk/analytic re-derivation from
  already-committed bench measurements (Iteration 20/22/25/27 sidecar-cycle
  precedent).
- New reusable functions in `lab/thermo_sidecar.py`: `gas_conduction_h_eff`,
  `lumped_cube_mass_kg`, `mixed_length_scale_regime` — see
  `phase3_synthesis.md` for the exact signatures and the Director's one
  structural decision (folding Red Team's attacks 4a/4b into one new trust-
  suite stage).
- New trust-suite stage 18: three identity gates (h_eff·L==k_air any L;
  mass/L³==density any L; the ON-endpoint call site's literal `r_out_m`
  value reproduces the already-published 3.293076×10⁻⁵ K figure — the one
  gate that actually discriminates a correct length choice from a wrong
  one at this call site).
- `experiments/054-.../run.py` computes the mixed regime for the ON-endpoint
  and re-runs exp-045's own Block C 8-point grid (Host D, 4 ratios ×
  {5τ,0.5τ}) through `coupled_segment_general` — imported via
  `importlib.util` from `experiments/045-.../run.py` under a private module
  name (exp-050's own precedent) — at the MIXED chain's own
  `dt_ss_full`/`tau_thermal_s`, not the `w_on`-consistent pair Block C
  originally used. Both the decoupled proxy and the exact coupled-ODE
  trajectory are computed; `exact <= decoupled` is checked directly, not
  assumed (Phase-2 mandatory fix 2).

## Idealizations (unchanged from `phase1_proposal.md`, plus one addition)

- Nu=2 quiescent-gas conduction limit (still air, no forced convection).
- Lumped-capacitance, cube-shaped thermal mass — NOT the module's own true-
  disk convention; exp-046's own sensitivity check found the operative
  conclusion survives a true-disk recheck (97×), not re-verified here.
- Steady-state graybody radiative linearization about `T_ambient`.
- Bench-scale, not witness-scale — **T8/T13's near-field→witness-scale
  bridge `h_eff` question is explicitly NOT addressed by this cycle** (see
  P-054-6; this is the corrected scope statement, mandatory fix 1).
- Static ON-state ratio for the ON-endpoint; unaffected by this cycle's
  length-scale correction.
- Slip-flow correction disclosed as a sensitivity bound (~-5.3% at r_out),
  not folded into the headline.
- Achromatic by construction (ε_r≡1), no per-λ re-examination.
- `P_abs` itself is measurement-locked, not re-derived — only the
  downstream `h_eff`/mass/area chain is corrected.
- **NEW (mandatory fix 5, QUANTUM):** the Block-C `n(t)`-independence claim
  (P-054-3) holds only while `k_f`/`k_r` remain exogenous rate-constant grid
  parameters — `lab/kinetics.py::integrate_two_state` explicitly refuses a
  time-varying `I_profile` (`NotImplementedError`); if a future cycle
  re-derives `k_f` from `I(t)` self-consistently, this independence must be
  re-argued, not assumed to carry over.
- **NEW (mandatory fix 3, MATERIALS):** the silicon thermal identity
  (ρ=2330 kg/m³, C_p=700 J/(kg·K), κ=148 W/(m·K)) is
  **ASSUMED — provenance terminates unsourced (T18)**, per
  `REALIZABILITY_MEMO.md`'s own standing downgrade — not independently
  re-sourced this cycle. `mass_kg=ρ·r_out³` further assumes 100%-fill
  crystalline silicon, undisclosed in the Phase-1 draft, disclosed here.

**NETD disclaimer (propagated verbatim per mandatory fix 6, at every
prediction below that quotes a detectability classification): NETD is an
instrument/detector threshold, not a human perceptual one — no prediction
below bears on constraint-3/4's human-eye verdict.**

## Predictions — committed to git BEFORE any Phase-4 run (house discipline, non-negotiable)

Supersedes `phase1_proposal.md`'s own P-054-1 through P-054-7 per
`phase3_synthesis.md`'s disposition of all 7 Red Team mandatory-fix items.

| ID | Prediction | Band | Basis |
|---|---|---|---|
| P-054-1 | Corrected `dt_ss_full` for the ON-endpoint (τ=3.9), mixed chain, via the NEW `mixed_length_scale_regime` code (not hand arithmetic) | [2.8e-5, 3.6e-5] K | Regression anchor: must reproduce the already-published 3.293076×10⁻⁵ K side-computation (LOGBOOK Iteration 23) |
| P-054-2 | Corrected NETD-lo margin for the ON-endpoint. **NETD is an instrument threshold, not a human-eye one — not a constraint-3/4 finding.** | **500×–750×** (central ≈607×) | 0.020K / P-054-1's band |
| P-054-3a | Block C: `exact ≤ decoupled` (decoupled proxy stays conservative) holds at ALL 8 re-run points, at the mixed chain's own `dt_ss_full`/`tau_thermal_s` (τ_thermal=3.433×10⁻⁴s, 9.15× shorter than the originally-tested `w_on`-consistent regime) | exact/decoupled ratio ∈ **[0.98, 1.000]** at every point (closer to 1 than the original 0.966–0.987 range) | Physical argument: dwell/τ_thermal is ≈194.2× at the mixed chain vs ≈21.2× at `w_on`-consistent — the thermal system settles far more completely within each ON dwell, so the instantaneous-response (decoupled) approximation should track the exact coupled ODE MORE closely, not less, not merely stay conservative by the old margin |
| P-054-3b | Block C: worst-case `dT_periodic_decoupled` (max across the 8-point grid), mixed chain | [1.9e-6, 2.6e-6] K | Linear-scaling argument: correction factor 3.293076e-5/1.0875240683859519e-05 ≈3.0284× applied to the original headline 7.385465974827066e-7 K |
| P-054-4 | Corrected NETD-lo margin for the dose-accumulation article, using the EXACT coupled-ODE worst-case periodic ΔT (not the decoupled proxy) as the reported headline. **NETD is an instrument threshold, not a human-eye one.** | **7,000×–11,000×**, reported as a margin ≥ this band (since exact ≤ decoupled per P-054-3a, the true margin can only be equal to or larger than the decoupled-based figure) | 0.020K / P-054-3b's band, adjusted per P-054-3a |
| P-054-5 | Classification for both articles. **NETD is an instrument threshold, not a human-eye one — UNDETECTABLE here is not a constraint-3/4 finding.** | Both **UNDETECTABLE**, not MARGINAL or DETECTABLE | No candidate chain computed anywhere in exp-043/045/046/054's own record has ever produced a margin below 5× |
| P-054-6 | Scope boundary: this cycle's bench-scale correction vs. Iteration 25's separate, informal witness-scale (T8/T13/T14) estimate | **This cycle does NOT test, confirm, or refute Iteration 25's witness-scale estimate** — the two are different physical questions (bench geometric length-scale choice vs. near-field→witness-scale bridging); T8/T13's own witness-scale `h_eff` question stays open and unaddressed | Red Team's Phase-2 attack 1 (mandatory fix 1) — corrects the Phase-1 draft's own conflation |
| P-054-7 | New trust-suite stage 18 | 3 new identity checks (2 tautological-but-retained formula-consistency gates + 1 discriminating literal-length-pinned regression anchor), full bench green, 0 new FDTD calls | Iteration-20/22/25/27 sidecar-stage precedent; Red Team mandatory fix 4 |
| P-054-8 | Documentation completeness: ASSUMED-provenance label + 100%-fill disclosure present in this cycle's own parameter table and `results.json`; NETD disclaimer present at every prediction above; forward-pointer note appended to exp-043 and exp-045's own `NOTES.md` | All three present, verifiable by direct grep | Mandatory fixes 3, 6, 7 |

**Falsification condition, stated plainly**: if P-054-2 or P-054-4 land
outside their stated bands (particularly toward Iteration 25's old
~2.6×/~38–42× guess, or below 5×), or if P-054-3a's ratio comes back **above
1.0 at any point** (decoupled stops being conservative at the shorter
τ_thermal — the exact scenario EM's Phase-2 attack flagged as untested),
that is a real, reportable surprise, not a rounding difference.
