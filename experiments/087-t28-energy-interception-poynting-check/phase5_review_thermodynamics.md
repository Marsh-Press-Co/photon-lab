# PHASE 5 — REVIEW · Seat: THERMODYNAMICS · Panel Iteration 64 · exp-087

Fresh sub-agent, no memory of writing Phase 1 (this cycle's lead seat was
THERMODYNAMICS by rotation, but that instance is finished; this review
holds its own proposal's actual outcome to the same standard as anyone
else's).

## 1. Was the tripwire genuinely discharged with real FDTD work?

Independently checked, not trusted from NOTES.md's prose:

- `results.json::total_new_fdtd_calls = 13`, and `run_output.txt` lists
  13 distinct `one_call` dispatches (lines "[ 1/13]"–"[13/13]"), spanning
  both configs (`C40`/`G40`), all 3 angles, both legs (empty/article), plus
  one `STEPS=1400` settling-check call — total wall time 115.7s. This is
  not a desk rehash: `sigma_abs`/`sigma_ext`/`sigma_scat` differ
  meaningfully cell-to-cell (e.g. `sigma_ext` ranges 300.7–327.2 across
  angle and config, tracking the expected oblique-incidence trend), and
  `sigma_abs<0` was found at every cell on the first run — a genuine,
  previously-unexercised sign-convention bug (`i_inc` is a signed +x flux;
  `PAIR_PAD` propagates in −x, the first `widths()` caller to do so),
  traced to source and fixed by a caller-side wrapper with zero `lab/`
  diff (confirmed: the wrapper lives in `run.py`, not `lab/sections.py`).
  A fabricated or lightly-massaged desk exercise does not produce this
  shape of failure-then-fix. **Call-count claim confirmed correct**, and
  the "13, not 14" correction in NOTES.md is itself accurate (the settling
  spot-check reuses the main sweep's already-captured empty leg, needing
  only one extra call, not two).
- The 12 main-sweep FDTD calls plus 1 settling call is a genuine
  **article-loaded, purpose-built scene** — the same `PAIR_PAD` C40/G40
  geometry validated in exp-082/083, with `sections.widths()` (previously
  stage-8-gated but never run on this geometry, at oblique incidence, on
  `graded_black_shell`) applied for the first time. This matches the
  tripwire's own literal condition (below), not a thin substitute for it.

**Verdict: yes, this is a real, purpose-built FDTD measurement, not a
fifth deferral in disguise.**

## 2. The tripwire's literal text, re-read from LOGBOOK.md myself

Located at Iteration 63 (exp-086's own Phase-5 final audit, LOGBOOK.md
line ~4273–4278), quoted verbatim:

> "now FOUR consecutive cycles deferred/exempt (083–086), SEVEN since
> first named (Iteration 59) — **a fifth consecutive deferral without
> either building a purpose-built scene or explicitly retiring the
> "next scene-bearing cycle" framing fires Checkpoint criterion 4
> automatically**, pre-announced now on the R11 precedent."

Read on my own terms, independent of Red Team's Phase-2 audit for exp-087:
the condition is disjunctive over **process** ("building... or explicitly
retiring the framing"), with no clause anywhere conditioning on which
classification the measurement returns. **Red Team's reading (exp-087
`phase2_redteam_audit.md` §1b) is accurate** — I confirm it independently
from the source text, not by deference.

## 3. Independent judgment: does discharging it this way satisfy the
tripwire's *intent*, given P7 (PRIMARY) was falsified?

Yes — and I judge the falsification makes this a *more* credible
discharge than a confirming result would have been, for a reason worth
stating plainly: the tripwire exists because this cross-check had been
silently skipped four times running (LOGBOOK Iteration 60/61/63's own
"silent/thin-result shape" language). The failure mode the tripwire polices
is a program quietly avoiding a measurement that might embarrass its own
prior. THERMODYNAMICS (the lead seat, now finished, with no stake in this
review) pre-registered ENERGY-DECOUPLED at ≥2/3 angles with only
"moderate confidence," built the instrument, ran it, and got contradicted —
CONSISTENT at the two aliasing-clean angles and ENERGY-DOMINANT overall.
Reporting that outcome honestly (not massaging the classification, not
quietly re-scoping "decoupled" after the fact — checked below) is exactly
the behavior the tripwire is meant to produce. A cycle that discharges a
tripwire by predicting X and finding X is cheap to fake; a cycle that
predicts X, builds the real instrument, and reports not-X against its own
lead seat's own hypothesis is hard to fake. **Both the letter and the
intent are satisfied. No sixth-deferral concern from this seat.**

## 4. Independent end-to-end recomputation of `netd_disposition` (P8)

Fed the *committed* `results.json::widths` σ_ext/σ_abs (BOX_A) through
`ts.absorbed_power_established_ratio` → `ts.mixed_length_scale_regime` →
`ts.netd_disposition` myself, using the frozen constants from `run.py`
(§Frozen configuration), for all 6 (cfg,θ) cells (2 shown in full, all 6
cross-checked):

| cfg,θ | p_abs_w (recomputed) | dt_ss_full_K (recomputed) | NETD margin (0.020K/dt_ss) | class |
|---|---|---|---|---|
| C40, 36.0° | 2.748814e-12 | 4.516013e-05 | **442.87×** | UNDETECTABLE |
| C40, 38.6° | 2.941857e-12 | 4.833163e-05 | 413.81× | UNDETECTABLE |
| C40, 41.8° | 3.234850e-12 | 5.314518e-05 | 376.33× | UNDETECTABLE |
| G40, 36.0° | 2.754216e-12 | 4.524889e-05 | 442.00× | UNDETECTABLE |
| G40, 38.6° | 2.953626e-12 | 4.852498e-05 | 412.16× | UNDETECTABLE |
| G40, 41.8° | 3.258186e-12 | 5.352858e-05 | **373.63×** | UNDETECTABLE |

Every recomputed value is **bit-identical** to `results.json::thermo`
(confirmed programmatically, not eyeballed). The margin range is
373.63×–442.87×, matching NOTES.md's stated "≈374×–442×" exactly (373.63
rounds to 374). **P8's UNDETECTABLE classification and margin claim are
confirmed, independently, end-to-end.**

