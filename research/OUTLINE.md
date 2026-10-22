# Quantum Many-Body Dynamics and Quantum Information: design and coverage

Literature investigation date: 22 October 2026. This is an expandable research
textbook, organized by questions, not researchers. The evidence ledger in this
directory records source-level checks; bibliographies live in `references/`.

## Intellectual spine

How can reversible quantum evolution produce irreversible local physics? What
information remains accessible, how does it spread, and what prevents its loss?
The book follows a small set of recurring models (Ising, XXZ, random circuits,
disordered spins, driven spins, Lindblad chains) across these questions. Every
chapter reintroduces the specialized tools it needs, develops at least one
substantial calculation, and ends with exercises and a research bridge.

## Detailed architecture

| Part / chapter | Central question and technical development | Working calculation / research connection |
|---|---|---|
| I. 1 States and information | How is local mixedness compatible with global purity? Partial traces, Schmidt decomposition, entropy, mutual information, relative entropy | Two-qubit quench; Page typicality; canonical typicality |
| 2 Models, particles, and symmetries | What information is conserved? Spin/Pauli conventions, Fock spaces, Jordan–Wigner map, symmetry sectors | Derive XX chain fermionization and symmetry block dimensions |
| 3 Unitary dynamics and quenches | Which limits define relaxation? Spectral decomposition, diagonal ensemble, Gaussian evolution, correlation functions | Exact Ising mode quench and return amplitude |
| 4 Locality and light cones | Why does information have a speed? Nested commutators, Lieb–Robinson argument, propagation vs correlation cones | Free-particle Bessel front and interacting bounds |
| 5 Exact computation and evidence | What can small systems establish? Bit bases, exact diagonalization, Krylov propagation, typicality, uncertainty and limits | Reproducible Julia quench with convergence checks |
| II. 6 Equilibration and ETH | Why are individual eigenstates thermal locally? Dephasing, ETH ansatz, thermodynamic equivalence, FDT | Fluctuation estimate; Deutsch/Srednicki/Rigol; 2026 first-order transitions |
| 7 Spectral chaos | What does level repulsion diagnose? Symmetry resolution, RMT, spectral form factor, Thouless and Heisenberg times | Gap ratios; random-matrix comparison; limitations of finite spectra |
| 8 Entanglement growth | How is entanglement produced and transported? Quasiparticles, CFT intuition, Page curve, membrane picture | Interval entropy after a quench; integrable vs chaotic growth |
| 9 Operators and scrambling | How does a local perturbation become inaccessible? Pauli growth, OTOCs, butterfly fronts, decoupling, SYK | Squared-commutator derivation; MSS assumptions and experiment |
| 10 Quantum circuits | Which simplified dynamics preserve the right physics? Haar moments, Clifford/stabilizer formalism, designs, conservation | Purity domain walls; circuit/Hamiltonian distinctions |
| III. 11 Hydrodynamics | How do conservation laws govern late times? Continuity, diffusion, noise, nonlinear fluctuating hydrodynamics | Gaussian Green function and long-time tails |
| 12 Linear response and transport | How is transport measured? Kubo response, susceptibilities, conductivity, Drude weight, Mazur bounds | Diffusion/Einstein relation; boundary versus bulk protocols |
| 13 Integrability and ensembles | What replaces thermal equilibrium? Factorized scattering, Bethe equations, TBA, GGE and quasilocal charges | Free-fermion GGE and XXZ dressing |
| 14 Generalized hydrodynamics | How do infinitely many densities flow? Root densities, dressing, effective velocities, Euler equations | Partitioning protocol and domain-wall profiles |
| 15 Anomalous transport | When does diffusion fail? Ballistic/diffusive/superdiffusive scaling, KPZ, giant quasiparticles, near-integrability | Spin-chain scaling collapse; evidence vs universality claims |
| 16 Exactly tractable circuits | What can exact chaotic dynamics teach us? Dual unitarity, transfer matrices, correlators and entanglement | Reshuffled gates and exact cancellations |
| IV. 17 Disorder and localization | How does interference halt transport? Anderson localization, resonances, interacting l-bits | Locator expansion and logarithmic dephasing |
| 18 MBL transition and stability | Can localization survive rare thermal regions? Avalanche criterion, finite-size drift, dimensions and limits | Bath matrix-element comparison and scaling pitfalls |
| 19 Scars and constraints | How can selected states avoid thermalization? PXP, spectrum-generating structures, fragmentation, dipole conservation | Restricted dynamics and Krylov sectors |
| 20 Floquet dynamics | Can periodic driving avoid heating? Floquet theorem, Magnus/van Vleck expansions, optimal truncation, prethermal bounds | Driven two-level and spin systems; resonances and control |
| 21 Time crystals | What constitutes broken time-translation symmetry? Order parameters, rigidity, MBL vs prethermal stabilization | Period doubling; lifetime and thermodynamic limits; 2026 qutrits |
| V. 22 Open quantum systems | When is a subsystem Markovian? Reduced dynamics, channels, Born–Markov/secular approximations, GKSL | Derive amplitude damping and Liouvillian spectra |
| 23 Quantum trajectories | How does a measurement record change the state? Kraus maps, jumps, diffusive unraveling, ensemble equivalence | Jump simulation and conditioned vs unconditional entropy |
| 24 Dissipative phases | How do baths generate order and transitions? Steady states, detailed balance, gaps, metastability, boundary transport | Driven damped models and finite-size spectral caution |
| 25 Measurement-induced phenomena | Can information survive repeated observation? Monitored circuits, replica mappings, purification, critical scaling | Small-state simulation; percolation's restricted domain |
| 26 Information and error correction | When does dynamics encode a logical qubit? Channels, coherent information, reference diagnostics, codes and recovery | Erasure code; monitored dynamics as encoding; postselection cost |
| VI. 27 Critical quantum dynamics | What becomes universal near a transition in time? Landau–Zener, Kibble–Zurek, Loschmidt zeros, DQPT | Ising defect scaling and nonanalytic return rate |
| 28 Kinetics and field theory | How do quasiparticles and fields relax? Closed-time contour, response/noise, Boltzmann approximation, scaling fixed points | Collision conservation and nonthermal scaling constraints |
| 29 Long-range, gauge, and emergent directions | Which assumptions fail beyond local spin chains? Power-law cones, collective limits, Gauss laws, topology, non-Abelian constraints | Gauge-preserving dynamics, resource scaling, recent preprints |
| 30 Experiments and inference | How are entropies, correlations and phases inferred? Cold atoms, ions, Rydberg arrays, solid-state spins, processors, randomized measurements | SWAP/purity estimator and error budget |
| 31 Tensor networks | Why does entanglement limit simulation? SVD/MPS, TEBD, TDVP, MPO, purification, convergence | Schmidt truncation bound and two-site update |
| 32 Research workshop | How does one reproduce and extend a paper? Claim decomposition, benchmarking, scaling, negative controls, research design | Six complete reproduction project plans and frontier ledger |
| Appendices | Mathematical reference, selected worked exercise solutions, notation, research-paper map, bibliography | Cross-linked definitions and reproducibility guide |

