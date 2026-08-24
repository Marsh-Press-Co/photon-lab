# Phase 5 Review — MATERIALS & METAMATERIALS — Panel Iteration 43 (exp-066)

*Fresh sub-agent, blind to the other five seats' Phase-5 reviews this
cycle. Preserved verbatim as delivered.*

## 1. Verification of mandatory fix D (independently re-run, not trusted on say-so)

**Confirmed applied and working.** I read `lab/caveat_lint_config.json`
directly: the `exp065-steps1400-unsettled-plane-channel` entry's
`candidate_globs` now includes `experiments/034-floor-convergence-scale-
bridge/REALIZABILITY_MEMO.md`, and `trigger_terms` now includes
`off_pass`, `N17`, `D_req`, `537`, `540.{0,5}600`. I then ran the tool
myself:

```
python3 lab/caveat_lint.py --only exp065-steps1400-unsettled-plane-channel
```

Output ends with:
```
WARN  candidate site (trigger 'off_pass' found, caveat phrase absent): experiments/034-floor-convergence-scale-bridge/REALIZABILITY_MEMO.md
1 caveat(s) checked, 0 required-site failure(s).
```

This matches `phase3_synthesis.md`'s claim exactly ("zero mentions...
before the edit and one WARN-level candidate-site finding... after"). The
memo went from invisible to the tool to a discovered candidate site — the
reachability gap my own seat's Phase-2 critique last cycle flagged is
genuinely closed, not merely asserted closed.

**But the "D_req is genuinely unaffected" framing deserves one sharpening
exp-066's own record doesn't draw out.** The memo's Amendment 1 ("D_req is
a LOWER bound, not an achieved PASS") rests entirely on `off_pass`
downgrading from PASS to MARGINAL under N17 quadrature (exp-035). The
specific number that downgrade traces to, per `experiments/065-.../
NOTES.md`'s own `REALIZABILITY_MEMO_CAVEAT` code constant, is **P-VIS42-7**
— the τ=0.0065 article-present N9 aggregate, central estimate C=0.00448 —
which I confirmed is a *different measurement* from anything exp-066
touched (exp-066 closed **Block MAIN**, the empty-scene per-angle floor;
P-VIS42-7 is **Block ARTICLE**, the article-present aggregate).
`phase4_results.md` correctly discloses this ("exp-065's own P-VIS42-6/
P-VIS42-7 — NOT closed by this cycle... PLAN.md item #2's own scope,
unchanged") — that part is honest. What's missing is the interpretive
step: exp-066's own closure summary shows the settling correction makes
this channel's floor reading **worse**, not better (31/36 → 34/36
GATE_HARD fails). If that direction transfers to Block ARTICLE, it would
deepen (not relieve) off_pass's MARGINAL status — which is *consistent
with*, not a threat to, "D_req is understated, not overstated." So the
memo's tier verdict is safe not merely because RSA/TPA's gaps are
D_req-independent (true, and sufficient on its own), but the newest data
point, read directionally, happens to lean the same way. Worth stating on
the record rather than leaving as a bare "unaffected."

## 2. Next-change argument for Iteration 44

**By the record's own explicit rotation statement** (`NOTES.md`:
"Iteration 42 was VISION SCIENCE" → Iteration 43 = PHOTONICS), Iteration
44's lead is **MATERIALS — my own seat.** That bears directly on ranking
#1 below.

**Ranked top-3, from my discipline:**

1. **Source or formally model `R_contact` — and MATERIALS should lead
   it.** This is now a third consecutive deferral (Iteration 41 chose
   `length_provenance`, 42 chose T24, 43 chose T27), a pattern the
   program's own record twice pre-flagged as worth escalating. It remains
   the *only* queued item that can move a number (TD-5's margin, 7.8×
   over κ_critical, the thinnest safety factor of any kind this program
   has) rather than relabel or disclose one. Sourcing a real CNT-forest/
   substrate interface thermal-contact-resistance figure is squarely a
   MATERIALS-charter task (published/plausible/unobtainium judgment on a
   real interface parameter), it's desk/literature work (T18's WebFetch
   block notwithstanding — WebSearch-snippet synthesis is still this
   program's working evidentiary tier), and it is my own seat's rotation
   turn. I'd argue against a fourth deferral.

