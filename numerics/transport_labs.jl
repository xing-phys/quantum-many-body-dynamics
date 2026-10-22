# Independent transport demonstrations, Julia standard library only.
# Run: julia --startup-file=no numerics/transport_labs.jl
using LinearAlgebra
BLAS.set_num_threads(1)
using Printf
const ROOT = normpath(joinpath(@__DIR__, ".."))
mkpath(joinpath(ROOT,"data"))
# Closed free-fermion chain: H=-g sum(c†_x c_{x+1}+h.c.).
# C_ij=<c†_j c_i>, so the rightward current is -2g Im C_{x,x+1}.
L, g = 240, 1.0
h = SymTridiagonal(zeros(L), fill(-g,L-1))
F = eigen(h)
occ = Float64.(collect(1:L) .<= L÷2)
A = F.vectors' * Diagonal(occ) * F.vectors
open(joinpath(ROOT,"data","ghd-domain-wall.csv"),"w") do io
    println(io,"t,x,density,euler_density,rightward_current")
    for t in (12.0,24.0,36.0)
        G = F.vectors * Diagonal(exp.(-im .* F.values .* t))
        C = G*A*G'
        @assert norm(C-C') < 1e-10
        @assert abs(real(tr(C))-L/2) < 1e-9
        @assert minimum(real.(diag(C))) > -1e-10
        @assert maximum(real.(diag(C))) < 1+1e-10
        mse = Float64[]
        for j in 1:L
            x = j-(L+1)/2
            zeta = x/t
            ne = zeta < -2g ? 1.0 : zeta > 2g ? 0.0 : acos(zeta/(2g))/pi
            nj = real(C[j,j])
            jj = j<L ? -2g*imag(C[j,j+1]) : 0.0
            @printf(io,"%.10g,%.10g,%.12g,%.12g,%.12g\n",t,x,nj,ne,jj)
            abs(zeta)<1.7g && push!(mse,(nj-ne)^2)
        end
        @assert sqrt(sum(mse)/length(mse)) < 0.035
        @assert -2g*imag(C[L÷2,L÷2+1]) > 0
    end
end
# Dual-unitary phased SWAP: exact one-site channel and its powers.
d=2; ix(a,b)=a*d+b+1; gamma=0.37
U=zeros(ComplexF64,4,4)
for a in 0:1,b in 0:1
    U[ix(b,a),ix(a,b)]=exp(-im*gamma*(1-2a)*(1-2b))
end
R=similar(U)
for a in 0:1,b in 0:1,c in 0:1,e in 0:1
    R[ix(a,c),ix(b,e)]=U[ix(c,e),ix(a,b)]
end
@assert norm(U'*U-I)<1e-12
@assert norm(R'*R-I)<1e-12
id=Matrix{ComplexF64}(I,2,2)
x=ComplexF64[0 1;1 0]; z=ComplexF64[1 0;0 -1]
function ray_channel(a)
    T=U'*kron(a,id)*U
    M=zeros(ComplexF64,2,2)
    for i in 0:1,j in 0:1,r in 0:1
        M[i+1,j+1]+=T[ix(r,i),ix(r,j)]/2
    end
    M
end
@assert norm(ray_channel(z)-z)<1e-12
@assert norm(ray_channel(x)-cos(2gamma)*x)<1e-12
open(joinpath(ROOT,"data","dual-channel.csv"),"w") do io
    println(io,"edge_gates,x_correlation,z_correlation,x_exact")
    ax,az=copy(x),copy(z)
    for n in 0:20
        cx,cz=real(tr(ax*x))/2,real(tr(az*z))/2
        @assert abs(cx-cos(2gamma)^n)<1e-12
        @printf(io,"%d,%.12g,%.12g,%.12g\n",n,cx,cz,cos(2gamma)^n)
        ax,az=ray_channel(ax),ray_channel(az)
    end
end
println("Transport labs passed: covariance positivity/charge/Euler agreement, dual reshuffling, exact channel eigenmodes.")
