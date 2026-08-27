# PHASE 2 — CRITIQUE · QUANTUM OPTICS · Panel Iteration 55 · exp-078

*Blind critique, independent of other seats. Charter: non-classical
absorption, state-dependent or coherent interactions; mechanisms enter the
bench only as effective classical parameters or Red Team strikes them. This
proposal's mechanism (a coherent edge-image echo weighted by a complex
`r(theta;ABSORB)`) is the classical-coherent limit my own charter treats as
in-scope. For a desk-analysis, zero-FDTD cycle like this one, my seat's
operative territory is the one this program has repeatedly assigned it in
this exact T28 sub-thread (exp-073's `G0-e(ii)`, exp-077's null-calibration
appendix): null-calibration and look-elsewhere rigor on a period-comparison
claim.*

---

## 1. Steel-man (≤150 words)

This pre-screen does what a genuine zero-FDTD screen should. It derives a
new closed form rather than guessing a coordinate swap — validated first by
bit-exact reproduction of the established x-wall formula (`|dev|≤1.8e-15°`)
before being applied somewhere new — and scores it against three
already-established real periods using the identical imported
`_free_period_search` machinery this sub-thread has used since Iteration
46. It self-scores conservatively: despite 2 of 3 comparisons clearing the
0.30 SUPPORT bar, §7 refuses to call SUPPORT, citing `C80`'s
near-noise-floor `|r|`, R²=0.13–0.15 far below this program's credible
range, and the missing null-permutation control — all independently
checkable in the committed JSON. Most importantly, §7/§8 name the exact
cheap check needed as the load-bearing next move rather than quietly
banking the raw 2/3 as evidence. That is the correct epistemic posture for
a pre-screen.

## 2. Sharpest attack (≤150 words)

I ran the control the proposal names as its own cheapest next move
(`phase2_quantum_null_check.py`, importing `_free_period_search` and this
file's own staged-widening stage list unmodified, 2,000-trial i.i.d.
N(0,1) noise, seed=7 — reduced from this program's usual 20,000 for a
single Phase-2 turn's time budget, disclosed, SE≈1pp). Per-comparison,
P(null rel_dev≤0.30) = 0.26 / 0.14 / 0.16 for c80_c40 / pair_pad /
pair_absorb40 — individually unremarkable. Jointly (three independent
noise draws per trial, matching the real analysis's own three-independent-
curve structure): **P(≥2 of 3 SUPPORT by pure chance, zero relationship to
reality) = 0.080** — above the conventional 0.05 bar. Worse: **P(null
R²≥observed model R²) = 0.65 / 0.78 / 0.68** — the model's own 0.13–0.15
fits are matched or beaten by PURE NOISE 65–78% of the time on this
window. §7's "survives the pre-screen... not obviously wrong" is more
generous than these numbers support: the period match is at best
borderline-distinguishable from chance; the R² is not distinguishable from
chance at all.

## 3. Independent verification performed (this critique's own computation)

`phase2_quantum_null_check.py` (this directory), imports `y_wall_
prescreen.py`'s own `_free_period_search` (from `run69`, never
reimplemented, R4) and copies its 3-stage widening schedule (`narrow[1,4]`
n_grid=400 → `wide[1,15]` n_grid=2800 → `widest[1,60]` n_grid=6000) as a
plain data structure — the underlying search algorithm is imported, only
the Monte-Carlo harness is authored, matching `pad_round_trip_model.py`'s
own precedent for a "quiet" null-generation variant. Two checks, against
the real 31-point, `[36°,42°]` grid:

**(a) Per-comparison null (is a single `rel_dev≤0.30` match surprising?)**
2,000 independent `N(0,1)` 31-point noise curves per target, run through
the identical staged search:

| target | P*_real | observed rel_dev | observed R² | P(null rel_dev≤0.30) | P(null R²≥observed) |
|---|---|---|---|---|---|
| `c80_c40` | 2.8421° | 0.1296 (SUPPORT) | 0.1530 | **0.2635** | **0.6540** |
| `pair_pad` | 4.6113° | 0.3136 (INCONCLUSIVE) | 0.1331 | 0.1370 | 0.7840 |
| `pair_absorb40` | 4.1761° | 0.2330 (SUPPORT) | 0.1493 | **0.1615** | **0.6795** |

