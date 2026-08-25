# PHASE 3 — SYNTHESIS · Panel Iteration 48 · exp-071

**Director synthesis, post Red Team's Phase-2 audit verdict:
PROCEED-WITH-MANDATORY-FIXES, 7 mandatory items, ZERO overridden.** Full
audit: `phase2_redteam_audit.md`. This document records the
accepted/overridden disposition of every Phase-2 finding (PANEL.md's own
requirement) and the concrete implementation of each accepted fix.

## Disposition of all findings — nothing overridden

| # | Finding | Seat | Severity (Red Team) | Disposition |
|---|---|---|---|---|
| 1 | No settling-closure check exists for C60/C70 | ELECTROMAGNETISM | High, one of two most severe | **ACCEPTED.** Block SETTLE-C60C70 added, binding precondition on P-071-2. |
| 2 | Rayleigh resolution floor risk (REFUTE band) | QUANTUM OPTICS | High, other of two most severe | **ACCEPTED**, and **EXTENDED** by Red Team's own Phase-2 audit to gate the CONFIRM band too (the CONFIRM 30% threshold sits at only 75% of full resolving power — under the floor, not over it). Both directions of P-071-2 now gated. |
| 3 | Missing "ABSORB is not a material" caveat, CONFIRM-branch overclaim | MATERIALS | Real, cheap, mandatory (language) | **ACCEPTED.** Caveat reinstated verbatim in run.py's `ABSORB_NOT_MATERIAL_CAVEAT`; CONFIRM branch renamed `CONFIRMED_ABSORB_TIED_NUMERICAL_BOUNDARY_EFFECT`. |
| 4 | THERMO scope-inapplicability never stated | THERMODYNAMICS | Real, cheap, mandatory (language) | **ACCEPTED.** `THERMO_SCOPE_CAVEAT` added, printed unconditionally alongside every Combined Verdict. |
| 5 | 600nm-only scope can't license "genuine mechanism" language | PHOTONICS | Real but secondary — softens a label | **ACCEPTED as a caveat** (`WAVELENGTH_SCOPE_CAVEAT`, disclosed unconditionally). PHOTONICS' own proposed fix (a confirmatory 750nm leg) is **NOT** run this cycle — Red Team's audit ruled it recommended, not mandatory, out of this cycle's LOCKED 600nm-only mandate scope; queued as a fast-follow for Iteration 49 rather than broadening this cycle. |
| 6 | `_free_period_search` "identical methodology" was a prose promise, not code | QUANTUM OPTICS | Real, cheap, mandatory | **ACCEPTED.** `design_geometry.py` now imports `_fixed_period_fit`/`_free_period_search` by reference from exp-069's `run.py` and asserts the defaults `(center_deg=39.0, lo_deg=1.0, hi_deg=4.0, n_grid=400)` in code at import time. |
| 7 | De-scope docket didn't protect the new mandatory fixes | Red Team (own finding) | Real, cheap, mandatory | **ACCEPTED.** `fdtd_budget_minimum()` now names Block SETTLE-C60C70 and the resolution-floor computation as never-de-scoped, alongside Block G1 and Block DENSE-CAUSAL. |
| 8 | Hard stop understates the revised budget | Red Team (own finding) | Real, cheap, mandatory | **ACCEPTED.** Hard stop restated from 90 min to **100 min** (see Budget below). |
| — | `A=752` congruence / G1 construction | Red Team (own check) | Not a defect | Confirmed sound; no change. |

**Zero criticisms overridden.** Every mandatory-fix-docket item from
`phase2_redteam_audit.md` §6 is implemented exactly as specified, in code
where a code artifact exists (`design_geometry.py`, `run.py`) and in text
where the fix is language-only (the three caveats above, carried in
`run.py`'s `FROZEN_PREDICTIONS` block and printed with every result
regardless of outcome).

## Budget, recomputed after all mandatory fixes

