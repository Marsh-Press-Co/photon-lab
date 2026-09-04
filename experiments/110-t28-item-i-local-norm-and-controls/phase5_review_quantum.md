# PHASE 5 — REVIEW · QUANTUM OPTICS · Panel Iteration 87 (exp-110)

*Fresh context, blind to all other seats' Phase-5 output this cycle.
Charter: non-classical absorption / state-dependent or coherent
interactions; expressibility contract N/A this cycle (no σ(I)/σ(x,t)/
ε(ω)/gain mechanism anywhere in this document — confirmed structurally,
matching every governance cycle since Iteration 84). Special brief this
cycle: my own Phase-2 critique (`phase2_critique_quantum.md`) flagged
`classify_item_i_local`'s original single-realization
`max(mirror_floor(peccored), mirror_floor(hollow))` floor as a
correlated-not-independent point estimate; Red Team's Phase-2 audit
adopted this as Fix 1 (pooled median statistic). This review checks
whether the *actual implementation* of that fix is statistically sound
on the real, executed data — not merely present in the code.*

## 0. Scope and method

Re-derived, from source and from `results.json`'s own persisted raw
arrays, not trusted on NOTES.md's own reported numbers: (a)
`mirror_pooled_floor()`/`classify_item_i_local()`, line by line, plus an
independent from-scratch re-implementation cross-checked against both;
(b) item 2's four synthetic triples against the actual officially-executed
`linear_fit_control_output.json`; (c) a systematic scan of every
persisted `(r, margin)` cell for degenerate arithmetic (floor ≤ 0,
negative/non-finite SNR, resolved-mask/local_rel inconsistency), plus a
constructed synthetic edge case the real dataset does not happen to
exercise. All computation for this review is in throwaway scripts run
against the actual committed `run.py`/`results.json` in this session —
none of the figures below are hand-typed.

## 1. Task (a) — does Fix 1's pooled floor genuinely close my own
## Phase-2 concern?

**Yes, on the real data, bit-exact — independently re-verified two ways.**

