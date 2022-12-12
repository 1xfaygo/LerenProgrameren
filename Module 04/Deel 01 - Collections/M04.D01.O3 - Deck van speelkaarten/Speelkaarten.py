import random 
kleur = ["harten","Klaver","schoppen","ruiten"]
kaarten = ["boer","koning", "koningin","aas"]
speciale_kaarten = ["joker","2e joker"]
dek = []
for x in kleur:
    for z in kaarten:
        dek.append(f"{x},{z}")
    for c in range(2,11,1):
        dek.append(f"{x},{c}")

random.shuffle(dek)

for b in range(1,8):
    jouwkaarten = random.choice(dek)
    print(f"kaart {b}:{jouwkaarten}")
print(f"de rest van de 47 kaarten zijn:{dek}")