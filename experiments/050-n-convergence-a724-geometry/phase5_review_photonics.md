# PHASE 5 — REVIEW (PHOTONICS) · Panel Iteration 27 · exp-050

*Fresh sub-agent, charter: surface interaction, absorption spectra, angular
dependence, scattering cross-sections — is the proposal's/audit's optical
response coherent as stated, across wavelength and angle? Read `PANEL.md`,
`LOGBOOK.md` in full, `experiments/050-.../` in full, and cross-referenced
`experiments/042-.../design_geometry.py` and `experiments/049-.../results.json`.
Did not read any other seat's `phase5_review_*.md` for this cycle.*

## Scope check

This is an instrument-fidelity cycle, T1 escape route NONE, no mechanism,
no constraint-3/4 claim, no `REALIZABILITY_MEMO.md` exposure — confirmed by
my own read of `NOTES.md`/`run.py`/`results.json` (no such claim appears
anywhere; `REALIZABILITY_MEMO.md` is never referenced). My review scores the
audit's own design and conclusions, not a constraint verdict this cycle
never attempted.

## Verification performed (not trusted from prose)

Per R4 and this program's Red-Team discipline, I did not take `NOTES.md`'s
Reading section on faith. I re-ran `experiments/050-.../design_geometry.py`'s
actual committed `beam_divergence_incoherent_corrected` function myself,
through the `N_SERIES` doubling ladder, at both `GEOM_EXP042_OLD` and
`GEOM78`, for all three violating cells plus three comparison cells not
flagged as violations:

| θ₀,λ | geometry | C(n=41) | C(n=81) | C(n=161) |
|---|---|---|---|---|
| 36°,600nm | A752 | −5.933e-4 | −3.005e-4 | −3.083e-4 |
| 36°,600nm | **A724 (violation)** | **+3.173e-4** | **−3.691e-4** | −3.722e-4 |
| 40°,600nm | A752 | −4.29e-6 | +3.539e-4 | +3.442e-4 |
| 40°,600nm | **A724 (violation)** | **+1.777e-4** | **+7.664e-4** | +7.660e-4 |
| 40°,750nm | A752 | +1.775e-4 | +3.342e-4 | +3.313e-4 |
| 40°,750nm | **A724 (pre-registered exempt violation)** | **+1.590e-3** | **+7.040e-4** | +7.010e-4 |
| 38°,600nm | A752/A724 | −9.26e-4 / +4.469e-4 | −1.639e-4 / −8.162e-5 | (both nstar=81 at both geometries — not a "violation" since no tier *increase*, but the same fragile regime) |
| 36°,750nm | A752/A724 | +1.29e-5 / −7.407e-4 | −3.765e-4 / −5.031e-4 | (nstar=41 at both — but the 41→81 step uses 78%/47% of its own `ABS_TOL` margin; a near-miss, not a robust pass) |

This exactly reproduces `results.json`'s `per_cell_summary_geom78` entries
(spot-checked to the printed digit — e.g. NOTES.md's cited (36°,600nm)
`c41=+3.17×10⁻⁴`, converged `−3.69×10⁻⁴` matches my own independent
invocation exactly) and `NOTES.md`'s own Reading paragraph's cited figures.
**P-NCONV27-0's regression anchor, P-NCONV27-1's max-n\*=81 finding, and the
three-violation count are all independently confirmed by direct execution,
not merely re-read.**

One structural fact worth stating plainly, not in `NOTES.md`'s own Results
table: across the whole 108-combination grid, only **two** `nstar` values
ever occur — 41 (95 cells) and 81 (13 cells). No cell anywhere needs 161 or
higher. "Moved to a larger tier" in this cycle's entire record therefore
means, without exception, "flipped from clean-at-41 to needing-81" — a
binary event, not a graded one. That matters for how the three violations
should be read (below).

## Is the near-zero-crossing candidate mechanism physically plausible?

