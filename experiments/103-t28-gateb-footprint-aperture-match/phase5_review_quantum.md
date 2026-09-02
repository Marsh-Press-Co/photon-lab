#### QUANTUM OPTICS — verdict: **CONFIRM-WITH-GAPS**

### Independent recomputation (from `results.json` raw fields)

All headline numbers recomputed directly from raw fields, all exact matches (kappa_window, reversal count [confirmed strictly non-decreasing at every step], floor-gate RMS, span_mean, ratio_to_window, two settling rel_change spot-checks, kappa_window pointwise std/mean=0.8488332699891985, pointwise max/min=96.83×). No arithmetic discrepancy found anywhere.

### Independent re-derivation of Red Team's rel_phase-invariance ruling (Phase-2, item 9)

Read `lab/fdtd2d.py::add_line_source` docstring (`rel_phase`) and `lab/emit.py::_phasor` directly, from scratch, without assuming Red Team's framing:

- `add_line_source`'s own docstring states injecting `sin(ω·n − phase_geom(y) − rel_phase)` "multiplies this source's own steady-state Ez/Hy phasor by `exp(+i·rel_phase)`" — independently derived three ways (PHOTONICS/EM/Red Team, Iteration 35) and suite-gated (stage 20). Not a fresh claim for exp-103; load-bearing, already-validated engine behavior.
- `_phasor(f_a, f_b, ω, offset)` reconstructs `F` via linear combination of two real time-domain snapshots — no absolute value taken at that stage, so a common `exp(i·rel_phase)` factor propagates through unchanged.
- The engine is linear (no saturation, no gain, no nonlinearity anywhere in `fdtd2d.py`'s update loop) — a single-frequency drive with constant phase offset produces the SAME spatial solution multiplied by one global unit-modulus scalar.
- `|exp(i·rel_phase)·F(x,y)| = |F(x,y)|` exactly, at every point, for any `rel_phase`.

**Verdict on Red Team's override: RIGHT — confirmed independently, not merely accepted on authority.** Re-sampling at 3–4 `rel_phase` values would have reproduced the same `kappa` values (modulo pure floating-point/numerical-solver noise), burning 2–3 extra FDTD-call pairs for zero physical information. My own seat's Phase-2 remedy was correctly overridden.

### Findings

**1. [load-bearing]** Independently, and by a different route than PHOTONICS, arrived at essentially the same core finding: the adopted "≤10 cells (λ/2)" pitch is calibrated to the FIELD's own spatial period (λ=20 cells), but `kappa_region` is an INTENSITY (|E|²) quantity, whose coherent cross-term oscillates at DOUBLE the field's spatial frequency (period λ/2=10 cells) — so resolving the intensity fringe requires spacing <5 cells (quarter-wavelength), not ≤10. The adopted 10-cell pitch samples exactly at the intensity fringe's own period — the single most aliasing-prone case in sampling theory. Neither PHOTONICS's original Phase-2 critique nor Red Team's ruling distinguished field-Nyquist from intensity-Nyquist.

**2. [load-bearing]** This cycle's own disclosed data corroborates that the concern in (1) is not hypothetical. `kappa_window`'s own pointwise spatial-spread report — std/mean=0.849, 97× spread (min 0.0749%, max 7.25%) — is direct, independently-recomputed evidence of large-amplitude coherent spatial structure sitting right next to the 1-D x-line the 16-point trend is sampled along. NOTES.md's Result section characterizes the trend as showing "no sign of the aliased ripple… the risk would have produced" — but the same document's own numbers show ripple of comparable scale genuinely exists nearby. Internal-consistency tension.

**3. [non-load-bearing]** A smooth, zero-reversal monotonic envelope is, if anything, the signature more characteristic of a partially-coherent or broadband source (temporal/spectral averaging washes out fringe contrast) than of a single-frequency, fully-coherent CW field near a lossy scatterer — the regime this bench actually idealizes (600 nm only). Combined with findings 1–2, the more parsimonious read of the "clean" trend is sampling-grid aliasing against real coherent structure, not an absence of that structure. This does not falsify Prediction 2 as literally specified — it only means the interpretive claim built on top of that pass is asserted more strongly than the sampling design supports.

**4. [non-load-bearing]** `Delta_phi` (the complex phase, computed by exp-102 at every reported point) is not computed anywhere in exp-103's `run.py` — confirmed by direct grep of both files. Both `ez_empty`/`ez_article` are already complex arrays in memory from `sc.phasors()` at zero marginal FDTD cost, exactly the same "free extra reading" pattern this cycle already uses for the settling leg. Its absence doesn't invalidate any result, but a reader skimming could over-generalize Red Team's narrow rel_phase-invariance finding into "phase is a closed question this cycle," which it isn't.

**5. [non-load-bearing, confirming]** The settling-independence leg's convergence (0.003%–0.11% across all 5 near-field points) is a genuine, useful corroboration that this system's temporal dynamics are cleanly linear/classical — supporting (not proving) the T1: N/A framing.

### Argued next change

The cheapest, highest-value fix for the next cycle touching this instrument: two zero-marginal-FDTD-cost additions to the same already-captured field pairs — (1) restore `Delta_phi(x)` at all 16 points (exp-102's own convention, dropped this cycle without comment), giving a second, phase-based channel to cross-check the "smooth fill-in" story independently of magnitude; and (2) report `kappa_region`'s own local pointwise std/min/max at each of the 16 x-points — the same disclosure already given for `kappa_window` as a whole — which would directly reveal whether the reported trend is a genuine smooth envelope or an artifact of sampling at exactly the intensity fringe's own period (finding 1). Both are pure post-processing on data this cycle already paid for; neither adds a mechanism, changes T1:N/A, or costs a single additional FDTD call.
