# exp-083 — The full 31-point/0.2° `PAIR_PAD`-with-article re-test at 600nm (T28, Iteration 60)

**Panel Iteration 60.** Lead: **VISION SCIENCE** (by rotation). Executes
PLAN.md's Iteration-60 queue Tier 1 item 5 (`experiments/082-.../
phase5_redteam_audit.md` §10) — the near-unanimous single highest-value item
on the board.

## Hypothesis

exp-082 (Iteration 59) discharged PLAN.md's six-cycle tripwire on the
PAD-loaded real-article check at a disclosed, reduced-power 7-point/1°-step
window. Its primary amplitude-ratio metric (SURVIVES, `ratio=0.6573`) is
settled. But Red Team's own Phase-2 and Phase-5 audits proved, on four/five
independent lines of evidence, that the deeper mechanism-identity question —
whether the article-loaded channel carries the SAME lossless `PAD`-tied
phase mechanism (Iteration 53) or a qualitatively different,
article-mediated interaction — is UNRESOLVABLE at 7-point power. This cycle
runs the same harness at T28's own established full statistical power (31
points, 0.2° step, `[36°,42°]`) to resolve it, pre-registering PHOTONICS'
own two-branch-plus-null period discriminator (article-edge diffraction at
`4.611°` vs. the T21/T28-family `~1.96°–2.84°` vs. "neither established
family") as the primary test, bundling EM's own field-difference
decomposition (`ΔE_article=E_with−E_without`) as a zero-marginal-cost
companion instrument.

## Setup

`dg065.CONFIGS["C40"]`/`["G40"]` (`PAIR_PAD`), the established flagship
absorber (bit-identical to `exp-024`'s/`exp-082`'s `build_article()`), 31
angles (`dg069.DENSE_ANGLES`, `[36°,42°]`, 0.2° step — T28's own established
Block DENSE window), 600nm, STEPS=2800 (T28's own established settled
value). 125 FDTD calls (2 configs × 31 angles × 2 legs = 124, + 1
settling-precondition call). Full parameter table, T1 disposition (N/A), R6
disposition (does not apply, reasoned from first principles — §3b), and the
pre-registered three-branch band: `phase1_proposal.md` §1–5.

**Git-provenance discipline (this cycle's own critical, non-negotiable
instruction):** `phase1_proposal.md`, predictions only, committed and pushed
(`06cb96b`) strictly BEFORE `run.py` was written or any FDTD call executed —
restoring the standard flagged as a two-cycle-old tripwire (exp-081,
exp-082) at Iteration 59's own close. `run.py` and the in-progress run log
were committed separately, mid-run, as an explicit WIP checkpoint making no
claim about the outcome; this file and the final results are a further
separate, later commit.

## Result

**Reproduction precondition PASSED, bit-exact** (`max_dev=0.0` vs
`experiments/076-.../results.json::headline` at all 31 angles).

**PRIMARY: the three-branch period discriminator resolves to BRANCH B —
ARTICLE-EDGE DIFFRACTION, decisively.** `delta_scene(θ)`'s free period at
full power: `P*=2.9474°`, `R²=0.8582` — 3.7% from `P_edge_A=2.8421°` (T28's
own original `C80−C40` period), well inside the pre-registered 20%
tolerance; 36%/50% away from `P_continuity=4.611°` and `P_edge_B=1.9608°`
respectively. **A post-hoc, self-run 20,000-trial null-permutation control**
(not pre-registered, disclosed as such — zero new FDTD) shows the observed
`R²=0.858` exceeds the MAXIMUM achieved by 20,000 pure-noise permutations of
this exact data (`null_max=0.632`, `p=0.0`) — this result is not a
look-elsewhere artifact.

**EM's field-difference companion independently corroborates Branch B.**
The two single-config field-level decompositions (`ΔE_obj_article_C40`,
`ΔE_obj_article_G40`) are individually `R²`-inconclusive (`0.198`, `0.255`,
below the `0.30` floor) — disclosed, not swept aside. Their cross-config
PAIR (`ΔΔE_obj_article_PAD = G40−C40`, the field-level analog of
`delta_scene`, mirroring T28's own established practice of always scoring
`PAIR_PAD` as a difference) recovers `P*=2.5865°`, `R²=0.4582` — inside the
same `P_edge_A` band (`rel_dev=0.090`) — and its own fresh null-permutation
control also clears decisively (`p=0.00185`, `null_max=0.560`).

**Secondary (disclosed, not gating):** amplitude-ratio consistency check at
n=31 reproduces exp-082's own SURVIVES direction (`ratio=0.7243`, vs.
`0.6573` at n=7). `delta_empty`'s own free-period fit exactly reproduces
`P_continuity` — a harness-correctness identity (guaranteed by the
reproduction precondition), not new evidence. **`r(delta_scene,delta_empty)
@ n=31 = 0.3949, p=0.02806`** — a real, modest, nominally-significant
correlation, in some tension with the primary branch classification;
disclosed honestly with a multiple-comparisons caution (would not survive a
simple Bonferroni correction across this cycle's own headline-adjacent
tests) and a charter-neutral leakage explanation (two different-period
sinusoids over a short window are not fully orthogonal) — an open question,
not resolved by this cycle.

**Settling precondition (disclosed): `rel_dev=9.81×10⁻⁵`** — unchanged from
exp-082's own reading at the same cell, now at the full window's settled
step count.

Full numbers, self-scoring, and the complete null-permutation discussion:
`phase1_proposal.md` "PHASE 1 RESULTS" section (below its pre-registered
bands, appended after the run, never hand-typed — copied from
`results.json`/`run_output.txt`/`null_permutation_control.json`).

## Learned

1. **The mechanism-identity question exp-082 showed was unresolvable at
   7-point power is resolved at full (31-point) power, decisively, in favor
   of PHOTONICS' article-edge-diffraction hypothesis over QUANTUM's
   mechanism-continuity hypothesis** — not by increasing statistical power
   in the abstract, but by running the specific, pre-registered
   discriminating test both hypotheses' own authors specified and getting an
   unambiguous, null-controlled, doubly-instrument-corroborated answer. This
   is the first time in this nine-cycle-plus T28 sub-thread that the
   article-loaded channel's own dominant periodicity has been identified
   with statistical confidence.
2. **Two structurally different instruments — the established nonlinear
   Weber-contrast pair-fit and EM's new linear field-difference pair-fit —
   independently land in the same branch, each clearing its own fresh
   null-permutation control.** This is a materially stronger form of
   corroboration than either alone; EM's companion instrument (proposed at
   exp-082 Phase 5, run for the first time here) proved its own board-worthy
   value on its first use.
3. **A genuine, disclosed, unresolved tension remains**: the
   `delta_scene`/`delta_empty` correlation (`r=0.395, p=0.028` at n=31) is
   modest but real, and does not simply vanish now that the dominant period
   has been identified as belonging to a different family than
   `delta_empty`'s own established `4.611°` period. Whether this reflects
   genuine partial admixture of both mechanisms (idealization 7, disclosed
   in advance) or a leakage/short-window artifact between two
   moderately-different frequencies is not settled by this cycle.
4. **A pre-registered, inherited threshold (`R²≥0.30`) is not the same
   thing as a freshly-calibrated one** — this cycle's own post-hoc
   null-permutation control found the inherited floor sits close to the
   null distribution's own 90–95th percentile, only moderately
   conservative in isolation. The actual observed values (`R²=0.858`,
   `0.458`) cleared their own fresh null controls with wide margins, but
   the gap between "clears an inherited threshold" and "independently
   null-calibrated this cycle" is worth naming explicitly for any future
   cycle reusing this exact `R²≥0.30` gate.
5. **R6 (synthetic ground-truth recovery gate) correctly does not apply**,
   confirmed in hindsight: `delta_empty`'s own free-period fit at n=31
   recovered `P=4.611289746337977°` — the independently-known true value —
   exactly, to full float precision (a necessary consequence of the
   reproduction precondition, not fresh evidence, but a clean end-to-end
   confirmation that this exact machinery, at its native n=31 design power,
   performs precisely as required).

## Next

- **The genuinely open correlation tension (item 3, above)** — a natural
  Phase-2/5 follow-up: does a two-tone (superposition) fit of `delta_scene`
  against both `P_edge_A` and `P_continuity` simultaneously explain more
  variance than either alone, and if so, at what relative amplitude? Zero
  new FDTD, reuses this cycle's own committed `delta_scene` array.
- **PHOTONICS' own zero-FDTD desk pre-check** (`phase5_review_photonics.md`
  §2, not run this cycle): a coherent-sum construction treating the
  article's own two rim edges as a pair of secondary apertures
  (`y_wall_aperture_sum.py`'s own machinery, substituted with the article's
  edge coordinates) — an independent, mechanistic check of WHY Branch B's
  period sits where it does, not merely that it does.
- **The near-null σ(I) article follow-up** (`off_pass`, Tier 1 item 6,
  PLAN.md Iteration-60 queue) — does the confound's branch classification
  (and the correlation tension) change for a weakly-absorbing article?
- **QUANTUM's own lossless-PEC-only-disk control** (Tier 1 item 7) and the
  `PAIR_ABSORB40`/`C80−C40` extension (Tier 1 item 8) — neither re-tested
  this cycle, both still open board items.
- The x-wall wavelength-generality leg (750/450nm, Tier 2 item 9) — now
  SEVEN consecutive cycles deferred, and this cycle does not extend it
  (single-wavelength scope, disclosed idealization 1) — a Phase-5 Director
  action to state explicitly, not made in this pass.
