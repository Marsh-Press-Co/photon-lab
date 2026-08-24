# Phase 5 Review — QUANTUM OPTICS Seat, Panel Iteration 43 (exp-066)

*Fresh sub-agent, blind to the other five seats' Phase-5 reviews this
cycle. Preserved verbatim as delivered.*

## 0. Scope and method

I read LOGBOOK.md's RULED-OUT/ESTABLISHED/LIVE-THREADS sections and the
Iteration 42 entry in full, PANEL.md in full, VALIDATION.md in full,
PLAN.md's current-state and queue sections, exp-065's P-VIS42-10 verdict
(still `UNDECIDED`, confirmed live in `experiments/065-t24-absorb-
boundary-sweep/results.json`, untouched by exp-066), and every document
in `experiments/066-t27-block-main-settling-reverification/` — proposal,
all five Phase-2 critiques, the Red Team Phase-2 audit, the synthesis,
NOTES.md, `design_geometry.py`, `run.py`, `results.json`, and
`phase4_results.md`. I independently loaded `results.json` and
cross-checked the headline numbers (P-066-4's fit statistics, the
closure-summary GATE_HARD counts, the five bucket-flip rows) against the
prose in `phase4_results.md` rather than trusting the write-up's own
tables.

## 1. Literal read: does P-066-4's language slip anywhere?

**No. I checked every site and found the line held everywhere, including
inside `results.json` itself, not just the prose documents.**

- **`design_geometry.py`**, `FRINGE_FIT_STATISTICAL_ONLY_NOTE` (lines
  142–157): *"It makes NO claim about which physical mechanism, if any,
  the fit quality establishes — a recovered R^2 does not, by itself,
  distinguish a genuine coherent edge-diffraction fringe from the
  settling artifact's own (theta,lambda)-dependence correlating with the
  fringe model's own geometric clock A*cos(theta)... no future citation
  of this refit's R^2 may be read as 'confirmed edge-diffraction/
  coherent-fringe mechanism' while Block MINI's period-match test
  (P-VIS42-10, exp-065) remains UNDECIDED."* This is my own exp-065
  tripwire, extended, quoted verbatim into code — the exact fix I asked
  for.
- **`run.py`** (line 386): the verdict string is built programmatically
  as `"CONFIRMED (fit quality recovered, no mechanism claim)"` /
  `"REFUTED (fit quality degraded, no mechanism claim)"` — the disclaimer
  is baked into the verdict string itself, not just the surrounding
  prose, so it cannot be stripped by a future citation that quotes only
  the verdict.
- **`results.json`** (`scored.P-066-4.verdict`): confirmed live —
  `"CONFIRMED (fit quality recovered, no mechanism claim)"`, and the
  `statistical_only_note` field carries the full disclaimer text
  verbatim, so the machine-readable artifact itself, not only the
  human-readable write-up, resists mis-citation.
- **`NOTES.md`** (P-066-4 prediction, lines 144–153): *"Makes no claim
  about which physical mechanism, if any, the fit quality establishes."*
  Held at prediction-freeze, before the run — this is the pre-registered
  text, unchanged by the result.
- **`phase4_results.md`** (lines 82–91): *"Per mandatory fix C, this is
  reported and should be cited ONLY as a statement about fit quality...
  It is **explicitly not** evidence that the underlying mechanism is
  genuine coherent edge-diffraction rather than settling-transient
  content correlating with the same geometric clock... Block MINI's
  period-match test (P-VIS42-10, exp-065) remains UNDECIDED, unchanged by
  this cycle."* This is the strongest-worded passage in the whole packet
  and it is the one under the most temptation (numbers improved) — it
  holds.
- The one place I scrutinized hardest for creep — the `c*` shift
  discussion (phase4_results.md lines 93–99): *"consistent with (not
  proof of) the settling artifact having previously been inflating the
  measured amplitude relative to the diffraction model's own un-rescaled
  prediction, but this cycle does not adjudicate that reading."* This is
  a borderline sentence — it does offer a directional interpretation
  (which quantity was inflated) — but it stays on the settling-artifact
  side of the disclaimer, not the coherent-fringe-mechanism side, and it
  is explicitly hedged twice in one sentence ("consistent with, not proof
  of" / "does not adjudicate"). It does not violate mandatory fix C's
  specific scope. I flag it only because it is the closest anything in
  this packet comes to interpretive language, and a future citation
  lifting that clause out of context without the hedges would be a real
  risk — worth naming in the caveat-lint entry's `phrase_patterns` if it
  isn't already covered (it currently is not — `phrase_patterns` covers
  "coherent-fringe perturbation" and settling-confound language but not
  "inflating the measured amplitude").

