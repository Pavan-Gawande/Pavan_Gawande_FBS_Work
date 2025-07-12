# program to prompt user to enter userid and password. After verifying
# userid and password display a 4 digit random number and ask user to enter the
# same. If user enters the same number then show him success message otherwise
# failed. (Something like captcha)

import random
username = input("Enter the username : ")
password = input("Enter the password : ")

if( username == "admin" and password == "admin@123"):
    captcha = random.randint(1000, 9999)
    print("Captcha : ", captcha)
    cap = int(input("Enter the Captcha : "))
    if(captcha == cap):
        print("Login Successful...")
    else:
        print("Failed to Login...")
else:
    print("Invalid Credentials, Failed to Login...")