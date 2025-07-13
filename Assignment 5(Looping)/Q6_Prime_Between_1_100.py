# program to print prime numbers between 1 to 100.

for num in range(2, 101):
    i = 2
    while(i <= num // 2):
        if(num % i == 0):
            break
        i += 1
    else:
        print(num)