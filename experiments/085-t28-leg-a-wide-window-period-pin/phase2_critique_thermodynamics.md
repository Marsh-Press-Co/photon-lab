# PHASE 2 — CRITIQUE · THERMODYNAMICS · Panel Iteration 62 · exp-085

*Seat: THERMODYNAMICS. Fresh sub-agent, blind to any other seat's current-cycle
critique. Read in full: PANEL.md, LOGBOOK.md (RULED OUT R1–R10, ESTABLISHED,
LIVE THREADS T1–T28 including the full Iterations 46–61 T28 arc and both
Checkpoint entries), `experiments/084-.../NOTES.md`,
`phase1_derivation.py`, `derivation_results.json`, `phase5_redteam_audit.md`,
and the proposal under review, `experiments/085-.../phase1_proposal.md`,
including exp-084's own `phase1_proposal.md` (cited extensively by exp-085).*

## Independent verification performed before critiquing

Recomputed, from scratch, rather than accepted on faith:

- **Method A grid count**: `(80.0−2.0)/0.02 + 1 = 3901.0` — matches the
  proposal's claimed `N=3901` exactly.
- **Fraunhofer fraction, 0.197%**: `D_SP/(A_full²/λ) = 223/(1504²/20) =
  223/113,100.8 = 0.19717%` — matches. **Important, and worth flagging
  explicitly since this is exactly the kind of unit slip R9 exists to
  catch**: this number is correct *only* because it uses the FULL aperture
  width (1504 cells = 2×752), not the half-width `A=752` the rest of this
  file's own table calls "A." Substituting the half-width naively gives
  `223/(752²/20) = 0.789%`, a 4× different, wrong answer. Exp-084's own
  desk arithmetic used the correct (full-width) operand; exp-085 only
  *cites* the resulting 0.197% figure, never re-derives it with the wrong
  operand — so no error propagates into exp-085 itself, but the two
  quantities sharing the same "A" mnemonic is a latent trap for the next
  cycle that tries to recompute this from the parameter table alone.
- **Method C grid**: 37 sub-window centers × 31 points/window = 1147 —
  matches.
- **Total evaluations**: `3901+32768+1147 = 37,816`, not the proposal's
  stated "≈37,800" — a 16-count (0.04%) rounding slip, non-load-bearing,
  noted only because R4/R9 discipline says arithmetic gets checked even
  when "close enough" looks safe.
- **FFT sizing**: `2^15=32768`, pad `2^17=131072`, `sin(2°)=0.034899`,
  `sin(80°)=0.984808` — all confirmed.
- **Method B's period-conversion formula**: `Tc = radians(P)·cos(39°)` is
  confirmed, by reading `run69.py`'s own `_free_period_search` source
  (`x=sin(theta)`, `Tc = math.radians(p_star) * cos_c`), to be the actual
  convention `_free_period_search` uses — so `P_fft_deg =
  degrees((1/f_peak)/cos(radians(39)))` is the correct algebraic inverse,
  not a mismatched convention dressed up as one.

No arithmetic defect found in the numbers the proposal states. The one
substantive problem below is methodological, not a hand-computed digit.

## Steel-man (≤150 words)

A clean, cheap, correctly-scoped follow-up to exp-084's own top-ranked
Tier-1 item: it asks the one question the narrow 31-point window
structurally could not answer — whether leg (a)'s free-fit period is a
real asymptote or an artifact of under-sampling a possibly-chirped
near-field curve — at zero marginal FDTD cost, reusing validated machinery
unmodified. Every comparator number I recomputed checks out (grid counts,
Fraunhofer fraction, FFT sizing, the Method B period-conversion
convention). From my own charter: leg (a) is a vacuum-only, article-free,
non-absorptive geometry characterization of an already-validated function
— no material, no absorbed power, no article anywhere in this cycle's own
scope. There is genuinely no quantity here for an energy sidecar to
attach to, so the "T1: N/A / zero realizability content" scoping (§3, §6)
is substantively honest, not a smuggled exemption from a duty that should
otherwise apply.

## Sharpest attack (≤150 words)

§4 misapplies its own R10 citation. R10's carve-out for a deterministic,
zero-noise curve changes how a circular-shift result is *interpreted*
(self-similarity, not noise-robustness) — its text was written using
exp-084's own leg (a) as the worked example, where the null WAS run and is
precisely what downgraded the narrow-window SUPPORT to INCONCLUSIVE. R10's
mandatory clause requires the baseline be "always run and reported...
before it is reported as evidence," and a cycle that "omits [it] entirely
fires Checkpoint criterion 4 automatically." Exp-085 explicitly skips it on
the wide/dense curve, reasoning width and density substitute for it. But a
wider, denser, still-smooth curve is exactly as exposed to a
self-similarity false positive — Method C's own chirp-drift worry is that
identical risk restated. As pre-registered, any STABLE/period-match
outcome would ship without the one test R10 exists to enforce, the very
cycle after the rule was adopted for this exact function.

## Verdict: **support-with-changes**

The energy/detectability scoping is correct and needs no sidecar; the
arithmetic is clean. But §4's outcome bands must not be scored as
delivered — Method A's (and Method B's, if scored independently) wide/
dense fit needs a circular-shift-on-the-curve null run and reported
alongside `R²_wide`/`P_wide` before any STABLE, DRIFTING, or
period-match-tier outcome is filed as evidence, exactly as R10 requires
and exp-084 itself did on the narrow window. This is cheap (the curve is
deterministic and already computed) and does not change the proposal's
cost or scope — it closes a real compliance gap, not a physics one.

Separately, minor and non-blocking: neither §3 nor §6 mentions the
standing joint EM/THERMO energy-interception cross-check (the item
Checkpoint 4 just fired on for a third consecutive silent absence at
exp-084). Given this cycle is again zero-FDTD and article-free, the
correct disposition is almost certainly "still structurally cannot run,"
matching exp-084's own case — but exp-084's own Red Team audit explicitly
instructed future cycles to *state that precisely* rather than say
nothing. One sentence in §3 doing so would close this cleanly.

## Parameter change that would flip my verdict to plain "support"

Add the mandatory circular-shift-on-the-real-curve null (order-preserving
shifts of the wide/dense `c_wide(θ)` array itself) to §4's own outcome
scoring, run and reported before any STABLE/period-match verdict counts —
i.e., the missing clause is the fix; nothing else about the proposal needs
to change.
