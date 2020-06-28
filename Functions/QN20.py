from array import *
arr1=[]
arr2=[]
n=int(input("Enter the size of first array : "))
n1=int(input("Enter the size of first array : "))
print("Enter first array")
for i in range(n):
     x=int(input())
     arr1.append(x)
print ("Enter second array")
for i in range(n1):
     y=int(input())
     arr2.append(y)
print("The first array :",arr1)
print("The second array :",arr2)
result =list(filter(lambda x: x in arr1,arr2))
print("The result of intersection is :",result)

