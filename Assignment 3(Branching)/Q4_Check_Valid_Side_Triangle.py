# program to input all sides of a triangle and check whether triangle is valid or not

side1 = int(input("Enter 1st side of triangle : "))
side2 = int(input("Enter 2nd side of triangle : "))
side3 = int(input("Enter 3rd side of triangle : "))

if( (side1+side2)==side3 or (side1+side3)==side2 or (side3+side2)==side1 ):
    print("Given triangle is not valid triangle...")
else:
    print("Given triangle is valid triangle...")