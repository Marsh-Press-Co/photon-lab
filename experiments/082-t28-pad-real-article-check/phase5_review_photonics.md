# PHASE 5 — REVIEW · PHOTONICS · Panel Iteration 59 · exp-082

**Seat: PHOTONICS.** Fresh sub-agent, zero memory of any prior session —
including zero memory of my own predecessor seat's Phase-2 critique this
same cycle (`phase2_critique_photonics.md`), which I read fresh, as a
document I did not write. Blind to every other seat's own Phase-5 review
this cycle; `phase5_review_vision.md` already exists in this directory and
I did not read it (one line surfaced incidentally in a grep while tracing a
JSON field — noted and discarded, not used below). Read, in order: PANEL.md,
AGENTS.md, LOGBOOK.md (RULED OUT R1–R9, ESTABLISHED, LIVE THREADS in full,
T28's complete Iteration 46–58 history), PLAN.md's Iteration-59 queue, and
the complete `experiments/082-.../` record: `phase1_proposal.md`,
`NOTES.md`, `run.py`, `results.json`, `run_output.txt`,
`x_wall_realizable_refit.py`/`_results.md`/`_results.json`/`x_wall_output.txt`,
`phase_convention_extension.py`/`_results.md`/`_results.json`/
`phase_convention_output.txt`, all five Phase-2 critiques, and
`phase2_redteam_audit.md`. No RULED-OUT item (R1–R9) is re-proposed or
re-litigated below.

**Independent verification performed, not asserted from memory.** I did not
trust Red Team's Phase-2 audit's own numbers on its say-so — I rebuilt the
load-bearing statistics from raw primitives myself, in a session-local
scratch environment, touching nothing under `experiments/082-.../`:

- Recomputed `A_scene`, `A_empty`, `ratio` directly from `results.json`'s
  `delta_scene`/`delta_empty` arrays: bit-identical to the committed
  `0.6573`.
- Recomputed the Pearson correlation myself: `r = 0.0305731...` — matches
  the audit's `0.0306`/`0.031` exactly.
- Ran my own **exact 7!-permutation test** (5040 permutations, not the
  audit's number taken on faith): two-sided `p = 0.9530` — matches
  `p=0.953` exactly. I also independently derived the exact critical value:
  sorting all 5040 permuted `|r|` values, the 5%-tail cutoff is
  `|r|=0.7456` (252/5040 = exactly 0.05) — matches the audit's cited
  `≥0.746` to the digit.
- Reimplemented `_fixed_period_fit`/`_free_period_search` from
  `experiments/069-.../run.py` myself (not copied output, rebuilt from the
  committed source) and ran the `[1,4]°` narrow-stage search on both series:
  `delta_scene` → `P*=2.9398°, R²=0.8583`; `delta_empty` → `P*=1.0150°,
  R²=0.8637` — matches the audit's `2.940°/0.858` and `1.015°/0.864` to
  three decimals, and `rel_dev=1.896` reproduces exactly.
- Confirmed the ground-truth citation directly in its own source file:
  `experiments/077-.../pad_round_trip_results.json::test_a_pair_pad.real.
  chosen.p_star_deg = 4.611289746337977` — the full 31-point PAIR_PAD fit,
  widened to `[1,15]°` after hitting the `[1,4]°` boundary. `|4.611−1.015|
  /4.611 = 0.7799` — the audit's "78% miss" reproduces exactly.
- Vectorized and re-ran a 20,000-trial null-permutation control (the
  audit's own 200,000-trial version, at 1/10 the trials — a genuine
  independent re-implementation, not the same code): `P(R²≥0.858)=0.272`,
  `P(R²≥0.864)=0.263` — matches the audit's `0.272`/`0.257` to within
  expected Monte Carlo noise at this trial count.
- Checked the lag cross-correlation instability claim myself at all 9
  integer lags: values swing from `−0.71` (n=5) to `+0.998` (n=3) with no
  stable peak — the same qualitative pattern the audit reports (my lag-sign
  convention is mirrored relative to the audit's, a trivial labeling
  difference; the instability finding matches).
- Traced the disputed `6.1530×10⁻⁴` secondary-metric comparator to its
  actual source. My first attempt pulled `A_i`/`A_q` from
  `leg750_scored.carrier_diagnostics_PAIR_PAD` (a same-named-but-different
  750nm-leg field) and got `1.506×10⁻³` — a real mismatch against the
  audit's cited figure. The correct source is `headline.pair_pad.A_i/A_q`
  (the primary, official 600nm result): `√(A_i²+A_q²)=6.153024×10⁻⁴`,
  exact to the audit's own digit. With the correct field, both of the
  audit's downstream numbers reproduce exactly: naive `5.538×`, ptp-
  equivalent `1.2306×10⁻³`, corrected ratio `A_scene/ptp-equiv = 2.769×`.
  **Finding (LOW, non-load-bearing): the audit's own citation path,
  `results.json::carrier_diagnostics_PAIR_PAD`, is ambiguous — a
  differently-scoped field of the identical name exists at
  `leg750_scored.carrier_diagnostics_PAIR_PAD` and gives a materially
  different number (`1.506×10⁻³` vs `6.153×10⁻⁴`, 2.45× apart). The cited
  NUMBER is verified correct (sourced from `headline.pair_pad`); the path
  LABEL is not precise enough to disambiguate the two fields on its own.**
  Worth a one-line path correction (`headline.pair_pad.A_i/A_q`, not the
  bare field name) if this figure is ever re-cited; does not change any
  verdict, does not fire R4/R9 (the number itself is right, only the
  pointer to it is underspecified).

**Every other load-bearing number in `phase2_redteam_audit.md` §0 that I
attempted to independently rebuild reproduced exactly.** I did not find a
second discrepancy after resolving the one above.

---

## 1. Does the corrected record actually resolve what my predecessor
   PHOTONICS seat found?

Yes, cleanly, in both places that matter. My predecessor's Phase-2 attack
(`phase2_critique_photonics.md`) found `r=0.031` and argued this makes
"SURVIVES... not yet distinguishable from an artifact of the 7-point/1°-step
design" — a real finding, but one that only names the gap, not its full
depth. Red Team's audit (independently reproduced above) went further and
proved the gap is not merely under-tested but **structurally unresolvable
at this instrument's own power** — a stronger, more falsifiable claim, and
the corrected record states exactly that distinction, not a watered-down
version of it:

- **`NOTES.md`, "Learned" §2**: "The shape/mechanism-identity question is
  **demonstrated, not merely under-supported, to be below this instrument's
  own resolving power at n=7**" — states the four converging lines of
  evidence by name (permutation test, divergent free periods, the
  ground-truth miss, the null-permutation control) and correctly attributes
  the finding to Red Team's own §0, not restated as though independently
  re-derived in `NOTES.md` itself.
- **`phase1_proposal.md`, "PHASE 1 RESULTS"**: the pre-audit language is
  visibly struck and replaced in place, with an explicit banner
  ("[PHASE 3 — DIRECTOR SYNTHESIS APPLIED, superseding the language below
  in force.]") naming exactly what the old text overclaimed and why. The
  corrected "What this does NOT establish: mechanism continuity" section
  uses the identical "UNRESOLVABLE... not merely suspected" framing,
  itemizes all four lines of evidence with their numbers, and is explicit
  that "None of this proves the two series are unrelated either — that
  would itself require statistical power this instrument does not have at
  n=7" — correctly stating the finding is symmetric (rules out neither
  reading), not a disguised REFUTE.

Both documents also correctly keep the two claims separated rather than
letting the mechanism-identity correction bleed into the primary verdict:
`SURVIVES stands MECHANICALLY` (the `ratio=0.6573` computation, decisively
inside band, bit-exact reproduction) is stated as settled and untouched by
the correction, exactly as it should be — the correction narrows what
SURVIVES *means*, not whether the pre-registered band was cleared. I found
no place in either document where the two are conflated, and no place where
the corrected language quietly reverts to the old framing (I grepped both
files for "reaches the... channel" and "same... mechanism" outside the
explicitly-superseded and explicitly-corrected sections — no stray
recurrence).

**One gap, not previously flagged**: `phase3_synthesis.md` itself is the
clearest, most complete statement of the corrected framing (§4, "Corrected
headline framing") — but `phase3_synthesis.md` is a Director-authored
document, not `NOTES.md`/`phase1_proposal.md` themselves, and the task
brief's own question is specifically about the latter two. Having read all
three, my assessment is the correction genuinely landed in the two
documents that matter, not merely in the synthesis note describing them —
this is not a case of the fix being asserted in Phase 3 prose without the
underlying record actually being edited.

---

## 2. From my own charter's angle — a coherent optical-response story

**The task's own question: is there a coherent optical-response story for
WHY a phase-only PAD artifact might or might not survive with a real
absorber present, that a future, properly-powered (31-point) test should
predict in advance?** Yes — and the cycle's own data already contain a
concrete, falsifiable candidate for it, currently unremarked in the record.

**The physical setup.** `C = (B_obj − B_flank)/B_flank` is a ratio. The
flank windows sit outside `GUARD_OUT=185`, well clear of the object
(`R_OUT=78`), and see the same domain-scale illumination field the empty
scene does — so `B_flank`'s own θ-dependence should still carry the
PAD-tied wall-echo ripple, structurally, regardless of what sits in the
object window (this is a geometric fact about window placement, not an
assumption). The open question is what `B_obj(θ)` does: a `graded_black_
shell`+`pec_disk` article of radius `R_OUT=78` cells at `cpl=20` spans
`78/20 ≈ 3.9λ` at 600nm — large enough to present its own diffracting edge,
not a point scatterer. **A large absorbing disk's own rim is a second,
distinct source of angle-dependent interference structure at the
observation plane**, independent of whatever coherent echo the domain's
PEC walls produce. This is not a new mechanism class for T28 (T1: still
N/A, no constraint-3 claim implied) — it is a candidate explanation, from my
own charter (scattering cross-sections, angular dependence of a finite
absorbing object), for *why* `delta_scene(θ)` could show a comparable-scale
but decorrelated oscillation relative to `delta_empty(θ)`: not because the
same wall-echo mechanism persists in different form, but because a *second,
independent, article-edge-diffraction* oscillation of comparable magnitude
is superposed on it in the object window specifically (not the flank
windows, which sit outside the object's own diffraction near-field).

**A concrete, falsifiable discriminator for the next (31-point) test.**
This cycle's own 7-point free-period fit on `delta_scene` recovers
`P*=2.940°` — I flag this only as a *directional* hint, not evidence:
Red Team's own ground-truth check (§0j, independently reproduced above)
already proved this exact machinery recovers the *wrong* period for a
signal of independently-known period at this same n=7 power, so no period
recovered at 7 points should be trusted on its own. But the SHAPE of the
prediction is real and testable at full power: PAIR_PAD's own established,
already-known-correct period (31-point fit) is `P*=4.611°`
(`experiments/077-.../pad_round_trip_results.json`, confirmed above).
Separately, this sub-thread's own *original* T28 discovery period
(`C80−C40`, exp-069 Block DENSE, empty scene) is `P*≈2.8421°`, and T21's
own established source-taper fringe is `P(39°)≈1.9608°` — two *different*,
already-characterized diffractive periodicities, neither equal to `4.611°`.
**Pre-registerable prediction for the full 31-point `PAIR_PAD`-with-article
re-test**: if the article-loaded `delta_scene(θ)`'s TRUE free period lands
within the sub-thread's own established `≤20%` "within tolerance" band of
`4.611°`, that is positive evidence for mechanism continuity (the same
lossless wall-echo effect, observed through the article's own shadow term).
If it instead lands closer to the `≈2.84°` or `≈1.96°` family — periods
already tied to source/taper/aperture diffraction elsewhere in this
program's own record, structurally unrelated to the wall's own round-trip
distance — that is evidence for a qualitatively different, article-edge-
diffraction-dominated interaction, exactly the "new interaction" branch
Attack 1 left open. **This is a two-branch, falsifiable, charter-grounded
prediction a future cycle can commit to git before running the full window**
— sharper than "let's get more points and see," and it directly answers the
task's own question about what a properly-powered test should predict in
advance.

**A cheap, zero-FDTD desk pre-check exists before spending the 31-point
budget**, methodologically identical to this sub-thread's own precedent
(P-070-3, the `TAPER`-as-sub-aperture check that cleanly REFUTEd the
source-taper hypothesis at zero FDTD cost): does a coherent-sum construction
treating the article's own two rim edges as a pair of secondary apertures
(reusing `y_wall_aperture_sum.py`'s own already-built and already-gated
per-point-phase machinery, substituted with the article's `(obj_x±R_OUT,
obj_y)` edge coordinates in place of the y-wall's own edge coordinates)
predict a period closer to the `≈2.84°`/`≈1.96°` family than to `4.611°`,
using ONLY this cycle's own already-collected 7-point data as a shape
sanity check first. If it does, that is independent, converging evidence
for the article-edge-diffraction hypothesis before any new FDTD is spent —
if it does not, the hypothesis is cheaply falsified and the board should
not carry it forward.

---

## 3. Verdict on this cycle's own work: **PARTIAL**

Not PROMISING — no constraint-3 metric or mechanism-class boundary is
engaged (T1: N/A throughout, correctly and consistently stated). Not RULED
OUT — nothing here is falsified; the SURVIVES computation is decisive,
bit-exact, and correctly scoped, and the deeper mechanism question is
honestly shown open rather than incorrectly resolved either way. **PARTIAL**
is the correct call, for reasons independent of and reinforcing the
record's own self-scoring: this cycle (1) genuinely discharges PLAN.md's
six-cycle tripwire on item 7, the first article-loaded FDTD measurement in
nine T28 cycles; (2) delivers a real, decisively-inside-band SURVIVES result
on the flagship article class, correctly scoped (MATERIALS' Attack 2,
adopted) rather than generalized past its own evidence; (3) produces a
genuinely new, independently-reproducible instrument-limitation finding
(the free-period search's own ground-truth failure and null-permutation
near-miss at n=7) with implications for this sub-thread beyond this one
result; and (4) the Phase-2 overclaiming that would have made this a weaker
cycle was caught, independently re-derived from primitives (not merely
re-argued), and fully corrected before reaching this review, with the one
residual issue I found (the ambiguous JSON path label in Attack 5's own
citation) non-load-bearing and easily fixed. Checkpoint criteria: I concur
with the Phase-2 audit's own ruling — none fire, criterion 4 conditioned
on the fix docket landing, which my own independent re-reading of `NOTES.md`
and `phase1_proposal.md` (§1, above) confirms it did.

---

## 4. Ranked top-3 candidate directions for Iteration 60

1. **The full 31-point/0.2° `PAIR_PAD`-with-article re-test, pre-registered
   against the two-branch period prediction above (§2).** This is the
   single test that converts "the mechanism-identity question is
   unresolvable at n=7" into an actually-answered question, and it is now
   MORE specified than "get more points" — a genuine falsifiable prediction
   exists to commit to git before running it: TRUE period near `4.611°` →
   mechanism continuity; TRUE period near the `2.84°`/`1.96°` family →
   article-edge-diffraction, a distinct mechanism. Near-unanimous natural
   next step across every reviewer of this cycle who touched the
   correlation gap (my own predecessor seat, EM, Red Team); I add the
   specific falsifiable framing and the cheap zero-FDTD pre-check (§2) as
   what should precede it.
2. **The near-null σ(I) article follow-up** (MATERIALS' own flip condition,
   `off_pass`/`τ_off≈0.0065`, already named in `NOTES.md`'s own "Next"
   section). From my own charter angle this is not merely a generality
   check — it is a direct test of whether the fraction of the PAD ripple
   that "rides through" the ratio-channel scoring scales with the article's
   own absorption/extinction strength, a genuine optical-response question
   about how much of a boundary artifact a weakly-absorbing object leaves
   exposed versus a strongly-absorbing one. Comparable, testable prediction:
   if the ripple's *fractional* presence (ratio, not absolute amplitude)
   stays comparable across a ~100× change in the article's own baseline `C`,
   that argues for a background-dominated (flank-window-driven) mechanism;
   if it scales down sharply with weaker absorption, that argues the object
   window's own response is doing real work, consistent with the
   edge-diffraction hypothesis in §2 rather than a pure background
   systematic.
3. **`PAIR_ABSORB40`/`C80−C40` at the real article** (Idealization 3's own
   named-but-undone follow-up, also flagged in Red Team's own "Note for
   Iteration 60"). Tests whether SURVIVES is specific to the `PAD` axis or
   general to any boundary-tied confound once a real absorber occupies the
   object window — directly bears on whether the whole nine-cycle T28
   sub-thread's REFUTE-leaning mechanism-class rulings (all built on the
   empty scene) carry over once a real scene is involved, the same
   generalization question this cycle's own item 7 build was created to ask
   in the first place, now extended to the other two established pairs.

The x-wall wavelength-generality leg and the 750nm two-wall spot-check
remain real, long-deferred items — this cycle's own restored x-wall refit
(Tier 0 item 1) already partially serves the former — but neither is as
information-dense right now as resolving the mechanism-identity question
this cycle's own audit just proved is the board's best-characterized open
question. I would not defer them past Iteration 61 without an explicit
reason, matching this sub-thread's own established tripwire discipline.
