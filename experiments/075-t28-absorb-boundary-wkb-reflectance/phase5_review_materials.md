# PHASE 5 — REVIEW · MATERIALS & METAMATERIALS seat · Panel Iteration 52 (exp-075)

*Fresh sub-agent, blind to the other five Phase-5 reviews and to Red Team's
own Phase-5 final audit this cycle. Charter (PANEL.md, verbatim): "MATERIALS
& METAMATERIALS — sub-wavelength structure; what could physically realize
the proposed optical behavior. Owns the realizability bound (published /
plausible / unobtainium-with-parameters)." Read PANEL.md, LOGBOOK.md in
full, and this cycle's complete record (`phase1_proposal.md` with its
in-place `[PHASE-3 FIX]` corrections, `boundary_reflectance.py`/
`two_wall_cavity.py` + both results files, all five Phase-2 critiques,
`phase2_redteam_audit.md`, `phase3_synthesis.md`, `phase4_results.md`,
`NOTES.md`), plus `lab/fdtd2d.py` and `lab/materials.py`, before writing
this.*

---

## 1. Verdict: **PARTIAL**

Both tested boundary-reflectance-echo mechanisms — the single `-x`-wall
echo (Phase 1) and the correctly-derived two-wall cavity (Phase 3/4
mandatory fix) — REFUTE cleanly against the real T28 data, on a
methodologically careful, honestly-scoped, zero-FDTD instrument built and
run to this program's own house discipline (R4 reproduction, pre-registered
bands, a frozen prediction committed before the two-wall run touched real
data, a mandatory look-elsewhere/robustness leg on the one place a raw
number nominally cleared SUPPORT). From my own seat's charter this is a
genuine, well-earned narrowing: a specific, physically well-motivated
*structural* candidate for T28 — reflectance off the engine's own
domain-edge grading — is now closed off on two independently-derived
variants, not one. That is real progress, and PROMISING-adjacent on
process grounds.

