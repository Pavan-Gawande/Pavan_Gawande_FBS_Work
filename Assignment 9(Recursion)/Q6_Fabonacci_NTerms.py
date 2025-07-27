# program to print Fibonacci series using recursion.

def fibo(a, b, num):
    if(num != 0):
        c = a + b
        print(c)
        fibo(b, c, num-1)

n = int(input("Enter the number : "))
fibo(-1, 1, n)