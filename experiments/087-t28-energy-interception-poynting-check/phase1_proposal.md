# PHASE 1 — PROPOSAL · Panel Iteration 64 · exp-087 · Lead seat: THERMODYNAMICS

## "Measuring the Energy-Interception Cross-Check for Real" — a purpose-built, article-loaded Poynting-box measurement of `PAIR_PAD`'s absorbed/extinguished power, discharging the Iteration-59 forward tripwire

### 1. Mechanism narrative (≤300 words)

Not a phenomenon-mechanism proposal. Like every T28 instrument cycle since
exp-069, Checkpoint criterion 2 is N/A (§3). This is THERMODYNAMICS' own
half of the joint EM/THERMO energy-interception cross-check — named
jointly at Iteration 59/exp-082, deferred/exempt four consecutive cycles
since (083–086), now under a pre-announced fifth-deferral tripwire
(LOGBOOK Iteration 63, PLAN.md's active queue).

The cross-check's originally-scoped shape (Iteration 59) was a zero-FDTD
sanity bound reusing T9's broadside σ_abs/σ_ext=0.51 anchor. This
proposal instead measures it: `lab/sections.py`'s already-stage-8-gated
Poynting-box ledger (`widths()`), never yet applied to the T28
article-loaded scene, runs on the SAME flagship-absorber-loaded C40/G40
geometry exp-082/083 already built and validated, at a small subset of
the established 31-point window (θ=36°/39°/42° — the two edges + center)
— fresh, scene-specific σ_abs(θ)/σ_ext(θ) for both configs, at real
oblique incidence, for the first time. (T9's 0.51 anchor is a broadside
figure from a structurally different beam-scene bench — a genuine,
previously-unflagged commensurability gap this measurement closes rather
than assumes.)

`lab/thermo_sidecar.py`'s established chain
(`absorbed_power_established_ratio` → `mixed_length_scale_regime` →
`netd_disposition`) converts each measured width into an absorbed watt
and a scene-specific detectability figure, reusing exp-043's sourced
witness irradiance and exp-057's silicon thermal constants verbatim. The
genuinely new number is the article's REAL absorbed power's own
PAD-sensitivity: does `p_abs(θ)` change between C40 and G40 by a fraction
comparable to the already-measured Weber-contrast ripple
(`delta_scene(θ)`, exp-083, cited not recomputed), or is it decoupled —
does the confound's own energy budget corroborate or contradict ten-plus
cycles of phase/interference evidence (exp-076's lossless-vacuum proof),
now with the absorbing article physically present in the echo's own
round-trip path, closing the exact gap THERMODYNAMICS flagged at exp-082
Phase 2 ("`PAIR_PAD`'s proven losslessness was established empty-scene-
only, never re-verified with a real absorber in the echo's own round-trip
path").

### 2. Parameter table

| Quantity | Value | Source |
|---|---|---|
| λ | 600 nm | consistent with the rest of the T28 window (exp-069/082/083); no deviation |
| `dx_m` (grid pitch) | 30 nm = 3.0×10⁻⁸ m | `cpl=20` @ 600nm bench convention, exp-043/054/057/059 |
| `cpl` | 20 | `dg065.CPL[600]`, exp-082/083's own `_run_sim` |
| Article | PEC disk r=30 + `graded_black_shell` shell r_in=30→r_out=78 (defaults `sigma_max=0.5, eps_max=1.0`) | `materials.pec_disk`/`materials.graded_black_shell`, bit-identical to exp-024's `build("absorber")` and exp-082/083's `build_article()` |
| Configs | `C40`: absorb=40, pad=0, nx=360, ny=1584, obj_x=170, obj_y=792, src_x=300, plane_x=77, y_lo=40, y_hi=1544. `G40`: absorb=40, pad=40, nx=440, ny=1664, obj_x=210, obj_y=832, src_x=340, plane_x=117, y_lo=80, y_hi=1584 | `dg065.CONFIGS["C40"]`/`["G40"]` (`experiments/065-.../design_geometry.py`), re-exported verbatim by `dg069` |
| Angle subset | θ ∈ {36.0°, 39.0°, 42.0°} (window edges + center; 3 of the established 31) | `dg069.DENSE_ANGLES[0]`, `[15]`, `[-1]` |
| STEPS | 2800 (settled) | `dg069.STEPS_SETTLED`, matches exp-083's `STEPS_MAIN` |
| Poynting box `BOX_A` | C40: (80,260,702,882); G40: (120,300,742,922) — R_OUT+12 clearance | translates exp-024's established `BOX_CLEARANCE=12`/`OBJ_X,OBJ_Y,R_OUT=78` convention by the PAD shift (`obj_x,obj_y` per config) |
| Poynting box `BOX_B` | C40: (68,272,690,894); G40: (108,312,730,934) — R_OUT+24 clearance | **new this cycle**, box-independence companion, doubles `BOX_A`'s clearance, stays inside `GUARD_OUT=185` on every side |
| `REF` (i_inc strip) | C40: (170,792,80); G40: (210,832,80) | exp-024's established `REF=(OBJ[0],OBJ[1],80)` convention, translated by the PAD shift |
| WitnessScenario irradiance | `irr_central = 6.584362139917695e-06` W/cm² (candela=40000, efficacy=300 lm/W, distance=45 m) | exp-043's sourced `WITNESS` (WebSearch snippet-tier, T18); reused verbatim, **not** re-searched or re-derived this cycle |
| Thermal constants | k_air=0.026 W/(m·K), ρ=2330 kg/m³, c_p=700 J/(kg·K), emissivity=0.9, T_ambient=293.15 K (silicon, ASSUMED, provenance unsourced, T18/`REALIZABILITY_MEMO.md`) | exp-057's own committed constants, reused verbatim |
| `l_geometric_m` | 78×30nm = 2.34×10⁻⁶ m | `length_provenance="bench_construction"` (R_OUT is a real FDTD scene dimension, licensed per T23/exp-064) |
| NETD band | (0.020, 0.050) K | exp-043's sourced band (FLIR A325sc <50mK; academic high-performance ~20–30mK) |
| T9 broadside anchor (context only) | σ_abs/σ_ext = 0.51; `sigma_ext_cells=240.0073740162445`; `p_abs_w=1.7409069740390205e-12` W; `dt_ss=2.8601275372385233e-05` K; NETD margin ≈699.27× | `experiments/002`/`020`/`030` (ESTABLISHED, LOGBOOK.md); `experiments/057-.../run.py` — independently reproduced bit-exact this cycle by direct invocation of `lab.thermo_sidecar` (R4) |
| `delta_scene(θ)`, `C40_C(θ)` (cited, zero new FDTD) | θ=36°: Δ=-4.287148×10⁻⁴, C=-0.5763629; θ=39°: Δ=-1.484493×10⁻³, C=-0.5541307; θ=42°: Δ=-8.029954×10⁻⁴, C=-0.5175151 | `experiments/083-.../results.json::per_theta` — read, never hand-typed |
| Reproduction targets `C_empty(cfg,θ)` (zero new FDTD, cited) | C40: -0.008339 / 0.005174 / -0.003212 (36/39/42°); G40: -0.010497 / 0.004544 / -0.000185 | `experiments/083-.../results.json::per_theta[θ]["{C40,G40}_Ce"]` |
| Total new FDTD calls | 12 (2 configs × 3 angles × {empty, article} legs) | — |

### 3. Checkpoint criterion 2 statement

**N/A**, matching every T28 desk/instrument cycle since exp-069 and
exp-082's/exp-083's own explicit ruling ("instrument-fidelity/
generalization work, N/A — not merely not-yet-ripe"). This proposal makes
no phenomenon-mechanism claim and touches no constraint-3 witness scene;
it measures a bookkeeping quantity (absorbed/extinguished power) on an
already-scored T28 confound-diagnostic geometry. There is no T1
escape-route framing for this cycle to state.

### 4. Falsifiable predicted outcomes

**P1 (desk, zero-FDTD precondition).** `Sim.__init__`'s `damp_e` array
reads exactly `1.0` (pure vacuum, no graded loss) at every `BOX_A`/`BOX_B`
footprint cell, both configs — extending exp-065's own
`static_construction_identity` bit-exact-vacuum check to this cycle's new
box windows. **Predict PASS** (by construction: `R_OUT+24=102` cells
clears the `ABSORB=40` band by 62+ cells on every wall, per the parameter
table). **Must PASS before any FDTD-derived width is trusted** (same
halt-if-fails discipline as exp-065's causal-identity gate).

**P2 (reproduction precondition).** Fresh `C_empty(cfg,θ)` at θ∈{36,39,42}°
for C40/G40, computed from this cycle's own captures via
`amb.contrast_from_runs`, must reproduce the cited exp-083 values (table
above), max|Δ|<1e-9. **Predict PASS** — identical `Sim`/`build_article`
construction, reused via `_load()`, not retyped.

**P3 (box independence / noise floor, disclosed, not gating a verdict).**
`box_dev_ext(cfg,θ) = |σ_ext(BOX_A)−σ_ext(BOX_B)|/|σ_ext(BOX_A)|` and the
analogous `box_dev_abs` for σ_abs, reported at all 6 (cfg,θ) cells — sets
the instrument noise floor P5 gates against. No fixed number
pre-registered (context-setting, same role `box_dev` plays throughout
this program, e.g. exp-002/exp-028).

**P4 (measured energy quantities, disclosed context, NOT scored against a
fixed band).** σ_abs(cfg,θ)/σ_ext(cfg,θ) at `BOX_A`, compared informally
to T9's broadside anchor (0.51). Genuine uncertainty whether 36–42°
oblique incidence on a circularly-graded, rotationally-symmetric absorber
departs materially from the broadside figure (no established T28/T9
citation bears on this angle regime); reported, not pre-scored.

**P5 (PRIMARY, pre-registered, falsifiable).** For each θ∈{36,39,42}°:
compute `p_abs_w(cfg,θ)` via
`ts.absorbed_power_established_ratio(irr_central, σ_ext_cells(cfg,θ,BOX_A),
dx_m, ratio_abs_ext(cfg,θ,BOX_A))`;
`frac_p_abs(θ) = |p_abs_w(G40,θ)−p_abs_w(C40,θ)| / p_abs_w(C40,θ)`;
`frac_contrast(θ) = |delta_scene(θ)| / |C40_C(θ)|` (cited verbatim from
exp-083, table above: 7.44×10⁻⁴ / 2.68×10⁻³ / 1.55×10⁻³ at 36°/39°/42°);
`ratio_k(θ) = frac_p_abs(θ) / frac_contrast(θ)`.

*Noise-floor gate*: an angle is **UNRESOLVED** (excluded from
classification, disclosed not silently dropped) if
`|p_abs_w(G40,θ)−p_abs_w(C40,θ)|` does not exceed
`3 × max(box_dev_ext, box_dev_abs)(cfg,θ) × p_abs_w(C40,θ)` for either
config.

*Classification, over the resolved angles*:
- **ENERGY-DECOUPLED**: `ratio_k(θ) < 0.1` at every resolved angle.
- **ENERGY-DOMINANT**: `ratio_k(θ) > 10` at any resolved angle.
- **CONSISTENT**: every resolved angle has `0.1 ≤ ratio_k(θ) ≤ 10`.
- **MIXED**: resolved angles span more than one of the above.

**Pre-registered prediction: ENERGY-DECOUPLED at ≥2 of the 3 angles**,
stated with only moderate confidence. Reasoning (stated, not hidden): `σ_ext`
integrates a bulk Poynting flux over the object's own extinguishing
cross-section, while `delta_scene` is a background-subtracted, highly
localized contrast measurement at one observation window — a small
coherent phase perturbation at the object (the class of effect exp-076's
lossless-vacuum proof already implicates) can produce an easily-detected
local contrast delta without a comparably-fractional imprint on a
bulk-integrated power quantity. This prediction is corroborative, not
dispositive: a single 3-angle cycle cannot single-handedly overturn or
confirm ten-plus cycles of convergent phase/interference evidence: **it
can genuinely surprise it.** Falsified by CONSISTENT or ENERGY-DOMINANT
at ≥2 of 3 resolved angles, or by MIXED — either would be a materially
new finding warranting immediate follow-up, not a failure of this
proposal.

**P6 (scene-specific detectability, pre-registered).** `netd_disposition`
(via `mixed_length_scale_regime`, `l_geometric_m=2.34×10⁻⁶` m,
silicon-assumed) for both configs at all 3 angles. **Predict
UNDETECTABLE at every (cfg,θ) cell** — consistent with the flagship
absorber's every prior disposition (~699× margin at broadside, T5/exp-043/
exp-057). Falsified only if oblique σ_ext/ratio_abs_ext departs from the
broadside anchor by more than ~2 orders of magnitude, which no existing
T28/T9 citation suggests; a flip here would itself be a significant,
independently-flaggable finding.

### 5. Idealizations

1. **3-angle subset, not the full 31-point window.** Characterizes only
   the window's edges + center, not its fine θ-structure. If Phase 2/5
   judges the energy channel's own θ-dependence needs denser sampling,
   that is a follow-up, not this cycle's scope.
2. **Single λ=600nm**, matching the rest of the T28 window; no
   generalization to 450/750nm attempted here (the x-wall
   wavelength-generality leg, 11 cycles deferred, is a separate,
   standing item, out of this cycle's own scope).
3. **`iso_xsec_sq` area convention** (thermo_sidecar's own stated
   idealization, inherited unchanged): the absorbed-power↔area mapping
   treats the object as compact, not an infinite rod.
4. **Silicon thermal constants (ρ, c_p) are ASSUMED**, provenance
   unsourced (T18, `REALIZABILITY_MEMO.md`'s standing downgrade), reused
   verbatim from exp-057, not re-litigated this cycle.
5. **WitnessScenario irradiance/distance/candela are WebSearch
   snippet-tier** (T18, WebFetch confirmed EGRESS_BLOCKED), reused
   verbatim from exp-043, not re-searched this cycle.
6. **The `ratio_k` decade-scale tiers (0.1×/10×) are a deliberately wide,
   first-of-its-kind falsification band**, not a rigorously derived
   confidence interval — a stated methodological choice given genuine
   uncertainty in both the `widths()` ledger's own noise floor and the
   physical mapping between a bulk power integral and a localized
   contrast measurement.
7. **Settling is NOT independently re-verified for the `widths()`-derived
   channel specifically.** STEPS=2800 is T28's own established settled
   value for the Weber-contrast phasor channel (same `full_capture`/
   `phasors` primitive); this cycle inherits that settling evidence
   rather than re-running a dedicated STEPS=1400-vs-2800 spot-check on
   `sigma_abs`/`sigma_ext` themselves. Flagged as a plausible
   mandatory-fix candidate for Phase 2/3, not preempted here.
8. **The 3× box-dev noise-floor multiplier is a house-style choice**
   (mirrors R3's "survive a resolution change with margin" precedent),
   not a formally derived statistical significance threshold.
9. **NETD is an instrument/detector threshold, not a human-eye one**
   (standing disclaimer, inherited every prior cycle this sidecar is
   used).
10. **This cross-check bears only on T28's own confound-mechanism
    question and constraint-3's energy-ledger bookkeeping.** It does not
    test constraints 1/2/4, and does not re-open or re-score
    `REALIZABILITY_MEMO.md`'s verdict.
11. **Not this cycle's mandate, named but not scored**: the
    near-unanimous #1 grazing-incidence validity check
    (`edge_diffraction_c_empty_corrected`, PHOTONICS' charter), the
    x-wall wavelength-generality leg (11 cycles deferred), the full-scale
    null-calibration re-run, and R12-into-standard-practice all remain
    real, overdue T28 board items (PLAN.md's own Iteration-64 ranking,
    Tier 1/2) — they belong on Iteration 65's board, not folded into this
    proposal's own scored predictions.

### 6. Phase 4 plan (for Phase 2 critics to react to)

A single new script, `experiments/087-t28-energy-interception-poynting-
check/run.py`, will: (a) `_load()` exp-083's own `run.py` (the
`_load()` cross-experiment idiom already established, e.g. exp-083
loading exp-077's `pad_round_trip_model.py`) to reuse `dg` (→`dg069`),
`build_article`, `_run_sim` **verbatim, unmodified** — zero geometry
retyped; (b) define `box_a(cfg)`/`box_b(cfg)`/`ref(cfg)` translating
exp-024's established `BOX_CLEARANCE`/`REF` convention by each config's
own `obj_x`/`obj_y` (§2); (c) run P1's static-vacuum-footprint desk check
on both configs' `Sim.__init__` arrays (zero `.run()` steps) — **HALT if
it fails**, before any FDTD call; (d) run the 12 FDTD calls (3 angles ×
2 configs × {empty, article}, STEPS=2800), capturing via
`sc.full_capture`; (e) from each pair, compute `sc.widths()` at `BOX_A`
and `BOX_B`, and `amb.contrast_from_runs` for the P2 reproduction check;
(f) feed `BOX_A`'s σ_ext/ratio_abs_ext into
`ts.absorbed_power_established_ratio` (`irr_central`, `dx_m` from §2),
then `ts.mixed_length_scale_regime` and `ts.netd_disposition`; (g)
compute `frac_p_abs(θ)`, cite `frac_contrast(θ)` from exp-083's committed
`results.json` (read, never hand-typed), classify per §4-P5 with the
noise-floor gate applied first; (h) persist every intermediate
(`σ_abs`, `σ_ext`, `box_dev_*`, `p_abs_w`, `dt_ss_full_K`,
`netd_disposition`, `ratio_k`, resolved/unresolved flags) to
`results.json`. Output: `results.json` + `NOTES.md` reporting P1–P6
against this document's own pre-registered bands, plus an explicit
statement of what this cycle does and does not license about T28's
substantive mechanism question.

### 7. Tripwire discharge

This proposal is a genuine, purpose-built, article-loaded FDTD
measurement of the joint EM/THERMO energy-interception cross-check — not
the fifth silent/thin deferral the tripwire (LOGBOOK Iteration 63,
PLAN.md Tier 2 item 4) exists to catch.
It reuses the already-built, already-validated `PAIR_PAD` article-loaded
scene (exp-082/083) and the already-stage-8/-gated `sections.widths()`
Poynting-box machinery — never before combined — at a disclosed, bounded,
cheap 12-call subset of the established window, with a falsifiable,
numeric, pre-registered pass/fail classification (§4-P5) decided before
any code runs. Executing this Phase 1 → Phase 4 in full, with the
predicted bands scored honestly against the real measurement, directly
discharges the tripwire regardless of which classification (ENERGY-
DECOUPLED / CONSISTENT / ENERGY-DOMINANT / MIXED) the data return — the
tripwire's condition is "build it or explicitly retire the deferral
framing," not "confirm a particular answer." No result this cycle can
produce constitutes a sixth deferral.
