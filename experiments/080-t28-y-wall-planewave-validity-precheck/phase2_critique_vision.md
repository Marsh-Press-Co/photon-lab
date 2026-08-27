# PHASE 2 — CRITIQUE · VISION SCIENCE · Panel Iteration 57 · exp-080

*Fresh sub-agent, blind to the other Phase-2 critiques this cycle. Charter
duty: pin numeric perceptual thresholds before any run scores against them.
This cycle makes no perceptual claim, so my load-bearing task here is a
**pre-registration/scope-discipline audit**, independently verified against
git history and code, not a threshold-pinning exercise.*

---

## 1. Steel-man (≤150 words)

`phase1_proposal.md` is exactly what LOGBOOK's own T28 opening entry calls
it: instrument/model-fidelity work, "T1 route N/A, constraint 3 not
engaged." I independently grepped the full text for
witness/constraint/invisib*/perceptual/ambient/silhouette/scotopic/
photopic/contrast — zero hits. "Observer" appears exactly once, in a
parameter-table row (`dist_image` = image-to-observer *propagation
distance*), a pure ray-geometry quantity, not a visibility claim. The
document never invokes PANEL.md's "witness realism" metric row, never
implies the aperture-summary question bears on constraint 3, and states
plainly (§0) that "nothing here asserts a real y-wall echo... or any
dominantly-real Δε mechanism." This is disciplined scope-holding across a
third consecutive y-wall cycle where drift into implicit relevance-claims
would have been easy and gone unchallenged by six of seven seats.

## 2. Sharpest attack (≤150 words)

Independently verified via `git log -p`: exactly two commits exist
(`6fb6b99` freeze, `23203cc` results, 2m21s apart). The frozen commit's §4/§5
text matches `validity_precheck.py`'s constants exactly
(`FORECLOSE_RATIO=0.10`, `FORECLOSE_SPREAD=1.5`, `SUPPORT_R2=0.90`,
`SUPPORT_FLOOR_R2=0.75`, `REFUTE_R2=0.50`) — thresholds are genuinely
pre-registered, not adjusted post-hoc. But §5's contingency table, itself
frozen pre-run, routes **two of its three named branches**
(FORECLOSE+SUPPORT *and* FORECLOSE+INCONCLUSIVE) to "proceed to
PHOTONICS' build anyway"; only the narrow FORECLOSE+REFUTE branch (mean
R²<0.50, a low bar the observed 0.7345 clears easily) doesn't. Given (a)
was itself near-certain FORECLOSE (the proposal admits reusing exp-079's
own already-known 0.76–2.15%/2.6–2.75× figures, "I expect it to reproduce
closely"), "proceed anyway" was the near-default outcome across the
plausible (b) range, not a risk-sensitive finding earned by this run's own
result.

## 3. Verdict: **support**

No constraint-3/witness-relevance smuggling found; pre-registration
integrity (thresholds and the contingent recommendation) holds up under
independent git and JSON verification — every scored number I spot-checked
against `validity_precheck_results.json` matches the write-up exactly. The
attack above is a rigor-caveat on how much *weight* Phase 3 should assign
to "proceed anyway" as a discovery versus a structurally-favored default —
it does not identify a scope-discipline or pre-registration violation.

## 4. Parameter change that would flip my verdict

If Phase 3 or the PHOTONICS build cites this cycle's "proceed anyway" as
independent evidence the plane-wave construction is *likely* to succeed
(rather than merely "not foreclosed, worth trying"), or drops the
LOGBOOK T28 framing ("T1 route N/A, constraint 3 not engaged") when
carrying this cycle's language forward — that would flip me to
oppose/support-with-changes.
