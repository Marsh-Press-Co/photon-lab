# PHASE 2 — CRITIQUE · VISION SCIENCE · Panel Iteration 55 (exp-078)

*Fresh sub-agent, blind to the other five seats' critiques this cycle.*

**Charter note, stated plainly per the task brief and this sub-thread's own
established precedent (exp-075's VISION critique):** T28 is instrument/
model-fidelity work — no absorber, no switch, no ambient scene, no
constraint-3 claim anywhere in this file (§2's own "T1 escape route: N/A").
My charter has no perceptual threshold to pin here. What follows is this
seat's other standing duty, sharpened specifically for this cycle by R9 —
my own seat's most recent finding (Iteration 54, exp-077): auditing
whether every number this proposal compares to another number is actually
the same *kind* of quantity, normalized the same way, before a
"confirmed" or "self-scored" comparison is trusted.

## R4 reproduction (independent)

Ran `python3 y_wall_prescreen.py` myself from the experiment directory.
Output is byte-identical to the committed `_output.txt`, and
`y_wall_prescreen_results.json` is unchanged after the rerun (clean git
diff). Every number cited in `phase1_proposal.md` §5 reproduces exactly:
`P*_model` = 3.2105°/3.1654°/3.2030° for `C80−C40`/`PAIR_PAD`/
`PAIR_ABSORB40`, `rel_dev` = 0.1296/0.3136/0.2330, R² = 0.1530/0.1331/
0.1493, all three "at boundary" flags `False`. No hand-typed number found.

## Commensurability audit (this cycle's specific duty)

- **`rel_dev` (period vs. period, §5.3/§5.4): commensurate.** Both
  operands are best-fit periods in degrees-of-θ, extracted by the
  identical imported `_free_period_search`/`_fixed_period_fit` off the
  real delta curve and the model's `cos(Δφ_self)` curve alike — same
  units, same algorithm, no cross-normalization. This is real R9-style
  discipline applied correctly, not the T16 mistake repeated.
- **R² (§5.3): legitimately comparable, but the *use* made of it is
  riskier than the number itself.** `_fixed_period_fit`'s R² is provably
  affine-invariant (`SS_res`/`SS_tot` both scale under `y→αy+β`), so
  scoring model-R²=0.13–0.15 against real-R²=0.63–0.82 as "fraction of
  variance one sinusoid explains" is a valid like-for-like statistic even
  though the underlying curves are physically different quantities (a
  measured ambient-contrast delta vs. an unweighted, unit-amplitude phase
  proxy, Idealization 2). But §5.3/§7 reason 3 then reads the *gap*
  between those two R² values as evidence the model's period match is
  noise-driven. That doesn't follow: model-R² also measures something
  structurally different — how sinusoidal `Δφ_self(θ)` is *by
  construction* (a sum of two `hypot()` distance terms plus `arg(r(θ))`,
  none linear in θ). A genuinely correct mechanism could show exactly
  this R² for that reason alone, unrelated to noise vs. signal. Two
  technically-true, correctly-computed R² values are cited in a way that
  invites one particular reading (spurious match) the comparison alone
  cannot settle — the same *shape* of framing risk R9 exists to catch,
  softer than T16's arithmetic-only miss because no unit is actually
  mismatched here, but present in how the number is used to argue.
- **`|r|` magnitudes across C40/C60/C70/C80/G40 (§5.2): commensurate as
  compared** — all five are the same `reflection_coefficient()` output at
  different `ABSORB` depths, same normalization. But see below: the
  *interpretation* attached to the small values is independently checked
  and found wrong, which is the load-bearing finding this cycle.

## Steel-man (≤150 words)

This proposal is genuinely disciplined about the commensurability rule R9
exists to enforce. `rel_dev` compares two periods (degrees), both
extracted by the identical `_free_period_search`/`_fixed_period_fit`
machinery applied to real and model curves alike — same units, same
algorithm, no cross-normalization. R² is provably affine-invariant
(least-squares sinusoid fit; `SS_res`/`SS_tot` scale identically under
`y→αy+β`), so scoring model-R²=0.13–0.15 against real-R²=0.63–0.82 as
"fraction of variance one sinusoid explains" is a legitimate like-for-like
statistic even though the two curves are physically different quantities.
`|r|` values compared across C40/C60/C70/C80/G40 are all the same
`reflection_coefficient()` output at different `ABSORB` depths — no
mismatch there either. Nothing here divides two differently-normalized
physical quantities and calls it a ratio, unlike T16's `amp_ratio`/`C_thr`
chain. R4-verified: reran the script myself, bit-identical to the
committed JSON/stdout.

## Sharpest attack (≤150 words)

§5.2/§7 discount `C80`'s contribution to two of three nominal SUPPORT
verdicts by calling `|r|≈10⁻⁴–10⁻⁵` (C60/C70/C80) "within an order of
magnitude of float noise in the underlying transfer-matrix recursion." I
independently recomputed `reflection_coefficient()` at `ABSORB`=60/70/80,
θ=39°, in 50-digit mpmath precision and diffed against the committed
double-precision values: relative deviation 1.6×10⁻¹²–6.1×10⁻¹² at all
three depths — these `|r|` values are resolved to ~12 significant
figures. The claim is not merely unverified, it is false: genuine float
noise here is ~10⁻¹² relative, twelve orders of magnitude below `|r|`
itself. The file's own inherited gates (G-LOSSLESS 2.2e-16, G-N1 1.4e-15)
never tested this deep-absorb, near-total-absorption regime, so nothing
in the committed record could have caught this. Correcting it removes one
of §7's three stated reasons for INCONCLUSIVE over SUPPORT — it doesn't
flip the verdict alone, but Phase 3 should not inherit this caveat
unexamined.

## Verdict: **support-with-changes**

The proposal's own headline discipline is real: it correctly resists
letting "2 of 3 raw comparisons clear SUPPORT" read as evidence, and every
number I checked against its own citation reproduces exactly. But the
INCONCLUSIVE self-score is built on three stacked reasons (§7), and I have
now independently disconfirmed one of them (the noise-floor claim) and
flagged a second as resting on an R²-comparison that proves less than its
own prose implies (the framing-risk point above). Neither correction
changes today's Test-A-only verdict on its own — reason 1 (`PAIR_PAD`
itself missing SUPPORT) stands untouched and is, by the proposal's own
honest admission, the load-bearing one. But Phase 3 should not carry
"C80 is near-noise-floor" or "low model-R² means the match is probably
spurious" forward as settled facts; both need the correction above before
either informs how much weight the 2-of-3 raw SUPPORT reading, or the
recommended null-permutation follow-up, actually deserves.

**What would flip this to outright SUPPORT:** nothing in this cycle's own
scope — Test B and a null-permutation control (both explicitly deferred,
§0/§6) are the actual gates on a real SUPPORT, and no amount of
commensurability auditing substitutes for either.

**What would flip this to OPPOSE:** if the R²-framing point above turned
out to be load-bearing rather than incidental — e.g., if a null-
permutation control (Phase 2's own recommended next step, §8 item 1)
showed the model's own low-R² period matches occur at chance rates over
this narrow window, which would mean the corrected `|r|` finding bought
back a comparison that a direct look-elsewhere check then kills anyway.
Nothing in the record suggests this yet; it is the next affordable check,
not a standing objection.

**Single parameter change that would flip my verdict:** none needed to
move this to plain SUPPORT (the missing Test B and null-permutation
control are structural, not a parameter), but the corrected noise-floor
finding above is itself the single check that most changes how much
weight the raw 2-of-3 period reading deserves — it should be folded into
`phase1_proposal.md` §5.2/§7 before this document is cited as this cycle's
settled record, the same standard R9 sets for any "confirmed" comparison
that turns out to rest on an unchecked premise.
