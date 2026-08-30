# PHASE 2 — RED TEAM AUDIT · Panel Iteration 71 · exp-094

*Fresh sub-agent, RED TEAM charter (PANEL.md, verbatim: attacks every
proposal, speaks last and hardest; standard is not textbook-physics
compliance — speculation is permitted; kills internal inconsistency,
unfalsifiable claims, mechanisms that cannot be expressed as simulation
parameters, and proposals that quietly violate a target constraint —
especially #3). Received: `phase1_proposal.md` in full; all five blind
Phase-2 critiques in full (photonics, materials, em, thermodynamics,
vision); PANEL.md in full; LOGBOOK.md's RULED OUT (R1–R15 verbatim),
ESTABLISHED, and the complete T28 record (Iterations 46–70 read; 68/69/70
read in full); PLAN.md's Current-state section. Independently re-derived
from primary source, this session, via Read/Grep/Bash-Python — not taken
on the proposal's word or any critic's word: `lab/fdtd2d.py::Sim.run`
(the E-update coefficients), `lab/materials.py::graded_black_shell`/
`_graded_black`, `experiments/069-.../design_geometry.py` (R3 recipe,
`r3_config`), `experiments/090-.../run.py` (original `cpl=20` dataset),
`experiments/091-.../run.py` and `results.json` (R3 rescale, the 41.6°
bracket cell), `experiments/092-.../run.py` (`SIGMA_R3_CORRECTED`'s own
derivation and assert), `experiments/093-.../run.py` and `results.json`
(items 1/2/3/5, the n=8 table, the interior sweep, the sigma-branch
finding, `pair_metrics_full`/`cell_metrics_full` call sites, the
`netd_disclaimer` convention).

## 0. Scope note

Pure instrument/comparability recalibration: T1 route N/A (independently
re-confirmed against the unbroken LOGBOOK record for T28 since exp-069),
no phenomenon-mechanism claim, no `REALIZABILITY_MEMO.md` engagement.
Constraints 1–4 are not engaged by this cycle's substance, so no
`constraint-#N-violation` tag applies anywhere below — consistent with
every prior Red Team audit's treatment of a T28 desk/instrument cycle
(exp-091/092/093's own Phase-2/5 Red Team audits). The attacks below are
about internal consistency, verification completeness, and claim-scoping,
matching this seat's charter for a cycle of this shape.

---

## Adjudication of the five blind critiques, in the order received

### RT-1 — [inconsistency] MATERIALS + EM's convergent finding is REAL: no gate in §2.4 can ever catch a runtime sigma-wiring bug — CONFIRMED, elevated to MANDATORY

**Independently verified, not merely re-checked.** I grepped every
committed `run.py` in the R3/sigma lineage (`experiments/090,091,092,093`)
for any assertion that reads the constructed `Sim` object's own
`sigma_e` array:

```
grep -n "assert.*sigma|sim\.sigma_e\.max|sim\.sigma_e\[" .../09{0,1,2,3}*/run.py
  -> no matches, anywhere, ever, on this bench
```

**This confirms both critiques' shared premise exactly**: every sigma-related
gate this sub-thread has ever shipped — including the four proposed here
(§2.4 items 1–4) — is a static check on Python *constants*
(`R4_CONFIGS["..."]["A"]`, `L_GEOMETRIC_M_R4`, `SIGMA_R4_CORRECTED`), never
on what value actually lands in `sim.sigma_e` after
`build_article_r4_sigma()` runs. I independently re-read the Iteration-68
LOGBOOK entry (exp-091) that adopted R15: MATERIALS' own Phase-5
self-review there found `graded_black_shell`'s `sigma_max` had been left
at its **native default (0.5)** under the R3 rescale despite the
`τ_center=2·σ·r_out(cells)` convention already being established
(T10/SIGMA_ON) — i.e. the correct physical argument existed and was simply
never wired through at the one call site that mattered, undetected by
every gate then in place, found only by hand at Phase 5. A copy-paste slip
in Rank 1b's `_run_sim_r4_sigma`/`one_call_r4` (e.g. a stray
`SIGMA_NATIVE` or `SIGMA_R3_CORRECTED` where `SIGMA_R4_CORRECTED` belongs)
is the *exact same defect shape*, one call-site away, in a family this
cycle newly constructs from scratch — and every one of the four proposed
gates, run in sequence, would pass cleanly regardless, because none of
them touches the object the bug would actually corrupt.

**This is precisely this house's "genuinely convergent, load-bearing
catch from two independent seats" pattern (R6–R14's own elevation
standard)** — two seats, different reasoning paths (MATERIALS: direct
R15-precedent pattern-match; EM: derived from the update-equation algebra
that at `RATIO=2.0` every derived constant is an exact integer, so the
existing gates are a *weaker* discriminator here than they were at
`RATIO=1.5`), converging on the same underlying gap. **Ruling: real,
load-bearing, MANDATORY** — this is not a discretionary nice-to-have.

