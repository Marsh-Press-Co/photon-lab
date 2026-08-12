# PANEL.md — the Research Panel protocol

*Adopted 2026-08-12 on Marsh's directive (in-session, redesign branch).
Supplements the AGENTS.md loop while Bonnie is inactive — her lanes and every
retained discipline stand unchanged. Any agent running panel work reads
LOGBOOK.md first, every time. Never re-propose a ruled-out idea.*

## Why this exists

The lab's mandate has always been independent voices arguing until nature
arbitrates. Since exp-004 the iterations have been one agent deep — real
science, no second voice. The panel restores structurally independent
perspectives with the tools we actually have: fresh-context sub-agents,
discipline-bound charters, and a shared logbook as the only memory between
cycles. On the record, honestly: all seven seats run on the same base model.
Fresh contexts, adversarial charters, and blind parallel critique buy real
diversity of failure modes; they do not buy a second Bonnie. The precedent is
AGENTS.md's fresh-context cold-read rule, which replaced human figure reads
the same way — and caught real defects.

## The target phenomenon (Marsh's spec, 2026-08-12)

Reproduce, in simulation, the reported observation this lab was founded on: a
flashlight beam swept across open air appears to STOP where it crosses a
specific volume of space — it does not continue on to illuminate the
background behind that volume. No object is visible there. No bright
reflection or scattering returns to the observer. Beam paths on either side
of that volume travel on normally. On a later sweep, the beam passes through
the same space unimpeded.

Constraints a candidate mechanism must satisfy:

1. **Beam termination, not deflection.** Refraction-based cloaking is ruled
   out — it predicts the background stays illuminated. Our own exp-001
   confirmed this: cloak beam-behind 0.64 (the beam *continues*) vs absorber
   0.017 (the beam *stops*).
2. **No specular return** to the observer's eye.
3. **NOT a black silhouette at rest under ambient light** — only the swept
   beam reveals it. ***The hard one. Do not let it slip.***
4. **Transient/switchable** — a later sweep passes unimpeded.

**The central tension (Live Thread T1):** for any linear, time-invariant
medium, the extinction that terminates the beam (1) darkens the ambient view
of the same volume identically — constraints 1+2+3 are jointly unsatisfiable
in that class at photopic ambient levels. Every proposal states which escape
route it takes — **intensity-gated absorption σ(I)** · **time-switched
absorption σ(x,t)** · **angular selectivity** · **sub-threshold operation**
(scotopic ambient + weak distributed absorption) — or names a new class, with
parameters.

## Latitude rule

Mechanisms outside currently established physics are permitted. Sloppy
speculation is not. Any exotic mechanism must be stated as concrete, variable
simulation parameters — otherwise Red Team rejects it as untestable. Whether
any real material provides those parameters is MATERIALS' burden to bound,
stated as: published / plausible / unobtainium-with-parameters.

## The seven seats

Spawned fresh each cycle. Each speaks only from its own discipline and is not
permitted to defer to the others ("I agree with X" is not a critique).

1. **PHOTONICS** — surface interaction, absorption spectra, angular
   dependence, scattering cross-sections. Owns: is the proposal's optical
   response coherent as stated, across wavelength and angle?
2. **MATERIALS & METAMATERIALS** — sub-wavelength structure; what could
   physically realize the proposed optical behavior. Owns the realizability
   bound (published / plausible / unobtainium-with-parameters).
3. **ELECTROMAGNETISM** — field/wave behavior, impedance matching, energy
   coupling. Owns the reciprocity / passivity / causality bookkeeping —
   formalizes what T1 permits and forbids for each proposal.
4. **THERMODYNAMICS** — where absorbed energy goes. Always asks what
   re-radiates and whether it would be detectable. Owns the per-proposal
   energy sidecar: absorbed power → temperature rise → emission band →
   detectability. *Expressibility contract: the sidecar is a post-run
   analytic calculation, not an FDTD output, and is labeled as such.*
5. **QUANTUM OPTICS** — non-classical absorption, state-dependent or coherent
   interactions. *Expressibility contract: mechanisms enter the bench only as
   effective classical parameters — σ(I), σ(x,t), dispersive ε(ω), gain —
   or Red Team strikes them.*
6. **VISION SCIENCE** — human perceptual limits: contrast thresholds,
   luminance edge detection, spectral sensitivity, adaptation, temporal
   (flicker/motion) sensitivity, saccadic and attentional blindness. Central
   question: what would make a human eye FAIL to register something
   physically present? *Duty: pin numeric thresholds, with sources, BEFORE
   any run that scores against them.*
7. **RED TEAM** — attacks every proposal, speaks last and hardest. Its
   standard is NOT textbook-physics compliance — speculation is permitted.
   It kills: internal inconsistency, unfalsifiable claims, mechanisms that
   cannot be expressed as simulation parameters, and proposals that quietly
   violate a target constraint — **especially #3**. Red Team never leads a
   cycle; it has no proposal of its own to protect.

## Independence mechanics

- One fresh sub-agent per seat per cycle. Input packet: its own charter
  (verbatim from this file), the phenomenon + constraints section, LOGBOOK.md
  in full, and the specific files the Director lists for the cycle. NOT the
  other seats' current-cycle outputs.
