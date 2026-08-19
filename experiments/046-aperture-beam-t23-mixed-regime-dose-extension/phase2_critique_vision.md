# PHASE 2 — CRITIQUE · VISION SCIENCE (blind) · exp-046, Panel Iteration 23

*Every number below was re-derived or re-read from the cited file before it
was used. Verification log at the end.*

## Steel-man (≤150 words)

Verified, not conceded — this is the best-sourced Phase-1 document I have
audited. Every geometry constant reproduces (`042/design_geometry.py:119-137`);
`C_THR = 0.005` is at `042/run.py:41`; the 36-cell λ×θ₀×FWHM grid at `:89-91`;
`C_empty(+40°,600nm) = −0.010964794540566314` and exp-042's worst incoherent
cell `−0.004006497410421138` both match their `results.json` to every digit;
`profile="gauss"` is genuinely never exercised anywhere in-repo (grep confirms —
zero call sites). §2.1's w₀ / 2w₀ / 1504·(2w₀)⁻¹ / z_R / z_eff/z_R / N_F columns
recompute exactly, all 12 rows, plus the 518.0/388.5/310.8 full-aperture
reference. Block B's two committed regimes reproduce exp-045's `results.json` to
every printed digit. Block C's closed form reproduces all 8 committed Host-D
ratios (worst 9.13×10⁻⁴ relative). Block A carries a real absolute-identity gate
(S16-c, ≤1×10⁻¹²). The sidecar deferral is stated, not silent.

## Sharpest attack (≤150 words)

§6 defers my glare/adaptation sidecar because "producing numeric perceptual
thresholds from seat memory is exactly the failure mode that produced Iteration
22's fabricated PMMA citation." The same document then does it. §1: "607× below
NETD, Wien peak 9.885 µm, **eye-invisible**" — an unsourced perceptual verdict,
from seat memory, welded to a detector threshold. P-TH23-B3 promotes it to a
*scored* prediction ("still UNDETECTABLE and **eye-invisible**") whose entire
falsification band is `NETD_lo/dt_ss ∈ [600,615]` and Wien `∈ [9.87,9.90]`: the
perceptual half has no perceptual falsifier and cannot fail. That is exp-036's
spiropyran shape verbatim — a physical quantity carrying a visual claim never
scored against a sourced threshold. Idealization 9 hardens only per-point
*storage* — the one locus `netd_disposition()` already auto-fills
(`lab/thermo_sidecar.py:215`) — and omits both loci Iterations 20/21/22 actually
mandated: prose/console prints, and inline-at-point-of-claim. §4 breaches the
latter at B3, B5, C1, C3, C4.

## Verdict

**support-with-changes**

The physics and the arithmetic are sound; five defects are load-bearing for my
charter and one is a plain arithmetic error. All are zero-cost.

1. **The "eye-invisible" perceptual claim (sharpest attack).** Strike it from
   §1 and from P-TH23-B3's prediction text, or state its actual basis (Wien peak
   9.885 µm lies ~12,700× outside the photopic band) and give it a *perceptual*
   falsifier. As written the claim's only falsifier is a detector classification.
   PANEL.md assigns perceptual threshold-pinning to VISION, with sources, before
   any run scored against it — §6 correctly cites that rule to defer my
   deliverable and then breaches it in §1.

