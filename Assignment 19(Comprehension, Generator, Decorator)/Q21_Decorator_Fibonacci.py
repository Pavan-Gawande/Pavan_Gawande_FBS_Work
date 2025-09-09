
def decor(func):
    mem= {}
    def wrapper(n):
        if(n in mem):
            print("Getting value from memory...")
            return mem[n]
        else:
            print("Calculating result...")
            res = func(n)
            mem[n] = res
            return res
    return wrapper

@decor
def factorial(n):
    fact = 1
    for i in range(2, n+1):
        fact *= i
    return fact

print(factorial(5))
print(factorial(4))
print(factorial(5))
