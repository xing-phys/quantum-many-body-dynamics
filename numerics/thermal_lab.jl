#=
Small exact quantum-dynamics laboratories for chapters 6, 7, and 17–21.
Run: julia numerics/thermal_lab.jl
Only Julia standard libraries are required. This is finite-size pedagogy,
not a replication of thermodynamic transition estimates in cited papers.
=#
using LinearAlgebra, Random, Statistics, DelimitedFiles
include("ManyBodyLab.jl")
using .ManyBodyLab
BLAS.set_num_threads(1)
const ROOT_THERMAL = normpath(joinpath(@__DIR__, ".."))
const OUT_THERMAL = joinpath(ROOT_THERMAL, "data")
mkpath(OUT_THERMAL)
const RNG_THERMAL = MersenneTwister(2026102217)

"Pauli Ising H = J ZZ + hx X + hz[j] Z, open ends; bit 0 has Z=+1."
function thermal_ising(L; J=1.0, hx=1.05, hz=fill(0.5,L))
    H=zeros(Float64,1<<L,1<<L)
    for s in 0:(1<<L)-1
        z=[iszero(s & (1<<(j-1))) ? 1.0 : -1.0 for j in 1:L]
        H[s+1,s+1]=J*sum(z[j]*z[j+1] for j in 1:L-1)+sum(hz.*z)
        for j in 1:L
            H[(s ⊻ (1<<(j-1)))+1,s+1]+=hx
        end
    end
    Hermitian(H)
end

function thermal_ratios(E)
    d=diff(sort(E))
    [min(d[j],d[j+1])/max(d[j],d[j+1]) for j in 1:length(d)-1 if max(d[j],d[j+1])>1e-12]
end

println("ETH quench and diagonal matrix elements")
let
    L=8; hz=fill(0.5,L); hz[1]+=0.173 # remove reflection; no global spin-flip symmetry
    H=thermal_ising(L;hz); F=eigen(H)
    O=[iszero(s & (1<<(L÷2-1))) ? 1.0 : -1.0 for s in 0:(1<<L)-1]
    ψ0=zeros(ComplexF64,1<<L); ψ0[0x5a+1]=1
    c=F.vectors'*ψ0; p=abs2.(c); E0=real(dot(ψ0,H*ψ0))
    On=vec(sum(abs2.(F.vectors).*O;dims=1)); de=dot(p,On)
    inds=sortperm(abs.(F.values.-E0))[1:24]; mc=mean(On[inds])
    weights(β)=begin a=-β.*F.values; a.-=maximum(a); exp.(a)./sum(exp.(a)) end
    lo=-20.0; hi=20.0
    for _ in 1:100
        mid=(lo+hi)/2
        if dot(weights(mid),F.values)>E0; lo=mid; else; hi=mid; end
    end
    β=(lo+hi)/2; can=dot(weights(β),On)
    savecsv(joinpath(OUT_THERMAL,"thermal-eth-diagonal.csv"),["energy_density","observable","initial_weight"],
        [(F.values[j]/L,On[j],p[j]) for j in eachindex(p)])
    rows=[]
    for t in range(0,40;length=401)
        ψ=F.vectors*(exp.(-im*t.*F.values).*c)
        @assert abs(norm(ψ)-1)<1e-12
        @assert abs(real(dot(ψ,H*ψ))-E0)<1e-10
        push!(rows,(t,dot(abs2.(ψ),O),de,mc,can,entropy(ψ,L÷2,L)))
    end
    savecsv(joinpath(OUT_THERMAL,"thermal-eth-quench.csv"),["t","observable","diagonal_ensemble","microcanonical_24_levels","canonical","entropy"],rows)
    savecsv(joinpath(OUT_THERMAL,"thermal-eth-metadata.csv"),["L","J_pauli","hx","hz_bulk","hz_left","E0","beta","microcanonical_levels"],[(L,1,1.05,0.5,0.673,E0,β,24)])
end

