# PHASE 1 — PROPOSAL · Panel Iteration 87 (candidate exp-110)
## Lead seat: ELECTROMAGNETISM (rotation lead)
## "Item i's Local-Magnitude Floor Gate (Corrected Premise: Not Zero-FDTD), a Fault-Injection Control for `linear_fit_1_over_margin`, and `stage26`'s Truncation-Direction Negative Control"

### 0. What kind of cycle this is

**Governance/instrumentation cycle, not a mechanism proposal** — matching
exp-107/108/109's own established framing exactly. **T1 escape route: N/A.**
No σ(I)/σ(x,t)/angular-selectivity/sub-threshold machinery is built,
varied, or touched anywhere in this document; no constraint-1/2/3/4
verdict is scored or moved by any branch of it. Scoped exactly to the
three UNBLOCKED Tier-1 items on exp-109's own Reconciled Iteration-87
queue (`LOGBOOK.md` Iteration 86). Tier-0 item 0 — ruling on the
Iteration-85 Checkpoint-4 firing — is Marsh's call, out of scope, not
attempted, named only to confirm it remains pending.

### 0.5 Grounding-fact finding — the queue's own "zero new FDTD" premise for item 1 is FALSE

Independently verified, not taken on faith, three ways:

1. **The scratch path is gone.** `analyze.py`'s own `SCRATCH =
   "/tmp/claude-0/.../b3074561-e458-5939-8b7f-fe9684f9569f/scratchpad/
   exp108"` does not exist in this container (`ls` → No such file or
   directory). A whole-filesystem search for `*exp108*` or any
   `r{156,312}_*_done.pkl` file returns nothing, anywhere. Confirmed:
   this is a different, now-defunct session's ephemeral scratchpad —
   exactly the environment property this cycle's brief warned about.
2. **`results.json`/`analyze_output.json` never persisted the per-bin
   arrays item 1 needs.** Both files are byte-identical in structure
   (checked directly): `item_i` carries only `verdict`, `rel32` (48
   floats, **margin=32 only**, already `|delta32|/max_peccored32` —
   GLOBALLY normalized, exactly the quantity item 1 wants to replace),
   `runs=[]`, `run_details=[]` (empty because `confirm_all_margins=True`
   and zero bins cleared the 15% REFUTE bar — CONFIRM never populates
   them), `confirm_all_margins`, `sum_check_pass`, `bin_centers_deg`.
   Nowhere in either committed file do `pattern_by_margin_delta[m]`,
   `sigma_scat_by_margin_peccored[m]`, or `sigma_scat_by_margin_hollow[m]`
   appear, for ANY of the 6 margins, including margin=32. `analyze.py`
   computes them in-memory (lines 50-68 of its own `analyze_r()`) purely
   to feed `classify_item_i()` and is never told to serialize them.
3. **exp-108's own Phase-5 review record confirms the timing exactly.**
   PHOTONICS' own self-review (`phase5_review_photonics.md` §3b) and Red
   Team's own final audit (`phase5_redteam_audit.md` §0.1) both computed
   the 9.88%/10.88% local-normalized figures by reading "the raw pickled
   captures still on disk in this session's scratch directory" — i.e.
   the pickles existed THEN, in THAT session, and were consumed live.
   exp-109's own Idealizations (§5) already names this exact hazard for
   item ii's much lighter data need (`fit`/`delta_values`, both of which
   ARE committed) and explicitly did not need to cross it. Item 1's need
   is categorically heavier: the full-field phasor captures themselves.

**Conclusion: item 1 cannot be computed from already-committed data.** The
Iteration-86 queue's "zero new FDTD, all data already committed" line is
incorrect for this item — an honest correction to the permanent record,
not a criticism of exp-109 (MATERIALS' own cycle never touched item 1;
the premise was inherited from exp-108's own Phase-5 recommendation,
written when the pickles were still live and the gap was not yet visible
from a colder session). This finding drives this proposal's scope below:
rather than defer, I propose a **minimal, bit-identical re-capture** (the
literal same 6 FDTD calls exp-108 already made) whose sole NEW purpose is
persisting the per-bin data permanently — closing the gap for good,
exactly once, rather than leaving a fourth cycle to rediscover it cold.

