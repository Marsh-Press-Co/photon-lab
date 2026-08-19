# PHASE 5 — REVIEW · QUANTUM OPTICS (fresh context) · exp-045, Panel Iteration 22

**Charge executed:** independently verify that Block C's "role inversion" of
`lab.kinetics.pulse_train_segments` actually builds the ON-exposure/OFF-gap
alternation it claims to (not something subtly different, and not what my
own Phase-2 critique this cycle literally proposed either — that proposal is
checked too); assess whether the measured population-memory ratios (1.0051 at
5τ, 1.4509 at 0.5τ) are physically sensible against exp-038's own Host-D
findings; verify the disclosed `endswith("5tau")` substring-collision bug is
actually fixed, not just claimed fixed; and judge whether the DECOUPLED ΔT
scope limitation is acceptable for a "bounded" check or understates
something material to my own Iteration-21 concern.

**Process note, stated up front:** my own Phase-2 critique this cycle
(`phase2_critique_quantum.md`) proposed a specific call —
`pulse_train_segments(k_f_ambient, k_r, A=1, T_pulse=dwell_central,
dt_sweep, n_pulses=5)` — that Red Team's mandatory fix 5 cited as "exactly
QUANTUM's proposed design." **What was actually built does not match that
literal call.** Section 1 below establishes why the deviation is a correction
of a real defect in my own proposal, not an unfaithful implementation of it.

---

## 1. Does the role-inversion trick build the segment sequence I intended?

`lab/kinetics.py::pulse_train_segments(k_f_ambient, k_r, A, T_pulse,
dt_sweep, n_pulses)` builds, verbatim from source:

```
k_f_pulse = k_f_ambient * A
segs = [(k_f_ambient, k_r, dt_sweep), (k_f_pulse, k_r, T_pulse)] * n_pulses
     + [(k_f_ambient, k_r, dt_sweep)]
```

`run.py`'s Block C call:

```python
segs = kin.pulse_train_segments(
    k_f_ambient=k_f_on, k_r=k_r_d, A=0.0,
    T_pulse=dt_gap, dt_sweep=dwell_central, n_pulses=5)
```

Substituting: `k_f_pulse = k_f_on * 0.0 = 0.0`. The segment list becomes
`[(k_f_on, k_r_d, dwell_central), (0.0, k_r_d, dt_gap)] × 5 +
(k_f_on, k_r_d, dwell_central)` — i.e. **ON (exposure), OFF (relaxation),
ON, OFF, …, ON** — 11 segments, 6 ON + 5 OFF. This is exactly the alternation
the docstring claims.

**Hand-traced by hand for (r=1e-1, gap_name="0.5tau"), the Host-D worst-case
axis point**, using `relax_exact`'s closed form directly (n_eq=k_f/(k_f+k_r),
τ=1/(k_f+k_r)):

- ON: k_f=1.0, k_r=10 → n_eq=0.090909, τ=0.090909 s
- OFF: k_f=0.0, k_r=10 → n_eq=0, τ=0.1 s
- dwell_central=0.066667 s (10°/150°·s⁻¹), dt_gap=0.5τ_k=0.5/11=0.045455 s

Propagating n=0 through 11 segments by hand (convex-combination update at
each step) gives n after segment 1 (first ON) = **0.047245**, and after
segment 11 (sixth/final ON, following 5 complete OFF gaps) = **0.067909**.
`results.json`'s own `n_first_pulse` for this point is
**0.04724497262820006** and `n_periodic` is **0.06791082781081066** — matches
my hand derivation to 5 significant figures (residual is my own
hand-arithmetic rounding, not a code discrepancy). Ratio 0.067909/0.047245 =
**1.4374**, matching the stored `periodic_over_first_ratio` = 1.4374191...
exactly.

The boundary-index bookkeeping is also independently verified: with 11
segments, `t_arr`/`n_arr` has 12 entries (index 0 = n0, then one entry per
segment). ON segments sit at 0-indexed segment positions 0,2,4,6,8,10 →
their *end* states land at `n_arr` indices 1,3,5,7,9,11 — exactly the
`on_end_idx = [1, 3, 5, 7, 9, 11]` `run.py` uses. **Confirmed correct: the
role-inversion trick builds the physically-intended ON/OFF alternation, and
the code extracts the ON-end (peak) population at the right indices.**

### But it does not implement the call I literally proposed — and that is the correct outcome, not a deviation to flag as a defect

