# exp-096 — Angle-Domain Registration-Readback Gate (R3/R4/R5) + Zero-FDTD Bracket-Width Desk Bound

*Panel Iteration 73. Lead seat (rotation): PHOTONICS. Phase 1 proposal
only — no `run.py`, no FDTD calls executed by this document. Executes
Reconciled Iteration-73 queue items 1 and 2 (`experiments/095-t28-r4-
ground-truth-sign-control/NOTES.md` §Next, Red Team's own Phase-5 final
audit §7, LOGBOOK.md Iteration 72), the two items explicitly sequenced
BEFORE items 3/4 (bracketing the other three `cpl=20` nulls; the
reconciled node-bracketing re-run at 38.590°) and item 6 (the `cpl=50`/
`R5` interior sweep, deferred by every prior seat's own recommendation).*

## Standing-rule compliance header (checked against R1–R17; Red Team will
## check this line by line)

- **R1–R2, R6, R10** — not engaged: no carrier/phase mechanism proposed,
  no shell-thickness law, no named-constant search, no free-period fit.
  T1 route N/A throughout (see §4).
- **R3** (resolution-check meta-rule) — not directly engaged by this
  cycle's own core item (it reads back already-constructed objects at a
  single, fixed resolution per family; it does not itself compare across
  `cpl`). It is, however, the single most direct instrument this
  sub-thread has for distinguishing an R15-class cross-resolution finding
  from an R3-unrelated wiring defect — a CLEAN reading removes "the R3
  checks that have been running since exp-091 were themselves silently
  mis-registered" from the hypothesis space entirely.
- **R4/R9** (recompute-don't-hand-type; commensurability) — every figure
  cited below (the four `cpl=20` crossings, the three `cpl=30` crossings,
  the three cross-resolution migration magnitudes, every constant/function
  name) was retrieved this session by directly reading
  `experiments/090/092/095/069-.../{results.json,run.py,design_geometry.py}`
  and `lab/fdtd2d.py`, not hand-typed from LOGBOOK prose. Provenance is
  cited per figure in §3/§5.
- **R5/R11/R12** — not engaged: no named-constant search, no
  `free_period_with_widening` call, no seed-dependent statistic.
- **R7/R8** — engaged directly: this entire cycle IS the "cheap, affordable,
  previously-unaffordable check" R8's own lineage exists to force, applied
  to the single most-cited-but-never-run check in this 19-cycle sub-thread
  (Gate 5 has checked `sigma_e` magnitude at every `R3`/`R4`/`R5` call site
  it covers; it has never once checked `angle_deg`, `sim.lam`, or the
  phase-ramp array it produces).
- **R13/R14** (denominator floor gate; numerator subtractive-cancellation
  caution) — not engaged: this cycle computes no `ratio_k`, `frac_contrast`,
  or `frac_p_abs`; it reads Python/NumPy object attributes off a
  freshly-constructed `Sim`, not a physical measurement built from FDTD
  output.
- **R15 / its Iteration-71 addendum** — this cycle is the specific,
  previously-unexecuted check the addendum's own "far-from-null ground-
  truth control" and exp-095's own Rank-1c design both implicitly assumed
  was already covered by *some* layer of house discipline and discovered,
  at exp-095's own Phase-5, was not: Gate 5 validates `sigma_e`, never
  `angle_deg`/`sim.lam`/the phase array. This cycle closes that specific
  gap directly, at near-zero cost, exactly as the reconciled queue frames
  it ("the single most fundamental unresolved question").
- **R16** (NETD byproduct persistence) — not engaged: this cycle computes
  no thermal/NETD quantity of any kind; it never calls `cell_metrics_r{3,4,5}`
  or `netd_row()`.
- **R17** (bracket/tolerance sizing, adopted last cycle) — engaged on TWO
  fronts, both addressed explicitly: (a) this cycle's own item 2 (§5c) is a
  direct, first application of R17's own discipline — the desk bound is
  computed BEFORE any bracket is chosen, against the full set of
  already-filed migration figures, not an illustrative round number; (b)
  the numerical tolerance used inside the registration gate itself
  (`atol=1e-9` on a phase-ramp array comparison, §3) is explicitly NOT an
  R17-governed quantity — R17 governs brackets sized to test whether a
  *physical feature* (a node/crossing/period) is present or has moved;
  `atol=1e-9` tests whether two IEEE-754 float64 evaluations of the
  identical closed-form formula agree to within floating-point noise, a
  categorically different question with an eleven-order-of-magnitude
  safety margin computed explicitly in §3 — flagged here to preempt a
  Phase-2 conflation of the two.

## 1. Mechanism/instrument narrative

Not a mechanism proposal — pure instrument work, continuing the
established T28 desk/instrument pattern since exp-069. Nineteen cycles of
this sub-thread (exp-069 through exp-095) have measured `delta_scene(θ)`
across three grid densities (`cpl`∈{20,30,40}, with a fourth, `cpl=50`,
built but unexercised), located six real zero-crossings, and repeatedly
found that the `R4` family reverses sign relative to `R3` at every
interior point exp-094 sampled. exp-095's own Rank 1c asked the sharpest
version of the question this reversal raises — does the established
θ₀≈38.590° null survive in the `R4` family at all? — and got a FAIL: no
sign change across a ±0.1° bracket. Six blind Phase-5 reviews and Red
Team's own final audit shifted belief toward genuine node migration
(Rank 4's own companion reading places a `cpl=30` crossing 0.190° from
θ₀, matching established migration scale) but explicitly could not prove
it, because of one fact that has stood, unchecked, through every one of
those nineteen cycles: `_run_sim_r{3,4,5}_sigma`'s own mandatory Gate 5
(adopted Iteration 71) verifies that the constructed `Sim` object's
`sigma_e` array matches the intended `sigma_max` — and checks nothing
else. No cycle in this sub-thread has ever read back the constructed
`Sim` object's own `lam` (resolution) or the phase-ramp array
`add_line_source` builds from `angle_deg`, and compared either against
what the intended `θ`/`cpl` for that call actually was. A silent
mis-registration — the wrong `cells_per_lambda` reaching `Sim()` for a
given family, or the wrong `angle_deg` reaching `add_line_source()` for a
given job — would produce exactly Rank 1c's own observed signature (a
sign check that passes at amplitude-dominated far angles, a bracket that
fails to find a phase-dominated near-null node) and would be
*indistinguishable*, from `results.json` alone, from genuine physics.
This cycle builds the one check that reads the machinery itself, before
any of its output is trusted further, at a cost of zero additional FDTD
steps — the check operates entirely on `Sim` objects between
construction and `sim.run()`, a region every prior cycle's own code has
already had to pass through on every single call, just never inspected.

