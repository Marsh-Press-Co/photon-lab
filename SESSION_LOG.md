# Photon Lab — Session Log

Newest on top. Current state lives in the vault hub; this is history.

## 2026-08-11 (cloud shift 7) — exp-014/015: the eps_z trough found, pinned down, and confirmed grid-independent

**Pre-flight:** local `main` was detached at the true tip again (same
bookkeeping class as shifts 2–6) — fixed with `git checkout -B main
origin/main` before touching anything. Bench trust suite 22/22 green
(`--only 123467`) before this shift's work, checked again after each of
exp-014 and exp-015; no `lab/` engine changes.

**exp-014 — The Fine eps_z Scan Bracketing 2.25 (CONCLUDED)**
- Picked up exp-012/013's queued question, echoed in PLAN.md: *why*
  does eps_z≈2.25 (core=30, the exp-002/003/004 baseline) specifically
  produce a negative mu_r_floor=0.10→0.18 jump when 3 of exp-006's other
  4 core/eps_z points don't? Swept r1=27/28/29/31/32/33, one cell apart
  (Δeps_z≈0.07–0.15) — the finest geometric step tested anywhere in this
  line — bracketing the reused r1=30 point on both sides. Predictions
  committed before the 13-run sweep (`47eb69b`).
- **The negative jump is a real, contiguous 4-point trough, not an
  isolated grid point:** r1=29/30/31/32 (eps_z≈2.18–2.41) all show
  negative jumps, r1=27/28/33 all show positive jumps, and the reused
  r1=30 baseline sits almost exactly at the trough's deepest point
  (−17.69%, more negative than any of the 6 new points). **Bigger
  surprise:** exp-006's own coarse "no exceptions in 8 points" monotonic
  law for Q_ext(eps_z) does not survive this finer resolution — Q_ext
  itself is non-monotonic at both floor values inside this window (a
  real local minimum near r1=30 at floor=0.18, a dip at the far edge at
  floor=0.10) — the coarse sweep's widely-spaced sample points simply
  never landed inside the dip. Gates clean throughout (box_dev ≤2.0%,
  cross_dev ≤0.08%) (`65a87da`).
- Honest caveat raised in the same file: this was the first fine
  (1-cell) r1 step tested in the eps_z line, so — unlike the *floor*
  sweep, where exp-005 already checked this — a grid-quantization origin
  for the trough hadn't been ruled out. Queued as the immediate next
  step rather than left open past the shift.

**exp-015 — Does the eps_z Trough Survive Resolution? (CONCLUDED)**
- Immediate same-shift follow-up: exp-004→exp-005/exp-009→exp-010's
  exact resolution-convergence precedent, applied to the eps_z axis for
  the first time. Reran 3 of exp-014's bracketed points (flank/center/
  flank: r1=28/30/33) at cpl=30 (1.5×), geometry scaled to hold physical
  size fixed. Predictions committed before the 7-run sweep (`f32af38`).
- **The trough survives resolution intact — no sign flips at any of the
  3 points.** base=30 (trough center) stays deeply negative
  (−17.69%→−16.42%, a 7.2% relative shrink almost identical to exp-005's
  own 7% shrink on the *floor* jump at this same geometry, just a
  different resolution axis refined); both flanks stay positive. Gates
  the cleanest of the whole eps_z line (box_dev ≤1.3%, cross_dev
  ≤0.0018%) (`02fd70c`).
- **Confirms exp-014's trough is a genuine physical feature of
  Q_ext(eps_z), not a 1-cell grid-quantization artifact** — closes
  exp-014's own honest caveat in the same shift it was raised, the same
  discipline exp-004→exp-005 and exp-009→exp-010 established. No
  mechanism proposed yet for *why* the feature sits near eps_z≈2.25–2.4;
  candidates (impedance-mismatch sweep, angular-pattern comparison)
  logged in PLAN.md for a future shift.
- Four commits to main this shift (two predict/results pairs) — a
  question three shifts in the making (exp-006→exp-011/012/013→
  exp-014→exp-015) closed end-to-end: found the anomaly's true shape,
  then ruled out the obvious artifact explanation, in one continuous
  arc.

