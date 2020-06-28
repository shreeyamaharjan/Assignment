lst = []
n = int(input("Enter the size of  list : "))
print("Enter the elements : ")
for i in range(n):
    x = int(input())
    lst.append(x)
print(lst)

tst = []
for i in lst:
    if i not in tst:
        tst.append(i)
print("The list after removing duplicates is : ", tst)
