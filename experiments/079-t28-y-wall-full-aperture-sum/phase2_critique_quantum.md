# PHASE 2 — CRITIQUE · QUANTUM OPTICS · Panel Iteration 56 · exp-079

*Blind critique, independent of other seats. Charter: non-classical
absorption, state-dependent or coherent interactions; mechanisms enter the
bench only as effective classical parameters or Red Team strikes them. This
proposal's mechanism (a coherent aperture-weighted echo sum against a
complex `r(theta_local;ABSORB)`) is the classical-coherent limit my own
charter treats as in-scope. T1 escape route N/A (instrument/model-fidelity
thread). My seat's operative territory on this exact T28 sub-thread — null-
calibration and look-elsewhere rigor on a period-comparison claim — is
engaged directly by the task: is the "T21, not T28" read of §5.3 the R5
failure shape in a new guise, and is the one nominal Test-A SUPPORT
(`C80−C40`) sound?*

---

## 1. Steel-man (≤150 words)

This is a well-instrumented, honest negative result. It converts §2d's own
open question ("does the flat single-edge result generalize?") into a
sharply falsifiable computed answer: `ss_tot` ratio `9.4×10⁻⁷`, nine orders
of magnitude above exp-078's own degenerate floor, gate-clean across a
never-before-sampled `4.77°–15.50°` envelope, convergence-checked
1x→2x→4x to `<0.002%`. Branch (a) is cleanly REFUTEd. Rather than banking
that non-flatness as license to keep chasing the y-wall mechanism, §5.3
does the harder, more honest thing: it identifies *which* frequency
actually dominates (T21's, not T28's), backs it with a stated mechanism
(shared `A=752` driven-phase ramp), and uses that mechanism to actively
argue its own one marginal SUPPORT down rather than up — the same
epistemic posture this seat rewarded in exp-078's own self-scoring.

## 2. Sharpest attack (≤150 words)

I ran the decisive control myself: re-computed `E_echo` with
`r(theta_local(y_s))` replaced by a bare constant (`1.0`) — zero wall-echo
physics, only the source aperture's own driven phase and taper. Result:
`C80−C40` period `2.0085°`, R²=`0.9746`; solo `C40` `2.0310°`, R²=`0.9771`
— statistically indistinguishable from the committed model's `2.0301°`/
`0.9732` and `2.0226°`/`0.9733` (with reflectance weighting *on*). **The
model's central finding is guaranteed by the shared aperture geometry, not
by any property of the y-wall echo it was built to test.** This instrument
cannot discriminate a real y-wall echo from none — it reports the same
near-T21 period either way. That is a stronger, more specific claim than
§4/§6's disclosed "no null-permutation control" gap, and it is the finding
that actually settles whether "T21, not T28" is trustworthy — not a
random-noise Monte Carlo, which would be the wrong control for a
signal this well-resolved (R²≈0.97).

## 3. Independent verification performed (this critique's own computation)

**Why a standard R5 null-permutation control is the wrong instrument
here, and what I ran instead.** R5's addendum (exp-070) targets a *dense
search over many named candidates* finding a plausible match to noise-level
signal (sub-0.1% deviations recovered from search spaces of 36,680
combinations, on R² that never separated from chance). This proposal's
situation is structurally different in one load-bearing respect: the
recovered periods here are not noise-fit — `R²=0.97–0.98` at every solo
config curve (§5.5) and every pair-delta (§5.3/[6]), a strength this
sub-thread has never seen from a candidate mechanism model (compare
exp-078's own `R²=0.12–0.15`, itself ruled statistically indistinguishable
from a chance period-search fit by this seat's own Iteration-55 null
check). A generic i.i.d.-noise permutation control answers "could noise
produce this by chance" — the answer is obviously no at these R² — but
that is not the question that actually matters for trusting §5.3's causal
story. The question that matters is: **does this model's recovered period
depend on the physics it claims to be testing (the y-wall's ABSORB-
dependent reflectance), or is it a property of the aperture geometry the
model shares with the already-unrelated T21 mechanism regardless?**

I answered that directly (`phase2_quantum_ablation_check.py`-equivalent,
run inline, reusing `y_wall_aperture_sum.py`'s own imported
`build_aperture_grid`/`aperture_amplitude`/`source_driven_phase`/
`dist_image_cells`/`_trapz`/`_free_period_search` unmodified — only
`echo_field_curve`'s own `r_of_ys` term is replaced by a constant `1.0`,
zero reflectance physics, R4-compliant recomputation from the committed
primitives):

| quantity | committed model (`r(theta_local)` live) | ablated model (`r≡1`, no echo physics) |
|---|---|---|
| `C80−C40` P* | `2.0301°` (R²=`0.9732`) | `2.0085°` (R²=`0.9746`) |
| solo `C40` P* | `2.0226°` (R²=`0.9733`) | `2.0310°` (R²=`0.9771`) |
| `ptp(C80−C40)` | `1.470×10⁻⁵` | `6.932×10⁻²` (different scale — amplitude *is* reflectance-sensitive, as §5.3 itself claims) |

