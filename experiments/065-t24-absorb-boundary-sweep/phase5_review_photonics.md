# PHASE 5 — REVIEW · Panel Iteration 42 · Seat: PHOTONICS

*Reviewing exp-065 fresh, own charter: surface interaction, absorption
spectra, angular dependence, scattering cross-sections — is the proposal's
optical response coherent as stated, across wavelength and angle? Read in
full: `phase1_proposal.md`, all five `phase2_critique_*.md`,
`phase2_redteam_audit.md`, `phase3_synthesis.md`, `NOTES.md`,
`phase4_results.md`, `results.json`,
`settled_sweep_steps2800_diagnostic.json`, `design_geometry.py`. Numbers
below not taken on faith: re-derived independently from `results.json` and
the settled-sweep JSON where a committed artifact exists (see §2).*

---

## 1. Is the optical-response physics coherent as stated?

**Yes, on the mechanism this cycle actually engaged with — T21's edge-
diffraction picture — and the settling transient's own physical story is
consistent with that same mechanism, not a bolt-on excuse.**

The angular/wavelength scaffolding this cycle inherits (the two-taper-edge
Huygens fringe, period `P(θ)=λ/(A·cosθ)`, half-aperture `A=752` cells held
congruent across the `ABSORB` series) is this program's own independently
re-derived, Red-Team-vetted T21 result, correctly reused here, and the
Phase-2/3 handling of the one real new risk it created — three `ABSORB`
points landing on exact-integer-λ ratios at 600 nm specifically, the one
wavelength Block ARTICLE scores — was caught (PHOTONICS' own Phase-2
critique), independently reconfirmed by Red Team, and closed with a
correctly-chosen fourth point (`ABSORB=70`, verified non-resonant at all
three λ) before any FDTD call executed. That is the program working as
designed on an aliasing question, and P-VIS42-2a's clean CONFIRM (C70 falls
inside the C60/C80 bracket at all 6 cells) is a real, falsifiable result,
not a formality.

**The settling transient is not a generic "FDTD needs more steps" hand-wave
— it has the right qualitative signature for a grazing-incidence,
wide-aperture diffraction buildup, and I can independently ground its
timescale.** The mechanism this whole channel's `C_empty` structure is
attributed to (T21) is a coherent sum of contributions from a source
aperture with **half-width A=752 cells**. For a coherent sum over an
aperture that wide to reach its steady-state interference pattern at an
observation angle θ, the wave must have had time to traverse the
path-length spread between the aperture's center and its edges at that
angle — order `2·A·sinθ / S` steps (S≈0.700 cells/step, the Courant-limited
phase speed). At θ=40°: `2·752·sin40°/0.700 ≈ 2·752·0.643/0.700 ≈ 1381`
steps — strikingly close to the `STEPS=1400` this program has run this
channel at since Iteration 18. That is not a coincidence a bug would
produce: it says 1400 steps sits almost exactly at the aperture's own
coherent-buildup time at this angle, which is exactly the regime where a
transient reads large and doubling STEPS (to ~2× the buildup time) should
clear it — precisely what Diagnostic 2's four-point trend shows. The same
estimate at θ=35° gives ≈1233 steps — still comparable to 1400 — which I
used as a prediction and checked directly against committed data (§2,
below): the ±35° cells are **also** unsettled at 1400 steps, by an amount
comparable in absolute terms to ±38°/±40°, including a same-config **sign
flip** at 600 nm. The chosen title "±38°/±40°" is real but, on this
evidence, an underestimate of the affected window's true extent, not an
overstatement — the mechanism (aperture-transit time scaling with `sinθ`)
gives no reason for a sharp cutoff at 38°, and none is seen.

