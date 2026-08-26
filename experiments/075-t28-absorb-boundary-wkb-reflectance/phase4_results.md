# PHASE 4 — TEST · Panel Iteration 52 · exp-075
## The two-wall-cavity model, run against the real data: frozen prediction CONFIRMED

*Predictions frozen in `phase3_synthesis.md` Sec 3.6 (prior commit,
`daa4542`), BEFORE this script touched `block_dense.rows` — house
discipline, non-negotiable. All numbers below from
`two_wall_cavity.py`/`two_wall_cavity_results.json`, this directory; none
hand-typed (R4).*

---

## 1. Headline

**Combined Verdict: REFUTE — the frozen primary prediction (Test A
REFUTEs again) is CONFIRMED, with margin.** The correctly-derived
two-wall-cavity model — both PEC walls, physically correct
interferometer-arm path differences (`2·PLANE_X` and `2·((nx−1)−SRC_X)`,
NOT PHOTONICS' Phase-2 `nx`-substitution) — does **not** reproduce the
real `P*=2.8421°` family either. PHOTONICS' `nx`-substitution match is
CONFIRMED, as pre-registered, to be the look-elsewhere artifact Red
Team's own audit flagged it as being at risk of (`phase2_redteam_audit.md`
§3): once the actual physics is computed rather than a length scale
substituted, the match disappears.

---

## 2. Test A — period match

Both walls' own closed-form single-bounce periods (§1 of
`two_wall_cavity_results.json`, reproducing `phase3_synthesis.md` Sec
3.2's table exactly) sit in the same far-from-target range as the
already-tested single-wall model:

| `ABSORB` | `P_left(39°)` | `P_right(39°)` |
|---|---|---|
| 40 | 11.824° | 15.431° |
| 60 | 9.386° | 11.525° |
| 70 | 8.509° | 10.230° |
| 80 | 7.782° | 9.196° |

The full numeric interference model (coherent sum of direct + both
images) gives **`P_model=15.0000°`** — running to the SAME search-window
boundary the single-wall model hit (`R²=0.9062` at the boundary, even
higher than the single-wall model's `0.8587`, an even MORE cleanly
boundary-pinned, non-oscillating curve). Widened search (1-60°) again
runs to its own boundary (`P*=60.0000°`, `R²=0.9178`) — **the same
boundary-search-artifact class Red Team's audit named for the single-wall
model (mandatory fix 4) recurs here identically**, for the same reason:
combining two components whose own periods (7.8°-15.4°) are both several
times longer than the tested 6°-wide window produces a curve that,
correctly, never completes even one full oscillation across it.
`rel_period_dev=4.2778` — bit-identical to the single-wall model's own
figure (both pinned to the same 15.0000° search-boundary value) —
**REFUTE** under the pre-registered band (`>1.00`).

---

## 3. Test B — shape match, and why its nominal SUPPORT does not survive the robustness check

**Observed: `r²=0.3042`, Pearson `r=-0.5516` (negative correlation)** —
under the bare pre-registered band (`SUPPORT≥0.30`), this nominally
clears SUPPORT, unlike the single-wall model's own `r²=0.2586`
(INCONCLUSIVE). **This is exactly why Red Team's mandatory robustness
check matters, and exactly what it is for.**

**Circular-shift null-calibration (mandatory, `phase3_synthesis.md` Sec
3.5, R6-style order-preserving construction, `N=20,000` trials):**
against a null built by circularly shifting the REAL `delta(theta)`
array (preserving its own known θ-autocorrelation, lag-1≈0.92-0.94,
exp-074 Iteration 51) relative to the model's fixed predicted curve, the
observed `|r|=0.5516` sits at **p=0.1953** — the null's own mean
`|r|=0.2989` and its 95th percentile `|r|=0.6800` bracket the observed
value comfortably inside the "unremarkable" range. **NOT significant.**

