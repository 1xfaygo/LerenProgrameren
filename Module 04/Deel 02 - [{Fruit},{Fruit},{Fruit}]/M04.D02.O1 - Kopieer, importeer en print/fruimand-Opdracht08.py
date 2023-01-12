from fruitmand import fruitmand

fruitmand.append({'name' : 'waterlmelon',
    'weight' : 2500,
    'color' : 'green',
    'round' : True})

gewicht = 0

for x in fruitmand:
     gewicht += x['weight']
print(gewicht)