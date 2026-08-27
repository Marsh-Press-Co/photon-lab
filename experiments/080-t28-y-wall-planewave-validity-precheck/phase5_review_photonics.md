# PHASE 5 — REVIEW · PHOTONICS · Panel Iteration 57 · exp-080

**Seat: PHOTONICS** (surface interaction, absorption spectra, angular
dependence, scattering cross-sections; owns: is the proposal's optical
response coherent as stated, across wavelength and angle?). Fresh context,
blind to the other six seats' Phase-5 reviews this cycle. Read `PANEL.md`,
`AGENTS.md` in full; the complete exp-080 record in order
(`phase1_proposal.md`, `validity_precheck.py` as it now stands post-fold-in,
`validity_precheck_results.json`, all five Phase-2 critiques,
`phase2_redteam_audit.md`, `phase3_synthesis.md`, `phase4_results.md`,
`_output.txt`); for background, `experiments/079-.../phase5_redteam_audit.md`
§3/§7 and my own seat's prior review, `experiments/079-.../
phase5_review_photonics.md` §4 (the construction this whole cycle is about).
Also read `y_wall_aperture_sum.py`, `boundary_reflectance.py`,
`design_geometry.py` directly, and `lab/validation/VALIDATION.md`'s
measurement-lessons section. All numeric claims below marked "verified" were
recomputed by me, in a fresh scratch script, from the same already-gated
primitives this cycle imports — never taken on any seat's word.

## 1. Verdict on the whole cycle: **PARTIAL**

I concur with the record's own self-scoring, arrived at independently from
my own discipline's angle. Nothing in this cycle is ruled out under R1–R9,
and nothing here is a positive signal toward reproducing T28. What the cycle
actually delivers, from a PHOTONICS lens, is a coherent and self-consistent
(if uniformly negative) picture of this aperture's optical response at the
angles it is actually asked to operate at: (a) the near-field/far-field
violation is real and — I independently checked below — not an artifact of
the single 600nm wavelength tested; (b) the single-angle summary and (d) the
θ_beam-dependent image-term construction both fail for the same underlying
reason (the aperture's per-point bounce angle spans 5.3–15.0°, while
PHOTONICS' own `90°−θ_beam` argument samples 48–54° — a completely different
part of the wall's admittance response, §0.7/Attack-2-of-QUANTUM's own
correct point); and (c) the negative-`R²(abs)` pathology concentrated at
ABSORB=70/80 has a genuine, checkable optical mechanism (§3 below), not just
an "unexplained" flag. None of this is a proven mechanism-class boundary yet
(Checkpoint criterion 2, correctly, NOT YET RIPE per both Red Team and the
Director) — the decisive test (pair-delta periods vs. real T28 data) remains
unrun. **PARTIAL** is the right word for a cycle that narrows the board
cleanly without closing it.

## 2. Independent numeric verification (re-derived, not restated)

**(i) Reproduced `R²(Re, theta_eff primary)` for C70 bit-exact, from a
from-scratch script that does not import `validity_precheck.py`.** Rebuilt
the true per-point curve via `ywas.echo_field_curve`'s own constituent
primitives, checked it against `y_wall_aperture_sum_results.json` (drift
`0.0`), computed `theta_eff` fresh (`8.286452241908538°`), built the
single-angle model curve, and scored `R²(Re)`:

```
R2(Re, theta_eff primary) for C70, freshly reimplemented: 0.5214450714184593
committed JSON value:                                     0.5214450714184593
```

Exact match, to full float precision — the same number Red Team's own
from-scratch audit already found. This adds a fourth independent
reproduction of this specific figure (proposal, Red Team, and now this
review), from a script none of the prior three shared code with.

**(ii) Wavelength-generality check on the (a) FORECLOSE verdict — not
computed anywhere in this cycle's own record.** Part (a) is scored at 600nm
only (`λ=20` cells). This program's own metrics table (`PANEL.md`) commits
to a 450/600/750nm sweep as a standing "witness realism" requirement, and
Red Team's own Iteration-58 recommendation (item 3) flags the 750/450nm leg
as still deferred. Since `d_F=W²/λ` is wavelength-dependent while
`dist_image` and `theta_local` are pure geometry (no λ dependence at all), I
checked whether the FORECLOSE verdict is fragile to wavelength using
`br.CPL={450:15, 600:20, 750:25}` (cells):

```
lambda_nm  lambda_cells  d_F=W^2/lambda (cells)
450        15            150,801.1
600        20            113,100.8
750        25             90,480.6

