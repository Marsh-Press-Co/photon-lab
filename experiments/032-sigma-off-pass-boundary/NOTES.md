# exp-032 — The σ(I) OFF-State PASS-Boundary Run

Panel Iteration 9. Lead seat: **MATERIALS & METAMATERIALS** (rotation), executing
Iteration 8's binding, Red-Team-ranked, three-times-deferred Iteration-9
priority (LOGBOOK.md Iteration 8 close; PLAN.md Next-work queue item (1)).
Full seven-seat cycle: Phase 1 proposal (MATERIALS) → 5 blind parallel
critiques (PHOTONICS, ELECTROMAGNETISM, THERMODYNAMICS, QUANTUM OPTICS,
VISION SCIENCE — all support-with-changes) → Red Team last with everything
(verdict: proceed-with-mandatory-fixes) → Phase 3 synthesis (this file) →
predictions committed → Phase 4 run. Full verbatim transcript: LOGBOOK.md
Iteration 9.

## Hypothesis

VISION's frozen perceptual ladder (T2: PASS |C|<0.005, MARGINAL
0.005–0.02, FAIL ≥0.02, sourced Blackwell 1946 + CIE 19/2 1981) has never
once been cleared by any σ(I) OFF-state article this program has built —
exp-026's off_lab (τ=0.008) and off_field (τ=0.032), and exp-030's
r=78/156/312 re-measurement of both, are MARGINAL or FAIL everywhere. The
established linear transfer constant g=|C|/τ (0.576–0.691 across 3λ,
exp-026 off_lab) predicts that a weaker OFF-state article, τ_off≈0.0065,
would cross the PASS line for the first time (C≈g·0.0065, ≈0.0037–0.0045,
below 0.005) — **if** the linear g-transfer model extrapolates cleanly
below its own validated range (τ∈[0.008,0.10]). This run tests exactly
that extrapolation, at the cheapest possible cost (reusing an
already-validated bench verbatim), and — per Red Team's mandatory Phase-2
fix — adds a second, lower-τ bracket point specifically to discriminate
whether the extrapolation is safe (bulk-absorption-dominated, g flat as
τ→0) or unsafe (edge/rim-scattering-floor-dominated, g rises as τ→0,
per T9's established rim-transmission mechanism).

**This is instrumentation of the σ(I) escape route's OFF-state endpoint
only — not a working mechanism.** Both articles are ordinary static,
linear, time-invariant media (σ fixed, real, non-dispersive). Neither
this run nor any prior σ(I) cycle has built an actual intensity-dependent
conductivity function. Whether any real medium can gate σ between
τ_off≈0.0065 and the established τ_on≈3.9 ON endpoint (a ratio of ≈600×,
*worse* than exp-026's already-unobtainium 122–487×, precisely because
chasing the PASS line pushes τ_off lower) remains T1's separate,
unresolved central tension — UNOBTANIUM-WITH-PARAMETERS, standing since
Iteration 2 Phase 5, unmoved by this run's outcome either direction.

## Phase 1 — Proposal (MATERIALS, summary; full text LOGBOOK.md Iteration 9)

One new uniform-conductivity, index-matched (ε_r=1, no PEC core) sponge
disk at τ_off≈0.0065, on exp-026's exact ±35° N=9 fallback ambient bench
(r_out=78, NX=360, NY=1584), scored against VISION's frozen ladder at all
3λ. Six falsifiable predictions (P-MAT-1 through P-MAT-6), a realizability
bound (τ_off≈0.0065: PUBLISHED, weaker than either already-PUBLISHED
off_lab/off_field endpoint; the switching mechanism: UNOBTANIUM-WITH-
PARAMETERS, unchanged by this run), and an explicit statement that a PASS
result *sharpens*, not eases, T1's central tension (the σ_on/σ_off ratio
grows to ≈600×).

## Phase 2 — Critiques (five seats, blind, summary; full text LOGBOOK.md Iteration 9)

All five: **support-with-changes**. Three seats (PHOTONICS, ELECTROMAGNETISM,
QUANTUM OPTICS) independently converged, via three different framings, on
the same core issue: the proposal's central g-transfer constants (g450,
g600 especially) are exp-026's own *documented band-misses* — g450
plausibly floor-biased low (SNR≈5.2, its thinnest channel), g600
explicitly "NOT floor-explicable... genuinely unexplained" (its cleanest
channel, SNR≈79–167) — extrapolated below their entire tested range at
the thinnest SNR this program's σ(I) line has ever attempted (≈4.2 at
450nm). VISION separately attacked the proposal against VISION's *own*
frozen scale-bias rule (idealization iii: near-invisible |C|<0.1 readings
are not robust at this ~10λ bench) and proposed a companion r=156 leg.
THERMODYNAMICS flagged a missing energy-sidecar sentence (continuous
ambient illumination still deposits a real, non-zero absorbed fraction,
even with no beam-scene channel).

