import random
score = 0
ronde = 0
te_raden_getal = random.randint(1,1000)
print(te_raden_getal)
while ronde <20 :
    teller = 0
    while teller != 10:
        geraden_getal = int(input("Raad een getal tussen 1 en 1000:"))
        if geraden_getal == te_raden_getal:
            print("geraden")
            score +=1
            teller = 10
        verschilsgetal = abs(te_raden_getal - geraden_getal)
        if te_raden_getal > geraden_getal:
            print("Hoger")
        elif te_raden_getal < geraden_getal:
            print("lager")
        if verschilsgetal <=20:
            print("je bent heel warm")
        elif verschilsgetal <=50:
            print("Je bent  warm")
    ronde +=1
    if ronde < 20:
        stopvraag = input("wil je nog verder spelen ja of nee")
        if stopvraag == "nee":  
            ronde= 20      
    print(f"je hebt {score} keer het getal geraden")           
# stap 1: raad 1 getal
# stap 2: 3 controles
# stap 3: programeer 1 ronde
# stap 4: programeer 20 roden
# stap 5: input maken
# stap 6: teller maken met score