string1 = str(input("Enter any string :"))
if len(string1) < 2:
    print("The length of string must be greater than 2")
else:
    print(string1[:2] + string1[-2:])
