# THERMODYNAMICS — Phase 5 Review · Panel Iteration 54 · exp-077 (T28 PAD round-trip echo refit)

*Fresh sub-agent, THERMODYNAMICS charter (PANEL.md, verbatim): "where
absorbed energy goes. Always asks what re-radiates and whether it would be
detectable. Owns the per-proposal energy sidecar: absorbed power ->
temperature rise -> emission band -> detectability. Expressibility
contract: the sidecar is a post-run analytic calculation, not an FDTD
output, and is labeled as such." Blind to all other Phase-5 reviews this
cycle, including my own Phase-2 critique's text (read only as a historical
artifact under review, not as a starting point). Grounded on PANEL.md in
full and LOGBOOK.md lines 1–270 (R1–R8) and 1892–2461 (T28's full
Iteration 46–53 history) before reading the exp-077 record.*

---

## 0. Verdict

**PARTIAL**, from this seat's own lens.

The mechanism finding itself — Combined REFUTE for both `PAIR_PAD` and
`PAIR_ABSORB40` on the complete two-wall instrument — is thermodynamically
clean and I find no defect in it: the absorbed-power bookkeeping behind it
(§2 below) is now correctly stated and independently reproduces exactly.
That REFUTE narrows T28 further, joining exp-075's own `ABSORB`-boundary-
reflectance REFUTE, and is not something this seat has grounds to
overturn. What keeps this from a clean RULED-OUT-and-move-on for my own
charter is that the sidecar's own **detectability** disposition (§3,
`PAIR_ABSORB40`) rests on a comparison that is not actually computed in
commensurable units (§3 below) — a real, if non-load-bearing, gap in the
one paragraph this document is my seat's to own.

---

## 1. Red Team's Attack-4 finding, independently re-verified from
`boundary_reflectance.py`'s own primitives — it holds up, and so does the
corrected code

