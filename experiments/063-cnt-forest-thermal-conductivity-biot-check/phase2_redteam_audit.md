# Phase 2 — RED TEAM final audit (exp-063 / Panel Iteration 40)

*Fresh sub-agent, receives everything: the Phase-1 proposal and all five
blind Phase-2 critiques. Never leads; speaks last and hardest. Standard is
NOT textbook-physics compliance — it kills internal inconsistency,
unfalsifiable claims, mechanisms that cannot be expressed as simulation
parameters, and quiet violations of a target constraint, especially #3.*

**Verified directly, not taken on any seat's word.** Independently
recomputed every number in Section 4 by direct Python invocation (not
copied from the proposal or any critique): `4εσT_amb³=5.142614061`,
`Bi(silicon,148)=1.75676e-4`, all sixteen `CF(κ,L)` cells (bench and all
four MP-5 points), `κ_critical(CF=1.35, L=1051.2µm)=0.089731`, TD-4's
margin band `[554.92×, 698.36×]` against the predicted `[555×,698×]`, and
TD-5's margin band `[1.0274×, 1.3479×]` against the predicted
`[1.03×,1.35×]` — all reproduce to the printed digit; no arithmetic
defect found, matching EM's own independent re-derivation. Read
`lab/thermo_sidecar.py` in full. **Ran `lab/caveat_lint.py` and
`lab/numeric_lint.py` live** (whole-registry, both tools) rather than
trusting VISION's prose account of what they would report — confirmed
both currently exit 0 (all registered checks pass) precisely because no
entry for `biot_number`/`front_surface_conduction_correction`/
`κ_critical`/`0.0897` exists in either registry yet; grepped
`phase1_proposal.md` directly for `NETD|human perceptual|human.eye|
constraint-3` — zero hits outside the generic §2/parameter-table
mentions, confirming VISION's claim precisely. Read `git log` for
`lab/numeric_lint.py`/`lab/numeric_lint_config.json` and
`lab/caveat_lint_config.json` to establish exact build-vs-proposal
timing (commit `2d6e5e7`, "Iteration 40 mandatory Director rider," is the
commit immediately BEFORE `9c60b05`, exp-063 Phase 1 — `numeric_lint.py`
was built this same iteration, before this proposal existed, with zero
prior opportunity to carry an exp-063 entry). Read
`experiments/034-.../REALIZABILITY_MEMO.md` Entry 2 and grepped
`experiments/061-.../` for MATERIALS' cited "front tips exposed... root
bonded" language — not found verbatim anywhere in the record (see attack
4). Independently traced `graded_black_shell`'s radial absorption
structure through LOGBOOK.md's T9 record (Iterations 4/5, `materials.py`'s
own `_graded_black`: conductivity peaks at `r_in=30`, is zero at
`r_out=78`; the radial-binned ledger measured essentially 100% of
absorption landing before the shell's outer boundary) to confirm
PHOTONICS' claim independently, not on its word. Read `PANEL.md` in full
(this seat's own charter, the Checkpoint criteria verbatim, the metrics
table), `LOGBOOK.md` in full (~12907 lines: the R1–R5 ruled-out registry,
the complete T1–T26 live-thread record, and every prior Checkpoint-4
firing's own reasoning — Iterations 17, 20, 24, 36, 37, and both
Iteration-39 firings read in full, not summarized), and both Iteration-39
CHECKPOINT blocks in `PLAN.md`'s Current-state section in full.

---

## 1. Numbered attacks (independent)

