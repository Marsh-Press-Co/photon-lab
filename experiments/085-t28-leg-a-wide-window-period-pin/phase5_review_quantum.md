# PHASE 5 — REVIEW · QUANTUM OPTICS · Panel Iteration 62 · exp-085

*Fresh context, blind to any other seat's current-cycle Phase-5 review. Read
in full: PANEL.md; LOGBOOK.md in full (RULED OUT R1–R10, ESTABLISHED, LIVE
THREADS, the complete T28 arc, both Checkpoint entries, Iterations 58–61 in
full); the complete exp-085 record in order (`phase1_proposal.md`, all five
Phase-2 critiques, `phase2_redteam_audit.md`, `phase3_synthesis.md`,
`phase4_derivation.py`, `derivation_results.json`, `NOTES.md`).*

## 0. Scope check

§3/§0 of the record's own framing — T1 route N/A, Checkpoint criterion 2
N/A, zero realizability content — is correct and independently re-confirmed:
nothing in this cycle scores against any phenomenon constraint or fits a
material parameter. My seat's charter (non-classical/coherent interactions,
expressed only as effective classical parameters) is not directly engaged by
the physics either — this is a deterministic scalar-diffraction desk
exercise. My duty here, per this thread's own established convention (I
built the circular-shift null this exact function was first tested against,
exp-084) and per this cycle's assignment, is statistical: adjudicate whether
this cycle's central self-disclosed tension is read correctly.

## 1. Independent verification performed

- **Recomputed `frac_recovered` from the raw 37-window array, not accepted
  from the summary field.** `min(r2_local)=0.3540`, all 37 clear `≥0.30`,
  zero below. `frac_recovered=1.0` is arithmetically correct — the number
  itself is not in dispute; what it *means* is.
- **Fix 3 (`center_deg` bug) — traced in code, correctly implemented.**
  `phase4_derivation.py` computes `Tc_wrong = radians(p_star)·cos(39°)` then
  re-references `p_local_corrected = degrees(Tc_wrong / cos(radians(θc)))`
  per sub-window — exactly the correction Phase 3 specified. Methods A/B
  correctly keep `center_deg=39°` unchanged.
