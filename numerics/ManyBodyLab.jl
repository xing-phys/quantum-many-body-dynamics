module ManyBodyLab
using LinearAlgebra, SparseArrays, Random, Statistics, DelimitedFiles
export xxz, ising, entropy, evolve, localgate!, trotter, krylov, savecsv

"Open XXZ chain, S=σ/2; bit j-1 encodes down spin at site j."
function xxz(L; J=1.0, Δ=1.0, fields=zeros(L))
    H = zeros(Float64, 1 << L, 1 << L)
    for s in 0:(1<<L)-1
        z = [iszero(s & (1 << (j-1))) ? 0.5 : -0.5 for j in 1:L]
        H[s+1,s+1] += sum(fields .* z)
        for j in 1:L-1
            H[s+1,s+1] += J*Δ*z[j]*z[j+1]
            if z[j] != z[j+1]
                f = s ⊻ (1 << (j-1)) ⊻ (1 << j)
                H[f+1,s+1] += J/2
            end
        end
    end
    Hermitian(H)
end

"Open Pauli Ising chain H=-J XX-g Z-h X (g,h are energies)."
function ising(L; J=1.0, g=1.05, h=0.2)
    H = zeros(Float64,1<<L,1<<L)
    for s in 0:(1<<L)-1
        for j in 1:L
            H[s+1,s+1] += iszero(s & (1<<(j-1))) ? -g : g
            H[(s ⊻ (1<<(j-1)))+1,s+1] -= h
        end
        for j in 1:L-1
            H[(s ⊻ (1<<(j-1)) ⊻ (1<<j))+1,s+1] -= J
        end
    end
    Hermitian(H)
end

"Entropy across low a bits versus the remaining L-a bits. Natural logarithms."
function entropy(ψ, a, L)
    p = abs2.(svdvals(reshape(ψ,1<<a,1<<(L-a))))
    -sum(x*log(x) for x in p if x>1e-14)
end
evolve(F::Eigen, ψ, t) = F.vectors * (exp.(-im*t .* F.values) .* (F.vectors' * ψ))

"Apply a gate to neighboring sites. Local index is s_j+2s_(j+1)+1."
function localgate!(ψ, G, j, L)
    mask = (1<<(j-1)) | (1<<j)
    for s in 0:(1<<L)-1
        iszero(s & mask) || continue
        inds = [s+1, (s | (1<<(j-1)))+1, (s | (1<<j))+1, (s | mask)+1]
        ψ[inds] = G * ψ[inds]
    end
    ψ
end

"Dense-state second-order even/odd XXZ Trotter reference, not an MPS algorithm."
function trotter(ψ0, L, t, dt; Δ=0.7)
    n = round(Int,t/dt)
    isapprox(n*dt,t; atol=1e-12) || error("t must be multiple of dt")
    ψ=ComplexF64.(ψ0)
    h = Matrix(xxz(2; Δ))
    half = exp(-im*dt/2*h); whole=exp(-im*dt*h)
    for _ in 1:n
        for j in 1:2:L-1; localgate!(ψ,half,j,L); end
        for j in 2:2:L-1; localgate!(ψ,whole,j,L); end
        for j in 1:2:L-1; localgate!(ψ,half,j,L); end
    end
    ψ
end

"Fully reorthogonalized Krylov exponential action, for transparent small tests."
function krylov(H, ψ, t, m)
    Q=zeros(ComplexF64,length(ψ),m); Q[:,1]=ψ/norm(ψ); used=m
    for j in 1:m-1
        v=H*Q[:,j]
        for _ in 1:2, k in 1:j; v -= dot(Q[:,k],v)*Q[:,k]; end
        β=norm(v)
        if β<1e-13; used=j; break; end
        Q[:,j+1]=v/β
    end
    Q=Q[:,1:used]
    K=Hermitian(Q'*H*Q)
    Q*(exp(-im*t*Matrix(K))[:,1])*norm(ψ)
end

function savecsv(path, header, rows)
    open(path,"w") do io
        println(io,join(header,","))
        for row in rows; println(io,join(row,",")); end
    end
end
end
