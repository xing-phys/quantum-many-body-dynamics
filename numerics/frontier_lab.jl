# Exact three-matter-site Z2 gauge example from chapter 29.
# Run: julia numerics/frontier_lab.jl
# Pauli matter/link layout: matter1, link12, matter2, link23, matter3.
using LinearAlgebra
include("ManyBodyLab.jl")
using .ManyBodyLab
BLAS.set_num_threads(1)
const FRONTIER_ROOT=normpath(joinpath(@__DIR__,".."))
const FRONTIER_OUT=joinpath(FRONTIER_ROOT,"data")
mkpath(FRONTIER_OUT)

function frontier_pauli(j,N,kind)
    D=1<<N; A=zeros(Float64,D,D)
    for s in 0:D-1
        if kind==:x
            A[(s ⊻ (1<<(j-1)))+1,s+1]=1
        elseif kind==:z
            A[s+1,s+1]=iszero(s&(1<<(j-1))) ? 1 : -1
        else
            error("kind must be :x or :z")
        end
    end
    A
end

N=5; D=1<<N; Id=Matrix{Float64}(I,D,D)
X=[frontier_pauli(j,N,:x) for j in 1:N]
Z=[frontier_pauli(j,N,:z) for j in 1:N]
G=[X[1]*X[2], X[2]*X[3]*X[4], X[4]*X[5]]
J=0.7; h=0.8; m=0.5; ε=0.15
H=-J*(Z[1]*Z[2]*Z[3]+Z[3]*Z[4]*Z[5])-h*(X[2]+X[4])-m*(X[1]+X[3]+X[5])
P=foldl(*,[(Id+g)/2 for g in G])
penalty=sum((Id-g)/2 for g in G)
@assert norm(P*P-P)<1e-12
@assert round(Int,tr(P))==4
@assert maximum(norm(H*g-g*H) for g in G)<1e-12
string=Z[1]*Z[2]*Z[4]*Z[5]
@assert maximum(norm(string*g-g*string) for g in G)<1e-12
@assert norm(Z[1]*G[1]-G[1]*Z[1])>1
ψ0=fill(ComplexF64(1/sqrt(D)),D) # all positive x, physical
F=eigen(Symmetric(H)); c=F.vectors'*ψ0
rows=[]
for λ in (0.0,4.0,12.0)
    Hbad=H+ε*(Z[1]+Z[3]+Z[5])+λ*penalty
    Fb=eigen(Symmetric(Hbad)); cb=Fb.vectors'*ψ0
    for t in range(0,20;length=301)
        ideal=F.vectors*(exp.(-im*t.*F.values).*c)
        ψ=Fb.vectors*(exp.(-im*t.*Fb.values).*cb)
        @assert norm(P*ideal-ideal)<1e-12
        @assert abs(norm(ψ)-1)<1e-12
        physical=real(dot(ψ,P*ψ))
        defect=real(dot(ψ,penalty*ψ))/3
        conditional=abs2(dot(ideal,P*ψ))/physical
        push!(rows,(λ,t,clamp(1-physical,0,1),defect,conditional,abs2(dot(ideal,ψ))))
    end
end
savecsv(joinpath(FRONTIER_OUT,"thermal-gauge-protection.csv"),
    ["lambda","t","physical_sector_leakage","gauss_defect_density","conditional_target_fidelity","target_fidelity"],rows)
open(joinpath(FRONTIER_OUT,"thermal-gauge-metadata.txt"),"w") do io
    println(io,"Julia ",VERSION,"; 3 matter sites,2 links,5 total qubits,open boundary electric fields +1; Pauli convention.")
    println(io,"J=0.7,h=0.8,m=0.5; gauge-breaking epsilon=0.15 times sum matter Z; penalty lambda sum_j (1-G_j)/2,lambda=0,4,12.")
    println(io,"Initial all-positive x state; physical sector dimension4. Exact dense eigendecomposition; t=0..20 in301 points.")
    println(io,"Projector idempotence, Gauss commutators, string invariance, physical rank, norm and ideal constraint preservation verified.")
    println(io,"Toy finite lattice only; no continuum, thermalization, or asymptotic protection claim.")
end
println("Gauge laboratory complete: physical rank, commutators, strings and conservation checks passed.")