**Yes — and I can name the specific optical mechanism NOTES.md's own
Reading section stops short of identifying.** `beam_divergence_incoherent_corrected`'s
per-angle profile is `-Re(E·H*)` under the *corrected* convention (obliquity
folded into H only, per Faraday's law for `add_line_source`'s real
line-current physics — exp-042's own Iteration-19 erratum). This is a
genuinely **signed** quantity, oscillating spatially and with angle at the
T21 edge-diffraction fringe period `P(θ)=λ/(A·cosθ)`. Contrast this with the
other two functions in the same audit: `beam_divergence_incoherent`'s
per-angle profile is `|G@amp|²` — strictly non-negative by construction,
so its angular sum never approaches a delicate cancellation, and indeed
**zero of `incoherent`'s 9 FWHM=20° cells ever change tier, at either
geometry** (verified directly from `results.json`'s `tier_table`).
`beam_divergence_coherent`'s own fragility (QUANTUM's Attack-2 mechanism,
Red-Team-confirmed) is a *different* physical effect entirely — grating-lobe
replica truncation against a shifting taper edge, an aperture/windowing
phenomenon — and it too shows **zero** upward tier moves this run (all
`coherent` FWHM=20° cells either hold or improve). The fragility this cycle's
Reading section is puzzling over belongs to exactly one function, for a
reason traceable to that function's own field convention, not a generic
property of "FWHM=20° cells" or "the exempted regime" in the abstract.

At FWHM=20°, `gaussian_angle_weights`'s own `half_width_factor=2.5` samples
a fixed ±50° window (5×FWHM) regardless of geometry. That window spans many
periods of the T21 fringe (≈38–71 periods depending on λ, see below) — a
broad coherent-in-angle integral of a signed, oscillating quantity. When
that integral's net value happens to sit close to zero (common in this
grid: 6 of the 9 FWHM=20°/`incoherent_corrected` cells sit at `|C|` of order
10⁻⁴–10⁻³ at A=752 already, an order of magnitude or more below `C_THR`),
the reported value is the *residual* of a near-total cancellation, set by
the window's edge structure rather than its bulk — and a coarse n=41
quadrature can misjudge both the residual's magnitude and its **sign**
relative to the n≥81 answer. My own n-by-n trace above shows this exactly:
at (36°,600nm)/A724 and (40°,750nm)/A724 the n=41→81 step **crosses zero or
nearly halves**, producing an absolute jump that happens to clear
`ABS_TOL=5×10⁻⁴` even though the converged value itself is 1–8× that same
`ABS_TOL` — i.e., the criterion's own absolute floor (calibrated for
judging convergence against `C_THR=0.005`) is comparable in scale to the
signal being judged, exactly as `NOTES.md`'s Reading section flags, but the
underlying reason it happens to only this function is a real, verifiable
optical fact about the corrected convention's signed integrand, not
incidental.

## Does the shared pattern (FWHM=20°, `incoherent_corrected`, small |C|) point to physics NOTES.md missed?

Yes, in one respect. NOTES.md's Reading treats the three violations as one
undifferentiated observation and explicitly declines to adjudicate between
"(a) real near-zero-crossing sensitivity... (b) an `ABS_TOL`-scale
construction artifact... or (c) something else." My own verification
resolves this further than "not decided": **it is (a) and (b) together, not
competing alternatives** — the near-zero crossing (a) is the real, physical
event (a broad-angle coherent integral of a signed fringe-oscillating
quantity landing near its own zero, driven by a genuine ~3.7% geometry-
induced phase shift in the T21 fringe, not noise), and the `ABS_TOL`-scale
comparability (b) is *why the convergence machinery, as currently
calibrated, is unable to certify that near-zero value cleanly* — the
residual's magnitude and the tolerance floor happen to be the same order,
so ordinary quadrature refinement (not a bug, not aliasing in Attack 1's
sampling-density sense) produces an apparent "non-convergence." Both halves
are real; neither is "just an artifact" in the dismissive sense, and neither
alone is the whole story. This is a sharper, falsifiable account than
NOTES.md's own three-way hedge.

## Is there a real physical reason 600nm specifically (not 450nm) joins 750nm here?

**Partially, and I can name a candidate predictor, but the data does not let
me call this settled — a genuine, disclosed limit of what this review can
close.** The fixed ±50° angular window spans a number of T21 fringe periods
that scales as `100°/P(θ) ∝ A/λ` (shorter λ → shorter period → more periods
spanned before the window edges are reached). Computing this directly:
≈65–71 periods at 450nm, ≈48–53 at 600nm, ≈38–42 at 750nm (both
geometries). A broader-window integral built from more oscillation cycles
is, in general, a better-averaged, more nearly self-cancelling sum, whose
residual is proportionally less sensitive to a small phase shift introduced
at the window's edges by a 3.7% change in `A` — a real, quantifiable,
falsifiable mechanism, and directionally consistent with 750nm (fewest
periods) showing the pre-registered violation, 600nm (intermediate) joining
it, and 450nm (most periods) staying clear.

