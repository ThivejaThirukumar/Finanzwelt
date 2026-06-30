import streamlit as st 
import random
import plotly.express as px 

startkurs = 100.0 
rendite = -100  # Startwert, garantiert < 20, damit die Schleife überhaupt startet

while rendite <= 20:
    kurse = [startkurs]
    for tag in range(251):
        veraenderung = random.gauss(0.0005, 0.015)
        neuer_kurs = kurse[-1] * (1 + veraenderung)
        kurse.append(neuer_kurs)
    
    hoechstkurs = max(kurse)
    tiefstkurs = min(kurse)
    schlusskurs = kurse[-1]
    rendite = (schlusskurs - startkurs) / startkurs * 100

print(rendite)