# exp-064 — Phase 2 Critique: PHOTONICS (blind)

**Steel-man (150 words max).** §7's argument is correctly stated and does
real work: the optical theorem ties σ_ext to Im[f(0)], a coherent/
diffractive forward-scattering quantity, not a ray-geometric one, so an
extinction-derived length (`w_on`, `L=τ_true/α`) can differ from — and for
a resonant/sub-wavelength scatterer substantially exceed — any real
geometric length of the object producing it (T9 already measures this
inflation for `w_on` on this bench). That is textbook-correct and it is
the right physical reason an **allow-list** (`bench_construction`,
`measured_geometric`) is the correct enforcement shape rather than a
deny-list of today's two known-bad examples: the failure mode is general
to wave optics, not particular to `w_on` or `τ/α`. Converting T23 from a
docstring into `_validate_length_provenance`, gated by an absolute-
identity refusal test (QP-4) and a zero-physics-change regression test
(QP-2/QP-5), is the right structural close after three prose-only
deferrals.

**Sharpest attack (150 words max).** §6's headline — real Vantablack
forest height "up to 14 µm" vs. the witness-scale need of 331–1051 µm,
"24×–75× taller" — silently equates forest HEIGHT with the single-pass
Beer-Lambert path length `L=τ_true/α` needed to reach τ_true. That
equivalence requires ballistic, normal-incidence propagation through a
homogeneous effective medium. A real CNT forest is a dilute (~1–10% fill),
vertically-aligned scattering mat — it is black precisely because it
multiply scatters and traps light, so photon transport through it is
diffusive, not a straight ray; the true absorption path for a given
physical height need not equal that height. Separately, and independent
of scattering: the target phenomenon is a SWEPT beam (constraint 4),
generally oblique — even in the pure-ballistic limit the geometric path is
`h/cosθ`, which alone can move the ratio in either direction depending on
θ and front-surface R(θ). §6 states one crisp multiplicative gap with
neither treatment disclosed, risking the number being cited forward as a
clean geometric-realizability finding rather than the angle/transport-
idealization-laden estimate it actually is.

**Verdict: support-with-changes.**

**Parameter change that would flip to plain support:** add one disclosed-
idealization sentence to §6 (matching the document's own §8 idealization
discipline) stating the 14 µm/331–1051 µm comparison assumes normal-
incidence, single-pass, homogeneous-medium (Beer-Lambert) transport, is
not corrected for angle-of-incidence path lengthening or scattering-
mediated diffusive transport, and is therefore a bound of unstated
direction, not a resolved thickness-realizability gap. This changes no
code, no gate, and no falsifiable prediction in §5 — it only prevents §6's
queued, disclosed-as-unresolved finding from later reading, in LOGBOOK.md
or PLAN.md, as more settled than it is.
