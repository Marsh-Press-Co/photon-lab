# Phase 2 Critique — MATERIALS & METAMATERIALS (blind)

*Panel Iteration 76. Critiquing `phase1_proposal.md` (THERMODYNAMICS, rotation
lead). Independent, discipline-only critique per PANEL.md — not shown any
other seat's Phase 2 output.*

## 1. Steel-man

This is careful, well-scoped house-discipline work executing a properly
reconciled queue. It reuses only already-verified machinery — no new `Sim`,
registration-gate, or geometry code — and spends R5 for the first time on a
genuinely defensible target (Null B, the one null with two same-direction
marginal shifts on file, not a resource-blind default). Item 1's asymmetric
bracket width is derived from Null C's *own* directly-measured cpl20→cpl30
shift (not borrowed by analogy), correctly discharging R17, and pre-registers
a real three-way outcome space (SIGN-CHANGE / VANISHING-AMPLITUDE /
INCONCLUSIVE) rather than a single-hypothesis test. It explicitly discloses
(Idealization 49) that any Richardson-style figure remains descriptive, never
claims a convergence-order proof. Item 3 adds real falsifiable content at
zero marginal FDTD cost. As MATERIALS work, this is honest: it neither
overclaims nor manufactures a realizability finding where none exists.

## 2. Sharpest attack

R15's own addendum (exp-094, this sub-thread's founding rule) requires that
**before** a third resolution point is trusted to adjudicate genuine
migration vs. artifact, the *new* family must independently reproduce the
already-known-correct sign at a robust, far-from-null angle — because a
uniform reversal is indistinguishable from a systematic registration defect
baked into that family's own construction. R5 has spent **zero** real FDTD
calls in its entire recorded history — independently confirmed this session:
`experiments/095-.../results.json::rank2={"skipped":true,"reason":"Rank 1
combined go/no-go gate did not PROCEED"}`. Its own "Gates 1–6" are
construction-time/sigma-wiring checks, not registration verification —
exp-095's own NOTES.md says so outright ("Gate 5 has never...independently
verified geometric/angular registration"). Item 2 spends all 24 new R5 calls
inside a ≤0.5°-wide bracket hugging Null B itself, plus one settling angle at
the same location — zero far-from-null R5 points anywhere. As designed, the
Richardson figure item 2 produces cannot be trusted by this proposal's own
governing rule.

## 3. Verdict

**Support-with-changes.**

Secondary, lower-priority note (not the flip criterion): exp-098's own
Reconciled Iteration-76 queue item 5 — this seat's own carried item —
explicitly asks that "the cpl-is-orthogonal-to-realizability finding" be
*stated explicitly in a future Result section*. Independently confirmed via
`design_geometry.py` (`L_GEOMETRIC_M_R4 == L_GEOMETRIC_M_R5` to 1e-12; only
`DX_M_R{4,5}` and cell counts change with `cpl`) that this finding is in fact
true and cheap to state — but this proposal's §3 T1 disposition never uses
the words "realizability" or "orthogonal" anywhere, leaving its own queued
deliverable undischarged a second time. This is a paperwork gap, not a
physics one, and does not by itself change the verdict.

## 4. Parameter change that would flip the verdict

Add **one** far-from-null R5 sign-check angle (e.g. reuse Rank 1a's own
39.2°/39.4° idiom, or any angle ≥1° from every established cpl=20 null) at
both legs and both conditions — 4 additional `sim.run()` calls, run and
required to reproduce the already-known R4/R3 sign before item 2's Rank 2b
interior points or its Richardson figure are reported as anything beyond
"uninterpretable pending R5 ground-truth check." With that gate in place and
passing, this seat supports the proposal as designed.
