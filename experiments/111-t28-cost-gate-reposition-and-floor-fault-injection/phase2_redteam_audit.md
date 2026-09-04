# Phase 2 Critique — RED TEAM (final pass), Panel Iteration 88, exp-111

**Charter** (verbatim, PANEL.md): attacks every proposal, speaks last and
hardest. Standard is NOT textbook-physics compliance. Kills internal
inconsistency, unfalsifiable claims, mechanisms that cannot be expressed as
simulation parameters, and proposals that quietly violate a target
constraint — especially #3. Never leads a cycle.

## 0. Method

Every consequential numeric or code-behavior claim below — the proposal's
own and each of the five Phase-2 critiques' own — was independently
re-derived this session by running Python against the real committed
source (`experiments/110-.../run.py`, `chunk_runner.py`,
`experiments/110-.../results.json`) or by direct source reads, not by
trusting a critique's own report of what it found (R4/R4-Third-Addendum
discipline, applied to my own review of the five critiques as well as to
the proposal). Every number reported below reproduced. Details in §1.

## 1. Independent re-verification (numbers, not narrative)

**Cost/exponent chain** (own Python run against `results.json`):
`t156 = sum(r156.total_wall_s.values()) = 752.2232966423035`;
`t312 = sum(r312.total_wall_s.values()) = 6938.207038640976`;
`ratio = 9.223600318696624`; `ln(ratio)/ln(2) = 3.2053299988171697`.
**Matches the proposal's §2.0 `KAPPA_COST_EXPONENT` exactly**, and matches
all five critiques' own independent re-derivations.

**Floor range / `n_resolved`**: own scan of `results.json["r156"/"r312"]
["local_diag"]` gives floor range `2.3458052774092807e-4`–
`2.0959081684008007e-3`; `n_resolved` sums r156 `{24:32,32:34,40:36,48:34,
57:34,65:33}`=203/288, r312 `{24:36,32:38,40:40,48:36,57:36,65:36}`=222/288.
**Exact match** to §2.0's frozen table.

**Named bins**: `results.json["r156"]["named_bin_status"]` =
`{"margin32": {"deg": -146.25, "resolved": false}}`; `["r312"][...]` =
`{"deg": 168.75, "resolved": false}`. **Exact match.**

**Item 4 formula, all three cases**, computed independently: positive
`2.0**3.2053299988171697*1.10 = 10.145960350566288`; non-regression
`752.2232966423035*(2.0**3.2053...)*1.10 = 7632.027742505074` (`<10800` ✓);
discriminating case `pilot_total_wall_s=1349.875`: old (`kappa**3.0`, no
margin) `=10799.0` (PASS); new `=13695.778220666` (FAIL). **All exact.**

**§3 cost-projection table** (proposal's own disclosed formula,
`t156/t312 × cpl_ratio**3`, independently computed): cpl=25 → r156
`1469.19s`, r312 `13551.19s`, both `15020.37s = 4.172h`; cpl=30 → r156
`2538.75s`, r312 `23416.45s`, **both `25955.20s = 7.2098h`**. The
proposal's own table states cpl=30 "Both r" as "~6.5h" — **confirmed wrong,
independently, from the proposal's own formula and exp-110's own real
data**. `6.5h` is the r=312-*alone* column's own conversion
(`23416.45/3600=6.5046`). MATERIALS' finding is correct, exactly as
reported.

