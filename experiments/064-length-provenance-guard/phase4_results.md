# exp-064 — Phase 4 Results

Official run, against commit `b9323bb` (Phase 3 synthesis + guard
implementation, predictions frozen before this run). No WebSearch, no
FDTD — T1 escape route N/A, a pure code-architecture/trust-suite cycle.

---

## Full bench — 107/107

```
python3 lab/validation/run_all.py --only 12346789,10,11,18,19,20,21,22,23,24
...
107/107 checks passed in 175 s
```
Exit code 0. All pre-existing 78 checks (stages 1,2,3,4,6,7,8,9,10,11,18,
19,20,21,22,23) still pass unaffected — **diagnostic_only** and
**length_provenance** did not change any already-committed physics
(QP-5, confirmed). The 29 new stage-24 checks (below) all pass.

## Stage 18 — retagged, unaffected

All 10 checks PASS, including the discriminating ON-endpoint regression
(`dt_ss_full_K` = 3.293076e-05, matching LOGBOOK's Iteration-23
side-computation to 1e-9). The formula-identity loop's four test lengths
now carry honest tags — three `bench_construction` (1e-6, 2.34e-6=R_OUT_M,
5.0e-5), one `extinction_derived_diagnostic_only`/`diagnostic_only=True`
(7.079002048463575e-6). **Genuine find, not hypothetical**: that fourth
value is `w_on_m` from `experiments/046-.../results.json` — a real,
literal instance of the exact extinction-derived length category T23
forbids in a conduction role, silently present as an "arbitrary" test
point in this gate since Iteration 31 (exp-054) and never previously
flagged. Harmless (a pure formula self-consistency identity, `h*L==k_air`,
holds for ANY L regardless of what it represents — no physical prediction
was ever drawn from this specific test value), but the guard correctly
surfaces it now that a caller must declare provenance.

## Stage 23 — retagged, unaffected, plus one new disclosure check

All 5 checks PASS (4 pre-existing regression anchors + 1 new: the
`L_MP5_730X_M` diagnostic call's `geometric_realizability` field correctly
reads `"UNGROUNDED..."`, not silently `"N/A"` as a licensed call would).
`correction_factor` at both L_BENCH_M (1.013006) and L_MP5_730X_M
(1.015703) reproduce exp-063's own committed Phase-1 script output
bit-for-bit (QP-5).

## Stage 24 — length_provenance guard, 29/29 (NEW)

**Gate 1 — refusal identity, 12/12.** All four guarded functions raise
`ValueError` for all three forbidden `(length_provenance, diagnostic_only)`
combinations (`extinction_derived_diagnostic_only`+`False`;
`bogus_provenance`+`False`; `""`+`False`). Zero tolerance, zero
exceptions (QP-4 CONFIRMED).

**Gate 2 — `inspect.signature` identity, 4/4.** `length_provenance` is
present, `KEYWORD_ONLY`, and has NO default on `gas_conduction_h_eff`,
`lumped_cube_mass_kg`, `mixed_length_scale_regime`,
`front_surface_conduction_correction` (QP-1 CONFIRMED).

**Gate 3 — licensed-call identity, 5/5.** A `bench_construction`-tagged
call to `mixed_length_scale_regime` reproduces `dt_ss_full_K`=3.293076e-05
exactly (QP-5); both guarded functions' pre-existing `netd_disclaimer`
strings survive the guard's own dict-literal edit byte-identical (RT-2
CONFIRMED — this exact caveat class was lost twice before, Iterations 17
and 40, on these same strings); `geometric_realizability` reads correctly
`"N/A..."` for the licensed call and `"UNGROUNDED..."` for the diagnostic
one (checked in stage 23 above); `model_note` (a third pre-existing key)
also confirmed present.

**Gate 4 — source-inspection, the load-bearing deliverable, 5/5 clean —
plus an independent deliberate-break verification (RT-1).** Text-scans
`run_all.py`'s own committed source for every real
`front_surface_conduction_correction`/`mixed_length_scale_regime` call
site: found 2 witness-scale (`L_MP5_730X_M`) and 3 bench-scale
(`L_BENCH_M`/`R_OUT_M`) call sites, all correctly tagged.

**RT-1, independently verified against the actual committed commit
`b9323bb`** (not a hypothetical description — executed):

```
$ git rev-parse HEAD
b9323bbd2b1dd0928b6bce333d5fbee9b2a0435a

# one witness-scale call site hand-mistagged bench_construction:
$ python3 lab/validation/run_all.py --only 24
  [FAIL] length-provenance-guard · source-scan: live
    front_surface_conduction_correction(L_MP5_730X_M, ...) call site
    carries the diagnostic tag: MISTAGGED OR MISSING
    (expect both markers present in the same call)
27/28 checks passed in 0 s
(exit code 1)

# reverted to the committed source:
$ git status --short
(clean, zero diff)
$ python3 lab/validation/run_all.py --only 24
28/28 checks passed in 0 s
(exit code 0)
```

**This is the single strongest piece of evidence in this cycle's record**:
the source-inspection gate is not merely present, it DEMONSTRABLY catches
the exact failure class (a Phase-3-author mistagging a real witness-scale
call site) that Red Team's Phase-2 audit identified as the proposal's
central defect. Without gate 4, this exact mistake would have shipped
invisibly under a green 27→28-check suite reading only gates 1-3.

---

## Experiment `run.py` retags — QP-2

All 5 pre-existing `mixed_length_scale_regime` call sites (exp-054,
exp-057, exp-059 ×2, exp-060) retagged `bench_construction` on the first
attempt, zero raise, zero code-level workaround (`python3 -c "import ast;
ast.parse(...)"` syntax-verified on all four files; QP-2 CONFIRMED —
every one uses a real `R_OUT_M`/`r_out_m` bench geometric length).

---

## §6 disposition — STRUCK, not restated

Per `phase3_synthesis.md` §1 item 2: Phase 1's §6 realizability claim
(24×–75× gap against an uncited ~14µm figure) does not survive Phase-2
review — MATERIALS' independently-confirmed contradiction against
exp-061's own already-established MP-2/MP-5 record (true gap ≈1×–10.5×),
compounded by PHOTONICS' undisclosed forest-height-vs-path-length
equivalence. **Not restated at a corrected number either** — struck
entirely, per Red Team's own option (b). The underlying question (real
CNT-forest/Vantablack pitch, diameter, and thickness, pinned together)
remains exactly where it already lived: PLAN.md's standing queue item 3.
This document adds nothing new to that thread.

---

## T23 status: CLOSED

`gas_conduction_h_eff`'s own docstring rule — a real geometric length of
the conducting/radiating SOLID body, never an optical/extinction-derived
one, closed BY ARGUMENT at Iteration 23/exp-046 — is now enforced by
required, validated, keyword-only declaration on every call to
`gas_conduction_h_eff`, `lumped_cube_mass_kg`, `mixed_length_scale_regime`,
and `front_surface_conduction_correction`, and independently verified
against this file's own real committed source (gate 4), not merely
against the guard function's own behavior in isolation. **A green
`diagnostic_only=True` call answers a provenance-honesty question ONLY,
never a buildability question** (`geometric_realizability` field,
Red Team mandatory-fix 4) — exp-063's own witness-scale correction-factor
numbers (1.015703 at κ=2.0 W/(m·K), κ_critical=0.089731 W/(m·K)) are
unchanged in value, now correctly and permanently labeled as diagnostic
rather than licensed.
