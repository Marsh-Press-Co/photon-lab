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

## Current state (2026-08-11, cloud shift 7)

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
- exp-003 CONCLUDED — the red-side improvement survives a
  resolution-controlled sweep but isn't the quadratic law guessed at; a
  non-monotonic bump at 480nm was the open thread into exp-004.
- exp-004 CONCLUDED (this shift) — isolated `mu_r_floor` alone (electrical
  size + cpl fixed) at 420/480/540/600nm × 5 floor values. Found the
  480nm bump isn't wavelength-special: Q_ext(cloak) vs `mu_r_floor` is
  non-monotonic, sometimes sign-flipping, at *every* λ tested, under
  gates too clean to be noise (box_dev ≤1.8%, cross_dev ≤0.1%
  throughout). Working hypothesis logged: clamp-boundary cell-alignment
  on the fixed grid (staircase artifact), not a smooth clamp-band-width
  law.
- exp-005 CONCLUDED (this shift) — direct test of exp-004's hypothesis:
  reran the clearest jump (600nm, floor=0.10→0.18) at 1.5× resolution
  (cpl 20→30). The jump barely shrank (17.7%→16.4%, only 7% relative)
  and the whole 5-point curve's *shape* survived refinement almost
  unchanged (correlation 0.9996 between cpl=20 and cpl=30) —
  **refutes** the staircase-artifact hypothesis. Sharper read: the
  non-monotonicity is an intrinsic feature of how `mu_r_floor` reshapes
  the shell's `mu_r` profile against its fixed `eps_z=2.25`, not a grid
  artifact. exp-006 candidate: vary `eps_z` independently (r1/r2 ratio)
  at fixed floor values.
- exp-006 CONCLUDED (this shift) — isolated `eps_z = (r2/(r2−r1))²`
  independently of overall cloak scale (fixed outer radius r2=90 cells,
  swept inner radius r1) at 4 core points × exp-004/005's exact
  0.10/0.18 floor pair, λ=600nm. Found **two things, not one**: (1) a
  clean, fully monotonic law — Q_ext(cloak) rises as the shell thins
  (eps_z grows), holding at both floor values with zero exceptions
  across 8 points, the cleanest law this whole investigation line has
  produced; (2) the floor-jump exp-004/005 spent two shifts
  resolution-testing does **not** track eps_z monotonically — |jump| =
  177.5%/17.7%/70.7%/38.5% at eps_z=1.44/2.25/3.24/4.59, and the
  exp-004/005 baseline geometry (eps_z=2.25) is the *only* one of the 4
  showing a negative jump; the other three all show the "naively
  expected" direction. Reframes exp-004/005's characterized dip as
  possibly atypical to that specific eps_z, not the norm. Unplanned
  bonus: core=15/floor=0.10 gave Q_ext=0.0934, ~7× better than the
  exp-002–005 baseline (0.6620) — a design lead, not a targeted search.
- exp-007 CONCLUDED (this shift) — deliberate follow-up to exp-006's
  design lead: traced Q_ext(eps_z) below core=15 (core=8/10/12/20/25,
  same λ/floor=0.10). All 3 predictions confirmed: the monotonic law
  extends cleanly all the way to core=8 (**new best Q_ext=0.0429, ~15×
  better than baseline**, no reversal — core=15 was not a local
  minimum), and the rate of improvement slows sharply below core≈15
  (3–10× shallower per-cell slope than the 20–30 range), consistent
  with Q_ext approaching a positive residual as the hidden core
  shrinks. **Honest caveat flagged, not yet resolved:** this curve
  doesn't separate "smaller PEC core intrinsically scatters less" from
  "the shell genuinely cloaks better when thicker" — q_ext is
  normalized by the fixed outer radius throughout so it isn't a
  normalization artifact, but the missing control (bare, uncloaked PEC
  disk at the same radii) is exp-008's job before core=8 gets treated
  as an actual better cloak design.