## 2. Design

**Two questions, two independent instruments, both zero-FDTD, run
together this cycle because the reconciled queue names them both as the
cheap, code-only/desk-only items to clear before any of items 3/4/6
(which all cost real FDTD calls) are worth spending on.**

### 2a. The registration-readback gate (queue item 1, PRIMARY)

**What it reads.** For a `Sim` object at the point immediately after
`add_line_source()` returns and before `sim.run()` is ever called:

- `sim.lam` — set once, in `Sim.__init__`, to `float(cells_per_lambda)`
  (`lab/fdtd2d.py:75`) — the resolution actually wired into this object,
  independent of what any caller *intended* to pass.
- `sim.source_specs[-1]['angle_deg']` — the raw `angle_deg` value
  `add_line_source` received (`lab/fdtd2d.py:184`), stored verbatim, no
  arithmetic applied.
- `sim.sources[-1]['x']` and `sim.sources[-1]['sl']` — the source's
  physical placement (`lab/fdtd2d.py:178-181`), a `slice(y_lo, y_hi)`
  object.
- `sim.sources[-1]['phase']` — the actual phase-ramp array
  `add_line_source` computed and stored: `k = 2π/self.lam;
  phase = k·sin(radians(angle_deg))·(yy − 0.5·(y_lo+y_hi)) + rel_phase`
  (`lab/fdtd2d.py:172-175`), one value per y-cell in the source's span.

**What it independently recomputes.** For each representative point (§3),
the intended `(family, θ, cpl_intended, y_lo_intended, y_hi_intended,
x_intended)` tuple is known ahead of time — it is copied verbatim from an
already-committed job constant in `experiments/095-.../run.py` (§3 table,
column "Provenance"), never invented fresh. The gate computes, from these
INTENDED values alone (never reading them back off the `Sim` object it is
checking):

