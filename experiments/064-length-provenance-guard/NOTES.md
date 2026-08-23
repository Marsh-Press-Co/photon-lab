# exp-064 — An Enforced `length_provenance` Guard, Closing T23

**Panel Iteration 41.** Lead: QUANTUM OPTICS, by rotation. T1 escape
route: **N/A** — a code-architecture/instrument-trust cycle on the
standing THERMO sidecar, the exp-054/060/063 class: zero constraint-
1/2/3/4 metric scored, zero FDTD. Executes Iteration 40's binding forward
commitment (Red Team's Phase-5 final audit): resolve live thread T23's
witness-scale length-legitimacy question this cycle — deferred at
Iterations 38, 39, and 40 (disclosure only) — or a fourth deferral is
itself a program-integrity finding at Iteration 42. Full process record:
`phase1_proposal.md` (QUANTUM OPTICS), `phase2_critique_{photonics,
materials,em,thermodynamics,vision}.md` (five blind critiques, all
support-with-changes), `phase2_redteam_audit.md` (PROCEED-WITH-MANDATORY-
FIXES, no Checkpoint criterion fires), `phase3_synthesis.md` (this
cycle's Director synthesis, all in this directory).

---

## Hypothesis

`gas_conduction_h_eff`'s own docstring (`lab/thermo_sidecar.py`) states,
unconditionally, that its length argument must be "a real geometric
length of the conducting/radiating SOLID body... NEVER an optical/
extinction-derived length." T23 opened this question at Iteration 22
(exp-045, `w_on` vs `r_out`), closed it BY ARGUMENT — never by code — at
Iteration 23 (exp-046), and the rule has since been violated in the open:
exp-063's own witness-scale `front_surface_conduction_correction` calls
(`L=τ_true/α`, the MP-5/730× figure) are, on the rule's own plain text,
exactly the forbidden category — disclosed in prose at Iterations 38, 39,
and 40, never enforced.

**Hypothesis**: converting this rule from a docstring a caller must
remember into a required, validated, keyword-only `length_provenance`
argument — an allow-list of licensed provenances
(`bench_construction`/`measured_geometric`), plus an explicit
`diagnostic_only` escape hatch for extinction-derived lengths used for
bracket/diagnostic purposes only — will (1) change zero already-committed
physics for every real bench-scale call site, (2) correctly and
losslessly re-tag exp-063's own witness-scale calls as diagnostic rather
than licensed, and (3) be enforced not just at the function level but
against the actual committed source of every real call site, closing the
"disclosure nothing checks" failure pattern that let T23 survive three
cycles.

---

## Setup — parameter table (Phase 1 §3/§4, unchanged in substance by
Phase 3; see `phase3_synthesis.md` §3 for the applied mandatory-fix
docket, primarily additive)

| Knob | Value / spec |
|---|---|
| `LICENSED_LENGTH_PROVENANCE` | `frozenset({"bench_construction", "measured_geometric"})` |
| `DIAGNOSTIC_ONLY_PROVENANCE` | `frozenset({"extinction_derived_diagnostic_only"})` |
| `_validate_length_provenance(length_provenance, diagnostic_only)` | raises `ValueError` unless licensed or (diagnostic-tagged AND `diagnostic_only=True`) |
| `_geometric_realizability_note(length_provenance, diagnostic_only)` | (Phase 3 addition, mandatory-fix 4) — `"UNGROUNDED..."` when diagnostic, `"N/A..."` when licensed; the buildability-vs-provenance-honesty distinction |
| `gas_conduction_h_eff`, `lumped_cube_mass_kg` | gain `*, length_provenance, diagnostic_only=False` |
| `mixed_length_scale_regime`, `front_surface_conduction_correction` | gain the same, validate once, forward unchanged to internal calls; return dicts gain `length_provenance`/`diagnostic_only`/`geometric_realizability` keys |
| `biot_number` | unchanged, unguarded (no length argument) |
| `lab/validation/run_all.py` stage 24 | 4 gates: refusal identity (12 forbidden-tag cases), `inspect.signature` identity, licensed-call identity (numeric + string-preservation), **source-inspection** (Phase 3 mandatory-fix 1 — text-scans this file's own committed source for every real call site, not just fresh in-memory calls) |

---

## Falsifiable predictions — committed BEFORE Phase 4's official run

See `phase3_synthesis.md` §4 for the full table (QP-1 through QP-5, plus
Phase-3-added RT-1/RT-2). Restated in brief:

- **QP-1/QP-4**: `length_provenance` required/keyword-only/no-default on
  all 4 functions; 12/12 forbidden-tag refusals.
- **QP-2/QP-5**: all 5 committed bench-scale call sites (experiment
  `run.py` files) plus stage 18/23's own bench-scale cells retag cleanly,
  zero physics change (bit-identical regression numbers).
- **QP-3**: stage 23/24's witness-scale `L_MP5_730X_M` calls become
  diagnostic-only, not silently relicensed.
- **RT-1**: a deliberately-injected mistagged call site is CAUGHT by
  stage 24 gate 4 (FAIL), and the fix, once reverted, PASSes again —
  proving the source-inspection gate is not vacuous.
- **RT-2**: pre-existing `netd_disclaimer` strings survive the guard's
  edit byte-identical on both guarded functions.

---

## Idealizations (Phase 1's five items stand; §6's realizability finding
is STRUCK per Phase 3 §1 item 2 — not an idealization of a surviving
claim, a claim that does not survive)

1. **The guard enforces DECLARATION, not detection.** `_validate_length_
   provenance` cannot inspect where a float actually came from; it only
   checks the string a caller asserts. A caller could, in principle, tag
   an extinction-derived length `"measured_geometric"` and the guard
   alone would not catch the lie — this is why Phase 3's stage-24 gate 4
   additionally source-scans the *specific, currently-known* witness-scale
   variable name (`L_MP5_730X_M`) rather than relying on the allow-list
   alone; a genuinely NEW mistagged variable name would still only be
   caught by declaration discipline, not detection.
2. **Two licensed categories may prove too coarse or too narrow over
   time**; a one-line addition to `LICENSED_LENGTH_PROVENANCE` if a future
   geometry class needs a third — out of this cycle's scope.
3. **`biot_number` is correctly left unguarded** — it takes no length
   argument; if a future length-dependent Biot variant is added, it
   inherits this guard.
4. **The allow-list checks provenance-TIER, not provenance-ROLE**
   (Red Team attack 5, non-blocking) — a future honestly-measured
   gap/standoff or aperture length would pass the identical tag while
   feeding a physically different conduction regime into the same
   formula. No current or proposed call site is anything but `r_out`-class
   or the MP-5 extinction-derived length; a structural blind spot, not a
   live violation.
5. **No FDTD, no new network access.** T18 (WebFetch) blocked, as every
   prior cycle; the Phase-1 route-(a) diligence (2 WebSearch queries) is
   disclosed in `phase1_proposal.md` §6 but its headline finding does NOT
   survive into this cycle's scored record (see Idealizations header
   above and `phase3_synthesis.md` §1 item 2).

---

## Registry (mandatory-fix docket item, `caveat_lint_config.json`)

New entry `exp064-length-provenance-disclosure`: any document restating
exp-063's own witness-scale correction-factor numbers must disclose they
are now `diagnostic_only=True`, not licensed, and that a green
diagnostic-path gate answers a provenance-honesty question only, never a
buildability one. `required_sites` = this file + `phase4_results.md`
(both from the start — VISION confirmed this avoids the `NOTES.md`-only
narrow-scoping shape that fired Checkpoint criterion 4 at Iteration 40).
`diagnostic_only`/`provenance-honesty`/`buildability` — the phrase this
paragraph itself carries, satisfying the registry entry at this site.

---

## Result

TBD — filled after Phase 4's official run (`phase4_results.md`).

## Learned

TBD — filled after Phase 4's official run.

## Next

TBD — filled after Phase 5.
