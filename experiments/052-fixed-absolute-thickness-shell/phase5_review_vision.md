# VISION SCIENCE — Phase 5 Review, Panel Iteration 29 (exp-052)

*Fresh context. Read PANEL.md, LOGBOOK.md (RULED OUT R1–R5; LIVE THREADS
T1–T24, with emphasis on T2/T16/T21), PLAN.md's Current-state and the
LOCKED Iteration-29/30 entries, and the complete exp-052 record
(`phase1_proposal.md`, all five `phase2_critique_*.md` including my own,
`phase2_redteam_audit.md`, `phase3_synthesis.md`, `NOTES.md`,
`design_geometry.py`, `run.py`, `results.json`) before writing this.*

## Reading

The headline reproduces bit-for-bit from `results.json::fit`:
`C78_established = −0.7208684660449545`, `C_fixedabs(156) = −0.80668176727563`,
`C_fixedabs(312) = −0.84031612126995`. P1_deepening_vs_c78 = 0.085813
(matches direct subtraction); P2_delta_156_to_312 = 0.033634 (matches),
against my own Phase-2-widened band of ±0.00156 (`P2_R312_BAND` in
`design_geometry.py`, `= 2×T16_R156_BUDGET`) — **21.6× the band**, not
merely "over 20×" as the prompt characterized it; I get the same order
independently. P1/P2/P3 all read CONFIRMED in the committed
`fit` block, and I reproduce all three verdicts from the raw numbers
without needing to trust the stored verdict strings.

