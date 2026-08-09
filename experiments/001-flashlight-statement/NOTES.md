# exp-001 — The Flashlight Statement

**2026-08-09 · driver: Clyde (solver) · Bonnie (witness figure) · Preston
(acceptance test) · status: predictions committed, runs pending**

The founding experiment. A federal agent's flashlight beam "went from
shining far into the distance to stopping about 50 yards away on nothing in
particular" (Disclosure corpus,
`pursue-r1--western_us_event_slides_5.08.2026`). Three physical hypotheses
dress the same object; Maxwell's equations judge which one matches his
words.

## The scene

One PEC core (r = 0.9 µm), dressed three ways, plus the empty reference:

| Scene | Dressing |
|---|---|
| `empty` | nothing — the reference each λ is normalized against |
| `reflector` | bare metal — the ordinary object |
| `absorber` | graded-black coat, 0.9 → 2.34 µm (the designed sponge, suite stage 7) |
| `cloak` | Schurig reduced cloak, shell 0.9 → 2.7 µm (suite stage 5), PEC flush at r1 |

Same beam, same numerics (560×560 cells, courant 0.32, 3200 steps), swept
across **450 / 600 / 750 nm** — because the agent's flashlight was white
light, and a single-wavelength match is not a match.

Measurements per scene per λ, all vs that λ's empty reference:
- **observer return** — total angle-integrated backward flux at the source
  plane (the camera the witness *is*)
- **beam-behind** — intensity in a fixed box past the object vs empty
  space (does the beam continue into the distance?)
- **scattered RMS** — envelope deviation in an annulus outside every
  dressing (how loudly does the object announce itself?)

## Predictions — on the record BEFORE the first run

*(This file is committed to git before `run.py` executes; the commit
timestamps are the proof.)*

- **P1 (reflector):** returns ≥ 5× the absorber's flux at every λ;
  beam-behind ≤ 0.15 at every λ; behavior roughly wavelength-flat.
- **P2 (absorber):** observer return ≤ 0.02 absolute (camera-floor
  territory) at every λ; beam-behind ≤ 0.2; wavelength-flat. Darkness in
  both directions — the beam stops, and nothing glints.
- **P3 (cloak, on-design 600 nm):** beam-behind ≥ 0.5 (the smoke test
  measured 0.64) — the beam visibly *continues* — with scattered RMS below
  the bare reflector's.
- **P4 (cloak, off-design 450/750 nm):** the disguise cracks — beam-behind
  drops ≥ 30% relative to its 600 nm value at both ends of the sweep, and
  scattered RMS rises ≥ 1.5× vs its 600 nm value. The causality wall,
  previewed (exp-003 measures it properly).
- **P5 (the verdict):** the witness's words match the **absorber**
  signature — beam stops + nothing returns + no wavelength dependence — and
  specifically do NOT match the cloak, whose entire function is that the
  beam *continues* "into the distance," which is the opposite of what he
  described. The reflector fails on the glint.

## Idealizations (per lab convention)

2D TMz, single-frequency CW per run (three runs approximate the white-light
sweep), reduced cloak parameters with the μ_r ≥ 0.05 stability clamp,
graded-loss boundaries, soft tapered plane source, one observer plane (no
time gating of multiple bounces), λ/15–λ/25 resolution across the sweep.

## Results

*(Appended after the run — the section above this line was committed
first.)*