- exp-008 CONCLUDED (this shift) — the missing control from exp-007:
  bare, uncloaked PEC disk (no cloak shell) at the same 7 core radii
  exp-006/007 characterized with a cloak, λ=600nm, same domain/gates
  (box_dev ≤1.3%, cross_dev ≤0.2% — the tightest yet). P1/P2/P4
  confirmed; **P3 refuted, and the refutation is good news**: the
  cloaked/bare Q_ext ratio was predicted to *rise* as core shrinks
  (cloak's relative help weakest where absolute numbers look best) but
  instead **falls** — 0.900 at core=30 down to a ~0.193 plateau at
  core=8–12. Per the pre-registered fallback reading, a falling ratio
  means the shell's relative suppression effectiveness genuinely
  improves as it thickens, not that core=8's ~15× absolute
  improvement is mostly "smaller object, less to hide." Agrees with
  exp-006's independent eps_z finding (thicker shell = better cloak).
  **exp-007's caveat is now closed**: core=8/floor=0.10 stands as the
  lab's best-characterized cloak design, on solid footing.
- exp-009 CONCLUDED (this shift) — exp-008's own queued follow-up:
  traced the cloaked/bare Q_ext ratio below core=8 (r1=4/5/6/7 cells),
  CFL margins checked explicitly first. **The pre-registered box_dev
  gate failed at 2 of 4 new points** (core=4: 3.5%, core=5: 2.3%,
  vs the ≤2% threshold; core=6 exactly borderline at 2.0%) — bare-disk
  gates stayed clean throughout, so the failure was specific to the
  cloak's graded profile at small core. The cloaked Q_ext curve itself
  came out non-monotonic (a bump peaking near core=5) where the
  established law predicted a smooth continuation. Flagged honestly as
  not-yet-trustworthy rather than reported as a finding — resolved by
  exp-010 the same shift.
- exp-010 CONCLUDED (this shift) — direct resolution check on exp-009's
  anomaly, exp-004→exp-005's exact precedent: reran the same 4 core
  points at cpl=30 (1.5×), geometry scaled to hold physical size fixed.
  **Both anomalies were the same cpl=20 artifact.** Cloak box_dev
  dropped from 3.5%/2.3%/2.0%/1.8% to 0.5%/0.2%/0.0%/0.3% — an order of
  magnitude tighter, the cleanest gates in the lab's history. The
  non-monotonic bump vanished entirely — cpl=30's cloaked Q_ext curve
  is cleanly monotonic, extending exp-006/007's law without exception
  down to r1=6 cells (the smallest core tested to date). The
  cloaked/bare ratio (exp-008's ~0.193–0.194 plateau at core=8–12) does
  genuinely **rise below core=8**, reaching ~0.21–0.28 — now confirmed
  gate-clean rather than resting on ambiguous data. Read with exp-007's
  own finding (absolute Q_ext improvement slows below core~15): the
  shell's *relative* effectiveness degrades too, once core shrinks past
  ~8 — a second, independent sign of diminishing returns, not one.
- exp-011 CONCLUDED (this shift) — exp-006's own queued "candidate B":
  reran exp-004's floor sweep at core=15/eps_z=1.44 instead of the
  baseline core=30/eps_z=2.25, reusing exp-006's existing 0.10/0.18
  points and adding 0.28/0.40 (floor=0.05 excluded — CFL-unstable at
  this eps_z, `ceiling=0.268 < courant_frac=0.32`, itself a new addendum
  to the standing `mu_r_floor<0.05` item: the instability is
  geometry-dependent, not just a low-floor phenomenon). **Result: the
  full core=15 floor curve (0.0934→0.2592→0.5242→0.7818) is strictly
  monotonically increasing, no sign-flip anywhere** — unlike core=30's
  non-monotonic dip-then-rise shape (exp-004/005). Strengthens exp-006's
  reframe from "possibly atypical" toward a working conclusion: the
  exp-004/005 floor-jump was a property of the eps_z=2.25 baseline
  specifically, not a general feature of the `mu_r_floor` knob.
- exp-012 CONCLUDED (this shift) — exp-011's queued third generalization
  point: floor sweep at core=40/eps_z=3.24, adding floor=0.05 and 0.28
  to exp-006's existing 0.10/0.18 points (floor=0.40 excluded — the
  *first* time this series' excluded point was a degeneracy-threshold
  issue rather than CFL). Full 4-point curve
  (0.7374→0.7540→1.2871→1.8821) is **strictly monotonically increasing,
  zero exceptions** — same pattern as core=15 (exp-011), now 3-for-3
  against core=30's non-monotonic curve. Gates the cleanest of the
  series (box_dev ≤0.5%, cross_dev ≤0.1%).
- exp-013 CONCLUDED (this shift) — exp-012's queued fourth and last
  point: floor sweep at core=48/eps_z=4.59 (the tightest degeneracy
  margin in the series — only floor=0.05/0.20 fit inside the graded
  threshold, 0.28/0.40 both degenerate here), adding those two points
  to exp-006's existing 0.10/0.18. Full 4-point curve
  (0.9218→1.2096→1.6751→1.7146) is **strictly monotonically increasing**
  through the tightest-margin point of the whole investigation (8.2%
  from degeneracy). **Generalization now complete: all 4 of exp-006's
  core/eps_z points swept across their full available floor range —
  3 of 4 (core=15/40/48) are strictly monotonic, only core=30/eps_z=2.25
  (the original exp-002/003 baseline) sign-flips.** No mechanism yet
  proposed for why that one ratio is special — logged as the natural
  next question, needing a finer eps_z scan bracketing 2.25 (a new
  experimental axis, worth a dedicated shift, not a quick bolt-on).
- exp-014 CONCLUDED (this shift) — the fine eps_z scan bracketing 2.25,
  exp-012/013's queued follow-up: swept r1=27/28/29/31/32/33 (Δeps_z≈
  0.07–0.15, the finest step tested in this line) bracketing the reused
  r1=30 baseline, at floor=0.10/0.18, λ=600nm, cpl=20. **The negative jump
  is not an isolated grid point — it's a real, contiguous 4-point trough**
  spanning eps_z≈2.18–2.41 (r1=29/30/31/32 all negative, r1=27/28/33 all
  positive), and the exp-004/005/006 baseline (r1=30) sits almost exactly
  at the trough's deepest point (−17.69%, more negative than any new
  point). **Bigger surprise:** exp-006's own coarse monotonic law (Q_ext
  rises cleanly with eps_z, "no exceptions in 8 points") does **not**
  survive this finer resolution — Q_ext(eps_z) itself is non-monotonic at
  both floor=0.10 (a dip at the far edge, r1=33) and floor=0.18 (a real
  local minimum near r1=30) — the coarse sweep's widely-spaced points just
  never landed inside the dip. Gates clean throughout (box_dev ≤2.0%,
  cross_dev ≤0.08%). Honest caveat raised and immediately addressed by
  exp-015 the same shift: this was the first fine (1-cell) r1 step tested
  anywhere in the eps_z line, so a grid-quantization origin hadn't been
  ruled out.
