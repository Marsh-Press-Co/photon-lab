# PHASE 5 — RED TEAM FINAL AUDIT · Panel Iteration 84 (exp-107)
## "The Properly-Powered R5 Census, a Ground-Truth Recovery Gate, and Three Zero/Low-Marginal-Cost `kappa_window` Closeouts"

*Fresh context. Receives everything: `phase1_proposal.md`, all five Phase-2
critiques, `phase2_redteam_audit.md`, `NOTES.md`, `results.json`, `run.py`,
`chunk_runner.py`, `finalize.py`, `run_output.txt`, `checkpoint_validation.txt`,
and all six blind Phase-5 reviews. Mandatory reading completed in full:
LOGBOOK.md (RULED OUT R1–R24, ESTABLISHED, LIVE THREADS including T28's full
history), PANEL.md, PLAN.md's Current state, exp-106's NOTES.md/
`phase5_redteam_audit.md` (own closing paragraphs read with particular care —
§2/§6 below), exp-100's NOTES.md/`disposition_memo.md`. Every numeric claim
below that mattered to a ruling was independently re-derived from primitives
(`results.json`, `run.py`/`run_output.txt`, direct arithmetic), not taken on
any review's or LOGBOOK's own word — including the two items this task
flagged for special scrutiny (§0.1, §2).*

---

## 0. Independent re-verification from primitives

**0.1 PHOTONICS' R9-class T9-anchor-blending finding — CONFIRMED, exactly.**
`results.json::item1_rows`: `delta_abs_ext_ratio(156) = -2.96857069029266e-05`,
`(312) = -2.468427690099917e-05`. Against the *like-for-like* T9 anchor
(exp-027, `+1.56×10⁻⁶`, the same `sections.widths()` box-ledger channel):

```
2.96857e-5 / 1.56e-6 = 19.03  ->  19.0x  (r=156)
2.46843e-5 / 1.56e-6 = 15.82  ->  15.8x  (r=312)
```

matches PHOTONICS' review digit-for-digit. `exp-031`'s `6.8×10⁻⁶` is, per
LOGBOOK's own T9 entry, a *different measurement channel* (single-angle
ambient Weber-contrast, not a radial/box-ledger absorbed-power delta) —
blending it into "the T9-established near-zero order" is the exact
same-signal-different-normalization shape R9 exists to catch. This does not
reverse `item1_pass=True` at either r (both deltas remain 2–3 orders of
magnitude below `abs_ext_ratio` itself, ~0.49–0.50) but the Result section's
"roughly an order of magnitude above the T9 anchors" phrasing understates a
genuine ~15–20x (1.2+ decade) gap. **ADOPTED, annotated directly into
NOTES.md** (§7, below).

**0.2 The exp-106-code-fix carryover question — independently re-derived
from primitives, not taken from the consolidated secondhand summary.** Three
separate documents checked directly:

1. **exp-106's own `phase5_redteam_audit.md`, read at its own closing
   sections with particular care (per this task's instruction).** Its §5
   "Reconciled Iteration-84 queue," **Tier 0, item 2**, reads in full:
   *"Ratify or reject proposed R24 (§2, above) — the mandatory-fix-
   consequence-implementation rule this audit recommends... non-firing per
   every prior R-rule's own founding-instance precedent."* This is the ONLY
   Tier-0/1/2/3 line item anywhere in that queue that mentions R24. It is
   about ratifying the RULE. Separately, in the earlier "Recommended, not
   applied by this audit" preamble (line 519–520, prose, not a numbered
   Tier item): *"require either a `run.py` change — Iteration 84's job,
   since this audit may not touch `run.py`..."* — this is the actual
   code-fix task, and it was **never itself promoted to a numbered line
   item in the Tier list**; items 3–8 that follow that preamble are a
   different, adjacent set (an `abs_ratio(312)` trust caveat, a
   `p3_trusted`-ceiling statement, the `closure` narration, the raw-array
   persistence retraction, a settling-pilot wall-time field, and the
   `delta_scene` retirement mandate) — none of the eight is "wire the
   reclassification trigger into `run.py`'s classification logic."
2. **exp-106's own `run.py`, read directly, line-by-line at the
   classification block (lines 754–765).** Confirmed: `classification` is
   set purely from `sr_fa` thresholds (`CONFIRMS`/`REFUTES`/`AMBIGUOUS`)
   plus noise/trust qualifiers. **No check of `p_abs_frac_diff`
   (12.31%/17.96%) against any `~10%` trigger exists anywhere in this
   function, or anywhere else in the file** (`grep -n "shape_ratio_
   fixedabs\|classification"` returns no such check). The mandatory-fix-1
   reclassification consequence is, independently confirmed, still not
   coded — exactly as exp-106's own audit found, unchanged.
