# Phase 5 Review — PHOTONICS (blind, fresh context)

## 1. Independent verification findings

**Optical coherence across λ/angle.** P-068-5's interior-angle empty-scene pattern is physically sane: `|C_empty|` grows monotonically from near-zero at 0°/±5° (≈2–3×10⁻⁵) through ±15° (≈2.5×10⁻⁴) to ±25° (≈6–7×10⁻⁴) — edge-diffraction/fringe amplitude rising toward grazing, exactly the near-vs-far-from-grazing signature checked — internally consistent with exp-066's own passivity/settling story (defect grazing-localized, not uniform). Article-row C values (both configs ≈ −0.0053 to −0.0056 at 2800 steps) stay negative and MARGINAL — expected sign/order of magnitude for a weak absorber. The 750nm Tier2 cell flips sign relative to 600nm at fixed θ=−35° (−0.0081 vs +0.0018 at C40) — a single-angle reading in an interference-governed channel (T21 fringes), consistent with a wavelength-dependent diffraction-pattern shift, not a red flag.

**`_c_self` algebra — verified directly against `lab/ambient.py`.** `incoherent_sum` on a single profile `p` normalized by scalar `f` returns `p/f`; `weber(obj_mean(p/f), flank_mean(p/f)) = weber(obj_mean(p), flank_mean(p))` — the normalization scalar cancels exactly regardless of value. `_c_empty(profile, cfg)` self-pairs the profile, so its result is provably just the self-Weber-contrast of the profile — content-agnostic, confirmed by direct derivation.

**REALIZABILITY_MEMO contingency / 750nm coherence.** `realizability_memo_amendment_needed` logic correctly evaluates false — both configs' |C| (0.0056, 0.0053) stay well inside [0.0025, 0.01]. 750nm extension is honestly scoped (Tier0/Tier2 only, never claims full-N9 750nm coverage); reformulated P-068-4 is the physically correct fallback, no cross-STEPS extrapolation smuggled in.

**Process note.** This seat's own Phase-2 critique (θ=−35°/750nm optional/first-to-cut) was fully adopted at Phase 3 (mandatory fix 3) — Tier2 promoted to never-de-scoped, extended to both configs. P-068-6 independently confirmed 4/4 STEPS=2800 converged there.

## 2. Verdict: PARTIAL

Headline (P-068-2/3) genuine and load-bearing; supporting math (`_c_self`) and convergence claim (P-068-6) both check out under independent re-derivation. P-068-1's REFUTED (C40 breaches GATE_HARD, new instrument-characterization finding at aggregate level) and P-068-4's PARTIAL split keep this from PROMISING. Not RULED OUT — no mechanism class foreclosed.

## 3. Ranked top-3 for Iteration 46

1. Block MINI's period-match test — desk-first zero-cost check, then FDTD or formal retirement.
2. Resolve P-068-4's config-dependent 750nm-vs-600nm convergence-ordering split.
3. R_contact literature search.

## 4. Process concern

None rising to a citation-worthy defect from independent re-derivation.
