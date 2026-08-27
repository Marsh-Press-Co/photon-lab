# PHASE 5 — REVIEW · VISION SCIENCE · Panel Iteration 55 (exp-078)

*Fresh sub-agent, blind to the other five Phase-5 reviewers and to Red
Team's own Phase-5 final audit (which has not yet run). Charter (PANEL.md
seat 6, verbatim): "human perceptual limits... pin numeric thresholds,
with sources, BEFORE any run that scores against them." As stated already
in this cycle's own `phase2_critique_vision.md` and every prior T28
instrument-fidelity cycle: **no perceptual threshold exists to pin here**
— T1 escape route N/A, no absorber, no ambient scene, no constraint-3
claim anywhere in this record. Per this task's own brief, this seat's
load-bearing duty this cycle is the other standing one: commensurability
auditing (R9's own origin, adopted on this seat's Iteration-54 finding),
sharpened here to trace every corrected comparison back to its defining
primitives and to independently verify at least one load-bearing number.*

---

## 1. Verdict: **PARTIAL**

exp-078 set out to answer one narrow question — does a closed-form,
zero-FDTD period pre-screen of the y-normal (transverse) wall echo land
anywhere near T28's established periods, before anyone spends the effort
building the full coherent propagator? After a load-bearing angle-
convention bug (raw `theta` vs. the geometrically correct `90-theta` for
a y-stratified interface) was caught by three independently blind Phase-2
critics and corrected before Phase 3 froze anything, the honest answer is
**no, not encouragingly**: 0/3 comparisons SUPPORT, 0/3 REFUTE, and a
fresh 20,000-trial null-calibration control confirms none of the three
corrected `rel_dev`/R² values are distinguishable from pure noise at the
conventional 0.05 level (`PAIR_PAD`, T28's own actual dominant target:
`p=0.1258`). This is real, verified narrowing of the SAME shape as
exp-075/077 before it: a candidate mechanism class is not desk-closed
(nothing here reaches the `>1.00` REFUTE bar either), but the specific
evidentiary case the as-filed document made for building the full
y-mirrored propagator (2 of 3 raw comparisons clearing SUPPORT) is now
known to have been entirely an angle-convention artifact. Not PROMISING —
nothing here should be read as license to spend on the full model.

Where I diverge from a simple "process worked, nothing to add" reading:
my own independent audit (§2 below) found the corrected write-up itself
still carries an unflagged internal inconsistency — a table that was never
regenerated at the corrected angle, sitting directly beneath prose marked
"CORRECTED" — and a genuine structural fact about the model's own
construction that the record states empirically ("essentially unmoved")
but never explains, which materially changes how much evidentiary weight
`PAIR_PAD`'s own Test-A result can ever carry, under this instrument, no
matter what future run improves it. Neither finding moves the Combined
Verdict; both are worth fixing before Iteration 56 cites this record.

---

## 2. Independent re-verification (R4) and commensurability audit

I did not restate any figure from `phase1_proposal.md`, `phase3_
synthesis.md`, `phase4_results.md`, or `phase2_redteam_audit.md`'s prose.
Every number below was recomputed by importing `y_wall_prescreen.py` and
calling its own functions directly, or read from the raw committed JSON,
not from any document's narrative about either.

### 2a. R9 registry check — independently re-derived, clean

Red Team's Phase-2 audit (Attack 7) already ruled no R9-shaped unit
mismatch exists in this file's scoring. I re-derived this independently
rather than accept it on Red Team's word: `rel_dev` compares two periods,
both in degrees-of-θ, both extracted by the identical imported
`_free_period_search`/`free_period_with_widening` machinery applied to the
real `delta(theta)` curve and the model's `cos(Δφ_self)` curve alike — same
units, same algorithm, no cross-normalization anywhere in `score_period()`
or its callers. The null-calibration p-values (`P(null rel_dev≤0.30)`,
`P(null rel_dev≤observed)`, `P(null R²≥observed)`) are three distinct,
correctly-labeled proportions, never conflated with each other or with a
raw `rel_dev`. **No R9-style defect found, confirmed by direct code
re-derivation, not by re-checking Red Team's own arithmetic.**

