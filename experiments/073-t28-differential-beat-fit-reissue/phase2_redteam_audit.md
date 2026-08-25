# PHASE 2 — RED TEAM AUDIT · Panel Iteration 50 · exp-073 (T28 corrected differential/beat-fit re-issue)

*Fresh sub-agent, RED TEAM charter. Receives the Phase-1 proposal and all
five blind Phase-2 critiques; speaks last. Desk-only instrument/statistics
re-verification cycle on live thread T28 — T1 N/A, constraint 3 not
engaged, so constraint tags are N/A throughout; attacks below are tagged
`[inconsistency]`, `[unfalsifiable]`, `[inexpressible]`, `[statistical-
defect]`, or `[process]` per the defect class, matching exp-072's own
Phase-2 audit's precedent of extending PANEL.md's literal tag set.*

---

## 0. Framing — what this audit did, and what it independently verified

Every load-bearing numerical claim across all five critiques was
re-executed from the committed JSON or re-derived in an independent
implementation, not adjudicated from prose. Three things needed genuine
computation, not just reading: (a) reproducing EM's χ₀ figures from
exp-072's own `results.json`; (b) independently re-implementing QUANTUM's
sign-flip-null Monte Carlo stress test from scratch, on the real design
geometry; (c) quantifying VISION's structural concern about clause (vi)
using exp-072's own already-published carrier-gate calibration figures as
an order-of-magnitude proxy. All three reproduced closely enough to
certify the seats' findings as independently confirmed, not merely
internally consistent prose.

**Verification ledger (reproduced independently, this audit):**

