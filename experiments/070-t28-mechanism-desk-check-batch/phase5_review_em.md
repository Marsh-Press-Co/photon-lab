# PHASE 5 — REVIEW · ELECTROMAGNETISM · Panel Iteration 47 (exp-070)

*Fresh sub-agent, ELECTROMAGNETISM charter (PANEL.md seat 3: field/wave
behavior, impedance matching, energy coupling; owns reciprocity/passivity/
causality bookkeeping). Blind to any other seat's Phase-5 review this
cycle. My own seat's exp-069 Phase-5 review is the origin of the
`ABSORB`-depth-tied candidate mechanism this cycle's item (a) was built to
test against — reviewed here on the merits, including where this cycle's
result cuts against it.*

## Verdict: PARTIAL

The batch is well-executed as instrument work: zero FDTD cost, a 10-item
mandatory-fix docket applied in full with no items dropped, a
null-permutation control that does real, demonstrated work (turns two
apparent sub-0.1%-deviation "hits" into correctly-scored NEITHERs), and I
independently re-ran `desk_check_mechanism.py` and reproduced
`results.json` **bit-for-bit** (diff clean). No fabrication, no rounding
games. Process discipline is real.

But P-070-1's CONFIRM — this cycle's only non-NEITHER, non-REFUTE
verdict, and the one load-bearing result carried into the Iteration-47/48
queue — is weaker than its own prose states, on a reading straight out of
my own seat's charter (field superposition). The batch does not, in fact,
cleanly establish "config-invariant" in the strong sense the Learned
section claims; it establishes something real but softer, and the
distinction matters for how queue item 2 should be framed, not just
whether it should run.

---

## 1. [LOAD-BEARING] P-070-1's CONFIRM does not test what "config-invariant" needs, and the numbers it produces are in tension with my own seat's founding same-frequency argument

**The result.** `P*_free(C40)=2.4361°` (R²=0.4327), `P*_free(C80)=2.5338°`
(R²=0.4337). Both land inside the 20% CONFIRM band measured *against
`P*_delta=2.8421°`* (14.29%, 10.85% deviation) — the gate Red Team's
Phase-2 audit specified after correctly killing the original bare-R²
design (Attack 1). I independently recomputed all four numbers from the
committed script; they reproduce exactly.

**What the CONFIRM band does not check.** The physically relevant claim
for "config-invariant" — a single length scale, shared by construction
between `C40`/`C80` (candidate: `R_OUT`=`W_OBJ`=78 cells, both configs),
producing one periodicity present identically in both raw curves — implies
`P*(C40) ≈ P*(C80)` **directly**, not merely that each separately falls
within a generous band of a third number (`P*_delta`, itself only a
single-cosine fit to the *difference* series, R²=0.627, not independently
established ground truth — Idealization 9 says as much). The design never
scores the direct comparison. I did:

```
|P*(C80) - P*(C40)| / mean = 3.93%
```

