# PHASE 2 — RED TEAM AUDIT · Panel Iteration 86 (candidate exp-109)
## "The R24 Second-Instance Smooth Gate and R23's Missing `RESULT_TEXT` Half — Closing the Right Queue Item, Correctly, With Six Real Text/Code Gaps Left Open"

Red Team seat, fresh context. Received: PANEL.md, LOGBOOK.md in full (RULED
OUT registry R1–R25 read in full), PLAN.md's Current-state section, the
Phase-1 proposal, and all five blind Phase-2 critiques (PHOTONICS,
ELECTROMAGNETISM, THERMODYNAMICS, QUANTUM OPTICS, VISION SCIENCE — MATERIALS
is this cycle's lead and does not critique its own proposal). Every
load-bearing figure below was independently re-derived from primitives —
`experiments/108-.../run.py`, `.../analyze.py`, `.../results.json`,
`.../reclassify_106.py`, `.../phase2_redteam_audit.md`,
`.../phase5_review_vision.md`, `experiments/104-.../run.py` — not trusted
from any seat's restatement, including this document's own quotations.

---

## 0. Independent re-verification from primitives

**0.1 The OLS inequality (all five critiques touch this; independently
re-derived from scratch, not from any critique's arithmetic).**
`linear_fit_1_over_margin`'s design matrix is `A_mat = [1, 1/margin]` — an
intercept column plus one regressor. For any OLS fit that includes an
intercept, the constant model `ŷ = mean(y)` is a feasible point in the same
least-squares search space (set `B=0`), so the fitted model's own residual
sum of squares can never exceed `Σ(y−ȳ)²` — i.e. `residual_std ≤ raw_std`
always, with equality only when the fit places zero weight on `1/margin`.
This is a general fact about OLS-with-intercept, true independent of
whether the fit happens to look "smooth" by this codebase's own
`is_monotonic or r_squared≥0.90` test. Confirmed exact, both r, against
`experiments/108-.../results.json`'s own committed `tier1.r{r}.item_ii`
block:

| r | `delta_values` (6, from `results.json`) | `np.std(delta_values)` (raw) | `fit.residual_std` | `fit.r_squared` | `fit.is_monotonic` | `fit.smooth` |
|---|---|---|---|---|---|---|
| 156 | `[-3.2254e-5,-2.9686e-5,-2.1943e-5,-1.8651e-5,-1.9736e-5,-2.4697e-5]` | **5.008327900579266e-06** | 2.89716280726349e-06 | 0.6653735294260243 | `False` | **`False`** |
| 312 | `[-2.8692e-5,-2.4684e-5,-2.9952e-5,-2.6736e-5,-2.4369e-5,-2.8845e-5]` | **2.1240857290489e-06** | 2.102199273342035e-06 | 0.020501712361515212 | `False` | **`False`** |

Both `raw_std`/`residual_std` values reproduce the Phase-1 proposal's own
§4 table to <1e-9 relative (`5.008328e-6`/`2.124086e-6` as stated). Both
`fit["smooth"]` are `False` — the proposal's own claim that both r take
the new raw-fallback branch is confirmed exact, from the actual committed
arrays, not merely the proposal's restatement of them. `raw/residual`
ratios: **1.72870× (r=156)**, **1.01041× (r=312)** — QUANTUM's 1.73×/1.01×
confirmed to 3 significant figures. Both raw-std values clear the CONFIRM
bar (`0.5·|Δ_boxA|` = 1.4845e-5/1.234e-5): `5.008e-6 ≤ 1.4845e-5` and
`2.124e-6 ≤ 1.234e-5`, both `True` — the predicted `CONFIRM`/`CONFIRM`
outcome at both r is independently confirmed, not merely arithmetically
plausible.

**0.2 `classify_item_i()`'s own CONFIRM branch — re-traced line-by-line
against `experiments/108-.../run.py:196–250`.** `confirm_all_margins` is
computed by a loop over all 6 margins comparing `relm` against
`ITEM_I_CONFIRM_REL`, entirely independent of any `fit` object. `runs` is
built by a separate contiguous-run scan over `rel32 >= ITEM_I_REFUTE_REL`.
`linear_fit_1_over_margin` is called **exactly once**, inside
`for (i0, j0) in runs:` (line 236–239) — this loop body is unreached when
`runs` is empty. The verdict assignment is:
```
if confirm_all_margins and not runs:
    verdict = "CONFIRM"
elif runs and smooth_run_found:
    verdict = "REFUTE"
else:
    verdict = "AMBIGUOUS"
```
CONFIRM requires `not runs` — i.e. CONFIRM is only reachable in exactly the
case where the fit-and-smoothness code path is never entered at all. This
independently confirms PHOTONICS' finding (§1, below).

**0.3 The original Iteration-85 mandatory fix's own text, re-read
directly** (`experiments/108-.../phase2_redteam_audit.md:340–347`, EM+
QUANTUM's unified item-ii remedy, quoted verbatim by that document): *"before
reporting raw `std` across the 6 margins as a placement-noise proxy, report
whether the sequence is monotonic (or fits a smooth `1/margin`-type trend)
in margin, at both r. If it is, report the residual-from-fit `std`
(QUANTUM's own ask) as the genuine floor."* This sentence's own grammar
already presupposes raw `std` as the thing that would otherwise be
reported, with the residual-from-fit `std` as the smoothness-gated
override — i.e. the ORIGINAL Phase-2 fix's own text, not merely the OLS
inequality or an analogy to a sibling classifier, already specifies raw
`std` as the non-smooth-case default. This is a stronger, more directly
on-point textual ground for choosing alternative (a) than either ground the
Phase-1 proposal actually cites (§4's own bullet (a)) — see §1 Attack 1,
below, and §3.

**0.4 `n_fdtd_calls`/`total_wall_s` provenance — independently opened
`results.json`.** Both are genuine top-level keys: `n_fdtd_calls: 6`,
`total_wall_s: 7712.0`. `tier1.r156.gate_p0.pass_` = `True`,
`tier1.r156.reproduction_precondition.pass_` = `True`,
`tier1.r312.gate_p0.pass_` = `True`,
`tier1.r312.reproduction_precondition.pass_` = `True` — four independent
booleans, all `True`. THERMODYNAMICS' §0-level provenance claims and its
undisclosed-AND-combination claim are both confirmed (§1 Attacks 3–4,
below).

**0.5 R23's "human-readable-citation" half — independently re-opened
`experiments/108-.../phase5_review_vision.md`.** §2d, verbatim: *"The
`DISCLAIMER` text itself never appears verbatim anywhere in the Result
section prose — only a *description* of..."* — exact match to VISION's
citation this cycle. The Phase-1 proposal's own binding
Execution-requirement row (§4 table, last row) reads, verbatim: *"Phase 4's
Result section quotes, inline, the actual printed OLD-vs-NEW `item_ii`
comparison and the pass/fail of both live asserts"* — no clause requiring
`result_text`/`predictions_text`/the `DISCLAIMER` span to be quoted
verbatim in NOTES.md's own Result section. VISION's finding is confirmed
exact (§1 Attack 5, below).

**0.6 Constraint/T1 structural check.** Every function this proposal
touches or adds (`classify_item_ii()`'s new body, the `--predictions-only`
block, `reclassify_108.py`) is a classification-statistic gate or a
text/persistence pipeline over already-committed scalars — none reads or
writes an optical, absorption, or perceptual parameter. T1 escape route
`N/A` is confirmed structurally correct; no constraint-1/2/3/4 verdict is
scored or moved anywhere in the diff.

---

## 1. Numbered attacks

**Attack 1 — [inconsistency] The alternative-(b) rejection's own
"sibling-precedent" analogy misdescribes `classify_item_i()`'s actual code,
independently confirmed at §0.2.** §4's rejection of forcing AMBIGUOUS on
a non-smooth fit argues `classify_item_i()`'s own CONFIRM (null) branch is
"unconditional on smoothness... exactly because a null finding needs no
trend-removal story to be believed" — framing it as a considered design
choice to treat null claims differently from positive ones. Traced to
source: CONFIRM fires only when `not runs` is true, which means the
`for (i0,j0) in runs:` loop containing the fit-and-smoothness test never
executes for a CONFIRM verdict — there is no smoothness judgment on the
table to be indifferent to. The branch is structurally incapable of facing
a smoothness question, not deliberately exempt from one. This is the
proposal's own load-bearing analogy, in the proposal's own document,
misdescribing sibling code it directly quotes — the exact shape this
program's R4/R9 lineage (a cited figure or claim must reproduce from its
own source before it is relied upon) already exists to catch, one level
removed from a numeric figure to a code-behavior claim. **Not
outcome-determining**: §0.3 independently supplies a strictly stronger
textual ground for choosing (a) over (b) that the proposal never cites (the
original mandatory fix's own words already specify raw `std` as the
non-smooth default) — so alternative (a) survives on grounds the proposal
did not use, even with this one removed. **Fix**: rest the (b)-rejection on
(i) the OLS-inequality proof (§4 bullet (a), independently re-verified
airtight at §0.1) and (ii) the original fix's own text (§0.3), not the
item-i analogy; either correct or delete the item-i sentence.

**Attack 2 — [inconsistency] §4's "more conservative... in every case"
claim is false as a general statement, independently re-derived at
§0.1.** REFUTE fires when `stat ≥ boxA`. Since `raw_std ≥ residual_std`
always (§0.1), substituting the inflated raw statistic makes the REFUTE
inequality strictly *easier* to satisfy, not harder — the fallback is
conservative against manufacturing a false CONFIRM (the narrower, true
claim the proposal also makes) but simultaneously liberal/anti-conservative
against manufacturing a false REFUTE. **Not outcome-reversing at either
tested r** (both raw values land deep inside the CONFIRM band, nowhere
near `boxA`) but the blanket "in every case" framing is wrong and will
matter the first time this gate scores a point sitting nearer the REFUTE
boundary — exp-108's own Reconciled Iteration-86 queue (Tier 2 item 1)
already names a queued r=624 point for exactly this channel. **Fix**:
replace with an accurate two-sided statement in §4 prose and in the
generated `stat_source` string itself (not merely the surrounding NOTES.md
prose, since `stat_source` is the artifact a future citation will actually
quote — R21's own standard, applied here to a string rather than a
persisted field).

**Attack 3 — [inconsistency] `gate_p0_pass`/`repro_pass`'s own
combination rule across r=156/312 is never stated, independently confirmed
underspecified at §0.4.** The proposal's `reclassify_108.py` flow (item 6)
says these two booleans are "read directly from exp-108's own committed
`results.json`, not hand-typed" but never states HOW two per-r booleans
(`tier1.r156.gate_p0.pass_`, `tier1.r312.gate_p0.pass_`, and likewise for
`reproduction_precondition`) collapse into the single `gate_p0_pass`/
`repro_pass` arguments `build_result_text()` actually takes. Unlike
`classify_item_ii()`'s exact new body (given verbatim), this reduction rule
is left to Phase-4 implementer judgment. **Not outcome-reversing this
cycle** — all four source booleans are independently confirmed `True`
(§0.4), so any sane reduction (AND, OR, "both individually reported") gives
the same headline PASS — but an undisclosed combination rule is exactly
the shape of gap this program's own governance-cycle precedent (R4's
"precisely recomputed" standard, extended to combination logic, not just
arithmetic) exists to close before it is load-bearing at some future r
where the two r's disagree. **Fix**: state explicitly, in
`reclassify_108.py`'s own code and docstring, that both are the logical AND
of the two per-r `pass_` fields.

**Attack 4 — [inconsistency] `build_result_text()`'s own assembled prose
will read exp-108's historical wall-time spend with no attribution note,
in a document whose own zero-new-FDTD fact lives only in §0/§5, not in the
Result prose itself — independently confirmed at §0.4.** `build_result_text()`
(unmodified by this proposal) renders literally:
`"{n_fdtd_calls} real FDTD calls, {total_wall_s:.1f}s ({total_wall_s/60.0:.2f} min)
total wall time, zero \`lab/\` diff..."`. Called this cycle with
`n_fdtd_calls=6, total_wall_s=7712.0` — genuine, verified exp-108 figures
(§0.4) — this produces "6 real FDTD calls, 7712.0s (128.53 min) total wall
time" inside exp-109's own `result_text`, with nothing in that string
itself flagging that all 6 calls and all 7712.0s belong to exp-108, not
this cycle (which makes zero new `Sim.run()` calls, confirmed structurally
at §0.6). A future citation that quotes `result_text` verbatim — which
Attack 5/mandatory fix 6, below, will make the REQUIRED way to cite this
document — would read exp-109 itself as having spent that wall time. This
is the mirror image of R21 (a persisted field's own finding must reach
Result prose, not stay in Setup/Idealizations): here the number IS in
Result prose, but the fact that makes it non-misleading (its exp-108
provenance) is not. **Fix**: add an explicit attribution/source-note line
to the assembled `result_text` (or a `wall_time_source` sidecar string
threaded into it) disclosing these figures are exp-108's own historical
spend, reused verbatim, zero new FDTD this cycle.

**Attack 5 — [unfalsifiable] The binding Execution-requirement leaves
R23's "human-readable-citation" half open, unbound by anything falsifiable
— independently confirmed at §0.5.** The proposal's own §4 table commits
Phase 4's NOTES.md only to quoting the item_ii OLD-vs-NEW comparison and
the pass/fail of both live asserts. Nothing obligates NOTES.md's own Result
section to quote `results.json['result_text']`/`['predictions_text']`
verbatim rather than paraphrase — exactly the gap exp-108's own Phase-5
VISION review (§2d, §0.5 above) found as a *recurring*, not novel, defect
on this document family. As currently scoped, a Phase-4 author could
satisfy every binding requirement in this proposal while still writing a
hand-typed paraphrase of the DISCLAIMER in NOTES.md's Result section — the
R4/R23 "hand-typed prose instead of code-generated, asserted text" failure
shape, unclosed by anything this document requires checked. **Fix**: add a
binding clause requiring Phase 3/4's NOTES.md Result section to quote
`results.json['result_text']`/`['predictions_text']` verbatim, in full.

**Attack 6 — [governance-completeness, non-blocking] The `analyze.py`
companion-edit patch is described only in prose, not shown as an exact
diff, and (by the proposal's own disclosed idealization) is never
exercised this cycle.** Unlike `classify_item_ii()`'s "exact new body"
(given verbatim, §2 of the proposal), the required `analyze.py` line-85
companion edit is described only as "item_ii dict below gains
`stat_used`/`stat_source` keys, verdict/`delta_boxA` keys unchanged in name
and meaning." `analyze.py` is explicitly not re-run this cycle (no live
phasor pickles remain, per the proposal's own Idealizations) — so this
edit, whatever its exact final form, ships untested this cycle, an
R18-adjacent gap (new code joining an already-partially-verified
architecture without its own executed check) that the proposal's own §5
R18 disclosure does not explicitly cover (that disclosure names only
`classify_item_ii()`'s new branch, not this companion call site). **Low
severity** — a mechanical dict-merge, not new classification logic — and
does not gate Phase 4 (Phase 4 has zero new FDTD calls regardless of this
file's state). **Fix (optional, not mandatory)**: show the exact
`analyze.py` diff in Phase 3, or explicitly extend the existing R18
disclosure to name this call site too.

**Attack 7 — [constraint-#3-violation check, structural, negative
result]** Independently re-confirmed at §0.6: no touched or added code
path in this proposal reads or writes σ(I), σ(x,t), ε(ω), an absorption
parameter, or a perceptual/Weber-contrast quantity — the entire diff is a
classification-statistic gate plus a text/persistence pipeline over
already-committed scalars. **T1 = N/A is correct; no constraint-1/2/3/4
verdict is touched.** No violation found; recorded per this program's own
precedent (exp-108 Attack 4) of stating the negative result explicitly
rather than leaving constraint-immunity as an unchecked assertion.

---

## 2. Disposition of the five blind Phase-2 critiques

**PHOTONICS — ADOPT the core finding in full (§0.2, Attack 1).** The
sibling-precedent misdescription is real and independently re-traced from
`run.py` source, not merely the critique's restatement. **Partial override
of framing, not substance**: PHOTONICS' own flip condition offers two
alternatives ("rest the rejection solely on the OLS-inequality proof... or
explicitly correct the item_i description"). Red Team's own independent
finding at §0.3 (the original mandatory fix's own text already specifies
raw `std` as the non-smooth default) supplies a *third*, stronger ground
neither PHOTONICS nor the proposal cites — folded into mandatory fix 1
below rather than treated as a simple either/or.

**ELECTROMAGNETISM — ADOPT in full, unconditionally.** The
inequality re-derivation (2.897e-6 ≤ 5.008e-6 at r=156; 2.102e-6 ≤ 2.124e-6
at r=312) and the "conservative w.r.t. false-CONFIRM, liberal w.r.t.
false-REFUTE" correction are both independently re-verified exact at §0.1
and Attack 2. No override.

**THERMODYNAMICS — ADOPT both findings in full.** The `n_fdtd_calls=6`/
`total_wall_s=7712.0` provenance check and the undisclosed AND-combination
gap (§0.4, Attack 3) are both independently confirmed. The wall-time
attribution concern (Attack 4) is independently confirmed as a real,
distinct gap from R21's own literal shape (R21 concerns a finding never
narrated at all; this concerns a narrated number missing its own
attribution) but recognizably in the same lineage — treated here as its
own attack, not folded into R21 by name, since R21 is scoped to the
NETD/thermal-sidecar channel specifically and this is a different channel.
No override.

**QUANTUM OPTICS — ADOPT the literal finding and its literal flip
condition (persist/narrate the 1.73×/1.01× raw/residual ratio) — explicit
scope discipline applied, not a rejection.** The ratio re-derivation is
exact (§0.1). QUANTUM's sharpest attack also *names*, without requesting
as its flip condition, a deeper question: whether `R2_SMOOTH_THRESHOLD=
0.90` — borrowed from `classify_item_i`'s different anisotropy-detection
question — is itself calibrated for item ii's question. **Red Team does
NOT extend QUANTUM's finding into a mandatory re-derivation of that
threshold this cycle**, for three independent reasons: (a) it is
non-outcome-reversing at both tested r regardless of exact threshold value
in any defensible range (CONFIRM holds under either branch at both r); (b)
this cycle is explicitly, narrowly scoped to the Tier-0 queue items only
(§5, Idealizations) — re-deriving a shared threshold is exactly the kind
of "manufacturing a third rule the fix never specified" overreach the
proposal itself correctly warns against for alternative (b); (c) it is
already correctly queued as future work, not dropped: exp-108's own
Reconciled Iteration-86 queue Tier 2 item 3 ("formalize the absolute-floor
six-margin family from a resolution/aliasing bound") is the right vehicle.
This is a genuine, disclosed override of a possible over-reading of
QUANTUM's critique, not of anything QUANTUM itself demanded.

**VISION SCIENCE — ADOPT in full, unconditionally.** The exp-108 §2d
citation and the gap between it and this proposal's own binding
Execution-requirement row are both independently confirmed exact (§0.5,
Attack 5). No override.

---

## 3. Resolving tensions between critiques

**PHOTONICS wants the item-i analogy corrected or removed; does this touch
EM's or QUANTUM's own recommended text edits?** No material tension.
PHOTONICS' fix targets the alternative-(b)-rejection paragraph specifically
(§4, the "why raw std, not forced AMBIGUOUS" discussion). EM's fix targets
a different sentence in the *same section* — the "conservative... in every
case" clause inside bullet (a)'s own OLS-inequality discussion — and
QUANTUM's fix targets the `stat_source` string and Result prose
specifically for the ratio. These are three non-overlapping edits inside
one §4; none of PHOTONICS' correction changes the truth value of EM's
inequality-direction correction or QUANTUM's ratio figures, and none of
EM's or QUANTUM's edits depend on the item-i analogy standing or falling.
All three can and should be applied together, in the same Phase-3 pass over
§4, without sequencing constraints between them.

**Does closing R24's second instance (this cycle's whole point) create any
new R24-shaped risk of its own?** Checked directly: the fix's own specified
consequence (fall back to raw `std` when not smooth) IS wired directly into
`classify_item_ii()`'s executed body (§2 of the proposal, independently
re-run against committed primitives at §0.1) — not merely narrated. No new
R24 instance. The one genuinely underspecified reduction rule found this
cycle (Attack 3, `gate_p0_pass`/`repro_pass`) is a *specification* gap in
new code, not a *rule stated but never wired* gap in already-adopted code —
a different, milder shape than R24's own trigger condition.

**Does Tier-0 item 3's fix quietly attempt to rule on the Iteration-85
Checkpoint-4 firing itself (Tier-0 item 0, explicitly out of scope)?**
Checked directly: fixing the code defect that CAUSED the Checkpoint-4
firing (§0.6, Attack 7 confirms no constraint/T1 scope creep) is not the
same act as ruling on the firing's own governance consequence (a Marsh-only
call). The proposal correctly treats these as separate and defers only the
latter. No defect found here.

---

## 4. Overall verdict: **PROCEED-WITH-MANDATORY-FIXES**

The governance/instrumentation work is sound in structure and, on the one
substantive question this cycle actually decides (item ii's own smooth-gate
fallback statistic), sound in execution: the OLS-inequality proof is
airtight (§0.1), the fix is wired directly into the executed classification
path rather than narrated (closing R24's second instance for real, not
merely a third time in prose), and the predicted CONFIRM/CONFIRM outcome at
both r reproduces exactly from already-committed primitives. Nothing in
this cycle's diff touches, varies, or scores a mechanism, so T1/constraint
scoring is correctly, structurally N/A throughout (§0.6, Attack 7). No
attack below rises to internal inconsistency threatening the core fix,
unfalsifiability of any predicted outcome, an inexpressible mechanism (none
proposed), or a constraint violation. All seven attacks are text/code
completeness gaps — a misdescribed sibling-code analogy, an overclaimed
"conservative in every case" generalization, an undisclosed boolean
reduction rule, a missing wall-time attribution note, and an unclosed
human-readable-citation half of R23 — each cheap to close, each entirely
inside this cycle's own already-scoped Tier-0 zero-FDTD remit, none
requiring any new `Sim.run()` call.

**Mandatory fixes, before Phase 3 freezes NOTES.md (this cycle has zero
new FDTD calls, so "before Phase 4" and "before Phase 3 synthesis is
written" are the same gate here):**

1. **[PHOTONICS + Red Team, §0.2/§0.3, Attack 1]** Correct §4's rejection
   of alternative (b): `classify_item_i()`'s CONFIRM branch
   (`confirm_all_margins and not runs`) never reaches the loop that calls
   `linear_fit_1_over_margin`/tests smoothness — it is structurally
   incapable of facing a smoothness judgment, not a deliberate design
   choice to exempt null findings from one. Rest the rejection instead on
   (a) the OLS-inequality proof (§4 bullet (a), independently re-verified
   airtight) and (b) the original Iteration-85 mandatory fix's own text
   (`experiments/108-.../phase2_redteam_audit.md:340–347`), which already
   specifies raw `std` as the fix's own pre-registered non-smooth default —
   a strictly stronger, more directly on-point ground than either the
   item-i analogy or the OLS proof alone.
2. **[ELECTROMAGNETISM, Attack 2]** Replace "more conservative... in every
   case" (§4 bullet (a) prose AND the generated `stat_source` string) with
   an accurate two-sided statement: conservative against false-CONFIRM,
   liberal/anti-conservative against false-REFUTE (since `stat ≥ boxA`
   fires REFUTE, and inflating `stat` only ever makes that easier). Applies
   to both the human-authored prose and the machine-generated
   `stat_source` text — R21's "the artifact a future citation will
   actually quote" standard, applied to a string, not only a persisted
   field.
3. **[QUANTUM OPTICS, §0.1]** Persist and narrate, in `stat_source` and
   Result prose, the raw/residual ratio whenever the fallback fires:
   **1.729× at r=156, 1.010× at r=312** (both re-derived exact,
   independently of QUANTUM's own arithmetic). Gives the next cycle that
   scores this gate (the queued r=624 point) a concrete number, not only a
   caveat sentence.
4. **[THERMODYNAMICS, §0.4, Attack 3]** State explicitly, in
   `reclassify_108.py`'s own code and docstring, that `gate_p0_pass` and
   `repro_pass` are each the logical AND of the corresponding per-r
   `pass_` field at r=156 AND r=312 (four source booleans, all
   independently confirmed `True` this audit) — not an undisclosed
   reduction a reader must infer.
5. **[THERMODYNAMICS, Attack 4]** Add an explicit attribution/source-note
   line to the assembled `result_text` disclosing that the
   `{n_fdtd_calls} real FDTD calls, {total_wall_s}s... total wall time`
   figures are exp-108's own historical spend, reused verbatim — zero new
   FDTD calls this cycle — so a future verbatim citation of exp-109's own
   `result_text` cannot misread that spend as this cycle's own.
6. **[VISION SCIENCE, §0.5, Attack 5]** Add a binding clause requiring
   Phase 3/4's NOTES.md Result section to quote
   `results.json['result_text']` and `['predictions_text']` verbatim, in
   full — not a paraphrase — closing the specific "human-readable-citation"
   half of R23 that exp-108's own Phase-5 VISION review (§2d) found still
   open, and that this proposal's current binding Execution-requirement row
   does not cover.

**Additionally, non-blocking, recommended (Attack 6):** either show the
exact `analyze.py` line-85 companion-edit diff in Phase 3, or explicitly
extend the existing R18 disclosure (§5 Idealizations) to name this call
site alongside `classify_item_ii()`'s own new branch, since it too ships
unexercised this cycle.

**Explicit overrides (stated per this program's own Director/Red-Team
transparency discipline, one level down):** Red Team does **not** extend
QUANTUM OPTICS' critique into a mandatory re-derivation of
`R2_SMOOTH_THRESHOLD=0.90` for item ii's own question this cycle (§2,
QUANTUM disposition) — non-outcome-reversing at both tested r, out of this
cycle's own disclosed Tier-0-only scope, and already correctly queued
(exp-108 Reconciled Iteration-86 queue, Tier 2 item 3). This is the only
override; all five critiques' own literal findings and literal flip
conditions are otherwise adopted in full.

**R-lineage note (not a firing, a caution for Phase 3):** none of the six
mandatory fixes above constitutes an R-rule firing — all are caught here,
blind, before Phase 3 freeze, matching this program's own unbroken
discharge-test precedent (R11/R12/R13/.../R25's shared "does not fire on
its own founding instance, caught before freeze" pattern). Left unfixed
into a frozen NOTES.md, fix 5 (wall-time attribution) would be a strong
candidate for a fresh R21-lineage instance on a new channel, and fix 6
(verbatim Result-section citation) would extend R23's own still-open
human-readable-citation gap past its first identified instance
(exp-108 §2d) into a second — worth naming explicitly since R23 itself
"carries no forward-elevating clause" (LOGBOOK.md, Iteration-85 CHECKPOINT
block) and so would not auto-fire Checkpoint criterion 4 even on a genuine
second instance, making pre-freeze closure here the only enforcement
mechanism available.
