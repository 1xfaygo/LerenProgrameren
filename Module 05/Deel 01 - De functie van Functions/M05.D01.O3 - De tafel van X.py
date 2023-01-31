def tafel_function(aantal_vraag): 
    for x in range(1,11):
        print(f"{x} x {aantal_vraag} = {x*aantal_vraag}")
aantal_vraag = int(input("welke tafel wil je weten?"))
tafel_function(aantal_vraag)