# PHASE 2 — CRITIQUE · VISION SCIENCE · Panel Iteration 46 (exp-069)

*Fresh sub-agent, VISION SCIENCE charter, blind to other seats' Phase-2
critiques this cycle. My own seat led Iteration 42 (exp-065), which built
Block MINI and discovered the P-VIS42-10 power gap this cycle is fixing.*

## Steel-man (≤150 words)

This is the most literal fulfillment yet of the LOCKED text: the mandate
asked for "≥2–3 T21 periods at ~0.2° spacing, settled STEPS≥2800,
desk-first" and the design delivers 31 points, 0.2° step, 3.03 periods,
STEPS=2800, with the desk check actually run first this time (unlike
Iteration 45, where Red Team's own audit silently dropped that half). It
also fixes the deepest defect in the original instrument: P-VIS42-10's
REFUTE clause was conjunctive but `run.py` only ever coded the amplitude
half (Red Team's Phase-5 catch) — §4 now codes the missing period-match
statistic with T fixed from first-principles geometry (`cpl/A`), not a
free fit, avoiding a new R4/R5-class unfalsifiable-regressor risk. Zero
`lab/` diff, G-1 identity gate, and a genuinely orthogonal C80 3-point
settling closure (P-069-4) at zero marginal design cost. This is real
statistical-power engineering, not a fourth relabel.

## Sharpest attack (≤150 words)

The Combined-verdict row (§5) reopens exactly the escape hatch the LOCKED
mandate exists to close. §1's narrative claims "either outcome closes the
item for good," but §5's actual logic has three buckets: REFUTE-REFUTE,
CONFIRM-CONFIRM, and "any other combination ⇒ PARTIAL... not forced into
either claim." PLAN.md's mandate requires "run the properly-powered test
**or** formally retire it with a stated reason — no further relabeling."
The proposal never states what happens if PARTIAL lands: nothing commits
Phase 3 to a retirement action, so "PARTIAL, reported as such" could
become Iteration 47's fourth/fifth deferral, dressed as rigor instead of
neglect. Compounding this: §1's own history is misattributed — "exp-066
later proved unsettled... by 59.8–74.4%" is wrong on both figures. 74.4%
is exp-065's C40 convergence trend; 59.8% is exp-065's own P-VIS42-11
(C80/40°/600nm) — exp-066 tested only C40, never C80 (its NOTES.md Setup:
"exp-041/exp-065's C40 config, unchanged"). A proposal built to close a
citation-discipline gap should not itself misattribute the very finding
that motivates it.

## Line-by-line arithmetic audit

- §3 cost: `31×(50.0+69.6) = 3707.6` — **checks out**. SETTLE-C80
  `2×104.4 = 208.8` — **checks out**. Total CPU `3916.4` — **checks out**.
- Wall formula `1.15 × 3916.4 / (4 × 0.98) = 1148.9 s ≈ 19.15 min` —
  **checks out**, and matches `design_geometry.fdtd_budget()`'s own
  formula in `experiments/065-.../design_geometry.py` line 433
  (`OVERHEAD_FACTOR * cpu / (N_WORKERS * PARALLEL_EFFICIENCY)`)
  term-for-term, not a re-derived approximation.
- 3× envelope `1148.9×3 = 3446.7 s ≈ 57.4 min` — **checks out**.
- θ list: center 39.0, half-span 3.0, step 0.2 → range [36.0, 42.0],
  `(42.0−36.0)/0.2 + 1 = 31` — **internally consistent**, and 38.0/40.0
  land exactly on the grid as claimed (needed for the G-1 gate).
- `T = cpl/A = 20/752 = 0.0265957...` — rounds correctly.
- One open question, not an error: the desk check that justifies scoping
  to 600nm-only measures the **settling** delta (`C_2800 − C_1400`) at
  fixed padding, not the **padding** delta (`C80 − C40`) Block MINI
  actually scores — a different quantity. Its "flip-fraction 1.0" at
  600nm is samples landing almost exactly at Nyquist for `P(40°,600nm)`
  (0.5027 samples/period), which is consistent with genuine period-lock
  but is also the sampling regime most prone to a false-alternation
  read. Using it to pre-commit away 450/750nm for the *actual* scored
  quantity is a plausible transfer, not a demonstrated one — disclosed
  nowhere in §6's idealizations as an assumption, only as a wavelength
  choice.

## Verdict: **support-with-changes**

The design itself is sound and is the strongest-yet attempt to give Block
MINI the power this program always owed it. But Phase 3 must not be
allowed to write "PARTIAL" and move on: it should adopt a stated,
pre-committed rule now — e.g., any non-decisive combined outcome triggers
automatic formal retirement of the period-match test (with reason) at
this exact close, not a fifth deferral — before the run, not after. The
misattribution in §1 should also be corrected (exp-065, not exp-066) so
the committed NOTES.md doesn't ship a wrong provenance for its own
motivating fact.

## Single parameter change that would flip my verdict

Add one line to §5's Combined-verdict row, pre-committed before the run:
*"A PARTIAL combined outcome is not treated as inconclusive-and-deferred;
it triggers immediate formal retirement of the period-match test at this
cycle's own close, stated reason: statistical power was raised to the
mandate's own spec and the result is still non-decisive, which is itself
the finding."* Without that sentence, this is support-with-changes; with
it, this is unconditional support.
