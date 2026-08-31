# Phase 5 Review — QUANTUM OPTICS (blind, independent)

*Panel Iteration 72, exp-095. Charter (verbatim): non-classical absorption,
state-dependent or coherent interactions; mechanisms enter the bench only
as effective classical parameters — σ(I), σ(x,t), dispersive ε(ω), gain —
or Red Team strikes them. This review is written blind to every other
seat's Phase-5 output; it owes Rank 1c — my own seat's own idea, adopted
via this cycle's mandatory-fix #2 — no deference. T1 route N/A this cycle
(pure instrument validation, matching every T28 desk/instrument cycle
since exp-069); nothing below touches σ(I)/σ(x,t)/ε(ω)/gain as a
phenomenon claim.*

## Verdict: **CONCUR-WITH-GAP** — the Rank 1c FAIL is correctly read as an
## integrity-relevant finding, but the specific ±0.1° bracket was sized
## without reference to calibration data sitting in the same document, and
## is very likely too narrow to have been a fair test either way.

The combined go/no-go HALT (Rank 1a PASS, Rank 1c FAIL → do not proceed to
Ranks 2/3) was the right conservative call given what was measured, and I
find no arithmetic or procedural defect in how Rank 1c was run, gated, or
reported. But the specific numeric pattern recovered, examined on its own
physics, does not read as strong evidence of a registration/phase defect
in the R4 family — it reads as at least as consistent with genuine,
resolution-dependent node migration, in the same direction as this exact
sub-thread's own already-established calibration point. The test as built
had materially less power to distinguish these two stories than the
89-call HALT this cycle attaches to it might suggest.

## 1. Independent re-derivation of the Rank 1c numbers

