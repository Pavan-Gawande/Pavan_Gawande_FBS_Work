#To print the first n prime numbers

n = int(input("Enter the value of n : "))
p = 2
while(n > 0):
    for i in range(2, p//2 +1):
        if(p%i == 0):
            break
    else:
        print(p)
        n -= 1
    p += 1
    