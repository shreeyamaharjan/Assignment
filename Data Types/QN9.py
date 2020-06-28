string = str(input("Enter any string : "))
first = string[0]
last = string[-1]
mid = string[1:-1]
print(''.join(last + mid + first))
