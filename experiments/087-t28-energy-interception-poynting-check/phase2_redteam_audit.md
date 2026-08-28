# PHASE 2 — RED TEAM AUDIT · Panel Iteration 64 · exp-087
## "Measuring the Energy-Interception Cross-Check for Real"

Charter: attacks every proposal, speaks last and hardest; standard is not
textbook-physics compliance; kills internal inconsistency, unfalsifiable
claims, inexpressible mechanisms, and quiet constraint violations
(especially #3). Checkpoint criterion 2 is correctly N/A this cycle (no
phenomenon-mechanism claim, per §3) — this audit accordingly does not weigh
T1/constraint-1/2/4 questions; it weighs measurement validity and
constraint-3 bookkeeping honesty, matching what the proposal itself claims
to be.

Everything below was independently re-derived from source (`lab/sections.py`,
`lab/thermo_sidecar.py`, `lab/validation/run_all.py`, `experiments/069.../
design_geometry.py`, `experiments/024.../run.py`, `experiments/083.../
run.py`) or recomputed by hand — not accepted from any critique's own
prose, per this program's own R4/R9 discipline.

---

## 0. Housekeeping verification (R4-style, before anything else)

- Parameter-table arithmetic re-derived independently and confirmed exact:
  `BOX_A` = OBJ ± (R_OUT+12) = 170±90 / 792±90 → `(80,260,702,882)` for C40;
  shift by PAD=40 for G40 → `(120,300,742,922)`. `BOX_B` = OBJ ± (R_OUT+24) =
  170±102/792±102 → `(68,272,690,894)`. Both match the proposal's table
  exactly; no hand-typing error found.
- `dg069.CPL[600]=20`, `R_OUT`, `GUARD_OUT=185`, `STEPS_SETTLED=2800`, and
  `DENSE_ANGLES` (31 points, 36.0→42.0, step 0.2°, indices 0/15/30 =
  36.0/39.0/42.0 exactly) all confirmed by direct read of
  `experiments/069-.../design_geometry.py` — the proposal's citations of
  `DENSE_ANGLES[0]`/`[15]`/`[-1]` are correct, not approximate.
- `REF = (OBJ_X, OBJ_Y, 80)` confirmed from `experiments/024-.../run.py`
  line 35 — "i_inc strip (empty run)" verbatim, a **fixed spatial location
  keyed to the object's own position**, swept only in incidence angle
  across calls. This fact is load-bearing for Attack 1 below.
- Total new FDTD calls: 2 configs × 3 angles × 2 legs = 12. Confirmed.

---

## 1. Independent verification of each critique's factual claims

### 1a. EM — `sigma_ext_cross` never checked for `graded_black_shell` / obliquely

Read `lab/validation/run_all.py` directly rather than trusting the critique.
Every place `sigma_ext_cross` appears in the whole suite:

| Line | Stage | Object | Angle | Gate |
|---|---|---|---|---|
| 513 (`xi_p`) | stage 8 | bare PEC disk | broadside | `xi_p<=0.12` |
| 649 (`xr`) | stage 9 gate f | **lossless** dielectric cylinder | 30° oblique | `xr<=0.12` |
| 2055 (`xi_u`) | uniform-lossy-shell stage | `uniform_lossy_shell` (a **different** absorbing profile from `graded_black_shell`) | broadside | `xi_u<=0.12` |

**EM's load-bearing claim is CONFIRMED exactly**: nowhere in this table is
the object `graded_black_shell` (this program's actual flagship absorber,
the one `exp-087` measures), at any angle. Nowhere is any absorbing/lossy
object checked obliquely — the only oblique check (stage 9 gate f) is on a
*lossless* scatterer, which cannot exercise the absorption channel at all.
`exp-087` is simultaneously the first oblique application of `widths()` to
an absorbing article AND the first application of the extinction-two-routes
identity to `graded_black_shell` specifically, at any angle — a real,
previously-uncrossed combination.

