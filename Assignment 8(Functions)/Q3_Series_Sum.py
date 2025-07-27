# program to find sum of following series using functions :
# a. 1+ 2 + 3 + 4+..... + n
# b. 1!+ 2! + 3! + 4!+..... + n!
# c. 1^1 + 2^2 + 3^3+ ...... n^n

def sumN(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    print(f"The sum of series till {n} is {sum}")
    
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

def factSum(n):
    sum = 0
    for i in range(1, n+1):
        sum += factorial(i)
    print(f"Sum of fact series till {n} is {sum}")

def powSum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i**i
    return sum


while(True):
    print("\n1) 1 + 2 + 3 + 4 + . . . + n")
    print("2) 1! + 2! + 3! + . . . . + n!")
    print("3) 1^1 + 2^2 + 3^3 + . . . + n^n")
    print("4) Exit")
    ch = int(input("Enter your choice : "))
    if(ch == 4):
        break
    elif(ch == 1):
        num = int(input("Enter the value for n : "))
        factSum(num)
    elif(ch == 2):
        num = int(input("Enter the value for n : "))
        factSum(num)
    elif(ch == 3):
        num = int(input("Enter the value for n : "))
        sum = powSum(num)
        print(f"Sum of series till {num} is {sum}")
    else:
        print("Invalid Input.......!!")
