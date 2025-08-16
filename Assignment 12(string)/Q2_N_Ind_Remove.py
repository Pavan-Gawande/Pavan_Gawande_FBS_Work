# Program to Remove the nth Index Character from a Non-Empty String

st = input("Enter the string : ")
n = int(input("Enter the index : "))

output = st[:n] + st[n+1:]
print("String after removal : ", output)