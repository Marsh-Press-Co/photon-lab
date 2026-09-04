# PHASE 5 — RED TEAM FINAL AUDIT · Panel Iteration 88 (exp-111)
## The Cost-Gate Reposition and Floor Fault-Injection Cycle: All Four Convergent Findings Independently Re-Verified From Primitives, One New R23 Addendum, Zero Checkpoint Firings

Charter (verbatim, PANEL.md): attacks every proposal, speaks last and
hardest. Standard is NOT textbook-physics compliance. Kills internal
inconsistency, unfalsifiable claims, mechanisms that cannot be expressed
as simulation parameters, and proposals that quietly violate a target
constraint — especially #3. Never leads a cycle.

## 0. Framing and method

Read, in full: PANEL.md; LOGBOOK.md's Ruled-Out registry (R1–R28) and the
Iteration-85/86/87 (exp-108/109/110) narrative entries; the complete
exp-111 record (`phase1_proposal.md`, all five Phase-2 blind critiques,
`phase2_redteam_audit.md`, `NOTES.md`, `results.json`); and, unlike the six
blind Phase-5 reviewers, all six of their reviews
(`phase5_review_{photonics,materials,em,quantum,vision,thermodynamics}.md`).
Then re-verified from primitives — actually ran Python against the
committed code, never trusted a review's own prose — the four most
consequential findings the six reviews converged on, per this cycle's own
task charter, applying R4/R4-Third-Addendum's "independently re-derive,
don't re-quote" discipline to the six reviews' own claims as well as to
NOTES.md's.

**Verdict on method, stated up front**: every one of the four target
findings holds up. Two are, if anything, UNDERSTATED by the reviews that
found them (see §2, §3). No review's own claim needed correcting. This is
an unusually clean six-way (plus this audit's own, seven-way) convergence.

## 1. Finding 1 — NOTES.md's Phase-3 disposition table's "both assert `DISCLAIMER_88 in ...`" claim is false

**Independently re-verified, confirmed false as MATERIALS, PHOTONICS,
VISION, and THERMODYNAMICS each found.** `grep -n "assert"` against the
committed `predictions_result_88.py`, as shipped at Phase 4, returns
exactly one hit: line 180, inside `if "--predictions-only" in sys.argv`,
covering only `predictions_text`. `build_result_text_88()` contained no
assert anywhere, and no committed script anywhere in the exp-111 directory
called it with real data. Directly executed: calling
`build_result_text_88(fi, gate, formula, cpl)` with the four real
committed `*_output.json` files and no `wall_time_source` produces a
string that does NOT match `results.json["result_text"]` (missing one
line); supplying the exact `wall_time_source` string embedded in the
persisted text reproduces it byte-for-byte. So the content is genuine and
correct — but it was produced by an invocation this session never captured
as committed, re-runnable code, and the "both assert" claim itself is
false.

## 2. Finding 2 — NOTES.md's Result section is not a byte-exact "verbatim quote" (VISION's finding, UNDERSTATED, not overstated)

**Independently re-verified by full diff, confirmed — and the deviation is
larger than a first read of VISION's own review suggests.** Extracted the
exact block between `RESULT (exp-111, Panel Iteration 88)` and
`### Interpretation` from the frozen `NOTES.md`, called
`build_result_text_88()` with the real four `*_output.json` files and the
correct `wall_time_source`, and diffed byte-for-byte. Two substantive
sentences appear in NOTES.md's own "verbatim quote" that the function
itself never generates anywhere in its f-string: Item 1's "but at 2 of the
24 swept phases (0°, 180°) the pooled floor reads *exactly* `0.0`, not
merely small" (itself a claim this audit finds is factually WRONG at
180° — see §3), and Item 3's "(was hand-typed as '~6.5h' in
`phase1_proposal.md` — that figure was the r=312-alone column's own value,
misplaced; corrected here per mandatory fix 4)". Every other line differs
in formatting only (backticks, em-dashes, re-wrapped line breaks — an
artifact of `build_result_text_88`'s own f-string layout, e.g.
`calls=\n{...}`, being re-wrapped for prose readability by hand). VISION's
own review states this correctly; this audit's own contribution is
confirming the diff a second, independent way and noting that one of the
two added sentences is not merely "an accurate addition" but an
independently-false one (§3) — meaning the hand-edited Result section
introduced a NEW error the function's own real output does not carry, not
only prose the function omits.

