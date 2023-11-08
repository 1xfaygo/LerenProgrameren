def aantal_bolletjes():
            aantal = int(input('Hoeveel bolletjes wilt u?: '))
            return aantal

def bakje_horentje():
        bakje_vraag = input('Wilt u een bakje of hoorentje?: ')
        if bakje_vraag.lower() == 'bakje':
            return 'bakje'
        elif bakje_vraag.lower() == 'hoorentje':
            return 'hoorentje'
        else:
            print('Sorry, dat begrijp ik niet.')

def opnieuw_bestellen():
        opnieuw_bestellen_vraag = input('Wilt u opnieuw bestellen? (Ja/Nee): ')
        if opnieuw_bestellen_vraag.lower() == 'ja':
            return "ja"
        else:
            return "nee"
    






