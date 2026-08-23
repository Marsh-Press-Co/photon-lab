# Phase 5 — THERMODYNAMICS review (exp-062 / Panel Iteration 39)

*Fresh sub-agent, blind to the other six seats' current-cycle Phase-5
reviews. Charter: where absorbed energy goes; always asks what
re-radiates and whether it would be detectable; owns the per-proposal
energy sidecar (absorbed power → ΔT → emission band → detectability) as
a post-run analytic calculation, never an FDTD output.*

**Read in full**: `PANEL.md`; `LOGBOOK.md` (RULED OUT R1–R5 in full; LIVE
THREADS T1–T26, header-and-body for T18/T21/T25/T26 and a structural pass
over the rest); `PLAN.md` lines 1–100 and ~1904–1990; this cycle's
complete record (`phase1_proposal.md`, all five `phase2_critique_*.md`,
`phase2_redteam_audit.md`, `phase3_synthesis.md`, `NOTES.md`,
`phase4_results.md`); `experiments/061-.../NOTES.md`'s THERMO disposition
section and `lab/thermo_sidecar.py` in full; `REALIZABILITY_MEMO.md`
Entry 2; `lab/caveat_lint.py` and `caveat_lint_config.json`, both
exercised live against the working tree (not merely read).

---

## 1. Idealization 9 — was Red Team's docket item 4 applied correctly and fully?

**Applied correctly and fully, as scoped at Phase 3 — but now stale in one
specific, load-bearing way, given Phase 4's actual result. A further fix
is owed at this Phase 5.**

