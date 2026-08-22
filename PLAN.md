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

## Current state (2026-08-22, panel Iteration 36 done (exp-059, PARTIAL —
Checkpoint criterion 4 fired and was remediated same-shift, Marsh notified,
see CHECKPOINT below — provisional-to-PROMISING per Red Team's own stated
path now that the Tier-1 fixes have landed and re-verified); rotation
continues at MATERIALS for Iteration 37, no new LOCK fires — see
PANEL.md/LOGBOOK.md for the phenomenon-program's own current state; this
section's numbered history stops at the pre-redesign exp-023 baseline,
panel-era entries live in the queue below and in full in LOGBOOK.md)

**CHECKPOINT (Iteration 36, 2026-08-22, criterion 4 — program-integrity
drift).** Red Team's Phase-5 audit ruled Checkpoint criterion 4 FIRES,
without qualification: the caveat-placement/propagation defect pattern
(Iterations 17/24/32/33/34/35) recurred TWICE, independently, inside
Iteration 36 itself — the first time it has recurred inside the very
cycle whose own mandatory fix (MF-3) was written to close it. Not a
physics finding — all four `Q_ext(x)` gates, the regression anchor, and
every one of six Phase-5 seats' independent re-derivations stand
unchallenged. Three Tier-1 doc fixes applied same-shift (`lab/qext_theory.py`
×2 sites, `lab/validation/run_all.py`'s stage-21 docstring), full bench
67/67 reverified after. Per Iteration 17's own direct precedent this is a
notification, not a pause: Marsh is convened (this entry + LOGBOOK.md
Iteration 36 + SESSION_LOG.md), unblocked Iteration 37 work continues. A
mechanical, lint-style caveat-propagation-check tool (not another
hand-applied wording patch) is queued as Iteration 37's own #3 priority,
per Red Team's own ruling that a fifth wording-only fix would not
distinguish this closure from the six that already preceded and failed to
hold. Full record: LOGBOOK.md Iteration 36 Phase 5.

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
- exp-016 CONCLUDED (this shift) — mechanism candidate 1 (outer-boundary
  impedance mismatch): pure material-array probe, no FDTD stepping —
  built a bare `Sim`, called the real `schurig_reduced_cloak_tm`
  builder, and read the actual solver tensor at r=r2 across the trough
  bracket (r1=27–33) plus exp-006's corner points (15/40/48), at
  floor=0.10/0.18/0.40. **Refuted, decisively, two ways at once:**
  `|Γ(eps_z)|²` (the outer-wall reflection coefficient) rises smoothly
  and strictly monotonically with zero local feature anywhere near the
  trough, and it is *exactly floor-identical* at every trough-bracket
  point (0.10 vs 0.18 give bit-identical `mu_r(r2)`) — a floor-
  independent quantity structurally cannot produce the floor-dependent
  sign flip that defines the trough. Honest bonus finding: grid
  quantization can flip a point from "analytically unclamped" to
  "numerically clamped" right at threshold (r1=33/floor=0.40) — a small,
  real effect the continuous formula alone would have missed.
- exp-017 CONCLUDED (this shift) — mechanism candidate 2 (angular-
  pattern shape comparison, trough vs flanks): new instrumentation added
  to `lab/sections.py` (`angular_scattered_pattern`, verified against
  stage 8 + a per-run self-consistency identity at machine epsilon), run
  at r1=27/30/33 (flank/trough/flank), floor=0.10, λ=600nm — 4 runs,
  5.1 min. **Also refuted — magnitude-only, no new scattering mode.**
  Shape correlation places the trough inside the same family as both
  flanks (0.9688/0.9717 vs the flank-flank 0.9383); the one asymmetry
  (trough correlates *better* with each flank than they do with each
  other) is fully explained by ordinary distance in eps_z-space, not
  anomaly. **Both queued mechanism candidates are now closed — neither
  explains the trough.** New candidate proposed for a future shift: a
  frequency-domain view (sweep λ at fixed core=30/eps_z=2.25 — the
  mirror of exp-003's λ sweep — to test whether the trough is a
  resonance-like condition tied to the fixed λ=600nm/cpl=20 grid rather
  than a pure eps_z effect).
- exp-018 CONCLUDED (this shift) — the frequency-domain mirror
  experiment exp-017 queued: swept λ (420–750nm, exp-003's own scaling
  machinery) anchored at the trough's own geometry (r1=30/r2=90 at f=1),
  scaling r1/r2 together so eps_z stayed inside the established trough
  window (2.2228–2.2907) at every λ while the shell's radial extent in
  wavelengths varied 2.40λ–4.30λ. **Major reframe: the eps_z trough is
  not an eps_z effect.** The negative floor-0.10→0.18 jump survived at
  exactly one point — λ=600nm, the *only* sweep point where shell
  thickness (r2−r1=60 cells) lands on an exact integer number of
  wavelengths (3.00λ at cpl=20). All 5 other points came back positive
  (+3% to +92%) despite eps_z barely moving (0.068 range) — eps_z does
  not track the effect; shell-thickness-in-wavelengths does. Gates clean
  (box_dev ≤1.81%, cross_dev ≤0.085%); λ=600 point reproduces exp-014's
  reused number exactly. Reframes exp-006/011–017's "eps_z≈2.25 trough"
  as a coincidence of exp-002's original geometry choice (shell=3.00λ),
  not a real eps_z-axis feature. New sharp hypothesis: a shell-thickness
  standing-wave/Fabry-Pérot condition — tested immediately by exp-019.
- exp-019 CONCLUDED (this shift) — exp-018's own queued direct test:
  brackets r1=50 (shell=40 cells=2.00λ) ±3 cells, mirroring exp-014's
  bracket around 3.00λ, same floor pair, r2=90 fixed. **The
  standing-wave hypothesis does NOT generalize to 2λ.** All 5
  complete-floor-pair points (r1=47–51) show positive jumps (+34% to
  +46%), squarely inside the range exp-018 found at its own non-3λ
  points — no dip, no band, nothing resonance-like near 2λ. Narrows
  exp-018's hypothesis considerably: whatever produces the negative jump
  at 3λ isn't a generic "shell = integer × λ" rule; 2λ and 3λ behave
  differently. r1=48 reproduces exp-006/013's existing core=48 numbers
  exactly (sanity check). One honest gate miss flagged, not hidden:
  r1=47/floor=0.18 box_dev=2.17%, just over the 2% band (doesn't touch
  the r1=50 target point, itself among the cleanest in the set, or the
  qualitative conclusion).
- exp-022 CONCLUDED (cloud shift 10; renumbered at the redesign merge) — exp-019's own queued follow-up: every
  point in the eps_z/shell-thickness line since exp-006 had shared one
  fixed outer radius, r2=90 cells — never varied. Moved r2 itself for
  the first time (r2=75 and r2=120, brackets around r2=90), holding
  shell=3λ=60 cells fixed at each, ±3-cell bracket around each new
  target, floor pair 0.10/0.18 reused. **Result: neither new r2
  reproduces r2=90's negative jump at its own shell=3λ point** — both
  targets come back strongly positive (+173.5% at r2=75/r1=15, +51.0%
  at r2=120/r1=60), squarely inside the range exp-018/019 already found
  at every non-3λ/non-r2=90 point. **The "shell=3λ" feature is
  r2=90-specific, not a portable shell-thickness law.** Combined with
  exp-018 (not eps_z) and exp-019 (not any-integer-λ), the population
  of things that don't explain the original exp-004/005/006 finding is
  now large; still zero mechanism identified. One honest gate miss
  flagged: 4 of 7 r2=75/floor=0.10 points missed box_dev≤2%
  (2.55–3.36%) — resolved same-shift by exp-023.
- exp-023 CONCLUDED (cloud shift 10; renumbered at the redesign merge) — direct resolution check (cpl 20→30,
  exp-005/010/015 precedent) on exp-022's r2=75/floor=0.10 gate misses,
  3 representative core points (worst miss, target, clean flank).
  **Gate miss was ordinary cpl=20 grid noise**: box_dev roughly halves
  at all 3 points (e.g. 3.36%→1.71%), all now clear 2%; jump values
  shift only 3.1–4.8% relative, no sign flip. Closes exp-022's one open
  caveat in the same shift it was raised — the r2=75 half of exp-022's
  conclusion now stands on fully gate-clean footing.

**2026-08-12 — program redesign (Marsh's directive, in-session):** new work
runs under `PANEL.md` / `LOGBOOK.md` — the seven-seat research panel
targeting the founding phenomenon under four explicit constraints (beam
termination · no return · **no ambient silhouette** · switchable),
continuous mode with checkpoints. The remaining [open] items below are
**PARKED** (mirrored in LOGBOOK.md, resumable, off the critical path).

- [done 2026-08-12, panel Iteration 1] **exp-020 the ambient-appearance
  baseline** — instrument built (stage 9, 13/13; Beer–Lambert anchor to
  0.001), constraint 3 measured for the first time: absorber C = −0.686
  (Tier-A photopic FAIL ×34 field bar), material blindness ~20% (rim
  transmission), dilute sponge on its geometric value to 0.001. Verdict:
  PROMISING. 750 nm carries an asterisk pending the margin rerun.
- [done 2026-08-12, panel Iteration 2, cloud panel shift] **exp-024 the
  instrument-margin fix** — MARGIN_MULT=3.5 (ny 1200→1584) REFUTED as the
  governing mechanism (δ_C gate missed at all 6 λ/weighting combos,
  non-monotonically — 450nm got worse despite the best margin ratio ever
  measured); the pre-committed ±35° fallback (dropping only the ±40°
  angles) resolved it cleanly everywhere instead, localizing the real
  mechanism to something angle-specific at ±40°, not margin-ratio-driven.
  Bonus: settled the λ-ordering question exp-020 left open — a real, small
  (~1.5–1.9%) red-ward |C| growth in hard-edged articles survives the
  clean floor (not pure bias). Constraint-3 headline reconfirmed
  (C≈−0.684). exp-025 (same shift, direct resolution check on the
  chromatic finding, closing a gap Red Team's Phase-5 audit caught):
  CONFIRMED real, not a grid artifact — 4th time this program's R3 rule
  has refuted an artifact hypothesis. Verdict: PROMISING. Full record:
  LOGBOOK.md Iteration 2.
- [done 2026-08-13, panel Iteration 3, cloud panel shift] **exp-026 the
  σ(I) endpoint triplet** — MATERIALS' OFF-lab/OFF-field/ON static sponge
  articles (τ=0.008/0.032/3.9) on the ±35° fallback baseline, 114 new FDTD
  sim calls. Red Team's decisive Phase-2 catch: the original P-MAT8
  prediction (σ_abs/σ_ext≥0.90 for the ON article) directly contradicted
  the bench's own ESTABLISHED `graded_black_shell` measurement (0.51,
  same r_out) — rebanded to [0.35,0.65] pre-freeze, confirmed by real data
  (measured 0.606–0.608). Seven of eight predictions confirmed cleanly;
  P-MAT6 (a calibration constant) held at 4 of 6 points, both misses on
  OFF-lab in opposite directions. **No PASS/FAIL or constraint-3 language
  attaches to the near-threshold OFF-lab/OFF-field C readings** (VISION's
  mandatory ruling, Red Team-escalated) — the first cycle to produce C
  values with real SNR against both frozen bars, but the r=156 scale-bridge
  check that would license perceptual language stays queued, not built.
  Two new findings: (1) beam-behind is NOT wavelength-flat (46% relative
  spread, non-monotonic, uncorrelated with grid resolution — PHOTONICS'
  Phase-5 candidate mechanism: a settling-time artifact from fixed
  `BEAM_STEPS` across a cpl sweep, not real material physics); (2) the ON
  article's σ_abs/σ_ext sits ~0.10 ABOVE the 0.51 anchor, opposite the
  direction Red Team/EM's own mandatory-fix reasoning predicted — and EM's
  Phase-5 review sharpened this into a program-wide finding: **both 0.51
  and 0.61 exceed the idealized ≤0.5 geometric-optics ceiling**, meaning
  neither is the asymptotic material constant this program has been
  citing (new LIVE THREAD T9). Red Team's Phase-5 audit (verdict: MINOR
  ISSUES) caught two real record defects — P-MAT6's miss-count undercounted
  (an undisclosed second miss, not floor-explicable) and a run-count/
  elapsed-time bookkeeping inconsistency (a code instrumentation bug) —
  both corrected same-shift in NOTES.md/LOGBOOK.md and `run.py`. Verdict:
  PROMISING. Full record: LOGBOOK.md Iteration 3.
- [done 2026-08-13, panel Iteration 4, cloud panel shift] **exp-027
  settling, spread, and the PEC ablation** — resolved both of Iteration
  3's queued threads in one cycle. T9 **ANSWERED**: PEC-core presence is
  incidental to the established 0.51-vs-0.61 σ_abs/σ_ext gap (true
  Δ=+1.56×10⁻⁶ between PEC-cored and PEC-free versions of the identical
  graded-shell profile, indistinguishable from zero; angular-pattern
  channel independently corroborates) — rim/profile-transmission geometry
  drives the gap, not the PEC core, though not yet formally floor-gated
  (Red Team's Phase-5 catch: box_dev is ≈1221× the measured delta, no
  established decision floor exists for this channel yet). P-MAT4's
  chromatic beam-behind anomaly: settling-time cleanly, uniformly refuted
  at all 3λ (doubling `BEAM_STEPS` moves beam-behind ≤0.0012pp everywhere)
  — but the standard R3 spatial check (cpl×1.5) made the anomaly WORSE
  (46%→128% relative spread) instead of confirming/refuting it as
  artifact, the first time in 6 R3 applications this program has produced
  that outcome (new LIVE THREAD T10). Red Team's Phase-5 audit (MINOR
  ISSUES) caught two numeric defects (a rounding slip inflating the T9
  delta 6.4×; the pre-freeze-disclosure blind-run count undercounted "3 of
  16" vs. the true 8 of 16) and QUANTUM independently caught a scoring
  error (VISION's commitment clause read "not triggered" using only Block
  1's data when Block 2's much larger shift — up to −1.54pp — does trigger
  it) — all four corrected same-shift in NOTES.md/LOGBOOK.md. Verdict:
  PROMISING. Full record: LOGBOOK.md Iteration 4.
- [done 2026-08-13, panel Iteration 5, cloud panel shift] **exp-028 the
  radial ledger and the channel cross-check** — resolved both of
  Iteration 4's queued threads, one (T10) far more substantially than
  predicted. New machinery: `lab/sections.py::radial_absorbed_power`
  (radial-binned absorbed-power ledger), gated by new suite stage 10
  (PEC-core hard zero + empirical closure, calibrated 1.5% after a
  first-run measurement of 1.11%, confirmed settling-independent). Full
  bench 45/45 green throughout. **Load-bearing Red Team catch, before any
  run**: exp-027's own published Block 2 (the T10 finding) never rescaled
  `SIGMA_ON` per λ, silently drifting the ON article's optical depth from
  3.9 to 5.70/5.85/5.95 across the sweep — an explicit erratum added to
  T10's LOGBOOK entry, independent of exp-028's own outcome. Result: **T10
  substantially reframed** — the correctly-τ-held rerun shows box-ledger
  σ_ext spread flat (6.49%) and the corrected beam-behind spread only
  46.41%→49.46% (+3.05pp), not the published 46.41%→127.57% (+81.16pp) —
  **96% of T10's reported "enlargement" evaporates**; a small residual
  survives, open. **T9 sharpened from coincidence to mechanism**: Cell B's
  (non-PEC) core absorbs only 0.0062% of total power (resolution-stable)
  — the graded shell's own σ(r) profile extinguishes nearly everything
  before the field reaches the core, in either construction. Phase 5 (six
  fresh seats + Red Team audit): three of six seats independently caught
  the same display-rounding defect (core_frac shown as "0.01%", true
  0.0062%) and Red Team caught a second instance of the same bug class
  (a resolution-match figure) — both corrected same-shift; **new LIVE
  THREAD T11 opened** (box-ledger channel's own decision-floor
  characterization, promoted from a twice-recurring unassigned backlog
  item); VISION's Phase-5 dissent (arguing r=156 should move to Iteration
  6, not 7) preserved on the record, not overridden silently; Checkpoint
  criterion 4 pre-registered as a tripwire on Iteration 7's r=156 build
  actually happening. Verdict: PROMISING. Full record: LOGBOOK.md
  Iteration 5.