I did not take either party's word for it. I imported `boundary_
reflectance.py` fresh, called its own `damp_e_profile` → `nu_profile` →
`n_profile_exact` → `reflection_coefficient` exactly as `pad_round_trip_
model.py::compute_r_profiles` does (same `omega600 = 2π/20`, same 31-point
`thetas` array pulled from `experiments/076/results.json::headline`), and
computed `1-|r(θ;ABSORB)|²` myself, from scratch:

```
ABSORB=40: 1-|r|² ranges 99.995874% (θ=42.0°) – 99.999159% (θ=36.0°)
ABSORB=80: 1-|r|² ranges 99.999999%(2.9e-5|r|) – 99.999999%(1.16e-4|r|)
Δ = |af80 - af40| ranges 8.409772e-06 – 4.124687e-05
```

This is bit-exact against `pad_round_trip_results.json::thermo_sidecar`
(`absorbed_frac_40_min/max = 0.9999587397839939 / 0.9999915893711646`,
`delta_absorbed_frac_min/max = 8.409772118245229e-06 /
4.124687467921273e-05`) and bit-exact against Red Team's Attack-4 cited
figures. **The corrected code's own reported range, 99.9959%–99.9992%, is
right.**

I then checked my own Phase-2 critique's arithmetic directly, the way Red
Team says to: plug the critique's own cited `|r|` endpoints into `1-|r|²`
by hand:

```
|r|=0.0029  ->  1-r² = 0.99999159  = 99.999159%
|r|=0.0064  ->  1-r² = 0.99995904  = 99.995904%
```

Both of those match *my* independent recomputation (and Red Team's) to
six decimal places — not the range my Phase-2 critique actually printed
(`99.9979%–99.9996%`). **Yes, I made the arithmetic slip Red Team's Attack
4 describes, and it is exactly the shape Red Team characterizes**: my
stated deviation-from-100% at each endpoint (0.0021% at the near-unity
end, 0.0004% at the far end) is almost precisely half the correct
deviation (0.0042%, 0.0008%) — consistent with a stray factor-of-two
somewhere in a `1-|r|²` vs. `(1-|r|)²`-flavored slip, or a mid-calculation
halving, that I did not carry through correctly at the time. I have not
dug further into which exact keystroke did it — as Red Team's own audit
notes, the root cause is immaterial to the ruling. What is not in
question after this independent recomputation: **the corrected absolute
percentages in the current `phase1_proposal.md` §3 and in `thermo_
sidecar_check`'s own output are correct; my earlier cited range was not.**

The one number from my Phase-2 critique that *does* survive intact is the
`Δ(absorbed fraction)` differential itself, `8.4×10⁻⁶`–`4.1×10⁻⁵` — I
verified this bit-exact against my own from-scratch recomputation above,
against Red Team's Attack-4 figure, and against `thermo_sidecar`'s own
JSON output. This is because, as Red Team correctly diagnosed, that
figure was evidently computed as a direct `af80 - af40` difference rather
than routed through the erroneous intermediate absolute percentages — the
two computations don't share the bug. **So: Red Team's Attack-4 finding
holds up completely on independent re-verification, including the
"corrected code's own percentages are right" half of it, and my own prior
critique's specific error is confirmed, characterized correctly (a
roughly-2× slip at each endpoint), and non-load-bearing exactly where Red
Team said it was.**

---

## 2. The `PAIR_PAD` common-mode reasoning — independently re-confirmed

Separately from the percentages: I re-verified, by reading `pad_round_
trip_model.py` line 176 directly, that `r_for["C40"]` and `r_for["G40"]`
are the literal same NumPy array object (`r_for = {"C40": r40, "G40":
r40, "C80": r80}`), not independently recomputed values that merely
happen to agree — so the absorbed-power fraction is common-mode by
code-level construction for `PAIR_PAD`, exactly as the corrected §3 now
states, and exactly as my own Phase-2 critique's steel-man (correctly)
argued before Red Team ever found the percentage slip. This part of my
prior work stands.

---

## 3. NEW finding — the T5/exp-043 "4–5 orders of magnitude below" comparison is not actually computed in commensurable units, and a same-instrument comparison that IS commensurable was sitting in this cycle's own data

The task asks me to check §3/Idealization 12's disposition for
`PAIR_ABSORB40`: *"Four to five orders of magnitude below any energy scale
this program has ever treated as thermodynamically significant (T5/
exp-043's own microbolometer-NETD floor is ~100× ABOVE readings orders of
magnitude larger than this) — argued negligible quantitatively, not by
category exemption."*

I went back to what T5/exp-043 actually measured (LOGBOOK.md's own T5
entry, line 455 area; `lab/thermo_sidecar.py`, stage 15): a **witness-
pinned absolute irradiance** (exp-043's own docket-#7 sourcing,
6.58×10⁻⁶ W/cm² central, later corrected from an earlier unsourced
placeholder) hitting a **real absorber article** (`graded_black_shell`,
or an OFF/ON σ(I) article) at bench/witness scale, run through an actual
`P_abs → ΔT → emission-band(~10 µm) → microbolometer-NETD(8.6–100 mK,
4 sourced refs)` chain, producing a temperature-rise number in Kelvin/
milli-Kelvin that is then compared, in the *same units*, against a
sensor's own noise floor.

`PAIR_ABSORB40`'s `Δ(absorbed fraction) = 8.4×10⁻⁶`–`4.1×10⁻⁵` is a
**dimensionless fractional reflectance difference** — `Δ(1-|r|²)` at a
domain-truncation boundary — with **no witness wattage pinned anywhere in
this document**, no absorber article present (§4: T1 N/A, no absorber,
no scene, confirmed by re-reading the full file), and no `ΔT`/emission-
band calculation run on it at all. Worse, the boundary it's computed at
is not a witness-scene object in the first place: Idealization 10
(independently confirmed in code this cycle, `verify_symmetric_damping`)
establishes that the `ABSORB` band is the FDTD engine's own domain-
truncation admittance layer — the identical unrealizable matched-`eps=mu`
construction on all four edges — not a physical absorber a beam could
warm and that could re-radiate into a witnessed scene. There is nothing
here for T5's chain to attach to: no pinned watts to convert the fraction
into an absolute `ΔP_abs`, and no physical object to assign a heat
capacity/emissivity to even if there were.

Comparing a unitless fractional delta with no absolute power anchor
against a milli-Kelvin-denominated detectability floor computed for a
real absorber at a pinned wattage is not "four to five orders of
magnitude below" in any sense that a physicist should accept without the
missing conversion step shown — it reads as a quantitative bound but is
actually an analogy between two different kinds of number that happen to
both be small. This is the same underlying failure shape R4/R8 exist to
police (a comparison presented as computed when the intermediate step
that would make it computed was never run), just not one that changes
any verdict here, since nothing in Test A/B routes through this sentence.

**What a valid, same-units comparison actually shows, computed from this
cycle's own already-collected data:**

```
Δ(absorbed fraction), PAIR_ABSORB40:        8.410e-06 – 4.125e-05
real Δ(theta) signal itself, PAIR_ABSORB40: ptp = 6.218e-03  (std = 1.520e-03)
                                             (experiments/076 headline series,
                                              pad_round_trip_results.json::
                                              real_delta_absorb40)
