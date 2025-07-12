#program to check if the given number is positive or negative.

num = int(input("Enter a number : "))
if(num < 0):
    print("Given number is negative")
elif(num > 0):
    print("Given number is positive")
else:
    print("Given number is neutral")