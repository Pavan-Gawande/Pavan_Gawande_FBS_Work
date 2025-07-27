# program to find sum of following series using recursive functions:
# i. 1! + 2! + 3! + 4! +..... + n!

def factorial(num):
    if(num == 0):
        return 1
    return num*factorial(num-1)

def sumFact(n):
    if(n == 1):
        return 1
    else:
        return factorial(n) + sumFact(n-1)

num = int(input("Enter the value of n : "))
print(sumFact(num))
        