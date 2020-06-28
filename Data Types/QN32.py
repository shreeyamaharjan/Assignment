dict = {}

n=int(input("Enter the value for n : "))
for i in range(n+1):
    if i != 0:
         k = i
         v = i**2
         dict.update({k : v})
print(dict)