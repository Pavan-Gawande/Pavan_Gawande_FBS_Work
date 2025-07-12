# program to check if given number Strong Number.

num = int(input("Enter a number: "))
sum = 0
temp = num

while(num != 0):
    a = num % 10
    num //= 10
    fact = 1
    i = 1
    while(i <= a):
        fact *= i
        i += 1
    sum += fact
if(sum == temp):
    print("Strong number")
else: 
    print("Not a strong number")