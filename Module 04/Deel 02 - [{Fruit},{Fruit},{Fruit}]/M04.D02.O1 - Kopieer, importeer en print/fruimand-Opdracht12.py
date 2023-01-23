from fruitmand import fruitmand
fruit_kleuren = {'orange': 'oranje'}
nieuwe_fruitmand = sorted(fruitmand, key=lambda d :d['name'], reverse=True)
for z in nieuwe_fruitmand:
    fruit_name = (z['name'])
    if len(fruit_name) == max(len(x['name']) for x in nieuwe_fruitmand):
        print(f"De {fruit_name} {len(fruit_name)} letters heeft een {z['color']} kleur en een gewicht van {z['weight']/1000} KG")
