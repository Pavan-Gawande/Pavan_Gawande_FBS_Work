# program to reverse a given number using recursive function.

def reverse(num, rev):
    if(num != 0):
        a = num%10
        rev = rev*10 + a
        return reverse(num//10, rev)
    else:
        return rev

num = int(input("Enter the number : "))
print(f"Reverse of {num} is {reverse(num, 0)}")