# program to find sum of digits of a number.

def sumDigit(num):
    temp = num
    sum = 0
    while(num > 0):
        sum += num%10
        num //= 10
    print(f"Sum of digits of {temp} is {sum}")

num = int(input("Enter the number : "))
sumDigit(num)