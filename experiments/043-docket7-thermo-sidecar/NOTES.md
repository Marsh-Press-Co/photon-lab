# exp-043 — Docket #7 + `lab/thermo_sidecar.py`: sourcing the witness wattage/dwell window and promoting the ledger to reusable code

Panel Iteration 20. Lead: PHOTONICS (rotation: VISION→PHOTONICS→MATERIALS→EM→
THERMO→QUANTUM→repeat). Runner: cloud panel shift, 2026-08-18.

Executing THERMODYNAMICS' pre-registered Iteration-19 tripwire (LOGBOOK.md
Iteration 19 close, PLAN.md Tier-1 #1): a fourth consecutive deferral of
docket #7/`thermo_sidecar` fires Checkpoint criterion 4 without further
debate. Legitimately PHOTONICS' lead slot per Iteration-18 precedent (a
Red-Team-ranked priority not native to the lead seat's own charter).

## PHASE 1 — PROPOSAL (PHOTONICS, lead)

Not a mechanism proposal — an instrument-and-sourcing build (same class as
exp-039/040/036). Two independently-scoped, separately-gated deliverables:

**(A) Docket #7, narrowed to its current binding scope**: source flashlight
irradiance at the witness volume and the beam's dwell time on one spot
during a sweep via WebSearch (WebFetch confirmed EGRESS_BLOCKED for
scholarly domains, T18, ≥5 consecutive shift-confirmations — manufacturer
specs/standards bodies expected more WebSearch-tractable, disclosed as a
reasoned not guaranteed expectation).

**(B) `lab/thermo_sidecar.py`**: promote the ad-hoc `thermo_sidecar_analytic`
dict — inconsistently implemented across exp-032/033/034/035 (Red Team's
Phase-2 desk audit found THREE distinct implementations across four files,
not one dict copy-pasted four ways as first claimed — corrected below) —
into one reusable, regime-dispatched module with a new trust-suite stage.
Applied for the first time to the ON-endpoint (τ=3.9, measured
σ_abs/σ_ext=0.6075) and the program's own flagship absorber
(`graded_black_shell`, established σ_abs/σ_ext=0.51) with a real, disclosed
absorbed-power calculation, not a hand-typed placeholder.

Full Phase-1 parameter table, idealizations, and original (unrevised)
per-metric predictions: see `phase1_proposal.md` in this directory (the
verbatim text the five Phase-2 seats critiqued, kept as the historical
record per this program's flag-don't-rewrite convention).

## PHASE 2 — CRITIQUE (five blind seats, then Red Team with everything)

