# PHASE 5 — RED TEAM FINAL AUDIT · Panel Iteration 87 (exp-110)
## Item i's Local-Magnitude Floor Gate, a Fault-Injection Control for
## `linear_fit_1_over_margin`, `stage26`'s Truncation Control, and R27's Own Founding Instance

*Charter (PANEL.md, verbatim): attacks every proposal, speaks last and
hardest. Standard is NOT textbook-physics compliance — speculation is
permitted. Kills: internal inconsistency, unfalsifiable claims, mechanisms
that cannot be expressed as simulation parameters, and proposals that
quietly violate a target constraint — especially #3. Never leads a cycle;
no proposal of its own to protect. Sole seat reading everything at Phase 5.*

Read in full: PANEL.md; LOGBOOK.md (RULED OUT R1–R26 in full; ESTABLISHED;
LIVE THREADS T1–T28, T28's own Iterations 46–86 in full detail); the
complete `experiments/110-.../` directory (`phase1_proposal.md`, all five
`phase2_critique_*.md`, `phase2_redteam_audit.md`, `NOTES.md`, `run.py`,
`chunk_runner.py`, `analyze.py`, `finalize.py`, `linear_fit_control.py`/
`_output.json`, `results.json` in full, all six `phase5_review_*.md`);
`lab/validation/run_all.py` lines 2698–2825 (stage26 incl. Gate 3);
`experiments/105-.../run.py`, `experiments/106-.../run.py`,
`experiments/107-.../run.py` (read directly, myself, for MATERIALS'
finding — see §2). No re-proposal or re-litigation of any RULED OUT (R1–R26)
idea anywhere below.

---

## 0. Framing

Governance/instrumentation cycle, T1 correctly N/A — confirmed structurally
by every one of six blind Phase-5 reviews independently, and re-confirmed
here: no σ(I)/σ(x,t)/angular-selectivity/sub-threshold machinery anywhere
in this document's tree; no constraint-1/2/3/4 verdict scored or moved.
Every falsifiable prediction in `NOTES.md` states an explicit falsification
condition and every one held — genuinely, independently re-derived by all
six reviews from primitives, not restated. All eight Phase-2 mandatory
fixes are genuinely implemented in committed code, confirmed independently
by (at minimum) EM's own line-by-line fix-table audit and cross-confirmed
by the other five reviews on the specific fixes each checked. R23 is
honored to a byte-exact standard (VISION, independently diffing
`results.json`'s persisted text fields against `NOTES.md`'s own quoted
blocks: exact match, both fields). **No factual or arithmetic defect
survives anywhere in the object-level physics/instrumentation claims** —
consistent with every one of the six blind reviews.

Five distinct new gaps were found, none raised at Phase 2 (including by my
own Phase-2 audit), all discovered fresh at Phase 5. This audit's job is to
independently re-verify the two most consequential of these from
primitives — not merely re-read the reviews that found them — rule on a
sixth (a logic-direction dispute inside the Director's own Phase-4 prose),
and decide what all of this means for R1–R27, the Combined Verdict, and
Iteration 88.

---

## 1. Independent re-verification — THERMODYNAMICS' causal-positioning claim

**Traced the actual call chain myself, from `chunk_runner.py` and
`analyze.py`'s own source, not from THERMODYNAMICS' review's own account of
it.**

`chunk_runner.py` (the only file anywhere in this cycle's tree that calls
`Sim.run()`) imports `run as R` and calls `R.geom_fixedabs`,
`R.CPL_600`, `R.COURANT_FRAC`, `R.ABSORB`, `R.EDGE` — **zero reference to
`cost_gate_check`, `COST_GATE_PILOT_S`, or `COST_GATE_TOTAL_S` anywhere in
the file** (confirmed by direct read of the full 138-line file, not a
grep). `step_once(r, which)` runs one `CHUNK_STEPS`-sized chunk
unconditionally whenever invoked — for ANY `(r, which)` pair, including
`(312, "empty")`, `(312, "hollow")`, `(312, "peccored")` — with no
upstream gate of any kind. `analyze.py`'s own `__main__` block confirms the
actual, intended execution order: it calls `have(156, ...)` and
`have(312, ...)` — presupposing the underlying `_done.pkl` files already
exist, i.e. that `chunk_runner.py` has ALREADY been invoked to completion,
per-scene, for whichever `(r, which)` combinations it finds — before
`cost_gate_check()` is ever evaluated. `cost_gate_check(pilot_empty,
pilot_total)`'s own two arguments are r=156's own MEASURED wall times,
which cannot exist before r=156's three `Sim.run()` calls have already
finished. There is no orchestrator anywhere in this tree that consults the
gate's output *before* deciding whether to invoke `chunk_runner.py` for
r=312 — that decision is made by whatever foreground Bash calls the
operator issues, and `chunk_runner.py` obeys unconditionally.

**Quantified independently, from `results.json`'s own raw `total_wall_s`
fields** (not from NOTES.md's or THERMODYNAMICS' own restated numbers):

```
r156 sum   = 250.6266 + 250.0832 + 251.5135 =   752.223 s
r312 sum   = 2334.842 + 2232.955 + 2370.409 = 6938.207 s
total      =                                  7690.430 s
r312 / total                                =   0.90219   (90.2%)
```

**Confirmed exactly.** 90.2% of this cycle's own wall-clock spend was, by
construction, already complete before `cost_gate_check()`'s own inputs
could exist even in principle — and `chunk_runner.py`, the sole caller of
`Sim.run()`, never consults the gate at any point. The gate happened to
clear this cycle (`proceed_to_r312=True`, confirmed by direct read of the
persisted `cost_gate` dict) so nothing was wasted in fact — but had r=156's
pilot come in over budget, `r312_deferred=True` would have been written
into `results.json` while the 6,938s of r=312 compute had **already been
spent regardless**, since nothing upstream of `analyze.py` asks the gate's
permission. `run.py`'s own comment (line 70: "abort r=312 leg if the pilot
exceeds this") and R27's own founding narrative (citing Iteration 83's
precedent — "the primary leg's own empty pilot… cleared the threshold and
committed", i.e. a check that gates the *decision to spend*) both claim a
capability the code, as actually wired, does not have.

**Ruling: THERMODYNAMICS' finding is CONFIRMED, independently, from the
actual call-chain source — not merely from the review's own restatement of
it.** This is real, previously-uncaught (by five Phase-2 critiques and my
own Phase-2 audit — all six of us confirmed "the gate exists and branches"
at grep-level, none traced upstream-vs-downstream), and non-outcome-
reversing this cycle only by margin, not by design. See §5 for the rule
this earns.

---

## 2. Independent re-verification — MATERIALS' R27-founding-instance overclaim

**Read exp-105/106/107's own `run.py` myself, directly — not on MATERIALS'
or the Director's own say-so.**

```
$ grep -n "COST_GATE\|r312_committed\|r312_primary_committed\|r312_settling_committed" \
    experiments/105-t28-kappa-scale-bridge/run.py
663:    r312_committed = projected_2call_min < 180.0 and (wall_312_pilot / 60.0) < 90.0
671:    if r312_committed:
753:    r_list = [78, 156] + ([312] if r312_committed else [])
```

Read lines 650–689 in full: `r312_committed` is computed from the r=312
empty-scene pilot's own MEASURED wall time (`wall_312_pilot`, `t0`/`time.
time()` around a single `_run()` call), and the entire expensive article
call plus every downstream analysis block sits **inside** `if
r312_committed:` (line 671) — genuinely upstream of the spend it gates,
the opposite of exp-110's own causal-positioning gap (§1). This is a real,
executing, correctly-positioned conditional, using hardcoded literals
(`180.0`, `90.0`), not a named `COST_GATE_*` constant.

```
$ grep -n "COST_GATE\|r312_primary_committed\|r312_settling_committed" \
    experiments/106-t28-kappa-window-floor-fixedabs-control/run.py
642:    r312_primary_committed = (wall_312_empty_pilot / 60.0) < 90.0 and projected_primary_min < 180.0
658:    if r312_primary_committed:
724:        r312_settling_committed = ((wall_312_empty_settling_pilot / 60.0) < 90.0
729:        if r312_settling_committed:
```

Two real, executing, correctly-positioned conditionals — again hardcoded
literals, no named constant. LOGBOOK's own Iteration 83 entry independently
corroborates the settling gate actually FIRED that cycle ("r=312 genuinely
NOT RUN — its own empty-scene settling pilot alone (103.28 min) exceeded
the 90-min per-leg cost gate on its own, correctly deferring the two
article calls that would have followed") — this directly falsifies
THERMODYNAMICS' own Phase-2 sharpest attack ("Iteration 83's own r=312
defer happened by a human reading printed per-chunk wall times and
manually stopping; nothing in the codebase would stop a run that blew the
budget") — Iteration 83 *is* exp-106, and the defer was a real,
upstream-positioned code branch, not a human intervention.

```
$ grep -n "COST_GATE\|r312_committed" \
    experiments/107-t28-delta-scene-r5-census-decision/run.py
111:COST_GATE_TOTAL_S = 150 * 60
329:    r312_committed = projected_total_s <= COST_GATE_TOTAL_S
330:    if r312_committed:
335:        print(f"  [cost gate] ABORTING r=312 leg -- projected {projected_total_s:.1f}s exceeds ...")
```

exp-107 introduces a *named* constant (`COST_GATE_TOTAL_S = 150*60`, a
different value from exp-108's later `180*60`) AND wires it into a real,
upstream branch with an explicit abort message.

```
$ grep -rn "COST_GATE" experiments/108-t28-reclassification-angular-pattern-batch/*.py
run.py:63:COST_GATE_PILOT_S = 90 * 60
run.py:64:COST_GATE_TOTAL_S = 180 * 60
```

Zero other hits in `chunk_runner.py` or `analyze.py` — exp-108 alone
defines the two named constants and never enforces either.

**Ruling: MATERIALS' finding is CONFIRMED, exactly, from primary source —
independently re-derived here without trusting MATERIALS' own transcription
of the line numbers.** `NOTES.md`'s own R27 paragraph — "Founding instance:
exp-105 through exp-108 (four-plus cycles) each reused `COST_GATE_PILOT_S`/
`COST_GATE_TOTAL_S`, invoked only in prose" — is **false as stated**.
exp-105/106 enforce an equivalent bound via hardcoded conditionals (no
named constant existed yet — they cannot have "reused" names that did not
exist); exp-107 introduces a named constant AND wires it into a real,
upstream branch; **exp-108 alone** is the genuine founding instance of "a
documented numeric gate, referenced only in prose, with zero enforcing
code." The false claim propagates through three layers of this cycle's own
review process before Phase 5: THERMODYNAMICS' Phase-2 critique originates
it; my own Phase-2 Red Team audit repeats and extends it *twice* (§1.5:
"CONFIRMED... zero enforcement code, exactly as THERMODYNAMICS states" —
verifying only the exp-108-scoped grep, never the "back through
exp-105/106" extension; §4: "THERMODYNAMICS is the first seat... across
this entire sub-thread's history back through exp-105/106..." — again
unverified against those files' own source); Phase-3 synthesis (`NOTES.md`)
states it as ratified fact. **None of the three layers opened exp-105/106/
107's own source before asserting a claim about what all three cycles did
— including me, at Phase 2, on this exact document.**

**This does not retroactively invalidate R27's own text.** The rule's
forward-looking discipline ("a numeric gate defined as a module-level
constant, referenced only in prose, is not a gate until wired into
executable code") is sound and generically valid, matching the R16/R21–R26
lineage; a single genuine instance (exp-108) is sufficient founding
precedent under this program's own established convention — none of R5
through R26 required more than one. Only the founding-instance
*evidentiary narrative* is false, not the rule it supports.

---

## 3. Ruling on VISION's logic-direction finding

**Task: is VISION's reasoning about common-mode bias and RESOLVED-vs-
UNRESOLVED risk actually correct? Re-derived from the mirror-differencing
algebra myself, independently, before ruling — not adopted from VISION's
or PHOTONICS' or my own Phase-2 audit's prior write-ups.**

The construction: `mirror_pooled_floor(pattern_48)` = the median, over 24
within-margin bin-pairs, of `|pattern[i] − pattern[47−i]| / 2`. Decompose
any per-bin measurement contamination at bin `i` into an odd
(antisymmetric) component `d_odd[i] = (e[i]−e[47−i])/2` and an even
(common-mode) component `d_even[i] = (e[i]+e[47−i])/2`. Only `d_odd`
survives inside the difference `pattern[i]−pattern[47−i]`; any `d_even`
component — a bias, artifact, or systematic offset present identically at
bin `i` and its mirror bin `47−i` — cancels to exactly zero, algebraically,
regardless of magnitude, at any sample size (re-derived directly; matches
PHOTONICS' Phase-2 attack and my own Phase-2 §1.1 re-derivation exactly).

**Direct consequence, worked through here independently:** whenever real
common-mode contamination is present, `mirror_pooled_floor` is a
**structural UNDERESTIMATE** of the true per-bin noise scale — the true
floor is `≥` the measured one, never `<`. Given `RESOLVED ⟺ |pattern[bin]|
≥ K·floor`:

- **RESOLVED is the classification put at risk.** A bin can clear an
  artificially-low `K·floor` bar without clearing the TRUE (possibly
  larger) noise bar — a false positive risk, systematic in direction
  (the floor can only ever be too low or exactly right, never too high).
- **UNRESOLVED is, if anything, the MORE robust classification under this
  exact bias.** A bin that fails to clear an already too-lenient floor
  would fail an even higher, common-mode-corrected floor by an even wider
  margin. Common-mode contamination in the floor's own construction makes
  an UNRESOLVED call *more* certain, not less.

**`NOTES.md`'s own Result/Interpretation text applies this backward.** Both
PHOTONICS-named bins came back UNRESOLVED-BY-CONSTRUCTION this cycle. The
Result text hedges: "though PHOTONICS' own unclosed common-mode-blindness
concern (Idealizations) means this instrument cannot rule out a real but
common-mode-masked effect at either bin." Worked through the mechanism the
DISCLAIMER itself names (floor underestimation via cancellation), this
does not follow — that mechanism, if anything, *reinforces* an UNRESOLVED
verdict rather than undermining it. A logically distinct second mechanism
(a common-mode-symmetric artifact directly suppressing the bin's own raw
reading, not the floor estimate) could in principle support the stated
hedge, but this is a different claim than the one the DISCLAIMER text
actually makes, and `NOTES.md` never states or derives it.

**Ruling: VISION is CORRECT.** The Interpretation prose misapplies the
disclosed common-mode-blindness mechanism to the wrong side of the
RESOLVED/UNRESOLVED split. Severity: non-outcome-reversing and non-fatal —
item 1c/1d stays explicitly informational, no scored verdict depends on
this sentence, and the document's own bottom-line ("not corroborated…
genuinely open, not resolved either direction") is independently
defensible on the K=3/median house-style-convention-status ground alone,
without needing the (misapplied) common-mode argument at all. This is a
real logic error in load-bearing prose immediately surrounding a
verbatim-quoted DISCLAIMER — squarely inside the class of finding this
program's same-shift-annotation convention exists to fix cheaply, not a
Checkpoint-grade defect on its own. Fixed same-shift, §7 below.

---

## 4. Do these five findings fire any Checkpoint criterion — checked element-by-element against R1–R27's own operative text

**PANEL.md's own criterion 4 text** ("unfalsifiable claims, a constraint
quietly dropped — especially #3") does not literally apply to anything
found this cycle: every prediction states an explicit falsification
condition and all were independently re-derived as genuinely falsifiable
by five Phase-2 critiques, my own Phase-2 audit, and all six Phase-5
reviews; T1/constraint-3 is correctly, explicitly, structurally N/A,
confirmed independently by every layer, not quietly dropped. Criteria 1–3
and 5 are plainly N/A (no constraint metric scored; no proven boundary; no
`lab/` diff beyond the disclosed stage26 extension, itself a validation
addition not an engine-physics change; this cycle plainly advances the
logbook). What remains is whether any *named R-rule's* own forward-
elevating clause fires, since that is the mechanism this program has
consistently used to operationalize criterion 4 for process/governance
findings:

- **Finding 1 (QUANTUM, `resolved` mask's missing `floor>0` guard).**
  Not R13 (R13 concerns a decade/threshold classification built on a
  denominator with a *demonstrated or knowable* real zero-crossing scored
  against real data — here the degenerate case is a constructed synthetic
  edge case that provably does not occur anywhere in the real captured
  data, independently re-confirmed here: floor strictly positive,
  `2.346×10⁻⁴`–`2.096×10⁻³`, at all 12 real `(r,margin)` cells, matching
  QUANTUM's own figure exactly). Not R18 (no claimed check-coverage
  overclaim exists anywhere in `NOTES.md`/`DISCLAIMER` about this specific
  edge case — the DISCLAIMER's "not validated clean of common-mode
  contamination" language is honest, if (per §3) misapplied downstream,
  not an overclaim about this guard). A genuine, disclosed-now, first-use-
  instrument construction gap, caught blind within this cycle's own
  Phase-5 review layer, non-outcome-reversing on real data. **Does not
  fire.**
- **Finding 2 (PHOTONICS, "narrows rather than resolves" understates the
  evidence; margin-independence computed but not narrated).** Not R4/R20
  (no figure or citation fails to reproduce — every number PHOTONICS cites
  is independently confirmed exact; this is a characterization/emphasis
  gap, not a false claim). Not R21 (the finding's OWN headline — both
  named bins UNRESOLVED, bin counts — *is* stated inline in Result prose;
  R21's own trigger requires a persisted finding's headline to be
  ABSENT from Result narration entirely, which is not the case here; the
  additional six-margin/bimodal detail is a refinement of an already-
  narrated finding, not a wholly unnarrated one). An interpretive/
  completeness gap, PHOTONICS' own characterization, confirmed correct
  here. **Does not fire.**
- **Finding 3 (THERMODYNAMICS, causal positioning — §1 above).** Checked
  against R23 (scoped to repeated disclaimer strings — does not apply),
  R24 (requires a specific prior Phase-2 mandatory fix's consequence,
  Phase-3-claimed "adopted in full," about THIS specific property — no
  prior cycle ever claimed anything about the gate's own causal
  positioning; Fix 5's own literal text — "wire `COST_GATE_*` as
  executable code... after the r=156 pilot leg" — says nothing about
  upstream/downstream position relative to `Sim.run()`, and is genuinely
  satisfied by what was built), R25 (requires a prior audit naming-then-
  deferring this exact gap — no prior audit, including my own Phase-2
  one, ever named it). **Does not fire on any existing rule's literal
  text — genuinely new, earns its own rule instead (§5, R28).**
- **Finding 4 (EM, `kappa_ratio**3` formula's ~15% underestimate).**
  Not R17 (R17 concerns a tolerance/bracket sized to test feature
  presence/absence against established precedent; this concerns a cost-
  projection formula's own predictive accuracy — a different object).
  Could not have been caught before this cycle (no real r=312 timing data
  at this family existed until this cycle's own re-capture) — the
  precondition every prior R-rule's "known, named, ignored" bar requires
  is absent by construction. **Does not fire; not itself a fresh rule's
  founding instance either** (too narrow/formula-specific to warrant its
  own numbered rule — folded as a disclosed companion caution under R28,
  §5).
- **Finding 5 (MATERIALS, R27 founding-instance overclaim — §2 above).**
  This is a genuine R4-class defect (an "established fact" multi-cycle
  claim that fails to reproduce from its own cited primary sources)
  surviving Phase-3 freeze — but it survives inside `NOTES.md`'s "New
  standing rule — R27" section, not its "Result" or "Learned" section.
  **R20's own literal text requires the defect survive "into its
  Result/Learned sections" specifically** — checked directly against
  R20's own operative text, not by loose analogy: this defect lives in a
  textually distinct section. R20's tally for this document, strictly
  read, is **zero** on this ground (Finding 2 above is not R4-shaped
  either), well short of "three or more" even under the most generous
  reading. **R20 does not fire.** But see §5 — this earns its own R4
  addendum rather than nothing.

**No named R-rule (R1–R27) fires Checkpoint criterion 4 this cycle.**
Every one of the five findings, individually, was caught blind, within
this cycle's own six-seat-plus-Red-Team review layer, before this entry —
matching this program's own consistent non-firing pattern for
first-discovery gaps (Iterations 78-second-instance non-firing precedent
aside, which required an already-ratified forward clause on an already-
fired rule; nothing here matches that shape). This is the SAME overall
density/shape this program has already ruled non-firing at Iteration 82
(exp-105: six CONFIRM-WITH-GAPS, zero clean CONFIRM, including a genuine
citation defect that also survived my own seat's own Phase-2 "independent
re-check") — exp-110 is not qualitatively worse than that precedent, it
is the same shape recurring once, which is exactly why §5 below graduates
it from "pattern to watch" to a ratified rule rather than treating it as
inert.

---

## 5. New standing rules

### R28 — a cost/safety/scope gate's own code-level branch must sit causally upstream of the resource expenditure it purports to control

**R28 (proposed and adopted by this Phase-5 final audit, Iteration 87).**
A numeric cost, safety, or scope gate satisfying R27 (enforced by
executable code that actually branches on its outcome) is necessary, but
not sufficient: the branch must be independently traced, from the actual
resource-consuming call site backward, to confirm it sits CAUSALLY
UPSTREAM of the expenditure it purports to control — not merely that the
gate function exists, is called, and branches somewhere in the pipeline.
A gate whose only inputs are measurements of an expenditure that has
already occurred, and whose only consumer is a downstream analysis step
deciding whether to *trust* already-produced output, cannot prevent that
expenditure, however faithfully it satisfies R27's own text. **Founding
instance: exp-110's own `cost_gate_check()`** (Fix 5, R27's own founding
fix) — genuinely wired, genuinely branches, satisfies R27's own literal
text in full — but sits inside `analyze.py`, downstream of 90.2% of this
cycle's own wall-clock spend (§1, independently re-derived from the actual
`chunk_runner.py`→`analyze.py` call chain, not merely grepped for), while
`chunk_runner.py` — the sole caller of `Sim.run()` anywhere in this
cycle's tree — never consults it. Missed by six review layers before
Phase 5 (five blind Phase-2 critiques plus my own Phase-2 Red Team audit),
all of which confirmed "the gate exists and branches" without tracing
whether the branch sits upstream or downstream of the cost. **Does not
fire on its own founding instance**, matching every prior rule's own
precedent — genuinely non-outcome-reversing this cycle (the gate cleared;
the true spend was in fact affordable). **Companion caution, not a
separate rule (EM's own Phase-5 finding, §2 of `phase5_review_em.md`,
independently re-confirmed here):** even once correctly repositioned
upstream, a gate's own projection formula must be checked against real
data as soon as such data exists — `cost_gate_check()`'s own
`kappa_ratio**3` term underestimates the measured r=312/r=156 wall-time
ratio by ~15% (measured `9.224×` combined, per-scene `8.93×`–`9.42×`, vs.
projected `8.0×`; effective exponent `≈3.21`, not `3.00` — independently
recomputed here from `results.json`'s own raw `total_wall_s` fields,
matching EM's own figures exactly), anti-conservative for a safety gate,
non-blocking here only by a wide (44%→36%) margin that has nothing to do
with the formula's own accuracy. **Rule, forward: a future cycle that
ships an R27-satisfying gate whose own causal position is later found to
sit downstream of the cost it purports to control, on this or any
T28-adjacent channel, in any form, fires Checkpoint criterion 4
automatically, no further deliberation** — a single-instance-ratified,
forward-firing model, matching R16/R21/R22/R23/R24/R25/R26/R27's own
precedent. Same-shift fix: `NOTES.md` annotated (§7); the actual code
reposition (`chunk_runner.py` consulting the gate before its own r=312
`Sim.run()` calls) is Iteration-88's own Tier-1 item, not attempted here
(a real code change, not an annotation).

### R4 — Third addendum: a Phase-2 Red Team audit's own multi-cycle claims must be independently verified per-cycle before they are trusted forward

**Third addendum (Iteration 87, exp-110), extending the R4/Addendum-1
lineage to name Phase-2 Red Team audits explicitly, discharging the
"pattern to watch" LOGBOOK opened at Iteration 82.** Iteration 82 (exp-105)
found THERMODYNAMICS' own self-review catching that "Red Team's own
Phase-2 audit repeated the identical wrong [dominance-ratio] figures while
explicitly claiming to have independently re-checked them," and ruled:
"flagged forward as a pattern to watch, not yet a rule (one instance; a
second would be grounds for extending the R4/Iteration-50 addendum's text
to name Phase-2 Red Team audits alongside Phase-5 reviewers)." **This
cycle is that second instance** (§2, above): THERMODYNAMICS' own Phase-2
critique originated a claim about "Iteration 83's own r=312 defer"
happening "by a human reading printed per-chunk wall times and manually
stopping" and about `COST_GATE_*` being reused "invoked only in prose"
across "exp-105 through exp-108 (four-plus cycles)"; my own Phase-2 Red
Team audit repeated and extended this claim TWICE (§1.5, §4) while
verifying only an exp-108-directory-scoped grep, never opening exp-105/
106/107's own source; Phase-3 synthesis then ratified the unverified
multi-cycle claim into R27's own permanent founding-instance text. Caught
only at Phase 5, by MATERIALS, independently reading all three prior
cycles' own `run.py` directly — exactly the check R4's own first addendum
already required of "any later Phase-5 reviewer," and exactly the check
neither THERMODYNAMICS' own critique nor my own Phase-2 audit performed
before the claim reached a permanent, ratified rule text. **Rule,
extended: a Phase-2 Red Team audit's own claim about MULTIPLE PRIOR
CYCLES' collective behavior (a "this pattern spans N cycles" framing) must
be independently verified against EACH named prior cycle's own primary
source — not only the cycle immediately under review — before it is
trusted, adopted into a mandatory-fix docket, or, especially, ratified
into a new standing rule's own founding-instance narrative. A
single-cycle-scoped check does not license a multi-cycle historical
claim.** **Does not fire on its own founding/consolidating instance**
(this cycle) — matching R5's own two-occurrence-before-generalization
precedent (Iteration 47's own addendum) rather than the single-instance-
ratified R16-lineage model, since this addendum's own text is what
Iteration 82 explicitly reserved for "a second instance." **Standing
forward clause: a THIRD instance of a Phase-2 Red Team audit's own
unverified multi-cycle claim reaching a frozen, ratified record, on this
or any channel, fires Checkpoint criterion 4 automatically.**

---

## 6. Combined Verdict

**NOTES.md's own claimed Combined Verdict, "PROMISING," does not stand.**
All six blind Phase-5 reviews independently, without seeing one another's
work, landed **CONFIRM-WITH-GAPS** — a unanimous six-of-six departure from
the Director's own label, none of the six overridden by this audit on any
substantive point. I adopt the substance of that unanimous verdict, but
correct its housing in this program's own taxonomy: "CONFIRM-WITH-GAPS" is
the label individual Phase-5 seats use to grade a document's OWN claimed
verdict, not itself a Combined-Verdict category this program's LOGBOOK has
ever used. Cast in the house PROMISING/PARTIAL/RULED-OUT taxonomy — the
one every T28 governance cycle since Iteration 82 (exp-105 through
exp-109, five consecutive cycles, with no exception) has actually used —
this cycle's own pattern is textbook **PARTIAL**: not RULED OUT (nothing
foreclosed; T1 correctly N/A throughout); not PROMISING (a real,
independently-derived gap cluster survives Phase-3 freeze — MATERIALS'
own R4-class citation defect inside R27's own founding text, which
propagated through my own Phase-2 audit twice; THERMODYNAMICS' causal-
positioning gap, missed by six review layers including mine; a logic
error in the Director's own Phase-4 Interpretation prose; a first-use-
instrument construction gap; an interpretive under-statement — none
individually fatal, together denser than a clean landing carries); real,
disclosed, independently-reproduced progress on every other axis (item
1a/1b/2/3 clean; the grounding-fact/data-persistence gap genuinely,
permanently closed; R23 honored byte-exact; all eight Phase-2 mandatory
fixes genuinely, not merely claimed, implemented).

**Combined Verdict, corrected: PARTIAL.**

This is not a rejection of MATERIALS' own explicit dispute so much as a
refinement of its housing: MATERIALS is right that "PROMISING is not
earned while [the R27 citation defect] stands uncorrected," and every
other seat's own independent verdict agrees in substance (none used
"PROMISING," all six used the program's own standard signal for "real
gaps, not a clean landing") — PARTIAL is that signal's correct name in
this program's own established Combined-Verdict vocabulary.

---

## 7. Same-shift corrections (applied directly, this audit — zero re-run,
## zero verdict-arithmetic change)

The following are fixed by direct, disclosed annotation — matching
exp-106/107/108/109's own precedent of Red Team applying same-shift fixes
directly to the frozen record, and this program's own "annotate, don't
silently rewrite" convention (T10):

1. **`NOTES.md`'s R27 paragraph** — corrected "Founding instance: exp-105
   through exp-108 (four-plus cycles)…" to state the true pattern
   (exp-105/106: hardcoded upstream conditionals, no named constant;
   exp-107: named constant, wired upstream; exp-108 alone: named,
   unenforced) — MATERIALS' finding, §2 above.
2. **R27's forward-elevating clause** — restated with the same explicit
   "on this or any T28-adjacent channel, in any form" generalization
   language R16/R21 already use (THERMODYNAMICS' Ambiguity 1).
3. **R27's "Founding instance" label** — relabeled to name exp-110 (the
   ratifying/fixing cycle) per this registry's own universal convention,
   rather than the antecedent cycles (THERMODYNAMICS' Ambiguity 2).
4. **`NOTES.md`'s Interpretation paragraph** — the common-mode-blindness
   hedge corrected to state the true risk direction (RESOLVED calls carry
   the disclosed risk; UNRESOLVED calls, including both named bins, are
   if anything reinforced by the same mechanism) — VISION's finding, §3
   above.
5. **`NOTES.md`'s Result section** — THERMODYNAMICS' causal-positioning
   finding (§1) and EM's formula-bias finding (§5, R28) disclosed
   explicitly, alongside a note that `run.py`'s own "abort r=312 leg"
   comment (line 70) overclaims the gate's actual current capability.
6. **`NOTES.md`'s Result section** — QUANTUM's `floor==0`/`resolved`-mask
   finding disclosed as a known, non-firing-on-real-data construction gap.
7. **`NOTES.md`'s Result section** — PHOTONICS' margin-independence/
   bimodal-separation finding (both named bins UNRESOLVED at all 6
   margins, `local_snr` in 0.06–0.40 (r=156)/0.13–0.39 (r=312), a clean
   bimodal gap from the RESOLVED population) stated explicitly, not left
   implicit in `results.json["local_diag"]`.
8. **Combined Verdict** — corrected PROMISING → PARTIAL (§6).
9. **`phase2_critique_thermodynamics.md` and `phase2_redteam_audit.md`**
   (this cycle's own frozen Phase-2 documents) — flagged, not rewritten,
   with a pointer to this audit's §2 correcting the "manually stopping"
   characterization of Iteration 83/exp-106 and the "four-plus cycles"
   claim.

Two items are named but explicitly NOT attempted same-shift (real code
changes, not annotations — Iteration-88's own job, per R25's own
discipline, given their own numbered Tier-1 lines in §8 below):
repositioning `cost_gate_check()` upstream in `chunk_runner.py` (R28's
own remedy), and the split symmetric/asymmetric (plus QUANTUM's
purely-symmetric degenerate-case) fault-injection control for
`mirror_pooled_floor`/`classify_item_i_local`.

---

## 8. Reconciled Iteration-88 queue

**Tier 0 — governance, cheap, same-shift-adjacent (mostly discharged by
this audit; remainder is bookkeeping)**

0. (carried, unchanged, all six reviews independently confirm) Rule on the
   Iteration-85 Checkpoint-4/R24 firing — Marsh's call, still pending,
   out of scope for any Panel proposal.
1. R27 text corrections (§7 items 1–3) — **applied this shift.**
2. R28 ratified (§5) — **done, this audit.**
3. R4 Third Addendum ratified (§5) — **done, this audit.**
4. NOTES.md Interpretation/Result annotations (§7 items 4–7) — **applied
   this shift.**
5. Combined Verdict correction (§7 item 8) — **applied this shift.**

**Tier 1 — real cross-seat convergence (named in every one of six Phase-5
reviews' own top-3, in some form)**

1. **Execute the queued fault-injection control for `mirror_pooled_floor`/
   `classify_item_i_local`, both sub-cases, sharpened per QUANTUM's own
   finding.** (a) an injected ASYMMETRIC synthetic perturbation (already
   planned); (b) an injected SYMMETRIC/common-mode synthetic perturbation,
   including — per QUANTUM's own Phase-5 finding — an explicit
   purely-symmetric/zero-odd-component degenerate case exercising the
   `floor==0` branch, asserting `classify_item_i_local` either flags this
   case explicitly (a status distinct from `RESOLVED`) or documents why
   silent pass-through is acceptable. Zero new FDTD; named in all six
   Phase-5 reviews' own top-3, the single strongest cross-seat consensus
   item this cycle produced.
2. **Reposition the R27/R28 cost gate genuinely upstream of the spend**
   (THERMODYNAMICS' own #1; this audit's own R28 remedy): have
   `chunk_runner.py` itself call `cost_gate_check()` — using r=156's own
   already-logged `total_wall_time()` figures — before attempting r=312's
   first `Sim.run()` call, and refuse to proceed (rather than merely
   informing a downstream analysis step) if it fails. Zero new FDTD,
   reuses existing logged data. Directly discharges R28's own founding
   gap before a future cycle's pilot genuinely blows the budget on a
   heavier geometry.
3. **PHOTONICS' own independent, non-differencing floor check** (a
   `cpl`-refinement spot check) at the two named bins (−146.25° at r=156,
   +168.75° at r=312) — named in five of six Phase-5 reviews' own top-3
   (THERMODYNAMICS, QUANTUM, PHOTONICS, EM, VISION). The only instrument
   that can actually discriminate genuine common-mode-masked structure
   from pure discretization noise at these two bins — no amount of
   further work on the mirror-floor construction itself can close this
   (§3's own conclusion). Genuine new FDTD, correctly deferred a second
   cycle now.
4. **Apply an empirical safety margin (or the measured `x≈3.2` exponent)
   to `cost_gate_check()`'s own projection formula** (EM's own #1;
   R28's own companion caution) before it is relied upon at a tighter
   margin or a different `kappa_ratio` than this cycle's fixed `2.0`.

**Tier 2**

1. `R2_SMOOTH_THRESHOLD=0.90` re-derivation (queued since Iteration 86
   Tier 2b, now its own explicit line per exp-109's own split, still
   outstanding — named by QUANTUM's own #3 this cycle).
2. MATERIALS' own fabrication-tolerance quantitative bound for the mirror
   floor's disclaimer — literature-grounded percent-level azimuthal
   thickness/dose non-uniformity figure, propagated to a predicted
   angular-pattern deviation scale (MATERIALS' own #3, now a THIRD
   consecutive cycle naming this undone item).
3. State item 1c/1d's full per-margin table (not only the same-shift
   headline annotation applied above) in a proper Result-section pass —
   all six margins, the bimodal-gap framing, the 3.5×–30× figure
   (PHOTONICS' own #2).
4. `CLOSURE_CONFIRM`/`CLOSURE_FALSIFY` dead-code cleanup — one-line
   removal, inherited vestigial constants (THERMODYNAMICS' own minor
   finding, §3 of `phase5_review_thermodynamics.md`).
5. A fourth r-point, r=624, testing THERMODYNAMICS' own `r^-1.16`
   fixed-abs projection (~52.6× margin, just above the 50× `box_dev`
   floor) — long-standing, unchanged since Iteration 85.

**Tier 3 — unchanged standing items**

The oblique-angle extension; the 750/450nm leg; the `G40` full-width leg
(now deferred many consecutive cycles); the x-wall admittance refit;
`PAD`-with-article survival; `box_dev`'s own thinning margin (~9.0× at
r=312, still unresolved, a different quantity from this cycle's own
noise-floor finding).

---

## 9. Summary table — the five findings

| # | Seat | Finding | Independently re-verified | Fires? |
|---|---|---|---|---|
| 1 | QUANTUM | `resolved` mask lacks `floor>0` guard (unlike `local_snr`) | Yes — code read + `results.json` scan (floor strictly positive, 2.3e-4–2.1e-3, all 12 real cells) | No |
| 2 | PHOTONICS | "narrows" understates evidence (3.5×–30× below K=1, all 6 margins, bimodal) | Yes — `results.json` `local_snr` values recomputed | No |
| 3 | THERMODYNAMICS | Cost gate sits downstream of 90.2% of spend | Yes — traced `chunk_runner.py`/`analyze.py` call chain myself, §1 | No (existing rules); **earns R28** |
| 4 | EM (self-review) | `kappa_ratio**3` underestimates real ratio by ~15% | Yes — recomputed from `results.json` raw wall times, §5 | No; folded as R28 companion caution |
| 5 | MATERIALS | R27 founding-instance narrative false (exp-108 alone, not "4+ cycles") | Yes — read exp-105/106/107's own `run.py` myself, §2 | No (R20 misses on section-scope); **earns R4 Third Addendum** |

**Checkpoint status: no criterion fires this cycle.** Two new standing
rules ratified (R28, R4 Third Addendum), both correctly non-firing on
their own founding/consolidating instances, both carrying forward clauses.
**Combined Verdict: PARTIAL** (corrected from the Director's own initial
PROMISING).
