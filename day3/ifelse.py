print("Basic python relational operators. \n")

b = int(input("Enter a number: \n"))
c = int(input("Enter a second number: \n"))

if b == c:
    print(f"{b} is equal to {c}")
elif b < c:
    print(f"{b} is less than {c}")
elif b > c:
    print(f"{b} is greater than {c}")
else:
    print("error")
