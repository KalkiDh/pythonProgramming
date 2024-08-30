dis=int(input("Enter total distance travelled in kilometres : "))
wait=int(input("Enter total time of waiting in mins : "))
amt=0.0


if dis>0 and dis<=4 :
    amt=99.0
else:
    amt=(99.0+((dis-4)*21.0))

waitamt=(wait*2.0)
totalamt=amt+waitamt
if dis<0 or wait<0 :
    print("Enter a valid number ")
else:
    print("Amount to be paid : ",totalamt)
print("Thank you")

