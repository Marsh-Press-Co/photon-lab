# exp-064 — Phase 5 Review: PHOTONICS (blind, fresh context)

*Panel Iteration 41. Fresh sub-agent, no prior context on this cycle beyond
the record read per the Phase-5 packet (PANEL.md, LOGBOOK.md in full,
PLAN.md's current-state + Iteration-41 queue, `lab/thermo_sidecar.py` and
`lab/validation/run_all.py` stages 18/23/24 as they now stand, and the
complete exp-064 process record — Phase 1 through Phase 4). Have NOT read
and did not seek out any other seat's Phase-5 review of this cycle.*

**Scope discipline stated up front, as the task asks**: this cycle is
code-architecture, not optics. PHOTONICS' charter — surface interaction,
absorption spectra, angular dependence, scattering cross-sections — bears
on exactly two things here: (1) whether the guard's physical
justification (the optical theorem / extinction-vs-geometric-cross-section
argument) is textbook-sound, and (2) the one place a real absorption/
scattering-transport question was raised and then struck. Everything else
in this cycle (keyword-only Python arguments, `inspect.signature`,
text-scanning a source file) is software architecture; I say so rather
than dress up a code-review as an optics finding.

---

## 1. Independent verification performed, not merely trusted

Before assessing anything, I re-derived rather than trusted the following,
against the actual repo state (commit `482392a`, confirmed current):

- **Read `lab/thermo_sidecar.py` in full** (594 lines) and
  `lab/validation/run_all.py` stages 18, 23, 24 in full — not summaries.
- **Ran the full trust suite myself**: `python3 lab/validation/run_all.py
  --only 12346789,10,11,18,19,20,21,22,23,24` → **107/107 in 258s**,
  matching `phase4_results.md`'s own citation exactly.
- **Reproduced the deliberate-break test (RT-1) myself**, independently of
  the transcript in `phase4_results.md`: hand-edited a copy of
  `run_all.py`, relabeling the `L_MP5_730X_M` call in
  `front_surface_conduction_correction` from
  `length_provenance="extinction_derived_diagnostic_only",
  diagnostic_only=True` to `"bench_construction", diagnostic_only=False`,
  then ran `--only 24`. Result: **27/28, one FAIL, the exact injected
  defect** (`source-scan: live front_surface_conduction_correction
  (L_MP5_730X_M, ...) call site carries the diagnostic tag: MISTAGGED OR
  MISSING`). Reverted (`cp` from a pre-edit backup, confirmed `git status
  --short` clean) and re-ran: **28/28 clean.** This is not a claim I am
  relaying — I watched the gate catch the injected defect myself.
- **Confirmed the `w_on_m` claim bit-for-bit**: grepped
  `experiments/046-aperture-beam-t23-mixed-regime-dose-extension/
  results.json` directly. `"w_on_m": 7.079002048463575e-06` appears
  verbatim, matching stage 18's retagged test value exactly, to every
  printed digit.
- **Confirmed all 5 pre-existing bench-scale call sites** (exp-054,
  exp-057, exp-059 ×2, exp-060) carry `length_provenance="bench_
  construction"` by direct grep of each `run.py`.
- **Independently re-derived the struck §6 arithmetic** by reading
  `experiments/061-.../phase4_results.md`'s own MP-2 and MP-5 sections
  directly (not MATERIALS' or Red Team's summary of them): MP-2's
  CONFIRMED, sourced real-forest thicknesses are 100–500µm (three
  corroborated citations); MP-5's own table gives witness-need figures of
  332µm and 1056µm among its six rows. `1056/100 ≈ 10.6×` — matching the
  "~1×–10.5×" corrected gap Red Team cites, not Phase 1's uncited
  "24×–75×" figure, which traces to nothing in the record I can find
  either.

Every headline numeric and behavioral claim in this cycle's record that I
attempted to independently reproduce, reproduced exactly. I found no
discrepancy between the written record and the actual repo state.

---

## 2. (a) Is the guard's physical design sound on a fresh read?

**Yes — the allow-list design and its optical-theorem justification are
correct textbook physics, and this program's own independently-derived
record already corroborates the claim rather than merely asserting it.**

`_validate_length_provenance`'s docstring argument is: an extinction
cross-section σ_ext is tied, via the optical theorem, to Im[f(0)] — the
imaginary part of the *forward*-scattering amplitude — a coherent,
diffractive quantity, not a ray-geometric one, so σ_ext can differ from
(and for resonant or sub-wavelength scatterers, substantially exceed) any
real geometric length of the object producing it. That is correct as
stated (the extinction theorem, Bohren & Huffman-standard), and it is the
right reason an allow-list beats a deny-list here: the failure mode this
guard defends against is general to wave optics (any future
extinction/absorption-derived quantity is suspect, not just today's two
named examples), so blacklisting `w_on` and `L=τ_true/α` by name would
leave the guard blind to the next one — precisely how T23 itself survived
three prose-only deferrals.

