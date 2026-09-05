# exp-112 — Panel Iteration 89

**Lead seat: QUANTUM OPTICS** (rotation: PHOTONICS→MATERIALS→
ELECTROMAGNETISM→THERMODYNAMICS→QUANTUM OPTICS→VISION SCIENCE).
Governance/instrumentation cycle continuing the T28 sub-thread (opened
Iteration 46, exp-069 — an unexplained ~2.8° angular periodicity in a
`C80−C40` padding-delta pattern; `T1` route N/A throughout its own
43-iteration history to date). Executes the Reconciled Iteration-89
queue's headline Tier-1 item (LOGBOOK.md Iteration 88 /
`experiments/111-.../phase5_redteam_audit.md` §8): PHOTONICS' own
independent, non-differencing floor check (a `cpl`-refinement spot check),
deferred twice, executed here for the first time. Tier-0 items (ruling on
the Iteration-85 Checkpoint-4/R24 firing; ratifying the R23 First
Addendum) are Marsh's call, explicitly out of scope, not attempted.

## Phase 1 — Propose (QUANTUM OPTICS)

Full text: `phase1_proposal.md` (as amended below, Phase 2).

## Phase 2 — Critique

Five blind critiques, all **support-with-changes**, zero opposition, each
finding a distinct, independently-verified defect:

- **PHOTONICS**: no bin-neighborhood cross-correlation check exists to
  distinguish a genuine deterministic near-field feature (which should
  imprint correlated structure across adjacent angular bins) from an
  isolated noise spike, despite the check being zero-marginal-FDTD-cost.
- **MATERIALS**: the `ABSORB`/`EDGE` domain-edge sponge scaling is
  claimed part of "the same congruent-refinement convention" as
  `tau_shell`/`sigma_max`, but is **not** resolution-invariant (no
  Courant-factor normalization on the per-timestep multiplicative mask)
  — computed accumulated log-attenuation `13.93`→`17.24` (discrete
  cell-sum route).
- **ELECTROMAGNETISM**: independently found the identical non-invariance
  via a different route (closed-form continuum integral, `-13.26`→
  `-16.57`) — both converge on the same `~1.25×` real, disclosed-nowhere
  change.
- **THERMODYNAMICS**: the Phase-4 pipeline **as shipped cannot run** —
  `chunk_runner.py`/`analyze.py` both `import run as R110` then `import
  run as R`, and Python's module cache silently aliases both names to
  the same object; confirmed by actually executing
  `python3 chunk_runner.py 156 25 empty`, which crashed with
  `AttributeError` before any `Sim.run()` call.
- **VISION**: "detection floor," used in the mechanism narrative to
  frame this as QUANTUM's own charter question, is never disambiguated
  from a human perceptual/observer-detection threshold (constraint-3's
  own vocabulary) and does not appear in the code-enforced `DISCLAIMER`
  string R23's own asserts check — the same failure shape as the
  historical R9/T16 unit-conflation.

**Red Team's Phase-2 audit** (`phase2_redteam_audit.md`) independently
re-derived/re-executed every one of the above from primitives (confirming
all five bit-exact or by direct re-execution), combined them into a
6-item mandatory-fix docket, disclosed one upgrade (PHOTONICS' own
conditional fix elevated to mandatory), zero opposition overrides.
**Verdict: PROCEED-WITH-MANDATORY-FIXES.** Recommended a new standing
rule, R29 (same-basename module import-cache collision). Ruled: zero
Checkpoint criteria fire, contingent on the docket landing before Phase 4
executes for real.

## Phase 3 — Synthesis (Director)

**All six mandatory-fix-docket items accepted in full, applied this
shift, before any Phase-4 `Sim.run()` call — no criticism overridden.**

1. **Fix 1 (module collision, hard blocker)**: renamed this cycle's own
   `run.py` → `run112.py`; `chunk_runner.py`/`analyze.py` now `import
   run112 as R`, with executed identity assertions (`assert R is not
   R110`, `assert hasattr(R, "geom_fixedabs_cpl")`) added to both.
   Re-verified by actual re-execution, not by re-reading the diff:
   `run112.py --verify-geometry` → `pass_=True` both r; `analyze.py` now
   runs cleanly through to its correct pre-data early-exit
   (`r=156/cpl=25 captures not yet complete...`, exit 0) instead of
   crashing.
