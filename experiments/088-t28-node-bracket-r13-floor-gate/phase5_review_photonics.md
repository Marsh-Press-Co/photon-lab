# PHASE 5 — REVIEW · PHOTONICS · exp-088 · Panel Iteration 65/66 handoff

*Fresh context, blind to any other seat's current-cycle Phase-5 output. Read
in full: LOGBOOK.md's RULED OUT (R1–R13) and LIVE THREADS/T28 through
Iteration 64/exp-087; PANEL.md; the complete exp-088 cycle record
(`phase1_proposal.md`, all five Phase-2 critiques, `phase2_redteam_audit.md`,
`phase3_synthesis.md`, `NOTES.md`, `run.py`, `results.json`); exp-087's
`results.json`/`NOTES.md`. No FDTD run; no other file modified.*

## Verdict

**CONCUR-WITH-RESERVATIONS (this sub-thread's own PARTIAL house convention —
no PROMISING/RULED-OUT candidate-physics claim exists to grade; this is T28
instrument work).** I concur with every arithmetic and gate result as filed
— I independently rebuilt `frac_p_abs(38.4°)` and `ratio_k(38.4°)` from
`sigma_ext`/`ratio_abs_ext`/`p_abs_w` primitives and they reproduce exactly;
no R4-class slip anywhere. I do **not** concur that the record's own
treatment of the 38.4° dip — filed as "disclosed, not adopted... this
cycle's own data cannot distinguish those readings" — is the end of the
optical story. On my own charter (angular/wavelength coherence of the
absorbed-power channel), there is a specific, checkable, better-supported
explanation the write-up never states, and it changes which follow-up is
actually decisive.

## 1. Independent recomputation (not trusted from the summary fields)

Traced from `results.json::widths` (BOX_A, the leg `thermo` actually uses)
and `lab/thermo_sidecar.py::absorbed_power_established_ratio`, which gives
`p_abs_w = i_incident_w_cm2 · 1e4 · (sigma_ext_cells·dx_m)² · ratio_abs_ext`
— **quadratic in `sigma_ext_cells`**, not linear in `sigma_abs`. This
matters: it is not simply "the fractional difference in `sigma_abs`."

- `C40, 38.4°, BOX_A`: `sigma_ext=310.17504292`, `ratio_abs_ext=0.51310183`
  → `sigma_ext²·ratio_abs_ext = 49364.79` (my hand computation; matches to
  5 sig figs against the file's own `p_abs_w` after dividing out the shared
  `i_incident·dx²·1e4` constant, which I verified is bit-identical between
  configs by back-solving `p_abs_w/(sigma_ext²·ratio_abs_ext)` for both
  C40 and G40 at 38.4°: `5.9257×10⁻¹⁷` both times — confirms the constant
  really is shared, so all of the config-to-config difference lives in
  `sigma_ext²·ratio_abs_ext`, not in a hidden per-config scale factor).
- `G40, 38.4°, BOX_A`: `sigma_ext=310.25674045`, `ratio_abs_ext=0.51350045`
  → `49429.17`.
- `frac_p_abs(38.4°) = |49429.17−49364.79|/49364.79 = 1.304×10⁻³`,
  **reproducing the filed `1.3041×10⁻³` exactly.**
