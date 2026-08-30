# PHASE 5 — REVIEW · MATERIALS & METAMATERIALS (blind) · exp-094 · Panel Iteration 71

*Fresh sub-agent, MATERIALS & METAMATERIALS charter. Read in full: PANEL.md;
LOGBOOK.md (RULED OUT R1–R15 verbatim, ESTABLISHED, LIVE THREADS T1–T28 in
full, including my own seat's Iteration-68 exp-091 self-review that founded
R15); PLAN.md's Current-state section; the complete exp-094 record
(`phase1_proposal.md`, all five Phase-2 critiques, `phase2_redteam_audit.md`,
`phase3_synthesis.md`, `NOTES.md` in full, `run.py`, `results.json`,
`run_output.txt`). Independently re-derived from primary source this
session (not taken on any document's word): `lab/materials.py::
graded_black_shell`/`_graded_black`/`_grids`, `run.py`'s own
`_run_sim_r4_sigma`/Gate-5 implementation, `results.json`'s `gates`/`rank1b`/
`rank3` blocks, `design_geometry.py`'s R4 block (the committed diff), and
this cycle's own git history (`git log`/`git show` on the experiment
directory). Blind to every other Phase-5 seat's review and to the Red Team
final audit.*

## Verdict: **CONCUR-WITH-GAP(S)**

The science holds up to independent re-derivation — Gate 5 is a genuine,
correctly-wired discriminator, and I find no construction bug in the `R4`
family itself. But two independently-confirmed, previously-uncaught record
defects survive into the permanent record, and the disclosed shared-recipe
idealization (17) is not being read as sharply as this cycle's own actual
result — a *full* reversal, not a partial drift — demands.

## 0. My own Phase-2 finding's fix, independently re-verified (not on faith)

**Gate 5 landed correctly and is genuinely discriminating.** I traced
`_run_sim_r4_sigma`'s inline assert against `lab/materials.py`'s own
`graded_black_shell`/`_grids` source, not against any document's citation of
it: `shell_mask = (rr >= PEC_R_R4) & (rr <= dg.R4_R_OUT)` on the `ez`-point
grid is *exactly* `graded_black_shell`'s own `shell = (rr >= r_in) & (rr <=
r_out)` indexing when called with `r_in=PEC_R_R4, r_out=R4_R_OUT` — not an
approximation. I further verified the assert's own target is mathematically
forced, not merely empirically expected to pass: `_graded_black(d)` returns
`sig = 0.5*s²` with `s=d³(10−15d+6d²)`, so `sig` peaks at exactly `0.5` at
`d=1` (the inner edge, `r=r_in`), and `graded_black_shell` sets
`sigma_e[shell] += sigma_max*sig/0.5` — so `max(sigma_e[shell_mask])` is
forced to equal `sigma_max` *exactly*, up to floating point, whenever the
correct constant is passed. This means Gate 5 is not a coin-flip check; a
wiring bug (wrong constant at the call site) would deterministically be
caught. `results.json::gates.gate5_runtime_sigma_array` reports
`pass_=True, n_article_calls_checked=16` — I independently recomputed this
count from the job tables (`jobs_r1a`: 2 steps × 2 configs = 4 article
calls; `jobs_r1b`: 2 configs × 6 angles = 12 article calls; 4+12=16) and it
reproduces exactly. `run_output.txt` lines 79/116 confirm both sub-batches
"completed their inline runtime sigma_e/sigma_max assert without raising."
**This part of NOTES.md's claim is fully substantiated, not merely
asserted — I verified it, I did not take it on faith.**

**But one specific, adjacent claim is NOT substantiated by anything in the
committed record, and should not have entered NOTES.md as fact.** Both the
Result section and Learned #4 state Gate 5 was "independently confirmed
during Phase 4 to be a genuine discriminator... by injecting a simulated
R15-style wiring defect into a standalone test harness during Phase 4
(correctly raised `AssertionError`)." I grepped `run.py`, `run_output.txt`,
and `results.json` for any trace of this event ("harness," "injected,"
"simulated," "wiring") — zero matches, anywhere. I then checked `git log`
and `git show` on every commit touching this experiment directory — no
commit ever added, modified, or removed a test-harness file of any kind.
**This specific verification event has no corroborating artifact anywhere
in this repository.** It may well have happened as an ephemeral,
uncommitted check during the shift — but as written, it is a hand-asserted
claim about a verification methodology entering a permanent record, with
nothing behind it a future reader (or this review) can reproduce. This is
the identical *shape* of gap R4 (this house's own standing rule) exists to
catch — a self-consistency/verification claim must be producible by
invoking actually-committed machinery, not asserted from memory of a
session — applied here to a qualitative "we tested the test" claim rather
than a numeric figure. It happens to be non-load-bearing (my own
independent derivation above shows the gate genuinely discriminates, on
different, reproducible grounds), but the house discipline is that a wrong
or unverifiable claim does not get a pass for being non-binding.

## 1. Does the new `R4` family genuinely preserve sub-wavelength structural realism at the coarser-to-finer ratio?

**On every checkable dimension, yes — I find no construction bug.**
Independently re-verified: shell thickness `(R4_R_OUT−PEC_R_R4)/cpl =
96/40 = 2.4λ`, bit-identical in wavelength terms to native (`48/20=2.4λ`)
and `R3` (`72/30=2.4λ`); core/shell ratio `60/156=0.3846`, identical to
native/`R3`'s `30/78=45/117=0.3846`; `L_GEOMETRIC_M_R4=2.34×10⁻⁶` m,
bit-identical to native and `R3` (`results.json::gates.gate3`, `dev=0.0`).
`R4_RATIO=2.0` is in fact a *cleaner* congruent rescale than `R3_RATIO=1.5`
was — every `R4` base constant is an exact-integer scaling with zero
rounding, whereas `R3`'s own recipe forced two half-integer roundings
(`PLANE_X`: `77×1.5=115.5→116`; `GUARD_OUT`: `185×1.5=277.5→278`), a small
(~0.4%) geometric inexactness `R3` has always carried and `R4` does not.
`SIGMA_R4_CORRECTED=0.25` is independently re-derivable from
`fdtd2d.py`'s own loss-update coefficient (EM's Phase-2 finding, which I
independently spot-checked against the `graded_black_shell` formula above
and found consistent), not merely pattern-matched — and Gate 5 (above)
confirms it actually lands in the constructed object. So: the *shape* of
the object at `cpl=40` is faithful to the design intent, and the
wiring that wasn't checked at `R3`'s birth (R15's founding defect) is now
checked here.

**But "faithful mechanical rescale of R3's own recipe" is not the same
claim as "an independent test of continuum convergence," and Idealization
17 (correctly disclosed) does not go far enough given what this cycle
actually found.** `R4` is generated by substituting `R4_RATIO` into the
*identical* `r3_config()` formula — same taper-length convention, same
`ABSORB`/PML sizing-in-cells convention, same box-clearance convention,
same object-to-boundary placement rule. Any resolution-*independent*
systematic this recipe carries (not a grid-density effect at all, but a
choice baked into the formula itself) reproduces unchanged in `R4`. That
would be a tolerable risk for a *slowly-varying* quantity. It is not a
tolerable risk for the *specific* quantity measured here: `delta_scene` at
this near-null is an established (R13/R14) subtractive-cancellation
residual between two nearly-identical PAD-phase-timing configs, and this
program's own T10 finding is exactly that such near-field, point-probe-like
channels are sensitive to how the curved shell boundary staircases against
the underlying Yee grid — a sub-cell registration effect that is, by
construction, *different* at `cpl=30` and `cpl=40` (the physical circle
sits at different fractional-cell offsets at each density) but need not be
*monotonically converging* between them. Two points generated from one
shared formula cannot distinguish "the true continuum value is near this
sign and cpl=30 badly under-resolved it," from "this bench's own
discretization scheme has a persistent, recipe-level artifact that
produces different-but-equally-wrong staircasing noise at each density,"
from "the feature genuinely oscillates and neither point is close to
converged." **A full sign-and-classification reversal at all six sampled
points — not a partial drift at some and stability at others — is exactly
the outcome pattern that is equally consistent with all three of those
readings.** I do not believe this cycle's own data can adjudicate between
them, and I do not think NOTES.md's own Idealization 17/Next#1 language
("not independent confirmations... a `cpl=50` check would show whether the
sequence is converging") is wrong, but it under-states how little either
`cpl=30` or `cpl=40` should currently be trusted individually — the correct
reading right now is that **both readings are equally suspect**, not that
`cpl=40`'s reversal is the more-refined, more-trustworthy answer.

## 2. `R4_BASE_OBJ_Y` spec-ambiguity resolution — correctly resolved, but exposes a second, softer verification gap

**Resolved correctly.** I independently re-derived it two ways. (a) Against
`R3`'s own precedent: `R3_BASE_OBJ_Y = R3_BASE_NY//2 = 1188` (no `ABSORB`
subtraction at that stage — `r3_config()` subtracts it exactly once, later,
via `y_lo = absorb+pad`), and by hand, `r3_config()`'s own `A=obj_y−y_lo`
for `C40_R3` gives `1188−60=1128 = round(752×1.5)` — matching `A_HALF_
APERTURE×R3_RATIO` exactly, confirming the *pattern* `R4_BASE_OBJ_Y =
R4_BASE_NY//2` (not `NY//2 − ABSORB`) is the one that mirrors `R3`. (b)
Plugging the committed value (`R4_BASE_OBJ_Y=1584=R4_BASE_NY//2`) through
`r4_config()` by hand: `C40_R4` gives `A=(1584+0)−(80+0)=1504`; `G40_R4`
gives `A=(1584+80)−(80+80)=1504` — both match Gate 2's own asserted
`1504` exactly, and `results.json::gates.gate2_a_congruence` confirms
`pass_=True`. **The committed `design_geometry.py` value is correct.**