Every mandatory fix from Red Team's Phase-2 docket that touches my own
concerns landed: the r=312 band was widened exactly as I proposed
(`P2_R312_BAND`, not a re-measurement — Red Team's cheaper alternative,
which I accept in hindsight was the right call, since the actual delta
cleared even the widened band by more than an order of magnitude — a
tighter band would not have changed the verdict). The core-fill check
(fix 3, Director's redesign of Red Team's own item) reads
`core_fill_delta_theta0 = −1.13×10⁻⁶` (r=156) and `+1.13×10⁻⁶` (r=312) —
four orders of magnitude inside the ±0.02 band — so T9's "core content is
incidental" null is now shown, for the first time, to hold at
`r_in/r_out` = 0.692 and 0.846, not just the self-similar family's fixed
0.385. R-gate is clean (`R_coat = −2.88×10⁻⁷`, essentially machine-zero
against the 0.2% bar). The self-similar comparator was correctly
re-measured PEC-cored rather than cited hollow from exp-030
(`C_selfsim(156) = −0.730455`, `C_selfsim(312) = −0.732254` — both barely
moved from the historical hollow-core figures, consistent with the
core-fill null holding at the self-similar family's own smaller ratio).

**One item from Phase 2 — not mine — stayed genuinely open, disclosed as
such rather than smoothed over:** QUANTUM's coherent-vs-incoherent
bridge-gate concern (item 7). The Director's own Phase-3 ruling states
plainly that this was *not* closed this cycle, for a stated,
defensible reason (avoiding an under-tested new instrument built under
time pressure, per T11/T22's own cautionary precedent). I return to why
this matters more now, not less, below.

## Physical meaning

**The constraint-3 declination call (§4/NOTES.md: "T1 escape route: NONE
... no PASS/MARGINAL/FAIL language") is still correct, and this cycle's
own numbers make it more clearly correct, not less.** T2's frozen ladder
is `C_thr(L) = 0.005·max[1,(L/3)^−p]`, p∈[0.4,0.5] — even at the most
permissive scotopic corner this program has ever computed (T21's fringe
amplitude, 0.0237 at 750nm/θ=40°, was flagged as "4.7× VISION's own T2
photopic C_thr" and treated as a genuine contamination risk precisely
*because* it approached a threshold), the loosest number this program has
ever entertained as threshold-adjacent sits roughly two orders of
magnitude below |C|≈0.72–0.84. This object was never a threshold article
and the gap only grew (0.7209→0.8067→0.8403): scoring it against C_thr
would be a category error, and the proposal was right to say so from
Phase 1 through NOTES.md without hedging.

**But "not a threshold question" does not mean "not a vision-science
question" — the task's own framing is right to push here, and the
numbers support a real, if narrower, perceptual claim.** Converting Weber
contrast to a luminance ratio (`L_obj/L_bg = 1+C`): C78 → 0.279,
`C_fixedabs(156)` → 0.193, `C_fixedabs(312)` → 0.160. All three sit in
the regime where a human observer reads "obviously a dark/black object,"
but that is not the same as reading as indistinguishable steps. The
relevant literature is *suprathreshold contrast discrimination*, not
detection: the classical "near-miss to Weber's law" for contrast
increments (Legge & Foley, *J. Opt. Soc. Am.* 70:1458, 1980 — signal
thresholds scale with pedestal contrast roughly as a power law with
exponent near 0.6, not the naive Weber-fraction-constant assumption) and
a separate, more directly relevant anchor for *how dark is "as black as
it can get"*: Mantiuk et al.'s "The luminance of pure black" reports the
perceived-pure-black luminance ratio rising with surround brightness —
roughly 4.4% of surround at a dim (≈0.1 cd/m²) surround, but only
≈0.1% of surround at a bright (≈900 cd/m²) photopic surround (figures as
returned by WebSearch snippet, **not primary-source-verified this
cycle** — the fetch itself was blocked by the same network egress class
T18 has logged for six-plus iterations running against scholarly domains;
stated here as PLAUSIBLE-with-a-named-source, not PUBLISHED-and-checked,
same standard MATERIALS applies in `REALIZABILITY_MEMO.md`). Both this
cycle's luminance ratios (16–28%) sit comfortably *above* that
photopic "pure black" floor (≈0.1–1%), meaning neither reading is close
to saturating human blackness perception — the −0.72→−0.84 step is
plausibly still inside the range where a human would report the deeper
one as visibly darker/more complete, not a distinction without a
difference. I flag this as PLAUSIBLE, sourced but not verified — pinning
it tighter needs the primary-source check this program has been blocked
on since Iteration 13/14 (T18), not a new claim exp-052 can settle.

**The more consequential vision-science point is the one the task
specifically raises: depth of Weber contrast and angular extent of
"complete" shadow are different quantities, and this experiment measures
only the first.** The proposal's own mechanism narrative (§1/§3 of
`phase1_proposal.md`, carried unchanged into `NOTES.md`) is explicitly a
claim about geometry: "a fixed-width rim-leak channel becomes a shrinking
[angular] fraction of a growing silhouette." That is a claim about the
*spatial/angular extent* over which the silhouette reads near-complete
(→−1, T9's idealized bound) versus the diffuse, partially-transmissive
rim T9 originally characterized as a single point figure. But `C` as
scored here is one aggregate number per geometry — the instrument never
produces a radial or angular profile of *local* contrast from silhouette
center to edge. **The measured deepening trend (−0.721→−0.807→−0.840,
and — the sharper tell — decelerating at a slower rate than the
self-similar family's own −0.7209→−0.7305→−0.7322 plateau toward
C_∞≈−0.734) is consistent with, but does not itself directly demonstrate,
a growing angular fraction of near-complete blackness.** It is equally
consistent with a uniform deepening across the whole silhouette with no
change in rim proportion at all — the aggregate number cannot distinguish
the two. This is exactly the T16-style instrument gap my charter exists
to flag: no spatially-resolved silhouette instrument exists in this
program yet, and this cycle's own headline finding is the first result
whose stated *mechanism* depends on one.

**Why this matters for constraint 3's own visibility footprint,
independent of the Tier-A/Tier-W threshold question:** if the mechanism
argument is right, a real fixed-thickness ultra-black coating — the
realizable case this whole cycle exists to test, per MATERIALS' own
21-iteration-deferred claim — would present a *more* convincing,
harder-edged "hole in space" as the coated object gets physically larger,
not a softer one. That is a genuine reframe of what T8/T13/T14's
established self-similar-family citations have been used to argue: the
self-similar family's shallowing-toward-a-plateau was, on this reading,
plausibly an artifact of an unrealizable growing-thickness material law,
not a physical prediction about how a real coating looks at scale. The
scalar `C` result supports the *direction* of that reframe; a
spatially-resolved instrument would be needed to confirm the *mechanism*,
which is a different, sharper claim with real consequences for how this
program should read every future large-object silhouette citation.

## Argued next change

**Build a spatially-resolved silhouette-contrast profile instrument** —
local Weber contrast as a function of radial/angular position across the
object's own silhouette, not just the region-aggregate `C` this program
has used since Iteration 1 — to directly test whether the "shrinking
leak-channel fraction" mechanism is real or whether the aggregate
deepening is uniform. This is the concrete instrument gap the physical-
meaning section above identifies; it is a natural, cheap extension of the
already-validated `lab/ambient.py` machinery (same runs, different
post-processing: bin the existing field data by radial distance from the
silhouette edge instead of area-averaging it into one number) rather than
new FDTD machinery. I am not proposing this compete with the already-
LOCKED Iteration-30 slot (my own stage-10 temporal instrument) — it is a
separate, smaller-scope item for the ranked queue below.

**Does this result change my priority ranking for the still-unresolved
coherent-vs-incoherent bridge gate (QUANTUM's Phase-2 flag)?** Yes —
**it should be elevated, not left where it was.** Before this cycle, the
bridge gate's only validated point (exp-029, stage 11) sat at shell
fraction 61.5% (r=78, where the fixed-absolute and self-similar families
coincide), and the concern was academic: the measured cross-term
(+0.0224% aggregate) was small relative to what it was being asked to
license. This cycle's own mandatory, CONFIRMED result is scored at shell
fraction 30.8% (r=156) and, if the cost-gated leg is trusted, 15.4%
(r=312) — 2× and 4× further from the only validated point than this
program has ever asked the incoherent-sum approximation to cover — and it
now underpins the single largest, most load-bearing deepening number this
thread has ever produced (a 21.6×-over-band, T14-reversing result). The
qualitative *direction* of the finding is almost certainly robust to a
small coherent cross-term (the deltas are 100–1000× larger than the only
cross-term ever measured), but the *magnitude* — which is exactly what
licenses the "approaches −1, doesn't plateau" reframe above — is not
provably immune, and nobody has checked whether the cross-term itself
grows as the rim thins (a physically plausible direction QUANTUM's own
critique named). Higher stakes, same open gap: this belongs above where
it would have ranked before exp-052.

**Does it change my ranking for the still-deferred N33/finer-angular-
quadrature work (T16)?** Not the way the question might suggest — this
cycle's own magnitude (21.6× the widened band, itself already 2× T16's
measured budget) is far too large for angular-quadrature sampling noise
to be a live rival explanation, so I am **not** arguing N33 should jump
the queue *because of* exp-052's numbers. But Red Team's own Phase-2
audit of my critique surfaced a real, separate gap worth naming
explicitly: **T16's entire angular-quadrature uncertainty budget
(7.80×10⁻⁴) was measured exclusively on a near-null σ(I) OFF-state
article (|C|≈0.005) — never on an opaque/deep-shadow absorber, which is
the article class behind most of this program's constraint-3 citations,
including this cycle's own headline and the T1 wall figure itself.**
Whether the same angular-sampling sensitivity applies at |C|≈0.7–0.84 is
an unexamined assumption, not a measured fact, carried by analogy only.
This is cheaper and more targeted than a blanket N33 build: rerun the N9
vs. N17 comparison on the `absorber_fixedabs` r=156 object this cycle
already built, rather than (or before) the more expensive full N33
program.

## Ranked top-3 (Iteration 31+ — Iteration 30 already LOCKED to my own
stage-10 instrument, not re-ranked here)

1. **Rerun the stage-11 coherent-vs-incoherent bridge gate at the
   fixed-absolute shell's new, untested fraction regime** (30.8% at
   r=156, 15.4% at r=312 if that leg is trusted) — QUANTUM's Phase-2 flag,
   left explicitly open by the Director. Elevated above where it would
   have ranked pre-exp-052: it now licenses the program's largest
   confirmed deepening result, at a shell-fraction 2–4× further from the
   only validated point than ever asked of this instrument before.
2. **A targeted N9-vs-N17 angular-quadrature check on the opaque-absorber
   article class** (reuse the already-built `absorber_fixedabs` r=156
   object) — closes a real, previously-unexamined gap: T16's whole
   angular-sampling uncertainty budget has only ever been measured on a
   near-null σ(I) article, never on the deep-shadow class most of this
   program's citations actually are. Cheaper and more directly targeted
   than a blanket N33 build.
3. **The λ-generalization run (450nm or 750nm, r=156 only) for P-3's T14
   verdict** — PHOTONICS' concern, Red-Team-ruled REAL and LOAD-BEARING,
   closed this cycle only by re-wording (scoping P-3 to 600nm), not by
   measurement. Directly bears on whether the "harder-edged/more complete
   shadow at scale" reframe generalizes across the visible band (PANEL.md's
   own metrics table requires wavelength dependence for exactly this class
   of claim) or is a 600nm-specific coincidence of this shell's
   thickness-in-wavelengths ratio (1.92λ–3.2λ across the 3λ sweep, per
   Red Team's own arithmetic).

*Not re-ranked here but still live per PLAN.md's existing queue and not
superseded by anything above: the GEOM78 `ABSORB` FDTD sweep and
THERMODYNAMICS' `h_eff` re-derivation, both flagged by Red Team as
approaching unconditional-trigger territory on deferral count alone,
independent of this cycle's findings.*
