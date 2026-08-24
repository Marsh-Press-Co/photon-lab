# PHASE 5 — REVIEW · Panel Iteration 42 · ELECTROMAGNETISM (blind, fresh context)
## exp-065 — The T24 `ABSORB` Boundary Sweep

**Seat charter applied:** field/wave behavior, impedance matching, energy
coupling; reciprocity/passivity/causality bookkeeping — formalizing what T1
permits and forbids per proposal. This cycle is N/A on T1 (instrument-
fidelity class, correctly self-scoped); the charter work here is auditing
whether the gate machinery and the settling finding are sound EM claims, not
merely procedurally-satisfied checkboxes.

---

## 1. My read of the results, from this charter's standard

### (a) Does `static_construction_identity()` discharge what G-2 needed to certify?

**Partially, and the part it does not cover is exactly the part that turned
out to matter.** The two gates are not interchangeable claims, and the
cycle's own record shows why.

`static_construction_identity()` compares `damp_e`/`damp_hx` — the *static
coefficient arrays* `Sim.__init__` builds from `absorb` alone, zero `.run()`
steps — at the scored-window cells between C40 and G40, offset by `pad`.
Bit-identical, `damp_e == 1.0` in the window. This is a legitimate and
*strong* check of one specific thing: that the padded domain's construction
is a bug-free coordinate shift plus vacuum extension — i.e., that the two
`Sim` objects are solving **the same PDE with the same local coefficients**
in the shared footprint. It is a congruence-of-inputs proof, and it is
strictly better than the voided dynamic gate at catching the failure mode
it targets (an off-by-one or asymmetric pad), because it inspects the
arrays a construction bug would actually corrupt, rather than inferring
their correctness from field propagation.

**What it does not, and structurally cannot, certify: that the two
configurations' *fields* agree at any finite, practically-used step count.**
Same-PDE-with-same-local-coefficients only implies same-converged-solution
in the infinite-time / fully-settled limit — an argument about steady
state, not transient state. The original dynamic gate (`n=359`, later
corrected to `n=247`) was reaching for the field-level claim directly, via
causality: a snapshot equality that would hold at *any* time up to the
causal horizon, transient or not. That claim is strictly stronger where it
applies, and its Phase-3 voiding (247 < 319, the direct source→plane
arrival time) is not a defect introduced by choosing the static
replacement — it is a discovery that **no causally-certified dynamic
snapshot equality is available at this geometry, at any step count a
causality argument alone can reach.** The static gate was the correct next
move given that, but it is honest to name what got given up: a
construction-congruence certificate, not a field-equality certificate.

**This gap is not academic — Diagnostic 1/2/3 in `phase4_results.md` are
its concrete manifestation.** The reason P-VIS42-2's headline flipped from
REFUTED (STEPS=1400) to CONFIRMED-leaning (STEPS=2800) is precisely that
the *fields* in the differently-padded configurations were not equally
settled at STEPS=1400 — a fact the static gate has no way to see, by
construction. A residual worry this raises, which I looked for and did
**not** find strong evidence for: that the differently-sized pads
(`PAD ∈ {0,20,30,40}`) themselves impose *different* round-trip distances
to the y-boundaries, hence different transient decay times, hence that part
of the STEPS=1400 `C80−C40` delta could be a differential-settling artifact
riding on top of (not purely) a boundary-reflectivity effect. Diagnostic 1
partially rules this out: C40 (unpadded) and C60 (padded, PAD=20) show
comparable 1400→2800 relative shifts (74.4% vs 68.4%) at the one cell
tested — evidence the transient is dominated by something common to the
channel (grazing-angle/y-boundary interaction, discussed below), not by
pad size specifically. But this was checked at **one cell, two of five
configs** — C70, G40, N60, and the other 17 SWEEP cells never received even
this weaker check. I would not treat differential-settling-by-pad as ruled
out; I would treat it as disclosed-but-unclosed, on the same footing as the
750nm residual the Director already flags as open.

**Verdict on (a):** the static gate is the right tool for what it does, and
Phase 3's diagnosis of why the dynamic gate had no valid window is
correct EM reasoning (I re-traced `Sim.run` myself and confirm the 5-point
cross stencil's exactly-1-cell/step domain of dependence — the H-update
reads `Ez` at ±1 cell, the E-update reads the just-computed H at ±1 cell,
independent of `courant_frac`; this is not something the static-array
check needed but it is something the causal-step derivation needed and got
right this cycle). But the swap left a real, disclosed, not-yet-closed
energy-coupling gap: nothing in this cycle's gates certifies that any
config's field is *settled* at the step count its headline number is read
at, and the one config that mattered most (C40, the 19-iteration program
anchor) turned out not to be, by a factor of ~3.9× at the one cell checked.
The old dynamic gate, correctly derived, would have told you *that gap
exists* (by failing to clear 319) before a single FDTD call ran — which is
exactly what happened. Read generously: the gate voiding did not create
the blind spot, it **correctly reported** it, and the panel's own
settling follow-up then independently rediscovered it empirically. That is
the system working, not failing — but it means "the gate passed" (G-2) must
not be read by any future cycle as license to treat STEPS=1400 as settled
on this channel. It only certifies the geometry is honest; it says nothing
about the clock.

