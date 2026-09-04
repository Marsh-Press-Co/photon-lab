# PHASE 5 — THERMODYNAMICS REVIEW · Panel Iteration 87 (exp-110)

*Fresh sub-agent, blind to every other seat's Phase-5 output this cycle.
Charter: where absorbed energy goes; what re-radiates and whether it would
be detectable; owns the per-proposal energy sidecar (post-run analytic,
labeled as such). Not lead this cycle (EM led). Own Phase-2 critique this
cycle flagged Fix 5 (cost gate unwired) and Fix 6 (`wall_time_source`
unused) — both independently re-checked from source below, not taken on
the strength of my own earlier claim.*

## 0. Method

Read PANEL.md, LOGBOOK.md in full (RULED OUT R1–R26, T28 Iterations
83–86), and every file in `experiments/110-.../`: `phase1_proposal.md`,
all five `phase2_critique_*.md`, `phase2_redteam_audit.md`, `NOTES.md`,
`run.py`, `chunk_runner.py`, `analyze.py`, `finalize.py`,
`linear_fit_control.py`/`_output.json`, `results.json`. Every figure below
was independently recomputed — either by direct arithmetic on
`results.json`'s own persisted primitives, or by importing and invoking
`run.py`'s own committed functions — never taken on NOTES.md's or Red
Team's own say-so.

## 1. Fix 5 (cost gate) — genuinely wired as code, but with a causal-positioning gap not caught by any prior layer

