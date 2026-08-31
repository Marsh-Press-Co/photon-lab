# Phase 2 Critique — QUANTUM OPTICS (blind, independent)

*Panel Iteration 73, exp-096. Charter (verbatim): non-classical absorption,
state-dependent or coherent interactions; mechanisms enter the bench only
as effective classical parameters — σ(I), σ(x,t), dispersive ε(ω), gain —
or Red Team strikes them. T1 route N/A this cycle (pure instrument
validation). This review is written blind to every other seat's Phase-2
output. The registration-readback gate under review is my own seat's own
proposal, adopted from exp-095's Phase-5 review — owed no deference here.*

## Steel-man (≤150 words)

The design faithfully executes what this seat asked for, correctly scoped:
it reads back `sim.lam`, `angle_deg`, source placement, and the actual
phase-ramp array from the real, unmodified `Sim` object at construction
time — matching Gate 5's own precedent rather than inventing new machinery.
Provenance for every recomputed value is cited to a file/line, not
hand-typed (R4/R9 discipline). The mandatory three-scenario fault-injection
suite is genuinely coherence-aware, not boilerplate: FI-C (the sign flip,
`sin(−θ)=−sinθ`) is exactly the defect class a magnitude-only phase check
would miss, and the proposal explicitly designs Check 4 as a signed-array
comparison to guard against it — direct evidence the author internalized
the phase-domain reasoning behind my original ask rather than reducing it
to a scalar `angle_deg` diff. Zero marginal FDTD cost, honestly disclosed
idealizations (31–37) pre-empt several likely objections before they are
raised.

## Sharpest attack (≤150 words)

All four checks validate wiring *fidelity given the job constants* — they
never validate the constants themselves. §3's `theta_intended`/
`cpl_intended` for every one of the 8 points is pulled from exp-095's
`run.py` (`RANK1A_ANGLES=[39.2,39.4]`, line 263; `RANK1C_ANGLES=
[38.49,38.69]`, line 264; etc.) — the *same* file, same constants, that
the production call sites already consume. But an independent, textually
separate ground truth already exists and predates that file: exp-095's own
NOTES.md froze these exact angles in its Predictions section *before* any
Phase-4 script was written (house discipline, non-negotiable). The gate
never cross-checks run.py's constants against NOTES.md's frozen prose. A
transcription slip made when those constants were first typed into run.py
— a swapped pair, a mistyped digit — would leave the gate's own
recomputation and the real call site in perfect, CLEAN agreement while
silently testing the wrong angle entirely. This is the coherent-
registration analog of R4's own hand-typed-figure rule: recomputing from
an already-committed source verifies internal consistency, not correctness
against the experimental design of record.

## Verdict: **support-with-changes**

## Change that would flip to unconditional support

Add a fifth, near-zero-cost check: for each of the 8 representative
points, assert the `theta_intended`/`cpl_intended` values read from
run.py's job constants equal the values stated in exp-095's NOTES.md
frozen Predictions section (cited by line, same discipline as the rest of
§3). This closes the shared-root blind spot — the one case where a CLEAN
result from the existing four checks would not actually license the §5a
"registration removed as a live explanation" conclusion the whole cycle
exists to earn.
