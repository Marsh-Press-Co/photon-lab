# PHASE 2 — CRITIQUE · PHOTONICS · Panel Iteration 70 · exp-093

*Blind, parallel critique. No access to any other seat's Phase-2 output
this cycle.*

## Steel-man (≤150 words)

This is disciplined instrument work that earns its keep. It executes
exactly the Reconciled Iteration-70 queue exp-092's own Red Team audit
set (§8, items 1/2/3/5), in the sequence Red Team itself mandated
(sigma check before net expansion — learned, correctly, from exp-092's
own resequencing catch), with zero scope creep and an honestly declined
item 6. The sigma_max PRIMARY-channel check is now *correctly localized*
to the actual near-null region (41.8°/42.0°), closing a real scope gap
Rank 3's original three census angles never covered. R13's floor gate is
applied consistently to the new sweep, correctly flagging 41.8°/42.0° as
NODE-UNRESOLVABLE rather than silently scoring near-null noise. The
dispersion integral (item 4) is properly hedged: it REFUTEs one specific,
pre-declared candidate mechanism by 2–3 orders of magnitude and explicitly
declines to promote its own reverse-calculated 24,000–72,000-cell
implied length to a new hypothesis — genuinely disciplined restraint.

## Sharpest attack (≤150 words)

Item 1's off-grid sweep refines only **angular** density (0.025° steps
in θ) at **fixed cpl=30** — it never tests spatial resolution at the
disputed 41.75°–41.90° window. A "TWO-NODE CONFIRMED" verdict is framed
as ruling out a macro-period aliasing artifact, but says nothing about
whether the double-crossing is a **cpl=30-specific discretization
artifact** — the exact failure mode R15 exists to catch, established by
this thread's own parent cycle (exp-091) via a genuine cpl 20→30 check,
not via denser angular sampling. No cpl=40 (or any second resolution)
point is planned anywhere near this window; the declined Tier-2 cpl=40
point targets the *original* census angles, not here. Worse, any
floor-clearing "confirming" point would clear FLOOR_FRAC=0.10 — the
identical gate LOGBOOK Iteration 66/67 found empirically inadequate at
1.3–1.5× margins, precisely the thin-margin regime a genuine near-total
null neighborhood produces. This design cannot license the R15-grade
conclusion item 2 is poised to consume from it.

## Verdict

**Support-with-changes.**

## Parameter change that would flip verdict to full support

Add an explicit, pre-registered Idealization stating that item 1's
TWO-NODE CONFIRMED/SINGLE-NULL/STILL AMBIGUOUS outcome is angular-only
and **not yet R15-qualified** — and gate item 2 so it may only report a
provisional zone (both readings, as it already does for STILL AMBIGUOUS)
rather than a settled two-node or single-null input — until a genuine
cpl=40 spot-check is run at the interior near-null angles themselves
(not the original census angles). A cheap version costs zero extra
budget: swap 2 of item 1's 6 off-grid θ-points for a cpl=40 check at
2 fixed interior angles instead.
