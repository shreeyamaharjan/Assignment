def checkkey(dict, key):
    if key in dict:
        print("Key already exists")
        print("key = {}  value = {}".format(key, dict[key]))

    else:
        print("Key doesnot exist")


dict = {}
n = int(input("Enter the number of elements : "))
for i in range(n):
    k = input("Enter key : ")
    v = input("Enter value : ")
    dict.update({k: v})
print(" Dictionary : ", dict)
key = input("Enter any number")
checkkey(dict, key)
