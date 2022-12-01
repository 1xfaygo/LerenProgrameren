from tokenize import Name
from unicodedata import name


print ("|_______________________________________________________________|")
print ("| Solicitatieformulier Circusdirecteur voor Circus HotelDeBotel |")
print ("|_______________________________________________________________|")
print ("| Er wordt u een aantal relevante vragen gesteld...             |")
print ("| Gelieve die naar eer en geweten in te vullen.                 |")
print ("| Als blijkt dat u aan de criteria voldoet dan komt u in        |")
print ("| aanmerking voor een serieus sollicitatiegesprek!              |")
print ("| Ontspan maar blijf wakker hier komen de vragen.               |")
print ("|_______________________________________________________________|")

Naam = input("Wat is uw Naam?:").lower()
if Naam == "jan":
    raise NameError('Jan is kapot lelijk dus hij is niet welkom!')
else:
    Geslacht = input("Ben uw een man of een vrouw?").lower()
if Geslacht == "trans":
    raise NameError('sikter lan opdonderen')
else:
    rijbewijs = input ("Bent u in bezit van een geldig Vrachtwagen rijbewijs? J/N:").lower()
    Diploma = input("Bent uw in bezit van een MBO niveau-4 Ondernemen? J/N").lower()
    Hoed= input("bent uw in bezit van een hoge hoed? J/N").lower()

if Geslacht == "man":
    snor = input ("Heeft uw een snor? J/N").lower()
    if snor == "ja":
        snorlenget = int(input("hoelang is uw snor? (in cm):"))

    elif Geslacht == "vrouw":
        krullen = int(input("Hoelang is uw rood krullend haar? (in cm):"))
        if krullen == "ja":
            krullenLengte = int(input("Hoelang is uw rood krullend haar? (in cm):"))


lengte = int(input("hoe lang ben uw? (in cm):"))
gewicht = int(input ("Wat is uw gewicht? (in kg):"))
if gewicht > 100:
    raise NameError ('ga naar de gym dikzak')
else:
    certificaat = input ("Heeft u een overleven met een gevaarlijk persoon certificaat? J/N:")
tafeldiploma = input ("Heeft u een tafeldiploma? J/N:")
neus = int(input("Hoelang is uw neus? (in cm):"))
teennagel = input (" knipt uw een rechter teennagel? J/N:")
praktijk = int(input("Hoeveel jaar heeft u praktijkervaring met dieren-dressuur?:"))

if praktijk > 4 and Diploma.lower() == "ja" and rijbewijs.lower() == "ja" and Hoed.lower() == "ja" and (Geslacht == "vrouw" and krullen.lower() == "ja" and  krullenLengte > 20) or (Geslacht == "man" and snor.lower() == "ja" and snorlenget > 10) and lengte > 150 and gewicht > 90 and certificaat.lower() == "ja" and tafeldiploma.lower() == "ja" and neus.lower() == "ja" and teennagel.lower() == "ja":
    print ("gefeliciteerd! U komt in aanmerking voor een sollicitatiegesprek, stuur snel uw CV!")
else:
     print ("U voldoet niet aan onze strenge eisen voor de functie van Circusdirecteur, het spijt ons!")