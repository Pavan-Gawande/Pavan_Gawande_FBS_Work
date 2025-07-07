# To calculate the cost of painting the walls of a room

height = int(input("Enter the height of the wall: "))
width = int(input("Enter the width of the wall: "))

rate = int(input("Enter the rate per square unit: "))

area = (height * width)*4                                   # Total area for 4 walls
cost = area * rate                                          # Total cost for painting the walls
print("Total cost of painting the walls is: Rs.", cost)     # Display the total