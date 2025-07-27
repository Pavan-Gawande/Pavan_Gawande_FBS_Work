# program to check if entered number is a palindrome or not.

def isPalindrome(num):
    temp = num
    rev = 0
    while(num > 0):
        rev = rev*10 + num%10
        num //= 10
    if(temp == rev):
        print(f"{temp} is a palindrome ...")
    else:
        print(f"{temp} is not a palidrome ... !!")

num = int(input("Enter a number :"))
isPalindrome(num)