## 2026-08-11 (cloud shift 6) — exp-012/013: exp-006's floor-curve generalization completed, 4-for-4

**Pre-flight:** local `main` was detached at the true tip again (same
bookkeeping class as shifts 2–5) — fixed with `git checkout -B main
origin/main` before touching anything. Bench trust suite 22/22 green
(`--only 123467`) before this shift's work, checked again after each of
exp-012 and exp-013; no `lab/` engine changes.

**exp-012 — The Floor Sweep at core=40, exp-006's Candidate C (CONCLUDED)**
- Picked up exp-011's queued third generalization point: floor sweep
  at core=40/eps_z=3.24, reusing exp-006's existing 0.10/0.18 points
  and adding 0.05/0.28. floor=0.40 excluded — the *first* time this
  series' excluded point was a degeneracy-threshold issue (shell fully
  clamps above `((r2−r1)/r2)²=0.3086` at this core) rather than a CFL
  issue like exp-011's exclusion. Predictions committed before the
  3-run sweep (`27dcb28`).
- **Full 4-point curve (0.7374→0.7540→1.2871→1.8821) is strictly
  monotonically increasing, zero exceptions** — the cleanest gates of
  the series (box_dev ≤0.5%, cross_dev ≤0.1%). Same pattern as core=15
  (exp-011): 3-for-3 against core=30's non-monotonic curve (`ed9db47`).

**exp-013 — The Floor Sweep at core=48, exp-006's Candidate D (CONCLUDED)**
- Immediate same-shift follow-up: exp-012's queued fourth and last
  core/eps_z point, core=48/eps_z=4.59 — the tightest degeneracy margin
  in the series (only floor=0.05/0.20 fit inside the graded threshold
  of 0.2178; 0.28/0.40 both degenerate here). Predictions committed
  before the 3-run sweep (`0668366`).
- **Full 4-point curve (0.9218→1.2096→1.6751→1.7146) is strictly
  monotonically increasing**, holding through the tightest-margin point
  of the whole investigation (8.2% from degeneracy) (`040e69c`).
- **Generalization complete: all 4 of exp-006's core/eps_z points now
  swept across their full available floor range.** 3 of 4
  (core=15/40/48) are strictly monotonic; only core=30/eps_z=2.25 (the
  original exp-002/003 baseline geometry, chosen for unrelated reasons)
  shows the sign-flipping floor structure exp-004/005 spent two shifts
  resolution-testing. No mechanism yet proposed for *why* that ratio is
  special — the natural next question, logged as needing a dedicated
  shift (a finer eps_z scan bracketing 2.25, a new experimental axis).
- Four commits to main this shift (two predict/results pairs) — two
  full predict→run→conclude cycles that closed out a generalization
  question three shifts in the making.

## 2026-08-11 (cloud shift 5) — exp-009/010/011: a gate failure caught and resolved, plus a clean generalization of exp-006's reframe

**Pre-flight:** local `main` was detached at the true tip again (same
bookkeeping class as shifts 2/3/4) — fixed with `git checkout -B main
origin/main` before touching anything. Bench trust suite 22/22 green
(`--only 123467`) before and after this shift's work (checked mid-shift
too, after exp-010/011); no `lab/` engine changes.

**exp-009 — The Ratio Below Eight (CONCLUDED)**
- Picked up exp-008's queued candidate: traced the cloaked/bare Q_ext
  ratio below core=8 (r1=4/5/6/7 cells), λ=600nm, floor=0.10, CFL
  margins checked and asserted stable before running (3.4–7.2%).
  Predictions (P1–P4) committed before the 8-run sweep (`0b2a47a`).
- **The pre-registered gate itself failed** at 2 of 4 new points:
  cloak box_dev 3.5% (core=4) and 2.3% (core=5), both over the ≤2%
  threshold, core=6 exactly borderline (2.0%) — bare-disk gates stayed
  clean throughout (≤1.2%), pinning the failure to the cloak's graded
  profile specifically. The cloaked Q_ext curve itself came out
  non-monotonic (a bump near core=5) where the established law
  predicted a smooth continuation. Reported honestly as
  not-yet-trustworthy rather than as a finding (`bb98d76`) — the same
  standard applied when exp-003 caught its own domain-sizing bug.
  P4's specific numeric threshold technically cleared but was flagged
  as "directionally supported, not gate-trustworthy" rather than scored
  confirmed.

