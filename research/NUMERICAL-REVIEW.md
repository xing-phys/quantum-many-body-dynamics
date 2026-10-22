# Numerical reproducibility and interface review

Reviewed 22 October 2026, while the root agent was rendering/integrating. This
was a **read-only audit of programs, documentation, checked-in CSVs, and plotting
interfaces**. No book build was run and no generated data or figure was changed.
The independently executed transport checks from the earlier authoring phase and
the root agent's reported successful core/MPS/monitored runs are distinct from
this audit. Concurrent edits can make the file locations below move.

## Overall result

No incorrect Hamiltonian factor, current sign, or mismatched plotted observable
was found in the inspected artifacts. The formulas, numerical parameters, and
chapter captions agree for the core quench, PXP, Floquet convergence, free-domain
wall, dual channel, and gauge examples. The scripts have appropriate finite-size
and model limitations in their comments/captions. The principal remaining issues
are completeness of the advertised reproduction commands and precision about
what an assertion establishes.

## Concrete integration fixes

1. **Use the complete Makefile workflow in README and the laboratory.**
   At review time, `README.md:16` and `computational-laboratory.qmd:107` regenerate
   only `run_all.jl`, `thermal_lab.jl`, and the core `plot_figures.py`. They omit
   transport, gauge, MPS compression, monitored-circuit CSVs, and thermal/transport
   figures. The *current* `Makefile` already includes all six executable Julia
   generators, including `frontier_lab.jl`, and all three plotters with pinned
   script metadata. The simplest documentation sequence is:

   ```sh
   make data
   make figures
   make check
   quarto render
   python3 scripts/audit.py --rendered
   ```

   These steps are sequential. Rendering from checked-in outputs remains a
   separate, cheaper workflow. The initial Makefile snapshot omitted the gauge
   generator, but a refreshed `make -n data figures` showed that this has already
   been fixed during integration.

2. **Qualify the period-doubling control.** `thermal_lab.jl:153` uses
   `single_spin=cos(n*theta)`, with no inter-pulse longitudinal field. Its
   interacting comparator includes both random longitudinal fields and random
   ZZ bonds. This is a correct clean pulse-error beating illustration, but it is
   not a matched-disorder comparison isolating interaction stabilization.
   `21-time-crystals.qmd` can retain its plotted data and add that distinction to
   the caption. A stronger future control sets the ZZ bonds to zero while keeping
   the exact same field realization, pulse, initial state, and observation times.

3. **Call the Euler check agreement, not a convergence study.**
   `transport_labs.jl:33` checks interior RMSE below 0.035 at one chain length
   (L=240) and t=12,24,36. It does not assert monotone improvement or perform a
   size/grid refinement. The prose in chapter 14 and stdout should say
   "agreement with the interior Euler profile at the specified times" rather
   than "Euler convergence". This changes the evidence claim, not the sound
   numerical result.

4. **Set the transport BLAS thread count.** `transport_labs.jl:3` imports
   LinearAlgebra but does not call `BLAS.set_num_threads(1)`, unlike the other
   eigensystem scripts. Adding that line makes CPU use and numerical execution
   behavior more predictable. This is a reproducibility/performance improvement;
   it does not repair a failed physical check.

## Small interface improvements

- `scripts/plot_transport.py` assumes `figs/` already exists. The complete
  workflow is safe because the core plotter creates it first and it is tracked
  in this checkout. For a standalone plotter, add
  `(ROOT/'figs').mkdir(exist_ok=True)` as the other plotters do.
- `mps_compression.jl` and `monitored_circuit.jl` assume `data/` exists. The
  ordered Makefile workflow is safe because earlier generators create it. An
  independent standalone entry point should create its output directory.
- Add brief laboratory table entries for the two transport CSVs, gauge CSV, MPS
  CSV, and monitored-circuit CSV. The data are present but the current laboratory
  table documents only the original eight outputs.
- The browser monitored demonstration uses 32 records; the Julia CSV uses 64
  records, L=6, 40 layers, seed 2026. Their PRNGs also differ. They implement the
  same stated R_y/CZ/Born-sampling model class but are not intended to agree
  trajectory by trajectory. Record that distinction alongside the CSV link.
- Core, thermal, and gauge examples write useful provenance records. The
  transport, MPS, and monitored programs currently encode their parameters in
  source but write no corresponding runtime/version metadata file. A small
  extras-provenance record would make the exported CSVs easier to use on their
  own.

## Generator and figure trace

