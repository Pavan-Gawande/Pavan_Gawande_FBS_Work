# program to print all numbers in a range divisible by a given number.

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
x = int(input("Enter a number to check the divisibility : "))

i = start
while(i <= end):
    if(i % x == 0):
        print(i)
    i += 1