I also independently re-derived the numbers rather than trusting the
prose: `results.json`'s `fringe_fit_refit.sign_agree=30`,
`r2_cstar=0.8270797090069711`,
`original_steps1400_fit.r2_cstar=0.7852421354715854` — matches
phase4_results.md's table exactly (0.8271 vs 0.7852, Δ=+0.042). The
closure-summary's `n_fail_1400=31`/`n_fail_2800=34` and all 5
bucket-flip rows I spot-checked against the raw `C_1400`/`C_2800` values
match the prose table cell-for-cell. **Nothing hand-typed, nothing that
doesn't reproduce from the committed artifact (R4 compliance verified
independently, not just asserted).**

**Verdict on this check: mandatory fix C held completely.** Better than
exp-065's own failure — that time the verdict *string* asserted a
mechanism nobody coded a test for; this time the string, the note, the
prediction, the results.json field, and the prose all say the same
disclaimed thing, redundantly, in a way that makes it harder for a future
careless citation to find an unguarded quote.

## 2. Next change — ranked top-3 from QUANTUM OPTICS' charter

**Does the improved fit quality make Block MINI's period-match test MORE
or LESS urgent? MORE — unambiguously, and for a specific reason beyond
"it was already queued."**

Before this cycle, a future citation reaching for "T21's fringe is real"
had to explain away a mediocre 27/30 sign agreement and r²=0.785 fit to
unsettled data — a citation risk that was at least self-limiting, because
the fit itself looked shaky. Now the identical unresolved ambiguity
(settling-transient content vs genuine coherent edge-diffraction, both
driven by the same `A·cos θ` clock) sits underneath a **clean 30/30
sign-match and r²=0.827 on settled data** — a much more citable-looking
number, attached to a disclaimer that lives in prose and JSON fields
rather than in anything that stops a future Phase 1 proposal from quoting
"r²=0.83, 30/30 sign agreement" without the surrounding sentence. This is
exactly the shape of risk my own charter exists to police: better numbers
create more temptation to over-claim, not less, and the discipline
holding this cycle's language in check is entirely human/procedural
(mandatory fix C, the tripwire, this review), not mechanical. The one gap
I can point to concretely: `lab/caveat_lint_config.json`'s
`exp065-steps1400-unsettled-plane-channel` entry's `phrase_patterns`
still targets "coherent-fringe perturbation" but not the specific numbers
this cycle produced (`r2_cstar`, `0.8271`, `30/30`) — a future citation
of just the number, stripped of the word "perturbation," would not trip
the lint.

**Ranked top-3:**

1. **Implement Block MINI's period-match test for real, at settled STEPS
   (≥2800), with enough angular density to actually test periodicity —
   the single instrument that can adjudicate this question, still
   unbuilt after two consecutive cycles of deferral.** exp-065's own
   attempt used 5 points spanning ~1 T21 period (too underpowered even in
   principle, honestly disclosed as such). The correct design needs ≥2–3
   periods (T21 period ≈1.989° at 40°/600nm per this cycle's own
   committed number) at ~0.2° spacing, run at STEPS=2800 not 1400, so the
   measurement isn't itself contaminated by the artifact under test. This
   is now Iteration 44's single highest-value item from my charter's
   perspective, precisely because this cycle's improved numbers raise the
   cost of leaving it undone.
