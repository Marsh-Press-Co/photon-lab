# PHASE 5 — REVIEW · MATERIALS & METAMATERIALS · Panel Iteration 83 (exp-106)

*Fresh seat, blind to all other seats' current-cycle Phase-5 reviews. Charter:
sub-wavelength structure; what could physically realize the proposed optical
behavior; owns the realizability bound (published / plausible /
unobtainium-with-parameters). Read in full before writing: `PANEL.md`,
`LOGBOOK.md` (RULED OUT R1–R23; ESTABLISHED; Live Threads T1/T8/T9/T13/T14/T28
in full, including this seat's own exp-105 Phase-5 review, which proposed the
fixed-absolute-thickness discriminating control this cycle executes), the
complete exp-106 record (`phase1_proposal.md`, all five Phase-2 critiques,
`phase2_redteam_audit.md`, `NOTES.md`, `run.py`, `results.json`), exp-052
(`experiments/052-fixed-absolute-thickness-shell/`), exp-105's own `NOTES.md`,
and `experiments/034-floor-convergence-scale-bridge/REALIZABILITY_MEMO.md`
AMENDMENT 6/7 (read directly, not via any seat's quotation of it).*

## 0. Independent numeric verification (recomputed from `results.json`'s raw fields, not from `NOTES.md` prose)

**R_CORE/R_COAT ratios, both families, r=156/312** — from `geom_156`/`geom_312`/
`geom_156_fixedabs`/`geom_312_fixedabs`:
- self-similar r=156: 60/156 = 0.384615 (r=312: 120/312 = 0.384615) — held exactly
  at T9's own validated 0.385 anchor at *every* r, by construction (κ scales
  `R_CORE` and `R_COAT` together).
- fixed-abs r=156: 108/156 = 0.692308; r=312: 264/312 = 0.846154.
Both reproduce `phase2_redteam_audit.md`'s own cited "0.692"/"0.846" exactly.

**`shape_ratio_fixedabs`**: `item4_fixedabs.shape_ratio = 18.228333623646076`
→ "18.2283" reproduces exactly. **Self-similar `shape_ratio`** (recomputed
fresh this cycle, not reused): `p3_selfsim.shape_ratio = 19.787847024468125`
→ "19.7878" reproduces exactly, and itself reproduces exp-105's committed
19.79 to 4 significant figures (cross-cycle, cross-capture confirmation).

**`abs_ratio`**: recomputed directly from `kappa_windows_fixedabs`/
`kappa_windows_selfsim`: `0.000962183331795694 / 0.0008866623871477821 =
1.085174…` → matches `1.0851744088196273` exactly. `9.009267358438566e-06 /
4.79303718569495e-06 = 1.879657…` → matches `1.8796573048352636` exactly.

**Ledger, both families, r=156/312** — recomputed from `ledger_r156`/
`ledger_r312`'s own `sigma_abs`/`sigma_ext`/`core_power`/`radial_total`/
`box_a`,`box_b`-derived `sigma_ext`:
- `abs_ext_ratio` (σ_abs/σ_ext): r156 selfsim `249.017/480.688 = 0.518043`
  (matches `0.5180430284747772`); r156 fixedabs `279.661/560.199 = 0.499217`
  (matches); r312 selfsim `498.483/960.446 = 0.519012` (matches); r312
  fixedabs `588.022/1191.326 = 0.493586` (matches). All four sit within ~5%
  of T9's established ~0.51 anchor, in both families, at both r.
- `core_frac` = `core_power/radial_total`: `0.0/x = 0.000e+00` at all four
  (r, family) cells — matches exactly (`core_power=0.0` in every ledger block).
- `box_dev`: r156 selfsim `7.97e-05`→"0.0001"; fixedabs `7.58e-04`→"0.0008";
  r312 selfsim `4.90e-05`→"0.0000"; fixedabs `2.20e-04`→"0.0002" — all
  reproduce the rounded figures `NOTES.md`/`result_text` state, and all sit
  2+ orders of magnitude inside the established `≤0.12` box-independence bound.
- `p_abs_frac_diff` (`|σ_abs,fa − σ_abs,ss| / σ_abs,ss`): r156
  `|279.661−249.017|/249.017 = 30.644/249.017 = 0.123058` → matches
  `0.12305795332466973` ("0.1231"/12.31%) exactly. r312
  `|588.022−498.483|/498.483 = 89.539/498.483 = 0.179622` → matches
  `0.17962207739772926` ("0.1796"/17.96%) exactly.

