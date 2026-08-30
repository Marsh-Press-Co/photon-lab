# PHASE 2 — CRITIQUE · Panel Iteration 70 · exp-093 · Seat: VISION SCIENCE

## Steel-man (≤150 words)

Item 5b's NETD framing is done right, not just asserted. `NETD_BAND_K=
(0.020, 0.050)` is not a bare literal here — it is the house constant sourced
at Iteration 20 (exp-043, `phase1_proposal.md`/Phase 4: 4 independent
microbolometer-NETD references, 8.6–100mK, `CONFIRMED`), the same band
Rank 3's own already-filed C-config values (`4.6×10⁻⁵`–`5.2×10⁻⁵` K) already
sit 374×–442× inside. Predicting the same UNDETECTABLE classification for the
14 backfilled G-config cells is a disciplined, falsifiable extrapolation from
an already-grounded threshold, not a new unsourced number. Idealization 3
("NETD is not a human-eye threshold... `REALIZABILITY_MEMO.md` is not
re-opened") is worded identically to exp-092's own text and correctly keeps
this instrument reading from being mistaken for a constraint-3 verdict. §13
individually checks all fifteen RULED OUT rules against this specific design
rather than asserting compliance — real disclosure discipline, the thing my
seat exists to police.

## Sharpest attack (≤150 words)

§1's narrative — the section most likely to be quoted later, per the
Iteration-65 CHECKPOINT's own stated worry — states THERMODYNAMICS' reading
of the upper window "for detectability: **nothing, either way**" (line 34)
and predicts the energy channel stays "smooth and undetectable regardless"
(line 41), with **zero inline qualifier at either point** that this is
NETD/instrument detectability, not constraint-3 human-eye detectability. The
disambiguating text (Idealization 3) sits ~470 lines later. This is the exact
disclaimer-erosion shape that fired Checkpoint criterion 4 four times in this
sub-thread (Iterations 53/63/64/65) and that Red Team's own Iteration-19
ruling named explicitly: "every claim needs its own disclaimer AT THE POINT
OF THE CLAIM." Compounding it: §10's mandatory carried-idealizations banner
cites only Idealizations 3/6/7/11 from exp-092 — silently omitting
Idealization 1 (2D TMz, single λ=600nm, no chromatic sweep), which literally
every one of this cycle's 56 new calls is subject to, and which a bare
"undetectable" claim needs precisely to stay scoped. The Result section
doesn't exist yet (Phase 1 only) — I cannot verify the banner is carried
there, so I name it as a **forward requirement**: Phase 3/4 must repeat this
exact banner, corrected, inline at every prose paragraph reporting item 5/5b,
not once at the top.

## Idealization-citation accuracy check (performed, not assumed)

I read exp-092's own `NOTES.md` Idealizations section directly (11 numbered
items) rather than trusting §10's citation. Idealizations 3, 6, 7, and 11 are
each quoted/adapted **accurately** — no mis-cited number, no altered
substance (11 is correctly re-mapped from Rank-3/Rank-1 language to this
cycle's item-3/item-1 numbering). That specific failure class (a wrong
idealization number or misquoted text) does **not** recur here. What does
recur is the *sibling* failure this exact idealization-8 lineage was built
to catch: exp-092's own Idealization 8 ("no full R3-rescaled rebuild of
exp-083's 31-point window... both remain open, separate, standing T28
items") was itself restored only after VISION caught it silently dropped
from exp-092's own `phase1_proposal.md` (Iteration 69, LOGBOOK). exp-093's
§10 does not carry Idealization 8 forward at all, even though §9 names the
identical still-open item ("Rank-2-in-exp-090's-own-queue unbiased
margin-vs-distance rebuild on the full 31-point window: still deferred,
unchanged") — the same fact, now split across two sections instead of
carried as a numbered, banner-governing idealization. Lower-severity than
the Idealization-1 omission above (it governs no *new* §11 prediction
directly), but it is the same drop shape recurring in the same numbered
lineage, and belongs in the fix list rather than left to a third catch.

## NETD_BAND_K sourcing

Not merely asserted — see steel-man. One minor, non-blocking gap: §11's
item-5b prediction cites `NETD_BAND_K=(0.020, 0.050)` with no inline pointer
to its Iteration-20/exp-043 origin, unlike the proposal's otherwise
consistent practice of citing sources for reused constants. Worth a one-line
fix, not load-bearing.

## Verdict: **support-with-changes**

The instrument work itself (item 5's backfill, item 3's localized sigma
check, item 1's resolution sweep) is sound and does not, on inspection,
smuggle in any undisclosed human-perceptual claim beyond the §1 language
above. Constraint 1/2/3/4 are genuinely untouched by the *mechanism* of this
proposal — only its *prose* leaks scope.

**Single change that would flip this to full support:** add an inline
`(NETD/instrument, not human-eye)` qualifier at both bare "detectability"/
"undetectable" occurrences in §1 (lines 34 and 41), and add Idealization 1
(2D TMz, single λ=600nm) to §10's "governed by Idealizations..." banner list
— fixing the point-of-claim gap Red Team's Iteration-19 rule requires,
before this proposal's own Phase 1 text is the thing a future cycle quotes.