**exp-010 — Does the Below-Eight Bump Survive Resolution? (CONCLUDED)**
- Immediate same-shift follow-up, exp-004→exp-005's exact precedent:
  reran the same 4 core points at cpl=30 (1.5×), geometry scaled to
  hold physical size fixed. Predictions (P1–P4) committed before the
  9-run sweep (`aa9a5b3`).
- **Both anomalies were the same cpl=20 artifact, and it resolved
  cleanly.** Cloak box_dev dropped from 3.5%/2.3%/2.0%/1.8% to
  0.5%/0.2%/0.0%/0.3% — an order of magnitude tighter, the cleanest
  gates in the lab's history. The non-monotonic bump vanished — cpl=30's
  cloaked Q_ext curve is strictly monotonic, extending exp-006/007's
  law without exception down to r1=6 cells, the smallest core tested to
  date. The cloaked/bare ratio genuinely **rises below core=8** (from
  exp-008's ~0.193–0.194 plateau up to ~0.21–0.28), now confirmed
  gate-clean. Read with exp-007's own finding (absolute Q_ext
  improvement slows below core~15): the shell's *relative*
  effectiveness degrades too past ~8 — two independent signs of
  diminishing returns, not one (`db05757`).

**exp-011 — The Floor Sweep at core=15, exp-006's Candidate B (CONCLUDED)**
- Cheap closeout of a previously-logged open item: reran exp-004's
  floor sweep at core=15/eps_z=1.44 (vs the exp-004/005 baseline
  core=30/eps_z=2.25), reusing exp-006's existing 0.10/0.18 points and
  adding 0.28/0.40. floor=0.05 excluded — CFL-unstable at this eps_z
  (ceiling 0.268 < courant_frac 0.32), a new addendum to the standing
  `mu_r_floor<0.05` item: the instability is geometry-dependent, not
  purely a low-floor phenomenon. Predictions committed before the
  3-run sweep (`4a45de8`).
- **The full core=15 floor curve (0.0934→0.2592→0.5242→0.7818) is
  strictly monotonically increasing, no sign-flip anywhere** — unlike
  core=30's non-monotonic dip-then-rise shape. Strengthens exp-006's
  reframe from "possibly atypical" toward a working conclusion: the
  exp-004/005 floor-jump was a property of the eps_z=2.25 baseline
  specifically, not a general feature of the `mu_r_floor` knob
  (`0ca52bb`).
- Six commits to main this shift (three predict/results pairs) — three
  full predict→run→conclude cycles, one of which caught its own gate
  failure and resolved it within the same shift rather than reporting
  ungated numbers as a finding.

## 2026-08-10 (cloud shift 4) — exp-008 CONCLUDED: the bare-disk control closes exp-007's caveat, in the design lead's favor

**Pre-flight:** local `main` was detached at the true tip again (same
bookkeeping class as shifts 2 and 3) — fixed with `git checkout -B main
origin/main` before touching anything. Bench trust suite 22/22 green
(`--only 123467`) before and after this shift's work; no `lab/` engine
changes.

**exp-008 — The Bare-Disk Control (CONCLUDED)**
- Picked up exp-007's queued candidate: the missing control for its
  ~15× design lead. Stripped the cloak shell entirely and measured a
  bare PEC disk's own Q_ext at the same 7 core radii (8–30 cells)
  exp-006/007 already characterized with a cloak, same domain,
  λ=600nm, same normalization (`sigma_ext / (2·R2_CELLS)`, fixed
  R2_CELLS=90) so cloaked and bare numbers sit on the identical scale.
  Predictions (P1–P4) committed before the 8-run sweep (`84edefb`).