**Verdict: every headline figure in this section reproduces exactly (machine
precision on every raw field checked) from `results.json`'s own primitives.
Zero R4-class defects found in the numbers I independently re-derived.** Gate
P0 and both reproduction checks (r=156/312, self-similar vs. exp-105's own
committed values) are `rel_dev=0.000e+00` — also independently confirmed by
direct inspection of `reproduction_r156`/`reproduction_r312`.

## 1. Does this cycle's own discriminating control settle the exp-105 Phase-5 question I raised?

**No — a real, but partial, advance. The primary discriminator remains
explicitly NOT-TRUSTED by its own author's own gate, and the one metric that
does clear cleanly shares the identical unresolved input the gate exists to
flag.**

The question I raised at exp-105 Phase 5 was concrete: holding `τ_shell`
fixed while `R_CORE`/`R_COAT` scale by κ forces the self-similar coating's own
**electrical thickness** to grow 4× (2.4λ→9.6λ) — a materials-physics
candidate mechanism for P3's accelerating collapse, additive to (not a
substitute for) the geometric z/z_R hypothesis, with an already-built,
zero-new-mechanism discriminating control (exp-052) sitting unused. This
cycle runs exactly that control. The result:

- `shape_ratio_fixedabs=18.2283` sits inside the pre-registered REFUTE band
  (≥14.8) — the same *direction* a clean read would give (geometric window
  effect dominates; growing electrical thickness is not the driver) — but
  `shape_ratio_fixedabs_trusted=False`, hard-gated, because r=312's own
  settling leg for `kappa_window` **never ran for either family**: the
  shared empty-scene pilot alone (103.28 min) exceeded the 90-minute
  per-leg abort threshold before either family's article pair could run.
  This is not a marginal caveat — `shape_ratio` is *defined* as
  `(k78−k156)/(k156−k312)` (`run.py::shape_ratio_fit`, confirmed by direct
  read), so the untested r=312 capture enters the headline number's
  denominator directly, for both families, not as a peripheral input.
- I checked whether this is also an R13/R14-style near-zero-denominator
  hazard (this program's own standing discipline for exactly this ratio
  shape) and it is **not**: `noise_flag.denom=8.82e-4` sits ~3.3× above
  `noise_flag.noise_floor=2.66e-4` for self-similar (`9.53e-4` vs `2.89e-4`,
  ~3.3× also for fixed-abs) — `noise_dominated=False` at both, correctly.
  The open risk here is categorically different from R13/R14's arithmetic
  fragility: it is a genuine, unresolved **settling/convergence** question
  about the raw r=312 field itself, which costs new FDTD wall-time to close,
  not a statistical recheck. Worth being precise about this distinction
  going forward — this cycle's own NOT-TRUSTED flag should not be read as
  "R13/R14 fired"; the noise-floor gate R13/R14 discipline calls for was run
  and passed cleanly.
- PHOTONICS' own sharper, ungated `abs_ratio` test (mandatory fix 2) does
  clear its pre-registered factor-of-2 band cleanly at both r (1.0852,
  1.8797), and — because it compares two families' raw `kappa_window` at the
  *same* r rather than differencing across r — it does not inherit
  `shape_ratio`'s own denominator-fragility shape. This is real, additional,
  corroborating evidence for geometric-window dominance, and I weigh it
  accordingly: two independent statistics, built from the same raw
  captures by two different constructions, both point the same direction.
  But two qualifications matter, and neither is stated in `NOTES.md`'s own
  framing ("independent of the settling question above"): **(a)** `abs_ratio`
  is built from the identical, never-settling-tested r=312 raw captures —
  "not gated by `..._trusted`" is a scoring-pipeline choice (this statistic
  was never wired to the trust flag), not evidence that the underlying
  capture is itself converged. **(b)** `abs_ratio(312)=1.8797` sits at 94%
  of its own 2.0 boundary — a thin margin. Given this cycle's own ledger
  independently confirms a real, non-trivial (12–18%) cross-family
  divergence in absorbed power at the *settled* r=156 pair (§2, below), it
  is not established that a hypothetical settling correction at r=312 would
  shift both families' `kappa_window` by the same *relative* amount — if it
  does not, `abs_ratio(312)` could move toward or past 2.0. This is not
  shown to happen; it is also not ruled out, and the write-up's framing
  ("independent of the settling question") overstates the independence.