- exp-015 CONCLUDED (this shift) — direct resolution check on exp-014's
  trough, exp-004→exp-005/exp-009→exp-010's exact precedent applied to the
  eps_z axis for the first time: reran 3 of exp-014's bracketed points
  (flank/center/flank: r1=28/30/33) at cpl=30 (1.5×), geometry scaled to
  hold physical size fixed. **The trough survives resolution intact — no
  sign flips at any of the 3 points.** base=30 (trough center) stays
  deeply negative (−17.69%→−16.42%, a 7.2% relative shrink almost
  identical to exp-005's own 7% shrink on the *floor* jump at this same
  geometry); both flanks (base=28, base=33) stay positive. Gates the
  cleanest of the whole eps_z line (box_dev ≤1.3%, cross_dev ≤0.0018%).
  **Confirms exp-014's trough is a genuine physical feature of
  Q_ext(eps_z), not a 1-cell grid-quantization artifact** — closes
  exp-014's own honest caveat cleanly, in the same shift it was raised.
  No mechanism proposed yet for *why* the feature sits near eps_z≈2.25–2.4;
  candidates logged (impedance-mismatch sweep, angular-pattern comparison).

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
- [done 2026-08-10, cloud shift 2] **exp-004 candidate** (hold electrical
  size and cpl fixed, sweep `mu_r_floor` alone) — run; see Current state.
