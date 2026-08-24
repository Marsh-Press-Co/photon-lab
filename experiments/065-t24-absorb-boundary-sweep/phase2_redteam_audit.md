# exp-065 — Phase 2 Red Team Audit

**Panel Iteration 42. Seat 7, RED TEAM.** Receives everything: the Phase-1
proposal (VISION SCIENCE, lead by rotation) and all five blind Phase-2
critiques (PHOTONICS, MATERIALS, ELECTROMAGNETISM, THERMODYNAMICS, QUANTUM
OPTICS). Speaks last. Standard: not textbook-physics compliance — this is
an instrument/model-fidelity cycle, T1 route N/A, correctly stated; no
mechanism is proposed, so the charter work is entirely: internal
consistency, falsifiability of the nine pre-registered predictions,
expressibility (moot — nothing here is a mechanism claim), and whether
constraint 3's evidentiary chain is quietly touched without disclosure.

Every claim below that could be independently re-verified against a
primary artifact was re-verified by direct execution or file read, not
relayed from a seat's critique: `design_geometry.py` re-run this shift,
diffed byte-for-byte against the committed `design_geometry_output.txt`
(identical); `ABSORB/cpl` ratios recomputed independently at all three
`(absorb, λ)` pairs; `causal_identity_step`'s six round-trip paths
recomputed by hand from the committed geometry, both under `S` and under a
literal 1-cell/step bound; `lab/fdtd2d.py::Sim.run` read in full and its
update stencil traced term-by-term; `REALIZABILITY_MEMO.md` read in full,
not grepped; `experiments/041-t20-angle-audit/results.json::block_main`
queried directly for its own angle coverage; a grep of the full experiment
directory for the literal string `0.00449` and for any script-side
computation of `0.69*0.0065`.

---

## Numbered attacks (most severe first)

**1. [unfalsifiable] — the integer-λ aliasing risk is real, independently
reconfirmed, and lands with full force on exactly the one channel that
feeds constraint 3; PHOTONICS' catch, verified and narrowed.** Recomputing
`ABSORB/cpl` directly at all nine `(absorb, λ)` combinations:

```
        450nm(cpl=15)   600nm(cpl=20)   750nm(cpl=25)
ABS=40      2.667            2.000           1.600
ABS=60      4.000            3.000           2.400
ABS=80      5.333            4.000           3.200
```

At 600nm — and **only** at 600nm — all three swept `ABSORB` values sit on
an exact integer multiple of λ (2λ/3λ/4λ), and both endpoints of the one
comparison P-VIS42-2's headline is built from (`C80 − C40`) are
simultaneously exact-integer (4λ and 2λ). Neither endpoint at 450nm
(2.667λ/5.333λ) nor at 750nm (1.6λ/3.2λ) is anywhere near an integer — so,
**narrowing PHOTONICS' own framing**: this artifact risk does not
contaminate all 18 P-VIS42-2 cells uniformly, only the 6 of 18 at 600nm.
But those are exactly the same 6 angles×1λ whose construction (`A=752`
etc.) is reused, unmodified, for Block ARTICLE — and Block ARTICLE is
600nm-only. So the wavelength this cycle's own text calls "the row meant
to bound real constraint-3 verdicts" (§0) is not merely *disproportionately*
exposed to this risk, it is **exclusively** measured at the one point in
the design where a periodic boundary-reflectivity term (a real, physically
plausible mechanism for a graded-loss ramp whose electrical thickness in
units of λ sets its own numerical-dispersion accumulation — not a
manufactured worry) would alias worst. This is precisely the failure shape
R2, T16, T21 and R5 already taught this program to distrust: an unmodeled
periodicity, sampled at too few points, at points that happen to coincide
with the periodicity's own special phases. No band in §4 can currently
distinguish "monotonic/smooth boundary-loss trend" from "three
coincidentally-resonant samples of a non-monotonic function" — P-VIS42-2's
CONFIRM/REFUTE bands and P-VIS42-3's Spearman-ρ discriminator are both
computed from the same three aliased points; they cannot rule the
alternative out because no non-aliased point exists anywhere in the design.