**Independent cross-reference, not noted anywhere in this cycle's own
record:** the direction of the residual (750 nm carries the largest
post-settling delta, per Diagnostic 3) is not a new observation for this
program — it is the SAME ordering ELECTROMAGNETISM/PHOTONICS flagged at
Iteration 19 (T21: "the best-fit scale c* grows monotonically with λ...
matching the λ-dependent causal-transit-margin idealization's own ordering
— thinnest settling margin at 750nm"), which named "a real FDTD
settling-margin test" as PHOTONICS'/EM's own #1 Tier-2 priority for
Iteration 20. I find no record that test was ever run (`LOGBOOK.md` never
reports a settling-margin FDTD result for the plane/tapered-source channel
between Iterations 20 and this cycle). **exp-065 backed into, and
confirms, a 22-iteration-old flagged risk that this program's own queue
named and then let lapse** — strong circumstantial support that this is
real, recurring physics on this channel rather than a one-off artifact of
this cycle's own padded-domain construction.

**Net: the optical-response physics — the fringe mechanism, its wavelength
scaling, and now the settling transient's own scaling with aperture
geometry and angle — is internally coherent and, where I can check it
independently, correctly characterized.** The one place the cycle's own
characterization is incomplete rather than wrong: it frames the settling
defect as an "±38°/±40°" phenomenon when the underlying mechanism (and my
own check of the committed ±35° rows) says it is a smoothly angle-dependent
one that happens to have been sampled most densely at ±38°/±40°.

---

## 2. Independent sanity-check of the settling finding

**Does a 4× reduction in `|C_empty|` at θ=40° between STEPS=1400 and 2800,
converging cleanly by 2800, make physical sense as a genuine transient?
Yes — and I verified the parts of it that are independently checkable
directly from committed data, not from `phase4_results.md`'s prose alone.**

**What I re-derived and confirms the record:**
- `block_sweep` rows (C40/C60, θ=40°, 600 nm, STEPS=1400) and
  `settled_sweep_steps2800_diagnostic.json` (STEPS=2800) both reproduce
  Diagnostic 1's table exactly: C40 −0.010965→−0.002802 (74.4%), C60
  −0.007721→−0.002442 (68.4%). **This is a solid, committed-artifact-backed
  result** — the "not padding-specific" claim holds on direct
  re-verification, not just on trust.
- `block_settle` in `results.json` independently confirms the single
  P-VIS42-11 scored point (C80/40°/600nm, 1400→2800, rel Δ=59.8%) bit-for-
  bit against the prose table.
- The qualitative signature — monotone-decreasing magnitude that goes flat
  (4200/5600 essentially identical to 2800, per the prose) — is exactly
  what a single dominant transient with characteristic time ~1000–1400
  steps should produce, and matches the independent aperture-transit
  estimate in §1 to within the right order of magnitude and at the right
  angle-dependence. A construction bug (coordinate error, wrong pad
  offset, aliased array indexing) would not typically produce a clean,
  monotone, angle-and-λ-graded convergence to a stable plateau that also
  matches an independently-derivable physical timescale — it would more
  plausibly produce a discontinuous jump, a resolution-dependent (not
  STEPS-dependent) artifact, or no convergence at all. None of those
  signatures are present.

**What would make me suspicious of a bug instead, checked against what's
actually on record:**
1. *Non-monotonic or oscillatory convergence with STEPS* — not present in
   the 1400→2800→4200→5600 trend as reported.
2. *A dependence on STEPS parity or some numerical coincidence rather than
   on physical transit time* — the trend's timescale matches my
   independent `2·A·sinθ/S` estimate to within ~10–15%, which is evidence
   *against* a numerology explanation.
3. *Failure to reproduce on the unpadded, 19-iteration-old anchor
   geometry* — checked directly (Diagnostic 1): C40 shows the **larger**
   of the two relative shifts, ruling out "artifact of this cycle's own
   novel padded-domain code," the most obvious bug candidate.
4. *A settled value that itself fails an independent identity* — not
   fully checked. The pad-only null (P-VIS42-5) was REFUTED at STEPS=1400,
   dominated by the same 750nm/+40° cell class, and was **not re-run at
   STEPS=2800** — this is the natural cross-check that a genuinely settled
   G40 should agree with a genuinely settled C40 (both are vacuum,
   G-2/`static_construction_identity` already proves this at the static-
   array level), and it is currently an open loose end, not a red flag.

**One finding of my own, not raised in `phase4_results.md` or any Phase-2
critique, that tempers confidence without undermining the physics:** the
4200- and 5600-step points that make Diagnostic 2's convergence trend read
as "clean" and "decisive" rather than merely "some reduction happened"
**exist only as typed numbers in `phase4_results.md`'s prose.** I grepped
the full experiment directory for `4200` and `5600`: they appear nowhere
in `run.py`, `results.json`, or any committed JSON — only in
`phase1_proposal.md`'s citation of exp-046 (a different check, on the beam
channel) and in this cycle's own prose table. This is precisely the class
of figure this program's own R4 house rule exists to police ("any
falsifier or self-consistency figure... MUST be produced by invoking the
actual committed function... never hand-typed"), and Red Team struck a far
less consequential figure (`0.00449`) for exactly this defect earlier in
this same cycle (attack 4). The 1400-step and 2800-step anchors of the
trend ARE committed and I independently verified them; the two points that
turn "a large reduction happened" into "clean, decisive convergence" are
not yet held to the same standard. **I do not doubt the physics — the
mechanism is independently motivated (§1) and the checkable half of the
trend is solid — but "decisive" is currently doing more work than the
committed record supports, and this should be closed (re-run and commit
4200/5600, plus the 750nm/C80 trend check `phase4_results.md` itself
names as needed) before it is cited elsewhere as an established
convergence result.**

