# exp-024 — Instrument Margin + Estimator Adjudication (panel Iteration 2)

**2026-08-12 · driver: Clyde as panel Director · status: predictions
committed, instrument not yet run**

Second experiment of the panel program (PANEL.md / LOGBOOK.md). Iteration 1
(exp-020) put constraint 3 on the record for the first time (absorber
C = −0.686, Tier-A photopic FAIL ×34) but its own instrument carried a
λ-dependent fringe-zone floor (δ_C = 0.0009/0.0068/0.0183 @ 450/600/750 nm)
that broke two pre-committed gates (P1a at 600/750, P1b at 750°/±40°) and
left an uncommitted floor-correction estimator (additive vs. ratio) doing
load-bearing interpretive work. Iteration 2's panel (LOGBOOK, this entry)
proposed the fix (PHOTONICS, lead), critiqued it five ways, and Red Team
returned **proceed-with-mandatory-fixes** with a decisive empirical finding:
PHOTONICS' own extrapolation model, backtested against exp-020's own three
measured (margin/fringe-ratio, δ_C) points, underpredicts δ_C by 5.7–15.7×
near ratio ≈ 1 — the true behavior there is a threshold collapse (EM's own
Iteration-1 finding), not a smooth power law. This file is the **Phase-3
synthesis**: one testable configuration, six mandatory fixes resolved on the
record, predictions committed before the first run.

## Synthesis — the panel's demands, resolved

**Accepted, implemented as stated:**

1. **VISION's flip — δ_C gate tightened to ≤ 0.001 at EVERY λ** (not
   PHOTONICS' 0.003, not just 600/750 nm). Red Team independently confirmed
   the reason: against the already-pinned OFF-lab σ(I) target (Materials,
   Iteration-1 Phase 5: τ_center = 0.008, chord-model C = −0.005), a 0.003
   gate gives SNR ≈ 1.7 — nowhere near decidable. `DELTA_C_GATE = 0.001` in
   `run.py`.
2. **THERMODYNAMICS' flip — BOX derived, not hand-tracked.** `design_geometry.py`
   now computes `BOX = (OBJ_X∓(R_OUT+12), OBJ[1]∓(R_OUT+12))` from a stated
   `BOX_CLEARANCE = 12` constant (reconstructed from exp-020's own BOX, which
   Thermo verified by hand) rather than being a one-line assertion. Printed:
   x-clear [40, 60] cells to damping, y-clear [662, 662] cells — symmetric,
   as it should be for an object recentered at NY/2.

**Accepted in substance, implemented differently than either flip proposed
(Red Team's attack #1 forced a stronger fix than either Phase-1 or Phase-2
offered):**

3. **The coverage-margin multiplier is 3.5×, not PHOTONICS' 2× or EM's
   flip-proposed 3×.** Red Team's decisive finding: backtesting PHOTONICS'
   own bracketing δ_C(ratio) models (p=1, p=2, calibrated to the single
   450 nm anchor) *backward* against exp-020's own 600/750 nm data points
   underpredicts δ_C by 5.7–15.7× — because the true δ_C(ratio) curve near
   ratio ≈ 1 is EM's own documented "twentyfold cancellation collapse"
   threshold, not a smooth decay of any single exponent. No amount of
   picking a "safer" exponent fixes an extrapolation across a
   discontinuity-like transition; the only sound fix is to not need the
   extrapolation. `MARGIN_MULT = 3.5` (`design_geometry.py`) pushes the
   worst-case margin/fringe-zone ratio to **4.53 / 3.92 / 3.51** at
   450/600/750 nm — 3–4× better than exp-020's *best* historical point
   (ratio 1.21 @ 450 nm, which gave δ_C = 0.0009) and clear of the ratio≈1
   collapse zone at every wavelength, not just the worst one. This costs
   NY 1200→**1584** (a 32% cell-count increase, ≈1.3× exp-020's own
   runtime) rather than PHOTONICS' 1360 (+13%) or EM's ~1510 (+26%) — the
   Director judged the extra ~10% runtime cheap insurance against
   re-running this exact iteration a second time.
4. **MATERIALS' flip (auto-rederive the sponge/g-value against whichever
   angle set is used if the extrapolation is off) is superseded, not
   adopted literally.** With no extrapolation model committed pre-run (item
   3), there is nothing to auto-check against — the standing worry
   (calibration resting on an unvalidated fit) is eliminated at the root
   rather than patched with a conditional re-derivation rule. MATERIALS'
   deeper point — the sponge calibration must not rest on unearned
   confidence — is honored more strongly than the literal flip asked for.
