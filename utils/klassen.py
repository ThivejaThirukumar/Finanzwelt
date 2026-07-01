import yfinance as yf
from utils.berechnungen import berechne_rendite


class UngueltigesSymbolError(Exception):
    pass


class Stock:
    def __init__(self, symbol, name, sektor):
        if not symbol.replace(".", "").isalpha():
            raise UngueltigesSymbolError(f"{symbol} ist kein gültiges Symbol")
        self.symbol = symbol
        self.name = name
        self.sektor = sektor
        self.kurshistorie = []

    def get_current_price(self):
        try:
            ticker = yf.Ticker(self.symbol)
            return ticker.fast_info["lastPrice"]
        except Exception:
            return None

    def calculate_return(self, startkurs):
        preis = self.get_current_price()
        if preis is None:
            return None
        return berechne_rendite(startkurs, preis)

    def __str__(self):
        return f"{self.name} ({self.symbol})"


class ETF(Stock):
    def __init__(self, symbol, name, ter):
        super().__init__(symbol, name, "ETF")
        self.ter = ter  # Total Expense Ratio in %

    def __str__(self):
        return f"{self.name} ETF (TER: {self.ter}%)"


class Transaction:
    def __init__(self, symbol, typ, anzahl, preis):
        self.symbol = symbol
        self.typ = typ        # "kauf" oder "verkauf"
        self.anzahl = anzahl
        self.preis = preis

    def __str__(self):
        return f"{self.typ.upper()} {self.anzahl}x {self.symbol} @ CHF {self.preis:.2f}"


class Portfolio:
    def __init__(self, name):
        self.name = name
        self.positionen = []
        self.transaktionen = []

    def add_stock(self, stock, anzahl, kaufkurs):
        self.positionen.append({
            "stock": stock,
            "anzahl": anzahl,
            "kaufkurs": kaufkurs
        })
        transaktion = Transaction(stock.symbol, "kauf", anzahl, kaufkurs)
        self.transaktionen.append(transaktion)

    def total_value(self):
        summe = 0
        for pos in self.positionen:
            preis = pos["stock"].get_current_price()
            if preis is not None:
                summe += preis * pos["anzahl"]
        return summe

    def total_return(self):
        gesamt_investiert = sum(
            pos["kaufkurs"] * pos["anzahl"]
            for pos in self.positionen
        )
        gesamt_wert = self.total_value()
        if gesamt_investiert == 0:
            return 0
        return (gesamt_wert - gesamt_investiert) / gesamt_investiert * 100

    def __str__(self):
        return f"Portfolio '{self.name}' — {len(self.positionen)} Positionen"


# Test
if __name__ == "__main__":
    apple = Stock("AAPL", "Apple", "Technologie")
    print(apple)

    msci = ETF("IWDA", "iShares World", 0.2)
    print(msci)

    p = Portfolio("Mein Portfolio")
    p.add_stock(apple, 10, 150.0)
    print(p)
    print(p.transaktionen[0])