It stays PARTIAL, not PROMISING, for the same reason the Combined Verdict
itself is REFUTE rather than a closed boundary: T28's own substantive
mechanism question — what actually produces the real, settled,
resolution-robust ~2.84° periodicity — is exactly where it was at
Iteration 46, six-plus cycles later, now having exhausted both the
differential/two-tone statistical-fit instrument class (formally retired,
Iteration 51's seventh-cycle rule) **and** the boundary-reflectance-echo
structural class (this cycle, both variants). PANEL.md's own "honest
alternative product" — a mapped constraint boundary — is what this cycle
delivers for the structural half of that space; it is not RULED OUT
(nothing here proves a *class* of mechanisms jointly impossible, only two
specific members of one class), and it is not a phenomenon-program result
at all (T1 route N/A throughout, correctly and consistently disclosed).

## 2. Independent re-verification (R4)

I re-ran, myself, from a completely fresh shell, both scripts this cycle
produced — not just read their committed JSON:

- `python3 boundary_reflectance.py` — reproduces every headline number
  bit-exact against `boundary_reflectance_results.json` and
  `phase1_proposal.md`: `P_model=15.0000°`, `R²=0.8587`/widened
  `R²=0.8785`, `rel_period_dev=4.2778`, shape `r²=0.2586`,
  `pearson_r=-0.5085`, `COMBINED VERDICT: REFUTE`, all three gates
  (G-LOSSLESS `2.220e-16`, G-N1 `1.404e-15`, G-PASSIVITY worst
  `|r|=0.006423`) passing.
- `python3 two_wall_cavity.py` — a genuine full re-run (not a JSON replay;
  it recomputes `n(x)`, `r(θ;ABSORB)`, and all three coherently-summed
  Huygens-Fresnel field terms at all 4 configs × 31 angles from scratch) —
  reproduces `two_wall_cavity_results.json` bit-exact: `D_left`/`D_right`
  tables, `P_model=15.0000°`, `R²=0.9062`/widened `R²=0.9178`,
  `rel_period_dev=4.2778` (identical to the single-wall figure, as
  claimed), shape `r²=0.3042`, `pearson_r=-0.5516`, circular-shift null
  `p=0.1953`, `COMBINED VERDICT: REFUTE`, `frozen_prediction_confirmed:
  true`.

Beyond re-running the committed scripts, I did three checks of my own that
are not restated from anyone else's work:

**(a) Independently re-derived the "matched-ε=μ" admittance claim from
scratch**, the physical claim my own Phase-2 critique this cycle and
`phase2_redteam_audit.md` §2b both rest on. TE (s-pol) wave impedance for a
stratified medium is `Z_TE = ωμ(x)/kx(x)`, with `kx(x) = k0√(ε(x)μ(x) −
sin²θ)`. For an ordinary (`μ≡1`) dielectric this gives the familiar
`Z_TE = ωε₀c/kx = 1/√(n²−sin²θ)`. This construct instead sets `μ(x)=n(x)`
(forced, per (b) below) with `ε(x)=n(x)` too, so `ε·μ=n²` and
`kx=k0√(n²−sin²θ)`, giving `Z_TE = n(x)/√(n(x)²−sin²θ)` — exactly
`reflection_coefficient`'s own `Z` line (`boundary_reflectance.py:195`),
an extra factor of `n(x)` relative to the ordinary-dielectric formula.
This is not a generic "effective index," it is the signature of a
magnetodielectric medium with `μ` tracking `ε` — confirming, independently,
that MATERIALS' Phase-2 attack and Red Team's own re-derivation (§2b of
the audit) are both correct, not merely plausible.

**(b) Cross-checked the forcing premise directly against `lab/fdtd2d.py`**
(not the proposal's paraphrase of it): `Sim.__init__` builds `damp_e`,
`damp_hx`, `damp_hy` from the *identical* `_damping(nx,ny)` call (same
`self.absorb`, same cubic ramp, same `exp(-0.30*d)`) at lines 98–100;
`Sim.run` damps `Hx`/`Hy` immediately after their curl update (lines
228/229, 237/238) and `Ez` after the curl update and source injection
(line 253) — E and H genuinely decay at the identical local rate at the
identical point, for both edges (only `Ez[1:-1,1:-1]` is ever written by
the curl step, line 240 — both `x=0` and `x=nx-1` are permanently zero,
confirming the two-PEC-wall premise `phase3_synthesis.md` §3.2 needs).
This is the code-level fact the entire matched-medium/realizability
argument is forced by, and it holds exactly as claimed.

**(c) Checked whether the "matched-ε=μ, unobtainium" scope caveat is
actually structurally distinct from this bench's own real, already-scored
physical absorber** — a question my own Phase-2 critique raised but did
not itself verify against code. Read `lab/materials.py::graded_black_shell`
(the object behind every T1/T5/T9/ESTABLISHED constraint-1/2 citation in
this program's history) directly: it writes `sim.sigma_e[shell] += ...`
and holds `sim.eps_r` at 1 (no `μ`/`_damping`-band involvement at all) —
an ordinary `μ=1`, conductivity-graded absorber, using `Sim.run`'s
*separate* `ca`/`cb` conductive E-update path, not the `_damping`
multiplicative-decay construct this cycle's entire transfer-matrix model
is built from. **This confirms, independently and at the code level, that
the two mechanisms are not merely conceptually different (as the
idealization-2 fix states) but literally implemented by disjoint code
paths in the same engine** — the REFUTE this cycle earns is fully
quarantined to `_damping`'s own domain-edge numerical construct and says
nothing, positively or negatively, about `graded_black_shell`-class
absorbers' own reflectance behavior. I did not find this specific
code-level disjointness stated anywhere in the cycle's own record
(`phase1_proposal.md`, `phase2_redteam_audit.md`, `phase3_synthesis.md`
all argue the realizability point from the *formula*, correctly, but none
cites `graded_black_shell`'s own source to show the two constructs never
share a code path) — a small, non-blocking addition worth folding into the
idealization note if this file is ever revised.

**(d) Re-derived Test B's null-calibration for the two-wall model from the
committed arrays, independently.** Because `n=31` real dense-sweep angles
leaves only **30** distinct non-zero circular shifts, the "N=20,000
trials" Monte-Carlo estimate is, for this specific array length, actually
sampling (with replacement) from a discrete population of 30 values, not a
continuum — worth knowing when reading the p-value's own precision, though
it does not change the qualitative reading here. I confirmed this two
ways: a fresh 20,000-trial Monte-Carlo run at an independent seed
(`p=0.1895`, matching the committed `p=0.1953` to Monte-Carlo noise), and
an **exhaustive** enumeration of all 30 possible shifts (not a sample):
`6/30 = 0.2000` shifts meet or exceed the observed `|r|=0.5516` — the
same "not significant" conclusion, now established exactly rather than by
sampling. `phase4_results.md`'s own reading ("NOT significant... the
null's own 95th percentile, 0.68, is not far above what was observed") is
correct and, on this exhaustive check, slightly conservative if anything
(the true small-sample distribution is discrete and I would flag `N=20,000`
as implying more granularity than a 30-point population actually has —
cosmetic, not load-bearing, since the qualitative verdict is unchanged
either way and the combined verdict does not depend on Test B at all,
§6 of the audit).

None of (a)–(d) moves any scored verdict. (a)/(b)/(c) reinforce the
realizability-scoping argument my own Phase-2 critique and Red Team's audit
both made; (d) is a minor, non-load-bearing precision note on an already-
correct reading.

## 3. Ranked top-3 candidates for Iteration 53

**(1) G40/PAD decorrelation (PLAN.md's own Iteration-52 queue item 2, ~31
FDTD calls).** This is the one item on the board that *relieves* rather
than discloses a real, three-cycle-old confound (`PAD = ABSORB − 40`
exactly across the entire congruent series since Iteration 48), and it
matters more, not less, after this cycle: with the boundary-reflectance-
echo class now doubly REFUTEd on the *existing* congruent series, any
future structural candidate that wants to test whether a real effect
tracks `ABSORB` depth specifically (rather than the domain padding that
has ridden along with it, unexamined, since Iteration 48) needs a
decorrelated design to test it on cleanly. The readout channel is already
specified (the phase-invariant amplitude `√(A_i²+A_q²)/a`, conditioning on
no fitted carrier phase, explicitly outside the seventh-cycle rule's
scope) and the geometry-reuse cost is already verified against
`experiments/065-.../design_geometry_output.txt`. Cheapest, least
speculative, most clearly still-authorized item on the board.

**(2) The record-hygiene bundle (queue item 3), with one MATERIALS-specific
addition.** Bundle exp-074's own corrections as queued, **and** — closing
the one gap I found in §2c above — fold in a one-line, code-adjacent note
tying the matched-ε=μ/unobtainium scope caveat explicitly to
`graded_black_shell`'s own disjoint code path (not just to the formula),
so a future citation of "REFUTE, boundary-reflectance-echo" cannot drift
toward reading it as bearing on this bench's own physical absorber family
even by analogy. Also: EM's Phase-2 finding (no gate tests cross-module
phase-convention consistency between `r(θ;ABSORB)` and `dg048`'s own
Huygens-Fresnel propagator) was correctly ruled informational-only this
cycle because Test A alone determines REFUTE regardless of it — but
`phase3_synthesis.md` §3.4 itself says this becomes load-bearing "the
moment a second coherently-summed echo term is added," which is exactly
what the two-wall model *is*. I'd tighten the forward-binding language: the
gate is now due on the *next* echo/cavity variant this program builds, not
merely "the third" — the two-wall model already used it twice (both
images), so a genuinely new third construction is what should trigger it,
worth stating unambiguously before it is forgotten across a rotation gap.

**(3) A genuinely new structural candidate, flagged speculative and
in need of its own look-elsewhere control before it is trusted — not yet
priced.** This cycle's own §5b/§2e cross-check (VISION's flagged gap,
independently sharpened by Red Team and Phase 3) established that the real
T28 residual signature is essentially **`ABSORB`-depth-independent**
(cross-config shape correlation `r=0.992–1.000`, exp-074), while *both*
tested boundary-echo mechanisms are strongly depth-*dependent* by
construction (the model's own echo amplitude scales 6.8×–41× across the
tested depths, §5b) — the opposite signature. That argues, on this
cycle's own evidence, for a mechanism tied to whatever *is* held fixed
across the congruent `ABSORB` series rather than to the band itself: per
`experiments/065-.../design_geometry.py`, the object/flank/guard window
geometry (`R_OUT=78`, `GUARD_OUT=185`, `W_FLANK=78`), `LEVER`, and `D_SP`
are all held bit-identical across every `ABSORB` config by the PAD
construction's own design intent — only the source-to-wall distances and
the band's own profile move. Any effect tied purely to that fixed geometry
would, however, cancel in the `C80−C40` difference exactly as the
already-established, config-independent boundary-free term does
(`boundary_free_spread_internal_check=0.0`, this cycle) — so a viable
version of this idea needs a mechanism that is *nearly but not exactly*
config-invariant (a secondary interaction between the T21 source-aperture
fringe, itself config-invariant at `A=752`, and something that shifts by a
few cells with `PAD`, most plausibly a residual-of-residual from
imperfect single-sinusoid fitting rather than a distinct physical echo).
I am not proposing this as a priced, ready-to-run design — I do not have
one — and Red Team's own §3 look-elsewhere finding this cycle (2 of 11
named length scales landing in-band under a naive substitution) is a
direct, recent warning against treating "shares the right qualitative
signature" as evidence on its own. I rank it third, behind two concretely
scoped, cheap items, precisely because it needs real design work and a
pre-registered null-permutation control (per R5's addendum) before it
earns FDTD time — but it is, to my reading of the full record, the most
substantively motivated open lead this cycle's own data actually points
toward, and is worth a seat with EM/PHOTONICS charter picking up.

## 4. What a general-purpose read would miss, from this seat's charter

Two things, both bearing on realizability scoping specifically:

**Correctly done, and worth crediting explicitly**: the matched-`ε=μ`
idealization this cycle added (Idealization 2, `[PHASE-3 FIX]`) is not
boilerplate — it is the difference between "boundary-reflectance
mechanisms are ruled out" (false, and exactly the kind of scope-creep
LOGBOOK's own R1/T9 precedents exist to prevent) and "this one, forced,
non-realizable numerical construct's reflectance is ruled out" (true, and
what the data actually supports). A general read that only tracks
Test A/B's REFUTE would not distinguish these, and a future cycle citing
this REFUTE without the scope note could wrongly treat *any* future
graded-absorber-reflectance proposal as pre-refuted. The idealization
note, `phase2_critique_materials.md`'s original attack, and Red Team's
independent re-derivation all get this right; my own re-derivation (§2a
above) confirms it a fourth time.

**Confirmed, not previously shown at the code level**: this REFUTE's
scope is even narrower than "not a realizable optical material" — it is
specific to the engine's own `_damping` construct, which literally never
executes in the same code path as `graded_black_shell` (the bench's
actual, already-realizability-scored absorber, `σ_e`-based, `μ≡1`). I
verified this directly against `lab/materials.py` (§2c above); nothing in
the cycle's own record states it this concretely. This matters going
forward specifically because T5's thermal-sidecar and every constraint-1/2
verdict this program has ever issued rest on `graded_black_shell`'s own
physics — this cycle's REFUTE, correctly read, cannot be cited against any
of that, and should not need re-deriving each time a future cycle touches
either construct.

Both points are the kind of "which numerical object does this claim
actually cover" question this seat exists to police, and both hold up
under independent re-derivation from the primitive sources (the admittance
algebra, `lab/fdtd2d.py`, `lab/materials.py`) rather than from any other
seat's or the Director's own prose.