**One correction to EM's own supporting prose, in the spirit of R4/R9's
"re-verify even a confirmed claim's own phrasing" discipline**: EM's
"Sharpest attack" text states the identity "has only ever been exercised on
a bare PEC disk at broadside incidence" — this slightly understates the
suite's actual (still insufficient) coverage: an oblique check exists (on a
lossless object) and a broadside check exists on a *different* lossy
profile (`uniform_lossy_shell`). Non-load-bearing — it does not change
which object/angle combination is actually missing, or the recommended
fix — but stated here so the record is precise. EM's own "Supporting
detail" section (the part that matters) is scoped correctly ("no analogous
`xi_d`/`xi_k` **anywhere in that function**") and is exact.

Confirmed also: `sections.widths()` (line ~151) already returns
`sigma_ext_cross` in its return dict — computing `xi_ext` costs zero
marginal FDTD calls, exactly as EM states.

**Verdict on EM's critique: CONFIRMED, load-bearing, mandatory fix.** This
is the single most consequential gap of the five: P5's entire primary
metric depends on `sigma_abs(BOX_A)`/`sigma_ext(BOX_A)` being trustworthy
for exactly the untested combination (oblique + absorbing + PAD-shifted
box) this program's trust suite has never certified.

### 1b. QUANTUM — vacuous classification at 0 resolved angles

Re-read §4-P5 verbatim (not paraphrased):

> **ENERGY-DECOUPLED**: `ratio_k(θ) < 0.1` at every resolved angle.
> **CONSISTENT**: every resolved angle has `0.1 ≤ ratio_k(θ) ≤ 10`.

At exactly 0 resolved angles, both are universally-quantified statements
over an empty set — both are **vacuously true simultaneously**. The
document names no tie-break. And §7 states, verbatim: "directly discharges
the tripwire regardless of which classification ... the data return ...
No result this cycle can produce constitutes a sixth deferral."

**Confirmed exactly as QUANTUM states.** Two things worth separating,
independently reasoned through here rather than merely re-stated:

- On the **Checkpoint-tripwire question specifically**: the tripwire's own
  text (LOGBOOK Iteration 63) is "a fifth consecutive deferral without
  either building a purpose-built scene or explicitly retiring the
  framing fires..." — *building* the scene-bearing measurement (which
  happens regardless of how many angles resolve) is the condition, not
  confirming an answer. So §7's discharge claim is literally defensible
  on the tripwire's own terms even at 0 resolved angles.
- On the **scientific-evidence question**, which is separate and is what
  QUANTUM is actually attacking: an all-UNRESOLVED outcome, if it silently
  rode along inside "regardless of which classification," would let a
  degenerate, uninformative run be reported with the same confidence as a
  real ENERGY-DECOUPLED/CONSISTENT finding — the exact silent/thin-result
  shape the tripwire exists to prevent, relocated from cycle-skipping into
  instrument degeneracy, as QUANTUM correctly names it.

**Verdict on QUANTUM's critique: CONFIRMED, load-bearing, mandatory fix.**
Both halves of QUANTUM's flip-parameter are worth adopting (explicit
0/1-resolved disposition language, plus a synthetic decade-boundary
recovery check) — the second is not merely nice-to-have: this program's own
R5/R10 lineage ("a threshold/period classifier's own discriminating power
must be demonstrated, not assumed, before it is trusted") applies in spirit
here even though neither rule's literal text (named-constant search; free-
period fit) covers a 3-point ratio classifier.

### 1c. PHOTONICS — 36/39/42° aliasing risk vs `P_edge_A`/`P*`

Re-derived the actual numbers rather than trusting "5–7%":

- `|3.0 − 2.8421| / 2.8421 = 5.56%` (P_edge_A, exp-069)
- `|3.0 − 2.9474| / 2.9474 = 1.79%` (P*, exp-083's own **decisively
  resolved, full-power** Branch B period — T28's current best-determined
  confound signature, not a superseded candidate)

**PHOTONICS' own "5–7%" framing UNDERSTATES the risk for the more important
of the two periods.** A 3.0° step against a ~2.9474° period sits at 1.02
cycles per step — within 2% of exact n=1 resonant aliasing, the classic
strobe condition where a periodic signal, sampled near its own period,
reads as an almost-constant phase offset at every sample rather than as
oscillation. Three points spaced this close to a 1-cycle-per-step condition
of the program's own best-established confound period cannot distinguish
"real smooth oblique-incidence trend," "artificially flattened by aliasing
into false ENERGY-DECOUPLED," or "artificially smooth-looking but actually
riding a fixed alias phase" from each other.

