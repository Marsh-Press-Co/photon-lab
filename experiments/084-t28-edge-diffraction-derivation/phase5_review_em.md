# PHASE 5 — BLIND FINAL REVIEW · ELECTROMAGNETISM · Panel Iteration 61 · exp-084

*Fresh context, zero memory of this cycle's earlier (now-adopted) blind
Phase-2 EM critique. Independent verification, not a rubber stamp.*

## 1. Verdict: **PARTIAL** (agree with the Combined Verdict as filed)

Leg (a): agree with the Phase-3 downgrade to INCONCLUSIVE on the period
match, and agree the shape-correlation finding (`r=0.958`) is real,
independently reproducible, and should stand as this cycle's genuine
positive result. Leg (b): agree NO VERDICT is the correct disposition —
but see §2 below, where I ran the cheap causal-discriminator test the
prior EM critique named and Phase 3 declined to run, and it changes what
should be trusted about the leg (b) causal story going forward. Checkpoint
criterion 4: agree it fires, with one precision correction to the record
(§4).

## 2. What I verified/tested myself

### 2.1 The phase-factor hypothesis for Anchor 2 — tested, and it fails outright, for a provable structural reason

I re-imported `phase1_derivation.py` unmodified and built a local,
uncommitted probe script
(`/tmp/.../scratchpad/probe_phase_factor.py`/`_2.py`/`_3.py` — exploratory
only, nothing written to the repo) that reuses `leg_a_curve`,
`leg_b_curve`, `propagate`, `dg048.field_and_h`, and `lab.ambient` exactly
as committed, varying only the stage-2 secondary-source weighting.

**Test A — literal `-i` / `exp(-i·π/2)` global factor** (multiply the
masked stage-1 field by a single constant before it re-enters `propagate()`
for stage 2): **no effect whatsoever** — `-i`, `+i`, and a real `-1`
control all reproduce the committed baseline's Anchor-2 numbers bit-for-bit
(`max_rel=2445.33%`, ratio range `[1.4656, 5.2793]` excluding
zero-crossing angles, identical to 6 significant figures across all four
factors tested).

This is not a near-miss — it is **provably impossible for any global
complex constant to change this pipeline's output at all**, for a clean
algebraic reason specific to this bench's own scoring convention:
`propagate()` is linear in `amp_src`, so multiplying the whole array by any
constant `c` scales both outputs by the same factor (`E→cE`, `H→cH`).
Since `Sx2 = -Re(E·conj(H))`, this rescales `Sx2(y)` by `|c|²` **uniformly
across every observation point**. `amb.weber(bo,bf) = (bo−bf)/bf` is a pure
ratio, so the `|c|²` cancels exactly — `weber()` is scale-invariant under
any global multiplicative rescaling of its input, complex or real, phase or
no phase. **The literal "-i normalization factor" hypothesis, read as a
bare global constant, is not a competing causal story to be weighed against
the write-up's RS-boundary-term guess — it is mathematically guaranteed to
leave `c_b_nomask(θ)` completely unchanged, before a single number is even
computed.** I verified this is not a coding accident by testing it four
independent ways (`-i`, `+i`, `-1`, and the untouched baseline) — all four
land on the identical float to 6+ digits, exactly as the algebra predicts.

**Test B — a natural cheap generalization: real per-source-point obliquity
envelope** `obliq1(y) = d1/hypot(d1, y−obj_y)` (a position-dependent, not
global, weighting — referenced to stage-1's own source/object geometry),
with and without an accompanying global `±i`: this is **not held back
by the scale-invariance argument** (it varies with `y`, so it does not
factor out as a single global `c`) — but it makes Anchor 2 **dramatically
worse**, not better: `max_rel` jumps from `2445%` to `>1,000,000%`, ratio
spread from `3.8` to `885`. Adding a global `±i` on top changes nothing
further (confirming Test A's invariance argument holds even layered on a
real envelope, exactly as the algebra predicts — a global phase times a
real position-dependent weight is still separable into [envelope]×[global
constant], and the constant still cancels).

**What this means for Iteration 62's queued fix**: the prior EM critique's
own named "parameter change that would flip my verdict" — read literally as
a bare `-i`/obliquity-times-phase-constant — cannot be the fix, and testing
it costs nothing to rule out. The qualitative diagnosis (a missing,
position-*and*-observation-point-dependent Rayleigh–Sommerfeld/Kirchhoff
obliquity kernel, not a simple envelope or a simple phase) is not weakened
by this — if anything it is sharpened: a correct fix must vary the
Green's-function weighting **per (source, observation) pair inside
`propagate()`'s own matrix** (matching how `field_and_h` already computes
`H` from `G0*obliquity`, generalized to a genuine RS-I `(1+cosθ)/2`-style
or RS-II `cosθ`-style element-wise kernel applied to construct `E2` itself,
not a pre-multiply of the input vector) — the "quick numerical probe" the
prior critique named as a decisive test turns out to have been
under-specified in a way that guaranteed a null result regardless of which
value was tried; the real, more expensive fix Phase 3 correctly deferred
to its own future proposal is the only route that can actually be tested.
This strengthens Phase 3's decision NOT to adopt "missing RS boundary term"
as settled (both original guesses — a bare RS term, and a bare phase
factor — are shown here to be under-specified placeholders, not competing
finished hypotheses) and should replace the open question in `NOTES.md`
item 2 with the sharper, narrower scope above.

