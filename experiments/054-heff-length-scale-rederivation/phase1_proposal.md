# exp-054 — The `h_eff` Length-Scale Re-derivation (Phase 1 proposal)

Panel Iteration 31. Lead: **THERMODYNAMICS** (rotation broken — this is the
LOCKED, UNCONDITIONAL fifth-deferral trigger named at Iteration-25/26/27/28/29
closes; PLAN.md's Iteration-31 entry). Runner: cloud panel shift, 2026-08-21.

Executing THERMODYNAMICS' own standing tripwire: formally derive which
characteristic length is physically licensed for `h_eff = k_air/L` in
`lab/thermo_sidecar.py`'s established-ratio thermal chain, implement the
corrected, internally-consistent chain in the reusable module itself (not a
one-off script), and re-run it for exp-043's ON-endpoint (τ=3.9) and
exp-045's dose-accumulation article — replacing Iteration 25's informal,
not-run ~5.1×→~2.6× / ~27,080×→~38–42× estimates with real numbers.

## Mechanism narrative (the physical argument)

h_eff = k_air/L (the Nu=2 quiescent-gas conduction limit) governs heat loss
through the still-air boundary layer around the object's own real solid
surface — boundary-layer physics tied to the body's actual physical
geometry, not to how it scatters light. This program's two candidate lengths
are not interchangeable. r_out (78 cells, 2.34 μm) is the bench's real
simulated geometric radius. w_on (235.967 cells, 7.079 μm) is a measured
extinction-cross-section width, diffraction-inflated past the real object —
T9 already shows ratio_abs_ext=0.6075 exceeds the ≤0.5 geometric-optics
ceiling a real Q_ext=1 body would obey. A solid body cannot conduct, hold
thermal mass, or radiate through a surface larger than itself: h_eff,
mass_kg, and the radiating/convecting area must all derive from r_out, the
one length that is actually a physical property of the conducting, radiating
solid. w_on stays licensed for exactly one purpose — computing absorbed
power via the MEASURED σ_abs/σ_ext ratio (`absorbed_power_established_ratio`,
unchanged) — a separate, already-calibrated optical quantity, not a free
parameter inside the h_eff chain. Forcing that same ratio's power onto
r_out (silently reverting to geometric Q_ext=1) would be equally wrong in
the other direction, discarding a real measurement.

The corrected chain is therefore MIXED, not uniform: P_abs stays on w_on
(unchanged); h_eff, mass_kg, and radiating area all move to r_out, tied
together by one cross-consistency construction (reusing exp-045's own
`self_consistent_regime` pattern, whose two logged endpoints were each
internally consistent but used the wrong single length throughout). This
formalizes, promotes into `lab/thermo_sidecar.py` as reusable, trust-suite-
gated code, and closes by argument what Iteration 23 (T23) already argued
informally in a since-superseded Phase-1 draft script — never coded into the
sidecar module itself, never applied to exp-043/045's own two headline
articles as a committed result. (276 words.)

### Where this leaves the module's shape

`absorbed_power_established_ratio` is **unchanged** — its `w_on`-based
`iso_xsec_sq` idealization was never the bug; it correctly encodes a
measured optical cross-section. What changes is everything downstream:
`steady_state_delta_T`/`transient_delta_T`'s `h_conv`, `area_m2`, and
`mass_kg` arguments must all be constructed from ONE new length, `r_out`,
via one shared helper (two new functions: `gas_conduction_h_eff(k_air, L)`
= `k_air/L`, and `lumped_cube_mass_kg(density, L)` = `density*L**3`, mirroring
exp-045's own `self_consistent_regime` cube convention) — not from `w_on`,
and not independently re-derived per call site. `mass_kg`/area therefore use
a **different** length (`r_out`) than the length embedded in `P_abs`
(`w_on`, via `sigma_ext_cells`) — that asymmetry is the corrected answer,
not a residual bug, because `P_abs` and `h_eff` are not the same physical
question.

## Parameter table (reused, not re-measured — citations, no new geometry)

All values below are already committed in the record; this cycle adds zero
new FDTD geometry.

| Quantity | Value | Source |
|---|---|---|
| `dx_m` (600nm/cpl20 bench) | 30 nm | `experiments/043-.../run.py:167` |
| `r_out_cells` / `r_out_m` | 78 / 2.34 μm | `experiments/043-.../run.py:168`, reused `experiments/045-.../run.py:102,195` |
| `sigma_ext_cells` (ON, τ=3.9) | 235.96673494878587 | exp-026 measurement; `experiments/043-.../results.json::on_endpoint_tau_3p9.sigma_ext_cells` |
| `w_on` (= `sigma_ext_cells·dx_m`) | 7.079002048463575 μm | derived, matches `experiments/045-.../results.json::block_b...w_on_consistent.length_m` |
| `ratio_abs_ext` (ON) | 0.6074830175566805 | `experiments/043-.../results.json::on_endpoint_tau_3p9.ratio_abs_ext_measured` |
| τ_center (ON endpoint) | 3.9 | exp-026/043/044/045 σ(I) endpoint definition |
| `P_abs_w` (ON, central / range) | 2.0044347652689456e-12 W / [3.34e-13, 1.344e-11] W | `experiments/043-.../results.json::on_endpoint_tau_3p9` |
| `irr_central` (P-D7-1) | 6.58e-6 W/cm² | `experiments/043-.../results.json::p_d7_1_irradiance` |
| `dwell_central` (P-D7-2) | 66.7 ms | `experiments/043-.../results.json::p_d7_2_dwell` |
| `NETD_BAND_K` (P-D7-4) | [0.020, 0.050] K | `experiments/043-.../results.json::p_d7_4_netd` |
| `k_air` | 0.026 W/(m·K) | `experiments/045-.../run.py:194` (textbook, room temp) |
| Silicon identity (ρ, C_p, κ_solid) | 2330 kg/m³, 700 J/(kg·K), 148 W/(m·K) | `experiments/037-.../NOTES.md:828-829`, reused `experiments/045-.../results.json::block_b...material_identity` |
| Emissivity, T_ambient | 0.9, 293.15 K | `experiments/043-.../run.py`, `experiments/045-.../run.py:106-107` |
| **Already-computed "mixed"-chain point** (ON endpoint) | `dt_ss_full`=3.293076e-5 K, margin=607× below NETD lo | LOGBOOK.md Iteration 23 close (exp-046 Phase 4, `dwell/τ_thermal`=194.176815× "bit-identical to `r_out`-consistent") — computed as a side-consequence of T23's closure, never stored as its own labeled result key, never coded into `lab/thermo_sidecar.py` |
| Dose-accumulation article (Block C, Host D, current headline) | `max_dT_periodic_decoupled_K`=7.385465974827066e-7 K, margin=27,080.214× (uses the `w_on`-consistent regime as primary, per `run.py:557`) | `experiments/045-.../results.json::block_c_dose_accumulation_kinetics` |
| `w_on`-consistent `dt_ss_full` (ON endpoint, for scaling) | 1.0875240683859519e-05 K | `experiments/045-.../results.json::block_b...w_on_consistent.dt_ss_full_K` |

**No new FDTD calls required.** Zero new simulation geometry — this is a
re-derivation of an existing sidecar computation from already-committed
inputs, matching the Iteration-20/22/25 sidecar-cycle precedent (desk/
analytic only). Phase 4 work is: (a) implement the two new helper functions
and the cross-consistency assertion in `lab/thermo_sidecar.py`; (b) a new
trust-suite identity stage (`h_eff·L == k_air` exactly; `mass_kg` built from
the same `L`; bit-for-bit reproduction of the already-published 3.293076e-5K
ON-endpoint figure as a regression anchor); (c) re-run exp-043's ON-endpoint
and exp-045's Block C dose-accumulation grid through the corrected chain.

## T1 escape route

**NONE.** This is pure instrument/model-fidelity work — correcting which
physical length feeds a post-run analytic heat-transfer formula — not a
mechanism proposal. It makes no claim about σ(I), σ(x,t), angular
selectivity, or sub-threshold operation, and does not touch any FDTD
scene. Matches the Iteration 20 (exp-043), Iteration 22 (exp-045), and
Iteration 25/27 (exp-048/050) sidecar/instrument-fidelity cycles' own
T1 disposition.

## Per-metric predicted outcomes (falsifiable, committed before any run)

| ID | Prediction | Band | Basis |
|---|---|---|---|
| P-054-1 | Corrected `dt_ss_full` for exp-043's ON-endpoint (τ=3.9), mixed chain (`P_abs` on `w_on`, `h_eff`/mass/area on `r_out`) | [2.8e-5, 3.6e-5] K | Reproduces the already-published 3.293076e-5K side-computation (LOGBOOK Iteration 23); band allows for the formal implementation surfacing a small (≤10%) discrepancy against the informal script arithmetic, not a wholesale re-derivation |
| P-054-2 | Corrected NETD-lo margin for the ON-endpoint | **500×–750×** (central ≈607×) | 0.020K / P-054-1's band |
| P-054-3 | Corrected `dt_ss_full` for exp-045's dose-accumulation worst-case point (Block C, current `w_on`-consistent max periodic ΔT scaled by the mixed/`w_on`-consistent `dt_ss_full` ratio, 3.293076e-5/1.0875240683859519e-05 ≈ 3.0284×, applied to 7.385465974827066e-7 K) | [1.9e-6, 2.6e-6] K | Linear-scaling argument: the decoupled dose-accumulation proxy is `dt_ss_full·n(t)`, and `n(t)` (population fraction) is set by kinetics alone, independent of the thermal-chain length choice (exp-045's own `results.json::block_c...scope_note`) — so the correction factor derived for the ON-endpoint carries over exactly |
| P-054-4 | Corrected NETD-lo margin for the dose-accumulation article | **7,000×–11,000×** (central ≈8,900×) | 0.020K / P-054-3's band |
| P-054-5 | Classification for both articles | Both stay **UNDETECTABLE**, not MARGINAL or DETECTABLE | No candidate chain (buggy original, `w_on`-consistent, `r_out`-consistent, or mixed) computed anywhere in exp-043/045/046's own record has ever produced a margin below 5× |
| P-054-6 | Comparison against Iteration 25's informal estimate | **REFUTED, not confirmed** — corrected margins land 2–3 orders of magnitude ABOVE the informal ~2.6× / ~38–42× guess, not near it | Iteration 25's estimate predates T23's own already-computed 607×/194.18× figures (Iteration 23, one cycle earlier) and appears not to have incorporated them; the dominant effect this cycle re-confirms is Iteration 20 Phase-5's own finding that fixing the ORIGINAL `h_conv=5.0 W/(m²K)` macroscopic placeholder to any gas-phase-conduction value (~3,700–11,000 W/(m²K)) raises the cooling rate by 2–3 orders of magnitude on its own, before the `r_out`-vs-`w_on` question is even asked |
| P-054-7 | New trust-suite stage | ≥3 new identity checks (h_eff·L, mass-from-same-L, ON-endpoint regression anchor), full bench green, 0 new FDTD calls | Iteration-20/22 sidecar-stage precedent |

Falsification condition, stated plainly: if the Phase 4 code run lands
P-054-2 or P-054-4 outside their stated bands (particularly if either drops
toward Iteration 25's ~2.6×/~38–42× guess, or below 5×), that is a real,
reportable surprise — not a rounding difference — and should be treated as
evidence the mixed-chain argument above has an error, not smoothed over.

## Idealizations (stated before any run)

- **Nu=2 quiescent-gas conduction limit** — still air, no forced convection
  or drafts; unchanged from Iteration 20/22's own standing idealization.
- **Lumped-capacitance, cube-shaped thermal mass** (`mass_kg = ρ·r_out³`) —
  reuses exp-045's own `self_consistent_regime` convention rather than a
  true-disk or fill-fraction model; exp-046's own Phase-4 sensitivity check
  found the operative `dwell/τ_thermal` conclusion survives a true-disk
  (97×) and fill-fraction-down-to-1% (19,418×) recheck, but this cycle does
  not re-run that sensitivity sweep for the NETD-margin numbers specifically.
- **Steady-state graybody radiative linearization** about `T_ambient` — small
  -signal `dP/dT`, not a full nonlinear Stefan-Boltzmann solve; unchanged
  from the module's existing `steady_state_delta_T`.
- **Bench-scale, not witness-scale.** All numbers stay at this bench's own
  FDTD geometry (`r_out`≈2.34 μm); T8/T13's near-field→witness-scale bridge
  remains separately unresolved and is not attempted here, exactly as
  exp-043/045 each state for their own bench-scale sidecar numbers.
- **Static ON-state ratio, not a σ(I) transient model.** The ON-endpoint's
  `ratio_abs_ext=0.6075` is treated as a steady-state ceiling; any
  dwell-limited kinetics gating (via `lab.kinetics.relax_exact`, as exp-043
  already applies) is unaffected by this cycle's length-scale correction —
  the kinetics fraction `n_at_dwell/n_ss` is independent of `h_eff`.
- **Slip-flow correction not applied to the headline.** `r_out`(2.34 μm) has
  a larger Knudsen number (≈0.028) than `w_on` did (≈0.009) — closer to,
  but still inside, the continuum regime; exp-045's own first-order
  thermal-slip correction (≈-5.3% at `r_out`) is disclosed as a sensitivity
  bound, not folded into the headline `h_eff`, matching its own precedent.
- **Achromatic by construction** (`ε_r≡1`, non-dispersive σ) — no per-λ
  dependence re-examined this cycle; exp-045's own Phase-5 finding that
  `dwell/τ_thermal` stays in-band across all 3 swept wavelengths for the
  `w_on`-consistent regime is not re-verified for the mixed regime here.
- **`P_abs` itself is measurement-locked, not re-derived.** This cycle does
  not revisit whether `absorbed_power_established_ratio`'s `iso_xsec_sq`
  convention is the right one for absorbed power — that question (T22) is
  explicitly out of scope; only the downstream `h_eff`/mass/area chain is
  corrected.
