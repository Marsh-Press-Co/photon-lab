# Phase 2 — Red Team Audit (exp-096, Panel Iteration 73)

*Seat charter (PANEL.md, verbatim): attacks every proposal, speaks last and
hardest; standard is not textbook-physics compliance — speculation is
permitted; kills internal inconsistency, unfalsifiable claims, mechanisms
that cannot be expressed as simulation parameters, and proposals that
quietly violate a target constraint, especially #3. Never leads a cycle,
has no proposal of its own to protect.*

Read, in the order specified: PANEL.md; LOGBOOK.md's RULED OUT R1–R17
(R16/R17 in full) and the complete T28 live thread through Iteration 72;
`experiments/095-.../NOTES.md` in full; `experiments/096-.../
phase1_proposal.md`; all five blind Phase-2 critiques (materials, em,
thermodynamics, quantum, vision); and, independently, this session:
`lab/fdtd2d.py` (`Sim.__init__`, `add_line_source`), `lab/materials.py`,
`experiments/069-.../design_geometry.py` (`r3_config`/`r4_config`/
`r5_config`, `R{3,4,5}_CONFIGS`, the six numbered Gates as defined in
`experiments/094-.../run.py`), and `experiments/095-.../run.py` (job
constants, `_run_sim_r{4,5}_sigma`). Every load-bearing figure below was
independently re-derived or directly read from source this session — not
taken on any critique's, or the proposal's own, word.

## 0. Scope note

Pure instrument-validation work (§4/Realizability: T1 route N/A,
Checkpoint criterion 2 N/A — confirmed, matching every T28 desk/instrument
cycle since exp-069). **`constraint-#N-violation` does not apply anywhere
in this audit** — there is no phenomenon-mechanism claim to quietly
violate constraint 1/2/3/4 with, and nothing found below smuggles one in.
**`inexpressible` also does not apply** — every quantity checked (`sim.lam`,
`angle_deg`, `sl`, the phase array) is already a concrete, already-existing
object attribute; nothing here gestures at an untestable mechanism. Both
tags are named, not silently dropped. Attacks below are tagged
`[inconsistency]` throughout — every genuine defect found is a mismatch
between what the document claims and what the source or its own text
actually shows, not a phenomenon-level claim of the unfalsifiable kind.

## 1. Independent verification of the five blind critiques

All five reproduce correctly on independent re-derivation from source.
Detail:

**MATERIALS** (Gate 5/registration gate verify recipe-output-reached-`Sim`,
never recipe-correctness). Read `design_geometry.py` directly:
`R3_CONFIGS`/`R4_CONFIGS`/`R5_CONFIGS` are module-level calls to
`r3_config()`/`r4_config()`/`r5_config()` — three functions that are
literal line-for-line mirrors of each other, differing only in which
`R{n}_BASE_*` constants (each `round(<native constant>×RATIO)`) they close
over. Read `lab/materials.py` directly: `dielectric_cylinder`/`pec_disk`/
`graded_black_shell`/`uniform_lossy_shell` write only to `sim.eps_r`,
`sim.sigma_e`, `sim.pec`, `sim.objects` — confirmed, never `sim.lam`,
`sim.sources`, `sim.source_specs`. **Confirmed** on both counts.

**ELECTROMAGNETISM** (Checks 1/2 compare a value against itself). Read
`experiments/095-.../run.py` directly: `_run_sim_r5_sigma` (line 307-308)
constructs `Sim(..., cells_per_lambda=dg.R5_CPL[600], ...)`; the exp-094
`_run_sim_r4_sigma` it mirrors (line 261-262) constructs
`Sim(..., cells_per_lambda=dg.R4_CPL[600], ...)`. `RANK1A_ANGLES=[39.2,
39.4]` at line 263, `RANK1C_ANGLES=[38.49,38.69]` at line 264,
`RANK3A_ANGLE=41.6` at line 268, `RANK4_ANGLE=38.4` at line 270 — all
confirmed bit-exact against the proposal's own §3 Provenance column.
`add_line_source(..., angle_deg=theta, ...)` where `theta` is one of these
same module-level constants, passed through unchanged. §3's own
"Provenance" column cites these exact same objects (`dg.R4_CPL[600]`,
`RANK1A_ANGLES[0]`) as the gate's `cpl_intended`/`theta_intended`.
**Confirmed**: Checks 1 and 2 are, as specified, a comparison of a Python
object against itself along the only axis (job-constant corruption) that
matters for a shared-root defect.

