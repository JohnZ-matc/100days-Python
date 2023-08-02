# Day 2 - Understanding Data Types and How to Manipulate Strings

# BMI calculator program

# BMI = weight/height**2


height = input("Enter your height here: \n")
weight = input("Enter your weight here: \n")

new_height = float(height)
new_weight = float(weight)

BMI = (new_weight / new_height**2)

print(f"Your BMI is, {BMI}%")
