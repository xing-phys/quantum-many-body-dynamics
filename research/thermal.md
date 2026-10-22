# Thermalization, spectral chaos, localization, scars, and driven matter

Literature audit: 2026-10-22. This record separates primary results, controlled deductions under stated assumptions, numerical observations, experimental observations at finite size/time, and unresolved asymptotic questions. Dates in citation keys are publication years for published papers and submission years for preprints. Entries without a verified journal reference remain explicitly labeled preprints. The source list is selective, not a claim of exhaustive coverage of all literature through 2026.

## Conceptual spine

The central question is how information encoded in an initially simple state becomes inaccessible to local measurements. Begin with exactly unitary evolution and distinguish conservation of global purity from equilibration of local observables. ETH provides a proposed structure for eigenstate matrix elements; spectral chaos describes correlations between energy levels; neither should silently replace the other. Then investigate mechanisms obstructing or delaying equilibration: integrability, disorder, constrained connectivity, rare nonthermal states, large energy scales, and periodic driving. The same ETH matrix-element estimate that supports a thermal subsystem also controls the avalanche argument against localization. The same high-frequency expansion that creates effective Hamiltonians also explains the limited lifetime of driven phases.

## Chapter 06: Can a pure isolated system thermalize?

1. Operational definitions of equilibration, thermalization, recurrence, and local distinguishability. A Bell-pair example explains how local entropy can increase at fixed global entropy.
2. Expand the initial state in energy eigenstates and derive the diagonal ensemble, retaining degeneracy blocks when needed. Distinguish infinite-time averages from typical finite-time behavior.
3. Derive the temporal-variance formula for nondegenerate gaps. Explain effective dimension and why few occupied eigenstates need not equilibrate.
4. Derive the Gibbs state by counting bath states, expanding the bath entropy, and identifying the finite-heat-capacity correction. State weak-coupling, subextensive-subsystem, and narrow-energy-window conditions.
5. Introduce diagonal and off-diagonal ETH, strong and weak ETH, symmetry sectors, the smooth envelope f(E,omega), entropy normalization, and the restricted meaning of random coefficients. Derive thermal averages from smooth diagonal elements and narrow energy support.
6. Insert the ETH ansatz into a spectral representation of a two-point function; derive detailed balance and the fluctuation-dissipation connection. Explain why higher-point functions require correlations among ETH coefficients.
7. Worked quench in a tilted-field Ising chain: compare time trace, diagonal ensemble, microcanonical result, and canonical result. Plot diagonal matrix elements versus energy and the size dependence of fluctuations.
8. Frontier reading: Serbyn et al. (2026) on first-order transitions. Carefully restrict the discussion to their all-to-all models and branch coexistence; avoid claiming a universal breakdown of local ETH in short-range systems.

Required derivations: diagonal ensemble; temporal variance; Gibbs reduction; ETH-to-thermalization implication; two-point spectral function. Exercises: degeneracies, broad initial energy distributions, symmetry mixing, finite-bath correction, weak versus strong ETH.

## Chapter 07: What does quantum chaos actually diagnose?

1. Explain why exponentially separating classical trajectories is not directly the definition of chaos for a finite-dimensional unitary state vector.
2. Introduce integrable versus nonintegrable level crossings, antiunitary symmetries, and GOE/GUE/GSE. Symmetry resolution precedes all statistics.
3. Derive Poisson nearest-neighbor spacings from independent levels and derive the two-by-two GOE Wigner surmise, explicitly labeling it a surmise rather than the exact large-matrix distribution.
4. Define consecutive-gap ratios and distinguish the unrestricted ratio from min/max ratio. Derive the Poisson mean 2 log(2)-1 and provide numerical GOE/GUE benchmarks with their conventions.
5. Derive the spectral form factor as a Fourier transform of two-level correlations. Explain disconnected versus connected pieces, spectral windows, averaging, dip/ramp/plateau, Thouless time, and Heisenberg time.
6. Explain the distinction between spectral universality and locality-sensitive dynamics; a Haar-random matrix has no spatial geometry. Connect the many-body Thouless time to slow modes and finite-size limits.
7. Research laboratories: kicked Ising Floquet spectra and the Kos–Ljubotina–Prosen derivation; Chan–De Luca–Chalker spatially extended circuits. Cross-reference operator spreading rather than conflating it with level repulsion.

