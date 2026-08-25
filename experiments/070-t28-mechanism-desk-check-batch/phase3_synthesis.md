# PHASE 3 — SYNTHESIS · Panel Iteration 47 · Director

## Disposition of Phase 2

Five blind critiques (PHOTONICS, MATERIALS, ELECTROMAGNETISM,
THERMODYNAMICS, VISION SCIENCE), all `support-with-changes`, none opposed.
Red Team's Phase-2 audit: **PROCEED-WITH-MANDATORY-FIXES**, 10-item docket,
**zero criticisms overridden** — every seat's sharpest attack accepted in
full, two (EM's item-a attack, PHOTONICS'/MATERIALS' look-elsewhere
concern) independently *proven* by Red Team's own executed diagnostics
rather than merely argued.

**Director accepts the Red Team ruling in full, no override, on any of
the ten docket items.** This is not a close call: Red Team did not merely
adjudicate the five critiques, it re-ran the proposal's own committed
logic against the proposal's own committed data and demonstrated, not
argued, that (a) the original item-(a) gate confirms today regardless of
which hypothesis is true, and (b) the named-constant search currently has
statistically zero power to distinguish a real geometric mechanism from
chance (100% of 10,000 random targets clear the 1% band). A Director
override would need a reason strong enough to contradict independently
executed code against committed data; none exists here.

## What changed from Phase 1 to the committed design

| # | Phase-1 proposal | Phase-3 committed design |
|---|---|---|
| 1 | Item (a) scored on bare free-fit R² (≥0.30 both configs) | Scored on the **recovered period's** deviation from `P*_delta` (≤20% both configs to CONFIRM; either config's R²<0.15 or deviation≥50% to REFUTE) — closes Attack 1 |
| 2 | Items (b)/(d)/(e): raw closest-match relative deviation only | A **permutation-null control** (`N=20,000`, `T~Uniform(100,1600)` cells, identical search space) is REQUIRED before any CONFIRM; `p≤0.05` gates CONFIRM on (b)/(d) — closes Attack 2 |
| 3 | "Best match" (singular, undefined under ties) | **All ties reported** (within 1e-9 relative); item (e) counts a match on ANY shared tied expression between branches — closes Attacks 3/4 |
| 4 | No gray-zone disposition | Every item has an explicit **NEITHER** catch-all, disclosed, non-narrowing — closes Attack 5 |
| 5 | No numerical-artifact caveat | Mandatory disclosed caveat (§ below): every `NAMED` constant is FDTD domain-construction bookkeeping, not a material parameter — a match is at least as consistent with a numerical-boundary-construction artifact of this engine's own **graded-loss absorbing boundary** (not PML — VALIDATION.md) as with a physical mechanism — closes Attacks 6/MATERIALS, with Attack 7's terminology fix applied |
| 6 | WKB fold-in silently absent | Disclosed explicitly (idealization, below) — closes Attack 6/THERMODYNAMICS |
| 7 | Recon-inside-band proximity not disclosed | Disclosed explicitly in NOTES.md (below) |
| 8 | — | Search-space provenance sentences below use the per-target-correct comparator (Red Team's own Attack 3 catch) |
| 9/10 | — | The null control runs as part of the committed script itself, before any result is narrated; PLAN.md queue item 2 is narrowed only by items clearing the corrected gate |

All ten items are implemented in `design_geometry.py` (module docstring
maps each fix to its implementation) and `desk_check_mechanism.py`
(the actual scoring). Nothing here required new `lab/` code or any FDTD
call — the batch's zero-cost, reuse-only construction is unchanged.

## Predictions — restated, corrected, committed to git BEFORE this run

See `NOTES.md` for the full predictions table (P-070-1 through P-070-5,
corrected per the docket above) and idealizations. This file and
`NOTES.md` are committed together, before `desk_check_mechanism.py` is
executed as this cycle's Phase 4 — the code itself was written and
debugged against this same committed data during Phase 3 (identical to
how Red Team's own diagnostics informed this docket), but the score
thresholds were fixed by Red Team's ruling, not tuned by the Director
after peeking at a result the committed code hadn't yet produced under
its final form.

## Gates

Zero new `lab/` diff — no trust-suite stage is added or touched. The
full bench (`lab/validation/run_all.py`, stages 1–25, heavy stage 5
optional) was reconfirmed green at the start of this shift (41/41 checks
in the fast subset run this session; see SESSION_LOG.md). No FDTD calls
occur in this cycle at all — there is no `box_dev`/`cross_dev` gate to
apply, and no absolute-identity gate is needed (this batch reads, but
does not re-derive, exp-069's own already-gated `results.json`; it does
not recompute `C_empty` values, only refits already-committed series).

## Checkpoint-criterion-2 candidacy

**Explicitly declined**, unchanged from Phase 1 — no mechanism class is
bounded by any outcome here.
