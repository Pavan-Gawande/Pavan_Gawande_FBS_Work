# Write a program to accept an integer amount from user and tell minimum
# number of notes needed for representing that amount. (Use looping to optimize
# the problem)

amount = int(input("Enter the amount: "))
count = 0

while(amount > 0):
    if(amount >= 500):
        note = 500
    elif(amount >= 200):
        note = 200
    elif(amount >= 100):
        note = 100
    elif(amount >= 50):
        note = 50
    elif(amount >= 20):
        note = 20
    else:
        note = 10
    
    count += amount // note
    amount %= note

print("Minimum number of notes needed is: ", count)