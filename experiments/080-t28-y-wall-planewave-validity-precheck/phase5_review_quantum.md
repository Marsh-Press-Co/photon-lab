# PHASE 5 — REVIEW · QUANTUM OPTICS (fresh, blind to other Phase-5 seats) · Panel Iteration 57 · exp-080

*Fresh sub-agent, QUANTUM OPTICS charter (PANEL.md seat 5): non-classical
absorption, state-dependent or coherent interactions; expressibility
contract — mechanisms enter the bench only as effective classical
parameters, or Red Team strikes them. I have no memory of the Phase-2
QUANTUM instance that authored `photonics_image_term_curve()` — I am
reading it, and the whole finished cycle, cold, exactly as any other seat
would. Blind to every other seat's Phase-5 review this cycle.*

**No RULED-OUT item (R1–R9) is re-proposed or re-litigated here.**

---

## 0. Independent re-derivation of `part_d_photonics_construction()`

Wrote a from-scratch script
(`/tmp/.../scratchpad/quantum_verify.py`, session-local) that does **not**
import `validity_precheck.py`. It imports only the same already-gated
primitives that file imports (`dg065.CONFIGS`, `br.n_profile_exact`/
`nu_profile`/`damp_e_profile`/`CPL`, `ywas.build_aperture_grid`/
`aperture_amplitude`/`dist_image_cells`/`source_driven_phase`/
`reflection_coefficient_vec`/`echo_field_curve`/`K600`/`_trapz`/
`CONGRUENT_KEYS`), re-implements `E_photonics(θ_beam) =
r(90°−θ_beam;ABSORB)·W(θ_beam)` (`W` = the unweighted image sum) from the
docstring description, not by copying the committed function body, and
scores raw and scale-corrected R² against the same
`y_wall_aperture_sum_results.json`/live-`echo_field_curve` true curve.

**Result: exact reproduction, to the printed digit, of every number in
`validity_precheck_results.json::part_d_photonics_construction`.**

| cfg | absorb | raw R²(Re) | raw R²(abs) | scale-corrected R²(Re) | scale-corrected R²(abs) |
|---|---|---|---|---|---|
| C40 | 40 | −1.0933×10⁵ | −3.5414×10⁵ | 0.8836 | 0.4902 |
| C60 | 60 | −5.1792×10⁶ | −2.3542×10⁷ | 0.6985 | 0.2225 |
| C70 | 70 | −3.3338×10⁵ | −2.3599×10⁷ | **0.0852** | −4.4949 |
| C80 | 80 | −1.0648×10⁶ | −1.9034×10⁷ | 0.5072 | −7.7066 |
| G40 | 40 | −8.1525×10⁴ | −3.9069×10⁵ | 0.8356 | 0.6632 |

Mean scale-corrected R²(Re) = **0.6020**, min = **0.0852** (C70) — bit-for-bit
identical to the committed JSON, to Red Team's own independent audit
(`phase2_redteam_audit.md` §0 item 8), and to QUANTUM's own Phase-2 critique
table. This is now the **third** independent from-scratch reproduction of
this exact result (QUANTUM Phase-2, Red Team Phase-2, and this review), all
agreeing to 4 decimal places. I also spot-checked the underlying physical
claim driving the mismatch: `|r(θ_local∈[5.3°,15.0°])|` ≈ 1.1×10⁻⁴ vs.
`|r(90°−θ_beam) for θ_beam∈[36°,42°]|` ≈ 0.016–0.039 at ABSORB=40 — a
~150–350× amplitude-regime gap, consistent with the "100–400×" figure
already on the record.

**Verdict on task (1): the numbers hold. No error found, no discrepancy of
any kind.** This is a clean, correctly-computed result by every check I can
run against it from primitives.

---

## 1. Is the Director's "effectively already built" ruling defensible?

**Partially — the classification of *what exists* is accurate; the
implicit claim that it satisfies this program's pre-registration discipline
the same way parts (a)/(b) did is not, and nobody in the record names this
gap plainly.**

Parts (a) and (b) derive their evidentiary weight from a specific,
auditable fact VISION's own Phase-2 critique confirmed via `git log`: the
numeric bands (`FORECLOSE_RATIO=0.10`, `SUPPORT_R2=0.90`, etc.) were
committed to git in `phase1_proposal.md` **before** `validity_precheck.py`
existed to compute anything against them. That is what "predictions
committed to git BEFORE the run" (PANEL.md Phase 3) actually buys: an
outsider can verify, from commit timestamps alone, that the scoring rule
could not have been shaped by already-known results.

