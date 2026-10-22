using LinearAlgebra, Random, Statistics, Test, Dates
include("ManyBodyLab.jl")
using .ManyBodyLab
LinearAlgebra.BLAS.set_num_threads(1)
const ROOT=normpath(joinpath(@__DIR__,".."))
const OUT=joinpath(ROOT,"data")
mkpath(OUT)
Random.seed!(20261022)

@testset "Exact textbook identities and conventions" begin
    X=ComplexF64[0 1;1 0]; Z=ComplexF64[1 0;0 -1]; I2=Matrix{ComplexF64}(I,2,2)
    v=ComplexF64[1,0,0,0]; t=0.371
    ψ=exp(-im*t*kron(X,X))*v
    p=sin(t)^2
    @test entropy(ψ,1,2) ≈ -p*log(p)-(1-p)*log(1-p) atol=1e-12
    @test Matrix(xxz(2;Δ=0)) ≈ real.((kron(X,X)+kron(ComplexF64[0 -im;im 0],ComplexF64[0 -im;im 0]))/4)
    L=5; H=xxz(L;Δ=0.7)
    Q=Diagonal([sum(iszero(s & (1<<(j-1))) ? 0.5 : -0.5 for j in 1:L) for s in 0:(1<<L)-1])
    @test norm(H*Q-Q*H)<1e-12
    # One-particle block equals hopping J/2, no hidden factor of two.
    inds=[(1<<(j-1))+1 for j in 1:L]
    @test Matrix(xxz(L;Δ=0))[inds,inds] ≈ Matrix(SymTridiagonal(zeros(L),fill(0.5,L-1)))
end

rows=[]
for t in range(0,π;length=301)
    p=sin(t)^2; S=-(p>0 ? p*log(p) : 0)-((1-p)>0 ? (1-p)*log(1-p) : 0)
    push!(rows,(t,p,S,-log(p^2+(1-p)^2)))
end
savecsv(joinpath(OUT,"two-qubit.csv"),["Jt","occupation","entropy","renyi2"],rows)

# Nonintegrable Ising quench: exact finite chain, no thermodynamic inference.
L=8; H=ising(L); F=eigen(H); ψ0=zeros(ComplexF64,1<<L); ψ0[1]=1
z=[sum(iszero(s & (1<<(j-1))) ? 1.0 : -1.0 for j in 1:L)/L for s in 0:(1<<L)-1]
rows=[]; E0=real(dot(ψ0,H*ψ0)); maxnorm=0.0; maxenergy=0.0
for t in range(0,12;length=241)
    ψ=evolve(F,ψ0,t)
    global maxnorm=max(maxnorm,abs(norm(ψ)-1))
    global maxenergy=max(maxenergy,abs(real(dot(ψ,H*ψ))-E0))
    push!(rows,(t,sum(abs2.(ψ).*z),entropy(ψ,L÷2,L)))
end
@test maxnorm<1e-12
@test maxenergy<1e-10
savecsv(joinpath(OUT,"ising-quench.csv"),["t","magnetization","entropy"],rows)

@testset "Krylov and Trotter convergence" begin
    exact=evolve(F,ψ0,0.5)
    @test norm(krylov(H,ψ0,0.5,28)-exact)<1e-10
    Lt=6; Ht=xxz(Lt;Δ=0.7); Ft=eigen(Ht)
    v=zeros(ComplexF64,1<<Lt); v[22]=1
    target=evolve(Ft,v,1.0)
    rows=[]
    for dt in (0.2,0.1,0.05,0.025)
        u=trotter(v,Lt,1.0,dt)
        @test abs(norm(u)-1)<1e-12
        push!(rows,(dt,norm(u-target)))
    end
    @test 3.8 < rows[2][2]/rows[3][2] < 4.2
    savecsv(joinpath(OUT,"trotter-convergence.csv"),["dt","state_error"],rows)
end