```
k_expected = 2 * pi / cpl_intended                       # NOT sim.lam yet
yy = np.arange(y_lo_intended, y_hi_intended, dtype=float)
phase_expected = (k_expected * np.sin(np.radians(theta_intended))
                  * (yy - 0.5 * (y_lo_intended + y_hi_intended)))
                  # rel_phase_intended = 0.0 at every point this cycle uses
```

**Four layered checks per point** (a point is CLEAN only if all four
pass; any single failure is a DEFECT at that point, localized by which
check caught it):

1. **Resolution registration.** `sim.lam == cpl_intended` (exact float
   equality — `self.lam` is a direct `float()` cast of the value passed
   to `Sim()`, no arithmetic in between, so this must be bit-exact on
   correct wiring).
2. **Angle-spec registration.** `sim.source_specs[-1]['angle_deg'] ==
   theta_intended` (exact — same reasoning: a direct pass-through).
3. **Placement registration.** `sim.sources[-1]['x'] == x_intended` AND
   `sim.sources[-1]['sl'] == slice(y_lo_intended, y_hi_intended)` (exact).
4. **Phase-ramp/k-vector registration (comprehensive).** `np.allclose(
   sim.sources[-1]['phase'], phase_expected_using_VERIFIED_sim.lam,
   atol=1e-9, rtol=0.0)` — recomputed a SECOND time, this time using the
   already-independently-verified `sim.lam` from check 1 (not
   `cpl_intended` directly) as the closed-form formula itself specifies
   (`k = 2π/self.lam`, not `2π/cpl_intended` — the two are only
   guaranteed identical once check 1 has already passed). This check
   alone is logically sufficient to catch anything checks 1–3 catch (a
   wrong `cpl` or `angle_deg` anywhere upstream necessarily produces a
   different phase array), but checks 1–3 are kept as cheap, independent,
   fault-localizing siblings — exactly this program's own established
   layered-verification habit (Phase 2/Phase 5/Red Team each
   independently re-deriving the same number by a different method).

**`atol=1e-9` justification (not R17-governed, per the compliance header
above).** Both the actual array and the recomputed one are IEEE-754
float64 evaluations of the identical closed-form expression; on correctly
wired input they are expected to be bit-exact (`atol=0`) unless NumPy's
internal operation ordering differs between the two call sites. The phase
values in this cycle's own representative set range up to
`k·sin(θ)·Δy_max ≈ (2π/50)·sin(41.85°)·1880 ≈ 158` radians (`R5`'s widest
y-window: `cfg["y_hi"]−cfg["y_lo"]=3760` cells for `C40_R5`/`G40_R5`
[`R5_BASE_NY − 2·R5_BASE_ABSORB = 3960 − 200`], `Δy_max` its half-span;
confirmed by reading `design_geometry.py::r5_config()`'s own arithmetic
directly, not guessed) — `atol=1e-9` sits roughly eleven orders of
magnitude below this scale, a floating-point-noise floor, not a physical
tolerance.

**Implementation route (Phase 4's own decision; both options specified
here so Phase 2/3 can pick one before any code is written).**

- **Option A (preferred): a minimal, additive, backward-compatible
  parameter.** Add `construct_only=False` to `_run_sim_r3_sigma`/
  `_run_sim_r4_sigma`/`_run_sim_r5_sigma` — when `True`, the function
  returns the constructed `sim` object immediately after
  `add_line_source()`, skipping both the Gate-5 assertion's downstream
  `sim.run(steps)` call and `sc.full_capture(sim)`. Default `False`
  preserves every existing call site bit-exact (a zero-diff guarantee
  verifiable by re-running any one already-filed cell and confirming an
  identical result — a free regression check this option gets for free).
  This lets the gate call the REAL, unmodified-in-behavior production
  functions directly — eliminating the risk named in Idealization 34
  (a hand-duplicated construction sequence drifting out of sync with the
  real call site over future cycles).
