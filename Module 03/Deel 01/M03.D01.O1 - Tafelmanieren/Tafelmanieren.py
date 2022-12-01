tafelvan1tot10 = int(input("welke tafel van wil je weten?"))
print(f"de tafel van {tafelvan1tot10} is")
for tafel in range(1,11):
    uitkomst = tafel * tafelvan1tot10
    print(f"{tafel} x {tafelvan1tot10} = {uitkomst}")