5. **Red Team's #3 (P-EST's undefined outcome gap) — replaced with a full,
   exhaustive three-way outcome partition** (Predictions, P-EST below) that
   covers every possible measured combination, not just two point-estimates
   with a gap between them. The additive-vs-ratio question itself is
   **retired as a going concern**: with δ_C ≤ 0.001 at every λ (the gate),
   raw C needs no correction at all — the whole debate this iteration exists
   to end simply doesn't arise if the gate holds, and the outcome partition
   states explicitly what happens if it doesn't.

**Accepted in part, one clause overridden with reason:**

6. **QUANTUM's flip (add the coherent-superposition bridge gate to THIS
   iteration, zero schema cost) — the "add it now" half is OVERRIDDEN; the
   "state the deferral explicitly, don't let it lapse by silence" half is
   ACCEPTED.** Red Team's independent read is adopted as the ruling reason:
   QUANTUM's "zero schema cost" framing is itself incomplete — simultaneous
   multi-angle current injection with random relative phases and M draws is
   new *source* machinery, and PANEL.md's own house rule ("new machinery ⇒
   new suite stage with at least one absolute identity gate BEFORE results
   are trusted") means it needs a properly gated suite stage of its own, not
   a bolt-on inside an instrument-margin rerun. **Ruling, on the record:**
   the bridge gate stays Iteration 4's job (σ(I) readiness), where it
   belongs alongside the shared-intensity-axis schema change it's paired
   with — not deferred by omission, deferred by this stated decision.

**Overridden outright: none beyond the two partial overrides above** (item 4
and the "add it now" half of item 6) — every other mandatory fix and flip is
implemented as proposed or strengthened.

## Setup (pinned by `design_geometry.py` — re-run it if any constant moves)

| Knob | exp-020 | exp-024 (this experiment) |
|---|---|---|
| Grid | Δ=30 nm, courant 0.99, absorb 40, cpl 15/20/25 | unchanged |
| Domain | 360 × 1200 | **360 × 1584** |
| Source | x=300, y∈[40,1160], taper 40 | x=300, y∈**[40,1544]**, taper 40 |
| Object center | (170, 600) | (170, **792**) |
| Object / articles | empty · absorber (PEC r=30 + graded shell 30→78) · PEC r=78 · sponge r=78 ε=1 σ=6.41e-4 (τ=0.10) | unchanged |
| Measurement plane | x=77 (lever 93, D_source→plane=223) | unchanged |
| Windows (rel. y0) | obj ≤78, guard (78,185], flank [185,263] | unchanged |
| `BOX` (ledger) | (80,260,510,690), hand-tracked | **(80,260,702,882), derived** (clearance=12 cells, `BOX_CLEARANCE`) |
| Coverage-margin rule | none pre-committed | **m ≥ 3.5·√(λ_max·D) ≈ 261.3 cells** — worst measured margin 261.88 cells |
| Margin/fringe ratio (worst angle) | 1.21 / 1.05 / 0.94 @ 450/600/750 nm | **4.53 / 3.92 / 3.51** @ 450/600/750 nm |
| δ_C decision-floor gate | reporting convention only (0.01/0.005 loose) | **hard gate ≤ 0.001 at every λ** |
| P1b coverage gate | ≥0.8 (missed at 750°/±40°: 0.795/0.796) | ≥0.8, must be clean everywhere |
| Floor-correction estimator | additive, used post-hoc, uncommitted | **retired** — raw C is the only currency if the gate holds (see P-EST) |
| Angles | 9 committed (0,±10,±20,±30,±40) + 8 N17 convergence | unchanged sets |
| N17 ceiling (ray trace) | not separately computed (N9 ceiling used) | **recomputed: −0.8074 (equal) / −0.8161 (cos)**, vs N9's −0.7990/−0.8092 |
| Pre-committed fallback (if gate misses) | none | **±35°, N=9** — geometry verified (worst margin 292.85, comfortably clear); ceilings pre-derived: opaque equal −0.8372, opaque cos −0.8447, sponge −0.0657 |
| Runs | 124 | **124** (same structure) |
| Runtime estimate | 472 s | ≈600–650 s (+32% cells, 4 workers) |

