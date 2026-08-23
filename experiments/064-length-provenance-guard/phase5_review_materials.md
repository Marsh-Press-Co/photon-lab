# exp-064 — Phase 5 Review: MATERIALS & METAMATERIALS

*Fresh sub-agent, blind to the other seats' current-cycle Phase-5 reviews.
Charter: sub-wavelength structure, what could physically realize a
proposed optical/thermal behavior; owns the realizability bound
(published / plausible / unobtainium-with-parameters). Read PANEL.md in
full, LOGBOOK.md in full (T23's complete history, Iteration 38–40 in
full, the live-threads register), PLAN.md's current-state and
Iteration-41 queue block, `lab/thermo_sidecar.py` and
`lab/validation/run_all.py` (stages 18/23/24) as they now stand, and all
of `experiments/064-length-provenance-guard/`. Independently re-verified
Red Team's own re-derivation against `experiments/061-.../phase4_results.md`'s
MP-2/MP-5 sections directly, by direct read, not by trusting either
seat's summary.*

---

## 0. Independent verification of Red Team's re-derivation (task item a)

**Confirmed correct, by direct read of `phase4_results.md`, not by
trusting MATERIALS' own Phase-2 critique or Red Team's restatement of
it.**

MP-2 (CONFIRMED) sources three corroborated real CNT-forest/Vantablack
thicknesses at the visible band: 300–500µm (forest-films-on-substrates
source), 100–300µm (Surrey NanoSystems VBx2 datasheet), and a weakly-
sourced ~250µm (S-VIS) — a combined sourced envelope of **100–500µm**.
The one figure below this (<20µm) is explicitly excluded by MP-2's own
text as mid-IR, not visible-band, "not a like-for-like near-total-
blackness comparator" (line 149, 157–159).

MP-5's own table (lines 299–335) computes six thickness-needed-for-
τ_true=8.26 rows from six different α anchors. The two extremal
visible-band rows are 332µm (S-VIS-paired) and 1056µm (300–500µm/1–2%R,
low-α end).

Cross-ratio, taking the extremes of each already-CONFIRMED/already-scored
range (not re-measuring anything): 1056/100 = **10.56×**; 332/500 =
**0.664×**. So the honest span, stated as a range, is **≈0.66×–10.56×**
— Red Team's "≈1×–10.5×" is a defensible rounding of that span (the
low end rounds up from 0.66 to "~1×"; nothing rounds down at either end
to manufacture a more favorable-looking number). I re-derived this
independently from the same two already-published tables and get the
identical figures. **Confirmed correct.** This is categorically different
from Phase 1's own "24×–75×" claim (331/14=23.6, 1051/14=75.1) — that
comparison used an uncited "~14µm" figure that Phase 1's own §6 never
checked against MP-2's own already-established 100–500µm record, and
which most plausibly duplicates the <20µm mid-IR outlier MP-2 itself
already named and excluded. MATERIALS' own Phase-2 catch, and Red Team's
independent confirmation of it, are both correct.

One caution on the corrected figure I did not see stated as sharply as
it should be even in the corrected framing: the 0.664×–10.56× span mixes
extrema across *different, non-corresponding* MP-1 α-anchors and MP-2
thickness sources (best-case α paired with worst-case sourced thickness,
and vice versa) — a legitimate best-case/worst-case *bounding* statement,
not a same-sample apples-to-apples ratio. That is a fair way to state a
bound, but it is worth being explicit that it is a bound of two
independently-varying quantities, not a single material's own measured
margin. Nothing in the record currently says this.

---

## 1. Was striking §6 entirely the right call, or was something real lost? (task item b)

**My own reading: striking was defensible on the compounding-error
argument Red Team gave, but it discarded more real information than the
Phase-3 synthesis credits, and I would have preferred Red Team's own
option (a) — restate, corrected and caveated.**

The case for striking (Red Team's stated reason): a corrected §6 still
carries PHOTONICS' undisclosed idealization (forest height ≠ single-pass
Beer-Lambert absorption path length under diffusive/multiply-scattering
transport; oblique incidence moves the ratio in an unstated direction) —
restating a number under that unresolved idealization risks shipping a
second under-qualified claim in the same paragraph that just got
corrected for shipping an uncorrected one, and R4 (this program's own
standing rule against hand-typed or under-checked "precisely recomputed"
figures) argues for caution rather than urgency here.

