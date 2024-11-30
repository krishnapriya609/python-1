'''
Author:Krishnapriya
Date:30/11/2024
'''
def factorial(num):
    if num==0:
        return 1
    else:
        return(num*factorial(num-1))
number=int(input("Enter the number"))
custom=factorial(number)
print("The factorial of number",custom)