3. **exp-107's own `phase1_proposal.md`, `NOTES.md`, and
   `phase2_redteam_audit.md`, read directly.** All three read the Tier-0
   R24 queue phrasing as pure rule-ratification bookkeeping: the proposal's
   own §6 states *"this cycle has no live ratify-or-reject action to
   take... a bookkeeping confirmation, not a re-opened question"*; `NOTES.
   md`'s own Synthesis repeats this near-verbatim; Red Team's own Phase-2
   audit (line 476–479) affirms it — *"nothing further is required of
   Phase 3 on this point."* **The actual `run.py` code-fix task is never
   mentioned anywhere in the Phase-1 proposal, Phase-2 critiques, Phase-2
   Red Team audit, or NOTES.md's Synthesis/Setup/Predictions/Result/Next
   sections.** `grep -n "R24\|code fix\|shape_ratio_fixedabs"` across all
   five Phase-2 critique files returns zero hits.

**Ruling: SILENTLY DROPPED — but with a root cause one cycle upstream of
this one, not solely an exp-107 failure.** The actual code-fix task was
disclosed only in a Phase-5-audit prose aside at exp-106's own close, never
converted into its own tracked Tier-0/1/2/3 line item — the "Reconciled
Iteration-N queue," this program's own primary cross-cycle-memory mechanism,
did not capture it. exp-107's Phase 1/Phase 2/NOTES.md layers then worked
faithfully from the queue as literally written, and — reasonably, given what
the queue actually said — treated the Tier-0 R24 line as fully discharged by
rule-ratification alone. That reading is technically defensible against the
queue's own text, but it is incomplete against exp-106's own fuller record,
and the two got conflated in every governing document of this cycle except
one: **THERMODYNAMICS' Phase-5 self-review** (`phase5_review_
thermodynamics.md` §6 item 3) independently traced the debt back to exp-106's
own Iteration-83 entry and named it explicitly: *"this cycle did not touch
`shape_ratio_fixedabs`'s classification logic at all (correctly out of
scope)... should not silently roll past a second deferral."* One of six
caught it; five of six (including both this cycle's own Phase-1 author and
its own Phase-2 Red Team audit) did not. **Net status as of this cycle's
close: the code fix is still not implemented, now carried, untracked as an
explicit queue item, across two full cycles (Iteration 83→84).** See §2/§3
for the rulings this triggers and §6 for where it lands in Iteration 85.

**Correction to the consolidated secondhand summary handed into this
audit**, per this task's own instruction to verify rather than trust it: the
summary characterized this as "silently dropped, conflated with the separate
R24-rule-ratification bookkeeping item — only partially caught by one of six
Phase-5 reviews." That is correct in substance and independently reconfirmed
here from primitives — but the summary omits the more consequential root
cause: the conflation was already baked into the Iteration-84 queue's own
text one cycle earlier, at exp-106's own Phase-5 close, not invented fresh
by exp-107. This distinction matters for §3's R24 ruling and for where the
remediation belongs (§6, Iteration-85 Tier 0).

**0.3 THERMODYNAMICS' `margin ~ r^-1.16` fit and the two projected
figures — CONFIRMED, and the "needs reconciling" framing in the consolidated
summary is itself mistaken.** Recomputed independently in Python from
`results.json::item3_rows`:

```
margin_selfsim:  156->343.40153175502877   312->171.87112284198233   ratio=1.998018  (log2=0.99857)
margin_fixedabs: 156->262.37425519280833   312->117.46331098784337   ratio=2.233670  (log2=1.15942)