2. **`C_THR`'s citation strips its own source line's disclaimer.**
   `042/run.py:41` reads in full: `C_THR = 0.005  # VISION's T2 photopic C_thr
   -- context only, this leg scores no perceptual pass/fail`. §2.0 imports the
   value with the perceptual half of that comment ("VISION's T2 photopic bar")
   and drops the disclaiming half. P-TH23-A1 then *scores* against it
   ("|C_empty| > `C_THR`=0.005 at ≥34 of 36 cells") with the only disclaimer
   sitting at §3, block-scope. Using `C_THR` here is legitimate and precedented —
   it is a contamination-risk yardstick for a *future* constraint-3 run, not an
   instrument-floor gate (the instrument gate is `GATE_HARD = 0.001`, exp-024/041)
   — but the program has already had to correct exactly this mislabeling once
   (LOGBOOK T20: "an earlier draft of this entry mislabeled it 0.005, which is
   VISION's own T2 perceptual C_thr bar, not an instrument-floor gate; caught at
   Iteration 18 Phase 2"). Reuse the comment verbatim at A1, and name the finding
   a contamination-risk/illumination-model reading, never a constraint-3 verdict.
   Related standing risk: `041/results.json` rows carry a bare
   `pass_gate_perceptual_context` field I flagged at Iteration 18 as primed for
   mis-citation; Block A must not add a second such field.

3. **The Tier-2 deferral never names the tripwire, and its escalation is weaker
   than this program's own precedent.** §6 frames the sidecar as merely "Tier 2
   in Red Team's own Iteration-22 ranking." It is not merely that. LOGBOOK
   Iteration 20 Phase 5: VISION "self-imposed an Iteration-23 tripwire" on this
   item, "matching THERMO's own precedent" — THERMO's precedent (Iteration 19)
   being "a fourth consecutive deferral should escalate to Red Team under
   criterion 4's spirit without further debate." Iteration 21 reaffirmed it
   ("stands unchanged, not accelerated"); Iteration 22's Tier-2 entry reads
   "(self-imposed tripwire, **now due**)." Deferring it at Iteration 23 *trips*
   it. The three stated reasons are genuinely specific and reason 2 (T18
   EGRESS_BLOCKED, eleventh consecutive confirmation) is dispositive on my own
   charter's terms — I do not contest the deferral itself. I contest that the
   proposal silently downgrades a tripped tripwire to a queue item, and that its
   replacement escalation ("recommends it as Iteration 24's Tier-1 #1 … if it
   slips past Iteration 24 it should be treated as a Red Team program-integrity
   item") is precisely the one-cycle-extension-via-prose device Iteration 22
   permanently closed for the sibling item — the aperture check whose hardened
   rule ("MUST run at Iteration 23, by any lead seat … Checkpoint criterion 4
   fires automatically and immediately — no further debate, no seat vote, no
   Director discretion, and no further one-cycle extensions via prose") is the
   only reason Block A exists in this proposal at all. The cycle takes the hard
   form of the escalation for the item it delivers and proposes the soft form for
   the item it drops. Fix: state that the Iteration-23 tripwire has tripped,
   route it to Red Team at this Phase 2 per its own terms, and if it is carried,
   carry it in the Iteration-22 hardened form (automatic criterion-4 firing if
   Iteration 24 closes without it), not in prose. The QUANTUM-as-lead /
   non-native-lead half *is* consistent with precedent (Iterations 18, 20, 21) and
   rotation (Iteration 24 is QUANTUM's slot; VISION's is 25) — that half is fine.

4. **Arithmetic error, §2.1, load-bearing for P-TH23-A2.** The `w_y(z)` entry for
   λ=450 nm / FWHM=2° reads **199.33**; the proposal's own stated formula
   `w_y = w₀√(1+(z_eff/z_R)²)/cos θ₀` with its own committed
   w₀=161.05, z_R=5432.3, z_eff=291.106 gives **210.539** — a 5.3% error. The
   other eleven rows reproduce exactly (88.69, 70.29, 114.61, 280.54, 115.61,
   79.47, 116.10, 350.57, 142.96, 89.91, 117.98 — all confirmed). §2 asserts
   "Nothing is asserted from memory"; this number is not reproducible from the
   cited constants. It is load-bearing because `w_y` is the sole width parameter
   of the §4 envelope model `b(y)=exp(−2(y−y_peak)²/w_y²)` that sets A1's and
   A2's bands, and A2's own tolerance (≤5% at ≥30/36, ≤10% at 36/36) is the same
   size as the error. Recompute the affected cell before Phase 3.

5. **Idealization 2's stated waist range is structurally impossible.** "At
   FWHM=20° the waist is only 1.07–1.34 λ." By the proposal's own relation
   w₀ = C·λ/Δθ, the waist in units of λ is *λ-independent*: C/Δθ(20°) = **1.0737 λ
   at all three wavelengths**, confirmed against §2.1's own table
   (16.11/15 = 21.47/20 = 26.84/25 = 1.0737). No 1.34 exists. A paraxial-validity
   idealization must not overstate its own margin. (Minor, same class:
   §2.4's `ln(21·e^(−0.5)) = 2.5443` is 2.54452; immaterial to C6's ±0.05 band.)

6. **P-TH23-A1's band is looser than its own predictor.** §4 reports the
   envelope model's 36-cell output as |C| ∈ [2.99×10⁻², 9.98×10⁻¹] — every cell
   already ≥6× `C_THR` — while A1's committed band is "≥34 of 36." A prediction
   pre-registered at a band its own committed predictor clears by 6× is the
   pattern Red Team flagged at Iteration 17 (RT2). Tighten to 36/36, or state
   that the ≥34/36 slack is reserved for the propagator/FDTD reduction, not the
   envelope model.

**On the NETD-propagation question directly (Director's brief):** no, the
proposal's committed language would not carry the disclaimer through if
implemented as described. Idealization 9's commitment is "stored per-point at all
2496 + 24 + 160 points" — but `ts.netd_disposition()` already returns a
`"disclaimer"` key at `lab/thermo_sidecar.py:215`, so per-point storage is
automatic unless a caller strips it (exp-045's defect, which I caught at
Iteration 22 and which was fixed). The loci that have actually failed — twice —
are NOTES.md prose and `run.py` console prints (Iteration 20, my own self-review;
Iteration 22, Red Team's fix list) and inline-at-point-of-claim in §4 (Iteration
21 mandatory fix 6). Idealization 9 names none of them, and §1/§4 already breach
the last one. Storage is the compliant locus; the proposal hardens the compliant
locus and leaves the failing ones unaddressed.

**On Block A's contamination-risk framing directly:** the *structure* is right —
§1 calls it instrument- and model-fidelity characterization, §3 states T1 escape
route NONE and issues no constraint-3/4 verdict at either tier, and A1/A7 are
scoped to `C_empty` and to exp-041's sponge reading, not to a scene. The failure
is at the sentence level, at items 1 and 2 above, in exactly the two places a
future cycle would cite from.

## Flip

Do all six above (all zero-cost). If only one: **strike "eye-invisible" from §1
and P-TH23-B3 and inline `lab/thermo_sidecar.py:215`'s disclaimer verbatim at
every §4 prediction that names NETD or UNDETECTABLE (B3, B5, C1, C3, C4), plus
`042/run.py:41`'s "context only, this leg scores no perceptual pass/fail" comment
verbatim at P-TH23-A1** — that single change removes the only unfalsifiable
perceptual claim in the document and closes the point-of-claim gap this program
has now had to fix in three consecutive cycles.

---

## Verification log (what I actually ran)

**Confirmed exact:**
- `042/run.py:41` — `C_THR = 0.005`, with the inline disclaimer quoted above.
- `042/run.py:89-91` — λ∈{450,600,750} × θ₀∈{36,38,40} × FWHM∈{2,5,10,20} = 36.
- `042/design_geometry.py:119-137` — NX/NY 360/1584, ABSORB/TAPER 40/40,
  SRC_X/PLANE_X 300/77, R_OUT/GUARD_OUT/W_FLANK 78/185/78, CPL {15,20,25},
  STEPS/COURANT 1400/0.99, OBJ_Y 792, D_SP 223, Y_LO/Y_HI 40/1544, A=752
  (asserted in code, not fitted). Aperture 1504 cells = 100.3/75.2/60.2 λ.
- `041/design_geometry.py:140-141` — `SPONGE_TAU_CENTER=0.10`,
  `SIGMA_SPONGE = 0.10/(2·78) = 6.410256410256410×10⁻⁴`.
- `lab/ambient.py:42-50` — `window_means`, |y−y₀| ≤ w_obj / guard_out ≤ |y−y₀| ≤
  guard_out+w_flank. Matches the quoted ±78 / 185–263 windows.
- `lab/fdtd2d.py:132-137,144-145,152-156` — `profile="gauss"`,
  `p = exp(−((y−y_c)/width)²)`, docstring "width = 1/e half-width in cells",
  `y_c = ½(y_lo+y_hi) = 792`. The amplitude-1/e ⇒ intensity-1/e² ⇒ w₀ mapping
  in §2.1 reason 2 is correct.
- **`profile="gauss"` has zero call sites repo-wide** — the grep claim holds;
  the engine path is genuinely untested, and a new suite stage is the correct
  PANEL.md response.
- `041/results.json` `block_main` — `C_empty(θ=+40°, 600nm) =
  −0.010964794540566314`; `elapsed_s/n_new_runs = 91.607/30 = 3.05 s/run`.
- `042/results.json` `phase5_erratum.block_beam_corrected.worst_cell` —
  750 nm, θ₀=38°, FWHM=2°, `C_incoherent = −0.004006497410421138`. Run 7's
  N_F=40.7 at θ₀=38° recomputes to 40.73. ✔
- §2.1 recomputed from scratch: C = 2√(2 ln 2)/2π = 0.37478125; all 12 w₀, 2w₀,
  1504/(2w₀) (2.80–46.69), z_R, z_eff/z_R and N_F values match; full-aperture
  N_F = 518.0/388.5/310.8. **Sole exception: w_y(450, FWHM=2) — see item 4.**
- walk = 162.02/174.23/187.12 at 36/38/40°; y_c,aim = 629.98/617.77/604.88;
  z_R(w₀=40, λ=20) = 251.3. ✔
- Truncation: unaimed rim residual exp(−(752/268.42)²) = 3.894×10⁻⁴ (I = 1.52×10⁻⁷);
  aimed 565/268.42 = 2.105 w₀ → 1.188×10⁻², 590/214.73 = 2.748 w₀. ✔
- Block B: all eleven quantities in columns 1–2 match
  `045/results.json::block_b_hconv_mass_rederivation_and_t22_table.length_scale_regimes`
  to every digit (h_eff 3672.8340834 / 11111.111111; area 5.0112270×10⁻¹¹ /
  5.4756×10⁻¹²; mass 8.2655553×10⁻¹³ / 2.9854066×10⁻¹⁴; dP/dT 1.8431176×10⁻⁷ /
  6.0868159×10⁻⁸; dt_ss 1.0875241×10⁻⁵ / 3.5982340×10⁻⁶; τ 3.1391858×10⁻³ /
  3.4332969×10⁻⁴; dwell/τ 21.236929 / 194.176815; Bi 1.7567568×10⁻⁴; Kn
  9.280969×10⁻³ / 2.807692×10⁻²; slip 3605.9016 / 10520.3528, −5.3168%).
  Mixed column re-derived independently: P_abs(w_on)/dP/dT(r_out) =
  2.0044348×10⁻¹²/6.0868159×10⁻⁸ = **3.2930761×10⁻⁵ K** ✔;
  NETD_lo/dt_ss = **607.33** ✔; Wien(293.15 K) = **9.8849 µm** ✔;
  (w_on/r_out)² = 9.15192 ✔; dP/dT ratio = 3.02805 ✔. τ_thermal's
  L_power-independence is algebraically correct as stated.
  `045/run.py:101-107,277-279,406-412` all match their cited line numbers;
  `self_consistent_regime`'s power branch confirms the mixed convention is a
  genuine third case, not a relabel.
- `lab/kinetics.py:97` — `N_TRANSIENT_TAU = 25.0`, docstring confirms it is the
  RK4-branch switchover for `integrate_segments` (`:131-133`, `:156`). The
  proposal's "the stake is smaller than T23's framing implies" reading is correct:
  nothing in the thermal chain is numerically integrated. `pulse_train_segments`
  at `:201-219` ✔.
- `lab/thermo_sidecar.py:146-177` (`steady_state_delta_T`, `transient_delta_T`),
  `:193-199` (NETD disclaimer docstring), `:215` (auto-attached disclaimer key),
  `:224-243` (`WitnessScenario`, WebSearch-snippet sourcing convention) ✔.
- `038/run.py:31-45` tiers: A/B at r≤1e-3 → PUBLISHED, C → PLAUSIBLE, r=1e-1 →
  PLAUSIBLE. The 6-PUBLISHED / 6-PLAUSIBLE split among the 12 new points is
  correct. dwell/τ_k = 6.67×10⁷ / 6.67×10⁴ / 66.7 / 0.667 ✔.
- Block C closed form, re-derived and run against all 8 committed exp-045
  points: 1.0034714/1.0034715/1.0034865/1.0051247 (5τ, exact to 10⁻¹⁴) and
  1.4522287/1.4522276/1.4521189/1.4385742 vs committed 1.4509044/1.4509034/
  1.4507961/1.4374191 — max 9.13×10⁻⁴ relative, under-converged in the stated
  direction. P-TH23-C5's ≤0.2% band holds. m=5 supremum 1/(1−e⁻⁵) = 1.0067837 ✔.
  Counts: 12 points × 2 gaps = 24; 16 × 5 × 2 = 160; 4·4·6·2·13 = 2496 (416 new) ✔.
- `037/NOTES.md:827-829` — ρ=2330, c_p=700, κ=148 for silicon ✔ (reused, and
  correctly labelled as reused rather than re-sourced).
- `042/design_geometry.py:96-104,187-192` — 13.0/9.8/7.8 periods, thinnest at
  750 nm ✔. Idealization 10's disclosure is accurate, including that this is the
  fourth consecutive deferral of the settling-margin test.
- `lab/validation/run_all.py` — 15 stages exist; stage 16 is the correct next
  index; S16-c is a genuine absolute-identity gate per PANEL.md's Phase-4 rule.
  "No `lab/` *engine* file modified" is a fair and correctly-drawn distinction.

**Ruled-out check:** nothing here resurrects R1, R2 or R3, and nothing
contradicts an established LOGBOOK finding. The proposal's claim that its
2.80×–46.69× bracket corrects T21's cited "3–30×" is fair — QUANTUM's Iteration-19
figure (≈2.5λ ≈ 50 cells at FWHM=20°) is consistent with 2w₀ = 2.147λ = 42.95
cells at 600 nm.

**Not defects, checked and cleared:** the A-unaimed beam walking 162–187 cells
off a ±78-cell window (idealization 11 — correctly called a property, not a
defect, and correctly paired with the aimed control); the A-aimed leg being
analytic-only; idealization 3's refusal to build the Schell-model bridge without
a sourced flashlight coherence length (correct — that figure still does not
exist anywhere in this program); A7's explicit EXPLORATORY tag; §1's own
pre-registered way to lose (P-TH23-A1 falling QUANTUM's way).