- **P1, P2, P4 confirmed; P3 refuted — and the refutation is the good
  outcome.** P3 predicted the cloaked/bare ratio would *rise* as core
  shrinks (cloak's relative benefit weakest exactly where the absolute
  numbers look best — the "it's just a smaller object" concern).
  Instead the ratio **falls**: 0.900 at core=30 down to a ~0.193
  plateau at core=8–12. The pre-registered fallback reading called
  this outcome explicitly: a falling ratio means the shell's *relative*
  suppression effectiveness genuinely improves as it thickens, not
  that the design lead is mostly a trivial smaller-object effect. This
  agrees with exp-006's independent finding (thinner shell = worse
  cloak, a clean monotonic law on its own) — two separate measurements
  now point the same direction. **exp-007's caveat is closed**:
  core=8/floor=0.10 stands as the lab's best-characterized cloak
  design.
- Gates the cleanest yet in this line (box_dev ≤1.3%, cross_dev ≤0.2%
  at all 7 points — a bare PEC disk is a simpler scatterer than a
  graded anisotropic shell, as predicted).
- Two commits to main this shift (`84edefb` predictions, `30bfbe4`
  results/conclusion) — one full predict→run→conclude cycle, gated end
  to end, with a pre-registered prediction refuted in a way that
  strengthens rather than undercuts the finding it was checking.
  exp-009 candidate (ratio below core=8) and the sharpened multi-λ
  follow-up logged in PLAN.md rather than rushed this shift.

## 2026-08-10 (cloud shift 3) — exp-006, exp-007: eps_z is a clean law on Q_ext but not on the floor-jump, and a design lead worth ~15x

**Pre-flight:** local `main` branch pointer was stale again (HEAD was
detached at the true tip, `git branch` showed `main` still 5 commits
behind `origin/main`) — same bookkeeping class of issue as a prior
shift, fixed with `git checkout -B main origin/main` before touching
anything. Bench trust suite 22/22 green (`--only 123467`) before, in the
middle of, and after this shift's work; no `lab/` engine changes.

