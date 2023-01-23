import random # ik import dit om de random.shuffle te gebruiken


naam_list = [] # ik maak een lege list om namen in te doen
vraag = ""#maak een lege string met de naam vraag
while True: # een while loop om de vragen opnieuw te laten vragen tot dat gezegd is om te stoppen
        vraag = input("voer een naam in:")
        if vraag in naam_list:# controleert of de ingevoerde naam al in de lijst met namen staat.
            print("naam zit er al in kies een andere naam")#dit print hij als er 2 dezelfde namen ingevoerd is
        else:#als dat niet zo is
            naam_list.append(vraag)# voegdt hij de naam toe bij de lijst
            print("Naam toegevoed aan de lijst")# print dat de naam is toegevoegd aan de lijst
            if len(naam_list) >= 3:# als de lijst gelijk of groter dan 3
                nog_een_naam = input("wil je nog een naam toevoegen? (ja/nee)")#vraag hij of je nog een naam wilt toevoegen

               

                if nog_een_naam.lower() != "ja":#als er op de vraag nee is ingevoerd
                    random.shuffle(naam_list)# dan husseldt hij de namen lijst
                    for x in range(len(naam_list)):
                        print(f"{naam_list[x]} heet het lootje van {naam_list[x-1]}")
                    break
