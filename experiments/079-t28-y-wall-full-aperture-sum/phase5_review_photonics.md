# PHASE 5 — REVIEW · PHOTONICS · Panel Iteration 56 · exp-079

**Seat: PHOTONICS** (surface interaction, absorption spectra, angular
dependence, scattering cross-sections). Fresh context, blind to the other
six seats' Phase-5 reviews this cycle. Read `PANEL.md`, `AGENTS.md`,
`LOGBOOK.md` in full (RULED OUT R1–R9; ESTABLISHED; LIVE THREADS in full,
close attention to T28's Iteration 46–55 history), `experiments/078-t28-y-
wall-echo-prescreen/phase5_redteam_audit.md` in full, this cycle's complete
record in order (`phase1_proposal.md` as corrected in place, all five
Phase-2 critiques, `phase2_redteam_audit.md`, `phase3_synthesis.md`,
`phase4_results.md`, `y_wall_aperture_sum.py`,
`y_wall_aperture_sum_results.json`, `_output.txt`), and
`experiments/075-.../boundary_reflectance.py`,
`experiments/065-.../design_geometry.py`,
`experiments/048-.../design_geometry.py::field_and_h`,
`lab/fdtd2d.py::Sim.add_line_source`.

## 1. Verdict: **PARTIAL**

The cycle's headline is correct and, on my own independent re-derivation from
the actual source code (not the write-up's prose), holds up cleanly: the
recovered `~2.02°` oscillation is the shared aperture window's own T21-family
content, and the construction that recovered it is provably incapable of
telling a real y-wall echo from no echo at all, at any period. That is a
genuine, well-earned negative result about *this specific instrument*, not
about the y-wall mechanism class. It is PARTIAL, not PROMISING, because
nothing here advances or forecloses whether a real y-wall coherent echo
exists — the instrument that could answer that question was never built this
cycle — and PARTIAL, not RULED OUT, because Red Team's own §8/§9 recommends a
structurally different construction that has not been tried and is not, on
my own analysis below, obviously doomed. My own independent contribution this
review: a from-primitives feasibility probe of that recommended construction
(§4) that neither this cycle's document nor any of its five critiques
computed.

## 2. Independent verification performed, from primitives

**(a) Re-derived T21's own reference period independently, not from any
citation.** `P(39°) = λ/(A·cos39°)` with `λ=CPL[600]=20` cells, `A=752`:
computed `1.960795°`, matching the cited `1.9608°` bit-for-bit (to the
printed digit). This is the number every downstream comparison in this
cycle's §5.3/§7 is measured against, and it was worth confirming from the
bare formula rather than trusting the write-up's own citation chain.

**(b) Re-derived `theta_local(y_lo)` for `C40` independently, from the raw
geometry, not from the JSON.** `atan(223/(792+40)) = 15.0043°`, matching the
proposal's own §2 table exactly.

**(c) Independently recomputed the corrected `ss_tot`-ratio order-of-
magnitude figure (Red Team's Attack 2 fix).** `9.392×10⁻⁷ / 5.9×10⁻²⁷ =
1.59×10²⁰`, `log₁₀ = 20.20` — confirms "≈20.2 orders of magnitude," the
corrected figure now in `phase1_proposal.md` §1/§5.2/§7, not the as-filed
"nine orders" error. I did this from the two raw ratios, not by re-reading
Red Team's own arithmetic.

**(d) Independently recomputed `A_eff = A·P_T21/P_T28 = 752·1.9608/2.8421 =
518.8141`** — confirms, to four significant figures, that this is the same
quantity LOGBOOK's own R5 addendum (Iteration 47, exp-070) already found and
ruled a null-permutation-indistinguishable-from-chance dead end
(`A_eff≈518.81`). Idealization 11's forward caution is not an assertion I
took on faith; it reproduces.

**(e) Read the structural claim (Attack 1) directly out of
`y_wall_aperture_sum.py`'s own function bodies, not out of any Phase-2/5
prose describing it.** `theta_local_deg(y_s, cfg)` and `dist_image_cells(y_s,
cfg)` both take only `y_s` and static per-config `cfg` fields (`d_sp`,
`obj_y`) — no `theta_beam` argument anywhere in either signature or body.
`source_driven_phase(y_s, theta_beam_deg, cfg)` is the *only* one of the
three per-point ingredients that takes `theta_beam_deg`. `echo_field_curve`'s
own docstring states this explicitly and its code matches: `r_of_ys`,
`amp_of_ys`, and `dist_img` are computed once per `(config, oversample)` via
`r_vec_cache` and reused unchanged across the whole `thetas_beam_deg` loop —
only `phase_drive` is recomputed per angle. This is the same structural fact
Red Team's audit derived analytically (§2 there) and QUANTUM confirmed
empirically (the `r≡1` ablation) — I confirm it a third, independent way, by
reading the actual per-point functions the coherent sum calls.

**(f) Confirmed `G40`/`C80`'s shared geometry directly from the parameter
table**, not from the ablation-control's own printed claim: both rows list
`OBJ_Y=832, y_lo=80, y_hi=1584` — identical. This is why `PAIR_ABSORB40`'s
ablated delta comes back *exactly* zero (§5, ablation JSON), not merely
small — a geometric fact I checked against the table myself before accepting
the mechanistic explanation for it.

**(g) A feasibility probe of Red Team's own §8/§9 recommendation, computed
fresh for this review (§4 below)** — not present anywhere in this cycle's
record, its critiques, or exp-078's.

## 3. Does the ~2.02° period generalize the flat result, mechanistically —
## and does my own prior-cycle 2.55° residual deserve more weight than the
## ruling gives it?

**The mechanistic story is genuinely, not merely asserted, correct — I
re-derived it independently (§2e) rather than accepting Red Team's
derivation on its word.** `E_echo`'s only θ_beam-dependent ingredient is the
identical driven-phase ramp `k·sinθ_beam·(y_s−OBJ_Y)` that already produces
T21's own real fringe in the direct field, evaluated over the identical
`[y_lo,y_hi]`/`TAPER=40` window. A coherent sum of that ramp against *any*
static, θ_beam-independent envelope — smooth or not — is edge-dominated near
T21's own period by the same stationary-phase argument this whole T28
sub-thread has used since exp-078 §3.2. This was close to guaranteed once
`theta_local`/`dist_image` were fixed θ_beam-independent, for any envelope,
real or wrong — not a coincidence, and not something a finer aperture grid or
a different ABSORB depth would have changed.

**On my own charter's own residual-sideband finding (this cycle's §5.3
companion note, adopted from `phase2_critique_photonics.md`), re-examined
independently here rather than simply re-affirmed:** I agree with the
ruling that it is non-load-bearing, but I place more weight on a **magnitude
argument than the "it's just a sidelobe" mechanistic argument**, and I think
the record should say so more plainly than it currently does. The
mechanistic claim — that a residual at `2.55°` is a diffraction-grating
side-lobe of the same finite, tapered aperture, not an independent physical
channel — is *plausible* but was never independently derived from first
principles anywhere in this cycle's record; nobody computed, analytically or
numerically, what secondary period a raised-cosine-tapered top-hat aperture
of this exact width *should* produce as its own near-edge diffraction
overtone, and checked that `2.55°` matches it. Absent that derivation, "it's
a sidelobe" is currently an inference from plausibility, not a demonstrated
fact — a real, if narrow, gap Red Team's own audit does not fully close (it
rules the finding non-load-bearing, correctly, but characterizes it as
"mechanistically subsumed" more confidently than the record actually
earns). **What DOES settle the question, independent of which mechanistic
story is right, is magnitude, and this is where I differ in emphasis, not
in verdict**: the residual is `≈2.8%` of the primary fit's own `ss_tot`,
which is itself already `9.4×10⁻⁷` of the real data's own scale — so in
absolute terms the residual sits at roughly `2.6×10⁻⁵`× the real `PAIR_PAD`
signal's own `ss_tot`. Even in the maximally generous reading — treat it as
a genuinely distinct physical channel, not a sidelobe at all — it is five
orders of magnitude too small to be a candidate explanation for T28's real,
measured periodicity. The magnitude argument is decisive on its own, without
needing the sidelobe mechanism to be proven; I would state the disposition
that way (a size argument first, a plausible-but-unverified mechanistic
account second) rather than the reverse, which is how this cycle's own
record currently reads. This does not change PHOTONICS' Phase-2 verdict or
this document's own Combined Verdict — it is a sharpening of *why* the
finding is safely set aside, not a re-opening of it.

## 4. Is Red Team's §8/§9 recommendation correct, physically? A concrete
## derivation route, and a feasibility probe

**Yes, on my own independent physical analysis — this is the right next
move, for a reason I can state precisely rather than by analogy alone.**
The x-wall's own two-plane-wave reduction (`experiments/078-.../
phase1_proposal.md` §3.1, re-verified by me at §2e above by reading
`boundary_reflectance.py`'s `image_geometry`/`c_empty_with_wall` directly)
works because mirroring the source *in x* leaves the y-driven phase ramp
completely untouched — the image aperture is the *same* coherently-steered
array, merely translated in x — so the WHOLE aperture, image and real alike,
presents a single, well-defined, θ_beam-dependent incidence angle to the
x-normal wall (θ_beam itself, since x is both the wall's normal and the
aperture's own steering axis). `boundary_reflectance.py`'s
`c_empty_with_wall` literally encodes this: one scalar `r_coeff` multiplies
the *entire* image field `E_i` (`E = E_d + r_coeff*E_i`), not a per-point
weight — `reflection_coefficient` is evaluated ONCE per θ_beam, at θ_beam
itself, and applied globally.

Every y-wall model this six-cycle sub-thread has built so far (exp-078's
single edge, this cycle's full aperture) instead evaluates `r()` at a
*per-point*, static-geometry bounce angle — the natural generalization of
"where does this one point's own image sit," but never the "what angle does
the whole coherently-steered beam make with the wall" question the x-wall
model actually answers. That is the root of Attack 1's finding, and it is
also exactly what a genuine plane-wave/global-steering picture would fix:
apply ONE scalar `r(90°−θ_beam;ABSORB)` — reusing `reflection_coefficient`/
`reflection_coefficient_vec` completely unchanged, just at a different
angle argument than either did — to the ENTIRE reflected-aperture sum, not
to each point's own static image geometry.

**Concrete derivation route (sketch, not built):**

1. **Image the source positions in y, not x.** For every real aperture
   point at `(SRC_X, y_s)`, its image through the `y=0` wall sits at
   `(SRC_X, −y_s)`. Critically — mirroring the x-wall's own established
   principle (`experiments/078-.../phase1_proposal.md` §3.2: "an image
   source preserves the real source's own instantaneous phase... from the
   mirrored position") — the image point radiates with the SAME complex
   amplitude/phase `_src_amp`/`aperture_amplitude`·`exp(i·phase(y_s))`
   the real point at `y_s` carries, *not* a phase recomputed at the mirrored
   position `−y_s`. This is the one piece that must NOT change relative to
   the per-point models already built.
2. **Build the image field as a full Huygens sum over the mirrored
   positions**, reusing `dg048.field_and_h`'s own constituent primitives
   (`aperture_profile`/`_src_amp`'s taper-and-phase formula, and the
   `G0=exp(i(kr−π/4))/√r` propagator it already uses) rather than
   `field_and_h` itself as a black box — `field_and_h`'s own `_geom_derived`
   hard-codes `y_src=y_obs=arange(y_lo,y_hi)` from the SAME `g` fields for
   both source and observation, so it cannot be reused unmodified the way
   `image_geometry`'s one-line `D_SP` edit sufficed for the x-wall. The
   image-to-observer distance is `hypot(D_SP, y_obs+y_s)` (image at `−y_s`,
   observer at `y_obs`; this is `dist_image_cells` already generalized to
   every `y_s`, reused unchanged from this cycle's own code) — this part
   already exists.
3. **Weight the ENTIRE image sum by ONE scalar `r(90°−θ_beam;ABSORB)`**,
   evaluated at the swept beam angle — not per aperture point. This is the
   single structural change from every prior y-wall model, and it is the
   piece Attack 1 says is missing: `r()` finally carries genuine θ_beam
   dependence.
4. **Total field:** `E(θ_beam) = E_direct(θ_beam) + r(90°−θ_beam;ABSORB) ·
   E_image_unweighted(θ_beam)`, scored by the identical
   `_free_period_search`/`score_period` machinery every T28 cycle since
   Iteration 46 has used.

**Is this buildable with existing gated machinery, zero new FDTD, the way
the x-wall model was? Partially — buildable, yes; as cheaply as the x-wall's
own trick, no, and that distinction matters.** Every *formula* involved
(`_src_amp`'s taper-and-phase, `G0`, `reflection_coefficient_vec`,
`dist_image_cells`) already exists and is already gated — zero new physics,
zero new FDTD. But unlike the x-wall's `image_geometry`, a one-line edit to
an existing function's input dict, the y-wall version needs a genuinely new
(if short, on the order of the existing `echo_field_curve`) glue function,
because `field_and_h` cannot be handed a mirrored source array without
bypassing its own convenience wrapper. That new function would need its own
small validation battery before being trusted, matching this program's own
R4/verify-before-claim standard already applied twice this cycle (the
vectorized `r()` bit-exact check, §2b/§5.1) — at minimum: (i) a sanity check
that in the limit of a vanishingly narrow aperture the construction reduces
toward the already-validated single-edge/point-image model; (ii) a
passivity spot-check, though this is largely inherited for free from
`reflection_coefficient`'s own already-gated `|r|≤1` guarantee, since the
new code only ever multiplies an already-bounded scalar against a Huygens
sum, introducing no new gain mechanism. This is a same-order-of-magnitude
cost to what this cycle itself already built (a few hours of desk work, not
a new engine feature), not a one-line trick — an honest correction to how
easily Red Team's own §9 phrasing ("mirroring what already, successfully,
makes the x-wall's own... reduction") could be read.

**A feasibility probe I ran fresh for this review, not present anywhere in
this cycle's record:** does `r(90°−θ_beam;ABSORB)`'s own phase vary fast
enough across the real 36°–42° sweep to plausibly produce a T28-matching
period on its own, or would it most likely show up as just another slow
envelope on the same T21 carrier? Using only `boundary_reflectance.py`'s own
already-gated `reflection_coefficient` (unchanged), I swept
`arg(r(90°−θ_beam;ABSORB))` over the real 31-point dense grid:

```
ABSORB=40: arg(r) spans 79.13deg to 154.34deg over the 36-42deg sweep
           (75.2deg of phase swing across 6deg of theta_beam)
ABSORB=80: arg(r) spans -312.44deg to -169.11deg
           (143.3deg of phase swing across 6deg of theta_beam)
free-period fit of cos(arg(r(90-theta_beam))) alone, both ABSORB depths:
           runs to the search boundary at 15deg -- no interior period
           resolved inside a 1-15deg window; the underlying phase swing
           implies a natural period on the order of 15-29deg, roughly
           4-15x longer than any period in T28's own 2.84-4.61deg family.
```

**Reading this honestly: `r(90°−θ_beam)` does now genuinely depend on
θ_beam — the structural defect Attack 1 identifies is fixed — but its own
characteristic angular scale is far slower than the 6° window can resolve
into an independent period, let alone one near T28's own band.** The most
likely outcome, if this construction were actually built, is that
`r(90°−θ_beam)`'s slow phase drift would show up as an amplitude/phase-
modulating envelope on top of the SAME T21-family carrier already present in
`E_direct` and in the image sum's own driven-phase ramp — an AM sideband
structure, not necessarily an independently-resolvable new frequency near
T28's own period. This is not a reason to skip building it: unlike every
per-point model tried so far, this construction is not *structurally
guaranteed* to fail regardless of the wall's reflectance (§2e), and whether
the envelope's own magnitude variation (not just phase — `|r|` swings
`1.6–3.9×10⁻²` at ABSORB=40 vs `2.0×10⁻⁴–1.9×10⁻³` at ABSORB=80 over the same
window, an order of magnitude difference in envelope depth between configs)
reshapes the effective near/far-edge balance enough to shift the recovered
period materially is a real, open, computable question this probe cannot
settle by itself — but it is a concrete, falsifiable, pre-registerable
prediction for whoever builds it: **expect the dominant recovered period to
still land close to T21's `1.96°`, with the interesting result being how far
off T21 it lands and whether that offset itself tracks `ABSORB` depth in a
way the per-point models could never produce (since their own `r()` weight
never varied with θ_beam at all).**

## 5. Ranked candidates for Iteration 57 (PHOTONICS' own view)

1. **Build the y-wall global-steering (single-scalar `r(90°−θ_beam)`,
   full-aperture-image) construction sketched in §4 — the genuinely
   different instrument Red Team's §8/§9 correctly identifies as needed,
   not a refinement of the per-point family. Desk-only, zero new FDTD,
   reuses `reflection_coefficient`/`reflection_coefficient_vec`,
   `aperture_profile`/`_src_amp`'s formulas, and `G0` unchanged; needs one
   new, short glue function plus the two small validation checks named in
   §4.** Pre-register my own §4 prediction before running it (dominant
   period likely still T21-proximate; the informative result is the size
   and `ABSORB`-dependence of the OFFSET from T21, not a clean SUPPORT/
   REFUTE on the first pass) so the run is falsifiable against a stated
   expectation, not scored post hoc. This is my #1 because it is the first
   y-wall construction in seven cycles whose own `r()` term is not
   analytically guaranteed to contribute zero new frequency content — every
   prior cycle's negative result was foreclosed by construction; this one
   is not.
2. **If item 1 is built and its dominant recovered period is (as my probe
   suggests is likely) still T21-proximate, immediately test whether the
   OFFSET from T21 — not the raw period — tracks `ABSORB`/`PAD` in a
   pattern the per-point models structurally could not produce.** This is
   the natural, cheap follow-on the AM-sideband picture in §4 predicts: a
   real wall-reflectance signature should modulate the T21 carrier's
   *phase/amplitude* even where it cannot shift its *frequency* outright,
   and a systematic `ABSORB`-dependent phase or amplitude offset — absent
   from every ablation-control result this cycle produced (§5.2/§5, all
   periods statistically indistinguishable under `r≡1`) — would be the
   first genuinely new, mechanism-discriminating signature this six-cycle
   sub-thread has found. Contingent on item 1's own result, not independent
   of it.
3. **Independently re-derive, from the raised-cosine taper formula itself
   (not the aperture width alone), what secondary diffraction period a
   `TAPER=40`-cell Hann edge on a `1504`-cell top hat should produce as its
   own near-edge overtone, and check it against the `2.55°` residual (§3)
   — desk-only, a standard slit-diffraction/apodization calculation, no new
   machinery.** This closes the one genuine, if narrow, gap I found in this
   cycle's own record (§3): the "it's just a sidelobe" mechanistic story for
   the residual sideband is plausible but was never actually derived and
   checked against a closed-form prediction, only asserted by analogy. Low
   priority relative to items 1–2 (the residual is five orders of magnitude
   too small to matter to T28's real signal regardless of which story is
   right), but it is a real, cheap, close-off item that would make this
   cycle's own record fully earned rather than merely plausible on this one
   point.

None of these three repeats a RULED-OUT item (R1–R9) or a named dead end
(`A_alt≈3·R_OUT`, the `519`/`A_eff≈518.81` cluster — independently
reconfirmed as the same number at §2d, cited here only as a forward caution,
never as a candidate fix — the P-normalized phase-offset regressor, or the
x-normal/unrealizable-admittance coherent echo). All three are zero-FDTD,
reuse only already-gated machinery plus the one short glue function named in
§4, and none require the far-wall/far-edge pair Red Team's own §8 correctly
argues would inherit Attack 1's limitation unchanged.

## Compliance note

No RULED OUT item is re-proposed or re-litigated. This review does not
modify `LOGBOOK.md`/`PLAN.md`/`SESSION_LOG.md`/`lab/ARTIFACTS.md`/
`lab/artifacts.py`/`AGENTS.md` or any other experiment file, and makes no
git changes.
