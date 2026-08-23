# Phase 5 — RED TEAM final audit (exp-063 / Panel Iteration 40)

*Fresh sub-agent, receives everything: the full Phase 1–4 record and all
six Phase-5 blind reviews. Never leads; speaks last and hardest. Standard
is NOT textbook-physics compliance — it kills internal inconsistency,
unfalsifiable claims, mechanisms that cannot be expressed as simulation
parameters, and proposals that quietly violate a target constraint,
especially #3.*

**Read in full before writing this**: `PANEL.md` (all five Checkpoint
criteria verbatim, this seat's own charter); `LOGBOOK.md` in full
(~12,907 lines — the R1–R5 ruled-out registry, the complete T1–T26
live-thread record, and every prior Checkpoint-criterion-4 ruling's own
reasoning, read in full, not summarized: Iterations 17, 20, 24, 32, 33,
34, 35, 36 (two independently-confirmed instances of the caveat-placement
pattern in one cycle), 37, 38 (two self-caught, non-firing instances),
and both Iteration-39 firings); `PLAN.md`'s Current-state section, both
Iteration-39 CHECKPOINT blocks in full; the complete exp-063 record
(`phase1_proposal.md`, all five `phase2_critique_*.md`,
`phase2_redteam_audit.md`, `phase3_synthesis.md`, `NOTES.md`,
`phase4_results.md`, all six `phase5_review_*.md`); `lab/thermo_sidecar.py`,
`lab/validation/run_all.py::stage23_front_surface_biot_correction`,
`lab/caveat_lint.py` + `lab/caveat_lint_config.json`, `lab/numeric_lint.py`
+ `lab/numeric_lint_config.json` in full. **Everything below that can be
run was run live this session, not taken on any seat's or any prior
audit's word** — see §1.

---

## 1. Independent live verification (before adjudicating anything)

```
$ python3 lab/validation/run_all.py --only 12346789,10,11,18,19,20,21,22,23
... 78/78 checks passed in 133s, including stage 23 (4/4):
  [PASS] correction_factor(k_solid=1e30) == 1 (k_solid->infinity limit)
  [PASS] CF(kappa=2.0 W/mK, L=bench=2.34um) vs exp-063 Phase-1 script output: 1.013006
  [PASS] CF(kappa=2.0 W/mK, L=MP5-730x=1051.2um) vs exp-063 Phase-1 script output: 1.015703
  [PASS] kappa_critical (CF(MP5-730x)==1.35 bisection) vs exp-063 Phase-1 Section 4: 0.089731

$ python3 lab/caveat_lint.py
8 caveat(s) checked, 0 required-site failure(s).   EXIT=0

$ python3 lab/numeric_lint.py
3 entry(ies) checked -- all PASS.   EXIT=0
```

Independently recomputed `biot_number`/`front_surface_conduction_correction`
by direct invocation of `lab/thermo_sidecar.py` (not copied from any
document) at all four sourced κ and both geometries:

```
kappa= 0.70  CF_bench=1.037160  margin_bench=674.216097   CF_mp5=1.044866  margin_mp5=1.292032
kappa= 9.62  CF_bench=1.002704  margin_bench=697.384305   CF_mp5=1.003265  margin_mp5=1.345607
kappa=40.00  CF_bench=1.000650  margin_bench=698.815560   CF_mp5=1.000785  margin_mp5=1.348941
kappa=50.00  CF_bench=1.000520  margin_bench=698.906400   CF_mp5=1.000628  margin_mp5=1.349153
kappa_critical = 0.089731 W/(m*K)
```

Matches `phase4_results.md`'s own summary table, EM's Phase-2 critique,
Red Team's own Phase-2 audit, and all six Phase-5 reviews' own independent
re-derivations to the printed digit. **This is now the fifth independent
re-derivation of Section 4's algebra to reach the identical numbers with
no arithmetic defect found anywhere.** Also read `lab/caveat_lint_config.json`
and `lab/numeric_lint_config.json` directly (not via any seat's quotation)
— confirmed below in §3.

**Verdict on the raw physics: sound, unanimously, on every independent
check this cycle and this audit produced.** Nothing in this audit
disputes a single scored number in `phase4_results.md`. What follows is
entirely a process-completeness question.

---

## 2. Independent verification of the six seats' claims

### 2.1 PHOTONICS (PROMISING) — the generation-side finding, and the new material-provenance finding

**Own Phase-2 attack confirmed closed.** Re-traced `materials.py`'s
`_graded_black` myself: `d = clip((r_out−rr)/(r_out−r_in),0,1)`, so
σ peaks at `r_in=30` and is zero at `r_out=78` — T9's radial-absorption
ledger, independently re-confirmed a fourth time (Iteration 4 EM,
Iteration 5 THERMO/Red Team, Iteration-40 Phase-2 Red Team, now this
audit). Idealization 9 states the contradiction verbatim, correctly
scoped to bench scale. Confirmed numerically inert for TD-3/TD-4: at
bench scale (`L=2.34µm`), `Bi_rad` ranges `2.4×10⁻⁶`–`8.8×10⁻⁵` across
the sourced κ range, three to four orders of magnitude below `Bi_gas`
(`5.2×10⁻⁴`–`3.7×10⁻²`) at every point. **Closed, confirmed independently
a fifth time.**

**New finding (§2 of PHOTONICS' review): verified, and important.**
TD-5's single correction factor combines `α_true` (this program's own
Beer–Lambert e-fold constant, exp-061/062, checked against a comparator
set of real published CNT-forest α figures spanning record-blackness/
Vantablack-adjacent application classes) with `κ_solid` (this cycle,
sourced from a bulk/aggregate mat, a VACNT-on-graphene-oxide composite,
and a densified/drawn sheet — three geometry classes, none of them
established as the SAME material as `α_true`'s own comparator set, and
none of them the program's own actual record-blackness/Vantablack
candidate either). Checked directly: nothing in this cycle's or exp-061/
062's own record establishes common provenance between the optical and
thermal constants TD-5 multiplies together. This is real and,
correctly, PHOTONICS does not claim it moves any verdict — the sourced κ
band brackets κ_critical comfortably regardless of which specific class
governs. **Confirmed, ranked into this audit's own top-3 below (item 3).**

### 2.2 MATERIALS (PROMISING) — the bracket flip condition, and the substrate-contact-resistance finding

**Own Phase-2 flip condition (the front-colocated bracket) confirmed
satisfied.** `NOTES.md`'s "The closed-form front-surface correction"
section adds exactly the bracket MATERIALS asked for; `phase4_results.md`
reports both endpoints at every TD-3/4/5 cell; Red Team's own Phase-2
sourcing correction (the "front tips exposed... root bonded" phrase is
MATERIALS' own reasoning, not a program-record quote) is applied
correctly in `NOTES.md`'s text. **Closed.**

**New finding (§3 of MATERIALS' review): verified, and this audit's
single most consequential open-physics item.** Query 10 (this cycle's
own Phase-4 result) found inter-tube van der Waals junction thermal
contact resistance (~4×10⁻⁸ m²K/W) nearly three orders of magnitude
worse than a covalent junction (~6×10⁻¹¹ m²K/W) — the SAME weak-contact
mechanism Phase 1's own hypothesis names as the reason CNT forests are
poor through-thickness conductors at all. MATERIALS is correct that
this mechanism plausibly also governs the forest ROOT's own bond to a
mounting substrate — a real fabrication interface neither of the two
coded brackets (front-colocated, correction≡1; rear-only, to quiescent
air) models, and one that would add a THIRD series resistance ON TOP of
whichever bracket endpoint currently governs, not fall between them.
Independently recomputed the headroom claim: `0.70/0.089731 = 7.80×` —
confirmed exactly, and correctly identified as this program's thinnest
safety factor of any kind on record (TD-4's bench margin has ≥6.7×
headroom on an entirely different, much larger absolute scale). This is
a flagged mechanism, not a scored finding (MATERIALS' own honest framing,
no query targeted it this cycle) — but it is the sharpest reason on the
table that "TD-5 does not materialize" should not be read as "TD-5 is
now closed." **Confirmed, ranked into this audit's own top-3 below
(item 2).**

### 2.3 ELECTROMAGNETISM (PROMISING) — the T23 forcing-mechanism argument

**Independently re-traced the licensing text**: `gas_conduction_h_eff`'s
docstring states, unconditionally, that `l_geometric` must be "a real
geometric length of the conducting/radiating SOLID body... NEVER an
optical/extinction-derived length." TD-5 reuses `L=τ_true/α` — a
thickness back-calculated from a sourced optical absorption coefficient
— in exactly the forbidden category, on the rule's own plain text, not
a hard case. Confirmed by direct `LOGBOOK.md` grep that this exact
lineage was flagged and explicitly deferred at Iteration 38 (THERMO) and
Iteration 39 (EM/Red Team, "closer to the guardrail than disclosed"),
and now a third time here (Red Team's own Phase-2 audit, attack 5,
mandatory fix 6 — disclosure only, not resolution).

**EM's central argument — independently evaluated on its own terms, not
adopted on authority.** EM does not argue this fires Checkpoint criterion
4 for exp-063 (EM explicitly disclaims that reading, correctly — this is
a substantive-physics deferral, honestly disclosed each time, not a
broken registry promise). EM instead asks this seat to treat a FOURTH
deferral past Iteration 41 as its own program-integrity finding, drawing
the explicit analogy to this program's self-catch-grace mechanism
(`exp061-t18-evidentiary-tier-propagation`'s own grace, declared fully
spent after its second self-catch at Iteration 38, with the next
recurrence auto-firing at Iteration 39). **I find this argument sound and
adopt it as a binding forward commitment, not merely a ranked priority**
— see §6.

### 2.4 THERMODYNAMICS (PROMISING, this cycle's own lead seat reviewing fresh) — the NOTES.md gap

**Independently re-verified.** `grep -n "^## " NOTES.md` confirms:
Hypothesis, Setup, "The closed-form front-surface correction," Falsifiable
predictions, Idealizations, Registry, Next — no `## Result`, no
`## Learned`. `git log` on the file: written once at the Phase-3 commit,
never touched since; `## Next` still reads as though Phase 4 has not run.
This is a real, checkable gap against this program's own house convention
(CLAUDE.md: "hypothesis / setup / result / learned / next") and its own
recent, consistent practice (exp-054, -060, -061, -062 all give `NOTES.md`
its own `Result`/`Learned` sections). **Confirmed. Correctly ruled by
THERMODYNAMICS as not itself a Checkpoint-4 matter** — no wrong number
propagates from it, `phase4_results.md` is the complete, independently-
reproducible record, and this program's own pattern fills this
customarily at Phase 5 close. **Made mandatory in this audit's own
docket (§5, item 5).**

**THERMODYNAMICS' own assigned question — is the boundary-condition
bracket worth prioritizing ahead of T23?** Independently re-derived the
same arithmetic: at the single worst sourced κ (0.7), the bracket spans
`[1.0×, 1.2920×]` at witness scale and `[699.27×, 674.22×]` at bench
scale — both endpoints clear their own falsification bars comfortably.
I agree the bracket is currently inert and should not be prioritized
ahead of T23 or the substrate-contact-resistance question — but I note
(§2.2 above) that MATERIALS' Phase-5 finding sharpens WHY the bracket
itself may not be the right frame at all (a third, worse scenario, not
an intermediate one) — this doesn't change THERMODYNAMICS' own
de-prioritization ruling, since that third scenario is unscored either.

### 2.5 QUANTUM OPTICS (PROMISING) — the η_thermal arithmetic

**Independently re-derived the sensitivity direction.**
`margin_actual = margin_computed / η_thermal` for any `η_thermal ≤ 1`,
confirmed by inspection of `front_surface_conduction_correction`'s own
linearity in whatever heat power drives the conduction chain — a lower
η_thermal can only WIDEN every margin, never narrow one toward
DETECTABLE. **Confirmed correct, not backwards.** QUANTUM's conclusion —
pinning η_thermal is not a priority, since its own uncertainty is
one-sided-safe — is right, and its low-priority flag (a non-thermalized
fraction must be re-emitted somewhere, possibly outside the thermal-IR
band this program's NETD channel tracks) is a genuinely new,
correctly-scoped-as-not-urgent observation. **Confirmed, carried forward
at low priority, not in this audit's own top-3** (nothing in the sourced
material identity gives this a live path to threatening a classification
this cycle or plausibly next cycle).

### 2.6 VISION SCIENCE (PROMISING) — three findings, adjudicated in §3–4

VISION's three findings are the load-bearing content of this audit and
are adjudicated in full below, not summarized here. Headline: findings
1 and 3 are confirmed exactly as stated and are made mandatory
same-shift fixes (§5). Finding 2 is confirmed exactly as stated but
**this audit rules differently than VISION's own §4 on whether it fires
Checkpoint criterion 4** — see §3.

---

## 3. The central ruling: does VISION's finding 2 (the `numeric_lint`
entry's own narrow site scoping) fire Checkpoint criterion 4?

**Ruling: YES — it fires. This is the one point on which this audit
overrides every one of the six Phase-5 seats, including VISION's own
reading of its own finding, and it is argued from the actual text of
this cycle's own pre-committed tripwire, not from a general instinct
that registry gaps are bad.**

### 3.1 What VISION found, independently re-verified live

```
$ python3 -c "
import json
d = json.load(open('lab/numeric_lint_config.json'))
for e in d:
    if e['id']=='exp063-cf-bench-vs-witness-derivation':
        print(e['site'])
"
experiments/063-cnt-forest-thermal-conductivity-biot-check/NOTES.md
```

Confirmed exactly: the entry's `site` field names one file, `NOTES.md`,
never `phase4_results.md`. Running `python3 lab/numeric_lint.py` shows
both PASS lines for this entry citing only `NOTES.md`. **VISION's fact
pattern is correct in every particular, independently re-verified, not
relayed.**

### 3.2 A finding VISION did not make, which this audit adds: the
identical gap-shape exists in a SECOND of the cycle's own three new
entries

```
$ python3 -c "
import json
d = json.load(open('lab/caveat_lint_config.json'))
for e in d:
    if e['id'].startswith('exp063'):
        print(e['id'], '->', e.get('required_sites'))
"
exp063-biot-correction-machinery         -> ['.../NOTES.md', '.../phase4_results.md']
exp063-thermo-disposition-netd-disclaimer -> ['.../NOTES.md']
```

`exp063-thermo-disposition-netd-disclaimer`'s `required_sites` covers
only `NOTES.md`, never `phase4_results.md` — the same narrow-scoping
shape as the `numeric_lint` entry, in a *different* registry (`caveat_lint`,
not `numeric_lint`), independently discovered by this audit, not named
by any of the six blind Phase-5 reviews. I checked whether this hides a
live violation the way Iteration 39's second firing did: it does not —
`phase4_results.md` genuinely carries the NETD disclaimer at every
TD-3/4/5 claim point (confirmed by direct grep, matching VISION's own
§1.2 finding), so the content is correct, only the mechanical check's
own reach is short, identical in kind to VISION's finding 2. **This
means the cycle's own three brand-new registry entries carry this exact
scoping gap in TWO of three, not one** — a systemic pattern in how this
cycle built its own registry machinery, not an isolated slip.

### 3.3 The two candidate precedents, applied to the actual text

**Precedent A — Iteration 38 (the precedent Red Team's own Phase-2 audit
this cycle invoked for VISION's *different*, Phase-2-stage finding):** a
caveat-lint gap found in a tool built THAT SAME cycle, with no entry that
could have existed before that cycle's own Phase-1 commit, is "a
self-caught, pre-freeze registration gap, not a docketed propagation
promise broken by hand-review" — does NOT fire, but sets "a binding
forward tripwire on any recurrence after the fix lands." This is the
precedent this cycle's own Phase-2 Red Team audit applied to VISION's
Phase-2 finding (no entry existed at all) — correctly, and I do not
disturb that ruling; it governed a fact pattern (total absence of any
registration) genuinely different from what is at issue now (an entry
that exists, built to the letter of what it was asked to check, but
scoped short of the whole picture).

**Precedent B — Iteration 39's second firing:** a textually distinct
sub-defect (`candidate_globs` under-scoping, not `required_sites`
under-scoping) in the SAME already-hardened entry, found at Phase 5,
still fired — on three grounds this audit re-derives directly from the
LOGBOOK/PLAN.md record rather than taking on faith: (1) the tripwire's
own temporal test ("discovered at Iteration 39 or later") is a floor,
not a per-iteration or per-gap-shape ceiling; (2) a textually distinct
gap-shape in the same entry is not "the same argument re-offered," which
is the only thing a "no further deliberation" clause forecloses; (3) a
same-shift fix represented as closing an entry's coverage, shown before
the cycle even closed not to have fully closed it, is exactly the fact
pattern that forecloses a "still just ordinary Phase-5 feedback" reading.

### 3.4 Why this cycle's OWN tripwire, not analogy to either precedent,
is the actually load-bearing text

This is the step VISION's own §4 does not take, and it is the reason
this audit reaches a different conclusion. **This cycle's own Phase-2
Red Team audit did not merely apply Precedent A by default — it wrote a
NEW, self-declared tripwire, deliberately, in the act of ruling that
VISION's Phase-2 finding does not fire:**

> "A forward tripwire is set here... if either registry gap... is NOT
> added at Phase 3, **or if a materially similar gap in either of THESE
> specific new entries is found again at Phase 5 or any later iteration,
> that DOES fire Checkpoint criterion 4 without further deliberation** —
> the same self-catch-grace mechanism this program has now applied
> consistently at Iterations 23, 37, and 38."
> — `phase2_redteam_audit.md` §3, accepted by the Director "without
> override," `phase3_synthesis.md` §2.

Three textual facts settle this, checked directly against the quoted
text, not inferred:

1. **The tripwire is a disjunction, and its second disjunct anticipates
   exactly this scenario.** "NOT added at Phase 3" (disjunct one — did
   not happen, both `caveat_lint` entries and the `numeric_lint` entry
   were added) is explicitly paired with an alternative: "a materially
   similar gap... found again" (disjunct two). A disjunction whose
   second branch could never independently trigger — because the first
   branch's negation (entries exist) would always make it vacuous — is
   not how this text reads; the second branch is written to cover
   precisely the case where the entries exist but still carry a gap of
   the same species as what VISION found at Phase 2 (the tool cannot
   verify a claim-bearing document it needs to reach). A narrow-scoped
   `site`/`required_sites` field is that species: the tool exists to
   verify a document; the document it needs to verify (`phase4_results.md`)
   is not in its reach. This is not a different kind of defect from "no
   entry exists at all" — it is the same defect, one increment less
   total than the original.
2. **The tripwire explicitly names "Phase 5" of the CURRENT cycle as a
   firing trigger — a deliberately harder line than Iteration 38's own
   tripwire, which covered only "after the fix lands" in a FUTURE
   cycle.** Iteration 38's tripwire, read and cited directly above,
   gave the ORIGINATING cycle's own Phase-5 a pass (both of Iteration
   38's own self-catches, one at Phase 2 and one at Phase 5, were
   forgiven in full, and only a THIRD instance, at Iteration 39, would
   fire). This cycle's Phase-2 Red Team, writing with that entire
   history already in front of it, chose NOT to reuse that softer
   wording — it wrote "at Phase 5 or any later iteration" into the SAME
   sentence, for the SAME originating cycle. That is not an accident of
   phrasing this audit is entitled to read past; it is the one place
   this cycle's own ruling deliberately diverges from the precedent it
   is otherwise following, and the divergence runs in the direction of
   MORE exposure at Phase 5, not less. Applying Precedent A's softer
   "whole originating cycle gets grace" rule here would overwrite the
   harder rule this cycle's own Red Team actually wrote, not merely
   interpret it.
3. **"No further deliberation required," read against Iteration 39's
   own application of the identical phrase, means the textual match is
   dispositive, not merely relevant.** Iteration 39's second firing did
   not ask whether the `candidate_globs` gap was IMPORTANT, whether it
   hid a currently-consequential defect, or whether a reasonable Red
   Team on first principles would have called it drift — it asked only
   whether the fact pattern named in the tripwire's own text had
   occurred, and ruled it had. This audit applies the same discipline
   here: VISION's finding 2 (and this audit's own §3.2 finding, a
   second instance of the identical shape) IS a materially similar gap,
   in one of the three specific new entries this cycle's Phase-2 audit
   named, found at this cycle's own Phase 5. The tripwire's own text
   does not ask, and this audit does not need to independently argue,
   whether the underlying content is currently correct (it is — see
   §3.5) or whether a hypothetical future violation would matter (it
   might not, given how comfortably every margin clears its bar). That
   is precisely the kind of "is this really drift, on the merits"
   re-litigation the "no further deliberation" clause exists to
   foreclose.

### 3.5 What this ruling is NOT saying, stated as precisely as
Iteration 39's own second firing stated it

This is a lighter-weight instance than either Iteration-39 firing, and
this audit says so plainly rather than inflating it: unlike Iteration
39's second firing, NEITHER gap found this cycle (VISION's finding 2,
this audit's own §3.2 finding) currently conceals a live violation of
the RULE those specific entries exist to enforce — `phase4_results.md`
genuinely carries both the NETD disclaimer (§3.2, confirmed) and the
correct bracket structure at both TD-3 and TD-5 (VISION's own §1.1/§2,
independently re-confirmed). The one live, if tiny, defect this cycle's
own record does carry (VISION's finding 3, §4 below) is not something
either narrow-scoped entry was ever built to catch even at full width
(a `derivation_consistency`/disclaimer-propagation check is not a
numeric-band-accuracy check) — so this is not, and this audit does not
rule it, Iteration-39-second-firing-shaped in the fullest sense (an
already-hardened tripwire failing to discover an ALREADY-VIOLATING
file). It fires on the narrower, but textually unambiguous, ground that
this cycle's own self-declared, Director-accepted tripwire names this
exact fact pattern — a materially similar coverage gap in one of its
three named entries, found at Phase 5 — as sufficient on its own,
without further deliberation. That is a fact about what this cycle
itself pre-committed to, independent of how consequential the
underlying gap turns out to be.

### 3.6 Disposition

Per unbroken precedent (Iterations 17/36/37/38/39×2), this is a
**notification, not a pause**. The Tier-1 mandatory fixes below (§5)
close both the specific site-scoping gaps (VISION's finding 2, this
audit's §3.2 finding) and the live numeric-accuracy defect (VISION's
finding 3) same-shift; nothing here blocks Iteration 41's unblocked
proposal work. Per this program's own established pattern of adopting
Red Team's audit over the raw seat count when the audit turns on a
process-completeness ground none of the blind seats were positioned to
see (Iterations 10, 12, 32, 36, 37, 39), **this overrides VISION's own
§4 conclusion on its own finding**, and overrides the raw 6-0 PROMISING
seat count — see §7.

---

## 4. VISION's findings 1 and 3 — independently re-verified, mandatory
same-shift fixes, do not independently raise the Checkpoint-4 question
beyond §3

### 4.1 Finding 1 — the Summary table / Bottom-line paragraph carry no
NETD/human-eye disclaimer

Independently re-grepped `phase4_results.md` lines 196–220 for "NETD,"
"human-eye," "constraint-3," and every paraphrase used elsewhere in the
same document: **zero hits.** Every individual TD-3/4/5 section above it
carries the disclaimer immediately above its own `**Result:**` line —
confirmed directly. **Confirmed exactly as VISION states.** This is the
mandatory-fix docket's own intent (Red Team's Phase-2 attack 1: "every
claim needs its own disclaimer AT THE POINT OF THE CLAIM") reaching a
document section (the Summary table, the single most-quotable location
in the whole record) that did not exist when the docket's own text was
written ("TD-3/TD-4/TD-5's own table rows"). Correctly ruled by VISION
as the Iteration-38 shape, not independently Checkpoint-4-shaped — I
concur, this is ordinary Phase-5 feedback catching a scope the Phase-3
docket could not yet see, distinct from §3's ruling (which turns on a
gap in a *registry entry's own mechanical reach*, not a gap in a
docket's own drafted scope). **Mandatory same-shift fix, §5 item 1.**

### 4.2 Finding 3 — the Summary table's "inside band" language is not
numerically accurate for 2 of 4 sourced κ values

Independently recomputed, by direct invocation, not hand-typed (§1
above supplies the full table). Confirmed exactly:

| Row | Predicted ceiling/floor (from TD-1's predicted κ band [0.1,20]) | Found at κ=40 | Found at κ=50 |
|---|---|---|---|
| TD-3 (bench CF, rear-only) | floor 1.001301 | 1.000650 — **below floor** | 1.000520 — **below floor** |
| TD-4 (bench margin, rear-only) | ceiling 698.3617× | 698.8156× — **above ceiling** | 698.9064× — **above ceiling** |
| TD-5 (MP-5 margin, rear-only) | ceiling 1.3479× | 1.3489× — **above ceiling** | 1.3492× — **above ceiling** |

Deviations are 0.06–0.10% relative, all in the SAFE direction (less
correction needed at bench scale, more margin at witness scale — never
toward any actual falsification condition, none of which is remotely
approached). **Root cause, confirmed by direct inspection of §Section 4's
own numbers**: TD-3/4/5's predicted bands were computed by propagating
TD-1's own PREDICTED κ range [0.1, 20] through the correction formula,
correctly, since that is all Phase 3 had before Phase 4 ran — but Phase
4's own search FOUND real κ figures (40, 50 W/(m·K)) that sit above that
predicted range's own ceiling, a fact `phase4_results.md`'s own TD-1
section discloses honestly ("the derived ≈40 W/(m·K) estimate sits just
above the band's own upper edge"). That disclosed overshoot was never
propagated into the DOWNSTREAM TD-3/4/5 Summary-table claims quoting
"inside band." **Confirmed exactly as VISION states, including that no
verdict is wrong and the direction is uniformly safe.** This is a real,
if small, defect in the committed record's own prose — a live, unfixed
inaccuracy sitting in `phase4_results.md` right now, unlike finding 1
(an omission) — and is the strongest single piece of evidence in this
review packet that a wider-scoped `numeric_lint`/`caveat_lint` reach
would have caught something real, not merely closed a hypothetical gap.
**Mandatory same-shift fix, §5 item 2.**

---

## 5. Mandatory-fix docket — same-shift, before this cycle's LOGBOOK.md/
PLAN.md/SESSION_LOG.md entries are written

All items below are cheap, zero-FDTD, and — per this program's own
unbroken precedent at every prior Checkpoint-4 firing (17, 36, 37, both
39 firings) — landing them same-shift is what converts this cycle's
verdict from PARTIAL to "PARTIAL, provisional-to-PROMISING," not a
separate future obligation.

1. **Correct `phase4_results.md`'s Summary table and Bottom-line
   paragraph's numeric claims** (VISION's finding 3, §4.2 above): change
   "inside band" language for TD-3, TD-4, and TD-5 to disclose that 2 of
   4 sourced κ values (40.0, 50.0 W/(m·K)) fall slightly outside the
   PREDICTED band (computed only over TD-1's own predicted κ range,
   [0.1,20]) — 0.06–0.10% low for TD-3, 0.06–0.10% high for TD-4/TD-5 —
   in every case in the safe direction, with no falsification condition
   approached. State the root cause (the predicted bands were computed
   over TD-1's predicted, not found, κ range) in one sentence.
2. **Add the NETD/human-eye disclaimer, verbatim, to `phase4_results.md`'s
   Summary table (header or a footnote row) and to the Bottom-line
   paragraph's opening sentence** (VISION's finding 1, §4.1 above).
3. **Widen `lab/numeric_lint_config.json`'s `exp063-cf-bench-vs-witness-
   derivation` entry (or add a sibling entry) to also check
   `phase4_results.md`'s own `### TD-3` / `### TD-5` sections** (confirmed
   header text: `phase4_results.md:115` and `:162`) for the same
   `front-colocated` / NETD-disclaimer basis-and-requirement pair
   (VISION's finding 2, §3 above — this is what closes the Checkpoint-4
   firing). Note for whoever applies this: `lab/numeric_lint.py`'s
   `derivation_consistency` entry schema currently takes a single `site`
   path, not a list (confirmed by direct source read, `check_derivation_
   consistency`, `lab/numeric_lint.py` line 227–228) — either extend the
   schema to accept a list, or register a second, distinct entry id for
   `phase4_results.md`. Either is zero-FDTD and cheap; do not defer this
   to "whatever needs it."
4. **Widen `lab/caveat_lint_config.json`'s `exp063-thermo-disposition-
   netd-disclaimer` entry's `required_sites` to include
   `experiments/063-.../phase4_results.md`**, matching its sibling entry
   `exp063-biot-correction-machinery` (this audit's own §3.2 finding —
   not raised by any blind seat, closes the second of two narrow-scoped
   entries this cycle built).
5. **Add `NOTES.md`'s missing `Result` and `Learned` sections**
   (THERMODYNAMICS' finding, §2.4 above). THERMODYNAMICS' own proposed
   text (`phase5_review_thermodynamics.md` §2) is accurate, independently
   re-verified against this audit's own §1 numbers, and may be adopted
   verbatim or lightly edited by the Director.

**Not mandatory this shift, correctly carried to Iteration 41 (queued,
not blocking)**: the disclaimer rule's own general, program-wide
`caveat_lint_config.json` entry (Red Team's Phase-2 audit's own
non-blocking standing item, already PLAN.md-queued); the substrate-
interface / root-to-substrate contact-resistance question (MATERIALS,
§2.2); the T23 length-legitimacy resolution (EM, §2.3, and see §6's
binding forward commitment); pinning the record-blackness/Vantablack
CNT forest's own pitch/diameter and κ together (multiple seats, §6).

---

## 6. Verdict

**PARTIAL, provisional-to-PROMISING once the five-item docket above
lands and is re-verified live this same shift** — explicitly overriding
the raw 6-0 PROMISING seat count.

**Why the override, stated against this program's own precedent
distinction (the task brief's own framing, and this program's actual
record):** a self-caught, already-disclosed, non-live-violation gap
normally does NOT override a clean consensus (Iteration 38's own
precedent — two self-catches, no criterion fired, verdict PROMISING). A
live, unresolved process gap CAN override a clean seat consensus
(Iterations 36, 37, 39). This cycle sits on the harder side of that line
for a narrow but decisive reason: it is not merely "structurally similar
to" the Iteration-39 shape by loose analogy — it is a fact pattern this
cycle's OWN Phase-2 Red Team audit pre-declared, in writing, Director-
accepted without override, WOULD fire without further deliberation if
found again at this cycle's own Phase 5 (§3.4). VISION's finding 2 (and
this audit's own §3.2 finding, an identical gap in a second entry no
blind seat caught) is exactly that fact pattern. Layered onto that: this
cycle also carries a genuine, if small and safely-directioned, LIVE
numeric inaccuracy in its own already-committed `phase4_results.md`
(VISION's finding 3) — not itself sufficient to fire on its own (no
existing registry entry, even at full width, was ever built to catch a
band-accuracy defect of this shape), but exactly the kind of thing a
mechanical check with the reach VISION's finding 2 says is missing would
have had a chance to catch, and didn't. Both are real, both are cheap
to close, and per this program's own unbroken practice, closing them
same-shift is what earns the "provisional-to-PROMISING" qualifier
rather than a bare PARTIAL — the physics itself (TD-1 through TD-5, all
five falsifiable predictions, independently re-derived FIVE times over
in this record with no defect found) has never been in question.

**What is NOT true, and this verdict does not claim**: this is not a
finding that exp-063's science is wrong, incomplete, or overclaimed —
every seat, and this audit, independently confirms the correct material's
κ does license the lumped assumption, decisively, across every real
figure this cycle sourced. The override is entirely a process-
completeness finding about this cycle's own registry-building discipline,
identical in kind (though lighter in weight) to every prior Checkpoint-4
firing this program has recorded.

---

## 7. Checkpoint criteria — explicit ruling, all five

1. **A configuration passes ALL constraint metrics.** Does NOT fire —
   zero constraint-1/2/3/4 metric is scored this cycle by design ("T1
   escape route: N/A"), confirmed true on inspection by every seat and
   this audit; Red Team's own Phase-2 attack 7 (the TD-5 "Checkpoint-1/2-
   adjacent" over-reach) was correctly caught and fixed before this cycle
   even ran Phase 4 — verified still correctly relabeled in the shipped
   `NOTES.md`.
2. **A proven boundary: a constraint subset shown jointly unsatisfiable
   within a whole mechanism class, gates clean.** Does NOT fire — this
   cycle proves no mechanism-class boundary; it is an instrument/
   model-fidelity correction to an already-issued realizability-adjacent
   disposition, and (per §3–6 above) does not gate fully clean this
   cycle regardless.
3. **A synthesis requires engine physics beyond the validated bench
   classes.** Does NOT fire — zero FDTD anywhere in this cycle; the only
   `lab/` file touched is `thermo_sidecar.py`, a non-FDTD analytic
   module, confirmed by direct inspection.
4. **Program-integrity drift (unfalsifiable claims, a constraint quietly
   dropped — especially #3).** **FIRES** — see §3 in full. Not on
   unfalsifiable claims or a dropped constraint (none exists this cycle)
   but on this cycle's own self-declared, Director-accepted forward
   tripwire, whose stated trigger condition (a materially similar gap in
   one of its three newly-registered entries, found at this cycle's own
   Phase 5) is met, independently re-verified live, twice over (VISION's
   finding 2, this audit's §3.2 finding).
5. **Two consecutive iterations with no logbook-advancing result.** Does
   NOT fire — Iteration 39 delivered a real, git-committed result
   (EM-2/3/4 CONFIRMED more decisively than predicted, the `n_eff`
   primary-source pin), and this cycle, once the mandatory-fix docket
   lands, does too.

---

## 8. Ranked top-3 (plus carried items) for Iteration 41

Reconciling all six seats' own picks: EM, THERMODYNAMICS, QUANTUM, and
VISION independently name the T23 length-legitimacy question #1 or #2;
MATERIALS raises the substrate-contact-resistance question (new this
cycle, sharpened by query 10); PHOTONICS raises the optical/thermal
material-provenance mismatch (also new this cycle). This audit's own
ranking, and the reasoning for placing the four-seat convergence pick
first:

**1. Resolve T23's witness-scale length-legitimacy question — with a
binding forward commitment, not another disclosure sentence.** Deferred
at Iteration 38 (THERMO), Iteration 39 (EM/Red Team), and again this
cycle (Iteration 40, mandatory fix 6, disclosure only) — three
consecutive cycles against an already-decided rule (`gas_conduction_
h_eff`'s own docstring, closed by argument at Iteration 23) and an
already-identified violation (`L=τ_true/α` is, on that rule's own plain
text, unambiguously an "optical/extinction-derived length"). EM's own
Phase-5 review (§2.3 above) argues this recurrence pattern — not this
cycle's own numeric luck — should drive Iteration 41's priorities, and
explicitly analogizes it to this program's self-catch-grace mechanism.
**This audit adopts EM's recommendation as a binding forward commitment,
not merely a ranked pick**: if this specific question (is `L=τ_true/α`,
or any future reuse of an optical-extinction-derived length in a
Fourier-conduction-path role, licensed) is deferred again past Iteration
41 without either (a) a real geometric length sourced for the actual
candidate class, or (b) `gas_conduction_h_eff`/`front_surface_conduction_
correction` gaining an enforced `length_provenance` argument that raises
or hard-flags the forbidden case, that FOURTH deferral is to be treated
as a program-integrity finding for Red Team's own ruling at Iteration
42 — the same disposition this program gave the `exp061-t18-
evidentiary-tier-propagation` lineage after ITS second self-catch.
Ranked first because it is now a process-integrity question independent
of physics stakes, and because resolving it costs nothing against any
currently-issued verdict while a later, inconvenient resolution would.

**2. Source, or at minimum formally model as a third disclosed scenario,
the CNT-forest root-to-substrate thermal contact resistance
(MATERIALS' new finding, §2.2 above).** A dedicated 3–5 query dispatch
plus a new `thermo_sidecar.py` function (a `bonded_substrate_conduction_
correction`, gated by an `R_contact→0 ⇒ CF→(bracket B)` identity limit,
per MATERIALS' own proposal) would convert this cycle's flagged
mechanism into a scored, falsifiable prediction — directly relevant
given TD-5's own thinnest-in-program-history 7.8× headroom on κ_solid
alone, independently re-confirmed by this audit.

**3. Pin the record-blackness/Vantablack-class CNT forest's own
parameters — pitch/diameter (Iteration 39's still-open #1 item) AND
through-thickness thermal conductivity (PHOTONICS' new finding, §2.1
above) — together, in one dedicated query set.** This closes the
standing near-field-coupling question and, independently, removes the
optical/thermal material-provenance mismatch PHOTONICS identifies this
cycle: both `α_true`/`n_eff` and `κ_solid` would then be sourced from the
SAME specific geometry class for the first time, rather than three
adjacent-but-unconfirmed comparator classes for the thermal side alone.
Query 8's own honest null this cycle (the already-pinned *Carbon* 2018
paper reports geometry but not a thermal figure) and MATERIALS' own
flagged ambiguity (whether that paper's "widths 80–350nm" names pitch or
an imprint-pattern feature size) make this a natural, low-cost single
follow-up rather than two separate searches.

**Carried, lower priority, not re-ranked**: QUANTUM's own low-urgency
flag (a non-thermalized-energy re-emission channel, one-sided-safe, not
urgent for the current candidate identity); the disclaimer rule's own
general `caveat_lint_config.json` registry entry (non-blocking, PLAN.md-
queued); CNT-forest ρ/C_p sourcing (Idealization 2/6, explicitly
scoped out this cycle).

---

## 9. Ruled-out registry check (R1–R5, T1–T26)

No re-proposal found, checked directly against the full registry, not
on any seat's summary. R1–R5 are structurally inapplicable — this cycle
proposes no mechanism, scores no constraint-1/2/3/4 metric, produces no
FDTD result, and no hand-typed "precisely recomputed" figure (every
number in this record, including every figure in this audit's own §1,
traces to direct invocation of `lab/thermo_sidecar.py`, reproduced by
trust-suite stage 23 as a permanent regression anchor). Of the live
threads, this cycle correctly extends T22 (the `Bi=k_air/k_solid`
identity, reused unchanged) and T23 (the `h_eff` length-scale licensing
question, correctly identified as still-open rather than silently
resolved, now the subject of this audit's own §6 forward commitment) —
neither is re-litigated as settled beyond what it already established.
T5 (the thermo ledger) is correctly extended with the program's first
sourced `κ_solid`. No conflation with T9's own generation-side ledger
beyond what PHOTONICS correctly disclosed as bench-scale-specific and
numerically inert. No thread in T1–T26 makes any prior claim about
CNT-forest through-thickness conductivity, Biot boundary conditions, or
front-surface conduction correction — this is new ground for the
program's record, not a restatement of anything already closed.

---

## Summary for the Director

| Item | Finding |
|---|---|
| Physics (TD-1 through TD-5) | Sound, independently re-derived five times over, no defect found anywhere |
| Six seats' own claims | All independently re-verified as stated (§2) |
| VISION finding 1 (Summary/Bottom-line disclaimer) | Confirmed; mandatory same-shift fix; Iteration-38-shaped, does not independently fire |
| VISION finding 2 (`numeric_lint` site scoping) | Confirmed; **FIRES Checkpoint criterion 4**, on this cycle's own self-declared, Director-accepted forward tripwire (§3) — the one point this audit overrides all six Phase-5 seats |
| This audit's own new finding (§3.2) | A second, identical scoping gap in `exp063-thermo-disposition-netd-disclaimer`, not caught by any blind seat — reinforces §3's ruling |
| VISION finding 3 (Summary-table numeric drift) | Confirmed; small (0.06–0.10%), safe-directioned, no verdict wrong; mandatory same-shift fix; strongest evidence a wider registry reach would have caught something real |
| THERMODYNAMICS' finding (NOTES.md Result/Learned gap) | Confirmed; mandatory same-shift fix; not itself Checkpoint-4-shaped |
| MATERIALS' new finding (substrate-contact-resistance) | Confirmed, real, unscored; ranked #2 for Iteration 41 |
| PHOTONICS' new finding (optical/thermal provenance mismatch) | Confirmed, real, unscored; folds into ranked #3 for Iteration 41 |
| EM's forcing-mechanism argument (T23, three deferrals) | Adopted as a binding forward commitment, ranked #1 for Iteration 41 |
| Verdict | **PARTIAL, provisional-to-PROMISING once the five-item mandatory-fix docket (§5) lands and is re-verified live this same shift** — overriding the raw 6-0 PROMISING seat count |
| Checkpoint criteria | 1/2/3/5 do not fire; **4 FIRES** (notification, not a pause) |
