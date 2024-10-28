while True:
    print("\1.covert celcius to fahrenheit")
    print("\2.convert fahrenheit to celcius")
    choice=int(input("enter your choice:"))
    if choice==1:
        temp1=int(input("enter the temperature in celcius"))
        print(temp1,"in fahrenheit is ",(temp1*9/5)+32)
    elif choice==2:
        temp2=int(input("enter the temperature in fahrenheit"))
        print(temp2,"in celcius is",(temp2-32)*5/9)
    elif choice==3:
         break
    else:
        print("invalid details")