### (b) Is ~2800-step settling at near-grazing angle, and the 4× overshoot shape, physically reasonable?

**The order of magnitude is plausible and has an identifiable mechanism;
the specific shape (a clean, one-sided, ~4× overshoot rather than a
build-up from below) is unusual enough that I would not certify it as
understood on four data points at one cell — but it is not evidence of a
bug, and there is independent cross-corroboration in this program's own
record that points the same direction.**

**Why the timescale is not obviously wrong.** The direct-arrival figure
(319 steps) bounds only the *first-arriving, unobstructed* signal path
(`D_SP/S`). It says nothing about the settling time of the *steady-state
interference pattern* the instrument actually reads — which requires every
significant secondary path (residual boundary reflection, edge
diffraction from the taper, near-grazing coupling to the y-boundaries) to
have decayed below the measurement's own resolution. At θ = 38–40°, the
source's radiated energy travels almost **along** y, i.e. nearly head-on
into the top/bottom absorbing bands rather than grazing past them — this
is the geometrically natural reason a *near-grazing-in-x* angle produces
the *worst* y-boundary coupling, and it is a mechanism specific to this
channel (plane/tapered source, wide aperture) that a focused on-axis
Gaussian beam (exp-046's own settling check, which found 0.036–0.083%
shifts) would not exercise at all — Diagnostic 1/Learned-2's own
explanation. A `y`-boundary round trip from the object window
(`OBJ_Y ≈ 792–832`) to the band edge and back is several hundred to
roughly a thousand cells at `S ≈ 0.70` cells/step, i.e. many hundreds to
~1500 steps for one round trip — comfortably inside the 1400→2800 window
where the reading is shown to change. A graded-loss band that is *not* a
perfect absorber (finite residual reflectivity by construction — that is
the entire question T24 opened) leaving a slowly-decaying resonant-cavity-
like residual after 1–2 such round trips, on a channel that is a
**near-null measurement** (a small difference between object and flank
windows, itself sitting near a T21 fringe), is a coherent, unforced
explanation: a near-null observable is disproportionately sensitive to a
small residual field the boundary reflectivity leaves behind, which is
exactly the kind of nonlinear amplification (small absolute perturbation,
large relative swing on a near-zero quantity) this program has hit before
on this same instrument (T16's angular-quadrature sensitivity, T21's
fringe itself).

**Why the specific shape deserves more scrutiny than the Director's
diagnostic table gives it.** A switch-on transient in a lossy cavity
"charging up" toward steady state is the textbook-intuitive picture, and
it approaches from *below* (or oscillates around the final value with
shrinking amplitude). What is reported here is the opposite: the
UNsettled (1400-step) reading is **larger** in magnitude than the settled
value, by a clean, one-directional factor of ~3.9, and the settling
appears to complete in a single step between 1400 and 2800 with no
visible residual structure from 2800 through 5600 (flat to 4 significant
figures). Two readings of that shape:
  - **Consistent-with-physics reading:** a truncated-CW source (a
    raised-cosine ramp of only ~86 steps at `cpl=20`) generates real
    spectral sidebands and a genuine early-time transient whose *coherent
    sum* with the direct/diffracted field can transiently exceed the
    final steady-state magnitude before relaxing to it — overshoot-then-
    settle is a completely ordinary feature of a driven, weakly-damped
    linear system with more than one interfering path, not an
    anomaly requiring a superluminal or acausal explanation. A near-null
    channel measuring a coherent sum of several comparable-magnitude,
    slowly-converging contributions is exactly where such an overshoot
    would show up largest in *relative* terms.
  - **Under-characterized reading, disclosed as such by the cycle itself
    (idealization 13):** four points at *one* cell is not enough to
    distinguish "a single well-behaved decaying transient, captured
    cleanly" from "two structurally different regimes that happen to
    look flat past 2800 at this one cell" — e.g., a beat between two
    close-lying decay rates that happens to nearly cancel by 2800 at
    600nm specifically. The 750nm residual (0.0032–0.0038 at STEPS=2800,
    2×+ the CONFIRM band, explicitly **not** shown converged even at
    2800) is the concrete warning sign that "settles cleanly by 2800" is
    not yet a general property of the channel — only of the one cell
    checked with the full 4-point trend.

