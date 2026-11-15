import json
I=json.load(open('i18n.json')); P=json.load(open('data/prices.json'))
T=r'''<!doctype html><html lang="hi-Latn"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Aaj Ke Daam · Chalo Samjhein with Nitin</title>
<meta name="description" content="Rasoi ka saman, dal, tel, sabzi, petrol-diesel (har rajya), sona-chaandi, rupaya aur Sensex-Nifty. Sarkari aur bharosemand source ke saath. 14 bhashaon mein.">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&family=Inter:wght@400;500;600;700;800&display=swap"><link rel="stylesheet" href="style.css"><link rel="icon" href="nitin.png">
<style>
.hero2{background:var(--navy);color:#fff;border-radius:26px;padding:24px 22px 20px;display:flex;flex-direction:column;gap:14px;position:relative;overflow:hidden}
.hero2::after{content:"";position:absolute;right:-60px;top:-60px;width:220px;height:220px;border-radius:50%;background:radial-gradient(circle,rgba(255,194,26,.35),transparent 70%)}
.hero2 h1{color:#fff;font-size:clamp(28px,6vw,46px)}
.hero2 h1 em{background:var(--gold);color:var(--navy)}
.hero2 .lede{color:#C9D6EA}
.upd{display:inline-flex;align-items:center;gap:8px;font-weight:800;font-size:13px;color:var(--gold);letter-spacing:.06em;text-transform:uppercase}
.upd i{width:9px;height:9px;border-radius:50%;background:#3DDC84;box-shadow:0 0 0 4px rgba(61,220,132,.25)}
.trust{display:flex;flex-wrap:wrap;gap:8px;position:relative;z-index:1}
.trust span{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.18);border-radius:999px;padding:6px 12px;font-size:13px;font-weight:700}
.pick{display:grid;grid-template-columns:1fr 1fr;gap:10px;position:relative;z-index:1}
.pick label{display:flex;flex-direction:column;gap:4px;font-size:11px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:#C9D6EA;min-width:0}
.pick select{font:inherit;font-size:16px;font-weight:700;letter-spacing:0;text-transform:none;padding:11px 12px;border-radius:12px;border:0;background:#fff;color:#0B213B;min-width:0;width:100%}
.tiles{display:grid;grid-template-columns:repeat(2,1fr);gap:12px}
@media(min-width:820px){.tiles{grid-template-columns:repeat(4,1fr)}}
.tile{background:var(--card);border-radius:20px;padding:16px;box-shadow:0 10px 26px rgba(11,33,59,.10);display:flex;flex-direction:column;gap:4px;min-width:0}
.tile .k{font-size:13px;font-weight:700;color:var(--muted);display:flex;gap:6px;align-items:center}
.tile .v{font-family:var(--display);font-size:clamp(22px,5vw,30px);font-weight:700;font-variant-numeric:tabular-nums;line-height:1.1}
.tile .s{font-size:12px;color:var(--muted)}
.tools{display:flex;gap:10px;flex-wrap:wrap}
.tools input{flex:1 1 220px;min-width:0;font:inherit;font-size:16px;padding:13px 16px;border-radius:14px;border:2px solid var(--line);background:var(--card);color:var(--ink)}
.tools input:focus-visible{outline:3px solid var(--gold);outline-offset:1px}
.wa{background:#1FA855;color:#fff}
.jump{display:flex;gap:6px;overflow-x:auto;padding-bottom:4px;scrollbar-width:none}
.jump a{flex:0 0 auto;text-decoration:none;font-weight:700;font-size:14px;padding:7px 13px;border-radius:999px;background:var(--card);border:1px solid var(--line)}
.blk{background:var(--card);border-radius:22px;padding:18px 18px 14px;box-shadow:0 10px 26px rgba(11,33,59,.08);display:flex;flex-direction:column;gap:6px;scroll-margin-top:84px;min-width:0}
.bh{display:flex;align-items:center;gap:12px}
.bh .ic{width:44px;height:44px;border-radius:14px;display:grid;place-items:center;font-size:24px;background:var(--chip);flex:0 0 auto}
.bh h2{font-size:20px}
.bh .u{margin-left:auto;font-size:12px;font-weight:800;color:var(--muted);white-space:nowrap}
.row{display:flex;align-items:center;gap:10px;padding:11px 2px;border-bottom:1px dashed var(--line)}
.row:last-of-type{border-bottom:0}
.row .n{flex:1;min-width:0;font-weight:700}
.row .n small{display:block;font-weight:500;color:var(--muted);font-size:12.5px}
.row .p{font-family:var(--display);font-weight:700;font-size:19px;font-variant-numeric:tabular-nums;white-space:nowrap}
.row .c{font-size:13px;font-weight:700;white-space:nowrap}
.cards{display:grid;grid-template-columns:repeat(2,1fr);gap:10px}
@media(min-width:620px){.cards{grid-template-columns:repeat(3,1fr)}}
@media(min-width:900px){.cards{grid-template-columns:repeat(4,1fr)}}
.ic2{background:var(--bg);border:1px solid var(--line);border-radius:16px;padding:12px;display:flex;flex-direction:column;gap:2px;min-width:0}
.ic2 .e{font-size:26px;line-height:1}
.ic2 .n{font-weight:700;font-size:15px;margin-top:6px;overflow-wrap:anywhere}
.ic2 .n small{display:block;font-weight:500;color:var(--muted);font-size:12px}
.ic2 .p{font-family:var(--display);font-weight:700;font-size:22px;font-variant-numeric:tabular-nums;margin-top:4px}
.ic2 .x{font-size:12px;color:var(--muted);font-weight:600}
.verified{display:flex;gap:8px;align-items:flex-start;background:var(--chip);border-radius:12px;padding:9px 11px;font-size:12.5px;color:var(--muted);margin-top:6px}
.verified b{color:var(--green)}
.up{color:var(--green)}.dn{color:var(--red)}
.grid2{display:grid;grid-template-columns:1fr;gap:16px}
@media(min-width:820px){.grid2{grid-template-columns:1fr 1fr}}
.how{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px}
.how div{background:var(--card);border-radius:18px;padding:16px;box-shadow:0 8px 20px rgba(11,33,59,.06)}
.how b{display:block;font-family:var(--display);margin-bottom:4px}
.how span{color:var(--muted);font-size:14px}
.note{background:var(--chip);border-radius:14px;padding:12px 14px;font-size:14px;color:var(--muted)}
.empty{display:none;color:var(--muted);font-weight:600}
main[dir=rtl] .bh .u{margin-left:0;margin-right:auto}
</style></head><body>
<nav class="top" aria-label="Main"><div class="in"><a class="brand" href="./"><img src="nitin.png" alt="">Chalo Samjhein with Nitin</a><div class="links"><a href="./">Home</a><a href="episodes.html">Episodes</a><a href="tools.html" aria-current="page">Free tools</a><a href="disclaimer.html">Disclaimer</a></div></div></nav>
<main class="in">
<section class="hero2">
<span class="upd"><i></i><span id="upd">Updated</span></span>
<h1 id="h1"></h1>
<p class="lede" data-u="lede"></p>
<div class="trust"><span>✅ Govt of India data</span><span>📌 Source on every number</span><span>🚫 No tips, no selling</span><span>🔄 Updated daily</span></div>
<div class="pick"><label><span data-u="lang"></span><select id="lang"></select></label><label><span data-u="state"></span><select id="st"></select></label></div>
</section>
<section class="tiles" id="tiles"></section>
<div class="tools"><input id="q" type="search"><a class="btn wa" id="wa" href="#" target="_blank" rel="noopener"><span aria-hidden="true">💬</span><span data-u="wa"></span></a></div>
<nav class="jump" aria-label="Sections"><a href="#fuel">⛽</a><a href="#anaaj">🌾</a><a href="#dal">🫘</a><a href="#tel">🫙</a><a href="#sabzi">🥔</a><a href="#roz">🥛</a><a href="#sona">🪙</a><a href="#market">📈</a></nav>
<p class="empty" id="none">—</p>
<section class="blk" id="fuel"><div class="bh"><span class="ic">⛽</span><h2><span data-u="fuel"></span> · <span id="stname"></span></h2></div><div id="fuelb"></div>
<div class="verified"><b>✔</b><span id="fuelsrc"></span></div></section>
<div id="kit" style="display:flex;flex-direction:column;gap:16px"></div>
<div style="display:flex;flex-direction:column;gap:16px">
<section class="blk" id="sona"><div class="bh"><span class="ic">🪙</span><h2 data-u="sona"></h2></div><div id="sonab"></div>
<div class="verified"><b>✔</b><span>IBJA (via 5paisa), HDFC Sky / PTI. Excl. GST and making charges; your jeweller's bill will be higher.</span></div></section>
<section class="blk" id="market"><div class="bh"><span class="ic">📈</span><h2 data-u="market"></h2></div><div id="marketb"></div>
<div class="verified"><b>✔</b><span>Upstox, Business Standard, 5paisa, Liquide. Closing values only; not a signal for what comes next.</span></div></section>
</div>
<p class="note" data-u="stnote"></p>
<div class="disc"><b>Not SEBI-registered.</b> <span data-u="disc"></span></div>
</main>
<footer><div class="in"><span><b>Not SEBI-registered.</b> Education and information only. Nothing here is a buy, sell or hold recommendation. I never ask for money or share tips on WhatsApp or Telegram; any such message is a fraud. Cyber fraud helpline: 1930 · cybercrime.gov.in</span><span><a href="https://www.youtube.com/@ChaloSamjheinWithNitin" target="_blank" rel="noopener">YouTube</a> · <a href="https://www.instagram.com/chalosamjheinwithnitin/" target="_blank" rel="noopener">Instagram</a> · <a href="disclaimer.html">Full disclaimer</a></span></div></footer>
<script>
const I=__I18N__;let P=__P__;
const ICON={anaaj:'🌾',dal:'🫘',tel:'🫙',sabzi:'🥔',roz:'🥛'};
const EM={rice:'🍚',wheat:'🌾',atta:'🌾',maida:'🥣',suji:'🥣',besan:'🟡',bajra:'🌾',jowar:'🌾',ragi:'🌾',tur:'🫘',urad:'🫘',moong:'🫘',chana:'🫘',masoor:'🫘',mustard:'🫙',groundnut:'🥜',sunflower:'🌻',soya:'🫙',vanaspati:'🫙',palm:'🌴',ghee:'🧈',potato:'🥔',onion:'🧅',tomato:'🍅',brinjal:'🍆',milk:'🥛',sugar:'🍬',gur:'🟤',tea:'🍵',salt:'🧂',petrol:'⛽',diesel:'🛢️',gold:'🪙',silver:'🥈',usd:'💵'};
const card=(e,n,p,x)=>`<div class="ic2 row"><span class="e">${e}</span><span class="n">${n}</span><span class="p">${p}</span>${x?`<span class="x">${x}</span>`:''}</div>`;
const store={get(k){try{return localStorage.getItem(k)}catch(e){return null}},set(k,v){try{localStorage.setItem(k,v)}catch(e){}}};
const $=id=>document.getElementById(id),lang=$('lang'),st=$('st'),q=$('q');
I.L.forEach(l=>lang.add(new Option(I.LN[l],l)));
const f=n=>Number(n).toLocaleString('en-IN',{minimumFractionDigits:2,maximumFractionDigits:2});
const kit=id=>{for(const r of Object.values(P.kit))for(const [k,p] of r)if(k===id)return p};
function fillStates(){const cur=st.value||store.get('wp_state')||'Delhi';st.innerHTML='';Object.keys(P.fuel).forEach(s=>st.add(new Option(s,s)));st.value=P.fuel[cur]?cur:'Delhi'}
function render(){const l=lang.value,U=k=>I.U[k][l],N=k=>I.I[k][l],en=k=>(l!=='en'&&l!=='hing')?`<small>${I.I[k].en}</small>`:'';
document.documentElement.lang=l==='hing'?'hi-Latn':l;document.querySelector('main').dir=l==='ur'?'rtl':'ltr';
$('h1').innerHTML=U('title').replace(/,\s*/,', <em>').replace(/$/,'</em>');
document.querySelectorAll('[data-u]').forEach(e=>e.textContent=U(e.dataset.u));q.placeholder=U('search');
$('upd').textContent='Updated '+P.updated+' · Kitchen '+P.dates.kitchen+' · Market '+P.dates.market;
const [pe,di]=P.fuel[st.value];$('stname').textContent=st.value;
$('tiles').innerHTML=[[`⛽ ${N('petrol')}`,'₹'+f(pe),st.value],[`🪙 ${N('gold')}`,'₹'+P.gold.now,P.gold.nowDate],[`🌾 ${N('atta')}`,'₹'+f(kit('atta')),'per kg · '+P.dates.kitchen],['📈 Nifty 50',P.market[1][1],P.market[1][2]+' · '+P.dates.market]].map(t=>`<div class="tile"><span class="k">${t[0]}</span><span class="v">${t[1]}</span><span class="s">${t[2]}</span></div>`).join('');
$('fuelb').innerHTML='<div class="cards">'+[['petrol',pe],['diesel',di]].map(([k,v])=>card(EM[k],N(k)+en(k),'₹'+f(v),'per litre')).join('')+'</div>';
$('fuelsrc').textContent='Goodreturns state-wise rates, cross-checked with Punjab Kesari / HDFC Sky ('+P.dates.fuel+'). State capital / main city; can change daily at 6 am.';
let k='';for(const [sec,rows] of Object.entries(P.kit)){k+=`<section class="blk" id="${sec}"><div class="bh"><span class="ic">${ICON[sec]}</span><h2>${U(sec)}</h2></div>`+'<div class="cards">'+rows.map(([id,p])=>card(EM[id],N(id)+en(id),'₹'+f(p),id==='milk'?'per litre':'per kg')).join('')+`</div><div class="verified"><b>✔</b><span>Dept of Consumer Affairs, Govt of India · all-India average retail · ${P.dates.kitchen}</span></div></section>`}
$('kit').innerHTML=k;
$('sonab').innerHTML='<div class="cards">'+[['gold',P.gold],['silver',P.silver],['usd',P.usd]].map(([id,o])=>card(EM[id],N(id)+en(id),(id==='usd'?'₹':'₹')+o.now,P.gold.prevDate+': ₹'+o.prev)).join('')+'</div>';
$('marketb').innerHTML='<div class="cards">'+P.market.map(r=>card('📈',r[0],r[1],`<span class="${/^[−-]/.test(r[2])?'dn':'up'}">${r[2]}</span> · ${P.dates.market}`)).join('')+'</div>';
$('wa').href='https://wa.me/?text='+encodeURIComponent(U('title')+' 👉 '+location.href);filter()}
function filter(){const v=q.value.trim().toLowerCase();let any=false;document.querySelectorAll('.blk').forEach(b=>{let n=0;b.querySelectorAll('.row').forEach(r=>{const ok=!v||r.textContent.toLowerCase().includes(v)||b.querySelector('h2').textContent.toLowerCase().includes(v);r.style.display=ok?'':'none';if(ok)n++});b.style.display=n?'':'none';if(n)any=true});$('none').style.display=any?'none':'block'}
lang.value=store.get('wp_lang')||'hing';fillStates();
lang.onchange=()=>{store.set('wp_lang',lang.value);render()};st.onchange=()=>{store.set('wp_state',st.value);render()};q.oninput=filter;render();
fetch('data/prices.json',{cache:'no-store'}).then(r=>r.json()).then(d=>{P=d;fillStates();render()}).catch(()=>{});
</script></body></html>'''
open('weekly-prices.html','w').write(T.replace('__I18N__',json.dumps(I,ensure_ascii=False)).replace('__P__',json.dumps(P,ensure_ascii=False)))
print('ok')
