# exp-054 Phase 5 Review — ELECTROMAGNETISM (blind, independent)

Panel Iteration 31, fresh-context review. Scope: field/wave energy
bookkeeping, reciprocity/passivity/causality — not a restatement of my own
Phase-2 critique, which this review instead goes and checks was actually
resolved rather than merely asserted resolved.

## What this cycle establishes, from this discipline's lens

The mixed-length-scale chain (`P_abs` on `w_on`, `h_eff`/`mass`/`area` on
`r_out`) is dimensionally and energetically coherent, as I found at Phase 2:
`P_abs` is an absolute wattage, `dp_dt` (`lab/thermo_sidecar.py:246`) is an
absolute thermal admittance in W/K built entirely from `r_out`, and
`ΔT = P_abs/dp_dt` needs no shared-area normalization step where mismatched
lengths could silently cancel wrong. Both `steady_state_delta_T` and
`mixed_length_scale_regime` guard `dp_dt <= 0` with a `ValueError`
(`lab/thermo_sidecar.py:162-163`, `:247-248`) — a real passivity check
(heat-loss admittance cannot be non-positive) rather than a claim taken on
faith. This is not the same failure Red Team killed at Iteration 22: that
bug split `h_eff` and `mass` across two different lengths *within one
solid-body subsystem*; this cycle separates a far-field diffractive optical
quantity from a local geometric one and keeps each internally uniform. The
formula-reduction claim (`coupled_segment_general` reduces exactly to
`coupled_kinetics_thermal_dT` at n0=dT0=0) also checks out **symbolically**,
not just numerically — I expanded both closed forms by hand and they are
algebraically identical term-for-term. So the core physics argument is
sound, and this is causal, passive bookkeeping throughout: no term here
depends on a future drive value, and no admittance is allowed to go
negative.

**I independently re-verified the load-bearing claim my own Phase-2 attack
forced onto this cycle's docket (mandatory fix 2), reading the raw
per-point data, not the summary fields.** Extracting all 8
`block_c_points` entries from `results.json::part_b_block_c_rerun`
directly:

| point | ratio (first pulse) | ratio (periodic) | conservative? |
|---|---|---|---|
| r=1e-9, 5τ | 0.996365 | 0.996389 | yes/yes |
| r=1e-9, 0.5τ | 0.996365 | 0.998565 | yes/yes |
| r=1e-5, 5τ | 0.996365 | 0.996389 | yes/yes |
| r=1e-5, 0.5τ | 0.996365 | 0.998565 | yes/yes |
| r=1e-3, 5τ | 0.996366 | 0.996391 | yes/yes |
| r=1e-3, 0.5τ | 0.996366 | 0.998567 | yes/yes |
| r=1e-1, 5τ | 0.996496 | 0.996534 | yes/yes |
| r=1e-1, 0.5τ | 0.996496 | 0.998716 | yes/yes |

All 16 ratios (8 points × 2 readings) satisfy `exact ≤ decoupled`, span
[0.996365, 0.998716], and sit inside the pre-registered `[0.98, 1.000]`
band with the correct sign — none crosses 1.0, which is what P-054-3a's own
falsification condition named as "a real, reportable surprise." The claim
`worst_exact_vs_decoupled_ratio=0.9987`/`all_decoupled_conservative=true`
in `results.json` is not a mischaracterized summary — it genuinely reflects
the per-point data. This also confirms P-054-3a's own physical argument
(dwell/τ_thermal ≈194.2× at the mixed chain vs. ≈21.2× at `w_on`-consistent
→ the system re-settles more completely between pulses → the decoupled
approximation should track tighter, not looser): the new ratios (0.9964–
0.9987) are indeed uniformly closer to 1.0 than the original `w_on`-
consistent range (0.966–0.987), in the direction the physical argument
predicted, at every one of the 8 points, not just on average. My own
Phase-2 attack is resolved, not merely closed on paper. I also independently
recomputed Part A (`dt_ss_full_K=3.293076054169135e-05`,
`tau_thermal_s=3.4332969490950116e-4`) and Part B's aggregate figures
(`max_dT_periodic_decoupled_K=2.236e-6`, `netd_lo_margin_exact=8954.6×`)
from the committed inputs and helper functions directly, bypassing
`results.json` entirely — all match to the last printed digit, and P-054-1
through P-054-5 all pass their pre-registered bands as claimed.

## Load-bearing defect found

**The self-check assertion (`run.py:165-171`) is not independent
validation, and the machinery it is supposed to protect has no permanent
regression gate anywhere in this codebase.**

1. `coupled_segment_general`'s general two-argument reduction to
   `coupled_kinetics_thermal_dT` at `n0=dT0=0` is an **algebraic identity**,
   not an empirical property of this run's specific inputs. Expanding
   `coupled_segment_general`'s `dT_final` formula
   (`experiments/045-.../run.py:168-171`) at `n0=0` and collecting the
   `exp(-dt/tau_th)` terms reproduces
   `coupled_kinetics_thermal_dT`'s bracket
   (`experiments/045-.../run.py:140-142`) term-for-term, for *any*
   `k_f, k_r, dt_ss_full, tau_thermal_s`. That means the assertion at
   `run.py:170-171` is mathematically guaranteed to pass regardless of
   whether `coupled_segment_general` is correctly implemented for the
   **nonzero**-`n0`/`dT0` case — which is exactly the case Block C actually
   exercises at every one of the 10 non-first segments per grid point
   (`_n_walk`, `_dT_walk` carried forward across the loop at
   `run.py:150-158`). A bug that broke only the nonzero-IC branch while
   leaving the `n0=0` branch intact would sail through this check
   unnoticed. I confirmed this is not merely a hypothetical concern: the
   assertion is retested 8 times (once per grid point, all with `n0=0`)
   and — as expected from the algebra — passes with `diff` machine-zero at
   every point (independently reproduced this run in a scratch script).

