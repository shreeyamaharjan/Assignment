def test_range(n):
    if n in range(2, 11):
        print("The number {} is in the range".format(n))
    else:
        print("The number {} is not in the range".format(n))


num = int(input("Enter any number:"))
test_range(num)
