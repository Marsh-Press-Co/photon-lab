# PHASE 5 — RED TEAM FINAL AUDIT · Panel Iteration 61 · exp-084
## Adjudicating all six blind Phase-5 reviews of the source-aperture/article-rim Fresnel edge-diffraction derivation — independently re-deriving EM's scale-invariance proof from `amb.weber`/`propagate`'s own code, re-running QUANTUM's circular-shift null on the shape-correlation finding, ruling on THERMODYNAMICS' Anchor-3 commensurability gap, ruling on VISION's Checkpoint-ritualization concern, finalizing R10's LOGBOOK text, and reconciling Iteration 62's queue

*Seat: RED TEAM. Fresh sub-agent, zero memory of any prior session, including
my own Phase-2 audit this cycle. Read, in commit order: `phase1_proposal.md`
(including its Phase-3 correction), `phase1_derivation.py`,
`phase1_output.txt`, `derivation_results.json`, all five Phase-2 critiques,
`phase2_redteam_audit.md`, `phase3_synthesis.md`,
`phase3_fix_docket_checks.py`/`_results.json`, `NOTES.md`, all six Phase-5
reviews, `PANEL.md` in full, and the relevant `LOGBOOK.md` sections (RULED
OUT R1–R9, ESTABLISHED, LIVE THREADS/T28 Iterations 58–60 in full). Every
load-bearing number below was independently recomputed from committed code
in this session — shown inline with the actual commands, not restated from
any of the six reviews' prose.*

---

## 0. Independent verification performed before adjudicating anything

- **`phase3_fix_docket_checks.py` re-run fresh**: reproduces
  `phase3_fix_docket_results.json` bit-exact (`git diff` on the file after
  re-running it: empty). Both numbers Phase 3 cites — `corr(leg_a,
  C80_real)=0.9581856926779434` and the circular-shift null
  `15/30=50.0%` — are independently confirmed live, not merely re-read.
- **The stale-JSON finding (PHOTONICS' §2.1)**: confirmed real and already
  fixed. `git show 52dcbb2:.../phase3_fix_docket_results.json` (Phase 3's
  own commit) contains the wrong key/value
  (`"leg_b_nomask_own_output_vs_real_C80 (control)": 0.9022947333208244`);
  `git show 87e182e:.../phase3_fix_docket_results.json` (the commit
  containing PHOTONICS' and EM's Phase-5 reviews) already contains the
  corrected key/value (`"leg_b_own_masked_output_vs_real_C80 (control)":
  -0.10459710451467671`), and `git status`/`git diff` on the current
  working tree confirm this corrected file is what is live now, matching
  the script's own fresh output exactly. **The fix is real, complete, and
  already landed — nothing further is owed here.** (PHOTONICS' own account
  — that it reverted its diagnostic fix so as to "leave no footprint" — is
  consistent with this: the correction present in `87e182e` was made by the
  Director alongside committing that Phase-5 batch, not by PHOTONICS
  itself.) No verdict in the record ever rested on the stale number — every
  prose citation (`phase1_output.txt` predates the JSON's existence,
  `phase2_redteam_audit.md`, `phase3_synthesis.md`) already used the
  correct `-0.10` figure.
- **PHOTONICS' aperture-width sensitivity sweep**: independently
  reconstructed from primitives (perturbing `g["ABSORB"]` in
  `dg065.propagator_geom`'s output, which is what actually sets the
  aperture half-width `A = OBJ_Y − ABSORB` inside `dg048._geom_derived`,
  holding `OBJ_Y`/`D_SP`/`TAPER`/`λ` fixed — not a stray `A` dict key,
  which `edge_diffraction_c_empty_corrected` never reads, confirmed by an
  initial failed attempt that changed nothing until I traced the real
  mechanism). Reproduces every cited value exactly: `r=0.9582` at 0%,
  `r=0.4527` at −1%, `r=−0.5545` at −5%, `r=−0.2816` at −20%. **Confirmed
  independently — a real, structure-sensitive corroboration of the
  shape-correlation finding, not a generic-smoothness artifact.**

---

## 1. Adjudication of the six Phase-5 reviews

All six reach **PARTIAL** independently, each from its own charter, each
having re-derived the decisive numbers rather than deferring. None
disagrees with Phase 3's substantive verdict; each adds something new:
PHOTONICS (stale JSON, a sharper sensitivity control, a third Anchor-2
hypothesis), MATERIALS (traces "zero realizability content" through the
correction and shows THERMODYNAMICS' 41× is orthogonal to any material
law), EM (proves the phase-factor hypothesis dead, names the chirp issue,
sharpens Checkpoint-4's own record), THERMODYNAMICS (independently
retraces the Checkpoint-4 chain, finds Anchor 3 not yet commensurable),
QUANTUM (a fourth-and-fifth independent reproduction of the period-match
null via two structurally different instruments, then applies the same
scrutiny to the shape-correlation finding for the first time — a genuinely
new test nobody had run), VISION (clean governance audit, a sharper
Checkpoint-4 argument than the Director's own, and the ritualization
concern). All six findings are adopted below except where a specific
ruling narrows or reframes one (Anchor 3, R10, Checkpoint 4's ritualization
framing) — none is overridden outright.

---

## 2. Task item 1 — EM's scale-invariance proof, independently re-derived from `amb.weber`/`propagate`'s own source, then confirmed by direct execution

**Verdict: CONFIRMED, exactly, by both algebra and code.**

`lab/ambient.py`:
```python
def window_means(b, y_lo, y0, w_obj, guard_out, w_flank):
    ...
    obj = float(b[rel <= w_obj].mean())
    fl = ...
    return obj, float(b[fl].mean())

def weber(b_obj, b_flank):
    return (b_obj - b_flank) / b_flank
```
`window_means` is a linear reduction (an arithmetic mean over a fixed index
set of a real array `b`); `weber` is a pure ratio of its two outputs.
`phase1_derivation.py::propagate`:
```python
def propagate(y_src, amp_src, y_obs, dx, lam_cells):
    ...
    G0 = np.exp(1j * (k * r - math.pi / 4.0)) / np.sqrt(r)
    E = G0 @ amp_src
    H = (G0 * obliquity) @ amp_src
    return E, H
```
is linear in `amp_src`. For any complex constant `c`: `amp_src → c·amp_src`
⟹ `E → c·E`, `H → c·H` (matrix-vector product is linear) ⟹
`Sx2 = −Re(E·conj(H)) → |c|²·Sx2` pointwise (a global real rescaling of the
*entire* array, since `c·conj(c) = |c|²` is a real scalar factored out of
every term) ⟹ `window_means` (linear) scales both outputs by the identical
`|c|²` ⟹ `weber = (bo−bf)/bf` cancels `|c|²` exactly, for **any** complex
`c ≠ 0` (real, imaginary, or of arbitrary phase and magnitude) — this is
not specific to a 90°-rotating `−i`/`+i` factor; it holds for every global
multiplicative rescaling.

I then verified this is not merely an algebra exercise by running it
against the literal committed pipeline (not a re-implementation):

```
baseline (c=1)[:5]     = [-0.02572369 -0.02306936 -0.01307157  0.00194656  0.01720905]
max|baseline - c=-i|   = 2.38e-16
max|baseline - c=+i|   = 2.38e-16
max|baseline - c=-1|   = 0.0
max|baseline - c=5e^i0.73| = 5.00e-16
```
Four independent global constants (two pure-imaginary, one negative-real,
one of arbitrary complex phase and non-unit magnitude) applied to leg (b)'s
own no-mask curve leave `c_b_nomask(θ)` unchanged to floating-point
precision — confirming EM's claim in its strongest, most general form (any
global complex constant, not only `±i`), independently, by execution, not
re-derivation of EM's own prose. **EM's ruling is correct: a bare global
phase/normalization constant is provably, not merely arguably, powerless
to close Anchor 2 under this bench's own Weber-contrast reduction.** The
real fix must be position-and-observation-point-dependent (a genuine
matrix-valued RS/Kirchhoff kernel applied inside `propagate`'s own
construction of `E2`, exactly as EM's own Test B and its own §3 ranking
conclude) — Phase 3's decision not to adopt either bare guess as settled is
correct, and this audit adds a proof, not merely a second opinion, that one
of the two named guesses (a bare phase factor) cannot be revived by
re-tuning its value.

