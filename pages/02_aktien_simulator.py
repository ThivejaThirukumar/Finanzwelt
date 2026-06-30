import streamlit as st 
import random
import plotly.express as px 

startkurs = 100.0 
rendite = -100  # Startwert, garantiert < 20, damit die Schleife überhaupt startet

while rendite <= 20:
    kurse = [startkurs]
    for tag in range(251):
        veraenderung = random.gauss(0.0005, 0.015)
        neuer_kurs = kurse[-1] * (1 + veraenderung)
        kurse.append(neuer_kurs)
    
    hoechstkurs = max(kurse)
    tiefstkurs = min(kurse)
    schlusskurs = kurse[-1]
    rendite = (schlusskurs - startkurs) / startkurs * 100

st.title("📊 Aktien-Simulator")
st.slider("Startkurs(CHF)", 10, 500, 100)
st.slider("Volatilität", 0.005, 0.05, 0.015)
random.gauss(0.005, vol)

col1, col2, col3 = st.columns(3)
col1.metric("startkurs", f"CHF {startkurs;.0f}")
col2.metric("Schlusskurs", f"CHF {startkurs:.0f}")
col3.metric("Rendite", f"{rendite:.1f}%")

tage = list(range(252))
fig = px.line(x = tage, y = kursem title = "Kursverlauf 252 Handelstage")
if > 0:
    color= "green"
else: 
    color = "red"

st.plotly_chart(fig, use_container_width=True)
st.expander("💡 Was ist Volatilität?") 