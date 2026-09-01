# Panel Iteration 76 — Phase 5 Review (VISION SCIENCE)

*Fresh sub-agent, blind to every other seat's Phase-5 output, per PANEL.md
independence mechanics. Charter: human perceptual limits — contrast
thresholds, luminance edge detection, spectral sensitivity, adaptation,
temporal sensitivity, saccadic/attentional blindness. Duty: pin numeric
thresholds, with sources, BEFORE any run that scores against them. exp-099
is T28 house-discipline/instrument-trust work (NOTES.md says so explicitly,
Idealization 7) — no ambient-contrast, adaptation, or temporal-sensitivity
claim is scored anywhere in this cycle for this seat's numeric thresholds to
bind against. That makes this review's center of gravity record hygiene,
banner/idealization coverage, and whether any claim implicitly touches a
perceptual question without flagging it — the lens this seat's own Phase-2
critique this cycle, and its own precedent at Iteration 74/exp-097, already
established for this sub-thread.*

## 1. Independent spot-verification

Five load-bearing claims, each re-checked directly against the committed
record (git log, `results.json`, `run.py`, `run_output.txt`), not taken on
NOTES.md's word:

**(a) Predictions genuinely frozen before results.json existed.** `git log`
on this directory shows a clean, ordered commit chain: Phase 1 (`a1dd0fc`)
→ four Phase-2 critiques (`a249234`, `6e63646`) → Red Team's Phase-2 audit
(`4948171`) → Phase 3/NOTES.md synthesis, **commit message literally reads
"predictions frozen"** (`1e3d0ba`) → `run.py` implementing that frozen spec
(`e6ad59b`) → a mid-run checkpoint (`d9f1006`) → a KeyError fix + relaunch
(`79c29ca`) → Phase 4 close with `results.json`/Result section (`b5e40fd`).
The Predictions section (`NOTES.md`) predates any FDTD execution by
timestamp and by content — confirmed, not merely asserted.

**(b) The mandatory carried-idealizations banner appears in all three
required places.** Per this sub-thread's own standing rule (CHECKPOINT
Iteration 65, adopted after this seat's own R14/R16-adjacent finding at
exp-088): the banner must appear at *both* the Predictions section and the
Result section, not merely once. Direct text check: the banner sentence
appears verbatim (with the correct idealization-number union, 1/7/17/38/
39/42/46/49/53–61) at the close of §Idealizations, again physically
duplicated inside §Predictions' own body (line "Carried idealizations
banner (duplicated here into the Predictions section body itself, per Fix
7...)"), and again inside §Result ("this section is governed by
Idealizations 1/7/17/38/39/42/46/49/53–61... restated here per this
program's own house discipline (VISION SCIENCE's originating fix,
exp-098)"). **Clean — no gap on the exact defect class this seat's own
prior-cycle work created the rule to prevent.**

