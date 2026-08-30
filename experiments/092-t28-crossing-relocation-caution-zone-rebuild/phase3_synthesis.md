# PHASE 3 — SYNTHESIS · Panel Iteration 69 · exp-092 · Director

## 1. Disposition of Red Team's mandatory-fix docket: seven items, zero overridden, plus one Director-caught addition

Red Team's Phase-2 audit (`phase2_redteam_audit.md`) independently re-derived
every load-bearing claim in `phase1_proposal.md` and all five blind
critiques from primary sources (its own §0), including a **fourth**
independent reproduction of Rank 2's DROP/RELABEL table (after EM's own
pre-verification, QUANTUM's independent re-derivation, and my own
independent reproduction before Phase 1 was even committed — see the
Phase-1 commit's own verification step). I re-ran that same fifth
reproduction myself, again, before accepting this synthesis (below, §1.1) —
it remains bit-exact. I adopt Red Team's verdict PROCEED-WITH-MANDATORY-FIXES
and all seven items **in full, none overridden** — every item survived
independent re-derivation by Red Team from source, and none is
discretionary except the one item Red Team itself flagged as such (the
42.0° settling spot-check, addressed in §3 below).

### 1.1 My own independent re-verification before accepting anything

- **Rank 2 table**: re-imported `experiments/090-.../run.py`'s actual
  `firth_logistic`/`auc`/`naive_mle_diverges` functions and re-ran the
  ORIGINAL/DROP/RELABEL recipe against the real `n=7` dataset myself.
  Bit-exact match to Red Team's §0 and every prior independent
  reproduction: `AUC=1.0/1.0/0.8333`, zone
  `[1.4764,2.1709]`/`[1.4764,2.1709]`/`[1.4764,1.3095]` (inverted),
  `m₅₀=2.071013/1.818061/1.031717`. This is now a **fifth** independent
  confirmation.
- **`sigma_max_R3=1/3`**: re-derived from `lab/materials.py::graded_black_shell`
  and `design_geometry.py::R3_RATIO=1.5`, `R3_R_OUT=117`: native
  `τ_center=2×0.5×78=78`; as-filed R3 `τ_center=2×0.5×117=117` (1.5×
  inflation); corrected `sigma_max_R3=78/(2×117)=1/3` exactly. Matches
  Red Team's own §0 derivation.
- **The zero-added-wall-time claim for resequencing** (§2 of the audit):
  independently confirmed the arithmetic is additive regardless of
  execution order — this holds by construction (CPU-time sums are
  commutative), not merely by Red Team's own arithmetic check.

## 2. A Director-level finding, not raised by any of the six prior parties: Rank 3's "zero-cost empty-leg reuse" claim is not actually implementable as specified

