# PHASE 2 — CRITIQUE · THERMODYNAMICS · exp-083

## Framing (the two questions this seat was asked)

**Is deferring Tier-0 item 2 (the joint EM/THERMO Poynting-bound
energy-interception cross-check) a real gap in THIS cycle's own record?**
A real but minor one — see the attack below. It is explicitly disclosed
(idealization 6, not silently dropped, so it does not repeat the R8/R4
shape this program polices), and my own seat ranked this cycle's primary
test #1 at Iteration 59's own Phase 5, ahead of item 2 — so the ordering
was my own seat's call too, not imposed. But item 2 is zero-FDTD and
desk-only; this cycle's own committed `results.json` now contains every
ingredient it needs (`delta_scene`, both `ΔE_article` legs, the flagship's
established extinction figures) for the first time. Nothing stopped it
riding along the way exp-082 rode two Tier-0 desk items alongside its own
primary FDTD build.

**Does Branch B reopen whether real absorbed power is involved?** Yes,
in a specific, non-obvious way — not because the oscillation itself
becomes dissipative, but because the mechanism now identified sits next
to genuinely lossy material in a way the prior "lossless" guarantee
never covered. Detailed below.

## Steel-man

Idealization 6 is honest, not a violation: it names the exact deferred
item, the exact reason (no FDTD dependency, separately queued), and does
not claim the energy question is closed. Sequencing was defensible on
its own terms — THERMODYNAMICS' own Iteration-59 vote put this cycle's
branch-discriminator test ahead of item 2, precisely because a correct
Poynting-bound interception calculation for an article-loaded, swept-angle
geometry is new analytic machinery in its own right (a joint EM/THERMO
design, not a one-line addition), and bolting it on unreviewed inside an
already-dense 125-call build risks exactly the rushed-addendum failure
mode this program's own R4/R9 history warns against. Running the
branch-discriminator cleanly first, then the energy check with the
now-identified mechanism in hand, is the more disciplined order — the
cross-check is strictly more informative post-Branch-B than it would have
been run blind.

## Sharpest attack

The record leans on Iteration 53's "PAD is provably lossless vacuum"
proof (re-derived from `lab/fdtd2d.py`'s own material law by Red Team,
exp-076) to treat T28's `PAIR_PAD` oscillation as energy-content-free
throughout — a proof this seat once already flagged as narrower than its
shorthand suggests (a prior "non-sequitur" finding on a cycle's §3,
traced to a code-level array identity, not a general argument). That
proof constrains the DOMAIN-WALL echo (Branch A) only: PAD is vacuum by
construction, so that route trivially carries no absorbed power.
**Branch B relocates the diffracting edge to the article's own rim —
R_OUT=78 cells, against `graded_black_shell`, genuinely lossy, not
vacuum.** Nothing here checks whether diffracted flux there is partly
intercepted and re-absorbed by the article's own coating, angle-
dependently. The "T1: N/A, purely coherent" framing throughout
`phase1_proposal.md`/`NOTES.md` is not established for Branch B's own
mechanism — it is carried over from Branch A's.

## Verdict: support-with-changes

The primary result stands: Branch B is decisive (`R²=0.858`, `p=0.0`
against a 20,000-trial null; corroborated by EM's independent
field-difference construction at `R²=0.458`, `p=0.00185`) and the
FDTD/statistical work is clean. The change required is not to this
cycle's own numbers but to what gets inherited: Tier 0 item 2 must be
re-scoped explicitly to Branch B's mechanism (interception at the
article's own absorbing rim, not the domain wall) before any future
cycle repeats the "purely coherent, T1: N/A" framing as settled for the
article-loaded channel. The `r=0.395, p=0.028` scene/empty correlation
this cycle disclosed as an open tension is consistent with — not proof
of — a small genuine energy leak riding under the dominant diffraction
signal; the interception cross-check is also the cheapest way to bound
that possibility.

## Parameter change that would flip this verdict

If Branch A (mechanism continuity, `P*` within 20% of `4.611°`) had won
instead of Branch B, I would move to plain support: Iteration 53's
lossless-vacuum proof transfers directly to a domain-wall-echo mechanism,
and the energy question stays adequately covered without new urgency.