`photonics_image_term_curve()`/`part_d_photonics_construction()` has no
analogous audit trail. The sequence that actually happened: QUANTUM's own
Phase-2 critique computed `E_photonics(θ_beam)` and its R² scores **first**
(as part of a blind critique, with no requirement to pre-register anything
— Phase 2 critiques are not bound by Phase 1's freeze discipline, and
nothing here suggests they should be), and only **then**, in the same
document, recommended that a SUPPORT/INCONCLUSIVE/REFUTE band be
"pre-register[ed]... before or immediately upon building" the construction.
By the time that sentence was written, the numbers computing exactly where
they'd fall against the very bands being proposed (borrowed verbatim from
part (b)'s own thresholds) were already known to their author. Red Team's
audit then adopts the construction as "effectively already built and
scored" and Phase 3 folds it into committed code — at no point does anyone
actually execute QUANTUM's own recommended freeze-then-score sequence for
this construction. The bands never get invoked as a formal verdict in the
committed code either (`part_d_photonics_construction()` returns raw
numbers and a prose `note`, not a `verdict` field the way `part_a()`/
`part_b()` do) — which is the right instinct, but it also means the
"does not clear a bar" language throughout Red Team's audit and
`phase3_synthesis.md` is a post-hoc narrative comparison to a threshold that
was never actually frozen for this object, dressed in the same rhetorical
weight as a properly pre-registered verdict.

