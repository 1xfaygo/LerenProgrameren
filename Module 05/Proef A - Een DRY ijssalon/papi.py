from functions import *


print("Welkom bij papi gelato je mag alle smaken kiezen zolang het maar vanille ijs is.")

while True:
        aantal = aantal_bolletjes()

        if aantal <= 4:
            bakje_of_hoorentje = bakje_horentje()
            print(f'Hier is uw {bakje_of_hoorentje} met {aantal} ijsbollen.')
        elif 4 < aantal <= 8:
            print(f'Hier is uw bakje met {aantal} ijsbollen.')
        else:
            print("Sorry dat hebben wij niet.")

        opnieuw_bestellen_vraag = opnieuw_bestellen()

        if opnieuw_bestellen_vraag == "nee":
             break
        