My own Phase-2 critique specified `A=1`. Tracing that literally: with `A=1`,
`k_f_pulse = k_f_ambient · 1 = k_f_ambient` — **the "pulse" segment and the
"ambient" segment would carry the identical generation rate**, regardless of
what numeric value `k_f_ambient` is set to. There is no way to read my own
proposed call that produces a genuine ON/OFF (or high/low) distinction: if
`k_f_ambient = k_f_on` (the Host-D rate), both segments sit at the same rate
and the alternation is vacuous (population just relaxes monotonically toward
one n_eq throughout, never distinguishing "exposure" from "gap"); if
`k_f_ambient = 0` instead, then `k_f_pulse = 0·1 = 0` too, and *neither*
segment ever generates population at all. **My own literal Phase-2 proposal
was underspecified/broken as written — it cannot produce a working
ON-exposure/OFF-gap test for any value of `k_f_ambient`.** What was actually
built (`A=0.0` with the roles swapped so the long `dt_sweep` slot carries the
real ON rate and the `T_pulse` slot is zeroed to carry the OFF gap) is a
disclosed, reasoned repair of that defect, not an unfaithful rendering of a
correct instruction. Credit where due: Red Team's own audit (Attack 9) and
the implementer got this right where my own critique-stage text did not, and
said so plainly in the docstring rather than silently substituting a
different call. **Finding: Block C's role-inversion is correct; my own
Phase-2 proposal, taken literally, was not implementable as I wrote it.**

### A second, real idealization the docstring's "role inversion" note does not surface

The role-inversion note discloses *which argument slot means what* — it does
not disclose that this also changes the **physical picture** relative to
exp-038's own Test B. In exp-038, the "ambient" segment was never a true
OFF/dark state — `k_f_ambient` there is the *same* nonzero rate used
throughout, so population relaxes only partway toward a positive `n_eq`
during the gap, and continues climbing slightly the whole time. In exp-045
Block C, `A=0.0` makes the OFF segment a **true dark state** (`k_f=0`,
population relaxes all the way toward `n_eq=0`, governed by `k_r` alone). For
a linearly-pumped FCA host, this is defensible as the more literal reading of
"the beam has moved on, nothing is illuminating this point" — but it is a
different forcing assumption from exp-038's own convention, not a mechanical
re-use of it, and this specific point is not called out anywhere in the
docstring, NOTES.md, or Red Team's audit. It also happens to be the
**generous** direction for constraint-3/4 (a real ambient light source
continuing to weakly pump the material between sweeps — which T17's own
structural finding says is physically present in the witness scene — would
leave *more* residual population at each gap's end than a hard-zero
assumption does, not less). Low severity given the margins found (Section 4
below), but a real, uncredited idealization, not merely a bookkeeping note.

---

## 2. Are the measured ratios (1.0051 at 5τ, 1.4509 at 0.5τ) physically sensible against exp-038's own Host-D findings?

Pulled exp-038's own Host-D, `dt_sweep="0.5tau"` rows directly from
`experiments/038-.../results.json` (all 15 host-D/ratio/A combinations):
ratios range **1.0000–1.2865**, with the maximum (1.2865) occurring at
r=1e-9 — the same ratio point (r=1e-9) where exp-045 Block C's own maximum
(1.4509) occurs. Order-of-magnitude and qualitative shape (small-r ratios
saturate to one r-independent ceiling; the ceiling shrinks as r grows toward
1) match exactly, and 1.4509 sits comfortably inside exp-038's own
programwide 0.5τ range (1.00–2.106, spanning Hosts D and E) — **not an
outlier, not a red flag.**

But NOTES.md's own comparison language ("matching exp-038's own established
1.4–1.6 finding" / "matching exp-038's own order-of-magnitude finding at a
different pulse duration") is **loosely true but imprecisely stated**: the
*programwide* 1.4–1.6 figure it cites was exp-038's own **rough impulse-train
estimate**, which exp-038's own Phase-5 review (LOGBOOK.md Iteration 15)
already found the measured data does not tightly obey (measured range was
1.00–2.106, not 1.4–1.6). The more relevant, apples-to-apples comparison —
exp-038's **own Host-D-specific** 0.5τ maximum, 1.2865 — is not cited
anywhere in exp-045's record. exp-045's 1.4509 exceeds that specific number
by **~13%**. Given Section 1's finding (a genuinely different OFF-gap
forcing assumption, plus a shorter/different exposure duration — 66.7ms vs
exp-038's fixed 100ms — plus a different "first" measurement convention:
exp-045's first-ON measurement starts from a truly cold `n0=0`, while
exp-038's "first pulse" follows one prior ambient dwell that already builds
some population before the first pulse is even measured), a ~13% elevation
relative to exp-038's own Host-D figure is the physically expected direction
and rough magnitude, not a coincidence and not an error. **Verdict: the
numbers are physically sensible and consistent with exp-038's Host-D
findings; the specific comparison the record draws is real but under-precise
— it should have named the Host-D-specific 1.2865 figure and the mechanism
for the ~13% gap, not only the looser programwide band.** This is a citation
precision issue, not a numerical defect — nothing here should be read as
casting doubt on the 1.4509 value itself, which I independently reproduced
by hand in Section 1.

