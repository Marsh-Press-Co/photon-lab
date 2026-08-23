# exp-064 — Phase 3 Synthesis (Director)

Panel Iteration 41. Lead: QUANTUM OPTICS, by rotation. Executes Iteration
40's binding forward commitment (Red Team's Phase-5 final audit): resolve
live thread T23's witness-scale length-legitimacy question this cycle, via
a real geometric length or an enforced `length_provenance` code-level
guard — a fourth deferral would itself be a program-integrity finding at
Iteration 42.

Phase 2 produced five blind critiques (all support-with-changes) and a
Red Team audit (PROCEED-WITH-MANDATORY-FIXES, no Checkpoint criterion
fires, one forward tripwire set — see `phase2_redteam_audit.md`). This
document resolves the debate into one testable configuration, states
which criticisms are accepted/overridden, and records the docket applied.

---

## 1. Criticisms accepted / overridden

**All four blocking mandatory-fix items from Red Team's docket are
ACCEPTED IN FULL, without override.** No Phase-2 criticism is overridden
this cycle — every attack Red Team ruled load-bearing was independently
re-verified by Red Team against primary artifacts before this synthesis
began, and each is fixed below with a concrete, verified mechanism, not
merely acknowledged in prose (the exact failure shape this cycle exists to
end).

1. **EM's catch (Red Team attack 1, mandatory-fix 1) — ACCEPTED.** The
   stage-24 gate suite as originally specified (Phase 1 §4) would not have
   enforced QP-3 against the real committed call sites. Fixed: stage 24
   gate 4 now text-scans `run_all.py`'s own committed source (`open(
   __file__)`, not a fresh in-memory call) for every
   `front_surface_conduction_correction`/`mixed_length_scale_regime` call
   site in the file, and FAILs unless every `L_MP5_730X_M`-class call
   carries `length_provenance="extinction_derived_diagnostic_only"` and
   `diagnostic_only=True` literally, and every `L_BENCH_M`/`R_OUT_M`-class
   call carries `length_provenance="bench_construction"`. **Verified live,
   not merely argued**: the gate was deliberately broken (one witness-scale
   call site relabeled `bench_construction` by hand) and re-run — it FAILed
   correctly (27/28, one FAIL, the exact injected defect) — then reverted
   and re-run clean (28/28). This is the single most important fix in this
   docket; see `phase4_results.md` for the full transcript.

2. **MATERIALS' contradiction catch + PHOTONICS' idealization gap (Red
   Team attacks 2/3, mandatory-fix 2) — ACCEPTED, §6 STRUCK.** Phase 1's
   §6 claimed a "genuinely new" 24×–75× realizability gap against an
   uncited "~14µm" figure. Red Team independently confirmed this
   contradicts this program's own already-established, sourced record
   (exp-061 MP-2 CONFIRMED: 100–500µm real CNT-forest/Vantablack
   thicknesses; MP-5's own table already computes the exact 332–1056µm
   witness-need figures §6 re-derived; correct existing gap ≈1×–10.5×, not
   24×–75×) — and PHOTONICS separately found even a corrected version would
   silently equate forest height with single-pass absorption path length,
   with no oblique-incidence or scattering-transport disclosure. Per Red
   Team's own option (b): **§6 is struck from this cycle's scored record
   entirely**, not restated at a corrected number (avoiding compounding one
   fix with another under-qualified claim). The underlying thickness/pitch/
   diameter question remains exactly where it already lived before this
   cycle touched it — PLAN.md's standing queue item 3 (pin record-blackness
   CNT-forest pitch/diameter AND thermal conductivity together) — undisturbed,
   not duplicated. `phase1_proposal.md` itself is left as originally
   written (this program's historical-record convention for a Phase-1 draft
   error corrected at Phase 3, per the T23/Iteration-22 precedent — the
   original mixed-length-scale sign-flip bug was likewise left in the
   Phase-1 file and corrected downstream, not silently edited away).

3. **VISION's catch (Red Team attack 4, mandatory-fix 3) — ACCEPTED.**
   Stage 24 gate 3 now asserts, for a licensed call to each of
   `mixed_length_scale_regime` and `front_surface_conduction_correction`,
   that the pre-existing `netd_disclaimer` string reads byte-identical to
   its pre-guard committed text (hardcoded literals, since these strings
   are static and not supposed to change). Verified live: both checks PASS
   against the actual post-guard dict.

4. **THERMODYNAMICS' catch (Red Team attack 6, mandatory-fix 4) —
   ACCEPTED, option (a).** Every guarded function's return dict now carries
   a `geometric_realizability` key, populated by
   `_geometric_realizability_note`: `"UNGROUNDED..."` when
   `diagnostic_only=True` (explicitly stating a green PASS answers
   provenance-honesty, never buildability), `"N/A -- ...licensed..."`
   otherwise. Option (a) — an additive field — was chosen over option (b)
   (dropping the witness-scale calls from the gated regression path
   entirely) because it preserves stage 23's own existing, already-
   committed regression anchors (the 1.013006/1.015703/0.089731 figures)
   without disturbing them, while still closing the ambiguity Red Team
   named; dropping the calls would have meant re-deriving or discarding
   real, working gate coverage for no additional protection this field
   doesn't already provide.

**Non-blocking items (Red Team attacks 5, 7, 8) — deferred as future
scope, per Red Team's own ranking**, correctly named by the Phase-1
proposal's own Idealizations 2/4 (provenance-ROLE vs. provenance-TIER;
material-identity coherence across `measured_geometric` sources) or
cosmetic (explicit `candidate_globs` — stated explicitly in the registry
entry built this cycle regardless, see §4 below).

---

## 2. Checkpoint question — Director's disposition

Red Team's Phase-2 audit ruled explicitly, criterion by criterion, that
none of the five Checkpoint criteria fire at Phase 2 (a proposal being
critiqued, before Phase-3 freeze, is the designed mechanism, not drift).
The Director accepts this ruling without override. **One live forward
tripwire is carried into this cycle's own Phase 3/4/5, binding**: if
Phase 3 (this document) shipped stage 24 without a real code-level check
on `run_all.py`'s actual committed source, and a future cycle later found
a mistagged witness-scale call site underneath a green suite, that would
fire criterion 4 automatically. **This tripwire is discharged, not merely
addressed**, by mandatory-fix 1 above (gate 4, independently verified live
via the deliberate-break test) — the condition it was conditioned on
(shipping without real enforcement) did not occur.

---

## 3. Mandatory-fix docket — applied

All four blocking items (§1 above) are implemented in code, on this
branch, verified live:

- `lab/thermo_sidecar.py`: `LICENSED_LENGTH_PROVENANCE`,
  `DIAGNOSTIC_ONLY_PROVENANCE`, `_validate_length_provenance`,
  `_geometric_realizability_note` (new); `gas_conduction_h_eff`,
  `lumped_cube_mass_kg`, `mixed_length_scale_regime`,
  `front_surface_conduction_correction` all gain a required, keyword-only,
  no-default `length_provenance` parameter plus `diagnostic_only=False`;
  `mixed_length_scale_regime`/`front_surface_conduction_correction`'s
  return dicts gain `length_provenance`, `diagnostic_only`,
  `geometric_realizability` keys. `biot_number` correctly left unguarded
  (takes no length argument).
- `lab/validation/run_all.py`: stage 18's formula-identity loop and
  ON-endpoint regression call, and stage 23's four
  `front_surface_conduction_correction` call sites, all retagged honestly
  (see §5 below for the one genuinely new finding this surfaced: one of
  stage 18's own pre-existing test values, `7.079002048463575e-6`, IS
  `w_on_m` from exp-046/results.json — a real, literal instance of an
  extinction-derived length, found while wiring the guard through, not a
  hypothetical). New `stage24_length_provenance_guard` (4 gates: refusal
  identity, `inspect.signature` identity, licensed-call identity incl.
  string-preservation, source-inspection). `_STAGE_IDS` widened to include
  24; wired into the dispatch table.
- `experiments/054-heff-length-scale-rederivation/run.py`,
  `experiments/057-graded-black-shell-flagship-mixed-regime/run.py`,
  `experiments/059-qext-x-cylinder-disk-check/run.py` (2 call sites),
  `experiments/060-sharp-uniform-lossy-disk-control/run.py`: all 5
  pre-existing `mixed_length_scale_regime` call sites retagged
  `length_provenance="bench_construction"` (all use a real `R_OUT_M`/
  `r_out_m` — QP-2 confirmed: 100% of committed bench-scale call sites
  classify cleanly, no code-level workaround needed).
- `lab/caveat_lint_config.json`: new entry
  `exp064-length-provenance-disclosure`, `required_sites` =
  `experiments/064-length-provenance-guard/{NOTES.md,phase4_results.md}`
  (VISION confirmed this scoping avoids the narrow, `NOTES.md`-only shape
  that fired Checkpoint criterion 4 at Iteration 40 — `phase4_results.md`
  is included from the start this cycle), `candidate_globs` stated
  explicitly (Red Team non-blocking item 8).

Full bench: **107/107** (`--only 12346789,10,11,18,19,20,21,22,23,24`),
166s. Zero `lab/ARTIFACTS.md`/`lab/artifacts.py`/`AGENTS.md`/`lab/viz.py`
touched; the only `lab/` files touched are `thermo_sidecar.py` (the
guarded module) and `validation/run_all.py`/`caveat_lint_config.json`
(the gate and registry).

---

## 4. Predictions — committed before Phase 4's official run

Restated from Phase 1's QP-1..QP-5 (all independently re-verified during
Phase-3 code-build, not merely re-asserted), plus two new predictions
covering the mandatory-fix docket:

| # | Claim | Predicted outcome |
|---|---|---|
| QP-1 | `length_provenance` required, keyword-only, no default on all 4 guarded functions | `inspect.signature` confirms on all 4 |
| QP-2 | Every committed bench-scale call site (5 in experiment `run.py` files + stage 18/23's own bench-scale cells in `run_all.py`) retags cleanly to `bench_construction`, zero raise | 100% clean retag |
| QP-3 | Stage 23/24's `L_MP5_730X_M` calls become `extinction_derived_diagnostic_only`/`diagnostic_only=True`, not silently relicensed | Confirmed AND now code-enforced (stage 24 gate 4) |
| QP-4 | Refusal gate is a true zero-tolerance absolute identity | 12/12 forbidden-tag cases raise |
| QP-5 | Guard changes zero already-committed physics | All bench-scale regression numbers bit-identical |
| **RT-1** (new) | Stage 24 gate 4 (source-inspection) actually catches a mistagged witness-scale call site, not merely a function-level defect | Deliberate-break test: FAIL when broken, PASS when correct |
| **RT-2** (new) | Pre-existing `netd_disclaimer` strings survive the guard's dict-literal edit byte-identical, on both guarded functions | Exact string match, both functions |

Predictions frozen at this commit, before Phase 4's official full-suite
run is recorded in `phase4_results.md`.

---

## 5. Final configuration for Phase 4

Phase 4 = the official trust-suite run (`lab/validation/run_all.py
--only 12346789,10,11,18,19,20,21,22,23,24`) plus the deliberate-break
verification of stage 24 gate 4, both captured verbatim in
`phase4_results.md`. No WebSearch, no FDTD (T1 escape route: N/A, per
Phase 1 §9, unchanged by Phase 3).
