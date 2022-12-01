naam = (input('wat is je naam en achternaam'))
straatnaam= (input('wat is de naam van je straat + je huisnummer'))
postcode= (input('wat is is je postcode'))
woonplaats= (input('wat is je woonplaats'))

adres= f'''----------------------------------------------------
|  Naam      : {naam}                
|  Adres     : {straatnaam}           
|  Postcode  : {postcode}                         
|  Woonplaats: {woonplaats}                          
----------------------------------------------------'''
print(adres)
