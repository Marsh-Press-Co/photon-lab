# PHASE 2 — CRITIQUE · Panel Iteration 23 · Seat: MATERIALS & METAMATERIALS

*Blind/parallel review of `phase1_proposal.md` (exp-046). Charter: sub-wavelength
structure and what could physically realize the proposed optical behavior; owns
the realizability bound (published / plausible / unobtainium-with-parameters).
Read first: PANEL.md, LOGBOOK.md (R1–R3, ESTABLISHED, T1–T23),
`experiments/034-floor-convergence-scale-bridge/REALIZABILITY_MEMO.md`
Amendments 1–4. Nothing here resurrects a ruled-out idea; nothing in the
proposal does either.*

---

## Steel-man (≤150 words)

The most numerically honest Phase-1 document this seat has audited. I recomputed
every Block-B quantity independently from `experiments/045-.../run.py:194-342`'s
own constants: h_eff 11111.111111, area 5.4756e-12, mass 2.9854066e-14, dP/dT
6.0868159e-08, P_abs 2.0044348e-12, dt_ss_full 3.2930761e-05, τ_th 3.4332969e-04,
dwell/τ 194.176815, Bi 1.7567568e-04, Kn 2.807692e-02, slip −5.3168%, NETD_lo
margin 607.3×, (w_on/r_out)² = 9.151923 — all exact, and the two committed
regimes reproduce `results.json` to every printed digit. C2's closed form
reproduces exp-045's eight Host-D points (1.8e-15 at 5τ, 9.1e-4 at 0.5τ, right
magnitude, right sign, right cause). Host A–D tier labels match
`experiments/038-.../run.py:39-46` exactly. `profile="gauss"` is grep-confirmed
never exercised. No realizability tier moves, and "T1 escape route: NONE" is
defensible.

## Sharpest attack (≤150 words)

**Block C exists to score against `REALIZABILITY_MEMO.md`'s tiers, yet its grid
contains zero UNOBTANIUM-tier points.** C1 runs Hosts A/B/C × r∈{1e-9…1e-1};
exp-038's grid is 5 hosts × 5 ratios (`run.py:25-26`), and `realizability_tier`
(`:39-46`) returns UNOBTANIUM-WITH-PARAMETERS for **Host E** and for **every
r=1.0**. So P-TH23-C4's "corroborating Amendment 3" is structurally impossible:
Amendment 3's finding is memory "*only* at Hosts D **and E** of the 25-point
grid" (memo `:93-96`) — a grid without E cannot corroborate it, and a grid with
no UNOBTANIUM point cannot test its actual claim, that the memory axis and the
D_req/irradiance realizability axis "are not shown to be independent."
Compounding: C2 already settles the question analytically (ratio_∞ = 1/(1−a·f);
threshold D/τ_k < ln21 − 0.5 = **2.54452**, not the stated 2.5443), so C3's 160
points verify code, not physics — the same "near-mechanical consequence"
Amendment 3 already flagged.

## Verdict

**support-with-changes.**

The cycle is sound, the arithmetic is overwhelmingly right, and it moves no tier.
Six changes, all desk-only, zero new FDTD:

- **M1 (binding).** Add **Host E** and the **r=1.0** column to Block C: 25-point
  grid, 9 new host/ratio combos × 2 gaps = 18 extra closed-form points. Without
  them Block C cannot score the tier it names, and P-TH23-C4/C6 cannot say
  anything about Amendment 3's UNOBTANIUM corner. Cost is microseconds. The
  Iteration-22 close's "remaining **12** host/ratio points" (`LOGBOOK.md:8361`)
  is itself the incomplete figure — 21 of exp-038's 25 remain after Host D — and
  Tier-1 #3's wording is "closing … in full" (`:8357-8359`), which 16/25 is not.
- **M2.** Relabel C3 from *test* to *verification*. Its committed band
  ("0.5τ threshold inside [2.4, 2.7]") is **entailed** by C2's own algebra, so it
  cannot fail except through a coding error. State plainly that Amendment 3's
  Red-Team tempering is answered by **C2 alone at zero cost**, and that the real
  finding — the memory criterion depends only on the dimensionless group D/τ_k
  (and m, r through f) — is a *theorem* of the two-state model with hard k_f=0,
  not an empirical discovery. Presenting 160 points as "the duration scan Red
  Team's tempering has been asking for since Iteration 15" (§6) overstates.
