# Phase 1 Proposal — Panel Iteration 44, candidate exp-067

**Seat: MATERIALS &amp; METAMATERIALS.** Lead item (locked, unconditional, per Red Team's Phase-5 final audit, `experiments/066-t27-block-main-settling-reverification/phase5_redteam_audit.md` §6, and LOGBOOK.md Iteration 43 M4): model the CNT-forest root-to-substrate thermal contact resistance, `R_contact`.

**Operational disclosure, stated up front, honestly, not buried:** this run is barred from WebSearch/WebFetch entirely. The dedicated 3–5 query dispatch Red Team's own Iteration-40 audit named as the correct remedy (`phase1_proposal.md`'s own Iteration-40 record; repeated verbatim in the exp-063 Phase-5 MATERIALS review, §8 item 1) is **not attempted this cycle**. This is a scope reduction, disclosed at the top, not a silent substitution — the real search stays queued (see §5).

---

## 1. Mechanism/scope narrative (293 words)

`R_contact` is the CNT-forest's root-to-substrate thermal contact resistance — the interface where the as-grown (or transferred) forest's base bonds to whatever it is grown or mounted on, distinct from the already-modeled inter-tube junctions inside the bulk. My own Iteration-40 Phase-5 review (`experiments/063-.../phase5_review_materials.md` §3) argued this interface is mechanistically plausible as a THIRD, worse-than-bracket-B thermal-resistance regime: the same weak, sparse van-der-Waals-type contact physics query 10 already measured for tube-tube junctions (contact resistance ≈4×10⁻⁸ m²K/W, ~3 orders of magnitude worse than a covalent junction; junction conductance &lt;1% of a single tube's own axial conductance) plausibly also governs the root's bond to a substrate — a real fabrication interface, never previously sourced or modeled here.

Under this cycle's explicit operational constraint — no WebSearch/WebFetch — the dedicated query dispatch Red Team's own audit specified for a directly-measured root/substrate figure cannot run. Disclosed here as a genuine scope reduction: instead, this proposal uses query 10's already-sourced inter-tube vdW contact-resistance figure as a physically-analogous PROXY/plausible-range anchor for the root-substrate interface — same underlying mechanism (weak, sparse vdW contact), a *different* specific interface — explicitly labeled an analogy-based estimate, never a direct root/substrate measurement. A real, dedicated literature search for that direct figure remains queued, named explicitly as still-open, carried to a future cycle once the search-tooling constraint clears — not declared closed by this analogy. `R_contact` enters the existing Biot-number/front-surface-conduction chain as a genuinely new SERIES thermal-resistance term, gated by the `R_contact→0 ⇒ CF→(bracket B)` identity Red Team specified.

---

## 2. Parameter table

**Physical derivation** (kept inside the existing chain's own normalization convention, per Red Team's instruction — not a reinvention of the rear-boundary physics): `front_surface_conduction_correction`'s existing model is a 1D series network — front-surface generation → solid conduction (`R_cond = L/κ_solid`) → rear-boundary loss to quiescent air + radiation (`R_rear = 1/h_combined`, `h_combined = k_air/L + 4εσT_amb³`) — normalized as `CF = 1 + R_cond/R_rear = 1 + Bi_gas + Bi_rad`. A bonded-substrate contact resistance is a **third series element** at the root, between the solid and whatever lies beyond (`R_contact`, units m²·K/W — matching the already-sourced figure's own units exactly, no conversion needed):

```
R_total = R_cond + R_contact + R_rear
CF_with_contact = R_total / R_rear = CF_bracket_B + R_contact · h_combined(L)
                                    = CF_bracket_B + Bi_contact
```

`Bi_contact(R_contact, L) = R_contact · (k_air/L + 4·ε·σ_SB·T_amb³)` — dimensionless, and **`R_contact→0 ⇒ Bi_contact→0 ⇒ CF→CF_bracket_B` exactly**, satisfying the required identity by construction, not by a separate limiting argument.

