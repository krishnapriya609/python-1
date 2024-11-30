
'''
def maximum(num1,num2,num3):
     numbers=[num1,num2,num3]
     numbers.sort()
     return numbers[2]
num1=int(input("enter the first number :"))
num2=int(input("Enter the second number:"))
num3=int(input("Enter the third number: "))
custom=maximum(num1,num2,num3)
print("The greatest number is",custom)
'''

def add_numbers(list):
    sum=0
    for i in list:
        sum=sum+i
    print(sum)
list=[]
element=int(input("Enter the element of the list"))

for i in range(element):
    num=int(input("enter the number"))
    list.append(num)
print(list)
add_numbers(list)








