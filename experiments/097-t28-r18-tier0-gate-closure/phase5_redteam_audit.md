# Phase 5 — Red Team Final Audit (exp-097, Panel Iteration 74)

*Fresh context, last seat, everything on the table: `phase1_proposal.md`, all
five blind Phase-2 critiques, `phase2_redteam_audit.md`, `NOTES.md`, `run.py`,
`results.json`, and all six Phase-5 reviews (photonics, materials, em,
thermodynamics, quantum, vision). Read in full this session: `PANEL.md`;
`LOGBOOK.md`'s RULED OUT registry R1–R18 verbatim; the T28 sub-thread's
Iterations 70–73 narrative in full; `experiments/096-.../NOTES.md` and
`run.py`; `experiments/069-t21-.../design_geometry.py`; `lab/fdtd2d.py`
~120–186. Every load-bearing figure below was independently re-derived from
source or by direct execution this session — nothing is taken on any
document's word, including the six Phase-5 reviews' own claims.*

## 1. Independent re-verification of the run

**Bit-exact reproduction, confirmed by fresh execution, not by trusting six
prior "bit-exact" claims.**

```
$ python3 experiments/097-t28-r18-tier0-gate-closure/run.py
```

Diffed the freshly-produced `results.json` against the git-committed version
(`git show HEAD:...results.json`) programmatically, field-by-field, with
`wall_time_s` excluded: **`EQUAL (excl wall_time_s): True`** — every other
field, including `registration_gate_outcome`, all nine fault-injection
results (positive control, FI-A through FI-H), `check5_extended`,
`check6_new`/`check6_old`, and the 21-construction count, matches exactly.
File restored to its committed state after the check (`git checkout --`).

**Trust suite**: `python3 lab/validation/run_all.py --only 12346789` —
**41/41 PASS**, independently re-run this session. `git log` confirms zero
`lab/` diff since exp-094 (three iterations back), and Predictions-before-run
discipline: `d8960f4` (Phase 3, NOTES.md frozen) precedes `29c8b17` (Phase 4,
results committed) in the commit history.

