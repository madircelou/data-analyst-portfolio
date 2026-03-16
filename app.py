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
# ─────────────────────────────────────────────
# NAVIGATION via query params
# ─────────────────────────────────────────────
nav_items = ["Accueil", "Projets", "Voyages", "Expérimentations"]
page = st.query_params.get("page", "Accueil")
if page not in nav_items:
    page = "Accueil"

# ─────────────────────────────────────────────
# STYLE GLOBAL
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;1,400&family=DM+Sans:wght@300;400;500&display=swap');

header, footer, #MainMenu { visibility: hidden; }
[data-testid="stSidebar"] { display: none; }
section[data-testid="stSidebarNav"] { display: none; }

/* remove default top padding so navbar is flush */
.block-container { padding-top: 0 !important; }

:root {
    --cream: #f4f1ed;
    --ink:   #1c1c1c;
    --muted: #7a7a7a;
    --coral: #d95f4b;
    --sage:  #7a9e7e;
    --gold:  #c9a84c;
    --white: #ffffff;
}

.stApp {
    background-color: var(--cream);
    color: var(--ink);
    font-family: 'DM Sans', sans-serif;
}

.hero-wrap {
    text-align: center;
    padding: 60px 20px 20px;
    border-bottom: 1px solid #ddd;
    margin-bottom: 50px;
}
.hero-name {
    font-family: 'Playfair Display', serif;
    font-size: clamp(52px, 8vw, 90px);
    font-weight: 700;
    letter-spacing: -0.02em;
    line-height: 1;
    color: var(--ink);
}
.hero-subtitle {
    font-size: 15px; font-weight: 300;
    letter-spacing: 0.25em; text-transform: uppercase;
    color: var(--muted); margin-top: 14px;
}
.hero-accent {
    display: inline-block;
    width: 40px; height: 3px;
    background: var(--coral);
    margin: 18px auto 0;
}

.section-label {
    font-size: 11px; font-weight: 500;
    letter-spacing: 0.3em; text-transform: uppercase;
    color: var(--coral); margin-bottom: 6px;
}
.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 30px; font-weight: 700;
    color: var(--ink); margin-bottom: 28px;
}

.bio-card {
    background: var(--white);
    border-radius: 12px;
    padding: 36px 40px;
    box-shadow: 0 2px 24px rgba(0,0,0,0.06);
    line-height: 1.85; font-size: 15px; color: #333;
}
.bio-card strong { color: var(--ink); font-weight: 500; }
.bio-highlight {
    display: inline-block;
    background: #fdf3e7; color: var(--coral);
    font-weight: 500; padding: 1px 8px; border-radius: 4px;
}

.projet-card {
    background: var(--white); border-radius: 12px;
    padding: 28px 30px;
    box-shadow: 0 2px 16px rgba(0,0,0,0.05);
    margin-bottom: 16px; border-left: 4px solid var(--coral);
}
.projet-title {
    font-family: 'Playfair Display', serif;
    font-size: 20px; font-weight: 700;
    color: var(--ink); margin-bottom: 8px;
}
.projet-tags { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 12px; }
.tag {
    font-size: 11px; font-weight: 500;
    letter-spacing: 0.08em; text-transform: uppercase;
    padding: 3px 10px; border-radius: 20px;
    background: var(--cream); color: var(--muted); border: 1px solid #ddd;
}

.map-intro {
    font-size: 15px; color: var(--muted);
    max-width: 600px; margin-bottom: 24px; line-height: 1.7;
}

