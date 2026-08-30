# Phase 2 Critique — MATERIALS & METAMATERIALS (blind)

## Steel-man (≤150 words)

`R4_RATIO=2.0` is, if anything, a *safer* mechanical substitution than
`R3_RATIO=1.5` was. Every base constant in `r3_config()`'s recipe scales by
an exact integer with zero rounding ambiguity (no `77*1.5→115.5→116`-style
half-integer cases exist anywhere in the R4 table) — independently
re-verified here: shell thickness `R4_R_OUT − PEC_R_R4 = 96` cells /
`cpl=40` = 2.4λ, bit-identical in wavelength terms to native (48/20=2.4λ)
and R3 (72/30=2.4λ), comfortably above `graded_black_shell`'s own stated
`≳1.5λ` minimum-thickness design assumption; the core/shell radius ratio
`PEC_R_R4/R4_R_OUT = 60/156 = 0.3846` reproduces native/R3's `30/78 =
45/117 = 0.3846` exactly. The physical-length gate would at least catch a
wrong exponent or mistyped base constant. As a pure geometry-family
extension of an already-congruent recipe, this is well-formed.

## Sharpest attack (≤150 words)

All four §2.4 gates are static algebraic checks on Python constants
(aperture equality, outer-radius equality, the `SIGMA_R4_CORRECTED`
*formula*) — none asserts anything about the **actually-constructed** `Sim`
object. Given `R4_RATIO=2.0` is an exact integer, item 3's "absolute
identity gate" is guaranteed to pass by construction whenever the correct
named constant was used — it verifies bookkeeping, not realization. This is
precisely the shape of R15's own founding defect (exp-091, MATERIALS'
self-review): `sigma_max` was left un-rescaled at runtime despite a
*correct formula* existing elsewhere, undetected by every prior gate, found
only by hand. Every new R4 function is declared a "mechanical mirror" of
its R3 sibling — copy-paste risk on the one line that matters,
`build_article_r4_sigma`'s `sigma_max` argument. A single call in Rank 1b
passing `SIGMA_NATIVE` or `SIGMA_R3_CORRECTED` instead of
`SIGMA_R4_CORRECTED` sails through every proposed gate, silently
reproducing R15's exact defect in a new resolution family — the falsifier:
no gate reads `sim.sigma_e` after construction.

## Realizability-bound scope note (this seat's own duty)

**N/A is correctly scoped, but only just.** `R4` changes no material law,
optical-response claim, or physical structure — it is the same PEC-cored
`graded_black_shell` object at a finer mesh, and every dimension re-derives
bit-identically to the already-scored native/R3 object (verified above).
That is a numerical-fidelity question, not a new "physical realization"
under the Latitude rule, so no fresh published/plausible/unobtainium
judgment is owed here. But the proposal's N/A framing should not be read as
"this cycle carries zero materials risk": if R4's realization of the
curved boundary is NOT faithful to the physical object at this finer
grid — the open question this critique raises — every past and future
MATERIALS realizability judgment resting on this bench's discretization
scheme inherits that defect silently. N/A on the bound; not N/A on the
verification burden.

## Verdict: **support-with-changes**

## Flip

Add one runtime identity gate, mirroring the existing vacuum-footprint (P1)
idiom: immediately after each `build_article_r4_sigma` call in Rank 1a/1b,
assert `np.isclose(sim.sigma_e[shell_mask].max(), SIGMA_R4_CORRECTED,
atol=1e-9)` before any FDTD step runs. That single check — verifying the
constructed material array, not just the constant that names it — would
move this to outright **support**.
