# exp-063 — Phase 1 Proposal: The Real Candidate Material's Own Thermal
# Conductivity, and Whether It Still Licenses a Lumped-Capacitance ΔT

**Panel Iteration 40. Lead: THERMODYNAMICS, by rotation.** T1 escape route:
**N/A** — a literature/analytic realizability-and-instrument continuation,
the exp-036/037/054/061/062 class: zero constraint-1/2/3/4 metric scored,
zero FDTD, zero new network access beyond the standing T18-blocked
WebSearch-snippet methodology.

---

## 1. Scope narrative (≤300 words)

Every THERMO-sidecar UNDETECTABLE verdict this program has ever issued —
`graded_black_shell_flagship`'s bench-scale 699.27× margin (exp-057) and
exp-061's own freshest, thinnest-ever witness-scale margins (1.35×–3.79×,
MP-5's found thickness range) — computes steady-state ΔT from a **lumped**
(uniform-temperature) model whose external heat-loss coefficient
`h_eff=k_air/L` is sourced, but whose internal SOLID thermal conductivity
`κ_solid` never enters the sidecar's own committed code at all
(`mixed_length_scale_regime` takes no `κ_solid` argument). Every Biot-number
check this program has run to gauge whether "uniform temperature" is even a
valid idealization (Iteration 22 Attack 6, Iteration 23's own Maxwell-
Garnett fill-fraction table) used **silicon's κ=148 W/(m·K) — flagged
`ASSUMED`, provenance terminating unsourced (T18), since Iteration 25** —
a generic kinetics-host placeholder chosen before this program's own
realizability line (exp-052→061→062) pinned the actual leading candidate
material class: a CNT-forest/Vantablack-type coating. Real CNT forests are
well documented as exceptionally POOR thermal conductors in their
growth-axis (through-thickness) direction, despite individual nanotubes'
own extreme intrinsic conductivity — a textbook consequence of weak,
sparse inter-tube van der Waals contacts, the same reason CNT forests are
studied as thermal-interface materials in the first place, not assumed
away.

This cycle sources that number for the first time and asks the THERMO
question nobody has: does the *correct* material's κ still license the
lumped assumption every committed margin rests on, or does absorbed power
pile up at the illuminated front surface faster than a poor conductor can
spread it — producing a peak surface ΔT (and IR emission) above the
sidecar's own uniform-body estimate? A closed-form correction factor is
derived below that answers this exactly, at zero new FDTD cost, and is
applied to both the flagship's bench-scale margin and exp-061's own
fragile witness-scale margin — the two places in this program's record
where the answer could actually move a classification.

---

## 2. T1 escape route: N/A

No mechanism is proposed. This is a model-fidelity / instrument-trust
cycle on the standing THERMO sidecar, the Iteration-20/22/25/27/29/31/34
class: it sharpens (or falsifies) already-issued UNDETECTABLE verdicts,
using the same T18-blocked WebSearch-snippet evidentiary tier this
program's realizability line has used since Iteration 13.

---

## 3. Parameter table

