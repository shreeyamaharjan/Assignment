def case_count(st):
    c1 = 0
    c2 = 0
    for i in range(n):
        if string[i].isupper():
            c1 += 1

        elif string[i].islower():
            c2 += 1
    print("The number of uppercase letters :", c1)
    print("The number of lowercase letters :", c2)


string = input("Enter any string :")
n = len(string)
case_count(string)