ratio (absorbed-fraction Δ / observed-signal ptp): ~1.4e-3 – 6.6e-3
```

Both quantities here are dimensionless, drawn from the identical
instrument, the identical dataset, and the identical normalization
convention this whole T28 sub-thread already uses for `amp_ratio`/`ptp` —
an actually commensurable comparison, unlike the T5 one. It says the
absorbed-power differential this pair produces is itself two-and-a-half
to three orders of magnitude *smaller than the very signal Tests A/B are
trying to explain* — i.e., even setting aside that Tests A/B already
REFUTE the coherent-echo shape/period match directly, a naive "does the
absorbed-power difference simply scale up into the observed field
perturbation" story was never plausible on energy grounds alone. That is
the actually-relevant thermodynamic argument for negligibility in this
instrument-fidelity context (is this energy scale even large enough to be
a candidate driver of the phenomenon under test), and it happens to
reinforce the same qualitative conclusion the flawed T5 comparison
gestured at — but it is the comparison this seat should have made, not
the one that borrowed a real-witness-scene detectability floor for a
scene that has neither a witness wattage nor a witness object.

**Disposition**: non-load-bearing (Tests A/B already carry the REFUTE
independent of this paragraph) but a real correction is owed. Idealization
12/§3 should either (a) drop the T5/NETD sentence entirely as inapplicable
to a no-witness-scene, no-absorber-article, no-pinned-wattage instrument-
fidelity thread, or (b) replace it with the ratio above, correctly labeled
as a same-instrument, same-units energy-scale check, not a detectability
claim in T5's sense at all.

---

## 4. Ranked candidate directions for Iteration 55 — energy-accounting lens

LOGBOOK's own Iteration-53 reconciled ranking already names most of the
board (fixed-carrier 750nm re-score; two-wall vs. 750nm leg; `PAD`-depth
causal sweep; broadband pulsed reflectance spectroscopy; full-width
750nm leg; real-absorber-article load test). From my own charter, ranked:

**1. Close the gap §3 above found: pin a witness wattage and run the real
absorbed-power differential through the already-built, trust-suite-gated
`lab/thermo_sidecar.py` chain end-to-end** (reusing exp-043's own already-
sourced ~6.58×10⁻⁶ W/cm² reference irradiance), *if and only if* a real
absorber article is ever added to this line of configs (item 3 below) —
without one, there is nothing physical for the chain to act on, which is
itself the point: today's `PAIR_ABSORB40` sidecar cannot be honestly
upgraded past "the fractional delta is small" without a real object in
the scene. Zero new FDTD on its own; contingent on item 3 for a target
to compute against.

**2. Broadband pulsed reflectance spectroscopy of the `ABSORB` boundary**
(already named, Iteration-53 Tier 1 item 5; seconded here on energy-
accounting grounds specifically). Every cycle in this sub-thread,
including this one, has treated `ABSORB`'s energy behavior as a single
number per angle at one wavelength (`1-|r(θ;ABSORB)|²` at 600nm). A
genuinely new thermal instrument class this program has not tried for
T28: measure the boundary's own **frequency-resolved** absorbed-power
profile (a handful of pulsed broadband FDTD calls, Poynting flux into the
`ABSORB` cells vs. time/frequency, not just the transfer-matrix `|r|²`
proxy) — this would show directly whether the boundary's energy
dissipation has any angle- or wavelength-structure of its own that a
purely phase/magnitude-at-one-frequency reflectance model could miss, and
would be the first time this sub-thread measures absorbed power as a
*time-domain FDTD output* rather than the THERMODYNAMICS-sidecar's own
analytic proxy — closing the gap between "post-run analytic calculation"
(this cycle, and every T28 cycle to date) and an actual measured energy
flux.

**3. Test whether the `PAD`-tied signal survives with a real absorbing
article loaded** (already named, Iteration-53 Tier 2 item 7; ranked here
specifically because it is the only queued item that would let this
seat's own sidecar attach to a real, witness-relevant absorbed-power
number for the first time in this six-cycle sub-thread's history — every
`{C40,C60,C70,C80,G40}` config to date is an *empty scene*, so every
"absorption" discussed so far, including this cycle's, is domain-
truncation-boundary bookkeeping, not a physical article warming up.
Loading a real absorber turns `PAIR_PAD`/`PAIR_ABSORB40` from a pure
instrument-fidelity question into one with an actual thermodynamic
referent, and is the precondition for item 1 above to mean anything.

None of these three re-open R1–R8 or any RULED-OUT item; all extend
already-vetted, already-committed machinery (`lab/thermo_sidecar.py`,
`boundary_reflectance.py`, `lab/fdtd2d.py::Sim.run()`).
