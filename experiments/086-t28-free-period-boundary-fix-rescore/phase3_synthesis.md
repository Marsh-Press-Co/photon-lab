# PHASE 3 — SYNTHESIS · Panel Iteration 63 · exp-086 · Director

*Director-run (the panel-shift agent driving this cycle). Received:
`phase1_proposal.md`, all five blind Phase-2 critiques, and Red Team's
Phase-2 audit (`phase2_redteam_audit.md`) in full. Per PANEL.md's Phase-3
mandate: resolves the debate into ONE testable configuration, records
accepted/overridden criticisms, and freezes predictions before any run.*

## 1. Corrected title / scope statement

Red Team's attack 6 stands: exp-085's own §7 ranking has no Tier structure.
This cycle executes **items 1–3 of that flat six-item list** (fix +
re-score; extend the null/correct significance; the bounded prior-citation
audit) plus the two cosmetic fixes (items 4–5 there) folded into the same
batch, per the original proposal's own scope. Items 4 (energy-interception,
explicitly deferred to a scene-bearing cycle) and 5 (leg-(b) Anchor 2 /
kernel rebuild) are **out of scope**, exempted explicitly per fix 3 below.
Renaming the experiment folder is unnecessary (its slug already describes
the actual scope correctly); only the proposal's own title line and any
future NOTES.md/LOGBOOK citation need the correction.

## 2. Disposition of all six mandatory fixes — ALL ACCEPTED, zero overrides

1. **Stride-phase pre-registration (QUANTUM, confirmed by Red Team).**
   ACCEPTED IN FULL. All three non-overlapping stride phases
   (θc starting 5°/7°/9°) will be computed and reported together, with the
   headline significance read as "phase-dependent, not robust" rather than
   any single cherry-picked number. Frozen prediction below reproduces Red
   Team's own already-twice-independently-confirmed figures exactly — this
   is now the THIRD independent computation, using the from-scratch
   corrected-machinery pipeline rather than a standalone re-implementation.