---

## 3. Is the disclosed `endswith("5tau")` bug actually fixed?

Confirmed directly: `"0.5tau".endswith("5tau")` evaluates `True` in Python —
the collision NOTES.md describes is real (the last four characters of
`"0.5tau"` are literally `"5tau"`). The **committed** `run.py` does not use
`endswith` or any string-parsing of the dict key anywhere in Block C. Each
point's `gap_name` is stored as an explicit field at construction time
(`block_c_points[f"r{r:.0e}_{gap_name}"] = {"r": r, "gap_name": gap_name,
...}`, `gap_name` bound directly from the `for gap_name, dt_gap in (("5tau",
...), ("0.5tau", ...))` loop variable — never re-derived from the key
string), and the aggregation filters use exact equality:

```python
max_ratio_5tau = max(... for v in block_c_points.values() if v["gap_name"] == "5tau")
max_ratio_05tau = max(... for v in block_c_points.values() if v["gap_name"] == "0.5tau")
```

`"5tau" == "0.5tau"` is `False` — exact string equality does not have the
substring-collision failure mode `.endswith` does. I re-ran the aggregation
independently from `results.json`'s own 8 points (Section 2's table above)
and reproduced `max_ratio_5tau=1.0051247...` and `max_ratio_0.5tau=
1.4509044...` exactly, confirming both that the filter is correct *and* that
it is not silently mixing the two gap settings (the two filtered sets are
disjoint and each has exactly 4 members, one per ratio, as expected).
**Verdict: genuinely fixed, not merely claimed fixed. Grep confirms no
remaining `.endswith` call anywhere in Block C's aggregation path.**

---

## 4. Is the DECOUPLED ΔT scope limitation acceptable for a "bounded" check?

Block C reports the **kinetics** population ratio via the exact segment
integration (`n_first`, `n_periodic` — genuinely exact, not decoupled: these
come straight out of `integrate_segments`, the same machinery Block A and
exp-038 both trust). What is *not* exact is the **thermal** consequence:
`dT_first_decoupled = dt_ss_full · n_first` and `dT_periodic_decoupled =
dt_ss_full · n_periodic` are a bare algebraic scaling, not a solve of the
coupled kinetics-thermal ODE with the correct (nonzero) initial population
at the start of each later ON segment. `coupled_kinetics_thermal_dT` — the
one closed form this program has that *does* solve the coupled ODE exactly —
is stated, correctly, to require `n(0)=0`, and is never called in Block C.

