# Finite real R_y/CZ monitored circuit; explicitly not Haar-random gates.
using LinearAlgebra, Random, Test
LinearAlgebra.BLAS.set_num_threads(1)
function rotate!(v,j,θ)
    bit=1<<(j-1);c=cos(θ/2);s=sin(θ/2)
    for i in 0:length(v)-1
        iszero(i&bit)||continue;a=v[i+1];b=v[(i|bit)+1]
        v[i+1]=c*a-s*b;v[(i|bit)+1]=s*a+c*b
    end
end
function measure!(v,j,rng)
    bit=1<<(j-1);p=sum(abs2(v[i+1]) for i in 0:length(v)-1 if !iszero(i&bit))
    outcome=rand(rng)<p;prob=outcome ? p : 1-p
    for i in 0:length(v)-1
        v[i+1]=(!iszero(i&bit))==outcome ? v[i+1]/sqrt(prob) : 0
    end
end
function monitored(L,p,depth,N,seed)
    angles=2π*rand(MersenneTwister(seed),L,depth);rng=MersenneTwister(seed+7919)
    means=zeros(depth+1);a=2^(L÷2)
    for _ in 1:N
        v=zeros(2^L);v[1]=1
        for t in 1:depth
            for j in 1:L;rotate!(v,j,angles[j,t]);end
            for j in (isodd(t) ? 1 : 2):2:L-1
                for i in 0:length(v)-1
                    if !iszero(i&(1<<(j-1))) && !iszero(i&(1<<j));v[i+1]*=-1;end
                end
            end
            for j in 1:L;if rand(rng)<p;measure!(v,j,rng);end;end
            @assert abs(norm(v)-1)<1e-11
            M=reshape(v,a,:);purity=sum(abs2,M*M')
            means[t+1]+=-log(clamp(purity,1/a,1))/N
        end
    end
    means
end
@test all(abs.(monitored(4,1.0,12,16,2026)).<1e-12)
@test monitored(4,0.0,12,1,2026)≈monitored(4,0.0,12,16,2026) atol=1e-12
mkpath(joinpath(@__DIR__,"..","data"))
out=joinpath(@__DIR__,"..","data","monitored-circuit.csv")
open(out,"w") do io
    println(io,"p,layer,mean_renyi2")
    for p in (0.0,0.15,0.6,1.0)
        means=monitored(6,p,40,64,2026)
        for t in 0:40;println(io,"$p,$t,$(means[t+1])");end
    end
end
println("Seeded monitored circuit generated; normalization and p=0,1 checks passed.")
