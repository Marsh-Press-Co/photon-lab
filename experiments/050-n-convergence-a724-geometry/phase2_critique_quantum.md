# PHASE 2 — CRITIQUE (QUANTUM OPTICS) · Panel Iteration 27 · exp-050

## Steel-man (≤150 words)

The proposal gets the one thing my own prior debugging is entitled to police
exactly right: §2.0 restates the *corrected* `delta_step` criterion
(exemption on `|C(2n)|<C_THR`, not a floored ratio) verbatim from
`experiments/049-.../run.py:111-121`, not the original ill-conditioned
Phase-1 formula. Because that logic is a pure function of the two `C`
values with no geometry dependence, it cannot resurrect the
thousands-of-percent artifact I caught at Iteration 26 merely by moving to
`GEOM78` — the fix is structurally geometry-agnostic, and §2.3's regression
anchor (full 108-row `per_cell_summary` match at `GEOM_EXP042_OLD`, not a
worst-cell-plus-counts summary) is genuinely executable, unlike exp-049's
own P-NCONV26-0, which Red Team found dead on arrival. `converged_value`'s
n*-not-asymptote semantics (my own Iteration-26 finding) is also carried
forward correctly (§4 preamble). This is careful, load-bearing reuse of
exactly the machinery I am positioned to check.

## Sharpest attack (≤150 words)

§2.4 treats the A=752→724 shift as one benign, monotonic period
perturbation (T21's edge-diffraction fringe, EM's mechanism) — but the
coherent function's own hardest cells are governed by a *different*
mechanism I found at Iteration 23: `beam_divergence_coherent`'s n=41
grating-lobe replicas sit at `ΔY≈λ_cells/(cosθ₀·δθ)` — a function of
λ,θ₀,FWHM,n only, **not of A**, so the replica's absolute cell position
(±712–722 at 750nm/FWHM=20°) does not shift at all. What shifts is the
aperture: GEOM78's taper zone moves from `[712,752]` to `[684,724]`, so a
replica sitting near the taper's *mild* edge at A=752 now sits deep inside
GEOM78's taper — a qualitative windowing change the period argument cannot
predict in either direction. P-NCONV27-3/7's "same direction, comparable
count" central estimates rest entirely on the wrong mechanism for exactly
the cells the audit's own headline (P-NCONV26-1a/P-NCONV27-3) is about.

## Verdict: support-with-changes

## Parameter change that would flip to full support

Add one desk computation before Phase 4: evaluate the grating-lobe replica
offset `ΔY(λ,θ₀,FWHM=20°,n=41)` against GEOM78's own taper-zone boundary
(`A−TAPER=684` to `A=724`, vs the A=752 case's `[712,752]`) for all three
wavelengths, and disclose whichever direction it predicts as an explicit
idealization/prediction addendum for the 9 FWHM=20° coherent cells —
instead of letting §2.4's fringe-period argument stand in, unqualified, for
a mechanism it was never derived to cover.
