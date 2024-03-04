class Bankomat:
    def __init__(self):
        self.kontostand = 0

    def einzahlen(self, betrag):
        self.kontostand += betrag
        print(f"{betrag} Euro wurden eingezahlt. Neuer Kontostand: {self.kontostand} Euro")

    def abheben(self, betrag):
        if betrag <= self.kontostand:
            self.kontostand -= betrag
            print(f"{betrag} Euro wurden abgehoben. Neuer Kontostand: {self.kontostand} Euro")
        else:
            print("Nicht genügend Geld auf dem Konto!")

    def kontostand_anzeigen(self):
        print(f"Aktueller Kontostand: {self.kontostand} Euro")


bankomat = Bankomat()

while True:
    print("\nBankomat-Simulation:")
    print("1. Einzahlen")
    print("2. Abheben")
    print("3. Kontostand anzeigen")
    print("4. Beenden")

    auswahl = input("Bitte wählen Sie eine Option (1-4): ")

    if auswahl == "1":
        betrag = float(input("Geben Sie den Einzahlungsbetrag ein: "))
        bankomat.einzahlen(betrag)
    elif auswahl == "2":
        betrag = float(input("Geben Sie den Abhebungsbetrag ein: "))
        bankomat.abheben(betrag)
    elif auswahl == "3":
        bankomat.kontostand_anzeigen()
    elif auswahl == "4":
        print("Vielen Dank für die Nutzung des Bankomaten. Auf Wiedersehen!")
        break
    else:
        print("Ungültige Auswahl. Bitte wählen Sie eine Option von 1 bis 4.")
