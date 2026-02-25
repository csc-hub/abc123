def add():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    return a + b
print("The sum of the two numbers is:", add())
c= int(input("Enter a number: "))
print("The result after subtraction is:", c)
if c > 0:
    print("The number is positive.")
elif c < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
