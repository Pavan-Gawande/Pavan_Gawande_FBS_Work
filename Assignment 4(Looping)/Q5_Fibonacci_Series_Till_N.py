# program to print Fibonacci series upto n.

num = int(input("Enter a number : "))
a = 1
b = 0

while(b <= num):
    print(b)
    b, a = a+b, b
