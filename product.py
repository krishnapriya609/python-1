def product_numbers(list):
    product=1
    for i in list:
        product=product*i
    print(product)
list=[]
element=int(input("Enter the element of the list"))

for i in range(element):
    num=int(input("enter the number"))
    list.append(num)
print(list)
product_numbers(list)