# PHASE 5 — REVIEW · VISION SCIENCE · Panel Iteration 46 (exp-069)

*Fresh sub-agent, VISION SCIENCE charter. Blind to any other seat's Phase-5
review this cycle. Read PANEL.md, LOGBOOK.md in full, PLAN.md's current
state + Iteration-46 queue, and this cycle's complete record (Phase 1–4,
NOTES.md, results.json) before writing this review.*

## 0. What this review checked, and how

Per this seat's own standing signature (LOGBOOK Iteration 45/exp-068's
five-finding sweep), this is a line-by-line audit, not a prose read. I did
five independent things beyond reading the record:

1. Hand-recomputed `ptp`, `mean`, `ratio` (P-069-1); `rel_dev` (P-069-3);
   both `P-069-4` cells; both `P-069-5` cells; and `ptp`/`mean`/`ratio`/
   `n_periods` (P-069-6) directly from `results.json`'s raw per-angle rows
   — not trusting the `scored` block's own arithmetic.
2. Re-ran `python3 design_geometry.py` myself and diffed its printed
   budget (100 calls, 6637.3 CPU-s, wall 32.45 min, 3× envelope 97.36 min)
   against every number quoted in `NOTES.md`/`phase3_synthesis.md`.
3. Loaded `experiments/065-.../settled_sweep_steps2800_diagnostic.json`
   directly and diffed all four G-1 reference values against
   `results.json`'s own `g1.checks[].ref` — confirming the gate cites a
   real, pre-existing committed file, not a fabricated one.
4. Grepped every committed file in this cycle for the string `PARTIAL` and
   for the misattributed `59.8`/`74.4` figures, to check the two
   mandatory-fix claims empirically rather than trusting the prose that
   says they were fixed.
5. Checked `git log`/`git diff --stat -- lab/` directly: `lab/` is clean,
   and the Phase-3 predictions commit (`95bc6dd`) precedes the Phase-4
   results commit (`c32a3fd`) — predict-before-run is real, not asserted.

**Everything below is independently reproduced, not restated from
`phase4_results.md`.**

## 1. The PARTIAL escape hatch — CLOSED, verified three independent ways

