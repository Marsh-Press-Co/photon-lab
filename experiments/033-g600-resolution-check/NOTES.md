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

## Learned

*(filled in after Phase 4/5 — see Results and Phase 5 review, below.)*

## Next

*(filled in at Phase 5 close — see LOGBOOK.md Iteration 10 and PLAN.md.)*
