# check number is prime or not
num=int(input("enter the number to chcek prime or not...!  "))
if num==1:
    print("number is prime")
if num>1:
        for i in range(2,num):
            if num%i==0:
                print("is is not prime")
                break
        else:
                print("number is prime")










