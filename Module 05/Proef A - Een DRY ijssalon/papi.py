from functions import *

bolletjes_prijs = 1.10
bakje_prijs = 0.75
hoorentje_prijs = 1.25

totaal_bolletjes = 0
totaal_bakjes = 0
totaal_hoorentje = 0

while True: 
    aantal = aantal_bolletjes()
    totaal_bolletjes += aantal
    if aantal <= 4:
        bakje_of_hoorentje = bakje_horentje()

        print(f'Hier is uw {bakje_of_hoorentje} met {aantal} ijsbollen.')
        if bakje_of_hoorentje == 'bakje':
            totaal_bakjes += 1
        else:
            totaal_hoorentje +=1
    elif 4 < aantal <= 8:
        totaal_bakjes +=1
        print(f'Hier is uw bakje met {totaal_bolletjes} ijsbollen.')
    else:
        print("Sorry, dat hebben wij niet.")

    opnieuw_bestellen_vraag = opnieuw_bestellen()

    if opnieuw_bestellen_vraag == "nee":
        break
1
totaal_bolletjes_prijs = totaal_bolletjes * bolletjes_prijs
totaal_bakjes_prijs = totaal_bakjes * bakje_prijs
totaal_hoorentjes_prijs = totaal_hoorentje * hoorentje_prijs

totaal_prijs = totaal_bolletjes_prijs + totaal_bakjes_prijs + totaal_hoorentjes_prijs

print(f'aantal bolletjes: {totaal_bolletjes} x {bolletjes_prijs} = {totaal_bolletjes_prijs:.2f}')
print(f'aantal hoorentjes: {totaal_hoorentje} x {hoorentje_prijs} = {totaal_hoorentjes_prijs:.2f}')
print(f'aantal bakjes: {totaal_bakjes} x {bakje_prijs} = {totaal_bakjes_prijs:.2f}')
print(f'Totaal te betalen: €{totaal_prijs:.2f}')
