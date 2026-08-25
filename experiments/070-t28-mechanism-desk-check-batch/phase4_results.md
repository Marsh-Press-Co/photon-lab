# PHASE 4 — RESULTS · Panel Iteration 47 · exp-070 (T28 mechanism desk-check batch)

Executed: `python3 desk_check_mechanism.py` (deterministic — fixed seed 0
on the null-permutation control; re-running reproduces every number
bit-for-bit). Zero FDTD calls. Full output: `results.json`.

## P-070-1 — per-config decomposition — **CONFIRM**

| Config | `R²_free` | Recovered `P*` | Deviation from `P*_delta=2.8421°` | Config confirms? |
|---|---|---|---|---|
| C40 | 0.4327 | 2.4361° | 14.29% | yes (≤20%) |
| C80 | 0.4337 | 2.5338° | 10.85% | yes (≤20%) |

Both configs' own free-fit periods (grid search `[1°,4°]`, `center=39°`)
land within 20% of the padding-delta's committed free-fit period, and
neither config's `R²` is disqualifying (`<0.15`) nor its deviation `≥50%`.
**The ~2.8°-family signature lives in `C40(θ)` and `C80(θ)`
individually**, not only in their difference — the config-invariant
hypothesis this item was built to test.

Contrast with the ORIGINAL (uncorrected) item-(a) design, which Red
Team's Phase-2 audit ran against this same data: bare `R²≥0.30` alone
would also have fired (0.4327/0.4337 both clear it), but via periods
(2.44°/2.53°) the original design's own prose ("the ~2.8°-family
signature") would have mis-described as matching 2.84° when they are
actually 11–14% off it — the corrected, period-aware gate reports the
same qualitative CONFIRM this time, but for the right, disclosed reason
(both periods are close enough to be the "2.8°-family," not close enough
to claim exact agreement).

## P-070-2 — beat-frequency reconstruction — **NEITHER**

Two branches from `1/P_beat = |1/P(39°,600nm) ± 1/P*_delta|`:

| Branch | `P_b` | `A_alt` | Best NAMED match | `best_rel` | `null_p` (N=20,000) |
|---|---|---|---|---|---|
| plus | 1.1603° | 1270.812 | `2·R_OUT+5·D_SP` (3-way tie: `R_OUT`/`W_FLANK`/`W_OBJ` interchangeable) | 0.0148% | **0.2039** |
| minus | 6.3233° | 233.188 | `LEVER+7·clear_src` / `9·clear_plane−5·clear_src` (2-way tie) | 0.0807% | **0.8055** |

Both branches find a sub-0.1% named-constant match — by the ORIGINAL
(uncorrected) 1%-only threshold, both would CONFIRM. Under the
null-permutation control (20,000 random targets, `T~Uniform(100,1600)`,
identical 36,680-expression search space), the "minus" branch's own match
is **worse than 80.6% of pure-chance targets in the same range** — not
merely "not significant," actively unremarkable. The "plus" branch fares
better (`p=0.204`) but still misses the `p≤0.05` gate by a wide margin.
**Neither branch survives null control; reported NEITHER, not a soft
CONFIRM, per docket item 9.**

## P-070-3 — taper-as-second-aperture — **REFUTE**

`P_taper(39°,600nm) = degrees(20/(40·cos39°)) = 36.86°` vs.
`P*_delta = 2.8421°` — **1197% off**, an order of magnitude beyond the
100% REFUTE bar. `TAPER=40` cells alone, treated as a diffracting
sub-aperture, is cleanly ruled out as the source of the ~2.84° period.
This item is unaffected by the mandatory-fix docket (it carried no
look-elsewhere or gray-zone risk to begin with) and reproduces the
Phase-1 proposal's own disclosed recon number exactly.

## P-070-4 — `A_eff` systematic trace — **NEITHER**

`A_eff = 20/(radians(2.8421°)·cos39°) = 518.812` cells. Closest NAMED
match: a **six-way tie at 519** —
`D_SP+8·clear_plane`, `2·LEVER+9·clear_plane`, `3·LEVER+3·ABSORB80`,
`3·LEVER+6·ABSORB40`, `3·LEVER+6·PAD80`, `6·TAPER+3·LEVER` — at
`best_rel=0.0363%`. The 750nm cross-validation using this candidate value
(519) gives `R²=0.7663` — clears the 0.70 bar, matching the Phase-1
proposal's disclosed post-hoc figure (`R²=0.7666`, PHOTONICS' own Phase-5
finding from exp-069) almost exactly. **Every raw-threshold component of
this prediction passes.** But `null_p=0.497` — this specific match is
statistically indistinguishable from the median outcome of a random
target in the same plausible range. **Reported NEITHER, per docket item
9: a `p>0.05` result is never a soft or qualified CONFIRM, regardless of
how many raw thresholds it clears.** This is the single sharpest
demonstration in this cycle of why Red Team's null-control mandate
mattered — every number that made P-070-4 look like this batch's
strongest finding at Phase 1 survives entirely intact into Phase 4, and
is still correctly NEITHER.

## P-070-5 — convergence check — **REFUTE**

(b)'s tie-sets (`{2·R_OUT+5·D_SP, 2·W_FLANK+5·D_SP, 2·W_OBJ+5·D_SP}` for
the "plus" branch; `{LEVER+7·clear_src, 9·clear_plane−5·clear_src}` for
"minus") share **zero** expressions with (d)'s tie-set (the six-way `519`
tie above). No overlap, in either branch — binary REFUTE, unaffected by
either branch's own NEITHER status on P-070-2, since (e) tests
label-overlap directly, not confirm-status agreement.

## Search-space provenance (docket item 8 — correcting Attack 3's own
## cross-target citation conflation)

For the record, stated per-target correctly: `3·R_OUT=234`'s own closest
rival (relevant to branch "minus," `A_alt=233.19`) is the **2-way tie at
233** (`LEVER+7·clear_src`, `9·clear_plane−5·clear_src`), `0.0815%` away
— NOT the `519`-tie numbers PHOTONICS' own critique cited when making
this same point. `A_eff=518.81`'s own closest rival is the **6-way tie at
519** above, `0.0363%` away. Both are real, independently reproduced
findings ("the headline candidate is not the closest match" holds for
both targets) — this section exists only to keep the correct pair of
numbers attached to the correct target going forward.

## Gates

Zero new `lab/` diff, zero FDTD calls — no `box_dev`/`cross_dev` gate
applies. `desk_check_mechanism.py` reads and refits already-gated
`results.json` data; it does not re-derive it. Full bench reconfirmed
green at shift start (41/41 fast-subset checks, SESSION_LOG.md).

## Checkpoint-criterion-2 candidacy

**Explicitly declined**, unchanged from Phase 1/3 — no mechanism class is
bounded by any outcome here; this is instrument/model-fidelity work.
