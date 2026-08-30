# exp-092 — T28 Crossing Relocation & Caution-Zone Rebuild

*Panel Iteration 69. Lead seat: ELECTROMAGNETISM. Runner: photonlab-shift
(cloud panel routine).*

## Hypothesis

exp-091 (Iteration 68) found that neither of its own ±0.2° `cpl=30`
brackets (40.2°/40.4° and 41.4°/41.6°) reproduces the known `cpl=20`
`delta_scene` zero-crossings (40.2654°, 41.4609°) — both windows read
same-signed at `cpl=30`, so the true crossings are outside both tested
windows, direction unknown from the tested points alone. exp-091's own
Phase-5 self-review (MATERIALS) separately found `build_article_r3` left
`graded_black_shell`'s `sigma_max` at its unscaled native default (`0.5`),
inflating the R3 article's accumulated optical depth ~1.5× relative to
native — checked and judged small on `p_abs_w` but never checked against
the PRIMARY `delta_scene`/`frac_contrast`/`ratio_k` channel. **Hypothesis,
genuinely two-sided, not a formality**: (1) a data-justified wider net
will locate both `cpl=30` crossings; (2) the unscaled `sigma_max` does
**not** materially contaminate the PRIMARY channel (a live, undecided
question — this cycle states no confident directional lean in advance).
This cycle also asks a third, purely desk-side question: what happens to
exp-090's own caution zone if 41.4° — which exp-091 found reclassifies
CONSISTENT at `cpl=30` — is dropped or relabeled in the `n=7` sample that
built it.

This cycle makes **no phenomenon-mechanism claim** — T1 escape route N/A,
Checkpoint criterion 2 N/A, matching every T28 desk/instrument cycle since
exp-069 (independently reconfirmed by Red Team, `phase2_redteam_audit.md`
§4, against the unbroken LOGBOOK record). It is pure instrument
recalibration.

## Setup

**Channel:** `PAIR_KEYS_R3=("C40_R3","G40_R3")` at `cpl=30`
(`R3_RATIO=1.5`, `experiments/069-t21-block-mini-period-match-power-up/
design_geometry.py`). λ=600nm throughout. No new `R3_CONFIGS` entry — both
configs already exist, added by exp-091.

**Three ranked items, run in ONE build, in the fixed order below (Red
Team's own mandatory resequencing, `phase2_redteam_audit.md` §2, Phase-3
synthesis §3 item 1) — 40 FDTD calls total:**

| Order | Block | Config(s) | Angles | `cpl` | `STEPS` | `sigma_max` | Calls |
|---|---|---|---|---|---|---|---|
| 1st | **Rank 3 — sigma_max PRIMARY-channel check** | C40_R3, G40_R3 | 37.2°, 40.2°, 41.4° | 30 | 4200 | 1/3 (article); N/A (empty, re-run fresh — see below) | 12 |
| 2nd | **Rank 1 — wider-net crossing search** | C40_R3, G40_R3 | 39.2°, 39.4°, 39.6°, 39.8°, 40.0°, 41.8°, 42.0° | 30 | 4200 | Rank 3's own verdict decides (see below) | 28 |
| — | **Rank 2 — caution-zone rebuild** | — (desk only, zero FDTD) | — | — | — | — | 0 |

Each (config, angle) cell above is 2 calls (empty + article legs).

**Why Rank 3's empty leg is 6 of its own 12 calls, not reused
(Director-level correction to `phase1_proposal.md` §4a, `phase3_synthesis.md`
§2):** `lab/ambient.py::contrast_from_runs` computes the article-leg
contrast `C` directly from the empty leg's own raw profile array (its
per-angle flank-mean normalization), not from the previously-computed
scalar `C_empty`. No T28-family experiment (exp-069 onward) persists raw
FDTD captures to disk — `results.json` carries only derived scalars — so
exp-091's own empty-leg captures are not retrievable from anything
committed to git. Rank 3's empty leg is therefore re-run fresh, inside
this script. Since `build_article_r3` (in any of its `sigma_max` variants)
is only ever invoked when `with_article=True`, the empty-leg field is
bit-independent of `sigma_max` — this re-run is a **deterministic
reproduction** of exp-091's own filed values, not new information, and
`run.py` asserts a bit-exact match against exp-091's own
`raw.r3_leg2_cpl30_steps4200::C_empty_c/C_empty_g` as a built-in
consistency check.

