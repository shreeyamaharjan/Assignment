lst = []
n = int(input("Enter the size of  list : "))
print("Enter the elements : ")
for i in range(n):
    x = str(input())
    lst.append(x)
print(lst)

count = 0
for i in lst:
    if len(i) >= 2 and i[0] == i[-1]:
        count += 1
print(count)
