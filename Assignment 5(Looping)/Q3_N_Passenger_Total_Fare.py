# Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
#   a. Children below 12 = 30% discount
#   b. Senior citizen (above 59) = 50% discount
#   c. Others need to pay full.

n = int(input("Enter the number of passengers: "))
fare = int(input("Enter the fare per passenger: "))
total_fare = 0
for i in range(n):
    age = int(input(f'Enter the age of passenger {i+1} : '))
    if( age < 12 ):
        total_fare += fare * 0.7          # 30% discount for children
    elif( age > 59 ):
        total_fare += fare * 0.5          # 50% discount for senior citizens 
    else:
        total_fare += fare

print("The total fare is : ", total_fare)