- **M3 (my charter, load-bearing).** Downgrade the silicon citation. §2.3 line
  185 labels it "(sourced: `experiments/037-.../NOTES.md:828-829`)". That line
  reads *"silicon's standard **cited** thermal constants (ρ≈2330 kg/m³, c_p≈700
  J/(kg·K), κ≈148 W/(m·K))"* — and `grep -rn "2330\|148 W\|c_p"` over the whole
  exp-037 directory returns **only that one paragraph**: no DOI, no reference, no
  primary source anywhere. exp-045's `run.py:206-208` claims the constants are
  "already sourced" in that line; they are not. exp-046 inherits and upgrades
  that false label. The **values are correct** for bulk crystalline Si (this is
  not a repeat of the fabricated PMMA citation, and idealization 6's
  live-path-in-repo audit is real work) — but idealization 6's standard is a
  *provenance* standard, and it is structurally incapable of detecting a chain
  that terminates in the word "cited" pointing at nothing. Label it
  **ASSUMED — provenance terminates unsourced (T18)** in `results.json`.
- **M4 (my charter).** Disclose the **fill-factor** idealization. mass = ρ_Si·L³
  assigns 100%-fill crystalline silicon to an article the very module doing the
  arithmetic calls "a dilute vapor/aerosol host"
  (`lab/thermo_sidecar.py:151-153`); exp-045's NOTES.md and run.py never mention
  it, and exp-046's idealization 5 covers only body *shape* (cube vs disk), not
  solid fraction. This is not cosmetic: with Bi≪1 and h≫4εσT³,
  τ_th ≈ ρ·C_P·L²/k_air, so §2.3's structural claim that *"T23's operative 'below
  vs above 25' question is decided by the conduction length **alone**"* is
  **wrong as stated** — it is decided by ρ·C_P·L²/(4εσT³L + k_air), and the
  ρ·C_P half is the unsourced half. Add a ρC_P sensitivity row (solid Si →
  1%-fill porous host is 2 decades in τ_th) beside idealization 5's disk row.
- **M5.** Commit **Amendment 5** to
  `experiments/034-floor-convergence-scale-bridge/REALIZABILITY_MEMO.md` at
  Phase 3, recording (a) C2's collapse of the memory axis to a dimensionless-dwell
  criterion and what that does to Amendment 3's "not shown to be independent
  axes" language, and (b) M3's provenance downgrade. §3's "no result here can
  move either UNOBTANIUM-WITH-PARAMETERS verdict" is true of the **tier labels**
  and false of the **memo's evidentiary content**. Amendment 4's own header
  records that exp-044 claimed to deliver an amendment and had not — a
  Checkpoint-4-conditional defect. Do not repeat it. Also record the memo's real
  path: the proposal cites bare `REALIZABILITY_MEMO.md` four times (§2.4, §3,
  P-TH23-C4) and no such repo-root file exists — a program-wide habit, but one
  that sits badly next to idealization 6's own stated standard.
- **M6 (arithmetic, outside my lane but it breaks a committed band).**
  §2.1's `w_y(450 nm, FWHM=2°) = 199.33` is **impossible by construction**: the
  stated formula gives **210.54**, and 199.33 is below the floor
  w₀/cos40° = 210.24 that any Gaussian must exceed. Eleven of the twelve w_y
  values reproduce to the printed digit; this one is 5.3% low, and it feeds the
  envelope model that sets **P-TH23-A2's ≤5% band**. Also: C = 2√(2ln2)/2π =
  **0.37478125**, not 0.3747808 (harmless at A0's 6-s.f. gate, but the document
  claims nothing is asserted from memory); and idealization 2's "waist is only
  **1.07–1.34 λ** at FWHM=20°" is a **single** value, 1.074 λ, since
  w₀/λ = C/Δθ is wavelength-independent by the proposal's own formula.

**On the two questions this seat was specifically asked:**

- *Does anything move a realizability tier?* **No.** Verified against
  `experiments/038-.../run.py:39-46` and Amendment 2's table: the Hosts A–D /
  r-column tier labels in §2.4 are reproduced **correctly** (6 PUBLISHED +
  6 PLAUSIBLE among the 12 new combos, exactly as `realizability_tier` returns),
  and no proposed result touches D_req or the irradiance gap. The claim not to
  move a tier is honest.
- *Is "T1 escape route: NONE" defensible — does any realizability verdict quietly
  depend on the old beam-divergence machinery?* **Yes, defensible; no, it does
  not.** `beam_divergence_incoherent`/`_coherent` exist **only** in
  `experiments/042-t21-magnitude-bridge/` (grep-verified across the repo), built
  at Iteration 19 — after every D_req figure. D_req ≈ 540–600× is τ_on/τ_off =
  3.9/0.0065 from exp-032/034's single-angle-per-run ambient readings (memo
  `:168-186`), which never touch that machinery. Block A cannot retroactively
  move a tier. **One caveat the proposal should state and does not:** if
  P-TH23-A1 lands as predicted (|C_empty| > C_THR at ≥34/36 cells, several near
  |C|≈1), then the empty-scene floor of the instrument that produced the
  τ_off = 0.0065 anchor is illumination-model-dependent at a scale far exceeding
  the bar it was scored against — which bears on the **magnitude** D_req cites,
  even though it cannot move the label. That belongs in §3 as a disclosed
  consequence, not left implicit.

