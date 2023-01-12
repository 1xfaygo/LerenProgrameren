from fruitmand import fruitmand
name = 10
fruit_kleuren = [{
    'color' : 'oranje'
}]
for x in fruitmand:
    test = len(x['name'])
    if test > name:
        fruit_name = x['name']
for z in fruit_kleuren:
    print(f"De {fruit_name} {len(fruit_name)} letters heeft een {z['color']} kleur en een gewicht van {x['weight']/1000} KG ")
