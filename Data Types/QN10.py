string =str(input("Enter any string : "))
result=""
for i in range(len(string)):
    if i%2==0:
        result=result+string[i]
print ("String after removing odd index : ",result)