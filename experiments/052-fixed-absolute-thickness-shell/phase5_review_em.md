# ELECTROMAGNETISM — Phase 5 Review, Panel Iteration 29 (exp-052)

*Fresh context. Charter: field/wave behavior, impedance matching, energy
coupling; owns the reciprocity/passivity/causality bookkeeping — formalizes
what T1 permits and forbids for each proposal. Read: PANEL.md, LOGBOOK.md in
full (RULED OUT, LIVE THREADS T1–T24), PLAN.md's Current-state and the LOCKED
Iteration-29 entry, and the complete exp-052 record (phase1_proposal.md, all
five phase2_critique_*.md, phase2_redteam_audit.md, phase3_synthesis.md,
NOTES.md, design_geometry.py, run.py, results.json).*

## Reading

exp-052 executes PLAN.md's unconditional, 21-iteration-deferred trigger:
build the fixed-absolute-thickness `graded_black_shell` variant
(`r_in = r_out − 48`, `sigma_max = 0.5` held fixed, not rescaled) and measure
its own ambient contrast `C`, as the direct test of MATERIALS' Iteration-7
realizability claim (a real coating's thickness doesn't grow with substrate
size) against T13/T14's "wrong-direction asymptote" puzzle. T1 escape route:
**none** — this is a passive, always-on, LTI absorber; no constraint-1–4
PASS/MARGINAL/FAIL language is invoked, correctly.

