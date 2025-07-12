# program to check if person is eligible to marry or not (male age >=21 and female age>=18)

gender = input("Enter your gender (m/f): ")
age = int(input("Enter your age : "))

if( gender == "m" and age>=21 ):
    print("Congrats, you can marry...")
elif( gender == "f" and age>=18 ):
    print("Congrats, you can marry...")
elif( gender not in "mf"):
    print("Invalid input....!!!")
else:
    print("Sorry, you can not marry...")