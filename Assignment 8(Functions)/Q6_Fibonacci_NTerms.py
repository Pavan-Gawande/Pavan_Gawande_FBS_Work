# program to print the following Fibonacci series using functions:
# 1 1 2 3 5 8 n terms

def fab(n):
    a = -1
    b = 1
    for i in range(n):
        c = a+b
        print(c)
        a = b
        b = c

n = int(input("Enter the no. of terms : "))
fab(n)