projected margin_selfsim(624)  = 171.87112.../1.998018 = 86.02082...   ~86.0x
projected margin_fixedabs(624) = 117.46331.../2.233670 = 52.58759...   ~52.6x
```

Both reproduce THERMODYNAMICS' review figures exactly. **These are NOT "two
different projection methods for the fixed-abs family"** (the consolidated
summary's framing, which this audit does not adopt) — **they are the
identical method (each family's own empirically observed 156→312
margin-halving ratio, extrapolated one further octave to a hypothetical
r=624) applied to two DIFFERENT families**: 86.0× is self-similar's own
projection (clean `r^-1`, exact to 3 sig figs); 52.6× is fixed-abs's own
projection (`r^-1.16`, from the super-linear `σ_ext` growth THERMODYNAMICS
correctly attributes to the fixed-thickness-coating mechanism). There is
nothing to reconcile between them — they are two different cells' own
forward-looking numbers, not competing estimates of the same quantity.
**ADOPTED as stated by THERMODYNAMICS; the consolidated-summary framing that
called for reconciliation is REJECTED as a misreading, corrected here.**

**0.4 Checkpoint/resume A/B test (`checkpoint_validation.txt`) —
independently re-read, methodology and result confirmed sound.** r=156's
empty and article scenes were each re-run via `chunk_runner.py`'s 3-chunk
pickle/resume path and diffed field-by-field against the original
single-shot captures: `max|diff|=0.000e+00` on every field (`ez_a`, `hx_a`,
`hy_a`, `ez_b`, `hx_b`, `hy_b`, the extracted phasor, `sigma_e`). This is a
genuine cross-validation against an uninterrupted run (not a
self-consistency re-run of the chunked path against itself, which is what
`run.py`'s own module docstring language could be misread as) — confirmed
directly from the log's own method description. No defect found; the
mechanism is bit-exact on the one leg (r=156) it could be tested against
directly, and by the identical-architecture argument both EM and QUANTUM
independently verified from `lab/fdtd2d.py::Sim.run()`'s source, this
extends to r=312's own numbers with high confidence, though not literal
r=312-scale verification (see §1, EM/QUANTUM disposition).

**0.5 `box_dev`-margin-shrinkage claim (MATERIALS) — CONFIRMED.**
`box_dev(156)=0.0007082491592625747 / |Δ|=2.96857×10⁻⁵ = 23.86x`;
`box_dev(312)=0.0002219226856419363 / |Δ|=2.468×10⁻⁵ = 8.99x`. Matches
MATERIALS' "~23.8×"/"~9.0×" exactly, down from T9's founding-instance
`box_dev≈0.0019` vs. `Δ≈1.56×10⁻⁶` ≈ 1218× (MATERIALS' "~1221×," within
this audit's own precision of hand-derived T9 figures — not independently
re-verified past MATERIALS' own citation, since it rests on an
80-cycle-old, already-multiply-confirmed anchor outside this cycle's own
new data).

**0.6 Independent grep confirmation for the R23 finding (VISION):**
`grep -in "disclaimer" run.py chunk_runner.py finalize.py` → **zero hits, in
all three files.** VISION's finding is exact, not merely trusted. See §3.

**0.7 New-machinery suite-gating check (EM/QUANTUM's shared finding),
independently confirmed:** `grep -rln "pickle|checkpoint|resume"
lab/ lab/validation/` → **zero matches.** `chunk_runner.py`'s mid-run
`Sim`-object pickling is confirmed genuinely new, unguarded by any of the 25
existing trust-suite stages, matching both seats' finding exactly.

---

## 1. Adjudication of the six Phase-5 reviews

**PHOTONICS — ADOPT in full.** The R9-class T9-anchor-blending finding
(§0.1) is exact and correctly scoped (non-load-bearing to `item1_pass`).
The second finding (`core_frac≈10⁻⁷` cannot see a phase-mediated
interference contribution to `sigma_ext`, only local Joule dissipation) is
sound reasoning, independently confirmed against `sections.py`'s own
construction (`radial_absorbed_power` integrates dissipation, `widths()`
derives `sigma_ext` from the optical theorem — genuinely different physical
quantities) — **ADOPTED**, and elevated together with MATERIALS' identical
(c) finding into this audit's own Iteration-85 Tier 1 (§6).

**MATERIALS — ADOPT in full, with one clarification.** The Hypothesis-
section scope-creep finding (NOTES.md's own Hypothesis section attributes a
constraint-1/2/3/4-immunity claim to `disposition_memo.md`, which never
discusses constraints at all — that authority is VISION's, not MATERIALS',
and rests on a citation MATERIALS itself did not make) is confirmed by
direct re-read of `disposition_memo.md`: its entire text is the three-branch
realizability argument; it does not mention constraints 1–4 anywhere.
**ADOPTED.** The `box_dev`-margin-shrinkage finding (§0.5) and the
`angular_scattered_pattern`-is-the-right-unused-instrument finding are both
**ADOPTED** — the latter is independently confirmed sound: `radial_
absorbed_power`/`widths()` are bulk, angle-integrated instruments that
cannot in principle detect a standing-wave/interference signature localized
in the angular distribution of scattered power, and this program has
already built and validated the correctly-targeted tool (`angular_
scattered_pattern`, exp-059/060) for exactly this question. The "delta
doesn't monotonically grow with ratio" finding is also confirmed directly
from the two filed deltas (2.969×10⁻⁵ at ratio 0.692 > 2.468×10⁻⁵ at ratio
0.846 — smaller magnitude at the higher ratio) — **ADOPTED**.

**ELECTROMAGNETISM — ADOPT the diagnostic findings; no remedy to override
(both already closed same-shift).** The `closure`-field silent-drop finding
(§0.7-adjacent: EM independently recomputed `closure=0.0196%`/`0.0563%`
from raw pickles and confirmed it would have passed cleanly had it been
run) is **ADOPTED** as a genuine, non-load-bearing discipline gap — I name
it explicitly, per EM's own framing, as an "R16-family shape" (an
established-elsewhere check quietly not carried into a new call site of the
same instrument) rather than a literal R16 recurrence (a different specific
field/channel than R16's own NETD-byproduct text covers) — see §6 for how
this folds into this audit's own new-rule proposal. The checkpoint/resume
verification gap EM named was **independently closed same-shift** (NOTES.
md's own post-Phase-5 addendum, §0.4 above) — EM's own prescribed remedy
was executed, not merely accepted in principle. The two-route
extinction-identity cross-check EM ran for free (`rel dev` 5.85×10⁻⁶/
1.21×10⁻⁵) is **ADOPTED** as a genuine, freely-available corroboration this
cycle's own record should have surfaced and didn't.

**THERMODYNAMICS — ADOPT in full; margin-erosion projection is the single
best unforced finding of this cycle.** The bit-exact fragile-cell
re-derivation (§0.3/§0 above) and the `r^-1`/`r^-1.16` mechanistic
explanation (conduction-dominated `dp_dt∝r`, self-similar's `sigma_ext∝r`
vs. fixed-abs's super-linear `sigma_ext∝r^1.08`, both independently
re-derived here) are **ADOPTED, exactly** — this is real, falsifiable,
thermodynamically-grounded work this cycle's own record should have done
and didn't. The R24-carryover flag (§6 item 3 of the review) is **ADOPTED**
and is the seed of §0.2/§2/§3's own ruling below, correctly scoped by
THERMODYNAMICS itself as "correctly out of scope" for this cycle's own
assigned items while still being a live, unresolved debt.

**QUANTUM OPTICS — ADOPT in full.** The anchor-impossibility re-derivation
(a third independent confirmation, digit-for-digit) needed no correction.
The statistical-rigor findings on Item 4 — non-independent, spatially
correlated pixels inflating a naive significance read; a two-point "worsens
with r" claim resting on exactly the sample size R15's own addendum already
named insufficient to call a trend established; `FLOOR_FRAC=0.10` reused a
second time this document without independent re-derivation, the same shape
this cycle's own Red Team audit caught once already (Attack 5, the G0
amplitude-ratio band) — are **ADOPTED in full**, independently checked
against the underlying `frac_unresolved` figures and R15's own text, both
of which support QUANTUM's reading exactly. The checkpoint/resume R8-shaped
gap this seat also flagged is the same one EM named, independently arrived
at — **ADOPTED**, closed same-shift.

**VISION SCIENCE — ADOPT in full; this is the most consequential
self-review this program has produced in the T28 sub-thread.** Both
self-owned Phase-1 defects (the empty-domain G0 anchor rule; the
`C_thr_lab` R9-shaped miscitation, 5.25×–7.87× discrepancy) are confirmed
exactly against `phase2_redteam_audit.md` §0.1/§0.4 — no correction needed,
this seat's own arithmetic is exact. The R23 code-absence finding (§0.6
above) is **ADOPTED** and is this cycle's single most important
newly-surfaced governance data point (§3, below) — VISION correctly
declined to rule on its own firing status ("a governance call for Red Team/
the Director, not mine to rule on unilaterally"), which this audit now
does. The item-4 perceptual-scope-boundary finding ("solver-numerics, not
perceptual... the two floors share nothing but the English word") is
**ADOPTED** as the correct, disciplined application of PANEL.md's
"speaks only from its own discipline" rule.

**No disagreement among the six on any load-bearing point.** All six
independently reproduce Gate P0, Item 3's margins, Item 1's deltas, and
Item 4's `frac_unresolved` figures exactly. The six reviews' secondary
findings are complementary, not competing (PHOTONICS'/MATERIALS' shared
`abs_ext_ratio`-falls-with-ratio physical signature; EM's/QUANTUM's shared
checkpoint/resume gap, independently arrived at and independently closed).

---

## 2. New defect none of the six (fully) caught, and its root cause

**The queue-item-completeness gap, one cycle upstream of this one.**
Five of six Phase-5 reviews (all but THERMODYNAMICS) treated this cycle's
own R24 governance note as settled without checking it against exp-106's
own full audit text — a reasonable reading of what the Tier-0 queue line
literally said, but incomplete against what exp-106's own document
actually, separately, disclosed. THERMODYNAMICS caught that the code fix
remains outstanding but did not diagnose *why* it fell through — that the
gap originates in exp-106's own Phase-5 audit not promoting a
prose-disclosed "requires a `run.py` change" remedy into its own numbered
Tier list, the one place this program's cross-cycle memory is designed to
be authoritative. This is the genuinely new finding: **a real, correctly-
identified-as-necessary code fix, disclosed by name in an audit's own
prose, is functionally indistinguishable from "not needed" to the next
cycle unless it is captured as its own explicit line item in that audit's
own Reconciled Iteration-N+1 queue** — the queue's own structure, not its
authors' diligence, is the single point of failure this cycle exposes. No
review named this specific mechanism; each treated the surface symptom
(exp-107 didn't fix it) rather than the structural cause (exp-106's own
record never actually asked it to, in the one place that counts).

**Proposed new standing rule — R25 (queue-item completeness).** *A
code-level fix an audit determines is necessary, but defers because "this
audit may not touch [file]" or an equivalent scope limit, must be added as
its own explicit, numbered line item in that audit's own Reconciled
Iteration-N+1 queue — never left only as a parenthetical aside inside a
different numbered item's prose or a Tier-0 governance line about a
different, textually-adjacent action (here: rule-ratification vs. a
concrete code change). A future cycle's own Phase 1–3 layers are entitled
to work from the queue as literally written; the fault for a dropped item
under this rule lies with the queue's own authorship, not with the cycle
that inherits an incomplete queue in good faith.* **Does not fire on its
own founding instance** (exp-106/exp-107), matching every prior R-rule's
own founding-instance precedent — this is the first time this exact
shape has been named. **Forward clause, matching R16/R21/R23/R24's own
single-instance-ratified, two/three-strike model**: a second instance of a
prose-disclosed, audit-identified code fix failing to appear as its own
Reconciled-queue line item, on any channel, fires Checkpoint criterion 4
automatically.

---

## 3. Rulings on the four named items

**R9 (PHOTONICS' anchor-blending citation finding).** **ADOPTED, exactly
as filed** — 19.0×/15.8× (r=156/312) against the like-for-like exp-027
anchor, not the "~10×" blended figure. Non-load-bearing to `item1_pass`.
Annotated directly into NOTES.md (§7).

**R20 (tally of R4-class defects surviving this cycle's own freeze).**
Computed explicitly, the same methodology exp-106's own audit used:

| Candidate | R4/R9-shaped (fails to reproduce/commensurate with its own cited source)? | Survives Phase-3 freeze into Result/Learned? | Counts toward R20? |
|---|---|---|---|
| Item 1's "roughly an order of magnitude above T9 anchors" (PHOTONICS, §0.1) | Yes — R9-class commensurability defect | Yes — Result section, verbatim | **Yes — 1** |
| Hypothesis section's constraint-1/2/3/4-immunity attribution to `disposition_memo.md` (MATERIALS) | Debatable — an overclaim of scope, not a figure/citation failing to reproduce numerically | Hypothesis section, not Result/Learned | No (wrong section, per R20's own strict text) |
| `closure` field never computed (EM) | No — a silently-dropped check, R16-family-shaped, not a citation mismatch | Absent by omission | No (wrong class) |
| R23 code-absence (VISION) | No — a code-presence gap, not a citation/figure mismatch | Idealizations section, not Result/Learned | No (wrong class) |
| R24 code-fix carryover (THERMODYNAMICS/§0.2) | No — a specification-vs-implementation gap on an INHERITED item, not a citation this document itself makes | N/A — the debt lives in exp-106's own file, not this one's Result | No (wrong class, wrong document) |
| Item 4 "worsens with r" (QUANTUM) | No — a statistical-rigor/sample-size overstatement, not a reproduction failure | Result section | No (wrong class) |

**Tally: 1, at most.** Falls far short of R20's "three or more" bar.
**R20 does NOT fire this cycle.**

**R21 (THERMODYNAMICS says it's discharged — do you agree?). AGREE,
independently confirmed.** Item 3's Result section states all four cells'
`dt_ss_K`/margin/classification inline, in prose, exactly matching R21's
own text ("stated inline in a cycle's own Result section, not merely
persisted to `results.json`"). Direct re-read of NOTES.md's Result section
confirms the full table is present verbatim, not merely referenced. R21 is
genuinely discharged this cycle, on this channel's third relevant
occasion (exp-099, exp-100 non-firing founding instances; this cycle is a
clean pass, not a third occurrence of the gap).

**R23 (VISION's disclaimer-erosion finding — live violation or
documentation-only?). Neither, precisely — a live compliance gap that is
non-load-bearing and does not, on this cycle's own facts, constitute a
firing-grade recurrence of R23's own text.** Three findings, held apart
deliberately:

1. **The code enforcement is genuinely, verifiably absent** (§0.6) — not
   a documentation slip or a stale comment; `run.py`/`chunk_runner.py`/
   `finalize.py` contain no `DISCLAIMER` constant, no generated
   Predictions/Result text, no assert, anywhere. This is a real, live gap
   in this cycle's own code, not merely an inaccurate description of it.
2. **R23's own operative text mandates code enforcement for "a disclaimer
   required in multiple document sections"** generated via the
   `PREDICTIONS_TEXT`/`RESULT_TEXT` pipeline exp-104–106 built. This
   cycle's document architecture (Tier 0 explicitly "text-only, zero
   code"; Tier 1's three items scored via hand-written NOTES.md tables,
   never invoking that pipeline) never engaged the machinery R23's rule
   text presupposes — so this is not a case of the mechanism being
   present-but-broken (R23's own Iteration-82 founding scope-gap shape);
   it is a case of the mechanism's entire precondition (a code-generated
   Predictions/Result text) not existing this cycle at all. Whether R23's
   own text should be read as requiring SOME minimal code enforcement even
   absent that pipeline is exactly the open Iteration-82 scope question
   (§0.2/genericize-vs-ratify-single-scope) — unresolved for a third
   consecutive cycle (82→83→84).
3. **Non-load-bearing, independently confirmed**: constraint-3 is
   correctly, explicitly N/A throughout this cycle (Red Team's own Phase-2
   audit, "no constraint-#N-violation found"; VISION's own Phase-5
   self-confirmation) — nothing was scored against a missing, wrong, or
   silently-eroded perceptual threshold. The gap is real but inert this
   cycle.

**Ruling: this is a live, verified compliance gap in the codebase (not
"documentation-only" in the sense of a mere prose inaccuracy) but it is
also not a "violation" in the rule-firing sense — R23's own text does not
yet clearly extend to a document family that never invokes the
code-generation pipeline it was built around, and the specific harm the
rule exists to prevent did not occur.** NOTES.md's own Idealizations claim
("R23 code-enforced... applies unchanged") IS false as stated for this
cycle's own code and is annotated accordingly (§7). Does not fire
Checkpoint criterion 4 — R23 carries no forward-elevating clause on file
(unlike R16/R21/R24), and this is the founding instance of the specific
"document family with no code-generation pipeline" scope question, not a
repeat of an already-named failure. **The standing Iteration-82 R23-scope
decision must be forced at Iteration 85** — three consecutive cycles of
silent non-resolution on an already-named governance item is its own
warning sign, distinct from and in addition to R25's own founding instance
above.

**R24 (the exp-106-code-fix carryover question).** Ruled in full at §0.2.
**SILENTLY DROPPED**, root cause traced to exp-106's own queue authorship
(§2), not solely an exp-107 failure. **Does NOT fire R24's own two-strike
forward clause** — that clause requires a future cycle to SHIP a NEW
Phase-3 "adopted in full" claim whose own consequence later proves uncoded;
exp-107 shipped no such new claim, it inherited an already-existing,
already-named debt and (through the queue's own incompleteness, not malice
or negligence) failed to execute or explicitly re-defer it. This is
R25's founding instance, not R24's second one. **The code fix itself
remains unimplemented** and is placed, explicitly, as Iteration-85's own
Tier 0 item 1 (§6).

---

## 4. Ruling on Checkpoint criterion 4

**Does NOT fire**, reasoned against each of PANEL.md's five criteria and
against every R-rule's own forward-elevating clause that could plausibly
apply:

- **Criterion 1/2/3** (constraint-metric pass; proven boundary; engine
  physics beyond validated bench classes): not applicable — this is a
  governance/instrumentation cycle, T1 correctly N/A throughout, no
  mechanism proposed or varied, no constraint scored.
- **Criterion 5** (two consecutive iterations with no logbook-advancing
  result): not applicable — exp-106 and exp-107 each produced genuine,
  disclosed, logbook-advancing findings (exp-106: the floor-gate
  falsification, the fixed-abs control's first execution; exp-107: the
  `delta_scene` retirement, Item 4's noise-floor discovery, the
  checkpoint/resume validation).
- **Criterion 4** (program-integrity drift — unfalsifiable claims, a
  constraint quietly dropped, especially #3): the specific sub-questions
  checked — **R20 tally is 1, short of "three or more"** (§3); **R24's own
  two-strike clause does not apply** (wrong failure shape, §3); **R16's
  three-strike clause does not literally extend to the `closure`-field
  drop** (a different specific field/channel than R16's own NETD-byproduct
  text names — EM's own "R16-family shape" language is an analogy, not a
  claimed recurrence); **R23 carries no forward-elevating clause on file**
  and this cycle's gap is the founding instance of a genuinely new scope
  question, not a repeat (§3); **constraint-3 was not quietly dropped** —
  it was explicitly, correctly, and repeatedly marked N/A by every layer
  of this cycle's own review (Phase-2 Red Team audit, all six Phase-5
  reviews), the opposite of a quiet drop.

**This is, however, the closest non-firing call in the R16/R21/R23/R24
"silent-drop" lineage's own history for THIS specific shape** (a named,
dated, "next iteration's job" carryover task vanishing between cycles) —
matching that lineage's own consistent founding-instance-does-not-fire
precedent, but only because R25 (§2) is being named and ratified for the
first time in this very document. **A second instance of R25's own pattern
fires Checkpoint criterion 4 automatically**, with no further
deliberation, matching every prior founding rule's own forward-elevating
convention.

---

## 5. Combined Verdict: PARTIAL

**Not RULED OUT** — T1 correctly, repeatedly N/A throughout (confirmed
independently at §0.7 and by two blind Phase-5 seats' own direct source
reads); no mechanism class is foreclosed or engaged this cycle.

**Not PROMISING** — no mechanism proposed, varied, or advanced; this is a
pure governance-and-instrumentation cycle by design (§0 of the Phase-1
proposal states this explicitly), and it delivers no phenomenon-
reproduction progress by its own scope.

**Real, disclosed progress, on both structurally independent halves:**

- **Tier 0.** The `delta_scene` R3-vs-R4-vs-R5 resolution-family-
  attribution question — deferred eight consecutive cycles (Iterations
  77–84) — is **formally, soundly retired**, discharging a genuinely
  overdue standing obligation by written argument rather than a costly,
  structurally-doomed census (the proposed census's own mandatory gate
  had an empty domain over any reasonably-sized window of this periodic
  signal — confirmed independently three separate times, §0 of Phase 2's
  own audit and again here). This matches this program's own Iteration-51
  precedent exactly and is, on the numbers, the correct call — no seat,
  including this audit, would make a different one with the same
  information.
- **Tier 1.** All three `kappa_window` closeouts executed honestly and
  without smoothing: Item 3 delivers this channel's first real,
  ledger-measured (not placeholder) thermal row and correctly narrates its
  own fragile cell (R21 genuinely discharged, §3); Item 1 passes only the
  loose T9-anchor band, disclosed as an honest partial, not rounded up;
  Item 4 falsified its own r=156 prediction and surfaced a genuinely new,
  previously-unanticipated finding (18–27% article-scene noise-floor
  contamination, worsening with r) that neither the Phase-1 proposal nor
  any Phase-2 critique predicted. The checkpoint/resume mechanism this
  cycle introduced as an environment workaround is now empirically
  validated bit-exact (§0.4), closing a real new-machinery trust gap the
  same shift it was raised.

**The genuine cost of this cycle, weighed honestly against the above:** a
real, previously-named, "Iteration 84's job" code-level fix (exp-106's own
`shape_ratio_fixedabs` reclassification trigger) survived this entire
cycle untouched, uncaught by five of six review layers, and never appeared
in this cycle's own forward-looking queue at all — not because anyone
ignored it, but because this program's own cross-cycle memory mechanism (a
prior audit's own Reconciled-queue text) failed to carry it forward in
trackable form. That is a real governance-process finding, not a
scored-verdict one, and it is the reason this audit proposes R25 and
places the fix, explicitly, at the top of Iteration 85.

---

## 6. Reconciled Iteration-85 queue

**Tier 0 — governance, zero-FDTD, binding on the next cycle.**

1. **Execute exp-106's own mandatory-fix-1 reclassification consequence**:
   wire the `p_abs_frac_diff > ~10%` divergence check directly into
   `run.py`'s `shape_ratio_fixedabs` classification logic (a small,
   deterministic code change — the trigger condition and the correct
   label, THREE-WAY AMBIGUOUS, are already known and computed; zero new
   FDTD). This is a two-cycle-old, still-unexecuted debt (§0.2/§3) — do
   not let it reach a third cycle unexecuted; that would fire Checkpoint
   criterion 4 automatically under R25 (§2/§4).
2. **Ratify or reject proposed R25** (§2, above) — the queue-item-
   completeness rule this audit recommends, founded on this cycle's own
   instance, non-firing per every prior R-rule's own founding-instance
   precedent.
3. **Force the standing R23 scope decision** (genericize the `DISCLAIMER`
   assert to a table-driven check covering every document family, or
   formally ratify R23 as intentionally scoped only to the code-generated-
   Predictions/Result-text pipeline) — now three consecutive cycles
   (82→83→84) without resolution. Separately decide whether a text-only/
   governance-cycle document that makes a perceptual/expressibility scope
   claim in prose (as this cycle's own Idealizations section did) needs
   *some* minimal code-level assert even absent a full Predictions/Result-
   text pipeline.

**Tier 1 — real cross-seat convergence (3+ of 6 seats independently name
these).**

1. **Run `lab/sections.py::angular_scattered_pattern` on the hollow-vs-
   PEC-cored fixed-abs pair at r=156/312** (MATERIALS' top ask, echoed by
   PHOTONICS) — the correctly-targeted instrument for a near-field/
   interference signature `radial_absorbed_power`/`widths()` cannot see by
   construction; reuses exp-059/060's own precedent.
2. **A genuine absolute (not box-to-box) noise-floor characterization for
   the `sections.widths()` box-ledger channel** — T9's own Iteration-4
   caveat, over 80 cycles old, now exposed at 9.0x margin at r=312 (down
   from 1221x at founding, §0.5) — before any future cycle treats a small
   cross-family `abs_ext_ratio` delta as decisively small again.
3. **Check Item 4's numerator noise-floor finding on the actual PEC-cored
   PRIMARY article** (both families, r=156/312), not the hollow
   substitute this cycle used — near-unanimous ask (PHOTONICS named it at
   exp-106; QUANTUM, VISION, and EM each name it again here) — to resolve
   whether `kappa_window`'s own "accelerating collapse" headline
   (exp-102/105/106) partly reflects solver noise floor rather than
   physics.
4. **Promote `chunk_runner.py`'s checkpoint/resume mechanism to a named,
   suite-gated trust-suite stage** (one absolute identity gate: chunked-
   vs-continuous agreement on a cheap reference case) — this cycle's own
   same-shift A/B test already proved it bit-exact at r=156 (§0.4);
   formalize it so future cycles inherit verified, not re-argued, trust
   (EM/QUANTUM, matching R18's own precedent).

**Tier 2.**

1. Re-derive Item 1's `≤2×10⁻⁵` "confirms" band specifically for these
   higher `R_CORE/R_COAT` ratios (0.692/0.846), per R17's own discipline,
   rather than reusing T9's original two-anchor spread unjustified.
2. Restore Item 3's `Q_ext`-invariance corroboration and the ledger
   `closure` identity (0.02–0.06%, §1) into Result prose — cheap, closes
   the "computed-not-narrated" pattern a second time on a different field
   (EM).
3. Re-frame Item 4's "worsens with r" claim per QUANTUM's own R15
   two-point caution and correlated-pixel-count concern, or gather a
   third r-point on this specific numerator channel before calling it a
   trend.
4. Decide whether the constraint-3 immunity claim (currently resting on
   VISION's sub-threshold reading, now 63% of `C_thr_lab`, not the
   mistakenly-cited 8–12%) needs its own explicit reopening condition,
   separate from MATERIALS' realizability-only one (MATERIALS' own
   sharpest attack, §1).

**Tier 3 — standing, unchanged this cycle.**

1. The oblique-angle extension of the θ=0°-validated `kappa_window`
   bridge.
2. The near-null-exclusion raw-bin-identity refinement (Iteration-82's own
   item, now three cycles deferred).
3. Standing T28 items untouched by this cycle: a fourth `kappa_window`
   r-point; a genuinely different bridge-family geometry; the 750/450nm
   leg; the `G40` full-width leg; the x-wall admittance refit; `PAD`-with-
   article survival at other wavelengths.

---

## 7. Same-shift fixes applied directly to NOTES.md (annotated, not
   silently rewritten — R4 convention)

1. **Item 1's Result-section T9-anchor comparison** — annotated with the
   corrected, like-for-like-only figures (19.0×/15.8×, not "roughly an
   order of magnitude") and the R9-class explanation (§0.1/§3).
2. **The R24 governance-bookkeeping paragraph** — annotated with the full
   two-item carryover history (rule-ratification vs. the still-outstanding
   `run.py` code fix), its root cause, and where the fix now lives in the
   Iteration-85 queue (§0.2/§2/§3/§6).
3. **The Idealizations section's `DISCLAIMER`/"R23 code-enforced" claim**
   — annotated as false for this cycle's own code, with the confirming
   grep result, the non-load-bearing scoping, and the standing R23-scope
   decision now three cycles unresolved (§3/§6).

No scored number, verdict, or classification string was altered by any of
the three annotations — all are narrative corrections to prose, matching
this sub-thread's own established R4 convention.
