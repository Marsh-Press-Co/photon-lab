# exp-030 — The r=156/312 Near-Field→Witness-Scale Bridge (T8), with a
# Box-Ledger Floor Companion (T11)

**2026-08-14 · driver: Clyde as panel Director · status: predictions
committed, instrument not yet run**

Seventh experiment of the panel program (PANEL.md / LOGBOOK.md). Iteration
7's build is VISION SCIENCE's own five-times-deferred r=156 near-field→
witness-scale bridge (live thread T8), hard-committed at Iteration 5's
close with a **pre-registered Checkpoint-4 tripwire**: if this build does
not execute as committed this cycle, Checkpoint criterion 4 fires
automatically. T11 (the box-ledger channel's own decision-floor
characterization) rides as a companion, strictly lower priority — r=156
takes priority over T11 if scope pressure emerges; T11 may fall back to
Iteration 8, r=156 may not.

Full seven-seat cycle: Phase 1 proposal (VISION SCIENCE) → 5 blind
parallel critiques (PHOTONICS, MATERIALS, ELECTROMAGNETISM,
THERMODYNAMICS, QUANTUM OPTICS — all support-with-changes, three
independently converging on the same core defect) → Red Team last with
everything (verdict: **proceed-with-mandatory-fixes**, 11 numbered
attacks, four caught by none of the five blind critiques) → Phase 3
synthesis (Director: all mandatory fixes accepted, zero overridden) →
predictions committed → Phase 4 run. Full verbatim transcript:
LOGBOOK.md Iteration 7.

## Synthesis — the panel's demands, resolved

**Accepted, implemented as stated (Red Team's mandatory-fix docket, in
priority order):**

