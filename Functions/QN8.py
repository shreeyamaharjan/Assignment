def unique_list(ls):
    x = []
    for a in ls:
        if a not in x:
            x.append(a)
    return x


n = int(input("Enter size of the list:"))
lst = []
print("Enter the items of the list:")
for i in range(n):
    x = int(input())
    lst.append(x)

print(lst)
print("The unique list is :", unique_list(lst))
