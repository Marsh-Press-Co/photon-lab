# PHASE 5 — REVIEW · PHOTONICS · Panel Iteration 84 (exp-107)

*Fresh context. Charter: is the proposal's optical response coherent as
stated, across wavelength and angle? Read: LOGBOOK.md in full (RULED OUT
R1–R24, ESTABLISHED, LIVE THREADS incl. T9/T28's full history, Iterations
76–83 in full), PANEL.md, PLAN.md's Current state, exp-106's NOTES.md, and
the full exp-107 record (`phase1_proposal.md`, all five Phase-2 critiques,
`phase2_redteam_audit.md`, `NOTES.md`, `results.json`, `run.py`,
`chunk_runner.py`, `finalize.py`, `run_output.txt`).*

## Independent number checks (from `results.json` raw fields)

1. **`delta_abs_ext_ratio`, r=156**: `abs_ext_ratio_pec_cored_exp106
   (0.4992167630142016) − abs_ext_ratio_hollow (0.49918707730729867) =
   2.96857×10⁻⁵`, matching the filed `-2.96857069029266e-05` (sign flipped
   because the file stores hollow−PEC). Reproduces exactly.
2. **`floor_gate_article_numerator`, r=312**: `floor = 0.10 × rms =
   0.10 × 7.213132466394405e-05 = 7.213132466394405e-06`, matches exactly.
   `frac_unresolved = 1070/4000 = 0.2675`, matches exactly.
3. **Item 3 margin, `(fixedabs, r=312)`**: `margin = NETD_BAND_K[0]/dt_ss
   = 0.020 / 1.7026593096860568e-4 = 117.46`, matches the filed
   `117.46331098784337` and the narrated `117.5×`/`117.463×`.

All three independently re-derive bit-exact or to stated precision. No
arithmetic defect found in the numbers themselves.

## Steel-man

This cycle does the historically hard thing correctly: it declines to
spend ~4h of cpl=50 FDTD on a census whose own Phase-2 layer proved could
not execute its own mandatory gate (G0's domain is empty over any
reasonably-sized window of a periodic signal whose own half-period sizes
the exclusion buffer — a genuinely structural, not local, defect), and
retires `delta_scene` R3-vs-R4-vs-R5 by citing an already-exhaustive,
zero-cost written disposition (`disposition_memo.md`) instead. That is the
scientifically correct call, not merely the cheap one, and the Tier-1
`kappa_window` closeouts are honestly, un-smoothed reported: Item 3 uses
real per-family `sigma_ext(r)` for the first time (not a placeholder) and
narrates the fragile `(fixedabs,312)≈117×` cell inline, discharging R21;
Item 4 surfaces a genuinely new, unanticipated finding (18–27% numerator
floor-gate contamination) rather than being buried in a clean-looking
aggregate; Item 1 is explicitly scored PASS-but-not-CONFIRMS rather than
rounded up. Gate P0 is exact at both r. The disclosed substitution (hollow,
not PEC-cored, article for item 4) is stated plainly, not hidden.

## Sharpest attack

**The Result section's own "roughly an order of magnitude above the T9
anchors" characterization rests on an uncaught R9-class commensurability
defect — mixing two anchors LOGBOOK's own T9 entry explicitly says are
different measurement channels.** `exp-027`'s `+1.56×10⁻⁶` is
`Δ(σ_abs/σ_ext)` measured via `sections.widths()` — the *same* channel
this cycle's own item 1 uses. `exp-031`'s `6.8×10⁻⁶` is, per LOGBOOK's own
T9 entry verbatim, "a completely different measurement channel
(single-angle ambient contrast, not radial or box-ledger absorbed
power)" — a dimensionless Weber-contrast delta, not an absorption/
extinction cross-section-ratio delta. NOTES.md's Predictions table and
Result section both cite these two side by side as "the T9-established
near-zero order" without flagging that difference — the exact shape R9
(RULED OUT registry) exists to catch: two operands of nominally the same
signal, normalized/measured differently, treated as interchangeable.

Correctly comparing only against the like-for-like anchor (exp-027,
1.56×10⁻⁶): this cycle's measured deltas are **19.0×** (r=156,
`2.969×10⁻⁵/1.56×10⁻⁶`) and **15.8×** (r=312, `2.468×10⁻⁵/1.56×10⁻⁶`)
larger — a genuine ~15–20× gap, over 1.2 decades, not the "~order of
magnitude" (~10×, ~1 decade) the prose states. Blending in the
wrong-channel exp-031 figure pulls the naive "gap" down toward ~4×,
materially prettying up how far this generalization sits from the
original T9 anchor. This does not, on the numbers as filed, reverse
the qualitative conclusion (both deltas remain 2–3 orders of magnitude
below the `abs_ext_ratio` values themselves, ~0.49–0.50) — but it means
the "same near-zero order of magnitude" framing understates a real,
consistent, and specifically-directioned widening of the gap as
`R_CORE/R_COAT` moves past T9's only-validated 0.385 anchor, and the
`≤2×10⁻⁵` "confirms" threshold itself was never independently
re-derived (an R17-shaped gap) from the correct single-channel anchor.

