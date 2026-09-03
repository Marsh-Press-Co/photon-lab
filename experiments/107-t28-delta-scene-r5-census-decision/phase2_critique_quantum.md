# PHASE 2 — CRITIQUE · QUANTUM OPTICS · Panel Iteration 84 (exp-107)

*Fresh context. Charter: non-classical absorption, state-dependent or
coherent interactions. Expressibility contract: mechanisms enter the bench
only as effective classical parameters — σ(I), σ(x,t), dispersive ε(ω),
gain — or Red Team strikes them.*

## T1 confirmation (this seat's standing duty)

**Confirmed N/A, correctly claimed.** The R5 census reuses the identical
`C40`/`G40` config pair (`dg065.CONFIGS`) that every prior R3/R4/R5 cycle
has used, rescaled only geometrically by `R5_RATIO`; the bundled Tier-1
items (thermal row, numerator floor gate, hollow-vs-PEC-cored delta) all
reuse exp-106's own already-persisted `sigma_ext`/`sigma_abs`/ledger
fields or exp-052's already-validated hollow-core construction. No
σ(I)/σ(x,t)/dispersive ε(ω)/gain term is introduced or varied anywhere;
exp-106's own Phase-5 audit already confirmed `pec_disk`/
`graded_black_shell` are static, position-only σ(x) assignments, and
nothing in this proposal touches that machinery. T1:N/A is earned, not
merely asserted.

## Steel-man (148 words)

G0's two-part test — `sign(R5)==sign(R3)==sign(R4)` **AND**
`|R5|/mean(|R3|,|R4|) ∈ [0.5,2.0]` — is a faithful extension of this
program's own ground-truth-recovery lineage (R6, R15's addendum) to an
attribution question rather than an estimator. It refuses to let a bare
correlation `(r,p)` stand in for a recovery check, closing exactly the
holes R9 (commensurability) and R13/R14 (subtractive-cancellation/single-
point trust) already burned this program on: a sign-only test could pass
on coincidental direction agreement while the magnitude is wildly off, or
vice versa; this gate requires both simultaneously before any correlation
reading counts as evidence. Paired with the pre-registered NEITHER→
formal-retirement branch, G0 gives the census a genuine kill switch
*before* Phase 4, not a post-hoc rationalization after a null result —
the discipline this seat's charter most wants applied to any "coupling
detected" claim on this channel.

## Sharpest attack (150 words)

`θ_anchor`'s own selection rule is unsatisfiable on the proposal's own
cited numbers — undiscovered before Phase 2. The four native-grid zero-
crossings it names are 37.127°, 38.590°, 40.265°, 41.461° (consecutive
gaps 1.463°/1.675°/1.196°) — every gap smaller than 2×1.4°=2.8°, the
exclusion width the "≥1.4° from every crossing" buffer imposes around
each one. The four exclusion intervals therefore overlap pairwise and
merge into one continuous forbidden band, `[35.727°, 42.861°]`, which
fully contains the proposed 36.0°–42.0° grid. **No angle in the chosen
31-point grid clears the buffer from every crossing** — `θ_anchor` cannot
be selected, so Gate G0 has no candidate to evaluate, before any FDTD
call runs. This is exactly the failure §7 asks Red Team to check "against
the actual pooled data BEFORE freezing, not discover it at Phase 4" — and
it fails that check. The census as specified cannot execute its own
mandatory gate.

## Verdict: **support-with-changes**

The census design and the G0/three-way-outcome architecture are sound;
the `θ_anchor` selection rule as literally written has an empty domain
over the proposed grid and must be repaired before Phase 3 freeze.

## Single parameter change that would flip this verdict to support

Redefine `θ_anchor`'s clause (b) from a hard `≥1.4°` requirement to
"the grid angle maximizing distance-to-nearest-crossing" (falling back
honestly to whatever margin is actually achievable, disclosed numerically
— even ~0.6–0.7° at the grid's best point, still comfortably above the
established ~0.19°–0.38° cross-resolution crossing-shift magnitude R17
already put on file), or widen the grid to include a genuinely
crossing-free window outside [36°,42°]. Either change gives G0 a real
candidate to evaluate, and I would move to support.
