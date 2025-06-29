# To swap two numbers using third variable.

num1 = int(input("Enter the first number(a) : "))
num2 = int(input("Enter the second number(b) : "))

temp = num1
num1 = num2
num2 = temp

print("value in a : ",num1, " value in b : ", num2)
