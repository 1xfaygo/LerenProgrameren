def aantal_bolletjes():
    while True:
        try:
            aantal = int(input('Hoeveel bolletjes wilt u?: '))
            return aantal
        except ValueError:
            print('Sorry dat begrijp ik niet. Voer een geldig getal in.')

def aantal_bolletjes_check():
    aantal = aantal_bolletjes()
    if aantal <= 4:
        bakje_of_horentje = bakje_horentje()
    elif 4 <= aantal <= 8:
        print(f'Hier u bakje met {aantal} ijsbollen.')
        opnieuw_bestellen()
    else:
        print('Sorry dat hebben wij niet.')
    
def bakje_horentje():
    bakje_vraag = input('Wilt u een bakje of hoorentje?:')
    
    if bakje_horentje != 'bakje':
        return 'horentje'
    elif bakje_horentje == 'bakje':
        return 'bakje'
    else:
        print('Sorry dat begrijp ik niet.')
    return bakje_horentje() 

def opnieuw_bestellen():
    opnieuw_bestellen_vraag = input('wilt u opnieuw bestellen?:')
    
    if opnieuw_bestellen_vraag != 'ja':
        print('Dankuwel voor bestellen bij papi gelato.')
    else:
        print("opniew")
