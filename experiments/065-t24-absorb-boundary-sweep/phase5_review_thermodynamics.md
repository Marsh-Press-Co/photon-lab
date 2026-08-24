# PHASE 5 — REVIEW · THERMODYNAMICS · Panel Iteration 42

*Reviewing exp-065 in full, fresh context: `phase1_proposal.md`, all five
`phase2_critique_*.md` (including my own seat's), `phase2_redteam_audit.md`,
`phase3_synthesis.md`, `NOTES.md`, `phase4_results.md`, `results.json`.
Charter: where absorbed energy goes — absorbed power → ΔT → emission band →
detectability, post-run analytic, labelled as such; own the per-proposal
energy sidecar.*

---

## 1. Read against my own charter's standard

### 1a. Did the T5/T5_THERMAL_CAVEAT disclosure — my own Phase-2 mandatory
fix — get correctly discharged?

**Mostly yes, in the machine-readable record; no, in the human-facing
results document.** `design_geometry.py` defines `T5_THERMAL_CAVEAT` as a
code constant (not hand-typed), `run.py` threads it structurally into both
`NOTES.md`'s "Carried caveats" list and into `results.json`'s
`caveats.t5_thermal` field and again inline in `P-VIS42-7`'s own `caveats`
array. The text is correct and complete: it names T5/Iteration-20/exp-043,
states the >100×-below-NETD UNDETECTABLE finding, and states explicitly
that only the far-boundary padding changes between C40 and C80 (same σ,
same r_out) so no new thermal question is opened. That is exactly what I
asked for at Phase 2, and it is code-produced, not prose I have to trust.

But `phase4_results.md` — the document a future cycle will actually read
when citing this experiment, per this program's own repeated Iteration-40
finding that a citation's real-world discovery risk lives in the
human-facing document, not just the JSON — **never mentions T5, thermal,
NETD, or detectability anywhere.** I grepped it directly; zero hits. And no
`caveat_lint_config.json` entry was ever registered for this cycle at all
(checked directly: the file's 9 entries run through `exp064-*`; there is no
`exp065-*` entry of any kind) — so nothing machine-checks that this
disclosure survives into any future document the way `exp063-thermo-
disposition-netd-disclaimer` machine-checks the CNT cycle's own NETD
sentence. This is the identical shape of gap that fired Checkpoint
criterion 4 at Iteration 40 (a disclosure present in one document, absent
from the sibling document a citation would actually be built from) — here
it is one step worse, because there is no registry entry at all to have
been under-scoped. Low stakes on its own (the physics claim itself is
correct and the disk's UNDETECTABLE disposition is genuinely inherited
unchanged — I re-derive this independently below), but it is a real,
disclosed-nowhere gap in exactly the place this program has been burned by
before.

### 1b. Does the settling confound have any thermal implication?

**The proposed reading — "no, because Block ARTICLE's own numbers are
separately scored" — is right for the quantity my charter actually owns,
and incomplete for a related quantity that is not mine but sits next to
it.**

Right, for absorbed power/ΔT/NETD: `lab/thermo_sidecar.py` is not imported
anywhere in this experiment (verified: `§8.3` states it, and no
`thermo_sidecar` symbol appears in `run.py` or `design_geometry.py`). The
T5 UNDETECTABLE finding this cycle cites is a *different, independently
computed* result from exp-043's own bench-scale run — a σ/r_out-driven
radial absorbed-power ledger and a lumped-capacitance ΔT calculation, not
a Weber-contrast reading. The STEPS=1400-vs-2800 settling defect lives
entirely inside the ambient-contrast `C_empty` channel (`sections.phasors`
→ `ambient.window_means` → `ambient.weber`) — a flux-ratio quantity built
from the observer-plane field snapshot at the *end* of a run that has not
reached steady state. Nothing in that pipeline touches the absorbed-power
integral my sidecar's own inputs are computed from. **Confirmed: no
thermal-disposition number in this program moves because of this cycle's
settling finding.**

Incomplete, for Block ARTICLE's own MARGINAL bucket call: P-VIS42-7's
C_C40 = −0.004503 / C_C80 = −0.004602 is an N9 aggregate over
`FALLBACK_ANGLES` = {0, ±5, ±15, ±25, ±35}° — **not** the ±38°/±40° cells
Diagnostic 1/2 actually tested. The one thing this cycle establishes about
STEPS=1400 is that it is badly unsettled *at 40° specifically, on an empty
scene* (74.4% relative shift at C40, 40°, 600nm) and that the mechanism is
general to "the plane/tapered-source empty-scene channel at near-grazing
angles," not to padding. Whether that same channel is similarly unsettled
at ±35° and inward, and — a second, untested axis — whether a *loaded*
scene (Block ARTICLE's actual σ>0 disk, which damps the field differently
than an empty cavity) settles at the same rate as the empty-scene diagnostic,
is simply not checked anywhere in this record. `phase4_results.md`'s own
"What this means for P-VIS42-3/4/5/9/10" section is explicit about every
other affected prediction but is silent on P-VIS42-6/7 — an omission, not
a stated "checked and fine." This is not a thermal finding — it is a
Weber-contrast/instrument-floor question, squarely VISION's or PHOTONICS'
charter — but it bears directly on how much confidence the "no new thermal
question is opened" sentence can borrow from the article's own C-value
being trustworthy at all. My own charter's disposition (UNDETECTABLE, from
an independent σ/r_out-based ledger) does not depend on this Weber-contrast
question either way — that is real, and worth stating cleanly rather than
implying the whole article row is untouched by the settling finding.

