def add():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if(a>b):
        print("a is greater")
    else:
        print("b is greater")
    print(a + b)

print("The sum of the two numbers is:", add())