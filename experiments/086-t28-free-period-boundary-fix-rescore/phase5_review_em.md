# PHASE 5 — REVIEW · ELECTROMAGNETISM · Panel Iteration 63 · exp-086

*Fresh context, blind to every other seat's current-cycle Phase-5 review.
This seat led this cycle's Phase 1; this review is an independent
re-check of the final, post-Phase-2/3/4 record against what actually ran
and was committed — not a rubber stamp of my own earlier proposal.*

## 1. Charter-specific task: is `shape_r_squared_pad`/`shape_r_squared_absorb40` really independent of the R11 bug?

**Verified true, by direct source trace, not taken on the Director's word.**

`shape_r_squared_pad`/`shape_r_squared_absorb40` (and their two-wall
siblings) are written in `pad_round_trip_model.py` §[7]/[9] as
`np.corrcoef(pred_delta, real_delta)[0,1] ** 2` — a bare Pearson
correlation between two already-computed arrays. I read the full
call chain feeding those two arrays (`compute_r_profiles` →
`predicted_c_empty`/`predicted_c_empty_two_wall` → `br.c_empty_with_wall`/
`tw.c_empty_two_wall`, and the real-data arrays read straight from
`experiments/076/results.json::headline`) and confirmed: **nowhere in
that chain does `free_period_with_widening` or `free_period_with_widening
_quiet` appear.** The shape statistic is a raw curve-correlation; the
period-search machinery R11 fixes is never invoked to produce it. This is
algebraically airtight, not merely empirically unmoved.

I then independently confirmed which statistic actually drives each cited
REFUTE, from the raw JSON (`pad_round_trip_results.json`), not from
prose:

| Verdict cited | `period_refute` | `shape_refute` | Driver |
|---|---|---|---|
| `pair_pad` (single-wall) | **True** | **True** | both — shape alone is sufficient |
| `two_wall_pair_pad` | False | **True** | shape alone |
| `two_wall_pair_absorb40` | False | **True** | shape alone |

So the Director's clarifying finding is correct for all three citations,
and for two of the three (`two_wall_pair_pad`, `two_wall_pair_absorb40`)
shape is the *only* thing firing REFUTE — the period leg is not even
close (`period_support`/`period_refute` both False). For `pair_pad`,
period_refute is *also* true, but since shape_refute alone would suffice
to reach REFUTE, this does not weaken the independence claim.

**I also checked the thing the Director's own falsifier left implicit**:
was `pair_pad`'s period leg (computed via the non-quiet
`free_period_with_widening`, the OTHER function this cycle fixes) ever
itself boundary-pinned in the original exp-077 run, such that the R11 bug
could have silently corrupted `rel_period_deviation_pad` too? Read
`test_a_pair_pad`/`test_a_pair_absorb40`/`test_a_two_wall_pair_pad`/
`test_a_two_wall_pair_absorb40` directly: **every real and model `chosen`
record across all four is `at_boundary: false`** (interior optima in the
`wide[1,15]` stage). The bug never fired for any of these four citations
even before this cycle's fix — an independent confirmation, at the level
of exp-077's own specific numbers, of exp-085's own audit finding that
the defect's only historical firings were exp-078/exp-079 (both inert).

**Falsifier discipline was honored, not fudged.** The one place a frozen
prediction (§3 item 2/6) came back numerically outside its own stated
band — `max_r2_over_trials=0.5180` at N=3000, below the predicted
`[0.56,0.78]` — was not silently absorbed. `phase4_null_calibration_
controlled_comparison.py` correctly recognized `max_r2_over_trials` is an
order statistic and built a matched-N/matched-seed control (reconstructing
the pre-fix buggy logic from git history) rather than trusting the naive
before/after diff. Result: bit-identical to 4 decimal places between old
and corrected logic at N=3000, despite the bug firing at a real 6.70%
rate — the boundary-pinned trials never approach the sampling max, which
is set by trials that already found a genuine interior optimum. This is
methodologically correct (isolates the fix's own effect from N-dependent
variance) and is exactly the kind of self-correction this program's R4/G0-e
discipline rewards. I re-verified `p_r2_ge_070=0.0000` stays far below the
falsifier's `0.05` line and `max_r2_over_trials=0.518` stays far below the
falsifier's `0.7156` line at both N=3000 runs — the falsifier genuinely
did not fire, and the real signal's own R²=0.8165/0.7156 remain far above
any corrected noise ceiling measured so far.

