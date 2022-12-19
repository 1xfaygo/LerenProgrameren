from fruitmand import fruitmand 
import random
vraag_aantal = int(input("voer een aantal:"))
for x in range(vraag_aantal):
    random_picker = random.randint(0,(len(fruitmand)-1))
    print(fruitmand[random_picker]['name'])