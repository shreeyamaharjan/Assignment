n = int(input("Enter the size of the list : "))
lst = []
print("Enter the list elements : ")
for i in range(n):
    x = int(input())
    lst.append((x))

print("The list is : ", lst)
print("The list is converted into tuple as :", tuple(lst))