## Flip

**To full support:** M1 + M3 alone — add Host E and the r=1.0 column (18 extra
closed-form points, no FDTD), and relabel the silicon identity ASSUMED rather
than "sourced." Everything else is wording and one arithmetic fix.

**To oppose:** if Phase 3 keeps P-TH23-C4's "corroborating
`REALIZABILITY_MEMO.md` Amendment 3" on a grid containing neither Host E nor any
UNOBTANIUM-tier point. That is a realizability claim this seat owns and the
proposed data cannot support, and it would be the fix-docket pattern
(`LOGBOOK.md:8369-8375`) recurring inside a realizability claim rather than
beside one.

---

## Verification log (MATERIALS, non-binding appendix — the work behind the above)

Everything below was recomputed or grepped from the repo this shift, not taken
from the proposal.

**Block B — reproduced exactly (pure `math`, `SIGMA_SB=5.670374419e-8`).**
irr = (40000/45²)/300/1e4 = 6.58436214e-06 W/cm²; dwell = 10/150 = 0.0666667 s;
r_out_m = 2.34e-06; w_on_m = 7.07900205e-06.

| Quantity | proposal | recomputed | exp-045 `results.json` |
|---|---|---|---|
| h_eff (mixed) | 11111.111111 | 11111.1111 | 11111.111111111113 (r_out) |
| area | 5.4756000e-12 | 5.4756e-12 | 5.475599999999998e-12 |
| mass | 2.9854066e-14 | 2.98540663e-14 | 2.985406631999999e-14 |
| dP/dT | 6.0868159e-08 | 6.08681589e-08 | 6.086815889755324e-08 |
| P_abs | 2.0044348e-12 | 2.00443477e-12 | (w_on branch) |
| dt_ss_full | 3.2930761e-05 | 3.29307605e-05 | — (new) |
| τ_thermal | 3.4332969e-04 | 3.43329695e-04 | 0.00034332969490950116 |
| dwell/τ | 194.176815 | 194.176815 | 194.17681504141214 |
| Bi | 1.7567568e-04 | 1.75675676e-04 | 0.00017567567567567568 |
| Kn | 2.807692e-02 | 2.80769231e-02 | 0.028076923076923083 |
| h slip / rel | 10520.3528 / −5.3168% | 10520.3528 / −5.31682% | 10520.352836448978 |
| NETD_lo/dt_ss | 607× | 607.335× | — |

P-TH23-B1 ✓ (τ_th is independent of L_power — confirmed algebraically and
numerically). P-TH23-B2 ✓ (9.151923 = (235.96673494878587/78)² exactly; 3.02805
vs w_on). P-TH23-B3 ✓ (607.3 ∈ [600,615]; Wien 2897.7715/293.15 = 9.8849 µm ∈
[9.87,9.90]). P-TH23-B4 ✓. P-TH23-B6 ✓ (e^−21.236929 = 5.983e-10;
e^−194.176815 = 4.68e-85).

**Block C — closed form C2 checked against all 8 committed Host-D points.**

| point | C2 closed form | exp-045 committed | rel |
|---|---|---|---|
| r1e-01_5tau | 1.0051247 | 1.0051247 | 1.8e-14 |
| r1e-03_5tau | 1.0034865 | 1.0034865 | 1.8e-15 |
| r1e-05_5tau | 1.0034715 | 1.0034715 | 1.8e-15 |
| r1e-09_5tau | 1.0034714 | 1.0034714 | 1.6e-15 |
| r1e-01_0.5tau | 1.4385742 | 1.4374191 | 8.0e-4 |
| r1e-03_0.5tau | 1.4521189 | 1.4507961 | 9.1e-4 |
| r1e-05_0.5tau | 1.4522276 | 1.4509034 | 9.1e-4 |
| r1e-09_0.5tau | 1.4522287 | 1.4509044 | 9.1e-4 |

The 5τ points agree to **machine precision**, not the "2.6×10⁻⁷" the proposal
reports — that figure is an artifact of comparing its own 7-s.f. rounding. The
0.5τ residual is exactly the finite-train offset the proposal names: `points`
carries **6** ON-end populations for `n_pulses=5`, and (a·f)⁶ ≈ 7×10⁻⁴ at
r→0, matching the 9.1×10⁻⁴ deficit in the under-converging direction. C5's band
(≤0.2%) is safe. Threshold: 1/(1−af) > 1.05 ⟺ af > 1/21 ⟺ D/τ_k < ln(21f);
at m=0.5, r≪1, ln(21)−0.5 = **2.544522**, not 2.5443. At m=5, 21f = 0.1414969
< 1 ⇒ no dwell qualifies, sup = 1/(1−e⁻⁵) = 1.0067836 ✓.

