# To find the reverse of the three digit number

num = int(input("Enter the 3 digit number : "))

a = num % 10
num //= 10

b = num % 10
c = num // 10

reverse = a*100 + b*10 + c

print("The reverse is : ",reverse)