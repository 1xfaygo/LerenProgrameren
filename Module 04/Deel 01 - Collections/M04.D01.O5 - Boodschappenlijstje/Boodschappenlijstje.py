boodschappenlist = {}


while True:
    item_vraag = input("Voeg een item toe:")
    aantal = int(input("hoveel wil je ?:"))
    if item_vraag in boodschappenlist:
        boodschappenlist[item_vraag] += aantal
    else:
        boodschappenlist.update({item_vraag : aantal})
    tweede_item_vraag = input("meer toevoegen")
    if tweede_item_vraag != "ja":
        break
    
print("-[BOODSCHAPPENLIJST]-")

for key,value in boodschappenlist.items():
    print(f"{key} : {value}")

print("----------------------") 