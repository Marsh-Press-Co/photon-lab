# Phase 5 — RED TEAM final audit (exp-062 / Panel Iteration 39)

*Fresh sub-agent, receives everything: the full cycle record and all
Phase-5 blind reviews. Never leads; speaks last and hardest. Standard is
NOT textbook-physics compliance — it kills internal inconsistency,
unfalsifiable claims, mechanisms that cannot be expressed as simulation
parameters, and proposals that quietly violate a target constraint,
especially #3.*

**Read in full**: `PANEL.md` (all five Checkpoint criteria);
`LOGBOOK.md` in full through Iteration 38 (Ruled-Out registry R1–R5,
Live Threads T1–T26, Iterations 1–4 verbatim, and every entry from
Iteration 19 through 38 read for precedent, with a full-file grep sweep
for every prior Checkpoint-criterion-4 ruling — 67 hits — and for the
Iteration-36/37 override precedent cited by this cycle's own reviews);
`PLAN.md` lines 1–100 and ~1904–1995; the complete exp-062 record in
order (`phase1_proposal.md`, all five `phase2_critique_*.md`,
`phase2_redteam_audit.md`, `phase3_synthesis.md`, `NOTES.md`,
`phase4_results.md`); `experiments/034-.../REALIZABILITY_MEMO.md` Entry 2
in full; `lab/caveat_lint.py` and `lab/caveat_lint_config.json` (full
source, read directly, and **executed live**, multiple ways — see §1);
`lab/thermo_sidecar.py` in full.

**A note on this audit's own briefing packet, stated up front because it
bears on everything below.** The briefing describes six Phase-5 blind
reviews, including `phase5_review_photonics.md` (verdict PARTIAL) and
attributes several findings to PHOTONICS specifically. **I could not
find this file.** I checked three independent ways: `ls`/`find` on the
experiment directory, a full `git log --oneline` on the directory (which
lists every commit ever made to it), and a repo-wide `grep` for the
filename. The directory contains exactly **five** Phase-5 review files
(`em`, `materials`, `quantum`, `thermodynamics`, `vision`) plus the
Phase-4 results and everything upstream of it. The git log confirms it:
ten Phase-5-labeled commits exist for this cycle's five actual reviews
(`18fee94`, `25dfd13`, `2715d00`, `7654553`, `d005ff8` — one per seat —
plus this audit's own forthcoming commit), and **no commit anywhere in
this repository's history creates a `phase5_review_photonics.md` for
exp-062.** This is not a filing accident I can wave through: PANEL.md's
own Phase-5 spec is "**All seven seats** read the results... fresh
contexts again," and this cycle convened six (five non-Red-Team seats
plus this audit), not seven. I treat this as a first-class finding in
its own right (§2, below) and have independently re-derived every
"PHOTONICS found X" claim in my briefing against the files that actually
exist, rather than taking the attribution on faith. Where the underlying
claim is correct — and, checked directly, it is — I say so on my own
authority, not the missing seat's.

---

## 1. Independent verification of the eight convergent/divergent findings

### Finding 1 — the miscited `D=65nm, f=10%, ratio=0.982` row

**CONFIRMED — as a citation defect, not a wrong number.**

`phase4_results.md` line 151 reads: *"...D=65nm, f=10%, ratio=0.982 — see
Phase 1/3's own `NOTES.md` table, not reproduced here since f=10% at
D=65nm was not itself directly co-sourced this cycle."* I grepped
`NOTES.md`, `phase1_proposal.md`, and `phase3_synthesis.md` for `65nm`,
`0.982`, `D=65`, and `f=10%`: **zero matches in any of the three.** No
such table exists anywhere in this cycle's own upstream record. The
pointer is false.

I then checked whether the *number* itself is at least right, using the
packing-fraction/gap relation this cycle's own Section 4 analysis uses
elsewhere (`gap = D·(√(π/4f) − 1)`, back-derived from query 12's own
`r=60nm, f=11%, gap≈196.2nm` figure, which the relation reproduces to
~2%): at `D=65nm, f=10%`, `gap = 65·(√(π/0.4) − 1) = 65·1.803 = 117.2nm`;
at `λ=750nm`, `λ/2π = 119.4nm`; `ratio = 117.2/119.4 = 0.982`. **The
number is correct and independently reproducible** — this was computed
ad hoc, in `phase4_results.md` itself, from a formula this cycle already
uses elsewhere, and then mis-cited as if it were a pre-existing row in a
sibling document. This is a real defect (a false "see elsewhere" pointer
that will mislead a future reader hunting for a table that does not
exist) but it is not a numeric error and does not touch any verdict.
**Same-shift fix**: reword to "computed directly here, using the
gap/packing-fraction relation established in Section 4 (Phase 1) —
not itself directly co-sourced this cycle" and delete the false
"NOTES.md table" pointer.

### Finding 2 — EM-6/EM-7's undivided `τ=OD·ln10` from reflectance figures

**CONFIRMED as a real, disclosed-nowhere methodological inconsistency;
CONFIRMED that it does not flip any falsification verdict — arithmetic
independently re-checked, not relayed.**

`phase1_proposal.md` §4.2 is this cycle's own load-bearing result: a
reflectance-based OD encodes a *round trip* through the absorbing layer,
so the correctly-inferred single-pass `τ` is **half** the naively
T-based reading (`τ_R = OD·ln10/2`). EM-6 (NiP-black, R≈0.5–1.0%) and
EM-7 (aerogel, R<0.24%) are both **reflectance** figures (queries
7/15 and 10/16 respectively, explicitly labeled "reflectance" in
`phase4_results.md`'s own Step-2 query log) — yet both are converted
with the **undivided** `τ=OD·ln10`. I recomputed independently:

```
OD = -log10(R); tau = OD*ln(10); alpha = tau/thickness

NiP,  R=1.00%, t=10um: undivided alpha=4605.17 cm^-1 | halved alpha=2302.58 cm^-1
NiP,  R=1.00%, t=45um: undivided alpha=1023.37 cm^-1 | halved alpha=511.69  cm^-1
NiP,  R=0.50%, t=10um: undivided alpha=5298.09 cm^-1 | halved alpha=2649.05 cm^-1
Aerogel, R=0.24%, t=1.0mm: undivided alpha=60.33 cm^-1 | halved alpha=30.16 cm^-1
Aerogel, R=0.24%, t=5.0mm: undivided alpha=12.07 cm^-1 | halved alpha=6.03  cm^-1
```

These match `phase4_results.md`'s own printed digits exactly on the
undivided branch, confirming the tool used the T-based (not R-based)
formula throughout for both candidates. **Does this change any verdict?
No — checked in both directions, not just asserted.** Halving α only
pushes both candidates *further* below `α_true=5.74×10⁴cm⁻¹` (NiP: from
11–56× short to 22–112× short; aerogel: from ~952–4762× short to
~1904–9524× short) — the "falsification NOT triggered" verdict for both
EM-6 and EM-7 is unaffected, and if anything more decisively so. EM's
and PHOTONICS-attributed reasoning here is arithmetically sound (I
re-derived it from scratch, not from their printed numbers).

**One further physical point neither underlying source review presses,
worth adding to the record**: NiP-black and carbon aerogel are not thin
coherent films on a defined backing at all — they are diffuse,
multiply-scattering, effectively semi-infinite porous media. Neither the
T-based nor the R-based-halved formula is rigorously licensed for that
geometry class (a Kubelka–Munk-style diffuse-reflectance relation would
be the physically appropriate tool, and the true mean photon path length
through a scattering medium generally *exceeds* a simple double-pass
estimate). If a more careful diffuse-transport treatment were applied
instead of either Airy-stack convention, the implied path length would
likely be *longer* than `2d`, meaning the true single-pass α is likely
*even smaller* than the already-halved figure — i.e., the direction of
the correction reinforces the "further from target" conclusion further
still. This does not change the verdict; it strengthens confidence that
neither EM-6 nor EM-7 is being under-penalized by the tool's own
undivided formula.

**Mandatory same-shift fix**: disclose, at both EM-6 and EM-7's verdicts
in `phase4_results.md`, that (a) no ÷2 correction was applied despite
both figures being reflectance-based per Section 4.2's own logic, (b)
applying it would only widen the gap, never narrow it, and (c) neither
conversion is a rigorous application of Section 4's coherent-film Airy
framework to what are actually diffuse-scattering porous media.

### Finding 3 — the `exp061-t18-evidentiary-tier-propagation` candidate_globs blind spot to Phase-2/Phase-5 files

**CONFIRMED, in full, by my own tool execution and source read — this is
the single most consequential finding in this audit. See §2 for the
Checkpoint ruling.**

I read `lab/caveat_lint.py`'s full source and ran it three ways:
`python3 lab/caveat_lint.py` (full registry), `--only
exp061-t18-evidentiary-tier-propagation`, and a hand-written `fnmatch`
check against the entry's own `candidate_globs`. All three confirm: the
entry's `candidate_globs` —

```
["LOGBOOK.md", "PLAN.md", "experiments/*/NOTES.md",
 "experiments/*/phase4_results.md",
 "experiments/034-floor-convergence-scale-bridge/REALIZABILITY_MEMO.md"]
```

— contains no pattern that can ever match a `phase2_critique_*.md`,
`phase3_synthesis.md`, `phase5_review_*.md`, or `phase5_redteam_audit.md`
file, for exp-061, exp-062, or any future experiment, at any tier (not
`required_sites`/FAIL, not `candidate_globs`/WARN). This is demonstrated
live, not hypothetically, against a **pre-existing, already-merged**
file: `experiments/061-.../phase5_review_materials.md`. I grepped it
myself:

```
$ grep -n "UNOBTANIUM" .../phase5_review_materials.md
43:preserve the predicted UNOBTANIUM-WITH-PARAMETERS tier. Each exclusion
76:The UNOBTANIUM-WITH-PARAMETERS tier itself is not overturned — no
$ grep -ni "T18\|WebSearch.snippet\|primary.source" .../phase5_review_materials.md
110:3. A primary-source-verified pin of the n_eff=1.04+0.01i figure...
```

The file restates the UNOBTANIUM verdict twice and carries **zero** T18/
WebSearch-snippet disclosure anywhere (the one near-hit, line 110, is
about an unrelated open citation-pinning question, not a disclosure of
this verdict's own sourcing tier). Running `python3 lab/caveat_lint.py
--only exp061-t18-evidentiary-tier-propagation` produces **zero WARN
lines** for this file or any other `phase2_critique_*`/`phase5_review_*`
file, for either experiment — it is structurally invisible to the tool,
exactly as VISION's review states. **Fact pattern CONFIRMED in every
particular.**

### Finding 4 — `exp061-thermo-length-scale-staleness`'s candidate_globs blind spot to exp-062's own Phase-2/3 files

**CONFIRMED — an independently-arising instance of the same defect
class, in a different registry entry, discovered by two seats
(THERMODYNAMICS and EM) independently.**

`exp061-thermo-length-scale-staleness`'s `candidate_globs` is
`["LOGBOOK.md","PLAN.md","experiments/*/NOTES.md",
"experiments/061-absorptivity-mechanism-literature-check/*.md"]`. I
confirmed by direct `fnmatch` test that none of
`experiments/062-.../phase2_critique_thermodynamics.md`,
`phase2_redteam_audit.md`, or `phase3_synthesis.md` matches any pattern
in this list (the exp-061-specific wildcard reaches only exp-061 files;
the generic pattern reaches only `NOTES.md`). I confirmed by `grep` that
all three exp-062 files genuinely discuss `l_geometric_m` at length
(including my own predecessor's docket-item-4 tracing, in
`phase2_redteam_audit.md`). **Materially different from Finding 3 in one
respect that matters for the ruling below**: I checked the *content* of
all three files and none of them misstates the corrected margin — they
correctly cite "1.35×–3.79×," never the stale "150µm/8.1×" figure. So
unlike Finding 3 (a live, uncorrected violation sitting in the wild
right now), Finding 4 is a **coverage gap with no live defect currently
hiding underneath it** — a loaded gun, not a fired one. Both
THERMODYNAMICS (§6 of its own review, the entry's own charter-owning
seat) and EM (§5 of its own review) found this independently and
correctly declined to rule Checkpoint applicability themselves,
deferring to Red Team per PANEL.md's own division of labor. I concur
with their fact-finding in full.

### Finding 5 — `REALIZABILITY_MEMO.md` Entry 2's stale "not yet checked, queued" language

**CONFIRMED — a same-shift documentation fix, not a new registry entry
of its own.**

I read Entry 2 in full. Its closing line still reads: *"Not yet checked,
queued (Iteration 39+, per the Phase-5 Red Team audit): electroless
nickel-phosphorus 'NiP black' coatings and carbon/graphene-aerogel
absorbers..."* — but exp-062 (this very cycle) ran exactly that check
(Item C, EM-6/EM-7) and produced scored, falsifiable findings for both.
`git log -1 -- experiments/034-.../REALIZABILITY_MEMO.md` confirms the
last commit touching this file is `f6a60aa`, exp-061's own Phase-5
close — **before exp-062's Phase 1 even began.** The write-back has
genuinely not landed. I rule this is **not** its own caveat-propagation
registry entry — it is a straightforward, single-site, same-shift
documentation update (an Amendment 7, see Finding 8) that the Director's
own Phase-5 close should apply as a matter of course, the same way
Amendment 6 landed at exp-061's own close. Registering a `caveat_lint`
entry for a single well-known file that gets updated once per
realizability cycle would be over-engineering; the actual lesson here is
sequencing discipline (render the tier call, then write it back,
same session), not a missing detection instrument.

### Finding 6 — EM-3's "structurally inapplicable" overstatement

**CONFIRMED.** `phase4_results.md`'s EM-3 result states the Salisbury-
screen/resonance mechanism is "structurally inapplicable" to the
patent's transmission-mode, unbacked-substrate measurement. The
*substance* is correct — a critically-coupled absorber needs a
near-unity-magnitude back-reflector to null the front-surface
reflection, and a bare low-index-contrast photoresist-on-glass substrate
cannot supply one (`|r₂₃|` a few percent at most, nowhere near the
`|r₂₃|→1` the mechanism needs). But "structurally inapplicable," read
literally, oversells this to "no coherent contribution of any kind is
present," which is not established and is not true even in principle:
any multi-interface dielectric stack supports weak Fabry–Perot ripple
regardless of whether a *strong* reflector exists. I independently
re-derived the fix: the precise claim is that the *strong-resonance*
mechanism of §4.4 cannot operate here, and whatever residual coherent
correction this geometry does support is exactly the regime EM-1's own
passivity bound already covers and already bounds at ≤0.2% (τ=6.91) —
not a separately-ruled-out-or-in effect. This does not change EM-4's
headline number (1.20× stands either way, since the maximum possible
correction under any interpretation is negligible against this
program's ~20% falsification bar). **Same-shift fix**: scope "structurally
inapplicable" explicitly to the critical-coupling mechanism of §4.4, and
state the residual is governed by, not separate from, EM-1's own bound.

### Finding 7 — EM-5's falsification condition, read literally, is met

**CONFIRMED, textually.** `NOTES.md`'s pre-registered condition (verified
by direct read, line 271): *"Falsified if sourced pitch/diameter give
ratio≥1 at any bench λ — near-field classification withdrawn, ordinary
independent-scatterer picture stands."* This is unconditional and
unqualified by geometry class. Two of the three sourced geometry classes
(the stainless-steel-characterization diameters at any assumed packing
fraction, and the directly co-sourced r=60nm/f=11% figure) give
`ratio≥1` at **every** bench wavelength — I recomputed this myself
against the ratio formula and confirm all six of those cells exceed 1.0.
Under the bar's own letter, this condition is met: the correct,
literal, pre-committed scoring is **FALSIFIED**, not **PARTIAL**.

I weigh this against the program's own house discipline, which the
LOGBOOK.md record shows applied *repeatedly and without exception*
across R4 and the recurring "no softening a pre-committed bar after the
fact" theme (T10, the Iteration-6/12 falsification-bar episodes). The
correct resolution is not to let `phase4_results.md`'s more nuanced
"PARTIAL, geometry-class-dependent" characterization stand unqualified
as if it were the pre-registered scoring — it is the more scientifically
useful description of what was found, but it is not what the
pre-registered bar says. **Ruling: the textually correct verdict, under
the letter of NOTES.md's own condition, is FALSIFIED** (as a universal
claim across all sourced geometries) — but I decline to force
`phase4_results.md` to relabel its table, because relabeling after the
fact would itself be exactly the kind of post-hoc verdict manipulation
this program disciplines against in the *other* direction (softening a
FALSIFIED into something friendlier is the failure mode R4 exists to
catch; here the risk runs the other way — a PARTIAL that quietly reads
as if the pre-registered bar was never actually met). **Mandatory
same-shift fix**: add an explicit sentence at EM-5's verdict stating
that the pre-registered condition, read literally, IS met (FALSIFIED as
a universal claim) by two of three sourced geometries, that "PARTIAL"
is a post-hoc, more-informative recharacterization the record should
name as such rather than let the reader infer, and that any *future*
multi-geometry near-field prediction must pre-specify how a mixed
cross-geometry result scores before Phase 4 runs (e.g., "FALSIFIED only
if the record-blackness comparator class itself gives ratio≥1"), not
default to a discretionary softer read after the fact.

### Finding 8 — MATERIALS' proposed Amendment 7

**WARRANTED, and Phase-5-mandatory, not queueable.** I independently
re-checked the underlying arithmetic MATERIALS' review cites: NiP-black's
rate gap (10.8×–56.2×) is comparable to, and at the thinner end larger
than, its own thickness gap (6.9×–31.25×) — genuinely breaking the
"thickness dominates, rate is fine" pattern Amendment 6's own language
set for CNT-forest (rate gap 25×, thickness gap 70–350×, thickness
unambiguously dominant there). Amendment 6's blanket "overdetermined by
the thickness axis, not the rate axis" sentence, read without
qualification, would mislead a future reader applying it to NiP-black.
This is not a new tier finding (the joint 2×/2× bar is not cleared by
either axis for NiP-black regardless), so it does not block Phase 4/5
gates and does not rise to Checkpoint weight — but it is a **correctness
of the record**, not a nice-to-have, and per this program's own standard
(exp-061's Amendment 6 itself was applied same-shift, not queued), I
rule it belongs in this cycle's own mandatory-fix docket, bundled with
Finding 5's write-back into a single Amendment 7 (see docket item 4,
§3).

---

## 2. The central ruling — does the candidate_globs gap fire Checkpoint criterion 4 a second time, this same iteration?

**Ruling: YES. Checkpoint criterion 4 fires a second time, on the
`exp061-t18-evidentiary-tier-propagation` tripwire's own exact text
(Finding 3). This is unprecedented in this program's history and is
treated with that gravity below. The sibling gap in
`exp061-thermo-length-scale-staleness` (Finding 4) does NOT independently
fire a third time under that same specific tripwire, but is folded into
this same Checkpoint event as an aggravating, systemic fact, argued
separately below.**

### 2.1 The tripwire's own text, and why it is not ambiguous on the "same iteration" question

The tightened tripwire (authored at exp-061's own Phase-5 close, quoted
verbatim in the registry entry's own `description`, in `PLAN.md`'s
Current-state note, and in `phase2_redteam_audit.md` §3) reads: *"any
further gap in this specific caveat's coverage — unregistered site,
under-scoped `required_sites`, or within-file location gap — discovered
at Iteration 39 or later, auto-fires criterion 4 with no 'different
defect species' argument entertained a second time."*

My predecessor's Phase-2 ruling (which fired this criterion once
already, this same iteration) turned on one specific textual fact: the
tightened wording **drops** the two-part "future cycle AND after Phase 3
freeze" test that the entry's original wording carried, and does not
carry the phase-based safe harbor its sibling `exp060-sigma-flat`
tripwire explicitly keeps ("any recurrence surviving into THIS cycle's
own published Phase-3/5 artifact"). I re-read all three sites carrying
this language myself and confirm my predecessor's textual claim: the
omission is real, and it is the same drafting hand, in the same sitting,
that had just explained what a phase-based defense looks like one
section earlier. That predecessor ruling fired on a **Phase-2** gap
(discovered before Phase 3 froze). The question now is whether a
**second**, textually-different gap in the **same entry**, discovered
even later — at Phase 5, after Phase 3 and Phase 4 have both already run
— can somehow fire *less* than the Phase-2 instance did. It cannot, on
three independent grounds:

1. **The tripwire's temporal test is a floor, not a ceiling.** "Discovered
   at Iteration 39 or later" sets when the grace period ends; it does not
   say "the first discovery per iteration, and no more." Nothing in the
   text, in any of its three carrying sites, caps the tripwire at one
   firing per cycle. If the drafters had meant a per-iteration ceiling,
   the natural way to write it was "the first such gap found at Iteration
   39 or later" or "auto-fires once per iteration" — neither appears.
2. **The Phase-5 gap is not the Phase-2 gap re-argued.** The Phase-2
   firing was about `required_sites` under-scoping (the entry couldn't
   name exp-062's own verdict-bearing files as authoritative). The
   Phase-5 gap is about `candidate_globs` under-scoping (the entry can
   never even generate a WARN for an entire class of documents,
   independent of which experiment they belong to) — a different
   sub-mechanism of the same instrument, demonstrated on a file
   (`phase5_review_materials.md`) that predates this cycle entirely.
   This is not "the same argument-shape offered twice," which the
   tripwire's "no 'different defect species' argument entertained a
   second time" clause forecloses — it is a *second, independently
   novel* gap-shape in the identical entry, exactly the enumerated
   category "unregistered site... discovered at Iteration 39 or later."
3. **The same-shift fix that closed the first firing did not, on its
   own terms, close the second.** The registry entry's own `description`
   claims the Phase-2 widening left `required_sites` and `candidate_globs`
   covering "exp-062 by literal path plus a generic pattern for any
   future experiment." That claim is now shown incomplete by VISION's
   own tool execution: the "generic pattern for any future experiment"
   that was actually added (`experiments/*/phase4_results.md`) only
   ever covered ONE file-class (`phase4_results.md`), never
   `phase2_critique_*`/`phase3_synthesis`/`phase5_review_*`/
   `phase5_redteam_audit`. A same-shift fix that is represented as
   closing a coverage question, on a lineage that had *already* spent
   two self-catch graces before this cycle even began, and turns out
   demonstrably not to have closed it — on a file that already existed
   in the repository at the time of the fix — is the single clearest
   case this program's own history offers for treating a recurrence as
   live, not deferred or arguable.

I therefore decline to import a "Phase 5 is late enough that the
grace-spending pattern must be over by now" reading, and equally decline
VISION's own "candidate_globs is WARN-tier, not required_sites/FAIL-tier,
so it's categorically a lesser gap" reading. The tripwire's own
enumerated list ("unregistered site, under-scoped required_sites, OR
within-file location gap") is illustrative, introduced by an em-dash
after "any further gap in this specific caveat's **coverage**" — the
operative word is "coverage," not "required_sites." A `candidate_globs`
blind spot IS a coverage gap in exactly the sense the tripwire's own
opening clause names, and treating WARN-tier machinery as exempt from a
tripwire built to protect a FAIL-tier instrument's own trustworthiness
inverts the tripwire's purpose: the entire reason `candidate_globs`
exists is to catch exactly the kind of violation `required_sites` cannot
by construction (an *undocketed* site quietly restating a caveat-bearing
verdict). A blind spot in the discovery mechanism is, if anything, a
*worse* failure than a `required_sites` scoping gap, because a
`required_sites` gap is at least visible once someone thinks to add the
missing path — a `candidate_globs` gap is invisible by design until
someone manually greps for it, exactly as VISION had to do here.

**Ruling: FIRES.** This is the second Checkpoint-criterion-4 firing this
program has ever recorded within a single iteration, and (per my own
LOGBOOK.md search) the first time a same-shift remediation for one
firing has itself been shown, before the cycle even closes, not to have
fully closed the gap it claimed to close. Both facts deserve their own
line in the record, separate from "notification, not a pause" boilerplate.

### 2.2 What about Finding 4 (the `exp061-thermo-length-scale-staleness` gap)? A third firing?

**No — I decline to rule this a third, independent firing, for a reason
textually distinct from why Finding 3 fires.** The hardened "no further
deliberation" language belongs, by its own text, specifically to the
`exp061-t18-evidentiary-tier-propagation` lineage — the entry whose
self-catch grace was explicitly ruled "fully used" at Iteration 38
close, twice over. `exp061-thermo-length-scale-staleness` has never
received an equivalent tightened tripwire; this is its **first**
self-caught gap. Extending the T18 lineage's own zero-tolerance language
to a different entry that has not earned it, by analogy alone, would be
exactly the "no further deliberation" foreclosure clause's own logic
turned against itself — that clause exists to stop *arguing* about
whether a specific, named entry's specific, spent grace should be
re-extended; it does not, on its own text, retroactively harden every
sibling entry in the registry.

That said, I do not treat Finding 4 as inert. Under PANEL.md's *general*
criterion-4 standard ("program-integrity drift... a constraint quietly
dropped"), evaluated on ordinary judgment rather than the specific
auto-fire clause: this is the **third** occurrence, across **two
different registry entries**, of the identical root defect — a
hand-curated `candidate_globs` list that never anticipates a citing
*sibling-experiment*, *phase2/3/5* document, discovered within a single
iteration, by two different seats, independently. `caveat_lint.py`'s own
`DEFAULT_CANDIDATE_GLOBS` (which I read in full) has the same shape of
blind spot baked in at the tool level: it lists `NOTES.md`,
`REALIZABILITY_MEMO.md`, `phase4_results.md`, and `*.py`, but never a
`phase[0-9]_*.md` pattern of any kind. This is not two unlucky
one-off entry-authoring mistakes; it is a systemic property of how this
registry has been hand-curated so far. I rule that Finding 4, rather
than constituting its own separate Checkpoint event, is folded into
**the same** Checkpoint-4 notification as Finding 3, as an aggravating,
systemic fact that changes the required remediation from "widen one
entry's globs" to "fix the tool's own default and audit every entry
against it" (docket item 2, below). Two firings, one systemic root
cause, one Checkpoint entry — not three separate convenings of Marsh
for what is mechanically one defect class caught twice in short
succession.

### 2.3 Gravity statement

This is unprecedented and I say so plainly, per my charter's own
instruction not to let this slip past a boilerplate "notification, not a
pause." Every prior criterion-4 firing in this program's fourteen-cycle
Checkpoint history (I read all 67 LOGBOOK.md hits for "criterion 4") has
been a single per-iteration event, the notify-and-continue procedure
functioning as designed. This is the first time it has fired **twice
within the same iteration on the same lineage**, and the first time a
same-shift fix explicitly represented as closing a criterion-4 finding
has been shown, by the very next review to touch the file, not to have
closed it — on a violation that was sitting in an already-merged,
pre-existing file the whole time. Per unbroken precedent (Iterations 17,
36, 37, 38, and this cycle's own Phase-2 event), this remains a
**notification, not a pause**: Phase 5 close proceeds, with the
mandatory-fix docket below applied same-shift and a CHECKPOINT entry
recorded in LOGBOOK.md, SESSION_LOG.md, and PLAN.md that explicitly
states this is a second, same-iteration firing — not folded silently
into the first CHECKPOINT block as if it were the same event. Not a
physics finding: no engine/FDTD result is affected by any part of this
ruling.

---

## 3. Mandatory-fix docket

1. **Fix the false citation in `phase4_results.md`'s EM-5 section**
   (Finding 1): remove the "see Phase 1/3's own NOTES.md table" pointer;
   state the D=65nm/f=10%/ratio=0.982 figure was computed directly here
   from Section 4's own gap/packing-fraction relation, not co-sourced.
2. **Widen `exp061-t18-evidentiary-tier-propagation`'s `candidate_globs`**
   to include a broad per-experiment glob (e.g.
   `experiments/061-absorptivity-mechanism-literature-check/*.md` and
   `experiments/062-thin-film-interference-and-near-field-coupling-bound/*.md`,
   or more robustly a generic `experiments/*/phase*.md` pattern),
   mirroring the pattern `exp052-alpha-60nm-absorptivity-open` and
   `exp061-thermo-length-scale-staleness` already use. **Also widen
   `exp061-thermo-length-scale-staleness`'s own `candidate_globs`** the
   same way (Finding 4). **Also add a generic `experiments/*/phase*.md`
   (or equivalent) pattern to `lab/caveat_lint.py`'s own
   `DEFAULT_CANDIDATE_GLOBS`**, so a *future* registry entry authored
   without a hand-curated per-experiment glob does not silently inherit
   this exact blind spot a fourth time. This is the tool-level fix §2.2
   requires, not just a per-entry patch.
3. **Close the live violation directly**: add a T18/WebSearch-snippet
   sourcing-tier disclosure to `experiments/061-.../phase5_review_materials.md`
   itself, at its own restated UNOBTANIUM verdict — the specific,
   already-existing file this audit's Finding 3 names.
4. **Add Amendment 7 to `REALIZABILITY_MEMO.md` Entry 2** (Findings 5 + 8,
   bundled — both are the same "write the Phase-5 tier call back into the
   memo" action): record EM-6 (NiP-black, 6.9×–31× thickness gap,
   10.8×–56.2× rate gap — closest real comparator on thickness, but
   comparable-not-dominated on rate, breaking the CNT-forest "thickness
   not rate" pattern) and EM-7 (carbon/graphene aerogel, 694×–3472×
   thickness gap, worst comparator found) as named rows; restate
   Amendment 6's "overdetermined by thickness, not rate" sentence as a
   per-comparator claim (true for CNT-forest specifically), not a general
   property of every checked class; disclose the cross-query-pairing
   evidentiary weakness (α and thickness for both new comparators are
   taken from different sources, not one source's own paired
   measurement); remove the now-stale "not yet checked, queued" line.
5. **Disclose the EM-6/EM-7 R-vs-T methodology gap** (Finding 2) at both
   verdicts in `phase4_results.md`: no ÷2 correction was applied to these
   reflectance-based figures despite Section 4.2's own logic; applying
   one only widens the gap; neither conversion is a rigorous application
   of Section 4's coherent-film framework to what are actually diffuse-
   scattering porous media.
6. **Tighten EM-3's wording** (Finding 6): scope "structurally
   inapplicable" explicitly to the critical-coupling mechanism of §4.4;
   state any residual coherent contribution is governed by, not separate
   from, EM-1's own already-computed passivity bound.
7. **Add an explicit note to EM-5's verdict** (Finding 7): the
   pre-registered falsification condition, read literally, IS met
   (FALSIFIED, as a universal claim) by two of three sourced geometries;
   "PARTIAL" is a disclosed, post-hoc recharacterization, not the letter
   of the pre-committed bar; any future multi-geometry near-field
   prediction must pre-specify its own cross-geometry scoring rule before
   Phase 4 runs.
8. **Fill `NOTES.md`'s `Learned`/`Next` sections**, currently placeholder
   text (`[to be filled at Phase 5 close]`) — verified still empty by
   direct read. Substance: THERMODYNAMICS' own recommended restatement
   (§2 of its review) is the correct content — EM-5's actual result is
   PARTIAL/geometry-class-dependent, not CONFIRMED; the record-blackness/
   Vantablack-class forest's own pitch/diameter remains unpinned; the
   THERMO margin (1.35×–3.79×, UNDETECTABLE) is unaffected; EM-5b's
   direction remains genuinely untested-for (Finding-adjacent, see
   QUANTUM's §1), not merely unresolved.
9. **Run PHOTONICS' Phase-5 review** before this cycle's own record is
   treated as closed (see §2, standing note, and §5 below). This is not
   optional bookkeeping: PANEL.md's own Phase-5 spec requires all seven
   seats, and five of six non-Red-Team reviews plus this audit is not
   seven. Whatever PHOTONICS' fresh-context review finds should be
   folded into the LOGBOOK.md Iteration 39 entry before it is written, or
   the entry must explicitly disclose that it closes on six of seven
   seats and name PHOTONICS' review as owed.
10. **Fill the missing `ratio@600nm` cells** in EM-5's table for the two
    query-11 rows (harmless by monotonicity — confirmed by direct
    computation, `ratio@600=2.017` at D=65nm, `2.886` at D=93nm, both
    consistent with the reported 450/750nm values — but the table should
    be complete against its own three-wavelength scoring bar).

None of items 1–8, 10 changes any tier, verdict, or headline number.
Item 9 is process-completeness, addressed on its own merits in §5.

---

## 4. Final verdict: **PARTIAL**

Every one of the six actual reviews (three PROMISING — MATERIALS,
THERMODYNAMICS, EM; one PARTIAL for substantive open-physics reasons —
QUANTUM; one PARTIAL-provisional-to-PROMISING for the process gap this
audit's §2 resolves — VISION) agrees the underlying EM physics is sound,
independently re-derived to the printed digit at three separate stages
(Phase 1, Red Team's Phase-2 audit, Phase 4's own re-invocation, and now
a fourth time by two of the five Phase-5 reviews), and that nothing here
moves exp-061's own UNOBTANIUM-WITH-PARAMETERS tier — if anything, four
independently-sourced real-material comparator classes now fail the
joint 2×/2× bar, the strongest overdetermination this program has ever
assembled for this tier. On the physics alone, this cycle would earn
PROMISING outright, and I do not dispute that assessment.

But the verdict this program renders at Phase 5 is not a physics-only
verdict — it is a verdict on the *cycle's contribution as a whole*,
including its own process discipline, and this program has an unbroken,
explicit precedent (Iterations 36 and 37, both read in full for this
audit) for exactly this situation: a raw seat-count majority of
PROMISING, overridden to PARTIAL by Red Team specifically because a
live, unresolved caveat-propagation gap survives Phase 5's own review,
in the very machinery built to prevent it. Iteration 36 was 4-2 in favor
of PROMISING and was overridden. Iteration 37 was 5-1 and was overridden.
This cycle presents a **second same-iteration Checkpoint-4 firing**,
found live in an already-merged file, on a lineage whose grace was
already ruled fully spent before this cycle even began, discovered by a
lone dissenting seat exactly as both precedent cycles required — a
strictly *more* serious process fact than either precedent case, not a
lesser one. Declining to apply the same discipline here, on a fact
pattern textually stronger than either precedent, would itself be
inconsistent.

I also weigh, independently, the missing seventh review (§2, standing
note). A Phase-5 close on six of seven mandated fresh reviews is itself
an incompleteness this program has never previously recorded, and I
decline to certify a cycle as fully reviewed while one charter's
fresh-context read has simply never happened.

**Verdict: PARTIAL, provisional-to-PROMISING** — the same disposition
VISION's own review reaches, now Red-Team-ruled rather than deferred.
Once (a) the mandatory-fix docket above lands and is re-verified live
(not merely claimed), specifically items 2–3 (the actual coverage gap
and its live violation) and item 9 (PHOTONICS' own review), this cycle's
verdict should read PROMISING going forward, exactly as the precedent
pattern resolves once its own gates close. Every numeric claim in
Sections 4–5 of `phase1_proposal.md` and every scored verdict in
`phase4_results.md` stands unchallenged by this ruling — the override is
about process completeness, not physics, precisely as it was at
Iterations 36 and 37.

---

## 5. Ranked top-3 for Iteration 40+

Reconciling all six seats' own rankings (EM, MATERIALS, THERMODYNAMICS,
QUANTUM, and VISION each nominated a top-3; PHOTONICS' own list does not
exist — see standing note above, itself the reason item 0 below is
listed ahead of the substantive physics queue):

**0. (Process-completeness, must precede treating this cycle as closed)**
Run PHOTONICS' own Phase-5 review, fresh context, before LOGBOOK.md's
Iteration 39 entry is finalized — or explicitly record in that entry
that it closes on six of seven mandated seats and name the missing
review as owed at the top of Iteration 40's own docket. Apply this
audit's own mandatory-fix docket (§3) same-shift, independently
re-verified (not merely re-asserted) by whichever seat or Director step
executes it — the exact discipline that would have caught this cycle's
own Finding-3 shortfall before a third seat had to name it a third time.

**1. Pin the record-blackness/Vantablack-class CNT forest's own
inter-tube pitch/diameter.** Every one of the six real reviews
independently nominates a version of this as its #1 or #2 priority
(EM, MATERIALS, THERMODYNAMICS, QUANTUM, VISION all name it explicitly;
it is the one open physical sub-claim every seat agrees is both
real and now newly tractable). This cycle's own query 13 pinned the
`n_eff=1.04+0.01i` citation's originating title (*Carbon*, 2018, vol.
129, pp. 8–14) for the first time in 3+ cycles — a targeted follow-up
search naming that paper directly, rather than generic "VACNT forest
pitch/diameter" queries, is a fundamentally higher-yield next query and
would let EM-5 be scored against the program's own actual comparison
class for the first time, closing (not merely sharpening) the standing
`l_geometric_m` homogenization-validity question every one of
THERMODYNAMICS', QUANTUM's, and EM's own dispositions traces back to
this exact unpinned geometry. One search plan serves all three charters
simultaneously.

**2. Resolve EM-5b's near-field-coupling direction with an actually
dedicated query set.** QUANTUM's own review makes the sharpest version
of this point, independently confirmed by my own read of the 18 queries
`phase4_results.md` actually ran: none contains "superradiant,"
"subradiant," "coupled-dipole," "local-field correction," or any
synonym for the direction question EM-5b claims to score — the
"CONFIRMED UNDECIDABLE" verdict is an honestly-disclosed null result,
but one produced as a byproduct of queries built for EM-5's existence
question, not a genuine, targeted search for direction. A dedicated
query set (`coupled dipole near field correction absorption cross
section carbon nanotube array`, `subradiant superradiant collective
absorption sub-wavelength scatterer array`) is cheap, zero-FDTD, and
closes a real, sign-carrying gap — this program's own T25/T26 precedent
is exactly the cautionary pattern (a scalar existence test passing while
a sign-carrying effect hides underneath) that makes this worth
prioritizing over pure tooling debt.

**3. Build the numeric/derivation-consistency-check tooling, already
re-filed with a named owner at Iteration 40 (PLAN.md, this program's own
Red Team mandatory-fix item 6, one cycle ago) — widened per EM's own
Phase-5 recommendation.** This program now has three-plus independent
instances of a documentation-consistency failure class across two
distinct shapes: a cited NUMBER drifting unreconciled across sibling
files (`τ_shell=24` vs. 9.4026; the stale 150µm vs. the corrected range)
and, newly this cycle, the SAME derivation methodology (OD→α, R-vs-T)
applied two inconsistent ways within one document without
cross-reference (Finding 2). Whoever inherits this Iteration-40 rider
should widen its scope accordingly — a harder, more valuable check than
originally scoped, and this cycle's own EM-6/EM-7 gap is a live, ready
test case for it.

**Carried, lower priority** (multiple seats, not independently
re-ranked here): the `sim.omega` historical registry entry (EM); THERMO's
T25 sidecar-absence entry, bundle-candidate with the length-scale
entries above; MATERIALS' own tier-interpretation follow-up on whether a
NiP-black-style graded-porosity homogenization-validity check is owed
the same scrutiny this cycle gave VACNT forests, if a future cycle
elevates NiP-black's standing further.

---

## 6. Explicit Checkpoint check, all five criteria

1. **A configuration passes ALL constraint metrics.** Does not fire —
   zero constraint-1/2/3/4 metric is scored this cycle; "T1 escape route:
   NONE" is honestly declared in `phase1_proposal.md` §2 and confirmed
   true by every one of the six real reviews and my own independent read
   of `NOTES.md`/`phase4_results.md` end to end.
2. **A proven boundary: a constraint subset shown jointly unsatisfiable
   within a whole mechanism class, gates clean.** Does not fire — this is
   a realizability-bound refinement layered onto exp-061's own
   already-closed UNOBTANIUM-WITH-PARAMETERS boundary, not a new proof of
   joint unsatisfiability, and it manifestly does not "gate clean" while
   this audit's own mandatory-fix docket (§3, ten items) stands open.
3. **A synthesis requires engine physics beyond the validated bench
   classes.** Does not fire — zero FDTD, zero `lab/` engine file touched
   anywhere in this cycle's record, confirmed by my own inspection; the
   only new artifacts are prose (`NOTES.md`/`phase4_results.md`) and
   registry JSON, neither of which is engine physics.
4. **Program-integrity drift (unfalsifiable claims, a constraint quietly
   dropped — especially #3).** **FIRES — a second time, this same
   iteration, on the `exp061-t18-evidentiary-tier-propagation` tripwire's
   own text.** Full argument in §2. This is treated as its own,
   explicitly-labeled second CHECKPOINT event, not folded silently into
   the Phase-2 firing already on record — the gravity this finding
   deserves, per my charter's own instruction not to let program-integrity
   drift slip quietly past a boilerplate "notification, not a pause."
5. **Two consecutive iterations with no logbook-advancing result.** Does
   not fire — this cycle delivers multiple real, git-committed
   deliverables (the closed R-vs-T/resonance ambiguity, two new
   falsifiable realizability comparators, a 3+-cycle-standing citation
   finally pinned, and this audit's own Checkpoint-4 finding and
   mandatory-fix docket), continuing an unbroken run of logbook-advancing
   iterations.

**Summary: criteria 1, 2, 3, and 5 do not fire. Criterion 4 fires — a
second time this iteration, unprecedented in this program's history.**
Per unbroken precedent (Iterations 17, 36, 37, 38, and this cycle's own
Phase-2 event), this is a **notification, not a pause**: a CHECKPOINT
entry recording this as a distinct, second, same-iteration firing must
be written into LOGBOOK.md, SESSION_LOG.md, and PLAN.md, Marsh is
notified, and this cycle's own close proceeds with the ten-item
mandatory-fix docket above applied same-shift and independently
re-verified — not merely re-asserted — before Iteration 40 begins.
