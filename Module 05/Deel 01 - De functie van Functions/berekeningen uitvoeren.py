def addition(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2


choice = ""
while not choice in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'):
    choice = input("Wat wilt u doen? A) getallen optellen, B) getallen aftrekken, C) getallen vermenigvuldigen, D) getallen delen, E) getal ophogen, F) getal verlagen, G) getal verdubbelen  H) getal halveren?: ").lower()
    if choice == 'niks':
        exit()

aantal = 1
while True:
    if aantal < 0 and choice != 'n' and choice in ('a','b','c','d'):
        n1 = aantal
        n2 = float(input("Geef de 2e getal op: "))


    elif aantal < 0 and choice != 'i' and choice in ('e', 'f', 'g', 'h'):
        number1 = aantal

    if choice in ('a','b','c','d'):
        n1 = float(input("Geef een getal op:"))
        n2 = float(input(f"geef nog een getal op:"))

    elif choice in ('e', 'f', 'g', 'h'):
        n1 = float(input("Geef een getal op: "))

    else:
        exit()



    if choice == 'a':
        aantal = addition(n1,n2)
        print(f"{n1} + {n2} = {aantal}")
    
    elif choice == 'b':
        aantal = subtraction(n1,n2)
        print(f"{n1} - {n2} = {aantal}")
    
    elif choice == 'c':
        aantal = multiplication(n1,n2)
        print(f"{n1} x {n2} = {aantal}")
    
    elif choice == 'd':
        aantal = division(n1,n2)
        print(f"{n1} : {n2} = {aantal}")

    elif choice == 'e':
        n1 = 1 
        aantal = addition(n1,n2)
        print(aantal)
    
    elif choice == 'f':
        n1 = 1
        aantal = subtraction(n1,n2)
        print(aantal)

    elif choice == 'g':
        n2 = 2
        aantal = multiplication(n1,n2)
        print(aantal)
    
    else: 
            n2 = 2
            aantal = division(n1,n2)
            print(aantal)
        
    choice = input(f"Wil je wat met het antwoord ({aantal}) doen? A) iets optellen, B) iets aftrekken, C) met iets vermenigvuldigen, D) ergens door delen, E) ophogen, F) verlagen, G) verdubbelen, H) halveren of N) Nee?")
    




    













