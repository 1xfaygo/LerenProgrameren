vragen = [{
    'vraag1': "(1) blijf je onder het bed liggen of (2)waag je een poging om te ontsnappen: ",
    'vraag2': "(1)ga je de beveilegings kamer in  of (2)loop je door: ",
    'vraag3': "(1) ga je naar boven of (2)ga je naar beneden",
    'verhaal1':'De leider comandeerd alle anderen mannen om te gaan zoeken naar jou dus verlaten ze allemaal de binnenplaats om jou te zoeken',
    'verhaal2':'je bent bent neer geschoten',
    'vervolg1': 'je loopt door de lange gang heen',
    'vervolg2':"pak je de wapon op? (1)ja of (2)nee: ",
    'vervolg3':'(1)ga je terug of (2)loop je door'
}]

def game(scenario):
    antwoord = int(input(scenario['vraag1']))
    if antwoord == 1:
        print(scenario['verhaal1'])
        print(scenario['vervolg1'])
        antwoord = int(input(scenario['vervolg3']))
        if antwoord == 1:
            print("je liep terug en bevindt je in de trappen huis")
            antwoord = int(input(scenario['vraag3']))
            if antwoord == 1:
                print("je bent succesvol ontsnapt ")
                print("WIN")
                exit()
            elif antwoord == 2:
                print("je loopt de voorraads kamer binnen en wordt van achter in je hoofd geschoten")
                print("LOSE")
                exit()
        elif antwoord == 2:
            print('je bent door gelopen en heb een uitgang gevonden')
            print("WIN")
            exit()
        
    elif antwoord == 2:
        print(scenario['verhaal2'])
        print("LOSE ")
        exit()
    else:
        return scenario['vervolg1']
    antwoord = int(input(scenario['vraag2']))
    if antwoord == 1:
        antwoord = int(input(scenario['vervolg2']))
        if antwoord == 1:
            print("je loopt door en komt bij een deur je doet de deur open wordt aangevallen je gebruikt je wapen en shiet die gene dood je onstapt succesvol uit de gevanenis")
            print("WIN")
            exit()


game(vragen[0])



