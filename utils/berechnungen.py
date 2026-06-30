def berechne_rendite(startkurs, endkurs):
    return(endkurs - startkurs)

def berechne_gewinn(startkurs, endkurs, anzahl_aktien = 1):
    return(endkurs - startkurs) * anzahl_aktien

def berechne_sharpe(rendite, volatilitaet): 
    if volatilitaet == 0: 
        return 0 
    return rendite / volatilitaet

def portfolio_zusammenfassung(aktien_dict): 
    pass

print(berechne_rendite(100, 120))   # sollte 20.0 ausgeben
print(berechne_gewinn(100, 120, 5)) # sollte 100 ausgeben
print(berechne_sharpe(10, 2))       # sollte 5.0 ausgeben