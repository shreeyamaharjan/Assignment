lst = []
n = int(input("Enter the size of  list : "))
print("Enter the elements : ")
for i in range(n):
    x = int(input())
    lst.append(x)
print(lst)
product = 1
for i in range(n):
    product = product * lst[i]
print("The product of all items in the list is : ", product)
