# exp-105 — The T8 r=78/156/312 Bridge, Extended to the Coherent Point/Region-Intensity Channel

**Panel Iteration 82. Lead seat (rotation): THERMODYNAMICS. Director:
Clyde (photonlab-shift, cloud panel shift).** Executes exp-104's own
Reconciled Iteration-82 queue, Tier 1 item 1 (Red Team's own consensus
top pick, "now unblocked by this cycle's clean [P2] null"). Instrument-
extension cycle, diagnostic only — T1: N/A, zero `lab/` diff, no
mechanism proposed or varied.

Full record: `phase1_proposal.md` (THERMODYNAMICS), `phase2_critique_
{photonics,materials,em,quantum,vision}.md` (five blind critiques, all
support-with-changes), `phase2_redteam_audit.md` (9 numbered attacks,
all 5 flip conditions ADOPTED in full — zero overridden — plus 3 new
Red-Team-only findings, verdict PROCEED-WITH-MANDATORY-FIXES).

## Hypothesis

T8 (exp-030, Iteration 7) established a self-similar r=78/156/312
near-field-to-witness-scale scaling methodology for the ambient
Weber-contrast instrument, returning a genuinely mixed result (the
absorber's shape-law failed both candidate power laws; PEC reversed
non-monotonically). That bridge has never touched the newer coherent,
phase-resolved point/region-intensity channel (`kappa_window`,
`kappa_region_wide`, `kappa_region_point`, `delta_phi`) built at
exp-102/103/104, hardened this very last cycle by a clean, genuinely
sub-Nyquist ripple null (exp-104's P2 FALSIFIED). Hypothesis: applying
T8's own formula chain (self-similar scaling by κ=r/78, the mandatory
`sigma_max(κ)=0.5/κ` optical-depth-preserving fix) to this channel will
show whether its own scale-dependence resembles T8's original mixed
finding or behaves differently, and will produce a first, disclosed
data point on whether that null generalizes across scale — bearing,
without resolving, on the still-open T13 thread (the C_∞-asymptote-vs-
witness-|C| mismatch).

## Setup

Full geometry/cost derivation: `phase1_proposal.md` §2 (Phase-1 draft) as
corrected by `phase2_redteam_audit.md` §5 (9 numbered fixes, all
adopted). Every geometric constant is computed by `run.py::geom(r)`,
never hand-typed — this file states the DESIGN, not fresh arithmetic
(R4 discipline).

