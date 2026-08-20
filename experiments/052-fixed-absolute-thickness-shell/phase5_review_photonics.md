# PHOTONICS — Phase 5 Review, Panel Iteration 29 (exp-052)

*Fresh context. Read `PANEL.md`, `LOGBOOK.md` (RULED OUT, LIVE THREADS in
full, with T9/T13/T14/T16/T21 read closely), `PLAN.md`'s Current-state and
the LOCKED Iteration-29/30 entries, and the complete exp-052 record
(`phase1_proposal.md`, all five `phase2_critique_*.md`, `phase2_redteam_
audit.md`, `phase3_synthesis.md`, `NOTES.md`, `design_geometry.py`,
`run.py`, `results.json`) before writing this. No other seat's Phase-5
review seen.*

## Reading

**Every headline number reproduces from the actual committed artifacts,
independently, not from prose.** I ran `design_geometry.py` directly
(`python3 design_geometry.py`) and confirmed its own printed assertions
pass with no error: `r_in_fixedabs(78)=r_in_selfsim(78)=30`,
`sigma_max=0.5` at both, `τ_shell=24.0` at every r∈{78,156,312} in both
families — **P-0 verified by execution, not by reading the code and
trusting it compiles.** I independently computed the wavelength-swing
arithmetic myself: `1440nm/450nm=3.2λ`, `/600nm=2.4λ`, `/750nm=1.92λ`,
matching the proposal and Red Team's audit exactly.

