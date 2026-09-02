#### THERMODYNAMICS — verdict: **CONFIRM**

**Independent verification performed directly against source, not NOTES.md's prose**

1. **`run.py` import/invocation check (grep, not trust).** `grep -n -i "thermo|sidecar|delta_t|netd|p_abs|import"` against
   `experiments/103-t28-gateb-footprint-aperture-match/run.py` returns exactly two `import` lines:
   `from lab import Sim, materials` and `from lab import sections as sc`. No occurrence of `thermo`, `sidecar`, `p_abs`,
   `delta_t`, or `netd` anywhere in the file outside the two disclosure comment/print blocks (docstring lines 17-25, print
   block lines 180-184) that *describe* the sidecar in prose. **Confirmed: `lab.thermo_sidecar` is genuinely never
   imported or invoked in this file.**

2. **`results.json` top-level key sweep for undisclosed thermal fields.** Enumerated every key at every nesting level
   programmatically and grepped the full key list for `therm|temp|delta|watt|power|abs_w|netd|radia|emiss` — **zero
   matches**. Full top-level key set: `experiment, panel_iteration, n_fdtd_calls, wall_primary_s, wall_2x_s,
   total_wall_s, geometry, behind_window, kappa_window, kappa_region_trend, floor_gate, settling_check, predictions`.
   `geometry`'s own sub-keys: `N, absorb, courant_frac, steps, steps_2x, src_x, cx, cy, r_core, r_coat, cpl, edge,
   h_region, floor_frac, stability_tol`. Nothing thermal-sounding is silently present. **R21 does not fire — there is
   no persisted-but-unnarrated thermal sidecar byproduct anywhere in this cycle's results.json.**

3. **Dependency-chain claim, verified against `lab/thermo_sidecar.py`'s own function body (lines 124-170), not
   NOTES.md's characterization of it.** `absorbed_power_established_ratio(i_incident_w_cm2, sigma_ext_cells, dx_m,
   ratio_abs_ext, area_convention="iso_xsec_sq")` — read the full body directly. `p_abs_w` is computed as
   `width_m = sigma_ext_cells * dx_m; area_m2 = width_m**2; area_cm2 = area_m2*1e4; p_ext_w = i_incident_w_cm2 *
   area_cm2; p_abs_w = p_ext_w * ratio_abs_ext`. Every symbol on that path (`sigma_ext_cells`, `dx_m`, `ratio_abs_ext`,
   `i_incident_w_cm2`) is a caller-supplied scalar; none of them is derived from, or reads, this experiment's FDTD
   source construction, amplitude, or `edge` parameter. **NOTES.md's dependency-chain claim is correct, confirmed by
   reading the function body myself, not by trusting the citation.**

4. **699.27× citation (exp-057), traced independently.** `experiments/057-graded-black-shell-flagship-mixed-regime/`
   pins `p_abs_w = 1.7409069740390205e-12 W`, sourced from `absorbed_power_established_ratio(sigma_ext_cells=
   240.0073740162445, ratio_abs_ext=0.51)` established in exp-043, and states this value is "NOT re-derived this
   cycle" (regression-asserted, not recomputed). `sigma_ext_cells=240.0073740162445` is exp-059's Mie/qext-theory
   extinction-width figure — a value with no dependency on exp-103's `add_line_source(edge=...)` construction at all.
   Since exp-103 changes only the source-side `edge`/taper parameter and touches no `sigma_ext_cells`, `ratio_abs_ext`,
   or `i_incident_w_cm2` input, **the 699.27× citation's own code path is unaffected by this cycle, confirmed on my own
   independent trace, not merely on NOTES.md's assertion.**

**Independent recomputation of headline numbers, from raw `results.json` fields**

- `kappa_window` recomputed as `article.mean / empty.mean` — exact match to reported `kappa_window.value`.
- `span_mean`/`ratio_to_window` recomputed from the 11 raw `kappa_region_trend` entries — exact match to both.
- `floor_gate.rms`/`floor`/`n_unresolved` recomputed — exact match.
- Reversal count for Prediction 2 recomputed from scratch = 0, strictly monotonic — exact match.
- One settling-check point spot-verified (x=352) — exact match.

All five independently recomputed quantities matched `results.json`'s own reported values exactly — no arithmetic or
transcription defect found anywhere I checked.

**Findings**

- **[non-load-bearing]** The thermal-sidecar disclosure (fix 7) is present in triplicate — NOTES.md Setup,
  NOTES.md Idealizations, and `run.py`'s own docstring/print block. Good discipline; no action needed.
- **[load-bearing]** All checked headline numbers reproduce exactly from raw fields. This cycle's arithmetic
  integrity is solid on every path I independently walked.
- **[non-load-bearing]** The line-number citation ("`lab/thermo_sidecar.py:124-168`") is close enough to be useful.

**Charter-relevance disposition, argued explicitly**

This cycle is genuinely orthogonal to THERMODYNAMICS' charter. `kappa_window`/`kappa_region` are behind-object
field-transmission intensity ratios — a near-field-optics/diffraction diagnostic, not an energy-budget question (no
`sigma_abs`, `sigma_ext`, or absorbed-fraction quantity is computed or touched anywhere in `run.py`). I find **zero
energy-balance content** in this cycle and register that explicitly, per my charter's own instruction to say so
rather than leave a blank review.

**Argued next change**

No sidecar-adjacent change is warranted by this cycle itself. My argued next change is process-level and
forward-looking: when Iteration 81 executes the deferred Tier 1 item 3 (T8 r=78/156/312 bridge extension), that
extension pushes this instrument toward witness-scale geometry — the same regime `lab/thermo_sidecar.py`'s own
scenario chain operates in. THERMODYNAMICS should pre-emptively flag, before that cycle's Phase 1 proposal is
written, that if the bridge extension's own source-aperture or standoff conventions end up reused (even by named
constant — the exact failure mode this cycle's own Learned #1 just diagnosed for `R4_TAPER`) inside any future cycle
that *does* invoke `thermo_sidecar`, the same cross-resolution rescaling scrutiny must be applied again to any
length/area constant crossing into a thermal-sidecar call — and that such a cycle's Result prose must narrate the
sidecar's own headline number inline (R21), not merely cite or persist it, the moment invocation actually occurs.