## 5. Was fix 6's triage rule correctly judged inapplicable?

**Yes — and more strongly than the record currently states.** I checked
`lab/thermo_sidecar.py::absorbed_power_established_ratio` directly: its
signature is `(i_incident_w_cm2, sigma_ext_cells, dx_m, ratio_abs_ext)` —
it takes **no thermal material constant at all**. The silicon
`(ρ, c_p)`/emissivity/`k_air` identity that fix 6's triage rule (~780×
Biot, ~116× H_CONV) is about enters the chain only downstream, in
`mixed_length_scale_regime`, which converts an already-computed `p_abs_w`
into `dt_ss_full_K` (feeding P8/NETD only). **`p_abs_w` itself — and
therefore `frac_p_abs(θ)`, `ratio_k(θ)`, and the entire PRIMARY P7
classification — is a pure function of this cycle's real FDTD
`sigma_ext`/`ratio_abs_ext` measurement and has zero dependence on the
ASSUMED silicon constants.** So:

- Fix 6's triage rule is correctly inapplicable on its stated literal
  ground (nothing departed from UNDETECTABLE, confirmed above).
- It is *also* structurally inapplicable to the falsified PRIMARY metric
  for a reason no document in this cycle's record states explicitly: P7's
  ENERGY-DOMINANT/CONSISTENT finding cannot be an artifact of the
  ASSUMED-material-constant compounding gap MATERIALS flagged in Phase 2,
  because that gap doesn't reach P7's inputs at all. This is a genuine
  reassurance about the falsification's robustness that is worth adding
  to the permanent record, not merely inferred.

## 6. Is there a smaller-scale flip risk *within* the UNDETECTABLE band that
bears on the PRIMARY metric?

Checked the noise-floor gate's own margin, not just its pass/fail bit —
`resolved(θ) = |p_g40−p_c40| > 3×box_dev_max×p_c40`:

| θ | \|Δp_abs\| | noise floor (3×box_dev_max×p_c40) | margin over floor |
|---|---|---|---|
| 36.0° | 5.403e-15 | 1.691e-15 | 3.20× |
| 38.6° | 1.177e-14 | 2.623e-15 | 4.49× |
| 41.8° | 2.334e-14 | 2.188e-15 | 10.67× |

All 3 angles clear the pre-committed noise floor with real margin (worst
case 3.2×, not a coin-flip near 1×) — `box_dev` itself is tiny (0.005%–
0.03%, well inside the `xi_ext≤0.12` tolerance the geometry was gated
against). **Resolved=True at all 3 angles is a legitimate call, not a
borderline one riding the noise-floor definition.** This is the correct
place to have looked for a flip risk (measurement noise), and it clears;
the material-constant swing (fix 6) was never the right axis to check
against P7 in the first place (§5).