**But this reveals NOTES.md's own frozen Phase-3 spec was internally
self-contradictory, and Red Team's own Phase-2 verification of this exact
constant did not fully close the gap it was checking.** `NOTES.md` line 112
tables the formula `R4_BASE_NY//2 − R4_BASE_ABSORB` (=1504) for
`R4_BASE_OBJ_Y` — the *wrong* formula. Threading *that* value through
`r4_config()`'s own `A=obj_y−y_lo` line (which subtracts `ABSORB` a *second*
time via `y_lo`) gives `A=1504−80=1424` for `C40_R4`, silently breaking
Gate 2's own `A==1504` requirement by 80 cells — directly contradicting the
same document's own Setup-section sentence ("Both configs give `A = obj_y
− y_lo = 1504`"). `design_geometry.py`'s own committed comment (lines
236–254) discloses this exact contradiction and resolves it toward the
`R3`-mirroring reading, verified above. Because Gate 2 is a static,
pre-FDTD assert, the wrong formula would have HALTED the run loudly, not
silently corrupted a result — so this was never a live risk to any
delivered number. **But it means Phase 2's own "documentation
completeness, non-blocking" note on this exact constant was not fully
rigorous**: Red Team's audit verified that the flagged formula reproduces
the *target number* 1504 in isolation
(`R4_BASE_NY//2−R4_BASE_ABSORB=1584−80=1504`) and judged that sufficient —
but never checked whether *that same value*, substituted as `R4_BASE_OBJ_Y`
itself and threaded through `r4_config()`'s own downstream subtraction,
reproduces the same target (it does not — it gives 1424). That is an
R9-shape gap (verifying a number reproduces is not the same as verifying it
is the *correct quantity to substitute* downstream) applied to a spec
constant rather than a unit-comparison, caught here only because Phase 4's
own coding forced the full substitution to actually happen. Non-load-
bearing (self-defended by Gate 2, correctly resolved, correctly disclosed
forward in both `design_geometry.py`'s comment and `results.json`'s own
`spec_resolution_disclosures` key) — but a genuinely new instance of a
known failure family, worth naming for the record.