## Phase 2 — Red Team (last, with everything; full text LOGBOOK.md Iteration 9)

**Verdict: proceed-with-mandatory-fixes.** Independently verified every
quantitative claim above against `results.json`/code — all confirmed
accurate. Found the convergent g-transfer concern real and load-bearing,
but **not** best fixed by PHOTONICS' own proposed bridging point (τ≈0.012
sits *above* the already-validated τ=0.008 floor — a real arithmetic
error in that critique, caught by none of the other four seats): the
correct fix is EM's own proposal, a bracket point *below* τ_off
(τ≈0.003), which actually discriminates the two live hypotheses (bulk vs.
edge-scattering-floor mechanism). Also found: a band mismatch between the
proposal's own P-MAT-1 (C-band from g∈[0.55,0.7692]) and P-MAT-2 (g-band
[0.50,0.80]) that none of the five blind critiques caught; VISION's
scale-bias attack is real but not fatal (the proposal's own §5 hedge is
substantively adequate, just inconsistently repeated at the headline
sentences — the *second consecutive cycle* this exact documentation
pattern has appeared, after exp-031); VISION's proposed r=156 companion
leg is legitimate but not free (single-λ-only apparatus, worse SNR than
this run's own worst channel) and repeats a request the Director already
resolved identically at Iteration 3 — queue for Iteration 10, don't fold
in now; THERMODYNAMICS' fix is genuinely distinguishable from the
Iteration-5 no-op pattern *provided* it shows real arithmetic, not just
an assertion.

## Phase 3 — Synthesis (Director)

**Accepted, folded into this run's design:**

1. **EM's mandatory bracket point** — a second article, `off_bracket`
   (τ=0.003), same geometry, same run batch. Corrects/supersedes
   PHOTONICS' mislabeled τ≈0.012 suggestion (accepted in spirit — a
   below-floor discriminator is needed — overridden in specific value,
   per Red Team's catch that 0.012 doesn't bracket anything below
   τ_off=0.0065).
2. **QUANTUM's disposition clause** — adopted verbatim, zero cost: if
   `off_pass`'s own measured g600 continues off_lab's established
   unexplained-high pattern (≥0.69), the 600nm reading is flagged
   `anomaly_consistent` in `results.json` and must not be read as an
   unqualified clean PASS even if it numerically clears 0.005.
3. **THERMODYNAMICS' energy sidecar** — computed in code
   (`thermo_sidecar_analytic` in `results.json`), showing the actual
   τ_off/τ_on ratio and optically-thin absorbed-fraction estimate against
   the established ON-article σ_abs/σ_ext anchor (0.6056–0.6083) — labeled
   explicitly POST-RUN ANALYTIC, NOT AN FDTD OUTPUT (THERMO's own
   expressibility contract).
4. **Red Team's g-band harmonization** (attack #2) — P-MAT-1 and P-MAT-2
   below both now score against one shared band, `G_BAND=(0.50,0.80)`,
   applied identically to both articles.
