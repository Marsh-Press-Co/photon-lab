# PHASE 2 — CRITIQUE · PHOTONICS · Panel Iteration 60 · exp-083

**Seat: PHOTONICS.** Fresh sub-agent, zero memory of any prior session. Read
PANEL.md, AGENTS.md, LOGBOOK.md (RULED OUT R1–R9, ESTABLISHED, LIVE THREADS,
T28's history from its Iteration-46 origin through Iteration 57/exp-080 —
LOGBOOK.md itself has not yet been updated past exp-080; Iterations 58/59
read directly from `experiments/081.../` and PLAN.md's Iteration-60 queue,
which reconciles exp-082 in full), PLAN.md's Iteration-60 entry, the complete
`experiments/083-.../` record (`phase1_proposal.md`, `NOTES.md`, `run.py`,
`results.json`, `run_output.txt`, `null_permutation_control.json`), and my
own predecessor seat's article-edge-diffraction hypothesis
(`experiments/082-.../phase5_review_photonics.md`). Blind to this cycle's
other Phase-2 critiques, per PANEL.md.

**Independent verification performed.** I did not take the self-scored
numbers on faith. Read `run.py`'s `classify()`/`permutation_test_r()`
directly (the branch-band logic matches the pre-registered text exactly:
`REL_DEV_TOL=0.20`, `R2_FLOOR=0.30`, three mutually-exclusive-by-construction
bands). Pulled `results.json::primary_period_discriminator` directly and
confirmed the self-scored numbers bit-exact against the committed JSON:
`P*=2.9473684210526314°`, `R²=0.858195125110302`, `rel_dev_edge_a=0.0370`,
`rel_dev_edge_b=0.5031`, branch `B_ARTICLE_EDGE_DIFFRACTION` — all reproduce
from the file, not the prose. Confirmed `secondary_correlation` matches the
cited `r=0.39494`, `p=0.02806` exactly, and `null_permutation_control.json`
matches the null-control prose exactly (`R²_obs=0.8582` vs `null_max=0.6324`
for `delta_scene`; `R²_obs=0.4582` vs `null_max=0.5599` for the EM pair — I
note the EM-pair observed value does NOT exceed its own null max, contrary
to a reading of "exceeds the null" applied loosely to both; the correct,
narrower claim — `p=0.00185`, decisively below the null's 99th percentile —
is what the write-up actually states, and that claim is accurate). Pulled
`dg065.CONFIGS["C40"]`/`["G40"]` directly: `R_OUT=78` cells, `lever
(obj_x−plane_x)=93` cells, `y_lo/y_hi` span giving the source's own
`A_HALF_APERTURE=752` — confirming `P_edge_B=1.9608°` is a source-taper
quantity (`T_SINTHETA_600=CPL[600]/752`), structurally unrelated to the
article's own `R_OUT` at all, contra any implicit reading that both
reference periods are "article-adjacent."

---

## Steel-man (≤150 words)

This cycle did the statistics right. Three pre-registered bands, checked
non-overlapping by construction (0.278° clean margin), a bit-exact
reproduction precondition, and — new this cycle, not merely inherited — a
20,000-trial post-hoc null-permutation control showing `R²=0.858` exceeds
the *maximum* of 20,000 pure-noise shuffles of this exact data, not just a
p-value. EM's independent, structurally different (linear field-difference,
not Weber-contrast) instrument lands in the same period family with its own
fresh null control (`p=0.00185`). That two orthogonal constructions agree is
real, hard-won convergent evidence that `delta_scene`'s dominant periodicity
is NOT `P_continuity=4.611°` — a clean, well-supported negative result against
QUANTUM's mechanism-continuity hypothesis, correctly and honestly
distinguished from the separate question of what the periodicity actually
*is*.

## Sharpest attack (≤150 words)

"Branch B: ARTICLE-EDGE DIFFRACTION" has no mechanistic content for the
period actually recovered. `P_edge_A=2.8421°` is T28's own founding mystery
period — nine-plus dedicated mechanism cycles (desk batch, x-wall echo,
y-wall single-edge, y-wall full aperture, plane-wave y-wall) have tested and
REFUTEd every domain-echo candidate for it; nobody has ever derived it from
geometry. Landing on it doesn't identify a NEW article-rim mechanism — it
shows the article-loaded channel inherited the SAME unexplained quantity the
empty scene already produces. My own back-of-envelope two-rim-edge estimate
(`Δy=2·R_OUT=156` cells, `λ=20` cells, near-field-corrected) lands near 7–9°,
nothing like 2.84° — the "article rim diffracts" story doesn't obviously
predict this number either. The proposal's own §2 desk pre-check (rim as two
secondary apertures) — the one test that would actually derive rather than
pattern-match a period — was never run (`NOTES.md`, "Next," admits this).
Grouping the mechanistically-understood `P_edge_B` (T21 source taper, unrelated
to the article) with the unexplained `P_edge_A` into one "family" for scoring
purposes also borrows P_edge_B's legitimacy to dress up a match to a still-
mysterious number as an "established" outcome.

---

## Supporting discussion (not length-limited)

### 1. The branch label is a relabeling, not an explanation

