# PHASE 5 — RED TEAM FINAL AUDIT · Panel Iteration 47 · exp-070
## T28 mechanism desk-check batch

*Fresh sub-agent, RED TEAM charter (PANEL.md seat 7). Receives the full
exp-070 record and all six blind Phase-5 reviews. Speaks last and hardest.
Standard for this cycle: NOT textbook-physics compliance — internal
consistency, falsifiability, program-integrity discipline, and this
program's own Checkpoint-4/R5/R4 precedent, applied explicitly.*

## 0. Independent re-verification performed

`python3 desk_check_mechanism.py`, re-run fresh in this session: output is
bit-for-bit identical to the committed `results.json` (all five verdicts,
all `null_p` values, all tie-sets, the 36,680/7,179 search-space counts).
This is the fourth independent bit-exact reproduction on record this cycle
(PHOTONICS, MATERIALS, EM, VISION each ran it; QUANTUM additionally
reimplemented the search/null-control from scratch in different code and
matched to the digit) — no computational defect exists anywhere in this
batch, confirmed a fifth time here.

Independently recomputed, from `results.json`'s raw fields, three numbers
central to this audit's rulings:
- `|P*(C80)−P*(C40)|/mean = 3.93%` (EM's cross-config figure) — reproduced
  exactly (`(2.5338−2.4361)/2.4850 = 0.03933`).
- Fixed-period-fit `R²` against T21's own 1.9608° period: `C40=0.2988`,
  `C80=0.2645` — reproduced exactly from `results.json`'s
  `r_squared_fixed` fields (PHOTONICS'/EM's shared citation).
- `python3 lab/caveat_lint.py`, run live against the current repo: **13
  registry entries checked, 0 required-site failures, and no entry anywhere
  in the tool's output references exp-070, `A_eff`, `A_alt`, `518.8`, or
  `233.19`.** PHOTONICS'/MATERIALS' finding — no registry entry exists for
  this cycle's own headline near-misses — is independently confirmed, live,
  not merely asserted from reading the JSON file.

All six blind Phase-5 reviews are independently well-founded on the record.
No review is overridden below; several are sharpened or given a more
precise procedural ruling than they gave themselves.

---

## 1. PHOTONICS'/MATERIALS' caveat-lint gap — does it fire Checkpoint criterion 4?

**No. Ruled a same-shift-fixable forward gap, matching this program's own
established non-firing precedent, not any firing precedent.**

**The finding is real** (independently confirmed above, live tool
execution, not the reviews' own prose). `lab/caveat_lint_config.json`'s
only T28-adjacent entry (`exp065-steps1400-unsettled-plane-channel`) does
not cover exp-070's own quantities; no entry anywhere protects a future
citation of `A_eff≈518.81`/`A_alt≈233.19` from being quoted without its
disqualifying `null_p` context. This is precisely the failure class LOGBOOK
records this program has fired Checkpoint criterion 4 on before.

**But firing requires an aggravating fact this program's own history
consistently requires, and none is present here.** Weighing against every
CHECKPOINT block in PLAN.md (Iterations 17, 36, 37, 38, 39×2, 40, 44/67,
45/68):

- **Every actual firing shares one of two aggravating facts**: (a) a
  violated pre-committed tripwire — Iteration 39's `candidate_globs`
  recurrence after its own lineage's "no further deliberation" clause had
  already been triggered once (Iteration 38) and its grace explicitly
  declared spent; Iteration 40's tripwire, pre-committed in writing at
  Phase 2 of the *same* cycle, fired when the exact named fact pattern
  recurred at that same cycle's own Phase 5. Or (b) survival through most
  or all of a cycle's five-phase process **undetected**, reaching a
  permanent artifact — Iteration 37's docstring wrong for three consecutive
  cycles at the single most permanent, every-run-executed site; Iteration
  44/67's sign-inverted formula surviving Phase 3, Phase 4's 23/23 gates,
  and four of six Phase-5 reviews before reaching a permanent regression
  gate.
- **Neither condition holds here.** No prior tripwire named exp-070's
  registry coverage specifically (unlike Iteration 40's self-declared,
  Director-accepted tripwire). And this is not a live violation surviving
  undetected — `caveat_lint.py` shows **zero** required-site failures
  today; every number that needs its `null_p` context carries it, in the
  same sentence, everywhere both PHOTONICS and VISION independently checked
  (§1, §1 of their own Phase-5 reviews). The gap is that the registry has
  never had an entry created for this cycle's own new quantities — found by
  two independent blind seats at Phase 5, this cycle's own natural
  checkpoint, **before** this cycle closes and **before** any future
  citation (most immediately, whatever document reports EM's C60/C70 test)
  has had the opportunity to violate it.
- **This is the exact shape of Iteration 38's own precedent** (exp-061):
  "a registry `required_sites` gap on the very entry built to prevent that
  class of gap... found by this cycle's own review process and fixed
  same-shift; neither overturned the tier; no Checkpoint criterion fires."
  It also matches the broader "found-before-close, fixed-same-shift"
  pattern VISION's own Phase-5 review names (Iterations 19/23/38/42) and
  the closely analogous Iteration 45/68 item ("a new
  `lab/caveat_lint_config.json` entry closing a two-cycle-overdue
  caveat-propagation gap" — one of that cycle's mandatory fixes, not a
  firing). The one textual difference — this is a brand-new experiment's
  registry entry that has never existed, not an existing entry's coverage
  drifting stale — if anything makes this a *weaker* case for firing than
  Iteration 38's own precedent, not a stronger one: nothing here is a
  broken promise, only an un-made one, caught at the first opportunity to
  make it.

**Ruling: does not fire.** Docket item below (§7, item 1) closes it
same-shift, mirroring PHOTONICS' own proposed entry name and MATERIALS'
proposed trigger terms.

---

## 2. EM's "P-070-1's CONFIRM is weaker than claimed" — correct, and what it does to the verdict

**Correct on the numbers, independently reproduced. Does not flip the
verdict to NEITHER. Requires a same-shift NOTES.md language correction,
not a re-score.**

EM's argument, reproduced independently above: `C40` and `C80`'s own
recovered periods (2.4361°, 2.5338°) differ from **each other** by 3.93% —
genuinely close, a real point for the config-invariant reading — but each
individually sits 14.29%/10.85% from the actual anchor number
(`P*_delta=2.8421°`) the CONFIRM band is scored against, and each carries a
non-negligible fixed-period fit to T21's own established 1.9608° fringe
(`R²=0.2988`/`0.2645`, only moderately below the free-fit's `0.43`/`0.43`).
By EM's own same-frequency-superposition argument — the identical algebraic
tool that opened T28 in exp-069 (`A` bit-identical between configs ⟹ a
45%-off delta period is evidence of a second contributor) — a *genuinely
shared* config-invariant component should reproduce at the **same**
frequency in both raw curves and should appear at that same frequency in
their difference; landing 11–14% off the delta's own free-fit period on a
31-point/~3-cycle window dominated by a known strong ~1.96° fringe is
exactly the signature of a **compromise fit** between two nearby,
imperfectly-separated frequencies, not a clean independent confirmation.

**This does not change the CONFIRM verdict.** P-070-1's gate (≤20%
deviation from `P*_delta` for both configs) is a pre-committed,
Red-Team-audited band, reusing this program's own established convention
verbatim (P-069-3's identical 20%/50% bands). Both configs clear it,
honestly, on data that reproduces bit-exact. House discipline — predictions
committed before the run are scored as committed, not re-scored after a
later review sharpens the interpretation (the same principle Q3 below
applies to R5) — forecloses converting a cleared pre-registered gate into
NEITHER after the fact merely because a Phase-5 review shows the band was
generous. EM's own review does not ask for a re-score either; it asks for
softened language.

**What EM's finding does require, same-shift**: NOTES.md's Learned #1
currently reads "the recovered periods inside `C40(θ)` and `C80(θ)` alone
... both independently land close to the padding-delta's own free-fit
period" — this overstates what was shown. Corrected language (docket item
2, §7): disclose the 3.93% cross-config spread, the fixed-period `R²`
pair against T21's own fringe, and state plainly that the result is more
consistent with a compromise fit between a strong known component and a
weaker, imperfectly-resolved second one than with a tightly-matching
independent signal — a real, CONFIRMED-under-its-own-gate result, but
softer than the prose currently conveys. The "Next" section's "P-070-1
positively disfavors the `ABSORB`-tied hypothesis" also needs one word of
softening (§7, item 3) for the same reason — the disfavoring is real but
not decisive, which is exactly why EM's own C60/C70 causal test, not more
desk arithmetic, is the correct next step (unanimous, §4 below).

---

## 3. QUANTUM's R5-precedent argument — retroactive or forward-only?

**Correct, and independently confirmed to be a stronger case than R5's own
numbers. Forward-only. No NOTES.md re-score.**

QUANTUM's finding: R5 (Iteration 28) ruled a regressor out with an AUC
(0.649) merely *close to* its own 0.65 REFUTE line, on structural grounds —
a trivial zero-information baseline beat it. Exp-070's P-070-2/4 matches
are, on QUANTUM's own independently-reconstructed null distribution
(median null best-match deviation ≈0.037%, tighter than either real
target's own best match), a **more decisive** instance of the identical
shape: the real matches (0.015%/0.081%/0.036%) sit at or worse than the
null median (the "minus" branch, `p=0.8055`, is beaten by over 80% of pure
chance). By this program's own R5 discipline, that is REFUTE-grade
evidence, not gray-zone evidence — yet the pre-committed CONFIRM/REFUTE
schema (`refute = best_rel≥0.10` only) has no path from a high `null_p` to
REFUTE, so both land in NEITHER by construction.

**Ruled forward-only, not retroactive, for the same pre-registration
reason as §2 above**: the predictions were committed to git, gated, and
scored exactly as designed before the run; QUANTUM's own review does not
ask for a re-score either, and NOTES.md's/`phase4_results.md`'s existing
prose already carries the correct epistemic force ("statistically
indistinguishable from chance," "worse than 80.6% of pure-chance targets")
— the boolean label is a schema limitation, not a misreported finding.
Converting an already-honestly-narrated NEITHER into a re-scored REFUTE
after the fact would be the exact house-discipline violation Iteration 46's
Block MINI FORMAL_RETIREMENT precedent exists to prevent (predictions
scored as committed, not re-litigated after the fact because a later review
would have designed the bands differently).

**What this does require, same-shift**: a forward-looking schema note
(docket item 5, §7) — any future reuse of this null-controlled
named-constant-search pattern should include a symmetric REFUTE arm
(`refute = best_rel≥0.10 OR null_p≥0.50`, QUANTUM's own proposed band) —
plus recording `A_alt≈3·R_OUT` (233) and `A_eff≈`[the 519-cluster] as named
dead ends not to be re-proposed as T28 mechanism candidates without new
information, the same treatment R4 gave exp-048's specific defect. This is
a Director/future-cycle house-rule note, not a change to this cycle's own
committed verdicts.

---

## 4. Docket item 10 — is queue item 2 narrowed honestly?

**Yes, confirmed independently. EM's C60/C70 test is genuinely licensed by
P-070-1's CONFIRM, not smuggled in from a NEITHER.**

Docket item 10's own text explicitly permits narrowing "by items (a)'s
corrected config-invariant CONFIRM/REFUTE" in addition to a null-controlled
CONFIRM — P-070-1 qualifies on its own terms, not as an exception. Checked
NOTES.md's "Next" section directly: it narrows *only* on P-070-1's CONFIRM,
states affirmatively that items (b)/(d)/(e) "contribute no surviving
candidate length scale," and nowhere uses the retired 0.08%/0.04% raw
closeness figures as a soft tiebreaker for which FDTD re-run to prefer.
VISION's own Phase-5 review (§3) independently checked the identical
question and found the same — this audit reproduces that finding rather
than taking it on faith, and finds no additional violation VISION missed.

**Confirming the convergence**: all six blind Phase-5 reviews
(PHOTONICS, MATERIALS, EM, THERMODYNAMICS, QUANTUM, VISION) independently
rank EM's C60/C70 `ABSORB`-varying falsification test as their #1 next
direction. This is a genuine, unprompted 6-for-6 convergence, not an
artifact of shared framing — each seat reaches it from its own charter
(PHOTONICS: statistical power on a 4-point sweep; MATERIALS: the correctly
narrowed causal test; EM: resolves its own Finding-1 ambiguity; THERMO: the
only branch with a live physical question to ask *after*; QUANTUM: the
cheapest decisive causal step; VISION: the only branch P-070-1 licenses).
**Confirmed, not disputed** — see ranked directions below.

---

## 5. Ranked top-3 candidate directions (required output)

**1. EM's C60/C70 `ABSORB`-depth falsification test (PLAN.md queue item 2,
first branch), strengthened by two same-cost additions this audit adds to
the mandate.** Reuses already-built congruent configs, zero new `lab/`
diff. On top of the existing mandate (score on recovered period per Attack
1's own lesson, report all four `ABSORB` depths 40/60/70/80 against each
other): (a) include EM's own direct cross-config consistency metric
(`|P*(Ca)−P*(Cb)|/mean`) at every pair, not only against a derived
reference — this is the metric §2 shows was missing and is what would
actually distinguish "genuine shared component" from "compromise fit" at
four points instead of two; (b) fold in the already-queued, near-zero-cost
peak-cell R3 resolution recheck (θ≈37.2°/41.4°, 2 calls) EM's Phase-5
review flags as still open — closing exp-069's own residual resolution-
scope gap before any C60/C70 result is treated as trustworthy costs
nothing extra and removes a standing caveat before it becomes load-bearing
for a causal claim.

**2. `R_contact`'s `measured_direct` literature search** (PLAN.md queue
item 3, unchanged ranking) — converges across 4 of 6 blind reviews
(PHOTONICS #3, MATERIALS #2, THERMODYNAMICS #3, VISION #3) as a standing
priority independent of T28: zero FDTD/rotation-slot competition with item
1, and still the only item across seven cycles now (Iterations 44–47) that
can move a real, sourced materials number for TD-5's still-UNANSWERED
tier (`REALIZABILITY_MEMO.md` Entry 3), blocked purely on WebSearch/WebFetch
tooling availability, not any physics or process gap.

**3. This cycle's own same-shift process docket** — the
`caveat_lint_config.json` registry entry for exp-070 (PHOTONICS/MATERIALS,
§1) and the R5-addendum/symmetric-REFUTE-band forward schema note
(QUANTUM, §3) — both zero-FDTD, minutes of work, and correctly the
highest-leverage moment to land them: before EM's C60/C70 write-up (item 1
above) becomes the first future document with occasion to cite
`A_eff≈518.81`/`A_alt≈233.19` without their null-controlled context, and
before any future cycle reinvents this exact null-permutation-control
lesson from scratch.

---

## 6. Checkpoint criteria — explicit ruling, all five

1. **Configuration passes all constraint metrics** — does not fire. N/A;
   this batch makes no constraint-3 claim (Checkpoint-2 candidacy declined
   throughout, correctly).
2. **Proven boundary, mechanism class jointly unsatisfiable** — does not
   fire. T1 route N/A for this entire cycle, as for exp-041/065/066/068/069.
3. **Synthesis requires engine physics beyond validated bench classes** —
   does not fire. Zero `lab/` diff, zero FDTD calls; pure arithmetic over
   already-gated data.
4. **Program-integrity drift** — does not fire. Ruled in full at §1 above:
   the caveat-lint gap is real but matches this program's own established
   same-shift, found-before-close non-firing pattern (Iteration 38's own
   precedent, and the broader Iterations 19/23/38/42/45 lineage), with
   neither of the two aggravating facts (violated pre-committed tripwire;
   undetected survival through the process) present. EM's and QUANTUM's
   findings (§2, §3) are real, substantive corrections, each handled by a
   same-shift docket item or a forward-only schema note per this program's
   own pre-registration discipline — neither rises to program-integrity
   drift; both are the process catching real things before they became
   load-bearing, which is the discipline working as designed, not a defect
   in it.
5. **Two consecutive iterations, no logbook-advancing result** — does not
   fire. This cycle discharges Red Team's own standing exp-069 forward
   tripwire, cleanly kills one T28 sub-hypothesis (item c, order-of-
   magnitude REFUTE), narrows toward (with EM's now-attached caveat) a
   config-invariant reading over an `ABSORB`-tied one, and establishes a
   generalizable house lesson (null-permutation control is mandatory for
   any future dense small-integer bookkeeping-constant search) — a real,
   if partial, logbook-advancing result. Iteration 46 (exp-069) was itself
   advancing, so this is not even the first of a potential two-cycle count.

**No Checkpoint criterion fires this cycle.**

---

## 7. Same-shift mandatory-fix docket (apply before this cycle closes)

1. **Add `lab/caveat_lint_config.json` entry `exp070-t28-named-constant-
   null-control`** (§1). `trigger_terms`: `A_eff`, `A_alt`, `518.8`,
   `233.19`, `519`, `234`, `P-070-2`, `P-070-4`. `required_sites` seeded
   with `experiments/070-.../NOTES.md` and `phase4_results.md`.
   `candidate_globs`: use the systemic `experiments/*/phase*.md` +
   `LOGBOOK.md`/`PLAN.md` pattern already established after Iteration
   39×2's own lesson about narrow-named-file scoping — do not repeat that
   mistake with a fresh, narrowly-scoped entry. Re-run `python3
   lab/caveat_lint.py` after and confirm 0 required-site failures.

2. **Soften NOTES.md's Learned #1** (§2): add the cross-config spread
   (`|P*(C80)−P*(C40)|/mean=3.93%`), the fixed-period-fit `R²` pair against
   T21's own 1.9608° fringe (`0.2988`/`0.2645`), and state the result is
   more consistent with a compromise fit than a clean independent
   config-invariant signal, attributed to EM's Phase-5 finding.

3. **Soften NOTES.md's "Next" section** (§2): replace "P-070-1 positively
   disfavors the `ABSORB`-tied hypothesis" with language acknowledging the
   disfavoring is real but not decisive (per item 2's correction), which is
   itself the reason EM's causal C60/C70 test, not further desk arithmetic,
   is the correct next step.

4. **Add EM's cross-config consistency figures to `phase4_results.md`'s
   P-070-1 section** (§2): the same numbers as item 2, in the results
   document itself, not only NOTES.md's narrative — computed from
   already-reported `results.json` fields, zero re-run required.

5. **Add a forward-looking LOGBOOK/R5-addendum note** (§3, QUANTUM):
   any future dense small-integer bookkeeping-constant search of this
   shape requires a pre-registered null-permutation control before any
   match counts as evidence; name `A_alt≈3·R_OUT` (233) and `A_eff≈`[the
   519-cluster] as closed dead ends, not to be re-proposed as T28
   mechanism candidates without new information; recommend a symmetric
   REFUTE band (`refute = best_rel≥0.10 OR null_p≥0.50`) for any future
   reuse of this pattern. Director's/LOGBOOK-editor's call on exact
   placement (new entry vs. R5 addendum), per QUANTUM's own deferral.

6. **Widen Idealization 4** (VISION, non-load-bearing but cheap): name
   both degenerate clusters (`{R_OUT, W_OBJ, W_FLANK}=78`;
   `{TAPER, ABSORB40, PAD80}=40`) and the `aperture_cells=2·A` structural
   redundancy; add one clause to `phase4_results.md`'s tie tables noting
   some listed "N-way ties" collapse to fewer independent coincidences.

7. **Correct the `N=20,000` rationale** (QUANTUM, cosmetic): state the
   actually-operative reason (Monte Carlo resolution at the `p≤0.05`
   decision boundary) rather than "matching the founding test's `N`" —
   the two null tests count structurally different things (noise draws vs.
   null-target draws over differently-sized per-trial search spaces).

8. **Add one QUANTUM-proposed disclosure sentence** to NOTES.md's mandatory
   -caveat section: the beat-frequency algebra in item (b) is classical
   linear superposition, no photon-statistics or coherence-time content —
   given the QUANTUM-OPTICS-lead byline, cheap to forestall ambiguity.

9. **Re-verify live after all text edits**: `python3
   lab/caveat_lint.py` (0 required-site failures, item 1's new entry
   active) and confirm `desk_check_mechanism.py` requires no code change
   (items 2–8 are text-only additions to already-computed, already-
   committed numbers — no re-run should be needed; if any number added
   to NOTES.md/`phase4_results.md` is not already present verbatim in
   `results.json`, compute it via a small script addition, never
   hand-type, per house rule R4).

None of these nine items requires new `lab/` engine code, a new FDTD call,
or a change to the batch's own zero-cost, reuse-only construction.

---

## Overall verdict: **PARTIAL**

Real, load-bearing process work: the standing exp-069 forward tripwire is
discharged: one T28 sub-hypothesis is cleanly killed (item c); the
named-constant search methodology's own null-controlled-search lesson is a
genuine, generalizable house-rule addition, independently reproduced by
every reviewing seat and this audit alike. But the substantive question —
what actually produces T28's ~2.84°-family periodicity — ends narrowed, not
answered: P-070-1's CONFIRM is real but softer than its own prose states
(§2), and P-070-2/4/5 correctly establish that this cycle's own desk
arithmetic contributes no surviving candidate. Six-for-six seat convergence
on EM's C60/C70 test as the correct next step is confirmed, not disputed.
No Checkpoint criterion fires. Full record reviewed: `phase1_proposal.md`,
all five Phase-2 critiques, `phase2_redteam_audit.md`, `phase3_synthesis.md`,
`NOTES.md`, `desk_check_mechanism.py`, `design_geometry.py`, `results.json`,
`phase4_results.md`, all six Phase-5 reviews.