2. **Quiet-variant audit, scoped and completed (MATERIALS, extended by Red
   Team).** ACCEPTED IN FULL, extended further by the Director:
   `free_period_with_widening_quiet` gets the SAME R11 fix applied (not
   merely audited unfixed) — the identical bug shape, left unrepaired in a
   function still actively used by every future T28 null-calibration call,
   would be inconsistent with R11's own text ("binding on any future reuse
   of the affected machinery"). Phase 4 re-runs
   `null_calibration_appendix` in FULL (all 60,001 calls, the corrected
   count per Red Team's attack 7 — not the original's "20,000", not
   MATERIALS' "40,000") on the corrected quiet function, against exp-077's
   own committed `real_delta_pad`/`real_delta_absorb40` data, and diffs
   every cited statistic against exp-077's own `pad_round_trip_results.json`
   values.

   **Director's own clarifying finding, independently derived while scoping
   this fix (not raised by any seat or Red Team)**: re-reading
   `pad_round_trip_results.json` directly, the `combined_verdict=REFUTE`
   citations (`pair_pad`, `two_wall_pair_pad`, `two_wall_pair_absorb40`) are
   driven by `shape_r_squared_*` — a Pearson shape-correlation between the
   MODEL's predicted curve and the REAL curve — a statistic computed
   entirely independently of `free_period_with_widening_quiet` and
   untouched by this bug. `null_calibration_appendix`'s own role is
   narrower than Red Team's attack 1 framed it: it establishes that the
   REAL data's own free-fit R² (0.8165 for `pair_pad`, 0.7156 for
   `pair_absorb40`, both from **interior, non-boundary-pinned** optima —
   confirmed directly from `pad_round_trip_results.json::test_a_pair_*
   .real.chosen`, `at_boundary` not present in that record but the p_star
   values, 4.611°/4.176°, sit well inside `[1,15]°`, nowhere near either
   stage's own boundary) stands out from a pure-noise floor
   (`max_r2_over_trials=0.5609`, `p_r2_ge_070=0.0` as currently cited) — a
   significance-of-the-real-signal check, not the REFUTE verdict's own
   evidentiary basis. **This does not excuse skipping the audit** (Red
   Team's fix 2 stands, in full, below) — a materially higher corrected
   null ceiling would still be a real, reportable finding about how
   confidently this program can call the real oscillation "not noise" — but
   it recalibrates the stakes: even a large upward correction to
   `max_r2_over_trials` cannot, on its own, flip any currently-cited
   REFUTE verdict, because REFUTE never reads that statistic. Falsifier for
   THIS clarification: if re-reading finds `shape_r_squared_*` is computed
   FROM a `free_period_with_widening`-family fit anywhere in its own call
   chain (not evident from the source read so far), this paragraph is
   wrong and must be retracted.

   **Frozen numeric prediction**: `p_r2_ge_070` corrected ≤ 0.02 (a small
   absolute rise from the currently-cited 0.0, bounded by the ~6.7%
   boundary-pinned subset Red Team sampled, most of which will land well
   under the 0.70 threshold even under the widened [1,15]° stage);
   `max_r2_over_trials` corrected stays inside `[0.56, 0.78]` — i.e. rises
   from the currently-cited 0.5609 but remains below both real R² values
   (0.8165, 0.7156). **Falsifier, explicitly, and Checkpoint-relevant**: if
   `p_r2_ge_070` corrected exceeds 0.05, OR `max_r2_over_trials` corrected
   meets or exceeds 0.7156 (the lower of the two real R² values), that is a
   materially different result from what this cycle predicts and must be
   flagged for Checkpoint-criterion-4 consideration at Phase 5, not quietly
   absorbed into the docket. Bootstrap-recovery stats (`recovered_mean/std
   _p_star_deg`, both variants) are predicted to change by
   <0.01° absolute — the bootstrap fits `yhat + boot_resid`, a signal
   dominated by the real, already-interior-optimum `yhat`, essentially
   never boundary-pins.

3. **Energy-interception exemption sentence (THERMODYNAMICS, confirmed).**
   ACCEPTED IN FULL. Stated here and copied verbatim into NOTES.md: *this
   cycle is a zero-FDTD instrument-repair/re-score desk cycle; no
   article-loaded FDTD scene exists anywhere in its scope, so the joint
   EM/THERMO energy-interception cross-check is structurally exempt this
   cycle, matching exp-084/085's own established language — not a fourth
   consecutive silent deferral.*

4. **Instrument-reliability caveat carried forward (VISION, confirmed).**
   ACCEPTED IN FULL. Every place this cycle's own corrected `classification
   _a` label is reported (this document, NOTES.md, the eventual LOGBOOK
   entry) must carry, verbatim or materially equivalent: *"NOT STABLY
   PERIODIC" is a statement about what this (now doubly-corrected)
   instrument can currently certify, not a claim that no near-normal-
   quarter periodicity exists — that question remains open.*

5. **Persist `ss_tot_full`/`ptp` per sub-window + grazing-incidence
   model-validity caveat (PHOTONICS, confirmed).** ACCEPTED IN FULL.
   `phase4_rescore.py`'s output JSON persists both fields for all 37
   sub-windows. NOTES.md's Idealizations section states explicitly: the
   ~5,444×–6,631× ptp growth across the grazing-incidence sub-windows
   raises an open question about whether `edge_diffraction_c_empty_
   corrected` remains inside its own valid near-field regime there — not
   resolved by this cycle, not silently omitted.

6. **Title correction (Red Team, new).** ACCEPTED — see §1 above.

**No criticism overridden.** Every one of the five blind critiques and
every one of Red Team's own additions survives Director review intact;
this synthesis adds one clarifying (not overriding) finding under fix 2.

## 3. Frozen predictions — Method C re-score (unchanged from Phase 1,
independently reproduced three times over — Phase 1's own arithmetic, Red
Team's from-scratch reimplementation, and now this synthesis's own
confirmation reading `phase2_redteam_audit.md` §1 directly)

- Boundary set under corrected machinery: **exactly 6/37** sub-windows
  (`θc∈{45,59,61,63,71,73}`), each newly flagged `converged=False,
  no_interior_optimum=True`.
- `frac_recovered` (recovered = `converged==True ∧ p_local_corrected≤6.0°
  ∧ r2_local≥0.30`): **21/37 = 0.5676** exactly.
- `classification_a` = **NOT STABLY PERIODIC** (the code's first-checked,
  unconditional `frac_recovered<0.80` gate branch — 0.568 fails it before
  any other criterion is evaluated).
- Spearman, three pre-registered stride phases, recovered-only subsample:
  θc-start=5°: **ρ=0.8571, p=0.0238** (exact permutation, n=7); θc-start=7°:
  **ρ=0.4286, p≈0.35**; θc-start=9°: **ρ=0.5357, p≈0.24**. Reported
  headline: significance is phase-dependent — one of three pre-registered
  alignments clears p<0.05, two do not — NOT a single confirmed/refuted
  verdict.
- Prior-citation audit (item 3, unchanged from Phase 1): predict no
  additional currently-cited T28 headline number is found corrupted beyond
  the two already-known-inert instances (exp-078, exp-079).

## 4. Idealizations (stated explicitly, carried into NOTES.md)

Single λ=600nm only. Zero new FDTD — every number here is a closed-form/
desk recomputation of already-validated machinery
(`edge_diffraction_c_empty_corrected`, verified bit-identical via
`FastEval` in exp-085, reused unchanged). The R11 fix changes ONLY how a
non-convergent search's result is selected and flagged — the underlying
`_free_period_search`/`_fixed_period_fit` grid-search and least-squares
machinery is untouched, byte-for-byte. The grazing-incidence amplitude
blow-up (fix 5) is disclosed, not resolved, this cycle. The quiet-variant
fix and full null-calibration re-run (fix 2) is confined to reading
already-committed exp-077 data (`real_delta_pad`/`real_delta_absorb40`,
`thetas`) — no new geometry, no new source data.

## 5. Checkpoint check (pre-run)

Checkpoint criterion 2 (mechanism-class boundary): **N/A** — instrument-
repair, not a phenomenon-mechanism claim, matching every T28 desk cycle
since exp-069. Criterion 4 (program-integrity drift): not fired by
anything in this synthesis; the one condition that WOULD warrant Phase-5
Checkpoint consideration is stated explicitly as a falsifier in §2 item 2
above, pre-registered before the run, not invented after seeing the
number.

**Predictions committed to git now, strictly before `phase4_rescore.py` is
written or run — house discipline, non-negotiable.**