I also independently re-verified the θ=38.6° zero-crossing explanation
from `experiments/083-.../results.json::per_theta` directly (not trusted
from NOTES.md): `delta_scene` values around that angle are
`37.6°:+1.587e-3, 38.0°:+1.923e-3, 38.4°:+8.08e-4, 38.6°:-4.15e-5,
38.8°:-8.57e-4, 39.2°:-1.829e-3` — confirmed, the curve crosses zero
almost exactly at 38.6°, inflating `ratio_k` there via a small denominator,
independent of the article's real physics. **But this does not rescue the
prediction**: excluding 38.6° as an artifact, the remaining two angles
(36.0°: ratio_k=2.64; 41.8°: ratio_k=5.71) are squarely **CONSISTENT**
(0.1–10), not the predicted **ENERGY-DECOUPLED** (<0.1). Under either
reading — include 38.6° (ENERGY-DOMINANT, by the pre-registered any-X
priority) or exclude it (CONSISTENT) — **the prediction is falsified
either way.** This is a robust falsification, not an artifact of one
outlier point, and Phase 5 should not let the (real, verified) zero-
crossing explanation for 38.6° specifically be misread as rescuing the
overall finding.

## 7. New energy-accounting question: does the ENERGY-DOMINANT swing carry
its own re-radiation/detectability consequence beyond what P8 checked?

This is the one substantive gap I found in the record. P8 computes
`netd_disposition` from each config's own **absolute** `p_abs_w` at
`BOX_A` — it never recomputes detectability for the **differential**
quantity (`|p_g40(θ)−p_c40(θ)|`) that P7's own `frac_p_abs` is built from,
even though that differential is the physically real thing test P7 to be
"energy-dominant" about. I ran this check myself, feeding the swing
directly through `mixed_length_scale_regime`/`netd_disposition` (same
constants, same `l_geometric_m`):

| θ | swing \|Δp_abs\| (W) | dt_ss from swing (K) | NETD margin | class |
|---|---|---|---|---|
| 36.0° | 5.403e-15 | 8.876e-08 | ~2.25×10⁵× | UNDETECTABLE |
| 38.6° | 1.177e-14 | 1.934e-07 | ~1.03×10⁵× | UNDETECTABLE |
| 41.8° | 2.334e-14 | 3.834e-07 | ~5.22×10⁴× | UNDETECTABLE |

**Answer: no new detectability concern.** The differential/swing signal
is *even further* from the NETD band than P8's already-comfortable
absolute-power margins (52,000×–225,000× vs. 374×–443×) — unsurprising
once stated (the swing is only 0.2–0.7% of an already-tiny absolute
power), but it was not previously computed anywhere in this cycle's
record, and "ENERGY-DOMINANT relative to Weber contrast" could otherwise
be misread by a future reader as implying some new re-radiation channel.
It does not. **Recommend this swing-specific recomputation be added as a
committed, named check** (not left to a future reviewer's independent
derivation, as happened here) if this sub-thread continues — it costs
zero additional FDTD calls, reusing already-captured data exactly as P8
does.

## 8. Supplementary check (own initiative): sensitivity of P7's numeric
value — not just its classification — to Idealization 3 (`iso_xsec_sq`)

Not asked directly, but squarely inside THERMODYNAMICS' charter (owns the
sidecar and its idealizations) and directly touches the falsified PRIMARY
metric, so I checked it. `absorbed_power_established_ratio`'s
`iso_xsec_sq` convention makes `p_abs_w ∝ sigma_ext²`; since `sigma_ext`
differs by only ~0.07%–0.37% between G40 and C40, squaring roughly
doubles the resulting fractional swing versus a hypothetical linear
(infinite-rod) convention. Recomputed `frac_p_abs`/`ratio_k` under a
linear convention: 36.0°→1.71, 38.6°→30.95, 41.8°→2.75 (vs. the actual
2.64/53.99/5.71). **The classification is unchanged** (38.6° still >10,
36.0°/41.8° still inside CONSISTENT) — the falsification is robust to
this idealization — **but the numeric value of `ratio_k` is convention-
dependent by roughly a factor of ~1.5–2×**, a sensitivity Idealization 3's
existing one-line disclosure does not quantify. Worth a line in a future
citation of this cycle's exact `ratio_k` numbers, though it does not
change today's classification or falsification verdict.

