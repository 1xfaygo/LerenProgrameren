from fruitmand import fruitmand
niet_rond = 0
rond = 0


z = False
while z == False:
    vraag_kleur = input('kies een kleur uit de fruitmand')
    for fruit in fruitmand:
        if fruit['color'] == vraag_kleur:
            z = True
        
    if fruit['round'] == True:
        rond +=1
        
    else:
        niet_rond +=1

    if rond < niet_rond:
        print(f"Er zijn {rond - niet_rond} meer ronde vruchten dan niet ronde vruchten in de kleur {vraag_kleur}")

    elif rond > niet_rond:
        print(f"Er zijn {niet_rond - rond} minder ronde vruchten dan niet ronde vruchten in de kleur {vraag_kleur}")

    elif rond == niet_rond:
        print(f"Er zijn {rond} ronde vruchten en {niet_rond} niet ronde vruchten in de kleur {vraag_kleur}")
        quit()
    else:
        print(f"{vraag_kleur} zit er niet in ")

            
        

        
        
