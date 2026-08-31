# PHASE 5 — REVIEW · ELECTROMAGNETISM (blind) · exp-095 · Panel Iteration 72

*Fresh sub-agent, ELECTROMAGNETISM charter (PANEL.md seat 3: field/wave
behavior, impedance matching, energy coupling; owns reciprocity/passivity/
causality bookkeeping; formalizes what T1 permits/forbids). Read in full:
PANEL.md; LOGBOOK.md (RULED OUT R1–R16 verbatim, ESTABLISHED, LIVE THREADS
T1–T28 including T28's complete history through Iteration 71/exp-094, and
my own seat's exp-094 dispersion-integral work cited in exp-094's Combined
Verdict); the complete exp-095 record (`phase1_proposal.md`,
`phase2_critique_em.md` [my own prior seat's work, re-read for continuity],
four other Phase-2 critiques, `phase2_redteam_audit.md`, `NOTES.md`,
`run.py`, `run_output.txt`, `results.json`,
`gate5_wiring_defect_verification_result.json`). No FDTD calls run; no
other `phase5_review_*.md` read or referenced. Every load-bearing figure
below was independently re-derived from `results.json`/`run_output.txt`
primitives this session, not taken on NOTES.md's or any prior seat's word.*

## 1. Charter-mandatory bookkeeping: reciprocity / passivity / causality

Nothing new to check materially — this cycle spends its FDTD budget
entirely inside the already-validated `R4` (`sigma_max`∈{0.25}) and `R3`
(`sigma_max`=1/3) families; the `R5` family's own Gate 1–6 static checks
all report `PASS=True` in `run_output.txt`, but **Rank 2/Rank 3 were
SKIPPED** (Rank 1 did not PROCEED), so `R5`'s Gate 5 runtime check was
never exercised against a real FDTD call this cycle — only its
fault-injection harness was run in isolation
(`gate5_wiring_defect_verification_result.json`: `control_pass=true`,
`injected_defect_pass=true`, `verdict=PASS`), confirming the harness itself
discriminates correctly, but proving nothing about any live `R5` call
because none occurred. This is disclosed correctly in `run_output.txt`
("RANK 2/RANK 3 — SKIPPED") and is not a defect — a HALT is honest.

For the material physics actually exercised (`graded_black_shell` at three
`sigma_max` values, Rank 1a/1c/4): same non-negative additive conductivity,
same non-dispersive real `eps_r`, same symmetric radial construction as
exp-094 — nothing here introduces gain, a negative-real-part term, or a
gyrotropic/biased/time-modulated coupling. `run_output.txt` confirms
`xi_ext<=0.12` and `sigma_abs>=0` PASS across every Rank-1/Rank-4 call.
**T1 bookkeeping verdict: clean, unchanged from exp-094.** Nothing in this
cycle is or could be mistaken for a T1-escape-route claim (correctly N/A
throughout).

## 2. The central question: is Rank 1c's FAIL wave-physics or a wiring defect?

### 2a. Restating the result precisely

Rank 1a (39.2°/39.4°, far from any known null): `delta_scene` negative at
both, `floor_pass=True` at both — PASS, matching the `cpl=20`/`cpl=30`
comparators in sign at both angles. Rank 1c (38.49°/38.69°, bracketing the
established `cpl=20` null `θ₀=38.590230°` at ±0.1°): `delta_scene(38.49°)
=−1.516840×10⁻³`, `delta_scene(38.69°)=−2.538531×10⁻³`, both
`floor_pass=True` — **same sign, no bracket** — FAIL, per the pre-committed
criterion (`NOTES.md` §Predictions, Rank 1c). Combined gate: PROCEED=False.

### 2b. Does numerical dispersion, at THIS finer resolution, get bigger or smaller?

It gets smaller — and by a well-constrained, independently re-derivable
amount, not merely "smaller in principle." My own seat's exp-093 item 4
(`experiments/093-.../results.json::item4`) tabulates the accumulated
Yee-grid dispersion phase differential between `cpl=20` and `cpl=30` at the
corrected aperture length scale (`ℓ_A`, `table_ell_A`), for six angles
including two on this exact `40.0718°`/`41.7811°`/`41.8377°` neighborhood.
Pulled directly, not hand-typed:

```
theta=37.2:    delta_phi_cpl20/delta_phi_cpl30 = 2.577346 / 1.142836 = 2.25522
theta=40.2:    ... = 1.333493 / 0.591287 = 2.25524
theta=40.0718: ... = 1.375139 / 0.609756 = 2.25523
theta=41.4:    ... = 0.995367 / 0.441320 = 2.25543
theta=41.7811: ... = 0.907753 / 0.402460 = 2.25551
theta=41.8377: ... = 0.895562 / 0.397052 = 2.25553
```

All six ratios cluster at **2.2552–2.2555**, matching the leading-order Yee
isotropic dispersion prediction `(cpl30/cpl20)² = (30/20)² = 2.25` to
within 0.24% — an independent, numeric confirmation (not assumed, derived
from the two already-filed phase columns) that this bench's own dispersion
error obeys the textbook `O(Δx²) ∝ 1/cpl²` scaling law essentially exactly
over this angular range. This means the physical prediction is unambiguous:
**dispersion phase error shrinks monotonically as `cpl` increases**, and by
a known factor. Extrapolating the same scaling to the `cpl=30→40` step
exercised by this cycle's own `R4` family:

```
delta_phi_cpl40 ≈ delta_phi_cpl30 × (30/40)² = delta_phi_cpl30 × 0.5625
delta_delta_phi(30,40) = delta_phi_cpl30 − delta_phi_cpl40 = delta_phi_cpl30 × 0.4375
delta_delta_phi(20,30) = delta_phi_cpl20 − delta_phi_cpl30 = delta_phi_cpl30 × 1.2552  (measured, above)
=> delta_delta_phi(30,40) / delta_delta_phi(20,30) ≈ 0.4375 / 1.2552 ≈ 0.3485
```

Applied to exp-093's own filed `predicted_dtheta(20,30)` values in this
angular neighborhood (`0.0037°–0.0113°`, `table_ell_A`), the projected
`cpl=30→40` dispersion-only node-shift is **≈0.0013°–0.0039°** — smaller
than the `20→30` shift by construction, and **25×–78× smaller than the
±0.1° bracket half-width Rank 1c used to test for the node's survival.**
This is an order-of-magnitude extrapolation from already-committed data
(zero new FDTD cost), not a fresh full dispersion-integral re-run at
`cpl=40` specifically — stated as such, matching this program's
disclosure convention. But it directly answers the task's framing: **yes,
dispersion at the finer `cpl=40` resolution is expected to be smaller, not
larger, than at `cpl=30`** — reinforcing, not merely repeating, exp-094's
own Combined-Verdict finding that dispersion already fell short by 32×–96×
at the *coarser*, larger `20→30` step. A `cpl=30→40` dispersion shift an
order of magnitude smaller still cannot plausibly move — let alone
eliminate — a zero-crossing across a 0.2°-wide bracket. **Smooth Yee-grid
dispersion is not a viable explanation for Rank 1c's FAIL, and refining the
grid makes this conclusion firmer, not weaker.**

### 2c. Staircasing remains live, but so does a construction defect — and Rank 1c cannot tell them apart

With dispersion ruled out quantitatively, two candidates remain, and they
predict the *identical* observable here:

**(i) Curved-boundary staircasing** (the account exp-094's own Combined
Verdict and my own prior-cycle review favored for the interior-window
reversal). Unlike smooth dispersion, staircasing error is not a small,
monotonically-shrinking `O(Δx²)` perturbation — it is a geometry-dependent
re-tiling of the shell's curved boundary at each new pixel pitch, capable
of shifting a near-field interference null's exact location by an amount
set by local curvature rather than a smooth convergence law (my own
exp-094 review, §3). A node genuinely migrating by more than 0.1° between
`cpl=30` and `cpl=40` is not physically absurd on this account, and has a
demonstrated precedent on this exact bench: the R15-addendum interior
window (41.750°–41.900°, 0.15° span) reversed **completely** between
`cpl=30` and `cpl=40` one cycle ago. A comparable-scale shift at 38.590°
would be consistent with that precedent.

**(ii) A construction/registration defect uncaught by Gate 5.** Gate 5
(`_run_sim_r4_sigma`, verified directly in `run.py`) checks exactly one
thing: that `sim.sigma_e[shell_mask].max()` equals the intended
`sigma_max`, where `shell_mask` is computed from `rr` — itself computed
from `cx, cy` that Gate 5 takes as given, never independently verified.
Gate 5 proves the *loss profile* is wired correctly at whatever center the
code thinks it is; it says nothing about whether `obj_x`/`obj_y`, the
source's `y_lo`/`y_hi`/`angle_deg`, or the box/reference-frame constants
are themselves correctly registered for the `R4` family. A small,
systematic coordinate or angle offset — invisible to every gate this
sub-thread has ever run — would produce **exactly** Rank 1c's observed
signature: amplitude-dominated far-field points (Rank 1a) pass because
sign there is set by the amplitude term, phase-insensitive to a small
offset; phase-dominated near-null points (Rank 1c) fail because sign there
is set by `cos(φ)` near `φ=π/2`, acutely sensitive to the same offset
(QUANTUM's Phase-2 argument, independently re-verified true by Red Team's
own audit — and now empirically realized, not merely hypothesized).

**These two hypotheses are observationally degenerate at what this cycle
measured.** Rank 1c was correctly designed (per the mandatory-fix docket)
to be *powered against* the registration-defect class in a way Rank 1a is
not — and it fired. But a genuinely-migrated node and a phase-shifted
apparent node produce the identical bracket-FAIL signature at a single
tested null. Rank 1c narrows the hypothesis space (rules out "no problem
at all," since Rank 1a alone would have missed this) but does **not**,
by itself, discriminate (i) from (ii). Treating this FAIL as settled
evidence for either the wave-physics story or the wiring-defect story,
without a further test, would be an overclaim in either direction —
NOTES.md correctly withholds a directional lean here, and I concur that
is the right call, not a placeholder.

### 2d. The discriminating test that would separate them, cheaply

A construction/registration defect of the size needed to explain Rank 1c
(a fixed coordinate or angle offset in the `R4` recipe) would be expected
to displace **every** established near-null feature in the family
coherently — the same offset applied uniformly wherever a node exists.
Genuine feature-specific physics (staircasing sensitivity set by local
curvature at each specific angle) would **not** be expected to move every
node by a similar amount or in a correlated direction — each null's
migration would depend on that null's own local geometry. This sub-thread
already has three more independently-established `cpl=20` nulls on record,
unused by this cycle: `37.127°`, `40.265°`, `41.461°` (`run_output.txt`'s
own re-pulled `cpl20` crossing set). **Recommendation (below, ranked #1):
run Rank 1c's identical node-bracketing methodology (±0.1°, same `R4`
family, same 8-call cost) at these three remaining nulls.** A uniform
FAIL across all four is strong evidence for a systematic, family-wide
registration defect (Gate 5 does not and structurally cannot catch this
class); a mixed result (some bracket, some do not) is evidence for
genuine, feature-dependent node migration, consistent with the
staircasing account and with this window's own precedent.

## 3. Independent sanity check: Rank 4's `ratio_k=808.6716`, `floor_pass=False`

Pulled directly from `results.json::rank4.corrected` and
`results.json::r13_floor_gate`, not from `run_output.txt`'s prose:

```
FLOOR (r13_floor_gate.floor)      = 1.917438×10⁻⁴
frac_contrast (rank4.corrected)   = 5.204102×10⁻⁶
delta_scene   (rank4.corrected)   = −2.938827×10⁻⁶
ratio_k       (rank4.corrected)   = 808.6716
p_abs_w_c                         = 2.9093637×10⁻¹²
p_abs_w_g                         = 2.9216075×10⁻¹²
```

**Floor check.** `frac_contrast=5.204102×10⁻⁶` vs. `FLOOR=1.917438×10⁻⁴`:
`frac_contrast/FLOOR = 0.02714` — `frac_contrast` sits at **2.7% of
FLOOR**, unambiguously below it. `floor_pass = (frac_contrast >= FLOOR)`
(the formula, confirmed by direct read of `pair_metrics()` in
`experiments/092-.../run.py:208-224`, imported verbatim through the
`exp094→exp093→exp092` `_load()` chain this cycle's own `run.py` uses) is
therefore **correctly** `False` here — this is not a misclassification;
`frac_contrast` genuinely, substantially fails the established floor.

**`ratio_k` internal consistency.** `ratio_k = frac_p_abs/frac_contrast`
by the same formula. Re-deriving `frac_p_abs` independently from the filed
power primitives: `frac_p_abs = |p_abs_w_g − p_abs_w_c|/p_abs_w_c =
|2.9216075×10⁻¹² − 2.9093637×10⁻¹²| / 2.9093637×10⁻¹² = 1.22438×10⁻¹⁴ /
2.9093637×10⁻¹² = 4.2085×10⁻³`. Cross-check: `ratio_k × frac_contrast =
808.6716 × 5.204102×10⁻⁶ = 4.2085×10⁻³` — **matches to 4 significant
figures, independently re-derived from the opposite direction.** The
huge `ratio_k` is arithmetically forced entirely by the tiny denominator
(`frac_contrast`, 37× below FLOOR), not by any anomaly in the numerator:
`frac_p_abs=0.42%` is an unremarkable, small energy-channel fluctuation,
squarely inside this program's own established sub-1%-swing pattern for
the absorbed-power channel (Idealization 23 lineage) — there is no
"numerator spike," only a denominator plunging toward zero. **This is
exactly the R13-founding signature** (a large `ratio_k` against a
near-flat numerator signals proximity to a null in the denominator, not
distance from one — the relationship PHOTONICS' own exp-094 Phase-2
critique already established and Red Team confirmed by direct
recomputation) operating textbook-correctly here. **Verdict: fully
internally consistent — `ratio_k=808.6716` and `floor_pass=False` are
exactly what a genuine, tighter near-null denominator produces, and
`floor_pass=False` is the demonstrably correct classification given the
committed FLOOR value.** `Y=None` (not `Y=1`/ENERGY-DOMINANT) follows
correctly from `run.py`'s own `y_r4 = 1 if (floor_pass and ratio_k>
RATIO_HIGH) else (0 if floor_pass else None)` — `floor_pass=False` routes
straight to `None`, so Rank 4's own `NEITHER` verdict is the correct,
code-consistent classification, not a hedge.

**A genuinely new observation this check surfaces, not previously
flagged in NOTES.md's own Result section at this strength.** Comparing
this cycle's corrected-sigma reading against exp-094's own already-filed
native-sigma reading at the identical angle (`results.json::rank4.
native_comparator`): `frac_contrast` collapses from `2.848×10⁻⁴` (native,
`ratio_k=16.9967`, itself already flagged FLIPPED and near-null-adjacent
by exp-094's own R13/R14 signature) to `5.204×10⁻⁶` (corrected) — a
further **~54.7× drop**, while `ratio_k` grows a further **~47.6×**
(`16.9967→808.6716`). This is not merely "38.4° is near a null" (already
known); it is that the `sigma_max` correction alone drives `delta_scene`
at 38.4° dramatically closer to zero than the native reading already was
— the identical qualitative pattern already demonstrated at 42.0° (exp-093
item 3: native/corrected sign-flip) and now shown to be far sharper at
38.4° specifically. This strengthens, quantitatively, QUANTUM's own
self-falsified Idealization-21 finding that native-sigma-only readings at
38.4° were never safe to trust alone — and argues the 38.4° `cpl=20→30`
"FLIPPED" classification is itself very plausibly a sigma-sensitivity
artifact near a genuine, sigma-dependent zero-crossing, independent of
whatever is happening at the 41.75°–41.90°/38.590° windows. Not scored
(Rank 4's own pre-registered criterion correctly returns NEITHER — no
directional lean was licensed), but worth recording explicitly as a
sharper, quantified version of the finding NOTES.md states only
qualitatively.

## 4. Other checks performed

- **Rank 1a's control-angle distances**, re-derived independently against
  the full six-crossing set in `run_output.txt`: `39.2°→0.6098°` from
  `38.5902°`, `39.4°→0.6718°` from `40.0718°` — both bit-exact to the
  values `NOTES.md`/`run_output.txt` state. Confirmed genuinely
  far-from-null by construction.
- **Gate 5 fault-injection harness** (`gate5_wiring_defect_verification_
  result.json`): `control_pass=true`, `injected_defect_pass=true`
  (correctly fails when `sim.sigma_e[shell_mask].max()=0.5` is injected
  against an expected `sigma_max=0.2`). Confirms the harness discriminates
  a genuine `sigma_e`-magnitude defect — but, per §1 above, this says
  nothing about the registration-class defect §2c discusses, which is a
  structurally different failure mode Gate 5 was never built to catch.
- **Call-count/budget bookkeeping**: `total_fdtd_calls=20` (Rank 1's 16 +
  Rank 4's 4), matching the FAIL-path total `NOTES.md` committed to before
  the run (`16+4=20`). Consistent.
- No sign, energy-conservation, or passivity anomaly found anywhere in
  this cycle's own record beyond what §2/§3 already discuss.

## Verdict: **CONCUR-WITH-GAP**

Rank 1c's FAIL is real, correctly computed, and — per §2b's freshly
re-derived scaling — **cannot be smooth Yee-grid dispersion**, which is
expected to be smaller at `cpl=40` than at `cpl=30` and, extrapolated from
this bench's own already-filed `20→30` dispersion-integral data, falls
short of the tested ±0.1° bracket by roughly 25×–78×. What remains open,
and is **not** resolved by anything this cycle ran, is whether the
explanation is genuine curved-boundary staircasing (physically plausible,
with direct precedent on this same window one cycle ago) or a
construction/registration defect that Gate 5 structurally cannot detect
(equally plausible, and specifically the class Rank 1c was built to probe
without being able to fully discriminate it from the physics
explanation). Rank 4's `ratio_k=808.6716`/`floor_pass=False` result is
independently re-derived and fully self-consistent — the correct
classification given the committed FLOOR — and surfaces a sharper,
previously under-stated finding: the `sigma_max` correction alone drives
38.4°'s `frac_contrast` an additional ~55× closer to zero than the native
reading already showed, strengthening the case that 38.4° sits on a
genuine, sigma-sensitive near-null rather than requiring a separate
explanation from the 41.75°–41.90°/38.590° windows.

## Ranked top candidate next step (Iteration 73)

1. **Node-bracket the three remaining established `cpl=20` nulls
   (37.127°, 40.265°, 41.461°) in the `R4` family, ±0.1° each, identical
   methodology to this cycle's Rank 1c (≈24 calls, 8 per null).** This is
   the cheapest test that can actually discriminate §2c's two live
   hypotheses: a uniform FAIL across all four nulls implicates a
   family-wide registration defect (motivating a new coordinate/placement
   gate, analogous to Gate 5 but for `cx`/`cy`/source geometry, since
   nothing currently checks this); a mixed result supports genuine,
   feature-dependent node migration and reopens the `cpl=50` (`R5`) queue
   item with confidence that Rank 1's far-field-only sign check is not,
   by itself, sufficient clearance for further `R4`-family-derived spend.
2. **Do not resume the `cpl=50` (`R5`) interior sweep (the skipped Rank 2)
   until item 1 above runs.** R15's addendum demanded a ground-truth
   control before trusting further `R4`-family spend specifically because
   a registration defect, if present, would be inherited by every
   mechanically-derived ratio in the same `r{n}_config()` recipe
   (Idealization 17) — running `R5` now would risk spending ~529+ CPU-min
   on a family that may carry the identical undetected defect as `R4`.
3. **A dense local re-scan of `delta_scene(R4)` across 38.3°–38.9°** (a
   handful of points at `cpl=40`, reusing the existing `R4` machinery) to
   locate — if it exists — where this window's zero-crossing actually
   sits at `cpl=40`, rather than only testing bracket-presence at the
   `cpl=20` location. If item 1 supports genuine migration, this is the
   natural follow-up; if item 1 supports a registration defect, this test
   is not worth running until the defect is found and fixed.