## 3. Finding 3 — the `floor<=0.0` guard is not floating-point-robust, and NOTES.md's own "exactly 0.0 at 180°" claim is itself false

**Both halves independently re-verified from scratch; both hold.**

**3a. The guard.** `classify_item_i_local()`'s `floor_degenerate =
bool(floor <= 0.0)` is a bit-exact-zero test. Constructed, independently
of QUANTUM's own review, two realistic-magnitude (`~3e-3`) synthetic
patterns whose asymmetric content sits near this bench's own
antisymmetric-canceling phase:

```
floor = 5.854691731421724e-18
floor_degenerate = False
n_resolved = 48 / 48   (every bin marked resolved)
local_snr_peccored (sample): 7.7e14, 9.1e14, 8.6e14, 7.8e14, 9.4e14 ...
```

`floor_degenerate` reads `False` (wrong — this floor is floating-point
noise, not a measurement), every bin reads `resolved=True` (wrong, for the
same reason), and `local_snr` reports physically-meaningless values in the
`10^14`–`10^15` range. No `inf` is produced (mandatory fix 3's own literal
target is genuinely closed — confirmed, swept synthetic amplitude down to
`5e-300` at the same phase and never produced one), but a "confidently
resolved, high-SNR" reading built on a floor that IS floating-point noise
is just as substantively wrong. This is a direct instance of R13's own
established concern (LOGBOOK RULED OUT registry: "a ratio classifier
whose denominator is built from a quantity independently known... to have
real zero-crossings must be floor-gated on that quantity's own absolute
or amplitude-normalized magnitude — not merely on the numerator's own
measurement-noise floor") — here the `floor` value itself, used as
`local_snr`'s own denominator, needed exactly this kind of magnitude-based
gate and did not get one; a bit-exact `<=0.0` test is the naive shape R13
already exists to warn against. Does not fire on any of the 12 real
committed cells (all floors five-plus orders of magnitude clear of this
danger zone, independently re-confirmed) — matching R13's own "does not
retroactively violate itself on data that has never triggered it"
precedent.

**3b. NOTES.md's own numeric claim.** Directly re-ran
`mirror_pooled_floor()` at exactly phase=0° and phase=180° of FI-D's own
construction:

```
phase=0.0    -> floor = 0.0                       (bit-exact)
phase=180.0  -> floor = 1.951563910473908e-18      (NOT bit-exact zero)
```

NOTES.md's Interpretation states "the pooled floor reads exactly `0.0`...
at swept phases 0° and 180°" — true at 0°, **false at 180°** by
`~1.95e-18`. Mechanism: `deg2rad(0)=0.0` exactly, so `cos(θ_i)` and
`cos(-θ_i)` are bit-identical by construction; `deg2rad(180)=π`, only
approximately representable in IEEE-754, so `cos(-θ_i+2π)` is computed via
an argument-reduction step that is mathematically exact but not bit-exact
— a genuine, reproducible floating-point residual, not a mathematical
near-miss. Non-outcome-reversing (the code's own `never_exactly_zero`
check already uses a `1e-12` tolerance, so both a bit-exact `0.0` and
`1.95e-18` read identically there — FI-D's own filed FAIL is unaffected)
but a genuine R4-class defect (a claimed-exact figure that does not
reproduce from its own cited source) in the Director's own Phase-4 prose,
independently confirmed, and — notably — this residual is not an isolated
curiosity: it is the SAME magnitude-class quantity §3a's adversarial
construction demonstrates the production guard is not robust to. Fed
directly into `classify_item_i_local` at realistic pattern magnitudes,
this exact 180°-phase residual (or one of the same scale) is precisely
what produces the `floor_degenerate=False`/`local_snr~1e14` misclassification
in §3a — the documentation slip and the guard's own non-robustness are two
views of the identical floating-point fact, not two unrelated findings.

## 4. Finding 4 — `gate_reposition_control.py`'s five cases test only the fresh-build branch; the resume branch is independently confirmed correct but untested

**Independently re-verified by direct execution, confirmed exactly, including EM's own claim that the causal property holds on resume.**

`step_once`'s real control flow, read directly:
```
if os.path.exists(done_path): return True                    # early exit
if r == 312: check_cost_gate_for_312()                        # the gate
if os.path.exists(ckpt_path):
    sim = state["sim"]            # RESUME -- build_sim NEVER called
