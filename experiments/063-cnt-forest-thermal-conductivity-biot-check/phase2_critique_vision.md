# VISION SCIENCE — Phase 2 Critique of exp-063 Phase 1 Proposal

*Fresh sub-agent, blind to the other six seats' current-cycle critiques.
Charter: human perceptual limits — contrast thresholds, luminance edge
detection, spectral sensitivity, adaptation, temporal sensitivity,
saccadic/attentional blindness. Central question: what would make a human
eye FAIL to register something physically present? Standing duty this
cycle: registry-propagation check for this cycle's own new numbers/
machinery, per the Director's Iteration-40 pre-flight work.*

## 1. Steel-man (≤150 words)

The proposal's real virtue from this discipline's lens is what it
correctly refuses to claim: §2 states up front "zero constraint-1/2/3/4
metric scored," and Idealization 1 discloses its own 1D front-flux/
rear-loss geometry as deliberately worst-case, not a claimed physical
picture — it never dresses a thermal correction up as a constraint-3
finding. The derivation is honest about direction (the correction factor
is provably ≥1, never manufacturing a spurious cooling result), carries a
real absolute-identity gate (κ_solid→∞ recovers `dt_ss_full` exactly,
factor→1), and both headline predictions (TD-3/4 bench, TD-5 witness) are
pre-committed bands with falsification conditions stated before any
search runs — the house discipline my own charter has repeatedly had to
fight for (T18/NETD, Iteration 17/20). Sourcing κ_solid at all, after 15
iterations of silicon's unsourced 148 W/(m·K) placeholder, closes a real
instrument-fidelity gap rather than opening a new detection channel.

## 2. Sharpest attack (≤150 words)

TD-3/4/5 restate "UNDETECTABLE"/"DETECTABLE" classifications at the exact
table cells a future reader will quote, but none of the three carries the
mandatory disclaimer this program's own Iteration-17/20 Checkpoint-4
firing forced into permanent code: `thermo_sidecar.netd_disposition()`
and `mixed_length_scale_regime()` both hard-code "NETD is an instrument/
detector threshold, not a human perceptual one ... does NOT bear on
constraint-3/4's human-eye verdict" at every dict they return. §2's
generic "zero constraint metric scored" sentence is exactly the "stated
once in a methodology section, not at the point of the claim" pattern Red
Team's own attack 7 ruled insufficient. This matters more here than in
any prior cycle: TD-5 explicitly frames a κ<0.0897 outcome as this
program's "first-ever thermal-detectability classification flip,"
Checkpoint-1/2-adjacent, requiring escalation — precisely the condition
under which an excited Phase-4/5 write-up or Marsh notification is
likeliest to conflate "DETECTABLE by microbolometer" with "visible to the
eye at rest," reintroducing the exact scope-tag conflation this charter
exists to prevent.

## 3. Special standing duty — registry-propagation check on this cycle's
own new numbers/machinery (mandatory, stated regardless of verdict)

**Scope-boundary, stated precisely (per the task brief):** if TD-5
resolves toward DETECTABLE, that is an *instrument*-detectability
finding (microbolometer NETD, ~8–14µm mid/long-wave IR) — it does not,
by itself, touch constraint 3 (a black silhouette visible to a human
observer at rest under ambient light). Human photopic/scotopic vision
tops out well below 750nm; nothing in this program's IR band is in
spectral range for any human visual mechanism this charter governs
(cone/rod spectral sensitivity, adaptation, contrast thresholds — none
apply to thermal-IR emission). A DETECTABLE flip would be a real,
escalation-worthy finding for an instrumentation reader, but it answers a
different question than the one my charter polices, and the proposal
should say so exactly where TD-5 is stated, not leave it to be inferred.