### 2.2 EM bookkeeping on leg (a)'s corrected verdict — no violation found, one point overlooked by all five prior seats

Leg (a) is linear, source-free (no gain, no ε with negative imaginary
part), vacuum-only diffraction using `dg048.field_and_h`'s own convention
(E bare, H obliquity-weighted — Faraday's law for a driven line current,
independently hardened at T21/exp-042/046). The kernel
`G0=exp(i(kr−π/4))/√r` is symmetric under source↔observation exchange
(`hypot` is symmetric), so **reciprocity holds by construction**; the
phase convention is the correct outgoing/retarded branch (no acausal
term), and **no lossy or amplifying medium enters leg (a) anywhere**
(Idealization 4 is honest and correctly scoped) — **passivity and energy
conservation are not at risk because nothing in leg (a) redistributes
energy through anything but free-space propagation.** I found no violation.

One point none of the five blind critiques nor Red Team's audit raised,
worth stating for the record: EM's own (this cycle's) critique flagged
`C_model_a(θ)` as visibly **chirped** (non-stationary — unequal peak
heights/trough depths) rather than a stationary single-frequency signal,
but treated this only as a caveat on comparability to `P_edge_A`. From this
seat's own charter, that chirp is not incidental — **genuine near-field
(Fresnel) diffraction is expected to be chirped**: the governing phase is
quadratic in aperture position, so the *local* instantaneous angular
frequency of the fringe pattern is itself position/angle-dependent; a
single "best-fit sinusoid period" is a structurally lossy summary of a
signal that a correct near-field model does not predict to have one fixed
period at all. This cuts both ways and neither was said plainly this
cycle: (a) it is independent, physics-native support for treating the
`r=0.958` shape match as the real finding and the period-match framing as
the wrong comparator, rather than a downgraded version of the right one;
(b) it also means a 31-point, ~6°-window circular-shift null test — built
to ask "is a *fixed*-period fit distinguishable from noise" — may be
underpowered by construction for scoring a signal the model itself
predicts is *not* fixed-period, independent of whether `R²=0.3697` is
"real": a smooth, slowly chirping low-frequency curve over only ~2 periods
of window will generically admit many comparably-good fixed-period fits
under reshuffling regardless of whether the chirp itself is genuine
physics. This does not overturn the INCONCLUSIVE call (I have no basis to
claim the null test was actually miscalibrated, only that a chirped
process is a harder case for it than a stationary one), but it strengthens
the case for candidate direction #3 below rather than trying to rescue the
period-match framing.

### 2.3 Checkpoint criterion 4's own justification — firing is warranted, but the record overstates "silent"

