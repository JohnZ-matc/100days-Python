# new rollercoaster program

print("Welcome to the Rollercoaster!\n")

height = int(input("How tall are you in cm?\n"))
bill = 0
if height >= 120:
    age = int(input("How old are you?\n"))
    if age < 7:
        bill = int(5)
        print("The cost of a child ticket is $5.\n")
    elif age <= 17:
        bill = int(10)
        print("The cost of an adolescent ride is $10.\n")
    else:
        bill = int(15)
        print("The cost of an adult ticket is $15.\n")

    photo = input("If you would like a $3 photo with your ticket, type [Y]. If not, [N]: ")
    if photo == "y":
        print(f"you owe, ${bill + 3}.\n")
    else:
        print(f"You owe, ${bill}.\n")
else:
    print("You are too short for the ride.\n")
