# Phase 2 Critique — QUANTUM OPTICS seat, candidate exp-067

## 1. Steel-man (support side)

The two-tag `r_contact_provenance` scheme correctly follows the allow-list-not-deny-list discipline `_validate_length_provenance` established (anything not explicitly licensed raises, rather than trying to enumerate known-bad values), ties its diagnostic tag to a mandatory paired boolean exactly the way `extinction_derived_diagnostic_only` requires `diagnostic_only=True`, and proposes a stage-25 gate 4 explicitly modeled on stage-24 gate 4 — the source-inspection mechanism that is the actual lesson of T23 ("closed by argument… violated in the open for three cycles" until code enforcement existed). Disclosing 100% of this cycle's test values honestly as `analogy_proxy_diagnostic`, with zero claimed as `measured_direct`, shows the proposers understand the pattern's *purpose* — provenance-honesty, not buildability — not just its syntax.

## 2. Sharpest attack

The excerpt never states that `bonded_substrate_conduction_correction`'s return dict carries `r_contact_provenance`/`r_contact_diagnostic_only` forward. Every existing `length_provenance`-guarded dict-returning function writes `length_provenance`, `diagnostic_only`, *and* a `geometric_realizability` honesty-note directly into its return dict — documented reason (`absorbed_power_established_ratio`'s own docstring): "the idealization travels with the number into every results.json… never a silent float." Nobody re-reads `thermo_sidecar.py` source before citing a number; they read results.json. If the new function's dict omits these keys, the `ValueError` guard is airtight at the call site but the tag evaporates the instant the function returns — recreating T23's exact failure ("disclosure nothing checks") one hop downstream of where the fix landed. Separately, the excerpt describes only a gate-4 analog (source-scan); it never claims a gate-2 analog (`inspect.signature`: keyword-only, no default) — without that, a future default value on `r_contact_provenance` compiles silently, and a call site that simply omits the argument produces no text for gate 4's regex to catch at all.

## 3. Verdict

**Support-with-changes.**

## 4. The single change that would flip this to unconditional support

Require the actual implementation to do two things the proposal excerpt currently leaves unstated: (a) write `r_contact_provenance`, `r_contact_diagnostic_only`, and an analogous honesty-note (mirroring `_geometric_realizability_note`) as literal keys into `bonded_substrate_conduction_correction`'s return dict, and (b) give stage 25 all four gate types stage 24 has — not just the gate-4 source-scan, but gate-1 (forbidden-tag refusal identity), gate-2 (`inspect.signature` keyword-only/no-default identity), and gate-3 (licensed-call numeric + string-preservation identity) analogs. As proposed, only the gate-4 half of the existing four-gate discipline is explicitly committed to.

---

**Files reviewed:**
- `/home/user/photon-lab/lab/thermo_sidecar.py` — `_validate_length_provenance` (lines 236–260), `LICENSED_LENGTH_PROVENANCE`/`DIAGNOSTIC_ONLY_PROVENANCE` (215–233), `_geometric_realizability_note` (263–282), and all four guarded functions (`gas_conduction_h_eff` 286, `lumped_cube_mass_kg` 310, `mixed_length_scale_regime` 333, `front_surface_conduction_correction` 435) — note each dict-returning one writes `length_provenance`/`diagnostic_only`/`geometric_realizability` into its return value.
- `/home/user/photon-lab/lab/validation/run_all.py` — `stage24_length_provenance_guard` (lines 2173–2336): gate 1 refusal identity (2229–2260), gate 2 signature identity (2262–2273), gate 3 licensed-call identity (2275–2307), gate 4 source-inspection text-scan (2309–2336).