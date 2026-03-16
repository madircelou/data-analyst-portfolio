# ─────────────────────────────────────────────
# TOP NAVIGATION BAR (RESPONSIVE)
# ─────────────────────────────────────────────

nav_items = ["Accueil", "Projets", "Voyages", "Expérimentations"]

st.markdown("""
<style>

.navbar {
    background:#1c1c1c;
    padding:0 28px;
    height:52px;
    display:flex;
    align-items:center;
    margin:-1rem -1rem 0 -1rem;
}

.nav-inner {
    width:100%;
    display:flex;
    align-items:center;
}

.nav-logo {
    font-family:'Playfair Display', serif;
    font-size:17px;
    font-weight:700;
    color:white;
    letter-spacing:-0.01em;
}

.nav-links {
    margin-left:auto;
    display:flex;
    gap:28px;
}

.nav-links span {
    font-family:'DM Sans', sans-serif;
    font-size:11px;
    letter-spacing:0.18em;
    text-transform:uppercase;
    color:rgba(255,255,255,0.6);
}

@media (max-width:700px){

    .nav-links{
        gap:16px;
        overflow-x:auto;
    }

}

</style>

<div class="navbar">
    <div class="nav-inner">
        <div class="nav-logo">E. Marcouire</div>
    </div>
</div>

""", unsafe_allow_html=True)

# boutons de navigation (fonctionnels)

cols = st.columns(len(nav_items)+1)

for i, item in enumerate(nav_items):

    with cols[i+1]:

        active = st.session_state.page == item

        label = f"**{item}**" if active else item

        if st.button(label, key=f"nav_{item}", use_container_width=True):
            st.session_state.page = item
            st.rerun()

page = st.session_state.page
