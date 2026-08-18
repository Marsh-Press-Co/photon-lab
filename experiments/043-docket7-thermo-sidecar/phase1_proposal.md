# Phase 1 proposal — verbatim (PHOTONICS, lead, panel Iteration 20)

Kept verbatim per this program's flag-don't-rewrite convention (T10
precedent). Superseded in load-bearing respects by Phase 3's synthesis in
`NOTES.md` — read that first for what was actually built.

## "Docket #7 + `lab/thermo_sidecar.py`: Sourcing the Witness Wattage/Dwell Window and Promoting the Ledger to Reusable Code" (candidate exp-043)

*Executing THERMODYNAMICS' pre-registered Iteration-19 tripwire (LOGBOOK.md Iteration 19 close, PLAN.md Tier-1 #1): a fourth consecutive deferral of docket #7/`thermo_sidecar` fires Checkpoint criterion 4 without further debate. This is legitimately PHOTONICS' lead slot per Iteration-18 precedent (a Red-Team-ranked priority not native to the lead seat's own charter) — precedent: Iteration 18 (QUANTUM led T20's audit, not a QUANTUM mechanism).*

### 1. Instrument/deliverable narrative (≤300 words)

Not a mechanism proposal — an instrument-and-sourcing build, the same class as exp-039 (`temporal_csf.py`), exp-040 (`amplitude_bridge.py`), and exp-036 (the RSA/TPA literature check). Two independently-scoped, separately-gated deliverables, run in the same cycle but never allowed to contaminate each other's verdict — the explicit answer to exp-042's own mandatory-fix #7 concern that bundling literature-sourcing with a code deliverable risks under-resourcing both.

**(A) Docket #7, narrowed to its current binding scope**: source two specific numbers via WebSearch — flashlight irradiance at the witness volume, and the beam's dwell time on one spot during a sweep — both cited repeatedly since Iteration 1 as "witness estimate ~10⁻³ W/cm²" and "10ms–1s window," neither ever backed by a citation. This directly ungates MATERIALS' `REALIZABILITY_MEMO.md` (every UNOBTANIUM-WITH-PARAMETERS irradiance-gap number rests on the unsourced 10⁻³ W/cm² figure) and THERMO's own NETD dispositions (dwell-limited, not steady-state, per constraint 4).

**(B) `lab/thermo_sidecar.py`**: promote the ad-hoc `thermo_sidecar_analytic` dict — independently copy-pasted with inconsistent regime handling into exp-032, -033, -034, -035's `run.py`/`design_geometry.py` — into one reusable module with real functions, dispatched correctly by optical-depth regime (weak-τ chord model vs. established σ_abs/σ_ext for near-saturating articles, a distinction the copy-pasted versions did not enforce uniformly), gated by a new trust-suite stage with an absolute identity. Applied for the first time to the program's own flagship article (`graded_black_shell`, the headline absorber) with real sourced wattage, not a placeholder.

*(NOTE, Phase-3: Red Team's Phase-2 desk audit found this "one dict, four copy-pastes" framing factually wrong on inspection — see NOTES.md's Phase 2/3 sections for the correction: three distinct implementations across four files, and the ON-endpoint was always hand-typed, never computed via the chord formula.)*

### 2. Parameter table

**Part A — docket #7 sourcing plan (WebSearch snippet-level; WebFetch confirmed blocked for scholarly domains across ≥5 consecutive shift-confirmations, T18 — see §6 sourcing-approach note)**

