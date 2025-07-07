# This code calculates the cost of fencing a rectangular field and a circular field based on given dimensions and rate per unit length.

radius = 20
length = 50
breadth = 40
rate = 35

perimeter = 2*length + breadth + 3.14*radius
cost = (perimeter * rate)* 5                    # Total cost for 5 rounds of fencing    
print("Total cost of fencing the field is: Rs.", cost)                                       