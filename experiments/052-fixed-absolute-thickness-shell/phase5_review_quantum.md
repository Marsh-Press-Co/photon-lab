# QUANTUM OPTICS — Phase 5 Review · Panel Iteration 29 · exp-052

*Fresh sub-agent, no memory of prior cycles. Read PANEL.md, LOGBOOK.md
(RULED OUT R1–R5, LIVE THREADS, Iteration 6/exp-029's full record,
Iteration 28's LOCKED-trigger entries), PLAN.md's Current-state + LOCKED
Iteration-29 entry, and the complete exp-052 record (`phase1_proposal.md`,
all five `phase2_critique_*.md` including my own, `phase2_redteam_audit.md`,
`phase3_synthesis.md`, `NOTES.md`, `design_geometry.py`, `run.py`,
`results.json`). This review does not see any other seat's Phase-5 output.*

## Reading

The headline reproduces exactly: `C_fixedabs` = **−0.72087 → −0.80668 →
−0.84032** at r=78/156/312 (`results.json::fit`), P-1/P-2/P-3 all
**CONFIRMED**, R-gate clean (`R_coat = −2.88×10⁻⁷`, five orders under the
0.2% band), and the core-fill check (P-5) confirms T9's "core is
energetically incidental" null generalizes far past its previously-tested
ratio — `core_fill_delta_theta0` is ~1.1×10⁻⁶ at r_in/r_out = 0.692 and
0.846, essentially the same near-zero delta T9 measured at 0.385. This is
a clean, monotonic, well-gated cycle by every check it ran.

My own Iteration-28 Phase-2 critique of this proposal flagged that
`experiments/029`'s coherent-superposition bridge gate — the only
empirical license this program has ever produced for treating the ambient
instrument's per-angle intensity sum as safe — was validated exactly once,
at shell-fraction 61.5% (r=78, where the fixed-absolute and self-similar
families coincide). `phase3_synthesis.md` item 7 confirms, in writing,
that the Director did **not** close this: re-implementing exp-029's
cross-term measurement for the new object was judged too risky to attempt
under this shift's time budget, and the concern is disclosed as an open,
unresolved assumption, not silently cleared. `design_geometry.py`'s own
fix-7 comment states the stand-down argument explicitly: "the measured
cross-term's smallness... is a property of the N9 angular-averaging/source
geometry... not obviously a function of the object's own shell thickness"
— an argued, not measured, claim.

I went back to `lab/ambient.py` and `experiments/030-scale-bridge/run.py`
directly rather than trusting that framing. This surfaces something my own
Phase-2 critique under-stated: exp-029's bridge gate validated a **beam
(amplitude 1.0) plus one weak off-axis probe (amplitude 0.014142,
amp_rel=2×10⁻⁴)** — a wildly asymmetric two-source configuration whose own
Cauchy-Schwarz cross-term ceiling (2√amp_rel ≈ 2.83%) is small *because of
that asymmetry*, not because of anything about the object. The instrument
this cycle's entire headline result actually runs on is different in
kind: `lab/ambient.py::incoherent_sum` post-hoc-sums nine **equal-amplitude
(1.0)** angled runs (`run.py` line 176: `amplitude=1.0` at every θ in the
N9 set) — no dominant "beam," no weak probe. That configuration's own
pairwise cross-term ceiling is not 2.83% — it is unbounded by exp-029's
result at all, at *any* shell fraction, including the one exp-029 tested.
The shell-fraction gap I raised at Phase 2 is real and unresolved, but it
sits on top of a structurally larger, pre-existing gap: the bridge gate
has never validated the actual equal-amplitude multi-angle configuration
the ambient `C` instrument uses, at any geometry this program has run.

## Physical meaning

The question I was asked: does an effect this large (ΔC ≈ 0.12 across the
family, 0.086 at the r=156 point alone) make my own concern more urgent or
less?

**The naive "too big to be the artifact" argument is true but doesn't
answer the right question.** exp-029 measured its own cross-term at
+0.0224% of the beam's absorbed power (126× under its Cauchy-Schwarz
ceiling) — four orders of magnitude below a 0.086–0.12 shift in C. If the
only candidate contamination were "more of exactly what exp-029 measured,"
the effect size argument would be decisive: it isn't. But that argument
only bounds a coherence artifact *of the same kind and scale* exp-029
characterized — a weak-probe-on-strong-beam cross-term. It says nothing
about the untested, structurally different, equal-amplitude N9
configuration this cycle's `C` is actually built from, whose own
Cauchy-Schwarz ceiling is not 2.83% but formally unbounded by anything
this program has measured. "The effect is too large for a 0.02% artifact"
is true and irrelevant to whether an unmeasured, potentially much larger
artifact exists in the instrument this result actually uses.

