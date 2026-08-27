# PHASE 2 — CRITIQUE · ELECTROMAGNETISM · Panel Iteration 59 · exp-082

*Fresh sub-agent, blind to the other six seats' Phase-2 critiques this cycle.
Read PANEL.md, AGENTS.md, LOGBOOK.md (RULED OUT R1–R9, ESTABLISHED, LIVE
THREADS in full, T28's complete Iteration 46–58 history), PLAN.md's
Iteration-59 queue, and the complete `experiments/082-.../` directory
(`phase1_proposal.md`, `NOTES.md`, `run.py`, `results.json`,
`run_output.txt`, the x-wall refit and phase-convention-extension files),
plus `experiments/075-.../phase5_redteam_phase_convention_check.py`. Not
read: any other seat's `phase2_critique_*.md` this cycle.

**Independent verification performed, not asserted from memory:**
(1) spot-checked 3 of the 7 `C_empty` reproduction points (θ=36/39/42) by
loading `experiments/076-.../results.json::headline` myself and diffing
against `experiments/082-.../results.json::per_theta` — bit-exact, `0.0`
deviation, confirmed independently of the committed `max_dev=0.0` claim.
(2) Ran a second, independent settling check the proposal did not run:
`C40`, θ=38° (the angle contributing the single largest `delta_scene`
value, `+1.923×10⁻³`) with the article loaded, `STEPS=2800` vs `STEPS=4200`
— the historically-precedented settling-*closure* pair (exp-069 Block
MINI), not the committed check's `2800`-vs-`1400` pair, and a different
angle. Result: `C(2800)=-0.5643962`, `C(4200)=-0.5643960`, `rel_dev=
2.84×10⁻⁷` — three orders of magnitude tighter than the committed θ=39°
check's own `9.81×10⁻⁵`. (3) Computed the Pearson correlation between the
seven `delta_scene(θ)` and `delta_empty(θ)` values reported in
`results.json` — a check neither `phase1_proposal.md` nor `run.py` performs.

---

## 1. Reproduction and settling preconditions

**Reproduction precondition: real, but scoped narrower than its own framing
claims.** Independently confirmed bit-exact (§ above). But it only exercises
the `with_article=False` code path — the exact geometry/engine harness
(`dg065.CONFIGS`, `Sim`, `contrast_from_runs`) this sub-thread has run
unchanged since exp-069. The genuinely NEW code this cycle adds —
`build_article()`, materializing `obj_x`/`obj_y` as a physical PEC+shell
object for the first time in nine T28 cycles — is exercised by NEITHER the
reproduction check NOR any other independent gate. `max_dev=0.0` on the
empty leg says the harness is unchanged; it says nothing about whether the
article is correctly placed, non-overlapping with the boundary bands, or
behaving as the established absorber does once embedded in this specific
geometry. One reassuring fact I verified independently, not stated in the
proposal: `obj_x = BASE_OBJ_X + pad`, `obj_y = BASE_OBJ_Y + pad`
(`design_geometry.py` line 267–268) — the article moves congruently with
`PAD`, preserving this sub-thread's own congruent-series convention. That is
a real, structural reason to trust the placement is sane, but it is a fact
about geometry, not a verified fact about the FDTD output — no analog of
the established absorber invariants (wall reflection ≤0.2%, observer return
= camera floor) was checked for this specific embedding.

**Settling precondition: thin as pre-registered, corroborated by my own
extension, but still not R3-grade.** A single directional check at one
angle, one config, one STEPS pair understates what "a real article
introduces new path lengths" should worry about — my own independent
check (different angle, different STEPS pair, the historically-established
closure value) also came back clean, three orders of magnitude below the
primary metric's own scale. Two independent spot-checks passing cleanly is
better evidence than one, but it is still 2 of 14 (config×angle)
cells, both on the same config family's "safe middle" — neither tests `G40`
(the longer-round-trip config) nor the extreme angles (36°/42°) where
`delta_scene`/`delta_empty` diverge most in sign (§2).

---

## 2. The correlation gap — the load-bearing finding of this review

`results.json`'s own per-θ table lets `delta_scene(θ)` and `delta_empty(θ)`
be compared point-by-point, not just by peak-to-peak amplitude. I did:
**Pearson r = 0.031** — statistically indistinguishable from zero at n=7 —
and only 4 of 7 angles even share a sign. The `SURVIVES` verdict is scored
*entirely* on `ratio = ptp(delta_scene)/ptp(delta_empty) = 0.657`, a scalar
that is blind to shape. Two curves with unrelated θ-dependence but similar
amplitude produce the identical `ratio` a genuinely shape-matched pair
would. This matters specifically because of what this sub-thread has
already, independently, established: `P*=2.8421°` sits at only ≈2.8
samples/period against this cycle's own 1° step — the 7-point/6° window
captures "≈2.1 periods" (idealization 2's own words), a regime where a ptp
statistic is highly sensitive to exactly where the 7 samples happen to land
relative to the true peaks, and where even a small article-induced
path-length shift (exactly the mechanism the settling precondition exists
to worry about) would shift `delta_scene`'s phase relative to
`delta_empty`'s by an amount easily large enough to scramble a 7-point
Pearson r while leaving ptp amplitude roughly preserved. **So the near-zero
correlation is consistent with two different readings that this cycle's
own instrument cannot distinguish**: (a) a genuinely new, article-induced
interference structure at comparable scale but unrelated origin — SURVIVES
would then be the right label for the wrong reason; or (b) the SAME
`PAD`-tied mechanism, phase-shifted by the article's own presence — still
informative, but "rides through, phase-shifted" is a materially different,
more specific finding than "rides through, comparable-scale." Neither
`phase1_proposal.md`'s predictions nor its idealizations name this
possibility; it is a genuine gap, not a disclosed limitation.

---

## 3. Item 4's self-downgrade

**I agree with the self-downgrade, and it is the methodologically correct
call under this program's own standing discipline, not merely a cautious
one.** The `[CALIB]` block is precisely an energy-conservation check
(`|r_measured|=1.0` for a lossless real-n=1 spacer, independent of any
convention question) — its failure at 2 of 3 angles (`|r|` 6–9× low,
`peak_match=False`) means the forward/backward decomposition itself is not
reliably resolving the reflected component at this more-grazing range, for
reasons undiagnosed. Treating the nominal "6/6 favor `r`" tally as
resolving anything would repeat exactly the shape **R8** exists to forbid:
an unverified argument ("the extraction is probably still fine because...")
substituted for an independently computed check, on a flagged verification
gap that has already twice fired Checkpoint criterion 4 on this exact
sub-thread (exp-075, exp-077) for precisely this failure mode.

**A more charitable reading exists, but I decline to use it to move the
verdict, for the same R8 reason.** The measured-vs-code phase deviations at
the three angles (1.4°/17.6°/11.1°) are far smaller than the ≈50°–150°
angular separation between `r` and `conj(r)` at this range — suggesting the
`[CALIB]` failure may be primarily an *amplitude* leakage effect (plausibly
diffraction sidelobe contamination of the backward-wave bin, worse at more
grazing incidence) rather than a *phase*-scrambling one, which would leave
the "closer_to" classification more trustworthy than the blanket
"cannot be trusted" framing credits. I have not independently computed
this — it is exactly an "argument, not a check," the R8 shape — so it
belongs on the board as a named, affordable follow-up (diagnose whether the
degradation is phase-preserving), not as grounds to overturn "genuinely
inconclusive" this cycle.

---

## 4. A passivity/energy bound on SURVIVES's scale

No hard numeric bound is available: Weber contrast is a nonlinear function
of intensity, and the `PAD`-tied artifact is proven (Iteration 53,
`lab/fdtd2d.py` primitives) to be pure lossless-vacuum phase interference —
it carries no absorbed-power budget of its own to bound against via a
Poynting-theorem argument the way the article's own extinction does.

What passivity/superposition DOES license, qualitatively: this bench is
fully linear (no σ(I), no time-varying ε anywhere in this construction), so
the field with the article present decomposes exactly as
`E_no-article(θ) + E_scattered-by-article(θ)`. The established flagship
absorber extinguishes essentially everything incident on it (wall
reflection ≤0.2%, observer return = camera floor, beam-behind 1.5–1.8% —
LOGBOOK ESTABLISHED) and sits, per §1, congruently inside the object window
both configs share. A ratio at or near 1.0 (the artifact surviving
*unattenuated*) would be the more physically surprising reading, since a
near-total absorber occupying the window ought to remove at least some
coherent flux from any boundary-echo pathway that spatially threads near
it. A ratio near 0 (clean CANCELS) is the naively expected reading for a
pure background/boundary systematic under object-minus-flank subtraction.
**The measured `0.657` — partial, neither extreme — is not implausible in
scale on this qualitative reading**, though I stop short of calling it
positive evidence for the mechanism, given §2's unresolved shape question.

---

## 5. Steel-man (≤150 words)

This cycle finally exercises the real, article-loaded scoring channel every
constraint-3 citation actually uses, after six deferrals — and does so with
real discipline: the reproduction precondition is genuinely bit-exact (I
independently confirmed three points against `experiments/076-.../
results.json` myself), the pre-registered SURVIVES/CANCELS/INCONCLUSIVE
bands were frozen before the run, and the result lands centrally inside
SURVIVES, not near a boundary — not a marginal call dressed up as decisive.
The article's `obj_x`/`obj_y` moves congruently with `PAD`
(`BASE_OBJ_X+pad`), correctly preserving this sub-thread's own established
congruent-series geometry rather than introducing a silent new confound the
way the `PAD`/`ABSORB` conflation did at Iteration 48. Both discipline
items this program cares about most — pre-registration before running, and
reproduction against an already-committed number — were done, and done
at the tightest possible bar (`max_dev=0.0`), not merely "small."

## 6. Sharpest attack (≤150 words)

The `SURVIVES` verdict rests on a single scalar — `ptp` ratio — blind to
shape. I computed the Pearson correlation between the seven
`delta_scene(θ)` and `delta_empty(θ)` values `results.json` already
contains: **r=0.031**, only 4/7 signs agreeing — no detectable point-by-point
relationship between "the confound on the scoring channel" and "the
confound on the proxy channel" it is claimed to be. At only ≈2.1 periods of
the established `P*=2.8421°` fringe sampled at 7 points, this is exactly the
regime where a small article-induced path-length shift (the mechanism the
settling precondition itself names) can preserve `ptp` amplitude while
scrambling point-by-point correlation — so `ratio=0.657` cannot distinguish
"the same mechanism, phase-shifted" from "an unrelated new oscillation at
similar scale." `SURVIVES` may be the right label, but "comparable
amplitude" and "the SAME signal" are different claims, and only the weaker
one is established.

## 7. Verdict: **support-with-changes**

The finding is genuine, charter-relevant, and correctly discharges the
six-cycle tripwire — I would not oppose it reaching Phase 3. But the
headline "SURVIVES" language in `NOTES.md`/`phase1_proposal.md` should be
qualified: it establishes comparable-*scale* presence on the real scoring
channel, not confirmed shared-*mechanism* presence, until the correlation
gap (§2) is addressed. This is not a Checkpoint-4-shaped defect (nothing was
falsely claimed as independently verified; the gap is a genuine, disclosed-
by-omission methodological limit, not a defended wrong claim) — it is a
same-shift-fixable scoping correction, matching this sub-thread's own
non-firing precedent for honest, promptly-caught gaps (Iterations 51, 53,
55, 56).

## 8. The single parameter change that would flip my verdict

Add a lag-aware shape check — either a full-power re-score at the existing
31-point/0.2° window (this cycle's own idealization 2 already names this as
deferred, not new work) or, cheaper, a cross-correlation of `delta_scene`
against `delta_empty` over a small lag range at the current 7 points. A
peak cross-correlation materially above the raw `r=0.031` (e.g. >0.6) at a
small, physically explicable lag would resolve my concern and move me to
**support** outright — the amplitude-scale finding is solid either way;
only the "same mechanism" reading needs the extra check.