- **Option B (fallback, zero diff to any existing file): inline
  replication**, mirroring `gate5_wiring_defect_verification.py`'s own
  established idiom exactly (that script already does not call
  `_run_sim_r5_sigma`; its own negative-control leg builds `Sim(...)` and
  calls `build_article_r5_sigma(...)` directly, inline). If Red Team rules
  Option A an out-of-scope touch to already-"verbatim, zero-diff" call
  sites, Option B is available at identical zero FDTD cost, at the price
  of the duplication risk named in Idealization 34.

Materials construction (`build_article_r{3,4,5}_sigma`, Gate 5's own
`sigma_e` check) is **not exercised** by this gate's core check — confirmed
this session by reading `lab/materials.py` directly: none of
`dielectric_cylinder`/`pec_disk`/`graded_black_shell`/`uniform_lossy_shell`
touches `sim.lam`, `sim.sources`, or `sim.source_specs` (they write only
to `sim.eps_r`, `sim.sigma_e`, `sim.pec`). Skipping materials construction
therefore loses no coverage of the angle/k-vector question and keeps the
check maximally cheap; Gate 5 already independently covers the
materials/`sigma_e` axis at every one of these families' call sites, and
this cycle does not re-derive that.

No new `lab/` engine code and no new suite stage is required — matching
Gate 5's own precedent (an inline runtime assertion plus a companion
fault-injection script, no new trust-suite stage was added at Iteration
71 either). This gate is code that reads already-existing object state; it
adds no new physics to the bench.

### 2b. Fault-injection positive control (queue item 1, mandatory
### per this program's own R-lineage discipline — a check with no
### positive control is not evidence)

Mirrors `experiments/095-.../gate5_wiring_defect_verification.py`'s own
idiom exactly: a **positive control** (correct wiring, gate must report
CLEAN, must NOT flag) and, for the first time in this idiom's three-cycle
history (exp-091's `sigma_max` self-review finding → exp-094's Gate 5 →
this cycle), **three distinct injected-defect scenarios**, not one — because
the registration question spans three independent failure axes (family/
resolution, angle, sign), and a single fault-injection scenario would only
demonstrate the gate catches ONE of them.

| # | Scenario | What is corrupted | Ground truth held by the gate | Must be caught by |
|---|---|---|---|---|
| Positive control | Correct wiring | Nothing — `Sim(cells_per_lambda=dg.R4_CPL[600])`, `add_line_source(angle_deg=39.2, ...)` | 40, 39.2° | Gate reports CLEAN (must NOT flag) |
| FI-A | Family/`cpl` swap | `Sim(cells_per_lambda=dg.R3_CPL[600]=30)` constructed for a call site the gate is told is `R4`-intended (`cpl_intended=40`) | 40 | Check 1 (and, transitively, Check 4) |
| FI-B | Angle swap (adjacent-job mix-up) | `add_line_source(angle_deg=38.69, ...)` at a point the gate is told is intended for `θ=39.2°` — a real, plausible defect shape: an adjacent Rank's own already-committed angle value (`RANK1C_ANGLES[1]`) landing in a `RANK1A_ANGLES[0]`-labeled construction, e.g. via a job-list indexing bug | 39.2° | Checks 2 and 4 |
| FI-C | Sign flip | `add_line_source(angle_deg=-39.2, ...)` where intended is `+39.2°` — since `sin(−x)=−sin(x)`, this negates the entire phase array while leaving its magnitude pattern superficially similar; a magnitude-only check would miss it | +39.2° | Checks 2 and 4 (a check comparing `abs()` values only would NOT catch this — the design in §2a compares signed arrays specifically to guard against it) |

FI-A and FI-B/C are each constructed once (one representative angle from
the R4 family, `θ=39.2°`, is sufficient to demonstrate each failure mode —
this is a discriminator-validation exercise, not a census). **All three
injected scenarios MUST be caught** (flagged as a defect by at least one
of Checks 1–4) for the gate to be judged a genuine discriminator rather
than a rubber stamp — see §5b for the falsifiable prediction and its
consequence if not met.

### 2c. Zero-FDTD bracket-width desk bound (queue item 2)

A pure, already-computable arithmetic comparison — no `Sim` object, no
code execution beyond a calculator, frozen here before any run (§5c gives
the actual numeric answer, computed now, not deferred).

## 3. Parameter table

