# PHASE 3 — SYNTHESIS · Director · Panel Iteration 57 · exp-080

**Role: Director** (synthesizes, does not vote). Read the complete Phase 1
record (`phase1_proposal.md`, `validity_precheck.py`, `validity_precheck_results.json`),
all five blind Phase-2 critiques, and Red Team's Phase-2 audit
(`phase2_redteam_audit.md`) in full before writing this.

## 1. Disposition of Red Team's Phase-2 audit

Red Team's ruling: **PROCEED-WITH-MANDATORY-FIXES**, a 5-item prioritized fix
docket, zero overrides of any of the five blind critiques (every one ADOPTED
IN FULL). Red Team independently re-derived, from primitives, in its own
from-scratch scratch script, all eight load-bearing numeric claims across the
five critiques — every one reproduced exactly, several to 4+ decimal places.

**The Director adopts Red Team's audit in full — all 5 fix-docket items,
zero overrides.** Given that Red Team itself already independently
re-verified every claim from primitives (not merely re-stated the blind
critiques' own numbers), there is no remaining verification gap for the
Director to re-litigate; the synthesis task here is to fold the fix docket
into the permanent record and the committed code, and to correct
`phase1_proposal.md`'s own pre-QUANTUM Combined-reading language — exactly
Attack 1's own named risk, addressed here rather than left to recur.

## 2. Fixes applied (all 5, in `validity_precheck.py`)

1. **[HIGH, Attack 1]** `phase1_proposal.md`'s Combined reading is
   **superseded by this document**, not silently left standing. PHOTONICS'
   own §4 image term is no longer "not yet built" — QUANTUM's blind Phase-2
   critique built it (zero new FDTD, fully gated primitives) and Red Team
   independently reproduced the construction and every score to 4 decimal
   places. Folded into `validity_precheck.py` as
   `photonics_image_term_curve()` / `part_d_photonics_construction()` — the
   canonical, committed, reusable implementation going forward, not a
   critique-file-only artifact.
2. **[HIGH, Attack 2]** MATERIALS' realizable-admittance rerun of part (b)
   folded in as `reflection_coefficient_vec_realizable()` /
   `part_b_realizable()`. Part (b)'s verdict is now reported as
   **admittance-family-dependent**, not as a single INCONCLUSIVE number: mean
   `R²=0.7345` (matched, unobtainium) vs. mean `R²=0.4305`, **REFUTE**, with
   C40/G40 negative (realizable, `μ_r=1`) — worst exactly at `ABSORB=40`,
   the depth exp-079's own MATERIALS review already found the two families
   diverge most (`89.08°` `arg(r)` deviation).
3. **[MEDIUM, Attack 2/§3 item 3]** THERMODYNAMICS' `|r(90°−θ_beam)|²`
   power-budget table folded in as `part_c_power_budget_at_true_angle()` —
   explicitly labeled as answering a different question, at a different
   angle, from part (b)'s own `theta_eff`-based `|r|²` values (5+ orders of
   magnitude smaller) — a reader can no longer conflate the two.
4. **[MEDIUM, Attack 4]** PHOTONICS' calibration-corrected `R²(abs)` folded
   in as `part_b_abs_calibration_corrected()`: the raw `theta_eff`-based
   `R²(abs)=-7.82/-8.45` (C70/C80) is now reported alongside the
   shape-only-optimal `-1.65/-2.30`, separating the avoidable calibration
   component from the real, still-unexplained, ABSORB-depth-concentrated
   (worst at 70/80, clean at 40/60/G40) optical-response question. **This
   question is NOT resolved here** — it is disclosed as open, exactly as
   Red Team's own ruling requires (Attack 4 is informational-track, not a
   defect requiring resolution this cycle).
