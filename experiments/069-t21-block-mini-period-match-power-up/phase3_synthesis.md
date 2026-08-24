# PHASE 3 — SYNTHESIS · Panel Iteration 46 · exp-069 (Block MINI power-up)

*Director synthesis, post Phase 2 (five blind critiques + Red Team's
Phase-2 audit, verdict PROCEED-WITH-MANDATORY-FIXES, 10-item docket).*

## Disposition of the mandatory-fix docket

**All 10 items ADOPTED. Zero overridden.** Red Team's own Phase-2 audit did
the reconciliation work explicitly (§2 of `phase2_redteam_audit.md`,
"Reconciliation of the five blind critiques — explicit, per-seat") and
found no place where a blind critique's core point should be rejected — the
Director independently re-read all five critiques plus the audit and
concurs with every disposition. This is stated explicitly, per PANEL.md's
own requirement that the Director "state which criticisms it accepts and
which it overrides, and why," and per LOGBOOK Iteration 45's own standing
instruction not to silently drop a substantive point.

| # | Fix | Disposition | Implementation |
|---|---|---|---|
| 1 | Wire P-069-4 as a binding precondition on the Combined Verdict | ADOPTED | `run.py::score()` — Combined Verdict requires P-069-4 CONFIRM as one of five conjunctive conditions, not an independent side-row |
| 2 | Correct §4's epistemic framing (stationary-phase LIMIT, not exact/independent) | ADOPTED | NOTES.md Idealization 5; `run.py` docstring; `design_geometry.py::P_deg` docstring |
| 3 | Restructure Combined Verdict into one fully-corroborated gate | ADOPTED + EXTENDED (Red Team's own extension of EM's literal ask, itself adopted verbatim) | `run.py::score()` — 5-way conjunction (P-069-1/2/3/4/5) |
| 4 | Pre-committed non-decisive-outcome rule (no PARTIAL-and-defer) | ADOPTED, essentially verbatim (VISION) | `run.py::score()` — third branch is `FORMAL_RETIREMENT_NON_DECISIVE` with the stated reason computed in code, not written after the fact |
| 5 | Minimal R3 (resolution) check, cpl 20→30 | ADOPTED, upgraded from "C80 alone at minimum" to both configs (C40_R3 + C80_R3), matching Red Team's "if budget allows" | `design_geometry.py::R3_CONFIGS`/`r3_config()`; `run.py::block_r3()`; new P-069-5 |
| 6 | Correct Idealization #2's backward "least-aliased" justification | ADOPTED (PHOTONICS + QUANTUM, independently convergent) | NOTES.md Idealization 2; desk-check framing corrected in NOTES.md's own "Desk-first check" section |
| 7 | Bounded 750nm confirmatory sub-sweep | ADOPTED (PHOTONICS), scope: θ∈[38°,41°]/0.2°/16 pts/both configs/STEPS=2800, disclosed as non-gating (P-069-6) given its own under-powered ~1.22-period span | `design_geometry.py::LEG750_*`; `run.py::block_leg750()` |
| 8 | Correct §1 misattribution (exp-066→exp-065) | ADOPTED, verbatim (VISION) | NOTES.md — figures now correctly attributed in the desk-check section and nowhere claims exp-066 tested C80 |
| 9 | R_contact disclosure | ADOPTED, verbatim (MATERIALS) | NOTES.md Idealization 9; `run.py`'s own `r_contact_disposition` field in `results.json` |
| 10 | Report raw `ptp`/`mean` alongside P-069-1's ratio | ADOPTED (EM's supporting note) | `run.py::score()` — `p1` dict carries `ptp`, `mean`, `ratio` all three |

## Budget recomputation (Red Team's docket item 7 instruction)

Phase 1's original design (64 calls, 19.15 min wall, 57.4 min 3× envelope,
75 min hard stop) is superseded. With items 5 (4 R3 calls) and 7 (32 LEG750
calls) added: **100 calls total, ≈6637 CPU-s, wall ≈32.5 min, 3× envelope
≈97.4 min.** This breaches the original 75 min hard stop (as Red Team's
instruction anticipated it might) — resolved by **restating the hard stop
to 100 min**, not by de-scoping, since the actual predicted wall (32.5 min)
carries a comfortable ≈3.1× margin under the new hard stop and neither de-
scope candidate (LEG750, R3) is itself expensive enough to be worth cutting
pre-emptively. The pre-declared de-scope order (LEG750 first, then R3 down
to its C80-alone floor, never DENSE/SETTLE) stands as a live fallback if
the actual run exceeds this prediction significantly, per Red Team's own
instruction.

## No open disagreement carried into Phase 4

Every one of the five blind critiques' load-bearing points, and all of Red
Team's own additional attacks (notably Attack 1, the "not settling" claim
never actually gated by P-069-4 — caught by none of the five blind seats),
is either fixed in the design (`design_geometry.py`/`run.py`, this commit)
or disclosed in `NOTES.md` (this commit). Predictions are committed to git
in this same batch, before `run.py` is invoked for score — house discipline,
non-negotiable.
