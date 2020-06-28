tup1=[]
n=int(input("Enter the size of list : "))
print("Enter the elements : ")
for i in range(n):
    a=int(input())
    tup1.append(a)
print(tup1)
print(type(tup1))
tup1=tuple(tup1)
print(type(tup1))
print(tup1)
tup1=tup1 +(9,15,50)
print(tup1)