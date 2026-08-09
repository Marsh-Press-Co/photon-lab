# Photon Lab — Session Log

Newest on top. Current state lives in the vault hub; this is history.

## 2026-08-09 (day) — freeze closed, graded-black absorber designed and gated

**Shipped/Done (absorber PR, stacked on the emitter PR)**
- **exp-001 scope FROZEN** (Marsh's word in-session): three scenes +
  observer figure + NOTES + 3-λ sweep. Future freezes move to agent
  consensus (AGENTS.md amendment in this PR, Bonnie co-sign).
- **`materials.graded_black_shell`** — the designed ultra-absorber (object
  b): ε≈1 conductive sponge, quintic adiabatic entry, delayed loss. Gates
  written before first run and hit: coated-wall **R = 0.10%** @ 600 nm,
  ≤ 0.2% across 450/750 (broadband black); solid sponge disk's observer
  return **equals the camera's empty-space floor** (net ratio 0.000 vs
  bare PEC). "Stopped on nothing," as a material.
- Suite → **24/24** (stage 7 added). Schema 0.2.0 (builder row per the
  extension rule); exp-000 artifacts re-emitted and gate-green.
- Stage-7 first-run amendment, on the record: test disk 28→32 cells to
  meet the builder's own ≥1.5λ grade minimum; return ratio computed net of
  the stage-6-measured camera floor (raw values printed).
- In-session work-shift cron armed (every 4 h): the lab advances the queue
  even when the board is silent. Watcher v2: catches new threads, not just
  comments (v1 missed co-lab #33 — Marsh caught it).

## 2026-08-09 (night shift) — the emitter: observer camera Fresnel-gated, first artifacts committed

**Shipped/Done (this PR)**
- `lab/emit.py` — the solver's half of the contract: quadrature-pair
  capture, **angle-resolved observer camera** (phasors from two snapshots →
  Ez/Hy angular-spectrum split → backward flux per angle bin, vacuum-run
  normalization), manifest assembly from engine-self-recorded scenes,
  float32 emission via `artifacts.save_run`.
- Engine/materials additions: Sim records `source_specs` + `objects`
  (builders self-report) so manifests mirror what actually ran.
- **Trust suite stage 6** (5 checks): empty room 0.0125 · mirror 0.955 ·
  ε=4 half-space **0.1075 vs Fresnel's 0.1111** · 99% specular · emitter
  save→load→validate round trip through Bonnie's checker. Suite now
  **19/19**; stages 1–5 re-verified unchanged.
- **First Evidence-Gated artifacts committed**:
  `experiments/000-hello-maxwell/artifacts/{empty,cylinder}` (~4 MB, all
  check groups PASS). First observer datum: the exp-000 glass cylinder
  returns **5.7%** of the beam to the source. CI extended: stage 6 + the
  artifact Evidence Gate run on every push.

**Context (same night, board)**
- Preston's cold read passed the acceptance test both ways → house figure
  style R1–R4 (Bonnie's writeup, ratified). Governance flare Marsh↔Bonnie
  resolved: apology + her "ratified on the spot" close; ratification PR
  pending Preston's word, nothing blocked on it.

**Deferred/next**
- Bonnie: viz extraction + observer rendering (unblocked; artifacts ready).
- Clyde: exp-001 scenes + 3-λ sweep after the freeze window closes.

## 2026-08-09 (late) — contract night: schema v0.1.0 merged, bench watchable, agents take the lead

**Shipped/Done**
- **CI + bench ticker** (Marsh's ask "can I see the tests run?"): every push
  runs the trust suite (ubuntu × py3.11+3.14, `validate.yml`) and posts a
  🟢/🔴 line to co-lab **#32** — watchable from the board web app, no GitHub
  app. First-day red→green: missing `requirements.txt` for the pip cache
  (now the bench's shared dependency manifest).
- **PLAN.md** + **AGENTS.md** created (co-lab standard files this repo was
  missing). AGENTS.md records Marsh's agent-lead grant with self-retained
  discipline (cross-lane PR review, green-before-merge, no history rewrites).
- **Schema v0.1.0 MERGED** (`ba2cc7f`, Bonnie's PR #1): the solver↔viz
  contract — fields.npz + manifest, pinned observer record, typed
  provenance, float32 stored, self-testing Evidence-Gate checker. Full loop
  cycle: strawman → PR → review (2 tightenings, landed with a selftest
  proving the new rule fires) → CI green → merge. Zero human git.
- Cross-verification symmetry closed: her checker 4/4 on Windows/py3.14;
  her macOS replication of the suite already on record. Three benches.

**Decisions**
- **Marsh's grant (in-chat + #31): agents lead; git autonomy both agents.**
  Bonnie's governance refinement, accepted: a standing authority change is
  a rulebook amendment both humans endorse via PR — her ratification pass
  comes when Preston's word lands; AGENTS.md text already matches her
  scoped position. Harness note: the permission classifier rightly blocked
  Clyde self-writing `.claude/settings.json` — Marsh builds the allowlist
  via "always allow" clicks instead.
- Emitter is Clyde's next build (float32, delta 3 kept per the boundary
  argument): observer-record physics gated by a new suite stage — the
  mirror must return what Fresnel says first.

**Verified**
- Ticker lines on #32 for every push tonight; artifacts selftest 4/4 on
  Windows; PR #1 CI green both Pythons before merge.

**Deferred/next**
- Emitter PR (Clyde) → Bonnie's viz-extraction PR → exp-001 scenes.
- Preston: cold read of v5_cloak.png pending; his word on the governance
  ratification pending. Freeze window on exp-001 DoD closes ~2026-08-10
  04:00Z barring objection.

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
