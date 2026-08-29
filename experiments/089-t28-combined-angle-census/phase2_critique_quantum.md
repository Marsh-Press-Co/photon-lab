# PHASE 2 — CRITIQUE · QUANTUM OPTICS · exp-089

## Verification performed (before the deliverable below)

Independently reproduced, from raw primitives, every load-bearing number
this critique turns on — not merely re-stated:

- **R13 desk margins** (§4 table): recomputed `frac_contrast_of(θ)=|delta_scene|/|C40_C|`
  and `FLOOR=0.10×RMS` directly from `experiments/083-.../results.json::per_theta`
  (31-point window). Reproduced **exactly**: RMS=1.917438×10⁻³, FLOOR=1.917438×10⁻⁴,
  margins 2.1709×/1.4764×/1.3095× at 37.2°/40.2°/41.4°, and the cited prior-point
  margins (3.879×, 7.495×, 8.019×, 6.589× at 36.0°/38.4°/38.8°/41.8°) — no R4 slip.
- **Q3's interpolation arithmetic**: reconstructed `frac_p_abs` at 36.0°/41.8° from
  `retroactive_exp087_reclassification` (`ratio_k×frac_contrast`) and at 38.4°/38.8°
  from `results.json::frac_p_abs`, then reproduced both cited 37.2° estimates exactly
  (local trend 1.6348×10⁻³, wide trend 3.0514×10⁻³) and the cited ">3× miss at 38.4°"
  claim exactly (wide-trend-predicted 4.1373×10⁻³ vs. actual 1.3041×10⁻³ = **3.172×**).
- **Q4's REFUTE-threshold anchors**: reproduced both cited "smooth trend" values
  exactly (6.5427×10⁻³ at 40.2°, 7.0463×10⁻³ at 41.4°).

Everything the document cites numerically checks out. The finding below is about
what these correctly-computed numbers, read together, imply — not an arithmetic
error.

## Steel-man

R14's own three-part discharge is applied with real discipline, not ritual. (a)
is honestly deferred — Idealization 10 and §4 both state plainly it needs data
this proposal doesn't have, and nothing in Q3/Q6 secretly assumes it: Q3's bands
are built by interpolating `frac_p_abs` itself (the numerator time-series), never
by assuming the *parent* curves `p_abs_w(C40,·)`/`p_abs_w(G40,·)` are smooth —
so a Phase-4 R14(a) failure at the new angles would not retroactively invalidate
Q3's own logic, only its inputs. (c) is disclosed with a real, quantified margin
(0.02–0.075° over the half-period bound), not smoothed into a passing aggregate.
The design's own quantitative self-awareness — flagging its own Q3 interpolation
as "demonstrated unreliable" from a documented 3.17× miss at 38.4° — is exactly
the self-skeptical posture this exact document's own R14 founding instance
required, and it is applied honestly where it's applied.

## Sharpest attack

R14(b)'s "fit declined" is honest about *not* running the formal fit — but Q4,
the replacement it runs instead, quietly imports the fit's inferential weight
through a biased back door, without the fit's own null-under-noise discipline
(R5/R10, which the document itself says "still applies to any FORMAL period
claim" — implying, wrongly, that it doesn't apply here). Q4's REFUTE signatures
(≥5.5×10⁻³ at 40.2°, ≥6.0×10⁻³ at 41.4°) are anchored to "smooth 38.8°→41.8°
trend" values (6.54×10⁻³, 7.05×10⁻³) computed by the **identical linear-
interpolation method the document's own Q3 paragraph, four pages earlier,
documents as overestimating `frac_p_abs` by 3.17× at the nearest tested point**
(38.4°, inside this same span). That bias runs in exactly the direction that
would produce a false REFUTE: if the true no-periodicity trend at 40.2°/41.4°
is similarly ~3× smaller than the naive interpolation implies, the genuinely
smooth-continuation case could still read comfortably below both REFUTE
thresholds — a false CONFIRM, manufactured by a comparator this document
already proved unreliable in this exact regime, not by inherited periodicity.
The CONFIRM side is not exposed to this (both operands become real FDTD
measurements at Phase 4), but REFUTE is defined against a value never
independently re-derived from a bias-corrected baseline. This is the R5/R10
look-elsewhere failure shape — an uncontrolled comparator deciding a
CONFIRM/REFUTE call — arriving through the door R14(b) explicitly left open by
declining the disciplined route.

## Verdict

**Support-with-changes.** The desk-computable R13 margins and R14(a)/(c)
discharge are sound and independently reproduced exactly; Q4's downstream role
is explicitly disclaimed as "directional... not a substitute for" the formal
fit, and Q3/Q6's headline classification does not strictly require Q4 to
CONFIRM — so this does not warrant opposition. But as written, a Q4 REFUTE
verdict is not trustworthy evidence against periodicity, and Q6's framing
("If both... hold their Q3 CONSISTENT lean") invites exactly the informal
reliance on Q4 that R5/R10 exist to prevent once Phase 5 prose starts citing
it — this sub-thread's own disclaimer-erosion history (four confirmed
instances, the most recent firing Checkpoint criterion 4 one cycle ago) is
direct evidence that a caveat stated once in §6 does not reliably survive to
every later citation.

## Parameter change that would flip toward unqualified support

Before Phase 4: redefine Q4's REFUTE signatures against a bias-corrected
reference (e.g., the wide-trend value divided by the empirically observed
38.4° overestimation factor, ≈3.17×, or equivalently against the *local*
narrow-window trend the same way Q3's own more-trusted estimate is built) —
or, more conservatively, drop Q4's REFUTE/CONFIRM verdict language entirely
and report it only as a raw number alongside the real fit still queued
(Idealization 12), never as a labeled CONFIRM/REFUTE finding that Q6 or a
future Phase-5 citation could treat as load-bearing.

## Secondary note (non-load-bearing, flagged for self-skeptical discipline)

Idealization 13 asserts the inverted `back_frac`/`fwd_frac` labels "are not
read anywhere in this cycle's own scored quantities" — an absence claim, in
the present tense, about code that does not exist yet (this is a Phase 1
proposal; no `run.py` has been written). Unlike exp-087's own NOTES.md, which
grounded the identical claim with "confirmed by reading `run.py::main()` in
full," this document cites no check at all — it is carried forward from
exp-088's own Idealization 12 as an assumption about machinery being reused
unmodified, which is a reasonable inference but not yet a verified fact for
*this* cycle's own code. Given this seat's own prior false "no fourth instance
exists" claim at exp-088 (Iteration 65, rejected by Red Team), flagging this
now rather than after Phase 4: this claim should be re-verified by grep against
the actual committed `run.py` once it exists, not silently inherited as
already-true.