The **period and R² are essentially unchanged** by removing the wall-echo
physics entirely; only the **amplitude scale** changes (by orders of
magnitude, since `r(theta_local(y_s))` sets the overall echo strength) —
exactly consistent with §5.3's own prose ("the reflectance/image-distance
envelope... differs between configs in AMPLITUDE and OVERALL PHASE, not in
fundamental frequency"), now confirmed as a *load-bearing structural fact*
about this specific construction, not merely a plausible-sounding
narrative. This is a stronger form of verification than a null-permutation
control could offer for this particular claim, and it is cheap (reuses
every primitive already committed, zero new FDTD, ~10 lines of new code).

**Second check — sensitivity of the one marginal SUPPORT.** I scanned
fixed-period R² for all three pair-deltas across `[1.80°,2.30°]` in
`0.02°` steps (`_fixed_period_fit`, imported, not reimplemented). Each
curve has one clean, well-separated peak — `C80−C40` peaks at `≈2.02°–
2.03°`, `PAIR_PAD` at `≈1.99°–2.00°`, `PAIR_ABSORB40` at `≈2.00°–2.02°` —
a real, small (2%) but consistent spread, not a flat/ambiguous optimum.
Free-period-search grid resolution is not the cause (`n_grid` 400→40,000
moves `C80−C40`'s P* by `<0.004°`, `rel_dev` by `<0.001`, verdict
unchanged at every resolution). **But the spread itself explains the
marginal SUPPORT mechanically**: `C80−C40`'s own peak sits at the
*farthest* extreme from T21's exact value (`1.9608°`) of the three
comparisons — exactly the direction that pulls its `rel_dev` against
T28's `2.8421°` target down to `0.2857`, just inside the `≤0.30` bar,
while `PAIR_PAD`'s peak (closer to T21's true value) misses SUPPORT by a
wide margin (`rel_dev=0.5679`). If `C80−C40`'s fitted period had instead
landed at its own theoretical T21 value (`1.9608°`, R²=`0.9425` when
fixed there — a real, only slightly worse fit than the free optimum's
`0.9732`), `rel_dev` against T28 would be `0.3101` — **just outside the
SUPPORT bar**. The one nominal SUPPORT is real in the sense that it
reproduces cleanly and is not a grid artifact, but its SUPPORT-vs-
INCONCLUSIVE classification rides on a ~0.04°, ~2%, config-to-config
fitting-window difference between three curves that are all, by my own
ablation above, actually measuring the same underlying T21-scale
aperture-diffraction quantity. This is a genuine finding, not a search
artifact — but it is not independent evidence for T28's mechanism either,
matching §7's own self-graded skepticism.

## 4. Verdict: **support-with-changes**

The physics is sound and the honest core finding — branch (a) REFUTEd,
the recovered signal is T21's, not T28's — survives, and is *strengthened*
by my own independent ablation, which shows this is not merely a
proximity coincidence but a structural property of the construction. §4's
own R5 disclosure is more cautious than the substance actually requires:
a standard null-permutation control would have been the wrong tool (the
signal is not noise-level), and the "single, targeted, pre-named
comparison" framing, while defensible in spirit (EM's caution predates
this cycle), understates how *mechanically guaranteed* the T21 match is —
it would have appeared regardless of what the y-wall's reflectance
physics did, a fact this critique's ablation establishes and the proposal
itself never checks. That gap should not survive Phase 3 unresolved,
matching this program's own R8 standard: a specific, affordable check
that would resolve a disclosed gap was never run.

**Required change**: fold this ablation (or an equivalent `r(theta_local)
≡ const` re-run) into the committed record before Phase 3 treats §7's
"T21, not T28" characterization as final for the Iteration-56 ranking.
State explicitly that this construction's discriminating power for the
y-wall mechanism specifically is near-zero — the period result would look
the same whether or not the wall reflects at all — which is a *sharper*,
more informative negative than "the recovered period happens to sit near
T21's" on its own. Separately, §7's "1/3 nominal SUPPORT" language should
be paired with the fixed-period-at-T21 comparison above (`rel_dev=0.31`,
just missing SUPPORT) to make explicit that the SUPPORT/INCONCLUSIVE line
for `C80−C40` is set by sub-2% fitting-window noise on a common T21
carrier, not by an independently resolved second frequency.

## 5. Single change that would flip this to full support

Add the reflectance-ablation control (§3, this critique) to
`y_wall_aperture_sum_results.json`/`phase1_proposal.md` §5, with §7's
"T21, not T28" verdict language extended to state the instrument's
near-zero discriminating power explicitly. No change to the Test-A-only
numbers or the committed periods is needed — the ablation confirms them,
it does not contradict them. Absent that addition, I hold at
support-with-changes: the underlying claim is correct and now
independently re-verified, but the committed record currently argues it
from proximity and mechanism-in-prose alone, when a cheap, decisive,
zero-new-FDTD structural test was available and unrun — exactly the shape
R8 exists to catch before it propagates into the Iteration-56 ranking as
settled.
