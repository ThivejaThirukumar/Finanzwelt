import datetime
import requests


def get_wechselkurs(basis, ziel):
    """Gibt den aktuellen Wechselkurs von basis zu ziel zurück."""
    try:
        url = f"https://api.frankfurter.app/latest?from={basis}&to={ziel}"
        response = requests.get(url, timeout=5)
        daten = response.json()
        return daten["rates"][ziel]
    except requests.ConnectionError:
        return None
    except Exception:
        return None


def get_wechselkurs_verlauf(basis, ziel, tage=30):
    """Gibt historische Wechselkurse der letzten X Tage zurück."""
    try:
        ende = datetime.date.today()
        start = ende - datetime.timedelta(days=tage)
        url = f"https://api.frankfurter.app/{start}..{ende}?from={basis}&to={ziel}"
        response = requests.get(url, timeout=5)
        daten = response.json()
        verlauf = {
            datum: werte[ziel]
            for datum, werte in daten["rates"].items()
        }
        return verlauf
    except Exception:
        return None


# Test
if __name__ == "__main__":
    kurs = get_wechselkurs("CHF", "EUR")
    print(f"CHF/EUR: {kurs}")
