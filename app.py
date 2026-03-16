import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Elodie Marcouire | Portfolio",
    layout="wide"
)

# ---------------- STYLE ---------------- #

st.markdown("""
<style>

header {visibility:hidden;}
footer {visibility:hidden;}
#MainMenu {visibility:hidden;}

.stApp{
background-color:#f4f1ed;
color:#1f1f1f;
font-family: "Segoe UI", sans-serif;
}

/* titre */

.name{
font-size:70px;
text-align:center;
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
justify-content:space-between;
margin-top:50px;
}

.step{
background:white;
padding:20px;
border-radius:10px;
width:22%;
text-align:center;
box-shadow:0 4px 12px rgba(0,0,0,0.08);
transition:0.2s;
cursor:pointer;
}

.step:hover{
transform:translateY(-5px);
box-shadow:0 6px 16px rgba(0,0,0,0.15);
}

/* sections */

.section{
margin-top:70px;
}

/* metrics */

[data-testid="stMetricValue"]{
color:#1f1f1f;
font-size:35px;
}

[data-testid="stMetricLabel"]{
color:#555;
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

    st.markdown('<div class="name">Elodie Marcouire</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Portfolio Data Analyst</div>', unsafe_allow_html=True)

# ---------------- TIMELINE ---------------- #

    st.markdown("### Mon parcours")

    st.markdown("""
<div class="timeline">

<a href="https://fr.wikipedia.org/wiki/Baccalauréat_en_France" target="_blank" style="text-decoration:none;color:inherit">
<div class="step">
<b>2020</b><br>
Bac ES<br>
Spécialité Maths
</div>
</a>

<a href="https://www.u-bordeaux.fr/" target="_blank" style="text-decoration:none;color:inherit">
<div class="step">
<b>2020-2024</b><br>
Licence MIASHS<br>
Université de Bordeaux
</div>
</a>

<a href="https://www.domofrance.fr/" target="_blank" style="text-decoration:none;color:inherit">
<div class="step">
<b>2024-Aujourd'hui</b><br>
Alternante Data Analyst<br>
Domofrance
</div>
</a>

<div class="step">
<b>What's next ?</b><br>
La suite reste à écrire
</div>

</div>
""", unsafe_allow_html=True)

# ---------------- ABOUT + RADARS ---------------- #

    st.markdown('<div class="section"></div>', unsafe_allow_html=True)

    col1,col2 = st.columns([2,1])

    with col1:

        st.markdown("""
### Qui suis-je ?

Enchantée !

Actuellement **en alternance en data**, je suis toujours à la recherche de nouveaux sujets à explorer.

J’ai grandi en changeant souvent d’environnement : j’ai vécu **au Maroc, en Mauritanie, au Sénégal, à Paris**, et aujourd’hui à Bordeaux.

Ces expériences m’ont appris à observer, m’adapter et comprendre des contextes très différents — un peu comme lorsqu’on explore un dataset inconnu.

Curieuse et motivée, j’aime jouer avec la donnée et essayer de comprendre ce qu’elle raconte.

Pour moi la data c’est un peu de la **magie** : on part de quelque chose de brouillon et petit à petit des patterns apparaissent et des solutions émergent.

Sur ce site, je vous propose donc de découvrir **ma vie à travers la data** : mes projets, mes explorations et quelques analyses qui reflètent ma curiosité.
""")

    with col2:

        radar1, radar2 = st.columns(2)

        # DATA ANALYSIS

        data_analysis = pd.DataFrame({
            "tool":["Python","SQL","Excel","R"],
            "score":[3,4,3,2]
        })

        fig1 = px.line_polar(
            data_analysis,
            r="score",
            theta="tool",
            line_close=True
        )

        fig1.update_traces(
            fill='toself',
            line_color="#1f77b4",
            fillcolor="rgba(31,119,180,0.4)"
        )

        fig1.update_layout(
            showlegend=False,
            paper_bgcolor="rgba(0,0,0,0)",
            polar=dict(
                bgcolor="rgba(0,0,0,0)",
                radialaxis=dict(
                    visible=True,
                    range=[0,4],
                    gridcolor="#bdbdbd",
                    tickfont=dict(color="#1f1f1f")
                ),
                angularaxis=dict(
                    tickfont=dict(color="#1f1f1f")
                )
            )
        )

        radar1.plotly_chart(fig1,use_container_width=True)

        # DATA STACK

        stack = pd.DataFrame({
            "tool":["Snowflake","Talend","Power BI","DataGalaxy","Confluence"],
            "score":[3,3,4,2,2]
        })

        fig2 = px.line_polar(
            stack,
            r="score",
            theta="tool",
            line_close=True
        )

        fig2.update_traces(
            fill='toself',
            line_color="#ff7f0e",
            fillcolor="rgba(255,127,14,0.4)"
        )

        fig2.update_layout(
            showlegend=False,
            paper_bgcolor="rgba(0,0,0,0)",
            polar=dict(
                bgcolor="rgba(0,0,0,0)",
                radialaxis=dict(
                    visible=True,
                    range=[0,4],
                    gridcolor="#bdbdbd",
                    tickfont=dict(color="#1f1f1f")
                ),
                angularaxis=dict(
                    tickfont=dict(color="#1f1f1f")
                )
            )
        )

        radar2.plotly_chart(fig2,use_container_width=True)

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
        "lat":[20.25,41.90,38.72,40.41,51.50,14.69,33.57,35.90,13.75],
        "lon":[-10.32,12.49,-9.13,-3.70,-0.12,-17.44,-7.59,14.51,100.50]
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
