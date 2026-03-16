import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Elodie Marcouire | Data Portfolio",
    layout="wide"
)

# -------- STYLE -------- #

st.markdown("""
<style>

/* Background général */
.stApp {
    background-color: #fafafa;
}

/* Titres */

.big-title {
font-size:64px;
font-weight:700;
margin-bottom:10px;
}

.subtitle {
font-size:28px;
color:#6b7280;
margin-bottom:40px;
}

/* texte général */

p, li {
font-size:18px;
}

/* sections */

.section {
margin-top:70px;
}

/* KPI */

.kpi-card {
background-color:white;
padding:30px;
border-radius:16px;
text-align:center;
box-shadow:0 4px 12px rgba(0,0,0,0.06);
}

.kpi-number {
font-size:42px;
font-weight:700;
}

.kpi-label {
color:#6b7280;
font-size:18px;
}

/* timeline */

.timeline {
border-left: 3px solid #2563eb;
padding-left:25px;
margin-top:20px;
}

.timeline-item {
margin-bottom:25px;
font-size:18px;
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
        st.image("photo.jpg", width=250)
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

# -------- KPI -------- #

st.markdown('<div class="section"></div>', unsafe_allow_html=True)
st.subheader("About me in numbers")

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.markdown("""
    <div class="kpi-card">
    <div class="kpi-number">4</div>
    <div class="kpi-label">Years studying data</div>
    </div>
    """, unsafe_allow_html=True)

with k2:
    st.markdown("""
    <div class="kpi-card">
    <div class="kpi-number">15+</div>
    <div class="kpi-label">Dashboards built</div>
    </div>
    """, unsafe_allow_html=True)

with k3:
    st.markdown("""
    <div class="kpi-card">
    <div class="kpi-number">20+</div>
    <div class="kpi-label">Datasets explored</div>
    </div>
    """, unsafe_allow_html=True)

with k4:
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
