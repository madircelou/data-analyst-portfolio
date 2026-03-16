import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Elodie Marcouire | Portfolio",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─────────────────────────────────────────────
# STYLE GLOBAL
# ─────────────────────────────────────────────

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;1,400&family=DM+Sans:wght@300;400;500&display=swap');

header {visibility:hidden;}
footer {visibility:hidden;}
#MainMenu {visibility:hidden;}

:root {
    --cream:   #f4f1ed;
    --ink:     #1c1c1c;
    --muted:   #7a7a7a;
    --coral:   #d95f4b;
    --sage:    #7a9e7e;
    --gold:    #c9a84c;
    --white:   #ffffff;
}

.stApp {
    background-color: var(--cream);
    color: var(--ink);
    font-family: 'DM Sans', sans-serif;
}

[data-testid="stSidebar"] {
    background-color: var(--ink) !important;
}
[data-testid="stSidebar"] * {
    color: var(--white) !important;
}
[data-testid="stSidebar"] .stRadio label {
    font-family: 'DM Sans', sans-serif;
    font-size: 15px;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    padding: 6px 0;
}

.hero-wrap {
    text-align: center;
    padding: 60px 20px 10px;
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
    font-family: 'DM Sans', sans-serif;
    font-size: 16px;
    font-weight: 300;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    color: var(--muted);
    margin-top: 12px;
}
.hero-accent {
    display: inline-block;
    width: 40px;
    height: 3px;
    background: var(--coral);
    margin: 18px auto 0;
}

.section-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    color: var(--coral);
    margin-bottom: 8px;
}
.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 32px;
    font-weight: 700;
    color: var(--ink);
    margin-bottom: 30px;
}

.bio-card {
    background: var(--white);
    border-radius: 12px;
    padding: 36px 40px;
    box-shadow: 0 2px 24px rgba(0,0,0,0.06);
    line-height: 1.85;
    font-size: 15px;
    color: #333;
}
.bio-card strong { color: var(--ink); font-weight: 500; }
.bio-highlight {
    display: inline-block;
    background: #fdf3e7;
    color: var(--coral);
    font-weight: 500;
    padding: 1px 8px;
    border-radius: 4px;
}

.radar-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 11px;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--muted);
    text-align: center;
    margin-bottom: 4px;
}