Read plainly, "BRANCH: B_ARTICLE_EDGE_DIFFRACTION" asserts a mechanism. What
was actually tested is narrower: *does the recovered period sit within 20%
of either of two numbers borrowed from unrelated prior experiments?* Neither
reference period was derived from the article's own geometry inside this
cycle (or any cycle) — `P_edge_A` is a bare empirical fit from exp-069's
empty-scene `C80−C40` sweep (LOGBOOK Iteration 46: "a real, unexplained
~2.84° periodicity... settled and unexplained," a characterization that has
not changed through Iteration 57), and `P_edge_B` is T21's source-taper
fringe, a quantity about the *source's* raised-cosine aperture, computed from
`A_HALF_APERTURE=752`, with zero dependence on `R_OUT` or the article's
presence at all (confirmed directly in `dg065.CONFIGS` and
`design_geometry.py`, above). So a match to `P_edge_A` specifically — which
is what happened, at `rel_dev=0.037`, an order of magnitude inside tolerance,
while `P_edge_B` misses at 50% — is a match to the one candidate that has
never been mechanistically derived by anyone, including this cycle. Calling
that "article-edge diffraction, confirmed" overstates what a period-family
membership test can show. The honest headline is: *not* mechanism continuity
(ruled out with real margin); *possibly* the same still-unidentified
artifact that already haunts the empty scene, now also present with the
article loaded. That is a materially different, more open claim than
"a new interaction, the article's own rim, explains this" — and it changes
what should be searched for next (whatever produces T28's original empty-
scene mystery, not a fresh article-scattering derivation).

### 2. A quantitative sanity check the cycle itself could have run cheaply

Treating the article's own top/bottom rim (`Δy=2·R_OUT=156` cells) as a pair
of coherent secondary sources at the object plane, illuminated by a beam
swept near θ≈39°, observed at `lever=93` cells downstream: a simple two-point
interference-fringe estimate gives `Δθ ≈ λ/(Δy·cosθ) ≈ 20/(156·0.777) ≈
9.5°` — 3× too large. Even allowing generously for the true construction
being some other combination of these lengths (near-field, not the naive
far-field two-slit formula I used), this is exactly the kind of check
PHOTONICS' own predecessor review named as the necessary next step *before*
trusting the label — "a coherent-sum construction treating the article's own
two rim edges as a pair of secondary apertures... an independent, mechanistic
check of WHY Branch B's period sits where it does, not merely that it does"
(`phase5_review_photonics.md` §2) — and it was not run this cycle either
(`NOTES.md`, "Next," item 2, explicitly deferred). Until it is, "article-edge
diffraction" is a name, not a demonstrated mechanism, for this specific
result.

### 3. The r=0.395/p=0.028 tension: the "multiple-comparisons" framing is not
   the whole story, and cuts a way the write-up doesn't discuss

The disclosed leakage explanation — two different-period sinusoids over a
short window are not fully orthogonal — is directionally correct but
under-argued as stated. Quantify it: `delta_scene`'s recovered frequency is
`f_A=1/2.9474=0.3393` cycles/deg, `delta_empty`'s is `f_C=1/4.6113=0.2169`
cycles/deg, `Δf=0.1224` cycles/deg, window `W=6°`. `Δf·W≈0.73` — *below* the
Rayleigh/sinc-null resolution limit (`Δf·W=1`) for cleanly separating two
frequencies over a finite window. That does support "some correlation between
differently-labeled series is expected even if the true generators are
independent" — but it cuts the other way too: at `Δf·W<1`, a single free-
period fit is not guaranteed to cleanly assign a genuinely mixed
(two-component) signal to one dominant period either. Idealization 7 already
flags this possibility explicitly and leaves it open; the correlation figure
is independent, real evidence that the mixture question is not merely
hypothetical here — it is exactly the pattern a partial-continuity admixture
would produce. "Multiple-comparisons caution" is an argument for not treating
`p=0.028` as a confirmed detection of shared mechanism; it is not an argument
for treating the primary single-period branch classification as immune to
the same window-resolution limitation. The two-tone superposition fit
`NOTES.md` proposes as a "Next" item is the actual adjudicating test for
both concerns simultaneously and was not run this cycle — I'd weight it
higher than the write-up currently does, given it bears directly on whether
Branch B's own `P*=2.9474°` is a clean single tone or a resolution-limited
blend.

---

## Verdict: **support-with-changes**

The FDTD work, the reproduction precondition, and the null-permutation
statistics are sound and independently verified above — I found no numeric
error. What needs to change before this cycle's headline stands as written:
(1) demote "ARTICLE-EDGE DIFFRACTION" from an asserted mechanism to what was
actually shown — a period-family match to T28's own unexplained `P_edge_A`,
explicitly flagged as *not yet mechanistically derived from the article's
geometry*; (2) do not let `P_edge_B` (a fully-understood, article-independent
source-taper quantity) continue lending "established" credibility to a
`P_edge_A` match by classification-bucket proximity alone; (3) the
correlation tension needs the two-tone fit, not just a multiple-comparisons
disclaimer, before "resolved" is the word future cycles inherit.

## Single parameter change that would flip my verdict to full support

Run the zero-FDTD article-rim two-secondary-aperture desk pre-check
(`phase5_review_photonics.md` §2, exp-082) and have it *independently derive*
a period within 20% of `2.8421°` from `R_OUT=78`/`lever=93`/the swept-angle
geometry alone — a genuine first-principles prediction, not a post-hoc match.
If that check instead predicts something far from `2.84°` (as my own rough
estimate above suggests it might), that would sharpen my attack into an
outright oppose on the mechanistic label, though not on the underlying
period-family statistics, which would still stand.