- [done 2026-08-13, panel Iteration 6, cloud panel shift] **exp-029 the
  coherent-superposition bridge gate** — QUANTUM's own mandatory,
  fourth-cycle build (deferred three times prior), scoped per its own
  Iteration-5 Phase-5 notes: graded-shell endpoint article (exp-028's
  Cell B construction, not a uniform disk), `radial_absorbed_power`'s
  closure identity as a second acceptance gate, derived (not hand-copied)
  material constants. New machinery: suite stage 11 (multi-source
  coherent superposition gate — two absolute identities, joint-vs-summed
  phasor at 1.9×10⁻¹⁵/2.4×10⁻¹⁵ RMS relative error, both vacuum and
  lossy-object scenes), full bench 48/48 green. **Every prediction
  confirmed — the cleanest cycle in the program's history by that
  measure.** Bridge-gate machinery now validated end-to-end, no longer
  deferred. Coherent interference cross-term measured for the first time:
  +0.0224% of beam absorption, 126–152× below its own Cauchy-Schwarz
  ceiling (two independent Phase-5 re-derivations, EM and QUANTUM,
  converged on a corrected TRUE ceiling of 3.40% from measured powers,
  vs. the pre-registered nominal 2.83%) — a normalized degree-of-
  coherence γ≈0.66%, real but ~99.3% washed out by spatial averaging in
  this geometry (not a universal law, QUANTUM's own caution). Bin-wise
  check confirms real, small spatial structure (5.02× the aggregate,
  genuine radial interference fringe) an aggregate check alone would
  wash out. Red Team's Phase-5 audit (verdict: MINOR ISSUES) caught one
  real record defect: VISION's Phase-5 "fourth consecutive constraint-3-
  silent cycle" count was itself wrong (Iteration 3 ran a real 81-run
  ambient scene with C values, misclassified as beam-scene-only) —
  corrected to **three**, matching Iteration 5's own original count.
  **Checkpoint criterion 5 given an explicit ruling for the first time in
  the program's history** (non-firing). T11 folded in as a companion to
  Iteration 7's own r=156 build (VISION's own Phase-5 pick, near-
  unanimous 5-of-6 seats). QUANTUM's own remaining open half (the
  incoherent-ensemble/phase-quadrature idiom, concretely scoped and
  mathematically pre-verified by Red Team) queued for a future QUANTUM
  lead cycle. Verdict: PROMISING. Full record: LOGBOOK.md Iteration 6.
- [done 2026-08-14, panel Iteration 7, cloud panel shift] **exp-030 the
  r=156/312 near-field→witness-scale bridge (T8) + box-ledger floor
  companion (T11)** — VISION's five-times-deferred mandatory build,
  hard-committed at Iteration 5's close with a pre-registered
  Checkpoint-4 tripwire: **executed in full this cycle, the tripwire
  does not fire.** Red Team's Phase-2 audit caught the Phase-1
  proposal's r=78 anchors citing the wrong, gate-failing ±40° geometry
  (corrected in code: absorber −0.7209, PEC −0.8673, V-weighted
  fallback) plus a three-way-converged `graded_black_shell` optical-
  depth confound (fixed: σ_max=0.5/κ, holding radial optical depth
  constant). 89 new FDTD sim calls, ~5.1h (r=312's 37-run leg alone took
  3.87h — ~8× the proposal's own estimate, the largest timing miss in
  program history, κ³ FDTD scaling). **Real deliverable: PASS/FAIL
  language is now decidable on near-threshold constraint-3 C values for
  the first time** — the δ_C floor gate passed cleanly at both r=156
  and r=312; T9 and T11 both close with their first floor-referenced
  verdicts (T9 decisively null 234–446× below the floor, T10 decisively
  real 93–178× above it). **But scored against VISION's own frozen
  thresholds, every σ(I) OFF-state article ever built is still MARGINAL
  (OFF-lab) or FAIL (OFF-field) at every scale tested — no configuration
  has ever PASSed constraint 3.** The cycle's central technical question
  — does C(z/z_R) bridge cleanly to witness scale — came back genuinely
  unresolved: PEC's C(r) is flatly non-monotonic (new live thread
  **T12**, candidate mechanism: Fresnel-zone/edge-diffraction ripple
  aliased by the family's factor-4 r-steps at fixed measurement-plane
  offset, independently proposed by PHOTONICS and EM); and Red Team's
  Phase-5 audit — missed by all six blind review seats — found this
  cycle's own fitted witness-scale prediction (≈−0.73/−0.86) sharply
  contradicts the |C|≈0.98 estimate that has justified this whole
  thread since Iteration 1 (new live thread **T13**). **Verdict:
  PARTIAL.** New Checkpoint-4 tripwire adopted: any future citation of
  this cycle's witness-scale numbers without flagging T13, or any
  reliance on PEC's fit or box_dev as a settled floor before their own
  R3 checks land, is a retroactive trigger. Full record: LOGBOOK.md
  Iteration 7.
- [done 2026-08-14, panel Iteration 8, cloud panel shift] **exp-031 the
  T12 ripple sweep, the T13 desk reconciliation, and QUANTUM's σ-held
  g-point** — Red Team's Phase-2 catch (none of five blind seats found
  it): exp-030's own `graded_black_shell` "absorber" construction was
  missing its historical PEC core (a hollow, not solid, shell at every
  θ=0/ambient reading it ever produced). Fixed, folded into this cycle's
  own T12 sweep. 18 new FDTD calls (~13 min for the sweep+quantum legs;
  the accepted THERMO sidecar failed twice and is deferred, root cause
  pinned by THERMODYNAMICS' own Phase-5 review — a bad `ref`, not just a
  bad box — and guarded in code against a silent third attempt).
  **T12's own dense PLANE_DX sweep came back a clean null** (zero
  significant ripple reversals across 17 points) **but its N_F coverage
  (≈8–110) never reaches the window (≈81–325) where the original
  r=156→312 reversal actually lives** — narrowed, not refuted; the
  correct next test is a genuine r-family sweep, not a denser PLANE_DX
  sweep (Red Team found EM's own proposed cheap fix likely infeasible —
  it would require sub-0.2λ standoff). **The core-correction delta is
  negligible** (6.8×10⁻⁶) — good news, independently reproducing T9's
  "core is incidental" finding via a new channel. **T13 stays
  unresolved for the one article that matters and got WORSE, not
  better**: the corrected absorber's dual-law disagreement (0.220)
  exceeds the original (0.132). Red Team's Phase-5 audit elevated this
  into new live thread **T14** — the absorber's contrast shallows,
  not deepens, toward what should be the geometric-shadow limit,
  confirmed on three independent axes (construction, baseline,
  functional form), the same pathology Iteration 7's finding e2 first
  named. **QUANTUM's g-calibration gap closes** at one new floor-
  corrected point (g=0.697, within 2% of established endpoints) —
  language corrected at Phase 5 to state this is licensed only in the
  weak-perturbation regime tested, not program-wide. **Verdict:
  PARTIAL. Program-integrity flag raised explicitly by Red Team, adopted
  by the Director as a binding Iteration-9 priority (not a Checkpoint
  violation — neither criterion 4 nor 5 fires on the letter)**:
  Iterations 4–8 are five straight cycles of instrument/reconciliation
  work; VISION's cheapest, most directly mechanism-relevant proposal (a
  σ(I) PASS-boundary run) has been the top Phase-5 pick for three
  iterations running without being built. Full record: LOGBOOK.md
  Iteration 8.
- [done 2026-08-14, panel Iteration 9, cloud panel shift] **exp-032 the
  σ(I) OFF-state PASS-boundary run** — MATERIALS' lead (rotation),
  executing Iteration 8's three-times-deferred binding priority. One new
  static/linear σ(I) OFF-state article (`off_pass`, τ=0.0065) plus Red
  Team's mandatory below-τ_off bracket point (`off_bracket`, τ=0.003), on
  exp-026's exact ±35° N=9 fallback bench. **`off_pass` clears VISION's
  frozen |C|<0.005 lab bar at all 3λ — the first σ(I) OFF-state
  configuration in this program's nine-iteration history to do so.**
  But g600(off_pass)=0.6927 tripped QUANTUM's own pre-registered
  disposition clause (≥0.69, matching off_lab's established, previously-
  unexplained g600=0.6913) — now a 4-point recurrence across three
  experiments, but Phase 5 (PHOTONICS + QUANTUM, independently) caught
  that every point shares an untested grid resolution at 600nm (the one
  wavelength on this bench line never R3-checked) — "reproducible"
  language walked back to flagged-pending-check. The bracket-point
  discriminator came back a genuine, uninformative null on the bulk-vs-
  edge-scattering mechanism question (EM's Phase-5 finding: the ambient-
  contrast channel is structurally underpowered for that question
  regardless of SNR at these τ; the correctly-targeted instrument,
  `radial_absorbed_power`, exists and was unused this cycle). A PASS here
  mechanically worsens σ(I)'s realizability picture (σ_on/σ_off → ≈600×,
  worse than any prior cycle) — MATERIALS' Phase-5 informal literature
  check put real numbers (reverse saturable absorbers, 2–10×) 1–2 orders
  of magnitude short of that target for the first time in seven cycles of
  citing "unobtainium." THERMODYNAMICS' own energy-sidecar fix had a
  self-caught, same-shift-corrected arithmetic defect (a ~6.4× ratio-
  composition error). **Verdict: PARTIAL** — 5 of 6 seats + Red Team's
  adjudication; QUANTUM OPTICS' lone PROMISING dissent preserved on the
  record, overridden per this program's own precedent (verdict turns on
  whether a cycle's own open questions close, not a favorable headline
  number). This PASS is explicitly a bench-scale diagnostic (VISION's own
  idealization iii), NOT a Tier-W/Tier-A constraint-3 verdict — the
  r=156 scale-bridge companion leg stays queued, now third in line. No
  Checkpoint criterion fires. Full record: LOGBOOK.md Iteration 9.
