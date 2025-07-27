# program to find sum of digits using recursion.

def sumOfDigit(num, sum):
    if(num != 0):
        a = num % 10
        return a + sumOfDigit(num//10, sum)
    else:
        return 0

num = int(input("Enter the number : "))
print(f"Sum of digits of {num} is {sumOfDigit(num, 0)}")