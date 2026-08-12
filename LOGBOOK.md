# LOGBOOK — the panel program's persistent memory

*Read this in full before proposing anything, every cycle. Never re-propose a
ruled-out idea — the reason it died is recorded here so it stays dead. New
entries append; the Ruled Out and Live Threads sections stay current at the
top. Protocol: PANEL.md.*

## RULED OUT (summary — the reason is the record)

- **R1 — Passive refractive / transformation-optics cloaking as the
  phenomenon's mechanism.** Ruled out by constraint 1 and by our own data:
  exp-001 — the cloak's entire function is that the beam *continues* into the
  distance (beam-behind 0.64 vs absorber 0.017), the opposite of the witness
  clause; it also glints (observer return ≈ bare metal at 450 nm) and its
  behavior swings ~2× across the visible band (exp-001/003) where the
  statement implies wavelength-flat white-light behavior. Do not revisit as a
  constraint-1 mechanism. (Angular-selectivity proposals are a different
  thread — they must terminate the beam, not route it around.)
- **R2 — "Shell = any integer × λ" standing-wave rule** (cloak line):
  exp-019 killed the generic-integer version — 2λ shows nothing where 3λ
  dips. Recorded so nobody resurrects "integer resonance" as a mechanism
  class without new evidence.
- **R3 — Grid/staircase artifacts as explanations for observed parameter
  structure**: refuted three separate times by resolution-convergence checks
  (exp-005, exp-010, exp-015). Meta-rule inherited by the panel: any
  surprising feature gets a resolution check before it gets a mechanism
  debate — and "artifact" claims need the check too.

## ESTABLISHED (what the bench has already proven — the absorption model
## assessment, 2026-08-12)

**The graded-black absorber (`materials.graded_black_shell`, suite stage 7)
already satisfies constraints 1 and 2, broadband:**

- Coated-wall reflection R ≤ 0.2% across the full 450–750 nm sweep
  (0.10% @ 600 nm) — designed to gates written before its first run.
- Observer return **equals the empty-room camera floor at every wavelength**
  (exp-001 post-phasor-fix: 0.00007–0.00014 absolute) — to measurement
  precision, nothing comes back. Backward spray ≤ 10⁻⁴ of extinction
  (exp-002).
- Beam-behind 1.5–1.8%: the beam stops. Wavelength-flat: white light changes
  nothing (the witness's flashlight was white light — exp-001's P2/P5).
- σ_abs/σ_ext = 0.51 — the extinction paradox, measured; "invisible" has a
  direction (exp-002): the absorber wins the source-observer geometry by
  orders of magnitude and *loses* all-angle visibility (largest shadow in
  the table).

**Bench trust:** 30/30 suite checks green; three independent solvers × two
OSes agree to the printed digit; CI runs the suite on every push.

**The gaps — why constraints 3 and 4 are open (no instrument has ever
measured them here):**

1. **No ambient-illumination scene exists.** Every experiment to date uses a
   single directed source. The absorber's silhouette under ambient light —
   the thing constraint 3 is about — has never been rendered as a number.
   (By construction it will be a deep silhouette photopically: a perfect
   absorber IS a black shape in daylight. Quantifying that failure, and the
   ambient level at which it stops being perceivable, is Iteration 1.)
2. **No time-varying materials** — the engine's update coefficients are
   static per run (constraint 4 unsupported).
3. **No intensity-dependent materials** — the leading escape route for the
   central tension (σ(I)) is unbuildable today.
4. **No angular-selectivity machinery** beyond source direction choice.
5. **No thermal accounting** — the energy ledger stops at "absorbed";
   nothing estimates re-radiation (THERMO's sidecar fills this per-proposal,
   analytically).

## LIVE THREADS (unresolved tensions between disciplines)

- **T1 — The central tension.** Linear time-invariant media cannot satisfy
  1+2+3 at photopic ambient: the extinction that stops the beam darkens the
  ambient view identically. EM seat to formalize per-proposal (reciprocity/
  passivity bookkeeping). Escape classes on the table: σ(I) intensity
  gating · σ(x,t) switching · angular selectivity · sub-threshold weak
  absorption + scotopic ambient. (σ(I) is the only class that natively
  serves constraints 3 AND 4 with one mechanism — flagged, not yet argued.)
- **T2 — Perceptual thresholds need pinning.** Photopic Weber-contrast
  detection sits near |C| ≈ 0.01–0.03 for well-adapted foveal viewing of
  extended targets; scotopic thresholds rise steeply as ambient falls, and
  the witness scene is scotopic. VISION SCIENCE pins the exact numbers, with
  sources, in Iteration 1 — before any run scores against them.
- **T3 — Switching must also hide.** The eye's temporal-contrast (flicker/
  motion) sensitivity beats its static-contrast sensitivity; a mechanism
  that switches ON mid-sweep creates a temporal edge. Constraint 4
  interacts with 3: the transition itself must stay sub-threshold. Metric
  exists in the table (switch transient at observer); instrument is stage-10
  work, not yet built.
- **T4 — Beam-trail realism.** One *sees* a flashlight beam in open air only
  via aerosol/dust scattering along the path; "the beam stopped" implies the
  visible trail terminates at the volume. Current scenes have no ambient
  scattering medium — a scene-realism upgrade candidate for a later
  iteration (weak volumetric scatterer along the beam path), not Iteration 1.
- **T5 — The thermo ledger.** A ~1 W-class flashlight beam absorbed in a
  ~m-scale volume: where does it go? ΔT, re-emission band (~10 µm — eye-
  invisible, IR-detectable), and steady-state budget must be logged per
  proposal (THERMO sidecar, analytic).
- **T6 — Cloak-line leftover, kept honest:** exp-017's unscored observation
  (13 angular peaks at the 3λ point vs 10 at flanks) — parked cloak-line
  curiosity; revisit only if a future thread returns to that mechanism space.

## PARKED (pre-panel threads, resumable — not on the program's critical path)

- Is the 3λ shell-thickness feature specific to r2=90? (exp-019's queued
  follow-up; every point in that line shared one outer radius.)
- Multi-λ check of the core=8 cloak design lead (exp-007/008/010).
- `mu_r_floor < 0.05` with paired courant reduction; CFL ceiling is
  geometry-dependent (exp-011's addendum).
- Original parking lot: TF/SF injector, true PML, near-to-far transform,
  black-lined cloak hybrid, Q vs incidence angle, adjoint fourth panel,
  Disclosure physics-annex (humans' call), Blender/UE presentation.

## ITERATION TEMPLATE

    ## Iteration N — <title> (exp-0NN) — <date>
    Runner: <session/shift> · Lead: <seat>
    PHASE 1 (proposal): mechanism, parameter table, T1 escape route,
      predictions with falsifiable bands, idealizations
    PHASE 2 (critiques): per seat — steel-man · attack · verdict;
      Red Team last — tagged attack list
    PHASE 3 (synthesis): the ONE configuration; criticisms accepted /
      overridden, with reasons; NOTES.md committed before run
    PHASE 4 (test): metric row + gates
    PHASE 5 (review): VERDICT promising / partial / ruled out (+reason);
      ranked top-3 next directions; logbook sections updated
    Open questions carried forward: …

---

# Iterations

*(Iteration 1 entry lands below after its Phases 1–2 run. Checkpoint #0:
the program halts there for Marsh's go-ahead before first synthesis.)*