**Representative registration-check points (queue item 1) — 8 total, all
`(family, θ)` pairs reused verbatim from already-committed job constants
in `experiments/095-t28-r4-ground-truth-sign-control/run.py`, chosen
specifically to avoid introducing any new, undischarged angle choice
(R17's own spirit applied even though R17 itself governs a different
class of quantity — see compliance header):**

| Family | `cpl_intended` | θ (deg) | Provenance (exact source) | `y_lo`/`y_hi`/`x` source |
|---|---|---|---|---|
| `R4` | `dg.R4_CPL[600]`=40 | 39.2 | `RANK1A_ANGLES[0]`, exp-095 `run.py:263` | `dg.R4_CONFIGS["C40_R4"]` |
| `R4` | 40 | 39.4 | `RANK1A_ANGLES[1]`, exp-095 `run.py:263` | same |
| `R4` | 40 | 38.49 | `RANK1C_ANGLES[0]`, exp-095 `run.py:264` | same |
| `R4` | 40 | 38.69 | `RANK1C_ANGLES[1]`, exp-095 `run.py:264` | same |
| `R4` | 40 | 41.6 | `RANK3A_ANGLE`, exp-095 `run.py:268` | same |
| `R3` | `dg.R3_CPL[600]`=30 | 38.4 | `RANK4_ANGLE`, exp-095 `run.py:270` | `dg.R3_CONFIGS["C40_R3"]` |
| `R5` | `dg.R5_CPL[600]`=50 | 41.825 | `RANK2A_ANGLE`/`RANK2B_NATIVE_ANGLES[0]`, exp-095 `run.py:265,267` | `dg.R5_CONFIGS["C40_R5"]` |
| `R5` | 50 | 41.850 | `RANK2B_NATIVE_ANGLES[1]`, exp-095 `run.py:267` | same |

Both configs in each family's pair (`C40_R{n}`/`G40_R{n}`) share identical
`nx,ny,src_x,y_lo,y_hi` by this program's own established congruent-
construction discipline (Gate 3, `A` held bit-identical across the pair,
independently re-verified at every prior R3/R4/R5 cycle) — checking one
member of each pair per angle is representative of both; Phase 4 may
cheaply check both members of all 8 pairs (16 constructions total) at
zero additional design cost if Red Team prefers exhaustive coverage over
the minimum-representative set specified here.

**Fault-injection scenarios (queue item 1, §2b):** 1 positive control + 3
injected-defect scenarios, all at `R4`/`θ=39.2°` (the same point already
in the representative set above), per the table in §2b.

**Zero-FDTD desk bound (queue item 2) — no parameters beyond the
already-filed figures below.**

## 4. T1 escape route

**N/A** — independently re-verified against LOGBOOK.md's own record:
every T28 sub-thread entry from Iteration 46 through Iteration 72 states
T1 route N/A / Checkpoint criterion 2 N/A. This cycle takes no position on
σ(I)/σ(x,t)/angular selectivity/sub-threshold operation, makes no
phenomenon-mechanism claim, and does not touch `REALIZABILITY_MEMO.md`.
Matching every T28 desk/instrument cycle since exp-069, this is pure
INSTRUMENT-VALIDATION work — a construction-time wiring audit and a desk
arithmetic bound, neither making any claim about a material or mechanism.

## Realizability bound

**N/A**, identical reason. `REALIZABILITY_MEMO.md` is not opened, cited,
or re-scored.

## 5. Predicted outcomes, frozen before any run (or, for §5c, before any
## calculation beyond what is already shown)

### 5a. Registration-readback gate outcome (PRIMARY, queue item 1)

**No confident lean stated on CLEAN vs. DEFECT-FOUND** — this is
explicitly, by the reconciled queue's own framing, the single most
fundamental *open* question in this 19-cycle sub-thread; a proposal that
stated a lean here would be manufacturing confidence this program's own
record does not support. Both outcomes are genuinely informative and
neither is treated as a preferred result:

- **CLEAN** (all 8 representative points pass all 4 checks): removes
  construction-time wiring/registration as a live explanation for
  exp-095's own Rank 1c FAIL entirely. Does not, by itself, PROVE genuine
  node migration (Idealization 32) — it eliminates one candidate from a
  currently-two-candidate hypothesis space (registration defect vs.
  migration), leaving migration as the sole surviving explanation among
  the two Red Team's own exp-095 audit named, strengthening (not
  completing) the "2:1 to 3:1, impressionistic" reading already on file.
