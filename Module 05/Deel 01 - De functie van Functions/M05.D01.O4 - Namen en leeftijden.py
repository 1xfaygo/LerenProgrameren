def namen_leeftijd():
        namen_leeftijddict = {}
        naam_vraag = input("wat is je naam?: ")
        leeftijd_vraag = input("hoe oud ben je?:")
        namen_leeftijddict['name'] = naam_vraag
        namen_leeftijddict['age'] = leeftijd_vraag
        return namen_leeftijddict

namen_leeftijdlist = []

while True:
    namen_leeftijdlist.append(namen_leeftijd())
    if input("Wil je nog een persoon toevoegen? (ja/nee").lower() == "nee":
        break
    
for x in namen_leeftijdlist:
     print(f"{x['name']} is {x['age']} jaar")