### 1. Narrative (≤300 words)

Three items, one unifying EM-seat concern (reciprocity/symmetry
bookkeeping) tying items 1 and 3 together, item 2 standing alone.

**Item 1.** `classify_item_i`'s `rel32` divides every bin's deviation by
the single global peak bin — PHOTONICS' own Phase-5 finding. I propose a
**local floor gate**, not a full renormalization: re-capture the identical
6-call geometry (byte-for-byte `geom_fixedabs`, gated against exp-106's
own committed values exactly as exp-108 did), this time persisting the
full 48-bin, 6-margin peccored/hollow/delta arrays into `results.json`
permanently. Then floor-gate each bin using a **mirror-symmetry noise
floor**: this bench is mirror-symmetric about the propagation axis
(normal-incidence plane source, circularly-symmetric target, box centered
on the target) — bin θ and bin −θ are exactly paired (24 pairs, no
self-paired bin), and any measured asymmetry between them in a SINGLE
capture is pure discretization noise, in the SAME units as the pattern
itself (unlike item ii's `abs_ext_ratio`-scale floor, avoiding PHOTONICS'
own unit-mismatch critique). A bin is scored only if BOTH its peccored
AND hollow parent values individually clear this floor — discharging R13
(denominator) and R14 (numerator-parent smoothness) in one gate. Reported
as an **informational diagnostic**, not folded into item i's already-
Phase-5-corrected, dominant-lobe-scoped CONFIRM.

**Item 2.** `linear_fit_1_over_margin`'s monotonic-OR-R²≥0.90 smooth gate
has never been fault-injection tested (R18). Four deterministic synthetic
6-point sequences at the real margins, isolating both arms of the OR.

**Item 3.** `stage26`'s negative control tests only over-running
(under-reported `steps_done`). I add the symmetric truncation direction
(over-reported `steps_done`), closing R18's coverage the other way.

### 2. Parameter table

