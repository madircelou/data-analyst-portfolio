import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Elodie Marcouire | Portfolio Data",
    layout="wide"
)

# ---------------- STYLE ---------------- #

st.markdown("""
<style>

.stApp {
background-color:#f4f1ed;
color:#2f2f2f;
}

/* Bandeau */

.hero {
background:#8b5e3c;
padding:60px;
border-radius:10px;
margin-bottom:40px;
}

.hero-title {
font-size:60px;
font-weight:700;
color:white;
}

.hero-sub {
font-size:22px;
color:#f3e7db;
}

/* timeline */

.timeline {
display:flex;
justify-content:space-between;
margin-top:40px;
}

.step {
background:white;
padding:20px;
border-radius:10px;
width:30%;
box-shadow:0 3px 10px rgba(0,0,0,0.08);
text-align:center;
}

/* tools */

.tool-card {
background:white;
padding:15px;
border-radius:10px;
margin-bottom:15px;
box-shadow:0 3px 8px rgba(0,0,0,0.05);
}

.section {
margin-top:60px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- NAVIGATION ---------------- #

page = st.sidebar.radio(
    "Navigation",
    ["Accueil","Projets","Voyages","Expérimentations"]
)

# =====================================================
# ACCUEIL
# =====================================================

if page == "Accueil":

    # HERO BANNER

    st.markdown("""
<div class="hero">
<div class="hero-title">Elodie Marcouire</div>
<div class="hero-sub">Portfolio Data Analyst</div>
</div>
""", unsafe_allow_html=True)

# ---------------- TIMELINE ---------------- #

    st.markdown("### Mon parcours")

    st.markdown("""
<div class="timeline">

<div class="step">
<b>2020</b><br>
Bac ES<br>
Mention Bien
</div>

<div class="step">
<b>2020 - 2024</b><br>
Licence MIASHS<br>
Université de Bordeaux
</div>

<div class="step">
<b>2024 - Aujourd'hui</b><br>
Alternante Data Analyst<br>
Domofrance
</div>

<div class="step">
<b>What's next ?</b><br>
La suite reste à écrire…
</div>

</div>
""", unsafe_allow_html=True)

# ---------------- ABOUT + TOOLS ---------------- #

    st.markdown('<div class="section"></div>', unsafe_allow_html=True)

    col1, col2 = st.columns([2,1])

    with col1:

        st.markdown("""
### Qui suis-je ?

Enchantée !

Actuellement **en alternance en data**, je suis toujours à la recherche de nouveaux sujets à explorer.

Curieuse et motivée, j'aime jouer avec la donnée et essayer de comprendre ce qu'elle raconte.  
Pour moi la data c'est un peu de la **magie** : on part de quelque chose de brouillon et petit à petit des patterns apparaissent et des solutions émergent.

Ce que j'aime le plus dans ce métier, c'est explorer des datasets, poser des questions et trouver des insights qui permettent de mieux comprendre les problèmes.
""")

    with col2:

        st.markdown("### Outils")

        st.markdown("""
<div class="tool-card">
<b>Python</b><br>
Analyse de données, pandas, visualisation
</div>
""", unsafe_allow_html=True)

        st.markdown("""
<div class="tool-card">
<b>SQL</b><br>
Extraction et transformation des données
</div>
""", unsafe_allow_html=True)

        st.markdown("""
<div class="tool-card">
<b>Power BI</b><br>
Création de dashboards et reporting
</div>
""", unsafe_allow_html=True)

        st.markdown("""
<div class="tool-card">
<b>Excel</b><br>
Exploration rapide et manipulation de données
</div>
""", unsafe_allow_html=True)

# ---------------- CHIFFRES ---------------- #

    st.markdown('<div class="section"></div>', unsafe_allow_html=True)

    st.subheader("Quelques chiffres")

    df = pd.DataFrame({
        "Catégorie":[
            "Années dans la data",
            "Dashboards réalisés",
            "Datasets explorés",
            "Pays visités"
        ],
        "Valeur":[4,15,20,9]
    })

    fig = px.bar(
        df,
        x="Valeur",
        y="Catégorie",
        orientation="h",
        color="Valeur",
        text="Valeur",
        color_continuous_scale="Brwnyl"
    )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="#f4f1ed",
        coloraxis_showscale=False
    )

    st.plotly_chart(fig,use_container_width=True)

# =====================================================
# PROJETS
# =====================================================

elif page == "Projets":

    st.title("Projets")

    st.write("Les projets data seront présentés ici.")

# =====================================================
# VOYAGES
# =====================================================

elif page == "Voyages":

    st.title("Voyages")

    travel = pd.DataFrame({
        "country":[
            "Mauritanie","Italie","Portugal","Espagne",
            "Angleterre","Sénégal","Maroc","Malte","Thaïlande"
        ],
        "lat":[
            20.25,41.90,38.72,40.41,51.50,14.69,33.57,35.90,13.75
        ],
        "lon":[
            -10.32,12.49,-9.13,-3.70,-0.12,-17.44,-7.59,14.51,100.50
        ]
    })

    fig = px.scatter_geo(
        travel,
        lat="lat",
        lon="lon",
        hover_name="country",
        projection="natural earth"
    )

    fig.update_layout(height=600)

    st.plotly_chart(fig,use_container_width=True)

# =====================================================
# EXPERIMENTATIONS
# =====================================================

elif page == "Expérimentations":

    st.title("Expérimentations")

    st.write("Des analyses exploratoires seront ajoutées ici.")