| Claim | Source | Status |
|---|---|---|
| G0-e(i)'s synthetic generator: `C_A=a0·cos(w_A·u−ψ0)`, `C_B=a0·cos(w_B·u−ψ0)` — one `a0`, one `ψ0` for both members, verbatim from exp-072's `ground_truth_recovery_check` | PHOTONICS | **VERIFIED** — read directly off exp-072's `run.py:557-583` and exp-073's own §4 text; identical construction, zero `δa`/`Δψ` axis added |
| `A_i` tripwire's qualifying condition `\|a_B−a_A\|≥1e-4` is always false under G0-e(i)'s own generator | PHOTONICS | **VERIFIED** — `a_B−a_A≡0` by construction; clause is dead code |
| exp-072's closed, real `χ₀` values: −0.0197 / −0.0203 / −0.0062 / −0.0434 rad | EM | **VERIFIED, exact**, computed independently from `experiments/072-.../results.json`'s `A_q`/`amplitude` fields via `χ₀=arctan(A_q/2a_cbar)` |
| `tan χ₀ / sin χ₀` ratio at those values: 1.0002–1.0009 | EM | **VERIFIED, exact** |
| EM's a-priori `χ₀` reconstruction (−1.205 / −0.583 / −0.581 / −2.403 rad) from `m₀`, `T_x`, `x̄` | EM | **VERIFIED, exact**, independently recomputed |
| `n_grid=3000` refit slope 0.0024637°/cell, R²=0.8328, vs `m₀`=0.0025564°/cell (n_grid=400) | THERMODYNAMICS | **VERIFIED, exact** — `results.json → saturating_vs_linear.linear.{slope,r_squared}` = 0.002463678368980155 / 0.832803568626572 |
| Sign-flip null (sign-flip `resid5`, add to `yhat0`, refit) on pure-noise synthetic data at the real 31-point design: empirical rejection rate ≈2–6× nominal α | QUANTUM | **INDEPENDENTLY REPRODUCED FROM SCRATCH** — own from-scratch implementation gives 5.5×/2.3×/1.7× at α=0.01/0.05/0.10 (QUANTUM: 5–6×/2.2–2.6×/1.6–1.9×) |
| Leverage mechanism: `E[Var(R_q^surr)]/Var(R_q^obs) ≈ 0.79`, `mean diag(M5) = 26/31 = 0.8387` | QUANTUM | **VERIFIED, exact** — own closed-form + simulation reproduces 0.794 and 0.8387 exactly |
| Neither Freedman–Lane-on-`resid0` nor leverage-studentized-`resid5` fully closes the calibration gap | QUANTUM | **VERIFIED IN SUBSTANCE** — own MC: `resid0` α=0.05 empirical ≈0.068–0.070 (inside G0-e(ii)'s own band at that one cell) but 22/216 cell-α combinations tested still fall outside band; `resid5` studentized ≈0.08 at α=0.05, matches QUANTUM's 0.084 |
| §5 contains no "G-gate table"; clause (vi)'s cross-reference is unresolved in the document as written | VISION | **VERIFIED** — direct grep, §5 is titled "Named-constant / parameter search — R5 applicability" and defines no per-carrier admissibility statistic |
| `1.2591°`'s closeness ratio to `T_mean` (0.49–0.50) vs. exp-072's own already-published `carrier_gate_q95` (0.27–0.47) at all four pairs — `T_delta` always inside, `1.2591°` always outside | VISION (qualitative), Red Team (quantitative) | **VERIFIED, exact**, computed directly from `results.json`; used as an order-of-magnitude proxy for exp-073's own (not-yet-computed) sign-flip-null `q95`, since both are 95th percentiles of the identical statistic under differently-constructed but similarly-shaped nulls |

No claim from any of the five critiques was found to be fabricated,
mis-transcribed, or unreproducible. All five verdicts (support-with-changes
× 5) are upheld as read — every seat found a real defect, correctly
characterized, with a workable remedy or an explicit "I flag this, I have
not resolved it" disclosure.

---

## 1. Numbered attacks

### Attack 1 — [inconsistency] PHOTONICS' finding is confirmed exactly: G0-e(i)'s synthetic sweep is structurally incapable of exercising the phase-dominated regime, and one of its own two named tripwires is dead code.

Verified directly against the proposal's own §4 text and exp-072's `run.py`
(the generator exp-073 states it reuses unchanged): `A = a·cos(2πu/T_A−ψ₀)`,
`B = a·cos(2πu/T_B−ψ₀)` — one shared amplitude symbol, one shared phase
symbol, for every one of the 1,728 cells, old or newly widened. `δa≡0` and
`Δψ≡0` identically throughout the entire sweep. Two independently
verifiable consequences:

1. The `A_i` tripwire (*"must match the directly-constructed `a_B−a_A`
   within 1% at every cell where `\|a_B−a_A\|≥1e-4`"*) has a qualifying
   condition that is false at every one of the 1,728 cells (`0≥1e-4` is
   never true). It is described as an active check and cannot evaluate on
   a nonzero target anywhere in the sweep — this program's own R4/verify-
   before-claim discipline exists precisely to catch a check that is
   *described* as running but *cannot* run.
2. `χ₀ = πΔf·x̄ + Δψ/2` is the model's own statement that the phase offset
   between two configs has two physically distinct sources — a period
   shift projected to window centre, and an independent phase offset that
   carries no frequency information. Since `Δψ≡0` throughout the sweep,
   `G0-e` can only ever generate `χ₀` through the `Δf·x̄` route. A graded-
   absorption-depth boundary (the actual varied parameter between
   `C40`/`C60`/`C70`/`C80`) is, on ordinary boundary-optics grounds, at
   least as likely to shift reflection phase as spatial period — meaning
   the pipeline has never been certified accurate in exactly the regime a
   real config-to-config difference is most likely to produce.

**Is this HALT-worthy, or something else?** Neither REJECT-REDESIGN nor a
pass-through. This is a genuine gap in R6's own mandatory gate — a gate
whose entire justification (LOGBOOK R6, adopted on the exp-072 sign-bug
precedent) is that it must certify the pipeline correct **before any real
data is scored**, across the regimes the real data could plausibly occupy.
Shipping `G0-e` with a structurally unreachable branch on the one channel
most likely to matter physically is the same *shape* of defect R6 exists
to prevent, one level removed — a coverage gap in the safety gate itself,
not a data-scoring error. It must be fixed in code before `run.py`'s
`G0-e` is committed and trusted, per PHOTONICS' own remedy: an independent
`δa/a ∈ {0, 0.03, 0.10}` axis and an independent `Δψ ∈ {0, ±0.3, ±0.8}`
rad axis, decoupled from the `ΔP`/`ψ₀` sweep, zero new FDTD cost. This is
not a Checkpoint-4 firing (caught cleanly at Phase 2, before any commit,
by the mechanism designed to catch it — this program's own established
non-firing shape), but it is a binding mandatory-fix item, not a
disclosure-only one: an uncorrected `G0-e` cannot be trusted to certify
what R6 requires it to certify.

### Attack 2 — [inconsistency] EM's finding is confirmed exactly: §3a's "binds hard this cycle" claim for the `A_q=2a_cbar·tanχ` correction is falsified by 30–100× on the identical substrate this cycle re-fits, and the error traces to an unverified inherited a-priori figure, not a fresh mistake.

Independently recomputed both sides. The a-priori estimate (`χ₀ ≈
π·Δf_pred·x̄`, `Δf_pred` from the committed `m₀` and each pair's `T_x`)
reproduces EM's numbers exactly: −1.205 / −0.583 / −0.581 / −2.403 rad —
a real, reproducible, data-free calculation, not fabricated. Its origin is
traceable: it echoes exp-072's own Phase-5 O-6 ruling almost verbatim
(*"the docket's own regime of interest (`χ ≈ 1.2 rad`) is where it
becomes a factor of 2.6"*), itself never checked at the time against
exp-072's own already-closed numbers. exp-073's proposal repeats this
inherited estimate without checking it against the one thing that would
have caught it: the identical carrier-fit machinery, applied to the
identical 124 points, whose real output was already sitting, published,
in `experiments/072-.../results.json` when exp-073 was written. The real
`χ₀` values (independently recomputed here, exact to EM's figures):
−0.0197 / −0.0203 / −0.0062 / −0.0434 rad; `tan/sin` ratio 1.0002–1.0009 —
a 0.02–0.09% correction, two to three orders of magnitude below the
claimed 2.6×.

This is a genuine `[inconsistency]`: the document's own §3 evidentiary-
class discipline (a/b/c) exists specifically to prevent an unverified
number from riding into a "binds hard" claim, and it missed its own case,
on its own reused substrate, with the falsifying data one directory away.
**Non-gating** (T2-4 feeds only the coefficient table, no Combined-Verdict
branch reads `A_q`/`χ₀`), so this is a text-only fix, not a threshold
change — but it is the direct trigger for the broader contamination
question ruled on in §3, below, which is more consequential than the
prose error itself.

### Attack 3 — [inconsistency] THERMODYNAMICS' finding is confirmed exactly: `m₀` is R4-compliant (loaded, never typed) but is the wrong-resolution reference, the third recurrence of the named Attack-5 defect.

Independently verified against `experiments/072-t28-differential-beat-fit/
results.json`: the already-committed `n_grid=3000` refit gives slope
`0.002463678368980155`°/cell, R²=`0.832803568626572` — exact match to
THERMODYNAMICS' cited 0.0024637/0.8328. `m₀=0.0025563909774436134` is
exp-071's own `n_grid=400` fit, the *same* node-collision quantization
§2b.1 explicitly adopts `n_grid=3000` to remove from the carrier search —
but §2c's power table and P-073-4's disclosed rate band both still anchor
to the unresolved value. **Low-stakes as scored**: verified the CONFIRM
band `[m₀/3,3m₀]` is disclosed, non-gating, and wide enough that a 3.76%
shift changes nothing reachable; the only gating rate clause (P-073-4
REFUTE, `ΔP<0` with `\|ΔP\|≥0.010°`) does not reference `m₀` at all. But
this is the exact defect this document's own Phase-2 grounding material
(exp-072's `phase5_redteam_audit.md`, item i) already named as recurring
inside "the disclosure written to prevent it" — a third instance on the
identical quantity, in a cycle whose entire purpose is closing recurring
defect classes. Mandatory fix, zero cost: load `saturating_vs_linear.
linear.slope` from exp-072's own already-committed JSON at Phase 3, carry
`m₀` alongside only as the historical/Iteration-48-native anchor.

### Attack 4 — [statistical-defect] QUANTUM's finding is independently reproduced from scratch on the real design geometry: the sign-flip null as literally specified is anti-conservative by 2–6× nominal, driven by a leverage effect, and neither of the two obvious textbook fixes reliably closes the gap. This is the single most consequential finding in this audit.

Built an independent Monte Carlo implementation — own code, own random
seeds, the real 31-point 36.0°–42.0° θ grid, the real 5-column frozen
basis, `CENTER_DEG=39.0` — with **zero reference to QUANTUM's own code**,
only to the algebraic construction §3b/T2-3 specifies. Result, pure H₀
noise (`y=ε`, no ramp signal), sign-flip `resid5`, N=20,000 surrogates per
draw, swept over carrier phase and noise level:

| Nominal α | This audit's independent MC | QUANTUM's reported range |
|---|---|---|
| 0.01 | **0.055** (5.5×) | 0.049–0.061 (5–6×) |
| 0.05 | **0.117** (2.3×) | 0.108–0.132 (2.2–2.6×) |
| 0.10 | **0.172** (1.7×) | 0.160–0.188 (1.6–1.9×) |

Also independently re-derived the leverage mechanism from first principles:
`E[Var(R_q^surr)]/Var(R_q^obs) = Σᵢ row5ᵢ²·(M5)ᵢᵢ / Σᵢ row5ᵢ²`, computed
directly as **0.7943** (QUANTUM: 0.79), with `mean diag(M5) = 26/31 =
0.8387` exactly matching the textbook `(n−p)/n` value. Both of QUANTUM's
proposed fixes were independently tested: sign-flipping `resid0`
(classical Freedman–Lane) instead of `resid5` brings single-cell rejection
rates close to nominal at some grid points (α=0.05 empirical ≈0.068,
inside G0-e(ii)'s own tolerance band there) but a wider sweep (27 grid
cells × 3 noise levels × 8 carrier phases, matching G0-e(ii)'s own
specified coverage) still puts **22 of 216 cell-α combinations outside
G0-e(ii)'s own calibration band** — real, but not uniformly closing the
gap, matching QUANTUM's own careful "improves but does not fully close it"
language rather than the more optimistic single-cell reading. Leverage-
studentized `resid5` similarly improves without fully closing (own MC:
≈0.08 at α=0.05, matching QUANTUM's 0.084).

**Ruling on the design question this attack forces** (per the specific
charge to decide this): **do not mandate a specific null-construction fix
now; keep G0-e(ii) as a binding, non-relaxable HALT, as already specified,
but require it to be more informative on both outcomes.** Two reasons.
First, I have independently shown neither "obvious" fix reliably passes
this exact design's own calibration bar either — mandating one now, on
the strength of a single favorable-looking cell, risks shipping a
*second-generation* miscalibrated null under false confidence, which is
precisely the class of mistake this entire cycle exists to correct (the
exp-072 sign-bug precedent: an unverified fix, believed correct, shipped
anyway). Second, the G0-e(ii) gate is doing exactly the job R6 was written
for: if it HALTs, that is the safety net functioning, not a wasted cycle —
provided the HALT itself is reported as a real, quantified, LOGBOOK-worthy
finding (a genuine bound on this instrument class: *small-n (n=31, p=5),
leverage-concentrated ramp-coefficient sign-flip nulls are anti-
conservative on this exact design, by a mechanism now characterized
exactly*), not merely "gate fired, nothing to report." This is folded into
the mandatory-fix docket (§4, items A1–A3) as a reporting requirement, not
a redesign mandate. It is also the direct answer to the "fix it now vs.
let the gate catch it" tension the mandate itself flags exp-072 as having
faced: here, unlike exp-072's sign bug (invisible to every gate, caught
only by three independent Phase-5 seats forward-simulating ground truth),
the calibration problem is now pre-emptively caught by the pre-registered
gate itself, before any real data is touched — the correct resolution of
that tension, not a deferral of it.

### Attack 5 — [inexpressible] + [inconsistency] VISION's finding is confirmed on both counts: clause (vi)'s cross-reference is unresolved in the document as written, and its most natural completion collapses T2-1 to a single-carrier test at exactly the pairs where the displaced comparator matters most.

**(a) Inexpressible as specified.** Direct grep of the full document
confirms §5 is titled "Named-constant / parameter search — R5
applicability" and defines no per-carrier admissibility gate of any kind.
Clause (vi)'s only literal antecedent for "clause (iv) at its own carrier"
is `\|T_delta−T_mean\|/T_mean ≤ q₉₅`, written specifically for `T_delta`.
What the identical substitution means for `1.2591°` is undefined. A gate
this document names as a flagship new safeguard (T2-1, the mandate's own
third folded item) is not computable as specified — a genuine
specification gap, not a citation slip, exactly as charged.

**(b) The natural completion is structurally biased against the carrier
it is supposed to test.** Quantified directly, using exp-072's own
already-published, non-contaminating `carrier_gate_q95` figures (computed
under exp-072's *restricted* null) as a same-order-of-magnitude proxy for
exp-073's own not-yet-computed sign-flip-null `q₉₅` — both are 95th
percentiles of the identical `\|T_x−T_mean\|/T_mean` statistic under
similarly-shaped surrogate ensembles on the identical design, so the
comparison is structurally informative even though the exact number will
differ:

| Pair | `q₉₅` (exp-072's restricted null) | ratio at `T_delta` | ratio at `1.2591°` |
|---|---|---|---|
| C40–C60 | 0.4715 | 0.1235 (passes) | 0.4936 (**fails**) |
| C60–C70 | 0.2724 | 0.1622 (passes) | 0.5020 (**fails**) |
| C70–C80 | 0.3853 | 0.2540 (passes) | 0.5028 (**fails**) |
| C40–C80 | 0.3767 | 0.1410 (passes) | 0.4944 (**fails**) |

At all four pairs, `T_delta` clears by a comfortable margin and `1.2591°`
misses by roughly the same margin it was designed to clear by
(`≥2.36 Rayleigh widths` was chosen to be *maximally* displaced — the
same property that makes it fail a closeness gate). If exp-073's own
sign-flip-null `q₉₅` lands anywhere near the same order of magnitude —
plausible, since both nulls are residual-based surrogate ensembles on the
identical fixed design — clause (vi) collapses to agreement with
`T_delta` alone at every pair, precisely where VISION's own exp-072 check
showed every pair flips sign somewhere in the admitted band. This is not
merely a documentation problem; it is a design defect masquerading as
one, and it must be fixed at the level VISION proposes, not merely
footnoted.

**Mandatory fix, VISION's own two-part remedy, adopted verbatim:** (1) a
self-contained, explicit definition of the per-carrier admissibility
statistic and its `q₉₅` source (computed and reported in-run, from that
candidate's own sign-flip surrogate ensemble — no forward reference); (2)
a non-emptiness floor — if the admitted non-`T_mean` set is empty for a
pair, that pair is `NOT_EVALUABLE` for T2-1, never vacuously passed. Both
must be fixed before Phase 3 commits `run.py` and thresholds to git; this
is a specification gap in the mandate's own flagship new safeguard, not a
minor wording issue.

### Attack 6 — [process] The cross-cycle structural fact none of the five critiques named in full: because exp-073's carrier-fit and 5-column-OLS machinery is bit-identical to exp-072's own already-committed, already-published code, on the identical data, exp-073's own real point-estimate table is already computable — right now — from `experiments/072-.../results.json`, not merely the one coefficient EM flagged.

Verified directly against exp-072's committed `run.py`: `N_GRID_CARRIER=
3000`, `CENTER_DEG=39.0`, the identical 5-column basis and sign convention
(`psi=-atan2(fit["b"],fit["a"])`), `T_WRONG_DISPLACED=1.2591`, applied to
the identical 124-point substrate — all confirmed literally unchanged in
exp-073's §2b/§3a. Since none of exp-073's three new-machinery items
(T2-1's admissibility gate, T2-3's null, T2-4's coefficient-table
relabeling) touch the underlying OLS point estimates, exp-073's own real
`T_mean`, `a_cbar`, `ψ̄`, `A_i`, `A_q`, `R_i`, `R_q`, `Δf`, `\|Δf\|·X`, `ΔP`
(magnitude **and sign**), and `carrier_r_squared`, for all four pairs, are
not merely "class (b), a previously-closed finding from an earlier cycle"
in the sense the document's own §0 taxonomy defines (its own worked
example — exp-071's `ABSORB`-depth slope — is a genuinely independent,
different-cycle result); they are a **bit-exact preview of this cycle's
own Phase-4 output**, sitting in a file every seat and the Director were
directed to read as this cycle's own grounding material.

EM's critique demonstrates the practical consequence for one coefficient
(`A_q`/`χ₀`); this attack generalizes it. This is a genuine escalation of
the contamination question beyond what exp-072's own §4 ruling
contemplated (which addressed *within-cycle* Phase-2 computation) — here
the "prior cycle's real answer" is structurally baked into the *new*
cycle's own mandatory reading list, before Phase 1 was even proposed.
Ruled on formally in §3 below, with binding conditions.

### Attack 7 — [statistical-defect] EM's own flagged, self-acknowledged gap deserves promotion, not a footnote: G0-e(ii) calibrates only against i.i.d. Gaussian synthetic noise, and Attack 4 already shows the null fails calibration even in that easiest case — the untested harder case (structured/correlated real FDTD residuals) can only be as bad or worse.

EM raised this as supporting detail, explicitly declining to quantify it
("I cannot quantify its size without the real residuals in hand"), and
correctly did not make it the sharpest attack. Red Team's own independent
confirmation of Attack 4 changes its weight: since the null is already
shown miscalibrated on the *best-case* i.i.d. assumption G0-e(ii) tests,
a genuinely correlated real residual (which the design elsewhere concedes
is real enough to justify rejecting case-resampling for `SE(ΔP)`, §3a)
cannot make the calibration problem better and plausibly makes it worse.
This is directly answerable at zero additional FDTD cost — resample the
already-committed per-config free-period-fit residuals from exp-069/071
as an empirical noise distribution, instead of i.i.d. Gaussian, and re-run
G0-e(ii)'s calibration sweep on that leg too. Folded into the mandatory-
fix docket alongside Attack 4, not as a separate gate.

### Attack 8 — R5/named-constant-search check — not re-triggered; confirmed clean, independently.

§5's own reasoning is sound and unchanged from exp-072's identical,
already-cleared argument: one physically-motivated functional form, four
pre-specified pairs, one 1-D period-grid continuum already established
non-triggering across three prior cycles (exp-069/071/072). `T_WRONG=
1.2591°` is a single pre-registered, data-free-derived constant, not a
search. No LOGBOOK R5 ruled-out item appears anywhere in this document.
Confirmed clean — no attack here, recorded for completeness per this
program's own standing R5-check convention.

---

## 2. Adjudication of the five critiques

| Seat | Sharpest attack | Ruling |
|---|---|---|
| PHOTONICS | G0-e(i)'s vacuous `A_i` tripwire; phase-dominated regime never exercised | **CONFIRMED, independently re-verified from the document and exp-072's own generator code.** Adopted as Attack 1, mandatory fix (docket A1). |
| ELECTROMAGNETISM | `A_q` "binds hard" claim contradicted 30–100× by exp-072's own already-closed `χ₀` | **CONFIRMED, independently re-verified exact.** Adopted as Attack 2. Its own re-derivation of `A_q=2a_cbar·tanχ` from scratch (steel-man) and its algebraic proof of `E[R_q^surr]=0` (supporting detail) are both independently spot-checked here and hold; its self-flagged residual-correlation caveat is promoted to Attack 7. |
| THERMODYNAMICS | `m₀` is the wrong-resolution reference, third Attack-5 recurrence | **CONFIRMED, independently re-verified exact against `results.json`.** Adopted as Attack 3. Its secondary citation-provenance note (Iteration 5 vs Iteration 2) is correct and folded into the docket as a minor fix. |
| QUANTUM OPTICS | Sign-flip null anti-conservative 2.2–6× nominal, leverage-driven | **CONFIRMED, independently reproduced from an entirely separate implementation.** Adopted as Attack 4, ruled the most consequential finding in this audit. Its own two candidate fixes are independently tested here and found not to fully close the gap either — the correct conclusion, matching QUANTUM's own careful hedging over a more optimistic single-number reading. |
| VISION SCIENCE | Clause (vi)'s "§5 G-gate table" does not exist; the natural completion structurally excludes the displaced comparator | **CONFIRMED on both counts, the second one quantitatively strengthened here** using exp-072's own published `carrier_gate_q95` figures as a proxy (0.49–0.50 ratio for `1.2591°` vs. 0.27–0.47 `q₉₅` at all four pairs — fails everywhere). Adopted as Attack 5. Its own disclosure that it did not compute the real `q₉₅` and did not run any part of the real estimator is verified accurate and is exactly the right level of restraint for a Phase-2 seat under this cycle's contamination discipline. |

**No finding from any seat is overruled.** This is a genuine outlier
relative to exp-072's own Phase-2 audit (which overrode three seats'
specific remedies while accepting their diagnoses) — every one of the
five critiques this cycle got both the diagnosis and, where offered, a
workable remedy right. The one place this audit modifies rather than
adopts verbatim is QUANTUM's own optional fix (§ Attack 4): QUANTUM
proposed *either* of two specific null-construction changes as the thing
that would flip its verdict to unqualified support; this audit finds
neither reliably passes the design's own calibration bar and therefore
declines to mandate either, instead hardening the reporting requirements
around the existing G0-e(ii) HALT. This is a refinement of QUANTUM's own
already-hedged position ("whichever is adopted, G0-e(ii) must stay a
binding, non-relaxable HALT"), not a reversal of it.

---

## 3. Ruling on pre-registration contamination

**This audit's ruling extends, rather than repeats, exp-072's own §4
ruling — it addresses a structurally new form of the same risk, arising
specifically because this cycle's mandate is a re-issue of unchanged
machinery on unchanged data.**

**The facts, established in Attacks 2 and 6.** exp-073's carrier-fit and
ramped-differential-OLS machinery (§2b.1–§2b.2) is bit-identical to
exp-072's own already-committed, already-published, post-fix `run.py`,
applied to the identical 124-point substrate. Every real per-pair point
estimate this cycle's Phase 4 will produce — `T_mean`, `a_cbar`, `ψ̄`,
`A_i`, `A_q`, `R_i`, `R_q`, `Δf`, `\|Δf\|·X`, and `ΔP` including its sign —
is therefore already computable, bit-exact, from `experiments/072-.../
results.json`, and was in fact independently computed, for the `A_q`/
`χ₀` channel, by this cycle's own EM critique. This document (`phase1_
proposal.md`) and its mandatory grounding reading (item 5 of the task's
own reading list, `experiments/072-.../run.py`, `results.json`) place
these numbers in front of every Phase-2 seat, and the Director at Phase 3,
before exp-073's own Phase 4 has run.

**Why this is not covered by exp-072's own condition-1/class-(b)
taxonomy as written.** §0's own worked example of a "class (b),
previously-closed, non-contaminated finding" is exp-071's `ABSORB`-depth
slope — a genuinely independent number from a cycle that predates
exp-072's existence, computed by different machinery for a different
purpose. exp-072's own point estimates are not that: they are the *same*
computation, on the *same* data, that exp-073's own Phase 4 will re-run.
Calling them "class (b)" stretches the taxonomy past what it was built to
license.

**Is it outcome-determining? Ruled: not for the Combined Verdict, as
currently specified — but real, and binding conditions attach.** Applying
the same test exp-072's own ruling used (§4, condition 1, "every docket
item must be justified by an argument that does not reference an observed
value"):

1. **None of exp-073's three new-machinery items were tuned in response to
   the now-known numbers.** T2-3 (the sign-flip null) is justified purely
   algebraically — independently re-verified in EM's own critique and,
   separately, in this audit's Attack 4 — with no reference to any
   observed `R_q`, `p`, or `ΔP`. T2-1 (the admissibility gate) is
   justified by a leakage-minimization argument over the search range,
   computed with zero data. T2-4 (the `tan χ` identity) is an exact
   trigonometric identity, true regardless of any observed value. None
   of the frozen constants (`N_GRID_CARRIER`, `CENTER_DEG`, `T_WRONG`,
   `HOLM_PAIRS`, `SAT_DECAY_L`) were newly chosen for this cycle at all —
   they are inherited unmodified from exp-072's own data-free derivations.
2. **The one place a real, previously-closed number enters this document's
   own argument — Attack 2 / EM's `χ₀` correction — touches an explicitly
   non-gating quantity.** No Combined-Verdict branch reads `A_q` or `χ₀`
   (§2b.3, restated in §3a). Fixing the prose to state the real expected
   magnitude, per the mandatory-fix docket, is disclosure, not a
   threshold change — structurally identical to how exp-072's own ruling
   treated QUANTUM's "disclosed structure without revealing outcome
   numbers" as acceptable, versus VISION's outcome-determining disclosure
   as requiring binding conditions.
3. **CONFIRM availability.** Per exp-073's own §7 pre-registration
   paragraph (already anticipating a version of this issue), any request
   to loosen a threshold based on an observed value is barred. This
   ruling extends that bar explicitly to cover values that are "observed"
   only in the sense of being re-derivable from exp-072's own committed
   files: no gate, band, or threshold anywhere in `run.py` may be set,
   moved, or selected with reference to any of exp-072's own real
   per-pair `A_q`, `a_cbar`, `A_i`, `R_i`, `R_q`, `ΔP`, or their signs,
   at any point between this audit and Phase 4's run — not only "after
   Phase 3's git commit" as the current text states, but from this audit
   forward, since the numbers are already in circulation.

**Ruling — three binding conditions, extending exp-072's own four:**

1. **Disclosure, extended.** The pre-registration paragraph (§7) must
   name this audit's finding explicitly: that exp-073's own real point
   estimates (not only `A_q`/`χ₀`) are bit-exact reproductions of
   exp-072's own already-published values, because the underlying
   machinery is unchanged — and must state that no threshold was set or
   moved with reference to them, citing this audit.
2. **Forward lock.** Any change to a gate, band, or threshold made after
   this audit and before Phase 4's run, for any reason traceable to
   exp-072's known real numbers, must be treated as a fresh Phase-1/2
   pre-registration decision — not folded into this cycle's own Phase 3
   synthesis as a same-cycle correction. This is the direct extension of
   exp-072's own condition-3 "CONFIRM cannot be certified as
   pre-registered" logic to the point-estimate level, not only the
   verdict level.
3. **If Phase 4 reaches a CONFIRM-shaped outcome on any pair**, `phase3_
   synthesis.md`/`phase4_results.md` must additionally disclose this
   audit's §3 finding alongside whatever contamination language the cycle
   already carries — a reader must be able to discount the "clean
   re-issue" framing without reconstructing this document's own
   reasoning.

**This ruling does not require re-scoping exp-073 or delaying Phase 3.**
It requires one disclosure paragraph and one forward constraint, both
zero-cost. The underlying reason this is tractable — unlike exp-072's own
contamination episode, which touched outcome-determining `p`-values and
required a `CONFIRM_UNCERTIFIED` escape hatch — is that every verdict-
determining gate in exp-073 was independently verified (Attacks 1–5, this
audit) to be justified data-free, and none of them was found to have been
adjusted in light of the now-known numbers.

---

## 4. Verdict

# **PROCEED-WITH-MANDATORY-FIXES**

The estimator is sound (independently re-verified: EM's from-scratch
re-derivation of `A_q=2a_cbar·tanχ` holds; the algebraic proof of
`E[R_q^surr]=0` under the sign-flip construction holds), the re-issue's
overall discipline is real (the a/b/c evidentiary-class taxonomy is a
genuine, load-bearing improvement over exp-072's own first draft, and it
correctly caught and disclosed most of what it was built to catch), and
every defect found in this audit — including the most severe one, Attack
4's calibration failure — is addressable at zero FDTD cost, before `run.
py` and thresholds are committed to git. REJECT-REDESIGN would be wrong:
nothing here indicates the differential/beat-fit approach itself is
unsound, only that this specific re-issue's safety machinery (`G0-e`) and
one new gate's specification (T2-1 clause vi) are not yet complete, and
one prose claim (the `χ₀` regime estimate) is wrong in a way that is
cheap to correct. This is exactly the shape PROCEED-WITH-MANDATORY-FIXES
exists for, matching exp-072's own Phase-2 precedent almost exactly one
cycle later, on a design meant to fix that cycle's failures.

---

## 5. Mandatory-fix docket — 12 items, to be applied at Phase 3 before `run.py` and thresholds are committed to git

**A. `G0-e` completeness and reporting (Attacks 1, 4, 7)**

1. **Add an independent-amplitude, independent-phase axis to `G0-e(i)`'s
   synthetic generator.** `δa/a ∈ {0, 0.03, 0.10}` and `Δψ ∈ {0, ±0.3,
   ±0.8}` rad, each decoupled from the existing `T_A`/`ΔP`/`ψ₀` sweep,
   zero new FDTD cost. Restores a live, non-vacuous check on `A_i` and
   genuinely exercises the phase-dominated (`Δψ`-driven) branch of `χ₀` a
   graded-absorption-depth boundary is at least as likely to produce as
   the period-shift branch. *(Attack 1, PHOTONICS' own remedy, adopted
   verbatim.)*
2. **Disambiguate the `A_i` tripwire's evidentiary class in code and in
   §3a's own taxonomy, explicitly.** Either (a) keep it purely synthetic
   — now meaningful once item 1 lands — and label it class (c); or (b)
   retain a separate real-data cross-check against the directly-measured
   `a_B−a_A` from the real 124 points (as exp-072's own T1-2 had it,
   10% tolerance, not 1%), correctly labelled class (b)/data-derived, not
   "not data-derived." Do not leave the current draft's self-contradicting
   label standing. *(Attack 1.)*
3. **Keep `G0-e(ii)` as a binding, non-relaxable HALT, unmodified in
   construction — do not adopt either candidate fix (Freedman–Lane on
   `resid0`; leverage-studentized `resid5`) as a same-cycle patch.**
   Neither was independently verified here to reliably clear the
   calibration bands (22/216 cell-α combinations still fail for `resid0`
   in this audit's own wider sweep). Instead: (a) persist the **full**
   24-cell × 3-α calibration table (empirical rejection rate, signed
   deviation from nominal, PASS/FAIL) to `results.json` and
   `phase4_results.md` **regardless of whether the cycle HALTs** — this is
   itself a genuine, LOGBOOK-worthy finding about this design class
   (small-n, `n=31, p=5`, leverage-concentrated ramp-coefficient sign-flip
   nulls, independently confirmed anti-conservative by 2–6×, mechanism
   characterized exactly); (b) if `G0-e(ii)` HALTs, the Combined Verdict
   must emit a named branch — e.g. `HALT_NULL_MISCALIBRATED`, not a
   generic HALT — carrying the calibration table; (c) any future adoption
   of a corrected null construction, in any subsequent cycle, must pass
   its own fresh `G0-e(ii)`-style pre-registered calibration test before
   gating real data — never a hand-picked patch adopted after seeing a
   failure. *(Attack 4, this audit's ruling.)*
4. **Add a residual-structure robustness leg to `G0-e(ii)`.** Repeat the
   calibration sweep using resampled real per-config residuals (from the
   already-committed exp-069/071 free-period-fit residuals) instead of
   i.i.d. Gaussian noise, zero new FDTD. Report both legs' calibration
   tables side by side; if the i.i.d. leg already HALTs (independently
   shown likely here), report the structured-residual leg's own numbers
   too rather than skipping it as moot — it is the harder, more realistic
   test and its own numbers are informative regardless of the i.i.d.
   outcome. *(Attack 7, EM's self-flagged gap, promoted.)*

**B. Estimator, coefficient-table, and gate corrections (Attacks 2, 3, 5)**

5. **Correct §3a's `A_q=2a_cbar·tanχ` "binds hard" justification.**
   Replace the "χ₀ order 0.5–1.2 rad" a-priori claim with the already-
   closed, non-contaminating exp-072 values as the operative expectation
   for this substrate (−0.006 to −0.043 rad; `tan/sin` ratio
   1.0002–1.0009), citing them explicitly as class-(b) disclosure. State
   plainly that the inherited a-priori figure (itself traceable to
   exp-072 Phase-5's O-6 ruling, never checked against exp-072's own real
   closed numbers) was wrong by one to two orders of magnitude for the
   real substrate, though it remains a legitimate a-priori estimate under
   the counterfactual that the true effect matched `m₀`'s predicted size.
   T2-4 remains non-gating throughout; this is a text-only fix. *(Attack
   2, EM's own remedy, adopted.)*
6. **Re-anchor §2c's power table and P-073-4's disclosed rate comparison
   to the `n_grid=3000`-consistent slope**, loaded at runtime from
   `experiments/072-t28-differential-beat-fit/results.json →
   saturating_vs_linear.linear.slope` (0.002463678368980155, R²=0.8328) —
   not re-derived, not re-typed. Carry `m₀` (exp-071's `n_grid=400` value)
   alongside only as the historical/Iteration-48-native anchor. Closes the
   third recurrence of the Attack-5 defect. *(Attack 3, THERMODYNAMICS'
   own remedy, adopted.)*
7. **Implement T2-1 (clause vi) with a self-contained, non-forward-
   referencing definition.** (a) An explicit per-carrier admissibility
   statistic for every non-`T_mean` candidate, with its own `q₉₅` computed
   from that candidate's own sign-flip-surrogate ensemble and reported
   in-run — no reference to a "§5 G-gate table." (b) A non-emptiness
   floor: if the admitted non-`T_mean` set is empty for a pair, that pair
   is `NOT_EVALUABLE` for T2-1, never vacuously passed. Both fixed before
   any real pair is fit. *(Attack 5, VISION's own remedy, adopted
   verbatim.)*
8. **Disclose the admission/exclusion outcome for `1.2591°` explicitly, at
   every pair, in P-073-1/P-073-5.** Given this audit's own quantitative
   estimate (§ Attack 5b) that a closeness-based reading of clause (iv)
   would exclude `1.2591°` at all four pairs, `phase4_results.md` must
   state plainly if that is the actual Phase-4 outcome — not merely
   report a technically-passing gate without noting it collapsed to a
   single-carrier (`T_delta`-only) test. *(Attack 5.)*

**C. Contamination disclosure (Attack 6, §3)**

9. **Extend the pre-registration-discipline paragraph (§7)** to state,
   citing this audit: exp-073's own real per-pair point estimates
   (`T_mean`, `a_cbar`, `ψ̄`, `A_i`, `A_q`, `R_i`, `R_q`, `Δf`, `\|Δf\|·X`,
   `ΔP` including sign, `carrier_r_squared`) are bit-exact reproductions
   of exp-072's own already-published `results.json`, because the
   carrier-fit/ramped-OLS machinery is unchanged on unchanged data — not
   merely the `A_q`/`χ₀` channel EM's critique surfaced. State that no
   gate, band, or threshold was set or moved with reference to them.
10. **Forward lock**: any gate/band/threshold change made from this audit
    forward, for any reason traceable to exp-072's known real numbers,
    must be treated as a fresh Phase-1/2 decision, not a same-cycle Phase
    3 correction.
11. **If Phase 4 reaches a CONFIRM-shaped outcome on any pair**, disclose
    this audit's §3 finding alongside the existing contamination
    language, in `phase3_synthesis.md` and `phase4_results.md`.

**D. Minor / documentation**

12. **Correct Idealization 13's citation** from "house precedent,
    Iteration 5" to "house precedent, Iteration 2" — a citation-provenance
    slip (THERMODYNAMICS' secondary note, independently spot-checked
    against LOGBOOK.md's own text and confirmed correct), not a
    substantive gap; the sidecar-N/A argument itself is sound on its
    merits regardless of the citation fix.

**Unchanged, independently re-verified sound, no fix required**: G0-a/b/c;
the frozen 5-column basis and its sign convention; the design-respecting
residual bootstrap for `SE(ΔP)`; `T_WRONG=1.2591°`'s own derivation and
value; the Holm-over-3 scope; `ρ_c`'s reframing as a carrier-sensitivity
diagnostic; the `ABSORB`-or-`PAD`-tied writing rule and every disclosure
convention in §3a/§8. No seat attacked these; this audit spot-checked each
against exp-072's own already-verified record and found no defect.

---

## 6. What this cycle should expect to publish

Given Attack 4's independently-confirmed calibration failure, the most
likely Phase-4 outcome, even after the mandatory-fix docket lands, is
**`HALT_NULL_MISCALIBRATED`** at `G0-e(ii)` — the design's own safety net
firing before any of the four real pairs is scored. That is not a wasted
cycle if docket item A3 is implemented: it converts an otherwise-invisible
statistical-methodology failure into a genuine, quantified, reusable
finding about carrier/phase-conditioned ramp-coefficient nulls on small,
leverage-concentrated angular-sweep designs — directly generalizable to
any future T28 (or other) cycle that fits a similar coefficient, in the
same spirit as the R5 addendum's null-permutation-control house rule. If
`G0-e(i)`/`G0-e(ii)` both clear (plausible if item 1's widened synthetic
coverage and item 4's residual-structure leg do not themselves surface new
failures), the substantive T28 question remains exactly where exp-072 left
it — bounded by window identifiability, not yet resolved — and this
cycle's honest contribution is closing the process gaps exp-072's own
Phase-5 audit deferred to it, not a new physics finding. Either outcome is
a real advance on the T28 thread; neither should be reported as more than
it is.