Pulled directly from `results.json::rank1.rank1c` (bit-exact match to
`run_output.txt` and NOTES.md's own table):

| θ | `delta_scene` (R4, cpl=40) | `floor_pass` |
|---|---|---|
| 38.49° | **−1.516840×10⁻³** | True |
| 38.69° | **−2.538531×10⁻³** | True |

Both negative, both floor-clearing (margin `ratio_k`=2.64×/1.83× over the
`FLOOR`), verdict **FAIL** per the pre-registered criterion (both
floor-clear, same sign). Confirmed correct arithmetic and correct
application of the pre-registered rule — no defect in the scoring itself.

## 2. Does this pattern look like smooth amplitude variation with no nearby
## zero, or could a phase/registration defect produce exactly this?

The task's framing is right that the raw two-point reading — magnitude
*growing* from 38.49° to 38.69° (−1.517×10⁻³ → −2.539×10⁻³, a factor of
1.67×) rather than shrinking toward zero — does not, by itself, look like
"approaching a nearby crossing from one side." But two further pieces of
evidence, both independently pulled from this cycle's own `results.json`,
sharpen this rather than leave it as a coin flip.

**(a) The four-point trend (38.49°→38.69°→39.2°→39.4°, spanning Rank 1c
and Rank 1a together) is non-monotonic — a real trough, not a runaway
drift.** Local slope: `38.49→38.69`: −5.11×10⁻³/deg; `38.69→39.2`:
−1.20×10⁻³/deg (deepening, but decelerating); `39.2→39.4`: **+2.79×10⁻³/deg
(reversing)** — `delta_scene` peaks in magnitude near 39.2° and is already
recovering toward zero by 39.4°, heading toward the next established
crossing (40.0718°/40.265°, cpl30/cpl20). This is the shape of a smooth,
single-signed interference trough between two real nodes, not an erratic
or monotonically-diverging signal — mechanistically unremarkable *given*
the trough exists somewhere in this span, which is exactly what R13/R14's
established `delta_scene(θ)` oscillation (period ≈2.84–2.95°) predicts.

**(b) The sign pattern is directionally consistent with — not merely
compatible with, but predicted by — the one calibration point this
sub-thread already has, and that calibration was never applied.**
`delta_scene(θ)` at cpl=20 is established (R13's founding record,
`experiments/090/results.json::q8.crossings_deg`, independently re-cited
in this cycle's own NOTES.md line 192) to read **+8.083×10⁻⁴ at 38.4°**
and **−4.151×10⁻⁵ at 38.6°** — i.e. the curve crosses from *positive* to
*negative* as θ increases through θ₀≈38.590°. A registration/coordinate
shift of the incidence angle (whether from genuine resolution-dependent
node migration or a wiring defect — see §3 below, these are not separable
by this test) is, to leading order, a lateral translation of this same
curve along θ. If that translation moves the crossing to a **higher** θ
(past 38.69°), both Rank 1c points would sit *before* the shifted node —
i.e. on the pre-crossing (**positive**) side. If it moves the crossing to
a **lower** θ (below 38.49°), both points sit *after* it, on the
post-crossing (**negative**) side. **We observe negative at both points —
only the leftward (lower-θ) shift direction is consistent with the data.**
And a leftward shift is exactly the direction this sub-thread's own
already-located crossing shift went: exp-092's lower crossing moved from
40.265420° (cpl=20) to 40.071838° (cpl=30), **Δθ = −0.194°**, also toward
lower θ. Two independent crossings on the same channel, both refined
toward lower θ under resolution refinement, is a real, if modest,
directional coincidence in favor of genuine migration over an arbitrary
bug — a wiring defect has no particular reason to prefer one sign of
angular offset over the other, while a genuine physical effect coupling
resolution to a systematic bias in the same direction at two different
features would be a coherent (if still unexplained) finding.

**This argument is suggestive, not dispositive — and by its own construction
cannot rule out a defect anyway.** A one-parameter lateral-translation
model is the simplest account, and I have not fit or verified it beyond
the sign-consistency argument above; a defect that also acts on amplitude
or shape, not just phase, would not obey it. More fundamentally: a genuine
resolution-dependent node migration and an angular-registration wiring bug
are **not separable by any test built on the node's own apparent location**
— both manifest identically, as a shifted zero-crossing. This is the sharp
form of my own Phase-2 critique, now empirically realized rather than
merely predicted: Rank 1c can detect "the node is not where it should be,"
but nothing in its design, however the bracket were widened, can tell you
*why* — that requires an independent check on the R4 family's own
machinery (§4).

## 3. Is ±0.1° a fair bracket? — No; the calibration to answer this was
## sitting unused in this cycle's own document.

`NOTES.md` line 192 states the `cpl=20` crossing set (`37.127°, 38.590°,
40.265°, 41.461°`); line 194, two lines later, states the `cpl=30`
crossings (`40.0718°, 41.7811°, 41.8377°`). The **only** crossing common to
both resolutions by nearest-match is `40.265°→40.0718°`, a shift of
**−0.1936°** — larger, on its own, than the entire ±0.1° half-width Rank
1c uses. This number was never computed anywhere in `phase1_proposal.md`,
`phase2_redteam_audit.md`, or `NOTES.md` (confirmed by direct grep of all
three — see also §"Standing-rule observation" below), despite both inputs
to it sitting two lines apart in the same crossing table this cycle's own
NOTES.md built. Three reasons this makes ±0.1° very likely too narrow,
stated in increasing order of severity:

1. **The available calibration point is for a smaller resolution jump than
   the one being tested.** `40.265°→40.0718°` measures a `cpl=20→cpl=30`
   shift (`RATIO` 1.0→1.5, a half-step). Rank 1c tests the `R4` family at
   `cpl=40` (`RATIO` 1.0→2.0, a full step) — a larger resolution change
   than the one that already produced a 0.194° shift. There is no reason
   to expect a *smaller* migration at a *coarser*-to-finer jump than the
   one already measured; naive linear extrapolation in `1/cpl` would
   suggest something closer to 0.29–0.39°, not 0.1°.
2. **This exact sub-thread's own most recent finding (exp-094, the cycle
   this one exists to follow up) is that the SAME `cpl=30→cpl=40` jump, on
   the *neighboring* window (41.75°–41.90°), produced not a partial shift
   but a complete sign-and-classification reversal at all six points** —
   qualitatively larger than a smooth 0.19°-scale translation. If the
   38.590° node's own migration under the identical resolution jump is
   drawn from anything like that same distribution, ±0.1° was essentially
   guaranteed to miss it before a single FDTD call ran, regardless of
   whether the true cause is legitimate physics or a defect.
3. **The bracket was proposed, by me, as "e.g. ±0.1°" in the Phase-2
   critique** (a placeholder illustrating the shape of a phase-sensitive
   control, not a derived number) **and it was never revisited against
   the calibration data before being frozen as the actual gating
   criterion.** Neither Red Team's Phase-2 audit (which recomputed and
   *did* cite `40.0718°` independently, attack #1) nor the Phase-3
   synthesis connected that same figure back to Rank 1c's own tolerance.
   This is a real gap in this cycle's own review chain, not merely an
   idealization footnote (Idealization 28 discloses the check is
   "coarser... than a full free-period fit" but does not address whether
   the specific coarseness chosen was sized against available evidence).

**Net effect:** Rank 1c's FAIL is real, correctly computed, and correctly
triggered the conservative HALT — but it should be read as **"the node,
if present, sits further than ±0.1° from θ₀≈38.590° in the R4 family,"**
not as "the R4 family shows no evidence of this node's presence." Framed
that way, given point 1–2 above, a FAIL was close to the expected outcome
under either the benign (migration) or concerning (defect) hypothesis —
the test had low power to discriminate them either way, which is a
narrower and more specific finding than "an integrity finding," though not
a weaker one for planning purposes.

## 4. Broader adversarial read of the cycle

**The HALT was the right call procedurally, independent of the above.** A
control built to gate expensive spend on an ambiguous or negative reading
should HALT on ambiguity, not require proof of a defect — this cycle spent
20 calls instead of 86, correctly, and did not force Rank 2/3's
necessarily-inconclusive `cpl=50` spend (itself independently shown, by
this cycle's own Phase-2 MATERIALS finding, unable to discharge R15's
addendum alone) into a Rank-1 reading this review shows was underpowered
regardless. Good discipline, genuinely improved over exp-094: Gate 5's
fault-injection verification was written **and actually run** this Phase
(confirmed, `gate5_wiring_defect_verification_result.json`:
`control_pass=true`, `injected_defect_pass=true`) rather than claimed and
later found unverifiable — directly correcting exp-094's own R4-flagged
overclaim.

**A second, smaller open thread, not flagged anywhere in this cycle's own
record:** Rank 1a's own magnitude trend across three resolutions is not
obviously converging. At 39.2°: `cpl20=−1.829×10⁻³ → cpl30=−2.492×10⁻³
(×1.362) → R4(cpl40)=−3.150×10⁻³ (×1.264 vs cpl30)`. At 39.4°:
`cpl20=−1.867×10⁻³ → cpl30=−2.211×10⁻³ (×1.184) → R4=−2.591×10⁻³ (×1.172)`.
Growth ratios are decelerating (1.362→1.264; 1.184→1.172) — consistent
with slow convergence, not alarming — but neither point has stabilized to
within this program's own historical ~7% "resolution-converged" precedent
(R3's meta-rule) after three refinements. The sign check's PASS is
correctly scored (sign is what was gated), but "PASS" at these two points
should not be read as "the R4 family's magnitude is settled here" — it
isn't, yet, even at the far-from-null control points chosen specifically
for their presumed stability. Worth a one-line disclosure if this cycle's
NOTES.md is revised, and worth watching at any future resolution point.

**Rank 4 (NEITHER, corrected-sigma 38.4° at cpl=30):** independently
re-derived, `frac_contrast=5.204×10⁻⁶` against `FLOOR=1.917×10⁻⁴` —
`floor_pass=False` by roughly two orders of magnitude, not a close call.
Correctly scored NEITHER; no issue found.

**Standing-rule observation (recommendation, not a rule I can adopt).** The
underlying gap in §3 is generalizable beyond this cycle: a
phase-sensitive/node-bracketing tolerance was chosen illustratively in a
Phase-2 critique and frozen without being checked against an
already-computed, already-cited cross-resolution shift magnitude sitting
in the same committed document. This is a sibling to R4/R9's own
"recompute, don't hand-type, and check commensurability" lineage, but
targets a *tolerance choice* rather than a *cited figure* — worth Red
Team's consideration as a candidate addendum: **any future bracket/
tolerance sized to test node presence or location must be justified
against the largest already-established cross-resolution shift magnitude
available for a comparable resolution-ratio jump, not adopted as a
round-number illustration from the critique that first proposed it.** I
name this as a recommendation for Red Team to weigh, not a rule I have
standing to adopt from this seat.

## Ranked candidate directions for Iteration 73

**1 (highest value, cheapest, resolves the actual ambiguity this cycle
leaves standing).** A widened, directional node search in the R4 family
near 38.590°, informed by §2's directional argument: search **toward
lower θ first** (e.g. 37.9°–38.49° in 0.1°–0.2° steps) rather than
symmetric widening, since both the sign pattern and the one available
calibration point argue the node — if present — most likely sits below
38.49°, not above 38.69°. A located crossing (any sign change with
`floor_pass=True` on both flanking points) would resolve this cycle's
ambiguity in the "genuine migration" direction without touching the
registration-defect question directly; a wide search with no crossing
found anywhere in, say, `[37.5°, 39.4°]` would be much stronger (though
still not conclusive) evidence against simple migration and would raise
the priority of item 2.

**2 (the test §2 shows Rank 1c structurally cannot supply, and the one
that would actually distinguish migration from defect).** An independent,
node-location-agnostic verification of the R4 family's own angular/
incidence-registration wiring — the angle-domain analog of Gate 5's
runtime `sigma_e`/`sigma_max` check. No gate anywhere in this sub-thread's
history (confirmed against the full Gate 1–6 list in this cycle's own
`run_output.txt`) has ever read back the constructed `Sim` object's own
injected incidence angle/k-vector and asserted it matches the intended
θ — every gate to date checks geometry constants and sigma, never the
angle actually wired into the source. This would settle §2's "migration
vs. defect" question directly, independent of where any node is, and at
comparable cost to Gate 5's own fault-injection idiom.

**3.** Apply the calibration discipline named in the Standing-rule
observation above retroactively to this cycle's own ±0.1° choice — either
by running item 1's widened search, or, if budget does not permit both
this cycle, by stating explicitly in any forward-facing summary of this
cycle's result that Rank 1c's FAIL is a **narrow-bracket, direction-untested
finding**, not a general "the node is absent from the R4 family" claim —
avoiding a mis-scoped citation of this cycle's own FAIL propagating into a
future cycle the way several prior overclaims in this exact sub-thread
have (R4's addendum, R16).

Also still open, standing, unaffected by this review: the x-wall
wavelength-generality leg (now twenty consecutive cycles deferred);
PHOTONICS' own grazing-incidence validity check; the unbiased
margin-vs-distance rebuild; the ritualization governance question
(Iteration 61).
