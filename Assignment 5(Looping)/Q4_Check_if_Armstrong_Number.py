# Write a program to check if given number is Armstrong number or not.
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 
#         1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4 )

num = int(input("Enter a number : "))
temp = num
count = 0

while(num > 0):
    num //= 10
    count += 1
    
num = temp
sum = 0
while(num > 0):
    digit = num % 10
    num //= 10
    sum += digit ** count

if(sum == temp):
    print("Given number is an Armstrong number.")
else:
    print("Given number is not an Armstrong number.")