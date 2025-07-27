# program to check if a given number is Armstrong number or not. For each task create separate functions.

def count(num):
    cnt = 0
    while(num > 0):
        num //= 10
        cnt += 1
    return cnt

def isArmstrong(num, c):
    sum = 0
    temp = num
    while(num > 0):
        a = num % 10
        sum += a**c
        num //= 10
    if(temp == sum):
        return 1
    else:
        return 0

num = int(input("Enter the number : "))
c = count(num)
ans = isArmstrong(num, c)

if(ans):
    print(f"{num} is an armstrong number  . . .")
else:
    print(f"{num} is not armstrong number . . . !!")