Re-read `mirror_pooled_floor(pattern_48, percentile=50)`
(`run.py:288-307`): for `n=48`, forms 24 pairs
`|pattern[i]-pattern[47-i]|/2` for `i∈[0,23]` (an exact, non-overlapping
index-reversal partition — re-confirmed `n-1-i=47-i` covers all 24
distinct pairs with no self-pair, matching Red Team's own §1.1
re-derivation), and returns `np.percentile(pairs, 50)` — the **median of
24 pair-differences, computed once per pattern per margin**, not a
single per-bin draw. `classify_item_i_local` then takes
`floor = K * max(mirror_pooled_floor(peccored), mirror_pooled_floor(hollow))`
— the `max` now combines two **pooled** (24-sample) statistics, one per
physical scene, rather than two single correlated point-draws. This is
exactly Fix 1 as specified in `phase2_redteam_audit.md` §6 ("the median…
of `|pattern[i]-pattern[47-i]|/2` over the 24 within-margin bin-pairs,
computed once per pattern per margin, not re-drawn per bin").

Checked at 5 sample `(r, margin)` points — `(156,24)`, `(156,32)`,
`(156,48)`, `(312,32)`, `(312,65)` — spanning both r and both edge/interior
margins: for each, I (1) called the actual committed
`run.mirror_pooled_floor()`/`run.classify_item_i_local()` live against
the raw `results.json["r{r}"]["raw_patterns"][m]` arrays, and (2)
independently re-implemented the pairing+median arithmetic from scratch
(no call into `run.py` at all). All three of {persisted
`local_diag[m]`, live function call, from-scratch re-derivation} agree to
full float precision (`floor_peccored_pooled`, `floor_hollow_pooled`,
`floor`, the `resolved` boolean array, and `n_resolved`) at every sampled
point — zero mismatches. **R4 satisfied: the persisted floor genuinely is
what the committed pooling function computes, not a number that merely
looks plausible.**

Separately, re-derived the *statistical* claim underlying Fix 1 (not just
the arithmetic): built a synthetic 48-bin pattern with (i) only
odd/antisymmetric injected noise and (ii) only even/common-mode injected
noise (including a large uniform +5.0 offset applied to every bin) and
called the real `mirror_pooled_floor()` on each. Odd noise (std 0.01
injected) → floor reads `0.004369` (nonzero, tracks the injected scale).
Even noise (std 0.05 injected) and the +5.0 uniform offset → floor reads
**exactly `0.0`** in both cases. This independently confirms, from first
principles rather than by trusting Red Team's own algebra, that the
pooled floor genuinely: (1) is sensitive to the odd/antisymmetric
component at a scale set by real injected noise, and (2) is exactly,
not merely mostly, blind to any common-mode component, matching the
disclosed limitation verbatim.

**Conclusion on (a): Fix 1 is genuinely implemented, not merely present.**
It closes the specific concern my own Phase-2 critique raised
(correlated single-realization max) — `floor_p`/`floor_h` are now each a
24-sample pooled statistic rather than a single-bin draw, verified
bit-exact from the persisted arrays by two independent methods.

## 2. Task (b) — item 2's four triples against the officially executed
## output

**Confirmed bit-exact, independently, against the real executed
artifact.**

`linear_fit_control_output.json` (the file `linear_fit_control.py`
actually wrote on its official Phase-4 run) contains:
`P1=(True, 1.0, True)`, `P2=(True, 0.397147, True)`,
`P3=(False, 0.912047, True)`, `N1=(False, 0.096971, False)` — matching
NOTES.md's Predictions table to the stated precision.

I re-ran `linear_fit_control.py` fresh, cold, in this session (not
trusting the committed JSON on its own say-so): it reproduces
`is_monotonic`/`r_squared`/`residual_std`/`smooth` to full float
precision for all four cases, its own four internal assertions pass, and
`git status`/`git diff` on the rewritten `linear_fit_control_output.json`
show **zero diff** against the git-committed version — the fresh
recomputation is byte-identical to what is already on record, not merely
close.

Also checked the "byte-for-byte reused from exp-108/109" claim itself,
which item 2's control depends on for its own validity (a control that
tests a *different* function than the one actually used elsewhere would
be worthless): AST-compared `linear_fit_1_over_margin` between this
cycle's `run.py` and `experiments/108-.../run.py`, ignoring only the
docstring text — **AST-identical**. The function item 2 fault-injects is
genuinely the same function `classify_item_i`/`classify_item_ii` call.

**Conclusion on (b): CONFIRMED**, no gap found.

## 3. Task (c) — K=3/median/within-margin on real data: edge cases

**No edge-case defect fires on the actual executed data** — a full scan
of all 12 `(r, margin)` cells (576 bins total: 288 at r=156, 288 at
r=312) found:

- `floor` (and `floor_peccored_pooled`/`floor_hollow_pooled`
  individually) is strictly positive everywhere — range `2.346e-4` to
  `2.096e-3` across all 12 cells, nowhere near zero.
- Zero negative or non-finite `local_snr_peccored`/`local_snr_hollow`
  values anywhere.
- `local_rel` is `None` exactly where `resolved=False` and a finite
  non-negative float exactly where `resolved=True`, at every one of 576
  bins — no leakage either direction.
- Independently re-derived the `resolved` AND-gate
  (`|peccored|>=floor & |hollow|>=floor`) directly from the raw
  `raw_patterns` arrays and the persisted `floor` at all 12 cells — exact
  match to the persisted `resolved` array every time.
- Bin-count totals reproduce NOTES.md's own Result-prose figures exactly:
  425/576 RESOLVED overall (203/288 at r=156 = 70.5%, 222/288 at r=312 =
  77.1%), 151/576 UNRESOLVED (85 + 66) — matching `finalize.py`'s own
  computed percentages, not hand-typed, and matching what I get
  independently from the raw persisted arrays.