**2. [inconsistency] — the causal-identity gate's derivation is
mathematically wrong, independently reconfirmed by tracing the actual
stencil; EM's catch, confirmed and characterized.** Read `lab/fdtd2d.py`'s
`Sim.run` directly: the H-update depends on `Ez` at cells offset by 1 (`Hx`
from `Ez[:,1:]-Ez[:,:-1]`, `Hy` from `Ez[1:,:]-Ez[:-1,:]`), and the
E-update depends on the just-computed `H` at cells offset by 1
(`Hy[1:,1:-1]-Hy[:-1,1:-1]`, `Hx[1:-1,1:]-Hx[1:-1,:-1]`). Composing these,
`Ez(new,i,j)` depends on exactly `Ez(old,i,j)`, `Ez(old,i±1,j)`,
`Ez(old,i,j±1)` — a 5-point cross. Per full loop iteration (one "step"),
this numerical domain of dependence grows by **exactly 1 cell along each
axis**, independent of `courant_frac`; `_damping`'s multiplicative
`Ez *= damp_e` cannot widen it. That is strictly faster than the wave's own
Courant-limited phase speed `S = 0.700036` cells/step used in
`causal_identity_step`. Recomputing the function's own six paths by hand
from `CONFIGS['C40']`/`CONFIGS['G40']`: the binding path is 263 cells
(`2·clear_src(20) + (src_x−plane_x)(223)`, C40's own tighter clearance).
`floor(263/0.700036) − 16 = 359` (reproduces the script exactly). `floor(263/1) − 16 = 247`
— a 112-step, 45.3% overstatement. **This is not a `≥1e-16`-relative-error
rounding quibble — it is a category error**: `S` bounds where the
*physical wavefront* sits; it says nothing about where a discrete,
finite-support recursion's *exact-zero boundary* sits, and those are
different lines. `causal_identity_step`'s own docstring states "Signal
speed is the Courant number `S`... the fastest an FDTD update can
transport information" — this sentence is factually false as a claim
about the stencil (true only as a claim about the modeled physics).

**3. [inconsistency] — REALIZABILITY_MEMO.md's own downgrade of this exact
τ is omitted where the identical number gets a fresh bucket; MATERIALS'
catch, independently confirmed by direct read.** `REALIZABILITY_MEMO.md`
line 263 names τ_off=0.0065 as "the best-characterized OFF article
(exp-032's `off_pass`)" and builds D_req≈540–600× and the memo's own
UNOBTANIUM-WITH-PARAMETERS verdict from it by name (lines 270–334). Its own
Amendment (lines 10–30, Iteration 12) goes further than MATERIALS' critique
quotes: this exact τ "no longer clears the bar at EITHER geometry it has
ever been checked at" and the memo explicitly instructs future readers that
"D_req≈540–600× below should therefore be read as a LOWER bound... not an
achieved reference point measured from a configuration that actually
cleared the bar." `phase1_proposal.md` never cites this file. P-VIS42-7
reports a fresh PASS/MARGINAL/FAIL bucket for this identical τ at a third,
never-before-measured geometry with zero pointer to either the memo or its
own Amendment — the exact "check a number against the existing record
before citing it as new" gap this program's own R4 discipline exists to
close (see exp-064 Phase-2 audit, attack 2, for the identical shape one
cycle prior).

**4. [inconsistency] — the "descriptive-only" central estimate is
hand-typed, not code-produced, contradicting §8.3's own completeness claim;
new, not raised by any blind seat.** §8.3 states: "every figure in this
document is produced by `python3 design_geometry.py`... or read
programmatically from a committed `results.json`. The only figures
transcribed from prose are T24's own published beam-channel numbers... and
are stored in `T24_BEAM`." Grepped the full experiment directory and
`design_geometry.py` for the literal figure P-VIS42-7 reports,
`0.00449`: **zero hits anywhere in the script or its committed output.**
`0.69 * 0.0065 = 0.004485` — the arithmetic behind the quoted number — is
likewise absent from `design_geometry.py`. This is not one of the disclosed
`T24_BEAM` exceptions (a different, explicitly named class). It is a
hand-typed, "precisely recomputed"-style figure appearing in a headline-
adjacent prediction row, in the exact document class R4 exists to police
("any falsifier or self-consistency figure cited... MUST be produced by
invoking the actual committed function... never hand-typed, however simple
the arithmetic looks") — and §8.3's own R4/R5 disclosure section, whose job
is to certify this document's compliance, makes a completeness claim that
is false for this one figure. Independently additive to MATERIALS' attack
(which is about the constant's non-portability, a different defect on the
same number) and to attack 3 above.

**5. [unfalsifiable] — the "cancels to first order" premise has no
falsifier and the program's own two prior legs are at least as consistent
with the opposite hypothesis; QUANTUM's catch, confirmed.** Idealization 6
asserts matched-angle differencing "cancels the quadrature phase error to
first order" as the load-bearing justification for treating a delta,
rather than an absolute reading, as trustworthy. No falsification band in
§4 tests this premise itself. T24's own two already-measured legs — `ABSORB
40→60` giving **+0.0070** at one cell and **−0.0022** at another
(opposite sign, `phase5_redteam_audit.md` §7, reproduced verbatim in
`T24_BEAM`) — are at least as consistent with a boundary-perturbed
re-phasing of T21's own coherent edge-diffraction fringe (the SAME
mechanism §2.4 invokes to explain why N60 is dangerous) as with the
proposal's own "additive boundary-loss systematic" framing. The desk
propagator cited as ground truth is explicitly boundary-free and
structurally cannot adjudicate between these two hypotheses — it is not
a neutral referee for this specific question, only for the aperture
question it was built to answer.

**6. [inconsistency] — the established UNDETECTABLE thermal finding for
this exact article class is never cited; THERMODYNAMICS' catch, confirmed.**
T5/Iteration 20 (exp-043, `lab/thermo_sidecar.py`) established, on the
record, that every OFF-state σ(I) article at this bench scale reads
UNDETECTABLE, >100× below sourced microbolometer NETD. Block ARTICLE's
disk shares τ and construction idiom with that exact article class
(idealization 8's own admission). §8.3's only sentence mentioning
`thermo_sidecar` exists solely to disclose non-triggering of Iteration 41's
`length_provenance` tripwire — a different obligation from PANEL.md's
metrics-table duty ("Absorbed energy budget + predicted re-radiation" —
"THERMO sidecar," recorded "every run"). Harmless in outcome (the
inheritance is almost certainly benign — same σ, same r_out, only the
far-boundary padding changes) but the duty is not discharged, and a
document this disclosure-dense left it silent rather than stated.

**7. [unfalsifiable] — a settling-time/domain-size confound, structurally
identical to this program's own T10 precedent, is disclosed as a gap but
never closed, and no blind seat raised it.** Idealization 3: `STEPS=1400`
is licensed by EM's exp-046 settling check (1400→2800→4200 moved C by
0.083%/0.036%) — "measured on the **beam** channel at the **unpadded**
domain only. Not re-verified on the plane channel or in the padded
domains." The padded domains (C60: 400×1624; C80: 440×1664; G40: 440×1664)
are, per idealization 4, geometries this program has **never run**. T10
(LOGBOOK, Iteration 4/5) is this program's own on-the-record lesson that a
geometry refinement can conflate with a settling-time confound that
mimics the very physics under study, and that this confound specifically
escaped a first R3 check once already (exp-027) before being caught. Here
the analogous risk is not resolution but domain size: if the larger padded
cavities need more than 1400 steps to reach the same degree of steady-state
as the unpadded C40 domain, any residual transient would grow
systematically with `ABSORB` — indistinguishable, under P-VIS42-2's
current bands, from genuine `ABSORB`-dependent boundary reflectivity. The
desk propagator's zero-degeneracy argument (§2.4) is not a defense here: it
proves the *steady-state* target is identical across the congruent series,
it says nothing about whether 1400 steps is enough to *reach* that target
identically in a larger box.

**8. [inconsistency, non-blocking] — §8.2 overstates what G-1/G-2
discharge; EM and PHOTONICS independently convergent, confirmed.** G-1 is
a pre-existing-value regression at `ABSORB=40` only; G-2 certifies only the
pre-boundary-interaction vacuum extension at the (corrected, per attack 2)
causal window. Neither touches the region *after* the wave reaches the
band — which is exactly what Block SWEEP exists to measure. §8.2's framing
that these two absolute gates "authorize" trust in the padded-domain
congruence claim is fine as a Phase-4 go/no-go check; treating them as
having "discharged" the new-configuration-class concern (rather than
relocated the open half of it into Block SWEEP's own results) overstates
their reach. Non-blocking — a wording fix, not a design fix.

**9. [minor, non-blocking, new] — P-VIS42-1's own anchor set does not
cover the ±35° legs it and P-VIS42-6/7 both depend on.** `ANCHOR_ANGLES =
(-40,-38,38,40)` — checked directly against
`experiments/041-t20-angle-audit/results.json::block_main`, whose own
`theta` coverage is `{-40..-36, 36..40}` (a 1°-step T21 fringe scan); it
contains no ±35° rows at all. So the ±35°×3λ legs of C40 — used in both
Block SWEEP's 18-cell headline and Block ARTICLE's N9 aggregate — have no
prior committed value in this program's history at this exact geometry to
anchor against; P-VIS42-1's "absolute gate" is silent on them. Not raised
by any blind seat. Low stakes (an implementation bug specific to the ±35°
angle codepath, and to no other angle, would be an unusual failure mode)
but cheap to close if a prior ±35° figure exists anywhere in this
program's record at a comparable geometry.

---

## The two load-bearing questions, answered directly

**Is EM's causal-step finding real, and is it "the gate would still
probably pass" or "the gate cannot be trusted to detect a real
problem"?** Real — independently reconfirmed to the integer, both the
263/247/359 arithmetic and the underlying stencil claim. Characterizing the
severity precisely: this is **not** "the gate cannot be trusted to detect a
real problem" in the sense that matters most — a genuine construction bug
(a coordinate-shift error, an asymmetric pad, a wrong `y_lo` convention)
would produce differences many orders of magnitude above float64 noise and
would be caught identically whether the threshold is 247 or 359; nothing
here weakens the gate's bug-catching power. What it **does** mean is
sharper than a cosmetic rounding note: the "guaranteed IDENTICAL by
causality alone, `Δ=0.0`" language attached to an ABSOLUTE-standard gate —
the single gate this cycle's own idealization 4 names as one of only three
licenses for trusting every padded-domain result in Blocks SWEEP/ARTICLE/
BEAM — is not the rigorous derivation it is presented as. If G-2 passes at
n=359 (likely, given the smooth raised-cosine-ramped source's rapid
precursor decay), the PASS is real evidence the construction is sound, but
it is evidence of an **unverified empirical decay assumption**, not of the
causality argument actually advanced. This program has been burned by
exactly this shape before at the identical severity tier (Iteration 23's
stage-16 gate, scored against a physically wrong comparator, shipped green)
— the remedy there was the same one available here: recompute at the
rigorous bound and re-verify, cheaply, before trusting the PASS as proof
rather than as evidence.

**Is the PHOTONICS integer-λ aliasing finding real, and does it threaten
P-VIS42-2's HEADLINE specifically, or is it a minor caveat?** Real,
independently reconfirmed (table above). It threatens the headline
**unevenly but consequentially**: 12 of P-VIS42-2's 18 cells (450nm,
750nm) sit at generic, non-resonant `ABSORB/λ` ratios and are not exposed
to this specific risk. The 6 cells at 600nm are fully exposed — both
endpoints of the one comparison scored (`C80 − C40`) are exact integer
multiples of λ. Because Block ARTICLE (P-VIS42-6/7, the row this cycle's
own §0 calls the one meant to "bound real constraint-3 verdicts") is
600nm-only, the aliasing risk is not diluted there at all — it is the
entire channel. This is squarely inside Red Team's own charter's
"especially #3" clause: not because constraint 3 is violated (no Tier-W/
Tier-A verdict is claimed, correctly), but because the ONE row in this
cycle that touches constraint 3's evidentiary chain is measured at exactly
the point this program's own aliasing history (R2, T16, T21, R5) says to
distrust most, with no non-resonant cross-check anywhere in the design to
rule the alternative out.

---

## Checkpoint-criteria ruling, explicit, all five

- **Criterion 1** (a configuration passes all constraint metrics): does not
  fire — this cycle is explicitly N/A on T1, scores no constraint-1/2/4
  metric, and P-VIS42-7 issues no Tier-W/Tier-A verdict (§5 item 4,
  independently confirmed by reading §5 directly).
- **Criterion 2** (a proven mechanism-class boundary): does not fire —
  nothing here bounds a mechanism class; this is instrument
  characterization.
- **Criterion 3** (engine physics beyond validated classes): does not
  fire — zero `lab/` diff (to be re-verified at Phase 3/4 as stated in
  §8.2), the `absorb=` constructor argument is pre-existing and already
  exercised at five other values in this repo.
- **Criterion 4** (Red Team flags program-integrity drift): **does not
  fire at this stage, and should not.** This is a Phase-2 critique of a
  Phase-1 *proposal* — nothing has been committed, no FDTD call has been
  made, no gate has shipped green against a wrong target. Attacks 1–9
  above are exactly the class of defect Phase 2 exists to surface before
  Phase 3 freeze; per this program's own Iteration-41 Phase-2 audit
  precedent (exp-064, attack-1 ruling), "Phase 1/2 catches followed by
  Phase-3 fixes are the *designed* mechanism, not a violation of it." This
  is unlike Iteration 39's Phase-2 firing, whose trigger was a
  **pre-existing, already-binding, textually explicit tripwire**
  ("any further gap... discovered at Iteration 39 or later, auto-fires
  criterion 4") — no such live tripwire targets any defect found here.
  Iteration 41's `length_provenance` forward tripwire is the only live one
  in scope, and §8.3 correctly discloses non-triggering (zero guarded call
  sites touched). **One forward tripwire is set by this audit**: if Phase 3
  ships without re-deriving `causal_identity_step` at the rigorous 1-cell/
  step bound (attack 2) or without adding a non-aliased `ABSORB` point to
  Block SWEEP (attack 1), and a later cycle finds either omission was
  load-bearing for a wrong conclusion already propagated into `LOGBOOK.md`,
  that is a program-integrity finding for Red Team's own ruling at the
  cycle that finds it.
- **Criterion 5** (two consecutive non-advancing iterations): does not
  fire — Iteration 41 advanced the logbook (T23 genuinely closed); this
  cycle is mid-process.

**Summary: none of the five Checkpoint criteria fire.** Attacks 1 and 2 are
serious and load-bearing for Phase 3, but severity-of-finding and
Checkpoint-firing are not the same thing, and PANEL.md's own Phase 2→3
mechanism is precisely how this program is supposed to catch this class of
defect before it becomes a program-integrity finding, not after.

---

## Verdict: **PROCEED-WITH-MANDATORY-FIXES**

The congruent-padding construction is genuinely sound single-variable
bookkeeping (independently re-verified: the geometry table, the exact
desk-propagator degeneracy, the FDTD budget and cost basis all reproduce
byte-for-byte on a fresh run), the design correctly isolates the question
T24 left unmeasured for nineteen iterations, and all five blind seats plus
this audit converge on support-with-changes, not oppose. The defects found
are in falsifiability of the headline claim under an under-sampled
periodicity risk, in the rigor of one load-bearing absolute gate's
derivation, and in disclosure completeness against this program's own
existing record — all fixable before Phase 3 freeze, at near-zero
additional FDTD cost, none of which requires re-architecting the
experiment.

## Mandatory-fix docket for Phase 3, ranked

**Blocking — must land before any FDTD call executes:**

1. **[attack 1]** Add a fourth `ABSORB` point to Block SWEEP at a value
   that is not an integer multiple of λ at any of the three wavelengths.
   Verify against `cpl∈{15,20,25}` first — checked directly this shift:
   `ABSORB=50` looks safe at 450/600nm (`50/15=3.333`, `50/20=2.5`) but is
   itself exactly `2λ` at 750nm (`50/25=2.0`), so it does **not** clear the
   bar; `ABSORB=70` clears all three (`70/15=4.667`, `70/20=3.5`,
   `70/25=2.8`) and is the point to add. Score it under P-VIS42-2/3's
   existing bands. ~18 more calls, well inside the 90-minute stop.
2. **[attack 2]** Recompute `causal_identity_step` using the stencil's true
   1-cell/step propagation speed, not `S`, giving `n≈247` in place of 359.
   Re-run P-VIS42-1b (G-2) at the corrected step. If it still passes at
   `n=247` — a strictly harder bound — the padded-domain congruence claim
   is genuinely proven rather than merely consistent with underflow, and
   the cycle proceeds on solid ground. If it fails at 247 but passed at
   359, that is itself the finding: diagnose before any other FDTD call
   reads a result, per the proposal's own stated halt condition.
3. **[attack 5]** Add QUANTUM's proposed falsifiable test of the "first-
   order cancellation" premise: a dense (≤0.5°-step) mini angular sweep of
   `ΔC_empty(θ) = C_empty(C80,θ) − C_empty(C40,θ)` spanning at least one
   full T21 fringe period at 600nm, scored for whether the delta itself
   oscillates with `P(θ)=λ/(A·cosθ)` (falsifying the additive-systematic
   framing) or stays flat (confirming it). Cheap — one extra angle block
   at one λ, on an already-built domain.

**Blocking — documentation/disclosure fixes, zero FDTD cost:**

4. **[attack 3]** Add a one-line `REALIZABILITY_MEMO.md` cross-reference
   inline at P-VIS42-7, naming both the memo's UNOBTANIUM-WITH-PARAMETERS
   verdict and its own Amendment that this exact τ no longer clears the
   bar at any geometry checked — not merely that it is "an instrument
   diagnostic."
5. **[attack 4]** Either strike the `0.00449` figure from P-VIS42-7, or
   compute it inside `design_geometry.py` (so it is code-produced, closing
   the R4 gap) and carry T15's non-portability caveat in the same sentence
   it appears in, not by cross-reference alone.
6. **[attack 6]** Add a one-sentence citation to T5's established
   UNDETECTABLE finding (Iteration 20, exp-043) at P-VIS42-7/§5, stating
   explicitly that Block ARTICLE's disk inherits that disposition
   unchanged and that no new thermal question is opened by C40 vs C80.
7. **[attack 7]** Extend the settling check to at least one point in the
   largest padded domain: one `ABSORB=80` cell, `STEPS` doubled to 2800,
   compared against the `STEPS=1400` reading. ~2 extra calls. If the delta
   is comparable to exp-046's own 0.083%/0.036% beam-channel figures, the
   settling-confound risk is closed; if not, P-VIS42-2's headline must be
   read as bounded by this uncertainty, not treated as clean.
8. **[§0]** Name explicitly what is being traded off by choosing this item
   over PLAN.md's top-ranked CNT `R_contact` term (THERMO's fix) — one
   sentence, no design change.

**Non-blocking, recommended:**

9. **[attack 8]** Soften §8.2's framing: G-1/G-2 authorize running the
   experiment; they do not pre-validate Block SWEEP's own answer.
10. **[attack 9]** If a prior committed ±35°×3λ `C_empty` figure exists
    anywhere in this program's record at a comparable geometry, cite it as
    a secondary anchor for those legs; otherwise disclose the gap in
    idealization 4 alongside the other never-before-run-geometry caveats.
11. Note, not attacked, confirmed correct on independent re-derivation: the
    §2.4 "fringe phase shift" row and the §3 fringe-period row are two
    distinct partial derivatives of the same two-edge phase model (θ vs.
    A), not one formula misapplied twice (PHOTONICS' own supporting
    detail, verified by hand to 3 decimal places) — the document should
    say so explicitly, since nothing currently prevents a reader from
    assuming the shift row "follows from" the period row directly above
    it.

---

*RED TEAM, Panel Iteration 42, Phase-2 audit of exp-065. Every seat's
critique read; independent re-verification performed by direct script
execution (`design_geometry.py`, byte-identical rerun), direct code read
(`lab/fdtd2d.py::Sim.run` in full, `causal_identity_step` traced by hand),
and direct file read (`REALIZABILITY_MEMO.md` in full,
`experiments/041-.../results.json::block_main`) before any attack above
was accepted as confirmed rather than merely relayed.*
