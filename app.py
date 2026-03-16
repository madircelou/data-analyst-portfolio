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