| # | File | Change |
|---|---|---|
| 1a | `experiments/108-.../chunk_runner.py` (**re-run verbatim, unmodified**) | 6 `Sim.run()` calls, foreground Bash only (exp-107/108's own diagnosed backgrounding-slowness finding, reused without re-testing): `empty`/`hollow`/`peccored` × r∈{156,312}, `geom_fixedabs(r)`, `CPL_600=20`, `COURANT_FRAC=0.32`, `ABSORB=EDGE=TAPER=40`, `ABS_THICKNESS=48` (held const), `SIGMA_MAX_FIXED=0.5`. r=156: N=1120, CX=504, CY=560, SRC_X=128, STEPS=6400, R_CORE=108, R_COAT=156. r=312: N=2240, CX=1008, CY=1120, SRC_X=256, STEPS=12800, R_CORE=264, R_COAT=312. `CHUNK_STEPS=2200`. Identical geometry constants exp-108 already used — zero new mechanism, pure re-capture. |
| 1b | `experiments/110-.../analyze.py` (**new, forked from exp-108's own**) | Reuses `R.gate_p0(g)` and `R.reproduction_precondition(...)` unmodified (must PASS exactly, else halt before any new claim is trusted — same discipline as exp-108). NEW: for each r, each margin m∈MARGINS, serializes `pattern_by_margin_peccored[m]` (48 floats), `pattern_by_margin_hollow[m]` (48 floats), `pattern_by_margin_delta[m]` (48 floats) into `results.json["item_i"]["raw_patterns"][m]` — the persistence fix, permanent, ≈1728 floats total (6 margins × 3 arrays × 48 bins × 2 r), kilobytes not megabytes, git-committable (unlike the multi-MB field pickles). |
| 1c | `experiments/110-.../run.py` — **new function** `mirror_floor(pattern_48, bin_centers_deg)` | `bin_centers_deg[i] = -176.25 + 7.5*i` exactly (verified against exp-108's own committed array both r); its mirror is `bin_centers_deg[47-i] = -176.25+7.5*(47-i) = 176.25-7.5*i = -bin_centers_deg[i]` exactly — an exact index reversal (`mirror(i)=47-i`), asserted against the committed array before use rather than assumed. Returns a 48-length array where each bin gets `\|pattern[i]-pattern[47-i]\|/2` (both members of a pair get the identical value). |
| 1d | `experiments/110-.../run.py` — **new function** `classify_item_i_local(r, margin, pattern_peccored, pattern_hollow, pattern_delta, bin_centers_deg, K=3.0)` | Per bin: `floor = K * max(mirror_floor(pattern_peccored,...)[bin], mirror_floor(pattern_hollow,...)[bin])`. Bin is `RESOLVED` iff `\|pattern_peccored[bin]\| >= floor AND \|pattern_hollow[bin]\| >= floor` (R13+R14 joint gate — both parents, not just one); else `UNRESOLVED-BY-CONSTRUCTION` (R13's own prescribed label). For RESOLVED bins: `local_rel[bin] = \|pattern_delta[bin]\| / \|pattern_peccored[bin]\|`, reported against the SAME 5%/15% bands item i already uses, **labeled informational, not a verdict**. `local_snr[bin] = \|pattern_peccored[bin]\|/floor` reported for EVERY bin regardless of gate outcome (R13's "disclosed as such" convention — nothing hidden behind the K choice). |
| 2 | `experiments/110-.../linear_fit_control.py` (**new**) | Imports `linear_fit_1_over_margin`, `R2_SMOOTH_THRESHOLD`, `MARGINS` from exp-108's own `run.py` via `importlib.util.spec_from_file_location` (exp-108/109's own established idiom — the directory name is not a valid package identifier). Runs the 4 synthetic sequences below, asserts each outcome, zero `Sim.run()` calls anywhere. |
| 3 | `lab/validation/run_all.py` — `stage26_chunked_run_identity()` (patched in place, disclosed `lab/` diff, no engine-physics change) | New negative-control block appended after the existing one (lines ~2772-2791): a second corrupted checkpoint, symmetric direction (spec below). New `check(...)` call, same "chunked-run" stage tag. |

**Item 2's four synthetic sequences** (computed NOW by direct invocation
of the actual committed `linear_fit_1_over_margin(MARGINS, y)`, `MARGINS
=(24,32,40,48,57,65)`, R4 discipline — not hand-derived):

| Case | Construction | `y` values | `is_monotonic` | `r_squared` | `residual_std` | `smooth` |
|---|---|---|---|---|---|---|
| **P1** — exact trend, zero noise | `y = A + B/margin`, `A=-1.5e-5, B=-4.0e-4` | `[-3.1667e-5,-2.7500e-5,-2.5000e-5,-2.3333e-5,-2.2018e-5,-2.1154e-5]` | **True** | **1.0** | **3.6e-21** | **True** |
| **P2** — monotonic, poor 1/margin fit (isolates OR's monotonic arm) | `y = 1e-9·exp(margin/6)` | `[5.46e-8,2.07e-7,7.86e-7,2.98e-6,1.336e-5,5.068e-5]` | **True** | **0.397** | 1.412e-5 | **True** |
| **P3** — non-monotonic, good fit (isolates OR's R² arm) | P1's exact sequence with bin margin=40 (index 2) perturbed by `+3.0e-6` | `[-3.1667e-5,-2.7500e-5,-2.2000e-5,-2.3333e-5,-2.2018e-5,-2.1154e-5]` | **False** | **0.912** | 1.118e-6 | **True** |
| **N1** — non-monotonic, poor fit (negative control) | Deterministic zigzag, `amplitude=3.0e-6` | `[3e-6,-3e-6,3e-6,-3e-6,3e-6,-3e-6]` | **False** | **0.097** | 2.851e-6 | **False** |

No RNG/seed anywhere — every case is a closed-form deterministic sequence,
reproducing bit-exact on any re-run (R12's own multi-seed concern is N/A:
nothing here is a noise-sample order statistic).

**Item 3's truncation-direction negative control** (exact spec, mirrors
the existing over-run block structurally):

```python
# negative control (extended, this cycle): TRUNCATION direction —
# over-reported steps_done -> resumed run advances FEWER steps than true total
sim_probe2 = fresh_scene()
sim_probe2.run(CHUNK)                       # 300 real physical steps done
ckpt2 = pickle.dumps(sim_probe2)
sim_resumed2 = pickle.loads(ckpt2)
corrupted_steps_done2 = 2 * CHUNK           # LIES: claims 600 done, true=300
remaining2 = TOTAL_STEPS - corrupted_steps_done2   # = 300, not the true 600
sim_resumed2.run(remaining2)                # ends at 300+300=600 real steps, not 900
fields_truncated = capture_fields(sim_resumed2)
# ... max|diff|, rel_diff_truncated computed identically to the existing block
check("chunked-run",
      "negative control (truncation): over-reported checkpoint (steps_done "
      "high by one chunk) vs continuous, relative max|diff| (ez scale)",
      f"{rel_diff_truncated:.3f}", rel_diff_truncated > 0.01,
      ">0.01 (gate must discriminate)")
```

`corrupted_steps_done2 = 2*CHUNK = 600` keeps `remaining2 = 300 > 0` safely
positive (no negative-argument edge case) while producing a genuine
truncation: the resumed run stops 300 physical steps short of the true
900-step total, the symmetric direction to the existing block's 300-step
over-run (1200 vs 900).

### 3. T1 escape-route statement

**N/A**, matching every governance cycle since Iteration 84. Confirmed
structurally: item 1 touches only angular-pattern floor-gating math (no
σ(I)/σ(x,t) content possible in a symmetry-based noise floor); item 2
touches a pure numpy curve-fit diagnostic; item 3 touches a checkpoint/
resume identity gate on a fixed empty-scene bench configuration. No
constraint-1/2/3/4 verdict is scored or moved anywhere in this document.

### 4. Predicted outcomes — falsifiable bands, stated before any code runs

**Item 1a (re-capture fidelity):** `gate_p0` PASS exact, both r (bit-
identical geometry constants — deterministic FDTD, no randomness, matches
exp-107's own chunk_runner A/B bit-exactness precedent). `reproduction_
precondition` PASS, `sigma_abs`/`sigma_ext`/`abs_ext_ratio` matching
exp-108's own committed `results.json` values to <1e-9 relative at both r
(279.6607/560.1989 at r=156; 588.0218/1191.3259 at r=312) — falsified by
ANY deviation exceeding that bound, which would mean this re-capture is
NOT the reproduction it claims to be.

**Item 1b (persistence):** `len(results.json["item_i"]["raw_patterns"][m]
["peccored"]) == 48` for all 6 margins, both r — 100% coverage, no gaps.
Falsified by any missing margin/scene/r combination.

**Item 1c/1d (mirror floor — genuinely uncertain, the actual question this
instrument exists to answer):** I predict at least SOME of the 30/48
bins PHOTONICS' own review already found carry <1% of the peak's power
(both r) will fail the `K=3` floor gate (`UNRESOLVED-BY-CONSTRUCTION`) —
a pattern spanning ~5 orders of magnitude of dynamic range across 48 bins
cannot plausibly stay several floor-multiples above a roughly-constant
absolute discretization-noise floor all the way down to its smallest
bins. Falsified if ALL 48 bins clear `K=3` comfortably (`local_snr>10`
everywhere) at both r — a legitimate, informative negative result meaning
the floor gate was unnecessary here. For the two specific bins PHOTONICS
named (−146.25° at r=156, +168.75° at r=312, each read ~10% local
deviation under the old global-blind computation): I take NO position in
advance on whether they land RESOLVED-with-genuine-structure or
UNRESOLVED-by-construction — that is the open question item 1 exists to
answer, not something I should pre-commit either way to protect a
preferred outcome.

**Item 2:** all four `(is_monotonic, r_squared, smooth)` triples in the
table above reproduce bit-exact (they are pure deterministic numpy
arithmetic on closed-form sequences, already computed above by direct
invocation of the real committed function — Phase 4 re-invokes the
identical code and must return the identical numbers to full float
precision, or the "committed" figures above were wrong).

**Item 3:** `rel_diff_truncated > 0.01` (the gate's own minimum
discrimination bar) — high confidence, since the existing over-run
direction already measures `2.0` (200%) for a comparable 300-step/33%
count error, and this FDTD scene has no known structural reason a
300-step deficit would land near-zero relative deviation. I predict
`rel_diff_truncated` lands in `(0.01, 10]` — same order of magnitude as
the existing control, not pinned to an exact value. Falsified (gate fails
to discriminate) only if `rel_diff_truncated <= 0.01`.

### 5. Idealizations

- Item 1's floor gate is a NEW, first-use instrument (mirror-symmetry
  noise estimation). Per R18's own discipline, it should ideally receive
  its own fault-injection control (inject a KNOWN synthetic asymmetric
  perturbation into a fabricated 48-bin pattern, confirm the floor
  correctly flags it) before being fully trusted — **named explicitly as
  this cycle's own queued follow-up, not silently assumed complete**
  (R25's own discipline: a deferred check must become its own numbered
  queue line, not a parenthetical). Placed as Tier-1, Iteration-88 queue.
- `K=3` is a disclosed house-style multiplier, not derived from a
  resolution/aliasing bound (same disclosed-convention status as the
  existing six-margin absolute-floor family). `local_snr` is reported for
  every bin regardless, so a future reviewer can re-threshold without a
  re-run.
- Item 1's local diagnostic is explicitly INFORMATIONAL — it does not
  replace, gate, or reclassify item i's own existing (Phase-5-corrected,
  dominant-lobe-scoped) CONFIRM verdict. Keeping it un-scored is a
  deliberate scope choice: folding a brand-new instrument straight into a
  frozen verdict, in the same cycle it is built, is the exact shape of
  gap R24 exists to catch.
- Item 1's re-capture is bit-for-bit the same geometry/config exp-108
  already ran — this is a data-persistence fix, not new physics. The
  cost gate (`COST_GATE_PILOT_S=90min`, `COST_GATE_TOTAL_S=180min`,
  reused verbatim) still applies; if the r=312 pilot exceeds it, that
  leg defers exactly as exp-105/106 precedent allows, and item 1's
  r=312 analysis is reported NOT-RUN, not silently skipped.
- Item 2 does not re-derive `R2_SMOOTH_THRESHOLD=0.90` itself (already
  queued separately, Iteration-86 Tier 2b) — these controls test whether
  the OR-logic branch selection mechanically fires correctly at the
  EXISTING threshold, not whether 0.90 is the right number.
- Item 3's patch is a disclosed `lab/` diff (extending `stage26`, no
  engine-physics change) — the trust suite must stay green (41/41
  standard set) before this document is trusted, matching every prior
  `lab/`-touching cycle's own discipline.
- Tier-0 item 0 (the Iteration-85 Checkpoint-4 ruling) is explicitly not
  attempted — Marsh's call, out of scope for a Panel proposal.
- Every other queue item (Tier 2/3: `R2_SMOOTH_THRESHOLD` re-derivation,
  a fourth r-point, MATERIALS' fabrication-tolerance framing, the
  oblique-angle/750-450nm/`G40`/x-wall/`PAD` items, `box_dev`'s own
  thinning margin) is out of scope for this cycle, unchanged.