Red Team's docket item 4 required disclosure of two linked points, "not
one": (a) my own Phase-2 point — if EM-5 is CONFIRMED, flag for Phase 5
whether the standing THERMO disposition's `l_geometric_m`
(`exp061-thermo-length-scale-staleness`, margin 1.35×–3.79×) rests on a
Beer–Lambert bulk-homogenization this cycle's own result calls into
question; and (b) Red Team's own sharper, independently-traced finding —
that `l_geometric_m` is *definitionally* `τ_true/α` at MP-1's own
`n_eff=1.04+0.01i`-derived α figure, the same Bruggeman/effective-medium
fit Item B is interrogating, and that this construction sits textually
adjacent to (though, on Red Team's own inspection, does not violate)
`thermo_sidecar.py::gas_conduction_h_eff`'s docstring prohibition on "an
optical/extinction-derived length... NEVER" in place of "a real
geometric length of the... SOLID body."

Checked directly against `NOTES.md` Idealization 9 (lines ~241–259): both
points are present, not one. Point (a) appears verbatim as "If Item B's
near-field test is CONFIRMED, the α figure `l_geometric_m` is built from
is exactly the kind of number whose homogenization-validity this cycle
calls into question. Flagged for Phase 5 review." Point (b) appears
immediately after, introduced explicitly as "Separately, and
independently of Item B's outcome," and states the full chain — real
hypothetical-solid-thickness construction, not a grid-artifact proxy,
"textually adjacent to — though on inspection does not violate —"
`thermo_sidecar.py`'s guardrail, "named here so a future reader does not
have to rediscover it." I independently re-traced this chain against
`experiments/061-.../NOTES.md` (the THERMO disposition section, lines
~209–260 and ~450–461) and `thermo_sidecar.py` lines 186–199 myself, not
merely trusting Red Team's or my own Phase-2 characterization, and the
tracing holds: `l_geometric_m` = MP-5's found multiple (230×–730×) ×
1.44µm = `τ_true/α` at α=2.28×10³cm⁻¹, itself the `n_eff=1.04+0.01i`
Bruggeman fit — an extinction-derived quantity, defensible as-used
(representing a real hypothetical solid's thickness, not a
`sigma_ext_cells*dx_m`-style simulation-grid proxy, the module's own
named bad example) but genuinely adjacent to the forbidden category, as
both docket points require stating. **As a disclosure of what was known
at Phase 3, this is complete and honest — the mandatory fix was applied
correctly and in full.**

**Why it now needs a further fix.** Idealization 9's own trigger
condition is written as a binary: *"If Item B's near-field test is
CONFIRMED..."* Phase 4's actual result (`phase4_results.md`, EM-5) is
**PARTIAL** — falsified as a universal claim, confirmed for one sourced
CNT-forest geometry class (spin-capable/yarn-precursor forests, directly-
stated gap, ratio<1 at all three bench λ) and refuted for two others
(the stainless-steel-characterization diameter class and the directly
co-sourced r=60nm/f=11% forest, both ratio>1 at every bench λ except a
near-unity crossing at 750nm for one unfavorable combination) — with the
explicit further finding that **neither this cycle nor exp-061's own
query 9 ever pinned the pitch/diameter of the actual record-blackness/
Vantablack-class forest that MP-1's own α figure and `l_geometric_m`
cite.** Neither branch of Idealization 9's own "if CONFIRMED / [implicit
else]" structure cleanly fires: EM-5 is not CONFIRMED (so the sentence as
literally written does not trigger), but it is also not a clean
withdrawal of the near-field classification (which the proposal's own
§8 falsification condition — "falsified if sourced pitch/diameter give
ratio≥1 at any bench λ" — would treat as fully closing the question)
because it confirmed for a real, sourced, non-strawman geometry class.
`NOTES.md`'s own Idealization 4 anticipated exactly this shape of
problem for the *placeholder-vs-sourced* axis ("a CONFIRMED finding
confirms a placeholder-consistent result... Phase 4/5 must say so
explicitly") but Idealization 9 was drafted before Phase 4 ran and could
only anticipate a binary CONFIRMED/falsified outcome for Item B, not a
geometry-class-dependent PARTIAL with the specific comparison class
itself unpinned. This is not a defect in how the docket item was
executed — it is the ordinary, expected staleness of a pre-registered
conditional once the actual result lands outside the two cases it
imagined. Per this program's own house discipline (the same standard
that produced the `exp061-thermo-length-scale-staleness` entry in the
first place: a Phase-3 number left uncorrected after a later finding in
the same document superseded it), leaving Idealization 9 as literally
worded, unreconciled with Phase 4's actual PARTIAL result, is exactly the
kind of gap this program's own review discipline exists to close before
a future cycle cites Idealization 9 as if EM-5 had cleanly resolved
either way. **The further fix**: `NOTES.md`'s own `Learned`/`Next`
sections (currently `[to be filled at Phase 5 close]`) must restate
Idealization 9's finding to reflect the actual, three-way, geometry-
class-dependent result — see §2 below for the substance of that
restatement.

---

## 2. What EM-5's actual (PARTIAL/mixed) result implies for `l_geometric_m`

**It does not resolve the standing dependency in either direction — it
sharpens exactly what remains unknown, and that sharpening itself is the
useful result.** Before Phase 4, the open question was binary-shaped:
"is real CNT-forest geometry inside or outside the near-field-coupling
regime?" Phase 4 answers a *different*, more precise question that the
binary framing had quietly presupposed had one answer: **which forest?**
The result shows the regime classification is geometry-class-dependent —
confirmed for one real, sourced application class (spin-capable/yarn-
precursor forests) and refuted for two others (denser, larger-diameter
characterization and modulation-study forests) — and, decisively for my
own disposition, **the specific forest whose pitch/diameter would
actually settle the question for `l_geometric_m`'s own input — the
record-blackness/Vantablack-class comparator MP-1/MP-2 themselves drew
from — was never pinned, this cycle or last.**

This means the honest position on `l_geometric_m`'s homogenization is
neither "confirmed compromised" nor "confirmed clean" — it is **open,
and now demonstrably NOT closable by a generic "CNT forests are/aren't
near-field-coupled" argument**, because the answer turns on a geometry
this program has still never sourced for the specific material class its
own α citation actually uses. Three consequences follow, all disclosure-
level (no new margin computation is owed — see §3):

1. **The margin (1.35×–3.79×) itself is unchanged and the UNDETECTABLE
   classification is unaffected** — this was true before Phase 4 and
   remains true; nothing in EM-5's result touches the thermal physics
   (`gas_conduction_h_eff`, mass, ΔT_ss) downstream of `l_geometric_m`,
   only the trustworthiness of the α figure that length is built from.
2. **The uncertainty is now better characterized, not larger or
   smaller.** Before this cycle, the near-field question was unasked of
   any real geometry. After it, we know the effect is real and material
   for at least one CNT-forest application class — it is not a
   theoretical curiosity — but we also know the specific comparison
   class the disposition actually cites remains outside every sourced
   geometry this program has found. This is a genuine narrowing (from
   "unknown whether this matters at all" to "known to matter for some
   real forests, unknown whether it matters for THIS forest") even
   though it does not close the question.
3. **QUANTUM's own Phase-2 flip (EM-5b, direction) compounds this,
   unresolved (CONFIRMED UNDECIDABLE, Phase 4).** Even where near-field
   coupling IS confirmed present (the spin-capable-forest class), nothing
   in this cycle's record says whether that coupling would bias the
   Bruggeman-fitted `n_eff` — and therefore `l_geometric_m` — toward a
   LARGER or SMALLER effective α than the independent-scatterer reading
   assumes. A margin of 1.35× is fragile enough that either directional
   bias, if eventually pinned and large, could matter to the
   UNDETECTABLE classification's own robustness in a way a same-signed
   "coupling exists" finding alone cannot evaluate.

**Recommended restatement for `NOTES.md`'s `Learned` section** (substance,
for the Director to adopt or amend): *"EM-5's actual result is PARTIAL,
not CONFIRMED: near-field coupling is real for at least one sourced
CNT-forest class and absent for two others, and the specific record-
blackness-class forest `l_geometric_m`'s own α figure derives from
remains geometrically unpinned by any search this program has run
(exp-061 query 9 or exp-062 queries 11–12/15). The standing THERMO
disposition's UNDETECTABLE classification and 1.35×–3.79× margin are
unaffected (no new sidecar computation is owed), but the open question
Idealization 9 flagged is NOT resolved by this cycle in either direction
— it is sharpened into a specific, nameable, still-open sub-question:
pin the pitch/diameter of the actual comparator forest the n_eff=1.04+
0.01i citation describes (now that its title is pinned — Carbon, 2018,
vol. 129, pp. 8–14 — a future WebSearch-snippet pass, or a T18-unblock,
could target that paper's own reported geometry directly), and separately
resolve EM-5b's direction question before treating the near-field-
coupling finding as informative about `l_geometric_m`'s bias, not just
its existence."*

---

## 3. Is any new energy-sidecar computation owed this cycle?

**No — unchanged from my own Phase-2 critique, and Phase 4's actual
result does not change this.** This remains a zero-FDTD, zero-new-
absorbed-power cycle: `phase4_results.md` reports WebSearch-snippet
findings and closed-form Airy/passivity/gap-ratio arithmetic, none of
which is a new measured absorbed-power number for any configuration this
program has simulated. PANEL.md's per-run ledger obligation ("Absorbed
energy budget + predicted re-radiation") attaches to FDTD runs, of which
this cycle has none — my charter's expressibility contract explicitly
labels the sidecar "a post-run analytic calculation, not an FDTD output,"
and there is no new run to post-process. The genuinely new finding this
cycle produces (EM-5's PARTIAL, geometry-class-dependent near-field
result) bears on the *trustworthiness of an existing sidecar's input*
(`l_geometric_m`), which is a disclosure obligation (§§1–2, above), not a
computation obligation — no ΔT, h_eff, or mass calculation needs
re-running, because none of those functions' own inputs (density,
k_air, dwell time, the construction's physical thickness) changed; only
the confidence behind the α figure that `l_geometric_m` is derived from
did, and even that confidence is now "more precisely characterized as
open" rather than "moved in a specific direction." EM-6/EM-7 (the new
NiP-black/aerogel comparators) likewise produce no sidecar obligation:
neither crosses into the "within 2× of both α and thickness" band that
would make either a candidate `graded_black_shell` realization needing
its own detectability check — they remain literature comparators for
MATERIALS' tier judgment, not new simulated or hypothesized objects this
bench has built.

---

## 4. Verdict: **PROMISING**

The core EM physics (Sections 4–5 of the frozen configuration) is sound,
independently re-derived to the printed digit at three separate stages
(Phase 1's own script, Red Team's Phase-2 re-derivation, Phase 4's
own re-invocation) and delivered a **more decisive, structural**
resolution of the R-vs-T/resonance ambiguity than predicted (EM-3/EM-4:
the OD figure's measurement geometry makes the Salisbury-screen
alternative *structurally inapplicable*, not merely disfavored by a
probabilistic broadband reading) — a genuine improvement over exp-061's
unchecked point estimate, landing exactly where the pre-registered
falsification conditions said a "reinforces, does not threaten" outcome
would land, without foreclosing the possibility that it could have gone
the other way. The two new realizability comparators (EM-6 NiP-black,
EM-7 carbon/graphene aerogel) are real, falsifiable, band-scored
findings — one the closest real-material secondary comparator this
program has ever found (6.9×–31× thickness gap, smaller than CNT-
forest's own 70–350×), the other the worst (694×–3472×) — genuinely new
information, not a null result dressed up. The one open item (EM-5/EM-5b,
near-field coupling existence and direction) is a real, disclosed,
geometry-class-dependent PARTIAL, not a failure of the cycle's own
design — it correctly replaced QUANTUM's vocabulary-presence fallback
with a physical test, and the physical test worked exactly as a good
instrument should: it returned a nuanced, geometry-dependent answer
instead of a false binary. The Checkpoint-4 firing (the
`exp061-t18-evidentiary-tier-propagation` tripwire) was a registry-
scoping notification, not a physics defect, remediated same-shift and
independently verified live by this review (`caveat_lint.py --only
exp061-t18-evidentiary-tier-propagation` now PASSes all four required
sites). None of this reaches RULED OUT (nothing here closes a mechanism
class or a T1 escape route — this cycle scores no constraint metric by
design) and PARTIAL undersells a cycle whose two mechanism-class
questions (R-vs-T basis; resonance-vs-bulk) both closed cleanly and whose
two new comparator classes both delivered real, falsifiable, non-
degenerate findings. The genuinely open item (near-field direction and
the unpinned comparator-forest geometry) is exactly the sharpened,
nameable next step PANEL.md's own "honest alternative product" language
anticipates — a real finding about the boundary of what this program's
own α citation can currently support, not a failure to find one.

---

## 5. Top-3 ranked candidate directions for Iteration 40+

1. **[THERMO-owned, my own disposition's direct next step] Pin the
   pitch/diameter geometry of the ACTUAL record-blackness/Vantablack-
   class CNT forest `l_geometric_m`'s own α figure (n_eff=1.04+0.01i)
   describes.** This cycle pinned the citation's title for the first
   time (*Carbon*, 2018, vol. 129, pp. 8–14, "Modulation of the effective
   density and refractive index of carbon nanotube forests via
   nanoimprint lithography") after 3+ cycles of being un-pinnable — a
   real, useful unlock. A future cycle should mine WebSearch snippets
   specifically targeting THIS paper's own reported pitch/diameter/
   packing-fraction figures (title-targeted search is a fundamentally
   different, higher-yield query than the generic "VACNT forest
   inter-tube spacing" queries this cycle and exp-061 both ran) and score
   the resulting geometry against the already-built `gap/(λ/2π)`
   criterion. This is the one search that would actually close, not
   merely sharpen, Idealization 9's own open question — directly in my
   own charter's line, since it resolves whether the sidecar's own input
   length rests on a licensed homogenization.
2. **Resolve EM-5b (near-field coupling direction — enhance or suppress)
   via a more targeted search than this cycle's reused query set.**
   QUANTUM's own Phase-2 flip (superradiant/subradiant collective
   response, the T25/T26-precedented "sign hides under a scalar gate"
   risk) remains CONFIRMED UNDECIDABLE, not because the physics is
   unknowable but because this cycle's queries were built for existence,
   not direction — a dedicated query set (`coupled dipole near field
   correction absorption cross section carbon nanotube array`,
   `subradiant superradiant collective absorption sub-wavelength
   scatterer array`) is a cheap, high-value follow-up that would let a
   future cycle actually bound which way, and by how much, any
   confirmed near-field coupling would move the cited α relative to the
   independent-scatterer reading.
3. **Render MATERIALS' own deferred Phase-5 tier interpretation for
   EM-6/EM-7** (explicitly assigned to Phase 5 by this cycle's own
   Phase-3 synthesis, not yet rendered in this file) **and, if MATERIALS
   elevates NiP-black to a closer comparator than CNT forests, re-run
   this cycle's own near-field-coupling-style validity check against
   NiP-black's OWN microstructure** (a rough, graded-porosity metal
   surface — a structurally different homogenization risk than a VACNT
   forest's near-field coupling, but a comparably unexamined one). NiP-
   black is now the closest real-material comparator this program has
   ever found; if MATERIALS' tier judgment treats that as materially
   narrowing MP-4's exclusion, the same "is a bulk-α reading licensed at
   all for this microstructure" question this cycle asked of CNT forests
   would need asking of NiP-black too, before any α figure derived from
   it could safely feed a future THERMO disposition.

---

## 6. Second same-iteration Checkpoint-4 gap — found, own charter

**A second, independently-discovered, same-shape registry-scoping gap
exists in `exp061-thermo-length-scale-staleness` — my own standing
disposition's entry — verified live, not merely suspected.**

Running `python3 lab/caveat_lint.py --only exp061-thermo-length-scale-staleness`
against the current working tree shows 0 required-site failures (the
entry's single required site, `experiments/061-.../NOTES.md`, still
correctly carries the corrected 1.35×–3.79× margin) — but the WARN
candidate-discovery pass, which is supposed to surface undocketed sites
citing the same trigger terms, **never lists any of exp-062's own files**,
even though `experiments/062-.../NOTES.md` contains the literal string
`l_geometric_m` and the phrase "margin 1.35×–3.79×" (verified by direct
`grep`), and `experiments/062-.../phase2_critique_thermodynamics.md`,
`phase2_redteam_audit.md`, and `phase3_synthesis.md` all discuss
`l_geometric_m`'s construction at length (Red Team's own docket item 4
tracing lives in `phase2_redteam_audit.md`, not in any file this entry's
`candidate_globs` can reach).

Tracing why, directly in `lab/caveat_lint.py`'s own source: this entry's
`candidate_globs` is `["LOGBOOK.md","PLAN.md","experiments/*/NOTES.md",
"experiments/061-absorptivity-mechanism-literature-check/*.md"]` — a
generic `NOTES.md` pattern (which DOES match exp-062's NOTES.md) plus one
exp-061-specific wildcard that reaches every OTHER exp-061 file but no
exp-062 file at all. exp-062's `NOTES.md` is caught by the generic
pattern but is silently excluded from even a WARN listing because it
already contains one of the entry's own `phrase_patterns`
(`1\.35.{0,10}3\.79`) — correct behavior, not a bug, for that one file
(it already carries the caveat). But `phase2_critique_thermodynamics.md`,
`phase2_redteam_audit.md`, and `phase3_synthesis.md` — three files that
extensively discuss `l_geometric_m`'s construction, including the single
sharpest tracing of it this program has ever produced (Red Team's
docket item 4) — are **structurally invisible to this registry entry**:
they match no `candidate_globs` pattern at all, so the tool never even
checks whether they carry, misstate, or omit the corrected margin. This
is the *identical* failure shape Red Team's own Phase-2 audit found and
ruled Checkpoint-criterion-4-firing for the sibling
`exp061-t18-evidentiary-tier-propagation` entry this same iteration: a
required_sites/candidate_globs list, scoped before a citing cycle
existed, that cannot discover that cycle's own verdict-bearing documents.

**This is NOT ruled, by this seat, to auto-fire Checkpoint criterion 4
the way the sibling tripwire did.** That entry's "no further
deliberation" auto-fire language is textually specific to the
`exp061-t18-evidentiary-tier-propagation` lineage, whose self-catch grace
Red Team explicitly ruled "fully used" at Iteration 38 close — a
tightened tripwire this entry (`exp061-thermo-length-scale-staleness`)
has never received, and this is its FIRST self-caught gap, not a second
strike against an already-spent grace. On the general Checkpoint-4
standard (program-integrity drift), I do not find an unfalsifiable claim,
an inconsistency, or a quietly-dropped constraint here — the required
site still passes, and no wrong number has actually propagated anywhere
in the record; this is a coverage gap with no live defect underneath it,
the same posture Red Team found for the `exp060-p10`-style near-misses
before they escalated. **But it is the same BUG PATTERN recurring across
TWO different registry entries within the same iteration** (discovered
independently — VISION found the first at Phase 2, I found this one at
Phase 5) — a program-level observation Red Team and the Director should
weigh: whether `caveat_lint_config.json` entries should default to a
broader candidate-discovery pattern (e.g., a generic
`experiments/*/phase[0-9]_*.md` glob, covering critiques/synthesis/audit
files program-wide, not just NOTES.md and phase4_results.md) rather than
requiring each entry's author to anticipate every future citing file by
name or narrow pattern. **Recommended same-shift mandatory fix** (cheap,
mechanical, matching the Phase-3 remediation already applied to the
sibling entry): widen `exp061-thermo-length-scale-staleness`'s
`candidate_globs` to include a generic pattern reaching sibling-cycle
critique/synthesis/audit files (at minimum
`experiments/*/phase2_critique_thermodynamics.md` and
`experiments/*/phase2_redteam_audit.md` and
`experiments/*/phase3_synthesis.md`, or more robustly
`experiments/*/phase*.md`), so a future cycle's mischaracterization of
`l_geometric_m` in a critique or synthesis document — not just a NOTES.md
— would actually surface as a WARN. I flag this for Red Team's own
ruling on Checkpoint applicability, per PANEL.md's own discipline that no
single seat unilaterally fires or dismisses a criterion-4 candidate; my
own read is that it warrants the same-shift mechanical fix regardless of
the ruling, since — like the sibling gap — remediation costs nothing and
closes the exact failure shape this program's own history (six prior
caveat-propagation near-misses before `caveat_lint.py` was built) shows
recurs when left open across cycles.

---

## 7. Ruled-out registry check (R1–R5, T1–T26)

**No re-proposal found**, independently checked against `LOGBOOK.md`'s
RULED OUT section (R1–R5, full text) and a structural pass over the LIVE
THREADS section, with a direct read of T18, T21, T25, and T26 (the four
threads the cycle's own record and critiques cite by name).

- **R1–R5**: none apply. This cycle proposes no T1 mechanism (T1 escape
  route: NONE, honestly declared and true on inspection — no
  constraint-1/2/3/4 metric is scored anywhere in `phase1_proposal.md`,
  `NOTES.md`, or `phase4_results.md`). R4 (hand-typed "precisely
  recomputed" figures) is the one rule with live bite on a desk-
  calculation cycle like this one, and it is honored throughout: every
  numeric figure in Sections 4.5/5.3 of the proposal, and every figure in
  `phase4_results.md` (EM-2's re-derived 6.908×10⁴cm⁻¹/1.2034×, EM-6's
  4605–5298cm⁻¹ band, EM-7's 12.06–60.32cm⁻¹ band) is stated as computed
  by direct invocation, independently re-verified by Red Team at Phase 2
  to the printed digit.
- **T18** (WebFetch evidentiary ceiling): correctly invoked, not
  re-litigated — `phase4_results.md` Step 1 re-confirms the block (43+
  consecutive attempts since Iteration 13) before falling back to
  WebSearch-snippet synthesis, disclosed at the file's own closing
  verdict per the (now-widened) `exp061-t18-evidentiary-tier-propagation`
  registry entry, independently verified live by this review (§6's
  `caveat_lint.py` invocation) to actually PASS all four required sites,
  not merely claimed to.
- **T21** (ambient-contrast per-angle fringe, an FDTD-source instrument
  artifact) and **T25/T26** (coherent-vs-incoherent ambient-sum bridge
  gate, empty-scene artifact): both are FDTD-instrument-characterization
  threads about this program's own `lab/ambient.py` machinery. exp-062
  runs zero FDTD and makes no ambient-contrast claim; its near-field-
  coupling rider (Item B) is a real-material homogenization-validity
  question at VACNT geometric scales, a different physical object from
  either thread. QUANTUM's and Red Team's own citations of T25/T26 (as a
  structural precedent for "a scalar gate can pass while a sign-carrying
  effect hides underneath," applied to EM-5's binary existence test) are
  correctly used as an analogy for a risk pattern, not as a re-proposal
  of either thread's own specific claim — verified independently, this
  reading holds on direct inspection of both threads' actual text.
- No thread in the T1–T26 list makes a claim about thin-film
  interference, black-matrix optical-density conventions, or
  Salisbury-screen/critically-coupled absorbers — Section 4's Airy-stack
  analysis is new to this program's record, not a restatement or
  contradiction of anything already closed.

---

## Summary for the Director

Idealization 9 was applied correctly and fully against Red Team's
original two-point docket requirement — the gap is not in its
authorship, but in its own necessarily pre-Phase-4 binary framing now
being outrun by Phase 4's actual three-way, geometry-class-dependent
result. That result does not move the standing THERMO disposition's
UNDETECTABLE classification or its 1.35×–3.79× margin, and owes no new
sidecar computation, but it does owe an updated `Learned`/`Next`
disclosure (§2) reflecting that the near-field question is sharpened, not
closed, and that the specific comparator forest `l_geometric_m` actually
depends on remains geometrically unpinned. A second, independently-
discovered, same-shape registry-scoping gap exists in my own
disposition's `caveat_lint_config.json` entry (§6) — recommended for a
same-shift mechanical fix regardless of its Checkpoint-4 status, which I
defer to Red Team's ruling. Verdict: **PROMISING**.
