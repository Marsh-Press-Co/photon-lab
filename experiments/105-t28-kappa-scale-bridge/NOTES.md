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

## Result

**6 real FDTD calls, 3883.3s (64.72 min) wall time, zero `lab/` diff
throughout.** r=312's cost-gated pilot (empty scene alone) came in at
1867.5s (31.13 min, well under the 90-min abort threshold), so the full
r=312 leg was committed and executed — better than the worst case the
Phase-1 proposal's own cost model disclosed (up to 7.1h).

**Gate P0: PASS.** **Gate P1 (r=78, rescoped self-consistency check):
PASS**, max_rel=0.000e+00. **Fresnel/Nyquist pre-check**: r=78
nyquist_margin=4.936 (TRUSTED); r=156 nyquist_margin=2.468 (TRUSTED);
r=312 nyquist_margin=1.234 (MARGINAL-REDUCED-CONFIDENCE) — exactly as
predicted, all three tiers landed where the pre-registered thresholds
put them.

**kappa_window(r): 78→0.018337, 156→0.0008867, 312→0.000004793.**

**P2 (monotonicity): CONFIRMED**, as predicted.

**P3 (functional-form + shape discriminator): SCORED — the headline,
genuinely surprising finding.** With r=312 committed, the full 2-point-
fit-vs-held-out-r=78 test ran: shape_ratio = **19.79** (vs. the sqrt-law
band 2.00±0.3 and the linear-law band 4.00±0.5 — nearly 5× past the
linear-law's own already-generous band, and ~4× further out than T8's
own already-REFUTED absorber ratio of 5.33 on the ambient channel).
Model-A (sqrt-law) miss=85.55%, Model-B (linear-law) miss=75.93% —
both catastrophically outside the pre-registered 25%/60% tolerance
bands. **kappa_window falls by ~20.7× from r=78→156, then by ~185×
from r=156→312** — accelerating, not merely failing to fit a power law.
This is a materially different (and much more extreme) failure shape
than T8's own P-VISION-1b REFUTE on the ambient channel, which showed
modest absolute-C drift (−0.72→−0.73→−0.73, order-10% relative changes)
against the SAME two candidate laws. Not interpreted here (R3 meta-rule
— a surprising feature gets a resolution check before a mechanism
debate) — flagged explicitly for Phase 5.

**P4 (sub-Nyquist ripple generalization, GATED): FALSIFIED at all three
r, and TRUSTED at r=78 and r=156.** r=78 (reused): P2-analog=FALSIFIED
(0 reversals), nyquist_tier=TRUSTED. r=156 (new): P2-analog=FALSIFIED
(0 reversals), settling_pass=True (0/53 kappa failures, 0/53 phase
failures, both well inside tolerance), nyquist_tier=TRUSTED —
**P4_TRUSTED=True**, exp-104's own clean null genuinely generalizes to
r=156 under a real, passing settling check on the exact channel that
had never been settling-tested before. r=312 (new): P2-analog=FALSIFIED
(0 reversals) but nyquist_tier=MARGINAL-REDUCED-CONFIDENCE (no settling
leg run there, disclosed idealization) — reported with reduced
confidence, not silently treated as equally trustworthy as r=156's.

**P5 (thermal sidecar): CONFIRMED.** Classification UNDETECTABLE at all
three r (699.27×/349.80×/175.06×, monotonically declining as predicted);
r=78 row reproduces the locked 699.27× citation exactly
(2.860128e-05 K). Realizability/diffraction-inflation caveat carried
inline as committed.

## Learned

1. **The coherent point/region-intensity channel's own near-field
   scale-dependence is far steeper, and shaped completely differently,
   than the ambient Weber-contrast channel's already-REFUTED T8
   finding** — this is new information, not a replication. Where T8's
   own absorber showed slow, near-monotonic drift close to (though
   outside) both candidate power laws, this channel's kappa_window
   collapses by more than four orders of magnitude across the same
   r-family (0.018→0.00089→0.0000048), accelerating rather than
   flattening. Both cross-channel non-replication (P3, this cycle) and
   the earlier cross-channel replication of a clean ripple null (P4,
   also this cycle) are real, disclosed findings about how much this
   program's two existing near-field instruments actually agree with
   each other under scale — the answer is "sometimes, and sometimes not
   at all," itself informative for how much weight either channel's own
   near-field readings should carry pending a real witness-scale bridge.
2. **The Nyquist/Fresnel pre-check (mandatory fix 4) worked exactly as
   designed** — it predicted, before any r=312 call ran, that the
   sub-Nyquist margin would degrade to MARGINAL at r=312 (1.234, just
   above the UNRESOLVED floor of 1.0) while staying comfortably TRUSTED
   at r=156 (2.468) — and the actual P4 readings landed in exactly the
   predicted trust tiers. This is a genuinely useful, cheap, reusable
   diagnostic for any future extension of this instrument to r>312.
3. **The new point-channel settling leg (mandatory fix 3) passed
   cleanly** (0/53 kappa failures, 0/53 phase failures) — the first time
   this program has ever settling-tested `kappa_region_point`/
   `delta_phi_point` at any geometry, closing a genuine gap EM's
   Phase-2 critique identified (this channel had never been checked, at
   any r, in this program's history).
4. **r=312's real cost (1867.5s pilot, ~52.1 min for the full 2-call
   leg) came in well under the Phase-1 proposal's own worst-case
   estimate** (up to 7.1h) — closer to its optimistic-case naive-κ³
   estimate than to T8's own 3.5×-worse-than-naive precedent. This
   program's own T8-derived cost-blowup caution was the right posture
   to take (a real risk that did not materialize this time is not
   evidence the caution was wrong to hold).

## Next (candidate directions, Iteration 83 queue material)

1. **P3's own accelerating-collapse finding needs a resolution check
   before any mechanism debate** (R3 meta-rule) — is `kappa_window`'s
   own ~20×/~185× two-step collapse a genuine near-field physical
   effect (the fixed-cell window offset representing an ever-shrinking
   FRACTION of the object's own growing radius, pushing the measurement
   ever deeper into the geometric shadow's near zone as r grows), a
   floor/dynamic-range artifact (kappa_window(312)=4.8e-6 is getting
   close to floating-point/discretization noise territory relative to
   the empty-scene intensity scale), or something else? A dedicated,
   zero-new-mechanism resolution/floor check is the single highest-
   value item this cycle's own result creates.
2. **A settling-independence leg at r=312** — the one disclosed
   idealization this cycle did not close (no settling check ran at
   r=312 at all), now directly relevant since r=312's own nyquist_tier
   is already MARGINAL; a settling artifact there would compound with,
   not merely coexist alongside, the aliasing-margin risk.
3. **A real, measured `sections.widths()` `sigma_ext(r)` trend**,
   replacing P5's own `Q_ext`-invariance placeholder — zero marginal
   FDTD cost, reusing this cycle's own captured fields (deferred from
   the Phase-1 proposal's own Next list, still open).
4. **The oblique-angle extension of this same θ=0°-validated bridge**
   (deferred explicitly in the Phase-1 proposal, still open).
5. The standing `delta_scene` R3-vs-R4 split (Tier 3, now SIX
   consecutive deferrals per exp-104's own explicit written warning —
   a seventh must be re-justified in writing or executed) — untouched
   by this cycle, exactly as exp-102/103/104 left it.
6. The other two Reconciled Iteration-82 Tier-1 items (R23's own scope
   decision; the near-null-exclusion raw-bin-identity refinement) —
   explicitly out of this cycle's own scope, still open.
