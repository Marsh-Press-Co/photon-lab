# Phase 2 — RED TEAM final audit (exp-062 / Panel Iteration 39)

*Fresh sub-agent, receives everything: the Phase-1 proposal and all five
blind Phase-2 critiques. Never leads; speaks last and hardest. Standard is
NOT textbook-physics compliance — it kills internal inconsistency,
unfalsifiable claims, mechanisms that cannot be expressed as simulation
parameters, and quiet violations of a target constraint, especially #3.*

**Verified directly, not taken on any seat's word:** re-derived every
numeric claim in `phase1_proposal.md` Sections 4.5 and 5.3 by direct
Python invocation (OD→τ→α conversions, the passivity-bound percentages,
the CNT pitch/gap/ratio arithmetic) — all confirmed exact to the printed
digit. Read `lab/caveat_lint.py`'s full source and `lab/caveat_lint_config.json`
live, and independently exercised the `exp061-t18-evidentiary-tier-propagation`
entry's `required_sites`/`candidate_globs`/`DEFAULT_CANDIDATE_GLOBS` logic
by inspection to confirm the structural gap VISION's critique alleges.
Read `experiments/061-absorptivity-mechanism-literature-check/NOTES.md`
and `lab/thermo_sidecar.py` in full to independently trace `l_geometric_m`'s
actual derivation (not merely trusting THERMODYNAMICS' characterization of
it). Read `PANEL.md`, `LOGBOOK.md` in full (the complete R1–R5 ruled-out
registry and T1–T26 live-thread history), `PLAN.md` lines 1–100 and
~1895–1949, `experiments/034-.../REALIZABILITY_MEMO.md` Entry 2 in full,
and exp-061's own `phase4_results.md`/`phase5_redteam_audit.md` for
continuity of standard.

---

## 1. Numbered attacks (independent)

**1. [inconsistency]** `phase1_proposal.md` Idealization 8 commits to
adding "a new registry entry" in `lab/caveat_lint_config.json` for any
new corrected numbers this cycle produces, but says nothing about
*widening* the already-existing `exp061-t18-evidentiary-tier-propagation`
entry — the one entry this cycle's own Section 4 text is near-certain to
trigger (its `trigger_terms` include `graded_black_shell.{0,30}absorptivity`
and `alpha.{0,15}(1\.66|1\.667|5\.7|5\.73|5\.74)`, both of which
`phase1_proposal.md` itself already matches, e.g. "graded_black_shell's
absorptivity question" and "α_true≈5.74×10⁴ cm⁻¹" repeated throughout
Section 4). Verified live against the actual registry file: `required_sites`
is exactly `["experiments/061-.../NOTES.md", "experiments/061-.../phase4_results.md"]`
— two literal, exp-061-specific paths — and `candidate_globs` is
`["LOGBOOK.md","PLAN.md","experiments/*/NOTES.md",
"experiments/034-.../REALIZABILITY_MEMO.md"]`. Neither this cycle's own
forthcoming NOTES.md nor its Phase-4 results file is discoverable: the
`NOTES.md` glob WOULD catch exp-062's NOTES.md as a WARN-only candidate
(not a required, gating site), but there is no `experiments/*/phase4_results.md`
pattern anywhere in this entry's `candidate_globs` **or** in
`lab/caveat_lint.py`'s own `DEFAULT_CANDIDATE_GLOBS` (confirmed by direct
source read, lines 128–139) — so a `phase4_results.md`-style file belonging
to any experiment other than exp-061 is structurally invisible to this
tool, at any WARN or FAIL tier. **See Section 3 below for the ruling on
whether this fires Checkpoint criterion 4** — the single highest-stakes
call in this audit, argued from the tripwire's own exact text, not asserted.

