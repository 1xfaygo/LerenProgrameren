Console = 55.00 
pc= 45.00 
prijsconsole = 0
prijspc = 0
premiummembershipkorting= 15.00
welkeplatform = input ("Console of Pc?")
premiummembershipconsole = input("heeft u een premium membership voor de console?")
premiummembershippc= input("heeft u een premium membership voor de pc?")

if premiummembershipconsole == 'ja':
    premiumgamekortingconsole = prijsconsole -premiummembershipkorting

elif premiummembershippc == 'ja':
    premiummembershipkortingpc = prijspc  -premiummembershipkorting

if premiummembershippc == 'nee':
    premiummembershipkortingpc = pc+0
    
elif premiummembershipconsole == 'nee':
    premiumgamekortingconsole = Console+0

if welkeplatform == 'console':  
    consolegameqyt = int(input('hoeveel games op de console wilt uw?'))
    prijsconsole = Console * consolegameqyt -premiumgamekortingconsole

elif welkeplatform == 'pc':
    pcgameqyt = int(input('hoveel games wilt uw op de pc?'))
    prijspc = pc * pcgameqyt-premiummembershipkorting

totaalprijs = prijspc + prijsconsole- premiummembershipkorting
print(f'totaal prijs is {totaalprijs} Euro!')