else:
    sim = build_sim(g, which)     # FRESH -- the only path the control tests
sim.run(chunk)
```
All 5 of `gate_reposition_control.py`'s own cases call `fresh_scratch()`
and never write a `ckpt_path` for r=312 — confirmed by direct source read
of every `setup_fn`. `STEPS(312) = round(3200 · kappa_of(312)) =
round(3200·4.0) = 12800`; `CHUNK_STEPS=2200` ⟹ 6 chunks per r=312 scene
(1 fresh + 5 resume). **In the real, already-completed exp-110 r=312
capture, 5 of every 6 real `Sim.run()` calls per r=312 scene went through
the untested resume branch** — independently confirmed by this same
arithmetic, matching EM's own figure exactly.

Constructed the missing case directly (a standalone probe, not a
committed-control edit): wrote favorable r=156 done-markers/wall-time
logs, wrote a checkpoint (`ckpt_path`) for r=312/"empty" holding a stub
`sim` object whose own `.run()` raises a sentinel the instant it is
called, and ran the real, unmodified `chunk_runner.step_once(312,
"empty")`:

```
[empty r=312] resumed at steps_done=2200
RuntimeError: REAL_SIM_RUN_REACHED_ok        (only after the gate check ran)
```

Then repeated with r=156 markers absent (unfavorable precondition), same
resumed checkpoint:
```
RuntimeError: cost gate: r=156/empty not complete -- cannot evaluate cost_gate_check() before r=312.
```
(the sentinel `.run()` was never reached). **The underlying causal
property genuinely holds on the resume branch too** — `check_cost_gate_
for_312()` sits unconditionally between the done-check and the
fresh/resume split, so it fires identically regardless of which branch
`step_once` is about to take. Mandatory fix 1's own claim ("genuinely
upstream of every real r=312 `Sim.run()` call") is true in full. But the
committed control — the thing whose whole purpose is to prove this,
R28-style, by execution rather than by reading the `if`/`else` structure —
covers only the branch that is NOT where 5/6 of the real spend happens.
This is precisely the shape R28 itself was founded to retire (a claim
resting on structural reading rather than full executed tracing),
recurring one branch deeper, non-outcome-reversing here only because this
audit checked it and it happens to hold.

## 5. THERMODYNAMICS' own closed-form claim (FI-D's "aliased regime" framing) — independently re-derived, confirmed exactly

Writing `θ_i = 2π·BIN_CENTERS_DEG[i]/P*`, and using
`BIN_CENTERS_DEG[i] == -BIN_CENTERS_DEG[47-i]` (confirmed exactly for all
48 bins, zero violations):

```
arr(i) - arr(47-i) = -2 · amplitude · sin(phase) · sin(θ_i)
```

Independently re-derived from `cos(A+B)-cos(A-B) = -2 sin A sin B` and
confirmed numerically against the actual constructed array (max abs
deviation from the closed form ≈ `5.2e-18`, pure floating-point roundoff —
the formula is exact). **This vanishes identically across every bin pair
iff `sin(phase)=0` (`phase=0°` or `180°`), completely independently of
`P*`.** Re-ran FI-D's own construction at four periods other than T28's
own `P*=2.8421°` (`5°`, `13.37°`, `100°`, `3°`): the exact/near-exact-zero
collapse at `phase=0°/180°` occurs in EVERY case tested, with the
`phase=180°` residual scaling only with floating-point noise, not with
`P*`. **THERMODYNAMICS' finding holds exactly**: NOTES.md's own framing of
FI-D as characterizing "the realistic aliased/intermediate regime"
(implying a T28-`P*`-specific aliasing interaction with the 7.5°-bin
instrument) is misleading — the phase-0°/180° collapse is a generic
property of testing ANY single pure cosine, of any period, on this
mirror-symmetric bin grid. The genuinely T28-specific content is confined
to the shape of the recovery curve at the OTHER 22/24 swept phases, not
the mere existence of the two blind phases.

## 6. Classifying the findings against R1–R28 — novel, or an instance of an existing rule?

Checked each finding, individually, against the full RULED OUT registry
text (not a summary), per this cycle's own charter instruction.

- **Finding 1** (the "both assert" claim): this is a claim that a
  mandatory fix ("wire predictions/result text... re-fire `assert
  DISCLAIMER in ...`") was "Implemented as: ...both assert" in a frozen
  Phase-3 disposition table, which turns out false for one of two sibling
  functions. Structurally, this is **R23's own "predictions half done,
  result half not" sub-shape**, recurring a SECOND time on this document
  family (first instance: Iteration 85/exp-108, VISION's finding there,
  where `build_result_text()` had ZERO call sites and ZERO asserts at
  all; fully closed and byte-verified at Iteration 86/exp-109) — now on a
  NEW, cycle-specific successor string (`DISCLAIMER_88`), one cycle after
  the original string's own symmetry was independently confirmed. It is
  **not** R4/R20-class in the strict sense those rules define (a
  claimed-exact FIGURE, CITATION, LABEL, or COINCIDENCE failing to
  reproduce) — it is a claim about code SCOPE (does an assert exist),
  closer kin to R18 (a check's claimed scope vs. its actual source) and,
  more precisely, to R23 itself. See §7 for the ruling on whether R23's
  own "no forward-elevating clause" text still holds given this second
  instance.
- **Finding 2** (Result section not byte-exact "verbatim quote"): this
  IS clean R4-class — "a claimed... quote... that does not reproduce
  from its own cited source," matching R4's own founding concern
  (exp-048's "precisely recomputed" figures that were never actually
  invoked) almost exactly, one document-genre over (a full text block,
  not a numeric figure).
- **Finding 3b** (NOTES.md's "exactly 0.0 at 180°" claim): also clean
  R4-class — "a claimed-exact figure... that does not reproduce from its
  own cited source" is a literal description of this defect. QUANTUM's
  own review independently names it this way too.
- **Finding 3a** (the `floor<=0.0` guard's own non-robustness): this is
  **not** R4-class (nothing is mis-cited; the code genuinely does what
  its own docstring says, on a bit-exact-comparison reading) — it is a
  **direct instance of R13's own established principle** (a
  ratio-classifier denominator needing a magnitude-based, not
  bit-exact, floor gate), applied one level deeper than R13's own
  founding instance (there, `ratio_k`'s denominator itself; here, `floor`
  as `local_snr`'s own denominator). Genuinely a fresh technical
  instance of an EXISTING rule, not a new failure category.
- **Finding 4** (`gate_reposition_control.py`'s fresh-branch-only
  coverage): this is a **direct instance of R18's own established
  pattern** (a check's documented/claimed scope not matching its actual
  source-code coverage; a check joining an already-partially-verified
  layered architecture — here, R27/R28's own — needing its own
  fault-injection control in the SAME cycle it is added). LOGBOOK's own
  record shows this exact R18 shape recurring repeatedly across this
  T28 sub-thread (exp-096 founding; exp-097, "one cycle inside R18's own
  founding discipline"; exp-108's own Iteration-85 finding) without ever
  escalating to a forward-elevating clause or firing Checkpoint 4 — each
  instance caught blind, same-cycle, and fixed. This cycle's instance
  matches that established, non-escalating precedent exactly.

## 7. Does R23's own "no forward-elevating clause" ruling still hold? Does R20's "three or more" density test fire?

**R23's own text, re-read directly (LOGBOOK.md RULED OUT registry, full
entry)**: the rule requires a code-level assert on a single
source-of-truth string; it carries **no three-strike/forward-elevating
clause of its own**, unlike R16/R21/R22/R24/R25/R26/R27/R28. This cycle's
own Phase-2 Red Team audit already established this correctly (§1, that
document, re-reading R23's own ratified text directly rather than
assuming it) — for the scenario THAT audit considered (a proposal
shipping with ZERO `DISCLAIMER`/R23 machinery at all, the "third silence
instance" question). **This audit's own finding is a different scenario**:
the machinery WAS shipped, but asymmetrically — the specific "predictions
half done, result half not" sub-shape, now on its second real-world
instance (exp-108, exp-111). Re-reading R23's ratified text again, with
THIS specific scenario in mind: it still carries no forward-elevating
clause covering ANY sub-shape of its own violation, including this one.
**Ruling: R23's own "no forward-elevating clause" finding still holds in
full** — a second instance of the predictions/result assert-asymmetry
sub-shape does not, on any rule currently on the books, automatically
fire Checkpoint criterion 4.

**R20's "three or more independent R4-class defects in one document"
test**: R20's own text requires DISTINCT R4-class defects (a claimed
figure/citation/label/coincidence failing to reproduce), not a count of
REVIEWING SEATS that independently caught the same one — four seats
converging on Finding 1 strengthens confidence the defect is real; it
does not multiply the defect count, exactly as this program's own R4
lineage has always treated multi-seat convergence (e.g. Iteration 51's
"two of five... independently... restated the identical false figure" was
counted as ONE recurring instance of a shape, not two). Tallying
STRICTLY DISTINCT R4-class defects in this document, each surviving
Phase-3/4 freeze and caught only at Phase 5:

1. Finding 2 (Result section not a byte-exact "verbatim quote").
2. Finding 3b (Interpretation's false "exactly 0.0 at 180°" claim).

That is **two**, not three. Two candidates for a third were considered
and explicitly rejected: (a) Finding 1 (the "both assert" claim) is ruled
R23-shaped, not R4-shaped, per §6, above — a claim about code SCOPE, not
a figure/citation/label/coincidence; (b) the FI-D "realistic aliased
regime" framing (§5) is ruled closer to R17's own shape (a
framing/emphasis issue needing equal weight given to an alternative
characterization, not a hard binary fact that either reproduces or
doesn't — the underlying MATH is correct; only the narrative EMPHASIS is
incomplete) than to R4/R20's shape (a specific claimed figure that is
simply wrong). **Ruling: R20's tally for this document is 2, one short
of "three or more" — does NOT fire.** This continues (not crosses) an
established pattern this exact governance sub-thread has now shown for
FOUR CONSECUTIVE cycles (exp-108 tally 2, exp-109 tally 2, exp-110 tally
2, exp-111 tally 2 by this audit's own count) — named explicitly here as
a standing observation, not itself a rule violation, since R20's bar is a
hard threshold, not a trend test. A future Red Team audit may wish to
consider whether four consecutive near-misses at the identical tally
warrants its own supplementary discipline; this audit does not ratify
one, reasoning that R20's own text is a deliberately hard density bar and
inventing a "trending toward 3" test would be exactly the kind of
inference-stretching this seat's charter exists to resist, not indulge.

## 8. A new rule: R23 First Addendum

Given Finding 1 is a genuine SECOND real-world instance of the specific
"predictions half asserted, result half not" sub-shape (Iteration
85/exp-108 first, fully closed and byte-verified at Iteration 86/exp-109,
now recurring at Iteration 88/exp-111 on a NEW successor disclaimer
string introduced this cycle) — and given R23 itself, unlike eight of its
siblings, carries no mechanism to escalate a recurrence of its own core
violation — this audit proposes and ratifies, per this program's own
established practice of a Phase-5 final audit proposing and adopting new
rules directly (matching R16/R17/R18/R19/R20/R21/R22/R26/R28's own
precedent):

**R23 First Addendum — a code-level assert satisfying R23 for one
disclaimer string does not transfer to a NEW disclaimer-successor string a
later cycle introduces; each new single-source-of-truth string must
independently ship BOTH the predictions-side and result-side assert,
verified via a committed, re-invocable call site — not an ad hoc,
uncaptured invocation — in the SAME cycle it is introduced, before a
Phase-3 disposition table may claim the pair is symmetric.** Founding
basis: Iteration 85/exp-108 (the original `DISCLAIMER` string's own
result-side assert was entirely absent) and Iteration 88/exp-111 (a NEW
`DISCLAIMER_88` string repeats the identical asymmetry, one level over,
despite the original string's own symmetry having been independently,
byte-exactly verified one cycle prior). **Does not fire on this, its own
consolidating instance** (exp-111), matching every prior rule's own
founding/consolidating-instance precedent in this registry — same-shift
fix applied directly, this audit (§9). **Standing forward-elevating
clause**: a THIRD instance of "predictions half asserted, result half
not," on this or any T28-adjacent channel, on any disclaimer string, in
any form, fires Checkpoint criterion 4 automatically, no further
deliberation — mirroring R16/R21/R22/R24/R26/R27/R28's own
single-instance-ratified, forward-firing convention.

No other new rule is warranted. Findings 3a and 4 are confirmed instances
of R13 and R18 respectively (§6) — genuinely new technical occurrences,
not new failure categories, and both match this sub-thread's own
established non-escalating precedent for their respective rule families
(R13: does not fire on data that has never triggered it; R18: recurs
routinely across this sub-thread without escalation, each instance caught
blind and fixed same-cycle or next-cycle).

## 9. Same-shift corrections (applied directly, this audit — zero re-run, zero verdict-arithmetic change)

1. `predictions_result_88.py`: `build_predictions_text_88()` and
   `build_result_text_88()` both now assert `DISCLAIMER_88 in text` INSIDE
   the function itself (fires on every real call, not conditioned on a
   specific script's own entry point).
2. `finalize_88.py` (new): loads the four real committed
   `*_output.json` control files, calls both builder functions with the
   real `wall_time_source`, asserts both disclaimers present, and verifies
   byte-for-byte reproduction of `results.json`'s own `predictions_text`/
   `result_text` fields (predictions modulo one harmless
   `print()`-appended trailing newline, VISION's own Phase-5 finding,
   independently re-confirmed) — `python3 finalize_88.py` passes, closing
   Finding 1 for good: a future reviewer can now reproduce
   `results.json["result_text"]` from committed code alone.
3. `NOTES.md`, mandatory-fix table row 5: blockquoted annotation
   disclosing the "both assert" claim is false as shipped, describing the
   fix above, and naming this as the R23 First Addendum's own consolidating
   instance.
4. `NOTES.md`, Result section heading: blockquoted annotation disclosing
   the "verbatim quote" claim is false (hand-edited, not a copy), pointing
   to `finalize_88.py` for the genuine reproducible path.
5. `NOTES.md`, Item 1 Result text: blockquoted annotation disclosing the
   `floor<=0.0` guard's own non-robustness (Finding 3a), with the
   adversarial reproduction and the R13 classification.
6. `NOTES.md`, Item 2 Result text: blockquoted annotation disclosing the
   untested checkpoint-resume branch (Finding 4), with the independent
   confirmation that the underlying causal property holds and the R18
   classification.
7. `NOTES.md`, Interpretation section: two blockquoted corrections —
   the "exactly 0.0 at 180°" claim corrected to `~1.95e-18` with the
   floating-point mechanism (Finding 3b); the FI-D "aliased regime"
   framing corrected with THERMODYNAMICS' own closed form and the
   multi-period reproduction (§5).
8. `NOTES.md`, Combined Verdict section: blockquoted Red Team ruling
   confirming PARTIAL unchanged, summarizing all four findings, the
   Checkpoint-criteria ruling (§10, below), and the trust-suite
   re-confirmation.
9. `NOTES.md`, Idealizations "Does establish" bullet: blockquoted
   annotation qualifying the "realistic aliased/phase-swept case" and
   "genuinely, verifiably upstream of every real r=312 `Sim.run()` call"
   language against §4/§5's own findings.
10. `NOTES.md`, Reconciled Iteration-89 queue: three new, explicitly
    numbered Tier-1 items (R25 discipline) — the sixth
    `gate_reposition_control.py` resume-branch case; the R13-style
    magnitude floor-gate hardening; a non-sinusoidal/multi-harmonic FI-D
    successor case — plus a new Tier-0 item asking the next cycle to rule
    on the R23 First Addendum proposed here.

Trust suite re-confirmed green after these patches: **43/43, 143s**
(current suite size; matches the count in place before this shift — zero
`lab/` diff, as this cycle's own T1/N/A scope requires). `git status`
confirms the diff is scoped to exactly `NOTES.md`,
`predictions_result_88.py`, and the new `finalize_88.py` — no other file
in this experiment directory or `experiments/110-.../` touched.

## 10. Checkpoint criteria — checked element-by-element against PANEL.md's own five-item list

1. **A configuration passes ALL constraint metrics** — N/A. This cycle is
   pure governance/instrumentation; T1 correctly N/A throughout, zero
   constraint-1/2/3/4 scoring touched.
2. **A proven boundary (constraint subset jointly unsatisfiable)** — N/A,
   same reason.
3. **A synthesis requires engine physics beyond validated bench classes**
   — N/A; zero `lab/` diff, confirmed by `git status` and the
   re-confirmed-green trust suite.
4. **Red Team flags program-integrity drift** — the specific question
   this audit exists to answer. Per §7, R20 does not fire (tally 2, one
   short); per §7/§8, R23 carries no forward-elevating clause and the new
   R23 First Addendum explicitly does not fire on its own consolidating
   instance; per §6, Findings 3a/4 are confirmed instances of R13/R18,
   both non-firing per established, unbroken precedent for those rules.
   **No Checkpoint criterion newly fires this cycle.** The STANDING,
   still-open Iteration-85 Checkpoint-4/R24 firing (LOGBOOK.md, that
   entry) remains unresolved, unchanged by anything in this cycle — this
   audit does not and cannot close it (Marsh's own ruling, explicitly out
   of scope for a Panel proposal, per NOTES.md's own Tier-0 item 0).
5. **Two consecutive iterations with no logbook-advancing result** — does
   not apply; this cycle lands a real, independently-verified upstream
   cost-gate reposition (mandatory fixes 1/2, R27/R28), a genuinely closed
   `inf`-self-contradiction (mandatory fix 3), a corrected cost-projection
   formula and table (mandatory fix 4), and four newly surfaced, now-fixed
   or now-queued gaps — real forward motion, not stagnation.

## 11. Combined Verdict

**PARTIAL** — unchanged from the Director's own working verdict and from
all six blind Phase-5 reviews' independently-landed CONFIRM-WITH-GAPS.
Not RULED OUT: T1 is correctly N/A throughout, confirmed structurally by
every reviewing layer including this one. Not PROMISING: this cycle's own
record, as filed at Phase 4, carried four real, independently-confirmed
gaps (two R4-class documentation defects; one R13-class guard-robustness
gap; one R18-class control-coverage gap) plus a genuine second instance
of an R23-adjacent sub-shape — none individually fatal, none reversing
any mandatory-fix PASS or touching constraint/T1 scoring, but denser than
a clean landing carries, and continuing this exact T28 governance
sub-thread's own well-established pattern (every cycle since Iteration 82
has landed PARTIAL). Real, disclosed, now-independently-seven-ways-
reproduced progress stands alongside the gaps: mandatory fixes 1/2/4 all
genuinely pass their own falsification criteria; the R27/R28 cost gate is
now genuinely repositioned upstream, confirmed by direct execution against
BOTH the fresh-build and checkpoint-resume branches (this audit going
beyond what the committed control itself proves); the `inf`
self-contradiction is genuinely closed; `finalize_88.py` now makes
`results.json`'s own two text fields genuinely reproducible from committed
code alone for the first time this cycle.

## 12. Reconciled Iteration-89 queue

**Tier 0** — (0a) rule on the Iteration-85 Checkpoint-4/R24 firing at the
next convened checkpoint (unchanged, still Marsh's call, still pending).
(0b, new this audit) ratify or reject the R23 First Addendum proposed in
§8 above.

**Tier 1** — newly-found gaps this cycle's own Phase-5 layer surfaced
(R25 discipline, numbered, not parenthetical): (1) add a sixth
`gate_reposition_control.py` case exercising the checkpoint-RESUME branch
directly (a pre-written `ckpt_path` for r=312, both a favorable and an
unfavorable r=156 state) — the underlying causal property is independently
confirmed to hold (§4, above), but the committed control itself still does
not prove it. (2) Harden `classify_item_i_local`'s own
`floor_degenerate`/`floor<=0.0` test from a bit-exact-zero comparison to
an amplitude/epsilon-scaled magnitude floor gate, per R13's own
established discipline — this cycle's own adversarial construction
demonstrates `floor≈5.85e-18` reads `floor_degenerate=False` and produces
`~1e14`-scale physically-meaningless "SNR" values (§3a). (3) A genuinely
non-sinusoidal or multi-harmonic FI-D-style perturbation (PHOTONICS' own
original Phase-2 request) — a single pure cosine can never escape
periodically revisiting FI-A/FI-B's own two clean extremes, at any period
(§5); this remains the untested, genuinely more informative probe of the
"neither clean odd nor even" regime. **(Carried forward from exp-110's own
queue, unexecuted twice now)**: (4) Execute item 3 (PHOTONICS' own
independent, non-differencing floor check, a `cpl`-refinement spot check)
at the two named bins, protected by this cycle's own repositioned,
safety-margined cost gate — start with `cpl=25`, r=156-alone-first (~24.5
min, per the regenerated `cpl_cost_table.py`); genuine new FDTD, correctly
deferred twice now, should not be deferred a third time without new,
equally explicit reasoning. (5) The long-outstanding
`R2_SMOOTH_THRESHOLD=0.90` re-derivation (now a fifth consecutive cycle
naming it undone). (6) MATERIALS' own fabrication-tolerance quantitative
bound (now a fourth consecutive cycle naming it undone).

**Tier 2** — a full per-margin item-1c/1d Result-section table (still
outstanding, Iteration-87 Tier 2 item 3); `CLOSURE_CONFIRM`/
`CLOSURE_FALSIFY` dead-code cleanup (Iteration-87 Tier 2 item 4); a fourth
r-point (r=624) — requires re-deriving/re-validating
`KAPPA_COST_EXPONENT`/`COST_GATE_SAFETY_MARGIN` at a new `kappa_ratio`,
not assuming they transfer (this cycle's own Idealizations).

**Tier 3 — unchanged standing items**: the oblique-angle extension; the
750/450nm leg; the `G40` full-width leg; the x-wall admittance refit;
`PAD`-with-article survival; `box_dev`'s own thinning margin (~9.0× at
r=312, still unresolved).

## 13. Summary table — the four target findings, this audit's own independent re-verification

| # | Finding (seat) | Independently re-verified? | Classification | Fires anything? |
|---|---|---|---|---|
| 1 | "Both assert `DISCLAIMER_88`" is false (MATERIALS/PHOTONICS/VISION/THERMODYNAMICS) | **CONFIRMED** — exactly 1 assert exists, `build_result_text_88()` has none | R23's own "predictions/result asymmetry" sub-shape, 2nd instance | R23 alone: no. New **R23 First Addendum** ratified this audit: does not fire on its own consolidating instance; 3rd instance auto-fires Checkpoint 4 forward |
| 2 | Result section not byte-exact "verbatim quote" (VISION) | **CONFIRMED**, understated — one added sentence is itself independently false | Clean R4-class | R20 tally +1 (of 2 total) |
| 3a | `floor<=0.0` guard not FP-robust (QUANTUM) | **CONFIRMED** — `floor≈5.85e-18` → `floor_degenerate=False`, `local_snr~1e14` | Instance of R13 | R13: no (no real cell triggers it) |
| 3b | NOTES.md's "exactly 0.0 at 180°" claim (QUANTUM) | **CONFIRMED false** — actual value `1.9516e-18` | Clean R4-class | R20 tally +1 (of 2 total) |
| 4 | `gate_reposition_control.py` tests fresh branch only, never resume (EM) | **CONFIRMED**; causal property independently confirmed to hold on resume too | Instance of R18 | R18: no (matches this sub-thread's own non-escalating precedent) |
| 5 | FI-D "aliased regime" framing is P*-independent (THERMODYNAMICS) | **CONFIRMED exactly** — closed form `-2·amplitude·sin(phase)·sin(θ_i)`, reproduced at 4 other periods | R17-adjacent framing issue, not R4/R20 | None |

**R20 tally: 2 of 3 required — does NOT fire.** **Checkpoint criterion 4:
does NOT fire.** **Combined Verdict: PARTIAL, unchanged.**
