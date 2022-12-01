#bedrag_string = input("Voer bedrag in:")
#bedrag = float(bedrag_string)
bedrag = int(input("Voer bedrag in :")) #* 100

aantal_twee_euro = bedrag // 200
print("aantal 2 euro: {}".format(aantal_twee_euro))
restantt = bedrag - 200 * aantal_twee_euro

aantal_een_euro = restantt // 100
print("aantal 1 euro: {}".format(aantal_een_euro))
restantt = bedrag - 100 * aantal_een_euro


aantal_50_cent = restantt // 50
print(f"aantal 50 cent: {aantal_50_cent}")
restantt = restantt - 50 * aantal_50_cent

aantal_20_cent = restantt // 20
print(f"aantal 20 cent: {aantal_20_cent}")
restantt = restantt - 20 * aantal_20_cent


aantal_10_cent = restantt // 10
print(f"aantal 10 cent: {aantal_10_cent}")
restantt = restantt - 10 * aantal_10_cent


print(restantt)
