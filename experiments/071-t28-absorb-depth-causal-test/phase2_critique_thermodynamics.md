# PHASE 2 — CRITIQUE · Panel Iteration 48 · exp-071
## THERMODYNAMICS (seat 4, blind, verbatim)

*Fresh sub-agent, THERMODYNAMICS charter (PANEL.md seat 4): where absorbed
energy goes; owns the per-proposal energy sidecar (absorbed power →
temperature rise → emission band → detectability), expressed as a
post-run analytic calculation, labeled as such. Read `phase1_proposal.md`,
`design_geometry.py` (re-run, verified — figures match: 74 calls, 5882.3
CPU-s, wall 28.76 min, 3× envelope 86.28 min, de-scope floor 70
calls/24.53 min — all bit-exact), `lab/fdtd2d.py::Sim._damping`, exp-065's
`design_geometry.py` (source of `CONGRUENT_KEYS`, `T5_THERMAL_CAVEAT`), and
LOGBOOK.md's T28 thread and RULED OUT R3/R5(+addendum) in full.*

## Discipline-specific finding: does the sidecar apply here at all?

Checked hard, per instruction, before concluding "nothing bites." Traced
`ABSORB` to its actual referent in `lab/fdtd2d.py::Sim._damping`: it is the
thickness of the FDTD grid's own graded-loss **domain-truncation boundary**
— a cubic ramp `(i/absorb)^3` fed into `exp(-0.30·d)` and multiplied onto
the E/H updates on all four edges of the computational box. This is the
engine's numerical analog of a PML/absorbing boundary condition. It is not,
and was never proposed as, a candidate witness-scene material — no `σ(x,t)`,
no dispersive `ε(ω)`, no article radius or optical depth is attached to it.

Two independent reasons the energy sidecar has nothing to attach to this
cycle specifically:

1. **No absorbing article is run.** This proposal's own idealization 8
   states single-angle `C_empty` (no-object) readings only; Block ARTICLE
   (the `tau=0.0065`, `r_out=78` uniform disk that DOES carry a thermal
   disposition — exp-065's own `T5_THERMAL_CAVEAT`, inherited from T5/
   Iteration-20/exp-043: UNDETECTABLE, >100x below sourced microbolometer
   NETD) is explicitly **not** re-run here (idealization 4). There is no
   physical absorber in this cycle's scene for power to be deposited in,
   in any sense relevant to a witness-scale re-radiation question.

2. **Even confined to the boundary's own internal bookkeeping, "more
   `ABSORB` depth" does not mean "more absorbed power."** With no PEC/
   absorbing object in the `C_empty` legs, essentially all source power
   that reaches the lossy edge is eventually dissipated there in *every*
   one of the four congruent configs — that is the boundary's entire
   purpose, and it is what makes `C40`/`C60`/`C70`/`C80` "congruent" at
   all (exp-065's own construction: A, clearances, and `D_SP` held fixed).
   What changes with `ABSORB` depth is the **residual reflectivity** — the
   small non-absorbed remainder that leaks back and produces the very
   `C_empty` interference structure T28 is chasing — not the aggregate
   absorbed-energy total. That is an EM/reflectivity question (already
   this cycle's own headline), not a thermodynamic one: nothing here
   re-radiates into the world because nothing here is a physical material.

PANEL.md's "ledger" metric row is scoped to candidate mechanism configs in
the phenomenon program; this cycle's own T1 statement ("N/A —
instrument/mechanism-identification class... constraint 3 not engaged")
correctly places it outside that scope, and I concur from my own reading
of the mechanics, not by deferring to the proposal's say-so.

## Steel-man (≤150 words)

The proposal is thermodynamically clean by omission, and correctly so.
`ABSORB` is the engine's own PML-analog boundary depth, not a material
parameter — attaching a "temperature rise → emission band → detectability"
calculation to a numerical domain-truncation layer would be a category
error, manufacturing a sidecar where no physical absorber exists to own
one. The proposal doesn't run Block ARTICLE (the one component in this
experimental family that DOES carry a live thermal disposition), so
exp-065's `T5_THERMAL_CAVEAT` is correctly left undisturbed rather than
reopened. And because all four congruent configs are, by construction,
near-total absorbers at their boundary regardless of depth, there is no
absorbed-energy trend hiding in the causal manipulation that a sidecar
would need to characterize. The energy-ledger metric row genuinely does
not apply to an N/A-T1-route, constraint-3-disengaged instrument test, and
the proposal states that scope correctly.

## Sharpest attack (≤150 words)

The proposal never says any of this. Nowhere in `phase1_proposal.md`'s
idealizations, T1-escape-route section, or narrative does it state that
`ABSORB` is a domain-truncation boundary condition rather than a candidate
absorbing material — the one fact that makes the THERMO sidecar
inapplicable. That silence is a real gap against this program's own
convention (CLAUDE.md: "every writeup states its idealizations";
exp-065's own file carried `T5_THERMAL_CAVEAT` forward explicitly for
exactly this reason). The vocabulary risk is concrete: this program's
absorbing-mechanism proposals for the actual phenomenon also use
"graded-loss absorbing" language for `σ(x,t)` candidates. If P-071-2
CONFIRMs an "ABSORB-depth-tied" periodicity, a future reader skimming
LOGBOOK could misread that as evidence about a physical absorbing
mechanism's energy behavior, rather than a PML reflectivity artifact with
zero witness-scene material behind it. One missing sentence, not a fatal
defect, but it is the sentence my seat exists to require.

## Verdict: **support-with-changes**

## Parameter/text change that would flip nothing (already support) but is requested

Add one idealization line, verbatim or equivalent: *"`ABSORB` is
`lab/fdtd2d.py::Sim._damping`'s own domain-truncation graded-loss boundary
(a PML analog), not a candidate witness-scene absorbing material — no
THERMO energy/re-radiation sidecar attaches to this cycle's result under
either CONFIRM or REFUTE, and `T5_THERMAL_CAVEAT` (exp-065, Block ARTICLE)
is untouched because Block ARTICLE is not run this cycle."* Cheap,
desk-only, zero `lab/` diff, closes the one scope-boundary gap this
discipline found.
