# program to print sum of series upto n.

num = int(input("Enter a number : "))
sum = 0
i = 1

while(i <= num):
    sum += i
    i += 1
print(sum)