1. **[Red Team #1, load-bearing] The r=78 "established" C anchors for the
   OPAQUE articles (absorber, PEC) are corrected.** The Phase-1 proposal
   cited exp-024's **primary** (±40°) geometry values (−0.684/−0.826) —
   the exact configuration Iteration 2's own data showed **missed the
   δ_C≤0.001 gate at all six λ/weighting combinations, non-monotonically**.
   Recomputed in code (`design_geometry.py::C78_ESTABLISHED`) from the
   actual per-λ **fallback** (±35°, NY=1584) numbers in exp-024's own
   NOTES.md, V-weighted with the program's frozen CIE 1924 weights:
   **absorber = −0.7209, PEC = −0.8673** (vs. the proposal's wrong
   −0.684/−0.826 — a ~0.037–0.041 correction, roughly half the width of
   P-VISION-1's own "widened bars" tolerance zone). The sponge anchors
   (off_lab = −0.0055, off_field = −0.0217) were already correctly sourced
   from the fallback geometry — re-verified bit-for-bit against
   exp-026/results.json, unchanged.
2. **[PHOTONICS #2, adjudicated by Red Team over MATERIALS'/QUANTUM's
   alternative fixes] `graded_black_shell`'s sigma_max is rescaled as
   sigma_max(κ) = 0.5/κ**, holding the shell's radial optical depth
   integral(σ dr) exactly constant across r=78/156/312 (printed-asserted
   in code: 24.0 at every κ) — isolating the z/z_R diffraction effect
   Block 1 exists to measure from a confounding "the coating got optically
   thicker" effect the proposal's original held-σ_max scaling would have
   introduced (independently caught by PHOTONICS, MATERIALS, and QUANTUM,
   three different diagnoses of the same root defect). r_in stays
   self-similar (round(30κ)) — the geometric scale-invariance the fit
   itself needs; MATERIALS' alternative (fixed absolute thickness) would
   have broken that. **New machinery, gated before trust**: a flat-coating
   R re-check at each new (σ_max, thickness) pair (`run.py::
   coated_wall_r_gate`), reusing suite-7's own wall-test idiom — measured
   R_coat ≈ 0 (order 1e-5, well below the established 0.2% bar) at all
   three scales (see Results). MATERIALS' realizability caveat (a
   literally self-similar shell would be unobtainium — 0.31–0.92 m thick
   [corrected post-Phase-5, Red Team's audit: the original 0.6–1.9m
   figure read the witness RADIUS (0.5–1.5m, the code's own convention)
   as a diameter — a real unit error, not just an ambiguity; the
   honest figure is roughly 2× smaller, still comfortably unobtainium
   for a coating] —
   at witness scale) is kept as a stated idealization, not adopted as the
   geometry fix.
3. **[QUANTUM #3, Red Team's "relabel, don't rescale" adjudication] The
   OFF-lab/OFF-field sponge articles keep their existing τ_center-held-
   fixed convention** — correct for their role in the C(z/z_R) fit.
   §3's claim that this family licenses "σ(I) OFF-state bars transfer to
   witness scale" is **struck** — that would need a separate, σ-held
   analysis this cycle does not run.
4. **[Red Team #3/#4/#5, none of Phase 2's five blind critiques caught]
   T11's `box_dev` metric is redefined** to this program's own established
   convention, `abs(σ_ext_A − σ_ext_B) / abs(σ_ext_A)` (verified against
   all 27 prior uses in this repo) — not the Phase-1 proposal's own
   drifted `/mean` formula. The T9/T10 "consequence" ratios are computed
   **in code**, not hand-asserted — Red Team independently caught BOTH the
   proposal's own arithmetic error on this sentence AND a second,
   independent error in THERMODYNAMICS' own hand-corrected figure on the
   same sentence (proposal: "3–3000×"; THERMODYNAMICS' correction:
   "167–5000×"; Red Team's own, independently re-derived: **≈320–9,615×**
   — see `run.py::run_fit`'s printed T9/T10-vs-floor computation). T9 and
   T11 are also now explicitly flagged, in this record, as **cross-article**
   (T9 measures `graded_black_shell`; T11 measures the uniform-conductivity
   ON disk) — a second, independent reason box_dev is a floor on T11's own
   channel specifically, not automatically transferable to T9's.
5. **[Red Team #6, constraint-3 relevant] A δ_C empty-scene decision-floor
   check is added at r=156** (`run.py::run_floor156`, reusing the empty
   captures Block 1 already collects — zero marginal FDTD cost) **before**
   P-VISION-3's PASS/FAIL licensing language is trusted. The ±35° fallback's
   clean floor was only ever established at r=78's own NY=1584; this
   cycle's own coverage-margin formula is structurally the same rule
   Iteration 2's own data showed does NOT govern the real δ_C mechanism —
   dropping ±40° did — so the floor must be re-measured at the new
   geometry, not assumed to transfer by formula.
6. **[Red Team #7] At r=312, PEC and the graded_black_shell absorber (the
   two hard-edged, angle-sensitive articles) run the full N=9 fallback
   angle set, not N=5.** The N5-vs-N9 convergence precedent (exp-026's
   P-MAT7, |Δ|=0.0005) was measured on the smoothest, lowest-contrast
   article in the whole program (the τ=0.10 dilute sponge) and should not
   be generalized to opaque, hard-edged articles at an unprecedented scale
   without its own check. The OFF-lab/OFF-field sponges keep N=5 at r=312
   — the precedent's own regime. (Cost consequence: r=312's run count rises
   from the proposal's original 25 to **37**.)

**Recommended, not mandatory — adopted anyway (cheap, closes a
Checkpoint-adjacent risk named at Iteration 4/5):**

7. **[Red Team #9] One doubled-STEPS_AMBIENT settling diagnostic at
   r=156** (absorber, λ=600nm only — `run.py::run_settle156`), checking
   whether T10's own settling-re-entering-at-finer-geometry confound
   (Iteration 4/5's own hard-won lesson) shows up here. EM's framing
   ("exactly T10's confound, one iteration old") was itself over-strong —
   Red Team's own audit found `STEPS_AMBIENT(r)` genuinely does scale with
   the growing domain (unlike T10's actual bug, a literal unrescaled
   constant) — but a direct check is cheap and closes the question rather
   than leaving it argued.

**Overridden outright: none.** Every one of Red Team's numbered attacks
was either a cheap, mechanical correction (recompute a number in code, fix
a formula) or a scoping edit (strike one sentence) — none required
abandoning the r=156 commitment itself, and Red Team's own verdict
explicitly weighed and rejected reject/re-defer as unwarranted given the
defects' cheap, mechanical nature.

**A defect the Director caught independently, during Phase-4 implementation
(not raised by any Phase-2/Red-Team seat — logged here per house
convention, flag don't silently fix):** the Phase-1 proposal's own §2a
formula chain used `D_SP(r)*tan(35°)` inside the NY-sizing "coverage
margin" term. Since this experiment's angle set never exceeds ±35°
(unlike exp-024/026's inherited ±40°-sized domain), this is in fact the
*more* correct, purpose-built choice for exp-030's own geometry — not a
bug to fix — but it means the formula's own r=78 output (NY≈1528, if it
were evaluated) does **not** reproduce exp-024's actual established
NY=1584 (which was sized for the now-abandoned ±40° primary geometry and
inherited unchanged through exp-026). This is expected and immaterial: the
r=78 point is entirely REUSED (no new geometry is built for it), and the
formula is only trusted to build r=156/312's genuinely new domains — where
its (deliberately tighter, purpose-built) margin is validated directly by
mandatory fix 5's own δ_C floor check at r=156, rather than assumed by
analogy to legacy practice. Flagged here as an idealization, not silently
smoothed over.

## Setup (pinned by `design_geometry.py` — re-run it if any constant moves)

| Knob | Value |
|---|---|
| r-family | 78 (REUSED, 0 new runs) / 156 (NEW) / 312 (NEW) |
| PLANE_DX | 15 cells, FIXED across the family (not self-similar) — maximizes the z/z_R dynamic range the fit needs |
| λ / cpl | 600 nm / 20 (single-λ scope) |
| Domain (r=156) | 660×2480, STEPS=2706 |
| Domain (r=312) | 1260×4264, STEPS=5317 |
| Angles | FALLBACK_ANGLES (±35,±25,±15,±5,0), N=9 — all articles @ r=156; PEC+absorber @ r=312. N5_SUBSAMPLE (±35,±15,0,15,35) — off_lab/off_field @ r=312 only |
| Articles | absorber (`graded_black_shell`, r_in=round(30κ), σ_max=0.5/κ — fix 2) · PEC (`pec_disk`) · off_lab (τ=0.008, σ held fixed) · off_field (τ=0.032, σ held fixed) |
| C(z/z_R) model | C = C_∞ + B·√(z/z_R), fit exactly on (r=156, r=312); r=78 held out as a free validation point |
| Witness z/z_R | z_w·λ/r_w² (z_w=45m, r_w=0.5–1.5m, λ=550nm docket #7) → central 2.475e-5, band [1.1e-5, 9.9e-5] |
| T11 companion | box_dev on the beam-scene bench (established τ=3.9 uniform ON disk), r=78 (1 run, confirmatory) + r=156 native+cpl×1.5 (4 runs); r=312 OPTIONAL, falls back to It.8 |
| R-gate | flat-coating reflectance re-check at each new (σ_max, thickness) — fix 2/Red Team #8 |
| δ_C floor check | @ r=156, reusing Block-1 empty captures — Red Team #6 |
| Settling diagnostic | doubled STEPS @ r=156, absorber, λ=600nm — Red Team #9 |
| Run count | Block 1: r=156 (45) + r=312 (37) = 82. T11: 5 (r=78+r=156). Settling: 2 extra beam runs. **Total committed: ~89 new FDTD sim calls.** |

## Predictions (committed before this file's first FDTD run)

**Gate-relevant / pre-run diagnostics:**

- **P-VISION-R1 (R-gate, fix 2/Red Team #8):** flat-coating R_coat ≤ 0.2%
  at every r in {78,156,312} with the rescaled σ_max — the coating stays
  broadband-black once optical depth is held constant. *(Run FIRST, before
  any Block-1 result is trusted — a failure here would mean the graded
  shell's own R≤0.2% pedigree does NOT transfer under the rescaling, and
  the absorber's own C(z/z_R) numbers would need re-interpretation.)*
- **P-VISION-F1 (δ_C floor, Red Team #6):** |C_empty| at r=156 (±35°
  fallback, NY sized by exp-030's own tighter, purpose-built margin rule)
  stays ≤ 0.005 (the program's own lab-bar decision-floor convention) —
  confirming the floor collapses at r=156 the way it did at r=78's ±35°
  fallback, licensing P-VISION-3's PASS/FAIL language. A miss here means
  no PASS/FAIL language is licensed at r=156/312 regardless of what Block
  1 itself measures, and the domain would need widening in a follow-up.
- **P-VISION-S1 (settling, Red Team #9):** doubled-STEPS C at r=156
  (absorber, θ=0) differs from the native-STEPS reading by ≤ 0.01 in C —
  confirms `STEPS_AMBIENT(r)`'s linear D_SP-ratio scaling is adequate,
  closing the question rather than leaving it argued.

**The bridge fit (Block 1, T8):**

- **P-VISION-1 (functional-form validation, the gate before any
  witness-scale belief):** the (r=156, r=312)-only fit's implied C(78)
  reproduces the corrected established C(78) within **0.03** for both
  absorber and PEC → sqrt-law validated. Miss in (0.03, 0.08] → widened
  error bars, no witness-scale verdict language. Miss > 0.08 → sqrt-law
  REJECTED for these articles; a linear alternative (see P-VISION-1b) or a
  4th r-point would be needed in a future cycle.
- **P-VISION-1b (shape discriminator):** [C(78)−C(156)] / [C(156)−C(312)]
  (using the CORRECTED C(78)) — sqrt-law (p=0.5) predicts **2.00 ± 0.3**;
  a linear law (p=1) predicts **4.00 ± 0.5**.
- **P-VISION-2 (deepening direction):** both absorber and PEC show
  monotonically MORE NEGATIVE C as r grows (C(78) > C(156) > C(312)).
- **P-VISION-3 (load-bearing, gated on P-VISION-F1 passing):** the
  near-threshold OFF-lab/OFF-field sponges show |ΔC(78→312)| ≤ **0.0010**
  (OFF-lab) / **0.0025** (OFF-field) — if confirmed AND P-VISION-F1
  passes, licenses PASS/FAIL language on these near-threshold C values for
  the first time in the program's history.

**T11 companion (box-ledger channel decision floor, redefined metric —
fix 4):**

- **P-VISION-T11-1** (r=78, box_dev, established convention): band
  [0.05%, 1.0%].
- **P-VISION-T11-2** (r=156, box_dev): band [0.05%, 1.5%], hypothesized
  roughly r-independent — falsified if > 3× the r=78 reading.
- **P-VISION-T11-3** (r=156, cpl×1.5 companion): shrinks to [0.65, 0.80]×
  the native (cpl=20) reading.
- **Consequence (computed in code, fix 4 — NOT hand-asserted):**
  box_dev(156)'s predicted band vs. T9's Δσ_abs/σ_ext=1.56e-6 and T10's
  6.49% spread — printed by `run.py::run_fit` at Phase-4 close, not
  pre-committed as a specific ratio (both the proposal's and
  THERMODYNAMICS' own hand-computed ratios were independently found wrong
  by Red Team; the honest commitment here is "computed in code," not a
  specific number).

## Idealizations (lab convention, carried from Phase 1 + Phase 2/Red Team)

2D TMz, single polarization, single λ=600nm scope. PLANE_DX fixed (not
self-similar) — samples a different relative near-field depth at each r,
by design. 2-point exact fit; r=78 held out, not fit. Extrapolation gap:
sampled z/z_R∈[0.0031,0.049], witness scale is 1.5–2.5 decades beyond the
smallest sampled point — a real, stated extrapolation risk the sqrt-law's
physical motivation (Fresnel-zone diffraction scaling) partially
mitigates, does not eliminate (EM's Phase-2 note: no independent
disk-diffraction-theory derivation of this exact exponent is offered;
P-VISION-1's own held-out check is the actual validation, not the
formula's pedigree). `graded_black_shell` scaling now holds radial optical
depth constant (fix 2), not the original proposal's held-σ_max reading —
MATERIALS' realizability caveat (the literal r_in/r_out self-similar
construction is unobtainium — 0.31–0.92m coating thickness [corrected
post-Phase-5, see §Results — the original 0.6–1.9m figure was a real
unit error, witness radius misread as diameter] — at witness scale; a
real ultra-black coating's thickness is independent of substrate
size) is on the record here, not resolved. T11 measures the beam-scene
box-ledger channel (single-source, T9/T10's own usage) — explicitly a
DIFFERENT instrument from the ambient bench, and (Red Team's fix 4) now
explicitly flagged as measuring a DIFFERENT ARTICLE than T9's own
(uniform-conductivity ON disk vs. `graded_black_shell`) — box_dev is a
floor on T11's own channel/article, a same-run/cross-box quantity, and
should not be read as automatically transferable to T9's or T10's own
cross-run/cross-article comparisons (THERMODYNAMICS' Phase-2 point,
preserved). T11's r=312 leg is explicitly optional/cost-gated, deferred to
Iteration 8 if scope pressure emerges. No coherent-superposition
interaction (Iteration 6's own machinery, untouched — QUANTUM's Phase-2
review confirmed the incoherent-ensemble analytic-zero result generalizes
to any r_out, so scaling this bench cannot reintroduce a coherence
artifact). Graded damping bands, not PML, throughout.

## Results

**89 new FDTD sim calls, ~5.1 hours total wall-clock** (Block 1 @ r=156:
45 runs, 1780s; Block 1 @ r=312: 37 runs, 13946s ≈ 3.87h — nearly 8×
longer than the Phase-1 proposal's own hand estimate, the single largest
timing miss in this program's history, driven by κ³ FDTD cost scaling
that the proposal's own §7 correctly flagged in kind but underestimated
in magnitude; settling diagnostic: 2 runs; T11: 3 runs; rgate + timing
pilot: zero/one extra runs). Full raw data: `results.json`.

**Pre-run diagnostics — all three CONFIRMED:**

- **P-VISION-R1 (R-gate):** R_coat ≈ 0 (order 1e-5: −2.9e-7 / −4.9e-5 /
  +... at r=78/156/312) at every r — the σ_max=0.5/κ rescale preserves
  the coating's broadband-black behavior exactly as fix 2 requires.
  Bare-wall sanity check reproduced stage7's own R≈0.98 baseline
  (measured 0.978), confirming the test rig itself.
- **P-VISION-F1 (δ_C floor):** r=156: **−0.00121** (≤0.005 gate, clean).
  Also checked at r=312, beyond the mandatory-fix's own minimum
  requirement: **−0.00028** (N9) / **−0.00024** (N5) — even cleaner than
  r=156. The floor collapses at both new geometries; P-VISION-3's
  PASS/FAIL language is licensed at both.
- **P-VISION-S1 (settling):** native C = −0.83412, doubled C = −0.83412
  — identical to 5 decimals. `STEPS_AMBIENT(r)`'s linear scaling is
  amply adequate; no settling artifact at this geometry.

**The bridge fit (Block 1, T8) — a genuinely mixed result, reported
honestly:**

| Article | C(78) est. | C(156) | C(312) | Fit C_∞ / B | C_pred(78) | miss | shape ratio |
|---|---|---|---|---|---|---|---|
| Absorber | −0.7209 | −0.7305 | −0.7323 | −0.7341 / +0.0324 | −0.7269 | **0.0060** | **5.33** |
| PEC | −0.8673 | −0.8698 | −0.8659 | −0.8620 / −0.0702 | −0.8776 | **0.0103** | **−0.635** |

- **P-VISION-1 (functional-form validation):** both articles pass the
  ≤0.03 miss gate (absorber 0.0060, PEC 0.0103) — nominally CONFIRMED.
  **But PEC's pass is not a clean validation** — see P-VISION-2 below;
  a 2-parameter fit landing near a 3rd point doesn't mean the underlying
  curve is well-described by *any* smooth 2-parameter law when that curve
  isn't even monotonic.
- **P-VISION-1b (shape discriminator) — REFUTED for both articles, in
  different ways.** Absorber's ratio (5.33) sits outside BOTH the
  sqrt-law band (2.00±0.3) AND the linear-law band (4.00±0.5) — the true
  r=78→156 drop is sharper, relative to r=156→312, than either simple
  power law predicts. PEC's ratio is **negative** (−0.635) — only
  possible if C(78)→C(156) and C(156)→C(312) move in OPPOSITE
  directions, which they do (see next item). Neither article's
  discriminator behaves as either candidate law predicts.
- **P-VISION-2 (monotonic deepening) — CONFIRMED for the absorber,
  REFUTED for PEC, a genuine surprise.** Absorber: −0.7209 → −0.7305 →
  −0.7322, cleanly monotonic. **PEC: −0.8673 → −0.8698 (deepens) →
  −0.8659 (SHALLOWS again, ending up less negative than even the r=78
  point)** — non-monotonic, not predicted by any seat in Phase 1 or 2.
  Per this program's own R3 meta-rule ("any surprising feature gets a
  resolution check before a mechanism debate"), this is flagged as an
  open question for Phase 5/a future iteration, not interpreted here —
  candidates include a genuine near-to-far transition feature specific
  to a hard reflector (PEC has no rim-transmission channel to smooth
  the trend, unlike the absorber), a grid-quantization effect at the
  r=312 domain's much larger cell count, or an artifact of the δ_C floor
  (clean, but not identically zero) beginning to matter at PEC's much
  larger |C|. **Not yet explained — a new candidate live thread.**
- **P-VISION-3 (load-bearing, sponge scale-robustness) — CONFIRMED
  cleanly for both articles.** OFF-lab |Δ(78→312)| = **0.00031** (≤0.0010
  gate). OFF-field |Δ(78→312)| = **0.00046** (≤0.0025 gate). Combined
  with P-VISION-F1's clean floor at both r=156 AND r=312: **PASS/FAIL
  language is now licensed on the near-threshold OFF-lab/OFF-field C
  values for the first time in this program's history** — the load-
  bearing deliverable of this whole cycle, delivered cleanly.

**T11 companion (box-ledger channel decision floor):**

| Point | box_dev (established convention) |
|---|---|
| r=78 | 0.0365% |
| r=156, native cpl=20 | 0.0376% |
| r=156, cpl=30 (×1.5) | 0.0696% |

- **P-VISION-T11-1/T11-2 — REFUTED (both read below the predicted
  bands), but the underlying hypothesis they were built to test HOLDS.**
  Both r=78 (0.0365%) and r=156 (0.0376%) read below the predicted
  [0.05%,1.0%]/[0.05%,1.5%] floors — a genuine miss on the absolute
  band. But the actual scientific question — is box_dev roughly
  r-independent? — is answered cleanly: the two readings agree to 3%
  relative (ratio 1.03), far inside the ×3 falsification threshold.
- **P-VISION-T11-3 — REFUTED, in the surprising direction.** The cpl=30
  companion measured 0.0696%, a **1.85× GROWTH** over native (0.0376%),
  not the predicted 0.65–0.80× shrink. This is the opposite of every
  established R3 (resolution-refinement) precedent in this program
  except one: **T10's own exp-027 finding, "the R3 check can ENLARGE a
  feature, not just confirm/refute it"** — previously a lone exception
  across 6 prior R3 applications, now possibly a second instance, on a
  *different* channel (box_dev vs. `BEAM_BEHIND`). Not yet interpreted;
  flagged for Phase 5 as a genuine, real miss, not smoothed over.
- **T9/T10 floor consequence, computed in code (fix 4):** using the
  measured box_dev readings, T9's established Δσ_abs/σ_ext=1.56×10⁻⁶
  sits **234–446× BELOW** the measured floor at every point tested —
  decisively, robustly null, not a floor-limited reading. T10's
  established 6.49% box-ledger spread sits **93–178× ABOVE** the same
  floor — decisively a real signal, not floor noise. **Both T9 and T10
  now have their first-ever floor-referenced verdict** (previously
  informal magnitude arguments only) — T11's own founding purpose
  delivered, even though the specific predicted bands (P-VISION-T11-1/2)
  themselves missed.

## Honest summary

The mandatory, five-times-deferred r=156 build **executed in full this
cycle** — the pre-registered Checkpoint-4 tripwire does not fire. The
cycle's single biggest deliverable — PASS/FAIL language now licensed on
the program's own near-threshold constraint-3 C values — landed cleanly.
T9 and T11 both close out with real, floor-referenced verdicts for the
first time. Against that: the functional-form question this whole build
exists to answer (does C(z/z_R) follow a clean, single-exponent power law
bridging bench to witness scale?) comes back **genuinely mixed** — the
absorber's shape doesn't match either candidate law tightly, and PEC is
flatly non-monotonic, an unpredicted surprise needing its own resolution
check before any witness-scale number for PEC specifically should be
trusted. T11's own resolution companion also missed, in the same
direction as this program's one prior "R3 enlarges" exception. Two new,
concrete open questions for a future cycle, neither of which erases this
cycle's own real deliverables.

## Phase 5 — post-hoc findings (full verbatim record: LOGBOOK.md
## Iteration 7)

Six fresh seats + Red Team audit. **Director's verdict: PARTIAL** (not
RULED OUT — nothing forecloses a mechanism; not PROMISING — the central
technical question, does C(z/z_R) bridge cleanly to witness scale, comes
back genuinely unresolved). Two corrections landed in this file this
shift (flagged, not silently rewritten): the MATERIALS realizability
figure (§ above, 0.31–0.92m not 0.6–1.9m — a real unit error caught by
Red Team) and the sponges' r=156 reading (below).

**The most consequential Phase-5 finding, caught by NONE of the six
blind seats, only by Red Team's audit:** this cycle's own witness-scale
extrapolation (absorber C_pred(witness)≈−0.734, PEC≈−0.862, essentially
flat across the ENTIRE committed witness uncertainty band) sharply
contradicts the |C|≈0.98 estimate that has justified prioritizing this
exact thread across five iterations — the two numbers were never
compared side by side anywhere in this program's record until now. The
Director's own added reading: the fitted C_∞ is the model's z/z_R→0
asymptote, and physically an opaque silhouette's contrast should
approach C→−1 in the true far field, not saturate short of it — a
structural, not just numerical, mismatch. New live thread **T13**
opened for this; see LOGBOOK.md.

**Second finding:** the sponges' apparent r=156 "excess deepening" is
mostly **instrument bias, not a real effect** — the r=156 δ_C floor
(−0.00121, ~4.3× larger than r=312's) explains 87–97% of each sponge's
own r=156 excursion from a linear 78↔312 interpolation (doesn't touch
P-VISION-3's own gate, which correctly uses only the floor-clean 78/312
endpoints). PEC's own excursion is only ~38% explained the same way —
consistent with a real mechanism (Fresnel-zone ripple, independently
proposed by PHOTONICS and EM) operating on top, not instead. New live
thread **T12** opened for PEC's non-monotonicity.

**Program-integrity statement (Red Team's own demand, stated explicitly
per house convention):** PASS/FAIL language is now decidable — a real,
earned instrument achievement. **But no σ(I) OFF-state article this
program has ever built has PASSed constraint 3 at any tier, at any
scale.** OFF-lab is MARGINAL everywhere (0.00548–0.00681, never below
the 0.005 bar); OFF-field is FAIL everywhere (0.02174–0.02336, never
below the 0.02 bar). This cycle characterized the instrument; it did not
find, or bring closer, a working escape route.

**New Checkpoint-4 tripwire, adopted:** any future citation of this
cycle's witness-scale C_pred numbers without flagging the T13
discrepancy, or any treatment of PEC's fit/witness number or box_dev as
a settled floor before their own R3 checks resolve, is a retroactive
criterion-4 trigger.
