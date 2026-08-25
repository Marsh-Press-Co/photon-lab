# PHASE 2 — RED TEAM AUDIT · Panel Iteration 47 · exp-070 (T28 mechanism desk-check batch)

*Fresh sub-agent, RED TEAM charter (PANEL.md seat 7). Receives the Phase-1
proposal AND all five blind Phase-2 critiques, per PANEL.md's independence
mechanics. Goes last. Standard for this cycle (per the Director's framing,
matching exp-069's own precedent for a non-mechanism cycle): NOT
textbook-physics compliance — internal consistency, falsifiability,
expressibility as simulation parameters, and program-integrity discipline
(R4 hand-typed-figure rule, the Checkpoint-4 PARTIAL-escape-hatch history,
this program's own null/permutation-control precedent for look-elsewhere
risk — R5's AUC ruling, T28's own 20,000-trial null test). Tag set this
cycle: `[inconsistency | unfalsifiable | inexpressible | program-integrity]`
— `constraint-#N` is N/A, as it was for exp-069.*

## 0. Framing — what is actually at stake this cycle

This is PLAN.md's Iteration-47 queue item 1, itself Red Team's own
standing forward tripwire from exp-069's Phase-5 final audit: T28's
unexplained ~2.84° `C80−C40` periodicity must receive "at least one cheap,
desk-only first move" by Iteration 48's close, or the gap becomes
Checkpoint-4-adjacent on its own. The batch is zero-FDTD-cost desk
arithmetic over already-committed data (`exp-069/results.json`,
`exp-065/design_geometry.py`) — nothing here can break trust-suite gates
or touch `lab/` engine code. The stakes are entirely about scoring
discipline: whether the CONFIRM/REFUTE bands this batch commits to git
actually measure what they claim to, given this program's own hard-won
lessons about look-elsewhere risk (R5, T28's own founding fit) and
escape-hatch reporting (Checkpoint-4, exp-069's Attack 4).

All five seats verdict `support-with-changes`; none opposes. This audit's
job is to determine whether "changes" is a euphemism doing too much work.
**Independent computation below shows it is worse than any of the five
critiques characterizes it, on both of its two live risk points (items a
and b/d/e) — not merely "likely" broken, but demonstrably broken, on the
actual committed data, run through the actual proposed logic.**

## 1. Numbered attacks

**Attack 1 — [inconsistency] Item (a)'s discriminator does not merely risk
a false CONFIRM (EM's framing) — it CONFIRMS, on the real committed data,
via a third, unexplained period matching neither hypothesis.** EM's attack
argued this "will almost certainly fire." I ran the proposal's own
literal method (`_free_period_search`, identical grid `P*∈[1.0°,4.0°]`,
400 points, `center_deg=39.0`, imported unmodified from
`exp-069/run.py`) against the real `block_dense.rows` `C_empty_C40(θ)`
and `C_empty_C80(θ)` series (31 points, already committed):

```
R²_free(C40) = 0.4327  at P* = 2.4361°
R²_free(C80) = 0.4337  at P* = 2.5338°
```

Both clear the §5 CONFIRM bar (`R²≥0.30` for both) by a wide margin —
under the pass/fail logic exactly as specified in §7 (`p1: confirm =
r2_free_c40>=0.30 and r2_free_c80>=0.30`), P-070-1 CONFIRMS today,
mechanically, with no further FDTD spend. This is strictly worse than EM
characterized: the recovered periods (2.44°, 2.53°) match **neither**
T21's own 1.96° fringe **nor** the delta's own 2.84° free-fit — a third,
unaccounted-for value, on the raw individual curves. §5's prose reads a
P-070-1 CONFIRM as "the ~2.8°-family signature already lives in `C40(θ)`
and/or `C80(θ)` alone" — but the actual recovered period is 11-16% off
2.84°, no closer to that hypothesis than to T21's own. As currently
scored, item (a) will report CONFIRM regardless of which (if either)
hypothesis is true, and the number it reports in support means nothing
without also reporting the recovered period next to it.

**Attack 2 — [program-integrity] The named-constant search (items b/d/e)
has a measured, near-100% null-hypothesis pass rate — independently
verified by direct simulation, not merely argued from space size.**
PHOTONICS' and MATERIALS' space-size arithmetic (36,680 expressions,
7,179 distinct values) is exactly reproduced (§2 below). Going one step
further — running the actual permutation-null check both critiques
*propose* but neither *executes* — against `N=10,000` control targets
drawn uniformly from PHOTONICS' own proposed plausible range `[100,1600]`
cells:

```
fraction of random targets with a same-space match within 1%:  100.00%
fraction of random targets with a same-space match within 10%: 100.00%
median closest-match relative deviation:                        0.0369%
```

Robust across three narrower alternate ranges tested (`[300,700]`,
`[150,900]`, `[50,2000]`): still 100.00% in every case. **Every single one
of 10,000 random targets in the physically plausible range finds a match
inside the current CONFIRM band, and the typical (median) match is
*tighter* than the proposal's own headline `3·R_OUT` match to `A_alt`
(0.037% vs 0.347%).** REFUTE (§5: "no match within 10% relative on either
branch") is not merely unlikely under the current design — on this
evidence it is statistically unreachable. This is a stronger, decisive
form of PHOTONICS'/MATERIALS' shared finding: not "a severe look-elsewhere
problem," but an instrument that currently has **zero discriminating
power** between "real geometric mechanism" and "pure numerical coincidence."

**Attack 3 — [program-integrity, non-load-bearing] PHOTONICS' own sharpest
attack conflates two different targets when illustrating "the headline
candidate is not the closest match."** Independently re-verified by exact
enumeration: PHOTONICS cites "six ties (`6·TAPER+3·LEVER`,
`D_SP+8·clear_plane`, etc.) beat it 4× tighter (0.037% vs 0.156%)" to
argue against the "headline candidate (`3·R_OUT=234`)." But `6·TAPER+3·
LEVER` and `D_SP+8·clear_plane` are the six-way tie at value **519**
(rel. deviation 0.0366%), which is the closest rival to **`A_eff=518.81`**
(item d) — and 0.156% is `A−3·R_OUT=518`'s own deviation from `A_eff`, not
`3·R_OUT=234`'s deviation from `A_alt=233.19` (which is 0.347%, item b).
The correct comparison for `3·R_OUT=234` vs `A_alt` is: closest rival is
**233** (`LEVER+7·clear_src`, `9·clear_plane−5·clear_src`, a *two*-way
tie, not six), at 0.0815% — beating `3·R_OUT` by 4.26×, coincidentally
almost the identical ratio PHOTONICS quotes, but from the wrong pair of
numbers and the wrong tie-count. PHOTONICS' bottom-line conclusion
("headline is not the closest match, beaten several-fold") independently
holds for *both* targets when computed correctly, so this does not change
PHOTONICS' verdict or this audit's ruling — but it is exactly the
class of hand-typed/cross-source-conflated figure R4 exists to catch, this
time inside a Phase-2 critique rather than a proposal, the same species of
gap as exp-069's own Attack 5 (a critique's motivating citation subtly
wrong, substantive point still standing). Recorded so Phase 3 does not
propagate the wrong tie-group into NOTES.md.

**Attack 4 — [inexpressible] Item (e)'s "convergence check" is not
computable as specified, because "the best match" is not well-defined.**
Attacks 2/3 establish that both `A_eff` and `A_alt` have multi-way ties at
their closest distance (six-way at `519` for `A_eff`; two-way at `233`
for `A_alt`; more ties appear at looser but still CONFIRM-band distances,
e.g. the 66-way tie at `520`, 0.229%). §7 steps 4 and 6 say "record best
match name" (singular) with no stated tie-break rule. Step 7 then compares
"step 4's and step 6's best-matching NAMED combinations" for exact or
algebraic equality — but which of six (or more) equally-good candidates is
"the" match determines P-070-5's CONFIRM/REFUTE outcome, and nothing in
the committed script design fixes that choice in advance. This is a real
gap, not a style note: an arbitrary implementation choice (e.g. dict
iteration order, first-found-wins) would silently decide a scored
prediction.

**Attack 5 — [unfalsifiable] No pre-committed disposition for gray-zone
outcomes — VISION's catch, independently reconfirmed by direct inspection
of §5's bands.** Confirmed exactly as VISION states: P-070-1 (one config
≥0.30 and the other <0.30, or both in `[0.15,0.30)`), P-070-2 (either
branch's best deviation in `[1%,10%)`), and P-070-4 (a match ≤1% with
`R²∈[0.40,0.70)`) are all structurally undefined outcomes with §7's stated
logic. This is the identical failure shape LOGBOOK records as this
program's own standing Checkpoint-4 pattern, and the one exp-069's own
Red Team audit (this cycle's immediate predecessor, same repo, same
mandate lineage) required a mandatory fix to close — with the fix
language already written and available to copy. Given Attacks 1 and 2
above make it likely that several of P-070-1/2/4 land exactly in these
undefined zones once corrected, this gap is not hypothetical.

**Attack 6 — [program-integrity] THERMODYNAMICS' PLAN.md-named WKB
fold-in is dropped with zero disclosure — confirmed absent across the
entire document.** Grepped the full proposal: no mention of "WKB,"
"adiabatic," or "reflectance" anywhere in the narrative, parameter table,
or nine idealizations. PLAN.md's own Iteration-47 queue text is explicit:
"THERMODYNAMICS' own desk-only WKB/adiabatic boundary-reflectance model
for the graded-loss `ABSORB` band folds into this same batch if capacity
allows, not competing with it for resources." This is the second
consecutive cycle a PLAN.md-named, capacity-permitting item has gone
undisclosed at Phase 1 in this exact spot (exp-069 dropped R_contact the
same way; this cycle's own Idealization list has room for eight other
items and could have carried a ninth). Not yet a repeat-offense pattern
rising to R4's "third consecutive cycle" bar, but one more silent
instance and it should.

**Attack 7 — [inconsistency, minor] MATERIALS' "PML" language is
imprecise for this engine.** VALIDATION.md states explicitly: "graded-loss
bands (**not** PML) at the domain edges." MATERIALS' sharpest attack calls
the boundary "PML/absorbing-boundary reflection leakage" — the
"absorbing-boundary reflection leakage" half is accurate and the
substantive point stands (a graded-loss band's own reflectance can still
depend on its depth, exactly the confound this thread is chasing), but any
caveat sentence Phase 3 lifts from this critique should say "graded-loss
absorbing boundary," not "PML," to stay accurate to `lab/fdtd2d.py`'s
actual construction and not misdescribe this engine's own documented
design choice.

**No constraint-#N-violation applies.** T1 route is correctly N/A
(instrument/model-fidelity class); Checkpoint-criterion-2 candidacy is
correctly declined for every outcome (§8). Checked and confirmed clean.

## 2. Independent verification of the five critiques — per-seat

**PHOTONICS (support-with-changes).** Steel-man on items (a) and (c)
independently confirmed accurate — (c)'s `P_taper(39°,600nm)=36.86°`
figure reproduced exactly by direct recomputation (`degrees(20/(40·
cos(39°)))=36.868°`), an order of magnitude off `P*=2.8421°`, a clean
REFUTE. Sharpest attack (search-space size and density) **independently
reproduced exactly**: 280 singles + 36,400 pairs = 36,680 total, 7,179
distinct values, 140/85 expressions within 1% of `A_eff`/`A_alt`
respectively (confirmed these are counts of *expressions*, not *distinct
values* — PHOTONICS never states which convention it used; only 10/5
*distinct values* land within 1% — see docket item 3 below, an
underspecified-metric gap PHOTONICS itself doesn't flag). "Headline not
closest match" claim **independently reconfirmed true for both targets**,
but the illustrating numbers **conflate the two targets** — Attack 3,
non-load-bearing. Proposed fix (permutation-null control, N=10,000,
range `[100,1600]`) **ADOPTED AND EXECUTED** — Attack 2's own numbers are
this fix, run for real, and the result is more decisive than PHOTONICS'
own space-density argument alone establishes.

**MATERIALS (support-with-changes).** Steel-man confirmed accurate — the
proposal's self-classification (Checkpoint-2 declined, T1 N/A, "numerology
-vs-mechanism discriminator, not a mechanism proof" in its own
Idealization 7) is exactly as described. Sharpest attack (NAMED constants
are FDTD bookkeeping, not material parameters; no false-positive-rate
control) **independently reconfirmed**: every one of the 14 `NAMED`
entries traces to `design_geometry.py::config()`'s own construction
fields (padding, absorbing-boundary depth, taper length, clearances) —
none is a `ε(ω)`, `σ`, or layer-thickness quantity MATERIALS' charter
could grade. **ADOPTED, and independently strengthened** by Attack 2's
executed null check. The "numerical-scheme-artifact, not physical optics"
framing **ADOPTED** as a mandatory caveat (see ruling 3, docket item 5) —
with the "PML" wording corrected per Attack 7.

**ELECTROMAGNETISM (support-with-changes).** Steel-man confirmed accurate.
Sharpest attack (item a confirms by construction, regardless of the true
signal) **ADOPTED AND PROMOTED from "almost certainly fires" to
"demonstrated to fire"** — Attack 1 is EM's own claim, executed against
real data, with the additional finding (not in EM's own critique) that the
recovered period matches neither candidate hypothesis. EM's proposed fix
(score on recovered period, or a two-term fixed+free model) **ADOPTED,
primary variant selected** — see ruling 1 below. EM's secondary note (beat
-frequency "well-separated frequencies" assumption, self-flagged as
non-blocking) reviewed and agreed non-blocking; Idealization 6 already
carries an adequate hedge.

**THERMODYNAMICS (support-with-changes).** Steel-man confirmed accurate —
correctly identifies this as a rare cycle where the charter has little
physics to grade (empty scene, no object, no absorbed-power channel).
Sharpest attack (WKB fold-in silently dropped) **independently
reconfirmed by full-text grep of the proposal** — zero mentions. **ADOPTED
IN FULL** — Attack 6. Ruled on below (ruling 4): real, not cosmetic, but
minor and cheaply closed.

**VISION SCIENCE (support-with-changes).** Steel-man confirmed accurate.
Sharpest attack (no pre-committed gray-zone disposition; three of five
items have a live undefined outcome zone) **independently reconfirmed by
direct inspection of every band in §5** — VISION's three named gaps
(P-070-1, P-070-2, P-070-4) are exactly as described; P-070-5 is correctly
identified as the only strictly binary one. **ADOPTED IN FULL, and ranked
the single most important finding among all five critiques** — same
ranking exp-069's own Red Team audit gave this identical failure shape one
cycle ago, for the identical reason (LOGBOOK's own Checkpoint-4 record).
Second finding (disclosed recon values already sit inside two of five
CONFIRM bands) **independently reconfirmed by direct recomputation**:
`A_alt=233.188` (recomputed via the beat formula, matches disclosed
`233.19`) is 0.347% from `3·R_OUT=234`, inside the 1% CONFIRM band;
`A_eff=518.812` (recomputed, matches disclosed `518.81`) is 0.156% from
`518`, inside 1%, with the disclosed `R²=0.7666` already 0.0666 above the
0.70 bar. **ADOPTED IN FULL** — Attack 2's own null-check result makes
this finding sharper still: those same "already inside the band" values
are *not exceptional* against the null distribution (median null-match
deviation 0.037% is *tighter* than `A_alt`'s own 0.347% match to
`3·R_OUT`), so the HARKing risk VISION flags and the look-elsewhere risk
PHOTONICS/MATERIALS flag are the same underlying defect, not two separate
problems.

**No override of any of the five critiques' core, load-bearing points.**
Every sharpest attack is adopted in full or adopted-and-strengthened with
independently executed evidence; the one place this audit goes beyond
"adopt as proposed" is running PHOTONICS'/MATERIALS' own suggested
permutation-null check for real rather than leaving it as a proposed
future step, and finding it more decisive than either seat's own
space-counting argument shows on its own. Attack 3 corrects a
non-load-bearing citation error inside PHOTONICS' own text without
changing PHOTONICS' verdict.

## 3. Decisive rulings on the four posed questions

**(1) Does item (a) need EM's fix before this batch can run at all?**
**Yes, unconditionally, and the need is now proven rather than merely
argued.** Attack 1 shows item (a) CONFIRMS today, on real committed data,
via a spurious third period. Running the batch with item (a) unfixed does
not risk a misleading headline — it manufactures one. **Primary fix
(adopted): score P-070-1 on the recovered period, not bare R².** CONFIRM
requires `|P*_free(C40)−P*_delta|/P*_delta ≤ 20%` **AND** the same for
`C80` — reusing the exact tolerance convention already used elsewhere in
this batch (P-070-2/3/4), so no new machinery or judgment call is
introduced. REFUTE requires either config's free-fit `R²<0.15` **OR** its
recovered period misses `P*_delta` by `≥50%`. Anything else is `NEITHER`
(folds into docket item 4). EM's secondary two-term-model variant is
sound but adds new statistical machinery this batch's zero-FDTD, reuse-
only design otherwise avoids entirely — not required given the simpler
fix is already sufficient and directly falls out of a tolerance band this
batch uses four other times.

**(2) Does the named-constant search need a null-control correction
before ANY match is reported as more than "consistent with, unable to
distinguish from chance"? If yes, specify exactly.** **Yes, and Attack 2's
own executed check both proves the need and hands Phase 3 the concrete,
already-validated procedure — implement this exactly:**

1. **Range:** `T ~ Uniform(100, 1600)` cells (PHOTONICS' own proposed
   aperture-scale plausibility window; independently confirmed
   range-insensitive across three alternate ranges tested, so this choice
   is not doing hidden work).
2. **Trials:** `N=20,000` (matching T28's own founding permutation test
   exactly, LOGBOOK/exp-069 — not the smaller `N` either blind critique
   proposed independently, for direct precedent-consistency).
3. **Per trial:** draw one `T_i`; evaluate the identical search space (§3
   row 5 — all 280 singles + 36,400 pairs, `|c|≤10`, read from `CONFIGS`,
   never hand-typed); record `best_rel_i = min` relative deviation over
   the whole space.
4. **Null distribution:** the 20,000 `best_rel_i` values.
5. **Real statistic:** for each real target (`A_alt`, both beat branches;
   `A_eff`), compute its own `best_rel` the identical way (Attack 4's
   tie-break fix, docket item 3, applies here too — report ALL tied
   closest matches, not one).
6. **Percentile:** `p = fraction of null trials with best_rel_i ≤ the real
   target's own best_rel`.
7. **Gate:** P-070-2/P-070-4/P-070-5 may be scored CONFIRM only if `p ≤
   0.05` for the relevant target (the real match must be tighter than 95%
   of what pure chance achieves in this same space). `p` itself must be
   reported alongside every CONFIRM or NEITHER verdict, not only the
   binary pass/fail.
8. **Do not accept this audit's own N=10,000 scratch numbers as the gated
   result** (R4: diagnostic-only, not code-committed at prediction-freeze)
   — Phase 3/4 must re-run at N=20,000 through the actual committed
   script. Given the scratch run already shows 100% of `N=10,000` random
   targets clear the 1% band with a *tighter* median deviation
   (0.037%) than either real target's own best match to its nearest
   named-constant rival, the honest expectation to state in the proposal
   text going into Phase 3 is that `p` is likely to land near or above
   50th percentile for both targets — i.e., the corrected search will
   most likely NOT license a CONFIRM. That expectation must be stated
   as a prediction, not discovered as a surprise at Phase 5.

**(3) Should MATERIALS' "even a CONFIRM might be a numerical-scheme
artifact" point be a mandatory disclosed caveat regardless of outcome?**
**Yes, unconditionally, and independently strengthened by this audit's own
finding.** Every `NAMED` constant is FDTD domain-construction bookkeeping
(confirmed, Attack/§2); Attack 2's null check shows the search space is
dense enough that essentially any length scale in the plausible range
finds a same-quality match, which is itself consistent with — arguably
predicted by — a boundary-construction-tied artifact rather than a
load-bearing physical resonance (bookkeeping constants that happen to
share small-integer ratios with each other by construction, not by
physics). The caveat must ship regardless of P-070-2/4/5's outcome,
worded as MATERIALS proposed with Attack 7's "PML"→"graded-loss absorbing
boundary" correction (docket item 5).

**(4) THERMODYNAMICS' WKB gap and VISION's gray-zone/HARKing gap — real,
cosmetic, or between? Minimal fix for each?** **VISION's gap is real and
structural — this cycle's single highest-priority fix**, for the same
reason exp-069's own Red Team ranked the identical failure shape as its
own top finding one cycle ago: LOGBOOK's Checkpoint-4 record exists
because of exactly this pattern, and Attacks 1/2 above make the gray zones
non-hypothetical (a corrected item (a) and a null-corrected item (b)/(d)
are each likely to land somewhere a binary CONFIRM/REFUTE band does not
cover). Minimal fix: one explicit sentence per item, "any outcome outside
both bands is reported as `NEITHER`, disclosed verbatim, and does not
count toward narrowing PLAN.md queue item 2's scope" — mirroring
exp-069's own mandatory-fix-4 language exactly (docket item 4).
**THERMODYNAMICS' gap is real but minor** — a named, capacity-permitting
PLAN.md item dropped without a trace, the same species of omission as
exp-069's own R_contact gap, but (unlike R_contact's un-blocked-tooling
excuse) here there's no stated reason it was skipped at all. Given this
batch's genuinely zero marginal FDTD cost, the minimal fix is a one-line
disclosure sentence matching the R_contact precedent (docket item 6) —
folding in an actual WKB estimate as a new item (f) is not required this
cycle (it is real new analytic work, not a free byproduct of what (a)–(e)
already compute, unlike item (e)'s convergence check), but is not
prohibited if capacity allows.

## 4. Overall verdict

**PROCEED-WITH-MANDATORY-FIXES.**

The batch's core structure is sound and genuinely disciplined: it is
zero-FDTD-cost, reuses validated statistics and committed data rather than
re-deriving anything, correctly declines Checkpoint-2 candidacy, and item
(c) alone already delivers a clean, real, order-of-magnitude REFUTE at
zero risk. No seat opposes. But two of its five items are not merely
imperfect as this audit found them — they are **proven, by direct
execution of the proposal's own committed logic against the proposal's
own committed data, to not measure what §5's prose claims they measure**:
item (a) CONFIRMS today regardless of the true signal, landing on a third,
unexplained period; items (b)/(d)/(e)'s search space clears its own
CONFIRM band for 100% of tested random targets. Both defects are fixable
entirely at the design stage, with zero new FDTD spend and no change to
the batch's core zero-cost construction — exactly the shape of gap this
program's own PROCEED-WITH-MANDATORY-FIXES verdict exists for, not
REJECT or MAJOR-REDESIGN. Deferring this batch further, given it is
already the Iteration-48 tripwire's own designated first move, is not an
option Red Team will countenance either.

**Accepted in full, all five seats:** PHOTONICS (search-space
characterization, headline-not-closest-match), MATERIALS (bookkeeping-not
-material-parameters, artifact-vs-mechanism caveat), ELECTROMAGNETISM
(item-a confirms-by-construction), THERMODYNAMICS (WKB omission), VISION
SCIENCE (gray-zone gap, HARKing-shaped band placement). **No criticism
from any of the five seats is overridden.** This audit's own contribution
beyond the five: executing PHOTONICS'/MATERIALS' own proposed
null-control check for real (Attack 2, with concrete numbers now on
record), proving rather than arguing EM's attack (Attack 1), and two new,
independently-found gaps — item (e)'s tie-break well-definedness problem
(Attack 4) and a non-load-bearing citation conflation inside PHOTONICS'
own critique (Attack 3).

### Mandatory-fix docket (10 items — apply at Phase 3, before predictions are committed to git)

1. **Redefine P-070-1's pass/fail logic to score the recovered period, not
   bare R².** CONFIRM: `|P*_free(C40)−P*_delta|/P*_delta ≤ 0.20` **AND**
   same for `C80`. REFUTE: either config's `R²_free < 0.15` **OR** its
   recovered-period deviation `≥ 0.50`. Else `NEITHER` (item 4). Report
   the recovered `P*` value for each config alongside its `R²`, always.
   (Attack 1 — ADOPT + PROVE EM.)

2. **Add the permutation-null control to items (b)/(d)/(e), exactly as
   specified in ruling (2) above:** `N=20,000`, `T~Uniform(100,1600)`
   cells, identical search space, report `p`-percentile alongside every
   CONFIRM. No P-070-2/4/5 CONFIRM may be reported without this `p`
   computed and disclosed. (Attack 2 — ADOPT + EXECUTE PHOTONICS +
   MATERIALS.)

3. **Fix item (e)'s (and the null-control's) tie-break well-definedness
   gap.** When multiple named-constant expressions tie (within float
   tolerance, e.g. `1e-9` relative) for closest match, report ALL tied
   expressions, not one; item (e)'s convergence check counts as a match
   if the two sets (from `A_alt` and `A−A_eff`) share ANY common
   normalized expression, not only if their single "best" picks agree.
   Also state explicitly which counting convention (distinct expressions
   vs. distinct numeric values) any "N candidates land within X%"
   sentence in NOTES.md uses — PHOTONICS' own 140/85 figures are an
   expression-count, independently reproduced as such; the corresponding
   distinct-value counts are 10/5. (Attack 3 + Attack 4 — this audit's
   own catch.)

4. **Add the pre-committed gray-zone catch-all, per item, matching
   exp-069's own mandatory-fix-4 language verbatim:** "any P-070-N outcome
   outside both its CONFIRM and REFUTE band is reported as `NEITHER`,
   disclosed verbatim in NOTES.md, and does NOT count toward narrowing
   PLAN.md queue item 2's scope." (Attack 5 — ADOPT VISION in full,
   ranked this cycle's single highest-priority fix.)

5. **Add MATERIALS' mandatory disclosed caveat, regardless of outcome, in
   §1/§8 (not buried in an idealization):** "No outcome of items (b), (d),
   or (e) — CONFIRM, REFUTE, or NEITHER — bears on realizability or
   establishes a physical diffraction mechanism. Every `NAMED` constant is
   this bench's own FDTD domain-construction bookkeeping (grid padding,
   graded-loss absorbing-boundary depth, taper length, window/guard
   geometry), not a material or physical-optics parameter; a match is at
   least as consistent with a numerical-boundary-construction artifact of
   THIS engine's own graded-loss band (not PML — `lab/fdtd2d.py`'s
   documented construction, VALIDATION.md) as with a physically real
   diffracting edge." (Attack 7 + MATERIALS — ADOPT with terminology
   correction.)

