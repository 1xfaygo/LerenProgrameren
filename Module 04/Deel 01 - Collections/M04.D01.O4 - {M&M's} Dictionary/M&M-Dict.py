import random
zak_dict = {}
lijst_kleur = ("rode","Blauwe","groene","gele","bruine")

inhoudsvraag = int(input("Hoeveel M&Ms moeten in de zak?:"))
aantalM_en_Ms = 1 #dit doe ik omdat ik niet geen range gebruik dus maak ik een teller zodat hij elke keer optelt hoveel m&ms er zijn
for x in range(inhoudsvraag):
    keuzekleur = random.choice(lijst_kleur)
    if keuzekleur not in zak_dict:
        zak_dict.update({keuzekleur:teller})
    else:
        zak_dict[keuzekleur] +=1

print(zak_dict)