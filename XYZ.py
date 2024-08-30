"""print("Enter a number : ")
inpnum=input()
print(int(inpnum)+10)
a=23
b=10
a,b=b,a
print(a,b)
a=[12,13,1313,134,33,3,45]
a.sort()
a.reverse()
a.pop(3)
print(a)
b=(1,2,8,5,45,515,2,5,10582)

print(a,b)
print(type(b))"""

#Program to accept age and display if eligible to drive or not.
print("Enter your age : ");
age=int(input())
if age<7 or age>100:
    print("Enter a valid age.")
elif age ==18:
    print("You are eligible to drive.")
else:
    print("You are not eligible to drive.")