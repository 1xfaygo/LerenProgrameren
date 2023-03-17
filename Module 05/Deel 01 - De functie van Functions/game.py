vragen = [{
    'vraag': "(1) blijf je onder het bed liggen of (2)waag je een poging om te ontsnappen: ",
    'vraag2': "(1)ga je de beveilegings kamer in  of (2)loop je door: ",
    'verhaal1':'je wordt onder shot gehouden',
    'verhaal2':'je rent weg',
    'vervolg1':98,
    'vervolg2':"pak je de wapon op? (1)ja of (2)nee: ",
}]
items = []

def game(scenario):
    antwoord = int(input(scenario['vraag']))
    if antwoord == 1:
        print(scenario['verhaal1'])
        if scenario['vervolg1'] == 98:
            print('Je bent dood')
            exit()
        else:
            return scenario['vervolg1']
    elif antwoord == 2:
        print(scenario['verhaal2'])
    antwoord = int(input(scenario['vraag2']))
    if antwoord == 1:
        antwoord = int(input(scenario['vervolg2']))
        if antwoord == 1:
            print("WIN")
        else:
            print("LOSE")


game(vragen[0])