**Is this material?** Block A's own `host_d_witness_dwell_consistency_check`
— computed at the *exact same* `dwell_central` and the *exact same* Host-D
ratios Block C uses — already quantifies how far the decoupled shortcut
drifts from the exact coupled solution for a **cold-start** (`n0=0`)
exposure: 1.44–1.50% relative difference (matching exp-044's own published
figure, reproduced again here). That number bounds how wrong
`dT_first_decoupled` can be. It does **not** bound `dT_periodic_decoupled`,
because the periodic exposure does not start at `n0=0` — it starts at
whatever population survived the preceding OFF gap (e.g., ≈0.043 at the
r=1e-1/0.5τ point traced in Section 1, not 0). No closed form or numerical
check anywhere in this program's own record currently bounds the coupled
thermal response for a *warm-started* exposure. Given the thermal time
constant (`τ_thermal` ≈ 0.5–1.6ms across Block B's two self-consistent
regimes) is roughly 40–130× shorter than `dwell_central` (66.7ms) and
1–2 orders of magnitude shorter than most of the swept OFF gaps, the thermal
system should track the (slower) population signal closely in the *typical*
case — but this is a plausibility argument, not a checked bound, and the
worst Block-A points (R≈0.67–0.73, i.e. dwell comparable to τ_kinetics — the
same regime the Host-D r=1e-1 point in Section 1 actually sits in) are
exactly where Block A's own sweep shows the decoupled approximation is
*least* accurate. **Given the huge margin already found (27,080× below
`netd_lo` at the worst Block-C point), this gap cannot plausibly flip the
UNDETECTABLE verdict — a coupling correction of even 50% would leave >13,000×
margin.** But it is a real, quantifiable hole specifically in the piece of
physics my own Iteration-21 concern was about (population memory *and its
thermal consequence*, not population memory alone), and NOTES.md's framing
("bounded, not a new closed-form solution... a disclosed scope limit") is
honest about the gap existing but does not attempt to bound its size the way
Section 4's argument above does. **Verdict: acceptable as a "bounded" check
for THIS cycle's verdict (does not threaten UNDETECTABLE), but the gap is
real, not fully closed, and specifically sits inside my own concern's actual
substance — recommended as a low-cost Iteration-23/24 follow-up (see
priority #2 below), not left as a permanent idealization.**

---

## Cross-check against my own Iteration-21 concern, directly

Iteration 21's own record (LOGBOOK.md, Iteration 21 close) states my
concern verbatim: "Block A tests only a single cold-started dwell, not the
repeated-sweep/dose-accumulation regime exp-038 (Iteration 15) already
flagged Host D... as relevant to." Block C directly answers this: it is a
genuinely repeated-sweep test (5 ON/OFF cycles, not a single cold dwell), it
targets Host D as I asked, it reuses exp-038's own 5τ/0.5τ bounding-pair
convention as I asked, and — per Sections 1–3 above — it is correctly built
and its numbers are physically sensible. **My Iteration-21 concern is
substantially, not fully, closed**: the *population*-memory half is now
measured directly and correctly; the *thermal consequence of population
memory under a warm restart* (Section 4) remains an open, quantified-as-
low-risk-but-unverified corner.

---

## Verdict for the cycle: **PARTIAL**

The core deliverables (Block A's coupled-ODE sweep, Block B's h_conv/mass_kg
correction, Block C's dose-accumulation check) are real, independently
re-derivable, and land where claimed — I found zero arithmetic defects
anywhere I checked by hand. Block C in particular is a genuine, correctly-
executed override of a two-cycle-running deferral, and directly answers the
substance of my own Iteration-21 catch, not merely its letter. This earns
more credit than a bare PARTIAL usually implies. But per this program's own
established standard (verdict turns on whether a cycle's open questions
close, not a favorable count), two real gaps remain, both disclosed at some
level but neither fully closed: (1) the coupled-thermal-response-to-a-
warm-started-exposure question Section 4 identifies, genuinely unresolved
and inside my own concern's actual substance, though low-risk given the
margins; (2) the imprecise Host-D-specific numeric comparison in Section 2,
a documentation gap, not a numeric one. Neither threatens the UNDETECTABLE
finding. **PARTIAL, trending toward PROMISING** — this is the strongest
Block-C-specific result this thread has produced, and the remaining gaps are
small, quantifiable, and cheap to close.

---

## Ranked top-3 candidate directions for Iteration 23

**#1 — QUANTUM's aperture-consistent single-coherent-mode beam check
(standing Checkpoint-4 tripwire).** Per LOGBOOK.md Iteration 21's own close
and PLAN.md's carried Iteration-22 Tier-2 listing, this has now been
deferred twice (Iterations 19→20, 20→21) with an explicit, on-the-record
rule that a further deferral "fires Checkpoint criterion 4 without further
debate." It was correctly not mandatory for Iteration 22 (ELECTROMAGNETISM's
lead cycle, occupied with Block A/B/C above), but nothing in this cycle's
record does this check, and the task brief for this review confirms it is
now due at Iteration 23. **Yes, this should be my #1 pick** — not because it
is scientifically more urgent than #2 below, but because the program's own
house discipline makes it non-negotiable: a further deferral is a
program-integrity failure this panel has pre-committed to treat as an
automatic Checkpoint trigger, and QUANTUM is the only seat that can execute
it. It should be scheduled and executed at the very next opportunity this
seat leads or is otherwise tasked, not folded silently into a future
non-QUANTUM-led cycle's bundle the way Block C nearly was for a third time.

**#2 — Extend `coupled_kinetics_thermal_dT` (or a sibling closed form) to a
nonzero initial population, and re-run Block C's periodic-pulse ΔT through
it.** Closes Section 4's gap directly: the coupled ODE
`dn/dt=k_f(1−n)−k_r·n, n(0)=n0≠0`; `dΔT/dt=(1/τ_th)(ΔT_ss·n(t)−ΔT),
ΔT(0)=ΔT0` has a closed form of the same shape as the existing `n0=0`
solution (an extra term proportional to `n0·e^{−t/τ_k}` propagates through
the same integrating-factor derivation my Phase-2 critique this cycle
already carried out for the `n0=0` case) — this is a small, mechanical
extension of already-verified algebra, not new machinery, and at near-zero
marginal FDTD cost. Directly retires the one piece of my own Iteration-21
concern Block C left open.

**#3 — Reconcile and precisely re-state the exp-045-vs-exp-038 Host-D
0.5τ comparison** (Section 2): cite exp-038's own Host-D-specific 1.2865
figure (not only the looser programwide 1.4–1.6 band), and disclose the
~13% elevation's likely cause (the hard-zero-OFF-gap idealization identified
in Section 1, distinct from the disclosed argument-role-inversion) as a
named idealization, not just an implicit consequence of the role-inversion
note. Cheap (desk-only, no new run), but real — the current record risks a
future cycle citing "matches exp-038" without noticing the specific number
it should match is different from the one actually cited.
