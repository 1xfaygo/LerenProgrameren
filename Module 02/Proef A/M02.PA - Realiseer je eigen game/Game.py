# een functie maken die je vraagt of je opnieuw wilt spelen
# een teller bij toe te voegen dat laat zien hoeveel keer je hebt gewonnen en veloren
# 2 extra eindes toevoegen 1 win en 1 los scenario
# de controle gaat via lijst dat aan de hand van aangegeven antwoorden check of het een goed antwoord is ingevuld
#############################
#lijst met alle kiesbare antwoorden
antwoorden = [1,2,'ja','nee']
############################

print("Je wordt wakker en je moet naar school.")
opstaan = int(input("(1)Ga je vandaag naar school of (2)meld je zelf ziek?"))
if opstaan == 1:
    print("Je loopt naar de douche.")
    while True:
        try:
            douchevraag= input("Ga je vandaag douchen? (ja/nee)").lower()
            if douchevraag == "ja":
                break
            shampoovraag = input("Ga je shampoo gebruiken. (ja/nee)").lower()
            if shampoovraag == "ja":
                print("Je gaat vandaag lekker ruiken.")
                break
            elif shampoovraag == "nee":
                print("je gaat vandaag niet fris ruiken.")
                break
            else:
                print("voer ja of nee in")
            if douchevraag == "nee":
                print("Gadverdamme je gaat ruiken naar een dode kat.")
                break
            tandenpoesten = input("Ga jij je tandenpoetsen? (ja/nee)").lower()
            if tandenpoesten == "ja":
                print("je adem ruikt vandaag fris.")
                break

            elif tandenpoesten == "nee":
                print("Je adem gaat vandaag ruiken naar bedorven ei.")
                break
        except NameError:
            print("voer ja of nee in")
# while True:
#     try:
#         kleding = int(input("Je gaat je omkleden welke outfit kies je (1/2)"))
#         if kleding == 1:
#             print("je een confortabele trainingspak gekozen")
#             break
#         elif kleding == 2:
#             print("je hebt en hoodie en spijkerbroek aan gedaan.")
#             break
#         else:
#             print("voer een getal in ")
#     except ValueError:
#                 print("voer 1 of 2 in")

# print("je pak je spullen en stapt uit huis")
# while True:
#     try:
#         vervoer = int(input("wat voor vervoer neem jij? ((1)fiets , (2)scooter , (3)OV?  [kies een getal]"))
#         if vervoer == 1:
#             print("je hebt de fiets gepakt en onderweg terwijl je overstak op in een dode hoek werd jij aangereden door een vrachtwagen. (slecht einde)")
#             print("helaas je dood gegaan [ GAME OVER! ]")
#             break

#         elif vervoer == 2:
#             print("Je hebt de scooter gepakt en kwam veilig en optijd op school aan. (goed einde)")
#             print("gefeliciteerd  [ GAME WON! ]")
#             break

#         elif vervoer == 3:
#             print("Je hebt besloten om met het OV te gaan en je kwam op het trein station aan maar je trein is vertraagd met 30 minuten komt nu te laat op school aan. (slecht einde)")
#             print("helaas je hebt te laat gekomen [ GAME OVER! ]")
#             break
#         else:
#             print("voer ja of nee in")
#     except ValueError:
#             print("voer een getal in")



# elif opstaan == 2:
# print("je bent thuisgebeleven omdat je geen zin had om naar school te gaan ")
# ontbijt = input("Met wat ga je mee ontbijten: Cornflakes of pannekoeken.").lower()
    #     if ontbijt == "cornflakes":
    #         print("Je hebt lekker ontbeten en gaat nu de hele dag gamen (goed einde)")
    #         print("Gefeliciteerd [ GAME WON! ]")

    #     elif ontbijt == "pannekoeken":
    #         print("Je ging pannekoeken bakken maar de eieren die jij had gebruikt waren bedorven") 
    #         print("Nu heb je het al op dus heb nu buikpijn en zit de hele dag op de WC (slecht einde)")
    #         print("helaas je bent ziek geworden [ GAME OVER! ]")

    #     else:
    #         print("voer ja of nee in")



