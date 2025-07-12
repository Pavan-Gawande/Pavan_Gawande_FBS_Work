# program to input angles of a triangle and check whether triangle is valid or not.

ang1 = int(input("Enter the 1st angle of triangle : "))
ang2 = int(input("Enter the 2nd angle of triangle : "))
ang3 = int(input("Enter the 3rd angle of triangle : "))

if( (ang1+ang2+ang3) == 180):
    if(ang1==0 or ang2==0 or ang3==0):
        print("Angle cannot be zero...")
    else:
        print("The triangle is valid...")
else:
    print("The given triangle is not valid...")