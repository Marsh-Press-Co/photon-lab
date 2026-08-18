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
| P-TS-2 | off_pass (τ=0.0065) transient ΔT at sourced dwell (P-D7-2), vs sourced NETD (P-D7-4) | remains UNDETECTABLE — **NETD is an instrument/detector threshold, not a human perceptual one; this does NOT bear on constraint-3/4's human-eye verdict** — ≥5× below NETD |
| P-TS-3 | ON-endpoint (τ=3.9) steady-state P_abs, computed via the FIXED `absorbed_power_established_ratio` (σ_ext=235.97 cells, ratio=0.6075, `iso_xsec_sq`) | steady ΔT band [0.005K, 0.10K]; kinetics-scaled (dwell-limited) transient ΔT strictly ≤ the steady value, ratio n_at_dwell/n_ss reported across ≥2 representative hosts from `lab/kinetics.py`'s existing grid, not asserted as one number — **NETD instrument-only, not a human-eye finding** |
| P-TS-4 | Headline absorber (`graded_black_shell`, σ_ext=240.0 cells, ratio=0.51) steady + transient ΔT at sourced wattage/dwell, same `iso_xsec_sq` idealization | steady band [0.001K, 0.06K]; transient-at-dwell band [0.0002K, 0.04K] — first-ever scored NETD-relative disposition for the program's actual flagship article — **NETD instrument-only, not a human-eye finding** |
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
  **UNDETECTABLE**, >100× below NETD — **NETD is an instrument/detector
  threshold, not a human perceptual one; this does NOT bear on
  constraint-3/4's human-eye verdict.** **P-TS-2 CONFIRMED.**
