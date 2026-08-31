# PHASE 5 — REVIEW · MATERIALS & METAMATERIALS (blind) · exp-095 · Panel Iteration 72

*Fresh sub-agent, MATERIALS & METAMATERIALS charter ("sub-wavelength
structure; what could physically realize the proposed optical behavior.
Owns the realizability bound — published / plausible /
unobtainium-with-parameters"). Read in full: PANEL.md; LOGBOOK.md
(RULED OUT R1–R16 verbatim, ESTABLISHED, LIVE THREADS T1–T27, and T28's
complete history Iterations 46–71 in full, including my own Iteration-68
exp-091 self-review that founded R15 and my own Iteration-71 exp-094
review that proposed the R15 addendum this cycle exists to discharge);
the complete exp-095 record (`phase1_proposal.md`, all five Phase-2
critiques, `phase2_redteam_audit.md`, `NOTES.md`, `run.py`,
`run_output.txt`, `results.json`,
`gate5_wiring_defect_verification_result.json`,
`gate5_wiring_defect_verification.py`); the R5 block in
`experiments/069-.../design_geometry.py`; my own Phase-2 critique
(`phase2_critique_materials.md`) for continuity. Every load-bearing
number below was independently re-derived from committed source this
session, not taken on any document's word. Blind to every other Phase-5
seat's review and to the Red Team final audit.*

## Verdict: **CONCUR**

The gate did exactly what it was built to do, and it did so on data I
independently re-verify as bit-exact and correctly classified. Given my
own Phase-2 critique — that the `R5` family cannot, by construction,
discharge R15's addendum regardless of what it reads — the fact that
Rank 2/3 never actually spent their ~68 of the cycle's 86-call PASS-path
budget is not a loss for this seat's charter; it is 68 calls this
sub-thread did not need to spend to learn that MATERIALS' own concern
was moot this cycle. What the outcome leaves genuinely unexamined is not
realizability (this cycle correctly stays N/A on that) but a narrower,
checkable question the record does not yet ask: whether Rank 1c's FAIL
is evidence of a wiring defect at all, or simply the already-documented
node-migration effect landing outside a bracket narrower than its own
established precedent. See §3.

## 1. Independent re-verification of the Rank 1c numbers, from `results.json` directly

Read `results.json::rank1.rank1c` directly, not `NOTES.md`'s prose
restatement of it:

| θ | `delta_scene` | `floor_pass` | sign |
|---|---|---|---|
| 38.49° | −1.516840×10⁻³ | `true` | negative |
| 38.69° | −2.538531×10⁻³ | `true` | negative |

Both against the printed `r13_floor_gate.floor = 1.917438×10⁻⁴`: margins
7.91× and 13.24× respectively — comfortably floor-clearing by this
sub-thread's own R13 standard, not a borderline call either way.
**Same sign, both floor-clear — bit-exact match to the pre-registered
FAIL criterion** (`NOTES.md`: "FAIL = both floor-clear but SAME sign").
`rank1.proceed_gate: false` and the top-level `proceed_gate: false` are
consistent with each other and with `rank2`/`rank3` both correctly
recorded as `{"skipped": true, "reason": "Rank 1 combined go/no-go gate
did not PROCEED"}`. `total_fdtd_calls: 20 = rank1_calls(16) +
rank4_calls(4) + rank2_calls(0) + rank3_calls(0)` — arithmetic checks.
I also independently re-verified Rank 1a (both angles negative,
`floor_pass=true`, "PASS") and Rank 4 (`|delta_scene|=2.939×10⁻⁶ ≪
floor=1.917×10⁻⁴`, `floor_pass=false` → correctly `Y=null`, "NEITHER" is
the only defensible label). **No arithmetic or gate-logic defect found
anywhere in this cycle's headline figures.**

## 2. Is skipping Rank 2/3 the right outcome, from my own Phase-2 critique's angle?

My own blind Phase-2 critique (`phase2_critique_materials.md`) argued
that `R5` (`cpl=50`) is drawn from the *identical* mechanical
`r{n}_config()` recipe as `R3`/`R4` — only Gate-3-exact ratios (`cpl` a
multiple of 10) are reachable from it, `R5_RATIO=2.5` continues the same
`1.5→2.0→2.5` arithmetic progression, and a recipe-level systematic (if
one exists) reproduces at every ratio the recipe can produce by
definition. Red Team's own independent re-derivation (`phase2_redteam_
audit.md` §1, attack #3) confirmed this exactly and tightened the
underlying condition (`78·cpl/20` is integer iff `cpl` is a multiple of
10 — I re-verified this arithmetic identity independently and it is
correct). The Phase-3 synthesis adopted the fix I asked for almost
verbatim: `NOTES.md`'s mandatory-fix item 4 states, non-buried, "No
Rank-2b outcome... discharges R15's addendum on its own" — and this
sentence is printed to `run_output.txt` and persisted into
`results.json::r4_r5_family_disclaimer` even though Rank 2b never ran,
so a future reader who only sees the skip still gets the caveat that
would have governed its result.

Given that, this cycle's outcome is the right one **from this seat's own
charter specifically**: the ~529–595 CPU-minutes (71% of the PASS-path
budget) that would have bought a `cpl=50` reading were never spent, and
by my own Phase-2 argument that reading — CONFIRM, REFUTE, or AMBIGUOUS
— would not have been admissible as evidence toward closing R15 on its
own regardless of which way it came out. The gate did not merely save
money; it saved money on the specific item this seat had already argued,
before any run, could not deliver what it was funded to deliver. That is
the gate working as intended, not a near-miss.

**What this does NOT mean**: it does not mean nothing was lost. Two
things genuinely were, neither a realizability finding:

- The native-sigma `R5` comparator leg (mandatory fix #3, EM's own
  catch) and the `cell_metrics_r5`/Rank-2 energy-channel check
  (mandatory fix #8, THERMODYNAMICS' own catch) were built correctly
  into `run.py` (§4, below) but never exercised against real Rank-2
  angles — those fixes are proven present in code, not proven correct
  in practice, until a future cycle actually runs Rank 2.
- The companion desk bound (mandatory fix #5, my own critique's own
  remedy (b)) is explicitly gated on "Rank 2b's classification differs
  from exp-094's own filed `cpl=40` classification" — since Rank 2b
  never ran, this bound was never computed either. My own proposed
  quantitative check of whether the `cpl=45`-scale radius drift could
  plausibly explain an observed reversal remains, itself, undischarged
  — not because it was declined, but because its own trigger condition
  never fired. This is a genuinely open item, not resolved by this
  cycle's HALT.

## 3. The R5 geometry block: uncorrupted, available — and, in one narrow
## sense, already smoke-tested with real FDTD, not merely committed-and-idle

**Uncorrupted and independently re-verified, constant by constant.**
I recomputed every entry in `design_geometry.py`'s R5 block
(`experiments/069-.../design_geometry.py`, lines 313–399) from the raw
`R5_RATIO=2.5` substitution, not by trusting the inline comments:
`R5_R_OUT=round(78×2.5)=195` (exact, no rounding — `195` reproduces);
`R5_GUARD_OUT=round(185×2.5)=round(462.5)` — Python's banker's rounding
sends `462.5` to `462` (nearest even), matching the committed value and
its own comment; `R5_BASE_PLANE_X=round(77×2.5)=round(192.5)→192`, same
rounding rule, matches; `SIGMA_R5_CORRECTED=0.5/2.5=0.2` exact;
`L_GEOMETRIC_M_R5=195×1.2×10⁻⁸=2.34×10⁻⁶` m, bit-identical to native/`R3`/
`R4`'s own `2.34×10⁻⁶` m to the precision printed. `python3 -c
"ast.parse(...)"` on the full file confirms valid syntax, and `grep -c
"^R5_RATIO"` returns exactly 1 — no duplicate or shadowed definition.
The module's own `assert` statements (Gate-3/4-equivalent checks
embedded directly in `design_geometry.py`, e.g. `assert abs(
L_GEOMETRIC_M_R5 - L_GEOMETRIC_M_R4) < 1e-12`) execute at import time —
since `run.py` completed this cycle and `results.json::gates.gate3_l_
geometric_bit_identity.pass_=true`, these module-level asserts already
fired successfully once, for real, this cycle. **The block is correct
and load-bearing-ready for a future cycle to import without
modification.**

**Not merely untouched-and-idle, though: it was exercised end-to-end,
once, with real FDTD, independent of Rank 2's own skip.** I read
`gate5_wiring_defect_verification.py` directly rather than trusting its
own docstring's claim. Its "positive control" calls
`m._run_sim_r5_sigma(cfg, 41.825, 200, True, m.dg.SIGMA_R5_CORRECTED)`
— this is not a stub: `_run_sim_r5_sigma` (`run.py` lines 295–323)
constructs a real `lab.fdtd2d.Sim` object at the genuine `R5_CPL=50`
grid density, calls `build_article_r5_sigma` (real `pec_disk` +
`graded_black_shell` calls against `PEC_R_R5`/`R5_R_OUT`), and then
`sim.run(200)` — a genuine, if short (200 of the settled 7000 steps),
FDTD loop. `gate5_wiring_defect_verification_result.json` records
`control_pass: true` (correct wiring ran without raising) and
`injected_defect_pass: true` with the literal caught
`AssertionError` text (`"...sim.sigma_e[shell_mask].max()=0.5 vs
sigma_max=0.2"` — the exact R15-founding defect shape, correctly
detected). I confirmed via `grep` that `run.py`'s own `run_block_r5`/
`run()` function is never called when `proceed_gate=False` (the
`if not proceed_gate:` branch at line 727 sets `rank2 =
dict(skipped=True, ...)` directly, bypassing every R5 call site) — so
the *substantive* Rank-2 science genuinely never ran, exactly as this
cycle's own accounting states. But the *fault-injection verification*
script is a separate process (its own docstring: "NOT executed by the
authoring agent" during Phase 3, "to be RUN for real during Phase 4"),
and its result file's presence and specific content (a real caught
`AssertionError` string, not a hand-typed placeholder) indicate it *was*
actually run, at real (if abbreviated) FDTD cost, as its own docstring
required. **Net finding: the `R5` construction code path is not merely
syntactically present — it has been confirmed to execute correctly on a
real `Sim` object, including under fault injection, even though no
angle in the cycle's own scientific sweep (Rank 2a/2b) was ever
measured.** A future cycle reusing this block inherits a family that is
geometrically verified, sigma-verified, and now run-time-wiring-verified
— strictly stronger footing than "committed but never touched," though
still short of "validated by a real physics reading," which remains
exactly as absent as the FAIL correctly left it.