**Rank 3's branch rule for Rank 1's `sigma_max` (fixed here, before any
run — house discipline; a live, undisclosed choice at runtime is not
permitted):** Rank 3's verdict (see Predictions, R3) is computed from
`delta_scene`(ratio+sign) and `frac_contrast`(ratio) at all three census
angles, worst-case across six cells, using the identical
`ratio_sign_verdict` bands `phase1_proposal.md`/exp-091 §4(a) already
established (`[0.3,3.0]` CONFIRM / `[0.1,10]` REFUTE / else NEITHER).
- **CONFIRM** → Rank 1's article leg runs at `sigma_max=0.5` (exp-091's
  own as-filed convention).
- **REFUTE** → Rank 1's article leg runs at `sigma_max=1/3` (corrected).
- **NEITHER** → Rank 1's article leg runs at `sigma_max=1/3` (the
  conservative default — avoid this program's own T10/SIGMA_ON precedent
  of knowingly measuring with a systematically-too-strongly-absorbing
  article under genuine doubt), disclosed explicitly in the Result section
  as a NEITHER-triggered default, not a CONFIRM-level finding.

**Rank 1's angle set — seven points, all existing `DENSE_ANGLES` grid
members**: `{39.2°, 39.4°, 39.6°, 39.8°, 40.0°, 41.8°, 42.0°}`. The first
five (39.6°–40.0°, plus 41.8°/42.0°) bracket the naive linear-extrapolated
`cpl=30` crossing locations (≈40.04°/≈41.69°, re-derived from exp-091's own
already-collected bracket-pair slopes — see `phase1_proposal.md` §2a for
the arithmetic); the two added this synthesis, 39.2°/39.4°, extend the
lower net on PHOTONICS' own stronger, directly-measured basis: `delta_scene
(40.2°)` already flipped sign under `cpl` refinement by a magnitude
comparable to the *entire* `40.0°→40.2°` approach at `cpl=20`, direct
evidence the local curve near the lower crossing may have moved by more
than the 2-point secant alone estimates (`phase2_redteam_audit.md` §1.1,
elevated from discretionary to mandatory). Combined with the four
already-committed `cpl=30` points from exp-091 (40.2°, 40.4°, 41.4°,
41.6°), this gives two continuous, 0.2°-step `cpl=30` windows: `{39.2°,
39.4°, 39.6°, 39.8°, 40.0°, 40.2°, 40.4°}` (1.2° span) and `{41.4°, 41.6°,
41.8°, 42.0°}` (0.6° span).

**Disclosed limitation, unchanged from `phase1_proposal.md`**: 42.0° is
the literal edge of `DENSE_ANGLES`; if the upper crossing has moved past
it, this design cannot locate it (named forward, §Next, not resolved this
cycle — the optional settling-margin-motivated 42.0° double-`STEPS`
spot-check Red Team named as discretionary is declined this cycle on
budget grounds, `phase3_synthesis.md` §3 item 5).

**Cost** (hand-derived, `dg069._cost()` basis, `experiments/091-.../run.py`
per-call figures reused unmodified): 8073.0 CPU-s ≈ 134.6 CPU-min; wall ≈
39.5 min at 4 workers; 3× safety envelope ≈ 118.5 min. At the top of, but
inside, this sub-thread's own established ~100–150 CPU-min per-cycle band
(exp-091 itself: 125.6 CPU-min). Resequencing Rank 3 before Rank 1 changes
neither figure — CPU-time is additive regardless of execution order,
independently confirmed (`phase3_synthesis.md` §5).

**Applied unchanged:** `XI_TOL=0.12`, `NOISE_MULT=3.0`,
`RATIO_LOW/HIGH=0.1/10.0`, `FLOOR_FRAC=0.10`, `FLOOR=1.91744×10⁻⁴`
(applied unrecomputed against the new `cpl=30` numbers — a disclosed
mixed-resolution comparison, Idealization 6), `BOX_CLEARANCE_A/B_R3`,
`REF_HALF_H_R3` — all R3-scaled exactly as exp-091 established.

## Predictions (frozen, committed BEFORE any Phase-4 script runs)

**Carried idealizations banner (mandatory at both this section and the
future Result section, per the Iteration-65 CHECKPOINT's escalated,
non-discretionary rule): every prediction below is governed by
Idealizations 3/6/7/11 (§ below): NETD is not a human-eye threshold; this
cycle does not test constraint 1/2/3/4 or re-open `REALIZABILITY_MEMO.md`;
`FLOOR` is applied, not recomputed, against the new points; a Rank-3
REFUTE/NEITHER reopens Rank 1's own net-placement logic as provisional for
a future cycle, not merely licensing a different `sigma_max` for this
cycle's own 28 calls.**

**(R3) PRIMARY, runs FIRST, gates Rank 1's `sigma_max` — does the
sigma-corrected article move `delta_scene`/`frac_contrast` materially at
any of the three census angles?** Applying `ratio_sign_verdict`'s existing
`[0.3,3.0]`/`[0.1,10]` bands (a **repurposed, generic magnitude/sign
tolerance** — this is a material-parameter question, `sigma_max`
0.5→1/3 at fixed `cpl=30`, not the same kind of test as exp-091's own
resolution-rescale question the band was originally built for; stated
plainly per Red Team's RT-1) to `{sigma-corrected}/{as-filed exp-091}` at
each of `delta_scene` (sign+ratio) and `frac_contrast` (ratio) independently,
worst-case across all six (angle × quantity) cells: **CONFIRM** = all six
cells inside `[0.3,3.0]`, all `delta_scene` signs held. **REFUTE** = a
`delta_scene` sign flip at any angle, or any ratio outside `[0.1,10]`.
**NEITHER** = otherwise (some cell in `[0.1,0.3)`/`(3.0,10]`, no sign
flip). **No confident directional lean stated in advance** — this is a
genuinely open, two-sided question.

**(R3b) PRIMARY, non-gating — THERMODYNAMICS' co-equal energy-channel
check (zero marginal FDTD cost, byproduct of the same six article-leg
calls).** `p_abs_w` ratio `{sigma-corrected}/{as-filed}` at all three
angles: **CONFIRM** = ratio ∈ `[0.3,3.0]`, same sign of
`p_abs_w(G40_R3,θ)−p_abs_w(C40_R3,θ)`. **REFUTE** = sign flip or ratio
outside `[0.1,10]`. Directional lean (disclosed, not gating): a modest
*decrease* is expected, consistent with T9's established
`ratio_abs_ext≈0.51` near-saturation anchor (a 33% conductivity cut should
move an already-substantially-saturated absorber's `p_abs_w` sub-linearly,
not proportionally). `ratio_abs_ext_raw` reported disclosed, checked for
remaining within ~2–3% of the 0.51 anchor at all three angles — informational,
not scored against a CONFIRM/REFUTE band.

**(R1a) PRIMARY, runs SECOND, at the `sigma_max` R3 licenses — does the
wider net locate a genuine sign change in either window?** **CONFIRM** = a
sign change detected within the 7-point lower window (39.2°–40.4°)
AND/OR the 4-point upper window (41.4°–42.0°), with flanking same-signed
points confirming a single monotonic crossing. **REFUTE** = no sign
change anywhere in either extended window. **NEITHER** = a sign change is
found but the local curve is non-monotonic within the window (more than
one apparent crossing).

**(R1b) diagnostic, not gating** — report the interpolated crossing
location(s) where found, against both the naive extrapolation
(≈40.04°/≈41.69°) and the native `cpl=20` location (40.2654°/41.4609°),
signed shift magnitude at each. No pre-registered tolerance band — a
location report, not pass/fail.

**(R1c) diagnostic, not gating** — `ratio_k`/floor-gate classification at
all 7 new angles, using the existing unrecomputed `FLOOR`/`RATIO_HIGH=10`,
falls out of the same pipeline at zero marginal cost; reported as context.

**(R2) PRIMARY — Rank 2's own zero-FDTD recomputation reproduces the table
below (pre-verified independently five times over — by EM at Phase 1, by
QUANTUM OPTICS and Red Team at Phase 2, and by the Director twice, once at
Phase 2 review and once at Phase 3 synthesis — before this document was
frozen).** **CONFIRM** = every cell reproduces to ≥4 significant figures
when `run.py` recomputes it live from `experiments/090-.../run.py`'s own
functions. **REFUTE** = any disagreement — itself an important finding
(an implementation subtlety this proposal and five independent reviewers
all missed), to be investigated, not silently reconciled.

| Treatment | n | pos | AUC(margin) | zone `[lo,hi]` | inverted? | Firth `m₅₀` | naive MLE diverges? |
|---|---|---|---|---|---|---|---|
| ORIGINAL | 7 | 2 | 1.0000 | [1.4764, 2.1709] | No | 2.071013 | Yes |
| (i) DROP 41.4° | 6 | 1 | 1.0000 | [1.4764, 2.1709] (unchanged) | No | 1.818061 | Yes |
| (ii) RELABEL 41.4°→0 | 7 | 1 | 0.8333 | [1.4764, 1.3095] | **Yes** | 1.031717 | **No** (converges) |

**Empty-leg consistency check (zero-cost byproduct of Director fix #8,
`phase3_synthesis.md` §2):** Rank 3's freshly re-run empty legs at
37.2°/40.2°/41.4° (`cpl=30`, `STEPS=4200`) are asserted to reproduce
exp-091's own filed `C_empty(C40_R3,θ)`/`C_empty(G40_R3,θ)` bit-exact.
**CONFIRM** = exact match (float equality — deterministic FDTD, no
tolerance needed). **REFUTE** = any deviation — itself a significant,
unanticipated finding about this bench's own determinism, to be
investigated before trusting anything else this cycle measures.

## Idealizations

1. **2D TMz, single λ=600nm** — no chromatic sweep; the x-wall
   wavelength-generality leg remains separately queued, unchanged (now
   well past sixteen consecutive cycles deferred).
2. **Single article pair, `C40`/`G40`** (`PAIR_PAD`) — no claim about
   `C60`/`C70`/`C80` proper.
3. **NETD is not a human-eye threshold.** Nothing here bears on
   constraint-3/4's human-eye verdict; `REALIZABILITY_MEMO.md` is not
   re-opened or re-scored.
4. **Bench scale only** — same ≈2.34µm physical radius at native and R3
   resolution (the R3-scaling rule).
5. **`NOISE_MULT=3.0`, `FLOOR_FRAC=0.10`, `RATIO_LOW/HIGH=0.1/10.0`** —
   inherited house constants, unre-derived.
6. **`FLOOR`/`RMS[frac_contrast]` applied, not recomputed,** against the
   new points in both Rank 1 and Rank 3 — a disclosed mixed-resolution
   comparison.
7. **This cycle does not test constraints 1/2/3/4 and takes no T1
   escape-route position.**
8. **No full R3-rescaled rebuild of exp-083's 31-point window**, and no
   extension of R14(b)'s still-queued formal null-controlled period fit —
   both remain open, separate, standing T28 items (exp-091's own
   Idealization 8, restored here after `phase1_proposal.md`'s silent drop
   — VISION's Phase-2 finding, upheld by Red Team).
9. **The angles chosen (Rank 1's seven, Rank 3's three) were chosen for
   T28-census/crossing-bracketing relevance, not as a random or
   representative sample** of the dense window.
10. **No settling re-check at the new Rank-1 angles/legs.** `STEPS=4200`
    at `cpl=30` is argued clean from the *depth of convergence margin*
    exp-091's own `(c1)/(c2)` checks already established at 40.2°/41.4°
    (`10⁻⁷`–`10⁻⁴` relative deviation, six-plus orders of magnitude inside
    the `≤1%` bar) — not from a blanket claim that settling is
    never angle-dependent. **This program's own T27 record (Iterations
    42–45) shows settling residuals CAN be angle-dependent, sign-flipping
    even, at a severely under-settled `STEPS` count** (Red Team's RT-2,
    upheld) — the operative argument here is that the checked margin at
    `STEPS=4200` is so many orders of magnitude larger than any plausible
    angle-to-angle variation that it cannot plausibly be consumed by one,
    not that angle-dependence is structurally impossible. The optional
    42.0°-edge settling spot-check this reasoning would motivate as extra
    insurance is named forward, not run this cycle (budget, `phase3_
    synthesis.md` §3 item 5).
11. **A Rank-3 REFUTE or NEITHER-default reopens Rank 1's own §2a
    net-placement logic as provisional for a future cycle** — resequencing
    (item 1 of the mandatory-fix docket) fixes which article Rank 1's 28
    calls measure; it does not, by itself, revalidate whether the net's
    own location (derived from uncorrected-article bracket-slope data)
    is still correctly aimed under a corrected article. New this cycle
    (Red Team's own addition, `phase2_redteam_audit.md` §2).

## Result

**Carried idealizations banner** (mandatory at both this section and the
Predictions section, per the Iteration-65 CHECKPOINT's own escalated,
non-discretionary rule): every finding below is governed by
**Idealizations 3/6/7/11**: NETD is an instrument/detector threshold, not
a human perceptual one — nothing here bears on constraint-3/4's human-eye
verdict; this cycle does not test constraint 1/2/3/4 and takes no T1
escape-route position (`REALIZABILITY_MEMO.md` untouched, Checkpoint
criterion 2 N/A); `FLOOR`/`RMS[frac_contrast]` are applied, not recomputed,
against the new points; a Rank-3 REFUTE/NEITHER-default would have
reopened Rank 1's own net-placement logic as provisional — moot this
cycle, since Rank 3 CONFIRMed (see below).

All 40 FDTD calls completed (20.58 min wall — 7.58 min Rank 3, 13.01 min
Rank 1); all house gates PASS (`vac_pass`, `xi_pass`, `nonneg_pass`, all
exhaustively checked). The Director-added empty-leg consistency check
(Idealization/fix #8, `phase3_synthesis.md` §2) **ALL MATCH** — all six
freshly re-run empty-leg `C_empty` values reproduce exp-091's own filed
values bit-exact, confirming this bench's FDTD is deterministic as
assumed and validating the "re-run rather than reuse" fix.

- **(R3) PRIMARY — CONFIRM, cleanly, at all three census angles and both
  scored quantities.** The sigma-corrected (`1/3`) article's `delta_scene`
  ratio vs. exp-091's own as-filed (`0.5`) value: `0.9226`/`1.0141`/`1.1720`
  at 37.2°/40.2°/41.4°, sign held at all three; `frac_contrast` ratio:
  `0.9382`/`1.0267`/`1.1827` — all six cells comfortably inside `[0.3,3.0]`.
  **The unscaled `sigma_max` confound MATERIALS flagged at exp-091's own
  Phase-5 self-review does NOT materially contaminate the PRIMARY
  `delta_scene`/`frac_contrast` channel.** This is a genuine, clean
  resolution of exp-091's own single most consequential open question
  (`phase5_redteam_audit.md` §7: "on par with... the still-unlocated
  crossings") — the sign flip and razor-thin 40.2° survival exp-091
  reported are resolution-genuine, not a sigma-scaling artifact.
- **(R3b) PRIMARY, non-gating — CONFIRM.** `p_abs_w` ratio
  `0.9610`/`0.9619`/`0.9602` at the three angles — a clean, small,
  *consistent* ~3.8–4.0% decrease at every angle, matching THERMODYNAMICS'
  own pre-registered directional lean (a 33% conductivity cut moving an
  already-near-saturated absorber's `p_abs_w` sub-linearly, per the T9
  `ratio_abs_ext≈0.51` anchor) almost exactly. `ratio_abs_ext_raw` itself
  measured `0.5139`/`0.5127`/`0.5147` — within `0.54–0.93%` of the `0.51`
  anchor at all three angles, comfortably inside THERMODYNAMICS' own
  named `~2–3%` band.
- **[Sigma branch] CONFIRM → Rank 1 ran at `sigma_max=0.5`** (native,
  exp-091's own as-filed convention), the pre-registered branch outcome.
  Rank 1's own results below are therefore directly comparable to
  exp-091's own filed `cpl=20` data with no sigma-scaling caveat **at the
  three tested census angles (37.2°, 40.2°, 41.4°)**. Scope correction
  (Red Team's Phase-5 final audit, `phase5_redteam_audit.md`): none of
  the three sits inside the near-total interference null Rank 1 itself
  discovers below (nearest tested point, 41.4°, sits 0.38–0.44° from the
  upper double-crossing, where `delta_scene` reads an order of magnitude
  smaller than anywhere Rank 3 sampled) — the CONFIRM does not, on its
  own, extend to that specific region; see Learned item 3's own
  correction below.
- **(R1a) PRIMARY — NEITHER**, the pre-registered outcome for "a crossing
  found but the local curve is non-monotonic within a window" — and a
  genuinely split result underneath that one mechanical label, reported
  in full rather than flattened to it:
  - **Lower window — a clean success.** Exactly ONE crossing found,
    `theta=40.0718°`, a single monotonic sign change across all seven
    points (`-2.49e-3` at 39.2° rising smoothly to `+9.86e-4` at 40.4°,
    exp-091's own already-committed bracket point). Shift vs. the known
    `cpl=20` location (`40.2654°`): **`-0.1936°`** — a real, sizeable
    relocation, larger than either tested `cpl=30` bracket in exp-091 could
    have shown. Shift vs. the naive linear extrapolation this cycle's own
    Phase-1 design used to size the net (`≈40.04°`): only **`+0.0318°`** —
    the naive 2-point secant, despite PHOTONICS' own upheld objection that
    its amplitude-based corroboration was a non sequitur, turns out to have
    been a good *quantitative* predictor of the actual location, for
    whatever reason (not claimed as validated methodology, since n=1).
  - **Upper window — a new, more complex structure, not a located single
    crossing.** TWO crossings found, `41.7811°` and `41.8377°`, only
    `0.0566°` apart — the local curve crosses zero, comes back, and
    crosses again within one grid step's neighborhood, rather than making
    one clean transition. This coincides exactly with `theta=41.8°` itself
    reading `NODE-UNRESOLVABLE` (`floor_pass=False`, `delta_scene=
    -1.865e-5`, the smallest-magnitude value this cycle measured by nearly
    an order of magnitude) — the two located crossings straddle a genuine,
    near-total interference null, not sampling noise. **This is a new
    positive finding, not merely a failure to locate**: exp-091's own
    single-bracket instrument could not have shown this structure exists;
    this cycle's own denser net proves the upper crossing region is
    genuinely more complex than a single zero-crossing, at `cpl=30`,
    independent of whether either individual crossing's own location is
    itself considered "found" in the (R1a) sense.
- **(R1b) diagnostic** — both located crossings, against both comparators:

  | | `cpl=30` location | vs. known `cpl=20` | vs. naive extrapolation |
  |---|---|---|---|
  | Lower | 40.0718° | −0.1936° | +0.0318° |
  | Upper (first of two) | 41.7811° | +0.3202° | +0.0911° |
  | Upper (second of two) | 41.8377° | +0.3768° | +0.1477° |

  Both crossings moved in the *predicted directions* (lower → smaller θ,
  upper → larger θ) — the PHOTONICS-upheld "widening lobe" qualitative
  picture (Rank 1's own §2a) is directionally confirmed even though its
  amplitude-based corroboration was independently ruled a non sequitur;
  the *quantitative* naive-extrapolation estimates were good for the lower
  crossing and only fair (0.09–0.15° off) for the upper pair, unsurprising
  since the upper region's own true structure (two nearby crossings, not
  one) was never representable by a single-crossing 2-point secant model
  to begin with.
- **(R1c) diagnostic** — new floor-clearing classifications at the seven
  new angles: 39.2°/39.6°/39.8° CONSISTENT, 39.4° ENERGY-DECOUPLED
  (`ratio_k=0.0762`, the lowest value this cycle measured), 40.0°
  ENERGY-DOMINANT (`ratio_k=18.89`, floor-clearing), **41.8° AND 42.0°
  both NODE-UNRESOLVABLE** (`floor_pass=False` at both) — the floor gate
  correctly excludes the entire upper window's edge region, not only the
  41.8° point the double-crossing straddles; the whole `41.8°–42.0°`
  neighborhood reads small, node-proximate signal, consistent with §Result
  above's reading of a genuine near-total null there, not an isolated
  single-point artifact. No new claim is scored against these — context
  only, per the pre-registered design.
- **(R2) PRIMARY — CONFIRM, bit-exact.** The live in-`run.py` recomputation
  reproduces the five-times-independently-pre-verified frozen table
  exactly: `AUC=1.0/1.0/0.8333`, zone `[1.4764,2.1709]`(unchanged under
  DROP)/`[1.4764,1.3095]`(inverted under RELABEL), `m₅₀=2.071013/1.818061/
  1.031717`, naive-MLE-diverges `True/True/False`. This closes the loop on
  a deliverable that was, by the time of this run, arguably the
  best-verified single computation in this sub-thread's history (six
  independent reproductions across three cycles' worth of parties, this
  live run making a seventh).

**Reading the two Rank-1 crossing locations against exp-090's own caution
zone (context, not a re-litigation of R15 — that remains Iteration-70's
own named task, `phase3_synthesis.md` §6 unchanged):** now that the true
`cpl=30` lower-crossing location (`40.072°`) is known, the `cpl=20`
census point at `40.2°` sits `0.194°` past it (on the *positive* side, per
Rank 3's own reproduced sign), while `40.4°` sits `0.332°` past it —
consistent with `delta_scene(40.2°, cpl=30)` reading small-but-positive,
matching this cycle's own already-reported `+4.37e-4` value from Rank 3.
Full re-fitting of R15's own caution zone against these newly-located
crossings is out of scope this cycle (queued forward, §Next) — this
paragraph is a consistency note, not a new computation.

## Learned

1. **A genuinely open, two-sided instrument-validity question can resolve
   cleanly in the "not contaminated" direction** — Rank 3's CONFIRM across
   both `delta_scene`/`frac_contrast` and the co-equal `p_abs_w` channel,
   with `ratio_abs_ext` landing within ~1% of the T9 anchor at all three
   angles, is about as clean a negative result as this program's own
   `[0.3,3.0]` band has ever produced. exp-091's own headline sign flip
   and caution-zone-inverting finding stand *more* firmly for having
   survived this check, not merely unchallenged by it.
2. **A wider net can succeed and reveal new complexity in the same
   measurement.** The pre-registered CONFIRM/NEITHER/REFUTE trichotomy for
   (R1a) was built around "how many crossings did each window find," which
   correctly classifies this cycle's result as NEITHER — but that one label
   undersells a substantively split outcome (a clean single-crossing
   success in one window, a genuinely new double-crossing structure
   discovered in the other). Future crossing-search designs on this
   channel should consider scoring each window's own outcome separately
   from the start, rather than only a combined worst-case verdict.
3. **A double-crossing pair separated by 0.057° straddling a
   floor-gate-failing point is consistent with, but not yet independently
   confirmed as, a genuine two-node feature** — the three cited signals
   (two sign changes, and a `NODE-UNRESOLVABLE` classification at the
   point they straddle) are real and do point to the same underlying
   region (a near-total interference null at `cpl=30` near 41.8°), but
   all three are drawn from the same `floor_pass=False` neighborhood
   R13's own gate exists to flag as untrustworthy at a single resolution,
   not from independent, floor-clearing measurements — corroboration
   from inside the disputed region is weaker than the "not a numerical
   artifact" language originally here implied. **Corrected same-shift**
   (Red Team's Phase-5 final audit, `phase5_redteam_audit.md` §1;
   independently caught by PHOTONICS' blind Phase-5 review, which found
   this sentence directly contradicted the Next section's own admission
   (item 1 below, renumbered from item 2 — see the Next section's own
   note) that a denser check is still needed to distinguish a genuine
   two-node feature from an under-resolved single deep null): the same
   open question this Learned item now states plainly is answered, not
   begged, is exactly what Next item 1 (below) should resolve before any
   future caution-zone rebuild treats both crossings as independently
   settled inputs.
4. **This program's own `_run_sim_r3`-family FDTD calls are exactly
   deterministic across separate process invocations** — six independent
   bit-exact reproductions of exp-091's own filed empty-leg values,
   confirmed live in this cycle's own `run.py`, is now empirical
   confirmation (not merely an architectural assumption) that "re-run
   rather than persist" is a costless substitute for a raw-capture cache
   this program has never built.

## Next

Ranked, reconciling this cycle's own two live open items with the items
`phase1_proposal.md` §7 and `phase3_synthesis.md` explicitly deferred.
**Re-ordered same-shift** (Red Team's Phase-5 final audit,
`phase5_redteam_audit.md`, reconciling all six Phase-5 reviews' own
top-3s — PHOTONICS, ELECTROMAGNETISM, and QUANTUM OPTICS independently
converge on resolving the upper-window ambiguity before or alongside,
not after, the caution-zone re-fit): the original ordering below put the
re-fit first; every seat that ranked both items ranked the resolution
check no lower than co-equal with it, since a re-fit built on an
unresolved double-crossing input would risk exactly the failure mode
R15 itself exists to catch. The two items are re-numbered accordingly;
neither's own text is otherwise changed.

1. **A dedicated, denser sweep of the upper window (41.6°–42.2°, finer
   than the native 0.2° `DENSE_ANGLES` step)** to resolve whether the
   double-crossing pair at 41.78°/41.84° is a genuine two-node feature or
   an under-resolved single deep null — this cycle's own grid cannot
   distinguish those without off-grid points. **Elevated to Next item 1**
   (was item 2): the single most decisive, cheapest test of the exact
   ambiguity Learned item 3 (above) now discloses rather than resolves.
2. **Re-fit/re-derive R15's own caution-zone question using the two newly
   located `cpl=30` crossings** (or three, counting the upper pair
   separately) as inputs, now that Rank 3 has confirmed the sigma_max
   confound does not contaminate this reading — the natural next step
   given this cycle's own two PRIMARY results (R3 CONFIRM licenses citing
   Rank 1's numbers cleanly; Rank 1 locates the lower crossing and reveals
   the upper region's real structure). **Was Next item 1**: still the
   right next major step, but should run gated on, or at minimum report
   both a single-null and a two-node version of, item 1's own result —
   not silently pick one reading of the upper region.
3. **Extend the search past 42.0°** — this cycle's own §2b-disclosed
   window-edge risk was not realized for the *located* crossings (both
   fell inside the tested windows), but the newly-discovered upper
   complexity means the true picture past 42.0° remains unknown; still
   named, not resolved.
4. Carried forward, unchanged, standing: PHOTONICS' own grazing-incidence
   validity check (still the single most-repeated item on the whole T28
   board); the x-wall wavelength-generality leg (well past sixteen
   consecutive cycles deferred); the still-queued R14(b) formal
   null-controlled period fit; the Rank-2-in-exp-090's-own-queue unbiased
   margin-vs-distance rebuild on the full 31-point window; a `cpl=40`
   third resolution point (Tier 2, `phase1_proposal.md` §7); extending R3
   to exp-090's remaining four caution-zone points (Tier 3); the
   structural/governance items at Tier 4; the ritualization governance
   question (Iteration 61), still unresolved.
