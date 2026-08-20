# PHASE 3 — SYNTHESIS · Panel Iteration 26 (exp-049) · Director

*Director role per PANEL.md: synthesizes, does not vote, states which
criticisms are accepted and which are overridden, and writes NOTES.md with
predictions committed to git BEFORE the run.*

## Disposition of Phase 2

All five blind critiques returned **support-with-changes**. Red Team's
sequential audit (everything: proposal + all five critiques), having
independently re-derived or re-run every load-bearing claim against live
code, ruled **PROCEED-WITH-MANDATORY-FIXES** with an 8-item docket, two items
(Attacks 5 and 7) elevated above the blind seats' own framing after Red Team
found QUANTUM's proposed fix formula doesn't work and found a defect (the
P-NCONV26-0 regression gate's non-executability) that none of the five blind
seats caught.

**All 8 mandatory-fix items are ADOPTED IN FULL. None overridden.** Red
Team's own docket already resolved the one place a Phase-2 tension existed
(QUANTUM's fix formula vs. what actually works, verified by running both) —
there is no seat disagreement left for the Director to arbitrate; the docket
is unanimous plus independently strengthened. Disposition of each item:

1. **[Attack 5 — Δrel exemption]** ADOPTED as Red Team's corrected formula,
   not QUANTUM's original: `Δrel(n) = 100·|C(2n)−C(n)|/|C(2n)|` when
   `|C(2n)|≥C_THR`; else judge on `Δabs≤ABS_TOL` alone. Applied across the
   full 36×3 grid (not just the 9 FWHM=20° cells) per Red Team's own finding
   that 4 FWHM=10° combinations show the identical artifact.
2. **[Attack 7 — P-NCONV26-0 executability]** ADOPTED via Red Team's option
   (ii): restate the regression gate against what
   `experiments/046-.../results.json` actually contains (the two worst-cell
   figures, committed convention only, plus the two integer threshold
   counts) rather than a fictional 36-cell table, and rather than silently
   importing `beam_divergence_coherent_corrected` from exp-046's own
   `run.py` — which would widen this audit's declared 3-function scope for
   one regression check alone. This keeps the cycle's own function-count,
   cost accounting (Attack 4), and scope statement (§2.0/idealization 5)
   internally consistent, at the cost of a weaker (but honestly labeled)
   regression check. Director's reasoning for choosing (ii) over (i): the
   proposal's own §2.0 table and idealization 5 both commit to exactly three
   functions; adding a fourth to satisfy one sub-clause of one prediction is
   the kind of scope drift PANEL.md's Phase-3 synthesis exists to resist,
   and Red Team offered both options as equally valid — (ii) is strictly
   cheaper and equally sound.
3. **[Attack 2 — P-NCONV26-2 per-function split]** ADOPTED. Three separate
   Spearman correlations, one per function, each its own ≥0.70 confirm bar;
   operational definition stated explicitly (§ below) to remove the
   ambiguity Red Team's −0.343 pooled counter-example exposed. Idealization
   4's "predicted to track similarly" language corrected to state the
   measured Phase-2 split (ρ=0.717 incoherent / 0.600 corrected / 0.450
   coherent) as the actual, disclosed, pre-Phase-4 prior — not a claim of
   similarity.
4. **[Attack 4 — completeness ledger + profiled cost]** ADOPTED. `run.py`
   emits a per-(cell, function, N_SERIES-entry) completeness record; cost
   budgeted from Red Team's measured ≈52-minute single-threaded figure, not
   the Phase-1 proposal's own (now-superseded) ~20-minute estimate.
5. **[Attack 1 — MATERIALS' geometry-scope trigger]** ADOPTED. A committed
   follow-up trigger is added to PLAN.md's queue at shift close-out: this
   sweep's n* findings are scoped to exp-042/046's A=752 geometry only and
   must not be cited as governing exp-048's A=724 fallback geometry without
   a fresh, cheap re-run there.
6. **[Attack 6 — VISION's inline T24 caveat]** ADOPTED. Sentence attached
   directly to P-NCONV26-5's own prediction text in the frozen predictions
   below, not left in an idealization alone.
7. **[Attack 3 — THERMO's arithmetic correction]** ADOPTED. P-NCONV26-5's
   margin restated as 1.247972852046454× / 24.7973%.
8. **[Attack 8 — P-NCONV26-4's unfalsifiable aside]** ADOPTED via demotion:
   the specific "n*∈{641,1281} at the hardest cell" sub-claim is restated as
   descriptive-only (motivating why N_SERIES extends to 5121), not as a
   scored falsifier, per Red Team's own finding that it is currently
   unfalsifiable as written and, when checked, measured wrong (true n*=81 at
   that cell — a real result about how fast a window-averaged Weber contrast
   converges relative to a raw fringe amplitude, now stated as an honest
   *finding*, not a pre-registered miss).

## The corrected experimental design

Superseding §2.2 of `phase1_proposal.md` (preserved unedited there as the
historical Phase-1 record, per this program's own "flag, don't rewrite"
convention — T10/exp-045/exp-046 precedent):

**Convergence criterion (corrected):** for function f, cell c, doubling step
n→2n:

> `Δabs(n) = |C(2n) − C(n)|`
> `Δrel(n) = 100·|C(2n) − C(n)| / |C(2n)|` **if** `|C(2n)| ≥ C_THR=0.005`,
> **else the relative-error clause is exempted** and the step is judged on
> `Δabs(n) ≤ ABS_TOL=5×10⁻⁴` alone.
> A doubling step CONVERGES iff `Δabs(n) ≤ ABS_TOL` AND (Δrel exempted OR
> `Δrel(n) ≤ REL_TOL=1.0%`).

Trustworthy order n* is still the smallest N_SERIES entry where two
consecutive doublings both converge (§2.2's original two-consecutive-pass
discipline, unchanged — Red Team found no defect in that part).

**P-NCONV26-2's operational correlation, stated explicitly:** for each
function f ∈ {incoherent, incoherent_corrected, coherent} independently,
compute Spearman ρ between §2.1's predicted difficulty ranking (9 cells,
ties broken by the stated λ-primary/θ₀-secondary order) and the measured
`Δrel(41→81)` magnitude at those same 9 cells, **using the corrected Δrel
formula above** (so a near-zero-|C| cell contributes its exempted status,
not a runaway percentage, to the ranking). Each of the three ρ values is
scored against its own ≥0.70 confirm bar independently; there is no pooled
statistic.

**P-NCONV26-0, restated:** reproduce, from unmodified
`experiments/046-.../results.json`
(`block_a_aperture_consistent_beam.angular_sampling_convergence`), exactly
the four numbers that file records — `worst_rel_move_committed_convention_pct
= 4.472688822027389`, `n_cells_above_1pct_committed = 2`,
`n_cells_above_0p16pct_committed = 3`, and the worst-cell identity — computed
via this audit's own `beam_divergence_coherent` at n=41 and n=401 (committed
convention only; the corrected-convention comparison is dropped, not
silently satisfied by an out-of-scope function).

All other structure (N_SERIES, the 36-cell grid, the three in-scope
functions, idealizations 1–3/5–9) carries forward from `phase1_proposal.md`
unchanged; idealization 4 is corrected per item 3 above.

## Predictions committed BEFORE the run

See `NOTES.md`, written and committed in the same commit as this file,
**before** `run.py` is executed. House discipline: non-negotiable.