## 4. Does Rank 1c's FAIL say anything about REALIZABILITY? Honestly: no.

Answering this directly, because the charter explicitly asks me not to
force an angle that doesn't apply. This cycle is pure instrument
recalibration — `NOTES.md`'s own T1-route and realizability-bound
sections both state N/A, and I find nothing in the record that smuggles
a materials/mechanism claim past that disclaimer. Rank 1c's FAIL is a
statement about whether a coherent-interference *bookkeeping quantity*
(`delta_scene`, a difference of two FDTD-measured contrasts between
congruent numerical configs) changes sign inside a ±0.1° angular
window at one grid density — a question entirely about discretization
and instrument behavior, resolved or not, with zero dependence on any
material property, absorption law, or sub-wavelength structure choice.
`REALIZABILITY_MEMO.md` is correctly never opened. There is no published/
plausible/unobtainium-with-parameters call to make here, because there
is no candidate physical mechanism on the table this cycle — and saying
so plainly is more useful to the record than manufacturing a bound that
doesn't exist.

**The one place my charter does have standing, and where the broader T28
sub-thread remains silent, is one level up from this cycle.** *If* the
~2.84° `delta_scene` periodicity T28 has chased since Iteration 46 is
eventually confirmed as a genuine physical effect (not a discretization
artifact) — the question this entire R3/R4/R5 resolution-ladder exists
to settle — MATERIALS' own charter question would then become live for
the first time in this sub-thread's 19-cycle history: what sub-wavelength
structural feature of the `graded_black_shell` profile itself (a smooth
`σ(r)` grading from `r_in` to `r_out`, no periodic structure anywhere in
its own definition) could plausibly produce an angular interference
period at that scale? Two candidate mechanisms have already been tested
and REFUTEd (Iteration 52's single-wall and two-wall boundary-reflectance
echo models, on a phase convention independently confirmed correct) —
but neither of those was a *materials* mechanism in this seat's sense;
both were domain-boundary (PML-wall) reflectance models, not shell-profile
structure. No cycle in this sub-thread has yet asked whether the graded
profile's own functional form (`_graded_black`'s `s=d³(10−15d+6d²)`,
independently re-derived by my own exp-094 review to force
`max(σ)=σ_max` exactly at the inner edge) could itself support a
resonant or quasi-periodic sub-structure at the observed scale. This
remains open regardless of this cycle's outcome — flagged here as a
standing, not urgent, item, since the sub-thread's own current-and-correct
priority is still establishing whether the feature is physical at all
before asking what physical structure could produce it.