- The two PHOTONICS-named bins (`-146.25°` at r=156, `+168.75°` at
  r=312, margin=32) are both confirmed, independently, as
  `UNRESOLVED-BY-CONSTRUCTION` (`resolved=False`, `local_rel=None`),
  matching NOTES.md's claim exactly.

**But a genuine, reproducible construction-level gap exists, latent on
this cycle's own real data (does not fire here) — worth flagging, not
folding into this cycle's verdict.** `floor = K * max(floor_p, floor_h)`
is only ever guarded against `==0` on the `local_snr_*` computation
(`... if floor > 0 else np.full(..., np.inf)`); the `resolved` mask
itself has **no such guard**:

```python
resolved = (np.abs(pattern_peccored) >= floor) & (np.abs(pattern_hollow) >= floor)
```

If `floor` degenerates to exactly `0.0` — which my own §1 synthetic test
shows happens deterministically whenever a pattern's mirror-asymmetry is
*purely* common-mode/even (zero odd component) — `np.abs(x) >= 0.0` is
true for *every* real `x`, including `x=0` itself. I constructed a
minimal synthetic case (a perfectly mirror-symmetric 48-bin pattern,
`pattern[i]==pattern[47-i]` exactly) and called the real
`classify_item_i_local()` on it: `floor=0.0`, **`n_resolved=48/48`** (every
bin marked RESOLVED, including bin 0 where `pattern_peccored[0]=0`
exactly), and the `local_rel` computation for that bin divides `0/0`,
raising a `RuntimeWarning: invalid value encountered in divide` and
silently landing as `None` in the output (indistinguishable, from the
JSON alone, from a bin that was correctly gated `UNRESOLVED`). This is
not a hypothetical bug in the abstract — it is a direct, deterministic
consequence of the same "structurally blind to common-mode noise"
property the DISCLAIMER already names as a *bias* concern, but the
DISCLAIMER's own text ("a RESOLVED bin under this gate is cleared only
against the ODD/antisymmetric noise component, not validated clean of
common-mode contamination") does not capture this *sharper*
consequence: in the limiting/degenerate case of **purely** common-mode
contamination, the floor does not merely fail to validate cleanliness —
it collapses to zero and stops discriminating at all, silently passing
every bin, including a genuinely null one, as RESOLVED.