- **Fix 4 (4-band precedence) — traced in code, correctly implemented and
  MECE.** Disagreement-first, then narrow-window-undershot, then
  confirms-narrow, then catch-all — matches the frozen order exactly, and I
  re-checked by construction that the four conditions partition every
  reachable `(P_wide,P_fft,R²_wide)` triple (disagreement is the sole
  first-priority gate; among agreeing pairs, bands 2/3/4 are checked in
  order with 4 as an unconditional catch-all). **One undisclosed gap,
  non-load-bearing this run:** band 2's own "post-null" clause
  (`phase3_synthesis.md`, "only reported if Fix 1's circular-shift null also
  clears") never pins a numeric bar in the frozen spec; `phase4_derivation.py`
  invents `null_a["fraction_meet_or_exceed"] < 0.15` at implementation time.
  This did not matter this run (band 1/disagreement fired first,
  `rel_dev(P_wide,P_fft)=0.628` far past 0.10), but it is exactly the kind
  of un-pinned Phase-4 numeric choice R4's "predictions committed before the
  run" discipline exists to catch before it becomes load-bearing on a future
  cycle that actually reaches band 2.
- **Specificity control (R5) sanity-checked**: `n_clear=0/60` is a trivial
  consequence of `R²_wide=0.0128<0.30` gating every target in
  `specificity_sweep` — confirms the control is wired correctly, not an
  independent finding on its own.
- **Window-overlap geometry recomputed independently** (not addressed by
  either the record or any Phase-2 critique — see §3).

## 2. The central question: is "genuinely bimodal, not uniformly
   contaminated" statistically sound?

**No — not as stated, and a formal treatment sharpens this into a much
weaker claim than NOTES.md's prose conveys.**

Treating the 10 sampled sub-windows' pass/fail-at-40% outcomes as a small
binomial sample, under the natural null hypothesis **H0: every sub-window
is uniformly ~50%-contaminated, matching exp-084's own narrow-window
precedent exactly** (i.e., R10's original worry — a smooth deterministic
curve clears R²≥0.30 under reshuffling about half the time, everywhere, not
just in some windows):

- Exact two-sided binomial test, `k=4, n=10, p=0.5`: **p=0.754.** Nowhere
  close to rejecting H0. 4/10 is close to the single most probable outcome
  a fair-coin-like 50%-contamination process would produce at n=10
  (mode is 5/10).
- Clopper-Pearson 95% CI for the true per-window contamination rate, given
  4/10: **[0.122, 0.738].** This interval comfortably contains both
  "uniformly ~50% contaminated" (matching R10's own worked precedent
  exactly) and "mostly clean" — the data cannot distinguish them.
- Power check: even if the *true* rate were as extreme as 20% or 80% (a
  large, substantively meaningful deviation from uniform 50%), n=10 has
  only **37.6% power** to detect that as significantly different from 0.5
  at α=0.05. This design could not reliably tell "mostly-real" from
  "mostly-contaminated" even if the underlying truth were that lopsided.

**The "40% at Fix 2's own trigger threshold, exactly" framing in NOTES.md
should be read as a coincidence of a coarse count landing on a round
number, not as a precision result** — 4/10 and 5/10 and 3/10 are all
statistically indistinguishable at this sample size.

The visual "gap" in the raw values (nothing between 0.167 and 0.600 across
the 10) is the more interesting piece of the NOTES.md argument, but it is
not rescued by a larger sample size argument either: gaps of this width are
unremarkable order-statistics behavior for only 10 draws from almost any
smooth, non-degenerate underlying distribution — observing *no* mass near
0.5 (the value pure per-window noise would be expected to cluster around,
since a genuinely non-periodic segment's own best fit and its reshuffled
copies are drawn from a similar process) is mildly suggestive of two
regimes, but "mildly suggestive from 10 points" and "genuinely bimodal" are
different epistemic weights, and no dip-test or mixture-model comparison
was run to tell them apart.

**Verdict on the specific claim: NOTES.md overstates what this sample
establishes.** The correct, disciplined statement is: *the sampled null
check is consistent with a partially-real, partially-contaminated pattern,
but is also fully consistent with uniform ~40–50% contamination
matching R10's own precedent — the sample is underpowered to distinguish
these, and `frac_recovered=1.0` should be read as an upper bound on real
local periodicity, not a count of 37 independently confirmed findings.*
This is precisely the R10 failure mode (specificity/pass-rate readings
substituting for a null-under-noise test) recurring one level down — this
cycle correctly *ran* the mandatory null (crediting Fix 2), but then
under-read what a 10-sample binomial count can support, at the exact moment
its own headline finding depended on the answer.

## 3. A genuinely new finding: the 37 sub-windows are not independent, and
   ρ's p-value is computed as if they were

Not caught by any of the five Phase-2 critiques, Red Team's audit, Phase 3,
or NOTES.md. Method C's sub-windows step by `θc: 2°` but are each `6°` wide
(`±3°`) — **adjacent windows overlap by 4° of their 6° span, 66.7%.**
Windows only become genuinely independent at spacing `≥6°`, i.e. roughly
every 3rd sample — **the effective independent sample size across the
72°-wide domain is closer to ~12, not 37.**

The reported `ρ=0.8817, p=5.76×10⁻¹³` is a Spearman test computed as if the
37 `(θc, P_local)` pairs were independent observations. They are not — each
adjacent pair shares most of its own underlying data and its own local fit.
This does not mean the trend is spurious (visually and physically it is a
strong, monotone-looking pattern, and the underlying mechanism — a
Fresnel-zone chirp whose local period should vary smoothly and coherently
with angle — gives a real reason to expect exactly this kind of smooth
trend) — but the stated p-value is not a valid measure of how surprising
that trend is under a "no coherent trend" null, because 66.7%-overlapping
windows cannot supply 37 independent pieces of evidence. A defensible fix:
recompute ρ (and, ideally, a permutation-based significance level, since
this is the same deterministic-curve territory R10 governs) using only the
~12 non-overlapping windows, or apply a block/moving-window correction to
the effective sample size before citing any p-value as evidence. The
qualitative trend likely survives this correction given how monotone it
looks by eye across all 37 points — but "likely survives, not yet checked"
is a different, weaker claim than the one currently in the record.

## 4. Steel-man

This is a well-executed instance of this program's own hard-won discipline
working as designed. Five independent blind critiques and Red Team's audit
all independently caught the identical defect (R10 misapplied as a skip-the-
null exemption) from four different angles — a textbook demonstration that
independent review catches what a single fresh context, however careful,
would plausibly have missed. The `center_deg=39°` hardcode bug (EM's find,
independently reproduced twice) is a real, subtle, cheaply-fixed defect that
would have silently corrupted every Method C trend reading had it shipped
uncorrected. Both MECE gaps (QUANTUM's overlap/gap counterexamples, VISION's
missing strong-chirp cell) were independently reproduced from scratch by Red
Team and closed cleanly in Phase 3, with a documented, ordered decision
procedure rather than post-hoc adjudication. The cycle's own honest
disclosure of the Fix-2/Fix-5 collision (STRONG COHERENT CHIRP reported
un-downgraded despite tripping the reliability flag) — stated plainly in
the run's own printed output and NOTES.md, not smoothed over — is exactly
the "disclosed, not silently patched" standard this program holds itself
to, and it correctly deferred the resolution to Phase 5 rather than
improvising an answer under time pressure. R4/R9 discipline (every cited
number traced to a committed source, re-derived independently by at least
three parties across this record) is airtight throughout.

## 5. Sharpest critique

The cycle's own resolution of its central tension is not yet earned. NOTES.md
reaches for a specific, load-bearing characterization — "genuinely bimodal,
not uniformly contaminated" — from a sample of 10 binary outcomes that a
five-minute binomial calculation shows cannot support that level of
confidence (p=0.754 against uniform-50%-contamination; 95% CI spanning
12%–74%). This is not a minor rounding slip; it is the same shape of error
R9 was adopted to catch (an operation performed correctly — the count is
right, 4/10 — on operands that don't license the conclusion drawn from
them), now applied to a statistical-power question instead of a
unit-commensurability one. Compounding it: the headline positive finding's
own significance figure (`ρ`'s `p=5.8×10⁻¹³`) is computed over 37 points
that are ~67% pairwise overlapping and therefore worth roughly a third of
that as independent evidence — nobody in five blind critiques or Red Team's
audit checked this, because everyone's attention (correctly, given R10) was
on the R²-threshold self-similarity question, not on whether the
*sub-windows themselves* supply independent samples for the trend test
built on top of them.

## Verdict: **PARTIAL** — not ruled out, not promising

Matches this T28 desk-cycle sub-thread's own standing disposition
(Checkpoint criterion 2 N/A, instrument-fidelity work). Substantively, two
things are now real and cheap to state plainly: (1) **scenario (i) — a
single dominant global tone — is decisively excluded at the wide-window
scale**, independently by two instruments (Method A's `R²_wide` collapses
from the narrow window's 0.37 to 0.013, indistinguishable from its own
circular-shift null at 45.4%; Method B's FFT finds no sharp peak in-range
and its true global maximum sits at 140°, essentially DC). This is a solid,
already-fully-verified negative result. (2) **Scenario (ii) — a genuine,
coherent chirp — is directionally supported but not yet properly certified**:
the trend is real-looking and physically motivated, but its two supporting
numbers (`frac_recovered=1.0`'s implied "all real," and ρ's `p=5.8×10⁻¹³`)
are each less certain than stated once the sampling that produced them is
examined formally — the first because n=10 cannot resolve bimodal-vs-uniform,
the second because 37 non-independent points were scored as if independent.
Neither defect reverses the finding; both mean it is currently *asserted*
with more confidence than the record's own numbers can support.

## Ranked top-3 candidate next directions (Iteration 63)

1. **Properly power the reliability question, then resolve the Fix-2/Fix-5
   classification collision with the answer, not with narrative.** Extend
   the circular-shift null to all 37 sub-windows (already shown cheap by
   this cycle's own timing — ~1 additional minute), and correct the
   `ρ`/trend significance test for the ~67% pairwise window overlap (use
   only the ~12 non-overlapping windows, or a block-permutation null on the
   full 37-window curve) before any STRONG COHERENT CHIRP / DRIFTING verdict
   is filed as settled. This directly answers the question this cycle's own
   design left open, with power instead of a 10-point anecdote, and closes
   the un-downgraded-classification contradiction NOTES.md itself flagged as
   "Phase 5's first job."
2. **Log the wide-window global-null-tone exclusion as a standing T28
   boundary result**, independent of how (1) resolves — both global
   instruments (A, B) collapsing to noise-floor over a 13×-wider, 10×-denser
   domain is a real, already-computed, already-verified finding worth
   carrying into the permanent record now, not gated behind the chirp
   question.
3. **Pin a disclosure norm for small-sample null-check designs**, in the
   R9/R10 lineage: when a mandatory null test is run on only a *sample* of
   sub-instances (as Fix 2 did here), the write-up must state the sample's
   own statistical power/CI for the claim it is being used to support (a
   binomial CI, here) at the same time the pass/fail count is reported —
   not as a follow-up correction. This is the precise gap that let a
   coincidental "exactly at the 40% trigger" count get narrated as "genuine
   bimodality" before anyone ran the five-minute calculation showing it
   couldn't support that reading.
