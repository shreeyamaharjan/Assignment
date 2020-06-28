dict = {}
n = int(input("Enter the number of elements : "))
for i in range(n):
    k = input("Enter key : ")
    v = input("Enter value : ")
    dict.update({k: v})
print(dict)

for k, v in dict.items():
    print(k, "\t" + v)
