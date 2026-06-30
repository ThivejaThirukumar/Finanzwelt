import streamlit as st
import plotly.express as px 

st.title("📈 Zinseszins-Rechner")

kapital = st.slider("Startkapital (CHF)", 100, 100000, 1000)
zinssatz = st.slider("Zinssatz pro Jahr", 0.0, 0.20, 0.05)
jahre = st.slider("Anzahl Jahre", 1, 50, 10)

endkapital = kapital * (1 + zinssatz) ** jahre
gewinn = endkapital - kapital

if zinssatz > 0.20:
    st.warning("Warnung: Zinssatz über 20% unrealistisch")
elif jahre < 1:
    st.error("Fehler: mindestens 1 Jahr eingeben")
else:
    st.metric("Endkapital", f"CHF {endkapital:,.0f}", f"+{gewinn:,.0f} CHF")


jahre_liste = list(range(0, jahre + 1)) # X werte 
werte = [kapital * (1 + zinssatz) ** j for j in jahre_liste] # Y Werte 
werte_ohne = [kapital + kapital*zinssatz*j for j in jahre_liste]

fig = px.line(x=jahre_liste, y=werte, title = "Wachstum mit Zinseszins")
fig.add_scatter(x = jahre_liste, y = werte_ohne, name = "Ohne Zinseszins")
st.plotly_chart(fig, use_container_width = True) 

with st.expander("Was ist Zinseszins?"):
    st.write("Zinseszins bedeutet dass du Zinsen auf deine Zinsen bekommst. " \
    "Im ersten Jahr verdienst du Zinsen nur auf dein Startkapital. " \
    "Aber im zweiten Jahr verdienst du Zinsen auf dein Startkapital UND auf die Zinsen vom ersten Jahr. " \
    "Das wiederholt sich jedes Jahr — und genau das lässt dein Geld immer schneller wachsen.")