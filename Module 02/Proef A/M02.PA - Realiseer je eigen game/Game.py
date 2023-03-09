# een functie maken die je vraagt of je opnieuw wilt spelen
# een teller bij toe te voegen dat laat zien hoeveel keer je hebt gewonnen en veloren
# 2 extra eindes toevoegen 1 win en 1 los scenario

def stop():
    while True:
        invoer = input("Wil je nog een keer spelen? (ja/nee):")
        if invoer == "nee":
            return True
        elif invoer == "ja":
            return False
        else:
            print("Ongeldige invoer, kies 'ja' of 'nee'.")

Game_won_teller = 0

stoppen = 0

while stoppen < 1:
    print(f"je hebt {Game_won_teller} keer gewonnen")
    print("Je wordt wakker en je moet naar school.")
    while True:
        opstaan = input("(1)Ga je vandaag naar school of (2)meld je zelf ziek?")

        if opstaan == "1":
                print("Je loopt naar de douche.")

                douchevraag= input("Ga je vandaag douchen? (ja/nee)").lower()
                if douchevraag == "ja":

                    shampoovraag = input("Ga je shampoo gebruiken. (ja/nee)").lower()
                    if shampoovraag == "ja":
                        print("Je gaat vandaag lekker ruiken.")
                    elif shampoovraag == "nee":
                        print("je gaat vandaag niet fris ruiken.")
                    else:
                        print("voer ja of nee in")

                elif douchevraag == "nee":
                    print("Gadverdamme je gaat ruiken naar een dode kat.")
                else:
                        print("voer ja of nee in")

                tandenpoesten = input("Ga jij je tandenpoetsen? (ja/nee)").lower()
                if tandenpoesten == "ja":
                    print("je adem ruikt vandaag fris.")

                elif tandenpoesten == "nee":
                    print("Je adem gaat vandaag ruiken naar bedorven ei.")
                else:
                    print("voer ja of nee in")

                kleding = int(input("Je gaat je omkleden welke outfit kies je (1/2)"))

                if kleding == 1:
                    print("je een confortabele trainingspak gekozen")
                elif kleding == 2:
                    print("je hebt en hoodie en spijkerbroek aan gedaan.")
                else:
                    print("voer ja of nee in")
                print("je pak je spullen en stapt uit huis")
                vervoer = input("wat voor vervoer neem jij? ((1)fiets , (2)scooter , (3)OV?  [kies een getal]")
                if vervoer == 1:
                    print("je hebt de fiets gepakt en onderweg terwijl je overstak op in een dode hoek werd jij aangereden door een vrachtwagen. (slecht einde)")
                    print("helaas je dood gegaan [ GAME OVER! ]")
                    print(stop())
                    stoppen = 10

                elif vervoer == 2:
                    print("Je hebt de scooter gepakt en kwam veilig en optijd op school aan. (goed einde)")
                    print("gefeliciteerd  [ GAME WON! ]")
                    Game_won_teller +=1
                    print(stop())
                if stop() == 'nee':
                    stoppen = 10

                elif vervoer == 3:
                    print("Je hebt besloten om met het OV te gaan en je kwam op het trein station aan maar je trein is vertraagd met 30 minuten komt nu te laat op school aan. (slecht einde)")
                    print("helaas je hebt te laat gekomen [ GAME OVER! ]")
                    print(stop())
                if stop() == 'nee':
                    stoppen = 10
                else:
                        print("voer ja of nee in")


        if opstaan == "2":
            print("je bent thuisgebeleven omdat je geen zin had om naar school te gaan ")
            ontbijt = input("Met wat ga je mee ontbijten: Cornflakes of pannekoeken.").lower()
            if ontbijt == "cornflakes":
                print("Je hebt lekker ontbeten en gaat nu de hele dag gamen (goed einde)")
                input("Gefeliciteerd [ GAME WON! ]")
                Game_won_teller +=1
                print(stop())
                if stop() == 'nee':
                    stoppen = 10

            elif ontbijt == "pannekoeken":
                print("Je ging pannekoeken bakken maar de eieren die jij had gebruikt waren bedorven") 
                print("Nu heb je het al op dus heb nu buikpijn en zit de hele dag op de WC (slecht einde)")
                print("helaas je bent ziek geworden [ GAME OVER! ]")
                print(stop())
                if stop() == 'nee':
                    stoppen = 10
            else:
                print("voer ja of nee in")



