import streamlit as st
import random
import plotly.express as px

st.title("📊 Aktien-Simulator")

startkurs = st.slider("Startkurs (CHF)", 10, 500, 100)
vol = st.slider("Volatilität", 0.005, 0.05, 0.015)

rendite = -100  # Sentinel-Wert damit die Schleife startet

while rendite <= 20:
    kurse = [startkurs]
    for tag in range(251):
        veraenderung = random.gauss(0.0005, vol)
        neuer_kurs = kurse[-1] * (1 + veraenderung)
        kurse.append(neuer_kurs)

    hoechstkurs = max(kurse)
    tiefstkurs = min(kurse)
    schlusskurs = kurse[-1]
    rendite = (schlusskurs - startkurs) / startkurs * 100

col1, col2, col3 = st.columns(3)
col1.metric("Startkurs",   f"CHF {startkurs:.0f}")
col2.metric("Schlusskurs", f"CHF {schlusskurs:.0f}")
col3.metric("Rendite",     f"{rendite:.1f}%")

tage = list(range(252))

if rendite > 0:
    farbe = "green"
else:
    farbe = "red"

fig = px.line(
    x=tage,
    y=kurse,
    title="Kursverlauf 252 Handelstage",
    color_discrete_sequence=[farbe]
)
st.plotly_chart(fig, use_container_width=True)

with st.expander("💡 Was ist Volatilität?"):
    st.write("""
        Volatilität beschreibt wie stark eine Aktie schwankt.
        Eine hohe Volatilität bedeutet grosse, unvorhersehbare
        Kurssprünge nach oben und unten.
        Eine tiefe Volatilität bedeutet ruhige, stabile Kursbewegungen.
        Verschiebe den Slider und schau wie sich der Chart verändert!
    """)
