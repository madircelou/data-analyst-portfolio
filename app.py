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

# ─────────────────────────
# GLOBAL STYLE
# ─────────────────────────

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=DM+Sans:wght@300;400;500&display=swap');

header, footer, #MainMenu {visibility:hidden;}

:root{
--cream:#f4f1ed;
--ink:#1c1c1c;
--muted:#7a7a7a;
--coral:#d95f4b;
--sage:#7a9e7e;
}

.stApp{
background:var(--cream);
color:var(--ink);
font-family:'DM Sans',sans-serif;
}

/* HERO */

.hero-wrap{
text-align:center;
padding:60px 20px 20px;
border-bottom:1px solid #ddd;
margin-bottom:50px;
}

.hero-name{
font-family:'Playfair Display',serif;
font-size:clamp(52px,8vw,90px);
font-weight:700;
}

.hero-subtitle{
font-size:14px;
letter-spacing:.25em;
text-transform:uppercase;
color:var(--muted);
margin-top:14px;
}

.hero-accent{
width:40px;
height:3px;
background:var(--coral);
margin:18px auto 0;
}

/* SECTION */

.section-label{
font-size:11px;
letter-spacing:.3em;
text-transform:uppercase;
color:var(--coral);
}

.section-title{
font-family:'Playfair Display',serif;
font-size:30px;
margin-bottom:20px;
}

/* BIO */

.bio-card{
background:white;
border-radius:12px;
padding:36px;
box-shadow:0 2px 24px rgba(0,0,0,.06);
line-height:1.8;
}

/* NAVBAR */

.navbar{
background:#1c1c1c;
padding:0 32px;
height:50px;
display:flex;
align-items:center;
margin:-1rem -1rem 0 -1rem;
}

.nav-inner{
display:flex;
width:100%;
align-items:center;
}

.nav-logo{
font-family:'Playfair Display',serif;
color:white;
font-weight:700;
font-size:17px;
}

.nav-links{
margin-left:auto;
display:flex;
gap:28px;
}

.nav-links span{
color:rgba(255,255,255,.6);
font-size:11px;
letter-spacing:.18em;
text-transform:uppercase;
}

@media (max-width:700px){

.nav-links{
overflow-x:auto;
gap:16px;
}

}

</style>
""", unsafe_allow_html=True)

# ─────────────────────────
# NAVBAR
# ─────────────────────────

nav_items = ["Accueil","Projets","Voyages","Expérimentations"]

st.markdown("""
<div class="navbar">
<div class="nav-inner">
<div class="nav-logo">E. Marcouire</div>
</div>
</div>
""", unsafe_allow_html=True)

cols = st.columns(len(nav_items)+1)

for i,item in enumerate(nav_items):

    with cols[i+1]:

        active = st.session_state.page == item
        label = f"**{item}**" if active else item

        if st.button(label,key=f"nav_{item}",use_container_width=True):
            st.session_state.page=item
            st.rerun()

page = st.session_state.page

# ─────────────────────────
# PAGE ACCUEIL
# ─────────────────────────

if page == "Accueil":

    st.markdown("""
    <div class="hero-wrap">
        <div class="hero-name">Elodie Marcouire</div>
        <div class="hero-subtitle">Data Analyst · Bordeaux</div>
        <div class="hero-accent"></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-label">Parcours</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Ma trajectoire</div>', unsafe_allow_html=True)

    components.html("""
<style>
body{background:#f4f1ed;font-family:'DM Sans'}
.tl{display:flex;overflow-x:auto;padding:10px}
.tl-item{flex:1;min-width:150px;text-align:center}
.tl-dot{
width:14px;height:14px;border-radius:50%;
background:#d95f4b;margin:0 auto 12px
}
.tl-year{font-weight:700}
.tl-role{font-size:12px}
</style>

<div class="tl">

<div class="tl-item">
<div class="tl-dot"></div>
<div class="tl-year">2002–18</div>
<div class="tl-role">Maroc · Mauritanie · Sénégal</div>
</div>

<div class="tl-item">
<div class="tl-dot"></div>
<div class="tl-year">2020</div>
<div class="tl-role">Bac ES</div>
</div>

<div class="tl-item">
<div class="tl-dot"></div>
<div class="tl-year">2020–24</div>
<div class="tl-role">Licence MIASHS</div>
</div>

<div class="tl-item">
<div class="tl-dot"></div>
<div class="tl-year">2024 →</div>
<div class="tl-role">Alternance Domofrance</div>
</div>

</div>
""", height=120)

    col1,col2 = st.columns([3,2])

    with col1:

        st.markdown('<div class="section-label">À propos</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Qui suis-je ?</div>', unsafe_allow_html=True)

        st.markdown("""
<div class="bio-card">

J'ai grandi entre **le Maroc, la Mauritanie et le Sénégal** avant de venir étudier à Bordeaux.

Aujourd'hui **alternante Data Analyst chez Domofrance**, je travaille avec  
**Power BI · Snowflake · Talend** pour transformer des données brutes en tableaux de bord utiles.

Ce qui me passionne :  
ce moment où un dataset chaotique révèle soudainement un **pattern**.

Parce que la donnée est avant tout **une histoire à raconter**.

</div>
""", unsafe_allow_html=True)

    with col2:

        components.html("""

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<style>
.wrapper{
display:flex;
gap:20px;
justify-content:center;
flex-wrap:wrap;
}

.chart{
width:200px;
height:200px;
}
</style>

<div class="wrapper">

<canvas id="chart1" class="chart"></canvas>
<canvas id="chart2" class="chart"></canvas>

</div>

<script>

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

new Chart(document.getElementById("chart1"),{
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

new Chart(document.getElementById("chart2"),{
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

</script>

""",height=260)

# ─────────────────────────
# PAGE PROJETS
# ─────────────────────────

elif page == "Projets":

    st.title("Projets")
    st.write("Section projets en construction.")

# ─────────────────────────
# PAGE VOYAGES
# ─────────────────────────

elif page == "Voyages":

    travel = pd.DataFrame({
        "country":["Mauritanie","Italie","Portugal","Espagne","Angleterre","Sénégal","Maroc","Malte","Thaïlande"],
        "lat":[20.25,41.9,38.72,40.41,51.5,14.69,33.57,35.9,13.75],
        "lon":[-10.32,12.49,-9.13,-3.7,-0.12,-17.44,-7.59,14.51,100.5]
    })

    fig = px.scatter_geo(
        travel,
        lat="lat",
        lon="lon",
        hover_name="country"
    )

    st.plotly_chart(fig,use_container_width=True)

# ─────────────────────────
# EXPERIMENTATIONS
# ─────────────────────────

elif page == "Expérimentations":

    st.title("Expérimentations")
    st.write("Section laboratoire de data stories.")
