UITGRAVEN_M3 = 25   
AFVOEREN_M3 = 32.5
VOORRIJDKOSTEN_GROOTE = 20
VOORRIJDKOSTEN_AFSTAND = 50

lengte = float(input("wat is de Lengte? (in m)"))
breedte = float(input("wat is de Lengte? (in m)"))
diepte = float(input("wat is de Lengte? (in m)"))
afstand_klant = int(input("afstand in km"))
inhoud = round((lengte * breedte * diepte), 2)# inhoud in m3
kosten_uitgraven = inhoud * UITGRAVEN_M3
kosten_afvoeren = inhoud * AFVOEREN_M3
grond_verwerken = kosten_uitgraven * kosten_afvoeren

voorrijdkosten = 0
if inhoud < 20 and afstand_klant < 50:
    voorrijdkosten += 100 +1.25 * afstand_klant
elif inhoud >= 100 +1.25* afstand_klant:
    voorrijdkosten += 100 + 1.25 *afstand_klant

print(inhoud)
print(f"afvoeren + graven eur: {grond_verwerken:2f}:")

