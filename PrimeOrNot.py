num=int(input("Enter a number to check whether it is prime or not : "))
if num>1:
    for i in range(2,num):
        if (num/i)==0:
            print(num," is not a prime number.")
            break
        else :
            print("It's a prime number. ")
    else :
        print("Not a prime number ")






