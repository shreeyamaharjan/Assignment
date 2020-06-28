lst1 = []
n1 = int(input("Enter the size of first list : "))
print("Enter the elements : ")
for i in range(n1):
    x = int(input())
    lst1.append(x)
print(lst1)

lst2 = []
n2 = int(input("Enter the size of second list : "))
print("Enter the elements : ")
for i in range(n2):
    x = int(input())
    lst2.append(x)
print(lst2)
lst1[-1:]=lst2
print(lst1)