The case against striking, which I think deserved more weight than it
got: the ≈0.66×–10.56× figure is not a new measurement subject to R4's
own concern about hand-typed arithmetic — it is a **ratio of two numbers
this program had already independently scored and committed** (MP-2
CONFIRMED, MP-5 PARTIAL, both already in `phase4_results.md`, both
re-verified live by Red Team and by me against the primary file). The
"undisclosed idealization" PHOTONICS caught is a real gap, but Red Team's
own docket for a *restated* §6 explicitly required PHOTONICS' one-
sentence idealization disclosure alongside it (mandatory-fix item 2,
option (a)) — meaning the corrected, properly-caveated version was
already fully specified and ready to ship at essentially zero
incremental risk. Striking it does not make the underlying question go
away; it makes the one already-computed, already-checked answer to "how
big is the gap between what's been grown and what witness scale needs"
*undiscoverable* without a future reader re-deriving it from MP-2/MP-5
by hand — the exact kind of buried-in-two-different-documents-and-never-
reconciled state this program's own R4/numeric-consistency discipline
exists to prevent, now recreated in the other direction (a correct,
useful number, un-surfaced, rather than a wrong one, surfaced).

Concretely, what was lost: the raw MP-5 table on its own reads as "230×–
730× the *bench construction*" — a number that, read in isolation,
suggests deep unobtainium territory. The ≈0.66×–10.5× figure is a
materially more informative reading of the *same* underlying data: it
says the witness-scale thickness need sits close to, and in the best
case *within*, the range of real published CNT-forest/Vantablack
thicknesses (100–500µm) — not 230–730× beyond anything ever grown, only
up to an order of magnitude beyond the thinnest reported sample. That is
a genuinely different, more encouraging realizability picture than the
"×1.44µm-bench-construction" framing alone conveys, and it is exactly
the kind of synthesis MATERIALS' own charter (the realizability bound)
exists to produce. Filing it under "PLAN.md queue item 3, undisturbed"
is not equivalent to having stated it: item 3 is scoped as "pin pitch/
diameter and κ together," and nothing in its text currently points a
future reader at this specific, already-computable comparison.