**Tier table (§2.4) — correct.** `realizability_tier(host, r)`
(`experiments/038-.../run.py:39-46`): A/B at r≤1e-3 → PUBLISHED; A/B at r=1e-1 →
PLAUSIBLE; C, D at r≤1e-3 → PLAUSIBLE; all r=1.0 and all Host E →
UNOBTANIUM-WITH-PARAMETERS. The proposal's 6 PUBLISHED + 6 PLAUSIBLE count is
right. `TIER` at `:32-36` agrees. Note P-TH23-C4's "6/6 + 6/6" counts host/ratio
*combos* while C1/C2/C3 count *points* (×2 gaps) — harmless, but make the unit
explicit in `results.json`.

**Geometry (§2.0) — spot-checked verbatim.**
`experiments/042-.../design_geometry.py:119-137`: NX 360, NY 1584, ABSORB 40,
TAPER 40, SRC_X 300, PLANE_X 77, R_OUT 78, GUARD_OUT 185, W_FLANK 78, CPL
{450:15,600:20,750:25}, STEPS 1400, COURANT 0.99, OBJ_Y 792, D_SP 223, Y_LO 40,
Y_HI 1544, A 752 — all ✓. `SIGMA_SPONGE` = 0.10/(2·78) = 6.41025641025641e-04
(`041-.../design_geometry.py:140-141`) ✓. Aperture 1504 cells = 100.3/75.2/60.2 λ
✓.

**Block A anchors.** `experiments/041-.../results.json` `block_main.rows[19]` =
{theta 40.0, lambda 600, C_empty −0.010964794540566314} ✓ — S16-c's regression
target is real. `block_main.elapsed_s/n_new_runs` = 91.60724997520447/30 =
3.0536 s/run ✓. exp-042 `phase5_erratum.block_beam_corrected.worst_cell` =
{750 nm, θ₀ 38, FWHM 2, C_incoherent −0.004006497410421138} ✓, and N_F at that
cell (z_eff = 223/cos38° = 283.0) is 40.7 ✓. `lab/fdtd2d.py:152-156` implements
`profile="gauss"` as p = exp(−((y−y_c)/width)²) ✓, so `width` ≡ w₀ (amplitude
1/e = intensity 1/e²) with no engine change; `grep -rn "gauss"` over all `.py`
finds it referenced **only** in `lab/fdtd2d.py` and `lab/artifacts.py` — never
called from any experiment or validation stage ✓, so the "never exercised or
trust-gated" claim holds.

**§2.1 table — 11 of 12 w_y values exact, one impossible.** With C = 0.37478125,
z_eff = 291.10583, w₀, 2w₀, 1504/(2w₀), z_R, z_eff/z_R and N_F reproduce every
printed digit at all twelve cells (including the 2.80×–46.69× span and the
full-aperture 518.0/388.5/310.8). `w_y` reproduces at eleven cells (88.69, 70.29,
114.61, 280.54, 115.61, 79.47, 116.10, 350.57, 142.96, 89.91, 117.98) and fails
at one: 450 nm/FWHM=2° gives **210.54**, printed **199.33** — below the
w₀/cos40° = 210.24 floor, so it is not a convention difference. walk = 162.02 /
174.23 / 187.12 ✓; y_c,aim = 629.98 / 617.77 / 604.88 ✓. A4's replica spacings
(343.8/458.4/573.0 at FWHM=20; 5730 at FWHM=2, λ=750) ✓ and the 526-cell
object+flank span ✓. Idealization 4's rim residuals: exp(−(752/268.42)²) =
3.899e-04 amplitude, 1.52e-07 intensity ✓; aimed-leg truncation 565/268.42 =
2.105 w₀ ✓ (but the FWHM=2° cells at 450 nm truncate at ~3.5 w₀, outside the
stated "2.10–2.75 w₀" — widen or scope the range).

**Provenance chain, traced to its terminus.**
`exp-046 §2.3:185` → "(sourced: `037-.../NOTES.md:828-829`)" →
`exp-045/run.py:206-210` "already sourced and used in … line 828-829" →
`exp-037/NOTES.md:828-829` "silicon's standard cited thermal constants (ρ≈2330,
c_p≈700, κ≈148)" → **nothing**. `grep -rn "2330\|148 W\|c_p\|C_P"` over
`experiments/037-*/` returns three lines total, two of them that sentence. The
constants are right; the citation is a self-reference. Load-bearing:
τ_th ∝ ρ·C_P (B1/B6, and T23's "below vs above N_TRANSIENT_TAU=25"), and
κ_Si = 148 alone carries P-TH23-B4's Bi = 1.76e-04 lumped-capacitance claim
(vs ≈0.137 under the superseded PMMA identity — `LOGBOOK.md` T22, and
`exp-045/run.py:308-317`).
