import random
zak_dict = {}
lijst_kleur = ("rode","Blauwe","groene","gele","bruine")

inhoudsvraag = int(input("Hoeveel M&Ms moeten in de zak?:"))
aantalM_en_Ms = 1 #dit doe ik omdat ik niet geen range gebruik dus maak ik een teller zodat hij elke keer optelt hoveel m&ms er zijn
for x in range(inhoudsvraag):
    random_kleur = random.choice(lijst_kleur) # jouke: let op gebruik variabelen namen, zit op meer plekken!!!
    if random_kleur not in zak_dict:
        zak_dict.update({random_kleur : aantalM_en_Ms})
    else:
        zak_dict[random_kleur] +=1

print(zak_dict)
