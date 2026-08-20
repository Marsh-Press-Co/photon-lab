# PHASE 2 — CRITIQUE (MATERIALS & METAMATERIALS) · Panel Iteration 28 · exp-051

*Blind critique. No other seat's current-cycle output read. All numbers below
were produced by invoking already-committed functions, never hand-typed (R4).
Scratch code: `/tmp/.../scratchpad/{offsets.py,score.py,anchor.py}`. This is a
Phase-2 pre-check in the exp-050 Red Team idiom, **not** a substitute for
Phase 4's own independent implementation.*

## Steel-man (≤150 words)

exp-050 left a real, narrow, cheap question, and this is the rare instrument
proposal whose citation hygiene is clean. I re-derived §2.1 from source rather
than trusting it: **all eighteen n\* values reproduce exactly** from
`experiments/050-.../results.json`'s `per_cell_summary_geom78` (7 tier-unstable
/ 11 tier-stable, exactly as claimed, including the 450/38 masked pair), and
**all nine `P(θ₀)` figures reproduce to four decimals** from
`λ_cells/(724·cos θ₀)`. After exp-048's and exp-049's non-reproducing headline
figures, an R4-clean anchor table is worth saying out loud. The design is
honest where it could have been slippery: an explicit `NOT_FOUND` diagnostic
instead of a silent drop, a bit-exact regression gate checked first, a
pre-registered way to lose, no `lab/` change, no tier claim, thirteen minutes.
And the object under audit — the GEOM78 desk propagator — is the one every
future near-boundary contamination citation rests on.

## Sharpest attack (≤150 words)

The crux is computable today, so I computed it. My §2.2a implementation
reproduces exp-042's committed `edge_diffraction_c_empty`/`_corrected`
**bit-exactly (relative error 0.0)** at all nine cells — it passes P-PCDP-0 —
and §2.2c's offsets then pre-refute the proposal. **P-PCDP-2's hard-
falsification clause already fires**: no threshold in [0.05, 0.40] reaches
sensitivity ≥5/7 *and* specificity ≥7/11 (t=0.30 → 2/7, 7/11; t=0.40 → 7/7,
5/11). `log₁₀(|C(81)|/ABS_TOL)` — the regressor Iteration-27's ranked #1
specifically demanded — is **at chance (AUC 0.52, better-signed direction)**;
`|offset|` alone gives 0.649. And the node story runs backwards: the three
smallest offsets (0.040, 0.098, 0.108) are two *stable*, one unstable, while
450/38 — the flagship shared-null cell — has **no zero crossing inside the
default ±0.6·P window in either convention**, reaching antinode
(|offset| ≈ 0.38) only after widening.

## Verdict

**Support-with-changes** — but the changes are not optional. As frozen, this
cycle's primary and fallback predictions both land REFUTED, and a REFUTED
reading here is *unattributable*: it cannot distinguish "phase offset does not
govern tier stability" from "the offset estimator is undefined at the very
cells the cycle exists to explain." A diagnostic that can only lose, and
whose loss teaches nothing, does not close either of exp-050's open questions —
and §1 claims it closes both.

### The measured table (my §2.2a/c pre-check, GEOM78, FWHM=20°)

Offsets from a 601-point ±0.6·P scan; stable to 7 digits against a 1601-point
rerun. `|C(81)|` from exp-050's own committed `beam_divergence_*`, n=81.

| cell (λ/θ₀) | conv | \|offset\| | \|C(81)\| | n\* |
|---|---|---|---|---|
| 450/36 | inc / corr | 0.4049 / 0.4193 | 5.90e-5 / 1.81e-4 | 41 / 41 |
| 450/38 | inc / corr | 0.3903\* / 0.3783\* | 2.25e-4 / 4.87e-5 | **81 / 81** |
| 450/40 | inc / corr | 0.3968 / 0.3830 | 1.09e-3 / 1.03e-3 | 41 / **81** |
| 600/36 | inc / corr | 0.3372 / 0.3198 | 2.31e-4 / 3.69e-4 | 41 / **81** |
| 600/38 | inc / corr | 0.0405 / 0.1084 | 6.11e-5 / 8.16e-5 | 41 / **81** |
| 600/40 | inc / corr | 0.1552 / 0.1294 | 8.73e-4 / 7.66e-4 | 41 / **81** |
| 750/36 | inc / corr | 0.4773 / 0.4768 | 3.88e-4 / 5.03e-4 | 41 / 41 |
| 750/38 | inc / corr | 0.1782 / 0.0979 | 1.13e-4 / 2.10e-4 | 41 / 41 |
| 750/40 | inc / corr | 0.4680 / 0.3334 | 7.22e-4 / 7.04e-4 | 41 / **81** |

