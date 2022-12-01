A =  int(input("geef een getal aan:"))
B =  int(input("geef een getal aan:"))

max= A
min= B

if A >B:
    print(f"a is het grootste getal: {max}")

elif A< B :
    print(f"a is het kleinste getal: {min}")

else:
    print (f"a en b zijn even groot")

print (f"Het minimum is: {min}")
print (f"Het maximum is: {max}")