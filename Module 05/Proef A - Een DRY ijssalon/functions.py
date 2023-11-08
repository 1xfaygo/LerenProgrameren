<<<<<<< HEAD
def aantal_bolletjes():
            aantal = int(input('Hoeveel bolletjes wilt u?: '))
            return aantal

def bakje_horentje():
        bakje_vraag = input('Wilt u een bakje of hoorentje?: ')
        if bakje_vraag.lower() == 'bakje':
            return 'bakje'
        elif bakje_vraag.lower() == 'hoorentje':
            return 'hoorentje'
=======
# def aantal_bolletjes():
#     while True:
#         try:
#             aantal = int(input('Hoeveel bolletjes wilt u?: '))
#             return aantal
#         except ValueError:
#             print('Sorry dat begrijp ik niet. Voer een geldig getal in.')

# def aantal_bolletjes_check():
#     aantal = aantal_bolletjes()
#     if aantal <= 4:
#         bakje_of_horentje = bakje_horentje()
#     elif 4 <= aantal <= 8:
#         print(f'Hier u bakje met {aantal} ijsbollen.')
#         opnieuw_bestellen()
#     else:
#         print('Sorry dat hebben wij niet.')
    
# def bakje_horentje():
#     bakje_vraag = input('Wilt u een bakje of hoorentje?:')
    
#     if bakje_horentje != 'bakje':
#         return 'horentje'
#     elif bakje_horentje == 'bakje':
#         return 'bakje'
#     else:
#         print('Sorry dat begrijp ik niet.')
#     return bakje_horentje() 

# def opnieuw_bestellen():
#     while True:
#             opnieuw_bestellen_vraag = input('wilt u opnieuw bestellen?N (JA/NEE):')
#             if opnieuw_bestellen_vraag != 'ja':
#                     print('Dankuwel voor bestellen bij papi gelato.')
#                     return opnieuw_bestellen_vraag
def aantal_bolletjes():
    while True:
        try:
            aantal = int(input('Hoeveel bolletjes wilt u?: '))
            return aantal
        except ValueError:
            print('Sorry, dat begrijp ik niet. Voer een geldig getal in.')

def bakje_horentje():
    while True:
        bakje_vraag = input('Wilt u een bakje of horentje?: ')
        if bakje_vraag.lower() == 'bakje':
            return 'bakje'
        elif bakje_vraag.lower() == 'horentje':
            return 'horentje'
>>>>>>> 67eaf9c03bcfaf9aef6c46ee3ea988a43997afda
        else:
            print('Sorry, dat begrijp ik niet.')

def opnieuw_bestellen():
<<<<<<< HEAD
        opnieuw_bestellen_vraag = input('Wilt u opnieuw bestellen? (Ja/Nee): ')
        if opnieuw_bestellen_vraag.lower() == 'ja':
            return "ja"
        else:
            return "nee"
    






=======
    while True:
        opnieuw_bestellen_vraag = input('Wilt u opnieuw bestellen? (Ja/Nee): ')
        if opnieuw_bestellen_vraag.lower() != 'ja':
            print('Dank u wel voor bestellen bij Papi Gelato.')
            break

def main():
    aantal = aantal_bolletjes()
    
    if aantal <= 4:
        bakje_of_horentje = bakje_horentje()
        print(f'Hier is uw {bakje_of_horentje} met {aantal} ijsbollen.')
    elif 4 < aantal <= 8:
        print(f'Hier is uw bakje met {aantal} ijsbollen.')
        opnieuw_bestellen()
    else:
        print('Sorry, dat hebben wij niet.')
>>>>>>> 67eaf9c03bcfaf9aef6c46ee3ea988a43997afda
