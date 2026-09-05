# Phase 5 Review — VISION SCIENCE, self-review (exp-113, Panel Iteration 90)

**Fresh sub-agent, blind context, self-review.** I am a different instance of
this seat than the one that wrote `phase1_proposal.md` — I have not seen its
own reasoning, only its outputs (this document, the code, and the five blind
critiques + Red Team's audit it drew). I have not seen and did not seek out
any other seat's Phase-5 output this cycle. Read: `PANEL.md` in full;
`LOGBOOK.md`'s RULED OUT registry lines 1–1400 (R27–R31 in full); the T28
opening (`sed -n '3094,3200p'`); the full Iteration-89 entry
(`sed -n '24215,24415p'`); and, in the experiment directory,
`phase1_proposal.md`, all five `phase2_critique_*.md`,
`phase2_redteam_audit.md`, `NOTES.md`, `run113.py`, `chunk_runner113.py`,
`analyze113.py`, `results.json` — all in full. Every numeric claim below was
independently re-derived from `results.json`/`run113.py`/`chunk_runner113.py`
primitives via direct computation (shown inline), not taken from any
document's own prose. I also independently re-ran the fast trust-suite
invocation this session (`python3 lab/validation/run_all.py --only
12346789`) rather than trusting NOTES.md's own citation. No `Sim.run()` call
made by me; nothing below required one. (Incidental note for transparency:
a directory-wide grep I ran for the string `"41/41"` briefly surfaced two
lines of `phase5_review_quantum.md`'s own text in the tool output before I
registered what the file was; I did not open or otherwise read that file,
did not use its content, and had already independently located and begun
investigating the same 41-vs-43 question myself from `phase1_proposal.md`
line 397 vs. `NOTES.md` lines 107/242 before that grep ran. The finding
below is my own, independently re-derived from primitives, not borrowed.)

## Verdict: **CONFIRM-WITH-GAPS**

My own original Phase-1 proposal's framing, predictions, and idealizations
hold up well under independent re-derivation — no numeric claim I checked is
wrong, and the charter-fit call is unaffected by the outcome. But two real,
non-trivial gaps survive into the frozen record: (1) the R32/Fix-5b
direction-validation apparatus my own proposal's Phase-3 fix built is
entirely **unexercised on real data** this cycle, a fact easy for a future
citation to elide; and (2) the R31 control-representativeness fix (Fix 3b/4)
closes the *duration* half of THERMODYNAMICS' own Phase-2 finding but not the
*grid-size* half, and the residual is not named as an explicit caveat in the
R23-protected `DISCLAIMER` text. Neither gap is a defect that should have
blocked this cycle, and neither changes the Combined Verdict (PARTIAL,
correctly the Director's own label) — but both are worth naming plainly
before Iteration 91 treats this cycle's machinery as fully closed.

## Findings

### 1. Charter-fit re-assessment: does the REFUSAL change it? No — verified explicitly, not assumed.

My own original proposal (§0, stated up front rather than buried in
Idealizations) declared that this seat's "pin numeric thresholds... BEFORE
any run that scores against them" duty does not bind this cycle, because no
Weber-contrast/`C_thr(L)`/luminance-edge/spectral-sensitivity/adaptation/
temporal-sensitivity claim is made or scored anywhere in the document — this
is instrument-fidelity/resolution-convergence work, not phenomenon work.

The cost-gate REFUSAL is a pure resource-budget event: `chunk_runner113.py`'s
own `check_cost_gate_for_r312` (confirmed, by direct reading, called
unconditionally before `step_budgeted(...)` on every r=312 invocation,
lines 238–240) raised `RuntimeError` before any `Sim.run()` call touched
r=312 at all. Nothing about *why* the gate refused (a same-session
per-step-speed measurement, `speed_ratio=0.406`, vs. a `10800s` wall-clock
bound) introduces any perceptual quantity, threshold, or claim — it is
arithmetic over wall-clock seconds. I traced every field in `results.json`'s
`cost_gate`/`r31_control` blocks (reproduced bit-exact below) and none of
them is, or could be recast as, a perceptual measurement. **The charter-fit
call is unchanged, and explicitly confirmed rather than assumed**: a REFUSED
gate is exactly as charter-irrelevant to VISION SCIENCE as an APPROVED one
would have been, because the gate sits entirely outside the phenomenon/
perceptual layer in either direction. My own proposal's declining "to force
a vision-science mechanism angle onto content that is not phenomenon work"
was and remains the correct call.

What *does* remain squarely mine, unaffected by the outcome: the two
DISCLAIMER additions §7 names (the ABSORB/EDGE sponge restoration, and the
prophylactic disambiguation of Check C's "percentile"/"null population"/
"outlier" vocabulary from signal-detection-theory vocabulary). Both survive
into the frozen `results.json` text verbatim (confirmed by direct string
search in `results.json`'s own `predictions_text`/`result_text` fields) —
the vocabulary-disambiguation addition in particular turns out to have
protected exactly the text that actually shipped, since the gate-refused
branch still renders the full `DISCLAIMER` (see §3 below). It was not wasted
effort on a leg that never produced named-bin data; it protects the
permanent record regardless.

### 2. R23 discipline in the gate-refused branch — genuinely enforced now; a real forward risk named, not a present defect

`analyze113.py`'s early-exit branch (lines 142–198, the code path that
actually executed this cycle) carries its **own** independent pair of R23
asserts:

```
159:            assert R.DISCLAIMER in predictions_text
184:            assert R.DISCLAIMER in result_text
```

— distinct from, not merely inherited from, the normal-path asserts at
lines 219/244 (which never execute this cycle, since `raise SystemExit(0)`
at line 195 exits first). Both fired on real, live execution (NOTES.md's own
claim, and independently confirmed by me: `results.json`'s own
`predictions_text`/`result_text` fields both contain the full `DISCLAIMER`
string verbatim, checked by direct substring search).

More importantly, the *design* is more robust than "someone remembered to
paste two asserts": `DISCLAIMER` is a single module-level string constant,
embedded unconditionally inside the literal body of `build_predictions_text`
and `build_result_text` (`run113.py` lines 577, 618) — not passed as a
parameter, not reconstructed per call site. **Both branches of
`analyze113.py` call the same two functions** (gate-refused: lines 158, 162;
normal: lines 218, 238) rather than each branch building its own text. This
is the opposite shape from the one that caused the R23 First Addendum
(Iteration 88, exp-111): there, a *new* disclaimer-successor string
(`DISCLAIMER_88`) was built by a bespoke pair of functions, one of which
(`build_result_text_88`) was never actually wired to an assert or a
committed call site. Here, there is no second string and no bespoke
builder — the gate-refused branch reuses the exact same single source of
truth the normal branch does.

**The forward risk, stated explicitly since the task asks for it**: the
gate-refused branch is now real, tested, working code — but it is also, by
construction, code that runs only when a future cost-gate decision refuses,
which this program's own house discipline hopes becomes progressively rarer
as sessions/hardware/controls improve. A future editor revising this branch
(e.g., to add more diagnostic detail to the refusal message, exactly the
kind of edit this branch already required once) could plausibly do so by
writing a bespoke f-string directly rather than continuing to call
`R.build_predictions_text`/`R.build_result_text` — precisely the shape that
produced the R23 First Addendum, in precisely the kind of less-exercised,
lower-scrutiny code path that shape favors. Nothing here is broken today;
I am naming a specific, non-hypothetical recurrence vector for Red Team's
own Phase-5 audit to weigh (a candidate addition to the R23 lineage,
alongside the First Addendum: *a shared single-source-of-truth builder
function must not be bypassed by a new branch's own bespoke text, even when
that branch is reached rarely* — I do not have standing to ratify this
unilaterally in a self-review; I flag it as a finding, not a rule).

### 3. Independent re-derivation of NOTES.md's own Phase-4/Result section — all bit-exact, zero corrections needed

Re-derived directly from `results.json` (not from NOTES.md's own prose):

| Quantity | NOTES.md's claim | `results.json` primitive | Match |
|---|---|---|---|
| Short control: steps/scene, wall-s, speed_ratio | 1000, 190.7s, 0.439 | `r31_control.short`: 1000, 190.74358129501343, 0.43938422809539435 | exact |
| Sustained control: steps/scene, wall-s, speed_ratio | 3334, 687.5s, 0.406 | `r31_control.sustained`: 3334, 687.4980702400208, 0.40643257440437214 | exact |
| Used reading (lower, more conservative) | sustained | `used_label: "sustained"` (0.406 < 0.439) | exact |
| Total FDTD calls / wall time this cycle | 6, 878.2s (14.64 min) | `n_fdtd_calls=6`; `878.2416515350342/60=14.637...` | exact (sum of short+sustained `n_scenes`, `control_wall_s`) |
| R31-scaled projection vs. bound | 16737.4s vs. 10800s, REFUSED | `cost_gate.scaled.projected_312_total_s=16737.440100170577`, `total_pass=False` | exact |
| Naive/uncontrolled projection (would-have-approved) | 6802.6s, APPROVED | `cost_gate.raw.projected_312_total_s=6802.6408688513`, `total_pass=True` | exact, and reproduces Iteration-89's own briefed figure bit-exact |
| Session speed vs. historical | 0.406× (slower) | same field | exact |

I also re-derived the underlying formula chain by hand (not just compared
stored fields): `speed_ratio = historical_per_step_s / this_session_per_step_s`
for both short (0.02793657.../0.06358119...=0.439384...) and sustained
(0.02793657.../0.06873606...=0.406433...); `scaled_total = pilot_total_wall_s
/ used_speed_ratio` (670.4777698516846/0.40643257440437214=1649.6654354889522,
matching `cost_gate.scaled.pilot_total_wall_s` exactly); and
`projected = pilot_total_wall_s × kappa_ratio^kappa_exponent × safety_margin`
for both raw and scaled branches, reproducing `6802.6408688513` and
`16737.440100170577` to full float precision. **No arithmetic error anywhere
in the chain.**

**A surface-level "discrepancy" I checked and resolved rather than either
ignoring or wrongly flagging**: `phase1_proposal.md` §7 cites the trust
suite at **43/43**; `NOTES.md` (lines ~107, ~242) cites **41/41**, twice.
These are not in conflict. `phase1_proposal.md`'s own text names the bare
invocation, `python3 lab/validation/run_all.py` (no `--only` flag), which
defaults to stages 1–9 **including** the heavy stage 5 (`stage5_cloak`,
which I confirmed by direct source inspection contains exactly 2 `check(...)`
calls). `NOTES.md`'s figures match this program's own long-standing
`--only 12346789` convention (heavy stage 5 explicitly skipped) — I
independently re-ran that exact invocation this session and got **41/41
checks passed in 98s**, zero failures. `41 + 2 = 43` reconciles the two
citations exactly; this is two legitimate, differently-scoped invocations,
not a documentation defect. Re-confirms `git status --short lab/` empty
throughout, matching every claim in the record.

### 4. R32/Fix 5b's direction-validation apparatus is real, correctly-built code — and entirely unexercised on real data this cycle

Fix 5 (QUANTUM's Phase-2 finding, the most consequential of the five, R32
ratified on it) replaced a silently-inverted, single-directional Check-C
reading with two symmetric fields plus a `direction_validated` flag, gated
on `analyze113.py`'s own `resolved_unresolved_crosstab` — which needs real
r=312/`cpl=25` `pattern_delta` data to run. Tracing the control flow: that
crosstab call lives inside `analyze_r312_cpl25()` (line 90), which is called
only from the normal-path branch (line 202), which never executes this
cycle (the gate-refused early exit at line 195 fires first, and no
`r{312}_cpl25_*_done.pkl` files exist to satisfy the `have(...)` check at
line 142 in the first place, since zero r=312 `Sim.run()` calls occurred).

**So `resolved_unresolved_crosstab` ran only on synthetic unit-test data
this cycle (NOTES.md's own disclosure), never on this bin's real data.**
`R32` itself is correctly ratified as a *governance rule* regardless (it
does not depend on this cycle's own data landing — it is a standing
discipline for any cycle that recalibrates a statistic's direction), and
nothing in NOTES.md or the DISCLAIMER overclaims otherwise — `results.json`
correctly has no `resolution_check`/`check_c` block at all this cycle (the
gate-refused `out` dict, lines 185–192 of `analyze113.py`, carries no such
key). But this is exactly the kind of fact a future citation could compress
incorrectly ("exp-113 validated Check C's direction per R32") if it only
reads the LOGBOOK entry's headline and not the actual `results.json`
contents — worth stating plainly for Iteration 91: **the direction question
Fix 5b exists to answer remains as open today as it was at Phase 2**, on
both the r=156 bin (exp-112, still thin/non-monotonic per QUANTUM's own
Phase-2 derivation) and the r=312 bin (this cycle, never reached).

### 5. R31 control-representativeness (Fix 3b/4): the *duration* half is closed; the *grid-size* half is not, and isn't named as a residual caveat in the frozen text

THERMODYNAMICS' own Phase-2 sharpest attack named two distinct confounds in
a single-burst control: the burst's *short duration* (cannot see
sustained-load effects) and the control's *smaller grid* (r=156, `N=1400²`)
relative to the production job it gates (r=312, `N=2800²`, "a 4×-larger
array" — THERMODYNAMICS' own phrase, independently confirmed by direct
computation: `2800²/1400²=4`). Red Team's Fix 4 mandated "a second,
sustained reading... comparable duration to a real production sub-chunk,"
and `chunk_runner113.py::run_control()` (confirmed by direct reading,
lines 187–205) does exactly that — `_time_control_blend` is invoked at
`SHORT_CONTROL_STEPS=1000` and `SUSTAINED_CONTROL_STEPS=3334`, both **on
the r=156 grid** (`g = R.geom_fixedabs_cpl(156, 25)`, line 177 of
`chunk_runner113.py` — unconditionally, not parameterized by `r`). Fix 4 as
specified and as coded closes the *duration* dimension precisely as asked;
it does not, and was never asked to, touch the *array-size* dimension.

This residual is disclosed only weakly: the `control_line` text embedded in
`predictions_text`/`result_text` (via `build_predictions_text`, `run113.py`
line 557 on) names "the already-completed r=156/cpl=25 scenes" as the
control's own source — a careful reader can infer the grid-size mismatch
from that phrase, and the underlying code comments (`run113.py` lines
166–176, `chunk_runner113.py` lines 168–176) name the confound explicitly
by its correct physical mechanism (cache/memory-bandwidth saturation at
larger working-set size, turbo-boost decay under sustained load) — but none
of this appears inside the R23-protected `DISCLAIMER` string itself, and no
sentence anywhere in the frozen text states, as a named residual risk
alongside Fix 1/Fix 2's own explicitly-labeled caveats, "this control was
never run on r=312's own, 4×-larger grid; array-size-dependent throughput
effects remain untested by either control reading." A reader who saw only
Red Team's Fix 4 docket item and the DISCLAIMER text could reasonably, if
incorrectly, conclude THERMODYNAMICS' full concern was closed. It was not —
only the half Fix 4 was actually scoped to close was. (This is not a defect
in Fix 4's own execution — it does precisely what THERMODYNAMICS' own
proposed remedy, and Red Team's docket text, asked for. It is a residual
gap in what got carried into the permanent, R23-protected disclosure layer.)

### 6. Nothing in my own original proposal is shown wrong by the real outcome; one planning figure was superseded, correctly disclosed as such

I checked every falsifiable claim and idealization in `phase1_proposal.md`
against what actually happened:

- **Idealization 2 anticipated this exact failure mode before it occurred**:
  "a slower session here would need the `r31_control_ratio` machinery to
  correctly scale the projection UP... `chunk_runner113.py`'s own
  `check_cost_gate_for_r312` is written to raise (not silently proceed) if
  `proceed_to_r312` reads `False`." This is precisely what happened. I read
  this as the proposal's own foresight being validated, not merely
  surviving — worth stating plainly rather than only noting "nothing was
  wrong."
- **§2.1's "FDTD calls this cycle: 3"** did not materialize (6 real calls
  occurred, all at r=156, zero at r=312) — this is not an error in the
  original document; the same section explicitly labels the cost/margin
  figure "provisional" pending the R31 control, and the actual outcome is
  prominently, correctly disclosed in NOTES.md's own Result and Combined
  Verdict sections. A planning number contingent on a gate that could
  refuse is not falsified by the gate refusing; it is superseded, and the
  record says so.
- **The T1-N/A claim, the box_a/CPL_RATIO/sponge/vocabulary disclosures,
  and every geometry/scope claim** all check out unchanged against
  `results.json` and the executed code — no correction needed.

## Ranked top-3 candidate directions for Panel Iteration 91

1. **Re-attempt the `+168.75°`/r=312/`cpl=25` bin — the single carryover
   highest-value item — with a fresh same-session R31 control that ALSO
   closes the grid-size dimension named in Finding 5**: keep Fix 4's
   short+sustained duration pair, but add a third, cheap, bounded
   same-session timing point *on the r=312 grid itself* (e.g. a few hundred
   `empty`-scene steps at `N=2800²`, timing only, no scoring data) before
   trusting the next projection — closing the residual THERMODYNAMICS'
   critique named but Fix 4 didn't reach, at near-zero marginal cost
   relative to the multi-hour production spend it gates.
2. **Execute Fix 5b's `resolved_unresolved_crosstab` for real the moment
   r=312/`cpl=25` data exists — make it an explicit, named Tier-1 queue line
   paired with item 1, not an assumed automatic consequence.** Per Finding
   4, this is real, committed, zero-marginal-FDTD-cost code that has never
   touched real data; Iteration 91 should not let a second gate-adjacent
   deferral (cost this cycle, something else next) push it past a third.
3. **Send Finding 2 (the gate-refused branch's own forward R23-bypass risk)
   to Red Team's own Phase-5 final audit for a ruling** — either fold it
   into a future R23 addendum (a shared single-source-of-truth builder must
   not be bypassed by a new branch's own bespoke text) or explicitly decline
   it as non-actionable; either way it should be adjudicated on the record
   rather than left as an unranked observation in this document alone.

Not in my own top 3, but named for completeness since the Reconciled queue
still carries them: the Tier-2 `cpl=30` third resolution point (gated,
correctly, on items 3–4 of the *previous* queue, now done); the
`R2_SMOOTH_THRESHOLD=0.90` re-derivation (seventh consecutive cycle
undone — orthogonal to this leg); MATERIALS' own fabrication-tolerance bound
(sixth consecutive cycle); the sixth `gate_reposition_control.py`
checkpoint-resume case. None of these engage anything this cycle's own
outcome changed.
