# To calculate the cost of painting the walls(interior and exterior)
#  _________
# |         |
# |         | _________
# |         ||         |
# |_________||         |
#            |         |
#            |_________|

Room_Area = int(input("Enter the area of both rooms : "))
CostInt = int(input("Enter the cost of painting for interior wall : "))
CostExt = int(input("Enter the cost of painting for exterior wall : "))

Wall_Length = (Room_Area/2)**0.5                    # as room_area = 2(side*side)
Price_Interior = (Wall_Length*CostInt)*8
Price_Exterior = (Wall_Length*CostExt)*8

print("The total cost for painting the interior wall : ",Price_Interior)
print("The total cost for painting the exterior wall : ", Price_Exterior)