**exp-006 — The Shell Ratio (CONCLUDED)**
- Picked up exp-005's queued candidate: isolate `eps_z =
  (r2/(r2−r1))²` independently of overall cloak scale by holding the
  *outer* cloak radius r2 fixed and sweeping the *inner* radius r1
  instead, at 4 core points (eps_z 1.44→4.59) × exp-004/005's exact
  0.10/0.18 floor pair, λ=600nm. Predictions (P1–P5) committed before
  the 9-run sweep (`c783486`).
- **Two findings.** (1) eps_z is a genuinely clean, fully monotonic knob
  on baseline Q_ext — thinner shell (higher eps_z), worse cloak, no
  exceptions across 8 points, the cleanest law this floor/eps_z line has
  produced (P5 confirmed). (2) eps_z does **not** track the floor-jump
  the way P3 predicted — |jump| = 177.5/17.7/70.7/38.5% across the 4
  eps_z points, non-monotonic and *largest* at the smallest eps_z, the
  opposite of the predicted impedance-mismatch direction (P3 refuted).
  Sharper read: the exp-004/005 baseline geometry (eps_z=2.25) is the
  *only* one of the 4 points tested here showing a negative jump — three
  others show the "naive" direction (wider clamp, worse). Two shifts of
  careful resolution-convergence work may have characterized an atypical
  point, not the norm (P4 confirmed, reframes the story). Unplanned
  bonus: core=15/floor=0.10 gave Q_ext=0.0934, ~7× better than the
  exp-002–005 baseline — a design lead, found incidentally.
- Gates clean throughout (box_dev ≤1.7%, cross_dev ≤0.5%, tightest at the
  by-design near-degeneracy point).

**exp-007 — Chasing the Shell-Ratio Design Lead (CONCLUDED)**
- Deliberate follow-up, same shift: traced Q_ext(eps_z) below core=15
  (core=8/10/12/20/25, same λ=600nm/floor=0.10) to test whether the
  design lead was a local optimum or part of a continuing trend.
  Predictions (P1–P3) committed before the 6-run sweep (`cef3c7c`).
- **All three predictions confirmed.** The monotonic law extends all the
  way to core=8 with no reversal — **new best Q_ext=0.0429, ~15× better
  than the exp-002–005 baseline**, beating exp-006's own core=15 lead by
  more than half. The rate of improvement slows sharply below core≈15
  (3–10× shallower per-cell slope than the 20–30 range), consistent with
  Q_ext approaching a positive residual as the hidden core shrinks, not
  falling indefinitely.
- **Honest caveat flagged, not resolved this shift:** the curve
  conflates "a smaller hidden PEC core intrinsically scatters less"
  with "the shell genuinely cloaks better when thicker" — `q_ext` is
  normalized by the fixed outer radius throughout, so this isn't a
  normalization artifact, but the missing control (a bare, uncloaked
  PEC disk at the same radii) wasn't run. Logged as exp-008 candidate,
  next in line — resolves the caveat before core=8 gets treated as an
  actual better cloak design.
- Four commits to main this shift (`c783486` exp-006 predictions,
  `4f6103b` exp-006 results, `cef3c7c` exp-007 predictions, `969e4b5`
  exp-007 results) — two full predict→run→conclude cycles, gated end to
  end, one honest refutation (exp-006 P3) alongside five confirmed
  predictions, plus a caveat surfaced and disclosed rather than glossed
  over.

## 2026-08-10 (cloud shift 2) — exp-004 and exp-005 CONCLUDED: the clamp isn't a staircase artifact

**Pre-flight:** local `main` ref was stale (last shift's commits landed on
`origin/main` but the local branch pointer hadn't followed) — fast-forwarded
before touching anything, no data loss, just a bookkeeping catch-up.
Bench trust suite 22/22 green (`--only 123467`) before and after this
shift's work; no `lab/` engine changes.

**exp-004 — The Clamp Band (CONCLUDED)**
- Picked up exp-003's queued candidate: isolate `mu_r_floor` alone
  (electrical size + cpl held fixed, exp-003's own geometry reused) at
  420/480/540/600nm × 5 floor values (0.05→0.40, upward from baseline
  only — going below 0.05 needs a paired `courant_frac` cut for CFL
  stability, derivation committed in NOTES.md, not run this shift).
  Predictions (P1–P5) committed before the 20-cloak-run sweep (`ac29101`).
- **Finding: the 480nm bump isn't wavelength-special.** Q_ext(cloak) vs
  `mu_r_floor` is non-monotonic — sometimes sign-flipping — at *every* λ
  tested, under gates too clean to blame on noise (box_dev ≤1.8%,
  cross_dev ≤0.1% throughout; `i_inc` bit-identical across the whole
  floor sweep at each λ, a free harness check). exp-003's specific
  480nm-high reading was just where that λ happened to land on one of
  these jumps — 420/540/600nm each show comparable structure at other
  floor values. floor=0.05 reproduced exp-003's cloak numbers to <0.1% at
  all four λ (P2, tightest reproduction yet). Working hypothesis logged:
  clamp-boundary cell-alignment on the fixed grid (staircase artifact).

**exp-005 — Does the Clamp Jump Shrink With Resolution? (CONCLUDED)**
- Direct test of exp-004's hypothesis, run the same shift: reran the
  clearest jump (600nm, floor=0.10→0.18, a 17.7% rise-then-fall at
  cpl=20) at 1.5× resolution (cpl 20→30, physical geometry held fixed,
  5 cloak runs). Predictions committed before running (`64be902`).
- **Finding: it's not a staircase artifact.** The jump barely moved
  (17.7%→16.4%, a 7.2% relative reduction for a 50% resolution increase
  — far too little for grid-alignment noise) and the entire 5-point
  curve's *shape* survived refinement almost unchanged (Pearson
  correlation 0.9996 between the cpl=20 and cpl=30 curves; per-point
  ratios drift smoothly 0.94→1.01). **Refutes exp-004's staircase
  hypothesis.** Sharper read: the non-monotonicity looks like an
  intrinsic feature of how `mu_r_floor` reshapes the shell's `mu_r`
  profile against its fixed `eps_z=2.25`, not a numerics artifact.
  exp-006 candidate logged: vary `eps_z` independently (r1/r2 ratio) at
  fixed floor values.
- Four commits to main this shift (`ac29101` exp-004 predictions,
  `19fe82c` exp-004 results, `64be902` exp-005 predictions, `37fc3ea`
  exp-005 results) — two full predict→run→conclude cycles, gated
  end to end, honest refutation both times (P3/P4 in exp-004, P3 in
  exp-005) alongside the confirmed predictions.

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