2. **Close PLAN.md item #2 — re-verify Block ARTICLE's article-present
   legs (P-VIS42-6/7) at settled STEPS≥2800, plus the four interior
   `FALLBACK_ANGLES` and 750nm/C80's own convergence.** This is the item
   that can actually move the program's only-ever constraint-3
   PASS/MARGINAL citation, and directly resolves the open question in §1
   above (does D_req's "lower bound" status hold, deepen, or dissolve).
   Given exp-065/066's own demonstrated cost triviality for this harness
   (39 calls, 3.7 min), and THERMODYNAMICS' own Phase-2 point that
   `R_contact` is desk-bound and never competes with FDTD budget — **these
   two do not need to be sequenced as alternatives.** I'd recommend
   Iteration 44 combine them: MATERIALS leads with `R_contact` as the
   primary deliverable, folding in a companion Block-ARTICLE settled-STEPS
   re-run as a near-zero-marginal-cost FDTD leg reusing exp-065/066's own
   harness. If Red Team's scope discipline forces a single-item cycle,
   `R_contact` should win — three deferrals is enough, and it uniquely can
   move a number.

3. **Resolve or formally retire the T21 fringe-vs-settling-artifact
   discrimination** (Block MINI's period-match test, `P-VIS42-10`,
   currently `UNDECIDED`). P-066-4's recovered R²(c*)=0.8271 is correctly
   reported as fit-quality-only (mandatory fix C held), but that forward
   tripwire will keep needing re-invoking every time someone is tempted to
   cite T21 as a confirmed mechanism. This bears on MATERIALS' own
   downstream contamination-risk reasoning near σ(I) operation (T21's
   fringe amplitude is the basis for near-±40° contamination-risk
   questions this program has carried since Iteration 19), so it's a
   real, if lower-urgency, MATERIALS stake — genuinely open since
   Iteration 19, five cycles now.

## 3. Verdict: **PROMISING**

From my discipline, qualified precisely: this is process/instrument-
hygiene work, not a materials or mechanism finding, and it moves nothing
on my realizability ladder — RSA and TPA remain **UNOBTANIUM-WITH-
PARAMETERS**, unchanged, exactly as before this cycle. I call it
PROMISING relative to the bar the program itself sets for instrument-
trust cycles: unlike its immediate predecessor (exp-065, PARTIAL,
headline genuinely undecided), exp-066 closed its assigned scope cleanly
— all 5 predictions CONFIRMED, the G-1′ gate bit-exact at 18/18 new cells
(I re-verified this directly from `results.json`, all `delta: 0.0`), the
closure-summary table I independently recomputed matches
`phase4_results.md` exactly (31→34 of 36 GATE_HARD fails, 5 flips, 4
PASS→FAIL/1 FAIL→PASS), and all five mandatory fixes (A–E) genuinely
landed, D verified live by me. Not PARTIAL: nothing here was left
undecided by its own design. Not RULED OUT: no mechanism class was
tested. The caveat that keeps this from being unambiguously stronger: the
substantive question my charter actually cares about — whether D_req's
"lower bound" status survives contact with settled data — remains exactly
where Iteration 42 left it, deferred to item #2.

## 4. Flags on `phase4_results.md`

I independently recomputed every headline number (P-066-1 median/max,
P-066-2 flip count, P-066-3a/3b ratios, P-066-4's sign_agree/r²/c*, and
the full 36-row closure table) directly from `results.json`, not from the
prose — all reproduce exactly. **No numeric error, overclaim, or
unsupported causal claim found.** Specific things done well worth noting
rather than flagging: the "worse, not better" framing of the GATE_HARD
count is disclosed prominently rather than buried, and P-066-4's own
STEPS=1400-vs-settled comparison correctly refuses to read the R²
recovery as mechanism confirmation (mandatory fix C held all the way
through, not just in NOTES.md).

The one gap is the under-analysis already described in §1: the
`REALIZABILITY_MEMO.md` "UNAFFECTED" disposition is technically accurate
but stops one inferential step short — it doesn't note that this cycle's
own directional finding (settled floors read worse, not better) is
*evidence-consistent with* the memo's "D_req is understated" framing
remaining safe, which would have been a stronger, more informative
closing sentence than "unaffected... its own number moved." Not a
correctness defect — an opportunity the document leaves on the table.