**`floor_degenerate`/`local_snr_*` interaction** (own numpy run, FI-C's
exact construction: `peccored[i]=3.0e-3+1.0e-6·(i-23.5)²`,
`hollow[i]=1.5e-3+4.0e-7·(i-23.5)²`, `n=48`, patched
`classify_item_i_local` reproduced verbatim from §2.1's diff): output
`floor=0.0`, `floor_degenerate=True`, `resolved=[False]*48` — **and**
`local_snr_peccored`/`local_snr_hollow` both `[inf, inf, inf, ...]`.
**QUANTUM's finding is real and reproduces exactly** — the patch as
specified leaves a live contradiction (`resolved=False` beside
`local_snr=inf`) in the same returned dict.

**Guard-placement / early-return order** (direct read of
`chunk_runner.py`'s committed `step_once`): current code is
`g = R.geom_fixedabs(r); ckpt_path, done_path = path_for(r, which); if
os.path.exists(done_path): ...; return True` — the existing early-return
for an already-DONE scene. The proposal's own diff inserts
`check_cost_gate_for_312()` as the unconditional first statement, i.e.
**before** `geom_fixedabs`, **before** the done-file check. **EM's finding
is real and independently confirmed from source**: a `step_once(312,
"empty")` status-check call on an already-completed r=312 scene now also
re-executes the gate, and none of the four listed control cases test this
state (all four assume "not yet done").

**"Sole `Sim()`/`.run(` caller" premise**: own
`grep -n "Sim(\|\.run("` across all of `experiments/110-.../*.py` confirms
`chunk_runner.py` is the only file constructing `Sim(...)` or calling
`.run(` — `analyze.py`/`finalize.py`/`linear_fit_control.py` do not.
Matches EM's and the proposal's own premise exactly.

**R23/DISCLAIMER occurrence count**: `grep -c -i
"DISCLAIMER\|R23\|predictions_text\|result_text"` against this cycle's own
`phase1_proposal.md` → **0**, confirming VISION's claim exactly. Extended
the check myself, per R4-Third-Addendum discipline (a critique's own
claim about *prior* cycles' behavior must be verified per-named-cycle, not
trusted): ran the identical grep against `experiments/107-t28-delta-scene-
r5-census-decision/phase1_proposal.md` and `experiments/110-t28-item-i-
local-norm-and-controls/phase1_proposal.md` — **both return 0**,
independently confirming the two prior instances VISION's critique cites
(exp-107 directly; exp-110 via Iteration 87's own LOGBOOK-recorded VISION
finding, which I did not merely re-quote but re-checked against exp-110's
own file). **If this cycle ships unfixed, it is a genuine, independently-
verified third instance of an identical silence pattern on this exact
document-family channel.**

**R23's own text, re-read directly** (LOGBOOK.md RULED OUT registry,
R23 full entry): the rule requires a code-level assert on a single
source-of-truth `DISCLAIMER` string, but **carries no three-strike/
forward-elevating clause of its own** — confirmed by cross-referencing
Iteration 85/exp-108's own Phase-5 audit text, itself found verbatim in
LOGBOOK: *"R23: ... but R23 itself carries no forward-elevating clause and
cannot, on its own text, fire Checkpoint 4."* This is a standing,
previously-litigated finding, not my own interpretation — I located and
read it directly rather than assuming VISION's framing. **VISION's own
critique this cycle is careful never to claim R23 itself auto-fires
(it draws an analogy to R16/R21/R22/R27/R28's OWN clauses, which is
accurate as an analogy, and correctly frames the consequence as "this
seat's verdict would harden toward oppose," not as an automatic
Checkpoint-4 trigger) — so there is nothing to override in VISION's
critique text itself.** What needs stating explicitly, for the record,
since the task asks it directly: a third R23-silence instance, standing
alone, does **not** automatically fire Checkpoint criterion 4 under any
rule currently on the books — only R16/R21/R22/R24/R25/R26/R27/R28 carry
that mechanism; R23 does not. This does not make the finding
non-mandatory — it is still real, cheap to fix, and exactly the kind of
density this program has previously converted into a new rule (R23 itself
was born this way) — but the escalation stakes are lower than the
"forward-elevating" framing might suggest to a reader skimming quickly.

**Guard math** (`floor_degenerate ⟺ floor==0.0` under real usage): own
check confirms `floor = K·max(floor_p, floor_h)`, both terms are
percentiles of `abs(·)` arrays (non-negative by construction), `K=3.0>0`,
so `floor≥0` always, and the real 12-cell floor minimum
(`2.3458e-4`) is strictly positive — matches EM's claim exactly.

## 2. Steel-man of the proposal as a whole (not repeating any single seat)

Independent of any one critique, this proposal is the cleanest T28
governance cycle I can independently verify in this sub-thread's own
record: every headline number in its own §2.0 grounding-fact table
reproduces exactly from real committed data (not one hand-typed figure
survives contact with source, except the single §3 cost-table cell below);
it caught, itself, before any critique touched it, that the Iteration-88
queue's own premise ("r=156's own already-logged wall times") was false in
this session, and scoped item 2's control around that fact rather than
fabricating numbers (the identical discipline Iterations 86/87 each had to
learn the hard way); it explicitly re-verifies T1 N/A against what THIS
cycle changes, not by copying exp-110's language; and it declines to
bundle item 3's genuine new-FDTD spend into a cycle whose own job is to
fix the gate that should protect that spend — a defensible, explicitly
reasoned sequencing argument, not a hidden drop.

## 3. Adopt/override disposition, per critique

- **PHOTONICS — ADOPT the substance, PARTIAL OVERRIDE on urgency/framing.**
  Independently confirmed: FI-A/B/C are the two pure mirror-parity
  extremes; this bench's own established `P*=2.8421°` T28 oscillation,
  aliased against this instrument's 7.5°/bin pitch (48 bins over 360°),
  would indeed produce neither a clean odd nor even pattern under `i↔47-i`
  pairing — a real, uncontested gap in the pattern's realism, not a coding
  error. **Override**: R18's own literal text (re-read directly, RULED OUT
  registry) requires a fault-injection *positive/negative control*, which
  FI-A (positive) and FI-B (negative) jointly satisfy — it does not require
  every plausible intermediate input shape. So I do **not** rule this an
  R18 violation blocking Phase 4 the way, say, EM's or QUANTUM's findings
  do. What I **do** adopt as mandatory: the proposal's own claim that this
  cycle "closes the last open R18 gap" is an overclaim against what the
  triad actually demonstrates (the two mathematical corners, not the
  aliased/mixed regime) — that claim must be narrowed in the frozen text,
  and PHOTONICS' own cheap, zero-new-FDTD FI-D case (a swept-phase
  quasi-periodic perturbation at `P*=2.8421°`) should be added this cycle
  since it costs nothing and directly strengthens rather than merely
  narrows the claim — but Red Team's own minimum bar is the narrowed claim,
  not literally requiring FI-D's construction (matching PHOTONICS' own
  stated flip condition, which accepts either).

