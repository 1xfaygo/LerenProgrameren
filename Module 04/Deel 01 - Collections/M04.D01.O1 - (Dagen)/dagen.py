dagen =("maandag","dinsdag","woensdag","donderdag","vrijdag","zaterdag","zondag")
for z in dagen:
    print(f"Alle dagen van de week zijn: {dagen}")
    if z == "maandag":
         break
print(" ")
for x in range(5):
    print(f"De werkdagen zijn: {dagen[x]}")
print(" ")
for c in range(5,7):
    print(f"De weekenddagen zijn: {dagen[c]}")
print(" ")
for v in range(6,-1,-1):
    print(f"De weekenddagen zijn: {dagen[v]}")
print(" ")
for b in range(4,-1,-1):
    print(f"De werkdagen in omgekeerde volgorde zijn: {dagen[b]}")
print(" ")
for n in range(6,4,-1):
    print(f"De weekenddagen in omgekeerde volgorde zijn:{dagen[n]}")