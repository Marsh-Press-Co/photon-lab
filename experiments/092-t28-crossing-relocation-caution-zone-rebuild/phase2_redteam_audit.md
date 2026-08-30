# PHASE 2 — RED TEAM FINAL AUDIT · Panel Iteration 69 · exp-092
## "Crossing Relocation & Caution-Zone Rebuild"

Red Team reads everything: `phase1_proposal.md` plus all five blind Phase-2
critiques (PHOTONICS, MATERIALS, THERMODYNAMICS, QUANTUM OPTICS, VISION
SCIENCE). Scope note, matching every T28 desk/instrument cycle's own Red
Team audit since exp-069 (069/087/088/089/090/091): this is a
zero-mechanism instrument-recalibration cycle. **Confirmed, not assumed**
(§4, below): T1 route is genuinely N/A and Checkpoint criterion 2 is N/A,
not merely not-yet-ripe — this cycle proposes no phenomenon mechanism and
its own load-bearing numbers (§3 of this audit) stay far below the
perceptual threshold this whole program exists to test. The charter's four
attack tags are adapted per this sub-thread's own established convention:
`constraint-#N-violation` would cover a misstatement of a standing R-rule
or a quiet re-opening of the T1/constraint-3 N/A framing; `unfalsifiable`
covers a claimed benefit or claim that cannot be checked against any
committed prediction; `inconsistency` covers internal contradiction,
mistransferred evidence, and failure to carry an already-disclosed caveat
forward; `inexpressible` does not apply anywhere in this cycle (every
quantity is concretely FDTD- or desk-computable) and is not used below.

## 0. Independent verification performed (before adjudicating anything)

Nothing below is taken on the proposal's word, any critique's word, or the
task brief's own framing.

