# exp-062 — Phase 2 Critique: THERMODYNAMICS

**Panel Iteration 39. Seat: THERMODYNAMICS (blind critique, Phase 2).** Proposal under review: `experiments/062-thin-film-interference-and-near-field-coupling-bound/phase1_proposal.md` (Lead: ELECTROMAGNETISM). T1 escape route: NONE. Zero FDTD, zero constraint-1/2/3/4 metric scored this cycle.

---

## 1. Steel-man (≤150 words)

Correctly scoping this cycle as sidecar-free is the right call, not an omission. My charter's sidecar is a *post-run analytic calculation* converting an FDTD-measured absorbed power into ΔT and a detectability verdict (PANEL.md's expressibility contract) — this cycle runs zero FDTD and produces no new absorbed-power number, so there is nothing to convert. The proposal's own EM-4 falsification condition explicitly holds `α_true=5.74×10⁴ cm⁻¹` — the anchor my own standing disposition's `l_geometric_m`/margin chain is built from — fixed and untouched throughout; it only re-examines an already-EXCLUDED, out-of-class candidate's own OD-to-α conversion, a judgment call that by the proposal's own falsification logic (EM-3/EM-4) can only reinforce, not revise, that exclusion. Declining Red Team's item 3 (a tooling proposal, not a field/wave-coupling question) rather than annexing scope outside an EM-led cycle is exactly the charter-boundary discipline my own seat has had to exercise before.

## 2. Sharpest attack (≤150 words)

The proposal's own Section 5 rider predicts EM-5 CONFIRMED — near-field coupling among sub-λ CNT tubes (`ratio≈0.68<1` at 550nm) — and states this makes "a bulk-homogenization/Beer–Lambert reading of the forest's blackness... at minimum incomplete." That finding is not QUANTUM/EM-only: `l_geometric_m` in the standing THERMO disposition (`exp061-thermo-length-scale-staleness`, margin 1.35×–3.79×) is computed as `τ_true/α` using these *identical* CNT-forest α figures — and `thermo_sidecar.py::gas_conduction_h_eff`'s own docstring requires `l_geometric` be "a real geometric length of the... SOLID body... NEVER an optical/extinction-derived length." If the underlying (R,thickness) pairs don't reduce to a genuine bulk α at all, the derived length feeding `h_eff`/mass/area is exactly the kind of optically-proxied length that module warns against — yet nothing in this proposal names the dependency. Zero FDTD correctly means no *new* sidecar run; it does not excuse silence about an existing sidecar's own input now under live challenge from this cycle's own predicted result.

## 3. Verdict: **support-with-changes**

The physics is sound and the zero-sidecar posture is correctly reasoned for what this cycle actually computes — no new absorbed-power measurement exists to convert, and PANEL.md's per-run ledger obligation attaches to runs, of which there are none. But the proposal is silent on a real, cheap-to-flag cross-charter dependency: its own predicted EM-5 outcome bears directly on whether the standing THERMO margin's `l_geometric_m` rests on a licensed homogenization. This is not a physics defect in the proposal's own analysis — it is an undisclosed linkage of exactly the shape this program's caveat-propagation discipline exists to catch before a future cycle cites the 1.35×–3.79× margin without knowing its own foundation was quietly reopened.

## 4. The parameter/text change that would flip my verdict to full support

Add one sentence to Section 8 (Falsification conditions) or Section 9 (Idealizations): *"If EM-5 is CONFIRMED (near-field-coupling regime, ratio<1 at all three bench wavelengths), flag for Phase 5 review whether the standing THERMO disposition's `l_geometric_m` (`exp061-thermo-length-scale-staleness`, derived as τ_true/α from these same CNT-forest α figures) rests on a Beer–Lambert bulk-homogenization this cycle's own result calls into question — no new margin computation is owed this cycle (zero FDTD), but the dependency must be named now, not silently rediscovered later."* That single disclosure closes the gap without requiring any new calculation, run, or scope expansion.

## 5. Ruled-out / refuted-claim check

No re-proposal found. The proposal touches none of R1–R5 (refractive cloaking, integer-λ shell rules, grid-artifact claims, hand-typed "precisely recomputed" figures — this proposal's own Section 4.5 numbers are explicitly computed by direct invocation, R4-compliant — or the T21 phase-offset regressor) and does not resurrect any refuted T1–T26 finding (ambient-instrument angular/domain confounds, coherent-superposition artifacts, settling-time or resolution anomalies). It is a clean, self-contained realizability-bound continuation with no live thread violated.
