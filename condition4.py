temperature=int(input("Enter the temperature"))
scale=input("is this in (C)elsius or (F)ahrenheit?")
if scale=="C":
    f = (9/5*temperature) + 32
    print(temperature ,"is in",f,"fahrenhit" )
elif scale=="F":
    c=5/9*(temperature-32)
    print(temperature," is in ",c, "celcius")





