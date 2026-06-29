import streamlit as st 

kapital = 1000.0
zinsatz = 0.25
jahre = 0.1

endkapital = kapital * (1 + zinsatz) ** jahre

if zinsatz > 0.20:
    print("Warnung: Zinsatz über 20% unrealistisch")
elif jahre < 1:
    print("Fehler mindestens 1 Jahr eingeben")
else: 
    print("Berechnung OK")

print(f"Endkapital:CHF {endkapital:.2f}")