That is genuinely close — a real point in the CONFIRM reading's favor,
and I want to be honest about that; it is not scored anywhere in this
cycle's committed record, but it exists in the data and it is evidence
*for* a shared component. **The problem is the other half of the
picture, which the "genuinely lives in each config individually" language
in NOTES.md's Learned #1 glosses over**: both recovered periods sit
14.29%/10.85% away from `P*_delta` — the number that anchors the
CONFIRM band and, in items (b)/(d), is the number the whole named-constant
search is built around. Apply my own seat's exact argument from exp-069
Phase 5 (§1.1 there — reproduced verbatim by this batch's own Phase-1
narrative, §1): *a linear combination of sinusoids at the same frequency
is itself a sinusoid at that same frequency, regardless of relative
amplitude or phase.* If `C40(θ)` and `C80(θ)` truly share one
config-invariant periodic component at ~2.44–2.53°, that **same**
frequency has to appear in `delta(θ) = C80(θ) − C40(θ)` — not a
frequency measured 11–14% away. The founding T28 argument (bit-identical
`A=752` ⟹ the delta's 45%-off period is evidence of a second contributor)
and this cycle's own P-070-1 gate are the identical algebraic tool,
applied to two different pairs of curves — and it points in slightly
different directions each time: `A` bit-identical rules out "delta is just
reweighted T21 fringe"; a genuinely shared secondary component in `C40`/
`C80` should show up in `delta` at *its own* unshifted frequency, and by
that standard 2.84° vs. 2.44–2.53° is itself a non-trivial mismatch, not a
clean confirmation.

**The more likely reading, from a field-superposition standard**: `C40(θ)`
and `C80(θ)` are each raw curves already known (exp-066: settled fixed-
period `r²(c*)` up to 0.83) to be dominated by T21's own ~1.96° fringe. A
single free-period least-squares search over a 31-point/~3-cycle window
containing (at minimum) a strong ~1.96° component plus a weaker,
imperfectly-characterized second component will generically report a
**compromise frequency** between the two — not cleanly either. Both
`R²_free` values (0.43) are well below what a clean single dominant period
would produce (compare T21's own settled fixed-period fit, R²≈0.83) and
well above flat-null; `C40`/`C80` land 24–29% from T21's own 1.96° *and*
11–14% from `P*_delta` — consistent with exactly this compromise-fit
picture, not cleanly diagnostic of either hypothesis. My own Phase-2
critique this cycle flagged the raw-R² version of this exact confound
(Attack 1 in Red Team's language); the "recovered period" fix Red Team
adopted closes the *original* failure mode (CONFIRM-by-construction on
bare R²) but does not close *this* one, because it still scores against a
single reference number rather than checking self-consistency between the
two configs or separating T21's own strong component from whatever else is
there.

**Proposed fix (for the next cycle that touches this data, or a same-shift
addendum if capacity allows):** add an explicit sub-test scoring
`|P*(C40)−P*(C80)|/mean ≤ 10%` as a *second required conjunct* for
P-070-1 CONFIRM (currently unscored, though computable for free from data
already in `results.json`), and adopt my own Phase-2 critique's originally
-proposed, Red-Team-declined secondary variant — a two-term fixed(T21)
-plus-free model fit to each raw curve, scoring the free term's own R²
contribution after T21's known component is accounted for — before this
result is treated as settling anything about mechanism class. Until then,
**Learned #1's language should be softened**: "the ~2.8°-family signature
lives in each config individually" overstates what was shown; "each
config's raw curve carries periodic structure beyond T21's own fringe,
loosely consistent in location with `P*_delta` but not confirmed as the
same frequency by direct comparison" is the defensible claim.

## 2. Honest disclosure of the tension with my own seat's exp-069 finding — mostly yes, one gap

Phase 1 (§1) correctly and explicitly frames this batch as testing "a
competing, equally falsifiable candidate" against "EM's own framing," and
the CONFIRM/REFUTE table's REFUTE cell states plainly that a
difference-only signal "favors EM's ABSORB-tied framing instead." The
attribution trail is real and traceable, not buried — I do not find this
soft-pedaled at the sourcing level. **The one gap**: NOTES.md's own
Learned #1 and Next section state the result ("disfavors an
ABSORB-depth-tied mechanism") without naming it as cutting against my own
seat's own prior finding specifically — a reader who has not read
`phase1_proposal.md`'s §1 would not know this. Minor, cosmetic, easily
fixed (name the finding explicitly in Learned #1 next time this thread is
touched) — not load-bearing given Finding 1 already shows the "disfavors"
reading itself needs softening.

## 3. Beat-frequency algebra (item b) — sound in form, over-literal in application, correctly non-load-bearing

`1/P_beat = |1/P_a − 1/P_b|` is the standard envelope-period relation for
two added sinusoids of comparable amplitude and nearby frequency — the
algebra itself is not wrong. The looseness is in what gets fed into it:
`P*_delta` (a single-cosine least-squares fit to a ~6°-wide,
~2–3-apparent-cycle window, R²=0.627) is treated as if it were an
*empirically observed* beat/envelope period, when it is actually the best
single-frequency approximation to whatever multi-component signal is
really there. A genuine beat pattern needs several observed envelope
cycles to distinguish "real modulation" from "best single-frequency fit to
a short, noisy, multi-component series" — this window has neither the
span nor the resolving power to make that distinction, and Idealization 6
discloses the adjacent risk (non-additive mechanism) but not this
narrower one (the fitted period standing in for an observed one). This
does not change anything this cycle: P-070-2 lands NEITHER purely on the
null-permutation gate, correctly, regardless of whether the beat algebra's
literal identity holds. Flagged for any future cycle that leans on this
formula as a positive identification tool rather than a screening one.

## 4. Reciprocity / passivity / causality — no violation found

This batch is pure post-hoc arithmetic over already-gated FDTD output; it
makes no new physical claim about the engine. The mandatory disclosed
caveat (docket item 5) — a NAMED-constant numeric match is at least as
consistent with FDTD domain-construction bookkeeping (graded-loss
absorbing-boundary depth, taper length, guard clearances — not PML, per
VALIDATION.md) as with a physically real diffracting edge — is exactly
the right level of caution from a field-physics standard, and Attack 2's
executed null check (100% of random targets in-range clear the 1% band)
independently earns it. Nothing here strains passivity (`|r|≤1` throughout
a graded lossy boundary is unremarkable) or causality (this batch touches
no transient/settling question; that ground was covered by exp-069's own
P-069-4/5). No finding.

## 5. Independent reproduction

`python3 desk_check_mechanism.py` run fresh in a clean copy of this
directory; output diffed byte-for-byte against the committed
`results.json` — **identical**. All five P-070-N verdicts, all `null_p`
values, all tie-sets reproduce exactly.

---

## Ranked top-3 candidate directions, Iteration 48

**(1) Run EM's own C60/C70 `ABSORB`-depth falsification test (PLAN.md
queue item 2), and fold in a direct period-consistency check across all
four `ABSORB` depths (40/60/70/80), not just two more pairwise deltas.**
This is the correct next step precisely *because* Finding 1 shows P-070-1
does not cleanly settle config-invariant-vs-`ABSORB`-tied on its own — a
causal sweep (does the recovered period trend systematically with
`ABSORB` depth, or stay flat across all four?) is strictly more decisive
than any desk-arithmetic proxy, already-built at zero new `lab/` diff, and
directly resolves the ambiguity this review surfaces rather than requiring
another round of statistical re-litigation. Score it on recovered period,
not bare R² (Attack 1's own lesson, now doubly earned), and report
`P*(C40)`, `P*(C60)`, `P*(C70)`, `P*(C80)` against each other directly, not
only against a single derived reference.

**(2) The already-queued peak-cell R3 resolution recheck (θ≈37.2°/41.4°,
2 calls, near-zero marginal cost).** exp-069's own residual caveat — the
existing R3 check sits near `delta(θ)`'s zero-crossing, an order of
magnitude short of this program's own ~7% historical "survives resolution"
precedent — is still open and cheap to close before any further mechanism
claim leans on "T28 survives resolution."

**(3) `R_contact`'s `measured_direct` literature search** — unchanged
ranking from Iterations 46/47's own queue: zero FDTD cost, orthogonal to
T28 entirely, the only item across six cycles now that can move a real
sourced materials number (`REALIZABILITY_MEMO.md` Entry 3, TD-5's 7.8×
margin, still UNANSWERED).

Full record reviewed: `phase1_proposal.md`, `phase2_critique_em.md`,
`phase2_redteam_audit.md`, `phase3_synthesis.md`, `NOTES.md`,
`desk_check_mechanism.py`, `design_geometry.py`, `results.json`,
`phase4_results.md`; `experiments/069-t21-block-mini-period-match-power-up/
NOTES.md`, `phase4_results.md`, `phase5_review_em.md`.
