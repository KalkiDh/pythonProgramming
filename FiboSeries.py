nTerms=int(input("Enter the no. of terms you want in the series : "))

n1=0
n2=1
count=0

if nTerms<=0:
    print("Enter a positive number .")
elif nTerms==1:
    print("Fibonacci series till ",nTerms," : 0")
else:
    print("Fibonacci series till ", nTerms, " : ")
    while count<nTerms:
        print(n1,end=",")
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
print()
