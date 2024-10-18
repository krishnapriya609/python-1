'''
author:krishnapriya
date:18-10-2024
description: Python program that uses functions from the math module to perform the following operations on a number provided by the user:


'''
 import math
number=int(input("Enter a number"))
square_root=math.sqrt(number)
print("square_root of" , number , square_root)
factorial=math.factorial(number)
print("factorial of" ,number ,factorial )
power=math.pow(number,2)
print("power of " , number , power)