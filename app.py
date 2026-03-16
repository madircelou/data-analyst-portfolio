import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Elodie Marcouire | Portfolio",
    layout="wide"
)

# ---------------- STYLE GLOBAL ---------------- #

st.markdown("""
<style>

/* supprimer header streamlit */

header {visibility:hidden;}
footer {visibility:hidden;}
#MainMenu {visibility:hidden;}

/* fond */

.stApp{
background-color:#f4f1ed;
color:#2f2f2f;
}

/* titre */

.name{
font-size:70px;
text-align:center;
font-family: "Trebuchet MS", sans-serif;
font-weight:700;
margin-top:40px;
}

.subtitle{
text-align:center;
font-size:22px;
color:#6b6b6b;
margin-bottom:40px;
}

/* timeline */

.timeline{
display:flex;
align-items:center;
justify-content:space-between;
margin-top:30px;
}

.step{
background:white;
padding:20px;
border-radius:10px;
width:22%;
box-shadow:0 3px 8px rgba(0,0,0,0.08);
text-align:center;
}

.arrow{
font-size:40px;
text-align:center;
}

/* tools */

.section{
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

    # TITRE

    st.markdown('<div class="name">Elodie Marcouire</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Portfolio Data Analyst</div>', unsafe_allow_html=True)

# ---------------- TIMELINE ---------------- #

    st.markdown("### Mon parcours")

    st.markdown("""
<div class="timeline">

<div class="step">
<b>2020</b><br>
Bac ES<br>
Spécialité Maths
</div>

<div class="arrow">→</div>

<div class="step">
<b>2020-2024</b><br>
Licence MIASHS<br>
Université de Bordeaux
</div>

<div class="arrow">→</div>

<div class="step">
<b>2024-Aujourd'hui</b><br>
Alternante Data Analyst<br>
Domofrance
</div>

<div class="arrow">→</div>

<div class="step">
<b>What's next ?</b><br>
La suite reste à écrire
</div>

</div>
""", unsafe_allow_html=True)

# ---------------- ABOUT + TOOLS ---------------- #

    st.markdown('<div class="section"></div>', unsafe_allow_html=True)

    col1,col2 = st.columns([2,1])

    with col1:

        st.markdown("""
### Qui suis-je ?

Enchantée !

Actuellement **en alternance en data**, je suis toujours à la recherche de nouveaux sujets à explorer.

Curieuse et motivée, j'aime jouer avec la donnée et essayer de comprendre ce qu'elle raconte.

Pour moi la data c'est un peu de la **magie** : on part de quelque chose de brouillon et petit à petit des patterns apparaissent et des solutions émergent.

Ce que j'aime le plus dans ce métier, c'est explorer des datasets, poser des questions et trouver des insights qui permettent de mieux comprendre les problèmes.
""")

    # radar chart tools

    with col2:

        tools = pd.DataFrame({
            "tool":["Python","SQL","Power BI","Excel","R"],
            "score":[4,4,3,3,2]
        })

        fig = px.line_polar(
            tools,
            r="score",
            theta="tool",
            line_close=True
        )

        fig.update_traces(fill='toself')

        fig.update_layout(
            showlegend=False,
            polar=dict(
                bgcolor="rgba(0,0,0,0)"
            )
        )

        st.plotly_chart(fig,use_container_width=True)

# ---------------- CHIFFRES ---------------- #

    st.markdown('<div class="section"></div>', unsafe_allow_html=True)

    st.markdown("### Quelques chiffres")

    c1,c2,c3,c4 = st.columns(4)

    c1.metric("Années dans la data","4")
    c2.metric("Dashboards réalisés","15+")
    c3.metric("Datasets explorés","20+")
    c4.metric("Pays visités","9")

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