## 3. Does this change my Iteration-68 (R15) assessment?

**Yes — I believe R15 warrants a new addendum, though the Director/Red
Team, not one seat, should adopt it.** R15's own founding text (Iteration
68, my own self-review) characterizes the risk as a *calibration boundary
built from points near a resolution-sensitive node* — framed around
individual points near an edge. This cycle's Rank 1b shows the same
underlying hazard can manifest as a **wholesale reversal of an entire
previously-classified interior region** (all six points, not one boundary
point, flipping both sign and classification together) — a qualitatively
stronger and structurally different failure than "a boundary point's own
classification is uncertain." I recommend the addendum state: a resolution
check that fully reverses an entire sampled span, rather than partially
drifting it, should be read as evidence that *neither* resolution's reading
is trustworthy yet, and specifically must not be resolved by treating the
finer grid as automatically more correct — mirroring my own §1 finding
above that two points sharing one construction recipe cannot, by
themselves, distinguish convergence from a persistent recipe-level
artifact.

## Genuinely new defect found (summary)

An unverifiable, hand-asserted verification claim ("a standalone test
harness... during Phase 4") entered `NOTES.md`'s permanent record (Result
section + Learned #4) with zero supporting artifact anywhere in `run.py`,
`run_output.txt`, `results.json`, or git history — non-load-bearing (I
independently re-derived Gate 5's soundness on different grounds) but a
real instance of this house's own R4 discipline, applied to a verification-
methodology claim rather than a numeric figure. Secondary, smaller finding:
Red Team's own Phase-2 "resolves correctly either way" clearance of the
`R4_BASE_OBJ_Y` ambiguity checked formula-reproduces-target-number, not
formula-is-correct-when-substituted-downstream — an R9-shape near-miss,
self-defended by Gate 2, correctly resolved in the end.

## Ranked top candidate next step

1. **A third `cpl` resolution point at the same six interior angles
   (matching NOTES.md's own Next#1), but explicitly framed as necessary,
   not merely confirmatory, because of Idealization 17's shared-recipe
   risk** — two points built from one substituted-ratio formula cannot
   distinguish genuine convergence from a persistent construction-recipe
   artifact; a third point is the minimum needed to see a trend at all. If
   budget allows, prefer a ratio that is not a clean multiple of the
   existing two (e.g. `cpl=45` rather than `cpl=50`/`cpl=60`) to reduce the
   chance any shared-recipe artifact aliases consistently across all three
   points the same way.
2. Retrofit Gate 5's runtime `sigma_e`-array check onto the `R3` family's
   own existing sigma-branch call sites (exp-091/092/093), which have never
   had an equivalent check — named in this cycle's own Learned #4 as a
   candidate, and directly relevant given Rank 2 of this very cycle ran a
   `R3`-family sigma-branch call with no such gate.
3. 38.4°'s flip (Rank 3) deserves the same dedicated zero-crossing-
   proximity follow-up 41.4°'s flip received at exp-092 — before any future
   citation treats the `n=11` caution-zone table as settled.
