from functools import reduce

fibo = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])
num = int(input("Enter the value for n"))
print("Fibonacci series upto {} is :")
print(fibo(num))