2. **`lab/validation/run_all.py`'s new stage 18 (lines 1563-1611) never
   touches `coupled_segment_general` at all.** Its three gates cover only
   `gas_conduction_h_eff`, `lumped_cube_mass_kg`, and
   `mixed_length_scale_regime` (the ON-endpoint regression anchor). Block
   C's entire exact-vs-decoupled comparison — the specific property my own
   Phase-2 attack demanded be checked — runs on machinery (`coupled_segment_
   general`, imported from `experiments/045-.../run.py`) that sits **outside
   the trust suite entirely**. Its only prior validation against an
   independent numerical method is exp-044's original
   `scipy.integrate.odeint` cross-check (cited at `experiments/045-.../
   run.py:129-133`) — of the *different*, `n0=0`-only closed form
   (`coupled_kinetics_thermal_dT`), not of the general segment-chaining
   function Block C actually calls 11 times per grid point. Nowhere in the
   committed record (`experiments/045`, `experiments/046`,
   `experiments/054`, `lab/validation/`) is `coupled_segment_general`
   itself cross-checked against an independent numerical integrator at
   nonzero initial conditions.
3. I closed that specific gap myself this review, since it bears directly
   on whether P-054-3a's numbers can be trusted: RK4-integrated the same
   coupled ODE (`dn/dt`, `dΔT/dt`) at the mixed chain's own `dt_ss`/`tau_th`
   for all 4 Block-C ratio values, starting from representative nonzero
   `(n0, dT0)` pairs (e.g. `r=1e-1, n0=0.9, dT0=3e-5`). `coupled_segment_
   general` matches the RK4 result to ~1e-15 relative error at every test
   point. **The formula itself is correct** — this is not a physics bug,
   and it does not change my verdict on P-054-3a/3b/4's reported numbers,
   which I have now independently confirmed by an *actually* independent
   method. But that verification lives only in this review's scratch work,
   not in the codebase: the next cycle that edits `coupled_segment_general`,
   `kinetics.py`'s segment machinery, or their call sites has nothing in
   `lab/validation/run_all.py` that would catch a regression there, and the
   existing in-script assert would not catch one either, for the reason
   above.

This means P-054-7's claim ("full bench green... 3 new identity checks")
is accurate as literally stated but overstates what the trust suite
actually *protects*: it gates the new `thermo_sidecar.py` helpers, not the
imported ODE machinery the cycle's own headline reproducibility claim
(P-054-3a) most depends on.

## Ranked candidate next directions (Iteration 32+, this discipline's lens)

1. **Promote `coupled_segment_general` into a real trust-suite stage**, with
   a numerical-integrator cross-check (RK4 or `scipy.integrate.odeint`, matching
   exp-044's own precedent) at nonzero `(n0, dT0)` as the discriminating gate —
   not just the tautological `n0=dT0=0` reduction. This closes the one gap this
   review found that is not already closed, and is cheap: the check I ran this
   review is a ~40-line script.
2. **PHOTONICS' deferred Q_ext(x) closed-form check** (queued, not mandatory,
   per Red Team's audit). From this discipline's angle it is also a passivity
   sanity bound: `Q_ext = w_on/(2·r_out) ≈ 1.51` sits inside the passive
   extinction-paradox ceiling (`Q_ext → 2`) for a large absorbing cylinder, so
   nothing here signals a violation — but an unbounded convention artifact in
   how much of that 1.51 is real diffraction vs. `iso_xsec_sq` shape choice
   indirectly sets how large the `r_out`/`w_on` split (and the 9.15× τ_thermal
   shrink this whole cycle leans on) actually is.
3. **T8/T13's witness-scale `h_eff` bridge** (P-054-6, explicitly left open) —
   the one piece of Iteration 25's original tripwire this cycle still has not
   touched; the natural next link in the same standing chain.
4. Re-run exp-046's true-disk (97×) / fill-fraction (19,418×) sensitivity
   checks specifically against the MIXED-chain P-054-2/4 margins — NOTES.md's
   own idealizations list flags this was not re-verified for these particular
   numbers this cycle.

## Verdict: **PROMISING**

The corrected chain's physics is sound (independently re-derived, not just
trusted), and the specific concern my own Phase-2 seat raised — whether
"decoupled is conservative" survives a 9.15×-shorter τ_thermal — is now
genuinely, verifiably resolved at all 8 points, not merely claimed resolved
in a summary field. This is a real, load-bearing result, not a rounding
exercise. The defect found here is a rigor/process gap (regression-test
coverage for imported ODE machinery), not a result-invalidating physics
error — I independently confirmed the underlying formula is correct by a
genuinely independent method (RK4) this review, something the codebase
itself has never done for this function's nonzero-IC branch. That gap
should be closed before this machinery is leaned on again (Block C-style
re-runs are exactly this program's recurring idiom), but it does not
overturn P-054-1 through P-054-5's reported numbers.
