# Phase 5 Review — PHOTONICS (exp-113, Panel Iteration 90)

*Fresh sub-agent, blind context. Charter (verbatim, PANEL.md): surface
interaction, absorption spectra, angular dependence, scattering cross-
sections — is the proposal's optical response coherent as stated, across
wavelength and angle? I have not seen and did not seek out any other
seat's Phase-5 output this cycle. Read PANEL.md in full; LOGBOOK.md's
RULED OUT registry (R1–R31 in full, R27–R31 read closely), the T28
live-thread opening (`sed -n '3094,3200p'`), and the full Iteration-89
entry (`sed -n '24215,24415p'`). Read every file in
`experiments/113-t28-r312-cpl25-plus168-bin/` in full:
`phase1_proposal.md`, all five Phase-2 critiques, `phase2_redteam_audit.md`,
`NOTES.md` (Phase 1 through Combined Verdict), `run113.py`,
`chunk_runner113.py`, `analyze113.py`, `results.json`. Independently
re-ran `python3 run113.py --verify-geometry` (fresh this session:
`pass_=true`, zero mismatches, both r) and `python3
lab/validation/run_all.py` (fresh this session: **43/43 checks passed**,
185s), read `results.json` directly with Python/`json`, and re-derived
every numeric claim below from primitives — nothing here is taken from
NOTES.md's own transcription. No real FDTD run by me; I did not touch
`chunk_runner113.py` or invoke any `Sim.run()`.*

## Verdict: **CONFIRM-WITH-GAPS**

