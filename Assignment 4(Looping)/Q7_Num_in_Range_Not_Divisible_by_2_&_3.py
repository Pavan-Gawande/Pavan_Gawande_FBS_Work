# program to print all integers upto n that aren’t divisible by 2 and 3.

num = int(input("Enter a number: "))
i = 1
while(i <= num):
    if(i % 2 != 0 and i % 3 != 0):
        print(i)
    i += 1
