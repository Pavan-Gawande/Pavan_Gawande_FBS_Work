# program to print first n prime numbers.

limit = int(input("Enter a number : "))
count = 0
num = 2

while(count < limit):
    i = 2
    while(i <= num//2):
        if(num % i == 0):
            break
        i += 1
    else:
        print(num)
        count += 1
    num += 1