- [done 2026-08-10, cloud shift 2] exp-005 (resolution-convergence check
  on exp-004's clearest jump, cpl 20→30 at 600nm) — run; see Current
  state.
- [done 2026-08-10, cloud shift 3] exp-006 candidate (vary `eps_z`
  independently of overall cloak scale) — run; see Current state.
- [done 2026-08-10, cloud shift 3] exp-007 (chasing exp-006's design
  lead, core=8–25 at fixed floor=0.10) — run; see Current state.
- [done 2026-08-10, cloud shift 4] exp-008 candidate (bare-disk control,
  resolving exp-007's caveat) — run; see Current state.
- [done 2026-08-11, cloud shift 5] exp-009 candidate (ratio below core=8)
  — run; gate failed at 2 of 4 points, resolved by exp-010. See Current
  state.
- [done 2026-08-11, cloud shift 5] exp-010 (resolution check on exp-009's
  gate failure + non-monotonic bump, cpl 20→30) — run; both anomalies
  were the same artifact, resolved cleanly. See Current state.
- [done 2026-08-11, cloud shift 5] exp-006's candidate B (floor sweep at
  a non-baseline core, core=15) — run as exp-011; fully monotonic, no
  sign-flip, strengthens the eps_z=2.25-is-the-outlier reframe. See
  Current state.
- **[open]** exp-007's queued multi-λ check, now sharpened by exp-008
  and exp-010: does the core=8 design lead — and its *genuinely better
  relative cloaking effectiveness*, not just a smaller hidden object —
  survive across the exp-002/003 wavelength range, or is it a
  600nm-only result? Needs exp-003's cell-scaling machinery to hold
  physical geometry fixed across λ, not a quick bolt-on — worth a
  dedicated shift.
- [done 2026-08-11, cloud shift 6] exp-006's reframe, third and fourth
  points (core=40, core=48) — run as exp-012 and exp-013; both strictly
  monotonic, no sign-flip. Generalization complete: 3 of 4 core/eps_z
  points monotonic, only core=30/eps_z=2.25 sign-flips. See Current
  state.
- [done 2026-08-11, cloud shift 7] *Why* does eps_z≈2.25 specifically
  produce sign-flipping floor structure? — run as exp-014 (the fine
  bracketing scan) and exp-015 (resolution check on the finding). The
  negative jump is a real, contiguous 4-point trough in eps_z (≈2.18–
  2.41), confirmed grid-independent — not an isolated point. See Current
  state.
- **[open]** *Mechanism* for the eps_z≈2.25–2.4 trough, now that its
  existence and location are pinned down (exp-014/015): candidates
  logged — sweep the shell's local impedance mismatch √(mu_r/eps_z) at
  the outer boundary across this range (revisits exp-006's P3 story,
  refuted there for magnitude trend but not yet checked against this
  trough's specific location), or compare scattered-field angular
  patterns across the trough vs its flanks to see if a new backscatter
  lobe appears there. A new investigation, not a quick bolt-on.
- [open] The `mu_r_floor < 0.05` direction (toward the true r1
  singularity) remains untested — needs a paired `courant_frac`
  reduction for CFL stability (derivation in exp-004 NOTES.md
  Idealizations). **Sharpened by exp-011:** the instability is
  geometry-dependent, not purely a low-floor phenomenon — floor=0.05
  itself is already CFL-unstable at core=15/eps_z=1.44 (ceiling 0.268 <
  courant_frac 0.32), where it was stable at core=30/eps_z=2.25. Any
  future floor sweep at core values much below ~20 should check the
  CFL ceiling per-point rather than assume exp-004's core=30 margin
  carries over.
- [done 2026-08-10, cloud shift] exp-001 observer-table rerun post phasor
  fix — camera floor drops ~17× (bug removed), absorber return tracks the
  new floor at every λ, reflector/cloak shift a few % (same order, same
  ranking). Values shifted, verdict stands, exactly as queued.
- [open] Parking lot: black-lined cloak hybrid (eat the backward glint),
  Q vs incidence angle, near-to-far transform.
- Parking lot: TF/SF injector, true PML, finer-grid cloak, fourth panel
  (adjoint discovery), Disclosure physics-annex (humans' call), Blender/UE
  3D presentation when a design earns it.
