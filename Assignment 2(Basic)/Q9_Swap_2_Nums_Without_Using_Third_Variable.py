# To swap two numbers without using third variable.

a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))

a, b = b, a

print("value in a : ",a, " value in b : ", b)