I re-invoked `lab.ambient.contrast_from_runs` myself, cold, against the raw
per-angle flux profiles stored in `results.json["block"]`, not against the
precomputed `results.json["fit"]` block — same numbers to full float
precision: `C_fixedabs(156)=-0.80668176727563`,
`C_selfsim(156)=-0.7304552322383192`,
`C_fixedabs(312)=-0.84031612126995`,
`C_selfsim(312)=-0.7322544463081008`. These match the task brief's cited
figures (`-0.72087→-0.80668→-0.84032` and `-0.72087→-0.73046→-0.73225`) to
the stated precision. `C78_ESTABLISHED["absorber"]` in exp-030's own module
is `-0.7208684660449545` — the task brief's `-0.72087` and NOTES.md's
`-0.7209` both round correctly from it; the Phase-1 proposal's own
`-0.7211` (Red Team's Attack 6b, item 4 in the accepted-fixes docket) is a
genuine transcription slip, corrected before freeze — I confirm the
correction is what actually shipped in `design_geometry.py`
(`C78_ABSORBER_ESTABLISHED = dg30.C78_ESTABLISHED["absorber"]`, imported
not hand-typed).

**The empty-scene floor cross-checks bit-exact against exp-030's own
independent record**, which I take as real evidence the domain reuse
claimed in NOTES.md idealization 3 is genuine, not just asserted: this
cycle's own new θ-sweep of `"empty"` at r=156/312 produced
`C_empty(156)=-0.0012113954918918646` and
`C_empty(312)=-0.00028259705918531886`; grepping exp-030's own
`results.json` finds `floor156/delta_C = -0.0012113954918918646` and
`floor312/delta_C_N9 = -0.00028259705918531886` — identical to every
printed digit. That is a stronger, unclaimed confirmation than "inherited
by argument."

**P-5 (θ=0 core-fill check) verified**: `core_fill_delta_theta0` =
`-1.133×10⁻⁶` (r=156) and `+1.126×10⁻⁶` (r=312), both ~4 orders of
magnitude inside the ±0.02 band — genuinely decisive at θ=0. **R-gate
(P-4) verified**: `R_coat=-2.88×10⁻⁷`, indistinguishable from the ideal
zero, comfortably inside ≤0.002.

**One thing I did NOT need to re-derive but did check**: `run.py`'s own
`run_fit()` carries a disclosed, self-caught comment flagging that an
earlier draft scored P-1 against stale `-0.7350/-0.7305` bands (leftover
from the raw Phase-1 draft, superseded by NOTES.md's actually-committed
`-0.7255`/`C78` bands) — fixed before the shipped scoring ran, and stated
as non-load-bearing since the measured value clears either band by a wide
margin. This is exactly the class of defect **R4** (this program's own
house rule) exists to catch, and it was caught here at fit time rather
than becoming a ninth recurrence. Worth noting for the record, not a new
finding.

## Physical meaning

**The mechanism argument is internally coherent and the Phase-2/Phase-3
process caught the right things.** Holding shell thickness fixed in cells
(hence in physical nm, since `dx=30nm` is held fixed across this bench's
own multi-λ convention) while `r_out` grows is a clean, single-variable
geometric-law test once `τ_shell` is confound-controlled at 24.0 in both
families (verified, not just asserted) — Red Team's own catch that the
comparator family was hollow-core and uncorrected was the right thing to
flag and the right thing to fix by re-measuring at the full N9-ambient
level rather than patching a number. I have nothing to add to that
process; it was done correctly.

**Whether the *effect size* is coherent is a separate question, and here
I have a finding none of the five blind Phase-2 seats or Red Team's audit
raised: the deepening rate is decelerating, and by an amount worth
watching.** Using `1+C` as the natural "distance from a perfect silhouette"
residual: `1+C(78)=0.2791`, `1+C_fixedabs(156)=0.19332`,
`1+C_fixedabs(312)=0.15968`. The step 78→156 removes `0.0858` of residual;
the step 156→312 removes only `0.0336` — less than half, despite `r_out`
doubling both times. A naive "fixed-width leak channel becomes a shrinking
angular fraction" argument (leak fraction ∝ 1/r_out, since the leak
channel's absolute width is pinned to the fixed 48-cell shell) predicts
the residual should roughly *halve* at each doubling — it does at
78→156 (ratio 0.693, close to the naive 1/2, though not exact) but only
drops to ratio 0.826 at 156→312, well short of halving. **This is
precisely the qualitative signature (a deepening step that flattens with
scale) that historically preceded T14's own discovery in the self-similar
family** — there the sqrt-law and ceiling-law fits both found a C∞
parameter that undershoots −1. I am not claiming the fixed-absolute family
repeats T14's failure — P-1/P-2/P-3's own falsifiable bands are cleared by
wide margins (17× and 21× the required thresholds respectively, computed
from the numbers above) and REFUTED is nowhere near triggering. But a
2–3-point family scored only against inequality thresholds ("deepens by at
least X") cannot distinguish "converges cleanly to −1" from "converges to
some C∞ that is much closer to −1 than the self-similar family's, but
still short of it" — and the deceleration I measured is consistent with
either reading. This is a coherence question squarely inside my charter
(is the magnitude of this optical response internally consistent with the
stated mechanism, or does it show early signs the mechanism is
incomplete?) and it is currently unresolved.

**The single-λ scope is a real, load-bearing gap, and I agree with
Phase 2's PHOTONICS seat and Red Team's ruling that it is the correct
priority, for reasons beyond what was argued at Phase 2.** The proposal's
own mechanism narrative is explicitly a thickness-in-wavelengths argument
(§1/§3), yet is tested at exactly one λ where that ratio happens to be a
clean 2.4λ. This program has direct, on-the-record precedent for treating
such coincidences with suspicion: **R2** (ruled out) found a "shell = 3λ"
feature that looked like a real standing-wave law at one geometry
(`r2=90`, 600nm) and evaporated at every other geometry and every other
integer multiple tested (exp-018/exp-019/exp-022); **T21**'s own governing
fringe period is λ-dependent in a way that is *not* monotonic in the
intuitive direction (600nm sampled nearest its own Nyquist limit, giving
the cleanest-looking signal for reasons unrelated to the underlying
physics being "special" there); and this program's own prior PHOTONICS
Phase-5 finding (T21 addendum, Iteration 19) is that the best-fit
diffraction amplitude scale `c*` grows monotonically and non-trivially
with λ (1.81/2.74/3.23 at 450/600/750nm). None of these prove the
fixed-absolute deepening is a 600nm-specific artifact — but they are three
independent, on-the-record instances of this exact bench producing
λ-dependent behavior in near-field/rim-diffraction channels that a
single-wavelength reading cannot rule out, and they are the concrete
reason I would not treat P-3's CONFIRMED verdict as safe to generalize
without a measurement. Phase 3's resolution (scope the language to
600nm-only rather than run a new λ) was the right cost/rigor tradeoff for
*this* cycle, but it leaves the generalization question genuinely open,
not merely deferred as a formality.

**The θ=0-only core-fill check (P-5) is decisive at the one angle least
likely to expose a core-content effect.** The mechanism this whole cycle
argues about is a *grazing/tangential* leak-channel effect — the angles
where a ray's chord through the graded shell is shortest, and where any
interior structure would have the most geometric opportunity to matter.
T9's null was itself never validated above `r_in/r_out=0.385` before this
cycle (confirmed independently in `design_geometry.py`'s own printed
ratios: 0.3846/0.6923/0.8462), and this cycle's own core-fill check, while
a genuine and useful extension of that ratio, only tests it at boresight.
I read the P-5 CONFIRMED result as real evidence T9 survives at these
ratios *at normal incidence* — not yet evidence it survives at the ±25°/
±35° angles that actually feed the N9 ambient sum whose deepening is this
cycle's headline. This is disclosed in NOTES.md idealization 5, correctly,
so it is not a hidden gap — but it is the second-most-consequential open
angular question in this record, after wavelength.

## Argued next change

**Run the r=156 leg of both families (fixed-absolute and self-similar,
PEC-cored, same N9 instrument, same domain) at 450nm and 750nm.** This is
the cheapest available test of the single most load-bearing open question
in this cycle's own record: it directly answers whether the deepening
mechanism is a general property of fixed-absolute-thickness shells or a
600nm/2.4λ-specific coincidence, in the same sense R2 turned out to be a
`r2=90`/3λ-specific coincidence rather than a portable law. Cost is small
relative to what has already been spent — exp-030's own r=156 rate
(~40–84s/run) puts a comparable 28-run block at the same ≈20–35 minutes
this cycle's own r=156 leg took, ×2 for the two new wavelengths, and the
domain-construction machinery (`design_geometry.py::GEOM`, the N9 angle
set, the R-gate idiom) is already built and reused verbatim — no new
instrumentation, no new gates to design. If the deepening holds in
direction and rough magnitude at 450/750nm, P-3's program-level T14
verdict earns the generalization Phase 3 explicitly declined to claim this
cycle; if it doesn't (or reverses, per T21/PHOTONICS' own λ-ordering
precedent), that is itself a significant, falsifiable finding about
exactly which physical regime this fix genuinely operates in.

