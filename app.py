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
    ["Home","Projects","Travel","Experiments"]
)

# =====================================================
# HOME
# =====================================================

if page == "Home":

    st.markdown('<div class="big-title">Elodie Marcouire</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Data Analyst Portfolio</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1,2])

    # PHOTO
    with col1:
        try:
            st.image("photo.jpg", width=250)
        except:
            st.write("📷 Photo coming soon")

    # ABOUT ME
    with col2:

        st.markdown("""
### About me

Nice to meet you!

Currently working as a **Data Analyst apprentice**, I am always looking for new topics to explore.

Curious and motivated, I love playing with data and trying to understand what it hides.  
For me, data analysis is a bit like **magic**: you start with something messy and little by little patterns appear and solutions emerge.

What I enjoy the most is exploring datasets, asking questions and finding insights that help understand problems better.
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
        <div class="kpi-number">9</div>
        <div class="kpi-label">Countries visited</div>
        </div>
        """, unsafe_allow_html=True)

# ---------------- TOOLS GRAPH ---------------- #

    st.markdown('<div class="section"></div>', unsafe_allow_html=True)
    st.subheader("Tools")

    tools = pd.DataFrame({
        "Tool":["Python","SQL","Power BI","Excel","R"],
        "Level":[4,4,3,3,2]
    })

    fig_tools = px.line_polar(
        tools,
        r="Level",
        theta="Tool",
        line_close=True
    )

    fig_tools.update_traces(fill='toself')

    st.plotly_chart(fig_tools,use_container_width=True)

# ---------------- JOURNEY ---------------- #

    st.markdown('<div class="section"></div>', unsafe_allow_html=True)
    st.subheader("My Journey")

    st.markdown("""
<div class="timeline">

<div class="timeline-item">
<b>2020</b> – Baccalauréat ES (Mention Bien)
</div>

<div class="timeline-item">
<b>2020 - 2024</b> – Université de Bordeaux  
Licence Mathématiques & Informatique appliquées aux Sciences Sociales
</div>

<div class="timeline-item">
<b>2024 - Today</b> – Data Analyst (Apprenticeship)
</div>

</div>
""", unsafe_allow_html=True)

# =====================================================
# PROJECTS
# =====================================================

elif page == "Projects":

    st.title("Projects")

    st.write("Projects and analyses will appear here.")

# =====================================================
# TRAVEL MAP
# =====================================================

elif page == "Travel":

    st.title("Travel Analytics")

    travel = pd.DataFrame({
        "country":[
            "Mauritania","Italy","Portugal","Spain",
            "United Kingdom","Senegal","Morocco","Malta","Thailand"
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
# EXPERIMENTS
# =====================================================

elif page == "Experiments":

    st.title("Data Experiments")

    st.write("Small data explorations will appear here.")