On the specific rebuttal the task brief invites me to weigh — that
`i_inc`'s fixed-strip location (not itself angle-swept) makes this less
dangerous — **I find this rebuttal fails, and in fact cuts the other way.**
`REF=(OBJ_X,OBJ_Y,80)` is a location fixed in space, observed under a
*swept incidence angle*, in the *empty* run (§0, confirmed from source).
That is **structurally identical** to how T28's periodicity itself was
originally discovered and is still characterized: exp-069's/exp-083's
Weber-contrast measurements are also taken at one fixed downstream
location while θ is swept on an otherwise-empty-or-near-empty scene
(Iteration 60's own Phase-5 finding: "`P_edge_A` was originally measured
on the EMPTY scene" — `experiments/069-...`'s `run.py` has zero article
calls). "Fixed location, swept angle" is the exact experimental shape that
already produces this family of periodicity elsewhere in this program's
own record — it is not evidence of immunity, it is evidence of exposure.
There is no physical reason the near-object region at `x=OBJ_X` would be
uniquely exempt from a swept-angle interference/edge-diffraction artifact
that this program's own nine-cycle T28 sub-thread has shown is present,
in some form, essentially everywhere downstream of the source aperture.

**Verdict on PHOTONICS' critique: CONFIRMED, and independently
strengthened (not overstated).** The specific numeric framing understates
its own strongest case; the proposed rebuttal path (fixed REF location)
does not hold up under direct sourcing of how the fixed-location/swept-
angle idiom has behaved before in this exact program.

### 1d. MATERIALS — two provisional inputs compounding into P6

Read `lab/thermo_sidecar.py::mixed_length_scale_regime` directly. Its own
docstring states the chain explicitly: `p_abs_w` is passed through
UNCHANGED from "whatever an UPSTREAM optical measurement produced it as"
(here: `absorbed_power_established_ratio`, fed by this cycle's own
first-of-its-kind oblique/PAD-shifted `sigma_ext_cells`/`ratio_abs_ext`),
while `h_eff`/mass/area derive from `l_geometric_m` under silicon
`(ρ, c_p)` explicitly tagged `"material_provenance": "ASSUMED --
provenance terminates unsourced (T18)"`. Both inputs are real,
independently disclosed (Idealization 4 for the material identity; nothing
names the pairing), and MATERIALS is correct that nothing pre-registers
how a flip in P6 would be triaged between "genuine new oblique physics"
and "material-constant-swing artifact."

