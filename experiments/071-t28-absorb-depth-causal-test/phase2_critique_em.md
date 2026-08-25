# exp-071 — Phase 2 Critique: ELECTROMAGNETISM (blind)

**Seat charter applied:** field/wave behavior, impedance matching, energy
coupling; reciprocity/passivity/causality bookkeeping; formalizing what T1
permits and forbids. T1 is correctly N/A this cycle (instrument/mechanism-
identification class, constraint 3 not engaged) — the charter work here is
auditing whether the free-period-recovery methodology is a sound EM
measurement across four boundary-thickness configurations, and specifically
whether this program's own settling/domain-of-dependence discipline — the
exact class of defect this seat caught at Iteration 42 (exp-065's causal
gate using the wave's Courant phase speed instead of the leapfrog stencil's
true 1-cell/step domain of dependence) — is properly inherited here.

Verified independently: `python3 design_geometry.py` reproduces every
number in `phase1_proposal.md` bit-for-bit (`A=752` congruence assertion,
the four `ABSORB`/`PAD`/`NX`/`NY` rows, `P(39°,600nm)=1.9608°`, the two
peak-angle `|delta|/(ptp/2)` fractions 0.949/0.984 against zero-crossing
values ~0.06/0.08 at 39°/40°, and the full budget: 74 calls / 5882.3 CPU-s
/ 28.76 min wall / 86.28 min envelope). House rule R4 satisfied — no
hand-typed figure found.

---

## Steel-man (≤150 words)

This is a genuine causal manipulation, not another named-constant search —
it correctly avoids R5/R5-addendum scope (one already-named physical
parameter, four already-built configs, no combinatorial look-elsewhere).
Holding `A=752` bit-identical across all four `ABSORB` depths (asserted in
code, independently re-verified) isolates the boundary's own thickness as
the single varied quantity — the textbook single-variable design T28 has
lacked since exp-070 could only compare two points. Reusing exp-069's
already-committed `C40`/`C80` dense sweep behind a bit-exact G1 identity
gate is the correct zero-cost way to extend two points to four without
re-spending FDTD budget on data already trusted. Extending the peak-cell
R3 recheck to all four configs (not just the literally-queued `C40`/`C80`
pair) closes exp-069's own disclosed near-zero-crossing resolution gap
honestly, at near-zero marginal cost, before it becomes load-bearing for a
causal claim.

## Sharpest attack (≤150 words)

The design imports `STEPS_SETTLED=2800` as "this program's settled floor"
and applies it to `C60`/`C70` with no settling-closure check anywhere in
this cycle. But no such check has ever been run on `C60`/`C70` at any
angle or λ: the asymptotic 4-point convergence trend (1400/2800/4200/5600)
that actually certified 2800 was run only on `C40`/40°/600nm (exp-065);
exp-069's `Block SETTLE-C80` (4200-vs-2800) certified only `C80`. `C60`/
`C70` have only a two-point 1400→2800 ratio from exp-065's Block SWEEP
(C60: 68.4%, comparable to C40's 74.4%) — evidence 2800 is *closer* to
converged, not that it *is*. Block R3-PEAK (cpl 20→30) is a spatial check,
orthogonal to this temporal one, and cannot substitute. This program's own
Learned note from the exact experiment that established 2800 (exp-065)
states plainly: "a settling check calibrated on one channel... does not
transfer to a structurally different channel... settling is per-channel,
not per-geometry" — and `ABSORB` depth changes `NX`/`NY`/damping profile,
i.e. the geometry, for exactly the two configs (`C60`,`C70`) never
independently checked. An unverified, angle-dependent settling residual in
`C60(θ)`/`C70(θ)` alone would masquerade as exactly the `ABSORB`-tracking
period-trend P-071-2 is built to detect.

---

## Discussion (supporting the two items above)

**On the settling gap, precisely.** Table trace, `phase1_proposal.md`'s
own Block table: `G1` reruns `C40`/`C80` at 600nm/STEPS=2800 to certify
*reuse* of already-settled data, not to certify anything new. `DENSE-
CAUSAL` runs `C60`/`C70` at cpl=20/STEPS=2800 — new FDTD spend, the entire
causal manipulation — with zero settling check attached. `R3-PEAK` runs
all four at cpl=**30**/STEPS=**4200**, which rescales *both* spatial
resolution and the physical geometry (`NX`/`NY`/`ABSORB` all ×1.5) —
this is a genuinely different simulation, not a same-geometry settling
probe of the `DENSE-CAUSAL` data. Nowhere does the design run `C60`/`C70`
at cpl=20, STEPS=2800 **and** STEPS=4200 (or any longer value) at matched
geometry, the one comparison that would actually answer "is 2800 settled
for these two specific configs." This is the same gap-shape this program
found and fixed for `C80` (exp-069) and for `C40` (exp-065) — but the
current design treats those two fixes as if they transferred to the two
configs actually generating this cycle's new data, which is precisely the
extrapolation the program's own house lesson (quoted above, from the
experiment that discovered STEPS=1400 was unsettled in the first place)
warns against.