**Independent corroboration worth naming, from this program's own prior
record (not new work this cycle):** T21's own Iteration-19/20 finding
(PHOTONICS' `c*` fit) found the best-fit fringe-amplitude scale grows
monotonically with λ (1.81/2.74/3.23 at 450/600/750nm), an ordering that
was read at the time as matching "the λ-dependent causal-transit-margin
idealization's own ordering (thinnest settling margin at 750nm)" rather
than Yee-grid dispersion. This cycle's 750nm residual — the wavelength
with the largest unresolved settling gap at fixed STEPS — lands on
**exactly the same wavelength** that finding flagged three iterations
before this channel's settling was ever directly measured. That is a
second, independent measurement pointing the same direction, and it
raises my confidence that "settling margin is thinnest at 750nm on this
channel" is a real, physically consistent property of this bench
(coarser `cpl` at shorter λ vs. finer `cpl` at 750nm interacting with a
fixed `STEPS` and a fixed `ramp_periods`, as `phase4_results.md`'s own
candidate mechanism proposes) rather than a coincidence local to this
cycle.

**My overall read on (b): reasonable, not yet fully verified.** The
magnitude and general shape (grazing angle → strong y-boundary coupling →
slow residual decay on a near-null instrument → large relative overshoot)
has a coherent, causally sound EM mechanism and independent cross-
corroboration from T21's own earlier, unrelated finding. I would not call
this "something is off" in the sense of a bug or an unphysical result. But
I would also not treat "STEPS=2800 settles this channel" as established —
it is established at exactly one (θ, λ) cell, contradicted in degree (not
in direction) by the 750nm residual at the *other* cells that did get a
two-point check, and the shape (clean single-step overshoot-then-flat)
is the kind of pattern that historically, on this exact instrument
(T10/T16/T21), has turned out to hide a second confound once looked at
more closely. Diagnostic 3's own residual-mechanism paragraph
(`phase4_results.md`, "candidate mechanism... not verified this cycle")
already says this; I am agreeing with the Director's own hedge, from the
charter whose job is exactly to police this kind of energy-coupling claim.

---

## 2. Verdict: **PARTIAL**

Both absolute-identity gates are sound and passed; the cycle's own
mandatory-fix discipline (Red Team attack 7, almost dropped as a routine
robustness check) surfaced a real, load-bearing, previously-unmeasured
settling gap in a 19-iteration-old program anchor — a genuine and
significant finding, honestly reported and not smoothed over. But the
cycle's own headline question (does T24's systematic transfer as
absolute or relative) is explicitly undecided by its own admission, and
the replacement gate's coverage gap (construction congruence, not field
settling) is disclosed but not yet closed. PARTIAL is the correct
reading of a cycle that converted its stated question into a bigger,
more consequential open question rather than answering either.

---

## 3. Ranked candidate next directions (my charter's ranking)

1. **A multi-cell settling convergence trend, not a single-cell one.**
   The 4-point (1400/2800/4200/5600) trend that resolved 600nm/C40/40°
   needs to be run at minimum on the worst-residual cell (750nm, C80,
   either ±40°) before "STEPS=2800 settles the channel" is treated as
   established anywhere in LOGBOOK.md. This is the direct, cheap
   (4 calls) closer for the single largest open item this cycle leaves.
2. **A genuine y-boundary reflectivity measurement, isolated from the
   fringe/near-null channel that is currently the only instrument
   reading it.** My own charter's reading of the mechanism (near-grazing
   angle ⇒ near-normal incidence on the y-boundary ⇒ residual
   reflectivity dominating a near-null observable) is a *hypothesis*,
   consistent with the data but not directly tested. A dedicated
   diagnostic — e.g. a closed-surface flux/energy-ledger check
   (this program's `sections.widths`-style box-ledger idiom, T9/T11's
   own precedent) around the y-boundary specifically, at fixed STEPS
   and varying `absorb`, at both a grazing and a non-grazing angle for
   contrast — would directly test whether the settling timescale and
   magnitude actually track y-boundary distance/reflectivity the way I
   argue above, rather than resting on a plausibility argument alone.
3. **Re-verify `experiments/041-t20-angle-audit`'s own MAIN-block rows
   at STEPS≥2800** (the Director's own #1, which I concur with, ranked
   here #3 only because it is a re-verification of prior work rather
   than new physics/instrument understanding) — the program-wide
   consequence (T21's fringe fit, T16's quadrature deltas, every
   near-threshold constraint-3 citation built on the ±38°/±40° family)
   is the largest-stakes item on the board, but it is mechanically
   downstream of items 1–2 rather than informative on its own: without
   knowing whether 750nm is actually settled by 2800 or needs more, a
   re-verification sweep risks repeating exactly this cycle's own
   single-step-count trap at a new nominal value.

---

## 4. Checkpoint opinion (my own reasoned view, per charter)

**No Checkpoint criterion fires from my seat's reading, but criterion 4 is
close, and I want that on the record rather than silently resolved.** The
settling gap is a genuine, load-bearing instrument-trust defect that has
sat silently under nineteen iterations of downstream physics claims
(T16, T21, every near-threshold constraint-3 citation) — the shape of a
criterion-4 finding. What keeps it from firing, in my reading: it was
**found and disclosed within the same shift**, by the program's own
mandatory-fix discipline, not discovered later by a future audit of an
unflagged gap — the same distinction Red Team has applied consistently
since Iteration 19 (caught-and-corrected same-shift vs. shipped-quietly).
It only becomes a criterion-4 matter if a future cycle cites the
±38°/±40° MAIN-block family, or this cycle's own STEPS=2800 sweep, as
settled without first closing candidate direction #1 above.

---

*Prepared by ELECTROMAGNETISM, panel Iteration 42, Phase 5. Fresh context,
blind to the other six seats' Phase-5 reviews per PANEL.md's independence
mechanics.*
