# program to check whether a number is prime or not using recursion.

def is_prime(num, start):
    if(start < num):
        if(num % start == 0):
            return 0
        else:
            return is_prime(num, start+1)
    else:
        return 1

num = int(input("Enter a number to check if prime : "))

if(num < 2):
    print(f"{num} is not prime number...")
else:
    ans = is_prime(num, 2)
    if(ans):
        print(f"{num} is a prime number...")
    else:
        print(f"{num} is not a prime number...!!")