### 1c. Is PLAN.md's top-ranked CNT `R_contact` item named honestly, or
minimized?

**Neither — it is absent.** Red Team's Phase-2 mandatory-fix docket item 8
read: "Name the CNT `R_contact` trade-off explicitly — one sentence added
to §0, no design change." `phase3_synthesis.md`'s own disposition table
records it as accepted and "Applied as: one sentence added to §0." I
checked every document this cycle produced for the words `R_contact`,
`CNT`, or `trade`/`trade-off`: `phase1_proposal.md` (unmodified since
03:25, before the 03:55 Phase-3 synthesis — its mtime alone shows it was
never touched to add the promised sentence), `NOTES.md`, `phase4_results.md`,
`results.json`, `run.py`. **Zero hits anywhere except the original two
mentions already in `phase1_proposal.md` §0 before the fix was even
proposed.** The sentence that was accepted as a mandatory fix and recorded
as delivered was never actually written into any committed document.

This is my seat's specific catch, and it is not a small thing: PLAN.md's
current queue (checked directly, lines 2223–2234) names the CNT-forest
`R_contact` term as item (1), "CURRENT top-of-queue," named at or near #1
by five of six Iteration-41 seats, and "the ONLY carried item that can
actually MOVE TD-5's own margin" — this program's thinnest safety factor
of any kind on record (7.8×). exp-065 is the **second consecutive cycle**
this item has been passed over (once at Iteration 41 in favor of the
`length_provenance` guard, now again at Iteration 42 in favor of T24). That
trade-off is a legitimate call to make — Red Team's own Iteration-41
recommendation to feed a constraint-scored FDTD run is a real, competing
program-integrity concern — but a mandatory fix was specifically written to
require that the trade-off be *named*, was accepted, recorded as applied,
and then not applied. This is the identical species of defect R4 exists to
police ("a falsifier or self-consistency figure... MUST be produced by
invoking the actual committed function... never hand-typed") extended one
step further: not a wrong number, but a *docket item marked delivered that
was never delivered at all* — the fix-docket-delivery pattern this program
named explicitly after its third recurrence (R4's own text) and has now
recurred an unknown-but-nonzero-additional time, unflagged by any of the
six Phase-2 seats, unflagged by Red Team's own audit (which reviewed the
proposal, not the post-synthesis delivery), and undetected until this
Phase-5 read.

---

## 2. Verdict

**PARTIAL**, on my own charter's terms, converging with what the record
already shows program-wide. The core physics claim my seat can verify
independently is clean and low-risk: Block ARTICLE's τ=0.0065 disk
inherits the T5/exp-043 UNDETECTABLE disposition unchanged (same σ, same
r_out — the only thing this cycle varies is a far-field boundary that has
no absorbed-power role), and the code-produced caveat text saying so is
accurate. But the cycle's actual headline (T24's own inheritance question)
is explicitly undecided — REFUTED-then-recomplicated by the STEPS=1400
settling defect, which is itself a real, large, well-diagnosed, honestly
reported finding — and one mandatory-fix item squarely inside program
process discipline (naming the CNT trade-off) was accepted and then not
delivered, undetected by five other seats and by Red Team's own audit.

