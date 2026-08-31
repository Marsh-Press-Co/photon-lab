# Phase-2 Critique — ELECTROMAGNETISM (blind)

## Steel-man (≤150 words)

The formula the gate reads back and independently recomputes is verified,
by direct read of `lab/fdtd2d.py:172-175`, to be the exact production
closed form (`k=2π/self.lam`; `phase=k·sin(radians(angle_deg))·(yy−yc)+
rel_phase`) — no paraphrase, no drift. The `atol=1e-9` claim checks out
numerically: at the largest tested phase magnitude (~158 rad, R5/41.85°,
arithmetic reproduced independently here), a bit-exact replay of the
identical operation sequence with identical inputs has roundoff many
orders of magnitude below 1e-9, while the smallest plausible defect
signal (FI-B's angle-swap, sin(39.2°)−sin(38.69°)≈0.006 → ~1.4 rad delta
at R4's y-span) sits ~9 orders above it — comfortable margin both
directions, no false-positive/false-negative risk from tolerance choice.
The mandatory FI-A/B/C triad (family, angle, sign) is a real, non-trivial
positive control, correctly scoped to zero FDTD cost, and correctly
separated from run-time dispersion (Idealization 31, citing this seat's
own exp-095 finding accurately).

## Sharpest attack (≤150 words)

The gate is not independent of what it audits. Verified by reading code:
`_run_sim_r4_sigma` constructs `Sim(cells_per_lambda=dg.R4_CPL[600], ...)`
(run.py, R5 analog shown at lines 307-308) and `RANK1A_ANGLES=[39.2,39.4]`
(run.py:263) feeds `add_line_source` — both bare literals. §3's own
"Provenance" column cites these *same* objects (`dg.R4_CPL[600]`,
`RANK1A_ANGLES[0]`) as the gate's "intended" ground truth. So Checks 1/2
compare a value against itself, not against an out-of-band truth — a
wrong literal (typo'd `R4_CPL={600:40}` when 45 was meant; a mis-typed
`RANK1A_ANGLES`) propagates identically into both sides of every
comparison and reads CLEAN. Worse, Check 4 is specified to use the
*already-verified* `sim.lam` (not `cpl_intended`) — so if Check 1 ever
passed on a shared-literal defect, Check 4's "independent" recompute
inherits the same corrupted lam and also passes, contradicting §2a's own
"this check alone is logically sufficient" claim. §5a's CLEAN framing
("removes registration... entirely") overclaims: it can only rule out
call-site plumbing bugs downstream of the job constants, not a defect
baked into the constants/`r{n}_config()` recipe itself — exactly the
"systematic, not random" class Red Team's own exp-095 audit named as
still-live.

## Verdict

**support-with-changes.**

## Flip-to-oppose / flip-to-clean-support change

Add one out-of-band cross-check per representative point: the 8
`(cpl_intended, θ_intended, ...)` tuples get hand-transcribed as literal
constants inside the gate's own module (not imported from `dg.R4_CPL`/
`RANK1A_ANGLES`), with an explicit comment citing this critique as the
reason, so a defect shared between the job-constant source and the
production call site is no longer structurally invisible; and reword §5a
to "removes call-site wiring as a live explanation for the *specific*
angles/families checked" rather than "entirely," matching Idealization 35's
own (correct, but currently disconnected) scope caveat.