**What I confirmed lands.** `run.py::cost_gate_check(pilot_empty_wall_s,
pilot_total_wall_s)` is real code (lines 340–357): it computes
`pilot_pass`, projects `r=312`'s total via `kappa_ratio**3`, computes
`total_pass`, and returns `proceed_to_r312`. `analyze.py`'s call site
(line 106: `cost_gate = R.cost_gate_check(pilot_empty, pilot_total)`) is
the ONLY call anywhere in this cycle's tree (`grep -rn
"cost_gate_check"` → one definition, one call, confirmed) and it
genuinely branches on the result (line 113:
`if cost_gate is not None and cost_gate["proceed_to_r312"]:` — gating
whether `r312`'s data enters `results.json` at all, and setting
`r312_deferred` accordingly). This is a real, executed structural
improvement over `COST_GATE_PILOT_S`/`COST_GATE_TOTAL_S`'s own
four-cycle history (exp-105→108) as two referenced-in-prose,
never-imported constants — independently reconfirmed by direct grep of
`experiments/108-.../chunk_runner.py` and `analyze.py`: zero hits beyond
the two definitions, exactly as my own Phase-2 critique and Red Team's
audit (§1.5) found.

**From-scratch recomputation, R4 discipline (not hand-typed).** I
imported the actual committed `run.py` and called
`cost_gate_check(250.6266098022461, 752.2232966423035)` — the exact
`pilot_empty_wall_s`/`pilot_total_wall_s` figures in `results.json`'s own
`cost_gate` field (`752.2232966423035` is itself independently verified
to be the sum of `r156`'s three per-scene wall times, `250.6266098022461
+ 250.08318996429443 + 251.51349687576294`, matching to full float
precision). The result reproduces `results.json`'s own persisted
`cost_gate` dict **bit-exact on every field**:
`pilot_pass=True, kappa_ratio=2.0, projected_312_total_s=6017.786373138428,
total_pass=True, proceed_to_r312=True`. Fix 5 is genuinely executed,
committed-function output, not asserted.

**The gap: the gate is causally incapable of preventing the spend it
exists to gate — undisclosed anywhere in NOTES.md.** Tracing the actual
call chain (not just grepping for the function name, per the charge in
this seat's brief): `cost_gate_check()` is called ONLY inside
`analyze.py`, and only AFTER `r=156`'s three captures are already
complete and analyzed (its own two inputs, `pilot_empty`/`pilot_total`,
are `r=156`'s own MEASURED wall times — they cannot exist before the
`r=156` `Sim.run()` calls have already finished). `analyze.py` then
checks `have(312, "empty")` etc. to decide whether to analyze `r=312` —
but `chunk_runner.py`, the only code anywhere in this cycle that actually
calls `Sim.run()`, **never imports, calls, or reads `cost_gate_check()`
or any of its outputs anywhere** (confirmed: `grep -n "cost_gate"
chunk_runner.py` → one docstring mention only, zero executable
reference). `chunk_runner.py` is invoked per-`(r, which)` pair by
whatever foreground Bash calls the operator issues — there is no
orchestrator in this tree that consults the gate *before* deciding
whether to invoke `chunk_runner.py` for `r=312`.

Quantified: `r=312`'s own three captures cost `2334.8423988819122 +
2232.955216884613 + 2370.4094228744507 = 6938.207038640976s` —
**90.2% of this cycle's entire `7690.430335283279s` wall-clock spend**
(independently summed and cross-checked bit-exact against the persisted
`total_wall_s`). By construction, that spend was already complete before
`cost_gate_check()` could have been evaluated even in principle (its own
inputs did not yet exist), and the code that actually runs `Sim.run()`
never consults it at all. In this cycle the gate happened to clear
(`proceed_to_r312=True`) so nothing was wasted in fact — but had the
`r=156` pilot come in over budget, `r312_deferred=True` would have been
written and `results.json["r312"]` withheld from the analysis, while the
6,938s of `r=312` FDTD compute would have **already been spent
regardless**, since nothing upstream of `analyze.py` ever asks the gate's
permission. This is a materially different thing than what `run.py`'s
own comment claims the gate does ("**abort** r=312 leg if the pilot
exceeds this," line 70) and than what R27's own founding narrative holds
up as the standard being restored (Iteration 83's precedent: "the
primary leg's own empty pilot... cleared the threshold and committed" —
i.e., a check that gated the *decision to spend*, not merely the
*decision to trust already-spent output*). NOTES.md's Idealizations
(item 1's own R27 paragraph) states only that "item 1's r=312 analysis
is reported NOT-RUN, not silently skipped" — narrowly, technically
accurate about what the code does — but nowhere discloses that the gate
cannot prevent the underlying `Sim.run()` spend, which is the actual cost
a "cost gate" exists to control. **None of the five Phase-2 critiques nor
Red Team's own audit caught this** — all confirmed the gate exists and
branches (a `grep`-level check), none traced whether the branch sits
upstream or downstream of the cost it gates.

This is not a fresh instance of R23/R24/R25 (same reasoning Red Team
applied to the pre-fix gap in §4: none of the three rules' literal
triggers are met — there is no prior "adopted in full" claim about THIS
specific causal-positioning property, and this is this exact gap's own
first appearance). It also does not retroactively undo R27's founding
ruling (Fix 5 genuinely satisfies R27's own literal text — "enforced by
executable code that actually branches on it and records the outcome" —
which says nothing about WHERE in the pipeline the branch must sit). It
is, however, a real, previously-uncaught, disclosure-worthy gap: Fix 5 is
letter-complete, substance-incomplete relative to its own motivating
language.

## 2. Fix 6 (wall-time attribution) — genuinely landed, cleanly verified

`finalize.py` (lines 65–76) builds `wall_time_source` from
`results.json`'s own already-summed `total_wall_s`
(`7690.430335283279` → formatted `"7690.4s (128.17 min)"`) plus the
six individual per-scene figures, explicitly stating it is "distinct from
exp-108's own historical 7712.0s/6-call figure." This is passed into
`R.build_result_text(..., wall_time_source=wall_time_source)` — the
**only** call site of `build_result_text()` anywhere in this cycle's tree
(confirmed by grep), closing exactly the gap I flagged at Phase 2
(exp-108/109 defined `build_result_text()`'s `wall_time_source` parameter
but never called it with a real value; exp-108 itself never called the
function at all). I independently recomputed `7690.4/60 = 128.17383...`
→ rounds to `128.17`, matching. `7690.4s` is genuinely, arithmetically
distinct from `7712.0s` (a ~21.6s difference, consistent with a fresh
6-call re-capture of bit-identical geometry rather than a copy of the old
figure) — not a coincidental near-match that could be mistaken for
reused data. The identical string reaches `NOTES.md`'s own Result section
verbatim (byte-compared: `results.json["result_text"]`'s wall-time
sentence and NOTES.md's own quoted block match exactly, including the
per-scene breakdown). **Fix 6 landed cleanly and fully — no gap found.**

## 3. T1 (energy ledger) — genuinely N/A, independently confirmed, one hygiene note

Grepped every `.py` file and `NOTES.md` in this cycle's tree for
`ledger_check`, `closure`, `core_frac`, `thermal`, `netd`, `emission`,
`re-?radiat`, `temperature` (case-insensitive): the only hits anywhere
are `CLOSURE_CONFIRM = 0.001` / `CLOSURE_FALSIFY = 0.01` (`run.py:85–86`)
— two module-level constants inherited byte-for-byte from exp-108's own
shared header block, **never referenced again anywhere in this cycle's
code** (a second grep for the identifiers themselves confirms zero
further hits). `reproduction_precondition()` does compute genuine
absorbed/extinction cross-sections (`sigma_abs`, `sigma_ext`,
`abs_ext_ratio` via `sc.widths()`), but strictly as a REPRODUCTION gate
against exp-106's already-published, already-reviewed ledger figures —
matched to `<1e-6` relative and reported PASS/FAIL, never interpreted,
extended, or cited toward any new absorbed-power, thermal, or
re-radiation claim. No `Sim`-level thermal sidecar, NETD row, or emission
calculation is built, called, or persisted anywhere. **T1: N/A is
genuinely, structurally confirmed** — independently re-derived here, not
merely accepted from the proposal's or Red Team's own claim.

One minor, non-blocking hygiene note, worth naming precisely because it
is the same *shape* of defect this cycle's own Fix 5/R27 was built to
police, even though R27's own text (scoped to "cost, safety, or scope"
gates) does not literally apply to it: `CLOSURE_CONFIRM`/
`CLOSURE_FALSIFY` are dead code this cycle — defined, unused, inherited
via the "byte-for-byte reused" constants block. Harmless (they gate
nothing, mislead nothing, and are never read), but worth a one-line
Iteration-88 cleanup so a future reader does not have to re-derive, as I
just did, that they are vestigial rather than silently load-bearing.

## 4. R27 as a governance artifact — reasonably well-specified, two real ambiguities

Assessed independent of whether R27 should exist (it should — the
underlying four-cycle gap was real and Red Team's Phase-2 §4 ruling that
none of R23/R24/R25 literally fired is correct on my own re-check of
each rule's operative text against `COST_GATE_*`'s own history).

**Trigger: clear.** "A numeric cost, safety, or scope gate... defined as
a module-level constant, and referenced only in prose/docstring/
Idealizations language, is not a gate at all until it is enforced by
executable code that actually branches on it and records the outcome" is
a concrete, checkable condition (exactly the `grep`-for-enforcement test
Red Team and I both applied). **Founding-instance-does-not-fire: present
and stated**, but see the labeling issue below. **Forward-elevating
clause: present**, matching the single-instance-ratified model R16/R21–
R26 all share.

**Ambiguity 1 — the forward clause is narrower-worded than its siblings',
possibly unintentionally.** R16's and R21's own forward clauses each
explicitly generalize scope in their own text: "on this or any
T28-adjacent channel, in any form." R27's forward clause reads only "a
future cycle that reuses **a** documented numeric gate a second time
without executable enforcement" — it does not restate that
generalization. Read against R27's own founding-paragraph definition
("a numeric cost, safety, or scope gate (**e.g.** `COST_GATE_*`)" — the
"e.g." signaling the rule is not meant to be scoped to those two named
constants specifically), the forward clause is PROBABLY intended to
cover any future differently-named gate of the same shape, not only a
literal second un-enforcement of `COST_GATE_PILOT_S`/`TOTAL_S`
specifically (an unlikely recurrence now that Fix 5 exists) — but the
forward clause's own sentence does not say so explicitly the way its two
closest siblings do, leaving a future Red Team auditor to infer scope
from the founding paragraph rather than read it directly off the
operative forward-firing sentence.

**Ambiguity 2 — "Founding instance" is labeled inconsistently with every
other rule in this registry.** R27's own text: "Founding instance:
exp-105 through exp-108 (four-plus cycles) each reused
`COST_GATE_PILOT_S`/`COST_GATE_TOTAL_S`..." — naming the ANTECEDENT,
pre-rule cycles as "the founding instance." Every other rule in
LOGBOOK's registry (R5 through R26, checked directly against each one's
own text) instead labels the CURRENT, ratifying cycle as its "founding
instance" or "founding case" — even where, as in R20's own text, the
underlying pattern traces back further ("Founding case: exp-099's own
`NOTES.md` accumulated FIVE total instances across its lifecycle"' —
the founding case is still the current document, not the antecedent
one). exp-110 is this cycle's own actual ratifying/fixing cycle, but
R27's text never assigns it that label — it is only implied by the
"does not fire on its own founding instance" sentence that follows.
A future reader checking whether exp-110 itself counts as "the founding
instance" (relevant if a future audit ever needs to count instances
toward the forward clause) must infer it rather than read it stated
plainly, the one place in this registry where that inference is needed
at all. Non-blocking this cycle (exp-110 both ratifies and fixes the gap
same-shift, so no live ambiguity results), but a real drafting
inconsistency relative to this program's own established convention,
worth a one-line correction if R27's text is ever touched again.

Neither ambiguity is severe enough to make R27 unusable as written — a
future auditor applying ordinary interpretive care reaches the sensible
reading either way — but both are genuine, checkable specification gaps,
independently found here, not restating any other seat's or Red Team's
own language (R27's text as drafted was authored this same cycle and had
not yet been Phase-5-reviewed by any seat when I read it).

## 5. Verdict on this cycle's Combined Verdict claim

**CONFIRM-WITH-GAPS.**

Every object-level physical/instrumentation claim reproduces exactly from
primitives: item 1a's reproduction figures (`sigma_abs`/`sigma_ext` at
both r, `<1e-9` relative — I independently confirmed `rel_dev=0.0`
exactly), item 1b's 48/48-bin persistence at all 6 margins both r, item
1c/1d's bin counts (`203/288=70.5%` r=156, `222/288=77.1%` r=312,
independently re-summed from `n_resolved`/`n_total` — both PHOTONICS-
named bins UNRESOLVED-BY-CONSTRUCTION, matching NOTES.md exactly), item
2's four synthetic triples (bit-exact against `linear_fit_control_output.
json`), and item 3's `rel_diff_truncated=1.999` are all genuinely,
independently reproduced, not merely restated. T1 is genuinely N/A. Fix 6
landed cleanly. R23 is genuinely live-fired (both `DISCLAIMER` asserts
confirmed present in the persisted text fields).

The gap is Fix 5: real, executed, non-hand-typed code that satisfies
R27's own literal text — but, traced through the actual `chunk_runner.py`
→ `analyze.py` call chain rather than merely grepped for, the gate sits
downstream of 90.2% of this cycle's own wall-clock spend and is
structurally incapable of aborting the costly leg the way its own
motivating language (`run.py`'s "abort r=312 leg" comment; R27's own
Iteration-83 precedent narrative) claims. This did not reverse any
outcome this cycle (the gate cleared; the spend was in fact affordable)
and is not a fresh instance of any existing R-rule — but it is a real,
independently-derived, previously-uncaught gap that NOTES.md's own
"every one of the eight Phase-2-mandated fixes genuinely implemented and
verified, not merely claimed" language overstates for Fix 5 specifically,
and Combined-Verdict "PROMISING" does not disclose. Plus the two R27
specification ambiguities above (§4) and the CLOSURE_CONFIRM/FALSIFY
dead-code hygiene note (§3) — none individually severe, together a real
gap cluster on a cycle whose Combined Verdict claims a clean landing.

## 6. Ranked top-3 candidate directions for Iteration 88

1. **Reposition the R27 cost gate upstream of the spend, not merely
   downstream of it.** Concretely: have `chunk_runner.py` itself call
   `cost_gate_check()` (using `r=156`'s own already-logged
   `total_wall_time()` figures, already computed by the existing
   wall-time log) before attempting `r=312`'s first `Sim.run()` call, and
   refuse to proceed (raising or printing a clear abort message) rather
   than silently letting the operator invoke it regardless. Zero new
   FDTD cost, reuses existing logged data, directly closes §1's gap
   before a future cycle's pilot genuinely blows the budget on a
   72-minute-heavier geometry.
2. **PHOTONICS' own already-queued Iteration-88 fault-injection control**
   for `mirror_pooled_floor`/`classify_item_i_local` — split into (a)
   asymmetric (planned) and (b) symmetric/common-mode (Red Team Fix 2) —
   is the single highest-value physics-adjacent item still open on this
   sub-thread and was correctly deferred, not skipped, this cycle; it is
   the only way to learn whether the two PHOTONICS-named bins' still-
   unresolved status (§1c/1d, this cycle's own genuine finding) reflects
   real common-mode-masked structure or pure noise.
3. **One-line R27 text correction** (§4 above): restate the forward
   clause with the same explicit "on this or any T28-adjacent channel, in
   any form" generalization language R16/R21 already use, and relabel
   "Founding instance" to name exp-110 (the ratifying/fixing cycle)
   rather than the antecedent exp-105–108 cycles, matching every other
   rule's own convention — cheap, zero-FDTD, closes an ambiguity before
   it is ever load-bearing for a real forward-clause count.