2. **Use this cycle's own 36-cell settling-delta dataset (`C(1400)−
   C(2800)`, already committed, zero new FDTD cost) as a second,
   independent discriminator — desk-only.** If the settling artifact is a
   smooth, non-periodic transient (turn-on ramp, or a monotonic
   margin-periods decay), its delta should NOT itself show `A·cos θ`-
   periodic structure matching the T21 fringe's own period. If it does
   show that structure, that's evidence the "settling artifact" is itself
   a coherent multi-path transient (see #3), which would reopen rather
   than close the mechanism question. This is a genuinely free test this
   cycle's own data licenses and nobody has run yet.
3. **Test whether the STEPS-dependent residual is itself a coherent
   physical effect (multi-path/aperture-edge interference settling in
   over the `MARGIN_PERIODS` window) rather than a numerical artifact to
   be waved away as "unsettled."** Red Team's own attack 3 already
   surfaced the better candidate mechanism (exp-042's `MARGIN_PERIODS`,
   thinnest at 750nm, tracking the fit residual's λ-dependence) but
   explicitly did not test it causally. If the transient decay itself has
   oscillatory rather than smooth-monotonic character as STEPS increases,
   that would be squarely inside my charter (a genuinely coherent, not
   numerical, phenomenon) and would reframe "settling artifact" language
   used throughout T27/T24 — worth knowing before that language hardens
   into program vocabulary.

I'd rank #1 above #3 for Iteration 44 specifically because #1 is the one
instrument this program has now deferred across two full cycles (queued
at Iteration 42, deferred again in exp-066's own item #2 split), while #3
is a genuinely new idea this cycle's own Red Team audit surfaced but
nobody has committed to a design for yet.

## 3. Verdict from my discipline

**Partial — process-promising, physics-null.** T1 escape route is
correctly NONE and stayed NONE throughout (verified: no σ(I)/σ(x,t)/
ε(ω)/gain parameter anywhere in `design_geometry.py` or `run.py`); this
is pure instrument re-verification and advances no constraint-3
mechanism claim in either direction. From my charter's narrow lens the
result I most care about — mandatory fix C's discipline — held completely
under real pressure (improved numbers, a T21 fringe-fit result that
*looks* more confirmable than last cycle's), which is itself the finding
worth recording: the program's forward-tripwire mechanism (write the
disclaimer into the verdict string and the JSON, not just the prose)
worked exactly as designed. I concur with the packet's own PARTIAL
framing.

## 4. Flags on phase4_results.md — over-claims, under-disclosures, errors

- **No over-claim found.** Every mechanism-adjacent sentence I traced
  back to a primary number checked out, and the strongest disclaiming
  language (lines 84–91) is also the most load-bearing passage in the
  document — it isn't buried.
- **One under-disclosure, minor, already flagged as deferred rather than
  concealed:** `lab/caveat_lint_config.json`'s `exp065-steps1400-
  unsettled-plane-channel` entry still describes Block MAIN as broadly
  "unsettled pending re-verification" — it has not been updated to
  reflect that Block MAIN's own 30/30 cells are now closed at STEPS≥2800,
  while Block ARTICLE (P-VIS42-6/7) and Block MINI (P-VIS42-10) remain
  open. `phase4_results.md` itself names this explicitly as "a
  Phase-5/close-of-cycle task, not this Phase-4 file's own scope" (line
  118) — so it's disclosed, not hidden, but it is a real to-do this
  cycle's close needs to execute, and its `phrase_patterns` should also
  be widened to catch a bare `r2_cstar`/`0.827`/`30/30` citation stripped
  of the word "perturbation" (see §2 above).
- **No numeric errors found.** I independently recomputed the
  closure-summary GATE_HARD counts (31/36→34/36), all 5 bucket-flip rows,
  and the fringe-fit r²/sign-agree figures directly from `results.json`
  rather than trusting the write-up, and every value matched to the
  printed digit.
- **One legitimate scope caveat, correctly stated, not an error:** the
  write-up is careful that P-VIS42-6/7 (Block ARTICLE, τ=0.0065
  article-present, N9 aggregate) are **not** closed by this cycle — a
  structurally different measurement from Block MAIN's empty-scene
  cells — and does not overstate this cycle's reach onto that separate
  open item. This is exactly right and worth crediting.

**Bottom line for the Director:** mandatory fix C is not just formally
satisfied, it's satisfied in the machine-readable artifact as well as the
prose, which is a genuine improvement in citation-safety over exp-065's
own failure mode. The one thing this cycle's success buys is urgency, not
closure — Block MINI's period-match test is now the more, not less,
load-bearing piece of unfinished business on the books.