2. **Fix 2 (ABSORB/EDGE disclosure)**: `phase1_proposal.md` §5/§2.1
   corrected in place — the sponge's non-invariance is now a computed,
   disclosed number (`13.93→17.24`, `~1.25×`, both ~6–8 orders below the
   measurement floor, non-fatal) instead of a vague "not independently
   re-derived" idealization. Folded into `run112.py`'s own `DISCLAIMER`
   string (single source of truth, R23 discipline).
3. **Fix 3 (neighbor-correlation Check C)**: `run112.py::
   neighbor_correlation_check()` added — Pearson-correlates the ±2-bin
   window of the delta pattern around the named bin, cpl=20 vs cpl=25,
   `corr≥0.5` bar. `classify_resolution_check`'s own Check-A branch now
   gates the "candidate real structure" language on Check C clearing its
   bar; a SURVIVES-but-Check-C-fails reading is reported as "not yet
   ruled out," never upgraded.
4. **Fix 4 (DISCLAIMER clause)**: one sentence appended to `DISCLAIMER`
   itself defining "detection floor" as the instrument's own
   grid-discretization SNR threshold, not a human/observer-detection
   threshold — covered by both existing R23 asserts for free.
5. **Fix 5 (re-verify asserts fire on real execution, not merely present
   in source)**: per Red Team's own Attack 5, VISION's "closes... the
   asymmetry" language is **not** carried forward as settled here — both
   `assert DISCLAIMER in ...` calls (predictions-side, confirmed above;
   result-side) will be re-verified by actual execution once Phase 4
   produces real captures and `analyze.py` reaches its own result-text
   assert, reported in the Result section below, not assumed now.
6. **Fix 6 (recommended, non-blocking)**: `analyze.py` now persists
   `sigma_abs`/`sigma_ext` (both captures) into `results.json`'s own
   `energy_ledger` field, plus the full 48-bin `pattern_peccored`/
   `pattern_hollow`/`pattern_delta` arrays (needed by Check C and by any
   future physical interpretation).

**R29 ratified** (LOGBOOK.md RULED OUT registry, this shift) — the
same-basename-module import-collision failure shape Red Team's audit
named. Founding instance; does not fire; forward-firing on a second
instance, matching this registry's own standing precedent.

**T1 escape route: N/A**, confirmed structurally (Red Team's own Phase-2
audit §0) — no `σ(I)`/`σ(x,t)`/angular-selectivity/sub-threshold content
anywhere in this cycle; no constraint-1/2/3/4 verdict is scored or moved.

## Setup

Congruent `cpl=20→25` (ratio 1.25×) grid-resolution refinement of the
`fixedabs` family's own r=156 geometry (empty / hollow-article /
PEC-cored-article), holding `tau_shell` (shell optical thickness) and
total simulated optical periods exactly invariant by construction
(verified: `320·S` at both `cpl`, `S=courant_frac/√2`). Full parameter
table in `phase1_proposal.md` §2.1 (unchanged by Phase 2's fixes — only
the ABSORB/EDGE *disclosure*, not the geometry itself, changed). Target:
bin index 4 (`−146.25°`, `r=156`, `margin=32`/`box_a`) — currently
`UNRESOLVED-BY-CONSTRUCTION` at `cpl=20` (`local_snr≈0.10`, ~10× below
even the K=1 floor) yet reads a `9.88%` local fractional deviation
between the hollow and PEC-cored angular-scattering patterns. Three real
FDTD calls this cycle (empty/hollow/peccored, r=156 only); the
`+168.75°` bin at r=312 is explicitly deferred (§3 of the proposal —
the existing R27/R28 cost gate, invoked for real via
`R.cost_gate_check`, would refuse an r=312 expansion at `cpl=25`:
`14906.3s` projected vs. `10800s` bound).

## Predictions (committed to git BEFORE any Phase-4 code is executed for
## real, house discipline, non-negotiable — verbatim quote of
## `run112.py::build_predictions_text()`'s own output, post-fix)

