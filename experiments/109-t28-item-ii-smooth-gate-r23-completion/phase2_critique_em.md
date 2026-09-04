# PHASE 2 — CRITIQUE · ELECTROMAGNETISM · Panel Iteration 86 (exp-109)

Fresh sub-agent, blind to every other seat's critique this cycle. Read
PANEL.md, LOGBOOK.md in full, PLAN.md's Current state, the Phase 1
proposal, and its subject code before critiquing.

**Steel-man (≤150 words):**
The raw-std ≥ residual_std inequality is textbook-correct for this
specific design matrix. `A_mat = [1, 1/margin]` (in
`linear_fit_1_over_margin`) carries an intercept column, so the constant
model ŷ=mean(y) is a feasible point in the least-squares search space —
forcing RSS_opt ≤ RSS_constant, hence residual_std ≤ raw_std, with both
computed via the *same* n/ddof=0 divisor (no normalization mismatch to
hide a violation). I independently re-derived it and it holds exactly at
both r: 2.897e-6 ≤ 5.008e-6 (r=156), 2.102e-6 ≤ 2.124e-6 (r=312). Applied
to a CONFIRM verdict whose physical meaning is "the box-family
measurement floor sits safely below the independently-measured
|Δ_boxA| signal," raw_std is the correct conservative choice: it can
only push a verdict away from a false CONFIRM, never manufacture one —
consistent with this program's established null-result-skepticism
standard (R13/R14).

**Sharpest attack (≤150 words):**
§4 claims raw_std is "provably... more conservative... in every case."
That overclaims. The inequality only bounds stat *from below* (raw_std
≥ residual_std); it says nothing about REFUTE. Since REFUTE fires when
stat ≥ boxA, inflating stat via raw_std makes REFUTE strictly *easier*
to trigger — the fallback is conservative against false-CONFIRM but
simultaneously anti-conservative against false-REFUTE. At the two tested
r this is moot (raw_std sits 2.96×/5.81× below even the CONFIRM bar,
verified by independently recomputing `np.std(delta_values)` from
`results.json` — 5.00833e-6 at r=156, 2.12413e-6 at r=312, matching the
proposal's table to its claimed <1e-9 relative precision), so no outcome
flips here. But the *universal* "conservative in every case"
characterization is false for a future r/config where a trusted-detrend
fit would land AMBIGUOUS while the raw-std fallback pushes it past the
REFUTE bar — that case is coming, since Tier-2's own queued r=624 point
exists precisely to test a new margin regime.

**Verdict: support-with-changes**

**Change that would flip to `support`:** In §4(a) and in `stat_source`'s
non-smooth-branch string, replace "more conservative... in every case"
with an accurate two-sided statement: conservative w.r.t. false-CONFIRM
(never deflates the floor below the trusted-detrend estimate),
simultaneously liberal w.r.t. REFUTE (inflates the floor, so more
readily crosses the REFUTE bar) — so a future non-smooth REFUTE/
AMBIGUOUS reading is not silently read as "the safe, conservative
answer" the way this document's current framing would license.