Reading: a bare `rel_dev≤0.30` on any ONE comparison is unremarkable —
noise clears it 14–26% of the time on this narrow window (window
distribution under null: ~93% stay in `narrow[1,4]`, confirming the model
curves' own reported "interior optimum, narrow window" results are not
themselves suspicious). The R² comparison is the more damning number: pure
noise reaches or exceeds the model's own R² 65–78% of the time — this
program's own established credible floor (R²≈0.26–0.30 even for exp-070's
"softer than first read" CONFIRM) is not approached by either the real
data (0.63–0.82, safely above) or, evidently, by this model (0.13–0.15,
statistically indistinguishable from noise-fit R² on this window).

**(b) Joint null (is "2 of 3 SUPPORT" itself surprising?)** 2,000 trials,
each drawing THREE independent noise curves (one per target) and scoring
each against its own real reference, matching the real analysis's
three-independent-model-curve structure:

```
distribution of #SUPPORT-out-of-3 under null:
  0 SUPPORTs: 0.5525   1 SUPPORT: 0.3675   2 SUPPORTs: 0.0740   3 SUPPORTs: 0.0060
P(>=2 of 3 SUPPORT under null) = 0.0800
OBSERVED: 2 of 3 (c80_c40, pair_absorb40)
```

**Net answer to the question posed** (§8 item 1, directly): the observed
"2 of 3 clear SUPPORT" pattern occurs by pure chance about 1 trial in 12.5
(p=0.080) — above the conventional 0.05 significance bar, so it is **not**
cleanly distinguishable from the R5/exp-070 "any reasonably dense search
finds a plausible match" failure mode, though it is not squarely inside it
either (a coin-flip-adjacent result, not a confident null-rejection). The
R² leg is unambiguous: the model's own fit quality carries essentially no
information relative to noise on this window (65–78% overlap). Taken
together, this is genuine new information for Phase 3: **the proposal's
self-scored INCONCLUSIVE is the empirically correct verdict, not an
under-claim** — but §7's framing ("not obviously wrong," "survives the
cheap period pre-screen") reads more encouraging than a p=0.08 joint match
rate and a 65–78% R²-null-overlap actually license. If anything, a reader
should come away from this pre-screen leaning toward "uninformative,"
not "promising but unconfirmed."

**Disclosed limitation**: `n_trials=2,000`, not this program's usual
20,000 (R5/exp-070/exp-077 precedent) — a time-budget reduction for a
single Phase-2 critique turn, stated in the script's own header and
runtime output, not silently applied. SE on a proportion near p=0.08–0.26
at n=2,000 is ≈0.6–1.0pp — sufficient to place these numbers solidly
above the 0.05 bar (not a boundary-precision question) but not to resolve
a true tail probability an order of magnitude smaller.

## 4. Verdict: **support-with-changes**

The physics/derivation work (§3's edge-image re-derivation, its bit-exact
x-wall validation, the shared-damping-formula premise check) is sound and
this critique found no defect in it. The self-scored **INCONCLUSIVE**
verdict is, per the null-calibration control above, the correct call —
this is not a case (unlike exp-070's named-constant search, R5's
Iteration-47 addendum) where the missing control would have flipped a
confident-looking match to demonstrably-chance; the honest reading is
closer to "genuinely ambiguous; the control does not rescue it into
SUPPORT, but does not cleanly REFUTE it either." Per this program's own R8
standard (an unverified robustness question named as load-bearing may not
be left unrun before the next phase treats it as informational), this
control should not remain absent from the committed record now that it
has been run — a fourth cycle in this same T28 sub-thread would otherwise
recreate the exact gap R8 was adopted to close.

**Required change**: add this null-calibration appendix (or an equivalent,
higher-trial-count re-run at 20,000 trials matching house convention) to
the committed record before Phase 3 treats §7's "survives the pre-screen"
language as license for further spend (e.g., building the full Test-B
propagator, item 5 in §8). Revise §7 to state the joint p=0.080 and the
65–78% R²-null-overlap explicitly, replacing "not obviously wrong" with
language that matches what the calibration actually shows: weakly,
not-quite-significantly above chance on period, indistinguishable from
chance on fit quality.

## 5. Single change that would flip this to full support

Fold this critique's null-calibration numbers (or a re-run at the house
20,000-trial standard) directly into `y_wall_prescreen_results.json`/
`phase1_proposal.md` §5, with §7's verdict language brought into alignment
with them — no change to the Test-A-only INCONCLUSIVE verdict itself, or
to any of §3's derivation, is needed. Absent that addition, I hold at
support-with-changes rather than full support, matching this program's own
R8 precedent one cycle removed: the check must actually be run and
recorded, not left as a named-but-unrun open question a fourth time in
this sub-thread's history.
