# exp-033 — The g600 Resolution Check (Block A only)

Panel Iteration 10. Lead: **ELECTROMAGNETISM** (rotation). Runner: cloud panel
shift, 2026-08-15. Full seven-seat cycle recorded verbatim in LOGBOOK.md
Iteration 10; this file is the experiment-local record — hypothesis, setup,
idealizations, and the predictions committed to git **before** any run
(house discipline, non-negotiable).

## Hypothesis

Iteration 9 closed with a live thread (T1's own carried-forward item): a
"g600 ≥ 0.69" reading recurs across four σ(I) OFF-state ambient points, all
sharing an untested grid resolution at 600 nm (the one wavelength on this
bench line never R3-checked). PLAN.md's Iteration-10 queue ranked closing
this first.

ELECTROMAGNETISM's Phase-1 desk analysis (verified independently by three
Phase-2 seats plus Red Team, to the last digit) found that the "recurrence"
dissolves once the empty-scene decision floor is subtracted additively: all
twelve previously-published (τ, λ, cpl) points collapse onto one
resolution-scale-independent constant, g₀ ≈ 0.689, via
g_corr = |C_scene − C_empty| / τ. The raw g600 ≥ 0.69 reading is g₀ showing
through at the one wavelength whose floor happens to be near zero — not
distinct physics.

**exp-033 tests whether that desk collapse survives a real resolution
change (cpl 20→30) at 600 nm**, the actual R3 check Iteration 9 queued —
now run in the *g_corr* currency the desk analysis motivates, with the
disposition pre-registered on the fit's own statistical properties, not on
where a single new number happens to land.

## Scope change from Phase 1, and why (Director's synthesis, Phase 3)

The Phase-1 proposal included a second block ("Block B"): `radial_absorbed_
power` applied to beam-scene versions of `off_pass`/`off_bracket`, testing
whether OFF-state absorption is bulk- or rim-dominated. **Block B is CUT
this cycle.** PHOTONICS' Phase-2 attack — independently confirmed by Red
Team's own direct computation — showed Block B as scoped cannot answer its
own question: the real bulk-vs-rim signal (max|ρ_k−1| ≈ 5.9×10⁻⁴ at
τ=0.0065) sits 17–34× below its own discriminator gates, and three of its
five predictions are geometry/normalization identities that confirm for
*any* uniform disk at any τ≪1 — Iteration 9's structural null, repeated
with a new instrument. Red Team's own ruling offered an explicit,
sanctioned fallback: fix Block B properly (PHOTONICS' τ=0.10 substitution +
`angular_scattered_pattern` readout + a re-derived analytic reference model
for the discriminator) *or* cut it and re-scope as a standalone cycle. Given
the risk of mis-implementing the re-banded discriminator under this cycle's
own time budget, the Director elected to cut it rather than risk shipping a
second broken instrument in one cycle. **Re-queued for a future standalone
lead cycle** (see Next, below) — not smuggled in here as an unreviewed
bolt-on, consistent with this program's own precedent (exp-028's Red Team
fix #6 on r=156).

## Phase 1 — Proposal (ELECTROMAGNETISM, verbatim, abridged to Block A)

See LOGBOOK.md Iteration 10 for the full verbatim Phase 1 text (both
blocks). Block A's desk table (all twelve points reproduced exactly by Red
Team from the committed `results.json` files):

| τ | 450 | 600 | 750 |
|---|---|---|---|
| 0.003 | 0.6886 | 0.6887 | 0.6870 |
| 0.0065 | 0.6875 | 0.6876 | 0.6860 |
| 0.008 | 0.6870 | 0.6872 | 0.6855 |
| 0.032 | 0.6798 | 0.6800 | 0.6784 |

g_corr = g₀(1 − (4/3π)τ), g₀ = 0.6889 ± 0.0002 (pooled, 12 points, imposed
curvature coefficient) — **the imposed coefficient is itself refuted by a
free fit** (see Phase 2, QUANTUM/Red Team). Free per-λ fit at 600 nm/cpl=20
(native): **A(g₀) = 0.689593, B = 0.299943**, max residual 6.5×10⁻⁶.

## Phase 2 — Critique (five blind, then Red Team) — summary

All five blind seats (PHOTONICS, MATERIALS, THERMODYNAMICS, QUANTUM OPTICS,
VISION SCIENCE) independently verified the desk arithmetic to the digit and
returned **support-with-changes**, each catching a distinct, orthogonal
defect. Red Team's verdict: **PROCEED-WITH-MANDATORY-FIXES**, catching two
further load-bearing defects none of the six blind seats found. Full
sixteen-attack verbatim record: LOGBOOK.md Iteration 10. Summary of what
changed the design (mandatory fixes, all accepted):

