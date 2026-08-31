# Phase-2 Blind Critique — MATERIALS & METAMATERIALS

*Panel Iteration 72. Seat charter: sub-wavelength structure; what could
physically realize the proposed optical behavior; owns the realizability
bound (published / plausible / unobtainium-with-parameters). Reviewing
`experiments/095-t28-r4-ground-truth-sign-control/phase1_proposal.md` blind
— no other seat's Phase-2 critique read.*

## Steel-man (≤150 words)

This is disciplined instrument work. Rank 1's ground-truth sign control
correctly gates the expensive `R5` spend (32 of 60 calls) so a compromised
`R4` anchor cannot be paid for twice — exactly the R6/R15-lineage
discipline this sub-thread's own history shows is easy to skip. I
independently recomputed every entry in the new `R5` geometry-constants
table (`R5_RATIO=2.5` substituted into `r4_config()`/`r3_config()`'s own
formula) and every value reproduces exactly, including the Gate-3
bit-identical-radius claim: `L_GEOMETRIC_M_R5 = 195×1.2×10⁻⁸ = 2.34×10⁻⁶`
m, matching native/`R3`/`R4` to <10⁻²¹ m. The `cpl=45` rejection is also
arithmetically correct — `78×2.25=175.5` really does force a genuine
~0.28% shell-radius drift that would break Gate 3. Idealization 17 is
disclosed honestly, not buried. Call accounting (60/10-call totals) checks
out to the call.

## Sharpest attack (≤150 words)

MATERIALS' own exp-094 self-review named the real risk: a "shared
construction-recipe artifact" could "alias consistently across all three
points the same way," and named `cpl=50` by name as the option to avoid.
exp-095's override is arithmetically correct but not merely a defensible
trade-off — it is structurally inescapable in a way the proposal never
surfaces: `R_OUT=78` is even, so under this recipe ONLY half-integer ratio
steps (1.5, 2.0, 2.5, 3.0…) keep the physical radius Gate-3-exact.
`cpl=50` (2.5×) simply continues the arithmetic progression `R3`(1.5×)/
`R4`(2.0×) already are — of every viable "third point," it is the LEAST
alias-breaking choice available, not a neutral one. This means the
mechanical `r{n}_config()` recipe (Idealization 17) cannot, by
construction, ever produce the alias-breaking third point R15's addendum
calls for without sacrificing the radius invariant governing this whole
sub-thread — yet ~529 of 744 CPU-min (71% of budget) is spent on exactly
this item, framed in §1 as R15's own "minimum-discharge package."

## Verdict: support-with-changes

The arithmetic, gating, and disclosure discipline are sound and I found no
computational defect. But §1's "minimum-discharge package" framing and
§5's Rank-2b outcome taxonomy (TWO-NODE CONFIRMED / SINGLE-NULL / STILL
AMBIGUOUS) both implicitly promise more than three same-recipe points,
however cleverly ratioed, can deliver: none of those three outcomes can
actually distinguish genuine continuum convergence from a persistent
recipe-level artifact, because a recipe-level bias — by definition —
reproduces at every ratio drawn from the same formula, including this
one. Idealization 17 says this correctly in the small print; the
narrative sections should say it at the same volume, and Rank 2b's result
should be reported as necessary-but-insufficient evidence toward R15,
not as the addendum's discharge.

## Parameter change that would flip my verdict to support

Reword §1 and §5's Rank-2b framing to state explicitly, before any run,
that no Rank-2b outcome discharges R15's addendum on its own — that doing
so requires either (a) an independently-implemented discretization (not a
ratio substituted into the shared formula) or (b) a companion desk check
quantifying whether `cpl=45`'s own ~0.28% radius drift alone could
plausibly explain any observed sign difference, bounding rather than
avoiding the alias-breaking option MATERIALS actually asked for.
