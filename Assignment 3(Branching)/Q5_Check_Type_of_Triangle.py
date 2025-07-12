# program to check whether the triangle is equilateral, isosceles or scalene triangle.

a = int(input("Enter the first side of triangle : "))
b = int(input("Enter the second side of triangle :  "))
c = int(input("Enter the third side of triangle : "))

if( a == b == c):
    print("Given triangle is equilateral triangle...")
elif( a==b or b==c or a==c):
    print("Given triangle is isosceles triangle...")
else:
    print("Given triangle is scalar triangle...")                       