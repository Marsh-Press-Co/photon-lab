# exp-002 — How Invisible Is Invisible?

**2026-08-09 · driver: Clyde · status: predictions committed, machinery pending**

exp-001 proved its verdict with an observer camera and a beam-behind box —
but its scattered-RMS number conflated two different betrayals (the
absorber "scattered" 0.75 by *removing* light). This experiment builds the
proper currency: **scattering, absorption, and extinction cross-sections**
(2D: widths), separated into backscatter vs forward components, so
"how invisible" becomes one defensible number per object per wavelength.

## Method (machinery to be built: `lab/sections.py` + trust-suite stage 8)

Complex scattered field by phasor subtraction (scene − empty, same source
phase, from quadrature pairs — Hx capture added alongside Ez/Hy). A closed
four-face Poynting box around the object then yields:

- **σ_scat** — net *outflow* of scattered-field power through the box /
  incident intensity, split by face into backward / lateral / forward.
- **σ_abs** — net *inflow* of total-field power through the box.
- **σ_ext = σ_scat + σ_abs**, cross-checked against the **optical theorem**
  (extinction from the forward-scattering amplitude) — the machinery's
  self-consistency gate: two independent routes to σ_ext must agree.
- **Q_ext = σ_ext / (2 · outer radius)** — extinction efficiency, the
  invisibility ranking metric (each object normalized by its own
  silhouette).

## Predictions — on the record BEFORE the machinery exists

- **P1 (gates):** optical theorem holds within 12% on every scene
  (discretization tolerance); a lossless dielectric cylinder reads
  σ_abs/σ_ext ≤ 0.05 (the absorption channel must be silent on lossless
  objects).
- **P2 (absorber):** σ_abs/σ_ext ≥ 0.85 at every wavelength — it eats,
  it doesn't spray — and backscatter carries ≤ 10% of its (small) σ_scat.
- **P3 (cloak):** at 600 nm, the cloak posts the **lowest Q_ext of the
  three dressings** — cloaking quantified in the field's own currency. At
  450 nm it loses that rank (exp-001's asymmetric crack, restated in
  cross-section units); at 750 nm it keeps or nearly keeps it.
- **P4 (reflector):** Q_ext roughly flat across the sweep — the boring
  baseline that anchors the table.

## Idealizations

2D TMz widths (not 3D cross-sections); same clamp/resolution caveats as
exp-001 (resolution co-varies with λ — the controlled-resolution version
remains exp-003's job); box measurement in the near-to-mid field with
graded-loss walls rather than PML.

## Method amendments (recorded before results, per house practice)

- The "optical theorem" route was implemented as the near-field
  **incident×scattered cross-term integral** (its exact statement on a
  closed box) plus **box independence** as the second independent route —
  safer than far-field amplitude normalization. Both gated in stage 8.
- Stage-8 forensics found and fixed a phasor-convention bug in `lab/emit`
  whose signature was exp-001's "camera floor" (1.25% = sin²(ω/2)); post-
  fix the empty room reads 1e-4 and Fresnel agrees to three decimals.
  exp-001's observer *values* shift accordingly (verdict unaffected —
  the absorber still equals the floor at every λ); its rerun is queued.
- The absorber gate was recalibrated on first contact with the
  **extinction paradox**: any opaque disk's forward shadow lobe carries
  ~half its extinction (the PEC's Q≈2.2 is the textbook signature), so
  abs/ext ≈ 0.5 is correct physics, and the true absorber signature is
  backward silence.

## Results

*(12 runs, 9.7 min. Everything above the amendments line was committed
before the machinery existed; amendments before these numbers.)*

| Scene | λ (nm) | σ_ext (cells) | **Q_ext** | abs/ext | back_frac | box dev |
|---|---|---|---|---|---|---|
| reflector | 450 | 128.8 | 2.15 | −0.003 | 0.20 | 0.000 |
| reflector | 600 | 132.5 | 2.21 | −0.005 | 0.20 | 0.003 |
| reflector | 750 | 138.6 | 2.31 | 0.003 | 0.19 | 0.010 |
| absorber | 450 | 240.5 | 1.54 | 0.515 | **0.0000** | 0.000 |
| absorber | 600 | 240.0 | 1.54 | 0.512 | **0.0000** | 0.002 |
| absorber | 750 | 243.0 | 1.56 | 0.512 | **0.0001** | 0.001 |
| cloak | 450 | 92.8 | **0.515** | 0.003 | 0.28 | 0.010 |
| cloak | 600 | 69.1 | **0.384** | 0.011 | 0.26 | 0.004 |
| cloak | 750 | 54.5 | **0.303** | 0.000 | 0.31 | 0.000 |

### Predictions scored

- **P1 (gates) — CONFIRMED.** Box deviations ≤ 1.0% on all nine
  measurements; the lossless PEC's absorption channel reads ±0.5% (a
  production-run identity check passing for free); extinction routes agree
  to 0.2% in stage 8.
- **P2 (absorber) — half confirmed, half refuted, the refuted half being
  the extinction paradox** (see amendments): abs/ext is 0.51, not ≥ 0.85,
  because the forward shadow lobe is physics no opaque object escapes. The
  backscatter clause was beaten by three orders of magnitude: back_frac
  ≤ 10⁻⁴ vs the predicted ≤ 0.10. And σ_ext is flat to 1.2% across the
  sweep — broadband, as designed.
- **P3 (cloak) — first clause confirmed emphatically, second refuted with
  a discovery.** At 600 nm the cloak posts Q_ext = 0.384 — lowest of the
  three by 4–6×, cloaking quantified in the field's own currency. But it
  never "loses the rank" at 450: it degrades (0.515) yet stays lowest —
  and toward red it *improves monotonically* (0.303 at 750). Combined with
  exp-001's beam-behind trend, the reduced cloak is better at longer
  wavelengths in BOTH currencies. Working hypothesis for exp-003: its
  imperfections (clamp band, staircase, reduced-parameter mismatch) are
  **fixed-size defects**, electrically smaller at long λ — predicting
  performance degradation ∝ (defect size / λ)². The resolution confound
  (cells-per-λ co-varies) still rides along; exp-003's controlled design
  must separate the two.
- **P4 (reflector) — CONFIRMED.** Q_ext 2.15→2.31 across the sweep,
  drifting +7.6% — the boring baseline, wearing the textbook extinction
  paradox (Q ≈ 2) visibly.

### The finding

**"Invisible" has a direction.** Integrated over all angles, the cloak is
the better hider by 4× (it removes far less light from the world:
Q 0.38 vs 1.54). To an observer at the source — the witness geometry — the
absorber wins overwhelmingly: its backward spray is 10⁻⁴ of its
extinction, while the cloak throws 26–31% of its scatter *backward*, which
is exactly the glint exp-001's camera saw. Two philosophies of hiding:
the cloak is small-but-noisy, the absorber is big-but-silent-backward.
Any claim about invisibility must state *from where* — which is,
in retrospect, precisely why the witness's one-directional flashlight
statement was decidable at all.

## Next

- **exp-003 — the broadband wall, redesigned around tonight's discovery:**
  separate fixed-defect electrical size from grid resolution (fixed
  cells-per-λ, scaled geometry) and test the (defect/λ)² hypothesis
  against the monotonic red-side improvement.
- exp-001 observer-table rerun post phasor fix (values shift, verdict
  stands) — queued for a cloud shift.
- Parking lot: absorber-vs-cloak hybrid (black-lined cloak — eat the
  backward glint?), Q_ext vs incidence angle, near-to-far transform for
  true far-field patterns.