### 2b. Independently verified: `phase1_proposal.md` §5.2's own table was
never regenerated at the corrected angle — a real, previously-uncaught
R4-family risk, exactly the kind the task asked me to check for

I ran `edge_image_curve`/`free_period_with_widening` myself, directly,
for all five configs (`C40`/`C60`/`C70`/`C80`/`G40`) at **both**
`use_corrected_angle=False` (as-filed) and `use_corrected_angle=True`
(the primary, pre-registered computation per the mandatory-fix docket),
independent of `phase4_results.md`'s own re-run:

| cfg | ptp (as-filed) | P* (as-filed) | R² (as-filed) | at bdry (as-filed) | P* (corrected) | R² (corrected) | at bdry (corrected) |
|---|---|---|---|---|---|---|---|
| C40 | 76.897° | 3.2180° | 0.1557 | no | 3.2180° | 0.1537 | no |
| C60 | 131.795° | 4.0000° | 0.2418 | **yes → 60°, R²=0.9895** | 3.1278° | 0.1197 | no |
| C70 | 133.798° | 4.0000° | 0.2777 | **yes → 60°, R²=0.8740** | 3.1955° | 0.1424 | no |
| C80 | 358.446° | 3.1880° | 0.1439 | no | 2.9098° | 0.1100 | no |
| G40 | 76.897° | 3.2105° | 0.1544 | no | 3.1053° | 0.1204 | no |

**The as-filed column reproduces `phase1_proposal.md` §5.2's committed
table exactly, digit for digit** — `ptp`, `P*`, `R²`, and the "yes, widens
to 60°" boundary flags for `C60`/`C70` all match. **The corrected column
does not appear anywhere in the document.** Under the corrected angle —
the one Phase 3/4 declared primary, the one every scored `PAIR_*`
comparison in §5.3 actually uses — **no individual config hits the search
boundary at all**; `C60`/`C70`'s entire "runs to 60°, implausibly high R²"
story is a pure artifact of the wrong angle and simply does not occur
under the model this cycle adopted as its own headline computation.

This matters because of *where* it sits, not just that it's stale. §5.2's
own surrounding prose was patched with a visible strikethrough and a bold
**CORRECTED** tag addressing whether the boundary-running behavior is
"float noise" or real — but that correction discusses a phenomenon
(`C60`/`C70` pinning to a 60° period) that the corrected model does not
actually produce. A reader who trusts the "CORRECTED" label (reasonably —
it is right next to the table, and Phase 4's own docket item 5 states
"§5.2/§5.3/§7 rewritten around the corrected numbers") would come away
believing `C60`/`C70`'s boundary-pinning is settled, real model behavior.
It is not: it is settled, real behavior of the **wrong**-angle model,
which the committed document keeps displaying as if it were live. This is
the precise shape PANEL.md's own R4 discipline and this task's own
briefing named as a risk — an in-place correction that leaves a stale
number standing next to a "corrected" label, primed to be read as current.
**Non-load-bearing**: `C60`/`C70` enter no scored `PAIR_*` comparison
either way (§5.2's own text says so, correctly, both before and after
correction), so nothing about the Combined Verdict moves. But a future
reader citing "`C60`'s free period widens to 60° under this model" would
be citing a claim that is false under the model this cycle actually
adopted — worth a same-shift table refresh before Iteration 56 cites this
record, the same standard R4's addendum sets for any figure a Phase-5
reviewer finds not fully corrected.

### 2c. A genuine structural finding neither the proposal nor any Phase-2
critique states: `PAIR_PAD`'s Test-A period is mathematically forced to
equal `C40`'s (and `G40`'s) own individual period — it is not independent
evidence

