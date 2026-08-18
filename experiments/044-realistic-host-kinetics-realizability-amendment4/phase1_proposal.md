# Phase 1 proposal — verbatim (MATERIALS, lead, panel Iteration 21)

Kept verbatim per this program's flag-don't-rewrite convention (T10
precedent). Superseded in load-bearing respects by Phase 3's synthesis in
`NOTES.md` — read that first for what was actually built.

## "The Realistic-Host ON-Endpoint Kinetics Gate + REALIZABILITY_MEMO.md Amendment 4" (candidate exp-044)

# PHASE 1 — PROPOSAL · Panel Iteration 21 (candidate exp-044) · Lead seat: MATERIALS & METAMATERIALS

## Scope decision (stated up front, per Director's brief)

Two blocks, bundled under exp-034's own precedent for "tightly-related,
all-zero-cost, all-desk/analytic items," not exp-042's "don't bundle
unrelated deliverables" caution (exp-043) — because both blocks share one
input (`lab/kinetics.py`'s existing 5×5 grid and its
`REALIZABILITY_MEMO.md` tier labels) and one output shape (a
realizability-tier table entry), not two independent charters stapled
together:

- **Block A — Priority #1 (Red Team's "single most consequential open
  item," QUANTUM's native charge, executed here under Iteration-18/20
  non-native-lead precedent):** rerun the σ(I) ON-endpoint kinetics gate
  against `lab/kinetics.py`'s own PUBLISHED/PLAUSIBLE-tier grid points, not
  the two r=1 UNOBTANIUM boundary probes exp-043 tested.
- **Block B — Priority #4 (native):** `REALIZABILITY_MEMO.md` Amendment 4
  — the three named citation corrections.

**Deferred, one line each:** #2 (THERMO's h_conv/mass_kg re-derivation) —
needs THERMO's own judgment on the gas-conduction correlation choice, not
a MATERIALS-appropriable arithmetic swap. #3 (EM's
geometric-disk-vs-`iso_xsec_sq` table entry, T22) — EM's own committed
convention call, not mine to pre-empt. #5 (PHOTONICS' 3λ
achromatic-idealization check) — cheap and independent, but adds a third,
disconnected desk thread rather than deepening the two above; better run
standalone next cycle. Block A quietly depends on `iso_xsec_sq` staying
as-is (flagged in Idealizations) — deferring #3 is a scope choice, not an
oversight.

---

## 1. Mechanism / instrument narrative (≤300 words)

Neither block proposes a mechanism. Both are instrument corrections
applied to existing machinery — no new code, no new trust-suite stage,
zero FDTD calls.

**Block A.** Exp-043's kinetics gate tested the σ(I) ON endpoint (τ=3.9,
established `ratio_abs_ext`=0.6075) at exactly two `lab/kinetics.py` grid
points — both r=k_f/k_r=1, the grid's UNOBTANIUM-tier top extreme,
self-corrected at Iteration-20's own close from "representative" to
"boundary probe." The genuinely open question — does a real,
literature-plausible host reach meaningful ON-state absorption within one
flashlight dwell — was never tested. This block reuses exp-043's own
reference ceiling (steady-state ΔT at full n=1 population) and dwell
(66.7ms central) verbatim, sweeping it across the grid's 16
non-UNOBTANIUM points (Hosts A–D × RATIOS excluding r=1). It also surfaces
and discloses a structural property of exp-043's own scaling formula
(ceiling×n_at_dwell/n_ss): because it divides out n_ss, it returns ≈the
full ceiling for ANY host whose relaxation time is fast relative to dwell,
regardless of how small the true steady-state population is — silently
insensitive to r for Hosts A/B/C. A second, disclosed reading
(ceiling×n_at_dwell directly) is reported alongside it, not substituted
for it.

**Block B.** Three citation corrections to `REALIZABILITY_MEMO.md`,
triggered by exp-043's newly-sourced witness irradiance (46× below the
program's old placeholder): (1) an RSA sub-finding that used the old
placeholder to claim a subclass "clears" irradiance is checked against the
new number; (2) TPA's OOM gap is recomputed against the new witness point;
(3) the 45m witness-distance parameter is connected to the founding
statement's own "50 yards."

## 2. Parameter table

### Block A — ON-endpoint kinetics gate, PUBLISHED/PLAUSIBLE-tier hosts