- **MATERIALS — ADOPT in full.** The §3 table's cpl=30 "Both r" arithmetic
  slip reproduces exactly as MATERIALS reports, independently recomputed
  from the proposal's own disclosed formula against real exp-110 data
  (§1, above). Non-outcome-reversing for this cycle (item 3 isn't run) but
  load-bearing for whatever cost/scope call Iteration 89 makes off this
  exact table — must be corrected before freeze.

- **ELECTROMAGNETISM — ADOPT in full; this is the single most important
  finding in this cycle's five critiques.** Both attacks independently
  reproduce: (1) the proposal's own text never commits
  `gate_reposition_control.py` to patching the real imported
  `chunk_runner.build_sim` and calling the real `chunk_runner.step_once`
  unmodified, as opposed to a hand-copied reimplementation of the control
  flow — and R28's own founding-instance text (re-read directly, RULED OUT
  registry) exists *precisely* because a gate was "shown to branch," six
  review layers deep, without ever being traced against the real call
  site; a reimplemented mock in this cycle's own remedial fix would
  reproduce that exact gap one layer deeper, on the very rule this cycle
  exists to close. (2) The guard's unconditional placement ahead of the
  existing `if os.path.exists(done_path): return True` early-return is
  confirmed directly from the diff, and none of the four listed control
  cases exercises "r=312 already done, r=156 logs absent/stale" — a state
  that will legitimately occur on any resumed/status-check invocation.

- **QUANTUM OPTICS — ADOPT in full.** Independently reproduced in real
  numpy against FI-C's exact stated construction: the patched function's
  `resolved` correctly flips to `[False]*48`, but
  `local_snr_peccored`/`local_snr_hollow` remain `[inf]*48` in the *same*
  return dict — a live self-contradiction the proposed fix does not guard
  against, on a pre-existing ternary the patch leaves untouched.

