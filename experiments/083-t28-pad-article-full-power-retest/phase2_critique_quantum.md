# PHASE 2 — CRITIQUE (QUANTUM OPTICS, blind) · exp-083

**Independent re-verification performed, not asserted.** I wrote my own
from-scratch, fully vectorized reimplementation of `_free_period_search`/
`_fixed_period_fit` (batched normal-equations solve over the 400-point
`[1°,4°]` grid, `np.linalg.solve`, no code shared with `pad_round_trip_model.py`)
and ran it against `results.json`'s committed `delta_scene`/`thetas` arrays:

- **Fit reproduction: exact.** `R²=0.8581951251`, `P*=2.947368°` — matches
  the committed figures to the digit.
- **Null-permutation control: independently reconfirmed with a different
  RNG seed and a different code path** (20,000 trials, seed unrelated to
  the committed script's `seed=7`): `mean=0.1922, p95=0.3355, p99=0.4136,
  max=0.6665, count≥R²_obs=0/20000`. My own max (0.6665) differs from the
  committed run's max (0.6324) by an amount consistent with Monte Carlo
  noise at n=20,000 — both independently confirm **R²=0.858 exceeds every
  trial in a 20,000-draw pure-noise null**, on two separate implementations
  and RNG streams. The branch-B classification and its null-control claim
  hold up under independent re-derivation from primitives.

## A new, quantitative test from this charter's own angle: coherent superposition, not forced either/or

My predecessor seat's exp-082 review argued from first principles that a
real absorber sitting inside the echo's own path necessarily produces a
coherent cross-term (`|E_no-article+E_scattered|²` ⊃ `2·Re(E_no-article·
E_scattered*)`) — meaning BOTH the pre-existing PAD-tied term and a new
article-tied term should generally coexist in the scored signal, not
compete as mutually exclusive alternatives. This cycle's own primary test
is a single free-period search that necessarily reports one dominant `P*`
— by construction it cannot see a second, weaker component riding on top.
I tested this directly, using only already-committed data, zero new FDTD:

**A two-tone model — `delta_scene = c0 + a₁cos(ω_A x)+b₁sin(ω_A x) +
a₂cos(ω_C x)+b₂sin(ω_C x)`, both periods FIXED at the pre-registered
`P_edge_A=2.8421°` and `P_continuity=4.6113°` (no free search, so none of
R5's look-elsewhere concern applies) — fits dramatically better than either
single-tone model:**

```
single-tone, fixed at P_edge_A only:        R² = 0.8452  (3 params)
single-tone, fixed at P_continuity only:    R² = 0.2919  (3 params)
free-period single-tone (this cycle's PRIMARY):  R² = 0.8582  (P*=2.9474°)
two-tone, BOTH fixed periods simultaneously: R² = 0.9575  (5 params, n=31)
```

Adding the `P_continuity` tone on top of `P_edge_A` improves the fit far
beyond what 2 extra parameters explain by chance: F(2,26)=34.3, p=5.1×10⁻⁸.
The `P_continuity`-tone's own fitted amplitude is **43.6% of the
`P_edge_A`-tone's amplitude** — not a residual sliver. I ran the identical
20,000-trial null-permutation control on this exact two-tone construction
(same fixed periods, no free search): null mean=0.133, max=0.704,
**p=0/20000** — the improvement is not an artifact of adding degrees of
freedom to noise; it clears its own fresh null by the same wide margin the
primary test does.

**Reading:** the data support a genuine coherent superposition — a
dominant article-edge-diffraction component (amplitude-dominant, ~2.3× the
secondary term) PLUS a real, null-controlled, non-negligible
`PAD`-continuity component riding on it — more than they support a clean
either/or. This gives the `r=0.395` correlation (already flagged, correctly,
as an open tension in `NOTES.md`) quantitative teeth: it is not merely "in
some tension," it is exactly what a two-component signal with a
2.3:1 amplitude ratio between two moderately-separated periods, sampled at
n=31 over ~2 periods of the dominant term, would produce.

---

## Steel-man (148 words)

The three-branch discriminator is methodologically sound for what it is
built to answer — "which single established family dominates?" — and it
answers that question correctly and robustly: Branch B is not a
boundary call (3.7% deviation, an order of magnitude inside the 20%
tolerance; the other two bands miss by 36–50%), and its `R²=0.858` clears
a fresh, independently-reconfirmed-twice-over null-permutation control by
the full width of the null distribution, not a marginal p-value. The
pre-registration discipline is exemplary: the exact discriminating test
both hypotheses' own authors specified was pre-committed and run
unmodified. Treating `r=0.395`/`p=0.028` as disclosed-not-gating context
was the correct call given the multiple-comparisons caution honestly
stated alongside it — a single correlation number, run post-hoc, should
not override a pre-registered primary test. Nothing here is wrong; it is
answering a narrower question than its own prose sometimes implies.

## Sharpest attack (149 words)

`NOTES.md` states the mechanism-identity question "is resolved at full
power, decisively" and "identified with statistical confidence" — a clean
either/or outcome. My two-tone test shows this overclaims: a model
containing BOTH pre-registered periods simultaneously (no free search, own
null-controlled at p=0/20000) explains 11.3 more variance points than the
winning single-tone model, via an F-test at p=5×10⁻⁸, with the losing
period's own tone carrying 44% of the winning tone's amplitude — a real
second component, not noise. The three-branch discriminator is a forced
single-winner classifier by construction; it cannot express "both, at this
ratio" even when the data say exactly that. `NOTES.md`'s own "Next" section
names this test ("does a two-tone fit... explain more variance") but frames
it as an open future item rather than running it — despite being
zero-new-FDTD, reusing the already-committed `delta_scene` array, and
bearing directly on how strongly "decisively" earns its claim.

## Verdict: **support-with-changes**

The primary branch-B finding and its null-control are independently
re-verified here from primitives and stand as reported — Branch B genuinely
is the dominant component. What does not stand as reported is the framing
of this as a clean, complete resolution of the mechanism-identity question.
The two-tone result (above) shows a real, null-controlled, ~44%-amplitude
secondary component matching the `PAD`-continuity family survives
alongside the dominant article-edge term — a mixed-mechanism reality the
forced three-branch choice cannot express and the write-up's "decisively"/
"resolved" language does not disclose.

## Parameter change that would flip verdict to full support

Add the two-tone fit (both pre-registered periods, fixed, no free search —
exactly as computed above, zero new FDTD, reuses only committed data) as a
disclosed companion to the primary discriminator, and soften every
"resolves... decisively"/"identified with statistical confidence" sentence
in `NOTES.md`/`phase1_proposal.md` to state precisely what is and is not
established: Branch B dominates by amplitude and is the correct answer to
"which single family wins," but a real, null-controlled `PAD`-continuity
component (~44% relative amplitude) coexists and is not explained away by
that answer. With that correction, this cycle's actual measurements are
sound and I would move to full support.
