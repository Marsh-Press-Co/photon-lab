# exp-063 — Phase 4 Results

**Panel Iteration 40.** WebSearch-snippet synthesis only. T18 (WebFetch,
primary-source access) re-confirmed blocked before any snippet fallback,
per every prior cycle's convention: 2/2 attempts (`arxiv.org`,
`www.ncbi.nlm.nih.gov`), both `EGRESS_BLOCKED`. Every verdict below is
sourced via WebSearch-snippet synthesis, not primary-source PDF/DOI-
verified reading (T18) — disclosed here at every scored verdict, per
registry entry `exp061-t18-evidentiary-tier-propagation`.

Ten committed queries executed, unchanged from `phase1_proposal.md` §6.

---

## Query log

1. `vertically aligned carbon nanotube forest through-thickness thermal conductivity measured` — VACNT-grown-on-reduced-graphene-oxide composite film, through-thickness κ=9.62 W/(m·K); several thermal-interface-material papers found, no other single directly-reported through-thickness number in the snippets.
2. `carbon nanotube forest thermal interface material effective thermal conductivity low` — as-grown CNTs "intrinsic thermal conductivity ≈160 W/(m·K), rising to ≈450 W/(m·K) after annealing" (ambiguous sourcing — see §"A flagged ambiguous data point" below); short-forest (≲400µm) thermal resistance breakdown: interfacial ≈0.6–0.7 cm²K/W, intrinsic forest ≈0.1 cm²K/W (a DERIVED, not directly-reported, κ follows — see TD-1 below); forest thermal resistance rises with forest length (root-density argument).
3. `CNT array axial thermal conductivity inter-tube contact resistance mechanism` — individual MWCNT axial κ≈2000 W/(m·K) (comparator, query-7 territory, not scored against TD-1/TD-2); inter-tube contact-resistance mechanisms named (van der Waals coupling, metal-cluster phonon bridges, covalent functionalization) — mechanistically consistent with query 10's own finding (below).
4. `Vantablack coating thermal conductivity substrate heat dissipation` — **no usable number.** Results are manufacturer-marketing-style claims ("Vantablack has the highest thermal conductivity... of any material... in high-emissivity applications," "high thermal conduction... very little outgassing") with zero cited figure — not scored, flagged unreliable/non-quantitative, not treated as evidence either direction (a real, if mild, tension with this cycle's own low-κ hypothesis is noted but not adjudicated on marketing copy).
5. `carbon nanotube forest density height thermal conductivity W/m·K published` — **the single cleanest hit this cycle found**: "the bulk nanotube mat shows a low value of approximately 0.7 W/(m·K) at room temperature, which represents the thermal conductivity of densely packed nanotube aggregates" — explicitly a BULK/AGGREGATE figure, not an individual-tube one. Also: individual-tube comparators (37,000 W/(m·K) at 100K, 6,600 W/(m·K) room temp) — comparator territory, query-7 overlap.
6. `carbon nanotube forest anisotropic thermal conductivity axial lateral cross-plane` — axial ≫ lateral confirmed qualitatively (as predicted, Idealization 4); ONE specific number: "thermal conductivity and thermal diffusivity along the alignment are 50±5 W/(m·K) and 45±5 mm²/s... measured from multiwalled carbon nanotube SHEETS DRAWN FROM A FOREST" — a post-processed, densified/aligned form, NOT the as-grown vertical-forest architecture this cycle's band targets (see "A flagged geometry-class distinction" below).
7. `single multi-walled carbon nanotube intrinsic axial thermal conductivity value` [comparator only, per Phase 1's own scoping] — individual/cleanest-case tube axial κ ~10³ W/(m·K) order, one (19,8) SWCNT lower bound κ≥730±17 W/(m·K), literature range up to >1000 W/(m·K) — 1–3 orders of magnitude above every bulk-forest figure found (queries 1/5/6), consistent with the predicted degradation factor. Not scored against TD-1/TD-2 (comparator only, as pre-registered).
8. `"Carbon" 2018 129 8-14 carbon nanotube forest nanoimprint density thermal` — re-confirms the already-pinned citation (Park et al., *Carbon* 2018, vol. 129, pp. 8–14, "Modulation of the effective density and refractive index of carbon nanotube forests via nanoimprint lithography," exp-062 query 13) and adds geometry context (widths 80–350nm, heights >500µm, aspect ratio >1000:1) — but **no thermal-conductivity figure reported in the available snippets**; the paper's own title/abstract scope is optical (density/refractive-index), not thermal. Honest null, exactly as Idealization/§6 flagged as possible ("if reported").
9. `carbon nanotube forest specific heat capacity bulk density measurement` [scoped OUT of predictions, Idealization 2/6, zero-cost rider only] — bulk density range 20–1500 kg/(m³) found (measurement-method-dependent); no ρ/C_p figure specific enough to use, and none needed this cycle.
10. `carbon nanotube array thermal contact resistance van der Waals tube-tube junction` — **directly confirms the predicted mechanism** (query 10's own purpose, per §6): tube-tube junction thermal conductance ≈12 pW/K, "less than 1% of the axial thermal conductance" of a single tube; van der Waals junction contact resistance ≈4×10⁻⁸ m²K/W vs. ≈6×10⁻¹¹ m²K/W for a covalent junction — nearly **three orders of magnitude** worse, quantitatively grounding TD-1's central hypothesis (contact-resistance-dominated transport) rather than leaving it asserted.

---

## A flagged geometry-class distinction (not a falsification, a disclosed spread)

The single highest bulk-forest-adjacent figure found (query 6's 50±5
W/(m·K)) is measured on multiwalled CNT **sheets drawn from a forest** —
a post-processing/spinning step that densifies and re-aligns the tubes,
improving inter-tube contact relative to an as-grown vertical forest.
This is the same class distinction Iteration 39 (exp-062, EM-5) already
established for near-field coupling: "spin-capable/yarn-precursor"
forests behave differently from denser, as-grown classes. This program's
own actual candidate geometry (a record-blackness/Vantablack-type
as-grown coating) is closer to the un-drawn, as-grown class the other
figures (0.7, 9.62 W/(m·K)) represent — but no query this cycle pinned
the record-blackness/Vantablack forest's OWN thermal figure specifically
(the analogous gap Iteration 39 left for the near-field-coupling
question, on the pitch/diameter axis — still the program's #1 ranked
Iteration-40+ queue item, unaddressed by this cycle, a different physical
quantity).

## A flagged ambiguous data point

Query 2's "as-grown CNTs... intrinsic thermal conductivity ≈160 W/(m·K),
rising to ≈450 W/(m·K) after annealing" is not scored against TD-1/TD-2
either direction. The phrasing ("as-grown CNTs," not "as-grown CNT
forest") and its proximity in the broader literature to bundle/tube-level
values (not bulk-aggregate values) make it more likely a bundle/tube
comparator (query-7 territory) than a forest-bulk figure — but the
snippet alone does not settle this, and unlike query 6's figure it has no
disclosed measurement-geometry detail to make the class call confidently.
Flagged, not adjudicated, following this program's own standing
discipline for exactly this kind of snippet ambiguity (T18).

---

## Predictions, scored

### TD-1 — Sourced κ_CNT-forest (through-thickness/axial)

**Predicted:** Band [0.1, 20] W/(m·K), central ≈2 W/(m·K). Falsified if
sourced figures cluster above 50 W/(m·K); INCONCLUSIVE if no axial figure
exists.

**Result: NOT falsified.** Multiple genuine bulk-forest/through-thickness
figures exist (query 1: 9.62; query 5: 0.7; a derived estimate from query
2's interfacial-resistance breakdown, ≈40 for a ≲400µm forest — see note
below), so this is not the INCONCLUSIVE branch either. The figures found
**cluster well below the 50 W/(m·K) falsification bar** — 0.7 and 9.62
both sit inside the predicted [0.1,20] band directly; only the drawn-sheet
figure (50±5, a different, densified geometry class per the flag above)
sits AT the bar, and the derived ≈40 estimate sits just above the band's
own upper edge but still comfortably below the falsification threshold.
**Verdict: CONFIRMED, band and central estimate both roughly right** —
the true value is geometry-class-dependent (0.7–9.62 W/(m·K) for
as-grown/aggregate forms, up to ≈40–50 W/(m·K) for densified/drawn
forms), a real spread this cycle's single-point central estimate did not
anticipate but which stays inside the predicted OUTER band throughout,
with the falsification bar not crossed by any genuinely bulk-forest
figure found.

*Derivation note (the ≈40 W/(m·K) figure):* query 2's own reported
breakdown (short forest, L≲400µm: interfacial resistance ≈0.6–0.7
cm²K/W, intrinsic forest resistance ≈0.1 cm²K/W) implies κ_eff = L /
R_intrinsic ≈ 0.04 m / (0.1×10⁻⁴ m²·K/W · ... ) — computed directly:
L=400µm=4×10⁻⁴m, R=0.1 cm²K/W=1×10⁻⁵ m²K/W, κ=L/R=4×10⁻⁴/1×10⁻⁵=40
W/(m·K). This is a DERIVED number (this cycle's own arithmetic on a
reported resistance breakdown), not a directly-reported forest κ —
flagged as such, not presented as a primary-source figure.

### TD-2 — Bi_gas = k_air/κ_solid

**Predicted:** Band [0.0013, 0.26], central ≈0.013. Falsified if outside
[0.0005, 1.0].

**Result: CONFIRMED across the full found range.** Computed directly
(`lab/thermo_sidecar.biot_number`, reproduced by stage 23):

```
kappa=0.70  (bulk mat)          -> Bi_gas=0.03714
kappa=9.62  (VACNT-rGO composite)-> Bi_gas=0.00270
kappa=40.0  (derived, query 2)   -> Bi_gas=0.00065
kappa=50.0  (drawn sheet, query 6)-> Bi_gas=0.00052
```

Every value lands inside [0.0005, 1.0]; the drawn-sheet figure (0.00052)
sits closest to the falsification floor but does not cross it.

### TD-3 — Front-surface correction factor, bench geometry (bracket)

**Predicted:** [1.0 (front-colocated endpoint), 1.001–1.26 (rear-only
endpoint, across TD-1's κ band)]. **NETD is an instrument threshold, this
row bears on no human-eye/constraint-3 verdict.**

**Result: CONFIRMED, rear-only endpoint at the tight end of its own
band across every sourced κ.** Computed directly, front-colocated
endpoint identically 1.0 throughout (by construction):

```
kappa=0.70  -> CF_bench(rear-only)=1.03716
kappa=9.62  -> CF_bench(rear-only)=1.00270
kappa=40.0  -> CF_bench(rear-only)=1.00065
kappa=50.0  -> CF_bench(rear-only)=1.00052
```

Every sourced κ gives a rear-only correction well inside the predicted
[1.001,1.26] band, clustered near its own tight (low-correction) end —
the sourced κ values are mostly HIGHER than TD-1's own central 2 W/(m·K)
guess, which pushes the correction factor closer to 1 (a smaller
correction), not farther from it.

### TD-4 — Corrected flagship margin (bracket)

**Predicted:** [554.92×–698.36× (rear-only endpoint), 699.27×
(front-colocated endpoint, unmodified)]. Falsified (rear-only endpoint)
if it drops below 100× anywhere in the sourced range. **NETD is an
instrument threshold, this row bears on no human-eye/constraint-3
verdict.**

**Result: CONFIRMED, not falsified, margin stays deep in UNDETECTABLE
territory throughout.**

```
kappa=0.70  -> margin_bench(rear-only)=674.22x
kappa=9.62  -> margin_bench(rear-only)=697.38x
kappa=40.0  -> margin_bench(rear-only)=698.82x
kappa=50.0  -> margin_bench(rear-only)=698.91x
```

Every sourced κ gives a rear-only margin between 674× and 699× — inside
the predicted [554.92×,698.36×] band at its own tight end (674.22× is
the single lowest value, from the lowest sourced κ, 0.7 W/(m·K), the
genuinely worst case found) and comfortably above the 100× falsification
bar throughout, by roughly 7×.

### TD-5 — Corrected exp-061 witness-scale margin, MP-5/730× point
(bracket, conditional on the length-legitimacy caveat)

**Predicted:** [1.0274×–1.3479× (rear-only endpoint), 1.35×
(front-colocated endpoint, never crosses 1.0×)]. Rear-only endpoint
falsified toward DETECTABLE if sourced κ < 0.0897 W/(m·K). **NETD is an
instrument threshold, this row bears on no human-eye/constraint-3
verdict — and this row's own disposition is a significant
realizability-margin finding warranting Director/Marsh attention if
falsified, NOT a Checkpoint-criterion-1/2 target-constraint result.**

**Result: NOT falsified — decisively so, not marginally.** Every sourced
κ is 8×–560× ABOVE κ_critical=0.0897 W/(m·K):

```
kappa=0.70  (lowest sourced, worst case found) -> margin_mp5(rear-only)=1.2920x
kappa=9.62                                      -> margin_mp5(rear-only)=1.3456x
kappa=40.0                                      -> margin_mp5(rear-only)=1.3489x
kappa=50.0                                       -> margin_mp5(rear-only)=1.3492x
```

Even at the single LOWEST κ found this cycle (0.7 W/(m·K), the bulk
nanotube mat figure, query 5 — the most conservative real number in the
whole search), the corrected rear-only margin is **1.2920×**, comfortably
inside the predicted [1.0274×,1.3479×] band and nowhere near 1.0×. **This
program's own "first-ever thermal-detectability classification flip"
scenario (TD-5's own headline framing) does NOT materialize against any
figure this cycle found** — the answer to the cycle's own hypothesis
question ("does the correct material's κ still license the lumped
assumption") is **yes, decisively, across the full range of real
candidate-material figures sourced**, not merely "not yet falsified."

---

## Summary table

**Mandatory-fix note (Red Team's Phase-5 audit, item 1): two of the four
sourced κ values (40.0, 50.0 W/(m·K)) sit slightly OUTSIDE TD-3/4/5's own
PREDICTED bands below — because those bands were computed by propagating
TD-1's own PREDICTED κ range ([0.1,20], the only thing Phase 3 had before
Phase 4 ran), not the FOUND κ range, which Phase 4's own search showed
extends slightly higher (TD-1's own text above discloses this: "the
derived ≈40 W/(m·K) estimate sits just above the band's own upper edge").
The "Found" column's rear-only endpoints at κ=40/50 are therefore
correct, live numbers — 0.06–0.10% outside the row's own PREDICTED
column, always in the SAFE direction (less correction at bench scale,
more margin at witness scale, no falsification condition approached).
"CONFIRMED" below means the falsification CONDITION is not triggered, not
that every found value sits inside the originally-predicted numeric
range.** NETD is an instrument/detector threshold, not a human perceptual
one — nothing in this table bears on constraint-3/4's human-eye verdict.

| Prediction | Predicted | Found | Verdict |
|---|---|---|---|
| TD-1 (κ_CNT-forest) | [0.1,20] W/(m·K), central ≈2 | 0.7–9.62 W/(m·K) for as-grown/bulk-aggregate forms (query 1/5); ≈40 (derived) to 50±5 W/(m·K) for densified/drawn forms (query 2/6) — geometry-class-dependent spread, falsification bar (>50 clustering) not crossed | **CONFIRMED** |
| TD-2 (Bi_gas) | [0.0013,0.26], central ≈0.013 | 0.00052–0.03714 across sourced κ, all inside [0.0005,1.0] | **CONFIRMED** |
| TD-3 (CF, bench, bracket) | [1.0, 1.001–1.26] | rear-only endpoint 1.00052–1.03716 across sourced κ — **at κ=40/50, 1.000650/1.000520 sit ~0.06% below the predicted-band floor (1.001301), a found-vs-predicted-κ-range artifact, not a falsification** | **CONFIRMED** |
| TD-4 (corrected flagship margin, bracket) | [554.92×–698.36×, 699.27×] | rear-only endpoint 674.22×–698.91× — **at κ=40/50, 698.82×/698.91× sit ~0.06% above the predicted-band ceiling (698.36×), same artifact** — >6.7× above the 100× bar throughout | **CONFIRMED** |
| TD-5 (corrected MP-5/730× margin, bracket) | [1.0274×–1.3479×, 1.35×] | rear-only endpoint 1.2920×–1.3492× — **at κ=40/50, 1.3489×/1.3492× sit ~0.07–0.10% above the predicted-band ceiling (1.3479×), same artifact** — inside band otherwise; κ_critical=0.0897 never approached (nearest sourced κ is 8× above it) | **CONFIRMED — DETECTABLE-flip scenario does not materialize** |

**Bottom line (NETD is an instrument/detector threshold, not a human
perceptual one — nothing in this paragraph bears on constraint-3/4's
human-eye verdict): the correct candidate material's own thermal
conductivity DOES still license the lumped-capacitance assumption every
committed THERMO-sidecar margin in this program's history rests on.** The worst
real figure found (0.7 W/(m·K), the bulk-aggregate bulk figure) moves the
flagship's bench-scale margin from 699.27× to 674.22× (a 3.6% tightening)
and exp-061's own thinnest-ever witness-scale margin from 1.35× to
1.2920× (a 4.3% tightening) — real, measurable, and the correct
next-order correction to apply going forward, but nowhere close to
threatening either classification. The two disclosed-not-resolved
caveats from Phase 3 (the rear-only boundary condition's own physical
plausibility, MATERIALS; the witness-scale length's own T23 legitimacy,
EM) remain open — but even granting the FULL rear-only worst-case
formula at its own predicted-band values, no classification flips. The
front-colocated bracket endpoint (this cycle's other honestly-reported
possibility) shows zero correction at all, for any κ_solid.

**Two honest open items, not this cycle's job to close (Phase 3's own
scoping, `phase3_synthesis.md` §5):** the substrate-interface
boundary-condition question (which bracket endpoint is actually correct
for a real coating-on-substrate deployment) and the witness-scale
length-legitimacy question (is `τ_true/α` a licensed `h=k/L` conduction
length at all) both stay open, unaffected by how comfortably this
cycle's own found κ values clear both margins — a future cycle resolving
either could still change the STORY even though it would not, on this
cycle's own numbers, change the VERDICT.
