import time
inventory = []
items = {}
def opnieuw():
    while True:
        try:
            keuze_6 = int(input("(1)ja of (2)nee"))
            if keuze_6 == 1:
                time.sleep(2)
                print("je wordt opnieuw geladen")
                break
            else:
                print("kies uit de gegeven opties")
        except ValueError:
            print("voer een getal in ")
print("----------------------")
print("-----PRISON-ESCAPE----")
print("----------------------")
print("")
time.sleep(1)
print("je wordt wakker in een verlaten gevangenis cel en je hebt geen herrinering van waar je bent.")
print("")
time.sleep(3)
print("je loopt de cel uit en kijk om je heen en in de verte zie je een bordje staan met wat tekst.")
print("")
time.sleep(2)
while True:
    try:
        keuze_1 = int(input("(1)ga je naar het bordje lopen of (2)je omgeving verkennen"))
        time.sleep(2)
        if keuze_1 == 1:
            time.sleep(2)
            print("onderweg lopen naar de bordje die je in de verte zag stapte op wat gebroken glas dat een harde geluid maakte,")
            break
        else:
            print("kies uit de gegeven opties")
    except ValueError:
        print("voer een getal in ")
print("")
print("Uit shock stond je stil en hoorde je voetstappen jou kant komen dus verstopt je zo snel mogelijk als je kan.")
print("")
time.sleep(3)
print("je hebt je verstopt onder een cel-bed en ziet een groep van 10 zwaar bewapende criminelen die de binnenplaats binnenstormen")
print("")
time.sleep(2)
print("Wat doe je nu")
while True:
    try:
        keuze_2 = int(input("(1) blijf je onder het bed liggen of (2)waag je een poging om te ontsnappen"))
        time.sleep(2)
        if keuze_2 == 1:
            time.sleep(3)
            print("De leider comandeerd alle anderen mannen om te gaan zoeken naar jou dus verlaten ze allemaal de binnenplaats om jou te zoeken")
            break
        else:
            print("kies uit de gegeven opties")
    except ValueError:
        print("voer een getal in ")
print("")
print("je wacht af tot dat je iedereen de binnenplaats hoordt weg gaat")       
time.sleep(2) 
print("")
print("je kuipt onder het bed vandaan en loop de cel uit")
print("")
print("je kijkt voorzichtig uit de cel deur en loopt naar buiten en loopt naar het bordje die je eerder zag")
print("")
print("je loopt dor de gang heen en komt langs de bewakings kamer en vind daar 2 dode bewakers ")
print("")
while True:
    try:
        keuze_3 = int(input("(1) ga je de beveilegings kamer in  of (2)loop je door"))
        time.sleep(2)
        if keuze_3 == 1:
            time.sleep(2)
            print("je loopt de beveilegings kamer in en checkt beide lichamen om te checken of ze iets bij hun hadden en 1 van de 2 beveiligers had een wapen op zich")
            break
        else:
            print("kies uit de gegeven opties")
    except ValueError:
        print("voer een getal in ")
print("")
while True:
    try:
        keuze_4 = int(input("(1) pak je het wapen op  of (2) laat je hem liggen en loopt de kamer uit "))
        time.sleep(2)
        if keuze_4 == 1:
            time.sleep(2)
            print("je hebt de wapen opgepakt en en in je broekzak gedaan")
            items['wapon'] = "Glock 12"
            inventory.append(items)
            for wapen in items:
                print(f"{items['wapon']}  HAS BEEN ADDED TO YOUR INVENTORY")
            break
        else:
            print("kies uit de gegeven opties")
    except ValueError:
        print("voer een getal in ")
print("")
print("je loopt de kamer uit en loopt langs de donkere gangen wat dood loopt met een deur aan je rechter kant ")
print("")
print("je komt bij een deur aan en je hoort een stem vanuit de deur")
print("")
time.sleep(2)
print("je hoort een stem zeggen: 'je hebt geen keuze je moet de deur openen'")
print("")
time.sleep(2)
while True:
    try:
        keuze_5 = int(input("(1)doe je de deur open of (2)loop je langzaam van de deur vandaan"))
        if keuze_5 == 1:
            time.sleep(2)
            print("je doet de deur open en er komt een man met een mes op je af en hij steekt je neer")
            break
        else:
            print("kies uit de gegeven opties")
    except ValueError:
        print("voer een getal in ")
print("")
print("je bent dood")
print("")  
time.sleep(2)
print("GAME OVER")
print("")
time.sleep(2)
print("Wil je opnieuw spelen")
opnieuw()
