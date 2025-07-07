# To find if a 3-digit number is such that the first digit is twice the second and half of the third.

num = int(input("Enter a 3 digit number: "))
a = num // 100
b = (num // 10) % 10
c = num % 10
if(a == 2*b and 2*a == c):
    print("Yes, you have done it!")
else:
    print("Please try next time!")