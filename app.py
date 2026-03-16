import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Elodie Marcouire | Data Portfolio",
    layout="wide"
)

# -------- STYLE -------- #

st.markdown("""
<style>

body {
background-color: #ffffff;
}

.big-title {
font-size:50px;
font-weight:700;
}

.subtitle {
font-size:22px;
color:grey;
margin-bottom:40px;
}

.section {
margin-top:60px;
}

.kpi-card {
background-color:#f6f7fb;
padding:25px;
border-radius:12px;
text-align:center;
}

.kpi-number {
font-size:35px;
font-weight:700;
}

.kpi-label {
color:grey;
}

.timeline {
border-left: 3px solid #4A90E2;
padding-left:20px;
margin-top:20px;
}

.timeline-item {
margin-bottom:20px;
}

</style>
""", unsafe_allow_html=True)

# -------- HEADER -------- #

st.markdown('<div class="big-title">Elodie Marcouire</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Data Analyst Portfolio</div>', unsafe_allow_html=True)

# -------- ABOUT ME -------- #

col1, col2 = st.columns([1,2])

with col1:

    try:
        st.image("photo.jpg", width=220)
    except:
        st.write("📷 Photo coming soon")

with col2:

    st.markdown("""
### About me

Data analyst en alternance issue d’une formation en **Mathématiques & Informatique appliquées aux Sciences Sociales**.

Je travaille sur l'analyse et l'exploitation de données pour aider à la **prise de décision**, créer des **dashboards**, et transformer les données en **insights utiles**.

J’aime explorer les données, comprendre les phénomènes et créer des visualisations simples et efficaces.

**Tools:** Python | SQL | Power BI | Excel
""")

# -------- KPI DASHBOARD -------- #

st.markdown('<div class="section"></div>', unsafe_allow_html=True)
st.subheader("About me in numbers")

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:
    st.markdown("""
    <div class="kpi-card">
    <div class="kpi-number">4</div>
    <div class="kpi-label">Years studying data</div>
    </div>
    """, unsafe_allow_html=True)

with kpi2:
    st.markdown("""
    <div class="kpi-card">
    <div class="kpi-number">15+</div>
    <div class="kpi-label">Dashboards built</div>
    </div>
    """, unsafe_allow_html=True)

with kpi3:
    st.markdown("""
    <div class="kpi-card">
    <div class="kpi-number">20+</div>
    <div class="kpi-label">Datasets explored</div>
    </div>
    """, unsafe_allow_html=True)

with kpi4:
    st.markdown("""
    <div class="kpi-card">
    <div class="kpi-number">3</div>
    <div class="kpi-label">Languages spoken</div>
    </div>
    """, unsafe_allow_html=True)


# -------- JOURNEY -------- #

st.markdown('<div class="section"></div>', unsafe_allow_html=True)
st.subheader("My Journey")

st.markdown("""
<div class="timeline">

<div class="timeline-item">
<b>2020</b> – Baccalauréat Economique et Social  
Spécialité Mathématiques (Mention Bien)
</div>

<div class="timeline-item">
<b>2020 - 2024</b> – Université de Bordeaux  
Licence Mathématiques & Informatique appliquées aux Sciences Sociales  
Parcours Economie et Gestion
</div>

<div class="timeline-item">
<b>2024 - Aujourd'hui</b> – Data Analyst (Alternance)  
Analyse de données internes  
Création de dashboards et reporting automatisés  
Nettoyage et structuration de bases de données
</div>

</div>
""", unsafe_allow_html=True)

# -------- DATA VIZ -------- #

st.markdown('<div class="section"></div>', unsafe_allow_html=True)
st.subheader("About me in data")

data = {
    "Metric": [
        "Years studying data",
        "Dashboards built",
        "Datasets explored",
        "Countries visited",
        "Books read per year"
    ],
    "Value": [4, 15, 20, 10, 12]
}

df = pd.DataFrame(data)

st.bar_chart(df.set_index("Metric"))
