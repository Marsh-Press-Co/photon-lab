# PHASE 2 — CRITIQUE · VISION SCIENCE · Panel Iteration 47

**Proposal:** `phase1_proposal.md` (QUANTUM OPTICS lead) — T28 mechanism
desk-check batch, zero FDTD cost.

## Steel-man (≤150 words)

This is disciplined desk work: every quantity traces to already-committed
`results.json`/`design_geometry.py`, reuses `_fixed_period_fit`/
`_free_period_search` verbatim rather than re-deriving statistics (R4), and
states real, load-bearing idealizations (the `R_OUT`=`W_OBJ` degeneracy,
the `|c|≤10` search-space bound, the linear-superposition assumption behind
the beat formula). It correctly declines a constraint-3/Checkpoint-2 claim
and treats the batch as a "numerology-vs-mechanism discriminator, not a
mechanism proof" — appropriately modest. Disclosing the reconnaissance
numbers openly, rather than quietly folding them into the bands, is the
right instinct: it lets Phase 2 see exactly what informed the design. It
also meets the standing forward tripwire's deadline with real, falsifiable
content rather than a token gesture.

## Sharpest attack (≤150 words)

§5 has no pre-committed disposition for outcomes that land in neither band
— and such gaps exist for three of five items. P-070-1: one config ≥0.30,
the other <0.30 (or both in [0.15,0.30)) is undefined. P-070-2: either
branch landing in [1%,10%) is undefined. P-070-4: a match ≤1% with
R²∈[0.40,0.70) satisfies neither CONFIRM nor REFUTE. Only P-070-5 is truly
binary. exp-069 hit exactly this shape (P-069-2/3 both landed "NEITHER")
and only survived it honestly because mandatory-fix-4 pre-wrote an
explicit "anything else ⇒ FORMAL RETIREMENT, stated reason" catch-all —
the direct fix for what this program's own record calls the "PARTIAL
escape hatch." This proposal explicitly declines that architecture ("No
Combined Verdict gate is proposed here... unlike exp-069's five-way
conjunction"), leaving each item's gray zone to be narrated at Phase 3 with
no binding rule constraining how.

Worse, the disclosed recon isn't neutral background — it already sits
*inside* two of the five CONFIRM bands. P-070-2's CONFIRM threshold is
"≤1% relative"; the disclosed `A_alt≈233.19` vs `3·R_OUT=234` is 0.35%
off — already inside. P-070-4's CONFIRM requires "≤1% AND R²≥0.70"; the
disclosed `A_eff≈518.81` vs `518` is 0.16% off, and §3 row 8 already
cites the "already-computed... post-hoc R²=0.7666" — 0.0666 above the
0.70 line. Two of five bands were set with the answer already in hand,
comfortably inside; nothing in §5 discloses whether the 1%/0.70
thresholds were chosen before or after those specific numbers were
computed. That is the shape of HARKing regardless of intent, and with no
gray-zone catch-all in place, a favorable narration of P-070-2/4 as
"CONFIRMED, narrows queue item 2" is exactly the kind of cherry-pickable
multi-way reporting this program's own R4/Checkpoint-4 history keeps
punishing when it appears anywhere else.

## Verdict

**support-with-changes.**

## Single change that would flip to full support

Add an explicit, pre-committed catch-all disposition for every item's gray
zone — e.g. "any P-070-N outcome outside both its CONFIRM and REFUTE band
is reported as `NEITHER`, disclosed verbatim in NOTES.md, and does NOT
count toward narrowing queue item 2's scope" — mirroring exp-069's own
mandatory-fix-4 language, plus a one-line disclosure in §5 itself (not
buried in §1) that the P-070-2/P-070-4 CONFIRM thresholds already contain
the disclosed recon values, so Phase 3/4 readers can judge the
pre-registration's independence for themselves.