**QUANTUM OPTICS** (an independent, textually separate, pre-run-frozen
ground truth already exists and is not checked). Confirmed directly:
`experiments/095-.../NOTES.md`'s own "## Predictions" section states, in
prose, `delta_scene(R4, 39.2°) < 0 AND delta_scene(R4, 39.4°) < 0` (Rank
1a) and the `38.49°/38.69°` node-bracketing pair (Rank 1c) — committed to
git, per house discipline, *before* `run.py` was written. The proposal's
own gate never cross-checks `run.py`'s job constants against this earlier,
independent document. **Confirmed**, and this is the sharpest of the
three routes to the same crux, because NOTES.md predates `run.py` and so
cannot share a copy-paste origin with it.

**THERMODYNAMICS** (§7's "12 Sim constructions" is wrong — true count is
10). Re-derived directly from §2b/§3: positive control =
`Sim(cells_per_lambda=40)`, `angle_deg=39.2` — identical to representative
point 1 (`R4`, `θ=39.2°`, `cpl=40`). FI-B injects `angle_deg=38.69` at
`cpl=40` — identical, as a constructed `Sim` object, to representative
point 4 (`R4`, `θ=38.69°`, `cpl=40`); only the *label* the harness attaches
("intended θ=39.2°") differs, not the object built. FI-A
(`cpl=30`×`θ=39.2`) and FI-C (`angle_deg=−39.2`) are genuinely new
combinations absent from the 8. **Confirmed**: 8 + 2 new = 10 distinct
constructions, not 12.

