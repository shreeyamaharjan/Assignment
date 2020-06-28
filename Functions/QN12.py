def compute(n):
    return lambda x: x * n

n=int(input("Enter any unknown number: "))
num = int(input("Enter any number : "))
result=compute(n)
print("The result is = ", result(num))
