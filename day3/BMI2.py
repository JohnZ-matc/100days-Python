# BMI Calculator with conditional statement

print("Welcome to BMI Calc 2.0")

h = float(input("How tall are you in m? \n"))
w = float(input("How many kg do you weigh? \n"))
bmi = round(w / (h * h), 2)

if bmi <= 18.5:
    print(f"Your BMI is {bmi}. You are clinically underweight. Eat a Burger!")
elif bmi <= 25.5:
    print(f"Your BMI is {bmi}. You are just fine the way you are. Keep it up!")
elif bmi <= 35:
    print(f"Your BMI is {bmi}. You are obese. Go for a walk!")
else:
    print(f"Your BMI is {bmi}. You are clinically obese. Chill out on the donuts!")