My own Phase-2 critique's sharpest attack was that §5's Combined-verdict
row had a third bucket ("any other combination ⇒ PARTIAL... not forced
into either claim") with no stated consequence — structurally identical to
the citation-tripwire-only pattern that fired Checkpoint criterion 4 one
cycle ago on this exact test. Checking whether that hatch is actually
closed, not just promised to be closed, requires three separate checks,
and all three pass:

**(a) Red Team's Phase-2 audit adopted the fix as the single highest
priority, not a footnote.** `phase2_redteam_audit.md`'s own Attack 4 names
it "the sharpest structural gap," explicitly credits my own Phase-2
critique, and its §3 "Decisive rulings" section states: *"Yes,
unconditionally... This is the single highest-priority fix in this
docket."* Mandatory-fix-4's text is my own proposed sentence, adopted
"essentially verbatim."

**(b) The fix is a genuine code branch, not prose.** I read `run.py::score()`
directly (lines 420–444). The Combined Verdict is a strict three-way
`if/elif/else`: `COHERENT_FRINGE_FULLY_CORROBORATED` (5-way conjunction),
`ADDITIVE_SYSTEMATIC_VINDICATED` (2-way conjunction), or
`FORMAL_RETIREMENT_NON_DECISIVE` with a reason string computed inline.
**There is no third string anywhere in the code path that says "PARTIAL"
or defers.** I grepped `run.py`, `results.json`, `NOTES.md`, and
`phase4_results.md` for the literal string `PARTIAL`: every one of the six
hits is the disclaimer "NOT reported as PARTIAL-and-deferred" — zero
instances of an actual PARTIAL verdict being issued anywhere in this
cycle's own committed artifacts.

**(c) The actual scored outcome exercises the retirement branch, correctly.**
P-069-1 REFUTE (`ratio=16.20`, independently recomputed and confirmed
exact), P-069-2 NEITHER (`R²=0.2016`, inside the 0.15–0.50 gray zone),
P-069-3 NEITHER (`rel_dev=44.95%`, inside the 20–50% gray zone), P-069-4
CONFIRM, P-069-5 CONFIRM. Neither the 5-way nor the 2-way gate closes
(P-069-2 satisfies neither its own confirm nor refute band), so the code
correctly falls to `FORMAL_RETIREMENT_NON_DECISIVE` — verified by tracing
the actual boolean values through `score()`'s own `if coherent / elif
additive / else` by hand, not by trusting the printed label.

Attack 1 (a second, related gap my critique did not itself catch — the
"not settling" language never actually gated by P-069-4) was also fixed
correctly: the `coherent` branch's own `combined_reason` string states
"settling CONFIRM, resolution CONFIRM" as a direct consequence of the
conjunction, not an unguarded side-claim. I confirmed this is watertight
by checking that `p4["confirm"]` is one of the five terms `and`-ed into
`coherent` in the actual source, not merely documented as such.

**Verdict on this specific question: the hatch is genuinely closed, at the
code level, not just in this cycle's prose.** This is the strongest form
of closure this program's own house discipline can produce — a
pre-committed, git-committed-before-the-run decision rule, exercised
mechanically by the real scored data, with no PARTIAL string reachable
from any branch.

## 2. Is "New live thread T28" Block MINI relabeled, or genuinely new?

This is the sharper, second-order question, and it deserves equal
scrutiny: closing the *specific* Block MINI test cleanly is not the same
as closing the underlying *pattern* of endless deferral if the very next
paragraph reopens the identical question under a new thread number.

**My reading, after tracing the actual claims: T28 is a legitimately
different question, not T21/Block MINI relabeled — but it inherits real
structural risk from the same lineage, worth a pre-emptive tripwire.**

Reasoning:

- Block MINI's own, specific, LOCKED question was: *does the
  `C80−C40` padding-delta oscillation phase-lock to T21's own
  established, zero-free-parameter continuum-diffraction period,
  `P(θ)=λ/(A·cosθ)`?* That question got a clean, non-ambiguous answer:
  **no** — the best global fit lands at `P*=2.84°`, 45% off `P(39°)=1.96°`,
  outside the 20% within-tolerance band and just short of the 50%
  out-of-tolerance band, with a solid `R²=0.6272` (i.e., not noise finding
  a spurious period — a real, comparably well-determined *different*
  period). This is a well-powered, decisive non-match, and the
  pre-committed rule correctly retires the specific test that was built to
  answer that specific question.
- What's left over is a **new empirical fact this program did not
  previously have**: the padding delta itself is real, resolution-robust
  (P-069-5 CONFIRM, ratio 1.97/2.50 at cpl 20→30, same sign both angles)
  and settling-robust (P-069-4 CONFIRM, both cells ≪0.01% relative shift
  4200-vs-2800), oscillating at a *different, specific* period. Nobody
  in this program's history knew this delta had any real periodic
  structure at all before this cycle — Block MINI's original 5-point,
  0.5°-step, STEPS=1400 test could not have resolved it either way.
- Critically, `phase4_results.md`'s own candidate-mechanism list for T28
  points **away** from T21's mechanism space (source/aperture edge
  diffraction, governed by `A`) and toward a structurally different
  length scale: *"a boundary-thickness-scale mechanism specific to the
  `ABSORB` band itself (T24's own original subject, never actually
  isolated from the source/aperture geometry T21 governs)."* `C40` and
  `C80` differ in exactly two things by construction: `ABSORB` (40 vs 80)
  and `pad` (0 vs 40) — both T24-lineage quantities, not T21-lineage ones.
  A periodic structure tied to *that* difference, at a *different* period
  than T21's own `A`-governed fringe, is a coherent, falsifiable, genuinely
  new hypothesis — not a repackaging of the old one.
- The write-up treats it with the right weight, not an inflated one: it
  explicitly **declines** Checkpoint-criterion-2 candidacy ("T28 is a real,
  unresolved mechanism question, not yet a proven mechanism-class
  boundary" — correct; no constraint-set has been shown jointly
  unsatisfiable here), and explicitly queues it as **"ordinary backlog, not
  locked"** — a deliberate, stated difference from how Block MINI itself
  was carried forward as a mounting, eventually-LOCKED item for three-plus
  cycles. That distinction is exactly the discipline the mandate was
  written to enforce, applied correctly to the new finding rather than
  only to the old one.

**Residual risk, not a defect in this cycle's own record:** this program's
own history (T20→T21→T24→T27→T28, five threads deep, Iterations 18
through 46) shows a structural tendency for every resolved question's
residual to spin off a new named thread, several of which (T21 itself,
T24) took upward of twenty iterations to reach a properly-powered test.
T28 is legitimately new today; nothing about *this* cycle indicates it is
being used to smuggle a deferral. But if T28 is left to sit as ordinary,
un-prioritized backlog for three-plus cycles the way `P-VIS42-10` was, this
program will have reproduced the exact failure shape one thread later —
just with a clean conscience about the immediate cycle that opened it. I
recommend a cheap, explicit tripwire now (see §5) rather than waiting for
a future Checkpoint-4 firing to notice the pattern again.

## 3. Full numeric cross-check — `phase4_results.md`/`NOTES.md` vs `results.json`

Every number below was independently recomputed from `results.json`'s raw
per-angle rows, not copied from the scored block or the prose.

| Quantity | My recomputation | `results.json` `scored` | `phase4_results.md`/`NOTES.md` prose | Match |
|---|---|---|---|---|
| P-069-1 `ptp` | 0.00402626 (max@37.2° − min@41.6°) | 0.004026256293785282 | "ptp=0.004026" | exact |
| P-069-1 `mean` | −0.00024853 (Σ31/31) | −0.000248529423384259 | "mean=−0.000249" | exact |
| P-069-1 `ratio` | 16.2003 | 16.200320424677294 | "ratio=16.20" | exact |
| P-069-2 `R²` | (fit re-derivable; not hand-refit — a 3-param OLS, low bug-surface, cross-checked via P-069-6's independent 750nm fit using the identical `_fixed_period_fit` code path, self-consistent) | 0.20164960065653104 | "R²=0.2016" | exact (as reported) |
| P-069-3 `P*`, `rel_dev` | rel_dev = \|2.84211−1.96080\|/1.96080 = 0.4495 | `p_star_deg=2.8421052631578947`, `rel_dev=0.44946577727371634` | "P*=2.84°... 45% off... R²=0.63" | exact |
| P-069-4 θ=39° `rel` | \|C4200−C2800\|/\|C2800−C1400\| = 9.288e-8/0.0033817 = 2.747e-5 | 2.746641496329539e-05 | "2.7×10⁻⁵" | exact |
| P-069-4 θ=40° `rel` | 6.634e-8/0.0039273 = 1.689e-5 | 1.6892442255289214e-05 | "1.7×10⁻⁵" | exact |
| P-069-5 θ=39° ratio | 0.00023022/0.00011678 = 1.9714 | 1.9714293677163448 | "1.97" | exact |
| P-069-5 θ=40° ratio | 0.00041624/0.00016660 = 2.4985 | 2.4985190290855552 | "2.50" | exact |
| P-069-6 `ptp`, `mean`, `ratio` | 0.0084025, 0.0029034, 2.8940 | 0.008402496442399765 / 0.0029034231140690338 / 2.8939965386663866 | "ratio=2.89" | exact |
| P-069-6 `n_periods` | 3.0/2.45099 = 1.2240 | 1.2239933230311382 | "~1.22 periods" | exact |
| G-1 all 4 cells | diffed directly against `experiments/065-.../settled_sweep_steps2800_diagnostic.json` | `delta=0.0` all four, `ref` values bit-identical to the exp-065 file on disk | "4/4 exact" | exact, and the reference file is real, not fabricated |
| `design_geometry.py` budget | re-ran the script myself: 100 calls, 6637.3 CPU-s, wall 32.45 min, envelope 97.36 min | — (not in results.json) | "100 calls, ≈6637 CPU-s, wall ≈32.5 min... 97.4 min" | exact |

**Zero transcription errors found, at any precision.** This is a
meaningfully cleaner arithmetic record than several recent cycles this
program has logged (cf. Iteration 44's shipped sign-inverted formula,
Iteration 42's P-VIS42-6/7 propagation gap) — the difference here is a
computed, code-sourced Combined Verdict and code-sourced budget table
(house rule R4, "never hand-typed") rather than hand-derived prose
figures, which structurally removes most of the surface area those past
errors occupied.

## 4. `NOTES.md` Result/Learned/Next — consistency check

`NOTES.md`'s post-Phase-4 "Result" section states `ptp/|mean|=16.20`,
`R²=0.2016`, `P*=2.84°` at 45% deviation with `R²=0.63`, both P-069-4/5
CONFIRM, and `Combined Verdict: FORMAL_RETIREMENT_NON_DECISIVE` — all
match `results.json`/`phase4_results.md` exactly (checked above). The
"Learned" section's three points are consistent with the scored data (a
real periodic signal exists; its period does not match T21's; properly
powering a chronically-deferred test can produce an honest non-result).
The "Next" section correctly states Block MINI is retired, not "still
pending," and correctly scopes T28 as unlocked backlog — matching
`phase4_results.md`'s own framing exactly, no drift between the two files.

Mandatory-fix-8's misattribution correction (`exp-066` never tested `C80`;
the 59.8%/74.4% figures both belong to `exp-065`) is verified **absent**
from every committed file in this cycle — I grepped `NOTES.md`,
`phase4_results.md`, `results.json`, and `desk_check_settling_delta.py`
for both figures and for `exp-066`/`exp-065`; the only surviving
`exp-066` references are correctly-scoped citations to `exp-066`'s real
36-cell Block MAIN settling dataset (which `exp-066` did produce), never
a claim that `exp-066` tested `C80`.

## 5. `design_geometry.py`/`run.py` — STEPS/cpl/θ bookkeeping

No off-by-one or unit confusion found. Specifically checked:

- `DENSE_ANGLES` construction (`center ± i·step`, `i∈[-15,15]`) produces
  exactly 31 points, `36.0` to `42.0`, both asserted in code and verified
  by re-running the script — 38.0°/40.0° land exactly on the grid as
  required for the G-1 gate.
- `T_SINTHETA_600 = CPL[600]/A = 20/752 = 0.026595744...` — correct, and
  independently re-derived as the exact period of `sinθ` for the
  established `P(θ)=λ/(A·cosθ)` formula's own first-order behavior (a
  self-consistency check on a fitted model, correctly *not* oversold as
  independent verification — Idealization 5's hedge is honored throughout
  the scoring code, not just the prose, per mandatory fix 2).
- `R3` rescale constants (`R3_BASE_PLANE_X=116`, `R3_BASE_GUARD_OUT=278`,
  `R3_RATIO=1.5`, `R3_CPL={600:30}`) — I independently diffed these
  against `experiments/033-.../design_geometry.py`'s own committed R3
  precedent (`PLANE_X=116`, `GUARD_OUT=278`, `RATIO=1.5`, `CPL=30`) and
  they match bit-for-bit, confirming this is a genuine reuse of an
  established idiom, not a superficially-similar new construction.
- `R3_STEPS=4200` deliberately coincides numerically with the unrelated
  `STEPS_STRESS=4200` (native-cpl settling stress test) — the code and
  comments explicitly disclose this as a coincidence of two *different*
  quantities at *different* resolutions, not a shared value smuggled
  across contexts. Correct and appropriately flagged.
- `A_HALF_APERTURE=752` is asserted equal across `CONFIGS["C40"]["A"]` and
  `CONFIGS["C80"]["A"]` at import time (line 114), and the R3-rescaled `A`
  is separately asserted equal to `round(752×1.5)=1128` at both R3 configs
  (line 217) — both congruent-construction identities are enforced by
  code, not merely claimed.

## 6. Does this cycle satisfy PLAN.md's LOCKED "no further relabeling, no
further citation-tripwire-only treatment"?

**Yes**, on the specific, narrow scope the mandate names — Block MINI's
period-match test itself. The test was built to the mandate's own
literal spec (≥2–3 T21 periods — delivered 3.06; ~0.2° spacing — delivered
exactly; settled STEPS≥2800 — delivered, with a first-ever C80 3-point
convergence closure beyond it; desk-first — delivered, and this time
actually run first, unlike Iteration 45's own silent drop of the
identical QUANTUM-proposed desk check). Its result is genuinely
non-decisive by a properly-powered test, and the pre-committed,
code-executed rule retired it rather than deferring it a fifth time. This
is not a citation-tripwire-only treatment (the underlying test was
*actually run*, at the mandated power) and it is not a relabel (the
verdict string is a new, distinct outcome class — `FORMAL_RETIREMENT_
NON_DECISIVE` — not `P-VIS42-10`'s old verdict renamed).

The one place I would push back, gently, on "satisfied in full": the
mandate's spirit is about this program's own deferral pattern generally,
not only this one test's letter. T28 is real and legitimately new (§2),
but it is also exactly the kind of loose end that, left unscheduled for
several cycles, becomes the next Checkpoint-4 firing. Closing the letter
of the mandate on Block MINI while leaving an equally-shaped open question
sitting as ordinary backlog is a smaller version of the same risk — not a
violation this cycle, but worth naming explicitly rather than only
noticing it in three cycles' time.

## Verdict: **PARTIAL**

Not RULED OUT — nothing here forecloses a mechanism class or proves a
jointly-unsatisfiable constraint set; T24's own inheritance question (does
the boundary systematic transfer as additive or something else) is now
better-informed, not worse. Not PROMISING — a LOCKED, four-cycle-deferred
mandate closing on a genuinely non-decisive result, however honestly
reported, is not itself forward progress on T21's original mechanism
question; and a new open thread (T28) is left with no scheduling
commitment, one cycle after this exact program fired Checkpoint criterion
4 for under-scheduling the item T28 descends from.

This is real, disciplined work: the escape hatch is closed at the code
level (not just in prose), the arithmetic is clean across every number I
independently recomputed, and the new finding (a real, resolution- and
settling-robust periodic structure that does *not* match T21's own
mechanism) is reported with exactly the hedged, non-overclaiming language
this program's house discipline requires. PARTIAL reflects that the
cycle's own headline question closed honestly without closing decisively
— the correct, undramatic outcome of a properly-powered null-adjacent
result, not a process failure.

## Ranked top-3 candidate directions for Iteration 47

1. **Give T28 an explicit, cheap, pre-committed first move — before it
   accrues a second undisclosed deferral.** The zero-cost check
   `phase4_results.md` itself names but does not schedule: does `2.84°`
   relate to any *other* geometric quantity this cycle's own construction
   already fixes (the `ABSORB` difference 80−40=40, the `pad` difference
   40−0=40, or a harmonic/subharmonic — `2.84/1.96≈1.45` is flagged as
   "not obviously clean" but was never checked against `ABSORB`- or
   `pad`-derived length scales specifically). This is desk-only, reuses
   already-committed data, and either kills or substantially narrows T28
   before any FDTD spend — directly forestalling the T21-style multi-cycle
   drift this program has now seen twice (T21 itself, T24).
2. **The real, dedicated `measured_direct` R_contact literature search** —
   PLAN.md's Iteration-46 queue item #2, still the only queued item across
   four cycles now that can move a real materials number (TD-5's 7.8×
   margin) rather than relabel or re-verify one; this cycle's own
   mandatory-fix-9 disclosure confirms it remains untouched, still gated
   only on WebSearch/WebFetch tooling availability, not on any rotation
   slot.
3. **Extend the desk-check discipline this cycle modeled to T24's own
   still-open inheritance question.** exp-069's headline finding (§1 of
   `phase4_results.md`: the `C80−C40` delta is real and periodic, not the
   flat additive systematic T24's framing has assumed since Iteration 23)
   directly undercuts the assumption underneath every near-threshold
   constraint-3 τ-bucket call that has ever cited T24's additive-transfer
   claim. A cheap, targeted re-audit of which specific citations depend on
   that assumption (mirroring T27's own `caveat_lint_config.json`
   discipline) is lower-cost than a new FDTD cycle and closes a citation
   integrity gap this cycle's own physics finding just opened.
