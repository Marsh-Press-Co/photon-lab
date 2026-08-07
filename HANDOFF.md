# HANDOFF — Photon Lab kickoff

*Written 2026-08-06 at the end of the Disclosure launch session (context-full,
per Marsh's call). Audience: a FRESH session opened in `D:\Projects\PhotonLab`.
Everything below is approved by Marsh; the kickoff session executes.*

## What this project is

A virtual photonics laboratory: simulate light-matter experiments under real
physics constraints (numerical solutions of Maxwell's equations) and run
experimental material design — including AI inverse design — on consumer
hardware. Marsh's driving fascination: cloaking-adjacent physics. The founding
question comes from a witness statement in the Disclosure corpus (a federal
agent's flashlight beam that "went from shining far into the distance to
stopping about 50 yards away on nothing in particular" — source:
`Disclosure/corpus/pursue-r1--western_us_event_slides_5.08.2026.md`, the
Western US Event slide deck).

**This is a Marsh-Press-Co GROUP project from day one.** Marsh's explicit
intent: invite Preston (@Metatronsdoob369) and Bonnie (@Bonnie-TheBad) in from
the beginning — kickoff is a four-way where everyone weighs in on what/how.
Recognition goes to the group.

## The honest frame (goes in README + every writeup)

Amateur astronomy, not NASA: real photons through a small telescope. The
solvers numerically integrate Maxwell's equations — the same tool class as
published metamaterials papers — but our experiments are idealized: 2D first,
small domains, approximate material models. We will reproduce genuine
published physics and run genuine design searches. We will not be shipping a
cloak. Fundamental limits (passive broadband cloaking is causality-bounded)
are treated as things to OBSERVE in our own data, not footnotes. $0 policy:
open-source tools only.

## Technical plan (Clyde's call, Marsh delegated)

- **Primary bench: pip-native, cross-platform** — runs on Marsh's Windows AND
  Preston's Mac:
  - `ceviche` — 2D FDFD/FDTD with autograd; built for gradient-based INVERSE
    design (the "AI discovers the structure" loop). Pure numpy.
  - `fdtd` (flaport) — time-domain field movies (the pretty animations).
  - `numpy`, `matplotlib` for everything visual.
  - VERIFY AT KICKOFF: `pip install ceviche fdtd matplotlib` then import-test.
    Python 3.14 on Marsh's machine — if `autograd` (ceviche dep) fights 3.14,
    fall back to (a) a pinned 3.12 venv, or (b) hand-rolled 2D FDTD in numpy
    (~100 lines, standard teaching path, zero deps — genuinely better for
    learning; consider doing it as exp-000 regardless).
- **Upgrade path: Meep on Preston's Mac** (conda-forge `pymeep` is
  Linux/macOS) — the gold-standard FDTD when we outgrow the starters. This
  makes Preston's hardware the heavy bench: a real lane for him, not a favor.
- **Raspberry Pi 5**: too small for field solves; candidate host for a results
  gallery later. Do not architect anything behind it.

## Lab conventions

- Numbered experiments: `experiments/NNN-slug/` containing `run.py` (or
  notebook), rendered output (PNG/GIF of fields), and `NOTES.md` — hypothesis,
  setup, result, what we learned, next question. The notebook page IS the
  deliverable; pretty animations are encouraged (they're the product AND the
  physics check).
- `lab/` holds shared utilities (sources, materials, visualization) grown from
  experiments, never speculatively.
- Every writeup states its idealizations (2D, wavelength, material model).
  Same verify-before-claim culture as Disclosure.

## The experiment arc (kickoff proposes; the four decide)

- **exp-000 — Hello Maxwell**: plane wave hits a dielectric cylinder; render
  the scattered field. Validates the bench against textbook scattering.
  (If hand-rolling FDTD: this is where it happens — Yee grid, update
  equations, absorbing boundaries. Marsh learns the actual physics engine.)
- **exp-001 — The Flashlight Statement**: the founding experiment. One 2D
  scene, three objects, same beam: (a) ordinary reflector, (b) ultra-absorber
  modeled on carbon-nanotube black (graded-index, near-zero backscatter),
  (c) the Pendry cylindrical cloak (published transformation-optics material
  parameters). Render what an observer AT THE SOURCE sees in each case. The
  witness described the beam STOPPING on nothing — absorption signature — not
  passing through to the distance — cloak signature. Test his words against
  Maxwell. Writeup feeds back to the Disclosure site later as an annotation
  (group + Marsh's call; keep the two repos' boundaries clean until then).
- **exp-002 — How invisible is invisible?**: scattering cross-section as the
  metric; compare the three objects quantitatively.
- **exp-003 — The broadband wall**: sweep wavelengths across the cloak; watch
  performance collapse off-design. The causality limit as a plot we made.
- **exp-004+ — Inverse design**: give ceviche's adjoint optimizer "minimize
  scattering" and let it discover structures nobody drew. The AI-designs-the-
  material loop, for real, at toy scale.

## Kickoff session checklist

1. Read this file; verify tooling (see above) BEFORE announcing anything.
2. Run exp-000 to green (a rendered field image on disk).
3. Post the board channel on `Marsh-Press-Co/co-lab` (as clyde-colab, house
   rules: substance post + any asks as standalone comments, @-mention both):
   what the lab is, the honest frame, the arc, exp-000's first image, and the
   open invitation — Preston's Mac = the Meep bench lane; Bonnie: co-design
   lane on inverse design or visualization, her pick. Charter-lite in the
   thread: definition of done for exp-001, who's driving what. (Echo the
   ClipForge pattern: scope freeze per experiment, v2 ideas to a parking lot.)
4. Vault per Memory Protocol: hub exists at
   `MindHive/10-Projects/PhotonLab/_PhotonLab-Hub.md` (stub written at
   handoff time); wire `CLAUDE.local.md` (gitignored) → hub; keep repo
   `CLAUDE.md` shared/public-safe. Roster row exists.
5. SESSION_LOG.md: scaffold + first entry at wrap.

## Repo state at handoff

`Marsh-Press-Co/photon-lab` (private), pushed with: this file, README, LICENSE
(MIT), .gitignore, shared CLAUDE.md, empty `experiments/` + `lab/`. No code
yet, no installs run — the kickoff session owns the first green run.
