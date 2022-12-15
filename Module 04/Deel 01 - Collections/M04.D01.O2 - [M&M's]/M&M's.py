import random

kleur =("oranje","blauwe","groene","bruine")
zak =[]
zakvraag = input("hoeveel m&m's moeten er in de zak:")
for x in zakvraag:
    random = random.randint(0,3)
    zak.append(kleur[random])

print(f"in de zak zit {zakvraag} {zak} m&m in ")