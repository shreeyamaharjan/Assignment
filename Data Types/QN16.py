lst = []
n = int(input("Enter the size of  list : "))
print("Enter the elements : ")
for i in range(n):
    x = int(input())
    lst.append(x)
print(lst)
sum = 0
for i in range(n):
    sum = sum + lst[i]
print("The product of all items in the list is : ", sum)
