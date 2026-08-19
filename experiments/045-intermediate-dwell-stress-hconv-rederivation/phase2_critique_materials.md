# Phase 2 critique — MATERIALS & METAMATERIALS

## Steel-man (≤150 words)

Block B's re-derivation is legitimate, needed work, and I can confirm its
scope claim independently: `REALIZABILITY_MEMO.md`'s verdict section and
tier table never reference `mass_kg` or `tau_thermal_s` anywhere — only
`D_req` (dynamic range) and operating irradiance govern every
UNOBTANIUM-WITH-PARAMETERS tier. Re-deriving a thermal time constant
cannot move a tier built entirely from a different axis; the proposal's
own claim on this point is correct, not merely asserted. Separately: none
of Block A's 16 host/ratio/regime points represent a realizable cloak
material regardless of what mass_kg turns out to be — Hosts A–D are
exactly the "linearly-pumped FCA (doped Si/Ge)" row Amendment 2 already
rates UNOBTANIUM-WITH-PARAMETERS (1–9 OOM short on D_req). The proposal
never claims otherwise ("T1 escape route: NONE") — this is honest,
correctly-scoped instrument-fidelity work on an article this program
already knows can't cloak anything.

## Sharpest attack (≤150 words)

`density_PMMA=1180 kg/m³` is wrong for what Block A's own grid models,
and its citation doesn't check out. Hosts A–D are linearly-pumped
(photoconductive) FCA in **doped silicon/germanium** (T17's Iteration-14
extension, exp-037/038) — not a photochromic dye in a polymer host. PMMA
is a dye-host material from a *different* row of Amendment 2's table.
Worse: `run.py`'s own citation — "the most commonly cited photochromic-dye
host polymer in this program's own literature surveys (T17/T18,
exp-036/037)" — is unverifiable: `PMMA` appears **nowhere** in this repo
except exp-045's own two files (checked via `grep -rl PMMA`, zero other
hits, including exp-036/037 themselves). Meanwhile exp-037 already
computed and used silicon's real, sourced density (ρ=2330 kg/m³) for this
exact mechanism. Using it instead of PMMA gives mass_si/mass_pmma=1.975×,
so dwell/τ_thermal(fully-corrected) = **64.2×**, outside the proposal's
own committed [100×,160×] band for P-EM45-A6 — its own falsification
condition fires.

## Verdict

**Support-with-changes.**

## Parameter change that would flip to plain support

Replace `density_PMMA=1180 kg/m³` with silicon's own density
(ρ=2330 kg/m³, already sourced and used in exp-037 for this identical
Host A–D mechanism), rename the label from PMMA to silicon, delete the
fabricated T17/T18/exp-036/037 PMMA citation, and revise P-EM45-A6's
predicted band before the run (dwell/τ_thermal lands near 64×, not
100–160×, still comfortably above `N_TRANSIENT_TAU=25` and still more
favorable than the uncorrected 48.4×, so the qualitative "relief" claim
survives — only the specific committed number needs correcting). Water
may stay as a disclosed alternate bound if a reason is given for why a
hydrogel or aqueous-suspended host is on the table; as written it reads
as an arbitrary second guess rather than a bound tied to the modeled
mechanism, same defect as PMMA one level down.
