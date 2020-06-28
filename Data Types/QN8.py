string = str(input("Enter any string : "))
n = int(input("Enter value for n : "))
first = string[:n]
last = string[n + 1:]
print(''.join(first + last))