- `frac_contrast(38.4°) = 1.4370×10⁻³` (from `experiments/083-.../
  results.json::per_theta["38.4"]`, `|delta_scene|/|C40_C|`, independently
  recomputed and matching every other seat's this cycle).
- `ratio_k(38.4°) = 1.3041×10⁻³ / 1.4370×10⁻³ = 0.9075`, **reproducing the
  filed `0.9075117524430284` exactly.**

**No arithmetic defect. The surprise is real, not a bookkeeping error.**
One genuinely new observation from doing this by hand rather than trusting
the summary: because `p_abs_w ∝ sigma_ext²`, any few-tenths-of-a-percent
difference in the *raw FDTD* `sigma_ext` between the C40/G40 geometries
gets **doubled** in its fractional effect on `p_abs_w`, and `frac_p_abs`
is itself already a small (~0.1–0.6%) difference-of-differences quantity.
This is a real amplification mechanism worth flagging (§4) even though I
find no evidence below that it is what actually happened at 38.4°.

## 2. Is the dip-then-rise optically coherent, or does it smell like an artifact?

**My answer: it is optically coherent — more coherent, in fact, than the
cycle's own Q4 model — for a reason the record never states.**

`frac_p_abs(θ) = |p_abs_w(G40,θ) − p_abs_w(C40,θ)| / p_abs_w(C40,θ)` is a
**G40-minus-C40 differential channel**. Checking `experiments/083-.../
run.py` directly (line 120): `delta_scene(θ) = C(G40;θ,article) −
C(C40;θ,article)` — the *exact same config pair*, C40 vs. G40, the pair
exp-076 built specifically to decorrelate the PAD effect from ABSORB depth.
`delta_scene`, on this identical pair, is the channel T28 has already
established — Iteration 46 onward, `p<5×10⁻⁵`/`p=0.0`-null-controlled twice
over (exp-069, exp-083) — carries a genuine, resolution-robust, settled
periodic oscillation at `P*≈2.84–2.95°`, "neither an unsettled transient
nor a crude grid artifact" (T28's own LIVE THREAD text). `frac_p_abs` and
`frac_contrast` are therefore not an independent numerator and a
separately-oscillatory denominator, as R13's framing (and this cycle's own
§4) implicitly treats them — **they are two different physical
observables (absorbed power vs. ambient Weber contrast) measured on the
identical PAD-differencing pair**, both plausibly inheriting the same
underlying interference structure between the two geometries' extra
reflection path. Given that, assuming `frac_p_abs` is smooth/near-linear
across a 5.8° span — while its sibling differential on the *same pair* is
confirmed **not** smooth over that same span, at almost exactly that
period (5.8°/2.9°≈2.0 periods) — is the assumption that should have been
flagged as fragile, not the result that broke it. PHOTONICS' own Phase-2
critique this cycle came close ("no argument is offered for why
`frac_p_abs`... should be smooth here... Iteration 53's finding... is
never invoked") but stopped short of the concrete mechanism above: it isn't
merely "no argument was given," it's that the *literal same config pair*
already falsifies the smoothness prior on its sibling channel.

**Against the artifact reading, checked directly (not argued):**
`box_dev` at `(C40,38.4°)`=4.96×10⁻⁵ and `(G40,38.4°)`=1.61×10⁻⁴ sit
squarely inside the range this exact instrument has produced at *every*
other T28 angle on record (exp-087's own six cells at 36.0°/38.6°/41.8°
range 5.0×10⁻⁵–3.0×10⁻⁴); `xi_ext` at 38.4° (1.1×10⁻⁴–3.9×10⁻⁴) is
unremarkable against the same history and nowhere near `XI_TOL=0.12`.
Nothing in the box-independence or extinction-routes-agreement gates
flags 38.4° as numerically unusual — if anything, 38.8° (`box_dev(abs)`
up to 4.7×10⁻⁴) is the noisier of the two new angles by this metric, not
38.4°, the opposite of what a naive "the surprising point must be the
noisy one" prior would predict.

**But this doesn't fully clear Idealization 7, and the omission reads
differently now than it did at Phase 1.** `box_dev` tests box-A-vs-box-B
*independence*, which a shared, not-yet-settled transient would pass
identically in both boxes while still being numerically wrong in absolute
terms — it is necessary, not sufficient, evidence against an
under-settling explanation. exp-087's own STEPS=1400-vs-2800 spot check
(`rel_dev(sigma_abs)=7.9×10⁻⁵`) was run at G40/38.6° only, and this
cycle explicitly declined to add a new one at 38.4°/38.8° (Idealization
7, correctly disclosed, and Red Team's own Phase-2 audit reviewed and
did not elevate it). Given that a genuine, order-unity-relative-magnitude
surprise landed at *exactly one* of the two specifically-unchecked
angles, I read that omission as **less defensible in hindsight than it
was at Phase 2** — not because anything currently on the record points to
a settling defect (nothing does), but because R3's own standing meta-rule
("any surprising feature gets a resolution check before it gets a
mechanism debate") is precisely triggered by this situation, and the one
check this program's own house discipline calls for (an independent
settling spot-check *at the surprising point itself*) has still never
been run. The periodicity explanation in §2 above is the *better-argued*
reading of the two, but it is a physical argument, not a resolution
check, and R3 does not accept an argument in place of the check.

## 3. Does this threaten CONSISTENT, or the Q1/Q5 predictions?

**Numerically: no. Interpretively: it weakens the generality of what
CONSISTENT is entitled to mean, in a way that compounds — not duplicates
— the gap this cycle's own Red Team audit already named.**

- **Q1** is desk-only, computed entirely from already-committed exp-083/
  exp-087 data, and does not depend on this cycle's new FDTD at all — the
  38.4° dip cannot touch it. Unaffected.
- **Q5's label** survives on the numbers: `ratio_k(38.4°)=0.908` clears
  `RATIO_LOW=0.1` by nearly an order of magnitude, so `classify_resolved`
  still returns CONSISTENT over `[2.642, 5.710, 0.908, 3.873]` — this is
  not a close call at the classifier's own boundary.
- **What the dip does threaten** is the implicit story *behind* the
  label — that this channel is "comparable-order-of-magnitude coupled...
  not decoupled" in some stable, general sense near this window. If
  `frac_p_abs` genuinely inherits `delta_scene`'s own ~2.84–2.95° period
  (§2), then `ratio_k`'s apparent stability across these 5 points could be
  a **phase coincidence** — two independently-oscillating curves of
  comparable period sampled at points where they happen not to produce an
  extreme ratio — rather than evidence of a stable coupling constant. A
  denser sweep could in principle show `ratio_k` swinging into "X" or "D"
  territory somewhere the *numerator* peaks or troughs, entirely
  independent of any `delta_scene` zero-crossing — a distinct hazard from
  the one R13 was built to catch (R13 guards only the denominator). This
  sharpens, with a concrete mechanism, the sampling-completeness gap Red
  Team's own audit already flagged in §6.2/Next (only 1 of 4 known
  `delta_scene` near-zero features has ever had `ratio_k` measured near
  it) — my finding says the open risk is not confined to those three
  *denominator*-side nodes; it plausibly extends to wherever the
  *numerator* has its own extrema, which is currently completely
  unmapped (5 points, no period fit possible).

