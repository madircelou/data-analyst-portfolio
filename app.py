import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Elodie Marcouire | Data Portfolio",
    layout="wide"
)

# CSS styling
st.markdown("""
<style>

.presentation {
    background-color: #f5f7fb;
    padding:40px;
    border-radius:10px;
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


# TITLE
st.title("Elodie Marcouire")
st.subheader("Data Analyst Portfolio")


# PRESENTATION SECTION
st.markdown('<div class="presentation">', unsafe_allow_html=True)

col1, col2 = st.columns([1,2])

with col1:
    st.image("photo.jpg", width=220)

with col2:
    st.markdown("""
### About me

Data analyst en alternance, issue d’une formation en **Mathématiques & Informatique appliquées aux Sciences Sociales**.

Je travaille sur l’analyse et l’exploitation de données afin d’aider à la prise de décision.  
Je développe des **tableaux de bord**, j’analyse des datasets et je transforme les données en **insights exploitables**.

J’aime particulièrement comprendre les phénomènes à travers la data et créer des visualisations claires et utiles.

**Tools:** Python | SQL | Power BI | Excel
""")

st.markdown('</div>', unsafe_allow_html=True)


# TIMELINE
st.header("My Journey")

st.markdown("""
<div class="timeline">

<div class="timeline-item">
<b>2020</b> – Baccalauréat Economique et Social  
Spécialité Mathématiques (Mention Bien)
</div>

<div class="timeline-item">
<b>2020 - 2024</b> – Université de Bordeaux  
Licence Mathématiques & Informatique appliquées aux Sciences Humaines & Sociales  
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


# ABOUT ME IN DATA
st.header("About me in data")

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
