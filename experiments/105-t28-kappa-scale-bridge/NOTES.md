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

**Gate P1 scope note (Phase-5 mandatory fix 5, Red Team's own final-
audit finding, none of the six blind reviews caught this):** Gate P1
(rescoped) verifies only `kappa_region_wide`'s r=78 self-consistency —
it does NOT touch `kappa_window_78` (loaded directly from exp-103's own
`results.json`, unverified by any gate this cycle runs), the actual
anchor P2's monotonicity test and P3's shape-discriminator fit both
score against. The underlying construction is very likely correct
(`window_stats()` is byte-identical to exp-103's own function, and the
window-anchor re-parameterization is algebraically identical to
exp-103/104's window at r=78 — independently confirmed by Red Team), but
this cycle's own "every reused constant is ground-truth-verified" framing
does not, in fact, extend to the one scalar the headline findings depend
on most directly. Stated here so a future reader does not credit "Gate
P0/P1 PASS" with more coverage than this cycle's own code provides.

**kappa_window(r): 78→0.018337, 156→0.0008867, 312→0.000004793.**

**P2 (monotonicity): CONFIRMED**, as predicted.

**P3 (functional-form + shape discriminator): SCORED — the headline
finding, now CAVEATED per Phase-5 mandatory fixes 3/4 (Red Team's final
audit; independently found by PHOTONICS/EM/QUANTUM/THERMODYNAMICS).**
With r=312 committed, the full 2-point-fit-vs-held-out-r=78 test ran:
shape_ratio = **19.79** (vs. the sqrt-law band 2.00±0.3 and the
linear-law band 4.00±0.5 — nearly 5× past the linear-law's own already-
generous band, and ~4× further out than T8's own already-REFUTED
absorber ratio of 5.33 on the ambient channel). Model-A (sqrt-law)
miss=85.55%, Model-B (linear-law) miss=75.93% — both catastrophically
outside the pre-registered 25%/60% tolerance bands. **kappa_window
falls by ~20.7× from r=78→156, then by ~185× from r=156→312** —
accelerating, not merely failing to fit a power law. This is a
materially different (and much more extreme) failure shape than T8's
own P-VISION-1b REFUTE on the ambient channel, which showed modest
absolute-C drift (−0.72→−0.73→−0.73, order-10% relative changes)
against the SAME two candidate laws.

**Sharper characterization (mandatory fix 3, PHOTONICS/Red Team):**
because this bridge's own forced geometry gives `x(78):x(156):x(312) =
4:2:1` exactly, ANY two-parameter power law `κ(x)=κ_∞+B·x^n` obeys the
exact algebraic identity `shape_ratio = 2^n`, independent of `κ_∞`, `B`,
or the fit method — the measured 19.79 is therefore precisely equivalent
to an implied global exponent **n≈4.31** (`log₂(19.79)`). This is
roughly double the steepest theory-motivated candidate this program has
tested on this bench family (n≈1–2, standard Fresnel/edge-diffraction
shadow-falloff asymptotics), and — since `graded_black_shell`'s own
τ_shell=24 is held exactly fixed at every r, killing direct shell
transmission identically at every scale — the r-dependent signal must
ride entirely on edge-diffraction-type effects, for which an *apodized*
(smoothly-graded) shell should, if anything, SUPPRESS ripple/diffractive
leakage relative to a hard edge — the wrong direction for n≈4.3, not
merely an unexplained magnitude. A reusable diagnostic for any future
extension of this bridge (κ=8, r=624, etc.).

**Confidence caveat (mandatory fix 4, EM/Red Team — symmetric to P4's
own, below):** `kappa_window_312` (and therefore `shape_ratio` and the
n≈4.31 reading) shares r=312's own MARGINAL-REDUCED-CONFIDENCE Nyquist
tier and complete absence of a settling leg — the identical disclosed
risk P4's own r=312 reading carries, three paragraphs below. Unlike P4,
`run.py`'s own P3-scoring path does not (yet) propagate this risk into
its own verdict field; this is stated here explicitly rather than left
implicit, per Red Team's own finding that this is this cycle's single
most consequential code-level gap. **Not interpreted as physics yet**
(R3 meta-rule — a surprising feature gets a resolution check before a
mechanism debate): Phase 5 additionally surfaced that `kappa_window` has
never been floor-gated at any r in this program's history (unlike its
sibling DENSE_X channels), and that a genuine, previously-unnamed
alternative mechanism exists — holding `τ_shell` fixed while `R_CORE`/
`R_COAT` scale by κ forces the coating's own ELECTRICAL thickness to
grow 4× (2.4λ→9.6λ) across this family, a different absorbing/
interference regime than the pure geometric-window (z/z_R) hypothesis,
with an already-built discriminating control (exp-052's fixed-absolute-
thickness variant) — flagged explicitly for Iteration 83, not chased
here.

**Scope-boundary note (mandatory fix 6, VISION/Red Team):** however
dramatic in raw-ratio terms, this collapse carries ~zero information
bearing on constraint-3. Under even the loosest possible naive mapping
`C=κ−1` (Weber contrast is bounded in `[−1,0]`), all three r-points
already sit deep in saturation past this program's own pinned photopic
threshold `C_thr=0.005` (`|C|`=0.9817/0.9991/0.99999521 at r=78/156/312)
— the ~1,100× total collapse in raw `kappa_window` buys only
`ΔC≈0.018`, a saturating, threshold-irrelevant move. `kappa_window` is
a coherent, single-λ, on-axis near-field transmission diagnostic
(T11/beam-transmission lineage), structurally different from
constraint-3's own ambient/Weber-contrast instrument, and this cycle's
own headline result should never be cited as constraint-3-relevant.

**P3b (a pre-registered, Phase-1-flagged falsifiable prediction —
mandatory fix 2, PHOTONICS/Red Team, scored here after being silently
dropped between the Phase-1 proposal and this file's own frozen
Predictions section):** the sign of Model-A's own fitted slope,
`model_A_B = +0.00701` — **positive, the "right-direction" reading**
(κ decreases as x decreases, i.e. as r grows — consistent with the
near-field shadow continuing to deepen toward a genuine floor rather
than T14's own "wrong-direction asymptote" pathology found on the
ambient/Weber-contrast channel). This is a genuine, structurally
different-channel NON-replication of T14's own finding — materially
informative for T13/T14 either way, though not itself construed as
resolving either thread (a different metric, κ not C).

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

## Phase 5 outcome (six blind reviews + Red Team final audit)

Six blind Phase-5 reviews, all CONFIRM-WITH-GAPS (no clean CONFIRM among
them — a materially denser gap cluster than either exp-102 or exp-104's
own Phase-5 layer). **PHOTONICS** proved the `shape_ratio≡2^n` identity
from primitives (§ above), found `kappa_window` never floor-gated at any
r, found r=312's raw window/point-channel intensities discarded rather
than persisted, and found P3b silently dropped between Phase 1 and the
frozen Predictions. **MATERIALS** independently reproduced the full
thermal table and P3 numbers exactly, and identified the growing-
electrical-thickness alternative mechanism (τ_shell fixed while R_CORE/
R_COAT scale by κ, so the coating's own electrical thickness grows 4×)
with an already-built discriminating control (exp-052). **ELECTROMAGNETISM**
hand-verified the settling leg (a landslide pass, 14.5–30× inside
tolerance at every one of 53 spot-checked points) and found this cycle's
single most consequential code-level gap: P4 has a real risk-propagation
gate (`p4_156_trusted`) symmetric to its own Nyquist/settling pre-check,
but P3 — whose own headline number is a RAWER, less-residualized read of
the identical MARGINAL-tier r=312 capture — has no equivalent gate at
all. **QUANTUM OPTICS** independently reproduced every headline number
exactly and confirmed zero non-classical content is expressible in this
pipeline regardless of outcome magnitude (T1 correctly N/A). **VISION
SCIENCE** found the R23 disclaimer assert covers only `RESULT_TEXT`, not
`PREDICTIONS_TEXT`, despite the module docstring's own two-assert claim
— a second, code-level data point in this sub-thread's disclaimer-
erosion lineage — and proved, with numbers, that P3's own dramatic
collapse carries ~zero constraint-3 information (even the loosest naive
κ→C mapping saturates past photopic threshold already at r=78; the
~1,100× collapse buys only ΔC≈0.018). **THERMODYNAMICS' own self-review**
found a genuine defect in its own Phase-1 proposal (a dominance-ratio
citation, 1949×/487×, that does not reproduce from its own stated
constants — correct values ≈2160.6×/≈540.1×) and, going further, that
Red Team's own Phase-2 audit repeated the identical wrong figures while
explicitly claiming to have independently re-checked them.

Red Team's Phase-5 final audit independently re-verified every finding
from primitives (the `shape_ratio≡2^n`/n≈4.31 identity re-derived by
direct symbolic expansion; the dominance-ratio error re-derived from raw
constants and traced to a likely dropped ε factor; the settling-leg
margins spot-checked at 5 of 53 points; every floor-gate/data-discard
claim confirmed by direct code trace) and adopted all six reviews **in
full, zero overrides**. Found one new defect none of the six caught:
Gate P1 never touches `kappa_window_78` (loaded unverified from a
different experiment's file) — the actual anchor P2 and P3 both score
against — a real precondition-coverage gap distinct from Gate P1's own
(correctly rescoped) `kappa_region_wide` check. **R20 tally: 0.** The
dominance-ratio error is one root-cause defect appearing in two
pre-freeze documents (`phase1_proposal.md`, this seat's own
`phase2_redteam_audit.md`) — confirmed absent from `NOTES.md`'s own
frozen Result/Learned sections by direct grep, so it does not survive
Phase-3 freeze and does not count toward R20 (ruled once, not twice, per
this program's own Iteration-50 counting precedent); every other
candidate defect is a different rule-class entirely (R18/R21-shaped or
an instrumentation-completeness gap, not an R4-shaped wrong-figure
citation). **R20 does NOT fire.** The fact that this seat's own Phase-2
"independent re-check" reproduced rather than caught the error is
disclosed plainly as a first-of-its-kind verification-layer failure —
flagged forward as a pattern to watch, not yet a rule (one instance).
**Checkpoint criterion 4 does NOT fire**: R20's bar unmet; T1 correctly,
repeatedly N/A; constraint-3 proactively (not quietly) scoped out with
numbers (VISION's own ΔC≈0.018 finding is the opposite of a quiet drop);
P5's own numeric bands were pre-demoted to descriptive-only at Phase 3,
and P3's SCORED verdict is a real, falsifiable, already-scored result
(the gap EM found is a missing confidence qualifier, not an unfalsifiable
claim standing unflagged); R16/R21/R22's own forward-elevating clauses
checked explicitly, none trip (R21 does NOT fire a third time — P5's own
NETD finding IS narrated inline in Result, the channel R21 is scoped
to). Two standing forward cautions named, neither firing: the Red-Team-
repeats-a-wrong-figure pattern (one instance), and R23's own two-assert
founding pattern losing one assert this cycle (a second disclaimer-
erosion data point, code-level this time).

**Combined Verdict: PARTIAL** (not RULED OUT — no mechanism class
foreclosed, T1:N/A throughout, correctly; not PROMISING — this cycle's
own declared headline finding, P3's shape_ratio=19.79, is by its own
correct R3-meta-rule choice not yet interpreted, and Phase 5 now shows it
rests on zero floor-gating, no risk-propagation gate symmetric to P4's,
a Gate P1 that never touches its own r=78 anchor, and a genuine
unconsidered alternative mechanism with an already-built, unused
discriminating control — a denser, more consequential gap cluster,
concentrated specifically on the headline result, than either exp-102's
single cosmetic citation slip or exp-104's own framing/evidentiary-
strength cluster). The four OTHER scored verdicts this cycle (Gate P0,
Gate P1-rescoped, P2, P4 at r=78/156, P5) all independently reproduce
clean, with wide margins where margins were checked — this is a real,
logbook-advancing cycle, correctly and honestly not oversold, not a
failed one.

## Next — Reconciled Iteration-83 queue (Red Team's own final-audit
## tiered ranking, `phase5_redteam_audit.md` §7)

**Tier 0 — same-shift, zero-FDTD, applied this shift (see mandatory
fixes above, now landed in this file's own Result section and in
`run.py`).**

**Tier 1 — highest priority, cheap-to-moderate FDTD, real 4-of-6-seat
convergence (PHOTONICS/EM/THERMODYNAMICS ranked #1 or #2; QUANTUM cited
it as the load-bearing precondition):**

1. **Floor-gate `kappa_window`/`window_stats()`'s own output at every
   already-captured r (156, 312), and stop discarding r=312's point-
   channel raw intensities** (persist `wide_channel`/`point_channel`/
   window means for r=312 the same way r=156 already does) — the single
   load-bearing precondition for trusting or refuting P3's own
   accelerating-collapse finding as physics rather than partly a floor/
   dynamic-range artifact.
2. **A settling-independence leg on `kappa_window` itself** (not merely
   `kappa_region_point`, already done this cycle) **at r=156, and — more
   urgently, given the MARGINAL Nyquist tier already there — at r=312.**
3. **Gate P3's own scored verdict on r=312's Nyquist/settling status**,
   symmetric to the already-built `p4_156_trusted` pattern — closing the
   risk-propagation asymmetry EM and Red Team both independently found.
4. **Re-run the `kappa_window`/P3 bridge on exp-052's existing fixed-
   absolute-thickness `graded_black_shell` variant at r=156/312** —
   MATERIALS' own newly-identified, already-built, zero-new-mechanism
   discriminator between the geometric-window (z/z_R) hypothesis and the
   growing-electrical-thickness materials hypothesis. Should reuse items
   1–3's own machinery (floor-gated, settling-checked, risk-gated) from
   the start.

**Tier 2 — important, sequenced after Tier 1 resolves whether P3's
collapse is trustworthy:**

1. A fourth r-point (e.g. r≈221, the geometric mean of 156/312) to break
   the two-point degeneracy and test whether the implied n≈4.3 exponent
   is stable or itself compounding.
2. A real, measured `sections.widths()` `sigma_ext(r)` trend, replacing
   P5's own `Q_ext`-invariance placeholder — re-ranked given P3's own
   finding now sharpens the case for verifying rather than assuming this
   invariance (THERMODYNAMICS' own self-review finding); cross-check
   against exp-030's own T11 `Q_ext` two-point precedent (+0.58% drift
   at κ=2 on a self-similarly-scaled box).
3. Split the blanket "UNOBTANIUM-WITH-PARAMETERS at every r" tag into a
   scaling-law sentence and a per-geometry absolute-thickness sentence
   (1.44–5.76µm, plausibly within the already-cited µm–mm real-coating
   range) — MATERIALS' cheap precision fix.
4. Pin VISION's κ↔C scope-boundary finding as a standing, cited note or
   LOGBOOK T13/T14 cross-reference — preventing any future citation of
   "shape_ratio=19.79" from being misread as constraint-3-relevant.

**Tier 3 — standing, deferred, unchanged this cycle:**

1. The oblique-angle extension of this same θ=0°-validated bridge
   (deferred explicitly at Phase 1, still open).
2. **The `delta_scene` R3-vs-R4 split — now SIX consecutive deferrals;
   Iteration 83 is the point requiring explicit written re-justification
   or execution**, not a silent seventh deferral.
3. The other two Reconciled Iteration-82 Tier-1 items still open (R23's
   own scope decision, now sharpened by this cycle's own second erosion
   data point; the near-null-exclusion raw-bin-identity refinement).
4. A doubled-STEPS settling spot-check at r=312's own near-field-closest
   `DENSE_X` point on the wide/point channels specifically — largely
   superseded in priority by Tier 1 item 2's broader `kappa_window`
   settling leg, which should be built first.
