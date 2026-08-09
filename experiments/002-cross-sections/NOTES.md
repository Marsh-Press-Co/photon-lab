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

## Results

*(Appended after machinery passes stage 8 and the nine scene-runs execute.
Everything above this line was committed first.)*
