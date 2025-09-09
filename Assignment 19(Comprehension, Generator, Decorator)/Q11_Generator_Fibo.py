# We want to generate Fibonacci numbers up to a certain limit.
# Instead of computing and storing the entire sequence in memory,
# create generator to yield Fibonacci numbers one by one,
# conserving memory and allowing for easy iteration.

def fibo(limit):
    a, b = 0, 1
    while(a <= limit):
        yield a
        a, b = b, a+b

n = int(input("Enter the no. of terms : "))
for i in fibo(n):
    print(i, end=" ")