**Underlying construction-code arithmetic**, re-derived from
`design_geometry.py` source directly, not from any document's restatement:
read `r3_config()`/`r4_config()`/`r5_config()` (lines 192–210, 265–283,
350–367) by hand. `y_hi = ny - y_lo` in all three; for `C40_R3`
(`pad=0`): `ny=R3_BASE_NY=round(1584·1.5)=2376`, `y_lo=R3_BASE_ABSORB+pad=
round(40·1.5)+0=60`, `y_hi=2376-60=2316`. For `C40_R5`: `3960-100=3860`.
Both bit-exact against `R{3,5}_CONFIGS["C40_R{3,5}"]`'s own stored fields
and against `results.json`'s `check5_extended` block. **Confirms the
`y_hi`/`R{n}_BASE_NY` fix (EM+THERMODYNAMICS' Phase-2 catch) landed
correctly in the frozen document and is arithmetically sound**, independent
of all six Phase-5 reviews' own (concurring) confirmations of the same.

**Directly re-executed the fault-injection triad myself**, not merely
re-run via `main()`:

```
check6 on mislabeled point (family="R3"→"R4" override, true line-511/38.4°):
{'theta_ok': True, 'family_ok': False, 'cpl_ok': False, 'clean': False}
```

— this single line of direct execution is the crux fact behind §3 below.

Also independently confirmed by direct code read: `run_fi_g()` (`run.py`
236–250) perturbs only `native_src_x`; `check5_recipe_spot_check_extended()`
(183–203) reads only `dg.R{3,4,5}_CONFIGS["C40_R{3,4,5}"]`, never any
`G40_*` key; `design_geometry.py` (216/287/371) confirms `G40_R3`/`G40_R4`/
`G40_R5` all exist as distinct dict keys, never referenced by Check 5's own
code. Independently word-counted all five Phase-2 critiques' Steel-man/
Sharpest-attack sections programmatically: PHOTONICS 138/145,
ELECTROMAGNETISM 99/**156**, QUANTUM 124/**156**, THERMODYNAMICS
129/**170**, VISION 139/**156** — **bit-exact match to VISION's own Phase-5
table.** Re-grepped LOGBOOK.md's Iteration-65/exp-088 banner-rule text
(line 4969): *"required at BOTH the Predictions section AND the Result
section"* — confirmed verbatim, matching the proposal's and every review's
own citation.

**Conclusion: the run is bit-exact reproducible, the trust suite is green,
and every cross-cutting figure independently re-checked this session
(y_hi/BASE_NY arithmetic, the FI-H direct execution, the word counts, the
banner-rule text, the G-config gap, the FI-G src_x-only scope) reproduces
exactly as the document and/or the six Phase-5 reviews claim.**

## 2. Ruling on the six Phase-5 reviews

All six: **CONCUR-WITH-GAP(S)**, zero DISPUTE among them. Ruling on each:

### PHOTONICS — **ADOPT in full**

Gap 1 (Check 5's FI-G exercises `src_x` only, never `y_lo`/`y_hi`, for any
of the three families — two of the check's own three asserted quantities
have zero demonstrated fault-injection discriminating power): independently
confirmed by direct code read of `run_fi_g()` above. Real, genuinely new
(missed by all five blind Phase-2 critiques and Red Team's own Phase-2
audit — QUANTUM's Phase-2 critique got closest, flagging FI-G's family
scope, not its within-family quantity scope), correctly ruled
non-load-bearing (the underlying `y_lo`/`y_hi` values are independently
right, confirmed above by my own from-scratch `design_geometry.py`
re-derivation, a route outside the gate's own machinery). Gap 2 (Idealization
40 documentation error) — see §3, ADOPT, converges with MATERIALS/EM. Gap 3
(ledger arithmetic, "TEN... 64–74" vs. a literal `74-64+1=11`) — trivial,
correctly self-scoped as low-confidence and zero-stakes; not independently
re-derived here (not worth the cost — PHOTONICS itself flags the ambiguity
in what the counting convention actually is).

### MATERIALS — **ADOPT in full**

The Idealization-40 finding (§3 below) independently re-derived by direct
execution, not merely code-reading — this is the strongest form of
verification among the three seats that caught it. Correctly notes Red
Team's own Phase-2 fix code (`phase2_redteam_audit.md` §3) had the keying
right; the drift happened between that fix and NOTES.md's own prose
description of it. Self-critical review of MATERIALS' own Phase-1 proposal
(the R3/R5 extension), as PANEL.md's own precedent expects of a lead seat.
Ranked-candidates list is sound; item 3 (a governance call on the
grazing-incidence item) is addressed in §7 below.

### ELECTROMAGNETISM — **ADOPT in full**

The most rigorous of the three independent Idealization-40 catches: derives
the field-theory soundness of both new formulas first (correctly, bit-exact
against `lab/fdtd2d.py`), confirms the `y_hi`/`BASE_NY` fix did not leak
into Result, and only then finds the Idealization-40 gap — including the
important, correctly-scoped caveat the other two catches understate:
`cpl_ok`'s independence from `pt["family"]` is **contingent on `R3`/`R4`/
`R5`'s `cpl` values being pairwise distinct (30/40/50)**, not a structural
guarantee. This is the sharpest of the three write-ups and the one whose
own prediction — "none independently executed the corrected function
against a mislabeled point and inspected `cpl_ok` in isolation" —
**forecast QUANTUM's own review's failure mode before QUANTUM's review was
read** (see §3).

### THERMODYNAMICS — **ADOPT in full**

The "doubled... to 41" wording nitpick is independently confirmed: `21×2=42
≠41`; the true counterfactual (20 unshared Checks-1–4 constructions + 20
unshared Check-7 constructions + 1 FI-D = 41) was independently re-derived
by this seat from first principles, not merely re-arithmetic'd, and I
re-verify it holds: **41, exact.** "Doubled" is a loose gloss (the 20-point
shared subset doubles to 40, plus the already-singular FI-D construction),
not a literal doubling of 21. Correctly ruled non-load-bearing, correctly
scoped as a one-word precision issue, not a numeric error. Every other
bookkeeping claim in this review (construction-count re-derivation, the
monotonic 8→9→10 / 20→21→22 ledger-count grep, the FI-G rounding
non-coincidence check) independently reproduces.

### QUANTUM OPTICS — **ADOPT the verdict and the new finding; PARTIALLY
### OVERRIDE one factual claim in §2**

The G-config scope gap (Check 5 has never tested any `G40_*` config, for
any family, and this cycle's own restated Idealizations 39/42 silently drop
the explicit disclosure exp-096's original Idealization 39 carried) is
independently confirmed by direct code read (§1 above: `check5_recipe_
spot_check_extended()` reads only three `C40_*` keys). Real, genuinely new,
correctly scoped as minor/disclosure-only/non-blocking. The banner-
verification discharge (§5 of that review) is independently confirmed:
`NOTES.md`'s Result section carries the sentence, matching the literal
Iteration-65 rule text I re-grepped myself. **However:** QUANTUM's own §2
analysis of `cpl_ok` contains a factual error that **directly reproduces
the Idealization-40 mistake this cycle's own EM/MATERIALS/PHOTONICS
reviews independently caught elsewhere in the same document set.** QUANTUM
writes: *"`cpl_ok`: `CPL[pt["family"]]` vs. `cpl_frozen` — both sides
ultimately keyed by `pt["family"]` once `family_frozen` resolves it, so
`cpl_ok` is not independently meaningful in isolation (Idealization 40 says
this explicitly, correctly)."* This is false, by the same direct-execution
evidence three other seats and I independently produced: `family_frozen`
is looked up by `notes_line` alone (`NOTES_MD_FROZEN_FAMILY_BY_LINE[line]`)
and **never reads `pt["family"]` at all** — it does not "resolve... once
`family_frozen` resolves it" in any sense that reintroduces dependence on
the untrusted field. `cpl_ok`'s right-hand operand is unconditionally
independent of `pt["family"]`, not merely "safe because gated behind
`family_ok`" as QUANTUM's own logical-AND argument (which is separately
correct as an argument about the *composite* `clean` value) implies about
`cpl_ok` *itself*. **Practical consequence: none** — QUANTUM's own
downstream reasoning (the composite `clean` correctly flips to `False`
under FI-H via `family_ok` regardless) is sound, and its verdict is
unaffected. But this seat's review is the fourth touchpoint on this exact
line of code in this cycle's record, and the only one of the four that
gets the underlying fact wrong rather than right — ironic, since this
seat's own charter this cycle was explicitly "does Check 6's three-sub-check
design genuinely, independently discriminate the state it claims to."
**Ruling: ADOPT the review's verdict, new finding (G-config gap), and
banner discharge; OVERRIDE the specific §2 factual claim about `cpl_ok`'s
keying — the correct characterization is EM's and MATERIALS' (§3 below),
not QUANTUM's own restatement of Idealization 40.**

### VISION SCIENCE — **ADOPT in full**

The banner-discharge PASS (both Predictions and Result sections carry the
sentence, first-attempt-correct after two consecutive prior-cycle drifts) is
independently confirmed by direct read. The standing-items ledger increment
(9→10, 21→22) is confirmed monotonic and correctly restored per PHOTONICS'
Phase-2 catch. **The word-cap finding is independently reproduced exactly**
(§1 above: PHOTONICS 145 within cap; EM/QUANTUM/VISION 156; THERMODYNAMICS
170) — a genuine, previously-uncaught, non-load-bearing procedural gap,
correctly scoped as founding-instance (not a "known, named, ignored"
recurrence) and correctly not escalated to DISPUTE.

## 3. The Idealization-40 finding: is it real, and what should be done?

**Real, confirmed independently by direct execution (§1), not merely by
reading three seats' agreeing prose.** `check6_positional_and_cpl`'s
`cpl_ok` sub-check reads:

```python
family_frozen = NOTES_MD_FROZEN_FAMILY_BY_LINE[line]          # keyed by notes_line
cpl_frozen, _ = NOTES_MD_FROZEN_CPL_BY_FAMILY[family_frozen]  # keyed by family_frozen, NOT pt["family"]
cpl_ok = bool(CPL[pt["family"]] == cpl_frozen)                # LHS only reads pt["family"]
```

`cpl_frozen`'s lookup key is `family_frozen` — itself independent of
`pt["family"]` — so only the left-hand operand depends on the untrusted
field. NOTES.md's Idealization 40 states the opposite ("STILL keyed by
`pt["family"]` on both sides... not an independent per-point check [in
isolation]"). Direct execution on the FI-H mislabeled point settles it:
`cpl_ok=False` independently of `family_ok`, not a value that merely rides
along.

**Genuinely four-way touched, but not four-way *convergent* in the sense of
four independent correct catches.** PHOTONICS, MATERIALS, and EM
independently, correctly identify the same under-claim, by three different
methods (code reading, direct execution on FI-H, and code reading plus a
formal contingency caveat, respectively). QUANTUM OPTICS is the fourth seat
to touch this exact code this cycle — its charter this cycle was precisely
to verify Check 6's discriminating power — but its own write-up **repeats
the Idealization-40 error rather than catching it**, independently
demonstrating EM's own prediction that a reviewer who does not directly
execute the isolated `cpl_ok` value against a mislabeled point will carry
the false characterization forward. This is not disqualifying to QUANTUM's
overall verdict (which rests on the composite `clean` value, correctly
computed), but it means the correct count is **three independent correct
catches, one independent incorrect echo** — a nuance worth logging exactly,
not rounding up to "four-way convergent" in the record.

**Is it load-bearing?** No, on every count independently checked: it is a
documentation-only claim, points in the *safe* direction (the code is
stronger — more independent — than described, not weaker), and nothing in
`results.json`, the CLEAN verdict, or any fault-injection outcome depends
on which characterization is correct. It also does not resurface R18's
dangerous direction (a check's real coverage narrower than claimed); it is
the mirror case, which several reviews correctly note makes it non-
dangerous but does not make it non-real.

**What should be done: a documentation fix, queued Tier 0, not urgent, not
gating.** Correct Idealization 40 (and `run.py`'s matching docstring) to
state that `cpl_frozen` is sourced via `family_frozen`, independent of
`pt["family"]`, and that this makes `cpl_ok` alone already discriminate
every currently-possible family mislabel among `R3`/`R4`/`R5` — contingent
on their `cpl` values staying pairwise distinct (EM's caveat, the most
complete of the three formulations, adopted here as the fix text). Since
this is a Phase-1/Phase-3-authored Idealization now cited by five
downstream documents (three correctly, one incorrectly, and this audit),
the fix belongs in a same-shift LOGBOOK correction note, not a `results.json`
rerun — nothing computational changes.

## 4. New findings of my own, beyond the six reviews

1. **QUANTUM's own Phase-5 §2 factual error** (§3 above) — the sharpest
   finding this audit adds: not a new code defect, but a documented
   instance of exactly the failure class this whole two-cycle detour exists
   to police (a claimed-scope statement that does not survive independent
   execution), occurring inside a Phase-5 *review*, one layer beyond every
   prior instance in this sub-thread's history (which have all been in
   Phase-1/Phase-3 proposal documents, never a review document itself).
   Non-load-bearing, but worth naming precisely so a future cycle citing
   "QUANTUM's Phase-5 review confirmed `cpl_ok`'s dependence on `family_ok`"
   does not inherit the wrong reason for a right-shaped conclusion.
2. **No other undetected code-level defect found.** I independently
   re-checked every fault-injection scenario's own logic (not merely its
   result) against `lab/fdtd2d.py`'s actual `add_line_source` construction
   (lines ~132–186, read directly this session) and found no formula error,
   no self-referential comparator beyond the already-disclosed FI-A/Check-4
   case (correctly carried forward from R18's founding cycle), and no
   silent construction-code change since exp-096 (`construct_sim`,
   `phase_expected`, `design_geometry.py`'s `r{3,4,5}_config()` are byte-
   identical, confirmed by the import-by-reference design and independently
   spot-read this session).
3. **The grazing-incidence/x-wall ledger counting ambiguity (PHOTONICS' Gap
   3) is real but genuinely low-stakes** — I did not fully resolve which
   counting convention is authoritative (the record shows at least one
   iteration where the line was not verbatim-restated, per Iteration-71's
   own "named at Iterations 64/65/67/68/69/70/71" phrasing, an inconsistent
   base for either an inclusive-range or a restatement-count convention).
   Flagged, not chased further — zero stakes, as PHOTONICS itself already
   states.

## 5. Checkpoint ruling — all five criteria

1. **Config passes all constraint metrics** — N/A. No mechanism, no T1
   position; confirmed directly from `phase1_proposal.md`/`NOTES.md` §4,
   and this is the fourth consecutive zero-FDTD T28 desk cycle
   (exp-069-pattern). **Does not fire.**
2. **A proven boundary, gates clean** — N/A, identical reason. **Does not
   fire.**
3. **Synthesis requires engine physics beyond validated bench classes** —
   No. Zero `lab/` diff, confirmed by `git log`; every new construction
   uses already-validated `Sim`/`add_line_source` machinery unmodified.
   **Does not fire.**
4. **Red Team flags program-integrity drift (unfalsifiable claims, a
   constraint quietly dropped, especially #3)** — the substantive question
   this cycle poses. Every gap found this cycle — PHOTONICS' Gap 1/2,
   MATERIALS'/EM's Idealization-40 catch, THERMODYNAMICS' wording nitpick,
   QUANTUM's G-config gap (and its own §2 error, found by me), VISION's
   word-cap finding — was caught **blind, at Phase 5, before this LOGBOOK
   entry**, matching this sub-thread's own established discharge precedent
   (R16/R17/R18's own founding instances). None is a recurrence of a
   previously-named-and-ignored pattern: the G-config gap is a *disclosure*
   drift on an already-known, narrowly-scoped limitation (the reconciled
   queue that commissioned this cycle asked only for the `R3`/`R5` family
   extension, never the `G`-config axis — so its absence is not "known,
   named, mandated, ignored," only "known, imprecisely re-disclosed"); the
   FI-G src_x-only scope and the Idealization-40 documentation error are
   both first-time-named gaps in this cycle's own newly-added code, not
   reused unfixed machinery. No constraint (#1–#4 of the phenomenon target)
   is in play at all this cycle, so constraint-3 cannot have been quietly
   dropped. **Does not fire** — matching every one of the six Phase-5
   reviews' own independent rulings, and Red Team's own Phase-2 audit's
   "caught here, at Phase 2... does not rise to known, named, ignored"
   precedent for the tautology finding specifically.
5. **Two consecutive iterations with no logbook-advancing result** — No.
   This cycle produced a genuinely stronger, fault-injection-verified
   seven-check gate (up from exp-096's four-verified-of-six), closed a
   real tautology before it could reach Phase 3, and is the direct
   predicate for unblocking Tier 1 real-FDTD spend. **Does not fire.**

**No checkpoint fires this cycle.** No new standing rule is proposed — R18
already covers the pattern seen (a check's documented scope must survive
contact with its actual code), and every instance found this cycle is a
fresh application of R18's existing discipline, not a new failure shape.

## 6. Combined Verdict

**PARTIAL, converging toward closure of the registration-detour question.**
The core claim survives, independently re-verified from source and by
direct execution, not on any document's word: R18's own Tier-0 discipline,
applied retroactively to R18's own founding gate, closes the four
previously-claimed-vs-actual coverage gaps (Check 6 positional +
`cpl_intended`, Check 5's `R3`/`R5` extension, Check 7's new amplitude-taper
axis) plus the tautology Red Team caught mid-cycle at Phase 2 — the
earliest an R18-class defect has been caught in this sub-thread's history —
**without discovering a genuine registration defect anywhere in the
underlying, already-validated construction code.** Every placement/phase/
taper/resolution/angle quantity independently re-derivable from
`design_geometry.py`/`lab/fdtd2d.py` source matches what the gate reports,
confirmed by at least two independent routes (the gate's own fault
injection, and — for the specific quantities this cycle's own instrument
under-tests — my own and PHOTONICS'/MATERIALS' from-scratch re-derivations
outside the gate's own machinery).

**Corrected/final scope**, narrower than a bare "CLEAN, seven checks" would
suggest, on three independently-confirmed axes: (1) Check 5's own
fault-injection control (`FI-G`) validates only the `src_x` branch of its
three-quantity assertion, for all three families — the `y_lo`/`y_hi`
branch (the source-placement span the phase-ramp formula itself centers
on) has zero demonstrated FI-discriminating power, though the underlying
values are independently confirmed correct by a route outside the gate;
(2) Check 5 has never tested any `G40_*` (padded) config, for any family —
a known, pre-existing limitation whose disclosure was imprecisely
compressed this cycle rather than newly introduced; (3) Idealization 40's
own text mischaracterizes `cpl_ok`'s actual independence, understating (not
overstating) the check's real power — non-dangerous, but a documentation-
scope error inside the very Idealization meant to describe a fix for a
documentation-scope error, further echoed rather than caught by one of the
six Phase-5 reviews itself.

**Tier 1 is genuinely, fully unblocked — I concur with all six Phase-5
reviews, independently.** None of the three scope gaps above implicates the
underlying construction code that Tier 1's real FDTD spend will exercise:
every quantity Tier 1 depends on (resolution, angle, placement, phase,
taper, at `R3`/`R4`/`R5`, `C` and `G` configs alike) is independently
confirmed correct this session by re-deriving it directly from
`design_geometry.py`/`lab/fdtd2d.py` source — a route that does not depend
on the gate's own self-test completeness. The residual gaps are holes in
the *instrument's own self-certification*, not evidence of, or even a
live risk factor for, an actual undetected placement/registration defect.
Nothing here needs fixing *before* Tier 1 proceeds; the fixes below are
zero-FDTD, cheap, and can run alongside or interleaved with Tier 1's real
spend, matching every reviewing seat's own ranking (none placed a Tier-0
item ahead of Tier 1's item 6 this cycle).

## 7. Reconciled Iteration-75 queue

**Tier 0 — zero-FDTD, documentation/code fixes, run alongside Tier 1, not
gating it (all six reviews agree none of these blocks real spend):**

1. **Correct Idealization 40** (and `run.py`'s matching docstring) to state
   `cpl_frozen` is keyed by `family_frozen` (via `notes_line`), independent
   of `pt["family"]` — making `cpl_ok` alone already discriminate every
   currently-possible family mislabel, contingent on `R3`/`R4`/`R5`'s `cpl`
   values staying pairwise distinct (EM's fullest formulation; converges
   MATERIALS+EM+PHOTONICS' Gap 2). **Also log, in the same correction, that
   QUANTUM's own Phase-5 review §2 independently repeats this exact
   mischaracterization** (§3/§4 above) — a same-shift LOGBOOK note, not a
   re-run, so a future citation of that review does not inherit the wrong
   reason for its otherwise-correct verdict.
2. **Add `FI-G′` (`native_absorb` corrupted, e.g. 41 not 40) to Check 5,
   scored against all three families** (PHOTONICS' Gap 1, the highest-
   priority Tier-0 item: two of the check's own three asserted quantities
   currently have zero fault-injection coverage). Zero new `Sim`
   constructions, same cost class as the existing `FI-G`. `FI-G″`
   (`native_ny` corrupted) is optional but cheap to bundle in the same
   commit.
3. **Restate Idealization 39/42 to explicitly name the still-open
   `G40_*`-config scope gap in Check 5's extension**, matching exp-096's
   own original precision (QUANTUM's finding) — one line, no code change.
4. **Thermodynamics' wording nitpick**: "would have silently doubled...
   to 41" → "would have silently grown the construction count to 41,
   nearly double" — one-word precision fix, no re-run needed.
5. **A Director note logging VISION's word-cap finding** as a named
   precedent (so a repeat is judged against it), without requiring the
   four already-adopted Phase-2 critiques themselves to be rewritten —
   their substance is unaffected and already correctly adopted.

**Tier 1 — resume real FDTD spend, now properly unblocked (unanimous
across all six Phase-5 reviews and this audit's own independent
confirmation):**

6. **Bracket the other three established `cpl=20` nulls at `cpl=40`**
   (~24 calls) — ranked #1 by every seat that ranked this cycle
   (PHOTONICS, MATERIALS, EM, THERMODYNAMICS, QUANTUM, VISION, unanimous).
   The decisive discriminator between a family-wide `cpl=40` recipe defect
   and feature-dependent node migration; the registration axis has now
   been checked as thoroughly as zero-FDTD code review can take it.
7. **The re-centered, directionally-weighted node-bracketing re-run at
   θ₀≈38.590°**, sized to the confirmed ≥0.5° single-sided half-width
   (exp-096's desk bound; ~8–16 calls) — ranked #2, sequenced after item 6
   per every seat's own stated reasoning (a family-wide finding from item
   6 would reprioritize how item 7's result should be read).
8. **Pre-wire `netd_row()`/`cell_metrics_r{3,4,5}` sidecar extraction into
   whichever of items 6/7's `run.py` computes `delta_scene`/
   `frac_contrast`, from first commit, per R16** (THERMODYNAMICS' own
   preventive item, echoed by EM/QUANTUM/VISION) — this is the first
   real-FDTD cycle on this window since exp-094's own R16 near-miss;
   wiring the sidecar from first commit, not a fix-docket afterthought, is
   the only way to guarantee this does not become R16's forward-elevating
   clause's third occurrence.
9. **Item 9 (the `cpl=50`/`R5` interior sweep) stays deferred** — unanimous
   across every seat that has addressed sequencing since exp-095; reuse
   the already-built, gate-verified family, do not rebuild it.

**Standing, unranked, carried forward:** PHOTONICS' own grazing-incidence
validity check (now ten-or-eleven consecutive cycles undischarged,
Iterations 64–74, exact count ambiguous per §4.3 above but the fact of
non-discharge is not) — **MATERIALS' own governance recommendation is
adopted here**: this item should either be scheduled within the next two
cycles or the Director/Red Team should make an explicit, reasoned call to
formally deprioritize it, closing Iteration 61's still-open ritualization
question for this specific item rather than letting the count climb
indefinitely as a restated-but-never-executed line; the x-wall
wavelength-generality leg (22 consecutive cycles deferred, 076–097, same
governance question); the unbiased margin-vs-distance rebuild; the
ritualization governance question itself (Iteration 61).