Every load-bearing numeric claim in this cycle's own record reproduces
exactly from primitives: the box_a wavelength-clearance figures (3.2λ at
r=156, 6.4λ at r=312, exactly `kappa_ratio=2.0`), the three sponge-margin
figures (4.0175 / 3.4298 / 2.4664 orders, against floor / signal / |delta|
respectively), the R31-scaled cost-gate arithmetic (`16737.4s` vs. the
`10800s` bound, bit-exact re-derivation of `scaled_total=670.4778/
0.40643257=1649.665s` → `projected=1649.665·2.0^3.20533·1.1=16737.44s`),
and the raw/naive `6802.6s` figure the Reconciled-Iteration-90 queue
itself cited. `results.json`'s `gate_refused`/`named_bin_reached=False`
branch is internally consistent: it carries none of the real-data-
dependent keys (`resolution_check`, `named_bin`, `pattern_delta`,
`energy_ledger`, `total_wall_s_by_scene`) that the "have all three
scenes" branch of `analyze113.py` would have written — because that
branch never ran. This is the cleanest gate-refused record this T28
sub-thread has produced (cleaner than exp-111's sequencing-choice
deferral or exp-112's density-choice deferral): a real, disclosed,
correctly-upstream (R28) refusal, not a documentation gap dressed up as
one.

Not plain CONFIRM, because two real, previously-uncaught completeness
gaps surface under my own charter's re-derivation duty (below) — neither
outcome-reversing, both genuinely new (not raised at Phase 2 by anyone,
including Red Team's own audit), and both in the same "frozen text
lags the real branch that executed" shape this program's R23 lineage
exists to catch.

## Findings

### F1 — Confirmed true: Fix 1/Fix 2's disclosure content is geometry/baseline-only and remains fully accurate despite zero real r=312/cpl=25 data this cycle

This was the task's own open question, and I did not assume the answer.
Traced both fixes to their inputs in `run113.py`:

- **Fix 1** (`_BOX_A_CLEARANCE_LAMBDA_R156`/`_R312`) is computed purely
  from `geom_fixedabs_cpl(r, 25)`'s own returned geometry dict
  (`box_a`, `CX`, `R_COAT`, `cpl`) — a pure function of fixed
  construction constants, zero dependency on any `Sim.run()` output at
  either `r`. I re-derived it independently: `geom_fixedabs_cpl(156,25)`
  → clearance 80 cells/25=**3.2λ**; `geom_fixedabs_cpl(312,25)` →
  clearance 160 cells/25=**6.4λ**, ratio exactly 2.0. Correct and
  unaffected by the gate refusal.
- **Fix 2** (`_SPONGE_MARGIN_ORDERS_{FLOOR,SIGNAL,DELTA}`) uses
  `BASELINE_FLOOR`/`BASELINE_PECCORED`/`BASELINE_HOLLOW`/`BASELINE_DELTA`
  — all four pulled from `experiments/110-.../results.json["r312"]`, the
  **cpl=20 baseline already committed by exp-110**, not anything this
  cycle's own Phase 4 would have produced — plus `_SPONGE_ABS_VAL`,
  reused verbatim from exp-112's own cpl=25-specific (not r-specific)
  correction. I re-derived all three figures from these same primitives
  independently (`4.0175`/`3.4298`/`2.4664`, matching to 4 significant
  figures) and confirm none of the three depends, even indirectly, on
  cpl=25 r=312 data.

Both fixes' figures appear, byte-identical, inside the `DISCLAIMER`
string actually persisted in `results.json`'s `result_text` (I read this
directly, not from NOTES.md) — so the disclosure a reader sees in the
real, frozen record is exactly as accurate as it would have been had the
gate approved the spend. This is good instrument-discipline design: the
two fixes with the least real-data dependency are also the two immune to
this cycle's own gate refusal.

### F2 — Genuinely new: the shared `DISCLAIMER` string's present-tense phrasing over-claims in the gate-refused branch specifically

`DISCLAIMER` (the R23 single-source-of-truth constant) is interpolated
unconditionally into both `build_predictions_text()` and
`build_result_text()` — correct hygiene for avoiding cross-branch
divergence, but it means two of its own clauses, written when Phase 4's
outcome was still unknown, read as false once the actual branch that ran
is known:

- *"...was never validated at r=312, **the geometry this cycle actually
  tests**."* — false in the branch that actually executed:
  `named_bin_reached=False`; r=312 was the geometry this cycle *intended*
  to test and was gated before doing so. Zero `Sim.run()` calls occurred
  at r=312 this cycle (confirmed: `results.json` carries no r=312 field
  data of any kind).
- *"...**this cycle's own scored Check-B reading** is the
  CPL_RATIO-normalized one."* — no Check-B reading of any kind was ever
  computed this cycle; `classify_resolution_check()` was never called
  (it requires the real `pat_delta` array that only exists in the
  unreached branch).

Both clauses are accurate as *predictions* (in `predictions_text`, they
describe the plan) but are stale, uncorrected carry-overs when the
identical string is re-used inside `result_text` for the branch that
actually shipped. The surrounding Result-section prose (`NOT REACHED --
R27/R28/R31 cost gate REFUSED...`) does correctly disambiguate this for
anyone reading the whole block — so this is not the "STILL implies real
r=312 data exists" failure mode at the level of the frozen record taken
as a whole. It is a real, if narrow, instance of exactly that failure
mode at the level of the shared `DISCLAIMER` string taken in isolation
— precisely the kind of citation-shortening risk this program's own
R4/R9 lineage was created to catch (a future citation that quotes only
the `DISCLAIMER` block, not the surrounding Result text, would
mischaracterize this cycle as having produced a scored Check-B/Check-C
reading). Non-blocking (does not change any verdict-arithmetic; the
actual scored fields don't exist to be miscited), but a genuine gap this
seat's own charter (is the optical-response account coherent *as
stated*) exists to flag.

### F3 — Genuinely new: `NOTES.md`'s own "Setup" section states a plan as an accomplished fact, uncorrected after Phase 4

`NOTES.md` §Setup (written at Phase 3, before Phase 4 ran, per house
discipline): *"...3 real FDTD calls this cycle (empty/hollow/peccored,
r=312, cpl=25), R31-gated by a same-session control point..."* — phrased
in the present/declarative, not as a stated intention. The Phase 4 and
Result sections further down the same document correctly report what
actually happened (6 real FDTD calls, all at r=156; zero at r=312), but
the Setup section itself is never retroactively annotated. A reader who
stops at "Setup" (a plausible failure mode for a long document — the
same shape F2 names) would conclude 3 real r=312 FDTD calls were made
this cycle; they were not. Same non-blocking, disclosure-completeness
class as F2, not a new category.

### F4 — Independently caught: a stale trust-suite figure in `NOTES.md`

`NOTES.md` cites the trust suite as **41/41** in two places (Phase-3
verification, line ~107; Combined-Verdict-adjacent Phase-4 re-check, line
~242). `phase1_proposal.md`'s own citation (line ~397, the same cycle)
says **43/43**. I independently re-ran `python3 lab/validation/run_all.py`
fresh this session: **43/43 checks passed, 185s** — confirming
`phase1_proposal.md`'s figure is the correct, current one and `NOTES.md`'s
`41/41` is stale (most likely an uncorrected carry-over of exp-112's own
early-Phase-3/4 count, before exp-112's own Phase 5 added new stages that
brought the total to 43 — exp-112's `phase5_redteam_audit.md` and
`phase5_review_thermodynamics.md` both cite 43/43). Non-consequential (the
suite is genuinely green either way, and no `lab/` diff exists this
cycle — I confirmed zero uncommitted changes under `lab/`), but it is a
real, independently-verified numeric transcription defect inside the same
document that asserts, elsewhere, that "all numeric claims were verified
against primitives" — worth a same-shift correction the next time
`NOTES.md` is touched.

### F5 — Confirmed: which of the five Phase-3 fixes got real exercise this cycle

