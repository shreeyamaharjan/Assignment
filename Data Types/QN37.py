dict = {'a': 4, 'b': 1, 'c': 9, 'd': 5}
print("The dictionary is:", dict)
product = 1
for i in dict:
    product = product * dict[i]
print("The product of all items in dictionary is :", product)