```
PREDICTIONS (pre-registered, exp-112, Panel Iteration 89)

This is an instrument-fidelity/resolution-convergence check on an angular-scattering-pattern noise floor, not a phenomenon-mechanism proposal -- no sigma(I)/sigma(x,t)/angular-selectivity/sub-threshold content, no Weber-contrast or C_thr(L) perceptual scoring, is performed anywhere in this document. 'Coherent sub-wavelength structure', as used here, means spatially deterministic classical field structure, not quantum coherence -- no non-classical or state-dependent mechanism is proposed, varied, or required. The congruent cpl-resolution-refinement construction (geom_fixedabs_cpl) is verified byte-exact to the cpl=20 baseline geometry at cpl==20 (verify_geometry_identity), but this is the FIRST application of that construction to the fixedabs family -- a single new resolution point (cpl=25) relative to the cpl=20 baseline can rule out a sign-flip/order-of-magnitude collapse but CANNOT establish full continuum convergence (R15's own two-point caution): a third, differently-scaled resolution point would be needed for that stronger claim, not proposed this cycle. This leg tests r=156 alone -- the +168.75deg bin at r=312 remains untested, deferred pending this cycle's own gate (Sec 2.0) and Phase-4 outcome. 'Detection floor', throughout this document, means the K=3/K=1 mirror-pooled-floor instrument's own grid-discretization SNR threshold -- NOT a human perceptual or observer-detection threshold; no constraint-2/3 claim is made or implied by this term (Phase-2 Red Team audit Docket Fix 4, VISION's own finding). The domain-edge sponge (ABSORB/EDGE) scaling is NOT resolution-invariant the way tau_shell/sigma_max is -- its one-way accumulated log-attenuation genuinely rises from 13.93 (cpl=20, absorb=40) to 17.24 (cpl=25, absorb=50), a real ~1.25x change -- but both values sit 6-8 orders of magnitude below the ~1e-4-1e-3 measurement-floor scale this cycle actually measures at, so it cannot manufacture the near-field signal under test (Phase-2 Red Team audit Docket Fix 2, MATERIALS'/ELECTROMAGNETISM's own independently convergent finding). A Check-A SURVIVES reading may be described as 'candidate real structure' only if Check C (neighbor_correlation_check, below) also clears its own corr>=0.5 bar -- otherwise it is reported as 'not yet ruled out', never upgraded on Check A alone (Phase-2 Red Team audit Docket Fix 3, PHOTONICS' own finding).

**Geometry identity (zero-FDTD, pre-Phase-4)**: verify_geometry_identity()
returns pass_=True at both r=156 and r=312 (geom_fixedabs_cpl(r, cpl=20)
byte-exact to R.geom_fixedabs(r)). Falsified by any mismatch -- HALT
before any Sim.run() call.

**Reproduction/self-consistency precondition**: sum(sigma_scat_per_bin) ==
sigma_scat (from sections.widths(), same box -- angular_scattered_pattern's
own docstring identity) to <1e-9 relative, at margin=32, both peccored and
hollow captures, r=156, cpl=25. Falsified by any larger deviation -- HALT
before the named-bin comparison is trusted.

**Named bin (-146.25deg, r=156, margin=32, bin index 4) --
the genuinely uncertain question this leg exists to answer**:
Check A (mirror-pooled-floor instrument, reused unmodified, at cpl=25):
SURVIVES if local_snr_peccored AND local_snr_hollow both clear 1.0
(the K=1 bar cleanly separating exp-110's own RESOLVED/UNRESOLVED
populations); COLLAPSES if neither local_snr improves over its cpl=20
value (0.0965/0.1061); else
AMBIGUOUS. Check B (this program's own founding T28 R3 standard):
SURVIVES if delta[idx] keeps the same sign as cpl=20
(-1.073928e-05) and stays within one order of magnitude of it;
COLLAPSES on a sign flip or a >=10x drop; else AMBIGUOUS. Check C
(+/-2-bin neighborhood correlation, cpl=20 vs cpl=25,
Docket Fix 3): a Check-A SURVIVES reading may be described as "candidate
real structure" only if corr>=0.5; otherwise it is reported as "not
yet ruled out" regardless of Check A's own reading. No advance position
taken on which outcome any of the three checks will report.
```

## Result

*(To be filled after Phase 4 — verbatim quote of
`run112.py::build_result_text()`'s own output, fed the real captured
control outputs, persisted in `results.json`.)*

## Combined Verdict

*(Pending Phase 4 + Phase 5.)*

## Idealizations — what this cycle does and does not establish

See `phase1_proposal.md` §5 (as amended by Phase 2's Docket Fixes 2–4,
above) for the full, corrected list. Summary: does establish a real,
executed, congruent `cpl=20→25` refinement with three independent,
complementary, pre-registered checks; does NOT establish full continuum
convergence (a single new resolution point, R15 discipline); does NOT
test the `+168.75°` bin at r=312 this cycle (cost-gate-deferred).