What makes this more than a plausible-sounding argument is that **this
program has already independently measured the exact phenomenon the
justification invokes**, on this bench, in a different cycle, with no
foreknowledge that it would later become the reasoning for a guard:
`lab/qext_theory.py` (stage 21, exp-059) computed the closed-form PEC
extinction efficiency `Q_ext_PEC(24.5044) = 2.1177` — comfortably above
the sharp-edged-scatterer diffraction floor of 2 (the "extinction
paradox," itself a direct consequence of the optical theorem: a large
opaque obstacle removes exactly twice its own geometric cross-section
worth of power from the beam, half by direct interception and half by
diffractive shadow-formation). The bench's own measured graded-shell
`Q_ext = 1.5385` and the T9 thread's own documented `w_on/(2·r_out)≈1.54`
inflation are the SAME phenomenon this cycle's docstring cites in the
abstract. The guard's physical reasoning is not borrowed authority; it is
consistent with, and in a meaningful sense already empirically
demonstrated by, this program's own independently-run physics. I find no
daylight between the stated justification and the underlying optics.

Two smaller observations, neither blocking:

- The docstring's phrasing ("Im[f(0)]") is written generically, but this
  bench is a 2D FDTD engine (`qext_theory.py`'s own TM_z cylinder series
  confirms this explicitly). The 2D optical theorem has a different
  numerical prefactor/convention than the 3D form the docstring's phrasing
  most directly evokes. This is a precision nitpick, not a correctness
  problem — the *qualitative* claim (σ_ext is a coherent/diffractive
  quantity, not a ray-geometric one) holds in both 2D and 3D identically,
  and nothing in the guard's actual enforcement logic depends on which
  convention is meant. Worth a one-clause tightening if this docstring is
  next touched; not worth a mandatory fix on its own.
- EM's Phase-2 attack 5 (provenance-**TIER** vs. provenance-**ROLE** — the
  allow-list checks *how* a length was obtained, not *which physical
  entity* it characterizes; an honestly-measured gap/standoff distance
  would pass the identical `bench_construction` tag while feeding a
  physically different conduction regime into the same `h=k/L` formula) is
  a genuine structural gap from my own reading, correctly ruled
  non-blocking since no current or proposed call site is anything but
  `r_out`-class or the MP-5 extinction-derived length. I agree with that
  disposition on a fresh read — it is real, it is not live, and closing it
  now would have been solving a problem that does not yet exist at the
  cost of scope discipline this program has repeatedly rewarded.

**Verdict on (a): sound.** Both the allow-list shape and its stated
physical grounding hold up under independent scrutiny, and are stronger
for being independently reproducible from this program's own prior,
unrelated measurements rather than resting on the docstring's own
say-so.

---

## 3. (b) Does striking Phase-1 §6 leave anything actually unresolved?

**No — the excision was correct, clean, and the underlying substantive
question was never actually opened by this cycle in the first place; it
was already sitting, correctly scoped, in exp-061's own MP-2/MP-5 record,
untouched by the strike.**

I independently re-derived both catches that killed §6:

1. **MATERIALS'/Red Team's numeric catch is correct.** §6's headline
   "24×–75×, no query surfaced a directly-measured height at this scale"
   compared the witness-need figures against an uncited "up to 14
   micrometers" claim. But this program's own already-CONFIRMED record
   (exp-061 MP-2) sources real CNT-forest/Vantablack thicknesses at
   100–500µm — an order of magnitude larger than the uncited 14µm figure,
   and MP-5's own table already computed the exact 332µm/1056µm
   witness-need numbers §6 re-derived. The honest, already-scored gap is
   ~1×–10.5×, not 24×–75×. I verified this by reading MP-2/MP-5 directly,
   not by trusting the citation chain — it checks out exactly.
2. **PHOTONICS' own (this cycle's blind PHOTONICS seat, not me — a
   different fresh instance) idealization catch also holds under my own
   re-derivation**: even the corrected ~1×–10.5× figure silently equates
   forest *height* with the single-pass Beer-Lambert absorption path
   length needed to reach τ_true. That equivalence assumes ballistic,
   normal-incidence propagation through a homogeneous effective medium. A
   real CNT forest is explicitly dilute (~1–10% fill per this program's
   own record) and is black *because* it multiply scatters — diffusive
   transport, not a straight ray. Height and absorption path length need
   not be equal, and the direction of that inequality is not obvious
   without a real transport model. Separately, constraint 4's own swept,
   generally-oblique beam means even the pure-ballistic limit needs
   `h/cosθ`, not `h`.

