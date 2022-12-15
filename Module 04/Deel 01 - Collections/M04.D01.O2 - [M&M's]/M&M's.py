import random

kleur =("oranje","blauwe","groene","bruine","paars")
zak =[]
zakvraag = int(input("hoeveel m&m's moeten er in de zak:"))
for x in range(zakvraag):
    keuze = random.choice(kleur)
    zak.append(keuze)
print(f"in de zak zitten de volgende m&ms in: ")
print(zak)