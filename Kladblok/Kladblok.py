#als je print gebruikt je aleen maar bij een string comma's aan het begin en eind en de rest niet
#tussenhaakje vertel je wat je wilt printen
#multilijn zijn meerdere lijnen
#input is altijd een string
# bv PRIJS is een constante
# in  en not 
# boolean is true of false
#!= is niet gelijk aan en == is gelijk aan
# in zoekt of iets er IN zit
#break  stopt een loop
# try betekend begin deze progamma 
#een functie 
#def kan je een eigeen functie maken 
#return is antoord krijgen op mijn functie
#ascii is een lijst voor waarde van iets in '' 
# een constante is een variablen die niet veranderd
# een condidtie is bijvoorbeeld x > 
#while is een keuze
#teller = 0
# operator not,and,or
# int,float,bool,list,
# not betekend False
# met remove haal je een element weg en met de pop haal je de element nummer weg
# de insert is iets toevoegen aan het begin van een list
# append is iets toevoegen aan een list en pop en remove is iets weghalen
# type geeft het  datatype terug van de ding
#  een list begint bij 0
# if antwoord in list print het altijd true
# antwoord = input("voer ja of nee")




































# programma wat om namen vraagt, om leeftijden vraagt
# dit opslaat in een dict vervolgens de hoogste leeftijd print. 
# mijn_namen_dict = {}

# while True:
#     naam = input("wat is je naam? (stop om te stoppen)")

#     if naam == "stop":
#         break
#     # controle of naam er in zit
#     if naam in mijn_namen_dict:
#         if input("wilt uw bijwerken? (ja/nee)") != "ja":
#             continue
#     leeftijd = int(input("Wat is je leeftijd:"))

#     # controle of iemand met de zelfde leeftijd in zit
#     if leeftijd in mijn_namen_dict.values():
#         for n,l in mijn_namen_dict.items():
#             if l == leeftijd:
#                 break 
#         print(f"{n}is al zo oud")
#         if input("toch doorgaan? ja/nee") != "ja":
#             continue

#     # update of mijwerken van dictionary
#     # mijn_namen_dict[naam] = leeftijd
#     mijn_namen_dict.update({naam : leeftijd})

# print(mijn_namen_dict)
# leeftijd_lijst = list(mijn_namen_dict.values())
# namen_lijst = list(mijn_namen_dict.keys()) 
# print(f"de leeftijd van iedereen {leeftijd_lijst}")
# print(f"de oudeste persoon is :{namen_lijst[leeftijd_lijst.index(max(leeftijd_lijst))]}")















# while antwoord not in ("ja ,  nee"):
#     print("het is goed")

# while True:
#     antwoord = input("voer ja of nee")
#     if antwoord in ("ja ,  nee"):
#         break

# mijn_dictr = {
#     123456789: "een",
#     123456788: "twee",
#     123456787: "drie",
#     123456786: "vier"
# }
# for val in mijn_dictr.values():
#     print(val)

# for x in mijn_dictr.keys():
#     print(x)

# print(dir(mijn_dictr))
# print("")
# mijn_list = [1]

# print(dir(mijn_list))












# de functie vraagt aan de gebruiker en geeft deze terug
# def vraag_een_getal(vraag: str) -> int: # betekend defineer = maak aan
#     while True:
#         try:
#             leeftijd = int(input(vraag))
#             break
#         except ValueError:
#             print("je moet wel een getal invoeren")
#             continue
#     return leeftijd




# leeftijd = vraag_een_getal("voer leeftijd in:")

#functie die teruggeeft: "hallo naam" 
# def naam_stellen(vraag: str) -> str:
#     naam = input(antwoord)
#     return naam
# antwoord = naam_stellen("voer je naam")#functieaanroep












# def geeft_naam_met_hallo(n: str)-> str:
#     zin = f"hallo {n}"
#     return zin

# antwoord = geeft_naam_met_hallo("yassine")
# print(antwoord)






















# def vraag_om_letter(vraag:str) -> str:
#     while True:
#         leter = input(vraag)
#         if len(leter) > 1:
#             print("je moet wel een leter invoeren")
#         else:
#             return leter
# print(vraag_om_letter('voer een letter in:'))















# geboorte_jaar = vraag_een_getal("voer geboorte jaar in:")
# geboorte_maand = vraag_een_getal("voer geboorte maand in:")
# geboorte_dag =vraag_een_getal("voer geboorte dag in:")

# print(leeftijd)




# begint met 5 vermingvuldig met 3 tot 1000 is bereikt
def keer_drie(getal: int, max:int) ->int:
    if getal>=max:
        return getal
    else:
        getal *= 3
        return keer_drie(getal, max)





# 15
# 45
# 135