\* `NOT_FOUND` at ±0.6·P; values are post-widening to 1.5·P. Note also that at
450/38 the two conventions' zeros sit **0.77·P apart**, directly contradicting
§1's own premise that they "zero-cross at nearly, but not exactly, the same θ"
(elsewhere that premise holds well — 0.017·P at 600/36).

### Second finding: the excluded third of the grid is the falsifying third

The task's ranked #1 says *"across the full FWHM=20° grid."* §2.1 drops
`coherent` (9 of 27 combinations) as outside "the incoherent-family." But
`beam_divergence_coherent` and `beam_divergence_incoherent` build their
per-angle field from **the identical** `_G_for_g(lam, gd, obliquity=True)` and
`_src_amp` (`experiments/050-.../design_geometry.py:123-153`) — so §2.2a's
single-angle fringe for `coherent` *is* `convention="incoherent"`, and its
`|offset|` is **identical by construction**. Yet at these same 9 cells
`coherent`'s n\* is 81,81,81,81,41,41,81,81,41 against `incoherent`'s
41,81,41,41,41,41,41,41,41 — **different labels at 5 of 9 cells at an
identical x1**. Those 9 combinations are precisely the data that tests whether
`|offset|` can govern anything at all, they cost ≈25% more runtime, and they
are the only ones excluded. Whatever the intent, the scope choice removes the
falsifier.

### Third: two counting slips, cheap to fix at Phase 3

- §2.3/§6 bill "9×3 = 27 (θ₀,λ) spot-check points ... × 2 conventions ≈ 54
  evaluations." The grid is 3 θ₀ × 3 λ = **9** cells × 2 conventions = **18**
  points; λ is double-counted. (I ran all 18 — see the anchor result above.)
- P-PCDP-5 scores "the 18 per-combination slope ratios," but §2.2e's ratio
  `|slope_corrected| / |slope_incoherent|` is defined **per cell**, so exactly
  **9** exist. An IQR-span test plus a node/antinode subgroup contrast on N=9
  (5 antinode / 4 near-node by my table) is thinner than idealization 6
  discloses.

### Realizability relevance — my charter's question, answered plainly

§3 says no `REALIZABILITY_MEMO.md` tier can move, and I confirm it — but the
sharper point is that **nothing else moves either, on either outcome**. The
entire phenomenon lives at `|C(81)|` = 4.9×10⁻⁵ – 1.1×10⁻³ (measured above):
**4.5–100× below `C_THR = 0.005`, and roughly 2–140× smaller than** T24's own
*uncharacterized, uncorrected* ABSORB systematic (0.002–0.007 absolute) on
this same channel, which idealization 10 scopes out. n=41's practical safety
at GEOM78 is already settled (exp-050 P-NCONV27-1, 100/108, CONFIRMED); the
residual is which side of a fixed tolerance line a near-null lands on, and
exp-050's own Phase 5 already ruled that a *coincidence*. That is legitimate
instrument work. It is not work that changes a single citation this program
has issued or plans to issue.

Which is why the queue position matters. Iteration 28 would be the **third
consecutive n-convergence-family desk cycle** (26, 27, 28) and the sixth
instrument/model-fidelity cycle in nine (20, 22, 23, 26, 27, 28). Ranked item
(4) — my own seat's fixed-absolute-thickness `graded_black_shell` variant —
stands at **10+ iterations deferred, now across three consecutive instrument
cycles**, and was "independently re-ranked again" at both Iteration 26 and 27.
That is verbatim the anti-pattern Red Team named at Iteration 26 when it
forced exp-049 to run ("a third consecutive deferral would repeat this
program's own named r=156 anti-pattern"). I am not asking Phase 3 to swap the
cycle. I am asking that exp-051's close carry an **unconditional
Iteration-29 trigger** for item (4), of the kind VISION's r=156 trigger
carried at Iteration 11 — not another re-ranking.

## The single change that would flip me to full support

**Score the predictor against the continuous target, not the binary tier
label.** Replace P-PCDP-1/2's `n*≠41` classification with a regression of
`Δabs(41→81) = |C(81) − C(41)|` — and of the per-cell convention ratio
`Δabs_corrected/Δabs_incoherent` — on the same two regressors. This is what
Iteration-26's own priority #3 actually specified ("score Δrel(41→81) against
a predictor including each cell's phase offset"), it is what the ~1.9–2.3×
asymmetry is a statement *about*, and it is immune to my attack: a binary
label that flips at **7 of these same 18 combinations** under a mere 3.87%
geometry change (exp-049's A=752 table vs exp-050's A=724 table, both
committed — I diffed them) is not a stable target for a classifier, whereas
the step magnitude is a real, fast-settling, 9-significant-figure quantity at
both geometries. Restore `coherent` at the same time and the cycle recovers
27 points, a genuine degenerate-x1 control, and a result that means something
in either direction.
