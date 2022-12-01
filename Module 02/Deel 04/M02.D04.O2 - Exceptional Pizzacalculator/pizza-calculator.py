small =8.99
medium=12.49
large=14.49


maatpizzasmall=input(f" wilt uw een pizza small:{small} (25cm) ")
maatpizzamedium=input(f"wilt uw een pizza medium:  {medium}   (29cm) ")
maatpizzalarge=input(f"wilt uw een pizza large: {large}  (35cm) type")
pizzapuntaantal=int(input("Hoeveel pizza punten wilt uw?"))
totaal=()

if maatpizzasmall=="small":
    totaal=(small)

if maatpizzamedium=="medium":
    totaal=(medium)

if maatpizzalarge=="large":
    totaal=(large)



print("   ")
print("TOTAAL")
print(totaal)


 
