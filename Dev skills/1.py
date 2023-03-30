# gastheer = input("wie is de gastheer")
# gasten = int(input("hoeveel gasten zijn er?"))
# drank = False
# Chips = True 

# if gastheer !="corbijn" and (gastheer == 'yassine' or(drank and (gasten >= 4 and gasten <=20 or gastheer))):
#     print("start the party")
# else:
#     print("no party")


# Prompt user for amount in US dollars
usd = float(input("Enter amount in US dollars: "))

# Convert US dollars to Euros using the current exchange rate of 1 USD to 0.85 EUR (as of September 2021)
eur = usd * 0.85

# Display the result
print(f"${usd:.2f} is equal to €{eur}")
