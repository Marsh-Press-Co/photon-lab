# exp-113 — Panel Iteration 90 (candidate)

**Lead seat: VISION SCIENCE (rotation lead, PHOTONICS→MATERIALS→
ELECTROMAGNETISM→THERMODYNAMICS→QUANTUM OPTICS→VISION SCIENCE→repeat;
Iteration 89 led with QUANTUM OPTICS, so Iteration 90 leads here).**
Governance/instrumentation cycle continuing the T28 sub-thread (opened
Iteration 46, exp-069; T1 route N/A throughout its own 44-iteration
history to date). Executes the Reconciled Iteration-90 queue's own Tier-1
items 1–4 (LOGBOOK.md Iteration 89 /
`experiments/112-t28-cpl25-floor-spot-check/phase5_redteam_audit.md` §10):
the `+168.75°` companion bin at r=312/`cpl=25`, R31-gated by a fresh
same-session control, using the SAME three-check instrument, with Check C
recalibrated per R30 and Check B normalized per Item 4's `CPL_RATIO`
finding. Tier-0 items (0a: ruling on the Iteration-85 Checkpoint-4/R24
firing; 0b: ratifying the R23 First Addendum; 0c: ratifying R30/R31) are
Marsh's/a future Director-session's call, out of scope here.

**A note on this seat's own charter fit, stated up front, not buried in
Idealizations**: this is instrument-fidelity/resolution-convergence work
on a grid-discretization noise floor — not a phenomenon-mechanism
proposal. My own charter's numeric-perceptual-threshold duty ("pin
numeric thresholds, with sources, BEFORE any run that scores against
them") does **not bind here** — no Weber-contrast, `C_thr(L)`, luminance-
edge, spectral-sensitivity, adaptation, or temporal-sensitivity claim is
made or scored anywhere in this document, matching exp-108 through
exp-112's own identical framing. I decline to force a vision-science
mechanism angle onto content that is not phenomenon work. What this seat
*does* genuinely own here, and what the remainder of this document
concentrates on: (1) whether this cycle's own `DISCLAIMER`/R23 machinery
actually closes every term a human reader could mis-scope as a
perceptual claim — the established VISION-seat pattern across
exp-107/109/110/111's own critiques — and (2) an independent read of the
falsification bands and idealizations for genuine completeness, the same
standard any seat owes a Phase-1 document.

## 1. Mechanism/execution narrative (≤300 words)

Execute the companion leg the Reconciled Iteration-90 queue names as its
single highest-value item: the **+168.75° bin** (r=312, margin=32/`box_a`,
bin index 46 of 48) — the r=312 mirror companion of exp-112's own
`−146.25°`/r=156 bin, both flagged by PHOTONICS' Iteration-85 self-review
at comparably large local fractional deviations (r=156: 9.88%; r=312, this
bin: **10.88%**, re-derived below) while sitting well below even the K=1
mirror-pooled floor at `cpl=20` (`local_snr_peccored=0.2584`,
`local_snr_hollow=0.2865` — closer to K=1 than exp-112's own r=156 bin
was, but still UNRESOLVED-BY-CONSTRUCTION). The question is identical in
kind to exp-112's own: does this bin's reading reflect genuine
deterministic sub-wavelength field structure the PEC-core/hollow boundary
condition imprints, or is it a fixed-Cartesian-grid artifact at `cpl=20`?