Reading `y_wall_prescreen.py` line 478 directly:
`model_delta_pad = cos(Δφ_self^{G40}(θ)) − cos(Δφ_self^{C40}(θ))`. I
confirmed numerically (§3.4's own premise, independently re-derived) that
because `C40` and `G40` share `ABSORB=40`, `arg(r(θ;40))` is bit-identical
between them at every swept θ (`diff=0.0` at 36°/39°/42°, both angle
conventions) — only the theta-*independent* `fixed_offset` term differs
(`76.999` vs `154.500` cells). So `Δφ_self^{G40}(θ) = Δφ_self^{C40}(θ) + c`
for a **constant** `c` (no θ-dependence at all, for fixed λ). By the
identity `cos(x+c)−cos(x) = −2 sin(c/2)·sin(x+c/2)`, `model_delta_pad(θ)`
is therefore, exactly, a rescaled, phase-shifted copy of the **same**
underlying oscillation `Δφ_self^{C40}(θ)` — not a new function with its
own independent θ-dependence. A single-frequency sinusoid fit (which is
what `free_period_with_widening` performs) cannot distinguish a
phase-shifted, rescaled copy of a curve from the original when it comes
to recovered *period* — only the fitted amplitude and phase parameters
differ. The committed JSON confirms this is not an approximation:
`primary_model_pair_deltas.pair_pad.p_star_deg = 3.218045112781955`, **bit-
identical to 15 significant digits** to `primary_model_period_search.
chosen.C40.p_star_deg = 3.218045112781955`, independently reproduced by
my own re-run.

This is a real consequence of the model's own construction, worth stating
plainly since neither `phase1_proposal.md`'s Idealization list (1–8) nor
any of the five Phase-2 critiques name it: **`PAIR_PAD`'s Test-A period,
under this instrument, is not measuring anything about the `PAD`/geometry
axis specifically — it is re-testing `C40`'s (equivalently `G40`'s) own
individual `arg(r(θ;40))` oscillation against the real `PAIR_PAD`
reference period, with the `PAD` axis contributing only an overall
amplitude scale-factor, never new θ-structure.** This generalizes: *any*
future `PAIR_*` comparison built from two configs sharing `ABSORB` will
inherit this same degeneracy under the edge-image reduction, by
construction, regardless of whether the underlying y-wall mechanism is
correct. It does not change today's verdict (the failed-to-clear-SUPPORT
result stands either way, and the JSON's own R² value for the pair,
`0.15635`, is close enough to `C40`'s own `0.15365` that no numeric
correction is owed), but it is a materially different piece of
information about what this pre-screen's own headline comparison is
actually capable of showing, and it bears directly on how much weight
`PAIR_PAD`'s specific `rel_dev=0.3021` should carry in any future ranking
that treats it as "the actual dominant target's own dedicated test."

---

## 3. Ranked top-3 Iteration-56 candidates

Checked against R1–R9 and T28's named dead ends first: none of the three
below revisits a ruled-out idea (no cloak/refraction claim, no
integer-λ/shell-thickness rule, no re-litigated ground-truth or
null-calibration gate already settled elsewhere, no unfit-conditioning
closure claim).

### #1 — Execute the twice-deferred "real absorbing article loaded" PAD-sensitivity test (LOGBOOK Iteration 54 Tier 2 item 9, this seat's own named charter-relevant candidate, exp-076/exp-077's own ranking)

Every T28 cycle in this sub-thread's history, including this one, has run
on the **empty scene** — the `PAD_TIED` signal (Iteration 53) and this
cycle's own y-wall pre-screen both characterize a phenomenon that has never
been tested with anything physically present in the domain. This is the
one item on the standing Iteration-54 ranking explicitly named as this
seat's own charter-relevant question ("this cycle's empty-scene-only scope
could not reach it") and it has now been deferred twice without execution
(Iterations 53 and 54; exp-078 did not touch it either). Deferring it a
third time without an explicit reason is exactly the pattern Iteration
54's own ranking flagged as something that should not recur. From my own
seat's actual charter: an empty-scene coherent-echo artifact that vanishes
or changes character once a real absorbing object occupies the domain is a
fundamentally different finding for the phenomenon program than one that
survives — the former means T28's entire six-plus-cycle sub-thread has been
characterizing a pure solver artifact with no bearing on any future
constraint-3 scene; the latter means it is a genuine feature of how this
engine represents any absorbing article, which the program's own eventual
Tier-W/Tier-A ambient-contrast readings would inherit silently. Cheap
relative to a full propagator build (reuses the existing `graded_black_
shell` article and the already-validated `C_empty`-family instrumentation,
no new machinery), and it is the one candidate that actually tests whether
this six-cycle instrument-fidelity investigation has any downstream
relevance to the program's real target at all.

