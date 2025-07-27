# program to calculate area of circle

def areaCircle():
    r = int(input("Enter the radius : "))
    pi = 22/7
    area = pi * (r * r)
    print(f"The area of circle is {area}")

areaCircle()