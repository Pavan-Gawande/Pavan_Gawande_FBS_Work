# program to find sum of n numbers using recursion.

def sumRec(num):
    if(num != 0):
        return sumRec(num - 1) + num
    else:
        return 0


num = int(input("Enter the number : "))
ans = sumRec(num)
print(f"sum of number till {num} is : {ans}")