# exp-110 — Panel Iteration 87 (candidate)

**Lead seat: ELECTROMAGNETISM (rotation lead, VISION→PHOTONICS→MATERIALS→
ELECTROMAGNETISM→THERMODYNAMICS→QUANTUM).** Governance/instrumentation
cycle continuing the T28 sub-thread. Executes the Reconciled Iteration-87
Tier-1 queue (LOGBOOK.md Iteration 86, exp-109's own Combined Verdict).
Tier-0 item 0 (ruling on the Iteration-85 Checkpoint-4/R24 firing) is
Marsh's call, explicitly out of scope, not attempted.

## Hypothesis

Three independent Tier-1 items, bundled per this program's own established
practice (Iterations 83–86):

1. Does `classify_item_i`'s global-peak normalization (`rel32`) hide real
   angular-pattern shape structure in the ~62.5% of bins carrying <1% of
   peak power — or is the ~10% local deviation PHOTONICS' own Iteration-85
   self-review found in those bins near-null relative-error blowup? A
   local-magnitude floor-gated diagnostic, built this cycle for the first
   time (informational only, per Red Team Fix 2 — see below), is the
   instrument to find out.
2. Has `linear_fit_1_over_margin`'s own `is_monotonic OR r_squared>=0.90`
   smooth/noise discriminator — load-bearing for both `classify_item_i`'s
   REFUTE branch and `classify_item_ii`'s R24-fix branch — ever itself been
   validated against known-smooth and known-noisy synthetic input? (R18
   discipline: no, not until this cycle.)
3. Does `stage26_chunked_run_identity`'s existing negative control, which
   only tests UNDER-reported `steps_done` (causing an over-run), also catch
   the symmetric OVER-reported direction (causing a truncated run)?

## Grounding-fact correction (Phase 1, independently reconfirmed by all
## five Phase-2 critiques and Red Team)

The Iteration-86 queue's own "zero new FDTD, all data already committed"
premise for item 1 is **false**. The per-bin angular-pattern arrays
`classify_item_i` needs for local-magnitude renormalization were computed
in-memory by exp-108's own `analyze.py` from raw FDTD field captures
pickled to `SCRATCH = ".../b3074561-.../scratchpad/exp108"` — a different,
now-defunct session's ephemeral scratchpad, confirmed gone from this
container by direct filesystem check. `results.json`/`analyze_output.json`
never persisted anything beyond `rel32` (already globally normalized),
`runs=[]`, `run_details=[]`. This is an honest correction to the permanent
record, not a criticism of exp-109 (MATERIALS' own cycle never touched
item 1; the premise was inherited from exp-108's own Phase-5
recommendation, written when the pickles were still live).

**Scope decision, given this correction:** re-capture exp-108's own
identical 6-call geometry (empty/hollow/peccored × r=156/312,
byte-for-byte the same `geom_fixedabs`), this time persisting the per-bin
arrays permanently — closing the data-persistence gap for good, rather than
leaving a fourth cycle to rediscover it cold.

## Phase 2 — accepted/overridden criticisms (Director's disposition)

All five blind Phase-2 critiques (PHOTONICS, MATERIALS, THERMODYNAMICS,
QUANTUM, VISION) landed **support-with-changes**, zero opposition, each
finding a genuinely different defect. Red Team's Phase-2 audit
independently re-derived every consequential claim from primitives (not
trusted on the critiques' own say-so — see `phase2_redteam_audit.md` §1),
found two of the five attacks (PHOTONICS' and QUANTUM's, both on the
mirror-floor construction) to be **two distinct root causes, not one** (a
structural bias vs. a correlated-single-realization variance problem — see
§2 there), and combined the five critiques into 8 numbered mandatory fixes.

**Director's disposition: all 8 mandatory fixes ADOPTED IN FULL, zero
further overrides beyond Red Team's own one partial override** (MATERIALS'
own remedy option (b) — "add a genuine R14(a) numerator-smoothness check"
— declined as unachievable on physically multi-lobed diffraction-pattern
curves; MATERIALS' own alternative option (a) — "drop the R14-discharge
claim" — adopted instead, per Red Team §1.4/§6 Fix 3).

| # | Fix | Disposition |
|---|---|---|
| 1 | Pool the mirror-floor statistic (median, within-margin, over the 24 bin-pairs) rather than a single per-bin/per-margin point estimate — closes QUANTUM's correlated-realization attack, zero new FDTD | **Implemented**: `run.py::mirror_pooled_floor()` |
| 2 | Disclose the mirror floor's structural blindness to common-mode/even noise (PHOTONICS' attack, unclosed by pooling); split the queued Iteration-88 fault-injection control into asymmetric (planned) + symmetric/common-mode (new) sub-items | **Disclosed** in `DISCLAIMER`; **queued** as Iteration-88 items (a)/(b), below |
| 3 | Correct "discharges R13 and R14" → "discharges R13 only" | **Implemented**: `classify_item_i_local()`'s own docstring, this NOTES.md |
| 4 | Add discretization-noise-vs-fabrication-tolerance disclaimer | **Implemented** in `DISCLAIMER` |
| 5 | Wire `COST_GATE_PILOT_S`/`COST_GATE_TOTAL_S` as executable code (R27, new standing rule — see below), not a prose promise | **Implemented**: `run.py::cost_gate_check()`, called from `analyze.py` |
| 6 | Use `build_result_text()`'s `wall_time_source` to distinguish this cycle's genuinely new wall time from exp-108's historical 7712.0s | **Implemented**: `chunk_runner.py`'s own per-(r,which) wall-time log, summed and reported explicitly, distinct from exp-108's own figure |
| 7 | Bind Phase 3/4 to `build_predictions_text()`/`build_result_text()`, assert `DISCLAIMER in` both, persist both, NOTES.md quotes `result_text` verbatim (R23) | **Implemented** — see Predictions below (verbatim quote) and Result (after Phase 4) |
| 8 | State bin counts clearing/failing the K=3 floor gate, and the two PHOTONICS-named bins' disposition, in Result prose, not only `results.json` | **Committed to** — reported in Result, below, after Phase 4 |

## New standing rule — R27 (proposed by this cycle's own synthesis, per
## Red Team's Phase-2 audit §4's own explicit invitation to the Director)

**R27 — a numeric cost, safety, or scope gate (e.g. `COST_GATE_*`) defined
as a module-level constant, and referenced only in prose/docstring/
Idealizations language, is not a gate at all until it is enforced by
executable code that actually branches on it and records the outcome (not
a ruled-out idea; a standing house-discipline rule, proposed by this
cycle's own Phase-3 synthesis on THERMODYNAMICS' Phase-2 finding, Red
Team's Phase-2 audit §1.5/§4/§6 Fix 5).** Founding instance: exp-105
through exp-108 (four-plus cycles) each reused `COST_GATE_PILOT_S`/
`COST_GATE_TOTAL_S`, invoked only in prose ("abort r=312 leg if projected
exceeds this," "commit r=312 only if pilot wall time <90 min") — `grep -rn
"COST_GATE"` across exp-108's own directory finds only the two definitions
and zero enforcing branches anywhere in `chunk_runner.py` or `analyze.py`.
Checked element-by-element against R23/R24/R25's own operative text by
Red Team's Phase-2 audit (§4): none of the three literally fires (R23 is
scoped to repeated disclaimer strings; R24 requires a specific Phase-2
"adopted in full" claim about the gate's own enforcement, which never
existed; R25 requires a prior audit naming-then-dropping the fix, and
THERMODYNAMICS is the first seat ever to name this gap). A genuinely new
failure shape, not a recurrence of any named one. **Does not fire on its
own founding instance**, matching every prior rule in this registry.
**Rule, forward: a future cycle that reuses a documented numeric gate a
second time without executable enforcement, after this rule is on the
books, fires Checkpoint criterion 4 automatically** — a single-instance-
ratified, forward-firing model, matching R16/R21/R22/R23/R24/R25/R26's own
precedent. This cycle's own founding instance is fixed same-shift (Fix 5,
`run.py::cost_gate_check()`).

## T1 escape route: N/A

Confirmed structurally, independent of any layer's own claim (Red Team
§0): item 1 touches only angular-pattern floor-gating arithmetic (no
σ(I)/σ(x,t)/angular-selectivity/sub-threshold content is possible in a
symmetry-based noise floor); item 2 touches a pure numpy curve-fit
diagnostic; item 3 touches a checkpoint/resume identity gate on a fixed
empty-scene bench. No constraint-1/2/3/4 verdict is scored or moved
anywhere in this document.

## Setup

- `run.py` — shared geometry (`geom_fixedabs`, byte-for-byte reused from
  exp-106/108), `gate_p0`/`reproduction_precondition`/
  `reproduction_precondition_108` (HALT-before-trust checks),
  `linear_fit_1_over_margin`/`classify_item_i`/`classify_item_ii` (byte-
  for-byte reused, unchanged, item i/ii's own frozen classifiers),
  `mirror_pooled_floor`/`classify_item_i_local` (item 1's new,
  informational-only diagnostic, Fix 1/3 applied), `cost_gate_check`
  (R27's own founding fix), `DISCLAIMER`/`build_predictions_text`/
  `build_result_text` (R23, Fixes 2/4/6/7 folded into `DISCLAIMER`).
- `chunk_runner.py` — item 1a's own re-capture driver, byte-for-byte
  exp-108's own geometry/scene construction, foreground Bash calls only
  (exp-107's own diagnosed backgrounding-slowness finding, reused without
  re-testing). Environment-path correction, disclosed, non-substantive:
  `SCRATCH` repointed to this session's own scratchpad (exp-108's own
  hardcoded path is the defunct one this cycle exists to stop relying on).
  Adds a per-(r,which) wall-time log (Fix 6).
- `analyze.py` — item 1a/1b/1c/1d's own analysis: loads the 6 captures,
  runs `gate_p0`/both reproduction preconditions, persists the full
  48-bin/6-margin peccored/hollow/delta arrays (item 1b), runs
  `classify_item_i_local` per margin, applies the R27 cost gate after the
  r=156 pilot before attempting r=312.
- `linear_fit_control.py` — item 2's own fault-injection control, four
  deterministic synthetic sequences, zero `Sim.run()` calls.
- `lab/validation/run_all.py::stage26_chunked_run_identity` — patched in
  place (disclosed `lab/` diff, no engine-physics change) to add item 3's
  own symmetric truncation-direction negative control (Gate 3). Verified
  green pre-freeze: `python3 lab/validation/run_all.py --only 26` → 3/3;
  full standard suite `--only 12346789` → 41/41 (80s).

## Idealizations

- Item 1's mirror floor is a NEW, first-use instrument. Per R25's own
  discipline, its own fault-injection control is named as its own
  explicit, numbered Iteration-88 queue item (not a parenthetical): (a) an
  injected ASYMMETRIC synthetic perturbation, confirming the floor
  correctly flags it; (b) an injected SYMMETRIC/common-mode synthetic
  perturbation, confirming the floor correctly does NOT flag it (Fix 2 —
  this is the genuinely unclosed gap Fix 1's pooling cannot reach).
- `K=3` and `percentile=50` (median) are disclosed house-style choices,
  not derived from a resolution/aliasing bound — `local_snr` is reported
  for every bin regardless, so a future reviewer can re-threshold without
  a re-run.
- Item 1's local diagnostic is explicitly INFORMATIONAL — it does not
  replace, gate, or reclassify `classify_item_i`'s own existing (Phase-5-
  corrected, dominant-lobe-scoped) CONFIRM verdict. Keeping it un-scored
  is deliberate: folding a brand-new instrument straight into a frozen
  verdict the same cycle it is built is the exact shape R24 exists to
  catch.
- Item 1's mirror floor characterizes grid-discretization/floating-point
  noise for the IDEALIZED simulated geometry only — Fix 4, folded into
  `DISCLAIMER`.
- Item 1's mirror floor is structurally blind to common-mode/even noise —
  Fix 2, folded into `DISCLAIMER`; not closed by Fix 1's pooling.
- Item 1's re-capture is bit-for-bit the same geometry/config exp-108
  already ran — a data-persistence fix, not new physics. The R27 cost gate
  (now code-enforced) still applies; if the r=312 pilot check fails,
  `r312_deferred=True` is written and item 1's r=312 analysis is reported
  NOT-RUN, not silently skipped.
- Item 2 does not re-derive `R2_SMOOTH_THRESHOLD=0.90` itself (already
  queued separately, Iteration-86 Tier 2b) — these controls test whether
  the OR-logic branch selection mechanically fires correctly at the
  EXISTING threshold, not whether 0.90 is the right number.
- Item 3's patch is a disclosed `lab/` diff (extending `stage26`, no
  engine-physics change) — trust suite confirmed green (41/41) both before
  and after, per the standing discipline for every `lab/`-touching cycle.
- Tier-0 item 0 (the Iteration-85 Checkpoint-4/R24 ruling) is explicitly
  not attempted — Marsh's call, out of scope for a Panel proposal.
- Every other queue item (Tier 2/3: `R2_SMOOTH_THRESHOLD` re-derivation, a
  fourth r-point, MATERIALS' fabrication-tolerance framing, the
  oblique-angle/750-450nm/`G40`/x-wall/`PAD` items, `box_dev`'s own
  thinning margin) is out of scope for this cycle, unchanged.

## Predictions (committed to git BEFORE this file's first real `Sim.run()`
## call, house discipline, non-negotiable)

```
PREDICTIONS (pre-registered, exp-110, Panel Iteration 87)

Raw physical angular-scattering-pattern and absorbed-power/ extinction ratios only -- no Weber-contrast or C_thr(L) perceptual scoring is performed this cycle; not a claim about human visibility. angular_scattered_pattern() is a square-path near-to-mid-field angular sample, not a true circular far-field pattern (function's own docstring). The absolute-floor six-margin family and item 1's own mirror-symmetry floor are both new conventions this cycle, not independently re-derived from a resolution or aliasing bound. Item 1's mirror floor characterizes grid-discretization/floating-point noise for the IDEALIZED simulated geometry ONLY -- a bin clearing it licenses NO inference about a physically realized coated disk's own achievable angular-pattern symmetry (real deposition/machining tolerances sit orders of magnitude above this floor's ~1e-9-1e-4 scale). Item 1's mirror floor is structurally BLIND to common-mode/even noise (a bias, not variance -- any bias identical at bin i and its mirror bin cancels exactly in the differencing construction, at any sample size, unclosed by pooling) -- a RESOLVED bin under this gate is cleared only against the ODD/antisymmetric noise component, not validated clean of common-mode contamination. Item 1's diagnostic is INFORMATIONAL ONLY and does not replace, gate, or reclassify item i's own existing frozen CONFIRM verdict.

**Item 1a** (re-capture fidelity): gate_p0 PASS exact, both r. reproduction_
precondition PASS, sigma_abs/sigma_ext/abs_ext_ratio matching exp-108's own
committed results.json to <1e-9 relative at both r (r=156:
sigma_abs=279.6607, sigma_ext=560.1989; r=312: sigma_abs=588.0218,
sigma_ext=1191.3259). Falsified by ANY deviation exceeding that bound.

**Item 1b** (persistence): len(results.json["item_i"]["raw_patterns"][m]
["peccored"]) == 48 for all 6 margins, both r actually captured (r=312
conditional on the cost gate below). Falsified by any missing combination.

**Item 1c/1d** (mirror pooled floor -- genuinely uncertain, the open
question this instrument exists to answer): I predict at least SOME of
the low-power bins PHOTONICS' own Iteration-85 self-review found (<1% of
peak power, 30/48 bins both r) will fail the K=3 pooled floor gate
(UNRESOLVED-BY-CONSTRUCTION). Falsified if ALL 48 bins clear K=3
comfortably (local_snr>10 everywhere) at both r captured. No advance
position taken on the two specific bins PHOTONICS named (-146.25 deg at
r=156, +168.75 deg at r=312) -- RESOLVED-with-genuine-structure or
UNRESOLVED-by-construction, whichever the run produces.

**Item 2**: all four synthetic (is_monotonic, r_squared, smooth) triples
reproduce bit-exact (deterministic numpy arithmetic on closed-form
sequences, independently re-verified already by QUANTUM and VISION's own
Phase-2 critiques by direct invocation of the real committed function):
P1=(True, 1.0, True); P2=(True, 0.397, True); P3=(False, 0.912, True);
N1=(False, 0.097, False).

**Item 3**: rel_diff_truncated > 0.01 (the gate's own minimum
discrimination bar), predicted in (0.01, 10], same order of magnitude as
the existing over-run control's own 2.0 (200%) figure. Falsified only if
rel_diff_truncated <= 0.01.

**Cost gate (R27, wired as code this cycle)**: pilot_empty_wall_s for
r=156 predicted well under 5400s (90 min) based on exp-108's own recorded
combined 128.5 min/6-call wall time (r=156 is the cheaper leg, k=2 vs
k=4). If the pilot clears, r=312 is attempted; if not, r312_deferred=True
is written and item 1's r=312 analysis is reported NOT-RUN, not silently
skipped.
```

(Pre-registered independently already, item 3: `--only 26` re-run above
already shows `rel_diff_truncated=1.999`, inside the predicted (0.01,10]
band — falsification check for item 3 PASSES pre-freeze, disclosed here
rather than hidden, since the stage26 patch had to be smoke-tested against
the live trust suite before this document could honestly claim "trust
suite green" in Setup, above. Items 1a/1b/1c/1d/2 are NOT yet run as of
this commit — Phase 4 begins after this document lands in git.)

## Result

**Every predicted outcome held — nothing falsified.** `finalize.py`
asserted `DISCLAIMER in` both `predictions_text` and `result_text` (both
passed) and persisted both into `results.json` (Fix 7). Trust suite
confirmed green after Phase 4: `--only 12346789` → 41/41 (77s).

```
RESULT (exp-110, Panel Iteration 87)

Raw physical angular-scattering-pattern and absorbed-power/ extinction ratios only -- no Weber-contrast or C_thr(L) perceptual scoring is performed this cycle; not a claim about human visibility. angular_scattered_pattern() is a square-path near-to-mid-field angular sample, not a true circular far-field pattern (function's own docstring). The absolute-floor six-margin family and item 1's own mirror-symmetry floor are both new conventions this cycle, not independently re-derived from a resolution or aliasing bound. Item 1's mirror floor characterizes grid-discretization/floating-point noise for the IDEALIZED simulated geometry ONLY -- a bin clearing it licenses NO inference about a physically realized coated disk's own achievable angular-pattern symmetry (real deposition/machining tolerances sit orders of magnitude above this floor's ~1e-9-1e-4 scale). Item 1's mirror floor is structurally BLIND to common-mode/even noise (a bias, not variance -- any bias identical at bin i and its mirror bin cancels exactly in the differencing construction, at any sample size, unclosed by pooling) -- a RESOLVED bin under this gate is cleared only against the ODD/antisymmetric noise component, not validated clean of common-mode contamination. Item 1's diagnostic is INFORMATIONAL ONLY and does not replace, gate, or reclassify item i's own existing frozen CONFIRM verdict.

6 real FDTD calls, 7690.4s (128.17 min)
total wall time this cycle, zero `lab/` diff except the disclosed stage26
symmetric-truncation addition (item 3).
(This cycle's own genuinely new wall time: 7690.4s (128.17 min), 6 real FDTD calls -- distinct from exp-108's own historical 7712.0s/6-call figure (a separate, already-committed capture of the identical geometry); per-scene: r156 empty/hollow/peccored = 250.6s/250.1s/251.5s; r312 empty/hollow/peccored = 2334.8s/2233.0s/2370.4s.)

**Gate P0: PASS.**
**Reproduction precondition: PASS.**
**Item 1a (re-capture fidelity):** PASS exact, both r -- reproduction_precondition rel_dev=0.0 exactly at both r (r=156: sigma_abs=279.6607, sigma_ext=560.1989; r=312: sigma_abs=588.0218, sigma_ext=1191.3259 -- matches exp-108's own committed results.json exactly). NOT FALSIFIED.
**Item 1b (persistence):** PASS -- 48/48 bins persisted for all 6 margins, both r. NOT FALSIFIED.
**Item 1c/1d (mirror pooled floor, informational):** NOT FALSIFIED -- some bins fail the K=3 pooled floor gate at both r, as predicted (not 'ALL clear comfortably'). r=156: 203/288 bins RESOLVED (70.5%), 85 UNRESOLVED-BY-CONSTRUCTION (29.5%) across all 6 margins. r=312: 222/288 RESOLVED (77.1%), 66 UNRESOLVED (22.9%). The two PHOTONICS-named bins (margin=32): r=156 bin at -146.25 deg is UNRESOLVED-BY-CONSTRUCTION; r=312 bin at 168.75 deg is UNRESOLVED-BY-CONSTRUCTION. Neither named bin's ~10% local-normalized reading from exp-108's own Phase-5 review clears the K=3 mirror-pooled floor at this cycle's own default (K=3, median, within-margin) -- their earlier local-deviation readings are NOT validated as genuine shape structure by this instrument; they are exactly the shape of reading this floor gate exists to catch (near-null relative-error territory), though PHOTONICS' own unclosed common-mode-blindness concern (Idealizations) means this instrument cannot rule out a real but common-mode-masked effect at either bin.
**Item 2 (linear_fit_1_over_margin control):** PASS -- all four predicted (is_monotonic, r_squared, smooth) triples reproduced bit-exact: P1=(True, 1.000, True); P2=(True, 0.397, True); P3=(False, 0.912, True); N1=(False, 0.097, False). All four fault-injection assertions passed (python3 linear_fit_control.py). NOT FALSIFIED.
**Item 3 (stage26 truncation control):** PASS -- rel_diff_truncated=1.999 (lab/validation/run_all.py --only 26: 3/3), inside the predicted (0.01,10] band, same order of magnitude as the existing over-run control's own 2.0. NOT FALSIFIED.
```

**Interpretation.** Item 1a/1b/2/3 are clean, unsurprising confirmations of
already-established machinery (a bit-identical re-capture, a fault-
injection control validating logic that was already believed correct, a
symmetric extension of an existing gate). **Item 1c/1d is the genuinely
new finding**, and it cuts the OTHER way from PHOTONICS' own Iteration-85
speculation: neither of the two specific bins PHOTONICS named as carrying
a real ~10% local-normalized deviation clears this cycle's own K=3
mirror-pooled floor — both read as `UNRESOLVED-BY-CONSTRUCTION`, i.e. this
instrument cannot distinguish their ~10% reading from pure grid-
discretization noise at the K=3 threshold. This does **not** prove the
deviation is noise (Fix 2's own disclosed common-mode blindness means a
real, mirror-symmetric structural effect at exactly those bins would look
identical to this floor gate) — but it does mean PHOTONICS' own "real
shape structure" reading is **not corroborated** by the one instrument
built this cycle to test it, and the honest disposition is genuinely
open, not resolved either direction. ~23–30% of all sampled bins
(85/288 at r=156, 66/288 at r=312) sit below the K=3 floor entirely —
informationally relevant for any FUTURE cycle that might consider scoring
`classify_item_i_local`'s output, but this cycle's own item i CONFIRM
verdict is untouched (informational only, per Fix 2's reasoning).

**Combined Verdict: PROMISING** — a clean governance/instrumentation
cycle: T1 correctly N/A throughout (confirmed structurally, not merely
asserted); every one of the eight Phase-2-mandated fixes genuinely
implemented and verified, not merely claimed; R23 fully honored (both
DISCLAIMER asserts live-fired, both text fields persisted, quoted
verbatim above); the data-persistence gap that made the Iteration-86
queue's own premise false is closed for good (item 1b); a new, real,
disclosed finding (item 1c/1d) that appropriately narrows rather than
resolves a two-cycle-old open question, exactly as an informational
diagnostic should. Zero Checkpoint criteria fire pending Phase 5's own
independent review (see below).
