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

## Current state (2026-08-13, panel Iteration 5)

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

## Next work

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
- **[queued — panel Iteration 6, lead per rotation QUANTUM OPTICS,
  mandatory build committed this shift]** the coherent-superposition
  bridge-gate package (deferred three times prior; this is the mandatory
  fourth-cycle build, not a fifth deferral) — QUANTUM's own Iteration-5
  Phase-5 scoping notes (not binding, but strong self-authored precedent):
  run the bridge gate on a graded-shell-shaped endpoint article, not a
  uniform sponge disk; fold in `radial_absorbed_power`'s closure identity
  as a second acceptance gate alongside the aggregate box-ledger check;
  hold every per-λ material constant to a printed-assertion discipline
  (the SIGMA_ON lesson). Also queued, ranked by Iteration 5's Phase-5
  consensus: (a) the box-ledger channel's own decision-floor/noise
  characterization — **T11, now the single most-repeated unclosed backlog
  item in this program's history** (3-of-6 Iteration-5 seats, plus two
  prior Red Team recommendations); (b) a cheap sub-cell/window offset
  sweep closing T10's small residual (+3.05pp) — 3-of-6 seats, lowest
  cost on the table; (c) extending `radial_absorbed_power` to the full 3-λ
  sweep, ± angular (r,θ) decomposition (PHOTONICS); (d) docket #7's
  analytic thermal sidecar, now seedable with real spatial data
  (THERMODYNAMICS); (e) a shell-thickness/optical-depth economy sweep
  testing where "the core doesn't matter" stops holding (MATERIALS).
- **[queued — panel Iteration 7, lead per rotation VISION SCIENCE,
  mandatory build committed Iteration 5, pre-registered Checkpoint-4
  tripwire if it slips]** VISION's r=156 scale-bridge check (T8) — five
  consecutive cycles of attempted deferral, each caught only by
  adversarial review; this is the hard commitment, not a sixth soft one.
  VISION's own Iteration-5 Phase-5 pre-staging suggestion: pin the
  r=78/156/312 geometry family, the committed C(z/z_R) extrapolation
  functional form, and which existing articles it runs against, now
  rather than at Iteration 7 itself, to shrink the real cost of the build
  when it comes due. VISION's own dissent (this should have been
  Iteration 6) is on the record in LOGBOOK.md Iteration 5 Phase 5 —
  unresolved, not silently dropped.
- **[queued]** docket #7: sourced witness-scenario parameter table +
  glare/adaptation sidecar (zero runs) → Tier-W constraint-3 scoring on
  the now-unqualified measured C≈−0.684 (exp-024 removed exp-020's 750nm
  asterisk and estimator ambiguity); potential checkpoint criterion 1
  (Tier W) if the 4–21× sub-threshold closure holds.
- **[queued]** stage-10 temporal instrument (VISION's Iteration-2 Phase-5
  #2): TCSF bars pinned first (de Lange/Watson, sourced) — the last
  unmeasured perceptual axis (T3), gates constraint 4.
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