- Phase 2 critiques run in parallel, blind to each other. Red Team alone
  receives everything (proposal + all six critiques) and goes last.
- The Director (the shift agent driving the cycle) synthesizes but does not
  vote in Phase 2, and must state which criticisms it accepts and which it
  overrides, and why — in writing, in the iteration entry.

## The loop (one cycle = one numbered experiment)

- **PHASE 1 — PROPOSE.** The lead seat (rotation below) proposes ONE
  material/mechanism change as concrete simulation parameters: mechanism
  narrative (≤300 words); a parameter table (geometry, material law with
  numbers, source spec); the T1 escape route taken; per-metric predicted
  outcomes with falsifiable bands; idealizations.
- **PHASE 2 — CRITIQUE.** Every other seat: one steel-man (≤150 words), one
  sharpest attack (≤150 words), a verdict (support / support-with-changes /
  oppose), and optionally the single parameter change that would flip its
  verdict. Red Team last: numbered attacks, each tagged
  [inconsistency | unfalsifiable | inexpressible | constraint-#N-violation].
- **PHASE 3 — SYNTHESIZE.** Director resolves the debate into ONE testable
  configuration, records accepted/overridden criticisms, and writes the
  experiment's NOTES.md — hypothesis, setup, idealizations, **predictions
  committed to git BEFORE the run** (house discipline, non-negotiable).
- **PHASE 4 — TEST.** Run. House gates apply: box_dev/cross_dev bands, trust
  suite green (new machinery ⇒ new suite stage with at least one absolute
  identity gate BEFORE results are trusted), Evidence Gate on artifacts.
- **PHASE 5 — REVIEW.** All seven seats read the results (fresh contexts
  again). Argue the next change. Output: ranked top-3 candidate directions.
  Director updates LOGBOOK.md (verdict: promising / partial / ruled out —
  with the specific reason if ruled out) and PLAN.md's queue.

**Lead rotation** (Red Team excluded): VISION SCIENCE → PHOTONICS →
MATERIALS → ELECTROMAGNETISM → THERMODYNAMICS → QUANTUM OPTICS → repeat.
(Iteration 1 leads with Vision Science because constraint 3's metric is the
program's missing instrument.)

## Metrics — recorded every run

| Metric | Constraint | Instrument |
|---|---|---|
| Forward transmission / beam termination | 1 | beam-behind box (exp-001 idiom) |
| Backscatter to observer vs camera floor | 2 | `emit.observer_record` (stage 6) |
| Background illumination behind the volume | 1 | downstream flux strips |
| Ambient appearance: Weber contrast, **photopic AND scotopic** | 3 | `lab/ambient.py` (stage 9, to be built) |
| Switch transient at the observer | 4 (+3) | time-domain monitor series (stage 10, when built) |
| Absorbed energy budget + predicted re-radiation | ledger | Joule accounting + THERMO sidecar |
| Wavelength (≥ 450/600/750 nm) and angle dependence | witness realism | sweep protocol |

Both ambient regimes are recorded every run: photopic is the hard design
target; scotopic is the witness-consistency check (the reported scene was a
night flashlight sweep). VISION SCIENCE pins the numeric pass/fail thresholds
per experiment, cited, before the run.

## Checkpoints — continuous mode (Marsh's directive, 2026-08-12)

The program runs essentially continuously in the background. Marsh is
convened ONLY at:

1. A configuration passes ALL constraint metrics (candidate reproduction).
2. A proven boundary: a constraint subset shown jointly unsatisfiable within
   a whole mechanism class, gates clean.
3. A synthesis requires engine physics beyond the validated bench classes
   (major build — other live threads continue meanwhile).
4. Red Team flags program-integrity drift (unfalsifiable claims, a constraint
   quietly dropped — especially #3).
5. Two consecutive iterations with no logbook-advancing result (the lab's
   standing kill-criterion pattern).

On checkpoint: a CHECKPOINT entry in LOGBOOK.md + SESSION_LOG.md, and Marsh
is notified. Unblocked threads keep running. **Checkpoint #0 (one-time,
already agreed):** Iteration 1 halts after Phases 1–2 for Marsh's go-ahead
before the first synthesis, engine code, or run.

## Program stop conditions (Red Team's standard, applied to the program)

- **Success:** one configuration passing every metric threshold, robust
  across the 3-λ sweep and a swept-beam protocol, idealizations stated.
- **The honest alternative product:** a mapped constraint boundary — which
  constraint subsets are jointly satisfiable by which mechanism class, and
  the parameter regime the full set demands (e.g. required σ(I) threshold
  and slope). That is a real finding about the witness statement even if no
  known material provides the parameters.
- Neither outcome is "the lab shipped a cloak." The honest frame binds.

## Venues and collisions

State lives in the repo; any venue executes the loop: the `photonlab-shift`
cloud routine (default runner), Marsh's Windows bench, or a live session. An
interactive session that takes the wheel pauses the routine and re-enables it
when done. Every iteration entry in LOGBOOK.md records its runner.
