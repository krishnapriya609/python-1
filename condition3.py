number1=int(input("enter first number"))
number2=int(input("enter second number"))
number3=int(input('enter third number'))
if number1>number2 and number1>number3:
    print(number1, "greater than than other two")
elif number2>number3:
    print(number2, "greater than other two")
else:
    print(number3, "is greater than other two")