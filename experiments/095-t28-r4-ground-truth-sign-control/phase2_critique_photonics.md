# Phase 2 critique — PHOTONICS (blind, independent)

Panel Iteration 72, exp-095. Charter: surface interaction, absorption
spectra, angular dependence, scattering cross-sections — is the proposal's
optical response coherent as stated, across wavelength and angle?

## Steel-man (≤150 words)

This is disciplined optical bookkeeping, exactly matched to the phenomenon
it tests. T28's `delta_scene` signal is a coherent interference quantity —
its zero-crossings are a genuine angular feature (an established ~2.84°
period, R13/R14-verified sensitivity near nodes), so the right question
before spending 529 of this cycle's 744 CPU-min on a new `cpl=50` family is
exactly the one Rank 1 asks: does the `R4` family still recover an
already-known SIGN at points with no crossing nearby? I independently
re-derived every cited comparator (39.2°: −1.8292×10⁻³/−2.4921×10⁻³;
39.8°: −1.2131×10⁻³/−9.7931×10⁻⁴, `ratio_k` 0.9197/3.8410, `floor_pass`
True) directly from `experiments/083.../results.json` and
`experiments/092.../results.json` — all bit-exact. The `R5` geometry table
(`round(77×2.5)=192`, `round(185×2.5)=462`) also reproduces exactly under
Python's actual round-half-to-even semantics. A rare, fully-verified table.

## Sharpest attack (≤150 words)

The go/no-go gate treats 39.2° and 39.8° as interchangeable "far-from-null"
evidence, but they are not equally far from an interference node. Using
exp-092's own independently-located lower crossing (θ=40.0718°, `cpl=30`
Rank 1), 39.8° sits only **0.272°** away — ≈9.6% of the established 2.84°
period — while 39.2° sits **0.872°** away (≈31% of a period). This
sub-thread's own record shows node locations migrating by 0.05°–0.27°
between adjacent resolution families (exp-092's own cpl20→cpl30 shift was
0.194°) — the same scale as 39.8°'s entire buffer. A registration-type
defect big enough to plausibly explain the near-null reversal this cycle
exists to check could push 39.8° across zero without indicating anything
about the deeper defect class, while 39.2° would pass regardless of whether
that defect is present at all. The two-point gate is not the redundant
check its own "at both angles" framing implies — one point is doing nearly
all the discriminating work, and it is the weaker-margin one.

## Verdict

**support-with-changes.**

## Parameter change that would flip to full support

State, in §2's go/no-go table, each control angle's distance to the nearest
independently-located crossing (0.272°/0.872°, zero new computation — both
numbers already sit in committed `results.json` files), and replace 39.8°
with a point comparably far from any known crossing as 39.2° is (e.g. 39.0°
or 39.4°, same call count, zero added cost) — so the two-point gate carries
the redundant diagnostic power its framing claims rather than one strong
point and one marginal one.
