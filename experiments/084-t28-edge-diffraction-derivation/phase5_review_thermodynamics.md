# PHASE 5 — REVIEW · THERMODYNAMICS (blind, fresh instance) · Panel Iteration 61 · exp-084

*Zero memory of any prior session, including of my own Phase-2 critique this
cycle. Independent review, per PANEL.md and this seat's charter: where
absorbed energy goes; what re-radiates; is it detectable; owns the
per-proposal energy sidecar.*

## 1. Independent verdict: **PARTIAL**

I reach the same label as `phase3_synthesis.md`'s Combined Verdict, but by
my own charter-specific route, not by deference:

- **Leg (a)**: correctly downgraded to INCONCLUSIVE on the period-match
  (`R²=0.3697` sits at the *median*, not a tail, of its own circular-shift
  null — confirmed below). The surviving positive (`r=0.958` shape
  correlation) is real, but — from my seat specifically — it has never been
  checked for energy-consistency on its own terms: leg (a) is a lossless,
  boundary-free vacuum construction by design (Idealization 4), so nothing
  is owed there in absorbed-power terms, but nobody has yet asked whether
  its fringe *amplitude* (not just its *shape*) is consistent with a
  passive, energy-conserving redistribution of the source's own power
  around a tapered edge, as opposed to an amplitude that only matches after
  an implicit rescaling. Open, not yet a defect.
- **Leg (b)**: NO VERDICT stands, correctly, on Anchor 2 alone. But I
  independently re-read `leg_b_curve()` and found a problem with how this
  cycle's own energy argument (my prior instance's Phase-2 attack, adopted
  into Phase 3 as "Anchor 3") is framed — see §2.3. It doesn't reverse
  anything already decided, but it means Anchor 3 should not walk into
  Iteration 62 as currently worded.
- **Checkpoint criterion 4**: FIRES, correctly, on the record as filed —
  independently re-verified in §2.1.

Nothing here rises to PROMISING (no constraint-bearing mechanism result;
this is instrument-fidelity work, T1/Checkpoint-2 both N/A as the file
itself states) and nothing is RULED OUT (leg (a)'s shape-correlation is a
real, survives-scrutiny finding; leg (b) is an open instrument gap, not a
closed negative).

## 2. What I verified myself

### 2.1 The Checkpoint-4 chain (Iteration 59 → 60 → 61), independently traced

Read `LOGBOOK.md`'s Live-Thread-T28 narrative directly (not taking
`phase3_synthesis.md`'s summary on faith):

- **Iteration 59 (exp-082)**, Tier-0 reconciled ranking, item (2): *"EM's/
  THERMODYNAMICS' joint energy-interception cross-check (a tighter Poynting/
  interception bound on this cycle's own article-loaded geometry)"* —
  **first named here**, not run this cycle (a new item added to the board,
  not yet a deferral in the "should have run, didn't" sense).
- **Iteration 60 (exp-083)**, Phase-5 THERMODYNAMICS review flags it "now a
  **second consecutive deferred cycle**"; the reconciled Iteration-61
  ranking logs it explicitly: *"approaching but not yet at the R8-family
  tripwire — a third consecutive deferral without an explicit reason would
  fire it."* This is a real, written, forward-binding precommitment, not
  something Iteration 61 invented after the fact.
- **Iteration 61 (exp-084)**: `phase1_proposal.md` contains zero
  occurrences of "Poynting," "interception," or "cross-check" — confirmed
  by grep myself, matching both my own prior Phase-2 critique and Red
  Team's audit independently. No explicit deferral reason appears anywhere
  in Phase 1 or the five Phase-2 critiques. Phase 3 supplies reasoning only
  *after* Red Team's audit already flagged the firing, and explicitly
  declines to use that reasoning to avert the tripwire, calling a
  same-shift excuse "exactly the kind of after-the-fact rationalization...
  R8 exists to catch." That is the correct call, and it means the
  characterization **"third consecutive silent deferral"** is accurate as
  of the record that actually matters (Phase 1/Phase 2, before any
  post-hoc justification was possible) — not overstated, not understated.
  **Checkpoint criterion 4 firing is independently confirmed correct.**

### 2.2 Numbers reproduced from committed files (R4)

- `ptp_b = 0.08209591594490195`, reproduced bit-exact by re-importing
  `phase1_derivation.py` as a module and calling `leg_b_curve(mask_r_out=
  R_OUT)` directly — matches `derivation_results.json` to full float
  precision.