## Verdict on this cycle's Combined Verdict contribution

**From THERMODYNAMICS: PARTIAL, and this seat votes to credit the
tripwire discharge as genuine and honestly reported.** Specifically:

- Tripwire discharge: **genuine**, both letter and intent (§§1–3).
- P8/detectability bookkeeping: **independently re-verified end-to-end,
  confirmed correct** (§4), and now extended with a swing-specific check
  that closes the one gap I found (§7) — the answer to that gap is
  reassuring (no new detectability consequence), so the energy-ledger's
  bookkeeping *is* honestly closed on the detectability axis specifically.
- P7 (PRIMARY): **genuinely falsified**, robustly (§6), not an artifact of
  noise-floor marginality, material-constant compounding (§5), or the
  θ=38.6° zero-crossing point alone (§6). This is real, new, and
  contradicts ten-plus cycles' phase/interference-only prior at the two
  cleanest angles. **This is the one thing Iteration 65 must not let
  quietly evaporate** — it is a materially new finding about T28's own
  confound mechanism, not a footnote to a successful tripwire discharge.

No Checkpoint-criterion-4 concern from this seat; no unfalsifiable claim;
no quiet constraint-3 overclaim found (Idealization 10's affirmative
scope language was carried inline correctly everywhere I checked it in
NOTES.md and run.py's own `scope_note`/`netd_disclaimer` fields).

## Ranked candidate directions for Iteration 65 (THERMODYNAMICS' own vantage)

1. **Investigate the CONSISTENT/ENERGY-DOMINANT finding itself, not just
   its instrument.** At the two aliasing-clean angles (36.0°, 41.8°), bulk
   absorbed-power PAD-sensitivity and localized Weber-contrast
   PAD-sensitivity are comparable in fractional magnitude (ratio_k 2.6–
   5.7) — genuinely surprising against ten-plus cycles of phase/
   interference-only evidence. Densify the angle sampling across more of
   the established 31-point window (avoiding the ~2.84–2.95° aliasing
   band this cycle already mapped) to see whether CONSISTENT holds broadly
   or was itself a 2-point fluke, and open a mechanism question: what
   physical channel would make bulk absorbed power and localized contrast
   co-vary at this magnitude if they are not the same underlying effect?
2. **Formalize the swing-specific NETD recomputation (§7) as a named,
   committed check**, not an ad hoc post-hoc derivation — zero marginal
   FDTD cost, closes a real gap in what P8 currently reports, and directly
   forecloses a plausible misreading of "ENERGY-DOMINANT" as implying a
   new re-radiation channel.
3. **Re-run P7 with θ=38.6° explicitly flagged/excluded as a known
   node-adjacent point, plus 1–2 additional clean angles**, to test
   whether CONSISTENT survives on more than 2 data points — the current
   falsification is real and robust to the specific artifact found, but
   rests on a thin n=2 "clean" sample for a finding this consequential.
4. **Quantify the `iso_xsec_sq`-vs-rod-convention sensitivity (§8) as a
   standing, citable number** wherever this cycle's exact `ratio_k` values
   are next quoted, so a future cycle does not treat 53.99 or 2.64 as
   convention-independent facts.

## Files consulted (all read/executed directly, not summarized secondhand)

- `/home/user/photon-lab/PANEL.md`, `/home/user/photon-lab/LOGBOOK.md`
  (targeted full-context reads at the T28 live-thread history, Iteration
  59–63 energy-interception naming/tripwire entries, RULED OUT registry
  index)
- `/home/user/photon-lab/experiments/087-t28-energy-interception-poynting-check/`
  `phase1_proposal.md`, `phase2_critique_materials.md`,
  `phase2_redteam_audit.md`, `phase3_synthesis.md`, `NOTES.md`, `run.py`,
  `results.json`, `run_output.txt`
- `/home/user/photon-lab/lab/thermo_sidecar.py` (read directly;
  `absorbed_power_established_ratio`/`mixed_length_scale_regime`/
  `netd_disposition` invoked directly against committed `results.json`
  data for independent recomputation)
- `/home/user/photon-lab/experiments/083-t28-pad-article-full-power-retest/results.json`
  (read directly for the θ=38.6° zero-crossing verification)