**1. [mandatory fix]** Confirms VISION's sharpest attack, independently
verified by direct grep of the live document: TD-3, TD-4, and TD-5 each
restate an UNDETECTABLE/DETECTABLE-adjacent classification without the
NETD/human-eye disclaimer appearing anywhere near the claim — the phrase
"human perceptual," "constraint-3," or any paraphrase of
`thermo_sidecar.py`'s own hard-coded disclaimer text does not occur
**anywhere** in `phase1_proposal.md`, not even once in a generic
methodology section. This is the program's oldest continuously-enforced
caveat (Iteration 20, Red Team's own attack 7: "the NETD/human-eye
conflation is a live recurrence of the exact pattern class that fired
Checkpoint criterion 4 at Iteration 17 — every claim needs its own
disclaimer AT THE POINT OF THE CLAIM"), permanently hard-coded into every
dict `mixed_length_scale_regime` and `netd_disposition` return. It matters
more this cycle than any prior one: TD-5 is explicitly billed as this
program's "first-ever thermal-detectability classification flip" —
exactly the framing under which a reader is likeliest to conflate
instrument-DETECTABLE with eye-visible. **A genuinely new finding this
audit adds, not raised by VISION or any other seat**: the disclaimer rule
itself has never been promoted into a `lab/caveat_lint_config.json`
registry entry across 20 iterations of enforcement — it survives purely
on code-dict convention and institutional memory, with zero mechanical
propagation check on the PROSE (as opposed to the `results.json` dicts,
which carry it structurally). Mandatory: (a) the verbatim sentence at
TD-3/TD-4/TD-5's own table rows; (b) a new registry entry for the rule
itself (not just this cycle's instance of it) — closing a two-decade-old
gap in the registry's own coverage, not only patching exp-063.

**2. [confirmed live, does NOT independently fire Checkpoint-4 — full
argument in Section 3]** Confirms VISION's registry-propagation finding
by direct tool execution, not by trusting its prose: `python3
lab/caveat_lint.py` and `python3 lab/numeric_lint.py` both exit 0 today,
and neither registry contains any entry whose `trigger_terms`/patterns
would match `κ_critical`, `0.0897`, `biot_number`, or
`front_surface_conduction_correction`. This is not a coverage gap in an
existing entry (the shape both Iteration-39 firings were) — it is the
complete absence of any entry for numbers that did not exist in the
record before this cycle's own Phase 1 commit (`9c60b05`), one commit
after `numeric_lint.py` itself was built (`2d6e5e7`). Idealization 8's
"whatever new sourced numbers need a registry entry at Phase 3/5" is
vague but not evasive — see the ruling below on whether vague counts as
a defect worth firing on.

**3. [inconsistency]** Confirms and independently verifies PHOTONICS'
attack. Traced `graded_black_shell`'s conductivity law directly:
`_graded_black`'s `d = clip((r_out−rr)/(r_out−r_in),0,1)` puts `d=1`
(peak σ) at `rr=r_in=30` and `d=0` (zero σ) at `rr=r_out=78` —
independently re-confirmed against LOGBOOK's own T9 record (Iteration 4
EM, Iteration 5 THERMO/Red Team: the radial-binned ledger measured
essentially all Joule dissipation landing before the shell's outer
boundary, core_frac≈0.00–0.01%). Section 4's model puts `P_abs` "enters
uniformly over the illuminated FRONT surface" and treats `L=l_geometric_m
=r_out` as the conduction path from that front surface to a rear-only
loss channel — for the bench-scale flagship specifically, this is
optically backwards from where the object's own established absorption
profile says power actually lands (near `r_in`, deep in the shell, not at
`r_out`). `gas_conduction_h_eff`'s own docstring text ("NEVER an
optical/extinction-derived length") is not the rule being broken here —
PHOTONICS is right that it's a *different* conflation on a new axis
(`l_geometric_m` reused as both the licensed radiating envelope AND an
unlicensed absorption-to-loss-surface conduction path). Confirmed
independently: at bench scale `Bi_rad(L=2.34µm)` is 3–4 orders of
magnitude below `Bi_gas` at every κ in the predicted band (my own
recomputation above), so this conflation is numerically inert for
TD-3/TD-4 specifically — it does not move those two predictions — but it
is exactly the sort of unexamined assumption that should not be allowed
to season a "first-ever classification flip" claim (TD-5) without at
least being named.

**4. [inconsistency]** Confirms MATERIALS' attack on its substance;
partial correction on its sourcing. The physical point — real CNT-forest
record-blackness coatings are grown ON a substrate (root-bonded), with
the growth axis exposed to the ambient at the tip, not free-standing on
both faces — is well-supported by the program's own established language
("coating" is used throughout `REALIZABILITY_MEMO.md` Entry 2 and every
exp-061/062 citation of the candidate class). But MATERIALS' own quoted
phrase — "front tips exposed to air/light, root bonded to whatever it
blacks out," attributed to "`REALIZABILITY_MEMO.md` Entry 2, exp-061/062"
— does not appear verbatim anywhere in either file on direct grep. This
is MATERIALS' own reasonable elaboration of an established program
convention, not a fabricated citation, but it is presented as though
quoted from the record; Phase 3 should state the deployment-geometry
argument as MATERIALS' own physical reasoning, not as an existing program
finding. The underlying attack stands regardless: §4's rear-only-loss
choice is asserted, not derived, as the worst case for THIS geometry, and
a front-colocated-loss variant is a live, unexamined bracket, not a
straw man — Idealization 1's own "a real object loses some heat locally
near the front too" sentence already half-concedes this without following
it to its conclusion.

**5. [inconsistency, deferred-not-resolved]** Confirms EM's attack.
Independently traced the license test: `gas_conduction_h_eff`'s docstring
requires `l_geometric` be "a real geometric length of the
conducting/radiating SOLID body... NEVER an optical/extinction-derived
length (e.g. `w_on = sigma_ext_cells*dx_m`)." The witness-scale `L` values
this proposal reuses verbatim (331.2–1051.2µm) are exp-061's MP-5
figures — themselves `(required thickness at a real CNT-forest α)/(1.44µm)
× 1.44µm`, i.e. a thickness *back-calculated* from a sourced optical
absorption coefficient (`τ_true/α`), not a directly measured geometric
length of any simulated or real object. Confirmed by direct LOGBOOK.md
grep that this exact concern was raised and explicitly deferred at
Iteration 39 (line 12726–12729: "Red Team's own independent tracing found
this closer to `thermo_sidecar.py`'s own 'never an optical/extinction-
derived length' guardrail than disclosed") on the identical `l_geometric_m`
lineage this proposal now reuses in a *more* geometrically demanding role
(a literal Fourier conduction-path length, not merely an `h_eff`/mass/area
scale). Exp-063 is silent on all of it. This is not a rederivation
request — EM is right that the resistance-network algebra is agnostic to
what `L` physically means — but TD-5's *physical conclusion*, the one
prediction billed as this program's first classification-flip candidate,
is not yet entitled to treat that length as settled.

**6. [mandatory fix]** Confirms QUANTUM's attack. `P_abs` is reused
verbatim as the lattice-heat input to Section 4's conduction chain with
no stated `η_thermal` coupling-efficiency parameter — the first cycle
to source any material-specific constant for the actual candidate
identity, and the natural place this was owed. QUANTUM's own physical
argument (near-zero PL quantum yield, sub-ps electron-phonon relaxation
in graphitic/semi-metallic carbon) is standard and almost certainly
correct, but "almost certainly correct" is doing unstated work directly
under TD-5.

**7. [inconsistency — new, not raised by any of the five critiques]**
Section 5/TD-5's own text calls a κ<0.0897 DETECTABLE flip
"Checkpoint-1/2-adjacent, requiring escalation." This over-reaches.
PANEL.md's Checkpoint criteria 1 and 2 are specifically about the FOUR
NUMBERED TARGET CONSTRAINTS (beam termination, no specular return, no
ambient silhouette, transient/switchable) — "a configuration passes ALL
constraint metrics" (1) and "a constraint subset shown jointly
unsatisfiable" (2). This cycle self-declares, correctly, "zero
constraint-1/2/3/4 metric scored" — and VISION's own critique
independently confirms a thermal-IR microbolometer-DETECTABLE finding is
orthogonal to constraint 3/4's human-eye question, not merely adjacent to
it. Labeling a possible TD-5 outcome "Checkpoint-1/2-adjacent" invites a
reader — including, per VISION's own worry, an excited Phase-4/5
write-up — to read a realizability-margin tightening as movement toward
an actual target-constraint result, the identical conflation VISION's own
attack 1 is built to prevent, now appearing in the predictions section's
own escalation language rather than in a missing disclaimer. Mandatory:
relabel as "a significant realizability-margin finding warranting
Director/Marsh attention" without invoking Checkpoint criteria 1/2 by
number.

**Confirmed clean, not an attack.** Idealizations 2 (steady-state only, ρ
and C_p untouched), 3 (adjacent-application-class provenance, correctly
inherited from exp-061's own convention), 5 (linearization at T_amb, not
front-surface T — self-consistent given every ΔT in this program's record
is µK–mK scale), 6 (no double-dilution of an already-effective published
κ), and 7 (T18 re-confirmation convention) are all honestly stated and
require no correction. TD-1/TD-2's predicted bands are genuinely
falsifiable, with real literature-checkable failure conditions, not
loose enough to be guaranteed. No re-proposal of R1–R5 or any refuted
T1–T26 finding was found on direct read of the full ruled-out registry
(LOGBOOK.md lines 8–74) and the complete live-thread record — this is a
zero-mechanism, zero-FDTD model-fidelity continuation in the established
T22/T23/Iteration-25 register, and "T1 escape route: N/A" is honestly
declared and true on inspection; no `constraint-#N-violation` tag applies
anywhere in this cycle, and none of the five critiques found one either.

---

## 2. Adjudication of the five critiques

**PHOTONICS — CONFIRM**, independently re-traced through `materials.py`
and LOGBOOK's own T9 record rather than taken on trust (attack 3 above).
PHOTONICS' own directional read — that a corrected generation length
would likely *shrink*, not grow, the witness-scale correction — is
consistent with my own recomputation: Bi_rad is the only length-dependent
term, and nothing in a more front-loaded generation profile would make
the REAR-only loss assumption (a separate variable) worse.

**MATERIALS — CONFIRM the substance, correct the sourcing** (attack 4
above). The deployment-geometry argument is sound and important; the
specific quoted phrase attributed to the program record is MATERIALS'
own paraphrase, not a verbatim finding — Phase 3 should attribute it
correctly.

**ELECTROMAGNETISM — CONFIRM**, on independent re-derivation of both the
algebra (clean, matches to the printed digit) and the T23-licensing gap
(attack 5 above, independently traced to the exact LOGBOOK.md line
recording the Iteration-39 deferral). EM's own framing — "not a
rederivation, only an honest bookkeeping step this program has already
built the vocabulary for" — is accurate; this is the correct scope for
the fix.

**QUANTUM OPTICS — CONFIRM** (attack 6 above). The physical argument for
η_thermal≈1 is sound and cheap to state; the gap is disclosure, not
physics.

**VISION SCIENCE — CONFIRM both findings, independently re-verified by
direct tool execution and direct document grep**, not relayed. On the
Checkpoint-4 question VISION explicitly deferred to the Director/Red
Team: see Section 3 below for the full ruling, argued from the actual
Iteration-38/39 precedent text, not from a general sense that registry
gaps are bad.

### On the three-way convergence (PHOTONICS / MATERIALS / EM) — do they
agree, contradict, or triangulate?

**They triangulate — three independent, non-contradictory findings about
three different variables in the same Section-4 model, not three
readings of the same defect.**

- **PHOTONICS** attacks the **generation-side geometry** (where power
  enters the solid) — bench-scale-specific, since it is argued directly
  from T9's own measured radial profile for `graded_black_shell`, a
  bench construction. PHOTONICS itself grants that front-loading is
  separately defensible at witness scale (exp-061's own `α_true≈5.74×10⁴
  cm⁻¹`, e-fold≈174nm, means real absorption genuinely concentrates near
  the illuminated face there) — so this attack's force is concentrated on
  TD-3/TD-4, where I independently confirm it is numerically inert
  (Bi_gas dominates by 3–4 orders of magnitude), not on TD-5.
- **MATERIALS** attacks the **loss-side geometry** (where heat exits) —
  witness-scale-specific, argued from the real deployment's own
  substrate-bonded rear face, orthogonal to where absorption is
  generated. This is the attack that actually bears on TD-5's
  κ_critical=0.0897 falsification boundary.
- **ELECTROMAGNETISM** attacks neither boundary condition directly — it
  attacks whether the **length itself** (`L=τ_true/α`) is a legitimate
  input to `h=k/L` at all, a licensing question that would need
  resolving regardless of which of MATERIALS' two boundary-condition
  brackets is correct.

**Where they agree:** all three converge on the same conclusion —
TD-5's κ_critical=0.0897 boundary rests on Section-4 geometric
assumptions that have not been examined against this program's own
standing findings (T9, T23, `REALIZABILITY_MEMO.md` Entry 2), and none
of the three thinks this overturns TD-4's flagship UNDETECTABLE finding.
**Where they agree on direction:** PHOTONICS (a corrected generation
length would shrink the correction) and MATERIALS (a corrected loss
geometry would push CF toward 1) point the SAME way — both suggest, if
anything, the real correction is smaller than Section 4's worst-case
number, not larger. Neither seat's fix would move TD-5 toward
DETECTABLE. EM's finding carries no directional claim at all — it is a
gate on whether the calculation is licensed to run at all with this `L`,
independent of which direction any fix to it would push. **Conclusion
for the Director**: TD-5 should not be dropped (none of the three seats
argues for that, and the underlying Biot arithmetic is sound throughout)
but should ship as an explicit bracket (MATERIALS' fix) with both the
generation-geometry caveat (PHOTONICS' fix) and the length-licensing
caveat (EM's fix) stated inline, not resolved by omission — a
reframing, not a rejection, of TD-5's headline number.

---

## 3. The central ruling: does VISION's registry-gap finding fire
Checkpoint criterion 4?

**Ruling: NO — does not fire.** This is the single highest-stakes call in
this audit, and it is argued from the actual text of the two closest
precedents, not from a general instinct that registry gaps are bad.

**The task brief asks the right question directly: is this a NEW gap in
a tool JUST built this same iteration with no prior chance to register
it, or a gap in an EXISTING registry entry that already carried a
documented propagation promise?** On direct inspection it is
unambiguously the former, on two independent grounds:

1. `lab/numeric_lint.py` was committed at `2d6e5e7` ("Iteration 40
   mandatory Director rider"), the commit **immediately before**
   `9c60b05` (exp-063 Phase 1). Its registry carries exactly two entries,
   both inherited from exp-062's own Phase-5 R-vs-T fix — there has never
   been a point in this tool's existence where an exp-063 entry could
   have been added before this cycle's own Phase-1 proposal existed to
   register.
2. `lab/caveat_lint_config.json` is an existing, six-entry registry, but
   none of its six entries' `trigger_terms` are about `κ_critical`,
   `biot_number`, or `front_surface_conduction_correction` — these are
   not an existing entry's coverage gap (the shape of both Iteration-39
   firings, where a hardened, previously-widened `exp061-t18-
   evidentiary-tier-propagation` entry failed to discover a NEW file it
   was supposed to be able to find). They are numbers that simply did
   not exist in the record before this cycle's own Phase-1 commit.

**This is the exact fact pattern Red Team already ruled on, one cycle
earlier than the ones cited in the task brief, at Iteration 38 — a
closer precedent than either Iteration-39 firing.** At Iteration 38,
VISION found, live, that `lab/caveat_lint.py` — a tool built THAT SAME
cycle — failed its own self-referential check: the T18-propagation
disclosure had not propagated to Phase-1's own verdict-bearing rows,
inside the very cycle that built the tool. LOGBOOK.md records the ruling
verbatim (line 12539–12541): **"Red Team ruled this does NOT fire
Checkpoint criterion 4 (a self-caught, pre-freeze registration gap, not a
docketed propagation promise broken by hand-review) but set a binding
forward tripwire on any recurrence after the fix lands."** That is
exactly this cycle's shape: a brand-new number/machinery, found missing
its registry entry at Phase 2, before Phase 3 freeze, by the panel's own
review process working as designed — not a promise already made and
broken.

**The Iteration-39 double-firing is textually distinguishable, not just
factually different.** Both Iteration-39 firings hit
`exp061-t18-evidentiary-tier-propagation`, an entry Red Team had
EXPLICITLY hardened at Iteration 38's own close, in writing, to strip out
the ordinary "caught before Phase 3 froze" safe harbor for that one
lineage specifically, after its self-catch grace had already been spent
twice in a single prior cycle: *"any further gap in this specific
entry's coverage, discovered at Iteration 39 or later, auto-fires
criterion 4, no further deliberation."* No such hardened, safe-harbor-
stripped tripwire exists for anything in exp-063's own new machinery —
there is no prior "grace already spent" event for `biot_number` or
`κ_critical` because they have never existed before this cycle. Exp-062's
own Phase-2 Red Team audit states the program-wide DEFAULT plainly, and I
adopt its reasoning rather than re-deriving it: "LOGBOOK.md's own
Iteration 37 record establishes... the program-wide default... a
caveat-placement gap caught at Phase 2, before Phase 3 synthesis, does
NOT fire Checkpoint-4." The Iteration-39 firings are the narrow,
textually-justified EXCEPTION to that default, not a new default of their
own — extending their zero-tolerance language to every unrelated registry
gap found at Phase 2 would itself be exactly the kind of "further
deliberation"/unargued extension by analogy Iteration 39's own ruling
(PLAN.md line 135–141, on the sibling `exp061-thermo-length-scale-
staleness` gap) explicitly declined to do even for a closely related
entry in the SAME cycle.

**Ruling, stated plainly**: VISION's finding is real, correctly argued,
and must be fixed at Phase 3 — but it is ordinary, expected, pre-freeze
Phase-2 feedback of exactly the kind this program's Phase 2/3 loop exists
to catch and correct before it ever reaches committed record. **A
forward tripwire is set here, matching the program's own standing
pattern for exactly this situation**: if either registry gap (κ_critical/
biot_number machinery in `caveat_lint_config.json`, or the bench-vs-
witness derivation-consistency entry in `numeric_lint_config.json`) is
NOT added at Phase 3, or if a materially similar gap in either of THESE
specific new entries is found again at Phase 5 or any later iteration,
that DOES fire Checkpoint criterion 4 without further deliberation —
the same self-catch-grace mechanism this program has now applied
consistently at Iterations 23, 37, and 38.

---

## 4. Final ruling

**PROCEED-WITH-MANDATORY-FIXES.**

The core Biot/conduction-resistance derivation in Section 4 is sound,
independently re-derived twice now (EM's critique, this audit) and
confirmed to the printed digit; the κ_solid gap it closes is real and
long-overdue (silicon-proxied, unsourced, since Iteration 25); the
κ_solid→∞ absolute-identity gate is genuine. No defect found here
requires abandoning the cycle's scope or returning to Phase 1 — every
attack above is a scoped, cheap-to-apply correction, the posture Red Team
has taken at every comparable realizability/instrument-fidelity
continuation (exp-036/037/054/060/061/062). None of the five blind seats
opposed.

### Mandatory-fix docket (before Phase 4 search runs)

1. Add the NETD/human-eye instrument-vs-constraint-3 disclaimer verbatim
   at TD-3, TD-4, and TD-5's own table rows/claim points — not only in
   §2's generic framing (VISION's flip condition). Separately, open a
   standing item (not blocking this cycle) to give the disclaimer itself
   its first `lab/caveat_lint_config.json` registry entry, closing a
   20-iteration-old gap in the registry's own coverage of this rule.
2. Add concrete `lab/caveat_lint_config.json` entries for `κ_critical=
   0.0897` and the `biot_number`/`front_surface_conduction_correction`
   machinery, with the NETD disclaimer as a `phrase_pattern`, drafted at
   Phase 3, not deferred as "whatever needs it" (VISION §3
   recommendation).
3. Add a `lab/numeric_lint_config.json` `derivation_consistency` entry
   keyed to this proposal's own bench-vs-witness application of one
   `CF(κ,L)` formula at two length scales — the module's own docstring
   names exp-062's EM-6/EM-7 drop as its structural regression case; this
   proposal's split is a textbook twin (VISION §3 recommendation).
4. Disclose in §7 that `L=l_geometric_m` is reused at bench scale in a
   role (absorption-to-loss-surface conduction distance) its own
   docstring never licenses, and that this contradicts T9's established
   radial ledger for the flagship specifically (PHOTONICS' flip
   condition, attack 3 above).
5. Add a second closed-form variant (front-colocated loss, correction
   factor → 1 identically) alongside §4's rear-only variant, reporting
   BOTH at every TD-3/4/5 cell as a bracket, not a single "the" corrected
   margin, until the substrate-interface question is resolved or
   explicitly left open (MATERIALS' flip condition, attack 4 above;
   correct the sourcing of the "coating on a substrate" language to
   MATERIALS' own reasoning, not a program-record quote).
6. Add one sentence to §7 disclosing that witness-scale `L` (`t=τ_true/α`)
   has never been run through T23's own licensing test for `h=k/L`
   conduction lengths — flagged open at Iteration 39 (and, per THERMO's
   own trace, adjacent territory at Iteration 38), unresolved here; TD-5's
   disposition is conditional on that length being licensed, not a clean,
   self-contained finding (EM's flip condition, attack 5 above).
7. Add one Idealization item naming and justifying `η_thermal≡1`,
   citing standard carbon-nanomaterial photophysics (QUANTUM's flip
   condition, attack 6 above).
8. Relabel TD-5's "Checkpoint-1/2-adjacent, requiring escalation"
   language: Checkpoint criteria 1/2 concern the four numbered target
   constraints, none of which this cycle scores; state instead as "a
   significant realizability-margin finding warranting Director/Marsh
   attention," without invoking Checkpoint criteria 1/2 by number (Red
   Team's own attack 7, not raised by any blind seat).

---

## 5. Checkpoint criteria — explicit ruling, all five

1. **A configuration passes ALL constraint metrics.** Does not fire —
   zero constraint-1/2/3/4 metric is scored this cycle; "T1 escape route:
   N/A" is honestly declared and true on inspection. Attack 7 above exists
   precisely because the proposal's own language risks blurring this
   line without actually crossing it.
2. **A proven boundary: a constraint subset shown jointly unsatisfiable
   within a whole mechanism class, gates clean.** Does not fire — this
   cycle touches no mechanism or constraint at all; it is an instrument/
   model-fidelity correction to an already-issued realizability-adjacent
   disposition (exp-057/exp-061's THERMO box), not a new proof of joint
   unsatisfiability, and does not gate clean given the open mandatory-fix
   docket above.
3. **A synthesis requires engine physics beyond the validated bench
   classes.** Does not fire — zero FDTD, zero `lab/` engine file touched
   by this proposal (only `thermo_sidecar.py`, a non-FDTD analytic
   module, gains two new functions); confirmed by direct read of §2's own
   scope statement and Idealization 8.
4. **Program-integrity drift (unfalsifiable claims, a constraint quietly
   dropped — especially #3).** **Does not fire.** See Section 3's full
   argument: VISION's registry-gap finding is a self-caught, pre-freeze
   registration gap on brand-new numbers in a tool built this same
   iteration — the Iteration-38 precedent for exactly this shape, not the
   Iteration-39 precedent for a previously-hardened tripwire's own
   coverage failure. A forward tripwire is set on both new entries
   (Section 3, final paragraph): any recurrence surviving to Phase 5 or a
   later iteration in either of THESE specific entries auto-fires
   criterion 4 without further deliberation, matching this program's own
   standing self-catch-grace mechanism (Iterations 23, 37, 38).
5. **Two consecutive iterations with no logbook-advancing result.** Does
   not fire — Iteration 39 (exp-062) delivered a real, git-committed
   result (EM-2/EM-3/EM-4 CONFIRMED more decisively than predicted, the
   `n_eff` primary-source pin); this criterion concerns historical
   continuity and is not evaluable against Iteration 40's own outcome
   from inside a Phase-2 audit, since no Phase 3/4 result yet exists for
   this cycle.

**Summary: none of the five Checkpoint criteria fires.** Marsh is not
convened this cycle. Phase 3 synthesis should proceed with the
eight-item mandatory-fix docket above, item 1 and item 5 first (the
two that reframe TD-5's own headline number, the prediction most likely
to be quoted out of context).
