# Phase 2 Critique — THERMODYNAMICS (blind, fresh context)

*(A harness-level safety-review notice fired on this sub-agent's transcript upstream, unrelated to the content below — reviewed directly by the Director; no prompt injection or suspicious instruction found in the critique text itself.)*

## Steel-man (≤150 words)

This is a clean instrument-fidelity re-score, not a new physical construction, so it's thermally inert by design. Article params are stated bit-identical to exp-065's Block ARTICLE (τ_center=0.0065, σ_e=4.1667e-5, R_OUT=78 — verified in `experiments/065-t24-absorb-boundary-sweep/design_geometry.py`); STEPS=1400→2800 only corrects an FDTD *transient* in the ambient-contrast C reading, an optical/scattering quantity. Absorbed power is a separate analytic function of τ, r_out, and incident flux — none of which move here — so nothing this proposal does can touch the T5/exp-043 UNDETECTABLE disposition (>100× below sourced NETD) already established for this exact off_pass-class article. No new energy channel opens, no THERMO sidecar re-run is owed, and "T1 route N/A" is thermally sound on its own narrow terms.

## Sharpest attack (≤150 words)

The proposal's own reuse list for exp-065's `design_geometry.py` — "CONFIGS, FALLBACK_ANGLES, TAU_OFF_PASS, SIGMA_OFF_PASS, GATE_HARD, C_THR_LAB, MARGINAL_LO/HI" — silently omits `T5_THERMAL_CAVEAT`, the constant my own seat forced into that exact file at Iteration 42 ("Red Team attack 6 / THERMODYNAMICS' catch") specifically so Block ARTICLE's τ=0.0065 disk could never be re-scored without its established UNDETECTABLE thermal disposition attached. No `caveat_lint_config.json` entry mechanically guards this propagation (zero hits for T5/thermal in the registry), so nothing stops exp-068's own NOTES.md/phase4_results.md from republishing the corrected PASS/MARGINAL C values with the caveat dropped — the exact propagation-gap species that fired Checkpoint criterion 4 at Iterations 38-40.

## Verdict: support-with-changes

## Flip

Add one line to the parameter table committing to carry `T5_THERMAL_CAVEAT` (and sibling `REALIZABILITY_MEMO_CAVEAT`/`G_TRANSFER_T15_CAVEAT`) verbatim into every new site where Block ARTICLE's C value or PASS/MARGINAL bucket is stated — zero FDTD cost.

## Files checked

`experiments/065-t24-absorb-boundary-sweep/design_geometry.py` (lines 170-189, 601), `NOTES.md` (lines 143-155), `phase2_critique_thermodynamics.md`, `phase3_synthesis.md` (line 55); `experiments/066-t27-block-main-settling-reverification/design_geometry.py` (no T5 constant — correctly N/A, empty-only legs); `experiments/067-r-contact-bonded-substrate-correction/phase5_redteam_audit.md`, `NOTES.md` (confirms R_contact and Block ARTICLE are physically disjoint systems); `lab/caveat_lint_config.json` (grep for T5/thermal/exp065- returns only the unrelated settling entry, no thermal-disposition guard); LOGBOOK.md (exp-032 origin of the off_pass article; Iterations 42-44 full record).