**There is a real, physically motivated reason a bigger effect at this
geometry raises the *stakes*, even without raising the measured
*probability*.** Two things changed together this cycle, not one:
(a) the shell fraction shrank (61.5%→30.8%→15.4%), pushing the object
toward exactly the thin, rim-dominated, near-field-diffractive regime
this program's own T9/T12/T14 threads already associate with *more*
structure, not less — T12's ripple, and the ~15% diffractive-leakage
finding this program attributes to thin absorbing shells at scale, are
both evidence that thinner/larger objects in this bench are more prone to
near-field interference structure per unit size, not immune to it; and
(b) the result this structure would contaminate is now load-bearing for a
much bigger claim than a diagnostic number — it is the empirical basis for
overturning 21 iterations of "self-similar is the harder realizability
ask," for the 1.44µm fixed-thickness-coating realizability argument in
§9, and for T14's own reframing (P-3: the wrong-direction shallowing is
NOT a property of near-field/rim-diffraction geometry generally). None of
this cycle's own internal gates test for the risk in question: P-0 checks
transcription identity, P-4 (R-gate) checks flat-wall normal-incidence
reflectance only (explicitly disclaimed in fix 9 as saying nothing about
this), and P-5 checks core-content sensitivity. A systematic coherent
cross-term bias in the incoherent-sum instrument would not trip any of
them — it would look exactly like this: clean, monotonic, gate-passing.
Cleanness here is evidence against the failure modes those three gates
test for; it is not evidence against the one gate this cycle didn't run.

**There is also a real, physically motivated argument the other
direction**, and intellectual honesty requires stating it as clearly as
the risk argument: the absolute shell thickness stays fixed at 48 cells
while `r_out` grows, so the object's angular/azimuthal extent (which sets
how many fringe periods a cross-term's spatial oscillation sweeps through
before radial/angular integration) grows with `r_out`, not with the
shell. By the same J₀(|Δk|·r) mechanism PHOTONICS used at Iteration 6 to
argue exp-029's own cross-term was smaller than a naive single-radius
estimate, MORE averaging length at larger r_out could mean MORE
cancellation, not less — a stability argument, not a risk argument.

Both directional arguments are physically motivated; neither is measured,
in either family member of this cycle. That is the actual state of
evidence, and it is unchanged by the fact that ΔC came out large — the
result's size moved what is *at stake* in this gap, not what is *known*
about it. A large, clean, well-gated result that rests on one genuinely
untested instrument assumption is not "de-risked" by its own size; it is
a large, clean result whose one soft spot has become more expensive to
leave soft.

## Argued next change

Escalate the bridge-gate re-validation, but not as a literal rerun of
exp-029's own idiom — that idiom (beam + weak off-axis probe, amp_rel=2×
10⁻⁴) tests a configuration `lab/ambient.py`'s N9 sum does not use. The
correctly-targeted build is a joint-coherent injection of **several
equal-amplitude (1.0) angled sources**, matching `run.py`'s own N9
convention, run simultaneously in one `Sim` on the fixed-absolute object
at r=156 (this cycle's own mandatory geometry) — reusing suite stage 11's
existing field-identity gates (Q1/Q2-style, trivially exact regardless of
outcome) plus a new absorbed-power cross-term measurement analogous to
P-QUANTUM-7/9, scored against the incoherent sum `lab/ambient.py` actually
computes from the same angle set. A full 9-source joint run is the
complete answer; a cheaper interim bound — jointly injecting just the two
most angularly separated equal-amplitude members of the N9 set (θ=−35°,
θ=+35°) and comparing the coherent absorbed-power sum against their
incoherent intensity sum, at the fixed-absolute r=156 object — would
directly measure the worst-case pairwise cross-term this program has never
bounded, at low marginal FDTD cost, before committing to the full build.

## Ranked top-3

*(Iteration 30 is already LOCKED to VISION's stage-10 temporal instrument
— ranking here is for Iteration 31+.)*

1. **The redesigned coherent-vs-incoherent bridge-gate re-validation**,
   built against the actual equal-amplitude N9 ambient configuration (not
   exp-029's weak-probe idiom), on the fixed-absolute object at r=156.
   Argue for escalation toward unconditional priority: this program now has
   a 21-iteration-deferred realizability claim, a T14 reframing, and this
   cycle's own headline deepening trend all resting on one instrument
   assumption that has never been tested in the configuration it is
   actually used in, at any geometry.
2. **The same check extended to r=312** (shell fraction 15.4%, the
   furthest point yet from the validated 61.5% anchor) if/when r=312's own
   ambient leg runs — the r=312 pilot in `results.json` already logged
   ~656s for a single-angle probe (~77 min extrapolated for a full leg),
   so this should be scoped and budgeted together with that decision, not
   after it.
3. **A cheap, desk-only interim diagnostic**: recompute the fringe-period/
   azimuthal-averaging count for the actual N9 angle spacing (not exp-029's
   single θ=30° probe geometry) at r=156 and r=312, the same style of
   calculation `design_geometry.py` already does for other desk items in
   this cycle. This would sharpen which of the two directional physical
   arguments above (more averaging at larger r_out vs. more diffractive
   structure at thinner shell fraction) is likely to dominate, and should
   inform — not substitute for — item 1's scoping, before FDTD budget is
   committed.