---

## 3. Ranked next directions — does the settling gap change my seat's own
priority ranking relative to CNT `R_contact`?

**No — it sharpens the case for `R_contact`, it does not compete with it.**
The STEPS=1400 finding is entirely inside the ambient-contrast/Weber-
contrast instrument (an optical/perceptual channel); it touches zero
absorbed-power, zero ΔT, zero NETD-comparison machinery anywhere in this
program's record. There is no version of "re-verify exp-041's MAIN-block
rows at STEPS≥2800" that moves TD-5's 7.8× margin or any other THERMO
sidecar number. My ranking, in order:

1. **CNT-forest root-to-substrate `R_contact` term (PLAN.md's own
   top-of-queue, now deferred twice).** Unchanged priority, and now
   carrying an added, specific obligation: whichever cycle finally builds
   it should also close out this cycle's own undelivered §0 sentence as
   part of the same pass, so the "why was this deferred again" record is
   honest going forward, not just physically correct going forward. This
   is still the only queued item that can *move* a number rather than
   relabel or disclose one, on this program's own thinnest safety margin.
2. **Re-verify exp-041's MAIN-block ±38°/±40° rows at STEPS≥2800, scoped
   to determine downstream citation impact** (Phase 4's own Next item 1).
   Not my charter's item to lead, but I flag it as urgent from my seat's
   own review discipline: this is a genuine candidate for retroactive
   uncertainty on every T21/T24/near-threshold-constraint-3 number since
   Iteration 18, and the sooner it is scoped the sooner any future THERMO
   sidecar work that happens to cite an ambient-contrast bucket (as
   P-VIS42-7 does, descriptively) knows whether that citation is safe.
3. **Register a `caveat_lint_config.json` entry for `T5_THERMAL_CAVEAT`**,
   scoped to both `NOTES.md` and `phase4_results.md` from the start (not
   `NOTES.md`-only, repeating Iteration 40's own already-named mistake) —
   cheap, in my own charter, and closes the one gap this review found that
   is actually mine to own.

---

## 4. Checkpoint criterion opinion

**In my own reasoned opinion: yes, criterion 4 fires** — narrowly, on the
undelivered CNT `R_contact` mandatory-fix sentence (§1c above), not on the
STEPS=1400 settling finding. The settling discovery is the process working
exactly as designed: self-caught, disclosed prominently, followed up
same-shift, not hidden — that is the opposite of drift. But a docket item
Red Team wrote, the Director accepted, and `phase3_synthesis.md` records
as "Applied," that was in fact never written into any committed document,
is precisely "program-integrity drift" in the sense my charter's own
prior catch (R4, adopted after its third recurrence) exists to name — an
unfulfilled mandatory fix silently absent from the record it was supposed
to correct, undetected by six other independent reviews before this one.
It is my seat's own specific catch to make, and I make it as a finding for
Red Team's ruling, not a self-executing verdict.

---

*THERMODYNAMICS, Panel Iteration 42, Phase 5.*