**One correction to EM's own proposed remedy, independently derived
here**: EM's offered fifth gate,
`assert abs(2*SIGMA_R4_CORRECTED*R4_R_OUT - 2*SIGMA_NATIVE*R_OUT) < 1e-9`,
does **not** actually close the gap EM itself just diagnosed. Substituting
the proposal's own definitions,
`SIGMA_R4_CORRECTED := SIGMA_NATIVE/R4_RATIO` and
`R4_R_OUT := round(R_OUT*R4_RATIO)` (exact, no rounding error at
`R4_RATIO=2.0`), the two sides of EM's own assert reduce algebraically to
`SIGMA_NATIVE·R_OUT ≡ SIGMA_NATIVE·R_OUT` — **true by construction for any
value of `SIGMA_NATIVE`/`R_OUT`/`R4_RATIO` whatsoever**, and already fully
implied by the existing gate 4 (`SIGMA_R4_CORRECTED==0.25`, which alone
pins the one free numeric input). It is a second static check on the same
constants, not a check on the constructed `Sim`. **This is the identical
"trivially-true-by-construction" failure EM's own sharpest attack names**
— EM diagnosed the disease correctly but its own prescribed remedy has it
too. MATERIALS' proposed fix (`assert np.isclose(sim.sigma_e[shell_mask].
max(), SIGMA_R4_CORRECTED, atol=1e-9)`, evaluated immediately after each
`build_article_r4_sigma` call, before any FDTD step runs) is the one gate
of the two that actually reads the object the bug lives in, and is the
one that should be mandatory. EM's assert may be added alongside it for
documentation value (it does no harm), but must not be substituted for,
or represented as equivalent to, MATERIALS' runtime check.

### RT-2 — [inconsistency] PHOTONICS' backwards-reasoning catch on Rank 2's CONFIRM lean — CONFIRMED, independently re-derived, MANDATORY same-shift fix

Independently recomputed, from `experiments/091-.../results.json::
raw.r3_leg4_cpl30_steps4200_bracket["41.6"]`: `ratio_k=25.9467426898452`
— matches the proposal's own citation bit-exact. Independently recomputed
the proposal's own n=8 table (`experiments/093-.../results.json::item2.
base_table`) to locate 41.6° relative to both populations the proposal
itself names:

- **"Far-from-null CONSISTENT" population** (37.2°, 39.2°–39.8°):
  `ratio_k` = 1.8463 (37.2°), 0.9197 (39.2°), 0.0762 (39.4°), 1.2111
  (39.6°), 3.8410 (39.8°) — range **0.076–3.841**, matching the proposal's
  own cited "0.08–3.8" band exactly.
- **Confirmed-fragile interior sweep** (41.825°–41.9°, corrected sigma,
  floor-clearing points, from `experiments/093-.../results.json::item1`):
  `ratio_k` = 29.577 (41.825°), 25.109 (41.85°) — the proposal's own cited
  "20.5×–29.6×" band.
- **41.6° (native sigma)**: `ratio_k = 25.9467` — sits **inside** the
  confirmed-fragile band (25.1–29.6), roughly **7× further** from the
  far-from-null population's own upper edge (3.841) than 41.6° is from
  that population.

Given `frac_p_abs` is independently established near-flat across this
window (item 3b/5b, both CONFIRM, both cited correctly elsewhere in this
same proposal — 0.008639 at 41.6° native vs. 0.0054–0.0069 at the interior
sweep, same order of magnitude, not the order-of-magnitude swings seen
elsewhere on this channel), `ratio_k = frac_p_abs/frac_contrast` with a
roughly-fixed numerator means a **large** `ratio_k` is arithmetically a
signature of a **small** `frac_contrast` denominator — i.e. proximity to
`delta_scene`'s own zero-crossing, R13's own established mechanism,
adopted by this very proposal's compliance header. The proposal's stated
lean — "`ratio_k=25.9` is not small" therefore 41.6° sits safely inside
the positive lobe — inverts that established relationship. **PHOTONICS'
correction is right, independently confirmed by direct recomputation, not
merely plausible.** This is squarely an R4/R9-shape defect (a
wrong-but-non-binding claim about to enter the permanent record) —
non-load-bearing to any gate or band (correctly, PHOTONICS' own scoping),
but this house's own standing discipline is that a wrong physical
justification does not get a pass for being non-binding. **MANDATORY,
same-shift, zero-FDTD fix**: strike the "informed lean" paragraph's
`ratio_k`-based justification for Rank 2 entirely, or replace it with the
correct reading — 41.6° sits in the *same* high-`ratio_k`, near-null-
adjacent population as the confirmed-fragile interior sweep, so REFUTE is
at least as plausible as CONFIRM there, disclosed as such.

### RT-3 — [inconsistency] EM's sequencing/provisionality point folds into RT-2's fix, not a separate mandatory item

EM's secondary point (Rank 2's "well inside the positive lobe" framing is
itself a claim about where the null's edge sits, established only at
`cpl=30`, and Rank 1 is the very check of whether that edge moves under
refinement) is correct as far as it goes, but once RT-2's fix is applied
— striking or correcting the directional lean rather than merely
softening its confidence — there is no remaining "settled ahead of time"
framing left to mark provisional. **Ruling: subsumed by RT-2, not an
independent mandatory item.** If the Director chooses to retain any
residual qualitative language about 41.6° after RT-2's correction (not
required), it must carry EM's "provisional pending Rank 1b" qualifier —
folded into RT-2's fix as a single combined edit, not a second one.

### RT-4 — VISION's ambiguity is REAL, confirmed by direct inspection of the actual call sites it worried about — MANDATORY, low-cost close

Independently traced the exact machinery §2.2 lists as "reused verbatim."
`experiments/093-.../run.py`'s own **item 1** and **item 3** — the two
items structurally identical in shape to this cycle's Rank 2 (a sigma
comparability close) and Rank 1 (an interior sweep on the R3-family
layer) — both call `pair_metrics_full`/`cell_metrics_full`, confirmed at
source (`run.py:346,451,547`), **not** the plain `pair_metrics`/
`cell_metrics` VISION worried might be silently bypassed. Confirmed
further, directly from `experiments/093-.../results.json`, that this
produces real NETD byproduct fields (`dt_ss_full_K_c`,
`netd_classification_c`, etc.) inside `item1`'s and `item3`'s own
`per_theta` records — exactly VISION's feared outcome, already realized
one cycle upstream of this proposal, on the identical code family this
cycle's Rank 1/Rank 2 will run through.

**What actually protected exp-093 from the "computed-but-never-reported"
failure mode**: a **top-level** `results.json["netd_disclaimer"]` key
("NETD is an instrument/detector threshold, not a human perceptual
one... does NOT bear on constraint-3/4's human-eye verdict"), written once
and covering every NETD field anywhere in that file, regardless of which
item produced it. **This proposal's own `results.json` is a new file for
a new `run.py`** (this cycle's own module-chain reuse loads functions, it
does not inherit a prior file's own top-level keys) — nothing in
`phase1_proposal.md` commits to writing an equivalent top-level
disclaimer into *this* cycle's own output, and given the precedent just
independently confirmed (Rank 2/Rank 3 will almost certainly call the
`_full` variants, matching exp-093's own item 1/item 3 idiom), the risk is
not hypothetical.

Given this exact shape of gap — a caveat that must travel with a field it
does not obviously live beside — has fired Checkpoint criterion 4 four
times in this program's history (Iterations 53/63/64/65) and was named
again, non-firing only by a hair, as recently as Iteration 68 (VISION's
`netd_disclaimer`-written-but-never-`print()`-ed catch) and Iteration 70
(THERMODYNAMICS' own self-caught "promised-but-unreported" NETD check),
**this is not a one-sentence courtesy — it is a MANDATORY, zero-cost,
pre-freeze requirement**: (a) state explicitly, before Phase 4 runs,
which cell/pair-metrics variant Rank 2 and Rank 3 invoke (on the evidence
above, almost certainly `_full`); and (b) regardless of the answer,
carry the identical top-level `netd_disclaimer`/`scope_note` convention
`experiments/093-.../results.json` established into this cycle's own
`results.json`, written whether or not any NETD field is ever printed to
`run_output.txt`.

### RT-5 — THERMODYNAMICS' zero-marginal-cost `p_abs_w` anchor check — CONFIRMED real, MANDATORY

Independently confirmed `p_abs_w` is already a `cell_metrics`/
`cell_metrics_full` output at every angle this bench has ever run
(verified directly in `experiments/093-.../results.json::item1.per_theta`,
which already carries `p_abs_w_c`/`p_abs_w_g` for all six `cpl=30`
interior points) — so the equivalent field on `cell_metrics_r4`'s own
output, for Rank 1's already-budgeted 32 calls, costs zero additional
FDTD time. THERMODYNAMICS' point stands independently of any critique-
counting exercise: exp-093 item 5's flatness/UNDETECTABLE finding is an
FDTD result at `cpl≤30` only, and R15 exists *specifically* because this
sub-thread has repeatedly found settled-looking features flip under grid
refinement (40.2°/41.4°'s own `Y` flip at exp-091; 42.0°'s own sign flip
at exp-093 item 3) — nothing in the record shows the energy-flatness
finding is any more resolution-immune than the coherent channel was
assumed to be before those two discoveries. Rank 1 is this cycle's own
most expensive, most novel item and its own §4 commits **no** equivalent
check, while Rank 2 — cheaper, less novel — already does. This is exactly
the shape of "affordable, named, not run" gap the R6–R12 lineage
(especially R8) exists to force closed before it becomes outcome-
determining rather than after. **MANDATORY**: add the identical
2–5%-of-0.51 `p_abs_w`-vs-T9-anchor informational check to Rank 1b's own
§4 predictions, and add an explicit new idealization stating the
energy-flatness finding is `cpl≤30`-verified only, not yet checked at
`cpl=40` — matching THERMODYNAMICS' own offered flip condition verbatim.

---

## Minor findings, folded into the docket, not separately numbered attacks

- **Documentation completeness, non-blocking.** §2.3's new-constants table
  omits `R4_BASE_OBJ_Y` (needed by `r4_config()`'s own construction,
  mirroring `r3_config()`'s un-tabulated `R3_BASE_OBJ_Y = R3_BASE_NY // 2`
  precedent exactly). Independently verified this resolves correctly
  either way (`R4_BASE_NY//2 − R4_BASE_ABSORB = 1584 − 80 = 1504`, matching
  gate 2's own asserted value) — not a defect, matches the un-tabulated
  precedent for the identical derived quantity in the R3 family. No fix
  required; noting only for completeness.
- **Cost-model note, non-blocking.** The proposal's own disclosure that
  every prior T28 cycle's actual wall time has landed well under its model
  estimate (exp-093: 29.4 min actual vs. 55–166 min estimated) is
  independently confirmed against the LOGBOOK record cited. No action
  needed; the estimate is conservative, not load-bearing to any decision.

None of these two, individually or together, changes the overall verdict;
both are non-blocking observations, not fixes.

---

## Working through PANEL.md's five Checkpoint criteria explicitly (not asserted by precedent — checked against this cycle's own record)

1. **A configuration passes all constraint metrics.** Not applicable —
   this cycle makes no constraint-metric claim; T1 route N/A, independently
   re-confirmed against the unbroken T28 LOGBOOK record since exp-069.
   Does not fire.
2. **A proven boundary — a constraint subset shown jointly unsatisfiable.**
   Not applicable — no mechanism-class claim is made or resolved anywhere
   in this proposal. Does not fire.
3. **Synthesis requires engine physics beyond the validated bench
   classes.** Not applicable — `R4` is a mechanical, zero-design-freedom
   geometric rescale of the already-validated `graded_black_shell`/
   `r3_config()` recipe; every new function is disclosed and independently
   verified here as a "mirror" of an existing, already-trusted one; zero
   `lab/` diff. Does not fire.
4. **Red Team flags program-integrity drift (unfalsifiable claims, a
   constraint quietly dropped — especially #3).** **The one requiring real
   judgment.** RT-1's gap and RT-4's disclaimer-carryover risk are both
   exactly the *shape* of defect (a verification gap that looks closed but
   isn't; a caveat that must travel with a field and might not) that has
   fired Checkpoint 4 repeatedly in this program's history when it reached
   Phase 3/LOGBOOK undetected. **It has not reached that point here** — both
   are caught at Phase 2, independently re-derived from primary source
   (not reasoned about, not taken on either critic's word), before any
   synthesis exists, matching this program's own repeatedly-applied
   "caught blind, before Phase 3 froze anything" non-firing test. **Ruling:
   does not fire, PROVIDED the mandatory fixes below (RT-1 through RT-5)
   are actually applied before Phase 3 freeze.** This is not a discretionary
   caveat — if RT-1's runtime gate is not actually added, or RT-4's
   disclaimer convention is not actually carried forward, and either later
   proves outcome-determining, that reopens this question at Phase 5 on a
   record showing the defect was named, specific, affordable, and not
   fixed — the exact "known, named, ignored" shape R6–R15 all fire on.
5. **Two consecutive iterations with no logbook-advancing result.**
   Iteration 69 (exp-092: crossing located, sigma confound cleanly ruled
   out on the PRIMARY channel) and Iteration 70 (exp-093: SINGLE-NULL
   resolved on the coherent channel, dispersion-alone mechanism genuinely
   REFUTEd, NETD backfill CONFIRM) were both independently confirmed
   logbook-advancing PARTIAL verdicts in LOGBOOK's own record — not two
   non-advancing cycles. Does not fire, regardless of how this cycle
   itself ultimately scores.

**None of the five criteria fire** — but criterion 4's non-firing is
explicitly conditional on the mandatory docket below actually landing in
`phase3_synthesis.md`/`NOTES.md`, not an unconditional pass.

---

## Overall verdict: **PROCEED-WITH-MANDATORY-FIXES**

The underlying instrument design is sound: the `R4` geometry family is a
faithful, independently-re-verified mechanical mirror of the
already-trusted `R3` recipe (every constant checked by hand against the
formula, the physical-length-invariance and congruent-construction
identities both confirmed bit-exact); the `SIGMA_CORRECTED(RATIO) =
SIGMA_NATIVE/RATIO` generalization is not merely pattern-matched from one
data point but independently re-derivable from `fdtd2d.py`'s own
E-update coefficient (confirmed here, agreeing with EM's own Phase-2
re-derivation); the call budget arithmetic checks out exactly (48 calls,
verified line by line against the table); every cited historical figure
(the n=7 `cpl=20` dataset, the 41.6° `cpl=30` bracket cell, the n=8 table)
reproduces bit-exact from primary source, satisfying R4/R9. The defects
below are all cheap, zero-FDTD, fixable entirely before Phase 3 freeze,
at no cost to the 48 already-budgeted calls.

**Mandatory fixes (five, none overridden, none discretionary):**

1. **(RT-1.)** Add a runtime identity gate, immediately after each
   `build_article_r4_sigma` call in Rank 1a/1b, asserting
   `np.isclose(sim.sigma_e[shell_mask].max(), <the sigma_max value passed
   at that call>, atol=1e-9)` **before any FDTD step runs** — MATERIALS'
   proposed fix, verified here as the one gate of the two Phase-2 offered
   that actually discharges the gap (EM's own proposed static
   τ_center-identity assert may be added as a documentation supplement but
   does not substitute for this — independently shown above to be
   algebraically implied by the existing gate 4 and trivially true by
   construction).
2. **(RT-2.)** Strike the Rank 2 "informed lean" paragraph's `ratio_k`-
   based CONFIRM justification, or replace it with the correct reading:
   41.6° (`ratio_k=25.9`, native sigma) sits in the *same* high-`ratio_k`
   population as the confirmed-fragile interior sweep (20.5×–29.6×), not
   the far-from-null CONSISTENT population (0.08×–3.8×) — so REFUTE is at
   least as plausible as CONFIRM there, disclosed as such rather than as a
   foreseeable-but-mislabeled surprise. (Folds in EM's provisionality
   point — RT-3 — as part of the same edit, not a separate change.)
3. **(RT-4.)** Before Phase 4 runs: state explicitly which cell/pair-
   metrics variant Rank 2 and Rank 3 invoke, and, regardless of the
   answer, commit to writing the identical top-level `netd_disclaimer`/
   `scope_note` convention `experiments/093-.../results.json` established
   into this cycle's own `results.json` — not contingent on whether any
   NETD field is ever printed to `run_output.txt`.
4. **(RT-5.)** Add, at zero additional FDTD calls, a `p_abs_w`-vs-0.51-
   T9-anchor informational check (2–5% band, mirroring Rank 2's own) to
   Rank 1b's §4 predictions, computed from the already-planned 32 calls;
   add an explicit new idealization stating exp-093's own energy-flatness
   finding is `cpl≤30`-verified only, not yet checked at `cpl=40`.
5. **(Housekeeping, folds RT-1's discharge condition into the record.)**
   Idealization 18 should be updated to note that the generalization
   `SIGMA_CORRECTED(RATIO)=SIGMA_NATIVE/RATIO` is, as of this audit,
   independently re-derivable from `fdtd2d.py`'s own loss-update
   coefficient (not merely empirically pattern-matched at one ratio) —
   EM's own Phase-2 finding, correct and worth preserving in the permanent
   record even though it does not change any verdict or band.

**Single most consequential fix**: #1. Everything else in this proposal
— the geometry, the budget, the falsifiable bands, the sequencing — holds
up to independent re-derivation from primary source; the one place a real
bug could hide undetected through every currently-planned gate is exactly
where R15 was born, one call-site over.
