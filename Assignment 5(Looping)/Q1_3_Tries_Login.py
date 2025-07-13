# program to prompt user to enter userid and password. If Id and password is 
# incorrect give him chance to re-enter the credentials. Let him try 3 times.
# After that program to terminate.

user = ""
password = ""
i = 3
while(i>0):
    user = input("Enter your username: ")
    password = input("Enter your password: ")
    if user == "admin" and password == "admin@123":
        print("Welcome to the system...")
        break
    else:
        print("Incorrect username or password. Please try again.")
        if( i == 1):
            print("You have no more chances left.")
        else:
            print(f"You have {i-1} chances left.")
    i -= 1