6. **Add a one-line THERMODYNAMICS disclosure, matching exp-069's own
   R_contact precedent:** "PLAN.md's Iteration-47 queue item 1's own
   named capacity-permitting fold-in — THERMODYNAMICS' desk-only
   WKB/adiabatic boundary-reflectance model for the graded-loss `ABSORB`
   band — is not picked up this cycle; no stated capacity constraint
   prevented it, this is a scope choice, disclosed rather than silent."
   (Attack 6 — ADOPT THERMODYNAMICS.)

7. **Disclose plainly in §1 (not buried in Idealization 7) that the
   P-070-2/P-070-4 CONFIRM thresholds already contain the disclosed recon
   values, comfortably inside:** `A_alt≈233.19` is 0.35% from `3·R_OUT`
   (CONFIRM bar is ≤1%); `A_eff≈518.81` is 0.16% from `518` with disclosed
   `R²=0.7666` already above the 0.70 bar. State whether the 1%/0.70
   thresholds were set before or after these specific numbers were
   computed, so Phase 3/4/5 readers can judge pre-registration
   independence for themselves. (Attack 2 sharpens this — ADOPT VISION.)

8. **Correct the search-space provenance sentence Phase 3 lifts into
   NOTES.md** so it does not repeat PHOTONICS' own cross-target
   conflation (Attack 3): if citing "the headline candidate is not the
   closest match," cite the correct comparator for whichever target is
   under discussion — `234` (`3·R_OUT`) vs `A_alt=233.19`'s own rival
   (`233`, a two-way tie, 0.0815% vs 0.347%), not the `A_eff`/`519`
   six-way tie's numbers. (Attack 3 — this audit's own catch.)

