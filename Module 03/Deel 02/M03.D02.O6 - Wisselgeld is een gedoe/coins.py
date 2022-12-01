# name of student: Yassine  
# number of student: 99072435
# purpose of program: wisselgeld te geven en berekenen  
# function of program: het berekenen van wisselgeld
# structure of program:er is gebruik gemaakt van if while loops, inputs, variable's en exeptions.


vijfeuro = 500
viereuro = 400
drieeuro = 300
tweeeuro = 200
eeneuro = 100
vijftigcent = 50
twintigcent = 20
tiencent = 10
vijfcent = 5

toPay = int(float(input('Amount to pay: '))* 100) # hoveel er betaald moet worden 
paid = int(float(input('Paid amount: ')) * 100) # hoeveel er is betaald
change = paid - toPay # wisselgeld variabelen

if change > 0: # als de variabel change 0 is begint de programma
  coinValue = 500 # de waarde van de coin in het begin
  
  while change > 0 and coinValue > 0:#start van de loop de loop stopt pas als alle wissel geld  teruggegeven is 
    nrCoins = change // coinValue # berekend change gedeeld door coinvalue dan krijg je nrCoins

    if nrCoins > 0: # als er nog een coin moet ingevoerd worden dan start de IF statement
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #laat je zien hoeveel munten van  coinvalue kan geven.
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #
      change -= nrCoinsReturned * coinValue #Change is - De aantal coins dat ingevoerd is keer de coinvalue

# comment on code below: Hier gaat die langs alle coinvalue's
    if coinValue == vijfeuro:
      l0l = nrCoinsReturned
    elif coinValue == viereuro:
      l0l2 = nrCoinsReturned
    elif coinValue == drieeuro:
      l0l3 = nrCoinsReturned
    elif coinValue == tweeeuro:
      l0l4 = nrCoinsReturned
    elif coinValue == eeneuro:
      l0l5 = nrCoinsReturned
    elif coinValue == vijftigcent:
      l0l6 = nrCoinsReturned
    elif coinValue == twintigcent:
      l0l7 = nrCoinsReturned
    elif coinValue == tiencent:
      l0l8 = nrCoinsReturned
    elif coinValue == vijfcent:
      l0l9 = nrCoinsReturned
    else:
      coinValue = 0
try:
  if change > 0: # Hier laat hij de change zien dat is ingevuld ,en  als de change niet is compleet terug gegeven
    print('Change not returned: ', str(change) + ' cents')
  else:
    print(f"{vijfeuro}: {l0l}")
    print(f"{viereuro}: {l0l2}")
    print(f"{drieeuro}: {l0l3}")
    print(f"{tweeeuro}: {l0l4}")
    print(f"{eeneuro}: {l0l5}")
    print(f"{vijftigcent}: {l0l6}")
    print(f"{twintigcent}: {l0l7}")
    print(f"{tiencent}: {l0l8}")
    print(f"{vijfcent}: {l0l9}")
except NameError: 
  exit()