println("GOE and Poisson gap-ratio references")
let
    rows=[]; D=160; samples=24
    for sample in 1:samples
        A=randn(RNG_THERMAL,D,D); A=(A+A')/sqrt(2)
        E=eigvals(Symmetric(A)); E=E[D÷5:4D÷5]
        for r in thermal_ratios(E); push!(rows,(1,sample,r)); end
        E=cumsum(randexp(RNG_THERMAL,D))
        for r in thermal_ratios(E); push!(rows,(0,sample,r)); end
    end
    savecsv(joinpath(OUT_THERMAL,"thermal-gap-ratios.csv"),["ensemble_1_GOE_0_Poisson","sample","ratio"],rows)
end

println("Disordered XXZ entanglement versus Anderson reference")
let
    L=8; samples=12; W=8.0
    times=vcat(0.0,exp10.(range(-1,2.5;length=100)))
    allrows=[]
    for sample in 1:samples
        fields=W.*(2rand(RNG_THERMAL,L).-1)
        for Δ in (0.0,1.0)
            H=xxz(L;Δ,fields); F=eigen(H)
            s0=sum(1<<(j-1) for j in 2:2:L)
            ψ0=zeros(ComplexF64,1<<L); ψ0[s0+1]=1
            c=F.vectors'*ψ0
            imb=[sum((isodd(j) ? 1 : -1)*(iszero(s&(1<<(j-1))) ? 1 : -1) for j in 1:L)/L for s in 0:(1<<L)-1]
            for t in times
                ψ=F.vectors*(exp.(-im*t.*F.values).*c)
                @assert abs(norm(ψ)-1)<1e-12
                push!(allrows,(sample,Δ,t,dot(abs2.(ψ),imb),entropy(ψ,L÷2,L)))
            end
        end
    end
    savecsv(joinpath(OUT_THERMAL,"thermal-localization.csv"),["sample","Delta","t","imbalance","entropy"],allrows)
end

println("Constrained PXP revivals")
let
    L=12; basis=[s for s in 0:(1<<L)-1 if iszero(s&(s<<1))]
    index=Dict(s=>i for (i,s) in enumerate(basis)); D=length(basis)
    @assert D==377
    H=zeros(Float64,D,D)
    for (i,s) in enumerate(basis), j in 1:L
        q=s ⊻ (1<<(j-1))
        if haskey(index,q); H[index[q],i]=0.5; end # Omega=1
    end
    @assert norm(H-H')<1e-12
    F=eigen(Symmetric(H)); rows=[]
    for (state,s0) in ((1,sum(1<<(j-1) for j in 1:2:L)),(0,0))
        ψ0=zeros(ComplexF64,D); ψ0[index[s0]]=1; c=F.vectors'*ψ0
        for t in range(0,40;length=401)
            ψ=F.vectors*(exp.(-im*t.*F.values).*c)
            full=zeros(ComplexF64,1<<L); full[basis.+1]=ψ
            push!(rows,(state,t,abs2(dot(ψ0,ψ)),entropy(full,L÷2,L)))
        end
    end
    savecsv(joinpath(OUT_THERMAL,"thermal-pxp.csv"),["state_1_staggered_0_empty","t","return_fidelity","entropy"],rows)
end

println("Floquet effective-Hamiltonian convergence")
let
    L=5; HA=Matrix(thermal_ising(L;hx=0.0)); HB=Matrix(thermal_ising(L;J=0.0,hx=1.05,hz=zeros(L)))
    rows=[]
    for T in exp10.(range(-2,-0.2;length=28))
        UF=exp(-im*T/2*HB)*exp(-im*T/2*HA)
        H0=(HA+HB)/2; H1=H0+im*T/8*(HA*HB-HB*HA)
        @assert norm(H1-H1')<1e-12
        push!(rows,(T,norm(UF-exp(-im*T*H0))/sqrt(1<<L),norm(UF-exp(-im*T*H1))/sqrt(1<<L)))
    end
    @assert 1.95<log(rows[2][2]/rows[1][2])/log(rows[2][1]/rows[1][1])<2.05
    @assert 2.95<log(rows[2][3]/rows[1][3])/log(rows[2][1]/rows[1][1])<3.05
    savecsv(joinpath(OUT_THERMAL,"thermal-floquet-convergence.csv"),["T","error_average","error_first_correction"],rows)
end

println("Finite-chain period-doubling control")
let
    L=8; ε=0.12; θ=π+ε
    fields=2π.*rand(RNG_THERMAL,L).-π
    bonds=0.4 .+0.2rand(RNG_THERMAL,L-1)
    d=zeros(1<<L); zbar=zeros(1<<L)
    for s in 0:(1<<L)-1
        z=[iszero(s&(1<<(j-1))) ? 1.0 : -1.0 for j in 1:L]
        d[s+1]=sum(fields.*z)+sum(bonds[j]*z[j]*z[j+1] for j in 1:L-1)
        zbar[s+1]=mean(z)
    end
    Xsum=Matrix(thermal_ising(L;J=0.0,hx=1.0,hz=zeros(L)))
    Ux=exp(-im*θ/2*Xsum); UF=Ux*Diagonal(exp.(-im.*d))
    @assert norm(UF'*UF-I)<1e-11
    ψ=zeros(ComplexF64,1<<L); ψ[1]=1; rows=[]
    for n in 0:160
        push!(rows,(n,cos(n*θ),dot(abs2.(ψ),zbar),ε))
        ψ=UF*ψ
    end
    savecsv(joinpath(OUT_THERMAL,"thermal-period-doubling.csv"),["period","single_spin","interacting_chain","pulse_error"],rows)
    ζ=exp(2π*im/3); Z=Diagonal([1,ζ,ζ^2]); X=ComplexF64[0 0 1;1 0 0;0 1 0]
    @assert norm(Z*X-ζ*X*Z)<1e-12
end

open(joinpath(OUT_THERMAL,"thermal-lab-metadata.txt"),"w") do io
    println(io,"Julia ",VERSION,"; seed=2026102217; BLAS threads=1")
    println(io,"ETH: L=8, Pauli Ising J=1,hx=1.05,hz=0.5 with left +0.173; initial bit state 0x5a; central Z; microcanonical nearest 24 levels.")
    println(io,"Ratios: GOE dimension160,24 independent samples,central60%; Poisson independent exponential gaps; folded min/max convention.")
    println(io,"Localization: open XXZ L=8,S=sigma/2,J=1,fields iid uniform[-8,8],12 matched disorder realizations per Delta=0,1; staggered initial spin state.")
    println(io,"PXP: open L=12,Omega=1,377 allowed configurations; staggered and empty initial states.")
    println(io,"Floquet: open L=5,HA=ZZ+0.5Z,HB=1.05X; first HA then HB; Frobenius unitary error/sqrt(D).")
    println(io,"Period doubling: one finite L=8 disorder realization; Pauli ZZ bonds iid[0.4,0.6],Z fields iid[-pi,pi],pulse theta=pi+0.12; T=1; all-up initial state.")
    println(io,"All calculations are small-system illustrations; none establishes an asymptotic phase or transition.")
end
println("Thermal laboratories completed; conservation, algebra, and truncation-order checks passed.")
