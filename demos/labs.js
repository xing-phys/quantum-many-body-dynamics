/* Transparent finite-model laboratories. No network access or dependencies. */
(function () {
  'use strict';
  const h = p => (p > 0 ? -p * Math.log(p) : 0) + (p < 1 ? -(1-p)*Math.log(1-p) : 0);
  const rng = seed => { let s = seed >>> 0 || 1; return () => { s ^= s << 13; s ^= s >>> 17; s ^= s << 5; return (s >>> 0) / 4294967296; }; };
  function rotate(v, site, theta) {
    const bit = 1 << site, c = Math.cos(theta/2), s = Math.sin(theta/2);
    for (let i=0; i<v.length; i++) if (!(i & bit)) {
      const a=v[i], b=v[i|bit]; v[i]=c*a-s*b; v[i|bit]=s*a+c*b;
    }
  }
  function cz(v, a, b) { for (let i=0; i<v.length; i++) if ((i & (1<<a)) && (i & (1<<b))) v[i] *= -1; }
  function measure(v, site, random) {
    const bit=1<<site; let p=0;
    for(let i=0;i<v.length;i++) if(i & bit) p+=v[i]*v[i];
    const result=random()<p, prob=result?p:1-p, scale=1/Math.sqrt(Math.max(prob,1e-30));
    for(let i=0;i<v.length;i++) v[i]=Boolean(i&bit)===result?v[i]*scale:0;
    return result;
  }
  function purity(v,L) {
    const a=1<<(L/2), b=v.length/a; let total=0;
    for(let i=0;i<a;i++) for(let j=0;j<a;j++) {
      let r=0; for(let k=0;k<b;k++) r+=v[i+a*k]*v[j+a*k]; total+=r*r;
    }
    return Math.min(1,Math.max(1/a,total));
  }
  function circuit(L,p,depth,count,seed) {
    const gateRandom=rng(seed), random=rng(seed+7919), angles=[];
    for(let t=0;t<depth;t++) angles.push(Array.from({length:L},()=>2*Math.PI*gateRandom()));
    const curve=new Float64Array(depth+1), states=[];
    for(let n=0;n<count;n++) {
      const v=new Float64Array(1<<L); v[0]=1;
      for(let t=0;t<depth;t++) {
        for(let j=0;j<L;j++) rotate(v,j,angles[t][j]);
        for(let j=t%2;j<L-1;j+=2) cz(v,j,j+1);
        for(let j=0;j<L;j++) if(random()<p) measure(v,j,random);
        curve[t+1]+=-Math.log(purity(v,L))/count;
      }
      states.push(v);
    }
    let mixedPurity=0;
    for(const v of states) for(const w of states) {
      let overlap=0;for(let i=0;i<v.length;i++) overlap+=v[i]*w[i];
      mixedPurity+=overlap*overlap/(count*count);
    }
    return {curve:Array.from(curve), mixedEntropy:-Math.log(Math.min(1,mixedPurity)), states};
  }
  function gaussian(x,D,t) { return Math.exp(-x*x/(4*D*t))/Math.sqrt(4*Math.PI*D*t); }
  const math={h,rng,rotate,cz,measure,purity,circuit,gaussian};
  if(typeof module!=='undefined' && module.exports) module.exports=math;
  if(typeof document==='undefined') return;
  function plot(canvas,curves,xmin,xmax,ymin,ymax,xlabel,ylabel,marker) {
    const c=canvas.getContext('2d'), w=900, height=380;canvas.width=w;canvas.height=height;
    c.fillStyle='#ffffff';c.fillRect(0,0,w,height);const left=70,right=25,top=25,bottom=55;
    const px=x=>left+(w-left-right)*(x-xmin)/(xmax-xmin),py=y=>height-bottom-(height-top-bottom)*(y-ymin)/(ymax-ymin);
    c.font='15px system-ui';c.strokeStyle='#dce3e7';c.fillStyle='#354b55';c.lineWidth=1;
    for(let j=0;j<=5;j++) {const y=ymin+(ymax-ymin)*j/5;c.beginPath();c.moveTo(left,py(y));c.lineTo(w-right,py(y));c.stroke();c.fillText(y.toFixed(2),6,py(y)+5);}
    for(let j=0;j<=5;j++) {const x=xmin+(xmax-xmin)*j/5;c.fillText(x.toFixed(1),px(x)-12,height-29);}
    for(const curve of curves) { c.strokeStyle=curve.color;c.lineWidth=2.5;c.beginPath();curve.points.forEach(([x,y],i)=>i?c.lineTo(px(x),py(y)):c.moveTo(px(x),py(y)));c.stroke(); }
    if(marker!==undefined){c.strokeStyle='#566873';c.setLineDash([5,5]);c.beginPath();c.moveTo(px(marker),top);c.lineTo(px(marker),height-bottom);c.stroke();c.setLineDash([]);}
    c.fillStyle='#354b55';c.fillText(xlabel,w/2-30,height-4);c.fillText(ylabel,left+5,17);
  }
  document.querySelectorAll('[data-lab="entanglement"]').forEach(el=>{
    const input=el.querySelector('input'),out=el.querySelector('output'),canvas=el.querySelector('canvas');
    function draw(){const t=+input.value,p=Math.sin(t)**2;plot(canvas,[{color:'#087f8c',points:Array.from({length:301},(_,i)=>{const x=i*Math.PI/300;return[x,h(Math.sin(x)**2)];})}],0,Math.PI,0,.75,'Jt','Subsystem entropy (nats)',t);out.textContent=`Jt=${t.toFixed(3)}; p₁=${p.toFixed(4)}; S(A)=${h(p).toFixed(4)} nats; global S=0.`;}
    input.addEventListener('input',draw);draw();
  });
  document.querySelectorAll('[data-lab="diffusion"]').forEach(el=>{
    const inputs=el.querySelectorAll('input'),out=el.querySelector('output'),canvas=el.querySelector('canvas');
    function draw(){const D=+inputs[0].value,t=+inputs[1].value;plot(canvas,[{color:'#087f8c',points:Array.from({length:501},(_,i)=>{const x=-25+i*.1;return[x,gaussian(x,D,t)];})}],-25,25,0,.65,'x','Density');out.textContent=`D=${D.toFixed(2)}, t=${t.toFixed(1)}; variance=2Dt=${(2*D*t).toFixed(2)}; full-line integrated charge=1.`;}
    inputs.forEach(i=>i.addEventListener('input',draw));draw();
  });
  document.querySelectorAll('[data-lab="circuit"]').forEach(el=>{
    const button=el.querySelector('button'),out=el.querySelector('output'),canvas=el.querySelector('canvas'),p=el.querySelector('[name=p]'),size=el.querySelector('[name=L]'),seed=el.querySelector('[name=seed]');
    function run(){button.disabled=true;out.textContent='Computing 32 conditioned trajectories…';setTimeout(()=>{
      const L=+size.value,prob=Math.max(0,Math.min(1,+p.value||0));p.value=prob;const result=circuit(L,prob,40,32,+seed.value||2026);
      plot(canvas,[{color:'#a53d55',points:result.curve.map((s,t)=>[t,s])}],0,40,0,L/2*Math.log(2),'Circuit layer','Mean conditioned S₂ (nats)');
      out.textContent=`L=${L}, p=${(+p.value).toFixed(2)}; final mean cut S₂=${result.curve[40].toFixed(3)}; S₂ of empirical average full state=${result.mixedEntropy.toFixed(3)}. Each trajectory remains globally pure. Finite sample; no critical-point inference.`;button.disabled=false;
    },20);}
    button.addEventListener('click',run);run();
  });
})();
