# PHASE 2 — CRITIQUE · QUANTUM OPTICS · Panel Iteration 23 (candidate exp-046)

*Blind parallel critique. Charter: non-classical absorption, state-dependent or
coherent interactions; mechanisms enter the bench only as effective classical
parameters. Block A is this seat's own Iteration-19/20 proposal (live thread T21),
and the proposal's headline contradicts this seat's own committed prediction —
adjudicated below on the physics, not on precedent.*

---

## Steel-man (≤150 words)

The core coherence claim is **correct**, and it defeats my own prior call.
`beam_divergence_coherent` (`experiments/042-t21-magnitude-bridge/design_geometry.py:337-355`)
sums √w-weighted complex fields through a *linear* propagator, so by linearity
E_tot = G @ [P(y)·S(y)], with S(y) the Fourier transform of the Gaussian amplitude
angular spectrum — i.e. an effective **Gaussian aperture envelope**, untruncated
(P(y)≈1 across it). I measured its 1/e amplitude half-width at all 24 (λ,θ₀,FWHM)
cells: it *is* the diffraction-limited waist. So "a coherent Gaussian angular
spectrum over a wide aperture already IS the diffraction-limited single mode"
holds. Reproducing Block A analytically on exp-042's own propagator and reduction:
**36/36 cells above C_THR, 35/36 at ≥20× the corrected incoherent value,
min|C| = 0.0323**. P-TH23-A1 passes; my Iteration-20 "lands near the incoherent
reading" is refuted. Conceded. `profile="gauss"` is indeed never exercised
(grep-confirmed) — stage 16 is warranted.

## Sharpest attack (≤150 words)

**Block A's waist is wrong by 1/cosθ₀, and it breaks the proposal's own headline.**
`add_line_source` builds `p = exp(-(((yy-yc)/width)**2))` along the source **line**
(`lab/fdtd2d.py:152-156`), so a beam tilted θ₀ has true waist `width`·cosθ₀; a real
Δθ-divergence emitter has y-footprint w₀/cosθ₀. The proposal applies exactly this
stretch at the *observation* plane (`phase1_proposal.md:125-126`) and omits it at the
*source* — so §2.1's w₀/z_R/N_F and §2.2 runs 4–9's `width` args are all 1.24–1.31×
too small, injecting 24–31% excess divergence. Verified at matched convention against
committed `C_coherent`: **16 of 27** FWHM≤10 cells exceed A3's 3% band with
`width`=w₀ (up to 960% at 600 nm/38°/2°) — A3's hard-falsification clause fires —
versus **1 of 27** with w₀/cosθ₀. A4 also fails: the fix drops 7/9 FWHM=20 gaps
below 2%, tripping A3's "replica explanation is wrong" clause.

**Supporting defects.** (i) The FWHM partition is **27/9**, not "24"/"12"
(`experiments/042-t21-magnitude-bridge/run.py:89-91`; verified in `results.json`).
(ii) A3 names no obliquity convention: `phase5_erratum.block_beam_corrected` has
**no coherent column**, so `C_coherent` exists only under the *superseded*
obliquity-on-E recipe while §6 declares corrected E/H primary — the erratum's own
"not a methodologically legitimate combination". (iii) §2.1's 450 nm/FWHM=2 w_y
reads 199.33; the stated formula gives **210.54** (199.35 uses cos 36°, not cos 40°).
(iv) Scope: both exp-042 columns share the same Δθ and differ in *étendue* — Block A
is the M²=1 endpoint, the incoherent column is a Gaussian–Schell source of M²≈2.8–47.
A1 therefore adjudicates a construction question, **not** T21's contamination risk
for a real (M²≫1) flashlight; the Schell bridge is still the only thing that closes it.

## Verdict

**support-with-changes.**

The cycle is sound in kind and Block A is the right instrument; the physics claim
this seat contested is correct and I withdraw the Iteration-20 prediction. But as
written Block A does not build the object it claims to, and P-TH23-A3/A4 will
register a pre-registered failure caused by a projection bug rather than by physics —
which would be recorded in LOGBOOK as a refutation of the reinterpretation itself.
That must be fixed before Phase 3, not after Phase 5.

## Flip

Replace the source-plane width everywhere in Block A with

> **w₀^(y) = 0.3747808 · λ_cells / (Δθ_rad · cos θ₀)**

and re-derive §2.1's z_R, z_eff/z_R, w_y(z), N_F and §2.2 runs 4–9's `width` from it
(A3 then passes at 26/27 FWHM≤10 cells). Alongside: fix the 27/9 counts, state A3's
obliquity convention explicitly (compare committed-convention Block A against
committed `C_coherent`, or generate a corrected-convention coherent column first),
and restate P-TH23-A1's scope as the **M²=1 endpoint**, not a T21 contamination
re-score. With those, this seat's verdict is unqualified support.