**Recommendation, carried to my own top-3 below**: recover this, not by
reopening exp-064's own scored record, but as a small, explicitly-scoped
addition to `REALIZABILITY_MEMO.md` (Entry 2's own natural home) —
computed once, correctly caveated with PHOTONICS' idealization sentence,
and cited back to MP-2/MP-5 rather than re-derived as new. This is a
disagreement with the Director's Phase-3 disposition, not a claim that
the disposition was reckless — striking was a safe, defensible choice
given the compounding-error concern; I judge it left value on the table
that a five-minute, zero-risk follow-up recovers.

---

## 2. Does the allow-list design hold up against MATERIALS' realizability-bound concerns? (task item c)

**No — and this is the sharpest finding of this review.** The guard
enforces *provenance-honesty* (did this length come from the bench scene,
a sourced measurement, or an acknowledged optical back-calculation) — a
question about **where a number came from**. It does not, and by its own
documented scope cannot, enforce **provenance-TIER** in MATERIALS' own
charter sense: whether the object that length describes is a published,
real, already-built material; a plausible-but-unbuilt one; or an
unobtainium-with-parameters one relative to `REALIZABILITY_MEMO.md`'s own
standing three-tier verdict axis (published / plausible /
unobtainium-with-parameters — the exact vocabulary this seat's charter
runs on, e.g. Entry 1's RSA/TPA/photochromic rows, Entry 2's own
UNOBTANIUM-WITH-PARAMETERS verdict).

This is visible directly in the code, not merely inferable. Read
`_geometric_realizability_note`'s own docstring and body
(`lab/thermo_sidecar.py`): for a `diagnostic_only=True` call it correctly
returns an `"UNGROUNDED..."` string distinguishing provenance-honesty from
buildability — real, useful, exactly the distinction this proposal set
out to add (Red Team mandatory-fix 4, THERMODYNAMICS' catch). But for
*every licensed call* — `bench_construction` or `measured_geometric` —
the identical field returns a flat `"N/A -- length_provenance=... is a
licensed real-geometric-length category; this field only qualifies
diagnostic_only=True calls."` That is a genuine, code-level admission that
the buildability-vs-honesty distinction the guard exists to make is
**only wired to the diagnostic path**. A `measured_geometric`-tagged
length is, by construction, honestly *sourced* — but nothing in
`_validate_length_provenance` or `_geometric_realizability_note` asks
whether the material class it was measured on is itself
published/real, plausible, or one this program's own memo would rate
UNOBTANIUM-WITH-PARAMETERS for an entirely unrelated reason (dynamic
range, irradiance threshold, dose accumulation — any of the axes
`REALIZABILITY_MEMO.md` already tracks). A future proposal could source a
perfectly real, perfectly honest `measured_geometric` length from a
material this program's own realizability memo would otherwise disqualify
on a different axis, and the guard would wave it through as "N/A —
licensed," with no signal at all that a realizability question remains
open. This is a distinct, sharper gap than the "does today's tagged
length actually belong to the SAME candidate identity as the rest of the
call" material-identity-coherence point already named (Red Team attack
7, my own Phase-2 secondary point) — that one is about internal
consistency between two lengths in one call; this one is about whether
the guard says anything at all about whether the object it licenses has
ever been shown buildable, for any material identity.

To be clear about severity: **this is not a live violation today.** Every
current bench-scale call site (`R_OUT_M`/`r_out_m`) is a length of the
FDTD-modeled solid body itself, not a sourced-but-unrelated-material
length, and no `measured_geometric` call site exists in the record yet at
all (route (a)'s own diligence in Phase 1 §6 found no real geometric
length usable at witness scale — the guard has never actually been
exercised on this path). It is a structural blind spot, comparable in
kind to EM's own already-flagged provenance-ROLE gap (attack 5,
non-blocking) and MATERIALS' own already-flagged material-identity-
coherence gap (attack 7, non-blocking) — but I judge it distinct from
both and worth naming explicitly on its own, because it is the one gap
that sits squarely on THIS seat's own charter question (the realizability
bound) rather than on a general software-correctness concern, and because
the very field built this cycle to close exactly this kind of ambiguity
(`geometric_realizability`) explicitly, by its own text, declines to
cover it for the licensed path. The fix is cheap and additive — see my
top-3, below — and does not require reopening anything this cycle
shipped.

---

## 3. Everything else checked

- **QP-1 through QP-5, RT-1, RT-2**: independently spot-checked against
  `lab/thermo_sidecar.py` and `phase4_results.md`'s own transcript. The
  allow-list (`{"bench_construction","measured_geometric"}` /
  `{"extinction_derived_diagnostic_only"}`), the keyword-only no-default
  signature, and the deliberate-break test (mistag one witness-scale call
  site → 27/28, revert → 28/28) are exactly as described. This is
  unusually strong verification for a "the gate actually gates" claim —
  better evidenced than most of this program's prior trust-suite-stage
  claims, which typically stop at "the gate passes," not "the gate was
  shown to fail when it should."
- **The `biot_number` non-guard** is correct: it takes no length
  argument (`Bi_gas = k_air/k_solid`), confirmed by direct read.
- **T23's own operative closure** (does an enforced check now sit on the
  actual committed call sites, not just the guard function's abstract
  behavior) is real: stage 24 gate 4 text-scans `run_all.py`'s own
  committed source, which is the one thing the original Phase-1 §4 gate
  suite (correctly caught by EM's Phase-2 attack, independently
  confirmed by Red Team) would NOT have done. This is the correct fix and
  it is verified, not merely asserted.
