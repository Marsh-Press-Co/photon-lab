# PHASE 2 — CRITIQUE · MATERIALS & METAMATERIALS · Panel Iteration 47
## exp-070, Phase-1 proposal (lead: QUANTUM OPTICS) — T28 mechanism desk-check batch

**Seat charter:** sub-wavelength structure; what could physically realize
the proposed optical behavior; owns the realizability bound (published /
plausible / unobtainium-with-parameters).

---

## Steel-man (≤150 words)

The proposal is honest about what class of work it is doing: it declines
Checkpoint-criterion-2 candidacy outright, states T1 is N/A, and its own
Idealization 7 calls itself "a numerology-vs-mechanism discriminator, not
a mechanism proof" — the correct self-labeling for a search over already-
committed numbers. It is genuinely falsifiable (bands fixed before the
run, per house R4), reuses committed code (`_fixed_period_fit`/
`_free_period_search`) rather than re-deriving statistics, and item (a) is
a real discriminator — it can distinguish EM's `ABSORB`-tied hypothesis
from a geometry-invariant one before the named-constant search even runs.
Item (e)'s cross-check (do two independently-derived candidates, `A_alt`
and `A_eff`, name the same combination?) is stronger evidence than either
match alone. It correctly flags — not ignores — the `R_OUT`≡`W_OBJ`
degeneracy (Idealization 4) and distinguishes itself from R2's ruled-out
wavelength-resonance framing (Idealization 8). Cheap, and it satisfies the
Iteration-48 tripwire.

## Sharpest attack (≤150 words)

Every entry in `NAMED` (§3) — `A`, `PAD`, `ABSORB`, `TAPER`, `GUARD_OUT`,
`W_FLANK`, `D_SP`, `LEVER`, `clear_plane`, `clear_src`, `aperture_cells` —
is FDTD domain-construction bookkeeping (grid padding, absorbing-boundary
depth, taper length, window/guard geometry), not a material parameter.
Nothing in this batch is checked against ε(ω), σ, a layer thickness, or
any other quantity a real structure could instantiate — so no CONFIRM
here can bound realizability at all; MATERIALS' own charter has literally
nothing to grade. Worse: the search space is combinatorially enormous —
14 named terms × coefficients ±1..10 singly, plus 91 pairs × 20×20
coefficient combinations, is tens of thousands of candidate numbers — and
P-070-2/4/5's CONFIRM bar ("within 1% relative") has **no stated
false-positive-rate control**, unlike this very thread's own house
precedent (exp-069's 20,000-trial null-distribution test for `R²=0.63`).
A "CONFIRM" from a ransack this large is expected by chance, not evidence.
And even a controlled CONFIRM would show the ~2.84° period tracks this
bench's OWN `PAD`/`ABSORB`/`TAPER` construction — the textbook signature
of PML/absorbing-boundary reflection leakage VALIDATION.md already names
as a trust risk — which argues the signal is a numerical-scheme artifact
of THIS FDTD implementation, not a physically realizable diffraction
mechanism, the opposite of what the mechanism narrative's language
("diffracting sub-aperture," "physically distinct oscillatory
contributor") suggests to a reader skimming past Idealization 7.

## Verdict: support-with-changes

The batch should run — it is cheap, meets the Iteration-48 tripwire, and
item (a) alone is worth the desk time regardless of items (b)–(e). But it
should not ship as written on two points: (1) the write-up needs a
one-line framing note, stated in §1/§8 not buried in Idealization 7 —
*no outcome of this batch, CONFIRM or REFUTE, bears on realizability;
every candidate constant is simulator bookkeeping, and a match is at
least as consistent with a numerical-boundary artifact as with a
physical mechanism* — so Phase 5 and any future LOGBOOK citation cannot
read a P-070-2/4/5 CONFIRM as "T28 has a real geometric mechanism"
without that caveat attached. (2) the matching bands need an empirical
null-rate check before CONFIRM is treated as informative.

## Parameter change that would flip this to plain support

Add, to §5/§7, a permutation-null control on the `NAMED`-constant search
itself: run the identical single-term/pair search (§3 row 5) against
`N≥1000` random target values drawn uniformly over the same range the
real `A_alt`/`A_eff` values fall in, and report what fraction of random
targets ALSO land a ≤1%-relative match somewhere in the space. Require
the real match's rate to sit below, say, the 5th percentile of that null
before P-070-2/4/5 can be scored CONFIRM rather than merely "found." This
is the exact discipline exp-069 already applied to `R²=0.63` (20,000-trial
null test) — extending it here costs nothing (desk-only, reuses the same
search code) and directly neutralizes the ransack-space attack above.
