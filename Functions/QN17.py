result = (lambda c: print("The string starts with given character") if c.startswith(ch) else print(
    "The string doesnot start with given character"))

ch = input("Enter any character : ")
string = str(input("Enter any string : "))
print(result(string))
