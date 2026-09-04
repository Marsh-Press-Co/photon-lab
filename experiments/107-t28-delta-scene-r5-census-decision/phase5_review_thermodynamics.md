# PHASE 5 — REVIEW · Panel Iteration 84 · Seat: THERMODYNAMICS

*Fresh-context review of exp-107's completed results. Blind to any other
seat's current-cycle Phase-5 review, per this cycle's own isolation
discipline. Charter: where absorbed energy goes; the per-proposal energy
sidecar (absorbed power → temperature rise → emission band →
detectability), a post-run analytic calculation, labeled as such, never an
FDTD output.*

## 0. Verdict up front

**CONFIRM-WITH-GAPS.** Item 3 — my own seat's mandatory Phase-2 fix — landed
correctly and reproduces bit-exact from `results.json`'s own `ledger_r156`/
`ledger_r312` fields, re-derived here from primitives using the actual
committed `lab/thermo_sidecar.mixed_length_scale_regime` function, not a
restatement. R21's narration commitment is genuinely honored: all four
cells, not merely the fragile one, are stated with their classification in
NOTES.md's own Result prose. The standing idealizations travel unchanged
and are still disclosed accurately. But there is a real, charter-relevant
gap this cycle's own record does not surface: the same two ledger points
that let this cycle finally compute a real (fixedabs, r=312) margin also
license a thermodynamically well-motivated projection of where that margin
is headed — and it lands almost exactly on top of the newly-tightened 50×
floor. That projection is not in the document, and it should have been.
Nothing here is load-bearing to any scored verdict this cycle filed (Tier 0
is a text-only retirement; Item 3 is a reproducibility gate, not a
physical-uncertainty test, by NOTES.md's own framing) — but it is the
single most consequential number this seat can add to the board for the
next cycle that touches this bridge.

## 1. Independent re-derivation of Item 3 from primitives (not from NOTES.md prose)

Recomputed the full chain from exp-106's `results.json::ledger_r156`/
`ledger_r312`, using the exact anchor constants and formula NOTES.md's own
Setup section states, by directly invoking the committed
`lab.thermo_sidecar.mixed_length_scale_regime` (not re-implementing it):

```
SIGMA_EXT_78 = 240.0073740162445; P_ABS_78 = 1.7409069740390205e-12
RATIO_ABS_EXT_78 = 0.51; DX_M = 30.0e-9
width_m_78 = SIGMA_EXT_78 * DX_M
i_incident = (P_ABS_78/RATIO_ABS_EXT_78) / (width_m_78**2 * 1e4)
  -> 6.584362139917695e-06   (matches results.json's item3_i_incident exactly)

for (family, r, sigma_ext_real, abs_ext_ratio_real) from ledger_r156/ledger_r312:
  width_m = sigma_ext_real * DX_M
  p_abs_w = i_incident * width_m**2 * 1e4 * abs_ext_ratio_real
  l_geometric_m = r * DX_M
  dt_ss_full_K = mixed_length_scale_regime(p_abs_w, l_geometric_m,
                   k_air=0.026, density_kg_m3=2330.0, c_p_j_kgk=700.0,
                   emissivity=0.9, t_ambient_k=293.15,
                   length_provenance="bench_construction")["dt_ss_full_K"]
  margin = 0.020 / dt_ss_full_K
```

Result, bit-exact against `results.json::item3_rows`:

| Family | r | `dt_ss_K` (re-derived) | `dt_ss_K` (filed) | Margin (re-derived) | Margin (filed) |
|---|---|---|---|---|---|
| selfsim | 156 | 5.824085844284275e-05 | 5.824085844284275e-05 | 343.40153175502877 | 343.40153175502877 |
| fixedabs | 156 | 7.622699104110958e-05 | 7.622699104110958e-05 | 262.37425519280833 | 262.37425519280833 |
| selfsim | 312 | 1.163662613549568e-04 | 1.163662613549568e-04 | 171.87112284198233 | 171.87112284198233 |
| fixedabs | 312 | 1.7026593096860568e-04 | 1.7026593096860568e-04 | **117.46331098784337** | **117.46331098784337** |

Every digit reproduces to full floating-point precision — this is not "close
enough," it is identical to the last printed bit. NOTES.md's Result table
states `117.5×` (one-decimal rounding of `117.463…`, consistent, not a
citation defect) and correctly names it "clears the tightened 50×
falsification bar with margin to spare." I confirm both the arithmetic and
the classification: `117.46 > 50`, PASS, and the classification string
(`UNDETECTABLE`) matches `netd_disposition()`'s own output at this
`dt_ss_K` against `NETD_BAND_K=(0.020,0.050)`. **My own Phase-2 mandatory
fix landed correctly, in full, to the stated precision.**

## 2. R21 discharge — checked field-by-field against `results.json`, not merely by presence

The Phase-2 audit flagged this channel as already carrying two non-firing
R21 founding instances (exp-099, exp-100) with a live three-strike
auto-fire clause — a third silent non-narration would fire Checkpoint
criterion 4 automatically. I read `results.json::item3_rows` directly
(reproduced in full in §1's table via my own re-derivation, not taken on
NOTES.md's word) and cross-checked every field NOTES.md's Result table
claims:

- `dt_ss_K`: present for all 4 cells, matches to full precision (§1).
- `Margin`: present for all 4 cells, matches to full precision (§1).
- `Classification`: `results.json` carries `"UNDETECTABLE"` at all 4 cells
  (`selfsim_156`, `fixedabs_156`, `selfsim_312`, `fixedabs_312`) —
  NOTES.md's table states `UNDETECTABLE` at all 4, verbatim match.

**R21 is genuinely discharged, not merely persisted.** All four cells are
narrated with their classification in Result prose — not only the
`(fixedabs, r=312)` fragile cell my own Phase-2 critique flagged, and not
only a headline aggregate. This is the cleanest of the three instances on
this channel to date: exp-099 omitted the sidecar from Result/Learned
entirely; exp-100 persisted-but-never-narrated; this cycle narrates the
full per-cell table, matching every field `results.json` actually carries.
**R21's three-strike clause does not fire — correctly, on the merits, not
by a close reading of scope.**

## 3. `mixed_length_scale_regime`'s standing idealizations — unchanged, correctly disclosed

Checked directly against the function's own source (`lab/thermo_sidecar.py`
lines 333–412): `material_provenance="ASSUMED..."` and
`mass_fill_fraction_assumption` (100%-fill crystalline solid at
`l_geometric_m`) are hardcoded into every returned dict regardless of the
caller's inputs — they describe the `h_eff`/mass/area chain's own
geometric-length assumptions, which depend only on `l_geometric_m`
(`=r·DX_M`, unchanged in kind between this cycle and every prior
invocation) and never on how `p_abs_w` was computed upstream. Using
exp-106's real, ledger-measured `sigma_ext`/`abs_ext_ratio` in place of
exp-105's `Q_ext`-invariance placeholder changes only the **numerator**
(`p_abs_w`) fed into the chain — the denominator side (`h_eff`, `mass_kg`,
`area_m2`, and the idealizations attached to them) is structurally
untouched by that substitution, exactly as the module's own "mixed by
design" docstring states. NOTES.md's own Idealizations section states this
correctly ("carries its own standing idealizations unchanged... not
re-litigated this cycle") — confirmed accurate, not merely asserted.

## 4. The gap: a thermodynamically-motivated margin-erosion projection this cycle could have made and did not

This cycle is the **first** to compute a real, ledger-measured thermal row
for the fixed-abs family at any r (my own Phase-2 steel-man named this as
standing debt; it is now closed). That also means it is the first cycle
with **two real fixed-abs data points** (r=156, r=312) to check for a
trend — and the trend is not benign.

**The two families are declining at genuinely different rates, and the
difference has a clean thermodynamic explanation.**

```
selfsim:  margin(156)/margin(312) = 343.40/171.87 = 1.998   (r doubled -> margin halved, exactly)
fixedabs: margin(156)/margin(312) = 262.37/117.46 = 2.234   (r doubled -> margin cut by 2.234x)
```

Why: at this bench length scale (`l_geometric_m` = tens of nanometers ×
`r`, i.e. microns), `mixed_length_scale_regime`'s own `dp_dt` is
conduction-dominated (`h_eff=k_air/l_geometric_m` swamps the radiative term
`4·ε·σ_SB·T³` by roughly three orders of magnitude at these `l_geometric_m`
values — a direct consequence of T5/T8's own standing "bench-scale, not
witness-scale" idealization). That makes `dp_dt ∝ area_m2·h_eff =
l_geometric_m²·(k_air/l_geometric_m) ∝ r` (linear in `r`), independent of
family. For the **self-similar** family, `sigma_ext` scales exactly
linearly with `r` by construction (κ-scaling preserves every length
ratio), so `p_abs_w ∝ σ_ext²·abs_ext_ratio ∝ r²` (with `abs_ext_ratio`
essentially flat, 0.5180→0.5190) — giving `dt_ss = p_abs_w/dp_dt ∝ r`
exactly, hence `margin ∝ 1/r` exactly. The data confirms this to 3 sig
figs (`1.998` vs. the exact `2.0` a pure `1/r` law predicts).

The **fixed-abs** family does not scale this way, because `ABS_THICKNESS`
is held constant (48 cells) while `r` grows — MATERIALS' own
"growing-electrical-thickness" mechanism, named at exp-105 and never
retired. That shows up directly in the ledger: `sigma_ext_fixedabs` grows
**super-linearly** in `r` (a `2.126×` increase for an exact `r`-doubling,
vs. self-similar's exact `2.000×`), while `abs_ext_ratio_fixedabs`
mildly declines (`0.4992→0.4936`, −1.1%). Net effect: `p_abs_w_fixedabs ∝
r^{2.16}` (not `r²`), so `dt_ss_fixedabs ∝ r^{1.16}` and
`margin_fixedabs ∝ r^{-1.16}` — a steeper decline than self-similar's
clean `r^{-1}`, and the data confirms the exponent exactly
(`log2(2.234) = 1.159`).

**Extrapolating this observed exponent one more octave (a hypothetical
r=624, already on Iteration 83/84's own standing queue as "a fourth
r-point to break the two-point shape-fit degeneracy," for an unrelated
reason):**

```
projected margin_selfsim(624)  ≈ 171.87 / 1.998  ≈ 86.0×   (comfortable)
projected margin_fixedabs(624) ≈ 117.46 / 2.234  ≈ 52.6×   (right on the 50x floor)
```

The pre-registered 50× falsification floor this cycle adopted (per my own
Phase-2 mandatory fix, "would catch a further order-of-magnitude erosion
the `<10×` band could not") is not a comfortably-distant tripwire for this
one cell — on the observed two-point trend, it is almost exactly where the
NEXT established r-point in this bridge family would land. This is not
asserted as a confirmed law (two points cannot distinguish a genuine
power-law exponent from noise or a construction-specific artifact — the
same epistemic caution R15/R17 already apply to this exact bridge's
`shape_ratio` question) — but it is a real, falsifiable, thermodynamically
grounded projection sitting in already-filed data, and it was not made
anywhere in this cycle's record.

## 5. Other findings

- **`i_incident` anchor unchanged, correctly reused.** The r=78 anchor
  constants (`SIGMA_EXT_78`, `P_ABS_78`, `RATIO_ABS_EXT_78=0.51`) are
  identical to every prior T28-bridge cycle's citation (T9's own
  established value) — no drift, confirmed by direct comparison against
  exp-105's own citation of the same three constants.
- **Item 1's hollow-vs-PEC-cored delta is thermodynamically consistent with
  Item 3's own `abs_ext_ratio` values.** `abs_ext_ratio_hollow` and
  `abs_ext_ratio_pec_cored_exp106` differ by `2.97×10⁻⁵`/`2.47×10⁻⁵`
  (r=156/312) — two-to-three orders of magnitude below the `abs_ext_ratio`
  values themselves (~0.49–0.50) that Item 3's own `p_abs_w` is built
  from, confirming the core-fill choice cannot materially perturb Item 3's
  own thermal numbers even though Item 3 uses the PEC-cored `abs_ext_ratio`
  (not the hollow one) throughout — the two items are self-consistent, not
  merely adjacent.
- **Item 4's own r=312 finding (article-scene numerator noise-floor
  contamination worsening with r, 18.3%→26.8%) is a different channel
  (`kappa_window`'s coherent-intensity numerator) than Item 3's own
  `sections.widths()`-derived `sigma_ext`/`sigma_abs`** — I checked whether
  Item 4's flagged contamination could itself be inflating Item 3's own
  `sigma_ext` reading at r=312 and found no shared code path:
  `sections.widths()` (Item 3's own source) integrates a phasor-magnitude
  field over the `box_a`/`box_b` extinction boxes, never touching
  `floor_gate_window()`'s own `behind`-window `|Ez|²` block Item 4 tests —
  independently confirmed by direct read of `lab/sections.py`'s call
  signature difference. Item 3's own numbers are not at risk from Item 4's
  finding.

## 6. Ranked top-3 candidate directions for Iteration 85 (THERMODYNAMICS' own charter)

1. **Pre-register the margin-erosion projection (§4) as a standing
   falsifiable Tier item, explicitly attached to whichever cycle next
   extends this bridge to a genuine fourth r-point** (already queued for
   an unrelated shape-fit reason). State the two-point power-law caveat
   plainly, but require the actual measured margin at that r be checked
   against both the `r^{-1}` (selfsim) and `r^{-1.16}` (fixedabs)
   extrapolations from this cycle's own two points before either family's
   thermal row is filed as "UNDETECTABLE, comfortable" without comment —
   at the fixed-abs family's own observed rate, the very next octave is
   where this program's own pre-registered 50× floor was built to fire.
2. **Source a real `k_solid`/`emissivity`/density for the actual candidate
   material class at these two r, and run `front_surface_conduction_
   correction`/`biot_number` on the real (not placeholder) fixed-abs
   ledger data** — this cycle's Item 3 uses only the lumped
   (lowest-fidelity) chain; the material-provenance-honest front-surface
   correction machinery (Iteration 40/41) has never been applied to any
   fixed-abs cell, and the growing-electrical-thickness mechanism §4
   identifies is exactly the kind of geometry where a front-surface (not
   lumped) correction could matter most.
3. **Resolve the mandatory-fix-1 "three-way ambiguous" reclassification
   this seat flagged at exp-106 (still open per that cycle's own
   Iteration-83 entry, `run.py`'s own code fix deferred to Iteration 84)**
   — this cycle did not touch `shape_ratio_fixedabs`'s classification
   logic at all (correctly out of scope), so the fix remains outstanding
   and should not silently roll past a second deferral now that R24's own
   two-strike clause is on the books.

*(Tier 0's retirement of the `delta_scene` R3-vs-R4-vs-R5 question is
outside this seat's charter to re-adjudicate; I note only that nothing in
Item 3's own thermal-margin finding bears on that question — the two
pieces of this cycle's work remain, as designed, structurally
independent.)*
