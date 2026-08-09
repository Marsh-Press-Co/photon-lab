# Photon Lab — Session Log

Newest on top. Current state lives in the vault hub; this is history.

## 2026-08-08 — exp-001 groundwork: lab/ engine + 14/14 trust suite

**Shipped/Done**
- `lab/fdtd2d.py` — engine grown from exp-000: conductivity, PEC,
  **anisotropic inverse-μ tensor** (B-then-H scheme, staggered evaluation),
  plane/Gaussian sources, Poynting line monitors, `spatial_wavelength`.
- `lab/materials.py` — dielectric cylinder, PEC disk, absorber **STUB**
  (Bonnie's lane preserved), Schurig/Cummer reduced TMz cloak (clamped,
  derivation + stability arithmetic in docstrings).
- `lab/validation/` — 5-stage trust suite + `VALIDATION.md`; board #31
  status note posted. Merged `f016384`.
**Verified (14/14)**
- exp-000 regression exact · Fresnel R 0.098 (theory 0.111±0.025) ·
  matched half-space R≈0.018 through scalar AND tensor μ paths ·
  scattered-field cross-solver corr 0.93 (flaport fdtd) / 0.96 (ceviche) ·
  cloak smoke −34% scattered RMS, beam-behind-object 0.057 → 0.641.
**Decisions**
- Cross-solver checks compare SCATTERED fields (scene − own vacuum) —
  total-field comparison caps correlation on source-profile differences.
- Cloak smoke framed as MACHINERY check (bar 0.75); cloak *quality* is
  exp-002/003's job. PEC flush at inner wall per canonical setup (the
  2-cell gap cost 11 RMS points).
- Bonnie's offered lanes untouched: absorber stub only, no viz module.
**Board (same night — the four-way arrived)**
- **Mandate (canon, recorded on #31):** Marsh in-session + Preston to Bonnie —
  the AGENTS drive experiment discussion/design; humans seed ideas. Design
  loop proposed and posted: predict-before-run → solver build (Clyde) →
  Evidence-Gated artifacts → observer/metric verdict (Bonnie) → nature
  arbitrates disagreements → NOTES.md per loop.
- **Bonnie's lane: viz + observer camera** (her amendment; all three
  materials back with Clyde). Contract: solver emits observer record +
  artifacts (her schema PR, Clyde veto); she never reaches solver internals;
  Clyde never touches figures. Her figure house rules adopted. She's
  replicating the 14/14 suite on macOS (3 solvers × 2 OSes).
- **Preston's role, his call: the acceptance test** — non-physicist reader
  of every figure ("if he can't answer the witness question from the figure,
  the figure failed"). First specific handed to him: read v5_cloak.png cold,
  report what it needs. Meep lane parked, zero pressure.
- **exp-001 DoD amended + freeze window:** three scenes + observer figure +
  NOTES + bench cross-check (✅) + **3-λ sweep (450/600/750)** — the witness's
  flashlight was white light; single-λ matches don't count. Prediction on
  record: the sweep cracks the cloak's match, not the absorber's. Frozen in
  ~24h barring human objection; fourth panel (adjoint discovery) parked.

**Deferred/next**
- Freeze window closes → build exp-001 scenes; Bonnie's schema PR + viz
  extraction PR; her macOS numbers.
- Parking lot: TF/SF injector, true PML, finer-grid cloak runs, fourth
  panel, Disclosure physics-annex (humans' call), Blender/UE 3D
  presentation when a design earns it.
**Notes/gotchas** (promoted: pointer now in repo CLAUDE.md)
- FFT λ on short strips quantizes (190 samples → 19.0/21.1, never 20.0);
  use `spatial_wavelength` (zero-pad + parabolic).
- Reflection monitors close to the interface — beam-diffraction losses
  cancel between reference and scene runs.
- flaport `fdtd` + ceviche both run the shared scene on Py 3.14 without
  incident (Object accepts ndarray permittivity; fdfd_ez solve fine).

## 2026-08-06 — Kickoff: bench verified, exp-000 first light, board live

**Shipped/Done**
- Bench verified **native on Python 3.14** (no 3.12 fallback needed): `ceviche`,
  `fdtd`, numpy 2.5.1, matplotlib 3.11.1 all import clean in the repo `.venv`.
- **exp-000 Hello Maxwell** (`dee58b0`): hand-rolled 2D TMz FDTD (Yee grid,
  plain numpy, no solver library) — 600 nm plane wave vs n=2 cylinder (r = 2λ).
  Deliverables: `field.png` (hero render), `setup.png`, `wave.gif` (140
  frames), `NOTES.md`, `run.py` with three built-in self-checks.
- **Board channel live: co-lab #31** — substance post (what the lab is, honest
  frame, arc, first-light links, charter-lite) + standalone asks:
  Preston → Meep heavy-bench lane + arc review; Bonnie → exp-001 absorber
  co-design OR `lab/` viz system, her pick.
- Live watchers armed (board ~90 s poll + Telegram).

**Decisions**
- exp-000 = hand-rolled engine (the handoff's sanctioned option, taken
  deliberately): Marsh learns the actual physics engine, zero dependency risk.
  Libraries reserved for exp-001+ and cross-validation.
- Figure house style: GitHub-dark surface (`#0d1117`) + Crameri `berlin`
  diverging colormap — renders blend into the repo page in dark mode.
- Proposed exp-001 definition of done (on the board, awaiting the four):
  three rendered scenes + one observer-at-the-source comparison figure +
  NOTES.md with idealizations + cross-check vs ≥1 library solver.

**Verified**
- Wavelength by FFT: set 20.0 cells, measured 20.0 cells — 600 nm exact.
- Stability: max|Ez| = 2.50, finite over 1400 steps. Shadow ratio 0.48.
- All three renders eyeballed; one contrast bug on setup.png caught and fixed
  before commit. The exit-face hot spot = **photonic nanojet**
  (Chen/Taflove/Backman 2004) — published physics reproduced unprompted.

**Deferred/next**
- Four-way weigh-in on #31 → scope freeze → build exp-001 The Flashlight
  Statement.
- Cross-validate the exp-000 scene through `ceviche` + `fdtd`.
- Parking lot: TF/SF plane-wave injector, true PML, scattering cross-section
  machinery (exp-002's metric).

**Notes/gotchas**
- Python 3.14 + autograd/ceviche: **no fight** — the handoff's headline risk
  didn't materialize. Installed and imported clean, first try.
- PIL `optimize=True` collapses duplicate GIF hold frames (165 written → 140
  stored) — intended dedup, not a bug.
