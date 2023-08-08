# Leap Year Calculator Program!

# String Variables

welcome = str("This is the Leap Year Calculator Program!\n")
prgmDesc = str("How it works: Enter a year, and the program will tell you if that year was a leap year.\n")

# Integer Variables


# Program

print(welcome + prgmDesc)

y = round(float(input("Enter a year: \n")), 2)

leapy1 = (y % 4 == 0)
leapy2 = (y % 100 == 0)
leapy3 = (y % 400 == 0)

if leapy1:
    if leapy2:
        if leapy3:
            print("Leap")
        else:
            print("Not Leap")
    else:
        print("Leap")
else:
    print("Not Leap")