- **Re-derived the DROP/RELABEL table (§3 of the proposal) from primary
  sources a fourth independent time**, importing `experiments/090-.../
  run.py`'s actual `auc`/`firth_logistic`/`naive_mle_diverges` unmodified
  and running the ORIGINAL/DROP/RELABEL recipe against exp-090's own
  committed `results.json::table1` myself (QUANTUM's critique reports
  having done this too, independently; the Phase-1 author, EM, reports a
  third independent pre-verification pass). **Every cell reproduces
  bit-exact**: AUC=1.000000/1.000000/0.833333, zone=[1.4764,2.1709]
  (unchanged)/[1.4764,1.3095] (inverted), Firth β=[1.7806,−5.6315]/
  [1.1798,−4.5447]/[0.0385,−2.8425], m₅₀=2.071013/1.818061/1.031717,
  naive-MLE-diverges=True/True/**False**. This is now a fourth independent
  confirmation of Rank 2's entire deliverable — the strongest evidentiary
  status any single component of this proposal carries.
- **Read `lab/fdtd2d.py::Sim._damping` directly**: confirmed it is a pure
  function of `self.absorb`, `nx`, `ny` only — no `pad` parameter anywhere
  in its body. `PAD`'s only effect is on domain size (which shifts `nx`/
  `ny`, hence where the fixed-width `absorb`-cell ramp sits) and scene
  coordinates, never the damping mask's own shape or depth. The proposal's
  §1 "provably lossless vacuum" premise is verified true in code, exactly
  as exp-076's own Red-Team-confirmed finding states.
- **Read `experiments/091-.../run.py:193`**: confirmed
  `materials.graded_black_shell(sim, cx, cy, PEC_R_R3, R3_R_OUT_CELLS)` is
  called with no `sigma_max` argument at exp-091's own R3 leg — the
  function's own default (`sigma_max=0.5`) is what exp-091 actually shipped,
  confirming the proposal's "as-filed, unscaled 0.5" premise from the
  primary source, not the proposal's paraphrase of it.
- **Re-derived `sigma_max_R3=1/3` from `lab/materials.py::graded_black_shell`
  and `experiments/069-.../design_geometry.py`**: `R3_R_OUT=round(78×1.5)
  =117` (confirmed by direct read), native `τ_center=2×0.5×78=78`, as-filed
  R3 `τ_center=2×0.5×117=117` (a genuine 1.5× inflation, matching
  `R3_RATIO` exactly), corrected `sigma_max_R3=78/(2×117)=1/3` exactly.
  Algebraically forced, not a fitted or approximate number.
- **Re-derived every cost/budget figure in §5** by hand from
  `dg069._cost()`'s own formula, reusing exp-091's own cited per-call
  costs (`C40_R3`: 168.75 CPU-s, `G40_R3`: 234.9 CPU-s — both confirmed
  unmodified against `experiments/091-.../phase2_redteam_audit.md` §0's
  own independently-derived figures): Rank 1 `5×2×(168.75+234.9)=4036.5`,
  Rank 3 `3×(168.75+234.9)=1210.95`, total `5247.45` CPU-s ≈ 87.5 CPU-min;
  wall `1.15×5247.45/(4×0.98)≈1539s≈25.6min`; 3× envelope ≈77min. All
  exact, all inside every established T28 per-cycle budget. **No defect
  found anywhere in the geometry, derivation, or budget arithmetic.**
- **Checked whether resequencing Rank 3 before Rank 1 changes the total
  wall-clock cost** (the practical objection a Director might raise
  against the sequencing fix both MATERIALS and QUANTUM demand, §2 below):
  computed separately, `wall(Rank 3 alone)≈355s` + `wall(Rank 1 alone)
  ≈1183s` ≈ `1538s` — bit-identical (to rounding) to the combined
  `1539s` figure above. CPU-time is additive regardless of execution
  order at this worker count; **sequencing costs zero additional wall
  time**, not merely "small."
- **Read `experiments/091-.../NOTES.md` lines 186–216 directly** (not the
  proposal's or VISION's paraphrase of it) to check the Idealization-8
  citation-gap claim (§1.5 below): confirmed exp-091's own Idealization 8
  reads "No full R3-rescaled rebuild of exp-083's 31-point window, and no
  extension of R14(b)'s still-queued formal null-controlled period fit —
  both remain open, separate, standing T28 items" and is absent from
  `phase1_proposal.md`'s §8 list verbatim.
- **Grepped `experiments/091-.../run.py` and `run_output.txt` for
  `netd_disclaimer`/`scope_note`**: confirmed both fields are written into
  the `results.json`-bound dict (`run.py` lines 420, 746, 749) and **never
  appear in `run_output.txt`** (zero hits) — the print-parity gap VISION
  cites is real, confirmed at the source, not merely restated from
  VISION's own exp-091 review.
- **Grepped LOGBOOK.md's own T27 record** (Iteration 42–45) to check
  Idealization 8's claim that "settling is a temporal/domain property, not
  source-angle-dependent" (§3, RT-2 below) against this program's own
  established record, rather than accepting the claim as self-evident.

## 1. Adjudication of the five blind critiques

### 1.1 PHOTONICS — the amplitude-inflation-corroborates-widening claim is a non sequitur — **UPHOLD**

Tag: `inconsistency`. PHOTONICS' core mathematical point is correct and I
verify it independently: a zero-crossing of `f(θ)` is invariant under a
uniform amplitude rescaling `f→k·f` — vertical growth carries no
information, by itself, about whether a horizontal (location) shift
occurred, still less its direction. §2a cites EM's own
`2.8×–5.2×` `frac_contrast` inflation (measured at three angles, none of
them the crossings) as "the same direction as" a claimed lobe-widening —
but inflation-at-non-crossing-points and crossing-location movement are
logically independent observables unless the inflation is itself shown to
be spatially non-uniform in a shape-relevant way, which the proposal never
demonstrates. The genuinely load-bearing evidence for widening is the
2-point secant extrapolation itself (§2a's own opposite-signed-shift
arithmetic, independently re-verified exact in §0 of exp-092's own QUANTUM
critique and reproducible from `results.json::a2.per_pair`) — that
argument stands on its own and does not need the amplitude citation to
support it. The amplitude sentence is surplus, incorrect corroboration
layered onto an otherwise sound argument, not the argument's foundation.

PHOTONICS' own proposed fix — extend the lower net by two more
`DENSE_ANGLES` points (39.2°/39.4°, ~4 calls) — rests on a *different*,
stronger, and independently checkable piece of evidence: at 40.2° itself,
`delta_scene` already flipped sign under `cpl` refinement
(`−1.5427×10⁻⁴`→`+4.3699×10⁻⁴`, exp-091), a jump comparable in size to
the entire `40.0°→40.2°` approach at `cpl=20` (`−6.899×10⁻⁴`→`−1.5427×10⁻⁴`,
a swing of similar order). This is direct, measured evidence that the
local curve near the lower crossing moved by an amount the 2-point secant
alone may underestimate — a distinct, better-grounded reason to widen than
the amplitude non sequitur, and one PHOTONICS states honestly is aimed
specifically at the lower window (the upper crossing has no analogous
already-observed sign flip at any sampled point, only extrapolation).
**Elevated from discretionary to mandatory** (see §5) on the same R8-style
logic Red Team applied to EM's bracketing fix in exp-091's own audit: a
cheap (~4-call), well-evidenced, named check exists to reduce a real risk
to this cycle's own single PRIMARY deliverable (locating the crossings) —
arguing around it rather than running it is exactly the shape R8 exists to
prevent, even though the design's own REFUTE outcome path already handles
a missed net gracefully (this is about protecting the deliverable's
*success* probability, not papering over an unhandled failure mode).

### 1.2 MATERIALS — Rank 1 spends 77% of budget on an article Rank 3 is built to test, unsequenced — **UPHOLD**; see §2 (dedicated adjudication)

### 1.3 THERMODYNAMICS — Rank 3 recomputes `p_abs_w`/`frac_p_abs` as an unscored byproduct — **UPHOLD**

Tag: `inconsistency`. I independently confirmed from §6 of the proposal
that Rank 3's own falsifiable-outcomes text scores only `delta_scene`
(sign+ratio) and `frac_contrast` (ratio) — no CONFIRM/REFUTE band appears
anywhere for `p_abs_w` or `frac_p_abs`, even though §4b explicitly states
both are "recomputed as a byproduct" of the same six calls. This is
exactly the asymmetric-treatment shape R14 (adopted Iteration 65, exp-088)
exists to police — a real physical-parameter change (a 33% conductivity
cut) with a genuine, cheap, already-computed output left unscored is the
"argued, not banded" gap this program's own R4/R8 lineage exists to close.
THERMODYNAMICS' own proposed band (`p_abs_w` ratio ∈ `[0.3,3.0]` CONFIRM,
directional lean toward a T9-consistent modest decrease; `ratio_abs_ext`
stability within ~2–3% of the established 0.51 anchor) is well-targeted,
correctly cites the T9 anchor as the reason to expect a modest rather than
linear-in-σ effect, and costs zero additional FDTD calls. **Mandatory.**

### 1.4 QUANTUM OPTICS — the same sequencing objection as MATERIALS, independently converged via a different reasoning path — **UPHOLD**; see §2

QUANTUM's own independent verification pass (§0 of its critique) is the
most thorough of the five — it re-derived every one of the proposal's
headline numbers from primitives before writing the critique at all,
including reproducing Rank 2's own DROP/RELABEL table bit-exact (matching
my own §0 reproduction above and the Phase-1 author's own pre-verification
— now three-to-four-way independent agreement on that specific
deliverable). QUANTUM frames the sequencing gap through this program's own
R7/R8 lineage ("price the cheap thing before committing to the expensive
one," applied to FDTD budget allocation rather than a statistical test) —
a genuinely different framing from MATERIALS' T10/SIGMA_ON-precedent
framing, converging on the identical fix from an independent angle. Per
this program's own standing convention (independently-converging blind
critiques carry more weight than either alone), this doubles the case for
treating the sequencing fix as mandatory rather than discretionary — see
§2.

### 1.5 VISION SCIENCE — a dropped idealization citation and a deferred print-parity fix — **UPHOLD, both**

Tag: `inconsistency`. Independently confirmed at the source (§0): exp-091's
own Idealization 8 ("no full R3-rescaled rebuild of exp-083's 31-point
window, and no extension of R14(b)'s... period fit") is genuinely absent
from `phase1_proposal.md`'s §8 list, which otherwise correctly re-cites
every other exp-091 idealization number-for-number (including correcting
exp-091's own Phase-1-draft mislabeling of "3/7/8"→"3/6/7" in its own
banner — a real, demonstrated improvement over the prior cycle, credited
in full). The R14(b) half of Idealization 8 is, in substance, still
carried forward elsewhere in this document (§7's "still-queued R14(b)
formal null-controlled period fit... standing, unaffected") — but the
"no full 31-point R3 rebuild" half has no equivalent restatement anywhere
in exp-092, and nothing in this cycle changes its truth. This is a real,
if narrow, instance of exactly the pattern the Iteration-65 CHECKPOINT's
escalated banner rule exists to police, even though — matching that
rule's own discharge test — it is caught here, blind, before Phase 3.

The print-parity finding is independently confirmed at the source (§0):
`netd_disclaimer`/`scope_note` are written to the dict that becomes
`results.json` but never printed to `run_output.txt` anywhere in exp-091's
record. §7 Tier 4 of this proposal explicitly defers the structural fix to
"whichever future cycle builds Iteration-69+'s own tooling improvements" —
but exp-092 **is** that future cycle: its own 26 new FDTD calls will
generate a fresh `run_output.txt` that, unfixed, reproduces the identical
gap in the identical machinery, one cycle after the defect was named and a
fix recommended. A one-line `print()` addition before Phase 4 is
essentially free. **Both mandatory** (§5).

**No item from any of the five Phase-2 critiques is overridden.** All five
independently verify, from primary sources, real gaps in the frozen
proposal; none rests on a misreading or an unfounded assumption once
checked against the code/data directly (§0). The only refinement applied
is scope, not substance: PHOTONICS' fix is elevated from "flip" to
mandatory (§1.1), matching this program's own R8 escalation precedent.

## 2. The sequencing objection — MATERIALS and QUANTUM, independently converged — dedicated adjudication

**Ruling: CORRECT AND PRACTICAL. Adopted as mandatory, not overridden, not
merely "correct but impractical this cycle."**

**Why correct.** Rank 3 (6 calls, reusing exp-091's own already-collected
empty-leg captures at zero extra cost, §0's verified empty-leg-reuse claim)
directly tests whether the exact article construction (`sigma_max=0.5`,
unscaled) Rank 1 spends 20 calls (77% of this cycle's own FDTD budget)
searching on is even the right article to be searching with. If Rank 3
REFUTEs (a live, self-rated possible outcome per the proposal's own §6 —
not a formality), every one of Rank 1's five newly-located points is, as
filed, a measurement of a systematically-too-strongly-absorbing article —
precisely the failure shape this sub-thread has already lived through once
by accident (the T10/SIGMA_ON erratum, LOGBOOK Iteration 4–5: "a
systematically different, more strongly absorbing article at every λ, not
a resolution-matched rerun"). Running it again here, as a *disclosed,
knowingly-deferred* risk on the cycle's single largest spend, rather than
gating it, converts an accidental historical mistake into a repeated,
avoidable one.

**Why practical.** I independently confirmed (§0) that resequencing costs
**zero additional wall-clock time**: CPU-time is additive regardless of
execution order at this worker count (`Rank 3 alone` + `Rank 1 alone` ≈
`1538s`, bit-identical to the combined `1539s` the proposal already
budgets), and nothing in Rank 3's own inputs depends on Rank 1's outputs
or vice versa (Rank 3 touches only 37.2°/40.2°/41.4°, never any of Rank
1's five new angles). The fix is a pure control-flow reordering in
`run.py` — run Rank 3's 6 calls first, branch on its CONFIRM/REFUTE/
NEITHER outcome, then run Rank 1's 20 calls at the article `sigma_max`
value that verdict licenses (0.5 if CONFIRM; 1/3 if REFUTE; a disclosed,
explicit scope decision — halt-and-report or run both articles at
proportionally reduced coverage — if NEITHER). This fits inside the
cycle's own stated 87.5 CPU-min budget and 77-minute safety envelope with
no re-scoping.

**A residual limitation resequencing does NOT fully close (Red Team's own
addition, not raised by either critique).** Gating Rank 1's *sigma_max
choice* on Rank 3's verdict fixes which article the 20 FDTD calls measure.
It does **not**, by itself, revalidate Rank 1's own **net placement**
(§2a's asymmetric, outward-biased 5-point window), which was derived from
a naive linear extrapolation of exp-091's own already-collected
`sigma_max=0.5` bracket-slope data. If Rank 3 REFUTEs, the corrected
article's true crossing locations are not guaranteed to fall inside a
window that was sized using the *uncorrected* article's own local slope
behavior — the net's own design logic, not merely its measurement, inherits
the same sigma dependency Idealization 9 already discloses but does not
price. This does not argue against resequencing (it is still strictly
better than not sequencing, and still costs nothing extra); it argues for
an explicit disclosure, alongside the resequencing fix, that a Rank-3
REFUTE should be read as reopening the net's own §2a placement logic for a
future cycle, not merely as licensing a different `sigma_max` value for
this cycle's own 20 calls.

## 3. Red Team's own additional attacks (not raised by any of the five blind critiques)

**RT-1. Rank 3's own §6 text mischaracterizes what question its reused
tolerance band is being applied to — a second occurrence, within one
cycle, of a band-mistransfer pattern already flagged once.** [`inconsistency`]

§6's own text for Rank 3 reads: "Reusing the same `[0.3,3.0]` CONFIRM /
`[0.1,10]` REFUTE ratio-and-sign bands exp-091 §4(a) established for the
**identical resolution-rescale question**." This is imprecise in a way
that matters: exp-091's own §4(a) used this band to test a *resolution*
change (`cpl=20` vs `cpl=30`, holding the article fixed). Rank 3 holds
resolution fixed (`cpl=30` throughout) and instead varies `sigma_max`
(0.5→1/3) — a *material-parameter* question, not a resolution one. Calling
this "the identical resolution-rescale question" is factually wrong as
written, and it matters because the band's own physical appropriateness
for *this* comparison is never independently argued — it is simply
inherited by citing a superficial resemblance ("a ratio-and-sign
tolerance band") to a differently-motivated prior use. This is the same
mistransfer shape PHOTONICS' own exp-091 critique already caught and Red
Team upheld one cycle earlier (`experiments/091-.../phase2_redteam_audit.md`
§1.1: "a wide magnitude-ratio band built for one physical quantity class
does not automatically transfer to a different one") — recurring here a
second time, inside the very cycle meant to test that channel's own
robustness, unflagged by any of the five blind critiques. **This does not
mean the band's actual numeric values are wrong for Rank 3's purpose** — a
generic order-of-magnitude "materially changed vs. not" tolerance is a
defensible house convention independent of mechanism, and nothing here
shows `[0.3,3.0]`/`[0.1,10]` is miscalibrated for detecting a genuine
sigma-driven shift. The defect is the document's own justification
text, which claims a physical identity between two different questions
that does not exist. **Fix (mandatory, wording only, zero cost):** correct
the sentence to state plainly that this is a *repurposed*, generic
magnitude/sign-change tolerance, not evidence that the sigma-correction
question and the resolution-rescale question are the same kind of test.

**RT-2. Idealization 8's justification for skipping a per-angle settling
check overclaims against this program's own established T27 record.** [`inconsistency`]

Idealization 8 states: "settling is a temporal/domain property, not
source-angle-dependent, in this bench's own established convention." I
checked this against LOGBOOK's own T27 thread (Iterations 42–45, the
`STEPS=1400`-unsettled-plane-channel finding) rather than accepting it at
face value. T27's own Phase-5 finding states plainly: "the exposure is
wider than exp-065's own Phase-4 framing: ±35°... **sign-flips under the
same correction, not just shifts in magnitude**" — a directly on-point,
already-established counter-example, on this identical instrument family,
that settling residuals *can* be angle-dependent, at least at an
under-settled `STEPS` count. Idealization 8's blanket claim is, as worded,
false against this program's own record. **This does not mean the actual
decision is wrong in practice.** T27's finding concerns a severely
under-settled regime (`STEPS=1400`, a small fraction of full convergence);
exp-091's own settling checks at `STEPS=4200`/`cpl=30` (the exact
configuration Rank 1 extends to five new nearby angles) landed
`10⁻⁷`–`10⁻⁴` relative deviation — six-plus orders of magnitude inside the
`≤1%` bar, not merely "settled enough." Extrapolating that depth of margin
to five `DENSE_ANGLES` points within 2.4° of the three already-checked
ones is physically reasonable; the correct argument is "the checked
margin is so large that a plausible angle-to-angle settling variation
cannot plausibly consume it," not "settling isn't angle-dependent, full
stop" — the latter claim this program's own T27 record already refutes at
a different operating point. **Fix (mandatory, wording only, zero
additional FDTD required):** rewrite Idealization 8 to argue from the
depth-of-convergence margin at the three checked angles, with an explicit
T27 cross-reference, rather than a blanket non-angle-dependence claim.
**Discretionary, not mandatory** (cost is trivial but not free, and the
corrected argument above is sound): add one settling spot-check (e.g.
`STEPS` doubled at 42.0°, the window-edge point furthest from any
already-checked angle) as belt-and-braces insurance, at the Director's
discretion given remaining budget headroom.

## 4. Confirming the T1/constraint-3 N/A framing holds — checked, not assumed

Per the task brief's own instruction, I did not take §9's "N/A, stated
plainly" on faith. Two independent checks: (1) grepped LOGBOOK.md's own
T28 sub-thread record (Iterations 46–68, exp-069 through exp-091) for
every Combined Verdict / Checkpoint-criterion-2 line — every single entry
reads "T1 route N/A" / "Checkpoint criterion 2: N/A" for this exact
desk/instrument sub-thread, with zero exceptions, confirming the
proposal's own claim that this is a structural, not incidental, property
of the whole sub-thread since its founding. (2) exp-091's own Red Team
audit (§3, independently reproduced here rather than merely cited)
computed the absolute-Weber-contrast scale of the very tolerance bands
this cycle reuses: even the loosest band edge (`×3.0`, CONFIRM) stays
7–12.5× below `C_THR_BASE=0.005` at all three census angles, and even the
REFUTE edge (`×10`) stays 2.1–3.7× below it. Nothing this cycle measures,
scores, or could plausibly REFUTE on approaches the perceptual threshold
this program's constraint-3 machinery exists to police. **The N/A framing
holds; it is not quietly slipping.**

## 5. Checkpoint / standing-rule check

**Constraint 1–4 / T1**: N/A, confirmed independently (§4) — no
misstatement found. No `constraint-#N` tag applies anywhere in this audit.

**R3**: this cycle is a direct, correctly-scoped continuation of R3's own
meta-rule and R15's own founding text (a caution-zone boundary built from
resolution-sensitive points must be R3-verified before further trust) —
not a violation of either. Rank 1 extends the search net; Rank 2 reports
the zone's own consequence under two counterfactual relabelings; Rank 3
extends R3's own resolution-check discipline to a second confound
(`sigma_max`) on the same channel. All three are faithful executions of
exp-091's own near-unanimous Reconciled-Queue Rank 1–3, not a scope
deviation.

**R13/R14**: correctly applied unchanged — the proposal explicitly declines
to re-derive or relax either threshold (§6, §8 Idealization 6), matching
exp-091's own precedent.

**R8 (an unverified robustness/independence argument is not sufficient
when an affordable named check exists)**: this rule is squarely engaged
twice in this cycle — the sequencing question (§2, MATERIALS+QUANTUM,
mandatory) and PHOTONICS' net-extension fix (§1.1, mandatory) both fit its
exact shape: a cheap, specific check exists and the proposal's own
disclosure (§2c, §7 Idealization 9) argues around running it rather than
running it. Both are elevated to mandatory below, matching how exp-091's
own audit applied R8 to EM's bracketing fix one cycle earlier.

**No Checkpoint criterion fires.** Every finding in this audit — the five
upheld critique attacks and the two Red-Team-original attacks (§3) — was
caught blind, at Phase 2, before any Phase 3 synthesis exists, matching
this program's own universal, standing discharge test (R6 through R15, and
every disclaimer-erosion instance's own first catch). None is a recurrence
of a previously "known, named, ignored" defect: RT-1's band-mistransfer
shape was caught and corrected within exp-091 itself one cycle ago (not
ignored, merely recurring in a new instance this cycle, caught here in
turn); RT-2's T27-contradiction is a first-time-shape finding (no prior
LOGBOOK entry names "Idealization 8-style settling claims must cite T27"
as an escalated, ignored lineage). **Checkpoint criterion 5** (two
consecutive non-advancing cycles): N/A — exp-091 was itself a
logbook-advancing PARTIAL (R15 adopted, the caution zone materially
revised), and this cycle, once the docket below lands, directly advances
the single most consequential open question R15 itself left standing (are
the `cpl=30` crossings actually located, and is the caution zone's own
foundation resolution-stable) — logbook-advancing by construction.

## 6. Overall verdict: **PROCEED-WITH-MANDATORY-FIXES**

The core deliverable — extending the crossing search to a data-justified
wider net, rebuilding the caution zone under two disciplined
counterfactuals, and testing whether `sigma_max` contaminates the PRIMARY
channel — is well-targeted, its own geometry/cost/statistical arithmetic
is sound everywhere independently checkable (§0), and Rank 2 in particular
is now a four-way independently-reproduced, essentially risk-free
deliverable. Nothing in this audit overturns the design's core. The docket
below closes seven real gaps, all fixable same-shift, at zero-to-trivial
additional cost, none requiring re-scoping this cycle's own budget.

### Mandatory-fix docket (apply before Phase 3 freezes; seven items — items 1–2 are load-bearing to this cycle's own PRIMARY deliverable, items 3–7 are real but non-load-bearing correctness/completeness fixes)

**Load-bearing:**

1. **Resequence Rank 3 before Rank 1**: run Rank 3's 6 calls first; branch
   Rank 1's `sigma_max` choice on Rank 3's own CONFIRM/REFUTE/NEITHER
   verdict (0.5 if CONFIRM; 1/3 if REFUTE; an explicit, disclosed scope
   decision if NEITHER) — zero additional wall-clock cost, independently
   confirmed (§0, §2). **Additionally disclose**, alongside this fix, that
   a Rank-3 REFUTE reopens Rank 1's own §2a net-placement logic (derived
   from uncorrected-article bracket data) for a future cycle, not merely
   the `sigma_max` value used this cycle (§2, Red Team's own addition).
2. **Extend Rank 1's lower net by two more `DENSE_ANGLES` points**
   (39.2°/39.4°, ~4 calls), on the direct, measured evidence that
   `delta_scene(40.2°)` already flipped sign by a magnitude comparable to
   the entire `40.0°→40.2°` approach at `cpl=20` (PHOTONICS, upheld and
   elevated to mandatory, §1.1) — independent of, and stronger than, the
   amplitude-inflation non sequitur, which should be struck or corrected
   in the same edit.

**Non-load-bearing, real, cheap:**

3. **Add a pre-registered CONFIRM/REFUTE band for `p_abs_w` and
   `ratio_abs_ext`** under Rank 3, mirroring exp-091's own (b2) convention
   (THERMODYNAMICS, upheld, §1.3) — zero additional FDTD calls.
4. **Correct the §6 Rank-3 justification text** so it no longer claims the
   reused `[0.3,3.0]`/`[0.1,10]` band was "established for the identical
   resolution-rescale question" — state plainly it is a repurposed,
   generic magnitude/sign tolerance, not evidence the sigma-correction and
   resolution-rescale questions are physically identical (Red Team, §3
   RT-1) — wording only.
5. **Rewrite Idealization 8** to argue from the depth-of-convergence
   margin at the three already-checked settling angles, with an explicit
   T27 cross-reference, rather than the blanket "not source-angle-
   dependent" claim this program's own T27 record already contradicts at
   a different operating point (Red Team, §3 RT-2) — wording only;
   optionally, at the Director's discretion, add one settling spot-check
   at the window-edge angle (42.0°) as cheap insurance, not required.
6. **Add exp-091's own Idealization 8** (the "no full 31-point R3 rebuild"
   half specifically — the R14(b) half is already carried in §7) to §8's
   list (VISION, upheld, §1.5) — wording only.
7. **Fix the print-parity gap before Phase 4**: add the one-line `print()`
   call for `netd_disclaimer`/`scope_note` so this cycle's own
   `run_output.txt` does not reproduce exp-091's exact defect (VISION,
   upheld, §1.5) — this cycle is the very "future cycle" §7 Tier 4 named
   as the deferral target; deferring it a second time inside the run that
   creates the artifact is no longer a first-instance gap.

No item above requires re-scoping this cycle's own budget; items 1–2
together add roughly 4 calls and zero net wall-clock time (§0, §2); items
3–7 are wording or already-computed-byproduct fixes at zero marginal
FDTD cost.