To be fair to the ruling: the numbers themselves are not HARKed in the
sense that matters most — QUANTUM chose its analysis *method* (build
`r(90°−θ_beam)·W(θ_beam)`, score by the same R² convention part (b) already
used) before knowing its own answer, and the method was not re-selected
after seeing an unfavorable result. Folding an already-twice-independently-
verified computation into reusable code is a reasonable thing to do without
re-freezing, and the exp-079 Iteration 56 precedent cited for it is real.
But that precedent (QUANTUM's reflectance-ablation control) was a
**structural-degeneracy diagnostic**, not a comparative score against
inherited SUPPORT/REFUTE-style bands — the two situations are less alike
than Phase 3 treats them. **My own house-discipline reading: "effectively
already built" is a fair description of the code's existence and of the
numbers' correctness; it is not a fair description of the numbers having
been produced under the same pre-registration discipline that gives part
(a)/(b)'s verdicts their weight, and the record should say so plainly
rather than lean on the precedent as if the gap were fully closed.**

**Consequence for Iteration 58, not a re-opening of this cycle**: the
"actually decisive test" both Red Team and Phase 3 correctly identify as
still pending — scoring `PAIR_PAD`/`PAIR_ABSORB40`/`C80−C40` deltas of
`photonics_image_term_curve()` (extended with `E_direct`, see §2) against
the real T28 reference periods via `_free_period_search` — is exactly the
place to actually run the freeze-then-score sequence QUANTUM's own Phase-2
critique called for and that this cycle never executed: pre-register the
SUPPORT/INCONCLUSIVE/REFUTE bands for *that* test, in git, before running
it. Doing so would retroactively supply the missing discipline for the
construction as a whole, even though the desk-level R² numbers reviewed
here would stand unchanged.

---

## 2. Does the `E_direct` omission make `photonics_image_term_curve()` a
## well-posed effective-classical-parameter model, and do the raw R² values
## tell you what they claim to?

**Two separate problems live under this one flagged omission, and the
record conflates them.**

**(a) Internal consistency of the R² test as actually run: not compromised
by `E_direct` on its own.** I traced what `ywas.echo_field_curve()` — the
"true" comparison curve — actually is: per its own docstring and exp-079's
§[5]/§[5a], `E_echo` is *itself* an echo-only quantity (the reflected-field
phasor alone, `r(θ_local(y_s))` weighted), never including any `E_direct`
term. So the R² comparison in part (d) is echo-only-model vs.
echo-only-model — `E_direct` is absent from *both* sides, not asymmetrically
dropped from one. On that narrow point, the docstring's own framing
("valid only insofar as it cancels identically across congruent-config pair
deltas") undersells why the comparison is fair: it isn't relying on a
cancellation argument at all for *this* R² test, because `E_direct` was
never part of the comparison target to begin with. This is worth
correcting in the docstring, not just flagging as unresolved.

**(b) Fitness for what the record uses the result *for*: this is where the
real problem is, and it is not the one flagged.** I went back to exp-079's
own `phase5_review_photonics.md` (§4, PHOTONICS' original sketch this
whole construction descends from) to check what PHOTONICS actually proposed
scoring, and how. Verbatim: *"Total field: `E(θ_beam) = E_direct(θ_beam) +
r(90°−θ_beam;ABSORB)·E_image_unweighted(θ_beam)`, scored by the identical
`_free_period_search`/`score_period` machinery every T28 cycle since
Iteration 46 has used."* PHOTONICS' own construction was never meant to be
scored by R² against exp-079's per-point `echo_field_curve` at all — it was
meant to be scored, as a **total field including `E_direct`**, against the
**real T28 reference periods**, the same pipeline every prior y-wall model
in this sub-thread has been held to. `photonics_image_term_curve()` differs
from that sketch in two compounding ways, not one: it drops `E_direct`,
*and* it substitutes a shape-comparison against a different theoretical
candidate curve for the free-period fit against real data that was always
the actual target metric. The docstring names only the first.

This matters for well-posedness in exactly my charter's terms. `E_direct`
is not a decoration here — exp-079's own Phase-5 PHOTONICS review (its
feasibility probe, same section) already predicted, from the phase-swing
of `arg(r(90°−θ_beam))` alone, that this construction's most likely
behavior is an "amplitude/phase-modulating envelope on top of the SAME
T21-family carrier already present in `E_direct`... an AM sideband
structure." If that prediction is right, `E_direct` is expected to be the
**dominant carrier** of whatever period content the real field has, and
`photonics_image_term_curve()` — by construction — contains none of it. A
model that has been built with its own predicted dominant term omitted, and
then scored for shape-fidelity against an admittedly-non-authoritative
stand-in curve rather than against the real data its own author specified,
is not yet the "effective classical parameter" object my charter asks for.
It is a **partial, unscored draft** of that object with a number attached
that looks like a verdict.

**Concretely, what the raw catastrophic R² (and even the scale-corrected
mean 0.602/min 0.085) do and don't tell you:**

- They **do** tell you, correctly and now three-times-independently
  verified, that `r(90°−θ_beam)`'s amplitude regime (0.016–0.039) is
  100–400× larger than the amplitude regime the true near-field geometry
  actually presents (`|r(θ_local)|`≈10⁻⁴) — a real, load-bearing,
  numerically solid consequence of part (a)'s FORECLOSE finding, and a
  genuinely new, previously-undisclosed quantitative fact about this
  construction (this stands regardless of everything below).
- They do **not** tell you how the *total* field `E_direct + r·E_image`
  would compare to anything, because `E_direct` was never built or added.
- They do **not** tell you how this construction performs on the metric
  its own proposer specified (`_free_period_search` against real T28
  periods) — Red Team's own Checkpoint-2 reasoning already makes a version
  of this point (comparing against exp-079's per-point curve is comparing
  against "only a CANDIDATE model" already shown incapable of
  discriminating real echo from none) — my own review reaches the same
  place from the opposite direction: not just that the *comparison target*
  is suspect, but that the *comparison methodology itself* (R² shape-fit)
  was never what PHOTONICS proposed running at all. Both gaps point at the
  same missing step: Iteration 58's already-planned free-period-fit test
  against real data, done with `E_direct` actually included.

**Recommendation, concrete and cheap (zero new FDTD, matching this
sub-thread's own scope discipline):** before Iteration 58 treats
`photonics_image_term_curve()` as ready for the free-period pipeline, add
`E_direct(θ_beam)` explicitly — it is not new physics, it is exp-079's own
already-gated direct-field formula (`_src_amp`/`aperture_profile`/`G0`,
named directly in PHOTONICS' own derivation route step 2) evaluated with no
wall term at all. Retitle the function's docstring to state plainly that it
implements only the *image-echo component* of PHOTONICS' sketch, not the
sketch itself, and that its R² scores answer "does the image term alone
resemble a different candidate model's shape," not "does PHOTONICS'
construction reproduce the real T28 signal."

---

## 3. New findings from this review, not already on the record

1. QUANTUM's own Phase-2 "required change" (pre-register bands before
   building) was already moot at the moment it was written, since the
   scored numbers existed at critique-writing time — a self-inconsistency
   in the record's own procedural language that neither Red Team's audit
   nor Phase 3's synthesis names, even though both explicitly discuss why
   no fresh freeze was needed (§1 above).
2. `echo_field_curve()`'s own `E_echo` is *already* echo-only (no
   `E_direct` on either side of the part (d) comparison) — the docstring's
   stated justification for the omission ("valid only insofar as it
   cancels... across pair deltas") is the wrong justification for why the
   *current* R² test is internally consistent; it is the right concern only
   for the *different*, not-yet-run free-period-fit-against-real-data test
   (§2 above).
3. PHOTONICS' own original Sec 4 sketch (exp-079 `phase5_review_photonics.md`
   §4) specifies scoring the total field against **real T28 periods** via
   `_free_period_search`, never an R²-against-a-candidate-curve comparison —
   the methodology substitution is a second, compounding gap alongside the
   already-flagged `E_direct` omission, not previously named as a separate
   issue in this cycle's record.

---

## 4. Verdict on the whole cycle: **PARTIAL**

I concur with the Combined Verdict already on record
(`phase3_synthesis.md` §3, `phase4_results.md`): (a) FORECLOSE stands,
solidly, on geometry alone; (b) is admittance-family-dependent
(INCONCLUSIVE matched / REFUTE realizable); (d)'s construction shows a
real, independently-triple-verified amplitude-regime pathology. None of
this closes the plane-wave/global-steering mechanism class — Checkpoint
criterion 2 correctly remains NOT YET RIPE. My own addition is procedural,
not a correction to any number: the "effectively already built" framing
should be qualified rather than treated as equivalent to this program's own
pre-registration standard, and the construction now sitting in committed
code is an image-term-only, non-authoritatively-scored draft of PHOTONICS'
actual sketch — real, correct as far as it goes, and not yet the object
Iteration 58's free-period test should assume it already has in hand
without first adding `E_direct` and pre-registering that test's own bands
in git, before running it, the way parts (a) and (b) of this very cycle
did.

Full independent-verification script: `/tmp/claude-0/-home-user-photon-lab/
2b060a3c-5a0e-59f0-94f6-5a474c2b79a3/scratchpad/quantum_verify.py`
(session-local; every number it produces is reproduced in §0 above and is
re-derivable from already-committed repo files alone).