Directly answering the task's own question, verified against
`results.json`'s actual key set (not assumed):

- **Genuinely exercised for real, on real (new) FDTD data this cycle**:
  the R27/R28/R31 cost-gate machinery itself, and Fix 3b/Fix 4 (the
  commensurable 3-scene-blend short+sustained control) — all ran for
  real, on real r=156/cpl=25 `Sim.run()` calls (6 calls, 878.2s total,
  `r31_control` block present in `results.json` with genuine measured
  `speed_ratio` values I independently recomputed bit-exact). This is
  the first time in this rule's own history that R31 has actually
  reversed a would-be-unsafe decision rather than merely being present.
- **Content is correct and meaningful, but never touched by real
  cpl=25/r=312 data because it never needed to be** (F1, above): Fix 1
  and Fix 2's own disclosed figures.
- **Never exercised against real data this cycle, code untested in
  production**: Fix 5 (the `low_percentile_outlier`/
  `high_percentile_outlier`/`direction_validated` fields inside
  `classify_resolution_check`) and Fix 5b (`resolved_unresolved_crosstab`
  in `analyze113.py`) — both live only inside the "have all three r=312
  scenes" branch of `analyze113.py`, which never ran. `results.json`
  carries no `resolution_check` key at all. R32's own direction question
  (does low or high correlation indicate real structure?) is exactly as
  unresolved after this cycle as it was after Phase 2 — not a regression,
  simply a genuinely deferred question, and correctly disclosed as such
  in the Combined Verdict.

## Charter-fit note

Like every T28 desk/instrument cycle since Iteration 46, my charter's
substantive question (is a scattering/absorption response coherent
across wavelength and angle?) has no data to examine this cycle — zero
angular-scattering-pattern data of any kind exists for r=312/cpl=25
anywhere in this repo. What I can and did police is whether the
optical-geometry bookkeeping that *does* exist (box_a depth, sponge
margins, the congruent-scaling recipe) is internally coherent and
correctly disclosed — confirmed yes, with the two narrow gaps above.

## Ranked top-3 candidate directions, Panel Iteration 91

1. **Before anything else, cheaply diagnose whether the 0.41×
   "this-session-is-slower" reading is genuine hardware/session variance
   or a confounded measurement, before either waiting for a faster
   session or asking Marsh to relax the bound.** R31's own control
   machinery assumes any speed difference reflects real per-step FDTD
   throughput, but the control's own wall-clock timing (`_time_control_blend`,
   plain `time.time()` around `sim.run()`) cannot distinguish genuine
   hardware slowness from transient contention on a shared machine
   (concurrent unrelated processes, thermal throttling, a noisy-neighbor
   effect) — exactly the class of confound this program's own R28
   (kappa-exponent fit) and EM's Phase-2 critique (3-scene-blend
   inflation) have both previously found stacking anti-conservatively in
   this same gate. A near-zero-cost check: re-run `--control` a second
   time, back-to-back, in immediate succession with nothing else running,
   and see if `speed_ratio` is stable; if it drifts by more than a small
   tolerance, the 0.41× figure is measuring session noise, not FDTD cost,
   and the real per-step cost may already be within budget. This is
   cheaper than either of the two options below and should be resolved
   first regardless of which is chosen next.
2. **If the control reading holds up, try a genuinely cheaper geometry
   variant of the same named-bin question rather than the full 3-scene/
   48-bin r=312 pattern** — e.g., a reduced angular capture (only the
   named bin's own ±2-bin neighborhood, not the full 48-bin sweep) or a
   reduced-STEPS early read exploiting the checkpoint/resume machinery
   already built (does `local_snr`'s trend already resolve at, say, 8000
   of the 16000 STEPS, before the sponge/boundary transient has fully
   settled?). Either could bring the projected cost under `10800s`
   without needing new hardware or a policy exception, though either
   would need its own Phase-2 scrutiny of whether it still tests the
   same physical question (the same class of confound Fix 1 flagged for
   box_a's own margin choice).
3. **If neither of the above closes the gap, take this to Marsh as a
   named, disclosed ask: a one-time relaxation of `COST_GATE_TOTAL_S`
   for this specific, already-fully-gated leg.** The gate is working
   exactly as designed (R28 upstream, R31 same-session-controlled) and
   the projected overrun is a modest ~55% over a 3-hour bound, not an
   order-of-magnitude blowout — a materially different ask than raising
   the bound generally. This is now the third consecutive cycle this
   exact named bin has been deferred (sequencing, then density risk, now
   a genuine cost-gate refusal) for reasons that are each individually
   correct but collectively read as this program's own resource ceiling,
   not its methodology, being the actual bottleneck on its own
   highest-value queued item — worth a direct, disclosed statement to
   that effect rather than a fourth quiet re-deferral.