| Input | Value | Source |
|---|---|---|
| Grid (reused verbatim, zero new points) | Hosts A(k_r=1e9)/B(1e6)/C(1e3)/D(1e1) × RATIOS {1e-9,1e-5,1e-3,1e-1} = 16 points | `experiments/038-t17-rate-equation-kernel/run.py::HOSTS,RATIOS`; Host E and r=1.0 excluded (always UNOBTANIUM per `run.py::realizability_tier`) |
| Tier split of the 16 points | 6 PUBLISHED (A,B × r∈{1e-9,1e-5,1e-3}), 10 PLAUSIBLE (A,B×r=1e-1; C,D×all 4 r) | same function, unmodified |
| Reference ON ceiling (n=1, full switch) | ΔT_ss = 3.9436×10⁻³ K | exp-043 `results.json::on_endpoint_tau_3p9.steady_state_dT_K_central` — `SIGMA_EXT_ON`=235.967 cells, `RATIO_ON`=0.60748 (exp-026, 600nm), `iso_xsec_sq` convention, irr_central=6.58×10⁻⁶ W/cm² |
| Dwell | 0.06667 s central (θ_beam=10°, ω=150°/s) | exp-043 Part A, docket #7 |
| NETD band | (0.020, 0.050) K | exp-043 Part A, P-D7-4 CONFIRMED |
| Reading (a) — reused convention | ΔT_a = ΔT_ss × (n_at_dwell/n_ss), `kin.relax_exact`/`kin.n_eq_exact` | exp-043's own formula, unmodified, for direct comparability |
| Reading (b) — disclosed companion | ΔT_b = ΔT_ss × n_at_dwell directly | this cycle's own addition — physically motivated (n(t) as a fraction of the n=1 reference the ceiling itself represents), not a silent replacement of (a) |

### Block B — `REALIZABILITY_MEMO.md` Amendment 4

| Correction | Old figure | New input | Recomputation method |
|---|---|---|---|
| RSA subclass irradiance (long-triplet, Hirata et al. *Nat. Mater.* 13, 938 (2014)) | "10⁻⁴ W/cm² — below the ~10⁻³ W/cm² witness estimate" (exp-036) | witness central 6.58×10⁻⁶ W/cm², range [1.10×10⁻⁶, 4.41×10⁻⁵] (exp-043 P-D7-1) | ratio = 1e-4 / irr |
| TPA irradiance gap (Sheik-Bahae/Van Stryland; He et al. 1995) | "9–12 OOM" (memo original text, using old ~1e-3 W/cm² point) | same witness figures as above | gap = log10(TPA_range / irr), same broad range (1e6–1e9 W/cm²) the original 9–12 figure used, swapping only the irradiance input |
| Witness distance (45.0 m, "carried unsourced") | flagged unsourced, exp-043 Phase-1 | founding statement: "stopping about 50 yards away" (README.md) | 50 yd × 0.9144 = 45.72 m |

## 3. T1 escape-route statement

**None — instrument/desk characterization.** Neither block proposes,
tests, or revises a T1 escape-route mechanism; both correct/extend
existing realizability and thermal-sidecar bookkeeping on the
already-instrumented σ(I) route.

## 4. Falsifiable predicted outcomes

**Block A** (all 16 points computed from committed formulas —
deterministic, not stochastic; falsifiable against my own worked numbers,
which the Phase-4 script must reproduce exactly):

- **P-MAT21-A1** (reading-(a) host/r-insensitivity, Hosts A/B/C): at all
  12 points with k_r≥1e3, n_at_dwell/n_ss ≥ 0.9999 regardless of r
  spanning 1e-9→1e-1 (8 decades) → ΔT_a ∈ [3.90×10⁻³, 3.95×10⁻³] K,
  effectively **constant**, at every one of those 12 points.
- **P-MAT21-A2** (reading-(a), Host D): ratio ∈ [0.485, 0.52] at all 4
  Host-D points (τ_D≈0.09–0.10s set almost entirely by k_r, weakly
  modulated by r) → ΔT_a ∈ [1.90×10⁻³, 2.05×10⁻³] K.
- **P-MAT21-A3** (reading-(a), NETD): all 16 points classify
  **UNDETECTABLE** — max ΔT_a (3.944×10⁻³ K) sits ≈5.1× below
  netd_lo=0.020K.
- **P-MAT21-A4** (reading-(b), dynamic span): ΔT_b spans >8 orders of
  magnitude across the grid — 3.94×10⁻¹² K at r=1e-9 up to 3.59×10⁻⁴ K at
  r=1e-1 — tracking n_ss directly (ΔT_b/ΔT_ss ≈ n_ss to within Host D's
  own ratio<1 correction).