**VISION SCIENCE** (missing §5 banner; §1 over word cap). Both confirmed
by direct inspection: `grep -c "governed by Idealizations"
phase1_proposal.md` returns exactly 1 hit, at line 497 inside §6 — §5
(opening at line 317) never states it, despite §6's own text asserting it
is "mandatory at both this section and §5." Word-count of §1 (the
"Mechanism/instrument narrative" section, verbatim text between its own
heading and §2's) is 335 words by direct count, against PANEL.md's own
"≤300 words" Phase-1 spec. **Confirmed**, both exactly as stated.

## 2. Numbered attacks

**#1 [inconsistency] — the proposal's own justification for checking only
one member of each C/G pair is factually wrong, and the error is not
cosmetic: it invalidates representativeness for exactly the two checks
(placement, phase array) that matter most.** §3 states: *"Both configs in
each family's pair (`C40_R{n}`/`G40_R{n}`) share identical `nx,ny,src_x,
y_lo,y_hi` by this program's own established congruent-construction
discipline (Gate 3, `A` held bit-identical across the pair...)."* I pulled
`R4_CONFIGS["C40_R4"]` and `["G40_R4"]` directly:

| field | `C40_R4` | `G40_R4` |
|---|---|---|
| `nx` | 720 | 880 |
| `ny` | 3168 | 3328 |
| `src_x` | 600 | 680 |
| `y_lo` | 80 | 160 |
| `y_hi` | 3088 | 3168 |
| `A` | 1504 | 1504 |

Only `A` is identical — every other field the proposal names as identical
is not. The citation is also wrong on its own terms: I read
`experiments/094-.../run.py`'s own gate labels directly — **Gate 2** is
"A congruence" (`C40_R4.A == G40_R4.A`), **Gate 3** is `L_GEOMETRIC_M_R4`
bit-identity *across families* (native/R3/R4), an unrelated cross-family
physical-radius check, not a cross-pair one. The proposal cites the wrong
gate for the wrong property. Substantively: `C40`/`G40` exist specifically
to test box-clearance/domain-boundary-wall sensitivity (`G` adds uniform
padding to push the walls further away) — they are, by design, two
*differently-wired* constructions, with only the source aperture `A` held
fixed so the underlying physics stays comparable. Checks 1 (`sim.lam`) and
2 (`angle_deg`) genuinely are representative across the pair, since `cpl`
and `θ` don't depend on which box-clearance config is used. **Checks 3
(placement: `x`, `sl`) and 4 (the phase-ramp array, a direct function of
`y_lo`/`y_hi`) are not** — a defect specific to how `G`'s own `pad`
argument propagates through `r{n}_config()` (a different code path through
the identical function, but a different multiplier) would not be
exercised by checking `C` alone, and `G` is exactly the code path most
likely to carry a pad-arithmetic defect since it is the one that adds a
nonzero `pad`. This directly undercuts the "checking one member... is
representative of both" claim for Checks 3/4 specifically — the same
claim that licenses using 8 points instead of 16.

**#2 [inconsistency] — the three-way convergent finding (MATERIALS/EM/
QUANTUM), independently re-verified against source at §1 above: the gate
validates job constants against themselves, never against a ground truth
outside the code path it audits.** §5a's CLEAN branch states this cycle
"removes construction-time wiring/registration as a live explanation for
exp-095's own Rank 1c FAIL... entirely." On the verification at §1, this
is not supportable as written: a CLEAN result at all 8 points, even
combined with a clean FI-A/B/C positive control, rules out only a
*caller-level plumbing* defect (a wrong literal typed at one call site
that diverges from the shared job constant) — it does **not** rule out
(a) a defect baked into the shared, deterministic `r{n}_config()` recipe
itself (MATERIALS — the class Idealization 17, carried into this very
proposal, already names as live and structurally reproduced at every
ratio); (b) a defect at the source-of-truth job constant itself
(`dg.R4_CPL`/`RANK1A_ANGLES`), which both the production call site and
this gate's own "intended" values read from identically (EM); or (c) a
transcription slip between `run.py`'s job constants and the textually
separate, temporally-*prior* ground truth in exp-095's own frozen
NOTES.md Predictions section (QUANTUM). See §4 below for whether this is
fatal.

**#3 [inconsistency] — EM's sharpest sub-finding, independently
re-verified against the proposal's own §2a text: Check 4, as specified,
inherits any corruption Check 1 fails to catch, contradicting §2a's own
"logically sufficient" claim.** §2a states Check 4 is recomputed "using
the already-independently-verified `sim.lam` from check 1 (not
`cpl_intended` directly)." Trace the failure mode this creates: if the
*source-of-truth* constant (`dg.R4_CPL[600]`) is itself wrong — not a
caller-level mismatch, but a defect at the one place both the production
call site and `cpl_intended` read from — then `sim.lam` and `cpl_intended`
are bit-identical (both equal to the same wrong number), so Check 1
passes. Check 4 then recomputes its comparator using that same "verified"
`sim.lam`, which is self-consistently wrong, and the actual phase array
(built from the same wrong `self.lam` inside `add_line_source`) agrees
with it. Check 4 passes too. §2a's claim that "this check alone is
logically sufficient to catch anything checks 1–3 catch" is true only for
the caller-plumbing defect class (a divergence *introduced downstream* of
the job constants) — it is false for the source-of-truth defect class
attack #2 names, which is exactly the class MATERIALS'/QUANTUM's fixes
target.

**#4 [inconsistency, minor] — the proposal's own §2a pseudocode computes a
`phase_expected` array using `cpl_intended` (commented "`# NOT sim.lam
yet`") that Check 4, as specified two paragraphs later, does not actually
use — Check 4 performs a second, separate recomputation using the
verified `sim.lam` instead.** Either the first array is a vestigial
illustration never compared against anything, or the document
under-specifies which of two candidate `phase_expected` arrays Check 4
actually diffs against `sim.sources[-1]['phase']`. Low severity (both
arrays are identical whenever Check 1 has already passed, which is the
only case where the ambiguity matters), but worth resolving in code
comments before Phase 4, not left for the implementer to guess.

**#5 [inconsistency] — THERMODYNAMICS' finding, confirmed at §1: §7's "12
`Sim` constructions" should read 10.** Non-load-bearing to the "0 FDTD
calls" claim (unaffected either way — none of the 12/10 constructions ever
reach `sim.run()`), but affects the wall-time estimate's own precision and,
more importantly, §5b's framing of the positive control as independent
evidence: it is the same object as representative point 1, already scored
under §5a. Not a problem in itself (reusing an already-scheduled correct
construction as the positive-control demonstrator is efficient, not
wrong) — but the document should say so explicitly rather than imply four
freshly-built configurations.

**#6 [inconsistency] — VISION's finding, confirmed at §1: §5 fails the
proposal's own stated house rule.** §6 states the carried-idealizations
banner is "mandatory at both this section and §5" (echoing the
Iteration-65 CHECKPOINT's non-discretionary "both Predictions and Result"
rule, extended by this document's own text to its own §5/§6 pair) — then
§5 never states it. This is the document contradicting its own explicit
claim of compliance, not merely an omission; the correct comparison class
per R17/R15's own lineage is a rule-compliance defect, not a numeric one.

**#7 [inconsistency, process] — VISION's finding, confirmed at §1: §1 runs
335 words against PANEL.md's own 300-word Phase-1 cap.** Zero-cost fix
(trim); flagged because this program's own discipline (R4/R9, applied
here to a *word-count* rule rather than a number) treats a stated
compliance claim that doesn't hold up under a direct count as worth
catching every time, not only when material.

## 3. Adjudication of the five blind critiques

| # | Seat | Finding | Disposition | Fix adopted |
|---|---|---|---|---|
| 1 | MATERIALS | Both gates verify recipe-output-reached-`Sim`, never recipe-correctness; §5a "entirely" overclaims | **ADOPTED** | Reword §5a (fix docket #2 below); add MATERIALS' own companion check — independently recompute ≥1 `R4` placement value from native base constants × `RATIO`, outside `r{n}_config()` |
| 2 | ELECTROMAGNETISM | Checks 1/2 compare a value against itself, not an out-of-band truth; Check 4 inherits Check 1's own possibly-corrupted `sim.lam` | **ADOPTED** (both halves — the second half independently re-derived and sharpened at attack #3 above) | **OVERRIDE the proposed remedy, not the finding.** EM's own fix (hand-transcribe the 8 tuples as fresh literal constants inside the gate module) adds no real independence if retyped from the same `run.py` source — a second manual copy of the same numbers guards against a keystroke slip, not a source-of-truth defect. QUANTUM's NOTES.md cross-check (below) is the more principled version of the same instinct — it checks against a document that predates `run.py` and cannot share its origin — and subsumes EM's ask. EM's secondary request (reword §5a's "entirely") is adopted verbatim into fix docket #2. |
| 3 | THERMODYNAMICS | §7's "12 Sim constructions" is arithmetically wrong; true count is 10 | **ADOPTED** | Correct the count; disclose which legs reuse already-scheduled representative-point objects (fix docket #5) |
| 4 | QUANTUM OPTICS | An independent, textually separate, pre-run-frozen ground truth (NOTES.md's own Predictions section) exists and is never checked | **ADOPTED** | Add QUANTUM's proposed fifth check as specified: for each of the 8 points, assert `run.py`'s job constants equal the values stated in exp-095 NOTES.md's frozen Predictions section (fix docket #4) — the single most load-bearing fix in this docket, since it is the one check in this audit's own judgment that closes a genuinely different defect class (transcription into `run.py`) rather than reformulating one already covered |
| 5 | VISION SCIENCE | §5 missing its own mandatory banner sentence; §1 over the 300-word Phase-1 cap | **ADOPTED**, both | Add the banner to §5 (fix docket #6); trim §1 (fix docket #7) |

All five: **ADOPTED, zero overridden findings.** One proposed *remedy*
(EM's, not the underlying attack) is overridden in favor of a more
principled alternative already on offer from a sibling critique — this is
adjudicating between two fixes for the same accepted defect, not
disputing the defect itself.

## 4. The three-way convergent finding: fatal or fixable?

**Fixable, and cheaply — not fatal to the proposal's core value.**

The convergence itself (MATERIALS/EM/QUANTUM independently reaching the
same crux by three different routes, none seeing the others' work) is
real and should be weighed at full strength, matching this program's own
precedent for multi-seat convergence (exp-095's own Phase-5: independent
convergence on a finding is treated as evidence the finding is a genuine
structural gap, not critique noise — six-for-six there, three-for-five
here, still unanimous among the seats that raised it). It identifies a
genuine, load-bearing gap: as specified, a CLEAN result cannot
distinguish "correctly wired" from "wrong at the one shared source every
downstream check reads from" — and that source-level defect class is
*exactly* the one this whole 19-cycle sub-thread's own Idealization 17 has
flagged as most concerning, because it is the one class that would explain
a *uniform* reversal across `R3`/`R4`/`R5` (all built from the identical
recipe) rather than a scattered one.

It is not fatal, for three reasons specific to what fixing it actually
costs:

1. **Every fix is zero-FDTD, code-only, and additive to the design already
   on the table** — none require abandoning the four-check architecture,
   the fault-injection triad, or the desk bound. QUANTUM's NOTES.md
   cross-check (fix #4) and MATERIALS' outside-the-recipe recompute
   (fix #3) are each a few lines of Python; neither touches `lab/fdtd2d.py`
   or spends a single `sim.run()` call. This matches this program's own
   "fix what's broken, don't force a redesign for a cheap check"
   discipline exactly — the same discipline that kept exp-095's own
   five-critique convergence at PROCEED-WITH-MANDATORY-FIXES rather than
   HALT-AND-REDESIGN.
2. **The gap is bounded, not open-ended.** After fixes #3/#4, the gate's
   honest scope becomes: rules out caller-level plumbing (as designed,
   unchanged), rules out `run.py`-vs-NOTES.md transcription (new, via
   QUANTUM's fix), and gets one spot-check against the recipe-level class
   (new, via MATERIALS' fix, extending the existing Gate-2 precedent —
   which already independently recomputes `A` from native constants ×
   `RATIO` — to the placement quantities this gate itself reads). What
   remains genuinely uncovered after these fixes is a narrower, honestly
   nameable residual: a defect in the recipe's *other* internal arithmetic
   that a single spot-check doesn't happen to probe. That is a legitimate
   idealization to state, not a reason to distrust the whole instrument.
3. **The core value survives untouched.** The single most load-bearing
   fact motivating this cycle — Gate 5 has checked `sigma_e` magnitude at
   every `R3`/`R4`/`R5` call site for two cycles running and has *never*
   checked `angle_deg`, `sim.lam`, or the phase array — is not disputed by
   any of the three critiques, by this audit's own independent source
   read, or by attack #1's independent finding. A correctly-scoped CLEAN
   result (post-fix) still converts "this whole axis has never been
   checked" into "checked and correctly wired, at the caller-plumbing and
   transcription levels, with one spot-check against the recipe level" —
   real, new, forward information, exactly matching what Idealization 32
   already (correctly) frames as narrowing, not closing, the two-candidate
   hypothesis space.

**Minimal fix, stated precisely:** reword §5a to name the three defect
classes it does and does not rule out (fix #2); add QUANTUM's NOTES.md
cross-check as a fifth, near-zero-cost check (fix #4); add one
MATERIALS-style independent recompute of an `R4` placement value from
native constants × `RATIO`, outside `r{n}_config()` (fix #3). That is the
entire minimal fix — it does not require exhaustive coverage of every
recipe constant, a second independent discretization scheme (which
MATERIALS itself, in the exp-095 precedent this cycle inherits, correctly
declined to demand), or any FDTD spend.

## 5. R17 boundary-drawing check: does `atol=1e-9` belong to R17?

**Independently checked; the proposal's exemption is correctly reasoned,
not a self-serving carve-out.** R17's own text (adopted verbatim from
exp-095's Phase-5 final audit, LOGBOOK RULED OUT registry) governs "a
tolerance/bracket/window sized to test whether a **feature** (a node,
crossing, or period) **is present or has moved**" — a physical/measurement
question about where something sits in the world, answered against
established cross-resolution or cross-condition shift magnitudes.
`atol=1e-9` on the Check-4 array comparison tests something categorically
different: whether two IEEE-754 float64 evaluations of the *identical*
closed-form formula, on the *same* inputs, agree to numerical noise — a
software-correctness question, not a physics-detection one. I
independently recomputed the margin the proposal states: at `R5`'s widest
window (`C40_R5`, `y_hi−y_lo=3760` cells, confirmed directly from
`R5_CONFIGS`), `k·sin(θ)·Δy_max = (2π/50)·sin(41.85°)·1880 ≈ 157.5` rad,
matching the proposal's "≈158" to the digit. Float64 ULP at that
magnitude is `~158×2⁻⁵²≈3.5×10⁻¹⁴` — `atol=1e-9` sits roughly five orders
of magnitude *above* the roundoff floor (comfortable headroom against
false positives from operation-ordering differences) and, independently,
about nine orders of magnitude *below* the smallest plausible genuine
defect signal (EM's own re-derivation: FI-B's `sin(39.2°)−sin(38.69°)≈
0.006` → a ~1.4 rad phase delta at `R4`'s span) — comfortable margin in
both directions, matching EM's own steel-man exactly on independent
re-derivation. **No fix required; this is not a boundary R17 was written
to police, and the proposal's own §ompliance-header reasoning holds up.**

## 6. Checkpoint criteria, briefly

None fire. Criterion 1/2/3/5: N/A, matching every T28 desk-cycle
disposition (no run yet; T1 N/A; no new engine machinery; no consecutive
non-advancing pair — exp-095 delivered a genuine HALT-with-new-anchor
result). Criterion 4 (program-integrity drift): the closest candidate is
attack #2/#3's overclaim, but it is caught here, blind, at Phase 2, before
Phase 3 freezes anything — matching this sub-thread's own unbroken
non-firing precedent (R6–R17's shared "caught blind, same phase, before
adoption" discharge test). Does not fire.

## 7. Verdict

**PROCEED-WITH-MANDATORY-FIXES.**

Not HALT-AND-REDESIGN. The convergent finding (§4) is real and would have
been serious left unaddressed — it directly threatens the specific
sentence ("removes... entirely") the proposal leans on to claim it closes
"the single most fundamental unresolved question" in this 19-cycle
sub-thread. But every defect found in this audit, including the one
genuinely novel structural finding (attack #1, the C/G pair
misattribution) and the sharpened convergent-finding sub-point (attack
#3), is a scoping, wording, or coverage-completeness problem answerable
with zero-FDTD, code-only additions to the design already on the table —
not a broken instrument, not an unfalsifiable claim, not a mechanism that
resists expression as simulation parameters. The eight-item docket below
is materially cheaper than the cycle it corrects, matching this program's
own unbroken same-shift-fix precedent (exp-095's own nine-item docket,
zero overridden, is the direct structural analogue).

## 8. Mandatory-fix docket (eight items, zero overridden)

1. **Correct §3's C/G-pair congruence claim and its citation.** Only `A`
   is held identical between `C40_R{n}`/`G40_R{n}` (Gate 2, not Gate 3 —
   Gate 3 is the unrelated cross-*family* `L_GEOMETRIC_M` check); `nx`,
   `ny`, `src_x`, `y_lo`, `y_hi` all differ by construction. Exercise the
   already-offered fallback: check **both** members of all 8 pairs (16
   constructions) for Checks 3 (placement) and 4 (phase array) at minimum
   — Checks 1/2 may still use one representative member per pair, since
   `cpl`/`θ` do not depend on which box-clearance config is used.
2. **Reword §5a's CLEAN branch** to name the three defect classes it does
   and does not rule out: rules out caller-level plumbing (as designed);
   after fixes #3/#4 below, also rules out `run.py`-vs-NOTES.md
   transcription and gets one spot-check against the shared-recipe class;
   does **not**, even post-fix, prove the shared `r{n}_config()` recipe's
   full internal arithmetic is defect-free. Replace "entirely" with this
   scoped language throughout §5a.
3. **Add MATERIALS' companion zero-FDTD check**: independently recompute
   at least one `R4` `y_lo`/`y_hi`/`cx`/`cy`/`src_x` value directly from
   the native (`cpl=20`) base constants × `RATIO`, outside the
   `r{n}_config()` code path — extending the existing Gate-2 precedent
   (which already does exactly this for `A`) to the placement quantities
   this registration gate itself reads.
4. **Add QUANTUM's fifth check**: for each of the 8 representative points,
   assert the `theta_intended`/`cpl_intended` values pulled from `run.py`
   job constants equal the values stated in exp-095's own NOTES.md frozen
   Predictions section, cited by line — the one fix in this docket that
   closes a defect class none of the other four checks can reach by
   construction.
5. **Correct §7's Sim-construction count from 12 to 10** (positive control
   ≡ representative point 1; FI-B ≡ representative point 4, as constructed
   objects), and state explicitly whether these two legs reuse the
   already-scheduled representative-point objects verbatim or are
   deliberately reconstructed.
6. **Add the missing "every prediction in §5 is governed by Idealizations
   1/7/17/31–37" banner sentence** to the top of §5, satisfying the
   document's own §6 requirement.
7. **Trim §1 to ≤300 words**, per PANEL.md's own Phase-1 spec.
8. **Clarify or remove** the vestigial `cpl_intended`-based `phase_expected`
   computation shown in §2a's "What it independently recomputes" code
   block, which Check 4 as specified does not actually use (it performs a
   separate, second recomputation from the verified `sim.lam` instead) —
   a documentation-only fix, zero design change.

No item requires any FDTD spend — every fix is either a wording
correction, a re-derivation from already-committed source, or (item 1) an
expansion from 8 to 16 already-zero-cost `Sim` constructions the proposal
itself names as available "at zero additional design cost."
