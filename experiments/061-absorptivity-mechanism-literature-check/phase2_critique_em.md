# Phase 2 — ELECTROMAGNETISM blind critique (exp-061 / Iteration 38)

*Fresh sub-agent, blind to the other four Phase-2 critiques and to Red
Team. Charter: field/wave behavior, impedance matching, energy coupling.
Owns the reciprocity/passivity/causality bookkeeping — formalizes what T1
permits and forbids for each proposal.*

### Steel-man (148 words)

The mechanism narrative is honest about what it is: a dimensional-
bookkeeping realizability check, T1-inert by design, in the same
zero-metric category as exp-036/037. Re-deriving α from
`design_geometry.py` rather than hand-typing it (R4) is the right
discipline, and I confirmed the number: `python3 design_geometry.py`
prints `alpha=0.016667/nm, e-fold length=60.00nm`, exactly matching the
proposal's headline figure — no transcription drift. The falsification
design is genuinely two-sided: MP-3's "NOT FOUND" prediction is stated as
the single most falsifying possible outcome for its own thesis, and MP-5
pre-commits to a graceful downgrade (PLAUSIBLE-at-larger-thickness)
rather than a binary kill. Comparing an effective forest-level literature
α against this bench's α under an explicit, disclosed idealization
(idealization 3) — rather than silently assuming Beer-Lambert applies to
real CNT structure — is the correct epistemic posture for a desk cycle
with a standing WebFetch block.

### Sharpest attack (150 words)

α is not honestly re-derived from field physics; it's `TAU_SHELL /
THICKNESS_NM`, where `TAU_SHELL = sigma_max_grid × thickness_cells` — a
raw grid-conductivity line-integral. This program already established
(exp-060, same panel history) that this exact quantity does **not** equal
true field-attenuation depth once loss is order-unity: `Im(n(σ))` is
concave in σ at this bench's normalization, producing an ~8.3% disclosed
residual at loss tangent t≈0.62 — and that correction itself only exists
because EM's *own* first attempt miscalculated t by dividing by
`sim.omega` instead of the physical frequency, a 1/S≈4.42 units bug Red
Team had to catch. `graded_black_shell`'s peak σ_e=0.5 (eps_r=1
throughout, confirmed) gives t≈1.59 via the established `t=σ·cpl/(2π)`
route — deeper into the nonlinear regime than the case that already
needed correcting — yet exp-061 never computes t, never solves
n=√(1+it), never invokes α=2ωIm(n)/c. It substitutes a length-unit bridge
(dx=30nm, genuinely valid) for a physics bridge (loss-tangent→Im(n)→α,
genuinely required) and treats the resulting number as though it were
the latter. The 1.667×10⁵cm⁻¹ figure is real grid arithmetic; whether it
is a physical absorption coefficient at all is unestablished.

**Verdict: support-with-changes.**

**Single change that would flip to support:** add one line deriving α
properly — compute t=σ(r)·cpl/(2π) across the graded profile, solve
n(r)=√(1+i·t(r)), integrate Im(n) radially to get the true attenuation-
weighted α, and report that number (not the raw line-integral one) as the
literature comparator. Given exp-060's residual was ~8.3% at t≈0.62 and
this shell's peak reaches t≈1.6, I'd expect the naive figure to be off by
tens of percent at minimum in the high-σ region — plausibly enough to
matter against MP-1's 1–2-OOM literature band, but not obviously enough
to flip MP-4's UNOBTANIUM verdict, so I do not oppose outright.

### On R1 / T1 escape-route territory

"NONE" is correct for *scoring* (no constraint metric evaluated). But
it's worth stating explicitly, not left implicit: `graded_black_shell` is
a purely passive, always-on, LTI medium — by T1's own central tension,
such a mechanism can *never* clear constraints 1+2+3 jointly at photopic
ambient on its own. Whatever this cycle's verdict on α turns out to be,
it can only ever bound a component of the "sub-threshold operation
(scotopic ambient)" escape route, not a general solution — the proposal
doesn't say this, and should, since a future reader could mistake a
favorable realizability verdict here for progress toward a
photopic-clearing (Tier-A) result.

### Tool verification (run myself, both from `/home/user/photon-lab`)

- `python3 lab/caveat_lint.py` → exit 0, 3 caveats checked, **0
  required-site failures**, several WARN candidate sites correctly
  surfaced (matches the proposal's claim exactly).
- `python3 lab/caveat_lint.py --selftest` → PRE-FIX (d5b4844) phrase
  ABSENT as expected, POST-FIX (4f29982) phrase FOUND as expected,
  "Self-test PASSED", exit 0.
- Both match the proposal's reported output verbatim; the tool's claims
  are genuine, not narrated.

**Missing registry entry, my discipline's own history:** the tool tracks
exp-060's *sigma_flat-matching* caveat but not the *prior, distinct* EM
bookkeeping bug in the same cycle — the original Fresnel-reflectance
calculation dividing by `sim.omega` (per-step phase advance) instead of
the physical angular frequency, a real ~4.42× correction Red Team had to
catch before EM's number could be trusted. That correction lives only in
prose (`NOTES.md`, this cycle's own history) with no
`caveat_lint_config.json` entry, no `required_sites`. Given exp-061 now
reproduces the same *species* of error (grid quantity treated as physical
quantity without the frequency/loss-tangent bridge), that omission is not
hypothetical — it should be registered before, not after, the next time
someone re-derives a σ→α figure.