Required derivations: Wigner surmise, Poisson gap ratio, form-factor identity. Numerics: symmetry-resolved small spin chains and GOE reference with fixed seed; quantify error under disorder/window averages. Exercises: unresolved parity falsely produces Poisson-like statistics, real Hamiltonian versus physical time reversal, finite spectral-window effects.

## Chapter 17: Can disorder retain quantum memory?

1. Derive the one-dimensional single-particle transfer matrix; contrast localization of orbitals with localization of many-body eigenstates.
2. Explain the enormous many-body density of states and why ordinary nondegenerate perturbation theory cannot establish stability uniformly in system size.
3. Introduce local integrals of motion as an effective description under a quasi-local diagonalizing-unitary assumption. Derive the interacting l-bit Hamiltonian and identify nonuniqueness of the l-bit basis.
4. Work through two interacting l-bits initially in x-polarized states, obtaining a closed-form reduced density matrix and purity. Extend the dephasing argument to exponential interactions and derive logarithmic entanglement growth with a convention-dependent decay length.
5. Contrast absence of particle transport, local memory, nonzero ac response, entanglement spreading, and spin echo. Anderson localization does not produce the same interaction-induced entanglement growth.
6. Relate resonant configurations and rare thermal regions to low-frequency conductivity; specify the phenomenological nature of continuously varying exponents.
7. Examine charge-density-wave experiments in quasiperiodic optical lattices. Persistent imbalance at accessible times is an observed finite-time regime; it does not by itself establish an infinite-time phase. Quasiperiodicity has different rare-region structure from independent random disorder.
8. State Imbrie's theorem with its one-dimensional model and level-statistics assumption. Do not imply a proof for the standard random-field Heisenberg model in all dimensions.

Numerics: clean versus random XXZ quench, noninteracting comparison, imbalance and half-chain entropy, multiple system sizes/disorder samples; label all outputs finite-size demonstrations.

## Chapter 18: Are localized phases stable to thermal avalanches?

1. Explain rare-region probabilities and the distinction between a finite-size/time MBL regime and a thermodynamic MBL phase.
2. Derive a thermal-inclusion hybridization estimate: a bath of Hilbert dimension D has level spacing W/D, while ETH matrix elements of a normalized local bath operator scale as D^(-1/2). Hybridization parameter is proportional to (g/W) sqrt(D).
3. Grow the inclusion into a localized environment with g(r) proportional to exp(-r/xi), derive the competition between spatial exponential suppression and entropy gain, and show why the numerical threshold depends on how xi and the absorbed volume are defined.
4. Explain why surface-to-volume geometry changes the avalanche argument in d>1. State its ETH and resonant-absorption assumptions, and distinguish it from a theorem covering every disordered Hamiltonian.
5. Introduce phenomenological real-space RG via alternating thermal and insulating blocks; explain historical Griffiths and infinite-randomness proposals and later avalanche refinements. Avoid presenting every historical exponent as settled.
6. Analyze exact-diagonalization drift: crossing motion, averaging choice, rare-tail undersampling, gap statistics versus dynamics, bath-coupled chains versus isolated inclusions, and order of limits.
7. Read Morningstar et al. with an explicit distinction between measured bath-induced relaxation rates and the extrapolation to the asymptotic transition.
8. Recent experiment: Li et al. (2025) reports faster imbalance decay with increasing size on 21/42/70-qubit two-dimensional simulators, consistent with delocalization/avalanche expectations, not a proof that all possible two-dimensional localization is impossible.

Exercises: critical seed size, rare-seed spacing, bath bandwidth, two definitions of localization length, insufficient finite-size collapse. Research project: compare fixed-bath and growing-bath estimates on the same toy model.

## Chapter 19: How can special states evade typical dynamics?

