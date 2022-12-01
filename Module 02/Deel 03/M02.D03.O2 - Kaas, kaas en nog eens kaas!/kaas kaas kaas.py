kleurkaas =input('is de kaas geel').lower()
if kleurkaas == 'ja':
    kaasgaten = input("zitten er gaten in?").lower()
    if kaasgaten == 'ja':
        kaasduur = input("is de kaas belagelijk duur?").lower()
        if kaasduur == 'ja':
            print("Emmenthaler")
        elif kaasduur == 'nee':
            print("Leerdammer")
    elif kaasgaten == 'nee':
        kaashard = input("is de kaas hard als steen?").lower()
        if kaashard == 'ja':
            print("Parmigiano Reggiano")
        elif kaashard == 'nee':
            print("Goudse Kaas")
else:
    kaasschimmel =input('Heeft de kaas blauwe schimmel?').lower()
    if kaasschimmel == 'nee':
        kaaskorst = input("Heeft de kaas een korst?").lower()
        if kaaskorst == 'ja':
            print("Camembert")
        else:
            print("Mozzarella")
    elif kaasschimmel == 'ja':
        korst = input("Heeft de kaas een korst?").lower()
        if korst == 'ja':
            print("Blue de Rochbaron")
        else:
            print("Foume d'Ambert")

