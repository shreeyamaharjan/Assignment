lst = []
n = int(input("Enter the size of  list : "))
print("Enter the elements : ")
for i in range(n):
    x = int(input())
    lst.append(x)
print(lst)

least = lst[0]
for i in range(n):
    if lst[i] < least:
        least = lst[i]
print("The smallest number from the list is : ", least)
