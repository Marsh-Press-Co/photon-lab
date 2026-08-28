# PHASE 2 — CRITIQUE · ELECTROMAGNETISM (blind) · Panel Iteration 61 · exp-084

## Steel-man (≤150 words)

Leg (a) is the first T28 cycle in ten-plus to *reuse* already-hardened bench
machinery — `dg048`'s obliquity-corrected E/H convention (E bare, H
obliquity-weighted per Faraday's law for a driven line current) — rather
than build a fresh reflectance model from scratch. That convention is
exactly the fix this program installed at T21/exp-042 and re-confirmed at
exp-046, so leg (a) inherits four cycles of prior hardening instead of
risking a sixth recurrence. Anchor 1 is a genuine, independent kernel
validation: forcing the discrete exact Green's-function sum into a
deliberately paraxial substitution collapses its residual against the
classical Hecht/Born–Wolf formula from 9.25×10⁻² to 3.29×10⁻³, confirming
the machinery before any T28-specific claim rides on it. Leg (a)'s R5
specificity control (5/60, 8.3%) is a real, tighter check than exp-083's
99.3%-cleared cautionary tale. Most creditable: leg (b) is honestly
WITHHELD, not filed as REFUTE, once its own pre-registered Anchor 2 failed
— R4 discipline working as designed.

## Sharpest attack (≤150 words)

I independently recomputed `c_b_nomask(θ)/c_a(θ)` across all 31 angles (the
file's own convergence check only probed θ=39°). Away from shared
zero-crossings the ratio is NOT a smooth θ-dependent scalar: 2.48→3.15→
2.51→1.47 (36.0°–37.6°), then 5.28→5.66→1.64→2.90 (38.0°–39.0°) — a shape
distortion, not a magnitude rescaling. A genuine missing obliquity/RS
boundary term (a real, smooth cosθ-type correction) would preserve `c_a`'s
own zero-crossings and rescale it smoothly; this doesn't. That's the
signature of a missing complex (phase-carrying) factor — the standard
Huygens–Fresnel `-i/λ` propagator normalization carries a 90° rotation —
consistent with feeding stage-1's bare field `E1` into `propagate()`
*unweighted*, reusing `field_and_h`'s convention validated for a driven
**current**, not a **field** value. That is the exact "obliquity/field-vs-
current convention" bug species VALIDATION.md documents recurring four
times already (line 76); "missing RS boundary term" may just be its fifth
recurrence under a different name. Separately, Idealization 4 ("no
absorbing/lossy medium anywhere") is imprecise: leg (b)'s opaque-strip mask
(`E→0`) IS an idealized perfect absorber (Kirchhoff's classically
non-self-consistent boundary condition) — plausibly the actual root cause.

## Verdict

**Support-with-changes.** Leg (a)'s SUPPORT is well-earned (validated
kernel, disciplined specificity control, honest structural-corollary
disclosure) but should carry one caveat before Iteration 62 treats it as
settled: the fitted `C_model_a(θ)` is visibly a **chirped** oscillation
(local peaks of unequal height at 37.2° and 39.0°, unequal-depth troughs
at 38.2° and 41.4°) rather than a stationary single-frequency signal — an
expected feature of genuine near-field Fresnel diffraction, but a
disciplinary caveat that a single "best-fit sinusoid period" (`P_model_a`)
is itself a lossy summary of a non-stationary curve, not a directly
comparable like-for-like with `P_edge_A`. Leg (b)'s withheld verdict is the
right call and should stay withheld — but its causal diagnosis
("missing Rayleigh–Sommerfeld boundary term") should not be adopted into
LOGBOOK as settled fact without first testing the sharper, cheaper,
convention-bug hypothesis above.

## Parameter change that would flip my verdict

Re-run leg (b)'s stage-2 propagation with the intermediate secondary
sources weighted by the *same* obliquity/phase convention `field_and_h`
uses for a driven current (i.e., test whether multiplying stage-1's `E1`
by an explicit `∂G/∂n`-style factor — obliquity times a 90°-rotating
normalization constant, not a bare field value — closes Anchor 2). If that
closes the gap (converges toward ratio 1.0) **and** it is a genuinely
different fix from a plain real-valued RS boundary term, this becomes a
strong **oppose** on the current diagnosis (the write-up misattributes a
known bug species as a novel physics subtlety). If it does *not* close the
gap, that strengthens the current diagnosis and would move me to full
**support** for leg (a) alone, with leg (b) explicitly retired as
"instrument needs a from-scratch RS treatment, not a patch" rather than
left as an open causal question.
