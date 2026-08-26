# Phase 5 Review — ELECTROMAGNETISM

**Cycle: exp-076, Panel Iteration 53 (G40/`PAD` decorrelation).** Fresh
context, blind to all other Phase-5 outputs this cycle. Read `LOGBOOK.md` in
full (RULED OUT R1–R8; LIVE THREADS in full, T21/T24/T27/T28 closely) and the
complete exp-076 record: `phase1_proposal.md`, all five `phase2_critique_*.md`,
`phase2_redteam_audit.md`, `phase3_synthesis.md`, `NOTES.md`, `run.py`,
`phase4_results.md`, `results.json`. Independently re-derived every number
cited below from `results.json` and, where relevant, from
`experiments/065-.../design_geometry.py`'s own construction code — nothing
here is taken from prose.

---

## 1. Verdict: **PARTIAL**

This is a clean, well-audited instrument build that answers its own
pre-registered question (`PAD_TIED`, not `ABSORB_TIED`) with a decisively
passed settling precondition — real, load-bearing progress on what a future
mechanism must explain. But no energy/passivity bookkeeping was ever attached
to the result, and doing that bookkeeping (§3, below) shows the finding is
narrower and more informative than "PAD-tied" — it is close to a first-
principles necessity, not a surprise, once the construction is examined. The
750nm advisory leg's ordering flip has a physically coherent candidate
explanation but is carried by an instrument leg with a real, previously
undisclosed hole (§4). T28's own substantive mechanism question is not
resolved — narrowed, correctly, in the less convenient direction, exactly as
`phase4_results.md`'s own Bottom Line states.

---

## 2. The settling gate: decisively passed, not a close call

Docket item 4's HALT-if-fails precondition (`STEPS=2800` vs `STEPS=4200` at
θ∈{39°,40°}, 600nm) is the one dynamical check this cycle ran on G40's own
previously-untested (thin `ABSORB=40` boundary sitting at C80's larger,
`NY=1664` domain) geometry. Reading `results.json::settling_gate` directly:

| θ | `frac` (shift / `amp_ref`) | bar (`THRESH_LOW`) | margin |
|---|---|---|---|
| 39° | 1.035×10⁻⁴ | 0.04976 | **~481×** inside the bar |
| 40° | 7.472×10⁻⁵ | 0.04976 | **~666×** inside the bar |

This is not a marginal pass sitting near its own bar — it clears by two and
a half orders of magnitude at both angles, an order of magnitude cleaner than
this program's own routine "10–100×" settling margins elsewhere in the T27/
T28 record. EM's and VISION's independently-converged Phase-2 concern (every
prior settling check on this channel co-varied boundary thickness and domain
size; G40 decouples them for the first time) was a genuine, previously-
uncharacterized gap and the 3-call cost was worth paying — but the answer is
unambiguous: **G40 is cleanly settled at `STEPS=2800`.** Nothing about the
headline `PAD_TIED` classification is at risk from settling.

One gap this margin does *not* close, flagged in §4: the settling check ran
only at 600nm. G40 has never been settling-tested at 750nm at all.

---

## 3. The missing energy-conservation/passivity check — and what it would show

**No energy-conservation, passivity, or reciprocity check runs anywhere in
this cycle.** `grep -n "passiv\|reciproc\|caus\|Cauchy\|energy" run.py`
returns exactly one hit — THERMODYNAMICS' textual N/A disposition — nothing
computational. `g0e_amplitude_channel_check.py` is a *statistical* recovery
gate (does the fitting procedure recover a known injected number), not a
physical one. This is the gap my charter exists to flag, and this cycle's
own three-config construction (C40, G40, C80 — different domain sizes,
different `ABSORB` thicknesses, decorrelated for the first time) is exactly
where it bites, because a genuine, decisive bookkeeping argument is available
at **zero marginal FDTD cost**, already licensed by data this cycle itself
committed.

**The argument.** `experiments/065-.../design_geometry.py::config()` builds
`PAD` cells as pure domain extension — `nx`/`ny` grow, every scene coordinate
shifts by `pad`, but the graded-loss damping arrays (`damp_e`/`damp_hx`,
`lab/fdtd2d.py::Sim._damping`) are constructed from `absorb` alone. This
cycle's own `static_construction_identity` gate — re-verified directly this
review, not re-run, since it is a pure code inspection of already-committed
logic — confirms this empirically at the scored windows:
`all_vacuum=True`, `max_diff=0.0` between the `damp_e`/`damp_hx` arrays of
any two configs sharing the same `absorb`, at every scored cell, at *every*
time step (a static fact, true independent of dynamics). **`PAD` is
provably, exactly, lossless vacuum — it carries zero damping coefficient
anywhere in the simulated volume.**

Maxwell's equations in a source-free lossless (σ=0) region conserve Poynting
flux exactly — a vacuum region can delay, disperse in phase, and geometrically
redistribute a wave, but it cannot absorb, generate, or otherwise change the
*magnitude* of power crossing it. The `ABSORB=40` graded-loss stack is
**bit-identical** between C40 and G40 (same `absorb` value, confirmed by the
construction-identity gate) — so the reflectance magnitude that stack
presents to an incident wave, `|r(θ; ABSORB=40)|`, is provably the *same*
physical quantity in both configs, by construction, not merely by
measurement. Nothing about adding 40 cells of pure vacuum between the
boundary and the scored window can change how much power that boundary
reflects.