1. Distinguish ordinary symmetry sectors, integrability, Hilbert-space fragmentation, exact embedded eigenstates, and atypical scar towers.
2. Derive Rydberg blockade from large nearest-neighbor interaction and obtain the PXP Hamiltonian. Count allowed bit strings through the Fibonacci recurrence.
3. Construct the forward-scattering subspace from the staggered product state. Compare its tridiagonal matrix to an SU(2) spin ladder, derive the ideal revival period, and quantify the leakage/error.
4. Explain approximate versus exact scars and why long-lived oscillations alone are insufficient evidence for a protected thermodynamic phase.
5. Demonstrate the Shiraishi–Mori embedding algebra, stating sector conventions and connecting to the published comment/reply if discussing ETH terminology.
6. Explain graph connectivity, Krylov subspaces, dipole conservation, and fragmentation; derive the continuity constraints behind inhibited dynamics. Ordinary conserved charges are not sufficient to imply fragmentation.
7. Research: variational TDVP maps weakly entangled states to nonlinear classical dynamics. Derive the tangent-space projection and explain variational leakage before making a periodic-orbit analogy.
8. 2026 frontier: graph-theoretic candidate states in frustrated Rydberg arrays; periodic scarred trajectories in integrable XYZ/XXZ chains expressed through Bethe quantum numbers. The latter challenges simplistic definitions equating scars with nonintegrability, so state the operational definition used.

Numerics: PXP state-dependent revivals, eigenstate entropy/overlap outliers, forward-scattering leakage, and comparison with generic product states. Exercises: constrained basis dimension, exact ladder commutators, graph components, variational error bound.

## Chapter 20: What can periodic driving engineer before it heats?

1. Define U(t+T,t), quasienergies modulo 2 pi/T, Floquet modes, micromotion, and the dependence of a stroboscopic Hamiltonian on time origin and logarithm branch.
2. Derive the Magnus expansion through the first commutator term. Use a two-step drive to derive the BCH correction with consistent unitary ordering and sign.
3. Work a rotating-frame tunneling example and obtain a Bessel-function-renormalized hopping; distinguish a large-amplitude rotating-frame expansion from naïve time averaging.
4. Explain locality-based high-frequency heating bounds, factorial growth of nested commutators, optimal truncation n* proportional to omega/J, and exponentially long prethermal times. Give hypotheses: bounded local Hilbert spaces/local energy scales and suitable interaction decay; bosonic unbounded spectra require separate control.
5. Connect approximate energy conservation to a prethermal Gibbs ensemble and distinguish this from near-integrable generalized ensembles.
6. Explain resonances, slow heating, Floquet ETH, and the infinite-temperature endpoint within exact symmetry sectors where generic heating applies. Integrable, localized, or specially constrained drives are exceptions.
7. Introduce anomalous Floquet edge motion and explain why U(T) or an effective static band Hamiltonian alone can miss topology of micromotion; coordinate detailed classification with the topology chapter.
8. Recent sources: multi-tone control suppressing parametric instabilities in driven bosonic lattices (2026) and emergent hierarchical symmetries protecting gauge-theory simulations (2026). State experimental versus model-specific numerical evidence.

Numerics: exact two-step spin-chain evolution, energy plateau, leading effective Hamiltonians, frequency dependence at several L. Exercises: time-origin transformation, branch ambiguity, optimal truncation estimate, resonance of one unbounded oscillator.

## Chapter 21: What makes a time crystal a phase?

1. Define spontaneous symmetry breaking and order of thermodynamic/long-time limits before applying them to discrete time translation.
2. Derive a perfect pi-pulse spin echo and show why exact single-spin period doubling alone does not establish a phase.
3. For U_F = X exp(-i D T) with X^2=1 and [D,X]=0, derive the order-parameter sign flip and quasienergy pairing. Explain the role of many-body order in stabilizing imperfect pulses.
4. Contrast eigenstate-ordered localized time crystals with energy-density-dependent prethermal crystals. State the lifetime, dimensionality, interaction-range, and equilibrium-order requirements of each mechanism.
5. Explain diagnostics: rigidity to pulse errors, initial-state dependence, spatial correlations, lifetime scaling, and controls against slow relaxation or externally imposed subharmonics.
6. Experiments: NV/dipolar and trapped-ion observations; prethermal trapped-ion realization; superconducting-processor eigenstate-order protocol. Discuss finite coherence and mitigation/time-reversal controls.
7. 2026 qutrit frontier: derive clock and shift operators Z and X with ZX = exp(2 pi i/3) XZ, then relate chiral domain-wall energetics to robust period tripling in a chain of 15 qutrits. Explicitly label the source a preprint and the observed size/time limits.

Exercises: no-interaction pi-pulse control, quasienergy pairing, Z3 algebra, finite-temperature ordering in short-range 1D, noise-limited lifetime versus intrinsic heating.

