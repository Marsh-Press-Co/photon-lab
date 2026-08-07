# Photon Lab — Session Log

Newest on top. Current state lives in the vault hub; this is history.

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
