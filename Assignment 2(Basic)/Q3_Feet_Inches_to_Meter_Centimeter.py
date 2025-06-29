# To convert distance in feet and inches to meter and centimeter respectively.

feet = float(input("Enter the distance in feet to get meter : "))
mtr = feet*0.3048
print("length in feet : ",feet, " is equal to :", mtr, " meter")

inches = float(input("\nEnter the distance in inches to get centimeter : "))
cm = inches*2.54
print("length in inches : ", inches, " is equal to : ",cm," Centimeter")