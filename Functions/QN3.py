def multiply(lst):
    count = 1
    for num in lst:
        count = count * num
    return count


n = int(input("Enter the size of the list:"))
lst = []
print("Enter the elements of the list:")

for i in range(n):
    x = int(input())
    lst.append(x)
print(lst)

print("The multiplication of all numbers in the list is", multiply(lst))