**But there is a real complication I will not paper over**: 450nm was
already the single *most* fragile wavelength at A=752 — all three of its
own FWHM=20°/`incoherent_corrected` θ₀ cells needed n\*=81 there (verified
directly against exp-049's own committed `results.json`), versus only 1 of
3 for 600nm and 1 of 3 for 750nm. Because this grid's own `N_SERIES` never
realizes a tier above 81 anywhere (confirmed above), a cell already sitting
at 81 at A=752 has no room left to register a *new* violation at A=724 in
this cycle's binary tier bookkeeping — it can only hold or improve. 450nm's
clean record in P-NCONV27-2 is therefore consistent with either "genuinely
less A-sensitive, as the periods-spanned argument predicts" or "already
saturated at the ceiling this instrument can detect, telling us nothing
about its true A-sensitivity." My own spot check of one 450nm cell's
`ABS_TOL` margin was out of scope for this review's time budget; it is the
cheapest possible next check (below) and would distinguish the two readings
directly, without any new FDTD.

## Verdict: PROMISING

For this cycle's own narrow, instrument-fidelity scope — does the audit's
own design and conclusions hold up — **PROMISING**, matching the pattern
this program's own precedent (Iteration 26) already established for a
cycle with one honestly-REFUTED, informative prediction among a mostly-
CONFIRMED set. Specifically:

- The regression anchor (P-NCONV27-0) is bit-exact against exp-049's own
  committed 108-row table, independently re-verified by me — the audit's
  foundation is sound.
- The headline instrument question (P-NCONV27-1: does GEOM78 need a larger
  global n\* than A=752's 81) is answered cleanly: **no**, confirmed, and
  I independently confirmed the max-n\*=81 finding.
- P-NCONV27-2's REFUTAL is not a design failure — it is the audit correctly
  finding that its own Phase-3-corrected, Red-Team-narrowed exemption zone
  (itself already a genuine improvement over the Phase-1 draft, arrived at
  through two independently-converging blind critiques plus a Red-Team
  live pre-check) still did not exhaustively characterize a distinct,
  genuinely small-signal failure mode. That is exactly the kind of honest,
  informative miss PANEL.md's falsifiability discipline exists to produce,
  and `NOTES.md`'s own disclosure of it (rather than quietly narrowing the
  prediction after the fact) is correct practice.
- Every numeric claim I checked against source — the three violating cells'
  `c41`/`converged_value` figures, the regression-anchor pass, the
  108-combination tier census — reproduced exactly.
- Practically, nothing here threatens any live contamination-risk or
  realizability citation: all three violating values remain 7–30× below
  `C_THR=0.005` regardless of which `n*` governs them (the same conclusion
  P-NCONV27-6b's own cross-validated headroom figure independently
  supports for the sharpest-stakes cell).

This is not a RULED-OUT or a PARTIAL call from my seat: the optical-response
story here, once traced to source, is internally coherent — three
functions, three physically distinct fragility mechanisms (none for
`incoherent`, aperture-truncation for `coherent`, signed-integrand
near-null-averaging for `incoherent_corrected`), correctly if incompletely
anticipated by two independent Phase-2 mechanisms, with the actual gap
between prediction and measurement traceable to a real, nameable physical
effect neither pre-registered mechanism was built to cover — not to a flaw
in the audit's own construction.

## Ranked next-step candidates for Iteration 28 (PHOTONICS' own priorities)

1. **Add the near-null-magnitude indicator to Red Team's own already-queued
   phase-corrected difficulty predictor** (LOGBOOK Iteration-27 priority
   #3): score Δrel(41→81) against a predictor that includes not just each
   cell's phase offset within its local T21 fringe period, but also
   `|C(n=81)|/ABS_TOL` as a second regressor. My own verification shows the
   three actual violations are far better explained by "converged value is
   only 1–8× `ABS_TOL`" than by phase-offset-within-period alone — this is
   the single cheapest, most load-bearing desk-only addition to a test this
   program is already committed to running.
2. **A companion `incoherent_corrected`-only diagnostic**: for all 9
   FWHM=20° cells (not just the 3 that flipped), report the signed
   `ABS_TOL − Δabs(41→81)` margin at both geometries. This directly answers
   whether 450nm's clean P-NCONV27-2 record reflects real insensitivity or
   a tier-ceiling artifact (my own §"600nm vs 450nm" finding, above) —
   zero new FDTD, reuses this cycle's own committed function unmodified,
   and would resolve the one genuine open question my own review could not
   close.
3. **The genuine FDTD `ABSORB` sweep at the T21-vs-T24 geometry**
   (LOGBOOK's separately-queued item, Iteration-27 priority #2): the
   near-null-crossing mechanism I identified here is entirely a property of
   the *desk* propagator (idealization 5, undisclosed FDTD cross-check at
   any n, any geometry, for `beam_divergence_*`). Whether a real FDTD run
   shows the same sign-flipping near-zero behavior at these specific
   coordinates, or whether it is a desk-model-only artifact of the
   continuum Huygens–Fresnel sum, is the physically deeper question my own
   discipline cannot answer from this cycle's own zero-FDTD design alone.