5. **[LOW, §3 item 5]** The `E_direct(theta_beam)` omission in
   `photonics_image_term_curve()` is stated explicitly in that function's own
   docstring as an inherited-not-independently-verified assumption — flagged
   forward for Iteration 58, not resolved here (resolving it would require
   new machinery this cycle's own zero-FDTD, desk-only scope does not cover).

**No FROZEN-PREDICTIONS git-freeze cycle was needed for this fold-in.**
Every number folded into `validity_precheck.py` above was already
independently computed AND independently re-verified from primitives, twice
over (once by the relevant blind critique, once by Red Team's own
from-scratch script) — a confirmatory re-implementation into committed code,
not a fresh, previously-unknown prediction (same reasoning exp-079
Iteration 56 Phase 3 gave for its own no-freeze fold-in of QUANTUM's
ablation control). Re-running `validity_precheck.py` after this edit
reproduced every one of Red Team's own independently-verified numbers
exactly (see `phase4_results.md`).

## 3. Combined reading, corrected

**(a) FORECLOSE** — confirmed a third independent way (EM's script, exp-079's
own Red Team audit, this cycle's own Red Team re-derivation from raw
geometry). Stands unqualified.

**(b) admittance-family-dependent**, not simply INCONCLUSIVE: INCONCLUSIVE
under the matched (unobtainium) family, **REFUTE** under the realizable
family. The matched-family number alone, as `phase1_proposal.md`'s own
PHASE 1 RESULTS reported it, was materially incomplete — corrected here.

**(c) PHOTONICS' own §4 image-term construction has effectively already
been built and scored, zero new FDTD, by QUANTUM's blind Phase-2 critique,
independently reproduced exactly by Red Team.** It does not clear a bar
comparable to, and by the shape-only (scale-corrected) floor measure is
**worse than**, this cycle's own already-INCONCLUSIVE part (b) result: raw
comparison is a catastrophic amplitude-regime mismatch (`R²` `-10⁴` to
`-10⁷`, a direct numerical consequence of part (a)'s FORECLOSE — the
aperture never actually presents `90°-θ_beam` to the wall); the most
generous possible shape-only rescue still lands at mean `R²(Re)=0.602`,
floor `0.085` at C70 (vs. this cycle's own floor `0.5214`), and repeats the
identical negative-`R²(abs)` pathology at the identical two configs (C70,
C80).

**None of this closes the plane-wave/global-steering construction as a T28
mechanism candidate** — Checkpoint criterion 2 remains NOT YET RIPE (Red
Team §4): the comparison above is against exp-079's own per-point model,
itself already known (via that cycle's reflectance-ablation control) to be
structurally incapable of discriminating a real echo from none. The
actually-decisive test — scoring `photonics_image_term_curve()`'s own
`PAIR_PAD`/`PAIR_ABSORB40`/`C80-C40` deltas against the REAL T28 reference
periods via the same `_free_period_search`/staged-widening pipeline every
prior y-wall model in this sub-thread has used — has never been run. That is
Iteration 58's own next step, not a repeat of the build.

## 4. Checkpoint ruling (adopted from Red Team's audit, independently
## reasoned through again by the Director, same conclusions)

- **Criterion 1**: N/A (zero constraint engagement).
- **Criterion 2**: NOT YET RIPE — strong negative desk-level evidence
  against the plane-wave/global-steering construction's per-point-shape
  fidelity, but not yet tested against the real T28 reference periods, the
  actually-decisive metric.
- **Criterion 3**: N/A (zero new FDTD, confirmed by direct audit of every
  file this cycle produced).
- **Criterion 4**: does NOT fire. Every number this cycle produced or
  inherited was independently re-verified at least once (Red Team's audit)
  and in several cases twice (Red Team + the Director's own re-run above);
  the one live risk Attack 1 named (stale pre-QUANTUM framing surviving into
  Phase 3 unreconciled) is closed by this document.
- **Criterion 5**: not at risk — this cycle substantively narrows the last
  untested member of the coherent-echo mechanism class, a cumulative result
  building on exp-079's own foreclosure of the full-aperture-sum family.

## 5. Gates

Zero `lab/` changes this entire cycle (confirmed: `git diff --stat -- lab/`
against the pre-cycle commit is empty). The house trust suite
(`lab/validation/run_all.py --only 12346789`) was confirmed green (41/41) at
shift start, before any panel work began, and no engine code was touched
since — no re-run required by house discipline for a zero-`lab/`-diff cycle
(same standard exp-079 Iteration 56 and every other zero-FDTD T28 cycle this
sub-thread has used).

## 6. Recommendation for Iteration 58's queue

Adopted verbatim from Red Team's own §6 (independently re-reasoned by the
Director, same conclusion): change the queue item from "build PHOTONICS' §4
construction" to "gate and extend what QUANTUM already built" —

1. Check the `E_direct` cancellation assumption explicitly (fix docket item
   5) before treating `photonics_image_term_curve()` as final.
2. Score its `PAIR_PAD`/`PAIR_ABSORB40`/`C80-C40` deltas against the real
   T28 reference periods via `_free_period_search`/staged-widening — the one
   test that actually bears on Checkpoint criterion 2.
3. Pair with the real 750/450nm wavelength-generality leg (deferred 4+
   consecutive T28 cycles) — informative independently of the shape-only
   finding above, since `λ` enters both `d_F` and the reflectance phase.
4. Weigh promoting the PAD-loaded real-article check (deferred FOUR
   consecutive cycles, exp-076 through exp-079) more seriously — if deferred
   a fifth time, the reason must be stated explicitly against this cycle's
   own finding, not by inertia.

Full record: `experiments/080-t28-y-wall-planewave-validity-precheck/` —
`phase1_proposal.md`, `validity_precheck.py`, `validity_precheck_results.json`,
five Phase-2 critiques, `phase2_redteam_audit.md`, this document.