**Reading, applying the SAME narrative discipline mandatory fix 4 already
established for the single-wall model:** a nominal `r²≥0.30` under a
sign-blind, autocorrelation-blind band is not, on its own, evidence of a
real shape match once the data's own known autocorrelation is accounted
for — an autocorrelated real curve compared against ANY smooth,
slowly-varying fixed predicted curve will show `|r|` in the 0.3-0.7 range
a sizeable fraction of the time by chance alone (the null's own 95th
percentile, 0.68, is not far above what was observed). Test B's nominal
SUPPORT here should be read as **not distinguishable from the
autocorrelation-driven chance level** — real information (the robustness
check itself is doing genuine work, exactly as designed), but not
evidence for the two-wall mechanism. The sign remains wrong-directioned
throughout (as with the single-wall model), consistent with, not
independent evidence for, a REFUTE reading.

**Because the pre-registered combining rule scores Test B under the bare
band (not the robustness check) for the Combined Verdict formula, and
Test A alone already REFUTEs, the Combined Verdict is unaffected either
way: REFUTE.** The robustness check's role here is narrative honesty
(don't let a look-elsewhere-vulnerable nominal SUPPORT stand
uncontextualized), not a rescoring — the same pre-registration-integrity
principle mandatory fix 4 already established.

---

## 4. What this settles, that the single-wall model alone could not

Red Team's Phase-2 audit (`phase2_redteam_audit.md` §3) could not,
without this run, distinguish "PHOTONICS' `nx`-match is a real signal
this program hasn't built the right model for yet" from "PHOTONICS'
`nx`-match is a look-elsewhere artifact of substituting a large,
physically-unmotivated length scale into a formula built for a different
mechanism." **This run answers that question: the actual, physically
correct two-wall model — using each wall's own genuinely-derived
distance, not the raw domain width — predicts periods in the same
7.8°-15.4° range the single-wall model already REFUTEd, and its own full
numeric free-period fit lands at the identical `15.0000°` search-boundary
value.** The `nx`-substitution match was the artifact Red Team's
look-elsewhere check said it was at risk of being.

**Both tested boundary-reflectance-echo mechanisms — single-wall and the
correctly-derived two-wall cavity — are now REFUTEd on the same real
data, with the two-wall model's own robustness check closing the one
respect in which its raw numbers looked more favorable than the
single-wall model's (Test B's nominal, but not robustness-surviving,
SUPPORT).** This is closer to earning the "narrows the remaining space"
framing `phase1_proposal.md`'s original §5 claimed prematurely (per
mandatory fix 4) — not because either individual REFUTE is new, but
because the specific gap Red Team's audit left open (an untested,
same-cost, same-machinery variant that looked promising on a first-pass
estimate) is now closed, in the same direction, by an honestly-run test
that was pre-registered to potentially go the other way.

---

## 5. What remains open (stated, not implied away)

- **Multiple internal bounces / a true resonant cavity treatment**
  (Idealization 6, both this file and `phase1_proposal.md`) remains
  unmodeled — bounded, not computed, as negligible given `|r|≤0.0064`
  (§3.3 of `phase3_synthesis.md`); a future cycle could compute this
  bound explicitly rather than argue it, though the physics does not
  suggest it would change this REFUTE.
- **The cross-module phase-convention gap** (EM, `phase2_redteam_audit.md`
  §2c/§4.3) remains genuinely open — this run does not resolve it, only
  avoids amplifying it differentially between the two echo terms
  (`phase3_synthesis.md` Sec 3.4).
- **T28's own substantive mechanism question — the ~2.84° periodicity's
  origin — is not answered by this cycle.** Two boundary-reflectance-echo
  mechanisms are ruled out; the mechanism itself remains open, same as
  every prior cycle on this thread.
- The matched-`ε=μ` realizability caveat (mandatory fix 3) applies
  identically to this two-wall model — both walls use the same
  `reflection_coefficient` machinery, so the same "this is a statement
  about the engine's own numerical construct, not physically realizable
  `μ=1` absorber coatings" caveat carries over without new derivation.

---

## Reproduction

`python3 experiments/075-t28-absorb-boundary-wkb-reflectance/two_wall_cavity.py`
— writes `two_wall_cavity_results.json` in this directory. Deterministic
except the circular-shift null (fixed `seed=42`, reproduces bit-exact run
to run).
