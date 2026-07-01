import streamlit as st
import plotly.express as px
from utils.api_helfer import get_wechselkurs, get_wechselkurs_verlauf

st.title("💱 Live Wechselkurse")
st.write("Daten werden von api.frankfurter.app geladen.")

# Vier Währungen nebeneinander
col1, col2, col3, col4 = st.columns(4)
waehrungen = ["EUR", "USD", "GBP", "JPY"]
spalten = [col1, col2, col3, col4]

for col, ziel in zip(spalten, waehrungen):
    kurs = get_wechselkurs("CHF", ziel)
    if kurs is not None:
        col.metric(f"CHF → {ziel}", f"{kurs:.4f}")
    else:
        col.error(f"{ziel}: keine Verbindung")

st.divider()

# Verlauf der letzten 30 Tage
st.subheader("📈 Verlauf letzte 30 Tage")

ziel_waehrung = st.selectbox("Währung wählen", ["EUR", "USD", "GBP", "JPY"])

verlauf = get_wechselkurs_verlauf("CHF", ziel_waehrung, 30)

if verlauf is not None:
    daten = list(verlauf.items())
    daten.sort()
    daten_x = [d[0] for d in daten]
    daten_y = [d[1] for d in daten]

    fig = px.line(
        x=daten_x,
        y=daten_y,
        title=f"CHF/{ziel_waehrung} — letzte 30 Tage",
        labels={"x": "Datum", "y": f"Kurs ({ziel_waehrung})"}
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.error("Keine Verbindung zur API. Bitte prüfe deine Internetverbindung.")

with st.expander("💡 Was ist ein Wechselkurs?"):
    st.write("""
        Ein Wechselkurs zeigt wie viel eine Währung in einer anderen wert ist.
        CHF/EUR = 0.95 bedeutet: 1 Schweizer Franken = 0.95 Euro.
        Wechselkurse ändern sich sekündlich durch Angebot und Nachfrage.
        Wenn du im Ausland einkaufst oder Aktien in USD kaufst,
        beeinflusst der Wechselkurs deinen effektiven Preis.
    """)

with st.expander("💡 Was ist eine API?"):
    st.write("""
        API = Application Programming Interface.
        Eine API ist eine Schnittstelle über die Programme miteinander
        kommunizieren können. Wir schicken eine Anfrage an
        api.frankfurter.app und bekommen die Wechselkurse als JSON zurück.
        JSON ist ein Textformat das strukturierte Daten überträgt —
        genau wie ein Dictionary in Python.
    """)
