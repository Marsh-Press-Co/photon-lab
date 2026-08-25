# PHASE 2 — CRITIQUE · MATERIALS & METAMATERIALS · Panel Iteration 48

## Steel-man (≤150 words)

The proposal correctly self-classifies T1 route N/A and constraint 3 not
engaged — no material or mechanism realizability claim is advanced, so this
seat's realizability bound genuinely has nothing to score against the
parameter table itself. Discipline is good: zero new `lab/` diff, `A=752`
held bit-identical across all four `ABSORB` depths (asserted in code, and I
reproduced `design_geometry.py`'s own output directly — every printed
number, including the R3-rescaled `A=1128` and the 74-call/28.76-min
budget, matches verbatim). Idealization 8 correctly keeps this off the
N9/N17 ambient-contrast/σ(I) channel entirely, so the missing
`REALIZABILITY_MEMO.md` cross-reference this seat had to flag on exp-065
(Iteration 42, P-VIS42-7) does not recur here — there is no σ, no article,
nothing this memo's UNOBTANIUM verdict could attach to. For a pure
instrument-diagnostic cycle, declining to manufacture a realizability
discussion is the right call, not an omission.

## Sharpest attack (≤150 words)

`ABSORB` is not a material — it is `lab/fdtd2d.py`'s own domain-truncation
device: a cubic conductivity ramp `sigma_max*((i)/absorb)**3` over the outer
40–80 cells, there to suppress edge reflections, with no material referent,
real or hypothetical (verified by reading `fdtd2d.py` directly). exp-070's
own Phase-3 synthesis (mandatory fix 5, MATERIALS' own Phase-2 catch that
cycle) made this a **required disclosed caveat** on every future citation of
`ABSORB`-derived numbers: "graded-loss absorbing boundary — not PML... not a
material or physical-optics parameter... at least as consistent with a
numerical-boundary-construction artifact... as with a physically real
diffracting edge." This proposal — the direct causal follow-up on that exact
parameter — drops the caveat entirely (zero occurrence of "numerical,"
"boundary condition," "PML," or "not a material" anywhere in
`phase1_proposal.md`) while its own committed verdict language moves the
opposite direction: the CONFIRM branch is titled **"genuine ABSORB-depth-tied
mechanism"** and the narrative claims "direct physical coupling between the
graded-loss boundary's own thickness and the observed periodicity." If the
sweep confirms, that headline phrasing will read downstream as a
materials/physical-optics finding about a real graded absorptive boundary —
exactly the overclaim last cycle's mandatory fix exists to prevent — a
regression of a fix adopted one cycle ago, not a new failure mode.

## Verdict: **support-with-changes**

The engineering, budget, and gates are sound and I could not find a defect
in the causal design itself — reusing exp-065's congruent series and
exp-069/070's free-period search on two genuinely new `ABSORB` points is
the correct test, and P-071-4's peak-cell R3 precondition properly closes
the "only tested near a zero-crossing" gap Red Team named. The defect is
entirely in language, not design, science, or gates, which is why this
does not rise to oppose: reinstating the caveat changes zero FDTD calls,
zero bands, zero budget lines.

## Parameter change that would flip the verdict

Before Phase 3 freeze, add (verbatim or by direct cross-reference to
`experiments/070-.../phase3_synthesis.md` docket item 5) the disclosed
caveat that `ABSORB` is FDTD domain-construction bookkeeping, not a
material or physical-optics parameter, and rename the CONFIRM branch's
parenthetical from "genuine ABSORB-depth-tied mechanism" to something like
"ABSORB-depth-tied numerical-boundary-construction artifact (not a
material/physical mechanism)." With that language fix, verdict → support.
