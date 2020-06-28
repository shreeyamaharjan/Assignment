string1 = str(input("Enter any string : "))
count = {}
for x in string1:
    if x in count:
        count[x] += 1

    else:
        count[x] = 1
print("Count of all characters : \n" + str(count))
