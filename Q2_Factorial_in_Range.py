# program to print factorial of numbers in the given range

def factorial(n):
    if(n == 1):
        return 1
    else:
        return n*factorial(n-1)

start = int(input("Enter the start of the range : "))
end = int(input("Enter the end of the range : "))

fact = factorial(start)
for i in range(start, end+1):
    print(f'factorial of {i} is {fact}')
    fact *= i+1
