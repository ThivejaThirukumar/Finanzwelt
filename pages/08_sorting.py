import streamlit as st
import plotly.express as px
import timeit
import random
from utils.algorithmen import insertion_sort, quicksort

st.title("⚡ Sorting-Algorithmen")
st.write("Wie schnell können Computer sortieren? Und warum ist der Algorithmus wichtig?")

st.divider()

# ── Aktien nach Rendite sortieren ─────────────────────────────────────────────
st.subheader("📊 Aktien sortieren")

aktien = {
    "Apple":    15.3,
    "Nestlé":   -2.1,
    "Novartis":  8.7,
    "Microsoft": 22.4,
    "Google":    11.2,
    "Amazon":   -5.8,
    "Tesla":    31.0,
    "Roche":     4.5,
}

sortier_kriterium = st.selectbox(
    "Sortieren nach",
    ["Rendite aufsteigend", "Rendite absteigend", "Name (A-Z)"]
)

namen = list(aktien.keys())
renditen = list(aktien.values())

if sortier_kriterium == "Rendite aufsteigend":
    sortiert = sorted(zip(renditen, namen))
    namen_sort = [x[1] for x in sortiert]
    renditen_sort = [x[0] for x in sortiert]
elif sortier_kriterium == "Rendite absteigend":
    sortiert = sorted(zip(renditen, namen), reverse=True)
    namen_sort = [x[1] for x in sortiert]
    renditen_sort = [x[0] for x in sortiert]
else:
    namen_sort = insertion_sort(namen)
    renditen_sort = [aktien[n] for n in namen_sort]

fig = px.bar(
    x=namen_sort,
    y=renditen_sort,
    title=f"Aktien — {sortier_kriterium}",
    color=renditen_sort,
    color_continuous_scale="RdYlGn",
    labels={"x": "Aktie", "y": "Rendite (%)"}
)
st.plotly_chart(fig, use_container_width=True)

st.divider()

# ── Performance-Vergleich ──────────────────────────────────────────────────────
st.subheader("⏱️ Performance-Vergleich")
st.write("Wie lange braucht jeder Algorithmus für verschiedene Datenmengen?")

n = st.slider("Anzahl Elemente (n)", 10, 2000, 500)

test_daten = [random.random() for _ in range(n)]

# Zeiten messen
zeit_insertion = timeit.timeit(
    lambda: insertion_sort(test_daten),
    number=5
) / 5 * 1000

zeit_quicksort = timeit.timeit(
    lambda: quicksort(test_daten),
    number=5
) / 5 * 1000

zeit_python = timeit.timeit(
    lambda: sorted(test_daten),
    number=5
) / 5 * 1000

algorithmen = ["Insertion Sort\nO(n²)", "Quicksort\nO(n log n)", "Python sorted()\nO(n log n)"]
zeiten = [zeit_insertion, zeit_quicksort, zeit_python]
farben = ["#E24B4A", "#EF9F27", "#639922"]

fig2 = px.bar(
    x=algorithmen,
    y=zeiten,
    title=f"Laufzeit bei n={n} Elementen",
    labels={"x": "Algorithmus", "y": "Zeit (Millisekunden)"},
    color=algorithmen,
    color_discrete_sequence=farben
)
st.plotly_chart(fig2, use_container_width=True)

col1, col2, col3 = st.columns(3)
col1.metric("Insertion Sort", f"{zeit_insertion:.3f} ms")
col2.metric("Quicksort",      f"{zeit_quicksort:.3f} ms")
col3.metric("Python sorted()", f"{zeit_python:.3f} ms")

if n > 500:
    faktor = zeit_insertion / max(zeit_quicksort, 0.001)
    st.info(f"Insertion Sort ist bei n={n} etwa **{faktor:.0f}x langsamer** als Quicksort!")

with st.expander("💡 Was ist Big-O Notation?"):
    st.write("""
        Big-O beschreibt wie die Laufzeit eines Algorithmus
        mit der Datenmenge wächst.

        O(n²) — Insertion Sort:
        Bei 10 Elementen: 100 Schritte.
        Bei 100 Elementen: 10'000 Schritte.
        Bei 1'000 Elementen: 1'000'000 Schritte!
        Die Laufzeit explodiert quadratisch.

        O(n log n) — Quicksort:
        Bei 10 Elementen: ~33 Schritte.
        Bei 100 Elementen: ~664 Schritte.
        Bei 1'000 Elementen: ~9'966 Schritte.
        Viel besser!

        Python's eingebautes sorted() ist in C implementiert
        und deshalb nochmals viel schneller als unser Python-Quicksort —
        aber der Algorithmus dahinter (Timsort) ist ebenfalls O(n log n).
    """)

with st.expander("💡 Wie funktioniert Insertion Sort?"):
    st.write("""
        Insertion Sort funktioniert wie Karten sortieren in der Hand.
        Du nimmst eine Karte nach der anderen und schiebst sie
        an die richtige Stelle zwischen den bereits sortierten Karten.
        Einfach zu verstehen, aber langsam bei vielen Elementen.
    """)

with st.expander("💡 Wie funktioniert Quicksort?"):
    st.write("""
        Quicksort wählt ein "Pivot"-Element (z.B. das mittlere).
        Alle kleineren Elemente kommen links, alle grösseren rechts.
        Dann wird dasselbe rekursiv auf links und rechts angewendet.
        Teile und herrsche — deshalb so viel schneller!
    """)