## 5. Sharpest finding — the ±0.1° bracket is narrower than this
## sub-thread's own already-documented node-migration precedent

This is my own independent contribution, not a restatement of anything
in the Phase-2 record or `NOTES.md`'s own Idealization 28 (which
correctly flags that Rank 1c is "a coarser recovery test... not a full
free-period fit" but does not quantify against a specific number
already on the books).

Rank 1c brackets the established `cpl=20` null at `θ₀≈38.590230°`
(`results.json::rank1.rank1c.theta0`, re-derived from `experiments/
090-.../results.json::q8.crossings_deg`) with a **±0.1°** window
(38.49°/38.69°). But this sub-thread's own record already documents,
for a *different*, better-instrumented null on the *same* `delta_scene`
curve, how far a zero-crossing moves between coarser and finer grids:
the lower crossing near 40°, independently located at both `cpl=20`
(`40.265420°`, `experiments/090.../results.json::q8.crossings_deg`) and
`cpl=30` (`40.071838°`, `experiments/092.../results.json::rank1.
crossing_report.lower_crossing_cpl30`), migrated by **0.193582°**
between those two resolutions — I recomputed this directly from both
files' own primitives; it is not hand-typed from any prior citation.
That is already **larger than Rank 1c's own ±0.1° half-width**, for a
*smaller* resolution jump (`RATIO` 1.0→1.5) than the one this cycle
actually tests (`RATIO` 1.0→2.0, a full doubling). The upper-window
crossing near 41.4°/41.8° migrated even further over the identical
`cpl=20→30` step (`41.460901°→41.781067°`, a **0.320166°** shift, same
recomputation method).