**Is the risk plausible, not just formally open?** The existing STEPS=2800
per-cell table (exp-065, 600nm/±40°) shows `C40→C60→C70→C80` = −0.003559→
−0.003216→−0.003147→−0.003368 — non-monotonic in `ABSORB` (dips at C70,
rises again at C80) at a single angle, on data never checked against a
longer STEPS. A non-monotonic residual exactly matches the shape a
partially-decayed reflection transient would leave (different round-trip
path length per config, since `NX`/`NY` are NOT congruent-invariant, only
`A` is), and is the kind of small, angle-structured, unsettled artifact
that a 31-point/0.2°-step free-period search is specifically built to fit
a spurious sinusoid to — this program's own `_free_period_search` has
already twice (exp-069 `P*=2.84°`/`R²=0.63`, exp-070's `A_eff`/`A_alt`
near-matches) demonstrated it will find a well-fit period in structure
that later analysis showed was not what it first appeared to be. A
settling artifact specific to `C60`/`C70` is a live, EM-motivated
candidate for exactly that failure mode here, and the design has no gate
that would catch it.

**On the CONFIRM/REFUTE trend bands, secondarily.** `TREND_CONFIRM_MIN_R2
=0.50` and `TREND_REFUTE_MAX_R2=0.30` are carried over verbatim from
P-069-2's fixed-period-fit convention (a different quantity: an R² of a
sinusoid fit to 31 angle points, not a linear fit to 4 `ABSORB` values).
A 4-point linear regression has 2 residual degrees of freedom; R² is not
independently re-derived here from any noise model of `P*`'s own
uncertainty (no error bars on `P*` propagate into the trend-fit
`R²`/spread bands anywhere in the design). This is not disqualifying —
P-071-3's full 6-pair disclosure and the NEITHER branch's explicit
non-silent handling are real mitigations, honestly reused from exp-069's
house discipline — but "well-motivated from a wave-physics standpoint" is
the wrong description for it; it is a procedurally-consistent, not a
noise-derived, threshold, and should be described as such rather than
implied to carry independent statistical weight.

**On reciprocity/passivity.** No new material law or source is
introduced; `damp_e`/`damp_hx` remain purely dissipative for any
`ABSORB`/`PAD` value, so no new passivity risk exists. Nothing here is a
reciprocity concern — this is a one-port transmission/reflection reading
along a fixed source-observer axis, unchanged in kind from exp-065/069.

---

## Verdict: **support-with-changes**

The causal design itself — four congruent points on one physical axis,
reused data behind a bit-exact gate, an honest peak-cell resolution
extension — is sound EM bookkeeping and the right structure for the
question T28 needs answered. What should not survive unchanged into Phase
3: treating `STEPS=2800` as settled-by-inheritance for `C60`/`C70` when no
settling-closure check has ever been run on either config, at any angle or
λ, and this program's own prior finding on this exact channel says
settling checks do not transfer across geometry changes.

**Single parameter change that would flip this to unconditional support:**
add a `Block SETTLE-C60C70` mirroring exp-069's `Block SETTLE-C80`
construction exactly — `C60`/`C70` at θ∈{39°,40°} (or, better, the two new
peak angles 37.2°/41.4°), 600nm, STEPS=4200 vs. the already-planned
STEPS=2800 reading, scored against the identical ≤1%/≥5% relative bands as
P-069-4 — and make it a binding precondition on P-071-2 exactly as
P-071-4 already is. Cost: 4 new calls (2 configs × 2 angles), a few
minutes of wall-clock inside the existing budget's own de-scope margin
(90 min hard stop vs. 28.76 min projected) — cheaper than the R3-PEAK
extension this design already made unprompted for a comparable class of
residual gap.
