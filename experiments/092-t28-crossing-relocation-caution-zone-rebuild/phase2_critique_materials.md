# PHASE 2 — CRITIQUE (MATERIALS & METAMATERIALS) · Panel Iteration 69 · exp-092

## Steel-man (≤150 words)

Rank 3 is a materially correct execution of the exact check my own
exp-091 self-review named. The `sigma_max_R3=1/3` derivation is right,
independently re-checkable from `lab/fdtd2d.py`'s update law: per-timestep
loss `alpha=sigma_e·S/(2·eps_r)` accumulated over a wave's `N`-cell
crossing (`N/S` timesteps) cancels `S` exactly, leaving depth
`∝ sigma_e×thickness(cells)` — and since `graded_black_shell`'s profile is
expressed in normalized depth `d∈[0,1]` (shape-preserved under R3, verified
in code), this holds for the *graded* profile too: `τ_true =
sigma_max·thickness_cells·K` for a fixed shape constant `K`, so the
`1/R3_RATIO` correction is scale-law-robust regardless of which exact
optical-depth formula one anchors to. The design also correctly proves
empty-leg reuse is bit-exact (no `build_article_r3` call on that path) and
adds 37.2° as a genuine negative control separating "sigma moves this
channel generically" from "sigma only matters near a node" — the right
discriminating design, not merely a cheap add-on.

## Sharpest attack (≤150 words)

Rank 1 spends 20 of 26 calls (77% of budget) relocating the crossings
using `sigma_max=0.5` — the exact construction whose validity on this
channel Rank 3 is built to test, run unsequenced with it rather than gated
by it. If Rank 3 finds the confound material on `delta_scene` (its own
§6 band explicitly calls this a genuinely open, two-sided question, not
disfavored in advance), Rank 1's entire 9-point curve — and the asymmetric,
outward-biased *net placement itself*, justified in §2a by a "lobe
widening" argument inferred from exp-091's own sigma=0.5 bracket data —
would need re-justification and likely re-running under the corrected
article, a third occurrence of this exact sub-thread's own named failure
("a systematically different, more strongly absorbing article... not a
resolution-matched rerun," T10/SIGMA_ON) — this time not accidental but a
disclosed, knowingly-deferred risk on 77% of the spend. Rank 3 only
re-tests exp-091's original three angles; none of Rank 1's five new points
are ever checked under corrected `sigma_max` this cycle.

## Verdict

**support-with-changes**

## Parameter change that would flip verdict

Sequence Rank 3 first (6 calls, cheap) as a gate: if it REFUTEs
(sign flip or ratio outside `[0.1,10]` in `delta_scene`), rerun Rank 1's
five new-angle points with `sigma_max=1/3` instead of `0.5` before
locating any crossing — same total call budget, reordered, closing the
gap where a materially wrong article could drive this cycle's own PRIMARY
crossing-location deliverable.
