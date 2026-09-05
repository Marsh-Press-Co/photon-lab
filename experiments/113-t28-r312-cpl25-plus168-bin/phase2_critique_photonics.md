# Phase 2 Critique — PHOTONICS (exp-113, Panel Iteration 90)

*Fresh sub-agent, blind context. Charter: surface interaction, absorption
spectra, angular dependence, scattering cross-sections — is the proposal's
optical response coherent as stated, across wavelength and angle? I have
not seen and did not seek out any other seat's Phase-2 output this cycle.
All numeric claims below were independently re-derived this session —
`python3 run113.py --verify-geometry` and `--predictions-only` re-run
fresh (both reproduce the document's own transcription exactly), bin
index 46/168.75° figures re-read directly from
`experiments/110-.../results.json` (not taken from the document's own
prose), and the box_a geometry re-computed directly from
`geom_fixedabs_cpl()` rather than trusted from the parameter table.*

## Steel-man (≤150 words)

Every number I re-derived reproduces exactly — no R4-class transcription
defect anywhere in this document. More importantly for my own charter,
the two Reconciled-queue instrument fixes are applied at the *correct*
surgical point: Check B's CPL_RATIO normalization is applied only where
raw, non-ratio `sections.py` output is compared **across** `cpl` (the
named-bin delta), leaving the shared, trust-suite-gated library itself
untouched for every other caller that compares **within** one `cpl`,
where the factor legitimately cancels — exactly the right scope, not an
overcorrection. Check C's null population is freshly computed for
r=312's own committed arrays rather than reused from r=156's Phase-5
scan, honoring R30's own text ("its own computable null population").
And the box_a/margin construction, which I independently re-derived from
`geom_fixedabs_cpl` rather than trusted, genuinely is self-similar in `r`
(clearance/R_COAT is r-invariant) — the family is coherently defined.

## Sharpest attack (≤150 words)

I re-computed box_a's clearance past the coat surface in **wavelengths**,
not cells, at both radii (`clearance_cells / cpl`): **3.2λ at r=156,
6.4λ at r=312 — exactly the kappa_ratio=2.0 scale-up, independent of
cpl.** "Margin=32" is not the same physical near-field test at 2x scale;
it is the same *proportional* margin, which places box_a **twice as far,
in wavelengths, from the shell** at r=312 as at r=156. Any genuinely
near-field/evanescent sub-wavelength feature (decay length set by λ, not
by r) would be markedly more attenuated by the time it reaches box_a at
r=312 — a scale confound orthogonal to, and undisclosed alongside, the
CPL_RATIO grid-unit confound this cycle correctly fixes. The document
frames r=312 as this bin's direct "mirror companion," but nothing in its
Idealizations discloses that "the same test" is being run at a
physically different near-field depth. This doesn't break this leg's own
internal falsifiability (each check scores against its own r=312/cpl=20
baseline), but it undercuts any future cross-r interpretation the
"companion bin" framing invites.

## Verdict: **support-with-changes**

The instrument itself is sound for what it self-contained-ly measures;
the gap is a missing disclosure, not a broken check.

## Parameter change that would flip to plain support

Add one Idealization item (computed, not hand-typed, matching this
cycle's own R4/VISION-addition convention) stating the box_a clearance in
wavelengths at both radii (3.2λ vs 6.4λ) and cautioning that r=156 and
r=312 outcomes should not be read as testing the same near-field depth
before Phase 5 draws any cross-leg conclusion from comparing this bin's
outcome to exp-112's own `−146.25°` result.