- **DEFECT-FOUND** (any point fails any check): reprioritizes every
  Iteration-73-queue item below this one — items 3/4/6 would need to wait
  for the defect's scope (is it `R4`-family-wide? angle-specific? shared
  with `R3`/`R5`?) to be understood and fixed before any further FDTD
  spend on this window is trustworthy. A defect found would also require
  auditing which of exp-092 through exp-095's own already-filed
  `results.json` citations rest on the affected call site(s) — named here
  as the immediate next action if this branch fires, not scoped further
  in this Phase-1 document.

### 5b. Fault-injection positive control (queue item 1, MUST-catch)

**Confident lean stated, as this program's own R-lineage discipline
requires:** all three injected-defect scenarios (FI-A, FI-B, FI-C) MUST
be caught (flagged by at least one of Checks 1–4), and the positive
control MUST NOT be flagged. This is not a hypothesis with genuine
uncertainty — it is a correctness requirement of the check's own design,
verifiable by inspection of §2a's four checks before any code runs: FI-A
is caught by Check 1 (`sim.lam` will read 30, not the intended 40); FI-B
and FI-C are each caught by Check 2 (`angle_deg` mismatch, exact) and
independently by Check 4 (the resulting phase array will differ
substantially — for FI-B, because `sin(38.69°)≠sin(39.2°)`; for FI-C,
because the entire array negates). **If any of the three is NOT caught,
the registration-readback gate itself is not a genuine discriminator and
§5a's CLEAN/DEFECT-FOUND result must not be trusted until the gate's own
design is fixed and re-verified** — stated plainly, matching this
program's own standard for a check with no working positive control.

### 5c. Zero-FDTD desk bound, computed now (queue item 2)

**Already-filed migration figures** (re-derived this session directly
from committed `results.json` files, not restated from LOGBOOK prose):

