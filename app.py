import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Elodie Marcouire | Portfolio",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ─────────────────────────────────────────────
# NAVIGATION
# ─────────────────────────────────────────────
nav_items = ["Accueil", "Projets", "Voyages", "Expérimentations"]
page = st.query_params.get("page", "Accueil")
if page not in nav_items:
    page = "Accueil"

# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────

# ─────────────────────────────────────────────
# STYLE GLOBAL CONTENU
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;1,400&family=DM+Sans:wght@300;400;500&display=swap');

header { visibility: hidden; }
footer { visibility: hidden; }
#MainMenu { visibility: hidden; }

:root {
    --cream: #f4f1ed;
    --ink:   #1c1c1c;
    --muted: #7a7a7a;
    --coral: #d95f4b;
    --sage:  #7a9e7e;
    --gold:  #c9a84c;
    --white: #ffffff;
}
.stApp { background-color: var(--cream); color: var(--ink); font-family: 'DM Sans', sans-serif; }

.hero-wrap { text-align:center; padding:60px 20px 20px; border-bottom:1px solid #ddd; margin-bottom:48px; }
.hero-name { font-family:'Playfair Display',serif; font-size:clamp(40px,8vw,88px); font-weight:700; letter-spacing:-0.02em; line-height:1; color:var(--ink); }
.hero-subtitle { font-size:14px; font-weight:300; letter-spacing:0.25em; text-transform:uppercase; color:var(--muted); margin-top:14px; }
.hero-accent { display:inline-block; width:40px; height:3px; background:var(--coral); margin:18px auto 0; }

.section-label { font-size:11px; font-weight:500; letter-spacing:0.3em; text-transform:uppercase; color:var(--coral); margin-bottom:6px; }
.section-title { font-family:'Playfair Display',serif; font-size:clamp(22px,4vw,30px); font-weight:700; color:var(--ink); margin-bottom:24px; }

.bio-card { background:var(--white); border-radius:12px; padding:30px 32px; box-shadow:0 2px 24px rgba(0,0,0,0.06); line-height:1.85; font-size:15px; color:#333; }
.bio-card strong { color:var(--ink); font-weight:500; }
.bio-highlight { display:inline-block; background:#fdf3e7; color:var(--coral); font-weight:500; padding:1px 8px; border-radius:4px; }

.projet-card { background:var(--white); border-radius:12px; padding:24px 26px; box-shadow:0 2px 16px rgba(0,0,0,0.05); margin-bottom:14px; border-left:4px solid var(--coral); }
.projet-title { font-family:'Playfair Display',serif; font-size:18px; font-weight:700; color:var(--ink); margin-bottom:8px; }
.projet-tags { display:flex; gap:8px; flex-wrap:wrap; margin-top:10px; }
.tag { font-size:10px; font-weight:500; letter-spacing:0.08em; text-transform:uppercase; padding:3px 9px; border-radius:20px; background:var(--cream); color:var(--muted); border:1px solid #ddd; }
.map-intro { font-size:15px; color:var(--muted); max-width:600px; margin-bottom:20px; line-height:1.7; }
</style>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════
# NAVBAR — rendue avant chaque page
# ═══════════════════════════════════════════════
_links = ""
for _item in nav_items:
    _active = _item == page
    _color = "white" if _active else "rgba(255,255,255,0.5)"
    _border = "border-bottom:2px solid #d95f4b;" if _active else "border-bottom:2px solid transparent;"
    _links += (
        f'<a href="?page={_item}" style="' 
        f'font-family:DM Sans,sans-serif;font-size:11px;font-weight:500;' 
        f'letter-spacing:0.2em;text-transform:uppercase;text-decoration:none;' 
        f'color:{_color};padding:0 18px;height:56px;display:flex;' 
        f'align-items:center;{_border}">{_item}</a>'
    )

st.markdown(f"""
<style>.nav-scroll::-webkit-scrollbar{{display:none;}}</style>
<div style="background:#1c1c1c;display:flex;align-items:center;
justify-content:space-between;padding:0 20px 0 24px;height:56px;
margin-bottom:0;flex-wrap:nowrap;">
  <span style="font-family:Playfair Display,serif;font-size:16px;
  font-weight:700;color:white;letter-spacing:-0.01em;white-space:nowrap;
  margin-right:12px;flex-shrink:0;">E. Marcouire</span>
  <div class="nav-scroll" style="display:flex;align-items:center;height:56px;
  overflow-x:auto;-webkit-overflow-scrolling:touch;flex-shrink:1;
  scrollbar-width:none;">{_links}</div>
</div>
""", unsafe_allow_html=True)

# Hint nav affiché sous la barre uniquement sur mobile
st.markdown("""
<style>
  .nav-mobile-hint { display:none; }
  @media(max-width:600px){ .nav-mobile-hint { display:block; } }
</style>
<div class="nav-mobile-hint" style="background:#1c1c1c;padding:2px 24px 6px;
font-size:9px;color:rgba(255,255,255,0.3);text-align:right;">← défiler →</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════
# ACCUEIL
# ═══════════════════════════════════════════════
if page == "Accueil":

    st.markdown("""
    <div class="hero-wrap">
        <div class="hero-name">Elodie Marcouire</div>
        <div class="hero-subtitle">Data Analyst · Bordeaux</div>
        <div class="hero-accent"></div>
    </div>
    """, unsafe_allow_html=True)

    # ── FRISE ─────────────────────────────────
    st.markdown('<div class="section-label">Parcours</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Ma trajectoire</div>', unsafe_allow_html=True)

    components.html("""
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
    <style>
      * { box-sizing:border-box; margin:0; padding:0; }
      html,body { background:#f4f1ed; overflow-x:hidden; }
      .tl-scroll { width:100%; overflow-x:auto; -webkit-overflow-scrolling:touch; }
      .tl { display:flex; min-width:600px; padding:10px 8px 24px; }
      .tl-item { flex:1; min-width:130px; position:relative; padding:26px 10px 16px; }
      .tl-item::before { content:""; position:absolute; top:19px; left:0; right:0; height:2px; background:#d9d5cf; }
      .tl-item:first-child::before { left:50%; }
      .tl-item:last-child::before  { right:50%; }
      .tl-dot { width:14px; height:14px; border-radius:50%; background:#d95f4b; border:3px solid #f4f1ed; box-shadow:0 0 0 2px #d95f4b; margin:0 auto 14px; position:relative; z-index:1; }
      .current .tl-dot { background:#7a9e7e; box-shadow:0 0 0 2px #7a9e7e; }
      .future  .tl-dot { background:transparent; border-color:#ccc; box-shadow:0 0 0 2px #ccc; }
      .tl-year { font-family:'Playfair Display',serif; font-size:17px; font-weight:700; color:#1c1c1c; text-align:center; margin-bottom:5px; }
      .current .tl-year { color:#7a9e7e; }
      .future  .tl-year { color:#7a7a7a; font-style:italic; }
      .tl-role { font-family:'DM Sans',sans-serif; font-size:11px; font-weight:500; color:#1c1c1c; text-align:center; margin-bottom:3px; }
      .tl-detail { font-family:'DM Sans',sans-serif; font-size:10px; color:#7a7a7a; text-align:center; line-height:1.5; }
    </style>
    <style>
      .hint { display:none; font-family:'DM Sans',sans-serif; font-size:9px; color:#bbb; text-align:right; padding:0 8px 2px; }
      @media(max-width:560px){ .hint { display:block; } }
    </style>
    <p class="hint">← défiler →</p>
    <div class="tl-scroll"><div class="tl">
      <div class="tl-item"><div class="tl-dot"></div><div class="tl-year">2002–18</div><div class="tl-role">Maroc · Mauritanie · Sénégal</div><div class="tl-detail">Grandir entre cultures,<br>lire les contextes</div></div>
      <div class="tl-item"><div class="tl-dot"></div><div class="tl-year">2020</div><div class="tl-role">Bac ES</div><div class="tl-detail">Spé. Mathématiques<br>Mention Bien</div></div>
      <div class="tl-item"><div class="tl-dot"></div><div class="tl-year">2020</div><div class="tl-role">Bordeaux</div><div class="tl-detail">Licence MIASHS<br>Université de Bordeaux</div></div>
      <div class="tl-item"><div class="tl-dot"></div><div class="tl-year">2023</div><div class="tl-role">Premiers dashboards</div><div class="tl-detail">Power BI · SQL · Python<br>La donnée comme langage</div></div>
      <div class="tl-item current"><div class="tl-dot"></div><div class="tl-year">2024 →</div><div class="tl-role">Alternante Data Analyst</div><div class="tl-detail">Domofrance<br>Snowflake · Talend · Power BI</div></div>
      <div class="tl-item future"><div class="tl-dot"></div><div class="tl-year">2026+</div><div class="tl-role">What's next?</div><div class="tl-detail">La suite est<br>encore à écrire ✦</div></div>
    </div></div>
    """, height=168)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── BIO + RADARS ──────────────────────────
    col_bio, col_radar = st.columns([3, 2], gap="large")

    with col_bio:
        st.markdown('<div class="section-label">À propos</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Qui suis-je ?</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="bio-card">
            <p>J'ai grandi entre le <strong>Maroc, la Mauritanie et le Sénégal</strong>
            avant de poser mes valises à Bordeaux pour ma licence
            <span class="bio-highlight">MIASHS</span>.
            Cette enfance nomade m'a appris une chose essentielle :
            comprendre rapidement un contexte inconnu — une compétence
            précieuse quand on explore un nouveau dataset.</p>
            <p style="margin-top:14px;">Aujourd'hui <strong>alternante Data Analyst chez Domofrance</strong>,
            je travaille au quotidien avec <span class="bio-highlight">Power BI · Snowflake · Talend</span>
            pour transformer des données brutes en tableaux de bord actionnables.
            J'interviens sur toute la chaîne : collecte, modélisation, visualisation et documentation.</p>
            <p style="margin-top:14px;">Ce qui me motive ? Ce moment un peu magique où un dataset chaotique
            révèle soudainement un pattern — parce que la donnée, c'est d'abord une <strong>histoire à raconter</strong>.</p>
        </div>
        """, unsafe_allow_html=True)

    with col_radar:
        st.markdown('<div class="section-label">Compétences</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Stack</div>', unsafe_allow_html=True)
        components.html("""
        <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500&display=swap" rel="stylesheet">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
        <style>
          * { box-sizing:border-box; margin:0; padding:0; }
          html,body { background:#f4f1ed; font-family:'DM Sans',sans-serif; }
          .wrap { display:flex; gap:8px; width:100%; }
          .chart-box { flex:1; text-align:center; min-width:0; }
          .chart-label { font-size:10px; font-weight:500; letter-spacing:0.18em; text-transform:uppercase; color:#7a7a7a; margin-bottom:6px; }
          .canvas-wrap { position:relative; width:100%; height:240px; }
        </style>
        <div class="wrap">
          <div class="chart-box"><div class="chart-label">Langages</div><div class="canvas-wrap"><canvas id="r1"></canvas></div></div>
          <div class="chart-box"><div class="chart-label">Outils métier</div><div class="canvas-wrap"><canvas id="r2"></canvas></div></div>
        </div>
        <script>
          const base={type:'radar',options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{r:{min:0,max:4,ticks:{display:false},grid:{color:'#e0dcd6'},angleLines:{color:'#e0dcd6'},pointLabels:{font:{family:'DM Sans',size:11},color:'#1c1c1c',padding:10}}}}};
          new Chart(document.getElementById('r1'),{...base,data:{labels:['Python','SQL','Excel','R'],datasets:[{data:[3,4,3,2],backgroundColor:'rgba(217,95,75,0.2)',borderColor:'#d95f4b',borderWidth:2,pointBackgroundColor:'#d95f4b',pointRadius:3}]}});
          new Chart(document.getElementById('r2'),{...base,data:{labels:['Snowflake','Talend','Power BI','DataGalaxy','Confluence'],datasets:[{data:[3,3,4,2,2],backgroundColor:'rgba(122,158,126,0.2)',borderColor:'#7a9e7e',borderWidth:2,pointBackgroundColor:'#7a9e7e',pointRadius:3}]}});
        </script>
        """, height=280)

    # ── DASHBOARD PRO ─────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-label">Dashboard pro</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Domofrance · ce que j&#39;ai produit</div>', unsafe_allow_html=True)

    components.html("""
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
    <style>
      * { box-sizing:border-box; margin:0; padding:0; }
      html,body { background:#f4f1ed; font-family:'DM Sans',sans-serif; }
      .db { border-radius:12px; overflow:hidden; box-shadow:0 4px 28px rgba(0,0,0,0.1); }
      .db-head { background:#1c1c1c; padding:13px 20px; display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:8px; }
      .db-head-title { font-family:'Playfair Display',serif; font-size:14px; font-weight:700; color:white; }
      .db-badge { font-size:9px; font-weight:500; letter-spacing:0.15em; text-transform:uppercase; background:rgba(217,95,75,0.25); color:#d95f4b; padding:4px 10px; border-radius:20px; border:1px solid rgba(217,95,75,0.35); }
      .kpi-row { display:grid; grid-template-columns:repeat(4,1fr); gap:1px; background:#e0dcd6; border-left:1px solid #e0dcd6; border-right:1px solid #e0dcd6; }
      .kpi { background:#fff; padding:14px 16px; }
      .kpi-lbl { font-size:9px; font-weight:500; letter-spacing:0.16em; text-transform:uppercase; color:#7a7a7a; margin-bottom:6px; }
      .kpi-val { font-family:'Playfair Display',serif; font-size:24px; font-weight:700; color:#1c1c1c; line-height:1; margin-bottom:4px; }
      .kpi-sub { font-size:10px; color:#7a7a7a; }
      .kpi-sub.up { color:#7a9e7e; font-weight:500; }
      .kpi-sub.warn { color:#d95f4b; font-weight:500; }
      .charts { display:grid; grid-template-columns:1fr; gap:1px; background:#e0dcd6; border:1px solid #e0dcd6; border-top:none; }
      .panel { background:#fff; padding:14px 14px 10px; }
      .panel-title { font-size:9px; font-weight:500; letter-spacing:0.14em; text-transform:uppercase; color:#7a7a7a; margin-bottom:10px; }
      .ch { position:relative; width:100%; height:180px; }
      .db-foot { background:#fff; border:1px solid #e0dcd6; border-top:none; border-radius:0 0 12px 12px; padding:7px 14px; display:flex; justify-content:space-between; flex-wrap:wrap; gap:4px; font-size:9px; color:#bbb; }
      @media(max-width:600px){ .kpi-row{grid-template-columns:repeat(2,1fr);} .kpi-val{font-size:18px;} }
    </style>
    <div class="db">
      <div class="db-head">
        <span class="db-head-title">TBD Activité · Domofrance — alternance 2024/2026</span>
        <span class="db-badge">Data Analyst en prod</span>
      </div>
      <div class="kpi-row">
        <div class="kpi"><div class="kpi-lbl">Projets bout-en-bout</div><div class="kpi-val">2</div><div class="kpi-sub up">↑ Conception → livraison</div></div>
        <div class="kpi"><div class="kpi-lbl">Mises en prod / semaine</div><div class="kpi-val">~1</div><div class="kpi-sub up">↑ dès le 5ème mois</div></div>
        <div class="kpi"><div class="kpi-lbl">Data Marts créés</div><div class="kpi-val">2</div><div class="kpi-sub">modélisation de A à Z</div></div>
        <div class="kpi"><div class="kpi-lbl">Bugs résolus</div><div class="kpi-val">∞</div><div class="kpi-sub warn">↯ c'est le métier</div></div>
      </div>
      <div class="charts">
        <div class="panel"><div class="panel-title">Répartition activité · volume estimé</div><div class="ch"><canvas id="donut"></canvas></div></div>
        <div class="panel"><div class="panel-title">Montée en compétences · indice /10</div><div class="ch"><canvas id="progress"></canvas></div></div>
      </div>
      <div class="db-foot">
        <span>Stack : Power BI · Snowflake · Talend · SQL · DataGalaxy · Confluence</span>
        <span>Mis à jour mars 2026</span>
      </div>
    </div>
    <script>
    new Chart(document.getElementById('donut'),{type:'doughnut',data:{labels:['Run & MEP','Projets structurants','Debug & support','Data Marts'],datasets:[{data:[45,25,20,10],backgroundColor:['#d95f4b','#7a9e7e','#c9a84c','#9b8fcf'],borderWidth:2,borderColor:'#fff',hoverOffset:6}]},options:{responsive:true,maintainAspectRatio:false,cutout:'60%',plugins:{legend:{position:'bottom',labels:{font:{family:'DM Sans',size:9},color:'#555',boxWidth:10,padding:8}}}}});
    const months=['Oct 24','Nov 24','Déc 24','Jan 25','Fév 25','Mar 25','Avr 25','Mai 25','Jun 25','Jul 25','Aoû 25','Mar 26'];
    new Chart(document.getElementById('progress'),{type:'line',data:{labels:months,datasets:[{label:'SQL/Snowflake',data:[4,5,5,6,6,7,7,7,8,8,8,8.5],borderColor:'#d95f4b',backgroundColor:'rgba(217,95,75,0.07)',borderWidth:2,pointRadius:3,tension:0.4,fill:true},{label:'Power BI',data:[5,6,6,7,7,7,8,8,8,8,8,8],borderColor:'#7a9e7e',backgroundColor:'rgba(122,158,126,0.07)',borderWidth:2,pointRadius:3,tension:0.4,fill:true},{label:'Python',data:[3,3,4,4,5,5,6,6,6,7,7,7],borderColor:'#c9a84c',backgroundColor:'rgba(201,168,76,0.07)',borderWidth:2,pointRadius:3,tension:0.4,fill:true}]},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{labels:{font:{family:'DM Sans',size:9},color:'#555',boxWidth:10,padding:8}}},scales:{x:{grid:{display:false},ticks:{font:{size:8},color:'#aaa',maxRotation:45}},y:{min:0,max:10,grid:{color:'#f4f1ed'},ticks:{font:{size:8},color:'#aaa',stepSize:2}}}}});
    </script>
    """, height=620, scrolling=True)

    # ── DASHBOARD PERSO ───────────────────────
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-label">Dashboard perso</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Elodie · les stats qui comptent vraiment</div>', unsafe_allow_html=True)

    components.html("""
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
    <style>
      * { box-sizing:border-box; margin:0; padding:0; }
      html,body { background:#f4f1ed; font-family:'DM Sans',sans-serif; }
      .db { border-radius:12px; overflow:hidden; box-shadow:0 4px 28px rgba(0,0,0,0.1); }
      .db-head { background:#1c1c1c; padding:13px 20px; display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:8px; }
      .db-head-title { font-family:'Playfair Display',serif; font-size:14px; font-weight:700; color:white; }
      .db-badge { font-size:9px; font-weight:500; letter-spacing:0.15em; text-transform:uppercase; background:rgba(122,158,126,0.3); color:#7a9e7e; padding:4px 10px; border-radius:20px; border:1px solid rgba(122,158,126,0.4); }
      .kpi-row { display:grid; grid-template-columns:repeat(4,1fr); gap:1px; background:#e0dcd6; border-left:1px solid #e0dcd6; border-right:1px solid #e0dcd6; }
      .kpi { background:#fff; padding:14px 16px; }
      .kpi-lbl { font-size:9px; font-weight:500; letter-spacing:0.16em; text-transform:uppercase; color:#7a7a7a; margin-bottom:6px; }
      .kpi-val { font-family:'Playfair Display',serif; font-size:22px; font-weight:700; color:#1c1c1c; line-height:1.1; margin-bottom:4px; }
      .kpi-sub { font-size:10px; color:#7a7a7a; }
      .kpi-sub.fun { color:#c9a84c; font-weight:500; font-style:italic; }
      .kpi-sub.up  { color:#7a9e7e; font-weight:500; }
      .charts { display:grid; grid-template-columns:1fr; gap:1px; background:#e0dcd6; border:1px solid #e0dcd6; border-top:none; }
      .panel { background:#fff; padding:14px 14px 10px; }
      .panel-title { font-size:9px; font-weight:500; letter-spacing:0.14em; text-transform:uppercase; color:#7a7a7a; margin-bottom:10px; }
      .ch { position:relative; width:100%; height:200px; }
      .lang-row { display:flex; align-items:center; gap:10px; margin-bottom:10px; }
      .lang-name { font-size:11px; font-weight:500; color:#1c1c1c; width:120px; flex-shrink:0; }
      .lang-bar-bg { flex:1; background:#f4f1ed; border-radius:4px; height:10px; overflow:hidden; }
      .lang-bar-fill { height:100%; border-radius:4px; }
      .lang-pct { font-size:10px; color:#7a7a7a; width:36px; text-align:right; flex-shrink:0; }
      .db-foot { background:#fff; border:1px solid #e0dcd6; border-top:none; border-radius:0 0 12px 12px; padding:7px 14px; display:flex; justify-content:space-between; flex-wrap:wrap; gap:4px; font-size:9px; color:#bbb; }
      @media(max-width:600px){ .kpi-row{grid-template-columns:repeat(2,1fr);} .kpi-val{font-size:18px;} }
    </style>
    <div class="db">
      <div class="db-head">
        <span class="db-head-title">TBD Vie · Edition Elodie Marcouire 2026</span>
        <span class="db-badge">Données certifiées authentiques</span>
      </div>
      <div class="kpi-row">
        <div class="kpi"><div class="kpi-lbl">Pays visités</div><div class="kpi-val">9</div><div class="kpi-sub up">↗ prochain : à déterminer</div></div>
        <div class="kpi"><div class="kpi-lbl">Taux trad. métier → data</div><div class="kpi-val">98 %</div><div class="kpi-sub fun">✦ 2% intraduisibles</div></div>
        <div class="kpi"><div class="kpi-lbl">Langues parlées</div><div class="kpi-val">3</div><div class="kpi-sub">FR · EN · Métier data</div></div>
        <div class="kpi"><div class="kpi-lbl">Curiosités / jour</div><div class="kpi-val">∞</div><div class="kpi-sub fun">non significatif</div></div>
      </div>
      <div class="charts">
        <div class="panel">
          <div class="panel-title">Maîtrise linguistique · /100</div>
          <div style="padding:8px 0 0;">
            <div class="lang-row"><span class="lang-name">🇫🇷 Français</span><div class="lang-bar-bg"><div class="lang-bar-fill" style="width:100%;background:#d95f4b;"></div></div><span class="lang-pct">100 %</span></div>
            <div class="lang-row"><span class="lang-name">🇬🇧 Anglais</span><div class="lang-bar-bg"><div class="lang-bar-fill" style="width:78%;background:#c9a84c;"></div></div><span class="lang-pct">78 %</span></div>
            <div class="lang-row"><span class="lang-name">📊 Langage métier</span><div class="lang-bar-bg"><div class="lang-bar-fill" style="width:98%;background:#7a9e7e;"></div></div><span class="lang-pct">98 %</span></div>
            <div class="lang-row"><span class="lang-name">🐍 Python</span><div class="lang-bar-bg"><div class="lang-bar-fill" style="width:70%;background:#9b8fcf;"></div></div><span class="lang-pct">70 %</span></div>
            <div class="lang-row"><span class="lang-name">🗄️ SQL</span><div class="lang-bar-bg"><div class="lang-bar-fill" style="width:85%;background:#d95f4b;opacity:0.7;"></div></div><span class="lang-pct">85 %</span></div>
            <div style="margin-top:12px;padding-top:8px;border-top:1px solid #f4f1ed;font-size:9px;color:#bbb;font-style:italic;">* 2% intraduisibles = réunions sans compte-rendu.</div>
          </div>
        </div>
        <div class="panel">
          <div class="panel-title">Continents explorés · indice dépaysement /5</div>
          <div class="ch"><canvas id="geo"></canvas></div>
        </div>
      </div>
      <div class="db-foot">
        <span>Sources : expérience personnelle · mémoire vive · feeling général</span>
        <span>Données non contractuelles · 16/03/2026</span>
      </div>
    </div>
    <script>
    new Chart(document.getElementById('geo'),{type:'radar',data:{labels:["Afrique de l'ouest","Europe du sud","Europe du nord","Asie du sud-est","Maghreb"],datasets:[{data:[5,4,3,3,5],backgroundColor:'rgba(201,168,76,0.2)',borderColor:'#c9a84c',borderWidth:2,pointBackgroundColor:'#c9a84c',pointRadius:4}]},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{r:{min:0,max:5,ticks:{display:false},grid:{color:'#e0dcd6'},angleLines:{color:'#e0dcd6'},pointLabels:{font:{family:'DM Sans',size:10},color:'#1c1c1c',padding:8}}}}});
    </script>
    <script>
    function resizeParent() {
      const h = document.body.scrollHeight;
      window.parent.postMessage({type:'streamlit:setFrameHeight', height: h}, '*');
    }
    window.addEventListener('load', resizeParent);
    window.addEventListener('resize', resizeParent);
    setTimeout(resizeParent, 100);
    setTimeout(resizeParent, 600);
    </script>
    """, height=670, scrolling=True)

    st.markdown("<br><br>", unsafe_allow_html=True)


# ═══════════════════════════════════════════════
# PROJETS
# ═══════════════════════════════════════════════
elif page == "Projets":

    st.markdown("""
    <div class="hero-wrap" style="padding:40px 20px 10px;">
        <div class="hero-name" style="font-size:clamp(34px,6vw,64px);">Projets</div>
        <div class="hero-subtitle">Études de cas & réalisations</div>
        <div class="hero-accent"></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    projets = [
        {"title": "Dashboard Impayés Locataires — Domofrance", "description": "Tableau de bord Power BI pour le suivi des impayés locataires. Modélisation Snowflake, pipeline Talend, 3 niveaux de granularité. Projet de bout-en-bout.", "tags": ["Power BI", "Snowflake", "Talend", "SQL"], "color": "#d95f4b"},
        {"title": "Data Mart — Projet structurant", "description": "Conception et implémentation d'un Data Mart sur Snowflake. Modélisation en étoile, documentation sur DataGalaxy, intégration dans la gouvernance des données.", "tags": ["Snowflake", "SQL", "DataGalaxy", "Modélisation"], "color": "#7a9e7e"},
        {"title": "Analyse exploratoire — Données ouvertes", "description": "Exploration d'un jeu de données public avec Python. Nettoyage, détection d'outliers, visualisation des corrélations.", "tags": ["Python", "Pandas", "Seaborn", "EDA"], "color": "#c9a84c"},
    ]

    for p in projets:
        tags_html = "".join([f'<span class="tag">{t}</span>' for t in p["tags"]])
        st.markdown(f"""
        <div class="projet-card" style="border-left-color:{p['color']};">
            <div class="projet-title">{p['title']}</div>
            <div style="font-size:14px;color:#555;line-height:1.7;">{p['description']}</div>
            <div class="projet-tags">{tags_html}</div>
        </div>
        """, unsafe_allow_html=True)

    st.info("✦ D'autres projets arrivent bientôt.")


# ═══════════════════════════════════════════════
# VOYAGES
# ═══════════════════════════════════════════════
elif page == "Voyages":

    st.markdown("""
    <div class="hero-wrap" style="padding:40px 20px 10px;">
        <div class="hero-name" style="font-size:clamp(34px,6vw,64px);">Voyages</div>
        <div class="hero-subtitle">9 pays · 4 continents · 1 curiosité constante</div>
        <div class="hero-accent"></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<p class="map-intro">Grandir en changeant de pays, c\'est apprendre à observer des systèmes très différents.</p>', unsafe_allow_html=True)

    travel = pd.DataFrame({
        "country": ["Mauritanie","Italie","Portugal","Espagne","Angleterre","Sénégal","Maroc","Malte","Thaïlande"],
        "lat":  [20.25,41.90,38.72,40.41,51.50,14.69,33.57,35.90,13.75],
        "lon":  [-10.32,12.49,-9.13,-3.70,-0.12,-17.44,-7.59,14.51,100.50],
        "note": ["Enfance · 3 ans","Voyage · Rome & Florence","Voyage · Lisbonne","Voyage · Barcelone","Voyage · Londres","Enfance · Dakar","Enfance · Casablanca","Voyage · La Valette","Voyage · Bangkok"]
    })

    fig = px.scatter_geo(travel, lat="lat", lon="lon", hover_name="country",
                         hover_data={"note":True,"lat":False,"lon":False}, projection="natural earth")
    fig.update_traces(marker=dict(size=12, color="#d95f4b", opacity=0.85, line=dict(width=1.5, color="#fff")))
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)",
        geo=dict(bgcolor="rgba(0,0,0,0)", showland=True, landcolor="#e8e4de",
                 showocean=True, oceancolor="#dce8f0", showcoastlines=True,
                 coastlinecolor="#c5bfb8", showframe=False, showcountries=True, countrycolor="#cec8c1"),
        margin=dict(t=10,b=10,l=0,r=0), height=480,
        font=dict(color="#1c1c1c", family="DM Sans"))
    st.plotly_chart(fig, use_container_width=True)


# ═══════════════════════════════════════════════
# EXPÉRIMENTATIONS
# ═══════════════════════════════════════════════
elif page == "Expérimentations":

    st.markdown("""
    <div class="hero-wrap" style="padding:40px 20px 10px;">
        <div class="hero-name" style="font-size:clamp(34px,6vw,64px);">Expérimentations</div>
        <div class="hero-subtitle">Analyses · Curiosités · Visualisations</div>
        <div class="hero-accent"></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="bio-card" style="max-width:600px;">
        <p>Cette section est un <strong>laboratoire ouvert</strong> — des analyses rapides,
        des visualisations expérimentales, des datasets trouvés par hasard.</p>
        <p style="color:#7a7a7a;font-size:13px;margin-top:12px;">
        Prochainement : analyse de mes habitudes de lecture · visualisation du coût de la vie · mini-projet NLP.</p>
    </div>
    """, unsafe_allow_html=True)
