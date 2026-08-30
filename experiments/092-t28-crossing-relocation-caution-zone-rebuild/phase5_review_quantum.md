# PHASE 5 — REVIEW · QUANTUM OPTICS · Panel Iteration 69 · exp-092

## Verification performed before writing this review

Every number below was re-derived from primitives I pulled myself — the
task brief's two mandatory checks, plus a third I added on the same
discipline, all done by importing the actual committed functions and
running them against `results.json`, not by reading the printed
conclusions and trusting them.

1. **`find_zero_crossings`, both windows, imported directly from
   `experiments/091-.../run.py` (unmodified) and applied to the raw
   `delta_scene` values `exp-092`'s own `combined{}` dict actually builds**
   (Rank 1's seven fresh per-theta values from `results.json::rank1.
   per_theta`, plus exp-091's own already-filed `40.2°/41.4°` — since the
   sigma branch chose native `0.5`, matching `run.py`'s own `filed_r3_leg2`
   branch — and `40.4°/41.6°` from exp-091's own `raw.
   r3_leg4_cpl30_steps4200_bracket`): reproduces **`40.07183833857387`**
   (lower), **`41.781067311937264`** and **`41.8376530294636`** (upper) —
   bit-exact against `run_output.txt`'s cited `40.0718°`/`41.7811°`/
   `41.8377°`, zero discrepancy. Hand-verified the linear-interpolation
   arithmetic (`t0 = θᵢ + Δθ·|a|/(|a|+|b|)`) for all three crossings against
   the raw bracket values directly (e.g. `40.0 + 0.2×(2.449455/6.819354) ≈
   40.0718`); matches to the precision of the hand calculation.
2. **`ratio_sign_verdict` for Rank 3, both `delta_scene` and
   `frac_contrast`, from the raw `(ratio, sign_match)` cells in
   `results.json::rank3.per_theta`** — recomputed the ratios myself from
   the stored `sigma_corrected_*`/`filed_*` pairs (not trusting the stored
   `*_ratio` fields), confirmed they match the stored fields exactly, then
   ran `ratio_sign_verdict` on both cell lists: `ds_verdict=CONFIRM`,
   `fc_verdict=CONFIRM`, `overall=CONFIRM` — matching `results.json`
   exactly. All six cells (`0.9226`/`1.0141`/`1.1720` for `delta_scene`;
   `0.9382`/`1.0267`/`1.1827` for `frac_contrast`) sit comfortably inside
   `[0.3,3.0]`, nowhere near either boundary — this is not a borderline
   CONFIRM.
3. **Added, not requested but load-bearing to R1b's own comparators**:
   re-derived the two "known `cpl=20`" crossing constants
   (`40.26541960305772`/`41.46090139413461`) hardcoded in `run.py` by
   running `find_zero_crossings` myself over the full 31-point `cpl=20`
   census (`experiments/083-.../results.json::per_theta`) — bit-exact
   match, confirming the comparator baseline `run.py` compares the new
   `cpl=30` locations against is itself correct, not merely internally
   consistent. Also re-derived Rank 2's ORIGINAL/DROP/RELABEL table an
   independent time, importing `firth_logistic`/`auc`/`naive_mle_diverges`
   from `experiments/090-.../run.py` directly and rebuilding the `n=7` rows
   from `090-.../results.json::table1` (itself cross-checked bit-exact
   against a from-scratch recomputation of `margin=frac_contrast/FLOOR`
   using `experiments/083-.../results.json`'s raw `delta_scene`/`C40_C`) —
   `AUC=1.0/1.0/0.8333`, zone `[1.4764,2.1709]`/unchanged/`[1.4764,1.3095]`
   inverted, `m₅₀=2.071012796646712/1.8180612310318796/1.0317173247854177`
   (matching the cited `2.071013/1.818061/1.031717` to the stated
   precision), `naive_mle_diverges=True/True/False`. **This is now at least
   a ninth independent bit-exact reproduction of this specific table**
   across this sub-thread's history (EM at Phase 1, QUANTUM and Red Team at
   Phase 2, the Director twice at Phase 2/3, and now this review, on top of
   the live in-`run.py` recomputation itself).

**Result: zero discrepancies found anywhere I checked** — not "small,"
not "non-load-bearing," genuinely zero, across three independently
re-derived headline computations plus a fourth supporting one.

## Verdict: **CONCUR**

I concur with every scored verdict in `NOTES.md`'s Result section: (R3)
CONFIRM, (R3b) CONFIRM, (R1a) NEITHER (correctly the mechanical output of
1 lower + 2 upper crossings, per the pre-registered rule), (R2) CONFIRM,
and the empty-leg consistency ALL MATCH. This is, on the numbers, one of
the cleanest single-cycle runs this sub-thread has produced — no gate
failure, no sign-flip surprise in the load-bearing verdicts, no arithmetic
defect anywhere I could find one. My findings below are completeness/
scope observations, not corrections to anything filed.

## §1. The mechanical NEITHER correctly reports a genuinely split result — and `NOTES.md` already says so; the pre-registration itself is the (mild, self-caught) gap

The three-way (R1a) trichotomy was built around counting crossings per
window. Under that rule, 1 lower + 2 upper crossings forces NEITHER
mechanically — I verified this myself (§ above) and the code's branch
(`if len(lower)<=1 and len(upper)<=1: ... else NEITHER`) implements the
pre-registered text exactly, no discretion exercised at runtime.

What I want to flag, distinctly from "was it computed correctly" (yes): a
single scalar CONFIRM/NEITHER/REFUTE label is a poor instrument for a
result that is, substantively, two independent findings glued together —
a clean, unambiguous single-crossing success in the lower window and a
genuinely new, un-forced double-crossing discovery in the upper window,
straddling a `NODE-UNRESOLVABLE` point. `NOTES.md` itself already names
this exact gap in its own "Learned" §2 ("that one label undersells a
substantively split outcome... future crossing-search designs on this
channel should consider scoring each window's own outcome separately")
— so this is not a new catch, it is a confirmation that the write-up's
own self-assessment is accurate and complete, not softened. I record it
here because a future Phase-1 author citing this cycle's own (R1a) verdict
in one line ("NEITHER") without the window-level detail would be a
regression from what this document itself already discloses.

## §2. The upper "new positive finding" rests on two points that fail the floor gate — the write-up discloses this, but the framing strength deserves one more sentence of caution

`NOTES.md`'s Result section calls the double-crossing "a new positive
finding, not merely a failure to locate" and cites three corroborating
signals: two sign changes and a `NODE-UNRESOLVABLE` classification at the
point they straddle (41.8°, `floor_pass=False`, the smallest-magnitude
`delta_scene` this cycle measured). I independently confirm all three
signals are real (§ above, and directly from `results.json::rank1.
per_theta`: 41.8° `ratio_k=172.46`, `floor_pass=False`; 42.0°
`ratio_k=15.96`, also `floor_pass=False`).

The caution I'd add: **both** flanking points of the shorter, second
crossing (41.8° and 42.0°) are themselves `NODE-UNRESOLVABLE` — the
`frac_contrast` at 42.0° (`1.533×10⁻⁴`) does clear `FLOOR`
(`1.917×10⁻⁴`)... actually checked directly: `1.533×10⁻⁴ < 1.917×10⁻⁴`,
so 42.0° fails the floor too, consistent with its own printed
`floor_pass=False`. That means the entire evidentiary basis for the
*second* of the two crossings (41.8°→41.84° segment) sits inside a region
this bench's own house floor-gate discipline (R13) says not to trust a
single point's classification from. The three-signal corroboration
argument is real and I don't think it's wrong — but "corroborating
signals that are all drawn from the same floor-failing neighborhood" is
weaker corroboration than three *independent* floor-clearing
measurements would be, and the write-up's "new positive finding" framing,
while hedged appropriately elsewhere (Learned §3 calls it "a coherent...
picture," not "proven"), would benefit from one explicit sentence noting
that R13's own floor gate — the instrument specifically built to flag
"don't trust a single point's classification here" — is failing at
*every* point inside the disputed region, not corroborating it from
outside. This is a wording refinement, not a defect: nothing here is
mis-scored, since (R1c) is explicitly diagnostic-only and none of this
feeds a CONFIRM/REFUTE band.

## §3. A minor, non-load-bearing code-hygiene finding: Rank 2's `dataset` is hand-retyped, not loaded, from already-machine-readable source

`run.py`'s Rank 2 block hardcodes the seven `(theta, ratio_k)` pairs as a
literal Python list (`dataset = [(36.0, 2.642368e0), ...]`) rather than
loading them from `experiments/090-.../results.json::table1`, even though
the `exp090` module is already imported in this same file and its
`results.json` is sitting one `json.load()` away (exactly the pattern
`run.py` already uses for `exp091`'s and `exp083`'s raw data two blocks
earlier). I checked whether this hand-retyping introduced any actual
error: it did not — every value matches `090-.../results.json::table1`
bit-exact, and I independently re-derived all seven `margin` values from
`exp-083`'s own raw `delta_scene`/`C40_C` a second, fully independent way
(§ above), confirming the numbers are correct regardless of source. This
is not the R4 pattern (a "precisely recomputed" figure asserted in prose
without invoking the function) — it is code hand-typing already-committed
JSON instead of loading it, a milder but structurally adjacent hazard:
nothing here caught it because nothing was wrong to catch, but the next
person to touch this file has no assertion or test tying `dataset` to its
source of truth, only my (and five prior parties') manual cross-check.
Cheap, zero-FDTD fix for whichever future cycle touches this file: load
`table1` from `090-.../results.json` directly, as the two adjacent blocks
already do.

## §4. Everything scoped to be checked, was — no gaps found in scope, sequencing, or disclosure discipline

Specifically confirmed, independent of the three items above: the
mandatory resequencing (Rank 3 before Rank 1) is implemented exactly as
`phase3_synthesis.md` specified, with the branch rule read directly from
`r3_verdict` at runtime, not hand-decided; the empty-leg re-run (Director
fix #8) is real FDTD, not a reuse-in-disguise, and its bit-exact match
against exp-091's own filed `C_empty` values is a genuine, non-trivial
determinism check that passed; the print-parity fix (mandatory-fix docket
item 7) is discharged — all three disclosure strings appear in
`run_output.txt`, confirmed directly, closing the exact gap named one
cycle earlier; the carried-idealizations banner cites 3/6/7/11 at both
the Predictions and Result sections, matching the actual applicable
idealization set (I checked each of the four against what the section
actually says, not just that four numbers are present). No T1/constraint
claim is made anywhere; the N/A framing is accurate to this cycle's actual
content.

## §5. Ranked candidates for Iteration 70

**Rank 1 — close R15's own founding gap: re-fit/rebuild `exp-090`'s
caution zone using the newly-located, now-verified real `cpl=30`
crossings (40.0718°, and 41.7811°/41.8377° or their pair) as direct
inputs, not merely the DROP/RELABEL counterfactuals on the existing `n=7`
labels.** This cycle's own Rank 2 answered "what happens to the zone if
the *existing* label is dropped or flipped" — genuinely useful, but a
different question from "what does the zone look like once the *actual*,
resolution-verified crossing location itself is available as new
information." R15 was adopted specifically because the true `cpl=30`
crossing locations were unknown; they are now known, cleanly, with a
verified (R3-CONFIRMed) sigma_max. This is the single most direct,
already-enabled next step this cycle's own two PRIMARY results jointly
license, and matches `NOTES.md`'s own Next item 1 — I rank it first for
the same reason the write-up does: nothing else on the board more
directly discharges the founding instance of a still-open standing rule.

**Rank 2 — a settling-`STEPS`-doubled spot-check specifically at 41.8°/
42.0°, before (and considerably cheaper than) the fuller off-grid dense
sweep `NOTES.md`'s own Next item 2 proposes.** Both points are the two
`NODE-UNRESOLVABLE` (`floor_pass=False`) points underlying the entire
upper double-crossing finding (§2, above) — the smallest-magnitude
readings this cycle produced, by nearly an order of magnitude at 41.8°.
This is exactly the operating regime this program's own established T27
record (LOGBOOK Iteration 42, `experiments/065-...`) already showed can
sign-flip under under-settling, not merely shift in magnitude — a
directly on-point precedent, not a generic caution. A 2-call (or 4, both
configs) doubled-`STEPS` check at these two specific angles is the
cheapest available test of whether the double-crossing is genuine
near-field structure or a settling artifact, and answers that question
before committing to a more expensive denser off-grid sweep whose own
value depends on the double-crossing being real in the first place. This
was named as discretionary and declined on budget grounds when Red Team
raised it in exp-092's own Phase 2 (`phase2_redteam_audit.md` §3 RT-2) —
at that time no low-magnitude near-null feature was known to exist at
these exact angles; this cycle's own Rank 1 result now supplies the
concrete reason to fund it that did not exist when it was declined.

**Rank 3 — extend Rank 3's own sigma_max-contamination check to angles
near the newly-located crossings themselves (≈40.0°–40.1°, ≈41.8°), not
only the three original census points (37.2°/40.2°/41.4°).** Rank 3
CONFIRMed cleanly and with comfortable margin (all six cells inside
`[0.3,3.0]`, none near either edge) — a real, well-evidenced result I do
not doubt directionally. But the three tested angles are not the
crossing locations this cycle went on to discover; 40.2° sits only
`0.128°` from the now-known lower crossing (a reasonable proxy) while
41.4° sits `0.38°`–`0.44°` from the upper pair (a weaker one), and
`NOTES.md`'s own Idealization 11 already discloses, in the abstract, that
"a Rank-3 REFUTE or NEITHER-default reopens Rank 1's own net-placement
logic... under a corrected article" — the CONFIRM outcome makes that
disclosure procedurally moot for choosing `sigma_max` this cycle, but it
does not empirically test whether the sigma-sensitivity conclusion itself
still holds *at* a real interference node rather than near one. Given
this sub-thread's own repeated pattern (a channel can look robust several
tenths of a degree from a node and still misbehave closer in — the exact
shape R15 itself was founded on), a cheap (2–4 call) check exactly at the
newly-known locations would close the residual, currently-untested
version of this question with real data rather than proximity-based
extrapolation from the existing CONFIRM.

Still open, unaffected, not re-ranked ahead of the above (carried
verbatim from `NOTES.md`'s own Next §, independently checked none is
being silently dropped): extending the search past 42.0° (the true upper
picture beyond the window edge remains unknown); PHOTONICS' own
grazing-incidence validity check (still the single most-repeated item on
the whole T28 board); the x-wall wavelength-generality leg (well past
sixteen consecutive cycles deferred); the still-queued R14(b) formal
null-controlled period fit; the Rank-2-in-`exp-090`'s-own-queue unbiased
margin-vs-distance rebuild on the full 31-point window; a `cpl=40` third
resolution point; extending R3 to the remaining four of `exp-090`'s seven
caution-zone points; the structural/governance items (persisting
`sigma_ext_cells`/`ratio_abs_ext_raw` forward); the ritualization
governance question (Iteration 61), still unresolved.

## §6. Checkpoint criterion check

No criterion fires. **Criterion 4** (program-integrity drift): none of
§§1–3 above is a "known, named, ignored" defect — §1 is a confirmed-clean
self-catch already in `NOTES.md`'s own Learned section; §2 is a wording
refinement on an already-hedged, already-disclosed claim, not a reversed
verdict; §3 is a first-instance, non-load-bearing code-hygiene
observation with zero actual error found, caught blind before this
LOGBOOK entry. No constraint claim is made anywhere (T1 route N/A,
independently reconfirmed accurate to this cycle's content, §4 above), so
no constraint-3 erosion risk exists to fire on. **Criterion 5** (two
non-advancing cycles): N/A — exp-091 was itself logbook-advancing (R15
adopted), and this cycle cleanly locates the crossings R15's own founding
instance left as its single most consequential open question, with a
CONFIRMed, well-margined sigma-validity check as a bonus clean result —
logbook-advancing by a wide margin, not a borderline call.

## Overall soundness verdict

**Sound, cleanly.** Across three independently re-derived headline
computations (the two required by this review's own brief, plus a third
I added covering the `cpl=20` comparator baseline and a ninth independent
reproduction of Rank 2's table), I found zero numeric or logical
discrepancies anywhere in `results.json`, `run_output.txt`, or `NOTES.md`
against the actual committed code and raw data. The three findings above
are a mechanical-label completeness note the document already self-flags,
a wording-strength refinement on an appropriately-hedged claim, and a
non-load-bearing code-hygiene observation with no error found — none rises
to a correction. This is the cleanest single-cycle record I can construct
for this sub-thread's own history of near-misses (the R4/R13/R14/R15
lineage this program's own registry is built from): a genuinely
well-verified proposal, faithfully and fully implemented, producing a
real, informative, honestly-reported split result.