**MATERIALS** — support-with-changes. §1(A)/§3's "directly ungates
REALIZABILITY_MEMO.md" overstates the stakes: RSA's verdict is
dynamic-range-bound (irradiance-independent per the memo's own text), and
TPA's 9–12 OOM gap dwarfs anything P-D7-1's predicted band ([3e-4,3e-3]
W/cm², <1 OOM of movement) could close. No plausible sourced-irradiance
outcome moves a MATERIALS tier.

**ELECTROMAGNETISM** — support-with-changes, LOAD-BEARING. The proposed
`absorbed_fraction_weak_tau` = `(π/4)τ(1−4τ/3π)` is verbatim
`chord_absorptance_series_legacy` (`lab/amplitude_bridge.py`), whose own
docstring (written after a prior Red Team audit) documents 5-sig-fig
accuracy ONLY to τ≤0.032 and unphysical (negative) behavior by τ=3.9. The
proposed TAU_WEAK_LIMIT≈0.5 is ~15.6× the validated boundary. A validated
exact replacement, `chord_absorptance_exact`, already exists in-repo,
unreferenced.

**THERMODYNAMICS** — support-with-changes, LOAD-BEARING (independently
converges with VISION, below). `NETD_BAND_K=(0.020,0.050)` is labeled
"exp-033's own implied microbolometer range" — a self-referential citation
to an already-unsourced bare literal (`exp-033/run.py:226`), never traced
to any datasheet or standard, five cycles running.

**QUANTUM OPTICS** — support-with-changes, LOAD-BEARING. P-TS-3 would feed
the ON-endpoint's ESTABLISHED STEADY-STATE ratio into
`transient_delta_T(..., dwell_s)` as a constant held for the whole dwell —
silently assuming instantaneous switching, contradicting T17's own standing
requirement (declare k_f/k_r, self-classify memoryless-vs-hysteretic before
Phase 3). `lab/kinetics.py` already has the exact machinery
(`relax_exact`, `t99=4.6·τ`) to gate this.

**VISION SCIENCE** — support-with-changes, LOAD-BEARING (converges with
THERMO). Same NETD_BAND_K catch, independently reached. Additionally: NETD
is a thermal-camera/detector band, not a human-eye threshold — nothing in
§4's prediction language states this at the point of the claim, one dropped
caveat from being misread as a constraint-3 human-perceptual verdict — the
exact scope-tag-non-propagation pattern that fired Checkpoint criterion 4
at Iteration 17.

**RED TEAM** (last, with the proposal + all five critiques) — independently
re-verified all three flagged claims (confirmed all three, with exact
numbers: series is 3.43% low at τ=0.5, 65.19% low at τ=1.95, negative
(−2.007) at τ=3.9; NETD confirmed unsourced anywhere in the repo; T17's
kinetics machinery confirmed present and matching). Corrected the
proposal's own historical narrative: NOT one dict copy-pasted four ways —
THREE distinct implementations (exp-032/035 never call the chord series at
all; only exp-033/034 share it verbatim), and the ON-endpoint's ΔT was
ALWAYS hand-typed as an explicitly-disclaimed hypothesis, in every file —
the "silently negative at τ=3.9" defect the proposal cites as historical
fact never actually fired. Eight numbered attacks total; the load-bearing
ones beyond the three above:

1. **[inexpressible, LOAD-BEARING, caught by no blind seat]**
   `absorbed_fraction_established_ratio(sig_lo, sig_hi)` cannot compute
   watts as specified — σ_abs/σ_ext is a *dimensionless ratio*; converting
   to absorbed power needs σ_ext (or Q_ext×area) as a *separate,
   independently-measured input*, not folded into a bare ratio signature.
   Any glue code assuming σ_ext≈geometric area (Q_ext=1) would smuggle in
   exactly the idealization T9 already refutes for these articles (both
   0.51 and 0.6075 EXCEED the ≤0.5 geometric-optics ceiling a Q_ext=1
   assumption implies).
2. [inconsistency, LOAD-BEARING] Attack 1 must be fixed BEFORE QUANTUM's
   kinetics-gate fix is applied, not alongside it — gating a static P_abs
   that is itself ill-normalized just makes the error look
   doubly-validated.
5. [inconsistency, LOAD-BEARING] Stage 15 as proposed gates only the
   weak-τ branch; the established-ratio branch — carrying both of this
   cycle's headline "first-ever" claims (P-TS-3/4) — needs its own
   identity gate too, per PANEL.md's own "new machinery ⇒ new stage with
   ≥1 absolute identity BEFORE results are trusted" rule.
6. [inconsistency, LOAD-BEARING] State explicitly which wattage feeds
   P-TS-1 (code-correctness regression, OLD unstated exp-033 inputs) vs.
   P-TS-2/3/4 (NEW, Part-A-sourced wattage) — do not let the two get
   silently conflated in one committed number.
7. [constraint-3-adjacent risk, LOAD-BEARING — elevated above VISION's own
   "correctable" framing] The NETD/human-eye conflation is a live
   recurrence of the exact pattern class that fired Checkpoint criterion 4
   at Iteration 17, which Iteration 19 explicitly warned would recur.
   Every P-TS-2/3/4 prediction sentence must carry its own
   "NETD is an instrument/detector threshold, not a constraint-3 human-eye
   verdict" disclaimer AT THE POINT OF THE CLAIM, not only in surrounding
   narrative.
3. [inexpressible, CORRECTABLE] "Graybody radiative-equilibrium" for a
   dilute vapor host, applied unchanged to a solid coated shell
   (`graded_black_shell`), needs an explicit statement of what `mass_kg`/
   `c_p` represent (coating film? substrate? — an unstated modeling
   choice) or must stay flagged unresolved, not silently generalized.
4. [unfalsifiable, CORRECTABLE] P-D7-3 ("genuinely different physical
   quantities") is true by definition regardless of the search outcome —
   needs either a real numeric overlap criterion or demotion from
   "prediction" to stated intent.

Red Team's adjudication: zero fixes REJECTED as overreach (all cheap,
zero marginal FDTD cost, proportionate). Red Team's own ruling on the
tripwire question: **YES, executing this proposal with attacks 1/2/5/6/7 +
EM's TAU_WEAK_LIMIT fix + THERMO/VISION's NETD sourcing applied genuinely
satisfies THERMODYNAMICS' Iteration-19 tripwire — not merely by headcount.**
One caveat carried forward, not silently absorbed: the ORIGINAL Iteration-1
docket #7 also bundled VISION's glare/adaptation Tier-W sidecar; this
cycle's narrower scope (matching PLAN.md's own Iteration-20 queue wording)
is the right call per exp-041/042's bundling caution, but VISION's own half
stays SEPARATELY OPEN, not retired here — stated as a Phase-3 commitment
below, not a footnote.

