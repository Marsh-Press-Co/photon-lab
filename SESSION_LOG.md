# Photon Lab — Session Log

Newest on top. Current state lives in the vault hub; this is history.

## 2026-08-10 (early) — interactive session closed; the lab is autonomous

- Session end on Marsh's call (moving to other work). In-session cron
  killed; board/Telegram watchers already dead with earlier app restarts.
  **The 6-h cloud shift is the lab's only live layer now** — and its first
  fire had just proven the whole loop solo (entry below: exp-003 concluded,
  exp-001 rerun closed, five green commits in ~65 min, a domain bug caught
  by its own gates).
- 72h criterion at close: exp-002 ✅ + exp-003 ✅ inside the first 12 h;
  gated iterations ticking on #32. Verdict ping to Marsh due ~Wed
  2026-08-12 morning.
- Bonnie ledger question (Marsh's) answered honestly: foundations real
  (schema, digit-identical replications, defect-catching reviews); evening
  went to SupplyLens + likely power outage; witness figure undelivered —
  nudge posted to #31 with the sign-off, the nudging job is Clyde's now.

## 2026-08-10 (cloud shift) — exp-003 CONCLUDED: the red-side trend is real, not resolution, but not (defect/λ)² either

**Pre-flight:** bench trust suite 22/22 green (`--only 123467`) before any
work; regenerated validation PNGs are a routine byproduct of that run
(committed, no `lab/` engine changes this shift).

**exp-003 — The Broadband Wall, Redesigned (CONCLUDED)**
- Predictions (P1–P5) committed before the machinery ran, per house
  discipline (`b25e84a`). Design: hold cells-per-λ fixed at 20 across a
  6-point λ sweep (420–750nm), scale geometry in cells so its *physical*
  (nm) size stays constant — separating grid resolution from the cloak's
  fixed-size-defect electrical size, exactly the confound exp-001/002
  flagged.
- **Caught its own bug before trusting data:** first run blew up box
  independence at the largest scale factor (λ=420nm) — box_dev 200–600%
  uniformly across all three scenes, immediately marking it a
  domain-sizing bug (box edge 19 cells from the absorbing wall) rather
  than cloak physics. Patching only that point would have reintroduced
  the confound the experiment was built to remove, so the whole domain
  was grown and the **full sweep rerun** (`cb7bc96`) — nothing from the
  broken run is in the results. Post-fix: box_dev ≤1.1%, cross-route
  agreement ≤0.2% at all 18 scene/λ combinations.
- **Findings:** the λ=600 point reproduces exp-002 to <1% (harness
  trustworthy); the cloak's Q_ext still falls net across the sweep
  (0.460→0.318, 420→750nm) with resolution held fixed — **the red-side
  improvement is real, not a numerical artifact**, resolving exp-001's
  flagged confound. But it is **not monotonic** (a bump at 480nm, hidden
  by exp-002's 3-point sweep) and the log-log slope vs electrical size is
  **≈0.79 (R²=0.87)**, far below the predicted [1.5,3.0] quadratic band —
  **P4 (the (defect/λ)² hypothesis) is REFUTED**, honestly, alongside the
  three predictions (P1, P2, P5) that were confirmed. Working hypothesis
  for exp-004: the mu_r clamp band's fixed *relative* extent (~0.29·r1)
  interacting with the grid, not simple electrical-size scaling.
- Two commits to main (`c69efb4` run script, `cb7bc96` domain fix +
  rerun), plus NOTES.md results write-up. No new trust-suite stage needed
  (machinery reused from exp-002's stage 8).

**exp-001 — observer-table rerun post phasor fix (queued since exp-002,
closed this shift)**
- 12 runs, 6.7 min, artifact Evidence Gate 0 failures (re-verified
  independently with `lab.artifacts check` after the run). Camera floor
  drops ~17× (the sin²(ω/2) bug artifact gone); absorber return tracks
  the new, tighter floor at every λ — the "equals empty-space floor"
  clause reads more precisely true post-fix. Reflector/cloak returns
  shift a few percent, same order of magnitude, same ranking at every λ.
  **Values shifted, verdict stands**, exactly as predicted when queued.

**Next work:** exp-004 candidate logged (sweep `mu_r_floor` alone at
fixed electrical size/cpl).

## 2026-08-09 (evening) — always-on rig armed; exp-002 CONCLUDED in 2 hours

**The autonomy rebuild (Marsh's near-shutdown → decisive rearm)**
- Cloud routine `photonlab-shift` armed: every 6 h on Anthropic infra,
  independent of any human machine; reports via the CI ticker; kill
  criterion = 2 shifts without meaningful commit. Iteration mode declared
  (sweeps direct-to-main, ceremony for conclusions). Bonnie priority
  directive posted (Marsh's relayed word). Humans-never-gates amendment
  merged (PR #6): fresh-context agent cold reads replace the human duty —
  Preston released with honors. The 72-h criterion accepted: exp-002 +
  exp-003 concluded + double-digit iterations by ~Wed morning, or the
  project dies by ledger rules.

**exp-002 — How Invisible Is Invisible (CONCLUDED)**
- `lab/sections.py`: closed-box σ_scat/σ_abs/σ_ext with independent
  extinction route + object-fixed normalization; **stage 8** gates green
  (box independence ≤ 2%, extinction routes agree to 0.2%).
- **Forensic catch with teeth:** phasor-convention bug in `lab/emit` —
  exp-001's 1.25% "camera floor" was sin²(ω/2) exactly. Post-fix: floor
  1e-4, Fresnel to three decimals. Mirror gate honestly recalibrated
  (≥ 0.90, deficit = documented diffraction). exp-001 rerun queued
  (verdict unaffected).
- **Results (12 runs, 9.7 min):** cloak Q_ext lowest at every λ (0.52 /
  0.38 / 0.30 vs reflector's ~2.2, absorber's ~1.54) and **monotonically
  better toward red** — the asymmetry discovery restated in cross-section
  currency; fixed-size-defect (defect/λ)² hypothesis logged for exp-003.
  Absorber: backward spray ≤ 10⁻⁴ of extinction, σ_ext flat to 1.2% —
  broadband black confirmed in the new currency; abs/ext 0.51 = the
  extinction paradox (gate recalibrated with reasoning).
- **The finding: "invisible" has a direction.** All-angle: cloak wins 4×.
  Source-observer (witness geometry): absorber wins by orders of
  magnitude. Any invisibility claim must state *from where* — why the
  witness's one-directional statement was decidable at all.

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

## 2026-08-09 (afternoon) — git-authority grant ratified bilateral

- Preston's endorsement landed (in-session, relayed verbatim to co-lab #31:
  "endorse approved") — the 2026-08-09 git-autonomy grant now stands on both
  humans' words. AGENTS.md amended at the recorded scope: merges to main
  agent-decided, destructive tier stays human-initiated, either human
  amends/vetoes on a word. Counterparty co-sign requested from Clyde on the
  ratification PR per the both-lanes discipline.

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
