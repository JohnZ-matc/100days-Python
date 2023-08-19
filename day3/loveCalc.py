################################# Love calculator Game ###########################
name1 = input("What is your name?\n")
name2 = input("What is your partner's name?\n")
combinedName = name1.lower() + name2.lower()
t = combinedName.count('t')
r = combinedName.count('r')
u = combinedName.count('u')
e = combinedName.count('e')

true = (t+r+u+e)

l = combinedName.count('l')
o = combinedName.count('o')
v = combinedName.count('v')
e = combinedName.count('e')

love = (l+o+v+e)

loveScore = str(true) + str(love)
totalScore = int(loveScore)
if totalScore < 10 or totalScore > 90:
    print(f"Your score is {totalScore}, you go together like coke and mentos.")
elif totalScore>= 40 or totalScore <= 50:
    print(f"Your score is {totalScore}, you'll be alright together.")
else:
    print(f"Your score is {totalScore}.")
