import random


boodschappenlist = {}

teller = 1

while True:
    itemvraag = input("Voeg een item toe:")
    if itemvraag in boodschappenlist:
        boodschappenlist[itemvraag] +=1 
    else:
        boodschappenlist.update({itemvraag : teller})
    tweedeitemvraag = input("meer toevoegen")
    if tweedeitemvraag != "ja":
        break
    
print("-[boodschappenlijst]-")

for key,value in boodschappenlist.items():
    print(f"{value} : {key}")

print("----------------------") 