# Free fermions: propagate a half-filled alternating Slater determinant.
Lf=80; hf=SymTridiagonal(zeros(Lf),fill(0.5,Lf-1)); ff=eigen(hf)
C0=Diagonal([isodd(j) ? 1.0 : 0.0 for j in 1:Lf]); rows=[]
for t in range(0,20;length=161)
    U=ff.vectors*Diagonal(exp.(-im*t.*ff.values))*ff.vectors'
    C=U*C0*U'; ν=clamp.(eigvals(Hermitian(C[1:Lf÷2,1:Lf÷2])),0,1)
    S=-sum((x>1e-14 ? x*log(x) : 0)+(1-x>1e-14 ? (1-x)*log(1-x) : 0) for x in ν)
    imb=sum((isodd(j) ? 1 : -1)*(2real(C[j,j])-1) for j in 1:Lf)/Lf
    @test abs(real(tr(C))-Lf/2)<1e-10
    @test norm(C*C-C)<1e-10
    push!(rows,(t,imb,S))
end
savecsv(joinpath(OUT,"free-fermions.csv"),["t","imbalance","entropy"],rows)

# Exact diffusion solution on infinite line; validity is the continuum model.
rows=[]
for t in (1.0,4.0,16.0), x in range(-20,20;length=401)
    D=1.0; push!(rows,(t,x,exp(-x*x/(4D*t))/sqrt(4π*D*t)))
end
savecsv(joinpath(OUT,"diffusion.csv"),["t","x","density"],rows)

# Ising Kibble-Zurek: asymptotic Landau-Zener pair probabilities near k=0.
# This is not an ODE simulation of a finite-endpoint ramp.
Nk=40000; ks=((1:Nk).-0.5)*π/Nk; rows=[]
for τ in exp10.(range(0,4;length=65))
    n=sum(exp.(-2π*τ.*ks.^2))/Nk
    asymptotic=1/(2π*sqrt(2τ))
    push!(rows,(τ,n,asymptotic))
end
savecsv(joinpath(OUT,"kibble-zurek.csv"),["tauQ","defect_density","asymptotic"],rows)
@test isapprox(rows[end][2],rows[end][3];rtol=1e-6)

# Ising Loschmidt rate in continuum momentum integration, gi=1.5 -> gf=0.5.
gi=1.5; gf=0.5; ks=((1:12000).-0.5)*π/12000
ri=sqrt.(1 .+gi^2 .-2gi.*cos.(ks)); rf=sqrt.(1 .+gf^2 .-2gf.*cos.(ks))
dotfields=((gi.-cos.(ks)).*(gf.-cos.(ks)).+sin.(ks).^2)./(ri.*rf)
rows=[]
for t in range(0,8;length=801)
    mod2=cos.(2 .*rf.*t).^2 .+dotfields.^2 .*sin.(2 .*rf.*t).^2
    rate=-sum(log.(max.(mod2,1e-30)))/(2length(ks))
    # k>0 modes: sum/L -> (1/2π) integral_0^π.
    push!(rows,(t,rate))
end
savecsv(joinpath(OUT,"loschmidt.csv"),["t","return_rate"],rows)

# Exactly sampled jump time for an undriven excited atom, gamma=1.
Ntraj=10000; waits=-log.(rand(Ntraj)); rows=[]
for t in range(0,6;length=121)
    measured=mean(waits .>t); exact=exp(-t)
    se=sqrt(exact*(1-exact)/Ntraj)
    push!(rows,(t,measured,exact,se))
end
@test maximum(abs(r[2]-r[3]) for r in rows)<0.025
savecsv(joinpath(OUT,"amplitude-damping.csv"),["t","trajectory_average","exact","standard_error"],rows)

open(joinpath(OUT,"provenance.txt"),"w") do io
    println(io,"Generated: ",Dates.now()," (local system clock)")
    println(io,"Julia ",VERSION,"; BLAS threads=1; seed=20261022; standard libraries only.")
    println(io,"Command: julia --startup-file=no numerics/run_all.jl")
    println(io,"Ising: open L=8, Pauli H=-sum XX-1.05 sum Z-0.2 sum X, initial all Z=+1.")
    println(io,"Norm drift=",maxnorm,"; energy drift=",maxenergy)
    println(io,"Free fermions: open L=80, hopping=1/2, odd sites occupied.")
    println(io,"KZ: near-critical Landau-Zener asymptotic formula, J=1, continuum midpoint quadrature.")
    println(io,"Loschmidt: thermodynamic Ising momentum integral, gi=1.5,gf=0.5,J=1.")
    println(io,"Damping: 10000 exact exponential waiting times, undriven excited atom, gamma=1.")
    println(io,"All @test checks passed; finite examples do not establish asymptotic phases.")
end
println("Generated eight datasets; all analytic, conservation, and convergence checks passed.")
