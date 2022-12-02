# chcek leap year is not...

year=int(input("enter the year:  "))
if (year%400==0) and (year%100==0):
    print("year is leap year")
elif(year%4==0)and (year%100!=0):
    print("year is an leap yaer")
else:
    print("year is not leap year")