- **r-family formula chain** (T8's own, `experiments/030-.../design_
  geometry.py::beam_geometry(r)`, re-derived): `κ(r)=r/78`; `N(r)=
  round(560κ)`; `CX(r)=round(252κ)`; `CY(r)=round(280κ)`; `SRC_X(r)=
  round(64κ)`; `STEPS(r)=round(3200κ)`; `ABSORB=EDGE=TAPER=40` fixed
  (exp-103's own corrected, cpl=20-calibrated value); `R_CORE(r)=
  round(30κ)`; `R_COAT(r)=r`; `sigma_max(r)=0.5/κ` (T8's own mandatory
  optical-depth-preserving fix, independently cross-validated at κ=2
  against the R4 family's own independently-built `SIGMA_R4_CORRECTED
  =0.25`, `experiments/069-.../design_geometry.py`).
- **Window/standoff anchor** — re-parameterized to the object's own
  physical surface (`R_COAT`), not the legacy `R_CLK` constant
  exp-103/104 inherited (algebraically identical at r=78, T10/SIGMA_ON-
  erratum-avoidance discipline): `BEHIND` window = `(CX+R_COAT+27,
  CX+R_COAT+127, CY-20, CY+20)`; `DENSE_X` = 53 points, 2-cell pitch,
  `[CX+R_COAT+22, CX+R_COAT+126]` — offset FIXED in cells across r (T8's
  own `PLANE_DX`-fixed convention), reproducing exp-103/104's own values
  bit-exact at κ=1 (Gate P0).
- **Channel machinery**: `kappa_window` (window-box mean-intensity
  ratio, exp-103's own formula), `kappa_region_wide`/`kappa_region_
  point`/`delta_phi_wide`/`delta_phi_point` (exp-102/103/104's own
  formulas, byte-for-byte reused), `H_REGION_WIDE=5`, `H_REGION_POINT=0`,
  `FLOOR_FRAC=0.10` — unchanged at every r.
- **Fresnel/Nyquist pre-check (mandatory fix 4, QUANTUM)**:
  `predicted_ripple_period(r) = λ_cells·D_eff/r` (D_eff=77 cells fixed,
  the window's own offset midpoint), gating whether `DENSE_PITCH=2`
  cells stays genuinely sub-Nyquist at each r via `nyquist_margin(r) =
  predicted_ripple_period(r)/(2·DENSE_PITCH)`: TRUSTED (≥2.0) / MARGINAL
  (1.0–2.0) / UNRESOLVED-BY-CONSTRUCTION (<1.0). `z_over_zr(r) =
  D_eff·λ_cells/r²` computed the same way — corrects the Phase-1
  proposal's own doubly-wrong hand-typed figure (Red Team attacks 1/2;
  see phase2_redteam_audit.md §0.1).
- **r=78: 0 new FDTD calls.** `kappa_window` reused from exp-103's own
  established `results.json::kappa_window.value` (0.018336958179764707);
  `kappa_region_wide/point`/`delta_phi` reused from exp-104's own
  committed `results.json`. **Gate P1, RESCOPED (mandatory fix 3, Red
  Team's own finding)**: this is a data-loading/transcription
  self-consistency check on exp-104's own already-computed scalars —
  NOT an independent cross-run physics-reproducibility test the way
  exp-104's own Gate P1 (built on a fresh `Sim.run()` capture) was; the
  distinction is stated explicitly wherever Gate P1 is reported.
- **r=156: 2 primary calls (empty+article, θ=0°, STEPS=6400)
  unconditionally committed**, PLUS **2 settling-independence calls at
  doubled STEPS=12800 on `kappa_region_point`/`delta_phi_point`
  SPECIFICALLY (mandatory fix 3, EM's own finding)** — exp-103's own
  settling leg (`STABILITY_TOL=0.20`) checked only the wide-box channel;
  this program has never settling-checked the zero-averaging point
  channel P4 depends on, at any r. Tolerance: 20% relative on
  `kappa_region_point`, 0.20 rad absolute on `delta_phi_point`, both
  gating P4's r=156 verdict jointly with the Nyquist-margin gate.
- **r=312: cost-gated, T8's own Iteration-7 precedent applied
  explicitly** (that leg overran its own hand estimate by ≈8×). Pilot:
  the empty-scene call alone, timed; proceed to the article-scene call
  only if the pilot is under 90 minutes AND the projected 2-call total
  is under 180 minutes; otherwise report r=312 as cost-deferred, not
  attempted, queued for a future cycle. No settling leg is run at r=312
  this cycle regardless (disclosed idealization, Next item).
- **THERMODYNAMICS sidecar: INVOKED this cycle** (departure from
  exp-102/103/104's own N/A precedent — genuinely varying `r_out`
  changes the thermal chain's `l_geometric_m` argument directly).
  Analytic model (`lab.thermo_sidecar.mixed_length_scale_regime`,
  already-gated, trust-suite stage 18): gas-conduction loss dominates
  radiative loss by ~3 orders of magnitude across this entire family, so
  `ΔT_ss(r) ∝ r_out` roughly linearly under a `Q_ext`-invariance
  placeholder for `σ_ext(r)`. **Realizability/diffraction-inflation
  caveat, restated inline (mandatory fix 6, MATERIALS)**: the
  `σ_ext(78)=240.007…` anchor this placeholder depends on is exp-057's
  own "ASSERTED, NOT INDEPENDENTLY BOUNDED" diffraction-inflated optical
  width (~1.54× the object's true geometric diameter), not an
  independent measurement — `graded_black_shell` stays UNOBTANIUM-WITH-
  PARAMETERS at every r. **Scored claims only (mandatory fix 9, Red
  Team's own reframing)**: the illustrative numeric margin bands are
  demoted to descriptive context; the two SCORED falsifiable claims are
  (a) NETD classification stays UNDETECTABLE at every committed r, and
  (b) the margin trend is monotonically non-increasing with κ.

## T1 escape-route statement

**N/A — instrumentation/diagnostic work**, exactly as T8's own founding
cycle and exp-102/103/104 were. No σ(I)/σ(x,t)/angular-selectivity
machinery is built or varied. Constraint-3/4 perceptual scoring is
explicitly NOT performed this cycle — the `DISCLAIMER` (extended per
mandatory fix 9/VISION to name the NETD classification explicitly as an
instrument/detector threshold, not a human-perceptual one, reusing
`thermo_sidecar.netd_disposition()`'s own disclaimer string verbatim) is
asserted present in both `PREDICTIONS_TEXT` and `RESULT_TEXT` (R23
pattern).

## Idealizations

- 2D TMz, single λ=600nm/cpl=20 scope, unchanged from exp-102/103/104.
- θ=0° only (normal incidence), not extended to an oblique-angle sweep
  this cycle — cost and apples-to-apples reasons stated in full in
  `phase1_proposal.md` §5; an oblique-angle extension of this same
  θ=0°-validated bridge is named as a Next item, not silently dropped.
- No settling-independence leg at r=312 this cycle, even if r=312 is
  committed — a genuine, disclosed scope reduction (Next item), distinct
  from the r=156 settling leg this cycle DOES commit.
- `graded_black_shell` remains UNOBTANIUM-WITH-PARAMETERS at every r —
  self-similar r=156/312 constructions are LARGER absolute idealized
  coatings, not more realizable ones (exp-030's own Iteration-7
  precedent: real CNT-black realizability follows the OPPOSITE,
  fixed-absolute-thickness scaling law).
- The thermal sidecar's `σ_ext(r)` values for r=156/312 are an
  ANALYTIC `Q_ext`-invariance placeholder, not a measured
  `sections.widths()` box-ledger reading — a real measurement (zero
  marginal FDTD cost, reusing this cycle's own captured fields) is
  named as a Next item, not committed this cycle.
- No witness-scale extrapolation is attempted or claimed this cycle —
  this is a bench-scale scale-robustness/generalization check only,
  exactly as T8's own Block 1 was for the ambient channel.
- `lab/` diff: zero.

## Predictions (frozen BEFORE any FDTD call — house discipline)

Verbatim from `run.py::build_predictions_text()` (generated by code, not
hand-typed, R23/R4 discipline) — printed in full by `run.py
--predictions-only`, reproduced here for the record at freeze time:

- **Gate P0** (ground-truth recovery, zero cost): `geom(78)` reproduces
  exp-103/104's own established constants exactly. Falsified by any
  mismatch → halt.
- **Gate P1** (r=78, RESCOPED self-consistency check): <1e-9 relative
  deviation on the reused scalars. Falsified → halt.
- **Fresnel/Nyquist pre-check** (zero cost): r=78 nyquist_margin=4.936
  (TRUSTED); r=156 nyquist_margin=2.468 (TRUSTED); r=312
  nyquist_margin=1.234 (MARGINAL-REDUCED-CONFIDENCE). `z_over_zr`: r=78
  =0.253123, r=156=0.063281, r=312=0.015820.
- **P2** (monotonicity): `kappa_window(r)` decreases monotonically with
  r. Predicted CONFIRMED.
- **P3** (functional-form + shape discriminator, full form requires
  r=312): pre-registered prior — T8's own r=78/156/312 bridge already
  found this exact discriminator REFUTED for `graded_black_shell` on the
  ambient channel (ratio 5.33, outside both the 2.00±0.3 and 4.00±0.5
  bands). A miss here would replicate, not contradict, established
  history. If r=312 is cost-deferred, only the qualitative single-step
  (78→156) direction is reported, explicitly not scored.
- **P4** (sub-Nyquist ripple generalization, GATED by both the
  Nyquist-margin pre-check and the new point-channel settling leg):
  predicted P2-analog FALSIFIED again at r=156 (extending exp-104's
  clean r=78 null) IF AND ONLY IF the settling leg passes (≤20%
  relative on κ, ≤0.20 rad on Δφ) AND the r=156 Nyquist margin clears
  TRUSTED (it does, 2.468, per the pre-check above). If the settling
  leg fails, the verdict is reported but flagged NOT-TRUSTED, not
  silently scored as clean.
- **P5** (thermal sidecar): scored claims only — (a) NETD classification
  stays UNDETECTABLE at every committed r; (b) margin trend
  monotonically non-increasing with κ. Illustrative numeric bands are
  descriptive context only, not scored (Red Team's own reframing,
  mandatory fix 9).

## Panel record

**Phase 1** (THERMODYNAMICS, lead seat by rotation): `phase1_proposal.md`.
**Phase 2**: five blind critiques, all support-with-changes
(`phase2_critique_{photonics,materials,em,quantum,vision}.md`) — three
independently caught the same 10× `z_over_zr` arithmetic error
(PHOTONICS, EM, QUANTUM); MATERIALS flagged the thermal sidecar's
Q_ext-anchor realizability caveat; EM flagged the missing point-channel
settling check; QUANTUM flagged the Fresnel-number/DENSE_PITCH scaling
risk for P4; VISION flagged the R23 disclaimer-scope gap for the newly-
live NETD channel. **Red Team's Phase-2 audit** (`phase2_redteam_
audit.md`): PROCEED-WITH-MANDATORY-FIXES, all five flip conditions
ADOPTED in full (none overridden), three new Red-Team-only findings (the
`z_over_zr` range bracket is a THIRD, independently-wrong figure, not
scatter around the known 10× error; Gate P1's actual narrower scope for
the reused r=78 leg; P5's own numeric bands were self-disclaimed as
non-binding, a real gap against PANEL.md's falsifiable-band requirement).
Checkpoint criterion 4 ruled explicitly NOT close to firing (T1:N/A
instrumentation, constraint 3 disclaimed by name in three sections, every
defect caught blind at Phase 2 before any freeze) — flagged forward as a
standing caution given this exact T28 sub-thread's four-instance
disclaimer-erosion history (the Iteration-65 CHECKPOINT firing on this
identical NETD/thermal-sidecar channel): the DISCLAIMER extension must
survive into Phase 4/5 Result prose, not merely fix Phase-3 wording, or a
fifth instance would be a much sharper firing candidate.

**Phase 3 (this synthesis, Director).** All 8 of Red Team's must-land
items adopted in full, zero overridden — every one independently
re-verified as cheap and load-bearing, and none required abandoning the
cycle's own disclosed scope or budget:

1. `z_over_zr`/`predicted_ripple_period` computed by `geom()`, printed,
   never hand-typed again.
2. (folded into 1 — the Grounding Note's own "every constant computed"
   claim is restored, not merely patched.)
3. New settling-independence leg on `kappa_region_point`/`delta_phi_
   point` specifically, at r=156, gating P4's verdict there.
4. Fresnel-forced `predicted_ripple_period`/`nyquist_margin` computed
   per r, gating P4's trust tier (TRUSTED/MARGINAL/UNRESOLVED).
5. `DISCLAIMER` extended to name the NETD classification explicitly,
   sourced from `thermo_sidecar.netd_disposition()`'s own string.
6. MATERIALS' Q_ext-invariance/diffraction-inflation caveat restated
   inline, immediately before the thermal table.
7. T8's own P-VISION-1b REFUTED-for-both-articles result pre-registered
   as prior information in P3's own prediction text.
8. Gate P1 explicitly rescoped for the reused r=78 leg (data-loading
   self-consistency check, not an independent physics reproduction).
9. (Recommended) P5's illustrative numeric bands demoted to descriptive
   context; only the classification-stays-UNDETECTABLE and margin-
   monotonic-decline claims are scored.

No criticism was overridden — all nine items (the five seats' flip
conditions plus Red Team's own three additional findings) were
independently re-derived from primitives by Red Team before this
synthesis, and every one is a cheap, mechanical, zero-to-low-marginal-
cost fix that leaves the cycle's own disclosed r=156-unconditional/
r=312-cost-gated scope and budget unchanged.

`run.py` implements all 9 fixes; `geom()`/Gate P0/Gate P1 logic was
independently dry-run-verified against exp-103/104's own committed
`results.json` files before predictions were frozen (Gate P0 PASS, Gate
P1 max_rel=0.0 PASS, Fresnel/Nyquist tiers as stated above) — this
dry-run touches zero FDTD machinery and is disclosed here as a
pre-freeze code-correctness check, not a result.

Predictions frozen and committed to git in this same commit, strictly
BEFORE `run.py`'s first `Sim.run()` call, per house discipline.
