# program to check if user has entered correct userid and password.

username = input("Enter the username : ")
password = input("Enter the password : ")

if( username == "admin" and password == "admin@123"):
    print("Login Successful...")
else:
    print("Invalid Credentials, Failed to Login...")