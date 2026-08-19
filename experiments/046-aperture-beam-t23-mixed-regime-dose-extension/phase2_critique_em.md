# PHASE 2 — CRITIQUE · Panel Iteration 23 · Seat: ELECTROMAGNETISM

*Blind, parallel. Charter: field/wave behavior, impedance matching, energy
coupling; owns the reciprocity / passivity / causality bookkeeping and what T1
permits and forbids. Every number below was re-derived or re-run against the
cited repo file before it was written.*

---

## Steel-man (≤150 words)

The citations survive audit almost intact. I re-derived the Gaussian relation
independently: FT{exp(−y²/w₀²)} ∝ exp(−k_y²w₀²/4), so I(θ) ∝ exp(−k²θ²w₀²/2),
half-max at kθw₀=√(2ln2), Δθ=2√(2ln2)/(kw₀), **C=2√(2ln2)/2π=0.37478125** —
correct, and `width` in `lab/fdtd2d.py:152-155` really is w₀ (amplitude-1/e =
intensity-1/e²). Every w₀, z_R and N_F entry in §2.1 reproduces to 6 s.f.;
full-aperture N_F 518.0/388.5/310.8 confirmed. `profile="gauss"` has **zero call
sites repo-wide** — never exercised, never gated, exactly as claimed. The
anchor −0.010964794540566314 traces correctly to `experiments/041-t20-angle-audit/results.json`
`block_main.rows[19]` (θ=+40°, 600 nm), not to exp-042. Blocks B/C reproduce
exp-045 exactly (h_eff, τ, Biot, Kn, slip −5.3168%, 607×, 9.885 µm). T1
bookkeeping is sound: an additive source-current profile change touches no
material, so reciprocity, passivity and causality are genuinely untouched.

## Sharpest attack (≤150 words)

**Block A's oblique geometry is self-contradictory, and stage 16 is blind to
it.** §2.2 passes the table's w₀ to `add_line_source(width=…)` — the
*along-the-line* 1/e half-width (`lab/fdtd2d.py:152-155`,
`p = exp(−((yy−yc)/width)²)`). Tilted by θ₀ the perpendicular waist is w₀cosθ₀,
so the emitted divergence is Δθ/cosθ₀ (2°→2.61° at 40°): the runs are **not**
aperture-consistent at their own labels, 21–31% off across θ₀=36–40°. §2.1's
w_y = w₀√(1+(z_eff/z_R)²)/cosθ₀ assumes the reverse. Correct: z_R,true = z_R cos²θ₀
⇒ w_y = w₀√(1+(z_eff/(z_R cos²θ₀))²). Measured against exp-042's *own*
propagator (Gaussian source, 1/e² width at `PLANE_X`, θ₀=40°, FWHM=2°):
**162/215/269 cells** at 450/600/750 nm; my form gives 161.7/215.2/268.8, §2.1
gives **210.54/280.54/350.57 (+18–30%)**. That w_y sets P-TH23-A2's ≤5% band.
S16-a runs at θ=0°; S16-b checks centroid only — no gate tests an oblique waist.

## Verdict

**support-with-changes.** The cycle is worth running — Blocks B and C verified
clean, the T1 statement is honest, the cost is trivial — but Block A cannot be
read as written. Mandatory changes, each with the evidence that forces it:

1. **Fix the obliquity projection** (attack above). Either pass
   `width = w₀/cos θ₀` so the perpendicular waist is w₀, or keep `width = w₀`
   and correct §2.1's w_y to w₀√(1+(z_eff/(z_R cos²θ₀))²). State which, and
   re-issue the table. Add an S16 gate at θ₀=40° that measures the *width*, not
   just the centroid; the present gate set cannot fail on this defect.
2. **P-TH23-A3 is arithmetically impossible and already falsified.** The grid is
   3λ × 3θ₀ × 4 FWHM = 36 (`experiments/042-t21-magnitude-bridge/run.py:89-91`),
   so FWHM≤10° is **27** cells and FWHM=20° is **9** — not the "24" and "12" the
   band is written against. I pre-computed the proposed reading with exp-042's own
   `_G0_for`/`_src_amp`/`window_means` machinery (Gaussian aperture, single angle,
   corrected E/H, unaimed): only **11 of 27** FWHM≤10° cells land within 3% of the
   committed `C_coherent`, all nine FWHM=2° cells miss by 57–966%, and three
   (600/36°, 750/38°, 750/40°) **flip sign**. A3's own hard-falsification clause
   fires before the run. Rewrite or drop it.