dist_ratio at 450nm: 0.57% (near edge) - 1.61% (far edge)
dist_ratio at 750nm: 0.95% (near edge) - 2.68% (far edge)
(600nm, for comparison: 0.76% - 2.15%)
```

**Result: FORECLOSE is robust across the program's own full 3-λ sweep, not
an artifact of the single wavelength tested.** At 450nm the aperture sits
*even deeper* in the Fresnel zone (shorter wavelength → larger `d_F`); at
750nm the margin loosens slightly but stays two orders of magnitude short of
the 10% FORECLOSE threshold and three orders short of the 100%
DOES-NOT-FORECLOSE threshold. `theta_local`'s own spread ratio is wavelength
independent (pure geometry), so it clears FORECLOSE identically at all three
wavelengths. This is a small, cheap, previously-unrun check that closes a
gap none of the five critiques or Red Team's audit raised: nobody asked
whether reporting FORECLOSE at 600nm alone was itself defensible before the
deferred wavelength leg runs. It is.

## 3. A mechanistic account of the ABSORB-depth-concentrated negative `R²(abs)` — refining, not just restating, an already-flagged open question

PHOTONICS' own Phase-2 critique, THERMODYNAMICS' Phase-2 critique, and Red
Team's Attack 4 all independently flag the same pattern (clean at
ABSORB=40/60/G40, catastrophic `R²(abs)` at ABSORB=70/80) as a real,
unexplained optical-response question. I ran one further check none of them
did: a fine angular sweep of `|r(theta_local)|` across the aperture's actual
`[5.2°,15.1°]` envelope, at all four ABSORB depths, to see not just the
*magnitude* of the swing (already reported) but its *shape*:

```
ABSORB=40: |r| min/max ratio = 1.30x, NON-monotonic (has an interior dip)
ABSORB=60: |r| min/max ratio = 2.21x, monotonic increasing
ABSORB=70: |r| min/max ratio = 7.23x, monotonic increasing
ABSORB=80: |r| min/max ratio = 8.67x, monotonic increasing
```

This is a clean, monotonic trend in ABSORB, and it is a coherent effect, not
a numerical artifact: `theta_local` here is measured from the wall's own
normal, so 5–15° is close-to-normal incidence, where a purely dielectric,
weakly-lossy stack's `|r(θ)|` is normally close to flat. As the graded
absorption depth (`ABSORB`) grows, the extra path length a ray picks up
inside the lossy layer by moving from 5° to 15° off normal (`∝1/cos θ`)
becomes large relative to the layer's own absorption length, so `|r(θ)|`
develops real curvature over exactly this window — and past some depth
(between ABSORB=40 and 60) the curve's shape crosses from having an interior
extremum to being monotonic across the full aperture envelope, which is
exactly why the fixed single-angle model's zero-crossings move the most at
ABSORB=70/80. **This is disclosed as additional, confirmatory context, not
a reversal of anyone's verdict** — the calibration-vs-shape split PHOTONICS'
own critique already made (§0 item 6, independently reproduced by Red Team)
still stands as the primary correction; this adds *why* the shape component
is concentrated there.

## 4. Task question (1): does `photonics_image_term_curve()` correctly implement my own exp-079 §4 sketch?

**No — it implements only half of it, and that half's own key omission
(`E_direct`) is more resolvable than the record currently states.**

My own exp-079 §4 review's construction (quoted from that document, step 4):

> **Total field:** `E(θ_beam) = E_direct(θ_beam) + r(90°−θ_beam;ABSORB) ·
> E_image_unweighted(θ_beam)`

`photonics_image_term_curve()`, as committed, computes only the second term:

```python
curve.append(r_at_beam[i] * w)   # w = the unweighted mirrored-aperture sum
```

There is no `E_direct` anywhere in the function. Its own docstring is
honest about this ("`E_direct(theta_beam)` is OMITTED here... flagged, not
resolved, by this file"), and Red Team's fix docket (item 5, LOW) and the
Director's Phase-3 synthesis (fix 5) both carry the caveat forward. So the
omission is disclosed, not hidden — but two things about it are worth
separating, which the record currently does not:

**(a) For THIS cycle's own scoring, the omission is benign, by construction,
not merely "flagged."** `y_wall_aperture_sum.py`'s own docstring states
`echo_field_curve` computes "the per-point complex contribution to the
REFLECTED (echo) field" — i.e., the true curve `photonics_image_term_curve()`
is compared against (`E_echo`) is *itself* echo-only, with no `E_direct`
term anywhere in it either. Comparing an echo-only model against an
echo-only truth is apples-to-apples; `E_direct`'s absence introduces no bias
into part (d)'s own `R²` numbers. Nobody in the record states this
explicitly, so it reads as more of an open gap than it is for the specific
comparison actually run.

**(b) For the *downstream* use the record itself recommends next — scoring
`PAIR_PAD`/`PAIR_ABSORB40`/`C80−C40` deltas of the *total* field
(`E_direct+r·W`) against the real, measured T28 reference periods — the
omission's validity is not merely "inherited-not-independently-verified." I
checked it, with zero new machinery, using only primitives
`validity_precheck.py` already imports:

```python
# "E_direct" reconstructed analogously to the x-wall's own E_d
# (boundary_reflectance.py::c_empty_with_wall): the SAME taper and
# driven-phase convention as the echo term, but propagated over the
# DIRECT (non-mirrored) source-to-observer distance hypot(D_SP, OBJ_Y-y_s),
# no wall, no r().
```

Result, at 5 θ_beam values across all 5 congruent configs:

```
max |E_direct(cfg) - E_direct(C40)| across the theta grid:
  C40: 0.000e+00   C60: 0.000e+00   C70: 0.000e+00
  C80: 0.000e+00   G40: 0.000e+00
