# Tip Calculator Program for multiple people
# If the bill is 150$, split between 5 people with a 12% tip.
# Each person should pay ($150 / 5) * 1.12.
# Round the result to the nearest hundereth decimal place.

bill = input("What is the total bill: \n")
party = input("How many people are splitting bill: \n")
tip = input("Would you like to tip %10, %12, %15?: \n")

bill_fl = float(bill)
party_int = int(party)
tip_int = int(tip)

total = (bill_fl / party_int) * (tip_int * .01 + 1)

print(round(total, 2))
