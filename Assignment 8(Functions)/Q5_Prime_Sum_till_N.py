# program to print sum of all prime numbers between 1 to n

def isPrime(n):
    for i in range(2, n):
        if(n%i == 0):
            return 0
    return 1

n = int(input("Enter the value of num : "))
sum = 0
for i in range(2, n+1):
    if(isPrime(i)):
        sum += i

print(f"Sum of prime numbers till {n} is {sum}")