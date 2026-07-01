import streamlit as st
import plotly.express as px
from utils.klassen import Stock, ETF, Portfolio, UngueltigesSymbolError
from utils.berechnungen import berechne_rendite

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

renditen = [berechne_rendite(s, e) for s, e in zip(starts, ends)]

# Portfolio-Objekt erstellen
portfolio = Portfolio("Mein Portfolio")

try:
    a1 = Stock("AAPL", name1, "Technologie")
    a2 = Stock("NESN", name2, "Konsum")
    a3 = Stock("NOVN", name3, "Gesundheit")
    portfolio.add_stock(a1, 10, start1)
    portfolio.add_stock(a2, 10, start2)
    portfolio.add_stock(a3, 10, start3)
except UngueltigesSymbolError as e:
    st.error(f"Fehler: {e}")

st.subheader("📊 Charts")

fig = px.pie(
    names=aktien_namen,
    values=ends,
    title="Portfolio-Verteilung"
)
st.plotly_chart(fig, use_container_width=True)

fig2 = px.bar(
    x=aktien_namen,
    y=renditen,
    title="Rendite je Aktie (%)",
    color=renditen,
    color_continuous_scale="RdYlGn"
)
st.plotly_chart(fig2, use_container_width=True)

st.subheader("📋 Transaktions-History")
for t in portfolio.transaktionen:
    st.write(str(t))

with st.expander("💡 Was ist OOP?"):
    st.write("""
        OOP = Objektorientierte Programmierung.
        Statt einzelner Variablen und Funktionen bündeln wir
        zusammengehörige Daten und Funktionen in einer Klasse.
        Eine Klasse ist wie eine Vorlage — z.B. "Stock".
        Ein Objekt ist eine konkrete Instanz davon — z.B. "Apple-Aktie".
        So bleibt der Code übersichtlich wenn das Projekt wächst.
    """)
