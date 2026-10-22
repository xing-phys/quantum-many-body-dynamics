# Transport, integrability, exact circuits, and kinetic theory: evidence ledger

Investigation date: **22 October 2026**. This is selected coverage, not an exhaustive
claim about all papers appearing in 2026. Links below lead to primary papers or
their author-posted preprints. Citation keys refer to `references/transport.bib`.

## Conceptual chapter plan

1. **Hydrodynamics:** derive local continuity from commutators; explain local
   equilibrium and scale separation; obtain diffusion, its Green function,
   fluctuating current, and long-time tails. Separate conserved density spreading
   from information spreading. Introduce nonlinear fluctuating hydrodynamics only
   after its fields and noise have been defined.
2. **Linear response:** interaction-picture derivation of retarded susceptibility;
   spectral representation and detailed balance; conductivity and its singular
   Drude part; Einstein relation; Hilbert-space projection proof of Mazur's bound;
   compare equilibrium, domain-wall, and boundary-reservoir protocols.
3. **Integrability:** distinguish solvability from absence of interactions; derive
   two-body Bethe scattering, periodic quantization, root/hole densities,
   Yang–Yang entropy, TBA, dressing, and free-mode GGE; explain quasilocal charges.
4. **GHD:** explain why a local GGE is the thermodynamic state variable; derive
   collision shifts/effective velocity and conservation-form GHD; solve a
   partitioning protocol; discuss diffusion, forces, entropy, and breakdown.
5. **Anomalous transport:** define dynamical exponents and measurable scaling
   relations; derive KPZ power counting and self-consistent giant-quasiparticle
   estimate; distinguish two-point KPZ scaling from full universality; explain
   weak integrability breaking, finite-time crossovers, and 2026 observations.
6. **Exact circuits:** define reshuffling and dual unitarity, derive cancellation
   identities and light-ray channels; distinguish nonintegrable exact dynamics
   from generic chaos; derive entanglement bounds/saturation and interpret SFF.
7. **Kinetics/field theory:** derive closed-time contour and classical/quantum
   rotation; define response, spectral, and statistical propagators; state the
   approximations leading to Boltzmann kinetics; prove collision invariants and
   entropy production; derive nonthermal scaling constraints and their limits.

## Source checks and coverage map

`A`: original abstract/metadata inspected; `T`: selected full-text sections or
equations inspected; `M`: metadata corroborated but original full text unavailable.
The `T` label does not mean a complete independent verification of all proofs in a paper.

