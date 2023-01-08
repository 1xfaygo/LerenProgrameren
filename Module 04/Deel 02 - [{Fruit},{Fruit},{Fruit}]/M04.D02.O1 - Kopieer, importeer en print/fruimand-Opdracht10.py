from fruitmand import fruitmand
testdict= {}
for x in fruitmand:
    testdict[x['name']] = x['weight'] / 100

volgordezetter=dict(sorted(testdict.items(), key=lambda x: x[1], reverse=True))

for key,value in volgordezetter.items():
    print(f"{key} {value} KG")