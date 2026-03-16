import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Elodie Marcouire | Portfolio",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# SESSION STATE
if "page" not in st.session_state:
    st.session_state.page = "Accueil"


# ─────────────────────────────────────────────
# STYLE GLOBAL
# ─────────────────────────────────────────────

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;1,400&family=DM+Sans:wght@300;400;500&display=swap');

header, footer, #MainMenu { visibility: hidden; }
[data-testid="stSidebar"] { display: none; }
section[data-testid="stSidebarNav"] { display: none; }

:root {
    --cream: #f4f1ed;
    --ink:   #1c1c1c;
    --muted: #7a7a7a;
    --coral: #d95f4b;
    --sage:  #7a9e7e;
    --gold:  #c9a84c;
    --white: #ffffff;
}

.stApp {
    background-color: var(--cream);
    color: var(--ink);
    font-family: 'DM Sans', sans-serif;
}

/* HERO */

.hero-wrap {
    text-align: center;
    padding: 60px 20px 20px;
    border-bottom: 1px solid #ddd;
    margin-bottom: 50px;
}

.hero-name {
    font-family: 'Playfair Display', serif;
    font-size: clamp(52px, 8vw, 90px);
    font-weight: 700;
}

.hero-subtitle {
    font-size: 15px;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    color: var(--muted);
    margin-top: 14px;
}

.hero-accent {
    width: 40px;
    height: 3px;
    background: var(--coral);
    margin: 18px auto 0;
}

/* SECTIONS */

.section-label {
    font-size: 11px;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    color: var(--coral);
}

.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 30px;
    margin-bottom: 28px;
}

/* BIO */

.bio-card {
    background: var(--white);
    border-radius: 12px;
    padding: 36px 40px;
    box-shadow: 0 2px 24px rgba(0,0,0,0.06);
    line-height: 1.85;
}

/* NAV BUTTONS */

div[data-testid="stHorizontalBlock"] div[data-testid="stButton"] button {
    background: #1c1c1c !important;
    border: none !important;
    border-radius: 0 !important;
    color: rgba(255,255,255,0.6) !important;
    font-size: 11px !important;
    letter-spacing: 0.2em !important;
    text-transform: uppercase !important;
}

div[data-testid="stHorizontalBlock"] div[data-testid="stButton"] button:hover {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# NAVBAR
# ─────────────────────────────────────────────

nav_items = ["Accueil", "Projets", "Voyages", "Expérimentations"]

st.markdown("""
<div style="
background:#1c1c1c;
height:52px;
display:flex;
align-items:center;
padding:0 40px;
margin:-1rem -1rem 0 -1rem;">
<span style="
font-family:'Playfair Display', serif;
font-size:17px;
font-weight:700;
color:white;">
E. Marcouire
</span>
</div>
""", unsafe_allow_html=True)

cols = st.columns([5,1,1,1,1])

with cols[0]:
    st.markdown(
        '<div style="height:40px;background:#1c1c1c;margin-top:-48px;"></div>',
        unsafe_allow_html=True
    )

for col, item in zip(cols[1:], nav_items):
    with col:
        if st.button(item, key=f"nav_{item}", use_container_width=True):
            st.session_state.page = item
            st.rerun()

page = st.session_state.page


# ─────────────────────────────────────────────
# PAGE ACCUEIL
# ─────────────────────────────────────────────

if page == "Accueil":

    st.markdown("""
    <div class="hero-wrap">
        <div class="hero-name">Elodie Marcouire</div>
        <div class="hero-subtitle">Data Analyst · Bordeaux</div>
        <div class="hero-accent"></div>
    </div>
    """, unsafe_allow_html=True)


    # BIO + RADARS

    col_bio, col_radar = st.columns([3,2])

    with col_bio:

        st.markdown('<div class="section-label">À propos</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Qui suis-je ?</div>', unsafe_allow_html=True)

        st.markdown("""
        <div class="bio-card">

        J'ai grandi entre **le Maroc, la Mauritanie et le Sénégal**
        avant de venir étudier à Bordeaux.

        Aujourd'hui **alternante Data Analyst chez Domofrance**,
        je travaille avec **Power BI · Snowflake · Talend**
        pour transformer des données brutes en tableaux de bord.

        Ce qui me passionne : comprendre ce que les données racontent.

        </div>
        """, unsafe_allow_html=True)


    with col_radar:

        components.html("""

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<style>
.wrap{
display:flex;
gap:20px;
justify-content:center;
}

.chart{
width:220px;
height:220px;
}
</style>

<div class="wrap">
<canvas id="radar1" class="chart"></canvas>
<canvas id="radar2" class="chart"></canvas>
</div>

<script>

setTimeout(() => {

const config = {
type:'radar',
options:{
responsive:true,
plugins:{legend:{display:false}},
scales:{
r:{
min:0,max:4,
ticks:{display:false},
grid:{color:"#e0dcd6"},
angleLines:{color:"#e0dcd6"},
pointLabels:{color:"#1c1c1c"}
}
}
}
};

new Chart(document.getElementById("radar1"),{
...config,
data:{
labels:["Python","SQL","Excel","R"],
datasets:[{
data:[3,4,3,2],
backgroundColor:"rgba(217,95,75,0.2)",
borderColor:"#d95f4b"
}]
}
});

new Chart(document.getElementById("radar2"),{
...config,
data:{
labels:["Snowflake","Talend","Power BI","DataGalaxy","Confluence"],
datasets:[{
data:[3,3,4,2,2],
backgroundColor:"rgba(122,158,126,0.2)",
borderColor:"#7a9e7e"
}]
}
});

},200)

</script>

""", height=260)


# ─────────────────────────────────────────────
# PAGE PROJETS
# ─────────────────────────────────────────────

elif page == "Projets":

    st.title("Projets")

    st.write("Section projets en cours de construction.")


# ─────────────────────────────────────────────
# PAGE VOYAGES
# ─────────────────────────────────────────────

elif page == "Voyages":

    travel = pd.DataFrame({
        "country":["Mauritanie","Italie","Portugal","Espagne","Angleterre","Sénégal","Maroc","Malte","Thaïlande"],
        "lat":[20.25,41.9,38.72,40.41,51.5,14.69,33.57,35.9,13.75],
        "lon":[-10.32,12.49,-9.13,-3.7,-0.12,-17.44,-7.59,14.51,100.5]
    })

    fig = px.scatter_geo(travel, lat="lat", lon="lon", hover_name="country")

    st.plotly_chart(fig, use_container_width=True)


# ─────────────────────────────────────────────
# PAGE EXPERIMENTATIONS
# ─────────────────────────────────────────────

elif page == "Expérimentations":

    st.title("Expérimentations")
