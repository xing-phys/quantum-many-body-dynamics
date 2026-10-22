# /// script
# requires-python = ">=3.11"
# dependencies = ["matplotlib==3.10.7", "numpy==2.3.4"]
# ///
"""Original diagrams and plots of Julia data; no physical simulation in Python."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle
ROOT=Path(__file__).resolve().parents[1]
(ROOT/'figs').mkdir(exist_ok=True)
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False,'savefig.bbox':'tight','font.family':'DejaVu Sans'})
def save(name,fig):
    for suffix in ['png','pdf']:
        fig.savefig(ROOT/'figs'/f'{name}.{suffix}',dpi=180)
    plt.close(fig)
a=np.genfromtxt(ROOT/'data'/'ghd-domain-wall.csv',delimiter=',',names=True)
fig,axs=plt.subplots(1,2,figsize=(8,3.2))
for t in np.unique(a['t']):
    q=a[a['t']==t];z=q['x']/t
    mask=np.abs(z)<2.5
    axs[0].plot(z[mask],q['density'][mask],label=f't={t:g}',lw=1)
    if t==max(a['t']):
        axs[0].plot(z[mask],q['euler_density'][mask],'k--',label='Euler prediction',lw=1.6)
        xb=(q['x']+.5)/t
        axs[1].plot(xb[mask],q['rightward_current'][mask],label='Finite-chain covariance',lw=1)
        z1=np.linspace(-2,2,400)
        axs[1].plot(z1,2/np.pi*np.sqrt(1-z1*z1/4),'k--',label='Euler prediction',lw=1.6)
axs[0].set(xlabel='ray x/t',ylabel='particle density',ylim=(-.03,1.03));axs[1].set(xlabel='bond ray x/t',ylabel='rightward particle current',xlim=(-2.5,2.5))
for ax in axs: ax.legend(fontsize=8);ax.grid(alpha=.15)
fig.suptitle('Free hopping g=1, L=240, initially full left / empty right')
save('ghd-domain-wall',fig)
a=np.genfromtxt(ROOT/'data'/'dual-channel.csv',delimiter=',',names=True)
fig,ax=plt.subplots(figsize=(6,3.2))
ax.plot(a['edge_gates'],a['z_correlation'],'-',label='Z: eigenvalue 1')
ax.plot(a['edge_gates'],a['x_correlation'],'o',ms=4,label='X: channel iteration')
ax.plot(a['edge_gates'],a['x_exact'],'--',label=r'$[\cos(2\gamma)]^n$, $\gamma=0.37$')
ax.set(xlabel='number of edge gates n',ylabel='normalized ray correlation',ylim=(-.03,1.08));ax.legend(fontsize=8);ax.grid(alpha=.15)
save('dual-channel',fig)
# Original conceptual diagram: actual contour has a sewn endpoint and rho0 boundary.
fig,ax=plt.subplots(figsize=(8,2.7));ax.set(xlim=(-.8,8),ylim=(-.8,2.2));ax.axis('off')
ax.add_patch(FancyArrowPatch((.2,1.4),(6.6,1.4),arrowstyle='-|>',mutation_scale=16,lw=2,color='#087f8c'))
ax.add_patch(FancyArrowPatch((6.6,.2),(.2,.2),arrowstyle='-|>',mutation_scale=16,lw=2,color='#a53d55'))
ax.plot([6.6,6.6],[.2,1.4],color='#43586a',lw=1.5)
ax.add_patch(Rectangle((-.15,-.05),.35,1.7,facecolor='#e6edf0',edgecolor='#43586a'))
ax.text(-.5,.8,r'$\rho_0$',ha='center',va='center',fontsize=15)
ax.text(3.2,1.65,r'forward branch: $a_+$, $U$',ha='center',color='#087f8c')
ax.text(3.2,-.15,r'backward branch: $a_-$, $U^\dagger$',ha='center',color='#a53d55')
ax.text(6.85,.8,'trace\nsewing',va='center',fontsize=10)
ax.text(.2,-.6,'initial time',ha='center');ax.text(6.6,-.6,'final time',ha='center')
save('keldysh-contour',fig)
print('Rendered transport results and closed-time contour as PNG/PDF.')