**Bottom line: physically plausible as a genuine, mechanistically-grounded
transient, independently corroborated by an order-of-magnitude estimate
and a 22-iteration-old flagged risk — not what I'd expect from a
construction bug — but the specific claim of "clean, decisive" convergence
rests partly on two uncommitted numbers that should be reproduced before
the story is treated as fully closed.**

---

## 3. Verdict (this program's standard three)

**PARTIAL**, from PHOTONICS' own charter standard.

The optical-response characterization this cycle actually delivered — the
fringe/aliasing handling, the congruent-geometry construction, and the
settling transient's physical coherence — is sound science, well beyond
"support-with-changes" quality by Phase 4. But the cycle's own
pre-registered headline question (does T24's beam-channel boundary
systematic transfer to the plane channel as absolute or relative?) is
explicitly undecided — the frozen STEPS=1400 data says REFUTE/absolute,
the disclosed settled-STEPS follow-up says mostly CONFIRM/relative with an
unresolved 750nm residual, and the cycle's own text states plainly it does
not resolve which is right. A cycle whose headline instrument-uncertainty
question remains open, even while producing a large and well-grounded
secondary finding, is this program's own recurring PARTIAL shape (cf.
T10/exp-028, Iteration 5), not PROMISING.

---

## 4. Ranked top-3 candidate next directions

1. **Close the settling-convergence evidentiary gap, then use it.** Commit
   (not re-type) the 4200/5600-step points at θ=40°/600nm/C40 as
   code-produced output, extend the 4-point trend check to at least one
   750nm/C80 cell (where the residual concentrates and convergence is not
   yet shown) and one ±35° cell (where I found the effect is present, at
   comparable magnitude, with a sign flip). Cheap relative to the program's
   own timing failure modes, and it converts "the physics is plausible" into
   "the physics is proven" for the numbers everything downstream will cite.
2. **Re-verify `experiments/041-t20-angle-audit`'s own MAIN-block ±38°/
   ±40° rows (and, per my §1 finding, the flanking ±35°-adjacent angles) at
   a settled STEPS value**, and scope exactly which downstream numbers
   (T21's fringe fit, every T21/T24 citation since Iteration 18) actually
   move versus merely inherit an uncharacterized-but-small uncertainty.
   This program has run 19 iterations of angle-domain work on a channel now
   shown to have been read at ~3.9–9× its converged magnitude at some
   angles; the scope of what's affected is not yet known and is the single
   highest-value open question this cycle surfaced.
3. **Re-score T24's own original inheritance question (P-VIS42-2) cleanly
   at settled STEPS**, reusing this cycle's own already-built and
   already-validated machinery (the congruent ABSORB series, the
   non-aliased C70 point, the static-construction-identity gate) — the
   actual question this cycle set out to answer, now answerable cheaply
   once (1) is closed.

---

## 5. Checkpoint criterion — my own reasoned opinion (not a ruling)

**I do not think this fires Criterion 4 as PANEL.md defines it, though it
is close enough that Red Team should rule explicitly, not by omission.**
Criterion 4 is keyed to program-integrity *drift* — unfalsifiable claims, a
constraint quietly dropped, a violated propagation promise on an
already-merged artifact. What this cycle found is different in kind: a
genuine, previously-unmeasured physics gap in a settling-time assumption
that this program's own record (Iteration 19/20, T21) explicitly flagged
and ranked as a #1 priority 22 iterations ago, then deprioritized through
ordinary competing-priorities triage, not through a broken promise or a
suppressed finding. No Tier-W/Tier-A constraint-3 verdict was ever built
directly on the unsettled ±38°/±40° numbers as a pass/fail line (T24's own
citations are diagnostic, not verdicts) — so nothing "quietly dropped" a
scored constraint. This reads to me as this program's own T10/erratum
pattern (a real, load-bearing measurement correction, disclosed the moment
it was found, same-shift) rather than a Criterion-4 integrity failure. It
*does* warrant the forward-looking discipline T10 got: an explicit erratum
on `experiments/041-.../NOTES.md` and `results.json` (left uncorrected as
historical record, flagged not rewritten, per house convention) once the
re-verification in §4 item 2 lands.

---

*PHOTONICS, Panel Iteration 42, Phase 5. Fresh context; no other seat's
current-cycle Phase-5 output read.*
