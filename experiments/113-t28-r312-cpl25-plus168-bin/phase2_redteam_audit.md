# Phase 2 Red Team Audit — exp-113 (Panel Iteration 90)

**Fresh sub-agent, full-visibility seat.** Read `PANEL.md` in full; `LOGBOOK.md`'s
full RULED OUT registry (R1–R31, R28–R31 read closely), the T28 live-thread
opening (`sed -n '3094,3200p'`), and the full Iteration-89 entry
(`sed -n '24215,24415p'`). Read `phase1_proposal.md`, `run113.py`,
`chunk_runner113.py`, `analyze113.py`, and all five Phase-2 critiques in full.
Unlike the five blind seats, I see everything, including their outputs — and I
did not take a single number from any of them on faith. Every figure below was
independently recomputed this session directly from `run113.py`/`run112.py`/
`run.py` primitives and the committed `experiments/110-.../results.json` /
`experiments/112-.../results.json` arrays (Python one-liners, shown inline
where load-bearing), never from a document's own prose. **No `Sim.run()` call
was made anywhere in this audit** — Phase 4 has not started, and nothing below
required it; every claim under review is either zero-FDTD geometry/arithmetic
or a claim about already-committed `results.json` data from exp-110/exp-112.

**T1/constraint-3 status, stated up front**: N/A throughout, confirmed
independently. Nothing in `run113.py`/`chunk_runner113.py`/`analyze113.py`
proposes, varies, or scores σ(I)/σ(x,t)/angular-selectivity/sub-threshold
content, or any constraint-1/2/3/4 claim. This is instrument-fidelity/
resolution-convergence work, matching every T28 desk/instrument cycle since
Iteration 46. Every attack below is tagged accordingly — none is a
constraint-#N violation.

---

## 1. Independent re-derivation of each of the five findings

### 1.1 PHOTONICS — box_a near-field-depth confound

**Independently reproduced, exactly.** Direct computation:

```
geom_fixedabs_cpl(156,25): R_COAT=195, box_a_hw=275 -> clearance=80 cells / cpl=25 = 3.2λ
geom_fixedabs_cpl(312,25): R_COAT=390, box_a_hw=550 -> clearance=160 cells / cpl=25 = 6.4λ
```
(traced to `box_a_hw = R_COAT + round(BOX_A_MARGIN0 * k * ratio)`, `run112.py`
line 122 — `BOX_A_MARGIN0=32` cells at cpl=20/r=156 baseline, and
`kappa_of(156)=2.0` since `R_BASE=78`, not 1 — a detail neither the proposal
nor the critique states but which I traced to confirm the arithmetic is
genuinely `kappa_ratio`-driven, not coincidental.) **CONFIRMED, verbatim.**
This is real: the same *proportional* margin (32 cells at cpl=20, scaled) sits
at a physically different near-field depth at the two radii, independent of
the `cpl=20→25` refinement. PHOTONICS is correct that this does not break
this leg's own internal falsifiability (each check scores against its own
r's own cpl=20 baseline) — but it is a genuine, previously undisclosed
confound sitting directly under the document's own "mirror companion"
framing (§1, §7 of `phase1_proposal.md`), which invites exactly the cross-leg
reading this finding says is not licensed.

### 1.2 MATERIALS — `_SPONGE_MARGIN_ORDERS` wrong comparator

**Independently reproduced, exactly.** From `run113.py`'s own live constants:

