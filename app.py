import streamlit as st
import pandas as pd

st.set_page_config(page_title="Elodie Marcouire | Data Portfolio", layout="wide")

# Style
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

st.title("Elodie Marcouire")
st.subheader("Data Analyst Portfolio")

st.markdown('<div class="presentation">', unsafe_allow_html=True)

col1, col2 = st.columns([1,2])

with col1:
    st.image("photo.jpg", width=200)

with col2:
    st.markdown("""
### About me

Data analyst en alternance, issue d’une formation en **Mathématiques & Informatique**.  
Je travaille sur l’analyse de données, la création de dashboards et l’aide à la prise de décision.

J’aime explorer les données pour comprendre des phénomènes réels et transformer les analyses en insights utiles.

**Tools:** Python | SQL | Power BI | Excel
""")

st.markdown('</div>', unsafe_allow_html=True)
