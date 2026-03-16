import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Elodie Marcouire | Data Portfolio",
    layout="wide"
)

# ---------------- STYLE ---------------- #

st.markdown("""
<style>

.stApp {
    background-color:#f4f1ed;
    color:#2f2f2f;
}

.big-title {
font-size:60px;
font-weight:700;
}

.subtitle {
font-size:24px;
color:#8b5e3c;
margin-bottom:40px;
}

.section {
margin-top:70px;
}

.kpi-card {
background:white;
padding:30px;
border-radius:15px;
text-align:center;
box-shadow:0 4px 12px rgba(0,0,0,0.08);
}

.kpi-number {
font-size:40px;
font-weight:700;
color:#8b5e3c;
}

.kpi-label {
font-size:18px;
color:#555;
}

.timeline {
border-left:4px solid #8b5e3c;
padding-left:25px;
margin-top:20px;
}

.timeline-item {
margin-bottom:25px;
font-size:18px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- NAVIGATION ---------------- #

page = st.sidebar.radio(
    "Navigation",
    ["Home","Projects","Travel Map","Data Experiments"]
)

# =====================================================
# HOME
# =====================================================

if page == "Home":

    st.markdown('<div class="big-title">Elodie Marcouire</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Data Analyst Portfolio</div>', unsafe_allow_html=True)

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

Je travaille sur l’analyse et l’exploitation de données pour aider à la **prise de décision**, créer des **dashboards**, et transformer les données en **insights utiles**.

J’aime explorer les données, comprendre les phénomènes et créer des visualisations simples et efficaces.

**Tools**

Python  
SQL  
Power BI  
Excel
""")

# ---------------- KPI ---------------- #

    st.markdown('<div class="section"></div>', unsafe_allow_html=True)
    st.subheader("About me in numbers")

    k1,k2,k3,k4 = st.columns(4)

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

# ---------------- JOURNEY ---------------- #

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
</div>

</div>
""", unsafe_allow_html=True)

# ---------------- DATA VIZ ---------------- #

    st.markdown('<div class="section"></div>', unsafe_allow_html=True)
    st.subheader("About me in data")

    df = pd.DataFrame({
        "Category":[
            "Years studying data",
            "Dashboards built",
            "Datasets explored",
            "Countries visited",
            "Books per year"
        ],
        "Value":[4,15,20,10,12]
    })

    fig = px.bar(
        df,
        x="Value",
        y="Category",
        orientation="h",
        color="Value",
        color_continuous_scale="Brwnyl"
    )

    st.plotly_chart(fig,use_container_width=True)

# =====================================================
# PROJECTS
# =====================================================

elif page == "Projects":

    st.title("Data Projects")

    st.write("Some of my data explorations and projects.")

    st.markdown("### Example project")

    st.write("""
Airbnb price analysis in European cities.

Goal:
- understand pricing differences
- explore geographic effects
""")

# =====================================================
# TRAVEL MAP
# =====================================================

elif page == "Travel Map":

    st.title("Travel Analytics")

    travel = pd.DataFrame({
        "city":["Lisbon","Rome","Barcelona","Amsterdam"],
        "lat":[38.72,41.90,41.38,52.37],
        "lon":[-9.13,12.49,2.17,4.89]
    })

    st.map(travel)

# =====================================================
# DATA EXPERIMENTS
# =====================================================

elif page == "Data Experiments":

    st.title("Data Experiments")

    st.write("Small analyses and experiments with datasets.")
