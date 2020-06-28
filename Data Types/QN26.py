lst = []
n = int(input("Enter the size of  list : "))
print("Enter the elements : ")
for i in range(n):
    x = int(input())
    lst.append(x)
print(lst)

string = str(input("Enter an string : "))
string += '{0}'
print([string.format(i) for i in lst])
