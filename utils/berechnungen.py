def berechne_rendite(startkurs, endkurs):
    return (endkurs - startkurs) / startkurs * 100

def berechne_gewinn(startkurs, endkurs, anzahl_aktien=1):
    return (endkurs - startkurs) * anzahl_aktien

def berechne_sharpe(rendite, volatilitaet): 
    if volatilitaet == 0: 
        return 0 
    return rendite / volatilitaet

def portfolio_zusammenfassung(aktien_dict): 
    pass