- [done 2026-08-15, panel Iteration 10, cloud panel shift] **exp-033 the
  g600 resolution check** — ELECTROMAGNETISM's lead (rotation), executing
  Iteration 9's top-ranked priority. R3-checked (cpl 20→30) the g600≥0.69
  recurrence at 600nm, the one wavelength on this bench line never
  resolution-tested, using a free-curvature-fit currency (g_corr, not the
  imposed 4/3π coefficient QUANTUM's Phase-2 review showed was already
  refuted by existing data) instead of raw g600. **Block B
  (`radial_absorbed_power` applied to off_pass/off_bracket, Iteration 9's
  #2 priority) was CUT this cycle** — PHOTONICS' Phase-2 critique found it
  structurally underpowered by 2–3 orders of magnitude and partly
  sign-degenerate, independently confirmed by Red Team; re-queued
  standalone, not run unmodified (Red Team's own sanctioned fallback).
  **Result: the raw-g600 cross-resolution shift is fully explained by the
  empty-scene decision floor's own shift, verified three independent ways
  to ≈10⁻⁸ precision** (EM's zero-parameter geometric chord model,
  QUANTUM's per-article decomposition, Red Team's cross-check) — a real
  advance, closing T1's carried-forward Iteration-9 item. **But Phase 5's
  seven-seat review (5 PROMISING, 2 substantive PARTIAL — PHOTONICS, Red
  Team) found the cycle answered a narrower question than first claimed**:
  the raw-g600 reading itself got MORE pronounced under refinement
  (0.6927→0.7056), not less; ΔA≈0 is closer to guaranteed-by-construction
  (the resolution change was almost entirely a common-mode floor shift
  that g_corr is built to cancel) than to strong evidence g₀ carries no
  separate resolution-dependent wave physics; and the actually-SCORED raw-C
  currency was never itself shown resolution-converged (moved toward FAIL
  at all four articles, only two resolution points). Two new open
  questions surfaced: g₀ sits ~15% below its own window-integrated
  geometric chord model, stable across resolution — argued as a real
  diffractive-leakage effect, not noise (PHOTONICS); and the retired
  QUANTUM Iteration-9 disposition clause's numeric successor is logically
  circular (Red Team). A real run-count bookkeeping bug was caught and
  corrected same-shift (50 FDTD calls, not 47 — the settling-control block
  runs all 5 scenes per invocation, not 2). **Verdict: PARTIAL**,
  Director adopting Red Team's audit over the raw 5-2 seat-verdict count,
  per this program's own established precedent (verdict turns on whether
  a cycle's own open questions close). MATERIALS' Phase-5 review found R3-
  CONFIRMED *hardens*, not leaves orthogonal, the σ(I) realizability
  tension, and surfaced a new, much larger gap: the mechanism must gate at
  flashlight irradiance (~10⁻³ W/cm²) against published RSA/two-photon
  onset thresholds (10⁶–10⁹ W/cm²) — 9–12 orders of magnitude short, a
  candidate Checkpoint-criterion-2 finding if it survives a dedicated
  check. No Checkpoint criterion fires this cycle (the Phase-3 tripwire on
  citing the PASS without its ε_r restriction was corrected same-shift,
  per Red Team's own conditional ruling). Full record: LOGBOOK.md
  Iteration 10.
- [done 2026-08-15, panel Iteration 11, cloud panel shift] **exp-034 the
  paired floor-convergence / r=156 scale-bridge cycle** — THERMODYNAMICS'
  lead, executing Iteration 10's two ranked priorities in one cycle plus
  Red Team's own mandatory fifth fix (Block N17_NATIVE, folded in by
  Director's budget call). Four independent blocks, 115 new FDTD calls
  (a harness bug — `ex.map`'s argument-passing mistake — crashed the
  first attempt after 46 calls, fixed and disclosed, full rerun clean,
  3378.8s). **CPL40 closed T1's carried-forward item cleanly**: both the
  empty-scene floor and the scored raw-C currency landed PLATEAU at
  cpl=40, neither converging nor diverging. **R156 found the program's
  only-ever σ(I) OFF-state PASS is fragile at scale** — every r=156
  reading of `off_pass` sits on the MARGINAL/near-PASS side of the bar,
  directionally robust across instrument choices, but Red Team's Phase-5
  audit confirmed a **second, undisclosed, comparably-sized domain-
  construction confound** (found by ELECTROMAGNETISM, missed by five of
  six blind seats and two Director catches) stacked under the disclosed
  angular-quadrature one — the "downgrades to MARGINAL" headline is
  directionally right but not yet resolution/domain-clean. **N17_156/
  N17_NATIVE found N9 angular quadrature — this program's own measurement
  standard since Iteration 1 — is NOT converged**: 0.88× the established
  N5-vs-N9 bound at r=156 (still flips the PASS/MARGINAL bucket), 3.2×
  the bound at r=78-native (the geometry the PASS citation actually
  uses). New live thread **T16** opened (the ambient-contrast channel's
  own angular-quadrature/domain-construction uncertainty budget, now
  measured for the first time and comparable to or larger than several
  headline PASS margins). **MATERIALS' realizability memo, deferred three
  iterations, finally written**: UNOBTANIUM-WITH-PARAMETERS for both
  candidate σ(I) mechanism classes — reverse saturable absorbers 1–2
  orders of magnitude short on dynamic range, two-photon absorption 9–12
  orders of magnitude short on operating irradiance, for two independent,
  non-trading-off reasons (`REALIZABILITY_MEMO.md`, a candidate
  Checkpoint-2 finding pending a rigorous, not informal, literature
  check). **Seven-seat Phase 5: unanimous PARTIAL, 7-for-7** — the first
  unanimous panel-era verdict — with four independently-converged
  arithmetic catches (a 1.9%→0.56% chord-sanity correction; a "4.2×"
  Learned-section error; a C78 anchor mislabeling; a dropped THERMO
  transient-ΔT regression) and one load-bearing new finding (EM's
  R156-vs-N17_156 domain confound) all corrected same-shift per Red
  Team's mandatory-fix list, disclosed not smoothed over. T15 (the g₀
  chord-model deficit) flagged as an open, unresolved three-way
  contradiction — this cycle's own fresh, committed chord model
  reproduces the measured value to 0.56%, not T15's claimed ~15%.
  Checkpoint criterion 4 ruled a tripwire (Red Team), satisfied by the
  same-shift corrections — does not fire. No other criterion fires. Full
  record: LOGBOOK.md Iteration 11.
- [done 2026-08-16, panel Iteration 12, cloud panel shift] **exp-035
  closing the R156/N17_156 domain × quadrature factorial, rebuilding
  N17_NATIVE, and reconciling T15** — QUANTUM OPTICS' lead (rotation),
  executing Iteration 11's own ranked priorities. 68 new FDTD calls (34 +
  34 + 0 desk-only), 2724.3s. Red Team's Phase-2 audit caught a
  load-bearing defect in the Phase-1 proposal (independently confirmed by
  PHOTONICS): the T15 reconciliation's cpl=40 comparator was a copy/paste
  fabrication, not a measurement — corrected via Red Team's own zero-cost
  recipe (raw g=|C|/τ at cpl=20/30/40 vs `chord_model_g0()`). **Result 1
  (T16): the domain and quadrature confounds disclosed at Iteration 11 do
  NOT add linearly at r=156 — they interact** (+2.109×10⁻⁴, at the
  REAL-INTERACTION threshold; ladder bucket stays MARGINAL either way).
  **Result 2 (T16, the bigger one): the r=78-native N17 rebuild — built
  correctly this time, N9 leg bit-identical to exp-033's own established
  citation, proving no domain confound — shows this program's own
  headline, first-ever constraint-3 σ(I) OFF-state PASS (exp-032,
  reconfirmed exp-033) downgrades from PASS to MARGINAL under N17
  quadrature.** As of this iteration, no σ(I) OFF-state configuration
  this program has ever measured survives N17 correction on a correctly-
  built domain, at either geometry tested. **Result 3 (T15): the gap
  grows monotonically with resolution (1.03%/2.69%/3.07% at
  cpl=20/30/40)** — T15 modestly reopens, not closes; a separate π/4-vs-
  chord-model-amplitude gap was fully explained as definitional (θ=0-only
  vs N9-oblique-averaged) and formally closed. Phase 5: **unanimous
  PARTIAL, 6-for-6 blind seats, Red Team affirms.** Two seats
  (PHOTONICS, EM) independently proposed the same near-field-fringe
  mechanism for the interaction, but Red Team ruled it plausible-not-
  proven (a real non-self-similarity confound between the two blocks'
  geometry). VISION's sharpest catch: bit-identical N9 does not prove
  N17_NATIVE_V2 is confound-free at N17, since the r=156 result proves a
  domain's effect on C is itself angle-dependent. THERMODYNAMICS caught
  and fixed a real, previously-uncaught numeric bug carried through two
  prior committed experiments (`OFF_STATE_DETECTABILITY_NOTE`'s
  steady-state range, corrected in live code, computed not hand-typed —
  does not change the UNDETECTABLE conclusion). MATERIALS' realizability
  memo recaptioned: D_req≈540–600× is now a lower bound, not an achieved
  reference point — sharpens, not weakens, UNOBTANIUM-WITH-PARAMETERS.
  **Checkpoint criterion 2 ruled explicitly: does NOT fire** — one
  calibration point failing corrected instrumentation is not proof σ(I)
  is jointly unsatisfiable as a mechanism class; that still needs the
  still-deferred rigorous literature check. Red Team's own program-health
  observation (not a criterion firing): Iterations 7–12, six consecutive
  cycles, have all closed PARTIAL, all instrument-hygiene work, not
  mechanism-testing — flagged for Iteration 13's sequencing. Verdict:
  PARTIAL. Full record: LOGBOOK.md Iteration 12.
- [done 2026-08-16, panel Iteration 13, cloud panel shift] **exp-036 the
  rigorous RSA/TPA/photochromic-photothermal literature check** —
  VISION SCIENCE's lead (rotation), executing Red Team's Iteration-12 top
  priority. Zero FDTD calls — the first cycle whose entire "run" was a
  WebSearch-grounded literature search, not a simulation. Four mechanism-
  class rows (RSA, TPA, photochromic, photothermal/VO2 — split from
  photochromic per THERMODYNAMICS' mandatory fix), each confirmed to fail
  via a distinct, now-citation-sharpened gap: RSA short ~22–30× on dynamic
  range even at the best published figure once the absorption-only
  correction is applied; TPA short ~9–11 orders of magnitude on
  irradiance (real citations: Sheik-Bahae/Van Stryland, He et al. 1995,
  ZnSe/GaAs Z-scan studies); photochromic fails on reverse-switching speed
  for durable systems; photothermal/VO2 fails on bulk thermal power-budget,
  shown fatal at every length scale from µm to m via a capped analytic
  estimate (THERMODYNAMICS), not just the cm–m scale originally predicted.
  **New live thread T17**: ELECTROMAGNETISM's Phase-2 catch — photochromic/
  photothermal switching is a hysteretic σ(I)-with-memory mechanism, not
  σ(x,t) as originally framed — exposed a genuinely new constraint-3-at-
  rest risk class. Its structural half (a class-level kinetics derivation:
  any such mechanism with slow reverse rate has a strictly positive
  steady-state colored population under unbounded ambient dwell time) is
  secure, independently re-derived and confirmed by Red Team. Its
  empirical anchor (spiropyran reaching 60–80% steady-state coloration
  under continuous ambient light) was originally over-claimed as "the
  sharpest finding of the cycle" — two independently-converging blind
  Phase-5 seats (PHOTONICS: wrong ambient-intensity regime, sun-comparable
  not the witness's dim/night scene; VISION SCIENCE: a chemistry fact
  never converted into a scored perceptual quantity) caught this, and Red
  Team's audit corrected the language same-shift — real chemistry, visual
  significance unverified, not yet a scored constraint-3 violation.
  **Checkpoint criterion 2 does NOT fire**, for two independent reasons:
  free-carrier absorption and combined saturable/RSA media remain
  untested (pre-disclosed), and even the four covered classes rest on
  WebSearch-snippet synthesis, not primary-source-verified figures (a
  disclosed methodology degradation — WebFetch was blocked by the sandbox
  egress proxy for essentially every scholarly domain across three of
  four search legs). Seven-seat Phase 5: unanimous PARTIAL. Verdict:
  PARTIAL. Full record: LOGBOOK.md Iteration 13.
- [done 2026-08-16, panel Iteration 14, cloud panel shift] **exp-037 the
  free-carrier-absorption / combined saturable-RSA media literature
  check** — PHOTONICS' lead (rotation), executing Iteration 13's
  near-unanimous top priority. Zero FDTD calls, three parallel search legs
  plus two analytic derivations and one capped THERMO estimate. **Closes
  the two mechanism classes LOGBOOK's own Iteration-13 record named as
  the program's last explicitly-tracked untested scope**: free-carrier
  absorption (split into three photonically distinct sub-classes —
  TPA-cascade, linearly-pumped/thresholdless, ENZ band-filling) and
  combined saturable/RSA media (three named architectures). All four fail:
  TPA-cascade FCA inherits TPA's own established irradiance gap (derived
  analytically, not searched — cost discipline); linearly-pumped FCA falls
  1–9 orders of magnitude short on dynamic range (first-ever quantitative
  cross-section for this row-type, Soref & Bennett 1987), with a genuinely
  open, T17-formula-scored at-rest question (n_ss≈10⁻⁹ to ~10⁻¹ depending
  on doping, held to VISION's language cap); ENZ fails on wavelength (near-
  IR, outside the 450/600/750nm sweep) AND on mechanism class (its headline
  nonlinearity is dominantly refractive, not absorptive — a new INSTANCE of
  R1's already-ruled-out principle, not a new failure category, corrected
  same-shift after the cycle's own first draft mischaracterized it);
  combined media fails on dynamic range (~0.65–2.1 orders short, corrected
  from a first-draft arithmetic error) with a "motivation mismatch" (the
  real literature's design goal is pulsed-laser-damage protection, not CW
  ambient-silhouette suppression). Graphene control case confirmed
  wrong-direction. **New live thread T18** (the field-enhancement/
  evidentiary-tier ceiling on the realizability-check line — three
  consecutive cycles of total WebFetch blockage, and MATERIALS' own
  field-enhancement arithmetic shows realistic plasmonic/cavity
  enhancement can't close irradiance gaps beyond ~6 orders of magnitude).
  **Checkpoint criterion 2 does NOT fire** — the evidentiary-tier gap
  alone is decisive, surviving a same-shift correction to the cycle's own
  overclaimed "all six classes checked" framing (the accurate count is
  narrower — see `REALIZABILITY_MEMO.md`'s Amendment 2, rewritten this
  shift with a consolidated nine-class table, a three-cycle-deferred
  MATERIALS deliverable finally closed). Seven-seat Phase 5 (six discipline
  seats + a second independent PHOTONICS self-audit pass, since PHOTONICS
  was this cycle's own lead): 3 independently-converging finding pairs
  across blind seats (wavelength-tagging discipline unexecuted a second
  cycle — PHOTONICS×2 + MATERIALS; ENZ/R1 + CW-pulsed-overclaim — EM +
  QUANTUM on each), Red Team's audit elevating and re-deriving every one
  directly rather than trusting seat characterizations, plus a 17-item
  same-shift fix docket including a genuine THERMO deliverable gap
  (self-caught, ruled load-bearing not queueable — a qualitative analogy
  replaced with an actual numeric estimate). Verdict: PARTIAL. Full
  record: LOGBOOK.md Iteration 14.
- [done 2026-08-16/17, panel Iteration 15, cloud panel shift] **exp-038
  the T17 rate-equation kernel** — MATERIALS' lead (rotation), executing
  Iteration 14's near-unanimous priority #3 (priorities #1/#2 blocked, T18
  re-confirmed a fourth consecutive shift). New machinery: `lab/kinetics.py`
  (0D two-state kinetics integrator, exact-exponential + RK4 propagators)
  + trust-suite stage 12 (5/5 gates, tightest 2.94×10⁻¹⁶). Bench-confirms
  T17's n_ss=k_f/(k_f+k_r) formula to machine precision for the first time
  (no longer resting on algebra alone) across a 25-point host/ratio grid.
  Two genuine implementation bugs (RK4 double-division; a stiff-segment
  cost/stability blowup) caught by the trust-suite gate itself failing on
  first run, fixed pre-trust — house discipline working as designed.
  **P-MAT-4 CONFIRMED** (only Host D lands in T3's provisional window);
  **P-MAT-5a CONFIRMED** (5τ: max ratio 1.006 ≤1.02); **P-MAT-5b PARTIALLY
  CONFIRMED** (the co-location claim — at-rest-memory risk and the
  realizability tier's least-realizable hosts coincide, at D/E — held
  exactly; the predicted 1.4–1.6 magnitude band was refuted by the
  measured 1.00–2.106 range). **Seven-seat Phase 5** (six blind discipline
  seats + Red Team audit, run the following shift after Phase 1-4 sat
  uncommitted to LOGBOOK for one shift boundary — see SESSION_LOG): all
  six seats independently re-derived every headline number from raw
  code/data, zero science-numeric defect found; four same-shift fixes
  applied (a dead-code bug in `run.py`'s P-MAT-5b check, independently
  caught by QUANTUM OPTICS and MATERIALS; the T3-provisional tag missing
  from all four Phase-4 results citations, VISION SCIENCE — the third
  consecutive committed iteration this exact pattern required a Phase-5
  catch, Checkpoint criterion 4 ruled exercised-not-fired with a standing
  instruction that a further recurrence fires it without debate; a THERMO
  N/A ruling resting on a category error, THERMODYNAMICS — exp-037's
  borrowed ΔT_ss figure never used n_ss, so a zero-cost ceiling bound was
  available and wrongly declined; the co-location finding's framing
  overclaiming independence, MATERIALS — Red Team derived it follows
  substantially from this cycle's own fixed pulse-duration parameter).
  `REALIZABILITY_MEMO.md` Amendment 3 added (a separate, tempered
  realizability axis — does not revise the existing linearly-pumped-FCA
  UNOBTANIUM verdict). No Checkpoint criterion fires. Verdict: PARTIAL.
  Full record: LOGBOOK.md Iteration 15.
- [done 2026-08-17, panel Iteration 16, cloud panel shift] **exp-039 the
  T3 temporal-CSF screen** — ELECTROMAGNETISM's lead (rotation), executing
  Iteration 15's ranked #1 priority. New machinery: `lab/temporal_csf.py`
  (pole-frequency screen against sourced de Lange/Kelly temporal-CSF
  landmarks, photopic + scotopic) + trust-suite stage 13 (5/5 gates after
  Phase 5's own fix, tightest 2.22×10⁻¹⁶). Retires the single most overdue
  item on the program's books, deferred at Iterations 13, 14, 15's own
  close. **Load-bearing Red Team Phase-2 catch, independently reconfirmed
  by the Director**: the Phase-1 draft's own headline claim ("all 10
  scotopic Host D/E points classify in_passband") was FALSE under the
  proposal's own numbers — corrected pre-commit to a clean 5/5 split
  (Host D unfavorable at every point, Host E favorable at every point).
  **Phase 5 found the corrected claim itself rested on a second,
  unresolved model choice** (three independently-converging seats —
  ELECTROMAGNETISM, VISION SCIENCE, PHOTONICS): the scotopic classifier
  applies a bandpass decision structure to a regime its own cited source
  calls low-pass. Red Team's audit quantified this as a directional
  REVERSAL, not just a loss of clean differentiation — under the
  corrected low-pass reading, Host E (read as "favorable in both
  regimes") is actually MORE concentrated in the sensitive zone than Host
  D. Mandatory same-shift fix applied: `classify_zone_lowpass` added,
  both model readings now ship side by side, P-EM-5 downgraded to
  `CONFIRMED-UNDER-BANDPASS-MODEL-ONLY` (new live thread **T19**, unclosed).
  **The T3-provisional tag survived intact through Phase 3, Phase 4, AND
  results.json simultaneously for the first time** in a pattern that
  required Phase-5 correction on three consecutive prior committed
  iterations (13, 14, 15) — Checkpoint criterion 4 independently
  reconfirmed NOT to fire, on either the tag pattern or T19's own finding.
  Seven-seat Phase 5 (six blind + Red Team): unanimous PARTIAL. Verdict:
  PARTIAL. Full record: LOGBOOK.md Iteration 16.
- [done 2026-08-17, panel Iteration 17, cloud panel shift] **exp-040 the
  amplitude bridge** — THERMODYNAMICS' lead (rotation), executing
  Iteration 16's unanimously-ranked-#1 priority. New machinery:
  `lab/amplitude_bridge.py` (σ_e(n) mixing law + saturating `chord_contrast`
  ray-chord transfer, generalizing exp-034's `chord_model_g0` into the
  never-before-measured saturation shoulder τ∈[0.3,2]) + trust-suite
  stage 14 (13 gates, two absolute identities). Phase 2's Red Team audit
  (16 numbered attacks, densest single-cycle catch-set to date) found two
  load-bearing defects no blind seat caught (A_req's silent divergence-
  point evaluation; a Block-R σ-copy bug that would have drifted τ by
  +50% and fired a false ARTIFACT) and adjudicated 12 load-bearing / 10
  correctable / 5 overreach-rejected fixes, keeping the cycle at 72 runs
  instead of a ~195-run expansion. **All 5 predictions CONFIRMED, first
  run**: the model reproduces measured |C| at two new shoulder articles
  to 0.20–0.43%, inside the model's existing 0.4–1.15% accuracy band; R3
  (cpl 20→30) measured 0.158%, live-proving the block-local-σ fix
  necessary. **Seven-seat Phase 5 (six blind + Red Team): unanimous
  PARTIAL** — three convergent findings (A_req table used the wrong
  inversion method, non-load-bearing; the chromatic "surprise" is 90–100%
  an instrument-floor artifact, floor-corrected residual runs the OPPOSITE
  direction from the original reading; stage 14's gate count was
  miscounted). THERMODYNAMICS self-reported its own charter gap and,
  filling it at Phase 5, found **v2 is the first article in this
  program's history whose predicted thermal signature crosses ABOVE an
  uncooled-microbolometer NETD band** (Red-Team-corrected framing: not a
  Tier-A exposure, parcel-frame-only, dwell-decided). Red Team's own
  catch (new live thread **T20**): the ±40° angle pair used since
  Iteration 11 to correct the program's only-ever constraint-3 PASS to
  MARGINAL is the same pair Iteration 2 excluded from the standing
  baseline for cause — a program-level inconsistency, never before
  assembled. **Checkpoint criterion 4 FIRES — the program's first
  Checkpoint firing since Checkpoint #0** — on a scope-tag propagation
  failure (process, not physics; every mandatory fix applied same-shift).
  Verdict: PARTIAL. Full record: LOGBOOK.md Iteration 17.
- [done 2026-08-17, panel Iteration 18, cloud panel shift] **exp-041
  auditing the ±40° angle pair as the N17 correction standard (T20)** —
  QUANTUM OPTICS' lead (rotation), executing Iteration 17's Red-Team-
  ranked #1 priority. 38 new FDTD calls (Block MAIN 30, Block OBJPRESENT 2,
  Block EXTEND 6), 137.8s, gates clean (41/41 bench). Phase 2's Red Team
  audit found two load-bearing defects no blind seat's own framing had
  fully resolved: the Phase-1 draft mislabeled 0.005 as the scoring gate
  when exp-024's own committed hard gate is 0.001 (0.005 is VISION's own
  T2 perceptual bar, not an instrument-floor gate — VISION's own catch,
  Red-Team-confirmed against code); and a false claim that θ=40° was
  already exercised by the trust suite (it never had been). Both fixed
  pre-commit; PHOTONICS' and EM's correctable block additions adopted.
  **Result: T20's own question closed, but not the way anyone predicted —
  the ±40° pair was never uniquely bad.** A 1°-step fine sweep found the
  per-angle empty-scene floor oscillates in SIGN with a ~1.4–2.5° period
  (wavelength-dependent) across the WHOLE 36°→43° window; at 600/750nm
  **every** swept angle fails the real 0.001 gate, not just ±40°. New live
  thread **T21** opened. **Seven-seat Phase 5 (six blind + Red Team):
  4 PARTIAL (PHOTONICS, MATERIALS, THERMO, VISION) vs. 2 PROMISING (EM,
  QUANTUM OPTICS)** — Red Team's central adjudication ruled the two
  PROMISING seats' disagreement with PHOTONICS' own λ-scaling read is not
  a real conflict: EM built a zero-free-parameter Huygens edge-diffraction
  model (source taper-edge offset A=752 cells, period P(θ)=λ/(A·cosθ))
  correctly predicting 600nm's clean alternation as a near-Nyquist
  aliasing effect (period≈2°, the 1°-sweep's own Nyquist limit) rather
  than the naive monotonic λ-scaling PHOTONICS' simpler test assumed; Red
  Team's own harder cross-λ phase-deviation test independently corroborated
  EM's mechanism. Ruled NOT primarily a `walk(θ)` grid-quantization
  artifact (wavelength-independent by construction, contradicting the
  observed per-λ pattern; no rounding stage found in `add_line_source`).
  Triple-confirmed citation fix: d(walk)/dθ≈6.0–7.2 cells/degree, not the
  originally-cited "≈4." **VISION's own load-bearing Phase-5 catch**: the
  Phase-3 gate fix had propagated cleanly inside `results.json`/NOTES.md
  but NOT yet into LOGBOOK's own LIVE THREADS T20 entry (still citing the
  stale 0.005 language, no T21 entry) — the exact scope-tag-propagation
  pattern that fired this program's only-ever Checkpoint-4 event one cycle
  earlier; fixed in the same Director's close that caught it, so
  Checkpoint criterion 4 does NOT fire (caught and corrected within the
  cycle, not left to recur). **Verdict: PARTIAL** — T20 closed cleanly and
  informatively; T21's mechanism is well-characterized but not yet
  magnitude-validated (signs/ranking only). Full record: LOGBOOK.md
  Iteration 18.
- [done 2026-08-18, panel Iteration 19, cloud panel shift] **exp-042 the
  edge-diffraction magnitude bridge, and the program's second same-shift
  erratum** — VISION SCIENCE's lead (rotation), executing Iteration 18's
  Red-Team-ranked #1 priority: a zero-cost analytic Huygens–Fresnel
  coherent-sum model scoring EM's edge-diffraction mechanism against all
  30 of exp-041's Block MAIN signed rows at magnitude level, paired with a
  beam-divergence/contamination-risk check. Phase 2's Red Team audit
  (8 mandatory fixes, none overridden) mandated a flux/Poynting reduction
  as PRIMARY, precise scoping of "zero free parameters," a domain-mismatch
  disclaimer, a mandatory coherent cross-check alongside the incoherent
  beam-divergence reading, and an explicit THERMO disposition. **Phase 4:
  sign agreement 28/30, R²=0.4176 (near-exactly the pre-committed central
  0.42) — closes Iteration 18's own magnitude-validation gap.** Beam-
  divergence: zero contamination risk under the incoherent (physically
  appropriate) reading; near-total contrast under the mandatory coherent
  cross-check, read as an idealization artifact. **Phase 5 found two
  load-bearing defects in the cycle's own headline claims**: ELECTROMAGNETISM
  found the committed "PRIMARY" convention misapplies obliquity (the
  Kirchhoff/Rayleigh–Sommerfeld fixed-field-screen recipe, not this
  bench's actual soft/additive current-array source) — the corrected
  convention (R²=0.657, c*=1.62) matches VISION's own original, mandatory-
  fix-3-superseded preliminary numbers almost exactly; VISION's own
  self-review found Block BEAM's "zero contamination risk" was never
  scored against Block MAGNITUDE's own best-fit correction — applying
  EITHER convention's own c* to its own worst cell flips it above
  threshold. **Both corrected same-shift** (`erratum.py`, `results.json`'s
  new `phase5_erratum` key; original text flagged, not rewritten, per
  T10's precedent) — **T21's contamination-risk question is NOT closed by
  this cycle.** QUANTUM OPTICS also found the coherent cross-check models
  fixed-aperture beamforming, not a real divergent beam's own footprint;
  PHOTONICS found a monotonic per-λ best-fit-scale trend that favors a
  settling-margin explanation over Yee-grid dispersion; MATERIALS found
  the domain it flagged as "different" is actually an exact ×1.5 rescale
  of the same scenario. Verdict: PARTIAL (3 PROMISING, 3 PARTIAL, Red
  Team's adjudication). No Checkpoint criterion fires (caught and
  corrected within the same shift) — but THERMODYNAMICS' own pre-
  registered tripwire stands: a fourth consecutive deferral of docket #7/
  `thermo_sidecar.py` fires criterion 4 without further debate. Full
  record: LOGBOOK.md Iteration 19.
- [done 2026-08-18, panel Iteration 20, cloud panel shift] **exp-043
  docket #7 + `lab/thermo_sidecar.py`** — PHOTONICS' lead (rotation,
  legitimately its slot per Iteration-18 precedent), executing
  THERMODYNAMICS' pre-registered Iteration-19 tripwire (a fourth
  consecutive deferral fires Checkpoint criterion 4 without further
  debate). *Logged retroactively this shift — Phases 1–5 and the erratum
  were run and committed the prior shift but LOGBOOK.md/PLAN.md/
  SESSION_LOG.md were left uncaught-up; see LOGBOOK.md Iteration 20 for
  the full record and the disclosure note.* Two deliverables: **(A)**
  docket #7's witness-parameter sourcing (WebSearch only, WebFetch still
  EGRESS_BLOCKED, T18) — flashlight irradiance-at-45m **FALSIFIED against
  the predicted band, coming in ~46× BELOW this program's own 5-cycle-old
  unsourced ~10⁻³ W/cm² placeholder** (6.58×10⁻⁶ W/cm² central; does not
  move any `REALIZABILITY_MEMO.md` tier), dwell time CONFIRMED (66.7ms
  central), microbolometer NETD sourced for the first time (8.6–100mK,
  matching the program's own 5-cycle-old placeholder almost exactly, now
  genuinely grounded). **(B)** `lab/thermo_sidecar.py` — the ad-hoc,
  actually-THREE-way-inconsistent `thermo_sidecar_analytic` dict promoted
  to one reusable, regime-dispatched module (weak-τ chord model vs.
  established-ratio, a new `iso_xsec_sq` area idealization, kinetics-gated
  ON-endpoint dwell scaling), gated by new trust-suite stage 15 (13/13,
  full bench 54/54). Applied for the first time to the program's own
  flagship absorber and σ(I) ON endpoint with real sourced wattage: every
  OFF-state article and `graded_black_shell` itself read UNDETECTABLE
  (>100× below NETD); the ON endpoint reads UNDETECTABLE too, but only at
  two UNOBTANIUM-tier kinetics boundary hosts, not a realistic one
  (Iteration 21's #1 priority). 6/8 predictions CONFIRMED, 1 PARTIAL, 1
  honest MISS (a provenance gap in an OLD hand-typed number, not the new
  module — anticipated by Red Team's own Phase-2 attack). **Phase 5's most
  severe catch**: VISION's own self-review found a Phase-4 claim that an
  erratum had been written to two other experiments' `results.json` was
  FALSE AS WRITTEN — Red Team ruled this would have fired Checkpoint
  criterion 4 on its own standing instruction had it not been fixed in the
  same close; it was, along with two other Tier-0 fixes (NETD-disclaimer
  propagation, a kinetics-host mischaracterization), so criterion 4 does
  NOT fire. New live thread **T22** opened (the `iso_xsec_sq` area
  convention — provably inert for every ΔT_ss verdict issued, live for
  τ_thermal and future short-dwell scenarios). THERMODYNAMICS' own
  tripwire is retired on process grounds. Verdict: PARTIAL (5 PARTIAL, 1
  PROMISING, Red Team's adjudication). Full record: LOGBOOK.md
  Iteration 20.
- [done 2026-08-18, panel Iteration 21, cloud panel shift] **exp-044 the
  realistic-host ON-endpoint kinetics gate + `REALIZABILITY_MEMO.md`
  Amendment 4 + PHOTONICS' 3λ achromatic check** — MATERIALS' lead
  (rotation), executing Red Team's Iteration-20 top-ranked priority
  (QUANTUM's own native charge). 8/8 predictions CONFIRMED: the σ(I)
  ON-endpoint stays UNDETECTABLE across all 16 real PUBLISHED/PLAUSIBLE-
  tier host/ratio points (worst-case margin 55.8× below NETD); docket #7's
  sourced witness irradiance REVERSES the RSA subclass's own "clears the
  witness estimate" framing (onset now 15.2× ABOVE the sourced central
  irradiance) and widens TPA's OOM gap to 11.2–14.2; the ON-endpoint's own
  σ_abs/σ_ext ratio is flat to 0.45% relative across 450/600/750nm
  (zero-cost, using exp-026's own already-committed 3λ data). **Phase 5
  (six blind seats, unanimous PARTIAL) found the cycle's own
  "Amendment 4" was never actually written into `REALIZABILITY_MEMO.md`**
  (MATERIALS + PHOTONICS, independently) — ruled Checkpoint-4-conditional
  by Red Team, resolved same-shift (written, no tier moves). Also found:
  the Phase-3 T22 idealization sentence over-generalized (true for the
  ceiling, false for `tau_thermal_s` specifically — EM's catch,
  Red-Team-quantified: real corrected relative difference 7.3×10⁻⁸–
  1.3×10⁻⁷, harmless); Red Team's own audit computed the Host-D coupled-ODE
  check (nobody else had) and found a real 1.44–1.50% relative difference,
  outside the clean-pass band though harmless to UNDETECTABLE; a caveat-
  propagation gap (THERMO+VISION) and a citation provenance error
  (QUANTUM), both fixed. THERMODYNAMICS self-imposes an Iteration-22 floor
  (not 23) on its own h_conv/mass_kg re-derivation; QUANTUM OPTICS
  self-imposes a Checkpoint-4 tripwire on a third deferral of its own
  aperture-consistent beam check. Verdict: PARTIAL. No Checkpoint criterion
  fires (contingent on, and satisfied by, the same-shift Amendment-4 fix
  and 7 other mandatory corrections). Full record: LOGBOOK.md Iteration 21.
- [done 2026-08-19, panel Iteration 22, cloud panel shift] **exp-045 the
  intermediate-dwell coupled kinetics-thermal stress sweep +
  h_conv/mass_kg re-derivation + dose-accumulation check** — ELECTROMAGNETISM's
  lead (rotation), executing Red Team's Iteration-21 Tier-1 priorities #1–2
  (Block C, priority #3, deferred at Phase 1 with stated reason, then
  overridden and added at Phase 3 per Red Team's Phase-2 mandatory fix).
  2080-point Block-A sweep (dwell/τ, 0.1×–10× of both time constants, 5
  τ_thermal regimes) **never threatens any UNDETECTABLE verdict** — a
  structurally proven ceiling (Block B's own corrections can only ever
  lower `dt_ss_full`). Block B's from-first-principles `h_conv`/`mass_kg`
  re-derivation (silicon identity, replacing PMMA — whose citation Phase 2
  found fabricated) shipped a real, sign-flipping length-scale-mixing bug
  in its own Phase-1 draft, caught by five blind seats + Red Team before
  any commit and corrected pre-run: the self-consistent headline
  (`dwell/τ_thermal`=21.2×, `w_on`-consistent) is genuinely LESS
  comfortable than the draft's own retracted 126.7× claim, though the
  physics conclusion is unaffected. Block C (population-memory/dose-
  accumulation, Host D) ran for the first time — real but harmless memory
  buildup (ratio 1.005–1.451), and a new closed form
  (`coupled_segment_general`) confirmed the decoupled ΔT proxy used for
  its classification is conservative everywhere tested. **Phase 5 (six
  blind seats + Red Team): PARTIAL** — PHOTONICS+EM independently opened
  new live thread **T23** (the `w_on`-vs-`r_out` length-scale question for
  `h_eff`, genuinely unresolved, elevated to Iteration-23 priority #2);
  VISION caught NOTES.md's own "all eight fixes adopted" claim was
  inaccurate (a 6th-plus recurrence of the program's own fix-docket-
  delivery pattern, caught and fixed same-shift, Checkpoint criterion 4
  does NOT fire). **Hardened rule stated**: QUANTUM's aperture-consistent
  beam check MUST run at Iteration 23 or Checkpoint criterion 4 fires
  automatically, no further debate. Verdict: PARTIAL (MATERIALS' lone
  PROMISING dissent preserved on the record, overridden per established
  precedent). Full record: LOGBOOK.md Iteration 22.
- [done 2026-08-19, panel Iteration 23, cloud panel shift] **exp-046 the
  aperture-consistent single-coherent-mode beam (T21) + T23's mixed
  length-scale regime + dose accumulation on the full exp-038 grid** —
  THERMODYNAMICS' lead (rotation), executing Iteration 22's hardened,
  unconditional Tier-1 #1 (QUANTUM's aperture-consistent beam check MUST
  run this cycle or Checkpoint criterion 4 fires automatically). Built
  `width=w₀/cosθ₀` at the source (a phased-array/leaky-wave picture
  matching `lab/fdtd2d.py`'s actual line-current + phase-ramp steering),
  trust-gating `profile="gauss"` (new suite stage 16) for the first time
  since the engine was built. **The advertised finding was never an
  experimental question**: Red Team's own Phase-2 Attack 2 proved
  exp-042's `beam_divergence_coherent` already synthesises the proposed
  aperture — an algebraic identity, not a physics result — but Phase 5
  found that same identity scoped too broadly by QUANTUM (Red Team's own
  finding, corrected against its own seat): at 9 of 36 cells a grating-lobe
  comb carries 42–68% of the aperture's intensity, not a single mode.
  **A trust-suite-integrity defect was caught and fixed the same shift it
  was created**: the new stage-16 gate scored the engine against a
  physically wrong comparator (independently caught by PHOTONICS and EM at
  Phase 5, sharpened by Red Team with new FDTD runs showing the gate was
  ~17× too loose where calibrated AND would have actively FAILED inside
  the very block it certifies) — repointed same-shift, re-passes at 0.46%.
  Block B (T23) resolved: the mixed regime is bit-identical to the
  `r_out`-consistent regime on the operative axis (τ_thermal has no
  power-length term at all), closing T23's operative question robustly
  while its nominal question (which length is licensed) is closed by
  argument, not measurement — THERMODYNAMICS' own fresh Phase-5 self-review
  found the fill-factor disclosure licensing that argument is itself
  incomplete (a validity-condition gap, Biot number, not yet a verdict
  threat). Block C's dose-accumulation closed form
  (`D/τ_k < ln(21f)`) extended to the full 21-new-point exp-038 grid,
  verified 250/250, vindicating Red Team's own Iteration-15 tempering of
  `REALIZABILITY_MEMO.md` Amendment 3 — Amendment 5 written same-shift.
  **Phase 5 (six blind seats + Red Team): PARTIAL** (5 PARTIAL, 1
  PROMISING — MATERIALS, scoped to its own charter). Four distinct
  instances of this program's own fix-docket-delivery pattern recurred in
  one cycle (an unfalsifiable "eye-invisible" claim surviving unflagged
  with a false "struck everywhere" claim repeated 2672× in `results.json`;
  a disclaimer delivered at 3 of 5 named loci; a Director-level judgment
  call absent from the machine-readable record; a hardened tripwire whose
  own carve-out re-admitted the device it existed to foreclose) — one
  cycle after the SUPERSEDED-banner remedy was invented for the first of
  these. **Checkpoint criterion 4 does NOT fire — conditional on a
  hardened, harder-than-any-prior-cycle same-shift Tier-0 docket (5
  items, of 20 total), all applied and verified this same shift** (suite
  re-confirmed 89/89, commit `c2a21f7`). No other criterion fires. Verdict:
  PARTIAL. Full record: LOGBOOK.md Iteration 23.
- [done 2026-08-19, panel Iteration 24, cloud panel shift] **exp-047 the
  glare/adaptation Tier-W sidecar** — VISION SCIENCE's lead, executing
  Iteration 23's hardened, unconditional tripwire (ran this cycle;
  Checkpoint criterion 4 did not fire). New machinery:
  `lab/glare_sidecar.py` (Stiles–Holladay veiling luminance + CIE
  veiling-contrast dilution, two algebraically cross-checked forms,
  bar-explicit `C_thr(L)`, corneal-irradiance converter), trust-suite
  stage 17 (6 identity gates, 17/17; full fast suite 58/58 throughout).
  **Headline (P-G24-2) CONFIRMED, robustly**: the established
  `graded_black_shell` absorber clears the bench-scale glare-diluted
  SURROGATE of Tier-W (never bare "Tier-W" — Red Team's central
  mandatory fix) under the "tracking" gaze regime at the ceiling
  stray-light estimate, LAB (cued) bar, across the full night-ambient
  band and both p — worst-case margin ~170×, and PHOTONICS' Phase-5
  closed-form bound shows no possible correction to the measured C
  (chromatic, fringe, or realizability-driven) can ever flip it (61×/
  246× margin even at the physical |C|=1.0 ceiling). Two load-bearing
  Phase-2 catches: EM found the original proposal's headline language
  contradicted its own bench-scale-only scope (fixed: every headline
  claim now carries the explicit surrogate label) plus a citation error
  (exp-030 is Iteration 7's close, not Iteration 4); Red Team caught
  (missed by all five blind seats) that Tier-W's cued observer requires
  the LAB bar, not the more lenient uncued FIELD bar, never disambiguated
  originally. **Phase 5 (six blind seats + Red Team): PROMISING** (4
  PROMISING, 2 PARTIAL — MATERIALS/THERMO, each scoped to one open item
  in their own charter, neither finding a defect in the claim itself).
  MATERIALS' major finding: the measured C is drawn from the
  self-similar-scaled `graded_black_shell` construction — the exact
  construction Iteration 7 already names UNOBTANIUM at witness scale; a
  plausibly-realizable fixed-absolute-thickness variant has been proposed
  since Iteration 7 and never built or measured, at any scale (sharper
  than the already-known bench≠witness gap, T8/T13/T14). EM independently
  found the headline grid's own `L_v/L_B` ratio spans ~2.5×10⁴×–2.2×10⁹×,
  far outside the disability-glare literature's typical calibration range
  — doesn't threaten PASS (the dilution formula's washout direction is
  fixed by construction) but tempers how the "170× robust margin" should
  be read. VISION caught a residual bare-"Tier-W" line inside this
  cycle's own NOTES.md Hypothesis section — the same overclaim pattern
  Phase 2 fixed elsewhere, recurring one level down inside the very
  document written to fix it (this program's sharpest instance yet of its
  own named fix-docket-delivery pattern, Iterations 13–23). Five cheap,
  zero-FDTD Phase-5 fixes applied same-shift (label, citation-provenance,
  two new idealization disclosures, ocular-exposure scale anchor); the
  three FDTD/new-experiment items correctly carried to Iteration 25. No
  Checkpoint criterion fires. Full record: LOGBOOK.md Iteration 24.
- **[queued — panel Iteration 25, ranked per Red Team's Iteration-24
  Phase-5 synthesis, lead: VISION SCIENCE (rotation)]** (1) **formal
  `REALIZABILITY_MEMO.md` entry for `graded_black_shell` at witness
  scale** (MATERIALS' finding, now Tier-0) — naming the self-similar-
  construction/evidence-base link explicitly, given exp-047 just
  promoted this article's bench-scale surrogate to headline status. (2)
  **T21 fringe-contamination bound at the actual ±35° fallback geometry**
  (PHOTONICS' finding) — cheap, reuses exp-042's own committed
  propagator, closes the one real gap in exp-047's own evidentiary chord
  without threatening its headline. (3) **Source or retire the
  `[0.5,2.0]` MARGINAL classification band convention** (VISION/QUANTUM,
  independently converged) — not load-bearing for exp-047's headline,
  will be for any future near-boundary grid (two of exp-047's own
  informational points already sit at ratio 0.907–1.085). (4) **Build and
  measure the fixed-absolute-thickness `graded_black_shell` variant's own
  C** (MATERIALS' eight-iteration-deferred Iteration-7 pick, natural
  companion to item 1). (5) **stage-16's forward half**: identity-gate
  Block A's own actual extremes (w₀=1.074λ and 10.74λ — both current
  identity gates sit at w₀≈2λ, and Block A's worst A3 residual and its
  whole low-N_F reach live at the ungated end), ~2 FDTD calls. (6)
  **QUANTUM's n-convergence audit of `gaussian_angle_weights`** (n=41 has
  never been convergence-tested in this program's history; n=401 already
  measured to move scored `C_empty` by up to 4.47% at 450nm/36°/
  FWHM=20°; exp-047's own Phase-5 confirmed zero contamination risk from
  any parallel thread, removing the last reason to keep deferring it) —
  **run this BEFORE** the M²/étendue reframing of T21 it gates (QUANTUM's
  own Phase-5 proposal, Red-Team-adopted: exp-042's two columns are M²=1
  and M²≈2.15–35.8 of the same scene; a crossover measured at M²≈10–20
  against a real flashlight's own M²≈10²–10³ would answer T21's
  contamination question with two sourceable numbers, replacing the
  coherence-length route T21 has been blocked on for four iterations) —
  identity-gate the high-M² endpoint against exp-042's own committed
  `block_beam_corrected` bit-for-bit before any intermediate M² is
  trusted. (7) **session-accumulated ocular dose disposition** (THERMO's
  own scoped-down next step from exp-047 — radiant exposure J/cm² via
  existing dwell figures, comparative order-of-magnitude only, not a
  hazard-standard verdict) — cheap, not urgent. **Tier 2 (moderate
  cost):** design the new **T24 `ABSORB`-systematic sweep** (`SRC_X`
  moved clear of the x-damping band so the confound EM's own two Iteration-
  23 legs exposed does not recur), ~6–9 FDTD calls; the R3 resolution
  check on the four cells where exp-046's own 36-cell grid reads a
  POSITIVE `C_empty` (a sign reversal across the visible band at FWHM=2°,
  contradicting a committed "no wavelength dependence" claim) before
  "glint at 750nm" enters the record as physics, per this program's own
  R3 meta-rule; extend Block C's dose-accumulation check's own duration
  scan interpretation to a genuinely continuous (not 5-point) sweep if
  the n-convergence audit (item 3) reopens any of its inputs; PHOTONICS'
  cheap R3 (cpl×1.5) recheck of exp-044's own 0.45% achromatic-flatness
  claim; the settling-margin FDTD test (now a FIFTH consecutive cycle's
  deferral for its standalone form, though EM's own Iteration-23 legs
  closed it for the two Block-A legs that mattered — see idealization
  11); MATERIALS' N17_NATIVE_V2 resolution-refinement leg (~8–17 new FDTD
  calls). **Tier 3 (standing):** deduplicating `realizability_tier` into
  one shared, imported location instead of two independent copies
  (exp-038, exp-039).
  Deprioritized, carried: a program-wide re-audit of every N17-vs-N9
  citation for exp-042's own obliquity-convention correction (unnecessary —
  a predictor-side artifact of that one analytic bridge); reopening
  `REALIZABILITY_MEMO.md` Amendment 1's own wording (correctable,
  non-urgent, no verdict moves); the staircase-σ(t) validation run
  (Iteration-18's own recommended-once-clear item — still blocked, now a
  SIXTH consecutive cycle's worth of deferral risk if it keeps slipping;
  flag to Marsh at next proposal time per the standing instruction);
  exp-029's coherent-decomposition machinery applied to the θ=38→41° field
  (downstream of the cheaper Tier-1/2 items above); testing whether a real
  σ(I) article damps the fringe (under-motivated by only 2 data points so
  far); a rigorous RSA literature pass (still blocked on the same
  WebFetch/T18 infrastructure gap); T19 (still blocked on T18/WebFetch, ten
  consecutive shift confirmations). **Program-level, flagged for Marsh's
  attention, not a work item**: the fix-docket-delivery pattern (a
  claimed-complete item not fully delivered) has now recurred a SEVENTH-
  PLUS time in nine iterations (13, 14, 15, 17, 20, 21, 22, 23, and now
  24 — this cycle's own sharpest instance, a residual overclaim surviving
  inside the very NOTES.md written to fix Phase 2's original overclaim of
  the same species) — the rate is not decreasing despite Red Team's own
  repeated flags; the mechanical/lint-style enforcement VISION SCIENCE
  proposed at Iteration 15 to catch this class automatically remains
  unadopted, eight iterations later.
  Lower priority, inherited: **Retroactive wavelength-tagging and
  primary-source re-verification** (exp-036's RSA/spiropyran figures,
  exp-037's TPA-cascade/Soref-Bennett figures) — still blocked pending a
  working full-text access route (T18, four consecutive shift
  confirmations); **escalating the WebFetch egress-proxy blockage**
  itself (T18) — still a network-policy matter outside agent control;
  patching the perceptual-scoring cap's enforcement mechanically (VISION
  SCIENCE's own Iteration-15 proposal — a lint-style check or a
  verbatim-reuse rule, rather than another wording patch, given that a
  Phase-3 wording fix demonstrably failed to propagate to Phase 4 this
  cycle); taxonomic homes for ENZ's χ⁽⁵⁾/3-photon-absorption RSA branch
  and the Joshi et al. energy-transfer-coupled dyad (PHOTONICS); the
  carrier-vs-molecular absorption-correction question extended to
  graphene/CNT sub-components (QUANTUM); the intrinsic cross-section-
  ratio-extraction discipline as a mandatory companion to the
  composite-figure search-order fix for any future combined-media check
  (MATERIALS); docket #7's sourced witness-parameter table (flashlight
  irradiance and the 10ms–1s window both still unsourced); QUANTUM's VO2
  absorption-correction category-error fix; THERMO's latent-heat/
  ΔT-quantity fix on promotion to reusable code; N33 at r=78-native and
  the second independently-built r=78-native N17 domain (both
  deprioritized further, still queued); a reproducibility/GUARD_OUT-
  fringe-period sweep testing the near-field-fringe interaction mechanism
  (PHOTONICS/EM); a genuine 3-λ sweep of the N9→N17 angular-convergence
  readings (never run on this channel); T11's own trust-suite stage for
  the ambient/line-source box-ledger channel; T14's PHOTONICS multi-point
  cored-absorber r-sweep (r≈78, 110, 156, 220, 312, fixed PLANE_DX=15,
  θ=0) — still never executed; a genuine PEC r-family ripple test near
  r≈270–350 (T12's own real open half); T11's dedicated multi-point/
  multi-box-pair box_dev floor characterization; Iteration 6's queued
  incoherent-ensemble/phase-quadrature idiom (contingent-only, unopposed);
  a formal reciprocity check (EM's own long-standing pick — now doubly
  relevant given EM's own Iteration-16 lead); the shell-thickness/
  optical-depth economy sweep (MATERIALS); T10's residual +3.05pp
  sub-cell/window-offset sweep; a genuinely continuous (non-step-function)
  Test-B sweep profile for the kinetics kernel (MATERIALS' Iteration-15
  #3 — `integrate_two_state`'s `I_profile` path is currently
  `NotImplementedError`); reconnecting the kernel to its original
  spiropyran empirical anchor at witness-relevant dim/night ambient
  (PHOTONICS/QUANTUM OPTICS, Iteration-15).
- [done 2026-08-19, panel Iteration 24] **docket #7 in full**: the
  witness-scenario parameter table (Iteration 20/exp-043) and the
  glare/adaptation sidecar (Iteration 24/exp-047) are both now closed.
  This item's own original caution — that the WITNESS-scale extrapolation
  the sidecar would score against is exactly what T13 shows is not yet
  trustworthy — was resolved by scoping exp-047's entire headline to the
  bench-scale surrogate explicitly, not by T13 itself closing (T13/T14
  remain open; see exp-047's own record and Iteration-25 queue item 1/2
  above). No Tier-W witness-scale verdict has been published; only a
  labeled bench-scale surrogate result.
- [done 2026-08-19, panel Iteration 25] **exp-048 the evidentiary-chord
  closure: `REALIZABILITY_MEMO.md` Entry 2, T21's real-geometry fringe
  bound, and the MARGINAL band sourced** — VISION SCIENCE's lead,
  executing exp-047's own Iteration-24 ranked queue items 1–3 in one
  desk-only cycle (zero new FDTD calls). **Block A**: formalized, not
  revised, Iteration 7's own informal UNOBTANIUM call for
  `graded_black_shell` at witness scale — real thickness/core-radius
  numbers (0.31–0.92m / 0.19–0.58m at 3 witness radii) computed from the
  self-similar construction's own formulas; a formally-derived σ_max
  reading was explicitly labeled **illustrative-only** after MATERIALS'
  Phase-2 catch (Red-Team-hardened) found the original framing silently
  fed meter-valued input into a grid-normalized FDTD formula with no
  dx/unit bridge — the identical near-field↔witness-scale conflation
  T8/T13/T14 already flagged for C, now caught for σ before it shipped.
  **Block B**: exp-042's own committed T21 edge-diffraction propagator
  re-parameterized to the ACTUAL ±35° fallback geometry the C=−0.7209
  headline anchor uses (not the ±40° geometry T21 was discovered at) —
  5 of 27 points exceed the hard gate, worst 0.004855, explicitly scoped
  as INCONCLUSIVE against live thread T24's own uncharacterized ABSORB
  boundary systematic (PHOTONICS' mandatory fix); does not threaten
  exp-047's headline (P-G24-2), which survives by 61.5×/245.8× under a
  corrected MULTIPLICATIVE worst-case bound (EM's mandatory fix,
  replacing an original additive "headroom 0.28" error). **Block C**:
  `lab/glare_sidecar.py`'s unsourced `[0.5,2.0]` MARGINAL band traced to
  T2's own committed ±0.3-log threshold uncertainty (match to 0.24%),
  regime-checked against exp-047's own three near-boundary points (all
  confirmed in the low-luminance regime that figure is committed for) —
  sourced, zero numeric change. **13 CONFIRMED, 1 PARTIAL** (an honest
  P-B1 miss against a rounded citation, confirmed against a precise
  same-formula comparator — the mechanism transfers correctly), **0
  REFUTED**. **Phase 5 (four PROMISING, two PARTIAL — VISION SCIENCE/
  MATERIALS, both scoped to items adjacent to the headline; Red Team's
  own independent verdict: PROMISING)**: two genuinely new cross-seat
  findings — PHOTONICS and ELECTROMAGNETISM independently caught an
  unreproducible "precisely recomputed" citation in NOTES.md (corrected;
  new standing house rule **R4** adopted, LOGBOOK.md); MATERIALS offered
  to render the tier call Entry 2 deferred (UNOBTANIUM-WITH-PARAMETERS),
  which Red Team declined as inconsistent with this memo's own
  literature-check standard. No Checkpoint criterion fires — flagged as
  a **third consecutive cycle** (23, 24, 25) of this program's own named
  fix-docket-delivery pattern, all caught and corrected same-shift. Full
  record: LOGBOOK.md Iteration 25.
- [done 2026-08-20, panel Iteration 26] **exp-049 the
  `gaussian_angle_weights` n-convergence audit** — PHOTONICS' lead
  (rotation), executing Iteration 25's own non-negotiable item (1). Zero
  new FDTD calls: a desk-only geometric n-doubling sweep (41→5121, plus
  n=401) of all three committed `beam_divergence_*` functions at
  exp-042/046's own 36-cell grid. **Headline CONFIRMED**: n=41 is
  genuinely under-converged for the coherent function at FWHM=20°
  (8/9 cells; worst-cell move 4.4747%, matching exp-046's own 4.473%
  citation to 0.1%) — exp-046's restored A4 mechanism is real, not a
  fluke. Secondary story lands softer than predicted: the T21-period/
  Nyquist analogy predicts the right direction but not a reliable
  per-cell ranking (Spearman ρ=0.45–0.48, all three functions, PARTIAL);
  FWHM=10° turns out to be **universally, cleanly converged at n=41**
  (100% of 81 cell-function combinations, not merely ≥70% as predicted) —
  the "genuinely open regime" prior was REFUTED. **The global maximum n\*
  anywhere in the entire 108-cell-function grid is 81** — n=41 is safe
  for 100/108 combinations at this geometry. 8 CONFIRMED, 2 PARTIAL,
  1 REFUTED. Two self-caught defects, both instances of R4's own named
  species one cycle after its adoption: a sign-convention bug in the
  scoring script (caught by the Director before Phase 5, both buggy and
  corrected values preserved) and, caught independently by two Phase-5
  seats (PHOTONICS, THERMODYNAMICS), a fabricated "n\*=321" figure in the
  write-up (true max is 81) plus a `results.json`/`run.py`
  reproducibility gap — both fixed same-shift; Red Team's audit found the
  fabricated figure had already propagated into two other seats' own
  review documents before catching it. **Checkpoint criterion 4 does NOT
  fire** (contingent on the applied same-shift fixes) but a new hardened
  rule is adopted: a **third** consecutive post-R4 non-reproducing
  headline figure fires criterion 4 automatically, no further debate —
  this cycle is the second such instance. No REALIZABILITY_MEMO.md tier
  or constraint-3/4 claim touched anywhere. Verdict: PROMISING. Full
  record: LOGBOOK.md Iteration 26.
- [done 2026-08-20, panel Iteration 27] **exp-050 the n-convergence audit
  at exp-048's A=724 fallback geometry** — MATERIALS' lead (rotation),
  executing Red Team's Iteration-26 Phase-5 ranked #1 item and MATERIALS'
  own Phase-2 Attack-1 follow-up trigger on exp-049. Zero new FDTD calls:
  generalized exp-042's three `beam_divergence_*` functions to take a
  geometry dict (exp-048 Block B precedent), with a mandatory regression
  anchor against `GEOM_EXP042_OLD` — bit-exact (0.0 relative error) for
  all three functions, including the first-ever geometry-dict
  generalization of the obliquity-on-E convention. **Headline CONFIRMED
  cleanly: global max n\* at GEOM78 stays 81, matching A=752 exactly
  (P-NCONV27-1); 100% of FWHM≤10° cells converge at n=41 (P-NCONV27-5)**
  — closes the follow-up trigger's own literal purpose: no future
  near-boundary citation at GEOM78 needs to defer to a re-run outside the
  FWHM=20°/`incoherent_corrected`-or-`coherent` regime. **But
  P-NCONV27-2 REFUTED, informatively**: Red Team's own pre-registered
  6-combination exemption zone (built from two independent mechanisms,
  Phase 2) caught the one violation it predicted (750nm/40°) but missed
  two more at 600nm (36°, 40°), same function, outside the zone — all
  three violating cells sit deep in the `|C|`~10⁻⁴ "exempted" near-zero
  regime. Six blind Phase-5 seats split 3 PROMISING / 1 PROMISING-with-
  a-ruled-out-sub-claim (QUANTUM) / 2 PARTIAL; PHOTONICS proposed a
  specific mechanism (the corrected convention's signed cross-term is
  uniquely prone to near-zero crossings) that QUANTUM and EM
  independently refuted by re-running `incoherent` at the same
  coordinates and finding the identical pathology. **Red Team's own
  audit resolved this by direct execution, not seat-counting**: both
  conventions share a genuine, fast-settling destructive-interference
  null of the same angular integral; which one trips the fixed
  `ABS_TOL` gate is a reproducible ~1.9–2.3× magnitude coincidence,
  unexplained — Iteration 28's own top priority. Two further real,
  same-shift-fixed disclosure gaps: THERMODYNAMICS found the disclosed
  runtime (~104min) likely excludes a discarded, comparably-expensive
  buggy first run (true cost ~208min, git-timestamp-confirmed,
  non-load-bearing); VISION SCIENCE independently found the sharpest-
  stakes cell's immediate 2°-step angular neighbors at GEOM78 actually
  **exceed `C_THR` outright** — a threshold breach absent at A=752,
  undisclosed until Phase 5. **No Checkpoint criterion fires** (all five
  explicitly checked; criterion 4 scrutinized directly against both
  PARTIAL findings, does not fire). **No new numbered live thread** —
  folded into T21's existing entry (same underlying fringe mechanism,
  now shown to also govern `beam_divergence_*`'s integrated quantity at
  a second geometry). New standing rule adopted: n-convergence CONFIRMED
  certifies numerical stability only, never geometry-stability of the
  underlying physical value. Verdict: PROMISING. Full record: LOGBOOK.md
  Iteration 27.
- [done 2026-08-20, panel Iteration 28, cloud panel shift] **exp-051 the
  alias-lattice difficulty predictor, tested out-of-sample** —
  ELECTROMAGNETISM's lead (rotation), executing Red Team's Iteration-27
  ranked #1 item. **The cycle's own Phase-1 design was killed at the desk
  by four independent blind seats before any run** — PHOTONICS, MATERIALS,
  QUANTUM OPTICS and Red Team each rebuilt its machinery from its prose and
  scored AUC(|offset|)=0.649 against its own 0.85 CONFIRMED bar, with a
  zero-information convention-identity baseline (AUC 0.792) beating it; the
  fringe's zero-crossings do not recur at `P` (gaps 0.137–1.279·P), so the
  proposed quantity was never a phase (now **R5** in LOGBOOK's ruled-out
  registry). **QUANTUM OPTICS proposed the replacement mid-cycle and Red
  Team independently rebuilt it cold**: the residual is the Poisson-alias
  term referenced to the quadrature **node lattice** `h`, not the fringe
  period — AUC 1.0000, r=0.999998 in-sample. **Director override at Phase
  3, the cycle's most consequential call:** since those 18 rows had been
  pre-computed twice during Phase 2, scoring them would have been
  transcription, so they became an unscored calibration set and **all eight
  predictions moved out-of-sample onto 198 untouched combinations** (22
  unstable / 176 stable; two geometries, three functions, four beam widths;
  unfitted thresholds; labels committed by exp-049/050). **Result: 5
  CONFIRMED, 2 PARTIAL, 1 REFUTED, 0 hard-falsified** — zero false
  positives across 81 well-sampled controls (P-ALIAS-3), clean transfer to
  the untouched A=752 geometry (P-ALIAS-4, accuracy 0.954), 94.95% exact
  `n*` prediction (P-ALIAS-7), and **exp-050's ~1.9–2.3× convention
  asymmetry closed** as the spectral-amplitude ratio at the alias frequency
  (P-ALIAS-5, ρ=0.933, median 1.920 vs measured 1.921). **All 10
  out-of-sample misses are `beam_divergence_coherent` rows** — a located,
  not diffuse, boundary: its complex-field sum structurally negates the
  exact sampling identity the model rests on, and its n=41 error is
  dominated by grating-lobe leakage, **the same mechanism exp-046/T24
  already quantified** but never connected to this residual until QUANTUM's
  Phase-5 review (a linearized cross-term fix was tested and falsified:
  0.1–48%, non-perturbative). Phase 5: **unanimous PROMISING, 6-for-6
  blind seats**, Red Team affirms. Two real narrative defects, each caught
  by multiple independent seats, both fixed same-shift: a P-ALIAS-5
  inversion misattribution (PHOTONICS + MATERIALS — the inversion is a
  calibration-set fact at the *other* geometry) and an "executed twice"
  cost claim (THERMODYNAMICS; `timing.json` records one process, "278s" was
  that run's own stage mark). **No Checkpoint criterion fires** (all five
  checked; criterion 4 scrutinized directly against both defects). Verdict:
  PROMISING. Full record: LOGBOOK.md Iteration 28.
- [done 2026-08-20, panel Iteration 29, cloud panel shift] **exp-052 the
  fixed-absolute-thickness `graded_black_shell` variant's own `C`** —
  executed PLAN.md's 21-iteration-deferred unconditional Iteration-29
  trigger (MATERIALS' item, first queued Iteration 7). Built `r_in(r_out)=
  r_out−48` (fixed absolute shell thickness, `sigma_max=0.5` held fixed,
  not rescaled), PEC-cored per a Red Team Phase-2 catch (exp-030's own
  reused comparator construction was silently HOLLOW — the exact defect
  exp-031 fixed for a different diagnostic, never propagated back), and a
  re-measured (also PEC-cored) self-similar comparator, 56 new FDTD calls.
  **Result: the fixed-absolute family DEEPENS monotonically and
  substantially toward −1** (C: −0.72087→−0.80668→−0.84032 at
  r=78/156/312, 600nm) **— the OPPOSITE of T13/T14's established
  wrong-direction shallowing** — while the re-measured self-similar
  comparator reproduces T14's own shallowing almost exactly
  (−0.72087→−0.73046→−0.73225, matching exp-030's own hollow-core figures
  to 4–5 significant digits — the core-fill correction changed nothing for
  THAT family either). All 5 scored predictions (P-0 through P-5)
  CONFIRMED, 0 PARTIAL, 0 REFUTED, margins 17–21× their required
  thresholds — the cleanest prediction sweep in this program's history by
  that count. The construction that was already the more realizable ask
  (1.44µm fixed absolute thickness vs. the self-similar family's
  0.31–0.92m witness-scale divergence) is now also shown to be optically
  better at scale — `REALIZABILITY_MEMO.md` Entry 2's nine-iteration "Open"
  line is CLOSED. **But two independent Phase-5 findings (PHOTONICS,
  ELECTROMAGNETISM), Red-Team-verified, show T14's puzzle is RELOCATED, not
  resolved**: the deepening rate decelerates (residual ratio 0.69 then
  0.83, short of the naive 1/r halving); a same-shift sqrt-law fit gives
  C_∞≈−0.87 to −0.88, still short of −1 by 0.12–0.16 — no formally
  committed `C(z/z_R)` extrapolation exists yet for this family (T8's own
  standing requirement). **A third finding (QUANTUM OPTICS) opens new live
  thread T25, program-wide, not exp-052-local**: the coherent-vs-incoherent
  ambient-sum bridge gate has never empirically validated the actual
  equal-amplitude N9 configuration `lab/ambient.py` uses, at ANY geometry
  this program has run in 29 iterations — exp-029's own gate tested a
  structurally different, asymmetric weak-probe configuration. **A fourth
  finding (THERMODYNAMICS): the Phase-1 proposal's own original P-5 (a
  THERMO energy sidecar) was silently overwritten at Phase 3 by an
  unrelated core-fill check reusing the same label** — an entire
  deliverable never computed, not a drifted number; caught by no Phase-2
  seat, no Phase-3 synthesis, no Phase-4 fit — only a fresh Phase-5
  THERMODYNAMICS instance, reading the record cold. Both gaps disclosed in
  `NOTES.md` and LOGBOOK.md's Iteration 29 entry with two new binding
  Checkpoint-4 tripwires; neither fires this cycle (both caught and
  disclosed before close, per this program's own established practice).
  All five Checkpoint criteria checked explicitly: none fire. **Standing-
  bar flag**: this cycle is THERMODYNAMICS' own `h_eff` re-derivation's
  fifth consecutive deferral (25–29) — per this program's own prior ruling,
  automatically LOCKED to Iteration 31, below, not re-ranked. Verdict:
  PROMISING. Next lead per rotation: QUANTUM OPTICS. Full record:
  LOGBOOK.md Iteration 29.
- **[LOCKED — panel Iteration 30, UNCONDITIONAL — BLOCKED this shift,
  2026-08-21, see note below]** **Build the stage-10
  temporal instrument** — the joint constraint-3/4 staircase-σ(t)
  validation run composing exp-038's kinetics `n(t)`, exp-039's timing
  classification, and exp-040's amplitude bridge against `C_thr(L)` in one
  scored transient, per Iteration 18's own never-retired design. Granted an
  unconditional trigger by Red Team at Iteration 28 Phase 5 on VISION
  SCIENCE's request: a **27-iteration span** (first ranked Iteration 1,
  last ranked Iteration 18, then **silently dropped from every ranked list
  for 10 consecutive iterations, 19–28**) — longer than the bar just
  applied to `graded_black_shell`, with a worse failure mode (it stopped
  competing at all). T3's joint constraint-3/4 verdict still does not
  exist; PANEL.md's own metrics table has named this instrument, unbuilt,
  since Iteration 1. **Unconditional, not subject to further ranked-list
  competition.**
  **BLOCKER (2026-08-21, cloud panel shift, pre-Phase-1):** the fresh
  QUANTUM OPTICS Phase-1 sub-agent dispatched to propose this build was
  terminated mid-read (before writing anything — `experiments/053-.../`
  was never created with content, cleaned up) by an upstream API-level
  content-policy block tagged `[bio]`, message "Sonnet 5 can't help with
  this... Start a new session to continue" (Acceptable Use Policy link
  attached). The agent had only reached the file-reading stage (LOGBOOK.md,
  PANEL.md, the exp-038/039/040 record) — no cause is visible in this
  shift's own record; the Director's own read of the same material found
  nothing bio-related (it is 2D-FDTD photonics: rate-equation kinetics for
  a switched absorber, temporal-CSF vision thresholds, irradiance/dynamic-
  range realizability figures — no biological, chemical, or weapons content
  by any plain reading). Possible false-positive on the kinetics/dose/
  irradiance vocabulary (`n(t)`, "dose accumulation," "carrier lifetime,"
  NETD thermal-detectability figures) pattern-matching a dual-use-research
  classifier. **Not retried this shift** — a repeated or reworded attempt
  to push the same request through risks looking like evasion of a safety
  control rather than a legitimate retry, and the Director has no way to
  confirm from inside the session whether the block is transient or
  content-tied. Marsh notified out-of-band. Iteration 30 stays LOCKED and
  UNCONDITIONAL; a future shift (or Marsh, in a live session) should
  attempt Phase 1 again, ideally starting fresh rather than resuming this
  blocked thread, and report back here whether the block reproduces.
  **BLOCK REPRODUCES (2026-08-21, second cloud panel shift, pre-Phase-1):**
  a second, independent, fully-fresh QUANTUM OPTICS Phase-1 sub-agent
  (new session, no memory of the first attempt) was dispatched with the
  identical task, unreworded. It was terminated by the same upstream
  content-policy block, same `[bio]` tag, same "start a new session"
  message, again mid-file-read (its last visible step: reading
  `design_geometry.py`/`fdtd2d.py` after LOGBOOK.md and the kinetics
  module) — no experiment-directory content was written either time.
  **This is now a confirmed, content-tied, reproducible block, not a
  transient one** — two independent fresh sessions given the same
  reading list (kinetics rate-equation code/prose, "population
  fraction," "dose," "carrier lifetime" vocabulary) both failed at the
  same stage. **Per the prior shift's own stated reasoning, a third
  attempt at this exact task — reworded or not — would risk reading as
  evasion of a safety control and was not made.** Director instead used
  the remainder of this shift to attempt panel Iteration 31 (a different
  topic, thermal heat-transfer physics, no kinetics/rate-equation
  vocabulary) as a diagnostic: does the block generalize to this
  program's whole vocabulary, or is it specific to the staircase-σ(t)
  build's own reading list? Result recorded in that entry, below.
  Iteration 30 stays LOCKED and UNCONDITIONAL, now flagged for Marsh's
  direct attention (out-of-band + this shift's notification): the
  routine cannot execute PANEL.md's own longest-standing mandatory
  instrument build without human intervention (e.g. a differently-scoped
  prompt, a different tool/session, or Marsh's own live-session attempt).
- [done 2026-08-21, panel Iteration 31, cloud panel shift] **exp-054 the
  `h_eff` length-scale re-derivation** — THERMODYNAMICS' own five-cycle-
  deferred, LOCKED/UNCONDITIONAL trigger, executed this shift (rotation
  broken for the pre-planned override, per the entry this bullet
  replaces). Formally resolved which characteristic length licenses
  `h_eff=k_air/L`: `h_eff`/mass/area on `r_out` (the object's real
  geometric length), `P_abs` stays on `w_on` (the calibrated optical
  measurement) — mixed by design, promoted to reusable, trust-suite-gated
  code (`lab/thermo_sidecar.py`, new stage 18). Applied to exp-043's
  ON-endpoint and exp-045's dose-accumulation article: **all 8
  pre-registered predictions CONFIRMED**, both stay UNDETECTABLE, full
  bench 114/114 (heavy stage 5 excluded). Two Phase-5 findings, both
  Red-Team-elevated: (1) the corrected margins are ~3× SMALLER than the
  standing figures they replace (607×/8,955× vs. 1,839×/27,080×), not
  larger — a same-shift disclosure fix, not a numeric problem; (2) this
  program's own flagship article, `graded_black_shell_flagship`, sits at
  the THINNEST thermal margin in the entire record (~6.04×) and still
  uses the now-twice-repudiated old chain, uncaught by stage 18 (a
  structural property — stage 18 gates only the two call sites this cycle
  touched) — **ranked #1 for Iteration 32+**, not fixed this cycle
  (correctly out of scope). No Checkpoint criterion fires (criterion 4
  scrutinized hardest — nearest miss, does not fire). Verdict: PROMISING.
  Full record: `experiments/054-heff-length-scale-rederivation/` —
  Phase-1 proposal, five Phase-2 blind critiques, Phase-2 Red Team audit,
  Phase-3 synthesis, NOTES.md, run.py, results.json, six Phase-5 blind
  reviews, Phase-5 Red Team audit. LOGBOOK.md Iteration 31.
- [done 2026-08-21, panel Iteration 32, cloud panel shift] **exp-055 the
  T25 coherent-vs-incoherent ambient-sum bridge gate, N=9 equal-amplitude**
  — QUANTUM OPTICS' lead (rotation, "still owed" per Iteration 31's own
  closing line), executing its own five-cycle-deferred T25 catch: built the
  real bridge gate against the actual equal-amplitude N=9 `FALLBACK_ANGLES`
  configuration every constraint-3 `C` citation rests on (new suite stage
  19, N=2→N=9 extension of stage 11's field-identity gates + a new
  absorbed-power closure gate), not exp-029's own structurally different
  N=2 amplitude-asymmetric proxy. Red Team's Phase-2 audit caught a
  load-bearing defect (the proposal's object was hollow, not the PEC-cored
  construction `C78_ESTABLISHED` actually rests on) and the Director's own
  Phase-3 catch found the proposal's cited anchor was a 3λ photopic-weighted
  average, not the correct single-λ=600nm figure — both fixed pre-run. 20
  new FDTD calls. **Result: good news for every existing headline `C`**
  (the loaded PEC-cored absorber's coherent-vs-incoherent deviation is
  small — raw flux −0.885%, Weber `C` shift 0.317% absolute, none of this
  program's citations ever used coherent injection so none are touched) —
  **but a striking new finding, live thread T26**: the EMPTY (vacuum) scene
  shows naive incoherent `C_empty≈0` vs. coherent N=9 joint-injection
  `C_empty=−0.0534`, over 10× VISION's own T2 photopic `C_thr`, from
  interference alone. Not a bug (Red-Team-confirmed as ordinary
  passivity-bounded multi-beam interference, EM's independently re-derived
  Cauchy-Schwarz ceiling), poses zero retroactive risk to any existing
  citation, but a real prospective risk for any future near-null σ(I)
  proposal that might substitute coherent injection for the incoherent
  pipeline. One suite gate (the new closure check) genuinely missed its
  reused tolerance at first run (2.887% vs ≤1.5%), an R3 check found it
  only partly a grid artifact, and the gate was recalibrated to ≤3.5% with
  full disclosure — feeding standing thread T11. **Phase 5: 3 PROMISING
  (MATERIALS, ELECTROMAGNETISM, QUANTUM OPTICS), 3 PARTIAL (PHOTONICS,
  THERMODYNAMICS, VISION SCIENCE) — Red Team's audit adopted PROMISING
  over the raw split**, per this program's own established precedent
  (Iterations 10/12). One mandatory same-shift fix applied (VISION's T2
  photopic-regime qualifier, previously stated unqualified). No Checkpoint
  criterion fires. **T25 itself stays open** — this cycle measures one
  fixed-relative-phase coherent realization, not the true random-phase
  incoherent ensemble; QUANTUM OPTICS' own Phase-5 sharpening: the
  incoherent sum is provably the analytic zero-mean of that ensemble
  (Iteration 6), so what remains open is the ensemble's VARIANCE, and T26
  is existence-proof it is not negligible in at least one channel. Verdict:
  PROMISING. Next lead per rotation: VISION SCIENCE (completes the
  rotation's second full cycle). Full record:
  `experiments/055-t25-coherent-ambient-bridge-gate/` — Phase-1 proposal,
  five Phase-2 blind critiques, Phase-2 Red Team audit, Phase-3 synthesis,
  NOTES.md, run.py, results.json, six Phase-5 blind reviews, Phase-5 Red
  Team audit. LOGBOOK.md Iteration 32.
- [done 2026-08-22, panel Iteration 33, cloud panel shift] **exp-056 the
  T26 near-null generalization test** — VISION SCIENCE's lead (rotation,
  completing the rotation's second full cycle), executing Iteration 32's
  own Red-Team-ranked #1 combined build. `off_pass`/`off_bracket`
  (τ=0.0065/0.003, exp-032) both loaded via fixed-zero-relative-phase N=9
  coherent joint injection, native r=78/cpl=20 + a rescaled r=117/cpl=30
  R3 leg on the empty-scene channel — 3 new FDTD calls. Red Team's Phase-2
  audit: 6 attacks, 7-item docket, 6 accepted + 1 (PHOTONICS' phantom-disk
  control) implemented differently at zero cost (Director's own catch:
  σ=0/ε_r=1 is physically identical to vacuum, so the established
  empty_joint reading IS that control point for free — a genuine 3-point
  τ∈{0,0.003,0.0065} curve at no extra cost). **Result: every scored
  prediction CONFIRMED — the T26 artifact generalizes, and the mechanism
  is sharpened.** `off_pass`/`off_bracket` both show the coherent-injection
  idiom's `|C_joint|` at 11.1–11.6× VISION's own T2 photopic `C_thr`
  (widening to 10.2–12.7× under a window-position sensitivity scan),
  refuting exp-055's own suppression hypothesis (the curve grows, not
  shrinks, with τ) and closely tracking QUANTUM's own Born-linear-
  perturbation model (1.2%/2.4% relative miss, independently re-derived by
  five of six Phase-5 seats plus Red Team — a fifth confirmation each).
  Four of six Phase-5 seats independently, unprompted, found the same
  corroborating cross-check (`p_abs_joint` scales with τ to 0.13–0.14%).
  R3 (P-VIS-3) and window-position (P-VIS-4) checks both CONFIRMED — T26
  is genuine interference physics, only modestly resolution/placement-
  sensitive. **No existing Tier-W/Tier-A constraint-3 verdict moves** (no
  citation has ever used coherent injection). Phase 5: **unanimous
  PROMISING, 6-for-6** — the program's second unanimous panel-era verdict
  (after Iteration 11's unanimous PARTIAL) — Red Team adopting the raw
  seat count without override. **New gap found this cycle** (EM, QUANTUM,
  Red-Team-confirmed): R3 was run only on the empty scene, never on the
  loaded legs the headline figures themselves come from — Iteration 34's
  #2 competitive priority. Four mandatory same-shift fixes applied
  (headline reordering to lead with the instrument-substitution-artifact
  framing; the "10–13×" figure decomposed rather than blended; the
  ambient-light-analog caveat propagated to ALL disposition branches, not
  only the CONFIRMED one; a new binding tripwire on the THERMO sidecar's
  scope-down). **`graded_black_shell_flagship`'s third deferral (ranked #1
  at Iteration 31's close, deferred at 32 and again this cycle) triggers
  the unconditional-lock bar Red Team itself pre-declared, in writing, at
  Iteration 32's close — GRANTED, LOCKED for Iteration 34, breaking
  rotation.** QUANTUM's own phase-variance redesign (deferred once this
  cycle, correctly scoped out as genuine new machinery) is pre-registered
  for a 2nd-deferral unconditional lock at Iteration 35 if not built at
  Iteration 34. No Checkpoint criterion fires (criterion 4 scrutinized
  hardest against the headline-ordering/"10–13×" findings — ruled the same
  same-shift-fixable documentation-gap class this program has repeatedly
  and correctly ruled non-firing; criterion 5 ruled explicitly not to
  apply). Verdict: PROMISING. Full record:
  `experiments/056-t26-near-null-generalization/` — Phase-1 proposal, five
  Phase-2 blind critiques, Phase-2 Red Team audit, Phase-3 synthesis,
  NOTES.md, design_geometry.py, run.py, results.json, six Phase-5 blind
  reviews, Phase-5 Red Team audit. LOGBOOK.md Iteration 33.
- [done 2026-08-22, panel Iteration 34, cloud panel shift] **exp-057
  closing the flagship's `H_CONV`/`MASS_KG`/`w_on`-area gap** —
  THERMODYNAMICS' lead, by UNCONDITIONAL LOCK breaking rotation (Red
  Team's Iteration-33 escalation ruling, executed). Zero new FDTD:
  `graded_black_shell_flagship`'s thermal margin, corrected through
  `mixed_length_scale_regime`, corrects from **6.04× to 699.27×**
  (UNDETECTABLE by a wide margin) — **~116× LARGER**, the OPPOSITE
  direction from exp-054's own ~3.03× shrink, because the flagship never
  had `H_CONV` corrected even once. Mechanism code-verified (not
  hand-typed): the radiative term's share of `dP/dT` collapses from
  co-equal-with-`H_CONV` (50.70%) to negligible (0.046%) once the
  physically-derived `h_eff≈11,111 W/m²K` swamps it — the Phase-1 draft's
  own naive two-factor story (`~235×`) was wrong even though its final
  number (`~116×`) was right, caught by EM's Phase-2 critique. Phase 5:
  **unanimous PROMISING, 6-for-6** — the program's third unanimous
  panel-era verdict — with six mandatory same-shift fixes (two citation
  errors — a wrong-file citation for the shell construction, and the
  silicon-provenance chain wrongly attributed to Iteration 20 rather than
  exp-045/046; a diffraction-inflation bound corrected from `~1.5–2×` to
  the correctly-derived `~2.37×`; a `Q_ext(x)` cycle-count reconciliation;
  full NETD-disclaimer propagation, closing an exact recurrence of an
  Iteration-31 finding). **Two new unconditional LOCKs fired at this
  cycle's own Phase-5 close** (below). No Checkpoint criterion fires.
  Verdict: PROMISING. Full record:
  `experiments/057-graded-black-shell-flagship-mixed-regime/` — Phase-1
  proposal, five Phase-2 blind critiques, Phase-2 Red Team audit, Phase-3
  synthesis, NOTES.md, run.py, results.json, six Phase-5 blind reviews,
  Phase-5 Red Team audit. LOGBOOK.md Iteration 34.
- [done 2026-08-22, panel Iteration 35, cloud panel shift] **exp-058
  QUANTUM's phase-variance redesign** — LOCKED, unconditional, breaking
  rotation (Iteration 33's pre-registered condition, fired at Iteration
  34's close). Built: `Sim.add_line_source(rel_phase=...)`, the new
  `lab/phase_lines.py` disk-persisted per-angle complex-`Ez`/`Hy`-line
  module, trust-suite stage 20 (Q7/Q8/Q9). Measured: N=2000 genuine
  random-relative-phase draws per article (`off_pass`/`off_bracket`) —
  T25's variance question CLOSES. `C(δ)` is heavy-tailed/mean-unstable
  (Weber `C` is an unbounded ratio, per EM's own Iteration-32 finding,
  now empirically confirmed at scale), but the underlying FLUX means
  (`b_obj`, `b_flank`) track the naive-incoherent anchor to <0.7%
  relative error — QUANTUM's own Iteration-6 zero-mean-cross-term
  theorem, re-derived N=2→N=9 and confirmed at the real instrument for
  the first time. The established δ=0 point (cited since Iteration 33)
  is MILDER than 80% of random draws (percentile rank 19.6%/18.75%) — an
  understatement, not an outlier; 98.7%/98.35% of draws exceed `C_thr`.
  No Tier-W/Tier-A verdict moves. Phase 5: **5 PROMISING/1 PARTIAL**
  (VISION SCIENCE) — Red Team's final audit OVERRODE the PARTIAL to
  PROMISING (same-shift-fixable documentation-gap class, direct
  Iteration-33 precedent), with a new binding tripwire: a further
  recurrence of the caveat-placement pattern is a retroactive
  Checkpoint-4 trigger. **Nine mandatory same-shift fixes applied**,
  all from data already on disk, zero new FDTD: a real sign-convention
  bug in `flux_from_lines` (found independently by two Phase-5 seats,
  proven mathematically inert on every number this cycle reported, fixed
  + closed with a new stage-20 gate); a backwards causal-direction error
  on the absorbed-power finding (constructive, not destructive); a false
  mechanism phrase; a ~77×-inflated coherence-length arithmetic error;
  an incomplete same-cycle caveat-placement promise; a minor citation
  slip; the raw `b_obj`/`b_flank` draws (previously discarded) now
  persisted; two new `VALIDATION.md` measurement-lesson entries. No
  Checkpoint criterion fires. Verdict: PROMISING. Full record:
  `experiments/058-t25-phase-variance-redesign/` — Phase-1 proposal,
  five Phase-2 blind critiques, Phase-2 Red Team audit, Phase-3
  synthesis, NOTES.md, design_geometry.py, run.py, results.json,
  `recompute_flux_signs.py`, `sign_fix_verification.json`, six Phase-5
  blind reviews, Phase-5 Red Team audit. LOGBOOK.md Iteration 35.
- [done 2026-08-22, panel Iteration 36, cloud panel shift] **exp-059 the
  LOCKED `Q_ext(x)` closed-form cylinder/disk check** — PHOTONICS' lead
  (by LOCK, Red Team's Iteration-34 ruling after 3 deferrals, this
  program's lowest-ever lock-trigger count, and by rotation coincidence).
  New module `lab/qext_theory.py` — the exact PEC-infinite-cylinder
  Bessel/Hankel partial-wave `Q_ext(x)` series, TM_z, zero new FDTD,
  trust-suite stage 21 (4 gates + regression anchor). **Result:** the
  flagship's measured `Q_ext=1.5385` sits at **72.6%** of the exact
  PEC-sharp-edge reference `Q_ext_PEC(ka=24.5044)=2.1177` — bounds, for
  the first time since Iteration 31, `w_on`'s diffraction-inflation
  assumption inside a physically sane envelope. **Does NOT change any
  scored thermal margin** (369×–1655× clear of NETD-lo either way,
  THERMODYNAMICS' own code-verified sensitivity check) and does NOT
  resolve the separate, still-open `iso_xsec_sq` squaring-convention
  question. Phase 2: five blind support-with-changes + Red Team
  (PROCEED-WITH-MANDATORY-FIXES, 6-item docket, plus its own new
  load-bearing finding — an empirical cross-check against already-
  committed bare-PEC FDTD data, 2.32% max deviation, the real answer to
  a gate-1 self-test tautology two seats independently caught). **Phase
  5: 4 PROMISING / 2 PARTIAL** — Red Team's audit found Checkpoint
  criterion 4 FIRES (two independent within-cycle recurrences of the
  caveat-placement pattern Iteration 35 pre-declared a tripwire on),
  **overriding the raw 4-2 count to PARTIAL**, provisional-to-PROMISING
  once three same-shift Tier-1 doc fixes landed (they did, re-verified,
  bench 67/67 green). CHECKPOINT entry filed (see Current-state note
  above); Marsh notified; Iteration 37 proceeds unblocked per Red Team's
  own explicit ruling. exp-057's own separate, self-contradictory
  "~295×" arithmetic error (THERMODYNAMICS' new Phase-5 catch) queued as
  a zero-cost Iteration-37 rider, not part of this cycle's docket.
  Verdict: PARTIAL (provisional-to-PROMISING). Full record:
  `experiments/059-qext-x-cylinder-disk-check/`, LOGBOOK.md Iteration 36.
- **[queued — ranked for Iteration 37+, per Red Team's Iteration-36
  Phase-5 reconciliation of all six seats — a rare six-way convergence
  on item 1, exp-059 — CURRENT top-of-queue, supersedes the list below as
  the active ranking, retained as valid backlog, not deleted]** (1) **The
  sharp-uniformly-lossy-disk FDTD control run** — all six Phase-5 seats
  named this in their top-3, five as #1; disentangles "edge grading
  reduces diffraction" from "any bulk loss damps PEC's resonance
  ripple," directly resolving MATERIALS' own PARTIAL-driving concern
  (MF-5) — cheap, one new scene, reuses `materials.pec_disk` at
  `R_COAT` with uniform non-graded sigma matched to the shell's own
  optical depth. (2) **The exp-057 erratum fix** — three string edits
  (`NOTES.md`/`run.py`/`results.json`), zero new FDTD, corrects the
  self-contradictory "~295×" figure to the code-verified 1655.18×,
  execute as a zero-cost rider before Iteration 37's own proposal work.
  (3) **Build the mechanical caveat-propagation-check tool** Red Team
  authorized at Iteration 36's Checkpoint-4 ruling — grep every
  mandatory-fix caveat's own key phrase across every file touched by
  that fix's cited sites, not just the sites the fix draft names by
  hand; a sixth hand-applied wording patch would not distinguish this
  closure from the ones that already preceded and failed to hold. (4)
  **MATERIALS' absorptivity/mechanism literature check** — now SEVEN
  cycles deferred (Iteration 29→36), approaching this program's own
  escalation pattern; pin it to one checkable question before an eighth
  deferral forces an unconditional lock. (5) **EM's TE_z companion
  series** for `qext_theory.py` — mechanical, zero new FDTD, would let
  gate 1's polarization-agnostic tautology claim be numerically
  demonstrated rather than argued, and resolves the Hankel-choice
  (`H^(1)` vs `H^(2)`) documentation gap EM's own Phase-5 review flagged.
  (6) **PHOTONICS' T26 λ/angle generalization** (oblique-incidence
  `Q_ext` extension, still a closed-form Bessel/Hankel series, zero new
  FDTD), paired with **`graded_black_shell_flagship`'s own 450/750nm
  sweep** (both PHOTONICS and MATERIALS named this). (7) Carried
  backlog, unblocked, lower urgency: R3-on-loaded-legs for
  `off_pass_joint`/`off_bracket_joint`; the flank-denominator
  distribution upgrade; a Geary-Hinkley tail-shape model of `C(δ)`;
  P-VIS-5's angle-quantization sensitivity formula; shell-vs-solid
  thermal-mass parameterization (3rd consecutive cycle open); QUANTUM's
  convergence-guard audit pass across `lab/`'s other closed-form modules
  for the "exact-threshold-from-a-wide-bracket" pattern (QUANTUM's own
  new Phase-5 finding: the `Q_ext(x)` module's own "x=260 exact
  threshold" claim is itself imprecise, true NaN onset ≈x=259 — Tier-2,
  non-blocking); `coupled_segment_general`'s RK4-cross-checked
  trust-suite promotion.
- **[superseded — the original locked-item bullet, retained only as a
  pointer to the LOCK's own history; the binding record is the [done]
  entry above]** ~~The `Q_ext(x)` closed-form cylinder/disk check~~ —
  now closed by exp-059, see above.
- **[queued — ranked for Iteration 36+ (behind the LOCKED item above),
  per Red Team's Iteration-35 Phase-5 reconciliation of all six seats,
  exp-058 — CURRENT top-of-queue, supersedes the list below as the
  active ranking, retained as valid backlog, not deleted]** (1)
  **R3-on-loaded-legs** — resolution check (cpl 20→30, exp-056's own
  rescaled-geometry idiom) on `off_pass_joint`/`off_bracket_joint`
  themselves, still never run (independently found by EM and QUANTUM at
  Iteration 33, unaffected by Iteration 35's different phase-variance
  axis) — Iteration 34's own #2 competitive priority, carried forward
  two cycles now. (2) **Upgrade the flank-denominator diagnostic** from
  a binary `<0.20` flag to a reported distribution/correlation — EM's
  own Iteration-35 Phase-5 re-analysis found a real, moderate
  (`corr≈0.45–0.50`, R²≈0.20–0.25) but only partially-explanatory
  correlation the binary flag can't show; also re-derive the 0.20
  threshold for an N=2000-ensemble context rather than reusing the
  single-realization calibration unmodified. (3) **A Geary-Hinkley
  quantitative model of `C(δ)`'s own tail shape** — QUANTUM OPTICS'
  Iteration-35 Phase-5 proposal, near-zero-cost now that
  `b_obj_draws`/`b_flank_draws` are persisted (exp-058's own
  `recompute_flux_signs.py`). (4) **P-VIS-5's angle-quantization
  sensitivity formula** (derive, not measure, per Red Team's own
  Iteration-33 mandatory fix) — named by 3 of 6 Iteration-33 seats,
  still open. (5) **MATERIALS' absorptivity/mechanism literature check**
  (exp-052 queue item 5) — zero-FDTD, deferred since Iteration 29, now
  **SEVEN** cycles running — flagged explicitly by both MATERIALS and
  Red Team at Iteration 35 as approaching this program's own escalation
  pattern (half the count that triggered two prior unconditional locks).
  (6) **λ/angle generalization** (450nm/750nm) for the T26 near-null
  result — exp-056 tested one native geometry at one λ only. (7)
  **Shell-vs-solid thermal-mass parameterization** — third-consecutive-
  cycle open item (Iteration 20→31→34), confirmed non-load-bearing to
  date but "a live landmine" for a future transient prediction. (8)
  **`graded_black_shell_flagship`'s own 450/750nm sweep** through the
  corrected chain, zero new FDTD. (9) **`coupled_segment_general`'s
  promotion** to a real trust-suite stage with an RK4 cross-check —
  exp-054's own carried item, still unbuilt across five cycles now.
- **[queued — ranked for Iteration 33+, per Red Team's Iteration-32
  Phase-5 reconciliation of all six seats, exp-055 — superseded by the
  Iteration-33 list above, retained as historical backlog; both
  are retained as valid backlog, not deleted]** (1) **A combined T26
  build**: the generalization test on a near-null σ(I) article
  (`off_pass`/`off_bracket`, exp-032/033) — the regime where the empty-
  scene coherent-injection artifact could actually flip a live
  PASS/MARGINAL verdict (QUANTUM OPTICS' and VISION SCIENCE's own top
  pick) — folding in, as same-build riders at near-zero marginal FDTD
  cost: EM's own empty-scene-specific R3/resolution check at the ACTUAL
  r=78 geometry (never done at Iteration 32 — the only R3 check ran on the
  unrelated small canonical scene) and PHOTONICS' window-position/
  angle-quantization sensitivity scan on the T26 measurement itself. Any
  future `C_thr` citation from this build must carry VISION's own T2
  photopic-regime qualifier (Iteration 32's own mandatory-fix docket).
  (2) **THERMODYNAMICS' `graded_black_shell_flagship` re-run through the
  corrected `mixed_length_scale_regime`** (exp-054 queue item 1, below) —
  now genuinely twice-deferred (Iterations 31 and 32), zero new FDTD, this
  program's own thinnest thermal-detectability margin (~6.04×, itself
  shown to shrink ~3.03× under this exact bug class) — if deferred a third
  time, this item should be considered for the same unconditional-trigger
  bar this program has applied twice before (`h_eff`, r=156/`graded_
  black_shell`). (3) **MATERIALS' absorptivity/mechanism literature check**
  (exp-052 queue item 5, below) — zero-FDTD, deferred since Iteration 29,
  now four cycles running.
- **[queued — ranked for Iteration 32+ / alongside the LOCKED Iteration-31
  slot, per Red Team's Iteration-29 Phase-5 reconciliation of all six
  seats]** (1) **The coherent-vs-incoherent ambient-sum bridge-gate
  revalidation, built against the actual equal-amplitude N9 configuration**
  (not exp-029's own strong-beam/weak-probe idiom) — new live thread **T25**
  (LOGBOOK.md), ranked #1 or #2 by five of six exp-052 Phase-5 seats
  (PHOTONICS #3, EM #2, QUANTUM #1, THERMODYNAMICS #2, VISION #1). No
  geometry this program has run, in 29 iterations, has ever had its actual
  ambient-sum instrument empirically bridge-gated — QUANTUM's own
  concretely-scoped proposal (joint equal-amplitude injection, reusing
  suite stage 11's existing field-identity gates) is the cheapest correct
  next build. (2) **The λ-generalization run** (450nm + 750nm, r=156, both
  families) — ranked by three of six seats (PHOTONICS #1, VISION #3,
  MATERIALS #2), cheap, directly tests whether exp-052's own T14 reframe is
  general or a 600nm/2.4λ-specific coincidence (three on-the-record program
  precedents — R2, T21, the Iteration-19 c*(λ) finding — for treating
  single-λ near-field results with exactly this suspicion). (3) **A
  formally committed `C(z/z_R)` extrapolation fit for the fixed-absolute
  family**, pre-registered falsifiable bands on `C_∞` vs. −1, ideally a 4th
  r-point — executes T8's own long-standing requirement for the first time
  on a family whose slope is correctly signed (EM #1, PHOTONICS #2);
  resolves whether exp-052's own 0.12–0.16 C_∞ shortfall is real or a
  3-point-fit artifact. (4) **The genuine FDTD `ABSORB` sweep at GEOM78** —
  carried unrun across Iterations 26–29 (four straight cycles now), already
  flagged at Iteration 28 as "approaching unconditional-trigger territory
  if deferred again" — one more deferral from meeting the same bar just
  applied to `h_eff`. (5) **MATERIALS' absorptivity/mechanism literature
  check** (T18-dependent, zero-FDTD either way) — the one remaining
  unchecked axis between exp-052's own PLAUSIBLE tier and a tier change on
  this program's now-favored design lead. (6) **A targeted N9-vs-N17
  angular-quadrature check on the opaque-absorber article class** (VISION,
  new this cycle) — T16's entire angular-sampling uncertainty budget has
  only ever been measured on a near-null σ(I) article, never on the
  deep-shadow class most of this program's citations, including exp-052's
  own headline, actually are. (7) **Extend exp-052's own core-fill check to
  the full N9 sweep**, not just θ=0 (MATERIALS) — the θ=0 null is decisive
  at boresight but T9's own established mechanism is a grazing/tangential
  effect; the ±25°/±35° angles that actually feed the headline deepening
  have never been core-fill-tested at these ratios. (8) **QUANTUM's
  grating-lobe/array-factor n\* criterion for `beam_divergence_coherent`**
  (carried unchanged from Iteration 28's own queue, item 2 there) — scored
  against the 72 `coherent` rows exp-051 already computed and labeled,
  using exp-046's validated zero-free-parameter closed form. (9) Low
  priority: promote the `_geom_derived`/`_G_for_g` hoisting pattern to a
  shared utility at the next geometry-parameterized module. Carried
  forward, not re-ranked: VISION's sub-degree angular sweep across
  36°–40° at 750nm/FWHM=2°/GEOM78 (Iterations 27/28/29); T8/T13/T14's
  sensitivity-band minimum bar (dormant 20+ iterations); fresh c*(λ) refit
  at the new geometry; regime-stratify T2's ±0.3-log uncertainty near the
  absolute-threshold edge; ocular-dose disposition.
- **[queued — ranked for Iteration 32+, per Red Team's Iteration-31
  Phase-5 reconciliation of all six seats, exp-054]** (1) **Re-run
  `graded_black_shell_flagship` through the corrected
  `mixed_length_scale_regime`** — this program's flagship article, at the
  record's thinnest thermal margin (~6.04×), still on the old,
  now-twice-repudiated `H_CONV=5.0`/hardcoded-mass/`w_on`-area chain;
  cheapest same-pattern desk-analytic work available (THERMODYNAMICS #1,
  Red Team's own top priority). (2) **Promote `coupled_segment_general`
  into a real trust-suite stage** with a nonzero-initial-condition
  numerical-integrator (RK4) cross-check — EM's Phase-5 review already did
  the verification once outside the repo; commit it as a permanent gate
  (EM #1). (3) **Parameterize `mixed_length_scale_regime`'s fill-fraction
  and material-provenance strings** so a future caller with a different
  material doesn't silently inherit exp-054's own silicon/ASSUMED-T18
  citation (MATERIALS #1, THERMODYNAMICS #2). (4) **A desk closed-form
  `Q_ext(x)` cylinder/disk check** bounding `w_on`'s ~3.03× excess over
  `r_out` — diffraction vs. `iso_xsec_sq` convention artifact (PHOTONICS
  #1, EM #2, THERMODYNAMICS #3, QUANTUM #4 — four of six seats). (5) **Run
  the mixed chain across the standard 450/600/750nm sweep**, reusing
  already-committed exp-026/044 per-λ data, zero new FDTD (PHOTONICS #2).
  (6) **T8/T13/T14's near-field→witness-scale `h_eff` bridge** — the
  largest standing gap in this thread, again explicitly left open
  (P-054-6); named by every seat that discussed scope, ranked lowest only
  because it is the biggest build of the six, not because it matters
  least.
- **[SUPERSEDED — now LOCKED to Iteration 30, see above]** stage-10
  temporal instrument (VISION's Iteration-2 Phase-5 #2): TCSF bars pinned
  first (de Lange/Watson, sourced) — the last unmeasured perceptual axis
  (T3), gates constraint 4. *This bare line, sitting outside the numbered
  queue for 10 consecutive iterations, is exactly the mechanism by which
  the item silently stopped competing (Red Team's Iteration-28 finding).
  It is retained only as a pointer; the binding entry is the LOCKED
  Iteration-30 slot above.*
- **[housekeeping]** cloud shift 10 (old routine, fired 06:23Z mid-redesign)
  committed its r2-isolation experiment as a second "exp-020" on main —
  renumbered to exp-022/023 at the redesign merge, content untouched, noted in
  SESSION_LOG. Old `photonlab-shift` routine to be paused by Marsh
  (owner-created; agents cannot modify it) — replaced by the panel-shift
  routine.

- **[open, contract lane]** Artifact-schema formalization for the ambient
  instrument: the `angle_deg` source key + per-run energy/intensity ledger
  rows belong in `lab/ARTIFACTS.md` — that is the cross-lane contract
  (Bonnie's veto lane, AGENTS.md), so it needs the counterparty-review PR,
  not a unilateral panel edit. Until then the ledger lives experiment-side
  in `results.json` (exp-020 synthesis, docket #4).

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
- [done 2026-08-11, cloud shift 8] *Mechanism* candidates for the
  eps_z≈2.25–2.4 trough — run as exp-016 (outer-boundary impedance
  mismatch) and exp-017 (angular-pattern shape comparison, new
  `lab.sections.angular_scattered_pattern` capability). **Both refuted.**
  See Current state.
- [done 2026-08-12, cloud shift 9] The frequency-domain mechanism check
  proposed by exp-017 — run as exp-018. **Major reframe: the "eps_z
  trough" is not an eps_z effect.** It's a shell-thickness standing-wave
  condition at exactly 3λ (exp-002's original geometry, a coincidence
  not a chosen eps_z). See Current state.
- [done 2026-08-12, cloud shift 9] Direct test of exp-018's standing-
  wave hypothesis at 2λ — run as exp-019. **Does not generalize**: no
  dip near 2λ, ruling out a generic "shell = integer × λ" rule. 3λ looks
  specific, not a member of a broader family (yet). See Current state.
- [done 2026-08-12, cloud shift 10] exp-019's own queued follow-up (is
  the 3λ feature reproducible at a different fixed r2?) — run as
  exp-022. **No**: neither r2=75 nor r2=120 reproduces the negative
  jump at their own shell=3λ point. The feature is r2=90-specific.
  Gate miss at r2=75/floor=0.10 resolved same-shift by exp-023. See
  Current state.
- **[open, parked — trough line]** exp-022's own queued follow-up (see its NOTES.md Next):
  the trough has now survived five mechanism/generality checks in a row
  (exp-016 impedance, exp-017 angular pattern, exp-018 eps_z, exp-019
  integer-λ, exp-022 r2) without one explaining or generalizing it.
  Two paths for a future dedicated shift: (a) declare
  r1=30/r2=90/λ=600nm/floor∈{0.10,0.18} an idiosyncratic anomaly and
  stop chasing it, returning fully to the design-lead line; or (b) one
  more targeted test — hold r1 AND r2 both fixed at exactly 30/90 and
  sweep λ finely (1–2nm steps) around 600nm to see whether the negative
  jump is itself narrow-band (a true resonance linewidth) — the mirror
  of exp-018's coarse λ sweep, which rescaled geometry to hold eps_z
  fixed rather than holding geometry fixed.
- [open, secondary, exp-017] A local-maxima count found 13 angular peaks
  at the trough vs 10 at each flank — unscored, not folded into the
  magnitude-only conclusion, but worth a finer-binned or bare-disk-
  referenced recheck if a future shift returns to this mechanism
  question. (Read now in light of exp-018/019: "the trough" in that
  observation is specifically the shell=3λ point, not an eps_z-axis
  location.)
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