## 4. Anything else optically incoherent?

- The Q4 central-estimate model interpolates linearly across 36.0°→41.8°
  (5.8°, ≈2.0 periods of the *established* oscillation on this exact
  config pair) using only the two endpoints. That a linear fit across
  two periods of a known-periodic signal, anchored on two points, missed
  an interior reading by more than 100% (0.908 vs. predicted floor of
  1.5) is the expected failure mode of that method for this class of
  signal, not evidence of new physics on its own. The ±20% band width was
  set from a single interior check (38.6°, +7.9%) that itself already hinted
  the model was straining — that check should have licensed more caution
  about the model's *functional form*, not just its numeric width.
- `ratio_abs_ext` (T9 anchor cross-check, Q7) stays pinned at
  0.5131–0.5138 across all 4 new cells, matching exp-087's own
  0.5128–0.5138 and T9's 0.51 broadside anchor to <1% — no wavelength/
  angle incoherence there; this is a genuinely reassuring, independent
  confirmation that the absorption physics *underlying* `p_abs_w` (as
  opposed to the differential built on top of it) is behaving exactly as
  established. It is precisely because this underlying ratio is so smooth
  that the differential's own non-monotonicity reads as structural
  (differencing two smoothly-varying-but-not-identically-phased curves),
  not as noise in the underlying absorption physics itself.
- I found no other angle/wavelength incoherence in the record: `xi_ext`,
  vacuum footprint, P1/P2/P4/non-negativity, and the NETD chain (Q6) are
  all clean and unremarkable at both new angles.

## Sharpest finding

`frac_p_abs` and `frac_contrast` are both built by differencing the
*identical* C40/G40 config pair — the one this program specifically
constructed (exp-076) to isolate the PAD effect — and that pair's
ambient-contrast differential (`delta_scene`) is already independently
confirmed, twice, to carry a genuine ~2.84–2.95° period. The cycle's own
Q4 model assumed the absorbed-power differential would be smooth over a
5.8°/≈2-period span without ever testing (or even naming) the far more
parsimonious alternative that it inherits the same periodicity as its
sibling on the same pair; the observed dip-then-rise is exactly the
qualitative shape a sparse, badly-clustered 5-point sample of such a
signal would produce, and is optically *more* consistent with "genuine
T28-family periodicity, not yet resolvable" than with either "denominator
artifact" (ruled out — 38.4°/38.8° both clear the R13 floor with room to
spare) or "new energy-coupling physics localized to 38.4°" (not
supported — nothing in `box_dev`/`xi_ext` singles that angle out, and a
single-point reading can't distinguish a genuine local anomaly from one
sample of an oscillating curve).

## Ranked top-3 for the Iteration-66 queue

1. **A minimal-cost `frac_p_abs(θ)` period check on the C40/G40 pair.**
   Not the full 124-call individual-`σ_abs` build (already correctly
   scoped out this cycle) — a handful of additional established-grid
   points bridging the two large unsampled gaps this cycle's own 5-point
   set leaves (36.0°→38.4° and 38.8°→41.8°; e.g. ~37.2°, ~40.2°) would let
   a period actually be fit against `delta_scene`'s own established
   `P*≈2.84–2.95°`/`P*=2.9474°`, directly testing §2's mechanism rather
   than leaving it as an unadopted disclosure. This is the single most
   diagnostic, cheapest next move: it resolves whether R13's
   denominator-only floor gate is a complete fix or whether `ratio_k`
   needs a symmetric numerator-side check.
2. **The settling spot-check Idealization 7 deferred, run specifically at
   the surprising point.** A STEPS=1400-or-4200-vs-2800 comparison at
   C40/G40, 38.4° (2–4 calls) is the one artifact-class explanation this
   cycle's own instrumentation (box_dev, xi_ext) cannot rule out by
   construction — matching R3's own standing "any surprising feature gets
   a resolution check" meta-rule, which has not yet been discharged here
   despite being directly triggered.
3. **Fold Red Team's already-named forward tripwire (measure `ratio_k` at
   the three other `delta_scene` node-adjacent angles, ≈37.1°/40.2°/41.4°)
   into the same future cycle as item 1**, rather than treating them as
   separate future asks — both target the same underlying open question
   (is this channel's CONSISTENT reading a stable property of the window,
   or a sampling coincidence at wherever it's been measured so far), and
   a single cycle that fits both curves' periods together would settle it
   far more efficiently than two.
