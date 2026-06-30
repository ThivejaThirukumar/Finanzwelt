import streamlit as st
import plotly.express as px
import csv
import json
import pandas as pd

st.title("📂 Marktdaten")

# ── Dictionary: Aktien-Datenbank ──────────────────────────────────────────────
aktien_db = {
    "AAPL":  {"name": "Apple",    "sektor": "Technologie", "kurs": 189.0, "aktien": 1000},
    "NESN":  {"name": "Nestlé",   "sektor": "Konsum",      "kurs": 98.0,  "aktien": 2000},
    "NOVN":  {"name": "Novartis", "sektor": "Gesundheit",  "kurs": 87.0,  "aktien": 1500},
}

# Tuple: Stammdaten die sich nicht ändern
SEKTOREN = ("Technologie", "Finanzen", "Gesundheit", "Konsum", "Energie")

# ── Dictionary Iteration ───────────────────────────────────────────────────────
st.subheader("📋 Aktien-Datenbank")
for symbol, info in aktien_db.items():
    st.write(f"**{symbol}** — {info['name']} ({info['sektor']}) — CHF {info['kurs']:.2f}")

# ── Dict-Comprehension: Marktkapitalisierung ───────────────────────────────────
marktkapitalisierung = {
    symbol: info["kurs"] * info["aktien"]
    for symbol, info in aktien_db.items()
}

st.subheader("💰 Marktkapitalisierung")
for symbol, mk in marktkapitalisierung.items():
    st.write(f"{symbol}: CHF {mk:,.0f}")

# ── CSV schreiben ──────────────────────────────────────────────────────────────
kursdaten = [
    ["Datum",      "AAPL",  "NESN", "NOVN"],
    ["2024-01-01", 180.0,   95.0,   84.0],
    ["2024-02-01", 183.0,   96.5,   85.5],
    ["2024-03-01", 186.0,   97.0,   86.0],
    ["2024-04-01", 189.0,   98.0,   87.0],
]

with open("data/kurse.csv", "w", newline="") as f:
    csv.writer(f).writerows(kursdaten)

# ── CSV lesen ──────────────────────────────────────────────────────────────────
st.subheader("📄 Kursdaten aus CSV")
with open("data/kurse.csv", "r") as f:
    for row in csv.reader(f):
        st.write(row)

# ── JSON speichern & laden ─────────────────────────────────────────────────────
with open("data/portfolio.json", "w") as f:
    json.dump(aktien_db, f, indent=2)

with open("data/portfolio.json", "r") as f:
    geladene_daten = json.load(f)

st.subheader("🔄 Portfolio aus JSON geladen")
st.write(f"Anzahl Aktien im Portfolio: {len(geladene_daten)}")

# ── Streamlit: CSV Upload ──────────────────────────────────────────────────────
st.subheader("📤 Eigene CSV hochladen")
uploaded = st.file_uploader("CSV hochladen", type=["csv"])

if uploaded is not None:
    df = pd.read_csv(uploaded)
    st.dataframe(df)

    # Chart aus hochgeladenen Daten
    erste_spalte = df.columns[0]
    zahlen_spalten = df.select_dtypes(include="number").columns.tolist()

    if zahlen_spalten:
        fig = px.line(df, x=erste_spalte, y=zahlen_spalten,
                      title="Kursverlauf aus deiner CSV")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Keine Zahlenwerte in der CSV gefunden.")

with st.expander("💡 Was ist ein Dictionary?"):
    st.write("""
        Ein Dictionary speichert Daten als Schlüssel-Wert-Paare.
        Statt einer Liste wo du Positionen (0, 1, 2...) brauchst,
        kannst du direkt mit einem Namen zugreifen:
        aktien_db["AAPL"] gibt dir sofort alle Apple-Daten.
        Das ist viel lesbarer als aktien_db[0]!
    """)

with st.expander("💡 Was ist ein Tuple?"):
    st.write("""
        Ein Tuple ist wie eine Liste, aber unveränderlich.
        Du kannst nichts hinzufügen, löschen oder ändern.
        Perfekt für Daten die sich nie ändern sollen —
        wie eine Liste von Sektoren oder Länder-Codes.
    """)