Before writing `run.py`, I checked exactly how `phase1_proposal.md`
§4a's claim — "exp-091's own already-committed empty-leg captures... may
be reused directly, verbatim, with zero new FDTD calls" — would be
implemented in code. **It cannot be, as written.** `lab/ambient.py::
contrast_from_runs(scene_profiles, empty_profiles, ...)` computes the
scene contrast `C` from the *raw empty-run profile array*
(`empty_profiles`), not from the previously-computed scalar `C_empty`
value alone — the scene profile is normalized against the empty run's own
per-angle flank mean (`incoherent_sum`'s `b/f` term) inside the *same*
function call that produces the new `C`. Grepped the entire
`experiments/` tree for a persisted raw-capture cache (`.npz`/`.npy`/`.pkl`
files under any T28-family experiment, `069` onward): **none exists** —
that convention was used only by very early experiments (000/001/058) and
was not carried forward. `exp-091`'s own `captures` dict is populated by
its `ProcessPoolExecutor` at runtime and never serialized; only derived
scalar metrics reach `results.json`. **The empty-leg profile array
needed to compute Rank 3's `C` at the sigma-corrected article is not
retrievable from anything committed to git.**

**Fix (Director-added, load-bearing, item 8 below): Rank 3's empty leg
is re-run fresh inside `run.py`, not "reused."** Since `build_article_r3`
is only invoked when `with_article=True` (confirmed by Red Team §0 from
`_run_sim_r3`'s own source), the empty-leg FDTD field is bit-independent
of `sigma_max` — re-running it is a **deterministic reproduction**, not
new information, and a bit-exact match against exp-091's own filed
`C_empty(C40_R3/G40_R3, θ)` values at these three angles becomes a free,
built-in consistency check on this cycle's own machinery (asserted in
`run.py`, not merely hoped for). This raises Rank 3 from 6 to **12
calls** (3 angles × 2 configs × 2 legs — mechanically identical in shape
to exp-091's own Leg 2, at the corrected `sigma_max`), and this cycle's
total from 34 to **40** new FDTD calls. Recomputed budget (§5) stays
inside this sub-thread's own established ~100–150 CPU-min per-cycle band.
This does not change §2 of Red Team's audit (the resequencing ruling):
Rank 3 remains independent of Rank 1's own inputs/outputs in both
directions, and resequencing Rank 3 first still costs zero net wall time
relative to running both blocks in either order (CPU-time is additive
regardless of ordering, confirmed by direct computation, §5).

## 3. Final design — reconciling all eight items (seven Red Team + one Director) into one frozen configuration

1. **[Red Team, load-bearing] Resequence Rank 3 before Rank 1.** `run.py`
   runs Rank 3's (now 12) calls in the first `ProcessPoolExecutor` batch,
   computes Rank 3's verdict (§4 below) from real gates, THEN dispatches
   Rank 1's 28 calls with the `sigma_max` that verdict licenses.
   **Pre-registered branch rule (must be fixed now, before any run, per
   house discipline — a live, undisclosed choice at runtime is not
   permitted):**
   - Rank 3 **CONFIRM** (negligible contamination) → Rank 1's article leg
     runs at `sigma_max=0.5`, matching exp-091's own as-filed convention.
   - Rank 3 **REFUTE** (material contamination) → Rank 1's article leg
     runs at the corrected `sigma_max=1/3`.
   - Rank 3 **NEITHER** → Rank 1's article leg runs at the corrected
     `sigma_max=1/3` (the conservative default: avoid repeating this
     program's own T10/SIGMA_ON precedent of knowingly measuring with a
     systematically-too-strongly-absorbing article when in genuine doubt),
     **disclosed explicitly in the Result section as a NEITHER-triggered
     default, not a CONFIRM-level finding.**
   **Additional disclosure (Red Team's own addition, carried forward
   verbatim):** a Rank-3 REFUTE (or NEITHER-default) reopens Rank 1's own
   §2a net-*placement* logic (derived from uncorrected-article bracket
   data) as provisional for a future cycle — resequencing fixes which
   article Rank 1 measures, not whether the net's own location is still
   correctly aimed under that article. Named forward, not resolved this
   cycle (Idealization 11).
2. **[Red Team, load-bearing] Extend Rank 1's lower net by two more
   `DENSE_ANGLES` points, 39.2°/39.4°** (8 calls, not the docket's own
   "~4" — see §1.1 correction below), on PHOTONICS' own stronger,
   measured-evidence basis (40.2°'s own already-observed sign flip), not
   the struck amplitude-inflation non sequitur. **Rank 1's final angle
   set: {39.2°, 39.4°, 39.6°, 39.8°, 40.0°, 41.8°, 42.0°} — seven points,
   28 calls** (was five points/20 calls). The amplitude-inflation
   sentence in `phase1_proposal.md` §2a is not retroactively edited (house
   convention — a frozen document is corrected forward); `NOTES.md`
   states the corrected justification directly.

   **A second Director-level arithmetic correction**: Red Team's own
   docket item 2 (and PHOTONICS' critique it quotes) states "~4 calls" for
   two new angles. Re-checked against this design's own call structure
   (2 configs × 2 legs per angle, matching the already-verified
   `5 angles × 4 calls/angle = 20 calls` in the original design): **two
   new angles cost 8 calls, not 4** (`2 angles × 2 configs × 2 legs`).
   PHOTONICS' own critique text ("~4-call points," read as an adjectival
   per-point figure) is consistent with this; Red Team's own restatement
   in the docket ("39.2°/39.4°, ~4 calls," read as a total) is not. Fixed
   here; the total call count and budget (§5) use the corrected figure.
3. **[Red Team, non-load-bearing] Pre-register a `p_abs_w`/`ratio_abs_ext`
   band for Rank 3.** Adopted as `NOTES.md` §Predictions (R3b):
   `p_abs_w` ratio `[0.3,3.0]` CONFIRM / `[0.1,10]` REFUTE (THERMODYNAMICS'
   own band, mirroring exp-091's own (b2) convention), reported as its own
   PRIMARY-but-non-gating prediction — it does **not** feed Rank 3's
   sigma_max branch decision (§4 below uses `delta_scene`/`frac_contrast`
   only, matching the proposal's own original framing of what the branch
   tests: the PRIMARY interference channel, not the energy channel).
   `ratio_abs_ext` reported disclosed, checked for staying within ~2–3%
   of the established T9 `≈0.51` anchor, non-gating.
4. **[Red Team, non-load-bearing] Correct the Rank-3 justification
   wording.** `NOTES.md` states plainly that the reused `[0.3,3.0]`/
   `[0.1,10]` band is a repurposed, generic magnitude/sign tolerance, not
   evidence that the sigma-correction question and exp-091's own
   resolution-rescale question are the same kind of test (RT-1).
5. **[Red Team, non-load-bearing] Rewrite Idealization 8's settling
   argument.** Restated in `NOTES.md` to argue from the depth-of-convergence
   margin at the three already-checked settling angles (exp-091's own
   `10⁻⁷`–`10⁻⁴` relative deviation, six-plus orders of magnitude inside the
   `≤1%` bar), with an explicit T27 cross-reference (RT-2), rather than a
   blanket "not angle-dependent" claim. **The optional 42.0° settling
   spot-check is declined this cycle**, explicitly: it is Red Team's own
   named discretionary item, its cost (~1614.6 CPU-s, comparable in size
   to Rank 1's entire two-point net extension) is not free, and this
   cycle's own budget (§5) is already at the top of this sub-thread's
   established band once items 1–2/8 are folded in. Named forward as a
   candidate first item if Rank 1's REFUTE outcome (§6 of
   `phase1_proposal.md`) is realized at the 42.0° edge specifically.
6. **[Red Team, non-load-bearing] Restore exp-091's own Idealization 8**
   (the "no full 31-point R3 rebuild" half) to `NOTES.md`'s idealizations
   list.
7. **[Red Team, non-load-bearing] Fix the print-parity gap in `run.py`
   itself**, this cycle, before it reproduces exp-091's exact defect a
   second time: `netd_disclaimer`/`scope_note` (and this cycle's own new
   `sigma_branch_disclaimer`, §4) are `print()`-ed to `run_output.txt`,
   not only written to the `results.json`-bound dict.
8. **[Director] Rank 3's empty leg is re-run fresh, not reused** (§2
   above) — 12 calls, not 6; a bit-exact-match assertion against exp-091's
   own filed `C_empty` values is added as a built-in consistency check.

## 4. Rank 3's branch verdict — the exact gate, fixed before any run

Reusing `experiments/091-.../run.py::ratio_sign_verdict` verbatim (the
same `[0.3,3.0]` CONFIRM / `[0.1,10]` REFUTE / else NEITHER logic already
used for exp-091's own (a) and (b2)), applied to **`delta_scene`**
(ratio = sigma-corrected/as-filed, sign_match = same sign) **AND**
**`frac_contrast`** (ratio only; always non-negative, so "sign_match"
is fixed `True` by construction — a REFUTE on this quantity can only come
from the ratio itself falling outside `[0.1,10]`) at all three census
angles, six (ratio, sign_match) cells total. **Overall Rank-3 verdict =
worst case across all six cells**: REFUTE if any cell REFUTEs; CONFIRM
only if all six cells CONFIRM; else NEITHER. This is the gate item 1's
branch rule above consumes — fixed, mechanical, and stated here strictly
before `run.py` exists.

## 5. Final call count and cost (re-derived by hand, corrected per §§2–3)

| Block | Calls | CPU-s | Basis |
|---|---|---|---|
| Rank 3 (3 angles × 2 configs × 2 legs, `STEPS=4200`) | 12 | `3×2×(168.75+234.9)=2421.9` | identical shape to exp-091's own Leg 2 |
| Rank 1 (7 angles × 2 configs × 2 legs, `STEPS=4200`) | 28 | `7×2×(168.75+234.9)=5651.1` | |
| **Total** | **40** | **8073.0 CPU-s ≈ 134.6 CPU-min** | |

Wall time at `N_WORKERS=4, PARALLEL_EFFICIENCY=0.98, OVERHEAD_FACTOR=1.15`
(unchanged house constants): `1.15×8073.0/(4×0.98)≈2368s≈39.5min`; 3×
safety envelope ≈ 118.5 min. **Resequencing itself changes neither
figure** — confirmed by direct computation, `wall(Rank 3 alone)≈693s` +
`wall(Rank 1 alone)≈1675s`≈`2368s`, matching the combined total exactly
(CPU-time is additive regardless of order). This sits at the top of, but
inside, the ~100–150 CPU-min band this sub-thread has used since exp-069
(exp-091 itself: 125.6 CPU-min/36.9 min wall/111 min envelope) — the two
Director-level corrections (§1.1/§2, §3 item 2) both push the budget up
from the as-filed proposal's 87.5 CPU-min, not down; both are load-bearing
to the design's own scientific validity, not discretionary padding.

## 6. What this synthesis does NOT change

No item — Red Team's seven or my own eighth — asks for a different
mechanism, a relaxed threshold, or a re-opened ruled-out question.
**T1 route N/A, Checkpoint criterion 2 N/A**, confirmed independently by
Red Team (§4 of its audit) against the unbroken LOGBOOK record for this
sub-thread since exp-069, re-confirmed here. R13/R14/R15 are applied
unchanged. No new numbered rule is being proposed by this synthesis.

## 7. Checkpoint criteria

Worked through explicitly, matching Red Team's own §5: none fire.
**Criterion 4** (program-integrity drift): every finding this cycle — five
upheld blind-critique attacks, two Red-Team-original attacks, and my own
two Director-level catches (§1.1's arithmetic slip, §2's empty-leg-reuse
defect) — was caught before Phase 3 freeze, all fixed in this same
synthesis, none a recurrence of a "known, named, ignored" defect.
**Criterion 5** (two non-advancing cycles): N/A — exp-091 was itself
logbook-advancing (R15 adopted, the caution zone materially revised), and
this cycle directly attempts to locate the crossings R15 itself left as
the single most consequential open question.

## 8. Predictions frozen

See `NOTES.md`, committed in this same push, strictly before any Phase-4
`run.py` exists — house discipline, non-negotiable.
