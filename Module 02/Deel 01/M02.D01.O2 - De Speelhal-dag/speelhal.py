vraag1 = int(input("Met hoeveel personen bent je?"))
vraag2 = int(input("hoe lang blijf je?"))
personen = vraag1
tijd = vraag2
prijs = 0.39 
toegangsticket = 7.45

totaal = toegangsticket * personen + tijd *prijs 
print(f"voor {tijd} min vip-Vr-seat")
 
print(f"Dit geweldige dagje-uit met {personen} mensen in de Speelhal met {tijd} minuten VR kost je maar {totaal} euro")