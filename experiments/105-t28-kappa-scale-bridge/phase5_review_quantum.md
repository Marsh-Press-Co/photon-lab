# PHASE 5 — REVIEW (QUANTUM OPTICS, fresh context, blind) — exp-105

*Charter: non-classical absorption, state-dependent or coherent
interactions. Expressibility contract: mechanisms enter the bench only as
effective classical parameters — σ(I), σ(x,t), dispersive ε(ω), gain — or
Red Team strikes them. Independently re-derived every number below from
`run.py`'s own source and `results.json`'s own persisted primitives —
nothing here is taken from `NOTES.md`'s own prose on faith.*

## 0. Scope check

T1 is correctly N/A throughout — no σ(I), σ(x,t), dispersive ε(ω), or gain
is proposed, varied, or scored anywhere in `phase1_proposal.md`, `run.py`,
or `results.json`. `graded_black_shell`'s `sigma_max(κ)=0.5/κ` is a static,
position-only rescale (T8's own already-adjudicated fix, reused verbatim);
no intensity or time argument is threaded anywhere in `materials.py` or
`run.py`. This is squarely instrumentation/diagnostic work under this
seat's own expressibility contract, exactly as `NOTES.md` states.

## 1. Independent re-derivation: `predicted_ripple_period(r)` / `nyquist_margin(r)`

Re-derived directly from `run.py::geom()` (lines 142–144):

```
z_over_zr(r)            = D_EFF * LAMBDA_CELLS / r**2     (D_EFF=77, LAMBDA_CELLS=20)
predicted_ripple_period  = LAMBDA_CELLS * D_EFF / r = 1540 / r
nyquist_margin(r)        = predicted_ripple_period / (2*DENSE_PITCH) = 1540/r/4 = 385/r
```

| r | 385/r (hand re-derivation) | `results.json::geom_r.nyquist_margin` | match |
|---|---|---|---|
| 78 | 4.935897… | 4.935897435897436 | exact |
| 156 | 2.467949… | 2.467948717948718 | exact |
| 312 | 1.233974… | 1.233974358974359 | exact |

`z_over_zr`: hand re-derivation gives 0.253123 / 0.063281 / 0.015820 at
r=78/156/312 — **exact match** to `results.json::geom_78/156/312.z_over_zr`
(0.25312294543063774 / 0.06328073635765943 / 0.01582018408941486) and to
`NOTES.md`'s own frozen-prediction text. This is the corrected figure this
seat's own Phase-2 critique caught (the Phase-1 draft's hand-typed
0.0026/0.0063/0.0016 sentence was ~10× too small and never printed by the
Appendix script) — Red Team's mandatory fix 1 landed correctly: `geom()`
now computes and prints this value, and the printed value matches a clean
hand re-derivation from the stated formula, not merely from the code's own
output. **CONFIRMED, digit-exact, both against the frozen prediction text
and against results.json.**

## 2. Is the Fresnel-forced 1/r period the right physical model for what would alias?

This was this seat's own Phase-2 flip condition (adopted as mandatory fix
4/attack 7, `phase2_redteam_audit.md` §2/§5 item 3). Worth re-examining
now that real data exists, not just the pre-registered gate.

