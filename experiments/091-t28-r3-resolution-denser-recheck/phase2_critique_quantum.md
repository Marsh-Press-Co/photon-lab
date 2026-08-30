# PHASE 2 — CRITIQUE · QUANTUM OPTICS · exp-091

## Verification performed (before the deliverable below)

Independently re-derived, from the already-committed record this proposal
cites, every number load-bearing to the two attacks below (not merely
re-stated): exp-089's own filed FLOOR-margin table (`results.json` via
`NOTES.md`) — 37.2°: 2.1709×, **40.2°: 1.4764×, 41.4°: 1.3095×** — and Red
Team's Phase-5 exp-089 crossing-distance re-derivation — **40.2°: 0.0654°,
41.4°: 0.0609°** from the nearest `delta_scene` zero-crossing, matching
this proposal's own §2b table (0.065°/0.061°) to 3 s.f. Also pulled
exp-069's own committed P-069-5 result (`ratio=1.97`/`2.50` at its two
test angles) and exp-069's own Phase-5 correction of that same band
(PHOTONICS/QUANTUM/EM, `phase4_results.md`), both directly relevant below.

## Steel-man

This cycle targets exactly the gap MATERIALS named at three consecutive
Phase-2/5 reviews (exp-088/089/090): the C40/G40 `PAIR_PAD` channel — the
instrument every caution-zone number in exp-090 and every classification
in exp-089 rests on — has never received R3's own mandated spatial
resolution check at any angle, let alone the two crossing-proximate
angles (40.2°/41.4°) setting the caution zone's own lower edge. Unlike
hedged prior passes, §4(b) states plainly, before any data exists, that a
full CONFIRM on (a) can still flip (b)'s classification, and treats
hold/hold, hold/flip, and flip/flip as equally informative outcomes — a
genuinely two-sided, no-lean prediction at precisely the two angles this
sub-thread's confidence is thinnest on, matching the honest-disclosure
standard R8/R9/R14 exist to enforce.

## Sharpest attack

§4c2 picks θ=40.2° as the *sole* settling spot-check angle, calling it
"this cycle's thinnest-margin, most crossing-proximate angle" — but the
proposal's own §2b table and exp-089's committed record say otherwise on
both metrics available: FLOOR margin is 1.4764× at 40.2° vs. **1.3095× at
41.4°** (41.4° is thinner), and crossing distance is 0.065° vs. **0.061°
at 41.4°** (41.4° is closer). By the record this proposal itself cites
bit-exact, **41.4° is the harder case on both counts, not 40.2°.** Since
(b) separately flags 41.4° as carrying this cycle's largest `ratio_k`
(28.81, its own "no confident lean" case), the one settling check meant to
certify `R3_STEPS=4200` at the hardest point instead validates the
second-hardest — leaving the actual worst case's settling adequacy
unverified. This is a single-point selection error in the design itself,
not a debatable judgment call: a mislabeled "hardest case."

## Secondary observation (not the primary attack, disclosed for completeness)

Reusing P-069-5's `[0.3,3.0]` band as the (a) CONFIRM criterion imports a
known-generous instrument, not a neutral one. Its own founding record
(exp-069 Phase-5, three independent seats, `phase4_results.md`) found this
exact band — at cells also sitting near a `delta(θ)` zero-crossing — CONFIRMed
(`ratio=1.97/2.50`) while *not* establishing resolution convergence of
location/amplitude; the passing ratios themselves already sit almost
exactly where they'd need to be (>2.51 at 40.2°, >2.88 at 41.4°) to flip
(b)'s classification. So (b)'s "logically separable" framing is arithmetically
correct but undersells the coupling: this program's own only directly
analogous precedent produced ratios in the exact range that make a
CONFIRM-on-(a)/flip-on-(b) outcome the *expected* case, not an edge case,
here — and a CONFIRM on (a) using this specific band would license the same
"resolution-converged" overclaim risk exp-069's own record had to retract.
Reusing the band without re-verifying it against this pair's own crossing
curvature is the R8 shape: an unverified cross-application, not a computed one.

## Verdict

**Support-with-changes.** The design correctly discharges a real,
repeatedly-flagged instrument gap and is honest about the coupling risk
in principle — but its own settling-adequacy safeguard (§4c2) is pointed
at the wrong angle by the record's own numbers, and its reused CONFIRM
band (a) carries a documented history of passing without resolving the
exact question it is being asked to answer here.

## Parameter change that would flip toward unqualified support

Run the §4c2 settling spot-check at θ=41.4° (or both 40.2° and 41.4°)
instead of 40.2° alone — the angle the proposal's own cited FLOOR-margin
and crossing-distance numbers show is actually the thinnest-margin,
most crossing-proximate case.
