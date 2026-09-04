# Phase 2 Critique — PHOTONICS seat

**Panel Iteration 88, exp-111.** Charter: surface interaction, absorption
spectra, angular dependence, scattering cross-sections — is the proposal's
optical response coherent as stated, across wavelength and angle?

## Independent verification performed before writing this critique

Ran the following against real committed source/data (not re-typed prose),
per R4 discipline:

- Recomputed `KAPPA_COST_EXPONENT` from `experiments/110-.../results.json`
  directly: `t156 = sum(r156.total_wall_s.values()) = 752.2232966423035`,
  `t312 = sum(r312.total_wall_s.values()) = 6938.207038640976`, ratio
  `9.223600318696624`, `ln(ratio)/ln(2) = 3.2053299988171697`. **Matches the
  proposal's §2.0 claim exactly.**
- Recomputed the floor range and `n_resolved` sums directly from
  `results.json["r156"/"r312"]["local_diag"]` and `["n_resolved"]`:
  floor `2.3458e-4`–`2.0959e-3`; `n_resolved` sums for both r match the
  proposal's frozen §2.0 table exactly, digit-for-digit.
- Checked the two named bins directly: `results.json["r156"]
  ["named_bin_status"]["margin32"]` = `{deg: -146.25, resolved: False}`;
  `["r312"][...]` = `{deg: +168.75, resolved: False}` — confirmed. Also
  checked whether these are a mirror pair of *each other*: with `n=48`,
  centers[4]=-146.25° mirrors to centers[43]=+146.25°, and centers[46]
  =+168.75° mirrors to centers[1]=-168.75°. **They are not a mirror pair
  of one another** — each is compared only against its own r-value's own
  mirror partner. Nothing in the proposal or LOGBOOK claims otherwise;
  no inconsistency found here.
- Read `run.py`'s `mirror_pooled_floor`/`classify_item_i_local` and
  `chunk_runner.py`'s `step_once`/`build_sim` directly to confirm the
  proposed patches (floor>0 guard, upstream cost-gate call) attach where
  the prose says they do.

All numeric claims independently checked pass exactly. No arithmetic or
citation defect found in this proposal's own numbers.

## Steel-man (≤150 words)

From PHOTONICS' seat, the strongest case for this proposal: it is careful,
scoped governance work that independently re-derives every numeric claim
from primitives (the 3.2053 exponent, the real n_resolved/floor figures,
the pilot wall-times) rather than restating prior text, matching R4
discipline exactly. The `floor>0` guard fixes a genuine mathematical
defect (`abs(x)>=0` vacuously TRUE regardless of signal, silently
mislabeling a degenerate case RESOLVED), verified non-regressive on all 12
real committed cells. Item 3 — the one item with real angular/optical
content — is explicitly, reasonably deferred with a stated, defensible
sequencing argument (fix the gate before spending the FDTD budget it is
meant to protect), not silently dropped, honoring this exact sub-thread's
own repeated deferral-discipline concern.

## Sharpest attack (≤150 words)

The FI-A/B/C fault-injection triad tests only the two idealized
mirror-symmetry extremes — paired antisymmetric impulses (FI-A) and
uniform/quadratic symmetric offsets (FI-B/C) — never the realistic
intermediate case a genuine angular contaminant would produce at these
exact bins. This bench's own established ~2.8421° boundary-echo
oscillation (T28, exp-069–052) aliased against this instrument's 7.5°/bin
pitch (~2.64 cycles per bin) would land neither cleanly even nor odd under
the i↔47-i pairing — it would scramble bin-to-bin, untested by any of the
three cases. So the control proves the code's boolean logic handles two
synthetic corner cases; it does not establish the pooled floor gives a
trustworthy scale estimate against the one concrete, already-documented
noise mechanism most plausibly present at -146.25°/+168.75° — exactly the
physical question item 1 exists to arbitrate, and exactly the mixed regime
R18 discipline should guard against, not only the pure extremes.

## Verdict

**support-with-changes.**

The item-1 code fix and non-regression control are sound and independently
verified; item 4's recalibration and item 2's upstream reposition are
correctly derived and correctly scoped as governance/instrumentation
(T1 N/A holds). The gap above does not invalidate anything already
claimed — it means the proposal's own framing ("closes the last open R18
gap") is overstated: R18 is closed against the two mathematical corner
cases, not against the realistic mixed/aliased noise shape this exact
bench has already demonstrated it produces.

## Parameter change that would flip verdict to support

Add a fourth case, **FI-D**: inject a swept-phase quasi-periodic
perturbation at the established `P*=2.8421°` period (phase relative to
the mirror axis swept over e.g. 8 values spanning 0–180°) on top of a
flat baseline, and report the pooled floor's min/max recovery across that
phase sweep — demonstrating the instrument's behavior in the
partially-mixed/aliased regime rather than only the two pure extremes. If
that case is added (or already run elsewhere and shown bounded), I move to
support.