`design_geometry.py::fdtd_budget()` (code-produced, not hand-typed — R4):

```
Block G1              calls=  4  cpu_s=239.2
Block DENSE_CAUSAL     calls= 62  cpu_s=3971.1
Block R3_PEAK          calls=  8  cpu_s=1672.0
Block SETTLE_C60C70    calls=  4  cpu_s=384.3
TOTAL calls = 78
TOTAL cpu_s = 6266.6
wall = 30.64 min
3x envelope = 91.92 min
```

Matches Red Team's independently-computed budget check
(`phase2_redteam_audit.md` §5: 78 calls, 6266.6 CPU-s, 30.65 min, 91.96 min
envelope) to within rounding.

**Hard stop: 100 min** (restated from the Phase-1 proposal's 90 min —
mandatory fix 8/Red Team item 7 — to preserve this program's own "a few
minutes past the 3× envelope" convention under the revised 78-call
budget).

**De-scope order if breached, updated (mandatory fix 7/Red Team attack
7):**
1. First: retract Block R3-PEAK from the 4-config extension to the
   literal `C40_R3`/`C80_R3`-only minimum (`fdtd_budget_minimum()`: 74
   calls, 26.41 min).
2. Second, only if still breached: retract Block R3-PEAK to a single peak
   angle (41.4°) at `C40_R3`/`C80_R3` only.
3. **Never de-scoped**: Block G1, Block DENSE-CAUSAL, **Block SETTLE-C60C70,
   and the resolution-floor computation** (the two items this cycle's own
   mandatory-fix docket added — Red Team's own explicit instruction, since
   the pre-existing de-scope logic predates these fixes and would
   otherwise silently drop them under budget pressure).

## T1 escape route, Checkpoint candidacy — unchanged from Phase 1

N/A (instrument/mechanism-identification class). No Checkpoint-criterion-2
candidacy. No Checkpoint criterion fires at Phase 3 (Red Team's Phase-2
audit §7: none of the five criteria apply — no engine-physics build, no
mechanism class bounded, no drift; the two severe findings were caught and
fixed within this cycle's own Phase 2, the discipline working as
intended).

## Predictions — committed to git BEFORE any run (house discipline, non-negotiable)

See `NOTES.md` for the full frozen predictions table (P-071-G1, Block
SETTLE-C60C70, P-071-1 through P-071-5, the Combined Verdict logic, and
all three mandatory caveats) — reproduced verbatim from `run.py`'s
`FROZEN_PREDICTIONS` string, so the committed prose and the executed code
cannot drift apart (this program's own established discipline, exp-046/065
precedent).

## Gates

Full bench (`lab/validation/run_all.py --only 12346789`) reconfirmed green
this shift before any panel work began: 41/41 checks (heavy stage 5
optional per house convention). Zero `lab/` diff throughout this design —
every config, rescale idiom, and cost figure is imported from
exp-065/exp-069, never redefined. `assert_lab_clean()` (run.py, reused
verbatim from exp-069's own idiom) re-verifies this at the start of every
run. P-071-G1 is the one local **absolute-identity** gate; it gates every
other number this cycle produces, including the reused exp-069 dense data.

## Tooling disclosure carried forward

Phase 1's proposal disclosed that `WebSearch`/`WebFetch` were present in
that sub-agent's own tool list. The Director independently confirms this
session also has `WebSearch`/`WebFetch` available (deferred tools, this
session's own tool list). **This is a capability change worth flagging to
Marsh** — PLAN.md's Iteration-48 queue item 2 (`R_contact`'s
`measured_direct` literature search) has been blocked for eight
consecutive cycles purely on this tooling's absence. It remains out of
this cycle's LOCKED scope (item 1 only); if wall-clock capacity remains
after this cycle's own FDTD run and Phase 5 close, the Director will
consider picking it up as a same-shift bonus per PLAN.md's own standing
invitation — not a commitment, disclosed here rather than silently
deferred a ninth time without comment.
