####################################################
#functie dat vraagt of je opnieuw wilt spelen

# def stop():
#     while True:
#         invoer = input("Wil je nog een keer spelen? (ja/nee):")
#         if invoer == "nee":
#             return True
#         elif invoer == "ja":
#             return False
#         else:
#             print("Ongeldige invoer, kies 'ja' of 'nee'.")


####################################################
#teller
Game_won_teller = 0
Game_won_teller +=1
########################################################
#functie die vanuit een lijst met antwoorden controleerd of het juiste antwoord is ingevoerd

# def antwoord_check():
#     antwoorden = [1, 2, 3,"ja","nee"]
#     if opstaan,douchevraag,shmapoovraag, in antwoorden:
#         break

# nog mee bezig
########################################################
#hoe de functie er ongeveer uit gaan zien
while True:
    try:
        lis = [2]
        invoer= int(input('voer een getal in'))
        if invoer in lis:
            print('test complete')
            break
        else:
            print('test failed')
    except ValueError:
        print("een getal!")
########################################################
#functie die vraagt of je elke keer opnieuw wilt spelen
def retry():
    opnieuw = input("wil je opnieuw spelen")
    