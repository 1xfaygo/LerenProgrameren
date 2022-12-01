vraag1 = int(input("hoeveel croisantjes wilt uw hebben?"))
croisant = vraag1
prijs_croisant = 0.39
vraag2 = int(input("hoveel stokbroden wilt uw hebben?"))
stokbrood = vraag2
prijs_stokbrood = 2,78
vraag3 = int(input("hoeveel kortingsbonnen heeft uw?"))
kortingsbon = (0.50 * vraag3)
uitkomst = (croisant + stokbrood - kortingsbon)
print(f"De feestlunch kost je bij de bakker {uitkomst} euro voor de {croisant} croissantjes en de {stokbrood} stokbroden als de {kortingsbon} euro aan kortingsbonnen nog geldig zijn!")