Striking §6 wholesale (Red Team's option (b), rather than restating a
"corrected" 1×–10.5× number) was the right call, and I would have made the
same recommendation on a fresh read: a corrected number still carrying the
undisclosed forest-height-vs-path-length equivalence would only have
compounded one flagged problem with another, and the actually-scored,
already-established figure (exp-061 MP-2/MP-5, PARTIAL — qualitatively
confirmed, quantitatively undershooting by ~230×–730× at visible
wavelengths) already lives, correctly qualified, in `LOGBOOK.md`/
`REALIZABILITY_MEMO.md`. Nothing about T23's own closure, or about this
program's realizability record, depends on §6 in any way — it was a
bounded, disclosed, Phase-1-optional diligence pass (explicitly named as
such in the proposal's own §6 header) that turned out to compute a
duplicate, wrong number and was correctly removed rather than patched.

**What I would flag, not as an unresolved-T23 matter but as a genuinely
open PHOTONICS-domain question this near-miss surfaces**: nobody in this
program's history has actually modeled the diffusive-transport correction
that would relate a real CNT forest's physical thickness to its effective
Beer-Lambert absorption length. Every `τ_true/α`-style back-calculation in
this program's realizability chain (MP-5, TD-5, the struck §6 itself)
implicitly assumes ballistic, normal-incidence, homogeneous-medium
propagation. This is not a defect in exp-064 — it is an idealization this
cycle correctly declined to paper over by restating a wrong number — but
it is real unfinished business one layer upstream of anything this
guard's `length_provenance` categories can express. See §5, candidate 2,
below.

**Verdict on (b): cleanly and correctly excised. Nothing load-bearing was
left dangling.**

---

## 4. (c) The `w_on_m`-as-test-value finding — does it deserve more than a
passing note?

**Yes. I read this as the single most interesting empirical finding in
this cycle, and it is under-exploited as filed — "harmless, disclosed as
Learned #3" undersells what it demonstrates.**

The fact pattern, independently confirmed (see §1): one of stage 18's four
"arbitrary" formula-identity test lengths, committed at Iteration 31
(exp-054) and unexamined for ten iterations, is bit-for-bit identical to
`w_on_m` — the canonical, by-name forbidden extinction-derived length T23
exists to keep out of a conduction role. It was genuinely harmless
*there*: `h·L == k_air` is a pure algebraic identity that holds for any
positive `L` regardless of what it represents, so no physical claim was
ever drawn from that specific value being what it was.

But the reason it matters more than a passing "Learned" bullet is what it
demonstrates about *detectability*, not about that one test's harm. This
value sat in committed, trust-suite-gated code for ten iterations,
survived every review this program's own extensive Phase-2/Phase-5
process ran on `stage18_length_scale_chain` across that span, and was
found only because a NEW requirement (declare provenance for every length)
forced someone to look at what each existing value actually *was*. That is
exactly the same discovery mechanism — a new tool surfacing an old,
undetected instance of the very failure it was built to catch — this
program has now logged three separate times in three different
sub-systems: `caveat_lint.py`'s own registry-scoping gaps (Iterations
38–40, firing Checkpoint criterion 4 twice), `numeric_lint.py` catching
exp-062's own EM-6/EM-7 R-vs-T methodology drop, and now `w_on_m` sitting
inside `thermo_sidecar.py`'s own test fixtures. Three for three is not
strong enough to call a proven law, but it is a real, recurring
pattern-of-patterns worth naming explicitly: **this codebase's own history
says that wherever a numeric or provenance discipline is enforced only by
convention rather than by a gate, an already-violating instance is more
likely than not to be sitting somewhere undetected, and the only way this
program has ever found one is by building the next gate.**

The guard closes the four call sites its own scope named (`gas_
conduction_h_eff`, `lumped_cube_mass_kg`, `mixed_length_scale_regime`,
`front_surface_conduction_correction`). It does **not** — and was never
scoped to — check whether an extinction-derived quantity (`w_on`,
`sigma_ext_cells`, `Q_ext`, `tau`, any `alpha`-derived length) is fed,
unflagged, into some OTHER length-consuming role anywhere else in `lab/`
or in an `experiments/*/run.py` (window/domain sizing in `design_
geometry.py`, `PLANE_DX`/`GUARD_OUT` construction, `sections.py`'s
radial-binning geometry, anything in `amplitude_bridge.py`). I did not
find an existing violation in the time available for this review — that
is a genuine limit of what a Phase-5 read can check, not a finding that
none exists. Given the base rate this program's own three prior instances
suggest, and given that `w_on_m` was found purely as an accident of
wiring an unrelated guard through, I think a dedicated, purpose-built
sweep is warranted rather than assumed unnecessary. See §5, candidate 1.

