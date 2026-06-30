import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import pandas as pd

st.title("📡 Echte Börsenkurse")

symbol = st.text_input("Aktien-Symbol eingeben", "AAPL")
st.caption("Beispiele: AAPL = Apple, NESN.SW = Nestlé, NOVN.SW = Novartis, MSFT = Microsoft")

periode = st.selectbox("Zeitraum", ["1mo", "3mo", "6mo", "1y", "2y", "5y"], index=3)

if symbol:
    try:
        daten = yf.download(symbol, period=periode, auto_adjust=True)

        if daten.empty:
            st.error(f"Symbol '{symbol}' nicht gefunden. Bitte prüfe die Schreibweise.")
        else:
            # Gleitende Durchschnitte
            daten["MA20"] = daten["Close"].rolling(20).mean()
            daten["MA50"] = daten["Close"].rolling(50).mean()

            # Kennzahlen
            aktueller_kurs = float(daten["Close"].iloc[-1])
            erster_kurs    = float(daten["Close"].iloc[0])
            rendite        = (aktueller_kurs - erster_kurs) / erster_kurs * 100

            col1, col2, col3 = st.columns(3)
            col1.metric("Aktueller Kurs", f"${aktueller_kurs:.2f}")
            col2.metric("Rendite", f"{rendite:.1f}%")
            col3.metric("Datenpunkte", len(daten))

            # Candlestick Chart
            fig = go.Figure()

            fig.add_trace(go.Candlestick(
                x=daten.index,
                open=daten["Open"].squeeze(),
                high=daten["High"].squeeze(),
                low=daten["Low"].squeeze(),
                close=daten["Close"].squeeze(),
                name=symbol
            ))

            # MA20 hinzufügen
            fig.add_scatter(
                x=daten.index,
                y=daten["MA20"].squeeze(),
                name="MA 20 Tage",
                line=dict(color="orange", width=1.5)
            )

            # MA50 hinzufügen
            fig.add_scatter(
                x=daten.index,
                y=daten["MA50"].squeeze(),
                name="MA 50 Tage",
                line=dict(color="blue", width=1.5)
            )

            fig.update_layout(title=f"{symbol} — Kursverlauf", xaxis_rangeslider_visible=False)
            st.plotly_chart(fig, use_container_width=True)

            # Tabelle: letzte 10 Tage
            st.subheader("📋 Letzte 10 Handelstage")
            st.dataframe(daten[["Open","High","Low","Close","Volume"]].tail(10))

    except Exception as e:
        st.error(f"Fehler beim Laden der Daten: {e}")

with st.expander("💡 Was ist ein gleitender Durchschnitt?"):
    st.write("""
        Der gleitende Durchschnitt (MA) glättet den Kursverlauf.
        MA20 = Durchschnitt der letzten 20 Handelstage.
        MA50 = Durchschnitt der letzten 50 Handelstage.
        Wenn der Kurs über dem MA liegt → positiver Trend.
        Wenn der Kurs unter dem MA liegt → negativer Trend.
        Trader nutzen diese Linien um Kauf- und Verkaufssignale zu erkennen.
    """)

with st.expander("💡 Was ist ein Candlestick-Chart?"):
    st.write("""
        Jede Kerze zeigt 4 Werte eines Handelstages:
        Open = Eröffnungskurs, Close = Schlusskurs,
        High = Tageshöchstkurs, Low = Tagestiefstkurs.
        Grüne Kerze = Kurs gestiegen (Close > Open).
        Rote Kerze = Kurs gefallen (Close < Open).
    """)