**Does not fire this cycle**: independently confirmed the real captured
data never approaches this regime (minimum floor across all 12 cells is
`2.346e-4`, roughly 3 orders of magnitude above zero) — item 1c/1d's own
reported bin counts and the two named bins' dispositions are unaffected.
This is a latent instrument gap, not a data-corrupting one, on par with
PHOTONICS'/QUANTUM's own Phase-2-flagged concerns about this same
first-use instrument (both already disclosed, both explicitly deferred
to Iteration 88 per R25's discipline) — not a fresh Checkpoint-firing
defect, since the instrument stays informational-only and no scored
verdict depends on it.

No other edge case found: `K*max(...)` can never be negative (built from
`abs()` throughout); the `n%2==0` assertion in `mirror_pooled_floor` is
currently trivially satisfied (48 is fixed) but is a real, undischarged
assumption if this function is ever reused on an odd-length pattern.

## 4. Steel-man of this cycle's own Combined Verdict (PROMISING)

The cycle earns real credit, independently reverified here, not merely
asserted: Fix 1's pooling is a genuine statistical improvement,
implemented correctly and reproducing bit-exact from primitives (§1);
item 2's fault-injection control is sound and its target function
verified to be the actual shared one (§2); the data-persistence gap that
made the Iteration-86 queue's own premise false is genuinely closed
(48/48 bins × 6 margins × both r, confirmed present); the two
PHOTONICS-named bins' dispositions are honestly reported in the
direction the data actually shows, not the direction that would have
looked more decisive; R23 compliance (`DISCLAIMER` in both text blocks)
is real, not merely claimed.

## 5. Sharpest attack

The instrument this cycle built to answer "is the ~10% local deviation
at two named bins real structure or noise" cannot answer that question
for those two bins with the confidence NOTES.md's Interpretation section
implies, for a reason distinct from the already-disclosed common-mode
bias: at real, executed floor values (`~2e-4`–`~2e-3`, far from zero),
the gate genuinely discriminates — but the SAME construction has a
literal, demonstrated failure point (floor→0, gate→vacuous) that the
disclosed common-mode-blindness language describes only in its milder
form ("not validated clean") rather than its sharper one ("stops
discriminating entirely, and would have silently marked a truly-zero
bin RESOLVED"). The Iteration-88 fault-injection control Idealizations
already queues a "(b) symmetric/common-mode perturbation, confirming the
floor correctly does NOT flag it" sub-item — as currently scoped, a
perturbation large enough to move `local_snr` without being large enough
to drive `floor` itself to exactly zero would NOT exercise this specific
degenerate branch. The queued control should explicitly include a
purely-symmetric (zero-odd-component) synthetic case as its own named
sub-case, not merely "a symmetric perturbation" in general.

## 6. Verdict on this cycle's Combined Verdict claim

**CONFIRM-WITH-GAPS.**

Not a clean CONFIRM: task (c) surfaces a real, independently-demonstrated
construction defect in the very instrument this cycle's own Fix 1 (my
own Phase-2 critique's remedy) produced — the `resolved` mask has no
`floor>0` guard, unlike its sibling `local_snr` computation two lines
away, and this is checkable, reproducible, and not merely theoretical (§3
constructs it directly against the real committed function). Not PARTIAL
and not a dispute: every falsifiable prediction in NOTES.md genuinely
held (tasks a/b are clean, zero mismatches, across every method I tried
to break them), the pooling fix is real and correctly implemented, R23
compliance is real, and the flagged gap is verified non-outcome-reversing
on this cycle's own actual data — the real floor never approaches zero at
any of the 12 captured cells. This is exactly the shape of finding this
program's "CONFIRM-WITH-GAPS" tier exists for: a genuine defect,
independently re-derived, that does not reverse this cycle's own reported
result but must not be silently absorbed into a clean CONFIRM either.

## 7. Ranked top-3 candidate directions, Iteration 88

1. **Extend the already-queued Iteration-88 fault-injection control
   (Idealizations sub-item (b)) to explicitly include a
   purely-symmetric/zero-odd-component synthetic pattern, and assert
   that `classify_item_i_local` either flags the degenerate
   `floor==0` case explicitly (a new status distinct from `RESOLVED`) or
   documents why silent pass-through is acceptable.** Directly closes
   this review's own §3 finding; zero new FDTD; the synthetic test
   harness for sub-item (a) (asymmetric injection) already needs to
   exist this cycle for the deferred queue item, so (b) is the same
   marginal cost. Highest priority because it is the one gap this review
   found that the currently-queued plan, as scoped, would not have
   caught.
2. **PHOTONICS' own deferred independent, non-differencing floor check
   (a `cpl`-refinement spot check) at the two named bins.** This is the
   only instrument on the table that can actually adjudicate the
   still-fully-open question this whole sub-thread exists to answer
   (real shape structure vs. noise at those two bins) — `classify_item_i_
   local`, even with Fix 1's pooling working correctly, is structurally
   incapable of ruling out a common-mode-masked real effect (§1, §5), so
   no amount of further work on the mirror-floor construction itself can
   close this; only an independently-constructed estimate can.
3. **`R2_SMOOTH_THRESHOLD=0.90` re-derivation** (queued since Iteration
   86 Tier 2b, still outstanding — exp-109's own Phase-5 QUANTUM review
   already flagged it as folded into a subordinate clause rather than
   its own line item). Item 2's control this cycle validated the OR-logic
   branch *mechanism* fires correctly at the existing threshold but never
   asked whether `0.90` is itself the statistically correct cutoff for
   `classify_item_ii`'s own R24-fix branch — the oldest single
   outstanding item in this exact sub-thread's own queue.
