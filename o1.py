a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
c=int(input("Enter a third number: "))
if a>b and a>c:
    print("The first number is greater than the second and third numbers.")
elif b>a and b>c:
    print("The second number is greater than the first and third numbers.")
elif c>a and c>b:
    print("The third number is greater than the first and second numbers.")
else:
    print("The first number is equal to the second number.")