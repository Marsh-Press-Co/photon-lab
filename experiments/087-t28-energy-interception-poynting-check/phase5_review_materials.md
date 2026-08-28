# PHASE 5 — REVIEW · Panel Iteration 64 · exp-087 · Seat: MATERIALS & METAMATERIALS

## 0. Independent verification (before any interpretation)

**P8/NETD, re-derived from `results.json::thermo`, not trusted from
NOTES.md's prose.** All 6 `(cfg,θ)` cells read `netd_classification:
"UNDETECTABLE"`, `dt_ss_full_K` spanning `4.516×10⁻⁵`–`5.353×10⁻⁵` K
against the sourced NETD band `(0.020, 0.050)` K. Recomputing the margin
directly (`0.020/dt_ss`): `443×` (C40/36°) down to `374×` (G40/41.8°) —
matches NOTES.md's stated "≈374×–442×" to within rounding. **The
pre-committed triage rule (Phase 3 fix 6: check any P8 departure against
the ~780× Biot / ~116× H_CONV historical swings before reading it as new
physics) was correctly never invoked, because there was no departure to
triage** — confirmed from the primary array, not from the "confirmed"
language in NOTES.md's own Result section. This closes my own Phase-2
critique's sharpest attack cleanly: the compounding-uncertainty risk I
flagged (ASSUMED silicon identity × first-of-its-kind oblique
absorbed-power reading) never had occasion to bite, because P8 landed
exactly where ten-plus prior cycles' own flagship-absorber dispositions
already sit (T5/exp-043/exp-057, ~500×–27,000× margins) — this cycle adds
one more comfortably-UNDETECTABLE data point, not a load-bearing new
claim resting on the compounded uncertainty.

**`ratio_abs_ext` at oblique incidence, recomputed directly from
`results.json::widths` (`sigma_abs/sigma_ext` at `BOX_A`), independently
of the `thermo` block's own cached copy:**

| θ | C40 | G40 |
|---|---|---|
| 36.0° | 154.2247/300.7705 = **0.51277** | 154.4204/300.9797 = **0.51306** |
| 38.6° | 159.6461/310.9618 = **0.51340** | 160.0122/311.4915 = **0.51370** |
| 41.8° | 167.4754/325.9469 = **0.51381** | 168.0564/327.1633 = **0.51368** |

All six cells reproduce the `thermo` block's `ratio_abs_ext_raw` field
exactly. Against T9's established broadside anchor (σ_abs/σ_ext = 0.51,
`sigma_ext_cells≈240`, ESTABLISHED section, LOGBOOK.md): every oblique
cell sits **within 0.55%–0.75% of the broadside figure**, all on the
high side, all six cells agreeing with each other to <0.2% despite
spanning a 6° incidence range and two different PAD geometries. This is
**not materially different from 0.51** by any standard this program has
ever applied (compare to T10's own ~7% "survives resolution" precedent,
or R3's historical bar) — it is a clean, first-ever confirmation that the
near-field extinction-paradox ratio T9/T8 established at broadside (0.51
exceeding the idealized ≤0.5 geometric-optics ceiling, read as a
near-field-limited measurement at this bench's own box geometry, not an
asymptotic material constant) **is robust across 36°–42° oblique
incidence for this article**, at this same near-field box scale. The
"genuine uncertainty" P4's own context section named — "whether 36–42°
oblique incidence on a circularly-graded, rotationally-symmetric absorber
departs materially from the broadside figure" — is now answered, cleanly,
in the unremarkable direction: **it does not depart materially.** This is
a small, real, disclosed materials/photonics finding this cycle produced
essentially for free (P4's own context leg, never separately ranked) and
it should be logged against T9, not left buried in a raw-data table.

## 1. The central question: does ENERGY-DOMINANT carry any realizability content?

**No. Idealization 10 stands, unmodified, after this result.** Working
through the physics rather than asserting the conclusion:

`p_abs` at each `(cfg,θ)` cell is the power a real, ordinary, broadband,
non-resonant graded-loss medium (`graded_black_shell`, published-tier,
Vantablack/CNT-forest analog, unchanged and already scored since
Iteration 24) absorbs from whatever total field actually reaches it.
`delta_scene`/`C_empty` is a background-subtracted, near-field Weber
contrast at one observation window. **Both are quadratic-in-field
functionals of the identical underlying total field** — direct incident
beam plus the small, coherent, PAD-geometry-dependent perturbation this
sub-thread has spent ten-plus cycles characterizing (exp-076's own
proof: the `ABSORB=40` boundary's reflectance MAGNITUDE is bit-identical
between `C40`/`G40` by construction; only a propagation-phase/round-trip-
timing effect can differ). If the PAD geometry perturbs the total field
illuminating the object by some small, coherent, θ-dependent fraction,
**every quadratic-in-field functional of that same field — the ambient
Weber contrast at the observation plane, and the absorbed power at the
object — should be expected to show comparable-order-of-magnitude
fractional sensitivity to it**, precisely because they are both reading
out the same perturbed field, not because the absorber has acquired any
new or unusual property. A `ratio_k` of order unity (the 2.64/5.71 CONSISTENT
reading at the two angles clear of the θ=38.6° node artifact) is the
generic, unsurprising outcome of this shared-field picture; it would take
a specific reason for the two functionals to be DEcoupled (e.g. the
absorbed-power channel being dominated by a large, PAD-insensitive DC term
that swamps the coherent perturbation, which is what this cycle's own
pre-registered prediction assumed and which the data now show is not the
case at two of three angles). Read this way, ENERGY-DOMINANT is a genuine
correction to this sub-thread's own EM/THERMO energy bookkeeping — it
means the PAD confound's "provably lossless" boundary-reflectance proof
(exp-076) does not, by itself, guarantee the confound is energy-inert once
a real absorbing article sits in the perturbed field's path — but it says
nothing new about what MATERIAL properties are required, because the
mechanism that explains it (ordinary linear-medium response to an
externally-imposed field perturbation) requires no special material
behavior at all. This is exactly the distinction Iteration 59's own
standing framing rule drew for the parent confound ("this whole confound
is a pure scene/domain-geometry fact, no material implicated") and this
cycle's own energy reading is fully consistent with that rule, not an
exception to it.

**On the specific mechanism named in my task brief** — does
grazing-angle-dependent effective absorption path length in the graded
shell plausibly couple to the same boundary/diffraction structure that
produces `delta_scene`'s own oscillation? **Not as a shared-origin
mechanism, and this distinction matters.** `graded_black_shell` has no
periodic microstructure at the ~2.8°-in-θ_beam angular scale this
program's whole T28 sub-thread has been chasing — it is a smooth,
monotonic, radially-graded σ(r) profile with no resonant or periodic
structure that could itself generate a ~2.8°-period signal. The shell
cannot be the SOURCE of the oscillation seen in `frac_p_abs(θ)`; at most
it is a passive TRANSDUCER, converting whatever periodicity already
exists in the illuminating field (from the domain-scale echo/diffraction
structure T28 has spent thirteen cycles trying to identify) into a
proportional modulation of its own absorbed power. A genuinely
grazing-angle-dependent absorption EFFICIENCY (secant-law path-length
lengthening as `θ_beam` increases) is real materials physics and would
produce a smooth, monotonic η_abs(θ) — consistent with the smooth,
near-constant `ratio_abs_ext` trend across 36°→41.8° I verified above
(0.51277→0.51381, a mild monotonic drift, no oscillation) — but that
smooth trend is a different, much lower-frequency phenomenon from the
~2.8° oscillation `PAIR_PAD`'s own `frac_p_abs` inherits from `delta_scene`.
**The correct reading, and the one this cycle's own data support, is:
the absorber's smooth angular response and the sharp domain-diffraction
oscillation are two independent, superposed effects on the same measured
quantity — the shell does not manufacture or resonantly amplify the
oscillation, it merely fails to filter it out.** This is the single
cheapest, highest-value confirming test available for Iteration 65 (§3,
below): compute `p_abs(C40,θ)` alone across the existing dense 31-point
grid (`sigma_abs` at `BOX_A`, zero new FDTD if exp-083's own captures are
re-loadable, otherwise ~31 cheap calls) and check it is smooth/monotonic
with no ~2.8° structure of its own — if true, that is the clean,
falsifiable confirmation of "passive transducer, not resonant source,"
closing this question with a real number rather than the physical
argument above.

## 2. Verdict on this cycle's Combined Verdict contribution

**Support-with-changes → support, no further changes needed.** P7's
FALSIFIED/ENERGY-DOMINANT classification is honestly and correctly
reported, the θ=38.6° node-artifact candidate explanation is disclosed
(not adopted) exactly as it should be, and the "does not rescue the
prediction even if fully credited" framing (the two clean angles alone
land CONSISTENT, not ENERGY-DECOUPLED) is the right, conservative reading.
My own Phase-2 sharpest attack is discharged by the data, not merely
argued away: P8 never departed from UNDETECTABLE, so the compounding-
uncertainty risk I named never became load-bearing. **From my seat
specifically: Idealization 10 ("bears only on T28's own confound-mechanism
question... does not re-open REALIZABILITY_MEMO.md's verdict") is
verified, not merely asserted, by this cycle's result** — the mechanism
that explains ENERGY-DOMINANT requires nothing beyond ordinary linear
passive-medium response to a domain-geometry-driven field perturbation,
touches no σ(I)/RSA/TPA/FCA tier, and the article itself (published-tier)
is unchanged. **Checkpoint criterion 2: N/A, confirmed** — this is
instrument/confound bookkeeping internal to T28's own sub-thread, not a
phenomenon-mechanism claim; nothing here bears on any constraint.
**No realizability tier moves.**

One disclosed-but-real residual concern, forward not blocking: the
`ratio_k` decade-scale tiers (Idealization 6) are explicitly a wide,
unrigorous first-of-its-kind band, and `θ=38.6°`'s own `ratio_k=53.99`
outlier — even though it does not decide the classification once the two
clean angles alone already land CONSISTENT — was large enough to trip the
`ENERGY-DOMINANT` outright-override rule on its own. A future extension
of this instrument to more angles should report whether the override rule
itself is well-conditioned near a `frac_contrast` zero-crossing, not only
disclose the individual outlier as this cycle correctly did.

## 3. Ranked candidate directions for Iteration 65 (MATERIALS' own vantage)

1. **(Highest value, cheapest)** Compute `sigma_abs(C40,θ)`/`sigma_abs(G40,θ)`
   individually (not just their PAD-difference) across the existing
   31-point dense window, and test whether each series alone is smooth
   (no ~2.8° structure) while their difference reproduces the oscillation —
   the direct, falsifiable test of §1's "passive transducer, not resonant
   source" reading. Zero new FDTD if exp-083's captures are re-loadable
   from disk; otherwise ≤31 cheap calls, reusing this cycle's own
   `sc.widths()`/`BOX_A` machinery verbatim.
2. **Extend this cycle's energy-interception measurement to the near-null
   σ(I) article** (`off_pass`, τ_off≈0.0065) — the article class that
   actually matters for constraint-3 realizability, unlike the flagship
   absorber (τ≈3.9) this cycle correctly scoped as a T28 confound-
   diagnostic geometry only. A weakly-absorbing σ(I) OFF-state article
   sits in a very different regime (much smaller absorbed-power baseline,
   possibly a different `ratio_k` order) — if a future σ(I) proposal ever
   needs this exact bookkeeping, better to know now whether ENERGY-
   DOMINANT-scale coupling is a flagship-absorber-specific finding or
   generalizes to weak absorbers, before it becomes load-bearing on an
   actual mechanism claim.
3. **Log the oblique-incidence `ratio_abs_ext≈0.513–0.514` confirmation
   against T9's LOGBOOK entry** (§0, above) — a genuine, first-ever,
   essentially free data point closing a previously-flagged "genuine
   uncertainty," should not be left buried in this cycle's raw
   `results.json` table.
4. **Not mine to re-rank, but still overdue**: PHOTONICS' grazing-incidence
   validity check on `edge_diffraction_c_empty_corrected` (near-unanimous
   #1 across six of seven seats at Iteration 64's own close) and the
   x-wall wavelength-generality leg (11+ consecutive cycles deferred) — both
   stand ahead of my own items 1–2 above on the program's own priority
   ordering; I list mine as MATERIALS-charter-relevant additions to that
   board, not replacements for it.