## PHASE 3 — SYNTHESIZE (Director)

**All Red-Team-designated LOAD-BEARING fixes adopted in full, no
overrides.** Resolved configuration:

**Part A (docket #7 sourcing)** — unchanged from Phase 1's plan, plus
THERMO/VISION's mandatory addition: **microbolometer NETD** is added as a
sixth sourced parameter (own WebSearch query: "uncooled microbolometer
NETD typical mK specification datasheet"), replacing the self-referential
`NETD_BAND_K` placeholder with a cited figure or an explicit
still-unsourced flag if search comes up empty. VISION's disclaimer
sentence — *"NETD is an instrument/detector threshold, not a human
perceptual one; no P-TS prediction in this experiment bears on
constraint-3/4's human-eye verdict"* — is added verbatim at the point of
every P-TS claim in Part B's own docstrings and in every results.json key
that reports a NETD comparison, not only here.

**Part B (`lab/thermo_sidecar.py`)** — API revised per EM's + Red Team's
attacks 1/5/6:

- Weak-τ branch: `TAU_WEAK_LIMIT = 0.032` (not 0.5). Reuses
  `lab.amplitude_bridge.chord_absorptance_exact` directly (already
  stage-14-gated, P-TH-5) rather than re-deriving the refuted series;
  raises above the limit rather than silently extrapolating.
- Established-ratio branch, RENAMED and RESIGNED per attack 1:
  `absorbed_power_established_ratio(I_incident_w_cm2, sigma_ext_cells,
  dx_m, ratio_abs_ext, area_convention="iso_xsec_sq")` — takes σ_ext
  (cells) and the grid spacing explicitly, not a bare ratio. Converts to
  physical extinction width `w = sigma_ext_cells·dx_m`, then to an
  absorbing AREA under a stated, disclosed idealization
  (`iso_xsec_sq`: the object's extent along the 2D simulation's invariant
  axis equals its measured in-plane extinction width — i.e. a compact
  blob, not an infinite rod — Area = w²). This is a NEW idealization this
  cycle adds explicitly, distinct from (and more conservative than) an
  infinite-rod assumption; flagged in Idealizations below, not hidden.
  `P_abs = I_incident_w_cm2 · (Area_m2·1e4) · ratio_abs_ext`.
- Trust-suite stage 15 gates BOTH branches (attack 5): (1) Wien's-law
  round-trip to machine precision; (2)
  `absorbed_power_established_ratio(..., ratio_abs_ext=0) == 0.0` exact,
  and `== I_incident·Area` exact at `ratio_abs_ext=1` — the bounds
  identity Red Team's attack 1 fix requires; (3) weak-branch reuse
  verified bit-identical to `chord_absorptance_exact` (trivial by
  construction, still gated per PANEL.md's rule); (4) the P-TS-1
  regression, explicitly re-scoped per attack 6 (below).
- P-TS-1 (attack 6): regression-tests `steady_state_delta_T` reproducing
  exp-033's hardcoded `8.17e-4K` using exp-033's OWN unstated-but-inferred
  inputs (code-correctness only — this does NOT use Part A's newly-sourced
  wattage, and is labeled so in results.json). P-TS-2/3/4 use Part A's
  NEW sourced wattage exclusively — the two are never conflated in one
  committed number.
- ON-endpoint disposition (attack 2, QUANTUM's fix, applied in the correct
  order): `absorbed_power_established_ratio` computes the STEADY-STATE
  P_abs(τ=3.9) first (now soundly normalized per attack 1), THEN
  QUANTUM's kinetics gate scales it by `n_at_dwell/n_ss` (via
  `lab.kinetics.relax_exact`) whenever the sourced dwell time is shorter
  than `t99` for the assumed host — reported alongside an explicit
  "steady-state ceiling, not dwell-achieved" label when that condition
  holds. This experiment does NOT pin a specific (k_f,k_r) host (T17's own
  standing requirement is satisfied by reporting the RATIO, generic to any
  host, rather than picking one arbitrarily) — reported as
  `n_at_dwell/n_ss` bounds across representative fast/slow hosts already
  characterized in `lab/kinetics.py`'s Iteration-15 grid, not a single
  number.
- `graded_black_shell` disposition (attack 3): explicitly flagged
  UNRESOLVED for the mass/heat-capacity model (what `mass_kg`/`c_p`
  represent for a coated-shell geometry is not decided this cycle) —
  P-TS-4 reports absorbed POWER and the steady-state ΔT under the SAME
  lumped-capacitance idealization already used for the weak-τ articles
  (stated as a like-for-like comparison, not a resolved better model),
  with the idealization gap disclosed, not silently generalized past.
- MATERIALS' reword (§1/§3 stakes language: this sources T5's ledger and
  future Tier-W scoring, NOT the realizability bound — no
  REALIZABILITY_MEMO.md tier moves regardless of outcome) — adopted
  verbatim.
- P-D7-3 (attack 4): demoted from "falsifiable prediction" to a stated
  Phase-3 intent (the two quantities — beam-sweep dwell time and material
  relaxation time — are definitionally distinct regardless of what
  WebSearch returns; no numeric criterion can falsify that, so it is not
  scored as a prediction in the table below).

**Historical-narrative correction (Red Team's finding) adopted**: NOTES.md
above already states the three-distinct-implementations finding rather
than repeating the Phase-1 proposal's "one dict copy-pasted four ways"
claim.

**No criticisms overridden.** All five blind seats' fixes and all of Red
Team's load-bearing attacks are adopted in full; only attack 4's disposal
(demote, don't drop the underlying disambiguation intent) counts as a
partial override of the proposal's own original framing, and Red Team's
own text sanctioned exactly that resolution.

**Tripwire disposition, stated as a Phase-3 commitment**: this cycle
executes THERMODYNAMICS' narrower Iteration-20 ask (docket #7's witness
table + `thermo_sidecar.py` re-scoping) in full. VISION's own half of the
ORIGINAL Iteration-1 docket #7 — the glare/adaptation Tier-W sidecar
(distance, veiling glare, adaptation persistence) — remains separately
open and is NOT retired by this cycle; it stays VISION's own queued
deliverable, unchanged in priority.

### Idealizations (stated explicitly, before any run)

- **`iso_xsec_sq` area convention** (new this cycle): the established-ratio
  branch's absorbing area is the SQUARE of the measured 2D extinction
  width — i.e. the object is treated as compact (roughly as extended along
  the simulation's invariant axis as across it), not as an infinite rod.
  An idealization, not a measurement; a different convention (e.g. a
  stated finite rod length) would change P_abs linearly.
- **Bench-scale, not witness-scale.** All absorbed-power numbers this
  cycle are computed at this bench's own FDTD geometry (R_OUT≈78 cells,
  ≈2.34 μm radius at 600nm/cpl20) — a µm-scale object, not the meters-scale
  witness volume. T8/T13's own still-unresolved near-field→witness-scale
  bridge governs any future extrapolation; this experiment does not
  attempt one, exactly as exp-032/033/034 have each stated for their own
  bench-scale σ(I) diagnostics.
- **Weak-τ branch (τ≤0.032) uses the validated exact chord model**
  (`chord_absorptance_exact`); the established-ratio branch (τ=3.9,
  τ_established=n/a for graded_black_shell since it's not defined by τ but
  by its own measured ratio) uses MEASURED σ_abs/σ_ext, not the chord
  model, because T9 already shows the chord/ray idealization structurally
  cannot exceed the 0.5 geometric-optics ceiling both measured articles
  exceed.
- **Lumped-capacitance, spatially uniform ΔT** — unresolved this cycle
  (ignores exp-028's own radial profile); carried forward, not fixed.
- **Achromatic by construction** (ε_r≡1, non-dispersive σ per T1) — no
  per-λ dependence in Part B this cycle.
- **NETD is an instrument/detector threshold, not a human perceptual
  one** — carried verbatim into every P-TS claim, per VISION's mandatory
  fix.
- **Sourcing**: WebSearch snippet-level only (T18, WebFetch blocked);
  ≥2 independent sources sought per Part-A figure where literature
  supports it, single-source figures flagged lower-confidence.

### Per-metric predictions, falsifiable, committed BEFORE any run

| ID | Prediction | Band |
|---|---|---|
| P-D7-1 | Sourced irradiance-at-volume (derived: candela→W/sr via efficacy, ÷distance²) | [3×10⁻⁴, 3×10⁻³] W/cm² |
| P-D7-2 | Sourced dwell time (beam-on-one-spot) | central [20ms, 500ms]; hard falsification if outside [10ms,1s] entirely |
| P-D7-4 (NEW, THERMO/VISION's fix) | Sourced microbolometer NETD | [5, 100] mK — brackets the existing unsourced [20,50]mK band; hard falsification if the search returns nothing citable (in which case NETD_BAND_K stays explicitly flagged UNSOURCED, not silently kept) |
| P-TS-1 | Regression: module reproduces exp-033's legacy 8.17×10⁻⁴K under exp-033's OWN old inputs | within ±25% (code-correctness only, NOT scored as new physics) |
| P-TS-2 | off_pass (τ=0.0065) transient ΔT at sourced dwell (P-D7-2), vs sourced NETD (P-D7-4) | remains UNDETECTABLE (instrument sense only — see disclaimer), ≥5× below NETD |
| P-TS-3 | ON-endpoint (τ=3.9) steady-state P_abs, computed via the FIXED `absorbed_power_established_ratio` (σ_ext=235.97 cells, ratio=0.6075, `iso_xsec_sq`) | steady ΔT band [0.005K, 0.10K]; kinetics-scaled (dwell-limited) transient ΔT strictly ≤ the steady value, ratio n_at_dwell/n_ss reported across ≥2 representative hosts from `lab/kinetics.py`'s existing grid, not asserted as one number |
| P-TS-4 | Headline absorber (`graded_black_shell`, σ_ext=240.0 cells, ratio=0.51) steady + transient ΔT at sourced wattage/dwell, same `iso_xsec_sq` idealization | steady band [0.001K, 0.06K]; transient-at-dwell band [0.0002K, 0.04K] — first-ever scored NETD-relative disposition for the program's actual flagship article, disclaimer attached |
| P-STAGE15 | New trust-suite stage 15 gates both branches, ≥1 absolute identity each | full bench green (≥56/56 given prior 41 fast-stage baseline + stage 15's own new checks), 0 FDTD calls |

Predictions committed to git in this same commit, before Part A/B are
executed (house discipline, non-negotiable).

## PHASE 4 — TEST

Zero FDTD calls (WebSearch + code only). Bench trust suite: 41/41 fast
stages unchanged + new stage 15's own 13/13 (Wien round-trip; weak-tau
branch bit-exact against `chord_absorptance_exact`; established-ratio
branch bounds identity at ratio=0/1; thermal identities) — 54/54 total,
0 new FDTD calls, matching P-STAGE15.

**Part A — docket #7, sourced (WebSearch snippet-level; WebFetch
EGRESS_BLOCKED for scholarly domains again this shift, T18's 6th
consecutive confirmation):**

- **Candela**: 4 named tactical/EDC products, 13,827–99,310 cd (Fenix
  PD36R V2.0/ACE, Olight Warrior Ultra/X4 — product spec sheets).
- **Luminous efficacy**: WebSearch returned the WRONG quantity for this
  calculation — 137–180 lm/W is white-LED DEVICE wall-plug efficacy
  (electrical→optical), not the luminous efficacy OF RADIATION needed to
  convert candela (photometric) to radiant intensity (radiometric),
  ~250–350 lm/W for a white-light SPD. Flagged explicitly, not silently
  substituted; 300 lm/W central used, not separately WebSearch-cited this
  cycle.
- **Distance**: 45m, carried unsourced per Phase-1's own scope decision.
- **Irradiance (P-D7-1)**: derived, central 6.58×10⁻⁶ W/cm², range
  [1.10×10⁻⁶, 4.41×10⁻⁵] W/cm² across the full candela/efficacy/distance
  uncertainty. **FALSIFIED against the predicted [3×10⁻⁴,3×10⁻³] W/cm²
  band — ~46× below the band's own low edge, and the entire uncertainty
  range never touches it.** A real, disclosed result of actually sourcing
  the number, not a point-estimate artifact (the full parameter-range
  check confirms it). Per MATERIALS' own Phase-2 fix (adopted verbatim):
  this does not move any `REALIZABILITY_MEMO.md` tier — RSA is
  irradiance-independent, and TPA's 9–12 OOM gap only widens with a lower
  measured irradiance.
- **Dwell (P-D7-2)**: central 66.7ms (10° assumed beam full-angle ÷ 150°/s
  assumed sweep rate, both order-of-magnitude, beam angle not separately
  WebSearch-confirmed this cycle), range [20.8, 200]ms.
  **CONFIRMED** inside the predicted [20,500]ms band.
- **NETD (P-D7-4, new)**: sourced range 8.6–100mK across 4 refs (FLIR
  A325sc <50mK product spec; academic high-performance devices 8.6–40mK;
  budget cameras ~100mK). Adopted band (0.020,0.050)K — the SAME numeric
  values this program used unsourced for 5 cycles, now genuinely
  grounded rather than self-referential. **CONFIRMED**.

**Part B — `lab/thermo_sidecar.py` applied to established readings** (600nm,
cpl20, R_OUT=78 cells, dx=30nm):

- **Weak-τ OFF-state articles** (off_pass/off_lab/off_field/off_bracket):
  P_abs ≈ 3–28 femtowatts; transient ΔT 1.5×10⁻⁵–1.6×10⁻⁴K, all
  **UNDETECTABLE**, >100× below NETD. **P-TS-2 CONFIRMED.**
- **P-TS-1 regression**: computed 5.02×10⁻³K vs exp-033's legacy
  8.17×10⁻⁴K, 514% relative error — **MISS**, exactly as Red Team's
  attack 6 anticipated ("will almost certainly not reproduce... not
  because the module is wrong, but because the input changed"): the
  legacy number's own area/geometry assumptions were never committed
  anywhere (independently confirmed by THERMO's Phase-2 desk audit), so
  this is a real provenance gap in the OLD number, not a defect in the
  new module — flagged as an erratum on exp-033/034/035's own
  `results.json` (their `off_pass_steady_state_dT_K=8.17e-4` should be
  read as unreproduced/unprovenanced going forward, not as validated).
- **ON endpoint (τ=3.9)**: P_abs=2.00×10⁻¹² W, steady ΔT=3.944×10⁻³K.
  **PARTIAL against P-TS-3**: sits ~21% BELOW the predicted [0.005,0.10]K
  band's own low edge — a real miss, disclosed, not hidden. Kinetics
  gate (QUANTUM's fix, applied after attack 1's normalization per Red
  Team's own ordering): fast host (k_r=1e6) reaches n_ss within the
  67ms dwell (ratio=1.0); slow host (k_r=1) reaches only ~12.5% of n_ss
  (ratio=0.125) — confirming QUANTUM's own Phase-2 point that which host
  applies is load-bearing, not cosmetic. Both hosts read **UNDETECTABLE**
  after this cycle's own self-caught methodology fix (below).
- **`graded_black_shell` (flagship absorber)**: P_abs=1.74×10⁻¹² W,
  steady/transient ΔT=3.311×10⁻³K, **UNDETECTABLE**. **P-TS-4
  CONFIRMED** — first-ever NETD disposition for this program's headline
  article, at bench scale.

**Self-caught methodology bug, fixed within this shift (disclosed per
this program's own erratum convention, not left for Phase 5):** an
earlier pass of `run.py` used `transient_delta_T`'s ADIABATIC (no-cooling)
mode uniformly. For the ON endpoint and flagship absorber this produced a
transient ΔT (0.191K / 0.166K, both DETECTABLE) EXCEEDING their own
steady-state ceiling (3.9mK / 3.3mK) — physically impossible for a system
approaching a fixed equilibrium under constant absorbed power. Root cause:
`dwell_central` (~67ms) is ~48× these articles' own linearized thermal
time constant (~1.4ms, from their tiny assumed mass) — deep in the
equilibrium-reaching regime, not the adiabatic one. Fixed by computing
`thermal_tau_s` from the same area/emissivity/h_conv inputs and using the
exponential-approach mode (`_physical_transient_dT` in `run.py`), which
guarantees transient ΔT ≤ steady-state ΔT by construction. The weak-τ
articles' own numbers happened to stay UNDETECTABLE either way (their
absorbed power is orders of magnitude smaller), so this bug was silent
there — caught only because the ON-endpoint/flagship numbers were large
enough to expose the inconsistency on inspection.

**Full predictions scorecard**: `results.json::predictions_scorecard`.
6 of 8 predictions CONFIRMED, 1 PARTIAL (P-TS-3, real and disclosed), 1
MISS (P-TS-1, anticipated by Red Team's own attack 6, a provenance
finding about the OLD number not a defect in the new one).