**The model's derivation is a legitimate, non-arbitrary transplant, not an
ad hoc guess.** `predicted_ripple_period=λ_cells·D_EFF/r` is the standard
two-edge/aperture (Young's-slit-style) fringe-spacing law — fringe spacing
at a fixed standoff `z=D_EFF` from two coherent edge sources separated by
`~2·r_out(r)` is `Δy≈λz/(2r_out)∝λ·D_EFF/r`, up to the same order-unity
convention choice this program's own **T21** edge-diffraction fringe model
already used (`P(θ)=λ/(A·cosθ)`, A the aperture half-width, θ=0 case
`P=λ/A`) — this cycle's `A` is the object's own growing radius `r_out(r)`
in place of T21's fixed source-taper half-width. This is genuinely the
correct physical analog (this bench's own diffracting edges — the object's
own rim — grow with `r`, unlike T21's fixed source aperture), not merely a
formula reused for convenience.

**Does it protect against a genuinely different-scaling alternative
mechanism, though?** Checked two concrete alternatives:

- **A fixed, λ-scale near-field standing-wave period (~λ/2=10 cells,
  r-independent)** — the ORIGINAL exp-103 degenerate-aliasing concern this
  whole gate lineage exists to catch. Under this alternative, `nyquist_
  margin` would be a CONSTANT `10/(2·2)=2.5` (TRUSTED) at every r, not the
  1.234 (MARGINAL) this cycle computes at r=312. The two models disagree
  in the SAFE direction here: the model actually used flags r=312 as
  *less* trustworthy than a fixed-λ/2 alternative would, not more —
  fails conservative, not permissive.
- **A domain-boundary echo (x-wall/y-wall class, T28's own R13-lineage
  candidate)** — this family's own path length scales with the DOMAIN
  (`N(r)∝κ`, i.e. ∝r, same as the object), giving period∝r — GROWING, not
  shrinking, with r. A growing period only gets safer under a
  fixed-pitch sub-sampling scheme; again fails conservative.

I could not construct a physically motivated candidate mechanism, tied to
this bench's own actual geometry, whose period would shrink *faster* than
1/r and therefore escape the 1/r-scaled gate's own protection at r=312.
**Verdict on this sub-question: the model is a reasonable, correctly-
motivated choice — the single most natural candidate given this bench's
own geometry — but it remains one assumed mechanism among a family that
was never exhaustively enumerated or cross-checked against an alternative
scaling law before the MARGINAL tier was accepted at face value.** That
this cycle's own gate correctly downgrades r=312 to
MARGINAL-REDUCED-CONFIDENCE (not silently TRUSTED) and `NOTES.md`'s Result
section states this plainly is the right epistemic posture regardless —
the gate does its job by flagging uncertainty, not by resolving it. Not a
defect; a legitimate scope boundary this cycle discloses honestly (see §5,
Next item 2's own r=312 settling gap, which compounds with this same
uncertainty).

## 3. P3 headline — independent verification of the accelerating collapse

Re-derived directly from `results.json::kappa_windows` (not from
`NOTES.md`'s own prose):

```
k78, k156, k312 = 0.018336958179764707, 0.0008866623871477821, 4.79303718569495e-06
k78/k156  = 20.68087971877445    ("~20.7×", NOTES.md)      — matches
k156/k312 = 184.9896741452515    ("~185×", NOTES.md)       — matches
shape_ratio = (k78-k156)/(k156-k312) = 19.787847024468125  — matches
  results.json::p3.shape_ratio (19.787847024468125) EXACTLY, digit-for-digit.
```

`p3.model_A_miss=0.8554612460207963` (85.55%) and `model_B_miss=
0.759276334508564` (75.93%) both independently recompute from the fitted
`(B,C)` pairs against the pre-registered `x78/x156/x312` values in
`results.json::p3` — both catastrophically outside the 25%/60% bands, as
claimed. **CONFIRMED, exact.**

## 4. The central expressibility-contract question: does this smuggle in any non-classical effect?

**No — and it structurally cannot, by construction, regardless of the raw
magnitude.** `lab/fdtd2d.py` is a deterministic, real-valued, linear 2D
TMz Maxwell solver: `graded_black_shell`/`pec_disk` are static, real
`σ(x)`/`ε(x)` arrays with no intensity, time, or state dependence anywhere
in this experiment's own code path (confirmed by direct read of `_run()`,
lines 170–178 — two `materials.*` calls with fixed numeric arguments, one
`add_line_source`, one `sim.run(steps)`). Every field this cycle reads
(`kappa_window`, `kappa_region_wide/point`, `delta_phi`) is a ratio or
phase difference of ordinary classical E-field phasors from that same
deterministic solve. There is no σ(I), no gain, no dispersive resonance,
no anything this seat's own charter would recognize as a "coherent
interaction" in the non-classical sense — "coherent" in this document's
own vocabulary means only "phase-resolved, not incoherently intensity-
summed," a classical-optics usage (interference of classical fields),
identical to how T21/T25/T26 used the word elsewhere in this program.

Given that, a mundane classical explanation is not merely *sufficient* —
it is the *only* thing available, since nothing else was built into the
pipeline. The accelerating four-orders-of-magnitude collapse is fully
consistent with ordinary classical near-field shadow-formation: the window
offset from the object's own surface is held FIXED in absolute cells (27
cells) while `R_COAT(r)` grows self-similarly, so the offset shrinks from
`27/78≈35%` of the object's own radius at r=78 to `27/312≈8.7%` at r=312 —
the measurement plane is pushed progressively closer to "flush with the
surface" in *relative* terms as r grows, exactly where classical near-field
intensity is expected to plunge steeply (evanescent/near-zone falloff of
the diffracted field close to a growing absorbing/scattering boundary).
Nothing about this requires, or could express, physics beyond a classical
Maxwell solve. If the magnitude "strains credulity" at all, it strains
*numerical* credulity (is `κ(312)=4.79×10⁻⁶` still above this bench's own
established floor, or is it approaching discretization/round-off noise? —
`NOTES.md`'s own Next item 1 correctly identifies this as the live open
question) — not physical credulity, and certainly not a quantum one. This
is exactly this seat's own expressibility-contract finding to make: **the
magnitude does not, and structurally cannot, exceed what this classical
engine can produce, because nothing non-classical was ever instantiated in
the pipeline it ran through.**

## 5. P4 quintile-period reproduction — `estimate_period()`'s own stated algorithm

**r=156 (full independent reconstruction from raw persisted primitives).**
`run.py` computes `residual_point_156 = point156[x] - wide156[x]`
(lines 589) and feeds each quintile's 10–11-point slice through
`estimate_period()` (lines 250–287). `results.json::r156.point_channel`
and `results.json::r156.wide_channel` persist the raw per-`x`
`kappa_region_point`/`kappa_region_wide` values, so this is independently
reconstructible from scratch, not merely from the diagnostic fields.
Re-implemented `estimate_period()` verbatim (same FFT/parabolic-interpolation
logic) in a standalone script, rebuilt `residual_point` from the two raw
channels, and re-ran all 5 quintiles:

| quintile | x-range | n | `results.json` period | independent recomputation |
|---|---|---|---|---|
| 0 | 682–702 | 11 | 33.05017605103204 | 33.05017605103204 |
| 1 | 704–724 | 11 | 32.75884976634453 | 32.75884976634453 |
| 2 | 726–746 | 11 | 34.08252715332239 | 34.08252715332239 |
| 3 | 748–766 | 10 | 24.863394908518295 | 24.863394908518295 |
| 4 | 768–786 | 10 | 32.49023817523714 | 32.49023817523714 |

**All 5 reproduce exactly, digit-for-digit**, from raw primitives, not
merely from the code's own diagnostic fields — the strongest form of
reproduction this seat can perform.

**r=312 (self-consistency only — a genuine, disclosed data-completeness
gap).** `results.json::r312` does NOT persist `point_channel`/
`wide_channel` (only `quintiles`, `p2`, `p4`, `nyquist_tier`, `committed`)
— confirmed by direct key inspection; `run.py`'s own r=312 branch (lines
670–677) computes `wide312`/`point312` locally but never adds them to the
persisted dict at the bottom of `main()` (unlike r=156's explicit
`wide_channel=wide156, point_channel=point156` at line ~850). This means
r=312's own quintile periods cannot be independently rebuilt from raw
field ratios by a reviewer working only from `results.json` — only from
the persisted `period_diag` fields (`interp_bin`, `nfft`, `peak_idx`,
`peak_power`, `median_power`). Checked self-consistency of the one
formula that *is* fully specified by those fields
(`freq_per_cell=interp_bin/(nfft·dx)`, `period=1/freq_per_cell`, `dx=2`):
all 5 r=312 quintile periods reproduce EXACTLY from their own persisted
`interp_bin`/`nfft` values (e.g. quintile 0: `interp_bin=4.1533671764903835`,
`nfft=64` → `period=30.81836846126392`, matching `results.json` to the
last printed digit; same for all 5). This confirms the *algebra* was
applied correctly to whatever raw data fed it, but — unlike r=156 — I
cannot rule out an upstream error in how `residual_point`/`wide` were
constructed for r=312, since those intermediate arrays are not on the
record. **This is a genuine, if minor, reproducibility gap distinct from
any defect found in the results** (see §7, Next item 3).

