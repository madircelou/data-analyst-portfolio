import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Maroc 2025 · Elodie",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ─────────────────────────────────────────────
# STYLE — cohérent avec app.py
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;1,400&family=DM+Sans:wght@300;400;500&display=swap');

header { visibility:hidden; }
footer { visibility:hidden; }
#MainMenu { visibility:hidden; }
[data-testid="stSidebar"] { display:none; }

:root {
    --cream: #f4f1ed;
    --ink:   #1c1c1c;
    --muted: #7a7a7a;
    --coral: #d95f4b;
    --sage:  #7a9e7e;
    --gold:  #c9a84c;
    --white: #ffffff;
    --sand:  #e8dcc8;
}
.stApp { background-color:var(--cream); color:var(--ink); font-family:'DM Sans',sans-serif; }

.hero-wrap { text-align:center; padding:56px 20px 20px; border-bottom:1px solid #ddd; margin-bottom:40px; }
.hero-name { font-family:'Playfair Display',serif; font-size:clamp(36px,6vw,72px); font-weight:700; letter-spacing:-0.02em; line-height:1; color:var(--ink); }
.hero-subtitle { font-size:14px; font-weight:300; letter-spacing:0.25em; text-transform:uppercase; color:var(--muted); margin-top:12px; }
.hero-accent { display:inline-block; width:40px; height:3px; background:var(--gold); margin:16px auto 0; }

.section-label { font-size:11px; font-weight:500; letter-spacing:0.3em; text-transform:uppercase; color:var(--coral); margin-bottom:6px; }
.section-title { font-family:'Playfair Display',serif; font-size:clamp(20px,4vw,28px); font-weight:700; color:var(--ink); margin-bottom:20px; }

.card { background:var(--white); border-radius:12px; padding:24px 28px; box-shadow:0 2px 16px rgba(0,0,0,0.06); margin-bottom:16px; }

/* KPI strip */
.kpi-strip { display:grid; grid-template-columns:repeat(4,1fr); gap:1px; background:#e0dcd6; border:1px solid #e0dcd6; border-radius:12px; overflow:hidden; margin-bottom:32px; }
.kpi-cell { background:#fff; padding:18px 16px; }
.kpi-lbl { font-size:9px; font-weight:500; letter-spacing:0.18em; text-transform:uppercase; color:#7a7a7a; margin-bottom:6px; }
.kpi-val { font-family:'Playfair Display',serif; font-size:26px; font-weight:700; color:var(--ink); line-height:1; margin-bottom:3px; }
.kpi-sub { font-size:10px; color:#7a7a7a; }

/* Étapes itinéraire */
.itin-item { display:flex; gap:16px; margin-bottom:0; }
.itin-line { display:flex; flex-direction:column; align-items:center; flex-shrink:0; }
.itin-dot { width:14px; height:14px; border-radius:50%; background:var(--gold); border:3px solid var(--cream); box-shadow:0 0 0 2px var(--gold); flex-shrink:0; }
.itin-vline { width:2px; flex:1; background:#e0dcd6; margin:4px 0; min-height:30px; }
.itin-content { padding-bottom:24px; flex:1; }
.itin-days { font-size:10px; font-weight:500; letter-spacing:0.15em; text-transform:uppercase; color:var(--coral); margin-bottom:3px; }
.itin-city { font-family:'Playfair Display',serif; font-size:18px; font-weight:700; color:var(--ink); margin-bottom:4px; }
.itin-desc { font-size:13px; color:#666; line-height:1.6; }
.itin-tags { display:flex; gap:6px; flex-wrap:wrap; margin-top:8px; }
.itin-tag { font-size:10px; padding:2px 8px; border-radius:12px; background:var(--cream); border:1px solid #ddd; color:var(--muted); }

/* Budget table */
.budget-row { display:flex; justify-content:space-between; align-items:center; padding:10px 0; border-bottom:1px solid #f4f1ed; font-size:14px; }
.budget-row:last-child { border-bottom:none; font-weight:500; }
.budget-cat { color:var(--ink); }
.budget-amt { font-family:'Playfair Display',serif; font-size:16px; font-weight:700; color:var(--ink); }
.budget-bar { height:6px; border-radius:3px; margin-top:4px; }

@media(max-width:600px){
  .kpi-strip { grid-template-columns:repeat(2,1fr); }
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# BACK LINK
# ─────────────────────────────────────────────
st.markdown("""
<a href="/" style="font-family:DM Sans,sans-serif;font-size:12px;font-weight:500;
letter-spacing:0.1em;text-transform:uppercase;text-decoration:none;
color:rgba(28,28,28,0.45);display:inline-flex;align-items:center;gap:6px;
margin-bottom:0;padding:16px 0 0 8px;">
  ← Retour au portfolio
</a>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# HERO
# ─────────────────────────────────────────────
st.markdown("""
<div class="hero-wrap">
  <div class="hero-name">🇲🇦 Maroc 2025</div>
  <div class="hero-subtitle">Projet voyage · analyse & planification data</div>
  <div class="hero-accent"></div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# KPIs
# ─────────────────────────────────────────────
st.markdown("""
<div class="kpi-strip">
  <div class="kpi-cell">
    <div class="kpi-lbl">Durée</div>
    <div class="kpi-val">10 j</div>
    <div class="kpi-sub">juillet 2025</div>
  </div>
  <div class="kpi-cell">
    <div class="kpi-lbl">Villes</div>
    <div class="kpi-val">4</div>
    <div class="kpi-sub">Marrakech · Essaouira · Fès · Chefchaouen</div>
  </div>
  <div class="kpi-cell">
    <div class="kpi-lbl">Budget total</div>
    <div class="kpi-val">1 400 €</div>
    <div class="kpi-sub">~140 € / jour</div>
  </div>
  <div class="kpi-cell">
    <div class="kpi-lbl">Km parcourus</div>
    <div class="kpi-val">~1 100</div>
    <div class="kpi-sub">Bordeaux → Marrakech → Fès → CDG</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# CARTE + ITINÉRAIRE
# ─────────────────────────────────────────────
col_map, col_itin = st.columns([3, 2], gap="large")

with col_map:
    st.markdown('<div class="section-label">Géographie</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">L\'itinéraire sur la carte</div>', unsafe_allow_html=True)

    villes = pd.DataFrame({
        "ville":  ["Bordeaux (départ)", "Marrakech", "Essaouira", "Fès", "Chefchaouen"],
        "lat":    [44.84, 31.63, 31.51, 34.03, 35.17],
        "lon":    [-0.58, -7.99, -9.77, -5.00, -5.27],
        "jours":  [0, 4, 2, 2, 2],
        "ordre":  [0, 1, 2, 3, 4],
        "type":   ["Départ", "Étape", "Étape", "Étape", "Étape"],
    })

    fig = go.Figure()

    # Ligne de trajet
    fig.add_trace(go.Scattergeo(
        lat=villes["lat"], lon=villes["lon"],
        mode="lines",
        line=dict(width=2, color="#c9a84c", dash="dot"),
        showlegend=False
    ))

    # Points
    colors = ["#7a7a7a", "#d95f4b", "#d95f4b", "#d95f4b", "#7a9e7e"]
    fig.add_trace(go.Scattergeo(
        lat=villes["lat"], lon=villes["lon"],
        mode="markers+text",
        marker=dict(size=[8,16,16,16,16], color=colors,
                    line=dict(width=2, color="white")),
        text=villes["ville"],
        textposition=["top right","top right","bottom left","top right","top right"],
        textfont=dict(family="DM Sans", size=11, color="#1c1c1c"),
        showlegend=False,
        hovertemplate="<b>%{text}</b><br>%{lat:.2f}N, %{lon:.2f}E<extra></extra>"
    ))

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        geo=dict(
            scope="africa",
            bgcolor="rgba(0,0,0,0)",
            showland=True, landcolor="#e8e4de",
            showocean=True, oceancolor="#dce8f0",
            showcoastlines=True, coastlinecolor="#c5bfb8",
            showcountries=True, countrycolor="#cec8c1",
            showframe=False,
            center=dict(lat=33, lon=-6),
            projection_scale=4.5
        ),
        margin=dict(t=0, b=0, l=0, r=0),
        height=380,
        font=dict(family="DM Sans", color="#1c1c1c")
    )

    st.plotly_chart(fig, use_container_width=True)

with col_itin:
    st.markdown('<div class="section-label">Planning</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Jour par jour</div>', unsafe_allow_html=True)

    etapes = [
        ("J1–J4", "Marrakech", "Médina, Jemaa el-Fna, souks, Jardins Majorelle, hammam.", ["Culture", "Gastronomie", "Shopping"]),
        ("J5–J6", "Essaouira", "Ville bleue et blanche, plage, vent, port de pêche.", ["Détente", "Côte atlantique"]),
        ("J7–J8", "Fès", "La plus ancienne médina du monde, tanneries, medersa.", ["Histoire", "Artisanat"]),
        ("J9–J10", "Chefchaouen", "La ville bleue, randonnée dans le Rif, coucher de soleil.", ["Nature", "Photographie"]),
    ]

    for days, city, desc, tags in etapes:
        tags_html = "".join(f'<span class="itin-tag">{t}</span>' for t in tags)
        st.markdown(f"""
        <div class="itin-item">
          <div class="itin-line">
            <div class="itin-dot"></div>
            <div class="itin-vline"></div>
          </div>
          <div class="itin-content">
            <div class="itin-days">{days}</div>
            <div class="itin-city">{city}</div>
            <div class="itin-desc">{desc}</div>
            <div class="itin-tags">{tags_html}</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
# BUDGET
# ─────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div class="section-label">Finance</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Analyse du budget</div>', unsafe_allow_html=True)

col_b1, col_b2 = st.columns([2, 3], gap="large")

budget = pd.DataFrame({
    "Catégorie":  ["✈️ Vols", "🏨 Hébergement", "🍽️ Restauration", "🚌 Transport local", "🎟️ Activités", "🛍️ Shopping & divers"],
    "Prévu (€)":  [320, 380, 180, 120, 150, 250],
    "Réel (€)":   [310, 400, 195, 105, 160, 230],
    "Couleur":    ["#d95f4b","#7a9e7e","#c9a84c","#9b8fcf","#5b8ec4","#e8915a"]
})
budget["Écart (€)"] = budget["Réel (€)"] - budget["Prévu (€)"]
budget["Écart (%)"] = ((budget["Réel (€)"] - budget["Prévu (€)"]) / budget["Prévu (€)"] * 100).round(1)

with col_b1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    for _, row in budget.iterrows():
        ecart_color = "#d95f4b" if row["Écart (€)"] > 0 else "#7a9e7e"
        ecart_str = f'+{row["Écart (€)"]}€' if row["Écart (€)"] > 0 else f'{row["Écart (€)"]}€'
        pct = int(row["Réel (€)"] / budget["Réel (€)"].sum() * 100)
        st.markdown(f"""
        <div class="budget-row">
          <div>
            <div class="budget-cat">{row['Catégorie']}</div>
            <div style="height:5px;width:{pct*2}px;max-width:180px;background:{row['Couleur']};
            border-radius:3px;margin-top:4px;opacity:0.6;"></div>
          </div>
          <div style="text-align:right;">
            <div class="budget-amt">{row['Réel (€)']} €</div>
            <div style="font-size:10px;color:{ecart_color};font-weight:500;">{ecart_str}</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

    total_prevu = budget["Prévu (€)"].sum()
    total_reel  = budget["Réel (€)"].sum()
    ecart_total = total_reel - total_prevu
    st.markdown(f"""
    <div class="budget-row" style="margin-top:8px;padding-top:12px;border-top:2px solid #1c1c1c;">
      <div style="font-weight:600;font-size:14px;">Total</div>
      <div style="text-align:right;">
        <div class="budget-amt">{total_reel} €</div>
        <div style="font-size:10px;color:#d95f4b;font-weight:500;">prévu : {total_prevu} € (+{ecart_total} €)</div>
      </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_b2:
    fig_b = go.Figure()
    fig_b.add_trace(go.Bar(
        name="Prévu",
        x=budget["Catégorie"],
        y=budget["Prévu (€)"],
        marker_color="rgba(28,28,28,0.12)",
        marker_line_color="rgba(28,28,28,0.3)",
        marker_line_width=1.5,
    ))
    fig_b.add_trace(go.Bar(
        name="Réel",
        x=budget["Catégorie"],
        y=budget["Réel (€)"],
        marker_color=budget["Couleur"].tolist(),
        marker_line_color="white",
        marker_line_width=1,
    ))
    fig_b.update_layout(
        barmode="group",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="DM Sans", color="#1c1c1c", size=11),
        legend=dict(orientation="h", y=1.1, font=dict(size=11)),
        height=320,
        margin=dict(t=20,b=0,l=0,r=0),
        xaxis=dict(tickfont=dict(size=10), gridcolor="#f0ece8"),
        yaxis=dict(gridcolor="#f0ece8", ticksuffix=" €")
    )
    st.plotly_chart(fig_b, use_container_width=True)

# ─────────────────────────────────────────────
# MÉTÉO / TEMPÉRATURES
# ─────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div class="section-label">Préparation</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Météo attendue · juillet</div>', unsafe_allow_html=True)

meteo = pd.DataFrame({
    "Ville":     ["Marrakech", "Essaouira", "Fès", "Chefchaouen"],
    "Tmax (°C)": [38, 26, 36, 30],
    "Tmin (°C)": [22, 18, 20, 19],
    "Pluie (mm)":[2, 3, 3, 5],
    "Ensoleillement (h)": [11, 9, 11, 10],
})

fig_m = go.Figure()
fig_m.add_trace(go.Bar(
    name="T° max", x=meteo["Ville"], y=meteo["Tmax (°C)"],
    marker_color="#d95f4b", marker_line_color="white", marker_line_width=1
))
fig_m.add_trace(go.Bar(
    name="T° min", x=meteo["Ville"], y=meteo["Tmin (°C)"],
    marker_color="#c9a84c", marker_line_color="white", marker_line_width=1
))
fig_m.add_trace(go.Scatter(
    name="Ensoleillement (h)", x=meteo["Ville"], y=meteo["Ensoleillement (h)"],
    mode="lines+markers", yaxis="y2",
    line=dict(color="#7a9e7e", width=2.5),
    marker=dict(size=7, color="#7a9e7e")
))
fig_m.update_layout(
    barmode="group",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="DM Sans", color="#1c1c1c", size=12),
    height=300,
    margin=dict(t=20,b=0,l=0,r=40),
    legend=dict(orientation="h", y=1.12, font=dict(size=11)),
    xaxis=dict(gridcolor="#f0ece8"),
    yaxis=dict(title="°C", gridcolor="#f0ece8", ticksuffix="°"),
    yaxis2=dict(title="h soleil", overlaying="y", side="right",
                gridcolor="transparent", range=[0,15], ticksuffix="h")
)
st.plotly_chart(fig_m, use_container_width=True)

# ─────────────────────────────────────────────
# NOTE BAS DE PAGE
# ─────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<div style="background:white;border-radius:12px;padding:20px 28px;
box-shadow:0 2px 12px rgba(0,0,0,0.05);border-left:3px solid #c9a84c;">
  <p style="font-size:13px;color:#666;line-height:1.7;margin:0;">
    <strong style="color:#1c1c1c;">Pourquoi ce projet ici ?</strong><br>
    Parce qu'un data analyst, ça analyse tout — y compris ses vacances. 
    Ce projet illustre comment j'applique mes réflexes data à un contexte perso : 
    structurer des données hétérogènes (budget, météo, géo), les visualiser clairement, 
    et en tirer des décisions concrètes. La donnée, c'est d'abord une <em>façon de penser</em>.
  </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
