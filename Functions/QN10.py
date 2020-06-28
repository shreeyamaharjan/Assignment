def even_numbers(num):
    x=[]
    for i in num:
        if i%2 ==0:
            x.append(i)
    return x

n=int(input("Enter size of list : "))
lst=[]
print("Enter the list of items:")
for i in range(n):
    a=int(input())
    lst.append((a))

print(lst)
print ("The even numbers are :",even_numbers(lst))