Phase 2 returned five independent support-with-changes verdicts; Red Team's
audit found all five real and load-bearing, added three more (the reused
self-similar comparator was itself HOLLOW-core and never re-measured at the
N9-ambient level — the same missing-`pec_disk` defect exp-031 had already
fixed for a different diagnostic and never propagated back), and issued
PROCEED-WITH-MANDATORY-FIXES. All nine items landed at Phase 3 except one,
disclosed rather than silently dropped: **the coherent-vs-incoherent ambient
bridge gate (exp-029's stage-11 idiom) was validated only at shell-fraction
61.5% (r=78, where the two families coincide) and was not re-run at this
cycle's own r=156/312 fractions (30.8%/15.4%)** — a Director-level scope
call under time budget, named as an open assumption, not a resolved one.

Results (`results.json::fit`), independently re-derived from the committed
file, match the headline exactly:

- `C_fixedabs`: −0.7208684660449545 (78, code-identity, P-0) →
  **−0.80668176727563** (156) → **−0.84031612126995** (312) — clean,
  monotonic, substantial deepening toward −1.
- `C_selfsim` (re-measured, PEC-cored, at the full N9 level — the corrected
  comparator): −0.72087 → **−0.7304552322383192** (156) →
  **−0.7322544463081008** (312) — near-flat, reproducing T14's own
  established shallowing pattern almost exactly.
- R-gate (P-4): `R_coat = −2.879×10⁻⁷` — clean, effectively zero, no bearing
  on the core-fill/comparator questions (correctly disclaimed, fix 9).
- Core-fill check (P-5/fix 3, θ=0 only): `core_fill_delta_theta0` =
  **−1.13×10⁻⁶** (r=156, ratio 0.692) and **+1.13×10⁻⁶** (r=312, ratio
  0.846) — T9's "core content is energetically incidental" null holds at
  ratios far beyond the single 0.385 point it was previously measured at,
  by this instrument.
- P-1/P-2/P-3 all read CONFIRMED in the committed `results.json`, verified
  independently against the file, not just the prose.

## Physical meaning

**T1 bookkeeping — nothing to formalize here, and that is itself the
correct reading.** The object under test is a static, isotropic, real-`σ`
(σ=0.5≥0, unchanged from the already-validated r=78 profile), non-gyrotropic
medium — trivially passive, reciprocal, and causal (no dispersion is added
or removed by this construction; only the radial extent of an unchanged
material law changes). No switching, no gain, no time-variation. T1's
central tension (constraints 1+2+3 jointly unsatisfiable for any LTI
medium at photopic ambient) is not engaged by this cycle and the proposal is
right not to claim it is. My charter's job this cycle is the *scale*
bookkeeping (T8/T13/T14), not T1's escape-route bookkeeping.

**Does deepening toward −1 make physical sense as z/z_R shrinks?** Yes, and
this is the crux the task asks me to check. In the ray-optics/geometric-
shadow limit, a passive, opaque, fully-extinguishing object subtends a
region of the observer's field where essentially none of the ambient field
survives; a Weber-contrast convention with a nonzero background necessarily
bottoms out at C=−1 there. T14 never disputed that −1 is the correct
limiting value — it disputed that the self-similar family's own *measured
trend* was even signed correctly to approach it (PHOTONICS' ceiling-law
exponent p=−0.148 and EM's own sqrt-law slope B<0 in Iteration 8 both showed
the self-similar family's fit structurally **cannot** reach −1 at any finite
distance — it curves the wrong way). That is the actual physical anomaly
T14 named, not merely "doesn't reach −1 yet."

**My own fit, on the fixed-absolute family's own three points**
(`z/z_R` = 0.04931/0.01233/0.003082 at r=78/156/312, reused verbatim from
`design_geometry.py`'s imported `GEOM`), using exp-030's own committed
idiom (`C = C_∞ + B·√(z/z_R)`, exact 2-point solve on the (156,312) pair,
r=78 held out as the free validation point — the identical convention
`experiments/030-scale-bridge/run.py::fit_sqrt_law` uses):

| Quantity | Value |
|---|---|
| B (slope) | **+0.6059** |
| C_∞ (sqrt-law asymptote) | **−0.8740** |
| C_pred(78), held out | −0.7394 (measured: −0.72087, miss = **0.0185**) |

That miss (0.0185) sits **inside exp-030's own pre-registered ≤0.03
"sqrt-law validated" band** (`experiments/030-scale-bridge/NOTES.md`,
P-VISION-1) — the identical bar the self-similar family's own fit was
scored against. So by this program's own established standard, the
fixed-absolute family's sqrt-law is validated, not merely plausible.

The sign is the load-bearing fact: **B is positive**, meaning C→C_∞
monotonically as z/z_R→0 — the structurally-correct direction, the exact
property T14 found the self-similar family's fit to lack (there, B<0). A
free-exponent check (3-parameter `C=C_∞+B·(z/z_R)^p` fit to all three
points) gives p≈**+0.68**, also positive — again the structurally-correct
sign, consistent with (not identical to) the pre-registered p=0.5. The
program's own shape discriminator
(`[C(78)−C(156)]/[C(156)−C(312)]`, sqrt-law predicts 2.00, linear predicts
4.00) reads **2.55** for this family — vs. **5.33** for the re-measured
self-similar comparator. 2.55 is closer to the sqrt-law's 2.00 than to the
linear law's 4.00, and far below the self-similar family's own
strongly-plateauing 5.33.

**But the fitted asymptote itself still falls short of −1**: C_∞ ranges
from **−0.874** (2-point exact fit, held-out-validated) to **−0.883**
(3-point least squares, residuals up to 0.004 — not a clean fit) to
**−0.862** (free-exponent 3-parameter fit) across every variant I tried —
a consistent shortfall of roughly **0.12–0.16** from the geometric-shadow
ceiling. Projected to the program's own central witness z/z_R (2.475×10⁻⁵,
`experiments/030-scale-bridge/NOTES.md`), the 2-point fit gives
**C_pred(witness) ≈ −0.871**, and the 3-point least-squares gives **≈−0.880**
— both far short of the standing, T13-flagged **unsourced** |C|≈0.98
figure this program has carried since Iteration 1 (traced by Iteration 8's
own desk audit to a single unfootnoted assertion, no derivation). My own
numbers give T13 a second, independent reason for caution about 0.98 —
not just "unsourced" but, for the one family this program has now measured
cleanest, **numerically disfavored** by roughly 0.1 in |C|.

**Verdict on the framing question the task poses: this cycle relocates
T14's puzzle, it does not resolve it.** The self-similar family's failure
mode was structural (wrong-signed slope/exponent — cannot reach −1 by
construction of its own fit, at any distance). The fixed-absolute family
does not share that defect: its slope and exponent are both correctly
signed, and its extrapolation passes this program's own held-out validation
bar. That is real, and it is consistent with — arguably it is the strongest
evidence yet for — Red Team's framing that **the self-similar family was
the anomaly, not black-shell absorbers generally**: removing its
growing-absolute-thickness confound removes the wrong-direction pathology.
What survives, narrower and quantified for the first time rather than
argued by analogy: even a correctly-signed, held-out-validated fit,
extrapolated from only three points spanning 1.5–2.5 decades short of
witness scale (the same extrapolation-gap caveat exp-030's own NOTES.md
already carries), lands short of the theoretical ceiling by a margin too
large to dismiss as fit noise but too thinly evidenced (3 points, no 4th
r-value, exponent not independently pinned) to call a second confirmed
anomaly either. This is exactly the T8/T13 "committed C(z/z_R)
extrapolation model before any near-threshold verdict is believed" gate —
and this cycle did not build or commit one (its own P-1/P-2/P-3 predictions
score deepening *direction and pairwise magnitude*, not a witness-scale
C_∞ claim). The fit above is mine, done for this review, not part of the
frozen record — it should not be cited as a program result until run
through the same house discipline (predictions committed before being
computed) T8 itself demands.

**Passivity/reciprocity bookkeeping — one live gap, correctly disclosed but
still open.** The established `σ_abs/σ_ext=0.51` figure this program has
carried since exp-002 already exceeds the idealized Babinet/shadow-formation
ceiling (≤0.5 for any perfectly-black object), attributed to T9's own
near-field-residual reading, not an asymptotic material constant. This
cycle's fixed-absolute object reaches `r_in/r_out` ratios (0.692, 0.846)
more than double any object this program has ever built (prior max 0.385) —
exactly the regime where a real core-vs-rim absorption imbalance would be
most likely to show up, and exactly the regime where any drift in that
ratio would matter most for judging whether the extinction paradox is
staying inside or drifting further past its idealized ceiling as the object
becomes more solid-core-dominated. What actually ran (fix 3, redesigned by
the Director from Red Team's original box-ledger proposal) is a θ=0
ambient-contrast delta between hollow and PEC-cored construction — genuinely
reassuring (Δ≈10⁻⁶, both signs, both r) that core content doesn't move the
*outward-facing ambient contrast*, but it is not a measurement of
`σ_abs/σ_ext` itself. Idealization 4 states this plainly: the sidecar's
0.51 input is reused, "unverified for this specific geometry." No
reciprocity or causality concern arises from anything measured this cycle —
the material law is unchanged in kind, only in radial extent — but the
energetic ceiling question (does 0.51 hold, or drift further past 0.5, at
these larger core fractions) remains an open bookkeeping item my charter is
responsible for flagging, not yet closed by this cycle's own instrument.

**One more inherited, unresolved precondition worth naming under this
charter's energy-coupling remit**: the entire P-1/P-2 result is read off
`lab/ambient.py`'s incoherent N9 sum, whose only empirical license
(exp-029's stage-11 coherent-vs-incoherent bridge gate) was measured at
shell-fraction 61.5% — this cycle's own scored geometry sits at 30.8%/15.4%,
untested. A thinner shell at fixed outer radius is a more strongly
rim-diffracting object; whether the incoherent-sum approximation still
holds there bears directly on whether the −0.807/−0.840 readings themselves
are trustworthy numbers, prior to any question about what they extrapolate
to. This was Red Team's own item 7, and the Director's Phase-3 disposition
disclosed rather than closed it — correctly, given the time budget, but it
remains the single largest unquantified risk sitting underneath this
cycle's own headline confirmation.

## Argued next change

Per T8's own standing requirement — a **committed** `C(z/z_R)`
extrapolation model, house-discipline predictions frozen before it is
trusted at near-threshold or witness scale — the highest-value next EM-
relevant step is to formalize the fit this review only sketched: pin a
functional form (sqrt-law per exp-030's own precedent, or the free exponent
my check found closer to p≈0.68 than p=0.5) for the fixed-absolute family
specifically, commit falsifiable CONFIRMED/PARTIAL/REFUTED bands for
`C_∞` against −1 *before* computing it, and — budget permitting — add a
4th r-point (this program has never fit any C(z/z_R) family with more than
3 points; every asymptote claim to date, on either family, rests on a
2-parameter fit to 2–3 numbers). Until that runs, no witness-scale number
for the fixed-absolute family — mine included — should be treated as more
than a suggestive estimate, and the standing unsourced |C|≈0.98 figure
should be actively disfavored in any future citation pending that same
formal check.

## Ranked top-3 (Iteration 31+; Iteration 30 is locked to VISION's stage-10
temporal instrument)

1. **Commit a formal, pre-registered `C(z/z_R)` extrapolation fit for the
   fixed-absolute family, with a 4th r-point if budget allows.** This is
   the direct execution of T8's own never-yet-honored requirement, now
   finally worth doing on a family whose slope is correctly signed. Cheapest
   version (desk-only, reusing the already-committed r=78/156/312 numbers,
   exactly like this review's own quick check but under house discipline)
   should run regardless of whether a 4th FDTD point is affordable — it
   directly resolves whether the ~0.12–0.16 shortfall from −1 is a real,
   second finding or a 3-point-fit artifact, and retires or sharpens the
   unsourced |C|≈0.98 figure for the first time with an actual derivation
   behind a number.
2. **Re-validate the coherent-vs-incoherent ambient bridge gate (exp-029's
   stage-11 instrument) at this cycle's own 30.8%/15.4% shell fractions.**
   Disclosed but unresolved by exp-052 itself (Red Team's item 7); existing
   machinery, no new code; and this program's own history (T20/T21/T22) is
   a repeated lesson that untested-precondition generalization gaps of
   exactly this shape do not stay harmless. Every number this review just
   analyzed depends on it.
3. **Extend T9's core-incidental null to a genuine energetic ledger
   (`radial_absorbed_power`/box-ledger, not just θ=0 ambient-C) at
   `r_in/r_out`=0.692/0.846** — Red Team's original Phase-2 proposal,
   redesigned down to a cheaper θ=0 ambient check for this cycle's time
   budget. The substitute answers "does core content move the outward
   view" (yes, negligibly); it does not answer "does `σ_abs/σ_ext` still
   respect its ≤0.5 idealized ceiling — or drift further past the
   established 0.51 — as the object's core fraction more than doubles past
   any ratio previously tested." That is a live passivity-adjacent
   bookkeeping question squarely inside this charter, and it is the one
   piece of this cycle's own energy-coupling picture that was argued around
   rather than measured.
