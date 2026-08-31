# Phase 5 — Red Team Final Audit (exp-096, Panel Iteration 73)

*Seat charter (PANEL.md, verbatim): attacks every proposal, speaks last and
hardest; standard is not textbook-physics compliance — speculation is
permitted; kills internal inconsistency, unfalsifiable claims, mechanisms
that cannot be expressed as simulation parameters, and proposals that
quietly violate a target constraint, especially #3. Never leads a cycle,
has no proposal of its own to protect.*

Read, in the order specified: PANEL.md in full (Checkpoints §, Phase-5
spec); LOGBOOK.md's RULED OUT R1–R17 in full (R1–R17, all addenda,
verbatim, including R16's and R17's own founding-instance and
forward-elevating-clause text) and the complete T28 live thread from
Iteration 46 (exp-069) through Iteration 72 (exp-095)'s own LOGBOOK entry;
every file in `experiments/096-t28-r4-registration-readback-gate/` —
`phase1_proposal.md`, all five blind Phase-2 critiques,
`phase2_redteam_audit.md`, `NOTES.md`, `run.py`, `results.json`,
`run_output.txt`, all six blind Phase-5 reviews. Independently re-verified,
this session, from source, not on any review's word: `results.json` read
directly; `run.py` read line-by-line (`check6_notes_md_cross_check`,
`run_checks_1234`, `run_fault_injection`, `construct_sim`); `lab/fdtd2d.py`
(`add_line_source`, both the `phase` and `profile` construction) read
directly; `run_output.txt` read directly. Every load-bearing figure below
was independently re-derived or directly read from primary source this
session.

## 0. Scope note

Pure instrument-validation work, matching every T28 desk/instrument cycle
since exp-069 (confirmed: T1 route N/A, Checkpoint criterion 2 N/A,
`REALIZABILITY_MEMO.md` untouched, zero `lab/` diff — independently
re-confirmed via `git status`/`git diff --stat lab/`, both empty, same as
three of six blind reviews already found). `constraint-#N-violation` does
not apply anywhere in this audit — no phenomenon-mechanism claim exists to
quietly violate a constraint with. Every attack below is tagged
`[inconsistency]` — a mismatch between a governing document's own claim and
what the executed code or its own output actually shows.

## 1. Independent re-verification of the six blind reviews' load-bearing claims

All six independently reproduce. Detail, focused on the four claims this
audit's own brief specifically named for re-derivation:

**FI-A's `check4_phase_ramp` value (PHOTONICS/MATERIALS/EM/QUANTUM).**
Read `results.json::fault_injection.FI_A_family_cpl_swap` directly:
`check1_resolution: false`, `check4_phase_ramp: true`,
`check4_max_abs_diff: 0.0`, `clean: false`. **Confirmed exactly as all four
reviews state.** Traced the mechanism independently in `run.py`
(`run_checks_1234`, lines 141–167): `expected = phase_expected(sim.lam,
theta_intended, ...)` — the comparator is built from `sim.lam`, the
*actual*, potentially-corrupted value baked into the `Sim` object, not an
independently-sourced reference. For FI-A, `sim.lam` reads 30 (the injected
value); `add_line_source` itself used the identical `self.lam=30` to build
the real stored `phase` array. Both sides of Check 4's comparison are
therefore functions of the same wrong number and agree by construction —
`check4_max_abs_diff=0.0` is not a near-miss, it is exact agreement between
two computations sharing one corrupted input. **This is unconditional, not
scenario-specific**: Check 4 can never independently corroborate the
*resolution* axis of the phase array, in any fault mode, because its own
reference recomputation always reads `sim.lam` after that value is already
whatever it actually is. `phase_expected(cpl_intended)` (the alternative,
`cpl_intended`-based comparator sketched in Phase 1's own pseudocode and
flagged vestigial by Red Team's own Phase-2 attack #4/fix #8) *would* have
caught FI-A — but Check 4, as actually shipped, does not use it.

**NOTES.md's own claim, traced.** Setup (§, "Fault-injection scenarios"
table): "Must be caught by ... Check 1 (transitively, Check 4)." Predictions
("Fault-injection positive control..."): "FI-A by Check 1, transitively
Check 4." Result: "FI-A (family/`cpl` swap) caught by Check 1 as predicted"
— **no mention of Check 4.** The "transitively Check 4" clause is silently
absent from the Result section, not flagged as falsified, not corrected, not
struck through with a note. This is a genuine, independently-verified defect
in the committed record: a frozen, pre-registered claim, falsified by the
cycle's own executed data, corrected by *omission* rather than by
*disclosure* — the identical shape PHOTONICS, EM, and QUANTUM each named
independently (a three-way blind convergence, MATERIALS confirming the
underlying `check4_phase_ramp=True` fact as a fourth, without drawing the
same "silently dropped" conclusion explicitly). **Confirmed, all four
reviews.**