| Program | Inputs/model actually used | Outputs / assertion coverage |
|---|---|---|
| `run_all.jl` + `ManyBodyLab.jl` | Seed 20261022; standard libraries; BLAS one thread | Eight core CSVs plus `data/provenance.txt`; two-qubit entropy, XXZ normalization, total Sz, one-particle hopping, norm/energy, Krylov reference, Trotter error ratio, Gaussian projector/charge, KZ quadrature, damping sampling checks |
| `thermal_lab.jl` | Seed 2026102217; BLAS one thread | ETH, ratio, localization, PXP, Floquet and period-doubling CSVs; normalization/energy for ETH, localization norm, PXP basis/rank and Hermiticity, Floquet asymptotic orders, Floquet unitarity, qutrit clock algebra |
| `transport_labs.jl` | L240, negative hopping g=1, full/empty wall, three times; phased SWAP gamma=.37 | Two CSVs; covariance Hermiticity/diagonal occupancy/charge, interior profile tolerance, current sign, both unitarities, ray-channel eigenmodes |
| `frontier_lab.jl` | Five qubits: three matter, two links; J=.7,h=.8,m=.5,epsilon=.15; penalties 0,4,12 | Gauge CSV plus metadata; projector idempotence/rank4, Gauss commutators, invariant string, noninvariant matter Z, norm and ideal-sector preservation |
| `mps_compression.jl` | Seed 20261022; L8 random complex dense state | Five-rank compression CSV; exact reconstruction, canonical tensors, sequential truncation bound. It is not scalable MPS time evolution. |
| `monitored_circuit.jl` | Seed2026 gates, separate record RNG; real R_y/CZ; L6,depth40,N64,p=0,.15,.6,1 | 164 CSV rows; normalization, p1 product-state entropy, p0 record-independent unitary history. It is not a Haar circuit or a phase-boundary calculation. |

`plot_figures.py` reads the eight core CSVs and produces eight corresponding
plot pairs plus two declared conceptual diagrams. `plot_thermal.py` reads the
thermal CSVs, draws a declared analytic avalanche toy curve, and conditionally
plots the gauge CSV if present. That conditional is convenient for partial
work but can hide a missing gauge reproduction step; the complete workflow
should always generate it. `plot_transport.py` reads the two transport CSVs and
produces their plots plus the original closed-time-contour diagram. Python does
not perform quantum evolution in these plotters.

## Scientific consistency checks

- The core Ising numerical Hamiltonian is
  `-sum XX -1.05 sum Z -.2 sum X`, open L8, initially all Z positive. Its
  `g` and `h` arguments are energies, as the function docstring states; the
  displayed example has J=1, so there is no dimensionless-g mismatch.
- The core free chain has *positive* hopping 1/2, odd sites occupied, and an
  odd-minus-even imbalance. The domain-wall transport chain has *negative*
  hopping -g. These are explicitly different conventions/preparations, each
  correctly stated, not accidentally reused datasets.
- For `C_ij=<c_j^dagger c_i>` and hopping -g, rightward number current is
  `-2g Im C[x,x+1]`. The transport code uses that sign and asserts positive
  central flow. The plot uses bond coordinate x+.5 for the current, versus site
  coordinate x for density.
- PXP matrix elements are Omega/2=.5. Chapter 19 uses the same Rabi-frequency
  convention, so its time label Omega=1 is correct.
- For `UF=exp(-iT HB/2) exp(-iT HA/2)`, the thermal code's
  `H1=(HA+HB)/2 + iT[HA,HB]/8` has the correct BCH sign. The assertions test
  one-period errors proportional to T^2 and T^3.
- Gauge-sector fidelity is divided by physical-sector probability before the
  conditional comparison, matching the chapter-29 caption. It is distinct from
  unconditional fidelity and leakage. Their plotted coexistence is meaningful.
- The low-momentum KZ quadrature and return-rate integral have the correct
  prefactors for the Pauli Ising normalization J=1. Their captions properly avoid
  calling the former a finite-endpoint ramp simulation.
- Monte Carlo damping uses exact exponential waiting times. The shaded band is
  pointwise binomial uncertainty; the sampled survival curve's points are
  correlated in time, so the band is not a simultaneous confidence region.
  The current caption only claims sampling uncertainty, which is appropriate.

## Read-only CSV checks performed

A Python-standard-library audit read all rows of the damping, domain-wall, dual
channel, MPS, monitored, and gauge files and found every value finite.
The domain-wall occupations lie in [0,1] up to roundoff (~4e-17 below zero),
the center flows right, the Z ray mode stays exactly one, and the X ray data
match their stored analytic values. MPS fidelities lie in [0,1], monitored
entropies are nonnegative and below the L6 half-chain maximum, and gauge
probabilities/fidelities lie in [0,1] up to ~3e-15 floating-point error.
No clipping of physical data was needed to pass this inspection.

This review does not independently reproduce the research papers cited by the
chapters. It verifies the pedagogical artifact interface, selected internal
identities, and consistency of finite calculations with their stated purpose.