---

## 3. Task item 2 — QUANTUM's circular-shift test on the shape-correlation finding, independently re-run from the committed `leg_a_curve()` output

**Verdict: CONFIRMED, bit-exact.**

```
r_obs = corr(leg_a_curve(), C80_real) = 0.9581856926779434
30 circular shifts of leg_a_curve() vs the FIXED real C80(theta):
  mean = -0.0319   max = 0.9629 (at shift=+1, i.e. +0.2°)   min = -0.6806
  n_shifts with |r| >= |r_obs| = 1/30 = 3.3%
  shift=+1 (+0.2°)  r=0.9629   <- the one shift that beats r_obs
  shift=+2 (+0.4°)  r=0.8046
  shift=+30(+6.0°)  r=0.7428
```

This matches QUANTUM's own figures exactly, including the specific
near-tied lag: the single shift that exceeds the zero-lag correlation is
the immediately adjacent one (+0.2°, `r=0.9629`, ~0.5% above the observed
value), not a distant or unrelated lag. QUANTUM's own reading is correct
and precisely calibrated: this is not a "the shape match is basically
noise" result (it sits at the ~97th percentile of its own null, sharply
unlike leg (a)'s period-match at the 50th) — but it is also not an
untouchable global optimum among all 31 circular registrations, and the
record should state both facts plainly, exactly as QUANTUM's own §2.3
does. **QUANTUM's finding is adopted in full, independently confirmed.**
I additionally note (not previously stated anywhere in the record) that
the near-tie is itself informative: a genuine spatially-coherent physical
match should score comparably at its immediate neighbor and fall off
farther away, which is exactly the observed shape (0.9582 → 0.9629 →
0.8046 → falling further at larger shifts, before the wrap-around
proximity effect raises shift=+30 back up) — this is evidence *for*, not
against, treating the correlation as real structure rather than a single
lucky alignment.

---

## 4. Task item 3 — THERMODYNAMICS' Anchor-3 commensurability finding: adjudicated

**Ruling: Anchor 3, as adopted in `phase3_synthesis.md` item 4, is NOT
yet well-posed. THERMODYNAMICS is correct, and the gap is real, R9-class,
and non-load-bearing this cycle but must not be inherited into Iteration
62 as settled house discipline.**

Independently confirmed the two facts THERMODYNAMICS' argument rests on:

1. **The mask is a total block, not a partial reflection.** Read
   `leg_b_curve()` directly: `masked = np.where(rel <= mask_r_out, 0.0 +
   0.0j, E1)` — the field is set to *exactly* zero inside the rim span,
   confirmed by inspection, not attenuated or phase-shifted. This is a
   Kirchhoff perfectly-absorbing-screen idealization; it contains no
   reflected term of any kind, by construction.
2. **`ptp_b` and `R≤0.2%` are measured on different instruments, in
   different units of what they claim to bound.** `ptp_b` is a
   `weber()`-reduced spatial fringe contrast (a *local* ratio of two
   window-averaged Poynting means at the observation plane, from a
   vacuum, zero-reflectivity diffraction calculation). `R≤0.2%` is a
   *global* reflected-power/incident-power fraction, established at a
   structurally different measurement (exp-001/002's beam-behind/
   observer-return geometry, on the real `graded_black_shell` material).
   Sharing units of "relative field amplitude" does not make them the
   same quantity — this is precisely the class of gap R9 exists to catch
   (reproducing the division, `0.0821/0.002≈41`, is not the same as
   verifying the two operands are commensurable).