3. **Disclose the convention mismatch in A3's target.** `block_beam.rows`'
   `C_coherent` was computed under the *superseded* obliquity-on-E convention;
   exp-042 committed **no** corrected coherent function (`design_geometry.py` has
   `beam_divergence_incoherent_corrected` at :279 but no coherent twin, and
   `phase5_erratum.block_beam_corrected` stores only `C_incoherent`). I measured
   the convention shift at up to **2.58%** (600 nm/38°/2°) — it alone consumes
   most of a 3% band.
4. **P-TH23-A1 is close to a geometric tautology, not a test of coherence.**
   Under A-unaimed the beam peaks at 792+walk = 954–979, i.e. inside the guard
   (78–185) or the +flank window (185–263, `lab/ambient.py:42-50`), while the
   object window (|y−792|≤78) sits in the beam's exponential wing. B_obj ≪ B_flank
   forces C→−1 whatever the physics. My precompute: 36/36 above C_THR, |C| =
   0.05–0.999. Switch to A-aimed and the *same* cells give **+2.7 to +4.6×10⁶** —
   opposite sign, seven orders of magnitude. A Weber contrast whose reference
   window is narrower than the beam offset is not a contamination measure; say so,
   and report A-aimed as a co-primary, not a footnote.
5. **P-TH23-A7 is ill-conditioned by ~360×.** Runs 8/9 sit at C_empty ≈ −0.997 /
   −0.947, so (1+C_empty) ≈ 2.8×10⁻³ / 5.3×10⁻². Dividing by that to "recover"
   exp-041's −0.05815337265493213 (verified: `block_objpresent.rows[1].C_sponge`)
   amplifies any error 360-fold. Drop it or widen the band by that factor.
6. **Two arithmetic slips.** §2.1 row 450 nm/FWHM=2° prints w_y = **199.33**; its
   own stated formula gives **210.54** (and the corrected formula 161.7) — it
   matches neither. Idealization 2's "waist is only **1.07–1.34 λ**" at FWHM=20°
   is dimensionally impossible: w₀/λ = C/Δθ = **1.0737 at all three λ**, by
   construction. §1 quotes the N_F floor as 0.32 where §2.1's table gives 0.24.
7. **Cross-platform reproducibility of S16-c.** A ≤1×10⁻¹² gate on a 1400-step
   FDTD result is a same-platform bit-reproducibility claim; state it as relative
   and name the reference platform, or the gate will fail for a reason that has
   nothing to do with this cycle.

Charter-specific findings, for the record: (a) reciprocity/passivity/causality
are untouched — `add_line_source` only appends to `Sim.sources`, no update
coefficient changes; (b) the Gaussian's evanescent content at the narrowest
waist (w₀=1.0737λ) is exp(−(πw₀/λ)²) ≈ 1.2×10⁻⁵ in amplitude, so no
non-propagating power is smuggled in — the paraxial idealization is honest at the
level claimed; (c) **S16-a is a legitimate absolute identity gate** per PANEL.md's
Phase-4 requirement (FDTD w(z) vs a zero-free-parameter closed form, with the
propagation reaching 1.03 z_R so w grows 43% — a real lever, not a null test) —
but its parameter point (θ=0°, w₀=2λ, Δθ=10.7°) is chosen where the block's
actual defect vanishes, which is why change 1 above is mandatory rather than
advisory.

## Flip

Set `width = w₀/cos θ₀` in every oblique Block-A call (and re-derive §2.1's w_y
accordingly), and add one S16 stage that gates the *1/e² width* of a θ₀=40°
Gaussian at `PLANE_X` against w₀√(1+(z_eff/(z_R cos²θ₀))²) to ≤3%. With that
single change the block measures the beam it claims to measure and my verdict
goes to **support**; the remaining items (A1's pointing degeneracy, A3's cell
count and precomputed falsification) are prediction-bookkeeping the Director can
resolve at Phase 3 without new cost.