## Primary-source coverage map

| Key | Primary source and verified link | Role and status |
|---|---|---|
| deutsch1991statistical | J. M. Deutsch, *Quantum statistical mechanics in a closed system* (1991), [DOI](https://doi.org/10.1103/PhysRevA.43.2046) | ETH precursor; random-matrix perturbation argument, not universal proof for every local Hamiltonian. |
| srednicki1994chaos | Mark Srednicki, *Chaos and Quantum Thermalization* (1994), [arXiv](https://arxiv.org/abs/cond-mat/9403051) | Eigenstate thermalization from Berry-type assumptions; original primary argument. |
| rigol2008thermalization | Marcos Rigol, Vanja Dunjko, Maxim Olshanii, *Thermalization and its mechanism for generic isolated quantum systems* (2008), [arXiv](https://arxiv.org/abs/0708.1324) | Microscopic numerical demonstration of diagonal-ensemble/ETH mechanism. |
| kaufman2016thermalization | Adam M. Kaufman et al., *Quantum thermalization through entanglement in an isolated many-body system* (2016), [arXiv](https://arxiv.org/abs/1603.04409) | Experiment connecting local thermality, entanglement, and global purity. |
| serbyn2026firstorder | Maksym Serbyn, Alexander Avdoshkin, Oriana K. Diessel, David A. Huse, *Eigenstate thermalization in thermal first-order phase transitions* (2026), [arXiv](https://arxiv.org/abs/2601.08347), [PRX DOI](https://doi.org/10.1103/4zs8-7kf4) | Published PRX 16, 031042. All-to-all models; semiclassics plus exact diagonalization; restricted ETH generalization. |
| oganesyan2007localization | Vadim Oganesyan, David A. Huse, *Localization of interacting fermions at high temperature* (2007), [arXiv](https://arxiv.org/abs/cond-mat/0610854) | Gap-ratio diagnostic and explicit finite-size drift caveat already in the original paper. |
| atas2013ratios | Y. Y. Atas, E. Bogomolny, O. Giraud, G. Roux, *Distribution of the ratio of consecutive level spacings in random matrix ensembles* (2013), [arXiv](https://arxiv.org/abs/1212.5611) | Accurate surmises; do not confuse small-matrix mean with exact large-matrix GOE mean. |
| kos2018chaos | Pavel Kos, Marko Ljubotina, Tomaž Prosen, *Many-Body Quantum Chaos: Analytic Connection to Random Matrix Theory* (2018), [arXiv](https://arxiv.org/abs/1712.02665) | Analytic many-body spectral form factor in kicked models. |
| chan2018spectral | Amos Chan, Andrea De Luca, J. T. Chalker, *Spectral Statistics in Spatially Extended Chaotic Quantum Many-Body Systems* (2018), [arXiv](https://arxiv.org/abs/1803.03841) | Model-dependent many-body Thouless-time scaling and spatial approach to RMT. |
| pal2010transition | Arijeet Pal, David A. Huse, *Many-body localization phase transition* (2010), [arXiv](https://arxiv.org/abs/1010.1992) | Landmark small-system exact diagonalization; early critical interpretation, not settled exponents. |
| serbyn2013entanglement | Maksym Serbyn, Z. Papić, Dmitry A. Abanin, *Universal slow growth of entanglement in interacting strongly disordered systems* (2013), [arXiv](https://arxiv.org/abs/1304.4605) | Dephasing mechanism for logarithmic entanglement conditional on localized description. |
| serbyn2013liom | Maksym Serbyn, Z. Papić, Dmitry A. Abanin, *Local conservation laws and the structure of the many-body localized states* (2013), [arXiv](https://arxiv.org/abs/1305.5554) | Local integrals of motion under stated locality assumptions. |
| huse2014phenomenology | David A. Huse, Rahul Nandkishore, Vadim Oganesyan, *Phenomenology of fully many-body-localized systems* (2014), [arXiv](https://arxiv.org/abs/1408.4297) | Interacting pseudospins, echo, distinct localization lengths. |
| imbrie2016localization | John Z. Imbrie, *On Many-Body Localization for Quantum Spin Chains* (2016), [arXiv](https://arxiv.org/abs/1403.7837) | Mathematical construction in 1D with level-attraction assumption; not unrestricted proof for XXZ. |
| schreiber2015localization | Michael Schreiber et al., *Observation of many-body localization of interacting fermions in a quasirandom optical lattice* (2015), [arXiv](https://arxiv.org/abs/1501.05661) | Finite-time experiment; quasiperiodic potential differs from random disorder. |
| gopalakrishnan2015conductivity | Sarang Gopalakrishnan, Markus Müller, Vedika Khemani, Michael Knap, Eugene Demler, David A. Huse, *Low-frequency conductivity in many-body localized systems* (2015), [arXiv](https://arxiv.org/abs/1502.07712) | Resonant-pair and rare-region phenomenology supported by numerical data. |
| vosk2015transition | Ronen Vosk, David A. Huse, Ehud Altman, *Theory of the many-body localization transition in one-dimensional systems* (2015), [arXiv](https://arxiv.org/abs/1412.3117) | Historical phenomenological RG; subdiffusive Griffiths regime; later avalanche work modifies critical picture. |
| deroeck2017stability | Wojciech De Roeck, François Huveneers, *Stability and instability towards delocalization in MBL systems* (2017), [arXiv](https://arxiv.org/abs/1608.01815) | ETH-based thermal inclusion argument; predicts dimensional/interaction-range instability under its assumptions. |
| thiery2018avalanche | Thimothée Thiery, François Huveneers, Markus Müller, Wojciech De Roeck, *Many-body delocalization as a quantum avalanche* (2018), [arXiv](https://arxiv.org/abs/1706.09338) | Multiscale diagonalization/RG with explicit assumptions. |
| morningstar2022avalanches | Alan Morningstar, Luis Colmenarez, Vedika Khemani, David J. Luitz, David A. Huse, *Avalanches and many-body resonances in many-body localized systems* (2022), [arXiv](https://arxiv.org/abs/2107.05642) | Bath-coupled relaxation and rare resonances; distinguishes MBL regime from phase. |
| li2025delocalization | Tian-Ming Li et al., *Many-body delocalization with a two-dimensional 70-qubit superconducting quantum simulator* (2025), [arXiv](https://arxiv.org/abs/2507.16882) | Experimental preprint: finite-size drift toward delocalization, 21/42/70 qubits. |
| bernien2017simulator | Hannes Bernien et al., *Probing many-body dynamics on a 51-atom quantum simulator* (2017), [arXiv](https://arxiv.org/abs/1707.04344) | Rydberg experiment and state-dependent revivals. |
| turner2018scars | Christopher J. Turner, Alexios A. Michailidis, Dmitry A. Abanin, Maksym Serbyn, Zlatko Papić, *Weak ergodicity breaking from quantum many-body scars* (2018), [arXiv](https://arxiv.org/abs/1711.03528) | Scar interpretation, atypical PXP eigenstates and forward-scattering picture; arXiv title differs. |
| shiraishi2017counterexamples | Naoto Shiraishi, Takashi Mori, *Systematic Construction of Counterexamples to the Eigenstate Thermalization Hypothesis* (2017), [arXiv](https://arxiv.org/abs/1702.08227) | Exact embedded states. Sector conventions prompted [comment](https://arxiv.org/abs/1711.06279) and [reply](https://arxiv.org/abs/1712.01999). |
| choi2019scars | Soonwon Choi et al., *Emergent SU(2) dynamics and perfect quantum many-body scars* (2019), [arXiv](https://arxiv.org/abs/1812.05561) | Deformed PXP revivals and exact toy construction; approximate and exact models must be distinguished. |
| michailidis2020mixedphase | Alexios A. Michailidis et al., *Slow quantum thermalization and many-body revivals from mixed phase space* (2020), [arXiv](https://arxiv.org/abs/1905.08564) | TDVP periodic-orbit interpretation; validate tangent-space leakage. |
| desaules2026frustrated | Jean-Yves Desaules, Aron Kerschbaumer, Marko Ljubotina, Maksym Serbyn, *Systematic construction of quantum many-body scars in frustrated Rydberg arrays* (2026), [arXiv](https://arxiv.org/abs/2605.05297) | Preprint; graph-theoretic candidate states and numerical demonstrations beyond bipartite lattices. |
| petrova2026orbits | Elena Petrova, Maksym Serbyn, Marko Ljubotina, *Periodic orbits and quantum many-body scars in integrable spin chains* (2026), [arXiv](https://arxiv.org/abs/2607.15132) | Preprint; Bethe-ansatz structure of orbit-supporting towers; operational scar terminology matters. |
| bukov2015floquet | Marin Bukov, Luca D'Alessio, Anatoli Polkovnikov, *Universal High-Frequency Behavior of Periodically Driven Systems: From Dynamical Stabilization to Floquet Engineering* (2015), [arXiv](https://arxiv.org/abs/1407.4803) | Authoritative methodological review; primary foundational derivations/examples. |
| abanin2015heating | Dmitry Abanin, Wojciech De Roeck, François Huveneers, *Exponentially slow heating in periodically driven many-body systems* (2015), [arXiv](https://arxiv.org/abs/1507.01474) | Rigorous linear-response heating bound for local bounded systems. |
| kuwahara2016magnus | Tomotaka Kuwahara, Takashi Mori, Keiji Saito, *Floquet-Magnus Theory and Generic Transient Dynamics in Periodically Driven Many-Body Quantum Systems* (2016), [arXiv](https://arxiv.org/abs/1508.05797) | Controlled truncated expansion; full thermodynamic Magnus series need not converge. |
| abanin2017effective | Dmitry A. Abanin, Wojciech De Roeck, Wen Wei Ho, François Huveneers, *Effective Hamiltonians, prethermalization and slow energy absorption in periodically driven many-body systems* (2017), [arXiv](https://arxiv.org/abs/1510.03405) | Quasi-conserved effective Hamiltonian and local dynamical control. |
| cruickshank2026multitone | Robbie Cruickshank, Samuel Lellouch, Marin Bukov, Eugene Demler, Nathan Goldman, Elmar Haller, *Suppressing Parametric Instabilities in Driven Bosonic Lattices through Multi-tone Control* (2026), [arXiv](https://arxiv.org/abs/2606.31667) | Experimental preprint; Cs condensate plus Bogoliubov modeling; no unrestricted bounded-spin theorem for bosons. |
| fu2026hierarchical | Zhanpeng Fu, Wei Zheng, Roderich Moessner, Marin Bukov, Hongzheng Zhao, *Protecting Quantum Simulations of Lattice Gauge Theories through Engineered Emergent Hierarchical Symmetries* (2026), [arXiv](https://arxiv.org/abs/2604.11085) | Preprint; effective theory and numerical quantum-link-model demonstration. |
| khemani2016phases | Vedika Khemani, Achilleas Lazarides, Roderich Moessner, S. L. Sondhi, *Phase Structure of Driven Quantum Systems* (2016), [arXiv](https://arxiv.org/abs/1508.03344) | Floquet eigenstate ordering and dynamical phases in localized models. |
| else2016crystals | Dominic V. Else, Bela Bauer, Chetan Nayak, *Floquet Time Crystals* (2016), [arXiv](https://arxiv.org/abs/1603.08001) | Symmetry-breaking definition and localized construction. |
| yao2017crystals | Norman Y. Yao, Andrew C. Potter, Ionut-Dragos Potirniche, Ashvin Vishwanath, *Discrete Time Crystals: Rigidity, Criticality, and Realizations* (2017), [arXiv](https://arxiv.org/abs/1608.02589) | Rigidity, model phase structure and experimental protocol. |
| else2017prethermal | Dominic V. Else, Bela Bauer, Chetan Nayak, *Prethermal Phases of Matter Protected by Time-Translation Symmetry* (2017), [arXiv](https://arxiv.org/abs/1607.05277) | Long-lived ordered phases protected by emergent symmetry and prethermalization. |
| kyprianidis2021prethermal | Antonis Kyprianidis et al., *Observation of a prethermal discrete time crystal* (2021), [arXiv](https://arxiv.org/abs/2102.01695) | Trapped-ion experiment; lifetime/frequency and initial-energy dependence. |
| mi2022crystal | Xiao Mi et al., *Time-crystalline eigenstate order on a quantum processor* (2022), [arXiv](https://arxiv.org/abs/2107.13571) | Superconducting experiment; generic initial states, reversal controls, finite-size analysis. |
| goss2026qutrit | Noah Goss et al., *A Qutrit Time Crystal Stabilized with Native Chiral Interactions* (2026), [arXiv](https://arxiv.org/abs/2605.14293) | Experimental preprint, 15 qutrits; chirality, domain walls, period tripling. |
| cemin2026graphs | Giovanni Cemin, Marin Bukov, Andrea Solfanelli, *Error correction and quantum information spreading on sparse random graphs* (2026), [arXiv](https://arxiv.org/abs/2610.12597) | Preprint, submitted October 8; Floquet Clifford circuit numerics and graph geometry; transfer to circuits/QEC chapter. |

## Audit cautions that should survive editing

- ETH is not an unrestricted proved theorem for all nonintegrable local Hamiltonians. Random-matrix derivations require assumptions; rare eigenstates, symmetries, coexistence, conservation laws, subsystem fraction, and the observable class matter.
- Diagonal ETH, off-diagonal ETH, level repulsion, thermal transport, scrambling, and Haar-random state design are distinct statements.
- The gap-ratio mean commonly quoted as 0.53590 is the 3x3 GOE surmise. Large GOE matrices approach about 0.5307. State which benchmark is used.
- Local integral-of-motion phenomenology explains the localized regime under a quasi-local diagonalization assumption; it does not by itself settle the existence of an asymptotic phase for every model.
- Avalanche arguments use a bath's ETH matrix elements and a growth rule. Thermal inclusion simulations, open-system relaxation, and isolated thermodynamic dynamics are related but different tests.
- Apparent crossings in L <= 24 exact diagonalization cannot establish a universal transition disorder or exponent without controlling drift and rare tails.
- A long-lived imbalance or subharmonic peak is an experimental observation, not automatically a thermodynamic phase diagnostic.
- Exponentially slow high-frequency heating theorems assume appropriate bounds on local terms. Unbounded bosons and continuum systems require additional care.
- No source posted after 2026-10-22 should be called covered. The seven 2026 sources above were verified directly; publication status must be updated separately from submission date.

## Reproducibility plan

Use Julia standard-library LinearAlgebra, SparseArrays, Random, Statistics, and DelimitedFiles for transparent exact-diagonalization laboratories. Fix seeds, record Hamiltonian conventions (Pauli versus spin operators), symmetry sector, spectral window, system size, disorder distribution, sample count, and computational limits beside each output. Distinguish a small pedagogical reproduction of a mechanism from replication of a published finite-size extrapolation. Provide plotted data as CSV/TSV plus scripts; figures should be generated rather than traced from copyrighted papers.

## Implemented numerical laboratories and added frontier sources

`numerics/thermal_lab.jl` implements the ETH quench and ensemble comparison, symmetry-free GOE/Poisson references, matched-disorder XXZ/Anderson comparison, PXP constrained dynamics, Floquet truncation convergence, and a finite-chain period-doubling control. `numerics/frontier_lab.jl` verifies and propagates a five-qubit Z2 gauge toy model. Both ran successfully on Julia 1.12.6; norms, energy/constraint conservation where applicable, combinatorial rank, algebra identities, and Floquet error orders were checked. Raw data and metadata are in `data/thermal-*`; original PNG/PDF figures are generated with `scripts/plot_thermal.py` using pinned NumPy/Matplotlib dependencies. These demonstrations reproduce mechanisms, not published thermodynamic extrapolations.

Chapter 29 adds primary-source bridges checked on 2026-10-22: [Tran et al., hierarchy of long-range light cones](https://arxiv.org/abs/2001.11509), [Thouless's original pumping paper](https://doi.org/10.1103/PhysRevB.27.6083), [Kitaev's anyon/code construction](https://arxiv.org/abs/quant-ph/9707021), [Casini–Huerta–Rosabal on gauge-region algebras](https://arxiv.org/abs/1312.1183), [Donnelly on non-Abelian gauge entropy](https://arxiv.org/abs/1406.7304), and [Potter–Vasseur on symmetry constraints to conventional MBL](https://arxiv.org/abs/1605.03601). [Chen et al., SU2 local thermalization](https://arxiv.org/abs/2603.23948) now lists JHEP10(2026)137, DOI 10.1007/JHEP10(2026)137, and is discussed with its minimally truncated plaquette-chain model, small-subsystem diagnostics, finite hardware windows, and error-mitigation qualifications.
