'''
Author:Krishnapriya
Date:29/11/2024
'''
def is_valid_mobile_number(number):
    if len(number)==10 and number[0] in "789":
        return True
    return False
mobile_number=input("Enter the number")
if is_valid_mobile_number(mobile_number):
    print("The mobile_number",mobile_number,"is valid")
else:
    print("The mobile number",mobile_number,"is invalid")





