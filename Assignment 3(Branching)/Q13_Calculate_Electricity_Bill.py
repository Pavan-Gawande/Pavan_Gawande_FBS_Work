# program to input electricity unit charges and calculate total electricity bill
# according to the given condition:
#   For first 50 units Rs. 0.50/unit
#   For next 100 units Rs. 0.75/unit
#   For next 100 units Rs. 1.20/unit
#   For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill

unit = int(input("Enter the units : "))
cost = 0
if(unit < 0):
    print("Units cannot be negative...")
elif(unit <= 50):
    cost = unit*0.5
elif(unit <= 150):
    cost = 50*0.5
    unit -= 50
    cost += unit*0.75
elif(unit <= 250):
    cost = 50*0.5
    unit -= 50
    cost += 100*0.75
    unit -= 100
    cost += unit*1.2
elif(unit > 250):
    cost = 50*0.5
    unit -= 50
    cost += 100*0.75
    unit -= 100
    cost += 100*1.2
    unit -= 100
    cost += unit*1.5
cost *=1.2
print("Cost : ",cost)