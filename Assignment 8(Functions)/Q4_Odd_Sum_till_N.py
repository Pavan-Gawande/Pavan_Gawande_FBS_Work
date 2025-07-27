# program to print sum of all odd numbers between 1 to n

def oddSum():
    n = int(input("Enter the value of n : "))
    sum = 0
    for i in range(1, n+1):
        if(i%2 == 1):
            sum += i
    print(f"Sum of odd numbers till {n} is {sum}")

oddSum()