**Net: PARTIAL, not settled.** This cycle turns exp-105's single, entirely
SCORED-BUT-CAVEATED shape_ratio into two mutually-corroborating readings —
real progress, and the r=312 primary-leg data (unlike the settling leg) did
commit, so this is not a null cycle. But the cycle's own stated hypothesis
("closing all four gaps lets P3's own accelerating collapse finally be
TRUSTED or REFUTED as physics") is not achieved: the discriminator itself
remains explicitly untrusted, and the supplementary metric that clears rests
on the same untested foundation it wasn't built to test.

## 2. The 12.31%/17.96% ledger divergence: physically sane, or something the ledger check's own purpose should have caught?

**Physically plausible in direction and mechanism — but large enough that
the pre-registered consequence attached to it (three-way reclassification)
should have fired, and did not.**

Both families hold `τ_shell=24.0` exactly (independently re-verified, §0),
so any Beer–Lambert-style transmitted-intensity comparison would be
identical between families. `kappa_window`'s signal is not that dead
channel, though — it is near-field diffraction around the shell boundary,
governed by *gradient steepness*, which `τ_shell` alone discards:
self-similar's `sigma_max` falls to 0.25/0.125 at r=156/312 (a gradual,
longer-path profile) while fixed-abs holds `sigma_max=0.5` fixed at every r
(a steep, abrupt profile, always over the same 48-cell/1.44µm path) —
exactly the confound THERMODYNAMICS' own Phase-2 critique named and the one
this cycle's ledger check was built to price.

My own re-derivation (§0) shows `abs_ext_ratio` (σ_abs/σ_ext) stays tightly
clustered near T9's established ~0.51 anchor in **both** families at **both**
r (0.518/0.499/0.519/0.494 — all within ~5% of each other and of the
anchor), and `core_frac=0.000` exactly at every cell. That is a genuinely
new, positive finding for this seat's own charter, worth stating plainly:
**T9's "PEC core stays energetically incidental" finding now generalizes,
for the first time, past its only-previously-validated `R_CORE/R_COAT=0.385`
anchor out to 0.692 and 0.846** — the core does not become a reflection
leak even at nearly double and better-than-double that ratio. This should
be stated as a positive, not merely a "sanity pass," in any Learned section.

But the *absolute* cross-sections diverge substantially: fixed-abs's
`sigma_ext` exceeds self-similar's by 16.6% at r=156 (560.2 vs 480.7) and
24.0% at r=312 (1191.3 vs 960.4), with `sigma_abs` diverging by the reported
12.31%/17.96%. Since `R_COAT` is *identical* between families at each r,
this is not a footprint-size effect — it is the steeper-gradient shell
behaving, in aggregate, more like an abrupt/PEC-like scatterer (larger
effective diffraction cross-section), consistent with this program's own
established T9/T10-era finding that abrupt boundaries extinguish/diffract
more than graded ones. **I read this as a real, physically-motivated,
non-pathological effect — not evidence of a broken construction** (closure,
box-independence, and core-concentration are all clean at every cell,
independently confirmed in §0). That is the "physically sane" half of the
question.

