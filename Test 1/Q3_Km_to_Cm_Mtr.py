# To convert distance in km to m and cm.

Distance_Km = int(input("Enter the distance (in km) : "))

Distance_Mtr = Distance_Km*1000        #convert from km to mtr, 1km = 1000mtr

Distance_Cm = Distance_Mtr*100         #convert from mtr to cm, 1mtr = 100cm

print("Distance in meter is : ",Distance_Mtr)
print("Distance in centimeter is : ",Distance_Cm)
