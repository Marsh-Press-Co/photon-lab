# Tier 1 item 4 — phase-convention tie-breaker extension to [47.5°,54.5°]: RESULT (genuinely inconclusive, disclosed)

PLAN.md Iteration-59 queue Tier 1 item 4 (near-unanimous top pick: EM #1,
QUANTUM #1, PHOTONICS #2, VISION #2). Extended `experiments/075-.../
phase5_redteam_phase_convention_check.py`'s own empirical FDTD tie-breaker
(the `[0°,20°,39°]` precedent) to `θ∈{48°,51°,54°}` inside item 1's own
`[47.5°,54.5°]` construction range, reusing its `measure_r`/`textbook_r`/
`committed_r` functions unchanged, at the same K=5 operating point its own
`[CALIB]` block found reliable at the original angle range. 6 new FDTD
calls, ~90s total, per the original file's own docstring.

## Result — DO NOT read the headline number as resolving anything

**Nominal tally: 6/6 sub-tests (3 calibration + 3 lossy) favor the
committed convention `r`, none favor `conj(r)`.**

**But the load-bearing `[CALIB]` reliability precondition FAILS at this
angle range**, unlike the original `[0°,20°,39°]` range: a lossless
(real n=1) spacer must show `|r_measured|=1.0` exactly, by energy
conservation, independent of any convention question — the original file's
own K=5 point satisfied this cleanly; here it does not.

| θ (deg) | calibration `|r_measured|` (must be ≈1.0) | `peak_match` |
|---|---|---|
| 48 | 0.1598 | True |
| 51 | 0.1228 | **False** |
| 54 | 0.1159 | **False** |

`|r_measured|` sits 6–9× BELOW the required 1.0, and `peak_match` (the
extraction's own internal sanity check — does the recovered spectral peak
land where the source's own steering angle predicts) fails at 2 of 3
angles. This is the SAME extraction-reliability failure mode the original
file already diagnosed and disclosed at large `K` (`K≥8`, its own §
"DISCLOSED LIMITATION") — **now shown to recur at the original file's own
reliable `K=5`, at this NEW, more-grazing angle range instead.** A genuinely
new finding about this instrument, not previously characterized: K=5's own
reliability is angle-range-dependent, not solely K-dependent.

**Self-scored disposition: GENUINELY INCONCLUSIVE, not a tie-breaker.**
The nominal "6/6 favor `r`" tally cannot be trusted with the confidence the
original `[0°,20°,39°]` result carries, because the one internal check that
licensed trusting K=5 there (the `[CALIB]` block) fails here. This does
**not** mean the committed convention is wrong at `[47.5°,54.5°]` — it means
this particular extraction method has not yet produced a reliable answer at
this angle range, and a different K (or a different extraction geometry
entirely) would be needed before this tie-breaker can be trusted the way
exp-075's own K=5 result was. **The `r`-vs-`conj(r)` question at
`[47.5°,54.5°]` remains genuinely open** — this rider narrows the
*instrument*, not the *answer*: it rules out treating this exact K=5/
[0°,20°,39°]-validated method as a drop-in tie-breaker at a new,
more-grazing range without re-validating its own calibration there first.

Full numbers: `phase_convention_output.txt`, `phase_convention_extension_
results.json`.