```
BASELINE_FLOOR    = 3.3825903e-4
BASELINE_PECCORED = 8.740493e-5
BASELINE_HOLLOW   = 9.691509e-5
BASELINE_DELTA    = -9.510156e-6
_SPONGE_ABS_VAL   = 3.248924e-8   (=exp(-17.242357))

log10(floor / sponge)      = 4.0175  (the code's own figure, "~4.02")
log10(peccored / sponge)   = 3.4298  ("~3.43")
log10(hollow / sponge)     = 3.4747
log10(|delta| / sponge)    = 2.4664  ("~2.47")
```
All four numbers match MATERIALS' critique to 3–4 significant figures.
**CONFIRMED, exactly.** `_SPONGE_MARGIN_ORDERS` is computed against
`BASELINE_FLOOR` — the instrument's own K=1 noise-floor scale (correctly the
denominator for `local_snr`, elsewhere in the same file) — not against the
named bin's own signal magnitude (peccored/hollow) or, more importantly, the
actual quantity Check B scores (`|delta|`). The disclosed "~4.02 orders,
non-fatal" figure is real arithmetic on the wrong operand for what the
DISCLAIMER string claims to bound ("the sponge... below it" — "it" reads as
the signal, not the floor). MATERIALS' own recomputation is right, and the
gap between "~4.0" and "~2.47" is large enough (over 1.5 orders) to matter for
a document whose own stated purpose this cycle is disclosure completeness.

### 1.3 ELECTROMAGNETISM — R28 upstream / sigma_ext_cross / PEC-zeroing cost asymmetry

**All three sub-claims independently reproduced.**
- R28 positioning: `chunk_runner113.py`'s `__main__` (lines 208–214) calls
  `check_cost_gate_for_r312(cpl_arg)` unconditionally before
  `step_budgeted(...)` on **every** r=312 CLI invocation (fresh-start or
  resumed) — confirmed by direct reading, no ambiguity. **CONFIRMED.**
- `sigma_ext_cross`: confirmed present in `lab/sections.py::widths()`
  (`"sigma_ext_cross": p_ext_cross / i_inc`, line 151) and persisted for both
  peccored and hollow in `analyze113.py`'s `energy_ledger` (lines 86–90) — a
  real fix, not merely disclosed. **CONFIRMED.**
- PEC-zeroing cost: `lab/fdtd2d.py::Sim.run()` (lines 253–255) executes
  `self.Ez *= self.damp_e` then, unconditionally, `if self.pec.any():
  self.Ez[self.pec] = 0.0` every step. `self.pec` is all-`False` by
  construction for `empty`/`hollow` (neither calls `materials.pec_disk`), so
  `.any()` is `False` and the masked write never executes for those two
  scenes; `peccored` alone pays it. Independently op-counting the non-`aniso`
  branch: 4 full-array ops for the H-update (`Hx-=`, `Hy+=`, `Hx*=damp`,
  `Hy*=damp`), 1 for the Ez update, 1 for `Ez*=damp_e`, 1 reduction for
  `.any()` — **7 baseline full-grid touches**, matching EM's own count
  exactly — plus, for `peccored` only, the masked assignment. `1/7 ≈ 14.3%`
  reproduces EM's cited "~14%" as a legitimate back-of-envelope op-count
  estimate, **not** a profiled/measured figure (none exists — no timing data
  can exist before Phase 4). **CONFIRMED as a real, correctly-signed
  asymmetry; the specific "~14%" is a reasonable estimate, explicitly not
  yet a measurement** — this distinction should be stated in the fix, not
  left implying a benchmarked number.
  Consequence, independently re-derived: `HISTORICAL_PER_STEP_S` averages all
  three scenes (`.../(3*STEPS)`), which blends 2 cheap + 1 costlier-by-~14%
  scene into one figure standing in for "empty" in `r31_control_ratio`
  — `(2 + 1.14)/3 ≈ 1.047×` inflation versus a true empty-only rate, matching
  EM's own "~5%" estimate. Tracing the sign through
  `speed_ratio = HISTORICAL_PER_STEP_S / this_session_per_step_s` (inflated
  numerator) → `scaled = pilot / speed_ratio` (deflated) →
  `projected_312_total_s` deflated — **anti-conservative, confirmed
  direction**, stacking with R28's own already-disclosed ~15% kappa-exponent
  miss in the same direction (both push toward false approval).

### 1.4 THERMODYNAMICS — R31 arithmetic direction / control representativeness

