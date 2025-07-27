# program to check if given number is Armstrong or not using recursive function.

def count(n):
    if(n < 10):
        return 1
    else:
        return count(n//10) + 1

def armstrong(num, cnt):
    if(num == 0):
        return 0
    else:
        return (num%10)**cnt + armstrong(num//10, cnt)

num = int(input("Enter a number : "))
c = count(num)
ans = armstrong(num, c)

if(num == ans):
    print(f"{num} is an armstrong number...")
else:
    print(f"{num} is not an armstrong...!!")