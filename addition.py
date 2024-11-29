'''
Author:Krishnapriya
Date:29/11/2024
'''
def addition(num1,num2):
    if num2==0:
        return num1
    else:
        return addition(num1+1,num2-1)
num1=int(input("enter the first number"))
num2=int(input("Enter the second number"))
custom=addition(num1,num2)
print("the sum=",custom)