**New numbers/machinery this cycle proposes, and their registry status:**
`biot_number`/`front_surface_conduction_correction` (new committed code),
κ_CNT-forest (new sourced number, band [0.1,20] W/(m·K)), and
κ_critical≈0.0897 W/(m·K) (a new, singular, load-bearing falsification
threshold — the single most consequential number this proposal
produces) have **no `lab/caveat_lint_config.json` entry today**, and
none of the existing six entries' `trigger_terms` would match text like
"κ_critical," "0.0897," or "Biot number front-surface correction" even
under the now-generic `experiments/*/phase*.md` `candidate_globs` (fixed
Iteration-40 pre-flight item 0) — that widening fixes *discovery* for
already-registered claims, it cannot discover a claim that was never
registered at all. Idealization 8 acknowledges this only as "whatever
new sourced numbers need a registry entry at Phase 3/5," deferred and
unspecific — no draft `id`, `trigger_terms`, or `phrase_patterns` is
proposed. Separately, and more concretely: this proposal's own headline
mechanism — one correction-factor formula applied identically at TWO
length scales (bench L=2.34µm, TD-3/4; witness L=1051.2µm, TD-5) to
produce two different corrected margins — is the exact shape
`lab/numeric_lint.py`'s `derivation_consistency` kind exists to check
(its own module docstring names exp-062's EM-6/EM-7 R-vs-T drop as the
regression case; this proposal's bench-vs-witness split is a structural
twin). κ_critical=0.0897 itself, once it propagates to LOGBOOK.md/
PLAN.md/NOTES.md at Phase 3/5, is also a textbook `numeric_drift`
candidate. The proposal explicitly declines to engage `numeric_lint.py`
at all ("a separate, already-assigned item, not re-proposed or annexed
here") — true of its *ownership*, but the tool is live, self-tested, and
built one commit before this proposal; declining to register against it
is a choice this proposal should own, not wave past.

**Recommendation for Phase 3, before freeze:** (a) add a new
`caveat_lint_config.json` entry for κ_critical=0.0897 and the
front-surface-correction machinery, with concrete `trigger_terms`
(e.g. `κ_critical`, `0\.0897`, `front.surface.conduction.correction`)
and the NETD/human-eye disclaimer as its required `phrase_pattern`; (b)
add a `numeric_lint_config.json` `derivation_consistency` entry keyed to
this proposal's own bench-vs-witness correction-factor application, and
a `numeric_drift` entry for κ_critical across its sibling sites once
Phase 3/5 write it more than once. Zero-cost, mechanical — no new
analysis.

## 4. Ruled-out / already-established re-proposal check

No re-proposal found. This continues live thread T23 (Iteration
22/23's own informal Biot-number/Maxwell-Garnett findings, never before
promoted to committed code) rather than resurrecting it — the proposal
correctly frames itself as promoting T23's own arithmetic, not
re-arguing T23's already-closed nominal question (which length scale is
licensed for `h_eff`). One point worth flagging for THERMODYNAMICS, not
mine to adjudicate: Iteration 23's own Phase-5 finding on a related
lumped-model breakdown (low fill fraction → high Biot) noted internal
gradients make "the radiating surface cooler, not warmer" in that
geometry — apparently in tension with this cycle's front-surface-hotter
picture. Idealization 1 disambiguates this correctly (this model's rear
boundary is the *only* loss channel, front is illuminated-only, a
different, deliberately worst-case convention from T23's whole-surface
radiating case) — I flag it only so THERMO's own critique confirms the
two are reconciled, not silently contradictory. No T18/NETD/sigma_flat/
thermo-length-scale-staleness registry entry is re-triggered incorrectly
by this proposal's own text.

## 5. Verdict

**Support-with-changes.**

The thermal-conductivity sourcing and closed-form correction are sound,
honestly worst-cased, and correctly declared out of constraint-3/4
scope at the top of the document. But Phase 3 must not proceed to a
Phase-4 search run until (1) the NETD/human-eye disclaimer sentence
appears verbatim at TD-3, TD-4, and TD-5's own claim points — not only
in §2's generic framing — and (2) concrete draft registry entries (§3
above) for κ_critical and the bench-vs-witness derivation are written
into the synthesis document, not deferred to "whatever needs it."

## 6. Single parameter change that would flip my verdict

Add, verbatim, at TD-3/TD-4/TD-5: *"This classification is an
instrument/microbolometer-NETD finding, not a constraint-3 human-eye
finding — see `thermo_sidecar.netd_disposition`'s own disclaimer."* Pair
it with one committed sentence naming the specific `caveat_lint_config.json`
and `numeric_lint_config.json` entries Phase 3 will add for κ_critical and
the correction-factor derivation. With both committed pre-freeze, this
becomes a clean **support**.
