# PHASE 5 — REVIEW · PHOTONICS · Panel Iteration 48 · exp-071

**Charter:** surface interaction, absorption spectra, angular dependence,
scattering cross-sections. Owns: is the proposal's optical response
coherent as stated, across wavelength and angle?

Fresh context, blind to any other seat's Phase-5 review this cycle. Blind
to my own seat's Phase-2 critique this cycle (a different fresh instance
wrote it) — read it as source material, not memory.

**Independent verification performed:** re-ran `python3 design_geometry.py`
— every printed figure (congruent-series table, peak-angle fractions
0.949/0.984, R3-rescaled configs, budget 78 calls/6266.6 CPU-s/30.64 min/
91.92 min envelope, Rayleigh-floor table) reproduces bit-for-bit. Loaded
`results.json` directly and recomputed the headline trend, all 6 pairwise
spreads/resolution ratios, both binding-precondition checks, and the
Combined Verdict logic from the raw per-cell data (not from
`phase4_results.md`'s prose) — every number matches exactly. Read
`lab/fdtd2d.py::Sim._damping` directly. **No R4 defect found anywhere in
this cycle's record.**

## 1. The C70/C80 exact period tie — grid-discretization artifact, or something else?

**The write-up's own read ("plausibly a grid-search discretization tie")
is correct, and I can independently confirm it rather than merely accept
it.** I reconstructed the full R²(P*) curve `_free_period_search` actually
searches over (400-point grid, step 3/399 = 0.007519°) for all four
configs directly from `results.json`'s own raw `dense_causal` rows, not
just the single reported maximum:

| Config | Best grid idx | R² at best idx | R² one step over | ΔR² |
|---|---|---|---|---|
| C60 | 202 (2.5188°) | 0.4483 | 0.4482 (idx 203) | 0.0001 |
| C70 | 204 (2.5338°) | 0.4422 | 0.4421 (idx 205) | 0.0001 |
| C80 | 203/204 (tie, 2.5263°/2.5338°) | 0.4337 | 0.4337 | **0.0000** |

**C80's own reported maximum is *itself* a tie between two adjacent grid
points before C70 ever enters the comparison.** Across an 8-point
neighborhood (~0.06° span) around each config's reported optimum, R²
varies by less than 0.002 for all four configs — a landscape flat enough
that which specific grid cell wins the argmax is effectively noise-driven,
exactly consistent with (not merely "not contradicted by," as
`phase4_results.md` states) the Rayleigh-floor finding: the window
supplies only 9.5% of the resolution needed to separate C40's period from
C80's. Two independent noisy series landing on the identical bin under
these conditions is close to expected behavior, not a surprising
coincidence needing its own explanation. **I'd go further than the
write-up's own hedge ("plausibly... not evidence"): given the measured
flatness, an exact match carries no more information than a near-match
would, and the write-up should say so affirmatively rather than only
disclaim the opposite reading.**

## 2. Combined Verdict NEITHER — the physically correct call, or too conservative?

**The resolution-floor gate is procedurally sound and I endorse it as
applied.** A 4-point R²=0.87 fit built from four individually-flat argmax
searches (§1) is not independent statistical weight in the way the raw
number suggests — Red Team's own extension of QUANTUM's finding (the
CONFIRM band sits at 75% of full resolving power, under the floor) is
correct, and I could not find a way to read the raw statistic as reliable
evidence for a genuine trend using this window alone.

**But "NEITHER" should not be read as "no optical reason to expect a
trend."** There is a concrete, first-principles reason — from my own
charter, not borrowed from EM's or MATERIALS' — to expect *exactly* this
signature: a small, smooth, saturating, monotonic drift in the recovered
single-tone period as `ABSORB` deepens, from 40 all the way flattening out
by 70–80.

`Sim._damping`'s cubic ramp (`(k/absorb)^3` for `k=1..absorb`,
`exp(-0.30·d)` per pass) is a graded-loss taper terminating in a hard grid
edge — the textbook setup for a residual, ABSORB-depth-dependent boundary
reflection, small but nonzero at any finite depth. A crude one-way
transmission estimate (`exp(-0.30·Σ ramp)`, ignoring the accumulated
per-timestep effect, so this is an order-of-magnitude bound, not a
derivation) gives round-trip *power* reflectivity:

| ABSORB | round-trip power (rel.) | ratio to ABSORB=40 |
|---|---|---|
| 40 | 1.83×10⁻³ | 1.00 |
| 60 | 9.12×10⁻⁵ | 0.050 |
| 70 | 2.04×10⁻⁵ | 0.011 |
| 80 | 4.54×10⁻⁶ | 0.0025 |