Independently verified the cited historical swing magnitudes rather than
trusting them: LOGBOOK confirms **Bi≈1.76×10⁻⁴, "~780× smaller"** (Iteration
22/exp-045's Biot correction) and **"~116× LARGER, the opposite direction"**
(Iteration 34/exp-057's own H_CONV fix) — both real, both load-bearing
material-identity-driven swings in this exact thermal chain, both
comfortably capable of moving a number by more than the "~2 orders of
magnitude" P6 sets as its own falsification bar. MATERIALS' point is not
that P6's band is wrong today (699× margin is real headroom) — it is that
nothing here commits, in advance, to checking a future flip against these
already-measured swing magnitudes before crediting it as new physics. This
is R9's commensurability discipline, applied prospectively to a
compounding-uncertainty gap rather than retrospectively to a unit mismatch.

**Verdict on MATERIALS' critique: CONFIRMED.** Real, correctly scoped
(MATERIALS itself notes P6's fallback margin is "wide enough today"), not
overstated, cheap to fix (one triage sentence, pre-committed before the
run).

### 1e. VISION — Idealization 10 is the affirmative constraint-3 seam

Re-read Idealization 10 verbatim: "This cross-check bears only on T28's own
confound-mechanism question and **constraint-3's energy-ledger
bookkeeping**. It does not test constraints 1/2/4, and does not re-open or
re-score `REALIZABILITY_MEMO.md`'s verdict." **Confirmed exactly as VISION
states**: constraint 3 is the one constraint named affirmatively rather
than placed in the exclusion list, and PANEL.md's own Metrics table lists
the absorbed-energy ledger as its own row, distinct from the constraint-3
Weber-contrast row — so the affirmative language is, today, technically
accurate, not an overclaim.

VISION's own cited precedent is real and on-point: T16 (Iteration 53, "24×
C_thr") and R12/exp-086's Iteration-63 "Learned section had silently
widened... to an unqualified claim" are both genuine, independently
recorded instances (confirmed above in §LOGBOOK reading) of exactly this
failure shape — a scoped, disclaimer-qualified finding surviving one
document's own frozen text but losing its qualifier in later Phase-3/5
prose. This is not a hypothetical risk manufactured for this cycle; it is
a twice-realized pattern on this exact sub-thread.

**Verdict on VISION's critique: CONFIRMED**, tagged as a forward risk
rather than an already-realized violation — correctly framed by VISION
itself ("the defect isn't here yet, but the seam that produced it twice
before is").

### Duplicate check

All five critiques attack five structurally different failure points
(instrument-identity verification gap; classification-scheme vacuity at a
boundary case; angle-lattice aliasing risk; compounding-uncertainty
non-disclosure; scope-language seam). **Zero overlap** — matching this
sub-thread's own recent precedent (exp-086 Phase 2: "five DIFFERENT
defects, zero overlap") and, read positively, evidence the five-seat blind
layer is functioning as designed rather than converging on the one most
visible issue.

---

## 2. Independent Red Team findings (not raised by any of the five critiques)

**Attack 6 — settling of the NEW `widths()`-derived channel is
unverified, contradicting this program's own R3 meta-rule.**
`[inconsistency]`

Idealization 7 admits: "Settling is NOT independently re-verified for the
`widths()`-derived channel specifically ... this cycle inherits [STEPS=2800]
settling evidence [from] the Weber-contrast phasor channel ... rather than
running a dedicated STEPS=1400-vs-2800 spot-check on `sigma_abs`/
`sigma_ext` themselves." This is true and disclosed, but it is inconsistent
with R3's own standing meta-rule ("any surprising feature gets a resolution
check before it gets a mechanism debate — and 'artifact' claims need the
check too") and with this program's own settling-precondition discipline,
which it otherwise follows scrupulously everywhere the box/channel
combination is new (exp-076's HALT-if-fails settling precondition when
`G40`'s geometry was first decoupled; exp-083's own settling spot-check at
`STEPS=1400` vs `2800`, disclosed-not-gating, run anyway). Both prior
instances treat "same underlying `full_capture`/`phasors` primitive" as
grounds to *check cheaply*, not grounds to *skip*. A Poynting-box flux
integral taken near the object (`BOX_A` sits close to the source relative
to the far-downstream ambient plane) can plausibly settle on a different
timescale than a downstream contrast window — this is exactly the kind of
"looks like the same physics, might not be" situation R3 exists for, and
it is untested here. Idealization 7 itself flags this as "a plausible
mandatory-fix candidate for Phase 2/3" — I am accepting that invitation.

**Attack 7 — the P4/P9 "informal T9 comparison" and P6's fallback both
quietly assume the just-measured `sigma_ext(BOX_A)` is itself trustworthy,
which is the same unverified premise as Attack 1/EM's finding.**
`[inconsistency]`

Not a new defect — a scope note. P4's "genuine uncertainty" framing and
P6's "699× margin" both implicitly treat this cycle's own freshly-measured
`sigma_ext_cells(cfg,θ,BOX_A)` as reliable. Once EM's fix (Attack 1) is
adopted, this is resolved as a side effect — flagged here only so Phase 3
does not treat P4/P6 as independent of the `xi_ext` gate.

---

## 3. Numbered attack list (final, tagged)

1. **[inconsistency]** The proposal claims to reuse "already-stage-8-gated"
   `sections.widths()` machinery as grounds for trust, but the specific
   identity that machinery's own docstring calls load-bearing
   ("extinction... two independent routes... must agree") has never been
   exercised on `graded_black_shell` at any angle, nor on any absorbing
   object obliquely — exactly the combination this cycle is first to run.
   The word "gated" is doing more work in the proposal's own §1/§6 framing
   than the suite's actual coverage supports. (EM, §1a above — CONFIRMED.)

2. **[inconsistency]** §4-P5's four classification categories are not
   mutually exclusive at 0 resolved angles (ENERGY-DECOUPLED and CONSISTENT
   are both vacuously true over an empty set), and §7's "regardless of
   which classification... the data return" language does not name this
   case, creating a route by which a fully degenerate, uninformative
   3-for-3-UNRESOLVED run could be filed as a completed, credited
   discharge indistinguishable in the record from a real finding. (QUANTUM,
   §1b above — CONFIRMED.)

3. **[unfalsifiable]** The {36°,39°,42°} angle grid is spaced at 3.0°,
   1.02 cycles of `P*=2.9474°` (exp-083's own decisively-resolved dominant
   T28 confound period) per step — within 1.8% of exact n=1 aliasing. As
   designed, a smooth or flat `frac_p_abs(θ)` reading at these 3 points
   cannot be distinguished from a real absence of θ-dependence, because
   the instrument is positioned almost exactly where it would ALSO read
   smooth/flat if the known confound artifact rides along at this box/REF
   location (see §1c — the "fixed location" rebuttal does not hold once
   sourced). P5's classification is not falsifiable against this specific
   alternative at n=3 on this lattice. (PHOTONICS, §1c above — CONFIRMED,
   strengthened.)

4. **[inconsistency]** Idealization 4 discloses the silicon thermal
   identity as ASSUMED, but nothing discloses that P6 is simultaneously
   fed by that ASSUMED identity AND a first-of-its-kind, not-yet-
   cross-validated (pending Attack 1's fix) oblique absorbed-power
   reading — two independent, compounding sources of uncertainty entering
   one "PRIMARY, pre-registered, falsifiable" NETD verdict with no stated
   plan for triaging a future flip between them. (MATERIALS, §1d above —
   CONFIRMED.)

5. **[constraint-3-violation, forward risk]** Idealization 10 is the one
   place this document names constraint 3 affirmatively rather than
   excluding it — accurate today, but the identical linguistic seam
   ("bears on constraint-3's bookkeeping" → paraphrased, in a later
   document, into "addresses constraint 3") has already produced two
   confirmed permanent-record errors on this exact sub-thread (T16/
   Iteration 53; R12/Iteration 63's Learned-section widening). Nothing in
   the current text prevents a third instance unless the disclaimer
   travels with every restatement. (VISION, §1e above — CONFIRMED.)

6. **[inconsistency]** The `widths()`-derived `sigma_abs`/`sigma_ext`
   channel's own settling behavior at `STEPS=2800` has never been
   independently spot-checked (Idealization 7's own admission) —
   inconsistent with this program's own R3 meta-rule and its own settling-
   precondition discipline applied everywhere else a box/channel
   combination is new. (Red Team, §2 above — new finding.)

---

## 4. Verdict: **PROCEED-WITH-MANDATORY-FIXES**

Nothing found here is fatal to the measurement, reveals an unfalsifiable
mechanism claim (there is no mechanism claim — Checkpoint criterion 2 is
correctly N/A), or reveals an *already-realized* quiet constraint-3
violation. But two of the six attacks (1 and 3) are directly load-bearing
on the PRIMARY pre-registered metric (P5) and must be closed before any
FDTD call, not disclosed-and-deferred: as filed, a favorable-looking
ENERGY-DECOUPLED result at 3 aliasing-adjacent points, computed from a
never-validated extinction identity, would not be distinguishable from two
different known artifacts, and this program's own R8 standard ("an
unverified argument about a flagged gap is not sufficient to file it
non-blocking when an affordable check exists") applies to both directly.
HALT is not warranted: every fix below is cheap (mostly zero marginal FDTD
calls) and none requires abandoning the measurement's own design.

---

## 5. Mandatory-fix docket for Phase 3 (prioritized, numbered)

**Tier 0 — before any FDTD call, changes the plan's own inputs/gates:**

1. **Add the `xi_ext` verification gate** (EM's fix). For both configs,
   both legs, at `BOX_A` (and `BOX_B`, per item 8 below): compute
   `xi_ext(cfg,θ,leg) = |sigma_ext_cross − sigma_ext| / |sigma_ext|` — zero
   marginal FDTD cost, `widths()` already returns `sigma_ext_cross`. HALT
   before computing any P5 classification unless `xi_ext ≤ 0.12` at every
   cell (reusing stage 8's own PEC tolerance, not inventing a new number).
2. **Break the aliasing lattice.** Replace {36.0°, 38.6°, 41.8°} for
   {36.0°, 39.0°, 42.0°}, or add a 4th point off the ~2.84–2.95° lattice,
   before running (PHOTONICS' flip-parameter, independently confirmed
   necessary — the current spacing sits within 1.8% of exact aliasing
   against `P*`, tighter than first estimated).
3. **Pre-register the 0/1-resolved-angle disposition explicitly.** State
   in §4 that 0 (and, if it occurs, 1) resolved angles must be reported as
   a degenerate/non-informative outcome, not folded into "regardless of
   classification" language — that phrase should be scoped to the four
   named classification outcomes only (QUANTUM's fix (a)).
4. **Add a minimal synthetic recovery check on the classification
   pipeline** before trusting the noise-floor gate or the 4-bucket scheme
   at n=3: inject synthetic `frac_p_abs`/`frac_contrast` pairs at the
   decade-boundary values (0.1, 1, 10) and confirm the pipeline recovers
   the correct bucket (QUANTUM's fix (b) — in the R5/R10 "demonstrate a
   threshold classifier's own discriminating power before trusting it"
   lineage).
5. **Run (or explicitly elevate) a settling spot-check on the new
   channel.** Either add one cheap `STEPS=1400` vs `2800` comparison of
   `sigma_abs`/`sigma_ext` at one (cfg,θ,box) cell (mirrors exp-083's own
   disclosed-not-gating settling idiom), or explicitly promote
   Idealization 7 from a bare list item to a named, disclosed, reported-
   alongside-P5 caveat — do not leave a "PRIMARY, pre-registered,
   falsifiable" verdict resting on unverified settling with no visible
   flag at the point where P5 is read.

**Tier 1 — cheap disclosure/framing fixes, no new FDTD:**

6. **Pre-commit a triage rule for a P6 flip.** State, before running: if
   P6 ever departs from UNDETECTABLE, that departure must first be checked
   against this program's own already-measured material-identity swing
   magnitudes (~780× Biot, Iteration 22; ~116× H_CONV, Iteration 34)
   before being read as new oblique physics rather than a compounding
   ASSUMED-constant artifact (MATERIALS' fix).
7. **Add the one-line non-negativity assertion**: `sigma_abs ≥ 0` and
   `p_abs_w ≥ 0` at every (cfg, θ, box, leg) cell — trivial by passivity,
   costs nothing, catches a sign/phasor-convention bug for free (EM's
   supporting-detail fix).
8. **Carry idealization 9's NETD disclaimer and idealization 10's "does
   not test constraint 3" framing verbatim, inline, at every restatement**
   of P6/constraint-3 language in `NOTES.md` and any Phase-3/5 prose — not
   filed once in frozen Phase-1 text and then compressed later (VISION's
   fix, matching the T16/R12 precedent this exact seat has caught twice).

**Tier 2 — record completeness, does not gate the run:**

9. Report `box_dev_ext`/`box_dev_abs` AND `xi_ext` at both `BOX_A` and
   `BOX_B` (not `BOX_A` only) so a future reviewer can separate
   spatial-placement noise from route-disagreement noise cleanly.
10. When P5's outcome is filed, explicitly log whether the observed
    `frac_p_abs(θ)`/`frac_contrast(θ)` curve sits inside or outside the
    aliasing risk band named in fix 2 — so a future reviewer does not have
    to re-derive Attack 3 from scratch to assess this run's own exposure.

**Standing forward tripwire, named explicitly for Phase 5:** if fixes 1
and/or 2 are not adopted and either the extinction-routes disagreement or
the aliasing risk later proves outcome-determining for P5's classification,
that matches this program's own established R8 firing shape (an affordable,
already-named check not run before a headline verdict is trusted) and
should fire Checkpoint criterion 4, not be weighed as a close call.
