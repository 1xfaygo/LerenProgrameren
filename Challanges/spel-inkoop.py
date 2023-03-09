prijs_games = 24.95
korting = 0.4
def spel_calculator():
    inkoop_prijs = prijs_games * (1.00 - korting)
    invoer = float(input("hoeveel games heb je:"))
    totaal = inkoop_prijs *invoer
    verzendkosten = 1 + (invoer -1) * 0.25
    uitkomst_totaal = verzendkosten + totaal
    return uitkomst_totaal
print(spel_calculator())