9. **Run the permutation-null control (item 2) BEFORE narrating any
   P-070-2/4/5 result in NOTES.md**, and if `p` lands above 0.05 for a
   given target (this audit's own N=10,000 scratch check makes this the
   likely outcome — see ruling 2 above), report that target's match as
   `NEITHER` under item 4's catch-all, explicitly stating it is
   statistically indistinguishable from chance, not as a qualified or
   soft CONFIRM. (Attacks 1+2+5, combined — the composite fix this
   docket exists to enforce.)

10. **PLAN.md queue item 2 (EM's C60/C70 test or PHOTONICS' 750nm re-run)
    must be narrowed only by items that clear docket item 9's corrected
    gate** — a `NEITHER` or a null-indistinguishable P-070-2/4/5 does not
    narrow queue item 2's scope; only a genuinely `p≤0.05` CONFIRM, or
    item (a)'s corrected config-invariant CONFIRM/REFUTE, may do so.
    (Direct consequence of items 1, 2, 4, 9 — stated once, explicitly, so
    Phase 5 cannot read a `NEITHER` as informative by default.)

None of these fixes require new `lab/` engine code, new FDTD calls, or a
change to the batch's own zero-cost, reuse-only construction. All ten are
computable from data already committed, before predictions are committed
to git, per house discipline.
