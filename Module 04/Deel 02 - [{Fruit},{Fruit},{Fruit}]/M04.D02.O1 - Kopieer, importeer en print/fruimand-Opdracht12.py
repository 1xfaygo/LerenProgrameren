from fruitmand import fruitmand
name = 10
fruit_kleur = ''
for x in fruitmand:
    test = len(x['name'])
    if test > name:
        fruit_name = x['name']
        fruit_kleur = x['color']
    

print(f"De {fruit_name} {len(fruit_name)} letters heeft een {fruit_kleur} kleur en een gewicht van {x['weight']/1000} KG ")
