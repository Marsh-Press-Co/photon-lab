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
first; `0ac8a89` is the proof of order. 12 runs, 9.8 min, all artifacts
through the Evidence Gate.)*

| Scene | λ (nm) | Observer return | Camera floor | Beam-behind | Scattered RMS |
|---|---|---|---|---|---|
| reflector | 450 | 0.0671 | 0.0024 | 0.042 | 0.702 |
| reflector | 600 | 0.0646 | 0.0013 | 0.057 | 0.703 |
| reflector | 750 | 0.0641 | 0.0009 | 0.078 | 0.702 |
| absorber | 450 | **0.0024 (= floor)** | 0.0024 | **0.015** | 0.755 |
| absorber | 600 | **0.0013 (= floor)** | 0.0013 | **0.018** | 0.737 |
| absorber | 750 | **0.0009 (= floor)** | 0.0009 | **0.017** | 0.750 |
| cloak | 450 | 0.0666 | 0.0024 | 0.303 | 0.532 |
| cloak | 600 | 0.0425 | 0.0013 | **0.636** | 0.463 |
| cloak | 750 | 0.0390 | 0.0009 | 0.695 | 0.419 |

### Predictions scored

- **P1 (reflector) — CONFIRMED.** Return 28–72× the absorber's; beam-behind
  ≤ 0.078 everywhere. Note: beam-behind drifts 0.042→0.078 across the sweep
  — longer wavelengths diffract more into the shadow, textbook behavior.
- **P2 (absorber) — CONFIRMED, at the strongest reading possible.** The
  observer return *equals the camera's empty-space floor at every
  wavelength* — to measurement precision, nothing comes back. Beam-behind
  1.5–1.8%: the beam stops. Wavelength-flat: white light changes nothing.
- **P3 (cloak on-design) — CONFIRMED.** Beam-behind 0.636; scattered RMS
  0.463 vs bare metal's 0.703.
- **P4 (cloak off-design) — HALF CONFIRMED, half refuted, and the refuted
  half is the finding.** At 450 nm the disguise cracked as predicted
  (beam-behind −52% relative). At 750 nm it *held* (+9%) and its scatter
  metric improved. The clamped, discretized reduced cloak fails
  **asymmetrically** across the spectrum — blue-side collapse, red-side
  robustness — which no prediction anticipated. Caveat logged before anyone
  over-reads it: grid resolution co-varies with wavelength in this sweep
  (λ/15 at 450 vs λ/25 at 750), so staircase numerics are entangled with
  cloak physics here. exp-003 must separate them (fixed cells-per-λ with
  scaled geometry) before the asymmetry is claimed as material physics.
- **P5 (the verdict) — CONFIRMED.** See below.

### The verdict

The witness said the beam went "from shining far into the distance to
stopping about 50 yards away on nothing in particular." Three clauses,
three measurements:

1. *The beam stopped* — beam-behind: absorber 0.017, cloak 0.64. A cloak's
   entire function is that the beam **continues** into the distance; his
   beam did not.
2. *On nothing* — observer return: absorber = camera floor (nothing to
   see, no glint, no edge); the cloak returns as much light as bare metal
   (0.067 vs 0.067 at 450 nm — the reduced cloak *glints*); the reflector
   is a lit surface, not "nothing."
3. *A flashlight* — white light. Only the absorber is wavelength-flat; the
   cloak's behavior swings by 2× across the visible band.

**Within this bench's idealizations, the statement describes an
impedance-matched broadband ultra-absorber — and specifically cannot
describe a transformation-optics cloak.** We have not shown what the agent
saw; we have shown which physics class his words belong to. Those are
different claims, and the lab makes only the second.

## What we learned

- The three-clause structure of the witness sentence maps one-to-one onto
  three independent measurements — the statement was *testable*, which is
  itself the finding that justifies this lab.
- "Invisible to an observer at the source" and "invisible from all angles"
  part ways dramatically: the absorber owns the first and fails the second
  (its shadow is enormous — scattered RMS 0.75, highest in the table); the
  cloak attempts the second and betrays itself on the first (the glint).
  exp-002 quantifies this properly with real cross-sections.
- The scattered-RMS metric conflates shadow with glint (the absorber
  "scatters" 0.75 by *removing* light, not radiating it). exp-002's
  machinery must separate forward-shadow from backscatter before
  cross-scene comparisons of that number mean anything.
- The reduced cloak's spectral failure is asymmetric — pending the
  resolution-controlled rerun, this is exp-003's opening question.

## Next

- Bonnie: the witness figure — three-panel observer view + the sweep, from
  these 12 artifacts (R1–R4 apply; the observer records carry the story).
- Preston: cold read of that figure — can a non-physicist see which object
  the witness described?
- exp-002: scattering cross-sections (separate shadow from glint).
- exp-003: the broadband wall, resolution-controlled (the asymmetry
  question).
- Parking lot: angled observer (witness geometry wasn't perfectly
  retroreflective), pulsed/time-gated illumination, absorber thickness
  sweep.