5. **Red Team's documentation-placement fixes** (attacks #6, #8) — the
   scale-bias hedge (this is a bench-scale diagnostic, not a Tier-W/A
   constraint-3 verdict; measured |C| here is explicitly a lower bound on
   real-scale |C| per VISION's own idealization iii) and the realizability
   cross-reference (a PASS *sharpens*, not eases, the σ_on/σ_off gap) are
   both restated inline in this file's Hypothesis section above, not left
   to live only in a buried idealizations paragraph — closing the same
   pattern Red Team flagged as now recurring for a second consecutive
   cycle (after exp-031). **Third consecutive occurrence of this pattern
   is elevated to a program-level documentation-discipline finding, not a
   per-cycle nit, if it happens again** — carried into Phase 5 as an
   explicit thing for future leads to check before freezing predictions.

**Overridden, with reasons (both explicitly queued, not silently dropped):**

6. **VISION's r=156 companion leg** — NOT built this cycle. Red Team's
   analysis is adopted verbatim: the r=156 apparatus (exp-030/031) is
   validated at 600nm only, its own δ_C floor (0.001211) is a
   single unrepeated measurement, and a companion leg there would land at
   SNR≈3.7 — *worse* than this run's own worst channel (4.2 at 450nm),
   not better. It would not de-risk the SNR concern; it would move the
   same concern to a thinner-margin, less-validated instrument. This is
   the identical class of request the Director already resolved at
   Iteration 3 (exp-026), overriding it there for the same reason
   (same-cycle geometry-redesign scope, not a same-cycle rider). **Queued
   explicitly for Iteration 10**: the same τ_off≈0.0065/τ_bracket≈0.003
   pair at r=156, 600nm only (matching that bench's own validated scope),
   scored as its own scale-bridge companion to this cycle's r=78 result.
7. **PHOTONICS' specific τ≈0.012 bridging point** — overridden as
   literally specified (Red Team's catch: it sits above the already-
   validated floor, testing already-known territory, not the
   extrapolation region). Superseded by EM's τ=0.003 bracket point, which
   tests the actually-relevant hypothesis space.

## Setup — parameter table (final, post-synthesis)

Geometry inherited verbatim from exp-026's ±35° fallback bench — see
`design_geometry.py` for the full constant block (identical to exp-026's:
NX=360, NY=1584, ABSORB=40, CPL={450:15,600:20,750:25}, SRC_X=300,
TAPER=40, R_OUT=78, OBJ=(170,792), PLANE_DX=15, PLANE_X=77, W_OBJ=78,
GUARD_OUT=185, W_FLANK=78, BOX=(80,260,702,882), FALLBACK_ANGLES=N=9
±35°, DECISION_FLOOR reused {450:0.00089, 600:0.00007, 750:0.00045}).

| Article | τ_center | σ_engine | Construction |
|---|---|---|---|
| `off_pass` | 0.0065 | 4.16667×10⁻⁵ | uniform disk, no PEC core, ε_r=1.0, single hard σ-step |
| `off_bracket` | 0.003 | 1.92308×10⁻⁵ | uniform disk, no PEC core, ε_r=1.0, single hard σ-step |

**Run plan:** 2 articles × 9 angles × 3λ = 54 object runs + 27 empty runs
(shared across both articles, same (angle,λ) grid) = **81 new FDTD calls**,
≈4 min at exp-026's own measured rate (108 calls/329s ≈ 3.05s/call). No
beam-scene channel this run (out of scope: τ_off is definitionally the
non-beam-terminating endpoint; ON-article beam behavior is exp-026's
already-published job, not remeasured here). No new `lab/` engine code —
trust suite unaffected, already 46/46 green pre-flight this shift.

## Predictions — committed BEFORE any run (house discipline, non-negotiable)

**P-MAT-1 (off_pass, per-λ ambient Weber contrast C, N=9 fallback, all 3λ).**
Central (established off_lab g carried down): C_450=−0.00374,
C_600=−0.00449, C_750=−0.00411. Band (G_BAND=[0.50,0.80], harmonized with
P-MAT-2): **C ∈ [−0.00520, −0.00325]** at every λ. Exhaustive disposition:
(a) all 3λ land |C|<0.005 → clean PASS *pending* the QUANTUM disposition
check on 600nm (see P-MAT-5, below) before it may be reported unqualified;
(b) 1–2 of 3λ land |C|<0.005, rest in [0.005,0.02) → chromatic partial
PASS, not white-light-flat; (c) all 3λ land ≥0.005 → PASS-boundary
prediction REFUTED — the linear g-transfer law breaks down below τ=0.008,
or true g at this τ exceeds 0.80.

**P-MAT-2 (off_bracket, per-λ ambient Weber contrast C, N=9, all 3λ).**
Central: C_450=−0.00173, C_600=−0.00207, C_750=−0.00189. Band
(same G_BAND=[0.50,0.80]): **C ∈ [−0.00240, −0.00150]**. Pre-registered
SNR risk: 450nm sits at SNR≈1.94 against the reused decision floor —
thinner than any channel this program has ever scored — **informational
only at 450nm, not a scored gate**; 600nm (SNR≈29.6) and 750nm (SNR≈4.2)
are the scored discriminators for this article.

**P-MAT-3 (g=|C|/τ transfer constant, per article per λ — tests whether
the linear regime extends below τ=0.008, and in which direction it
breaks if it does).** Central: same per-λ g's as off_lab
(0.576/0.691/0.632) at both τ. Band: g∈[0.50,0.80] at every λ, both
articles. **Discriminator (Red Team's mandatory addition):** if
`off_bracket`'s g is materially HIGHER than `off_pass`'s at the same λ
(beyond N9-vs-N5 convergence noise, see P-MAT-6), that is evidence for
the edge/rim-scattering-floor mechanism (g rises as τ→0) over the
bulk-absorption-dominated model this run's central predictions assume —
in which case P-MAT-1's own PASS reading, even if numerically achieved,
should be read as an extrapolation artifact of a breaking model, not
confirmation the model holds at this τ.

**P-MAT-4 (chromatic spread, |C(750)−C(450)|, wavelength-flatness,
each article separately).** Central: 0.0003–0.0007 (off_pass), 0.0001–
0.0003 (off_bracket, scaled by τ). Band: [0.0, 0.0015] and [0.0, 0.0010]
respectively.

**P-MAT-5 (QUANTUM's mandatory disposition clause, off_pass/600 only).**
If measured g600(off_pass) ≥ 0.69 (continuing off_lab's own established,
unexplained-high g600=0.6913 miss), the 600nm reading is flagged
`anomaly_consistent` in `results.json` and P-MAT-1's disposition (a) may
NOT be reported as an unqualified clean PASS at 600nm — it must be stated
as "PASSes numerically, anomaly-consistent, not yet distinguishable from
the same unexplained drift exp-026 already flagged."

**P-MAT-6 (N-convergence, N5 vs N9, off_pass@600, zero new runs, exp-026's
own P-MAT7 idiom).** |ΔC| ≤ 0.001, central ≤0.0006 (exp-026's own
confirmed value at a comparable-magnitude article was 0.0005).

**P-MAT-7 (THERMODYNAMICS' energy sidecar, post-run analytic, off_pass
only — NOT an FDTD output, expressibility contract).** Optically-thin
absorbed-fraction-of-intercepted-flux estimate ≈ τ_off ≈ 0.65%; expressed
relative to the ON article's own established σ_abs/σ_ext anchor
(0.6056–0.6083, τ=3.9) via the ratio τ_off/τ_on_established ≈ 0.00167
(≈0.167%) — computed in code (`thermo_sidecar_analytic`), not merely
asserted, per Red Team's mandatory condition. No detectability claim
beyond "orders of magnitude below the already-established ON-article
scale" — ΔT/emission-band chain stays blocked on docket #7's still-missing
witness-scenario watts, exactly as recorded since Iteration 1.

**P-MAT-8 (overall verdict against VISION's frozen ladder — scored per
exp-031's own established diagnostic convention, P-DIR-3: this is a
bench-scale diagnostic, NOT a Tier-W/Tier-A constraint-3 verdict; VISION's
own idealization iii — measured |C| at this ~10λ bench is a lower bound
on real-scale |C|; near-invisible readings |C|<0.1 are explicitly not
robust — applies to every number this run produces).** Central prediction:
`off_pass` clears PASS at all 3λ, pending P-MAT-5's disposition check;
`off_bracket` is a discriminator run, not itself scored against the
ladder as a headline (its own numbers are expected well inside PASS by
construction — its job is P-MAT-3's g-trend question, not a second PASS
claim).

## Idealizations

2D TMz, single polarization. Static/linear/time-invariant media
throughout — no σ(I) built in either article; this measures only the
hypothesized OFF-state static endpoint(s), no trajectory or gating claim
between OFF and ON. CW single-λ, 3-λ quadrature standing in for white
light; incoherent-sum idiom unchanged (`lab/ambient.py` untouched).
Back-lit ambient only — no beam-scene channel this run. ±35° N=9 fallback
geometry — inherits T7's still-open angle-specific residual-floor question
(±40° dropped, mechanism still unexplained) and every idealization
exp-024/026 already logged at this bench: chord-model bands are
geometric-optics (straight-ray Beer–Lambert, no diffraction term); ε_r
pinned at exactly 1.0 is zero *index-step* reflection by construction but
NOT zero reflection overall — the abrupt σ-step is its own scattering
channel (T9's rim-transmission mechanism, the live hypothesis P-MAT-3's
bracket-point comparison tests directly).

**Scoring against VISION's frozen ladder is a bench-scale diagnostic
(P-DIR-3 convention), NOT a witness-scale or Tier-W/Tier-A constraint-3
verdict.** Measured |C| at this ~10λ bench is a lower bound on real-scale
|C| (VISION's own idealization iii, Iteration 1) — any near-invisible
reading here (both articles' predicted centrals sit at |C|<0.1) is
explicitly *not* robust to that scale bias without VISION's own r=156
scale-bridge check, still unbuilt after eight further cycles and
explicitly queued (not silently dropped) for Iteration 10 as this run's
own companion leg.

**A PASS result here does not mean a real σ(I) medium can be built.** It
would mean only that a static, linear τ_off≈0.0065 object's contrast, at
this one bench geometry, crosses a perceptual threshold — a materials
fact, not a mechanism demonstration. If `off_pass` PASSes, the implied
σ_on/σ_off ratio any real intensity-gated switch would need to span grows
to ≈600×, *worse* than exp-026's already-unobtainium 122–487×, precisely
because chasing the PASS line pushes τ_off lower. This sharpens, not
eases, T1's central tension — the standing UNOBTANIUM-WITH-PARAMETERS
verdict (Iteration 2 Phase 5) is unmoved by this run's outcome either
direction.

## Result

*(to be filled in after Phase 4 run)*

## Learned

*(to be filled in after Phase 5 review)*

## Next

*(to be filled in after Phase 5 review)*