**Both sub-claims independently reproduced.** Direct execution of the real
committed functions (`run113.py::r31_control_ratio`,
`cost_gate_check_r31`), a session 2× slower than historical
(`this_session_per_step_s=0.055873`, `speed_ratio=0.5`):
```
scaled_total = 670.4778 / 0.5 = 1340.956s
projected_312_total_s (scaled) = 13605.28s > 10800s -> proceed_to_r312=False (REFUSES)
```
Matches THERMODYNAMICS' hand-check (their `≈13,607s`) to within rounding —
**CONFIRMED, the formula's direction is correct in both directions** (I also
re-ran the real, unscaled/raw case, reproducing `6802.64s`/`proceed=True`
bit-exact to the Director's briefed figure). The representativeness gap is a
sound, if not directly execution-testable pre-Phase-4, engineering argument:
`r=156`'s grid is `N=1400×1400`; `r=312`'s is `N=2800×2800` — a **4× larger**
array (confirmed by direct computation, matching THERMODYNAMICS' own "4×"
claim), and a 1000-step/~10–60s burst on the small grid cannot see
sustained-load effects (turbo-boost clock decay, cache/memory-bandwidth
saturation once working-set exceeds cache at the larger size) that a
multi-hour, 4×-larger production job would experience. **CONFIRMED as a real,
plausible, correctly-characterized gap** — same anti-conservative direction
as EM's finding (a short/light-load control reads faster than sustained
large-grid reality), stacking rather than cancelling.

### 1.5 QUANTUM OPTICS — Check C direction validity (the consequential one)

**Every cited number independently reproduced, bit-close.** Recomputing
`windowed_corr` over all 48 bins from `experiments/110-.../results.json`
(`r156/raw_patterns/32/delta`, cpl=20) against
`experiments/112-.../results.json['pattern_delta']` (real cpl=25 data), split
by `experiments/112-.../results.json['local_diag_margin32']['resolved']`:

```
resolved (n=34):   mean corr = 0.979296   range [0.816857, 0.999623]
unresolved (n=14):  mean corr = 0.992078   range [0.968881, 0.999502]
```
Matches QUANTUM's `0.9793`/`0.9921` exactly. The 8 lowest-correlation bins
overall: indices `[35,12,40,7,36,11,41,6]`, with **6 of 8 in the "resolved"
population** — indices `35,12,40,7,36,11` — whose baseline (cpl=20) SNR
values I independently pulled from `results.json['r156']['local_diag']['32']`
are `126.891, 130.464, 1.332, 1.351, 70.369, 67.679` — an **exact match** to
QUANTUM's cited `126.9, 130.5, 1.33, 1.35, 70.4, 67.7`, and indeed non-
monotonic with correlation (SNR ranges over two orders of magnitude among
these six with no correlation ordering). The named r=156 bin's own
correlation (`0.999358`) sits at the **89.58th percentile** of its own
48-window null — I recompute this directly and get the same figure QUANTUM
cites (89.6th). **Every empirical claim CONFIRMED, exactly.**