1. **[Red Team attack 1, LOAD-BEARING]** The Phase-1 proposal's Block-A
   parameter table specified articles by τ only, with no σ given — the
   exact precondition of exp-027's own historical T10 bug (a rescaled-
   geometry material constant computed downstream, silently drifting τ).
   **Fix:** σ pinned as an explicit number per article in
   `design_geometry.py`, with a runtime `assert` holding
   τ_center = 2·σ·r_out exactly for every article, checked at import time.
2. **[Red Team attack 5]** VISION's "unexplained ~2× drift" in the
   established 600 nm decision floor (0.00007 committed vs. 3.3166×10⁻⁵
   measured) is **not a drift at all** — exp-024's original committed table
   silently mixed weighting conventions (450 nm equal-weighted, 600/750 nm
   cos-weighted), while every scoring run since (exp-026/030/032) uses
   equal weights. **Fix:** `DECISION_FLOOR` corrected to the equal-weighted
   column {450: 8.8921e-4, 600: 3.3166e-5, 750: 4.3161e-4}. Erratum owed to
   LOGBOOK T7 and Iteration 9's carried-forward questions (recorded below).
3. **[Red Team attack 3]** The original 3-article design (off_bracket,
   off_pass, off_lab) left the fit exactly determined (3 points, 3 free
   parameters — zero residual, no diagnostic). **Fix:** off_field (τ=0.032,
   exp-026's third endpoint) restored, giving 4 points / 2 free parameters
   / 2 degrees of freedom and a real residual diagnostic.
4. **[Red Team attack 4, QUANTUM attack (ii), MATERIALS attack (1)/(2)]**
   The imposed (4/3π) curvature coefficient is refuted by a free fit on
   existing data (B/A = 0.435 vs. 4/(3π) = 0.424, a 2.5% miss, 35× the
   fit's own residual scatter — a *monotone* residual across all four τ,
   meaning the imposed model was already wrong before this cycle ran
   anything). **Fix:** the fit here is free (A, B both floated), never
   imposes 4/(3π); g₀ = A is reported as a **fitted bench-calibration
   parameter**, never a measured constant or mechanism signature.
5. **[Red Team attack 4]** The fit's own max residual is an extraordinarily
   sharp floor-error detector (a 2×10⁻⁴ floor shift inflates the clean
   3-parameter residual from 3×10⁻⁷ to 2×10⁻² — a >3000× amplification).
   **Fix:** gate the R3 disposition on the fit's own max residual
   (≤3×10⁻³ for the 4-article design) *before* trusting any comparison of
   the refit A against the established value — a zero-cost, self-produced
   data-quality gate.
6. **[Red Team attack 2/6, VISION P-VIS-0(ii)]** The original P-EM-1 band
   (±0.013 around g₀) was arithmetically unsatisfiable even at this
   bench's best-ever decision floor (native 600 nm floor alone already
   implies ΔA ≥ 0.0152, exceeding the band). **Fix:** rebanded to what the
   design can actually deliver (see Predictions, below), with INCONCLUSIVE
   pre-registered as a real, scoreable outcome — not a fallback invented
   after the fact.