.stat-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
    margin-top: 10px;
}
.stat-card {
    background: var(--white);
    border-radius: 12px;
    padding: 28px 20px;
    text-align: center;
    box-shadow: 0 2px 12px rgba(0,0,0,0.05);
    border-top: 3px solid var(--coral);
}
.stat-number {
    font-family: 'Playfair Display', serif;
    font-size: 42px;
    font-weight: 700;
    color: var(--ink);
    line-height: 1;
    margin-bottom: 8px;
}
.stat-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 12px;
    font-weight: 400;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--muted);
}
.stat-card:nth-child(2) { border-color: var(--sage); }
.stat-card:nth-child(3) { border-color: var(--gold); }
.stat-card:nth-child(4) { border-color: #9b8fcf; }

.projet-card {
    background: var(--white);
    border-radius: 12px;
    padding: 28px 30px;
    box-shadow: 0 2px 16px rgba(0,0,0,0.05);
    margin-bottom: 16px;
    border-left: 4px solid var(--coral);
}
.projet-title {
    font-family: 'Playfair Display', serif;
    font-size: 20px;
    font-weight: 700;
    color: var(--ink);
    margin-bottom: 8px;
}
.projet-tags { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 12px; }
.tag {
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    padding: 3px 10px;
    border-radius: 20px;
    background: var(--cream);
    color: var(--muted);
    border: 1px solid #ddd;
}

.map-intro {
    font-family: 'DM Sans', sans-serif;
    font-size: 15px;
    color: var(--muted);
    max-width: 600px;
    margin-bottom: 24px;
    line-height: 1.7;
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# NAVIGATION
# ─────────────────────────────────────────────

page = st.sidebar.radio(
    "Navigation",
    ["Accueil", "Projets", "Voyages", "Expérimentations"]
)

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
      .tl {
        display: flex;
        overflow-x: auto;
        padding: 10px 4px 28px;
      }
      .tl-item {
        flex: 1;
        min-width: 155px;
        position: relative;
        padding: 26px 12px 16px;
      }
      .tl-item::before {
        content: "";
        position: absolute;
        top: 19px; left: 0; right: 0;
        height: 2px;
        background: #d9d5cf;
      }
      .tl-item:first-child::before { left: 50%; }
      .tl-item:last-child::before  { right: 50%; }
      .tl-dot {
        width: 14px; height: 14px;
        border-radius: 50%;
        background: #d95f4b;
        border: 3px solid #f4f1ed;
        box-shadow: 0 0 0 2px #d95f4b;
        margin: 0 auto 16px;
        position: relative;
        z-index: 1;
      }
      .tl-item.current .tl-dot { background: #7a9e7e; box-shadow: 0 0 0 2px #7a9e7e; }
      .tl-item.future  .tl-dot { background: transparent; border-color: #ccc; box-shadow: 0 0 0 2px #ccc; }
      .tl-year {
        font-family: 'Playfair Display', serif;
        font-size: 20px; font-weight: 700;
        color: #1c1c1c;
        text-align: center; margin-bottom: 6px;
      }
      .tl-item.current .tl-year { color: #7a9e7e; }
      .tl-item.future  .tl-year { color: #7a7a7a; font-style: italic; }
      .tl-role {
        font-family: 'DM Sans', sans-serif;
        font-size: 12px; font-weight: 500;
        color: #1c1c1c;
        text-align: center; margin-bottom: 4px;
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
    # Layout : bio à gauche (col large), radars côte à côte à droite
    col_bio, col_radar = st.columns([3, 2], gap="large")

    with col_bio:
        st.markdown('<div class="section-label">À propos</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Qui suis-je ?</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="bio-card">
            <p>
                J'ai grandi entre le <strong>Maroc, la Mauritanie et le Sénégal</strong>
                avant de poser mes valises à Bordeaux pour ma licence
                <span class="bio-highlight">MIASHS</span>.
                Cette enfance nomade m'a appris une chose essentielle :
                comprendre rapidement un contexte inconnu — une compétence
                précieuse quand on explore un nouveau dataset.
            </p>
            <p>
                Aujourd'hui <strong>alternante Data Analyst chez Domofrance</strong>,
                je travaille au quotidien avec <span class="bio-highlight">Power BI · Snowflake · Talend</span>
                pour transformer des données brutes en tableaux de bord actionnables.
                J'interviens sur toute la chaîne : collecte, modélisation, visualisation et documentation.
            </p>
            <p>
                Ce qui me motive ? Ce moment un peu magique où un dataset chaotique
                révèle soudainement un pattern. Je construis ce portfolio pour raconter
                cette aventure — parce que la donnée, c'est d'abord une <strong>histoire à raconter</strong>.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col_radar:
        st.markdown('<div class="section-label">Compétences</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Stack</div>', unsafe_allow_html=True)

        # ── Les deux radars côte à côte dans des sous-colonnes ──
        r_col1, r_col2 = st.columns(2)

        RADAR_LAYOUT = dict(
            showlegend=False,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            margin=dict(t=30, b=10, l=10, r=10),
            height=260,
            font=dict(color="#1c1c1c", family="DM Sans"),
            polar=dict(
                bgcolor="rgba(0,0,0,0)",
                radialaxis=dict(
                    range=[0, 4],
                    tickfont=dict(color="#7a7a7a", size=9),
                    gridcolor="#e0dcd6",
                    linecolor="#e0dcd6",
                    showticklabels=False,
                ),
                angularaxis=dict(
                    tickfont=dict(color="#1c1c1c", size=11),
                    linecolor="#e0dcd6",
                    gridcolor="#e0dcd6",
                )
            )
        )

        with r_col1:
            st.markdown('<div class="radar-label">Langages</div>', unsafe_allow_html=True)
            data_analysis = pd.DataFrame({
                "tool": ["Python", "SQL", "Excel", "R"],
                "score": [3, 4, 3, 2]
            })
            fig1 = px.line_polar(data_analysis, r="score", theta="tool", line_close=True)
            fig1.update_traces(
                fill='toself',
                line_color="#d95f4b",
                fillcolor="rgba(217,95,75,0.25)"
            )
            fig1.update_layout(**RADAR_LAYOUT)
            st.plotly_chart(fig1, use_container_width=True)

        with r_col2:
            st.markdown('<div class="radar-label">Outils métier</div>', unsafe_allow_html=True)
            stack = pd.DataFrame({
                "tool": ["Snowflake", "Talend", "Power BI", "DataGalaxy", "Confluence"],
                "score": [3, 3, 4, 2, 2]
            })
            fig2 = px.line_polar(stack, r="score", theta="tool", line_close=True)
            fig2.update_traces(
                fill='toself',
                line_color="#7a9e7e",
                fillcolor="rgba(122,158,126,0.25)"
            )
            fig2.update_layout(**RADAR_LAYOUT)
            st.plotly_chart(fig2, use_container_width=True)

    # ── STATS ─────────────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-label">En chiffres</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Ce que disent les données</div>', unsafe_allow_html=True)

    components.html("""
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=DM+Sans:wght@400&display=swap" rel="stylesheet">
    <style>
      * { box-sizing: border-box; margin:0; padding:0; }
      body { background: transparent; }
      .grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 16px;
      }
      .card {
        background: #fff;
        border-radius: 12px;
        padding: 28px 16px;
        text-align: center;
        box-shadow: 0 2px 12px rgba(0,0,0,0.05);
        border-top: 3px solid #d95f4b;
      }
      .card:nth-child(2) { border-color: #7a9e7e; }
      .card:nth-child(3) { border-color: #c9a84c; }
      .card:nth-child(4) { border-color: #9b8fcf; }
      .num {
        font-family: 'Playfair Display', serif;
        font-size: 44px; font-weight: 700;
        color: #1c1c1c; line-height: 1;
        margin-bottom: 10px;
      }
      .lbl {
        font-family: 'DM Sans', sans-serif;
        font-size: 11px; font-weight: 400;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        color: #7a7a7a;
      }
    </style>
    <div class="grid">
      <div class="card"><div class="num">4</div><div class="lbl">Années dans la data</div></div>
      <div class="card"><div class="num">15+</div><div class="lbl">Dashboards réalisés</div></div>
      <div class="card"><div class="num">20+</div><div class="lbl">Datasets explorés</div></div>
      <div class="card"><div class="num">9</div><div class="lbl">Pays visités</div></div>
    </div>
    """, height=140)

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
    <p class="map-intro">
        Grandir en changeant de pays, c'est apprendre à observer des systèmes très différents.
        Voici la carte de mes escales — certaines pour l'enfance, d'autres pour la curiosité.
    </p>
    """, unsafe_allow_html=True)

    travel = pd.DataFrame({
        "country": ["Mauritanie","Italie","Portugal","Espagne","Angleterre","Sénégal","Maroc","Malte","Thaïlande"],
        "lat":  [20.25, 41.90, 38.72, 40.41, 51.50, 14.69, 33.57, 35.90, 13.75],
        "lon":  [-10.32, 12.49, -9.13, -3.70, -0.12, -17.44, -7.59, 14.51, 100.50],
        "note": [
            "Enfance · 3 ans sur place",
            "Voyage · Rome & Florence",
            "Voyage · Lisbonne",
            "Voyage · Barcelone & Madrid",
            "Voyage · Londres",
            "Enfance · Dakar",
            "Enfance · Casablanca & Rabat",
            "Voyage · La Valette",
            "Voyage · Bangkok & Chiang Mai"
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
            showframe=False,
            showcountries=True, countrycolor="#cec8c1",
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
        <p>
            Cette section est un <strong>laboratoire ouvert</strong> — des analyses rapides,
            des visualisations expérimentales, des datasets trouvés par hasard et trop intéressants
            pour ne pas être explorés.
        </p>
        <p style="color:#7a7a7a;font-size:13px;margin-top:12px;">
            Prochainement : analyse de mes habitudes de lecture · visualisation du coût de la vie entre mes villes · mini-projet NLP.
        </p>
    </div>
    """, unsafe_allow_html=True)
