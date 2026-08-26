# exp-076 Phase 4 — Official Run Results

**Panel Iteration 53.** Executes `run.py` against the FROZEN PREDICTIONS
committed in `NOTES.md`/`phase3_synthesis.md` (commit `c1e4af3`) — no
threshold, bin edge, or outcome-mapping rule was touched after this point.

## Two implementation bugs found and fixed during Phase 4 (disclosed per
this program's own verify-before-claim culture, not folded silently into
the frozen design)

Both are pure engineering defects in `run.py`'s execution/serialization
plumbing — **neither touches any frozen prediction, threshold, bin edge,
or outcome-mapping rule.** All FDTD physics results are bit-identical
across both crashed attempts and the final clean run (same seed, same
inputs, same deterministic engine).

1. **`settling_gate_check(pre, ...)` indexed its argument as if it were
   `pre["by_key"]` directly, when `block_settle_precondition()` actually
   returns the wrapper dict `{n_new_runs, elapsed_s, by_key}`** —
   `KeyError` after all 5 settling-precondition FDTD calls had already
   completed successfully (crashed before any data was lost from the
   *design*, only from that process's memory). Fixed by passing
   `pre["by_key"]` at the call site. First attempt crashed here; the 5
   settling calls were re-run clean on the second attempt (identical
   `C_empty` values to 6 significant figures against the first attempt's
   printed log, confirming determinism).
2. **`json.dump` cannot serialize a dict with tuple keys** —
   `settle_precondition=pre` embedded `pre["by_key"]`, keyed by
   `(theta, cpl_nm, steps)` tuples, directly into the output dict. Crashed
   at the very last line of `main()`, *after* all 50 FDTD calls and every
   headline/diagnostic computation had already completed and printed
   correctly to stdout — only the final `results.json` write failed.
   Fixed by converting `by_key`'s tuple keys to strings
   (`f"{theta}_{cpl_nm}nm_STEPS{steps}"`) before assembly, in both the
   success path and the (untriggered this run) HALT path, which had the
   same latent bug plus an unrelated additional one (`baseline`'s raw
   `data`/`committed72` fields, containing numpy arrays, were not stripped
   before serialization in the HALT branch — fixed to match the success
   path's stripping).

Second (and final) attempt: exit code 0, `results.json` written cleanly,
all values below independently cross-checked against the crashed
attempts' stdout logs (bit-identical, confirming no physics was affected
by either bug or its fix).

## Settling precondition (docket item 4) — PASSED with wide margin

Forward (EM's fix, MANDATORY, HALT-if-fails): `STEPS=2800` vs `STEPS=4200`
at θ∈{39°,40°}. Measured shift, as a fraction of `amp_ref`
(`THRESH_LOW`-normalized): **`frac_39=0.0001`, `frac_40=0.0001`**, both
~500× inside the `bar=0.0498` (`THRESH_LOW`) gate. **G40's own
previously-untested (thin `ABSORB=40` boundary at `C80`'s larger domain)
geometry is, in fact, cleanly settled at `STEPS=2800`** — EM's and
VISION's independently-converged Phase-2 concern was a real, correctly-
flagged, previously-uncharacterized gap (this program had never tested
this specific combination before), and checking it was worth the 3-call
cost, but the geometry turns out fine.

Backward (VISION's fix, disclosed-only, non-gating): `STEPS=1400` vs
`STEPS=2800` at θ=39° moves `C_empty` by **61.7%** relative; the bonus
reused θ=40° point (exp-065's own `Block PAD` `STEPS=1400` reading) moves
by **64.0%** relative. Both large — consistent with, and considerably
larger than, T27's own general finding that `STEPS=1400` is not settled
on this channel — confirming exp-065's original `Block PAD` `G40` reading
(the only prior FDTD data this program had for `G40`) was never fit to
score against T28's dense window, exactly as `phase1_proposal.md`
Idealization 4 disclosed. Disclosed only; does not gate anything, since
`STEPS=1400` data was never used as scored input.

## Headline result

| Quantity | Value | Bin |
|---|---|---|
| `x = amp_ratio(PAIR_PAD)` = `amp_ratio(C40, G40)` | **0.119366** | **HIGH** (≥0.116111) |
| `y = amp_ratio(PAIR_ABSORB40)` = `amp_ratio(G40, C80)` | **0.071616** | **MED** ([0.049762, 0.116111)) |

**`(x_bin, y_bin) = (HIGH, MED)` → `OUTCOME = PAD_TIED`** (confound NOT
relieved in the reassuring direction), per the frozen 9-cell table.

The pure-`PAD` effect (`x=0.119`, isolating padding/domain-geometry at
fixed `ABSORB=40`) is **larger** than the pure-`ABSORB` effect (`y=0.072`,
isolating boundary depth at fixed `PAD=40`) — and clears the strong
`HIGH` bar on its own. **Per the frozen PAD-TIED interpretation and
MATERIALS' caveat (docket item 7, carried verbatim): five iterations of
T28 causal claims on the congruent `{C40,C60,C70,C80}` `ABSORB`-series
(Iterations 48–52) must be re-read as possibly padding/domain-geometry-
tied, not physically tied to the graded boundary's absorption depth —
`ABSORB` and `PAD` are both pure numerical domain-construction
parameters; neither carries more physical standing than the other.**

## Disclosed diagnostics (non-gating, per docket items 2/3)

`rho_pad_absorb = 0.2108` (`dp_pad=-0.05013°`, `dp_absorb40=+0.13105°`,
`dp_c40_c80=+0.06684°`, loaded not re-fit). Per the frozen disposition:
this is an uncalibrated magnitude signal, not distinguishable from a
carrier-choice artifact — **no interaction claim is drawn from this
value.** For reference only: below the `≥1.00` figure that (had the old,
now-superseded §4(c2) language survived) would have been mis-read as
"real evidence," and well above the `≈0.041` value the same formula gives
retroactively on the original, real baseline series (Red Team's Phase-2
audit, computed for context, not gating there either).

`R_q` disclosure (docket item 3): not used in the gating `amp_ratio`
statistic; used, via `delta_P_obs`, only in the disclosed-only
`rho_pad_absorb` diagnostic above, with no null-calibration attached.

## 750nm advisory leg (docket item 5) — genuinely informative tension, not decisive

| Quantity | 600nm (headline) | 750nm (advisory) |
|---|---|---|
| `x = amp_ratio(PAIR_PAD)` | 0.119366 | 0.419868 |
| `y = amp_ratio(PAIR_ABSORB40)` | 0.071616 | 0.616131 |
| Ordering | `x > y` (PAD dominant) | `x < y` (ABSORB dominant) |

**`same_direction_as_600nm_headline = False`.** The 750nm leg's ordering
is the *opposite* of the 600nm headline's — at a genuinely non-aliased
wavelength (`ABSORB=40→1.6λ`, `80→3.2λ` at 750nm, vs 600nm's resonant
`2.0λ`/`4.0λ`, PHOTONICS' own Phase-2 aliasing concern). Per the frozen
design (Idealization 1, docket item 5's advisory/narrow-window label),
this does **not** overturn the 600nm `PAD_TIED` headline outcome — the
9-cell band machinery was never applied to this leg, the window is
narrower (3° vs 6°), and no wavelength-general citation is licensed
either way. But the direction flip is exactly the kind of signal
PHOTONICS' original aliasing attack (adopted as MANDATORY at Phase 2,
Attack 4) predicted could exist, and is itself a genuine, disclosed
finding: **this cycle's `PAD_TIED` headline should not be read as
wavelength-general without the still-outstanding full-width (6°/31-point)
non-aliased leg** the Phase-2 docket already flagged as required before
any such citation.

## Bottom line

**Outcome: `PAD_TIED`** — T28's amplitude-mismatch signal, on this
cycle's own decorrelated evidence at 600nm, tracks the padding/domain-
geometry construction axis at least as strongly as the `ABSORB`-boundary-
depth axis, with the pure-`PAD` reading landing in the strong (`HIGH`)
band and the pure-`ABSORB` reading in the middle (`MED`) band. This is
the **opposite** of the "confound relieved, genuinely `ABSORB`-tied"
outcome five prior T28 cycles' causal framing implicitly hoped for, and a
real, load-bearing correction to how the `{C40,C60,C70,C80}` congruent
series' prior findings (Iterations 48–52) should be cited going forward —
subject to MATERIALS' caveat that neither `ABSORB` nor `PAD` carries more
physical standing than the other (both are pure numerical FDTD
domain-construction parameters), and subject to the 750nm leg's disclosed
ordering-flip tension, which argues against treating this result as
wavelength-general pending a full-width non-aliased leg.

**T28's own substantive mechanism question — the ~2.84° periodicity's
origin — is still not identified by this cycle.** This cycle answers a
different, prerequisite question (which construction axis the amplitude-
mismatch signal tracks), and answers it in the less convenient direction:
the signal is now shown to be at least as much a property of the padded
domain construction as of the absorbing boundary's own depth, which
narrows what a future mechanism must explain (a candidate mechanism must
now also account for a real `PAD`/domain-geometry sensitivity) rather
than resolving it.

See `phase5_review_*.md`/`phase5_redteam_audit.md` for Phase 5 (six blind
reviews + Red Team final audit) and `NOTES.md`'s Result/Learned/Next for
the closing house-format summary.