**What this means for `PAIR_PAD`'s own `HIGH`-bin reading
(`x=0.119366`).** The entire measured `amp_ratio(C40,G40)` signal — the
largest of the two new pairs, and the one driving the `PAD_TIED` outcome —
cannot, by this argument, be a change in how much energy the boundary
reflects. It can only be a **coherent propagation-phase/interference
effect**: the same-magnitude reflected wave arrives at the scored window with
a different round-trip phase because it has travelled 80 extra cells (there
and back) of added vacuum path length before doing so. This is mechanistically
the *same class* of phenomenon T21 (Huygens edge-diffraction fringe, source-
side) and exp-075 (boundary-reflectance-echo, `ABSORB`-side, REFUTEd on
period grounds for the *wrong* independent variable — see §5) already
formalize for this bench: a fixed-magnitude coherent echo whose *phase*, not
its *amplitude*, is the free parameter the observed periodicity should be a
function of.

**Strengthens the `PAD_TIED` reading; also sharpens what it can mean.** This
is not a challenge to `phase4_results.md`'s headline — it is independent,
zero-cost corroboration from a different physical principle (passivity/
energy conservation) that a real, PAD-sensitive signal at fixed `ABSORB` is
physically expected, not merely an empirically-observed correlation with no
first-principles support. But it also narrows the *interpretation* MATERIALS'
own caveat (docket item 7) leaves open. MATERIALS correctly established
`ABSORB` and `PAD` "are both pure numerical domain-construction parameters;
neither carries more physical standing than the other" — true and necessary,
but read alone it leaves the two axes symmetric. They are not symmetric in
*kind*: `ABSORB` is the one construction parameter that can change a
reflected wave's **amplitude** (it is the only lossy element in the domain);
`PAD` can only change its **phase/timing**. A `PAD_TIED` amplitude-mismatch
reading is therefore best read specifically as *"the amplitude-mismatch
metric is more sensitive to the echo's round-trip phase than to the
boundary's own reflectance magnitude at this window/wavelength"* — a
sharper, more falsifiable statement than "padding/domain-geometry-tied," and
one with an immediate, cheap next test (§5, item 1).

**Recommended, forward, zero-cost**: this passivity argument should be added
to the LOGBOOK.md T28 entry as a load-bearing physical constraint on future
`PAD`-vs-`ABSORB` citations from this sub-thread, not left to be re-derived
by a future cycle from scratch.

---

## 4. The 750nm ordering flip: a coherent explanation exists, but the leg
   carries a real, previously undisclosed hole

`phase4_results.md` reports the flip honestly as "genuinely informative
tension, not decisive" and correctly declines to let it overturn the 600nm
headline. From this seat's charter, two things are worth adding.

**(a) A clean field-physics candidate exists, and it is not the same as
saying the flip is noise.** Every config this cycle runs sits at an exact
integer multiple of λ at 600nm (`ABSORB=40→2.000λ`, `80→4.000λ`) —
PHOTONICS' own Phase-2 finding, adopted MANDATORY. A graded lossy stack is
exactly the structure that can show Fabry–Pérot-like reflectance-*magnitude*
extrema at even-integer-thickness/λ conditions. If `|r(θ;ABSORB=40)|` is
itself anomalously large or small at the 600nm resonant condition relative to
750nm's genuinely non-aliased one (`1.6λ`/`3.2λ`), the *relative weighting*
between the amplitude-sensitive (`ABSORB`) and phase-sensitive (`PAD`)
contributions to `amp_ratio` would shift between the two wavelengths for a
first-principles reason — a resonance-dependent rebalancing, not a
breakdown of the underlying mechanism. This is consistent with, not
contradicted by, §3's passivity argument: §3 establishes `PAD` can only ever
act through phase, at any wavelength; it says nothing about how large the
`ABSORB`-driven amplitude channel is at a given wavelength, which is exactly
the free parameter a resonance condition would move.