**Proposed `bonded_substrate_conduction_correction` signature** (composes `front_surface_conduction_correction`, does not reimplement it — this module's own established reuse discipline):

```python
def bonded_substrate_conduction_correction(
        k_air: float, l_geometric_m: float, k_solid: float, emissivity: float,
        r_contact_m2k_w: float, t_ambient_k: float = 293.15, *,
        length_provenance: str, diagnostic_only: bool = False,
        r_contact_provenance: str, r_contact_diagnostic_only: bool = False) -&gt; dict:
    ...
    base = front_surface_conduction_correction(
        k_air, l_geometric_m, k_solid, emissivity, t_ambient_k,
        length_provenance=length_provenance, diagnostic_only=diagnostic_only)
    h_combined = k_air / l_geometric_m + 4.0 * emissivity * SIGMA_SB * t_ambient_k**3
    bi_contact = r_contact_m2k_w * h_combined
    correction_factor = base["correction_factor"] + bi_contact
    return {"correction_factor": correction_factor, "bi_contact": bi_contact,
            "base_correction_factor_bracket_b": base["correction_factor"],
            "r_contact_m2k_w": r_contact_m2k_w, "h_combined_w_m2k": h_combined,
            "r_contact_provenance": r_contact_provenance, ...}
```

`r_contact_m2k_w = 0` is a first-class, always-runnable call — the gate's own regression case, not a special path.

**`r_contact_provenance` — a new guard, modeled on `length_provenance`'s own T23-closed pattern**, because R_contact's own sourcing needs exactly the same "declare, don't just document" discipline this program applies to lengths:

| Tag | Meaning | Requires |
|---|---|---|
| `"measured_direct"` | a real, sourced root/substrate contact-resistance measurement | licensed unconditionally |
| `"analogy_proxy_diagnostic"` | an analogous-mechanism proxy (e.g. this cycle's query-10 figure) — NOT a direct measurement | `r_contact_diagnostic_only=True`, else `ValueError` |

**Every R_contact value this cycle proposes is, honestly, `analogy_proxy_diagnostic`** — none is `measured_direct`. This is disclosed explicitly, not softened.

**Proposed test points** (units m²·K/W throughout):

| Point | R_contact | Provenance | Basis |
|---|---|---|---|
| Gate | 0 | n/a (identity check) | recovers bracket B exactly |
| Primary anchor | **4×10⁻⁸** | `analogy_proxy_diagnostic` | phase4_results.md query 10 (inter-tube vdW junction), the task's specified anchor |
| Primary band, 1–2 orders around anchor | [4×10⁻⁹, 4×10⁻⁶] | `analogy_proxy_diagnostic` | bounds sensitivity around the anchor, per the task's own ask |
| **Second, already-sourced anchor (my own catch, disclosed below)** | **6×10⁻⁵–7×10⁻⁵** (midpoint 6.5×10⁻⁵) | `analogy_proxy_diagnostic` | phase4_results.md query 2's own **"interfacial ≈0.6–0.7 cm²·K/W"** figure — already committed, in a forest/TIM-boundary context, ~3 orders above the primary anchor |
| Stress point A | 1×10⁻³ | `analogy_proxy_diagnostic`, flagged speculative | first point where bench-scale TD-4's 100× bar comes under threat (below) |
| Stress point B | 1×10⁻² | `analogy_proxy_diagnostic`, flagged speculative | near-adiabatic mechanical contact; witness-scale approach to 1.0× |

**A disclosed, unresolved units-legitimacy flag on the primary anchor itself**: query 10's own companion figure (junction thermal conductance ≈12 pW/K, an absolute per-junction quantity) suggests `4×10⁻⁸ m²·K/W` most plausibly describes a nanoscale, per-junction contact PATCH's resistance, not a macroscopically-averaged areal density across a real root/substrate footprint (which is sparse — the same reason bulk κ_CNT-forest is orders of magnitude below single-tube κ). Applying it directly as a macroscopic root/substrate figure may therefore be **optimistic** by an unknown, possibly large factor. Query 2's own already-committed "interfacial ≈0.6–0.7 cm²·K/W" figure is a macroscopically-reported areal resistance in a forest/TIM-boundary context — arguably the more directly-relevant analog, ~3 orders of magnitude worse than the primary anchor. Neither figure is adjudicated as "correct" here; both are carried as disclosed, already-sourced anchors, motivating why the test band above extends well past a naive "1–2 orders around one number."

---

## 3. Gate design

New trust-suite stage 25 (`lab/validation/run_all.py`), four gates, matching stages 23/24's own established pattern exactly:

1. **THE ABSOLUTE IDENTITY** — `bonded_substrate_conduction_correction(..., r_contact_m2k_w=0.0, r_contact_provenance="measured_direct", ...)` reproduces `front_surface_conduction_correction`'s own `correction_factor` bit-for-bit (checked at both `L_BENCH_M` and `L_MP5_730X_M`) — the literal `R_contact→0 ⇒ CF→bracket B` limit Red Team specified.
2. **REGRESSION ANCHOR** — at `R_contact=4×10⁻⁸` (primary anchor) and `κ_solid=0.70 W/(m·K)` (TD-1's worst sourced figure), reproduces this cycle's own committed Phase-1 script-output numbers to a stated tolerance, same discipline as stage 23 gate 2.
3. **THE FALSIFICATION-BOUNDARY IDENTITY** — a bisection for `R_contact_critical`: at fixed `κ_solid=0.70`, the `R_contact` value that drives the witness-scale (MP-5/730×) margin to exactly 1.0× reproduces this cycle's own committed number to a stated tolerance — the direct analog of stage 23's `κ_critical` gate, now swept along the new axis.
4. **THE SOURCE-INSPECTION GATE** (mirrors stage 24 gate 4, EM's own load-bearing catch at exp-064) — text-scans `run_all.py`'s own committed source for every `bonded_substrate_conduction_correction` call site: any call using the primary/secondary anchor or stress-point R_contact values must literally carry `r_contact_provenance="analogy_proxy_diagnostic", r_contact_diagnostic_only=True`; `length_provenance` must be independently correct per T23's own existing rule at that same call site (bench vs. witness). Declaration-not-detection, disclosed as the same limit exp-064's own Idealization 1 already names.

New `caveat_lint_config.json` entry `exp067-r-contact-analogy-proxy-disclosure`: any future citation of this cycle's R_contact-corrected numbers must disclose "analogy-based proxy, not a directly-measured root/substrate figure" — `required_sites` = `NOTES.md` + `phase4_results.md` **from the start** (learning directly from Iteration 40's own Checkpoint-4-firing NOTES.md-only-scoping mistake, and Iteration 41's own fix).

---

## 4. Predictions, falsifiable, committed before any code runs

Derived analytically from the functional form above (§2) — reproduced here as the numbers Phase 4 must either confirm or falsify:

| R_contact (m²·K/W) | CF_bench | Bench margin (baseline 674.22×, bar 100×) | CF_witness | Witness margin (baseline 1.2920×, bar 1.0×) | κ_critical (baseline 0.089731) | Headroom vs κ=0.70 (baseline 7.80×) |
|---|---|---|---|---|---|---|
| 0 (gate) | 1.03716 | 674.22× | 1.04487 | 1.2920× | 0.089731 | 7.80× |
| 4×10⁻⁸ (primary anchor) | 1.03761 | **~674×, unmoved** | 1.04487 | **~1.2920×, unmoved** | ~0.089731 | **~7.80×, unmoved** |
| 6.5×10⁻⁵ (query-2 anchor) | 1.75972 | **397×, still clears bar 4×** | 1.04681 | **1.2896×, −0.2%** | 0.09023 | 7.76× |
| 1×10⁻³ (stress A) | 12.15 | **57.5× — CROSSES BELOW TD-4's own 100× bar** | 1.07474 | 1.2561×, −2.8% | 0.09811 | 7.14× |
| 1×10⁻² (stress B) | 112.2 | 6.2×, deep below bar | 1.34363 | **1.0047×, margin nearly erased** | 0.61295 | 1.14× |

**The headline, falsifiable prediction**: under this series-insertion model, the primary (query-10) anchor and even the query-2 anchor **do not meaningfully move either bracket-B margin** — because `Bi_contact` scales with `h_combined` (tens of W/m²K at witness scale, dominated by the already-modest gas-conduction/radiation loss channel), not with `κ_solid`, so it is structurally decoupled from the dominant `Bi_gas=k_air/κ_solid` term that governs both `κ_critical` and TD-5's 7.8× headroom. **A genuinely novel, counter-intuitive prediction**: the **bench-scale TD-4 margin (100× bar) is the more sensitive channel, not the witness-scale TD-5 margin (1.0× bar)** — because bench-scale `L` is tiny (2.34µm), making `h_combined` huge (≈11,116 W/m²K), so a fixed `R_contact` produces a proportionally much larger `Bi_contact` there. If Phase 4 measures `R_contact` values anywhere near query-2's own already-committed figure or above, **TD-4 is the first bracket to show real degradation, well before TD-5 approaches 1.0×** — a falsifiable, checkable claim, not asserted safe by default. If falsified (i.e., if a real R_contact figure or a corrected model instead couples through `κ_solid` directly), that itself is a reportable finding about which normalization the honest physics actually demands.

---

## 5. Idealizations (stated explicitly)

1. **This cycle's own R_contact VALUE is an analogy-based proxy, not a directly-sourced root/substrate figure.** A real literature search (the 3–5 query dispatch Red Team's own Iteration-40 audit specified) remains a **queued follow-up**, explicitly named as still-open, carried forward to whichever future cycle the WebSearch/WebFetch tooling constraint clears — not resolved, not silently closed by this cycle's analogy.
2. **The series-insertion model is a modeling choice inside the existing chain's own scope**, not a first-principles rederivation of the true root/substrate boundary condition — it satisfies the required `R_contact→0` limit and stays inside "add a series term," per the task's own scoping, but does NOT resolve my own Iteration-40 Phase-5 finding that the rear-boundary physics itself (gas conduction to quiescent air) may not even apply once the base is bonded to a substrate. A deeper reformulation of the rear boundary condition is explicitly out of scope this cycle.
3. **`l_geometric_m` in the new function is the SAME length already used by `front_surface_conduction_correction`** — no new length parameter is introduced. `length_provenance` tags carry forward unchanged at each call site: `"bench_construction"` for `L_BENCH_M` (2.34µm); `"extinction_derived_diagnostic_only"` with `diagnostic_only=True` for `L_MP5_730X_M` (1051.2µm, the T23-governed witness-scale figure) — per the existing, code-enforced T23 contract.
4. **The mechanistic analogy assumes the root/substrate interface is dominated by the same weak, sparse van-der-Waals-type contact physics as the already-measured tube-tube junction** — plausible (my own Iteration-40 argument), not proven. A real interface could differ either direction: catalyst-mediated CVD growth can produce genuine chemical bonding at the root (better than a vdW junction), or the macroscopic root/substrate contact area could be sparser than nm-scale tube-tube contacts (worse) — exactly why the direct search stays queued rather than treated as answered by analogy.
5. **A units/scale-legitimacy flag on the primary anchor itself**, disclosed not resolved: query 10's `4×10⁻⁸ m²K/W` figure most plausibly describes a per-junction nanoscale contact patch, not a macroscopic areal density — possibly optimistic if applied directly at macroscopic root/substrate scale. Query 2's own already-committed, ~3-orders-larger "interfacial ≈0.6–0.7 cm²K/W" figure is carried as a second anchor for exactly this reason.
6. **T1 escape route: N/A** — a desk/analytic-only, zero-FDTD cycle, matching exp-063/064's own scope discipline.
7. **NETD disclaimer carried forward unchanged**: nothing in this analysis bears on constraint-3/4's human-eye verdict — R_contact is a thermal-detectability (instrument) question only.

---

## 6. Secondary/optional scope — recommendation

**Recommend YES**, fold in a companion Block-ARTICLE settled-STEPS FDTD leg (Red Team's own Iteration-43 ranked item #2 — interior `FALLBACK_ANGLES` at STEPS≥2800, Block ARTICLE's article-PRESENT legs at settled STEPS, prioritizing 39–40°/450nm per ELECTROMAGNETISM's Iteration-43 Phase-5 finding), reusing exp-065/066's own harness (`CONFIGS["C40"]`/`_settle_one`/`_c_empty`) verbatim — **this is my own recommendation as this cycle's MATERIALS lead, and it matches a prior MATERIALS seat's own Iteration-43 Phase-5 recommendation** (PLAN.md's queue explicitly notes "MATERIALS' own Phase-5 review recommends folding both into one Iteration-44 cycle if scope allows").

**Reasoning**: R_contact (desk/literature-class work on `thermo_sidecar.py`) and the T27 settling leg (FDTD-budget work) are structurally orthogonal resource classes — they do not compete. **Sequencing recommendation**: complete R_contact's desk work first — it is the LOCKED, unconditional item; Red Team's own ruling explicitly forecloses a fourth deferral, while the T27 leg carries no such lock — then apply any remaining cycle scope to the T27 FDTD leg as a secondary track. I do **not** recommend folding in Block MINI's period-match test (#3) this cycle — it is lower-priority, and QUANTUM OPTICS/PHOTONICS are its natural owners, not MATERIALS' charter; leave it queued as-is.

---

**Candidate experiment number**: exp-067. **Files touched (proposed)**: `lab/thermo_sidecar.py` (new `bonded_substrate_conduction_correction`, `_validate_r_contact_provenance`), `lab/validation/run_all.py` (new stage 25, 4 gates), `lab/caveat_lint_config.json` (new entry `exp067-r-contact-analogy-proxy-disclosure`), plus (if §6's recommendation is adopted) `experiments/065-t24-absorb-boundary-sweep/`-class harness reuse for the T27 companion leg.