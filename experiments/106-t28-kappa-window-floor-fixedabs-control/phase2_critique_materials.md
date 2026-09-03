# MATERIALS & METAMATERIALS — Phase 2 Critique, Panel Iteration 83 (exp-106)

*Blind critique. Charter: sub-wavelength structure realizability —
published / plausible / unobtainium-with-parameters.*

## Steel-man (≤150 words)

Item 4 is a clean control. It reuses exp-052's Iteration-29,
Red-Team-hardened fixed-absolute-thickness construction verbatim
(`ABS_THICKNESS=48`, `SIGMA_MAX_FIXED=0.5`, PEC-cored) rather than
inventing a new material law — zero new mechanism, T1 stays N/A. The
r=78 anchor coincides exactly with both families (`R_CORE=30`,
`sigma_max=0.5`), giving a free, verifiable zero-cost identity check
before any new FDTD call. Critically, exp-052's own P-5 core-fill check
already validated this exact family at θ=0 out to shell-fraction ratios
0.692/0.846 (five orders of magnitude inside its ±0.02 band) — and
exp-106's channel is *also* θ=0-only (single normal-incidence line
source), so the one incidence angle this control's prior realizability
due-diligence covers is exactly the one this cycle needs. The
electrical-thickness-growth hypothesis it tests is real and previously
unconsidered on this channel.

## Sharpest attack (≤150 words)

Both families hold `tau_shell=24` fixed by construction (self-similar via
`sigma_max=0.5/kappa`; fixed-abs via literally-unchanged `sigma_max=0.5`
over a literally-unchanged 48-cell/1.44µm path) — so the comparison is
coherent as a geometric-vs-electrical-thickness discriminator on its own
terms. But §5's realizability sentence overclaims: it argues the
fixed-abs family is "closer to the µm-scale real-CNT-black range" on
**thickness alone**, silently carrying forward `sigma_max=0.5` unchanged
without ever checking whether *that* value is realistic. `tau_shell=24`
over 1.44µm implies an intensity e-folding length of ~60nm (exp-052's own
`EFOLD_LENGTH_NM` — computed, not asserted) — roughly 3× the optical
density real CNT-forest ultra-blacks (~99.97% absorption, ~8 e-foldings)
achieve over a comparable path. Exp-052's own Phase-5 ranked this
absorptivity-literature check its #1 open MATERIALS item precisely
because no citation exists (T18 WebFetch block) — it was never done by
Iteration 83. This proposal imports the unresolved half of the recipe
right alongside the resolved half and states only the resolved half's
conclusion.

## Verdict

**Support-with-changes.**

## Parameter change that would flip verdict

If item 4's write-up used the fixed-abs `shape_ratio` result to argue
`graded_black_shell` is materially closer to **PLAUSIBLE** (a
realizability upgrade) rather than purely as a mechanism discriminator,
I would oppose — that would spend an unverified `sigma_max=0.5`
absorptivity claim as if it were the already-resolved thickness claim.
As written (mechanism-only, UNOBTANIUM-WITH-PARAMETERS retained
unconditionally at every r in both families) it stays support-with-changes:
add one sentence to §5 disclosing that the thickness-realism argument and
the absorptivity-realism argument are separable, and only the former is
being made here.
