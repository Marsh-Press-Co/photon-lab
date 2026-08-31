# Panel Iteration 75 — Phase 2 Critique (PHOTONICS)

## 1. Steel-man (≤150 words)

Items (i)/(ii) are disciplined R4/R17 house-keeping: they reapply the
already-audited ±0.5° desk bound (exp-096, Red-Team-ratified) verbatim
rather than re-deriving a new figure per null, cite `q8.crossings_deg`
(exp-090) byte-exact, and use quartile spacing (0.333° stride) finer than
the largest known cpl20→cpl30 migration (0.377°) — a real design
improvement over exp-095's 2-point ±0.10° bracket that could hide a
crossing between same-sign samples. Item (v) finally schedules the
grazing-incidence validity item MATERIALS/Director flagged (exp-097),
outstanding 10-11 cycles, at genuinely zero marginal FDTD cost — GP1
(passivity) and GP3 (reciprocity code-read) are both well-posed, cheap,
legitimate desk checks, and Idealizations 46-50 disclose scope limits
honestly rather than overclaiming.

## 2. Sharpest attack (≤150 words)

GP2 cannot do what §4's table claims. `dg048._geom_derived(g)` takes no
`theta` argument — `gd["r"]` is fixed by aperture/observation-plane
geometry alone. `FastEval.__init__` (exp-085's `phase4_derivation.py:
88-95`) computes `gd`/`G0` once per geometry, reused across every θ; I
confirmed numerically (`CFG_C40`, λ=600nm cpl=20): `kr_min=k·min(r)=70.06`,
IDENTICAL at all 21 swept angles — VALID (≥2π) trivially, always, by
construction, not physics. GP2 can never report a θ* boundary. Worse:
GP1's `weber(bo,bf)` is a ratio — an amplitude blow-up cancels in
`(b_obj-b_flank)/b_flank`, invisible to the ≥−1 bound. This seat's own
prior finding (`experiments/086-.../phase5_review_photonics.md:120-135`)
already traced this model to "a bare scalar Kirchhoff-Huygens sum... no
Fresnel-transition or UTD-style shadow-boundary correction term," causing
a **5,444×-6,631× amplitude blow-up at θc≈59°-73°** — inside this cycle's
30°-89.5° sweep. Neither GP1 nor GP2 can see it; item (v) will report
PASS/VALID uniformly and risks discharging the 10-11-cycle standing item
while never touching the failure mode this seat already proved real.

## 3. Verdict

**support-with-changes.**

## 4. Parameter change that would flip to support

Replace GP2 with a genuinely θ-dependent instrument before this cycle
runs: report `|C(θ)|` or `max(|Sx|)` (raw, unnormalized amplitude) across
the sweep alongside the ratio, and/or a per-θ effective-aperture/Fresnel-
number check that actually varies with incidence angle (e.g.
`kr·cos(θ)²`-type UTD-transition proxy, not the fixed propagation-distance
`kr_min`). If GP1/GP2 are run as specified, item (v)'s Phase-4 write-up
must state plainly, before any run, that both checks are structurally
blind to amplitude-scale blow-up and cannot themselves discharge the
standing grazing-incidence item — only bound a different, narrower claim
(propagator far-field validity, which is θ-independent for this bench and
was already knowable from a single evaluation).