- **VISION SCIENCE — ADOPT the substantive finding in full; PARTIAL
  OVERRIDE on escalation framing (stated for the record, not as a
  disagreement of substance).** Zero `DISCLAIMER`/R23 occurrences
  independently confirmed, and independently extended to confirm exp-107
  and exp-110's own Phase-1 proposals are the two genuine prior instances
  (checked directly, not merely cited). This would be a real third
  instance if shipped unfixed. Override, precisely stated: R23's own
  ratified text (re-read directly) carries no forward-elevating/
  three-strike clause the way R16/R21/R22/R24/R25/R26/R27/R28 do —
  confirmed by a standing, previously-litigated LOGBOOK finding
  (Iteration 85/exp-108's own Phase-5 audit) — so a third instance does
  **not** by itself automatically fire Checkpoint criterion 4 under any
  existing rule. This does not weaken the fix's mandatory status (below);
  it corrects only the stated stakes of *not* fixing it.

## 4. R25 check (item 3's deferral)

Read R25's full text directly (RULED OUT registry): it binds an *audit's*
disclosed-but-unexecuted fix to its own numbered Reconciled-queue line, not
a parenthetical. This proposal's own §3 is a full, separately-headed
section ("## 3. Item 3 scoping decision: DEFER"), not a parenthetical
buried in another item's prose, and ends with a concrete, dated
recommendation for Iteration 89 (`cpl=25`, r=156-alone-first, ~24.5 min).
As *written*, this satisfies R25's discipline. The residual risk is
downstream, not in this document: Phase 3's own Reconciled-Iteration-89
queue must carry this forward as its own explicit, numbered Tier-1 line —
not fold it into a subordinate clause of a different item, the exact shape
that caused R25's own founding instance (exp-106→107) and the near-miss
QUANTUM flagged at Iteration 86. Flagged below as a mandatory instruction
to Phase 3, preventatively — not yet a violation, since Phase 3 has not
run.

## 5. MANDATORY FIXES (Phase-3 synthesis must adopt before Phase 4 runs anything)

1. **[inconsistency]** Bind `gate_reposition_control.py`'s claim of
   "genuinely upstream" causal verification to the real production call
   chain, not an unstated reimplementation: assert explicitly that the
   patch target is `chunk_runner.build_sim` (the imported module's real
   attribute) and that the exercised call is the real, unmodified
   `chunk_runner.step_once(312, "empty")` — before Phase 4 trusts this
   control's result as evidence the gate sits upstream of `Sim.run()`.
   (EM, adopted in full — the cycle's single highest-priority fix, given
   R28's own founding-instance shape.)

2. **[inconsistency]** Add a fifth control case to
   `gate_reposition_control.py`: r=312's `done_path` already exists (a
   status-check on an already-completed scene) with r=156 logs
   absent/stale, and pin its predicted behavior (no-op `True`, or a raise,
   named explicitly) before Phase 4 runs — the guard as specified is
   unconditional and sits ahead of the existing early-return, so this
   state is reachable in real usage and currently untested. (EM, adopted
   in full.)

3. **[inconsistency]** Extend the `floor>0.0` guard (or an explicit
   `np.nan`/sentinel fill) to `local_snr_peccored`/`local_snr_hollow` in
   the same patch to `classify_item_i_local`, and add an assertion to
   `floor_fault_injection_control.py`'s FI-C case that neither array is
   `inf` when `floor_degenerate=True` — independently confirmed the
   pre-fix ternary otherwise ships a live `resolved=False`/`SNR=inf`
   contradiction in the same dict. (QUANTUM, adopted in full.)

4. **[inconsistency]** Correct §3's cost-projection table: the cpl=30
   "Both r" cell must read `~7.2h` (`25,955.2s`), not `~6.5h` — the latter
   figure belongs to the r=312-alone column. Regenerate the table by
   invoking a script rather than hand-typing conversions, per R4's own
   standing text, so this correction is itself independently checkable.
   (MATERIALS, adopted in full.)

5. **[inconsistency]** Extend `DISCLAIMER` (or its Iteration-88 successor
   string) with the three new scope caveats this cycle introduces —
   `floor_degenerate`'s new non-RESOLVED semantics; `KAPPA_COST_EXPONENT=
   3.2053`/`COST_GATE_SAFETY_MARGIN=1.10`'s single-geometry/single-
   `kappa_ratio` scope limit (currently free prose in §6 only); the gate's
   upstream reposition — and wire `build_predictions_text()`/
   `build_result_text()` to state them inline, with both
   `assert DISCLAIMER in ...` calls re-fired against the updated text,
   before Phase 3/4 freeze. Independently confirmed this would otherwise
   be a genuine third instance of an identical silence pattern on this
   channel (exp-107, exp-110, and this cycle if unfixed) — real and
   mandatory on R23's own discipline and this program's density-to-new-
   rule precedent, though (per §3, above) not itself an automatic
   Checkpoint-4 trigger under any rule currently on the books. (VISION,
   adopted in full on substance.)

6. **[inconsistency]** Narrow the Predictions/Result text's own claim that
   item 1 "closes the last open R18 gap": state explicitly that R18 is
   discharged for the two tested mathematical corner cases (pure
   odd/asymmetric, pure even/symmetric-or-degenerate), and that the
   realistic aliased/intermediate regime this bench's own established
   `P*=2.8421°` T28 oscillation would produce at these exact bin pitches
   remains untested by this triad. Strongly recommended, not strictly
   required, to additionally add PHOTONICS' own proposed FI-D case
   (a swept-phase quasi-periodic perturbation at `P*=2.8421°`) this same
   cycle, since it costs zero new FDTD and would let the claim stand
   unnarrowed instead. (PHOTONICS, adopted on substance with the override
   in §3 above on how it must be discharged.)

7. **[process instruction, not an attack]** Phase 3's own Reconciled-
   Iteration-89 queue must carry item 3's deferral forward as its own
   explicit, numbered Tier-1 line (this proposal's own §3 recommendation:
   `cpl=25`, r=156-alone-first, protected by this cycle's repositioned
   gate) — not folded into a parenthetical or a subordinate clause of a
   different item, per R25's own text. Preventative: no violation has
   occurred yet, since Phase 3 has not run, but this is the exact failure
   shape R25 exists to prevent and the exact shape a prior cycle
   (exp-106→107) already fell into once.

None of the seven items rises to **unfalsifiable**, **inexpressible**, or
any **constraint-#N-violation** tag — T1 is correctly, structurally N/A
across items 1/2/4 (a boolean guard, orchestration ordering, and a
wall-clock projection formula touch no σ(I)/σ(x,t)/angular-selectivity/
sub-threshold content), and item 3, the one item with any physical
content, is untouched this cycle. All seven are internal-inconsistency-
shaped: a claim of completeness, causal position, or arithmetic that the
cycle's own code or text does not yet fully support.

## 6. Overall verdict

**PROCEED-WITH-MANDATORY-FIXES.**

The proposal's own numeric discipline is the strongest independently-
verified batch in this sub-thread's recent record — every claim except
one hand-typed table cell reproduced exactly, on direct re-derivation, and
its own §2.0 self-check already caught and correctly scoped around a real
grounding-fact error before any critique touched it. Nothing found rises
to internal inconsistency that cannot be closed by a same-shift code/text
patch, no claim is unfalsifiable, no mechanism is inexpressible as
simulation parameters, and T1/constraint-3 are correctly, verifiably N/A
throughout. The seven fixes above are exactly the kind of governance-layer
gap this sub-thread's own registry (R18, R23, R25, R28) already exists to
catch before freeze, not after — catching them now, at Phase 2, is the
process working as designed, not evidence of drift.

## 7. Checkpoint criteria implicated

**None.** Checked directly against PANEL.md's own five-item list:
(1) no constraint-metric PASS is claimed or attempted this cycle;
(2) no mechanism-class boundary is proven or attempted;
(3) no engine physics beyond the validated bench classes is invoked —
this is pure code/governance;
(4) program-integrity drift (unfalsifiable claims, a constraint quietly
dropped) — not found: every issue above was caught blind, at Phase 2,
before any Phase-3 freeze, by five independent critiques plus this
audit's own from-primitives re-verification, which is this program's own
established non-firing precedent for every prior founding-instance rule
in the registry (R5–R28 uniformly); T1/constraint-3 are not dropped, they
are correctly stated N/A;
(5) is a Phase-5/cross-iteration judgment, out of scope for a Phase-2
audit.