| Crossing pair | `cpl=20` location | `cpl=30` location | Migration magnitude | Provenance |
|---|---|---|---|---|
| Lower window | 40.265420° | 40.071838° | **0.193582°** (≈0.194°) | `experiments/090-.../results.json::q8.crossings_deg[2]`; `experiments/092-.../results.json::rank1.crossing_report` (lower) |
| Upper window, crossing 1 | 41.460901° | 41.781067° | **0.320166°** (≈0.320°) | `experiments/090-.../results.json::q8.crossings_deg[3]`; `experiments/092-.../results.json::rank1.crossing_report` (upper #1) |
| Upper window, crossing 2 | 41.460901° | 41.837653° | **0.376752°** (≈0.377°) | same `cpl=20` anchor; `experiments/092-.../results.json::rank1.crossing_report` (upper #2) |

All three are `cpl=20→cpl=30` migrations (`RATIO` 1.0→1.5). Rank 1c's own
tested transition (`cpl=20→cpl=40`, `RATIO` 1.0→2.0) is a *larger*
discretization jump than any of these three already-measured figures —
so treating `[0.194°, 0.377°]` as the plausible scale for a comparable
`cpl=40` migration is, if anything, an optimistic (lower) estimate, not a
conservative one; this is stated as an explicit limitation, not
smoothed over (Idealization 36).

**Computed containment ratios** (candidate bracket half-width `δ` ÷
established migration magnitude `M`; a bracket of half-width `δ` reliably
detects a migration of magnitude `M` only if `δ` comfortably exceeds `M`,
by the same margin-based logic R13/R15 already established empirically
for this sub-thread's own classification questions — misclassifications
at ≤1.48×, reliable classification only at ≥2.17× in that unrelated but
structurally analogous prior finding, cited here as a suggestive
benchmark, not a formal transplant — Idealization 37):

| Candidate `δ` (window is `θ₀±δ`) | vs. `M`=0.194° | vs. `M`=0.320° | vs. `M`=0.377° |
|---|---|---|---|
| ±0.1° (Rank 1c's own tested width) | 0.52× — MISSES | 0.31× — MISSES | 0.27× — MISSES |
| ±0.2° | 1.03× — razor-thin, barely covers only the smallest figure | 0.63× — MISSES | 0.53× — MISSES |
| ±0.4° | 2.07× — comfortable | 1.25× — thin | 1.06× — razor-thin, comparable fragility to this program's own R13/R15 empirical failure band |
| ±0.5° | 2.58× — comfortable | 1.56× — moderate | 1.33× — below the ~2× benchmark, but the most defensible of the three candidates |

**Answer:** at θ₀≈38.590°, **±0.2° is insufficient** — it would have
missed two of the three already-filed migration figures entirely and only
barely covers the smallest one. **±0.4° comfortably contains the smallest
two figures but leaves only a 6% margin against the largest
(0.377°)** — a margin this sub-thread's own prior empirical work (R13/R15)
has repeatedly shown to be unreliable in a structurally similar
margin-based classification setting. **±0.5° is the narrowest of the
three candidates that clears every already-filed figure by more than
30%**, though still short of the ~2× comfort level this program has
established elsewhere. **This computed conclusion independently
corroborates — without having read it in advance of doing this
calculation — exp-095's own already-queued item 4 design** ("directionally
weighted toward lower θ... covering at minimum 37.9°–38.5°, extended to
38.9° for symmetric coverage," an asymmetric half-width of roughly
0.3°–0.7° around 38.590°): that design's own low-side reach (0.69°)
exceeds every candidate examined here, and its high-side reach (0.31°)
sits between the ±0.2° and ±0.4° candidates — consistent with, not
contradicted by, this desk bound's own conclusion that ≥0.5° single-sided
half-width is the minimum defensible choice absent a specific reason to
weight one side more than the other.

## 6. Idealizations

**Carried forward from exp-095's own list, cited by original number:** 1
(2D TMz, 600nm only), 7 (no constraint-1/2/3/4 test, no T1 position), 17
(the `R3`/`R4`/`R5` families share one mechanical `r{n}_config()` recipe,
not three independent discretization schemes — directly relevant here: a
registration defect found in one family's shared construction code would,
by the same logic, be expected in all three).

**New this cycle:**

31. This gate checks CONSTRUCTION-TIME registration only (the `Sim`
    object's own stored state immediately after `add_line_source()`), not
    RUN-TIME numerical behavior accumulated during `sim.run()`. Run-time
    numerical dispersion is a separate, already-bounded question
    (ELECTROMAGNETISM's Phase-5 reviews, exp-093/094/095: Yee-grid
    dispersion independently ruled out at 25×–78× too small to explain
    the observed node-migration/FAIL signature). A CLEAN result from this
    cycle does not re-derive or strengthen that bound; it removes a
    different candidate explanation (pre-run wiring) from consideration.
32. This gate does not itself re-run, relocate, or adjudicate Rank 1c's
    own 38.590° node, and a CLEAN result does not, by itself, prove
    genuine node migration — it narrows the live hypothesis space from
    two named candidates (registration defect vs. migration) to one,
    which is a materially different, weaker claim than "migration is
    proven." Red Team's own exp-095 "2:1 to 3:1, impressionistic, not a
    computed posterior" framing is not converted into a computed
    posterior by this cycle either way.
33. The gate's own independent recomputation (§2a) uses the identical
    closed-form formula documented in `lab/fdtd2d.py::add_line_source`'s
    own docstring. It can detect a defect in how that formula's INPUTS
    were wired (the registration question this cycle exists to answer);
    it CANNOT detect a defect in the formula's OWN correctness (e.g. a
    latent sign or trig error that has stood unnoticed since the
    angle-ramp machinery's own introduction) — that is the responsibility
    of the trust suite's own stage-1/stage-9 regression gates, cited in
    the same docstring, which this cycle does not re-run or re-derive.
34. Whichever implementation route Phase 4 chooses (§2a, Option A or B),
    the gate's own replication or thin wrapper of each family's
    construction sequence must be kept in lock-step with the real
    `_run_sim_r{3,4,5}_sigma` call sites. A future cycle that edits those
    call sites (e.g. adds a new source parameter) without updating this
    gate could produce a stale CLEAN reading that no longer describes the
    actual production code path — the same class of duplication risk
    `gate5_wiring_defect_verification.py` already carries under Option B,
    which Option A is specifically designed to reduce (not eliminate:
    Option A's own `construct_only` branch could itself drift from the
    `construct_only=False` branch if a future edit touches one and not
    the other).
35. The 8-point representative set (§3) reuses angles already committed
    in exp-095's own job constants specifically to avoid introducing a
    fresh, undischarged angle choice — it is not an exhaustive audit of
    every angle this sub-thread has ever measured across 19 cycles. A
    CLEAN result is evidence about the shared construction CODE PATH for
    each family (the same few lines build every angle in that family), not
    a point-by-point certification of every individual historical
    measurement's own angle value.
36. The desk bound's own "comparable scale" assumption (§5c) — that a
    `cpl=20→40` migration falls in the same `[0.194°,0.377°]` range
    already measured for the smaller `cpl=20→30` step — is stated
    explicitly as optimistic, not conservative, since `cpl=40` represents
    a larger discretization change than `cpl=30` did from the same native
    baseline. No rigorous scaling law between migration magnitude and
    `RATIO` is fit or claimed; this is an order-of-magnitude sanity bound,
    matching the standard exp-095's own Idealization 29 already set for
    this class of calculation.
37. The R13/R15 margin-based comfort benchmark (≥2.17× reliable, ≤1.48×
    unreliable) cited in §5c's table is drawn from an unrelated
    measurement domain (a `ratio_k` decade classifier's own denominator
    floor gate) and is offered here only as a suggestive, structurally
    analogous benchmark for interpreting a containment-ratio margin — not
    a formal transplant of that finding's own statistical machinery to a
    geometric bracket-sizing question.

**Carried idealizations banner (mandatory at both this section and §5,
per the Iteration-65 CHECKPOINT's non-discretionary rule): every
prediction in §5 is governed by Idealizations 1/7/17 plus this cycle's own
31–37.**

## 7. Estimated FDTD call count and wall-time budget

**0 FDTD calls.** Every registration-check construction (§2a, 8
representative points plus the 4 fault-injection scenarios of §2b, 12
`Sim` constructions total) stops before `sim.run()` is ever invoked — the
quantities under test (`sim.lam`, `sim.source_specs`, `sim.sources[-1]`)
are fully determined at construction time and do not change during
integration. The desk bound (§2c/§5c) uses only already-filed numbers.
This is a genuine zero, not a "near-zero" rounding of a small integer —
stronger than Gate 5's own precedent, which spent a cheap 200-step real
run for its own positive control (`experiments/095-.../
gate5_wiring_defect_verification.py`, confirming the correctly-wired call
site doesn't crash under real integration). **Optional, not required:**
Phase 4 may add one cheap real `sim.run()` (a few hundred steps, a
handful of calls, seconds of wall time) mirroring that same precedent, as
an extra sanity check that a registration-CLEAN `Sim` object also
integrates without crashing — this cycle's own design does not need it to
answer the registration question and does not budget for it, but it is
flagged as an available, near-free option if Phase 2/3 want the extra
assurance.

**Wall time:** dominated by Python/NumPy object construction and array
comparison over 12 `Sim` objects (each allocating `nx×ny` arrays at the
relevant family's grid size — up to `R5`'s ~900×3960 cells — but never
stepping the FDTD update loop) plus a handful of already-filed-number
lookups for §5c. Estimated **under 60 seconds wall time total**, several
orders of magnitude below this sub-thread's own established ~100–150
CPU-minute per-cycle band — the cheapest cycle on record for this
sub-thread, matching the reconciled queue's own framing ("near-zero
marginal FDTD cost, code-only").

## 8. What this cycle does NOT do (explicit scope boundary)

Per the reconciled queue's own sequencing: items 3 (bracketing the other
three `cpl=20` nulls at `cpl=40`, ~24 calls, EM's proposal) and 4 (a
reconciled node-bracketing re-run at 38.590°, ~8–16 calls, informed
directly by this cycle's own §5c desk bound) are gated on this cycle's own
§5a outcome and are explicitly NOT run this cycle. Item 6 (resuming the
`cpl=50`/`R5` interior sweep) remains deferred, unanimous across every
seat that has addressed sequencing since exp-095 — not scheduled here.
This document proposes exactly items 1 and 2, sized and gated as the
reconciled queue itself specifies.