| Key | Primary source and year | Use / status |
|---|---|---|
| bethe1931chain | [Bethe, *Zur Theorie der Metalle. I. Eigenwerte und Eigenfunktionen der linearen Atomkette* (1931)](https://doi.org/10.1007/BF01341708) | Bethe wave functions; publisher title/abstract checked, A |
| kubo1957response | [Kubo, *Statistical-Mechanical Theory of Irreversible Processes. I* (1957)](https://doi.org/10.1143/JPSJ.12.570) | Response/FDT; original publisher blocked, M |
| mazur1969bound | [Mazur, *Non-ergodicity of phase functions in certain systems* (1969)](https://doi.org/10.1016/0031-8914(69)90185-2) | Projection bounds; publisher abstract checked, A |
| yang1969thermodynamics | [C. N. Yang and C. P. Yang, *Thermodynamics of a One-Dimensional System of Bosons with Repulsive Delta-Function Interaction* (1969)](https://doi.org/10.1063/1.1664947) | TBA; metadata corroborated in original later research, M |
| prosen2011drude | [Prosen, *Open XXZ spin chain: Nonequilibrium steady state and strict bound on ballistic transport* (2011)](https://arxiv.org/abs/1103.1350) | Quasilocal charge and rigorous Drude lower bound, A |
| prosen2011ness | [Prosen, *Exact nonequilibrium steady state of a strongly driven open XXZ chain* (2011)](https://doi.org/10.1103/PhysRevLett.107.137201) | Boundary-driven exact MPO; strong drive differs from linear response, A |
| znidaric2011dephasing | [Žnidarič, *Solvable quantum nonequilibrium model exhibiting a phase transition and a matrix product representation* (2011)](https://arxiv.org/abs/1011.0998) | XX + dephasing diffusion; fixed-bond-dimension NESS, A |
| bertini2021transport | [Bertini, Heidrich-Meisner, Karrasch, Prosen, Steinigeweg, Žnidarič, *Finite-temperature transport in one-dimensional quantum lattice models* (2021)](https://arxiv.org/abs/2003.03334) | Authoritative methods/review; selected equations reviewed, T |
| castro2016ghd | [Castro-Alvaredo, Doyon, Yoshimura, *Emergent hydrodynamics in integrable quantum systems out of equilibrium* (2016)](https://arxiv.org/abs/1605.07331) | Independent GHD origin; conservation/effective velocity equations inspected, T |
| bertini2016ghd | [Bertini, Collura, De Nardis, Fagotti, *Transport in Out-of-Equilibrium XXZ Chains: Exact Profiles of Charges and Currents* (2016)](https://arxiv.org/abs/1605.09790) | Independent GHD origin, partitioning and TEBD tests, A |
| denardis2019diffusion | [De Nardis, Bernard, Doyon, *Diffusion in generalized hydrodynamics and quasiparticle scattering* (2019)](https://arxiv.org/abs/1812.00767) | Diffusive correction/form factors; abstract and explanatory sections, T |
| ljubotina2017spin | [Ljubotina, Žnidarič, Prosen, *Spin diffusion from an inhomogeneous quench in an integrable system* (2017)](https://arxiv.org/abs/1702.04210) | Numerics: easy-axis diffusion, isotropic 2/3 exponent; discussion checked, T |
| ljubotina2019kpz | [Ljubotina, Žnidarič, Prosen, *Kardar-Parisi-Zhang physics in the quantum Heisenberg magnet* (2019)](https://arxiv.org/abs/1903.01329) | Two-point KPZ function, mixed-state MPO linear response; body checked, T |
| gopalakrishnan2019kinetic | [Gopalakrishnan and Vasseur, *Kinetic theory of spin diffusion and superdiffusion in XXZ spin chains* (2019)](https://arxiv.org/abs/1812.02701) | Fluctuating quasiparticle kinetic picture, A |
| ilievski2021super | [Ilievski, De Nardis, Gopalakrishnan, Vasseur, Ware, *Superuniversality of superdiffusion* (2021)](https://arxiv.org/abs/2009.08425) | Integrable non-Abelian models, giant quasiparticles; A |
| denardis2021stability | [De Nardis, Gopalakrishnan, Vasseur, Ware, *Stability of superdiffusion in nearly integrable spin chains* (2021)](https://arxiv.org/abs/2102.02219) | Perturbative longevity, not asymptotic proof; A |
| denardis2023nlfh | [De Nardis, Gopalakrishnan, Vasseur, *Non-linear fluctuating hydrodynamics for KPZ scaling in isotropic spin chains* (2023)](https://arxiv.org/abs/2212.03696) | Coupled-mode proposal respects spin-flip symmetry; context and equations checked, T |
| rosenberg2024magnetization | [Rosenberg et al., *Dynamics of magnetization at infinite temperature in a Heisenberg spin chain* (2024)](https://arxiv.org/abs/2306.09333) | 46-qubit full counting statistics; higher moments challenge full KPZ, A |
| takeuchi2025partial | [Takeuchi, Takasan, Busani, Ferrari, Vasseur, De Nardis, *Partial yet definite emergence of the Kardar-Parisi-Zhang class in isotropic spin chains* (2025)](https://arxiv.org/abs/2406.07150) | Extensive two-point numerical tests; partial emergence, A |
| doyon2025perspective | [Doyon, Gopalakrishnan, Møller, Schmiedmayer, Vasseur, *Generalized Hydrodynamics: A Perspective* (2025)](https://arxiv.org/abs/2311.03438) | Scope/extensions/limitations and research map, selected text checked, T |
| nahum2017growth | [Nahum, Ruhman, Vijay, Haah, *Quantum Entanglement Growth under Random Unitary Dynamics* (2017)](https://arxiv.org/abs/1608.06950) | KPZ entropy fluctuations; distinguish from OTOC broadening, A |
| nahum2018operator | [Nahum, Vijay, Haah, *Operator Spreading in Random Unitary Circuits* (2018)](https://arxiv.org/abs/1705.08975) | Exact averaged 1D biased diffusion, A |
| vonkeyserlingk2018operator | [von Keyserlingk, Rakovszky, Pollmann, Sondhi, *Operator hydrodynamics, OTOCs, and entanglement growth in systems without conservation laws* (2018)](https://arxiv.org/abs/1705.08910) | Information front hydrodynamics, A |
| rakovszky2018charge | [Rakovszky, Pollmann, von Keyserlingk, *Diffusive hydrodynamics of out-of-time-ordered correlators with charge conservation* (2018)](https://arxiv.org/abs/1710.09827) | Hydrodynamic tails behind ballistic fronts, A |
| alba2017entanglement | [Alba and Calabrese, *Entanglement and thermodynamics after a quantum quench in integrable systems* (2017)](https://arxiv.org/abs/1608.00614) | Quasiparticle entropy formula and assumptions inspected, T |
| zhou2020membrane | [Zhou and Nahum, *The entanglement membrane in chaotic many-body systems* (2020)](https://arxiv.org/abs/1912.12311) | Line tension and nonrandom extensions; selected body, T |
| bertini2018spectral | [Bertini, Kos, Prosen, *Exact Spectral Form Factor in a Minimal Model of Many-Body Quantum Chaos* (2018)](https://arxiv.org/abs/1805.00931) | Original odd-time proof/even-time conjecture distinction; body checked, T |
| bertini2019dual | [Bertini, Kos, Prosen, *Exact Correlation Functions for Dual-Unitary Lattice Models in 1+1 Dimensions* (2019)](https://arxiv.org/abs/1904.02140) | Exact light-ray channels, A |
| bertini2019entanglement | [Bertini, Kos, Prosen, *Entanglement spreading in a minimal model of maximal many-body quantum chaos* (2019)](https://arxiv.org/abs/1812.05090) | Exact solvable initial states/minimal-cut saturation; selected body, T |
| bertini2026duality | [Bertini, Claeys, Prosen, *Exactly solvable many-body dynamics from space-time duality* (2026)](https://arxiv.org/abs/2505.11489) | Review, RMP 98,025001; original abstract/metadata, A |
| berges2005nonequilibrium | [Berges, *Introduction to Nonequilibrium Quantum Field Theory* (2005)](https://arxiv.org/abs/hep-ph/0409233) | 2PI and controlled approximation context, A |
| sieberer2016keldysh | [Sieberer, Buchhold, Diehl, *Keldysh Field Theory for Driven Open Quantum Systems* (2016)](https://arxiv.org/abs/1512.00637) | Contour and response/noise pedagogy, A |
| schmied2019fixed | [Schmied, Mikheev, Gasenzer, *Non-thermal fixed points: Universal dynamics far from equilibrium* (2019)](https://arxiv.org/abs/1810.08143) | Nonperturbative kinetics, defects, prescaling; A |
| prufer2018universal | [Prüfer et al., *Observation of universal dynamics in a spinor Bose gas far from equilibrium* (2018)](https://arxiv.org/abs/1805.11881) | Spinor-gas experiment; methods and scaling figures inspected, T |
| erne2018universal | [Erne, Bücker, Gasenzer, Berges, Schmiedmayer, *Universal dynamics in an isolated one-dimensional Bose gas far from equilibrium* (2018)](https://arxiv.org/abs/1805.12310) | Scaling window/initial-condition comparisons; selected methods, T |

## Verified 2026 additions

| Key | Source | Result and evidence boundary |
|---|---|---|
| anand2026robustness | [Anand, Kemp, Wei, White, Zaletel, Yao, *Robustness of Kardar-Parisi-Zhang-like transport in long-range interacting quantum spin chains*](https://arxiv.org/abs/2602.15933v2) | v2, 9 April 2026; **preprint**. Tensor-network observation of long-lived z=3/2 and KPZ-compatible two-point functions up to about 10^3/J. Inozemtsev proximity is a **conjectured mechanism**, not a proof of asymptotic nonintegrable KPZ. A |
| santra2026crossover | [Santra, Łebek, Panfil, *Crossover from generalized to conventional hydrodynamics in nearly integrable systems under relaxation time approximation*](https://arxiv.org/abs/2603.02158) | 2 March 2026; **preprint**. Controlled calculations inside a **model relaxation-time collision operator**; not a microscopic derivation of that operator for arbitrary perturbations. A |
| scopa2026bloch | [Scopa, Zechmann, Knap, De Nardis, Bastianello, *Generalized Hydrodynamics of Bloch Oscillations in the Absence of a Lattice*](https://arxiv.org/abs/2605.18957v2) | v2, 14 September 2026; PRL 137,113404. GHD for finite-density impurities in Yang–Gaudin gas, bound-state renormalization of oscillations. A |
| mcculloch2026coherence | [McCulloch, Jacoby, Gopalakrishnan, *Long-lived local quantum coherences from hydrodynamic large deviations*](https://arxiv.org/abs/2604.27074v2) | v2, 14 September 2026; **preprint**. Nonperturbative rare voids protect charge-changing operators. Selected main-text and discussion sections checked, T. Requires suitable zero-entropy charge sectors; neutral ancillary activity can invalidate protection. Deterministic extension uses phenomenological conditioning; random-circuit derivation uses a dilute-coherence approximation with numerical checks. |

## Scientific cautions for manuscript integration

- The 2017 inhomogeneous-quench paper found the exponent but did not identify the
  final KPZ function accurately; the 2019 paper supplied that stronger evidence.
- KPZ entropy fluctuations in 1D noisy circuits, diffusive OTOC-front broadening
  in 1D, and KPZ-like spin transport are different observables/mechanisms.
- SU(2) symmetry alone does not establish asymptotic superdiffusion. Integrability,
  state polarization, perturbation class, time scales, and conservation laws matter.
- The Heisenberg spin structure factor is KPZ-compatible; higher current
  statistics exclude identifying magnetization with a single Burgers density.
- GHD is an emergent scaling theory; Euler order cannot predict all diffusive
  widths, microscopic oscillations, or entanglement for arbitrary initial states.
- Strongly driven NESS currents can have exponents different from linear-response
  equilibrium transport; boundary resistance and finite bias must be controlled.
- Dual unitarity does not imply chaos: SWAP and integrable/nonmixing examples exist.
  The 2018 SFF paper proves its original result for odd times and treats even
  times conjecturally; do not erase that qualification in historical coverage.

## Reproduction demonstrations and exercises

Julia: (i) finite-difference diffusion and analytic Gaussian; (ii) current and
continuity commutators in an XXZ chain; (iii) small-system Kubo spectral sum and
weak-bias evolution; (iv) free-fermion domain-wall covariance matrix compared with
Euler occupation formula; (v) Nyström quadrature and fixed-point TBA/dressing;
(vi) a dual-unitary gate reshuffle plus exact light-cone correlations;
(vii) numerical collapse with deliberate crossover contamination; (viii) a
conserving discretized collision integral and nonthermal scaling analysis.

Figures: microscopic bond current → coarse density → diffusion; quasiparticle
collision displacements; Riemann rays; three distinct spreading speeds; tensor
cancellations in two orientations; Keldysh contour; momentum-space flux cascade.
All proposed figures should be original drawings or regenerated data.

## Completed pedagogical computations and integration audit

- `numerics/transport_labs.jl` executed successfully with Julia 1.12.6 on
  22 October 2026. The L=240 hopping-chain domain wall passed Hermiticity,
  occupation-bound, total-charge, rightward-current-sign, and interior Euler
  profile checks. The phased-SWAP example passed ordinary and reshuffled
  unitarity and the exact X/Z channel-eigenmode trajectory checks.
- `scripts/plot_transport.py` renders those data and an original closed-time
  contour in PNG and PDF; all three PNGs were visually inspected.
- Integrated map cross-checks reopened original arXiv abstract/metadata records
  for Cemin–Bukov–Solfanelli 2610.12597 (8 October 2026, preprint), Chen et al.
  2603.23948v4 (6 September 2026, JHEP10(2026)137), Serbyn et al. 2601.08347
  (PRX16,031042), and Mark et al. 2609.30248 (24 September 2026, review preprint).
  These are abstract/metadata checks, not independent proof or hardware audits.