The consequence THERMODYNAMICS draws is correct: because the construction
that produces `ptp_b` contains no reflected term at all, the ~41× ratio
cannot be read as "this reflection-echo signal is 41× too large to be
real reflection" (there is no reflection-echo in the calculation to be
too large) — it is, at most, weak corroborating evidence that an
opaque-mask diffraction fringe is not a stand-in for a real absorber's
reflectance, a conclusion the mask's own `E→0` construction already
established more directly and elementarily. Used this way (as one more
piece of evidence for a conclusion already independently true, hedged
throughout the record, never asserted as a hard physical bound) the ~41×
figure is **not itself outcome-determining and does not, on its own,
trigger R9's Checkpoint-4 escalation clause this cycle** — it was not
filed into a permanent record as a "confirmed" comparison establishing a
claim by itself; Red Team's own Phase-2 attack 4 and Phase 3 both hedge it
correctly ("independent evidence for," "should be stated explicitly, not
left as an implicit consequence"). But **the standing rule Phase 3 adopted
for Iteration 62 — "compare each leg's predicted fringe amplitude against
the `graded_black_shell`'s established `R≤0.2%` ceiling as a mandatory
Anchor 3" — is written as if the two operands are already commensurable,
and they are not, for any construction shaped like this cycle's opaque
mask.**

**Minimal fix, adopted into the fix docket below (not a rewrite of the
underlying idea, which is sound)**:

1. **Scope Anchor 3 to constructions that actually contain a physically-
   scaled reflected term.** It is not a meaningful check against an
   all-or-nothing opaque (Kirchhoff) mask — only against a future leg (b)
   rebuild where the rim is modeled as `E → r·E` (a genuine partial
   reflection, `|r|²` set from the established ceiling or a real
   admittance-based `r(θ)`), exactly as THERMODYNAMICS' and MATERIALS' own
   Iteration-62 proposals already independently converge on building.
2. **Produce operand B through the identical `weber`/`window_means`
   pipeline that produces `ptp_b`, not by importing `R≤0.2%` wholesale
   from a different measurement geometry.** Concretely: propagate a known,
   physically-scaled reflectivity through the *same* leg-(b) construction
   (the same `d1`/`d2`, the same window/flank geometry) to obtain the
   Weber-contrast fringe amplitude a genuine reflection of that magnitude
   would produce *at this specific near-field geometry*, and compare
   *that* number — in the same units, from the same pipeline — to the
   observed `ptp_b`. This closes the commensurability gap by construction
   rather than by argument.

This is THERMODYNAMICS' own §2.3/§3-item-1 recommendation, adopted
verbatim as the correct minimal fix. It does not change Combined Verdict
(leg (b) already carries NO VERDICT via Anchor 2's independent failure)
and does not itself fire Checkpoint criterion 4 (caught same-shift, at
Phase 5, before LOGBOOK, on a finding that is not yet load-bearing —
matching this program's own established non-firing shape for a same-layer
catch). It is logged in the fix docket and the Iteration-62 ranking below
as a precondition for Anchor 3, not an optional refinement.

---

## 5. Task item 4 — VISION's Checkpoint-ritualization concern: adjudicated directly

**Ruling: the concern is legitimate and should be surfaced to Marsh
explicitly, but the diagnosis "the mechanism has lost teeth" is not what
the record actually supports. The more precise, defensible finding is
narrower: 13 consecutive notification-only firings is not itself evidence
of toothlessness, because the object-level fix has landed same-shift in
every one of the 13 cases regardless of whether Checkpoint 4 fired — but
THIS firing specifically exposes a real design gap in the escalating-
tripwire format that VISION's framing gets at without quite naming.**

**Why "notification, not pause" is not, on its own, evidence of
toothlessness.** PANEL.md's own text is explicit and was written this way
from the start, not discovered as a loophole after the fact: *"The program
runs essentially continuously in the background. Marsh is convened ONLY
at [five listed criteria]... On checkpoint: a CHECKPOINT entry in
LOGBOOK.md + SESSION_LOG.md, and Marsh is notified. Unblocked threads keep
running."* A standing human veto that is exercised at will, not a required
gate that blocks forward progress pending a response, is the explicitly
designed shape of this program's governance — "notification, not pause"
restates the design, it does not describe an emergent failure of it.
Separately and more importantly: **firing and fixing are different axes,
and the record conflates them if read carelessly.** In every one of the
prior 12 firings this audit or the six Phase-5 reviews touched (and, by
LOGBOOK's own account, in every firing on the books), the *substantive*
defect the tripwire is about — a wrong verdict, a sign bug, a dimensional
error, a silently-dropped check — was independently corrected via the
ordinary Phase-2/Phase-3/Phase-5 PROCEED-WITH-MANDATORY-FIXES machinery
*before* the firing is even logged. Checkpoint 4 is not the mechanism that
fixes anything; it is the mechanism that puts an unmissable, permanent,
Marsh-visible record of "this happened, on this program's own written
schedule" next to a fix that already happened through the normal review
layer. A tripwire whose job is exactly that — make silent recurrence
visible in the permanent record and notify the one human with standing
veto, without itself blocking work no human is required to gate — is
doing its job every time it fires, independent of whether the firing event
itself "does" anything further. The record also shows the threat of firing
has produced real behavior change more than once (Iteration 59's PAD-
loaded article check was built specifically to preempt a 7th-deferral
firing named at Iteration 56/57; this cycle's own Director explicitly
declined to retrofit a rushed fix purely to dodge the firing, calling
that exactly the kind of after-the-fact rationalization R8 exists to
catch, and let it fire instead) — a mechanism that shapes what a Director
is willing to do specifically to avoid a bad look in a permanent record is
not one with "zero consequence," even though no run is ever paused.

**Where VISION's instinct is right, more precisely stated than "13/13 is
ritual": this specific firing is the first in the escalating-tripwire
lineage (R6–R9-style "N consecutive deferrals fires automatically") where
the deferral was not a discretionary choice but a genuine scope mismatch.**
EM's own Phase-5 review independently establishes this (§2.3, adopted
above): the *full* joint energy-interception check, as scoped at Iteration
59, requires a real article-loaded FDTD field to bound intercepted vs.
re-radiated power against — and exp-084 has none (leg (a) is vacuum-only
by Idealization 4; leg (b)'s own numbers are independently invalidated by
Anchor 2 before any trustworthy amplitude exists to bound). Exp-082's and
exp-083's own silent absences of this same item *did* have live
article-loaded data available and skipped it anyway — those were genuine
discretionary neglect, exactly the pattern the tripwire exists to punish.
This cycle's absence is structurally different: a zero-FDTD desk cycle
landing in the lead rotation cannot engage a check that needs an
article-loaded scene, no matter how the Director prioritizes its own
time. The pre-committed tripwire text ("a third consecutive deferral
without an explicit reason fires it, no further deliberation") has no
clause distinguishing these two cases, so it fires identically on both —
correctly and by design in exp-082/083's case, but on what amounts to a
technicality in exp-084's case. **This is the real mechanism by which a
correctly-designed governance tool can start to look like ritual: not
because nobody is watching, but because an escalation counter with no
applicability gate accrues identically whether the underlying opportunity
to comply existed or not**, diluting the signal a 13th consecutive firing
carries for a reader trying to tell "neglect" from "scope."

**Ruling, stated plainly**: Checkpoint criterion 4 correctly fires this
cycle (Section 7 below) — the *literal* condition (a third consecutive
cycle with the item neither run nor explicitly deferred-with-reason in
Phase 1/Phase 2, before any post-hoc rationalization) is true, and the
Director's own decision not to game it with a same-shift excuse is the
right call, independently re-affirmed here. But the LOGBOOK entry should
say, precisely, what EM's review already supplies: this cycle had no
article-loaded scene to run the full check against, and a cheap partial
discharge (the reflectance-ceiling sanity comparison, Red Team's own
Phase-2 attack 4 / THERMODYNAMICS' Anchor 3) did happen same-shift —
crediting this narrows exp-084's own contribution to the pattern without
excusing exp-082's/exp-083's genuinely discretionary misses. And VISION's
own meta-question — should the panel treat 13-for-13 notification-only as
itself worth a Marsh-level question — is adopted as a **named, standing
governance item for Iteration 62's board** (Tier 3 below), not dismissed:
not because the mechanism has failed, but because an escalating tripwire
format with no scope-applicability clause is a genuine, fixable design
gap that will keep producing exactly this kind of diluted firing on any
item that is inherently scene-dependent, and a program 13 firings deep is
the right moment to close that gap rather than the 20th.

---

## 6. Task item 5 — R10's final wording

**Ruling: adopt QUANTUM's tightened formulation, with the escalation
clause and format brought into exact alignment with R6–R9's own house
style, cast as a single registry bullet (not a `##` section) per QUANTUM's
own correctly-identified structural gap. Full text below is what should
go into LOGBOOK's RULED OUT registry, immediately after R9.**

QUANTUM's own critique of the draft R10 (phase3_synthesis.md's "New
standing rule — R10" section) is independently confirmed correct on all
four points: (1) it is formatted as a `##` section, not a registry bullet
— a real structural mismatch against R6–R9's own single-bullet form,
confirmed by direct comparison against the registry text above; (2) it
carries no escalation clause at all — confirmed: R6 ("no further
deliberation"), R7 ("if it survives to Phase 3 unchanged"), R8 ("if the
named check was affordable and not run"), R9 ("when the comparison later
proves incommensurable") each state one; R10's draft text states only the
rule, never its consequence — R10 as drafted is genuinely the only member
of this four-rule lineage with no teeth, independent of §5's finding above
about criterion 4 in general; (3) no trailing "Full record:" citation —
confirmed absent; (4) the "open question" paragraph sets no bar for when a
non-circular-shift surrogate may be trusted, which is exactly the gap
Iteration 60's own EM/Red-Team AR(1) episode (an unreproduced surrogate
number, caught only because Red Team happened to rebuild it from scratch)
shows is not hypothetical — it already happened once, one cycle before R10
existed to name it.

QUANTUM's proposed replacement text is sound: it makes circular-shift the
mandatory default (closing the "any self-labeled surrogate could be cited"
gap), requires a surrogate's *family* to be justified by a stated
diagnostic of the data's own dependency structure *before* running (not
selected post hoc for a favorable answer — the same discipline R7 already
established for conditioning-number selection), requires independent
re-implementation-and-reproduction of a surrogate's own headline figure
before it is cited (matching this program's existing R4/R6 standard,
applied here to null-construction code specifically), states a tie-break
rule when tests disagree, and supplies the missing escalation clause. I
adopt it with only cosmetic tightening for registry-bullet form and one
substantive addition — QUANTUM's own flagged nuance about deterministic,
zero-noise desk curves (this cycle's own leg (a)) asking a different
question than real noisy FDTD data, which QUANTUM itself said deserved a
sentence in R10 and did not have room to draft; I supply it below.

**Final R10 text, for LOGBOOK's RULED OUT registry:**

> - **R10 — a specificity-over-candidate-targets sweep is not a
>   substitute for an order-preserving null-under-noise test; circular-
>   shift-on-the-real-data is the mandatory default, and a non-circular-
>   shift surrogate may supplement but never replace it without its own
>   independent verification (not a ruled-out idea; a standing
>   house-discipline rule, adopted Iteration 61, generalizing Red Team's
>   own recommendation in the R6/R7/R8/R9 lineage).** exp-084's leg (a)
>   nominally cleared its own pre-registered R5 specificity-over-targets
>   control (`5/60=8.3%` of candidate target periods also matched) and was
>   self-scored SUPPORT on that basis — but an order-preserving
>   circular-shift null on the SAME fitted curve, run against the literal
>   production `free_period_with_widening` pipeline, showed `R²=0.3697` is
>   met or exceeded by `15/30=50.0%` of the curve's own circular shifts,
>   sitting at the null distribution's median, not a rejection tail — the
>   verdict reverses. This is the second consecutive cycle (Iteration
>   60/exp-083's two-tone admixture claim; Iteration 61/exp-084's leg (a))
>   this exact divergence — a specificity-over-targets sweep reading
>   falsely reassuring while an order-preserving null-under-noise test
>   reverses the verdict — has been outcome-determining. **Rule: any
>   future free-period-fit or free-phase-fit SUPPORT/CONFIRM verdict must
>   clear a circular-shift-on-the-real-data null test — the mandatory
>   default, always run and reported even when another surrogate is also
>   tried — before it is reported as evidence; a specificity-over-
>   candidate-targets sweep alone is not sufficient.** A non-circular-shift
>   "equivalent structurally-matched surrogate" (AR(1)-parametric,
>   phase-randomized/IAAFT, wavelet-matched, or other) may supplement but
>   never replace the circular-shift verdict unless (a) the surrogate
>   family is justified, *before* it is run, by a stated diagnostic of the
>   observed data's own dependency structure (e.g. measured
>   autocorrelation or periodogram) — never selected after seeing which
>   surrogate gives the more favorable answer — and (b) the surrogate's
>   own null-generating code is independently re-implemented from scratch
>   by a second seat and its headline figure reproduces, matching this
>   program's existing R4/R6 reproduction standard, before it is cited in
>   a permanent record (Iteration 60's own EM/Red-Team episode — an
>   AR(1)-parametric figure that did NOT independently reproduce,
>   `p≈0.09–0.10` vs. the claimed `0.766` — is the standing cautionary
>   instance this clause exists to prevent recurring). If a validated
>   alternative surrogate and circular-shift disagree, both are reported
>   side by side and the more conservative one governs the verdict. When
>   the "observed curve" is itself a deterministic, zero-measurement-noise
>   quantity (a closed-form desk evaluation, not real instrument data with
>   physical noise — as in exp-084's own leg (a)), state explicitly that
>   the circular-shift result answers a self-similarity/specificity
>   question ("how much does this curve's own smoothness alone explain an
>   apparently good fit"), not a literal measurement-noise question — both
>   are legitimate uses of the same test, but conflating the two
>   misdescribes what "distinguishable from noise" means for a curve that
>   has no noise in it at all. **A cycle that ships a free-period/
>   free-phase SUPPORT verdict backed only by an unreproduced surrogate, or
>   that omits the mandatory circular-shift baseline entirely, fires
>   Checkpoint criterion 4 automatically — the one gap where R10, alone
>   among the R6–R9 lineage, previously carried no escalation
>   consequence.** Full record: `experiments/084-t28-edge-diffraction-
>   derivation/phase2_redteam_audit.md` §3, `phase3_synthesis.md` ("New
>   standing rule — R10"), `phase5_review_quantum.md` §3–§4,
>   `phase5_redteam_audit.md` §6, LOGBOOK.md Iteration 61.

---

## 7. Checkpoint ruling — all five criteria, reasoned through explicitly

**Criterion 1** (a configuration passes all constraint metrics): **N/A.**
Zero constraint-3/4 engagement anywhere in this cycle — confirmed by my own
fresh grep of `phase1_proposal.md`/`phase1_derivation.py`/`NOTES.md` for
`weber`/`window_means` usage: every call reduces a period-match/shape
comparison, never a threshold or adaptation quantity.

**Criterion 2** (a proven mechanism-class boundary): **N/A, not merely
not-yet-ripe — matching every T28 desk cycle since exp-069.** This is
instrument-fidelity/artifact-attribution work internal to the bench; no
mechanism-class claim bearing on any phenomenon constraint is made
anywhere, including in this audit's own new findings (the scale-invariance
proof, the shape-correlation null test, the Anchor-3 ruling are all
instrument-level facts).

**Criterion 3** (engine physics beyond validated bench classes): **N/A.**
`git diff --stat -- lab/` confirmed empty at HEAD by direct re-run. Zero
`lab/` files touched this cycle.

**Criterion 4** (program-integrity drift): **Fires, on the one matter
Phase 3 already identified — reasoned through independently, not a rubber
stamp, and its framing is sharpened per §5 above.**

*7a. The energy-interception cross-check's third consecutive silent
absence.* Independently re-traced the full chain from LOGBOOK's own T28
narrative (Iteration 59: item first named; Iteration 60: "now a second
consecutive deferred cycle... a third consecutive deferral without an
explicit reason would fire it"; Iteration 61/exp-084: zero occurrences of
"Poynting"/"interception"/"cross-check" anywhere in Phase 1 or the five
Phase-2 critiques, confirmed by my own grep, matching THERMODYNAMICS' and
Red Team's Phase-2 identical count). The literal, pre-committed condition
is true. **Fires — the 13th time in this program, per the Director's own
count, independently spot-checked against LOGBOOK's own explicit "11 for
11"/"12 for 12" citations at earlier points in this exact chain and found
consistent.** Ruled **notification, not a pause**, per this program's
unbroken precedent — see §5 above for the full reasoning on why this
disposition is correct and not evidence of toothlessness, and for the
sharper framing this audit adds: **the LOGBOOK entry should state
precisely that this cycle had no article-loaded FDTD scene to run the full
check against (unlike exp-082's/exp-083's own genuinely discretionary
silent absences), and that a cheap partial discharge — the reflectance-
ceiling sanity comparison (Red Team's Phase-2 attack 4 / THERMODYNAMICS'
Anchor 3) — happened same-shift and should be credited, though it does not
substitute for the full bound.** This does not change the firing (the full
check still was not run for a third consecutive cycle), only its
characterization.

*7b. Anchor 3's commensurability gap (§4, this audit).* Caught same-shift,
at Phase 5, before LOGBOOK — matching this program's own established
non-firing shape for a same-layer catch on a finding that is not yet
load-bearing (leg (b) already carries NO VERDICT via Anchor 2's
independent failure). **Does not fire** — but is logged (fix docket item
4, below) as a required precondition before Iteration 62 inherits Anchor 3
as settled.

*7c. The stale `phase3_fix_docket_results.json` (PHOTONICS' §2.1).*
Independently confirmed already fixed, in the same commit as the Phase-5
batch that found it (§0 above). **Does not fire** — a same-shift, non-
load-bearing catch, correctly not defended past a freeze point.

**Criterion 5** (two consecutive non-advancing iterations): **Not at
risk.** This cycle is the first in the nine-plus-cycle T28 sub-thread to
produce a positive shape-kinship result between a zero-FDTD vacuum
diffraction integral and real FDTD physics (`r=0.958`, now independently
confirmed on three separate axes: the original three-control comparison,
PHOTONICS' own aperture-sensitivity sweep, and QUANTUM's own circular-
shift null) — a genuine, logbook-advancing result, not a repeat of a prior
non-finding.

---

## 8. Same-shift mandatory-fix docket

1. **[Leg (a)'s verdict, already correctly downgraded]** No further action
   — INCONCLUSIVE on the period-match stands, independently re-confirmed
   here a further time (§0). The shape-correlation finding stands as the
   cycle's genuine positive result, now independently stress-tested on
   three separate axes (§0, §3).
2. **[Checkpoint-4 LOGBOOK language, §5/§7a]** State precisely, per §5's
   ruling: this cycle had no article-loaded FDTD scene for the full
   energy-interception bound; a cheap partial discharge (reflectance-
   ceiling sanity comparison) happened same-shift and is credited, though
   it does not substitute for the full bound, still queued for Iteration
   62 on a cycle with a real article-loaded scene.
3. **[Ritualization concern, §5]** Log VISION's meta-question as a named,
   standing Tier-3 governance item for Iteration 62's board (not dismissed,
   not treated as proof of failure): does the escalating-tripwire format
   (R6–R9/R10-style "N consecutive [X] fires automatically") need a
   scope-applicability clause, distinguishing "chose not to" from
   "structurally could not," before its own repeated firing on
   scene-dependent items dilutes the signal a firing is meant to carry?
4. **[Anchor 3, §4]** Do not carry `phase3_synthesis.md` item 4's wording
   into Iteration 62 unmodified. Scope Anchor 3 to a leg-(b) construction
   that contains a genuine, physically-scaled partial-reflection term (not
   an opaque Kirchhoff mask), and produce its comparison operand through
   the same `weber`/`window_means` pipeline that produces `ptp_b`, not by
   importing `R≤0.2%` from a different measurement geometry directly.
5. **[R10, §6]** Transcribe the final text in §6 above into LOGBOOK's
   RULED OUT registry, immediately after R9, replacing
   `phase3_synthesis.md`'s draft section in full.
6. **[Leg (b)'s causal diagnosis, EM's Test A/B + PHOTONICS' third
   hypothesis]** Do not adopt either "missing RS boundary term" or "missing
   bare phase factor" as settled. EM's own §2.1 proves the bare-phase-
   factor reading dead by algebra and execution (§2, this audit); PHOTONICS'
   own §2.3 names a third, cheaper, untested candidate (domain truncation
   at the fixed `[y_lo,y_hi]` intermediate window) that the existing
   convergence test cannot distinguish from either standing hypothesis.
   Queue PHOTONICS' own cheapest-first test (widen the intermediate window,
   holding sampling density fixed) alongside EM's own named matrix-valued
   RS/Kirchhoff kernel test, before Iteration 62 commits to a causal story.

None of the above touches `lab/`, any frozen prediction, or any RULED-OUT
item. No new FDTD is run by this audit.

---

## 9. Combined Verdict for the record: **PARTIAL**

For LOGBOOK.md's Iteration 61 entry, verbatim in substance:

**Leg (a) — INCONCLUSIVE on the period-match question, CONFIRMED POSITIVE
on shape-correlation, both independently re-verified a further time by
this audit.** The model curve's free-fit period (`P_model_a=2.5338°,
R²=0.3697`) nominally cleared the pre-registered SUPPORT band
(`rel_dev=0.1085`), but is met or exceeded by `15/30=50.0%` of the real
curve's own order-preserving circular shifts (this program's established
"harder companion" null, independently re-run here bit-exact) — the fit
sits at its own null distribution's median, not a rejection tail; VISION's
own pre-registered T21-decorrelation test, run to its conclusion,
independently mandates the identical downgrade by an unrelated route. The
period question is not settled either way — it is shown, correctly, to be
unresolved at this sample size, not refuted. **The surviving, genuinely
new positive finding**: the model curve's raw shape correlates `r=+0.958`
with the real FDTD `C80(θ)` curve — far above three unrelated controls
(`|r|<0.35`), independently confirmed by this audit's own re-run, and now
independently stress-tested on two further axes this cycle adds: (a)
PHOTONICS' own aperture-width sensitivity sweep (independently
reconstructed here) shows the match is structure-sensitive, not a generic
smoothness artifact — it degrades sharply within ±1–5% of the true
aperture width; (b) QUANTUM's own circular-shift null on the correlation
itself (independently re-run here bit-exact) shows `R²`/`r` sits at the
~97th percentile of its own null distribution — sharply unlike the
period-match's 50th — with an honest caveat that the best-scoring shift is
the immediately adjacent one, consistent with genuine spatially-coherent
structure, not a cherry-picked global optimum. **This is the first result
in this nine-plus-cycle T28 sub-thread showing a zero-FDTD, vacuum-only
diffraction construction tracking real FDTD physics this closely, on any
axis.**

**Leg (b) — NO VERDICT stands, an instrument-validation failure correctly
self-caught before a false conclusion could be drawn.** Anchor 2 (a
composition-of-propagators identity) fails a convergence-checked test
(stable 2.894–2.895 ratio across 1×–8× oversampling, ruling out
discretization). This audit independently, algebraically and by direct
execution, **proves** (not merely argues) that a bare global complex
constant — the specific form of EM's own named alternative hypothesis —
is powerless to close this gap, for a structural reason specific to this
bench's own `weber()` scale-invariance; the real fix requires a genuinely
position-and-observation-point-dependent kernel. PHOTONICS' own review
adds a third, cheaper, still-untested candidate cause (intermediate-window
truncation) the existing convergence test cannot rule out. Two competing,
now-better-specified causal hypotheses remain open for Iteration 62.
**THERMODYNAMICS' proposed Anchor 3 (fringe amplitude vs. the
`graded_black_shell`'s `R≤0.2%` ceiling) is real, useful diagnostic
evidence but is not yet a commensurable comparison** — comparing a
Weber-contrast fringe from a zero-reflectivity opaque-mask construction to
a global reflected-power fraction from an unrelated measurement geometry
is an R9-class gap, adjudicated and minimally fixed in this audit (§4):
scope it to a construction with a genuine partial-reflection term, and
produce both operands from the identical pipeline.

**New standing rule R10 adopted** (final text, §6 above): a
specificity-over-candidate-targets sweep is not a substitute for an
order-preserving null-under-noise test; circular-shift-on-the-real-data is
the mandatory default, with an escalation clause and a surrogate-
validation bar this audit adds to close the one gap (missing teeth) where
R10's own first draft was the sole exception among the R6–R9 lineage.

**Checkpoint criterion 4 FIRES — the 13th time in this program — on the
energy-interception cross-check's third consecutive silent absence,
ruled notification, not a pause, per unbroken precedent.** This audit
independently reasoned through, rather than pattern-matched, whether that
disposition still functions as real governance (§5): it does — the
substantive object-level defect the tripwire exists to catch is, in every
one of the 13 firings on this program's record, independently corrected
through the ordinary Phase-2/3/5 review layer *before* the firing is
logged, so "notification, not pause" describes a deliberate design choice
(Marsh holds a standing veto, exercised at will, never a required gate),
not an absence of consequence. But this specific firing exposes a genuine,
fixable design gap the ritualization concern correctly points toward: the
escalating-tripwire format has no clause distinguishing a cycle that
chose not to run a scene-dependent check from one, like this one, that
structurally could not (no article-loaded FDTD scene existed in exp-084 at
all) — diluting exactly the signal a 13th consecutive firing is meant to
carry. Logged as a named Tier-3 governance item for Iteration 62, not
dismissed and not treated as proof the mechanism has failed.

---

## 10. Reconciled ranking for Iteration 62's queue

### Tier 0 — zero FDTD, desk-only

1. **[R10, finalized, §6/§8 item 5]** Transcribe the final R10 text above
   into LOGBOOK's RULED OUT registry immediately after R9, replacing the
   draft section in `phase3_synthesis.md` in full.
2. **[Anchor-3 rescoping, §4/§8 item 4]** Rewrite the standing Anchor-3
   requirement before any future leg-(b) attempt inherits it: scope to a
   construction with a genuine partial-reflection term; produce both
   operands from the identical `weber`/`window_means` pipeline.
3. **[Checkpoint-4 LOGBOOK precision, §5/§8 item 2]** State explicitly:
   this cycle had no article-loaded scene for the full energy-interception
   bound (a scope mismatch, not discretionary neglect, unlike exp-082's/
   exp-083's own silent absences); a cheap partial discharge (Anchor
   3/attack 4) happened same-shift and is credited.
4. **[Ritualization item, named, §5/§8 item 3]** Add to the board: should
   the R6–R9/R10 escalating-tripwire format gain a scope-applicability
   clause (distinguishing "chose not to" from "structurally could not")
   before its own repeated firing on scene-dependent items dilutes the
   signal further? A genuine, fixable governance design question, not a
   rhetorical one.
5. **[Leg (b)'s causal diagnosis, narrowed, §2/§8 item 6]** Log: a bare
   global phase/normalization constant is proven, not argued, powerless to
   close Anchor 2 (this audit's own algebraic-plus-executed proof); do not
   re-test variants of it. Two live candidates remain: EM's own
   matrix-valued RS/Kirchhoff kernel (position-*and*-observation-point-
   dependent), and PHOTONICS' own domain-truncation hypothesis (widen the
   intermediate `[y_lo,y_hi]` window, holding sampling density fixed) —
   the latter is cheaper and should be run first.
6. **[Shape-correlation robustness, credited, §0/§3]** Log all three
   independent stress tests this cycle's own record now carries for
   `r=0.958`: three unrelated-shape controls (original), an aperture-width
   sensitivity sweep (PHOTONICS, independently reconstructed here), and a
   circular-shift null on the correlation itself (QUANTUM, independently
   reconfirmed here, 1/30=3.3%, near-tied with the adjacent lag).

### Tier 1 — cheap FDTD-adjacent / zero-marginal-cost next

7. **QUANTUM's own wide-window zero-FDTD re-evaluation of leg (a)'s model
   period** (§4 of its own review) — the single sharpest, cheapest
   available next test: `leg_a_curve()` is a deterministic, arbitrarily
   re-evaluable function of θ; holding the real target period fixed and
   evaluating the model over a much wider angular span (zero marginal
   FDTD cost) can pin `P_model_a`'s own asymptotic period to near-machine
   precision, settling the period question with certainty rather than a
   p-value, independent of any 31-point sampling window's own null
   distribution. Near-unanimous top-2 pick (QUANTUM #2, PHOTONICS #2 by
   substance if not by name).
8. **PHOTONICS' domain-truncation test for Anchor 2** (§2.3 of its own
   review, upgraded to Tier 1 alongside EM's own named test per fix-docket
   item 6, above) — strictly cheaper than EM's kernel rebuild (no new
   physics convention, just a wider `arange`), and a precondition for leg
   (b) — the one leg with genuine realizability content per MATERIALS —
   ever producing a trustworthy verdict.
9. **EM's own matrix-valued RS/Kirchhoff obliquity-kernel rebuild for leg
   (b)'s stage-2 propagation**, informed by this audit's own negative
   result on the bare-phase-factor alternative (§2) — scope as its own
   small, pre-registered proposal, not a patch under time pressure, per
   Phase 3's own correct original scoping.
10. **The rescoped Anchor-3-compliant leg (b) rebuild** (THERMODYNAMICS'
    own Iteration-62 proposal #1, item 4 above) — replace the opaque mask
    with a physically-scaled partial reflection (`E→r·E`, `|r|²≈R_ceiling`
    or a real admittance-based `r(θ)`, reusing already-gated exp-081
    primitives), gated behind items 8–9 above (fixing the causal
    diagnosis first, not compounding two open errors). This is also the
    construction that would, for the first time, let MATERIALS assign a
    published/plausible/unobtainium verdict to the article-rim question.

### Tier 2 — standing, increasingly overdue items

11. **The joint EM/THERMO energy-interception cross-check, full form** —
    still not run; Checkpoint-4 fired on its third consecutive absence
    this cycle (§7a); highest institutional priority for the first
    Iteration-62 cycle with a real article-loaded FDTD scene to reuse, per
    Iteration 59's own original scoping. Do not attempt a rushed,
    scope-mismatched version again purely to avoid a further firing —
    build it properly, once, as its own concretely-scoped formula with a
    pre-registered band (per EM's own §3 ranking item 2).
12. **The near-null σ(I) article follow-up** — still not run, now the
    single most overdue realizability-adjacent item on the whole T28
    board (named since Iteration 59).
13. **QUANTUM's own lossless-PEC-only-disk control** — still open.
14. **The `PAIR_ABSORB40`/`C80−C40` extension** — still open.
15. **The x-wall wavelength-generality leg (750/450nm)** — now **NINE**
    consecutive cycles deferred (076–084), the single oldest, most overdue
    item on the entire T28 board.
16. **A proper R3-grade settling convergence study with the article
    present.**

### Tier 3 — governance

17. Checkpoint criterion 2 ruled N/A this cycle, not merely not-yet-ripe —
    reasoned through explicitly against this audit's own new findings
    specifically (§7).
18. Checkpoint criterion 4 ruled FIRING (the 13th time), notification-not-
    pause, on the energy-interception item's third consecutive silent
    absence — with this audit's own sharpened framing (§5/§7a) crediting
    the partial discharge and naming the scope-mismatch distinction.
19. **The ritualization question itself, named as a standing Iteration-62
    board item** (§5/§8 item 3) — not resolved this cycle, deliberately:
    whether the R6–R9/R10 escalating-tripwire format needs a
    scope-applicability clause before a 14th, 15th, or 16th firing further
    dilutes what a firing is meant to signal.

---

## 11. Bottom line

**Combined Verdict: PARTIAL.** Leg (a)'s period-match question is
correctly downgraded from SUPPORT to INCONCLUSIVE (does not clear this
program's own harder-companion null, independently re-confirmed here); its
shape-correlation finding (`r=0.958`) is real, independently confirmed a
further two ways this audit adds (an aperture-width sensitivity sweep,
a circular-shift null on the correlation itself), and stands as the first
result in this nine-plus-cycle T28 sub-thread showing a zero-FDTD vacuum
diffraction construction tracking real FDTD physics this closely on any
axis. Leg (b) remains NO VERDICT, its Anchor-2 failure now sharpened by an
algebraic-and-executed proof that rules out one of its two candidate
causes outright and by a third, cheaper, untested candidate cause neither
prior document named. THERMODYNAMICS' Anchor 3 is real diagnostic evidence
but not yet a commensurable comparison, minimally fixed here. R10 is
adopted with the one gap (a missing escalation clause) that made it the
sole exception among the R6–R9 lineage now closed. Checkpoint criterion 4
fires — the 13th time — correctly, as notification not pause, a design
choice this audit independently re-affirms is not evidence of
toothlessness on its own terms, while crediting VISION's sharper,
narrower, genuinely actionable concern: the escalating-tripwire format
itself needs a scope-applicability clause before a mechanically-accruing
counter dilutes the very signal it exists to carry. T28's own founding
question — `P_edge_A`'s ultimate physical origin — remains open, narrowed
for the first time in this sub-thread's history toward a genuine physical
kinship with near-field diffraction rather than toward another refuted
reflection-echo class.
