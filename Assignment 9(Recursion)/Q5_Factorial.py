# program to find factorial using recursion.

def factorial(num):
    if(num == 0):
        return 1
    else:
        return num*factorial(num-1)

n = int(input("Enter a number to find factorial : "))
print(f'The factorial of {n} is {factorial(n)}')