**2. [unfalsifiable]** EM-3's "broadband/narrowband resonance
discriminator" (§4.4, §7, §8) cannot discriminate the hypothesis it is
built to test, as specified. The round-trip interference phase governing a
critically-coupled thin-film absorber is `2β = 2(2π/λ)n₂d·cosθ_t` — angle-
dependent. An integrating-sphere/hemispherical OD measurement (the natural
convention for a display-industry "how black does this look" figure,
Section 1's own framing) collects and averages over a range of incidence/
exit angles; at a fixed λ, some sampled angles sit at resonance while
others don't, so a genuinely **narrowband, resonant** absorber can read as
**broadband** once angle-averaged — the *opposite* of what EM-3 treats
"broadband" as evidence for. Idealization 1 (normal incidence only,
"a textbook or diffuse-scattering surface would need a fuller... treatment
this desk analysis does not attempt") forecloses ever checking whether
this candidate's own OD figure was measured this way. As specified, §8's
falsification condition for EM-3 fires only on a *narrow-wavelength*
reading or an explicit interference-stack mention — it never asks whether
the reported OD is specular/near-normal or angle-integrated, the one fact
that decides whether a "broadband" finding is even evidence at all. This
is structurally the same failure shape this program already downgraded
once, one cycle earlier, at exp-061's own Phase 5 (the coherence/
localization vocabulary-presence fallback, ruled "close to guaranteed to
read 'did not trigger' independent of the actual physics" and tagged
unfalsifiable in that cycle's own Red Team audit) — a claims-language
proxy standing in for a physical test, this time with a real chance of
pointing backwards rather than merely being uninformative.

**3. [unfalsifiable]** Section 6 runs MATERIALS' own Iteration-38-ranked
NiP-black/electroless-nickel and carbon/graphene-aerogel query set
(queries 7–10) as a "zero-marginal-cost" addition to this cycle's search,
but Section 7's predictions table contains no MP-style row for them at
all — no predicted α band, no predicted thickness band, no falsification
condition. Section 3 explicitly assigns their "interpretation as a
realizability comparator" to "MATERIALS' charter, not scored by this
proposal's own EM-native predictions," without naming which Phase-3/5 step
actually renders that interpretation or committing any number to test it
against. As constructed, queries 7–10 can return real, sourced α/thickness
figures for NiP-black and carbon/graphene-aerogel coatings and this cycle
will still produce **zero realizability verdict** on them — nothing here
is falsifiable, because nothing here is a claim. This is the precise
"task nominally done, substance never lands" shape `lab/caveat_lint.py`
and this program's caveat-propagation discipline exist to catch, now
appearing one layer up, in prediction design rather than caveat placement.

**4. [mandatory fix]** THERMODYNAMICS' finding is real and — independently
traced by this audit directly through `experiments/061-.../NOTES.md` and
`lab/thermo_sidecar.py`, not merely relayed — actually sharper than
THERMO's own critique states it. The standing THERMO disposition's
`l_geometric_m` values (331.2µm–1051.2µm, margins 3.79×–1.35×) are NOT an
independently-measured geometric figure: per NOTES.md's own THERMO
disposition section, they equal MP-5's "found multiple" (230×–730×) times
the construction's 1.44µm thickness, and MP-5's multiple is itself
`(required thickness at a real CNT-forest α)/(1.44µm)` — i.e. `τ_true/α`
at MP-1's own best in-band α figure. That α figure traces, per NOTES.md
line ~376, to "one single-source figure, **n_eff=1.04+0.01i-derived**, at
2.28×10³ cm⁻¹" — the exact Bruggeman/effective-medium VACNT fit whose
homogenization-validity is what exp-062 Section 5's near-field-coupling
rider is testing, and whose primary source this cycle's own query 13
attempts (again) to pin. If EM-5 is CONFIRMED (§5.2, predicted `ratio≈0.68<1`),
the α figure `l_geometric_m` is built from is exactly the kind of
number Section 5.1 itself says a licensed homogenization is needed to
trust. `lab/thermo_sidecar.py::gas_conduction_h_eff`'s own docstring (line
191–193, verified by direct read) requires `l_geometric` be "a real
geometric length of the conducting/radiating SOLID body... **NEVER an
optical/extinction-derived length**." The disposition's own construction
sits closer to that forbidden category than either NOTES.md or this
proposal discloses — defensible as-used (it represents the real physical
thickness a hypothetical solid built from that material would need, not a
simulation-grid proxy like the module's own named bad example,
`w_on = sigma_ext_cells*dx_m`), but the closeness itself is never named
anywhere in the record. Two things need saying, not one: (a) the
Beer–Lambert-homogenization dependency THERMO's own critique names, and
(b) that `l_geometric_m`'s construction is textually adjacent to the
module's own guardrail and survives only on the "real hypothetical solid
thickness, not a grid artifact" distinction — a distinction this cycle's
own result sharpens the stakes of but does not itself state.

**5. [mandatory fix]** QUANTUM OPTICS' finding is correct on independent
verification of the proposal's own text: §5.2's criterion (`ratio =
g/(λ/2π)`) is a binary existence test — it can confirm neighboring tubes
sit inside each other's reactive near field, but nothing in its
construction bounds *which way* that coupling would bias the Bruggeman-
fitted `n_eff` relative to an independent-scatterer Beer–Lambert reading.
Superradiant (cross-section-enhancing) and subradiant (absorption-
suppressing) collective response are both physically live outcomes of
dense sub-λ coupling, and this program's own T25/T26 lineage (LOGBOOK,
opened Iteration 29/32) already demonstrated that a scalar/binary gate can
pass cleanly while a large, sign-carrying effect hides underneath it. An
EM-5-CONFIRMED outcome (§5.2: "a bulk-homogenization... reading... is at
minimum incomplete") is honestly hedged, but MP-4's own mechanism question
— is the cited CNT-forest α figure biased optimistic or pessimistic
relative to the truth — is left exactly where exp-061 left it, dressed in
a cleaner instrument. This does not make §5 inexpressible (a coupled-
dipole/local-field correction factor on σ_eff is a legitimate, nameable
future bench parameter, per QUANTUM's own critique) — it is a scoping
gap, not a kill.

**6. [mandatory fix, new — not raised by any of the five critiques]**
Section 3's decline of Red Team's own Iteration-38 ranked item 3 (the
`lab/caveat_lint.py` numeric-cross-check extension) is reasoned honestly
on charter-boundary grounds, and MATERIALS' critique independently agrees
it is "correctly scoped." But the proposal's own disposition of it —
"Recommendation, not a commitment... I flag this for Red Team's own ruling
rather than deciding it unilaterally" — leaves it without an owner or a
committed slot. This item was **re-ranked UP** at exp-061's own Phase-5
close specifically because the identical numeric-drift bug class
(`τ_shell=24` vs. exp-060's 9.4026; the THERMO disposition's stale 150µm
vs. MP-5's own found range) had already recurred *twice in one shift*, with
that cycle's own language warning "a third, silent instance is the
realistic failure mode this tool would close." Declining to build it this
cycle is defensible; declining it with no named owner and no committed
future slot is not — it risks the item quietly falling out of the ranked
queue exactly the way this program's own caveat-propagation failures have
recurred before. This is a process-accountability gap, not a physics
defect, and cheap to close.

**7. [note]** Both idealizations 4 and 5 are honestly stated and do not
need mandatory correction, but Section 5's own falsification framing (§8,
EM-5) commits to an outcome ("Phase 4's actual sourced pitch/diameter
figures are predicted to confirm ratio<1 at all three bench wavelengths")
built entirely on Section 5.3's own disclosed placeholder assumptions
(`D=20nm, f=5%`, not exp-061's own sourced figures, which this proposal
states it could not extract). This is disclosed, not hidden, and
Idealization 4 correctly flags it — noted here only because it means EM-5's
"CONFIRMED" branch, if it lands, confirms a *placeholder-consistent*
finding, and Phase 3/5 should say so explicitly rather than letting
"CONFIRMED" read as validation of the D=20nm/f=5% assumptions themselves.

**Confirmed clean, not an attack.** All of Section 4.5's and Section
5.3's numeric outputs were independently re-run from the stated inputs by
this audit and match the proposal's own printed digits exactly (R4
compliance genuine, not merely claimed): `τ_T=6.9078, α_T=6.908×10⁴,
ratio=1.2034`; `τ_R=3.4539, α_R=3.454×10⁴, ratio=0.6017`; `bound(T)=0.002,
bound(R)=0.06325`; `p=79.27nm, gap=59.27nm, ratio=0.677`. The passivity
argument in §4.3 (`|r₁₂|,|r₂₃|≤1 ⟹ |ΔR/R₁₂|≲2e^{-τ}`) is sound EM
bookkeeping, correctly scoped as a ceiling rather than a point estimate.
No re-proposal of R1–R5 or of any refuted T1–T26 finding was found on a
direct read of the full registry (LOGBOOK.md lines 8–74 and the complete
T1–T26 live-thread record): this cycle's near-field-coupling regime
(Section 5) is a real-material homogenization-validity question at VACNT
pitch scales, a different physical object from T21's FDTD-source
diffraction fringe or T25/T26's coherent-ambient-sum machinery, and the
proposal does not conflate them. "T1 escape route: NONE" is honestly
declared and the proposal makes no constraint-1/2/3/4 claim anywhere —
no `constraint-#N-violation` tag applies to anything in this cycle, and
none of the five critiques found one either.

---

## 2. Adjudication of the five critiques' convergent findings

**PHOTONICS — CONFIRM.** Independently re-derived the physics: the
resonance condition's angle dependence is real, textbook thin-film optics,
and an angle-integrated measurement genuinely can smear a narrowband
resonant dip into an apparent broadband reading — the inversion PHOTONICS
describes is physically sound, not speculative. Idealization 1 does
foreclose ever checking it for this specific candidate. See attack 2
above; I go further than PHOTONICS' own "support-with-changes" framing by
tagging this `[unfalsifiable]` as specified, on the strength of its direct
structural parallel to exp-061's own already-downgraded vocabulary-
presence fallback — a precedent PHOTONICS' own critique names but does
not use to argue for a harder tag.

**MATERIALS — CONFIRM.** Independently verified against Section 6 and
Section 7 of the proposal: queries 7–10 are real, committed search items
and carry no falsifiable prediction band anywhere in the document. This is
not merely an omission MATERIALS is entitled to be annoyed about — it
is the exact "search without a verdict" failure mode this program's own
caveat-propagation discipline exists to catch, now one layer removed
(missing prediction infrastructure rather than a missing caveat phrase).
MATERIALS' own stated fallback verdict — oppose, if Phase 4 executes
today, unfixed — is not overclaiming; I would independently reach the
same threshold. See attack 3.

**THERMODYNAMICS — CONFIRM, with independent verification the critique
itself did not fully supply.** THERMODYNAMICS names the Beer–Lambert-
homogenization dependency correctly but does not trace `l_geometric_m`'s
actual construction back through NOTES.md and `thermo_sidecar.py`'s own
docstring guardrail — this audit did, and found the dependency sharper
than stated (see attack 4): the standing THERMO margin's own input length
is definitionally an extinction-derived quantity built from the very
`n_eff=1.04+0.01i` Bruggeman fit this cycle's Section 5 is interrogating,
sitting adjacent to (though, on inspection, not in violation of) the
module's own explicit prohibition on optical/extinction-derived lengths.
THERMODYNAMICS' proposed one-sentence fix is necessary but not, on this
audit's own tracing, sufficient — see mandatory-fix docket item 4 below
for the fuller disclosure this audit requires.

**QUANTUM OPTICS — CONFIRM.** Independently verified against §5.2's own
text: the criterion is a scalar existence test with no sign information,
and this program's own T25/T26 precedent (a scalar gate passing while a
sign-carrying effect hid underneath) is a real, on-point structural
analogy, not decoration. QUANTUM is also correct that this is not yet an
`[inexpressible]` finding — a coupled-dipole/local-field correction is a
nameable future bench parameter — so I do not elevate the tag beyond
`[mandatory fix]`, matching QUANTUM's own "support-with-changes" rather
than pushing toward opposition. See attack 5.

**VISION SCIENCE — CONFIRM the underlying finding; the tripwire ruling
itself is argued in full below (Section 3), separately, because it is the
single highest-stakes call in this audit and deserves its own treatment
rather than a one-line adjudication here.** VISION's factual claims are
independently verified true: `phase1_proposal.md` already trips this
entry's own `trigger_terms`; the entry's `required_sites` and
`candidate_globs` cannot discover either of this cycle's own forthcoming
verdict-bearing documents; and `candidate_globs`/`DEFAULT_CANDIDATE_GLOBS`
together contain no pattern that could ever discover a `phase4_results.md`
file for any experiment other than exp-061 by literal path. Where this
audit goes beyond VISION's own critique is on the consequence: VISION
argues doing the widening at Phase 3, before freeze, "keeps this discovery
outside the tripwire's own... firing condition." I rule that it does not
— see Section 3.

---

## 3. The central ruling: does the exp061-t18-evidentiary-tier-propagation
tripwire fire Checkpoint criterion 4, right now, at Iteration 39?

**Ruling: YES — Checkpoint criterion 4 FIRES.** This is argued from the
tripwire's own exact, twice-revised text, not from a general sense that
"gaps are bad."

**The tripwire's own textual history, read precisely.** The entry's
*original* trigger condition (as characterized by Red Team's own Phase-5
audit at exp-061, quoting it directly) required a recurrence "found again
**at a future cycle**," discovered "**after** Phase 3 has already frozen
predictions" — two conjunctive conditions. Under that original wording,
neither of exp-061's own two self-caught gaps fired: both were found
**within Iteration 38 itself** (not a future cycle), so the first
condition alone already failed regardless of timing-within-cycle.

At exp-061's own Phase-5 close, Red Team explicitly **replaced** that
two-part test with a new one, after ruling that the self-catch grace was
now fully used: *"any further gap in this specific caveat's coverage —
unregistered site, under-scoped `required_sites`, or within-file location
gap — discovered at Iteration 39 or later, auto-fires criterion 4 with no
'different defect species' argument entertained a second time."* This
text is preserved verbatim (modulo trivial rewording) in three independent
places I read directly: `phase5_redteam_audit.md` §3, `PLAN.md`'s Current-
state "Standing tripwire" paragraph, and the live `caveat_lint_config.json`
entry's own `description` field.

**The load-bearing textual fact: the new wording drops the "after Phase 3
has frozen predictions" clause entirely.** It was not carried forward,
narrowed, or restated in any of the three sites carrying the tightened
tripwire. What remains is a single temporal test — "discovered at
Iteration 39 or later" — with no phase-within-cycle qualifier. Iteration
39 is unambiguously satisfied (this is Iteration 39; the entry was
authored and both prior gaps occurred within Iteration 38). The drafters
of this specific tightened wording were the same seat, writing at the same
sitting, that had just finished explaining — in the same document, one
section earlier — exactly what a "before Phase 3 froze" defense looks like
and why it worked once. Had they intended that defense to survive a third
time, for this one lineage, the natural drafting move was to keep the
clause. They did not. Read against a body of house precedent that
otherwise treats "caught before Phase 3 froze" as a live, working defense
(see immediately below), the omission here reads as deliberate, not
careless — the entire point of tightening was that this lineage's grace
period, including the specific argument-shapes that worked before, "does
not get a third."

**Why I do not import the program's general Phase-2 exemption to save
this instance.** LOGBOOK.md's own Iteration 37 record establishes, in
terms directly on point, that the *program-wide default* is exactly what
VISION's critique invokes: a caveat-placement gap "caught at Phase 2,
before Phase 3 synthesis" does *not* fire Checkpoint-4, "matching
precedent (Iteration 36's own MF-3 origin, not its later Phase-5 firing)."
That default is real, and I do not dispute it as a general matter — it is
exactly what lets Phase 2 critique do its job. But Iteration 37's own
hardened tripwire for *that* lineage (the `sigma_flat`/caveat-placement
class) explicitly *keeps* a phase-based safe harbor in its own text: "any
recurrence surviving into **THIS cycle's own published Phase-3/5
artifact** fires Checkpoint-4 automatically" — a live, working, textually
present exception for anything caught and fixed before that artifact
freezes. That same tripwire, applied to that same lineage, *did* let a
Phase-2 catch pass without firing, and *did* fire later that same cycle
once a second instance survived into the frozen `run_all.py` docstring.
The `exp061-t18-evidentiary-tier-propagation` tripwire is a **different,
separately-hardened entry**, written by the same seat at a different
sitting, for a lineage that had *already* spent its one self-catch grace
twice over (once via a "different defect species" argument, once via a
"same-cycle, before this cycle's own freeze" argument — the identical
argument-shape VISION's critique now re-offers). Its own text pointedly
does not include the phase-based safe harbor its sibling tripwire (T-37's)
does. Treating the two as interchangeable — reading a general "Phase 2
doesn't count" rule into a tripwire whose entire purpose was to foreclose
exactly that class of argument for exactly this lineage — is the "further
deliberation" its own text forbids. I decline to do it.

**What this ruling is not.** It is not a finding that VISION's own conduct
this cycle was deficient — VISION did precisely the job the tripwire
exists to make happen: caught the structural gap, named the exact fix,
proposed it before freeze. The firing is a property of the tripwire's own
mechanical terms, not a judgment that anyone acted in bad faith or that
Phase 3 synthesis is somehow disqualified from applying the fix. Per
unbroken precedent (Iterations 17, 36, 37, and 38 itself), a criterion-4
firing is **a notification, not a pause**: Phase 3 synthesis and Phase 4
execution proceed, with the registry widening as a same-shift mandatory
fix (docket item 1, below), and a CHECKPOINT entry recorded in LOGBOOK.md,
SESSION_LOG.md, and PLAN.md exactly as those three prior firings were.

---

## 4. Final ruling

**PROCEED-WITH-MANDATORY-FIXES.**

The core EM physics (Sections 4–5) is sound, independently re-derived and
confirmed to the printed digit, and correctly scoped as a realizability-
bound refinement that does not (and does not claim to) move exp-061's own
UNOBTANIUM-WITH-PARAMETERS tier, which remains independently overdetermined
by MP-2's thickness axis regardless of how this cycle's own R-vs-T/near-
field questions resolve. None of the five blind critiques opposed;
MATERIALS' conditional threat to oppose is answered by a docket item
below, not by a redesign. No defect found here requires abandoning the
EM-led scope or returning to Phase 1 — every attack in Section 1 is a
scoped, nameable, cheap-to-apply correction, the same posture Red Team
has taken at every comparable realizability-continuation cycle
(exp-036/037/060/061).

### Mandatory-fix docket (before Phase 4 search runs)

1. **Widen `exp061-t18-evidentiary-tier-propagation`'s `required_sites`**
   to include this cycle's own `NOTES.md` and its Phase-4 results file
   (once its filename is fixed at Phase 3), **and** add a generic
   `experiments/*/phase4_results.md` pattern to that entry's
   `candidate_globs` **and** to `lab/caveat_lint.py`'s own
   `DEFAULT_CANDIDATE_GLOBS`, so this exact structural gap cannot recur
   under a fourth experiment number. This is required regardless of the
   Section-3 ruling above — it does not retroactively un-fire Checkpoint
   criterion 4, but it is the correct and necessary remediation.
2. **Add a measurement-geometry query** to Section 6's search plan
   (specular/near-normal vs. diffuse/integrating-sphere/angle-averaged
   sourcing of the black-matrix OD figure), and amend §8's EM-3
   falsification condition to state explicitly that an angle-*integrated*
   broadband reading is **not** evidence against Section 4.4's resonant-
   absorber hypothesis — at best uninformative, plausibly its expected
   signature.
3. **Attach MP-style falsifiable prediction bands** (predicted α range,
   predicted thickness range, an explicit falsification condition) to the
   NiP-black and carbon/graphene-aerogel query results (queries 7–10)
   before Phase 4 runs, with an explicit Phase-3 assignment of which seat
   renders the realizability-tier interpretation once results land.
4. **Add an explicit disclosure, in Section 8 or 9**, covering two linked
   points, not one: (a) THERMODYNAMICS' own proposed sentence — if EM-5 is
   CONFIRMED, flag for Phase 5 whether the standing THERMO disposition's
   `l_geometric_m` (`exp061-thermo-length-scale-staleness`, margin
   1.35×–3.79×) rests on a Beer–Lambert bulk-homogenization this cycle's
   own result calls into question; and (b) this audit's own sharper
   finding — that `l_geometric_m` is, by construction, `τ_true/α` at
   MP-1's own `n_eff=1.04+0.01i`-derived α figure, textually adjacent to
   (though not, on inspection, in violation of) `thermo_sidecar.py`'s own
   prohibition on optical/extinction-derived lengths, and that this
   closeness should be named rather than left for a future reader to
   discover.
5. **Add a qualitative, sourced-or-flagged-undecidable disclosure of
   direction** for the near-field-coupling effect (enhance vs. suppress
   the ensemble's effective absorption relative to the independent-
   scatterer Beer–Lambert reading) alongside EM-5's existence test, per
   QUANTUM's flip — no new search required beyond what Section 6 already
   commits to.
6. **Re-file the declined Item 3** (PHOTONICS' numeric-value-consistency-
   check tooling gap) in `PLAN.md`'s ranked queue with a named owner and a
   committed slot (PHOTONICS at next rotation, or the Director as standing
   infrastructure, per the proposal's own two options) — not left as a
   bare, unowned "recommendation."
7. **Queued, unchanged priority, non-blocking**: EM's `sim.omega`
   historical registry entry; THERMO's T25 sidecar-absence entry
   (bundle-candidate with item 4 above); the standing n_eff=1.04+0.01i
   primary-source pin (T18-blocked, standing watch only, query 13 already
   commits to another attempt this cycle).

---

## 5. Checkpoint criteria — explicit ruling, all five

1. **A configuration passes ALL constraint metrics.** Does not fire —
   zero constraint-1/2/3/4 metric is scored this cycle; "T1 escape route:
   NONE" is honestly declared and true on inspection.
2. **A proven boundary: a constraint subset shown jointly unsatisfiable
   within a whole mechanism class, gates clean.** Does not fire — this is
   a realizability-bound *refinement* (an R-vs-T correction and a near-
   field-coupling classifier) layered onto an already-closed boundary
   finding (exp-061's own UNOBTANIUM-WITH-PARAMETERS), not a new proof of
   joint unsatisfiability, and it manifestly does not "gate clean" given
   the open mandatory-fix docket above.
3. **A synthesis requires engine physics beyond the validated bench
   classes.** Does not fire — zero FDTD, zero `lab/` engine file touched,
   confirmed by direct inspection of the proposal's own scope statement
   and Idealization 8; the only new artifacts this cycle produces are
   `caveat_lint_config.json` registry entries, explicitly non-engine.
4. **Program-integrity drift (unfalsifiable claims, a constraint quietly
   dropped — especially #3).** **FIRES**, on the `exp061-t18-evidentiary-
   tier-propagation` tripwire's own terms — see Section 3's full argument
   above. Independently, attacks 2 and 3 (the EM-3 vocabulary-style test
   and the queries-7–10 scoring vacuum) are unfalsifiable-tagged findings
   of exactly the kind this criterion polices, though neither alone would
   have been dispositive at the "no further deliberation" severity the
   tripwire carries. Per unbroken precedent (Iterations 17, 36, 37, 38),
   this is a **notification, not a pause**: a CHECKPOINT entry must be
   written into LOGBOOK.md, SESSION_LOG.md, and PLAN.md, Marsh is
   notified, and Phase 3 synthesis proceeds with the mandatory-fix docket
   above (item 1 first).
5. **Two consecutive iterations with no logbook-advancing result.** Does
   not fire — Iteration 38 delivered two real, git-committed deliverables
   (`REALIZABILITY_MEMO.md` Entry 2's Amendment 6 closure and
   `lab/caveat_lint.py`); this criterion concerns historical continuity
   and is not evaluable against Iteration 39's own outcome from inside a
   Phase-2 audit, since no Phase 3/4 result yet exists for this cycle.

**Summary: criteria 1, 2, 3, and 5 do not fire. Criterion 4 fires**, on
the exact terms of a tripwire this program itself hardened one cycle ago
for this specific reason. Marsh is convened per PANEL.md's checkpoint
procedure; unblocked work continues.
