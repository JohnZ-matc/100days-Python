print("Ride Requirement Program \n")

height = int(input("How tall are you in cm? \n"))

if height >= 120:
    age = int(input("How old are you? \n"))
    if age <= 12:
        print("The cost of an child ticket is $5.\n")
    elif age < 18:
        print("The cost for your ticket is $7\n")
    else:
        print("The cost of an adult ticket is $12\n")
else:
    print("You are not tall enough to ride the rollercoaster.")
