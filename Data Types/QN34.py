dict = {}
n = int(input("Enter the number of elements : "))
for i in range(n):
    k = input("Enter key : ")
    v = input("Enter value : ")
    dict.update({k: v})
print("First Dictionary : ", dict)

dict1 = {}
n = int(input("Enter the number of elements : "))
for i in range(n):
    k = input("Enter key : ")
    v = input("Enter value : ")
    dict1.update({k: v})
print("Second Dictionary :", dict1)
dict.update(dict1)
print("The result after merging two dictionaries is : ", dict)
