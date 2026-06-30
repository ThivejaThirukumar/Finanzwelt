import streamlit as st
import plotly.express as px
from utils.berechnungen import berechne_rendite, berechne_gewinn

st.title("💼 Portfolio-Rechner")
st.subheader("Deine Aktien eingeben")

col1, col2, col3 = st.columns(3)

with col1:
    name1 = st.text_input("Aktie 1 Name", "Apple")
    name2 = st.text_input("Aktie 2 Name", "Nestlé")
    name3 = st.text_input("Aktie 3 Name", "Novartis")

with col2:
    start1 = st.number_input("Kaufkurs Aktie 1", value=100.0)
    start2 = st.number_input("Kaufkurs Aktie 2", value=80.0)
    start3 = st.number_input("Kaufkurs Aktie 3", value=60.0)

with col3:
    end1 = st.number_input("Aktueller Kurs Aktie 1", value=150.0)
    end2 = st.number_input("Aktueller Kurs Aktie 2", value=90.0)
    end3 = st.number_input("Aktueller Kurs Aktie 3", value=55.0)

aktien_namen = [name1, name2, name3]
starts = [start1, start2, start3]
ends = [end1, end2, end3]
werte = ends  # Aktueller Wert je Aktie für Pie-Chart

renditen = [berechne_rendite(s, e) for s, e in zip(starts, ends)]

fig = px.pie(names=aktien_namen, values=werte, title="Portfolio-Verteilung")
st.plotly_chart(fig, use_container_width=True)

fig2 = px.bar(x=aktien_namen, y=renditen, title="Rendite je Aktie (%)",
              color=renditen, color_continuous_scale="RdYlGn")
st.plotly_chart(fig2, use_container_width=True)