Geometric ceilings (ray trace, `design_geometry.py`, unaffected by NY —
pure function of R_OUT/LEVER/window geometry): N9 opaque C_geo = −0.7990
(equal) / −0.8092 (cos); N17 opaque C_geo = −0.8074 (equal) / −0.8161 (cos);
sponge C_geo = −0.0626 (both ray-trace-identical to exp-020's — geometry-
only, NY-independent). Fallback (±35°, N=9) ceilings: opaque −0.8372
(equal) / −0.8447 (cos); sponge −0.0657.

## T1 escape-route statement

Unchanged from Iteration 1's own framing: **this experiment implements no
escape mechanism.** It re-measures exp-020's four materially-unmodified
articles on a corrected instrument. No σ(I), σ(x,t), angular-selectivity,
or sub-threshold machinery is touched; `lab/ambient.py` is untouched.

## Predictions — committed before this experiment's first run

- **P-M1 (decision floor, hard gate δ_C ≤ 0.001 at every λ):** predict
  δ_C ∈ [0.00005, 0.0009] at all three λ — the new worst-case
  margin/fringe ratio (3.51–4.53) is 3–4× better than exp-020's *best*
  historical point (ratio 1.21 → δ_C 0.0009), so this is a qualitative,
  direction-only prediction, not a fitted extrapolation (Red Team's attack
  #1 is exactly why no functional form is committed here). **Falsification:**
  if δ_C > 0.001 at any λ despite the 3.5–4.5× margin ratio, that is a real,
  surprising instrument finding — not a bookkeeping miss — and no further
  same-shift patch is attempted; the pre-committed ±35° fallback (bands
  above) reruns instead, and the surprise itself goes to Phase 5 as a
  finding (the m ≥ k√(λD) family of rules would need a fundamentally
  different mechanism, not a bigger k).
- **P-M2 (coverage gate, ≥ 0.8):** predict min/median ≥ 0.99 at every
  committed angle and λ — the fringe-leakage mechanism that produced
  exp-020's 0.795/0.796 miss should be essentially eliminated at these
  margins.
- **P-M3 (absorber):** C ∈ [−0.71, −0.66], central ≈ −0.685 at every λ,
  both weightings — reproducing exp-020's physics (only floor precision
  changes). Falsifiable λ-ordering claim (PHOTONICS' own, carried forward):
  |C(750)_raw − C(450)_raw| ≤ 0.006 (near-flat, diffraction-fill argument,
  Fresnel numbers 2.6–4.4 at this near-field plane).
- **P-EST (estimator question — exhaustive three-way outcome partition,
  replacing Red Team #3's flagged undefined gap):**
  - **(a) δ_C ≤ 0.001 at all λ AND |C(750)−C(450)| ≤ 0.006:** wavelength-
    flatness is CONFIRMED DEFINITIVELY from raw data alone. The
    additive-vs-ratio estimator question is RETIRED — exp-020's apparent
    λ-ordering reversal was pure floor bias, settled without needing either
    correction model. This is the expected outcome.
  - **(b) δ_C ≤ 0.001 at all λ BUT |C(750)−C(450)| > 0.006:** a real,
    previously-hidden chromatic effect survives floor-precision — NOT an
    estimator failure (the floor is negligible either way), a genuine new
    finding warranting its own follow-up thread.
  - **(c) δ_C > 0.001 at any λ:** that λ's absorber number carries an
    explicit asterisk (floor-limited); raw C ± δ_C is reported with no
    correction (Red Team #2's standing rule: additive/ratio correction
    stays retired as an ongoing procedure regardless); the pre-committed
    ±35° fallback reruns that λ.
- **P-M4 (PEC, material blindness):** C ∈ [−0.85, −0.80]; split
  |C_PEC − C_absorber| = 0.14 ± 0.02 (rim-transmission mechanism, PHOTONICS
  Phase-5 Iteration 1, expected unchanged — a property of the shell's τ(r)
  profile, independent of the ambient floor).
- **P-N17 (N17 ceiling recompute + PEC near-field-excess check, Red Team's
  zero-run rider, now doubly verified — hand-derived in Iteration 2 Phase 1
  AND script-derived here):** predict PEC(N17, 600 nm, raw) excess over the
  −0.8074 ceiling of **0.020–0.035** — reproducing exp-020's excess
  (0.0271→0.0286, N9→N17) essentially unchanged, since the excess sits at
  the hard PEC edge (near-field, z/z_R-scale) and the margin fix only
  changes the far background. This rules out ceiling-coarseness as the
  excess's origin (again) but does NOT certify a design-ready mechanism —
  EM's T8 near-to-far bridge (r = 78/156/312 family) is still required
  before "near-field extinction excess" becomes a design input.
- **P-M5 (sponge):** C ∈ [−0.075, −0.055], central ≈ −0.063 — matching the
  geometric ceiling (−0.0626) to within exp-020's own 0.001-level agreement.
- **P-M6 (convergence + plane sensitivity, gates unchanged):**
  |C(N9)−C(N5)| ≤ 0.05; |C(N17)−C(N9)| ≤ 0.02 (empty + PEC @600); plane
  sensitivity (12/15/16) ≤ 0.05. Predict continued clean passes, reproducing
  exp-020's actual values (0.026 / 0.0115 / 0.0102) — near-object physics is
  untouched by the far-field margin fix.
- **P-M7 (ledger identities, BOX now derived not hand-tracked):** empty-box
  net flux ≤ 0.02 (relative); two-route σ_ext agreement ≤ 0.12; absorber
  σ_abs/σ_ext ≥ 0.45. Predict continued clean passes (exp-020: 0.0012/
  0.0006) — the derived BOX preserves the same 12-cell object clearance on
  every wall that exp-020's hand-picked BOX happened to have (verified:
  x-clear [40,60], y-clear [662,662] — symmetric, as expected for an object
  centered at NY/2).

## Idealizations (lab convention, unchanged from exp-020 unless noted)

2D TMz, one polarization; CW single-λ, 3-λ quadrature for white light;
linear-media incoherent-sum idiom, unchanged (`lab/ambient.py` untouched —
no σ(I) or time-varying material enters this iteration, per the explicit
Director ruling on QUANTUM's flip above); back-lit only, front-lit
reflectance channel deferred; graded damping bands, not PML; perceptual
scoring untouched — this iteration measures C more precisely, it does not
re-derive or re-score against the frozen threshold table. **New to this
iteration:** `MARGIN_MULT = 3.5` is a Director judgment call informed by
Red Team's backtest, not a first-principles derivation of exactly how much
margin is enough — P-M1's falsification clause is the honest test of that
judgment, not a certainty. The N17 ceiling recompute is a ray-trace
geometry calculation, not a wave-optics derivation (EM's own stated
limitation, carried over) — it rules out one failure mode for the PEC
near-field excess, not all of them.

## Run plan

1. `design_geometry.py` (done, verified above) → `run.py` (124 runs,
   ≈600–650 s estimated).
2. Score P-M1–P-M7 and P-EST/P-N17 in this file; results row into
   LOGBOOK.md (Iteration 2, Phase 4); panel Phase-5 review follows.
3. No `lab/` engine changes — trust suite reverification is a formality
   (no new machinery), but run per house discipline anyway before and
   after.

## Results

*(Appended after the run — everything above was committed first, commit
`b28635b`. Primary run: 124 runs, 390 s. Fallback rerun: triggered per
P-M1's own pre-committed contingency, 108 runs, 348 s — `run_fallback.py`,
committed `c67506b` alongside the primary raw data. Suite 41/41 before and
after (no `lab/` changes).)*

**Headline: the margin fix worked, but not for the reason predicted — and
that gap is itself the iteration's real finding.** MARGIN_MULT=3.5 pushed
the worst-case margin/fringe-zone ratio to 3.5–4.5× (vs exp-020's 0.94–1.21),
comfortably clear of the ratio≈1 collapse zone Red Team's backtest
identified. δ_C *did* improve dramatically at 600/750 nm (0.0068→0.0015,
0.0183→0.0037, both ~5× smaller) — but **missed the ≤0.001 gate at ALL SIX
(λ, weighting) combinations anyway**, including 450 nm, whose δ_C got
*worse* (0.0009→0.0026) despite having the single best margin/fringe ratio
(4.53) of any point measured, primary or historical. The margin/fringe-ratio
model — the mechanism this whole iteration was built around — does not
predict this. **P-M1: REFUTED, honestly, per its own pre-committed
falsification clause** ("if δ_C > 0.001 at any λ despite the 3.5–4.5×
margin ratio, that is a real, surprising instrument finding... the
pre-committed ±35° fallback reruns instead").

**The pre-committed fallback (±35°, N=9 — dropping only the two ±40° edge
angles) resolved it cleanly:** δ_C = 0.00089/0.00081 (450), 0.000033/0.000071
(600), 0.00043/0.00045 (750) — every combination passes the 0.001 gate,
most by an order of magnitude or more. **This localizes the residual
floor specifically to the ±40° angle pair, not to margin/fringe-zone ratio
at all** — trimming 5° off each side collapsed the floor 3–9× at every λ,
after a 32%-larger domain had already failed to touch it at 450 nm. Neither
this iteration's own margin-ratio model, EM's original coverage rule, nor
Red Team's backtest-motivated widening anticipated an angle-specific (not
ratio-driven) mechanism — genuinely new, unexplained, flagged for Phase 5,
not quietly folded into "margin fixed it."

**Weber contrast C (plane 15, equal weights, RAW — no correction applied,
per the retired-estimator ruling):**

| Article | Config | 450 nm | 600 nm | 750 nm | V-weighted |
|---|---|---|---|---|---|
| empty (δ_C) | primary (±40°) | −0.0026 | −0.0015 | −0.0037 | −0.0016 |
| empty (δ_C) | fallback (±35°) | +0.0009 | −0.0000 | +0.0004 | — |
| absorber | primary | −0.6781 | −0.6843 | −0.6866 | **−0.6840** |
| absorber | fallback | −0.7170 | −0.7211 | −0.7284 | — |
| PEC | primary | −0.8194 | −0.8243 | −0.8293 | −0.8240 |
| PEC | fallback | −0.8605 | −0.8677 | −0.8771 | — |
| sponge | primary | −0.0652 | −0.0639 | −0.0658 | −0.0640 |
| sponge | fallback | −0.0651 | −0.0661 | −0.0654 | — |

Convergence (PEC @600, primary geometry): N5 −0.7999 · N9 −0.8243 · N17
−0.8379. Plane sensitivity ≤ 0.0102 (absorber, worst). Ledger identities:
empty-box worst 0.0012 (≤ 0.02), two-route worst 0.0006 (≤ 0.12) — both
reproduce exp-020's own values (0.0012/0.0006) essentially exactly,
confirming the derived `BOX` preserves the ledger physics as predicted.

### Predictions scored

- **P-M1 — REFUTED at the primary (±40°) geometry; RESOLVED by the
  pre-committed fallback.** See headline above. The falsification clause
  fired exactly as written and the pre-committed response (no live patch,
  run the fallback) is what actually happened — this is the discipline
  working, not a miss to apologize for.
- **P-M2 — coverage gate PASSED but the central prediction MISSED.**
  Worst P1b min/median = 0.837 (≥ 0.8 gate: comfortable pass), but the
  predicted "≥0.99 everywhere" central value did not hold — 0.837 is well
  above gate but far short of the predicted near-unity coverage. Flagged,
  not hidden: the coverage-fraction formula (min/median of the empty
  window segment) evidently doesn't scale as cleanly with margin as guessed;
  worth a cheap look in a future iteration, not urgent (gate itself is
  solidly green).
- **P-M3 — band CONFIRMED; λ-ordering claim REFUTED, and this time it's
  real (P-EST resolves it below).** Primary absorber C ∈ [−0.6781,−0.6866]
  at every λ, band [−0.71,−0.66]: CONFIRMED, central ≈ −0.684 essentially
  reproducing exp-020's −0.686. λ-ordering: |C(750)−C(450)| = 0.0085
  (primary), 0.0114 (fallback) — both exceed the predicted ≤0.006 near-flat
  band. |C| *grows* toward red at both geometries and in both articles
  (see P-EST) — the opposite direction from the diffraction-fill argument
  either exp-020 or this proposal predicted, and, thanks to the fallback's
  clean floor, now known NOT to be an artifact of floor bias.
- **P-EST — outcome (b), the real-effect branch, CONFIRMED.** Per the
  pre-committed 3-way partition: fallback δ_C ≤ 0.00089 at every λ (well
  under the 0.001 gate) AND |C(750)−C(450)| = 0.0114 > 0.006 → **a real,
  small chromatic effect survives floor-precision.** This is NOT an
  estimator failure (the floor is negligible either way — no correction
  was applied or needed) and NOT the additive-vs-ratio question exp-020
  left open (that question is now moot, exactly as designed — raw fallback
  numbers need no correction). It IS a genuine, previously-hidden finding:
  |C| for both opaque articles (absorber AND PEC, same direction, same
  rough magnitude — absorber Δ=0.0114, PEC Δ=0.0166 at fallback) increases
  from 450→750 nm by roughly 1.5–1.9%, while the optically-thin sponge
  shows no clear trend (Δ=0.0003, noise-level against its own ~0.065
  signal). A real, small, opaque-article-specific chromatic silhouette
  effect, direction opposite the original diffraction-fill hypothesis —
  new candidate mechanism thread for a future iteration, not solved here.
- **P-M4 — CONFIRMED, tightly.** PEC ∈ [−0.8194,−0.8293] (band
  [−0.85,−0.80]). Material-blindness split |C_PEC−C_absorber| = 0.1413 /
  0.1400 / 0.1427 (450/600/750) — predicted 0.14 ± 0.02, central hit almost
  exactly at every λ.
- **P-N17 — CONFIRMED.** PEC(N17, 600 nm, raw) = −0.8379 vs the recomputed
  N17 ceiling −0.8074: excess = 0.0305, inside the predicted [0.020,0.035]
  band and the same order as exp-020's own excess (0.0271→0.0286, N9→N17)
  — reconfirms the near-field extinction excess as N-stable and
  margin-independent, still not certified as a design-ready mechanism
  (EM's T8 bridge remains the open gate for that).
- **P-M5 — CONFIRMED.** Sponge C ∈ [−0.0639,−0.0658] (band [−0.075,−0.055],
  central −0.063) — matches the geometric ceiling (−0.0626) to the same
  ~0.001–0.003 precision exp-020 achieved, now on a properly-margined
  instrument.
- **P-M6 — CONFIRMED.** N9 vs N5 ≤ 0.0244 (gate 0.05); N17 vs N9 ≤ 0.0136
  (gate 0.02); plane sensitivity ≤ 0.0102 (gate 0.05) — all comfortably
  inside, near-object convergence physics unaffected by the far-field
  margin change, as predicted.
- **P-M7 — CONFIRMED.** Empty-box worst 0.0012; two-route worst 0.0006 —
  both reproduce exp-020's own numbers essentially exactly. The derived
  `BOX` (Thermo's flip, item 2 above) preserves the ledger identities
  exactly as the hand-verified clearance arithmetic predicted.

### Headline (for LOGBOOK)

**The instrument-margin fix worked empirically but not by the mechanism
this iteration was built around.** A 3.5× coverage-margin multiplier
(worst-case ratio 3.5–4.5, vs exp-020's 0.94–1.21) cut the decision floor
substantially at 600/750 nm but *increased* it at 450 nm and missed the
pre-committed ≤0.001 gate everywhere — refuting the margin/fringe-ratio
model this whole line of reasoning (Phase-1 PHOTONICS, EM's original rule,
Red Team's backtest-driven widening) shared. The pre-committed ±35°
fallback — dropping only the ±40° edge angles — passed cleanly everywhere,
localizing the true mechanism to something angle-specific at ±40°, not
ratio-driven. That fallback data, clean at every λ, also settled the
λ-ordering question exp-020 left open: the reversal is **not** pure floor
bias — a real, small (~1.5–1.9%) growth of |C| toward red survives in both
opaque articles, opposite the originally-hypothesized diffraction-fill
direction. Constraint-3's headline number is essentially unchanged and
reconfirmed (absorber V-weighted C ≈ −0.684, vs exp-020's −0.686) — this
iteration's contribution is instrument precision and two new open
questions, not a changed verdict.

## Next (pre-registered)

For Phase 5: (1) the ±40°-specific floor mechanism — not margin/fringe-
ratio, something else, angle-specific; a natural next probe is a fine
angle sweep near ±40° (e.g. every 1° from 36° to 40°) to see whether the
floor onset is itself a sharp threshold like EM's ratio≈1 collapse, just
in angle rather than in margin. (2) the new, small, opaque-only red-ward
chromatic C trend (P-EST outcome b) — a genuine new finding, mechanism
unknown, worth its own dedicated thread. (3) Iteration 3's docket #7
(witness-scenario table) and Iteration 4's σ(I) readiness remain queued
per Iteration 1's merged ranking, untouched by this iteration's scope.
