# PHASE 2 — CRITIQUE · ELECTROMAGNETISM · Panel Iteration 26 (candidate exp-049)

*Blind parallel critique. Charter: field/wave behavior, impedance matching,
energy coupling; owns the reciprocity/passivity/causality bookkeeping. T21's
fringe-period model (`P(θ)=λ/(A·cosθ)`, LOGBOOK Iteration 18/19) is this
seat's own Iteration-18 Phase-5 derivation, reused here for a different
function — adjudicated on the physics, not on authorship.*

---

## Steel-man (≤150 words)

The T21 reuse is not analogy-by-convenience — for the incoherent functions
it is literally the same building block. `edge_diffraction_c_empty_corrected`
and each per-angle term of `beam_divergence_incoherent`/`_corrected` both
route through the identical `_src_amp`/`_G_for(lam,True)` machinery sharing
`A=752`. I re-ran the propagator directly (θ∈[35°,41°], 0.01° step, 600nm,
`design_geometry.py`): both the window-ratio `C_empty(θ)` and the raw
pointwise intensity `|E(OBJ_Y,θ)|²` — the actual incoherent-sum integrand —
show dominant FFT power at the bin nearest the predicted 1.9338° period. The
fringe genuinely lives in the quadrature's own integrand, not just in T21's
derived ratio. I independently recomputed §2.1's table at 450°/36°,
600°/38°, 750°/40° and the n≈709→641/1281/2561 ceiling arithmetic — all
match to stated precision. The two-consecutive-doubling criterion is a sound
generic defense against non-monotonic aliasing, and one C_THR-anchored
tolerance across all three functions is correctly motivated by what the
number is *for*.

## Sharpest attack (≤150 words)

`beam_divergence_coherent`'s error is not the T21 edge-fringe — it is the
finite-comb grating-lobe artifact of the Δθ_sample-spaced angular sampling
itself, already named in this program's own record (exp-046's
`effective_aperture_lobe_census`; T21's Iteration-22 synthesized-aperture/M²
reframing). That mechanism's natural length scale is Δθ_sample vs. the
*observation*-window geometry (R_OUT/GUARD_OUT/W_FLANK, or the synthesized
aperture w₀/cosθ₀), not `A=752` — the *source*-aperture edge offset that
governs T21's single-angle fringe. A rough check: at n=41/FWHM=20°/450nm,
the grating-lobe offset λ/(Δ(sinθ))≈425 cells lands nowhere near `A=752`. §2.1
applies one A-based period table to all three functions uniformly.
Idealization 4 concedes the mechanisms differ, but its only protection,
P-NCONV26-1b, tests relative *severity* (n\* count), not whether §2.1's own
λ/θ₀ *ordering* — what P-NCONV26-2 actually scores — is even the right
predictor for the coherent case. P-NCONV26-2 is not stated as scored
per-function, so a strong incoherent fit could mask a weak coherent one
inside one pooled correlation.

## Verified independently (recomputed, not taken on faith)

- **§2.1 table, 3 of 9 entries recomputed from `A=752` and `CPL`:**
  450nm/36°=1.4127°, 600nm/38°=1.9338°, 750nm/40°=2.4865° — all match the
  proposal to 4 decimal places (script run against
  `experiments/042-t21-magnitude-bridge/design_geometry.py` directly).
- **Ceiling derivation:** Δθ_req=1.4127/10=0.14127°, n_req=100/0.14127+1≈709
  — correct; falls between 641 (9.04 samples/period, just short) and 1281
  (18.08 samples/period, ≈1.8×) as claimed.
- **Fringe survives in the raw integrand, not just the derived ratio:** FFT
  of both `edge_diffraction_c_empty_corrected(θ)` and `|E(OBJ_Y,θ)|²` over
  θ∈[35°,41°] (0.01° step, degree-4 detrend) peaks at the bin nearest
  1.93°, consistent with the predicted period at this FFT resolution. This
  is the one number the whole §2.1 Nyquist argument for the *incoherent*
  functions rests on, and it holds up under independent recomputation.

## Reciprocity / passivity / causality (charter item d)

None applicable, and none manufactured. This cycle changes no material law,
injects no new source, and modifies no engine physics — it re-evaluates an
already-committed, already-validated desk propagator (`_G_for`/`field_and_h`,
whose obliquity/Faraday-consistency was this seat's own Iteration-19
correction) at different quadrature orders `n`. `A`, `D_SP`, the taper, and
the propagator kernel are all held fixed; only the number of angular samples
changes. There is no field configuration here that could violate reciprocity
or passivity, and nothing propagates faster than `c` in a purely analytic,
non-causal (steady-state phasor) desk calculation that was never claiming to
model transients. Idealization 5 states this scope correctly.

## Verdict

**support-with-changes.**

The audit is well-posed, honestly hedged (idealization 3 already flags the
analogy as its own falsifiable prior), and — for the two incoherent
functions — the reused T21 period model is independently verifiable and
correct, confirmed above by direct recomputation against the raw integrand,
not just the derived contrast. But the coherent function's own governing
mechanism is a distinct, already-named phenomenon in this program's record
with a different natural length scale, and the one test meant to keep the
two mechanisms from being conflated (idealization 4) doesn't actually check
whether §2.1's ordering transfers to the coherent case specifically — only
whether the coherent case is *more severe* than the incoherent one. As
written, a clean P-NCONV26-2 result could reflect the incoherent fit alone.

## Flip

Score P-NCONV26-2 as **three separate Spearman correlations** (one per
function, each own ≥0.70 bar), not one pooled statistic across all
27 function×cell points — and report, alongside §2.1's A-based period table,
the grating-lobe offset λ_cells/(Δθ_sample(n,fwhm)_rad·cosθ) at n=41 for the
9 FWHM=20° cells, compared against `GUARD_OUT+W_FLANK` (263 cells) rather
than `A`. If the coherent function's own difficulty ordering correlates
comparably well against ITS mechanistically-appropriate scale, idealization
4's "track similarly" claim is actually validated rather than assumed; if it
diverges, that is exactly the falsifier this audit should have been built to
catch. With that split, this seat's verdict is unqualified support.
