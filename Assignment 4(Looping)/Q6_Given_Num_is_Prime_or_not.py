# program to check if a given number is prime number or not.

num = int(input("Enter a number: "))
if(num < 2):
    print("Not a prime number")
else:
    i = 2
    while(i <= num//2):
        if(num % i == 0):
            print("Not a prime number")
            break
        i += 1
    else:
        print("Prime number")