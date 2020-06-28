def add(lst):
    count = 0
    for num in lst:
        count += num
    return count


n = int(input("Enter the size of the list:"))
lst = []
print("Enter the elements of the list:")

for i in range(n):
    x = int(input())
    lst.append(x)
print(lst)

print("The sum of all numbers in the list is", add(lst))
