print("Welcome to the tip calculator!")
cost = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12, or 15(%)? "))
num_people = int(input("How many people to split the bill? "))

amount = round((cost * (1+(tip/100)) / num_people), 2)

print(f"Each person should pay: ${amount:.2f}")