def maxm(a, b, c):
    if (a > b) & (a > c):
        return a
    elif (b > a) & (b > c):
        return b
    else:
        return c


a = input("Enter any number :")
b = input("Enter any number :")
c = input("Enter any number :")

print("The maximum of three numbers is:", maxm(a, b, c))
