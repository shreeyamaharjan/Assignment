num = int(input("Enter any number:"))
if num > 1:
    for i in range(2, num):
        if (num % i) != 0:
            print("{} is a prime number".format(num))
            break

        else:
            print("{} is not a prime number".format(num))
            break
else:
    print("{} is not a prime number".format(num))
