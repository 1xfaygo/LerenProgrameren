from fruitmand import fruitmand

fruitmand.append({'name' : 'waterlmelon',
    'weight' : 2500,
    'color' : 'green',
    'round' : True})
for x in fruitmand:
    print(x['weight'])