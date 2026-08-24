# PHASE 5 — REVIEW · VISION SCIENCE · Panel Iteration 43 · exp-066

*Fresh context, blind to the other five seats' current-cycle reviews.
This is my thread's direct sequel (I led Iteration 42/exp-065 and opened
T27; I also wrote this cycle's own Phase-2 critique, whose "fold in ±35°
at ~$0 cost" ask became Red Team's mandatory fix A). Preserved verbatim
as delivered. All numbers below were independently recomputed from
`results.json`, not read off the prose.*

## 1. Independent verification of the closure_summary and the GATE_HARD result

I loaded `results.json` directly and recomputed everything by hand rather
than trusting `phase4_results.md`'s tables:

- **`closure_summary`**: `n_fail_1400=31`, `n_fail_2800=34`,
  `n_bucket_flips=5` — recomputed from the 36 raw `(C_1400, C_2800)`
  pairs against `GATE_HARD=0.001`: bit-for-bit match. The 5 flip rows (4
  PASS→FAIL: −39°/450, +37°/450, +39°/450, −35°/750; 1 FAIL→PASS:
  +38°/600) also match exactly, sign and magnitude.
- **G-1′**: recomputed against `experiments/041-t20-angle-audit/
  results.json::block_main` directly — `max|Δ| = 0` across all 18 cells.
  Bit-exact, confirmed.
- **P-066-1/2**: median `|ΔC(2800−1400)|` on the 18 new cells =
  0.005766909912278462 (reported: 0.005767); sign-flip count = 3/18
  (reported: 3). Exact match.
- **P-066-3a/3b**: recomputed both convergence ratios from `block_stress`
  against the corresponding `block_main2800`/`block_g1ext`/`closure_
  summary` values — 0.00976% and 0.000717% respectively, matching the
  reported 0.0098%/0.00072% to the reported precision.
- **P-066-4**: `sign_agree=30/30`, `r²(c*)=0.8270797…` (reported 0.8271),
  `c*=0.8712101…` (reported 0.8712), original-fit figures (27/30,
  0.7852421354715854, 1.6196430704378861) reproduce exp-042's committed
  numbers exactly.

**Everything in `phase4_results.md`'s tables is numerically accurate.**
No fabricated or rounded-away figure found anywhere I checked.

**Does the 31/36→34/36 result threaten any live constraint-3 PASS/
MARGINAL citation? No — but the document doesn't say so explicitly, and
it should.** `GATE_HARD=0.001` is not `C_thr`. This program settled that
distinction the hard way at Iteration 18 (exp-041's own mandatory fix 1,
LOGBOOK.md ~line 7624–7638): `C_thr=0.005` gave "SNR≈1.7, nowhere near
decidable" on these near-grazing cells, so `GATE_HARD=0.001` — five times
stricter — was adopted specifically as the per-angle instrument-floor
decision rule for Block MAIN/SWEEP, explicitly labeled
`GATE_PERCEPTUAL_CONTEXT`/"not a perceptual bar" in exp-065's own Phase-1
proposal (line 239). Block MAIN (36–40°) is also not summed into the N9/
N17 aggregates that actually score constraint-3 (`FALLBACK_ANGLES` is;
only its ±35° cell overlaps, and that cell's sign-flip was already known
and disclosed at Iteration 42). So a worse GATE_HARD count at Block MAIN
does not, by itself, move any PASS/MARGINAL/FAIL constraint-3 verdict —
if anything it *reinforces* exp-041's original rationale for excluding
this whole angular window from the scored aggregate. `phase4_results.md`
never states this reasoning and never uses the words "C_thr" or
"constraint-3" anywhere in its text — it reports the "NET WORSE" headline
correctly and without overclaiming, but by omission, not by an
affirmative disclaimer. Given this program's own repeated history of
exactly this GATE_HARD/C_thr conflation risk (the reason exp-041 needed a
mandatory fix in the first place), I recommend one inline sentence at
Phase 5/close: *"GATE_HARD (0.001) is the instrument-floor gate, not
VISION's perceptual C_thr (0.005); this result characterizes Block
MAIN's excluded fringe zone and does not itself move any constraint-3
PASS/MARGINAL/FAIL verdict."* Zero cost, closes the ambiguity a fresh
reader (like me, cold) could otherwise fall into.

One more small provenance gap: the −35°/750nm PASS→FAIL flip is a
**restatement of an already-known finding** — its C(1400)/C(2800) values
(−0.00095→+0.00552) are the exact numbers T27's Iteration-42 opening
already reported as a sign flip. `phase4_results.md` explicitly notes the
+38°/600nm flip's provenance ("the cell already reported in exp-065's own
headline") but does not extend the same courtesy to −35°/750nm. Minor,
but worth symmetric treatment.

## 2. A live, unfixed gap: the caveat-lint registry entry itself is stale

