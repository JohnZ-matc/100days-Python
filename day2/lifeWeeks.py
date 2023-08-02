# Life in Weeks program

age = input("What is your current age? \n")

time_remain = 90 - int(age)

months_age = time_remain * 12 
weeks_age = time_remain * 52
days_age = time_remain * 365

print(f"You have {days_age} days, {weeks_age} weeks, and {months_age} months left.")
