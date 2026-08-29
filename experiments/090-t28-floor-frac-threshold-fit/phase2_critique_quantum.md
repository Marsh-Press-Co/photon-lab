# PHASE 2 — CRITIQUE · QUANTUM OPTICS · exp-090

## Verification performed (before the deliverable below)

Independently reproduced, from raw primitives and from scratch (no
statistics library), every load-bearing statistical claim this proposal
makes — not merely re-stated:

- **The 7-point margin table** (§2 Table 1): recomputed `margin(θ) =
  frac_contrast(θ)/FLOOR` directly from `experiments/087/088/089-.../
  results.json::frac_contrast` and `FLOOR=1.91744×10⁻⁴`. Reproduced
  **bit-exact**: sorted margins `1.3095(X), 1.4764(X), 2.1709(C), 3.8793(C),
  6.5889(C), 7.4946(C), 8.0187(C)` — no ties, AUC=1.0, matching §2 exactly.
- **P2 (exact permutation test)**: wrote my own enumeration of all
  `C(7,2)=21` label assignments and the Mann–Whitney/AUC statistic from
  scratch. Reproduced **exactly**: `AUC_obs=1.0`, `p=1/21=
  0.047619047619047616` (6 s.f. match to the proposal's own stated value).
- **P4 (Firth fit)**: implemented the modified-score Newton–Raphson update
  from the exact formula in §2's own table (`U*=Xᵀ(y−p+h∘(0.5−p))`,
  `H=W^{1/2}X(XᵀWX)⁻¹XᵀW^{1/2}`), independently, in 15 lines of NumPy.
  Converges in **20** iterations to `β=(1.7806,−5.6315)`, `m50=2.0710` —
  matches the proposal's own disclosed informal figure (`m50≈2.07`) to
  3 s.f. A parallel from-scratch naive (unpenalized) MLE does NOT converge
  in 200 iterations (`β→(203,−684)` and still climbing) — P1/P4's
  divergence-vs-convergence contrast holds up under independent
  re-implementation, not just the proposal's own claimed run.
- **P5 (LOO jackknife)**: enumerated all 7 leave-one-out 6-point subsets
  directly. Reproduces the proposal's own predicted pattern exactly — see
  Sharpest attack, below, for what this reproduction actually shows.

Everything the proposal cites numerically checks out. The finding below is
about what these correctly-computed numbers actually license, not an
arithmetic error anywhere in the document.

## Steel-man

Given R13's own founding complaint (a re-tuned knife-edge threshold is
premature) and Red Team's explicit exp-089 ask for a graduated caution
zone instead, the non-parametric zone (P3) is a genuinely disciplined
answer: a pure order statistic, zero free parameters, honestly reported as
wide (0.69, 47% of its own lower edge) rather than dressed up as tight.
The explicit refusal to regress on `frac_p_abs` (§5, on R13's-own-gate-
circularity grounds) and the explicit, pre-registered fallback if Firth's
`m50` disagrees with the zone (§7) show real methodological self-restraint
uncommon at this program's T28-desk-cycle scale. If Phase 5 needs a
defensible caution-zone recommendation from exactly 7 points today, built
from numbers already on the books, this is close to the most honest
version of that deliverable achievable without new FDTD.

## Sharpest attack

**P5's leave-one-out "stress test" is not falsifiable, and the proposal's
own P1 already proves this before a single LOO refit is run.** P1
establishes `AUC_obs=1.0` with **no ties**: every X-margin is strictly
below every C-margin. A basic property of order statistics — verified by
direct enumeration above, but derivable without running anything — is
that removing *any single point* from a strictly, tie-free totally
ordered set cannot un-separate the remainder: a subsequence of a strictly
ordered sequence is still strictly ordered. So "`AUC_LOO=1.0` in every
6-point subset" (P5's own stated falsifier: "Falsified if any LOO subset
loses full separation") is not an empirical outcome at all once P1 holds
— it is a deductive corollary of P1, guaranteed to pass with probability
1, for any 7-point dataset with `AUC=1.0` and no ties, regardless of
whether the underlying relationship is real physics or pure coincidence.
The same holds for the zone-edges half of P5: a min/max order statistic
over `n` points is provably unchanged by removing any point *other than*
the current argmin/argmax — so 5 of the 7 "exhaustive" refits (drop
36.0°/38.4°/38.8°/41.4°/41.8°) are guaranteed, a priori, to leave both
zone edges bit-identical (confirmed above: they do, to full float
precision), and the 2 informative refits (drop 40.2° or drop 37.2°) move
each edge to the *next* order statistic — again a deduction, not a
discovery. **P5 as specified contains zero bits of empirical information
beyond P1 itself.** Framing it as a "stress test" that "demonstrates the
separation is not an artifact of any single point," with a named
falsification condition, misrepresents a tautology as an empirical check
— the falsification condition can never fire given P1, so nothing was
actually risked. This is the mirror image of the naive-MLE hazard the
proposal itself is careful to name for P1/P4: an instrument dressed in
the language of a falsifiable test that cannot, in fact, fail.

## Verdict

**Support-with-changes.** The non-parametric zone (P3) and the Firth fit
(P4) are sound, independently reproduced bit-exact/to 3 s.f., and honestly
scoped (LOO-spread-as-uncertainty-proxy, no false CI claimed). But P5, as
written, should not be reported as a "stress test" with a named
falsification condition when that condition is mathematically unreachable
given P1 — a future citation of "P5 confirmed the zone is not fragile to
a single point" would misstate what was actually shown (a deduction, not
a measurement). This does not undermine the zone (P3) itself, which needs
no LOO corroboration to stand as a correctly-computed order statistic —
it undermines only the specific evidentiary weight P5 claims to add on
top of it.

**Secondary, non-fatal observation (not the primary attack, disclosed for
completeness):** P2's own framing — the permutation test "certif[ies] the
separation is not a 7-point coincidence" — invites more than the test
actually buys, for a related but distinct reason. `margin` and `Y` are
not exogenous to each other: `margin∝frac_contrast` and
`Y=1{frac_p_abs/frac_contrast>10}`, so the two share the same underlying
term. Concretely, the three points with nearly identical `frac_p_abs`
(40.2°: 7.100×10⁻³, 41.4°: 7.233×10⁻³, 41.8°: 7.214×10⁻³, within 2% of
each other) get *different* labels (X, X, C) purely because their margins
differ (1.48, 1.31, 6.59) — exactly R13's own founding denominator-pole
logic, and exp-089's own decomposition already attributes ~90% of the
swing to the denominator alone. Given that, near-perfect rank separation
by margin is close to expected once `frac_p_abs` stays within roughly one
order of magnitude across the window — the 21-way enumeration is correct
arithmetic, but "not a coincidence" reads as stronger, more independent
evidence than a test built on an already-mechanistically-explained
relationship can honestly supply.

## Parameter change that would flip toward unqualified support

Drop the "falsifiable"/"stress test" framing from P5 entirely — report
the LOO enumeration, if kept at all, as a deterministic illustration of
which single point each zone edge is sensitive to (informative for
communicating the zone's construction), not as a pre-registered
prediction with a falsification condition. Pair this with one sentence
next to P2 stating plainly that the permutation test corroborates, rather
than independently discovers, the margin–outcome relationship already
established mechanistically by R13/exp-089's own numerator/denominator
decomposition. Neither change alters P3's zone or P4's `m50` — both stand
as computed.