I read `lab/caveat_lint_config.json`'s `exp065-steps1400-unsettled-
plane-channel` entry directly (git-confirmed last touched at commit
`1a90ecf`, the Phase-3 predict-commit — **not** touched by the Phase-4
run at `5ba52a0`). Its description still reads: *"cited across every
T20/T21/T24-adjacent constraint-3 near-threshold reading since"* and
*"MUST disclose this unresolved settling gap until Iteration 43 (or
later) closes it"* — with zero acknowledgment that Block MAIN's 36
mandate-scope cells **are now closed**, per this cycle's own headline.
`phase4_results.md`'s own "AFFECTED-DISCLOSURE" section correctly names
this as an outstanding task ("a Phase-5/close-of-cycle task, not this
Phase-4 file's own scope") — but no `phase5_review_*.md` exists yet in
the experiment directory, so as of this review the task is still undone.
This is exactly the class of gap this program's own house discipline
exists to catch before close, and it's mine to flag: **the registry
entry needs an update distinguishing "Block MAIN (30 rows, ±36–40°) now
settled-verified" from "Block ARTICLE / interior FALLBACK_ANGLES / Block
MINI still open"** before this cycle closes, or a future citation of
Block MAIN as settled would still trip an unnecessary disclosure
requirement while a future citation of Block ARTICLE/interior angles as
settled would NOT trip anything at all (since the entry's `trigger_terms`
don't distinguish which sub-claim is being made).

## 3. Item #2 — checked for accidental closure: none found

I grepped every `.md`/`.py` file in `experiments/066-.../` for `C80`,
`Block ARTICLE`, `Block MINI`, `FALLBACK_ANGLES`. The record is
disciplined and consistent throughout: `NOTES.md`'s Idealizations,
`phase4_results.md`'s "AFFECTED-DISCLOSURE"/"UNAFFECTED" sections, and
the closure summary's own `n_cells=36` (item #1's scope only) all
correctly and repeatedly state that the interior `FALLBACK_ANGLES`
(0°/±5°/±15°/±25°), Block ARTICLE's article-present legs, the 750nm/C80
four-point trend, and Block MINI's period-match test are untouched and
remain PLAN.md item #2's scope. **P-VIS42-6/7 are explicitly and
correctly stated as "NOT closed by this cycle."** I found no place where
exp-066 implies otherwise. This is real, verified discipline, not just an
assertion I'm taking on faith.

## 4. Argue the next change — ranked top-3 for Iteration 44

This cycle's result does **not** lower item #2's priority — it reinforces
it. The empty-scene floor across the near-grazing window came back
worse, not better, once settled; the ±35° cell (the one FALLBACK_ANGLES
cell this cycle touches) sign-flipped for a second, independently-
confirmed time; and the *only* numbers this whole T27 thread has ever
produced that are actually scored against constraint-3 (P-VIS42-6/7,
Block ARTICLE) remain completely unverified for settling. My ranking,
from VISION's own charter:

1. **Re-run Block ARTICLE's article-present legs (τ=0.0065, off_pass/
   off_bracket/off_lab) at settled STEPS≥2800.** This is the single
   highest-priority item under my own duty ("pin numeric thresholds…
   BEFORE any run that scores against them") — the *only* run in this
   program's history that has ever produced a scored PASS/MARGINAL/FAIL
   constraint-3 number is still sitting on unverified STEPS=1400 data,
   nineteen-plus iterations after the fact.
2. **Settle-check the four interior `FALLBACK_ANGLES` (0°/±5°/±15°/
   ±25°).** Zero settling evidence exists for these at any STEPS beyond
   1400, and they are equally load-bearing to the N9 aggregate as ±35°,
   which has now sign-flipped twice.
3. **Build, or formally and explicitly retire, Block MINI's period-match
   test (P-VIS42-10).** Two cycles running (exp-065 self-caught,
   exp-066 Red-Team-caught again on the same failure shape one level up)
   this program has identified this as the only instrument that could
   discriminate T21's real-mechanism-vs-settling-artifact question, and
   two cycles running it has been deferred behind a relabeling fix
   instead of being built. A third deferral risks becoming the kind of
   recurring-defect pattern this program's own precedent (T23/
   `length_provenance`) treats as a Checkpoint-4-adjacent finding after
   three strikes.

Cross-charter note, not one of my three: `R_contact` is now at three
consecutive deferrals (Iterations 41→42→43), disclosed properly this
cycle (mandatory fix E) — a fourth at Iteration 44 is the line this
program's own record already named as worth flagging.

## 5. Verdict: **PARTIAL**

Item #1 (T27's own ranked-#1 priority) is genuinely, cleanly closed:
every prediction CONFIRMED, every gate PASSED, zero Phase-2 criticism
overridden, and every headline number I independently recomputed checks
out exactly. That is real, disciplined execution and I don't discount
it. But from VISION's own charter — the seat whose duty is constraint-3's
numeric thresholds — nothing here moves the program's only ever-scored
PASS/MARGINAL citations, and the "net worse" empty-floor finding, while
correctly scoped as instrument-floor rather than perceptual, sharpens
rather than resolves the urgency of the still-wide-open Block ARTICLE/
interior-angle work. Combined with the live, unfixed registry-staleness
gap (§2), I call this PARTIAL, not PROMISING, from my seat — other
charters closer to this cycle's own scope (PHOTONICS, ELECTROMAGNETISM)
may reasonably read it differently.