**Check 6's `cpl_intended` coverage (QUANTUM).** Read
`check6_notes_md_cross_check()` (`run.py:193–207`) directly, character by
character:
```python
found = any(abs(pt["theta"] - v) < 1e-9 for v in frozen_values)
```
`pt["theta"]` is the only field compared; `NOTES_MD_FROZEN_LINE_VALUES` maps
`notes_line → [angle values]` only — no `cpl`/family entry exists anywhere
in that dict or in this function. **Confirmed: `cpl_intended` is never
read inside this check.** Cross-checked against all three governing texts
QUANTUM cites (Phase 1 §2b — n/a, Check 6 didn't exist yet; NOTES.md's own
"Setup" §6: *"`theta_intended`/`cpl_intended`... compared against the
values frozen in... NOTES.md's own Predictions section"*; Red Team's own
Phase-2 fix docket item 4: *"assert the `theta_intended`/`cpl_intended`
values... equal the values stated in exp-095's own NOTES.md frozen
Predictions section"*) — both explicitly name `cpl_intended` as in scope.
**Confirmed: claimed scope exceeds actual code coverage, exactly as
QUANTUM found, independently verified here from the same source.**

**EM's set-membership finding, independently checked.** The same line of
code above is a membership test (`any(... for v in frozen_values)`) against
a two-element list for every line hosting a pair
(437/445/476). A same-line index swap upstream (e.g. `RANK1A_ANGLES=
[39.4,39.2]` instead of `[39.2,39.4]`) would leave every `pt["theta"]`
value still a member of the same two-element set — Check 6 would read
CLEAN. Checks 1–4 read `theta_intended` from the identical, already-swapped
constant, so they would not catch it either. **Confirmed: no check in this
cycle's six-check architecture would catch a same-line index swap** —
independently re-derived, not taken on EM's word.

**Desk-bound containment-ratio triple, ±0.5° (THERMODYNAMICS).** Read
`results.json::desk_bound.containment_ratios["0.5"]` directly: `{
"lower_window": 2.5829, "upper_window_1": 1.5617, "upper_window_2":
1.3271}` — the canonical order used throughout `migration_figures_deg` and
`run_output.txt`. NOTES.md's Result section states: *"±0.5° gives
1.33×/1.56×/2.58×"* — the exact reverse order (`upper_window_2`,
`upper_window_1`, `lower_window`). Confirmed by direct comparison against
`run_output.txt`, which prints the dict in canonical insertion order and
shows `lower_window=2.5829` at ±0.5°, not `1.33`. **Confirmed, bit-exact
match to THERMODYNAMICS' finding.** The ±0.2° triple two sentences earlier
in the same Result paragraph *is* in canonical order (`1.03/0.62/0.53`
matches `lower/upper1/upper2` exactly) — so the reversal at ±0.5° is not a
document-wide convention, it is an unlabeled, internally-inconsistent flip
within the same paragraph. Non-load-bearing: the Predictions section's own
single-number framing ("±0.5° gives 1.33× margin, the most defensible")
already correctly cites the *minimum* (binding) figure, so the eventual
conclusion (≥0.5° is the right order of magnitude) is unaffected.

**`sim_construction_count` vs. actual runtime construction events
(THERMODYNAMICS).** Traced `main()` and `run_fault_injection()` in `run.py`
directly. The representative loop (`REPRESENTATIVE` × `PAIR_KEYS`) calls
`run_checks_1234` → `construct_sim` → `Sim(...)` 16 times. Separately,
`run_fault_injection()` calls `run_checks_1234` four more times
(`positive_control`, `FI_A_family_cpl_swap`, `FI_B_angle_mislabel`,
`FI_C_sign_flip`) — **each of these four also calls `construct_sim` →
`Sim(...)` fresh**, including the positive control and FI-B, which
fix docket item #5 and NOTES.md's own Result both describe as "reusing"
representative points 1 and 4. Nothing in the code actually reuses a
Python object; every one of these four legs re-executes `Sim(cfg["nx"],
cfg["ny"], ...)` from scratch. **Total actual `Sim.__init__` calls: 16 + 4
= 20**, not the 18 `sim_construction_count` reports. `sim_construction_count`
is arithmetically self-consistent (`16 + 2 = 18`, where "2" counts only the
*genuinely new (family,θ,cpl) combinations* FI-A/FI-C add) but its own name
promises constructor-call count, which is 20. **Confirmed exactly as
THERMODYNAMICS found** — independently re-derived by static trace of the
code, not merely re-read from the review.