7. **[Red Team attack 14, QUANTUM's own mandatory fix]** QUANTUM's
   Iteration-9 raw-g600≥0.69 disposition clause is **formally retired**
   here, before this run: under g_corr, every one of the twelve existing
   points sits at 0.678–0.689, **below** 0.69 — the clause would never have
   fired once the floor is subtracted. Numeric successor stated in
   Predictions, below.
8. **[Red Team attack 13, VISION P-VIS-0(i)]** The scoring currency is
   declared **before** the run: VISION's frozen ladder (|C|<0.005 PASS,
   <0.02 MARGINAL, else FAIL) is scored on **raw C only**. g_corr-corrected
   C is reported as a labeled sensitivity, **never substituted** for the
   scored quantity — applying the correction to published `off_lab` data
   flips its 450 nm reading from PASS (0.004607) to MARGINAL (0.005496),
   which is exactly the kind of currency-dependent verdict this program's
   own precedent (T13, Iteration 9's g600 clause) says must never be
   decided after the numbers land.
9. **[Red Team attack 9, MATERIALS' own load-bearing catch]** The ε_r ≡ 1.0
   idealization (index-matched host) is **load-bearing for constraints 2
   and 3**, not a background note: at a realizable condensed-phase index
   (n=1.33–1.5), two-surface ambient contrast alone is C = −0.040 to
   −0.078 (a VISION-ladder **FAIL**, 9–17× the entire off_pass signal),
   *independent of τ*, and specular return is 143–571× the established
   camera floor (a constraint-2 violation). **Fix:** stated explicitly
   here, in `design_geometry.py`, and at every point of use for g₀ and the
   PASS verdict — g₀ is a constant of a **gas/aerosol-host article only**
   (n−1 ≲ 10⁻⁵), never a material transfer function.
10. **[Red Team attack 10/11/12, THERMODYNAMICS' own mandatory fix]** A
    POST-RUN ANALYTIC energy sidecar (expressibility contract: not an
    FDTD output) is included per article (chord-averaged absorptance
    model, verified by Red Team to every quoted figure). The LWIR
    detectability claim for the ON-state endpoint (τ=3.9) is **held at
    hypothesis-not-result**: Red Team's own counter-arithmetic shows the
    steady-state "2–5× above NETD" figure inverts once the phenomenon's
    own constraint 4 (a *swept* beam, not steady illumination) is applied
    — transient dwell-limited ΔT for the OFF-state endpoint is 30–700×
    *below* NETD, and the same scaling logic applies to the ON endpoint
    pending pinned dwell/geometry/host-phase parameters (docket #7, still
    deprioritized behind T13).

**Recommended-not-mandatory items deferred:** MATERIALS' ε_r=1.77
beam-scene realizability probe (was scoped as a Block-B companion; deferred
alongside Block B, the qualitative C=−0.04/−0.08 estimate stands in the
record per fix 9). PHOTONICS' multi-plane `observer_profile` readout
(superseded by the residual-gate, which Red Team showed is sharper and
already produced by the run at zero extra cost).

**Provenance note (Red Team attack 15):** the Phase-1 packet handed to Red
Team included one Director-inserted bracketed annotation routing MATERIALS'
finding for context (`[No idealization stated for eps_r=1.0's host-material
restriction — MATERIALS' critique below flags this as load-bearing.]`).
This was Director scaffolding added when assembling Red Team's input packet
*after* the five blind critiques were in — not part of ELECTROMAGNETISM's
frozen Phase-1 proposal, and not a violation of the blind-parallel
mechanic (which governs the five blind critiques, already complete when the
annotation was added; Red Team is the one seat that receives everything by
design). Recorded per Red Team's own demand for provenance clarity. Future
cycles: keep the frozen Phase-1 file byte-identical when assembling Red
Team's packet; put Director annotations in a clearly separate cover
section instead.

## Phase 3 — Synthesis (Director)

The ONE testable configuration: **Block A only**, all ten mandatory fixes
folded in, as coded in `design_geometry.py`/`run.py`. Checkpoint criterion 4
does **not** fire (Red Team's own ruling: nothing has been published; the
fixes catch drift pre-freeze) — but Red Team's tripwire is adopted verbatim:
*if g₀ appears in any post-run document as a measured constant or mechanism
signature rather than a fitted bench-calibration parameter, or if
`off_pass`'s PASS is cited anywhere without the ε_r≡1 restriction and its
consequence in the same sentence, criterion 4 fires retroactively.*

**r=156 companion leg (4th deferral):** defensible this cycle per VISION's
own Iteration-9 ranking and Red Team's endorsement (T13/T14 leave the sign
of scale bias empirically unsettled — building a bridge on an
still-partially-open question relocates problems rather than resolving
them). **Committed trigger adopted, per VISION's request and Red Team's
grant:** Iteration 11 builds it unconditionally, Checkpoint-4 tripwire on
non-execution. Note for the record: Red Team's attack 5 removes one of the
two stated preconditions (the "uncharacterized decision floor") outright —
the weighting-convention bug, not a real floor problem, was the obstacle.

## 2. Parameter table

See `design_geometry.py` for exact numbers (all verified/asserted at import
time). Summary: NX×NY = 540×2376 (×1.5 rescale of exp-032's native 360×1584,
independently rounded, physical size held); R_OUT=117; cpl=30 (native was
20); STEPS=2100 (native 1400, ×1.5 — fixes T10's settling confound that
exp-025's own R3 check did not address); courant=0.99; N=9 fallback angles
(±35/±25/±15/±5/0)°; 4 articles (off_bracket τ=0.003, off_pass τ=0.0065,
off_lab τ=0.008, off_field τ=0.032), uniform disk, ε_r=1, no PEC core,
σ = τ/(2·117) pinned as explicit numbers with a runtime assert. 5 scenes
(empty + 4 articles) × 9 angles = 45 calls, + 2-call settling control
(empty + off_pass @ θ=0, STEPS=1400) = **47 new FDTD calls**, smoke-tested
at ~64 s/call full-scale (2100 steps) → **est. ~12–15 min wall time** (4
workers). No `lab/` change → suite stays 46/46 fast-stage green (re-verified
before results are read).

## 3. T1 escape route

Intensity-gated absorption σ(I) — instrument/resolution-validation work on
its OFF-state endpoint, explicitly not a mechanism. Every article is
static, linear, time-invariant, passive (σ≥0, real, non-dispersive,
ε_r≡1, no gain): trivially reciprocal and causal. Nothing switchable is
built or claimed. The σ_on/σ_off realizability tension (≈537–600× per
MATERIALS' Iteration-10 propagation, unchanged by this cycle) is untouched.

## 4. Predicted outcomes (falsifiable bands, committed BEFORE the run)

**P-1 (primary, scored) — data quality gate.** The free 4-point fit's max
residual ≤ **3.0×10⁻³** (g_corr units). *If this fails, the R3 disposition
is INCONCLUSIVE regardless of what A comes out to* — the run's own data is
too noisy to trust a comparison.

**P-2 (primary, scored) — R3 disposition, three-way, pre-registered.**
Conditional on P-1 passing: let ΔA = |A_fit(600, cpl=30) − 0.689593|
(the established native-cpl free-fit intercept).
- **CONFIRMED (resolution-invariant):** ΔA ≤ **0.015**. g₀≈0.689 stands as
  a resolution-stable bench-calibration constant at 600 nm; the raw g600≥
  0.69 "recurrence" is fully explained as a floor artifact, closed.
- **ARTIFACT:** ΔA ≥ **0.035**. The desk-collapse hypothesis itself is
  wrong at 600 nm; every g≈0.69 citation (including exp-031's σ-held
  r=156 point) reopens as unresolved.
- **INCONCLUSIVE:** 0.015 < ΔA < 0.035, or P-1 fails. A real, pre-registered
  outcome — not a fallback invented after the fact (VISION's mandatory
  fix, Red Team-endorsed).
Central expectation (Director, informational only, not a separate scored
band): CONFIRMED, since the free-fit model already explains 12/12 existing
points to a residual of 6.5×10⁻⁶ at native resolution and nothing in this
design changes the underlying physics, only the grid.

**P-3 (informational, non-discriminating, stated as such in advance) — raw
g600.** g_raw600(off_pass) will likely land in a wide band influenced
almost entirely by the fresh 600 nm floor, not by P-2's question. **Whether
raw g600 lands above or below 0.69 does NOT by itself confirm or refute
P-2** — only the g_corr fit does. This channel is retained only to report
the retired QUANTUM clause's counterfactual outcome for the historical
record.

**P-4 (settling control, scored).** |ΔC|/|C| between the θ=0 reading at
STEPS=1400 (settling control) and STEPS=2100 (main sweep) ≤ **3%** — this
cycle's own fix for T10's settling confound (exp-025's own R3 check held
steps fixed and so cut post-ramp settling margin from 46 to 30 periods;
this design holds post-ramp periods at 49, matching native, verified by
Red Team's independent geometry re-derivation).

**P-5 (VISION ladder, scored, raw C only per mandatory fix 8).** Central
expectation: off_pass PASS at all 3-λ-equivalent measurement (this cycle
is 600 nm only) continues to hold — off_pass's raw C is far enough inside
the 0.005 bar (established central 0.0045 at cpl=20) that neither the
CONFIRMED nor ARTIFACT branch of P-2 flips it (VISION's own Phase-2 proof:
even at P-2's original, wider artifact-band edges the corrected |C| stayed
PASS both ways). If the fresh 600 nm floor comes back unusually large
(comparable to exp-025's own 750 nm refinement, which degraded 3.9×), the
PASS margin could tighten toward MARGINAL — reported, not silently
smoothed over.

## 5. Idealizations (lab convention)

2D TMz, one polarization. CW, 600 nm only (the 3-λ desk structure is
analyzed from existing published data, not re-run this cycle). Static,
linear, time-invariant media; no σ(I) built. Ambient = 9 discrete
incoherent plane waves over ±35°, post-hoc intensity sum (linear-media
idiom — invalid for any gated article). Back-lit ambient only, no
front-lit channel. **ε_r ≡ 1.0 (index-matched, gas/aerosol-host-only
idealization) is load-bearing for both g₀'s validity and the PASS verdict
— see mandatory fix 9, above; a realizable condensed-phase host fails both
constraints 2 and 3 independently of τ.** The free-curvature g_corr fit is
a first-order weak-perturbation bench-calibration estimator, valid at
τ ≤ 0.032 (this design's range), not extrapolated to τ=3.9 (the ON
endpoint, which saturates far from this linear regime). The THERMO sidecar
is a post-run analytic calculation (expressibility contract), not an FDTD
output; the ON-endpoint LWIR claim is explicitly unresolved (mandatory fix
10). Decision-floor correction (mandatory fix 2) applies to the historical
committed table only — this run measures its own fresh empty-scene floor
at cpl=30 and reports it independently. Bench scale ≈10λ; nothing here is
a Tier-W/Tier-A constraint-3 verdict; no scale bridge is built or claimed.

## Phase 4 — Results

**50 new FDTD calls** (corrected from an originally documented 47 — Red
Team's Phase-5 audit, attack 8: `run_ambient_group` always runs empty +
all four articles per invocation, so the settling-control block's single
call cost 5 FDTD sims, not 2; 3 of those 5 — off_bracket/off_lab/off_field
at 1400 steps — were computed but never analyzed, only empty and off_pass
were used, exactly as scoped. Erratum applied to `results.json::meta` and
to `run.py`'s own docstring, same shift), 1036 s (852 s main sweep + 184 s
settling control, the latter covering all 5 of its own calls). No `lab/`
change — suite reconfirmed 46/46 green pre-run.

| Prediction | Result | Verdict |
|---|---|---|
| **P-1** residual gate ≤3.0×10⁻³ | max_residual = **6.447×10⁻⁶** | **PASS** (**465×** inside the gate — corrected from an originally-reported 438×, MATERIALS'/QUANTUM's/PHOTONICS' Phase-5 review, all three independently) |
| **P-2** R3 disposition | ΔA = \|0.689637 − 0.689593\| = **0.0000442** (band: CONFIRMED ≤0.015) | **CONFIRMED, per the design's own pre-registered bands — see the corrected reading above and in Learned, below: this closes "the raw-g600 shift between resolutions is explained by the floor shift," verified independently three ways to ≈6×10⁻⁸; it does NOT by itself establish that g₀ carries no resolution-dependent wave physics (Red Team, Phase 5, attack 5) — that is a narrower, still-open question this design was not well-powered to test.** |
| **P-3** raw g600(off_pass), informational | g_raw = **0.7056 — further above 0.69 than the native-cpl reading (0.6927), not closer to it** (Red Team, Phase 5, attack 4) | as predicted, non-discriminating — and a sharper illustration than originally framed of why the raw-g600 clause needed retiring: refining the grid did NOT make the raw anomaly go away, it got MORE pronounced; only the floor-subtracted currency explains it. **The retired clause's numeric successor is itself circular** (Red Team, attack 3): because g_corr ≤ g_raw whenever C_empty and C share a sign (true by construction here), "g_corr < 0.69" cannot fail to hold once the floor is subtracted — the successor clause cannot disagree with the disposition it exists to test. Flagged as an open design defect for whoever next relies on it, not fixed retroactively (predictions/design are frozen once committed, per house discipline). |
| **P-4** settling, θ=0, \|ΔC\|/\|C\| ≤3% | **0.48%** (C(1400)=−0.004984, C(2100)=−0.005008) | **PASS**, comfortably inside the band |
| **P-5** VISION ladder, raw C (article is an ε_r≡1 gas/aerosol-host-only construction — mandatory fix 9; every PASS below is conditional on that idealization and its consequence, ~537–600× σ_on/σ_off, per MATERIALS' Phase-5 review, unchanged by this cycle) | off_bracket **PASS** (−0.00218), off_pass **PASS** (−0.00459), off_lab **MARGINAL** (−0.00561), off_field **FAIL** (−0.02188) | **as predicted at this resolution** — off_pass's raw-C PASS margin held (the undecidable-outcome risk VISION flagged did not materialize at THIS run's floor); off_lab's MARGINAL is not a new finding: its established native-cpl 600nm value (−0.005531) was already >0.005. **Caveat, not in the original prediction (Red Team's Phase-5 audit, attack 6): raw C moved toward the FAIL bar at every article under this one resolution step** (+3.97%/+1.86%/+1.51%/+0.39%, bracket→field), shrinking off_pass's own margin from 9.9% to 8.3% of the 0.005 bar — two points cannot distinguish a converging from a diverging trend; a third resolution point is needed before "the PASS margin held" is trusted as a settled fact rather than a one-step snapshot |

**All five predictions confirmed cleanly at face value — but Phase 5's
seven-seat review (below) found the headline overstates what this design
actually tested, and the Director's synthesis adopts Red Team's corrected
reading.** One number flagged honestly from the start, not smoothed over:
the **fresh empty-scene decision floor at 600nm/cpl=30 measured
1.165×10⁻⁴ — 3.5× larger than the established cpl=20 value (3.317×10⁻⁵)**,
a real floor degradation on the same order VISION's Phase-2 attack warned
about (citing exp-025's own 750nm history).

**CORRECTION (Red Team + ELECTROMAGNETISM, Phase 5, independently — struck
and rewritten, not smoothed over): the paragraph originally here claimed
the residual-gated methodology was "exactly why" the 3.5× floor
degradation "didn't cost the cycle its disposition," framing this as the
gate being robust to floor SIZE. That claim was backwards and is WRONG.**
A floor error δ enters g_corr as δ/τᵢ — across τ=0.003→0.032 that is a
10.7× *differential* perturbation, the most sharply non-uniform signature
this design's residual can detect (EM, verified: a genuine floor-
*mismeasurement* of the observed 8.33×10⁻⁵ magnitude gives max_residual =
8.5×10⁻³ and ΔA = 0.021 — INCONCLUSIVE, not CONFIRMED; Red Team
independently reproduced this exact counterfactual). **The gate is a
mismeasurement detector, not a floor-size-tolerant instrument — it stayed
clean here because the floor was measured ONCE, correctly, and applied
consistently across all four articles (a common-mode shift), not because
gates like this one are insensitive to floor magnitude.** A genuinely
noisy or inconsistent floor measurement of the same size WOULD have been
caught and WOULD have blocked the CONFIRMED disposition. This is still a
real, valuable result — it is just a narrower one than originally claimed.

**Sharper still (Red Team, Phase 5, attack 5): ΔA≈0 is closer to
guaranteed-by-construction than to a strong test of resolution-invariant
wave physics.** Because the resolution change here was overwhelmingly a
common-mode additive shift in C_empty (verified: ΔC across all four
articles = −8.345/−8.363/−8.371/−8.540 ×10⁻⁵, essentially identical to the
empty scene's own −8.331×10⁻⁵ shift — QUANTUM's independent decomposition
confirms the same to 5×10⁻⁵), and g_corr is *constructed* to subtract
C_empty, the fit's intercept A is largely insulated from exactly the kind
of perturbation this run measured — almost by algebraic construction, not
because g₀ was shown immune to genuine resolution-dependent wave physics.
**What this run actually demonstrates to high confidence (≈6×10⁻⁸ in
C-space) is that the additive-floor-subtraction MODEL is self-consistent
and precise** — a real, independently-useful result (three seats —
EM's zero-parameter geometric model, QUANTUM's per-article decomposition,
Red Team's cross-check — converge on it from different directions) — but
it is a narrower claim than "g₀ is confirmed resolution-invariant physics,"
which this design is not well-powered to test.

## Learned

*(Rewritten post-Phase-5, incorporating Red Team's audit and the six other
seats' independent findings — the version originally committed here
overstated the closure and has been struck per house discipline: flag,
don't silently rewrite. The struck text and why is preserved in the git
history of this file and in LOGBOOK.md Iteration 10.)*

**What genuinely closed:** the raw g600≥0.69 recurrence's *cross-resolution
behavior* is now explained, verified independently three separate ways
(EM's zero-parameter geometric chord model predicting g₀=0.6981 vs
measured 0.68964, −1.2%; QUANTUM's per-article floor/τ decomposition,
agreement to 5×10⁻⁵ on three articles independently; Red Team's direct
cross-check, raw-g change 0.0129 vs floor/τ = 0.0128) — the cross-
resolution shift in raw g600 is fully accounted for by the measured floor
shift, to extraordinary precision (≈6×10⁻⁸ in C-space). **This is a real,
useful result on its own terms: the additive-floor-subtraction model this
program has used since Iteration 2 is validated far more precisely than
before.**

**What did NOT close, contra this NOTES.md's own first-draft framing
(Phase 5's central correction, Red Team's audit + PHOTONICS + EM,
independently converging):**

1. **The raw-g600 recurrence itself is NOT gone — it got MORE pronounced
   under refinement** (g_raw(600,cpl=30)=0.7056 vs native 0.6927), not
   less. What closed is that this shift is *explained*, not that the
   underlying reading disappeared. "CLOSED" is the wrong word; "explained"
   is the right one.
2. **ΔA≈0 is a weaker test of g₀'s own resolution-invariance than the
   headline implied.** Because this cycle's resolution change was almost
   entirely a common-mode shift in C_empty, and g_corr is *constructed* to
   subtract C_empty, the fit's intercept is substantially insulated from
   exactly the perturbation measured — the design demonstrates the
   floor-subtraction model is self-consistent, which is real and valuable,
   but is only weak evidence that g₀ itself carries no separate
   resolution-dependent wave physics. A future check would need a
   resolution change that does NOT primarily manifest as a common-mode
   floor shift to test that more sharply.
3. **The SCORED currency (raw C, mandatory fix 8) was never itself shown
   resolution-converged.** Raw C moved toward the FAIL bar at all four
   articles under this one refinement step (off_pass's PASS margin:
   9.9%→8.3% of the bar); two points cannot distinguish convergence from
   a trend. Every PASS/MARGINAL/FAIL verdict this program has ever issued
   rests on a currency this cycle showed is *moving*, not settled.
4. **g₀ sits ~15% below its own window-integrated geometric chord model**
   (PHOTONICS, Phase 5: 0.814 geometric vs 0.6896 measured) — inconsistent
   with the THERMO sidecar's own separate amplitude assumption (π/4=0.785)
   computed in the same `results.json`. Because this deficit is stable
   across cpl=20→30 (a window-sampling numerical error would not survive
   that refinement), PHOTONICS argues resolution-invariance is *positive*
   evidence the 15% gap is a real diffractive-leakage effect at the
   measurement plane, not noise — meaning g₀ needs a SECOND restriction
   beyond ε_r≡1 (mandatory fix 9): it is specific to this bench's
   (PLANE_DX/λ, W_OBJ/r_out) geometry, not a portable constant even among
   gas-host articles at other standoffs. Unexplained; not investigated
   this cycle.
5. **The geometry is not fully self-similar under the ×1.5 rescale, contra
   this file's own earlier claim.** PLANE_DX rescaled 15→22 (independently
   rounded; exactly self-similar would be 22.5) — a −2.2% drift in
   standoff-in-wavelengths (0.750λ→0.733λ), on exactly the parameter T12
   has spent two iterations showing is diffraction-sensitive (Red Team,
   Phase 5, attack 7). Small, not disposition-changing this cycle, but a
   precedent for future rescales to check explicitly rather than assert.

**Mandatory fix 9 (ε_r≡1 idealization) carry-through was insufficient in
three places** (MATERIALS, Phase 5) — corrected in this revision: the P-5
results row and every bare "PASS" citation now carry the restriction and
its ≈537–600× consequence inline, not just in a separate `meta` key.

**Mandatory fix 1 (σ pinning + runtime assert) does not do what it claims**
(Red Team, Phase 5, attack 1): the assert is algebraically tautological
(σ is *defined* from τ, so it cannot fail) and does not provide the
independent guard against exp-027's own T10 bug pattern that the fix was
meant to add. τ was held correctly this run — verified separately, not by
this assert. Flagged in `design_geometry.py`, not silently left uncorrected.

**Block B (bulk-vs-edge mechanism instrument) remains unbuilt** — cut this
cycle per Red Team's Phase-2 sanctioned fallback. Still queued standalone.

**QUANTUM's Iteration-9 disposition clause is formally retired**, but its
numeric successor is logically circular (Red Team, Phase 5, attack 3: it
can never disagree with the disposition it exists to test, since g_corr's
sign construction guarantees g_corr < g_raw here). The retirement itself
stands; the successor clause needs a genuine, non-circular replacement
before it is cited as a real check again — flagged, not fixed
retroactively.

## Phase 5 — Review (seven fresh seats + Director's close)

All seven seats read `results.json` and this NOTES.md fresh (no memory of
having run or critiqued the cycle). Full verbatim record: LOGBOOK.md
Iteration 10. Summary:

**PROMISING (5):** THERMODYNAMICS, MATERIALS ("narrow"), QUANTUM OPTICS (no
dissent this cycle — contrast with Iteration 9), VISION SCIENCE, and
initially ELECTROMAGNETISM's own headline reading — each verified the
arithmetic independently and found the pre-registered question closed
cleanly on its own terms.

**PARTIAL (2), both substantive, not pro-forma:** **PHOTONICS** — found the
"λ-dependence of the floor" attribution is actually wrong (media are
non-dispersive here; what varies is resolution, not wavelength — the
floor is non-monotone/non-convergent across all three λ under refinement,
so "600nm's floor sits near zero" was a cpl=20 accident), found a simpler
closure (raw g600≥0.69 was arithmetically guaranteed at every floor this
bench has ever measured, no chromatic story needed), and found the ~15%
g₀ chord deficit (Learned, item 4, above). **RED TEAM's audit** — verified
every mandatory Phase-2 fix against the actual code (not just NOTES.md's
claims), found the floor-robustness reasoning backwards (Learned, above),
the run-count bookkeeping bug, the circular clause successor, and ruled
that ΔA≈0 is weaker evidence of g₀'s resolution-invariance than claimed —
and, invoking this program's own established precedent (verdict turns on
whether a cycle's open questions close, not on a favorable headline
number — Iterations 7, 8, 9 all PARTIAL for the identical reason),
**overruled the emerging PROMISING lean.**

**Director's close: VERDICT PARTIAL**, adopting Red Team's audit. All of
Red Team's mandatory same-shift corrections applied above and in
`design_geometry.py`/`run.py`/`results.json` (run count 47→50; the
floor-robustness paragraph struck and rewritten; ε_r qualifiers attached
inline to every PASS citation; the fix-1 assert's real limits stated; the
PLANE_DX non-self-similarity noted). **Checkpoint criterion 4** (the
Phase-3 tripwire on citing off_pass's PASS without the ε_r restriction in
the same sentence) does **not** fire — Red Team's own ruling was explicit
that it fires only if uncorrected at close, and it is corrected here, same
shift.

**The honest headline, replacing this file's own first draft:** exp-033
did real, verifiable work — it converted a three-experiment, four-point
"g600 recurrence" from an unexplained flag into a floor-subtraction effect
verified three independent ways to ~10⁻⁸ precision, a genuine advance on
T1. But it answered a narrower question than the one queued (raw-currency
resolution-invariance, not floor-subtracted-model self-consistency), left
the actually-scored currency (raw C) unconverged with only two resolution
points, surfaced two new open questions (the g₀ chord deficit; the
circular clause), and Block B — half of Iteration 9's binding two-item
priority — was never run. **No Checkpoint criterion beyond 4 fires**: not
a configuration passing every constraint (1); not a proven boundary (2);
no engine physics beyond validated bench classes (3); and this is not two
consecutive logbook-non-advancing cycles (5) — this cycle's own genuine,
verified content (the three-way-confirmed floor-subtraction result) is
real forward motion, just narrower than first claimed.

## Next

**Ranked per the Director's adjudication of all seven Phase-5 reviews**
(this supersedes the pre-Phase-5 draft ranking, which is struck below and
preserved for the record — house discipline, flag don't silently
overwrite):

1. **A third resolution point (cpl=40), empty + off_pass only, 600nm,
   N=9 — ~18 calls (Red Team's top Phase-5 pick, independently converged
   on by EM's "the floor degradation is genuinely open" finding).** This
   cycle created, rather than closed, the highest-leverage open question:
   is the empty-scene decision floor converging or diverging under
   refinement (it got WORSE at 600nm, cpl 20→30 — physically backwards for
   ordinary discretization error, per EM), and is the actually-SCORED raw-C
   currency (mandatory fix 8) itself resolution-converged? Two points
   cannot answer either question. Cheapest, highest-information item in
   the queue; gates trust in every PASS/MARGINAL/FAIL this program has
   ever issued on this bench, not just this cycle's own.
2. **VISION's r=156 companion leg — committed trigger, Iteration 11
   unconditional** (per Phase 3, Red Team's grant of precedent) — **but
   Red Team's Phase-5 review recommends pairing it with item (1) in the
   SAME cycle, not running it alone**: building a scale bridge on a floor
   that just moved 3.5× under refinement reproduces the exact objection
   that deferred r=156 four times already. VISION's own Phase-5 review
   independently converges: off_pass's PASS margin (4.14×10⁻⁴) is smaller
   than this bench's own N5-vs-N9 angular-quadrature convergence increment
   (~4.8×10⁻⁴) — a second, orthogonal reason the r=156 leg needs its own
   convergence riders (dual-currency pre-registration, a fresh δ_C(156)
   remeasurement, an N17 weak-article check), not a straight port of the
   r=78 bench's own machinery.
3. **Block B, properly scoped, as its own standalone lead cycle**
   (demoted from the pre-Phase-5 draft's #1, per VISION's and MATERIALS'
   independent Phase-5 arguments: attributing WHERE an OFF-state article's
   absorption sits is second-order to whether the currency that scores it
   is even converged). PHOTONICS' full fix package (τ=0.10 substitution,
   `angular_scattered_pattern`, a re-derived bulk-attenuation reference
   model) still needs its own Phase 1/2/3 cycle — PHOTONICS' Phase-5
   review additionally reframes its real target as the ~15% g₀ chord
   deficit (Learned, item 4), a ~250× stronger, more falsifiable signal
   than the original bulk-vs-rim ripple.

**Promoted from the pre-Phase-5 draft's #3 (MATERIALS' Phase-5 review,
independently argued by VISION):** **a proper realizability memo** now
carries a specific, striking new number worth a dedicated build, not just
citation: the σ(I) mechanism must gate at flashlight irradiance
(~10⁻³ W/cm²) against published RSA/two-photon-absorption onset
thresholds (10⁶–10⁹ W/cm²) — a **9–12 order-of-magnitude gap**, dwarfing
the previously-tracked 537–600× dynamic-range tension. If this survives a
dedicated check, MATERIALS flags it as a candidate for Checkpoint
criterion 2 (a proven boundary — PANEL.md's own honest-alternative-product
stop condition). Zero FDTD cost; runnable alongside any FDTD-heavy cycle.

*(Struck, pre-Phase-5 draft ranking, preserved for the record: 1. Block B
standalone. 2. r=156, unconditional, alone. 3. Realizability memo,
low-urgency. Superseded above once Phase 5's seven reviews — especially
Red Team's floor-convergence finding and VISION's quadrature-convergence
finding — showed the r=156 leg's own preconditions are less settled than
this cycle first believed, and that a cheap, orthogonal diagnostic
(item 1) now sits ahead of both.)*

Lower priority, inherited and unchanged this cycle: T11's own trust-suite
stage for the ambient/line-source box-ledger channel (THERMODYNAMICS, all
four articles' ΔT now cheaply reportable per its own Phase-5 review, not
just off_pass's); T14's PHOTONICS multi-point cored-absorber r-sweep; a
genuine PEC r-family ripple test near r≈270–350 (T12's own real open
half); T11's dedicated multi-point/multi-box-pair box_dev floor
characterization; Iteration 6's still-queued incoherent-ensemble/
phase-quadrature idiom (QUANTUM's own Phase-5 pick, #2 in its own ranking);
a formal reciprocity check (EM's own long-standing pick); the shell-
thickness/optical-depth economy sweep (MATERIALS); T10's residual
+3.05pp sub-cell/window-offset sweep.

Next lead per rotation: **THERMODYNAMICS** (Iteration 11) — its own
Phase-5 review commits to proposing item (2) above (r=156), one cycle
ahead of the rotation's original plan, given the committed-trigger
priority; item (1)'s cpl=40 diagnostic is cheap enough it may be folded in
as a companion block rather than requiring its own separate lead slot —
Iteration 11's own Phase 1 decides.
