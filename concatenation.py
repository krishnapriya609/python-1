'''
author:krishnapriya
description:concatenated string.
'''

first_name=input("enter your first name")
last_name=input("enter your second name")
name=first_name+ " " +last_name
print(name)
first_name_length= len(first_name)
print(first_name_length)
extracted_first_name=name[:first_name_length]
print(extracted_first_name)