- **P-MAT21-A5** (readings diverge at PUBLISHED tier): at every PUBLISHED
  point (A/B × r≤1e-3), ΔT_b/ΔT_a ≤ 1.1×10⁻³ — the two conventions
  disagree by ≥3 orders of magnitude, precisely because reading (a)
  saturates to ≈1 while n_ss≪1 (P-MAT21-A1's own mechanism).
- **P-MAT21-A6** (reading-(b), NETD, worst case): all 16 points
  UNDETECTABLE under reading (b) too — the largest ΔT_b (3.585×10⁻⁴ K,
  Host A or B at r=1e-1) sits ≈56× below netd_lo.
- **P-MAT21-A7** (best-characterized PUBLISHED point): Host A, r=1e-3
  (largest achievable PUBLISHED-tier n_ss=9.99×10⁻⁴) gives
  ΔT_b=3.94×10⁻⁶ K — ≥5000× below netd_lo. **Falsification condition:**
  any of P-MAT21-A1/A3/A6 failing (e.g. reading (a) showing real
  r-sensitivity at Hosts A/B/C, or any grid point crossing into
  MARGINAL/DETECTABLE) would overturn this cycle's own headline and
  requires immediate disclosure, not smoothing.

**Block B:**

- **P-MAT21-B1** (RSA reversal): 1×10⁻⁴ / irr_central = 15.2× [predicted
  band 14–16×]; 1×10⁻⁴ / irr_hi = 2.27× [band 2.0–2.5×] — the subclass's
  own onset now sits **above**, not below, the entire newly-sourced
  witness range. Tier unchanged (UNOBTANIUM-WITH-PARAMETERS — dynamic
  range alone is already decisive, irradiance-independent per
  Iteration-20's own Phase-2 finding), but the specific "clears, even
  below witness estimate" claim is stale and reverses sign.
- **P-MAT21-B2** (TPA OOM): like-for-like recomputation (same broad
  1e6–1e9 W/cm² range, swapping only the witness point) gives
  **11.2–14.2 OOM** central [predicted band 10.5–15.0 OOM under the full
  witness-uncertainty bracket] — vs. the original 9–12. **Falsification
  condition:** landing outside [9.5, 15.5] OOM under either method would
  mean the queue-note's own "~10–13" ballpark and this proposal's
  central-point method disagree in a way worth a dedicated note, not
  silent reconciliation.
- **P-MAT21-B3** (distance cross-reference): 50 yd = 45.72 m, 1.6% from
  exp-043's carried 45.0 m — **CONFIRMED** as a genuine match to
  README.md's founding statement, not previously connected; the memo's
  honest-limits section gets a caveat that this is still an eyewitness
  estimate, not a metered figure, not full sourcing.

## 5. Idealizations

- Block A reuses exp-043's reference ceiling (ΔT_ss=3.9436×10⁻³K),
  witness irradiance (6.58×10⁻⁶ W/cm²), and dwell (66.7ms) **verbatim,
  not re-derived** — any future correction to those upstream numbers
  (including this cycle's own deferred #2/#3 items, or Amendment 4's own
  witness-parameter cross-reference) propagates directly into Block A's
  absolute numbers, a disclosed dependency chain, not an independent
  re-measurement.
- Both readings assume the ON-reference's measured `ratio_abs_ext`=0.6075
  corresponds to n=1 exactly (linear σ_abs(n)∝n mixing, the same
  idealization exp-040's `amplitude_bridge` already uses elsewhere) — not
  independently re-derived for this specific endpoint this cycle.
- `iso_xsec_sq` still governs the ceiling's absolute magnitude (T22, live,
  deferred item #3 this cycle) — Block A's numbers would rescale if that
  convention is revised later.
- Host lifetimes (k_r grid) are inherited from exp-038/exp-037's own
  citations (Soref & Bennett 1987) plus two MATERIALS-owned boundary
  probes — not re-sourced this cycle; a citation audit of the lifetimes
  themselves is a different, undone task from Amendment 4's RSA/TPA
  corrections.
- `theta_beam`=10° is exp-043's own flagged **lower-confidence, not
  independently WebSearch-confirmed** figure — inherited uncertainty, not
  resolved here.
- NETD is an instrument/detector threshold, not a human perceptual one
  (VISION's standing mandatory disclaimer) — nothing in Block A bears on
  constraint-3/4's human-eye verdict.
- Block B is citation-correction-only by design — it does **not** reopen
  RSA/TPA's own dynamic-range/D_req findings (those stand), and performs
  no new literature search (T18's WebFetch blockage is unconfirmed this
  shift since Phase 1 runs no search at all; a fresh search at Phase 3/4
  would be a scope addition Phase 2 must explicitly bless).
- Both blocks add zero new trust-suite gates and zero new code — pure
  reuse of already-gated (`lab/kinetics.py` stage 12) and already-committed
  (exp-043 `results.json`) machinery.

---

**Files read to ground this proposal:** `PANEL.md`, `LOGBOOK.md` (full),
`PLAN.md` (full), `experiments/043-docket7-thermo-sidecar/{run.py,
results.json}`, `lab/kinetics.py`, `lab/thermo_sidecar.py`,
`experiments/038-t17-rate-equation-kernel/run.py`,
`experiments/034-floor-convergence-scale-bridge/REALIZABILITY_MEMO.md`,
`experiments/036-realizability-literature-check/NOTES.md`, `README.md`.
