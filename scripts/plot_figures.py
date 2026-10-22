# /// script
# requires-python = ">=3.11"
# dependencies = ["matplotlib==3.10.7", "numpy==2.3.4"]
# ///
"""Plot Julia-generated data; no scientific simulation takes place in this file."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
ROOT=Path(__file__).resolve().parents[1]
F=ROOT/'figs'; F.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False,'axes.grid':True,'grid.alpha':.16,'figure.dpi':150,'savefig.bbox':'tight','axes.labelsize':11})
colors=['#087f8c','#a53d55','#df9d28','#4d5792']
plt.rcParams['axes.prop_cycle']=matplotlib.cycler(color=colors)
def load(name): return np.genfromtxt(ROOT/'data'/f'{name}.csv',delimiter=',',names=True)
def save(name, fig):
    fig.savefig(F/f'{name}.png',dpi=180)
    fig.savefig(F/f'{name}.pdf')
    plt.close(fig)
a=load('two-qubit'); fig,ax=plt.subplots(figsize=(7,3.3))
ax.plot(a['Jt'],a['entropy'],label=r'$S_A$'); ax.plot(a['Jt'],a['renyi2'],'--',label=r'$S_{2,A}$'); ax.plot(a['Jt'],a['occupation'],':',label=r'$p_1$')
ax.set(xlabel=r'$Jt$',ylabel='Entropy (nats) / probability',ylim=(-.03,1.05));ax.legend(ncol=3);save('two-qubit',fig)
a=load('ising-quench');fig,axs=plt.subplots(1,2,figsize=(8,3.2))
axs[0].plot(a['t'],a['magnetization']);axs[0].set(xlabel='t',ylabel=r'$L^{-1}\sum_j\langle Z_j\rangle$')
axs[1].plot(a['t'],a['entropy']);axs[1].set(xlabel='t',ylabel='Half-chain entropy (nats)');save('ising-quench',fig)
a=load('trotter-convergence');fig,ax=plt.subplots(figsize=(5.5,3.4));ax.loglog(a['dt'],a['state_error'],'o-',label='State error'); ax.loglog(a['dt'],a['dt']**2*a['state_error'][-1]/a['dt'][-1]**2,'--',label=r'$\propto\delta t^2$');ax.set(xlabel=r'$\delta t$',ylabel=r'$\|\psi_{\rm Trotter}-\psi_{\rm exact}\|$');ax.legend();save('trotter-convergence',fig)
a=load('free-fermions');fig,axs=plt.subplots(1,2,figsize=(8,3.1));axs[0].plot(a['t'],a['imbalance']);axs[0].set(xlabel='t',ylabel='Staggered imbalance');axs[1].plot(a['t'],a['entropy']);axs[1].set(xlabel='t',ylabel='Half-chain entropy (nats)');save('free-fermions',fig)
a=load('diffusion');fig,axs=plt.subplots(1,2,figsize=(8,3.1))
for t in np.unique(a['t']):
    b=a[a['t']==t];axs[0].plot(b['x'],b['density'],label=f't={t:g}');axs[1].plot(b['x']/np.sqrt(t),b['density']*np.sqrt(t),label=f't={t:g}')
axs[0].set(xlabel='x',ylabel='Density');axs[1].set(xlabel=r'$x/\sqrt{t}$',ylabel=r'$\sqrt{t}\,n(x,t)$',xlim=(-6,6));axs[0].legend();save('diffusion',fig)
a=load('kibble-zurek');fig,ax=plt.subplots(figsize=(6,3.4));ax.loglog(a['tauQ'],a['defect_density'],label='Near-critical mode integral');ax.loglog(a['tauQ'],a['asymptotic'],'--',label=r'$1/(2\pi\sqrt{2\tau_Q})$');ax.set(xlabel=r'$J\tau_Q$ (J=1)',ylabel='Defect density');ax.legend();save('kibble-zurek',fig)
a=load('loschmidt');fig,ax=plt.subplots(figsize=(7,3.2));ax.plot(a['t'],a['return_rate']);ax.set(xlabel='Jt (J=1)',ylabel=r'$-L^{-1}\ln|\mathcal{G}(t)|^2$',title=r'Ising quench: $g_i=1.5\ \to\ g_f=0.5$');save('loschmidt',fig)
a=load('amplitude-damping');fig,ax=plt.subplots(figsize=(6,3.4));ax.plot(a['t'],a['exact'],label=r'$e^{-\gamma t}$');ax.plot(a['t'],a['trajectory_average'],'--',label='10,000 trajectories');ax.fill_between(a['t'],a['exact']-2*a['standard_error'],a['exact']+2*a['standard_error'],alpha=.2,label='±2 standard errors');ax.set(xlabel=r'$\gamma t$',ylabel='Excited-state probability');ax.legend();save('amplitude-damping',fig)
a=load('monitored-circuit');fig,ax=plt.subplots(figsize=(7,3.4))
for p in np.unique(a['p']):
    b=a[a['p']==p];ax.plot(b['layer'],b['mean_renyi2'],label=f'p={p:g}')
ax.set(xlabel='Circuit layer',ylabel='Mean conditioned S₂ (nats)',title='Real Rᵧ/CZ circuit, L=6, 64 Born-sampled records');ax.legend();save('monitored-circuit',fig)
a=load('mps-compression');fig,axs=plt.subplots(1,2,figsize=(8,3.3));axs[0].semilogx(a['chi'],a['normalized_fidelity'],'o-',base=2);axs[0].set(xlabel='Maximum bond dimension',ylabel='Normalized fidelity');axs[1].semilogy(a['chi'],np.maximum(a['state_error'],1e-16),'o-');axs[1].set(xlabel='Maximum bond dimension',ylabel='Dense-state error');save('mps-compression',fig)
# A conceptual diagram, explicitly not simulated data.
fig,ax=plt.subplots(figsize=(10,5));ax.set(xlim=(0,10),ylim=(0,5));ax.axis('off')
boxes=[(0.3,2.1,2.1,1.0,'Local unitary\ndynamics',colors[0]),(3.1,3.5,2.5,.8,'States & entanglement',colors[1]),(3.1,2.1,2.5,.8,'Operators & scrambling',colors[3]),(3.1,.7,2.5,.8,'Charges & transport',colors[2]),(6.6,2.1,2.9,1.0,'What information\nremains accessible?',colors[0])]
for x,y,w,h,label,c in boxes:
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.12',facecolor=c,edgecolor='none',alpha=.95));ax.text(x+w/2,y+h/2,label,ha='center',va='center',color='white',fontsize=12)
for y in (3.9,2.5,1.1):
    ax.add_patch(FancyArrowPatch((2.4,2.6),(2.95,y),arrowstyle='-|>',mutation_scale=15,color='#677782',connectionstyle='arc3,rad=0'))
    ax.add_patch(FancyArrowPatch((5.75,y),(6.45,2.6),arrowstyle='-|>',mutation_scale=15,color='#677782'))
ax.text(5,.1,'Disorder · constraints · driving · baths · measurements',ha='center',fontsize=11,color='#3c525c');save('atlas',fig)
# Cover: original schematic combining a circuit and a hydrodynamic cone.
fig,ax=plt.subplots(figsize=(7,9));fig.patch.set_facecolor('#102b3a');ax.set_facecolor('#102b3a');ax.set(xlim=(0,7),ylim=(0,9));ax.axis('off')
for j in range(10):
    ax.plot([.6,6.4],[1.1+j*.28,1.1+j*.28],color='#54808c',lw=.65,alpha=.7)
for layer in range(13):
    x=.8+layer*.43
    for j in range(layer%2,9,2):
        ax.add_patch(FancyBboxPatch((x,1.02+j*.28),.22,.46,boxstyle='round,pad=.015',facecolor=colors[(layer+j)%4],edgecolor='none',alpha=.92))
ax.text(.55,8.3,'QUANTUM',fontsize=32,color='white',weight='bold');ax.text(.55,7.65,'MANY-BODY',fontsize=32,color='white',weight='bold');ax.text(.55,7.0,'DYNAMICS',fontsize=32,color='white',weight='bold');ax.text(.57,6.4,'AND QUANTUM INFORMATION',fontsize=16,color='#a4d9d8');ax.text(.57,5.5,'From local quantum mechanics\nto the research frontier',fontsize=16,color='#d8e6eb',linespacing=1.6);ax.text(.57,.45,'RESEARCH EDITION  •  OCTOBER 2026',fontsize=10,color='#b8d4da');save('cover',fig)
print('Rendered 12 original scientific figures/diagrams, PNG + vector PDF.')
