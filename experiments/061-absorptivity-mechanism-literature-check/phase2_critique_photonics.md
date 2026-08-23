# Phase 2 — PHOTONICS blind critique (exp-061 / Iteration 38)

*Fresh sub-agent, blind to the other four Phase-2 critiques and to Red
Team. Charter: surface interaction, absorption spectra, angular
dependence, scattering cross-sections. Owns: is the proposal's optical
response coherent as stated, across wavelength and angle?*

**Steel-man (146 words).** The proposal's α≈1.667×10⁵ cm⁻¹ target is
optically well-posed as a *search target*: it's a single, honestly-derived
scalar (τ_shell/thickness) with explicit units, and the search plan
correctly segregates conductive-loss-dominated CNT-forest sources
(structurally the right comparison class for `graded_black_shell`'s
`eps_max=1.0` homogeneous-conductivity abstraction) from
index-grading-dominated black-silicon/moth-eye sources, refusing to pool
them. The falsification criterion (MP-4) requires BOTH a matched-α AND a
matched-thickness hit, closing the obvious "cite a thick sample" escape
hatch. The reasoning correctly anticipates that real CNT forests are
dilute, structurally-trapping media rather than homogeneous Beer-Lambert
absorbers, which is exactly the right optical distinction to draw before
comparing a bulk α across two structurally different absorption
mechanisms — this is the one part of the reasoning that is genuinely
optically sound.

**Sharpest attack (150 words).** The α being checked isn't even *this
program's own* graded-profile absorption coefficient. `TAU_SHELL=24`
(design_geometry.py) is `sigma_max_fixedabs(r)×thickness` = 0.5×48, i.e.
peak-σ times full thickness — the graded profile is never actually
integrated. But exp-060, for the *identical* object (r_in=30, r_out=78,
sigma_max=0.5, 48-cell shell), explicitly computed the graded profile's
own raw σ-line-integral: `sigma_max*(181/462)*(r_out-r_in) = 9.4026` —
2.55× smaller than 24. And exp-060 then showed even *that* raw integral
overstates true attenuation-weighted depth (Im(n) concavity, ~8.3%). So
the α handed to Phase 4 for a literature comparison is a legacy
self-similarity bookkeeping constant (Iteration 7, exp-030), never
reconciled with this program's own more careful, more recent, and
explicitly-cited (exp-060) computation of the same shell's actual
absorption. It's the wrong quantity before the CNT-forest question is
even asked.

**Verdict: support-with-changes.** Item (B) is sound and independently
verified below. Item (A)'s search plan and non-pooling discipline are
good, but the target number itself needs reconciling against exp-060's
σ-integral (9.40, not 24) and its Im(n) correction before Phase 4 spends
a literature search on a mis-derived α — MP-1/MP-2's bands would shift
materially (the "α≈1×10³–3×10⁴ cm⁻¹ vs 1.667×10⁵" gap narrows to more
like a 4× gap at τ=9.4, not 17×, which changes whether MP-4's UNOBTANIUM
call is as clear-cut as predicted). Secondary, lower-priority: the
comparison is scoped to one wavelength/one implicit dispersion-free α;
this program's own T21 fringe-mechanism and Iteration-19 chromatic
findings are not invoked to ask whether a single-number α comparison is
even the right lens, though this is a minor gap next to the primary one.

**Flip condition:** re-derive τ_shell for THIS check as the graded
profile's actual σ-line-integral (9.4026, following exp-060's own
method) rather than `sigma_max×thickness`, restate α/MP-1–MP-5 against
that anchor, and re-run before Phase 4's search executes.

## Tool verification (run myself, from `/home/user/photon-lab`)

`python3 lab/caveat_lint.py` → exit 0, 3 caveats checked, 0 required-site
failures, all 3 registry entries' `required_sites` PASS, several
WARN-level candidate sites correctly surfaced (e.g. `lab/materials.py`,
`experiments/060.../run.py` mention `uniform_lossy_shell` without
restating the Fresnel caveat — expected, non-gating).

`python3 lab/caveat_lint.py --selftest` → exit 0. Pre-fix commit
`d5b4844`: phrase ABSENT (expected) → PASS. Post-fix commit `4f29982`:
phrase FOUND (expected) → PASS. Self-test genuinely discriminates the
two real historical revisions — confirmed by direct execution, not just
trusting the prose.

Independently re-ran `python3
experiments/052-fixed-absolute-thickness-shell/design_geometry.py`: it
printed `thickness=1440.0nm, tau_shell=24.0, alpha=0.016667/nm,
e-fold length=60.00nm`, matching the proposal's cited figures exactly —
R4 (re-derived, not hand-typed) is satisfied in the narrow sense. The
problem the sharpest attack raises is one level up: the *code being
invoked* computes the wrong quantity, not that the proposal mis-
transcribed it.

**Does the tool's design hold up under PHOTONICS' lens?** Mechanically,
yes — loose ANY-OF regex matching, non-gating WARN tier, and a
hand-curated registry are reasonable choices for a documentation-
completeness lint, and its own reasoning for staying outside `run_all.py`
(documentation-completeness vs. physics-measurement gate) is sound and
consistent with what I observed running both tools. One gap from this
discipline specifically: the registry has no entry tracking *this*
critique's own class of defect — a numeric quantity (like `tau_shell`)
computed two different ways in two sibling experiments without a caveat
requiring them to be reconciled or cross-referenced. The tool greps for
phrase propagation, not for a *number* being redefined inconsistently
across files; that failure mode (a wavelength/angle-dependent or
magnitude quantity silently meaning two different things in two
experiments) is exactly the kind of thing this cycle's own item (A) just
tripped over, and the registry's `trigger_terms` mechanism could in
principle flag it (e.g. a `tau_shell` trigger with two DIFFERENT numeric
literals found at candidate sites) but currently doesn't attempt numeric-
value cross-checking at all — it only checks phrase presence/absence.