- `ptp_b / 0.002 = 41.05` — the "~41×" figure — arithmetically confirmed
  (this is the easy half of an R9 check; see §2.3 for the half that matters
  more).
- Read `leg_b_curve`'s actual masking line directly:
  `masked = np.where(rel <= mask_r_out, 0.0 + 0.0j, E1)` — the field is set
  to **exactly zero** inside the rim span, not attenuated or reflected.

### 2.3 A genuine, new finding: Anchor 3's two operands are not yet shown
commensurable (an R9-class gap, distinct from the one VISION already
cleared)

VISION's Phase-2 critique ran an "R9 commensurability" check and ruled it
clean — but that check covered only `rel_dev = |P_model−P_target|/P_target`
(degrees vs. degrees, the period-match arithmetic). It did not cover, and
was not asked to cover, the *separate* comparison my own prior-cycle
critique introduced: `ptp_b` (a Weber-contrast fringe amplitude) against
`R≤0.2%` (a power reflectance fraction). I checked this one myself, from
primitives:

- `leg_b_curve`'s output is `amb.weber(bo, bf)`, i.e.
  `C = (B_obj − B_flank)/B_flank`, where `B_obj`/`B_flank` are *local*
  window-averaged Poynting-flux (`Sx = −Re(E·conj(H))`) means **at the
  observation plane**, one relative to a nearby background flank. This is
  the same "C" metric used throughout the whole T28 sub-thread (`C40`,
  `C80`, `PAIR_PAD`, …) — a spatial fringe/interference contrast, not a
  global energy-conservation split.
- `R≤0.2%` is the coated absorber's own **global reflected-power / incident-
  power fraction**, established at a completely different measurement (the
  beam-behind/observer-return geometry of exp-001/002), not a Weber
  contrast at all.
- More importantly: the mask that produces `ptp_b` sets the field to
  **exactly zero** inside the rim — i.e. leg (b), as built, contains **no
  reflected term whatsoever**. It is a Kirchhoff perfect-absorbing-screen
  (total-block) diffraction calculation. EM's own blind Phase-2 critique
  independently noticed the same code fact for a different purpose
  (diagnosing Anchor 2's failure) — corroborating that this reading of the
  construction is correct, not a misreading on my part.

Putting these together: `ptp_b`'s size is a diffraction/shadowing fringe
amplitude from a **zero-reflectivity** construction. Comparing it against a
reflectance ceiling asks "is this too large to be a genuine partial
reflection?" of a model that was never computing a partial reflection in
the first place — a Weber-contrast fringe of several percent from
near-field shadowing of part of an aperture is not, on its own, evidence
that something exceeds an absorber's `R≤0.2%` budget, because nothing in
this construction claims to be measuring reflected power at all. **The
~41× number is real arithmetic on operands whose commensurability has not
been established — the harder half of an R9 check that VISION's own
"clean" ruling did not reach.**

This does **not** flip leg (b) back to any positive verdict — Anchor 2's
failure alone still disqualifies it, and I am not overriding that. But it
means **Anchor 3, as adopted in `phase3_synthesis.md` item 4 ("compare each
leg's predicted fringe amplitude against the established `R≤0.2%` ceiling"
as a standing requirement for any future leg-(b) attempt), needs to be
tightened before Iteration 62 inherits it as settled**: it is a meaningful
check only against a construction that actually contains a physically-
scaled reflected term — not against the current all-or-nothing opaque mask
— and its "operand B" should be produced by the *same* `weber`/
`window_means` pipeline that produces `ptp_b`, not borrowed wholesale from
a different geometry's own global reflectance measurement.

### 2.4 Everything else, spot-checked

- `corr(leg_a_curve, C80_real) = 0.958186` — independently reproducible in
  principle from the same committed arrays; I did not re-run the full
  31-point correlation myself but the figure is cross-confirmed three times
  in-record (Red Team's audit, VISION's independent route, Phase 3's own
  third re-run) and is not disputed by any seat, including mine.
- Red Team's circular-shift null (`15/30 = 50.0%` under the real
  `free_period_with_widening` pipeline) is the correct, harder-companion
  test and its use to downgrade leg (a) is sound; I have no energy-side
  objection to it.
