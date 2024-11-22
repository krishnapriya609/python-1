list_1=[1,2,3,4,5]
list_2=[6,7,8,9,10]
list_3=(list_1+list_2)
print("first list=",list_1)
print("second_list=",list_2)
print("combined_list=",list_3)
odd_numbers=[]
even_numbers=[]
for i in list_3:
    if i%2==0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)
print("odd numbers=",odd_numbers)
print("even numbers=",even_numbers)
print("sorted list=",even_numbers+odd_numbers)