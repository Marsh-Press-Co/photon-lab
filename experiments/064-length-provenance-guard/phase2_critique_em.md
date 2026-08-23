# exp-064 — Phase 2 Critique: ELECTROMAGNETISM (blind)

**Seat charter applied:** field/wave behavior, impedance matching, energy
coupling; reciprocity/passivity/causality bookkeeping; formalizing what T1
permits and forbids. This cycle scores no T1/constraint metric (N/A,
correctly stated) — the charter work here is auditing whether the guard is
a *sound formalization* of the physical rule this seat and PHOTONICS
argued to a conclusion at Iteration 23/31.

---

## Steel-man (≤150 words)

The allow-list-over-deny-list decision (§7) is the single most defensible
EM-grounded design choice here. T23's underlying physics is that σ_ext
ties to the imaginary part of the forward-scattering amplitude — a
coherent/diffractive quantity — which can exceed a solid's geometric
cross-section for resonant or sub-wavelength scatterers; that mismatch is
a general wave-optics property, not a fact peculiar to `w_on` or
`L=τ_true/α`. A deny-list of today's two known-bad lengths would leave the
guard blind to whatever NEXT extinction-derived quantity a future
proposal invents — exactly how T23 itself survived three deferred cycles
on a prose rule nothing checked. Requiring `length_provenance` as a
keyword-only, no-default parameter (QP-1/gate 4) closes the specific
failure mode that let a legacy call silently keep compiling unguarded.
The `correction_factor≡1` recovery identity (gate 1, k_solid→∞) is a
genuine, load-bearing absolute-identity gate in PANEL.md's sense, not
decoration.

## Sharpest attack (≤150 words)

The allow-list encodes provenance-TIER (measured vs. constructed vs.
optically back-calculated), not provenance-ROLE — which physical entity a
length belongs to. Nu=2's h=k/L reduction is licensed only when L is the
solid's own characteristic dimension; an honestly-measured gap/standoff
distance or aperture width is equally 'bench_construction' or
'measured_geometric' under the guard's own text, yet feeding either into
the same formula silently swaps in a different conduction regime
(bounded-gap or diffraction-governed) sharing the algebra, not the
licensing conditions. The docstring says 'of the modeled solid body';
`_validate_length_provenance` never checks that, only the tag string.
Worse: stage-24 gate 3 only proves the diagnostic path reproduces
exp-063's numbers when called WITH the right flag — nothing gates whether
`run_all.py`'s actual `L_MP5_730X_M` sites get retagged. QP-3's
falsification is enforced by Phase-3 discipline, not code — the exact
failure shape T23 itself is.

---

## Discussion (supporting the two items above, not a third headline)

**On the allow-list vs. the entity/role question.** The docstring text for
`bench_construction` ("a real, directly-specified physical dimension of
the modeled solid body") is stricter than what `LICENSED_LENGTH_
PROVENANCE` + `_validate_length_provenance` actually enforce: the code
accepts any string equal to `"bench_construction"`, regardless of whether
the underlying float is the solid's own dimension or, say, a standoff gap
built with equal directness into the same FDTD scene. This program has no
live gap/standoff or aperture-length call site today (I checked — every
current and proposed call site is either `r_out`-class or the MP-5
extinction-derived `L`), so this is not (yet) a live violation, only a
structural blind spot — comparable in kind to the "declaration, not
detection" limit the proposal's own Idealization 1 already discloses.
I do not treat it as blocking on its own. It becomes relevant only in
combination with the second point below.

**On QP-3's falsification condition and stage-24's actual coverage.**
Requiring stage 23's three witness-scale calls to move to
`extinction_derived_diagnostic_only`/`diagnostic_only=True` is the
correct EM-grounded consequence of closing T23 — it is exactly what the
docstring's "NEVER an optical/extinction-derived length" bar already
implies once enforcement exists at all. But the four stage-24 gates as
specified do not verify that Phase 3 actually did this at the three real
call sites in `run_all.py`; they verify the guard function's *behavior in
the abstract* (raises on bad tags; is numerically inert on already-tagged
bench calls; reproduces exp-063's numbers when called correctly with the
diagnostic flag). A Phase-3 author could tag `L_MP5_730X_M` calls
`"bench_construction"` — a false but syntactically well-formed
declaration — and every one of the four gates as written would still pass
green, because none of them read the actual argument strings passed at
those three specific lines of `run_all.py`. This is not hypothetical
caution: it is the identical failure shape this program has now logged
repeatedly (the fix-docket-delivery pattern; T23's own three-cycle prose
deferral) landing inside the very mechanism built to end that pattern.

---

## Verdict: **support-with-changes**

The core design (allow-list, keyword-only required argument, the
correction_factor≡1 absolute identity, forwarding one provenance through
`mixed_length_scale_regime`'s internal calls rather than re-declaring per
sub-call) is EM-sound and should proceed. The one change needed before
this closes T23 for real:

**Single parameter change that would flip this to unconditional support:**
add a fifth stage-24 gate (or a `numeric_lint_config.json`
`derivation_consistency`-style entry, mirroring `exp063-cf-bench-vs-
witness-derivation`) that inspects `run_all.py`'s actual stage-23 source
— by `inspect.getsource`/text scan, not merely re-invoking the function in
isolation — and FAILs unless every `L_MP5_730X_M` call site passes
`length_provenance="extinction_derived_diagnostic_only"` and
`diagnostic_only=True` literally, in the committed file. Without that
fifth gate, QP-3's falsification condition — the one prediction this
cycle exists to make binding — is enforced by human/panel review at
Phase 3, exactly the mechanism T23 already proved unreliable three cycles
running.
