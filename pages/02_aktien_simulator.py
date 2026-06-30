import streamlit as st 
import random
import plotly.express as px 

startkurs = 100.0 
kurse = []
kurse.append(startkurs)

for tag in range(251):
    veraenderung = random.gauss(0.0005, 0.015)
    neuer_kurs = kurse[-1] * (1 +veraenderung)
    kurse.append(neuer_kurs)

print(kurse)