# Successive-SVD MPS construction from a SMALL dense state; no scalable time evolution.
using LinearAlgebra, Random, Test, DelimitedFiles
LinearAlgebra.BLAS.set_num_threads(1)
function dense_to_mps(ψ,L;d=2,χmax=typemax(Int))
    A=Array{ComplexF64,3}[];weights=Float64[]
    R=reshape(ComplexF64.(ψ),1,length(ψ));χleft=1
    for j in 1:L-1
        F=svd(reshape(R,χleft*d,:));keep=min(χmax,length(F.S))
        push!(weights,sum(abs2,F.S[keep+1:end]))
        push!(A,reshape(F.U[:,1:keep],χleft,d,keep))
        R=Diagonal(F.S[1:keep])*F.Vt[1:keep,:];χleft=keep
    end
    push!(A,reshape(R,χleft,d,1));A,weights
end
function mps_to_dense(A)
    M=reshape(A[1],size(A[1],2),size(A[1],3))
    for j in 2:length(A)
        M=reshape(M*reshape(A[j],size(A[j],1),:),size(M,1)*size(A[j],2),size(A[j],3))
    end
    vec(M)
end
Random.seed!(20261022);L=8
ψ=randn(ComplexF64,2^L);ψ/=norm(ψ)
@testset "MPS reconstruction and sequential truncation" begin
    A,w=dense_to_mps(ψ,L)
    @test norm(mps_to_dense(A)-ψ)<1e-12
    @test sum(w)<1e-24
    for T in A[1:end-1]
        M=reshape(T,:,size(T,3));@test norm(M'*M-I)<1e-12
    end
    rows=[]
    for χ in (1,2,4,8,16)
        A,w=dense_to_mps(ψ,L;χmax=χ);v=mps_to_dense(A)
        error=norm(v-ψ);fidelity=abs2(dot(ψ,v))/norm(v)^2
        @test error^2<=sum(w)+1e-12
        push!(rows,(χ,error,fidelity,sum(w)))
    end
    mkpath(joinpath(@__DIR__,"..","data"))
    out=joinpath(@__DIR__,"..","data","mps-compression.csv")
    open(out,"w") do io
        println(io,"chi,state_error,normalized_fidelity,sum_discarded_weights")
        foreach(row->println(io,join(row,",")),rows)
    end
end
println("Small-state MPS construction, canonical gauges, and truncation checks passed.")