### #2 — Pre-register the amplitude/normalization convention for any future Test-B build, BEFORE it is built — a forward R9 guard, this seat's own duty stated literally

`phase1_proposal.md` Idealization 2 already discloses that `cos(Δφ_self)`
is "used as a unit-amplitude proxy oscillation curve" — not a real-unit
field amplitude, not normalized to `C_empty`'s Weber-contrast scale, not
weighted by `|r(θ)|` or aperture taper. This program has already paid once
for exactly this shape of gap: T16/R9 (this seat's own Iteration-54
finding) show a fitted-carrier-normalized `amp_ratio` compared directly to
a raw `C_thr` threshold, undetected for a full cycle, until traced back to
its defining primitives. The y-wall pre-screen's own §0 correctly scopes
Test B (a real amplitude/shape match against `delta(theta)`) as future
work, not this cycle's — which is exactly the moment to pin the
commensurability contract *before* anyone builds it, per this seat's own
charter duty ("pin numeric thresholds... BEFORE any run that scores
against them," generalized here to normalization conventions). Concretely:
any future Test-B build must state, in writing, before its first run,
whether its model curve is being compared to `C_empty(theta)` in raw
Weber-contrast units, in `amp_ratio`-style fitted-carrier-normalized units,
or in some third convention — and which of those (if any) the real
`delta(theta)` curve it's scored against actually uses. This is cheap
(a documentation/pre-registration step, not new code) and directly
forecloses a fourth instance of R9's own failure shape in this exact
sub-thread.

### #3 — Refresh `phase1_proposal.md` §5.2's table to the corrected angle (this review's own finding, §2b)

Lowest cost, lowest priority relative to #1–#2, but concrete and
previously unflagged: replace §5.2's still-as-filed per-config table with
the corrected values this review independently computed and reports above
(§2b), and either remove or re-scope the "widens to 60°" language, which
does not occur under the model this cycle adopted as primary. Zero new
computation is required — the corrected numbers already exist in the
committed JSON (`primary_model_period_search.chosen`); this is a table
copy-in, matching this program's own established practice for a same-shift
docket item.

---

## 4. Seat-specific finding

Stated plainly, as instructed: no perceptual threshold applies to this
cycle's record — no contrast measurement, no luminance edge, no adaptation
state, no constraint-3 scene exists anywhere in this file, and I found
nothing that smuggles one in. What I did contribute, as this seat has on
every prior non-perceptual T28 cycle, is the commensurability/rigor pass:
independently re-deriving the R9 registry check rather than accepting Red
Team's own clean bill of health on faith (§2a), and going one level past
what any of the six documents under review checked — not just "does the
corrected model reproduce," but "does the *write-up itself* now correctly
and completely reflect the corrected model everywhere it appears" (§2b),
and "does a passing commensurability check on `rel_dev`/R² also mean the
comparison being scored is actually independent, new information" (§2c).
Neither finding was visible from re-checking arithmetic alone — both
required tracing the comparison back to the code that produces it, exactly
this seat's standing duty, sharpened this cycle by being the seat whose
own Iteration-54 finding created R9 in the first place.

---

## Bottom line

**PARTIAL.** The corrected y-wall echo period pre-screen is genuinely
INCONCLUSIVE (Test-A-only) — 0/3 SUPPORT, 0/3 REFUTE, null-calibration-
confirmed indistinguishable from noise — and this narrowing is real: the
as-filed document's case for building the full propagator (2/3 raw SUPPORT)
was entirely an angle-convention artifact, correctly caught and corrected
before Phase 3 froze it. My own independent audit found the corrected
write-up is not itself fully consistent — §5.2's table was never
regenerated at the corrected angle (§2b) — and found a genuine structural
fact this cycle's own record states empirically but never explains:
`PAIR_PAD`'s Test-A period is mathematically guaranteed to equal `C40`'s/
`G40`'s own individual period by the model's construction, not independent
evidence about the `PAD` axis (§2c). Neither finding changes the Combined
Verdict. My top-ranked Iteration-56 candidate is the twice-deferred,
seat-native test of whether this entire six-cycle instrument-fidelity
signature survives with a real absorbing article in the domain — the one
open question that would tell this program whether any of it matters to
the phenomenon the panel actually exists to reproduce.