```

**`E_direct(θ_beam)`, defined this way, is bit-identical across all five
congruent configs, at every θ_beam tested — not approximately, exactly.**
This is not a coincidence to be re-checked with more data; it follows
directly from the congruent-series's own explicit design
(`design_geometry.py`'s header: "D_SP, LEVER, window geometry unchanged, for
every ABSORB," and `y_lo`/`OBJ_Y` both shift by the identical `PAD` amount).
Substituting `u=y_s−OBJ_Y` makes the taper, the driven phase, and the direct
propagation distance all manifestly PAD-invariant — `ABSORB` never enters
the direct term at all (it only enters through `r()`, on the echo side).
**Consequence: an `E_direct` term of this (the natural, x-wall-analogous)
form cancels EXACTLY in every one of the three pair-deltas Iteration 58 is
asked to run — `PAIR_PAD`, `PAIR_ABSORB40`, and `C80−C40` alike — not merely
"insofar as it cancels," but provably, from geometry the record already has
committed.** This is a positive, resolved finding, not an open flag, and it
required no FDTD and no new gated primitives — only composing functions
`validity_precheck.py` already imports.

**Caveat, stated honestly:** this rests on `E_direct` being defined the one
physically natural way consistent with the x-wall's own established
convention (a direct, unmirrored Huygens sum from the SAME real aperture to
the SAME observer point) — nobody has committed that definition to code
before this review, so this is my own reconstruction from the established
analogy, not a re-derivation of an already-agreed formula. But it is the
*only* definition consistent with what "E_direct" is required to mean by
the method-of-images structure the whole y-wall program borrows from the
x-wall (`E=E_d+r_coeff·E_i`), so it is not an arbitrary choice either.

## 5. Task question (2): is the Director's Phase-3 characterization of the fix docket complete and accurate?

**Four of five items, yes, checked line-by-line against Red Team's own
docket — faithful, complete, no content dropped.** Fix items 1–4 in
`phase3_synthesis.md` §2 restate Red Team's own §3 items 1–4 with matching
numbers, matching priority tags, and matching "not resolved here" framing
for item 4's ABSORB-depth question. I found no discrepancy in these four.

**Item 5 is where something is lost — an overstatement, not an omission.**
Red Team's own docket item 5 (§3, LOW) reads: *"Note explicitly, as an
inherited-not-verified assumption, that QUANTUM's (and PHOTONICS' §4)
construction omits `E_direct(θ_beam)`... **Cheap to check; not yet done.**"*
The Director's synthesis (§2, fix 5) restates the flag correctly but then
adds a claim Red Team never made: *"resolving it would require new
machinery this cycle's own zero-FDTD, desk-only scope does not cover."*

This is not accurate, and §4 above demonstrates it directly: resolving
whether `E_direct` cancels required exactly the same kind of ~15-line glue
function this SAME cycle already wrote five times over
(`reflection_coefficient_vec_realizable`, `single_angle_curve_realizable`,
`photonics_image_term_curve`, `part_b_abs_calibration_corrected`,
`part_c_power_budget_at_true_angle` — every one of them a new function,
zero new FDTD, built from already-gated primitives, folded into this
cycle's own committed code without a fresh freeze cycle). Red Team's own
"cheap to check" was the correct read; the Director's synthesis, in
elevating this to something needing machinery "this cycle's own... scope
does not cover," inflates the item's difficulty in a way that is
inconsistent with the cycle's own demonstrated practice one paragraph
earlier in the same document. It is a small, LOW-priority item either way —
this is not a program-integrity problem — but it is exactly the kind of
"lost/mischaracterized between Red Team's audit and the Director's
synthesis" gap this review was asked to check for, and it is real.

## 6. New finding this review surfaces (summary)

The `E_direct` cancellation across `PAIR_PAD`/`PAIR_ABSORB40`/`C80−C40` is
not an open assumption for Iteration 58 to carry forward and "check
eventually" — it is desk-provable right now, with the primitives already in
hand, and I have provided that proof (§4). This converts fix-docket item 5
from a LOW-priority open flag into a closed, zero-cost precondition:
whoever in Iteration 58 builds the full
`E_direct(θ_beam)+r(90°−θ_beam)·W(θ_beam)` construction for the actually-
decisive free-period test does not need to separately re-verify this
assumption — they can cite this derivation and move directly to the
free-period fit, saving a step Red Team's own queue (item 1) currently
lists as still-to-be-checked "before treating it as final."

Secondary, confirmatory findings: (i) the FORECLOSE verdict is robust across
the program's own full 450/600/750nm sweep, not just the 600nm tested this
cycle (§2ii) — closes a small generality gap nobody flagged; (ii) the
ABSORB-depth concentration of the negative `R²(abs)` pathology has a
coherent optical mechanism (progressively more curved `|r(θ)|` over the
aperture's own near-normal envelope as absorption depth grows, crossing from
a non-monotonic to a monotonic shape between ABSORB=40 and 60) rather than
remaining a bare, unexplained correlation (§3).

## 7. Recommendation for Iteration 58

I do not dispute Red Team's/the Director's own queue (§6 of both documents):
check `E_direct` cancellation, run the free-period fit on
`photonics_image_term_curve()`'s pair deltas against real T28 data, pair
with the 750/450nm leg, weigh the PAD-loaded real-article check. My only
addition: **item 1 of that queue (check `E_direct` cancellation) is now
done — cite §4 above rather than re-deriving it** — and the 750/450nm leg
(item 3) should also fold in the near-field-margin table at §2(ii), since it
is already computed and directly bears on whether the aperture stays deep
in the Fresnel zone at every wavelength this program's own metrics table
commits to checking.

No RULED-OUT item (R1–R9) is re-proposed or re-litigated by this review.
