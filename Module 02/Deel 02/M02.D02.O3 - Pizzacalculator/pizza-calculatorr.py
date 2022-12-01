import sys

smallpizza = 4.99
mediumpizza = 7.99
largepizza = 10.00
totaalpijspizzasmall= 0
totaalpijspizzasmedium= 0
totaalpijspizzaslarge= 0


try:
    pizzaqyt = int(input('hoeveel small pizza wilt u?'))
    qtymedium = int(input('hoeveel medium pizza wilt u?'))
    qtylarge = int(input('hoeveel large pizza wilt u?'))
except:
    print("kon niet calculeren")
try:
    totaalpijspizzasmall = smallpizza*pizzaqyt
    totaalpijspizzasmedium = mediumpizza * qtymedium
    totaalpijspizzaslarge = mediumpizza * qtylarge
except:
    print("Kan geen letters omzetten in cijfers")
    sys.exit()

   
totaalprijs = totaalpijspizzasmall + totaalpijspizzasmedium + totaalpijspizzaslarge
print(f'totaal prijs is {totaalprijs}!')