**(c) Every one of Red Team's seven mandatory Phase-2 fixes is actually
implemented in `run.py`, not merely described in NOTES.md prose.** Checked
each against source: Fix 1 (R5 fault-injection re-scoring) —
`run_r5_fault_injection_rescoring()` runs the full positive-control/FI-A–D/
FI-E/F/H idiom at `family="R5"` before any real R5 call, gates on
`step0["all_as_predicted"]` via a hard `assert`. Fix 2 (far-from-null R5
ground-truth check) — Step 1 spends 4 calls at θ=36.0°, compares sign
against `experiments/094-.../results.json` pulled at runtime, gates Step 3.
Fix 3 (priced HALT outcome) — the Predictions table carries an explicit
"No confident lean... HALT is a live, disclosed possibility" row for
`xi_ext`/`sigma_abs_nonneg`, and the code's own `assert xi_pass`/`assert
nonneg_pass` are present at the claimed lines. Fix 4 (corrected angle
labels) — `NULL_C_FILED_KEYS = sorted(float(k) for k in NULL_C_FILED.keys())`
pulls the true stored keys; no hand-typed `"41.294235"`/`"41.627568"`
anywhere in `run.py`. Fix 5 (period-gated VANISHING-AMPLITUDE) —
`period_criterion_met = bool(half_width_c >= DELTA_SCENE_PERIOD_DEG)` with
`DELTA_SCENE_PERIOD_DEG = 2.9474`, correctly gating the verdict branch. Fix
6 (θ₀ digit correction) — `THETA0_C` is pulled from `j090` at runtime, not
hand-typed at all in `run.py` (the hand-typed digit only ever lived in
Phase 1 prose, now corrected in NOTES.md's own citation). Fix 7 (banner
duplication) — confirmed under (b). **All seven land; none is a
paper-only fix.**

**(d) Every headline number in NOTES.md's Result section reproduces exactly
from `results.json`/`run_output.txt`.** Independently recomputed/re-read
(not trusted): item 1's 7-point `delta_scene` table, `r_ratios =
[1.331674, 0.283377]` (NOTES.md's "r₄=1.332"/"r₅=0.283"); item 2's
Step-1 sign (`-1.064305e-03`, negative, match=True), Step-2 `rel_dev=
0.1786%`, Step-3 crossing `θc50=39.776870°`, `shift_40_50=-0.144649°`, and
the Richardson figure (`observed_ratio=0.962283`, `naive_order2_ratio=
0.64`); item 3's five new `ptp` values and ratios (`849.8×`/`853.7×`/
`709.9×`/`503.2×`/`291.7×`) and the `gp2_tail_any_valid=False`,
`min_ratio=12.222×`, `max_ratio=78.534×` figures. **Every digit checked
matches to the last printed place.** `fdtd_calls=40`, matching the
pre-registered PASS-path total exactly (R19's own call-count/row-count
discipline holds here — 40 calls map to a fully-enumerated, cross-checked
job list, not a bare total).

**(e) A genuine gap: the Result section's "bit-identical, directly diffed"
verification claim is not itself reproducible from the committed record.**
NOTES.md's Result section states the crashed run's item-1 console output
was "directly diffed, this shift, against the crashed run's own console
capture" and found bit-identical to the successful re-run — offered as the
evidentiary basis for "no data was lost or altered." I checked what
*is* committed: the mid-run checkpoint commit (`d9f1006`, message: "Committing
the partial log now to satisfy the stop hook's untracked-file check") is
only 12 lines long and stops immediately after item 1's own launch banner
("new angles=[...]") — **before any of the 12 calls' per-theta output, let
alone the crash itself, was ever committed.** No artifact anywhere in this
directory's git history preserves the crashed run's completed item-1
console output for a future reader to re-diff. The underlying claim is very
likely true (I independently confirmed the final `results.json` values are
internally self-consistent and pass every downstream computation cleanly,
which is what a genuine crash-confined-to-a-lookup-bug predicts), but the
*specific verification method cited* — a direct diff against a preserved
console capture — cannot be independently re-run or audited from what is
actually in the repository. This is the same failure shape this program's
own R4/R9 lineage exists to police (a claimed exact/independently-verified
comparison that does not, in fact, reproduce from committed sources),
applied here to a claim *about the verification process itself* rather
than a physics figure — the same shape this sub-thread caught once before
at Iteration 71/exp-094 (Gate 5's own fault-injection provenance claim, "no
corresponding artifact anywhere in the committed record"). Non-load-bearing
(no scored verdict rests on it), but real, and it recurs in a document that
elsewhere goes out of its way to earn "not hand-typed"/"re-read this
session" trust for its arithmetic.

## 2. Steel-man

This is genuinely careful, well-gated work, and the panel's own layered
review process visibly did its job. The three-way convergent Phase-2 attack
on item 2 (MATERIALS' R15-addendum citation, QUANTUM's fault-injection-
coverage gap, EM's unpriced-HALT gap) is real, independently sourced by
three different methods against three different files, and Red Team's own
audit correctly ruled it mandatory rather than a courtesy fix — R5's first
real FDTD spend in this program's history was not allowed to proceed on
inherited trust alone. The result vindicates the caution without making it
look wasted: Step 0's fault injection and Step 1's ground-truth check both
passed cleanly, and Step 3 then delivered a genuine, cleanly-bracketed sign
change plus a second independent Richardson data point at Null B — real
scientific content, not merely a validated instrument sitting idle. Item
1's disclosed "bounce" (a genuine local trough, not a stall, not a
crossing) is exactly the kind of honestly-reported partial result this
program's own house discipline asks for, and item 3's non-resolution is
reported as such rather than forced toward either falsification branch —
both are the correct scientific behavior when the data don't cooperate.
Notably absent this cycle: any recurrence of this sub-thread's own
four-times-fired disclaimer-erosion lineage (Iterations 53/63/64/65) — the
carried-idealizations banner is clean at all three required locations (§1
above), and no perceptual/constraint-3 claim is smuggled in anywhere
without its governing Idealization 7 disclaimer attached.

## 3. Sharpest finding

**Three of the five blind Phase-2 critiques exceed PANEL.md's own ≤150-word
cap on at least one of their two mandatory prose sections, and Red Team's
Phase-2 audit — which sees all five and exists precisely to catch this —
did not flag it.** PANEL.md's Phase-2 format is explicit: "one steel-man
(≤150 words), one sharpest attack (≤150 words)." I counted each section
directly (header-to-header, excluding the header line itself):

| Critique | Steel-man | Sharpest attack |
|---|---|---|
| PHOTONICS | 117 | **182** (+32, 21% over) |
| MATERIALS | 135 | **151** (+1) |
| ELECTROMAGNETISM | **152** (+2) | 127 |
| QUANTUM OPTICS | 96 | 149 |
| VISION SCIENCE (this seat, Phase 2) | 145 | 135 |

PHOTONICS' sharpest-attack section is 21% over cap — not a rounding
question. This is not a novel defect class for this sub-thread: at
Iteration 74 (exp-097), this exact seat caught "four of five Phase-2
sharpest-attack sections exceeded the ≤150-word cap," logged into that
cycle's own record. That precedent means the pattern is *known* to this
program, yet it recurred two cycles later, past a Red Team Phase-2 audit
that explicitly claims to have "independently re-verified every
load-bearing claim... against source" for physics content but performs no
equivalent check on the format cap PANEL.md itself imposes on the
documents it is auditing. The content of the over-length sections is not
in question — PHOTONICS' 182-word attack (the "established-oscillation-
vs-decay conflation" finding, correctly adopted as mandatory Fix 5) is
substantively excellent and load-bearing to the cycle's own outcome; this
is a pure format-discipline lapse, not a physics defect, and does not
change any adopted fix or any scored verdict. But it is exactly the kind
of "known, named, ignored" recurrence shape (a defect class this program
has already caught once, recurring unflagged by the layer meant to catch
it) that this program's own R-rule lineage treats as worth naming even
when it does not clear a firing bar — logged here so a third recurrence
does not go unnoticed a second time.

## 4. Secondary finding

The Result-section verification claim identified at §1(e) above — a "bit-
identical, directly diffed" comparison that cannot be reproduced from any
committed artifact. Recommend, forward: when a mid-run crash is disclosed
and its harmlessness argued from a console diff, either commit the crashed
run's own terminal capture (even as a throwaway `*.crash.txt`) before
fixing and relaunching, or state explicitly that the comparison was
performed in-session and is not independently re-auditable from the repo —
the current phrasing ("directly diffed, this shift") reads as the former
without being the latter.

## 5. Tertiary finding — a forward risk on this seat's own charter

THERMODYNAMICS' own §T1 disposition (ratified without attack) commits
Iteration 77 to "an actual constraint-1/2/3/4 scoring pass treating the
now-more-fully-characterized `delta_scene(θ)` sign structure as an
angular-selectivity parameter." If that trigger is honored, it will be the
first run in this program's history to score `delta_scene(θ)` — an
instrument-validation quantity built and stress-tested entirely inside
this T28 desk sub-thread — against this seat's own perceptual-threshold
machinery (`C_thr(L)`, T2's frozen function; the T16 angular-quadrature
uncertainty budget; T21's edge-diffraction fringe/contamination risk; T24's
`ABSORB`-boundary systematic; T27's settling-convergence standard; R13–R15's
floor/resolution-sensitivity gates). Rotation puts QUANTUM OPTICS in the
lead seat for Iteration 77, not VISION SCIENCE — meaning the seat charged
with correctly invoking this instrument stack will not be the seat that
built and owns it. This is not a defect in exp-099 (nothing here proposes
running that pass without it), but it is a concrete, nameable risk this
seat's own charter duty ("pin numeric thresholds... BEFORE any run that
scores against them") exists to flag now, before Iteration 77 drafts a
proposal: the constraint-3 scoring pass, whenever it runs, must cite
`C_thr(L)` and the established floor/uncertainty gates by their existing,
already-pinned form — not re-derive or silently drop any of them.

## 6. Verdict: **CONCUR-WITH-GAP(S)**

The science is sound, honestly reported, and correctly gated — nothing
here would move a verdict or block the cycle. Two real, non-load-bearing
record-hygiene gaps (§3, §4) keep this out of a clean CONCUR: a recurring,
previously-named defect class (Phase-2 word-cap overruns) went uncaught a
second time, and one verification claim in the frozen Result section
cannot be independently re-audited from what is actually committed.

## 7. Ranked top-3 candidate directions for Iteration 77

Independently reasoned from this seat's own charter, not deferring to
NOTES.md's own draft Next section (though it substantially overlaps with
draft item 2).

**1. Execute the constraint-1/2/3/4 scoring pass now — do not let this
become an eighth consecutive T1-route-N/A cycle.** I agree with, and rank
above everything else, THERMODYNAMICS' own trigger: `delta_scene(θ)`'s
sign structure should be run, for the first time, through the actual
phenomenon-scoring instruments (`emit.observer_record`, `lab/ambient.py`,
the beam-behind box) as an angular-selectivity mask candidate. This
sub-thread has produced thirty-plus iterations (exp-069 through exp-099) of
genuinely rigorous instrument-trust work and essentially zero forward
motion on PANEL.md's own target phenomenon; T1 has read N/A for seven
straight cycles. That is not, on its own, a Checkpoint-5 violation (each
cycle has produced a real, logbook-advancing narrowing), but the honest
frame this program answers to (Marsh's own mandate; PANEL.md's stop
conditions) does not tolerate an indefinitely-deferred phenomenon test
behind an indefinitely-improving instrument. Per §5 above, whichever seat
leads must correctly inherit this seat's own pinned `C_thr(L)`/floor-gate
machinery rather than re-derive it from scratch.

**2. Null C's genuine trough, tested at the full ≥2.9474° half-width**
(concurring with NOTES.md's own draft item 1). This is legitimate,
well-motivated T28 instrument work — the bounce this cycle found is new
information, not a resolved question — but I rank it below item 1
specifically because it is *more of the same instrument-validation
category* this sub-thread has run for thirty cycles; if scope pressure
forces a choice between this and item 1, item 1 should win.

**3. A short, VISION-owned pre-flight note (not a full FDTD cycle)
cataloguing exactly which of this program's own established perceptual/
instrument caveats bind the moment `delta_scene(θ)` is first scored as a
constraint-3 mask — before Iteration 77's proposal is written, not
folded into it after the fact.** This directly discharges this seat's own
charter duty ("pin numeric thresholds, with sources, BEFORE any run that
scores against them") in concrete form: which `C_thr(L)` parameterization
governs at the relevant photopic/scotopic regime, which of T16/T21/T24/T27's
own uncertainty budgets and floor gates apply to a `delta_scene`-derived
mask specifically (none of them were built with this quantity in mind),
and which constraint tier (Tier-W vs. Tier-A) a first pass should even
target. Cheap, zero-FDTD, and removes the single most likely way item 1's
own scoring pass could ship a perceptually uncalibrated or uncaveated
result on its very first attempt.

Not re-proposing: any RULED-OUT idea (R1–R19 read in full this session).
The Richardson-pattern-generalization-to-Null-A and GP2′/`ptp`
direct-recompute items in NOTES.md's own draft Next (items 3–4) are
legitimate but sit outside this seat's own charter's center of gravity —
noted, not ranked, deferring to PHOTONICS'/QUANTUM's own seats to weigh
them.
