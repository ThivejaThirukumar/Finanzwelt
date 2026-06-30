from utils.berechnungen import berechne_rendite, berechne_gewinn

st.title("💼 Portfolio-Rechner")
st.subheader("Deine Aktien eingeben")
col1, col2, col3 = st.columns(3)
col1: name, col2: startkurs, col3; endkurs

aktien_namen = [name1, name2, name3]

renditen = [berechne_rendite(s,e) for s,e in zip(starts, ends)]

fig = px.pie(names = aktien, values = werte, title = "Portfolio-Verteilung")
fig2 = px.bar(x = aktien_namen, y = renditen, title = "Rendite je Aktie")
color = renditen, color_continous_scale = "RdYiGn"
