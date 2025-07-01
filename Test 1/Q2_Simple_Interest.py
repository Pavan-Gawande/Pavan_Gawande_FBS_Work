# To find the simple interest, using principal, rate and time.

principal = int(input("Enter the principal amount : "))
rate = int(input("Enter the rate per year (in percent) : "))
time = int(input("Enter the time in months : "))

time /= 12     # convert time to years

simple_interest = (principal*rate*time)/100

print("The simple interest is : ",simple_interest)