I draw two conclusions from this, neither available anywhere else in
the record I read:

1. **A FAIL at Rank 1c is not, on its own, more consistent with "the
   node vanished/reversed" than with "the node migrated beyond a ±0.1°
   window exactly as its own sub-thread's other two located nulls
   already have, at a smaller resolution step than this one."** Both
   38.49° and 38.69° reading the *same, comfortably floor-clearing*
   negative sign is equally compatible with a null that has simply
   moved to, say, 38.2° or 38.9° at `cpl=40` — ordinary (if still
   scientifically interesting) node migration, not a registration
   defect, and not evidence the θ₀≈38.59° feature has disappeared. The
   pre-registered FAIL label ("the established node appears to have
   vanished from this window in the `R4` family — a genuine integrity
   finding") is defensible as the conservative, house-discipline-
   correct label given only what this cycle measured, but the record as
   filed does not distinguish "vanished" from "moved beyond a window
   that was, by this sub-thread's own prior evidence, already too
   narrow to reliably catch a migration of this class."
2. **This also means Rank 1c was under-powered by construction in a way
   distinct from, but complementary to, QUANTUM's own Phase-2 attack**
   (the sign-check-at-antinodes-is-phase-blind argument, which the
   Rank-1c addition itself was built to answer). QUANTUM's point was
   about *where* to test (near a node, not far from one). Mine is about
   *how wide a window near that node is enough* — and the answer, using
   only numbers already in this program's own committed record before
   this cycle ran, is that ±0.1° is tighter than the smallest
   already-observed migration for a comparable resolution step on the
   same curve.

This does not overturn the FAIL, and does not itself argue Rank 2/3
should have run — my own §2 argument that `R5` cannot discharge R15
either way still stands, independent of this finding. It does mean a
future cycle re-testing node-bracketing at `cpl=40` (or any new
resolution) should size its bracket against this sub-thread's own
already-measured migration magnitudes (≥0.19°–0.32° at a smaller
`RATIO` step), not a round ±0.1° chosen for cost, and should treat
"FAIL, same sign" as ambiguous between disappearance and migration
unless the window is widened enough to rule migration out.

## Ranked recommendation for Iteration 73

1. **Re-run a node-bracketing recovery check at `cpl=40`, same 38.590°
   null, with a window sized against this sub-thread's own documented
   migration precedent** (≥0.4°–0.5° half-width, not ±0.1°) — the
   cheapest, most direct way to learn whether Rank 1c's FAIL was
   disappearance or an under-bracketed migration, before either
   conclusion is treated as settled. Zero new machinery; reuses
   `_run_sim_r4_sigma` verbatim at a few more angles.
2. **If (1) locates a genuine `cpl=40` crossing anywhere nearby, gate
   Rank 2's own future revival on it** exactly as this cycle's Rank 1
   was meant to gate Rank 2 — the combined go/no-go logic was sound in
   design; it should simply be re-run against a control window wide
   enough to be decisive, not narrowed for cost the first time and then
   trusted as if it weren't.
3. **Do not spend on the `cpl=50` (`R5`) family again until a
   qualitatively different discretization exists**, per my own Phase-2
   finding, re-confirmed unchanged by this cycle's outcome: no ratio
   drawn from the shared `r{n}_config()` recipe can discharge R15's
   addendum on its own. If a third resolution point is still wanted for
   trend-fitting purposes only (not for R15 discharge), it costs nothing
   additional to build — the R5 block is proven correct and available,
   per §3 — but its result should be labeled exactly as
   necessary-but-insufficient going in, matching this cycle's own
   correctly-adopted framing, not re-litigated from scratch.
