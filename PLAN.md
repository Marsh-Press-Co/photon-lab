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

## Current state (2026-08-19, panel Iteration 24)

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