| Knob | Value | Source / status |
|---|---|---|
| `k_air` | 0.026 W/(m·K) | established bench constant (exp-045/run.py:194), unchanged |
| Radiative linearization | `4·ε·σ·T_amb³`, ε=0.9, T_amb=293.15K, σ=5.670374419×10⁻⁸ W/(m²K⁴) | established bench constants (`thermo_sidecar.SIGMA_SB`), unchanged |
| Silicon proxy (superseded, for comparison only) | ρ=2330 kg/m³, C_p=700 J/(kg·K), **κ=148 W/(m·K)** | `ASSUMED — provenance terminates unsourced (T18)`, exp-054/057's own `MATERIAL_PROVENANCE_NOTE`; the object of this cycle's correction, not reused as ground truth |
| **κ_CNT-forest (through-thickness/axial)** | **predicted band [0.1, 20] W/(m·K), central ≈2 W/(m·K)** | **NOT YET SOURCED — this cycle's own Phase-4 WebSearch target** (see §6); general-domain-knowledge estimate, 1–3 orders of magnitude below both silicon (148) and individual-MWCNT intrinsic axial values (~200–3000 W/(m·K), a comparator, not the quantity used), consistent with the CNT-forest thermal-interface-material literature's well-known contact-resistance-dominated transport |
| Bench-scale geometry (`graded_black_shell_flagship`) | `L=l_geometric_m=r_out=78 cells × 30nm = 2.34×10⁻⁶ m`; `P_abs=1.7409×10⁻¹² W` (exp-057, unchanged) | exp-043/057, established, reused verbatim |
| Witness-scale geometry (exp-061's MP-5 disposition) | `L∈{331.2, 429.1, 538.6, 1051.2} µm` at MP-5 multiples {230×,298×,374×,730×}; margins {3.79×,2.98×,2.42×,1.35×} vs NETD-lo=0.020K (unchanged inputs) | exp-061 THERMO disposition, established, reused verbatim |
| NETD band | (0.020, 0.050) K | exp-043 docket #7, sourced, unchanged |
| New code (proposed) | `lab/thermo_sidecar.py::biot_number(k_air, k_solid)`, `front_surface_conduction_correction(k_air, l_geometric_m, k_solid, emissivity, t_ambient_k)` | promotes the informal, never-code-committed Biot arithmetic (Iteration 22/23) to trust-suite-gated code; new stage, ≥1 absolute-identity gate (κ_solid→∞ limit recovers `mixed_length_scale_regime`'s own `dt_ss_full` exactly, factor→1) |

---

## 4. The closed-form front-surface correction

**Model (deliberately worst-case, disclosed as Idealization 1):** steady
1D planar conduction. Absorbed power `P_abs` enters uniformly over the
illuminated FRONT surface (area `A=L²`, the sidecar's own `iso_xsec_sq`
convention); it must conduct across the full thickness `L` through
`κ_solid` before any of it can leave via the already-established combined
gas-conduction + radiation channel, idealized as acting ONLY at the far
(rear) boundary. This maximizes, not merely estimates, the front-vs-lumped
gap — a real object loses some heat locally near the front too.

```
dT_ss(lumped)      = P_abs / (A · dp_dT_area),   dp_dT_area = h_eff + 4εσT_amb³   [= mixed_length_scale_regime's own dt_ss_full]
dT_front-to-rear    = P_abs · L / (A · κ_solid)   [ordinary 1D Fourier conduction resistance]
dT_front(corrected) = dT_ss(lumped) + dT_front-to-rear
                     = dT_ss(lumped) · [ 1 + dp_dT_area · L / κ_solid ]
                     = dT_ss(lumped) · [ 1 + (k_air/L + 4εσT_amb³)·L / κ_solid ]
                     = dT_ss(lumped) · [ 1 + k_air/κ_solid + 4εσT_amb³·L/κ_solid ]
CORRECTION FACTOR   = 1 + Bi_gas + Bi_rad(L),   Bi_gas ≡ k_air/κ_solid (length-invariant, matches
                       the already-established Iteration-22 Attack-6 identity exactly),
                       Bi_rad(L) ≡ 4εσT_amb³·L/κ_solid (length-DEPENDENT, new this cycle —
                       negligible at bench scale, non-negligible at witness scale)
```

Computed by direct invocation (R4), not hand-typed:

```
k_air=0.026 W/mK, 4*eps*sigma*T_amb^3=5.14261 W/(m^2K), Bi(silicon,148 W/mK)=1.75676e-4

kappa=20.0 W/mK: Bi_gas=0.00130  CF(bench,L=2.34um)=1.0013  CF(MP5-730x,L=1051.2um)=1.0016
kappa=2.0  W/mK: Bi_gas=0.01300  CF(bench)=1.0130            CF(MP5-730x)=1.0157
kappa=0.5  W/mK: Bi_gas=0.05200  CF(bench)=1.0520            CF(MP5-730x)=1.0628
kappa=0.1  W/mK: Bi_gas=0.26000  CF(bench)=1.2601            CF(MP5-730x)=1.3141
```

`κ_solid` for zero correction (factor→1) crossing to margin=1 at the
MP-5/730× point: solving `CF=1.35` gives **κ_critical ≈ 0.0897 W/(m·K)** —
just below this cycle's own predicted band floor (0.1 W/(m·K)), a real,
literature-plausible falsification boundary, not a remote one.

---

## 5. Falsifiable predictions — committed BEFORE any search runs

| # | Claim | Predicted outcome | Falsification condition |
|---|---|---|---|
| **TD-1** | Sourced κ_CNT-forest (through-thickness/axial) | Band **[0.1, 20] W/(m·K)**, central ≈2 W/(m·K) — 1–3 orders of magnitude below silicon's 148 W/(m·K) | Falsified if sourced figures cluster above 50 W/(m·K) (silicon-comparable transport, contradicting the contact-resistance-dominated picture) or if no through-thickness/axial figure exists in the literature at all (scored INCONCLUSIVE, not falsified, in that case) |
| **TD-2** | Bi_gas = k_air/κ_solid, using the sourced κ | Band **[0.0013, 0.26]**, central ≈0.013 — 7×–1500× the established `Bi(silicon)=1.7568×10⁻⁴` | Falsified if the sourced κ places Bi_gas outside [0.0005, 1.0] |
| **TD-3** | Front-surface correction factor at the flagship's bench-scale geometry (`L=2.34µm`) | Band **[1.001, 1.26]**, central ≈1.013 — a real but modest (≤26%) correction | Falsified if the sourced κ drives the factor above 2× (would mean the bench-scale UNDETECTABLE classification itself is genuinely at risk, not merely tightened) |
| **TD-4** | Corrected flagship margin (699.27× ÷ TD-3's factor) | Band **[555×, 698×]** — stays UNDETECTABLE by a comfortable margin at every point in TD-1's band | Falsified (classification-relevant) only if the corrected margin drops below 100× anywhere in the sourced range — would newly rank the flagship's bench-scale margin as a program concern for the first time |
| **TD-5** | Corrected exp-061 witness-scale margin at the MP-5/730× point (1.35× ÷ front-surface correction factor at `L=1051.2µm`) | Band **[1.03×, 1.35×]** — predicted to STAY UNDETECTABLE across TD-1's band, but with materially LESS headroom than the already-fragile 1.35× figure; the low edge (1.03×) sits within ~3% of the classification boundary | **Falsified toward DETECTABLE** if sourced κ_CNT-forest < **0.0897 W/(m·K)** (below TD-1's own predicted floor, but a real, checkable literature outcome, not a remote one) — would be this program's **first-ever thermal-detectability classification flip**, a Checkpoint-1/2-adjacent finding requiring escalation, not a routine margin update |

---

## 6. Search plan — queries committed before Phase 4 runs

Continuation-class search (T18 assumed still blocked, re-confirmed at
Phase 4 per every prior cycle's convention; WebSearch-snippet synthesis
only, disclosed at every verdict per the registered evidentiary-tier
discipline).

1. `vertically aligned carbon nanotube forest through-thickness thermal conductivity measured`
2. `carbon nanotube forest thermal interface material effective thermal conductivity low`
3. `CNT array axial thermal conductivity inter-tube contact resistance mechanism`
4. `Vantablack coating thermal conductivity substrate heat dissipation`
5. `carbon nanotube forest density height thermal conductivity W/m·K published`
6. `carbon nanotube forest anisotropic thermal conductivity axial lateral cross-plane`
7. `single multi-walled carbon nanotube intrinsic axial thermal conductivity value` [comparator only — quantifies the forest-vs-single-tube degradation factor, not used directly in TD-1..TD-5]
8. `"Carbon" 2018 129 8-14 carbon nanotube forest nanoimprint density thermal` [re-targets the already-pinned n_eff paper (exp-062 query 13) for a zero-marginal-cost thermal figure, if reported]
9. `carbon nanotube forest specific heat capacity bulk density measurement` [ρ/C_p follow-up, lower priority — see Idealization 5]
10. `carbon nanotube array thermal contact resistance van der Waals tube-tube junction`

Queries 1–6,8 target TD-1/TD-2 directly; 7 is a comparator/sanity check
(individual-tube κ should exceed forest κ by orders of magnitude — a
consistency, not falsification, check); 9 is scoped explicitly OUT of
this cycle's own predictions (Idealization 5) but costs nothing riding
the same dispatch; 10 targets the mechanism (contact resistance) that
would make TD-1's predicted low band physically motivated, not just
numerically asserted.

---

## 7. Idealizations — stated honestly

1. **1D planar, front-flux/rear-only-loss geometry — deliberately
   worst-case, not a realistic 3D solve.** A real object loses heat along
   its whole exposed surface, not only at a far boundary; this model
   therefore OVERESTIMATES the true front-vs-lumped gap. Predictions
   TD-3/4/5 are upper bounds on the correction, lower bounds on the
   corrected margin — if even this worst-case correction leaves a
   comfortable margin, a more realistic 3D treatment would leave more.
2. **Steady-state only.** `ρ`, `C_p` (and hence `τ_thermal`, transient
   behavior) are untouched this cycle — this proposal corrects `dt_ss_full`
   only. A full material-identity replacement (sourcing CNT-forest ρ/C_p
   too) is scoped OUT, a next-step, not annexed here (query 9 is a
   zero-cost rider only, not a committed prediction).
3. **κ_solid is sourced from general VACNT/CNT-forest thermal-interface
   literature, not necessarily the SAME specific record-blackness/
   Vantablack-class geometry this program's own α/n_eff figures cite**
   (exp-061/062's own "adjacent application class" caveat, inherited
   here for the analogous thermal quantity) — disclosed, not silently
   assumed identical.
4. **Isotropic κ_solid assumed for the 1D model; real CNT forests are
   strongly anisotropic** (axial ≠ lateral). The search plan targets
   through-thickness/axial figures specifically, the physically relevant
   direction for this geometry (front-to-rear conduction), but a source
   that does not distinguish direction will be flagged, not silently used.
5. **The radiative linearization `4εσT_amb³` is evaluated at ambient T,
   not the (unknown, slightly higher) front-surface T** — an established
   bench convention (`thermo_sidecar.py`), self-consistent since every
   ΔT computed anywhere in this program's record is µK–mK scale, ≪293K.
6. **Fill fraction / porosity is not re-applied on top of the sourced
   κ.** Published CNT-forest thermal-conductivity figures are already
   EFFECTIVE (as-grown, porous-structure) values, not a bulk-solid figure
   requiring a separate Maxwell-Garnett dilution step (T23's own
   Iteration-23 table applied Maxwell-Garnett to silicon's BULK κ diluted
   by an assumed fill fraction — a different, and for a fibrous
   contact-resistance-dominated medium, likely less physically apt,
   model than using the composite's own directly-measured κ). This
   methodological distinction is stated here for a future reader, not
   silently substituted for T23's own standing table.
7. **T18 (WebFetch) assumed still blocked** — Phase 4 re-confirms before
   any WebSearch-snippet fallback, per every prior cycle's convention.
8. **This proposal registers no new `lab/caveat_lint.py` machinery**
   beyond whatever new sourced numbers need a registry entry at Phase
   3/5 (the standing discipline) — the Iteration-40 zero-cost
   pre-flight rider (numeric/derivation-consistency-check tooling,
   already named with the Director as owner, Iteration 38 mandatory-fix
   item 6 / Iteration 39 Next item 3) is a separate, already-assigned
   item, not re-proposed or annexed here.