- **The caveat-string-preservation gate** (VISION's catch, RT-2) closing
  a class of loss this program has now paid for twice on the identical
  `netd_disclaimer` string is a genuinely good, cheap addition.

---

## Verdict: **PROMISING**

This is a code-architecture/instrument-trust cycle, T1 escape route N/A,
zero constraint-1/2/3/4 metric scored by design — the right frame for
judging it is "did it close what it set out to close, honestly and
verifiably," not a mechanism verdict. On that frame: **yes.** T23 — a
real, load-bearing thread open across four cycles (22→23 by argument,
then violated in the open at 38/39/40 with only disclosure, never
enforcement) — is now closed by a genuinely enforced, independently
demonstrated (deliberate-break-tested) code-level guard, not another
disclosure sentence. The Phase-2 process caught the one defect that would
have mattered most (EM's attack: the original gate suite would not have
actually checked the real call sites) *before* it shipped, and Phase 3's
fix is independently verified, not merely re-asserted. My own seat's §6
catch was independently reverified correct by Red Team and by me. No
Checkpoint criterion fires, correctly.

I withhold a plain "promising, no reservations" only because of the two
findings above: (1) striking §6 rather than restating it correctly and
caveated left real, already-vetted realizability information off the
record for no compounding-risk reason I find fully compelling, and (2)
the `length_provenance` guard's own realizability-honesty field
(`geometric_realizability`) explicitly declines to say anything about
buildability for the licensed path — the exact axis this seat's charter
owns. Neither is a defect in what shipped; both are gaps in what the
cycle chose not to cover, cheaply fixable, and correctly scoped as
forward queue items rather than reasons to downgrade this cycle's own
verdict.

---

## Ranked top-3 candidate directions for Iteration 42

1. **Source, or formally model as a third disclosed scenario, the
   CNT-forest root-to-substrate thermal contact resistance** (my own
   Iteration-40 finding, carried unchanged as Iteration 41's own #1 item
   and correctly left untouched by this cycle's own scope). TD-5's own
   7.8× headroom on κ_solid is this program's thinnest safety margin of
   any kind on record, and query 10's already-sourced van der Waals
   inter-tube contact-resistance finding plausibly governs the
   root-substrate interface too, not just the inter-tube contacts already
   modeled. Highest-priority MATERIALS item on the board; unrelated to
   this cycle's own guard work and should not be further deferred.

2. **Extend `geometric_realizability` (or a sibling field) to the
   LICENSED path, not just `diagnostic_only=True`** — close the gap
   named in §2 above. Concretely: a `material_realizability_tier`
   parameter/field (published / plausible / unobtainium-with-parameters,
   `REALIZABILITY_MEMO.md`'s own existing vocabulary — no new taxonomy
   invented), optional today (no live `measured_geometric` call site
   exists to retrofit), but present so the FIRST future call that sources
   a real geometric length is forced to also declare its realizability
   tier rather than silently reading as fully-clean the moment it clears
   `_validate_length_provenance`. Zero FDTD, a few lines, directly closes
   a gap this cycle's own code comments admit exist ("this field only
   qualifies diagnostic_only=True calls").

3. **Recover the struck §6 finding correctly, as a committed
   `REALIZABILITY_MEMO.md` entry, not a re-litigation of exp-064's own
   scored record.** Compute and commit the ≈0.66×–10.56× MP-5-vs-MP-2
   gap (§0/§1 above), explicitly captioned as a comparison of two
   already-CONFIRMED/PARTIAL exp-061 numbers, carrying PHOTONICS' own
   one-sentence idealization caveat (forest-height ≠ single-pass
   Beer-Lambert path length under diffusive transport; not corrected for
   oblique incidence) verbatim. This is the natural companion to the
   already-queued PLAN.md item 3 (pin pitch/diameter + κ together) — pin
   the thickness-realizability comparison at the same time, in the same
   place, rather than leaving it implicit in two documents that never
   cite each other.

Carried, lower priority, correctly non-blocking per Red Team's own
Phase-2 ranking: EM's provenance-ROLE structural gap (attack 5) and my
own material-identity-coherence gap on `measured_geometric` across
different CNT-forest process classes (attack 7) — both real, both
still-hypothetical (no live call site triggers either today), both
naturally folded into item 2 above if/when a real `measured_geometric`
call site is finally sourced.