## 6. Verdict

**CONFIRM-WITH-GAPS.**

Every number this task asked me to independently re-derive reproduces
exactly: `predicted_ripple_period`/`nyquist_margin` at all three r (§1),
the P3 headline collapse figures and `shape_ratio=19.787847…` (§3), and
all 5 r=156 quintile periods from raw primitives plus all 5 r=312 quintile
periods from their own persisted diagnostics (§5). The Fresnel/Nyquist
gate's own physical model, while not the only conceivable one, is the
correctly-motivated choice for this bench's actual geometry and fails
conservative against the two concrete alternatives I could construct
(§2) — not a defect, a disclosed, defensible modeling choice. The
accelerating `kappa_window` collapse carries zero non-classical content by
construction and cannot strain this seat's own expressibility contract,
because nothing non-classical was ever instantiated in this cycle's
pipeline (§4). The one gap I found — r=312's raw `point_channel`/
`wide_channel` never persisted, unlike r=156's — is real, independently
confirmed against `run.py`'s own source, and narrows the reproducibility
class of r=312's own P4 verdict from "independently reconstructible from
raw fields" to "internally self-consistent from its own diagnostics only."
Non-load-bearing to any scored verdict this cycle (P4 at r=312 is already
reported at reduced confidence via the MARGINAL Nyquist tier, and no claim
anywhere treats it as equally trusted to r=156's TRUSTED reading) — but
worth naming plainly rather than leaving implicit, per this program's own
R4/R6 discipline on reproducibility gaps.

## 7. Top-3 ranked candidate directions for Iteration 83 (QUANTUM OPTICS' own charter)

1. **A resolution/floor check on `kappa_window(312)=4.79×10⁻⁶` specifically**
   (NOTES.md's own Next item 1, this seat's own top pick) — is the
   accelerating collapse a genuine near-field coherent-field effect, or is
   it approaching this bench's own numerical noise floor? A cheap,
   zero-new-mechanism `cpl 20→30` R3 check at r=312's own `BEHIND` window
   (not merely the P4 point/wide channels already checked) would directly
   distinguish a real, resolution-stable field ratio from discretization
   noise — the single highest-value item this cycle's own result creates,
   squarely inside this seat's own coherent-field-precision charter.
2. **Persist r=312's raw `point_channel`/`wide_channel` (or equivalently,
   the `residual_point`/`wide` arrays) to `results.json`** — a small,
   zero-marginal-cost fix (the values are already computed in-memory at
   lines 670–677, simply never written out) that closes the reproducibility
   gap named in §5 and would let any future reviewer independently rebuild
   r=312's own quintile periods from raw fields the same way r=156's are
   already reproducible today.
3. **The settling-independence leg at r=312** (NOTES.md's own Next item 2)
   — this cycle's own disclosed idealization, now doubly motivated: r=312
   already carries a MARGINAL Nyquist tier (§2), and an unchecked settling
   artifact there would compound with, not merely coexist alongside, the
   aliasing-margin risk on the exact coherent-phase-resolved channel this
   seat's own charter is responsible for auditing.
