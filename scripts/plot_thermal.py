# /// script
# requires-python = ">=3.11"
# dependencies = ["matplotlib==3.10.7", "numpy==2.3.4"]
# ///
"""Render original scientific figures from Julia-generated CSV data."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figs"
OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.size": 10, "axes.spines.top": False,
                     "axes.spines.right": False, "figure.dpi": 150,
                     "savefig.bbox": "tight", "axes.prop_cycle": plt.cycler(color=["#176d9c", "#bd522e", "#398158", "#8661a5"])})
def read(name):
    return np.genfromtxt(ROOT / "data" / name, delimiter=",", names=True)
def save(fig, name):
    fig.tight_layout()
    fig.savefig(OUT / f"{name}.png", dpi=180)
    fig.savefig(OUT / f"{name}.pdf")
    plt.close(fig)

d = read("thermal-eth-quench.csv")
fig, ax = plt.subplots(figsize=(7,3.5))
ax.plot(d["t"], d["observable"], lw=1, label="Exact finite-chain evolution")
for col,label,style,color in [("diagonal_ensemble","Diagonal ensemble","--","#bd522e"),("microcanonical_24_levels","Microcanonical, 24 levels",":","#398158"),("canonical","Canonical","-.","#8661a5")]:
    ax.axhline(d[col][0], label=label, linestyle=style, lw=1.2,color=color)
ax.set(xlabel="Time (J = 1)",ylabel="Central Pauli Z",title="Local equilibration: open tilted-field Ising chain, L = 8")
ax.legend(fontsize=8, ncol=2)
save(fig,"thermal-eth")

d=read("thermal-gap-ratios.csv")
fig, ax=plt.subplots(figsize=(6.5,3.6))
bins=np.linspace(0,1,26)
for code,label in [(0,"Independent levels"),(1,"GOE matrices, D = 160")]:
    v=d["ratio"][d["ensemble_1_GOE_0_Poisson"]==code]
    ax.hist(v,bins=bins,density=True,histtype="step",lw=1.5,label=f"{label}: mean {v.mean():.3f}")
x=np.linspace(0,1,200); ax.plot(x,2/(1+x)**2,"k--",lw=1,label="Poisson: 2 / (1 + r)²")
ax.set(xlabel="Folded adjacent-gap ratio r",ylabel="Probability density",xlim=(0,1),title="Level repulsion suppresses small adjacent-gap ratios")
ax.legend(fontsize=8)
save(fig,"thermal-gap-ratios")

d=read("thermal-localization.csv")
fig, axs=plt.subplots(1,2,figsize=(8,3.5))
for delta,label in [(0,"Anderson reference, Δ = 0"),(1,"Interacting XXZ, Δ = 1")]:
    sub=d[d["Delta"]==delta]; ts=np.unique(sub["t"])
    for ax,col in zip(axs,["imbalance","entropy"]):
        mean=np.array([sub[col][sub["t"]==t].mean() for t in ts])
        sem=np.array([sub[col][sub["t"]==t].std(ddof=1)/np.sqrt(12) for t in ts])
        ax.plot(ts[1:],mean[1:],label=label)
        ax.fill_between(ts[1:],(mean-sem)[1:],(mean+sem)[1:],alpha=.15)
        ax.set_xscale("log"); ax.set_xlabel("Time (J = 1)")
axs[0].set_ylabel("Staggered memory"); axs[1].set_ylabel("Half-chain entropy (nats)")
axs[1].legend(fontsize=8)
fig.suptitle("Disorder W = 8, L = 8, 12 matched disorder samples; shaded ±1 SEM",fontsize=10)
save(fig,"thermal-localization")

d=read("thermal-pxp.csv")
fig,axs=plt.subplots(1,2,figsize=(8,3.3))
for code,label in [(1,"Staggered initial state"),(0,"Empty initial state")]:
    sub=d[d["state_1_staggered_0_empty"]==code]
    axs[0].plot(sub["t"],sub["return_fidelity"],label=label)
    axs[1].plot(sub["t"],sub["entropy"],label=label)
axs[0].set(xlabel="Time (Ω = 1)",ylabel="Return fidelity")
axs[1].set(xlabel="Time (Ω = 1)",ylabel="Half-chain entropy (nats)")
axs[0].legend(fontsize=8)
fig.suptitle("State-dependent dynamics in the constrained PXP chain, open L = 12",fontsize=10)
save(fig,"thermal-pxp")

d=read("thermal-floquet-convergence.csv")
fig,ax=plt.subplots(figsize=(6.5,3.6))
ax.loglog(d["T"],d["error_average"],"o-",ms=3,label="Time average only: error ∝ T²")
ax.loglog(d["T"],d["error_first_correction"],"s-",ms=3,label="First commutator correction: error ∝ T³")
ax.set(xlabel="Drive period T",ylabel="One-period unitary error / √D",title="Controlled short-period convergence, open L = 5")
ax.legend(fontsize=8)
save(fig,"thermal-floquet-convergence")

d=read("thermal-period-doubling.csv")
fig,axs=plt.subplots(1,2,figsize=(8,3.4))
n=d["period"]
axs[0].plot(n[:41],d["interacting_chain"][:41],"o-",ms=3,label="Interacting finite chain")
axs[0].plot(n[:41],d["single_spin"][:41],"--",lw=1,label="Single-spin control")
axs[1].plot(n,(-1.)**n*d["interacting_chain"],label="Interacting finite chain")
axs[1].plot(n,(-1.)**n*d["single_spin"],"--",label="Single-spin control")
axs[0].set(xlabel="Drive periods n",ylabel="Magnetization")
axs[1].set(xlabel="Drive periods n",ylabel="Demodulated magnetization")
axs[1].legend(fontsize=8)
fig.suptitle("Period doubling with pulse error 0.12: one L = 8 realization; no phase inference",fontsize=10)
save(fig,"thermal-period-doubling")

# An explicitly declared avalanche toy model, not data from a quantum chain.
r=np.linspace(0,20,400)
fig,ax=plt.subplots(figsize=(6.5,3.4))
for xi in [0.8, 1/np.log(2), 2.2]:
    loglambda=1.2+r*(np.log(2)-1/xi)
    ax.plot(r,loglambda,label=f"Coupling decay length ξ = {xi:.2f}")
ax.axhline(0,color="black",lw=.8,linestyle="--")
ax.set(xlabel="Absorbed radius r",ylabel="log hybridization parameter",title="Symmetric-growth toy model: log Λ = 1.2 + r (log 2 − 1/ξ)")
ax.legend(fontsize=8)
save(fig,"thermal-avalanche")
gauge_path=ROOT/"data"/"thermal-gauge-protection.csv"
if gauge_path.exists():
    d=read("thermal-gauge-protection.csv")
    fig,axs=plt.subplots(1,2,figsize=(8,3.4))
    for lam in np.unique(d["lambda"]):
        sub=d[d["lambda"]==lam]
        axs[0].plot(sub["t"],sub["physical_sector_leakage"],label=f"Penalty λ = {lam:g}")
        axs[1].plot(sub["t"],sub["conditional_target_fidelity"],label=f"Penalty λ = {lam:g}")
    axs[0].set(xlabel="Time",ylabel="Probability outside physical sector")
    axs[1].set(xlabel="Time",ylabel="Target fidelity after physical projection")
    axs[0].legend(fontsize=8)
    fig.suptitle("Z₂ gauge toy model: three matter sites and two links; deliberate gauge-breaking error",fontsize=10)
    save(fig,"thermal-gauge-protection")
print("Rendered thermal laboratory figures as PNG and PDF.")
