dict = {}

for i in range(16):
    if i != 0:
         k = i
         v = i**2
         dict.update({k : v})
print("The Dictionary where the keys are numbers between 1 and 15 and the values are square of keys is \n", dict)