# To find area and perimeter of the figure
# ____________
#|             \
#|              |
#|____________ /

length = int(input("Enter the length : "))
breadth = int(input("Enter the breadth : "))
radius = int(input("Enter the radius : "))

pi = 3.14

perimeter = breadth + 2*length + pi*radius

area = length*breadth + pi*(radius**2)

print("Perimeter of this figure is : ", perimeter)
print("Area of the figure is : ", area)