**Verdict on (c): yes, deserves more than a passing note — it is
evidence, not just an anecdote, that this class of silent misuse is a
recurring structural risk in this codebase, and the guard as shipped
protects exactly the four functions it was scoped to protect, nothing
wider.**

---

## 5. My own ranked top-3 candidate directions for Iteration 42

Stated from my own discipline where it genuinely bears, and named
honestly as adjacent-to-charter where it is materials/software work I am
endorsing rather than leading:

**1. A dedicated, codebase-wide extinction-derived-length provenance
sweep — a new `numeric_lint.py` check-kind, not a manual grep.** Directly
motivated by §4 above. Build a check (reusing `numeric_lint.py`'s existing
`derivation_consistency` idiom, which already expresses "wherever
condition X holds, disclosure/treatment Y must also appear") that flags
any call site anywhere in `lab/`/`experiments/*/run.py` passing a variable
traceable to an extinction/absorption/scattering quantity (`sigma_ext`,
`w_on`, `Q_ext`, `tau`, `alpha`-derived lengths) into a function whose own
docstring declares a geometric-length requirement, without going through
`length_provenance` or an equivalent declared guard. This is the natural,
already-precedented way this program has closed exactly this shape of gap
three times before (see §4) — cheap, zero-FDTD, and it directly answers
the open question this Phase-5 review was asked to weigh in on rather
than leaving it as a one-line "Learned" bullet.

**2. A diffusive-transport (non-ballistic) correction to the `L=τ_true/α`
Beer-Lambert back-calculation used throughout the realizability chain.**
Directly motivated by §3 above — the idealization struck-along-with-§6,
not resolved by the strike. A real CNT forest is a dilute (~1–10% fill),
multiply-scattering mat; treating its physical thickness as a ballistic
single-pass absorption length is an unexamined assumption running through
MP-5 and every TD-bracket witness-scale figure this program has computed.
A sourced two-flux (Kubelka–Munk-class) or radiative-transfer treatment,
with a sourced scattering albedo for CNT-forest-class media, could tighten
or loosen the existing ~230×–730× MP-5 undershoot substantially in either
direction — a genuinely open, falsifiable, PHOTONICS-native question this
program has never actually modeled, only assumed away.

**3. Extend the guard from provenance-*TIER* to provenance-*ROLE*
(EM's Phase-2 attack 5), bundled with PLAN.md's own standing queue item 3
(pin CNT-forest pitch/diameter and thermal conductivity together).**
Currently correctly non-blocking (no live violation), but the moment a
real `measured_geometric` witness-scale length is eventually sourced (the
natural outcome of PLAN.md's own item 3), the guard's allow-list will
start doing real work distinguishing "a real length" from "a real length
of the *right physical entity*" — better to design that distinction in
before a live call site needs it than to discover the gap the way `w_on_m`
was discovered.

---

## 6. Verdict

**PROMISING.**

Reason: every falsifiable prediction this cycle committed (QP-1 through
QP-5, RT-1, RT-2) is independently reproducible against the actual repo
state — I reproduced the two most load-bearing ones myself (the
deliberate-break test and the full 107/107 bench) rather than trusting the
transcript. The core design (allow-list over deny-list, keyword-only
no-default argument, the source-inspection gate closing the exact
"disclosure nothing checks" failure shape T23 itself instantiated) is
physically and architecturally sound on a fresh, skeptical read, and its
central optical-theorem justification is not just plausible but already
corroborated by this program's own independently-derived stage-21
`Q_ext` physics. The one genuinely serious defect in this cycle's own
history — Phase 1's original stage-24 gate suite would not have enforced
anything against the real committed call sites — was caught at Phase 2,
before any code shipped, which is this program's designed mechanism
working as intended, not drift; Red Team correctly declined to fire any
Checkpoint criterion on that basis. The one factual error in the record
(§6's uncited, contradicted "14µm" figure) was caught by two independent
blind seats and cleanly excised rather than papered over. Nothing I
checked contradicted anything the record claims. This is a clean,
structurally sound, honestly self-correcting cycle.

**No Checkpoint criterion fires on my own reading.** Criterion 4 in
particular: I looked hard for a caveat that shipped stale or a claim that
outran its evidence, given this cycle's own subject matter is exactly
that failure class. I found none — the `geometric_realizability` field
correctly distinguishes provenance-honesty from buildability (mandatory
fix 4), the `netd_disclaimer` strings survive byte-identical (mandatory
fix 3, RT-2, independently confirmed), and the one place a claim did
outrun its evidence (§6) was caught and removed before this record was
ever written down as closed, not after.
