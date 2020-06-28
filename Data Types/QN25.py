dict = {}
n = int(input("Enter the number of elements : "))
for i in range(n):
    k = input("Enter key : ")
    v = input("Enter value : ")
    dict.update({k: v})

if not dict:
    print("Dictionary is empty")
else:
    print("Dictionary is not empty")
    print(dict)