## Cross-cutting standards

- Use natural logarithms, $\hbar=k_B=1$, and $S^a=\sigma^a/2$ unless stated otherwise.
- Separate a theorem under hypotheses, a controlled approximation, a numerical
  observation, an experimental inference, and a conjecture.
- Distinguish $L\to\infty$, $t\to\infty$, high-frequency, weak-coupling, and
  ensemble limits. Finite computation does not settle an asymptotic phase.
- Define specialized language before use. Reintroduce necessary notation in
  each chapter and link to a fuller treatment without making it a prerequisite.
- Research bridges explain motivation, the measured or proved object, method,
  assumptions, limitation, and an achievable first reproduction.
- Exercises include analytic derivations, checks of assumptions, numerical
  experiments, and open-ended research design; selected solutions are worked.
- Computational figures are generated by Julia numerical programs with saved
  CSV outputs; plotting may use Python. Browser demonstrations state their
  model and limitations and have static/PDF counterparts.
- Recent papers are included only when verified from a primary source by the
  investigation date. This is a selected, documented coverage map, not a claim
  of exhaustive indexing of every paper published in 2026.

## Maintenance

New work enters through the evidence ledger, then the paper map, then a chapter
revision with reproducible calculations where possible. Do not silently replace
an unsettled conjecture with a claim of consensus. Record changes in CHANGELOG.
