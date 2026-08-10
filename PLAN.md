# Photon Lab — PLAN

Standard co-lab shared-repo file (AGENTS.md convention): Vision is the
owner's words, durable; Current state and Next work stay fresh — the PR
that does the work updates this file, never a separate chore.

## Vision (Marsh, 2026-08-08, in-session — verbatim)

> the vision i see is that we can simulate reality with precise mathmatics
> that should leave probability that an actual design would work the same
> in the real world. [...] i want you and bonnie to keep discussing and
> trying new ideas and experiments in a collaborative effort to create this
> cloaking material or color or whatever. my belief is that two independent
> agents can work together to design the material needed and test their
> hypothesis and from the results work out a new design and test those
> results and the loop continues.

Operating mandate (Marsh + Preston, on the record at co-lab #31): **the
agents drive experiment design and discussion; the humans seed ideas.**
The honest frame binds every claim: amateur astronomy, not NASA —
idealizations stated, limits observed in our own data, no cloak shipping
promised. The arc from 2D mechanism-truth toward real-world-plausible
designs runs: single-λ → broadband → 3D → tolerance-to-imperfection.

## Current state (2026-08-10, cloud shift)

- exp-000 Hello Maxwell ✅ — hand-rolled 2D TMz FDTD, first light, photonic
  nanojet reproduced (`experiments/000-hello-maxwell/`).
- `lab/` bench ✅ — engine (ε/σ/PEC + anisotropic-μ) with a 14/14 trust
  suite (`lab/validation/VALIDATION.md`), replicated on macOS to the digit;
  CI runs the suite on every push (ticker: co-lab #32).
- Lanes: Clyde = solver + materials · Bonnie = viz + observer camera ·
  Preston = acceptance test (non-physicist figure reader) · Meep heavy
  bench parked on Preston's Mac.
- exp-001 The Flashlight Statement: DoD proposed (3 scenes + observer
  figure + NOTES + 3-λ sweep), freeze window open ~24h from
  2026-08-09 04:00Z.
- exp-002 CONCLUDED — "invisible" has a direction (see below).
- exp-003 CONCLUDED (this shift) — the red-side improvement survives a
  resolution-controlled sweep but isn't the quadratic law guessed at; a
  non-monotonic bump at 480nm is the open thread into exp-004.

## Next work

- [done 2026-08-09] Artifact schema v0.1.0 — merged (`ba2cc7f`), verified
  on all three benches.
- [done 2026-08-09] Preston's cold read → house figure style **R1–R4**
  (shadows self-explain · orientation gizmo · panels work solo · witness
  view beside the map). His reads gate exp-001 figures.
- [done 2026-08-09, this PR] Artifact emitter (`lab/emit.py`): quadrature
  capture, angle-resolved observer camera (Fresnel-gated, suite stage 6),
  manifest from engine self-recorded scenes. First committed artifacts:
  `experiments/000-hello-maxwell/artifacts/{empty,cylinder}` — CI now runs
  the Evidence Gate on committed artifacts every push.
- [claimed: Bonnie] `lab/viz` extraction + observer camera rendering,
  carrying the Evidence Gate figure checker + R1–R4. Unblocked by this PR;
  exp-000 artifacts are her real data.
- [done 2026-08-09, this PR] **Graded-black absorber** — exp-001's object
  (b), designed and gated (suite stage 7, 5/5): R ≤ 0.2% across the
  450–750 sweep, observer return at the camera floor. Schema bumped 0.2.0
  (new builder row per the extension rule); exp-000 artifacts re-emitted.
- **exp-001 scope FROZEN 2026-08-09 (Marsh's word)**: three scenes
  (reflector / graded-black absorber / reduced cloak) + observer-at-source
  figure + NOTES + 3-λ sweep. Future freezes: agent consensus per
  AGENTS.md amendment (this PR).
- [done 2026-08-09] **exp-001 The Flashlight Statement** — verdict:
  absorber, 4.5/5 pre-registered (PR #5). Witness figure (Bonnie) + agent
  cold read close the presentation half.
- [done 2026-08-09] **exp-002 How Invisible Is Invisible** — cross-section
  machinery (stage 8) + 12-run sweep. Finding: "invisible" has a
  direction — cloak wins all-angle 4×, absorber wins source-observer by
  orders of magnitude; cloak monotonically better toward red.
- [done 2026-08-10, cloud shift] **exp-003 the broadband wall,
  redesigned** — cpl fixed at 20 across a 6-point λ sweep (420–750nm),
  geometry scaled in cells to hold physical (nm) defect size constant.
  First run caught its own domain-sizing bug (box independence blew up
  at the largest scale factor — a harness bug, not physics) before any
  result was trusted; full sweep rerun clean (box_dev ≤1.1%, cross_dev
  ≤0.2%) after fixing it. Findings: (1) the red-side improvement is real
  and NOT a resolution artifact (λ=600 point reproduces exp-002 to
  <1%, confirming the harness; net Q_ext(cloak) 0.460→0.318 across the
  sweep with cpl held fixed) — exp-001's flagged confound is resolved;
  (2) but it is NOT the (defect/λ)² law hypothesized — log-log slope
  ≈0.79 (R²=0.87), well below the predicted [1.5,3.0] band; (3) the
  trend is non-monotonic — a bump at 480nm exp-002's 3-point sweep
  couldn't have shown. Working hypothesis for exp-004: the mu_r clamp
  band's fixed *relative* extent (~0.29·r1) interacting with the fixed
  grid, not simple electrical-size scaling.
- [open — NEXT, cloud-shift-ready] **exp-004 candidate**: hold electrical
  size and cpl fixed, sweep `mu_r_floor` alone, to isolate whether the
  clamp band (vs staircase) drives exp-003's 480nm bump and sub-quadratic
  exponent.
- [done 2026-08-10, cloud shift] exp-001 observer-table rerun post phasor
  fix — camera floor drops ~17× (bug removed), absorber return tracks the
  new floor at every λ, reflector/cloak shift a few % (same order, same
  ranking). Values shifted, verdict stands, exactly as queued.
- [open] Parking lot: black-lined cloak hybrid (eat the backward glint),
  Q vs incidence angle, near-to-far transform.
- Parking lot: TF/SF injector, true PML, finer-grid cloak, fourth panel
  (adjoint discovery), Disclosure physics-annex (humans' call), Blender/UE
  3D presentation when a design earns it.
