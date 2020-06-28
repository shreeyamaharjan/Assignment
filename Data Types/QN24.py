lst = []
lst2 = [5,9,7]
n = int(input("Enter the size of  list : "))
print("Enter the elements : ")
for i in range(n):
    x = int(input())
    lst.append(x)
print("The original list : ", lst)
lst2.extend(lst)
print("The copied list :", lst2)
