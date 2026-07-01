import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from utils.daten_laden import (
    lade_aktien_daten,
    berechne_renditen,
    berechne_korrelation,
    berechne_jahresrenditen
)

st.title("🔬 Marktanalyse")
st.write("Echte Daten, echte Analysen — powered by pandas.")

# Aktien-Auswahl
symbole_input = st.text_input(
    "Aktien-Symbole (kommagetrennt)",
    "AAPL, MSFT, NESN.SW, NOVN.SW"
)
symbole = [s.strip() for s in symbole_input.split(",")]
periode = st.selectbox("Zeitraum", ["1y", "2y", "5y"], index=1)

if st.button("📥 Daten laden"):
    with st.spinner("Lade Daten von Yahoo Finance..."):
        df = lade_aktien_daten(symbole, periode)

    if df is None or df.empty:
        st.error("Keine Daten gefunden. Prüfe die Symbole.")
    else:
        st.success(f"Daten geladen: {len(df)} Handelstage")
        st.session_state["df"] = df
        st.session_state["symbole"] = symbole

if "df" in st.session_state:
    df = st.session_state["df"]
    symbole = st.session_state["symbole"]

    st.divider()

    # ── Kursverlauf mit gleitendem Durchschnitt ────────────────────────────────
    st.subheader("📈 Kursverlauf mit gleitendem Durchschnitt")

    schlusskurse = df["Close"]
    ma20 = schlusskurse.rolling(20).mean()
    ma50 = schlusskurse.rolling(50).mean()

    fig = go.Figure()
    for sym in schlusskurse.columns:
        fig.add_scatter(x=schlusskurse.index, y=schlusskurse[sym], name=sym)
    fig.update_layout(title="Schlusskurse", xaxis_title="Datum", yaxis_title="Kurs")
    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # ── Korrelations-Heatmap ───────────────────────────────────────────────────
    st.subheader("🌡️ Korrelation zwischen Aktien")

    df_renditen = berechne_renditen(df)
    korr = berechne_korrelation(df_renditen)

    fig2 = px.imshow(
        korr,
        title="Korrelationsmatrix — tägliche Renditen",
        color_continuous_scale="RdBu",
        zmin=-1, zmax=1
    )
    st.plotly_chart(fig2, use_container_width=True)

    st.divider()

    # ── Inflation vs. Aktienrendite ────────────────────────────────────────────
    st.subheader("💰 Kaufkraft: CHF 1'000 über die Zeit")

    inflation = {2019: 0.4, 2020: -0.7, 2021: 0.6, 2022: 2.8, 2023: 2.1, 2024: 1.1}

    startkapital = 1000.0
    kaufkraft_inflation = [startkapital]
    jahre = sorted(inflation.keys())

    for jahr in jahre:
        neuer_wert = kaufkraft_inflation[-1] * (1 - inflation[jahr] / 100)
        kaufkraft_inflation.append(neuer_wert)

    fig3 = px.line(
        x=[str(j) for j in [jahre[0] - 1] + jahre],
        y=kaufkraft_inflation,
        title="Kaufkraft CHF 1'000 (nach Inflation)",
        labels={"x": "Jahr", "y": "Wert (CHF)"}
    )
    st.plotly_chart(fig3, use_container_width=True)

    st.divider()

    # ── Letzte Daten als Tabelle ───────────────────────────────────────────────
    st.subheader("📋 Letzte 10 Handelstage")
    st.dataframe(df["Close"].tail(10).round(2))

with st.expander("💡 Was ist Korrelation?"):
    st.write("""
        Korrelation misst wie ähnlich sich zwei Aktien bewegen.
        +1.0 = sie bewegen sich immer gleich (perfekte Korrelation).
        -1.0 = sie bewegen sich immer entgegengesetzt.
        0.0  = kein Zusammenhang zwischen den Bewegungen.
        Für ein gutes Portfolio willst du tiefe Korrelation —
        wenn eine Aktie fällt, soll die andere nicht auch fallen.
        Das nennt man Diversifikation.
    """)

with st.expander("💡 Was ist Inflation?"):
    st.write("""
        Inflation bedeutet dass Preise über Zeit steigen.
        2% Inflation bedeutet: was heute CHF 100 kostet,
        kostet nächstes Jahr CHF 102.
        Dein Geld auf dem Konto wird also jedes Jahr weniger wert,
        auch wenn die Zahl gleich bleibt.
        Deshalb ist investieren so wichtig — Aktien schlagen
        langfristig die Inflation.
    """)
