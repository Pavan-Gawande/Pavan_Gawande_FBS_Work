# program to check if given 3 digit number is a palindrome or not.

num = int(input("Enter a 3 digit number : "))

h_place = num//100
u_place = num%10

if(h_place == u_place):
    print("Given 3 digit number is a palindrome...")
else:
    print("Given 3 digit number is not a palindrome...!!")