| Parameter | Current unsourced placeholder (LOGBOOK) | Planned search queries | Source tier sought |
|---|---|---|---|
| Flashlight luminous output | 100–200 lm (Iter. 1, VISION, unsourced) | "ANSI FL1 flashlight lumens rating standard"; "typical EDC flashlight lumens output review" | Standard spec (ANSI/PLATO FL1) + ≥2 retail/review aggregators |
| Luminous efficacy (lm→W conversion) | none used anywhere in this program | "luminous efficacy white LED lm/W typical"; "luminous efficacy function photopic 683 lm/W" | Photometry textbook / CIE standard (683 lm/W @ 555nm is an exact SI-linked constant; LED efficacy ~80–150 lm/W needs a separate cited figure) |
| Beam candela / full-angle | 5×10³–2×10⁴ cd (Iter. 1, unsourced) | "flashlight beam candela ANSI FL1 spec typical"; "flashlight beam angle degrees typical spot/flood" | Manufacturer spec sheets (≥2 named products) |
| Witness distance | 45 m [30,60] (Iter. 1, unsourced) | *not resourced this cycle* — carried as-is | — |
| Irradiance at volume | ~10⁻³ W/cm² ("witness estimate," never sourced) | *derived*: candela → intensity via efficacy, ÷ distance² | Computed from the two sourced figures above |
| Dwell time (beam-on-one-spot) | 10ms–1s (exp-036, unsourced, flagged as conflated with a different quantity) | "hand sweep angular velocity typical degrees per second"; "saccade dwell fixation duration typical ms" | Human-factors / biomechanics literature, ≥2 sources |

**Part B — `lab/thermo_sidecar.py` API (original proposal, superseded per Phase 3 — see NOTES.md)**

```
absorbed_fraction_weak_tau(tau)                    # (pi/4)*tau*(1-4*tau/3*pi), valid tau <= 0.5 [SUPERSEDED: EM's fix -> 0.032, reuse chord_absorptance_exact]
absorbed_fraction_established_ratio(sig_lo, sig_hi) # [SUPERSEDED: Red Team attack 1 -- under-specified, needs sigma_ext + dx as explicit inputs]
steady_state_delta_T(P_abs_W, area_m2, emissivity, h_conv)
transient_delta_T(P_abs_W, mass_kg, c_p, dwell_s, thermal_tau_s=None)
wien_peak_wavelength_um(T_K)
netd_disposition(delta_T_K, netd_band_K, fill_factor, emissivity_correction)
WitnessScenario(...)
```

**Trust-suite stage 15 (original scope, superseded — see NOTES.md attack 5):**
Wien's-law round-trip; `absorbed_fraction_weak_tau(0) == 0.0`; regression
vs exp-033's hardcoded `8.17e-4 K` (ambiguous re: which wattage — see
NOTES.md attack 6).

### 3. T1 escape-route statement

None directly — pure instrument/sourcing characterization. Feeds T5 and
MATERIALS' `REALIZABILITY_MEMO.md` — *(NOTE Phase-3: MATERIALS'
Phase-2 critique found this overstates the realizability-memo payoff; see
NOTES.md — reworded)*. Does not address Tier-W's glare clause (VISION's
separate deliverable).

### 4. Per-metric predicted outcomes (original — superseded, see NOTES.md's revised table)

| ID | Prediction | Band |
|---|---|---|
| P-D7-1 | Sourced irradiance-at-volume | [3×10⁻⁴, 3×10⁻³] W/cm² |
| P-D7-2 | Sourced dwell time | central [20ms, 500ms] |
| P-D7-3 | Disambiguation outcome | *(superseded: demoted to stated intent, not a falsifiable prediction — Red Team attack 4)* |
| P-TS-1 | Reproduces exp-033's 8.17×10⁻⁴K | ±25% |
| P-TS-2 | off_pass transient ΔT vs NETD [0.02,0.05]K | UNDETECTABLE, ≥10× below |
| P-TS-3 | ON-endpoint transient ΔT | [0.01K, 0.15K] *(superseded: see NOTES.md's fixed version)* |
| P-TS-4 | Headline absorber steady+transient ΔT | steady [0.03K,0.25K]; transient [0.005K,0.15K] *(superseded)* |

### 5. Idealizations (original)

Regime dispatch (chord vs. established ratio); lumped-capacitance uniform
ΔT; graybody radiative-equilibrium (questioned, unresolved); dwell-vs-
switching-speed conflation risk (flagged); achromatic by construction;
sourcing tier discipline; scope boundary (VISION's glare sidecar excluded).

### 6. Sourcing-approach note (T18)

WebFetch EGRESS_BLOCKED for scholarly domains, ≥5 consecutive
shift-confirmations. Manufacturer specs/standards expected more
WebSearch-tractable than the RSA/TPA scholarly literature exp-036 hit —
a reasoned, not guaranteed, expectation.
