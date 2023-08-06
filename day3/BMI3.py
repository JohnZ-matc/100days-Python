# BMI Calculator with more conditional statements that allow user more choice

print("Welcome to BMI Calc 3.0 \n")

choice = int(input("Type 1 for metric or 2 for imperial measurements: \n"))

if choice == 1:
    heightMeters = float(input("How tall are you in meters? \n"))
    weightKilograms = float(input("How many kilo's do you weigh? \n"))
    metricBMI = round(weightKilograms / (heightMeters**2), 2)

    if metricBMI <= 18.5:
        print(f"BMI is {metricBMI}, underweight.")
    elif metricBMI <= 25.5:
        print(f"BMI is {metricBMI}, you are normal weight.")
    elif metricBMI <= 35:
        print(f"BMI is {metricBMI}, you are too heavy.")
    else:
        print(f"BMI is {metricBMI}, you are obese ")
elif choice == 2:
    heightFeet = float(input("How tall are you in inches? \n"))
    weightLbs = float(input("How many pounds are you \n"))
    imperialBMI = round((weightLbs / (heightFeet**2) * 703), 2)

    if imperialBMI <= 18.5:
        print(f"BMI is {imperialBMI}, underweight")
    elif imperialBMI <= 25.5:
        print(f"BMI is {imperialBMI}, you are normal weight.")
    elif imperialBMI <= 35:
        print(f"BMI is {imperialBMI}, you are too heavy.")
    else:
        print(f"BMI is {imperialBMI}, you are obese.")
else:
    print("error")