**(b) But the leg that would test this has a gap the record does not name.**
Checked directly against `results.json`: the settling precondition
(§2, decisive PASS) ran **only at 600nm**. `G40` has **never** been
settling-tested at 750nm, at any `STEPS`, by this cycle or any prior one —
`block_leg750`'s own C40/C80 rows inherit their settling license from T27's
generic Block-MAIN closure (exp-066, "settling-generalization... verified
along... the λ axis"), but that generalization was established for `C40`/
`C80`'s own geometries, never for `G40`'s newly-decoupled (thin boundary ×
large domain) combination — the exact combination this cycle's own Phase-2
docket (item 4) existed to check, and did check, but only at 600nm. Given
§2's own 600nm result is comfortably clean, this is not a reason for alarm —
but it is a real, disclosed-nowhere gap, and it means the 750nm ordering flip
currently rests on an unverified settling assumption stacked on top of an
already-disclosed narrow-window/poor-conditioning caveat (PHOTONICS' own
Phase-2 finding, `cond9≈478–529`).

**Net reading**: the flip is not evidence against treating `PAD_TIED` as a
real signal at 600nm (a resonance-dependent rebalancing is a physically
sensible story, and §3's passivity argument is wavelength-independent — it
holds at 750nm exactly as it does at 600nm). But the 750nm leg itself is not
yet trustworthy enough, on its own construction, to argue either for or
against wavelength-generality — it needs the settling check it never got
before its own qualitative "opposite ordering" reading is treated as more
than a hint.

---

## 5. Top-3 ranked candidate directions for Iteration 54

1. **PAD-parametrized round-trip echo model — reuse exp-075's own
   passivity-gated transfer-matrix machinery, reparametrized on round-trip
   *distance* (a function of `PAD`) rather than `ABSORB` depth.** Zero new
   FDTD to start: `experiments/075-.../boundary_reflectance.py` /
   `two_wall_cavity.py` already compute a passivity-gated (`G-PASSIVITY`,
   `|r|≤1`), causally-derived echo period as a function of the reflecting
   boundary's physical distance from the scored window — tested there
   against `ABSORB` depth (REFUTEd, period ~4.3–15.0× too long) on the
   *confounded* `C40`/`C80` series, where domain size and boundary depth
   moved together. §3's argument gives a first-principles reason the model
   was scored against the wrong independent variable for the `PAIR_PAD`
   signal specifically: refit the SAME passivity-gated model's round-trip
   distance against `PAD` (fixed `ABSORB=40`, using the C40/G40 pair, where
   the reflectance amplitude is now provably held constant and only the
   round-trip phase varies) rather than against `ABSORB`. This is the single
   most direct, cheapest (desk-only, reusing already-built and already-
   passivity-verified code) test of whether the `PAD_TIED` signal is the
   coherent-echo mechanism §3 predicts it structurally must be.
2. **Close the two settling gaps this review found, before either 750nm
   reading or a future wavelength-general citation is trusted**: (a) a
   2-call G40-at-750nm forward-settling leg (`STEPS=2800` vs `4200`,
   θ=39°/41° or the two extremal `block_leg750` angles), mirroring this
   cycle's own 600nm precondition exactly; (b) the still-outstanding
   full-width (6°/31-point), non-aliased-wavelength leg (450nm:
   `40/15≈2.667λ`, `80/15≈5.333λ`, both non-integer) that Idealization 1 and
   docket item 5 already flag as required before any wavelength-general
   `PAD_TIED` citation — the 3° advisory window cannot carry that claim on
   its own even once settled.
3. **Formalize §3's passivity bookkeeping as a standing LOGBOOK.md
   constraint on this sub-thread**, not a one-cycle aside: any future
   `PAD`-tied vs `ABSORB`-tied finding on this construction family should be
   read against the fact that `PAD` is provably lossless vacuum (zero
   damping coefficient, confirmed by this cycle's own
   `static_construction_identity` gate) and can therefore only ever act
   through propagation phase/timing, never through absorbed-power magnitude
   — sharpening MATERIALS' correct-but-symmetric "neither carries more
   physical standing" caveat into a falsifiable, mechanism-relevant
   asymmetry (amplitude channel vs. phase channel) that item 1 above
   directly operationalizes.

---

## 6. For the Director's LOGBOOK.md / PLAN.md update

- **T28 update**: record the settling-gate margin numbers explicitly
  (frac_39=1.03×10⁻⁴, frac_40=7.47×10⁻⁵, bar=0.0498, ~481–666× margin) —
  this program's own R4/R8 discipline argues for citing the actual numbers,
  not just "PASSED with wide margin," given this exact sub-thread's history
  of prose glosses drifting from committed figures.
- **New, disclosed gap, not previously named anywhere in this cycle's
  record**: `G40` has never been settling-tested at 750nm, at any `STEPS`.
  Recommend a one-line addition to the T28 LOGBOOK entry and to
  `lab/caveat_lint_config.json` (or the existing `exp065-steps1400-unsettled-
  plane-channel`-style entry, extended) naming this specifically, so a
  future cycle citing the 750nm leg's ordering flip does not inherit it
  silently the way this program's own T27 history shows such gaps otherwise
  do.
- **The passivity argument in §3** is, in this seat's judgment, the single
  most load-bearing addition this review makes: it converts "PAD-tied" from
  an empirical correlation into a physically-necessary consequence of the
  construction (PAD cannot dissipate, only dephase), and it hands Iteration
  54 a concrete, cheap, already-built-machinery test (item 1, §5) rather than
  another open-ended desk search of the kind R5's addendum already warns
  this sub-thread against.
- **No Checkpoint criterion fires from this seat's review.** The cycle's own
  process (Phase-2 catching the settling gap, the exhaustive/mutually-
  exclusive band rewrite, the `rho_pad_absorb` downgrade) worked as designed;
  nothing found here was hidden or defended — it is new information this
  cycle's own construction made available but did not itself compute.