Read `phase3_synthesis.md`'s Checkpoint reasoning against the actual
origin of the item (LOGBOOK Iteration 59, exp-082 Phase 5: "EM's/
THERMODYNAMICS' joint energy-interception cross-check (a tighter Poynting/
interception bound on this cycle's own article-loaded geometry)"). Two
things:

1. **The Director's own reasoning for firing (weighing, then rejecting, a
   same-shift-save argument) is sound and I agree with the conclusion.**
   The precommitment ("a third consecutive deferral without an explicit
   reason") is a deliberate commitment device; supplying a reason at Phase
   3 specifically to dodge a pre-scheduled firing is exactly the kind of
   after-the-fact rationalization this program's own R8 culture exists to
   catch, and the Director correctly declined to let itself off the hook.
2. **But the record should be more precise about what actually happened
   this cycle, and I don't think anyone caught this**: the full check, as
   originally scoped, requires a *real article-loaded FDTD field* to bound
   intercepted vs. re-radiated power against — something that does not
   exist in exp-084 at all (leg (a) is explicitly vacuum-only by
   Idealization 4; leg (b)'s own numbers are independently invalidated by
   Anchor 2, so there is no trustworthy amplitude to bound even if the
   check were attempted on it). A **cheap, partial discharge of the same
   underlying question did happen this cycle**, same-shift, at Phase 2:
   Red Team's own audit (attack 4) independently computed leg (b)'s raw
   `ptp_b=8.21×10⁻²` against the bench's own ESTABLISHED
   `graded_black_shell` reflectance ceiling (`R≤0.2%`) and found it ~41×
   too large — precisely the sanity-check comparison THERMODYNAMICS' own
   Phase-2 critique proposed as "Anchor 3." That is not the full
   Poynting-bound check named at Iteration 59, but it is not "zero
   engagement" either, and `phase3_synthesis.md`'s Checkpoint section
   doesn't credit it as a partial discharge anywhere.

**My own ruling as the EM seat: the firing should stand** (the *full*
article-loaded Poynting/interception bound genuinely was not run for a
third consecutive cycle, and this cycle had no article-loaded FDTD scene
to run it against — that scope mismatch is itself worth naming as the
real reason, rather than treating the absence as interchangeable with
exp-082's/exp-083's own silent absences, which *did* have live
article-loaded data available and skipped it anyway). I'd ask the LOGBOOK
entry to say precisely: *"the full joint bound remains undischarged for a
third cycle and this cycle had no article-loaded FDTD scene to run it
against; a cheap partial sanity-check (reflectance-ceiling comparison,
Red Team's Phase-2 attack 4 / THERMODYNAMICS' Anchor 3) was performed
same-shift and should be credited, though it does not substitute for the
full bound."* I also note, for the physics record, that the missing check
was **not outcome-determining this cycle**: leg (b) already carries NO
VERDICT for an independent reason (Anchor 2's failure), so nothing about
exp-084's own Combined Verdict would have changed had the full check been
run — the firing here is correctly a process/discipline event (the
program's own pre-committed schedule), not a sign that any energy
bookkeeping in the *filed* results is currently wrong or unaccounted for.

## 3. Ranked top-3 candidate next directions (from ELECTROMAGNETISM's charter)

1. **Build the real fix for leg (b), informed directly by §2.1's negative
   result.** A single global phase/normalization constant is now proven,
   not merely argued, powerless to close Anchor 2 under this bench's own
   Weber-contrast reduction — do not spend a cycle re-testing variants of
   it. The fix needs a genuinely matrix-valued (source-*and*-observation-
   point-dependent) Rayleigh–Sommerfeld/Kirchhoff obliquity kernel built
   into `propagate()` itself (RS-I `(1+cosθ)/2` or RS-II `cosθ` form,
   applied to construct `E2`, not pre-multiplied onto the input array),
   re-tested against Anchor 2 before any leg (b) SUPPORT/INCONCLUSIVE/
   REFUTE against `P*` is trusted. Scope it as its own small, pre-registered
   proposal (per Phase 3's own plan), not a patch under time pressure.
2. **Finally scope the joint EM/THERMO energy-interception check as a
   concrete formula with a pre-registered pass/fail band**, on a cycle
   with a real article-loaded FDTD scene to reuse (as Iteration 59 always
   intended) — three-plus cycles of prose-only naming ("a tighter Poynting/
   interception bound") without ever writing the actual quantity/threshold
   down is itself most of why it's been repeatedly deferrable; write the
   formula once, and this class of Checkpoint-4 firing stops being
   possible by construction.
3. **Test leg (a)'s shape-correlation finding against a chirped model,
   not a fixed-period one.** §2.2's point: genuine near-field diffraction
   is not expected to have a single stationary period, so `R²` of a
   best-fit sinusoid may be the wrong comparator for both the desk curve
   and the real FDTD `C80(θ)` curve. Fit both to a directly chirped model
   (the Fresnel-integral phase itself, or a locally-varying-frequency
   model) and compare parameters, rather than reducing both to one period
   number before testing significance — this could turn the `r=0.958`
   shape match into a properly falsifiable, better-powered claim instead
   of leaving it as a correlation with no matching significance framework
   of its own.