**One residual gap, disclosed by the cycle itself, not hidden**: the
full-scale 60,001-call re-run of `null_calibration_appendix` was not
completed (a bounded N=3000 sample was substituted, with the deviation
named in the script's own docstring and in NOTES.md). The controlled
comparison substantially de-risks this — the fix is now shown to have
negligible effect at matched N — but a full-scale run remains the
decisive close-out, correctly carried to the Tier-2 queue rather than
claimed as done.

**Conclusion: the Director's §2 item 2 claim is CONFIRMED**, independently
re-derived from source and from the raw JSON, not merely re-read from the
synthesis document.

## 2. Passivity / reciprocity / causality bookkeeping — my charter's standing duty

**Undisturbed. Confirmed explicitly, not assumed from the proposal's own
framing.** This cycle's committed diff (`git show f256d70`) touches
exactly two functions in each of two files — the post-loop `chosen`-
selection fallback inside `free_period_with_widening`/`_quiet` — adding
only a `converged`/`no_interior_optimum` flag-setting branch. I read the
full diff hunk-by-hunk: it does not touch `reflection_coefficient`,
`n_profile_exact`, `nu_profile`, `damp_e_profile`, `c_empty_with_wall`,
`c_empty_two_wall`, `c_empty_boundary_free`, or any of the three sanity/
passivity gates (`gate_lossless_unimodular`, `gate_single_layer_identity`,
`gate_passivity`) `pad_round_trip_model.py::run_gates` re-runs every
cycle. Those gates were not re-invoked this cycle (no new FDTD, no new
`r(theta)` computation — the existing `r40`/`r80` values are untouched),
but there was nothing for them to re-certify: the physics module producing
reflectance is byte-identical to exp-077's own already-gated version.
`verify_symmetric_damping()` (MATERIALS' realizability check on the
±x-wall admittance symmetry) is likewise untouched. **This is a search-
logic fix on curve-fitting selection, not a physics-model change, exactly
as the proposal and synthesis both state — independently confirmed here
by direct diff inspection rather than accepted from that framing.**

## 3. Other checks performed

- **Scope-mismatch fixes honored.** All six of Red Team's Phase-2
  mandatory fixes are present in the final record: three stride-phase
  Spearman results reported together (not one cherry-picked), the
  quiet-variant audit completed (not merely scoped out), the
  energy-interception exemption sentence present verbatim in both
  `phase3_synthesis.md` and `NOTES.md`, the instrument-reliability caveat
  carried forward at every "NOT STABLY PERIODIC" citation I found, and
  `ss_tot_full`/`ptp` persisted per sub-window in
  `phase4_rescore_results.json` (spot-checked: present, non-zero, growing
  by ~5,444× across the grazing region as PHOTONICS' critique predicted).
- **Reproduction discipline.** `frac_recovered=21/37=0.5676`,
  `classification_a="NOT STABLY PERIODIC"`, and the three Spearman figures
  in `phase4_rescore_results.json` match the frozen predictions in
  `phase3_synthesis.md`/`NOTES.md` to the printed digit — I recomputed
  these by loading the JSON directly, not by re-reading NOTES.md's prose.
- **Checkpoint criterion 2**: correctly N/A — no absorption mechanism, no
  constraint-3 scene, matching every T28 desk cycle since exp-069.
- **Checkpoint criterion 4**: nothing in this record warrants a firing.
  The one place a numeric prediction landed outside its stated band was
  caught and correctly re-diagnosed same-cycle (§1, above) — this
  program's own established non-firing shape, not its firing one.

## Verdict: **PARTIAL**

The repair itself is sound, narrowly scoped, and independently
verifiable at every load-bearing claim I checked from primitives. It does
not advance T28's substantive mechanism question (the ~2.84°-family
periodicity's origin) — it repairs and re-certifies the instrument that
measures it, which is exactly what this cycle set out to do and exactly
what R11 required before any of exp-085's classifications could be
trusted again. The passivity/reciprocity/causality bookkeeping this seat
owns is confirmed untouched, and the one claim I was specifically asked
to re-derive (shape-statistic independence from the R11 bug) holds up
under independent source-level and data-level verification.

## Ranked top candidates for the T28 sub-thread (none re-proposing R1–R11)

1. **Full-scale (60,001-call) `null_calibration_appendix` re-run.** The
   N=3000 controlled comparison found the fix's effect negligible at
   matched N, which substantially de-risks this item but does not
   substitute for it — it is the one piece of this cycle's own mandatory
   scope not completed at full scale, already correctly queued as Tier-2.
   Cheap relative to its evidentiary weight: it is the actual close-out of
   the highest-consequence attack this cycle's own Red Team audit raised
   (a 6.70%-firing defect inside the null underwriting a "settled since
   Iteration 54" REFUTE).
2. **The joint EM/THERMO energy-interception cross-check**, now four
   consecutive cycles deferred/exempt (083–086). Every deferral so far has
   been correctly scene-less-exempt, but the exemption itself is now a
   standing pattern this seat's own charter (energy coupling) should not
   let run indefinitely — the next scene-bearing T28 cycle should treat
   running it as non-negotiable, not merely "should," per this program's
   own R6–R10 escalation precedent for repeatedly-deferred items.
3. **PHOTONICS' grazing-incidence model-validity question**: does
   `edge_diffraction_c_empty_corrected` remain inside its own valid
   near-field/geometric-diffraction regime at the sub-windows where `ptp`
   grows 5,444×–6,631×? This is a precondition for trusting *any* future
   classification built on Method C's grazing-angle sub-windows,
   including a future re-attempt at resolving the near-normal-quarter
   periodicity question this cycle deliberately left open (not foreclosed
   — the instrument-reliability caveat is explicit that "NOT STABLY
   PERIODIC" is a statement about what the instrument can certify, not
   that no structure exists).