/* ── MOBILE RESPONSIVE ── */
@media (max-width: 768px) {
  .block-container {
    padding-left: 0.5rem !important;
    padding-right: 0.5rem !important;
  }
  .navbar { padding: 0 16px !important; }
  .navbar-logo { font-size: 14px !important; }
  .navbar-links { gap: 16px !important; }
  .navbar-links a { font-size: 9px !important; letter-spacing: 0.1em !important; }
  .hero-wrap { padding: 40px 12px 16px !important; }
  .hero-name { font-size: clamp(36px, 10vw, 64px) !important; }
  .hero-subtitle { font-size: 11px !important; letter-spacing: 0.15em !important; }
  .bio-card { padding: 24px 20px !important; font-size: 14px !important; }
  .section-title { font-size: 24px !important; }
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# NAVBAR — un seul bloc HTML propre, pleine largeur
# ─────────────────────────────────────────────
def nav_link(label, current):
    cls = "active" if label == current else ""
    return f'<a href="?page={label}" class="{cls}">{label}</a>'

links_html = "".join(nav_link(item, page) for item in nav_items)

# Barre pleine largeur : on sort du container Streamlit avec des marges négatives
st.markdown(f"""
<style>
  /* supprime le padding top/bottom du main container */
  .block-container {{
    padding-top: 0 !important;
    padding-left: 1rem !important;
    padding-right: 1rem !important;
  }}
  .navbar {{
    background: #1c1c1c;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 48px;
    height: 56px;
    /* sort du container pour aller bord à bord */
    margin-left: calc(-1rem - 4px);
    margin-right: calc(-1rem - 4px);
    margin-top: -4px;
  }}
  .navbar-logo {{
    font-family: 'Playfair Display', serif;
    font-size: 17px; font-weight: 700;
    color: white; letter-spacing: -0.01em;
    flex-shrink: 0;
  }}
  .navbar-links {{
    display: flex; gap: 36px;
    align-items: center; height: 100%;
  }}
  .navbar-links a {{
    font-family: 'DM Sans', sans-serif;
    font-size: 11px; font-weight: 500;
    letter-spacing: 0.2em; text-transform: uppercase;
    text-decoration: none; padding: 20px 0 18px;
    color: rgba(255,255,255,0.5);
    white-space: nowrap;
    transition: color 0.15s;
  }}
  .navbar-links a:hover {{ color: white; }}
  .navbar-links a.active {{
    color: white;
    border-bottom: 2px solid #d95f4b;
  }}
</style>
<nav class="navbar">
  <span class="navbar-logo">E. Marcouire</span>
  <div class="navbar-links">
    {links_html}
  </div>
</nav>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# ACCUEIL
# ─────────────────────────────────────────────
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
      * { box-sizing: border-box; margin: 0; padding: 0; }
      body { background: #f4f1ed; }
      .tl { display: flex; overflow-x: auto; padding: 10px 4px 28px; }
      .tl-item {
        flex: 1; min-width: 150px;
        position: relative; padding: 26px 12px 16px;
      }
      .tl-item::before {
        content: ""; position: absolute;
        top: 19px; left: 0; right: 0;
        height: 2px; background: #d9d5cf;
      }
      .tl-item:first-child::before { left: 50%; }
      .tl-item:last-child::before  { right: 50%; }
      .tl-dot {
        width: 14px; height: 14px; border-radius: 50%;
        background: #d95f4b; border: 3px solid #f4f1ed;
        box-shadow: 0 0 0 2px #d95f4b;
        margin: 0 auto 16px; position: relative; z-index: 1;
      }
      .current .tl-dot { background: #7a9e7e; box-shadow: 0 0 0 2px #7a9e7e; }
      .future  .tl-dot { background: transparent; border-color: #ccc; box-shadow: 0 0 0 2px #ccc; }
      .tl-year {
        font-family: 'Playfair Display', serif;
        font-size: 19px; font-weight: 700;
        color: #1c1c1c; text-align: center; margin-bottom: 6px;
      }
      .current .tl-year { color: #7a9e7e; }
      .future  .tl-year { color: #7a7a7a; font-style: italic; }
      .tl-role {
        font-family: 'DM Sans', sans-serif;
        font-size: 12px; font-weight: 500;
        color: #1c1c1c; text-align: center; margin-bottom: 4px;
      }
      .tl-detail {
        font-family: 'DM Sans', sans-serif;
        font-size: 11px; color: #7a7a7a;
        text-align: center; line-height: 1.55;
      }
    </style>
    <div class="tl">
      <div class="tl-item">
        <div class="tl-dot"></div>
        <div class="tl-year">2002–18</div>
        <div class="tl-role">Maroc · Mauritanie · Sénégal</div>
        <div class="tl-detail">Grandir entre cultures,<br>lire les contextes</div>
      </div>
      <div class="tl-item">
        <div class="tl-dot"></div>
        <div class="tl-year">2020</div>
        <div class="tl-role">Bac ES</div>
        <div class="tl-detail">Spécialité Mathématiques<br>Mention Bien</div>
      </div>
      <div class="tl-item">
        <div class="tl-dot"></div>
        <div class="tl-year">2020</div>
        <div class="tl-role">Bordeaux</div>
        <div class="tl-detail">Licence MIASHS<br>Université de Bordeaux</div>
      </div>
      <div class="tl-item">
        <div class="tl-dot"></div>
        <div class="tl-year">2023</div>
        <div class="tl-role">Premiers dashboards</div>
        <div class="tl-detail">Power BI · SQL · Python<br>La donnée comme langage</div>
      </div>
      <div class="tl-item current">
        <div class="tl-dot"></div>
        <div class="tl-year">2024 →</div>
        <div class="tl-role">Alternante Data Analyst</div>
        <div class="tl-detail">Domofrance<br>Snowflake · Talend · DataGalaxy</div>
      </div>
      <div class="tl-item future">
        <div class="tl-dot"></div>
        <div class="tl-year">2026+</div>
        <div class="tl-role">What's next?</div>
        <div class="tl-detail">La suite est<br>encore à écrire ✦</div>
      </div>
    </div>
    """, height=175)

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
            <p style="margin-top:16px;">Aujourd'hui <strong>alternante Data Analyst chez Domofrance</strong>,
            je travaille au quotidien avec <span class="bio-highlight">Power BI · Snowflake · Talend</span>
            pour transformer des données brutes en tableaux de bord actionnables.
            J'interviens sur toute la chaîne : collecte, modélisation, visualisation et documentation.</p>
            <p style="margin-top:16px;">Ce qui me motive ? Ce moment un peu magique où un dataset chaotique
            révèle soudainement un pattern — parce que la donnée, c'est d'abord une <strong>histoire à raconter</strong>.</p>
        </div>
        """, unsafe_allow_html=True)

    with col_radar:
        st.markdown('<div class="section-label">Compétences</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Stack</div>', unsafe_allow_html=True)

        # Deux radars Chart.js côte à côte dans un seul composant = zéro problème de layout
        components.html("""
        <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500&display=swap" rel="stylesheet">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
        <style>
          * { box-sizing: border-box; margin:0; padding:0; }
          html, body { background: #f4f1ed; font-family: 'DM Sans', sans-serif; }
          .wrap { display: flex; gap: 8px; width: 100%; }
          .chart-box { flex: 1; text-align: center; }
          .chart-label {
            font-size: 10px; font-weight: 500;
            letter-spacing: 0.18em; text-transform: uppercase;
            color: #7a7a7a; margin-bottom: 6px;
          }
          .canvas-wrap {
            position: relative;
            width: 100%;
            height: 280px;
          }
        </style>
        <div class="wrap">
          <div class="chart-box">
            <div class="chart-label">Langages</div>
            <div class="canvas-wrap"><canvas id="r1"></canvas></div>
          </div>
          <div class="chart-box">
            <div class="chart-label">Outils métier</div>
            <div class="canvas-wrap"><canvas id="r2"></canvas></div>
          </div>
        </div>
        <script>
          const radarOpts = {
            type: 'radar',
            options: {
              responsive: true,
              maintainAspectRatio: false,
              plugins: { legend: { display: false } },
              scales: {
                r: {
                  min: 0, max: 4,
                  ticks: { display: false, stepSize: 1 },
                  grid: { color: '#e0dcd6' },
                  angleLines: { color: '#e0dcd6' },
                  pointLabels: {
                    font: { family: 'DM Sans', size: 12 },
                    color: '#1c1c1c',
                    padding: 12
                  }
                }
              }
            }
          };

          new Chart(document.getElementById('r1'), {
            ...radarOpts,
            data: {
              labels: ['Python', 'SQL', 'Excel', 'R'],
              datasets: [{
                data: [3, 4, 3, 2],
                backgroundColor: 'rgba(217,95,75,0.2)',
                borderColor: '#d95f4b',
                borderWidth: 2,
                pointBackgroundColor: '#d95f4b',
                pointRadius: 3
              }]
            }
          });

          new Chart(document.getElementById('r2'), {
            ...radarOpts,
            data: {
              labels: ['Snowflake','Talend','Power BI','DataGalaxy','Confluence'],
              datasets: [{
                data: [3, 3, 4, 2, 2],
                backgroundColor: 'rgba(122,158,126,0.2)',
                borderColor: '#7a9e7e',
                borderWidth: 2,
                pointBackgroundColor: '#7a9e7e',
                pointRadius: 3
              }]
            }
          });
        </script>
        """, height=320)

    # ── MINI DASHBOARD ────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-label">Mon tableau de bord</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">En chiffres</div>', unsafe_allow_html=True)

    components.html("""
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
    <style>
      * { box-sizing:border-box; margin:0; padding:0; }
      html,body { background:#f4f1ed; font-family:'DM Sans',sans-serif; }

      .db-wrap { border-radius:12px; overflow:hidden; box-shadow:0 4px 28px rgba(0,0,0,0.1); }

      /* Header */
      .db-header {
        background:#1c1c1c; padding:14px 22px;
        display:flex; align-items:center; justify-content:space-between;
      }
      .db-title { font-family:'Playfair Display',serif; font-size:15px; font-weight:700; color:white; }
      .db-badge {
        font-size:9px; font-weight:500; letter-spacing:0.15em; text-transform:uppercase;
        background:rgba(217,95,75,0.25); color:#d95f4b;
        padding:4px 10px; border-radius:20px; border:1px solid rgba(217,95,75,0.4);
      }

      /* KPI strip */
      .kpi-strip {
        display:grid; grid-template-columns:repeat(4,1fr);
        gap:1px; background:#e0dcd6;
        border-left:1px solid #e0dcd6; border-right:1px solid #e0dcd6;
      }
      .kpi { background:#fff; padding:14px 16px; }
      .kpi-label {
        font-size:9px; font-weight:500; letter-spacing:0.18em; text-transform:uppercase;
        color:#7a7a7a; margin-bottom:6px;
      }
      .kpi-value {
        font-family:'Playfair Display',serif; font-size:26px; font-weight:700;
        color:#1c1c1c; line-height:1; margin-bottom:4px;
      }
      .kpi-delta { font-size:10px; font-weight:500; }
      .kpi-delta.up   { color:#d95f4b; }
      .kpi-delta.down { color:#7a9e7e; }
      .kpi-delta.neu  { color:#7a7a7a; }
      .kpi-ref { font-size:9px; color:#bbb; margin-left:4px; }

      /* Charts grid */
      .charts-grid {
        display:grid; grid-template-columns:5fr 7fr;
        gap:1px; background:#e0dcd6;
        border:1px solid #e0dcd6; border-top:1px solid #e0dcd6;
      }
      .chart-panel { background:#fff; padding:16px 16px 12px; }
      .panel-title {
        font-size:10px; font-weight:500; letter-spacing:0.12em; text-transform:uppercase;
        color:#7a7a7a; margin-bottom:12px;
      }
      .canvas-h { position:relative; width:100%; height:200px; }

      /* Legend row */
      .legend-row {
        background:#fff; border:1px solid #e0dcd6; border-top:none;
        padding:8px 16px; display:flex; gap:16px; flex-wrap:wrap; align-items:center;
      }
      .leg-item { display:flex; align-items:center; gap:5px; font-size:9px; color:#555; }
      .leg-dot  { width:10px; height:10px; border-radius:2px; flex-shrink:0; }

      /* Footer */
      .db-footer {
        background:#fff; border:1px solid #e0dcd6; border-top:none;
        border-radius:0 0 12px 12px; padding:8px 16px;
        display:flex; justify-content:space-between;
        font-size:9px; color:#bbb; letter-spacing:0.05em;
      }

      @media(max-width:560px) {
        .kpi-strip   { grid-template-columns:repeat(2,1fr); }
        .charts-grid { grid-template-columns:1fr; }
        .kpi-value   { font-size:20px; }
      }
    </style>

    <div class="db-wrap">

      <!-- Header -->
      <div class="db-header">
        <span class="db-title">Tableau de bord · E. Marcouire</span>
        <span class="db-badge">Portfolio Data Analyst</span>
      </div>

      <!-- KPIs -->
      <div class="kpi-strip">
        <div class="kpi">
          <div class="kpi-label">Expérience data</div>
          <div class="kpi-value">4 ans</div>
          <div class="kpi-delta neu">depuis 2020 <span class="kpi-ref">(M-1: 3 ans)</span></div>
        </div>
        <div class="kpi">
          <div class="kpi-label">Dashboards livrés</div>
          <div class="kpi-value">15 +</div>
          <div class="kpi-delta down">↑ +3 cette année <span class="kpi-ref">vs N-1</span></div>
        </div>
        <div class="kpi">
          <div class="kpi-label">Datasets explorés</div>
          <div class="kpi-value">20 +</div>
          <div class="kpi-delta down">dont 8 en prod <span class="kpi-ref">↑ +2</span></div>
        </div>
        <div class="kpi">
          <div class="kpi-label">Pays visités</div>
          <div class="kpi-value">9</div>
          <div class="kpi-delta up">↗ prochain : TBD <span class="kpi-ref"></span></div>
        </div>
      </div>

      <!-- Charts -->
      <div class="charts-grid">

        <!-- Horizontal bar : répartition compétences -->
        <div class="chart-panel">
          <div class="panel-title">Répartition compétences · niveau /10</div>
          <div class="canvas-h"><canvas id="hbar"></canvas></div>
        </div>

        <!-- Stacked bar + line : projets dans le temps -->
        <div class="chart-panel">
          <div class="panel-title">Dashboards livrés par trimestre · avec taux de complexité</div>
          <div class="canvas-h"><canvas id="stacked"></canvas></div>
        </div>

      </div>

      <!-- Legend -->
      <div class="legend-row">
        <div class="leg-item"><div class="leg-dot" style="background:#d95f4b;"></div>SQL / Power BI (core)</div>
        <div class="leg-item"><div class="leg-dot" style="background:#7a9e7e;"></div>Snowflake / Talend</div>
        <div class="leg-item"><div class="leg-dot" style="background:#c9a84c;"></div>Python / Excel</div>
        <div class="leg-item"><div class="leg-dot" style="background:#9b8fcf;"></div>R / Autres</div>
        <div class="leg-item"><div class="leg-dot" style="background:none;border:2px solid #d95f4b;border-radius:50%;"></div>— Taux complexité</div>
      </div>

      <!-- Footer -->
      <div class="db-footer">
        <span>Domofrance · Bordeaux · Snowflake · Power BI · Python · SQL</span>
        <span>Données indicatives &nbsp;·&nbsp; 16/03/2026</span>
      </div>

    </div>

    <script>
    // Horizontal bar — compétences
    new Chart(document.getElementById('hbar'), {
      type: 'bar',
      data: {
        labels: ['SQL','Power BI','Python','Snowflake','Excel','Talend','R'],
        datasets: [{
          data: [8.5, 8, 7, 7, 7, 6.5, 5],
          backgroundColor: ['#d95f4b','#d95f4b','#c9a84c','#7a9e7e','#c9a84c','#7a9e7e','#9b8fcf'],
          borderRadius: 4,
          borderSkipped: false
        }]
      },
      options: {
        indexAxis: 'y',
        responsive: true, maintainAspectRatio: false,
        plugins: { legend: { display: false } },
        scales: {
          x: { min:0, max:10, grid:{color:'#f4f1ed'}, ticks:{font:{size:9},color:'#aaa',stepSize:2} },
          y: { grid:{display:false}, ticks:{font:{family:'DM Sans',size:10},color:'#333'} }
        }
      }
    });

    // Stacked bar + line — projets par trimestre
    const labels = ['T1 23','T2 23','T3 23','T4 23','T1 24','T2 24','T3 24','T4 24','T1 25'];
    const simple  = [1,1,1,2,2,2,2,2,2];
    const moyen   = [0,0,1,0,1,1,1,1,1];
    const complexe= [0,0,0,0,0,1,0,1,0];
    const total   = labels.map((_,i) => simple[i]+moyen[i]+complexe[i]);
    const taux    = total.map(v => Math.round((v / 4) * 100)); // % fictif complexité

    new Chart(document.getElementById('stacked'), {
      data: {
        labels,
        datasets: [
          {
            type:'bar', label:'Simple',
            data: simple,
            backgroundColor:'#d95f4b', stack:'s', borderRadius:2
          },
          {
            type:'bar', label:'Moyen',
            data: moyen,
            backgroundColor:'#c9a84c', stack:'s', borderRadius:2
          },
          {
            type:'bar', label:'Complexe',
            data: complexe,
            backgroundColor:'#7a9e7e', stack:'s', borderRadius:2
          },
          {
            type:'line', label:'Taux complexité',
            data: taux,
            borderColor:'#d95f4b', borderWidth:2,
            pointBackgroundColor:'#d95f4b', pointRadius:4,
            tension:0.3, yAxisID:'y2', fill:false
          }
        ]
      },
      options: {
        responsive:true, maintainAspectRatio:false,
        plugins:{ legend:{display:false} },
        scales:{
          x:{ stacked:true, grid:{display:false}, ticks:{font:{size:9},color:'#888'} },
          y:{
            stacked:true, position:'left',
            min:0, max:5,
            grid:{color:'#f4f1ed'},
            ticks:{font:{size:9},color:'#aaa',stepSize:1}
          },
          y2:{
            position:'right', min:0, max:100,
            grid:{display:false},
            ticks:{
              font:{size:9},color:'#d95f4b',
              callback: v => v + ' %'
            }
          }
        }
      }
    });
    </script>
    """, height=520)

    st.markdown("<br><br>", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# PROJETS
# ─────────────────────────────────────────────
elif page == "Projets":

    st.markdown("""
    <div class="hero-wrap" style="padding:40px 20px 10px;">
        <div class="hero-name" style="font-size:clamp(36px,6vw,64px);">Projets</div>
        <div class="hero-subtitle">Études de cas & réalisations</div>
        <div class="hero-accent"></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    projets = [
        {
            "title": "Dashboard Locataires — Domofrance",
            "description": "Tableau de bord Power BI pour le suivi des indicateurs de satisfaction et d'occupation du parc immobilier. Connexion Snowflake, rafraîchissement automatique, 3 niveaux de granularité.",
            "tags": ["Power BI", "Snowflake", "SQL", "Alternance"],
            "color": "#d95f4b"
        },
        {
            "title": "Analyse exploratoire — Données ouvertes",
            "description": "Exploration d'un jeu de données public avec Python (pandas, seaborn). Nettoyage, détection d'outliers, visualisation des corrélations et synthèse des insights.",
            "tags": ["Python", "Pandas", "Seaborn", "EDA"],
            "color": "#7a9e7e"
        },
        {
            "title": "Pipeline de données — Projet universitaire",
            "description": "Conception d'un pipeline ETL en R pour agréger et nettoyer des sources hétérogènes. Modélisation relationnelle et rapport automatisé en RMarkdown.",
            "tags": ["R", "ETL", "MIASHS", "RMarkdown"],
            "color": "#c9a84c"
        },
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

    st.markdown("<br>", unsafe_allow_html=True)
    st.info("✦ D'autres projets arrivent bientôt — en cours de documentation.")

# ─────────────────────────────────────────────
# VOYAGES
# ─────────────────────────────────────────────
elif page == "Voyages":

    st.markdown("""
    <div class="hero-wrap" style="padding:40px 20px 10px;">
        <div class="hero-name" style="font-size:clamp(36px,6vw,64px);">Voyages</div>
        <div class="hero-subtitle">9 pays · 4 continents · 1 curiosité constante</div>
        <div class="hero-accent"></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <p class="map-intro">Grandir en changeant de pays, c'est apprendre à observer des systèmes très différents.
    Voici la carte de mes escales — certaines pour l'enfance, d'autres pour la curiosité.</p>
    """, unsafe_allow_html=True)

    travel = pd.DataFrame({
        "country": ["Mauritanie","Italie","Portugal","Espagne","Angleterre","Sénégal","Maroc","Malte","Thaïlande"],
        "lat":  [20.25, 41.90, 38.72, 40.41, 51.50, 14.69, 33.57, 35.90, 13.75],
        "lon":  [-10.32, 12.49, -9.13, -3.70, -0.12, -17.44, -7.59, 14.51, 100.50],
        "note": [
            "Enfance · 3 ans sur place","Voyage · Rome & Florence","Voyage · Lisbonne",
            "Voyage · Barcelone & Madrid","Voyage · Londres","Enfance · Dakar",
            "Enfance · Casablanca & Rabat","Voyage · La Valette","Voyage · Bangkok & Chiang Mai"
        ]
    })

    fig = px.scatter_geo(
        travel, lat="lat", lon="lon",
        hover_name="country",
        hover_data={"note": True, "lat": False, "lon": False},
        projection="natural earth"
    )
    fig.update_traces(marker=dict(size=12, color="#d95f4b", opacity=0.85, line=dict(width=1.5, color="#fff")))
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        geo=dict(
            bgcolor="rgba(0,0,0,0)",
            showland=True, landcolor="#e8e4de",
            showocean=True, oceancolor="#dce8f0",
            showcoastlines=True, coastlinecolor="#c5bfb8",
            showframe=False, showcountries=True, countrycolor="#cec8c1",
        ),
        margin=dict(t=10, b=10, l=0, r=0),
        height=520,
        font=dict(color="#1c1c1c", family="DM Sans")
    )
    st.plotly_chart(fig, use_container_width=True)

    chips = " &nbsp;·&nbsp; ".join(travel["country"].tolist())
    st.markdown(f'<p style="color:#7a7a7a;font-size:14px;">{chips}</p>', unsafe_allow_html=True)

# ─────────────────────────────────────────────
# EXPERIMENTATIONS
# ─────────────────────────────────────────────
elif page == "Expérimentations":

    st.markdown("""
    <div class="hero-wrap" style="padding:40px 20px 10px;">
        <div class="hero-name" style="font-size:clamp(36px,6vw,64px);">Expérimentations</div>
        <div class="hero-subtitle">Analyses · Curiosités · Visualisations</div>
        <div class="hero-accent"></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="bio-card" style="max-width:600px;">
        <p>Cette section est un <strong>laboratoire ouvert</strong> — des analyses rapides,
        des visualisations expérimentales, des datasets trouvés par hasard et trop intéressants
        pour ne pas être explorés.</p>
        <p style="color:#7a7a7a;font-size:13px;margin-top:12px;">
        Prochainement : analyse de mes habitudes de lecture · visualisation du coût de la vie entre mes villes · mini-projet NLP.</p>
    </div>
    """, unsafe_allow_html=True)