The instrument is the SAME congruent `cpl=20→25` refinement recipe
(`geom_fixedabs_cpl`, reused unmodified from `run112.py`, already
verified byte-exact to `R110.geom_fixedabs` at cpl==20 for BOTH r), now
applied at r=312 for the first time, with three checks — Check A
(`classify_item_i_local`, unmodified), Check B (this program's own
founding T28 R3 sign/order-of-magnitude standard, now reported BOTH raw
and `CPL_RATIO`-normalized per the Reconciled queue's own Item 4), and
Check C (the ±2-bin neighborhood correlation, now R30-null-calibrated as
a percentile within a freshly-computed r=312-specific 48-window
population, not a bare fixed bar). Nothing in this document proposes,
varies, or scores any T1-relevant content — matching every T28
desk/instrument cycle since Iteration 46.

## 2. Parameter table

### 2.0 Grounding-fact verification (independently re-run this session, before proposing anything — R4 discipline)

| Claim | Checked | Result |
|---|---|---|
| The named bin's own `cpl=20` baseline figures, r=312 | `python3 -c "import run113 as R; ..."` against `experiments/110-.../results.json`'s own `r312` block (not hand-typed) | Bin index **46** of 48 sits exactly on `168.75°`. `peccored[46]=8.740493442723667e-05`, `hollow[46]=9.691509002810126e-05`, `delta[46]=-9.510155600864586e-06` ⇒ local relative deviation `|delta|/|peccored|=10.881%` (re-derived; matches the Director's briefed "~10%" figure and the PHOTONICS Iteration-85 self-review this bin traces to). Mirror-pooled floor `=3.3826e-4`; `local_snr_peccored=0.25840`, `local_snr_hollow=0.28651` — both below K=1, but markedly closer to it than exp-112's own r=156 bin (`0.0965`/`0.1061`) was — a genuinely different starting point for this leg, not a re-run of the same numbers at a different label. |
| `geom_fixedabs_cpl(312,25)`'s own correctness (reused, not re-implemented) | `python3 run113.py --verify-geometry` (re-run fresh this session, zero-FDTD) | `{"pass_": true, "mismatches": []}` at BOTH r=156 and r=312 — unchanged from exp-112's own finding, confirmed again independently this session, not merely assumed to still hold. |
| `CPL_RATIO` identity | `assert CPL_RATIO == R112.CPL_RATIO` (module-load-time assertion, `run113.py`) | Passes on import — `1.25` bit-identical across `run112.py`/`run113.py`. |
| The historical `cpl=25`/r=156 pilot total (this cycle's own R31 baseline) | `python3 -c "import json; json.load(open('experiments/112-.../results.json'))['total_wall_s']"` | `670.4777698516846` — a bare **scalar**, confirming the briefed completeness gap: exp-112's own per-scene breakdown is genuinely unrecoverable from this file (see §5, Idealization 1). |
| Projected cost gate, AS IF this session ran at exp-112's own historical (Iteration 89) per-step speed, no R31 correction | `python3 -c "..."` invoking `R110.cost_gate_check(670.4777698516846/3.0, 670.4777698516846)` directly (the real committed function) | `{"projected_312_total_s": 6802.6408688513, "total_pass": true, "proceed_to_r312": true}` — reproduces the Director's briefed `6802.6s`/37% margin figure bit-exact. **This is the uncontrolled reading** — R31 (LOGBOOK.md, founding instance exp-112, ratified Iteration 89) requires a fresh same-session control point before this number gates anything; `chunk_runner113.py::check_cost_gate_for_r312` already implements this, not yet run (Phase 1, zero-FDTD). |
| Sponge (`ABSORB`/`EDGE`) log-attenuation figure, reused from exp-112's own Phase-2/Phase-5-corrected record | `python3 -c "import numpy as np; np.exp(-17.242357)"` | `3.248923608023393e-08` — bit-exact to MATERIALS'/Red Team's own Iteration-89 corrected figure. Freshly compared against THIS cycle's own r=312/`cpl=20` floor (`3.3826e-4`, above): margin `≈4.02` orders of magnitude, consistent with (not a re-derivation that could silently drift from) the corrected "~1.8–4.5 orders, not 6–8" finding — non-fatal at r=312 too. See §6 for why this needed independent re-checking rather than blind copy-forward. |

### 2.1 Geometry — congruent `cpl=20→25` refinement, r=312, fixedabs family (unchanged construction, new `r`)

| Quantity | `cpl=20` (baseline, exp-108/110, unchanged) | `cpl=25` (this cycle) |
|---|---|---|
| Domain `N` (cells, square) | 2240 | **2800** |
| `CX`, `CY` | 1008, 1120 | **1260, 1400** |
| `SRC_X` | 256 | **320** |
| `STEPS` | 12800 | **16000** |
| `R_CORE` | 264 | **330** |
| `R_COAT` | 312 | **390** |
| `sigma_max` | 0.5 | **0.4** |
| `tau_shell` (invariant, by construction) | 24.0 | 24.0 |
| `ABSORB` (PML-taper thickness, cells) | 40 | **50** |
| `EDGE` (source cosine-taper, cells) | 40 | **50** |
| `box_a` (margin=32) | — | **(710, 1810, 850, 1950)** |
| `ref` (incident-intensity strip) | — | **(1260, 1400, 300)** |

Re-verified this session (`geom_fixedabs_cpl(312,25)`, printed above): total
simulated optical periods `= STEPS·S/lam = 16000·S/25 = 640·S` — exactly
double exp-112's own r=156 figure (`320·S`), consistent with r=312 being a
`kappa_ratio=2.0` scale-up of r=156 at the SAME `cpl`, not an independent
construction. Domain-clearance: `box_a` spans `x∈[710,1810]`,
`y∈[850,1950]`, inside `N=2800`'s valid interior `[50,2750]` —
comfortably inside on every side.

**FDTD calls this cycle: 3** (empty, hollow-article, PEC-cored-article,
r=312 only, `cpl=25`). **STEPS per scene: 16000**; **total steps this
leg: 48000** (3×16000). **Projected wall time (uncontrolled reading,
§2.0): 6802.6s (113.4 min)**, against the `10800s`/3h bound — 37% margin,
**explicitly provisional**: R31 requires this to be re-derived from a
fresh same-session control (`chunk_runner113.py --control`) before it
gates the real Phase-4 spend; `chunk_runner113.py`'s own
`check_cost_gate_for_r312` raises rather than proceeds if no control
point is on file.

### 2.2 Target bin and falsification bands

**Target: bin index 46 (`168.75°`), margin=32 (`box_a`), r=312 only.**
Full bands in §4.

## 3. Scope decision: r=312 alone, R31-gated, zero further Tier-1 bundling

**r=312-alone**, matching the queue's own item 1 exactly — this is the
single leg the Reconciled Iteration-90 queue names as highest-value, and
bundling a second independent leg (e.g. attempting `cpl=30` at r=156 in
the same cycle, Tier 2 item 1) would repeat the density pattern this
governance sub-thread has landed PARTIAL under every cycle since
Iteration 82 (R20's own tally sits at 1–2 for five consecutive cycles
running per Red Team's own Iteration-89 final audit). Queue items 3
(R30-calibrated Check C) and 4 (`CPL_RATIO`-normalized Check B) are
executed as part of THIS leg's own instrument, not deferred — they are
what makes this leg's own readings trustworthy, not a separate bundle.

I decline to also attempt: the Tier-2 `cpl=30` third resolution point
(explicitly gated, by the queue's own text, on Tier-1 items 3–4 landing
first — which this cycle does, but a third data point is its own next
step, not this one); the `R2_SMOOTH_THRESHOLD=0.90` re-derivation (now a
sixth consecutive cycle naming it undone — orthogonal to this leg,
irrelevant since this cycle fits no smoothness model); MATERIALS' own
fabrication-tolerance bound (fifth consecutive cycle undone — explicitly
MATERIALS' own charter question); the sixth `gate_reposition_control.py`
checkpoint-resume case (EM's own item, its underlying property already
independently confirmed to hold). Each is a real outstanding debt, named
here for the record, not silently dropped — but bundling any of them onto
the cycle that finally executes the queue's own named highest-value item
repeats the exact density risk exp-112's own Phase-1 document already
reasoned through and declined for the same structural reason.

## 4. T1 escape route: N/A

Confirmed structurally, independently, against exactly what this cycle
changes: a congruent geometry-scaling function (reused, not modified), a
checkpoint/resume capture driver with a time-budgeted sub-chunk loop and
an R31 control mode, and a comparison of existing classification
functions' readings across two resolutions at a new `r`. No
σ(I)/σ(x,t)/angular-selectivity/sub-threshold content is expressible in a
grid-resolution parameter, a floor-comparison classifier, or a wall-time
control ratio. No constraint-1/2/3/4 verdict is scored or moved anywhere
in this document — matching every T28 desk/instrument cycle since
Iteration 46, including exp-108 through exp-112 by name.

## 5. Falsifiable predicted outcomes — numeric bands

Verbatim from `run113.py::build_predictions_text()` (re-run this session,
§2.0), restated here as an explicit table per this document's own format
requirement (the predictions text itself remains the single source of
truth — R23 discipline; this table transcribes it, it does not diverge
from it):

**Check A** (`classify_item_i_local`, unmodified, at `cpl=25`; baseline
`cpl=20` values: `local_snr_peccored=0.2584`, `local_snr_hollow=0.2865`):

| Outcome | Condition |
|---|---|
| SURVIVES, candidate-real-structure-eligible | `local_snr_peccored≥1.0` **AND** `local_snr_hollow≥1.0` **AND** Check C's own `supports_real_structure` is `True` (percentile ≤10th) |
| SURVIVES, not yet upgraded | both `local_snr≥1.0` but Check C's percentile is `>10th` |
| COLLAPSES | neither `local_snr` improves over its `cpl=20` value (`0.2584`/`0.2865`) |
| AMBIGUOUS | some improvement, still `<1.0` |

**Check B-normalized** (this cycle's own scored reading — `delta[idx]`
divided by `CPL_RATIO=1.25` before comparison, Item 4):

| Outcome | Condition |
|---|---|
| SURVIVES | `delta_cpl25/1.25` keeps the same sign as `cpl=20` (`−9.510156×10⁻⁶`) **AND** `0.1 ≤ \|ratio\| ≤ 10` |
| COLLAPSES | sign flip, OR `\|ratio\| < 0.1` |
| AMBIGUOUS | neither band cleanly applies |

**Check B-raw** (exp-112-comparable, uncorrected, disclosed but explicitly
**not** this cycle's scored reading — carried only for continuity/audit):
same bands, applied to the un-normalized `delta_cpl25`. Per the
`CPL_RATIO` finding (Item 4, §6), this reading is expected to read
SURVIVES essentially regardless of any real bin-specific structure, and
must not be cited as evidence on its own.

**Check C** (R30 null-calibrated percentile, this cycle's own r=312-
specific 48-window scan — computed fresh, not borrowed from exp-112's own
r=156 scan):

| Outcome | Condition |
|---|---|
| supports_real_structure = True | named bin's own ±2-bin windowed correlation sits at or below the **10th percentile** of this cycle's own 48-window null population |
| supports_real_structure = False | percentile `>10th` |

**No advance position is taken on which outcome any of the three checks
will report** — matching this program's own R10 discipline (report, don't
pre-pick, the more favorable reading) and exp-112's own identical
pre-registration posture.

## 6. Idealizations — what this leg does and does not establish

- **Does establish**: a real, executed, congruent `cpl=20→25` refinement
  of the fixedabs family's own r=312 geometry (the first FDTD data this
  specific bin has ever received beyond its single `cpl=20` reading),
  applying the SAME unmodified Check-A instrument, a properly
  `CPL_RATIO`-normalized Check B, and an R30-null-calibrated Check C —
  with a pre-registered, falsifiable verdict, gated by an R31 same-session
  cost control before the real spend is attempted.
- **Does NOT establish**: full continuum convergence at r=312 (R15's own
  two-point discipline — a single new resolution point relative to
  `cpl=20` can rule out (or fail to rule out) a sign-flip/order-of-
  magnitude collapse, no more). A third, differently-scaled resolution
  point at r=312 is not proposed this cycle.
- **Does NOT establish** whether the `−146.25°`/r=156 bin's own AMBIGUOUS
  reading (exp-112) generalizes to this bin — the two bins share a
  construction recipe and a comparable local-deviation magnitude, but
  nothing in this document assumes they must behave alike; that is
  exactly the open question this leg exists to answer, independently.
- **Idealization 1 — the cross-session historical wall-time breakdown is
  genuinely, not merely inconveniently, unrecoverable.** Independently
  re-checked this session (§2.0): `experiments/112-.../results.json`'s own
  top-level `total_wall_s` key is a bare scalar (`670.4777698516846`),
  confirming `analyze.py`'s own `dict(row, total_wall_s=scalar)` merge
  clobbered `row`'s own per-scene dict, as briefed. The per-STEP average
  used to seed `HISTORICAL_PER_STEP_S` (`670.4778/(3·8000)=0.027937s`/step)
  rests on the disclosed idealization that FDTD per-step cost is
  materials-invariant across the three scenes sharing identical
  `STEPS=8000`/`N=1400×1400` — a reasonable, but *assumed, not directly
  measured*, equal-split; the true empty/hollow/peccored split could
  differ (a PEC-cored or graded-shell scene plausibly costs marginally
  more per step than empty, from the extra materials update, though this
  program's `lab/fdtd2d.py` update loop touches the full grid regardless
  of contents — a point this Idealization states rather than resolves).
  `analyze113.py` fixes the underlying persistence bug going forward (a
  NEW key, `total_wall_s_by_scene`, distinct from the clobbered
  `total_wall_s` name), so this specific completeness gap cannot recur
  from THIS cycle's own output — but exp-112's own historical figure
  remains an averaged, not measured, per-scene baseline.
- **Idealization 2 — the projected cost is explicitly provisional until
  Phase 4's own R31 control runs.** The `6802.6s`/37%-margin figure (§2.0)
  assumes this session's own compute throughput matches exp-112's own
  Iteration-89 session bit-for-bit. R31's own founding instance found a
  `~2.19×` cross-session speed difference the OPPOSITE direction of what
  would have caused unsafe spend (this session was faster) — but nothing
  guarantees today's session repeats that direction or magnitude; a
  slower session here would need the `r31_control_ratio` machinery to
  correctly scale the projection UP, and `chunk_runner113.py`'s own
  `check_cost_gate_for_r312` is written to raise (not silently proceed)
  if `proceed_to_r312` reads `False` once the real control is measured. No
  Phase-4 `Sim.run()` call for the real r=312 legs occurs before that
  control point exists on file.
- **Idealization 3 — Check C's own null population includes the named
  bin's own observation.** The 48-window scan (`neighbor_correlation_
  null_scan`) computes the named bin's own windowed correlation as one of
  the 48 values it is then ranked against (not a leave-one-out null) —
  the SAME convention PHOTONICS'/QUANTUM's own Iteration-89 Phase-5 scans
  used, reused here for direct comparability rather than introducing a
  methodologically different (arguably slightly more rigorous)
  leave-one-out variant mid-thread. With `n=48` this makes at most a
  ~2-percentile-point difference at the threshold's own edge — disclosed,
  not expected to be outcome-determining, but named for Phase 2's own
  scrutiny rather than silently inherited.
- **Idealization 4 — the `≤10th percentile` Check-C bar is a disclosed,
  reasonable, but not independently re-derived choice.** It halves the
  distance from "any positive correlation counts" (the exp-112 defect
  R30 exists to fix) to "only the single most extreme reading counts"
  and roughly matches a conventional one-tailed 10% significance
  convention — but it was set by the Director's own brief for this
  cycle, not derived from a power calculation against this specific
  48-window population's own shape. Not proposed to change this cycle
  (changing it now, after seeing predicted context but before seeing real
  `cpl=25` data, would itself risk exactly the kind of post-hoc threshold
  tuning this program's own R5/R17/R30 lineage exists to prevent).
- **Does NOT re-derive** `R2_SMOOTH_THRESHOLD=0.90`, MATERIALS' own
  fabrication-tolerance bound, or the `gate_reposition_control.py`
  checkpoint-resume case — declined this cycle, §3.
- 2D TMz, λ=600nm only — unchanged program-wide scope.

## 7. What carries forward vs. what is revised from exp-112

**Carries forward, unmodified**: `geom_fixedabs_cpl` (reused by direct
import, not copy-paste — `run113.py` imports `run112 as R112` and calls
`R112.geom_fixedabs_cpl`); `classify_item_i_local`/`kappa_of`/
`cost_gate_check`/`COST_GATE_PILOT_S`/`COST_GATE_TOTAL_S` (imported from
`run110 as R110`, unmodified); the R29 distinct-module-name convention
(`run113.py`/`chunk_runner113.py`/`analyze113.py`, with executed identity
assertions in every downstream file); the `margin=32` choice (direct
symmetry with exp-112's own tested margin); the three-check (A/B/C)
framework itself; the R23 single-source-of-truth `DISCLAIMER` discipline;
the checkpoint/resume idiom (`SUBSTEP`/checkpoint-every-substep).

**Revised, this cycle, per the Reconciled Iteration-90 queue**:

- **Check C** (Item 3): a bare `corr≥0.5` pass/fail → a percentile within
  a freshly-computed, r=312-specific 48-window null population,
  `supports_real_structure` now requiring a **≤10th-percentile outlier**,
  not merely clearing a fixed bar (R30).
- **Check B** (Item 4): a single raw comparison → BOTH a raw (legacy,
  disclosed, explicitly NOT scored) and a `CPL_RATIO`-normalized (this
  cycle's own scored) reading, closing the previously-unrecognized
  zero-discriminating-power failure mode PHOTONICS' Iteration-89 Phase-5
  review found in `lab/sections.py::_face_flux()`'s own missing `dx`
  normalization. `lab/sections.py` itself is left unmodified (a shared,
  trust-suite-gated library every other caller in this program compares
  WITHIN one `cpl`, where the factor cancels) — the fix is applied only
  at this cycle's own point of cross-`cpl` comparison.
- **Cost gate** (Items 1+2): a bare cross-session `ratio**3` projection →
  an R31-compliant wrapper (`cost_gate_check_r31`) that requires a fresh
  same-session control point (`chunk_runner113.py --control`) before
  `proceed_to_r312` is trusted, reporting BOTH the raw (uncontrolled) and
  scaled (R31-corrected) readings rather than gating on the raw one
  silently.
- **Wall-time persistence**: a new key, `total_wall_s_by_scene`
  (`analyze113.py`), replacing the clobbering `dict(row,
  total_wall_s=scalar)` merge pattern that produced Idealization 1's own
  completeness gap in exp-112's `results.json`.
- **Target**: a new bin/`r` (`168.75°`/r=312, bin index 46) — the mirror
  companion of exp-112's own `−146.25°`/r=156 (bin index 4), not a re-run
  of the same question.
- **DISCLAIMER — my own two additions this cycle (VISION SCIENCE,
  Iteration 90), both applied directly to `run113.py`, before any
  execution**:
  1. **Restored and re-verified the ABSORB/EDGE sponge disclosure.**
     `run113.py`'s own committed `DISCLAIMER` (as handed to me) dropped
     exp-112's own hard-won, twice-corrected sponge-non-invariance
     disclosure entirely — a real regression in disclosure completeness,
     not merely a stylistic gap: the SAME `cpl=25`/`ABSORB=50` config is
     reused this cycle (the log-attenuation figure is `cpl`-specific, not
     `r`-specific, so it transfers unchanged), but the "orders of
     magnitude below the floor" comparison is `r`-specific (the floor
     scale differs at r=312 vs r=156) and had never been checked at this
     `r` before. I added it back, computed fresh against THIS cycle's own
     r=312 floor (§2.0: `~4.02` orders of magnitude, non-fatal, matching
     — not re-introducing the error in — MATERIALS' own corrected
     figure), as two new module constants (`_SPONGE_LOG_ATTEN_CPL25`,
     `_SPONGE_ABS_VAL`, `_SPONGE_MARGIN_ORDERS`) computed in code and
     interpolated into the `DISCLAIMER` string, not hand-typed (R4
     discipline).
  2. **Added a prophylactic disambiguation of Check C's own "percentile"/
     "null population"/"outlier" vocabulary from signal-detection-theory
     vocabulary.** This is a genuinely new term-scoping risk this cycle's
     own R30 fix introduces (it did not exist in exp-112's own Check-C
     text, which used a bare `corr≥0.5` pass/fail): "percentile of a null
     population," "outlier," and even "detection" (already covered)
     sitting next to each other is precisely the vocabulary of
     signal-detection theory — my own charter's own native instrument
     family (a percentile of a fitted psychometric function, d-prime,
     hit/false-alarm rate) — and a reader unfamiliar with this program's
     own convention could plausibly, if only briefly, read Check C's own
     statistic as a perceptual-detectability claim rather than a
     spatial-correlation-vs-grid-refinement one. I checked this
     document's own code and predictions/result text for any place this
     vocabulary is actually used inconsistently with a purely statistical
     reading — none exists; this is a **prophylactic** addition (closing
     a risk before it is exploited by a future citation that strips
     context, the exact R4/R9 "citation-shortening" failure mode this
     program has paid for before), not a correction of a discovered
     error, and it changes no verdict-arithmetic anywhere in this
     document.

  Both additions were verified, after being made, by re-running
  `python3 run113.py --verify-geometry` and `python3 run113.py
  --predictions-only` (both succeed, unchanged geometry-identity result)
  and by re-executing `python3 analyze113.py` (still correctly reaches
  its pre-data early-exit message) — the edits are additive text inside
  an f-string-interpolated constant, not a change to any classification
  function's own arithmetic; `git status --short lab/` remains empty
  throughout, and the trust suite was re-run fresh this session
  (`python3 lab/validation/run_all.py`): **43/43 checks passed**. Phase 2
  critics should diff `run113.py` against this document's own git history
  to see exactly these two additions and nothing else.
