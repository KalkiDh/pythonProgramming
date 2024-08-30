a = [12, 45, 1, 9, 10]
a.reverse()#To reverse an list
a.sort()#To sort an array in Python.Pthon me array nahi bolte hai bulki list and listing bolte hai
print(a)
s=["Dron","Abheer","Ayush","Anay","Harsh","Adi"]
s.sort()
print(s)
tp=(1,34,43,12,12,1)# () means the list is a tuple. Which means it cannot be changed.But [] can be changed
#tp[2]=50
print(tp)
#Slicing in string list
ab=[12, 45, 1, 9, 10,15]
print(ab[0:6:2])
#In python it is not compulsory to have variables of same data type
#Example
abc=["Dron","Abheer","Ayush","Anay","Harsh","Samir",45,12,78]
#abc.sort()# List abc cannot be sorted because Python cannot distinguish between string and int
print(abc)
abcd=[12, 45, 1, 9, 10]
abcd.append(454)# To insert the element given at the last of the list
abcd.insert(2,0)# To insert any element in the list. First is the index and second is the element
abcd.remove(1)# To remove any element from the list
print(abcd)
print(max(abcd))# To find minimum in the the list
print(min(abcd))# To find maximum in the list
# Swaping two numbers
a=1
b=8
# Traditional way to swap
"""temp=a
a=b
b=temp"""
# Swaping in python
a,b=b,a
print(a,b)