**Second, deeper gap: `core_frac≈10⁻⁷` is being used to argue the whole
core-presence question is negligible, but it only rules out a
spatially-concentrated absorption mechanism, not a phase-mediated
interference contribution to `σ_ext`.** `radial_absorbed_power`'s
`core_frac` measures what fraction of *absorbed power* lands inside
`r<R_CORE` — a real, valid check that no measurable heating occurs there
(and it is genuinely clean, ~10⁻⁷, at both r). But `sections.widths()`'s
`sigma_ext` is derived from the **optical theorem** — a forward-scattered
*field-phase* interference construction — not a power-deposition
integral. A PEC boundary at the core can imprint a coherent phase
footprint on the tiny residual field reaching it and reflect it back
through the shell (a genuine, physically expected difference: PEC
enforces `Ez=0` exactly, hollow leaves that region vacuum with no
boundary reflection at all) without depositing any detectable power
there — exactly the "Poynting-flux integral discards phase" distinction
this program's own record already drew at Iteration 78 (exp-101's own
Prediction-3 finding). `core_frac≈10⁻⁷` and `delta_abs_ext_ratio`
answer two different physical questions; the former cannot certify the
latter is noise rather than a real (if tiny) interference effect.

A related, physics-grounded observation that argues *against* the
specific "grows with `R_CORE/R_COAT`" mechanism the task brief raises,
worth stating explicitly since the data bear on it directly: the
fixed-abs family holds `tau_shell=24.0` **exactly** identical at every r
(`ABS_THICKNESS=48` cells and `sigma_max=0.5` both fixed) — so the
residual field amplitude reaching the core (`∝exp(−tau_shell)`) is
essentially unchanged between r=156 and r=312 regardless of
`R_CORE/R_COAT`. A genuine core-reflection/interference effect driven by
that residual field should therefore track `tau_shell` (constant here),
not `R_CORE/R_COAT` — and indeed the measured delta does **not** grow
with the ratio: `2.969×10⁻⁵` at ratio 0.692 (r=156) vs. a *smaller*
`2.468×10⁻⁵` at ratio 0.846 (r=312), the opposite direction from a
naive "more core exposure ⇒ more leakage" story. This is consistent
with either a small, roughly-tau-set real coupling effect (comparable
order at both r, since tau is unchanged) or numerical noise of similar
character (box_dev also shrinks with r, 0.00071→0.00022) — two points
cannot discriminate them, and the document does not attempt to.

## On Item 4's hollow-vs-PEC-cored scope caveat

NOTES.md's own disclosure — "not expected to depend materially... since
both scenes attenuate through the same shell; neither the hollow core nor
a PEC core meaningfully re-radiates power back into the window" — has a
real physical basis (the window is downstream of a `tau_shell=24` shell,
so the *dominant* suppression is identical between constructions) but
overstates its own certainty for the specific statistic at risk.
`frac_unresolved` (18–27%) is a **threshold/counting statistic operating
exactly in the noise-floor-adjacent regime** where a small coherent
perturbation — however power-negligible per `core_frac` — could shift
individual cells across the pass/fail line, the same fragility this
program's own R13/R14 lineage exists to flag for ratio/threshold
constructions built near a marginal boundary. The caveat should be stated
as a plausible hypothesis pending direct measurement, not as a
near-certainty — which NOTES.md's own Next item 1 (checking the numerator
floor-gate on the actual PEC-cored primary article) already correctly
proposes to resolve. I support that ranking.

## Wavelength/angle scope check

Correctly confirmed: no new wavelength or angle claim this cycle. λ=600nm
only throughout (Item 1/3/4 all reuse exp-106's own 600nm-only
`kappa_window` bridge); the `kappa_window` items are normal-incidence
(θ=0°) only, unchanged from exp-102–106; the retired census would have
been 600nm-only as well. The 750/450nm leg and the oblique-angle extension
remain correctly named as still-open, untouched items, not silently
dropped.

## Verdict: **CONFIRM-WITH-GAPS**

The retirement decision, the independent-reproduction numbers, and the
honest PASS-not-CONFIRMS/FALSIFIED framing are all sound and correctly
computed — nothing here reverses `item1_pass`, the r=156
`frac_unresolved` FALSIFICATION, or the Tier-0 retirement. But the
Result section's own optical-response narrative carries two real,
uncaught defects from this seat's discipline: an R9-shaped
commensurability error (blending a same-channel and a
different-channel "T9 anchor" to understate a genuine ~15–20× gap as
"~an order of magnitude"), and a category error (treating a
power-localization null, `core_frac`, as if it settled a
phase/interference-sensitive question, `σ_ext`, that it structurally
cannot address). Neither changes a scored verdict on file, but both
should be corrected before this cycle's "same near-zero order of
magnitude" language is cited forward as settled characterization.

## Single most important thing for Iteration 85, from PHOTONICS

**Run the numerator floor-gate check (item 4) on the actual PEC-cored
PRIMARY article, not the hollow substitute** — already NOTES.md's own
top-ranked Next item, and I endorse it as the single highest-value
action: it directly tests whether P2/P3's own "accelerating collapse"
headline on the `kappa_window` bridge partly reflects the solver's own
noise floor rather than physics, on the actual article the claim was
made about. While that capture exists, add one cheap, zero-extra-FDTD
diagnostic this review motivates: a coherent-phase comparison (not just
`|Ez|²` power) between the hollow and PEC-cored downstream fields at the
same window, so the hollow-vs-PEC-cored delta test's own optical
question — is there a real, phase-mediated core-boundary contribution to
`σ_ext`, distinct from power deposition — is actually discriminated
rather than continuing to be waved off by a power-only `core_frac` null
that cannot see it.