**PHOTONICS' amplitude-taper finding.** Read `lab/fdtd2d.py`'s
`add_line_source` directly (the `profile == "plane"` branch): a raised-
cosine window is built from the `edge` argument (`win = 0.5*(1-cos(pi*
arange(edge)/edge))`) and stored as `sim.sources[-1]['profile'] = amplitude
* p` — an entirely separate array from `phase`, built from a different
input (`edge`, not `angle_deg`). `run.py::construct_sim` passes
`edge=TAPER[family]` (i.e. `dg.R4_TAPER`/`R3_TAPER`/`R5_TAPER`) into every
one of the 18 `Sim` constructions. Grepped all six check functions and the
`results.json` schema for `profile`/`edge`/`TAPER`: **zero hits outside the
construction call itself.** No check, and no fault-injection scenario, ever
reads this array or verifies `TAPER[family]` against anything. **Confirmed
exactly as PHOTONICS found**, independently traced from `lab/fdtd2d.py`
source, not taken on the review's word. PHOTONICS' framing of why this
matters to its own charter — TAPER is a previously-named-and-refuted T28
mechanism candidate (exp-070, P-070-3: "TAPER alone as a sub-aperture
misses by 1197%") whose *value*, as distinct from its role as a
diffraction mechanism, has never been registration-audited — is correct and
sharpens, not merely restates, Idealization 31's scope.

**MATERIALS' Check-5 independence finding.** Read `r4_config()` in
`design_geometry.py` and `check5_recipe_spot_check()` in `run.py` side by
side. Both perform the identical two-stage arithmetic
(`round(native×RATIO)`, then `+pad`, then `y_hi = ny − y_lo`) on the
identical native literals (`300, 40, 1584`) and identical `RATIO=2.0` —
Check 5 supplies its own copies of these numbers rather than reading
`R4_BASE_SRC_X`/`R4_RATIO` off the module, so it *is* independent of the
function call and the module constants, but it is *not* independent of the
formula/method itself, which was necessarily authored by reading
`r4_config()`'s own source. **Confirmed exactly as MATERIALS found.** The
residual-risk localization — per-family `R{n}_BASE_*` literals, each
separately typed, not generated by shared logic — is the correct sharper
statement of Idealization 39's already-honest but generic disclosure.

**No discrepancy found between any review's claim and independently
re-derived source in this audit.** All six reviews' CONCUR-WITH-GAP(S)
verdicts, and every individual finding underneath them, reproduce exactly.

## 2. Per-review adjudication: ADOPT or OVERRIDE

| Seat | Core finding | Disposition | Reasoning |
|---|---|---|---|
| PHOTONICS | Amplitude-taper channel entirely unchecked by all 6 checks + FI triad; FI-A's "transitively Check 4" claim mechanically false, silently dropped in Result | **ADOPT, both** | Independently re-derived from `lab/fdtd2d.py` and `run.py` at §1 above. The taper finding is genuinely novel — none of the other five reviews, nor this seat's own Phase-2 critique, nor the original proposal's Idealization list, names it. Real, disclosed nowhere. |
| MATERIALS | Check 5 restates `r4_config()`'s own formula rather than independently re-deriving it; residual localizes to per-family `R{n}_BASE_*` literals | **ADOPT** | Independently confirmed at §1 by reading both functions side by side. A precise, correct narrowing of Idealization 39's own already-honest but generic disclosure — not a new overclaim, a sharper true statement of an existing one. |
| ELECTROMAGNETISM | Check 6 is set-membership not positional (same-line swap undetected); Checks 5/6 have zero fault-injection controls, unlike 1–4; independently re-derives the FI-A/Check-4 finding as a general, unconditional fact (not merely Red Team's own attack #3's source-of-truth-defect special case) | **ADOPT, all three** | Independently confirmed the set-membership mechanism, the absence of any FI scenario touching Checks 5/6 in `run_fault_injection()` (confirmed: it calls `run_checks_1234` exclusively, four times, none of which touches `check5_recipe_spot_check` or `check6_notes_md_cross_check`), and the FI-A mechanism at §1. This is the review that most precisely locates the *structural* cause (missing controls) behind the *symptomatic* defects (QUANTUM's Check-6 scope gap, the FI-A claim) — see §5. |
| THERMODYNAMICS | Containment-ratio triple silently reversed order in Result at ±0.5°, non-load-bearing; `sim_construction_count`(18) measures distinct configurations, not actual `Sim.__init__` calls (20) | **ADOPT, both** | Both independently re-derived at §1 — the ratio reversal by direct comparison against `run_output.txt`'s canonical dict order; the construction-count gap by static trace of every `construct_sim` call site in `run.py`. Both genuinely non-load-bearing, both genuinely real defects in the committed record, exactly the bookkeeping-precision lens this seat's own R16-founding history exists to apply. |
| QUANTUM OPTICS | All 5 NOTES.md line transcriptions bit-exact (no defect); Check 6 checks only `theta`, never `cpl_intended`, despite three governing documents naming both; independently, convergently, finds the same FI-A/Check-4 crux EM found | **ADOPT, all three** | The transcription re-verification and the Check-6 scope gap both independently confirmed at §1 (direct read of `run.py`'s `check6_notes_md_cross_check` source). The convergent FI-A finding is confirmed as a genuine third independent route to the same crux (QUANTUM traces it from the fault-injection data itself; EM traces it from re-reading its own overridden Phase-2 remedy against the executed Check 6; PHOTONICS traces it from re-deriving `phase_expected`'s own dependency on `sim.lam`) — three different methods, same conclusion, none seeing the others' work. Weighed at full strength per this program's own multi-seat-convergence precedent (exp-095 Phase-5, R16's own founding instance). |
| VISION SCIENCE | Both Phase-2 fixes (banner, word count) landed; Result section lacks the "governed by Idealizations..." banner the Iteration-65 rule requires at both Predictions and Result — and this is now at least the second consecutive cycle (exp-095, exp-096) doing the same thing, plus a prior non-firing instance before exp-090 named in the same review; self-reported "209 words" doesn't match a direct recount (~150) | **ADOPT, both** | Independently spot-checked: NOTES.md's Result section (lines 317–370, per the document read in full at the top of this audit) never states the umbrella banner sentence, only per-item Idealization citations inline. VISION's own precedent trace (checking whether exp-095's Result section satisfies the rule, and finding it does not either) is the kind of look-one-cycle-back verification this program's own convergence discipline rewards — genuinely useful, not merely defensive. The word-count discrepancy is real but trivially non-load-bearing (both 209 and ~150 clear the 300-word cap by a wide margin). |

**All six: ADOPT, zero overridden.** Every finding independently
re-verified from primary source in this audit, not taken on any review's
word. No review's finding is disputed, softened, or found to overreach its
own evidence.

## 3. Checkpoint criteria — worked through explicitly, all five

**Criterion 1 (a configuration passes ALL constraint metrics).** N/A. No
constraint metric (Weber contrast, beam-behind flux, backscatter, switch
transient) is computed anywhere in this cycle — confirmed by VISION's own
independent grep for constraint-3/witness vocabulary (zero hits) and this
audit's own read of `results.json`'s schema (no metric field of that class
present). Does not fire, does not apply.

**Criterion 2 (a proven boundary — a constraint subset shown jointly
unsatisfiable within a mechanism class).** N/A. T1 route N/A this cycle,
confirmed independently (no σ(I)/σ(x,t)/angular-selectivity/sub-threshold
position taken; `REALIZABILITY_MEMO.md` untouched). Matches every T28
desk/instrument cycle since exp-069. Does not fire, does not apply.

**Criterion 3 (a synthesis requires engine physics beyond the validated
bench classes — a major build).** N/A. Zero `lab/` diff, independently
confirmed via `git status`/`git diff --stat lab/` (both empty) — this
cycle adds no new engine machinery, only a read-only instrument built from
already-existing `Sim`/`add_line_source` object state. Does not fire.

**Criterion 5 (two consecutive iterations with no logbook-advancing
result).** Does not fire. exp-095 (Iteration 72) delivered a genuine
logbook-advancing result (Rank 1a PASS, Rank 1c FAIL, Rank 4 NEITHER, new
standing rule R17, a reconciled queue). exp-096 (this cycle) also delivers
a genuine, if narrower-than-first-stated, logbook-advancing result: within
its now-precisely-corrected scope (§4 below), it genuinely removes
caller-level plumbing as a live explanation for Rank 1c's FAIL — real new
information, not a null cycle. Two consecutive non-advancing iterations has
not occurred.

**Criterion 4 (program-integrity drift — unfalsifiable claims, a constraint
quietly dropped, or — per this sub-thread's own established generalization,
R6 through R17 — a "known, named, ignored" methodological defect).** The
closest call this cycle produces, and the one this audit weighs most
carefully, by design.

*First: is this the R16 "disclaimer-without-persistence" class, and does
its own forward-elevating clause ("a third disclaimer-without-persistence
occurrence... fires Checkpoint criterion 4 automatically") apply?*
**Independently checked and ruled: NO, this is not the same class, and the
auto-fire clause does not apply.** R16 governs a specific, narrow pattern:
a top-level disclaimer covering a byproduct NETD/thermal field travels
correctly, but the byproduct field itself (`dt_ss_full_K`,
`netd_classification`, extracted via `netd_row()`) is never persisted into
the cited report dict. This cycle computes **zero** thermal/NETD quantities
of any kind — independently confirmed by THERMODYNAMICS' own §0 (a
programmatic walk of the entire `results.json` tree for any
`netd`/`therm`/`p_abs`/`temp` key: zero hits) and by this audit's own read
of `run.py` (no call to `cell_metrics_r{3,4,5}` or `netd_row()` anywhere).
There is no disclaimer here, no byproduct field, and no persistence
question — the entire category R16 addresses is absent. Applying R16's
auto-fire clause to this cycle would be a category error, exactly as
THERMODYNAMICS itself independently concluded. **Explicitly ruled out, not
assumed out.**

*Second: is this an R4/R9/R17-class recurrence ("a claimed figure/
comparison/bracket does not survive contact with source, corrected by
omission")?* **Related in shape, but a genuinely different artifact class
— not a mechanical recurrence of an already-numbered rule's own text.** R4
governs hand-typed numeric figures not reproduced from the actual committed
function. R9 governs a cited ratio's *commensurability* (same units on both
operands). R17 governs a *bracket/tolerance width*. What this cycle
produced — independently confirmed at §1 — is different in kind from all
three: (a) a frozen, pre-registered claim about **which check catches which
fault** ("Check 1, transitively Check 4"), stated before the run, falsified
by the run's own output, and silently narrowed rather than disclosed as
wrong in the Result section (the FI-A/Check-4 finding); (b) a check's own
**documented scope, across three separate governing texts, exceeding its
actual code coverage** (Check 6 never reading `cpl_intended`) — QUANTUM's
own framing, independently confirmed correct: "the exact shape this
program's own R4/R9 lineage exists to police... just not previously
instantiated on a check's own *coverage*, only on numeric figures and
bracket widths." Neither (a) nor (b) is the literal text of any existing
numbered rule; both are structurally adjacent to the R4/R9 lineage's
underlying discipline ("a claim must survive independent contact with
source before it is trusted") applied to a genuinely new artifact — a
check's own claimed catching-power and a check's own claimed coverage,
rather than a number or a unit.

*Third: does the "known, named, ignored" bar (R6–R17's shared standard —
reusing the SAME already-fixed machinery unfixed, or defending a
one-sided framing against an affordable, skipped, named check) apply?*
**No.** This is this specific gate's own founding cycle. There is no prior
instance of this exact check (Check 6, or the FI-A/Check-4 relationship)
existing, being flagged, and then being reused unfixed — the gate itself
was built this cycle. Matching the unbroken precedent every prior rule in
the RULED OUT registry establishes (R5 through R17, each explicitly:
*"does not fire on its own founding instance"*), a genuinely new-shaped
gap, caught blind, at Phase 5, before this LOGBOOK entry is written, on its
own founding cycle, does not retroactively violate a standard that did not
yet exist when the cycle was designed.

*Fourth: weighed against this program's own two most recent precedents for
exactly this kind of close call — exp-094's R16 founding instance and
exp-095's R17 founding instance.* Both were: (i) caught blind, at Phase 5,
not earlier; (ii) the product of multi-seat independent convergence
(exp-094: THERMODYNAMICS + VISION on the disclaimer-persistence gap;
exp-095: THERMODYNAMICS/MATERIALS on the undersized bracket, QUANTUM
self-critically on the same gap by a different route); (iii) ruled the
"closest non-firing call in this sub-thread's history" at the time, **not**
firing; (iv) each produced a new standing rule (R16, R17) plus, for R16
specifically, a forward-elevating clause for future recurrences of that
exact class. This cycle's own FI-A/Check-4 finding matches that shape
closely: three-to-four-way independent blind convergence (PHOTONICS, EM,
QUANTUM directly; MATERIALS confirming the underlying fact), caught only
at Phase 5, on a claim that was frozen before the run and silently not
corrected when falsified. **Ruled, by the same standard applied at R16 and
R17's own founding instances: this is again the closest non-firing call
this sub-thread has produced since R17 — does NOT fire, for the same
founding-instance reason those two did not fire, but is named here,
explicitly, as exactly that close, and closes with a new standing rule
(§5) rather than being allowed to pass as routine.**

**Criterion 4 does NOT fire.** Ruled the closest non-firing call this
cycle produces, on two related but structurally distinct grounds (the
FI-A/Check-4 silently-uncorrected claim; Check 6's claimed-vs-actual
scope gap), neither matching R16's own narrow disclaimer-persistence class,
neither a recurrence of an already-numbered rule's own literal text, both
caught blind at Phase 5 before this entry, on their own founding cycle —
matching this program's unbroken founding-instance-does-not-fire precedent
exactly.

## 4. Combined Verdict — does the core claim survive, and what is the
## honestly-scoped headline?

**The core, load-bearing claim survives — but the CLEAN result's scope is
narrower, on at least four independently-confirmed axes, than NOTES.md's
own Idealization 38/39 residual-scope language states, and the "single
most load-bearing fix in this docket" (Check 6) is weaker than its own
governing text claims.**

What survives cleanly, independently re-verified at §1: nineteen prior T28
cycles genuinely never checked resolution/angle/placement registration at
all; this cycle built a real instrument for that axis; Checks 1–4 have a
genuine, executed, correctly-functioning fault-injection triad
(demonstrated positive control CLEAN, FI-B and FI-C both correctly caught
by Checks 2/4) that proves those four checks discriminate real defects, not
merely pass by construction; the zero-FDTD desk bound (≥0.5° single-sided
half-width recommendation) is arithmetically sound and independently
reproduced bit-exact by every reviewer and this audit. That is genuine,
new, forward information, not a null result.

What does **not** survive at the scope NOTES.md's own language claims:

1. **"Removes caller-level plumbing... entirely" (Checks 1–4) is true for
   the angle/placement axis but not, in any scenario, for the resolution
   axis specifically** — Check 4 provides zero independent corroboration of
   `sim.lam`; that axis rests on Check 1 alone (a bit-exact float
   comparison, which is itself sufficient, but the "four layered,
   partially-redundant checks" framing overstates its own redundancy on
   this specific axis).
2. **"Rules out `run.py`-vs-NOTES.md transcription drift" (Check 6) is true
   only for the angle component of each point** — the `cpl`/family
   component, explicitly named in three governing texts as in scope, is
   never checked. Combined with the set-membership (not positional)
   comparison, Check 6 as coded would not catch the single most plausible
   real-world instance of the defect class it exists to rule out (a
   same-line index swap in an already-committed job-constant list).
3. **Check 5's "recipe-internal spot-check... outside the `r{n}_config()`
   code path" is independent of the function call and module constants, not
   of the formula itself** — a defect shared between the recipe and its own
   restatement would not be caught, and the one point tested (`R4`/`C40`)
   leaves the per-family `R{n}_BASE_*` literals, where MATERIALS locates
   the actual residual risk, entirely untested for `R3`/`R5`.
4. **The amplitude-taper channel (`sim.sources[-1]['profile']`, driven by
   `edge=TAPER[family]`) is not checked by any of the six checks or the
   fault-injection triad at all** — a completely separate registration axis
   from phase/angle, with its own T28 history (`TAPER` as a previously-
   refuted mechanism candidate, exp-070), left entirely outside a gate that
   calls itself a "registration-readback gate."

**The honest, correctly-scoped headline for LOGBOOK.md:** *exp-096's
registration-readback gate, CLEAN. Within a scope narrower than first
stated: rules out caller-level plumbing on the angle/placement axis
(fault-injection-verified); rules out `run.py`-vs-NOTES.md transcription
drift on angle only, not `cpl`/family, and via a set-membership rather than
positional comparison; gives one non-independent (formula-restating)
recipe spot-check at `R4`/`C40` only; does not check the amplitude-taper
channel at all. Within this narrower, now-precisely-stated scope, it still
achieves its central purpose — removing caller-plumbing divergence as a
live explanation for exp-095's Rank 1c FAIL — and this continues to
strengthen, modestly, the case for genuine node migration as the better-
supported reading of that FAIL among the two candidates Red Team's exp-095
audit named. But five of this cycle's own governing claims about what the
gate rules out need re-statement, and the architecture's redundancy
("Check 4 alone is logically sufficient") does not hold on the one axis
(resolution) it was framed to cover.* This is a materially more honest
statement than "removes registration... entirely" (Phase 1's original,
already-corrected language) or even than NOTES.md's own post-fix
Idealization 38/39 language, which — accurate as far as it goes — does not
name any of the four gaps above.

**Verdict class: PARTIAL** — matching this sub-thread's own established
convention for a genuinely informative, forward-moving, but non-terminal
T28 desk/instrument cycle (the same class exp-094 and exp-095 both closed
at). Not RULED OUT (no mechanism class or hypothesis foreclosed; the
registration-vs-migration question is narrowed, not closed). Not PROMISING
(this is instrument work, T1 N/A, not a phenomenon-mechanism advance).

## 5. New standing rule — R18 (adopted)

**R18 — a check's own documented/claimed scope (what any governing
document — a proposal, a NOTES.md Setup or Predictions section, a Phase-2
fix docket — states it verifies) must be independently confirmed against
the check's own actual source code, line-by-line, before it is relied
upon, cited as closing a defect class, or described as load-bearing; and a
check joining an already-partially-fault-injection-verified layered-check
architecture — at any phase, including a mid-cycle Phase-2 fix docket —
must receive its own fault-injection positive/negative control in the SAME
cycle it is added, not merely inherit the trust its already-verified
siblings have earned (adopted Iteration 73, exp-096, generalizing the R4/R9
"claimed figure/comparison must survive contact with source" lineage,
applied here for the first time to a check's own coverage claim rather than
a numeric figure or bracket, and generalizing the R6/R8 "no positive
control is not evidence" standard from statistical estimators/robustness
arguments to construction-time correctness assertions specifically).**

This cycle's own record supplies the clean natural experiment that
motivates the rule, independently confirmed at §1: Checks 1–4 each have a
genuine, executed fault-injection scenario; Checks 5 and 6 have none. The
two scope-overclaim defects this audit adopts (Check 4's "transitively
catches FI-A" claim, falsified but silently dropped rather than corrected;
Check 6's claimed-but-unimplemented `cpl_intended` coverage) both occurred
on exactly the two checks (4's redundancy claim rests on comparing against
a corrupted-but-unflagged `sim.lam`; 6 itself) that either lack a control
entirely (Check 6) or whose specific claimed *redundancy* was never itself
put under test (Check 4's "logically sufficient" framing was never
independently fault-injected against a scenario designed to distinguish it
from Check 1's own coverage). Both defects survived three full phases of
review — Phase 1's own text, five blind Phase-2 critiques, Red Team's own
Phase-2 audit, Phase 3 synthesis — and were caught only at Phase 5, by
direct code re-reads rather than by any executed control that would have
surfaced them mechanically. Had a same-line-swap fault-injection scenario
been run against Check 6 (EM's own recommendation, independently endorsed
here), it would have shown Check 6 passing a defect it is documented to
catch — the exact discovery mechanism this rule requires going forward.

**Does not fire on its own founding instance** (exp-096), matching every
prior rule's own established precedent (R5 through R17, without exception).
This cycle's own CLEAN registration-gate verdict stands, correctly scoped
per §4 above, unaffected retroactively.

## 6. Reconciled Iteration-74 queue

Reconciling all six seats' own ranked candidate directions, by what each is
actually diagnostic of, cheapest-and-most-fundamental first — matching
exp-095's own Reconciled Iteration-73 queue format (proposing
seat(s)/cost/diagnostic purpose stated per item).

**Tier 0 — zero-FDTD, code-only, close this cycle's own gate's residual
gaps before further FDTD spend leans on it (R18's own discipline applied
retroactively to this cycle, before Iteration-73's queue items 3/4 resume
real spend on the code path this gate exists to police):**

1. **Fix Check 6 to positional (not set-membership) comparison, and add its
   own fault-injection scenario (a same-line index swap, e.g. temporarily
   reversing `RANK1A_ANGLES`) proving the fixed check now catches what the
   set-membership version could not** (EM, near-zero cost). Diagnostic of:
   whether the "single most load-bearing fix in the docket" (NOTES.md's own
   words) actually delivers the transcription-drift guarantee it is cited
   for. Highest priority: this is the specific check three governing texts
   already claim covers more than it does, and R18 exists to prevent this
   exact recurrence.
2. **Implement the `cpl_intended` half of Check 6** that NOTES.md's own
   Setup section, and Red Team's own fix-docket item 4, already claim exists
   — a same-shape addition to `NOTES_MD_FROZEN_LINE_VALUES`/
   `check6_notes_md_cross_check()` (QUANTUM, near-zero cost). Diagnostic of:
   closing the specific documented-vs-actual scope gap found this cycle,
   bundled with item 1 above (same function, same patch).
3. **Add a fault-injection negative control to Check 5** (a deliberately
   wrong `RATIO` or native constant, confirming Check 5 flags it) **and
   extend Check 5 to a genuinely formula-independent recompute at R3 and
   R5**, sourced from a document outside `design_geometry.py` (e.g. a
   from-scratch physical-units derivation, or exp-094/095's own NOTES.md
   constants tables) rather than a second restatement of `r{n}_config()`'s
   own arithmetic (MATERIALS + EM + VISION, converging independently; cost:
   zero-FDTD, a few lines each). Diagnostic of: whether the shared
   `r{n}_config()` recipe class — Idealization 17's long-standing, still-
   open concern — is genuinely clean, not merely self-consistent with its
   own restatement.
4. **Add a seventh check reading `sim.sources[-1]['profile']` against an
   independent recompute of the raised-cosine taper from `TAPER[family]`,
   plus a fourth fault-injection scenario (FI-D: a wrong/swapped `edge`
   value)** (PHOTONICS, zero-FDTD). Diagnostic of: the one registration axis
   (amplitude/aperture-edge) this cycle's own "registration-readback gate"
   name implies is covered and is not — directly relevant given `TAPER`'s
   own prior life as a named-and-refuted T28 mechanism candidate (exp-070).
5. **Bundle of zero-cost, same-shift documentation corrections** (fold into
   whichever of items 1–4 lands first): correct the "Check 1 (transitively,
   Check 4)" claim for FI-A in both Setup and Predictions to state plainly
   that Check 4 cannot independently corroborate a `cpl`-only defect in any
   scenario; label the desk-bound containment-ratio triples explicitly
   (`lower/upper1/upper2:`) rather than relying on silently-flippable
   positional order; correct the `design_geometry.py` citation shorthand
   (the file lives in the T21 `069-t21-block-mini-period-match-power-up/`
   directory, not a T28 `069-...` one — EM's finding, a small but recurring
   citation error across this sub-thread); correct the self-reported "209
   words" to the true recount (~150, VISION); **and — a governance item, not
   a code fix — the Director should state explicitly whether the
   Iteration-65 carried-idealizations-banner rule means "Predictions +
   Result" (its literal text) or "Idealizations + Predictions" (the pattern
   exp-095 and exp-096 have both actually followed), before a third
   occurrence forces the question under worse conditions** (VISION).

**Tier 1 — resume real FDTD spend, now properly unblocked (per §4's
correctly-scoped CLEAN verdict), sequenced after Tier 0 so any Tier-0
finding does not require retroactively auditing fresh FDTD spend:**

6. **Reconciled Iteration-73 queue item 3 — bracket the other three
   established `cpl=20` nulls at `cpl=40`** (EM's original proposal, ~24
   calls). Diagnostic of: whether Rank 1c's own FAIL pattern is a
   `cpl=40`-family-wide artifact or specific to the 38.590° feature — the
   decisive discriminator named at exp-095's own Phase-5.
7. **Reconciled Iteration-73 queue item 4 — the re-centered,
   directionally-weighted node-bracketing re-run at θ₀≈38.590°**, sized to
   this cycle's own confirmed ≥0.5° single-sided half-width (~8–16 calls).
   Diagnostic of: whether Rank 1c's FAIL reflects genuine node migration —
   the direct answer to the question this whole two-cycle registration
   detour exists to eventually enable.
8. **Pre-wire `netd_row()`/`cell_metrics_r{3,4,5}` sidecar extraction into
   whichever of items 6/7's `run.py` computes `delta_scene`/`frac_contrast`
   or any `_full` metrics variant, from first commit, per R16**
   (THERMODYNAMICS, preventive). Diagnostic of: nothing new by itself — a
   preventive application of an already-adopted rule to a code path
   (`_run_sim_r{3,4,5}_sigma`-family calls) whose sibling functions have
   twice produced an R16-class gap (exp-092/093, exp-094); cheaper to wire
   in before the run than to audit for its absence after.
9. **Item 6 (the `cpl=50`/`R5` interior sweep) remains deferred**, unanimous
   across every seat that has addressed sequencing since exp-095 — reuse the
   already-built, gate-verified family once items 6/7 resolve, do not
   rebuild it.

**Still open, standing, unaffected by this cycle (not resequenced):**
MATERIALS' own materials-adjacent angular-tolerance-scoping flag (not
urgent — T1/realizability remain N/A); the x-wall wavelength-generality leg
(now twenty consecutive cycles deferred, 076–096); PHOTONICS' own
grazing-incidence validity check (named at Iterations 64/65/67/68/69/70/71,
the single most-repeated undischarged item on the whole T28 board); the
unbiased margin-vs-distance rebuild (open since exp-090); the ritualization
governance question (Iteration 61).
