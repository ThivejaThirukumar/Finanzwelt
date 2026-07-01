import streamlit as st

st.set_page_config(page_title="FinanzWelt", page_icon="💹")

st.title("💹 FinanzWelt")
st.write("Willkommen bei FinanzWelt! Wähle eine Seite im Menü links.")

st.subheader("Was kannst du hier machen?")

col1, col2 = st.columns(2)

with col1:
    st.info("📈 Zinseszins-Rechner\nBerechne wie dein Geld wächst")
    st.info("📊 Aktien-Simulator\nSimuliere Börsenkurse")
    st.info("💼 Portfolio-Rechner\nAnalysiere dein Portfolio")

with col2:
    st.info("📂 Marktdaten\nLade und analysiere CSV-Daten")
    st.info("📡 Echte Börsenkurse\nLive-Daten von Yahoo Finance")