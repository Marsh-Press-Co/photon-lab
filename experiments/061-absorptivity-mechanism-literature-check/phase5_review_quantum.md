# Phase 5 — QUANTUM OPTICS blind review (exp-061 / Iteration 38)

*Fresh sub-agent, blind to the other five Phase-5 reviews and to Red
Team.*

**Verification performed.** `python3 lab/caveat_lint.py`: exit 0, **5
caveat(s) checked, 0 required-site failure(s)** — matches NOTES.md's
claim exactly. Independently re-derived two α conversions: (1)
n_eff=1.04+0.01i @ 550nm → α=4πk/λ = **2284.8 cm⁻¹**, matching the
reported "≈2.28×10³"; (2) the black-matrix patent, OD=3.0 @ 1µm →
τ=6.9078, α=**69,077.6 cm⁻¹** = 1.204× the 5.7353×10⁴ target, matching
"6.91×10⁴" and "1.20×" exactly. Both check out.

**Verdict: PARTIAL.** MP-2's thickness gap (70–350× for well-
corroborated sources) is solid and independent of everything below —
that finding stands. But MP-4's "coherence/localization fallback did
NOT trigger" sub-finding is weaker than its CONFIRMED label suggests,
and one exclusion rationale is incomplete. Neither defect flips MP-4's
tier, but both should reopen as unresolved, not closed.

**Defects found:**

1. **[MODERATE] The fallback's trigger condition tests vocabulary, not
   mechanism — and vocabulary is structurally biased toward
   non-triggering in this literature.** Query 6 returned "effective-
   medium/Bruggeman framing," and Phase 4 read that as evidence the
   underlying physics is classical/homogenizable. It isn't necessarily.
   Bruggeman/effective-medium fitting is the STANDARD REPORTING
   CONVENTION for reducing any measured (R, thickness) pair to a scalar
   (n,k) in this subfield — papers use it regardless of whether
   near-field CNT-CNT coupling contributed to the measured response,
   because it's how the field packages a number, not a claim about
   origin. VACNT forests pack tubes at pitches of tens of nanometers —
   deeply sub-wavelength at visible λ, textbook near-field-coupling
   geometry — and a Bruggeman fit is silent on whether that coupling
   shaped the reported k. The test as executed ("did the WebSearch
   snippet use localization words") will read "does not trigger" almost
   regardless of true mechanism, because essentially every source in
   this field reports effective-medium numbers by convention. That makes
   the fallback close to unfalsifiable as run. This doesn't overturn
   MP-1/MP-2 (the classical-parameter-scoping paragraph pre-authorized
   pooling into a scalar FOR THIS COMPARISON independent of origin), but
   MP-4's specific claim that the fallback "did not trigger" should be
   downgraded from CONFIRMED to OPEN — the test discriminated on framing
   convention, not on whether coherent coupling was screened out.

2. **[MINOR] The OD≥3.0 black-matrix exclusion rationale is correct but
   incomplete — it should also have invoked interference, not just
   discrete-pigment structure.** Elsewhere in the same document (query
   15), TiAlC/SiO₂ and Cr/oxide stacks were excluded from MP-3
   explicitly as "resonant/interference-based, not non-resonant." The
   organic black-matrix film — a sub-micron pigment-loaded photoresist
   layer, typically deposited within a multilayer LCD color-filter
   stack — is a plausible candidate for the same coherent thin-film
   interference enhancement (constructive absorption against a
   reflective substrate), which is squarely in this discipline's charter,
   not evidentiary tier. This wasn't checked. It would only REINFORCE
   MP-4's exclusion (an interference-assisted OD is even less comparable
   to a homogeneous graded medium than a "discrete-pigment" reading
   alone implies), so it isn't a numeric threat — but the document's
   internal consistency is off: the same red flag was applied to two
   candidates and withheld from a third that fits the same profile.

3. **[MINOR-EVIDENTIARY, not purely T18] The patent's "OD≥3.0" claims-
   language issue does have a coherent-optics dimension beyond pure
   evidentiary tier.** A patent optical-density figure is typically a
   best-case, single-condition (often normal-incidence, narrowband,
   backed-substrate) number, not a spectrally-integrated bulk-loss
   measurement — exactly the ambiguity that matters for distinguishing
   bulk absorption from interference-assisted absorption (defect 2). So
   this isn't purely a T18/evidentiary concern to wave off; it's coupled
   to the mechanism question above.

None of these change MP-2's dominant finding or the overall UNOBTANIUM-
WITH-PARAMETERS tier — concur with that headline. The gap is in how
confidently MP-4 closed the mechanism-class questions that are precisely
this charter's to police.

**Top-3 ranked candidate directions, Iteration 39:**

1. **Replace the coherence/localization fallback's vocabulary-presence
   test with a physical coupling-parameter test.** Estimate typical
   VACNT inter-tube pitch/diameter vs. visible λ from published
   packing-density figures (already partially in hand from query 9) and
   pre-register a numeric near-field-coupling-regime threshold, rather
   than relying on whether a WebSearch snippet happens to use
   localization language.
2. **Apply the interference-stack exclusion test to the black-matrix
   OD≥3.0 candidate specifically** — determine (or explicitly flag as
   open, if T18-blocked) whether its reported OD benefits from
   substrate-interference enhancement, closing the inconsistency in
   defect 2.
3. **A genuinely primary-source-verified recheck of the
   n_eff=1.04+0.01i figure** — already flagged in NOTES.md's own Next §4
   as MP-1's strongest in-band point, currently unpinnable to a title —
   worth escalating priority specifically because this critique turns on
   what that source's methodology actually assumed, which a title-less
   WebSearch snippet cannot settle.
