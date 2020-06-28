n = int(input("Enter the size of list:"))
nums=[]
print("Enter the integer numbers:")
for i in range(n):
    a = int(input())
    nums.append(a)
print("The list of numbers : ", nums)
even_nums = list(filter(lambda x: x % 2 == 0, nums))
odd_nums = list(filter(lambda x: x % 2 != 0, nums))
print("The list of even numbers : ", even_nums)
print("The list of odd numbers : ", odd_nums)