If the observed `C_empty(θ)` series is a superposition of a dominant,
ABSORB-independent term (aperture/`TAPER`-edge diffraction — the "shared
geometry" hypothesis, common to all four configs) plus a small
boundary-reflection term whose *amplitude* tracks this residual-power
curve, a single-tone fit to that sum should converge toward the aperture
term's own period as ABSORB deepens, with the correction shrinking
rapidly and non-linearly — not linearly, contrary to what P-071-2's own
linear-trend model assumes. **The observed data has exactly that shape**:
taking C80 as the best proxy for the asymptote, `P*(ABSORB)−P*(80)` is
−0.098°/−0.015°/0.000°/0.000° at ABSORB=40/60/70/80 — a drop of 85% from
40→60 against the crude reflectivity estimate's own predicted 95% drop,
then flattening, same as the reflectivity curve. This is an
order-of-magnitude, not exact, agreement (the estimate ignores per-step
accumulation and the fact that `PAD` — not `ABSORB` — sets the round-trip
*distance*, only `ABSORB` sets the round-trip *amplitude*, since exp-065's
own construction holds the plane/source-to-boundary clearance fixed at
37/20 cells for every config), but it is a real, checkable, un-fitted
prediction that neither the proposal nor any Phase-2 critique computed. It
gives a positive answer to the panel's own question: yes, there is an
independent optical reason to expect `ABSORB` depth to shift a
diffraction-order-adjacent quantity by a few percent, saturating fast —
and NEITHER, applied to a straight-line trend model, is the right verdict
for the model actually tested, not necessarily the right verdict for the
underlying optics.

## 3. Was my own Phase-2 critique's 600nm-scope finding properly closed?

**Yes — disclosed correctly and completely, not dropped as happened to a
comparable finding in exp-070.** `WAVELENGTH_SCOPE_CAVEAT` is defined once
in `run.py`, printed unconditionally with the Combined Verdict regardless
of outcome, reproduced verbatim in `NOTES.md` (idealization 2) and
`phase4_results.md`'s closing caveats section, and present in
`results.json["caveats"]["wavelength_scope"]` — I checked all four
locations directly. Red Team's Phase-2 audit correctly separated my
finding's two possible fixes (a text caveat vs. an actual 750nm leg) and
ruled the caveat mandatory-now, the leg recommended-but-out-of-locked-
scope — a defensible scope call given the mandate was explicitly item 1
only, not a broadening. The one thing I'd flag as unresolved, not
mishandled: the caveat as written says a 600nm CONFIRM "cannot distinguish
a λ-scaled physical coupling from a cell-count/discretization artifact,"
but this cycle's actual outcome was NEITHER, so the caveat never got
exercised against a real CONFIRM this cycle — it remains correctly staged
for whichever future cycle produces one.

## 4. Any other optical-coherence defect?

None found beyond the above. `_free_period_search`'s import-by-reference
and default-assertion fix (mandatory fix 5) closes the "prose promise, not
code fact" gap my own Phase-2 critique's peer (QUANTUM) raised; the peak-
angle verification (0.949/0.984 of window ptp) is independently
recomputed and correct; the settling and R3 preconditions are optically
inert to this seat's charter and I have no attack on either.

## Rating: **PARTIAL**

Real, verified process progress: the mandatory-fix docket (settling check,
resolution-floor gate) worked exactly as designed and caught a genuine
false-positive-shaped result before it reached the record — a monotonic,
high-R² 4-point trend that would have read as a clean CONFIRM under the
Phase-1 draft's original (non-resolution-gated) bands. No R4 defect, no
dropped caveat, the wavelength-scope disclosure fully intact. But the
substantive optical question T28 exists to answer — does a genuine,
physically-explicable ABSORB-depth coupling exist — ends narrower, not
answered: I now have a specific, quantitatively-motivated candidate
mechanism (§2) that the pre-registered linear-trend test was never built
to detect, because it assumes the wrong functional form (linear in
ABSORB, not a saturating two-tone-beat weight). Not PROMISING (constraint
3 untouched, T1 N/A throughout, as every seat agrees). Not RULED-OUT (the
opposite of what I found — a plausible mechanism, not a foreclosed one).

## Proposed next step (concrete, falsifiable, PHOTONICS-specific, desk-only)

Replace the four independent single-tone free-period fits with **one
joint two-tone fit across all 124 already-collected points** (four
configs × 31 angles, zero new FDTD calls):

`y_k(θ) = c0 + A_ap·cos(2π sinθ/T_ap + φ_ap) + w(ABSORB_k)·A_bd·cos(2π sinθ/T_bd + φ_bd)`

with `T_ap`, `T_bd`, `A_ap`, `A_bd`, `φ_ap`, `φ_bd` shared (fit) across all
four series, and `w(ABSORB_k)` **fixed, not fit** — taken from the
analytic round-trip-reflectivity ratio in §2 (or a more careful WKB
estimate that integrates the actual per-timestep damping rather than my
crude one-pass approximation, still zero-FDTD). This has far fewer
effective degrees of freedom than fitting 4 independent 3-parameter
sinusoids (6 shared unknowns vs. 12, with the ABSORB-dependence supplied
externally rather than estimated from the same noisy data it would need
to explain), and — critically — it does **not** require frequency-
resolving two nearby periods against each other the way P-071-2's
pairwise/trend test does; it tests whether a *predicted, saturating
amplitude-weighting law* fits the pooled data significantly better than
the null (single shared tone, `w≡0`), via an F-test or AIC comparison.
**Falsifiable outcome:** if the joint fit does not significantly
outperform the null, or if `T_bd` converges to something with no
plausible geometric referent (recalling `TAPER`-alone is already REFUTEd,
exp-070), that is real evidence against the boundary-reflection
hypothesis specifically — narrowing T28 further without needing more
angular resolution, which the window cannot supply at any reasonable
added cost.
