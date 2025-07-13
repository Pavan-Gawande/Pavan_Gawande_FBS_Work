# Write a program to solve the following series :
# a. 1! + 2! + 3! + 4! + .....n!
# b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
# d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
# e. x - x2/3 + x3/5 - x4/7 + .... to n terms

while True:
    print("\nChoose the series to solve:")
    print("1. 1! + 2! + 3! + ... + n!")
    print("2. N + N^2 + N^3 + ... + N^N")
    print("3. Geometric series from 1 to n with common ratio 2")
    print("4. S = a + a^2/2 + a^3/3 + ... + a^10/10")
    print("5. x - x^2/3 + x^3/5 - x^4/7 + ... to n terms")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")
    
    if choice == '6':
        break

    elif( choice == '1'):
        n = int(input("Enter the number of terms : "))
        sum = 0
        fact = 1
        i = 1
        while(i <= n):
            fact = fact * i
            sum += fact
            i += 1
        print("The sum of the series is : ", sum)
    
    elif( choice == '2'):
        n = int(input("Enter Value of N : "))
        sum = 0
        for i in range(1, n+1):
            sum += n**i
        print("The sum of the series is : ", sum)
        
    elif( choice == '3'):
        n = int(input("Enter the number of terms : "))
        sum = 0
        a = 1
        for i in range(n):
            a = 2**i
            sum += a
        print("The sum of the series is : ", sum)
    
    elif( choice == '4'):
        a = int(input("Enter the value of a : "))
        sum = 0
        for i in range(1, 11):
            sum += (a**i)/i
        print("The sum of the series is : ", sum)
    
    elif( choice == '5'):
        n = int(input("Enter the number of terms : "))
        x = int(input("Enter the value of x : "))
        sum = 0
        for i in range(n):
            if(i % 2 == 0):
                sum += (x**(i+1))/(i*2 + 1)
            else:
                sum -= (x**(i+1))/(i*2 + 1)
        print("The sum of the series is : ", sum)
    
    else:
        print("Invalid choice, please try again.")

