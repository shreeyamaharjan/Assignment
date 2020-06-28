n = int(input("Enter the size of list:"))
nums = []
print("Enter the integer numbers:")
for i in range(n):
    a = int(input())
    nums.append(a)
print("The list of numbers : ", nums)

squares = list(map(lambda x: x ** 2, nums))
print("The squares of every number in list is : ", squares)

cubes = list(map(lambda x: pow(x, 3), nums))
print("The cube of every number in list is : ", cubes)
