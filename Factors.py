def FactorsOfTheNumber(x):
    print("Factors : ")
    for i in range(1,x+1):
        if x%i==0:
            print(i)

num =int(input("Enter the no. to find its factors : "))
FactorsOfTheNumber(num)

