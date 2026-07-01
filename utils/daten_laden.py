import yfinance as yf
import pandas as pd


def lade_aktien_daten(symbole, periode="2y"):
    """Lädt historische Kursdaten für eine Liste von Symbolen."""
    try:
        df = yf.download(symbole, period=periode, auto_adjust=True)
        return df
    except Exception:
        return None


def berechne_renditen(df):
    """Berechnet tägliche prozentuale Renditen aus Schlusskursen."""
    schlusskurse = df["Close"]
    return schlusskurse.pct_change().dropna()


def berechne_korrelation(df_renditen):
    """Berechnet die Korrelationsmatrix zwischen Aktien."""
    return df_renditen.corr()


def berechne_jahresrenditen(df):
    """Berechnet die Rendite pro Jahr für jede Aktie."""
    schlusskurse = df["Close"]
    schlusskurse.index = pd.to_datetime(schlusskurse.index)
    jaehrlich = schlusskurse.resample("YE").last()
    return jaehrlich.pct_change().dropna() * 100


# Test
if __name__ == "__main__":
    df = lade_aktien_daten(["AAPL", "MSFT"], periode="1y")
    if df is not None:
        print(df["Close"].tail(5))