The deeper point, independently traced through the actual code history, goes
further than "the gap is thin": I read exp-112's own founding
`neighbor_correlation_check` docstring (`run112.py` lines 208–221) — its
literal, original premise is **"a genuine deterministic sub-wavelength field
feature should imprint spatially CORRELATED structure... unlike uncorrelated
Yee-grid discretization noise, which need not correlate bin-to-bin under a
resolution change"** — i.e. the ORIGINAL mechanistic claim is **HIGH
correlation across cpl = real structure**, matching QUANTUM's characterization
exactly and matching PHOTONICS' own original Iteration-89 framing. R30 (the
Iteration-89 finding) established that the fixed `corr>=0.5` BAR built on
that premise was uninformative (48/48 bins cleared it) — it did **not**
establish that the premise's DIRECTION was wrong, only that its calibrated
THRESHOLD was too loose to discriminate anything. `run113.py`'s own new
code (`classify_resolution_check`, lines 268–272) then silently **inverts**
that premise — `supports_real_structure = percentile_in_null <= 10.0`,
i.e. LOW correlation now counts as diagnostic — justified only by a new,
post-hoc comment ("LOW correlation = LESS like the generic pattern-wide
behavior = more consistent with a bin-specific feature") that was never part
of the original design, was constructed using the SAME r=156 dataset whose
own miscalibration motivated R30 in the first place, and is then applied,
unvalidated, to a **different geometry (r=312)** this cycle actually tests.
This is a real, load-bearing internal inconsistency: the code's own
comment directly contradicts the function it descends from (`run112.py`'s
own docstring) on which tail of the distribution means "real," and nothing
in this cycle's own committed code checks which one is actually true at the
geometry under test. **CONFIRMED and, if anything, understated by treating
it only as "thin/non-monotonic"** — it is a genuine direction flip, argued
from the very data that invalidated the instrument's prior calibration, not
merely an under-powered confirmation.

**My own direction ruling** (per the task's explicit request): Phase 4 should
proceed with neither the current low-percentile direction nor its opposite
asserted as evidentiary — it should ship this cycle as an **explicitly
UNDIRECTED, disclosed-only percentile reading**. Reasoning: (a) the
resolved/unresolved gap that motivates the current direction is thin (1.3
percentage points), non-monotonic with SNR, and plausibly explained by
proximity to the shared smooth diffraction envelope's zero-crossings/
inflections (a resolution-*sampling* artifact, orthogonal to "realness") —
QUANTUM's own alternative explanation, which I find at least as consistent
with the data as the "realness" story, and neither has been ruled out; (b)
the ORIGINAL premise (high-corr=real) and the CURRENT code (low-corr=real)
cannot both be right, and no mechanistic argument in this document
independently derives which one is — only an untested inference drawn from
one confounded dataset; (c) R30's own text ("checked against its own
already-computable null/background population... before its reading is cited
with evidentiary language") licenses exactly the fix QUANTUM names: compute
the SAME resolved-vs-unresolved cross-tabulation on r=312's own real cpl=25
data (zero marginal cost, arrays already computed by `analyze113.py`) and
let THAT determine, at the actual geometry under test, whether either
direction is even locally supported before any Phase-5 prose calls the
named bin's reading "candidate real structure" in either direction.

---

## 2. MANDATORY-FIX docket

All fixes below are applied by the Director at Phase 3, before any
`Sim.run()` call. None requires new FDTD data to implement.

**Fix 1 [PHOTONICS — inconsistency]**: Add an Idealization item to
`run113.py`'s `DISCLAIMER` (computed via `box_a_hw - R_COAT`, divided by
`cpl`, at both r — not hand-typed) stating the box_a clearance in
wavelengths at both radii (3.2λ at r=156, 6.4λ at r=312 — exactly
`kappa_ratio=2.0`, independent of cpl) and explicitly cautioning that Phase 5
must not read this leg's outcome and exp-112's `−146.25°` outcome as
testing the same physical near-field depth "companion" question — only the
same *proportional* margin at two different physical depths. Non-blocking
for Phase 4's own spend (each check is self-referential to its own r); blocks
Phase 5 cross-leg interpretation only.

**Fix 2 [MATERIALS — inconsistency]**: Change `run113.py`'s sponge-margin
computation and DISCLAIMER text to report and label THREE figures, not one:
`_SPONGE_MARGIN_ORDERS_FLOOR` (`log10(BASELINE_FLOOR/_SPONGE_ABS_VAL)` ≈4.02,
labeled explicitly as "relative to the instrument's own K=1 noise-floor
scale"), `_SPONGE_MARGIN_ORDERS_SIGNAL` (`log10(min(|peccored|,|hollow|)/
_SPONGE_ABS_VAL)` ≈3.43, labeled "relative to the named bin's own signal
magnitude"), and `_SPONGE_MARGIN_ORDERS_DELTA` (`log10(|BASELINE_DELTA|/
_SPONGE_ABS_VAL)` ≈2.47, labeled "relative to |delta|, the quantity Check B
actually scores"). Must land before Phase 3 freezes the R23-asserted
DISCLAIMER string permanently.

**Fix 3 [ELECTROMAGNETISM — inconsistency]**: (a) Correct Idealization 2's
false claim that FDTD per-step cost is "materials-invariant... regardless of
contents" — replace with the true, signed statement: `peccored` scenes pay a
real extra per-step cost from `Sim.run()`'s `self.Ez[self.pec]=0.0` masked
write (absent for `empty`/`hollow`), independently op-counted at ≈1 extra op
on ≈7 baseline full-grid ops (≈14%), explicitly labeled an *estimate*, not a
profiled measurement. (b) Change `chunk_runner113.py::run_control()` to
re-time the same 3-scene mix `HISTORICAL_PER_STEP_S` was built from (or,
per EM's own proposed fix, re-time the `peccored` scene specifically instead
of `empty`) so the same-session control and the cross-session historical
figure are commensurable at the same per-scene mix — removing the ≈5%
anti-conservative inflation of `speed_ratio` at its source rather than
patching it with a disclosure sentence. Must land before Phase 4 trusts
`proceed_to_r312`.

**Fix 4 [THERMODYNAMICS — inconsistency]**: Require `chunk_runner113.py`'s
`--control` mode to take a second, sustained reading (e.g.
`control_steps=10000`, comparable duration to a real r=312 production
sub-chunk) in addition to the current 1000-step burst, and have
`check_cost_gate_for_r312` gate on the LOWER (more conservative) of the two
resulting `speed_ratio` values, raising if they disagree by more than a
small pre-registered tolerance (e.g. 10%). Must land before Phase 4 trusts
`proceed_to_r312` — this is a control-INPUT-quality gap in the same family
as R28's gate-POSITION gap, and stacks with Fix 3 in the same anti-
conservative direction.

**Fix 5 [QUANTUM OPTICS — inconsistency, most consequential]**: (a) In
`run113.py::classify_resolution_check`, replace the single directional
`check_c["supports_real_structure"] = percentile_in_null <= 10.0` with two
symmetric, undirected fields — `low_percentile_outlier` (`<=10.0`) and
`high_percentile_outlier` (`>=90.0`) — and remove any Check-A branch text
that upgrades a reading to "candidate real structure" on either tail alone.
(b) Add to `analyze113.py`, once r=312's own real cpl=25 data lands, the
resolved-vs-unresolved (or SNR-quartile, if `resolved` is degenerate at
r=312) windowed-correlation cross-tabulation over all 48 of THIS geometry's
own bins (a few lines over `local_diag["resolved"]` and
`check_c["null_scan"]["all_window_corrs"]`, both already computed, zero
marginal FDTD cost) and persist it in `results.json`. (c) Until that
cross-tabulation is computed AND shows the SAME direction independently at
r=312 (not merely disclosed as untested), any Phase-5 Interpretation
language must report the named bin's percentile as an **undirected,
disclosed-only reading** — neither tail asserted as "supports real
structure." Must land before Phase 3 freezes any Check-C-referencing
DISCLAIMER text, and before any Phase-5 seat is handed this cycle's results.

**None of the five rises only to a disclosed override** — all five are cheap
(no new FDTD), concrete, and code/doc-expressible; I decline to soften any
of them. If forced to rank stakes: Fix 5 > Fix 3/4 (both gate real spend
decisions and stack anti-conservatively) > Fix 2 > Fix 1 (cheapest, purely
descriptive, does not change any check's own arithmetic).

---

## 3. Verdict

**PROCEED-WITH-MANDATORY-FIXES.**

Numbered attacks (tags per the required scheme; T1/constraint-3 correctly
N/A throughout this entire thread — no attack below is a constraint-#N
violation):

1. [inconsistency] The "companion bin" framing (§1/§7, `phase1_proposal.md`)
   omits a real, independently-confirmed near-field-depth confound (3.2λ vs
   6.4λ) — Fix 1.
2. [inconsistency] `_SPONGE_MARGIN_ORDERS`, as coded, compares sponge leakage
   to the wrong of three available quantities for a disclosure-purpose
   figure — Fix 2.
3. [inconsistency] Idealization 2 asserts a false engine-invariance property,
   independently refuted by direct inspection of `Sim.run()` — Fix 3(a).
4. [inconsistency] `HISTORICAL_PER_STEP_S`'s 3-scene blend is not
   commensurable with `run_control()`'s empty-only re-timing, biasing the
   R31-mandated `speed_ratio` anti-conservatively — Fix 3(b).
5. [inconsistency] R31's own control point is unrepresentative of the
   sustained, 4×-larger workload it calibrates — a control-input-quality gap
   R31's own text does not (yet) require closed — Fix 4.
6. [inconsistency] `classify_resolution_check`'s Check-C direction
   (`percentile<=10.0` ⇒ "real") directly contradicts the ORIGINAL, still-
   live `neighbor_correlation_check` docstring premise it descends from
   (high-corr ⇒ "real"), adopted post-hoc from the same dataset that
   invalidated the prior calibration, never independently validated at the
   new geometry this cycle tests — Fix 5. This is the one finding I would
   also flag as **borderline unfalsifiable as currently coded**: with no
   cross-tabulation gate, a future reader could cite either direction as
   "the check's own premise" and neither could be shown wrong from this
   document alone.

## 4. New standing rule proposed — R32

**R32 — a freshly-adopted or freshly-recalibrated discriminating statistic's
DIRECTION (which tail of its distribution counts as diagnostic) must be
independently validated — via a mechanistic argument stated before the
recalibrating data is seen, or a resolved/unresolved (or equivalently
labeled) cross-tabulation computed on the SAME geometry/scale the statistic
is about to be applied to — before its reading is scored or cited
evidentially in either direction (not a ruled-out idea; a standing
house-discipline rule, proposed by Red Team's Phase-2 audit, Iteration 90,
extending R30 one level deeper).** Distinguished from R30: R30 requires an
uncalibrated THRESHOLD to be checked against its own null population before
it is cited evidentially; it says nothing about which TAIL of that
population should count as signal once the threshold is recalibrated. R30's
own founding instance (exp-112) left this open, and exp-113 is the first
cycle to actually recalibrate a threshold — and, in doing so, silently
inverted the statistic's own founding premise (`neighbor_correlation_check`'s
original docstring: HIGH correlation across `cpl` indicates real structure;
`classify_resolution_check`'s new code: LOW correlation indicates real
structure) using the identical r=156 dataset whose own miscalibration
motivated the recalibration, then applied the new, unvalidated direction
unchanged to a different geometry (r=312) never checked against it. Caught
blind, at Phase 2, by QUANTUM's own critique, independently confirmed by
Red Team's own Phase-2 audit — before Phase 3, Phase 4, or any frozen
record, cleaner than every one of R28/R29/R30/R31's own Phase-5-caught
founding instances. **Rule: before any Result or Interpretation section cites
a directional discriminating statistic's reading evidentially, in either
direction, that direction must be validated independently of the data that
motivated its own most recent recalibration, and independently at each new
geometry/scale where the statistic is next applied — a validated direction
at one geometry does not transfer automatically to another.** **Does not
fire on its own founding instance** (exp-113) — caught at Phase 2, before any
freeze, matching every prior rule's own precedent. **Standing forward
clause: a future cycle that ships or evidentially cites a directional
statistic's reading without this validation, on this or any channel, fires
Checkpoint criterion 4 automatically, no further deliberation** — a
single-instance-ratified, forward-firing model, matching R16/R21–R31's own
precedent. Full record: `experiments/113-t28-r312-cpl25-plus168-bin/
phase2_critique_quantum.md`, `phase2_redteam_audit.md` §1.5, §2 Fix 5,
LOGBOOK.md Iteration 90 (pending Director ratification at Phase 3).