## Ranked top-3 (Iteration 31+; Iteration 30 is locked to VISION's stage-10 instrument)

1. **The λ-generalization run above (450nm + 750nm, r=156, both families).**
   Highest priority: directly closes the one gap that determines whether
   this cycle's finding is a program-level resolution of T14 or a
   single-wavelength result, cheap relative to what is already committed,
   and grounded in three independent on-the-record precedents (R2, T21,
   Iteration-19's `c*(λ)` finding) for why this specific bench should not
   be assumed λ-flat in exactly this kind of channel.

2. **A third scale point (or a proper functional-form fit against T14's own
   established sqrt-law/ceiling-law templates) for the fixed-absolute
   family.** The deceleration I measured (residual-removal ratio 0.693 at
   78→156 vs. 0.826 at 156→312 — falling short of the naive 1/2 the
   mechanism argument implies) is not itself alarming against this
   cycle's own thresholds, but it is exactly the shape that preceded T14's
   discovery in the self-similar family, and two new points plus one
   inherited anchor cannot distinguish "converges to −1" from "converges
   to a smaller-but-nonzero C∞." A fourth point (r=624, cost-gated exactly
   per this cycle's own r=312 precedent) or the T14 sqrt-law/ceiling-law
   fit applied to the existing three points would settle which reading is
   correct without new machinery.

3. **QUANTUM's deferred coherent-vs-incoherent bridge-gate rerun at the new
   shell-fraction regime (fix 7, explicitly NOT closed this cycle).** Lower
   priority than 1–2 because it is a different seat's primary instrument
   concern, but it bears directly on my own charter secondarily: the N9
   incoherent-sum instrument that produced every number I verified above
   was only ever empirically licensed at shell-fraction 61.5% (exp-029,
   r=78), and this cycle's own headline reading sits at 30.8% (r=156) and
   15.4% (r=312), untested. Red Team ruled this REAL and LOAD-BEARING and
   it remains open — if the coherent cross-term turns out to scale with
   shell fraction rather than staying a fixed small percentage, it would
   affect every `C` value this cycle reports, not just the fixed-absolute
   family's.