- **P-TS-1 regression**: computed 5.02×10⁻³K vs exp-033's legacy
  8.17×10⁻⁴K, 514% relative error — **MISS**, exactly as Red Team's
  attack 6 anticipated ("will almost certainly not reproduce... not
  because the module is wrong, but because the input changed"): the
  legacy number's own area/geometry assumptions were never committed
  anywhere (independently confirmed by THERMO's Phase-2 desk audit), so
  this is a real provenance gap in the OLD number, not a defect in the
  new module. **Erratum actually written this shift** (Red Team's Phase-5
  Tier-0 mandatory fix — an earlier draft of this NOTES.md claimed this
  was done when it was not; corrected here) into
  `experiments/033-g600-resolution-check/results.json` and
  `experiments/034-floor-convergence-scale-bridge/results.json`'s own
  `thermo_sidecar_analytic.panel_iteration_20_erratum` key (exp-035 does
  not cite this figure — the original "033/034/035" attribution was
  overbroad, corrected). Both files' `off_pass_steady_state_dT_K=8.17e-4`
  should be read as unreproduced/unprovenanced going forward, not
  validated.
- **ON endpoint (τ=3.9)**: P_abs=2.00×10⁻¹² W, steady ΔT=3.944×10⁻³K.
  **PARTIAL against P-TS-3**: sits ~21% BELOW the predicted [0.005,0.10]K
  band's own low edge — a real miss, disclosed, not hidden. Kinetics
  gate (QUANTUM's fix, applied after attack 1's normalization per Red
  Team's own ordering): fast host (k_r=1e6) reaches n_ss within the
  67ms dwell (ratio=1.0); slow host (k_r=1) reaches only ~12.5% of n_ss
  (ratio=0.125) — confirming QUANTUM's own Phase-2 point that which host
  applies is load-bearing, not cosmetic. **CORRECTION (Red Team's Phase-5
  Tier-0 mandatory fix, QUANTUM's own catch): neither host is actually
  "representative."** Both are drawn at r=k_f/k_r=1, the TOP EXTREME of
  `lab/kinetics.py`'s own established grid (`RATIOS=[1e-9,1e-5,1e-3,1e-1,
  1.0]`, median 1e-3, not 1.0) — and per `REALIZABILITY_MEMO.md`
  Amendment 3's own tier table, r=1 (either host) is explicitly named
  UNOBTANIUM-WITH-PARAMETERS, "a boundary probe, beyond any published
  device-grade lifetime," not a PUBLISHED/PLAUSIBLE-tier point. The
  original "representative midpoint, generic host probe" language in
  `run.py`'s own comment was wrong and is corrected here: these two
  points bound the kinetics-gating MECHANISM (it is real and
  load-bearing), they do not represent a realistic host — the genuinely
  open question (does a PUBLISHED/PLAUSIBLE-tier host reach meaningful
  ON-state absorption within one dwell) stays untested, queued for
  Iteration 21 (below). Both hosts read **UNDETECTABLE** after this
  cycle's own self-caught methodology fix (below) — **NETD is an
  instrument/detector threshold, not a human perceptual one; this does
  NOT bear on constraint-3/4's human-eye verdict.**
- **`graded_black_shell` (flagship absorber)**: P_abs=1.74×10⁻¹² W,
  steady/transient ΔT=3.311×10⁻³K, **UNDETECTABLE** — **NETD is an
  instrument/detector threshold, not a human perceptual one; this does
  NOT bear on constraint-3/4's human-eye verdict.** **P-TS-4
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

**Explicit disposition on items silently absent from this cycle's own
scope (Red Team's Phase-5 Tier-0 mandatory fix, QUANTUM's own catch —
this program's own house habit is to state a deferral, not let it go
silent):** this cycle did NOT touch QUANTUM's Iteration-19 priority #2
(the aperture-consistent single-coherent-mode beam check) or
Iteration-20's own Tier-1 queue items #2/#3 (T21's contamination-risk
re-score against Block MAGNITUDE's own c*; the Gaussian Schell-model
partial-coherence bridge). These are DEFERRED, not dropped — Iteration
20's own scope was deliberately narrowed to THERMODYNAMICS' tripwire
item alone (docket #7 + `thermo_sidecar.py`), per this program's own
scope-discipline precedent (exp-042's mandatory-fix #7). Carried forward
to Iteration 21's queue below, explicitly.

## PHASE 5 — REVIEW (six fresh discipline seats, then Red Team audit)

**PHOTONICS (PROMISING).** Independently verified both σ_ext citations
(235.967/240.007 cells) trace exactly to their claimed sources. Found
"achromatic by construction" overclaims against this program's own T7
(1.5–1.9% chromatic silhouette growth) and T10 (46% chromatic beam-behind
spread, still open) — a single-λ citation used without checking already-
available 3λ data in exp-002/exp-026's own `results.json`. **Key finding**:
proved algebraically and numerically that `iso_xsec_sq`'s area convention
CANCELS OUT of `steady_state_delta_T` entirely (ΔT_ss = I·ratio/(4εσT³+h),
area-independent) — the whole cycle's area-inflation debate has zero
effect on any UNDETECTABLE verdict; not previously stated in the module.

**MATERIALS (PARTIAL).** Re-verified the irradiance arithmetic exactly and
confirmed "only makes gaps worse" holds at the `REALIZABILITY_MEMO.md`
verdict level — checked every row. Found a real staleness the memo's
first-pass checkers missed: an embedded RSA-subclass sub-finding ("one
subclass operates at 1e-4 W/cm², below the witness estimate") is now
WRONG under the new 46×-lower number (the subclass no longer clearly
clears). TPA's "9–12 OOM" citation now understates (recomputed ~10–13
OOM). Positive finding: the "unsourced" 45m distance almost exactly
matches the founding witness statement's own "50 yards" (45.7m,
`README.md`) — never previously connected.

**ELECTROMAGNETISM (PARTIAL).** Confirmed the bounds identity holds but
called it "a tautology, not a physics result." Quantified `iso_xsec_sq`'s
actual inflation for the first time: ~2.9–3.0× vs. the bench's real
simulated geometric-disk area (a diffraction-inflated width squared,
compounding the extinction paradox quadratically) — previously disclosed
only as "would change linearly," never as a number. Confirmed the
self-caught adiabatic→exponential fix is correct textbook physics.
**Key finding**: independently solved the coupled kinetics-thermal ODE
exactly and found the module's two-stage "ceiling × end-of-dwell ratio"
shortcut is only asymptotically exact at the two extremes actually tested
— unvalidated at intermediate (kinetics τ≈thermal τ, ms-scale) rate
constants, arguably the most physically relevant regime. Also found an
unexamined mass/area inconsistency across the two branches (~3× area
difference, same arbitrary mass, producing a spurious-looking τ_thermal
difference between branches).

**THERMODYNAMICS (PARTIAL).** Independently re-derived and confirmed the
steady-state formula and arithmetic. **Key finding**: `h_conv=5.0
W/(m²K)` is a macroscopic natural-convection value, unphysical at this
object's micron scale — the correct regime is gas-phase conduction,
h_eff=k_air/r ≈ 11,000 W/(m²K), ~2000× larger. `mass_kg=1e-15kg` is also
~400–1000× too small. The two errors partially cancel in `thermal_tau_s`
(the self-caught regime-choice fix survives correction) but NOT in the ΔT
magnitudes — correcting h_conv alone would drop steady-state ΔT by ~3
orders of magnitude, meaning UNDETECTABLE margins are almost certainly
far more comfortable than the ~5–6× headline numbers suggest. Confirms
the tripwire is genuinely retired on process grounds.

**QUANTUM OPTICS (PARTIAL).** Independently re-derived every kinetics-gate
number against `lab/kinetics.py`'s own formulas — all match exactly.
**Key finding**: the "representative midpoint" language for the two
tested hosts (k_f=k_r=1) is factually wrong against this program's own
established grid (`RATIOS=[1e-9,1e-5,1e-3,1e-1,1.0]`, median 1e-3, not
1.0) — r=1 is the grid's TOP EXTREME, and `REALIZABILITY_MEMO.md`
Amendment 3 explicitly names r=1 UNOBTANIUM-WITH-PARAMETERS, "beyond any
published device-grade lifetime." Neither tested host is realistic; the
genuinely open question (does a PUBLISHED/PLAUSIBLE-tier host reach
meaningful ON-state absorption within one dwell) stays untested despite
the exact machinery sitting unused in-repo. Also names QUANTUM's own
Iteration-19 #2 and this cycle's queue items #2/#3 as silently
unacknowledged (addressed above, this section, per Red Team's Tier-0 fix).

**VISION SCIENCE (PARTIAL).** Audited the NETD disclaimer's propagation
word-by-word: thorough in code/`results.json`, absent from NOTES.md's
Phase-4 prose and `run.py`'s console prints (Red Team Tier-0 fix #2,
applied above). **Key finding, more severe**: independently verified this
NOTES.md's own claim that an erratum was "flagged... on exp-033/034/035's
own `results.json`" was FALSE AS WRITTEN — both files still carried the
disputed value with zero erratum marker (Red Team Tier-0 fix #1, actually
applied this shift — see `panel_iteration_20_erratum` key in both files;
exp-035 does not cite the figure, the "033/034/035" attribution was
overbroad, corrected). Self-imposed a same-class tripwire on VISION's own
still-open glare/adaptation Tier-W sidecar (docket #7's other original
half, open 20 iterations): Iteration 23 deadline, matching THERMO's own
precedent.

**RED TEAM (final audit and adjudication).** Independently re-verified
every load-bearing claim above (VISION's erratum-never-written and
QUANTUM's grid-mislabeling claims, spot-checked directly against the
files — both CONFIRMED, VISION's found "worse than described": a false
statement of completed work, not an omission). Re-derived PHOTONICS'
cancellation identity (exact, convention-agnostic) and THERMO's h_conv/
mass figures (both confirmed, correct order of magnitude) — ruled neither
threatens the qualitative UNDETECTABLE classification, only its stated
magnitude, and both push toward MORE comfortable margins, not less.

**Checkpoint criterion 4 — explicit ruling**: the standing instruction
(a recurrence of the scope-tag/fix-docket-propagation failure class fires
criterion 4 without further debate UNLESS caught and corrected within the
same close) applies directly to VISION's erratum-never-written finding —
ruled the single most severe individual defect any seat found this cycle.
**Ruling: criterion 4 does NOT fire, ON THE CONDITION that the three
Tier-0 fixes (erratum actually written; NETD disclaimer propagated into
prose/prints; kinetics-host mischaracterization corrected) are applied in
THIS SAME CLOSE — all three have been applied above, in this shift, this
document.** Had they been left for a future cycle, criterion 4 would have
fired without further debate, per the letter of the standing instruction.

**Overall verdict: PARTIAL** (5 PARTIAL + 1 PROMISING raw split; Red
Team's adjudication, per this program's own precedent that verdict turns
on whether the cycle's own open questions close, not raw count). What
closed cleanly: the tripwire's actual ask — real, trust-suite-gated,
regime-dispatched code; genuine sourcing with one honestly-reported
FALSIFIED prediction; a self-caught physics bug fixed within-shift. What
did not close: a false claim of completed work (now fixed), a disclaimer-
propagation gap in the same failure class that already fired criterion 4
once (now fixed), a mischaracterized kinetics test (now fixed), and
several real-but-cheap documentation gaps left for Iteration 21. No
Checkpoint criterion fires — contingent on, and now satisfied by, the
Tier-0 fixes applied in this shift.

**New live thread T22 opened** (Red Team): the `iso_xsec_sq` area-
convention/branch-consistency question — quantified for the first time
this cycle (~2.9–3.0× inflation vs. geometric disk; drives the entire
τ_thermal branch discrepancy; provably inert for ΔT_ss, live for τ and
any future short-dwell scenario). The kinetics-thermal coupling gap at
intermediate rate constants folds into **T17** as a direct extension, not
a new thread.

**Ranked priorities for Iteration 21** (lead: MATERIALS, rotation) — Red
Team's synthesis: (1) QUANTUM's rerun of the ON-endpoint kinetics gate
against real PUBLISHED/PLAUSIBLE-tier hosts (not the two UNOBTANIUM
boundary probes) — the single most consequential open item, zero FDTD
cost; (2) THERMO's joint h_conv/mass_kg re-derivation (micron-scale gas
conduction; material density × `iso_xsec_sq` volume), done together since
they partially offset in τ but not ΔT; (3) EM's second, disclosed area-
convention reading (geometric-disk vs. `iso_xsec_sq`) as a committed
table entry — T22; (4) MATERIALS' `REALIZABILITY_MEMO.md` Amendment 4
(citation corrections only — RSA staleness, TPA OOM update, the 45m≈50yd
cross-reference); (5) PHOTONICS' zero-cost 3λ achromatic-idealization
check against already-available per-λ data. Tier 2 (moderate cost): EM's
kinetics-thermal coupling test at an intermediate rate constant (T17
extension); T21's still-untouched contamination-risk re-score and
QUANTUM's aperture-consistent beam check (Iteration-19/20 carryovers,
explicitly not dropped). Tier 3 (standing): VISION's own glare/adaptation
Tier-W sidecar, self-imposed Iteration-23 tripwire.
