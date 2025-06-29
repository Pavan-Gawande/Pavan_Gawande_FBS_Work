# To find the sum of digits in 3 digit number

Num = int(input("Enter the 3 digit number : "))

A = Num % 10
Num //= 10
B = Num % 10
C = Num //10
Sum = A + B + C

print("The sum of digits is : ",Sum)