The half that is *not* adjudicated, and should be: **THERMODYNAMICS' own
Phase-2 flip condition (adopted into `phase2_redteam_audit.md`'s mandatory
fix 1) pre-registered an explicit consequence for exactly this outcome** —
*"if fixed-abs and self-similar's `p_abs`/`sigma_ext` fractions land within
~10% of each other at matched r, treat item 4's two-hypothesis framing as
adequately clean; if they diverge materially, report `shape_ratio_fixedabs`'s
CONFIRM/REFUTE bands as **three-way ambiguous** (thickness-law vs.
core-reflection/gradient-steepness vs. both), not a clean binary."* The
observed 12.31%/17.96% **exceed** that ~10% line at both r. But
`item4_fixedabs.classification` in `results.json` reads only
`"REFUTES-electrical-thickness-growth-hypothesis (NOT-TRUSTED — r=312
MARGINAL/unsettled)"` — the r=312-trust caveat is applied, but the
three-way-ambiguous reclassification the mandatory fix specified for a
material divergence is not, anywhere in `predictions_text`, `result_text`,
or the classification string itself. `NOTES.md`'s own Result section
explicitly declines to close this: *"whether 12–18% is 'physically sane'…
or itself informative is not adjudicated here."* This is a genuine gap, not
a minor wording issue: the cycle's own Panel record states *"All 7 of Red
Team's mandatory fixes ADOPTED in full"* and names no override touching
mandatory fix 1's interpretation clause — yet the specific, falsifiable
consequence that clause attached to a >10% divergence was narrowed, during
Phase-3 synthesis, to "a sanity check on concentration/box-independence"
only (Setup's own description), with the cross-family delta demoted to "no
pre-registered pass/fail band was frozen for this specific quantity." Given
the data landed exactly in the branch that consequence was written for,
this now matters: **item 4's own headline classification should read
three-way ambiguous (thickness-law vs. gradient-steepness vs. both), not a
bare REFUTE label with only a trust caveat appended.** This does not
overturn the (already NOT-TRUSTED) verdict, but it changes what a future,
settled version of that verdict would actually mean, and it is exactly the
kind of "a mandatory fix's own specified consequence quietly narrowed
between Phase-2 adoption and Phase-3 freeze" gap this program's R16/R19/
R21/R23 lineage exists to catch — see §3 below.

## 3. Gaps, inconsistencies, and one correction to my own prior-cycle review

**(a) A mandatory-fix consequence dropped between Phase-2 adoption and
Phase-3 freeze (§2, above).** Closest standing-rule analogs: R21 (a
persisted sidecar finding's own headline must be stated in Result prose, not
merely computed/persisted) and R17 (a tolerance/bracket's own justification
must be checked against precedent, not silently redefined) — this is
adjacent to both but distinct: the *number* (12.31%/17.96%) is stated
prominently in Result; what did not survive is the *interpretive
consequence* Phase 2's mandatory fix attached to it once that number
exceeded its own named threshold. I recommend the Director treat this as a
disclosed gap requiring a same-shift correction to `item4_fixedabs`'s own
classification string and to `result_text`, and flag it for explicit ruling
on whether it approaches Checkpoint criterion 4 (a mandatory fix the Panel
record states was "ADOPTED in full," whose specific pre-registered
consequence did not, in fact, survive into the frozen document, discovered
only because the exact condition it was built to catch actually occurred).

**(b) A correction to my own seat's prior-cycle finding, caught by
independently re-checking my own citation rather than trusting it forward.**
My own exp-105 Phase-5 review (§3, ranked-#2 recommendation) argued the
r=78/156/312 bench-scale absolute thicknesses (1.44/2.88/5.76µm) sit
"comfortably inside the µm–mm range this program has already cited as
achievable by real ultra-black coatings," and recommended splitting the
blanket UNOBTANIUM tag so the bench geometries themselves would read as
plausibly realistic, separate from the (unobtainium) scaling law. I
independently re-read `REALIZABILITY_MEMO.md` AMENDMENT 6 (Iteration 38,
exp-061 — 44 iterations before exp-105, and specifically scoped to this
exact construction) directly, not via any other seat's quotation of it, and
it says the opposite: *"real CNT-forest/Vantablack-class record-blackness
coatings run 100–500µm… 70–350× this construction's own 1.44µm shell… this
gap alone decides the tier."* My own prior review's "µm–mm range… comfortably"
language was citing a broad, informal Iteration-7 (exp-030) desk figure
without checking whether the program's own later, rigorous, literature-
sourced Amendment 6/7 had already sharpened it for this exact geometry —
the identical failure shape Red Team's Attack 6 caught in *this* cycle's
own MATERIALS Phase-2 critique (a since-superseded rate-axis claim), one
cycle later, on the same realizability question. **This is now the second
documented instance of that exact shape** (a MATERIALS-seat citation of a
prior-program figure without checking a later, superseding cycle),
sharpening the "not yet a rule, flagged forward" caution
`phase2_redteam_audit.md` names at its own close. exp-106's own Realizability
note (mandatory fix 4, Red Team's replacement text) gets this right —
independently verified here against the primary source, not merely trusted
because Red Team cited it — but my own prior review's recommendation is
still sitting, uncorrected, in exp-105's own Tier-2 queue ("splitting the
blanket UNOBTANIUM tag into scaling-law vs. absolute-thickness sentences").
**If that Tier-2 item is ever executed using its original framing, it would
reintroduce the exact stale claim this cycle's own Red Team just corrected.**
Flagging this explicitly so it is not silently inherited.

**(c) A precision gap in exp-106's own realizability note, not an error.**
"Self-similar's absolute thickness grows with r… and is therefore
marginally, not substantially, closer to the real range at larger r" is
true as a tier statement (UNOBTANIUM at every r, unchanged) but understates
the numeric trend on the thickness axis alone (69.4×→17.4× gap, r=78→312 —
a real 4× narrowing) and does not engage the RATE axis's own r-dependence
at all. A first-order estimate (not computed this cycle, offered here as a
flagged, testable follow-up, not a claim to trust): Amendment 6's own
honest, Im(n)-weighted `α≈1/174nm` figure was derived at this construction's
`sigma_max=0.5`/1.44µm profile (i.e., the r=78/fixed-abs-at-any-r case); if
the honestly-integrated local absorptivity scales roughly with `sigma_max`
under a fixed, self-similar profile *shape* (a reasonable but unverified
first-order assumption for a weakly-lossy graded medium), self-similar's own
rate-axis gap to the best real CNT-forest figure (`α≈2.28×10³cm⁻¹`, a 25.2×
gap at r=78) would *narrow* in step with the thickness-axis gap — to
roughly 6× at r=312 — rather than stay fixed or worsen. If that holds, both
of MATERIALS' realizability axes are converging for self-similar as r
grows, not just the thickness axis the note currently names — a materially
different, and cheap (zero-FDTD, analytic), story than "marginally, not
substantially" conveys on its own. I flag this as an open, directly
testable MATERIALS-charter item, not a correction to trust yet — I have not
performed Amendment 6's own detailed Im(n) integration at the new
`sigma_max` values, only noted the scaling argument that motivates checking.

**(d) The seventh consecutive `delta_scene` R3-vs-R4 deferral** is correctly,
explicitly re-justified in writing this cycle, citing the Iteration-51
no-seventh-cycle precedent — procedurally clean. I note only that this
file's own language ("Iteration 84… must either execute… or formally retire
it") now sets a hard tripwire for the very next cycle on a sub-thread with
its own history of repeated deferral-tracking gaps; worth the Director
flagging explicitly rather than letting it compete informally against
whatever Iteration 84 proposes next.

## Verdict: CONFIRM-WITH-GAPS

Every number I independently re-derived reproduces exactly (§0) — this is a
clean, honestly-instrumented cycle with no R4-class defect found in its own
record. The floor-gate and r=156 settling legs both closed cleanly, exactly
as designed, and the cost-gating machinery correctly and transparently
deferred the r=312 settling leg rather than either skipping it silently or
blowing the wall-clock budget to force it through. But the cycle's own
central claim — that closing these four gaps lets P3's accelerating
collapse be TRUSTED or REFUTED as physics — is not fully earned: the
discriminator itself stays explicitly NOT-TRUSTED, the one ungated
corroborating metric shares an unaddressed dependency on the same untested
capture, and a real, pre-registered interpretive consequence for the
ledger's own >10% divergence finding did not survive into the frozen
Result/classification text even though its own triggering condition was met.

## Ranked top-3 candidate directions for Iteration 84 (MATERIALS' own perspective)

1. **Close the r=312 settling leg on `kappa_window`, both families — the
   single missing precondition for trusting or refuting item 4's own
   headline finding.** The blocker was cost, not design: the shared
   empty-scene pilot alone (103.28 min) exceeded the 90-minute per-leg
   threshold before either family's article pair could even attempt to
   run. Since the two families share an identical r=312 domain/CFL/
   absorbing-boundary construction (only `R_CORE`/`sigma_max` differ), a
   physically-motivated settling-time estimate extrapolated from the
   already-measured r=78/156 decay behavior (rather than a blind,
   doubled-STEPS empirical re-probe) is the cheapest realistic route to
   closing this without a second 90-minute-plus pilot.

2. **Apply THERMODYNAMICS' own dropped mandatory-fix-1 consequence,
   same-shift, zero new cost:** reclassify `item4_fixedabs`'s own
   classification string and `result_text` to state the finding as
   three-way ambiguous (geometric z/z_R vs. thickness-law vs.
   gradient-steepness/core-reflection, or some combination), given the
   observed 12.31%/17.96% divergence exceeds the ~10% line that
   consequence was pre-registered against — bringing the frozen record
   into alignment with what the Panel record claims was adopted in full.

3. **Correct exp-105's own Tier-2 "split the UNOBTANIUM tag" queue item
   before it is executed**, using AMENDMENT 6/7's precise figures
   (100–500µm required, 1.44–5.76µm delivered, 17–70× short at every
   tested r — not the broader, superseded "µm–mm range… comfortably"
   framing my own prior-cycle review used) — and, opportunistically, run
   the cheap analytic (zero-FDTD) check of whether the rate-axis
   realizability gap narrows in step with the thickness-axis gap across
   the r-family (§3c), turning "marginally, not substantially" into an
   actual number on both of this seat's own realizability axes.