- MATERIALS' "zero realizability content" framing is untouched by anything
  here — my own finding is about instrument bookkeeping, not materials.

## 3. Ranked top-3 candidate directions for Iteration 62+ (THERMODYNAMICS' vantage)

**1. Build the joint energy-interception cross-check as a genuine
partial-reflection variant of leg (b), not a bolt-on ratio.** Concretely
scoped, zero new FDTD: replace `leg_b_curve`'s opaque mask
(`E→0` inside the rim) with a physically-scaled partial reflection
(`E → r·E` inside the rim, `|r|² ≈ R_ceiling` from the already-established
`graded_black_shell` figure, or a genuine admittance-based `r(θ)` if one
exists for that boundary — reuse `ywas.reflection_coefficient_vec`/
`d80.reflection_coefficient_vec_realizable`, already-gated primitives from
exp-081), propagated through the *identical* `propagate`/`window_means`/
`weber` pipeline already in this file. This single build (a) discharges the
three-cycle-deferred Checkpoint-4 item with a real construction, not a
box-check, since it is scoped exactly as Iteration 59 originally intended
(a cross-check *on an article-loaded geometry*, using already-gated
reflectance primitives); (b) makes Anchor 3 commensurable by construction,
fixing §2.3's gap; (c) gives EM's obliquity/phase-convention fix (next
item) a second, physically meaningful construction to test against. This
is also a partial answer to the Director's own stated worry: the concern
in `phase3_synthesis.md` was against retrofitting this *into exp-084's own
scope under time pressure* — done properly as its own Iteration-62
proposal, that objection doesn't apply.

**2. Run EM's cheaper Anchor-2 diagnostic before crediting either causal
story, and before anything is built on top of a fixed leg (b).** My own
independent read of the code (§2.3) supports EM's phase-convention
hypothesis over the write-up's own "missing Rayleigh–Sommerfeld term"
guess: the ratio's documented non-smoothness (`1.47×`–`5.66×`, not a smooth
`cosθ`-type rescaling) is the signature of a missing complex/phase factor,
not a missing real geometric correction — and a construction whose stage-2
secondary sources are unweighted bare field values (as this one is) is
exactly the "field vs. current convention" bug species this bench has hit
four times before (`VALIDATION.md`). Cheap (re-weight one line, re-run the
convergence check), and it gates item 1: building a partial-reflector
construction on top of an unfixed two-stage composition bug would just
compound two errors.

**3. An energy-consistency check on leg (a)'s own surviving finding.**
Leg (a) is a passive, lossless, boundary-free construction by
Idealization 4 — no absorption anywhere. That means its fringe *shape*
(the `r=0.958` finding) and its fringe *amplitude* are both fully
determined by the source's own radiated power redistributing itself around
a tapered aperture edge; nothing has yet checked whether `ptp_a=2.02×10⁻²`
is the right *scale* for that redistribution (as opposed to `dg048`'s
already-validated machinery just happening to reproduce the right shape at
some other amplitude). A cheap, zero-FDTD check: does leg (a)'s own
predicted power imbalance between the object window and flank integrate,
over the full aperture, to something consistent with energy conservation
in a source with no absorbing elements at all (a Parseval/flux-closure
check on the already-computed `E`, `H` fields)? This is squarely a
THERMODYNAMICS-charter question or, better, a genuine sidecar item for
whichever seat leads Iteration 62, before the `r=0.958` result is
over-credited in a future cycle as "diffraction confirmed" rather than
"shape confirmed, amplitude untested."

---

*Full record consulted: `PANEL.md`, `LOGBOOK.md` (RULED OUT R1–R9,
Live Thread T28 in full, R10 as stated in `phase3_synthesis.md` — not yet
appended to `LOGBOOK.md` at the time of this review), `experiments/
084-t28-edge-diffraction-derivation/` in full (`phase1_proposal.md`
including the Phase-3 correction, `phase1_derivation.py`,
`phase1_output.txt`, `derivation_results.json`, all five Phase-2
critiques, `phase2_redteam_audit.md`, `phase3_synthesis.md`,
`phase3_fix_docket_checks.py`/`phase3_fix_docket_results.json`,
`NOTES.md`), plus `experiments/081-t28-photonics-construction-total-field/
photonics_construction.py` (`item3_energy_budget`) and `lab/ambient.py`
(`weber`, `window_means`) for the primitives independently exercised in
§2.3.*
