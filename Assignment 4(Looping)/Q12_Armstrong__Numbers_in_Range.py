# program to print Armstrong number within a given range

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
i = start
while(i <= end):
    count = 0
    num = i
    while(num != 0):
        num //=10
        count += 1
    num = i
    sum = 0
    while(num != 0):
        a = num % 10
        num //= 10
        sum += a ** count
    if(sum == i):
        print(i)
    i += 1